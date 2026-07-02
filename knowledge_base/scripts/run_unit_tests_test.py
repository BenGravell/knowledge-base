from __future__ import annotations

import unittest

from knowledge_base.scripts.run_unit_tests import selected_test_modules


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
        modules = selected_test_modules(["knowledge_base/config.py"])

        self.assertIn("knowledge_base.catalog_test", modules)
        self.assertIn("knowledge_base.scripts.run_unit_tests_test", modules)


if __name__ == "__main__":
    unittest.main()
