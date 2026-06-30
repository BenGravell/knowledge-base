"""YAML formatting helpers for metadata fixers."""

import json

import yaml

from knowledge_base.scripts.audit_metadata.fixes.yaml_spans import _TOP_LEVEL_SCALAR_FIELD_RE, _top_level_field_span
from knowledge_base.scripts.audit_metadata.rules.field_data import _FOLDED_TEXT_FIELDS
from knowledge_base.scripts.audit_metadata.support.text import _normalize_inline_text


def _format_folded_scalar_field(field_name: str, value: str, newline: str) -> str:
    text = _normalize_inline_text(value)
    if not text:
        return f"{field_name}:{newline}"
    return f"{field_name}: >{newline}  {text}{newline}"


def _format_metadata_list_block(
    field_name: str,
    value: list[object],
    newline: str,
) -> str:
    if not value:
        return f"{field_name}:{newline}"

    lines = [f"{field_name}:"]
    for item in value:
        if item is None or item == "":
            lines.append("  -")
            continue
        dumped = yaml.safe_dump(
            [item],
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
            width=1_000_000_000,
        ).strip()
        item_text = dumped.removeprefix("-").strip()
        lines.append(f"  - {item_text}")
    return newline.join(lines) + newline


def _format_metadata_scalar_line(
    field_name: str,
    value: object,
    newline: str = "\n",
) -> str:
    if value is None or value == "":
        return f"{field_name}:{newline}"

    if isinstance(value, str):
        value = _normalize_inline_text(value)
        if field_name in _FOLDED_TEXT_FIELDS:
            return _format_folded_scalar_field(field_name, value, newline)
        if field_name == "arxiv_id":
            return f"{field_name}: {json.dumps(value, ensure_ascii=False)}{newline}"

    if isinstance(value, list):
        return _format_metadata_list_block(field_name, value, newline)

    dumped = yaml.safe_dump(
        {field_name: value},
        sort_keys=False,
        allow_unicode=True,
        width=1_000_000_000,
    ).strip()
    return dumped + newline


def _fix_metadata_scalar_field_in_yaml(raw: str, field_name: str, new_value: object) -> str:
    lines = raw.splitlines(keepends=True)
    for start, _line in enumerate(lines):
        parsed = _top_level_field_span(lines, start)
        if parsed is None:
            continue

        current_field_name, _value, end = parsed
        if current_field_name != field_name:
            continue

        match = _TOP_LEVEL_SCALAR_FIELD_RE.match(_line)
        newline = match.group("newline") if match else "\n"
        replacement = _format_metadata_scalar_line(
            field_name,
            new_value,
            newline or "\n",
        )
        return "".join([*lines[:start], replacement, *lines[end:]])

    return raw


__all__ = [name for name in globals() if name.startswith("_") and not name.startswith("__")]
