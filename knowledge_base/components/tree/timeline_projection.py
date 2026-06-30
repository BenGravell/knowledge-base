"""Timeline generated-page and data projection."""

from __future__ import annotations

from collections import Counter
from typing import Any
from urllib.parse import quote

from knowledge_base.components.tree.model import TreeModel
from knowledge_base.components.tree.projection_common import (
    UNCATEGORIZED_CATEGORY,
    as_list,
    clean_text,
    page_url,
)
from knowledge_base.generated_assets import TIMELINE_DATA, render_app_script_tags
from knowledge_base.generated_files import open_generated


def build_timeline_nav_index(model: TreeModel) -> dict[str, dict[str, Any]]:
    index: dict[str, dict[str, Any]] = {}
    for placement in model.placements_by_paper_id.values():
        source = placement.generated_source
        path = ["Tree", *placement.nav_path]
        super_category = path[1] if len(path) > 1 else None
        category = path[2] if len(path) > 2 else super_category or UNCATEGORIZED_CATEGORY
        sub_category = path[3] if len(path) > 3 else None
        index[source] = {
            "navLabel": placement.label,
            "superCategory": super_category,
            "category": category,
            "subCategory": sub_category,
            "path": path,
            "url": page_url(source),
        }
    return index


def build_timeline_order(model: TreeModel) -> dict[str, Any]:
    order = model.order.category_order_fields()
    return {
        "superCategoryOrder": order["superCategories"],
        "categoryOrder": order["categories"],
        "categorySuperCategory": order["categorySuperCategory"],
        "subCategoryOrder": order["subCategoryOrder"],
        "navPathOrder": order["navPathOrder"],
        "maxBranchDepth": order["maxBranchDepth"],
    }


def build_timeline_data(
    model: TreeModel,
    paper_details_by_source: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    nav_index = build_timeline_nav_index(model)
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
                "path": ["Tree", UNCATEGORIZED_CATEGORY],
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
                "authorShort": clean_text(details.get("authorShort")),
                "year": year,
                "source": clean_text(details.get("sourceName")),
                "type": clean_text(details.get("type")),
                "superCategory": nav.get("superCategory") or UNCATEGORIZED_CATEGORY,
                "category": nav.get("category") or UNCATEGORIZED_CATEGORY,
                "subCategory": nav.get("subCategory"),
                "path": nav.get("path") or ["Tree", UNCATEGORIZED_CATEGORY],
                "tags": as_list(details.get("tags")),
                "abstract": clean_text(details.get("abstract")),
                "summary": clean_text(details.get("summary")),
                "url": nav.get("url") or page_url(source),
                "treeUrl": f"../tree/#paper={quote(paper_id, safe='')}",
                "mapUrl": details.get("mapUrl") or f"../map/#paper={quote(paper_id, safe='')}",
                "timelineUrl": details.get("timelineUrl") or f"../timeline/#paper={quote(paper_id, safe='')}",
                "searchUrl": details.get("searchUrl") or f"../search/?paper={quote(paper_id, safe='')}",
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
            **build_timeline_order(model),
            "totalPapers": len(papers),
            "plottedPapers": sum(year_counts.values()),
            "undatedPapers": len(papers) - sum(year_counts.values()),
            "minYear": min(years) if years else None,
            "maxYear": max(years) if years else None,
            "yearBins": build_year_bins(year_counts),
            "uncategorizedCategory": UNCATEGORIZED_CATEGORY,
        },
    }


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


