import contextlib
import io
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path
from typing import Any, ClassVar
from unittest.mock import Mock, patch

import requests
import yaml

from knowledge_base.prefill import doi
from knowledge_base.prefill.runner import run_source
from knowledge_base.prefill.sources import mdpi


class MdpiIdentityTest(unittest.TestCase):
    URL = "https://www.mdpi.com/2227-9091/7/2/53"
    MESSAGE: ClassVar[dict[str, Any]] = {
        "DOI": "10.3390/risks7020053",
        "title": ["The Population Accuracy Index"],
        "author": [{"given": "Ross", "family": "Taplin"}],
        "published": {"date-parts": [[2019]]},
        "abstract": "An abstract.",
        "ISSN": ["2227-9091"],
        "volume": "7",
        "issue": "2",
        "page": "53",
        "resource": {"primary": {"URL": URL}},
    }

    def test_resolves_unlisted_journal_and_url_variants_without_guessing_doi(self):
        message = deepcopy(self.MESSAGE)
        message.update(ISSN=["1234-567X"], DOI="10.3390/publisher-chosen-suffix")
        message["resource"]["primary"]["URL"] = "https://www.mdpi.com/1234-567X/7/2/53"
        response = Mock()
        response.json.return_value = {"message": {"items": [message], "total-results": 1}}
        with patch("knowledge_base.prefill.sources.mdpi.requests.get", return_value=response) as get:
            result = mdpi.resolve_doi("http://mdpi.com/1234-567X/7/2/53/pdf?download=1")
        self.assertEqual(result, message["DOI"])
        self.assertIn("/journals/1234-567X/works", get.call_args.args[0])

    def test_ignores_search_rank_and_accepts_only_the_exact_publisher_url(self):
        unrelated = deepcopy(self.MESSAGE)
        unrelated["DOI"] = "10.3390/unrelated"
        unrelated["resource"]["primary"]["URL"] = self.URL + "0"
        response = Mock()
        response.json.return_value = {"message": {"items": [unrelated, self.MESSAGE], "total-results": 10000}}
        with patch("knowledge_base.prefill.sources.mdpi.requests.get", return_value=response) as get:
            self.assertEqual(mdpi.resolve_doi(self.URL), self.MESSAGE["DOI"])
            get.assert_called_once()
            self.assertEqual(get.call_args.kwargs["params"]["rows"], 10)

    def test_rejects_non_mdpi_hosts_before_requesting(self):
        with patch("knowledge_base.prefill.sources.mdpi.requests.get") as get:
            for url in ("https://evilmdpi.com/2227-9091/7/2/53", "https://example.com/mdpi.com/2227-9091/7/2/53"):
                self.assertFalse(mdpi.accept_url(url))
                with self.assertRaises(ValueError):
                    mdpi.resolve_doi(url)
            get.assert_not_called()

    def test_runner_requires_unique_verified_identity_before_handling_source(self):
        scenarios = (
            "wrong_journal",
            "missing_issn",
            "wrong_article",
            "wrong_url",
            "missing_url",
            "no_match",
            "ambiguous",
            "network_error",
            "wrong_doi",
            "changed_resource",
            "valid",
            "existing",
        )
        for scenario in scenarios:
            with self.subTest(scenario=scenario), tempfile.TemporaryDirectory() as directory:
                root = Path(directory)
                queue = root / "MDPI.md"
                queue.write_text(self.URL + "\n", encoding="utf-8")
                papers = root / "papers"
                message = deepcopy(self.MESSAGE)
                if scenario == "wrong_journal":
                    message.update(DOI="10.3390/economies7020053", ISSN=["2227-7099"])
                elif scenario == "missing_issn":
                    message.pop("ISSN")
                elif scenario == "wrong_article":
                    message["page"] = "54"
                elif scenario == "wrong_url":
                    message["resource"]["primary"]["URL"] = self.URL + "0"
                elif scenario == "missing_url":
                    message.pop("resource")
                items = [] if scenario == "no_match" else [message]
                if scenario == "ambiguous":
                    items.append({**message, "DOI": "10.3390/another-registration"})
                search = Mock()
                search.json.return_value = {"message": {"items": items, "total-results": len(items)}}
                fetched = deepcopy(message)
                if scenario == "wrong_doi":
                    fetched["DOI"] = "10.3390/risks7020054"
                elif scenario == "changed_resource":
                    fetched["resource"]["primary"]["URL"] = self.URL + "0"
                work = Mock()
                work.json.return_value = {"message": fetched}

                existing = root / "existing.yml"
                existing.write_text("abstract: Existing paper\n", encoding="utf-8")
                index: dict[str, Path] = (
                    {message["DOI"].lower(): existing} if scenario in {"wrong_journal", "existing"} else {}
                )
                output = io.StringIO()
                with (
                    patch.object(doi, "PAPERS_DIR", papers),
                    patch("knowledge_base.prefill.runner.build_doi_index", return_value=index),
                    patch("knowledge_base.prefill.doi.requests.get") as get,
                    patch("knowledge_base.prefill.runner.time.sleep"),
                    contextlib.redirect_stdout(output),
                ):
                    get.side_effect = requests.Timeout("unavailable") if scenario == "network_error" else [search, work]
                    run_source("mdpi", ["--input", str(queue)])

                written = list(papers.rglob("metadata.yml"))
                if scenario == "valid":
                    self.assertEqual(len(written), 1)
                    metadata = yaml.safe_load(written[0].read_text(encoding="utf-8"))
                    self.assertEqual(metadata["doi"], "10.3390/risks7020053")
                    self.assertEqual(metadata["link"], self.URL)
                else:
                    self.assertEqual(written, [])
                if scenario in {"valid", "existing"}:
                    self.assertEqual(queue.read_text(encoding="utf-8"), "")
                else:
                    self.assertEqual(queue.read_text(encoding="utf-8"), self.URL + "\n")
                    self.assertIn("1 failed", output.getvalue())
                self.assertEqual(existing.read_text(encoding="utf-8"), "abstract: Existing paper\n")


if __name__ == "__main__":
    unittest.main()
