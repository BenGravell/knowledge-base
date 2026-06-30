from __future__ import annotations

import unittest

from knowledge_base.scripts.list_unplaced_papers import (
    collect_nav_locations,
    collect_tree_leaves,
)
from knowledge_base.tree.model import TreeModel, TreeSource


class TreeOpsTests(unittest.TestCase):
    def test_unplaced_helpers_use_tree_model_paths_and_raw_sources(self) -> None:
        model = TreeModel.from_tree(
            [{"Area": [{"Tiny Paper": "docs/papers/2024/tiny/metadata.yml"}]}],
            resolve_source=lambda _source: TreeSource(
                paper_id="tiny",
                generated_source="papers/tiny.md",
            ),
        )

        self.assertEqual(
            collect_nav_locations(model),
            {"tiny": ["Area", "Tiny Paper"]},
        )
        leaves = collect_tree_leaves(model)
        self.assertEqual(leaves["tiny"].source, "docs/papers/2024/tiny/metadata.yml")
        self.assertEqual(leaves["tiny"].nav_path, ("Area", "Tiny Paper"))


if __name__ == "__main__":
    unittest.main()
