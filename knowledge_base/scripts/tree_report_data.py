"""Shared data access for Tree reporting scripts."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

import numpy as np
import yaml

from knowledge_base.catalog import Catalog, Entry
from knowledge_base.config import KB_DIR
from knowledge_base.embeddings.workbench import load_embedding_table
from knowledge_base.progress import emit_progress
from knowledge_base.tree.model import TreeBranch, TreeLeaf, load_tree_model
from knowledge_base.utils.paper_ids import paper_id_from_metadata

DOCS_DIR = KB_DIR / "docs"
METADATA_ROOT = DOCS_DIR / "papers"
SITE_CONFIG = KB_DIR / "zensical.yml"
TREE_YML = KB_DIR / "tree.yml"
EMBEDDING_CACHE = KB_DIR / "components" / "map" / "cache" / "embedding_cache.json"
CountMode = Literal["all", "branches"]


@dataclass(frozen=True)
class ReportPaper:
    id: str
    title: str
    algorithm: str
    metadata_path: Path
    generated_path: str
    abstract: str
    tags: tuple[str, ...]


def report_paper_from_entry(entry: Entry) -> ReportPaper:
    return ReportPaper(
        id=entry.id,
        title=entry.title,
        algorithm=entry.algorithm,
        metadata_path=entry.metadata_path,
        generated_path=entry.generated_source,
        abstract=entry.abstract,
        tags=entry.tags,
    )


def load_report_papers(
    metadata_root: Path = METADATA_ROOT,
    *,
    progress_label: str | None = None,
) -> dict[str, ReportPaper]:
    entries = Catalog.from_metadata_root(metadata_root).entries
    papers: dict[str, ReportPaper] = {}
    for index, entry in enumerate(entries, start=1):
        papers[entry.id] = report_paper_from_entry(entry)
        if progress_label is not None:
            emit_progress(index, len(entries), progress_label, every=100)
    return papers


def load_metadata(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data if isinstance(data, dict) else {}


def paper_id_from_file(metadata_file: Path, data: dict[str, Any]) -> str:
    return paper_id_from_metadata(metadata_file, data, METADATA_ROOT)


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def load_report_paper(metadata_file: Path, paper_id: str | None = None) -> ReportPaper | None:
    data = load_metadata(metadata_file)
    if not data:
        return None
    entry = Entry.from_metadata(metadata_file, data, metadata_root=METADATA_ROOT)
    if paper_id is None or paper_id == entry.id:
        return report_paper_from_entry(entry)
    return ReportPaper(
        id=paper_id,
        title=entry.title,
        algorithm=entry.algorithm,
        metadata_path=entry.metadata_path,
        generated_path=f"papers/{paper_id}.md",
        abstract=entry.abstract,
        tags=entry.tags,
    )


def collect_paper_paths(metadata_root: Path = METADATA_ROOT) -> dict[str, Path]:
    return {
        paper_id: paper.metadata_path
        for paper_id, paper in load_report_papers(metadata_root, progress_label="Collect paper IDs").items()
    }


def fast_paper_id_from_file(metadata_file: Path) -> str:
    with metadata_file.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.startswith("id:"):
                continue
            value = yaml.safe_load(line.partition(":")[2].strip())
            if value:
                return paper_id_from_file(metadata_file, {"id": value})
    return paper_id_from_file(metadata_file, {})


def relative_to_kb(path: Path) -> str:
    try:
        return str(path.relative_to(KB_DIR))
    except ValueError:
        return str(path)


def display_path(path: tuple[str, ...]) -> tuple[str, ...]:
    return path if path == ("Tree",) else ("Tree", *path)


def tree_yml_path(path: tuple[str, ...]) -> tuple[str, ...]:
    return display_path(path)


def format_path(path: tuple[str, ...]) -> str:
    return " > ".join(display_path(path))


def is_landing_item(label: str, child: Any) -> bool:
    landing_pages = {"tree.md", "tree/index.md"}
    return isinstance(child, str) and (
        child in landing_pages or (label.strip().lower() == "overview" and child in landing_pages)
    )


def collect_branches(tree_path: Path = TREE_YML, *, include_root: bool = False) -> list[TreeBranch]:
    model = load_tree_model(tree_path, base_dir=tree_path.parent, metadata_root=METADATA_ROOT)
    return [model.root, *model.branches] if include_root else list(model.branches)


def collect_nav_locations(model: Any) -> dict[str, list[str]]:
    return {paper_id: list(placement.nav_path) for paper_id, placement in model.placements_by_paper_id.items()}


def collect_tree_leaves(model: Any) -> dict[str, TreeLeaf]:
    leaves: dict[str, TreeLeaf] = {}
    for leaf in model.leaves:
        if leaf.paper_id:
            leaves.setdefault(leaf.paper_id, leaf)
    return leaves


def load_embedding_vectors(
    cache_path: Path = EMBEDDING_CACHE,
    *,
    normalize_rows: bool = False,
    missing_ok: bool = True,
) -> dict[str, np.ndarray]:
    if not cache_path.exists():
        if missing_ok:
            return {}
        raise FileNotFoundError(f"Embedding cache not found: {cache_path}")
    return {
        paper_id: vector
        for paper_id, vector in load_embedding_table(cache_path, mmap_mode="r")
        .by_id(normalize_rows=normalize_rows)
        .items()
        if vector.ndim == 1 and np.linalg.norm(vector) > 0
    }


__all__ = [
    "DOCS_DIR",
    "EMBEDDING_CACHE",
    "METADATA_ROOT",
    "SITE_CONFIG",
    "TREE_YML",
    "CountMode",
    "ReportPaper",
    "as_list",
    "collect_branches",
    "collect_nav_locations",
    "collect_paper_paths",
    "collect_tree_leaves",
    "display_path",
    "fast_paper_id_from_file",
    "format_path",
    "is_landing_item",
    "load_embedding_vectors",
    "load_metadata",
    "load_report_paper",
    "load_report_papers",
    "paper_id_from_file",
    "relative_to_kb",
    "tree_yml_path",
]
