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
