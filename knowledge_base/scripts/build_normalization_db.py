"""Compatibility wrapper for normalization database generation."""

from __future__ import annotations

from knowledge_base.scripts.build_normalization_db.cli import main

if __name__ == "__main__":
    raise SystemExit(main())
