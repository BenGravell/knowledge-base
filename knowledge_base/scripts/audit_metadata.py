"""Audit (and optionally fix) metadata.yml files under knowledge_base/docs/papers/."""

import argparse
import html
import json
import re
import sys
import unicodedata
from dataclasses import dataclass
from dataclasses import field as dc_field
from enum import Enum
from pathlib import Path

import yaml
from rich.console import Console

from knowledge_base.config import AUDIT_STATUS_FIELD, REQUIRED_FIELDS, VALID_AUDIT_STATUSES, VALID_FIELDS, VALID_TYPES

console = Console(highlight=False)
err_console = Console(stderr=True, highlight=False)

# Minor words that stay lowercase unless first/last in title (Chicago style)
_LOWERCASE_TITLE_WORDS = {
    # articles
    "a",
    "an",
    "the",
    # coordinating conjunctions
    "and",
    "but",
    "or",
    "nor",
    "for",
    "yet",
    "so",
    # prepositions
    "as",
    "at",
    "by",
    "in",
    "of",
    "on",
    "to",
    "up",
    "via",
    "per",
    "vs",
    "from",
    "into",
    "like",
    "near",
    "off",
    "onto",
    "out",
    "over",
    "plus",
    "since",
    "than",
    "till",
    "under",
    "until",
    "unto",
    "upon",
    "with",
}

# arXiv ID patterns (version suffix optional)
_ARXIV_NEW_RE = re.compile(r"^\d{4}\.\d{4,5}(v\d+)?$")  # e.g. 2401.09241
_ARXIV_OLD_RE = re.compile(  # e.g. math.CO/0701001
    r"^[a-z]+(-[a-z]+)?(\.[A-Z]{2})?/\d{7}(v\d+)?$"
)
_HTML_ENTITY_RE = re.compile(
    r"&(?:#[0-9]+|#x[0-9A-Fa-f]+|[A-Za-z][A-Za-z0-9]+);"
)
CHECK_UNKNOWN = "unknown"
CHECK_REQUIRED = "required"
CHECK_TITLE = "title"
CHECK_AUTHORS = "authors"
CHECK_YEAR = "year"
CHECK_ARXIV = "arxiv"
CHECK_ABSTRACT = "abstract"
CHECK_ESCAPE = "escape"
CHECK_TYPE = "type"
CHECK_STATUS = "status"
CHECK_PATH = "path"
CHECK_SUMMARY = "summary"
CHECK_OPTIONAL = "optional"
CHECKS: tuple[str, ...] = (
    CHECK_UNKNOWN,
    CHECK_REQUIRED,
    CHECK_TITLE,
    CHECK_AUTHORS,
    CHECK_YEAR,
    CHECK_ARXIV,
    CHECK_ABSTRACT,
    CHECK_ESCAPE,
    CHECK_TYPE,
    CHECK_STATUS,
    CHECK_PATH,
    CHECK_SUMMARY,
    CHECK_OPTIONAL,
)
_NEAR_EMPTY_ABSTRACT_CHAR_LIMIT = 120
_NEAR_EMPTY_ABSTRACT_WORD_LIMIT = 20
_LONG_ABSTRACT_CHAR_LIMIT = 6000
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
_AUTHOR_SUFFIX_RE = re.compile(
    r"^(?:"
    r"Jr\.?|Sr\.?|"
    r"I{2,3}|IV|V|VI{0,3}|IX|X|"
    r"Ph\.?D\.?|M\.?D\.?|DPhil|Esq\.?"
    r")$",
    re.I,
)
_LAST_NAME_PARTICLES = {
    "da",
    "das",
    "de",
    "del",
    "della",
    "den",
    "der",
    "di",
    "do",
    "dos",
    "du",
    "la",
    "las",
    "le",
    "les",
    "los",
    "ten",
    "ter",
    "van",
    "von",
}


# ---------------------------------------------------------------------------
# Author helpers
# ---------------------------------------------------------------------------


