#!/usr/bin/env python3
"""Bounded, synthetic installer properties; no network or user installations."""
from __future__ import annotations

import hashlib
import io
import json
import posixpath
import sys
import tempfile
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
if __name__ == "__main__":
    import atheris

    with atheris.instrument_imports():
        import install_distribution as installer
else:
    import install_distribution as installer


def test_one_input(data: bytes) -> None:
    if len(data) > 4096:
        return
    mode = data[0] % 8 if data else 0
    value = data[1:513].decode("utf-8", "replace")
    if mode == 0:
        try:
            path = installer.relative_path(value)
        except ValueError:
            return
        normalized = posixpath.normpath("/sandbox/" + path.as_posix())
        assert not path.is_absolute() and (normalized == "/sandbox" or normalized.startswith("/sandbox/"))
        return
    with tempfile.TemporaryDirectory(prefix="diamond-captain-fuzz-") as temporary:
        root = Path(temporary)
        package, project = root / "package", root / "project"
        skill_name = ".opencode/skills/diamond-captain/SKILL.md"
        payload = data[1:] or b"synthetic skill"
        source = package / skill_name
        source.parent.mkdir(parents=True)
        source.write_bytes(payload)
        (project / ".product-task").mkdir(parents=True)
        (project / ".product-task/state.json").write_bytes(b'{"checkpoint":"keep"}\n')
        (project / ".opencode").mkdir()
        (project / ".opencode/settings.json").write_bytes(b'{"setting":"keep"}\n')
        manifest = {"schema_version": 1, "distribution": {
            "kind": "native-skill", "service": "opencode", "version": "0.0.0",
            "core_version": "0.0.0", "skill_root": ".opencode/skills/diamond-captain"},
            "files": {skill_name: hashlib.sha256(payload).hexdigest()}}
        if mode == 1:
            manifest["files"] = {value: hashlib.sha256(payload).hexdigest()}
        elif mode == 2:
            manifest["distribution"]["service"] = value
        elif mode == 3:
            manifest["distribution"]["skill_root"] = value
        elif mode == 4:
            manifest["files"][skill_name] = value
        outside = root / "outside"
        outside.write_bytes(payload)
        if mode == 7:
            source.unlink()
            source.symlink_to(outside)
        (package / "DISTRIBUTION.json").write_text(json.dumps(manifest))
        accepted = False
        try:
            with redirect_stdout(io.StringIO()):
                destination = installer.install(package, project, dry_run=mode not in (5, 6))
                accepted = True
                if mode == 6:
                    installer.install(package, project, replace=True)
        except (ValueError, KeyError, OSError):
            if mode in (5, 6):
                raise  # A well-formed control must install, not merely reject everything.
        if accepted:
            # Invariant failures must not be swallowed as ordinary input rejection.
            destination.resolve().relative_to(project.resolve())
            if mode in (5, 6):
                assert (destination / "SKILL.md").read_bytes() == payload
        assert (project / ".product-task/state.json").read_bytes() == b'{"checkpoint":"keep"}\n'
        assert (project / ".opencode/settings.json").read_bytes() == b'{"setting":"keep"}\n'
        assert outside.read_bytes() == payload
        if mode not in (5, 6):
            assert not (project / ".opencode/skills").exists()
            assert not (project / ".diamond-captain-backups").exists()
        if mode == 7:
            assert not accepted, "A source symlink must never be accepted"


if __name__ == "__main__":
    atheris.instrument_func(test_one_input)
    atheris.Setup(sys.argv, test_one_input)
    atheris.Fuzz()
