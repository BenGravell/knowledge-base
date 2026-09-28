import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from knowledge_base.prefill.sources import ieee, neurips


class SourceUrlsTest(unittest.TestCase):
    def test_ieee_stamp_pdf_id(self):
        url = "https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=5751929&ref=abc"
        self.assertEqual(ieee.source_key_for_token(url), "5751929")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "IEEE.md"
            path.write_text(url + "\n")
            self.assertEqual(ieee.extract_entries(path), [("https://ieeexplore.ieee.org/document/5751929", "5751929")])

    @patch("knowledge_base.prefill.sources.ieee.fetch_doi_from_crossref_title", return_value="10.5772/78")
    @patch("knowledge_base.prefill.sources.ieee.fetch_page_html", return_value="")
    @patch("knowledge_base.prefill.sources.ieee.requests.get")
    def test_ieee_rejects_unrelated_title_doi(self, get, _page, _title):
        get.side_effect = [Mock(ok=False), Mock(text="Title: Motion Planning\n10.5772/78")]
        with self.assertRaisesRegex(ValueError, "No verified DOI"):
            ieee.fetch_ieee_doi("5751929")

    @patch("knowledge_base.prefill.sources.neurips.fetch_page_html")
    @patch("knowledge_base.prefill.sources.neurips.fetch_metadata_json", return_value={})
    def test_neurips_conference_links_and_year(self, _metadata, page):
        paper_hash = "31fb284a0aaaad837d2930a610cd5e50"
        url = f"https://proceedings.neurips.cc/paper_files/paper/2025/hash/{paper_hash}-Abstract-Conference.html"
        pdf = f"https://proceedings.neurips.cc/paper_files/paper/2025/file/{paper_hash}-Paper-Conference.pdf"
        page.return_value = (
            '<meta name="citation_title" content="Constrained Diffusers for Safe Planning and Control">'
            '<meta name="citation_author" content="Zhang, Jichen">'
            '<meta name="citation_pdf_url" content="' + pdf + '">'
            '<meta name="citation_publication_date" content="2026-04-23">'
            '<p class="paper-abstract">An abstract.</p>'
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "NEURIPS.md"
            path.write_text(url + "\n")
            self.assertEqual(neurips.extract_entries(path), [("2025", paper_hash)])
        fields = neurips.fetch_neurips_fields("2025", paper_hash)
        self.assertEqual(fields["link"], pdf)
        self.assertEqual(fields["year"], 2026)
        self.assertEqual(fields["links_alt"], [neurips.abstract_url("2025", paper_hash)])


if __name__ == "__main__":
    unittest.main()