TIMELINE_PAGE = r"""---
hide:
  - toc
---

<style>
body:has(#tl-app) .md-grid,body:has(#tl-app) .md-main__inner{max-width:100%!important}body:has(#tl-app) .md-content{max-width:none!important;padding:0!important}.md-content__inner:has(#tl-app){margin:0!important;padding:0!important;max-width:100%!important}body:has(#tl-app) .md-footer,.md-content__inner:has(#tl-app) h1:first-child,.md-content__inner:has(#tl-app)::before,.md-content__inner:has(#tl-app)::after{display:none!important}
.tl-page{--tl-blue:var(--kb-color-blue);--tl-teal:var(--kb-color-teal);--tl-rose:var(--kb-color-rose);--tl-gold:var(--kb-color-gold);--tl-ink:var(--md-default-fg-color);--tl-muted:var(--md-default-fg-color--light);--tl-hover-emphasis:#000;--tl-border:var(--kb-border-strong);--tl-soft-border:var(--kb-border-muted);--tl-panel:var(--kb-surface-muted);--tl-panel-strong:var(--kb-surface-tinted);--mm-border:var(--tl-border);--mm-soft-border:var(--tl-soft-border);--mm-panel:var(--tl-panel);--mm-control-height:2.12rem;--mm-settings-tile-bg:var(--kb-surface-raised);--mm-settings-tile-border:var(--kb-border-subtle);--kb-app-border:var(--tl-border);--kb-app-panel:var(--tl-panel);display:flex;flex-direction:column;gap:.85rem;margin-top:var(--kb-app-top-gap,1rem)}
[data-md-color-scheme="slate"] .tl-page{--tl-hover-emphasis:#fff;--tl-panel:var(--kb-surface-muted);--tl-panel-strong:var(--kb-surface-tinted)}
.tl-header{display:flex;align-items:start;justify-content:space-between;gap:1rem}.md-typeset .tl-header h1{margin:0;line-height:1.12}.md-typeset .tl-header p{margin:.28rem 0 0;color:var(--tl-muted);font-size:.82rem}
.tl-settings{border:1px solid var(--tl-border);border-radius:8px;background:var(--tl-panel);overflow:hidden}.tl-settings-header.kb-app-header{border:0;border-bottom:1px solid var(--tl-border);border-radius:8px 8px 0 0;background:var(--kb-app-header-bg)}.tl-settings.is-collapsed .tl-controls{display:none}.tl-settings.is-collapsed .tl-settings-header.kb-app-header{border-bottom:0;border-radius:8px}.tl-controls{display:flex;flex-wrap:wrap;gap:.65rem;align-items:end;padding:.85rem;background:var(--tl-panel)}.tl-control-group{display:grid;gap:.25rem}.tl-control-group,.tl-switch{flex:0 0 auto}.tl-category-control{flex:1 1 100%;min-width:0}.tl-control-group>span,.tl-control-group>label,.tl-switch-label{color:var(--tl-muted);font-size:.72rem;font-weight:800;letter-spacing:0;text-transform:uppercase}.tl-year-control input{box-sizing:border-box;min-height:2.35rem;border:1px solid var(--tl-border);border-radius:8px;background:var(--md-default-bg-color);color:var(--tl-ink);font:inherit}.tl-year-control>div{display:flex;align-items:center;gap:.32rem}.tl-year-control input{width:5.3rem;padding:.42rem .5rem}.tl-year-control input:focus{border-color:var(--tl-blue);outline:2px solid color-mix(in srgb,var(--tl-blue) 24%,transparent);outline-offset:1px}
.tl-icon-buttons{display:inline-flex;align-items:center;gap:.42rem;min-height:2.35rem}.tl-zoom-control{flex:1 1 13rem;min-width:12rem}.tl-detail-control{flex:0 0 auto;min-width:max-content}.tl-detail-controls{--tl-detail-button-size:2.35rem;display:grid;grid-template-columns:repeat(4,var(--tl-detail-button-size));justify-content:start;gap:4px;width:100%;max-width:100%;box-sizing:border-box}.tl-zoom-control .tl-icon-buttons{width:100%}.tl-detail-controls button,#tl-reset,.tl-icon-buttons button{min-height:2.35rem;color:var(--tl-ink);font:inherit;font-weight:700;cursor:pointer}.tl-detail-controls button{display:grid;place-items:center;min-width:0;width:var(--tl-detail-button-size);height:var(--tl-detail-button-size);max-width:100%;box-sizing:border-box;padding:5px 4px;border:1px solid var(--md-default-fg-color--lighter);border-radius:6px;background:var(--md-default-fg-color--lightest);color:var(--tl-muted);font-size:.72rem;line-height:1.1;white-space:nowrap;aspect-ratio:1}.tl-detail-controls button:hover{color:var(--tl-ink);border-color:var(--md-default-fg-color--light)}.tl-detail-controls button[aria-pressed="true"]{background:color-mix(in srgb,var(--tl-blue) 16%,var(--md-default-bg-color));border-color:var(--tl-blue);color:var(--tl-ink);font-weight:600}.tl-detail-icon{position:relative;display:grid;width:1.45rem;height:1.45rem;color:currentColor}.tl-detail-dot{display:block;width:.5rem;height:.5rem;border-radius:999px;background:currentColor;box-shadow:0 0 0 1px color-mix(in srgb,currentColor 18%,transparent)}.tl-detail-icon--die{grid-template-columns:repeat(3,1fr);grid-template-rows:repeat(3,1fr);align-items:center;justify-items:center}.tl-detail-icon--die-1 .tl-detail-dot:nth-child(1){grid-area:2/2}.tl-detail-icon--die-2 .tl-detail-dot:nth-child(1){grid-area:2/1}.tl-detail-icon--die-2 .tl-detail-dot:nth-child(2){grid-area:2/3}.tl-detail-icon--die-3 .tl-detail-dot:nth-child(1){grid-area:1/2}.tl-detail-icon--die-3 .tl-detail-dot:nth-child(2){grid-area:3/1}.tl-detail-icon--die-3 .tl-detail-dot:nth-child(3){grid-area:3/3}.tl-detail-icon--die-4 .tl-detail-dot:nth-child(1){grid-area:1/1}.tl-detail-icon--die-4 .tl-detail-dot:nth-child(2){grid-area:1/3}.tl-detail-icon--die-4 .tl-detail-dot:nth-child(3){grid-area:3/1}.tl-detail-icon--die-4 .tl-detail-dot:nth-child(4){grid-area:3/3}.tl-icon-buttons button{display:grid;place-items:center;width:2.05rem;height:2.05rem;min-width:2.05rem;min-height:2.05rem;padding:0;border:1px solid color-mix(in srgb,var(--md-default-fg-color) 12%,transparent);border-radius:999px;background:color-mix(in srgb,var(--md-default-fg-color) 7%,var(--md-default-bg-color));color:var(--tl-ink);font-size:1.3rem;font-weight:900;line-height:1;transition:border-color .16s ease,background .16s ease,color .16s ease,transform .16s ease}.tl-icon-buttons button:hover{border-color:var(--tl-blue);background:color-mix(in srgb,var(--tl-blue) 14%,var(--md-default-bg-color));transform:scale(1.04)}.tl-detail-controls button:focus-visible,.tl-icon-buttons button:focus-visible{border-color:var(--tl-blue);outline:2px solid color-mix(in srgb,var(--tl-blue) 24%,transparent);outline-offset:1px;box-shadow:0 0 0 4px color-mix(in srgb,var(--tl-blue) 10%,transparent)}.tl-zoom-control .tl-icon-buttons button span{display:block;line-height:1;transform:scale(1.02)}#tl-zoom-reset{font-size:1.15rem}.tl-zoom-control{white-space:nowrap}.tl-reset-all-control{padding-left:.78rem;margin-left:.15rem;border-left:1px solid var(--tl-border)}#tl-reset{align-self:end;padding:.48rem .85rem;border:1px solid var(--tl-border);border-radius:8px;background:var(--md-default-bg-color)}#tl-reset:hover{background:color-mix(in srgb,var(--tl-blue) 8%,transparent)}
.tl-switch{display:grid;gap:.25rem}.tl-switch-row{display:flex;align-items:center;gap:.55rem;min-height:2.35rem;padding:0 .65rem;border:1px solid var(--tl-border);border-radius:8px;background:var(--md-default-bg-color);cursor:pointer}.tl-switch-row input{position:absolute;opacity:0;pointer-events:none}.tl-switch-track{position:relative;width:2.3rem;height:1.22rem;border-radius:999px;background:color-mix(in srgb,var(--md-default-fg-color) 20%,transparent);transition:background .16s ease}.tl-switch-track::after{content:"";position:absolute;top:.16rem;left:.17rem;width:.9rem;height:.9rem;border-radius:50%;background:var(--md-default-bg-color);box-shadow:0 1px 4px color-mix(in srgb,#000 28%,transparent);transition:transform .16s ease}.tl-switch-row input:checked+.tl-switch-track{background:var(--tl-teal)}.tl-switch-row input:checked+.tl-switch-track::after{transform:translateX(1.04rem)}.tl-switch-text{font-size:.78rem;font-weight:700;color:var(--tl-ink)}
.mm-section{min-width:0;max-width:100%}
.mm-section-label{display:block;font-size:.68rem;text-transform:uppercase;letter-spacing:0;color:var(--md-default-fg-color--light);font-weight:600;margin-bottom:5px}
.mm-section--categories{flex:2 1 28rem}
.mm-bento-tile{min-width:0;min-height:0;box-sizing:border-box;padding:.56rem;border:1px solid var(--mm-soft-border);border-radius:8px;overflow:hidden}
.mm-settings-section .mm-bento-tile,.tl-settings .mm-bento-tile,.mm-bento-count{background:var(--mm-settings-tile-bg);border-color:var(--mm-settings-tile-border)}
.mm-bento-tile--categories{display:grid;grid-template-rows:auto minmax(0,1fr)}
.mm-bento-tile-head{display:flex;align-items:center;justify-content:space-between;gap:.6rem;min-width:0}
.mm-bento-tile-head .mm-section-label{margin:0 0 5px}
.mm-bento-tile-head .mm-cat-links{margin-bottom:5px;flex:0 0 auto}
.mm-cat-links{display:flex;gap:.4rem;margin-bottom:5px}
.mm-cat-links button{background:none;border:1px solid var(--md-default-fg-color--lighter);color:var(--md-default-fg-color--light);padding:1px 7px;border-radius:4px;cursor:pointer;font-size:.7rem}
.mm-cat-links button:hover{color:var(--md-default-fg-color);border-color:var(--md-default-fg-color--light)}
#mm-category-filters{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(12rem,100%),1fr));gap:3px .7rem;max-height:none;min-height:0;overflow:auto;padding-right:.25rem;scrollbar-width:thin}
.mm-cat-item{display:flex;align-items:center;gap:7px;min-width:0;cursor:pointer;padding:2px 0}
.mm-cat-item:hover .mm-cat-name{color:var(--md-default-fg-color)}
.mm-cat-dot{width:10px;height:10px;border-radius:50%;flex-shrink:0}
.mm-cat-name{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;color:var(--md-default-fg-color--light);font-size:.8rem}
.mm-cat-count{flex:0 0 auto;color:var(--md-default-fg-color--lighter);font-size:.72rem}
.mm-cat-item input[type="checkbox"]{accent-color:var(--md-accent-fg-color);margin:0;flex-shrink:0}
.mm-cat-group{margin-bottom:1px}
.mm-cat-group-header{display:flex;align-items:center;gap:5px;padding:3px 0}
.mm-cat-group-cb{flex-shrink:0;cursor:pointer;margin:0;accent-color:var(--md-accent-fg-color)}
.mm-cat-group-toggle{display:flex;align-items:center;flex:1;gap:5px;cursor:pointer;user-select:none;min-width:0}
.mm-cat-group-toggle:hover .mm-cat-group-name{color:var(--md-default-fg-color)}
.mm-cat-group-arrow{font-size:.65rem;color:var(--md-default-fg-color--lighter);flex-shrink:0;width:10px}
.mm-cat-group-toggle .mm-cat-dot{width:9px;height:9px}
.mm-cat-group-name{flex:1;min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-size:.75rem;font-weight:600;color:var(--md-default-fg-color--light);letter-spacing:0}
.mm-cat-group-items{padding-left:14px}
.mm-super-group{margin:3px 0 5px}
.mm-super-group>.mm-cat-group-header{padding-top:5px}
.mm-super-group>.mm-cat-group-header .mm-cat-group-name{color:var(--md-default-fg-color);font-size:.78rem}
.mm-super-group>.mm-cat-group-items{border-left:1px solid var(--md-default-fg-color--lightest);margin-left:5px;padding-left:12px}
.tl-workbench{display:grid;grid-template-columns:minmax(0,1fr);gap:.85rem;align-items:start}.tl-stage{min-width:0}.tl-stage{border:1px solid var(--tl-border);border-radius:8px;background:var(--tl-panel)}
.tl-modal{position:fixed;inset:var(--tl-header-h,var(--md-header-height,2.8rem)) 0 0 0;z-index:var(--kb-z-app-local-overlay,80);display:grid;place-items:center;padding:1rem;background:color-mix(in srgb,#000 48%,transparent);backdrop-filter:blur(3px)}.tl-modal[hidden]{display:none}.tl-modal-card{display:grid;grid-template-rows:auto minmax(0,1fr);width:min(48rem,calc(100vw - 1.2rem));max-height:min(82vh,calc(100vh - var(--tl-header-h,var(--md-header-height,2.8rem)) - 2rem),48rem);max-height:min(82dvh,calc(100dvh - var(--tl-header-h,var(--md-header-height,2.8rem)) - 2rem),48rem);border:1px solid var(--tl-border);border-radius:8px;background:var(--md-default-bg-color);box-shadow:0 22px 60px color-mix(in srgb,#000 34%,transparent);overflow:hidden}.tl-modal-head{display:flex;align-items:center;justify-content:space-between;gap:.75rem;padding:.82rem .95rem;border-bottom:1px solid var(--tl-border);background:var(--tl-panel)}.tl-modal-head h2{margin:0;font-size:1rem;line-height:1.25}.tl-modal-close{display:grid;place-items:center;flex:0 0 auto;width:2rem;height:2rem;border:1px solid var(--tl-border);border-radius:999px;background:var(--md-default-bg-color);color:var(--tl-ink);font:inherit;font-size:1.1rem;line-height:1;cursor:pointer}.tl-modal-close:hover{border-color:var(--tl-blue);background:color-mix(in srgb,var(--tl-blue) 8%,transparent)}.tl-modal-body{min-height:0;overflow:auto;padding:.9rem .95rem 1rem;scrollbar-width:thin}.tl-modal-body p{margin:.55rem 0 0;color:var(--tl-muted);font-size:.84rem;line-height:1.55}.tl-detail-kicker{margin-bottom:.25rem;color:var(--tl-gold);font-size:.72rem;font-weight:900}.tl-detail-title{color:var(--tl-ink)!important;font-weight:700}.tl-summary,.tl-abstract{color:var(--tl-ink)!important}.tl-modal-section-title{margin:.9rem 0 .25rem;color:var(--tl-muted);font-size:.7rem;font-weight:900;text-transform:uppercase}.tl-tags{display:flex;flex-wrap:wrap;gap:.28rem;margin-top:.72rem}.tl-tags span{padding:.16rem .42rem;border:1px solid var(--tl-soft-border);border-radius:999px;background:color-mix(in srgb,var(--tl-teal) 8%,transparent);color:var(--tl-muted);font-size:.68rem}.tl-detail-actions{display:flex;flex-wrap:wrap;gap:.42rem;margin-top:.9rem}
.tl-stage{display:flex;flex-direction:column;height:var(--tl-stage-height,62vh);min-height:0;overflow:hidden}.tl-stage-toolbar{display:flex;align-items:center;justify-content:space-between;gap:.6rem;flex:0 0 auto;min-height:2.7rem;padding:.62rem .75rem;border-bottom:1px solid var(--tl-border);color:var(--tl-muted);font-size:.8rem}#tl-status{min-width:0;max-width:100%;line-height:1.35;overflow-wrap:anywhere}#tl-selection-chip{max-width:50%;padding:.18rem .46rem;border:1px solid color-mix(in srgb,var(--tl-gold) 48%,transparent);border-radius:999px;background:color-mix(in srgb,var(--tl-gold) 11%,transparent);color:var(--tl-ink);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}.tl-svg-wrap{position:relative;flex:1 1 auto;width:100%;min-height:0;max-height:none;overflow-x:hidden;overflow-y:auto;background:var(--md-default-bg-color);scrollbar-width:thin}.tl-sticky-axis{position:sticky;top:0;left:0;right:0;height:2rem;margin-bottom:-2rem;z-index:var(--kb-z-app-sticky,8);box-sizing:border-box;overflow:hidden;background:var(--md-default-bg-color);pointer-events:none;transform:none}.tl-sticky-axis--top{border-bottom:1px solid var(--tl-soft-border)}.tl-sticky-axis--bottom{border-top:1px solid var(--tl-soft-border)}.tl-sticky-axis-tick{position:absolute;top:.28rem;left:0;transform:translateX(-50%);color:var(--tl-muted);font-size:11px;font-weight:800;line-height:1;white-space:nowrap}.tl-sticky-axis-tick::before{content:"";position:absolute;left:50%;width:1px;height:.48rem;background:color-mix(in srgb,var(--md-default-fg-color) 24%,transparent);transform:translateX(-50%)}.tl-sticky-axis--top .tl-sticky-axis-tick::before{top:1.05rem}.tl-sticky-axis--bottom .tl-sticky-axis-tick::before{bottom:1.05rem}.tl-sticky-axis-tick[data-edge="start"]{transform:translateX(0)}.tl-sticky-axis-tick[data-edge="start"]::before{left:0}.tl-sticky-axis-tick[data-edge="end"]{transform:translateX(-100%)}.tl-sticky-axis-tick[data-edge="end"]::before{left:100%}#tl-svg{display:block;width:100%;height:auto;min-width:0;max-width:100%!important;font-family:"Atkinson Hyperlegible Next","Segoe UI",sans-serif;touch-action:pan-y;user-select:none}.tl-svg-bg{fill:var(--md-default-bg-color)}.tl-grid-minor,.tl-grid-major{stroke:color-mix(in srgb,var(--md-default-fg-color) 11%,transparent);stroke-width:1}.tl-grid-major{stroke:color-mix(in srgb,var(--md-default-fg-color) 19%,transparent)}.tl-axis-line,.tl-lane-line{stroke:color-mix(in srgb,var(--md-default-fg-color) 18%,transparent);stroke-width:1}.tl-lane-line{stroke-dasharray:3 8}.tl-year-label{fill:var(--tl-muted);font-size:11px;font-weight:800;text-anchor:middle}.tl-group-label-bg{fill:var(--tl-panel);stroke:var(--tl-soft-border)}.tl-group-swatch{stroke:color-mix(in srgb,#000 20%,transparent);stroke-width:1.2}.tl-group-label{fill:var(--tl-ink);font-size:12px;font-weight:850}.tl-group-meta{fill:var(--tl-muted);font-size:10px;font-weight:700}.tl-stream{fill-opacity:.22;stroke-opacity:.55;stroke-width:1.2;vector-effect:non-scaling-stroke}.tl-paper-node{cursor:pointer;outline:none}.tl-paper-dot{stroke:transparent;stroke-width:0;vector-effect:non-scaling-stroke;transition:r .12s ease,stroke-width .12s ease,stroke .12s ease,filter .12s ease}.tl-hover-year-line{stroke:var(--tl-hover-emphasis);stroke-dasharray:6 6;stroke-width:1.4;opacity:0;pointer-events:none;transition:opacity .12s ease;vector-effect:non-scaling-stroke}.tl-paper-node:hover .tl-hover-year-line,.tl-paper-node:focus-visible .tl-hover-year-line{opacity:.9}.tl-paper-node:hover .tl-paper-dot,.tl-paper-node:focus-visible .tl-paper-dot{r:6.8px;stroke:var(--tl-hover-emphasis);stroke-width:3.2;filter:drop-shadow(0 0 4px color-mix(in srgb,var(--tl-hover-emphasis) 88%,transparent)) drop-shadow(0 0 12px color-mix(in srgb,var(--tl-hover-emphasis) 58%,transparent))}.tl-selected-label{fill:var(--tl-ink);paint-order:stroke;stroke:var(--md-default-bg-color);stroke-width:4px;font-size:12px;font-weight:900;pointer-events:none}.tl-drag-zoom{pointer-events:none}.tl-drag-band{fill:color-mix(in srgb,var(--tl-blue) 16%,transparent);stroke:color-mix(in srgb,var(--tl-blue) 68%,transparent);stroke-width:1.2}.tl-drag-edge{stroke:var(--tl-blue);stroke-width:1.4;stroke-dasharray:4 4}.tl-empty-svg{fill:var(--tl-muted);font-size:14px}.tl-empty,.tl-error{margin:0;color:var(--tl-muted)}
@media (max-width:680px){.md-content__inner:has(#tl-app){max-width:100%}.tl-header{display:grid}.tl-controls{display:grid;grid-template-columns:1fr}.tl-year-control>div{display:grid;grid-template-columns:1fr auto 1fr}.tl-year-control input{width:100%}.tl-reset-all-control{padding-top:.65rem;padding-left:0;margin-left:0;border-top:1px solid var(--tl-border);border-left:0}#tl-selection-chip{max-width:100%}.tl-stage{height:30rem}.tl-stage-toolbar{align-items:start;flex-direction:column}.tl-modal{padding:.55rem}.tl-modal-card{width:calc(100vw - 1.1rem);max-height:min(88vh,calc(100vh - var(--tl-header-h,var(--md-header-height,2.8rem)) - 1.1rem));max-height:min(88dvh,calc(100dvh - var(--tl-header-h,var(--md-header-height,2.8rem)) - 1.1rem))}}
</style>

<div id="tl-app" class="tl-page kb-app-page">
  <section id="tl-settings" class="tl-settings is-collapsed" aria-label="Timeline settings">
    <div class="tl-settings-header kb-app-header">
      <span class="kb-app-header-title">Timeline</span>
      <button id="tl-settings-toggle" class="tl-settings-toggle kb-app-header-action" type="button" aria-expanded="false" aria-controls="tl-settings-body"><span id="tl-settings-toggle-label">Show Settings</span></button>
    </div>
    <div id="tl-settings-body" class="tl-controls">
    <div class="tl-control-group tl-detail-control" aria-label="Level of Detail">
      <span>Level of Detail</span>
      <div class="tl-detail-controls" role="group" aria-label="Level of Detail">
        <button type="button" data-tl-mode="level1" aria-pressed="true" aria-label="Level of detail: Level 1" title="Level 1"><span class="tl-detail-icon tl-detail-icon--die tl-detail-icon--die-1" aria-hidden="true"><span class="tl-detail-dot"></span></span></button>
        <button type="button" data-tl-mode="level2" aria-label="Level of detail: Level 2" title="Level 2"><span class="tl-detail-icon tl-detail-icon--die tl-detail-icon--die-2" aria-hidden="true"><span class="tl-detail-dot"></span><span class="tl-detail-dot"></span></span></button>
        <button type="button" data-tl-mode="level3" aria-label="Level of detail: Level 3" title="Level 3"><span class="tl-detail-icon tl-detail-icon--die tl-detail-icon--die-3" aria-hidden="true"><span class="tl-detail-dot"></span><span class="tl-detail-dot"></span><span class="tl-detail-dot"></span></span></button>
        <button type="button" data-tl-mode="level4" aria-label="Level of detail: Level 4" title="Level 4"><span class="tl-detail-icon tl-detail-icon--die tl-detail-icon--die-4" aria-hidden="true"><span class="tl-detail-dot"></span><span class="tl-detail-dot"></span><span class="tl-detail-dot"></span><span class="tl-detail-dot"></span></span></button>
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
    <div class="tl-control-group tl-zoom-control" aria-label="Timeline zoom">
      <span>Zoom</span>
      <div class="tl-icon-buttons" role="group" aria-label="Timeline zoom">
        <button id="tl-zoom-in" type="button" title="Zoom in" aria-label="Zoom in">+</button>
        <button id="tl-zoom-out" type="button" title="Zoom out" aria-label="Zoom out">-</button>
        <button id="tl-zoom-reset" type="button" title="Reset zoom" aria-label="Reset zoom"><span aria-hidden="true">&#8634;</span></button>
      </div>
    </div>
    <div class="tl-control-group tl-reset-all-control" aria-label="Reset timeline filters">
      <span>View</span>
      <button id="tl-reset" type="button">Reset All</button>
    </div>
    <div class="mm-section mm-section--categories mm-bento-tile mm-bento-tile--categories tl-category-control" aria-label="Category filters">
      <div class="mm-bento-tile-head">
        <span class="mm-section-label">Categories</span>
        <div class="mm-cat-links">
          <button id="mm-all-cats" type="button">All</button>
          <button id="mm-no-cats" type="button">None</button>
        </div>
      </div>
      <div id="mm-category-filters"></div>
    </div>
    </div>
  </section>

  <section class="tl-workbench">
    <main class="tl-stage" aria-label="Paper timeline">
      <div class="tl-stage-toolbar" hidden>
        <div id="tl-status" hidden></div>
        <div id="tl-selection-chip" hidden></div>
      </div>
      <div id="tl-svg-wrap" class="tl-svg-wrap">
        <div id="tl-axis-top" class="tl-sticky-axis tl-sticky-axis--top" aria-hidden="true"></div>
        <svg id="tl-svg" role="img" aria-labelledby="tl-svg-title tl-svg-desc">
          <title id="tl-svg-title">Paper timeline</title>
          <desc id="tl-svg-desc">A year-driven stream timeline of knowledge-base papers grouped by tree category.</desc>
        </svg>
      </div>
    </main>
  </section>
  <div id="tl-modal" class="tl-modal" hidden>
    <article class="tl-modal-card" role="dialog" aria-modal="true" aria-labelledby="tl-modal-title">
      <header class="tl-modal-head">
        <h2 id="tl-modal-title">Paper</h2>
        <button id="tl-modal-close" class="tl-modal-close" type="button" aria-label="Close paper details">&times;</button>
      </header>
      <div id="tl-modal-body" class="tl-modal-body"></div>
    </article>
  </div>
</div>

""" + render_app_script_tags("timeline.md", "timeline") + "\n"


