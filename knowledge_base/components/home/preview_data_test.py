from __future__ import annotations

import copy
import unittest
from typing import Any

from knowledge_base.components.home.preview_data import build_home_search_data, build_home_tree_data
from knowledge_base.publishing.generated_assets import (
    EXPLORER_APP_SCRIPTS,
    HOME_APP_SCRIPTS,
    SEARCH_APP_SCRIPTS,
    SEARCH_DATA,
    TREE_DATA,
)


class HomePreviewDataTests(unittest.TestCase):
    def test_tree_samples_each_branch_and_preserves_real_paths_without_mutating_source(self):
        def leaf(index: int) -> dict[str, Any]:
            return {
                "id": f"paper-{index}",
                "label": f"Paper {index}",
                "kind": "paper",
                "children": [],
                "paper": {"id": str(index), "abstract": "large abstract" * 1000},
            }

        tree = {
            "root": {
                "id": "tree",
                "label": "Tree",
                "kind": "branch",
                "children": [
                    {
                        "id": "large",
                        "label": "Large",
                        "kind": "branch",
                        "children": [
                            {
                                "id": f"branch-{i}",
                                "label": f"Branch {i}",
                                "kind": "branch",
                                "children": [leaf(i * 5 + j) for j in range(5)],
                            }
                            for i in range(4)
                        ],
                    },
                    {"id": "small", "label": "Small", "kind": "branch", "children": [leaf(20), leaf(21)]},
                ],
            }
        }
        original = copy.deepcopy(tree)
        preview = build_home_tree_data(tree)
        self.assertEqual(tree, original)
        self.assertEqual(preview["meta"]["totalLeaves"], 14)
        self.assertEqual([n["id"] for n in preview["root"]["children"]], ["large", "small"])
        self.assertEqual([n["leafCount"] for n in preview["root"]["children"]], [12, 2])

        def check_subset(node: dict[str, Any], source: dict[str, Any]) -> None:
            self.assertEqual(node["id"], source["id"])
            self.assertEqual(node["label"], source["label"])
            self.assertNotIn("abstract", node.get("paper", {}))
            source_children = {n["id"]: n for n in source["children"]}
            for child in node["children"]:
                check_subset(child, source_children[child["id"]])
            self.assertEqual(
                node["leafCount"], sum(n["leafCount"] for n in node["children"]) if node["children"] else 1
            )

        check_subset(preview["root"], tree["root"])

    def test_search_contains_only_two_real_recent_matching_records(self):
        records = [{"id": str(i), "title": "Motion Planning", "year": 2020 + i} for i in range(20)]
        records.append({"id": "unrelated", "title": "Control", "year": 2050})
        original = copy.deepcopy(records)
        preview = build_home_search_data(records)
        self.assertEqual(preview["previewQuery"], "planning")
        self.assertEqual(list(preview["papers"]), ["19", "18"])
        self.assertTrue(all(paper in records for paper in preview["papers"].values()))
        self.assertEqual(records, original)
        self.assertNotIn("related", preview)

    def test_small_empty_and_nonmatching_corpora(self):
        self.assertEqual(
            build_home_tree_data({"root": {"id": "tree", "label": "Tree", "kind": "branch", "children": []}})["meta"][
                "totalLeaves"
            ],
            0,
        )
        self.assertEqual(build_home_search_data([])["papers"], {})
        records = [{"id": "one", "title": "Control", "year": ""}]
        self.assertEqual(build_home_search_data(records), {"papers": {"one": records[0]}, "previewQuery": ""})

    def test_only_home_excludes_full_corpus_assets(self):
        self.assertNotIn(TREE_DATA, HOME_APP_SCRIPTS.assets)
        self.assertNotIn(SEARCH_DATA, HOME_APP_SCRIPTS.assets)
        self.assertIn(TREE_DATA, EXPLORER_APP_SCRIPTS.assets)
        self.assertIn(SEARCH_DATA, SEARCH_APP_SCRIPTS.assets)


if __name__ == "__main__":
    unittest.main()
