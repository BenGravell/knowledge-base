"""Audit author/source/tag metadata against central normalization databases.

Usage:
  python scripts/audit_normalization.py
  python scripts/audit_normalization.py --file docs/papers/2021/2101.00000/metadata.yml
  python scripts/audit_normalization.py --fix
  python scripts/audit_normalization.py --format json

Create starter databases first with:
  python scripts/build_normalization_db.py
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from knowledge_base.config import KB_DIR  # noqa: E402
from knowledge_base.utils.normalization_db import (  # noqa: E402
    ascii_clean,
    author_initial_last_key,
    author_key,
    author_uses_first_or_last_initial,
    build_index,
    canonical_author_display,
    canonical_source_display,
    expand_tag_acronyms,
    load_yaml,
    parse_author,
    source_key,
    tag_key,
)


METADATA_ROOT = KB_DIR / "docs" / "papers"
NORMALIZATION_DIR = KB_DIR / "normalization"
AUTHORS_DB = NORMALIZATION_DIR / "authors.yml"
SOURCES_DB = NORMALIZATION_DIR / "sources.yml"
TAGS_DB = NORMALIZATION_DIR / "tags.yml"
TAG_DATABASE_ISSUE_PREFIX = "Tag differs from normalization database"
TAG_DATABASE_MISSING_PREFIX = "Tag is missing from normalization database"


@dataclass(frozen=True)
class Issue:
    path: Path
    field: str
    message: str
    suggestion: str | None = None


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def load_metadata(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    return data if isinstance(data, dict) else {}


def load_entries(path: Path, field: str) -> list[dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(path)
    entries = load_yaml(path).get(field)
    return [entry for entry in entries if isinstance(entry, dict)] if isinstance(entries, list) else []


def build_author_lookup(author_entries: list[dict[str, Any]]):
    index = build_index(author_entries, key_fn=author_key)
    initial_index: dict[str, set[str]] = {}
    for entry in author_entries:
        canonical = str(entry.get("canonical") or "").strip()
        if not canonical:
            continue
        key = author_initial_last_key(canonical)
        if key:
            initial_index.setdefault(key, set()).add(canonical)
    return index, initial_index


def author_suggestion(name: str, index, initial_index: dict[str, set[str]]) -> str | None:
    key = author_key(name)
    suggestion = index.lookup(key)
    if suggestion:
        return suggestion

    initial_key = author_initial_last_key(name)
    if initial_key:
        candidates = initial_index.get(initial_key, set())
        if len(candidates) == 1:
            return next(iter(candidates))

    return index.fuzzy(key, threshold=0.95)


def audit_author(
    path: Path,
    author: str,
    index: int,
    author_index,
    initial_index: dict[str, set[str]],
) -> list[Issue]:
    issues: list[Issue] = []
    clean_author = ascii_clean(author)
    suggestion = author_suggestion(author, author_index, initial_index)
    canonicalized = canonical_author_display(author)
    if suggestion is None and canonicalized != author:
        suggestion = canonicalized

    if clean_author != author:
        issues.append(
            Issue(
                path,
                "authors",
                f"Author has non-ASCII or compatibility characters at authors[{index}]: {author!r}",
                suggestion or clean_author,
            )
        )

    if author_uses_first_or_last_initial(author):
        issues.append(
            Issue(
                path,
                "authors",
                f"Author appears to use a first/last-name initial at authors[{index}]: {author!r}",
                suggestion,
            )
        )

    if suggestion and ascii_clean(author) != suggestion:
        issues.append(
            Issue(
                path,
                "authors",
                f"Author spelling differs from normalization database at authors[{index}]: {author!r}",
                suggestion,
            )
        )

    return issues


def audit_source(path: Path, source: str, source_index) -> list[Issue]:
    if not source:
        return []

    clean_source = canonical_source_display(source)
    suggestion = source_index.lookup(source_key(source))
    if suggestion is None:
        suggestion = source_index.fuzzy(source_key(source), threshold=0.94)
    if suggestion is None and clean_source != source:
        suggestion = clean_source

    if suggestion and clean_source != suggestion:
        return [
            Issue(
                path,
                "source",
                f"Source differs from normalization database: {source!r}",
                suggestion,
            )
        ]
    return []


def audit_tag(path: Path, tag: str, index: int, tag_index) -> list[Issue]:
    if not tag:
        return []

    suggestion = tag_index.lookup(tag_key(tag))
    expanded = expand_tag_acronyms(tag)
    if suggestion is None and expanded != tag:
        suggestion = tag_index.lookup(tag_key(expanded))

    if suggestion and tag != suggestion:
        return [
            Issue(
                path,
                "tags",
                f"{TAG_DATABASE_ISSUE_PREFIX} at tags[{index}]: {tag!r}",
                suggestion,
            )
        ]

    if suggestion is None:
        fallback = (
            expanded
            if expanded != tag
            else f"Add {tag!r} to normalization/tags.yml as a canonical tag or alias."
        )
        return [
            Issue(
                path,
                "tags",
                f"{TAG_DATABASE_MISSING_PREFIX} at tags[{index}]: {tag!r}",
                fallback,
            )
        ]
    return []


def normalized_tag_value(tag: str, tag_index) -> str:
    suggestion = tag_index.lookup(tag_key(tag))
    if suggestion:
        return suggestion
    expanded = expand_tag_acronyms(tag)
    if expanded != tag:
        suggestion = tag_index.lookup(tag_key(expanded))
        if suggestion:
            return suggestion
    return tag


def audit_tag_duplicates(path: Path, tags: list[Any], tag_index) -> list[Issue]:
    normalized_indexes: dict[str, list[int]] = {}
    for index, tag in enumerate(tags):
        normalized = normalized_tag_value(str(tag).strip(), tag_index)
        key = tag_key(normalized)
        if key:
            normalized_indexes.setdefault(key, []).append(index)

    duplicate_groups = {
        key: indexes
        for key, indexes in normalized_indexes.items()
        if len(indexes) > 1
        and len({str(tags[index]).strip().casefold() for index in indexes}) > 1
    }
    if not duplicate_groups:
        return []

    examples = ", ".join(
        ", ".join(f"{str(tags[index]).strip()!r} at index {index}" for index in indexes)
        for indexes in list(duplicate_groups.values())[:6]
    )
    if len(duplicate_groups) > 6:
        examples += f", ... ({len(duplicate_groups)} total)"
    return [
        Issue(
            path,
            "tags",
            f"Duplicate tag value(s) after tag database normalization: {examples}",
            "Replace aliases with canonical tags and remove duplicates.",
        )
    ]


def audit_file(path: Path, author_index, initial_index, source_index, tag_index) -> tuple[dict[str, Any], list[Issue]]:
    data = load_metadata(path)
    issues: list[Issue] = []
    authors = data.get("authors")
    if isinstance(authors, list):
        for index, author in enumerate(authors):
            issues.extend(
                audit_author(
                    path,
                    str(author),
                    index,
                    author_index,
                    initial_index,
                )
            )

    source = str(data.get("source") or "").strip()
    issues.extend(audit_source(path, source, source_index))
    tags = data.get("tags")
    if isinstance(tags, list):
        for index, tag in enumerate(tags):
            issues.extend(audit_tag(path, str(tag).strip(), index, tag_index))
        issues.extend(audit_tag_duplicates(path, tags, tag_index))
    return data, issues


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
            return "".join(lines[:start] + [replacement] + lines[end:])
    return raw


def issue_author_index(issue: Issue) -> int | None:
    match = re.search(r"authors\[(\d+)\]", issue.message)
    return int(match.group(1)) if match else None


def issue_tag_index(issue: Issue) -> int | None:
    match = re.search(r"tags\[(\d+)\]", issue.message)
    return int(match.group(1)) if match else None


def apply_fixes(results: list[tuple[Path, dict[str, Any], list[Issue]]]) -> int:
    fixed_files = 0
    for path, data, issues in results:
        raw = path.read_text(encoding="utf-8")
        new_raw = raw
        authors = list(data.get("authors") or []) if isinstance(data.get("authors"), list) else []
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

        tags = list(data.get("tags") or []) if isinstance(data.get("tags"), list) else []
        changed_tags = 0
        for issue in issues:
            if (
                issue.field != "tags"
                or issue.suggestion is None
                or not issue.message.startswith(TAG_DATABASE_ISSUE_PREFIX)
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


def relative_to_kb(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(KB_DIR.resolve()))
    except ValueError:
        return str(path)


def print_markdown(results: list[tuple[Path, dict[str, Any], list[Issue]]]) -> None:
    issue_count = sum(len(issues) for _, _, issues in results)
    print(f"# Normalization Audit\n\n{issue_count} issue(s) across {len(results)} file(s).\n")
    for path, _, issues in results:
        print(f"- `{relative_to_kb(path)}`")
        for issue in issues:
            print(f"  - [{issue.field}] {issue.message}")
            if issue.suggestion:
                print(f"    - Suggested: `{issue.suggestion}`")


def print_json(results: list[tuple[Path, dict[str, Any], list[Issue]]]) -> None:
    payload = [
        {
            "path": relative_to_kb(path),
            "issues": [
                {
                    "field": issue.field,
                    "message": issue.message,
                    "suggestion": issue.suggestion,
                }
                for issue in issues
            ],
        }
        for path, _, issues in results
    ]
    print(json.dumps(payload, indent=2, ensure_ascii=False))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Audit author/source/tag metadata against normalization databases."
    )
    parser.add_argument(
        "--file",
        metavar="PATH",
        help="Audit one metadata.yml file instead of all papers.",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format (default: markdown).",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Apply suggestions for authors/source/tag fields.",
    )
    args = parser.parse_args()

    try:
        author_entries = load_entries(AUTHORS_DB, "authors")
        source_entries = load_entries(SOURCES_DB, "sources")
        tag_entries = load_entries(TAGS_DB, "tags")
    except FileNotFoundError as exc:
        print(
            f"Missing normalization database: {exc.filename}. Run scripts/build_normalization_db.py first.",
            file=sys.stderr,
        )
        return 2

    author_index, initial_index = build_author_lookup(author_entries)
    source_index = build_index(source_entries, key_fn=source_key)
    tag_index = build_index(tag_entries, key_fn=tag_key)

    if args.file:
        targets = [Path(args.file)]
    else:
        targets = sorted(METADATA_ROOT.rglob("metadata.yml"))

    results: list[tuple[Path, dict[str, Any], list[Issue]]] = []
    for target in targets:
        data, issues = audit_file(target, author_index, initial_index, source_index, tag_index)
        if issues:
            results.append((target, data, issues))

    if not results:
        print(f"All {len(targets)} metadata.yml file(s) pass normalization audit.")
        return 0

    if args.format == "json":
        print_json(results)
    else:
        print_markdown(results)

    if args.fix:
        fixed_files = apply_fixes(results)
        print(f"\nFixed {fixed_files} file(s).")
        remaining = 0
        for target in targets:
            _, issues = audit_file(target, author_index, initial_index, source_index, tag_index)
            remaining += len(issues)
        return 1 if remaining else 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
