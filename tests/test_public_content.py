"""Publication regressions: nested payloads, deleted ancestors and metadata."""
import importlib.util
import io
import subprocess
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("guard", ROOT / "scripts/check_public_content.py")
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)


class PublicContentTests(unittest.TestCase):
    def test_private_paths_are_rejected_even_with_innocent_contents(self):
        for path in ("docs/" + "audits/result.md", "private-archives/backup.zip",
                     "data/events." + "jsonl", ".product-task/state.md"):
            with self.subTest(path=path):
                self.assertTrue(guard.check_entries({path: b"ordinary text"}))

    def test_private_values_are_detected_without_echoing_them(self):
        values = ["/Users/" + "actual-owner/project/file",
                  '"input_' + 'tokens": 123',
                  '"thread' + 'Id": "01234567-1234-1234-1234-123456789abc"',
                  "person@" + "gmail.com",
                  "https://chatgpt.com/" + "space/private-page"]
        for value in values:
            with self.subTest(category=values.index(value)):
                failures = guard.check_entries({"example.md": value.encode()})
                self.assertTrue(failures)
                self.assertNotIn(value, "\n".join(failures))

    def test_nested_release_archive_is_inspected(self):
        inner = io.BytesIO()
        with zipfile.ZipFile(inner, "w") as bundle:
            bundle.writestr("notes.md", "/Users/" + "actual-owner/project/file")
        outer = io.BytesIO()
        with zipfile.ZipFile(outer, "w") as bundle:
            bundle.writestr("payload.zip", inner.getvalue())
        failures = guard.check_entries({"release.zip": outer.getvalue()})
        self.assertTrue(any("release.zip!payload.zip!notes.md" in item for item in failures))

    def test_source_and_anonymous_test_data_are_allowed(self):
        self.assertEqual([], guard.check_entries({"tests/fixtures/example.csv": b"segment,count\na,2\n",
                                                  "README.md": b"Checks passed; live runtime remains unverified.\n"}))

    def test_deleted_private_ancestor_blocks_publication(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            def git(*args):
                return subprocess.check_output(["git", "-C", folder, *args], stderr=subprocess.DEVNULL)
            git("init", "-q")
            git("config", "user.name", "Fixture")
            git("config", "user.email", "fixture@users.noreply.github.com")
            (root / "notes.md").write_text('"output_' + 'tokens": 123\n')
            git("add", ".")
            git("commit", "-qm", "Initial fixture")
            (root / "notes.md").write_text("Clean latest file\n")
            git("add", ".")
            git("commit", "-qm", "Clean latest fixture")
            self.assertEqual([], guard.check_entries(guard.tree_entries(root, "HEAD")))
            self.assertTrue(guard.check_history(root, ["HEAD"]))

    def test_staged_guard_uses_index_instead_of_worktree(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            subprocess.run(["git", "init", "-q", folder], check=True)
            (root / "notes.md").write_text("Clean staged file\n")
            subprocess.run(["git", "-C", folder, "add", "."], check=True)
            (root / "notes.md").write_text('"output_' + 'tokens": 123\n')
            self.assertEqual([], guard.check_entries(guard.tree_entries(root, None)))


if __name__ == "__main__":
    unittest.main()
