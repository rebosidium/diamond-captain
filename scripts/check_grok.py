#!/usr/bin/env python3
"""Test an unchanged Claude release archive with an installed Grok Build CLI.

No download, authentication or model call. All host mutations use a temporary
GROK_HOME; personal Cursor/Claude compatibility sources are disabled for the run.
"""
from __future__ import annotations

import argparse
import json
import os
import shutil
import stat
import subprocess
import tempfile
import zipfile
from pathlib import Path

from build_distribution import ROOT, digest, json_bytes, safe_path, source_at_commit


def isolated_env(home: Path) -> dict[str, str]:
    env = os.environ.copy()
    env.update(GROK_HOME=str(home), GROK_DISABLE_AUTOUPDATER="1", GROK_MEMORY="0",
               GROK_SUBAGENTS="0", GROK_WEB_FETCH="0")
    for vendor in ("CLAUDE", "CURSOR"):
        for surface in ("SKILLS", "RULES", "AGENTS", "MCPS", "HOOKS"):
            env[f"GROK_{vendor}_{surface}_ENABLED"] = "0"
    return env


def active(entries: list[dict]) -> list[dict]:
    return [entry for entry in entries if entry.get("enabled", True)
            and not entry.get("disabled", False)
            and entry.get("compatibilityStatus") != "disabled"]


def check(cli: str, archive_path: Path, archive_sha256: str) -> dict:
    archive = archive_path.read_bytes()
    if digest(archive) != archive_sha256:
        raise ValueError("Archive SHA-256 differs from the supplied published digest")
    with tempfile.TemporaryDirectory(prefix="dr-grok-check-") as directory:
        temporary = Path(directory)
        home, project, package = (temporary / name for name in ("config", "project", "package"))
        home.mkdir()
        project.mkdir()
        (home / "config.toml").write_text("[cli]\nauto_update = false\n")
        with zipfile.ZipFile(archive_path) as bundle:
            names = bundle.namelist()
            if len(names) != len(set(names)):
                raise ValueError("Duplicate ZIP entry")
            for entry in bundle.infolist():
                safe_path(entry.filename)
                if entry.is_dir() or stat.S_ISLNK(entry.external_attr >> 16):
                    raise ValueError("Expected a flat list of ordinary package files")
            manifest = json.loads(bundle.read("DISTRIBUTION.json"))
            config = manifest["distribution"]
            if config["service"] != "claude-code" or config["kind"] != "claude-plugin" or \
                    config["skill_root"] != "skills/diamond-captain":
                raise ValueError("Expected the existing Claude Code distribution")
            if set(names) != set(manifest["files"]) | {"DISTRIBUTION.json"}:
                raise ValueError("Unexpected or missing package files")
            for name, expected in manifest["files"].items():
                if digest(bundle.read(name)) != expected:
                    raise ValueError(f"Modified package file: {name}")
            core = source_at_commit(ROOT, f"v{manifest['core']['version']}")
            hashes = {name: digest(data) for name, data in core.items()}
            if hashes != manifest["core"]["files"] or \
                    digest(json_bytes(hashes)) != config["core_sha256"]:
                raise ValueError("Package does not contain its declared canonical dependency")
            for name, data in core.items():
                if bundle.read(f"{config['skill_root']}/{name}") != data:
                    raise ValueError(f"Core differs from its published tag: {name}")
            bundle.extractall(package)
        env = isolated_env(home)

        def run(*args: str) -> str:
            return subprocess.run([cli, "--no-auto-update", *args], cwd=project, env=env,
                                  text=True, capture_output=True, check=True, timeout=45).stdout

        def inspect() -> dict:
            return json.loads(run("inspect", "--json"))

        version = run("--version").strip()
        validation = run("plugin", "validate", str(package)).strip()
        before = inspect()
        if active(before["skills"]) or active(before["plugins"]):
            raise ValueError("Unrelated active skills/plugins would contaminate discovery")
        if active(before["mcpServers"]) or before["hooks"]:
            raise ValueError("Unexpected active MCP servers or hooks in the test environment")
        run("plugin", "install", str(package), "--trust")

        def loaded() -> tuple[dict, dict]:
            state = inspect()
            plugins, skills = active(state["plugins"]), active(state["skills"])
            if len(plugins) != 1 or plugins[0]["name"] != "diamond-captain" or \
                    len(skills) != 1 or skills[0]["name"] != "diamond-captain":
                raise ValueError("Grok did not discover exactly the installed plugin and skill")
            plugin, skill = plugins[0], skills[0]
            installed = Path(plugin["path"])
            installed.resolve().relative_to(home.resolve())
            expected = installed / config["skill_root"] / "SKILL.md"
            if skill["source"]["type"] != "plugin" or \
                    Path(skill["source"]["path"]).resolve() != expected.resolve():
                raise ValueError("Discovered skill comes from a different source")
            payload = installed / config["skill_root"]
            actual = {p.relative_to(payload).as_posix(): digest(p.read_bytes())
                      for p in payload.rglob("*") if p.is_file()}
            if actual != hashes:
                raise ValueError("Installed core bytes differ from the published package")
            if plugin["provides"] != {"skills": 1, "agents": 0, "hooks": False, "mcpServers": 0}:
                raise ValueError("Unexpected executable plugin components")
            if active(state["mcpServers"]) or state["hooks"]:
                raise ValueError("Unexpected active external tools")
            return plugin, skill

        loaded()
        run("plugin", "disable", "diamond-captain")
        disabled = inspect()
        if active(disabled["skills"]):
            raise ValueError("Disabled plugin skill is still available")
        # 1.0.70 retains the installed plugin inventory with enabled=true even
        # while its skill disappears. Do not treat that inventory as activation.
        retained = [p for p in disabled["plugins"] if p["name"] == "diamond-captain"]
        run("plugin", "enable", "diamond-captain")
        loaded()
        return {
            "cli_version": version,
            "archive_sha256": archive_sha256,
            "distribution": {"service": config["service"], "version": config["version"]},
            "package_build": manifest["build"],
            "core_version": manifest["core"]["version"],
            "core_sha256": config["core_sha256"],
            "core_files_verified": len(hashes),
            "validation": validation,
            "active_plugins": 1, "active_skills": 1,
            "disable_enable_skill_inventory_passed": True,
            "disabled_plugin_inventory_retained": bool(retained),
            "model_invoked": False,
            "isolation": "Temporary GROK_HOME; personal compatibility scanners disabled",
        }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cli", default=shutil.which("grok"))
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--archive-sha256", required=True, help="Published ZIP SHA-256")
    parser.add_argument("--output", type=Path, help="New evidence JSON; refuses overwrite")
    args = parser.parse_args()
    if not args.cli:
        parser.error("Pass --cli /absolute/path/to/grok or install the official CLI separately")
    report = check(args.cli, args.archive, args.archive_sha256)
    data = json_bytes(report)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with args.output.open("xb") as target:
            target.write(data)
    print(data.decode(), end="")


if __name__ == "__main__":
    main()
