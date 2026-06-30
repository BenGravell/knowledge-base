from __future__ import annotations

import argparse
import tempfile
import unittest
from pathlib import Path

from knowledge_base.catalog import Catalog
from knowledge_base.scripts.arxiv_full_text.text import (
    embed_text_path,
    parsed_sidecar_provenance,
    sidecar_current_for_entry,
    write_converted_sidecar,
)

VALID_METADATA = """\
title: A Tiny Arxiv Paper
authors:
  - Ada Lovelace
year: "2024"
abstract: A compact abstract.
type: Conference Paper
audit_status: raw
arxiv_id: "2401.00001"
tags:
  - planning
summary: A compact summary.
link: https://arxiv.org/abs/2401.00001
"""


def load_entry(metadata_path: Path):
    return Catalog.from_metadata_root(metadata_path.parents[2]).entries[0]


CONVERTED_MARKDOWN = "## Introduction\n\n" + " ".join(
    "This paper presents useful arxiv source text for embedding cache validation with enough "
    "body prose to look like a real converted paper section."
    for _ in range(8)
)


class ArxivFullTextTests(unittest.TestCase):
    def test_generated_embed_text_sidecar_records_arxiv_id_provenance(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            metadata_path = Path(tmp) / "docs" / "papers" / "2024" / "2401.00001" / "metadata.yml"
            metadata_path.parent.mkdir(parents=True)
            metadata_path.write_text(VALID_METADATA, encoding="utf-8")
            entry = load_entry(metadata_path)
            path = embed_text_path(entry)
            args = argparse.Namespace(dry_run=False, min_chars=20)

            write_converted_sidecar(
                entry,
                path,
                CONVERTED_MARKDOWN,
                "arxiv-html",
                args,
            )
            text = path.read_text(encoding="utf-8")
            provenance = parsed_sidecar_provenance(text)

            assert provenance is not None
            self.assertEqual(provenance["arxiv_id"], "2401.00001")
            self.assertEqual(provenance["source"], "arxiv-html")
            self.assertTrue(sidecar_current_for_entry(entry, path))

            metadata_path.write_text(VALID_METADATA.replace("2401.00001", "2401.00002"), encoding="utf-8")
            stale_entry = load_entry(metadata_path)

            self.assertFalse(sidecar_current_for_entry(stale_entry, path))


if __name__ == "__main__":
    unittest.main()
