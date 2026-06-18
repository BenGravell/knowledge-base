"""Tiny stdout/stderr progress protocol for long-running repository scripts."""

from __future__ import annotations

import os
import sys

PROGRESS_ENV = "KB_PROGRESS"
PROGRESS_PREFIX = "::kb-progress"


def emit_progress(current: int, total: int, label: str = "", *, every: int = 1) -> None:
    if not os.environ.get(PROGRESS_ENV) or total <= 0:
        return
    current = min(max(int(current), 0), int(total))
    if current != total and every > 1 and current % every:
        return
    suffix = f" {label}" if label else ""
    print(f"{PROGRESS_PREFIX} {current}/{int(total)}{suffix}", file=sys.stderr, flush=True)
