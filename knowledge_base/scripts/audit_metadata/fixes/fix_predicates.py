"""Issue-routing predicates for metadata autofixes."""

from knowledge_base.config import VALID_TYPES
from knowledge_base.scripts.audit_metadata.rules.abstract_data import (
    _ABSTRACT_DOLLAR_MATH_ISSUE_PREFIX,
    _ABSTRACT_LATEX_ARTIFACT_ISSUE_PREFIX,
    _PUBLISHER_MARK_ABSTRACT_ISSUE_PREFIX,
    _SUMMARY_ABSTRACT_OVERLAP_ISSUE_PREFIX,
)
from knowledge_base.scripts.audit_metadata.rules.author_rules import (
    _AUTHOR_ASCII_NORMALIZATION_ISSUE_PREFIX,
    _AUTHOR_MOJIBAKE_ISSUE_PREFIX,
    _NON_INDIVIDUAL_AUTHOR_ISSUE_PREFIX,
)
from knowledge_base.scripts.audit_metadata.rules.encoding import _TEXT_MOJIBAKE_ISSUE_PREFIX
from knowledge_base.scripts.audit_metadata.rules.field_data import (
    _FOLDED_TEXT_FIELD_BLANK_LINE_ISSUE_PREFIX,
    _FOLDED_TEXT_FIELD_ISSUE_PREFIX,
    _FOLDED_TEXT_FIELD_MULTILINE_ISSUE_PREFIX,
    _FOLDED_TEXT_FIELDS,
    _MULTILINE_FORBIDDEN_FIELDS,
    _TITLE_CHARACTER_ESCAPE_ISSUE_PREFIX,
)
from knowledge_base.scripts.audit_metadata.rules.spacing_data import (
    _ASCII_MULTI_DASH_ISSUE_PREFIX,
    _BIG_WHITESPACE_ISSUE_PREFIX,
    _TIGHT_LETTER_PAREN_ISSUE_PREFIX,
)
from knowledge_base.scripts.audit_metadata.rules.tag_data import (
    _DATABASE_DUPLICATE_TAG_MESSAGE_PREFIX,
    _DUPLICATE_TAG_MESSAGE_PREFIX,
    _PLURAL_DUPLICATE_TAG_MESSAGE_PREFIX,
    _TAG_DATABASE_ISSUE_PREFIX,
)
from knowledge_base.scripts.audit_metadata.rules.tag_database import (
    _is_tag_database_missing_issue,
)
from knowledge_base.scripts.audit_metadata.rules.text_artifacts import _HIGH_CONFIDENCE_OCR_ARTIFACT_ISSUE_PREFIX
from knowledge_base.scripts.audit_metadata.support.model import (
    RULE_ABSTRACT_DOLLAR_MATH,
    RULE_ABSTRACT_LATEX_ARTIFACT,
    RULE_ABSTRACT_PUBLISHER_MARK,
    RULE_ASCII_MULTI_DASH,
    RULE_AUTHOR_ASCII_NORMALIZATION,
    RULE_AUTHOR_MOJIBAKE,
    RULE_BIG_WHITESPACE,
    RULE_CLEARABLE_SUMMARY,
    RULE_DATABASE_DUPLICATE_TAG,
    RULE_DUPLICATE_TAG,
    RULE_ESCAPED_SEQUENCE,
    RULE_FOLDED_TEXT_FIELD,
    RULE_FORBIDDEN_TAG,
    RULE_GARBLED_MARKUP,
    RULE_HIGH_CONFIDENCE_OCR_ARTIFACT,
    RULE_MULTILINE_FIELD,
    RULE_NON_INDIVIDUAL_AUTHOR,
    RULE_PLURAL_DUPLICATE_TAG,
    RULE_SOURCE_YEAR,
    RULE_TAG_VALUE,
    RULE_TEXT_MOJIBAKE,
    RULE_TIGHT_LETTER_PARENTHETICAL_SPACING,
    RULE_TITLE_VALUE,
    RULE_TYPE_VALUE,
    Issue,
)
from knowledge_base.utils.normalization_db import tag_key

_LOW_SIGNAL_SUMMARY_ISSUE_PREFIX = "Low-signal generated summary"


def _issue_rule_or_legacy(issue: Issue, rule: str, legacy_match: bool) -> bool:
    return issue.rule == rule or (issue.rule is None and legacy_match)


