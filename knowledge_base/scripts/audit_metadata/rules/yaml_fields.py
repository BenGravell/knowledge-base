"""YAML field-shape audit rules."""

import re
from pathlib import Path
from typing import Any

from knowledge_base.scripts.audit_metadata.fixes.yaml_spans import _is_block_scalar_header, _top_level_field_span
from knowledge_base.scripts.audit_metadata.rules.field_data import (
    _FOLDED_TEXT_FIELD_BLANK_LINE_ISSUE_PREFIX,
    _FOLDED_TEXT_FIELD_ISSUE_PREFIX,
    _FOLDED_TEXT_FIELD_MULTILINE_ISSUE_PREFIX,
    _FOLDED_TEXT_FIELDS,
    _MULTILINE_FORBIDDEN_FIELDS,
    _TITLE_CHARACTER_ESCAPE_ISSUE_PREFIX,
)
from knowledge_base.scripts.audit_metadata.support.model import (
    RULE_FOLDED_TEXT_FIELD,
    RULE_MULTILINE_FIELD,
    RULE_TITLE_VALUE,
    Issue,
)

_YAML_CHARACTER_ESCAPE_RE = re.compile(r"\\(?:x[0-9A-Fa-f]{2}|u[0-9A-Fa-f]{4}|U[0-9A-Fa-f]{8})")


def _is_folded_scalar_header(value: str) -> bool:
    return value.lstrip().startswith(">")


def _nonblank_content_line_count(lines: list[str], start: int, end: int) -> int:
    return sum(1 for line in lines[start + 1 : end] if line.strip())


def _blank_content_line_count(lines: list[str], start: int, end: int) -> int:
    return sum(1 for line in lines[start + 1 : end] if not line.strip())


def find_multiline_field_issues(path: Path, raw: str, data: dict[str, Any]) -> list[Issue]:
    issues: list[Issue] = []
    lines = raw.splitlines(keepends=True)
    for index, _line in enumerate(lines):
        parsed = _top_level_field_span(lines, index)
        if parsed is None:
            continue

        field_name, value, end = parsed
        if field_name in _FOLDED_TEXT_FIELDS:
            field_value = data.get(field_name)
            if isinstance(field_value, str) and field_value.strip() and not _is_folded_scalar_header(value):
                issues.append(
                    Issue(
                        path,
                        field_name,
                        f"{_FOLDED_TEXT_FIELD_ISSUE_PREFIX}: {field_name}",
                        "Use the `field: >` newline pattern with indented text.",
                        rule=RULE_FOLDED_TEXT_FIELD,
                    )
                )
            elif isinstance(field_value, str) and field_value.strip() and _is_folded_scalar_header(value):
                content_line_count = _nonblank_content_line_count(lines, index, end)
                blank_line_count = _blank_content_line_count(lines, index, end)
                if content_line_count > 1:
                    issues.append(
                        Issue(
                            path,
                            field_name,
                            (
                                f"{_FOLDED_TEXT_FIELD_MULTILINE_ISSUE_PREFIX}: "
                                f"{field_name} spans {content_line_count} YAML "
                                "content line(s)"
                            ),
                            f"Collapse the text to one indented line under `{field_name}: >`.",
                            rule=RULE_FOLDED_TEXT_FIELD,
                        )
                    )
                elif blank_line_count:
                    issues.append(
                        Issue(
                            path,
                            field_name,
                            (
                                f"{_FOLDED_TEXT_FIELD_BLANK_LINE_ISSUE_PREFIX}: "
                                f"{field_name} contains {blank_line_count} blank "
                                "YAML content line(s)"
                            ),
                            f"Remove blank lines from the folded `{field_name}: >` block.",
                            rule=RULE_FOLDED_TEXT_FIELD,
                        )
                    )
            continue

        if field_name not in _MULTILINE_FORBIDDEN_FIELDS:
            continue

        if end > index + 1 or _is_block_scalar_header(value):
            issues.append(
                Issue(
                    path,
                    field_name,
                    f"Field must be a single-line scalar but spans {end - index} YAML line(s)",
                    rule=RULE_MULTILINE_FIELD,
                )
            )

    return issues


def _top_level_field_raw(raw: str, target_field: str) -> str | None:
    lines = raw.splitlines(keepends=True)
    index = 0
    while index < len(lines):
        parsed = _top_level_field_span(lines, index)
        if parsed is None:
            index += 1
            continue

        field_name, _, end = parsed
        if field_name == target_field:
            return "".join(lines[index:end])
        index = end

    return None


def _decode_yaml_character_escape(sequence: str) -> str | None:
    prefix = sequence[1]
    digits = sequence[2:]
    if prefix not in {"x", "u", "U"}:
        return None

    try:
        codepoint = int(digits, 16)
        return chr(codepoint)
    except ValueError:
        return None


def find_title_character_escape_issues(
    path: Path,
    raw: str,
    fixed_title: str,
) -> list[Issue]:
    title_raw = _top_level_field_raw(raw, "title")
    if title_raw is None:
        return []

    matches = sorted(set(_YAML_CHARACTER_ESCAPE_RE.findall(title_raw)))
    if not matches:
        return []

    examples = ", ".join(matches[:5])
    if len(matches) > 5:
        examples += f", ... ({len(matches)} total)"

    decoded: list[str] = []
    for match in matches[:3]:
        decoded_char = _decode_yaml_character_escape(match)
        if decoded_char is None:
            decoded.append(f"{match} is not a valid Unicode scalar value")
        else:
            decoded.append(f"{match} decodes to {decoded_char!r}")
    decoded_note = f" ({'; '.join(decoded)})" if decoded else ""

    return [
        Issue(
            path,
            "title",
            f"{_TITLE_CHARACTER_ESCAPE_ISSUE_PREFIX}: {examples}{decoded_note}",
            fixed_title,
            rule=RULE_TITLE_VALUE,
        )
    ]


__all__ = [name for name in globals() if not (name.startswith("__") and name.endswith("__"))]
