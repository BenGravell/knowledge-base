"""
Fast map layout preview using Plotly.

Parses map-data.js, builds an interactive node scatter plot,
writes a self-contained HTML file, and opens it in the browser.

Usage:
    python preview_map.py              # write temp HTML, open browser
    python preview_map.py --serve      # also start a local HTTP server
    python preview_map.py --port 8765  # custom port (implies --serve)
    python preview_map.py --out preview.html  # save to specific path
"""

import argparse
import colorsys
import json
import re
import sys
import tempfile
import threading
import webbrowser
from pathlib import Path

DATA_FILE = Path(__file__).parent / "map-data.js"

UNCATEGORIZED_CATEGORY = "Uncategorized"
UNCATEGORIZED_CATEGORIES = {UNCATEGORIZED_CATEGORY, "Other", None, ""}

SUPER_CATEGORY_PALETTE = [
    {"h": 213, "s": 76, "l": 42},
    {"h": 152, "s": 70, "l": 35},
    {"h": 31, "s": 82, "l": 43},
    {"h": 271, "s": 62, "l": 44},
    {"h": 334, "s": 58, "l": 44},
    {"h": 12, "s": 72, "l": 42},
    {"h": 188, "s": 72, "l": 36},
]
NODE_MARKER_DIAMETER = 7


def load_data() -> dict:
    text = DATA_FILE.read_text(encoding="utf-8").strip()
    # Strip JS wrapper: const mapData = {...};
    text = re.sub(r"^const\s+mapData\s*=\s*", "", text)
    text = text.rstrip(";").rstrip()
    return json.loads(text)


def is_uncategorized(category: str | None) -> bool:
    return category in UNCATEGORIZED_CATEGORIES


def category_super_category(data: dict, category: str) -> str:
    explicit = data.get("meta", {}).get("categorySuperCategory", {}).get(category)
    if explicit:
        return explicit

    node = next(
        (
            item for item in data.get("nodes", [])
            if item["data"].get("category") == category
            and item["data"].get("super_category")
        ),
        None,
    )
    return node["data"]["super_category"] if node else category


def category_order(data: dict) -> list[str]:
    configured = data.get("meta", {}).get("categoryOrder") or []
    data_categories = {
        item["data"].get("category")
        for item in data.get("nodes", [])
        if item["data"].get("category")
    }
    ordered = [cat for cat in configured if cat in data_categories]
    ordered.extend(sorted(data_categories - set(ordered)))
    return ordered


def super_category_order(data: dict) -> list[str]:
    ordered = list(data.get("meta", {}).get("superCategoryOrder") or [])
    for category in category_order(data):
        if is_uncategorized(category):
            continue
        super_category = category_super_category(data, category)
        if super_category and super_category not in ordered:
            ordered.append(super_category)
    return ordered


def super_category_hsl(data: dict, super_category: str) -> dict[str, float]:
    order = super_category_order(data)
    index = max(order.index(super_category), 0) if super_category in order else 0
    palette_index = index % len(SUPER_CATEGORY_PALETTE)
    cycle = index // len(SUPER_CATEGORY_PALETTE)
    base = SUPER_CATEGORY_PALETTE[palette_index]

    return {
        "h": normalize_hue(base["h"] + cycle * 19),
        "s": base["s"],
        "l": base["l"],
    }


def categories_for_super(data: dict, super_category: str, current_category: str) -> list[str]:
    siblings = [
        cat for cat in category_order(data)
        if category_super_category(data, cat) == super_category
    ]
    if current_category not in siblings:
        siblings.append(current_category)
    return siblings


def clamp(value: float, lo: float, hi: float) -> float:
    return min(max(value, lo), hi)


def normalize_hue(hue: float) -> float:
    return hue % 360


def hsl_to_hex(hsl: dict[str, float]) -> str:
    r, g, b = colorsys.hls_to_rgb(
        normalize_hue(hsl["h"]) / 360,
        clamp(hsl["l"], 0, 100) / 100,
        clamp(hsl["s"], 0, 100) / 100,
    )
    return "#{:02X}{:02X}{:02X}".format(
        round(r * 255),
        round(g * 255),
        round(b * 255),
    )


