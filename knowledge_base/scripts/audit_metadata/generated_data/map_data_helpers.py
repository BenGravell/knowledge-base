"""Shared helpers for generated Map/Search audits."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from knowledge_base.publishing.generated_assets import (
    MAP_DATA,
    duplicate_values,
    format_id_examples,
    id_set_difference_messages,
)
from knowledge_base.scripts.audit_metadata.support.checks import CHECK_PATH
from knowledge_base.scripts.audit_metadata.support.model import Issue
from knowledge_base.scripts.audit_metadata.support.yaml_support import _yaml_safe_load
from knowledge_base.utils.paper_ids import paper_id_from_metadata


def _format_id_examples(ids: set[str] | list[str], limit: int = 8) -> str:
    return format_id_examples(ids, limit=limit)


def _load_json_file(path: Path) -> tuple[object | None, str | None]:
    try:
        return json.loads(path.read_text(encoding="utf-8")), None
    except FileNotFoundError:
        return None, "Missing file"
    except json.JSONDecodeError as exc:
        return None, f"JSON parse error: {exc}"
    except OSError as exc:
        return None, f"Could not read file: {exc}"


def _load_map_data_js(path: Path) -> tuple[dict[str, Any] | None, str | None]:
    try:
        raw = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None, "Missing file"
    except OSError as exc:
        return None, f"Could not read file: {exc}"

    try:
        data = MAP_DATA.loads_js_assignment(raw)
    except json.JSONDecodeError as exc:
        return None, f"mapData JSON parse error: {exc}"
    except ValueError:
        return None, "Expected JavaScript assignment like 'const mapData={...};'"
    return data, None


def _canonical_metadata_ids(
    targets: list[Path],
    kb_root: Path,
    *,
    metadata_by_path: dict[Path, dict[str, Any]] | None = None,
) -> tuple[dict[str, Path], list[Issue]]:
    metadata_root = kb_root / "docs" / "papers"
    expected: dict[str, Path] = {}
    issues: list[Issue] = []
    collisions: dict[str, list[Path]] = {}

    for path in targets:
        if metadata_by_path is not None and path in metadata_by_path:
            data = metadata_by_path[path]
        else:
            try:
                data = _yaml_safe_load(path.read_text(encoding="utf-8")) or {}
            except Exception:
                continue
        if not isinstance(data, dict):
            continue

        paper_id = paper_id_from_metadata(path, data, metadata_root)
        if paper_id in expected:
            collisions.setdefault(paper_id, [expected[paper_id]]).append(path)
        else:
            expected[paper_id] = path

    for paper_id, paths in sorted(collisions.items()):
        path_list = ", ".join(str(path) for path in paths)
        issues.append(
            Issue(
                kb_root / "components" / "map" / "generated" / MAP_DATA.name,
                CHECK_PATH,
                f"Canonical metadata ID {paper_id!r} is produced by multiple metadata files: {path_list}",
            )
        )

    return expected, issues


def _audit_id_set(
    *,
    path: Path,
    label: str,
    actual_ids: set[str],
    expected_ids: set[str],
    report_stale: bool,
    suggestion: str = "Regenerate map data, or run --fix after a metadata path change.",
) -> list[Issue]:
    return [
        Issue(path, CHECK_PATH, message, suggestion)
        for message in id_set_difference_messages(label, actual_ids, expected_ids, report_stale=report_stale)
    ]


def _duplicate_values(values: list[str]) -> set[str]:
    return duplicate_values(values)
