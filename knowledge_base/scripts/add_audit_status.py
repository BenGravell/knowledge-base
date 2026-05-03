"""Add audit_status field to metadata.yml files that are missing it.

Lifecycle stages (in order):
  raw       - auto-generated/imported, never manually reviewed
  partial   - some fields manually reviewed or corrected, but not complete
  reviewed  - all key fields verified, good summary present

Usage:
  python scripts/add_audit_status [ROOT] [--dry-run] [--file PATH]
"""

import argparse
import sys
from pathlib import Path

import yaml
from rich.console import Console

console = Console(highlight=False)

AUDIT_STATUS_FIELD = "audit_status"
VALID_STATUSES = ("raw", "partial", "reviewed")
DEFAULT_STATUS = "raw"


def _has_audit_status(path: Path) -> bool:
    raw = path.read_text(encoding="utf-8")
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError:
        return False
    return isinstance(data, dict) and AUDIT_STATUS_FIELD in data


def _append_audit_status(path: Path, status: str, dry_run: bool) -> bool:
    """Append audit_status field at the end of the file. Returns True if changed."""
    raw = path.read_text(encoding="utf-8")

    # Strip trailing whitespace/newlines, then append the field
    stripped = raw.rstrip()
    new_raw = stripped + f"\n{AUDIT_STATUS_FIELD}: {status}\n"

    if dry_run:
        return True

    path.write_text(new_raw, encoding="utf-8")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Add audit_status field to metadata.yml files missing it.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=f"""
Audit status lifecycle:
  raw       - auto-generated/imported, never manually reviewed
  partial   - some fields manually reviewed, not yet complete
  reviewed  - all key fields verified, good summary written

Files that already have audit_status are left untouched.
""",
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Repository root (default: current directory)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without writing files",
    )
    parser.add_argument(
        "--file",
        metavar="PATH",
        help="Process a single metadata.yml instead of the whole tree",
    )
    parser.add_argument(
        "--status",
        default=DEFAULT_STATUS,
        choices=VALID_STATUSES,
        help=f"Status to assign to new fields (default: {DEFAULT_STATUS})",
    )
    args = parser.parse_args()

    if args.file:
        targets = [Path(args.file)]
    else:
        papers_root = Path(args.root) / "docs" / "papers"
        if not papers_root.exists():
            sys.exit(f"Papers directory not found: {papers_root}")
        targets = sorted(papers_root.rglob("metadata.yml"))

    added = 0
    skipped = 0
    errors = 0

    for path in targets:
        try:
            if _has_audit_status(path):
                skipped += 1
                continue
            _append_audit_status(path, args.status, args.dry_run)
            added += 1
            verb = "[yellow]Would add[/]" if args.dry_run else "[green]Added[/]"
            console.print(f"{verb} [dim]{path}[/]")
        except Exception as exc:
            errors += 1
            console.print(f"[red]Error:[/] {path}: {exc}", stderr=True)

    dry = " (dry run)" if args.dry_run else ""
    console.print(
        f"\n[bold]{added}[/] file(s) updated{dry}, "
        f"[dim]{skipped}[/] already had {AUDIT_STATUS_FIELD!r}, "
        f"[red]{errors}[/] error(s)."
    )

    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
