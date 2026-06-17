"""List papers that have metadata but are missing from the MkDocs tree.

Usage:
  python scripts/list_unplaced_papers.py
  python scripts/list_unplaced_papers.py --neighbors 3
  python scripts/list_unplaced_papers.py --format paths
  python scripts/list_unplaced_papers.py --write-tree
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

REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from knowledge_base.config import KB_DIR
from knowledge_base.embedding_workbench import load_embedding_table
from knowledge_base.tree.model import (
    TreeLeaf,
    TreeModel,
    load_tree_model,
)
from knowledge_base.utils.paper_ids import paper_id_from_metadata

DOCS_DIR = KB_DIR / "docs"
METADATA_ROOT = DOCS_DIR / "papers"
MKDOCS_YML = KB_DIR / "mkdocs.yml"
EMBEDDING_CACHE = KB_DIR / "map" / "embedding_cache.json"
TREE_YML = KB_DIR / "tree.yml"


@dataclass(frozen=True)
class Paper:
    id: str
    title: str
    algorithm: str
    metadata_path: Path
    generated_path: str
    abstract: str
    tags: tuple[str, ...]


def paper_id_from_file(metadata_file: Path, data: dict[str, Any]) -> str:
    """Return the generated paper ID used by MkDocs gen-files."""
    return paper_id_from_metadata(metadata_file, data, METADATA_ROOT)


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
        algorithm = " ".join(str(data.get("algorithm") or "").split())
        abstract = str(data.get("abstract") or "").strip()
        tags = tuple(str(tag) for tag in as_list(data.get("tags")))
        papers[paper_id] = Paper(
            id=paper_id,
            title=title,
            algorithm=algorithm,
            metadata_path=metadata_file,
            generated_path=f"papers/{paper_id}.md",
            abstract=abstract,
            tags=tags,
        )
    return papers


def collect_nav_locations(model: TreeModel) -> dict[str, list[str]]:
    """Map generated paper ID to the human-readable nav path containing it."""
    return {paper_id: list(placement.nav_path) for paper_id, placement in model.placements_by_paper_id.items()}


def collect_tree_leaves(model: TreeModel) -> dict[str, TreeLeaf]:
    """Map generated paper ID to its raw tree source and nav path."""
    leaves: dict[str, TreeLeaf] = {}
    for leaf in model.leaves:
        if leaf.paper_id:
            leaves.setdefault(leaf.paper_id, leaf)
    return leaves


def load_embeddings(cache_path: Path) -> dict[str, list[float]]:
    if not cache_path.exists():
        return {}
    return {paper_id: vector.tolist() for paper_id, vector in load_embedding_table(cache_path).by_id().items()}


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
        score = sum(a * b for a, b in zip(missing, vector, strict=False)) / (missing_norm * placed_norm)
        rows.append((placed_id, score))

    return sorted(rows, key=lambda item: item[1], reverse=True)[:top_k]


def relative_to_kb(path: Path) -> str:
    try:
        return str(path.relative_to(KB_DIR))
    except ValueError:
        return str(path)


def yaml_key(value: str) -> str:
    if (
        value
        and value == value.strip()
        and not value.startswith(("-", "?", "@", "`"))
        and not re.search(r"[:#{}\[\],&*!|>%\"']", value)
        and value.lower() not in {"null", "true", "false", "yes", "no", "on", "off"}
    ):
        return value
    return json.dumps(value, ensure_ascii=False)


def tree_label(paper: Paper) -> str:
    return paper.algorithm or paper.title


def tree_source(paper: Paper) -> str:
    return relative_to_kb(paper.metadata_path)


def leaf_line_pattern(source: str) -> re.Pattern[str]:
    return re.compile(rf"^(?P<indent>\s*)-\s+(?P<label>.+):\s+{re.escape(source)}\s*(?P<comment>#.*)?$")


def insert_after_leaf(lines: list[str], source: str, new_line: str) -> bool:
    pattern = leaf_line_pattern(source)
    for index, line in enumerate(lines):
        if pattern.match(line.rstrip("\n")):
            lines.insert(index + 1, new_line)
            return True
    return False


def write_tree_placements(
    missing: list[Paper],
    nav_locations: dict[str, list[str]],
    tree_leaves: dict[str, TreeLeaf],
    embeddings: dict[str, list[float]],
    *,
    tree_path: Path,
    min_neighbor_score: float,
) -> tuple[list[tuple[Paper, TreeLeaf, float]], list[tuple[Paper, str]]]:
    placed: list[tuple[Paper, TreeLeaf, float]] = []
    skipped: list[tuple[Paper, str]] = []
    placed_ids = set(nav_locations)

    text = tree_path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    had_trailing_newline = text.endswith("\n")

    used_sources = {leaf.source for leaf in tree_leaves.values()}
    insertion_anchor_by_neighbor_source: dict[str, str] = {}
    for paper in missing:
        source = tree_source(paper)
        if source in used_sources:
            skipped.append((paper, "already present in tree.yml"))
            continue

        candidates = nearest_placed_neighbors(paper.id, placed_ids, embeddings, top_k=1)
        if not candidates:
            skipped.append((paper, "no placed embedding neighbor found"))
            continue

        neighbor_id, score = candidates[0]
        if score < min_neighbor_score:
            skipped.append(
                (
                    paper,
                    f"best neighbor score {score:.3f} is below --min-neighbor-score {min_neighbor_score:.3f}",
                )
            )
            continue

        neighbor = tree_leaves.get(neighbor_id)
        if neighbor is None:
            skipped.append((paper, f"nearest neighbor `{neighbor_id}` has no raw tree source"))
            continue

        pattern = leaf_line_pattern(neighbor.source)
        indent = None
        for line in lines:
            match = pattern.match(line.rstrip("\n"))
            if match:
                indent = match.group("indent")
                break
        if indent is None:
            skipped.append((paper, f"could not find neighbor source `{neighbor.source}` in tree.yml"))
            continue

        line = f"{indent}- {yaml_key(tree_label(paper))}: {source}\n"
        insertion_anchor = insertion_anchor_by_neighbor_source.get(neighbor.source, neighbor.source)
        if not insert_after_leaf(lines, insertion_anchor, line):
            skipped.append((paper, f"could not insert after source `{insertion_anchor}`"))
            continue

        insertion_anchor_by_neighbor_source[neighbor.source] = source
        placed.append((paper, neighbor, score))
        placed_ids.add(paper.id)
        used_sources.add(source)
        nav_path = (*neighbor.nav_path[:-1], tree_label(paper))
        tree_leaves[paper.id] = TreeLeaf(
            label=tree_label(paper),
            source=source,
            path=neighbor.path,
            nav_path=nav_path,
            paper_id=paper.id,
            generated_source=paper.generated_path,
            metadata_path=paper.metadata_path,
        )
        nav_locations[paper.id] = list(nav_path)

    new_text = "".join(lines)
    if had_trailing_newline and not new_text.endswith("\n"):
        new_text += "\n"

    if placed:
        yaml.safe_load(new_text)
        tree_path.write_text(new_text, encoding="utf-8")

    return placed, skipped


def print_write_summary(
    placed: list[tuple[Paper, TreeLeaf, float]],
    skipped: list[tuple[Paper, str]],
) -> None:
    print(f"Wrote {len(placed)} placement(s) to tree.yml.")
    for paper, neighbor, score in placed:
        location = " > ".join(neighbor.nav_path[:-1])
        print(f"- {tree_label(paper)} (`{paper.id}`) after `{neighbor.paper_id}` ({score:.3f}) in {location}")

    if skipped:
        print(f"\nSkipped {len(skipped)} paper(s):")
        for paper, reason in skipped:
            print(f"- {paper.title} (`{paper.id}`): {reason}")


def print_markdown(
    missing: list[Paper],
    nav_locations: dict[str, list[str]],
    embeddings: dict[str, list[float]],
    *,
    neighbors: int,
    total_missing: int,
) -> None:
    placed_ids = set(nav_locations)
    print("# Unplaced Papers\n")
    print(f"{total_missing} paper(s) have metadata but are missing from the Tree.\n")
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
        description="List metadata-backed papers missing from the MkDocs Tree.",
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
    parser.add_argument(
        "--write-tree",
        action="store_true",
        help=(
            "Insert missing papers into tree.yml after their nearest already-placed "
            "embedding neighbor. Uses the metadata algorithm as the label when present."
        ),
    )
    parser.add_argument(
        "--tree-yml",
        type=Path,
        default=TREE_YML,
        help="Tree YAML file to read and optionally write.",
    )
    parser.add_argument(
        "--min-neighbor-score",
        type=float,
        default=-1.0,
        help="When writing, skip placements below this cosine-similarity score.",
    )
    args = parser.parse_args()

    with MKDOCS_YML.open("r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    if not isinstance(config, dict):
        sys.exit(f"Could not parse MkDocs config: {MKDOCS_YML}")

    tree_model = load_tree_model(
        args.tree_yml,
        config=config,
        base_dir=KB_DIR,
        metadata_root=METADATA_ROOT,
    )
    papers = collect_papers(METADATA_ROOT)
    nav_locations = collect_nav_locations(tree_model)
    missing = [paper for paper_id, paper in sorted(papers.items()) if paper_id not in nav_locations]
    display = missing[: args.max_results] if args.max_results is not None else missing
    needs_embeddings = args.neighbors > 0 or args.write_tree
    embeddings: dict[str, list[float]] = load_embeddings(EMBEDDING_CACHE) if needs_embeddings else {}

    if args.write_tree:
        if not embeddings:
            sys.exit(
                f"Could not load embeddings from {EMBEDDING_CACHE}. "
                "Run `python knowledge_base/map/generate_map_data.py` first."
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
