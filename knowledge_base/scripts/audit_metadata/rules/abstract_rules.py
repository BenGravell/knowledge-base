"""Abstract and summary audit rules."""

import re
from pathlib import Path

from knowledge_base.scripts.audit_metadata.rules.abstract_data import (
    _ABSTRACT_DOLLAR_MATH_ISSUE_PREFIX,
    _ABSTRACT_LATEX_ARTIFACT_ISSUE_PREFIX,
    _LONG_ABSTRACT_CHAR_LIMIT,
    _LOW_SIGNAL_SUMMARY_ISSUE_PREFIX,
    _LOW_SIGNAL_SUMMARY_PHRASE,
    _NEAR_EMPTY_ABSTRACT_CHAR_LIMIT,
    _NEAR_EMPTY_ABSTRACT_WORD_LIMIT,
    _PDF_TEXT_ARTIFACT_RE,
    _PLACEHOLDER_ABSTRACT_RE,
    _PUBLISHER_MARK_ABSTRACT_ISSUE_PREFIX,
    _PUBLISHER_MARK_ABSTRACT_PATTERNS,
    _SCRAPED_ABSTRACT_PATTERNS,
    _SUMMARY_ABSTRACT_OVERLAP_ISSUE_PREFIX,
    _SUMMARY_ABSTRACT_OVERLAP_MIN_COVERAGE,
    _SUMMARY_ABSTRACT_OVERLAP_MIN_COVERED_WORDS,
    _SUMMARY_ABSTRACT_OVERLAP_MIN_RUN_WORDS,
    _SUMMARY_ABSTRACT_WORD_RE,
)
from knowledge_base.scripts.audit_metadata.rules.latex_data import _DOLLAR_SIGN_RE
from knowledge_base.scripts.audit_metadata.rules.latex_rules import _plain_latex_math_artifact_count
from knowledge_base.scripts.audit_metadata.support.model import (
    RULE_ABSTRACT_DOLLAR_MATH,
    RULE_ABSTRACT_LATEX_ARTIFACT,
    RULE_ABSTRACT_PUBLISHER_MARK,
    RULE_CLEARABLE_SUMMARY,
    Issue,
    Severity,
)
from knowledge_base.scripts.audit_metadata.support.text import _normalize_inline_text

_ABSTRACT_WORD_RE = re.compile(r"\babstract\b", re.I)

# ---------------------------------------------------------------------------
# Abstract-quality helpers
# ---------------------------------------------------------------------------


def _abstract_word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", text))


def _overlap_words(text: str) -> list[str]:
    return [match.group(0).casefold() for match in _SUMMARY_ABSTRACT_WORD_RE.finditer(text)]


def _longest_common_word_run(left: list[str], right: list[str]) -> tuple[int, int]:
    previous = [0] * (len(right) + 1)
    best_len = 0
    best_left_end = 0

    for left_index, left_word in enumerate(left, 1):
        current = [0] * (len(right) + 1)
        for right_index, right_word in enumerate(right, 1):
            if left_word != right_word:
                continue
            current[right_index] = previous[right_index - 1] + 1
            if current[right_index] > best_len:
                best_len = current[right_index]
                best_left_end = left_index
        previous = current

    return best_len, best_left_end - best_len


def _shared_shingle_coverage(
    summary_words: list[str],
    abstract_words: list[str],
    *,
    size: int = 8,
) -> float:
    if len(summary_words) < size or len(abstract_words) < size:
        return 0.0

    abstract_shingles = {tuple(abstract_words[index : index + size]) for index in range(len(abstract_words) - size + 1)}
    covered = [False] * len(summary_words)
    for index in range(len(summary_words) - size + 1):
        if tuple(summary_words[index : index + size]) in abstract_shingles:
            for covered_index in range(index, index + size):
                covered[covered_index] = True

    return sum(covered) / len(summary_words)


def find_summary_abstract_overlap_issues(
    path: Path,
    summary: str,
    abstract: str,
) -> list[Issue]:
    summary_words = _overlap_words(summary)
    abstract_words = _overlap_words(abstract)
    if not summary_words or not abstract_words:
        return []

    longest_run, run_start = _longest_common_word_run(summary_words, abstract_words)
    shingle_coverage = _shared_shingle_coverage(summary_words, abstract_words)
    covered_words = round(shingle_coverage * len(summary_words))
    run_coverage = longest_run / len(summary_words)

    has_long_run = longest_run >= _SUMMARY_ABSTRACT_OVERLAP_MIN_RUN_WORDS
    has_dominant_run = longest_run >= 12 and run_coverage >= 0.45
    has_broad_overlap = (
        covered_words >= _SUMMARY_ABSTRACT_OVERLAP_MIN_COVERED_WORDS
        and shingle_coverage >= _SUMMARY_ABSTRACT_OVERLAP_MIN_COVERAGE
    )
    if not (has_long_run or has_dominant_run or has_broad_overlap):
        return []

    snippet = " ".join(summary_words[run_start : run_start + longest_run])
    if len(snippet) > 120:
        snippet = snippet[:117] + "..."
    return [
        Issue(
            path,
            "summary",
            (
                f"{_SUMMARY_ABSTRACT_OVERLAP_ISSUE_PREFIX} "
                f"{longest_run} consecutive word(s) "
                f"({run_coverage:.0%} of summary); "
                f"{covered_words} word(s) covered by shared 8-word phrases "
                f"({shingle_coverage:.0%} of summary). Example: {snippet!r}"
            ),
            "Rewrite the summary in original observer-language instead of reusing abstract phrasing.",
            rule=RULE_CLEARABLE_SUMMARY,
        )
    ]


