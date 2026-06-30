"""Refresh local generated data needed by the static knowledge-base site.

Run from the repository root:

    python knowledge_base/scripts/refresh_offline_data.py

The script intentionally avoids ingest, prefill, and online enrichment flows.
It regenerates local Map/Semantic Search data and their sidecars, validates
metadata placement, and runs a final Zensical build so generated assets are
republished together.
"""

from __future__ import annotations

import argparse
import re
import time
from collections.abc import Callable
from pathlib import Path

from rich.console import Console
from rich.progress import BarColumn, Progress, SpinnerColumn, TaskID, TaskProgressColumn, TextColumn, TimeElapsedColumn

from knowledge_base.progress import PROGRESS_ENV, PROGRESS_PREFIX
from knowledge_base.scripts.offline_refresh import runner as _runner
from knowledge_base.scripts.offline_refresh import state as _state
from knowledge_base.scripts.offline_refresh.formatting import format_duration
from knowledge_base.scripts.offline_refresh.model import Step, StepResult
from knowledge_base.scripts.offline_refresh.runtime import subprocess_env as _subprocess_env
from knowledge_base.scripts.offline_refresh.steps import build_steps as _build_steps

KB_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = KB_DIR.parent
CONSOLE = Console()
CHILD_PROGRESS_RE = re.compile(rf"^\s*{re.escape(PROGRESS_PREFIX)}\s+(\d+)/(\d+)(?:\s+(.*))?$")
REFRESH_STATE_VERSION = 1
REFRESH_STATE_PATH = KB_DIR / ".generated" / "refresh-state.json"
HOT_START_STATUS_PATHS = (
    "knowledge_base/docs",
    "knowledge_base/tree.yml",
    "knowledge_base/zensical.yml",
    "knowledge_base/catalog.py",
    "knowledge_base/config.py",
    "knowledge_base/dev_cli.py",
    "knowledge_base/embedding_workbench.py",
    "knowledge_base/generated_assets.py",
    "knowledge_base/generated_files.py",
    "knowledge_base/generate_papers.py",
    "knowledge_base/scripts/refresh_offline_data.py",
    "knowledge_base/scripts/offline_refresh",
    "knowledge_base/components",
    "pyproject.toml",
    "poetry.lock",
)
HOT_START_REQUIRED_FILES = (
    KB_DIR / "components" / "map" / "cache" / "embedding_cache.json",
    KB_DIR / "components" / "map" / "cache" / "embedding_cache.vectors.npy",
    KB_DIR / "components" / "map" / "generated" / "map-data.js",
    KB_DIR / "components" / "map" / "generated" / "map-similarity.i16",
    KB_DIR / "components" / "semantic_search" / "embedding_cache.json",
    KB_DIR / "components" / "semantic_search" / "embedding_cache.vectors.npy",
    KB_DIR / "components" / "semantic_search" / "semantic-search-index.json",
    KB_DIR / "components" / "semantic_search" / "semantic-search-settings.json",
    KB_DIR / "components" / "semantic_search" / "semantic-search-vectors.i8",
    KB_DIR / "site" / "index.html",
    KB_DIR / "site" / "map" / "index.html",
    KB_DIR / "site" / "search" / "index.html",
)


def subprocess_env() -> dict[str, str]:
    return _subprocess_env(PROGRESS_ENV)


def site_has_paper_pages() -> bool:
    return _state.site_has_paper_pages(KB_DIR)


def state_fingerprint_paths() -> tuple[list[Path], str | None]:
    return _state.state_fingerprint_paths(REPO_ROOT, HOT_START_STATUS_PATHS)


def refresh_state_fingerprint() -> tuple[dict[str, object], str | None]:
    return _state.refresh_state_fingerprint(REPO_ROOT, HOT_START_STATUS_PATHS, REFRESH_STATE_VERSION)


def refresh_state_status() -> tuple[str, str]:
    return _state.refresh_state_status(REFRESH_STATE_PATH, REPO_ROOT, HOT_START_STATUS_PATHS, REFRESH_STATE_VERSION)


def write_refresh_state() -> str | None:
    return _state.write_refresh_state(REFRESH_STATE_PATH, REPO_ROOT, HOT_START_STATUS_PATHS, REFRESH_STATE_VERSION)


def writes_complete_default_outputs(args: argparse.Namespace) -> bool:
    return _state.writes_complete_default_outputs(args)


