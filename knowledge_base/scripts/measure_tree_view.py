"""Measure Tree page load and top-level branch click timing.

The default scenario starts from the Tree page's default load and clicks the
large first-level Decision-making branch. It combines phase timings emitted by
the Tree page when loaded with ``?ct_perf=1`` with Chrome Performance metrics
for script, style, and layout work.

Examples, from ``knowledge_base/``:

  python scripts/measure_tree_view.py
  python scripts/measure_tree_view.py --url http://127.0.0.1:8000/tree/
  python scripts/measure_tree_view.py --runs 7 --viewport 1366x900
"""

from __future__ import annotations

import argparse
import functools
import json
import statistics
import sys
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse

from verify_map_view import (
    CdpClient,
    find_chrome,
    get_tab_websocket,
    launch_chrome,
    parse_viewport,
    shutdown_chrome,
)


DEFAULT_VIEWPORTS = ["1366x900"]
DEFAULT_BRANCH = "Decision-making"
PERFORMANCE_METRICS = [
    "TaskDuration",
    "ScriptDuration",
    "LayoutDuration",
    "RecalcStyleDuration",
    "LayoutCount",
    "RecalcStyleCount",
    "Nodes",
    "JSHeapUsedSize",
]
PHASE_ORDER = [
    "hydrate.total",
    "render.total",
    "render.sunburst",
    "sunburst.model",
    "sunburst.snapshot",
    "sunburst.html.arcs",
    "sunburst.html.leafMarks",
    "sunburst.html.hitTargets",
    "sunburst.html.labels",
    "sunburst.dom",
    "sunburst.animationSetup",
    "render.focusedTree",
    "focusedTree.html",
    "focusedTree.dom",
    "render.selectionDetails",
    "render.indexPreviewTargets",
    "previewTargets.query",
    "previewTargets.index",
]


