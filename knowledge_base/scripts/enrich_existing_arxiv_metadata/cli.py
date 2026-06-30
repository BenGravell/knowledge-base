"""Command-line interface for enriching existing arXiv metadata."""

from __future__ import annotations

import argparse
import time

from knowledge_base.scripts.enrich_existing_arxiv_metadata.arxiv_api import fetch_batch
from knowledge_base.scripts.enrich_existing_arxiv_metadata.constants import BASE_DELAY
from knowledge_base.scripts.enrich_existing_arxiv_metadata.metadata import enrich, refresh_derived, target_files
from knowledge_base.scripts.enrich_existing_arxiv_metadata.text import bare_arxiv_id
from knowledge_base.scripts.enrich_existing_arxiv_metadata.yaml_io import load_yaml


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch-size", type=int, default=80)
    parser.add_argument("--delay", type=float, default=BASE_DELAY)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--refresh-derived",
        action="store_true",
        help="Refresh cautious algorithm labels from existing local metadata.",
    )
    args = parser.parse_args()

    paths = target_files(refresh_derived=args.refresh_derived)
    if args.limit:
        paths = paths[: args.limit]
    if args.refresh_derived:
        updated = 0
        for path in paths:
            if refresh_derived(path, dry_run=args.dry_run):
                updated += 1
        print(f"Done: {updated} refreshed")
        return

    by_id = {bare_arxiv_id(load_yaml(path).get("arxiv_id")): path for path in paths}
    ids = list(by_id)
    print(f"Found {len(ids)} raw arXiv-backed metadata files")

    updated = missing = failed = 0
    for start in range(0, len(ids), args.batch_size):
        chunk = ids[start : start + args.batch_size]
        print(f"Fetching {start + 1}-{start + len(chunk)} / {len(ids)}")
        try:
            records = fetch_batch(chunk)
        except Exception as exc:
            print(f"  ERROR batch fetch failed: {exc}")
            failed += len(chunk)
            time.sleep(BASE_DELAY)
            continue

        for arxiv_id in chunk:
            record = records.get(arxiv_id)
            if not record:
                print(f"  MISSING {arxiv_id}")
                missing += 1
                continue
            if args.dry_run or enrich(by_id[arxiv_id], record):
                updated += 1
        time.sleep(args.delay)

    print(f"Done: {updated} updated, {missing} missing, {failed} failed")
