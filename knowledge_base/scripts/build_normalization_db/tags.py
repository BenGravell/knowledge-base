"""Build tag normalization entries."""

from __future__ import annotations

import re
from collections import Counter, defaultdict
from typing import Any

from knowledge_base.scripts.build_normalization_db.authors import merge_aliases
from knowledge_base.utils.normalization_db import entry_aliases, expand_tag_acronyms, tag_dedupe_key, tag_key


def _is_short_acronym_tag(tag: str) -> bool:
    return bool(re.fullmatch(r"[A-Z0-9][A-Z0-9+./#*-]{1,}(?:\s+[A-Z0-9+./#*-]+)?", tag))


def _tag_canonical_score(tag: str, counts: Counter[str]) -> tuple[int, int, int, int, str]:
    expanded = expand_tag_acronyms(tag)
    uses_full_spelling = int(expanded == tag and not _is_short_acronym_tag(tag))
    capitalized = int(tag[:1].isupper() and tag[1:] != tag[1:].upper())
    return (uses_full_spelling, capitalized, counts[tag], -len(tag), tag)


def choose_tag_canonical(values: list[str], counts: Counter[str]) -> str:
    expanded_values = [expand_tag_acronyms(value) for value in values]
    candidates = sorted({*values, *expanded_values})
    for value in expanded_values:
        if value not in counts:
            counts[value] += sum(counts[raw] for raw in values if expand_tag_acronyms(raw) == value)
    return max(candidates, key=lambda tag: _tag_canonical_score(tag, counts)).strip()


def build_tag_entries(
    values: Counter[str],
    *,
    existing: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    canonical_to_values: dict[str, set[str]] = defaultdict(set)
    key_to_existing: dict[str, str] = {}
    for entry in existing:
        canonical = str(entry.get("canonical") or "").strip()
        if not canonical:
            continue
        canonical_to_values[canonical].add(canonical)
        for alias in entry_aliases(entry):
            canonical_to_values[canonical].add(alias)
        for value in canonical_to_values[canonical]:
            key_to_existing[tag_key(value)] = canonical

    unmatched: dict[str, list[str]] = defaultdict(list)
    counts = Counter(values)
    for value in values:
        expanded = expand_tag_acronyms(value)
        canonical = key_to_existing.get(tag_key(value))
        if canonical is None and expanded != value:
            canonical = key_to_existing.get(tag_key(expanded))
        if canonical:
            canonical_to_values[canonical].add(value)
            if expanded != value:
                canonical_to_values[canonical].add(expanded)
            continue

        dedupe_key = tag_dedupe_key(expanded)
        unmatched[dedupe_key].append(value)
        if expanded != value:
            unmatched[dedupe_key].append(expanded)
            counts[expanded] += values[value]

    for names in unmatched.values():
        unique_names = sorted(set(names))
        canonical = choose_tag_canonical(unique_names, counts)
        canonical_to_values[canonical].update(unique_names)

    entries = []
    for canonical in sorted(canonical_to_values, key=tag_key):
        aliases = merge_aliases(canonical, sorted(canonical_to_values[canonical]))
        entry: dict[str, Any] = {"canonical": canonical}
        if aliases:
            entry["aliases"] = aliases
        entries.append(entry)
    return entries
