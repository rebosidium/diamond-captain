#!/usr/bin/env python3
"""Build deterministic Actions artifacts from a future accepted version tag."""
from __future__ import annotations

import argparse
import importlib.util
import io
import re
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# Existing releases precede this accepted public commit and cannot use this route.
ACTIVATION_BASELINE = "22c2c935009b009ac7f71c8db95db2e7fef222bc"
VERSION = r"(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)\.(?:0|[1-9][0-9]*)"
TAG = re.compile(rf"(?:(openai|claude-code|opencode)-)?v({VERSION})\Z")
spec = importlib.util.spec_from_file_location("release_distribution_builder", Path(__file__).with_name("build_distribution.py"))
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


def parse_tag(tag: str) -> tuple[str | None, str]:
    match = TAG.fullmatch(tag)
    if not match:
        raise ValueError("Use a core or supported host release tag with a stable SemVer version")
    return match.group(1), match.group(2)


def validate_source(root: Path, tag: str, baseline: str = ACTIVATION_BASELINE) -> str:
    parse_tag(tag)
    commit = builder.git(root, "rev-parse", "HEAD")
    if commit == baseline:
        raise ValueError("The activation baseline is not a future release")
    if builder.tag_commit(root, tag) != commit:
        raise ValueError("Checkout must be the exact release tag")
    if builder.git(root, "status", "--porcelain", "--untracked-files=all"):
        raise ValueError("Release source must be clean and committed")
    for ancestor, descendant in ((baseline, commit), (commit, "refs/remotes/origin/main")):
        if subprocess.run(["git", "-C", str(root), "merge-base", "--is-ancestor", ancestor, descendant],
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode:
            raise ValueError("Release must descend from the activation baseline and be accepted in main")
    return commit


def prepare(root: Path, tag: str, output: Path, baseline: str = ACTIVATION_BASELINE) -> list[Path]:
    service, version = parse_tag(tag)
    commit = validate_source(root, tag, baseline)
    root = root.resolve()
    if output.is_symlink():
        raise ValueError("Release output cannot be a symlink")
    output = output.resolve()
    if output == root or root in output.parents:
        raise ValueError("Release output must be outside the source checkout")
    if service:
        stem, receipt, archive = builder.build(root, service, release=True)
        if receipt["distribution"]["version"] != version:
            raise ValueError("Host tag does not match distribution metadata")
    else:
        core = builder.source_at_commit(root, commit)
        if builder.core_version(core) != version:
            raise ValueError("Core tag does not match canonical metadata")
        hashes = {name: builder.digest(data) for name, data in core.items()}
        receipt = {"schema_version": 1, "release": {"kind": "core", "tag": tag, "version": version},
                   "build": {"commit": commit, "dirty": False},
                   "core": {"name": "diamond-captain", "version": version,
                            "content_sha256": builder.digest(builder.json_bytes(hashes)), "files": hashes}}
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED) as bundle:
            for name, data in sorted(core.items()):
                info = zipfile.ZipInfo("diamond-captain/" + str(builder.safe_path(name)), (1980, 1, 1, 0, 0, 0))
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                info.compress_type = zipfile.ZIP_DEFLATED
                bundle.writestr(info, data, compresslevel=9)
        archive = stream.getvalue()
        stem = "diamond-captain-" + tag
    files = {stem + ".zip": archive, stem + ".json": builder.json_bytes(receipt)}
    files[stem + "-SHA256SUMS"] = "".join(
        f"{builder.digest(data)}  {name}\n" for name, data in sorted(files.items())).encode()
    failures = builder._guard.check_entries(files)
    if failures:
        raise ValueError("Release payload failed public-content inspection: " + failures[0])
    if output.exists():
        for path in output.iterdir():
            if path.is_symlink() or not path.is_file() or path.name not in files or path.read_bytes() != files[path.name]:
                raise ValueError("Output contains different or unexpected data; use a fresh directory")
    output.mkdir(parents=True, exist_ok=True)
    for name, data in files.items():
        path = output / name
        if not path.exists():
            with path.open("xb") as handle:
                handle.write(data)
    return [output / name for name in sorted(files)]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        for path in prepare(ROOT, args.tag, args.output):
            print("Prepared " + path.name)
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Release preparation failed: {error}\n")


if __name__ == "__main__":
    main()
