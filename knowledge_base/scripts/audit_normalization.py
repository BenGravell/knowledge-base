"""Compatibility wrapper for the normalization audit CLI."""

# ruff: noqa: PLC0414

from __future__ import annotations

from knowledge_base.scripts.normalization_audit.cli import main
from knowledge_base.scripts.normalization_audit.fixes import issue_rule_or_legacy as issue_rule_or_legacy
from knowledge_base.scripts.normalization_audit.fixes import issue_tag_index as issue_tag_index
from knowledge_base.scripts.normalization_audit.model import RULE_TAG_VALUE as RULE_TAG_VALUE
from knowledge_base.scripts.normalization_audit.model import Issue as Issue

__all__ = [
    "RULE_TAG_VALUE",
    "Issue",
    "issue_rule_or_legacy",
    "issue_tag_index",
]

if __name__ == "__main__":
    raise SystemExit(main())
