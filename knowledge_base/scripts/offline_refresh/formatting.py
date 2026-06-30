"""Formatting helpers for refresh output."""

from __future__ import annotations

import shlex


def format_command(command: list[str]) -> str:
    return shlex.join(command)


def format_duration(duration_s: float) -> str:
    if duration_s < 60:
        return f"{duration_s:.1f}s"
    minutes, seconds = divmod(duration_s, 60)
    return f"{int(minutes)}m {seconds:.0f}s"


def format_status(failed: bool) -> str:
    return "[red]FAIL[/]" if failed else "[green]PASS[/]"
