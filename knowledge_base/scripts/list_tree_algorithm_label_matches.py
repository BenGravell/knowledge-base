"""List Tree leaves whose nav label exactly matches metadata algorithm.

Usage:
  python scripts/list_tree_algorithm_label_matches.py
  python scripts/list_tree_algorithm_label_matches.py --max-results 20
  python scripts/list_tree_algorithm_label_matches.py --format json
  python scripts/list_tree_algorithm_label_matches.py --fail-on-matches
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from knowledge_base.config import KB_DIR
from knowledge_base.tree.model import (
    TreeModel,
    load_tree_model,
)
from knowledge_base.tree.nav_source import TREE_YML

METADATA_ROOT = KB_DIR / "docs" / "papers"


@dataclass(frozen=True)
class Match:
    tree_path: tuple[str, ...]
    tree_label: str
    algorithm: str
    metadata_path: Path
    title: str


def normalize_label(value: str) -> str:
    return " ".join(value.split()).casefold()


def relative_to_kb(path: Path) -> str:
    try:
        return str(path.relative_to(KB_DIR))
    except ValueError:
        return str(path)


def load_metadata(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data if isinstance(data, dict) else {}


def load_algorithm_tree_model() -> TreeModel:
    return load_tree_model(
        TREE_YML,
        base_dir=KB_DIR,
        metadata_root=METADATA_ROOT,
    )


def collect_matches(model: TreeModel) -> list[Match]:
    matches: list[Match] = []

    for leaf in model.leaves:
        if leaf.metadata_path is None:
            continue

        data = load_metadata(leaf.metadata_path)
        algorithm = " ".join(str(data.get("algorithm") or "").split())
        if not algorithm:
            continue
        if normalize_label(leaf.label) != normalize_label(algorithm):
            continue

        title = " ".join(str(data.get("title") or "").split())
        matches.append(
            Match(
                tree_path=("Tree", *leaf.nav_path),
                tree_label=leaf.label,
                algorithm=algorithm,
                metadata_path=leaf.metadata_path,
                title=title,
            )
        )
    return matches


def format_tree_path(path: tuple[str, ...]) -> str:
    return " > ".join(path)


def print_markdown(matches: list[Match], *, total_matches: int) -> None:
    print("# Tree Labels Matching Metadata Algorithm\n")
    print(f"{total_matches} Tree leaf label(s) exactly match the metadata algorithm field.\n")
    for match in matches:
        print(f"- `{format_tree_path(match.tree_path)}`")
        print(f"  - Tree label: `{match.tree_label}`")
        print(f"  - Metadata algorithm: `{match.algorithm}`")
        print(f"  - Title: {match.title}")
        print(f"  - Metadata: `{relative_to_kb(match.metadata_path)}`")
    if total_matches > len(matches):
        print(f"\n... {total_matches - len(matches)} more match(es) not shown.")


def print_json(matches: list[Match]) -> None:
    payload = [
        {
            "tree_path": list(match.tree_path),
            "tree_label": match.tree_label,
            "algorithm": match.algorithm,
            "title": match.title,
            "metadata_path": relative_to_kb(match.metadata_path),
        }
        for match in matches
    ]
    print(json.dumps(payload, indent=2, ensure_ascii=False))


def main() -> int:
    parser = argparse.ArgumentParser(description="List Tree leaves whose label exactly matches metadata algorithm.")
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format (default: markdown).",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=100,
        help="Maximum number of matches to print (default: 100).",
    )
    parser.add_argument(
        "--fail-on-matches",
        action="store_true",
        help="Exit with status 1 when any matches are found.",
    )
    args = parser.parse_args()
    if args.max_results < 1:
        parser.error("--max-results must be at least 1")

    matches = collect_matches(load_algorithm_tree_model())
    displayed = matches[: args.max_results]
    if args.format == "json":
        print_json(displayed)
    else:
        print_markdown(displayed, total_matches=len(matches))
    return 1 if args.fail_on_matches and matches else 0


if __name__ == "__main__":
    raise SystemExit(main())