def category_hsl(data: dict, category: str) -> dict[str, float]:
    super_category = category_super_category(data, category)
    base = super_category_hsl(data, super_category)
    siblings = categories_for_super(data, super_category, category)
    index = max(siblings.index(category), 0)
    center = (len(siblings) - 1) / 2
    hue_step = min(7, 18 / (len(siblings) - 1)) if len(siblings) > 1 else 0

    return {
        "h": normalize_hue(base["h"] + (index - center) * hue_step),
        "s": clamp(base["s"] + (2 if index % 2 == 0 else -2), 48, 86),
        "l": clamp(base["l"] + (index - center) * 2.2, 32, 58),
    }


def sub_category_hsl(data: dict, category: str, sub_category: str) -> dict[str, float]:
    base = category_hsl(data, category)
    ordered = [
        item for item in data.get("meta", {}).get("subCategoryOrder", {}).get(category, [])
        if item
    ]
    siblings = ordered if sub_category in ordered else sorted(ordered + [sub_category])
    index = max(siblings.index(sub_category), 0)
    center = (len(siblings) - 1) / 2
    hue_step = min(4, 14 / (len(siblings) - 1)) if len(siblings) > 1 else 0

    return {
        "h": normalize_hue(base["h"] + (index - center) * hue_step),
        "s": clamp(base["s"] + (3 if index % 2 == 0 else -3), 45, 88),
        "l": clamp(base["l"] + (index - center) * 1.5 + (1 if index % 2 == 0 else -1), 32, 60),
    }


def node_color(data: dict, category: str, sub_category: str | None = None) -> str:
    if is_uncategorized(category):
        return "#000000"
    if sub_category:
        return hsl_to_hex(sub_category_hsl(data, category, sub_category))
    return hsl_to_hex(category_hsl(data, category))


def ordered_groups(data: dict, nodes: list[dict]) -> list[tuple[tuple[str, str | None], list[dict]]]:
    groups: dict[tuple[str, str | None], list[dict]] = {}
    for node in nodes:
        attrs = node["data"]
        key = (attrs["category"], attrs.get("sub_category"))
        groups.setdefault(key, []).append(node)

    data_categories = {key[0] for key in groups}
    categories = [cat for cat in category_order(data) if cat in data_categories]
    categories.extend(sorted(data_categories - set(categories)))

    ordered: list[tuple[tuple[str, str | None], list[dict]]] = []
    for category in categories:
        sub_order = data.get("meta", {}).get("subCategoryOrder", {}).get(category, [])
        data_sub_categories = {
            key[1] for key in groups
            if key[0] == category and key[1] is not None
        }
        sub_categories = [sub for sub in sub_order if sub in data_sub_categories]
        sub_categories.extend(sorted(data_sub_categories - set(sub_categories)))

        for sub_category in sub_categories:
            key = (category, sub_category)
            ordered.append((key, groups[key]))

        orphan_key = (category, None)
        if orphan_key in groups:
            ordered.append((orphan_key, groups[orphan_key]))

    return ordered


