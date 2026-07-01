"""Output helpers for unplaced-paper reports."""

from __future__ import annotations

import json
from typing import Any

from knowledge_base.scripts.list_unplaced_papers.embeddings import nearest_placed_neighbors
from knowledge_base.scripts.list_unplaced_papers.model import Paper
from knowledge_base.scripts.list_unplaced_papers.tree_ops import tree_label
from knowledge_base.scripts.tree_report_data import relative_to_kb
from knowledge_base.tree.model import TreeLeaf


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


def print_empty(format_name: str) -> None:
    if format_name == "json":
        print("[]")
    elif format_name == "markdown":
        print("# Unplaced Papers\n")
        print("0 paper(s) have metadata but are missing from the Tree.\n")


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
