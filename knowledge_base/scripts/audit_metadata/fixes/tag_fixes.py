"""YAML rewrite helpers for tag fields."""

import re

import yaml

from knowledge_base.scripts.audit_metadata.fixes.fix_predicates import (
    _is_database_duplicate_tag_issue,
    _is_duplicate_tag_issue,
    _is_forbidden_tag_issue,
    _is_plural_duplicate_tag_issue,
)
from knowledge_base.scripts.audit_metadata.fixes.yaml_spans import (
    _has_indented_continuation,
    _is_block_scalar_header,
    _is_multiline_quoted_scalar_header,
)
from knowledge_base.scripts.audit_metadata.rules.tag_duplicates import (
    _database_duplicate_tag_removal_indexes,
    _duplicate_tag_removal_indexes,
    _plural_duplicate_tag_removal_indexes,
)
from knowledge_base.scripts.audit_metadata.rules.tag_text import (
    _tag_issue_index,
)
from knowledge_base.scripts.audit_metadata.support.model import Issue


def _format_tags_block(tags: list[object], newline: str = "\n") -> str:
    if not tags:
        return f"tags:{newline}"

    lines = ["tags:"]
    for tag in tags:
        if tag is None or tag == "":
            lines.append("  -")
            continue
        dumped = yaml.safe_dump(
            [tag],
            sort_keys=False,
            allow_unicode=True,
            default_flow_style=False,
            width=1_000_000_000,
        ).strip()
        item = dumped.removeprefix("-").strip()
        lines.append(f"  - {item}")
    return newline.join(lines) + newline


def _fix_tags_in_yaml(
    raw: str,
    data: dict[str, object],
    tag_fixes: list[Issue],
) -> tuple[str, int]:
    tags_raw = data.get("tags")
    if not isinstance(tags_raw, list):
        return raw, 0

    tags = list(tags_raw)
    changed = 0
    for issue in tag_fixes:
        if (
            _is_duplicate_tag_issue(issue)
            or _is_plural_duplicate_tag_issue(issue)
            or _is_database_duplicate_tag_issue(issue)
            or _is_forbidden_tag_issue(issue)
        ):
            continue

        index = _tag_issue_index(issue)
        if index is None or index < 0 or index >= len(tags):
            continue
        if tags[index] == issue.suggestion:
            continue
        tags[index] = issue.suggestion
        changed += 1

    forbidden_tag_indexes = {
        index
        for issue in tag_fixes
        if _is_forbidden_tag_issue(issue)
        for index in [_tag_issue_index(issue)]
        if index is not None and 0 <= index < len(tags)
    }
    for index in sorted(forbidden_tag_indexes, reverse=True):
        del tags[index]
        changed += 1

    if any(_is_duplicate_tag_issue(issue) for issue in tag_fixes):
        for index in sorted(_duplicate_tag_removal_indexes(tags), reverse=True):
            del tags[index]
            changed += 1

    if any(_is_plural_duplicate_tag_issue(issue) for issue in tag_fixes):
        for index in sorted(_plural_duplicate_tag_removal_indexes(tags), reverse=True):
            del tags[index]
            changed += 1

    if any(_is_database_duplicate_tag_issue(issue) for issue in tag_fixes):
        for index in sorted(_duplicate_tag_removal_indexes(tags), reverse=True):
            del tags[index]
            changed += 1
        for index in sorted(_database_duplicate_tag_removal_indexes(tags), reverse=True):
            del tags[index]
            changed += 1

    if changed == 0:
        return raw, 0

    lines = raw.splitlines(keepends=True)
    for start, line in enumerate(lines):
        match = re.match(
            r"^(?P<indent>\s*)tags\s*:\s*(?P<value>.*?)(?P<newline>\r?\n)?$",
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
        elif not value.strip():
            while end < len(lines):
                next_line = lines[end]
                if not next_line.strip():
                    end += 1
                    continue
                if re.match(r"^-\s+", next_line):
                    end += 1
                    continue
                break

        replacement = match.group("indent") + _format_tags_block(
            tags,
            match.group("newline") or "\n",
        )
        return "".join([*lines[:start], replacement, *lines[end:]]), changed

    return raw, 0


__all__ = [name for name in globals() if name.startswith("_") and not name.startswith("__")]
