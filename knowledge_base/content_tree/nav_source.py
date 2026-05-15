"""Helpers for loading the standalone Content Tree navigation source."""

from __future__ import annotations

from pathlib import Path
from typing import Any
import re

import yaml


KB_DIR = Path(__file__).resolve().parents[1]
METADATA_ROOT = KB_DIR / "docs" / "papers"
CONTENT_TREE_YML = KB_DIR / "content_tree.yml"


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def slugify(name: str) -> str:
    """Match the generated paper page naming logic in ``generate_papers.py``."""
    return re.sub(r"[^a-zA-Z0-9]+", "_", str(name).lower()).strip("_")


def paper_id_from_metadata_file(metadata_file: Path) -> str:
    with metadata_file.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}
    if not isinstance(data, dict):
        data = {}

    if "id" in data:
        return slugify(data["id"])
    if metadata_file.stem != "metadata":
        return slugify(metadata_file.stem)
    return slugify(metadata_file.parent.name)


def metadata_source_path(source: str, base_dir: Path = KB_DIR) -> Path | None:
    source_path = source.replace("\\", "/").strip()
    if source_path.startswith("doc/papers/"):
        source_path = f"docs/{source_path.removeprefix('doc/')}"

    if not (
        source_path.startswith("docs/papers/")
        or source_path.startswith("./docs/papers/")
        or source_path.startswith("../knowledge_base/docs/papers/")
    ):
        return None

    path = (base_dir / source_path).resolve() if not Path(source_path).is_absolute() else Path(source_path)
    if not source_path.endswith((".yml", ".yaml")):
        path = path / "metadata.yml"
    return path


def normalize_source(source: str, base_dir: Path = KB_DIR) -> str:
    metadata_file = metadata_source_path(source, base_dir)
    if metadata_file is None:
        return source
    if not metadata_file.exists():
        raise FileNotFoundError(f"Content Tree source does not exist: {source}")
    return f"papers/{paper_id_from_metadata_file(metadata_file)}.md"


def normalize_nav_sources(node: Any, base_dir: Path = KB_DIR) -> Any:
    if isinstance(node, str):
        return normalize_source(node, base_dir)
    if isinstance(node, list):
        return [normalize_nav_sources(item, base_dir) for item in node]
    if isinstance(node, dict):
        return {
            label: normalize_nav_sources(child, base_dir)
            for label, child in node.items()
        }
    return node


def content_tree_from_config(config: dict[str, Any]) -> Any:
    for item in as_list(config.get("nav")):
        if isinstance(item, dict) and "Content Tree" in item:
            return item["Content Tree"]
    return []


def content_tree_nav_item_from_file(
    path: Path = CONTENT_TREE_YML,
    *,
    normalize: bool = True,
) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f) or {}

    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and "Content Tree" in item:
                tree = item["Content Tree"]
                if normalize:
                    tree = normalize_nav_sources(tree, path.parent)
                return {"Content Tree": tree}

    if not isinstance(data, dict) or "Content Tree" not in data:
        raise ValueError(f"{path} must contain a top-level 'Content Tree' nav item")
    tree = data["Content Tree"]
    if normalize:
        tree = normalize_nav_sources(tree, path.parent)
    return {"Content Tree": tree}


def content_tree_from_file(path: Path = CONTENT_TREE_YML, *, normalize: bool = True) -> Any:
    return content_tree_nav_item_from_file(path, normalize=normalize)["Content Tree"]


def load_content_tree(config: dict[str, Any] | None = None) -> Any:
    if CONTENT_TREE_YML.exists():
        return content_tree_from_file(CONTENT_TREE_YML)
    if config is None:
        return []
    return content_tree_from_config(config)
