from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from knowledge_base.catalog import (
    Catalog,
    CatalogLoadError,
    build_embedding_text,
    identifier_terms,
    paper_label,
    year_as_int,
)

VALID_METADATA = """\
title: A Tiny Paper
authors:
  - Ada Lovelace
  - Grace Hopper
year: "2024"
abstract: A compact abstract.
type: Conference Paper
audit_status: raw
arxiv_id: arXiv:cond-mat/0112110v2
doi: https://doi.org/10.1000/example
tags:
  - planning
summary: A compact summary.
link: https://arxiv.org/pdf/cond-mat/0112110v2
links_alt:
  - https://example.com/paper
"""


class CatalogTests(unittest.TestCase):
    def test_catalog_loads_metadata_into_searchable_entry(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            metadata_root = Path(tmp) / "docs" / "papers"
            metadata_path = metadata_root / "2024" / "cond-mat" / "0112110" / "metadata.yml"
            metadata_path.parent.mkdir(parents=True)
            metadata_path.write_text(VALID_METADATA, encoding="utf-8")

            catalog = Catalog.from_metadata_root(metadata_root)

        entry = catalog.entries[0]
        self.assertEqual(entry.id, "cond_mat_0112110")
        self.assertEqual(entry.generated_source, "papers/cond_mat_0112110.md")
        self.assertEqual(entry.author_last_names, ("Lovelace", "Hopper"))
        self.assertEqual(entry.year_value, 2024)
        self.assertEqual(entry.doi, "10.1000/example")
        self.assertEqual(entry.arxiv_id, "cond-mat/0112110")
        self.assertEqual(entry.label, "Lovelace et al. 2024")
        self.assertEqual(entry.url("map", ""), "map/#paper=cond_mat_0112110")
        self.assertIn("arXiv:cond-mat/0112110", entry.identifiers)

    def test_catalog_reports_validation_errors_with_metadata_path(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            metadata_root = Path(tmp) / "docs" / "papers"
            metadata_path = metadata_root / "2024" / "bad" / "metadata.yml"
            metadata_path.parent.mkdir(parents=True)
            metadata_path.write_text(
                VALID_METADATA.replace("type: Conference Paper", "type: Podcast"),
                encoding="utf-8",
            )

            with self.assertRaises(CatalogLoadError) as raised:
                Catalog.from_metadata_root(metadata_root)

        self.assertEqual(len(raised.exception.issues), 1)
        issue = raised.exception.issues[0]
        self.assertEqual(issue.metadata_path, metadata_path)
        self.assertIn("must be one of", issue.message)


class CatalogHelperTests(unittest.TestCase):
    def test_paper_label_prefers_algorithm_then_author_year_then_title(self) -> None:
        self.assertEqual(
            paper_label(
                title="Fallback Title",
                algorithm="Planner",
                authors=("Ada Lovelace",),
                year=2024,
            ),
            "Planner",
        )
        self.assertEqual(
            paper_label(
                title="Fallback Title",
                algorithm="",
                authors=("Ada Lovelace", "Grace Hopper"),
                year="2024",
            ),
            "Lovelace et al. 2024",
        )
        self.assertEqual(
            paper_label(title="Fallback Title", algorithm="", authors=(), year=""),
            "Fallback Title",
        )

    def test_year_as_int_accepts_only_reasonable_years(self) -> None:
        self.assertEqual(year_as_int("accepted in 2024"), 2024)
        self.assertIsNone(year_as_int("no year here"))
        self.assertIsNone(year_as_int(1499))

    def test_identifier_terms_adds_common_forms_without_duplicates(self) -> None:
        terms = identifier_terms(
            "paper-id",
            doi="10.1000/example",
            arxiv_id="2501.00001",
            primary_link="https://doi.org/10.1000/example",
            alternate_links=("https://doi.org/10.1000/example", "https://example.com/paper"),
        )

        self.assertEqual(terms.count("https://doi.org/10.1000/example"), 1)
        self.assertIn("DOI:10.1000/example", terms)
        self.assertIn("https://arxiv.org/pdf/2501.00001", terms)
        self.assertIn("https://example.com/paper", terms)

    def test_embedding_text_skips_blank_sections(self) -> None:
        self.assertEqual(
            build_embedding_text(title="", tags=(), summary="", abstract="Only abstract."),
            "Abstract: Only abstract.",
        )


if __name__ == "__main__":
    unittest.main()
