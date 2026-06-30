"""YAML read/write helpers for algorithm label suggestions."""

import re
from pathlib import Path
from typing import Any

import yaml

from knowledge_base.components.tree.nav_source import YAML_LOADER
from knowledge_base.components.tree.validation import TREE_YML
from knowledge_base.scripts.suggest_tree_algorithm_labels.label_text import clean_text
from knowledge_base.scripts.suggest_tree_algorithm_labels.model import Suggestion


def load_metadata(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.load(f, Loader=YAML_LOADER) or {}
    return data if isinstance(data, dict) else {}


def yaml_inline_value(value: str) -> str:
    dumped = yaml.safe_dump(
        {"value": value},
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=10_000,
    ).strip()
    prefix = "value: "
    if dumped.startswith(prefix):
        return dumped.removeprefix(prefix)
    raise ValueError(f"Could not render YAML scalar for {value!r}")


def yaml_key(value: str) -> str:
    placeholder = "__KB_TREE_LABEL_VALUE__"
    dumped = yaml.safe_dump(
        [{value: placeholder}],
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=10_000,
    ).strip()
    match = re.fullmatch(r"- (.*): " + re.escape(placeholder), dumped)
    if not match:
        raise ValueError(f"Could not render YAML key for {value!r}")
    return match.group(1)


def replace_metadata_algorithm(metadata_path: Path, algorithm: str) -> bool:
    lines = metadata_path.read_text(encoding="utf-8").splitlines(keepends=True)
    algorithm = clean_text(algorithm)
    replacement = "algorithm:\n" if not algorithm else f"algorithm: {yaml_inline_value(algorithm)}\n"
    for index, line in enumerate(lines):
        if re.match(r"^algorithm\s*:", line):
            if line == replacement:
                return False
            lines[index] = replacement
            metadata_path.write_text("".join(lines), encoding="utf-8")
            return True

    for index, line in enumerate(lines):
        if re.match(r"^title\s*:", line):
            lines.insert(index + 1, replacement)
            metadata_path.write_text("".join(lines), encoding="utf-8")
            return True

    lines.insert(0, replacement)
    metadata_path.write_text("".join(lines), encoding="utf-8")
    return True


def replace_tree_label(tree_path: Path, source: str, new_label: str) -> bool:
    lines = tree_path.read_text(encoding="utf-8").splitlines(keepends=True)
    source_pattern = re.escape(source)
    leaf_pattern = re.compile(rf"^(?P<indent>\s*)-\s+(?P<label>.+):\s+{source_pattern}\s*(?P<comment>#.*)?$")
    for index, line in enumerate(lines):
        body = line.rstrip("\n")
        match = leaf_pattern.match(body)
        if not match:
            continue

        rendered_key = yaml_key(new_label)
        comment = f" {match.group('comment')}" if match.group("comment") else ""
        replacement = f"{match.group('indent')}- {rendered_key}: {source}{comment}\n"
        if line == replacement:
            return False
        lines[index] = replacement
        tree_path.write_text("".join(lines), encoding="utf-8")
        return True

    raise ValueError(f"Could not find Tree leaf source {source!r} in {tree_path}")


def apply_canonical_label(
    suggestion: Suggestion,
    canonical_label: str,
    *,
    tree_path: Path = TREE_YML,
) -> list[Path]:
    label = clean_text(canonical_label)
    if not label:
        raise ValueError("Canonical label cannot be empty.")

    changed: list[Path] = []
    if replace_tree_label(tree_path, suggestion.source, label):
        changed.append(tree_path)
    if replace_metadata_algorithm(suggestion.metadata_path, label):
        changed.append(suggestion.metadata_path)
    return changed


__all__ = [
    "apply_canonical_label",
    "load_metadata",
    "replace_metadata_algorithm",
    "replace_tree_label",
    "yaml_inline_value",
    "yaml_key",
]
