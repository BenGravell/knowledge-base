"""Shared constants and path helpers for branch subgroup suggestions."""

from typing import Any

BROAD_TERMS = {
    "algorithm",
    "algorithms",
    "analysis",
    "applications",
    "control",
    "deep learning",
    "learning",
    "machine learning",
    "method",
    "methods",
    "model",
    "models",
    "optimization",
    "planning",
    "reinforcement learning",
    "robotics",
    "survey",
    "surveys",
    "theory",
}


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


__all__ = [name for name in globals() if not (name.startswith("__") and name.endswith("__"))]
