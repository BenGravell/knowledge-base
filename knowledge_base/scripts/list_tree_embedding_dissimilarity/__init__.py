"""Import-compatible surface for Tree embedding dissimilarity."""

# ruff: noqa: F401

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
