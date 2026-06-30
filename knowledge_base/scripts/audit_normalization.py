"""Compatibility wrapper for the normalization audit CLI."""

from __future__ import annotations

from knowledge_base.scripts.normalization_audit.cli import main
from knowledge_base.scripts.normalization_audit.fixes import issue_rule_or_legacy, issue_tag_index
from knowledge_base.scripts.normalization_audit.model import RULE_TAG_VALUE, Issue

__all__ = [
    "RULE_TAG_VALUE",
    "Issue",
    "issue_rule_or_legacy",
    "issue_tag_index",
]

if __name__ == "__main__":
    raise SystemExit(main())
