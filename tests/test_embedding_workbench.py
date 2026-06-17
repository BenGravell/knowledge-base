from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from knowledge_base.embedding_workbench import EmbeddingRow, refresh_embedding_cache


class EmbeddingWorkbenchTests(unittest.TestCase):
    def test_cache_hit_returns_ordered_matrix_without_model_call(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            cache_path = Path(tmp) / "embedding_cache.json"
            cache_path.write_text(
                json.dumps(
                    {
                        "model": "model-a",
                        "papers": {
                            "left": {"hash": "h1", "embedding": [1.0, 0.0]},
                            "right": {"hash": "h2", "embedding": [0.0, 1.0]},
                        },
                    }
                ),
                encoding="utf-8",
            )

            def fail_embed(_texts: list[str]) -> list[list[float]]:
                raise AssertionError("cache hit should not call the embedder")

            result = refresh_embedding_cache(
                [
                    EmbeddingRow("right", "Right text", "h2"),
                    EmbeddingRow("left", "Left text", "h1"),
                ],
                cache_path=cache_path,
                model="model-a",
                embed_texts=fail_embed,
            )

        self.assertEqual(result.changed_count, 0)
        self.assertEqual(result.matrix.tolist(), [[0.0, 1.0], [1.0, 0.0]])

    def test_refresh_prunes_stale_rows_and_invalidates_derived_cache(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            cache_path = Path(tmp) / "embedding_cache.json"
            cache_path.write_text(
                json.dumps(
                    {
                        "model": "model-a",
                        "papers": {
                            "stale": {"hash": "gone", "embedding": [9.0, 9.0]},
                            "changed": {"hash": "old", "embedding": [8.0, 8.0]},
                        },
                        "umap": {"key": "old"},
                        "force": {"key": "old"},
                    }
                ),
                encoding="utf-8",
            )
            embedded_texts: list[list[str]] = []

            def embed(texts: list[str]) -> list[list[float]]:
                embedded_texts.append(texts)
                return [[1.0, 2.0], [3.0, 4.0]]

            result = refresh_embedding_cache(
                [
                    EmbeddingRow("changed", "Changed text", "new"),
                    EmbeddingRow("fresh", "Fresh text", "fresh"),
                ],
                cache_path=cache_path,
                model="model-a",
                embed_texts=embed,
                invalidate_keys=("umap", "force"),
            )
            saved = json.loads(cache_path.read_text(encoding="utf-8"))

        self.assertEqual(embedded_texts, [["Changed text", "Fresh text"]])
        self.assertEqual(result.pruned_ids, ("stale",))
        self.assertEqual(result.changed_count, 2)
        self.assertEqual(result.matrix.tolist(), [[1.0, 2.0], [3.0, 4.0]])
        self.assertEqual(set(saved["papers"]), {"changed", "fresh"})
        self.assertNotIn("umap", saved)
        self.assertNotIn("force", saved)


if __name__ == "__main__":
    unittest.main()
