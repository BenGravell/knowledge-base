"""Refresh step models."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Step:
    group: str
    label: str
    name: str
    command: list[str]


@dataclass(frozen=True)
class StepResult:
    step: Step
    duration_s: float
    returncode: int
