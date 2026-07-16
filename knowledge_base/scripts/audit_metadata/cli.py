"""Command-line entrypoint for the metadata auditor."""

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml

from knowledge_base.config import AUDIT_STATUS_FIELD, KB_DIR, VALID_AUDIT_STATUSES
from knowledge_base.progress import emit_progress
from knowledge_base.scripts.audit_metadata.file_audit import audit_file
from knowledge_base.scripts.audit_metadata.fixes.apply_fixes import apply_fixes, console
from knowledge_base.scripts.audit_metadata.generated_data.map_data import audit_map_data_paths
from knowledge_base.scripts.audit_metadata.support.checks import CHECK_PATH, CHECKS
from knowledge_base.scripts.audit_metadata.support.cli_help import CHECKS_EPILOG
from knowledge_base.scripts.audit_metadata.support.model import _SEVERITY_RANK, Issue, Severity
from knowledge_base.scripts.audit_metadata.support.yaml_support import _yaml_safe_load


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


def _audit_status(data: dict[str, Any]) -> str:
    return str(data.get(AUDIT_STATUS_FIELD) or "").strip()


def _read_audit_status(path: Path) -> str | None:
    try:
        data = _yaml_safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError):
        return None
    if not isinstance(data, dict):
        return None
    return _audit_status(data)


def _filter_targets_by_audit_status(
    targets: list[Path],
    audit_status: str,
) -> tuple[list[Path], int]:
    filtered: list[Path] = []
    unreadable = 0
    for path in targets:
        status = _read_audit_status(path)
        if status is None:
            unreadable += 1
            continue
        if status == audit_status:
            filtered.append(path)
    return filtered, unreadable


def _skip_reviewed_errors(data: dict[str, Any], issues: list[Issue]) -> tuple[list[Issue], int]:
    if _audit_status(data) != "reviewed":
        return issues, 0

    kept = [issue for issue in issues if issue.severity != Severity.ERROR]
    return kept, len(issues) - len(kept)


def _filter_results_by_severity(
    results: list[tuple[Path, list[Issue]]],
    *,
    minimum: Severity,
) -> list[tuple[Path, list[Issue]]]:
    minimum_rank = _SEVERITY_RANK[minimum]
    filtered: list[tuple[Path, list[Issue]]] = []
    for path, issues in results:
        kept = [issue for issue in issues if _SEVERITY_RANK[issue.severity] >= minimum_rank]
        if kept:
            filtered.append((path, kept))
    return filtered


