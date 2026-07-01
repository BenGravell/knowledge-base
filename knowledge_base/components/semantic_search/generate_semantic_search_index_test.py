from __future__ import annotations

import json
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path

from knowledge_base.components.semantic_search.generate_semantic_search_index import (
    embedding_cache_matches_rows,
    semantic_asset_key,
    semantic_assets_current,
)
from knowledge_base.embeddings.workbench import EmbeddingRow


class SemanticSearchIndexCacheTests(unittest.TestCase):
    def test_asset_key_changes_when_row_hash_changes(self) -> None:
        papers = [{"id": "p1", "title": "Title", "hash": "paper-hash"}]
        key = semantic_asset_key(
            papers,
            [EmbeddingRow(id="p1:0", text="", content_hash="old", paper_id="p1")],
            model="model",
            browser_model="browser",
        )

        changed = semantic_asset_key(
            papers,
            [EmbeddingRow(id="p1:0", text="", content_hash="new", paper_id="p1")],
            model="model",
            browser_model="browser",
        )

        self.assertNotEqual(key, changed)

    def test_assets_current_requires_matching_manifest_key_and_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            manifest = root / "semantic-search-index.json"
            settings = root / "semantic-search-settings.json"
            vectors = root / "semantic-search-vectors.i8"
            settings.write_text("{}", encoding="utf-8")
            vectors.write_bytes(b"vectors")
            manifest.write_text(json.dumps({"assetKey": "key", "sourceFingerprint": "source"}), encoding="utf-8")

            args = Namespace(manifest=manifest, settings=settings, vectors=vectors)

            self.assertTrue(semantic_assets_current(args, asset_key="key"))
            self.assertTrue(semantic_assets_current(args, source_key="source"))
            self.assertFalse(semantic_assets_current(args, asset_key="other"))
            self.assertFalse(semantic_assets_current(args, source_key="other"))

    def test_embedding_cache_matches_rows_without_loading_vectors(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            cache = root / "embedding_cache.json"
            (root / "embedding_cache.vectors.npy").write_bytes(b"exists")
            cache.write_text(
                json.dumps(
                    {
                        "model": "model",
                        "vectors": "embedding_cache.vectors.npy",
                        "papers": {
                            "p1:0": {"hash": "hash", "row": 0},
                        },
                    }
                ),
                encoding="utf-8",
            )

            rows = [EmbeddingRow(id="p1:0", text="", content_hash="hash", paper_id="p1")]

            self.assertTrue(embedding_cache_matches_rows(cache, rows, "model"))
            self.assertFalse(embedding_cache_matches_rows(cache, rows, "other"))


if __name__ == "__main__":
    unittest.main()
