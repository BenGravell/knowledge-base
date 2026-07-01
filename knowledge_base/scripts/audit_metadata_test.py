from __future__ import annotations

import unittest
from pathlib import Path

from knowledge_base.scripts.audit_metadata.fixes.fix_predicates import _is_fixable_tag_issue
from knowledge_base.scripts.audit_metadata.rules.algorithm_cues import (
    _algorithm_issue_cue,
    _text_introduces_algorithm_label,
)
from knowledge_base.scripts.audit_metadata.rules.tag_text import _tag_issue_index
from knowledge_base.scripts.audit_metadata.rules.text_quality import (
    find_likely_misspelling_issues,
    find_ocr_spacing_issues,
)
from knowledge_base.scripts.audit_metadata.support.model import RULE_TAG_VALUE, Issue


class MetadataAuditRuleTests(unittest.TestCase):
    def test_fix_routing_uses_rule_code_and_index_before_message_text(self) -> None:
        issue = Issue(
            Path("metadata.yml"),
            "tags",
            "human wording may change freely",
            "Canonical Tag",
            rule=RULE_TAG_VALUE,
            index=3,
        )

        self.assertTrue(_is_fixable_tag_issue(issue))
        self.assertEqual(_tag_issue_index(issue), 3)

    def test_legacy_message_routing_still_works_for_ad_hoc_issues(self) -> None:
        issue = Issue(
            Path("metadata.yml"),
            "tags",
            "Tag is not in capital case at tags[2]: 'control'",
            "Control",
        )

        self.assertTrue(_is_fixable_tag_issue(issue))
        self.assertEqual(_tag_issue_index(issue), 2)

    def test_misspelling_detector_uses_word_boundaries(self) -> None:
        issues = find_likely_misspelling_issues(
            Path("metadata.yml"),
            "abstract",
            "The method can acheive stable tracking; preacheive is not a word hit.",
        )

        self.assertEqual(len(issues), 1)
        self.assertIn("'acheive' -> 'achieve'", issues[0].message)

    def test_ocr_split_detector_keeps_allowed_hyphenated_words(self) -> None:
        issues = find_ocr_spacing_issues(
            Path("metadata.yml"),
            "abstract",
            "The algor ithm handles non-convex optimization.",
        )

        self.assertEqual(len(issues), 1)
        self.assertIn("'algor ithm' -> 'algorithm'", issues[0].message)
        self.assertNotIn("non-convex", issues[0].message)

    def test_algorithm_intro_detector_uses_cached_patterns(self) -> None:
        self.assertTrue(
            _text_introduces_algorithm_label(
                "MPPI",
                "MPPI: A New Planner",
                "",
            )
        )

    def test_algorithm_cue_detector_uses_cached_patterns(self) -> None:
        self.assertEqual(
            _algorithm_issue_cue(
                "MPC",
                "Stability of MPC",
                "We study stability of model predictive control in uncertain systems.",
            ),
            ("stability analysis", "MPC stability analysis"),
        )


if __name__ == "__main__":
    unittest.main()
