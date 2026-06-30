"""Text-field YAML fix helpers."""

import re
from typing import Any

from knowledge_base.scripts.audit_metadata.fixes.yaml_rewrite import _fix_metadata_scalar_field_in_yaml
from knowledge_base.scripts.audit_metadata.fixes.yaml_spans import _top_level_field_span
from knowledge_base.scripts.audit_metadata.rules.abstract_data import _PUBLISHER_MARK_ABSTRACT_PATTERNS
from knowledge_base.scripts.audit_metadata.rules.encoding import _decode_utf8_mojibake_text
from knowledge_base.scripts.audit_metadata.rules.spacing_data import (
    _ASCII_MULTI_DASH_RE,
    _BIG_WHITESPACE_RE,
    _TIGHT_LETTER_PAREN_RE,
)
from knowledge_base.scripts.audit_metadata.rules.string_fields import (
    _is_text_spacing_field,
    _is_tight_letter_parenthetical_match,
    _walk_string_values,
)
from knowledge_base.scripts.audit_metadata.rules.text_quality import _apply_high_confidence_ocr_replacements
from knowledge_base.scripts.audit_metadata.rules.url_rules import _GARBLED_MARKUP_RE, _clean_garbled_markup_text
from knowledge_base.scripts.audit_metadata.support.text import _normalize_inline_text
from knowledge_base.scripts.audit_metadata.support.yaml_support import _yaml_safe_load


def _delete_publisher_marks_from_abstract(abstract: str) -> tuple[str, int]:
    cleaned = abstract
    removed = 0
    for _, pattern in _PUBLISHER_MARK_ABSTRACT_PATTERNS:
        cleaned, count = pattern.subn("", cleaned)
        removed += count

    if removed:
        cleaned = _normalize_inline_text(cleaned)
        cleaned = re.sub(r"\s+([,.;:])", r"\1", cleaned)
    return cleaned, removed


def _collapse_big_whitespace_after_indent(line: str) -> tuple[str, int]:
    match = re.match(
        r"^(?P<indent>[ \t]*)(?P<body>.*?)(?P<newline>\r?\n?)$",
        line,
    )
    if not match:
        return line, 0

    body = match.group("body")
    collapsed, count = _BIG_WHITESPACE_RE.subn(" ", body)
    if count == 0:
        return line, 0

    return match.group("indent") + collapsed + match.group("newline"), count


def _fix_big_whitespace_in_yaml(raw: str, fields: set[str]) -> tuple[str, int]:
    lines = raw.splitlines(keepends=True)
    changed = 0
    index = 0
    while index < len(lines):
        parsed = _top_level_field_span(lines, index)
        if parsed is None:
            index += 1
            continue

        field_name, _value, end = parsed
        if field_name not in fields:
            index = end
            continue

        for line_index in range(index, end):
            lines[line_index], count = _collapse_big_whitespace_after_indent(lines[line_index])
            changed += count

        index = end

    return "".join(lines), changed


def _replace_tight_letter_parenthetical_spacing(text: str) -> tuple[str, int]:
    changed = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal changed
        if not _is_tight_letter_parenthetical_match(match):
            return match.group(0)
        changed += 1
        return f"{match.group('left')} ({match.group('inner')})"

    return _TIGHT_LETTER_PAREN_RE.sub(replace, text), changed


def _fix_tight_letter_parenthetical_spacing_in_yaml(
    raw: str,
    data: dict[str, Any],
    fields: set[str],
) -> tuple[str, int]:
    fixed_raw = raw
    changed = 0
    for field_name in sorted(fields):
        if not _is_text_spacing_field(field_name):
            continue
        value = data.get(field_name)
        if isinstance(value, str):
            fixed_value, count = _replace_tight_letter_parenthetical_spacing(value)
            if count and fixed_value != value:
                fixed_raw = _fix_metadata_scalar_field_in_yaml(fixed_raw, field_name, fixed_value)
                data[field_name] = fixed_value
                changed += count
        elif isinstance(value, list):
            fixed_items = list(value)
            list_changed = 0
            for index, item in enumerate(fixed_items):
                if not isinstance(item, str):
                    continue
                fixed_item, count = _replace_tight_letter_parenthetical_spacing(item)
                if count and fixed_item != item:
                    fixed_items[index] = fixed_item
                    list_changed += count
            if list_changed:
                fixed_raw = _fix_metadata_scalar_field_in_yaml(fixed_raw, field_name, fixed_items)
                data[field_name] = fixed_items
                changed += list_changed

    return fixed_raw, changed


