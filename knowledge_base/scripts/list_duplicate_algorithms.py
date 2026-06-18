"""List metadata items that claim the same non-empty algorithm label.

Usage:
  python scripts/list_duplicate_algorithms.py
  python scripts/list_duplicate_algorithms.py --max-results 20
  python scripts/list_duplicate_algorithms.py --format json
  python scripts/list_duplicate_algorithms.py --fail-on-duplicates
"""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from knowledge_base.config import KB_DIR
from knowledge_base.utils.paper_ids import paper_id_from_metadata

METADATA_ROOT = KB_DIR / "docs" / "papers"


@dataclass(frozen=True)
class Paper:
    id: str
    title: str
    algorithm: str
    metadata_path: Path


def normalize_algorithm(value: str) -> str:
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


def collect_papers(metadata_root: Path = METADATA_ROOT) -> list[Paper]:
    papers: list[Paper] = []
    for metadata_path in sorted(metadata_root.rglob("metadata.yml")):
        data = load_metadata(metadata_path)
        algorithm = " ".join(str(data.get("algorithm") or "").split())
        if not algorithm:
            continue
        papers.append(
            Paper(
                id=paper_id_from_metadata(metadata_path, data, metadata_root),
                title=" ".join(str(data.get("title") or "").split()),
                algorithm=algorithm,
                metadata_path=metadata_path,
            )
        )
    return papers


def duplicate_groups(papers: list[Paper], *, min_count: int) -> list[tuple[str, list[Paper]]]:
    by_algorithm: dict[str, list[Paper]] = defaultdict(list)
    display_labels: dict[str, str] = {}
    for paper in papers:
        key = normalize_algorithm(paper.algorithm)
        by_algorithm[key].append(paper)
        display_labels.setdefault(key, paper.algorithm)

    groups = [
        (display_labels[key], sorted(items, key=lambda paper: paper.id))
        for key, items in by_algorithm.items()
        if len(items) >= min_count
    ]
    return sorted(groups, key=lambda item: (-len(item[1]), item[0].casefold()))


def print_markdown(
    groups: list[tuple[str, list[Paper]]],
    *,
    total_groups: int,
    total_items: int,
) -> None:
    print("# Duplicate Algorithm Claims\n")
    print(
        f"{total_groups} algorithm label(s) are claimed by multiple metadata items ({total_items} item assignments).\n"
    )
    for algorithm, papers in groups:
        print(f"- `{algorithm}` ({len(papers)} items)")
        for paper in papers:
            print(f"  - `{paper.id}`: {paper.title}")
            print(f"    - Metadata: `{relative_to_kb(paper.metadata_path)}`")
    if total_groups > len(groups):
        print(f"\n... {total_groups - len(groups)} more duplicate group(s) not shown.")


def print_json(groups: list[tuple[str, list[Paper]]]) -> None:
    payload = [
        {
            "algorithm": algorithm,
            "count": len(papers),
            "items": [
                {
                    "id": paper.id,
                    "title": paper.title,
                    "metadata_path": relative_to_kb(paper.metadata_path),
                }
                for paper in papers
            ],
        }
        for algorithm, papers in groups
    ]
    print(json.dumps(payload, indent=2, ensure_ascii=False))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="List non-empty metadata algorithm labels used by more than one paper."
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format (default: markdown).",
    )
    parser.add_argument(
        "--min-count",
        type=int,
        default=2,
        help="Minimum number of matching metadata items to report (default: 2).",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=100,
        help="Maximum number of duplicate groups to print (default: 100).",
    )
    parser.add_argument(
        "--fail-on-duplicates",
        action="store_true",
        help="Exit with status 1 when duplicate algorithm claims are found.",
    )
    args = parser.parse_args()

    if args.min_count < 2:
        parser.error("--min-count must be at least 2")
    if args.max_results < 1:
        parser.error("--max-results must be at least 1")

    groups = duplicate_groups(collect_papers(), min_count=args.min_count)
    displayed = groups[: args.max_results]
    if args.format == "json":
        print_json(displayed)
    else:
        print_markdown(
            displayed,
            total_groups=len(groups),
            total_items=sum(len(items) for _, items in groups),
        )
    return 1 if args.fail_on_duplicates and groups else 0


if __name__ == "__main__":
    raise SystemExit(main())
