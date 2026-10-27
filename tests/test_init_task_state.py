"""Intake initialization safety and snapshot regressions; no model calls."""
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / ".agents/skills/diamond-captain/scripts/init_task_state.py"
spec = importlib.util.spec_from_file_location("init_task_state", SCRIPT)
initializer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(initializer)


class IntakeTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.state = self.root / "task/TASK-STATE.md"
        self.snapshot = self.root / "task/initial.md"

    def test_intake_snapshot_is_preserved_after_later_edits(self):
        receipt = initializer.initialize(self.state, "SYNTHETIC", "A fictional service request", 2, self.snapshot)
        original = self.state.read_bytes()
        self.assertEqual(original, self.snapshot.read_bytes())
        self.assertEqual(hashlib.sha256(original).hexdigest(), receipt["sha256"])
        self.assertNotIn(b"### R-002", original)
        self.assertIn(b"| | | |", original)  # Later criteria stay unfilled.
        self.state.write_text("Later authorized checkpoint")
        self.assertEqual(original, self.snapshot.read_bytes())

    def test_existing_active_state_or_snapshot_is_never_overwritten(self):
        for target in (self.state, self.snapshot):
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text("existing user work")
            with self.assertRaises(FileExistsError):
                initializer.initialize(self.state, "SYNTHETIC", "request", snapshot=self.snapshot)
            self.assertEqual("existing user work", target.read_text())
            target.unlink()

    def test_invalid_intake_writes_nothing(self):
        for task_id, request, phase in (("../escape", "request", None), ("safe", "", 2), ("safe", "request", 7)):
            with self.subTest(task_id=task_id, phase=phase), self.assertRaises(ValueError):
                initializer.initialize(self.state, task_id, request, phase)
            self.assertFalse(self.state.exists())

    def test_symlink_target_is_not_followed(self):
        outside = self.root / "other"
        outside.mkdir()
        self.state.parent.mkdir()
        self.state.symlink_to(outside / "state.md")
        with self.assertRaises(FileExistsError):
            initializer.initialize(self.state, "SYNTHETIC", "request")
        self.assertEqual([], list(outside.iterdir()))

    def test_snapshot_failure_rolls_back_only_new_files(self):
        original = Path.open
        unrelated = self.root / "unrelated.md"
        unrelated.write_text("preserve")

        def fail_snapshot(path, mode="r", *args, **kwargs):
            if path == self.snapshot and mode == "xb":
                raise OSError("fixture: snapshot write failed")
            return original(path, mode, *args, **kwargs)

        with patch.object(Path, "open", fail_snapshot), self.assertRaises(OSError):
            initializer.initialize(self.state, "SYNTHETIC", "request", snapshot=self.snapshot)
        self.assertFalse(self.state.exists())
        self.assertEqual("preserve", unrelated.read_text())

    def test_cli_stdin_is_stored_as_data(self):
        request = "A literal request: `example` and $(example), no shell execution."
        result = subprocess.run([sys.executable, str(SCRIPT), "--state", str(self.state),
                                 "--task-id", "SYNTHETIC"], input=request, text=True,
                                capture_output=True, check=True)
        self.assertTrue(json.loads(result.stdout)["intake_only"])
        self.assertIn(request, self.state.read_text())


if __name__ == "__main__":
    unittest.main()
