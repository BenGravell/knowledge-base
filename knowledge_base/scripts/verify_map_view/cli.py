"""Command-line entrypoint for map view verification."""

from __future__ import annotations

import argparse

from knowledge_base.scripts.verify_map_view.browser import (
    find_chrome,
    get_tab_websocket,
    launch_chrome,
    parse_viewport,
    run_viewport,
    shutdown_chrome,
)
from knowledge_base.scripts.verify_map_view.cdp import CdpClient, ChromeSession


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify the map page in headless Chrome")
    parser.add_argument("--url", required=True, help="Served Zensical map URL")
    parser.add_argument("--chrome", help="Path to Chrome/Chromium")
    parser.add_argument(
        "--viewport",
        action="append",
        default=None,
        help="Viewport to test, e.g. 1366x900 or 390x844:mobile. May be repeated.",
    )
    args = parser.parse_args()
    viewports = args.viewport or ["1366x900", "390x844:mobile"]

    chrome = find_chrome(args.chrome)
    session: ChromeSession | None = None
    client: CdpClient | None = None
    try:
        session = launch_chrome(chrome)
        client = CdpClient(get_tab_websocket(session, args.url))
        all_metrics = {}
        for viewport in viewports:
            width, height, mobile = parse_viewport(viewport)
            metrics = run_viewport(client, args.url, width, height, mobile)
            all_metrics[viewport] = metrics
            fitted = metrics.get("fitted", {})
            print(
                f"PASS {viewport}: "
                f"{metrics.get('nodes')} nodes, "
                f"fit bbox x=[{fitted.get('minX'):.1f}, {fitted.get('maxX'):.1f}] "
                f"y=[{fitted.get('minY'):.1f}, {fitted.get('maxY'):.1f}]"
            )
        return 0
    finally:
        if client:
            client.close()
        shutdown_chrome(session)


__all__ = ["main"]
