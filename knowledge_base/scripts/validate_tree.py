"""Validate ``tree.yml`` local links and paper coverage.

Usage:
  python scripts/validate_tree.py
  python scripts/validate_tree.py --check-algorithm-labels
  python scripts/validate_tree.py --format json
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from knowledge_base.config import KB_DIR
from knowledge_base.progress import emit_progress
from knowledge_base.tree.validation import (
    format_tree_validation_report,
    relative_to_kb,
    validate_tree,
)


def issue_to_dict(issue: Any) -> dict[str, Any]:
    return {
        "code": issue.code,
        "message": issue.message,
        "tree_label": issue.tree_label,
        "algorithm": issue.algorithm,
        "source": issue.source,
        "expected_path": relative_to_kb(issue.expected_path) if issue.expected_path else None,
        "metadata_path": relative_to_kb(issue.metadata_path) if issue.metadata_path else None,
        "generated_path": issue.generated_path,
        "nav_path": list(issue.nav_path),
    }


def report_to_dict(report: Any) -> dict[str, Any]:
    return {
        "ok": report.ok,
        "tree_path": relative_to_kb(report.tree_path),
        "docs_dir": relative_to_kb(report.docs_dir),
        "metadata_root": relative_to_kb(report.metadata_root),
        "checked_links": report.checked_links,
        "metadata_count": report.metadata_count,
        "referenced_papers": report.referenced_papers,
        "issues": [issue_to_dict(issue) for issue in report.issues],
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate tree.yml links and metadata-backed paper placement.")
    parser.add_argument(
        "--tree-yml",
        type=Path,
        default=KB_DIR / "tree.yml",
        help="Path to the Tree YAML source.",
    )
    parser.add_argument(
        "--docs-dir",
        type=Path,
        default=KB_DIR / "docs",
        help="Path to the MkDocs docs directory.",
    )
    parser.add_argument(
        "--metadata-root",
        type=Path,
        default=KB_DIR / "docs" / "papers",
        help="Path to docs/papers metadata source.",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json"),
        default="text",
        help="Output format.",
    )
    parser.add_argument(
        "--check-algorithm-labels",
        action="store_true",
        help=("Fail when a metadata-backed Tree leaf label and non-empty metadata algorithm field disagree."),
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=None,
        help="Limit issue rows displayed in text output.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    report = validate_tree(
        args.tree_yml,
        docs_dir=args.docs_dir,
        metadata_root=args.metadata_root,
        check_algorithm_labels=args.check_algorithm_labels,
        progress_callback=lambda current, total, label: emit_progress(current, total, label, every=100),
    )

    if args.format == "json":
        print(json.dumps(report_to_dict(report), indent=2, ensure_ascii=False))
    else:
        print(format_tree_validation_report(report, max_results=args.max_results))

    return 0 if report.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
