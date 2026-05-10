"""
MkDocs gen-files script: publish Content Tree nav data as JavaScript.

Runs automatically during ``mkdocs build`` / ``mkdocs serve`` because it is
listed under ``gen-files.scripts`` in mkdocs.yml. The source of truth is the
``Content Tree`` branch in mkdocs.yml; this script converts it into a nested
JSON object that the landing page can render as a focused browser.
"""

from __future__ import annotations

import json
import re
from pathlib import PurePosixPath
from typing import Any

import mkdocs_gen_files
import yaml


MKDOCS_YML = "mkdocs.yml"
LANDING_PAGE = "content-tree.md"


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def content_tree(config: dict[str, Any]) -> list[Any]:
    for item in as_list(config.get("nav")):
        if isinstance(item, dict) and "Content Tree" in item:
            return as_list(item["Content Tree"])
    return []


def is_landing_item(label: str, child: Any) -> bool:
    return str(label).strip().lower() == "overview" and child == LANDING_PAGE


def slugify_id(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return slug or "node"


class IdFactory:
    def __init__(self) -> None:
        self.seen: dict[str, int] = {}

    def make(self, path: list[str], source: str | None = None) -> str:
        base = slugify_id("|".join(path + ([source] if source else [])))
        count = self.seen.get(base, 0)
        self.seen[base] = count + 1
        return base if count == 0 else f"{base}-{count + 1}"


def page_url(source: str) -> str:
    if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*://", source):
        return source
    if not source.endswith(".md"):
        return source

    path = PurePosixPath(source.removesuffix(".md"))
    if path.name == "index":
        path = path.parent

    target = str(path).strip("/")
    return "../" if not target else f"../{target}/"


def link_kind(source: str) -> str:
    if source.startswith("papers/") and source.endswith(".md"):
        return "paper"
    if source.endswith(".md"):
        return "page"
    return "link"


def build_leaf(label: str, source: str, path: list[str], ids: IdFactory) -> dict[str, Any]:
    full_path = path + [label]
    return {
        "id": ids.make(full_path, source),
        "label": label,
        "kind": link_kind(source),
        "source": source,
        "url": page_url(source),
        "path": full_path,
        "children": [],
        "leafCount": 1,
        "branchCount": 0,
    }


def build_branch(label: str, child: list[Any], path: list[str], ids: IdFactory) -> dict[str, Any]:
    full_path = path + [label]
    children = build_children(child, full_path, ids)
    leaf_count = sum(node["leafCount"] for node in children)
    branch_count = len([node for node in children if node["kind"] == "branch"])
    branch_count += sum(node["branchCount"] for node in children)
    return {
        "id": ids.make(full_path),
        "label": label,
        "kind": "branch",
        "source": None,
        "url": None,
        "path": full_path,
        "children": children,
        "leafCount": leaf_count,
        "branchCount": branch_count,
    }


def build_children(items: list[Any], path: list[str], ids: IdFactory) -> list[dict[str, Any]]:
    nodes: list[dict[str, Any]] = []
    for item in items:
        if isinstance(item, str):
            label = item.removesuffix(".md").replace("-", " ").replace("_", " ").title()
            nodes.append(build_leaf(label, item, path, ids))
            continue

        if not isinstance(item, dict):
            continue

        for label_raw, child in item.items():
            label = str(label_raw)
            if is_landing_item(label, child):
                continue
            if isinstance(child, str):
                nodes.append(build_leaf(label, child, path, ids))
            elif isinstance(child, list):
                nodes.append(build_branch(label, child, path, ids))

    return nodes


with open(MKDOCS_YML, "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

ids = IdFactory()
root_children = build_children(content_tree(config), ["Content Tree"], ids)
root = {
    "id": "content-tree",
    "label": "Content Tree",
    "kind": "branch",
    "source": None,
    "url": None,
    "path": ["Content Tree"],
    "children": root_children,
    "leafCount": sum(node["leafCount"] for node in root_children),
    "branchCount": len([node for node in root_children if node["kind"] == "branch"])
    + sum(node["branchCount"] for node in root_children),
}

data = {
    "root": root,
    "meta": {
        "totalLeaves": root["leafCount"],
        "totalBranches": root["branchCount"],
    },
}

with mkdocs_gen_files.open("javascripts/content-tree-data.js", "w") as out:
    out.write("window.contentTreeData = ")
    out.write(json.dumps(data, indent=2, ensure_ascii=False))
    out.write(";\n")
