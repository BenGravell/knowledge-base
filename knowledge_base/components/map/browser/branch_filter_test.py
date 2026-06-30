from __future__ import annotations

import unittest
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from knowledge_base.publishing.generated_assets import MAP_DATA

REPO_ROOT = Path(__file__).resolve().parents[4]
MAP_DATA_PATH = REPO_ROOT / "knowledge_base" / "components" / "map" / "generated" / "map-data.js"
QUADRATIC_PROGRAMMING_PATH = (
    "Decision-making",
    "Optimization",
    "Continuous Optimization",
    "Convex Optimization",
    "Quadratic Programming",
)


@dataclass
class BranchGroup:
    path: tuple[str, ...]
    is_category_leaf: bool
    children: dict[tuple[str, ...], BranchGroup] = field(default_factory=dict)
    leaf_ids: list[str] = field(default_factory=list)


def load_map_data() -> dict[str, Any]:
    return MAP_DATA.loads_js_assignment(MAP_DATA_PATH.read_text(encoding="utf-8"))


def paper_nav_path(attrs: dict[str, Any]) -> tuple[str, ...]:
    path = attrs.get("nav_path")
    if not isinstance(path, list):
        path = [attrs.get("super_category"), attrs.get("category"), attrs.get("sub_category")]
    return tuple(str(part).strip() for part in path if str(part or "").strip())


def map_branch_tree(map_data: dict[str, Any]) -> BranchGroup:
    nodes = map_data.get("nodes")
    if not isinstance(nodes, list):
        raise AssertionError("map-data.js must contain nodes")

    paths = [paper_nav_path(node["data"]) for node in nodes]
    branch_depth = max(4, int((map_data.get("meta") or {}).get("maxBranchDepth") or 0), *(len(path) for path in paths))
    root = BranchGroup(path=(), is_category_leaf=False)

    for node, path in zip(nodes, paths, strict=True):
        attrs = node["data"]
        padded = list(path)
        padded.extend([path[-1]] * (branch_depth - len(path)))
        parent = root
        for index, _label in enumerate(padded[:branch_depth]):
            prefix = tuple(padded[: index + 1])
            child = parent.children.setdefault(
                prefix,
                BranchGroup(path=prefix, is_category_leaf=index >= len(path)),
            )
            child.leaf_ids.append(str(attrs["id"]))
            parent = child

    return root


def find_branch(root: BranchGroup, path: tuple[str, ...]) -> BranchGroup:
    stack = list(root.children.values())
    while stack:
        group = stack.pop()
        if group.path == path:
            return group
        stack.extend(group.children.values())
    raise AssertionError(f"branch not found: {' / '.join(path)}")


def visible_branch_children(group: BranchGroup) -> list[BranchGroup]:
    return [child for child in group.children.values() if not child.is_category_leaf]


def navigator_child_row_ids(group: BranchGroup) -> list[str]:
    branch_children = visible_branch_children(group)
    if branch_children:
        return ["branch:" + " / ".join(child.path) for child in branch_children]
    return [f"paper:{paper_id}" for paper_id in group.leaf_ids]


class MapBranchNavigatorTests(unittest.TestCase):
    def test_leaf_branch_children_fall_back_to_direct_paper_rows(self) -> None:
        root = map_branch_tree(load_map_data())

        branch = find_branch(root, QUADRATIC_PROGRAMMING_PATH)

        self.assertFalse(branch.is_category_leaf)
        self.assertTrue(branch.children, "fixture must exercise hidden padded branch children")
        self.assertEqual(visible_branch_children(branch), [])
        self.assertEqual(
            set(navigator_child_row_ids(branch)),
            {
                "paper:1956_frank_an_algorithm_for_quadratic",
                "paper:1703_07870",
                "paper:2506_11513",
            },
        )


if __name__ == "__main__":
    unittest.main()
