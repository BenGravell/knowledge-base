"""Abstract and summary audit constants."""

import re

_NEAR_EMPTY_ABSTRACT_CHAR_LIMIT = 120
_NEAR_EMPTY_ABSTRACT_WORD_LIMIT = 20
_LONG_ABSTRACT_CHAR_LIMIT = 6000
_SUMMARY_ABSTRACT_OVERLAP_MIN_RUN_WORDS = 18
_SUMMARY_ABSTRACT_OVERLAP_MIN_COVERED_WORDS = 24
_SUMMARY_ABSTRACT_OVERLAP_MIN_COVERAGE = 0.45
_SUMMARY_ABSTRACT_OVERLAP_ISSUE_PREFIX = "Substantial verbatim overlap with abstract:"
_SUMMARY_ABSTRACT_WORD_RE = re.compile(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*")
_PDF_TEXT_ARTIFACT_RE = re.compile(r"\(cid:\d+\)")
_PLACEHOLDER_ABSTRACT_RE = re.compile(
    r"^(?:n/?a|none|no abstract(?: available)?|not available|abstract unavailable|"
    r"to be added|todo|tbd|unknown)\.?$",
    re.I,
)
_SCRAPED_ABSTRACT_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "journal navigation text",
        re.compile(r"\bPrevious article\s*Next article\b", re.I),
    ),
    (
        "publisher section toolbar",
        re.compile(r"PDF\s*Bib\s*TeX?\s*Sections\b", re.I),
    ),
    (
        "publisher tool links",
        re.compile(
            r"Tools\s*Add to favorites\s*Export Citation\s*Track Citations\s*Email Sections",
            re.I,
        ),
    ),
    (
        "references/cited-by section",
        re.compile(r"References\s*Cited By\s*Details\b", re.I),
    ),
    (
        "page abstract heading",
        re.compile(r"About\s*Abstract[A-Z]", re.I),
    ),
    (
        "related/references section",
        re.compile(r"Figures\s*Related\s*References\b", re.I),
    ),
    (
        "publisher author/profile chrome",
        re.compile(r"(?:Authors Info & Claims|View Profile)\b", re.I),
    ),
    (
        "publisher metrics/citation controls",
        re.compile(
            r"(?:Publication History|Get Citation Alerts|Save to Binder|Metrics\s*Total Citations)\b",
            re.I,
        ),
    ),
    (
        "publisher access controls",
        re.compile(r"Publisher Site\s*(?:Get Access|eReaderPDF)?\b", re.I),
    ),
)
_PUBLISHER_MARK_ABSTRACT_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "copyright notice",
        re.compile(
            "(?:"
            r"\N{COPYRIGHT SIGN}\s*(?:18|19|20)\d{2}[^.]{0,120}\.?|"
            r"\bcopyright\s*(?:\N{COPYRIGHT SIGN})?\s*(?:18|19|20)\d{2}[^.]{0,120}\.?|"
            r"\(c\)\s*(?:18|19|20)\d{2}[^.]{0,120}\.?"
            ")",
            re.I,
        ),
    ),
    (
        "rights-reserved notice",
        re.compile(r"\ball\s+rights\s+reserved\.?", re.I),
    ),
)
_PUBLISHER_MARK_ABSTRACT_ISSUE_PREFIX = "Contains publisher/copyright notice in the abstract:"
_ABSTRACT_DOLLAR_MATH_ISSUE_PREFIX = "Contains dollar math in the abstract"
_ABSTRACT_LATEX_ARTIFACT_ISSUE_PREFIX = "Contains plain LaTeX math artifact(s) in the abstract"
_LOW_SIGNAL_SUMMARY_ISSUE_PREFIX = "Low-signal generated summary"
_LOW_SIGNAL_SUMMARY_PHRASE = (
    "It is useful as a compact reference for the problem formulation, "
    "main assumptions, and evaluation setting behind the contribution."
)

__all__ = [name for name in globals() if name.startswith("_") and not name.startswith("__")]
