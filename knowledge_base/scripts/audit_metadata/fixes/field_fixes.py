"""YAML rewrite helpers for scalar metadata fields."""

import re
from typing import Any

import yaml

from knowledge_base.scripts.audit_metadata.fixes.yaml_rewrite import (
    _fix_metadata_scalar_field_in_yaml,
    _format_metadata_scalar_line,
)
from knowledge_base.scripts.audit_metadata.fixes.yaml_spans import (
    _TOP_LEVEL_SCALAR_FIELD_RE,
    _has_indented_continuation,
    _is_block_scalar_header,
    _is_multiline_quoted_scalar_header,
    _top_level_field_span,
)
from knowledge_base.scripts.audit_metadata.rules.field_data import _MULTILINE_FORBIDDEN_FIELDS


def _format_source_line(source: str, newline: str = "\n") -> str:
    dumped = yaml.safe_dump(
        {"source": source},
        sort_keys=False,
        allow_unicode=True,
        width=1_000_000_000,
    ).strip()
    return dumped + newline


def _fix_source_in_yaml(raw: str, new_source: str) -> str:
    lines = raw.splitlines(keepends=True)
    for start, line in enumerate(lines):
        match = re.match(
            r"^(?P<indent>\s*)source\s*:\s*(?P<value>.*?)(?P<newline>\r?\n)?$",
            line,
        )
        if not match:
            continue

        end = start + 1
        value = match.group("value")
        if (
            _is_block_scalar_header(value)
            or _is_multiline_quoted_scalar_header(value)
            or _has_indented_continuation(lines, start)
        ):
            while end < len(lines):
                next_line = lines[end]
                if next_line.strip() and not next_line.startswith((" ", "\t")):
                    break
                end += 1

        replacement = match.group("indent") + _format_source_line(new_source, match.group("newline") or "\n")
        return "".join([*lines[:start], replacement, *lines[end:]])

    return raw


def _fix_multiline_fields_in_yaml(
    raw: str,
    data: dict[str, Any],
    fields: set[str],
) -> tuple[str, int]:
    lines = raw.splitlines(keepends=True)
    changed = 0
    index = 0
    while index < len(lines):
        parsed = _top_level_field_span(lines, index)
        if parsed is None:
            index += 1
            continue

        field_name, value, end = parsed
        if (
            field_name in fields
            and field_name in _MULTILINE_FORBIDDEN_FIELDS
            and (end > index + 1 or _is_block_scalar_header(value))
        ):
            match = _TOP_LEVEL_SCALAR_FIELD_RE.match(lines[index])
            newline = match.group("newline") if match else "\n"
            replacement = _format_metadata_scalar_line(
                field_name,
                data.get(field_name),
                newline or "\n",
            )
            lines[index:end] = [replacement]
            changed += 1
            index += 1
            continue

        index = end

    return "".join(lines), changed


def _fix_folded_text_fields_in_yaml(
    raw: str,
    data: dict[str, Any],
    fields: set[str],
) -> tuple[str, list[str]]:
    fixed_raw = raw
    changed_fields: list[str] = []
    for field_name in sorted(fields):
        value = data.get(field_name)
        if not isinstance(value, str) or not value.strip():
            continue
        new_raw = _fix_metadata_scalar_field_in_yaml(fixed_raw, field_name, value)
        if new_raw != fixed_raw:
            fixed_raw = new_raw
            changed_fields.append(field_name)
    return fixed_raw, changed_fields


__all__ = [name for name in globals() if name.startswith("_") and not name.startswith("__")]
