"""List papers that have metadata but are missing from the MkDocs content tree.

Usage:
  python scripts/list_unplaced_papers.py
  python scripts/list_unplaced_papers.py --neighbors 5
  python scripts/list_unplaced_papers.py --format paths
  python scripts/list_unplaced_papers.py --fail-on-missing
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from knowledge_base.config import KB_DIR

DOCS_DIR = KB_DIR / "docs"
METADATA_ROOT = DOCS_DIR / "papers"
MKDOCS_YML = KB_DIR / "mkdocs.yml"
EMBEDDING_CACHE = KB_DIR / "mind_map" / "embedding_cache.json"


@dataclass(frozen=True)
class Paper:
    id: str
    title: str
    metadata_path: Path
    generated_path: str
    abstract: str
    tags: tuple[str, ...]


def slugify(name: str) -> str:
    """Match the generated paper URL logic in knowledge_base/generate_papers.py."""
    return re.sub(r"[^a-zA-Z0-9]+", "_", name.lower()).strip("_")


def paper_id_from_file(metadata_file: Path, data: dict[str, Any]) -> str:
    """Return the generated paper ID used by MkDocs gen-files."""
    if "id" in data:
        return slugify(str(data["id"]))
    if metadata_file.stem != "metadata":
        return slugify(metadata_file.stem)
    return slugify(metadata_file.parent.name)


def as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    return []


def collect_papers(metadata_root: Path) -> dict[str, Paper]:
    papers: dict[str, Paper] = {}
    for metadata_file in sorted(metadata_root.rglob("metadata.yml")):
        with metadata_file.open("r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        if not isinstance(data, dict):
            continue

        paper_id = paper_id_from_file(metadata_file, data)
        title = " ".join(str(data.get("title") or paper_id).split())
        abstract = str(data.get("abstract") or "").strip()
        tags = tuple(str(tag) for tag in as_list(data.get("tags")))
        papers[paper_id] = Paper(
            id=paper_id,
            title=title,
            metadata_path=metadata_file,
            generated_path=f"papers/{paper_id}.md",
            abstract=abstract,
            tags=tags,
        )
    return papers


def content_tree(config: dict[str, Any]) -> Any:
    """Return the nav subtree below the top-level Content Tree section."""
    for item in as_list(config.get("nav")):
        if isinstance(item, dict) and "Content Tree" in item:
            return item["Content Tree"]
    return []


def collect_nav_locations(nav: Any) -> dict[str, list[str]]:
    """Map generated paper ID to the human-readable nav path containing it."""
    locations: dict[str, list[str]] = {}

    def walk(node: Any, labels: list[str]) -> None:
        if isinstance(node, str):
            if node.startswith("papers/") and node.endswith(".md"):
                paper_id = node.removeprefix("papers/").removesuffix(".md")
                locations.setdefault(paper_id, labels[:])
            return

        if isinstance(node, list):
            for item in node:
                walk(item, labels)
            return

        if isinstance(node, dict):
            for label, child in node.items():
                if isinstance(child, str):
                    if child.startswith("papers/") and child.endswith(".md"):
                        paper_id = child.removeprefix("papers/").removesuffix(".md")
                        locations.setdefault(paper_id, labels + [str(label)])
                    continue
                walk(child, labels + [str(label)])

    walk(nav, [])
    return locations


def load_embeddings(cache_path: Path) -> dict[str, list[float]]:
    if not cache_path.exists():
        return {}
    with cache_path.open("r", encoding="utf-8") as f:
        cache = json.load(f)
    papers = cache.get("papers", {})
    if not isinstance(papers, dict):
        return {}
    embeddings: dict[str, list[float]] = {}
    for paper_id, entry in papers.items():
        if isinstance(entry, dict) and isinstance(entry.get("embedding"), list):
            embeddings[str(paper_id)] = entry["embedding"]
    return embeddings


def nearest_placed_neighbors(
    missing_id: str,
    placed_ids: set[str],
    embeddings: dict[str, list[float]],
    *,
    top_k: int,
) -> list[tuple[str, float]]:
    if top_k <= 0 or missing_id not in embeddings:
        return []

    missing = embeddings[missing_id]
    missing_norm = math.sqrt(sum(value * value for value in missing))
    if missing_norm == 0.0:
        return []

    rows: list[tuple[str, float]] = []
    for placed_id in placed_ids:
        vector = embeddings.get(placed_id)
        if vector is None:
            continue
        placed_norm = math.sqrt(sum(value * value for value in vector))
        if placed_norm == 0.0:
            continue
        score = sum(a * b for a, b in zip(missing, vector)) / (missing_norm * placed_norm)
        rows.append((placed_id, score))

    return sorted(rows, key=lambda item: item[1], reverse=True)[:top_k]


def relative_to_kb(path: Path) -> str:
    try:
        return str(path.relative_to(KB_DIR))
    except ValueError:
        return str(path)


def print_markdown(
    missing: list[Paper],
    nav_locations: dict[str, list[str]],
    embeddings: dict[str, list[float]],
    *,
    neighbors: int,
    total_missing: int,
) -> None:
    placed_ids = set(nav_locations)
    print(f"# Unplaced Papers\n")
    print(f"{total_missing} paper(s) have metadata but are missing from the Content Tree.\n")
    for paper in missing:
        print(f"- {paper.title} (`{paper.id}`)")
        print(f"  - Metadata: `{relative_to_kb(paper.metadata_path)}`")
        print(f"  - Generated page: `{paper.generated_path}`")
        candidates = nearest_placed_neighbors(
            paper.id,
            placed_ids,
            embeddings,
            top_k=neighbors,
        )
        if candidates:
            print("  - Nearest placed neighbors:")
            for neighbor_id, score in candidates:
                location = " > ".join(nav_locations.get(neighbor_id, []))
                print(f"    - {score:.3f} `{neighbor_id}`: {location}")
        elif neighbors > 0:
            print("  - Nearest placed neighbors: unavailable")


def print_json(
    missing: list[Paper],
    nav_locations: dict[str, list[str]],
    embeddings: dict[str, list[float]],
    *,
    neighbors: int,
) -> None:
    placed_ids = set(nav_locations)
    rows: list[dict[str, Any]] = []
    for paper in missing:
        candidates = nearest_placed_neighbors(
            paper.id,
            placed_ids,
            embeddings,
            top_k=neighbors,
        )
        rows.append(
            {
                "id": paper.id,
                "title": paper.title,
                "metadata_path": relative_to_kb(paper.metadata_path),
                "generated_path": paper.generated_path,
                "nearest_placed_neighbors": [
                    {
                        "id": neighbor_id,
                        "score": round(score, 6),
                        "nav_path": nav_locations.get(neighbor_id, []),
                    }
                    for neighbor_id, score in candidates
                ],
            }
        )
    print(json.dumps(rows, indent=2, ensure_ascii=False))


def main() -> None:
    parser = argparse.ArgumentParser(
        description="List metadata-backed papers missing from the MkDocs Content Tree.",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json", "paths"),
        default="markdown",
        help="Output format.",
    )
    parser.add_argument(
        "--neighbors",
        type=int,
        default=3,
        help="Number of nearest already-placed embedding neighbors to show.",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=None,
        help="Limit the number of missing papers displayed.",
    )
    parser.add_argument(
        "--fail-on-missing",
        action="store_true",
        help="Exit with status 1 when any missing papers are found.",
    )
    args = parser.parse_args()

    with MKDOCS_YML.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    if not isinstance(config, dict):
        sys.exit(f"Could not parse MkDocs config: {MKDOCS_YML}")

    papers = collect_papers(METADATA_ROOT)
    nav_locations = collect_nav_locations(content_tree(config))
    missing = [paper for paper_id, paper in sorted(papers.items()) if paper_id not in nav_locations]
    display = missing[: args.max_results] if args.max_results is not None else missing
    embeddings = load_embeddings(EMBEDDING_CACHE) if args.neighbors > 0 else {}

    if args.format == "paths":
        for paper in display:
            print(paper.generated_path)
    elif args.format == "json":
        print_json(display, nav_locations, embeddings, neighbors=args.neighbors)
    else:
        print_markdown(
            display,
            nav_locations,
            embeddings,
            neighbors=args.neighbors,
            total_missing=len(missing),
        )
        if args.max_results is not None and len(missing) > len(display):
            print(f"\n{len(missing) - len(display)} more missing paper(s) not shown.")

    if args.fail_on_missing and missing:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