def _fix_ascii_multi_dash_in_yaml(
    raw: str,
    data: dict[str, Any],
    fields: set[str],
) -> tuple[str, int]:
    fixed_raw = raw
    changed = 0
    for field_name in sorted(fields):
        value = data.get(field_name)
        if isinstance(value, str):
            fixed_value, count = _replace_ascii_multi_dash_punctuation(value)
            if count and fixed_value != value:
                fixed_raw = _fix_metadata_scalar_field_in_yaml(fixed_raw, field_name, fixed_value)
                data[field_name] = fixed_value
                changed += count
        elif isinstance(value, list):
            fixed_items = list(value)
            list_changed = 0
            for index, item in enumerate(fixed_items):
                if not isinstance(item, str):
                    continue
                fixed_item, count = _replace_ascii_multi_dash_punctuation(item)
                if count and fixed_item != item:
                    fixed_items[index] = fixed_item
                    list_changed += count
            if list_changed:
                fixed_raw = _fix_metadata_scalar_field_in_yaml(fixed_raw, field_name, fixed_items)
                data[field_name] = fixed_items
                changed += list_changed

    return fixed_raw, changed


def _replace_ascii_multi_dash_punctuation(text: str) -> tuple[str, int]:
    changed = 0

    def replacement(match: re.Match[str]) -> str:
        nonlocal changed
        changed += 1
        if _is_tight_ascii_multi_dash_join(text, match):
            return "-"
        left = " " if match.start() > 0 and not text[match.start() - 1].isspace() else ""
        right = " " if match.end() < len(text) and not text[match.end()].isspace() else ""
        return f"{left}-{right}"

    return _ASCII_MULTI_DASH_RE.sub(replacement, text), changed


def _word_before(text: str, index: int) -> str:
    end = index + 1
    while index >= 0 and (text[index].isalnum() or text[index] in "'’"):
        index -= 1
    return text[index + 1 : end]


def _word_after(text: str, index: int) -> str:
    start = index
    while index < len(text) and (text[index].isalnum() or text[index] in "'’"):
        index += 1
    return text[start:index]


def _is_tight_ascii_multi_dash_join(text: str, match: re.Match[str]) -> bool:
    if match.start() == 0 or match.end() >= len(text):
        return False

    left_char = text[match.start() - 1]
    right_char = text[match.end()]
    if left_char.isspace() or right_char.isspace():
        return False
    if left_char.isdigit() and right_char.isdigit():
        return True

    left_word = _word_before(text, match.start() - 1)
    right_word = _word_after(text, match.end())
    if not left_word or not right_word:
        return False
    if left_word.casefold() == "tire" and right_word.casefold() == "road":
        return True
    return left_word[0].isupper() and right_word[0].isupper() and len(right_word) > 1


def _fix_garbled_markup_in_yaml(raw: str) -> tuple[str, int]:
    changed = 0
    data = _yaml_safe_load(raw)
    if not isinstance(data, dict):
        return raw, 0

    replacements: list[tuple[str, str]] = []
    for _, value in _walk_string_values(data, ""):
        if not isinstance(value, str) or not _GARBLED_MARKUP_RE.search(value):
            continue
        cleaned = _clean_garbled_markup_text(value)
        if cleaned and cleaned != value:
            replacements.append((value, cleaned))

    new_raw = raw
    for old, new in replacements:
        new_raw_next = new_raw.replace(old, new)
        if new_raw_next != new_raw:
            changed += new_raw.count(old)
            new_raw = new_raw_next

    return new_raw, changed


def _fix_high_confidence_ocr_artifacts_in_yaml(
    raw: str,
    data: dict[str, Any],
    fields: set[str],
) -> tuple[str, int]:
    fixed_raw = raw
    changed = 0
    for field_name in sorted(fields):
        value = data.get(field_name)
        if not isinstance(value, str):
            continue

        fixed_value, count = _apply_high_confidence_ocr_replacements(value)
        if not count or fixed_value == value:
            continue

        fixed_raw = _fix_metadata_scalar_field_in_yaml(fixed_raw, field_name, fixed_value)
        data[field_name] = fixed_value
        changed += count

    return fixed_raw, changed


def _fix_mojibake_text_fields_in_yaml(
    raw: str,
    data: dict[str, Any],
    fields: set[str],
) -> tuple[str, int]:
    fixed_raw = raw
    changed = 0
    for field_name in sorted(fields):
        value = data.get(field_name)
        if not isinstance(value, str):
            continue
        fixed_value, count = _decode_utf8_mojibake_text(value)
        if not count or fixed_value == value:
            continue
        fixed_raw = _fix_metadata_scalar_field_in_yaml(fixed_raw, field_name, fixed_value)
        data[field_name] = fixed_value
        changed += count
    return fixed_raw, changed


__all__ = [name for name in globals() if name.startswith("_") and not name.startswith("__")]
