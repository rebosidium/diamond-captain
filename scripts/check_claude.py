#!/usr/bin/env python3
"""Validate and load the plugin with an isolated Claude Code CLI, without a model."""
from __future__ import annotations

import argparse
import io
import json
import os
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

from build_distribution import ROOT, build

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cli", default=shutil.which("claude"),
                        help="installed Claude Code executable; defaults to claude on PATH")
    args = parser.parse_args()
    if not args.cli:
        parser.error("Claude Code is not on PATH; pass --cli /absolute/path/to/the/installed/claude")
    _, manifest, archive = build(ROOT, "claude-code")
    with tempfile.TemporaryDirectory(prefix="dr-claude-check-") as directory:
        temporary = Path(directory)
        package, project = temporary / "package", temporary / "project"
        project.mkdir()
        archive_path = temporary / "plugin.zip"
        archive_path.write_bytes(archive)
        with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
            bundle.extractall(package)
        env = os.environ.copy()
        env.update(CLAUDE_CONFIG_DIR=str(temporary / "config"), DISABLE_TELEMETRY="1",
                   DISABLE_ERROR_REPORTING="1")
        cli = [args.cli]

        def run(*arguments: str) -> str:
            return subprocess.run(cli + list(arguments), cwd=project, env=env, check=True,
                                  text=True, capture_output=True, timeout=60).stdout

        version = run("--version").strip()
        for path in (package, package / "skills"):
            report = json.loads(run("plugin", "validate", str(path), "--strict", "--json"))
            if not report["success"]:
                raise ValueError(f"Strict validation failed: {path.name}")
        for path in (package, archive_path):
            plugins = json.loads(run("--plugin-dir", str(path), "plugin", "list", "--json"))
            matches = [plugin for plugin in plugins if plugin["id"] == "diamond-captain@inline"]
            if len(matches) != 1 or not matches[0]["enabled"] or \
                    matches[0]["version"] != manifest["distribution"]["version"]:
                raise ValueError(f"CLI did not load the distribution from {path.name}")
        if "details" in run("plugin", "--help"):
            details = run("--plugin-dir", str(package), "plugin", "details", "diamond-captain")
            if "Skills (1)  diamond-captain" not in details:
                raise ValueError("CLI did not discover the packaged skill")
            inventory = "component inventory: one diamond-captain skill"
        else:
            inventory = "this CLI has no plugin details command; inventory not asserted"
        print(f"{version}: PASS, strict manifest and skill validation")
        print(f"Directory and ZIP both loaded; {inventory}")
        print(f"Core {manifest['core']['version']}, SHA-256 {manifest['core']['content_sha256']}")
        print("Isolated CLAUDE_CONFIG_DIR; no model invocation or persistent installation")
        print("Model behavior and directory submission are separate checks")


if __name__ == "__main__":
    main()
