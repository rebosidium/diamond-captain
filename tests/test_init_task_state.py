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


class MinimalIntakeTests(unittest.TestCase):
    def test_minimal_keeps_request_and_snapshot_without_future_findings(self):
        with tempfile.TemporaryDirectory() as temporary:
            state = Path(temporary) / "TASK-STATE.md"
            snapshot = Path(temporary) / "initial.md"
            request = "Synthetic copy fix\nwith a second supplied line"
            receipt = initializer.initialize(state, "minimal", request, snapshot=snapshot, minimal=True)
            content = state.read_text()
            self.assertEqual(5, len([line for line in content.splitlines() if line.startswith("- ")]))
            self.assertIn(json.dumps(request), content)
            self.assertIn("phase unknown, not selected", content)
            self.assertIn("handoff acceptance pending", content)
            self.assertTrue(receipt["intake_only"])
            self.assertEqual(state.read_bytes(), snapshot.read_bytes())
            original = state.read_bytes()
            with self.assertRaises(FileExistsError):
                initializer.initialize(state, "minimal", request, minimal=True)
            self.assertEqual(original, state.read_bytes())
            with self.assertRaises(FileExistsError):
                initializer.initialize(state, "full", request)
            self.assertEqual(original, state.read_bytes())

    def test_minimal_cli_phase_and_dangling_symlink(self):
        with tempfile.TemporaryDirectory() as temporary:
            state = Path(temporary) / "TASK-STATE.md"
            command = [sys.executable, str(SCRIPT), "--state", str(state),
                       "--task-id", "minimal", "--phase", "3", "--minimal"]
            first = subprocess.run(command, input="Synthetic local fix", text=True,
                                   capture_output=True, check=True)
            self.assertTrue(json.loads(first.stdout)["intake_only"])
            self.assertIn("phase 3, supplied by user", state.read_text())
            original = state.read_bytes()
            self.assertNotEqual(0, subprocess.run(command, input="request", text=True,
                                                capture_output=True).returncode)
            self.assertEqual(original, state.read_bytes())
            state.unlink()
            outside = Path(temporary) / "untouched.md"
            state.symlink_to(outside)
            with self.assertRaises(FileExistsError):
                initializer.initialize(state, "minimal", "request", minimal=True)
            self.assertFalse(outside.exists())


MEMORY_SCRIPT = SCRIPT.with_name("init_product_memory.py")
memory_spec = importlib.util.spec_from_file_location("init_product_memory", MEMORY_SCRIPT)
memory_initializer = importlib.util.module_from_spec(memory_spec)
memory_spec.loader.exec_module(memory_initializer)


class ProductMemoryTests(unittest.TestCase):
    def test_only_header_facts_are_filled(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "product/PRODUCT-MEMORY.md"
            receipt = memory_initializer.initialize(target, "Synthetic service")
            content = target.read_text()
            expected = memory_initializer.TEMPLATE.read_text()
            for label, value in (("Product / service", "Synthetic service"),
                                 ("Memory path", str(target)),
                                 ("Last reconciled (date/time + timezone)", receipt["recorded_at"])):
                expected = expected.replace(f"- {label}:\n", f"- {label}: {value}\n")
            self.assertEqual(expected, content)
            self.assertTrue(receipt["header_only"])
            self.assertEqual(hashlib.sha256(target.read_bytes()).hexdigest(), receipt["sha256"])
            self.assertIn("- Owner: unassigned", content)

    def test_existing_and_dangling_symlink_are_preserved(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "memory.md"
            target.write_text("existing memory")
            with self.assertRaises(FileExistsError):
                memory_initializer.initialize(target, "Synthetic service")
            self.assertEqual("existing memory", target.read_text())
            target.unlink()
            outside = Path(temporary) / "not-created.md"
            target.symlink_to(outside)
            with self.assertRaises(FileExistsError):
                memory_initializer.initialize(target, "Synthetic service")
            self.assertFalse(outside.exists())

    def test_invalid_name_writes_nothing(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "memory.md"
            for product in (" ", "name\nextra", "name\rextra"):
                with self.assertRaises(ValueError):
                    memory_initializer.initialize(target, product)
                self.assertFalse(target.exists())

    def test_failed_write_or_close_removes_only_new_memory(self):
        for failure in ("write", "close"):
            with self.subTest(failure=failure), tempfile.TemporaryDirectory() as temporary:
                target = Path(temporary) / "memory.md"
                unrelated = Path(temporary) / "unrelated.md"
                unrelated.write_text("preserve")
                original_open = Path.open

                class BrokenStream:
                    def __enter__(self):
                        self.stream = original_open(target, "xb")
                        return self

                    def write(self, data):
                        self.stream.write(data[:7] if failure == "write" else data)
                        if failure == "write":
                            raise OSError("fixture: write failed")

                    def __exit__(self, *args):
                        self.stream.close()
                        if failure == "close":
                            raise OSError("fixture: close failed")

                def open_memory(path, mode="r", *args, **kwargs):
                    return BrokenStream() if path == target and mode == "xb" else original_open(path, mode, *args, **kwargs)

                with patch.object(Path, "open", open_memory), self.assertRaises(OSError):
                    memory_initializer.initialize(target, "Synthetic service")
                self.assertFalse(target.exists())
                self.assertEqual("preserve", unrelated.read_text())

    def test_cli_receipt_and_clear_refusal(self):
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "memory.md"
            command = [sys.executable, str(MEMORY_SCRIPT), "--memory", str(target),
                       "--product", "Synthetic service"]
            first = subprocess.run(command, text=True, capture_output=True, check=True)
            self.assertTrue(json.loads(first.stdout)["header_only"])
            original = target.read_bytes()
            second = subprocess.run(command, text=True, capture_output=True)
            self.assertNotEqual(0, second.returncode)
            self.assertIn("Preserve existing file", second.stderr)
            self.assertEqual(original, target.read_bytes())


if __name__ == "__main__":
    unittest.main()
