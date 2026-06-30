"""Tag normalization database helpers."""

from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

from knowledge_base.scripts.audit_metadata.rules.tag_casing import (
    _author_last_name_tag_proper_words,
    _suggest_tag_capitalization,
    _suggest_tag_without_leading_article,
)
from knowledge_base.scripts.audit_metadata.rules.tag_data import (
    _MAX_TAG_WORDS,
    _TAG_DATABASE_MISSING_ISSUE_PREFIX,
    _TAGS_DB,
    _TAGS_DB_HEADER,
    _URL_RE,
)
from knowledge_base.scripts.audit_metadata.rules.tag_text import (
    _forbidden_tag_reason,
    _is_long_tag_allowed,
    _issue_rule_or_legacy,
    _sentence_like_tag_reason,
    _tag_issue_index,
    _tag_word_count,
)
from knowledge_base.scripts.audit_metadata.support.model import RULE_TAG_DATABASE_MISSING, Issue, TagCanonicalFix
from knowledge_base.scripts.audit_metadata.support.text import _normalize_inline_text
from knowledge_base.scripts.audit_metadata.support.yaml_support import _yaml_safe_load
from knowledge_base.utils.normalization_db import build_index, dump_yaml, expand_tag_acronyms, load_yaml, tag_key


@lru_cache(maxsize=1)
def _tag_normalization_index():
    try:
        data = load_yaml(_TAGS_DB)
    except FileNotFoundError:
        return None, f"Missing tag normalization database: {_TAGS_DB}"
    except yaml.YAMLError as exc:
        return None, f"Could not parse tag normalization database {_TAGS_DB}: {exc}"

    entries = data.get("tags")
    if not isinstance(entries, list):
        return None, f"Tag normalization database has no list field: {_TAGS_DB}"
    tag_entries = [entry for entry in entries if isinstance(entry, dict)]
    return build_index(tag_entries, key_fn=tag_key), None


def _tag_database_error() -> str | None:
    _, error = _tag_normalization_index()
    return error


def _tag_database_canonical(tag: str) -> str | None:
    index, error = _tag_normalization_index()
    if error is not None or index is None:
        return None

    canonical = index.lookup(tag_key(tag))
    if canonical:
        return canonical

    expanded = expand_tag_acronyms(tag)
    if expanded != tag:
        return index.lookup(tag_key(expanded))
    return None


def _is_tag_database_missing_issue(issue: Issue) -> bool:
    return issue.field == "tags" and _issue_rule_or_legacy(
        issue,
        RULE_TAG_DATABASE_MISSING,
        issue.message.startswith(_TAG_DATABASE_MISSING_ISSUE_PREFIX),
    )


def _tag_entry_aliases(entry: dict[str, Any]) -> list[str]:
    aliases = entry.get("aliases")
    if not isinstance(aliases, list):
        return []
    return [str(alias).strip() for alias in aliases if str(alias).strip()]


def _tag_entry_known_keys(entries: list[dict[str, Any]]) -> set[str]:
    keys: set[str] = set()
    for entry in entries:
        canonical = str(entry.get("canonical") or "").strip()
        values = [canonical, *_tag_entry_aliases(entry)]
        for value in values:
            key = tag_key(value)
            if key:
                keys.add(key)
    return keys


def _missing_tag_canonical_fix(
    tag: str,
    data: dict[str, Any],
    existing_keys: set[str],
) -> TagCanonicalFix | None:
    observed = _normalize_inline_text(tag)
    if not observed:
        return None

    canonical = _normalize_inline_text(expand_tag_acronyms(observed))
    if not canonical:
        return None

    canonical_key = tag_key(canonical)
    if not canonical_key or canonical_key in existing_keys:
        return None

    proper_name_words = _author_last_name_tag_proper_words(data)
    if _URL_RE.search(canonical):
        return None
    if _forbidden_tag_reason(canonical):
        return None
    if _sentence_like_tag_reason(canonical):
        return None
    if _suggest_tag_without_leading_article(canonical, proper_name_words) is not None:
        return None
    if _suggest_tag_capitalization(canonical, proper_name_words) != canonical:
        return None
    if _tag_word_count(canonical) > _MAX_TAG_WORDS and not _is_long_tag_allowed(canonical):
        return None

    aliases: tuple[str, ...] = ()
    observed_key = tag_key(observed)
    if observed != canonical and observed_key and observed_key != canonical_key:
        aliases = (observed,)

    return TagCanonicalFix(canonical=canonical, aliases=aliases)