def _is_escaped_sequence_issue(issue: Issue) -> bool:
    return _issue_rule_or_legacy(
        issue,
        RULE_ESCAPED_SEQUENCE,
        issue.message.startswith("Contains escaped HTML/entity sequence"),
    )


def _is_garbled_markup_issue(issue: Issue) -> bool:
    return _issue_rule_or_legacy(
        issue,
        RULE_GARBLED_MARKUP,
        issue.message.startswith("Contains likely garbled HTML/XML markup"),
    )


def _is_big_whitespace_issue(issue: Issue) -> bool:
    return _issue_rule_or_legacy(
        issue,
        RULE_BIG_WHITESPACE,
        issue.message.startswith(_BIG_WHITESPACE_ISSUE_PREFIX),
    )


def _is_tight_letter_parenthetical_spacing_issue(issue: Issue) -> bool:
    return _issue_rule_or_legacy(
        issue,
        RULE_TIGHT_LETTER_PARENTHETICAL_SPACING,
        issue.message.startswith(_TIGHT_LETTER_PAREN_ISSUE_PREFIX),
    )


def _is_ascii_multi_dash_issue(issue: Issue) -> bool:
    return _issue_rule_or_legacy(
        issue,
        RULE_ASCII_MULTI_DASH,
        issue.message.startswith(_ASCII_MULTI_DASH_ISSUE_PREFIX),
    )


def _is_title_value_fix_issue(issue: Issue) -> bool:
    return (
        issue.field == "title"
        and issue.suggestion is not None
        and _issue_rule_or_legacy(
            issue,
            RULE_TITLE_VALUE,
            issue.message.startswith(
                (
                    "Not in title case:",
                    "Contains title markup/math garbage:",
                    _TITLE_CHARACTER_ESCAPE_ISSUE_PREFIX,
                )
            ),
        )
    )


def _is_author_mojibake_issue(issue: Issue) -> bool:
    return issue.field == "authors" and _issue_rule_or_legacy(
        issue,
        RULE_AUTHOR_MOJIBAKE,
        issue.message.startswith(_AUTHOR_MOJIBAKE_ISSUE_PREFIX),
    )


def _is_author_ascii_normalization_issue(issue: Issue) -> bool:
    return issue.field == "authors" and _issue_rule_or_legacy(
        issue,
        RULE_AUTHOR_ASCII_NORMALIZATION,
        issue.message.startswith(_AUTHOR_ASCII_NORMALIZATION_ISSUE_PREFIX),
    )


def _is_fixable_author_name_issue(issue: Issue) -> bool:
    return _is_author_mojibake_issue(issue) or _is_author_ascii_normalization_issue(issue)


def _is_fixable_non_individual_author_issue(issue: Issue) -> bool:
    return issue.field == "authors" and _issue_rule_or_legacy(
        issue,
        RULE_NON_INDIVIDUAL_AUTHOR,
        issue.message.startswith(_NON_INDIVIDUAL_AUTHOR_ISSUE_PREFIX),
    )


def _is_publisher_mark_abstract_issue(issue: Issue) -> bool:
    return issue.field == "abstract" and _issue_rule_or_legacy(
        issue,
        RULE_ABSTRACT_PUBLISHER_MARK,
        issue.message.startswith(_PUBLISHER_MARK_ABSTRACT_ISSUE_PREFIX),
    )


def _is_abstract_dollar_math_issue(issue: Issue) -> bool:
    return issue.field == "abstract" and _issue_rule_or_legacy(
        issue,
        RULE_ABSTRACT_DOLLAR_MATH,
        issue.message.startswith(_ABSTRACT_DOLLAR_MATH_ISSUE_PREFIX),
    )


def _is_abstract_latex_artifact_issue(issue: Issue) -> bool:
    return issue.field == "abstract" and _issue_rule_or_legacy(
        issue,
        RULE_ABSTRACT_LATEX_ARTIFACT,
        issue.message.startswith(_ABSTRACT_LATEX_ARTIFACT_ISSUE_PREFIX),
    )


def _is_text_mojibake_issue(issue: Issue) -> bool:
    return _issue_rule_or_legacy(
        issue,
        RULE_TEXT_MOJIBAKE,
        issue.message.startswith(_TEXT_MOJIBAKE_ISSUE_PREFIX),
    )


def _is_type_fix_issue(issue: Issue) -> bool:
    return (
        issue.field == "type"
        and issue.suggestion in VALID_TYPES
        and _issue_rule_or_legacy(
            issue,
            RULE_TYPE_VALUE,
            issue.message.startswith("Invalid value"),
        )
    )


