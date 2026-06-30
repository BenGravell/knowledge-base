"""Shared metadata audit result models and rule identifiers."""

from dataclasses import dataclass
from dataclasses import field as dc_field
from enum import Enum
from pathlib import Path

# ---------------------------------------------------------------------------
# Issue dataclass
# ---------------------------------------------------------------------------


class Severity(Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


_SEVERITY_RANK = {
    Severity.INFO: 0,
    Severity.WARNING: 1,
    Severity.ERROR: 2,
}


@dataclass
class Issue:
    path: Path
    field: str
    message: str
    suggestion: str | None = None
    severity: Severity = dc_field(default=Severity.ERROR)
    rule: str | None = None
    index: int | None = None


RULE_TITLE_VALUE = "title.value"
RULE_ESCAPED_SEQUENCE = "text.escaped-sequence"
RULE_GARBLED_MARKUP = "text.garbled-markup"
RULE_BIG_WHITESPACE = "text.big-whitespace"
RULE_TIGHT_LETTER_PARENTHETICAL_SPACING = "text.tight-letter-parenthetical-spacing"
RULE_ASCII_MULTI_DASH = "text.ascii-multi-dash"
RULE_AUTHOR_MOJIBAKE = "authors.mojibake"
RULE_AUTHOR_ASCII_NORMALIZATION = "authors.ascii-normalization"
RULE_NON_INDIVIDUAL_AUTHOR = "authors.non-individual"
RULE_ABSTRACT_PUBLISHER_MARK = "abstract.publisher-mark"
RULE_ABSTRACT_DOLLAR_MATH = "abstract.dollar-math"
RULE_ABSTRACT_LATEX_ARTIFACT = "abstract.latex-artifact"
RULE_TEXT_MOJIBAKE = "text.mojibake"
RULE_TYPE_VALUE = "type.value"
RULE_CLEARABLE_SUMMARY = "summary.clearable"
RULE_HIGH_CONFIDENCE_OCR_ARTIFACT = "text.high-confidence-ocr-artifact"
RULE_SOURCE_YEAR = "source.year"
RULE_MULTILINE_FIELD = "field.multiline"
RULE_FOLDED_TEXT_FIELD = "field.folded-text"
RULE_TAG_DATABASE_MISSING = "tags.database-missing"
RULE_TAG_VALUE = "tags.value"
RULE_FORBIDDEN_TAG = "tags.forbidden"
RULE_DUPLICATE_TAG = "tags.duplicate"
RULE_PLURAL_DUPLICATE_TAG = "tags.plural-duplicate"
RULE_DATABASE_DUPLICATE_TAG = "tags.database-duplicate"


@dataclass
class PathFix:
    old_path: Path
    new_path: Path
    old_rel: str
    new_rel: str


@dataclass(frozen=True)
class TagCanonicalFix:
    canonical: str
    aliases: tuple[str, ...] = ()
