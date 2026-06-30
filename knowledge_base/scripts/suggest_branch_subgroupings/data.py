"""Input loading for branch subgroup suggestions."""

from pathlib import Path

import numpy as np
import yaml

from knowledge_base.components.tree.model import TreeBranch as Branch
from knowledge_base.components.tree.model import load_tree_model
from knowledge_base.embedding_workbench import load_embedding_table
from knowledge_base.scripts.suggest_branch_subgroupings.common import EMBEDDING_CACHE, METADATA_ROOT, as_list
from knowledge_base.scripts.suggest_branch_subgroupings.model import Paper
from knowledge_base.utils.paper_ids import paper_id_from_metadata


def load_papers(metadata_root: Path = METADATA_ROOT) -> dict[str, Paper]:
    papers: dict[str, Paper] = {}
    for metadata_file in sorted(metadata_root.rglob("metadata.yml")):
        with metadata_file.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        if not isinstance(data, dict):
            continue
        paper_id = paper_id_from_metadata(metadata_file, data, metadata_root)
        tags = tuple(str(tag).strip() for tag in as_list(data.get("tags")) if str(tag).strip())
        papers[paper_id] = Paper(
            id=paper_id,
            title=" ".join(str(data.get("title") or paper_id).split()),
            algorithm=" ".join(str(data.get("algorithm") or "").split()),
            tags=tags,
            metadata_path=metadata_file,
        )
    return papers


def load_embeddings(cache_path: Path = EMBEDDING_CACHE) -> dict[str, np.ndarray]:
    if not cache_path.exists():
        raise FileNotFoundError(f"Embedding cache not found: {cache_path}")

    return {
        paper_id: vector
        for paper_id, vector in load_embedding_table(cache_path, mmap_mode="r").by_id().items()
        if vector.ndim == 1 and np.linalg.norm(vector) > 0
    }


def collect_branches(tree_path: Path, *, include_root: bool) -> list[Branch]:
    model = load_tree_model(
        tree_path,
        base_dir=tree_path.parent,
        metadata_root=METADATA_ROOT,
    )
    return [model.root, *model.branches] if include_root else list(model.branches)


__all__ = ["collect_branches", "load_embeddings", "load_papers"]
