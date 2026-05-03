"""Audit (and optionally fix) metadata.yml files under knowledge_base/docs/papers/."""

import argparse
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
# Per-file audit
# ---------------------------------------------------------------------------


def audit_file(path: Path) -> tuple[dict, list[Issue]]:
    issues: list[Issue] = []

    try:
        raw = path.read_text(encoding="utf-8")
        data = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        issues.append(Issue(path, "parse", f"YAML parse error: {exc}"))
        return {}, issues

    if not isinstance(data, dict):
        issues.append(Issue(path, "parse", "Root YAML value is not a mapping"))
        return {}, issues

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
        if not str(abstract).strip():
            issues.append(Issue(path, "abstract", "Empty"))

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


def apply_fixes(results: list[tuple[Path, list[Issue]]]) -> None:
    fixed = 0
    for path, issues in results:
        title_fixes = [
            i for i in issues if i.field == "title" and i.suggestion is not None
        ]
        if not title_fixes:
            continue
        new_title = title_fixes[0].suggestion
        try:
            raw = path.read_text(encoding="utf-8")
            new_raw = _fix_title_in_yaml(raw, new_title)
            if new_raw == raw:
                err_console.print(f"  [dim](no change written for {path})[/]")
                continue
            path.write_text(new_raw, encoding="utf-8")
            old_title = yaml.safe_load(raw).get("title", "")
            console.print(
                f"[green]Fixed:[/] {path}\n  {old_title!r}\n  [green]->[/] {new_title!r}"
            )
            fixed += 1
        except Exception as exc:
            err_console.print(f"[red]Error fixing {path}:[/] {exc}")
    console.print(f"\n[green]{fixed} file(s) fixed.[/]")


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
  abstract  - ERROR if empty
  type      - ERROR if not a recognised paper type
  audit_status - ERROR if not one of: raw, partial, reviewed
  path      - ERROR if YEAR/SLUG do not match metadata or expected slug format
  summary   - WARN if missing or empty
  optional  - INFO for each optional field that is not populated
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
        help="Auto-fix title-case issues (rewrites files in place)",
    )
    parser.add_argument(
        "--file",
        metavar="PATH",
        help="Audit a single metadata.yml instead of the whole tree",
    )
    args = parser.parse_args()

    if args.file:
        targets = [Path(args.file)]
    else:
        papers_root = Path(args.root) / "docs" / "papers"
        if not papers_root.exists():
            sys.exit(f"Papers directory not found: {papers_root}")
        targets = sorted(papers_root.rglob("metadata.yml"))

    results: list[tuple[Path, list[Issue]]] = []
    for p in targets:
        _, issues = audit_file(p)
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

    sys.exit(1 if n_errors else 0)


if __name__ == "__main__":
    main()
