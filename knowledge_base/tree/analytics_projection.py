"""Analytics generated-page and data projection."""

from __future__ import annotations

import json
import re
from collections import Counter
from typing import Any

from knowledge_base.publishing.generated_assets import ANALYTICS_DATA, render_app_script_tags
from knowledge_base.publishing.generated_files import open_generated
from knowledge_base.tree.model import TreeModel
from knowledge_base.tree.projection_common import (
    UNCATEGORIZED_CATEGORY,
    as_list,
    clean_text,
    page_url,
    slugify_id,
)
from knowledge_base.tree.timeline_projection import build_timeline_nav_index


def count_rows(counter: Counter[Any], *, limit: int | None = None) -> list[dict[str, Any]]:
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


def build_year_bins(year_counts: Counter[int]) -> list[dict[str, Any]]:
    years = sorted(year_counts)
    if not years:
        return []

    min_year = min(years)
    max_year = max(years)
    ranges: list[tuple[int, int]] = []

    if min_year < 1950:
        ranges.append((min_year, min(1949, max_year)))
    ranges.extend((max(start, min_year), min(start + 4, max_year)) for start in range(1950, min(2000, max_year + 1), 5))
    ranges.extend((year, year) for year in range(max(2000, min_year), max_year + 1))

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


def analytics_bin_step(year: int, mode: str) -> int:
    if mode == "fine":
        if year >= 2000:
            return 1
        if year >= 1950:
            return 5
        if year >= 1900:
            return 10
        return 50

    if year >= 2000:
        return 5
    if year >= 1950:
        return 10
    return 50


def analytics_bin_region(year: int, mode: str) -> str:
    if mode == "fine":
        if year >= 2000:
            return "2000-present"
        if year >= 1950:
            return "1950-1999"
        if year >= 1900:
            return "1900-1949"
        return "Pre-1900"

    if year >= 2000:
        return "2000-present"
    if year >= 1950:
        return "1950-1999"
    return "Pre-1950"


