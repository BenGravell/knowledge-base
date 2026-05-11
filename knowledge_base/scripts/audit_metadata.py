"""Audit (and optionally fix) metadata.yml files under knowledge_base/docs/papers/."""

import argparse
import html
import re
import sys
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
CHECK_ESCAPED_SEQUENCES = "escaped_sequences"
CHECK_MALFORMED_ABSTRACTS = "malformed_abstracts"
_LONG_ABSTRACT_CHAR_LIMIT = 6000
_PDF_TEXT_ARTIFACT_RE = re.compile(r"\(cid:\d+\)")
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


def _slugify(text: str) -> str:
    """Lowercase; replace runs of non-alphanumeric chars with single underscore."""
    s = text.lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    return s.strip("_")


def _extract_last_name(author: str) -> str:
    """Best-effort extraction of last name from a full name string."""
    # Strip generational/title suffix after comma: "Reeds, III" -> "Reeds"
    if "," in author:
        author = author[: author.index(",")]
    parts = author.strip().split()
    return parts[-1] if parts else author


def expected_slug(year: int, arxiv_id: str, title: str, authors: list[str]) -> str:
    if arxiv_id:
        return strip_arxiv_version(arxiv_id)
    first_author = authors[0] if authors else ""
    last_name = _slugify(_extract_last_name(first_author))
    # First four words of title; split on whitespace and hyphens
    title_tokens = re.split(r"[\s\-]+", title.strip())[:4]
    title_part = "_".join(_slugify(w) for w in title_tokens if w)
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


def find_malformed_abstract_issues(path: Path, abstract: str) -> list[Issue]:
    issues: list[Issue] = []
    text = _normalize_inline_text(abstract)
    if not text:
        return issues

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
    escaped_sequences_only: bool = False,
) -> tuple[dict, list[Issue]]:
    issues: list[Issue] = []

    if escaped_sequences_only:
        selected_checks = set(selected_checks or ())
        selected_checks.add(CHECK_ESCAPED_SEQUENCES)

    try:
        raw = path.read_text(encoding="utf-8")
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        issues.append(Issue(path, "parse", f"YAML parse error: {exc}"))
        return {}, issues

    if not isinstance(data, dict):
        issues.append(Issue(path, "parse", "Root YAML value is not a mapping"))
        return {}, issues

    if selected_checks is not None:
        if CHECK_ESCAPED_SEQUENCES in selected_checks:
            issues.extend(find_escaped_sequence_issues(path, data))
        if CHECK_MALFORMED_ABSTRACTS in selected_checks:
            abstract = data.get("abstract")
            if abstract not in (None, ""):
                issues.extend(find_malformed_abstract_issues(path, str(abstract)))
        return data, issues

    issues.extend(find_escaped_sequence_issues(path, data))

    # -- unknown fields --
    _valid_set = set(VALID_FIELDS)
    for key in data:
        if key not in _valid_set:
            issues.append(Issue(path, key, f"Unknown field {key!r}"))

    # -- required fields presence --
    missing = {f for f in REQUIRED_FIELDS if data.get(f) is None}
    for f in sorted(missing):
        issues.append(Issue(path, f, "Missing required field"))

    # -- title --
    title_raw = data.get("title")
    title = str(title_raw).strip() if title_raw not in (None, "") else ""
    if "title" not in missing:
        if not title:
            issues.append(Issue(path, "title", "Empty"))
        else:
            corrected = to_title_case(title)
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
    if "authors" not in missing:
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
    else:
        authors = []

    # -- year --
    if "year" not in missing:
        meta_year_raw = data.get("year")
        if not isinstance(meta_year_raw, int) or not (1000 <= meta_year_raw <= 9999):
            issues.append(Issue(path, "year", f"Must be a 4-digit integer; got {meta_year_raw!r}"))

    # -- arxiv_id --
    arxiv_raw = data.get("arxiv_id")
    arxiv_id = str(arxiv_raw).strip() if arxiv_raw not in (None, "") else ""
    if arxiv_id and not is_valid_arxiv_id(arxiv_id):
        issues.append(Issue(path, "arxiv_id", f"Invalid arXiv ID format: {arxiv_id!r}"))

    # -- abstract --
    if "abstract" not in missing:
        abstract = data.get("abstract")
        abstract_str = str(abstract)
        if not abstract_str.strip():
            issues.append(Issue(path, "abstract", "Empty"))
        else:
            issues.extend(find_malformed_abstract_issues(path, abstract_str))

    # -- type --
    if "type" not in missing:
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
    if "audit_status" not in missing:
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
    parts = path.parts
    try:
        papers_idx = next(i for i, p in enumerate(parts) if p == "papers")
        path_year_str = parts[papers_idx + 1]
        path_slug = parts[papers_idx + 2]
    except (StopIteration, IndexError):
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
    if meta_year is not None and int(meta_year) != path_year:
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
    summary = data.get("summary")
    if not summary or not str(summary).strip():
        issues.append(
            Issue(path, "summary", "Missing or empty", severity=Severity.WARNING)
        )

    # -- optional field completeness (info) --
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

