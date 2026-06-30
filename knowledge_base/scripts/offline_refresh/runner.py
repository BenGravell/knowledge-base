"""Subprocess runner and progress reporting for offline refresh."""

from __future__ import annotations

import re
import subprocess
import time
from collections.abc import Callable
from pathlib import Path

from rich.console import Console
from rich.progress import Progress, TaskID
from rich.table import Table

from knowledge_base.scripts.offline_refresh.formatting import format_command, format_duration, format_status
from knowledge_base.scripts.offline_refresh.model import Step, StepResult


def run_command(
    command: list[str],
    console: Console,
    *,
    repo_root: Path,
    env: dict[str, str],
    on_stdout_line: Callable[[str], bool] | None = None,
) -> tuple[int, str | None]:
    def handle_stdout_line(line: str) -> None:
        text = line.rstrip("\n")
        if on_stdout_line is not None and on_stdout_line(text):
            return
        console.print(text, markup=False, highlight=False)

    try:
        with subprocess.Popen(
            command,
            cwd=repo_root,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            encoding="utf-8",
            errors="replace",
            bufsize=1,
        ) as process:
            if process.stdout is None:
                return process.wait(), "stdout pipe was not created"
            for line in process.stdout:
                handle_stdout_line(line)
            return process.wait(), None
    except OSError as exc:
        return 127, str(exc)


def run_step(
    step: Step,
    *,
    index: int,
    total: int,
    dry_run: bool,
    console: Console,
    child_progress_re: re.Pattern[str],
    run_command_fn: Callable[[list[str], Console, Callable[[str], bool] | None], tuple[int, str | None]],
    progress: Progress | None = None,
    progress_task: TaskID | None = None,
    work_task: TaskID | None = None,
) -> StepResult:
    console.rule(f"{index}/{total} {step.group}: {step.label}", style="cyan")
    console.print(step.name, style="bold")
    console.print(f"$ {format_command(step.command)}", style="dim", markup=False, highlight=False, soft_wrap=True)
    if progress is not None and progress_task is not None:
        progress.update(progress_task, description=f"{step.group}: {step.label}")
    if progress is not None and work_task is not None:
        progress.update(work_task, description="Current work", completed=0, total=1, visible=False)
    if dry_run:
        if progress is not None and progress_task is not None:
            progress.advance(progress_task)
        return StepResult(step, 0.0, 0)

    def update_work_progress(current: int, total: int, label: str) -> None:
        if progress is None or work_task is None or total <= 0:
            return
        progress.update(
            work_task,
            description=label or f"{step.group}: {step.label}",
            completed=min(current, total),
            total=total,
            visible=True,
        )

    def advance_for_output(line: str) -> bool:
        match = child_progress_re.match(line)
        if not match:
            return False
        current = int(match.group(1))
        total = int(match.group(2))
        update_work_progress(current, total, match.group(3) or "")
        return True

    step_start_ns = time.perf_counter_ns()
    returncode, error = run_command_fn(step.command, console, advance_for_output)
    elapsed_s = (time.perf_counter_ns() - step_start_ns) / 1_000_000_000
    if error:
        console.print(f"Step failed after {format_duration(elapsed_s)}: {step.name}: {error}", style="bold red")
    elif returncode:
        console.print(f"Step failed after {format_duration(elapsed_s)}: {step.name}", style="bold red")
    else:
        console.print(f"Done in {format_duration(elapsed_s)}.", style="green")
    if progress is not None and progress_task is not None and not error and not returncode:
        progress.advance(progress_task)
    if progress is not None and work_task is not None and not error and not returncode:
        progress.update(work_task, visible=False)
    return StepResult(step, elapsed_s, returncode)


def print_timing_report(results: list[StepResult], total_s: float, *, failed: bool, console: Console) -> None:
    table = Table(title="Timing report" + (" (failed)" if failed else ""))
    table.add_column("Phase", style="bold")
    table.add_column("Step")
    table.add_column("Duration", justify="right")
    table.add_column("Status")
    for group in dict.fromkeys(result.step.group for result in results):
        group_results = [result for result in results if result.step.group == group]
        table.add_row(group, "Total", format_duration(sum(result.duration_s for result in group_results)), "")
        for result in group_results:
            table.add_row(
                "", result.step.label, format_duration(result.duration_s), format_status(bool(result.returncode))
            )
    table.add_row("Total", "", format_duration(total_s), format_status(failed))
    console.print()
    console.print(table)
