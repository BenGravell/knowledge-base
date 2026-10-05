"""Build-time geometry checks for the rendered Map settings controls."""

from __future__ import annotations

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from itertools import combinations
from pathlib import Path
from threading import Thread
from typing import Any, override

from knowledge_base.scripts.verify_map_view.browser import (
    find_chrome,
    get_tab_websocket,
    launch_chrome,
    shutdown_chrome,
    wait_for_page_ready,
)
from knowledge_base.scripts.verify_map_view.cdp import CdpClient

VIEWPORT_WIDTHS = (320, 390, 760, 761, 1024, 1366)
LAYOUT_SNAPSHOT = """
(async () => {
  await document.fonts.ready;
  await new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
  const header = document.getElementById('mm-panel-header');
  const dock = document.getElementById('mm-branch-dock');
  const branch = document.getElementById('mm-branch-panel');
  const toggle = document.getElementById('mm-panel-hide-btn');
  await Promise.all(branch.getAnimations().map(animation => animation.finished));
  const rect = el => {
    const {left, right, top, bottom} = el.getBoundingClientRect();
    return {name: el.id || el.getAttribute('aria-label') || el.className, left, right, top, bottom};
  };
  return {
    header: rect(header),
    controls: [...header.querySelectorAll('button, .mm-section-label:not(:has(button)), #mm-panel-title')].map(rect),
    overflow: [header, ...header.querySelectorAll('*'), dock, toggle, branch]
      .filter(el => el.clientWidth && el.scrollWidth > el.clientWidth + 1)
      .map(el => el.id || el.className),
    panels: ['mm-panel', 'mm-branch-dock'].map(id => rect(document.getElementById(id))),
    viewport: {left: 0, right: document.documentElement.clientWidth, bottom: innerHeight -
      (parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--mm-footer-h')) || 0)},
    dock: rect(dock),
    toggle: rect(toggle),
    branch: rect(branch),
    expanded: toggle.getAttribute('aria-expanded') === 'true',
    inert: branch.inert,
    toggleReachable: toggle.contains(document.elementFromPoint(
      toggle.getBoundingClientRect().left + toggle.clientWidth / 2,
      toggle.getBoundingClientRect().top + toggle.clientHeight / 2
    ))
  };
})()
"""


def layout_failures(snapshot: dict[str, Any], width: int) -> list[str]:
    """Reject overflow even when CSS hides it; touching edges are not collisions."""
    failures = [f"horizontal overflow: {name}" for name in snapshot["overflow"]]
    header = snapshot["header"]
    if header["left"] < -1 or header["right"] > width + 1:
        failures.append("settings header exceeds viewport")
    controls = snapshot["controls"]
    if len(controls) < 7:
        failures.append("missing settings controls")
    failures.extend(
        f"clipped control: {control['name']}"
        for control in controls
        if any(
            control[edge] < header[edge] - 1 if edge in ("left", "top") else control[edge] > header[edge] + 1
            for edge in ("left", "right", "top", "bottom")
        )
    )
    for a, b in combinations(controls, 2):
        if (
            min(a["right"], b["right"]) - max(a["left"], b["left"]) > 1
            and min(a["bottom"], b["bottom"]) - max(a["top"], b["top"]) > 1
        ):
            failures.append(f"collision: {a['name']} / {b['name']}")
    failures.extend(
        f"panel overlaps header: {panel['name']}" for panel in snapshot["panels"] if panel["top"] < header["bottom"] - 1
    )
    viewport, dock, toggle, branch = (snapshot[key] for key in ("viewport", "dock", "toggle", "branch"))
    if any(abs(dock[edge] - viewport[edge]) > 1 for edge in ("left", "right", "bottom")):
        failures.append("branch dock must span the viewport bottom")
    if any(abs(toggle[edge] - dock[edge]) > 1 for edge in ("left", "right", "bottom")):
        failures.append("branch toggle must span the dock bottom")
    if any(abs(branch[edge] - toggle[edge]) > 1 for edge in ("left", "right")):
        failures.append("branch selector and toggle must share width")
    if abs(branch["bottom"] - toggle["top"]) > 1:
        failures.append("branch selector must reveal above toggle")
    if (branch["bottom"] - branch["top"] > 1) != snapshot["expanded"]:
        failures.append("branch height must match expanded state")
    if snapshot["inert"] == snapshot["expanded"]:
        failures.append("collapsed branch must be inert")
    if not snapshot["toggleReachable"]:
        failures.append("branch toggle must remain reachable")
    return failures


class QuietHandler(SimpleHTTPRequestHandler):
    @override
    def log_message(self, format: str, *args: Any) -> None:
        pass


def verify_settings_layout(site_dir: Path) -> None:
    """Require Chrome and check actual published HTML/CSS/JS, not a mock layout."""
    session = launch_chrome(find_chrome(None))
    client = None
    try:
        handler = partial(QuietHandler, directory=str(site_dir))
        with ThreadingHTTPServer(("127.0.0.1", 0), handler) as server:
            thread = Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                url = f"http://127.0.0.1:{server.server_port}/map/"
                client = CdpClient(get_tab_websocket(session, url))
                client.call("Page.enable")
                for width in VIEWPORT_WIDTHS:
                    client.call(
                        "Emulation.setDeviceMetricsOverride",
                        {"width": width, "height": 844, "deviceScaleFactor": 1, "mobile": width <= 760},
                    )
                    client.call("Page.navigate", {"url": url})
                    wait_for_page_ready(client)
                    for step, expanded in enumerate((False, True, False)):
                        if step:
                            client.evaluate("document.getElementById('mm-panel-hide-btn').click()")
                        snapshot = client.evaluate(LAYOUT_SNAPSHOT)
                        failures = layout_failures(snapshot, width)
                        if snapshot["expanded"] != expanded:
                            failures.append("branch toggle did not change expanded state")
                        if failures:
                            raise AssertionError(
                                f"Map settings at {width}px (expanded={expanded}):\n" + "\n".join(failures)
                            )
                    client.evaluate("document.querySelector('.kb-lod-help-button').click()")
                    if not client.evaluate("document.getElementById('kb-lod-help').matches(':popover-open')"):
                        raise AssertionError("LoD click must open its explanation")
                    if not client.evaluate("""(() => {
                      const help = document.getElementById('kb-lod-help');
                      return help.scrollWidth <= help.clientWidth && help.scrollHeight <= help.clientHeight;
                    })()"""):
                        raise AssertionError("LoD explanation must fit without scrolling")
                    client.call(
                        "Input.dispatchKeyEvent",
                        {"type": "keyDown", "key": "Escape", "code": "Escape", "windowsVirtualKeyCode": 27},
                    )
                    if client.evaluate("document.getElementById('kb-lod-help').matches(':popover-open')"):
                        raise AssertionError("Escape must close the LoD explanation")
            finally:
                server.shutdown()
                thread.join()
    finally:
        if client:
            client.close()
        shutdown_chrome(session)