def find_low_signal_summary_issues(path: Path, summary: str) -> list[Issue]:
    text = _normalize_inline_text(summary)
    if _LOW_SIGNAL_SUMMARY_PHRASE not in text:
        return []

    return [
        Issue(
            path,
            "summary",
            f"{_LOW_SIGNAL_SUMMARY_ISSUE_PREFIX}: contains generic boilerplate",
            (
                "Replace with a paper-specific observer-language summary, or leave "
                "the field blank until one can be written from the source."
            ),
            rule=RULE_CLEARABLE_SUMMARY,
        )
    ]


def _format_labeled_text_hits(hits: list[tuple[str, str]]) -> str:
    examples: list[str] = []
    seen: set[tuple[str, str]] = set()
    for label, snippet in hits:
        snippet = _normalize_inline_text(snippet)
        if len(snippet) > 90:
            snippet = f"{snippet[:87]}..."
        key = (label, snippet)
        if key in seen:
            continue
        seen.add(key)
        examples.append(f"{label} ({snippet!r})")
        if len(examples) >= 4:
            break

    suffix = f", ... ({len(hits)} total)" if len(hits) > len(examples) else ""
    return ", ".join(examples) + suffix


def find_malformed_abstract_issues(
    path: Path,
    abstract: str,
    *,
    allow_short: bool = False,
) -> list[Issue]:
    issues: list[Issue] = []
    text = _normalize_inline_text(abstract)
    if not text:
        return issues

    word_count = _abstract_word_count(text)
    if _PLACEHOLDER_ABSTRACT_RE.fullmatch(text):
        issues.append(
            Issue(
                path,
                "abstract",
                f"Placeholder abstract: {text!r}",
                "Replace with the full source abstract, or leave blank only when no abstract truly exists.",
            )
        )
    elif not allow_short and (
        len(text) < _NEAR_EMPTY_ABSTRACT_CHAR_LIMIT or word_count < _NEAR_EMPTY_ABSTRACT_WORD_LIMIT
    ):
        issues.append(
            Issue(
                path,
                "abstract",
                f"Near-empty abstract ({len(text)} characters, {word_count} words)",
                "Replace with the full source abstract, or verify that the source abstract is genuinely this short.",
            )
        )

    scraped_hits = [label for label, pattern in _SCRAPED_ABSTRACT_PATTERNS if pattern.search(text)]
    if scraped_hits:
        examples = ", ".join(scraped_hits[:4])
        if len(scraped_hits) > 4:
            examples += f", ... ({len(scraped_hits)} total)"
        issues.append(
            Issue(
                path,
                "abstract",
                f"Looks like scraped page text mixed into the abstract: {examples}",
                "Replace with only the source abstract; remove navigation, references, metrics, and cited-by text.",
            )
        )

    publisher_mark_hits = [
        (label, match.group(0))
        for label, pattern in _PUBLISHER_MARK_ABSTRACT_PATTERNS
        for match in pattern.finditer(text)
    ]
    if publisher_mark_hits:
        issues.append(
            Issue(
                path,
                "abstract",
                f"{_PUBLISHER_MARK_ABSTRACT_ISSUE_PREFIX} {_format_labeled_text_hits(publisher_mark_hits)}",
                "Remove publisher notices, copyright footers, and rights-reserved text; keep only the source abstract.",
                rule=RULE_ABSTRACT_PUBLISHER_MARK,
            )
        )

    if _PDF_TEXT_ARTIFACT_RE.search(text):
        issues.append(
            Issue(
                path,
                "abstract",
                "Contains PDF extraction artifacts like '(cid:173)'",
                "Replace OCR/PDF text artifacts with clean source abstract text.",
            )
        )

    abstract_word_matches = _ABSTRACT_WORD_RE.findall(text)
    if abstract_word_matches:
        count = len(abstract_word_matches)
        issues.append(
            Issue(
                path,
                "abstract",
                f"Contains the word 'abstract' {count} time(s)",
                "Verify that an 'Abstract' heading, page chrome, or commentary was not copied into the abstract field.",
                severity=Severity.WARNING,
            )
        )

    dollar_count = len(_DOLLAR_SIGN_RE.findall(text))
    if dollar_count:
        issues.append(
            Issue(
                path,
                "abstract",
                f"{_ABSTRACT_DOLLAR_MATH_ISSUE_PREFIX}: {dollar_count} dollar sign(s), likely from inline/display math",
                "Rewrite math notation as readable plain text, for example O(n/k) instead of LaTeX dollar math.",
                severity=Severity.WARNING,
                rule=RULE_ABSTRACT_DOLLAR_MATH,
            )
        )

    latex_artifact_count = _plain_latex_math_artifact_count(text)
    if latex_artifact_count:
        issues.append(
            Issue(
                path,
                "abstract",
                f"{_ABSTRACT_LATEX_ARTIFACT_ISSUE_PREFIX}: {latex_artifact_count} likely artifact(s)",
                "Rewrite glued or command-name math artifacts as readable plain text, for example l_p or beta in [0, 1).",
                severity=Severity.WARNING,
                rule=RULE_ABSTRACT_LATEX_ARTIFACT,
            )
        )

    if not scraped_hits and len(text) > _LONG_ABSTRACT_CHAR_LIMIT:
        issues.append(
            Issue(
                path,
                "abstract",
                f"Unusually long ({len(text)} characters); verify this is only the abstract",
                severity=Severity.WARNING,
            )
        )

    return issues
