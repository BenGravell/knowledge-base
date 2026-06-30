"""Chrome capture helpers for home title gradient verification."""

from __future__ import annotations

import base64

from knowledge_base.scripts.verify_home_title_gradient.metrics import gradient_metrics
from knowledge_base.scripts.verify_home_title_gradient.model import CaptureMetrics
from knowledge_base.scripts.verify_home_title_gradient.png import png_rgba
from knowledge_base.scripts.verify_map_view.cdp import CdpClient


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
