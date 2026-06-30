"""Tag duplicate detection helpers."""

import re

from knowledge_base.scripts.audit_metadata.rules.tag_data import _NON_PLURAL_S_ENDINGS, _NON_PLURAL_S_WORDS
from knowledge_base.scripts.audit_metadata.rules.tag_database import _tag_database_canonical
from knowledge_base.scripts.audit_metadata.rules.tag_text import (
    _normalized_tag_for_duplicate_check,
    _tag_part_is_abbreviation_or_mixed,
)
from knowledge_base.utils.normalization_db import tag_key


def _database_tag_duplicate_groups(tags: list[object]) -> dict[str, list[int]]:
    tag_indexes: dict[str, list[int]] = {}
    for index, tag_raw in enumerate(tags):
        tag = str(tag_raw).strip()
        if not tag:
            continue
        canonical = _tag_database_canonical(tag) or tag
        key = tag_key(canonical)
        if not key:
            continue
        tag_indexes.setdefault(key, []).append(index)

    return {
        key: indexes
        for key, indexes in tag_indexes.items()
        if len(indexes) > 1
        and len({_normalized_tag_for_duplicate_check(str(tags[index]).strip()) for index in indexes}) > 1
    }


def _preferred_database_duplicate_tag_index(tags: list[object], indexes: list[int]) -> int:
    def score(index: int) -> tuple[int, int]:
        tag = str(tags[index]).strip()
        canonical = _tag_database_canonical(tag)
        is_canonical = canonical is not None and tag == canonical
        return (0 if is_canonical else 1, index)

    return min(indexes, key=score)


def _database_duplicate_tag_removal_indexes(tags: list[object]) -> set[int]:
    remove_indexes: set[int] = set()
    for indexes in _database_tag_duplicate_groups(tags).values():
        keep_index = _preferred_database_duplicate_tag_index(tags, indexes)
        remove_indexes.update(index for index in indexes if index != keep_index)
    return remove_indexes


def _database_duplicate_tag_fix_suggestion(
    tags: list[object],
    groups: dict[str, list[int]],
) -> str:
    suggestions: list[str] = []
    for indexes in groups.values():
        keep_index = _preferred_database_duplicate_tag_index(tags, indexes)
        removals = [f"{str(tags[index]).strip()!r} at index {index}" for index in indexes if index != keep_index]
        canonical = _tag_database_canonical(str(tags[keep_index]).strip())
        canonical_note = f" as {canonical!r}" if canonical else ""
        suggestions.append(
            f"keep {str(tags[keep_index]).strip()!r} at index {keep_index}{canonical_note}; "
            f"remove {', '.join(removals)}"
        )
    return "Resolve aliases through normalization/tags.yml: " + "; ".join(suggestions)


def _duplicate_tag_groups(tags: list[object]) -> dict[str, list[int]]:
    tag_indexes: dict[str, list[int]] = {}
    for index, tag_raw in enumerate(tags):
        normalized = _normalized_tag_for_duplicate_check(str(tag_raw).strip())
        if normalized:
            tag_indexes.setdefault(normalized, []).append(index)

    return {key: indexes for key, indexes in tag_indexes.items() if len(indexes) > 1}


def _duplicate_tag_removal_indexes(tags: list[object]) -> set[int]:
    remove_indexes: set[int] = set()
    for indexes in _duplicate_tag_groups(tags).values():
        remove_indexes.update(indexes[1:])
    return remove_indexes


def _singularize_trivial_plural_word(word: str) -> str:
    folded = word.casefold()
    if not folded or _tag_part_is_abbreviation_or_mixed(word):
        return folded
    if folded in _NON_PLURAL_S_WORDS:
        return folded
    if len(folded) <= 3:
        return folded
    if folded.endswith("ies") and len(folded) > 4:
        return folded[:-3] + "y"
    if folded.endswith(("sses", "ches", "shes", "xes", "zes")) and len(folded) > 4:
        return folded[:-2]
    if folded.endswith("s") and not folded.endswith(_NON_PLURAL_S_ENDINGS):
        return folded[:-1]
    return folded


def _plural_insensitive_tag_key(tag: str) -> str:
    key = re.sub(
        r"[A-Za-z]+",
        lambda match: _singularize_trivial_plural_word(match.group(0)),
        tag,
    )
    return " ".join(key.split()).casefold()


def _plural_duplicate_tag_groups(tags: list[object]) -> dict[str, list[int]]:
    plural_tag_indexes: dict[str, list[int]] = {}
    normalized_tag_by_index: dict[int, str] = {}

    for index, tag_raw in enumerate(tags):
        tag = str(tag_raw).strip()
        normalized_tag = _normalized_tag_for_duplicate_check(tag)
        if not normalized_tag:
            continue

        normalized_tag_by_index[index] = normalized_tag
        plural_key = _plural_insensitive_tag_key(tag)
        if plural_key:
            plural_tag_indexes.setdefault(plural_key, []).append(index)

    return {
        key: indexes
        for key, indexes in plural_tag_indexes.items()
        if len(indexes) > 1 and len({normalized_tag_by_index[index] for index in indexes}) > 1
    }


def _preferred_plural_duplicate_tag_index(
    tags: list[object],
    plural_key: str,
    indexes: list[int],
) -> int:
    def score(index: int) -> tuple[int, int, int]:
        normalized = _normalized_tag_for_duplicate_check(str(tags[index]).strip())
        is_singular = normalized == plural_key
        return (0 if is_singular else 1, len(normalized), index)

    return min(indexes, key=score)


def _plural_duplicate_tag_removal_indexes(tags: list[object]) -> set[int]:
    remove_indexes: set[int] = set()
    for plural_key, indexes in _plural_duplicate_tag_groups(tags).items():
        keep_index = _preferred_plural_duplicate_tag_index(tags, plural_key, indexes)
        remove_indexes.update(index for index in indexes if index != keep_index)
    return remove_indexes


def _plural_duplicate_tag_fix_suggestion(
    tags: list[object],
    groups: dict[str, list[int]],
) -> str:
    suggestions: list[str] = []
    for plural_key, indexes in groups.items():
        keep_index = _preferred_plural_duplicate_tag_index(tags, plural_key, indexes)
        removals = [f"{str(tags[index]).strip()!r} at index {index}" for index in indexes if index != keep_index]
        suggestions.append(
            f"keep {str(tags[keep_index]).strip()!r} at index {keep_index}; remove {', '.join(removals)}"
        )

    return "Prefer singular spelling: " + "; ".join(suggestions)


__all__ = [name for name in globals() if name.startswith("_") and not name.startswith("__")]
