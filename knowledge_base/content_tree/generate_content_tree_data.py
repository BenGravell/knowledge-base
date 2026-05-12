"""
MkDocs gen-files script: publish Content Tree nav data as JavaScript.

Runs automatically during ``mkdocs build`` / ``mkdocs serve`` because it is
listed under ``gen-files.scripts`` in mkdocs.yml. The source of truth is the
``Content Tree`` branch in mkdocs.yml; this script converts it into a nested
JSON object that the landing page can render as a focused browser.
"""

from __future__ import annotations

from collections import Counter
from datetime import date
import math
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
            "algorithm": clean_text(data.get("algorithm")),
            "authors": authors,
            "year": data.get("year") or "",
            "yearValue": year_as_int(data.get("year")),
            "sourceName": clean_text(data.get("source")),
            "type": clean_text(data.get("type")),
            "doi": clean_text(data.get("doi")),
            "arxivId": clean_text(data.get("arxiv_id")),
            "hasPrimaryLink": bool(clean_text(data.get("link"))),
            "alternateLinkCount": len(as_list(data.get("links_alt"))),
            "auditStatus": clean_text(data.get("audit_status")),
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
    year_counts: Counter[int] = Counter()

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
        year = details.get("yearValue")
        if isinstance(year, int):
            year_counts[year] += 1

        papers.append(
            {
                "id": paper_id,
                "label": label,
                "title": clean_text(details.get("title")),
                "authors": authors,
                "authorShort": ", ".join(last_name(str(author)) for author in authors[:3]),
                "year": year,
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

    years = sorted(year_counts)
    return {
        "papers": papers,
        "meta": {
            **build_timeline_order(root_node),
            "totalPapers": len(papers),
            "plottedPapers": sum(year_counts.values()),
            "undatedPapers": len(papers) - sum(year_counts.values()),
            "minYear": min(years) if years else None,
            "maxYear": max(years) if years else None,
            "yearBins": build_year_bins(year_counts),
            "uncategorizedCategory": UNCATEGORIZED_CATEGORY,
        },
    }


def count_rows(counter: Counter, *, limit: int | None = None) -> list[dict[str, Any]]:
    rows = [
        {"label": str(label), "count": int(count)}
        for label, count in sorted(counter.items(), key=lambda item: (-item[1], str(item[0]).casefold()))
        if str(label)
    ]
    return rows[:limit] if limit else rows


def year_bin_label(start: int, end: int) -> str:
    return str(start) if start == end else f"{start}-{end}"


def year_bin_width(start: int) -> int:
    if start < 1950:
        return 10
    if start < 2000:
        return 5
    return 1


def analytics_year_bin_label(start: int, end: int) -> str:
    if end < 1940:
        return "Pre-1940"
    return year_bin_label(start, end)


def analytics_year_bin_width(start: int) -> int:
    if start < 1941:
        return 10
    return 5


def build_year_bins(year_counts: Counter[int]) -> list[dict[str, Any]]:
    years = sorted(year_counts)
    if not years:
        return []

    min_year = min(years)
    max_year = max(years)
    ranges: list[tuple[int, int]] = []

    if min_year < 1950:
        ranges.append((min_year, min(1949, max_year)))
    for start in range(1950, min(2000, max_year + 1), 5):
        ranges.append((max(start, min_year), min(start + 4, max_year)))
    for year in range(max(2000, min_year), max_year + 1):
        ranges.append((year, year))

    return [
        {
            "label": year_bin_label(start, end),
            "start": start,
            "end": end,
            "width": year_bin_width(start)
            + (max(0, int(sum(year_counts.get(year, 0) for year in range(start, end + 1))) - 1) ** 0.62) * 0.7,
            "count": int(sum(year_counts.get(year, 0) for year in range(start, end + 1))),
        }
        for start, end in ranges
        if start <= end
    ]


def build_analytics_year_bins(year_counts: Counter[int]) -> list[dict[str, Any]]:
    years = sorted(year_counts)
    if not years:
        return []

    ranges: list[tuple[int, int]] = []

    if any(year < 1940 for year in years):
        ranges.append((min(year for year in years if year < 1940), 1939))

    if 1940 in year_counts:
        ranges.append((1940, 1940))

    post_1940_years = [year for year in years if year > 1940]
    if post_1940_years:
        first_start = 1940 + 5 * ((min(post_1940_years) - 1940) // 5)
        last_end = 1940 + 5 * math.ceil((max(post_1940_years) - 1940) / 5)
        for start in range(first_start, last_end, 5):
            ranges.append((start + 1, start + 5))

    return [
        {
            "label": analytics_year_bin_label(start, end),
            "start": start,
            "end": end,
            "width": analytics_year_bin_width(start),
            "count": int(sum(year_counts.get(year, 0) for year in range(start, end + 1))),
        }
        for start, end in ranges
        if start <= end
    ]


def normalize_author(author: str) -> str:
    return re.sub(r"\s+", " ", clean_text(author)).casefold()


def build_analytics_data(root_node: dict[str, Any]) -> dict[str, Any]:
    nav_index = build_timeline_nav_index(root_node)
    year_counts: Counter[int] = Counter()
    author_counts: Counter[str] = Counter()
    author_display: dict[str, str] = {}
    source_counts: Counter[str] = Counter()
    type_counts: Counter[str] = Counter()
    tag_counts: Counter[str] = Counter()
    super_counts: Counter[str] = Counter()
    category_counts: Counter[str] = Counter()
    audit_counts: Counter[str] = Counter()

    arxiv_count = 0
    doi_count = 0
    total_papers = 0

    for source, details in paper_details_by_source.items():
        total_papers += 1
        nav = nav_index.get(source)
        nav = nav or {
            "navLabel": "",
            "superCategory": None,
            "category": UNCATEGORIZED_CATEGORY,
            "subCategory": None,
            "path": ["Content Tree", UNCATEGORIZED_CATEGORY],
            "url": page_url(source),
        }
        authors = [clean_text(author) for author in as_list(details.get("authors")) if clean_text(author)]
        year = details.get("yearValue")
        source_name = clean_text(details.get("sourceName")) or "Unspecified"
        type_name = clean_text(details.get("type")) or "Unspecified"
        super_category = nav.get("superCategory") or UNCATEGORIZED_CATEGORY
        category = nav.get("category") or UNCATEGORIZED_CATEGORY
        tags = [clean_text(tag) for tag in as_list(details.get("tags")) if clean_text(tag)]
        audit_status = clean_text(details.get("auditStatus")) or "Unspecified"
        arxiv_id = clean_text(details.get("arxivId"))
        doi = clean_text(details.get("doi"))
        if isinstance(year, int):
            year_counts[year] += 1
        for author in authors:
            key = normalize_author(author)
            if not key:
                continue
            author_counts[key] += 1
            author_display.setdefault(key, author)
        source_counts[source_name] += 1
        type_counts[type_name] += 1
        super_counts[str(super_category)] += 1
        category_counts[str(category)] += 1
        audit_counts[audit_status] += 1
        tag_counts.update(tags)

        arxiv_count += bool(arxiv_id)
        doi_count += bool(doi)

    years = sorted(year_counts)
    year_rows = build_analytics_year_bins(year_counts)
    author_rows = [
        {"label": author_display[key], "count": int(count)}
        for key, count in sorted(author_counts.items(), key=lambda item: (-item[1], author_display[item[0]].casefold()))
    ]
    return {
        "metrics": {
            "totalPapers": total_papers,
            "datedPapers": sum(year_counts.values()),
            "undatedPapers": total_papers - sum(year_counts.values()),
            "uniqueAuthors": len(author_counts),
            "uniqueSources": len([label for label in source_counts if label != "Unspecified"]),
            "uniqueTags": len(tag_counts),
            "minYear": min(years) if years else None,
            "maxYear": max(years) if years else None,
            "arxivPapers": arxiv_count,
            "doiPapers": doi_count,
        },
        "years": year_rows,
        "authors": author_rows,
        "sources": count_rows(source_counts),
        "types": count_rows(type_counts),
        "tags": count_rows(tag_counts),
        "superCategories": count_rows(super_counts),
        "categories": count_rows(category_counts),
        "auditStatuses": count_rows(audit_counts),
    }


ANALYTICS_PAGE = r"""---
hide:
  - toc
---

<style>
.md-content__inner:has(#an-app){max-width:min(1420px,calc(100vw - 2rem))}
.an-page{--an-blue:#2367b3;--an-teal:#13877f;--an-rose:#bb3974;--an-gold:#ad6b16;--an-ink:var(--md-default-fg-color);--an-muted:var(--md-default-fg-color--light);--an-border:color-mix(in srgb,var(--md-default-fg-color) 15%,transparent);--an-soft-border:color-mix(in srgb,var(--md-default-fg-color) 9%,transparent);--an-panel:color-mix(in srgb,var(--md-code-bg-color) 70%,var(--md-default-bg-color));--an-panel-strong:color-mix(in srgb,var(--an-blue) 10%,var(--md-default-bg-color));--an-shadow:0 12px 28px color-mix(in srgb,#000 12%,transparent);display:flex;flex-direction:column;gap:.9rem;margin-top:1rem}
[data-md-color-scheme="slate"] .an-page{--an-blue:#58a6ff;--an-teal:#25b8ad;--an-rose:#ff6aa8;--an-gold:#f0a33e;--an-panel:color-mix(in srgb,var(--md-code-bg-color) 82%,#050910);--an-panel-strong:color-mix(in srgb,var(--an-blue) 16%,var(--md-default-bg-color));--an-shadow:0 14px 34px color-mix(in srgb,#000 34%,transparent)}
.an-header{display:flex;align-items:start;justify-content:space-between;gap:1rem}.md-typeset .an-header h1{margin:0;line-height:1.12}.md-typeset .an-header p{margin:.28rem 0 0;color:var(--an-muted);font-size:.82rem}
.an-metrics{display:grid;grid-template-columns:repeat(auto-fit,minmax(7rem,1fr));gap:.62rem}.an-metric{min-width:0;padding:.74rem .8rem;border:1px solid var(--an-border);border-radius:8px;background:linear-gradient(135deg,color-mix(in srgb,var(--an-teal) 8%,transparent),transparent 46%),var(--an-panel);box-shadow:0 8px 18px color-mix(in srgb,#000 7%,transparent)}.an-metric strong{display:block;color:var(--an-ink);font-size:1.35rem;line-height:1.1}.an-metric span{display:block;margin-top:.22rem;color:var(--an-muted);font-size:.72rem;font-weight:850;letter-spacing:0;text-transform:uppercase}.an-toolbar{display:flex;flex-wrap:wrap;align-items:end;gap:.65rem;padding:.78rem;border:1px solid var(--an-border);border-radius:8px;background:var(--an-panel)}.an-field{display:grid;gap:.25rem}.an-field:first-child{flex:1 1 18rem}.an-field label{color:var(--an-muted);font-size:.72rem;font-weight:850;text-transform:uppercase}.an-field input,.an-field select{box-sizing:border-box;min-height:2.35rem;border:1px solid var(--an-border);border-radius:8px;background:var(--md-default-bg-color);color:var(--an-ink);font:inherit}.an-field input{width:100%;padding:.58rem .72rem}.an-field select{padding:.42rem .56rem}.an-field input:focus,.an-field select:focus{border-color:var(--an-blue);outline:2px solid color-mix(in srgb,var(--an-blue) 24%,transparent);outline-offset:1px}
.an-grid{display:grid;grid-template-columns:1fr;gap:.85rem}.an-card{min-width:0;padding:.82rem;border:1px solid var(--an-border);border-radius:8px;background:var(--an-panel);box-shadow:var(--an-shadow)}.an-card--wide{grid-column:1 / -1}.an-card-head{display:flex;align-items:center;justify-content:space-between;gap:.65rem;margin:0 0 .68rem}.an-card h2{margin:0 0 .68rem;font-size:1rem;line-height:1.2}.an-card-head h2{margin:0}.an-card-limit{display:flex;align-items:center;gap:.35rem;color:var(--an-muted);font-size:.68rem;font-weight:850;text-transform:uppercase;white-space:nowrap}.an-card-limit select{box-sizing:border-box;min-height:1.9rem;border:1px solid var(--an-border);border-radius:8px;background:var(--md-default-bg-color);color:var(--an-ink);font:inherit;padding:.22rem .4rem;text-transform:none}.an-card-limit select:focus{border-color:var(--an-blue);outline:2px solid color-mix(in srgb,var(--an-blue) 24%,transparent);outline-offset:1px}.an-card-kicker{margin:-.35rem 0 .68rem;color:var(--an-muted);font-size:.74rem}.an-bars{display:grid;gap:.36rem}.an-bar{display:grid;grid-template-columns:minmax(7.5rem,1fr) minmax(6rem,2.2fr) auto;gap:.52rem;align-items:center;min-height:1.75rem}.an-bar-label{min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:.78rem;font-weight:750}.an-bar-track{height:.64rem;overflow:hidden;border-radius:999px;background:color-mix(in srgb,var(--md-default-fg-color) 8%,transparent)}.an-bar-fill{display:block;width:var(--an-w);height:100%;border-radius:inherit;background:linear-gradient(90deg,var(--an-teal),var(--an-blue))}.an-bar-count{color:var(--an-muted);font-size:.74rem;font-weight:800;text-align:right}.an-more{margin:.16rem 0 0;padding:.48rem .58rem;border:1px dashed var(--an-border);border-radius:8px;background:color-mix(in srgb,var(--an-blue) 6%,transparent);color:var(--an-muted);font-size:.73rem;font-weight:800;text-align:center}.an-year-hist{position:relative;display:flex;align-items:end;gap:0;box-sizing:border-box;width:100%;min-height:13rem;overflow:hidden;padding:.45rem .2rem .3rem;border-bottom:1px solid var(--an-border)}.an-year{position:relative;z-index:1;display:grid;align-items:end;flex:var(--an-bin-w) 1 0;min-width:0;height:12rem;outline:none}.an-year i{display:block;height:var(--an-h);min-height:2px;margin:0 1px;border-radius:999px 999px 0 0;background:linear-gradient(180deg,var(--an-rose),var(--an-gold));transition:filter .14s ease,opacity .14s ease,box-shadow .14s ease}.an-year:hover i,.an-year:focus-visible i{box-shadow:0 0 0 2px var(--md-default-bg-color),0 0 0 4px color-mix(in srgb,var(--an-gold) 62%,transparent),0 0 18px color-mix(in srgb,var(--an-rose) 42%,transparent);filter:saturate(1.28) brightness(1.08);opacity:1}.an-year:focus-visible{outline:2px solid color-mix(in srgb,var(--an-blue) 55%,transparent);outline-offset:2px}.an-year-axis{position:relative;height:1.35rem;color:var(--an-muted);font-size:.72rem;font-weight:800}.an-year-axis-tick{position:absolute;top:0;left:var(--an-x);transform:translateX(-50%);white-space:nowrap}.an-year-axis-tick[data-edge="start"]{transform:translateX(0)}.an-year-axis-tick[data-edge="end"]{transform:translateX(-100%)}.an-year-axis-tick::before{content:"";display:block;width:1px;height:.36rem;margin:0 auto .08rem;background:var(--an-border)}.an-year-tooltip{position:fixed;z-index:30;max-width:min(14rem,calc(100vw - 1rem));padding:.36rem .5rem;border:1px solid var(--an-border);border-radius:6px;background:var(--md-default-bg-color);box-shadow:0 10px 24px color-mix(in srgb,#000 18%,transparent);color:var(--an-ink);font-size:.74rem;font-weight:800;line-height:1.25;pointer-events:none;transform:translate(-50%,calc(-100% - .55rem));opacity:0;transition:opacity .12s ease}.an-year-tooltip.is-visible{opacity:1}.an-year-tooltip span{display:block;color:var(--an-muted);font-size:.66rem;font-weight:750}.an-table-wrap{max-height:34rem;overflow:auto;border:1px solid var(--an-border);border-radius:8px;background:var(--md-default-bg-color);scrollbar-width:thin}.an-table{width:100%;border-collapse:collapse;font-size:.76rem}.an-table th{position:sticky;top:0;z-index:1;background:var(--an-panel);color:var(--an-muted);font-size:.68rem;text-align:left;text-transform:uppercase}.an-table th,.an-table td{padding:.48rem .55rem;border-bottom:1px solid var(--an-soft-border);vertical-align:top}.an-paper-cell{display:grid;gap:.12rem;min-width:14rem}.an-paper-cell a{font-weight:850}.an-paper-cell span{color:var(--an-muted);font-size:.71rem}.an-empty,.an-error{margin:0;color:var(--an-muted)}
@media (max-width:900px){.an-grid{grid-template-columns:1fr}.an-header{display:grid}.an-bar{grid-template-columns:minmax(0,1fr) minmax(5rem,1.2fr) auto}}@media (max-width:620px){.md-content__inner:has(#an-app){max-width:100%}.an-bar{grid-template-columns:1fr auto}.an-bar-track{grid-column:1 / -1}.an-table th:nth-child(3),.an-table td:nth-child(3){display:none}}
</style>

<div id="an-app" class="an-page">
  <header class="an-header">
    <div>
      <h1>Analytics</h1>
      <p id="an-subtitle"></p>
    </div>
  </header>

  <section id="an-metrics" class="an-metrics" aria-label="Analytics metrics"></section>

  <section class="an-grid" aria-label="Aggregate charts">
    <article class="an-card an-card--wide">
      <h2>Papers by Year</h2>
      <div id="an-years" class="an-year-hist" role="img" aria-label="Histogram of papers by publication year"></div>
      <div id="an-year-axis" class="an-year-axis"></div>
      <div id="an-year-tooltip" class="an-year-tooltip" role="tooltip" hidden></div>
    </article>
    <article class="an-card">
      <div class="an-card-head">
        <h2>Authors</h2>
        <label class="an-card-limit" for="an-authors-limit">Rows
          <select id="an-authors-limit" data-limit-for="an-authors">
            <option value="5" selected>Top 5</option>
            <option value="10">Top 10</option>
            <option value="20">Top 20</option>
            <option value="50">Top 50</option>
            <option value="all">All</option>
          </select>
        </label>
      </div>
      <p class="an-card-kicker" id="an-author-kicker"></p>
      <div id="an-authors" class="an-bars"></div>
    </article>
    <article class="an-card">
      <div class="an-card-head">
        <h2>Sources</h2>
        <label class="an-card-limit" for="an-sources-limit">Rows
          <select id="an-sources-limit" data-limit-for="an-sources">
            <option value="5" selected>Top 5</option>
            <option value="10">Top 10</option>
            <option value="20">Top 20</option>
            <option value="50">Top 50</option>
            <option value="all">All</option>
          </select>
        </label>
      </div>
      <div id="an-sources" class="an-bars"></div>
    </article>
    <article class="an-card">
      <div class="an-card-head">
        <h2>Content Tree</h2>
        <label class="an-card-limit" for="an-super-categories-limit">Rows
          <select id="an-super-categories-limit" data-limit-for="an-super-categories">
            <option value="5" selected>Top 5</option>
            <option value="10">Top 10</option>
            <option value="20">Top 20</option>
            <option value="50">Top 50</option>
            <option value="all">All</option>
          </select>
        </label>
      </div>
      <div id="an-super-categories" class="an-bars"></div>
    </article>
    <article class="an-card">
      <div class="an-card-head">
        <h2>Tags</h2>
        <label class="an-card-limit" for="an-tags-limit">Rows
          <select id="an-tags-limit" data-limit-for="an-tags">
            <option value="5" selected>Top 5</option>
            <option value="10">Top 10</option>
            <option value="20">Top 20</option>
            <option value="50">Top 50</option>
            <option value="all">All</option>
          </select>
        </label>
      </div>
      <div id="an-tags" class="an-bars"></div>
    </article>
    <article class="an-card">
      <div class="an-card-head">
        <h2>Types</h2>
        <label class="an-card-limit" for="an-types-limit">Rows
          <select id="an-types-limit" data-limit-for="an-types">
            <option value="5" selected>Top 5</option>
            <option value="10">Top 10</option>
            <option value="20">Top 20</option>
            <option value="50">Top 50</option>
            <option value="all">All</option>
          </select>
        </label>
      </div>
      <div id="an-types" class="an-bars"></div>
    </article>
  </section>
</div>

<script src="../javascripts/analytics-data.js"></script>
<script src="../javascripts/analytics.js"></script>
"""


ANALYTICS_JS = r"""'use strict';
(function(){
  const app=document.getElementById('an-app'); if(!app) return;
  const data=window.analyticsData;
  if(!data||!data.metrics){app.innerHTML='<p class="an-error">Analytics data is unavailable. Run <code>mkdocs build</code> to regenerate it.</p>';return;}
  const metrics=data.metrics||{};
  const barSections=[['an-authors',data.authors],['an-sources',data.sources],['an-super-categories',data.superCategories],['an-tags',data.tags],['an-types',data.types]];
  const subtitle=document.getElementById('an-subtitle'),metricRoot=document.getElementById('an-metrics'),limitSelects=Array.from(document.querySelectorAll('[data-limit-for]')),authorKicker=document.getElementById('an-author-kicker'),yearRoot=document.getElementById('an-years'),yearAxis=document.getElementById('an-year-axis'),yearTooltip=document.getElementById('an-year-tooltip');
  let yearAxisTicks=[];
  subtitle.textContent=(metrics.totalPapers||0)+' items indexed';
  renderMetrics(); renderYears(); renderAllBars();
  limitSelects.forEach(select=>select.addEventListener('change',()=>renderBarSection(select.getAttribute('data-limit-for'))));
  yearRoot.addEventListener('pointerover',e=>{const bin=e.target.closest('.an-year');if(bin)showYearTooltip(bin,e);});
  yearRoot.addEventListener('pointermove',e=>{const bin=e.target.closest('.an-year');if(bin)positionYearTooltip(e.clientX,e.clientY);});
  yearRoot.addEventListener('pointerout',e=>{const bin=e.target.closest('.an-year');if(bin&&!bin.contains(e.relatedTarget))hideYearTooltip();});
  yearRoot.addEventListener('focusin',e=>{const bin=e.target.closest('.an-year');if(bin)showYearTooltip(bin);});
  yearRoot.addEventListener('focusout',e=>{if(e.target.closest('.an-year'))hideYearTooltip();});
  if(window.ResizeObserver&&yearAxis){new ResizeObserver(renderYearAxis).observe(yearAxis);}else{window.addEventListener('resize',renderYearAxis);}
  function renderMetrics(){const yearRange=metrics.minYear&&metrics.maxYear?metrics.minYear+' - '+metrics.maxYear:'Unknown';metricRoot.innerHTML=[card('Papers',metrics.totalPapers),card('Unique Authors',metrics.uniqueAuthors),card('Sources',metrics.uniqueSources),card('Unique Tags',metrics.uniqueTags),card('Year Range',yearRange),card('arXiv IDs',metrics.arxivPapers),card('DOIs',metrics.doiPapers)].join('');}
  function renderYears(){const rows=Array.isArray(data.years)?data.years:[],root=yearRoot,max=Math.max(1,...rows.map(r=>r.count||0));if(!rows.length){root.innerHTML='<p class="an-empty">No dated papers.</p>';if(yearAxis)yearAxis.innerHTML='';yearAxisTicks=[];return;}const total=rows.reduce((sum,r)=>sum+binWidth(r),0);const bars=rows.map(r=>{const label=r.label||r.year||'',count=r.count||0,width=binWidth(r),tip=label+': '+count;return '<span class="an-year" data-range="'+escAttr(label)+'" data-count="'+escAttr(count)+'" tabindex="0" aria-describedby="an-year-tooltip" aria-label="'+escAttr(tip)+'" style="--an-bin-w:'+width+'"><i style="--an-h:'+Math.max(2,Math.round(count/max*100))+'%"></i></span>';}).join('');root.innerHTML=bars;yearAxisTicks=axisTickCandidates(rows,total);renderYearAxis();}
  function renderAllBars(){authorKicker.textContent=plural(metrics.uniqueAuthors||0,'unique author')+' counted across author lists';barSections.forEach(([id,rows])=>renderBars(id,rows,selectedLimit(id)));}
  function renderBarSection(id){const section=barSections.find(([sectionId])=>sectionId===id);if(section)renderBars(section[0],section[1],selectedLimit(id));}
  function selectedLimit(id){const select=limitSelects.find(el=>el.getAttribute('data-limit-for')===id),value=select?select.value:'5';return value==='all'?Infinity:(parseInt(value,10)||5);}
  function renderBars(id,rows,limit){const root=document.getElementById(id),allItems=(Array.isArray(rows)?rows:[]).filter(r=>r&&r.count>0),visibleItems=allItems.slice(0,limit),max=Math.max(1,...visibleItems.map(r=>r.count));if(!allItems.length){root.innerHTML='<p class="an-empty">No data.</p>';return;}const bars=visibleItems.map(r=>'<div class="an-bar"><span class="an-bar-label" title="'+escAttr(r.label)+'">'+esc(r.label)+'</span><span class="an-bar-track"><span class="an-bar-fill" style="--an-w:'+Math.round(r.count/max*100)+'%"></span></span><span class="an-bar-count">'+esc(r.count)+'</span></div>').join('');const hidden=allItems.length-visibleItems.length;root.innerHTML=bars+(hidden>0?'<div class="an-more">'+esc(plural(hidden,'more item'))+' not displayed</div>':'');}
  function showYearTooltip(bin,e){if(!yearTooltip)return;const range=bin.getAttribute('data-range')||'',count=bin.getAttribute('data-count')||'0';yearTooltip.innerHTML=esc(range)+'<span>'+esc(plural(parseInt(count,10)||0,'paper'))+'</span>';yearTooltip.hidden=false;yearTooltip.classList.add('is-visible');if(e){positionYearTooltip(e.clientX,e.clientY);return;}const rect=bin.getBoundingClientRect();positionYearTooltip(rect.left+rect.width/2,rect.top);}
  function hideYearTooltip(){if(!yearTooltip)return;yearTooltip.classList.remove('is-visible');yearTooltip.hidden=true;}
  function positionYearTooltip(x,y){if(!yearTooltip||yearTooltip.hidden)return;const pad=8;yearTooltip.style.left=Math.min(Math.max(x,pad),window.innerWidth-pad)+'px';yearTooltip.style.top=Math.min(Math.max(y,pad),window.innerHeight-pad)+'px';}
  function renderYearAxis(){if(!yearAxis)return;const ticks=sampleAxisTicks(yearAxisTicks,yearAxis);yearAxis.innerHTML=ticks.map(t=>'<span class="an-year-axis-tick"'+tickEdgeAttr(t)+' style="--an-x:'+escAttr(t.x)+'%">'+esc(t.label)+'</span>').join('');}
  function binWidth(row){const width=parseFloat(row&&row.width);if(Number.isFinite(width)&&width>0)return width;const start=parseInt(row&&row.start,10);return Number.isFinite(start)&&start<1941?10:5;}
  function axisTickCandidates(rows,total){const ticks=[];let offset=0;rows.forEach(row=>{const width=binWidth(row),start=parseInt(row.start,10),end=parseInt(row.end,10),left=offset/total*100,right=(offset+width)/total*100;if(Number.isFinite(end)&&end<1940){ticks.push({label:'Pre-1940',x:((left+right)/2).toFixed(4),kind:'pre'});}else{if(Number.isFinite(start)&&start<=1941){ticks.push({label:'1940',x:left.toFixed(4),kind:'year'});}if(Number.isFinite(end)){ticks.push({label:String(end),x:right.toFixed(4),kind:'year'});}}offset+=width;});if(ticks.length)ticks[ticks.length-1].required=true;return ticks;}
  function sampleAxisTicks(ticks,axis){const all=Array.isArray(ticks)?ticks.filter(Boolean):[];if(all.length<=1)return all;const width=axis.clientWidth||axis.getBoundingClientRect().width||0;if(width<=0)return all.filter(t=>t.required||t.kind!=='year');const yearTicks=all.filter(t=>t.kind==='year'),preTicks=all.filter(t=>t.kind!=='year');for(const includePre of [true,false]){for(let step=1;step<=Math.max(1,yearTicks.length);step++){const chosen=yearTicks.filter((t,i)=>t.required||i%step===0);if(includePre)chosen.unshift(...preTicks);const ordered=dedupeTicks(chosen).sort((a,b)=>parseFloat(a.x)-parseFloat(b.x));if(!hasTickCollisions(ordered,axis,width))return ordered;}}return all.filter(t=>t.required);}
  function dedupeTicks(ticks){const seen=new Set();return ticks.filter(t=>{const key=t.label+'@'+t.x;if(seen.has(key))return false;seen.add(key);return true;});}
  function hasTickCollisions(ticks,axis,width){let lastRight=-Infinity;const gap=6;for(const tick of ticks){const box=tickBox(tick,axis,width);if(box.left<0||box.right>width||box.left<lastRight+gap)return true;lastRight=box.right;}return false;}
  function tickBox(tick,axis,width){const labelWidth=measureTickLabel(tick.label,axis)+8,x=parseFloat(tick.x)/100*width,edge=tickEdge(tick);let left=x-labelWidth/2;if(edge==='start')left=x;if(edge==='end')left=x-labelWidth;return{left,right:left+labelWidth};}
  function measureTickLabel(label,axis){const style=getComputedStyle(axis),canvas=measureTickLabel.canvas||(measureTickLabel.canvas=document.createElement('canvas')),ctx=canvas.getContext('2d');ctx.font=[style.fontStyle,style.fontVariant,style.fontWeight,style.fontSize,style.fontFamily].filter(Boolean).join(' ');return ctx.measureText(String(label||'')).width;}
  function tickEdge(tick){const x=parseFloat(tick&&tick.x);if(x<=0.001)return'start';if(x>=99.999)return'end';return'';}
  function tickEdgeAttr(tick){const edge=tickEdge(tick);return edge?' data-edge="'+edge+'"':'';}
  function card(label,value){return '<div class="an-metric"><strong>'+esc(value==null?'':value)+'</strong><span>'+esc(label)+'</span></div>';}
  function plural(n,s,p){return n+' '+(n===1?s:(p||s+'s'));}
  function norm(v){return String(v||'').toLowerCase().normalize('NFKD').replace(/[\u0300-\u036f]/g,'');}
  function esc(v){return String(v||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');}
  function escAttr(v){return esc(v).replace(/`/g,'&#96;');}
})();"""


TIMELINE_PAGE = r"""---
hide:
  - toc
---

<style>
body:has(#tl-app) .md-grid{max-width:100%!important}body:has(#tl-app) .md-content{padding:0 .8rem!important}.md-content__inner:has(#tl-app){margin:0!important;padding:0!important;max-width:100%!important}
.tl-page{--tl-blue:#2367b3;--tl-teal:#13877f;--tl-rose:#bb3974;--tl-gold:#ad6b16;--tl-ink:var(--md-default-fg-color);--tl-muted:var(--md-default-fg-color--light);--tl-border:color-mix(in srgb,var(--md-default-fg-color) 15%,transparent);--tl-soft-border:color-mix(in srgb,var(--md-default-fg-color) 9%,transparent);--tl-panel:color-mix(in srgb,var(--md-code-bg-color) 70%,var(--md-default-bg-color));--tl-panel-strong:color-mix(in srgb,var(--tl-blue) 10%,var(--md-default-bg-color));--tl-shadow:0 12px 28px color-mix(in srgb,#000 13%,transparent);display:flex;flex-direction:column;gap:.85rem;margin-top:1rem}
[data-md-color-scheme="slate"] .tl-page{--tl-blue:#58a6ff;--tl-teal:#25b8ad;--tl-rose:#ff6aa8;--tl-gold:#f0a33e;--tl-panel:color-mix(in srgb,var(--md-code-bg-color) 82%,#050910);--tl-panel-strong:color-mix(in srgb,var(--tl-blue) 16%,var(--md-default-bg-color));--tl-shadow:0 14px 34px color-mix(in srgb,#000 36%,transparent)}
.tl-header{display:flex;align-items:start;justify-content:space-between;gap:1rem}.md-typeset .tl-header h1{margin:0;line-height:1.12}.md-typeset .tl-header p{margin:.28rem 0 0;color:var(--tl-muted);font-size:.82rem}.tl-detail-actions a{display:inline-grid;place-items:center;min-height:2.1rem;padding:.36rem .65rem;border:1px solid var(--tl-border);border-radius:8px;background:var(--md-default-bg-color);color:var(--md-typeset-a-color);font-size:.78rem;font-weight:700;text-decoration:none;transition:border-color .16s ease,background .16s ease,transform .16s ease}.tl-detail-actions a:hover{border-color:var(--tl-blue);background:color-mix(in srgb,var(--tl-blue) 8%,transparent);transform:translateY(-1px)}
.tl-controls{display:grid;grid-template-columns:minmax(16rem,1fr) auto auto auto auto;gap:.65rem;align-items:end;padding:.85rem;border:1px solid var(--tl-border);border-radius:8px;background:var(--tl-panel);box-shadow:0 8px 22px color-mix(in srgb,#000 8%,transparent)}.tl-search,.tl-control-group{display:grid;gap:.25rem}.tl-search label,.tl-control-group>span,.tl-control-group>label,.tl-switch-label{color:var(--tl-muted);font-size:.72rem;font-weight:800;letter-spacing:0;text-transform:uppercase}.tl-search input,.tl-year-control input{box-sizing:border-box;min-height:2.35rem;border:1px solid var(--tl-border);border-radius:8px;background:var(--md-default-bg-color);color:var(--tl-ink);font:inherit}.tl-search input{width:100%;min-width:0;padding:.58rem .72rem}.tl-year-control>div{display:flex;align-items:center;gap:.32rem}.tl-year-control input{width:5.3rem;padding:.42rem .5rem}.tl-search input:focus,.tl-year-control input:focus{border-color:var(--tl-blue);outline:2px solid color-mix(in srgb,var(--tl-blue) 24%,transparent);outline-offset:1px}
.tl-segmented{display:inline-flex;min-height:2.35rem;overflow:hidden;border:1px solid var(--tl-border);border-radius:8px;background:var(--md-default-bg-color)}.tl-segmented button,#tl-reset{min-height:2.35rem;border:0;background:transparent;color:var(--tl-ink);font:inherit;font-weight:700;cursor:pointer}.tl-segmented button{padding:.48rem .64rem;border-right:1px solid var(--tl-soft-border)}.tl-segmented button:last-child{border-right:0}.tl-segmented button[aria-pressed="true"]{background:color-mix(in srgb,var(--tl-blue) 14%,transparent);color:var(--md-typeset-a-color)}#tl-reset{align-self:end;padding:.48rem .85rem;border:1px solid var(--tl-border);border-radius:8px;background:var(--md-default-bg-color)}#tl-reset:hover,.tl-segmented button:hover{background:color-mix(in srgb,var(--tl-blue) 8%,transparent)}
.tl-switch{display:grid;gap:.25rem}.tl-switch-row{display:flex;align-items:center;gap:.55rem;min-height:2.35rem;padding:0 .65rem;border:1px solid var(--tl-border);border-radius:8px;background:var(--md-default-bg-color);cursor:pointer}.tl-switch-row input{position:absolute;opacity:0;pointer-events:none}.tl-switch-track{position:relative;width:2.3rem;height:1.22rem;border-radius:999px;background:color-mix(in srgb,var(--md-default-fg-color) 20%,transparent);transition:background .16s ease}.tl-switch-track::after{content:"";position:absolute;top:.16rem;left:.17rem;width:.9rem;height:.9rem;border-radius:50%;background:var(--md-default-bg-color);box-shadow:0 1px 4px color-mix(in srgb,#000 28%,transparent);transition:transform .16s ease}.tl-switch-row input:checked+.tl-switch-track{background:var(--tl-teal)}.tl-switch-row input:checked+.tl-switch-track::after{transform:translateX(1.04rem)}.tl-switch-text{font-size:.78rem;font-weight:700;color:var(--tl-ink)}
.tl-workbench{display:grid;grid-template-columns:minmax(16rem,21rem) minmax(0,1fr);gap:.85rem;align-items:start}.tl-sidebar,.tl-stage{min-width:0}.tl-sidebar{position:sticky;top:4.2rem;display:grid;gap:.85rem;max-height:calc(100vh - 5.5rem);overflow:auto;scrollbar-width:thin}.tl-sidebar>div,.tl-detail,.tl-stage{border:1px solid var(--tl-border);border-radius:8px;background:var(--tl-panel);box-shadow:var(--tl-shadow)}.tl-sidebar>div,.tl-detail{padding:.78rem}.tl-sidebar h2,.tl-detail h2{margin:0 0 .58rem;font-size:.95rem;line-height:1.25}.tl-legend{display:grid;gap:.35rem}.tl-legend-item{display:grid;grid-template-columns:auto minmax(0,1fr) auto;gap:.5rem;align-items:center;width:100%;min-height:2.15rem;padding:.35rem .48rem;border:1px solid transparent;border-radius:8px;background:transparent;color:var(--tl-ink);cursor:pointer;font:inherit;text-align:left}.tl-legend-item:hover,.tl-legend-item.is-active{border-color:var(--tl-border);background:var(--tl-panel-strong)}.tl-legend-item span:nth-child(2){min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.tl-legend-item strong{color:var(--tl-muted);font-size:.76rem}.tl-legend-swatch{width:.72rem;height:.72rem;border:1px solid color-mix(in srgb,#000 22%,transparent);border-radius:50%;background:var(--tl-swatch)}
.tl-detail{color:var(--tl-ink)}.tl-detail p{margin:.5rem 0 0;color:var(--tl-muted);font-size:.82rem;line-height:1.5}.tl-detail-kicker{margin-bottom:.25rem;color:var(--tl-gold);font-size:.72rem;font-weight:900}.tl-detail-title{color:var(--tl-ink)!important;font-weight:700}.tl-detail dl{display:grid;gap:.42rem;margin:.7rem 0 0}.tl-detail dl>div{display:grid;grid-template-columns:4.5rem minmax(0,1fr);gap:.45rem}.tl-detail dt{color:var(--tl-muted);font-size:.72rem;font-weight:800}.tl-detail dd{min-width:0;margin:0;overflow-wrap:anywhere;font-size:.78rem}.tl-summary{color:var(--tl-ink)!important}.tl-tags{display:flex;flex-wrap:wrap;gap:.28rem;margin-top:.72rem}.tl-tags span{padding:.16rem .42rem;border:1px solid var(--tl-soft-border);border-radius:999px;background:color-mix(in srgb,var(--tl-teal) 8%,transparent);color:var(--tl-muted);font-size:.68rem}.tl-detail-actions{display:flex;flex-wrap:wrap;gap:.42rem;margin-top:.8rem}
.tl-stage{overflow:hidden}.tl-stage-toolbar{display:flex;align-items:center;justify-content:space-between;gap:.6rem;min-height:2.7rem;padding:.62rem .75rem;border-bottom:1px solid var(--tl-border);color:var(--tl-muted);font-size:.8rem}#tl-selection-chip{max-width:50%;padding:.18rem .46rem;border:1px solid color-mix(in srgb,var(--tl-gold) 48%,transparent);border-radius:999px;background:color-mix(in srgb,var(--tl-gold) 11%,transparent);color:var(--tl-ink);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.tl-svg-wrap{width:100%;max-height:min(78vh,980px);overflow-x:hidden;overflow-y:auto;background:var(--md-default-bg-color);scrollbar-width:thin}#tl-svg{display:block;width:100%;height:auto;min-width:0;max-width:100%!important;font-family:"Atkinson Hyperlegible Next","Segoe UI",sans-serif}.tl-svg-bg{fill:var(--md-default-bg-color)}.tl-grid-minor,.tl-grid-major{stroke:color-mix(in srgb,var(--md-default-fg-color) 11%,transparent);stroke-width:1}.tl-grid-major{stroke:color-mix(in srgb,var(--md-default-fg-color) 19%,transparent)}.tl-axis-line,.tl-lane-line{stroke:color-mix(in srgb,var(--md-default-fg-color) 18%,transparent);stroke-width:1}.tl-lane-line{stroke-dasharray:3 8}.tl-year-label{fill:var(--tl-muted);font-size:11px;font-weight:800;text-anchor:middle}.tl-group-label-bg{fill:var(--tl-panel);stroke:var(--tl-soft-border)}.tl-group-swatch{stroke:color-mix(in srgb,#000 20%,transparent);stroke-width:1.2}.tl-group-label{fill:var(--tl-ink);font-size:12px;font-weight:850}.tl-group-meta{fill:var(--tl-muted);font-size:10px;font-weight:700}.tl-stream{fill-opacity:.22;stroke-opacity:.55;stroke-width:1.2;vector-effect:non-scaling-stroke}.tl-paper-node{cursor:pointer;outline:none}.tl-paper-dot{stroke:var(--md-default-bg-color);stroke-width:1.8;vector-effect:non-scaling-stroke;transition:r .12s ease,stroke-width .12s ease}.tl-paper-node:hover .tl-paper-dot,.tl-paper-node:focus .tl-paper-dot{stroke:var(--tl-gold);stroke-width:3}.tl-paper-node.is-selected .tl-paper-dot{stroke:var(--tl-gold);stroke-width:3.2}.tl-selected-year-line{stroke:var(--tl-gold);stroke-dasharray:6 6;stroke-width:1.4;opacity:.82;pointer-events:none}.tl-selected-label{fill:var(--tl-ink);paint-order:stroke;stroke:var(--md-default-bg-color);stroke-width:4px;font-size:12px;font-weight:900;pointer-events:none}.tl-empty-svg{fill:var(--tl-muted);font-size:14px}.tl-empty,.tl-error{margin:0;color:var(--tl-muted)}
@media (max-width:980px){.tl-controls{grid-template-columns:1fr 1fr}.tl-workbench{grid-template-columns:1fr}.tl-sidebar{position:static;max-height:none;grid-template-columns:1fr}}@media (max-width:680px){.md-content__inner:has(#tl-app){max-width:100%}.tl-header{display:grid}.tl-controls{grid-template-columns:1fr}.tl-year-control>div{display:grid;grid-template-columns:1fr auto 1fr}.tl-year-control input{width:100%}#tl-selection-chip{max-width:100%}.tl-stage-toolbar{align-items:start;flex-direction:column}.tl-svg-wrap{max-height:72vh}}
</style>

<div id="tl-app" class="tl-page">
  <header class="tl-header">
    <div>
      <h1>Timeline</h1>
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
  const svg=document.getElementById('tl-svg'),svgWrap=document.getElementById('tl-svg-wrap'),status=document.getElementById('tl-status'),legend=document.getElementById('tl-legend'),detail=document.getElementById('tl-detail'),chip=document.getElementById('tl-selection-chip'),form=document.getElementById('tl-search-form'),search=document.getElementById('tl-search'),yearStart=document.getElementById('tl-year-start'),yearEnd=document.getElementById('tl-year-end'),reset=document.getElementById('tl-reset'),dotsToggle=document.getElementById('tl-show-dots'),modeButtons=Array.from(app.querySelectorAll('[data-tl-mode]'));
  const hslCache=new Map(),colorCache=new Map(),subColorCache=new Map(),jitterCache=new Map();
  const papers=data.papers.map(p=>{const y=Number.isInteger(p.year)?p.year:null;const sup=p.superCategory||UNCATEGORIZED;const cat=p.category||UNCATEGORIZED;const sub=p.subCategory||'';return Object.assign({},p,{year:y,superCategory:sup,category:cat,subCategory:sub,searchText:norm([p.label,p.title,p.authorShort,Array.isArray(p.authors)?p.authors.join(' '):'',y||'',sup,cat,sub,Array.isArray(p.tags)?p.tags.join(' '):'',p.summary||''].join(' '))});});
  const paperById=new Map(papers.map(p=>[p.id,p]));
  const plotted=papers.filter(p=>Number.isInteger(p.year));
  const minYear=data.meta.minYear||Math.min(...plotted.map(p=>p.year)),maxYear=data.meta.maxYear||Math.max(...plotted.map(p=>p.year)),yearBins=normalizeYearBins((data.meta||{}).yearBins,minYear,maxYear),defaultStartYear=minYear;
  const state={mode:'category',activeSuper:null,query:'',selectedId:null,yearStart:defaultStartYear,yearEnd:maxYear,showDots:true};
  const hashId=readPaperHash(); if(hashId&&paperById.has(hashId)) state.selectedId=hashId;
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
  function renderSvg(groups){clear(svg);const wrapWidth=svgWrap?svgWrap.clientWidth:0,parentWidth=svg.parentElement?svg.parentElement.clientWidth:0,available=Math.max(320,Math.floor(wrapWidth||parentWidth||960)),compact=available<760,topLabels=available<680,margin={top:topLabels?54:44,right:compact?24:48,bottom:52,left:topLabels?24:(compact?204:282)},baseRowH=state.mode==='sub'?(compact?62:68):state.mode==='super'?(compact?84:92):(compact?70:78),rows=groups.map(g=>({group:g,rowH:baseRowH+Math.min(72,Math.max(0,maxYearCount(g.papers)-4)*4)})),innerW=Math.max(180,available-margin.left-margin.right),width=margin.left+innerW+margin.right,height=Math.max(420,margin.top+rows.reduce((sum,r)=>sum+r.rowH,0)+margin.bottom),bottom=height-margin.bottom;svg.setAttribute('viewBox','0 0 '+width+' '+height);svg.setAttribute('width','100%');svg.setAttribute('height',height);append(svg,'rect',{x:0,y:0,width:width,height:height,class:'tl-svg-bg'});drawGrid(svg,margin,width,bottom);if(!groups.length){append(svg,'text',{x:margin.left,y:margin.top+70,class:'tl-empty-svg'},'No dated papers match the current filters.');return;}let top=margin.top;rows.forEach(row=>{const center=topLabels?top+Math.max(56,row.rowH*.64):top+row.rowH/2;drawGroup(svg,row.group,top,center,row.rowH,margin,innerW,topLabels);top+=row.rowH;});const selected=state.selectedId?paperById.get(state.selectedId):null;if(selected&&Number.isInteger(selected.year)){const x=xForYear(selected.year,margin,innerW);append(svg,'line',{x1:x,x2:x,y1:margin.top-14,y2:bottom,class:'tl-selected-year-line'});}}
  function drawGrid(root,margin,width,bottom){const innerW=width-margin.left-margin.right,g=append(root,'g',{class:'tl-grid'}),bins=visibleYearBins();responsiveYearTicks(yearBoundaryTicks(bins),margin,innerW).forEach(tick=>{const x=xForScaleValue(tick.value,margin,innerW),major=tick.kind!=='one'||tick.year%5===0,label=String(tick.year);append(g,'line',{x1:x,x2:x,y1:margin.top-18,y2:bottom,class:major?'tl-grid-major':'tl-grid-minor'});append(g,'text',{x:x,y:margin.top-24,class:'tl-year-label'},label);append(g,'text',{x:x,y:bottom+30,class:'tl-year-label'},label);});append(g,'line',{x1:margin.left,x2:width-margin.right,y1:margin.top-6,y2:margin.top-6,class:'tl-axis-line'});append(g,'line',{x1:margin.left,x2:width-margin.right,y1:bottom+8,y2:bottom+8,class:'tl-axis-line'});}
  function yearBoundaryTicks(bins){if(!bins.length)return[];const ticks=[];bins.forEach((bin,i)=>{const leftYear=Math.max(bin.start,state.yearStart),next=bins[i+1];if(i===0||leftYear>ticks[ticks.length-1].year)ticks.push({year:leftYear,value:scaleForYear(leftYear),kind:bin.kind});if(next){const rightYear=Math.max(next.start,state.yearStart);ticks.push({year:rightYear,value:next.offset,kind:next.kind});}else{const rightYear=Math.min(bin.end,state.yearEnd);if(rightYear>ticks[ticks.length-1].year)ticks.push({year:rightYear,value:scaleForYear(rightYear,true),kind:bin.kind});}});return ticks.filter((tick,i,rows)=>i===0||tick.year!==rows[i-1].year||Math.abs(tick.value-rows[i-1].value)>1e-6);}
  function responsiveYearTicks(ticks,margin,innerW){if(ticks.length<2)return ticks;const minGap=42,withX=ticks.map(t=>Object.assign({x:xForScaleValue(t.value,margin,innerW),region:tickRegion(t.year)},t)),selected=[];['coarse','five','one'].forEach(region=>{const rows=withX.filter(t=>t.region===region);if(!rows.length)return;const gaps=rows.slice(1).map((t,i)=>t.x-rows[i].x).filter(g=>g>0),baseGap=gaps.length?Math.min(...gaps):innerW,step=Math.max(1,Math.ceil(minGap/baseGap));rows.forEach((tick,i)=>{if(i%step===0||i===rows.length-1)selected.push(tick);});});return withoutTickCollisions(selected.sort((a,b)=>a.x-b.x),minGap);}
  function withoutTickCollisions(ticks,minGap){let lastX=-Infinity;return ticks.filter(tick=>{if(tick.x-lastX<minGap)return false;lastX=tick.x;return true;});}
  function tickRegion(year){return year<1950?'coarse':year<2000?'five':'one';}
  function drawGroup(root,group,top,center,rowH,margin,innerW,topLabels){const lane=append(root,'g',{class:'tl-group','data-group-key':group.key}),labelMax=topLabels?Math.max(72,innerW-90):Math.max(44,margin.left-60);append(lane,'line',{x1:margin.left,x2:margin.left+innerW,y1:center,y2:center,class:'tl-lane-line'});if(topLabels){append(lane,'rect',{x:margin.left,y:top+6,width:innerW,height:34,rx:8,class:'tl-group-label-bg'});append(lane,'circle',{cx:margin.left+12,cy:top+23,r:5,fill:group.color,class:'tl-group-swatch'});fitSvgText(append(lane,'text',{x:margin.left+26,y:top+20,class:'tl-group-label'},group.label),group.label,labelMax);append(lane,'text',{x:margin.left+26,y:top+34,class:'tl-group-meta'},plural(group.papers.length,'paper'));}else{append(lane,'rect',{x:0,y:top+4,width:margin.left-18,height:rowH-8,rx:8,class:'tl-group-label-bg'});append(lane,'circle',{cx:18,cy:center,r:5,fill:group.color,class:'tl-group-swatch'});fitSvgText(append(lane,'text',{x:32,y:center-3,class:'tl-group-label'},group.label),group.label,labelMax);append(lane,'text',{x:32,y:center+14,class:'tl-group-meta'},plural(group.papers.length,'paper'));}append(lane,'path',{d:streamPath(group,center,rowH,margin,innerW),fill:group.color,stroke:group.color,class:'tl-stream'});if(!state.showDots)return;const byYear=new Map();group.papers.forEach(p=>{if(!byYear.has(p.year))byYear.set(p.year,[]);byYear.get(p.year).push(p);});Array.from(byYear.keys()).sort((a,b)=>a-b).forEach(year=>{const items=byYear.get(year).sort((a,b)=>a.label.localeCompare(b.label)),range=jitterRangeForYear(year,items.length,innerW),topLimit=top+(topLabels?44:14),bottomLimit=top+rowH-14,yRadius=items.length<2?0:Math.max(0,Math.min(rowH*.34,(bottomLimit-topLimit)/2));items.forEach(p=>{const jitter=timelineJitter(group.key,year,p.id),x=xForYear(year,margin,innerW,jitter.x*range),y=clamp(center+jitter.y*yRadius,topLimit,bottomLimit);drawPaper(lane,p,x,y,group.color);});});}
  function fitSvgText(el,text,maxWidth){const value=String(text||'');el.textContent=value;if(!value||safeTextLength(el)<=maxWidth)return;const suffix='...';let lo=0,hi=value.length,best=suffix;while(lo<=hi){const mid=Math.floor((lo+hi)/2),next=value.slice(0,mid).trimEnd()+suffix;el.textContent=next;if(safeTextLength(el)<=maxWidth){best=next;lo=mid+1;}else{hi=mid-1;}}el.textContent=best;}
  function safeTextLength(el){return typeof el.getComputedTextLength==='function'?el.getComputedTextLength():el.textContent.length*7;}
  function streamPath(group,center,rowH,margin,innerW){const counts=new Map();group.papers.forEach(p=>counts.set(p.year,(counts.get(p.year)||0)+1));const bins=visibleYearBins(),samples=[];bins.forEach(bin=>{let v=0;counts.forEach((c,cy)=>{const d=(scaleForYear(cy)-bin.offset)/Math.max(1.1,bin.width*1.15);v+=c*Math.exp(-.5*d*d);});const h=clamp(3+Math.log1p(v)*10.5,3.2,rowH/2-10);samples.push({x:xForScaleValue(bin.offset+bin.width/2,margin,innerW),top:center-h,bottom:center+h});});if(!samples.length)samples.push({x:margin.left,top:center-3,bottom:center+3});return 'M '+samples.map(p=>p.x.toFixed(1)+' '+p.top.toFixed(1)).join(' L ')+' L '+samples.slice().reverse().map(p=>p.x.toFixed(1)+' '+p.bottom.toFixed(1)).join(' L ')+' Z';}
  function drawPaper(root,p,x,y,color){const selected=p.id===state.selectedId,g=append(root,'g',{class:'tl-paper-node'+(selected?' is-selected':''),'data-paper-id':p.id,tabindex:0,role:'button','aria-label':p.label+', '+p.year});append(g,'circle',{cx:x,cy:y,r:selected?6.8:4.4,fill:color,class:'tl-paper-dot'});append(g,'title',{},p.year+' - '+p.label+'\n'+p.title);if(selected)append(g,'text',{x:x+10,y:y-9,class:'tl-selected-label'},p.label);}
  function xForYear(y,margin,innerW,offset){return xForScaleValue(scaleForYear(y),margin,innerW)+(offset||0);}
  function xForScaleValue(v,margin,innerW){const start=scaleForYear(state.yearStart),end=scaleForYear(state.yearEnd,true);return margin.left+((v-start)/Math.max(1e-6,end-start))*innerW;}
  function scaleForYear(year,endEdge){const y=clampYear(year),bin=yearBins.find(b=>y>=b.start&&y<=b.end)||yearBins[yearBins.length-1];if(!bin)return y;const span=Math.max(1,bin.end-bin.start+(endEdge?0:1));const pos=endEdge&&y===bin.end?bin.width:((y-bin.start)/span)*bin.width;return bin.offset+pos;}
  function visibleYearBins(){const bins=yearBins.filter(bin=>bin.end>=state.yearStart&&bin.start<=state.yearEnd);return bins.length?bins:yearBins;}
  function normalizeYearBins(raw,minY,maxY){const rows=(Array.isArray(raw)?raw:[]).filter(b=>Number.isFinite(parseInt(b.start,10))&&Number.isFinite(parseInt(b.end,10))).map(b=>({label:String(b.label||b.start),start:parseInt(b.start,10),end:parseInt(b.end,10),width:binWidth(b),kind:binKind(b)})).sort((a,b)=>a.start-b.start);const bins=rows.length?rows:[{label:String(minY),start:minY,end:maxY,width:Math.max(1,maxY-minY+1),kind:'one'}];let offset=0;bins.forEach(bin=>{bin.offset=offset;offset+=bin.width;});return bins;}
  function binWidth(row){const width=parseFloat(row&&row.width);if(Number.isFinite(width)&&width>0)return width;const start=parseInt(row&&row.start,10);return Number.isFinite(start)?(start<1950?10:start<2000?5:1):1;}
  function binKind(row){const start=parseInt(row&&row.start,10);return Number.isFinite(start)&&start<1950?'coarse':Number.isFinite(start)&&start<2000?'five':'one';}
  function maxYearCount(items){const counts=new Map();(items||[]).forEach(p=>counts.set(p.year,(counts.get(p.year)||0)+1));return Math.max(0,...counts.values());}
  function timelineJitter(groupKey,year,paperId){const key=groupKey+'::'+year+'::'+paperId;if(!jitterCache.has(key))jitterCache.set(key,{x:Math.random()*2-1,y:Math.random()*2-1});return jitterCache.get(key);}
  function jitterRangeForYear(year,count,innerW){if(count<2)return 0;const bin=yearBins.find(b=>year>=b.start&&year<=b.end),start=scaleForYear(state.yearStart),end=scaleForYear(state.yearEnd,true),pxPerUnit=innerW/Math.max(1e-6,end-start),usable=Math.max(14,(bin?bin.width:1)*pxPerUnit*.74);return Math.min(28,usable/2);}
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


analytics_data = build_analytics_data(root)
timeline_data = build_timeline_data(root)

with mkdocs_gen_files.open("analytics.md", "w") as out:
    out.write(ANALYTICS_PAGE)

with mkdocs_gen_files.open("javascripts/analytics-data.js", "w") as out:
    out.write("window.analyticsData = ")
    out.write(json.dumps(analytics_data, indent=2, ensure_ascii=False))
    out.write(";\n")

with mkdocs_gen_files.open("javascripts/analytics.js", "w") as out:
    out.write(ANALYTICS_JS)
    out.write("\n")

with mkdocs_gen_files.open("timeline.md", "w") as out:
    out.write(TIMELINE_PAGE)

with mkdocs_gen_files.open("javascripts/timeline-data.js", "w") as out:
    out.write("window.timelineData = ")
    out.write(json.dumps(timeline_data, indent=2, ensure_ascii=False))
    out.write(";\n")

with mkdocs_gen_files.open("javascripts/timeline.js", "w") as out:
    out.write(TIMELINE_JS)
    out.write("\n")
