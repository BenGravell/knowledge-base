"""JavaScript map-page smoke checks."""

from pathlib import Path

JS_CHECKS = Path(__file__).with_name("checks.js").read_text(encoding="utf-8")

__all__ = ["JS_CHECKS"]
