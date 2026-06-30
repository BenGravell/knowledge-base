"""Low-level Tree interaction measurement."""

from __future__ import annotations

import json
import time
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from knowledge_base.scripts import measure_tree_view as core
from knowledge_base.scripts.verify_map_view.cdp import CdpClient


def with_query_params(url: str, params: dict[str, str]) -> str:
    parsed = urlparse(url)
    query = dict(parse_qsl(parsed.query, keep_blank_values=True))
    query.update(params)
    return urlunparse(parsed._replace(query=urlencode(query)))


def wait_for_tree_ready(client: CdpClient, timeout: float = 25) -> None:
    expression = """
    Boolean(
      window.treeData &&
      window.__ctTreePerf &&
      window.__ctTreePerf.enabled &&
      document.getElementById('ct-app') &&
      document.querySelector('#ct-sunburst-stage svg') &&
      document.querySelector('#ct-ancestor-chain [data-ct-select]')
    )
    """
    deadline = time.time() + timeout
    last_error: Exception | None = None
    while time.time() < deadline:
        try:
            if client.evaluate(expression, timeout=2):
                return
        except Exception as exc:
            last_error = exc
        time.sleep(0.15)
    raise TimeoutError(f"Tree page did not become ready: {last_error}")


def performance_metrics(client: CdpClient) -> dict[str, float]:
    result = client.call("Performance.getMetrics")
    metrics = result.get("metrics", [])
    return {str(metric["name"]): float(metric["value"]) for metric in metrics}


def metric_delta(before: dict[str, float], after: dict[str, float]) -> dict[str, float]:
    delta: dict[str, float] = {}
    for name in core.PERFORMANCE_METRICS:
        if name in before and name in after:
            delta[name] = after[name] - before[name]
    return delta


def run_once(
    client: CdpClient,
    url: str,
    branch: str,
    viewport: tuple[int, int, bool],
    run_index: int,
    reduced_motion: bool,
) -> dict[str, Any]:
    width, height, mobile = viewport
    client.call("Page.enable")
    client.call("Runtime.enable")
    client.call("Performance.enable")
    client.call(
        "Emulation.setDeviceMetricsOverride",
        {
            "width": width,
            "height": height,
            "deviceScaleFactor": 1,
            "mobile": mobile,
        },
    )
    if reduced_motion:
        client.call(
            "Emulation.setEmulatedMedia",
            {"features": [{"name": "prefers-reduced-motion", "value": "reduce"}]},
        )
    else:
        client.call("Emulation.setEmulatedMedia", {"features": []})

    nav_url = with_query_params(
        url,
        {
            "ct_perf": "1",
            "_tree_measure": f"{width}x{height}_{int(mobile)}_{run_index}",
        },
    )
    client.call("Page.navigate", {"url": nav_url})
    wait_for_tree_ready(client)
    before = performance_metrics(client)
    result = client.evaluate(
        core.JS_MEASURE_INTERACTION.replace("__BRANCH_LABEL__", json.dumps(branch)),
        timeout=35,
    )
    after = performance_metrics(client)
    result["cdpMetricDelta"] = metric_delta(before, after)
    return result