_TITLE_LINE_RE = re.compile(
    r"""^(title:\s*)(['"]?)(.*?)(['"]?)(\s*)$""",
    re.MULTILINE,
)


def _fix_title_in_yaml(raw: str, new_title: str) -> str:
    """Replace the title value in raw YAML text, preserving surrounding quoting."""

    def replacer(m: re.Match) -> str:
        prefix = m.group(1)
        q_open = m.group(2)
        q_close = m.group(4)
        needs_quotes = any(
            c in new_title for c in (":", "#", "[", "]", "{", "}", "&", "*", "!")
        )
        if needs_quotes and not q_open:
            return f'{prefix}"{new_title}"'
        return f"{prefix}{q_open}{new_title}{q_close}"

    return _TITLE_LINE_RE.sub(replacer, raw, count=1)


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
  authors   - ERROR if not a non-empty list of non-blank strings
  year      - ERROR if not a 4-digit integer
  arxiv_id  - ERROR if present but not a valid arXiv ID
  abstract  - ERROR if empty, contains scraped page text, or has PDF extraction artifacts
  escaped   - ERROR if string fields contain HTML/entity escapes like &#39; or &amp;
  type      - ERROR if not a recognised paper type
  audit_status - ERROR if not one of: raw, partial, reviewed
  path      - ERROR if YEAR/SLUG do not match metadata or expected slug format
  summary   - WARN if missing or empty
  optional  - INFO for each optional field that is not populated

Selective check flags are additive. If any are provided, only those check
families run:
  --check-escaped-sequences
  --check-malformed-abstracts
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
        "--check-escaped-sequences",
        action="append_const",
        const=CHECK_ESCAPED_SEQUENCES,
        dest="selected_checks",
        help="Check string fields for HTML/entity escape issues",
    )
    parser.add_argument(
        "--check-malformed-abstracts",
        "--check-abstract-issues",
        action="append_const",
        const=CHECK_MALFORMED_ABSTRACTS,
        dest="selected_checks",
        help="Check abstracts for scraped page text, PDF artifacts, and unusual length",
    )
    parser.add_argument(
        "--escaped-sequences-only",
        "--only-escaped-sequences",
        action="append_const",
        const=CHECK_ESCAPED_SEQUENCES,
        dest="selected_checks",
        help="Alias for --check-escaped-sequences",
    )
    args = parser.parse_args()
    selected_checks = set(args.selected_checks) if args.selected_checks else None

    if args.file:
        targets = [Path(args.file)]
    else:
        papers_root = Path(args.root) / "docs" / "papers"
        if not papers_root.exists():
            sys.exit(f"Papers directory not found: {papers_root}")
        targets = sorted(papers_root.rglob("metadata.yml"))

    results: list[tuple[Path, list[Issue]]] = []
    for p in targets:
        _, issues = audit_file(p, selected_checks=selected_checks)
        if issues:
            results.append((p, issues))

    all_issues = [i for _, issues in results for i in issues]
    n_errors = sum(1 for i in all_issues if i.severity == Severity.ERROR)
    n_warnings = sum(1 for i in all_issues if i.severity == Severity.WARNING)
    n_infos = sum(1 for i in all_issues if i.severity == Severity.INFO)

    if not all_issues:
        console.print(f"[green]All {len(targets)} metadata.yml file(s) pass audit.[/]")
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
            _, issues = audit_file(p, selected_checks=selected_checks)
            remaining_errors += sum(1 for i in issues if i.severity == Severity.ERROR)
        sys.exit(1 if remaining_errors else 0)

    sys.exit(1 if n_errors else 0)


if __name__ == "__main__":
    main()
