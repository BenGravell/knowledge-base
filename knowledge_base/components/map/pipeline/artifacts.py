"""Browser Map generated artifacts.

The generated Map data file assigns the browser global consumed by
``components/map/browser/app.js``. A compact int16 sidecar stores semantic
similarities, while metadata records the model, Tree ordering, aggregate
layouts, and Tree proximity scale needed by the Browser Map Model.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

import numpy as np

from knowledge_base.components.map.pipeline.io import write_bytes_atomic, write_text_atomic
from knowledge_base.components.map.pipeline.layouts import aggregate_force_params, build_aggregate_layouts
from knowledge_base.components.map.pipeline.settings import MAP_DATA_FORMAT_VERSION, SIMILARITY_EXPORT_SCALE
from knowledge_base.components.map.pipeline.similarity import (
    cosine_similarity_matrix,
    quantile_unitize_similarity_matrix,
    tree_proximity_metadata,
)
from knowledge_base.embedding_workbench import save_embedding_cache
from knowledge_base.generated_assets import MAP_DATA


def map_data_cache_key(
    papers: list[dict[str, Any]],
    layout_coords: np.ndarray,
    nav_order: dict[str, Any],
    model_name: str,
) -> str:
    """Stable key for generated browser Map artifacts."""
    node_fields = (
        "id",
        "title",
        "label",
        "authors",
        "year",
        "item_type",
        "super_category",
        "category",
        "sub_category",
        "nav_path",
        "tags",
        "summary",
        "abstract",
        "link",
        "hash",
    )
    payload = [{field: paper.get(field) for field in node_fields} for paper in papers]
    h = hashlib.sha256()
    h.update(str(MAP_DATA_FORMAT_VERSION).encode("ascii"))
    h.update(model_name.encode("utf-8"))
    h.update(json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))
    h.update(json.dumps(nav_order, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))
    h.update(np.rint(np.asarray(layout_coords, dtype=np.float64) * 10).astype("<i4").tobytes())
    h.update(str(SIMILARITY_EXPORT_SCALE).encode("ascii"))
    return h.hexdigest()[:24]


def build_map_nodes(papers: list[dict[str, Any]], layout_coords: np.ndarray) -> list[dict[str, Any]]:
    return [
        {
            "data": {
                "id": paper["id"],
                "label": paper["label"],
                "title": paper["title"],
                "authors": paper["authors"],
                "year": paper["year"],
                "item_type": paper["item_type"],
                "super_category": paper["super_category"],
                "category": paper["category"],
                "sub_category": paper["sub_category"],
                "nav_path": paper["nav_path"],
                "tags": paper["tags"],
                "summary": paper["summary"],
                "abstract": paper["abstract"],
                "link": paper["link"],
            },
            "position": {
                "x": round(float(layout_coords[index, 0]), 1),
                "y": round(float(layout_coords[index, 1]), 1),
            },
        }
        for index, paper in enumerate(papers)
    ]


def similarity_rows_for_embeddings(embeddings: np.ndarray) -> tuple[np.ndarray, dict[str, object]]:
    raw_sim = cosine_similarity_matrix(embeddings)
    sim, similarity_transform = quantile_unitize_similarity_matrix(raw_sim)
    rows = np.clip(
        np.rint(sim * SIMILARITY_EXPORT_SCALE),
        0,
        SIMILARITY_EXPORT_SCALE,
    ).astype(np.int16)
    return rows, similarity_transform


def build_graph_data(
    *,
    papers: list[dict[str, Any]],
    nodes: list[dict[str, Any]],
    similarity_rows: np.ndarray,
    similarity_output: Path,
    similarity_transform: dict[str, object],
    tree_proximity: dict[str, object],
    nav_order: dict[str, Any],
    aggregate_layouts: dict[str, dict[str, list[float]]],
    model_name: str,
) -> dict[str, Any]:
    return {
        "nodes": nodes,
        "similarity": {
            "scale": SIMILARITY_EXPORT_SCALE,
            "ids": [paper["id"] for paper in papers],
            "file": similarity_output.name,
            "dtype": "int16",
            "shape": [int(similarity_rows.shape[0]), int(similarity_rows.shape[1])],
            "byteOrder": "little",
        },
        "meta": {
            "model": model_name,
            "similarityScale": SIMILARITY_EXPORT_SCALE,
            "similarityTransform": similarity_transform,
            "total_papers": len(papers),
            "itemTypeOrder": sorted({paper["item_type"] for paper in papers}),
            "superCategoryOrder": nav_order["superCategories"],
            "categoryOrder": nav_order["categories"],
            "categorySuperCategory": nav_order["categorySuperCategory"],
            "subCategoryOrder": nav_order["subCategoryOrder"],
            "navPathOrder": nav_order["navPathOrder"],
            "maxBranchDepth": nav_order["maxBranchDepth"],
            "aggregateLayouts": aggregate_layouts,
            "treeProximity": tree_proximity,
        },
    }


def write_browser_artifacts(
    *,
    cache: dict[str, Any],
    cache_path: Path,
    papers: list[dict[str, Any]],
    layout_coords: np.ndarray,
    embeddings: np.ndarray,
    nav_order: dict[str, Any],
    model_name: str,
    output: Path,
    similarity_output: Path,
    force_params: dict[str, Any],
    force: bool,
) -> None:
    artifact_key = map_data_cache_key(papers, layout_coords, nav_order, model_name)
    artifact_entry_raw = cache.get("mapData")
    artifact_entry: dict[str, Any] = artifact_entry_raw if isinstance(artifact_entry_raw, dict) else dict[str, Any]()
    if not force and artifact_entry.get("key") == artifact_key and output.exists() and similarity_output.exists():
        print("    Map browser artifacts loaded from cache (inputs unchanged)")
        print(f"    Output: {output}")
        return

    similarity_rows, similarity_transform = similarity_rows_for_embeddings(embeddings)
    tree_proximity = tree_proximity_metadata(
        papers,
        similarity_rows,
        SIMILARITY_EXPORT_SCALE,
    )
    similarity_output.parent.mkdir(parents=True, exist_ok=True)
    write_bytes_atomic(similarity_output, similarity_rows.astype("<i2", copy=False).tobytes(order="C"))

    nodes = build_map_nodes(papers, layout_coords)
    print("    Precomputing aggregate LOD layouts…")
    node_coords = np.array(
        [[node["position"]["x"], node["position"]["y"]] for node in nodes],
        dtype=np.float64,
    )
    aggregate_layouts = build_aggregate_layouts(
        papers,
        node_coords,
        embeddings,
        nav_order,
        aggregate_force_params(force_params),
        verbose=True,
    )

    graph_data = build_graph_data(
        papers=papers,
        nodes=nodes,
        similarity_rows=similarity_rows,
        similarity_output=similarity_output,
        similarity_transform=similarity_transform,
        tree_proximity=tree_proximity,
        nav_order=nav_order,
        aggregate_layouts=aggregate_layouts,
        model_name=model_name,
    )

    output.parent.mkdir(parents=True, exist_ok=True)
    write_text_atomic(output, MAP_DATA.js_assignment(graph_data, separators=(",", ":")))
    cache["mapData"] = {
        "key": artifact_key,
        "format": MAP_DATA_FORMAT_VERSION,
        "output": output.name,
        "similarity": similarity_output.name,
    }
    save_embedding_cache(cache_path, cache)

    print(f"    Nodes : {len(nodes)}")
    print(
        f"    Similarity matrix: exported ({similarity_transform['method']} {similarity_transform['source']} -> [0, 1])"
    )
    print(f"    Similarity sidecar: {similarity_output} ({similarity_output.stat().st_size // 1024} KB)")
    print(f"    Tree proximity scale: exported (KL={tree_proximity['klDivergence']})")
    print(f"    Output: {output}")
