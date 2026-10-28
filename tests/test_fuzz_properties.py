"""The real fuzz properties also run as bounded deterministic regressions."""
from __future__ import annotations

import importlib.util
import random
import unittest
from pathlib import Path
from unittest.mock import patch

spec = importlib.util.spec_from_file_location("installer_fuzz_properties", Path(__file__).resolve().parents[1] / "fuzz/installer_fuzzer.py")
fuzzer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fuzzer)


class FuzzPropertyTests(unittest.TestCase):
    def test_all_modes_with_legitimate_and_adversarial_values(self):
        for mode in range(8):
            for value in (b"", b"../escape", b"/absolute", b"a\\b", b".opencode/skills/diamond-captain/SKILL.md", b"\x00", b"\xff", b"settings"):
                with self.subTest(mode=mode, value=value):
                    fuzzer.test_one_input(bytes([mode]) + value)

    def test_deterministic_bounded_mutations(self):
        generator = random.Random(67291)
        for _ in range(128):
            data = bytes(generator.randrange(256) for _ in range(generator.randrange(0, 100)))
            fuzzer.test_one_input(data)

    def test_oversized_input_is_not_processed(self):
        fuzzer.test_one_input(b"x" * 4097)

    def test_properties_detect_an_escaped_destination(self):
        with patch.object(fuzzer.installer, "install", return_value=Path("/synthetic-outside")):
            with self.assertRaises(ValueError):
                fuzzer.test_one_input(b"\x01safe-name")

    def test_valid_control_detects_an_installer_that_rejects_everything(self):
        with patch.object(fuzzer.installer, "install", side_effect=ValueError("reject all")):
            with self.assertRaises(ValueError):
                fuzzer.test_one_input(b"\x05synthetic-valid")


if __name__ == "__main__":
    unittest.main()
