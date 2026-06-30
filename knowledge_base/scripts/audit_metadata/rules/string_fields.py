"""String-field walking plus escaped/spacing/dash audit rules."""

# ruff: noqa: F811

import html
import re
from collections.abc import Iterator
from pathlib import Path
from typing import Any

from knowledge_base.scripts.audit_metadata.rules.spacing_data import (
    _ASCII_MULTI_DASH_ISSUE_PREFIX,
    _ASCII_MULTI_DASH_RE,
    _BIG_WHITESPACE_ISSUE_PREFIX,
    _BIG_WHITESPACE_RE,
    _TEXT_SPACING_EXCLUDED_FIELDS,
    _TIGHT_LETTER_PAREN_ISSUE_PREFIX,
    _TIGHT_LETTER_PAREN_RE,
    _TIGHT_PAREN_ALLOWED_PREFIXES,
)
from knowledge_base.scripts.audit_metadata.support.model import (
    RULE_ASCII_MULTI_DASH,
    RULE_BIG_WHITESPACE,
    RULE_ESCAPED_SEQUENCE,
    RULE_TIGHT_LETTER_PARENTHETICAL_SPACING,
    Issue,
    Path,
)
from knowledge_base.scripts.audit_metadata.support.text import _normalize_inline_text

_HTML_ENTITY_RE = re.compile(r"&(?:#[0-9]+|#x[0-9A-Fa-f]+|[A-Za-z][A-Za-z0-9]+);")

# ---------------------------------------------------------------------------
# Escaped-sequence helpers
# ---------------------------------------------------------------------------


def _html_unescape_repeated(text: str, max_rounds: int = 3) -> str:
    """Decode HTML entities, including values that were escaped more than once."""
    current = text
    for _ in range(max_rounds):
        decoded = _HTML_ENTITY_RE.sub(lambda m: html.unescape(m.group(0)), current)
        if decoded == current:
            break
        current = decoded.replace("\xa0", " ")
    return current


def _walk_string_values(value: Any, field_name: str) -> Iterator[tuple[str, str]]:
    if isinstance(value, str):
        yield field_name, value
    elif isinstance(value, list):
        for i, item in enumerate(value):
            yield from _walk_string_values(item, f"{field_name}[{i}]")
    elif isinstance(value, dict):
        for key, item in value.items():
            nested = f"{field_name}.{key}" if field_name else str(key)
            yield from _walk_string_values(item, nested)


def _metadata_field_root(field_name: str) -> str:
    return re.split(r"[.\[]", field_name, maxsplit=1)[0]


def _is_text_spacing_field(field_name: str) -> bool:
    return _metadata_field_root(field_name) not in _TEXT_SPACING_EXCLUDED_FIELDS


def _big_whitespace_examples(text: str, *, limit: int = 5) -> list[str]:
    examples: list[str] = []
    seen: set[str] = set()
    for match in _BIG_WHITESPACE_RE.finditer(text):
        left = _normalize_inline_text(text[max(0, match.start() - 40) : match.start()])
        right = _normalize_inline_text(text[match.end() : match.end() + 40])
        example = f"{left} [{len(match.group(0))} spaces] {right}".strip()
        if example in seen:
            continue
        examples.append(example)
        seen.add(example)
        if len(examples) >= limit:
            break
    return examples


def _is_tight_letter_parenthetical_match(match: re.Match[str]) -> bool:
    left = match.group("left")
    inner = match.group("inner")
    if len(left) < 3 or left.isupper():
        return False
    if any(char.isdigit() or char.isupper() for char in left[1:]):
        return False
    if re.search(r"\b(?:O|Theta|Omega)\($", match.string[: match.start()]):
        return False
    if left.casefold() in _TIGHT_PAREN_ALLOWED_PREFIXES:
        return False
    return any(char.isupper() for char in inner)


def _iter_tight_letter_parenthetical_matches(text: str):
    for match in _TIGHT_LETTER_PAREN_RE.finditer(text):
        if _is_tight_letter_parenthetical_match(match):
            yield match


