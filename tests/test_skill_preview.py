"""Frozen development transport checks, independent of release version pins."""
import io
import json
import sys
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_distribution as builder
import build_skill_preview as preview


class PreviewTests(unittest.TestCase):
    def test_exact_committed_core_and_reproducible_transport(self):
        commit = builder.git(ROOT, "rev-parse", "HEAD")
        data, receipt = preview.build(commit)
        self.assertEqual((data, receipt), preview.build(commit))
        core = builder.source_at_commit(ROOT, commit)
        with zipfile.ZipFile(io.BytesIO(data)) as bundle:
            prefix = "skills/diamond-captain/"
            actual = {name[len(prefix):]: bundle.read(name) for name in bundle.namelist()
                      if name.startswith(prefix)}
            self.assertEqual(core, actual)
            plugin = json.loads(bundle.read("plugin.json"))
            self.assertNotIn("version", plugin)
            description = next(line.partition(": ")[2] for line in core["SKILL.md"].decode().splitlines()
                               if line.startswith("description: "))
            self.assertEqual(description, plugin["description"])
            self.assertEqual(set(bundle.namelist()), {prefix + name for name in core} | {"plugin.json"})
        self.assertFalse(receipt["release"])
        self.assertEqual(commit, receipt["source_commit"])
        self.assertEqual(builder.digest(data), receipt["archive_sha256"])

    def test_invalid_plugin_identity(self):
        for name in ("../outside", "A bad plugin", ""):
            with self.subTest(name=name), self.assertRaises(ValueError):
                preview.build("HEAD", name)

    def test_private_core_is_rejected_before_export(self):
        core = builder.source_at_commit(ROOT, "HEAD")
        core["internal.md"] = ("/Users/" + "fixture-owner/private.txt").encode()
        with patch.object(preview, "source_at_commit", return_value=core), \
                self.assertRaisesRegex(ValueError, "Private material"):
            preview.build("HEAD")


if __name__ == "__main__":
    unittest.main()
