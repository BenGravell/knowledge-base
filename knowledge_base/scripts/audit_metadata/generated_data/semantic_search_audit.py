"""Audit generated Semantic Search data sidecars."""

from __future__ import annotations

from pathlib import Path

from knowledge_base.publishing.generated_assets import (
    SEMANTIC_SEARCH_INDEX,
    SEMANTIC_SEARCH_SETTINGS,
    semantic_paper_ids,
    semantic_settings_errors,
    semantic_vector_sidecar,
    validate_sidecar_file,
)
from knowledge_base.scripts.audit_metadata.generated_data.map_data_helpers import (
    _audit_id_set,
    _duplicate_values,
    _format_id_examples,
    _load_json_file,
)
from knowledge_base.scripts.audit_metadata.support.checks import CHECK_PATH
from knowledge_base.scripts.audit_metadata.support.model import Issue


def audit_semantic_search_data(
    grouped: dict[Path, list[Issue]],
    *,
    kb_root: Path,
    expected_ids: set[str],
    report_stale: bool,
) -> None:
    semantic_index_path = kb_root / "components" / "semantic_search" / SEMANTIC_SEARCH_INDEX.name
    semantic_index, error = _load_json_file(semantic_index_path)
    semantic_ids: list[str] = []
    if error:
        grouped.setdefault(semantic_index_path, []).append(Issue(semantic_index_path, CHECK_PATH, error))
    elif isinstance(semantic_index, dict):
        semantic_ids = _audit_semantic_papers(
            grouped,
            semantic_index_path,
            semantic_index,
            expected_ids,
            report_stale,
        )
        _audit_semantic_metadata(grouped, semantic_index_path, semantic_index, semantic_ids)
        _audit_semantic_settings(grouped, semantic_index_path, semantic_index)
    else:
        grouped.setdefault(semantic_index_path, []).append(
            Issue(semantic_index_path, CHECK_PATH, "semantic-search-index.json root is not an object")
        )


def _audit_semantic_papers(
    grouped: dict[Path, list[Issue]],
    semantic_index_path: Path,
    semantic_index: dict[str, object],
    expected_ids: set[str],
    report_stale: bool,
) -> list[str]:
    try:
        semantic_ids, bad_papers = semantic_paper_ids(semantic_index)
    except ValueError as exc:
        grouped.setdefault(semantic_index_path, []).append(Issue(semantic_index_path, CHECK_PATH, str(exc)))
        return []

    if bad_papers:
        grouped.setdefault(semantic_index_path, []).append(
            Issue(
                semantic_index_path,
                CHECK_PATH,
                f"semantic-search-index.json has {bad_papers} paper(s) without id",
            )
        )

    duplicate_semantic_ids = _duplicate_values(semantic_ids)
    if duplicate_semantic_ids:
        grouped.setdefault(semantic_index_path, []).append(
            Issue(
                semantic_index_path,
                CHECK_PATH,
                f"semantic-search-index.json has duplicate paper ID(s): {_format_id_examples(duplicate_semantic_ids)}",
            )
        )

    grouped.setdefault(semantic_index_path, []).extend(
        _audit_id_set(
            path=semantic_index_path,
            label="semantic-search-index.json papers",
            actual_ids=set(semantic_ids),
            expected_ids=expected_ids,
            report_stale=report_stale,
            suggestion="Regenerate Semantic Search data.",
        )
    )
    return semantic_ids


def _audit_semantic_metadata(
    grouped: dict[Path, list[Issue]],
    semantic_index_path: Path,
    semantic_index: dict[str, object],
    semantic_ids: list[str],
) -> None:
    count = semantic_index.get("count")
    dimension = semantic_index.get("dimension")
    if not isinstance(count, int) or count < 0:
        grouped.setdefault(semantic_index_path, []).append(
            Issue(semantic_index_path, CHECK_PATH, "semantic-search-index.json count is not a non-negative integer")
        )
    elif semantic_ids and count != len(semantic_ids):
        grouped.setdefault(semantic_index_path, []).append(
            Issue(
                semantic_index_path,
                CHECK_PATH,
                f"semantic-search-index.json count is {count}; expected {len(semantic_ids)}",
                "Regenerate Semantic Search data.",
            )
        )
    if not isinstance(dimension, int) or dimension < 0:
        grouped.setdefault(semantic_index_path, []).append(
            Issue(semantic_index_path, CHECK_PATH, "semantic-search-index.json dimension is not a non-negative integer")
        )

    try:
        vector = semantic_vector_sidecar(semantic_index, asset_dir=semantic_index_path.parent)
    except ValueError as exc:
        grouped.setdefault(semantic_index_path, []).append(
            Issue(semantic_index_path, CHECK_PATH, str(exc), "Regenerate Semantic Search data.")
        )
    else:
        if error := validate_sidecar_file(vector):
            grouped.setdefault(vector.path, []).append(
                Issue(vector.path, CHECK_PATH, error, "Regenerate Semantic Search data.")
            )


def _audit_semantic_settings(
    grouped: dict[Path, list[Issue]],
    semantic_index_path: Path,
    semantic_index: dict[str, object],
) -> None:
    settings_path = semantic_index_path.with_name(SEMANTIC_SEARCH_SETTINGS.name)
    settings, settings_error = _load_json_file(settings_path)
    if settings_error:
        grouped.setdefault(settings_path, []).append(Issue(settings_path, CHECK_PATH, settings_error))
    elif isinstance(settings, dict):
        for error in semantic_settings_errors(semantic_index, settings):
            grouped.setdefault(settings_path, []).append(
                Issue(settings_path, CHECK_PATH, error, "Regenerate Semantic Search data.")
            )
    else:
        grouped.setdefault(settings_path, []).append(
            Issue(settings_path, CHECK_PATH, "semantic-search-settings.json root is not an object")
        )
