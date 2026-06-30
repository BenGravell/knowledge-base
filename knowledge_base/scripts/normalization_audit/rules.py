"""Author, source, and tag normalization rules."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from knowledge_base.scripts.normalization_audit.io import load_metadata
from knowledge_base.scripts.normalization_audit.model import (
    RULE_AUTHOR_VALUE,
    RULE_SOURCE_VALUE,
    RULE_TAG_DATABASE_MISSING,
    RULE_TAG_VALUE,
    TAG_DATABASE_ISSUE_PREFIX,
    TAG_DATABASE_MISSING_PREFIX,
    Issue,
)
from knowledge_base.utils.normalization_db import (
    NormalizationIndex,
    ascii_clean,
    author_initial_last_key,
    author_key,
    author_uses_first_or_last_initial,
    build_index,
    canonical_author_display,
    canonical_source_display,
    expand_tag_acronyms,
    source_key,
    tag_key,
)


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def build_author_lookup(author_entries: list[dict[str, Any]]) -> tuple[NormalizationIndex, dict[str, set[str]]]:
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


def author_suggestion(name: str, index: NormalizationIndex, initial_index: dict[str, set[str]]) -> str | None:
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
    author_index: NormalizationIndex,
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
                rule=RULE_AUTHOR_VALUE,
                index=index,
            )
        )

    if author_uses_first_or_last_initial(author):
        issues.append(
            Issue(
                path,
                "authors",
                f"Author appears to use a first/last-name initial at authors[{index}]: {author!r}",
                suggestion,
                rule=RULE_AUTHOR_VALUE,
                index=index,
            )
        )

    if suggestion and ascii_clean(author) != suggestion:
        issues.append(
            Issue(
                path,
                "authors",
                f"Author spelling differs from normalization database at authors[{index}]: {author!r}",
                suggestion,
                rule=RULE_AUTHOR_VALUE,
                index=index,
            )
        )

    return issues


def audit_source(path: Path, source: str, source_index: NormalizationIndex) -> list[Issue]:
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
                rule=RULE_SOURCE_VALUE,
            )
        ]
    return []


def audit_tag(path: Path, tag: str, index: int, tag_index: NormalizationIndex) -> list[Issue]:
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
                rule=RULE_TAG_VALUE,
                index=index,
            )
        ]

    if suggestion is None:
        fallback = (
            expanded if expanded != tag else f"Add {tag!r} to normalization/tags.yml as a canonical tag or alias."
        )
        return [
            Issue(
                path,
                "tags",
                f"{TAG_DATABASE_MISSING_PREFIX} at tags[{index}]: {tag!r}",
                fallback,
                rule=RULE_TAG_DATABASE_MISSING,
                index=index,
            )
        ]
    return []


def normalized_tag_value(tag: str, tag_index: NormalizationIndex) -> str:
    suggestion = tag_index.lookup(tag_key(tag))
    if suggestion:
        return suggestion
    expanded = expand_tag_acronyms(tag)
    if expanded != tag:
        suggestion = tag_index.lookup(tag_key(expanded))
        if suggestion:
            return suggestion
    return tag


def audit_tag_duplicates(path: Path, tags: list[Any], tag_index: NormalizationIndex) -> list[Issue]:
    normalized_indexes: dict[str, list[int]] = {}
    for index, tag in enumerate(tags):
        normalized = normalized_tag_value(str(tag).strip(), tag_index)
        key = tag_key(normalized)
        if key:
            normalized_indexes.setdefault(key, []).append(index)

    duplicate_groups = {
        key: indexes
        for key, indexes in normalized_indexes.items()
        if len(indexes) > 1 and len({str(tags[index]).strip().casefold() for index in indexes}) > 1
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


def audit_file(
    path: Path,
    author_index: NormalizationIndex,
    initial_index: dict[str, set[str]],
    source_index: NormalizationIndex,
    tag_index: NormalizationIndex,
) -> tuple[dict[str, Any], list[Issue]]:
    data = load_metadata(path)
    issues: list[Issue] = []
    authors = data.get("authors")
    if isinstance(authors, list):
        for index, author in enumerate(authors):
            issues.extend(audit_author(path, str(author), index, author_index, initial_index))

    source = str(data.get("source") or "").strip()
    issues.extend(audit_source(path, source, source_index))
    tags = data.get("tags")
    if isinstance(tags, list):
        for index, tag in enumerate(tags):
            issues.extend(audit_tag(path, str(tag).strip(), index, tag_index))
        issues.extend(audit_tag_duplicates(path, tags, tag_index))
    return data, issues
