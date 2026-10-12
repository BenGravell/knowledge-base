"""Compare built home pages with cold-cache Chrome, gzip, and fixed throttling.

Run with one build to record a baseline, or two builds to alternate before/after
trials. External font/MathJax requests are blocked equally to remove CDN noise.
"""

from __future__ import annotations

import argparse
import gzip
import json
import statistics
import time
from contextlib import ExitStack
from functools import cache, partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from threading import Thread
from typing import Any, override
from urllib.parse import urlsplit

from knowledge_base.scripts.verify_map_view.browser import (
    find_chrome,
    get_tab_websocket,
    launch_chrome,
    shutdown_chrome,
)
from knowledge_base.scripts.verify_map_view.cdp import CdpClient

READY_PROBE = """
window.homeBenchmark = {errors: [], longTasks: []};
window.addEventListener('error', event => {
  if (event.message) window.homeBenchmark.errors.push(event.message);
});
new PerformanceObserver(list => {
  window.homeBenchmark.longTasks.push(...list.getEntries().map(e => e.duration));
}).observe({type: 'longtask', buffered: true});
function previewsReady() {
  const stages = [...document.querySelectorAll('.kb-bento-preview-stage')];
  if (stages.length === 2 && stages.every(stage => stage.getBoundingClientRect().width > 0) &&
      document.querySelector('.ct-sunburst-segment') &&
      document.querySelector('#ct-ancestor-chain [data-ct-select]') &&
      document.querySelector('#tag-search-app .paper-similar-card')) {
    requestAnimationFrame(() => {
      window.homeBenchmark.readyMs = performance.now();
    });
  } else {
    requestAnimationFrame(previewsReady);
  }
}
requestAnimationFrame(previewsReady);
"""


@cache
def compressed_file(path: Path) -> bytes:
    return gzip.compress(path.read_bytes(), compresslevel=6, mtime=0)


class GzipHandler(SimpleHTTPRequestHandler):
    @override
    def log_message(self, format: str, *args: Any) -> None:
        pass

    @override
    def do_GET(self) -> None:
        path = Path(self.translate_path(urlsplit(self.path).path))
        if path.is_dir():
            path /= "index.html"
        if path.is_file() and path.suffix in {".html", ".css", ".js", ".json", ".svg"}:
            data = compressed_file(path)
            self.send_response(200)
            self.send_header("Content-Type", self.guess_type(str(path)))
            self.send_header("Content-Encoding", "gzip")
            self.send_header("Content-Length", str(len(data)))
            self.end_headers()
            self.wfile.write(data)
        else:
            super().do_GET()


def trial(client: CdpClient, url: str) -> dict[str, Any]:
    client.call("Network.clearBrowserCache")
    client.evaluate("window.homeBenchmark = null")
    client.call("Page.navigate", {"url": url})
    deadline = time.monotonic() + 45
    while time.monotonic() < deadline:
        ready = client.evaluate('window.homeBenchmark?.readyMs && document.readyState === "complete"')
        if ready:
            break
        time.sleep(0.05)
    else:
        raise AssertionError("Home previews did not finish rendering within 45 seconds")
    result = client.evaluate("""(() => {
      const navigation = performance.getEntriesByType('navigation')[0];
      const resources = performance.getEntriesByType('resource').filter(r => r.name.startsWith(location.origin));
      return {
        readyMs: homeBenchmark.readyMs,
        domContentLoadedMs: navigation.domContentLoadedEventEnd,
        longTaskMs: homeBenchmark.longTasks.reduce((sum, ms) => sum + ms, 0),
        transferBytes: navigation.transferSize + resources.reduce((sum, r) => sum + r.transferSize, 0),
        errors: homeBenchmark.errors,
        dataAssets: resources.filter(r => /(?:tree|search|home-preview)-data\\.js/.test(r.name))
          .map(r => ({name: new URL(r.name).pathname, bytes: r.encodedBodySize})),
      };
    })()""")
    assert not result["errors"], result["errors"]
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sites", type=Path, nargs="+")
    parser.add_argument("--runs", type=int, default=7)
    parser.add_argument("--cpu-rate", type=float, default=4)
    parser.add_argument("--latency-ms", type=float, default=80)
    parser.add_argument("--download-mbps", type=float, default=10)
    parser.add_argument("--max-ready-ms", type=float, help="Maximum median preview time for the last build")
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    session = launch_chrome(find_chrome(None))
    client = CdpClient(get_tab_websocket(session, "about:blank"))
    measurements = {str(site): [] for site in args.sites}
    try:
        client.call("Page.enable")
        client.call("Network.enable")
        client.call("Network.setCacheDisabled", {"cacheDisabled": True})
        client.call("Network.setBlockedURLs", {"urls": ["https://*"]})
        client.call(
            "Emulation.setDeviceMetricsOverride",
            {"width": 1366, "height": 900, "deviceScaleFactor": 1, "mobile": False},
        )
        client.call("Emulation.setCPUThrottlingRate", {"rate": args.cpu_rate})
        client.call(
            "Network.emulateNetworkConditions",
            {
                "offline": False,
                "latency": args.latency_ms,
                "downloadThroughput": args.download_mbps * 1_000_000 / 8,
                "uploadThroughput": args.download_mbps * 1_000_000 / 8,
            },
        )
        client.call("Page.addScriptToEvaluateOnNewDocument", {"source": READY_PROBE})
        with ExitStack() as stack:
            servers = []
            for site in args.sites:
                assert (site / "index.html").is_file(), site
                server = stack.enter_context(
                    ThreadingHTTPServer(("127.0.0.1", 0), partial(GzipHandler, directory=str(site)))
                )
                thread = Thread(target=server.serve_forever, daemon=True)
                thread.start()
                stack.callback(thread.join)
                stack.callback(server.shutdown)
                servers.append(server)
            # Discard one warmup per build; every measured navigation still has an empty browser cache.
            for run in range(args.runs + 1):
                for site, server in zip(args.sites, servers, strict=True):
                    result = trial(client, f"http://127.0.0.1:{server.server_port}/")
                    print(
                        f'{site.name} {run}: {result["readyMs"]:.0f} ms, {result["transferBytes"]:,} bytes', flush=True
                    )
                    if run:
                        measurements[str(site)].append(result)
    finally:
        client.close()
        shutdown_chrome(session)
    summary = {
        name: {
            metric: round(statistics.median(row[metric] for row in rows), 1)
            for metric in ("readyMs", "domContentLoadedMs", "longTaskMs", "transferBytes")
        }
        for name, rows in measurements.items()
    }
    args.output.write_text(
        json.dumps({"conditions": vars(args), "medians": summary, "runs": measurements}, indent=2, default=str) + "\n"
    )
    print(json.dumps(summary, indent=2))
    if args.max_ready_ms is not None:
        assert summary[str(args.sites[-1])]["readyMs"] <= args.max_ready_ms, summary


if __name__ == "__main__":
    main()
