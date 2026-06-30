"""Author-field audit helpers."""

from pathlib import Path
from typing import Any

from knowledge_base.scripts.audit_metadata.rules.author_rules import (
    _author_ascii_normalization_issues,
    _looks_like_last_first_author,
    _non_individual_author_reason,
    _suspicious_author_char_descriptions,
)
from knowledge_base.scripts.audit_metadata.support.model import (
    RULE_AUTHOR_ASCII_NORMALIZATION,
    RULE_AUTHOR_MOJIBAKE,
    RULE_NON_INDIVIDUAL_AUTHOR,
    Issue,
)


def find_author_field_issues(
    path: Path,
    authors_raw: object,
    authors: list[Any],
) -> list[Issue]:
    issues: list[Issue] = []
    if not isinstance(authors_raw, list):
        return [Issue(path, "authors", "Must be a list")]
    if len(authors) == 0:
        return [Issue(path, "authors", "List is empty -- at least one entry required")]

    blank = [i for i, a in enumerate(authors) if not str(a).strip()]
    if blank:
        issues.append(Issue(path, "authors", f"Blank entries at index(es): {blank}"))

    last_first = [i for i, a in enumerate(authors) if _looks_like_last_first_author(str(a))]
    if last_first:
        examples = ", ".join(repr(str(authors[i])) for i in last_first[:3])
        if len(last_first) > 3:
            examples += f", ... ({len(last_first)} total)"
        issues.append(
            Issue(
                path,
                "authors",
                f"Author entries appear to use 'Last, First' order at index(es): {last_first}",
                f"Use first-name last-name order; review: {examples}",
            )
        )

    non_individual = {i: _non_individual_author_reason(str(a)) for i, a in enumerate(authors)}
    non_individual = {i: reason for i, reason in non_individual.items() if reason is not None}
    if non_individual:
        examples = ", ".join(f"{i}: {str(authors[i])!r} ({reason})" for i, reason in list(non_individual.items())[:4])
        if len(non_individual) > 4:
            examples += f", ... ({len(non_individual)} total)"
        issues.append(
            Issue(
                path,
                "authors",
                f"Author entries appear to be non-individual names at index(es): {list(non_individual)}",
                f"Replace organizations, team/institution placeholders, and one-token names with individual human authors where available; review: {examples}",
                rule=RULE_NON_INDIVIDUAL_AUTHOR,
            )
        )

    suspicious_chars: dict[int, list[str]] = {}
    for i, a in enumerate(authors):
        char_descriptions = _suspicious_author_char_descriptions(str(a))
        if char_descriptions:
            suspicious_chars[i] = sorted(set(char_descriptions))
    if suspicious_chars:
        examples = ", ".join(
            f"{i}: {str(authors[i])!r} ({', '.join(chars[:3])})" for i, chars in list(suspicious_chars.items())[:3]
        )
        if len(suspicious_chars) > 3:
            examples += f", ... ({len(suspicious_chars)} total)"
        issues.append(
            Issue(
                path,
                "authors",
                f"Author entries contain suspicious Unicode character(s) at index(es): {list(suspicious_chars)}",
                f"Replace mojibake/control characters with clean author names; review: {examples}",
                rule=RULE_AUTHOR_MOJIBAKE,
            )
        )

    ascii_normalization = _author_ascii_normalization_issues(authors)
    if ascii_normalization:
        examples = ", ".join(
            f"{i}: {str(authors[i])!r} -> {normalized!r}" for i, normalized in list(ascii_normalization.items())[:4]
        )
        if len(ascii_normalization) > 4:
            examples += f", ... ({len(ascii_normalization)} total)"
        issues.append(
            Issue(
                path,
                "authors",
                f"Author entries are not ASCII-normalized at index(es): {list(ascii_normalization)}",
                "Normalize author names to the native 26 English "
                f"letters for centralized author matching; review: {examples}",
                rule=RULE_AUTHOR_ASCII_NORMALIZATION,
            )
        )

    return issues


__all__ = ["find_author_field_issues"]