def _default_kb_root() -> Path:
    return KB_DIR


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Audit metadata.yml files under knowledge_base/docs/papers/.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=CHECKS_EPILOG,
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=_default_kb_root(),
        help="Knowledge base root containing docs/papers (default: auto-detect)",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help=(
            "Auto-fix title-case, tag database aliases/casing/leading articles/duplicate tags, "
            "high-confidence missing tag canonical entries, "
            "abstract publisher/copyright notices, abstract dollar math/plain math artifacts, high-confidence OCR artifacts, "
            "escaped HTML/entity/markup issues, author-name mojibake/diacritics, "
            "text-field mojibake, obvious collective/split author entries, "
            "blank arXiv-backed type fields, copied or low-signal summaries, "
            "high-confidence parse artifacts, "
            "multiline scalar fields, folded text-field style/content, large whitespace runs, "
            "tight parenthetical abbreviation spacing, ASCII multi-dash punctuation, "
            "source years, and path slugs; "
            "path fixes move metadata directories "
            "after metadata edits and update direct references"
        ),
    )
    parser.add_argument(
        "--file",
        metavar="PATH",
        help="Audit a single metadata.yml instead of the whole tree",
    )
    parser.add_argument(
        "--audit-status",
        choices=VALID_AUDIT_STATUSES,
        metavar="STATUS",
        help=(
            "Audit only metadata files whose audit_status matches STATUS. Choices: " + ", ".join(VALID_AUDIT_STATUSES)
        ),
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
    parser.add_argument(
        "--metadata-only",
        action="store_true",
        help="Audit metadata files without checking generated Map and Semantic Search data",
    )
    parser.add_argument(
        "--severity",
        choices=[severity.value for severity in Severity],
        default=Severity.INFO.value,
        metavar="LEVEL",
        help=(
            "Minimum severity to report: error shows ERROR only; warning shows "
            "WARNING and ERROR; info shows INFO, WARNING, and ERROR (default: info)"
        ),
    )
    args = parser.parse_args()
    selected_names, invalid_names = _normalize_check_names(_flatten_check_args(args.check_names))
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
    kb_root = Path(args.root)
    if args.audit_status:
        targets, unreadable_status_count = _filter_targets_by_audit_status(
            targets,
            args.audit_status,
        )
        if unreadable_status_count:
            console.print(
                f"[dim]Skipped {unreadable_status_count} file(s) whose "
                f"{AUDIT_STATUS_FIELD} could not be read while applying "
                f"--audit-status {args.audit_status}.[/]"
            )
        if not targets:
            console.print(f"[yellow]No metadata.yml file(s) matched {AUDIT_STATUS_FIELD}: {args.audit_status}.[/]")
            return

    skipped_reviewed_errors = 0
    results: list[tuple[Path, list[Issue]]] = []
    metadata_by_path: dict[Path, dict[str, Any]] = {}
    checked_file_count = len(targets)
    checked_path_data = selected_checks is None or CHECK_PATH in selected_checks
    checked_generated_data = checked_path_data and not args.metadata_only
    report_stale_map_ids = not args.file and args.audit_status is None
    for index, p in enumerate(targets, start=1):
        data, issues = audit_file(p, selected_checks=selected_checks)
        if not any(issue.field == "parse" for issue in issues):
            metadata_by_path[p] = data
        if args.skip_reviewed_errors:
            issues, skipped_count = _skip_reviewed_errors(data, issues)
            skipped_reviewed_errors += skipped_count
        if issues:
            results.append((p, issues))
        emit_progress(index, len(targets), "Audit metadata files", every=25)
    if checked_generated_data:
        checked_file_count += 6
        results.extend(
            audit_map_data_paths(
                targets,
                kb_root=kb_root,
                report_stale=report_stale_map_ids,
                metadata_by_path=metadata_by_path,
            )
        )

    minimum_severity = Severity(args.severity)
    results = _filter_results_by_severity(results, minimum=minimum_severity)

    all_issues = [i for _, issues in results for i in issues]
    n_errors = sum(1 for i in all_issues if i.severity == Severity.ERROR)
    n_warnings = sum(1 for i in all_issues if i.severity == Severity.WARNING)
    n_infos = sum(1 for i in all_issues if i.severity == Severity.INFO)

    if not all_issues:
        if checked_generated_data:
            console.print(f"[green]All {len(targets)} metadata.yml file(s) and generated data pass audit.[/]")
        else:
            console.print(f"[green]All {len(targets)} metadata.yml file(s) pass audit.[/]")
        if skipped_reviewed_errors:
            console.print(f"[dim]Skipped {skipped_reviewed_errors} error(s) from reviewed metadata.[/]")
        return

    parts = []
    if n_errors:
        parts.append(f"[bold red]{n_errors} error(s)[/]")
    if n_warnings:
        parts.append(f"[bold yellow]{n_warnings} warning(s)[/]")
    if n_infos:
        parts.append(f"[bold cyan]{n_infos} info(s)[/]")
    console.print(", ".join(parts) + f" across {len(results)} / {checked_file_count} file(s):\n")
    if skipped_reviewed_errors:
        console.print(f"[dim]Skipped {skipped_reviewed_errors} error(s) from reviewed metadata.[/]\n")

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
        path_replacements = apply_fixes(
            results,
            kb_root=kb_root,
            fix_paths=checked_path_data,
        )
        if path_replacements:
            targets = [path_replacements.get(p, p) for p in targets]
        remaining_errors = 0
        for p in targets:
            data, issues = audit_file(p, selected_checks=selected_checks)
            if args.skip_reviewed_errors:
                issues, _ = _skip_reviewed_errors(data, issues)
            remaining_errors += sum(1 for i in issues if i.severity == Severity.ERROR)
        if checked_generated_data:
            map_results = audit_map_data_paths(
                targets,
                kb_root=kb_root,
                report_stale=report_stale_map_ids,
            )
            remaining_errors += sum(
                1 for _, issues in map_results for issue in issues if issue.severity == Severity.ERROR
            )
        sys.exit(1 if remaining_errors else 0)

    sys.exit(1 if n_errors else 0)
