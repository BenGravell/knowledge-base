"""Batch-prefill metadata.yml files from a list of arXiv URLs/IDs.

Usage:
    python knowledge_base/scripts/prefill/arxiv.py [--input PATH] [--overwrite]

Defaults:
    --input  todo/papers/ARXIV.md
    --overwrite  False (skip IDs whose metadata.yml already exists)
"""

from collections.abc import Callable
from pathlib import Path
from typing import Any

from knowledge_base.scripts.prefill.arxiv_fetch import (
    ARXIV_URL_RE,
    BATCH_SIZE,
    ArxivBatchCache,
    extract_ids,
    fetch_with_retry,
)
from knowledge_base.utils.arxiv_utils import (
    build_metadata,
    normalize_arxiv_id,
    target_path,
    write_metadata,
)
from knowledge_base.utils.doi_utils import find_existing_by_arxiv_id
from knowledge_base.utils.prefill_template import REPO_ROOT, FieldMap

DEFAULT_INPUT = REPO_ROOT / "todo" / "papers" / "ARXIV.md"


def extract_entries(path: Path, record_parse_failure: Callable[[str], None] | None = None) -> list[str]:
    _ = record_parse_failure
    return extract_ids(path)


def prepare_context(entries: list[str], args: Any) -> dict[str, Any]:
    batch_size = BATCH_SIZE
    if args.first is not None:
        batch_size = max(1, min(BATCH_SIZE, args.first))
    return {"batch_cache": ArxivBatchCache(entries, batch_size=batch_size)}


def source_key_for_entry(entry: str) -> str | None:
    return normalize_arxiv_id(entry)


def source_key_for_token(token: str) -> str | None:
    m = ARXIV_URL_RE.search(token)
    arxiv_id = m.group(1) if m else token
    arxiv_id = normalize_arxiv_id(arxiv_id)
    return arxiv_id or None


def existing_for_entry(entry: str, context: dict[str, Any]) -> Path | None:
    _ = context
    return find_existing_by_arxiv_id(entry)


def needs_fetch_for_list_skipped(entry: str, context: dict[str, Any]) -> bool:
    _ = (entry, context)
    return False


def fetch_fields(entry: str, context: dict[str, Any]) -> FieldMap:
    batch_cache = context.get("batch_cache")
    if batch_cache is None:
        return fetch_with_retry(entry)
    return batch_cache.fetch(entry)


def build_prefill_metadata(entry: str, fields: FieldMap) -> FieldMap:
    _ = entry
    return build_metadata(fields)


def write_prefill_metadata(entry: str, fields: FieldMap, yaml_text: str) -> Path:
    return write_metadata(entry, fields["year"], yaml_text)


def success_message(prefix: str, entry: str, fields: FieldMap, out: Path) -> str:
    _ = out
    return f"{prefix}  OK -> {target_path(entry, fields['year'])}"