def _looks_like_author_suffix(segment: str) -> bool:
    cleaned = segment.strip().strip(".")
    return bool(cleaned and _AUTHOR_SUFFIX_RE.fullmatch(cleaned))


def _looks_like_last_first_author(author: str) -> bool:
    """Detect likely "Last, First" author entries while allowing suffix commas."""
    comma_parts = [part.strip() for part in author.split(",")]
    if len(comma_parts) < 2 or not comma_parts[0]:
        return False

    for part in comma_parts[1:]:
        if not part or _looks_like_author_suffix(part):
            continue
        return bool(
            re.search(r"[A-Za-z]", comma_parts[0])
            and re.search(r"[A-Za-z]", part)
        )

    return False


# ---------------------------------------------------------------------------
# Title-case helpers
# ---------------------------------------------------------------------------


def _cap_first(s: str) -> str:
    """Uppercase only the first character; leave the rest unchanged.

    Unlike str.capitalize(), this preserves mixed-case words like 'WestWorld'.
    """
    return s[0].upper() + s[1:] if s else s


def _case_token(token: str, force_cap: bool) -> str:
    """Apply title-case rules to a single word token (no hyphens)."""
    # Separate trailing punctuation for classification, reattach after
    m = re.match(r"^(.*?)([,:;!?.]*)$", token)
    core, tail = (m.group(1), m.group(2)) if m else (token, "")

    alpha = re.sub(r"[^a-zA-Z]", "", core)
    # All-uppercase: acronym (e.g. MPPI, GPU, G1) — preserve as-is
    if alpha and alpha == alpha.upper():
        return token
    # Mixed-case: uppercase beyond the first character signals an intentional
    # capitalization pattern (e.g. pRRTC, iPhone, WestWorld) — preserve as-is
    if len(alpha) > 1 and any(c.isupper() for c in alpha[1:]):
        return token

    if force_cap or core.lower() not in _LOWERCASE_TITLE_WORDS:
        return _cap_first(core) + tail
    return core.lower() + tail


def to_title_case(title: str) -> str:
    words = title.split()
    if not words:
        return title
    result = []
    after_colon = False
    for i, word in enumerate(words):
        is_first = i == 0
        is_last = i == len(words) - 1
        force = is_first or is_last or after_colon
        # Track whether the next word follows a subtitle colon
        after_colon = word.endswith(":")

        if "-" in word:
            # Hyphenated compound: case the first part normally; preserve
            # existing case on subsequent parts (e.g. "Sampling-based" stays
            # "Sampling-based", not "Sampling-Based").
            parts = word.split("-")
            cased_parts = [_case_token(parts[0], force)] + parts[1:]
            result.append("-".join(cased_parts))
        else:
            result.append(_case_token(word, force))

    return " ".join(result)


def is_title_case(title: str) -> bool:
    return title == to_title_case(title)


# ---------------------------------------------------------------------------
# arXiv helpers
# ---------------------------------------------------------------------------


def is_valid_arxiv_id(arxiv_id: str) -> bool:
    return bool(_ARXIV_NEW_RE.match(arxiv_id) or _ARXIV_OLD_RE.match(arxiv_id))


def strip_arxiv_version(arxiv_id: str) -> str:
    return re.sub(r"v\d+$", "", arxiv_id)


# ---------------------------------------------------------------------------
# Escaped-sequence helpers
# ---------------------------------------------------------------------------


def _html_unescape_repeated(text: str, max_rounds: int = 3) -> str:
    """Decode HTML entities, including values that were escaped more than once."""
    current = text
    for _ in range(max_rounds):
        decoded = _HTML_ENTITY_RE.sub(lambda m: html.unescape(m.group(0)), current)
        if decoded == current:
            break
        current = decoded.replace("\xa0", " ")
    return current


