from __future__ import annotations

import unittest
from pathlib import Path

from knowledge_base.scripts.normalization_audit.fixes import issue_rule_or_legacy, issue_tag_index
from knowledge_base.scripts.normalization_audit.model import RULE_TAG_VALUE, Issue


class NormalizationAuditRuleTests(unittest.TestCase):
    def test_normalization_tag_routing_uses_rule_code_and_index(self) -> None:
        issue = Issue(
            Path("metadata.yml"),
            "tags",
            "human wording may change freely",
            "Canonical Tag",
            rule=RULE_TAG_VALUE,
            index=4,
        )

        self.assertTrue(
            issue_rule_or_legacy(
                issue,
                RULE_TAG_VALUE,
                False,
            )
        )
        self.assertEqual(issue_tag_index(issue), 4)


if __name__ == "__main__":
    unittest.main()
