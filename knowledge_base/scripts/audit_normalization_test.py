from __future__ import annotations

import unittest
from pathlib import Path

from knowledge_base.scripts import audit_normalization


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
