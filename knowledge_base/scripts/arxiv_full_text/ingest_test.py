from __future__ import annotations

import argparse
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from knowledge_base.catalog import Catalog
from knowledge_base.scripts.arxiv_full_text.docling import inline_latex_inputs
from knowledge_base.scripts.arxiv_full_text.html import arxiv_html_markdown, usable_html
from knowledge_base.scripts.arxiv_full_text.ingest import process_entry
from knowledge_base.scripts.arxiv_full_text.text import (
    embed_text_path,
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


class ArxivFullTextIngestTests(unittest.TestCase):
    def test_html_with_unresolved_section_include_is_unusable(self) -> None:
        html = "<html><body><p>SubSection/Pipeline</p></body></html>"

        self.assertFalse(usable_html(html))

    def test_latex_fallback_inlines_starred_includes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "paper.tex"
            section = Path(tmp) / "SubSection" / "Pipeline.tex"
            section.parent.mkdir()
            root.write_text(r"Before\include*{SubSection/Pipeline}After", encoding="utf-8")
            section.write_text("Complete pipeline section.", encoding="utf-8")

            flattened = inline_latex_inputs(root)

            self.assertEqual(flattened, "BeforeComplete pipeline section.After")

    def test_html_ingest_falls_back_when_source_title_does_not_match_entry(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            metadata_path = Path(tmp) / "docs" / "papers" / "2024" / "2401.00001" / "metadata.yml"
            metadata_path.parent.mkdir(parents=True)
            metadata_path.write_text(VALID_METADATA, encoding="utf-8")
            entry = load_entry(metadata_path)
            args = argparse.Namespace(has_pandoc=True, timeout=10, pandoc_data_dir="", pandoc="pandoc")
            responses = [
                Mock(
                    status_code=200,
                    url="https://arxiv.org/html/2401.00001",
                    text="<html><head><title>Unrelated Template Paper</title></head><body>wrong</body></html>",
                ),
                Mock(
                    status_code=200,
                    url="https://ar5iv.labs.arxiv.org/html/2401.00001",
                    text="<html><head><title>[2401.00001] A Tiny Arxiv Paper</title></head><body>right</body></html>",
                ),
            ]

            with (
                patch("knowledge_base.scripts.arxiv_full_text.html.requests.get", side_effect=responses),
                patch("knowledge_base.scripts.arxiv_full_text.html.pandoc_convert", side_effect=lambda html, _: html),
            ):
                source, markdown, message = arxiv_html_markdown(entry, args)

            self.assertEqual(source, "ar5iv")
            self.assertIn("right", markdown or "")
            self.assertEqual(message, "")

    def test_process_entry_skips_current_sidecar_but_not_stale_marked_sidecar(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            metadata_path = Path(tmp) / "docs" / "papers" / "2024" / "2401.00001" / "metadata.yml"
            metadata_path.parent.mkdir(parents=True)
            metadata_path.write_text(VALID_METADATA, encoding="utf-8")
            entry = load_entry(metadata_path)
            path = embed_text_path(entry)
            args = argparse.Namespace(dry_run=False, force=False, min_chars=20, has_docling=False, has_pandoc=False)
            write_converted_sidecar(
                entry,
                path,
                CONVERTED_MARKDOWN,
                "arxiv-html",
                args,
            )

            self.assertEqual(process_entry(entry, args), f"skip existing {entry.id}")

            metadata_path.write_text(VALID_METADATA.replace("2401.00001", "2401.00002"), encoding="utf-8")
            stale_entry = load_entry(metadata_path)
            with patch("knowledge_base.scripts.arxiv_full_text.ingest.try_arxiv_html", return_value="wrote updated"):
                self.assertEqual(process_entry(stale_entry, args), "wrote updated")


if __name__ == "__main__":
    unittest.main()
