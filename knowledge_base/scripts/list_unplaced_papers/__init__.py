"""Import-compatible surface for unplaced-paper reporting."""

# ruff: noqa: F401

from knowledge_base.scripts.list_unplaced_papers.cli import main
from knowledge_base.scripts.list_unplaced_papers.embeddings import load_embeddings, nearest_placed_neighbors
from knowledge_base.scripts.list_unplaced_papers.model import Paper
from knowledge_base.scripts.list_unplaced_papers.output import (
    print_empty,
    print_json,
    print_markdown,
    print_write_summary,
)
from knowledge_base.scripts.list_unplaced_papers.paths import (
    DOCS_DIR,
    EMBEDDING_CACHE,
    METADATA_ROOT,
    SITE_CONFIG,
    TREE_YML,
    as_list,
    collect_paper_paths,
    collect_papers,
    fast_paper_id_from_file,
    load_paper,
    paper_id_from_file,
    relative_to_kb,
)
from knowledge_base.scripts.list_unplaced_papers.tree_ops import (
    collect_nav_locations,
    collect_tree_leaves,
    insert_after_leaf,
    leaf_line_pattern,
    tree_label,
    tree_source,
    write_tree_placements,
    yaml_key,
)