JS_MEASURE_INTERACTION = r"""
(async () => {
  const branchLabel = __BRANCH_LABEL__;
  const normalize = value => String(value || '')
    .toLowerCase()
    .replace(/[\u2010-\u2015]/g, '-')
    .replace(/[_-]+/g, ' ')
    .replace(/\s+/g, ' ')
    .trim();
  const compact = value => normalize(value).replace(/\s+/g, '');
  const app = document.getElementById('ct-app');
  const chain = document.getElementById('ct-ancestor-chain');
  const perf = window.__ctTreePerf;
  if (!app || !chain || !perf || !perf.enabled) {
    throw new Error('Tree perf hooks are not available; load the page with ?ct_perf=1.');
  }

  const navigation = performance.getEntriesByType('navigation')[0];
  const navigationTiming = navigation ? {
    domContentLoaded: navigation.domContentLoadedEventEnd - navigation.startTime,
    load: navigation.loadEventEnd - navigation.startTime,
    responseEnd: navigation.responseEnd - navigation.startTime,
  } : null;

  const counts = () => ({
    treeNodes: app.querySelectorAll('.ct-tree-node').length,
    treeButtons: app.querySelectorAll('.ct-tree-button').length,
    childRows: app.querySelectorAll('.ct-focus-section--children .ct-tree-node').length,
    previewTargets: app.querySelectorAll('[data-ct-preview-node]').length,
    sunburstSegments: app.querySelectorAll('.ct-sunburst-segment').length,
    sunburstCoarseMorphs: app.querySelectorAll('.ct-sunburst-coarse-morph').length,
    sunburstHitTargets: app.querySelectorAll('.ct-sunburst-hit-target').length,
    sunburstLabels: app.querySelectorAll('.ct-sunburst-label').length,
  });

  const waitFrame = () => new Promise(resolve => requestAnimationFrame(() => resolve(performance.now())));
  const waitIdle = () => new Promise(resolve => {
    const idle = window.requestIdleCallback || (callback => setTimeout(() => callback({ didTimeout: true }), 50));
    idle(() => resolve(performance.now()), { timeout: 700 });
  });
  const waitUntil = async (predicate, timeoutMs) => {
    const deadline = performance.now() + timeoutMs;
    while (performance.now() < deadline) {
      if (predicate()) return true;
      await waitFrame();
    }
    return predicate();
  };

  const candidates = Array.from(chain.querySelectorAll('[data-ct-select]')).map(element => {
    const labelElement = element.querySelector('.ct-tree-label');
    return {
      element,
      id: element.getAttribute('data-ct-select') || '',
      label: labelElement ? labelElement.textContent.trim() : element.textContent.trim(),
    };
  });
  const wanted = normalize(branchLabel);
  const wantedCompact = compact(branchLabel);
  const target = candidates.find(candidate => normalize(candidate.label) === wanted)
    || candidates.find(candidate => compact(candidate.label) === wantedCompact)
    || candidates.find(candidate => compact(candidate.label).includes(wantedCompact));
  if (!target) {
    throw new Error('Could not find Tree branch "' + branchLabel + '". Available: ' + candidates.map(c => c.label).join(', '));
  }

  const initial = {
    url: window.location.href,
    navigationTiming,
    counts: counts(),
    perf: perf.snapshot(),
  };

  const longTasks = [];
  let observer = null;
  try {
    observer = new PerformanceObserver(list => {
      list.getEntries().forEach(entry => {
        longTasks.push({
          name: entry.name,
          startTime: entry.startTime,
          duration: entry.duration,
        });
      });
    });
    observer.observe({ type: 'longtask' });
  } catch (error) {
    observer = null;
  }

  perf.reset();
  const beforeCounts = counts();
  const beforeClick = performance.now();
  target.element.click();
  const afterClick = performance.now();

  const beforeForcedLayout = performance.now();
  const appRect = app.getBoundingClientRect();
  const chainHeight = chain.offsetHeight;
  const bodyHeight = document.body.scrollHeight;
  const afterForcedLayout = performance.now();

  const afterCounts = counts();
  const firstFrame = await waitFrame();
  const secondFrame = await waitFrame();
  const animationSettled = await waitUntil(
    () => !app.querySelector('.ct-sunburst-svg.is-unfolding'),
    1500
  );
  const afterAnimation = performance.now();
  const idleTime = await waitIdle();
  if (observer) observer.disconnect();

  return {
    initial,
    target: {
      id: target.id,
      label: target.label,
    },
    interaction: {
      countsBefore: beforeCounts,
      countsAfter: afterCounts,
      layoutProbe: {
        appWidth: appRect.width,
        appHeight: appRect.height,
        chainHeight,
        bodyHeight,
      },
      timings: {
        clickSync: afterClick - beforeClick,
        forcedLayout: afterForcedLayout - beforeForcedLayout,
        toFirstFrame: firstFrame - beforeClick,
        toSecondFrame: secondFrame - beforeClick,
        toAnimationSettled: afterAnimation - beforeClick,
        toIdle: idleTime - beforeClick,
        animationSettled,
      },
      perf: perf.snapshot(),
      longTasks: longTasks.filter(task => task.startTime >= beforeClick),
    },
  };
})()
"""


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format: str, *args: Any) -> None:  # noqa: A002 - stdlib signature
        return


def serve_site(site_dir: Path) -> tuple[ThreadingHTTPServer, str]:
    if not site_dir.exists():
        raise FileNotFoundError(f"{site_dir} does not exist. Run mkdocs build first or pass --url.")
    handler = functools.partial(QuietHandler, directory=str(site_dir))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    host, port = server.server_address
    return server, f"http://{host}:{port}/tree/"


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
    import time

    deadline = time.time() + timeout
    last_error: Exception | None = None
    while time.time() < deadline:
        try:
            if client.evaluate(expression, timeout=2):
                return
        except Exception as exc:  # noqa: BLE001 - page may still be navigating
            last_error = exc
        time.sleep(0.15)
    raise TimeoutError(f"Tree page did not become ready: {last_error}")


def performance_metrics(client: CdpClient) -> dict[str, float]:
    result = client.call("Performance.getMetrics")
    metrics = result.get("metrics", [])
    return {str(metric["name"]): float(metric["value"]) for metric in metrics}


def metric_delta(before: dict[str, float], after: dict[str, float]) -> dict[str, float]:
    delta: dict[str, float] = {}
    for name in PERFORMANCE_METRICS:
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
        JS_MEASURE_INTERACTION.replace("__BRANCH_LABEL__", json.dumps(branch)),
        timeout=35,
    )
    after = performance_metrics(client)
    result["cdpMetricDelta"] = metric_delta(before, after)
    return result


