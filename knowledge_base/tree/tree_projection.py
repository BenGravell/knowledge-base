"""Browser Tree data projection."""

from __future__ import annotations

from typing import Any

from knowledge_base.tree.model import TreeBranch, TreeChild, TreeLeaf, TreeModel
from knowledge_base.tree.projection_common import page_url, slugify_id


class IdFactory:
    def __init__(self) -> None:
        self.seen: dict[str, int] = {}

    def make(self, path: list[str], source: str | None = None) -> str:
        base = slugify_id("|".join(path + ([source] if source else [])))
        count = self.seen.get(base, 0)
        self.seen[base] = count + 1
        return base if count == 0 else f"{base}-{count + 1}"


def link_kind(source: str) -> str:
    if source.startswith("papers/") and source.endswith(".md"):
        return "paper"
    if source.endswith(".md"):
        return "page"
    return "link"


def display_path(path: tuple[str, ...]) -> list[str]:
    return ["Tree"] if path == ("Tree",) else ["Tree", *path]


def branch_path_for_child(branch: TreeBranch, child: TreeChild) -> tuple[str, ...]:
    parent_path = () if branch.path == ("Tree",) else branch.path
    return (*parent_path, child.label)


def build_leaf(
    leaf: TreeLeaf,
    ids: IdFactory,
    paper_details_by_source: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    source = leaf.generated_source or leaf.source
    full_path = ["Tree", *leaf.nav_path]
    node: dict[str, Any] = {
        "id": ids.make(full_path, source),
        "label": leaf.label,
        "kind": link_kind(source),
        "source": source,
        "url": page_url(source),
        "path": full_path,
        "children": list[dict[str, Any]](),
        "leafCount": 1,
        "branchCount": 0,
    }
    if node["kind"] == "paper":
        node["paper"] = paper_details_by_source.get(source, dict[str, Any]())
    return node


def build_branch(
    branch: TreeBranch,
    *,
    branches_by_path: dict[tuple[str, ...], TreeBranch],
    leaves_by_parent_label_source: dict[tuple[tuple[str, ...], str, str], TreeLeaf],
    ids: IdFactory,
    paper_details_by_source: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    full_path = display_path(branch.path)
    children = build_branch_children(
        branch,
        branches_by_path=branches_by_path,
        leaves_by_parent_label_source=leaves_by_parent_label_source,
        ids=ids,
        paper_details_by_source=paper_details_by_source,
    )
    leaf_count = sum(node["leafCount"] for node in children)
    branch_count = len([node for node in children if node["kind"] == "branch"])
    branch_count += sum(node["branchCount"] for node in children)
    return {
        "id": ids.make(full_path),
        "label": full_path[-1],
        "kind": "branch",
        "source": None,
        "url": None,
        "path": full_path,
        "children": children,
        "leafCount": leaf_count,
        "branchCount": branch_count,
    }


def build_branch_children(
    branch: TreeBranch,
    *,
    branches_by_path: dict[tuple[str, ...], TreeBranch],
    leaves_by_parent_label_source: dict[tuple[tuple[str, ...], str, str], TreeLeaf],
    ids: IdFactory,
    paper_details_by_source: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    nodes: list[dict[str, Any]] = []
    parent_path = () if branch.path == ("Tree",) else branch.path
    for child in branch.children:
        if child.kind == "branch":
            child_branch = branches_by_path.get(branch_path_for_child(branch, child))
            if child_branch is not None:
                nodes.append(
                    build_branch(
                        child_branch,
                        branches_by_path=branches_by_path,
                        leaves_by_parent_label_source=leaves_by_parent_label_source,
                        ids=ids,
                        paper_details_by_source=paper_details_by_source,
                    )
                )
            continue

        if child.source is None:
            continue
        leaf = leaves_by_parent_label_source.get((parent_path, child.label, child.source))
        if leaf is not None:
            nodes.append(build_leaf(leaf, ids, paper_details_by_source))

    return nodes


def build_browser_tree(
    tree_model: TreeModel,
    ids: IdFactory,
    paper_details_by_source: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    branches_by_path = {branch.path: branch for branch in tree_model.branches}
    leaves_by_parent_label_source = {(leaf.path, leaf.label, leaf.source): leaf for leaf in tree_model.leaves}
    root_children = build_branch_children(
        tree_model.root,
        branches_by_path=branches_by_path,
        leaves_by_parent_label_source=leaves_by_parent_label_source,
        ids=ids,
        paper_details_by_source=paper_details_by_source,
    )
    return {
        "id": "tree",
        "label": "Tree",
        "kind": "branch",
        "source": None,
        "url": None,
        "path": ["Tree"],
        "children": root_children,
        "leafCount": sum(node["leafCount"] for node in root_children),
        "branchCount": len([node for node in root_children if node["kind"] == "branch"])
        + sum(node["branchCount"] for node in root_children),
    }