def _merge_tag_canonical_fix(
    existing: TagCanonicalFix,
    candidate: TagCanonicalFix,
) -> TagCanonicalFix:
    aliases: list[str] = list(existing.aliases)
    seen = {tag_key(alias) for alias in aliases}
    for alias in candidate.aliases:
        key = tag_key(alias)
        if key and key not in seen:
            aliases.append(alias)
            seen.add(key)
    return TagCanonicalFix(existing.canonical, tuple(aliases))


def _collect_missing_tag_canonical_fixes(
    results: list[tuple[Path, list[Issue]]],
) -> dict[str, TagCanonicalFix]:
    try:
        data = load_yaml(_TAGS_DB)
    except (FileNotFoundError, yaml.YAMLError):
        return {}

    entries = data.get("tags")
    if not isinstance(entries, list):
        return {}

    tag_entries = [entry for entry in entries if isinstance(entry, dict)]
    existing_keys = _tag_entry_known_keys(tag_entries)
    fixes: dict[str, TagCanonicalFix] = {}

    for path, issues in results:
        missing_issues = [issue for issue in issues if _is_tag_database_missing_issue(issue)]
        if path.name != "metadata.yml" or not missing_issues:
            continue

        try:
            metadata = _yaml_safe_load(path.read_text(encoding="utf-8")) or {}
        except (OSError, yaml.YAMLError):
            continue
        if not isinstance(metadata, dict):
            continue

        tags = metadata.get("tags")
        if not isinstance(tags, list):
            continue

        for issue in missing_issues:
            index = _tag_issue_index(issue)
            if index is None or index < 0 or index >= len(tags):
                continue
            tag = str(tags[index]).strip()
            candidate = _missing_tag_canonical_fix(tag, metadata, existing_keys)
            if candidate is None:
                continue

            key = tag_key(candidate.canonical)
            if key in fixes:
                fixes[key] = _merge_tag_canonical_fix(fixes[key], candidate)
            else:
                fixes[key] = candidate

    return fixes


def _write_missing_tag_canonical_fixes(
    fixes: dict[str, TagCanonicalFix],
) -> dict[str, TagCanonicalFix]:
    if not fixes:
        return {}

    data = load_yaml(_TAGS_DB)
    entries = data.get("tags")
    if not isinstance(entries, list):
        return {}

    tag_entries = [entry for entry in entries if isinstance(entry, dict)]
    existing_keys = _tag_entry_known_keys(tag_entries)
    added: dict[str, TagCanonicalFix] = {}

    for key, fix in sorted(fixes.items(), key=lambda item: tag_key(item[1].canonical)):
        canonical_key = tag_key(fix.canonical)
        if not canonical_key or canonical_key in existing_keys:
            continue

        aliases = [
            alias
            for alias in fix.aliases
            if tag_key(alias) and tag_key(alias) != canonical_key and tag_key(alias) not in existing_keys
        ]
        entry: dict[str, object] = {"canonical": fix.canonical}
        if aliases:
            entry["aliases"] = aliases
        entries.append(entry)

        existing_keys.add(canonical_key)
        existing_keys.update(tag_key(alias) for alias in aliases if tag_key(alias))
        added[key] = TagCanonicalFix(fix.canonical, tuple(aliases))

    if not added:
        return {}

    entries.sort(key=lambda entry: tag_key(str(entry.get("canonical") or "")))
    data["tags"] = entries
    dump_yaml(_TAGS_DB, data, header=_TAGS_DB_HEADER)
    _tag_normalization_index.cache_clear()
    return added


__all__ = [name for name in globals() if name.startswith("_") and not name.startswith("__")]
