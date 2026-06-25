"""Compatibility wrapper for arXiv full-text ingest."""

from __future__ import annotations

from knowledge_base.scripts.arxiv_full_text.ingest import (
    DEFAULT_SLEEP_SECONDS,
    METADATA_ROOT,
    MIN_MARKDOWN_CHARS,
    candidates,
    embed_text_path,
    main,
    process_entry,
    self_test,
)

__all__ = [
    "DEFAULT_SLEEP_SECONDS",
    "METADATA_ROOT",
    "MIN_MARKDOWN_CHARS",
    "candidates",
    "embed_text_path",
    "main",
    "process_entry",
    "self_test",
]


if __name__ == "__main__":
    raise SystemExit(main())
