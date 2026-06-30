"""Import-compatible surface for Tree embedding dissimilarity."""

from knowledge_base.scripts.list_tree_embedding_dissimilarity.analysis import (
    branch_depth,
    category_ids,
    cosine,
    find_branch_outliers,
    find_outliers,
)
from knowledge_base.scripts.list_tree_embedding_dissimilarity.cli import main
from knowledge_base.scripts.list_tree_embedding_dissimilarity.data import (
    EMBEDDING_CACHE,
    METADATA_ROOT,
    collect_branches,
    display_path,
    format_path,
    load_embeddings,
    load_metadata,
    load_papers,
    relative_to_kb,
)
from knowledge_base.scripts.list_tree_embedding_dissimilarity.model import Finding, Outlier, Paper, Scope
from knowledge_base.scripts.list_tree_embedding_dissimilarity.output import print_json, print_markdown

__all__ = [
    "EMBEDDING_CACHE",
    "METADATA_ROOT",
    "Finding",
    "Outlier",
    "Paper",
    "Scope",
    "branch_depth",
    "category_ids",
    "collect_branches",
    "cosine",
    "display_path",
    "find_branch_outliers",
    "find_outliers",
    "format_path",
    "load_embeddings",
    "load_metadata",
    "load_papers",
    "main",
    "print_json",
    "print_markdown",
    "relative_to_kb",
]
