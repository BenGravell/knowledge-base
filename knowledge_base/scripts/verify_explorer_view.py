"""Build-time geometry checks for the shared Tree and Map workspace."""

from __future__ import annotations

from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from itertools import combinations
from pathlib import Path
from threading import Thread
from typing import Any, override
from urllib.parse import quote

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
  const main = document.getElementById('kb-explorer-main');
  const workspace = document.getElementById('kb-explorer-workspace');
  const selector = document.getElementById('ct-ancestor-chain');
  window.__kbLayoutSelector ||= selector;
  await Promise.all([dock, branch, main].flatMap(el => el.getAnimations())
    .map(animation => animation.finished.catch(() => {})));
  const rect = el => {
    const {left, right, top, bottom} = el.getBoundingClientRect();
    return {name: el.id || el.getAttribute('aria-label') || el.className, left, right, top, bottom};
  };
  return {
    header: rect(header),
    controls: [...header.querySelectorAll('button, .mm-section-label:not(:has(button)), #mm-panel-title')].filter(el => el.getClientRects().length).map(rect),
    overflow: [header, ...header.querySelectorAll('*'), dock, toggle, branch]
      .filter(el => el.clientWidth && el.scrollWidth > el.clientWidth + 1)
      .map(el => el.id || el.className),
    main: rect(main),
    visibleModes: [['map', 'mm-app'], ['tree', 'ct-sunburst-panel']]
      .filter(([mode, id]) => {
        const el = document.getElementById(id);
        const style = getComputedStyle(el);
        return !el.hidden && style.display !== 'none' && style.visibility !== 'hidden' &&
          el.getBoundingClientRect().width > 0;
      }).map(([mode]) => mode),
    viewport: {left: 0, right: document.documentElement.clientWidth, top: workspace.getBoundingClientRect().top,
      bottom: innerHeight -
      (parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--mm-footer-h')) || 0)},
    dock: rect(dock),
    toggle: rect(toggle),
    branch: rect(branch),
    expanded: toggle.getAttribute('aria-expanded') === 'true',
    inert: branch.inert,
    sameSelector: selector === window.__kbLayoutSelector && branch.contains(selector),
    selection: [...selector.querySelectorAll('[data-ct-select][aria-current="true"]')]
      .map(el => el.getAttribute('data-ct-select')),
    toggleReachable: toggle.contains(document.elementFromPoint(
      toggle.getBoundingClientRect().left + toggle.clientWidth / 2,
      toggle.getBoundingClientRect().top + toggle.clientHeight / 2
    ))
  };
})()
"""

NAVIGATION_CHECK = """
(async () => {
  const check = (ok, message) => { if (!ok) throw new Error(message); };
  const settle = () => new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)));
  const app = document.getElementById('kb-explorer');
  const selector = document.getElementById('ct-ancestor-chain');
  const branch = document.getElementById('mm-branch-panel');
  const toggle = document.getElementById('mm-panel-hide-btn');
  const paperId = new URLSearchParams(location.hash.slice(1)).get('paper');
  const modeIs = mode => app.dataset.mode === mode &&
    [['map', 'mm-app'], ['tree', 'ct-sunburst-panel']].every(([name, id]) => {
      const pane = document.getElementById(id);
      return pane.inert === (name !== mode) &&
        (getComputedStyle(pane).visibility !== 'hidden') === (name === mode);
    });
  const switchMode = mode => document.querySelector(`[data-explorer-mode="${mode}"]`).click();
  const foldIs = expanded => toggle.getAttribute('aria-expanded') === String(expanded) &&
    branch.inert !== expanded && document.getElementById('ct-ancestor-chain') === selector;
  const visiblePapers = () => {
    const graph = window._map.graph();
    const renderer = window._map.renderer();
    renderer.refresh();
    return graph.nodes().filter(id => graph.getNodeAttribute(id, 'kind') === 'paper' &&
      !renderer.getNodeDisplayData(id).hidden).length;
  };
  await settle();
  check(modeIs('tree'), 'Explorer Tree URL must open Tree mode');
  check(paperId && window.kbTreeView.selection().paperId === paperId, 'Explorer Tree URL lost its paper');
  check(foldIs(false), 'Explorer must start with the branch selector collapsed');
  toggle.click();
  switchMode('map');
  await settle();
  check(modeIs('map') && window.kbTreeView.selection().paperId === paperId,
    'switching to Map must retain the selected paper');
  check(foldIs(true), 'switching to Map must retain the open shared branch selector');
  await new Promise(resolve => {
    window.addEventListener('popstate', resolve, {once: true});
    history.back();
  });
  await settle();
  check(modeIs('tree') && window.kbTreeView.selection().paperId === paperId,
    'Back must restore Tree mode and the selected paper');
  check(foldIs(true), 'Back must retain the open shared branch selector');
  document.getElementById('ct-sunburst-root').click();
  await settle();
  check(window.kbTreeView.selection().id === window.treeData.root.id, 'root control must select the root');
  const rootCount = visiblePapers();
  const paperCount = window._map.graph().nodes()
    .filter(id => window._map.graph().getNodeAttribute(id, 'kind') === 'paper').length;
  check(rootCount === paperCount && rootCount > 0, 'selecting root must show every Map paper');
  selector.querySelector('[data-ct-has-children]:not([aria-current="true"])').click();
  await settle();
  const selectedBranch = window.kbTreeView.selection().id;
  check(visiblePapers() > 0 && visiblePapers() < rootCount, 'selecting a branch must filter Map papers');
  switchMode('map');
  check(modeIs('map') && window.kbTreeView.selection().id === selectedBranch && foldIs(true),
    'Map must retain the selected branch and open selector');
  const graph = window._map.graph();
  const renderer = window._map.renderer();
  const target = graph.nodes().find(id => graph.getNodeAttribute(id, 'kind') === 'paper' &&
    !renderer.getNodeDisplayData(id).hidden);
  renderer.emit('clickNode', {node: target, event: {x: 100, y: 100}});
  check(window.kbTreeView.selection().paperId === target &&
    new URLSearchParams(location.hash.slice(1)).get('paper') === target,
    'Map paper selection must update Tree and the Explorer URL');
  renderer.emit('clickStage', {});
  check(!window.kbTreeView.selection().paperId &&
    JSON.stringify(window.kbTreeView.selection().path) === JSON.stringify(window.kbMapView.selection().path) &&
    new URLSearchParams(location.hash.slice(1)).get('ct') === window.kbTreeView.selection().id,
    'clearing Map paper selection must retain the same branch in both views and URL');
  toggle.click();
  switchMode('tree');
  check(modeIs('tree') && foldIs(false), 'Tree must retain the collapsed shared branch selector');
  return true;
})()
"""


def _header_layout_failures(snapshot: dict[str, Any], width: int) -> list[str]:
    failures = [f"horizontal overflow: {name}" for name in snapshot["overflow"]]
    header = snapshot["header"]
    if header["left"] < -1 or header["right"] > width + 1:
        failures.append("settings header exceeds viewport")
    controls = snapshot["controls"]
    if len(controls) < 3:
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
    return failures


def _workspace_layout_failures(snapshot: dict[str, Any]) -> list[str]:
    failures = []
    viewport, main, dock, header = (snapshot[key] for key in ("viewport", "main", "dock", "header"))
    for panel in (main, dock):
        if panel["top"] < header["bottom"] - 1:
            failures.append(f"panel overlaps header: {panel['name']}")
        if any(
            panel[edge] < viewport[edge] - 1 if edge in ("left", "top") else panel[edge] > viewport[edge] + 1
            for edge in ("left", "right", "top", "bottom")
        ):
            failures.append(f"panel exceeds workspace: {panel['name']}")
    if main["right"] - main["left"] <= 1 or main["bottom"] - main["top"] <= 1:
        failures.append("main view must remain visible")
    return failures


def _branch_dock_layout_failures(snapshot: dict[str, Any], width: int) -> list[str]:
    failures = []
    viewport, main, dock, toggle, branch = (snapshot[key] for key in ("viewport", "main", "dock", "toggle", "branch"))
    narrow = width <= 760
    dock_edges = ("left", "right", "bottom") if narrow else ("top", "right", "bottom")
    if any(abs(dock[edge] - viewport[edge]) > 1 for edge in dock_edges):
        failures.append("branch dock must span the workspace " + ("bottom" if narrow else "right"))
    if any(abs(toggle[edge] - dock[edge]) > 1 for edge in dock_edges):
        failures.append("branch toggle must span the dock " + ("bottom" if narrow else "right"))
    shared_edges = ("left", "right") if narrow else ("top", "bottom")
    if any(abs(branch[edge] - toggle[edge]) > 1 for edge in shared_edges):
        failures.append("branch selector and toggle must share " + ("width" if narrow else "height"))
    start, end = ("top", "bottom") if narrow else ("left", "right")
    if abs(branch[end] - toggle[start]) > 1 or abs(branch[start] - dock[start]) > 1:
        failures.append("branch selector must reveal " + ("above" if narrow else "left of") + " toggle")
    if (branch[end] - branch[start] > 1) != snapshot["expanded"]:
        failures.append("branch " + ("height" if narrow else "width") + " must match expanded state")
    if abs(main[end] - dock[start]) > 1:
        failures.append("main view and branch dock must meet without overlap")
    main_edges = ("left", "right", "top") if narrow else ("left", "top", "bottom")
    if any(abs(main[edge] - viewport[edge]) > 1 for edge in main_edges):
        failures.append("main view must fill the remaining workspace")
    if snapshot["expanded"]:
        fraction = (dock[end] - dock[start]) / max(1, viewport[end] - viewport[start])
        lower, upper = (0.45, 0.55) if narrow else (0.30, 0.40)
        if not lower <= fraction <= upper:
            failures.append(
                "expanded branch dock must occupy "
                + ("half the workspace height" if narrow else "30–40% of workspace width")
            )
    return failures


def layout_failures(snapshot: dict[str, Any], width: int) -> list[str]:
    """Reject overflow even when CSS hides it; touching edges are not collisions."""
    failures = [
        *_header_layout_failures(snapshot, width),
        *_workspace_layout_failures(snapshot),
        *_branch_dock_layout_failures(snapshot, width),
    ]
    if snapshot["inert"] == snapshot["expanded"]:
        failures.append("collapsed branch must be inert")
    if not snapshot["toggleReachable"]:
        failures.append("branch toggle must remain reachable")
    if not snapshot["sameSelector"]:
        failures.append("both modes must retain the shared branch selector element")
    if len(snapshot["visibleModes"]) != 1:
        failures.append("exactly one main view must be visible")
    return failures


def mode_switch_failures(before: dict[str, Any], after: dict[str, Any]) -> list[str]:
    failures = [
        f"switching modes moved {name}"
        for name in ("header", "main", "dock", "toggle", "branch")
        if any(abs(before[name][edge] - after[name][edge]) > 1 for edge in ("left", "right", "top", "bottom"))
    ]
    if before["selection"] != after["selection"]:
        failures.append("switching modes changed the selected branch")
    if before["expanded"] != after["expanded"]:
        failures.append("switching modes changed branch visibility")
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
                url = f"http://127.0.0.1:{server.server_port}/explorer/"
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
                        if expanded:
                            client.evaluate("""document.querySelector(
                              '#ct-ancestor-chain [data-ct-has-children]:not([aria-current="true"])'
                            ).click()""")
                        previous = None
                        for mode in ("map", "tree", "map"):
                            client.evaluate(f"document.querySelector('[data-explorer-mode=\"{mode}\"]').click()")
                            snapshot = client.evaluate(LAYOUT_SNAPSHOT)
                            failures = layout_failures(snapshot, width)
                            if snapshot["expanded"] != expanded:
                                failures.append("branch toggle did not change expanded state")
                            if snapshot["visibleModes"] != [mode]:
                                failures.append(f"mode selector did not show {mode}")
                            if previous:
                                failures.extend(mode_switch_failures(previous, snapshot))
                            if failures:
                                raise AssertionError(
                                    f"{mode.title()} settings at {width}px (expanded={expanded}):\n"
                                    + "\n".join(failures)
                                )
                            previous = snapshot
                    if width <= 760:
                        geometry = client.evaluate("""(() => {
                          const toggle = document.getElementById('mm-detail-toggle');
                          const mode = document.querySelector('.kb-mode-switch').getBoundingClientRect();
                          const rect = toggle.getBoundingClientRect();
                          if (Math.abs((rect.top + rect.bottom) - (mode.top + mode.bottom)) > 2)
                            throw new Error('LoD and mode switch must share one row');
                          if (document.getElementById('mm-detail-popover').matches(':popover-open'))
                            throw new Error('LoD choices must start collapsed');
                          return {x: rect.x + rect.width / 2, y: rect.y + rect.height / 2};
                        })()""")
                        client.call("Input.dispatchTouchEvent", {"type": "touchStart", "touchPoints": [geometry]})
                        target = client.evaluate("""(() => {
                          const picker = document.getElementById('mm-detail-popover');
                          if (!picker.matches(':popover-open')) throw new Error('Press must open LoD');
                          const rect = picker.getBoundingClientRect();
                          if (rect.left < 0 || rect.right > innerWidth) throw new Error('LoD popup overflows');
                          const button = picker.querySelector('button[data-level]:not(:disabled):not(.active)');
                          const box = button.getBoundingClientRect();
                          return {x: box.x + box.width / 2, y: box.y + box.height / 2, level: button.dataset.level};
                        })()""")
                        level = target.pop("level")
                        client.call("Input.dispatchTouchEvent", {"type": "touchMove", "touchPoints": [target]})
                        client.call("Input.dispatchTouchEvent", {"type": "touchEnd", "touchPoints": []})
                        if not client.evaluate(
                            f"""document.querySelector('#mm-detail-controls button.active').dataset.level === '{level}' &&
                          !document.getElementById('mm-detail-popover').matches(':popover-open')"""
                        ):
                            raise AssertionError(f"Sliding to {level} at {width}px must select it and close LoD")
                        client.evaluate("document.getElementById('mm-detail-toggle').click()")
                    else:
                        if not client.evaluate("""(() => {
                          const toggle = document.getElementById('mm-detail-toggle');
                          const picker = document.getElementById('mm-detail-popover');
                          const mode = document.querySelector('.kb-mode-switch').getBoundingClientRect();
                          const rect = picker.getBoundingClientRect();
                          return !toggle.getClientRects().length && !picker.hasAttribute('popover') &&
                            picker.querySelectorAll('button[data-level]').length === 5 &&
                            Math.abs((rect.top + rect.bottom) - (mode.top + mode.bottom)) <= 2;
                        })()"""):
                            raise AssertionError(f"LoD icons must appear inline at {width}px")
                        client.evaluate(
                            "document.querySelector('#mm-detail-controls button:not(:disabled):not(.active)').click()"
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
                    if width <= 760:
                        client.evaluate("document.getElementById('mm-detail-popover').hidePopover()")
                # Resizing an open picker must restore inline controls without losing selection.
                selected_level = client.evaluate(
                    "document.querySelector('#mm-detail-controls button.active').dataset.level"
                )
                for resize_width in (390, 1366):
                    client.call(
                        "Emulation.setDeviceMetricsOverride",
                        {
                            "width": resize_width,
                            "height": 844,
                            "deviceScaleFactor": 1,
                            "mobile": resize_width <= 760,
                        },
                    )
                    client.evaluate(
                        "new Promise(resolve => requestAnimationFrame(() => requestAnimationFrame(resolve)))"
                    )
                    if not client.evaluate(
                        f"""document.getElementById('mm-detail-popover').hasAttribute('popover') ===
                      {str(resize_width <= 760).lower()} &&
                      document.querySelector('#mm-detail-controls button.active').dataset.level === '{selected_level}'"""
                    ):
                        raise AssertionError("Resizing must adapt LoD controls and retain the selected level")
                    if resize_width <= 760:
                        client.evaluate("document.getElementById('mm-detail-toggle').click()")
                paper_id = client.evaluate("""(function firstPaper(node) {
                  if (node.kind === 'paper' && window._map.graph().hasNode(node.paper.id)) return node.paper.id;
                  for (const child of node.children || []) {
                    const id = firstPaper(child);
                    if (id) return id;
                  }
                })(window.treeData.root)""")
                if not paper_id:
                    raise AssertionError("Tree and Map must share a paper for navigation verification")
                client.call("Page.navigate", {"url": f"{url}?mode=tree#paper={quote(paper_id, safe='')}"})
                wait_for_page_ready(client)
                client.evaluate(NAVIGATION_CHECK)
                client.call("Page.navigate", {"url": f"{url}?mode=map&paper={quote(paper_id, safe='')}"})
                wait_for_page_ready(client)
                if not client.evaluate("""document.getElementById('kb-explorer').dataset.mode === 'map' &&
                  Boolean(window.kbTreeView.selection().paperId) &&
                  window.kbTreeView.selection().paperId === window.kbMapView.selection().paperId"""):
                    raise AssertionError("Explorer paper URLs must open the selected paper in Map mode")
            finally:
                server.shutdown()
                thread.join()
    finally:
        if client:
            client.close()
        shutdown_chrome(session)
