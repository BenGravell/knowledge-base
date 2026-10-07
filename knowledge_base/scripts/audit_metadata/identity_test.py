"""Regression checks for inconsistent paper identifiers at the audit boundary."""

import tempfile
import unittest
from pathlib import Path
from typing import Any

import yaml

from knowledge_base.scripts.audit_metadata.cli import _skip_reviewed_errors
from knowledge_base.scripts.audit_metadata.file_audit import audit_file


class IdentityAuditTests(unittest.TestCase):
    def audit(self, **data: Any):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "metadata.yml"
            path.write_text(yaml.safe_dump(data), encoding="utf-8")
            return audit_file(path, selected_checks={"identity"})

    def test_wrong_primary_doi_is_reported_even_for_reviewed_metadata(self):
        for status in ("raw", "partial", "reviewed"):
            with self.subTest(status=status):
                data, issues = self.audit(
                    link="https://doi.org/10.3390/risks7020053",
                    doi="10.3390/economies7020053",
                    audit_status=status,
                )
                self.assertEqual(len(issues), 1)
                self.assertIn("10.3390/risks7020053", issues[0].message)
                self.assertIsNone(issues[0].suggestion)
                self.assertEqual(_skip_reviewed_errors(data, issues), (issues, 0))

    def test_primary_identifiers_are_compared(self):
        for data in (
            {"link": "https://doi.org/10.1234/wrong", "doi": "10.1234/right"},
            {"link": "https://arxiv.org/pdf/2401.01234v2.pdf", "arxiv_id": "2401.05678"},
        ):
            with self.subTest(data=data):
                self.assertEqual(len(self.audit(**data)[1]), 1)

    def test_versions_alternates_and_unrecognized_hosts_do_not_false_positive(self):
        for data in (
            # MDPI identifiers require online source verification, not DOI inference.
            {"link": "https://www.mdpi.com/2227-9091/7/2/53", "doi": "10.3390/economies7020053"},
            {"link": "https://www.mdpi.com/2227-9091/7/2/53/pdf", "doi": "10.3390/risks7020053"},
            {"link": "https://doi.org/10.1234%2FABC", "doi": "10.1234/abc"},
            {"link": "https://arxiv.org/pdf/2401.01234v2.pdf", "arxiv_id": "2401.01234"},
            {"link": "https://arxiv.org/abs/math.OC/0301001", "arxiv_id": "math/0301001"},
            {
                "link": "https://arxiv.org/abs/2401.01234",
                "arxiv_id": "2401.01234",
                "doi": "10.1234/published",
                "links_alt": ["https://doi.org/10.1234/preprint"],
            },
            {"link": "https://example.com/mdpi.com/2227-9091/7/2/53", "doi": "10.3390/economies7020053"},
        ):
            with self.subTest(data=data):
                self.assertEqual(self.audit(**data)[1], [])


if __name__ == "__main__":
    unittest.main()
