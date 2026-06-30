"""Audit generated Map data and embedding cache sidecars."""

from __future__ import annotations

from pathlib import Path

from knowledge_base.generated_assets import MAP_DATA
from knowledge_base.scripts.audit_metadata.generated_data.map_data_helpers import (
    _audit_id_set,
    _duplicate_values,
    _format_id_examples,
    _load_json_file,
    _load_map_data_js,
)
from knowledge_base.scripts.audit_metadata.support.checks import CHECK_PATH
from knowledge_base.scripts.audit_metadata.support.model import Issue


def audit_generated_map_data(
    grouped: dict[Path, list[Issue]],
    *,
    kb_root: Path,
    expected_ids: set[str],
    report_stale: bool,
) -> None:
    map_data_path = kb_root / "components" / "map" / "generated" / MAP_DATA.name
    map_data, error = _load_map_data_js(map_data_path)
    if error:
        grouped.setdefault(map_data_path, []).append(Issue(map_data_path, CHECK_PATH, error))
        return
    if map_data is None:
        return

    node_ids = _audit_map_nodes(grouped, map_data_path, map_data, expected_ids, report_stale)
    _audit_map_similarity(grouped, map_data_path, map_data, node_ids, expected_ids, report_stale)

    meta = map_data.get("meta")
    if report_stale and isinstance(meta, dict) and meta.get("total_papers") != len(expected_ids):
        grouped.setdefault(map_data_path, []).append(
            Issue(
                map_data_path,
                CHECK_PATH,
                f"mapData.meta.total_papers is {meta.get('total_papers')!r}; expected {len(expected_ids)}",
                "Regenerate map data.",
            )
        )

    _audit_embedding_cache(grouped, kb_root, expected_ids, report_stale)


def _audit_map_nodes(
    grouped: dict[Path, list[Issue]],
    map_data_path: Path,
    map_data: dict[str, object],
    expected_ids: set[str],
    report_stale: bool,
) -> list[str]:
    nodes = map_data.get("nodes")
    if not isinstance(nodes, list):
        grouped.setdefault(map_data_path, []).append(Issue(map_data_path, CHECK_PATH, "mapData.nodes is not a list"))
        node_ids: list[str] = []
    else:
        node_ids = []
        bad_nodes = 0
        for node in nodes:
            data = node.get("data") if isinstance(node, dict) else None
            node_id = data.get("id") if isinstance(data, dict) else None
            if isinstance(node_id, str) and node_id:
                node_ids.append(node_id)
            else:
                bad_nodes += 1
        if bad_nodes:
            grouped.setdefault(map_data_path, []).append(
                Issue(map_data_path, CHECK_PATH, f"mapData.nodes has {bad_nodes} node(s) without data.id")
            )

    duplicate_node_ids = _duplicate_values(node_ids)
    if duplicate_node_ids:
        grouped.setdefault(map_data_path, []).append(
            Issue(
                map_data_path,
                CHECK_PATH,
                f"mapData.nodes has duplicate paper ID(s): {_format_id_examples(duplicate_node_ids)}",
            )
        )

    grouped.setdefault(map_data_path, []).extend(
        _audit_id_set(
            path=map_data_path,
            label="mapData.nodes",
            actual_ids=set(node_ids),
            expected_ids=expected_ids,
            report_stale=report_stale,
        )
    )
    return node_ids


