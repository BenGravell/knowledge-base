"""CLI for home title gradient verification."""

from __future__ import annotations

import argparse
import sys
import time
from urllib.parse import quote

from knowledge_base.scripts.verify_home_title_gradient.capture import capture_metrics
from knowledge_base.scripts.verify_home_title_gradient.fixture import html
from knowledge_base.scripts.verify_home_title_gradient.metrics import color_delta
from knowledge_base.scripts.verify_home_title_gradient.model import FailureMetrics
from knowledge_base.scripts.verify_map_view.browser import (
    find_chrome,
    get_tab_websocket,
    launch_chrome,
    shutdown_chrome,
)
from knowledge_base.scripts.verify_map_view.cdp import CdpClient


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify the animated home title gradient has no hard seam")
    parser.add_argument("--chrome", help="Path to Chrome/Chromium")
    parser.add_argument("--threshold", type=float, default=130.0, help="Maximum allowed adjacent RGB delta")
    parser.add_argument("--allowed-spikes", type=int, default=0, help="Allowed adjacent-pixel deltas above threshold")
    parser.add_argument(
        "--loop-delta-threshold", type=float, default=55.0, help="Maximum allowed first/last-frame mean RGB delta"
    )
    parser.add_argument("--frames", type=int, default=12, help="Frame offsets to sample per color scheme")
    args = parser.parse_args()

    chrome = find_chrome(args.chrome)
    session = launch_chrome(chrome)
    client: CdpClient | None = None
    try:
        client = CdpClient(get_tab_websocket(session, "home-title-gradient"))
        client.call("Page.enable")
        client.call("Runtime.enable")
        client.call(
            "Emulation.setDeviceMetricsOverride",
            {"width": 1000, "height": 180, "deviceScaleFactor": 1, "mobile": False},
        )
        client.call("Page.navigate", {"url": "data:text/html;charset=utf-8," + quote(html())})
        deadline = time.time() + 10
        while time.time() < deadline:
            if client.evaluate(
                "document.readyState === 'complete' && Boolean(document.getElementById('title'))", timeout=2
            ):
                break
            time.sleep(0.1)
        else:
            raise TimeoutError("gradient fixture did not load")

        failures: list[FailureMetrics] = []
        progress_values = [i / (args.frames - 1) for i in range(args.frames)]
        for scheme in ("default", "slate"):
            scheme_metrics = []
            for frame, progress in enumerate(progress_values):
                position = f"{200 - progress * 200:.2f}% 50.00%"
                metrics = capture_metrics(client, scheme, frame, position, args.threshold)
                scheme_metrics.append(metrics)
                print(
                    f"{scheme:7s} frame={frame:02d} pos={position:>15s} "
                    f"max_delta={metrics['max_delta']:6.2f} "
                    f"spikes={metrics['spike_pairs']:3d} "
                    f"pairs={metrics['checked_pairs']}"
                )
                if metrics["spike_pairs"] > args.allowed_spikes:
                    failures.append(
                        {
                            "scheme": metrics["scheme"],
                            "frame": metrics["frame"],
                            "position": metrics["position"],
                            "max_delta": metrics["max_delta"],
                            "spike_pairs": metrics["spike_pairs"],
                            "limit": args.threshold,
                        }
                    )
            loop_delta = color_delta(scheme_metrics[0]["mean_rgb"], scheme_metrics[-1]["mean_rgb"])
            print(f"{scheme:7s} loop_delta={loop_delta:6.2f}")
            if loop_delta > args.loop_delta_threshold:
                failures.append(
                    {
                        "scheme": scheme,
                        "frame": "loop",
                        "position": "last->first",
                        "max_delta": round(loop_delta, 2),
                        "spike_pairs": 0,
                        "limit": args.loop_delta_threshold,
                    }
                )

        if failures:
            worst = max(failures, key=lambda item: float(item["max_delta"]))
            raise AssertionError(
                "hard gradient edge detected: "
                f"{len(failures)} frame(s) exceeded limit {worst['limit']}; "
                f"worst {worst['scheme']} frame={worst['frame']} pos={worst['position']} "
                f"max_delta={worst['max_delta']} spikes={worst['spike_pairs']}"
            )
        return 0
    finally:
        if client:
            client.close()
        shutdown_chrome(session)


def run() -> int:
    try:
        return main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
