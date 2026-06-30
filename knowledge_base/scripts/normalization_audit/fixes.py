"""Apply normalization audit suggestions to metadata YAML."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

from knowledge_base.scripts.normalization_audit.model import RULE_TAG_VALUE, TAG_DATABASE_ISSUE_PREFIX, Issue
from knowledge_base.utils.normalization_db import tag_key


def _format_scalar_mapping(field: str, value: str, newline: str = "\n") -> str:
    dumped = yaml.safe_dump(
        {field: value},
        sort_keys=False,
        allow_unicode=False,
        width=1_000_000_000,
    ).strip()
    return dumped + newline


def _format_authors_block(authors: list[object], newline: str = "\n") -> str:
    if not authors:
        return f"authors:{newline}"
    lines = ["authors:"]
    for author in authors:
        if author is None or author == "":
            lines.append("  -")
            continue
        dumped = yaml.safe_dump(
            [str(author)],
            sort_keys=False,
            allow_unicode=False,
            default_flow_style=False,
            width=1_000_000_000,
        ).strip()
        item = dumped.removeprefix("-").strip()
        lines.append(f"  - {item}")
    return newline.join(lines) + newline


def _format_tags_block(tags: list[object], newline: str = "\n") -> str:
    if not tags:
        return f"tags:{newline}"
    lines = ["tags:"]
    for tag in tags:
        if tag is None or tag == "":
            lines.append("  -")
            continue
        dumped = yaml.safe_dump(
            [str(tag)],
            sort_keys=False,
            allow_unicode=False,
            default_flow_style=False,
            width=1_000_000_000,
        ).strip()
        item = dumped.removeprefix("-").strip()
        lines.append(f"  - {item}")
    return newline.join(lines) + newline


def _field_span(lines: list[str], start: int) -> tuple[str, str, int] | None:
    match = re.match(
        r"^(?P<key>[A-Za-z_][A-Za-z0-9_]*)\s*:\s*(?P<value>.*?)(?P<newline>\r?\n?)$",
        lines[start],
    )
    if not match:
        return None

    field = match.group("key")
    value = match.group("value")
    end = start + 1
    while end < len(lines):
        next_line = lines[end]
        if (
            next_line.strip()
            and not next_line.startswith((" ", "\t"))
            and not (not value.strip() and re.match(r"^-\s+", next_line))
        ):
            break
        end += 1
    return field, value, end


def _replace_field(raw: str, field: str, replacement: str) -> str:
    lines = raw.splitlines(keepends=True)
    for start in range(len(lines)):
        span = _field_span(lines, start)
        if span is None:
            continue
        span_field, _, end = span
        if span_field == field:
            return "".join([*lines[:start], replacement, *lines[end:]])
    return raw


def issue_author_index(issue: Issue) -> int | None:
    if issue.index is not None:
        return issue.index
    match = re.search(r"authors\[(\d+)\]", issue.message)
    return int(match.group(1)) if match else None


def issue_tag_index(issue: Issue) -> int | None:
    if issue.index is not None:
        return issue.index
    match = re.search(r"tags\[(\d+)\]", issue.message)
    return int(match.group(1)) if match else None


def issue_rule_or_legacy(issue: Issue, rule: str, legacy_match: bool) -> bool:
    return issue.rule == rule or (issue.rule is None and legacy_match)


def apply_fixes(results: list[tuple[Path, dict[str, Any], list[Issue]]]) -> int:
    fixed_files = 0
    for path, data, issues in results:
        raw = path.read_text(encoding="utf-8")
        new_raw = raw
        authors: list[Any] = list(data.get("authors") or []) if isinstance(data.get("authors"), list) else []
        changed_authors = 0
        for issue in issues:
            if issue.field != "authors" or issue.suggestion is None:
                continue
            index = issue_author_index(issue)
            if index is None or index >= len(authors):
                continue
            if authors[index] == issue.suggestion:
                continue
            authors[index] = issue.suggestion
            changed_authors += 1

        if changed_authors:
            new_raw = _replace_field(new_raw, "authors", _format_authors_block(authors))

        tags: list[Any] = list(data.get("tags") or []) if isinstance(data.get("tags"), list) else []
        changed_tags = 0
        for issue in issues:
            if (
                issue.field != "tags"
                or issue.suggestion is None
                or not issue_rule_or_legacy(
                    issue,
                    RULE_TAG_VALUE,
                    issue.message.startswith(TAG_DATABASE_ISSUE_PREFIX),
                )
            ):
                continue
            index = issue_tag_index(issue)
            if index is None or index >= len(tags):
                continue
            if tags[index] == issue.suggestion:
                continue
            tags[index] = issue.suggestion
            changed_tags += 1

        if changed_tags:
            deduped_tags: list[object] = []
            seen: set[str] = set()
            for tag in tags:
                key = tag_key(str(tag).strip())
                if key and key in seen:
                    continue
                if key:
                    seen.add(key)
                deduped_tags.append(tag)
            new_raw = _replace_field(new_raw, "tags", _format_tags_block(deduped_tags))

        source_issue = next(
            (issue for issue in issues if issue.field == "source" and issue.suggestion),
            None,
        )
        if source_issue is not None:
            new_raw = _replace_field(
                new_raw,
                "source",
                _format_scalar_mapping("source", source_issue.suggestion or ""),
            )

        if new_raw == raw:
            continue
        yaml.safe_load(new_raw)
        path.write_text(new_raw, encoding="utf-8")
        fixed_files += 1
        print(f"Fixed: {path}")
    return fixed_files
