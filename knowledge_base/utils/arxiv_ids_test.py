import unittest

from knowledge_base.utils.arxiv_ids import (
    arxiv_abs_url,
    arxiv_html_url,
    arxiv_pdf_url,
    arxiv_year_from_id,
    normalize_arxiv_id,
)


class ArxivIdentifierTests(unittest.TestCase):
    def test_normalizes_ids_and_urls(self) -> None:
        for value, expected in (
            (None, ""),
            ("arXiv:2401.01234v2", "2401.01234"),
            ("https://arxiv.org/pdf/math.CA/0410542", "math/0410542"),
            ("https://arxiv.org/pdf/math.mg/0502327", "math/0502327"),
            ("https://arxiv.org/pdf/cond-mat/9910332v3.pdf", "cond-mat/9910332"),
            ("https://ar5iv.labs.arxiv.org/html/2401.01234v2", "2401.01234"),
        ):
            with self.subTest(value=value):
                self.assertEqual(normalize_arxiv_id(value), expected)

    def test_infers_year_and_builds_urls_from_normalized_ids(self) -> None:
        for value, expected in (("2401.01234v2", 2024), ("cond-mat/9910332", 1999), ("2413.01234", 0), (None, 0)):
            with self.subTest(value=value):
                self.assertEqual(arxiv_year_from_id(value), expected)
        self.assertEqual(arxiv_abs_url("arXiv:2401.01234v2"), "https://arxiv.org/abs/2401.01234")
        self.assertEqual(arxiv_pdf_url("cond-mat/9910332v3"), "https://arxiv.org/pdf/cond-mat/9910332")
        self.assertEqual(arxiv_html_url("2401.01234v2"), "https://ar5iv.labs.arxiv.org/html/2401.01234")
