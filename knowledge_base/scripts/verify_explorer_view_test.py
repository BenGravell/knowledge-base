"""Regression tests for settings geometry and the mandatory build gate."""

from __future__ import annotations

import unittest
from copy import deepcopy
from typing import Any, override
from unittest.mock import patch

from knowledge_base import dev_cli
from knowledge_base.scripts.verify_explorer_view import layout_failures, mode_switch_failures


def rectangle(name: str, left: int, top: int, right: int, bottom: int) -> dict[str, Any]:
    return {"name": name, "left": left, "top": top, "right": right, "bottom": bottom}


class SettingsLayoutTests(unittest.TestCase):
    @override
    def setUp(self) -> None:
        self.snapshot = {
            "header": rectangle("header", 0, 0, 300, 120),
            "controls": [rectangle(str(i), i * 25, 0, i * 25 + 25, 20) for i in range(7)],
            "overflow": [],
            "main": rectangle("main", 0, 120, 300, 790),
            "viewport": rectangle("viewport", 0, 120, 300, 844),
            "dock": rectangle("dock", 0, 790, 300, 844),
            "toggle": rectangle("toggle", 1, 791, 299, 843),
            "branch": rectangle("branch", 1, 791, 299, 791),
            "expanded": False,
            "inert": True,
            "toggleReachable": True,
            "sameSelector": True,
            "selection": ["root"],
            "visibleModes": ["map"],
        }

    def test_wrapped_layout_and_touching_edges_pass(self) -> None:
        self.assertEqual(layout_failures(self.snapshot, 320), [])

    def test_workspace_can_start_below_header_gap(self) -> None:
        self.snapshot["viewport"]["top"] = 126
        self.snapshot["main"]["top"] = 126
        self.assertEqual(layout_failures(self.snapshot, 320), [])

    def test_rejects_each_failure_mode(self) -> None:
        cases = [
            ("horizontal overflow", lambda s: s["overflow"].append("controls")),
            ("collision", lambda s: s["controls"][1].update(left=20)),
            ("clipped control", lambda s: s["controls"][0].update(left=-5)),
            ("exceeds viewport", lambda s: s["header"].update(right=350)),
            ("panel overlaps", lambda s: s["main"].update(top=100)),
            ("exceeds workspace", lambda s: s["main"].update(left=-5)),
            ("main view must remain", lambda s: s["main"].update(bottom=120)),
            ("missing settings", lambda s: s["controls"].clear()),
            ("span the workspace bottom", lambda s: s["dock"].update(bottom=700)),
            ("span the dock bottom", lambda s: s["toggle"].update(right=250)),
            ("share width", lambda s: s["branch"].update(right=250)),
            ("reveal above", lambda s: s["branch"].update(bottom=700)),
            ("height must match", lambda s: s["branch"].update(top=700)),
            ("must be inert", lambda s: s.update(inert=False)),
            ("remain reachable", lambda s: s.update(toggleReachable=False)),
            ("meet without overlap", lambda s: s["main"].update(bottom=800)),
            ("fill the remaining", lambda s: s["main"].update(right=250)),
            ("shared branch selector", lambda s: s.update(sameSelector=False)),
            ("exactly one main view", lambda s: s.update(visibleModes=["map", "tree"])),
        ]
        for message, mutate in cases:
            with self.subTest(message=message):
                snapshot = deepcopy(self.snapshot)
                mutate(snapshot)
                self.assertTrue(any(message in failure for failure in layout_failures(snapshot, 320)))

    def test_branch_expands_upward_with_toggle_anchored(self) -> None:
        self.snapshot["dock"]["top"] = 482
        self.snapshot["branch"]["top"] = 483
        self.snapshot["main"]["bottom"] = 482
        self.snapshot.update(expanded=True, inert=False)
        self.assertEqual(layout_failures(self.snapshot, 320), [])
        self.snapshot["dock"]["top"] = 600
        self.assertTrue(any("half the workspace height" in failure for failure in layout_failures(self.snapshot, 320)))

    def test_wide_branch_expands_leftward_with_toggle_anchored(self) -> None:
        self.snapshot.update(
            viewport=rectangle("viewport", 0, 120, 1000, 844),
            header=rectangle("header", 0, 0, 1000, 120),
            main=rectangle("main", 0, 120, 960, 844),
            dock=rectangle("dock", 960, 120, 1000, 844),
            toggle=rectangle("toggle", 960, 120, 1000, 844),
            branch=rectangle("branch", 960, 120, 960, 844),
        )
        self.assertEqual(layout_failures(self.snapshot, 1000), [])
        self.snapshot["dock"]["left"] = 650
        self.snapshot["branch"]["left"] = 650
        self.snapshot["main"]["right"] = 650
        self.snapshot.update(expanded=True, inert=False)
        self.assertEqual(layout_failures(self.snapshot, 1000), [])
        self.snapshot["dock"]["left"] = 500
        self.assertTrue(any("30–40%" in failure for failure in layout_failures(self.snapshot, 1000)))

    def test_mode_switch_preserves_layout_selection_and_visibility(self) -> None:
        switched = deepcopy(self.snapshot)
        switched["visibleModes"] = ["tree"]
        self.assertEqual(mode_switch_failures(self.snapshot, switched), [])
        switched["dock"]["top"] -= 10
        switched["selection"] = ["another-branch"]
        switched["expanded"] = True
        self.assertEqual(
            mode_switch_failures(self.snapshot, switched),
            [
                "switching modes moved dock",
                "switching modes changed the selected branch",
                "switching modes changed branch visibility",
            ],
        )

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
