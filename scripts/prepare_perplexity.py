#!/usr/bin/env python3
"""Prepare an unchanged, pinned Claude ZIP for personal Perplexity upload.

Offline preflight only: no download, account installation or model invocation.
"""
from __future__ import annotations

import argparse
import io
import json
import stat
import zipfile
from pathlib import Path

from build_distribution import ROOT, _guard, digest, json_bytes, safe_path, source_at_commit


def verify(archive: bytes, pin: dict) -> dict:
    if digest(archive) != pin["archive_sha256"]:
        raise ValueError("Archive differs from the pinned published SHA-256")
    with zipfile.ZipFile(io.BytesIO(archive)) as bundle:
        entries = bundle.infolist()
        names = [entry.filename for entry in entries]
        if len(entries) > 1000 or sum(e.file_size for e in entries) > 20_000_000:
            raise ValueError("Package exceeds Perplexity import limits")
        if len(names) != len(set(names)):
            raise ValueError("Duplicate ZIP entry")
        for entry in entries:
            safe_path(entry.filename)
            if entry.is_dir() or stat.S_ISLNK(entry.external_attr >> 16):
                raise ValueError("Expected ordinary package files")
        receipt = json.loads(bundle.read("DISTRIBUTION.json"))
        config = receipt["distribution"]
        if (config["service"], config["kind"], config["skill_root"], config["version"]) != (
                "claude-code", "claude-plugin", "skills/diamond-captain",
                pin["distribution_version"]):
            raise ValueError("Unexpected distribution identity")
        if receipt["build"] != {"commit": pin["package_commit"], "dirty": False}:
            raise ValueError("Unexpected package source")
        if set(names) != set(receipt["files"]) | {"DISTRIBUTION.json"}:
            raise ValueError("Unexpected or missing package files")
        for name, expected in receipt["files"].items():
            if digest(bundle.read(name)) != expected:
                raise ValueError(f"Modified package file: {name}")
        core = source_at_commit(ROOT, f"v{pin['core_version']}")
        hashes = {name: digest(data) for name, data in core.items()}
        core_hash = digest(json_bytes(hashes))
        if (receipt["core"]["version"] != pin["core_version"] or
                receipt["core"]["files"] != hashes or
                receipt["core"]["content_sha256"] != core_hash or
                config["core_version"] != pin["core_version"] or
                config["core_sha256"] != core_hash or core_hash != pin["core_sha256"]):
            raise ValueError("Canonical dependency differs from its pin")
        for name, data in core.items():
            if bundle.read(f"{config['skill_root']}/{name}") != data:
                raise ValueError(f"Core differs from its published tag: {name}")
        plugin = json.loads(bundle.read(".claude-plugin/plugin.json"))
        if plugin["name"] != "diamond-captain" or not plugin.get("description") or \
                len(plugin["description"]) > 1024:
            raise ValueError("Invalid plugin name/description")
        skills = [name for name in names if name.startswith("skills/") and name.endswith("/SKILL.md")]
        if skills != ["skills/diamond-captain/SKILL.md"] or any(
                name.startswith(("hooks/", "agents/")) or name in ("mcp.json", ".mcp.json")
                for name in names):
            raise ValueError("Expected one skill and no executable plugin components")
        return {"route": pin["route"], "archive_sha256": pin["archive_sha256"],
                "package_commit": pin["package_commit"], "core_version": pin["core_version"],
                "core_sha256": core_hash, "core_files_verified": len(core),
                "package_files_verified": len(names), "uncompressed_bytes": sum(e.file_size for e in entries),
                "archive_changed": False, "client_import_verified": False,
                "note": "Offline preflight; real client evidence is recorded separately."}


def prepare(archive_path: Path, output: Path) -> dict:
    pin = json.loads((ROOT / "distributions/perplexity/import.json").read_text())
    archive = archive_path.read_bytes()
    report = verify(archive, pin)
    # Validate before writing; never replace an earlier package or test evidence.
    instructions = (ROOT / "distributions/perplexity/README.md").read_text()
    instructions = instructions.replace("(../../docs/perplexity-compatibility.md)", "(COMPATIBILITY.md)")
    files = {pin["archive_name"]: archive, "PREFLIGHT.json": json_bytes(report),
             "import.json": json_bytes(pin), "IMPORT.md": instructions.encode(),
             "COMPATIBILITY.md": (ROOT / "docs/perplexity-compatibility.md").read_bytes().replace(
                 b"(../distributions/perplexity/README.md)", b"(IMPORT.md)").replace(
                 b"(validation.md)", b"(https://github.com/rebosidium/diamond-captain/blob/main/docs/validation.md)").replace(
                 b"(host-installation-routes.md)", b"(https://github.com/rebosidium/diamond-captain/blob/main/docs/host-installation-routes.md)")}
    failures = _guard.check_entries(files)
    if failures:
        raise ValueError("Private material in import handoff: " + failures[0])
    output.mkdir(parents=True, exist_ok=False)
    for name, data in files.items():
        (output / name).write_bytes(data)
    (output / "SHA256SUMS").write_text("".join(
        f"{digest(data)}  {name}\n" for name, data in sorted(files.items())))
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True, help="New local directory; refuses overwrite")
    args = parser.parse_args()
    print(json_bytes(prepare(args.archive, args.output)).decode(), end="")


if __name__ == "__main__":
    main()
