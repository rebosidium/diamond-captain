"""Packaging and installation regressions; no providers or external writes."""
from __future__ import annotations

import importlib.util
import io
import json
import shutil
import subprocess
import tempfile
import unittest
import zipfile
from pathlib import Path
from contextlib import redirect_stdout
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


builder = load("build_distribution")
installer = load("install_distribution")


class DistributionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.stem, cls.manifest, cls.archive = builder.build(ROOT, "opencode")
        cls.core, _ = builder.pinned_core(ROOT, cls.manifest["distribution"], False)

    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.package = self.root / "package"
        with zipfile.ZipFile(io.BytesIO(self.archive)) as bundle:
            bundle.extractall(self.package)
        self.source = self.package / self.manifest["distribution"]["skill_root"]
        self.project = self.root / "project"
        self.project.mkdir()
        self.destination = self.project / ".opencode/skills/diamond-captain"
        quiet = redirect_stdout(io.StringIO())
        quiet.__enter__()
        self.addCleanup(quiet.__exit__, None, None, None)

    def test_reproducible_archive_and_exact_core_bytes(self):
        self.assertEqual(self.archive, builder.build(ROOT, "opencode")[2])
        source = self.core
        packaged = self.package / self.manifest["distribution"]["skill_root"]
        self.assertEqual(set(source), set(self.manifest["core"]["files"]))
        for name, data in source.items():
            self.assertEqual(data, (packaged / name).read_bytes(), name)

    def test_no_authored_skill_copies_in_distribution_definitions(self):
        self.assertEqual([], list((ROOT / "distributions").rglob("SKILL.md")))

    def test_dry_run_writes_nothing(self):
        installer.install(self.package, self.project, dry_run=True)
        self.assertEqual([], list(self.project.iterdir()))

    def test_invalid_backup_directory_is_rejected_without_installing(self):
        for name in (".diamond-captain-backups", ".diamond-captain-backups/opencode"):
            for dry_run in (True, False):
                with self.subTest(path=name, dry_run=dry_run):
                    project = self.root / f"blocked-{len(Path(name).parts)}-{dry_run}"
                    project.mkdir()
                    blocker = project / name
                    blocker.parent.mkdir(parents=True, exist_ok=True)
                    blocker.write_text("existing user file\n")
                    with self.assertRaises((ValueError, OSError)):
                        installer.install(self.package, project, dry_run=dry_run)
                    self.assertEqual("existing user file\n", blocker.read_text())
                    self.assertFalse((project / ".opencode").exists())

    def test_receipt_write_failure_preserves_fresh_and_existing_projects(self):
        original_open = Path.open

        def fail_receipt_write(path, mode="r", *args, **kwargs):
            if path.name.startswith("installed-") and "w" in mode:
                raise OSError("fixture: receipt write failed")
            return original_open(path, mode, *args, **kwargs)

        for replace in (False, True):
            with self.subTest(replace=replace):
                project = self.root / f"receipt-failure-{replace}"
                project.mkdir()
                state = project / ".product-task/TASK-STATE.md"
                state.parent.mkdir()
                state.write_text("existing active task\n")
                destination = project / ".opencode/skills/diamond-captain"
                if replace:
                    destination.mkdir(parents=True)
                    (destination / "old-only.md").write_text("old installation\n")

                def snapshot():
                    return {path.relative_to(project): path.read_bytes()
                            for path in project.rglob("*") if path.is_file()}

                before = snapshot()
                with patch.object(Path, "open", fail_receipt_write), \
                        self.assertRaisesRegex(OSError, "receipt write failed"):
                    installer.install(self.package, project, replace=replace)
                self.assertEqual(before, snapshot())
                if not replace:
                    self.assertFalse(destination.exists())

    def test_install_and_refuse_unrequested_overwrite(self):
        state = self.project / ".product-task/TASK-STATE.md"
        state.parent.mkdir()
        state.write_text("Keep active task state\n")
        installer.install(self.package, self.project)
        self.assertEqual(self.core["SKILL.md"],
                         (self.destination / "SKILL.md").read_bytes())
        with self.assertRaisesRegex(ValueError, "Already installed"):
            installer.install(self.package, self.project)
        self.assertEqual("Keep active task state\n", state.read_text())

    def test_replace_backs_up_whole_directory_outside_discovery(self):
        self.destination.mkdir(parents=True)
        (self.destination / "old-only.md").write_text("old installation")
        installer.install(self.package, self.project, replace=True)
        self.assertFalse((self.destination / "old-only.md").exists())
        backups = list((self.project / ".diamond-captain-backups/opencode").glob("*/old-only.md"))
        self.assertEqual(1, len(backups))
        self.assertEqual("old installation", backups[0].read_text())

    def test_missing_modified_and_unexpected_payload_files_are_rejected(self):
        payload = self.package / self.manifest["distribution"]["skill_root"]
        path = payload / "references/research.md"
        original = path.read_bytes()
        path.write_text("modified")
        with self.assertRaisesRegex(ValueError, "modified"):
            installer.install(self.package, self.project)
        path.unlink()
        with self.assertRaisesRegex(ValueError, "Missing"):
            installer.install(self.package, self.project)
        path.write_bytes(original)
        (payload / "unexpected.md").write_text("unexpected")
        with self.assertRaisesRegex(ValueError, "unexpected"):
            installer.install(self.package, self.project)
        self.assertEqual([], list(self.project.iterdir()))

    def test_symlink_in_destination_is_rejected_before_writing(self):
        outside = self.root / "outside"
        outside.mkdir()
        (self.project / ".opencode").symlink_to(outside, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "Symlink"):
            installer.install(self.package, self.project)
        self.assertEqual([], list(outside.iterdir()))

    def test_symlink_in_payload_is_rejected(self):
        payload = self.package / self.manifest["distribution"]["skill_root"]
        path = payload / "references/research.md"
        path.unlink()
        path.symlink_to(ROOT / builder.SOURCE / "references/research.md")
        with self.assertRaisesRegex(ValueError, "Symlink"):
            installer.install(self.package, self.project)

    def test_manifest_cannot_replace_project_root_or_escape(self):
        manifest_path = self.package / "DISTRIBUTION.json"
        original = json.loads(manifest_path.read_text())
        for invalid in (".", "../outside", "/tmp/outside", ".opencode/skills/../other"):
            original["distribution"]["skill_root"] = invalid
            manifest_path.write_text(json.dumps(original))
            with self.assertRaises(ValueError):
                installer.install(self.package, self.project, replace=True)
        self.assertEqual([], list(self.project.iterdir()))

    def test_wrong_core_pin_is_rejected(self):
        root = self.root / "mismatched-source"
        canonical = root / builder.SOURCE
        canonical.mkdir(parents=True)
        (canonical / "SKILL.md").write_bytes((ROOT / builder.SOURCE / "SKILL.md").read_bytes())
        (canonical / "LICENSE").write_text("fixture")
        adapter = root / "distributions/opencode"
        adapter.mkdir(parents=True)
        config = json.loads((ROOT / "distributions/opencode/distribution.json").read_text())
        config["core_version"] = "999.0.0"
        (adapter / "distribution.json").write_text(json.dumps(config))
        with self.assertRaisesRegex(ValueError, "Core version changed"):
            builder.build(root, "opencode")

    def test_canonical_symlinks_are_not_bundled(self):
        root = self.root / "source-with-symlink"
        canonical = root / builder.SOURCE
        canonical.mkdir(parents=True)
        (canonical / "SKILL.md").symlink_to(ROOT / builder.SOURCE / "SKILL.md")
        with self.assertRaisesRegex(ValueError, "symlinks"):
            builder.source_files(root)

    def test_same_version_content_drift_is_rejected(self):
        root = self.root / "drifted-source"
        shutil.copytree(self.source, root / builder.SOURCE)
        shutil.copytree(ROOT / "distributions/opencode", root / "distributions/opencode")
        (root / builder.SOURCE / "LICENSE").write_text("changed without a version bump")
        with self.assertRaisesRegex(ValueError, "pinned dependency"):
            builder.build(root, "opencode")

    def test_failed_replacement_restores_previous_installation(self):
        self.destination.mkdir(parents=True)
        (self.destination / "old-only.md").write_text("keep me")
        original_rename = Path.rename

        def fail_staged_rename(path, target):
            if path.is_dir() and any(part.startswith(".diamond-captain-stage-") for part in path.parts):
                raise OSError("fixture: staged rename failed")
            return original_rename(path, target)

        with patch.object(Path, "rename", fail_staged_rename), self.assertRaises(OSError):
            installer.install(self.package, self.project, replace=True)
        self.assertEqual("keep me", (self.destination / "old-only.md").read_text())
        self.assertEqual([], list(self.project.rglob("installed-*.json")))

    def test_release_build_rejects_uncommitted_work(self):
        with patch.object(builder, "git", return_value="?? uncommitted-file"), \
                self.assertRaisesRegex(ValueError, "clean, committed"):
            builder.build(ROOT, "opencode", release=True)

    def test_tagged_version_cannot_be_rebuilt_at_another_commit(self):
        real_git = builder.git
        real_tag_commit = builder.tag_commit

        def clean_git(root, *args):
            return "" if args[0] == "status" else real_git(root, *args)

        with patch.object(builder, "git", clean_git), \
                patch.object(builder, "tag_commit", side_effect=lambda root, tag:
                             "0" * 40 if tag.startswith("opencode-") else real_tag_commit(root, tag)), \
                self.assertRaisesRegex(ValueError, "already tagged"):
            builder.build(ROOT, "opencode", release=True)

    def test_every_service_bundles_the_same_complete_core(self):
        for config_path in sorted((ROOT / "distributions").glob("*/distribution.json")):
            service = config_path.parent.name
            with self.subTest(service=service):
                _, manifest, data = builder.build(ROOT, service)
                core, _ = builder.pinned_core(ROOT, manifest["distribution"], False)
                with zipfile.ZipFile(io.BytesIO(data)) as bundle:
                    prefix = manifest["distribution"]["skill_root"] + "/"
                    actual = {name[len(prefix):]: bundle.read(name) for name in bundle.namelist()
                              if name.startswith(prefix)}
                    self.assertEqual(core, actual)
                    kind = manifest["distribution"]["kind"]
                    if kind in {"claude-plugin", "agent-plugin"}:
                        path = ".claude-plugin/plugin.json" if kind == "claude-plugin" else "plugin.json"
                        plugin = json.loads(bundle.read(path))
                        self.assertEqual(manifest["distribution"]["version"], plugin["version"])
                        self.assertNotIn("install.py", bundle.namelist())
                        self.assertNotIn("hooks/hooks.json", bundle.namelist())
                        if kind == "agent-plugin":
                            self.assertEqual("https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
                                             plugin["$schema"])
                        marketplace = ".agents/plugins/marketplace.json"
                        if marketplace in bundle.namelist():
                            catalog = json.loads(bundle.read(marketplace))
                            self.assertEqual(plugin["name"], catalog["plugins"][0]["name"])
                            self.assertEqual("./", catalog["plugins"][0]["source"]["path"])

    def test_service_keeps_pinned_core_when_canonical_version_advances(self):
        root = self.root / "versioned-source"
        shutil.copytree(self.source, root / builder.SOURCE)
        shutil.copytree(ROOT / "distributions/opencode", root / "distributions/opencode")
        (root / "scripts").mkdir()
        shutil.copyfile(ROOT / "scripts/install_distribution.py", root / "scripts/install_distribution.py")

        def git(*args):
            return subprocess.check_output([
                "git", "-C", str(root), "-c", "user.name=Distribution test",
                "-c", "user.email=distribution-test@example.invalid", *args,
            ], text=True, stderr=subprocess.DEVNULL).strip()

        git("init", "-q")
        git("add", ".")
        git("commit", "-qm", "fixture: pinned core")
        old_commit = git("rev-parse", "HEAD")
        pinned_version = self.manifest["core"]["version"]
        git("tag", "-a", f"v{pinned_version}", "-m", "fixture release")
        entry = root / builder.SOURCE / "SKILL.md"
        original = entry.read_bytes()
        major, minor, patch_version = map(int, pinned_version.split("."))
        newer_version = f"{major}.{minor}.{patch_version + 1}"
        entry.write_bytes(original.replace(f'version: "{pinned_version}"'.encode(),
                                           f'version: "{newer_version}"'.encode()) + b"\nNew core behavior\n")
        git("add", ".")
        git("commit", "-qm", "fixture: core advances independently")
        _, manifest, data = builder.build(root, "opencode", release=True)
        self.assertEqual(pinned_version, manifest["core"]["version"])
        self.assertEqual(old_commit, manifest["core"]["source_commit"])
        with zipfile.ZipFile(io.BytesIO(data)) as bundle:
            self.assertEqual(original, bundle.read(".opencode/skills/diamond-captain/SKILL.md"))
        self.assertIn(f'version: "{newer_version}"'.encode(), entry.read_bytes())


if __name__ == "__main__":
    unittest.main()