def build_figure(data: dict):
    try:
        import plotly.graph_objects as go
    except ImportError:
        sys.exit("plotly not installed — run: pip install plotly")

    nodes = data["nodes"]
    traces = []

    # One node scatter per category/sub-category so the legend is useful and
    # click-to-hide works while matching the Sigma colour palette.
    seen_legend_groups: set[str] = set()
    for (cat, sub_cat), cat_nodes in ordered_groups(data, nodes):
        xs = [n["position"]["x"] for n in cat_nodes]
        ys = [n["position"]["y"] for n in cat_nodes]
        trace_name = f"{cat} / {sub_cat}" if sub_cat else cat
        trace_super = None if is_uncategorized(cat) else category_super_category(data, cat)
        legend_group = trace_super or cat
        legend_group_title = trace_super if trace_super not in seen_legend_groups else None
        seen_legend_groups.add(legend_group)

        hover_texts = []
        for n in cat_nodes:
            d = n["data"]
            authors = d.get("authors", [])
            author_str = "Unknown"
            if authors:
                author_str = authors[0] + (" et al." if len(authors) > 1 else "")
            sub = f"<br><i>{d['sub_category']}</i>" if d.get("sub_category") else ""
            super_cat = f"{d.get('super_category')} / " if d.get("super_category") else ""
            tags = ", ".join(d.get("tags", [])[:6])
            hover_texts.append(
                f"<b>{d['title']}</b><br>"
                f"{author_str} ({d['year']})<br>"
                f"{super_cat}{d['category']}{sub}<br>"
                f"<span style='color:#aaa'>{tags}</span>"
            )

        traces.append(
            go.Scatter(
                x=xs,
                y=ys,
                mode="markers",
                name=trace_name,
                marker=dict(
                    size=NODE_MARKER_DIAMETER,
                    color=node_color(data, cat, sub_cat),
                    line=dict(width=0.8, color="rgba(255,255,255,0.35)"),
                    opacity=0.9,
                ),
                text=hover_texts,
                hovertemplate="%{text}<extra></extra>",
                legendgroup=legend_group,
                legendgrouptitle_text=legend_group_title,
            )
        )

    meta = data.get("meta", {})
    n_nodes = len(nodes)
    model = meta.get("model", "")

    fig = go.Figure(traces)
    fig.update_layout(
        title=dict(
            text=f"Knowledge Base Map — {n_nodes} papers · {model}",
            font=dict(size=13, color="#8b949e"),
            x=0.5,
            xanchor="center",
        ),
        hovermode="closest",
        plot_bgcolor="#0d1117",
        paper_bgcolor="#0d1117",
        font=dict(color="#c9d1d9", family="system-ui, sans-serif"),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, showline=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, showline=False, scaleanchor="x", autorange="reversed"),
        margin=dict(l=10, r=10, t=50, b=10),
        height=920,
        legend=dict(
            bgcolor="rgba(13,17,23,0.85)",
            bordercolor="#30363d",
            borderwidth=1,
            font=dict(size=11),
            itemclick="toggle",
            itemdoubleclick="toggleothers",
        ),
        dragmode="pan",
    )
    return fig


def main():
    parser = argparse.ArgumentParser(
        description="Fast Plotly preview of the knowledge-base map"
    )
    parser.add_argument("--serve", action="store_true", help="Start a local HTTP server")
    parser.add_argument("--port", type=int, default=8765, metavar="PORT")
    parser.add_argument("--out", type=str, metavar="FILE", help="Save HTML to this path")
    args = parser.parse_args()

    if args.port != 8765:
        args.serve = True

    print(f"Parsing {DATA_FILE.name} …")
    data = load_data()
    n_nodes = len(data["nodes"])

    print(f"Building Plotly layout preview ({n_nodes} nodes) …")
    fig = build_figure(data)

    if args.out:
        out_path = Path(args.out)
    else:
        tmp = tempfile.NamedTemporaryFile(suffix=".html", prefix="map_", delete=False)
        out_path = Path(tmp.name)
        tmp.close()

    print("Writing HTML (CDN-linked plotly.js) …")
    fig.write_html(
        str(out_path),
        include_plotlyjs="cdn",
        full_html=True,
        config={
            "scrollZoom": True,
            "displayModeBar": True,
            "modeBarButtonsToRemove": ["select2d", "lasso2d"],
            "toImageButtonOptions": {"format": "svg", "filename": "map"},
        },
    )

    if args.serve:
        import os
        from http.server import HTTPServer, SimpleHTTPRequestHandler

        os.chdir(out_path.parent)

        class QuietHandler(SimpleHTTPRequestHandler):
            def log_message(self, *_):
                pass

        server = HTTPServer(("localhost", args.port), QuietHandler)
        url = f"http://localhost:{args.port}/{out_path.name}"
        print(f"Serving at  {url}  (Ctrl+C to stop)")
        threading.Timer(0.25, lambda: webbrowser.open(url)).start()
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")
    else:
        url = out_path.as_uri()
        print(f"Opening    {url}")
        webbrowser.open(url)


if __name__ == "__main__":
    main()