TIMELINE_JS = r"""'use strict';
(function(){
  const app=document.getElementById('tl-app'); if(!app) return;
  const data=window.timelineData;
  if(!data||!Array.isArray(data.papers)||!data.meta){app.innerHTML='<p class="tl-error">Timeline data is unavailable. Run <code>kb build</code> to regenerate it.</p>';return;}
  const UNCATEGORIZED=(data.meta&&data.meta.uncategorizedCategory)||'Uncategorized';
  const UNCATEGORIZED_SET=new Set([UNCATEGORIZED,'Other']);
  const PALETTE=[{h:213,s:76,l:42},{h:152,s:70,l:35},{h:31,s:82,l:43},{h:271,s:62,l:44},{h:334,s:58,l:44},{h:12,s:72,l:42},{h:188,s:72,l:36}];
  const NAV_PATH_ORDER=((data.meta||{}).navPathOrder||[]).filter(path=>Array.isArray(path)).map(path=>path.map(part=>String(part||'').trim()).filter(Boolean)).filter(path=>path.length);
  const navPathOrderIndex=new Map(NAV_PATH_ORDER.map((path,index)=>[path.join('::'),index]));
  const svg=document.getElementById('tl-svg'),svgWrap=document.getElementById('tl-svg-wrap'),stage=document.querySelector('.tl-stage'),toolbar=document.querySelector('.tl-stage-toolbar'),axisTop=document.getElementById('tl-axis-top'),status=document.getElementById('tl-status'),categoryFilters=document.getElementById('mm-category-filters'),allCats=document.getElementById('mm-all-cats'),noCats=document.getElementById('mm-no-cats'),modal=document.getElementById('tl-modal'),modalTitle=document.getElementById('tl-modal-title'),modalBody=document.getElementById('tl-modal-body'),modalClose=document.getElementById('tl-modal-close'),settings=document.getElementById('tl-settings'),settingsToggle=document.getElementById('tl-settings-toggle'),settingsToggleLabel=document.getElementById('tl-settings-toggle-label'),chip=document.getElementById('tl-selection-chip'),yearStart=document.getElementById('tl-year-start'),yearEnd=document.getElementById('tl-year-end'),reset=document.getElementById('tl-reset'),zoomIn=document.getElementById('tl-zoom-in'),zoomOut=document.getElementById('tl-zoom-out'),zoomReset=document.getElementById('tl-zoom-reset'),dotsToggle=document.getElementById('tl-show-dots'),modeButtons=Array.from(app.querySelectorAll('[data-tl-mode]'));
  syncTimelineHeaderHeight(); window.addEventListener('resize',syncTimelineHeaderHeight); if(window.visualViewport)window.visualViewport.addEventListener('resize',syncTimelineHeaderHeight);
  const hslCache=new Map(),colorCache=new Map(),subColorCache=new Map(),jitterCache=new Map(),yearBinLookup=new Map();
  const categoryOrderCache={value:null},superOrderCache={value:null};
  let activeCategories=new Set(),categoryFilterModel=null;
  const papers=data.papers.map(p=>{const y=Number.isInteger(p.year)?p.year:null;const sup=p.superCategory||UNCATEGORIZED;const cat=p.category||UNCATEGORIZED;const sub=p.subCategory||'',filterPath=paperFilterPath(p),filterKey=navPathFilterKey(filterPath);return Object.assign({},p,{year:y,superCategory:sup,category:cat,subCategory:sub,filterPath:filterPath,filterKey:filterKey,searchText:norm([p.label,p.title,p.authorShort,Array.isArray(p.authors)?p.authors.join(' '):'',y||'',sup,cat,sub,Array.isArray(p.tags)?p.tags.join(' '):'',p.summary||'',p.abstract||''].join(' '))});});
  const paperById=new Map(papers.map(p=>[p.id,p]));
  const plotted=papers.filter(p=>Number.isInteger(p.year));
  const minYear=data.meta.minYear||Math.min(...plotted.map(p=>p.year)),maxYear=data.meta.maxYear||Math.max(...plotted.map(p=>p.year)),yearBins=normalizeYearBins((data.meta||{}).yearBins,minYear,maxYear),defaultStartYear=minYear;
  const state={mode:'level1',selectedId:null,yearStart:defaultStartYear,yearEnd:maxYear,showDots:true,layout:null,dragZoom:null,renderPending:false,suppressCanvasClick:false,clearSelectionTimer:null};
  const hashId=readPaperHash(); if(hashId&&paperById.has(hashId)) state.selectedId=hashId;
  yearStart.value=state.yearStart; yearEnd.value=state.yearEnd; dotsToggle.checked=state.showDots;
  if(settings&&settingsToggle&&window.matchMedia&&window.matchMedia('(max-width: 680px)').matches){settings.classList.add('is-collapsed');settingsToggle.setAttribute('aria-expanded','false');if(settingsToggleLabel)settingsToggleLabel.textContent='Show Settings';}
  yearStart.addEventListener('change',syncYears); yearEnd.addEventListener('change',syncYears);
  dotsToggle.addEventListener('change',()=>{state.showDots=dotsToggle.checked;scheduleRender();});
  zoomIn.addEventListener('click',()=>zoomBy(.5));
  zoomOut.addEventListener('click',()=>zoomBy(2));
  zoomReset.addEventListener('click',resetZoom);
  if(allCats)allCats.addEventListener('click',()=>setAllCategoryFilters(true));
  if(noCats)noCats.addEventListener('click',()=>setAllCategoryFilters(false));
  reset.addEventListener('click',()=>{state.mode='level1';state.selectedId=null;state.showDots=true;state.dragZoom=null;dotsToggle.checked=true;setAllCategoryFilters(true,false);resetZoom(false);setHash(null);render();});
  if(settingsToggle)settingsToggle.addEventListener('click',()=>{const collapsed=!settings.classList.contains('is-collapsed');settings.classList.toggle('is-collapsed',collapsed);settingsToggle.setAttribute('aria-expanded',String(!collapsed));if(settingsToggleLabel)settingsToggleLabel.textContent=collapsed?'Show Settings':'Hide Settings';requestAnimationFrame(()=>{updateStageHeight();positionStickyAxes();});});
  if(modalClose)modalClose.addEventListener('click',closeModalSelection);
  if(modal)modal.addEventListener('click',e=>{if(e.target===modal)closeModalSelection();});
  window.addEventListener('keydown',e=>{if(e.key==='Escape'&&modal&&!modal.hidden)closeModalSelection();});
  modeButtons.forEach(button=>button.addEventListener('click',()=>{state.mode=button.getAttribute('data-tl-mode')||'level2';scheduleRender();}));
  svg.addEventListener('pointerdown',startZoomDrag);
  svg.addEventListener('pointermove',updateZoomDrag);
  svg.addEventListener('pointerup',finishZoomDrag);
  svg.addEventListener('pointercancel',cancelZoomDrag);
  svg.addEventListener('lostpointercapture',cancelZoomDrag);
  svg.addEventListener('dblclick',resetZoomFromBlank);
  svg.addEventListener('click',e=>{const target=e.target.closest('[data-paper-id]');if(target){selectPaper(target.getAttribute('data-paper-id'),true);return;}clearSelectionFromCanvas(e);});
  svg.addEventListener('keydown',e=>{if(e.key!=='Enter'&&e.key!==' ')return;const target=e.target.closest('[data-paper-id]');if(!target)return;e.preventDefault();selectPaper(target.getAttribute('data-paper-id'),true);});
  if(svgWrap)svgWrap.addEventListener('scroll',positionStickyAxes,{passive:true});
  window.addEventListener('resize',scheduleRender);
  window.addEventListener('scroll',()=>{updateStageHeight();positionStickyAxes();},{passive:true});
  window.addEventListener('popstate',()=>{const next=readPaperHash();state.selectedId=next&&paperById.has(next)?next:null;render();});
  if(window.ResizeObserver){new ResizeObserver(scheduleRender).observe(svgWrap);}
  buildCategoryFilters();
  render();
  function syncYears(){const a=clampYear(parseInt(yearStart.value,10)),b=clampYear(parseInt(yearEnd.value,10));setYearRange(a,b,true);}
  function updateYearInputs(){yearStart.value=state.yearStart;yearEnd.value=state.yearEnd;}
  function setYearRange(a,b,doRender){const start=clampYear(a),end=clampYear(b);state.yearStart=Math.min(start,end);state.yearEnd=Math.max(start,end);updateYearInputs();if(doRender!==false)scheduleRender();}
  function resetZoom(doRender){setYearRange(defaultStartYear,maxYear,doRender);}
  function zoomBy(factor){const fullSpan=maxYear-minYear+1,currentSpan=state.yearEnd-state.yearStart+1,nextSpan=clamp(Math.round(currentSpan*factor),1,fullSpan),center=(state.yearStart+state.yearEnd)/2;let start=Math.round(center-(nextSpan-1)/2),end=start+nextSpan-1;if(start<minYear){end+=minYear-start;start=minYear;}if(end>maxYear){start-=end-maxYear;end=maxYear;}setYearRange(start,end,true);}
  function clampYear(v){return Number.isFinite(v)?Math.min(Math.max(v,minYear),maxYear):minYear;}
  function selectPaper(id,push){if(!paperById.has(id))return;state.selectedId=id;if(push)setHash(id);render();const node=svg.querySelector('[data-paper-id="'+cssEscape(id)+'"]');if(node&&node.focus)node.focus({preventScroll:true});}
  function clearSelectionFromCanvas(e){if(state.suppressCanvasClick){state.suppressCanvasClick=false;return;}if(!state.selectedId||!state.layout)return;const p=svgPoint(e);if(!pointInsidePlot(p.x,p.y))return;cancelClearSelection();state.clearSelectionTimer=window.setTimeout(()=>{state.clearSelectionTimer=null;if(!state.selectedId)return;state.selectedId=null;setHash(null);render();},230);}
  function closeModalSelection(){if(!state.selectedId)return;state.selectedId=null;setHash(null);render();}
  function cancelClearSelection(){if(!state.clearSelectionTimer)return;window.clearTimeout(state.clearSelectionTimer);state.clearSelectionTimer=null;}
  function startZoomDrag(e){if(e.button!==0||!state.layout||e.target.closest('[data-paper-id]'))return;if(e.detail>=2){cancelClearSelection();return;}const p=svgPoint(e);if(!pointInsidePlot(p.x,p.y))return;state.dragZoom={pointerId:e.pointerId,startX:clamp(p.x,state.layout.margin.left,state.layout.margin.left+state.layout.innerW),endX:clamp(p.x,state.layout.margin.left,state.layout.margin.left+state.layout.innerW),moved:false};if(svg.setPointerCapture)svg.setPointerCapture(e.pointerId);}
  function updateZoomDrag(e){if(!state.dragZoom||state.dragZoom.pointerId!==e.pointerId)return;const p=svgPoint(e),left=state.layout.margin.left,right=left+state.layout.innerW,threshold=9;state.dragZoom.endX=clamp(p.x,left,right);state.dragZoom.moved=state.dragZoom.moved||Math.abs(state.dragZoom.endX-state.dragZoom.startX)>=threshold;if(!state.dragZoom.moved){clearDragZoom();return;}drawDragZoom();e.preventDefault();}
  function finishZoomDrag(e){if(!state.dragZoom||state.dragZoom.pointerId!==e.pointerId)return;updateZoomDrag(e);const drag=state.dragZoom,apply=drag.moved&&Math.abs(drag.endX-drag.startX)>=18;if(svg.releasePointerCapture)try{svg.releasePointerCapture(e.pointerId);}catch(err){}state.dragZoom=null;clearDragZoom();if(drag.moved){state.suppressCanvasClick=true;window.setTimeout(()=>{state.suppressCanvasClick=false;},0);}if(!apply)return;const a=yearForSvgX(Math.min(drag.startX,drag.endX)),b=yearForSvgX(Math.max(drag.startX,drag.endX));if(a===b)return;setYearRange(a,b,true);e.preventDefault();}
  function cancelZoomDrag(e){if(!state.dragZoom||e.pointerId!==undefined&&state.dragZoom.pointerId!==e.pointerId)return;state.dragZoom=null;clearDragZoom();}
  function resetZoomFromBlank(e){if(!state.layout||e.target.closest('[data-paper-id]'))return;const p=svgPoint(e);if(!pointInsidePlot(p.x,p.y))return;cancelClearSelection();state.dragZoom=null;clearDragZoom();resetZoom(true);e.preventDefault();}
  function pointInsidePlot(x,y){const l=state.layout;if(!l)return false;return x>=l.margin.left&&x<=l.margin.left+l.innerW&&y>=l.margin.top-22&&y<=l.bottom+12;}
  function svgPoint(e){if(svg.createSVGPoint&&svg.getScreenCTM){const pt=svg.createSVGPoint();pt.x=e.clientX;pt.y=e.clientY;const ctm=svg.getScreenCTM();if(ctm)return pt.matrixTransform(ctm.inverse());}const rect=svg.getBoundingClientRect(),viewBox=svg.viewBox.baseVal;return{x:(e.clientX-rect.left)/Math.max(1,rect.width)*viewBox.width,y:(e.clientY-rect.top)/Math.max(1,rect.height)*viewBox.height};}
  function yearForSvgX(x){const l=state.layout,start=scaleForYear(state.yearStart),end=scaleForYear(state.yearEnd,true),v=start+clamp((x-l.margin.left)/Math.max(1,l.innerW),0,1)*(end-start);return yearForScaleValue(v);}
  function yearForScaleValue(v){let nearest=minYear,nearestDist=Infinity;for(let y=minYear;y<=maxYear;y++){const left=scaleForYear(y),right=scaleForYear(y,true);if(v>=left&&v<=right)return y;const mid=(left+right)/2,dist=Math.abs(v-mid);if(dist<nearestDist){nearest=y;nearestDist=dist;}}return nearest;}
  function clearDragZoom(){svg.querySelectorAll('.tl-drag-zoom').forEach(node=>node.remove());}
  function drawDragZoom(){clearDragZoom();const drag=state.dragZoom,l=state.layout;if(!drag||!l)return;const x1=Math.min(drag.startX,drag.endX),x2=Math.max(drag.startX,drag.endX),top=l.margin.top-6,bottom=l.bottom+8,g=append(svg,'g',{class:'tl-drag-zoom'});append(g,'rect',{x:x1,y:top,width:Math.max(1,x2-x1),height:bottom-top,rx:4,class:'tl-drag-band'});append(g,'line',{x1:x1,x2:x1,y1:top,y2:bottom,class:'tl-drag-edge'});append(g,'line',{x1:x2,x2:x2,y1:top,y2:bottom,class:'tl-drag-edge'});}
  function scheduleRender(){if(state.renderPending)return;state.renderPending=true;requestAnimationFrame(()=>{state.renderPending=false;render();});}
  function updateStageHeight(){if(!stage)return;if(window.matchMedia&&window.matchMedia('(max-width: 680px)').matches){stage.style.setProperty('--tl-stage-height','30rem');return;}const rect=stage.getBoundingClientRect(),gap=12,min=Math.min(220,Math.max(140,Math.round(window.innerHeight*.22))),available=Math.floor(window.innerHeight-rect.top-gap),height=Math.max(min,available);stage.style.setProperty('--tl-stage-height',height+'px');}
  function render(){const visible=filtered(),groups=buildGroups(visible);renderStatus(visible,groups);renderDetail();updateStageHeight();renderSvg(groups);modeButtons.forEach(b=>b.setAttribute('aria-pressed',String(b.getAttribute('data-tl-mode')===state.mode)));}
  function filtered(){return plotted.filter(p=>p.year>=state.yearStart&&p.year<=state.yearEnd&&activeCategories.has(p.filterKey));}
  function buildGroups(visible){const map=new Map();visible.forEach(p=>{const d=groupDescriptor(p);if(!map.has(d.key))map.set(d.key,Object.assign({},d,{superCategory:p.superCategory,category:p.category,subCategory:p.subCategory,papers:[],yearCounts:null}));map.get(d.key).papers.push(p);});return Array.from(map.values()).sort((a,b)=>compare(a.sort,b.sort)||a.label.localeCompare(b.label));}
  function timelineLevel(){const raw=String(state.mode||'level1'),n=parseInt(raw.replace(/^\D+/,''),10);return clamp(Number.isFinite(n)?n:1,1,4);}
  function paperPathParts(p){const path=Array.isArray(p.path)?p.path.slice(1).filter(Boolean):[];if(path.length)return path;return[p.superCategory||UNCATEGORIZED,p.category].filter(Boolean);}
  function groupPathForLevel(p){const parts=paperPathParts(p);if(!parts.length)return[UNCATEGORIZED];const index=Math.min(timelineLevel()-1,parts.length-1);return parts.slice(0,index+1);}
  function sortForPath(parts){const s=parts[0]||UNCATEGORIZED,c=parts[1]||s,sub=parts[2]||'',subs=((data.meta||{}).subCategoryOrder||{})[c]||[];return[positive(superOrder().indexOf(s)),parts.length>1?positive(categoryOrder().indexOf(c)):0,parts.length>2?positive(subs.indexOf(sub)):0,parts.length];}
  function groupDescriptor(p){const level=timelineLevel(),parts=groupPathForLevel(p),label=parts[parts.length-1]||UNCATEGORIZED,pathLabel=parts.join(' / '),cat=parts[1]||p.category||label,sub=parts.length>2?parts.slice(2).join(' / '):'';return{key:'level'+level+':'+parts.join('::'),label:label,pathLabel:pathLabel,color:parts.length===1?(isUncat(label)?'#000000':superColor(label)):nodeColor(cat,sub),sort:sortForPath(parts)};}
  function renderSvg(groups){clear(svg);const wrapWidth=svgWrap?svgWrap.clientWidth:0,parentWidth=svg.parentElement?svg.parentElement.clientWidth:0,available=Math.max(320,Math.floor(wrapWidth||parentWidth||960)),compact=available<760,topLabels=available<680,level=timelineLevel(),margin={top:topLabels?54:44,right:compact?24:48,bottom:52,left:topLabels?24:(compact?204:282)},baseRowH=level>=4?(compact?58:64):level===3?(compact?62:68):level===1?(compact?84:92):(compact?70:78),density=densityStats(groups),rows=groups.map(g=>({group:g,rowH:rowHeightForGroup(g,baseRowH,density)})),innerW=Math.max(180,available-margin.left-margin.right),width=margin.left+innerW+margin.right,height=Math.max(420,margin.top+rows.reduce((sum,r)=>sum+r.rowH,0)+margin.bottom),bottom=height-margin.bottom;state.layout={margin:margin,innerW:innerW,width:width,height:height,bottom:bottom};svg.setAttribute('viewBox','0 0 '+width+' '+height);svg.setAttribute('width','100%');svg.setAttribute('height',height);append(svg,'rect',{x:0,y:0,width:width,height:height,class:'tl-svg-bg'});renderStickyAxes(drawGrid(svg,margin,width,bottom),margin,innerW);if(!groups.length){append(svg,'text',{x:margin.left,y:margin.top+70,class:'tl-empty-svg'},'No dated papers match the current filters.');drawDragZoom();return;}let top=margin.top;rows.forEach(row=>{const center=topLabels?top+Math.max(56,row.rowH*.64):top+row.rowH/2;drawGroup(svg,row.group,top,center,row.rowH,margin,innerW,topLabels,density,bottom);top+=row.rowH;});drawDragZoom();}
  function drawGrid(root,margin,width,bottom){const innerW=width-margin.left-margin.right,g=append(root,'g',{class:'tl-grid'}),bins=visibleYearBins(),ticks=responsiveYearTicks(yearBoundaryTicks(bins),margin,innerW);ticks.forEach(tick=>{const x=xForScaleValue(tick.value,margin,innerW),major=tick.kind!=='one'||tick.year%5===0,label=String(tick.year);append(g,'line',{x1:x,x2:x,y1:margin.top-18,y2:bottom,class:major?'tl-grid-major':'tl-grid-minor'});append(g,'text',{x:x,y:margin.top-24,class:'tl-year-label'},label);append(g,'text',{x:x,y:bottom+30,class:'tl-year-label'},label);});append(g,'line',{x1:margin.left,x2:width-margin.right,y1:margin.top-6,y2:margin.top-6,class:'tl-axis-line'});append(g,'line',{x1:margin.left,x2:width-margin.right,y1:bottom+8,y2:bottom+8,class:'tl-axis-line'});return ticks;}
  function renderStickyAxes(ticks,margin,innerW){if(!axisTop)return;const startX=axisXForSvgX(margin.left),endX=axisXForSvgX(margin.left+innerW),html=(ticks||[]).map(tick=>{const svgX=xForScaleValue(tick.value,margin,innerW),x=axisXForSvgX(svgX),edge=x<=startX+.5?'start':x>=endX-.5?'end':'';return '<span class="tl-sticky-axis-tick"'+(edge?' data-edge="'+edge+'"':'')+' style="left:'+x.toFixed(1)+'px">'+esc(tick.year)+'</span>';}).join('');axisTop.innerHTML=html;positionStickyAxes();}
  function axisXForSvgX(x){const vb=svg.viewBox&&svg.viewBox.baseVal,svgRect=svg.getBoundingClientRect(),wrapRect=svgWrap?svgWrap.getBoundingClientRect():svgRect,viewX=vb&&Number.isFinite(vb.x)?vb.x:0,viewW=vb&&vb.width?vb.width:(state.layout&&state.layout.width)||svgRect.width||1,scale=svgRect.width/Math.max(1e-6,viewW);return svgRect.left-wrapRect.left+(x-viewX)*scale+(svgWrap?svgWrap.scrollLeft||0:0);}
  function positionStickyAxes(){if(!axisTop)return;axisTop.style.transform='';}
  function yearBoundaryTicks(bins){if(!bins.length)return[];const ticks=[];bins.forEach((bin,i)=>{const leftYear=Math.max(bin.start,state.yearStart),next=bins[i+1];if(i===0||leftYear>ticks[ticks.length-1].year)ticks.push({year:leftYear,value:scaleForYear(leftYear),kind:bin.kind});if(next){const rightYear=Math.max(next.start,state.yearStart);ticks.push({year:rightYear,value:next.offset,kind:next.kind});}else{const rightYear=Math.min(bin.end,state.yearEnd);if(rightYear>ticks[ticks.length-1].year)ticks.push({year:rightYear,value:scaleForYear(rightYear,true),kind:bin.kind});}});return ticks.filter((tick,i,rows)=>i===0||tick.year!==rows[i-1].year||Math.abs(tick.value-rows[i-1].value)>1e-6);}
  function responsiveYearTicks(ticks,margin,innerW){if(ticks.length<2)return ticks;const minGap=42,withX=ticks.map(t=>Object.assign({x:xForScaleValue(t.value,margin,innerW),region:tickRegion(t.year)},t)),selected=[];['coarse','five','one'].forEach(region=>{const rows=withX.filter(t=>t.region===region);if(!rows.length)return;const gaps=rows.slice(1).map((t,i)=>t.x-rows[i].x).filter(g=>g>0),baseGap=gaps.length?Math.min(...gaps):innerW,step=Math.max(1,Math.ceil(minGap/baseGap));rows.forEach((tick,i)=>{if(i%step===0||i===rows.length-1)selected.push(tick);});});return withoutTickCollisions(selected.sort((a,b)=>a.x-b.x),minGap);}
  function withoutTickCollisions(ticks,minGap){let lastX=-Infinity;return ticks.filter(tick=>{if(tick.x-lastX<minGap)return false;lastX=tick.x;return true;});}
  function tickRegion(year){return year<1950?'coarse':year<2000?'five':'one';}
  function drawGroup(root,group,top,center,rowH,margin,innerW,topLabels,density,bottom){const lane=append(root,'g',{class:'tl-group','data-group-key':group.key}),labelMax=topLabels?Math.max(72,innerW-90):Math.max(44,margin.left-60);append(lane,'line',{x1:margin.left,x2:margin.left+innerW,y1:center,y2:center,class:'tl-lane-line'});if(topLabels){append(lane,'rect',{x:margin.left,y:top+6,width:innerW,height:34,rx:8,class:'tl-group-label-bg'});append(lane,'circle',{cx:margin.left+12,cy:top+23,r:5,fill:group.color,class:'tl-group-swatch'});fitSvgText(append(lane,'text',{x:margin.left+26,y:top+20,class:'tl-group-label'},group.label),group.label,labelMax);append(lane,'text',{x:margin.left+26,y:top+34,class:'tl-group-meta'},plural(group.papers.length,'paper'));}else{append(lane,'rect',{x:0,y:top+4,width:margin.left-18,height:rowH-8,rx:8,class:'tl-group-label-bg'});append(lane,'circle',{cx:18,cy:center,r:5,fill:group.color,class:'tl-group-swatch'});fitSvgText(append(lane,'text',{x:32,y:center-3,class:'tl-group-label'},group.label),group.label,labelMax);append(lane,'text',{x:32,y:center+14,class:'tl-group-meta'},plural(group.papers.length,'paper'));}append(lane,'path',{d:streamPath(group,center,rowH,margin,innerW,density),fill:group.color,stroke:group.color,class:'tl-stream'});if(!state.showDots)return;const byYear=groupYearCounts(group),plotLeft=margin.left,plotRight=margin.left+innerW;Array.from(byYear.keys()).sort((a,b)=>a-b).forEach(year=>{const items=byYear.get(year).items.sort((a,b)=>a.label.localeCompare(b.label)),count=items.length,range=jitterRangeForYear(year,count,innerW,density),topLimit=top+(topLabels?44:14),bottomLimit=top+rowH-14,yRadius=densityRadius(count,rowH,topLimit,bottomLimit,density),dotRadius=dotRadiusForCount(count);items.forEach(p=>{const jitter=timelineJitter(group.key,year,p.id),x=xForYear(year,margin,innerW,jitter.x*range),y=clamp(center+jitter.y*yRadius,topLimit,bottomLimit),r=dotRadius||4.4;if(x-r<plotLeft||x+r>plotRight)return;drawPaper(lane,p,x,y,group.color,dotRadius,margin.top-14,bottom);});});}
  function fitSvgText(el,text,maxWidth){const value=String(text||'');el.textContent=value;if(!value||safeTextLength(el)<=maxWidth)return;const suffix='...';let lo=0,hi=value.length,best=suffix;while(lo<=hi){const mid=Math.floor((lo+hi)/2),next=value.slice(0,mid).trimEnd()+suffix;el.textContent=next;if(safeTextLength(el)<=maxWidth){best=next;lo=mid+1;}else{hi=mid-1;}}el.textContent=best;}
  function safeTextLength(el){return typeof el.getComputedTextLength==='function'?el.getComputedTextLength():el.textContent.length*7;}
  function streamPath(group,center,rowH,margin,innerW,density){const counts=groupYearCounts(group),samples=[],minH=3.2,maxH=Math.max(minH,Math.min(rowH*.32,rowH/2-18)),pushSample=(year,h,endEdge)=>{const x=xForScaleValue(scaleForYear(year,endEdge),margin,innerW),last=samples[samples.length-1];if(last&&Math.abs(last.x-x)<.35){last.top=Math.min(last.top,center-h);last.bottom=Math.max(last.bottom,center+h);return;}samples.push({x:x,top:center-h,bottom:center+h});};streamSampleYears().forEach(year=>{const v=streamDensityAtYear(counts,year),h=minH+Math.pow(scaledStreamDensity(v,density),.86)*(maxH-minH);pushSample(year,h,false);});if(state.yearEnd>=state.yearStart){const endV=streamDensityAtYear(counts,state.yearEnd),endH=minH+Math.pow(scaledStreamDensity(endV,density),.86)*(maxH-minH);pushSample(state.yearEnd,endH,true);}if(!samples.length)samples.push({x:margin.left,top:center-3,bottom:center+3},{x:margin.left+innerW,top:center-3,bottom:center+3});return 'M '+samples.map(p=>p.x.toFixed(1)+' '+p.top.toFixed(1)).join(' L ')+' L '+samples.slice().reverse().map(p=>p.x.toFixed(1)+' '+p.bottom.toFixed(1)).join(' L ')+' Z';}
  function drawPaper(root,p,x,y,color,radius,guideTop,guideBottom){const g=append(root,'g',{class:'tl-paper-node','data-paper-id':p.id,tabindex:0,role:'button','aria-label':p.label+', '+p.year});append(g,'line',{x1:x,x2:x,y1:guideTop,y2:guideBottom,class:'tl-hover-year-line'});append(g,'circle',{cx:x,cy:y,r:radius||4.4,fill:color,class:'tl-paper-dot'});append(g,'title',{},p.year+' - '+p.label+'\n'+p.title);}
  function xForYear(y,margin,innerW,offset){return xForScaleValue(scaleForYear(y),margin,innerW)+(offset||0);}
  function xForScaleValue(v,margin,innerW){const start=scaleForYear(state.yearStart),end=scaleForYear(state.yearEnd,true);return margin.left+((v-start)/Math.max(1e-6,end-start))*innerW;}
  function scaleForYear(year,endEdge){const y=clampYear(year),bin=yearBinFor(y);if(!bin)return y;const span=Math.max(1,bin.end-bin.start+1),pos=clamp((y-bin.start+(endEdge?1:0))/span*bin.width,0,bin.width);return bin.offset+pos;}
  function yearBinFor(year){if(yearBinLookup.has(year))return yearBinLookup.get(year);const bin=yearBins.find(b=>year>=b.start&&year<=b.end)||yearBins[yearBins.length-1];yearBinLookup.set(year,bin);return bin;}
  function visibleYearBins(){const bins=yearBins.filter(bin=>bin.end>=state.yearStart&&bin.start<=state.yearEnd);return bins.length?bins:yearBins;}
  function normalizeYearBins(raw,minY,maxY){const rows=(Array.isArray(raw)?raw:[]).filter(b=>Number.isFinite(parseInt(b.start,10))&&Number.isFinite(parseInt(b.end,10))).map(b=>({label:String(b.label||b.start),start:parseInt(b.start,10),end:parseInt(b.end,10),width:binWidth(b),kind:binKind(b)})).sort((a,b)=>a.start-b.start);const bins=rows.length?rows:[{label:String(minY),start:minY,end:maxY,width:Math.max(1,maxY-minY+1),kind:'one'}];let offset=0;bins.forEach(bin=>{bin.offset=offset;offset+=bin.width;});return bins;}
  function binWidth(row){const width=parseFloat(row&&row.width);if(Number.isFinite(width)&&width>0)return width;const start=parseInt(row&&row.start,10);return Number.isFinite(start)?(start<1950?10:start<2000?5:1):1;}
  function binKind(row){const start=parseInt(row&&row.start,10);return Number.isFinite(start)&&start<1950?'coarse':Number.isFinite(start)&&start<2000?'five':'one';}
  function groupYearCounts(groupOrItems){if(groupOrItems&&Array.isArray(groupOrItems.papers)){if(groupOrItems.yearCounts)return groupOrItems.yearCounts;groupOrItems.yearCounts=groupYearCounts(groupOrItems.papers);return groupOrItems.yearCounts;}const counts=new Map();(Array.isArray(groupOrItems)?groupOrItems:[]).forEach(p=>{if(!counts.has(p.year))counts.set(p.year,{count:0,items:[]});const row=counts.get(p.year);row.count+=1;row.items.push(p);});return counts;}
  function streamSampleYears(){const years=[];for(let year=state.yearStart;year<=state.yearEnd;year+=1)years.push(year);return years;}
  function streamDensityAtYear(counts,year){let v=0;const bandwidth=2.8;counts.forEach((row,cy)=>{const d=(year-cy)/bandwidth;v+=row.count*Math.exp(-.5*d*d);});return v;}
  function densityStats(groups){const values=[],streamValues=[],years=streamSampleYears();(groups||[]).forEach(g=>{const counts=groupYearCounts(g);counts.forEach(row=>values.push(row.count));years.forEach(year=>{const v=streamDensityAtYear(counts,year);if(v>0)streamValues.push(v);});});if(!values.length)return{min:1,max:1,logMin:Math.log1p(1),logMax:Math.log1p(1),streamMin:1,streamMax:1,streamLogMin:Math.log1p(1),streamLogMax:Math.log1p(1),absLogMax:Math.log1p(128)};const max=Math.max(1,...values),min=Math.max(1,Math.min(...values)),streamMax=Math.max(1,...streamValues),streamMin=Math.max(1,Math.min(...streamValues));return{min:min,max:max,logMin:Math.log1p(min),logMax:Math.log1p(max),streamMin:streamMin,streamMax:streamMax,streamLogMin:Math.log1p(streamMin),streamLogMax:Math.log1p(streamMax),absLogMax:Math.log1p(128)};}
  function scaledDensity(value,stats){return scaledLogDensity(value,stats&&stats.logMin,stats&&stats.logMax,stats&&stats.min,stats&&stats.max,stats&&stats.absLogMax);}
  function scaledStreamDensity(value,stats){return scaledLogDensity(value,stats&&stats.streamLogMin,stats&&stats.streamLogMax,stats&&stats.streamMin,stats&&stats.streamMax,stats&&stats.absLogMax);}
  function scaledLogDensity(value,logMin,logMax,min,max,absLogMax){const v=Math.max(0,value||0);if(v<=0)return 0;const absDenom=Math.max(1e-6,(absLogMax||Math.log1p(128))-Math.log1p(1)),absolute=clamp((Math.log1p(v)-Math.log1p(1))/absDenom,0,1);if(!Number.isFinite(max)||max<=min)return absolute;const relative=clamp((Math.log1p(v)-logMin)/Math.max(1e-6,logMax-logMin),0,1);return clamp(absolute*.35+relative*.65,0,1);}
  function rowHeightForGroup(group,baseRowH,density){const peak=maxYearCount(group),level=timelineLevel(),extraMax=level===1?104:level===2?78:56;return baseRowH+Math.round(extraMax*Math.pow(scaledDensity(peak,density),.74));}
  function densityRadius(count,rowH,topLimit,bottomLimit,density){if(count<2)return 0;const maxRadius=Math.max(0,Math.min(rowH*.28,(bottomLimit-topLimit)/2));return clamp(maxRadius*(.16+.84*Math.pow(scaledDensity(count,density),.78)),5,maxRadius);}
  function dotRadiusForCount(count){return clamp(4.7-Math.log1p(Math.max(1,count))*.35,2.7,4.4);}
  function maxYearCount(groupOrItems){const counts=groupYearCounts(groupOrItems);return Math.max(0,...Array.from(counts.values()).map(row=>row.count));}
  function timelineJitter(groupKey,year,paperId){const key=groupKey+'::'+year+'::'+paperId;if(!jitterCache.has(key))jitterCache.set(key,{x:Math.random()*2-1,y:Math.random()*2-1});return jitterCache.get(key);}
  function jitterRangeForYear(year,count,innerW,density){if(count<2)return 0;const bin=yearBinFor(year),start=scaleForYear(state.yearStart),end=scaleForYear(state.yearEnd,true),pxPerUnit=innerW/Math.max(1e-6,end-start),usable=Math.max(14,(bin?bin.width:1)*pxPerUnit*(.42+.36*scaledDensity(count,density)));return Math.min(42,usable/2);}
  function paperFilterPath(p){let path=Array.isArray(p.path)?p.path.slice():[p.superCategory,p.category,p.subCategory].filter(Boolean);path=path.map(part=>String(part||'').trim()).filter(Boolean);if(path[0]==='Tree')path.shift();const label=String(p.label||'').trim(),title=String(p.title||'').trim(),last=path[path.length-1];if(path.length>1&&(last===label||last===title))path.pop();return path.length?path:[UNCATEGORIZED];}
  function navPathFilterKey(path){return'path:'+JSON.stringify((path||[]).map(part=>String(part||'')));}
  function paddedFilterPath(path,depth){const clean=(path||[]).map(part=>String(part||'').trim()).filter(Boolean),padded=clean.length?clean.slice():[UNCATEGORIZED],fallback=padded[padded.length-1]||UNCATEGORIZED;while(padded.length<depth)padded.push(fallback);return padded.slice(0,depth);}
  function categoryFilterColor(path,index){const parts=(path||[]).slice(0,index+1);if(isUncat(parts[0]))return'#000000';if(index===0)return superColor(parts[0]);const cat=parts[1]||parts[0],sub=index>=2?parts.slice(2).join(' / '):'';return nodeColor(cat,sub);}
  function ensureCategoryFilterChild(parent,label,options){const map=parent?parent.childMap:options.rootMap;if(map.has(label)){const existing=map.get(label);existing.isCategoryLeaf=existing.isCategoryLeaf&&options.isCategoryLeaf;return existing;}const path=parent?parent.path.concat(label):[label],group={label:label,path:path,pathIndex:options.pathIndex,parent:parent,children:[],childMap:new Map(),leafIds:[],filterKeys:new Set(),color:categoryFilterColor(path,options.pathIndex),category:path[1]||path[0]||UNCATEGORIZED,subCategory:options.pathIndex>=2?path.slice(2).join(' / '):null,isCategoryLeaf:options.isCategoryLeaf};map.set(label,group);if(parent)parent.children.push(group);else options.roots.push(group);return group;}
  function accumulateCategoryFilterGroup(group,paper){group.leafIds.push(paper.id);group.filterKeys.add(paper.filterKey);}
  function categoryFilterSortKey(group){const pathKey=(group.path||[]).join('::');if(navPathOrderIndex.has(pathKey))return[navPathOrderIndex.get(pathKey),group.label];if((group.pathIndex||0)===0){const index=superOrder().indexOf(group.label);return[index<0?Number.MAX_SAFE_INTEGER:index,group.label];}if((group.pathIndex||0)===1){const index=categoryOrder().indexOf(group.category);return[index<0?Number.MAX_SAFE_INTEGER:index,group.label];}const order=((data.meta||{}).subCategoryOrder||{})[group.category]||[],index=group.subCategory?order.indexOf(group.subCategory):-1;return[index<0?Number.MAX_SAFE_INTEGER:index,group.label];}
  function sortCategoryFilterGroups(groups){groups.sort((a,b)=>{const ak=categoryFilterSortKey(a),bk=categoryFilterSortKey(b);return ak[0]-bk[0]||String(ak[1]).localeCompare(String(bk[1]));});groups.forEach(group=>sortCategoryFilterGroups(group.children));}
  function buildCategoryFilterModel(){if(categoryFilterModel)return categoryFilterModel;const roots=[],rootMap=new Map(),branchDepth=Math.max(4,Number((data.meta||{}).maxBranchDepth)||0,...plotted.map(p=>p.filterPath.length));plotted.forEach(p=>{const originalPath=p.filterPath.length?p.filterPath:[UNCATEGORIZED],path=paddedFilterPath(originalPath,branchDepth);let parent=null;for(let index=0;index<branchDepth;index+=1){const label=path[index]||path[path.length-1]||UNCATEGORIZED,group=ensureCategoryFilterChild(parent,label,{rootMap:rootMap,roots:roots,pathIndex:index,isCategoryLeaf:index>=originalPath.length});accumulateCategoryFilterGroup(group,p);parent=group;}});sortCategoryFilterGroups(roots);categoryFilterModel={roots:roots};return categoryFilterModel;}
  function makeCatItem(key,labelText,color,count,onChildChange){const label=document.createElement('label');label.className='mm-cat-item';label.innerHTML='<input type="checkbox" checked data-cat="'+escAttr(key)+'"><span class="mm-cat-dot" style="background:'+escAttr(color)+'"></span><span class="mm-cat-name">'+esc(labelText)+'</span><span class="mm-cat-count">'+esc(count)+'</span>';label.querySelector('input').addEventListener('change',e=>{if(e.target.checked)activeCategories.add(key);else activeCategories.delete(key);if(onChildChange)onChildChange();applyCategoryFilter();});return label;}
  function makeFilterGroup(name,count,color,expanded,className){const groupEl=document.createElement('div');groupEl.className=className;const header=document.createElement('div');header.className='mm-cat-group-header';const groupCb=document.createElement('input');groupCb.type='checkbox';groupCb.className='mm-cat-group-cb';groupCb.checked=true;const toggleEl=document.createElement('span');toggleEl.className='mm-cat-group-toggle';toggleEl.innerHTML='<span class="mm-cat-group-arrow">'+(expanded?'&#9662;':'&#9656;')+'</span><span class="mm-cat-dot" style="background:'+escAttr(color)+'"></span><span class="mm-cat-group-name">'+esc(name)+'</span><span class="mm-cat-count">'+esc(count)+'</span>';const itemsEl=document.createElement('div');itemsEl.className='mm-cat-group-items';itemsEl.style.display=expanded?'':'none';toggleEl.addEventListener('click',()=>{const collapsed=itemsEl.style.display==='none';itemsEl.style.display=collapsed?'':'none';toggleEl.querySelector('.mm-cat-group-arrow').textContent=collapsed?'\u25be':'\u25b8';});header.appendChild(groupCb);header.appendChild(toggleEl);groupEl.appendChild(header);groupEl.appendChild(itemsEl);return{groupEl:groupEl,groupCb:groupCb,itemsEl:itemsEl};}
  function syncGroupCheckbox(groupCb,itemsEl){const childCbs=itemsEl.querySelectorAll('input[data-cat]'),checkedCount=Array.from(childCbs).filter(cb=>cb.checked).length;groupCb.indeterminate=checkedCount>0&&checkedCount<childCbs.length;groupCb.checked=childCbs.length>0&&checkedCount===childCbs.length;}
  function syncRenderedCategoryGroups(){if(!categoryFilters)return;categoryFilters.querySelectorAll('.mm-cat-group').forEach(groupEl=>{const header=groupEl.firstElementChild,itemsEl=header?header.nextElementSibling:null,groupCb=header?header.querySelector('.mm-cat-group-cb'):null;if(groupCb&&itemsEl)syncGroupCheckbox(groupCb,itemsEl);});}
  function setLeafCheckbox(cb,checked){cb.checked=checked;if(checked)activeCategories.add(cb.dataset.cat);else activeCategories.delete(cb.dataset.cat);}
  function filterLeafKey(group){return Array.from(group.filterKeys)[0]||navPathFilterKey(group.path);}
  function renderFilterLeaf(group,onChildChange,labelOverride=null,colorOverride=null){const key=filterLeafKey(group);activeCategories.add(key);return makeCatItem(key,labelOverride||group.label,colorOverride||group.color,group.leafIds.length,onChildChange);}
  function renderFilterGroup(group,expanded,className,onChildChange){const row=makeFilterGroup(group.label,group.leafIds.length,group.color,expanded,className),groupEl=row.groupEl,groupCb=row.groupCb,itemsEl=row.itemsEl;function syncThisGroup(){syncGroupCheckbox(groupCb,itemsEl);if(onChildChange)onChildChange();}groupCb.addEventListener('change',()=>{groupCb.indeterminate=false;itemsEl.querySelectorAll('input[data-cat]').forEach(cb=>setLeafCheckbox(cb,groupCb.checked));itemsEl.querySelectorAll('.mm-cat-group-cb').forEach(cb=>{cb.checked=groupCb.checked;cb.indeterminate=false;});if(onChildChange)onChildChange();applyCategoryFilter();});(group.filterChildren||group.children).forEach(child=>{itemsEl.appendChild(renderFilterNode(child,syncThisGroup));});syncGroupCheckbox(groupCb,itemsEl);return groupEl;}
  function renderFilterNode(group,onChildChange=null){const realChildren=group.children.filter(child=>!child.isCategoryLeaf);if(!realChildren.length)return renderFilterLeaf(group,onChildChange);group.filterChildren=group.children;if(group.pathIndex===1)return renderFilterGroup(group,false,'mm-cat-group',onChildChange);return renderFilterGroup(group,false,'mm-cat-group mm-super-group',onChildChange);}
  function buildCategoryFilters(selectedKeys=null){if(!categoryFilters)return;const model=buildCategoryFilterModel(),restoredSelection=selectedKeys instanceof Set?selectedKeys:null;categoryFilters.innerHTML='';activeCategories.clear();model.roots.forEach(root=>{categoryFilters.appendChild(renderFilterNode(root));});if(restoredSelection){activeCategories.clear();categoryFilters.querySelectorAll('input[data-cat]').forEach(cb=>{setLeafCheckbox(cb,restoredSelection.has(cb.dataset.cat));});syncRenderedCategoryGroups();}}
  function setAllCategoryFilters(checked,doRender=true){if(!categoryFilters){activeCategories=new Set(checked?plotted.map(p=>p.filterKey):[]);if(doRender!==false)scheduleRender();return;}categoryFilters.querySelectorAll('input[data-cat]').forEach(cb=>setLeafCheckbox(cb,checked));categoryFilters.querySelectorAll('.mm-cat-group-cb').forEach(cb=>{cb.checked=checked;cb.indeterminate=false;});if(doRender!==false)applyCategoryFilter();}
  function applyCategoryFilter(){scheduleRender();}
  function syncTimelineHeaderHeight(){const header=document.querySelector('.md-header'),h=header?Math.max(0,Math.ceil(header.getBoundingClientRect().height)):0;if(h)document.documentElement.style.setProperty('--tl-header-h',h+'px');}
  function renderStatus(visible,groups){if(status)status.textContent='';const selected=state.selectedId?paperById.get(state.selectedId):null;if(!selected){if(toolbar)toolbar.hidden=true;chip.hidden=true;chip.textContent='';return;}if(toolbar)toolbar.hidden=false;chip.hidden=false;chip.textContent=(selected.year?selected.year+' - ':'')+selected.label;}
  function renderDetail(){const p=state.selectedId?paperById.get(state.selectedId):null;if(!modal||!modalBody||!modalTitle)return;if(!p){modal.hidden=true;modalBody.innerHTML='';modalTitle.textContent='Paper';return;}const title=p.title||p.label||'Untitled',year=p.year||'Undated',summary=p.summary||'No summary recorded yet.',abstract=p.abstract||'No abstract recorded yet.',actions=window.kbSiteLinks.renderPaperSiteLinks(p,{includeDetail:true});modalTitle.textContent=title;modalBody.innerHTML='<div class="tl-detail-kicker">'+esc(year)+'</div>'+(p.label&&p.label!==title?'<p class="tl-detail-title">'+esc(p.label)+'</p>':'')+'<div class="tl-modal-section-title">Abstract</div><p class="tl-abstract">'+esc(abstract)+'</p><div class="tl-modal-section-title">Summary</div><p class="tl-summary">'+esc(summary)+'</p><div class="tl-detail-actions paper-link-pills">'+actions+'</div>';modal.hidden=false;}
  function nodeColor(cat,sub){if(isUncat(cat))return'#000000';if(sub){const key=cat+'::'+sub;if(!subColorCache.has(key))subColorCache.set(key,hslToHex(subHsl(cat,sub)));return subColorCache.get(key);}if(!colorCache.has(cat))colorCache.set(cat,hslToHex(categoryHsl(cat)));return colorCache.get(cat);}
  function isUncat(cat){return!cat||UNCATEGORIZED_SET.has(cat);}
  function categoryHsl(cat){if(hslCache.has(cat))return hslCache.get(cat);const sup=categorySuper(cat)||cat,base=superHsl(sup),siblings=categoriesForSuper(sup,cat),i=Math.max(siblings.indexOf(cat),0),center=(siblings.length-1)/2,step=siblings.length>1?Math.min(7,18/(siblings.length-1)):0,hsl={h:normHue(base.h+(i-center)*step),s:clamp(base.s+(i%2===0?2:-2),48,86),l:clamp(base.l+(i-center)*2.2,32,58)};hslCache.set(cat,hsl);return hsl;}
  function subHsl(cat,sub){const base=categoryHsl(cat),ordered=(((data.meta||{}).subCategoryOrder||{})[cat]||[]).filter(Boolean),siblings=ordered.includes(sub)?ordered:ordered.concat(sub).sort((a,b)=>a.localeCompare(b)),i=Math.max(siblings.indexOf(sub),0),center=(siblings.length-1)/2,step=siblings.length>1?Math.min(4,14/(siblings.length-1)):0;return{h:normHue(base.h+(i-center)*step),s:clamp(base.s+(i%2===0?3:-3),45,88),l:clamp(base.l+(i-center)*1.5+(i%2===0?1:-1),32,60)};}
  function categorySuper(cat){const explicit=(((data.meta||{}).categorySuperCategory)||{})[cat];if(explicit)return explicit;const p=papers.find(x=>x.category===cat&&x.superCategory);return p?p.superCategory:null;}
  function categoryOrder(){if(categoryOrderCache.value)return categoryOrderCache.value;const configured=((data.meta||{}).categoryOrder||[]),cats=new Set(papers.map(p=>p.category).filter(Boolean)),ordered=configured.filter(c=>cats.has(c));Array.from(cats).sort((a,b)=>a.localeCompare(b)).forEach(c=>{if(!ordered.includes(c))ordered.push(c);});categoryOrderCache.value=ordered;return ordered;}
  function superOrder(){if(superOrderCache.value)return superOrderCache.value;const ordered=Array.from(((data.meta||{}).superCategoryOrder||[]));categoryOrder().forEach(c=>{if(isUncat(c))return;const s=categorySuper(c)||c;if(s&&!ordered.includes(s))ordered.push(s);});papers.forEach(p=>{if(p.superCategory&&!ordered.includes(p.superCategory))ordered.push(p.superCategory);});if(!ordered.includes(UNCATEGORIZED))ordered.push(UNCATEGORIZED);superOrderCache.value=ordered;return ordered;}
  function superHsl(s){const order=superOrder(),i=Math.max(order.indexOf(s),0),base=PALETTE[i%PALETTE.length],cycle=Math.floor(i/PALETTE.length);return{h:normHue(base.h+cycle*19),s:base.s,l:base.l};}
  function superColor(s){return hslToHex(superHsl(s));}
  function categoriesForSuper(s,current){const siblings=categoryOrder().filter(c=>(categorySuper(c)||c)===s);if(!siblings.includes(current))siblings.push(current);return siblings;}
  function hslToHex(o){const h=o.h/360,s=o.s/100,l=o.l/100,fn=(p,q,t)=>{if(t<0)t+=1;if(t>1)t-=1;if(t<1/6)return p+(q-p)*6*t;if(t<1/2)return q;if(t<2/3)return p+(q-p)*(2/3-t)*6;return p;};let r,g,b;if(s===0){r=g=b=l;}else{const q=l<.5?l*(1+s):l+s-l*s,p=2*l-q;r=fn(p,q,h+1/3);g=fn(p,q,h);b=fn(p,q,h-1/3);}const hex=v=>Math.round(v*255).toString(16).padStart(2,'0');return'#'+hex(r)+hex(g)+hex(b);}
  function compare(a,b){for(let i=0;i<Math.max(a.length,b.length);i++){const d=(a[i]||0)-(b[i]||0);if(d!==0)return d;}return 0;}function positive(i){return i>=0?i:9999;}function clamp(v,min,max){return Math.min(Math.max(v,min),max);}function normHue(h){return((h%360)+360)%360;}function plural(n,s,p){return n+' '+(n===1?s:(p||s+'s'));}function norm(v){return String(v||'').toLowerCase().normalize('NFKD').replace(/[\u0300-\u036f]/g,'');}
  function readPaperHash(){const query=new URLSearchParams(window.location.search),queryId=query.get('paper')||query.get('tl');if(queryId)return queryId;const hash=window.location.hash.slice(1);if(!hash)return null;const params=new URLSearchParams(hash);return params.get('paper')||params.get('tl');}
  function setHash(id){const url=new URL(window.location.href);url.hash=id?'paper='+encodeURIComponent(id):'';window.history.pushState(null,'',url);}
  function append(parent,tag,attrs,text){const el=document.createElementNS('http://www.w3.org/2000/svg',tag);Object.keys(attrs||{}).forEach(k=>el.setAttribute(k,attrs[k]));if(text!==undefined)el.textContent=text;parent.appendChild(el);return el;}
  function clear(node){while(node.firstChild)node.removeChild(node.firstChild);}
  function esc(v){return String(v||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;').replace(/'/g,'&#39;');}
  function escAttr(v){return esc(v).replace(/`/g,'&#96;');}
  function cssEscape(v){return window.CSS&&typeof window.CSS.escape==='function'?window.CSS.escape(v):String(v).replace(/"/g,'\\"');}
})();"""


def write_timeline_assets(timeline_data: dict[str, Any]) -> None:
    with open_generated("timeline.md", "w") as out:
        out.write(TIMELINE_PAGE)

    with open_generated(TIMELINE_DATA.published_path, "w") as out:
        out.write(TIMELINE_DATA.js_assignment(timeline_data, separators=(",", ":")))

    with open_generated("javascripts/timeline.js", "w") as out:
        out.write(TIMELINE_JS)
        out.write("\n")
