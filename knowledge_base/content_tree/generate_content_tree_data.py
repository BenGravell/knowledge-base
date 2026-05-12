"""
MkDocs gen-files script: publish Content Tree nav data as JavaScript.

Runs automatically during ``mkdocs build`` / ``mkdocs serve`` because it is
listed under ``gen-files.scripts`` in mkdocs.yml. The source of truth is the
``Content Tree`` branch in mkdocs.yml; this script converts it into a nested
JSON object that the landing page can render as a focused browser.
"""

from __future__ import annotations

from datetime import date
import json
import re
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import quote

import mkdocs_gen_files
import yaml


MKDOCS_YML = "mkdocs.yml"
METADATA_ROOT = Path("docs/papers")
LANDING_PAGES = {"content-tree.md", "content-tree/index.md"}
UNCATEGORIZED_CATEGORY = "Uncategorized"


def as_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def content_tree(config: dict[str, Any]) -> list[Any]:
    for item in as_list(config.get("nav")):
        if isinstance(item, dict) and "Content Tree" in item:
            return as_list(item["Content Tree"])
    return []


def is_landing_item(label: str, child: Any) -> bool:
    return isinstance(child, str) and (
        child in LANDING_PAGES
        or (str(label).strip().lower() == "overview" and child in LANDING_PAGES)
    )


