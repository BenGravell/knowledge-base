"""tree.yml editing helpers for branch subgroup suggestions."""

import json
import re
from dataclasses import dataclass
from pathlib import Path

import yaml

from knowledge_base.scripts.suggest_branch_subgroupings.common import format_path, is_landing_item, tree_yml_path
from knowledge_base.scripts.suggest_branch_subgroupings.model import Suggestion


@dataclass(frozen=True)
class LineItem:
    label: str | None
    start: int
    end: int
    lines: tuple[str, ...]
    is_landing: bool


def split_list_mapping_line(line: str) -> tuple[int, str | None, str | None] | None:
    stripped = line.lstrip(" ")
    if not stripped.startswith("- "):
        return None

    indent = len(line) - len(stripped)
    body = stripped[2:].rstrip("\n")
    separator_index: int | None = None

    if body.startswith(('"', "'")):
        quote = body[0]
        escaped = False
        index = 1
        while index < len(body):
            char = body[index]
            if quote == '"' and escaped:
                escaped = False
            elif quote == '"' and char == "\\":
                escaped = True
            elif quote == "'" and char == "'" and index + 1 < len(body) and body[index + 1] == "'":
                index += 1
            elif char == quote:
                following = body[index + 1 :].lstrip()
                if following.startswith(":"):
                    separator_index = index + 1 + (len(body[index + 1 :]) - len(following))
                break
            index += 1
    else:
        for index, char in enumerate(body):
            if char == ":" and (index + 1 == len(body) or body[index + 1].isspace()):
                separator_index = index
                break

    if separator_index is not None:
        raw_label = body[:separator_index].strip()
        rest = body[separator_index + 1 :].strip()
        try:
            loaded_label = yaml.safe_load(raw_label)
        except yaml.YAMLError:
            loaded_label = raw_label
        return indent, str(loaded_label), rest

    return indent, None, body.strip()


def line_indent(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def block_end(lines: list[str], start: int, indent: int) -> int:
    for index in range(start + 1, len(lines)):
        if lines[index].strip() and line_indent(lines[index]) <= indent:
            return index
    return len(lines)


def find_branch_line(lines: list[str], path: tuple[str, ...]) -> tuple[int, int, int]:
    search_start = 0
    search_end = len(lines)
    expected_indent = 0

    for label in path:
        found: tuple[int, int] | None = None
        for index in range(search_start, search_end):
            parsed = split_list_mapping_line(lines[index])
            if parsed is None:
                continue
            indent, parsed_label, _ = parsed
            if indent == expected_indent and parsed_label == label:
                found = (index, indent)
                break

        if found is None:
            raise ValueError(f"Could not find branch path in tree.yml: {format_path(path)}")

        line_index, indent = found
        search_start = line_index + 1
        search_end = block_end(lines, line_index, indent)
        expected_indent = indent + 2

    return search_start - 1, search_end, expected_indent - 2


def scalar_leaf_label(source: str) -> str:
    return source.removesuffix(".md").replace("-", " ").replace("_", " ").title()


def collect_direct_line_items(
    lines: list[str],
    *,
    child_start: int,
    child_end: int,
    child_indent: int,
) -> list[LineItem]:
    starts: list[int] = []
    for index in range(child_start, child_end):
        parsed = split_list_mapping_line(lines[index])
        if parsed is not None and parsed[0] == child_indent:
            starts.append(index)

    items: list[LineItem] = []
    for offset, start in enumerate(starts):
        end = starts[offset + 1] if offset + 1 < len(starts) else child_end
        parsed = split_list_mapping_line(lines[start])
        if parsed is None:
            continue
        _, label, scalar = parsed
        display_label = label if label is not None else scalar_leaf_label(scalar or "")
        items.append(
            LineItem(
                label=display_label,
                start=start,
                end=end,
                lines=tuple(lines[start:end]),
                is_landing=is_landing_item(display_label, scalar or ""),
            )
        )
    return items


def yaml_key(label: str) -> str:
    if (
        label
        and label == label.strip()
        and not label.startswith(("-", "?", "@", "`"))
        and not re.search(r"[:#{}\[\],&*!|>%\"']", label)
        and label.lower() not in {"null", "true", "false", "yes", "no", "on", "off"}
    ):
        return label
    return json.dumps(label, ensure_ascii=False)


def apply_tree_suggestion(tree_path: Path, suggestion: Suggestion) -> None:
    text = tree_path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    had_trailing_newline = text.endswith("\n")

    branch_line, branch_end, branch_indent = find_branch_line(
        lines,
        tree_yml_path(suggestion.branch.path),
    )
    child_indent = branch_indent + 2
    line_items = collect_direct_line_items(
        lines,
        child_start=branch_line + 1,
        child_end=branch_end,
        child_indent=child_indent,
    )
    snippets_by_label: dict[str, list[LineItem]] = {}
    for item in line_items:
        if item.label is not None:
            snippets_by_label.setdefault(item.label, []).append(item)

    used_ids: set[int] = set()
    cluster_lines: list[str] = []
    for cluster in suggestion.clusters:
        cluster_lines.append(f"{' ' * child_indent}- {yaml_key(cluster.name)}:\n")
        for child in cluster.children:
            candidates = snippets_by_label.get(child.label, [])
            item = next((candidate for candidate in candidates if id(candidate) not in used_ids), None)
            if item is None:
                raise ValueError(f"Could not find child item in tree.yml: {child.label}")
            used_ids.add(id(item))
            cluster_lines.extend(f"  {line}" for line in item.lines)

    landing_lines: list[str] = []
    skipped_lines: list[str] = []
    for item in line_items:
        if id(item) in used_ids:
            continue
        if item.is_landing:
            landing_lines.extend(item.lines)
        else:
            skipped_lines.extend(item.lines)

    new_lines = lines[: branch_line + 1]
    new_lines.extend(landing_lines)
    new_lines.extend(cluster_lines)
    new_lines.extend(skipped_lines)
    new_lines.extend(lines[branch_end:])

    new_text = "".join(new_lines)
    if had_trailing_newline and not new_text.endswith("\n"):
        new_text += "\n"

    yaml.safe_load(new_text)
    tree_path.write_text(new_text, encoding="utf-8")


__all__ = ["LineItem", "apply_tree_suggestion"]
