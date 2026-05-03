"""Batch-prefill metadata.yml files from a list of arXiv URLs/IDs.

Usage:
    python prefill_arxiv.py [--input PATH] [--overwrite]

Defaults:
    --input  ../../todo/ARXIV_PAPERS.md
    --overwrite  False (skip IDs whose metadata.yml already exists)
"""

import argparse
import re
import time
from pathlib import Path

import requests

from knowledge_base.apps.arxiv_utils import (
    build_metadata,
    fetch_arxiv,
    metadata_to_yaml,
    target_path,
    write_metadata,
)

DEFAULT_INPUT = Path(__file__).parent.parent.parent / "todo" / "ARXIV_PAPERS.md"
ARXIV_ID_RE = re.compile(r"arxiv\.org/(?:abs|pdf)/([^\s/?#]+)")

# Duration in seconds between successful requests
# Set to 5 seconds, well above 3 seconds required by arXiv Terms of Use (which requries 3 seconds)
# https://info.arxiv.org/help/api/tou.html
BASE_DELAY = 5.0      
# Max number of retries
MAX_RETRIES = 5
# seconds to wait after first 429; doubles each retry
BACKOFF_BASE = 10.0   


def extract_ids(path: Path) -> list[str]:
    seen: set[str] = set()
    ids: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = ARXIV_ID_RE.search(line)
        arxiv_id = m.group(1) if m else line
        arxiv_id = arxiv_id.rstrip("/")
        if arxiv_id and arxiv_id not in seen:
            seen.add(arxiv_id)
            ids.append(arxiv_id)
    return ids


def fetch_with_retry(arxiv_id: str) -> dict:
    delay = BACKOFF_BASE
    last_exc: Exception = RuntimeError("no attempts made")
    for attempt in range(MAX_RETRIES):
        try:
            return fetch_arxiv(arxiv_id)
        except requests.HTTPError as exc:
            last_exc = exc
            if exc.response is not None and exc.response.status_code == 429:
                if attempt + 1 == MAX_RETRIES:
                    break
                print(f"    429 error, waiting {delay:.0f}s (attempt {attempt + 1}/{MAX_RETRIES})")
                time.sleep(delay)
                delay *= 2
            else:
                raise
    raise last_exc


def main() -> None:
    parser = argparse.ArgumentParser(description="Prefill arXiv metadata files.")
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    parser.add_argument("--overwrite", action="store_true",
                        help="Overwrite existing metadata.yml files")
    args = parser.parse_args()

    ids = extract_ids(args.input)
    print(f"Found {len(ids)} unique arXiv IDs in {args.input}")

    ok = skipped = failed = 0

    for i, arxiv_id in enumerate(ids, 1):
        prefix = f"[{i}/{len(ids)}] {arxiv_id}"

        try:
            data = fetch_with_retry(arxiv_id)
        except Exception as exc:
            print(f"{prefix}  ERROR fetching: {exc}")
            failed += 1
            time.sleep(BASE_DELAY)
            continue

        out = target_path(arxiv_id, data["year"])

        if out.exists() and not args.overwrite:
            print(f"{prefix}  SKIP (exists: {out})")
            skipped += 1
            continue

        metadata = build_metadata(data)
        yaml_text = metadata_to_yaml(metadata)
        write_metadata(arxiv_id, data["year"], yaml_text)
        print(f"{prefix}  OK -> {out}")
        ok += 1

        if i < len(ids):
            time.sleep(BASE_DELAY)

    print(f"\nDone: {ok} written, {skipped} skipped, {failed} failed")


if __name__ == "__main__":
    main()