def _is_clearable_summary_issue(issue: Issue) -> bool:
    return issue.field == "summary" and _issue_rule_or_legacy(
        issue,
        RULE_CLEARABLE_SUMMARY,
        issue.message.startswith(
            (
                _SUMMARY_ABSTRACT_OVERLAP_ISSUE_PREFIX,
                _LOW_SIGNAL_SUMMARY_ISSUE_PREFIX,
            )
        ),
    )


def _is_high_confidence_ocr_artifact_issue(issue: Issue) -> bool:
    return _issue_rule_or_legacy(
        issue,
        RULE_HIGH_CONFIDENCE_OCR_ARTIFACT,
        issue.message.startswith(_HIGH_CONFIDENCE_OCR_ARTIFACT_ISSUE_PREFIX),
    )


def _is_source_year_issue(issue: Issue) -> bool:
    return (
        issue.field == "source"
        and issue.suggestion is not None
        and _issue_rule_or_legacy(
            issue,
            RULE_SOURCE_YEAR,
            issue.message.startswith("Contains year"),
        )
    )


def _is_multiline_field_issue(issue: Issue) -> bool:
    return issue.field in _MULTILINE_FORBIDDEN_FIELDS and _issue_rule_or_legacy(
        issue,
        RULE_MULTILINE_FIELD,
        issue.message.startswith("Field must be a single-line scalar"),
    )


def _is_folded_text_field_issue(issue: Issue) -> bool:
    return issue.field in _FOLDED_TEXT_FIELDS and _issue_rule_or_legacy(
        issue,
        RULE_FOLDED_TEXT_FIELD,
        issue.message.startswith(
            (
                _FOLDED_TEXT_FIELD_ISSUE_PREFIX,
                _FOLDED_TEXT_FIELD_MULTILINE_ISSUE_PREFIX,
                _FOLDED_TEXT_FIELD_BLANK_LINE_ISSUE_PREFIX,
            )
        ),
    )


def _is_plural_duplicate_tag_issue(issue: Issue) -> bool:
    return issue.field == "tags" and _issue_rule_or_legacy(
        issue,
        RULE_PLURAL_DUPLICATE_TAG,
        issue.message.startswith(_PLURAL_DUPLICATE_TAG_MESSAGE_PREFIX),
    )


def _is_database_duplicate_tag_issue(issue: Issue) -> bool:
    return issue.field == "tags" and _issue_rule_or_legacy(
        issue,
        RULE_DATABASE_DUPLICATE_TAG,
        issue.message.startswith(_DATABASE_DUPLICATE_TAG_MESSAGE_PREFIX),
    )


def _is_duplicate_tag_issue(issue: Issue) -> bool:
    return (
        issue.field == "tags"
        and _issue_rule_or_legacy(
            issue,
            RULE_DUPLICATE_TAG,
            issue.message.startswith(_DUPLICATE_TAG_MESSAGE_PREFIX),
        )
        and not _is_plural_duplicate_tag_issue(issue)
        and not _is_database_duplicate_tag_issue(issue)
    )


def _is_forbidden_tag_issue(issue: Issue) -> bool:
    return issue.field == "tags" and _issue_rule_or_legacy(
        issue,
        RULE_FORBIDDEN_TAG,
        issue.message.startswith("Forbidden tag at tags["),
    )


def _is_fixable_missing_tag_canonical_replacement(
    issue: Issue,
    added_canonical_tag_keys: set[str],
) -> bool:
    if not _is_tag_database_missing_issue(issue):
        return False
    if issue.suggestion is None or issue.suggestion.startswith("Add "):
        return False
    return tag_key(issue.suggestion) in added_canonical_tag_keys


def _is_fixable_tag_issue(issue: Issue) -> bool:
    if (
        _is_duplicate_tag_issue(issue)
        or _is_plural_duplicate_tag_issue(issue)
        or _is_database_duplicate_tag_issue(issue)
        or _is_forbidden_tag_issue(issue)
    ):
        return True

    return (
        issue.field == "tags"
        and issue.suggestion is not None
        and _issue_rule_or_legacy(
            issue,
            RULE_TAG_VALUE,
            issue.message.startswith(
                (
                    "Tag is not in capital case",
                    "Tag starts with an article",
                    _TAG_DATABASE_ISSUE_PREFIX,
                )
            ),
        )
    )


__all__ = [name for name in globals() if name.startswith("_") and not name.startswith("__")]
