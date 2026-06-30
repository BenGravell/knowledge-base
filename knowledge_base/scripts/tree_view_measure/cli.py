"""Command-line interface for Tree performance measurement."""

from __future__ import annotations

import argparse
import json
import sys
from http.server import ThreadingHTTPServer
from pathlib import Path
from typing import Any

from knowledge_base.scripts import measure_tree_view as core
from knowledge_base.scripts.tree_view_measure.measure import run_once
from knowledge_base.scripts.tree_view_measure.server import serve_site
from knowledge_base.scripts.tree_view_measure.summary import summarize_viewport
from knowledge_base.scripts.verify_map_view.browser import (
    find_chrome,
    get_tab_websocket,
    launch_chrome,
    parse_viewport,
    shutdown_chrome,
)
from knowledge_base.scripts.verify_map_view.cdp import CdpClient


def main() -> int:
    parser = argparse.ArgumentParser(description="Measure Tree page click timing in headless Chrome")
    parser.add_argument("--url", help="Served Zensical Tree URL. Defaults to serving site/tree/ locally.")
    parser.add_argument("--site-dir", default="site", help="Built Zensical site directory used when --url is omitted.")
    parser.add_argument("--chrome", help="Path to Chrome/Chromium")
    parser.add_argument("--branch", default=core.DEFAULT_BRANCH, help="First-level branch label to click")
    parser.add_argument("--runs", type=int, default=5, help="Measured runs per viewport")
    parser.add_argument("--warmups", type=int, default=1, help="Unreported warm-up runs per viewport")
    parser.add_argument(
        "--viewport",
        action="append",
        default=None,
        help="Viewport to test, e.g. 1366x900 or 390x844:mobile. May be repeated.",
    )
    parser.add_argument(
        "--reduced-motion",
        action="store_true",
        help="Emulate prefers-reduced-motion: reduce to isolate non-animation cost.",
    )
    parser.add_argument("--json", action="store_true", help="Emit raw JSON instead of a text summary")
    args = parser.parse_args()

    if args.runs < 1:
        parser.error("--runs must be at least 1")
    if args.warmups < 0:
        parser.error("--warmups cannot be negative")

    server: ThreadingHTTPServer | None = None
    url = args.url
    if not url:
        server, url = serve_site(Path(args.site_dir))

    chrome = find_chrome(args.chrome)
    session = None
    client = None
    try:
        session = launch_chrome(chrome)
        client = CdpClient(get_tab_websocket(session, url))
        viewports = args.viewport or core.DEFAULT_VIEWPORTS
        results: dict[str, Any] = {
            "url": url,
            "branch": args.branch,
            "reducedMotion": args.reduced_motion,
            "viewports": {},
        }
        for viewport_label in viewports:
            viewport = parse_viewport(viewport_label)
            measured: list[dict[str, Any]] = []
            for index in range(args.warmups + args.runs):
                run = run_once(client, url, args.branch, viewport, index, args.reduced_motion)
                if index >= args.warmups:
                    measured.append(run)
            results["viewports"][viewport_label] = measured

        if args.json:
            print(json.dumps(results, indent=2))
        else:
            print(f"Tree timing URL: {url}")
            print(f"Scenario: default load, click {args.branch!r}")
            if args.reduced_motion:
                print("Motion: prefers-reduced-motion emulated")
            for viewport_label, runs in results["viewports"].items():
                print()
                print(summarize_viewport(viewport_label, runs))
        return 0
    finally:
        if client:
            client.close()
        shutdown_chrome(session)
        if server:
            server.shutdown()
            server.server_close()


def run() -> int:
    try:
        return main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
