from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from knowledge_base.tree.model import (
    TreeModel,
    common_prefix_length,
    load_tree_model,
    resolve_metadata_or_generated_source,
    tree_distance,
)


class TreeModelTests(unittest.TestCase):
    def test_tree_model_indexes_placements_without_root_path(self) -> None:
        tree = [
            {
                "Decision-Making": [
                    {
                        "Optimization": [
                            {"Planner": "papers/planner.md"},
                            {"Solver": "papers/solver.md"},
                        ],
                    },
                ],
            },
            {"Robotics": [{"Control": [{"Controller": "papers/controller.md"}]}]},
        ]

        model = TreeModel.from_tree(tree)

        self.assertEqual(
            model.placements_by_paper_id["planner"].category_fields(),
            {
                "super_category": "Decision-Making",
                "category": "Optimization",
                "sub_category": None,
                "nav_path": ["Decision-Making", "Optimization"],
            },
        )
        self.assertEqual(
            model.order.category_order_fields(),
            {
                "superCategories": ["Decision-Making", "Robotics"],
                "categories": ["Optimization", "Control"],
                "categorySuperCategory": {
                    "Optimization": "Decision-Making",
                    "Control": "Robotics",
                },
                "subCategoryOrder": {},
                "navPathOrder": [
                    ["Decision-Making"],
                    ["Decision-Making", "Optimization"],
                    ["Robotics"],
                    ["Robotics", "Control"],
                ],
                "maxBranchDepth": 2,
            },
        )

    def test_transparent_tree_wrapper_is_not_a_branch(self) -> None:
        model = TreeModel.from_tree({"Tree": [{"Theory": [{"Leaf": "papers/leaf.md"}]}]})

        placement = model.placements_by_paper_id["leaf"]
        self.assertEqual(placement.path, ("Theory",))
        self.assertEqual(model.order.super_categories, ("Theory",))

    def test_branch_children_carry_taxonomy_facts_without_landing_pages(self) -> None:
        model = TreeModel.from_tree(
            {
                "Tree": [
                    "tree.md",
                    {
                        "Theory": [
                            {"Direct": "papers/direct.md"},
                            {"Nested": [{"Leaf": "papers/leaf.md"}]},
                        ],
                    },
                ],
            }
        )

        self.assertEqual(
            [leaf.source for leaf in model.leaves],
            ["tree.md", "papers/direct.md", "papers/leaf.md"],
        )
        self.assertEqual([child.label for child in model.root.children], ["Theory"])
        theory = next(branch for branch in model.branches if branch.path == ("Theory",))
        self.assertEqual(theory.branch_count, 1)
        self.assertEqual(theory.leaf_count, 1)
        self.assertEqual(theory.direct_paper_ids, ("direct",))
        self.assertEqual(theory.descendant_paper_ids, ("direct", "leaf"))
        self.assertEqual(
            [(child.label, child.kind, child.paper_ids, child.source) for child in theory.children],
            [
                ("Direct", "leaf", ("direct",), "papers/direct.md"),
                ("Nested", "branch", ("leaf",), None),
            ],
        )

    def test_metadata_source_resolution_keeps_raw_and_generated_sources(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            metadata_root = root / "docs" / "papers"
            metadata_path = metadata_root / "2024" / "tiny-paper" / "metadata.yml"
            metadata_path.parent.mkdir(parents=True)
            metadata_path.write_text("title: Tiny Paper\n", encoding="utf-8")
            source = "docs/papers/2024/tiny-paper/metadata.yml"

            model = TreeModel.from_tree(
                [{"Theory": [{"Tiny": source}]}],
                resolve_source=lambda value: resolve_metadata_or_generated_source(
                    value,
                    base_dir=root,
                    metadata_root=metadata_root,
                ),
            )

        placement = model.placements_by_paper_id["tiny_paper"]
        self.assertEqual(placement.source, source)
        self.assertEqual(placement.generated_source, "papers/tiny_paper.md")
        self.assertEqual(placement.path, ("Theory",))

    def test_load_tree_model_reads_file_with_metadata_source_resolution(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            metadata_root = root / "docs" / "papers"
            metadata_path = metadata_root / "2024" / "tiny-paper" / "metadata.yml"
            metadata_path.parent.mkdir(parents=True)
            metadata_path.write_text("title: Tiny Paper\n", encoding="utf-8")
            tree_path = root / "tree.yml"
            tree_path.write_text(
                "Tree:\n  - Theory:\n      - Tiny: docs/papers/2024/tiny-paper/metadata.yml\n",
                encoding="utf-8",
            )

            model = load_tree_model(tree_path, metadata_root=metadata_root)

        placement = model.placements_by_paper_id["tiny_paper"]
        self.assertEqual(placement.source, "docs/papers/2024/tiny-paper/metadata.yml")
        self.assertEqual(placement.generated_source, "papers/tiny_paper.md")
        self.assertEqual(placement.path, ("Theory",))

    def test_tree_distance_counts_edges_between_branch_paths(self) -> None:
        left = ("Decision-Making", "Optimization", "Solvers")
        right = ("Decision-Making", "Planning")

        self.assertEqual(common_prefix_length(left, right), 1)
        self.assertEqual(tree_distance(left, right), 3)


if __name__ == "__main__":
    unittest.main()
