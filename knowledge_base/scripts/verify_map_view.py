"""Compatibility wrapper for the map view verifier package."""

from __future__ import annotations

import sys

from knowledge_base.scripts.verify_map_view.cli import main

if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
