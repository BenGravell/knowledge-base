"""Headless Chrome helpers for map view verification."""

from __future__ import annotations

import json
import os
import shutil
import socket
import subprocess
import tempfile
import time
import urllib.request
from typing import Any
from urllib.parse import quote

from knowledge_base.scripts.verify_map_view.cdp import CdpClient, ChromeSession
from knowledge_base.scripts.verify_map_view.js_checks import JS_CHECKS


def find_chrome(explicit: str | None) -> str:
    candidates = [explicit] if explicit else []
    candidates.extend(["google-chrome-stable", "google-chrome", "chromium", "chromium-browser"])
    for candidate in candidates:
        if not candidate:
            continue
        path = shutil.which(candidate) if os.path.basename(candidate) == candidate else candidate
        if path and os.path.exists(path):
            return path
    raise RuntimeError("Could not find Chrome. Pass --chrome /path/to/chrome.")


def free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def launch_chrome(chrome: str) -> ChromeSession:
    port = free_port()
    user_data_dir = tempfile.mkdtemp(prefix="kb-map-chrome-")
    command = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--disable-dev-shm-usage",
        "--disable-extensions",
        "--no-first-run",
        "--no-default-browser-check",
        "--enable-unsafe-swiftshader",
        f"--remote-debugging-port={port}",
        f"--user-data-dir={user_data_dir}",
        "about:blank",
    ]
    process = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    session = ChromeSession(process=process, user_data_dir=user_data_dir, port=port)
    wait_for_json(session, "/json/version")
    return session


def wait_for_json(session: ChromeSession, path: str, timeout: float = 10) -> Any:
    url = f"http://127.0.0.1:{session.port}{path}"
    deadline = time.time() + timeout
    last_error: Exception | None = None
    while time.time() < deadline:
        if session.process.poll() is not None:
            raise RuntimeError("Chrome exited before DevTools became available")
        try:
            with urllib.request.urlopen(url, timeout=1) as response:
                return json.loads(response.read().decode("utf-8"))
        except Exception as exc:
            last_error = exc
            time.sleep(0.1)
    raise TimeoutError(f"Timed out waiting for {url}: {last_error}")


def get_tab_websocket(session: ChromeSession, url: str) -> str:
    create_url = f"http://127.0.0.1:{session.port}/json/new?{quote('about:blank', safe='')}"
    request = urllib.request.Request(create_url, method="PUT")
    try:
        with urllib.request.urlopen(request, timeout=2) as response:
            tab = json.loads(response.read().decode("utf-8"))
            return str(tab["webSocketDebuggerUrl"])
    except Exception as exc:
        tabs = wait_for_json(session, "/json/list")
        if not tabs:
            raise RuntimeError(f"Could not create a Chrome tab for {url}") from exc
        return str(tabs[0]["webSocketDebuggerUrl"])


def wait_for_page_ready(client: CdpClient, timeout: float = 35) -> None:
    expression = """
    Boolean(
      window._map &&
      window._map.renderer &&
      window._map.renderer() &&
      window._map.graph &&
      window._map.graph() &&
      (!document.getElementById('mm-loading') || document.getElementById('mm-loading').style.display === 'none')
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
        time.sleep(0.25)
    raise TimeoutError(f"Map did not become ready: {last_error}")


def run_viewport(client: CdpClient, url: str, width: int, height: int, mobile: bool) -> dict[str, Any]:
    client.call("Page.enable")
    client.call("Runtime.enable")
    client.call(
        "Emulation.setDeviceMetricsOverride",
        {
            "width": width,
            "height": height,
            "deviceScaleFactor": 1,
            "mobile": mobile,
        },
    )
    base_url, sep, hash_fragment = url.partition("#")
    query_sep = "&" if "?" in base_url else "?"
    nav_url = f"{base_url}{query_sep}_verify={width}x{height}_{int(mobile)}_{time.time_ns()}"
    if sep:
        nav_url = f"{nav_url}#{hash_fragment}"
    client.call("Page.navigate", {"url": nav_url})
    wait_for_page_ready(client)
    result = client.evaluate(JS_CHECKS, timeout=30)
    failures = result.get("failures", []) if isinstance(result, dict) else ["JS checks returned no result"]
    if failures:
        formatted = "\n".join(f"  - {failure}" for failure in failures)
        raise AssertionError(f"{width}x{height} failed:\n{formatted}")
    return result.get("metrics", {})


def shutdown_chrome(session: ChromeSession | None) -> None:
    if not session:
        return
    try:
        session.process.terminate()
        session.process.wait(timeout=3)
    except Exception:
        session.process.kill()
    shutil.rmtree(session.user_data_dir, ignore_errors=True)


def parse_viewport(value: str) -> tuple[int, int, bool]:
    parts = value.split(":")
    size = parts[0]
    width_s, height_s = size.lower().split("x", 1)
    mobile = len(parts) > 1 and parts[1].lower() == "mobile"
    return int(width_s), int(height_s), mobile


__all__ = [
    "find_chrome",
    "free_port",
    "get_tab_websocket",
    "launch_chrome",
    "parse_viewport",
    "run_viewport",
    "shutdown_chrome",
    "wait_for_json",
    "wait_for_page_ready",
]
