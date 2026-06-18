"""Backfill the next missing arXiv embedding-text sidecars."""

from __future__ import annotations

import argparse
import shutil
import sys
import time
from pathlib import Path

from knowledge_base.catalog import Catalog, Entry
from knowledge_base.scripts.ingest_arxiv_full_text import (
    DEFAULT_SLEEP_SECONDS,
    METADATA_ROOT,
    MIN_MARKDOWN_CHARS,
    embed_text_path,
    process_entry,
)

DEFAULT_SKIP_LOG = Path(".cache/arxiv_embed_text_backfill_skips.txt")


def skipped_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {line.split("\t", 1)[0].strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}


def record_skip(path: Path, entry: Entry, message: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(f"{entry.arxiv_id}\t{entry.id}\t{message}\n")


def missing_entries(offset: int, batch_size: int, skipped: set[str]) -> tuple[list[Entry], int]:
    entries = [
        entry
        for entry in Catalog.from_metadata_root(METADATA_ROOT).entries
        if entry.arxiv_id and entry.arxiv_id not in skipped and not embed_text_path(entry).exists()
    ]
    return entries[offset : offset + batch_size], len(entries)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-size", type=int, default=10, help="Number of missing embed-text sidecars to attempt.")
    parser.add_argument("--offset", type=int, default=0, help="Skip this many missing candidates before the batch.")
    parser.add_argument("--dry-run", action="store_true", help="Fetch and convert, but do not write files.")
    parser.add_argument("--sleep", type=float, default=DEFAULT_SLEEP_SECONDS, help="Delay between entries.")
    parser.add_argument("--timeout", type=int, default=60, help="HTTP timeout in seconds.")
    parser.add_argument("--min-chars", type=int, default=MIN_MARKDOWN_CHARS, help="Minimum readable output size.")
    parser.add_argument("--pandoc", default="pandoc", help="Pandoc executable.")
    parser.add_argument("--pandoc-data-dir", default="", help="Optional Pandoc data directory.")
    parser.add_argument("--skip-log", type=Path, default=DEFAULT_SKIP_LOG, help="Ignored local log for failed IDs.")
    parser.add_argument("--retry-skips", action="store_true", help="Ignore the skip log for this run.")
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

    skipped = set() if args.retry_skips else skipped_ids(args.skip_log)
    entries, total_missing = missing_entries(args.offset, args.batch_size, skipped)
    if not entries:
        print("no missing arXiv embedding-text sidecars in this batch")
        return 0

    print(f"attempting {len(entries)} of {total_missing} missing arXiv embedding-text sidecar(s)")
    for index, entry in enumerate(entries):
        message = process_entry(entry, args)
        print(message)
        if not args.dry_run and not message.startswith("wrote "):
            record_skip(args.skip_log, entry, message)
        if args.sleep and index < len(entries) - 1:
            time.sleep(args.sleep)

    skipped = set() if args.retry_skips else skipped_ids(args.skip_log)
    remaining = missing_entries(0, 1, skipped)[1]
    print(f"attempted {len(entries)} candidate(s); {remaining} missing embed-text sidecar(s) remain")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
