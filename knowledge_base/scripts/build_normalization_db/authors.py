"""Build author normalization entries."""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any

from knowledge_base.utils.normalization_db import (
    ascii_clean,
    author_initial_last_key,
    author_key,
    canonical_author_display,
    entry_aliases,
    parse_author,
)


def author_quality(name: str, count: int) -> tuple[int, int, int, int, str]:
    parsed = parse_author(name)
    if parsed is None:
        return (0, 0, 0, count, name)
    no_edge_initials = int(not parsed.first_is_initial and not parsed.last_is_initial)
    ascii_only = int(ascii_clean(name) == name)
    middle_initials = sum(1 for part in parsed.middle if len(part.rstrip(".")) == 1)
    return (no_edge_initials, ascii_only, middle_initials, count, name)


def choose_author_canonical(names: list[str], counts: Counter[str]) -> str:
    best = max(names, key=lambda name: author_quality(name, counts[name]))
    return canonical_author_display(best)


def merge_aliases(canonical: str, values: list[str]) -> list[str]:
    aliases = {ascii_clean(value) for value in values if ascii_clean(value) and ascii_clean(value) != canonical}
    return sorted(aliases, key=str.casefold)


def build_author_entries(
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
            key_to_existing[author_key(value)] = canonical

    unmatched: dict[str, list[str]] = defaultdict(list)
    for value in values:
        key = author_key(value)
        canonical = key_to_existing.get(key)
        if canonical:
            canonical_to_values[canonical].add(value)
        else:
            unmatched[key].append(value)

    parsed_by_initial: dict[str, list[str]] = defaultdict(list)
    for names in unmatched.values():
        for name in names:
            key = author_initial_last_key(name)
            if key:
                parsed_by_initial[key].append(name)

    assigned: set[str] = set()
    for names in parsed_by_initial.values():
        parsed_names = [(name, parse_author(name)) for name in names]
        full_first_names = {
            parsed.first.casefold()
            for _, parsed in parsed_names
            if parsed is not None and not parsed.first_is_initial and not parsed.last_is_initial
        }
        if len(full_first_names) != 1:
            continue
        canonical = choose_author_canonical(names, values)
        canonical_to_values[canonical].update(names)
        assigned.update(names)

    for names in unmatched.values():
        remaining = [name for name in names if name not in assigned]
        if not remaining:
            continue
        canonical = choose_author_canonical(remaining, values)
        canonical_to_values[canonical].update(remaining)

    entries = []
    for canonical in sorted(canonical_to_values, key=str.casefold):
        aliases = merge_aliases(canonical, sorted(canonical_to_values[canonical]))
        entry: dict[str, Any] = {"canonical": canonical}
        if aliases:
            entry["aliases"] = aliases
        entries.append(entry)
    return entries
