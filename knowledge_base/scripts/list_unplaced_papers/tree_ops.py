"""Tree helpers for unplaced-paper reporting and insertion."""

from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

from knowledge_base.scripts.list_unplaced_papers.embeddings import nearest_placed_neighbors
from knowledge_base.scripts.tree_report_data import ReportPaper as Paper
from knowledge_base.scripts.tree_report_data import relative_to_kb
from knowledge_base.tree.model import TreeLeaf


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
