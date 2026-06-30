"""Data loading helpers for Tree embedding dissimilarity."""

from __future__ import annotations

import math
from pathlib import Path
from typing import Any

import yaml

from knowledge_base.components.tree.model import TreeBranch as Branch
from knowledge_base.components.tree.model import load_tree_model
from knowledge_base.components.tree.nav_source import TREE_YML
from knowledge_base.config import KB_DIR
from knowledge_base.scripts.list_tree_embedding_dissimilarity.model import Paper
from knowledge_base.utils.paper_ids import paper_id_from_metadata

METADATA_ROOT = KB_DIR / "docs" / "papers"
EMBEDDING_CACHE = KB_DIR / "components" / "map" / "cache" / "embedding_cache.json"


def relative_to_kb(path: Path) -> str:
    try:
        return str(path.relative_to(KB_DIR))
    except ValueError:
        return str(path)


def display_path(path: tuple[str, ...]) -> tuple[str, ...]:
    return path if path == ("Tree",) else ("Tree", *path)


def format_path(path: tuple[str, ...]) -> str:
    return " > ".join(display_path(path))


def load_metadata(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data if isinstance(data, dict) else {}


def load_papers() -> dict[str, Paper]:
    by_id: dict[str, Paper] = {}
    for metadata_path in sorted(METADATA_ROOT.rglob("metadata.yml")):
        data = load_metadata(metadata_path)
        paper_id = paper_id_from_metadata(metadata_path, data, METADATA_ROOT)
        by_id[paper_id] = Paper(
            id=paper_id,
            title=" ".join(str(data.get("title") or paper_id).split()),
            metadata_path=metadata_path,
        )
    return by_id


def collect_branches(tree_path: Path = TREE_YML) -> list[Branch]:
    return list(load_tree_model(tree_path, base_dir=KB_DIR, metadata_root=METADATA_ROOT).branches)


def load_embeddings(path: Path = EMBEDDING_CACHE) -> dict[str, tuple[float, ...]]:
    if not path.exists():
        return {}
    from knowledge_base.embedding_workbench import load_embedding_table

    embeddings: dict[str, tuple[float, ...]] = {}
    for paper_id, vector in load_embedding_table(path, mmap_mode="r").by_id().items():
        values = tuple(float(value) for value in vector)
        norm = math.sqrt(sum(value * value for value in values))
        if norm:
            embeddings[str(paper_id)] = tuple(value / norm for value in values)
    return embeddings
