"""Normalization audit output formats."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from knowledge_base.scripts.normalization_audit.io import KB_DIR
from knowledge_base.scripts.normalization_audit.model import Issue


def relative_to_kb(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(KB_DIR.resolve()))
    except ValueError:
        return str(path)


def print_markdown(results: list[tuple[Path, dict[str, Any], list[Issue]]]) -> None:
    issue_count = sum(len(issues) for _, _, issues in results)
    print(f"# Normalization Audit\n\n{issue_count} issue(s) across {len(results)} file(s).\n")
    for path, _, issues in results:
        print(f"- `{relative_to_kb(path)}`")
        for issue in issues:
            print(f"  - [{issue.field}] {issue.message}")
            if issue.suggestion:
                print(f"    - Suggested: `{issue.suggestion}`")


def print_json(results: list[tuple[Path, dict[str, Any], list[Issue]]]) -> None:
    payload = [
        {
            "path": relative_to_kb(path),
            "issues": [
                {
                    "field": issue.field,
                    "message": issue.message,
                    "suggestion": issue.suggestion,
                    "rule": issue.rule,
                    "index": issue.index,
                }
                for issue in issues
            ],
        }
        for path, _, issues in results
    ]
    print(json.dumps(payload, indent=2, ensure_ascii=False))