def median(values: list[float]) -> float:
    return statistics.median(values) if values else 0.0


def ms(value: float) -> float:
    return value * 1000


def fmt_ms(value: float) -> str:
    return f"{value:.1f} ms"


def collect_phase_durations(runs: list[dict[str, Any]], section: str) -> dict[str, list[float]]:
    phases: dict[str, list[float]] = {}
    for run in runs:
        entries = run[section]["perf"].get("entries", [])
        for entry in entries:
            name = str(entry.get("name", ""))
            duration = entry.get("duration")
            if isinstance(duration, (int, float)):
                phases.setdefault(name, []).append(float(duration))
    return phases


def top_phase_lines(phases: dict[str, list[float]], limit: int = 10) -> list[str]:
    ranked = sorted(
        phases.items(),
        key=lambda item: median(item[1]),
        reverse=True,
    )
    ordered = [item for item in ranked if item[0] in PHASE_ORDER]
    ordered.extend(item for item in ranked if item[0] not in PHASE_ORDER)
    return [f"    {name}: {fmt_ms(median(values))}" for name, values in ordered[:limit]]


def summarize_viewport(label: str, runs: list[dict[str, Any]]) -> str:
    timings = [run["interaction"]["timings"] for run in runs]
    cdp = [run.get("cdpMetricDelta", {}) for run in runs]
    long_tasks = [
        sum(float(task.get("duration", 0.0)) for task in run["interaction"].get("longTasks", []))
        for run in runs
    ]
    first = runs[0]
    counts_after = first["interaction"]["countsAfter"]
    target = first["target"]

    lines = [
        f"{label}: {len(runs)} measured run(s)",
        f"  target: {target['label']} ({target['id']})",
        (
            "  rendered after click: "
            f"{counts_after['childRows']} child rows, "
            f"{counts_after['treeButtons']} tree buttons, "
            f"{counts_after['sunburstSegments']} sunburst segments, "
            f"{counts_after.get('sunburstCoarseMorphs', 0)} coarse morphs, "
            f"{counts_after['previewTargets']} preview targets"
        ),
        "  wall-clock medians:",
        f"    click handler sync: {fmt_ms(median([float(t['clickSync']) for t in timings]))}",
        f"    forced layout probe: {fmt_ms(median([float(t['forcedLayout']) for t in timings]))}",
        f"    to first frame: {fmt_ms(median([float(t['toFirstFrame']) for t in timings]))}",
        f"    to second frame: {fmt_ms(median([float(t['toSecondFrame']) for t in timings]))}",
        f"    to animation settled: {fmt_ms(median([float(t['toAnimationSettled']) for t in timings]))}",
        f"    long-task total: {fmt_ms(median(long_tasks))}",
        "  Chrome metric deltas:",
    ]
    for name in PERFORMANCE_METRICS:
        values = [float(delta[name]) for delta in cdp if name in delta]
        if not values:
            continue
        value = median(values)
        if name.endswith("Duration"):
            lines.append(f"    {name}: {fmt_ms(ms(value))}")
        elif name in {"JSHeapUsedSize"}:
            lines.append(f"    {name}: {value / (1024 * 1024):.2f} MiB")
        else:
            lines.append(f"    {name}: {value:.1f}")

    lines.append("  initial-load Tree phase medians:")
    lines.extend(top_phase_lines(collect_phase_durations(runs, "initial")))
    lines.append("  click-render Tree phase medians:")
    lines.extend(top_phase_lines(collect_phase_durations(runs, "interaction")))
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Measure Tree page click timing in headless Chrome")
    parser.add_argument("--url", help="Served MkDocs Tree URL. Defaults to serving site/tree/ locally.")
    parser.add_argument("--site-dir", default="site", help="Built MkDocs site directory used when --url is omitted.")
    parser.add_argument("--chrome", help="Path to Chrome/Chromium")
    parser.add_argument("--branch", default=DEFAULT_BRANCH, help="First-level branch label to click")
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
        viewports = args.viewport or DEFAULT_VIEWPORTS
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


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