def _audit_map_similarity(
    grouped: dict[Path, list[Issue]],
    map_data_path: Path,
    map_data: dict[str, object],
    node_ids: list[str],
    expected_ids: set[str],
    report_stale: bool,
) -> None:
    similarity = map_data.get("similarity")
    if not isinstance(similarity, dict):
        grouped.setdefault(map_data_path, []).append(
            Issue(map_data_path, CHECK_PATH, "mapData.similarity is not an object")
        )
        return

    similarity_ids_raw = similarity.get("ids")
    if not isinstance(similarity_ids_raw, list) or not all(isinstance(item, str) for item in similarity_ids_raw):
        grouped.setdefault(map_data_path, []).append(
            Issue(map_data_path, CHECK_PATH, "mapData.similarity.ids is not a string list")
        )
        similarity_ids: list[str] = []
    else:
        similarity_ids = similarity_ids_raw
        grouped.setdefault(map_data_path, []).extend(
            _audit_id_set(
                path=map_data_path,
                label="mapData.similarity.ids",
                actual_ids=set(similarity_ids),
                expected_ids=expected_ids,
                report_stale=report_stale,
            )
        )
        if node_ids and similarity_ids != node_ids:
            grouped.setdefault(map_data_path, []).append(
                Issue(
                    map_data_path,
                    CHECK_PATH,
                    "mapData.similarity.ids does not exactly match mapData.nodes order",
                    "Regenerate map data.",
                )
            )

    rows = similarity.get("rows")
    if isinstance(rows, list) and similarity_ids:
        bad_row_count = len(rows) != len(similarity_ids)
        bad_row_width = any(not isinstance(row, list) or len(row) != len(similarity_ids) for row in rows)
        if bad_row_count or bad_row_width:
            grouped.setdefault(map_data_path, []).append(
                Issue(
                    map_data_path,
                    CHECK_PATH,
                    "mapData.similarity.rows shape does not match similarity.ids",
                    "Regenerate map data.",
                )
            )
    elif similarity_ids:
        _audit_similarity_sidecar(grouped, map_data_path, similarity, len(similarity_ids))


def _audit_similarity_sidecar(
    grouped: dict[Path, list[Issue]],
    map_data_path: Path,
    similarity: dict[object, object],
    size: int,
) -> None:
    sidecar = similarity.get("file")
    shape = similarity.get("shape")
    if not isinstance(sidecar, str) or not isinstance(shape, list) or len(shape) != 2:
        grouped.setdefault(map_data_path, []).append(
            Issue(
                map_data_path,
                CHECK_PATH,
                "mapData.similarity has neither rows nor a valid binary sidecar descriptor",
                "Regenerate map data.",
            )
        )
        return

    sidecar_path = map_data_path.with_name(sidecar)
    expected_shape = [size, size]
    expected_bytes = size * size * 2
    if shape != expected_shape:
        grouped.setdefault(map_data_path, []).append(
            Issue(
                map_data_path,
                CHECK_PATH,
                "mapData.similarity sidecar shape does not match similarity.ids",
                "Regenerate map data.",
            )
        )
    elif not sidecar_path.exists():
        grouped.setdefault(map_data_path, []).append(
            Issue(sidecar_path, CHECK_PATH, "mapData.similarity sidecar is missing", "Regenerate map data.")
        )
    elif sidecar_path.stat().st_size != expected_bytes:
        grouped.setdefault(map_data_path, []).append(
            Issue(
                sidecar_path,
                CHECK_PATH,
                f"mapData.similarity sidecar is {sidecar_path.stat().st_size} bytes; expected {expected_bytes}",
                "Regenerate map data.",
            )
        )


def _audit_embedding_cache(
    grouped: dict[Path, list[Issue]],
    kb_root: Path,
    expected_ids: set[str],
    report_stale: bool,
) -> None:
    cache_path = kb_root / "components" / "map" / "cache" / "embedding_cache.json"
    cache, error = _load_json_file(cache_path)
    if error:
        grouped.setdefault(cache_path, []).append(Issue(cache_path, CHECK_PATH, error))
    elif isinstance(cache, dict):
        cached_papers = cache.get("papers")
        if not isinstance(cached_papers, dict):
            grouped.setdefault(cache_path, []).append(
                Issue(cache_path, CHECK_PATH, "embedding_cache.json papers field is not an object")
            )
        else:
            grouped.setdefault(cache_path, []).extend(
                _audit_id_set(
                    path=cache_path,
                    label="embedding_cache.json papers",
                    actual_ids={str(key) for key in cached_papers},
                    expected_ids=expected_ids,
                    report_stale=report_stale,
                )
            )
    else:
        grouped.setdefault(cache_path, []).append(
            Issue(cache_path, CHECK_PATH, "embedding_cache.json root is not an object")
        )
