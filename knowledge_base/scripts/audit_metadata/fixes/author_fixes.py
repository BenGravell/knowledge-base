"""YAML rewrite helpers for author fields."""

import re
from typing import Any

import yaml

from knowledge_base.scripts.audit_metadata.fixes.yaml_spans import (
    _has_indented_continuation,
    _is_block_scalar_header,
    _is_multiline_quoted_scalar_header,
)
from knowledge_base.scripts.audit_metadata.rules.author_rules import (
    _fold_author_name_to_ascii,
    _repair_non_individual_author_list,
)
from knowledge_base.scripts.audit_metadata.rules.encoding import _decode_utf8_mojibake_text


def _format_authors_block(authors: list[object], newline: str = "\n") -> str:
    if not authors:
        return f"authors:{newline}"

    lines = ["authors:"]
    for author in authors:
        if author is None or author == "":
            lines.append("  -")
            continue
        dumped = yaml.safe_dump(
            [author],
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
            width=1_000_000_000,
        ).strip()
        item = dumped.removeprefix("-").strip()
        lines.append(f"  - {item}")
    return newline.join(lines) + newline


def _fix_author_names_in_yaml(raw: str, data: dict[str, Any]) -> tuple[str, int, int]:
    authors_raw = data.get("authors")
    if not isinstance(authors_raw, list):
        return raw, 0, 0

    authors = list(authors_raw)
    changed_authors = 0
    decoded_sequences = 0
    for index, author in enumerate(authors):
        if not isinstance(author, str):
            continue

        decoded_author, count = _decode_utf8_mojibake_text(author)
        fixed_author = _fold_author_name_to_ascii(decoded_author)
        if not fixed_author or fixed_author == author:
            continue

        authors[index] = fixed_author
        changed_authors += 1
        decoded_sequences += count

    if changed_authors == 0:
        return raw, 0, 0

    lines = raw.splitlines(keepends=True)
    for start, line in enumerate(lines):
        match = re.match(
            r"^(?P<indent>\s*)authors\s*:\s*(?P<value>.*?)(?P<newline>\r?\n)?$",
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

        replacement = match.group("indent") + _format_authors_block(
            authors,
            match.group("newline") or "\n",
        )
        return (
            "".join([*lines[:start], replacement, *lines[end:]]),
            changed_authors,
            decoded_sequences,
        )

    return raw, 0, 0


def _fix_non_individual_authors_in_yaml(raw: str, data: dict[str, Any]) -> tuple[str, int]:
    authors_raw = data.get("authors")
    if not isinstance(authors_raw, list):
        return raw, 0
    authors, changed = _repair_non_individual_author_list(authors_raw)
    if not changed:
        return raw, 0

    lines = raw.splitlines(keepends=True)
    for start, line in enumerate(lines):
        match = re.match(
            r"^(?P<indent>\s*)authors\s*:\s*(?P<value>.*?)(?P<newline>\r?\n)?$",
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

        replacement = match.group("indent") + _format_authors_block(
            authors,
            match.group("newline") or "\n",
        )
        return "".join([*lines[:start], replacement, *lines[end:]]), changed

    return raw, 0


__all__ = [name for name in globals() if name.startswith("_") and not name.startswith("__")]
