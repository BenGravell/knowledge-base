"""Command-line interface for normalization audit."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

from knowledge_base.scripts.normalization_audit.fixes import apply_fixes
from knowledge_base.scripts.normalization_audit.io import AUTHORS_DB, METADATA_ROOT, SOURCES_DB, TAGS_DB, load_entries
from knowledge_base.scripts.normalization_audit.model import Issue
from knowledge_base.scripts.normalization_audit.output import print_json, print_markdown
from knowledge_base.scripts.normalization_audit.rules import audit_file, build_author_lookup
from knowledge_base.utils.normalization_db import build_index, source_key, tag_key


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit author/source/tag metadata against normalization databases.")
    parser.add_argument(
        "--file",
        metavar="PATH",
        help="Audit one metadata.yml file instead of all papers.",
    )
    parser.add_argument(
        "--format",
        choices=("markdown", "json"),
        default="markdown",
        help="Output format (default: markdown).",
    )
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Apply suggestions for authors/source/tag fields.",
    )
    args = parser.parse_args()

    try:
        author_entries = load_entries(AUTHORS_DB, "authors")
        source_entries = load_entries(SOURCES_DB, "sources")
        tag_entries = load_entries(TAGS_DB, "tags")
    except FileNotFoundError as exc:
        print(
            f"Missing normalization database: {exc.filename}. Run scripts/build_normalization_db.py first.",
            file=sys.stderr,
        )
        return 2

    author_index, initial_index = build_author_lookup(author_entries)
    source_index = build_index(source_entries, key_fn=source_key)
    tag_index = build_index(tag_entries, key_fn=tag_key)

    targets = [Path(args.file)] if args.file else sorted(METADATA_ROOT.rglob("metadata.yml"))

    results: list[tuple[Path, dict[str, Any], list[Issue]]] = []
    for target in targets:
        data, issues = audit_file(target, author_index, initial_index, source_index, tag_index)
        if issues:
            results.append((target, data, issues))

    if not results:
        print(f"All {len(targets)} metadata.yml file(s) pass normalization audit.")
        return 0

    if args.format == "json":
        print_json(results)
    else:
        print_markdown(results)

    if args.fix:
        fixed_files = apply_fixes(results)
        print(f"\nFixed {fixed_files} file(s).")
        remaining = 0
        for target in targets:
            _, issues = audit_file(target, author_index, initial_index, source_index, tag_index)
            remaining += len(issues)
        return 1 if remaining else 0
    return 1
