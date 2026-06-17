"""Open a local build trace in Perfetto UI."""

from __future__ import annotations

import argparse
import functools
import http.server
import socketserver
import subprocess
import sys
import webbrowser
from pathlib import Path
from urllib.parse import quote


class CorsHandler(http.server.SimpleHTTPRequestHandler):
    def do_OPTIONS(self) -> None:
        self.send_response(204)
        self.end_headers()

    def end_headers(self) -> None:
        self.send_header("Access-Control-Allow-Origin", "https://ui.perfetto.dev")
        self.send_header("Access-Control-Allow-Methods", "GET, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.send_header("Access-Control-Allow-Private-Network", "true")
        super().end_headers()


class TraceServer(socketserver.TCPServer):
    allow_reuse_address = True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("trace", type=Path)
    parser.add_argument("--port", type=int, default=8765)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    trace = args.trace.resolve()
    if not trace.exists():
        print(f"Missing trace: {trace}", file=sys.stderr)
        return 1

    handler = functools.partial(CorsHandler, directory=str(trace.parent))
    with TraceServer(("127.0.0.1", args.port), handler) as server:
        host, port = server.server_address
        trace_url = f"http://{host}:{port}/{quote(trace.name)}"
        perfetto_url = f"https://ui.perfetto.dev/#!/?url={quote(trace_url, safe=':/?=&')}"
        print(f"Serving trace: {trace_url}")
        print(f"Opening Perfetto: {perfetto_url}")
        print("Leave this process running while Perfetto loads the trace. Ctrl-C stops it.")
        try:
            subprocess.Popen(["google-chrome-stable", "--new-window", perfetto_url])
        except OSError:
            webbrowser.open(perfetto_url)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
