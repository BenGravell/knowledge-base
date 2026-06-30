from __future__ import annotations

import json
import math
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from typing import cast

from knowledge_base.catalog import Entry
from knowledge_base.embedding_workbench import (
    EmbeddingRow,
    embedding_rows_for_entry,
    fastembed_effective_device,
    load_embedding_table,
    refresh_embedding_cache,
)


class EmbeddingWorkbenchTests(unittest.TestCase):
    def test_fastembed_auto_device_uses_available_cuda_provider(self) -> None:
        self.assertEqual(fastembed_effective_device("auto", ["CPUExecutionProvider"]), "cpu")
        self.assertEqual(
            fastembed_effective_device("auto", ["CUDAExecutionProvider", "CPUExecutionProvider"]),
            "cuda",
        )

    def test_fastembed_cuda_device_requires_cuda_provider(self) -> None:
        with self.assertRaises(SystemExit):
            fastembed_effective_device("cuda", ["CPUExecutionProvider"])

    def test_embedding_rows_for_entry_projects_chunks(self) -> None:
        entry = SimpleNamespace(
            id="paper",
            embedding_chunks=[
                SimpleNamespace(id="metadata", text="Metadata text", weight=3.0),
                SimpleNamespace(id="body", text="Body text", weight=1.0),
            ],
        )

        rows = embedding_rows_for_entry(cast(Entry, entry))

        self.assertEqual(
            rows,
            [
                EmbeddingRow("paper:metadata", "Metadata text", "1f17db27375c8a49", paper_id="paper", weight=3.0),
                EmbeddingRow("paper:body", "Body text", "751f5ed0ea11344a", paper_id="paper", weight=1.0),
            ],
        )

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
            vectors_saved = (cache_path.parent / saved["vectors"]).exists()

        self.assertEqual(embedded_texts, [["Changed text", "Fresh text"]])
        self.assertEqual(result.pruned_ids, ("stale",))
        self.assertEqual(result.changed_count, 2)
        self.assertEqual(result.matrix.tolist(), [[1.0, 2.0], [3.0, 4.0]])
        self.assertEqual(set(saved["papers"]), {"changed", "fresh"})
        self.assertEqual(saved["format"], "embedding-workbench-v2")
        self.assertEqual(saved["vectors"], "embedding_cache.vectors.npy")
        self.assertTrue(vectors_saved)
        self.assertEqual(saved["papers"]["changed"]["row"], 0)
        self.assertNotIn("embedding", saved["papers"]["changed"])
        self.assertNotIn("umap", saved)
        self.assertNotIn("force", saved)

    def test_load_embedding_table_reads_binary_cache(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            cache_path = Path(tmp) / "embedding_cache.json"

            result = refresh_embedding_cache(
                [
                    EmbeddingRow("left", "Left text", "h1"),
                    EmbeddingRow("right", "Right text", "h2"),
                ],
                cache_path=cache_path,
                model="model-a",
                embed_texts=lambda _texts: [[1.0, 0.0], [0.0, 1.0]],
            )
            table = load_embedding_table(cache_path, mmap_mode="r")

        self.assertEqual(result.matrix.tolist(), [[1.0, 0.0], [0.0, 1.0]])
        self.assertEqual(table.model, "model-a")
        self.assertEqual(table.ids, ("left", "right"))
        self.assertEqual(table.matrix.tolist(), [[1.0, 0.0], [0.0, 1.0]])
        self.assertEqual(table.by_id()["right"].tolist(), [0.0, 1.0])

    def test_binary_cache_embeds_only_new_rows(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            cache_path = Path(tmp) / "embedding_cache.json"
            refresh_embedding_cache(
                [
                    EmbeddingRow("left", "Left text", "h1"),
                    EmbeddingRow("right", "Right text", "h2"),
                ],
                cache_path=cache_path,
                model="model-a",
                embed_texts=lambda _texts: [[1.0, 0.0], [0.0, 1.0]],
            )
            embedded_texts: list[list[str]] = []

            def embed(texts: list[str]) -> list[list[float]]:
                embedded_texts.append(texts)
                return [[0.5, 0.5]]

            result = refresh_embedding_cache(
                [
                    EmbeddingRow("left", "Left text", "h1"),
                    EmbeddingRow("middle", "Middle text", "h3"),
                    EmbeddingRow("right", "Right text", "h2"),
                ],
                cache_path=cache_path,
                model="model-a",
                embed_texts=embed,
            )
            table = load_embedding_table(cache_path)

        self.assertEqual(embedded_texts, [["Middle text"]])
        self.assertEqual(result.changed_count, 1)
        self.assertEqual(result.matrix.tolist(), [[1.0, 0.0], [0.5, 0.5], [0.0, 1.0]])
        self.assertEqual(table.ids, ("left", "middle", "right"))
        self.assertEqual(table.matrix.tolist(), [[1.0, 0.0], [0.5, 0.5], [0.0, 1.0]])

    def test_chunk_rows_aggregate_to_paper_vectors(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            cache_path = Path(tmp) / "embedding_cache.json"
            rows = [
                EmbeddingRow("paper:metadata", "Metadata text", "hm", paper_id="paper", weight=3.0),
                EmbeddingRow("paper:body", "Body text", "hb", paper_id="paper", weight=1.0),
                EmbeddingRow("other:metadata", "Other text", "ho", paper_id="other", weight=1.0),
            ]

            result = refresh_embedding_cache(
                rows,
                cache_path=cache_path,
                model="model-a",
                embed_texts=lambda _texts: [[1.0, 0.0], [0.0, 1.0], [0.0, 1.0]],
            )
            table = load_embedding_table(cache_path)
            raw_table = load_embedding_table(cache_path, aggregate=False)
            saved = json.loads(cache_path.read_text(encoding="utf-8"))

        self.assertEqual(result.matrix.shape, (2, 2))
        self.assertAlmostEqual(float(result.matrix[0, 0]), 3 / math.sqrt(10), places=6)
        self.assertAlmostEqual(float(result.matrix[0, 1]), 1 / math.sqrt(10), places=6)
        self.assertEqual(table.ids, ("paper", "other"))
        self.assertEqual(raw_table.ids, ("paper:metadata", "paper:body", "other:metadata"))
        self.assertEqual(saved["papers"]["paper:metadata"]["paper_id"], "paper")
        self.assertEqual(saved["papers"]["paper:metadata"]["weight"], 3.0)


if __name__ == "__main__":
    unittest.main()
