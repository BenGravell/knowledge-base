"""Process environment helpers for refresh subprocesses."""

from __future__ import annotations

import os


def subprocess_env(progress_env: str) -> dict[str, str]:
    env = os.environ.copy()
    env.setdefault("PYTHONUNBUFFERED", "1")
    env[progress_env] = "1"
    return env
