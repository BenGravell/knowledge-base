"""Backfill the next missing arXiv full-text sidecars."""

from __future__ import annotations

import argparse
import shutil
import sys
import time

from ingest_arxiv_full_text import (
    DEFAULT_SLEEP_SECONDS,
    METADATA_ROOT,
    MIN_MARKDOWN_CHARS,
    full_text_path,
    process_entry,
)
from knowledge_base.catalog import Catalog, Entry


def missing_entries(offset: int, batch_size: int) -> tuple[list[Entry], int]:
    entries = [
        entry
        for entry in Catalog.from_metadata_root(METADATA_ROOT).entries
        if entry.arxiv_id and not full_text_path(entry).exists()
    ]
    return entries[offset : offset + batch_size], len(entries)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-size", type=int, default=10, help="Number of missing sidecars to attempt.")
    parser.add_argument("--offset", type=int, default=0, help="Skip this many missing candidates before the batch.")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and convert, but do not write files.")
    parser.add_argument("--sleep", type=float, default=DEFAULT_SLEEP_SECONDS, help="Delay between entries.")
    parser.add_argument("--timeout", type=int, default=60, help="HTTP timeout in seconds.")
    parser.add_argument("--min-chars", type=int, default=MIN_MARKDOWN_CHARS, help="Minimum readable output size.")
    parser.add_argument("--pandoc", default="pandoc", help="Pandoc executable.")
    parser.add_argument("--pandoc-data-dir", default="", help="Optional Pandoc data directory.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    args.force = False

    if args.batch_size < 1:
        raise SystemExit("--batch-size must be at least 1")
    if args.offset < 0:
        raise SystemExit("--offset must be non-negative")
    if not shutil.which(args.pandoc):
        raise SystemExit(f"Pandoc executable not found: {args.pandoc}")

    entries, total_missing = missing_entries(args.offset, args.batch_size)
    if not entries:
        print("no missing arXiv full-text sidecars in this batch")
        return 0

    print(f"attempting {len(entries)} of {total_missing} missing arXiv full-text sidecar(s)")
    for index, entry in enumerate(entries):
        print(process_entry(entry, args))
        if args.sleep and index < len(entries) - 1:
            time.sleep(args.sleep)

    remaining = missing_entries(0, 1)[1]
    print(f"attempted {len(entries)} candidate(s); {remaining} missing sidecar(s) remain")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
