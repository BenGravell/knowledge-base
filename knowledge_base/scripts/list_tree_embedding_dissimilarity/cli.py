"""CLI for Tree embedding dissimilarity reports."""

from __future__ import annotations

import argparse

from knowledge_base.components.tree.nav_source import TREE_YML
from knowledge_base.scripts.list_tree_embedding_dissimilarity.analysis import find_outliers
from knowledge_base.scripts.list_tree_embedding_dissimilarity.data import collect_branches, load_embeddings, load_papers
from knowledge_base.scripts.list_tree_embedding_dissimilarity.output import print_json, print_markdown


def main() -> int:
    parser = argparse.ArgumentParser(description="Soft-audit Tree categories for embedding outliers.")
    parser.add_argument("--scope", choices=("direct", "descendants"), default="direct")
    parser.add_argument("--min-items", type=int, default=3)
    parser.add_argument("--min-similarity", type=float, default=0.35)
    parser.add_argument("--min-drop-from-mean", type=float, default=0.15)
    parser.add_argument("--max-depth", type=int, default=None)
    parser.add_argument("--branch", help="Only audit branches whose path contains this text.")
    parser.add_argument("--max-results", type=int, default=50)
    parser.add_argument("--max-outliers-per-branch", type=int, default=3)
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument("--fail-on-findings", action="store_true")
    args = parser.parse_args()

    if args.min_items < 2:
        parser.error("--min-items must be at least 2")
    if args.max_results < 1:
        parser.error("--max-results must be at least 1")
    if args.max_outliers_per_branch < 1:
        parser.error("--max-outliers-per-branch must be at least 1")

    findings = find_outliers(
        collect_branches(TREE_YML),
        papers=load_papers(),
        embeddings=load_embeddings(),
        scope=args.scope,
        min_items=args.min_items,
        min_similarity=args.min_similarity,
        min_drop_from_mean=args.min_drop_from_mean,
        max_depth=args.max_depth,
        branch_filter=args.branch,
        max_outliers_per_branch=args.max_outliers_per_branch,
    )
    displayed = findings[: args.max_results]

    if args.format == "json":
        print_json(displayed)
    else:
        print_markdown(
            displayed,
            total_findings=len(findings),
            scope=args.scope,
            min_items=args.min_items,
            min_similarity=args.min_similarity,
            min_drop_from_mean=args.min_drop_from_mean,
            max_depth=args.max_depth,
        )
        if len(findings) > len(displayed):
            print(f"\n... {len(findings) - len(displayed)} more branch(es) not shown.")
    return 1 if args.fail_on_findings and findings else 0
