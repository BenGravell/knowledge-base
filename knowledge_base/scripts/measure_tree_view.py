"""Measure Tree page load and top-level branch click timing.

The default scenario starts from the Tree page's default load and clicks the
large first-level Decision-making branch. It combines phase timings emitted by
the Tree page when loaded with ``?ct_perf=1`` with Chrome Performance metrics
for script, style, and layout work.

Examples, from the repository root:

  python knowledge_base/scripts/measure_tree_view.py
  python knowledge_base/scripts/measure_tree_view.py --url http://127.0.0.1:8000/tree/
  python knowledge_base/scripts/measure_tree_view.py --runs 7 --viewport 1366x900
"""

from __future__ import annotations

from typing import Any

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


def with_query_params(url: str, params: dict[str, str]) -> str:
    from knowledge_base.scripts.tree_view_measure.measure import with_query_params as impl

    return impl(url, params)


def wait_for_tree_ready(*args: Any, **kwargs: Any) -> Any:
    from knowledge_base.scripts.tree_view_measure.measure import wait_for_tree_ready as impl

    return impl(*args, **kwargs)


def performance_metrics(*args: Any, **kwargs: Any) -> Any:
    from knowledge_base.scripts.tree_view_measure.measure import performance_metrics as impl

    return impl(*args, **kwargs)


def metric_delta(before: dict[str, float], after: dict[str, float]) -> dict[str, float]:
    from knowledge_base.scripts.tree_view_measure.measure import metric_delta as impl

    return impl(before, after)


def run_once(*args: Any, **kwargs: Any) -> Any:
    from knowledge_base.scripts.tree_view_measure.measure import run_once as impl

    return impl(*args, **kwargs)


def main() -> int:
    from knowledge_base.scripts.tree_view_measure.cli import main as measure_main

    return measure_main()


if __name__ == "__main__":
    from knowledge_base.scripts.tree_view_measure.cli import run

    raise SystemExit(run())