def _walk_string_values(value, field_name: str):
    if isinstance(value, str):
        yield field_name, value
    elif isinstance(value, list):
        for i, item in enumerate(value):
            yield from _walk_string_values(item, f"{field_name}[{i}]")
    elif isinstance(value, dict):
        for key, item in value.items():
            nested = f"{field_name}.{key}" if field_name else str(key)
            yield from _walk_string_values(item, nested)


def find_escaped_sequence_issues(path: Path, data: dict) -> list["Issue"]:
    issues: list[Issue] = []
    for field_name, value in _walk_string_values(data, ""):
        matches = sorted(set(_HTML_ENTITY_RE.findall(value)))
        if not matches:
            continue

        examples = ", ".join(matches[:5])
        if len(matches) > 5:
            examples += f", ... ({len(matches)} total)"
        decoded_examples = ", ".join(
            f"{match} decodes to {_html_unescape_repeated(match)!r}"
            for match in matches[:3]
        )
        issues.append(
            Issue(
                path,
                field_name,
                f"Contains escaped HTML/entity sequence(s): {examples}",
                decoded_examples,
            )
        )
    return issues


# ---------------------------------------------------------------------------
# Slug helpers
# ---------------------------------------------------------------------------


def _ascii_fold(text: str) -> str:
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")


def _slugify(text: str) -> str:
    """Lowercase; replace runs of non-alphanumeric chars with single underscore."""
    s = _ascii_fold(text)
    s = _collapse_intra_word_apostrophes(s).lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_")


def _title_slug_tokens(title: str) -> list[str]:
    s = _collapse_intra_word_apostrophes(_ascii_fold(title))
    raw_tokens = re.findall(r"[A-Za-z0-9]+(?:\.[A-Za-z0-9]+)*", s)
    return [slug for token in raw_tokens if (slug := _slugify(token))]


def _collapse_intra_word_apostrophes(text: str) -> str:
    """Keep names like D'Andrea or O'Neill together for author slugs."""
    return re.sub(r"(?<=[A-Za-z0-9])['’](?=[A-Za-z0-9])", "", text)


def _extract_last_name(author: str) -> str:
    """Best-effort extraction of last name from a full name string."""
    # Strip generational/title suffix after comma: "Reeds, III" -> "Reeds"
    if "," in author:
        author = author[: author.index(",")]
    parts = author.strip().split()
    if not parts:
        return author

    last_name_start = len(parts) - 1
    while last_name_start > 0:
        particle = parts[last_name_start - 1].strip(".").lower()
        if particle not in _LAST_NAME_PARTICLES:
            break
        last_name_start -= 1

    return " ".join(parts[last_name_start:])


def expected_slug(year: int, arxiv_id: str, title: str, authors: list[str]) -> str:
    if arxiv_id:
        return strip_arxiv_version(arxiv_id)
    first_author = authors[0] if authors else ""
    last_name = _slugify(
        _collapse_intra_word_apostrophes(_extract_last_name(first_author))
    )
    # First four slug-bearing words of title; punctuation separates words except
    # inside dotted terms such as C4.5.
    title_tokens = _title_slug_tokens(title)[:4]
    title_part = "_".join(title_tokens)
    return f"{year}.{last_name}.{title_part}"


# ---------------------------------------------------------------------------
# Issue dataclass
# ---------------------------------------------------------------------------


