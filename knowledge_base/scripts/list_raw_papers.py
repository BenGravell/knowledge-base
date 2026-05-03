"""List all metadata.yml files under knowledge_base/docs/papers/ with audit_status = raw.

Usage:
  python scripts/list_raw_papers.py [ROOT]
"""

import argparse
import sys
from pathlib import Path

import yaml
from rich.console import Console

from knowledge_base.config import AUDIT_STATUS_FIELD

console = Console(highlight=False)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="List papers with audit_status = raw.",
    )
    parser.add_argument(
        "root",
        nargs="?",
        default=".",
        help="Repository root (default: current directory)",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=None,
        metavar="N",
        help="Limit output to the first N results",
    )
    args = parser.parse_args()

    papers_root = Path(args.root) / "docs" / "papers"
    if not papers_root.exists():
        sys.exit(f"Papers directory not found: {papers_root}")

    targets = sorted(papers_root.rglob("metadata.yml"))
    raw_paths: list[Path] = []
    errors = 0

    for path in targets:
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            console.print(f"[red]YAML error:[/] {path}: {exc}", stderr=True)
            errors += 1
            continue

        if not isinstance(data, dict):
            continue

        if str(data.get(AUDIT_STATUS_FIELD, "")).strip() == "raw":
            raw_paths.append(path)

    display_paths = raw_paths[: args.max_results] if args.max_results is not None else raw_paths
    for p in display_paths:
        console.print(str(p))

    truncated = len(raw_paths) - len(display_paths)
    summary = f"\n[bold]{len(display_paths)}[/] raw paper(s) shown"
    if truncated:
        summary += f" ([dim]{truncated} more not shown[/])"
    summary += f" out of [dim]{len(targets)}[/] total."
    console.print(summary)

    if args.max_results is not None:
        console.print(f"\n[bold orange1]Results limited to first {args.max_results}. Omit --max-results to see all.[/]")

    if errors:
        sys.exit(1)


if __name__ == "__main__":
    main()
