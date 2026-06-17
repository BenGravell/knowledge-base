"""Canonical in-process Tree model."""

from __future__ import annotations

import re
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Literal

import yaml

from knowledge_base.tree.nav_source import (
    YAML_LOADER,
    metadata_source_path,
    tree_from_config,
    tree_from_file,
)
from knowledge_base.utils.paper_ids import paper_id_from_metadata

UNCATEGORIZED_CATEGORY = "Uncategorized"
TRANSPARENT_ROOT_LABELS = {"Tree"}
LANDING_PAGES = {"tree.md", "tree/index.md"}
GENERATED_PAPER_RE = re.compile(r"^papers/(?P<paper_id>.+)\.md$")


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def clean_label(value: Any) -> str:
    return str(value or "").strip()


def leaf_label_from_source(source: str) -> str:
    return source.removesuffix(".md").replace("-", " ").replace("_", " ").title()


def is_landing_item(label: str, source: str) -> bool:
    return source in LANDING_PAGES or (label.strip().lower() == "overview" and source in LANDING_PAGES)


def generated_paper_id(source: str) -> str | None:
    match = GENERATED_PAPER_RE.match(source.replace("\\", "/").strip())
    return match.group("paper_id") if match else None


@dataclass(frozen=True, slots=True)
class TreeSource:
    paper_id: str
    generated_source: str
    metadata_path: Path | None = None


@dataclass(frozen=True, slots=True)
class TreeLeaf:
    label: str
    source: str
    path: tuple[str, ...]
    nav_path: tuple[str, ...]
    paper_id: str | None = None
    generated_source: str | None = None
    metadata_path: Path | None = None


@dataclass(frozen=True, slots=True)
class TreeChild:
    label: str
    kind: Literal["branch", "leaf"]
    paper_ids: tuple[str, ...] = ()
    source: str | None = None


@dataclass(frozen=True, slots=True)
class TreeBranch:
    path: tuple[str, ...]
    children: tuple[TreeChild, ...]
    direct_paper_ids: tuple[str, ...]
    descendant_paper_ids: tuple[str, ...]

    @property
    def depth(self) -> int:
        return 0 if self.path == ("Tree",) else len(self.path)

    @property
    def branch_count(self) -> int:
        return sum(1 for child in self.children if child.kind == "branch")

    @property
    def leaf_count(self) -> int:
        return sum(1 for child in self.children if child.kind == "leaf")

    def count_for(self, mode: str) -> int:
        if mode == "branches":
            return self.branch_count
        return len(self.children)

    def children_for(self, mode: str) -> tuple[TreeChild, ...]:
        if mode == "branches":
            return tuple(child for child in self.children if child.kind == "branch")
        return self.children


@dataclass(frozen=True, slots=True)
class TreePlacement:
    paper_id: str
    label: str
    source: str
    generated_source: str
    path: tuple[str, ...]
    nav_path: tuple[str, ...]
    metadata_path: Path | None = None

    @property
    def super_category(self) -> str | None:
        return self.path[0] if self.path else None

    @property
    def category(self) -> str:
        if len(self.path) > 1:
            return self.path[1]
        return self.super_category or UNCATEGORIZED_CATEGORY

    @property
    def sub_category(self) -> str | None:
        return self.path[2] if len(self.path) > 2 else None

    def category_fields(self) -> dict[str, Any]:
        return {
            "super_category": self.super_category,
            "category": self.category,
            "sub_category": self.sub_category,
            "nav_path": list(self.path),
        }


@dataclass(frozen=True, slots=True)
class TreeOrder:
    super_categories: tuple[str, ...]
    categories: tuple[str, ...]
    category_super_category: dict[str, str | None]
    sub_category_order: dict[str, list[str]]
    nav_path_order: tuple[tuple[str, ...], ...]

    @property
    def max_branch_depth(self) -> int:
        return max((len(path) for path in self.nav_path_order), default=0)

    def category_order_fields(self) -> dict[str, Any]:
        return {
            "superCategories": list(self.super_categories),
            "categories": list(self.categories),
            "categorySuperCategory": dict(self.category_super_category),
            "subCategoryOrder": {category: list(labels) for category, labels in self.sub_category_order.items()},
            "navPathOrder": [list(path) for path in self.nav_path_order],
            "maxBranchDepth": self.max_branch_depth,
        }


