"""Audit generated Map and Semantic Search data against metadata IDs."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from knowledge_base.scripts.audit_metadata.generated_data.map_data_helpers import (
    _canonical_metadata_ids,
)
from knowledge_base.scripts.audit_metadata.generated_data.map_generated_audit import audit_generated_map_data
from knowledge_base.scripts.audit_metadata.generated_data.semantic_search_audit import audit_semantic_search_data
from knowledge_base.scripts.audit_metadata.support.model import Issue


def audit_map_data_paths(
    targets: list[Path],
    *,
    kb_root: Path,
    report_stale: bool,
    metadata_by_path: dict[Path, dict[str, Any]] | None = None,
) -> list[tuple[Path, list[Issue]]]:
    expected_by_id, setup_issues = _canonical_metadata_ids(targets, kb_root, metadata_by_path=metadata_by_path)
    expected_ids = set(expected_by_id)
    grouped: dict[Path, list[Issue]] = {}
    for issue in setup_issues:
        grouped.setdefault(issue.path, []).append(issue)

    audit_generated_map_data(
        grouped,
        kb_root=kb_root,
        expected_ids=expected_ids,
        report_stale=report_stale,
    )
    audit_semantic_search_data(
        grouped,
        kb_root=kb_root,
        expected_ids=expected_ids,
        report_stale=report_stale,
    )

    return [(path, issues) for path, issues in grouped.items() if issues]
