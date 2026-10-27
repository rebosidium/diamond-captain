#!/usr/bin/env python3
"""Install the verified native skill from an extracted distribution (Python 3.9+)."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import tempfile
import uuid
from pathlib import Path, PurePosixPath


def relative_path(value: str) -> Path:
    posix = PurePosixPath(value)
    if not value or posix.is_absolute() or ".." in posix.parts or "\\" in value:
        raise ValueError(f"Unsafe manifest path: {value!r}")
    return Path(*posix.parts)


def no_symlinks(root: Path, relative: Path) -> Path:
    path = root
    for part in relative.parts:
        path = path / part
        if path.is_symlink():
            raise ValueError(f"Symlink not supported for installation: {path}")
    return path


def verify(package: Path) -> tuple[dict, Path]:
    manifest_path = no_symlinks(package, Path("DISTRIBUTION.json"))
    manifest = json.loads(manifest_path.read_text())
    if manifest["schema_version"] != 1 or manifest["distribution"]["kind"] != "native-skill":
        raise ValueError("Unsupported distribution manifest")
    skill_root = relative_path(manifest["distribution"]["skill_root"])
    service = manifest["distribution"]["service"]
    if skill_root.as_posix() != f".{service}/skills/diamond-captain":
        raise ValueError("Unexpected native skill destination")
    source = no_symlinks(package, skill_root)
    files = manifest["files"]
    for name, expected in files.items():
        path = no_symlinks(package, relative_path(name))
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError(f"Missing or modified package file: {name}")
    prefix = skill_root.as_posix() + "/"
    expected_skill = {name[len(prefix):] for name in files if name.startswith(prefix)}
    actual_skill = set()
    for path in source.rglob("*"):
        if path.is_symlink():
            raise ValueError(f"Unexpected symlink: {path}")
        if path.is_file():
            actual_skill.add(path.relative_to(source).as_posix())
    if not expected_skill or expected_skill != actual_skill:
        raise ValueError("Skill payload has missing or unexpected files")
    return manifest, source


def install(package: Path, project: Path, replace: bool = False, dry_run: bool = False) -> Path:
    manifest, source = verify(package)
    if not project.is_dir():
        raise ValueError("Project must be an existing directory")
    project = project.resolve()
    config = manifest["distribution"]
    service = config["service"]
    if not service or any(char not in "abcdefghijklmnopqrstuvwxyz0123456789-" for char in service):
        raise ValueError("Invalid service name")
    destination = no_symlinks(project, relative_path(config["skill_root"]))
    if destination.exists() and not replace:
        raise ValueError(f"Already installed: {destination}; use --replace to back it up first")
    if destination.exists() and not destination.is_dir():
        raise ValueError(f"Installation destination is not a directory: {destination}")
    # Also check the backup path before any filesystem mutation.
    backup_root = no_symlinks(project, Path(".diamond-captain-backups") / service)
    for directory in (backup_root.parent, backup_root):
        if directory.exists() and not directory.is_dir():
            raise ValueError(f"Backup destination is not a directory: {directory}")
    if dry_run:
        print(f"Verified {service} {config['version']} / core {config['core_version']}")
        print(f"Would install: {destination}")
        return destination
    # Stage outside all skill discovery roots and on the destination filesystem.
    with tempfile.TemporaryDirectory(prefix=".diamond-captain-stage-", dir=project) as temporary:
        staged = Path(temporary) / "skill"
        shutil.copytree(source, staged)
        # Prepare and persist the receipt before switching the active skill.
        receipt_name = f"installed-{uuid.uuid4()}.json"
        staged_receipt = Path(temporary) / receipt_name
        staged_receipt.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")
        backup_root.mkdir(parents=True, exist_ok=True)
        destination.parent.mkdir(parents=True, exist_ok=True)
        receipt = backup_root / receipt_name
        receipt_ready = False
        backup = None
        try:
            staged_receipt.rename(receipt)
            receipt_ready = True
            if destination.exists():
                backup_target = backup_root / str(uuid.uuid4())
                destination.rename(backup_target)
                backup = backup_target
            staged.rename(destination)
        except OSError:
            if backup is not None:
                backup.rename(destination)
            if receipt_ready:
                receipt.unlink()
            raise
    print(f"Installed: {destination}")
    if backup is not None:
        print(f"Previous installation: {backup}")
    print(f"Receipt: {receipt}")
    return destination


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True)
    parser.add_argument("--replace", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        install(Path(__file__).resolve().parent, args.project, args.replace, args.dry_run)
    except (ValueError, KeyError, OSError) as error:
        parser.exit(1, f"Install failed: {error}\n")


if __name__ == "__main__":
    main()
