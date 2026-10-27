#!/usr/bin/env python3
"""Export an explicitly committed canonical skill for local client testing.

No release version, tag or published dependency pin is changed. Keep generated
preview receipts and client evidence in private storage outside source checkouts.
"""
from __future__ import annotations

import argparse
import io
import re
import zipfile
from pathlib import Path

from build_distribution import ROOT, _guard, core_version, digest, git, json_bytes, source_at_commit


def build(commit: str, plugin_name: str = "diamond-captain-preview") -> tuple[bytes, dict]:
    if not re.fullmatch(r"[a-z][a-z0-9-]*", plugin_name):
        raise ValueError("Invalid preview plugin name")
    resolved = git(ROOT, "rev-parse", "--verify", f"{commit}^{{commit}}")
    core = source_at_commit(ROOT, resolved)
    hashes = {name: digest(data) for name, data in core.items()}
    payload = {f"skills/diamond-captain/{name}": data for name, data in core.items()}
    header = core["SKILL.md"].split(b"---", 2)[1]
    description = re.search(rb"^description: (.+)$", header, re.M)
    if not description:
        raise ValueError("Preview requires the canonical single-line skill description")
    description = description[1].decode()
    if len(description) > 1024:
        raise ValueError("Canonical description exceeds the plugin import limit")
    payload["plugin.json"] = json_bytes({
        "name": plugin_name,
        "description": description,
        "license": "MIT"})
    failures = _guard.check_entries(payload)
    if failures:
        raise ValueError("Private material in preview payload: " + failures[0])
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
        for name, data in sorted(payload.items()):
            entry = zipfile.ZipInfo(name, (1980, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            entry.external_attr = 0o100644 << 16
            bundle.writestr(entry, data)
    archive = out.getvalue()
    return archive, {"release": False, "source_commit": resolved,
                     "declared_core_version": core_version(core),
                     "core_content_sha256": digest(json_bytes(hashes)), "core_files": hashes,
                     "plugin_name": plugin_name, "archive_sha256": digest(archive)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--commit", required=True, help="Exact committed source to freeze")
    parser.add_argument("--plugin-name", default="diamond-captain-preview")
    parser.add_argument("--output", required=True, type=Path, help="New private output directory")
    args = parser.parse_args()
    archive, receipt = build(args.commit, args.plugin_name)
    args.output.mkdir(parents=True, exist_ok=False)
    (args.output / "preview.zip").write_bytes(archive)
    (args.output / "PREVIEW.json").write_bytes(json_bytes(receipt))
    print(json_bytes(receipt).decode(), end="")


if __name__ == "__main__":
    main()
