"""Regression tests for settings geometry and the mandatory build gate."""

from __future__ import annotations

import unittest
from copy import deepcopy
from typing import Any, override
from unittest.mock import patch

from knowledge_base import dev_cli
from knowledge_base.scripts.verify_map_view.layout import layout_failures


def rectangle(name: str, left: int, top: int, right: int, bottom: int) -> dict[str, Any]:
    return {"name": name, "left": left, "top": top, "right": right, "bottom": bottom}


class SettingsLayoutTests(unittest.TestCase):
    @override
    def setUp(self) -> None:
        self.snapshot = {
            "header": rectangle("header", 0, 0, 300, 120),
            "controls": [rectangle(str(i), i * 25, 0, i * 25 + 25, 20) for i in range(7)],
            "overflow": [],
            "panels": [rectangle("panel", 0, 130, 300, 300)],
            "viewport": rectangle("viewport", 0, 0, 300, 844),
            "dock": rectangle("dock", 0, 790, 300, 844),
            "toggle": rectangle("toggle", 1, 791, 299, 843),
            "branch": rectangle("branch", 1, 791, 299, 791),
            "expanded": False,
            "inert": True,
            "toggleReachable": True,
        }

    def test_wrapped_layout_and_touching_edges_pass(self) -> None:
        self.assertEqual(layout_failures(self.snapshot, 320), [])

    def test_rejects_each_failure_mode(self) -> None:
        cases = [
            ("horizontal overflow", lambda s: s["overflow"].append("controls")),
            ("collision", lambda s: s["controls"][1].update(left=20)),
            ("clipped control", lambda s: s["controls"][0].update(left=-5)),
            ("exceeds viewport", lambda s: s["header"].update(right=350)),
            ("panel overlaps", lambda s: s["panels"][0].update(top=100)),
            ("missing settings", lambda s: s["controls"].clear()),
            ("span the viewport bottom", lambda s: s["dock"].update(bottom=700)),
            ("span the dock bottom", lambda s: s["toggle"].update(right=250)),
            ("share width", lambda s: s["branch"].update(right=250)),
            ("reveal above", lambda s: s["branch"].update(bottom=700)),
            ("height must match", lambda s: s["branch"].update(top=700)),
            ("must be inert", lambda s: s.update(inert=False)),
            ("remain reachable", lambda s: s.update(toggleReachable=False)),
        ]
        for message, mutate in cases:
            with self.subTest(message=message):
                snapshot = deepcopy(self.snapshot)
                mutate(snapshot)
                self.assertTrue(any(message in failure for failure in layout_failures(snapshot, 320)))

    def test_branch_expands_upward_with_toggle_anchored(self) -> None:
        self.snapshot["dock"]["top"] = 400
        self.snapshot["branch"]["top"] = 401
        self.snapshot.update(expanded=True, inert=False)
        self.assertEqual(layout_failures(self.snapshot, 320), [])

    @patch.object(dev_cli, "run_zensical", return_value=0)
    @patch.object(dev_cli, "validate_site_output", return_value=True)
    def test_build_requires_layout_check(self, _output, _build) -> None:
        with patch.object(dev_cli, "verify_settings_layout") as verify:
            self.assertEqual(dev_cli.build_site([]), 0)
            verify.assert_called_once_with(dev_cli.SITE_DIR)
        for error in (AssertionError("collision"), RuntimeError("Chrome missing")):
            with self.subTest(error=error), patch.object(dev_cli, "verify_settings_layout", side_effect=error):
                self.assertEqual(dev_cli.build_site([]), 1)


if __name__ == "__main__":
    unittest.main()