def _tight_letter_parenthetical_examples(text: str, *, limit: int = 5) -> list[str]:
    examples: list[str] = []
    seen: set[str] = set()
    for match in _iter_tight_letter_parenthetical_matches(text):
        left = _normalize_inline_text(text[max(0, match.start() - 40) : match.start()])
        right = _normalize_inline_text(text[match.end() : match.end() + 40])
        example = f"{left} [{match.group(0)}] {right}".strip()
        if example in seen:
            continue
        examples.append(example)
        seen.add(example)
        if len(examples) >= limit:
            break
    return examples


def _ascii_multi_dash_examples(text: str, *, limit: int = 5) -> list[str]:
    examples: list[str] = []
    seen: set[str] = set()
    for match in _ASCII_MULTI_DASH_RE.finditer(text):
        left = _normalize_inline_text(text[max(0, match.start() - 40) : match.start()])
        right = _normalize_inline_text(text[match.end() : match.end() + 40])
        example = f"{left} [{match.group(0)}] {right}".strip()
        if example in seen:
            continue
        examples.append(example)
        seen.add(example)
        if len(examples) >= limit:
            break
    return examples


def find_ascii_multi_dash_issues(path: Path, data: dict[str, Any]) -> list["Issue"]:
    issues: list[Issue] = []
    for field_name, value in _walk_string_values(data, ""):
        examples = _ascii_multi_dash_examples(value)
        if not examples:
            continue

        message = _ASCII_MULTI_DASH_ISSUE_PREFIX
        if examples:
            message += ": " + "; ".join(repr(example) for example in examples)
        issues.append(
            Issue(
                path,
                field_name,
                message,
                (
                    "Replace ASCII multi-dash punctuation with a single dash, "
                    "using a tight hyphen for compounds/ranges and spaces for "
                    "phrase breaks."
                ),
                rule=RULE_ASCII_MULTI_DASH,
            )
        )
    return issues


def find_tight_letter_parenthetical_spacing_issues(
    path: Path,
    data: dict[str, Any],
) -> list["Issue"]:
    issues: list[Issue] = []
    for field_name, value in _walk_string_values(data, ""):
        if not _is_text_spacing_field(field_name):
            continue
        examples = _tight_letter_parenthetical_examples(value)
        if not examples:
            continue

        message = _TIGHT_LETTER_PAREN_ISSUE_PREFIX
        if examples:
            message += ": " + "; ".join(repr(example) for example in examples)
        issues.append(
            Issue(
                path,
                field_name,
                message,
                ("Insert a space before parenthetical abbreviations, for example 'Method (ABC)'."),
                rule=RULE_TIGHT_LETTER_PARENTHETICAL_SPACING,
            )
        )
    return issues


def find_big_whitespace_issues(path: Path, data: dict[str, Any]) -> list["Issue"]:
    issues: list[Issue] = []
    for field_name, value in _walk_string_values(data, ""):
        examples = _big_whitespace_examples(value)
        if not examples:
            continue

        message = _BIG_WHITESPACE_ISSUE_PREFIX
        if examples:
            message += ": " + "; ".join(repr(example) for example in examples)
        issues.append(
            Issue(
                path,
                field_name,
                message,
                "Collapse accidental spacing to one space unless the spacing is semantically meaningful.",
                rule=RULE_BIG_WHITESPACE,
            )
        )
    return issues


def find_escaped_sequence_issues(path: Path, data: dict[str, Any]) -> list["Issue"]:
    issues: list[Issue] = []
    for field_name, value in _walk_string_values(data, ""):
        matches = sorted(set(_HTML_ENTITY_RE.findall(value)))
        if not matches:
            continue

        examples = ", ".join(matches[:5])
        if len(matches) > 5:
            examples += f", ... ({len(matches)} total)"
        decoded_examples = ", ".join(f"{match} decodes to {_html_unescape_repeated(match)!r}" for match in matches[:3])
        issues.append(
            Issue(
                path,
                field_name,
                f"Contains escaped HTML/entity sequence(s): {examples}",
                decoded_examples,
                rule=RULE_ESCAPED_SEQUENCE,
            )
        )
    return issues
