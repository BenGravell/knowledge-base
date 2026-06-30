"""Paper metadata loading helpers."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from knowledge_base.config import KB_DIR
from knowledge_base.progress import emit_progress
from knowledge_base.scripts.list_unplaced_papers.model import Paper
from knowledge_base.utils.paper_ids import paper_id_from_metadata

DOCS_DIR = KB_DIR / "docs"
METADATA_ROOT = DOCS_DIR / "papers"
SITE_CONFIG = KB_DIR / "zensical.yml"
EMBEDDING_CACHE = KB_DIR / "components" / "map" / "cache" / "embedding_cache.json"
TREE_YML = KB_DIR / "tree.yml"


def paper_id_from_file(metadata_file: Path, data: dict[str, Any]) -> str:
    """Return the generated paper ID used by generated site pages."""
    return paper_id_from_metadata(metadata_file, data, METADATA_ROOT)


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    return []


def fast_paper_id_from_file(metadata_file: Path) -> str:
    with metadata_file.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.startswith("id:"):
                continue
            value = yaml.safe_load(line.partition(":")[2].strip())
            if value:
                return paper_id_from_file(metadata_file, {"id": value})
    return paper_id_from_file(metadata_file, {})


def collect_paper_paths(metadata_root: Path) -> dict[str, Path]:
    paths: dict[str, Path] = {}
    metadata_files = sorted(metadata_root.rglob("metadata.yml"))
    for index, metadata_file in enumerate(metadata_files, start=1):
        paths[fast_paper_id_from_file(metadata_file)] = metadata_file
        emit_progress(index, len(metadata_files), "Collect unplaced-paper IDs", every=100)
    return paths


def load_paper(metadata_file: Path, paper_id: str | None = None) -> Paper | None:
    with metadata_file.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        return None

    paper_id = paper_id or paper_id_from_file(metadata_file, data)
    title = " ".join(str(data.get("title") or paper_id).split())
    algorithm = " ".join(str(data.get("algorithm") or "").split())
    abstract = str(data.get("abstract") or "").strip()
    tags = tuple(str(tag) for tag in as_list(data.get("tags")))
    return Paper(
        id=paper_id,
        title=title,
        algorithm=algorithm,
        metadata_path=metadata_file,
        generated_path=f"papers/{paper_id}.md",
        abstract=abstract,
        tags=tags,
    )


def collect_papers(metadata_root: Path) -> dict[str, Paper]:
    papers: dict[str, Paper] = {}
    metadata_files = sorted(metadata_root.rglob("metadata.yml"))
    for index, metadata_file in enumerate(metadata_files, start=1):
        paper = load_paper(metadata_file)
        if paper is not None:
            papers[paper.id] = paper
        emit_progress(index, len(metadata_files), "Collect unplaced-paper metadata", every=100)
    return papers


def relative_to_kb(path: Path) -> str:
    try:
        return str(path.relative_to(KB_DIR))
    except ValueError:
        return str(path)
