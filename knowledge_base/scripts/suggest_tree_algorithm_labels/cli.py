"""Command-line entrypoint for tree algorithm label suggestions."""

import argparse
import json
from pathlib import Path

from knowledge_base.scripts.suggest_tree_algorithm_labels.constants import ACTIONS, CONFIDENCE_LOW, CONFIDENCES
from knowledge_base.scripts.suggest_tree_algorithm_labels.output import (
    filter_suggestions,
    print_markdown,
    suggestion_to_dict,
)
from knowledge_base.scripts.suggest_tree_algorithm_labels.suggestions import collect_suggestions
from knowledge_base.tree.validation import METADATA_ROOT, TREE_YML


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Suggest canonical labels for Tree/metadata algorithm disagreements.")
    parser.add_argument(
        "--tree-yml",
        type=Path,
        default=TREE_YML,
        help="Path to the Tree YAML source.",
    )
    parser.add_argument(
        "--metadata-root",
        type=Path,
        default=METADATA_ROOT,
        help="Path to docs/papers metadata source.",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format.",
    )
    parser.add_argument(
        "--action",
        choices=ACTIONS,
        default=None,
        help="Only show suggestions with this recommended action.",
    )
    parser.add_argument(
        "--min-confidence",
        choices=CONFIDENCES,
        default=CONFIDENCE_LOW,
        help="Only show suggestions at or above this confidence.",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=100,
        help="Maximum number of suggestions to print in Markdown output.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.max_results < 1:
        raise SystemExit("--max-results must be at least 1")

    suggestions = collect_suggestions(args.tree_yml, args.metadata_root)
    filtered = filter_suggestions(
        suggestions,
        action=args.action,
        min_confidence=args.min_confidence,
    )

    if args.format == "json":
        print(
            json.dumps(
                {
                    "total_suggestions": len(suggestions),
                    "shown_suggestions": len(filtered),
                    "suggestions": [suggestion_to_dict(item) for item in filtered],
                },
                indent=2,
                ensure_ascii=False,
            )
        )
    else:
        print_markdown(
            filtered,
            total=len(suggestions),
            max_results=args.max_results,
        )
    return 0


__all__ = ["main", "parse_args"]