def hot_start_fast_path(args: argparse.Namespace) -> tuple[bool, str]:
    return _state.hot_start_fast_path(
        args,
        repo_root=REPO_ROOT,
        status_paths=HOT_START_STATUS_PATHS,
        required_files=HOT_START_REQUIRED_FILES,
        site_has_paper_pages=site_has_paper_pages,
        refresh_state_status=refresh_state_status,
    )


def run_command(
    command: list[str],
    console: Console,
    *,
    on_stdout_line: Callable[[str], bool] | None = None,
) -> tuple[int, str | None]:
    return _runner.run_command(
        command,
        console,
        repo_root=REPO_ROOT,
        env=subprocess_env(),
        on_stdout_line=on_stdout_line,
    )


def run_step(
    step: Step,
    *,
    index: int,
    total: int,
    dry_run: bool,
    console: Console,
    progress: Progress | None = None,
    progress_task: TaskID | None = None,
    work_task: TaskID | None = None,
) -> StepResult:
    return _runner.run_step(
        step,
        index=index,
        total=total,
        dry_run=dry_run,
        console=console,
        child_progress_re=CHILD_PROGRESS_RE,
        run_command_fn=lambda command, output_console, handler: run_command(
            command, output_console, on_stdout_line=handler
        ),
        progress=progress,
        progress_task=progress_task,
        work_task=work_task,
    )


def print_timing_report(results: list[StepResult], total_s: float, *, failed: bool, console: Console) -> None:
    _runner.print_timing_report(results, total_s, failed=failed, console=console)


def build_steps(args: argparse.Namespace) -> list[Step]:
    return _build_steps(args)


def parse_args() -> argparse.Namespace:
    from knowledge_base.scripts.offline_refresh.cli import parse_args as _parse_args

    return _parse_args()


def main() -> int:
    args = parse_args()
    steps = build_steps(args)
    run_start_ns = time.perf_counter_ns()
    returncode = 0
    results: list[StepResult] = []
    CONSOLE.print(f"Working directory: {REPO_ROOT}", style="dim", markup=False, highlight=False)
    if args.dry_run:
        CONSOLE.print("Dry run: no commands will be executed.", style="yellow")
    else:
        fast_path_start_ns = time.perf_counter_ns()
        fast_path, reason = hot_start_fast_path(args)
        if fast_path:
            if reason == "tracked refresh files are clean":
                state_error = write_refresh_state()
                if state_error:
                    CONSOLE.print(f"Could not write refresh state stamp: {state_error}", style="yellow")
            elapsed_s = (time.perf_counter_ns() - fast_path_start_ns) / 1_000_000_000
            CONSOLE.print(f"Hot-start no-op: {reason}.", style="green")
            CONSOLE.print(f"Offline generated data is already fresh ({format_duration(elapsed_s)}).", style="green")
            return 0
        CONSOLE.print(f"Hot-start fast path skipped: {reason}.", style="dim")

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TaskProgressColumn(),
        TimeElapsedColumn(),
        console=CONSOLE,
        redirect_stdout=False,
        redirect_stderr=False,
    ) as progress:
        progress_task = progress.add_task("Starting", total=len(steps))
        work_task = progress.add_task("Current work", total=1, visible=False)
        for index, step in enumerate(steps, start=1):
            result = run_step(
                step,
                index=index,
                total=len(steps),
                dry_run=args.dry_run,
                console=CONSOLE,
                progress=progress,
                progress_task=progress_task,
                work_task=work_task,
            )
            results.append(result)
            returncode = result.returncode
            if returncode:
                progress.update(progress_task, description="Stopped")
                break
        else:
            progress.update(progress_task, description="Complete")

    run_duration_s = (time.perf_counter_ns() - run_start_ns) / 1_000_000_000
    if not args.dry_run:
        print_timing_report(results, run_duration_s, failed=bool(returncode), console=CONSOLE)
    if returncode:
        return returncode

    if args.dry_run:
        CONSOLE.print("\nDry run complete.", style="green")
    else:
        if writes_complete_default_outputs(args):
            state_error = write_refresh_state()
            if state_error:
                CONSOLE.print(f"Could not write refresh state stamp: {state_error}", style="yellow")
        CONSOLE.print("\nOffline generated data is refreshed and the consistency checks passed.", style="green")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
