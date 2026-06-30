"""Per-file metadata audit orchestration."""

# ruff: noqa: F811

from pathlib import Path
from typing import Any

import yaml

from knowledge_base.config import (
    AUDIT_STATUS_FIELD,
    REQUIRED_FIELDS,
    VALID_AUDIT_STATUSES,
    VALID_FIELDS,
    VALID_TYPES,
)
from knowledge_base.scripts.audit_metadata.fixes.title_fixes import (
    _suggest_title_fix,
    _title_has_garbage,
    _yaml_safe_load,
)
from knowledge_base.scripts.audit_metadata.rules.abstract_rules import (
    find_low_signal_summary_issues,
    find_malformed_abstract_issues,
    find_summary_abstract_overlap_issues,
)
from knowledge_base.scripts.audit_metadata.rules.algorithm import find_algorithm_issues
from knowledge_base.scripts.audit_metadata.rules.author_checks import find_author_field_issues
from knowledge_base.scripts.audit_metadata.rules.encoding import (
    find_weird_text_character_issues,
)
from knowledge_base.scripts.audit_metadata.rules.path_checks import find_path_issues
from knowledge_base.scripts.audit_metadata.rules.string_fields import (
    find_ascii_multi_dash_issues,
    find_big_whitespace_issues,
    find_escaped_sequence_issues,
    find_tight_letter_parenthetical_spacing_issues,
)
from knowledge_base.scripts.audit_metadata.rules.tags import find_tag_issues
from knowledge_base.scripts.audit_metadata.rules.text_quality import (
    find_high_confidence_ocr_artifact_issues,
    find_likely_misspelling_issues,
    find_ocr_spacing_issues,
)
from knowledge_base.scripts.audit_metadata.rules.url_rules import (
    _looks_like_url,
    _strip_years_from_source,
    find_disallowed_url_issues,
    find_garbled_markup_issues,
)
from knowledge_base.scripts.audit_metadata.rules.yaml_fields import (
    find_multiline_field_issues,
    find_title_character_escape_issues,
)
from knowledge_base.scripts.audit_metadata.support.checks import (
    CHECK_ABSTRACT,
    CHECK_ALGORITHM,
    CHECK_ARXIV,
    CHECK_AUTHORS,
    CHECK_DASH,
    CHECK_ESCAPE,
    CHECK_MULTILINE,
    CHECK_OPTIONAL,
    CHECK_PATH,
    CHECK_REQUIRED,
    CHECK_SOURCE,
    CHECK_STATUS,
    CHECK_SUMMARY,
    CHECK_TAGS,
    CHECK_TITLE,
    CHECK_TYPE,
    CHECK_UNKNOWN,
    CHECK_URL,
    CHECK_WHITESPACE,
    CHECK_YEAR,
)
from knowledge_base.scripts.audit_metadata.support.model import (
    RULE_SOURCE_YEAR,
    RULE_TITLE_VALUE,
    RULE_TYPE_VALUE,
    Issue,
    Path,
    Severity,
)
from knowledge_base.scripts.audit_metadata.support.slugs import is_valid_arxiv_id
from knowledge_base.scripts.audit_metadata.support.yaml_support import _yaml_safe_load

_EMPTY_ABSTRACT_ISSUE_PREFIX = "Empty abstract"
_EMPTY_SUMMARY_ISSUE_PREFIX = "Missing or empty"
_LOW_SIGNAL_SUMMARY_ISSUE_PREFIX = "Low-signal generated summary"
_LOW_SIGNAL_SUMMARY_PHRASE = (
    "It is useful as a compact reference for the problem formulation, "
    "main assumptions, and evaluation setting behind the contribution."
)