SourceResolver = Callable[[str], TreeSource | None]


def resolve_generated_paper_source(source: str) -> TreeSource | None:
    clean_source = source.replace("\\", "/").strip()
    paper_id = generated_paper_id(clean_source)
    if paper_id is None:
        return None
    return TreeSource(paper_id=paper_id, generated_source=clean_source)


def resolve_metadata_or_generated_source(
    source: str,
    *,
    base_dir: Path,
    metadata_root: Path | None = None,
) -> TreeSource | None:
    clean_source = source.replace("\\", "/").strip()
    generated_id = generated_paper_id(clean_source)
    if generated_id is not None:
        return TreeSource(paper_id=generated_id, generated_source=clean_source)

    metadata_path = metadata_source_path(clean_source, base_dir)
    if metadata_path is None or not metadata_path.exists():
        return None

    root = metadata_root or base_dir / "docs" / "papers"
    with metadata_path.open("r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=YAML_LOADER) or {}
    if not isinstance(data, dict):
        data = {}
    paper_id = paper_id_from_metadata(metadata_path, data, root.resolve())
    return TreeSource(
        paper_id=paper_id,
        generated_source=f"papers/{paper_id}.md",
        metadata_path=metadata_path.resolve(),
    )


def common_prefix_length(a: tuple[str, ...], b: tuple[str, ...]) -> int:
    count = 0
    for left, right in zip(a, b, strict=False):
        if left != right:
            break
        count += 1
    return count


def tree_distance(a: tuple[str, ...], b: tuple[str, ...]) -> int:
    common = common_prefix_length(a, b)
    return (len(a) - common) + (len(b) - common)


def _append_once(items: list[str], value: str) -> None:
    if value and value not in items:
        items.append(value)


def _tree_order(branch_paths: list[tuple[str, ...]]) -> TreeOrder:
    super_categories: list[str] = []
    categories: list[str] = []
    category_super_category: dict[str, str | None] = {}
    sub_category_order: dict[str, list[str]] = {}

    for path in branch_paths:
        if len(path) == 1:
            _append_once(super_categories, path[0])
        elif len(path) == 2:
            _append_once(categories, path[1])
            category_super_category.setdefault(path[1], path[0])
        elif len(path) == 3:
            category = path[1]
            sub_category_order.setdefault(category, [])
            _append_once(sub_category_order[category], path[2])

    return TreeOrder(
        super_categories=tuple(super_categories),
        categories=tuple(categories),
        category_super_category=category_super_category,
        sub_category_order=sub_category_order,
        nav_path_order=tuple(branch_paths),
    )


@dataclass(frozen=True, slots=True)
class TreeModel:
    root: TreeBranch
    leaves: tuple[TreeLeaf, ...]
    branches: tuple[TreeBranch, ...]
    placements_by_paper_id: dict[str, TreePlacement]
    order: TreeOrder

    @classmethod
    def from_tree(
        cls,
        tree: Any,
        *,
        resolve_source: SourceResolver = resolve_generated_paper_source,
    ) -> TreeModel:
        leaves: list[TreeLeaf] = []
        branches: list[TreeBranch] = []
        placements_by_paper_id: dict[str, TreePlacement] = {}
        branch_paths: list[tuple[str, ...]] = []
        seen_branch_paths: set[tuple[str, ...]] = set()

        def add_branch_path(path: tuple[str, ...]) -> None:
            if path and path not in seen_branch_paths:
                seen_branch_paths.add(path)
                branch_paths.append(path)

        def add_leaf(
            label: str,
            source: str,
            path: tuple[str, ...],
        ) -> tuple[TreeChild | None, str | None]:
            clean_source = source.replace("\\", "/").strip()
            resolved = resolve_source(clean_source) if resolve_source else None
            nav_path = (*path, label)
            leaf = TreeLeaf(
                label=label,
                source=clean_source,
                path=path,
                nav_path=nav_path,
                paper_id=resolved.paper_id if resolved else None,
                generated_source=resolved.generated_source if resolved else None,
                metadata_path=resolved.metadata_path if resolved else None,
            )
            leaves.append(leaf)

            if resolved and resolved.paper_id not in placements_by_paper_id:
                placements_by_paper_id[resolved.paper_id] = TreePlacement(
                    paper_id=resolved.paper_id,
                    label=label,
                    source=clean_source,
                    generated_source=resolved.generated_source,
                    path=path,
                    nav_path=nav_path,
                    metadata_path=resolved.metadata_path,
                )
            paper_ids = (resolved.paper_id,) if resolved else ()
            child = None
            if not is_landing_item(label, clean_source):
                child = TreeChild(
                    label=label,
                    kind="leaf",
                    paper_ids=paper_ids,
                    source=clean_source,
                )
            return child, resolved.paper_id if resolved else None

        def walk(items: list[Any], path: tuple[str, ...]) -> TreeBranch:
            add_branch_path(path)
            children: list[TreeChild] = []
            direct_paper_ids: list[str] = []
            descendant_paper_ids: list[str] = []

            for item in items:
                if isinstance(item, str):
                    label = leaf_label_from_source(item)
                    child, paper_id = add_leaf(label, item, path)
                    if child is not None:
                        children.append(child)
                    if paper_id:
                        direct_paper_ids.append(paper_id)
                        descendant_paper_ids.append(paper_id)
                    continue

                if not isinstance(item, dict):
                    continue

                for raw_label, child in item.items():
                    label = clean_label(raw_label)
                    if isinstance(child, list):
                        if label in TRANSPARENT_ROOT_LABELS and not path:
                            transparent = walk(child, path)
                            children.extend(transparent.children)
                            direct_paper_ids.extend(transparent.direct_paper_ids)
                            descendant_paper_ids.extend(transparent.descendant_paper_ids)
                            continue
                        child_path = (*path, label)
                        branch = walk(child, child_path)
                        children.append(
                            TreeChild(
                                label=label,
                                kind="branch",
                                paper_ids=branch.descendant_paper_ids,
                            )
                        )
                        descendant_paper_ids.extend(branch.descendant_paper_ids)
                    elif isinstance(child, str):
                        tree_child, paper_id = add_leaf(label, child, path)
                        if tree_child is not None:
                            children.append(tree_child)
                        if paper_id:
                            direct_paper_ids.append(paper_id)
                            descendant_paper_ids.append(paper_id)

            branch = TreeBranch(
                path=path or ("Tree",),
                children=tuple(children),
                direct_paper_ids=tuple(dict.fromkeys(direct_paper_ids)),
                descendant_paper_ids=tuple(dict.fromkeys(descendant_paper_ids)),
            )
            if path:
                branches.append(branch)
            return branch

        root_items = tree if isinstance(tree, list) else [tree] if isinstance(tree, dict) else []
        root = walk(root_items, ())
        return cls(
            root=root,
            leaves=tuple(leaves),
            branches=tuple(branches),
            placements_by_paper_id=placements_by_paper_id,
            order=_tree_order(branch_paths),
        )

    def placement_fields_by_paper_id(self) -> dict[str, dict[str, Any]]:
        return {paper_id: placement.category_fields() for paper_id, placement in self.placements_by_paper_id.items()}


def load_tree_model(
    tree_path: Path,
    *,
    config: dict[str, Any] | None = None,
    base_dir: Path | None = None,
    metadata_root: Path | None = None,
) -> TreeModel:
    tree_path = Path(tree_path)
    if tree_path.exists():
        tree = tree_from_file(tree_path, normalize=False)
    elif config is not None:
        tree = tree_from_config(config)
    else:
        tree = tree_from_file(tree_path, normalize=False)

    source_base = base_dir or tree_path.parent
    return TreeModel.from_tree(
        tree,
        resolve_source=lambda source: resolve_metadata_or_generated_source(
            source,
            base_dir=source_base,
            metadata_root=metadata_root,
        ),
    )
