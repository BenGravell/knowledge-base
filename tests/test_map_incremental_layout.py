from __future__ import annotations

import unittest

import numpy as np

from knowledge_base.components.map.generate_map_data import (
    added_only_cache_hit,
    incremental_neighbor_positions,
)
from knowledge_base.embedding_workbench import fastembed_effective_device


class MapIncrementalLayoutTests(unittest.TestCase):
    def test_fastembed_auto_device_uses_available_cuda_provider(self) -> None:
        self.assertEqual(fastembed_effective_device("auto", ["CPUExecutionProvider"]), "cpu")
        self.assertEqual(
            fastembed_effective_device("auto", ["CUDAExecutionProvider", "CPUExecutionProvider"]),
            "cuda",
        )

    def test_fastembed_cuda_device_requires_cuda_provider(self) -> None:
        with self.assertRaises(SystemExit):
            fastembed_effective_device("cuda", ["CPUExecutionProvider"])

    def test_added_only_cache_hit_accepts_single_new_paper(self) -> None:
        entry = {
            "ids": ["a", "b"],
            "hashes": {"a": "ha", "b": "hb"},
        }
        papers = [
            {"id": "a", "hash": "ha"},
            {"id": "new", "hash": "hn"},
            {"id": "b", "hash": "hb"},
        ]

        self.assertEqual(added_only_cache_hit(entry, papers), (["a", "b"], ["new"]))

    def test_incremental_positions_keep_old_coords_and_place_new_row(self) -> None:
        coords = incremental_neighbor_positions(
            current_ids=["a", "new", "b"],
            embeddings=np.array(
                [
                    [1.0, 0.0],
                    [0.9, 0.1],
                    [0.0, 1.0],
                ],
                dtype=np.float32,
            ),
            previous_ids=["a", "b"],
            previous_coords=np.array(
                [
                    [10.0, 0.0],
                    [0.0, 10.0],
                ],
                dtype=np.float64,
            ),
        )

        self.assertEqual(coords.shape, (3, 2))
        self.assertEqual(coords[0].tolist(), [10.0, 0.0])
        self.assertEqual(coords[2].tolist(), [0.0, 10.0])
        self.assertTrue(np.all(np.isfinite(coords[1])))


if __name__ == "__main__":
    unittest.main()
