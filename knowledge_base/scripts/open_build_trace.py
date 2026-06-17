"""Open a local build trace in Perfetto UI."""

from __future__ import annotations

import argparse
import html
import http.server
import json
import mimetypes
import os
import socketserver
import subprocess
import sys
import webbrowser
from pathlib import Path
from urllib.parse import unquote


KB_DIR = Path(__file__).resolve().parents[1]
DEFAULT_PERFETTO_UI_DIR = KB_DIR / ".tools" / "perfetto-ui"
TRACE_URL = "/__trace"


def opener_html(trace: Path) -> str:
    title = trace.name
    escaped_title = html.escape(title)
    return f"""<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>{escaped_title}</title>
<style>
html, body, iframe {{ margin: 0; width: 100%; height: 100%; border: 0; }}
#status {{ position: fixed; inset: 12px auto auto 12px; z-index: 1; padding: 8px 10px; background: #fff; border: 1px solid #ccc; font: 14px sans-serif; }}
</style>
</head>
<body>
<div id="status">Loading trace...</div>
<iframe id="perfetto" src="/#!/?mode=embedded"></iframe>
<script>
const iframe = document.getElementById("perfetto");
const status = document.getElementById("status");
const traceUrl = {json.dumps(TRACE_URL)};
const title = {json.dumps(title)};

function waitForReady() {{
  return new Promise((resolve) => {{
    const interval = setInterval(() => iframe.contentWindow.postMessage("PING", "*"), 100);
    window.addEventListener("message", function onMessage(event) {{
      if (event.source === iframe.contentWindow && event.data === "PONG") {{
        clearInterval(interval);
        window.removeEventListener("message", onMessage);
        resolve();
      }}
    }});
  }});
}}

(async () => {{
  const response = await fetch(traceUrl);
  if (!response.ok) throw new Error(`${{response.status}} ${{response.statusText}}`);
  const buffer = await response.arrayBuffer();
  await waitForReady();
  iframe.contentWindow.postMessage({{
    perfetto: {{ buffer, title, fileName: title, localOnly: true }}
  }}, "*", [buffer]);
  status.remove();
}})().catch((error) => {{
  status.textContent = `Could not load trace: ${{error}}`;
}});
</script>
</body>
</html>
"""


def perfetto_ui_dir(path: Path) -> Path | None:
    ui_dir = path.expanduser().resolve()
    return ui_dir if (ui_dir / "index.html").is_file() else None


def send_file(handler: http.server.SimpleHTTPRequestHandler, path: Path) -> None:
    content_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    data = path.read_bytes()
    handler.send_response(200)
    handler.send_header("Content-Type", content_type)
    handler.send_header("Content-Length", str(len(data)))
    handler.end_headers()
    handler.wfile.write(data)


def make_handler(trace: Path, ui_dir: Path) -> type[http.server.SimpleHTTPRequestHandler]:
    class TraceHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self) -> None:
            request_path = self.path.split("?", 1)[0]
            if request_path == "/__open":
                html = opener_html(trace).encode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "text/html; charset=utf-8")
                self.send_header("Content-Length", str(len(html)))
                self.end_headers()
                self.wfile.write(html)
                return

            if request_path == TRACE_URL:
                send_file(self, trace)
                return

            relative = "index.html" if request_path == "/" else unquote(request_path).lstrip("/")
            target = (ui_dir / relative).resolve()
            if (ui_dir == target or ui_dir in target.parents) and target.is_file():
                send_file(self, target)
                return

            self.send_error(404)

    return TraceHandler


class TraceServer(socketserver.TCPServer):
    allow_reuse_address = True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("trace", type=Path)
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument(
        "--perfetto-ui-dir",
        type=Path,
        default=Path(os.environ.get("PERFETTO_UI_DIR", DEFAULT_PERFETTO_UI_DIR)),
        help="Local Perfetto UI dist directory. Defaults to PERFETTO_UI_DIR or knowledge_base/.tools/perfetto-ui.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    trace = args.trace.resolve()
    if not trace.exists():
        print(f"Missing trace: {trace}", file=sys.stderr)
        return 1
    ui_dir = perfetto_ui_dir(args.perfetto_ui_dir)
    if ui_dir is None:
        print(f"Missing local Perfetto UI: {args.perfetto_ui_dir}", file=sys.stderr)
        print("Build Perfetto UI once and set PERFETTO_UI_DIR to its ui/out/dist directory.", file=sys.stderr)
        return 1

    handler = make_handler(trace, ui_dir)
    with TraceServer(("127.0.0.1", args.port), handler) as server:
        host, port = server.server_address
        open_url = f"http://{host}:{port}/__open"
        print(f"Serving local Perfetto UI: http://{host}:{port}/")
        print(f"Trace file: {trace}")
        print("Leave this process running while Perfetto loads the trace. Ctrl-C stops it.")
        try:
            subprocess.Popen(["google-chrome-stable", "--new-window", open_url])
        except OSError:
            webbrowser.open(open_url)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
