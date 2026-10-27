#!/usr/bin/env python3
"""Check native discovery in an isolated OpenCode CLI, without a model call."""
from __future__ import annotations

import io
import json
import os
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

from build_distribution import ROOT, build

CLI_VERSION = "1.19.4"


def main() -> None:
    _, manifest, archive = build(ROOT, "opencode")
    with tempfile.TemporaryDirectory(prefix="dr-opencode-check-") as directory:
        temporary = Path(directory)
        package, project = temporary / "package", temporary / "project"
        project.mkdir()
        with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
            bundle.extractall(package)
        subprocess.run([sys.executable, str(package / "install.py"), "--project", str(project)],
                       check=True, capture_output=True, text=True)
        env = os.environ.copy()
        for name in ("XDG_CONFIG_HOME", "XDG_DATA_HOME", "XDG_CACHE_HOME", "XDG_STATE_HOME"):
            env[name] = str(temporary / name.lower())
        env["OPENCODE_DISABLE_EXTERNAL_SKILLS"] = "1"
        cli = ["npm", "exec", "--yes", f"--package=opencode-ai@{CLI_VERSION}", "--", "opencode"]
        version = subprocess.run(cli + ["--version"], cwd=project, env=env, check=True,
                                 text=True, capture_output=True, timeout=60).stdout.strip()
        if version != CLI_VERSION:
            raise ValueError(f"Unexpected CLI version: {version}")
        result = subprocess.run(cli + ["debug", "skill", "--pure"], cwd=project, env=env,
                                check=True, text=True, capture_output=True, timeout=60)
        skills = json.loads(result.stdout)
        matches = [skill for skill in skills if skill["name"] == "diamond-captain"]
        expected = project / manifest["distribution"]["skill_root"] / "SKILL.md"
        if len(matches) != 1 or Path(matches[0]["location"]).resolve() != expected.resolve():
            raise ValueError("CLI did not discover exactly the installed canonical skill")
        if "# Diamond Captain" not in matches[0]["content"]:
            raise ValueError("CLI returned incomplete skill content")
        print(f"OpenCode {version}: PASS, exactly one diamond-captain at the installed project path")
        print(f"Core {manifest['core']['version']}, SHA-256 {manifest['core']['content_sha256']}")
        print("Isolated XDG directories; external plugins/skills disabled; no model invocation")


if __name__ == "__main__":
    main()
