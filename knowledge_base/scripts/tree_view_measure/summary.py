"""Summary formatting for Tree performance measurements."""

from __future__ import annotations

import statistics
from typing import Any

from knowledge_base.scripts import measure_tree_view as core


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
    ordered = [item for item in ranked if item[0] in core.PHASE_ORDER]
    ordered.extend(item for item in ranked if item[0] not in core.PHASE_ORDER)
    return [f"    {name}: {fmt_ms(median(values))}" for name, values in ordered[:limit]]


def summarize_viewport(label: str, runs: list[dict[str, Any]]) -> str:
    timings = [run["interaction"]["timings"] for run in runs]
    cdp = [run.get("cdpMetricDelta", {}) for run in runs]
    long_tasks = [
        sum(float(task.get("duration", 0.0)) for task in run["interaction"].get("longTasks", [])) for run in runs
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
    for name in core.PERFORMANCE_METRICS:
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
