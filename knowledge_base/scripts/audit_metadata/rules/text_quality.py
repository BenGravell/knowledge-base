"""Misspelling and OCR artifact audit rules."""

import re
from pathlib import Path

from knowledge_base.scripts.audit_metadata.rules.text_artifacts import (
    _COMMON_MISSPELLING_CORRECTIONS,
    _COMMON_MISSPELLING_RE,
    _COMMON_MISSPELLINGS,
    _HIGH_CONFIDENCE_OCR_ARTIFACT_ISSUE_PREFIX,
    _HIGH_CONFIDENCE_OCR_ARTIFACTS,
    _LINEBREAK_HYPHEN_RE,
    _OCR_SPLIT_PARTS_RE,
    _OCR_SPLIT_RE,
    _SUSPENDED_HYPHEN_JOINERS,
    _VALID_HYPHENATED_OCR_SPLITS,
)
from knowledge_base.scripts.audit_metadata.support.model import RULE_HIGH_CONFIDENCE_OCR_ARTIFACT, Issue, Severity


def find_likely_misspelling_issues(
    path: Path,
    field: str,
    text: str,
) -> list[Issue]:
    folded = text.casefold()
    found = {match.group(1) for match in _COMMON_MISSPELLING_RE.finditer(folded)}
    hits = [
        (typo, _COMMON_MISSPELLING_CORRECTIONS[typo.casefold()])
        for typo in _COMMON_MISSPELLINGS
        if typo.casefold() in found
    ]

    if not hits:
        return []

    examples = ", ".join(f"{typo!r} -> {correction!r}" for typo, correction in hits[:6])
    if len(hits) > 6:
        examples += f", ... ({len(hits)} total)"
    return [
        Issue(
            path,
            field,
            f"Contains likely misspelling(s): {examples}",
            "Review against the source text and fix only genuine typos.",
            severity=Severity.WARNING,
        )
    ]


def _apply_high_confidence_ocr_replacements(text: str) -> tuple[str, int]:
    fixed = text
    changed = 0
    for _label, pattern, replacement in _HIGH_CONFIDENCE_OCR_ARTIFACTS:
        fixed, count = pattern.subn(replacement, fixed)
        changed += count
    return fixed, changed


def find_high_confidence_ocr_artifact_issues(
    path: Path,
    field: str,
    text: str,
) -> list[Issue]:
    hits: list[tuple[str, str]] = []
    for label, pattern, _replacement in _HIGH_CONFIDENCE_OCR_ARTIFACTS:
        hits.extend((match.group(0), label) for match in pattern.finditer(text))

    if not hits:
        return []

    examples = ", ".join(f"{artifact!r} -> {replacement!r}" for artifact, replacement in hits[:6])
    if len(hits) > 6:
        examples += f", ... ({len(hits)} total)"
    return [
        Issue(
            path,
            field,
            f"{_HIGH_CONFIDENCE_OCR_ARTIFACT_ISSUE_PREFIX} {examples}",
            "Replace exact OCR artifacts with their clean source words.",
            severity=Severity.WARNING,
            rule=RULE_HIGH_CONFIDENCE_OCR_ARTIFACT,
        )
    ]


def _ocr_split_examples(text: str, *, limit: int = 8) -> list[str]:
    examples: list[str] = []
    seen: set[str] = set()
    for match in _OCR_SPLIT_RE.finditer(text):
        parts = _OCR_SPLIT_PARTS_RE.match(match.group(0))
        if parts is None:
            continue
        word = (parts.group("head") + parts.group("tail")).casefold()
        split_at = len(parts.group("head"))
        if parts.group("sep").startswith("-") and (word, split_at) in _VALID_HYPHENATED_OCR_SPLITS:
            continue
        example = f"{match.group(0)!r} -> {word!r}"
        if example in seen:
            continue
        examples.append(example)
        seen.add(example)
        if len(examples) >= limit:
            return examples
    return examples


def _is_suspended_hyphen_compound(match: re.Match[str]) -> bool:
    return match.group("tail").casefold() in _SUSPENDED_HYPHEN_JOINERS


def find_ocr_spacing_issues(path: Path, field: str, text: str) -> list[Issue]:
    examples = _ocr_split_examples(text)
    linebreak_examples: list[str] = []
    for match in _LINEBREAK_HYPHEN_RE.finditer(text):
        if _is_suspended_hyphen_compound(match):
            continue
        value = match.group(0)
        if value not in linebreak_examples:
            linebreak_examples.append(value)
        if len(linebreak_examples) >= 5:
            break

    if not examples and not linebreak_examples:
        return []

    fragments: list[str] = []
    if examples:
        fragments.append(", ".join(examples[:5]))
    if linebreak_examples:
        fragments.append("line-break hyphenation: " + ", ".join(repr(example) for example in linebreak_examples[:5]))
    return [
        Issue(
            path,
            field,
            "Contains likely OCR word-splitting artifact(s): " + "; ".join(fragments),
            "Join accidentally split words and remove line-break hyphenation when the source word is not hyphenated.",
            severity=Severity.WARNING,
        )
    ]