def aligned_bin_start(year: int, step: int) -> int:
    return (year // step) * step


def build_analytics_year_bins(year_counts: Counter[int], mode: str) -> list[dict[str, Any]]:
    years = sorted(year_counts)
    if not years:
        return []

    ranges: list[tuple[int, int, bool]] = []
    start = aligned_bin_start(min(years), analytics_bin_step(min(years), mode))
    max_year = max(years)
    while start <= max_year:
        step = analytics_bin_step(start, mode)
        raw_end = start + step - 1
        end = min(raw_end, max_year)
        ranges.append((start, end, mode == "coarse" and end == max_year))
        start = raw_end + 1

    rows: list[dict[str, Any]] = []
    for start, end, is_present_bucket in ranges:
        if start > end:
            continue
        row = {
            "label": f"{start}-Present" if is_present_bucket else year_bin_label(start, end),
            "start": start,
            "end": end,
            "width": analytics_bin_step(start, mode),
            "count": int(sum(year_counts.get(year, 0) for year in range(start, end + 1))),
            "region": analytics_bin_region(start, mode),
        }
        if is_present_bucket:
            row["presentYear"] = max_year
        rows.append(row)
    return rows


def normalize_author(author: str) -> str:
    return re.sub(r"\s+", " ", clean_text(author)).casefold()


def build_analytics_category_tree(root_node: dict[str, Any]) -> list[dict[str, Any]]:
    def build_branch_node(node: dict[str, Any]) -> dict[str, Any] | None:
        direct_papers = 0
        children: list[dict[str, Any]] = []

        for child in as_list(node.get("children")):
            if not isinstance(child, dict):
                continue
            if child.get("kind") == "paper":
                direct_papers += 1
            elif child.get("kind") == "branch":
                child_row = build_branch_node(child)
                if child_row:
                    children.append(child_row)

        count = direct_papers + sum(int(child.get("count") or 0) for child in children)
        if count <= 0:
            return None

        return {
            "id": str(node.get("id") or slugify_id(str(node.get("label") or ""))),
            "label": str(node.get("label") or "Untitled"),
            "count": count,
            "children": children,
        }

    rows: list[dict[str, Any]] = []
    for child in as_list(root_node.get("children")):
        if isinstance(child, dict) and child.get("kind") == "branch":
            row = build_branch_node(child)
            if row:
                rows.append(row)
    return rows


def build_analytics_data(
    root_node: dict[str, Any],
    model: TreeModel,
    paper_details_by_source: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    nav_index = build_timeline_nav_index(model)
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
            "path": ["Tree", UNCATEGORIZED_CATEGORY],
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
    coarse_year_rows = build_analytics_year_bins(year_counts, "coarse")
    fine_year_rows = build_analytics_year_bins(year_counts, "fine")
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
        "years": coarse_year_rows,
        "yearBins": {
            "coarse": coarse_year_rows,
            "fine": fine_year_rows,
        },
        "authors": author_rows,
        "sources": count_rows(source_counts),
        "types": count_rows(type_counts),
        "tags": count_rows(tag_counts),
        "superCategories": count_rows(super_counts),
        "categories": count_rows(category_counts),
        "categoryTree": build_analytics_category_tree(root_node),
        "auditStatuses": count_rows(audit_counts),
    }


ANALYTICS_PAGE = r"""---
hide:
  - toc
---

<style>
body:has(.md-content__inner > #an-app) .md-grid,body:has(.md-content__inner > #an-app) .md-main__inner{max-width:100%!important}body:has(.md-content__inner > #an-app) .md-content{max-width:none!important;padding:0!important}.md-content__inner:has(> #an-app){margin:0!important;padding:0!important;max-width:100%!important}body:has(.md-content__inner > #an-app) .md-footer,.md-content__inner:has(> #an-app)>h1:first-child,.md-content__inner:has(> #an-app)::before,.md-content__inner:has(> #an-app)::after{display:none!important}
.an-page{--an-blue:var(--kb-color-blue);--an-teal:var(--kb-color-teal);--an-rose:var(--kb-color-rose);--an-gold:var(--kb-color-gold);--an-ink:var(--md-default-fg-color);--an-muted:var(--md-default-fg-color--light);--an-border:var(--kb-border-strong);--an-soft-border:var(--kb-border-muted);--an-panel:var(--kb-surface-muted);--an-panel-strong:var(--kb-surface-tinted);--kb-app-border:var(--an-border);--kb-app-panel:var(--an-panel);--kb-app-header-bg:var(--kb-surface-raised);display:flex;flex-direction:column;gap:.9rem;margin-top:var(--kb-app-top-gap,1rem)}
[data-md-color-scheme="slate"] .an-page{--an-panel:var(--kb-surface-muted);--an-panel-strong:var(--kb-surface-tinted)}
.an-header{display:flex;align-items:center;justify-content:space-between;gap:1rem}.an-header.kb-app-header{background:var(--kb-app-header-bg)}.md-typeset .an-header h1{margin:0;line-height:1.2}.md-typeset .an-header p{margin:.28rem 0 0;color:var(--an-muted);font-size:.82rem}
.an-metrics{display:grid;grid-template-columns:repeat(auto-fit,minmax(7rem,1fr));gap:.62rem}.an-metric{min-width:0;padding:.74rem .8rem;border:1px solid var(--an-border);border-radius:8px;background:var(--an-panel)}.an-metric strong{display:block;color:var(--an-ink);font-size:1.35rem;line-height:1.1}.an-metric span{display:block;margin-top:.22rem;color:var(--an-muted);font-size:.72rem;font-weight:850;letter-spacing:0;text-transform:uppercase}.an-toolbar{display:flex;flex-wrap:wrap;align-items:end;gap:.65rem;padding:.78rem;border:1px solid var(--an-border);border-radius:8px;background:var(--an-panel)}.an-field{display:grid;gap:.25rem}.an-field:first-child{flex:1 1 18rem}.an-field label{color:var(--an-muted);font-size:.72rem;font-weight:850;text-transform:uppercase}.an-field input,.an-field select{box-sizing:border-box;min-height:2.35rem;border:1px solid var(--an-border);border-radius:8px;background:var(--md-default-bg-color);color:var(--an-ink);font:inherit}.an-field input{width:100%;padding:.58rem .72rem}.an-field select{padding:.42rem .56rem}.an-field input:focus,.an-field select:focus{border-color:var(--an-blue);outline:2px solid color-mix(in srgb,var(--an-blue) 24%,transparent);outline-offset:1px}
.an-grid{display:grid;grid-template-columns:1fr;gap:.85rem}.an-card{min-width:0;padding:.82rem;border:1px solid var(--an-border);border-radius:8px;background:var(--an-panel)}.an-card--wide{grid-column:1 / -1}.an-card-head{display:flex;align-items:center;justify-content:space-between;gap:.65rem;margin:0 0 .68rem}.an-card h2{margin:0 0 .68rem;font-size:1rem;line-height:1.2}.an-card-head h2{margin:0}.an-bin-toggle{display:inline-flex;min-height:1.9rem;overflow:hidden;border:1px solid var(--an-border);border-radius:8px;background:var(--md-default-bg-color)}.an-bin-toggle button{min-height:1.9rem;padding:.28rem .55rem;border:0;border-right:1px solid var(--an-soft-border);background:transparent;color:var(--an-ink);font:inherit;font-size:.7rem;font-weight:850;cursor:pointer}.an-bin-toggle button:last-child{border-right:0}.an-bin-toggle button[aria-pressed="true"]{background:color-mix(in srgb,var(--an-blue) 14%,transparent);color:var(--md-typeset-a-color)}.an-bin-toggle button:hover{background:color-mix(in srgb,var(--an-blue) 8%,transparent)}.an-card-limit{display:flex;align-items:center;gap:.35rem;color:var(--an-muted);font-size:.68rem;font-weight:850;text-transform:uppercase;white-space:nowrap}.an-card-limit[hidden]{display:none}.an-card-limit select{box-sizing:border-box;min-height:1.9rem;border:1px solid var(--an-border);border-radius:8px;background:var(--md-default-bg-color);color:var(--an-ink);font:inherit;padding:.22rem .4rem;text-transform:none}.an-card-limit select:focus{border-color:var(--an-blue);outline:2px solid color-mix(in srgb,var(--an-blue) 24%,transparent);outline-offset:1px}.an-card-kicker{margin:-.35rem 0 .68rem;color:var(--an-muted);font-size:.74rem}.an-bars{display:grid;gap:.36rem}.an-bar{display:grid;grid-template-columns:minmax(7.5rem,1fr) minmax(6rem,2.2fr) auto;gap:.52rem;align-items:center;min-height:1.75rem}.an-bar-label{min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:.78rem;font-weight:750}.an-bar-track{height:.64rem;overflow:hidden;border-radius:999px;background:color-mix(in srgb,var(--md-default-fg-color) 8%,transparent)}.an-bar-fill{display:block;width:var(--an-w);height:100%;border-radius:inherit;background:linear-gradient(90deg,var(--an-teal),var(--an-blue))}.an-bar-count{color:var(--an-muted);font-size:.74rem;font-weight:800;text-align:right}.an-more{width:100%;margin:.16rem 0 0;padding:.48rem .58rem;border:1px dashed var(--an-border);border-radius:8px;background:color-mix(in srgb,var(--an-blue) 6%,transparent);color:var(--an-muted);font:inherit;font-size:.73rem;font-weight:800;text-align:center;cursor:pointer}.an-more:hover,.an-more:focus-visible{border-color:var(--an-blue);background:color-mix(in srgb,var(--an-blue) 11%,transparent);color:var(--md-typeset-a-color)}.an-more:focus-visible{outline:2px solid color-mix(in srgb,var(--an-blue) 35%,transparent);outline-offset:2px}.an-more-note{margin:.16rem 0 0;color:var(--an-muted);font-size:.72rem;font-weight:750;text-align:center}.an-year-hist{position:relative;display:flex;align-items:end;gap:0;box-sizing:border-box;width:100%;min-height:13rem;overflow:hidden;padding:.45rem .2rem .3rem;border-bottom:1px solid var(--an-border)}.an-year{position:relative;z-index:1;display:grid;align-items:end;flex:var(--an-bin-w) 1 0;min-width:0;height:12rem;outline:none}.an-year i{display:block;height:var(--an-h);min-height:2px;margin:0 1px;border-radius:999px 999px 0 0;background:linear-gradient(180deg,var(--an-rose),var(--an-gold));transition:none}.an-year:focus-visible{outline:2px solid color-mix(in srgb,var(--an-blue) 55%,transparent);outline-offset:2px}.an-year-axis{position:relative;height:1.35rem;color:var(--an-muted);font-size:.72rem;font-weight:800}.an-year-axis-tick{position:absolute;top:0;left:var(--an-x);transform:translateX(-50%);white-space:nowrap}.an-year-axis-tick[data-edge="start"]{transform:translateX(0)}.an-year-axis-tick[data-edge="end"]{transform:translateX(-100%)}.an-year-axis-tick::before{content:"";display:block;width:1px;height:.36rem;margin:0 auto .08rem;background:var(--an-border)}.an-year-tooltip{display:none!important}.an-table-wrap{max-height:34rem;overflow:auto;border:1px solid var(--an-border);border-radius:8px;background:var(--md-default-bg-color);scrollbar-width:thin}.an-table{width:100%;border-collapse:collapse;font-size:.76rem}.an-table th{position:sticky;top:0;z-index:1;background:var(--an-panel);color:var(--an-muted);font-size:.68rem;text-align:left;text-transform:uppercase}.an-table th,.an-table td{padding:.48rem .55rem;border-bottom:1px solid var(--an-soft-border);vertical-align:top}.an-paper-cell{display:grid;gap:.12rem;min-width:14rem}.an-paper-cell a{font-weight:850}.an-paper-cell span{color:var(--an-muted);font-size:.71rem}.an-empty,.an-error{margin:0;color:var(--an-muted)}
@media (max-width:900px){.an-grid{grid-template-columns:1fr}.an-header{display:grid}.an-bar{grid-template-columns:minmax(0,1fr) minmax(5rem,1.2fr) auto}}@media (max-width:620px){.md-content__inner:has(#an-app){max-width:100%}.an-bar{grid-template-columns:1fr auto}.an-bar-track{grid-column:1 / -1}.an-table th:nth-child(3),.an-table td:nth-child(3){display:none}}
.an-bar{grid-template-columns:minmax(0,1fr) auto;column-gap:.52rem;row-gap:.18rem;align-items:start}.an-bar-label{grid-column:1;grid-row:1;overflow:visible;overflow-wrap:anywhere;white-space:normal;text-overflow:clip;line-height:1.25}.an-bar-count{grid-column:2;grid-row:1}.an-bar-track{grid-column:1 / -1;grid-row:2}
.an-year-hist{display:grid;gap:.42rem;min-height:0;overflow:visible;padding:0;border-bottom:0}.an-year{display:grid;grid-template-columns:minmax(0,1fr) auto;column-gap:.52rem;row-gap:.18rem;align-items:end;height:auto;outline:none;touch-action:pan-y}.an-year[data-region-start="true"]{position:relative;margin-top:.52rem;padding-top:1.05rem}.an-year[data-region-start="true"]::before{content:"";position:absolute;top:.52rem;left:0;right:0;border-top:1px solid color-mix(in srgb,var(--md-default-fg-color) 18%,transparent)}.an-year-label{grid-column:1;grid-row:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:.78rem;font-weight:750}.an-year-count{grid-column:2;grid-row:1;color:var(--an-muted);font-size:.74rem;font-weight:800;text-align:right}.an-year-track{grid-column:1 / -1;grid-row:2;height:.64rem;overflow:hidden;border-radius:999px;background:color-mix(in srgb,var(--md-default-fg-color) 8%,transparent)}.an-year i{display:block;width:var(--an-w);height:100%;min-height:0;margin:0;border-radius:inherit;background:linear-gradient(90deg,var(--an-teal),var(--an-blue));transition:none}.an-year-axis{display:none}
.an-category-control{display:flex;align-items:center;gap:.45rem}.an-category-control-label{color:var(--an-muted);font-size:.68rem;font-weight:850;text-transform:uppercase;white-space:nowrap}.an-category-level{display:grid;grid-template-columns:repeat(3,1.9rem);gap:4px}.an-category-level button{display:grid;place-items:center;width:1.9rem;height:1.9rem;min-width:1.9rem;min-height:1.9rem;padding:0;border:1px solid var(--an-border);border-radius:6px;background:var(--md-default-bg-color);color:var(--an-muted);cursor:pointer}.an-category-level button:hover{border-color:var(--an-blue);background:color-mix(in srgb,var(--an-blue) 9%,transparent);color:var(--an-ink)}.an-category-level button[aria-pressed="true"]{border-color:var(--an-blue);background:color-mix(in srgb,var(--an-blue) 16%,var(--md-default-bg-color));color:var(--an-ink)}.an-category-level button:focus-visible{outline:2px solid color-mix(in srgb,var(--an-blue) 28%,transparent);outline-offset:1px}.an-die{display:grid;width:1.25rem;height:1.25rem;grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3,1fr);align-items:center;justify-items:center}.an-die-dot{display:block;width:.42rem;height:.42rem;border-radius:999px;background:currentColor}.an-die--1 .an-die-dot:nth-child(1){grid-area:2/2}.an-die--2 .an-die-dot:nth-child(1){grid-area:2/1}.an-die--2 .an-die-dot:nth-child(2){grid-area:2/3}.an-die--3 .an-die-dot:nth-child(1){grid-area:1/2}.an-die--3 .an-die-dot:nth-child(2){grid-area:3/1}.an-die--3 .an-die-dot:nth-child(3){grid-area:3/3}.an-category-tree{display:grid;gap:.3rem}.an-category-row{display:grid;grid-template-columns:minmax(0,1fr) auto;column-gap:.52rem;row-gap:.18rem;align-items:start;min-height:1.8rem}.an-category-label{grid-column:1;grid-row:1;min-width:0;overflow:visible;overflow-wrap:anywhere;white-space:normal;text-overflow:clip;color:var(--an-ink);font-size:.78rem;font-weight:750;line-height:1.25}.an-category-path{display:block;margin-top:.05rem;overflow:visible;overflow-wrap:anywhere;white-space:normal;text-overflow:clip;color:var(--an-muted);font-size:.66rem;font-weight:650}.an-category-count{grid-column:2;grid-row:1;color:var(--an-muted);font-size:.74rem;font-weight:800;text-align:right}.an-category-track{grid-column:1 / -1;grid-row:2;min-width:0;height:.64rem;overflow:hidden;border-radius:999px;background:color-mix(in srgb,var(--md-default-fg-color) 8%,transparent)}.an-category-fill{display:block;width:var(--an-w);height:100%;border-radius:inherit;background:linear-gradient(90deg,var(--an-teal),var(--an-blue))}
.an-card,.an-card *{box-sizing:border-box}.an-card-head{min-width:0;flex-wrap:wrap}.an-category-control{min-width:0}.an-category-level{flex:0 0 auto}
@media (max-width:700px){.an-card-head{align-items:flex-start}.an-category-control{flex:1 1 100%;justify-content:space-between}}
@media (max-width:380px){.an-category-control{align-items:flex-start;display:grid;grid-template-columns:1fr}.an-category-level{justify-content:start}.an-category-label{overflow:visible;overflow-wrap:anywhere;white-space:normal;text-overflow:clip}.an-category-path{overflow-wrap:anywhere;white-space:normal}}
</style>

<div id="an-app" class="an-page kb-app-page">
  <header class="an-header kb-app-header kb-app-header--static">
    <div>
      <h1 class="kb-app-header-title">Analytics</h1>
    </div>
  </header>

  <section id="an-metrics" class="an-metrics" aria-label="Analytics metrics"></section>

  <section class="an-grid" aria-label="Aggregate charts">
    <article class="an-card an-card--wide">
      <div class="an-card-head">
        <h2>Years</h2>
        <div class="an-bin-toggle" role="group" aria-label="Year bin density">
          <button type="button" data-an-bin="coarse" aria-pressed="true">Coarse</button>
          <button type="button" data-an-bin="fine" aria-pressed="false">Fine</button>
        </div>
      </div>
      <div id="an-years" class="an-year-hist" role="img" aria-label="Horizontal bar chart of items by publication year"></div>
      <div id="an-year-axis" class="an-year-axis"></div>
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
            <option value="100">Top 100</option>
          </select>
        </label>
      </div>
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
            <option value="100">Top 100</option>
          </select>
        </label>
      </div>
      <div id="an-sources" class="an-bars"></div>
    </article>
    <article class="an-card">
      <div class="an-card-head">
        <h2>Categories</h2>
        <div class="an-category-control">
          <span class="an-category-control-label">Level of Detail</span>
          <div class="an-category-level" role="group" aria-label="Level of Detail">
            <button type="button" data-an-category-level="1" aria-pressed="true" aria-label="Level of detail: Level 1" title="Level 1"><span class="an-die an-die--1" aria-hidden="true"><span class="an-die-dot"></span></span></button>
            <button type="button" data-an-category-level="2" aria-pressed="false" aria-label="Level of detail: Level 2" title="Level 2"><span class="an-die an-die--2" aria-hidden="true"><span class="an-die-dot"></span><span class="an-die-dot"></span></span></button>
            <button type="button" data-an-category-level="3" aria-pressed="false" aria-label="Level of detail: Level 3" title="Level 3"><span class="an-die an-die--3" aria-hidden="true"><span class="an-die-dot"></span><span class="an-die-dot"></span><span class="an-die-dot"></span></span></button>
          </div>
        </div>
      </div>
      <div id="an-super-categories" class="an-category-tree"></div>
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
            <option value="100">Top 100</option>
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
            <option value="100">Top 100</option>
          </select>
        </label>
      </div>
      <div id="an-types" class="an-bars"></div>
    </article>
  </section>
</div>

""" + render_app_script_tags("analytics.md", "analytics") + "\n"


ANALYTICS_CSS = ANALYTICS_PAGE.split("<style>\n", 1)[1].split("</style>", 1)[0].strip()
ANALYTICS_HOME_CSS = "\n".join(ANALYTICS_CSS.splitlines()[1:]).strip()
ANALYTICS_APP_HTML = ANALYTICS_PAGE.split("</style>\n\n", 1)[1].split("\n\n<script", 1)[0].strip()
ANALYTICS_APP_HTML = re.sub(
    r"\n\s*<header class=\"an-header.*?</header>\n",
    "\n",
    ANALYTICS_APP_HTML,
    count=1,
    flags=re.S,
).strip()
ANALYTICS_APP_HTML = re.sub(
    r'^<div id="an-app" class="[^"]*">\n|\n</div>$',
    "",
    ANALYTICS_APP_HTML,
).strip()


ANALYTICS_JS = r"""'use strict';
(function(){
  const app=document.getElementById('an-app'); if(!app) return;
  const data=window.analyticsData;
  if(!data||!data.metrics){app.innerHTML='<p class="an-error">Analytics data is unavailable. Run <code>kb build</code> to regenerate it.</p>';return;}
  const MAX_BAR_ROWS=100,HIDE_LIMIT_BELOW=12;
  const metrics=data.metrics||{};
  const barSections=[['an-authors',data.authors],['an-sources',data.sources],['an-tags',data.tags],['an-types',data.types]];
  const metricRoot=document.getElementById('an-metrics'),limitSelects=Array.from(document.querySelectorAll('[data-limit-for]')),yearRoot=document.getElementById('an-years'),yearAxis=document.getElementById('an-year-axis'),binButtons=Array.from(app.querySelectorAll('[data-an-bin]')),categoryLevelButtons=Array.from(app.querySelectorAll('[data-an-category-level]')),yearTooltip=null;
  let categoryLevel=1;
  let yearBinMode='coarse';
  let yearAxisTicks=[];
  renderMetrics(); renderYears(); renderAllBars();
  limitSelects.forEach(select=>select.addEventListener('change',()=>renderBarSection(select.getAttribute('data-limit-for'))));
  app.addEventListener('click',e=>{const more=e.target.closest('.an-more');if(more)showMoreBars(more.getAttribute('data-more-for'));});
  binButtons.forEach(button=>button.addEventListener('click',()=>{yearBinMode=button.getAttribute('data-an-bin')==='fine'?'fine':'coarse';binButtons.forEach(btn=>btn.setAttribute('aria-pressed',String(btn===button)));renderYears();}));
  categoryLevelButtons.forEach(button=>button.addEventListener('click',()=>{categoryLevel=Math.max(1,Math.min(3,parseInt(button.getAttribute('data-an-category-level'),10)||1));syncCategoryLevelButtons();renderCategoryTree();}));
  if(window.ResizeObserver&&yearAxis){new ResizeObserver(renderYearAxis).observe(yearAxis);}else{window.addEventListener('resize',renderYearAxis);}
  function renderMetrics(){const yearRange=metrics.minYear&&metrics.maxYear?metrics.minYear+' - '+metrics.maxYear:'Unknown';metricRoot.innerHTML=[card('Items',metrics.totalPapers),card('Authors',metrics.uniqueAuthors),card('Sources',metrics.uniqueSources),card('Tags',metrics.uniqueTags),card('Year Range',yearRange),card('arXiv IDs',metrics.arxivPapers),card('DOIs',metrics.doiPapers)].join('');}
  function renderYears(){const bins=data.yearBins||{},rows=Array.isArray(bins[yearBinMode])?bins[yearBinMode]:(Array.isArray(data.years)?data.years:[]),root=yearRoot,max=Math.max(1,...rows.map(r=>r.count||0));if(!rows.length){root.innerHTML='<p class="an-empty">No dated items.</p>';if(yearAxis)yearAxis.innerHTML='';yearAxisTicks=[];return;}let lastRegion=null;const bars=rows.slice().reverse().map(r=>{const label=r.label||r.year||'',count=r.count||0,tip=label+': '+count,pct=Math.max(2,Math.round(count/max*100)),region=r.region||'',regionStart=lastRegion&&region&&region!==lastRegion;lastRegion=region||lastRegion;return '<span class="an-year" data-range="'+escAttr(label)+'" data-count="'+escAttr(count)+'" data-region-start="'+(regionStart?'true':'false')+'" tabindex="0" aria-label="'+escAttr(tip)+'"><span class="an-year-label" title="'+escAttr(label)+'">'+esc(label)+'</span><span class="an-year-count">'+esc(count)+'</span><span class="an-year-track"><i style="--an-w:'+pct+'%"></i></span></span>';}).join('');root.innerHTML=bars;if(yearAxis)yearAxis.innerHTML='';yearAxisTicks=[];}
  function renderAllBars(){syncLimitControls();barSections.forEach(([id,rows])=>renderBars(id,rows,selectedLimit(id)));renderCategoryTree();}
  function renderBarSection(id){const section=barSections.find(([sectionId])=>sectionId===id);if(section)renderBars(section[0],section[1],selectedLimit(id));}
  function selectedLimit(id){const section=barSections.find(([sectionId])=>sectionId===id),rows=section?section[1]:[],count=(Array.isArray(rows)?rows:[]).filter(r=>r&&r.count>0).length,select=limitSelects.find(el=>el.getAttribute('data-limit-for')===id);if(!select||select.closest('.an-card-limit')?.hidden||count<HIDE_LIMIT_BELOW)return Math.min(count,MAX_BAR_ROWS);return Math.min(parseInt(select.value,10)||5,MAX_BAR_ROWS);}
  function syncLimitControls(){limitSelects.forEach(select=>{const id=select.getAttribute('data-limit-for'),section=barSections.find(([sectionId])=>sectionId===id),count=(Array.isArray(section&&section[1])?section[1]:[]).filter(r=>r&&r.count>0).length,label=select.closest('.an-card-limit');if(label)label.hidden=count<HIDE_LIMIT_BELOW;});}
  function syncCategoryLevelButtons(){categoryLevelButtons.forEach(button=>button.setAttribute('aria-pressed',String((parseInt(button.getAttribute('data-an-category-level'),10)||1)===categoryLevel)));}
  function renderCategoryTree(){const root=document.getElementById('an-super-categories'),rows=Array.isArray(data.categoryTree)?data.categoryTree:[],flat=categoryRowsForLevel(rows,categoryLevel).sort(categoryRowSort),max=Math.max(1,...flat.map(r=>r&&r.count||0));if(!root)return;syncCategoryLevelButtons();if(!flat.length){root.innerHTML='<p class="an-empty">No categories.</p>';return;}root.innerHTML=flat.map(row=>renderCategoryRow(row,max)).join('');}
  function categoryRowsForLevel(rows,level){const target=Math.max(1,Math.min(3,level||1)),flat=[];walkCategoryRows(rows,1,[],target,flat);return flat;}
  function walkCategoryRows(rows,depth,path,target,flat){(Array.isArray(rows)?rows:[]).filter(row=>row&&row.count>0).forEach(row=>{const children=(Array.isArray(row.children)?row.children:[]).filter(child=>child&&child.count>0),nextPath=path.concat(row.label),terminal=!children.length;if(depth>=target||terminal){flat.push(Object.assign({},row,{pathLabel:nextPath.join(' / ')}));return;}walkCategoryRows(children,depth+1,nextPath,target,flat);});}
  function categoryRowSort(a,b){return (b.count||0)-(a.count||0)||String(a.pathLabel||a.label||'').localeCompare(String(b.pathLabel||b.label||''));}
  function renderCategoryRow(row,max){const pct=Math.max(2,Math.round((row.count||0)/max*100)),path=row.pathLabel&&row.pathLabel!==row.label?'<span class="an-category-path" title="'+escAttr(row.pathLabel)+'">'+esc(row.pathLabel)+'</span>':'';return '<div class="an-category-row"><span class="an-category-label" title="'+escAttr(row.label)+'">'+esc(row.label)+path+'</span><span class="an-category-track"><span class="an-category-fill" style="--an-w:'+pct+'%"></span></span><span class="an-category-count">'+esc(row.count)+'</span></div>';}
  function renderBars(id,rows,limit){const root=document.getElementById(id),allItems=(Array.isArray(rows)?rows:[]).filter(r=>r&&r.count>0),visibleItems=allItems.slice(0,Math.min(limit,MAX_BAR_ROWS)),max=Math.max(1,...visibleItems.map(r=>r.count));if(!allItems.length){root.innerHTML='<p class="an-empty">No data.</p>';return;}const bars=visibleItems.map(r=>'<div class="an-bar"><span class="an-bar-label" title="'+escAttr(r.label)+'">'+esc(r.label)+'</span><span class="an-bar-track"><span class="an-bar-fill" style="--an-w:'+Math.round(r.count/max*100)+'%"></span></span><span class="an-bar-count">'+esc(r.count)+'</span></div>').join('');const hidden=allItems.length-visibleItems.length,canShowMore=hidden>0&&visibleItems.length<MAX_BAR_ROWS;root.innerHTML=bars+(canShowMore?'<button class="an-more" type="button" data-more-for="'+escAttr(id)+'" aria-label="Show more '+escAttr(id.replace(/^an-/,'').replace(/-/g,' '))+'">'+esc(plural(hidden,'more item'))+' not displayed</button>':hidden>0?'<p class="an-more-note">'+esc(plural(hidden,'more item'))+' hidden by 100-row cap</p>':'');}
  function showMoreBars(id){const select=limitSelects.find(el=>el.getAttribute('data-limit-for')===id);if(!select)return;const current=selectedLimit(id),options=Array.from(select.options),next=options.find(option=>(parseInt(option.value,10)||0)>current);if(!next)return;select.value=next.value;renderBarSection(id);select.focus({preventScroll:true});}
  function showYearTooltip(bin){if(!yearTooltip)return;const range=bin.getAttribute('data-range')||'',count=bin.getAttribute('data-count')||'0';yearTooltip.innerHTML=esc(range)+'<span>'+esc(plural(parseInt(count,10)||0,'item'))+'</span>';yearTooltip.hidden=false;yearTooltip.classList.add('is-visible');positionYearTooltipForBar(bin);}
  function showYearTouchTooltip(bin,touch){if(!yearTooltip||!bin||!touch)return;const range=bin.getAttribute('data-range')||'',count=bin.getAttribute('data-count')||'0';yearTooltip.innerHTML=esc(range)+'<span>'+esc(plural(parseInt(count,10)||0,'item'))+'</span>';yearTooltip.hidden=false;yearTooltip.classList.add('is-visible');positionYearTooltip(touch.clientX,touch.clientY);}
  function hideYearTooltip(){if(!yearTooltip)return;yearTooltip.classList.remove('is-visible');yearTooltip.hidden=true;}
  function positionYearTooltip(x,y,side,bounds,avoid){if(!yearTooltip||yearTooltip.hidden)return;const pad=8,gap=8,box=bounds||{left:0,right:window.innerWidth,top:0,bottom:window.innerHeight},w=yearTooltip.offsetWidth||0,h=yearTooltip.offsetHeight||0;if(side==='right'){const minLeft=box.left+pad,maxRight=box.right-pad,placeLeft=x+gap+w>maxRight,left=placeLeft?Math.min(Math.max(x-gap,minLeft+w),maxRight):Math.min(Math.max(x+gap,minLeft),Math.max(minLeft,maxRight-w)),visualLeft=placeLeft?left-w:left,anchor=avoid||{},candidates=[(anchor.bottom||y)+gap,(anchor.rowTop||y)-gap-h,(anchor.top||y)-gap-h,y-h/2].map(top=>clampTooltipTop(top,box,h,pad));let top=candidates[0],best=Infinity;(candidates.length?candidates:[top]).forEach(candidate=>{const score=tooltipCollisionScore(visualLeft,candidate,w,h,anchor.rects||[]);if(score<best){best=score;top=candidate;}});yearTooltip.style.left=left+'px';yearTooltip.style.top=top+'px';yearTooltip.style.transform=placeLeft?'translate(-100%,0)':'translate(0,0)';return;}const topMin=box.top+pad+h/2,topMax=box.bottom-pad-h/2,top=topMin<=topMax?Math.min(Math.max(y,topMin),topMax):y;yearTooltip.style.left=Math.min(Math.max(x,box.left+pad),box.right-pad)+'px';yearTooltip.style.top=top+'px';yearTooltip.style.transform='translate(-50%,calc(-100% - .55rem))';}
  function positionYearTooltipForBar(bin){const anchor=bin.querySelector('.an-year-track i')||bin.querySelector('.an-year-track')||bin,rect=anchor.getBoundingClientRect(),bounds=yearRoot.getBoundingClientRect(),row=bin.getBoundingClientRect();positionYearTooltip(rect.right,rect.top+rect.height/2,'right',bounds,{top:rect.top,bottom:rect.bottom,rowTop:row.top,rects:yearLabelRects()});}
  function yearLabelRects(){return Array.from(yearRoot.querySelectorAll('.an-year-label,.an-year-count')).map(el=>el.getBoundingClientRect()).filter(rect=>rect.width>0&&rect.height>0);}
  function clampTooltipTop(top,box,h,pad){const min=box.top+pad,max=box.bottom-pad-h;return min<=max?Math.min(Math.max(top,min),max):min;}
  function tooltipCollisionScore(left,top,w,h,rects){return rects.reduce((sum,rect)=>{const x=Math.max(0,Math.min(left+w,rect.right)-Math.max(left,rect.left)),y=Math.max(0,Math.min(top+h,rect.bottom)-Math.max(top,rect.top));return sum+x*y;},0);}
  function handleYearTouch(e){const touch=e.touches&&e.touches[0];if(!touch)return;const target=document.elementFromPoint(touch.clientX,touch.clientY),bin=target&&target.closest?target.closest('.an-year'):null;if(bin&&yearRoot.contains(bin)){showYearTouchTooltip(bin,touch);}}
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


def write_analytics_assets(analytics_data: dict[str, Any]) -> None:
    with open_generated("stylesheets/analytics.css", "w") as out:
        out.write(ANALYTICS_HOME_CSS)
        out.write("\n")

    with open_generated(ANALYTICS_DATA.published_path, "w") as out:
        out.write(ANALYTICS_DATA.js_assignment(analytics_data, separators=(",", ":")))

    with open_generated("javascripts/analytics.js", "w") as out:
        analytics_js = ANALYTICS_JS.replace(
            "(function(){\n  const app=document.getElementById('an-app'); if(!app) return;",
            "(function(){\n  const appHtml="
            + json.dumps(ANALYTICS_APP_HTML, ensure_ascii=False)
            + ";\n  const app=document.getElementById('an-app'); if(!app) return; "
            "if(!app.firstElementChild) app.innerHTML=appHtml;",
            1,
        )
        out.write(analytics_js)
        out.write("\n")
