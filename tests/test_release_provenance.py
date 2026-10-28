"""Deterministic future-tag Actions artifact preparation."""
from __future__ import annotations

import io
import json
import shutil
import tempfile
import unittest
import zipfile
from pathlib import Path

from test_distributions import fixture_git, load

prepare = load("prepare_release")
ROOT = Path(__file__).resolve().parents[1]


class ReleaseProvenanceTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.sandbox = Path(temporary.name)
        self.root = self.sandbox / "repo"
        self.root.mkdir()
        core = self.root / prepare.builder.SOURCE
        core.mkdir(parents=True)
        (core / "SKILL.md").write_text('---\nname: diamond-captain\nmetadata:\n  version: "9.8.7"\n---\nSynthetic skill.\n')
        (core / "LICENSE").write_text("MIT fixture license\n")
        (self.root / "README.md").write_text("Synthetic release fixture\n")
        adapter = self.root / "distributions/opencode"
        adapter.mkdir(parents=True)
        hashes = {p.name: prepare.builder.digest(p.read_bytes()) for p in sorted(core.iterdir())}
        config = {"service": "opencode", "version": "2.0.0", "core_version": "9.8.7",
                  "core_sha256": prepare.builder.digest(prepare.builder.json_bytes(hashes)),
                  "kind": "native-skill", "skill_root": ".opencode/skills/diamond-captain"}
        (adapter / "distribution.json").write_bytes(prepare.builder.json_bytes(config))
        (adapter / "README.md").write_text("Synthetic native package\n")
        (self.root / "scripts").mkdir()
        shutil.copyfile(ROOT / "scripts/install_distribution.py", self.root / "scripts/install_distribution.py")
        fixture_git(self.root, "init", "-q")
        fixture_git(self.root, "add", ".")
        fixture_git(self.root, "commit", "-qm", "fixture activation boundary")
        self.baseline = fixture_git(self.root, "rev-parse", "HEAD")
        fixture_git(self.root, "tag", "v9.8.6")
        (self.root / "README.md").write_text("Reviewed future release fixture\n")
        fixture_git(self.root, "add", ".")
        fixture_git(self.root, "commit", "-qm", "fixture reviewed change")
        self.commit = fixture_git(self.root, "rev-parse", "HEAD")
        fixture_git(self.root, "update-ref", "refs/remotes/origin/main", self.commit)
        fixture_git(self.root, "tag", "v9.8.7")
        fixture_git(self.root, "tag", "opencode-v2.0.0")
        self.output = self.sandbox / "assets"

    def test_valid_tags_and_reject_shell_or_path_values(self):
        for tag in ("v1.2.3", "openai-v1.2.3", "claude-code-v1.2.3", "opencode-v1.2.3"):
            self.assertEqual(prepare.parse_tag(tag)[1], "1.2.3")
        for tag in ("v01.2.3", "v1.2", "v1.2.3;echo", "../v1.2.3", "other-v1.2.3", "v1.2.3\n"):
            with self.assertRaises(ValueError):
                prepare.parse_tag(tag)

    def test_core_is_complete_reproducible_and_has_bound_receipt(self):
        self.build()
        archive = next(self.output.glob("*.zip"))
        original = archive.read_bytes()
        with zipfile.ZipFile(io.BytesIO(original)) as bundle:
            self.assertEqual(set(bundle.namelist()), {"diamond-captain/SKILL.md", "diamond-captain/LICENSE"})
            self.assertEqual(bundle.read("diamond-captain/SKILL.md"), (self.root / prepare.builder.SOURCE / "SKILL.md").read_bytes())
        prepare.prepare(self.root, "v9.8.7", self.sandbox / "second", self.baseline)
        self.assertEqual(original, next((self.sandbox / "second").glob("*.zip")).read_bytes())

    def test_host_reuses_existing_builder_and_pinned_core(self):
        self.build("opencode-v2.0.0")
        expected = prepare.builder.build(self.root, "opencode", release=True)[2]
        self.assertEqual(next(self.output.glob("*.zip")).read_bytes(), expected)

    def test_old_tag_or_unaccepted_source_is_refused(self):
        fixture_git(self.root, "checkout", "--detach", "-q", self.baseline)
        with self.assertRaises(ValueError):
            prepare.prepare(self.root, "v9.8.6", self.output, self.baseline)
        fixture_git(self.root, "checkout", "--detach", "-q", self.commit)
        fixture_git(self.root, "update-ref", "refs/remotes/origin/main", self.baseline)
        with self.assertRaises(ValueError):
            prepare.prepare(self.root, "v9.8.7", self.output, self.baseline)
        self.assertFalse(self.output.exists())

    def test_dirty_source_and_output_inside_source_are_refused(self):
        (self.root / "uncommitted.txt").write_text("keep")
        with self.assertRaises(ValueError):
            prepare.prepare(self.root, "v9.8.7", self.output, self.baseline)
        (self.root / "uncommitted.txt").unlink()
        with self.assertRaises(ValueError):
            prepare.prepare(self.root, "v9.8.7", self.root / "dist", self.baseline)

    def test_different_existing_output_is_preserved(self):
        self.build()
        archive = next(self.output.glob("*.zip"))
        archive.write_bytes(b"existing candidate")
        with self.assertRaises(ValueError):
            prepare.prepare(self.root, "v9.8.7", self.output, self.baseline)
        self.assertEqual(archive.read_bytes(), b"existing candidate")

    def build(self, tag="v9.8.7"):
        return prepare.prepare(self.root, tag, self.output, self.baseline)

    def test_output_symlink_is_refused(self):
        destination = self.sandbox / "existing"
        destination.mkdir()
        self.output.symlink_to(destination, target_is_directory=True)
        with self.assertRaises(ValueError):
            self.build()
        self.assertEqual(list(destination.iterdir()), [])

    def test_tag_version_must_match_core_or_host_metadata(self):
        for tag in ("v9.8.8", "opencode-v2.0.1"):
            fixture_git(self.root, "tag", tag)
            with self.subTest(tag=tag), self.assertRaises(ValueError):
                self.build(tag)
        self.assertFalse(self.output.exists())
