from __future__ import annotations

import unittest

from pydantic import ValidationError

from knowledge_base.metadata import REQUIRED_FIELDS, VALID_FIELDS, MetadataRecord


class MetadataTests(unittest.TestCase):
    def test_normalizes_legacy_yaml_values(self) -> None:
        record = MetadataRecord.model_validate(
            {
                "title": "  A paper  ",
                "authors": " Ada Lovelace ",
                "year": "2024",
                "doi": "https://doi.org/10.1000/example",
                "arxiv_id": "arXiv:cond-mat/0112110v2",
                "tags": [" planning ", None, ""],
                "abstract": None,
                "links_alt": "https://example.com/paper",
            }
        )
        self.assertEqual(record.title, "A paper")
        self.assertEqual(record.authors, ("Ada Lovelace",))
        self.assertEqual(record.year, "2024")
        self.assertEqual(record.doi, "10.1000/example")
        self.assertEqual(record.arxiv_id, "cond-mat/0112110")
        self.assertEqual(record.tags, ("planning",))
        self.assertEqual(record.abstract, "")
        self.assertEqual(record.links_alt, ("https://example.com/paper",))
        self.assertEqual(record.audit_status, "")

    def test_rejects_unknown_fields_invalid_choices_and_nested_values(self) -> None:
        for data in (
            {"unknown": "value"},
            {"title": ["A paper"]},
            {"authors": [["Ada Lovelace"]]},
            {"year": True},
            {"type": "Not a paper type"},
            {"audit_status": "approved"},
        ):
            with self.subTest(data=data), self.assertRaises(ValidationError):
                MetadataRecord.model_validate(data)

    def test_preserves_audit_requirements_and_defaults(self) -> None:
        self.assertEqual(REQUIRED_FIELDS, ("title", "authors", "year", "type", "abstract", "audit_status"))
        self.assertEqual(VALID_FIELDS, tuple(MetadataRecord.model_fields))
        self.assertEqual(MetadataRecord().year, "")
        self.assertEqual(MetadataRecord(year=2024).year, 2024)
