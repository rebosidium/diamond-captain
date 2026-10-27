#!/usr/bin/env python3
"""Build reproducible service packages from the one canonical skill (stdlib only)."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import io
import json
import re
import subprocess
import tarfile
import zipfile
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path(".agents/skills/diamond-captain")
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
_guard_spec = importlib.util.spec_from_file_location("public_content_guard", Path(__file__).with_name("check_public_content.py"))
_guard = importlib.util.module_from_spec(_guard_spec)
_guard_spec.loader.exec_module(_guard)


def git(root: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(root), *args], text=True).strip()


def tag_commit(root: Path, tag: str) -> str | None:
    result = subprocess.run(["git", "-C", str(root), "rev-parse", "--verify", f"refs/tags/{tag}^{{commit}}"],
                            text=True, capture_output=True)
    return result.stdout.strip() if result.returncode == 0 else None


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def json_bytes(value: dict) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode()


def safe_path(value: str) -> PurePosixPath:
    path = PurePosixPath(value)
    if not value or path.is_absolute() or ".." in path.parts or "\\" in value:
        raise ValueError(f"Unsafe package path: {value!r}")
    return path


def source_files(root: Path) -> dict[str, bytes]:
    directory = root / SOURCE
    files = {}
    for path in sorted(directory.rglob("*")):
        if "__pycache__" in path.parts or path.suffix in {".pyc", ".pyo"}:
            continue
        if path.is_symlink():
            raise ValueError(f"Canonical skill must not contain symlinks: {path}")
        if path.is_file():
            files[path.relative_to(directory).as_posix()] = path.read_bytes()
    if "SKILL.md" not in files or "LICENSE" not in files:
        raise ValueError("Canonical skill or its license is missing")
    return files


def core_version(files: dict[str, bytes]) -> str:
    match = re.search(rb'^  version: "([0-9]+\.[0-9]+\.[0-9]+)"$', files["SKILL.md"], re.M)
    if not match:
        raise ValueError("Canonical skill must declare metadata.version")
    return match[1].decode()


def source_at_commit(root: Path, commit: str) -> dict[str, bytes]:
    data = subprocess.check_output(["git", "-C", str(root), "archive", commit, SOURCE.as_posix()])
    files = {}
    prefix = SOURCE.as_posix() + "/"
    with tarfile.open(fileobj=io.BytesIO(data), mode="r:") as archive:
        for entry in archive.getmembers():
            if entry.isdir():
                continue
            if not entry.isfile() or not entry.name.startswith(prefix):
                raise ValueError("Pinned canonical source contains an unsupported file")
            name = entry.name[len(prefix):]
            safe_path(name)
            files[name] = archive.extractfile(entry).read()
    if "SKILL.md" not in files or "LICENSE" not in files:
        raise ValueError("Pinned canonical skill or its license is missing")
    return dict(sorted(files.items()))


def pinned_core(root: Path, config: dict, release: bool) -> tuple[dict[str, bytes], str]:
    current = source_files(root)
    version = config["core_version"]
    tagged = tag_commit(root, f"v{version}")
    if core_version(current) == version:
        # Catch edits made under an existing core version, even in a dev build.
        hashes = {name: digest(data) for name, data in current.items()}
        if digest(json_bytes(hashes)) != config["core_sha256"]:
            raise ValueError("Core content differs from this distribution's pinned dependency")
        if tagged is None:
            if release:
                raise ValueError(f"Release dependency tag v{version} is unavailable; fetch it first")
            return current, "HEAD"
        pinned = source_at_commit(root, tagged)
        if pinned != current:
            raise ValueError("Core content differs from its published version tag")
    else:
        if tagged is None:
            raise ValueError(f"Core version changed and pinned tag v{version} is unavailable; fetch it first")
        pinned = source_at_commit(root, tagged)
    if core_version(pinned) != version:
        raise ValueError("Pinned core tag has a different metadata.version")
    return pinned, tagged


def build(root: Path, service: str, release: bool = False) -> tuple[str, dict, bytes]:
    if not re.fullmatch(r"[a-z][a-z0-9-]*", service):
        raise ValueError("Invalid service name")
    adapter = root / "distributions" / service
    config = json.loads((adapter / "distribution.json").read_text())
    if config["service"] != service or not SEMVER.fullmatch(config["version"]) or \
            not SEMVER.fullmatch(config["core_version"]):
        raise ValueError("Invalid distribution identity/version")
    core, core_ref = pinned_core(root, config, release)
    version = core_version(core)
    core_hashes = {name: digest(data) for name, data in core.items()}
    core_digest = digest(json_bytes(core_hashes))
    if config["core_sha256"] != core_digest:
        raise ValueError("Core content differs from this distribution's pinned dependency")
    skill_root = str(safe_path(config["skill_root"]))
    kind = config["kind"]
    if kind == "native-skill":
        if skill_root != f".{service}/skills/diamond-captain":
            raise ValueError("Native skill destination must be the service's own skills directory")
    elif kind in {"claude-plugin", "agent-plugin"}:
        if skill_root != "skills/diamond-captain":
            raise ValueError("Plugin skill must use the standard skills directory")
    else:
        raise ValueError(f"Unsupported distribution kind: {config['kind']}")
    dirty = bool(git(root, "status", "--porcelain", "--untracked-files=all"))
    if release and dirty:
        raise ValueError("Release builds require a clean, committed checkout")
    commit = git(root, "rev-parse", "HEAD")
    if release:
        tagged = tag_commit(root, f"{service}-v{config['version']}")
        if tagged is not None and tagged != commit:
            raise ValueError("This version is already tagged: build from that exact tag or bump the distribution version")
    payload = {f"{skill_root}/{name}": data for name, data in core.items()}
    payload["README.md"] = (adapter / "README.md").read_bytes()
    if kind == "native-skill":
        payload["install.py"] = (root / "scripts/install_distribution.py").read_bytes()
    else:
        plugin = json.loads((adapter / "plugin.template.json").read_text())
        if "version" in plugin:
            raise ValueError("Plugin version is generated from distribution.json; do not duplicate it")
        plugin["version"] = config["version"]
        manifest_path = ".claude-plugin/plugin.json" if kind == "claude-plugin" else "plugin.json"
        payload[manifest_path] = json_bytes(plugin)
        payload["LICENSE"] = core["LICENSE"]
        marketplace = adapter / "marketplace.json"
        if marketplace.exists():
            payload[".agents/plugins/marketplace.json"] = marketplace.read_bytes()
    manifest = {
        "schema_version": 1,
        "distribution": config,
        "core": {
            "name": "diamond-captain", "version": version,
            "source_path": SOURCE.as_posix(),
            "source_commit": git(root, "log", "-1", "--format=%H", core_ref, "--", SOURCE.as_posix()),
            "content_sha256": core_digest,
            "files": core_hashes,
        },
        "build": {"commit": commit, "dirty": dirty},
        "files": {name: digest(data) for name, data in sorted(payload.items())},
    }
    payload["DISTRIBUTION.json"] = json_bytes(manifest)
    failures = _guard.check_entries(payload)
    if failures:
        raise ValueError("Private material in distribution payload: " + failures[0])
    archive = io.BytesIO()
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as bundle:
        for name, data in sorted(payload.items()):
            safe_path(name)
            info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            bundle.writestr(info, data, compresslevel=9)
    stem = f"diamond-captain-{service}-{config['version']}-core-{version}"
    return stem, manifest, archive.getvalue()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("service", help="directory under distributions/")
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    parser.add_argument("--release", action="store_true", help="require a clean checkout")
    args = parser.parse_args()
    try:
        stem, manifest, archive = build(ROOT, args.service, args.release)
        files = {f"{stem}.zip": archive, f"{stem}.json": json_bytes(manifest)}
        files[f"{stem}-SHA256SUMS"] = "".join(
            f"{digest(data)}  {name}\n" for name, data in sorted(files.items())
        ).encode()
        args.output.mkdir(parents=True, exist_ok=True)
        # Never silently replace a previous build with different bytes.
        for name, data in files.items():
            path = args.output / name
            if path.exists() and path.read_bytes() != data:
                raise ValueError(f"Different build already exists: {path}; use a new output directory")
        for name, data in files.items():
            path = args.output / name
            path.write_bytes(data)
            print(path)
    except (ValueError, KeyError, OSError, subprocess.CalledProcessError) as error:
        parser.exit(1, f"Build failed: {error}\n")


if __name__ == "__main__":
    main()
