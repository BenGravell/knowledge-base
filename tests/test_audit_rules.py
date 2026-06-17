from __future__ import annotations

import unittest
from pathlib import Path

from knowledge_base.scripts import audit_metadata, audit_normalization


class MetadataAuditRuleTests(unittest.TestCase):
    def test_fix_routing_uses_rule_code_and_index_before_message_text(self) -> None:
        issue = audit_metadata.Issue(
            Path("metadata.yml"),
            "tags",
            "human wording may change freely",
            "Canonical Tag",
            rule=audit_metadata.RULE_TAG_VALUE,
            index=3,
        )

        self.assertTrue(audit_metadata._is_fixable_tag_issue(issue))
        self.assertEqual(audit_metadata._tag_issue_index(issue), 3)

    def test_legacy_message_routing_still_works_for_ad_hoc_issues(self) -> None:
        issue = audit_metadata.Issue(
            Path("metadata.yml"),
            "tags",
            "Tag is not in capital case at tags[2]: 'control'",
            "Control",
        )

        self.assertTrue(audit_metadata._is_fixable_tag_issue(issue))
        self.assertEqual(audit_metadata._tag_issue_index(issue), 2)

    def test_misspelling_detector_uses_word_boundaries(self) -> None:
        issues = audit_metadata.find_likely_misspelling_issues(
            Path("metadata.yml"),
            "abstract",
            "The method can acheive stable tracking; preacheive is not a word hit.",
        )

        self.assertEqual(len(issues), 1)
        self.assertIn("'acheive' -> 'achieve'", issues[0].message)

    def test_ocr_split_detector_keeps_allowed_hyphenated_words(self) -> None:
        issues = audit_metadata.find_ocr_spacing_issues(
            Path("metadata.yml"),
            "abstract",
            "The algor ithm handles non-convex optimization.",
        )

        self.assertEqual(len(issues), 1)
        self.assertIn("'algor ithm' -> 'algorithm'", issues[0].message)
        self.assertNotIn("non-convex", issues[0].message)

    def test_algorithm_intro_detector_uses_cached_patterns(self) -> None:
        self.assertTrue(
            audit_metadata._text_introduces_algorithm_label(
                "MPPI",
                "MPPI: A New Planner",
                "",
            )
        )

    def test_algorithm_cue_detector_uses_cached_patterns(self) -> None:
        self.assertEqual(
            audit_metadata._algorithm_issue_cue(
                "MPC",
                "Stability of MPC",
                "We study stability of model predictive control in uncertain systems.",
            ),
            ("stability analysis", "MPC stability analysis"),
        )


class NormalizationAuditRuleTests(unittest.TestCase):
    def test_normalization_tag_routing_uses_rule_code_and_index(self) -> None:
        issue = audit_normalization.Issue(
            Path("metadata.yml"),
            "tags",
            "human wording may change freely",
            "Canonical Tag",
            rule=audit_normalization.RULE_TAG_VALUE,
            index=4,
        )

        self.assertTrue(
            audit_normalization.issue_rule_or_legacy(
                issue,
                audit_normalization.RULE_TAG_VALUE,
                False,
            )
        )
        self.assertEqual(audit_normalization.issue_tag_index(issue), 4)


if __name__ == "__main__":
    unittest.main()
