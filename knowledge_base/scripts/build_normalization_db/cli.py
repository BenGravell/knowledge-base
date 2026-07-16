"""CLI for building normalization databases."""

from __future__ import annotations

import argparse
import sys
from typing import Any

from knowledge_base.scripts.build_normalization_db.authors import build_author_entries
from knowledge_base.scripts.build_normalization_db.collect import collect_values, existing_entries
from knowledge_base.scripts.build_normalization_db.config import (
    AUTHORS_DB,
    AUTHORS_HEADER,
    KB_DIR,
    SOURCES_DB,
    SOURCES_HEADER,
    TAGS_DB,
    TAGS_HEADER,
)
from knowledge_base.scripts.build_normalization_db.sources import build_source_entries
from knowledge_base.scripts.build_normalization_db.tags import build_tag_entries
from knowledge_base.utils.normalization_db import dump_yaml


def main() -> int:
    parser = argparse.ArgumentParser(description="Build starter author/source/tag normalization databases.")
    parser.add_argument(
        "--update", action="store_true", help="Merge newly observed names/sources/tags into existing databases."
    )
    parser.add_argument(
        "--force", action="store_true", help="Rebuild databases from scratch even if they already exist."
    )
    parser.add_argument("--dry-run", action="store_true", help="Print counts without writing database files.")
    parser.add_argument(
        "--only",
        nargs="+",
        choices=("authors", "sources", "tags"),
        default=("authors", "sources", "tags"),
        help="Build only the selected normalization database(s).",
    )
    args = parser.parse_args()

    if args.update and args.force:
        parser.error("--update and --force are mutually exclusive")

    selected = set(args.only)
    selected_paths = {"authors": AUTHORS_DB, "sources": SOURCES_DB, "tags": TAGS_DB}
    existing_selected = [name for name, path in selected_paths.items() if name in selected and path.exists()]
    if not args.update and not args.force and existing_selected and not args.dry_run:
        print(
            "Normalization database(s) already exist for: "
            + ", ".join(existing_selected)
            + ". Use --update to merge new values or --force to rebuild.",
            file=sys.stderr,
        )
        return 2

    authors, sources, tags = collect_values()
    author_entries: list[dict[str, Any]] = []
    source_entries: list[dict[str, Any]] = []
    tag_entries: list[dict[str, Any]] = []
    if "authors" in selected:
        author_entries = build_author_entries(
            authors, existing=existing_entries(AUTHORS_DB, "authors") if args.update else []
        )
        print(f"Observed {len(authors)} author spellings -> {len(author_entries)} author entries.")
    if "sources" in selected:
        source_entries = build_source_entries(
            sources, existing=existing_entries(SOURCES_DB, "sources") if args.update else []
        )
        print(f"Observed {len(sources)} source spellings -> {len(source_entries)} source entries.")
    if "tags" in selected:
        tag_entries = build_tag_entries(tags, existing=existing_entries(TAGS_DB, "tags") if args.update else [])
        print(f"Observed {len(tags)} tag spellings -> {len(tag_entries)} tag entries.")

    if args.dry_run:
        return 0

    if "authors" in selected:
        dump_yaml(AUTHORS_DB, {"version": 1, "authors": author_entries}, header=AUTHORS_HEADER)
        print(f"Wrote {AUTHORS_DB.relative_to(KB_DIR)}")
    if "sources" in selected:
        dump_yaml(SOURCES_DB, {"version": 1, "sources": source_entries}, header=SOURCES_HEADER)
        print(f"Wrote {SOURCES_DB.relative_to(KB_DIR)}")
    if "tags" in selected:
        dump_yaml(TAGS_DB, {"version": 1, "tags": tag_entries}, header=TAGS_HEADER)
        print(f"Wrote {TAGS_DB.relative_to(KB_DIR)}")
    return 0
