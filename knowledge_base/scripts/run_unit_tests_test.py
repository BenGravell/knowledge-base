from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import time
import unittest
from pathlib import Path

from knowledge_base.scripts.run_unit_tests import REPO_ROOT, selected_test_modules


class RunUnitTestsSelectionTests(unittest.TestCase):
    def test_test_file_runs_itself(self) -> None:
        self.assertEqual(
            selected_test_modules(["knowledge_base/catalog_test.py"]),
            ["knowledge_base.catalog_test"],
        )

    def test_source_file_runs_adjacent_test(self) -> None:
        self.assertEqual(
            selected_test_modules(["knowledge_base/catalog.py"]),
            ["knowledge_base.catalog_test"],
        )

    def test_source_without_adjacent_test_runs_full_suite(self) -> None:
        modules = selected_test_modules(["knowledge_base/no_adjacent_test_fixture.py"])

        self.assertIn("knowledge_base.catalog_test", modules)
        self.assertIn("knowledge_base.scripts.run_unit_tests_test", modules)


class RunUnitTestsTimingTests(unittest.TestCase):
    def run_fixture(self, source: str) -> subprocess.CompletedProcess[str]:
        with tempfile.TemporaryDirectory() as directory:
            Path(directory, "timing_fixture.py").write_text(source, encoding="utf-8")
            return subprocess.run(
                [
                    sys.executable,
                    "-c",
                    "from knowledge_base.scripts import run_unit_tests as runner; "
                    "runner.selected_test_modules = lambda _: ['timing_fixture']; "
                    "raise SystemExit(runner.main([]))",
                ],
                cwd=REPO_ROOT,
                env={
                    **os.environ,
                    "PYTHONPATH": directory,
                    "KB_TEST_STARTED_AT": str(time.time()),
                },
                capture_output=True,
                text=True,
                check=False,
                timeout=5,
            )

    def test_failure_reports_all_phase_times_and_test_name(self) -> None:
        result = self.run_fixture(
            "import unittest\n"
            "class Example(unittest.TestCase):\n"
            "    def test_failure(self):\n"
            "        self.fail('intentional failure')\n"
        )
        self.assertEqual(result.returncode, 1, result.stderr)
        for label in (
            "environment and Python startup",
            "test selection",
            "load timing_fixture",
            "test execution",
            "Python runner total",
        ):
            self.assertRegex(result.stderr, rf"{label}: \d+\.\d{{3}}s")
        self.assertIn("test_failure", result.stderr)
        self.assertIn("intentional failure", result.stderr)

    def test_timeout_reports_active_phase_even_with_test_output_buffered(self) -> None:
        terminate = "import os, signal; os.kill(os.getpid(), signal.SIGTERM)"
        for phase, source in (
            ("load timing_fixture", terminate),
            (
                "test execution",
                "import unittest\n"
                "class Example(unittest.TestCase):\n"
                "    def test_timeout(self):\n"
                f"        {terminate}\n",
            ),
        ):
            with self.subTest(phase=phase):
                result = self.run_fixture(source)
                self.assertEqual(result.returncode, 124, result.stderr)
                self.assertIn(f"TIMEOUT during {phase}:", result.stderr)
                self.assertIn("Python runner total:", result.stderr)
                if phase == "test execution":
                    self.assertIn("test_timeout", result.stderr)


if __name__ == "__main__":
    unittest.main()