def slugify_id(text: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return slug or "node"


def slugify_page(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "_", name.lower()).strip("_")


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


def paper_id_from_metadata(metadata_file: Path, data: dict[str, Any]) -> str:
    if "id" in data:
        return slugify_page(str(data["id"]))
    if metadata_file.stem != "metadata":
        return slugify_page(metadata_file.stem)
    return slugify_page(metadata_file.parent.name)


def clean_text(value: Any) -> str:
    text = str(value or "").strip()
    return re.sub(r"[ \t\r\f\v]+", " ", text)


def year_as_int(value: Any) -> int | None:
    if isinstance(value, int):
        year = value
    else:
        match = re.search(r"\b([12][0-9]{3})\b", str(value or ""))
        if not match:
            return None
        year = int(match.group(1))

    if 1500 <= year <= date.today().year + 5:
        return year
    return None


def last_name(author: str) -> str:
    author = clean_text(author)
    if "," in author:
        return author.split(",", 1)[0].strip()
    parts = author.split()
    return parts[-1] if parts else author


def make_paper_label(data: dict[str, Any]) -> str:
    algorithm = clean_text(data.get("algorithm"))
    if algorithm:
        return algorithm

    authors = as_list(data.get("authors"))
    year = year_as_int(data.get("year"))
    if authors:
        et_al = " et al." if len(authors) > 1 else ""
        year_suffix = f" {year}" if year else ""
        return f"{last_name(str(authors[0]))}{et_al}{year_suffix}"

    return clean_text(data.get("title")) or "Untitled"


def collect_paper_details() -> dict[str, dict[str, Any]]:
    details: dict[str, dict[str, Any]] = {}
    for metadata_file in sorted(METADATA_ROOT.rglob("*.yml")):
        with open(metadata_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f) or {}
        if not isinstance(data, dict):
            continue

        paper_id = paper_id_from_metadata(metadata_file, data)
        source = f"papers/{paper_id}.md"
        authors = [clean_text(author) for author in as_list(data.get("authors"))]
        authors = [author for author in authors if author]
        details[source] = {
            "id": paper_id,
            "label": make_paper_label(data),
            "title": clean_text(data.get("title")),
            "authors": authors,
            "year": data.get("year") or "",
            "yearValue": year_as_int(data.get("year")),
            "sourceName": clean_text(data.get("source")),
            "type": clean_text(data.get("type")),
            "tags": [clean_text(tag) for tag in as_list(data.get("tags")) if clean_text(tag)],
            "abstract": clean_text(data.get("abstract")),
            "summary": clean_text(data.get("summary")),
            "mindMapUrl": f"../mind-map/#paper={quote(paper_id, safe='')}",
        }
    return details


paper_details_by_source = collect_paper_details()


def build_leaf(label: str, source: str, path: list[str], ids: IdFactory) -> dict[str, Any]:
    full_path = path + [label]
    node = {
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
    if node["kind"] == "paper":
        node["paper"] = paper_details_by_source.get(source, {})
    return node


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
            if item in LANDING_PAGES:
                continue
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


def build_timeline_nav_index(root_node: dict[str, Any]) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}

    def walk(node: dict[str, Any]) -> None:
        if node.get("kind") == "paper" and node.get("source"):
            path = as_list(node.get("path"))
            super_category = path[1] if len(path) > 1 else None
            category = path[2] if len(path) > 2 else super_category or UNCATEGORIZED_CATEGORY
            sub_category = path[3] if len(path) > 3 else None
            index[str(node["source"])] = {
                "navLabel": node.get("label") or "",
                "superCategory": super_category,
                "category": category,
                "subCategory": sub_category,
                "path": path,
                "url": node.get("url") or page_url(str(node["source"])),
            }

        for child in as_list(node.get("children")):
            if isinstance(child, dict):
                walk(child)

    walk(root_node)
    return index


def build_timeline_order(root_node: dict[str, Any]) -> dict[str, Any]:
    super_categories: list[str] = []
    category_order: list[str] = []
    category_super_category: dict[str, str | None] = {}
    sub_category_order: dict[str, list[str]] = {}

    def add_once(items: list[str], label: str) -> None:
        if label not in items:
            items.append(label)

    for super_node in as_list(root_node.get("children")):
        if not isinstance(super_node, dict) or super_node.get("kind") != "branch":
            continue
        super_label = str(super_node.get("label") or "")
        add_once(super_categories, super_label)

        for category_node in as_list(super_node.get("children")):
            if not isinstance(category_node, dict) or category_node.get("kind") != "branch":
                continue
            category_label = str(category_node.get("label") or "")
            add_once(category_order, category_label)
            category_super_category.setdefault(category_label, super_label)

            for sub_node in as_list(category_node.get("children")):
                if not isinstance(sub_node, dict) or sub_node.get("kind") != "branch":
                    continue
                sub_category_order.setdefault(category_label, [])
                add_once(sub_category_order[category_label], str(sub_node.get("label") or ""))

    return {
        "superCategoryOrder": super_categories,
        "categoryOrder": category_order,
        "categorySuperCategory": category_super_category,
        "subCategoryOrder": sub_category_order,
    }


def build_timeline_data(root_node: dict[str, Any]) -> dict[str, Any]:
    nav_index = build_timeline_nav_index(root_node)
    papers: list[dict[str, Any]] = []

    for source, details in paper_details_by_source.items():
        nav = nav_index.get(
            source,
            {
                "navLabel": "",
                "superCategory": None,
                "category": UNCATEGORIZED_CATEGORY,
                "subCategory": None,
                "path": ["Content Tree", UNCATEGORIZED_CATEGORY],
                "url": page_url(source),
            },
        )
        authors = as_list(details.get("authors"))
        paper_id = str(details.get("id") or source.removeprefix("papers/").removesuffix(".md"))
        label = clean_text(nav.get("navLabel")) or clean_text(details.get("label")) or clean_text(details.get("title"))

        papers.append(
            {
                "id": paper_id,
                "label": label,
                "title": clean_text(details.get("title")),
                "authors": authors,
                "authorShort": ", ".join(last_name(str(author)) for author in authors[:3]),
                "year": details.get("yearValue"),
                "source": clean_text(details.get("sourceName")),
                "type": clean_text(details.get("type")),
                "superCategory": nav.get("superCategory") or UNCATEGORIZED_CATEGORY,
                "category": nav.get("category") or UNCATEGORIZED_CATEGORY,
                "subCategory": nav.get("subCategory"),
                "path": nav.get("path") or ["Content Tree", UNCATEGORIZED_CATEGORY],
                "tags": as_list(details.get("tags")),
                "summary": clean_text(details.get("summary")),
                "url": nav.get("url") or page_url(source),
                "mindMapUrl": details.get("mindMapUrl") or f"../mind-map/#paper={quote(paper_id, safe='')}",
            }
        )

    papers.sort(
        key=lambda paper: (
            paper["year"] is None,
            paper["year"] or 9999,
            paper["superCategory"] or "",
            paper["category"] or "",
            paper["subCategory"] or "",
            paper["label"].lower(),
        )
    )

    years = [paper["year"] for paper in papers if isinstance(paper.get("year"), int)]
    return {
        "papers": papers,
        "meta": {
            **build_timeline_order(root_node),
            "totalPapers": len(papers),
            "plottedPapers": len(years),
            "undatedPapers": len(papers) - len(years),
            "minYear": min(years) if years else None,
            "maxYear": max(years) if years else None,
            "uncategorizedCategory": UNCATEGORIZED_CATEGORY,
        },
    }


TIMELINE_PAGE = r"""---
hide:
  - navigation
  - toc
---

<style>
.md-content__inner:has(#tl-app){max-width:min(1500px,calc(100vw - 2rem))}
.tl-page{--tl-blue:#2367b3;--tl-teal:#13877f;--tl-rose:#bb3974;--tl-gold:#ad6b16;--tl-ink:var(--md-default-fg-color);--tl-muted:var(--md-default-fg-color--light);--tl-border:color-mix(in srgb,var(--md-default-fg-color) 15%,transparent);--tl-soft-border:color-mix(in srgb,var(--md-default-fg-color) 9%,transparent);--tl-panel:color-mix(in srgb,var(--md-code-bg-color) 70%,var(--md-default-bg-color));--tl-panel-strong:color-mix(in srgb,var(--tl-blue) 10%,var(--md-default-bg-color));--tl-shadow:0 12px 28px color-mix(in srgb,#000 13%,transparent);display:flex;flex-direction:column;gap:.85rem;margin-top:1rem}
[data-md-color-scheme="slate"] .tl-page{--tl-blue:#58a6ff;--tl-teal:#25b8ad;--tl-rose:#ff6aa8;--tl-gold:#f0a33e;--tl-panel:color-mix(in srgb,var(--md-code-bg-color) 82%,#050910);--tl-panel-strong:color-mix(in srgb,var(--tl-blue) 16%,var(--md-default-bg-color));--tl-shadow:0 14px 34px color-mix(in srgb,#000 36%,transparent)}
.tl-header{display:flex;align-items:start;justify-content:space-between;gap:1rem}.md-typeset .tl-header h1{margin:0;line-height:1.12}.md-typeset .tl-header p{margin:.28rem 0 0;color:var(--tl-muted);font-size:.82rem}.tl-header-actions{display:flex;flex-wrap:wrap;justify-content:flex-end;gap:.45rem}.tl-header-actions a,.tl-detail-actions a{display:inline-grid;place-items:center;min-height:2.1rem;padding:.36rem .65rem;border:1px solid var(--tl-border);border-radius:8px;background:var(--md-default-bg-color);color:var(--md-typeset-a-color);font-size:.78rem;font-weight:700;text-decoration:none;transition:border-color .16s ease,background .16s ease,transform .16s ease}.tl-header-actions a:hover,.tl-detail-actions a:hover{border-color:var(--tl-blue);background:color-mix(in srgb,var(--tl-blue) 8%,transparent);transform:translateY(-1px)}
.tl-controls{display:grid;grid-template-columns:minmax(16rem,1fr) auto auto auto auto;gap:.65rem;align-items:end;padding:.85rem;border:1px solid var(--tl-border);border-radius:8px;background:linear-gradient(135deg,color-mix(in srgb,var(--tl-teal) 9%,transparent),transparent 42%),linear-gradient(315deg,color-mix(in srgb,var(--tl-gold) 8%,transparent),transparent 44%),var(--tl-panel);box-shadow:0 8px 22px color-mix(in srgb,#000 8%,transparent)}.tl-search,.tl-control-group{display:grid;gap:.25rem}.tl-search label,.tl-control-group>span,.tl-control-group>label,.tl-switch-label{color:var(--tl-muted);font-size:.72rem;font-weight:800;letter-spacing:0;text-transform:uppercase}.tl-search input,.tl-year-control input{box-sizing:border-box;min-height:2.35rem;border:1px solid var(--tl-border);border-radius:8px;background:var(--md-default-bg-color);color:var(--tl-ink);font:inherit}.tl-search input{width:100%;min-width:0;padding:.58rem .72rem}.tl-year-control>div{display:flex;align-items:center;gap:.32rem}.tl-year-control input{width:5.3rem;padding:.42rem .5rem}.tl-search input:focus,.tl-year-control input:focus{border-color:var(--tl-blue);outline:2px solid color-mix(in srgb,var(--tl-blue) 24%,transparent);outline-offset:1px}
.tl-segmented{display:inline-flex;min-height:2.35rem;overflow:hidden;border:1px solid var(--tl-border);border-radius:8px;background:var(--md-default-bg-color)}.tl-segmented button,#tl-reset{min-height:2.35rem;border:0;background:transparent;color:var(--tl-ink);font:inherit;font-weight:700;cursor:pointer}.tl-segmented button{padding:.48rem .64rem;border-right:1px solid var(--tl-soft-border)}.tl-segmented button:last-child{border-right:0}.tl-segmented button[aria-pressed="true"]{background:color-mix(in srgb,var(--tl-blue) 14%,transparent);color:var(--md-typeset-a-color)}#tl-reset{align-self:end;padding:.48rem .85rem;border:1px solid var(--tl-border);border-radius:8px;background:var(--md-default-bg-color)}#tl-reset:hover,.tl-segmented button:hover{background:color-mix(in srgb,var(--tl-blue) 8%,transparent)}
.tl-switch{display:grid;gap:.25rem}.tl-switch-row{display:flex;align-items:center;gap:.55rem;min-height:2.35rem;padding:0 .65rem;border:1px solid var(--tl-border);border-radius:8px;background:var(--md-default-bg-color);cursor:pointer}.tl-switch-row input{position:absolute;opacity:0;pointer-events:none}.tl-switch-track{position:relative;width:2.3rem;height:1.22rem;border-radius:999px;background:color-mix(in srgb,var(--md-default-fg-color) 20%,transparent);transition:background .16s ease}.tl-switch-track::after{content:"";position:absolute;top:.16rem;left:.17rem;width:.9rem;height:.9rem;border-radius:50%;background:var(--md-default-bg-color);box-shadow:0 1px 4px color-mix(in srgb,#000 28%,transparent);transition:transform .16s ease}.tl-switch-row input:checked+.tl-switch-track{background:var(--tl-teal)}.tl-switch-row input:checked+.tl-switch-track::after{transform:translateX(1.04rem)}.tl-switch-text{font-size:.78rem;font-weight:700;color:var(--tl-ink)}
.tl-workbench{display:grid;grid-template-columns:minmax(16rem,21rem) minmax(0,1fr);gap:.85rem;align-items:start}.tl-sidebar,.tl-stage{min-width:0}.tl-sidebar{position:sticky;top:4.2rem;display:grid;gap:.85rem;max-height:calc(100vh - 5.5rem);overflow:auto;scrollbar-width:thin}.tl-sidebar>div,.tl-detail,.tl-stage{border:1px solid var(--tl-border);border-radius:8px;background:var(--tl-panel);box-shadow:var(--tl-shadow)}.tl-sidebar>div,.tl-detail{padding:.78rem}.tl-sidebar h2,.tl-detail h2{margin:0 0 .58rem;font-size:.95rem;line-height:1.25}.tl-legend{display:grid;gap:.35rem}.tl-legend-item{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:.5rem;align-items:center;width:100%;min-height:2.15rem;padding:.35rem .48rem;border:1px solid transparent;border-radius:8px;background:transparent;color:var(--tl-ink);cursor:pointer;font:inherit;text-align:left}.tl-legend-item:hover,.tl-legend-item.is-active{border-color:var(--tl-border);background:var(--tl-panel-strong)}.tl-legend-item span:nth-child(2){min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.tl-legend-item strong{color:var(--tl-muted);font-size:.76rem}.tl-legend-swatch{width:.72rem;height:.72rem;border:1px solid color-mix(in srgb,#000 22%,transparent);border-radius:50%;background:var(--tl-swatch)}
.tl-detail{color:var(--tl-ink)}.tl-detail p{margin:.5rem 0 0;color:var(--tl-muted);font-size:.82rem;line-height:1.5}.tl-detail-kicker{margin-bottom:.25rem;color:var(--tl-gold);font-size:.72rem;font-weight:900}.tl-detail-title{color:var(--tl-ink)!important;font-weight:700}.tl-detail dl{display:grid;gap:.42rem;margin:.7rem 0 0}.tl-detail dl>div{display:grid;grid-template-columns:4.5rem minmax(0,1fr);gap:.45rem}.tl-detail dt{color:var(--tl-muted);font-size:.72rem;font-weight:800}.tl-detail dd{min-width:0;margin:0;overflow-wrap:anywhere;font-size:.78rem}.tl-summary{color:var(--tl-ink)!important}.tl-tags{display:flex;flex-wrap:wrap;gap:.28rem;margin-top:.72rem}.tl-tags span{padding:.16rem .42rem;border:1px solid var(--tl-soft-border);border-radius:999px;background:color-mix(in srgb,var(--tl-teal) 8%,transparent);color:var(--tl-muted);font-size:.68rem}.tl-detail-actions{display:flex;flex-wrap:wrap;gap:.42rem;margin-top:.8rem}
.tl-stage{overflow:hidden}.tl-stage-toolbar{display:flex;align-items:center;justify-content:space-between;gap:.6rem;min-height:2.7rem;padding:.62rem .75rem;border-bottom:1px solid var(--tl-border);color:var(--tl-muted);font-size:.8rem}#tl-selection-chip{max-width:50%;padding:.18rem .46rem;border:1px solid color-mix(in srgb,var(--tl-gold) 48%,transparent);border-radius:999px;background:color-mix(in srgb,var(--tl-gold) 11%,transparent);color:var(--tl-ink);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.tl-svg-wrap{width:100%;max-height:min(78vh,980px);overflow-x:hidden;overflow-y:auto;background:var(--md-default-bg-color);scrollbar-width:thin}#tl-svg{display:block;width:100%;height:auto;min-width:0;max-width:100%!important;font-family:"Atkinson Hyperlegible Next","Segoe UI",sans-serif}.tl-svg-bg{fill:var(--md-default-bg-color)}.tl-grid-minor,.tl-grid-major{stroke:color-mix(in srgb,var(--md-default-fg-color) 11%,transparent);stroke-width:1}.tl-grid-major{stroke:color-mix(in srgb,var(--md-default-fg-color) 19%,transparent)}.tl-axis-line,.tl-lane-line{stroke:color-mix(in srgb,var(--md-default-fg-color) 18%,transparent);stroke-width:1}.tl-lane-line{stroke-dasharray:3 8}.tl-year-label{fill:var(--tl-muted);font-size:11px;font-weight:800;text-anchor:middle}.tl-group-label-bg{fill:color-mix(in srgb,var(--tl-panel) 86%,transparent);stroke:var(--tl-soft-border)}.tl-group-swatch{stroke:color-mix(in srgb,#000 20%,transparent);stroke-width:1.2}.tl-group-label{fill:var(--tl-ink);font-size:12px;font-weight:850}.tl-group-meta{fill:var(--tl-muted);font-size:10px;font-weight:700}.tl-stream{fill-opacity:.22;stroke-opacity:.55;stroke-width:1.2;vector-effect:non-scaling-stroke}.tl-paper-node{cursor:pointer;outline:none}.tl-paper-dot{stroke:var(--md-default-bg-color);stroke-width:1.8;vector-effect:non-scaling-stroke;transition:r .12s ease,stroke-width .12s ease}.tl-paper-node:hover .tl-paper-dot,.tl-paper-node:focus .tl-paper-dot{stroke:var(--tl-gold);stroke-width:3}.tl-paper-node.is-selected .tl-paper-dot{stroke:var(--tl-gold);stroke-width:3.2}.tl-selected-year-line{stroke:var(--tl-gold);stroke-dasharray:6 6;stroke-width:1.4;opacity:.82;pointer-events:none}.tl-selected-label{fill:var(--tl-ink);paint-order:stroke;stroke:var(--md-default-bg-color);stroke-width:4px;font-size:12px;font-weight:900;pointer-events:none}.tl-empty-svg{fill:var(--tl-muted);font-size:14px}.tl-empty,.tl-error{margin:0;color:var(--tl-muted)}
@media (max-width:980px){.tl-controls{grid-template-columns:1fr 1fr}.tl-workbench{grid-template-columns:1fr}.tl-sidebar{position:static;max-height:none;grid-template-columns:1fr}}@media (max-width:680px){.md-content__inner:has(#tl-app){max-width:100%}.tl-header{display:grid}.tl-header-actions{justify-content:start}.tl-controls{grid-template-columns:1fr}.tl-year-control>div{display:grid;grid-template-columns:1fr auto 1fr}.tl-year-control input{width:100%}#tl-selection-chip{max-width:100%}.tl-stage-toolbar{align-items:start;flex-direction:column}.tl-svg-wrap{max-height:72vh}}
</style>

<div id="tl-app" class="tl-page">
  <header class="tl-header">
    <div>
      <h1>Timeline</h1>
      <p id="tl-subtitle"></p>
    </div>
    <div class="tl-header-actions">
      <a href="../mind-map/">Mind Map</a>
      <a href="../content-tree/">Content Tree</a>
    </div>
  </header>

  <section class="tl-controls" aria-label="Timeline controls">
    <form id="tl-search-form" class="tl-search">
      <label for="tl-search">Find a paper</label>
      <input id="tl-search" type="search" autocomplete="off" placeholder="Search papers, authors, tags, or branches">
    </form>
    <div class="tl-control-group" aria-label="Stream grouping">
      <span>Streams</span>
      <div class="tl-segmented" role="group" aria-label="Stream grouping">
        <button type="button" data-tl-mode="super">Super</button>
        <button type="button" data-tl-mode="category" aria-pressed="true">Category</button>
        <button type="button" data-tl-mode="sub">Sub</button>
      </div>
    </div>
    <div class="tl-switch">
      <span class="tl-switch-label">Papers</span>
      <label class="tl-switch-row" for="tl-show-dots">
        <input id="tl-show-dots" type="checkbox" checked>
        <span class="tl-switch-track" aria-hidden="true"></span>
        <span class="tl-switch-text">Dots</span>
      </label>
    </div>
    <div class="tl-control-group tl-year-control" aria-label="Year range">
      <label for="tl-year-start">Years</label>
      <div>
        <input id="tl-year-start" type="number" inputmode="numeric">
        <span>to</span>
        <input id="tl-year-end" type="number" inputmode="numeric">
      </div>
    </div>
    <button id="tl-reset" type="button">Reset</button>
  </section>

  <section class="tl-workbench">
    <aside class="tl-sidebar" aria-label="Timeline legend and selected paper">
      <div>
        <h2>Categories</h2>
        <div id="tl-legend" class="tl-legend"></div>
      </div>
      <article id="tl-detail" class="tl-detail" aria-live="polite">
        <h2>Select a Paper</h2>
        <p>Click a point in the timeline or search for a title to inspect it.</p>
      </article>
    </aside>
    <main class="tl-stage" aria-label="Paper timeline">
      <div class="tl-stage-toolbar">
        <div id="tl-status"></div>
        <div id="tl-selection-chip" hidden></div>
      </div>
      <div id="tl-svg-wrap" class="tl-svg-wrap">
        <svg id="tl-svg" role="img" aria-labelledby="tl-svg-title tl-svg-desc">
          <title id="tl-svg-title">Paper timeline</title>
          <desc id="tl-svg-desc">A year-driven stream timeline of knowledge-base papers grouped by content-tree category.</desc>
        </svg>
      </div>
    </main>
  </section>
</div>

<script src="../javascripts/timeline-data.js"></script>
<script src="../javascripts/timeline.js"></script>
"""


TIMELINE_JS = r"""'use strict';
(function(){
  const app=document.getElementById('tl-app'); if(!app) return;
  const data=window.timelineData;
  if(!data||!Array.isArray(data.papers)||!data.meta){app.innerHTML='<p class="tl-error">Timeline data is unavailable. Run <code>mkdocs build</code> to regenerate it.</p>';return;}
  const UNCATEGORIZED=(data.meta&&data.meta.uncategorizedCategory)||'Uncategorized';
  const UNCATEGORIZED_SET=new Set([UNCATEGORIZED,'Other']);
  const PALETTE=[{h:213,s:76,l:42},{h:152,s:70,l:35},{h:31,s:82,l:43},{h:271,s:62,l:44},{h:334,s:58,l:44},{h:12,s:72,l:42},{h:188,s:72,l:36}];
  const svg=document.getElementById('tl-svg'),svgWrap=document.getElementById('tl-svg-wrap'),subtitle=document.getElementById('tl-subtitle'),status=document.getElementById('tl-status'),legend=document.getElementById('tl-legend'),detail=document.getElementById('tl-detail'),chip=document.getElementById('tl-selection-chip'),form=document.getElementById('tl-search-form'),search=document.getElementById('tl-search'),yearStart=document.getElementById('tl-year-start'),yearEnd=document.getElementById('tl-year-end'),reset=document.getElementById('tl-reset'),dotsToggle=document.getElementById('tl-show-dots'),modeButtons=Array.from(app.querySelectorAll('[data-tl-mode]'));
  const hslCache=new Map(),colorCache=new Map(),subColorCache=new Map();
  const papers=data.papers.map(p=>{const y=Number.isInteger(p.year)?p.year:null;const sup=p.superCategory||UNCATEGORIZED;const cat=p.category||UNCATEGORIZED;const sub=p.subCategory||'';return Object.assign({},p,{year:y,superCategory:sup,category:cat,subCategory:sub,searchText:norm([p.label,p.title,p.authorShort,Array.isArray(p.authors)?p.authors.join(' '):'',y||'',sup,cat,sub,Array.isArray(p.tags)?p.tags.join(' '):'',p.summary||''].join(' '))});});
  const paperById=new Map(papers.map(p=>[p.id,p]));
  const plotted=papers.filter(p=>Number.isInteger(p.year));
  const minYear=data.meta.minYear||Math.min(...plotted.map(p=>p.year)),maxYear=data.meta.maxYear||Math.max(...plotted.map(p=>p.year)),defaultStartYear=Math.min(Math.max(1940,minYear),maxYear);
  const state={mode:'category',activeSuper:null,query:'',selectedId:null,yearStart:defaultStartYear,yearEnd:maxYear,showDots:true};
  const hashId=readPaperHash(); if(hashId&&paperById.has(hashId)) state.selectedId=hashId;
  subtitle.textContent=plural(data.meta.plottedPapers,'dated paper')+' from '+minYear+' to '+maxYear+(data.meta.undatedPapers?' - '+plural(data.meta.undatedPapers,'undated paper')+' kept searchable':'');
  yearStart.value=state.yearStart; yearEnd.value=state.yearEnd; dotsToggle.checked=state.showDots;
  form.addEventListener('submit',e=>{e.preventDefault();const first=filtered()[0];if(first) selectPaper(first.id,true);});
  search.addEventListener('input',()=>{state.query=search.value.trim();render();});
  yearStart.addEventListener('change',syncYears); yearEnd.addEventListener('change',syncYears);
  dotsToggle.addEventListener('change',()=>{state.showDots=dotsToggle.checked;render();});
  reset.addEventListener('click',()=>{state.mode='category';state.activeSuper=null;state.query='';state.selectedId=null;state.yearStart=defaultStartYear;state.yearEnd=maxYear;state.showDots=true;search.value='';yearStart.value=defaultStartYear;yearEnd.value=maxYear;dotsToggle.checked=true;setHash(null);render();});
  modeButtons.forEach(button=>button.addEventListener('click',()=>{state.mode=button.getAttribute('data-tl-mode')||'category';render();}));
  legend.addEventListener('click',e=>{const button=e.target.closest('[data-tl-super]');if(!button)return;const next=button.getAttribute('data-tl-super');state.activeSuper=state.activeSuper===next?null:next;render();});
  svg.addEventListener('click',e=>{const target=e.target.closest('[data-paper-id]');if(target) selectPaper(target.getAttribute('data-paper-id'),true);});
  svg.addEventListener('keydown',e=>{if(e.key!=='Enter'&&e.key!==' ')return;const target=e.target.closest('[data-paper-id]');if(!target)return;e.preventDefault();selectPaper(target.getAttribute('data-paper-id'),true);});
  window.addEventListener('popstate',()=>{const next=readPaperHash();state.selectedId=next&&paperById.has(next)?next:null;render();});
  if(window.ResizeObserver){let pending=false;new ResizeObserver(()=>{if(pending)return;pending=true;requestAnimationFrame(()=>{pending=false;render();});}).observe(svgWrap);}else{window.addEventListener('resize',render);}
  render();
  function syncYears(){const a=clampYear(parseInt(yearStart.value,10)),b=clampYear(parseInt(yearEnd.value,10));state.yearStart=Math.min(a,b);state.yearEnd=Math.max(a,b);yearStart.value=state.yearStart;yearEnd.value=state.yearEnd;render();}
  function clampYear(v){return Number.isFinite(v)?Math.min(Math.max(v,minYear),maxYear):minYear;}
  function selectPaper(id,push){if(!paperById.has(id))return;state.selectedId=id;if(push)setHash(id);render();const node=svg.querySelector('[data-paper-id="'+cssEscape(id)+'"]');if(node&&node.focus)node.focus({preventScroll:true});}
  function render(){const visible=filtered(),groups=buildGroups(visible);renderLegend();renderSvg(groups);renderStatus(visible,groups);renderDetail();modeButtons.forEach(b=>b.setAttribute('aria-pressed',String(b.getAttribute('data-tl-mode')===state.mode)));}
  function filtered(){const terms=norm(state.query).split(/\s+/).filter(Boolean);return plotted.filter(p=>p.year>=state.yearStart&&p.year<=state.yearEnd&&(!state.activeSuper||p.superCategory===state.activeSuper)&&(!terms.length||terms.every(t=>p.searchText.includes(t))));}
  function buildGroups(visible){const map=new Map();visible.forEach(p=>{const d=groupDescriptor(p);if(!map.has(d.key))map.set(d.key,Object.assign({},d,{superCategory:p.superCategory,category:p.category,subCategory:p.subCategory,papers:[]}));map.get(d.key).papers.push(p);});return Array.from(map.values()).sort((a,b)=>compare(a.sort,b.sort)||a.label.localeCompare(b.label));}
  function groupDescriptor(p){const si=positive(superOrder().indexOf(p.superCategory)),ci=positive(categoryOrder().indexOf(p.category)),subs=((data.meta||{}).subCategoryOrder||{})[p.category]||[],subi=positive(p.subCategory?subs.indexOf(p.subCategory):-1);if(state.mode==='super')return{key:'super:'+p.superCategory,label:p.superCategory,pathLabel:p.superCategory,color:isUncat(p.category)?'#000000':superColor(p.superCategory),sort:[si,0,0]};if(state.mode==='sub'){const label=p.subCategory||p.category;return{key:'sub:'+p.category+'::'+(p.subCategory||'(direct)'),label:label,pathLabel:p.subCategory?p.category+' / '+p.subCategory:p.category,color:nodeColor(p.category,p.subCategory),sort:[si,ci,subi]};}return{key:'category:'+p.category,label:p.category,pathLabel:p.superCategory+' / '+p.category,color:nodeColor(p.category,''),sort:[si,ci,0]};}
  function renderSvg(groups){clear(svg);const wrapWidth=svgWrap?svgWrap.clientWidth:0,parentWidth=svg.parentElement?svg.parentElement.clientWidth:0,available=Math.max(320,Math.floor(wrapWidth||parentWidth||960)),compact=available<760,margin={top:44,right:compact?24:48,bottom:52,left:compact?136:188},rowH=state.mode==='sub'?(compact?62:68):state.mode==='super'?(compact?84:92):(compact?70:78),innerW=Math.max(140,available-margin.left-margin.right),width=margin.left+innerW+margin.right,height=Math.max(420,margin.top+groups.length*rowH+margin.bottom),bottom=height-margin.bottom;svg.setAttribute('viewBox','0 0 '+width+' '+height);svg.setAttribute('width','100%');svg.setAttribute('height',height);append(svg,'rect',{x:0,y:0,width:width,height:height,class:'tl-svg-bg'});drawGrid(svg,margin,width,bottom);if(!groups.length){append(svg,'text',{x:margin.left,y:margin.top+70,class:'tl-empty-svg'},'No dated papers match the current filters.');return;}groups.forEach((g,i)=>drawGroup(svg,g,margin.top+i*rowH,margin.top+i*rowH+rowH/2,rowH,margin,innerW));const selected=state.selectedId?paperById.get(state.selectedId):null;if(selected&&Number.isInteger(selected.year)){const x=xForYear(selected.year,margin,innerW);append(svg,'line',{x1:x,x2:x,y1:margin.top-14,y2:bottom,class:'tl-selected-year-line'});}}
  function drawGrid(root,margin,width,bottom){const span=Math.max(1,state.yearEnd-state.yearStart),innerW=width-margin.left-margin.right,step=yearStep(span,innerW),first=Math.ceil(state.yearStart/step)*step,g=append(root,'g',{class:'tl-grid'});for(let y=first;y<=state.yearEnd;y+=step){const x=xForYear(y,margin,innerW),major=y%(step*5)===0||step===1;append(g,'line',{x1:x,x2:x,y1:margin.top-18,y2:bottom,class:major?'tl-grid-major':'tl-grid-minor'});append(g,'text',{x:x,y:margin.top-24,class:'tl-year-label'},String(y));append(g,'text',{x:x,y:bottom+30,class:'tl-year-label'},String(y));}append(g,'line',{x1:margin.left,x2:width-margin.right,y1:margin.top-6,y2:margin.top-6,class:'tl-axis-line'});append(g,'line',{x1:margin.left,x2:width-margin.right,y1:bottom+8,y2:bottom+8,class:'tl-axis-line'});}
  function yearStep(span,innerW){const raw=Math.max(1,Math.ceil(54/(innerW/Math.max(1,span)))),steps=[1,2,5,10,25,50,100];return steps.find(step=>step>=raw)||100;}
  function drawGroup(root,group,top,center,rowH,margin,innerW){const lane=append(root,'g',{class:'tl-group','data-group-key':group.key});append(lane,'line',{x1:margin.left,x2:margin.left+innerW,y1:center,y2:center,class:'tl-lane-line'});append(lane,'rect',{x:0,y:top+4,width:margin.left-18,height:rowH-8,rx:8,class:'tl-group-label-bg'});append(lane,'circle',{cx:18,cy:center,r:5,fill:group.color,class:'tl-group-swatch'});append(lane,'text',{x:32,y:center-3,class:'tl-group-label'},group.label);append(lane,'text',{x:32,y:center+14,class:'tl-group-meta'},plural(group.papers.length,'paper'));append(lane,'path',{d:streamPath(group,center,rowH,margin,innerW),fill:group.color,stroke:group.color,class:'tl-stream'});if(!state.showDots)return;const byYear=new Map();group.papers.forEach(p=>{if(!byYear.has(p.year))byYear.set(p.year,[]);byYear.get(p.year).push(p);});Array.from(byYear.keys()).sort((a,b)=>a-b).forEach(year=>{const items=byYear.get(year).sort((a,b)=>a.label.localeCompare(b.label));items.forEach((p,i)=>{const y=clamp(center+(i-(items.length-1)/2)*9,top+14,top+rowH-14);drawPaper(lane,p,xForYear(year,margin,innerW),y,group.color);});});}
  function streamPath(group,center,rowH,margin,innerW){const span=Math.max(1,state.yearEnd-state.yearStart),sampleStep=Math.max(1,Math.ceil(span/220)),counts=new Map();group.papers.forEach(p=>counts.set(p.year,(counts.get(p.year)||0)+1));const sigma=Math.max(1.2,sampleStep*2.2),samples=[];for(let y=state.yearStart;y<=state.yearEnd;y+=sampleStep){let v=0;counts.forEach((c,cy)=>{const d=(y-cy)/sigma;v+=c*Math.exp(-.5*d*d);});const h=clamp(3+Math.sqrt(v)*8.5,3.2,rowH/2-9);samples.push({x:xForYear(y,margin,innerW),top:center-h,bottom:center+h});}if(samples[samples.length-1].x<margin.left+innerW){const h=clamp(3+Math.sqrt(counts.get(state.yearEnd)||0)*8.5,3.2,rowH/2-9);samples.push({x:margin.left+innerW,top:center-h,bottom:center+h});}return 'M '+samples.map(p=>p.x.toFixed(1)+' '+p.top.toFixed(1)).join(' L ')+' L '+samples.slice().reverse().map(p=>p.x.toFixed(1)+' '+p.bottom.toFixed(1)).join(' L ')+' Z';}
  function drawPaper(root,p,x,y,color){const selected=p.id===state.selectedId,g=append(root,'g',{class:'tl-paper-node'+(selected?' is-selected':''),'data-paper-id':p.id,tabindex:0,role:'button','aria-label':p.label+', '+p.year});append(g,'circle',{cx:x,cy:y,r:selected?6.8:4.4,fill:color,class:'tl-paper-dot'});append(g,'title',{},p.year+' - '+p.label+'\n'+p.title);if(selected)append(g,'text',{x:x+10,y:y-9,class:'tl-selected-label'},p.label);}
  function xForYear(y,margin,innerW){return margin.left+((y-state.yearStart)/Math.max(1,state.yearEnd-state.yearStart))*innerW;}
  function renderLegend(){const bySuper=new Map();plotted.forEach(p=>{if(p.year<state.yearStart||p.year>state.yearEnd)return;if(state.query&&!matchesQuery(p,state.query))return;bySuper.set(p.superCategory,(bySuper.get(p.superCategory)||0)+1);});const supers=superOrder().filter(s=>bySuper.has(s));Array.from(bySuper.keys()).sort().forEach(s=>{if(!supers.includes(s))supers.push(s);});legend.innerHTML=supers.map(s=>{const active=state.activeSuper===s,color=s===UNCATEGORIZED?'#000000':superColor(s);return '<button type="button" class="tl-legend-item'+(active?' is-active':'')+'" data-tl-super="'+escAttr(s)+'"><span class="tl-legend-swatch" style="--tl-swatch:'+escAttr(color)+'"></span><span>'+esc(s)+'</span><strong>'+(bySuper.get(s)||0)+'</strong></button>';}).join('')||'<p class="tl-empty">No categories in range.</p>';}
  function matchesQuery(p,q){const terms=norm(q).split(/\s+/).filter(Boolean);return terms.every(t=>p.searchText.includes(t));}
  function renderStatus(visible,groups){const label=state.mode==='super'?'super-category stream':state.mode==='sub'?'sub-category stream':'category stream';status.textContent=plural(visible.length,'paper')+' across '+plural(groups.length,label)+(state.showDots?'':' - dots hidden');const selected=state.selectedId?paperById.get(state.selectedId):null;if(!selected){chip.hidden=true;chip.textContent='';return;}chip.hidden=false;chip.textContent=(selected.year?selected.year+' - ':'')+selected.label;}
  function renderDetail(){const p=state.selectedId?paperById.get(state.selectedId):null;if(!p){detail.innerHTML='<h2>Select a Paper</h2><p>Click a point in the stream or search for a title to inspect the paper, jump to its generated page, or open it in the Mind Map.</p><p>The current view runs from <strong>'+esc(state.yearStart)+'</strong> to <strong>'+esc(state.yearEnd)+'</strong>.</p>';return;}const tags=Array.isArray(p.tags)&&p.tags.length?'<div class="tl-tags">'+p.tags.slice(0,12).map(t=>'<span>'+esc(t)+'</span>').join('')+'</div>':'';const authors=Array.isArray(p.authors)&&p.authors.length?p.authors.slice(0,8).join(', ')+(p.authors.length>8?', ...':''):'No authors recorded';const path=Array.isArray(p.path)?p.path.filter(Boolean).join(' / '):[p.superCategory,p.category,p.subCategory].filter(Boolean).join(' / ');detail.innerHTML='<div class="tl-detail-kicker">'+esc(p.year||'Undated')+'</div><h2>'+esc(p.label||p.title||'Untitled')+'</h2>'+(p.title&&p.title!==p.label?'<p class="tl-detail-title">'+esc(p.title)+'</p>':'')+'<dl><div><dt>Authors</dt><dd>'+esc(authors)+'</dd></div>'+(p.source?'<div><dt>Source</dt><dd>'+esc(p.source)+'</dd></div>':'')+'<div><dt>Path</dt><dd>'+esc(path)+'</dd></div></dl>'+(p.summary?'<p class="tl-summary">'+esc(p.summary)+'</p>':'')+tags+'<div class="tl-detail-actions"><a href="'+escAttr(p.url)+'">Open paper</a><a href="'+escAttr(p.mindMapUrl)+'">Open in Mind Map</a></div>';}
  function nodeColor(cat,sub){if(isUncat(cat))return'#000000';if(sub){const key=cat+'::'+sub;if(!subColorCache.has(key))subColorCache.set(key,hslToHex(subHsl(cat,sub)));return subColorCache.get(key);}if(!colorCache.has(cat))colorCache.set(cat,hslToHex(categoryHsl(cat)));return colorCache.get(cat);}
  function isUncat(cat){return!cat||UNCATEGORIZED_SET.has(cat);}
  function categoryHsl(cat){if(hslCache.has(cat))return hslCache.get(cat);const sup=categorySuper(cat)||cat,base=superHsl(sup),siblings=categoriesForSuper(sup,cat),i=Math.max(siblings.indexOf(cat),0),center=(siblings.length-1)/2,step=siblings.length>1?Math.min(7,18/(siblings.length-1)):0,hsl={h:normHue(base.h+(i-center)*step),s:clamp(base.s+(i%2===0?2:-2),48,86),l:clamp(base.l+(i-center)*2.2,32,58)};hslCache.set(cat,hsl);return hsl;}
  function subHsl(cat,sub){const base=categoryHsl(cat),ordered=(((data.meta||{}).subCategoryOrder||{})[cat]||[]).filter(Boolean),siblings=ordered.includes(sub)?ordered:ordered.concat(sub).sort((a,b)=>a.localeCompare(b)),i=Math.max(siblings.indexOf(sub),0),center=(siblings.length-1)/2,step=siblings.length>1?Math.min(4,14/(siblings.length-1)):0;return{h:normHue(base.h+(i-center)*step),s:clamp(base.s+(i%2===0?3:-3),45,88),l:clamp(base.l+(i-center)*1.5+(i%2===0?1:-1),32,60)};}
  function categorySuper(cat){const explicit=(((data.meta||{}).categorySuperCategory)||{})[cat];if(explicit)return explicit;const p=papers.find(x=>x.category===cat&&x.superCategory);return p?p.superCategory:null;}
  function categoryOrder(){const configured=((data.meta||{}).categoryOrder||[]),cats=new Set(papers.map(p=>p.category).filter(Boolean)),ordered=configured.filter(c=>cats.has(c));Array.from(cats).sort((a,b)=>a.localeCompare(b)).forEach(c=>{if(!ordered.includes(c))ordered.push(c);});return ordered;}
  function superOrder(){const ordered=Array.from(((data.meta||{}).superCategoryOrder||[]));categoryOrder().forEach(c=>{if(isUncat(c))return;const s=categorySuper(c)||c;if(s&&!ordered.includes(s))ordered.push(s);});papers.forEach(p=>{if(p.superCategory&&!ordered.includes(p.superCategory))ordered.push(p.superCategory);});if(!ordered.includes(UNCATEGORIZED))ordered.push(UNCATEGORIZED);return ordered;}
  function superHsl(s){const order=superOrder(),i=Math.max(order.indexOf(s),0),base=PALETTE[i%PALETTE.length],cycle=Math.floor(i/PALETTE.length);return{h:normHue(base.h+cycle*19),s:base.s,l:base.l};}
  function superColor(s){return hslToHex(superHsl(s));}
  function categoriesForSuper(s,current){const siblings=categoryOrder().filter(c=>(categorySuper(c)||c)===s);if(!siblings.includes(current))siblings.push(current);return siblings;}
  function hslToHex(o){const h=o.h/360,s=o.s/100,l=o.l/100,fn=(p,q,t)=>{if(t<0)t+=1;if(t>1)t-=1;if(t<1/6)return p+(q-p)*6*t;if(t<1/2)return q;if(t<2/3)return p+(q-p)*(2/3-t)*6;return p;};let r,g,b;if(s===0){r=g=b=l;}else{const q=l<.5?l*(1+s):l+s-l*s,p=2*l-q;r=fn(p,q,h+1/3);g=fn(p,q,h);b=fn(p,q,h-1/3);}const hex=v=>Math.round(v*255).toString(16).padStart(2,'0');return'#'+hex(r)+hex(g)+hex(b);}
  function compare(a,b){for(let i=0;i<Math.max(a.length,b.length);i++){const d=(a[i]||0)-(b[i]||0);if(d!==0)return d;}return 0;}function positive(i){return i>=0?i:9999;}function clamp(v,min,max){return Math.min(Math.max(v,min),max);}function normHue(h){return((h%360)+360)%360;}function plural(n,s,p){return n+' '+(n===1?s:(p||s+'s'));}function norm(v){return String(v||'').toLowerCase().normalize('NFKD').replace(/[\u0300-\u036f]/g,'');}
  function readPaperHash(){const hash=window.location.hash.slice(1);if(!hash)return null;const params=new URLSearchParams(hash);return params.get('paper')||params.get('tl');}
  function setHash(id){const url=new URL(window.location.href);url.hash=id?'paper='+encodeURIComponent(id):'';window.history.pushState(null,'',url);}
  function append(parent,tag,attrs,text){const el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.keys(attrs||{}).forEach(k=>el.setAttribute(k,attrs[k]));if(text!==undefined)el.textContent=text;parent.appendChild(el);return el;}
  function clear(node){while(node.firstChild)node.removeChild(node.firstChild);}
  function esc(v){return String(v||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');}
  function escAttr(v){return esc(v).replace(/`/g,'&#96;');}
  function cssEscape(v){return window.CSS&&typeof window.CSS.escape==='function'?window.CSS.escape(v):String(v).replace(/"/g,'\\"');}
})();"""


timeline_data = build_timeline_data(root)

with mkdocs_gen_files.open("timeline.md", "w") as out:
    out.write(TIMELINE_PAGE)

with mkdocs_gen_files.open("javascripts/timeline-data.js", "w") as out:
    out.write("window.timelineData = ")
    out.write(json.dumps(timeline_data, indent=2, ensure_ascii=False))
    out.write(";\n")

with mkdocs_gen_files.open("javascripts/timeline.js", "w") as out:
    out.write(TIMELINE_JS)
    out.write("\n")
