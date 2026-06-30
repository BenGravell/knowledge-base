from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from knowledge_base.scripts.list_tree_algorithm_label_matches import collect_matches
from knowledge_base.tree.model import TreeModel, TreeSource


class ListTreeAlgorithmLabelMatchesTests(unittest.TestCase):
    def test_algorithm_label_matcher_uses_tree_model_metadata_paths(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            metadata_path = Path(tmp) / "metadata.yml"
            metadata_path.write_text(
                "title: Tiny Paper\nalgorithm: Exact Algorithm\n",
                encoding="utf-8",
            )
            model = TreeModel.from_tree(
                [
                    "tree/index.md",
                    {"Area": [{"Exact Algorithm": "docs/papers/2024/tiny/metadata.yml"}]},
                ],
                resolve_source=lambda source: (
                    TreeSource(
                        paper_id="tiny",
                        generated_source="papers/tiny.md",
                        metadata_path=metadata_path,
                    )
                    if source.startswith("docs/papers/")
                    else None
                ),
            )

            matches = collect_matches(model)

        self.assertEqual(len(matches), 1)
        self.assertEqual(matches[0].tree_path, ("Tree", "Area", "Exact Algorithm"))
        self.assertEqual(matches[0].metadata_path, metadata_path)


if __name__ == "__main__":
    unittest.main()
