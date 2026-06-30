"""Shared constants and path helpers for branch subgroup suggestions."""

from pathlib import Path
from typing import Any, Literal

from knowledge_base.config import KB_DIR

DOCS_DIR = KB_DIR / "docs"
METADATA_ROOT = DOCS_DIR / "papers"
EMBEDDING_CACHE = KB_DIR / "components" / "map" / "cache" / "embedding_cache.json"
LANDING_PAGES = {"tree.md", "tree/index.md"}
CountMode = Literal["all", "branches"]

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


def display_path(path: tuple[str, ...]) -> tuple[str, ...]:
    return path if path == ("Tree",) else ("Tree", *path)


def tree_yml_path(path: tuple[str, ...]) -> tuple[str, ...]:
    return display_path(path)


def format_path(path: tuple[str, ...]) -> str:
    return " > ".join(display_path(path))


def relative_to_kb(path: Path) -> str:
    try:
        return str(path.relative_to(KB_DIR))
    except ValueError:
        return str(path)


def is_landing_item(label: str, child: Any) -> bool:
    return isinstance(child, str) and (
        child in LANDING_PAGES or (label.strip().lower() == "overview" and child in LANDING_PAGES)
    )


__all__ = [name for name in globals() if not (name.startswith("__") and name.endswith("__"))]
