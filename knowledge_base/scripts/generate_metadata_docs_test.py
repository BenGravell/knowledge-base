from __future__ import annotations

import unittest

from pydantic import ValidationError

from knowledge_base.scripts.generate_metadata_docs import (
    REFERENCE_PATH,
    TEMPLATE_PATH,
    render_reference,
    validate_template,
)


class MetadataReferenceTests(unittest.TestCase):
    def test_checked_in_reference_and_template_match_model(self) -> None:
        template = TEMPLATE_PATH.read_text(encoding="utf-8")
        self.assertEqual(REFERENCE_PATH.read_text(encoding="utf-8"), render_reference(template))

    def test_template_must_include_all_fields_in_order(self) -> None:
        template = TEMPLATE_PATH.read_text(encoding="utf-8")
        for invalid in ("[]", template.replace("algorithm: ABC\n", ""), template + "unknown: value\n"):
            with self.subTest(template=invalid), self.assertRaises(ValueError):
                validate_template(invalid)

    def test_template_must_satisfy_model_and_audit_presence_rules(self) -> None:
        template = TEMPLATE_PATH.read_text(encoding="utf-8")
        with self.assertRaises(ValidationError):
            validate_template(template.replace("audit_status: raw", "audit_status: invalid"))
        with self.assertRaisesRegex(ValueError, "null required fields: year"):
            validate_template(template.replace("year: 1234", "year: null"))