class Severity(Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


@dataclass
class Issue:
    path: Path
    field: str
    message: str
    suggestion: str | None = None
    severity: Severity = dc_field(default=Severity.ERROR)


# ---------------------------------------------------------------------------
# Abstract-quality helpers
# ---------------------------------------------------------------------------


def _normalize_inline_text(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def _abstract_word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9]+(?:[-'][A-Za-z0-9]+)*", text))


def find_malformed_abstract_issues(path: Path, abstract: str) -> list[Issue]:
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
    elif len(text) < _NEAR_EMPTY_ABSTRACT_CHAR_LIMIT or word_count < _NEAR_EMPTY_ABSTRACT_WORD_LIMIT:
        issues.append(
            Issue(
                path,
                "abstract",
                f"Near-empty abstract ({len(text)} characters, {word_count} words)",
                "Replace with the full source abstract, or verify that the source abstract is genuinely this short.",
            )
        )

    scraped_hits = [
        label
        for label, pattern in _SCRAPED_ABSTRACT_PATTERNS
        if pattern.search(text)
    ]
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

    if _PDF_TEXT_ARTIFACT_RE.search(text):
        issues.append(
            Issue(
                path,
                "abstract",
                "Contains PDF extraction artifacts like '(cid:173)'",
                "Replace OCR/PDF text artifacts with clean source abstract text.",
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


# ---------------------------------------------------------------------------
# Per-file audit
# ---------------------------------------------------------------------------


def audit_file(
    path: Path,
    *,
    selected_checks: set[str] | None = None,
) -> tuple[dict, list[Issue]]:
    issues: list[Issue] = []

    def should_check(check: str) -> bool:
        return selected_checks is None or check in selected_checks

    try:
        raw = path.read_text(encoding="utf-8")
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        issues.append(Issue(path, "parse", f"YAML parse error: {exc}"))
        return {}, issues

    if not isinstance(data, dict):
        issues.append(Issue(path, "parse", "Root YAML value is not a mapping"))
        return {}, issues

    if should_check(CHECK_ESCAPE):
        issues.extend(find_escaped_sequence_issues(path, data))

    # -- unknown fields --
    if should_check(CHECK_UNKNOWN):
        _valid_set = set(VALID_FIELDS)
        for key in data:
            if key not in _valid_set:
                issues.append(Issue(path, key, f"Unknown field {key!r}"))

    # -- required fields presence --
    missing = {f for f in REQUIRED_FIELDS if data.get(f) is None}
    if should_check(CHECK_REQUIRED):
        for f in sorted(missing):
            issues.append(Issue(path, f, "Missing required field"))

    # -- title --
    title_raw = data.get("title")
    title = str(title_raw).strip() if title_raw not in (None, "") else ""
    if should_check(CHECK_TITLE) and "title" not in missing:
        if not title:
            issues.append(Issue(path, "title", "Empty"))
        else:
            corrected = _suggest_title_fix(raw, title)
            if title != corrected:
                issues.append(
                    Issue(
                        path,
                        "title",
                        f"Not in title case: {title!r}",
                        corrected,
                    )
                )

    # -- authors --
    authors = data.get("authors")
    if should_check(CHECK_AUTHORS) and "authors" not in missing:
        if not isinstance(authors, list):
            issues.append(Issue(path, "authors", "Must be a list"))
            authors = []
        elif len(authors) == 0:
            issues.append(
                Issue(path, "authors", "List is empty -- at least one entry required")
            )
        else:
            blank = [i for i, a in enumerate(authors) if not str(a).strip()]
            if blank:
                issues.append(
                    Issue(path, "authors", f"Blank entries at index(es): {blank}")
                )
            last_first = [
                i
                for i, a in enumerate(authors)
                if _looks_like_last_first_author(str(a))
            ]
            if last_first:
                examples = ", ".join(repr(str(authors[i])) for i in last_first[:3])
                if len(last_first) > 3:
                    examples += f", ... ({len(last_first)} total)"
                issues.append(
                    Issue(
                        path,
                        "authors",
                        "Author entries appear to use 'Last, First' order at index(es): "
                        f"{last_first}",
                        f"Use first-name last-name order; review: {examples}",
                    )
                )
    else:
        authors = authors if isinstance(authors, list) else []

    # -- year --
    if should_check(CHECK_YEAR) and "year" not in missing:
        meta_year_raw = data.get("year")
        if not isinstance(meta_year_raw, int) or not (1000 <= meta_year_raw <= 9999):
            issues.append(Issue(path, "year", f"Must be a 4-digit integer; got {meta_year_raw!r}"))

    # -- arxiv_id --
    arxiv_raw = data.get("arxiv_id")
    arxiv_id = str(arxiv_raw).strip() if arxiv_raw not in (None, "") else ""
    if should_check(CHECK_ARXIV) and arxiv_id and not is_valid_arxiv_id(arxiv_id):
        issues.append(Issue(path, "arxiv_id", f"Invalid arXiv ID format: {arxiv_id!r}"))

    # -- abstract --
    if should_check(CHECK_ABSTRACT) and "abstract" not in missing:
        abstract = data.get("abstract")
        abstract_str = str(abstract)
        if not abstract_str.strip():
            issues.append(Issue(path, "abstract", "Empty"))
        else:
            issues.extend(find_malformed_abstract_issues(path, abstract_str))

    # -- type --
    if should_check(CHECK_TYPE) and "type" not in missing:
        paper_type = data.get("type")
        type_str = str(paper_type).strip() if paper_type not in (None, "") else ""
        if type_str not in VALID_TYPES:
            issues.append(
                Issue(
                    path,
                    "type",
                    f"Invalid value {type_str!r}; must be one of: {sorted(VALID_TYPES)}",
                )
            )

    # -- audit_status --
    if should_check(CHECK_STATUS) and "audit_status" not in missing:
        audit_status = data.get(AUDIT_STATUS_FIELD)
        status_str = str(audit_status).strip() if audit_status not in (None, "") else ""
        if status_str not in VALID_AUDIT_STATUSES:
            issues.append(
                Issue(
                    path,
                    AUDIT_STATUS_FIELD,
                    f"Invalid value {status_str!r}; must be one of: {VALID_AUDIT_STATUSES}",
                )
            )

    # -- path structure --
    if should_check(CHECK_PATH):
        parts = path.parts
        try:
            papers_idx = next(i for i, p in enumerate(parts) if p == "papers")
            path_year_str = parts[papers_idx + 1]
            path_slug = "/".join(parts[papers_idx + 2 : -1])
        except (StopIteration, IndexError):
            issues.append(Issue(path, "path", "Cannot locate papers/YEAR/SLUG in path"))
            return data, issues

        if not path_slug:
            issues.append(Issue(path, "path", "Cannot locate papers/YEAR/SLUG in path"))
            return data, issues

        if not re.match(r"^\d{4}$", path_year_str):
            issues.append(
                Issue(path, "path", f"YEAR component {path_year_str!r} is not 4 digits")
            )
            return data, issues

        path_year = int(path_year_str)

        # Year in metadata should match path year
        meta_year = data.get("year")
        try:
            meta_year_int = int(meta_year) if meta_year is not None else None
        except (TypeError, ValueError):
            meta_year_int = None
        if meta_year_int is not None and meta_year_int != path_year:
            issues.append(
                Issue(
                    path,
                    "path",
                    f"Metadata year {meta_year!r} does not match path year {path_year}",
                )
            )

        # Slug check (only when we have enough data)
        author_strs = [str(a) for a in (authors or [])]
        if author_strs and title:
            exp = expected_slug(path_year, arxiv_id, title, author_strs)
            if path_slug != exp:
                issues.append(
                    Issue(
                        path,
                        "path",
                        f"Slug {path_slug!r} does not match expected {exp!r}",
                        exp,
                    )
                )

    # -- summary (warning) --
    if should_check(CHECK_SUMMARY):
        summary = data.get("summary")
        if not summary or not str(summary).strip():
            issues.append(
                Issue(path, "summary", "Missing or empty", severity=Severity.WARNING)
            )

    # -- optional field completeness (info) --
    if should_check(CHECK_OPTIONAL):
        audit_status_val = str(data.get(AUDIT_STATUS_FIELD) or "").strip()
        if audit_status_val == "raw":
            issues.append(Issue(path, AUDIT_STATUS_FIELD, "raw; skipping optional field checks", severity=Severity.INFO))
        else:
            for f in VALID_FIELDS:
                if f in REQUIRED_FIELDS or f == "summary":
                    continue  # already covered by required-check or summary-warning above
                val = data.get(f)
                is_empty = val is None or (isinstance(val, (str, list)) and not val)
                if is_empty:
                    if f == "arxiv_id":
                        link = str(data.get("link") or "").strip()
                        if link and "arxiv.org" not in link:
                            continue
                    issues.append(Issue(path, f, "Not populated", severity=Severity.INFO))

    return data, issues


# ---------------------------------------------------------------------------
# Fix helpers
# ---------------------------------------------------------------------------

_TITLE_LINE_RE = re.compile(r"^title\s*:\s*(?P<value>.*?)(?P<newline>\r?\n?)$")
_BLOCK_SCALAR_HEADER_RE = re.compile(r"^[>|][0-9+-]*(?:\s+#.*)?$")


def _format_title_line(new_title: str, line_ending: str = "\n") -> str:
    return f"title: {json.dumps(new_title, ensure_ascii=False)}{line_ending}"


def _is_block_scalar_header(value: str) -> bool:
    return bool(_BLOCK_SCALAR_HEADER_RE.match(value.strip()))


def _is_multiline_quoted_scalar_header(value: str) -> bool:
    stripped = value.lstrip()
    if not stripped or stripped[0] not in ("'", '"'):
        return False

    quote = stripped[0]
    escaped = False
    for char in stripped[1:]:
        if quote == '"' and char == "\\" and not escaped:
            escaped = True
            continue
        if char == quote and not escaped:
            return False
        escaped = False
    return True


def _has_indented_continuation(lines: list[str], start: int) -> bool:
    for line in lines[start + 1 :]:
        if not line.strip():
            continue
        return line.startswith((" ", "\t"))
    return False


def _plain_multiline_title_parts(raw: str) -> tuple[str, str] | None:
    lines = raw.splitlines(keepends=True)
    for start, line in enumerate(lines):
        m = _TITLE_LINE_RE.match(line)
        if not m:
            continue

        value = m.group("value")
        if _is_block_scalar_header(value) or not _has_indented_continuation(
            lines, start
        ):
            return None

        end = start + 1
        continuation_lines = []
        while end < len(lines):
            next_line = lines[end]
            if next_line.strip() and not next_line.startswith((" ", "\t")):
                break
            if next_line.strip():
                continuation_lines.append(next_line.strip())
            end += 1

        header = value.strip()
        try:
            parsed = yaml.safe_load(f"title: {header}\n")
            header = str(parsed.get("title", header)) if isinstance(parsed, dict) else header
        except yaml.YAMLError:
            header = header.strip("'\"")

        continuation = " ".join(continuation_lines)
        return header, continuation

    return None


def _normalize_for_duplicate_title_check(title: str) -> str:
    return " ".join(title.split()).casefold()


def _suggest_title_fix(raw: str, title: str) -> str:
    parts = _plain_multiline_title_parts(raw)
    if parts is not None:
        header, continuation = parts
        if (
            header
            and continuation
            and _normalize_for_duplicate_title_check(header)
            == _normalize_for_duplicate_title_check(continuation)
        ):
            return header

    return to_title_case(title)


def _fix_title_in_yaml(raw: str, new_title: str) -> str:
    """Replace the title value in raw YAML text.

    Titles are usually single-line scalars, but older metadata can use folded or
    literal block scalars. In that case the title node spans the `title: >` line
    plus the following indented lines, so replacing only the first line leaves a
    dangling duplicate continuation line behind.
    """
    lines = raw.splitlines(keepends=True)
    for start, line in enumerate(lines):
        m = _TITLE_LINE_RE.match(line)
        if not m:
            continue

        end = start + 1
        value = m.group("value")
        if (
            _is_block_scalar_header(value)
            or _is_multiline_quoted_scalar_header(value)
            or _has_indented_continuation(lines, start)
        ):
            while end < len(lines):
                next_line = lines[end]
                if next_line.strip() and not next_line.startswith((" ", "\t")):
                    break
                end += 1

        replacement = _format_title_line(new_title, m.group("newline"))
        return "".join(lines[:start] + [replacement] + lines[end:])

    return raw


def _is_escaped_sequence_issue(issue: Issue) -> bool:
    return issue.message.startswith("Contains escaped HTML/entity sequence")


def _fix_escaped_sequences_in_yaml(raw: str) -> tuple[str, int]:
    new_raw = _html_unescape_repeated(raw)
    return new_raw, len(_HTML_ENTITY_RE.findall(raw))


def apply_fixes(results: list[tuple[Path, list[Issue]]]) -> int:
    fixed = 0
    for path, issues in results:
        title_fixes = [
            i for i in issues if i.field == "title" and i.suggestion is not None
        ]
        has_escaped_sequence_fixes = any(_is_escaped_sequence_issue(i) for i in issues)
        if not title_fixes and not has_escaped_sequence_fixes:
            continue
        try:
            raw = path.read_text(encoding="utf-8")
            new_raw = raw
            messages = []

            if title_fixes:
                new_title = title_fixes[0].suggestion
                new_raw = _fix_title_in_yaml(new_raw, new_title)
                old_title = yaml.safe_load(raw).get("title", "")
                messages.append(f"  title: {old_title!r} [green]->[/] {new_title!r}")

            if has_escaped_sequence_fixes:
                new_raw, n_decoded = _fix_escaped_sequences_in_yaml(new_raw)
                if n_decoded:
                    messages.append(f"  decoded {n_decoded} escaped sequence(s)")

            if new_raw == raw:
                err_console.print(f"  [dim](no change written for {path})[/]")
                continue
            yaml.safe_load(new_raw)
            path.write_text(new_raw, encoding="utf-8")
            console.print(f"[green]Fixed:[/] {path}")
            for message in messages:
                console.print(message)
            fixed += 1
        except Exception as exc:
            err_console.print(f"[red]Error fixing {path}:[/] {exc}")
    console.print(f"\n[green]{fixed} file(s) fixed.[/]")
    return fixed


def _flatten_check_args(check_args: list[list[str]] | None) -> list[str]:
    if not check_args:
        return []
    return [name for group in check_args for name in group]


def _normalize_check_names(names: list[str]) -> tuple[set[str], list[str]]:
    selected: set[str] = set()
    invalid: list[str] = []
    valid = set(CHECKS)
    for name in names:
        if name in valid:
            selected.add(name)
        else:
            invalid.append(name)
    return selected, invalid


def _audit_status(data: dict) -> str:
    return str(data.get(AUDIT_STATUS_FIELD) or "").strip()


def _skip_reviewed_errors(data: dict, issues: list[Issue]) -> tuple[list[Issue], int]:
    if _audit_status(data) != "reviewed":
        return issues, 0

    kept = [issue for issue in issues if issue.severity != Severity.ERROR]
    return kept, len(issues) - len(kept)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit metadata.yml files under knowledge_base/docs/papers/.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Checks performed on each metadata.yml:
  unknown   - ERROR for any field not in the VALID_FIELDS schema
  required  - ERROR if any of title, authors, year, abstract, type, audit_status missing
  title     - ERROR if empty; ERROR if not in title case
  authors   - ERROR if not a non-empty list of non-blank strings; ERROR if entries look like Last, First order
  year      - ERROR if not a 4-digit integer
  arxiv     - ERROR if arxiv_id is present but not a valid arXiv ID
  abstract  - ERROR if empty, near-empty, placeholder-like, contains scraped page text, or has PDF extraction artifacts
  escape    - ERROR if string fields contain HTML/entity escapes like &#39; or &amp;
  type      - ERROR if not a recognised paper type
  status    - ERROR if audit_status is not one of: raw, partial, reviewed
  path      - ERROR if YEAR/SLUG do not match metadata or expected slug format
  summary   - WARN if missing or empty
  optional  - INFO for each optional field that is not populated

By default, every check runs. Use --check to opt into a smaller set:
  --check abstract escape

Available --check names:
  unknown required title authors year arxiv abstract escape type status path summary optional
""",
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Repository root (default: current directory)",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Auto-fix title-case and escaped HTML/entity issues (rewrites files in place)",
    )
    parser.add_argument(
        "--file",
        metavar="PATH",
        help="Audit a single metadata.yml instead of the whole tree",
    )
    parser.add_argument(
        "--check",
        nargs="+",
        action="append",
        metavar="NAME",
        dest="check_names",
        help="Run only the named checks. Names: " + ", ".join(CHECKS),
    )
    parser.add_argument(
        "--skip-reviewed-errors",
        action="store_true",
        help="Do not report or fail on ERROR issues for metadata with audit_status: reviewed",
    )
    args = parser.parse_args()
    selected_names, invalid_names = _normalize_check_names(
        _flatten_check_args(args.check_names)
    )
    if invalid_names:
        parser.error(
            "unknown --check value(s): "
            + ", ".join(sorted(set(invalid_names)))
            + "\nvalid values: "
            + ", ".join(CHECKS)
        )
    selected_checks = selected_names or None

    if args.file:
        targets = [Path(args.file)]
    else:
        papers_root = Path(args.root) / "docs" / "papers"
        if not papers_root.exists():
            sys.exit(f"Papers directory not found: {papers_root}")
        targets = sorted(papers_root.rglob("metadata.yml"))

    skipped_reviewed_errors = 0
    results: list[tuple[Path, list[Issue]]] = []
    for p in targets:
        data, issues = audit_file(p, selected_checks=selected_checks)
        if args.skip_reviewed_errors:
            issues, skipped_count = _skip_reviewed_errors(data, issues)
            skipped_reviewed_errors += skipped_count
        if issues:
            results.append((p, issues))

    all_issues = [i for _, issues in results for i in issues]
    n_errors = sum(1 for i in all_issues if i.severity == Severity.ERROR)
    n_warnings = sum(1 for i in all_issues if i.severity == Severity.WARNING)
    n_infos = sum(1 for i in all_issues if i.severity == Severity.INFO)

    if not all_issues:
        console.print(f"[green]All {len(targets)} metadata.yml file(s) pass audit.[/]")
        if skipped_reviewed_errors:
            console.print(
                f"[dim]Skipped {skipped_reviewed_errors} error(s) from reviewed metadata.[/]"
            )
        return

    parts = []
    if n_errors:
        parts.append(f"[bold red]{n_errors} error(s)[/]")
    if n_warnings:
        parts.append(f"[bold yellow]{n_warnings} warning(s)[/]")
    if n_infos:
        parts.append(f"[bold cyan]{n_infos} info(s)[/]")
    console.print(
        ", ".join(parts) + f" across {len(results)} / {len(targets)} file(s):\n"
    )
    if skipped_reviewed_errors:
        console.print(
            f"[dim]Skipped {skipped_reviewed_errors} error(s) from reviewed metadata.[/]\n"
        )

    for path, issues in results:
        console.print(f"[bold]{path}[/]")
        for issue in issues:
            if issue.severity == Severity.ERROR:
                badge = "[bold red]ERROR[/]"
            elif issue.severity == Severity.WARNING:
                badge = "[bold yellow]WARN [/]"
            else:
                badge = "[bold cyan]INFO [/]"
            console.print(f"  {badge} [bold]\\[{issue.field}][/] {issue.message}")
            if issue.suggestion is not None:
                console.print(f"         [dim]-> {issue.suggestion}[/]")
        console.print()

    if args.fix:
        apply_fixes(results)
        remaining_errors = 0
        for p in targets:
            data, issues = audit_file(p, selected_checks=selected_checks)
            if args.skip_reviewed_errors:
                issues, _ = _skip_reviewed_errors(data, issues)
            remaining_errors += sum(1 for i in issues if i.severity == Severity.ERROR)
        sys.exit(1 if remaining_errors else 0)

    sys.exit(1 if n_errors else 0)


if __name__ == "__main__":
    main()
