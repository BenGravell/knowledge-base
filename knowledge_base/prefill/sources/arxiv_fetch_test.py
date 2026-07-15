import unittest
from unittest.mock import Mock, patch

from knowledge_base.prefill.sources.arxiv_fetch import ArxivBatchCache


class ArxivBatchCacheTest(unittest.TestCase):
    @patch("knowledge_base.prefill.sources.arxiv_fetch.fetch_many_via_oai")
    @patch("knowledge_base.prefill.sources.arxiv_fetch.fetch_many_with_retry")
    def test_atom_omissions_fall_back_to_oai(self, fetch_atom: Mock, fetch_oai: Mock) -> None:
        fetch_atom.return_value = {"2401.01234": {"arxiv_id": "2401.01234"}}
        fetch_oai.return_value = {"math.CA/0410542": {"arxiv_id": "math.CA/0410542"}}
        cache = ArxivBatchCache(["2401.01234", "math.CA/0410542"])
        cache.use_oai = False

        records, attempted = cache.fetch_batch(["2401.01234", "math.CA/0410542"])

        self.assertEqual(set(records), {"2401.01234", "math.CA/0410542"})
        self.assertEqual(attempted, ["2401.01234", "math.CA/0410542"])
        fetch_oai.assert_called_once_with(["math.CA/0410542"])


if __name__ == "__main__":
    unittest.main()
