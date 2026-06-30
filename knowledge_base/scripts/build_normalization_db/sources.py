"""Build source normalization entries."""

from __future__ import annotations

from collections import Counter, defaultdict
from typing import Any

from knowledge_base.scripts.build_normalization_db.authors import merge_aliases
from knowledge_base.utils.normalization_db import canonical_source_display, entry_aliases, source_key


def build_source_entries(
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
            key_to_existing[source_key(value)] = canonical

    unmatched: dict[str, list[str]] = defaultdict(list)
    for value in values:
        key = source_key(value)
        canonical = key_to_existing.get(key)
        if canonical:
            canonical_to_values[canonical].add(value)
        else:
            unmatched[key].append(value)

    for names in unmatched.values():
        best = max(names, key=lambda name: (values[name], len(name), name))
        canonical = canonical_source_display(best)
        canonical_to_values[canonical].update(names)

    entries = []
    for canonical in sorted(canonical_to_values, key=str.casefold):
        aliases = merge_aliases(canonical, sorted(canonical_to_values[canonical]))
        entry: dict[str, Any] = {"canonical": canonical}
        if aliases:
            entry["aliases"] = aliases
        entries.append(entry)
    return entries
