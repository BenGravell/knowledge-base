"""Command-line interface for listing unplaced papers."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

from knowledge_base.config import KB_DIR
from knowledge_base.scripts.list_unplaced_papers.embeddings import load_embeddings
from knowledge_base.scripts.list_unplaced_papers.output import (
    print_empty,
    print_json,
    print_markdown,
    print_write_summary,
)
from knowledge_base.scripts.list_unplaced_papers.tree_ops import (
    write_tree_placements,
)
from knowledge_base.scripts.tree_report_data import (
    EMBEDDING_CACHE,
    SITE_CONFIG,
    TREE_YML,
    collect_nav_locations,
    collect_tree_leaves,
    load_report_papers,
)
from knowledge_base.tree.model import load_tree_model


def main() -> None:
    parser = argparse.ArgumentParser(
        description="List metadata-backed papers missing from the site Tree.",
    )
    parser.add_argument("--format", choices=("markdown", "json", "paths"), default="markdown", help="Output format.")
    parser.add_argument(
        "--neighbors",
        type=int,
        default=3,
        help="Number of nearest already-placed embedding neighbors to show.",
    )
    parser.add_argument("--max-results", type=int, default=None, help="Limit the number of missing papers displayed.")
    parser.add_argument(
        "--fail-on-missing",
        action="store_true",
        help="Exit with status 1 when any missing papers are found.",
    )
    parser.add_argument(
        "--write-tree",
        action="store_true",
        help=(
            "Insert missing papers into tree.yml after their nearest already-placed "
            "embedding neighbor. Uses the metadata algorithm as the label when present."
        ),
    )
    parser.add_argument("--tree-yml", type=Path, default=TREE_YML, help="Tree YAML file to read and optionally write.")
    parser.add_argument(
        "--min-neighbor-score",
        type=float,
        default=-1.0,
        help="When writing, skip placements below this cosine-similarity score.",
    )
    args = parser.parse_args()

    with SITE_CONFIG.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    if not isinstance(config, dict):
        sys.exit(f"Could not parse site config: {SITE_CONFIG}")

    tree_model = load_tree_model(args.tree_yml, config=config, base_dir=KB_DIR)
    nav_locations = collect_nav_locations(tree_model)
    papers_by_id = load_report_papers()
    missing_ids = [paper_id for paper_id in sorted(papers_by_id) if paper_id not in nav_locations]
    if not missing_ids:
        print_empty(args.format)
        return

    missing = [papers_by_id[paper_id] for paper_id in missing_ids]
    display = missing[: args.max_results] if args.max_results is not None else missing
    needs_embeddings = args.neighbors > 0 or args.write_tree
    embeddings: dict[str, list[float]] = load_embeddings(EMBEDDING_CACHE) if needs_embeddings else {}

    if args.write_tree:
        if not embeddings:
            sys.exit(
                f"Could not load embeddings from {EMBEDDING_CACHE}. "
                "Run `python -m knowledge_base.components.map.pipeline.generate_data` first."
            )
        tree_leaves = collect_tree_leaves(tree_model)
        placed, skipped = write_tree_placements(
            display,
            nav_locations,
            tree_leaves,
            embeddings,
            tree_path=args.tree_yml,
            min_neighbor_score=args.min_neighbor_score,
        )
        print_write_summary(placed, skipped)
        if args.fail_on_missing and (len(missing) - len(placed) > 0):
            raise SystemExit(1)
        return

    if args.format == "paths":
        for paper in display:
            print(paper.generated_path)
    elif args.format == "json":
        print_json(display, nav_locations, embeddings, neighbors=args.neighbors)
    else:
        print_markdown(display, nav_locations, embeddings, neighbors=args.neighbors, total_missing=len(missing))
        if args.max_results is not None and len(missing) > len(display):
            print(f"\n{len(missing) - len(display)} more missing paper(s) not shown.")

    if args.fail_on_missing and missing:
        raise SystemExit(1)
