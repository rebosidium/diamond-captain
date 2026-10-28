"""Offline preflight regressions; no account access or model calls."""
import copy
import io
import importlib.util
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_distribution as builder
import prepare_perplexity as preflight
from test_distributions import pinned_repository


class HandoffGuardTests(unittest.TestCase):
    def test_private_handoff_is_rejected_without_writing(self):
        with tempfile.TemporaryDirectory() as directory:
            source, output = Path(directory) / "input.zip", Path(directory) / "output"
            source.write_bytes(b"fixture")
            original = Path.read_text

            def private_instructions(path, *args, **kwargs):
                if path == ROOT / "distributions/perplexity/README.md":
                    return "/Users/" + "fixture-owner/private.txt"
                return original(path, *args, **kwargs)

            with patch.object(preflight, "verify", return_value={}), \
                    patch.object(Path, "read_text", private_instructions), \
                    self.assertRaisesRegex(ValueError, "Private material"):
                preflight.prepare(source, output)
            self.assertFalse(output.exists())


class PerplexityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Current adapter with its real pinned/tagged core, not the mutable
        # development core or evidence for a published archive.
        temporary = tempfile.TemporaryDirectory()
        cls.addClassCleanup(temporary.cleanup)
        repository = Path(temporary.name)
        cls.core = pinned_repository(repository, "claude-code")
        _, receipt, archive = builder.build(repository, "claude-code")
        with zipfile.ZipFile(io.BytesIO(archive)) as z:
            cls.files = {name: z.read(name) for name in z.namelist()}
        cls.pin = {"route": "claude-plugin-upload", "distribution_version": receipt["distribution"]["version"],
                   "package_commit": receipt["build"]["commit"], "core_version": receipt["core"]["version"],
                   "core_sha256": receipt["core"]["content_sha256"], "archive_name": "fixture.zip"}

    def fixture(self, files=None):
        out = io.BytesIO()
        with zipfile.ZipFile(out, "w") as z:
            for name, data in (files or self.files).items():
                z.writestr(name, data)
        archive = out.getvalue()
        return archive, {**self.pin, "archive_sha256": builder.digest(archive)}

    def test_complete_canonical_payload(self):
        archive, pin = self.fixture()
        report = preflight.verify(archive, pin)
        self.assertEqual(len(self.core), report["core_files_verified"])
        self.assertFalse(report["archive_changed"])
        self.assertFalse(report["client_import_verified"])

    def test_bad_digest_or_dependency_pin_fails(self):
        archive, pin = self.fixture()
        for key in ("archive_sha256", "core_sha256", "package_commit", "distribution_version"):
            with self.subTest(key=key), self.assertRaises(ValueError):
                preflight.verify(archive, {**pin, key: "wrong"})

    def test_wrong_namespace_is_rejected_even_with_consistent_receipt(self):
        for target in ("skill_root", "plugin_name"):
            with self.subTest(target=target):
                files = copy.copy(self.files)
                receipt = json.loads(files["DISTRIBUTION.json"])
                if target == "skill_root":
                    receipt["distribution"]["skill_root"] = "skills/other-skill"
                else:
                    name = ".claude-plugin/plugin.json"
                    plugin = json.loads(files[name])
                    plugin["name"] = "other-skill"
                    files[name] = builder.json_bytes(plugin)
                    receipt["files"][name] = builder.digest(files[name])
                files["DISTRIBUTION.json"] = builder.json_bytes(receipt)
                archive, pin = self.fixture(files)
                expected = "Unexpected distribution identity" if target == "skill_root" else "Invalid plugin"
                with self.assertRaisesRegex(ValueError, expected):
                    preflight.verify(archive, pin)

    def test_self_consistent_tampered_core_is_rejected_against_tag(self):
        files = copy.copy(self.files)
        name = "skills/diamond-captain/references/phases.md"
        files[name] += b"\nModified fixture\n"
        receipt = json.loads(files["DISTRIBUTION.json"])
        receipt["files"][name] = builder.digest(files[name])
        files["DISTRIBUTION.json"] = builder.json_bytes(receipt)
        archive, pin = self.fixture(files)
        with self.assertRaisesRegex(ValueError, "Core differs"):
            preflight.verify(archive, pin)

    def test_missing_reference_or_extra_file_fails(self):
        for name in ("missing", "extra"):
            files = copy.copy(self.files)
            if name == "missing":
                files.pop("skills/diamond-captain/references/research.md")
            else:
                files["unexpected.txt"] = b"unlisted"
            archive, pin = self.fixture(files)
            with self.subTest(name=name), self.assertRaises(ValueError):
                preflight.verify(archive, pin)

    def test_prepare_preserves_existing_output_and_exact_zip(self):
        archive, pin = self.fixture()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "input.zip"
            source.write_bytes(archive)
            output = root / "output"
            original = json.loads

            def read_pin(data, *args, **kwargs):
                result = original(data, *args, **kwargs)
                return pin if isinstance(result, dict) and result.get("route") == "claude-plugin-upload" else result

            with patch.object(preflight.json, "loads", side_effect=read_pin):
                preflight.prepare(source, output)
                self.assertEqual(archive, (output / "fixture.zip").read_bytes())
                for line in (output / "SHA256SUMS").read_text().splitlines():
                    expected, name = line.split("  ", 1)
                    self.assertEqual(expected, builder.digest((output / name).read_bytes()), name)
                self.assertIn("(COMPATIBILITY.md)", (output / "IMPORT.md").read_text())
                self.assertIn("(IMPORT.md)", (output / "COMPATIBILITY.md").read_text())
                spec = importlib.util.spec_from_file_location(
                    "handoff_links", ROOT / ".agents/skills/diamond-captain/tests/check_package.py")
                links = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(links)
                _, failures = links.check_links(output)
                self.assertEqual([], failures)
                (output / "user-state.md").write_text("preserve")
                with self.assertRaises(FileExistsError):
                    preflight.prepare(source, output)
                self.assertEqual("preserve", (output / "user-state.md").read_text())

    def test_invalid_input_creates_no_output(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source, output = root / "wrong.zip", root / "output"
            source.write_bytes(b"not the pinned archive")
            with self.assertRaises(ValueError):
                preflight.prepare(source, output)
            self.assertFalse(output.exists())


if __name__ == "__main__":
    unittest.main()
