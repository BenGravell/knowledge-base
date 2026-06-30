"""Compatibility imports for unplaced-paper data loading."""

from knowledge_base.scripts.tree_report_data import (
    DOCS_DIR,
    EMBEDDING_CACHE,
    METADATA_ROOT,
    SITE_CONFIG,
    TREE_YML,
    as_list,
    collect_paper_paths,
    fast_paper_id_from_file,
    paper_id_from_file,
    relative_to_kb,
)
from knowledge_base.scripts.tree_report_data import (
    load_report_paper as load_paper,
)
from knowledge_base.scripts.tree_report_data import (
    load_report_papers as collect_papers,
)

__all__ = [
    "DOCS_DIR",
    "EMBEDDING_CACHE",
    "METADATA_ROOT",
    "SITE_CONFIG",
    "TREE_YML",
    "as_list",
    "collect_paper_paths",
    "collect_papers",
    "fast_paper_id_from_file",
    "load_paper",
    "paper_id_from_file",
    "relative_to_kb",
]
