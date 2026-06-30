"""YAML loading and in-place scalar replacement helpers."""

from __future__ import annotations

import re
import textwrap
from pathlib import Path
from typing import Any

import yaml

from knowledge_base.config import VALID_FIELDS

TOP_LEVEL_FIELD_RE = re.compile(r"^(?P<key>[A-Za-z_][A-Za-z0-9_]*):(?P<value>[^\n\r]*)(?P<newline>\r?\n?)$")


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def dump_yaml(data: dict[str, Any]) -> str:
    lines: list[str] = []

    def add_scalar(key: str, value: Any) -> None:
        if value is None:
            lines.append(f"{key}:")
        elif key == "arxiv_id" and value:
            lines.append(f'{key}: "{value}"')
        elif isinstance(value, str) and ("\n" in value or len(value) > 80):
            lines.append(f"{key}: >")
            lines.extend(
                f"  {line}" for line in textwrap.wrap(value, width=100, break_long_words=False, break_on_hyphens=False)
            )
        elif isinstance(value, str):
            dumped = yaml.safe_dump({key: value}, sort_keys=False, allow_unicode=True).strip()
            lines.extend(dumped.splitlines())
        else:
            lines.append(f"{key}: {value}")

    for key in VALID_FIELDS:
        value = data.get(key)
        if isinstance(value, list):
            lines.append(f"{key}:")
            lines.extend(f"  - {item}" for item in value)
        else:
            add_scalar(key, value)

    return "\n".join(lines) + "\n"


def top_level_field_span(lines: list[str], start: int) -> tuple[str, str, int] | None:
    match = TOP_LEVEL_FIELD_RE.match(lines[start])
    if not match:
        return None

    field_name = match.group("key")
    value = match.group("value")
    end = start + 1
    if value.lstrip().startswith(("|", ">")) or (end < len(lines) and lines[end].startswith((" ", "\t"))):
        while end < len(lines):
            next_line = lines[end]
            if next_line.strip() and not next_line.startswith((" ", "\t")):
                break
            end += 1

    return field_name, value, end


def format_scalar_line(field_name: str, value: object, newline: str = "\n") -> str:
    if value is None or value == "":
        return f"{field_name}:{newline}"

    dumped = yaml.safe_dump(
        {field_name: value},
        sort_keys=False,
        allow_unicode=True,
        width=1_000_000_000,
    ).strip()
    return f"{dumped}{newline}"


def replace_scalar_field(raw: str, field_name: str, value: object) -> str:
    lines = raw.splitlines(keepends=True)
    for start, line in enumerate(lines):
        parsed = top_level_field_span(lines, start)
        if parsed is None:
            continue

        current_field, _current_value, end = parsed
        if current_field != field_name:
            continue

        match = TOP_LEVEL_FIELD_RE.match(line)
        newline = match.group("newline") if match else "\n"
        replacement = format_scalar_line(field_name, value, newline or "\n")
        return "".join([*lines[:start], replacement, *lines[end:]])

    prefix = raw if raw.endswith("\n") or not raw else f"{raw}\n"
    return f"{prefix}{format_scalar_line(field_name, value)}"
