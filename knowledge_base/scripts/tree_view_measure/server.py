"""Local static-site server helpers for Tree measurement."""

from __future__ import annotations

import functools
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, override


class QuietHandler(SimpleHTTPRequestHandler):
    @override
    def log_message(self, format: str, *args: Any) -> None:
        _ = (format, args)


def serve_site(site_dir: Path) -> tuple[ThreadingHTTPServer, str]:
    if not site_dir.exists():
        raise FileNotFoundError(f"{site_dir} does not exist. Run `kb build` first or pass --url.")
    handler = functools.partial(QuietHandler, directory=str(site_dir))
    server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    host = str(server.server_address[0])
    port = int(server.server_address[1])
    return server, f"http://{host}:{port}/tree/"
