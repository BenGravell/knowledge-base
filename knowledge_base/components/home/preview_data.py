"""Small build-time samples for the inert home previews; never load full corpora there."""

from __future__ import annotations

import re
from collections.abc import Iterator
from typing import Any


def build_home_tree_data(tree_data: dict[str, Any]) -> dict[str, Any]:
    def paper_leaves(node: dict[str, Any]) -> Iterator[dict[str, Any]]:
        if node["kind"] == "paper":
            yield node
        for child in node.get("children", []):
            yield from paper_leaves(child)

    selected = set()
    for branch in tree_data["root"]["children"]:
        leaves = list(paper_leaves(branch))
        count = min(12, len(leaves))
        # Evenly sample each top-level branch so smaller subjects remain visible.
        selected.update(leaves[i * len(leaves) // count]["id"] for i in range(count))

    def prune(node: dict[str, Any]) -> dict[str, Any] | None:
        children = [sample for child in node.get("children", []) if (sample := prune(child)) is not None]
        if not children and node["id"] not in selected and node is not tree_data["root"]:
            return None
        sample = {key: node[key] for key in ("id", "label", "kind", "source", "url") if key in node}
        sample["children"] = children
        sample["leafCount"] = (
            sum(child["leafCount"] for child in children) if children else int(node["kind"] == "paper")
        )
        sample["branchCount"] = sum(child["branchCount"] + int(child["kind"] == "branch") for child in children)
        if "paper" in node:
            sample["paper"] = {key: node["paper"][key] for key in ("id", "label", "algorithm") if key in node["paper"]}
        return sample

    root = prune(tree_data["root"])
    assert root is not None, "The preview must retain the tree root"
    return {"root": root, "meta": {"totalLeaves": root["leafCount"], "totalBranches": root["branchCount"]}}


def build_home_search_data(records: list[dict[str, Any]]) -> dict[str, Any]:
    matches = [paper for paper in records if re.search(r"\bplanning\b", paper["title"], re.IGNORECASE)]
    sample = sorted(matches or records, key=lambda paper: str(paper.get("year") or ""), reverse=True)[:2]
    return {"papers": {paper["id"]: paper for paper in sample}, "previewQuery": "planning" if matches else ""}
