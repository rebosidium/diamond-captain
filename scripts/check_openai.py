#!/usr/bin/env python3
"""Read the generated plugin with Codex app-server; no install or model request."""
from __future__ import annotations

import io
import json
import os
import selectors
import subprocess
import tempfile
import time
import zipfile
from pathlib import Path

from build_distribution import ROOT, build


def main() -> None:
    _, manifest, archive = build(ROOT, "openai")
    version = subprocess.check_output(["codex", "--version"], text=True).strip()
    with tempfile.TemporaryDirectory(prefix="dr-openai-check-") as directory:
        temporary = Path(directory)
        package = temporary / "package"
        with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
            bundle.extractall(package)
        marketplace = (package / ".agents/plugins/marketplace.json").resolve()
        initialize = {"id": 1, "method": "initialize", "params": {
            "clientInfo": {"name": "dr-distribution-check", "version": "0.1.0"},
            "capabilities": {"experimentalApi": True},
        }}
        read = {"id": 2, "method": "plugin/read", "params": {
            "marketplacePath": str(marketplace), "pluginName": "diamond-captain",
        }}
        with (temporary / "server.log").open("wb") as errors:
            process = subprocess.Popen(
                ["codex", "-c", "analytics.enabled=false", "-c", "feedback.enabled=false",
                 "app-server", "--stdio"], cwd=temporary, stdin=subprocess.PIPE,
                stdout=subprocess.PIPE, stderr=errors, bufsize=0,
            )

            def send(message: dict) -> None:
                process.stdin.write((json.dumps(message) + "\n").encode())
                process.stdin.flush()

            try:
                send(initialize)
                buffer = b""
                plugin = None
                deadline = time.monotonic() + 45
                with selectors.DefaultSelector() as selector:
                    selector.register(process.stdout, selectors.EVENT_READ)
                    while plugin is None and time.monotonic() < deadline:
                        if not selector.select(1):
                            continue
                        data = os.read(process.stdout.fileno(), 65536)
                        if not data:
                            raise RuntimeError("Codex app-server closed before returning the plugin")
                        buffer += data
                        while b"\n" in buffer:
                            line, buffer = buffer.split(b"\n", 1)
                            message = json.loads(line)
                            if message.get("id") in (1, 2) and "error" in message:
                                raise RuntimeError(f"Codex rejected the check: {message['error']['message']}")
                            if message.get("id") == 1:
                                send({"method": "initialized", "params": {}})
                                send(read)
                            elif message.get("id") == 2:
                                plugin = message["result"]["plugin"]
                if plugin is None:
                    raise TimeoutError("Codex plugin/read did not finish within 45 seconds")
            finally:
                process.terminate()
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait(timeout=5)
                process.stdin.close()
                process.stdout.close()
        expected = (package / manifest["distribution"]["skill_root"] / "SKILL.md").resolve()
        skills = plugin["skills"]
        if plugin["summary"]["name"] != "diamond-captain" or \
                plugin["summary"]["localVersion"] != manifest["distribution"]["version"]:
            raise ValueError("Codex returned another plugin or distribution version")
        if len(skills) != 1 or skills[0]["name"] != "diamond-captain:diamond-captain" or \
                Path(skills[0]["path"]).resolve() != expected:
            raise ValueError("Codex did not discover exactly the packaged skill")
        if plugin["hooks"] or plugin["mcpServers"]:
            raise ValueError("Unexpected executable plugin components")
        print(f"{version}: PASS, portable manifest and local marketplace parsed")
        print("plugin/read found exactly one diamond-captain:diamond-captain at the packaged path")
        print(f"Core {manifest['core']['version']}, SHA-256 {manifest['core']['content_sha256']}")
        print("Read-only app-server check; no model invocation, plugin install or settings changes")


if __name__ == "__main__":
    main()
