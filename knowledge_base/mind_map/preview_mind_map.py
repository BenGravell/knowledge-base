"""
Fast mind-map graph preview using Plotly.

Parses mind-map-data.js, builds an interactive scatter/network graph,
writes a self-contained HTML file, and opens it in the browser.

Usage:
    python preview_mind_map.py              # write temp HTML, open browser
    python preview_mind_map.py --serve      # also start a local HTTP server
    python preview_mind_map.py --port 8765  # custom port (implies --serve)
    python preview_mind_map.py --out preview.html  # save to specific path
"""

import argparse
import json
import re
import sys
import tempfile
import threading
import webbrowser
from pathlib import Path

DATA_FILE = Path(__file__).parent / "mind-map-data.js"

# Material Design 800-weight palette (matches existing Cytoscape viz)
_PALETTE = [
    "#AD1457", "#6A1B9A", "#283593", "#1565C0", "#00695C",
    "#2E7D32", "#558B2F", "#F57F17", "#E65100", "#BF360C",
    "#4E342E", "#37474F", "#00838F", "#0277BD", "#4527A0",
    "#00796B", "#827717", "#6D4C41", "#546E7A", "#C62828",
]


def load_data() -> dict:
    text = DATA_FILE.read_text(encoding="utf-8").strip()
    # Strip JS wrapper: const mindMapData = {...};
    text = re.sub(r"^const\s+mindMapData\s*=\s*", "", text)
    text = text.rstrip(";").rstrip()
    return json.loads(text)


def build_figure(data: dict):
    try:
        import plotly.graph_objects as go
    except ImportError:
        sys.exit("plotly not installed — run: pip install plotly")

    nodes = data["nodes"]
    edges = data["edges"]

    # Position lookup: id -> (x, y)  — position is a sibling of data, not nested inside it
    pos = {
        n["data"]["id"]: (n["position"]["x"], n["position"]["y"])
        for n in nodes
    }

    categories = sorted({n["data"]["category"] for n in nodes})
    cat_color = {cat: _PALETTE[i % len(_PALETTE)] for i, cat in enumerate(categories)}

    # Single edge trace — all edges as one scatter with None separators (fastest)
    ex, ey = [], []
    for e in edges:
        src, tgt = e["data"]["source"], e["data"]["target"]
        if src in pos and tgt in pos:
            x0, y0 = pos[src]
            x1, y1 = pos[tgt]
            ex += [x0, x1, None]
            ey += [y0, y1, None]

    traces = [
        go.Scatter(
            x=ex,
            y=ey,
            mode="lines",
            line=dict(width=0.6, color="rgba(180,180,200,0.15)"),
            hoverinfo="none",
            showlegend=False,
        )
    ]

    # One node scatter per category so the legend is useful and click-to-hide works
    for cat in categories:
        cat_nodes = [n for n in nodes if n["data"]["category"] == cat]
        xs = [n["position"]["x"] for n in cat_nodes]
        ys = [n["position"]["y"] for n in cat_nodes]

        hover_texts = []
        for n in cat_nodes:
            d = n["data"]
            authors = d.get("authors", [])
            author_str = ", ".join(authors[:3]) + (" et al." if len(authors) > 3 else "")
            sub = f"<br><i>{d['sub_category']}</i>" if d.get("sub_category") else ""
            tags = ", ".join(d.get("tags", [])[:6])
            hover_texts.append(
                f"<b>{d['title']}</b><br>"
                f"{author_str} ({d['year']})<br>"
                f"{d['category']}{sub}<br>"
                f"<span style='color:#aaa'>{tags}</span>"
            )

        traces.append(
            go.Scatter(
                x=xs,
                y=ys,
                mode="markers",
                name=cat,
                marker=dict(
                    size=7,
                    color=cat_color[cat],
                    line=dict(width=0.8, color="rgba(255,255,255,0.35)"),
                    opacity=0.9,
                ),
                text=hover_texts,
                hovertemplate="%{text}<extra></extra>",
            )
        )

    meta = data.get("meta", {})
    n_nodes = len(nodes)
    n_edges = len(edges)
    model = meta.get("model", "")

    fig = go.Figure(traces)
    fig.update_layout(
        title=dict(
            text=f"Knowledge Base Mind Map — {n_nodes} papers · {n_edges} edges · {model}",
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
        description="Fast Plotly preview of the knowledge-base mind map"
    )
    parser.add_argument("--serve", action="store_true", help="Start a local HTTP server")
    parser.add_argument("--port", type=int, default=8765, metavar="PORT")
    parser.add_argument("--out", type=str, metavar="FILE", help="Save HTML to this path")
    args = parser.parse_args()

    if args.port != 8765:
        args.serve = True

    print(f"Parsing {DATA_FILE.name} …")
    data = load_data()
    n_nodes, n_edges = len(data["nodes"]), len(data["edges"])

    print(f"Building Plotly graph ({n_nodes} nodes, {n_edges} edges) …")
    fig = build_figure(data)

    if args.out:
        out_path = Path(args.out)
    else:
        tmp = tempfile.NamedTemporaryFile(suffix=".html", prefix="mind_map_", delete=False)
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
            "toImageButtonOptions": {"format": "svg", "filename": "mind_map"},
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
