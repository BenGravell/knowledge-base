import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from knowledge_base.prefill import doi
from knowledge_base.prefill.sources import elsevier, ieee, rss


class PublisherFallbacksTest(unittest.TestCase):
    @patch("knowledge_base.prefill.doi.requests.get")
    def test_crossref_title_match_is_exact(self, get: Mock) -> None:
        response = Mock()
        response.json.return_value = {
            "message": {
                "items": [
                    {"title": ["Similar Paper"], "DOI": "10.1/wrong"},
                    {"title": ["A <i>Useful</i> Paper"], "DOI": "10.1/right"},
                ]
            }
        }
        get.return_value = response

        self.assertEqual(doi.fetch_doi_from_crossref_title("A Useful Paper"), "10.1/right")

    @patch("knowledge_base.prefill.sources.elsevier.requests.get")
    @patch("knowledge_base.prefill.sources.elsevier.fetch_doi_from_crossref_pii", side_effect=ValueError)
    def test_elsevier_uses_public_article_api(self, _crossref, get: Mock) -> None:
        get.return_value = Mock(
            ok=True,
            json=lambda: {"full-text-retrieval-response": {"coredata": {"prism:doi": "10.1016/j.crma.2008.03.014"}}},
        )

        doi = elsevier.fetch_elsevier_doi(
            "https://www.sciencedirect.com/science/article/pii/S1631073X08000964",
            "S1631073X08000964",
        )

        self.assertEqual(doi, "10.1016/j.crma.2008.03.014")

    @patch("knowledge_base.prefill.sources.ieee.fetch_doi_from_crossref_title")
    @patch("knowledge_base.prefill.sources.ieee.fetch_page_html")
    @patch("knowledge_base.prefill.sources.ieee.requests.get")
    def test_ieee_uses_rendered_title_when_xplore_blocks_scraping(
        self, get: Mock, fetch_page: Mock, fetch_title: Mock
    ) -> None:
        get.return_value = Mock(ok=False)
        fetch_page.side_effect = ["", "Title: A Useful IEEE Paper\n\nMarkdown Content:"]
        fetch_title.return_value = "10.1109/example"

        self.assertEqual(ieee.fetch_ieee_doi("123"), "10.1109/example")
        fetch_title.assert_called_once_with("A Useful IEEE Paper")


class CurrentRssPageTest(unittest.TestCase):
    HTML = """
<meta name="description" content="RSS 2026, July 13, 2026 - July 17, 2026" />
<h3 class="page-title"><b>HOP: Fast Planning</b></h3>
<div class="paper-author-name">Miaomiao Dai, Zhongqiang Ren</div>
<a href="https://www.roboticsproceedings.org/rss22/p186.pdf" title="Download PDF">PDF</a>
<p><b>Abstract: </b>A horizon-optimal planning method.</p>
"""

    def test_extract_current_program_url(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "RSS.md"
            path.write_text("https://roboticsconference.org/program/papers/186/\n", encoding="utf-8")

            self.assertEqual(
                rss.extract_entries(path),
                [
                    (
                        "https://roboticsconference.org/program/papers/186/",
                        "",
                        "program/papers/186",
                    )
                ],
            )

    @patch("knowledge_base.prefill.sources.rss.fetch_page_html", return_value=HTML)
    def test_parse_current_program_page(self, _fetch) -> None:
        fields = rss.fetch_rss_fields("https://roboticsconference.org/program/papers/186/", "")

        self.assertEqual(fields["title"], "HOP: Fast Planning")
        self.assertEqual(fields["authors"], ["Miaomiao Dai", "Zhongqiang Ren"])
        self.assertEqual(fields["year"], 2026)
        self.assertEqual(fields["abstract"], "A horizon-optimal planning method.")
        self.assertEqual(fields["link"], "https://www.roboticsproceedings.org/rss22/p186.pdf")


if __name__ == "__main__":
    unittest.main()
