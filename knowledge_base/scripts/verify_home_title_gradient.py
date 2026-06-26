"""Check the home title gradient animation for seam-like hard edges."""

from __future__ import annotations

import argparse
import base64
import math
import struct
import sys
import time
import zlib
from pathlib import Path
from typing import TypedDict
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from knowledge_base.scripts.verify_map_view import (  # noqa: E402
    CdpClient,
    find_chrome,
    get_tab_websocket,
    launch_chrome,
    shutdown_chrome,
)

Rgb = tuple[float, float, float]


class GradientMetrics(TypedDict):
    text_pixels: int
    checked_pairs: int
    max_delta: float
    mean_rgb: Rgb
    spike_pairs: int


class CaptureMetrics(GradientMetrics):
    scheme: str
    frame: int
    position: str


class FailureMetrics(TypedDict):
    scheme: str
    frame: int | str
    position: str
    max_delta: float
    spike_pairs: int
    limit: float


def png_rgba(data: bytes) -> tuple[int, int, bytes]:
    if not data.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError("screenshot is not a PNG")

    pos = 8
    width = height = color_type = None
    idat: list[bytes] = []
    while pos < len(data):
        length = struct.unpack(">I", data[pos : pos + 4])[0]
        kind = data[pos + 4 : pos + 8]
        payload = data[pos + 8 : pos + 8 + length]
        pos += 12 + length
        if kind == b"IHDR":
            width, height, bit_depth, color_type = struct.unpack(">IIBB", payload[:10])
            if bit_depth != 8 or color_type not in (2, 6):
                raise ValueError(f"unsupported PNG format: depth={bit_depth}, color={color_type}")
        elif kind == b"IDAT":
            idat.append(payload)
        elif kind == b"IEND":
            break

    if width is None or height is None or color_type is None:
        raise ValueError("PNG missing IHDR")

    channels = 4 if color_type == 6 else 3
    stride = width * channels
    raw = zlib.decompress(b"".join(idat))
    rows: list[bytes] = []
    prev = bytearray(stride)
    offset = 0
    for _ in range(height):
        filter_type = raw[offset]
        row = bytearray(raw[offset + 1 : offset + 1 + stride])
        offset += stride + 1
        for i, value in enumerate(row):
            left = row[i - channels] if i >= channels else 0
            up = prev[i]
            up_left = prev[i - channels] if i >= channels else 0
            if filter_type == 1:
                row[i] = (value + left) & 0xFF
            elif filter_type == 2:
                row[i] = (value + up) & 0xFF
            elif filter_type == 3:
                row[i] = (value + ((left + up) // 2)) & 0xFF
            elif filter_type == 4:
                p = left + up - up_left
                pa, pb, pc = abs(p - left), abs(p - up), abs(p - up_left)
                row[i] = (value + (left if pa <= pb and pa <= pc else up if pb <= pc else up_left)) & 0xFF
            elif filter_type != 0:
                raise ValueError(f"unsupported PNG filter: {filter_type}")
        prev = row
        rows.append(bytes(row))

    if channels == 4:
        return width, height, b"".join(rows)

    rgba = bytearray(width * height * 4)
    out = 0
    for row in rows:
        for i in range(0, len(row), 3):
            rgba[out : out + 4] = row[i : i + 3] + b"\xff"
            out += 4
    return width, height, bytes(rgba)


def color_delta(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b, strict=True)))


