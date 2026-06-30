"""Command-line entrypoint for branch subgroup suggestions."""

import argparse
import json
import sys
from pathlib import Path

from knowledge_base.components.tree.nav_source import TREE_YML
from knowledge_base.scripts.suggest_branch_subgroupings.common import relative_to_kb


def main() -> None:
    parser = argparse.ArgumentParser(
        description=(
            "Suggest one new Tree sub-grouping level for branches with too many "
            "direct children, using cached text embeddings."
        )
    )
    parser.add_argument("--min", dest="minimum", type=int, default=2)
    parser.add_argument("--max", dest="maximum", type=int, default=7)
    parser.add_argument("--sweet-spot", type=int, default=5)
    parser.add_argument(
        "--count",
        choices=("all", "branches"),
        default="all",
        help="Match list_branching_factor_violations.py counting mode.",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format.",
    )
    parser.add_argument(
        "--branch",
        default=None,
        help="Only suggest for branches whose formatted path contains this text.",
    )
    parser.add_argument(
        "--max-depth",
        type=int,
        default=None,
        help="Only consider branches through this depth; Tree is depth 0.",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=10,
        help="Maximum number of overfull branches to suggest.",
    )
    parser.add_argument(
        "--max-groups",
        type=int,
        default=None,
        help="Maximum candidate group count. Defaults to an automatic range.",
    )
    parser.add_argument(
        "--show-items",
        type=int,
        default=12,
        help="Markdown: show up to N children per suggested group.",
    )
    parser.add_argument(
        "--min-embedded-children",
        type=int,
        default=4,
        help="Skip branches with fewer than N embeddable direct children.",
    )
    parser.add_argument(
        "--exclude-root",
        action="store_true",
        help="Do not consider the synthetic Tree root branch.",
    )
    parser.add_argument(
        "--write-tree",
        action="store_true",
        help=(
            "Write exactly one suggested regrouping into tree.yml. "
            "Use --branch or --max-results 1 to select a single target."
        ),
    )
    parser.add_argument(
        "--tree-yml",
        type=Path,
        default=TREE_YML,
        help="Tree YAML file to read and optionally write. Defaults to knowledge_base/tree.yml.",
    )
    args = parser.parse_args()

    if args.minimum < 0 or args.maximum < 1:
        sys.exit("--min must be non-negative and --max must be at least 1.")
    if args.minimum > args.maximum:
        sys.exit("--min cannot be greater than --max.")
    if args.sweet_spot < 1:
        sys.exit("--sweet-spot must be at least 1.")
    if args.max_depth is not None and args.max_depth < 0:
        sys.exit("--max-depth must be at least 0.")
    if args.max_groups is not None and args.max_groups < 2:
        sys.exit("--max-groups must be at least 2.")

    from knowledge_base.scripts.suggest_branch_subgroupings.clustering import build_suggestion, find_too_many_branches
    from knowledge_base.scripts.suggest_branch_subgroupings.data import collect_branches, load_embeddings, load_papers
    from knowledge_base.scripts.suggest_branch_subgroupings.output import print_markdown, suggestion_to_json
    from knowledge_base.scripts.suggest_branch_subgroupings.tree_edit import apply_tree_suggestion

    tree_path = args.tree_yml
    branches = collect_branches(
        include_root=not args.exclude_root,
        tree_path=tree_path,
    )
    too_many = find_too_many_branches(
        branches,
        mode=args.count,
        maximum=args.maximum,
        max_depth=args.max_depth,
        branch_filter=args.branch,
    )

    papers = load_papers()
    embeddings = load_embeddings()
    suggestions = []
    for branch in too_many:
        suggestion = build_suggestion(
            branch,
            children=branch.children_for(args.count),
            embeddings=embeddings,
            papers=papers,
            minimum=args.minimum,
            maximum=args.maximum,
            sweet_spot=args.sweet_spot,
            max_groups=args.max_groups,
            min_embedded_children=args.min_embedded_children,
        )
        if suggestion is not None:
            suggestions.append(suggestion)
        if args.max_results is not None and len(suggestions) >= args.max_results:
            break

    wrote_tree = False
    if args.write_tree:
        if not suggestions:
            sys.exit("--write-tree found no suggestion to write.")
        if len(suggestions) > 1:
            sys.exit("--write-tree needs exactly one suggestion. Narrow with --branch or pass --max-results 1.")
        apply_tree_suggestion(tree_path, suggestions[0])
        wrote_tree = True

    if args.format == "json":
        print(
            json.dumps(
                {
                    "too_many_branch_count": len(too_many),
                    "suggestion_count": len(suggestions),
                    "wrote_tree": wrote_tree,
                    "tree_yml": relative_to_kb(tree_path),
                    "suggestions": [suggestion_to_json(suggestion, mode=args.count) for suggestion in suggestions],
                },
                indent=2,
                ensure_ascii=False,
            )
        )
    else:
        if wrote_tree:
            print(f"Wrote suggested subgrouping to {relative_to_kb(tree_path)}.\n")
        print_markdown(
            suggestions,
            total_too_many=len(too_many),
            mode=args.count,
            maximum=args.maximum,
            shown_items=args.show_items,
        )


__all__ = ["main"]
