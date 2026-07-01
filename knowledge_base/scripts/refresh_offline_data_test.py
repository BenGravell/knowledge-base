from __future__ import annotations

import argparse
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from knowledge_base.scripts import refresh_offline_data as refresh


def default_args(**overrides: object) -> argparse.Namespace:
    values: dict[str, object] = {
        "audit_severity": "error",
        "fastembed_device": "auto",
        "force": False,
        "full_build": False,
        "map_backend": "fastembed",
        "no_fast_path": False,
        "skip_audit": False,
        "skip_build": False,
        "skip_force_layout": False,
        "skip_map": False,
        "skip_semantic_search": False,
        "strict": False,
    }
    values.update(overrides)
    return argparse.Namespace(**values)


class RefreshOfflineDataTests(unittest.TestCase):
    def test_clean_fallback_ignores_untracked_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            input_path = root / "knowledge_base" / "docs" / "input.md"
            output_path = root / "knowledge_base" / "map" / "generated" / "map-data.js"
            state_path = root / "knowledge_base" / ".generated" / "refresh-state.json"
            input_path.parent.mkdir(parents=True)
            output_path.parent.mkdir(parents=True)
            input_path.write_text("tracked input\n", encoding="utf-8")
            output_path.write_text("generated output\n", encoding="utf-8")

            subprocess.run(["git", "init"], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=root, check=True)
            subprocess.run(["git", "config", "user.name", "Test User"], cwd=root, check=True)
            subprocess.run(["git", "add", "knowledge_base/docs/input.md"], cwd=root, check=True)
            subprocess.run(["git", "commit", "-m", "initial"], cwd=root, stdout=subprocess.DEVNULL, check=True)
            input_path.with_name("scratch.md").write_text("untracked input\n", encoding="utf-8")

            with (
                patch.object(refresh, "REPO_ROOT", root),
                patch.object(refresh, "REFRESH_STATE_PATH", state_path),
                patch.object(refresh, "HOT_START_STATUS_PATHS", ("knowledge_base/docs",)),
                patch.object(refresh, "HOT_START_REQUIRED_FILES", (output_path,)),
                patch.object(refresh, "site_has_paper_pages", return_value=True),
            ):
                fast_path, reason = refresh.hot_start_fast_path(default_args())

                self.assertTrue(fast_path)
                self.assertEqual(reason, "tracked refresh files are clean")

    def test_refresh_state_allows_dirty_but_current_hot_start(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            input_path = root / "knowledge_base" / "docs" / "input.md"
            output_path = root / "knowledge_base" / "map" / "generated" / "map-data.js"
            state_path = root / "knowledge_base" / ".generated" / "refresh-state.json"
            input_path.parent.mkdir(parents=True)
            output_path.parent.mkdir(parents=True)
            input_path.write_text("old input\n", encoding="utf-8")
            output_path.write_text("generated output\n", encoding="utf-8")

            subprocess.run(["git", "init"], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            subprocess.run(["git", "add", "knowledge_base/docs/input.md"], cwd=root, check=True)
            input_path.write_text("dirty but refreshed input\n", encoding="utf-8")

            with (
                patch.object(refresh, "REPO_ROOT", root),
                patch.object(refresh, "REFRESH_STATE_PATH", state_path),
                patch.object(refresh, "HOT_START_STATUS_PATHS", ("knowledge_base/docs",)),
                patch.object(refresh, "HOT_START_REQUIRED_FILES", (output_path,)),
                patch.object(refresh, "site_has_paper_pages", return_value=True),
            ):
                self.assertIsNone(refresh.write_refresh_state())

                fast_path, reason = refresh.hot_start_fast_path(default_args())

                self.assertTrue(fast_path)
                self.assertIn("refresh state stamp matches", reason)

                output_path.write_text("generated output changed outside tracked state\n", encoding="utf-8")
                fast_path, reason = refresh.hot_start_fast_path(default_args())

                self.assertTrue(fast_path)
                self.assertIn("refresh state stamp matches", reason)

                input_path.write_text("changed after refresh\n", encoding="utf-8")
                fast_path, reason = refresh.hot_start_fast_path(default_args())

                self.assertFalse(fast_path)
                self.assertEqual(reason, "refresh state stamp is stale")

    def test_generated_step_state_skips_when_outputs_and_inputs_match(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            input_path = root / "knowledge_base" / "docs" / "input.md"
            output_path = root / "knowledge_base" / "components" / "semantic_search" / "semantic-search-index.json"
            state_path = root / "knowledge_base" / ".generated" / "semantic-search-refresh-state.json"
            input_path.parent.mkdir(parents=True)
            output_path.parent.mkdir(parents=True)
            input_path.write_text("tracked input\n", encoding="utf-8")
            output_path.write_text("generated output\n", encoding="utf-8")

            subprocess.run(["git", "init"], cwd=root, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True)
            subprocess.run(["git", "add", "knowledge_base/docs/input.md"], cwd=root, check=True)

            step = refresh.Step("Generate", "Semantic Search", "Regenerate Semantic Search", ["semantic"])
            with (
                patch.object(refresh, "REPO_ROOT", root),
                patch.object(refresh, "HOT_START_STATUS_PATHS", ("knowledge_base/docs",)),
                patch.object(refresh, "GENERATED_STEP_STATE_PATHS", {"Semantic Search": state_path}),
                patch.object(refresh, "GENERATED_STEP_REQUIRED_FILES", {"Semantic Search": (output_path,)}),
            ):
                self.assertIsNone(refresh.write_step_refresh_state(step))

                skip, reason = refresh.generated_step_can_hot_start(step, default_args())

                self.assertTrue(skip)
                self.assertIn("refresh state stamp matches", reason)

                self.assertFalse(refresh.generated_step_can_hot_start(step, default_args(no_fast_path=True))[0])

                input_path.write_text("changed after semantic search\n", encoding="utf-8")
                skip, reason = refresh.generated_step_can_hot_start(step, default_args())

                self.assertFalse(skip)
                self.assertEqual(reason, "refresh state stamp is stale")


if __name__ == "__main__":
    unittest.main()
