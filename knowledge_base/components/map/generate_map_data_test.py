from __future__ import annotations

import unittest

import numpy as np

from knowledge_base.components.map.pipeline.layouts import (
    added_only_cache_hit,
    incremental_neighbor_positions,
)


class MapDataIncrementalLayoutTests(unittest.TestCase):
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