def gradient_metrics(width: int, height: int, rgba: bytes, threshold: float) -> GradientMetrics:
    raw_mask = [False] * (width * height)
    for index in range(width * height):
        base = index * 4
        rgb = (rgba[base], rgba[base + 1], rgba[base + 2])
        alpha = rgba[base + 3]
        raw_mask[index] = alpha > 245 and (max(rgb) - min(rgb)) > 12

    mask = [False] * (width * height)
    erosion = 2
    for y in range(erosion, height - erosion):
        for x in range(erosion, width - erosion):
            index = y * width + x
            mask[index] = all(
                raw_mask[(y + dy) * width + x + dx]
                for dy in range(-erosion, erosion + 1)
                for dx in range(-erosion, erosion + 1)
            )

    max_delta = 0.0
    spike_pairs = 0
    checked_pairs = 0
    text_pixels = 0
    rgb_sums = [0, 0, 0]
    for y in range(height):
        row = y * width
        for x in range(width):
            index = row + x
            if not mask[index]:
                continue
            base = index * 4
            rgb = (rgba[base], rgba[base + 1], rgba[base + 2])
            text_pixels += 1
            rgb_sums[0] += rgb[0]
            rgb_sums[1] += rgb[1]
            rgb_sums[2] += rgb[2]
            for neighbor in (index + 1 if x + 1 < width else None, index + width if y + 1 < height else None):
                if neighbor is None or not mask[neighbor]:
                    continue
                other = neighbor * 4
                delta = color_delta(rgb, (rgba[other], rgba[other + 1], rgba[other + 2]))
                checked_pairs += 1
                max_delta = max(max_delta, delta)
                if delta > threshold:
                    spike_pairs += 1

    mean_rgb: Rgb = (
        (
            round(rgb_sums[0] / text_pixels, 2),
            round(rgb_sums[1] / text_pixels, 2),
            round(rgb_sums[2] / text_pixels, 2),
        )
        if text_pixels
        else (0.0, 0.0, 0.0)
    )
    return {
        "text_pixels": text_pixels,
        "checked_pairs": checked_pairs,
        "max_delta": round(max_delta, 2),
        "mean_rgb": mean_rgb,
        "spike_pairs": spike_pairs,
    }


def html() -> str:
    css = "\n".join(
        [
            (ROOT / "knowledge_base/docs/stylesheets/extra/tokens.css").read_text(),
            (ROOT / "knowledge_base/docs/stylesheets/extra/home.css").read_text(),
            """
            :root {
              --md-default-bg-color: #ffffff;
              --md-default-fg-color: #1b1f29;
              --md-default-fg-color--light: #56616d;
              --md-code-bg-color: #f3f5f7;
              --md-primary-fg-color: #005eb8;
            }
            [data-md-color-scheme="slate"] {
              --md-default-bg-color: #1b1f29;
              --md-default-fg-color: #ffffff;
              --md-default-fg-color--light: #c7d0dc;
              --md-code-bg-color: #111822;
              --md-primary-fg-color: #83bfff;
            }
            html,
            body {
              margin: 0;
              min-height: 100%;
              background: transparent;
              font-family: Arial, sans-serif;
            }
            .md-content__inner:has(.kb-home-bento) {
              padding: 1rem 0;
            }
            .md-content__inner:has(.kb-home-bento) > h1:first-child {
              animation: none !important;
              font-size: 92px;
              margin: 0 auto;
            }
            .kb-home-bento {
              display: block;
              width: 1px;
              height: 1px;
            }
            """,
        ]
    )
    return f"""<!doctype html>
<meta charset="utf-8">
<style>{css}</style>
<main class="md-typeset">
  <div class="md-content__inner">
    <h1 id="title">Knowledge Base</h1>
    <div class="kb-home-bento" aria-hidden="true"></div>
  </div>
</main>
"""


def capture_metrics(client: CdpClient, scheme: str, frame: int, position: str, threshold: float) -> CaptureMetrics:
    setup = f"""
    (async () => {{
      document.documentElement.setAttribute('data-md-color-scheme', {scheme!r});
      document.body.setAttribute('data-md-color-scheme', {scheme!r});
      const title = document.getElementById('title');
      title.style.backgroundPosition = {position!r};
      await document.fonts.ready;
      await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
      const rect = title.getBoundingClientRect();
      return {{
        x: Math.max(0, Math.floor(rect.left) - 3),
        y: Math.max(0, Math.floor(rect.top) - 3),
        width: Math.ceil(rect.width) + 6,
        height: Math.ceil(rect.height) + 6
      }};
    }})()
    """
    clip = client.evaluate(setup, timeout=5)
    shot = client.call(
        "Page.captureScreenshot",
        {
            "format": "png",
            "clip": {**clip, "scale": 1},
            "fromSurface": True,
            "captureBeyondViewport": True,
            "omitBackground": True,
        },
        timeout=10,
    )
    width, height, rgba = png_rgba(base64.b64decode(shot["data"]))
    return {
        **gradient_metrics(width, height, rgba, threshold),
        "scheme": scheme,
        "frame": frame,
        "position": position,
    }


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


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
