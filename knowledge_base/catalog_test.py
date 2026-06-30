from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from knowledge_base.catalog import (
    Catalog,
    CatalogLoadError,
    build_embedding_chunks,
    build_embedding_text,
    chunk_embedding_text,
    clean_embedding_sidecar_text,
    compact_embedding_content,
    embedding_input_sidecar_path,
    embedding_input_sidecar_text,
    embedding_token_count,
    identifier_terms,
    paper_label,
    truncate_embedding_text,
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

    def test_catalog_compacts_sidecar_text_for_embedding(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            metadata_root = Path(tmp) / "docs" / "papers"
            metadata_path = metadata_root / "2024" / "2501.00001" / "metadata.yml"
            metadata_path.parent.mkdir(parents=True)
            metadata_path.write_text(VALID_METADATA, encoding="utf-8")
            metadata_path.with_name("embed_text.md").write_text(
                "## Introduction\n\n"
                "Opening contribution paragraph explains policy optimization and reusable reinforcement learning ideas.\n\n"
                "Summary: Source label should keep useful semantic words without the prefix.\n\n"
                "Citation cleanup keeps useful model context while dropping noisy links "
                "(Heaven, (https://arxiv.org/html/2501.00001#bib.bib1)).\n\n"
                "1234567890 2345678901 3456789012 4567890123 table row 9999999999 8888888888\n\n"
                + "\n\n".join(
                    f"Body paragraph {index} discusses compact semantic excerpts for robust embedding search "
                    f"without letting one full paper overwhelm the model input window."
                    for index in range(40)
                )
                + "\n\nClosing implication paragraph connects the method to map search and paper discovery.\n\n"
                "## References\n\n"
                "[1] Ada Example. Reference noise that should not enter embeddings. 2024.",
                encoding="utf-8",
            )

            entry = Catalog.from_metadata_root(metadata_root, write_embedding_input_sidecars=True).entries[0]
            raw_input_sidecar_text = embedding_input_sidecar_path(metadata_path).read_text(encoding="utf-8")
            parsed_input_sidecar_text = embedding_input_sidecar_text(metadata_path)

        self.assertIn("Opening contribution paragraph", entry.embedding_text)
        self.assertTrue(any(chunk.section == "Introduction" for chunk in entry.embedding_chunks))
        self.assertIn("Source label should keep useful semantic words", entry.embedding_text)
        self.assertIn("Closing implication paragraph", entry.embedding_text)
        self.assertNotIn("Title:", entry.embedding_text)
        self.assertNotIn("Summary:", entry.embedding_text)
        self.assertNotIn("Abstract:", entry.embedding_text)
        self.assertNotIn("Content:", entry.embedding_text)
        self.assertNotIn("1234567890", entry.embedding_text)
        self.assertNotIn("Reference noise", entry.embedding_text)
        self.assertNotIn("https://", entry.embedding_text)
        self.assertIn("<!-- embedding-input:v1 -->", raw_input_sidecar_text)
        self.assertEqual(parsed_input_sidecar_text, entry.embedding_text)

    def test_catalog_prefers_checked_in_embedding_input_sidecar(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            metadata_root = Path(tmp) / "docs" / "papers"
            metadata_path = metadata_root / "2024" / "2501.00001" / "metadata.yml"
            metadata_path.parent.mkdir(parents=True)
            metadata_path.write_text(VALID_METADATA, encoding="utf-8")
            metadata_path.with_name("embed_text.md").write_text(
                "## Introduction\n\nLong source text should not be compacted when cache exists.",
                encoding="utf-8",
            )
            embedding_input_sidecar_path(metadata_path).write_text(
                "Cached exact model input for human inspection.\n",
                encoding="utf-8",
            )

            entry = Catalog.from_metadata_root(metadata_root, write_embedding_input_sidecars=True).entries[0]
            input_sidecar_text = embedding_input_sidecar_path(metadata_path).read_text(encoding="utf-8")
            refreshed_entry = Catalog.from_metadata_root(
                metadata_root,
                refresh_embedding_input_sidecars=True,
            ).entries[0]
            refreshed_sidecar_text = embedding_input_sidecar_path(metadata_path).read_text(encoding="utf-8")
            parsed_refreshed_sidecar_text = embedding_input_sidecar_text(metadata_path)

        self.assertEqual(entry.embedding_text, "Cached exact model input for human inspection.")
        self.assertEqual(input_sidecar_text, "Cached exact model input for human inspection.\n")
        self.assertNotIn("Long source text", entry.embedding_text)
        self.assertIn("Long source text", refreshed_entry.embedding_text)
        self.assertIn("<!-- embedding-input:v1 -->", refreshed_sidecar_text)
        self.assertEqual(parsed_refreshed_sidecar_text, refreshed_entry.embedding_text)

    def test_generated_embedding_input_sidecar_refreshes_when_embed_text_changes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            metadata_root = Path(tmp) / "docs" / "papers"
            metadata_path = metadata_root / "2024" / "2501.00001" / "metadata.yml"
            metadata_path.parent.mkdir(parents=True)
            metadata_path.write_text(VALID_METADATA, encoding="utf-8")
            metadata_path.with_name("embed_text.md").write_text(
                "## Introduction\n\n"
                "In this paper, we propose initial policy optimization cache text that should be replaced "
                "after the upstream embedding text sidecar changes.",
                encoding="utf-8",
            )

            initial_entry = Catalog.from_metadata_root(metadata_root, write_embedding_input_sidecars=True).entries[0]
            initial_sidecar_text = embedding_input_sidecar_path(metadata_path).read_text(encoding="utf-8")
            metadata_path.with_name("embed_text.md").write_text(
                "## Introduction\n\n"
                "In this paper, we propose updated policy optimization cache text that should invalidate "
                "the generated embedding input sidecar for this paper.",
                encoding="utf-8",
            )
            refreshed_entry = Catalog.from_metadata_root(metadata_root, write_embedding_input_sidecars=True).entries[0]
            refreshed_sidecar_text = embedding_input_sidecar_path(metadata_path).read_text(encoding="utf-8")

        self.assertIn("initial policy optimization cache text", initial_entry.embedding_text)
        self.assertIn("initial policy optimization cache text", initial_sidecar_text)
        self.assertIn("updated policy optimization cache text", refreshed_entry.embedding_text)
        self.assertIn("updated policy optimization cache text", refreshed_sidecar_text)
        self.assertNotIn("initial policy optimization cache text", refreshed_entry.embedding_text)
        self.assertNotIn("initial policy optimization cache text", refreshed_sidecar_text)

    def test_stale_arxiv_embed_text_sidecar_is_not_used_for_embedding_input(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            metadata_root = Path(tmp) / "docs" / "papers"
            metadata_path = metadata_root / "2024" / "2501.00002" / "metadata.yml"
            metadata_path.parent.mkdir(parents=True)
            metadata_path.write_text(
                VALID_METADATA.replace("cond-mat/0112110v2", "2501.00002"),
                encoding="utf-8",
            )
            metadata_path.with_name("embed_text.md").write_text(
                '<!-- arxiv-full-text:v1 {"arxiv_id":"2501.00001","source":"arxiv-html"} -->\n\n'
                "## Introduction\n\n"
                "In this paper, we propose stale arxiv source text that must not reach embeddings.",
                encoding="utf-8",
            )

            entry = Catalog.from_metadata_root(metadata_root, write_embedding_input_sidecars=True).entries[0]
            sidecar_text = embedding_input_sidecar_path(metadata_path).read_text(encoding="utf-8")

        self.assertNotIn("stale arxiv source text", entry.embedding_text)
        self.assertNotIn("stale arxiv source text", sidecar_text)

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
            "Only abstract.",
        )

    def test_embedding_text_uses_natural_document_text(self) -> None:
        text = build_embedding_text(
            title="A Tiny Paper",
            tags=("planning", "control"),
            summary="A compact summary.",
            abstract="A compact abstract.",
        )

        self.assertEqual(
            text,
            "A Tiny Paper\n\nTopics include planning, control.\n\nA compact summary.\n\nA compact abstract.",
        )
        self.assertNotIn("Title:", text)
        self.assertNotIn("Summary:", text)
        self.assertNotIn("Abstract:", text)

    def test_embedding_chunks_keep_long_abstract_without_truncating(self) -> None:
        abstract = " ".join(
            f"Sentence {index} explains a useful control and optimization idea for semantic retrieval."
            for index in range(80)
        )

        chunks = build_embedding_chunks(title="", tags=(), summary="", abstract=abstract)
        text = "\n\n".join(chunk.text for chunk in chunks)

        self.assertGreater(len([chunk for chunk in chunks if chunk.role == "abstract"]), 1)
        self.assertIn("Sentence 0 explains", text)
        self.assertIn("Sentence 79 explains", text)
        self.assertLessEqual(max(len(chunk.text) for chunk in chunks), 2_000)
        self.assertLessEqual(max(embedding_token_count(chunk.text) for chunk in chunks), 256)

    def test_embedding_chunks_keep_sentence_abbreviations_together(self) -> None:
        chunks = chunk_embedding_text(
            "Dr. Hooker read the manuscript and reported a coherent result. "
            "The MS. work was copied and circulated before publication. "
            "Mr. Darwin revised the argument and added evidence. "
            "Prof. Wallace supplied an independent account of natural selection.",
            max_chars=74,
            min_chars=0,
        )

        text = "\n\n".join(chunks)
        self.assertGreater(len(chunks), 1)
        self.assertIn("Dr. Hooker", text)
        self.assertIn("MS. work", text)
        self.assertIn("Mr. Darwin", text)
        self.assertIn("Prof. Wallace", text)
        self.assertFalse(any(chunk.endswith(("Dr.", "MS.", "Mr.", "Prof.")) for chunk in chunks))
        self.assertLessEqual(max(len(chunk) for chunk in chunks), 74)
        self.assertLessEqual(max(embedding_token_count(chunk) for chunk in chunks), 256)

    def test_embedding_text_removes_inline_urls(self) -> None:
        text = build_embedding_text(
            title="A Tiny Paper",
            tags=(),
            summary=r"Code is available at https://example.test/repo and \urlhttps://example.test/other.",
            abstract=r"Documentation lives at \url{ann-benchmarks.com}.",
        )

        self.assertNotIn("https://", text)
        self.assertNotIn(r"\url", text)

    def test_embedding_text_removes_url_pointer_boilerplate(self) -> None:
        text = build_embedding_text(
            title="",
            tags=(),
            summary="",
            abstract=(
                "This paper introduces a useful gene-editing assistant. "
                "The published version of this draft is available at https://example.test/published."
            ),
        )

        self.assertEqual(text, "This paper introduces a useful gene-editing assistant.")
        self.assertNotIn("published version", text)

    def test_embedding_text_compaction_prefers_complete_sentences(self) -> None:
        compacted = truncate_embedding_text(
            "First sentence stays whole. Second sentence is intentionally long and should be omitted.",
            30,
        )

        self.assertEqual(compacted, "First sentence stays whole.")
        self.assertFalse(compacted.endswith("..."))
        self.assertEqual(
            truncate_embedding_text("A sentence that trails off... More text follows.", 30),
            "A sentence that trails off.",
        )
        self.assertEqual(
            truncate_embedding_text("In cases where this is e.g. available, the method can proceed. Later text.", 70),
            "In cases where this is e.g. available, the method can proceed.",
        )
        self.assertEqual(
            truncate_embedding_text("First good sentence. The following three points are:", 80),
            "First good sentence.",
        )

    def test_embedding_content_compaction_prefers_coherent_sections(self) -> None:
        compacted = compact_embedding_content(
            "## Introduction\n\n"
            "Opening paragraph frames data-driven control and reinforcement learning for compact semantic search.\n\n"
            "The rest of this paper is organized as follows. This sentence is boilerplate.\n\n"
            "In this paper, we propose a data-enabled policy optimization method that computes policy gradients "
            "from persistently exciting data and gives global convergence guarantees.\n\n"
            "### Lemma 2\n\n"
            "Those bounds are also true for technical symbols and should not become the paper summary.\n\n"
            "### Proof\n\n"
            "where the following matrix identities continue for several equations without semantic context.\n\n"
            "## Conclusion\n\n"
            "In this paper, we showed that the method uses finite data, supports regularization, and improves "
            "the optimization landscape for direct adaptive control.",
            max_chars=700,
        )

        self.assertIn("Opening paragraph", compacted)
        self.assertIn("we propose a data-enabled policy optimization method", compacted)
        self.assertIn("we showed that the method uses finite data", compacted)
        self.assertNotIn("The rest of this paper", compacted)
        self.assertNotIn("Those bounds", compacted)
        self.assertNotIn("Proof", compacted)
        self.assertFalse(compacted.endswith("..."))

    def test_embedding_sidecar_removes_empty_citation_stubs(self) -> None:
        cleaned = clean_embedding_sidecar_text(
            "## Introduction\n\nThe model improves by 5% on \\[\\] while preserving useful semantic context."
        )

        self.assertIn("The model improves by 5% while preserving useful semantic context.", cleaned)
        self.assertNotIn("on.", cleaned)

    def test_embedding_sidecar_ignores_arxiv_full_text_provenance_marker(self) -> None:
        cleaned = clean_embedding_sidecar_text(
            '<!-- arxiv-full-text:v1 {"arxiv_id":"2501.00001","source":"arxiv-html"} -->\n\n'
            "## Introduction\n\nUseful paragraph with enough semantic words for embedding."
        )

        self.assertEqual(cleaned, "## Introduction\n\nUseful paragraph with enough semantic words for embedding.")

    def test_embedding_sidecar_heading_whitespace_does_not_crash(self) -> None:
        cleaned = clean_embedding_sidecar_text("##\tIntroduction\n\nUseful paragraph with enough words.")

        self.assertEqual(cleaned, "## Introduction\n\nUseful paragraph with enough words.")

    def test_embedding_sidecar_strips_tabbed_h1_title(self) -> None:
        cleaned = clean_embedding_sidecar_text(
            "#\tPaper Title\n\n##\tIntroduction\n\nUseful paragraph with enough words."
        )

        self.assertEqual(cleaned, "## Introduction\n\nUseful paragraph with enough words.")

    def test_embedding_sidecar_normalizes_adjacent_heading_forms(self) -> None:
        cases = {
            "##   1. Introduction": "## Introduction",
            "###\tTabbed Section Title": "### Tabbed Section Title",
            "#### Abstract": "## Abstract",
            "### A) Model Details": "### Model Details",
            "### A Model Details": "### Model Details",
            "### a Equilibrium traffic": "### Equilibrium traffic",
            "### Proof of Theorem [3.3](https://example.test#proof)": "### Proof of Theorem 3.3",
        }

        for raw_heading, expected_heading in cases.items():
            with self.subTest(raw_heading=raw_heading):
                cleaned = clean_embedding_sidecar_text(f"{raw_heading}\n\nUseful paragraph with enough words.")
                self.assertEqual(cleaned, f"{expected_heading}\n\nUseful paragraph with enough words.")

    def test_embedding_sidecar_ignores_empty_hash_lines(self) -> None:
        cleaned = clean_embedding_sidecar_text("##\n#\n\nUseful paragraph with enough words.")

        self.assertEqual(cleaned, "## Paper Body\n\nUseful paragraph with enough words.")

    def test_embedding_sidecar_still_stops_before_appendix(self) -> None:
        cleaned = clean_embedding_sidecar_text(
            "## Introduction\n\nUseful paragraph with enough words.\n\n## Appendix A\n\nExtra proof text should not stay."
        )

        self.assertEqual(cleaned, "## Introduction\n\nUseful paragraph with enough words.")

    def test_embedding_sidecar_keeps_prose_appendix_mentions(self) -> None:
        cleaned = clean_embedding_sidecar_text(
            "## Introduction\n\n"
            "The matrix Laplace transform method follows an earlier argument.\n\n"
            "Appendix.\n\n"
            "The insight is still part of the main technical development."
        )

        self.assertIn("The insight is still part", cleaned)

    def test_embedding_sidecar_stops_before_plain_appendix_heading(self) -> None:
        cleaned = clean_embedding_sidecar_text(
            "## Introduction\n\nUseful paragraph with enough words.\n\nAppendix A\n\nExtra proof text should not stay."
        )

        self.assertEqual(cleaned, "## Introduction\n\nUseful paragraph with enough words.")

    def test_embedding_sidecar_deduplicates_repeated_docling_headings(self) -> None:
        cleaned = clean_embedding_sidecar_text(
            "## Introduction. Introduction\n\n"
            "Useful paragraph with enough words.\n\n"
            "### Application: The matrix Bernstein inequality. Application: The matrix Bernstein inequality\n\n"
            "Another useful paragraph with enough words."
        )

        self.assertIn("## Introduction\n\nUseful paragraph with enough words.", cleaned)
        self.assertIn("### Application: The matrix Bernstein inequality", cleaned)
        self.assertNotIn("Application: The matrix Bernstein inequality. Application", cleaned)

    def test_embedding_sidecar_drops_pdf_artifact_lines(self) -> None:
        cleaned = clean_embedding_sidecar_text(
            "## Introduction\n\n"
            "Image: img/concept.pdf\n\n"
            "$^*$ Corresponding author: mailto:author@example.testauthor@example.testfootnote-1\n\n"
            "Robots can adapt after damage with useful semantic context \\supercite."
        )

        self.assertNotIn("Image:", cleaned)
        self.assertNotIn("mailto:", cleaned)
        self.assertNotIn("footnote-", cleaned)
        self.assertNotIn("supercite", cleaned)
        self.assertIn("Robots can adapt after damage with useful semantic context.", cleaned)

    def test_embedding_sidecar_preserves_raw_math_macros(self) -> None:
        cleaned = clean_embedding_sidecar_text(
            "## Introduction\n\nThe matrix order is expressed as $\\mtx{A} \\preccurlyeq\\mtx{B}$ in the proof."
        )

        self.assertIn("$\\mtx{A} \\preccurlyeq\\mtx{B}$", cleaned)

    def test_embedding_sidecar_repairs_pdf_diacritic_loss(self) -> None:
        cleaned = clean_embedding_sidecar_text(
            "## Introduction\n\n"
            "Traditionally, networks have been described using the random graph theory of Erd os and Renyi."
        )

        self.assertIn("Erd\u0151s and R\u00e9nyi", cleaned)
        self.assertNotIn("Erd os", cleaned)

    def test_embedding_sidecar_repairs_diacritic_loss_after_reflow(self) -> None:
        cleaned = clean_embedding_sidecar_text(
            "## Introduction\n\n"
            "Traditionally, networks have been described using the random graph theory of Erd\n\n"
            "os and Renyi (ER), but the predictions of the theory were rarely tested in the real world."
        )

        self.assertIn("Erd\u0151s and R\u00e9nyi", cleaned)
        self.assertNotIn("Erd os", cleaned)

    def test_embedding_sidecar_removes_tex_spacing_spans(self) -> None:
        cleaned = clean_embedding_sidecar_text(
            "## Introduction\n\n"
            "The model has exponent $\\gamma\\_{model}=2.9$ (Fig.$\\,$2A). "
            "Indeed, as Fig.$\\,$2A demonstrates, $P(k)$ depends on $m\\_0+t$."
        )

        self.assertIn("(Fig. 2A).", cleaned)
        self.assertIn("as Fig. 2A demonstrates", cleaned)
        self.assertIn("$\\gamma_{model}=2.9$", cleaned)
        self.assertIn("$m_0+t$", cleaned)
        self.assertNotIn("$\\,$", cleaned)

    def test_embedding_sidecar_reflows_converter_line_breaks(self) -> None:
        cleaned = clean_embedding_sidecar_text(
            "## Introduction\n\n"
            "The above examples (\n\n"
            "12) demonstrate that many large random networks share common properties.\n\n"
            "Most real world networks are open,\n"
            "they form by the continuous addition of new vertices.\n\n"
            "Both models assume that we start with a fixed number (\n\n"
            "$N$) of vertices that are then randomly connected.\n\n"
            "we show that, independent of the system, the probability\n\n"
            "$P(k)$ that a vertex interacts with $k$ other vertices decays as a power-law.\n\n"
            "These aspects are discussed in Sec.\n\n"
            "II, while Sec.III is not model-specific at all."
        )

        self.assertIn("The above examples (12) demonstrate", cleaned)
        self.assertIn("networks are open, they form", cleaned)
        self.assertIn("fixed number ($N$) of vertices", cleaned)
        self.assertIn("probability $P(k)$ that a vertex", cleaned)
        self.assertIn("discussed in Sec. II, while", cleaned)
        self.assertNotIn("(\n\n12)", cleaned)
        self.assertNotIn("probability\n\n$P(k)$", cleaned)

    def test_embedding_sidecar_repairs_split_docling_heading(self) -> None:
        cleaned = clean_embedding_sidecar_text(
            "## Polynomial moments and the spectral\n\n"
            "norm of a random matrix. Polynomial moments and the spectral norm of a random matrix "
            "We can also study the spectral norm of a random matrix."
        )

        self.assertIn("## Polynomial moments and the spectral norm of a random matrix", cleaned)
        self.assertIn("We can also study the spectral norm", cleaned)
        self.assertNotIn("## Polynomial moments and the spectral\n\nnorm", cleaned)

    def test_embedding_sidecar_rejects_front_matter_only_monograph(self) -> None:
        cleaned = clean_embedding_sidecar_text(
            "# Monograph Title\n\n"
            "Author Name\n\n"
            "###### Contents\n\n"
            "1. 0 Preface\n\n"
            "## Chapter 0 Preface\n\n"
            "This preface thanks colleagues and describes the manuscript history, but it is not the technical body."
        )

        self.assertEqual(cleaned, "")

    def test_embedding_sidecar_monograph_starts_at_first_real_chapter(self) -> None:
        cleaned = clean_embedding_sidecar_text(
            "# Monograph Title\n\n"
            "Author Name\n\n"
            "###### Contents\n\n"
            "1. 0 Preface\n"
            "2. 1 Matrix Methods\n\n"
            "## Chapter 0 Preface\n\n"
            "This preface thanks colleagues and describes manuscript history.\n\n"
            "## Chapter 1 Matrix Methods\n\n"
            "Matrix concentration inequalities control random matrices with useful noncommutative tail bounds.\n\n"
            "## References\n\n"
            "Reference noise."
        )

        self.assertEqual(
            cleaned,
            "## Chapter 1 Matrix Methods\n\n"
            "Matrix concentration inequalities control random matrices with useful noncommutative tail bounds.",
        )


if __name__ == "__main__":
    unittest.main()