def audit_file(
    path: Path,
    *,
    selected_checks: set[str] | None = None,
) -> tuple[dict[str, Any], list[Issue]]:
    issues: list[Issue] = []

    def should_check(check: str) -> bool:
        return selected_checks is None or check in selected_checks

    try:
        raw = path.read_text(encoding="utf-8")
        data = _yaml_safe_load(raw)
    except yaml.YAMLError as exc:
        issues.append(Issue(path, "parse", f"YAML parse error: {exc}"))
        return {}, issues

    if not isinstance(data, dict):
        issues.append(Issue(path, "parse", "Root YAML value is not a mapping"))
        return {}, issues

    if should_check(CHECK_ESCAPE):
        issues.extend(find_escaped_sequence_issues(path, data))

    if should_check(CHECK_URL):
        issues.extend(find_disallowed_url_issues(path, data))
        issues.extend(find_garbled_markup_issues(path, data))

    if should_check(CHECK_MULTILINE):
        issues.extend(find_multiline_field_issues(path, raw, data))

    if should_check(CHECK_DASH):
        issues.extend(find_ascii_multi_dash_issues(path, data))

    if should_check(CHECK_WHITESPACE):
        issues.extend(find_big_whitespace_issues(path, data))
        issues.extend(find_tight_letter_parenthetical_spacing_issues(path, data))

    # -- unknown fields --
    if should_check(CHECK_UNKNOWN):
        _valid_set = set(VALID_FIELDS)
        issues.extend(Issue(path, key, f"Unknown field {key!r}") for key in data if key not in _valid_set)

    # -- required fields presence --
    missing = {f for f in REQUIRED_FIELDS if data.get(f) is None}
    if should_check(CHECK_REQUIRED):
        issues.extend(Issue(path, f, "Missing required field") for f in sorted(missing))

    # -- title --
    title_raw = data.get("title")
    title = str(title_raw).strip() if title_raw not in (None, "") else ""
    title_corrected = title
    if title and should_check(CHECK_TITLE):
        title_corrected = _suggest_title_fix(raw, title)
    if title and (should_check(CHECK_TITLE) or should_check(CHECK_ESCAPE)):
        issues.extend(find_title_character_escape_issues(path, raw, title_corrected))
    if should_check(CHECK_TITLE) and "title" not in missing:
        if not title:
            issues.append(Issue(path, "title", "Empty"))
        else:
            issues.extend(find_weird_text_character_issues(path, "title", title))
            issues.extend(find_likely_misspelling_issues(path, "title", title))
            issues.extend(find_high_confidence_ocr_artifact_issues(path, "title", title))
            if title != title_corrected:
                message = (
                    f"Contains title markup/math garbage: {title!r}"
                    if _title_has_garbage(title)
                    else f"Not in title case: {title!r}"
                )
                issues.append(
                    Issue(
                        path,
                        "title",
                        message,
                        title_corrected,
                        rule=RULE_TITLE_VALUE,
                    )
                )

    # -- algorithm --
    if should_check(CHECK_ALGORITHM):
        issues.extend(find_algorithm_issues(path, data))

    # -- authors --
    authors_raw = data.get("authors")
    authors: list[Any] = authors_raw if isinstance(authors_raw, list) else []
    if should_check(CHECK_AUTHORS) and "authors" not in missing:
        issues.extend(find_author_field_issues(path, authors_raw, authors))

    # -- tags --
    if should_check(CHECK_TAGS):
        issues.extend(find_tag_issues(path, data))

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

    # -- source --
    if should_check(CHECK_SOURCE):
        source_raw = data.get("source")
        source = str(source_raw).strip() if source_raw not in (None, "") else ""
        if source and not _looks_like_url(source):
            source_without_years = _strip_years_from_source(source)
            if source_without_years != source:
                issues.append(
                    Issue(
                        path,
                        "source",
                        f"Contains year in source field: {source!r}",
                        source_without_years,
                        rule=RULE_SOURCE_YEAR,
                    )
                )

    # -- abstract --
    if should_check(CHECK_ABSTRACT) and "abstract" not in missing:
        abstract = data.get("abstract")
        abstract_str = str(abstract)
        if not abstract_str.strip():
            issues.append(
                Issue(
                    path,
                    "abstract",
                    _EMPTY_ABSTRACT_ISSUE_PREFIX,
                    "Fill from the source when an abstract exists; leave blank only after verifying the source has no abstract.",
                    severity=Severity.WARNING,
                )
            )
        else:
            issues.extend(find_weird_text_character_issues(path, "abstract", abstract_str))
            issues.extend(find_likely_misspelling_issues(path, "abstract", abstract_str))
            issues.extend(
                find_high_confidence_ocr_artifact_issues(
                    path,
                    "abstract",
                    abstract_str,
                )
            )
            issues.extend(find_ocr_spacing_issues(path, "abstract", abstract_str))
            audit_status = str(data.get(AUDIT_STATUS_FIELD) or "").strip()
            issues.extend(
                find_malformed_abstract_issues(
                    path,
                    abstract_str,
                    allow_short=audit_status == "reviewed",
                )
            )

    # -- type --
    if should_check(CHECK_TYPE) and "type" not in missing:
        paper_type = data.get("type")
        type_str = str(paper_type).strip() if paper_type not in (None, "") else ""
        if type_str not in VALID_TYPES:
            type_suggestion = None
            link = str(data.get("link") or "")
            if not type_str and (arxiv_id or "arxiv.org" in link.casefold()):
                type_suggestion = "Preprint"
            issues.append(
                Issue(
                    path,
                    "type",
                    f"Invalid value {type_str!r}; must be one of: {sorted(VALID_TYPES)}",
                    type_suggestion,
                    rule=RULE_TYPE_VALUE,
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
        path_issues, stop = find_path_issues(path, data, authors, title, arxiv_id)
        issues.extend(path_issues)
        if stop:
            return data, issues

    # -- summary --
    if should_check(CHECK_SUMMARY):
        summary = data.get("summary")
        audit_status = str(data.get(AUDIT_STATUS_FIELD) or "").strip()
        if not summary or not str(summary).strip():
            if audit_status != "raw":
                issues.append(
                    Issue(
                        path,
                        "summary",
                        _EMPTY_SUMMARY_ISSUE_PREFIX,
                        severity=Severity.WARNING,
                    )
                )
        else:
            issues.extend(find_low_signal_summary_issues(path, str(summary)))
            issues.extend(find_likely_misspelling_issues(path, "summary", str(summary)))
            issues.extend(
                find_high_confidence_ocr_artifact_issues(
                    path,
                    "summary",
                    str(summary),
                )
            )
            if "abstract" not in missing:
                issues.extend(
                    find_summary_abstract_overlap_issues(
                        path,
                        str(summary),
                        str(data.get("abstract") or ""),
                    )
                )

    # -- optional field completeness (info) --
    if should_check(CHECK_OPTIONAL):
        audit_status_val = str(data.get(AUDIT_STATUS_FIELD) or "").strip()
        if audit_status_val == "raw":
            issues.append(
                Issue(path, AUDIT_STATUS_FIELD, "raw; skipping optional field checks", severity=Severity.INFO)
            )
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


__all__ = ["audit_file"]
