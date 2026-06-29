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
import hashlib
import json
import os
import re
import shlex
import subprocess
import sys
import time
from collections.abc import Callable
from dataclasses import dataclass
from pathlib import Path

from rich.console import Console
from rich.progress import BarColumn, Progress, SpinnerColumn, TaskID, TaskProgressColumn, TextColumn, TimeElapsedColumn
from rich.table import Table

from knowledge_base.embedding_workbench import FASTEMBED_DEVICE_CHOICES
from knowledge_base.progress import PROGRESS_ENV, PROGRESS_PREFIX

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
    "knowledge_base/map",
    "knowledge_base/semantic_search",
    "knowledge_base/tree",
    "pyproject.toml",
    "poetry.lock",
)
HOT_START_REQUIRED_FILES = (
    KB_DIR / "map" / "cache" / "embedding_cache.json",
    KB_DIR / "map" / "cache" / "embedding_cache.vectors.npy",
    KB_DIR / "map" / "generated" / "map-data.js",
    KB_DIR / "map" / "generated" / "map-similarity.i16",
    KB_DIR / "semantic_search" / "embedding_cache.json",
    KB_DIR / "semantic_search" / "embedding_cache.vectors.npy",
    KB_DIR / "semantic_search" / "semantic-search-index.json",
    KB_DIR / "semantic_search" / "semantic-search-settings.json",
    KB_DIR / "semantic_search" / "semantic-search-vectors.i8",
    KB_DIR / "site" / "index.html",
    KB_DIR / "site" / "map" / "index.html",
    KB_DIR / "site" / "search" / "index.html",
)


@dataclass(frozen=True)
class Step:
    group: str
    label: str
    name: str
    command: list[str]


@dataclass(frozen=True)
class StepResult:
    step: Step
    duration_s: float
    returncode: int


def format_command(command: list[str]) -> str:
    return shlex.join(command)


def format_duration(duration_s: float) -> str:
    if duration_s < 60:
        return f"{duration_s:.1f}s"
    minutes, seconds = divmod(duration_s, 60)
    return f"{int(minutes)}m {seconds:.0f}s"


def format_status(failed: bool) -> str:
    return "[red]FAIL[/]" if failed else "[green]PASS[/]"


def subprocess_env() -> dict[str, str]:
    env = os.environ.copy()
    env.setdefault("PYTHONUNBUFFERED", "1")
    env[PROGRESS_ENV] = "1"
    return env


def site_has_paper_pages() -> bool:
    papers_dir = KB_DIR / "site" / "papers"
    return papers_dir.exists() and next(papers_dir.rglob("index.html"), None) is not None


def state_fingerprint_paths() -> tuple[list[Path], str | None]:
    tracked = subprocess.run(
        ["git", "ls-files", "--cached", "--", *HOT_START_STATUS_PATHS],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if tracked.returncode:
        return [], "git ls-files failed"

    return sorted(REPO_ROOT / line for line in tracked.stdout.splitlines() if line), None


def refresh_state_fingerprint() -> tuple[dict[str, object], str | None]:
    paths, error = state_fingerprint_paths()
    if error:
        return {}, error

    digest = hashlib.sha256()
    file_count = 0
    missing_count = 0
    byte_count = 0
    for path in paths:
        rel_path = path.relative_to(REPO_ROOT).as_posix()
        digest.update(rel_path.encode("utf-8"))
        digest.update(b"\0")
        if not path.exists():
            missing_count += 1
            digest.update(b"<missing>\0")
            continue
        try:
            size = path.stat().st_size
            digest.update(f"{size}\0".encode("ascii"))
            with path.open("rb") as handle:
                for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                    digest.update(chunk)
        except OSError as exc:
            return {}, f"could not read {rel_path}: {exc}"
        file_count += 1
        byte_count += size

    return {
        "version": REFRESH_STATE_VERSION,
        "digest": digest.hexdigest(),
        "file_count": file_count,
        "missing_count": missing_count,
        "byte_count": byte_count,
    }, None


def refresh_state_status() -> tuple[str, str]:
    if not REFRESH_STATE_PATH.exists():
        return "missing", "no refresh state stamp"
    try:
        saved = json.loads(REFRESH_STATE_PATH.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return "stale", f"refresh state stamp is unreadable: {exc}"
    current, error = refresh_state_fingerprint()
    if error:
        return "stale", error
    if saved == current:
        return "match", "refresh state stamp matches current tracked files"
    return "stale", "refresh state stamp is stale"


def write_refresh_state() -> str | None:
    state, error = refresh_state_fingerprint()
    if error:
        return error
    REFRESH_STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    temporary = REFRESH_STATE_PATH.with_suffix(".json.tmp")
    try:
        temporary.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        temporary.replace(REFRESH_STATE_PATH)
    except OSError as exc:
        return f"could not write refresh state stamp: {exc}"
    return None


def writes_complete_default_outputs(args: argparse.Namespace) -> bool:
    return not (
        args.strict
        or args.skip_force_layout
        or args.skip_map
        or args.skip_semantic_search
        or args.skip_audit
        or args.skip_build
        or args.full_build
        or args.map_backend != "fastembed"
        or args.fastembed_device != "auto"
        or args.audit_severity != "error"
    )


def hot_start_fast_path(args: argparse.Namespace) -> tuple[bool, str]:
    if args.no_fast_path:
        return False, "disabled by --no-fast-path"
    if (
        args.force
        or args.strict
        or args.skip_map
        or args.skip_semantic_search
        or args.skip_audit
        or args.skip_build
        or args.full_build
        or args.map_backend != "fastembed"
        or args.fastembed_device != "auto"
        or args.audit_severity != "error"
    ):
        return False, "custom options require running the requested steps"

    missing = [path for path in HOT_START_REQUIRED_FILES if not path.exists()]
    if missing:
        return False, f"missing {len(missing)} generated output(s)"
    if not site_has_paper_pages():
        return False, "site paper pages are missing"

    state, state_reason = refresh_state_status()
    if state == "match":
        return True, state_reason
    if state == "stale":
        return False, state_reason

    status = subprocess.run(
        ["git", "status", "--porcelain=v1", "--untracked-files=no", "--", *HOT_START_STATUS_PATHS],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if status.returncode:
        return False, "git status failed"
    if status.stdout.strip():
        return False, "tracked refresh files changed"
    return True, "tracked refresh files are clean"


def run_command(
    command: list[str],
    console: Console,
    *,
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
            cwd=REPO_ROOT,
            env=subprocess_env(),
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
        match = CHILD_PROGRESS_RE.match(line)
        if not match:
            return False
        current = int(match.group(1))
        total = int(match.group(2))
        update_work_progress(current, total, match.group(3) or "")
        return True

    step_start_ns = time.perf_counter_ns()
    returncode, error = run_command(
        step.command,
        console,
        on_stdout_line=advance_for_output,
    )
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


def build_steps(args: argparse.Namespace) -> list[Step]:
    py = sys.executable
    steps: list[Step] = []

    validate_tree = [py, "knowledge_base/scripts/validate_tree.py"]
    if args.strict:
        validate_tree.append("--check-algorithm-labels")
    steps.append(Step("Validate", "Tree nav", "Validate Tree nav links and paper coverage", validate_tree))

    steps.append(
        Step(
            "Validate",
            "Tree coverage",
            "Check that every metadata-backed paper is in the Tree",
            [
                py,
                "knowledge_base/scripts/list_unplaced_papers.py",
                "--neighbors",
                "0",
                "--fail-on-missing",
            ],
        )
    )

    if not args.skip_semantic_search:
        semantic_search = [
            py,
            "knowledge_base/semantic_search/generate_semantic_search_index.py",
            "--fastembed-device",
            args.fastembed_device,
        ]
        if args.force:
            semantic_search.append("--force")
        steps.append(
            Step(
                "Generate",
                "Semantic Search",
                "Regenerate Semantic Search index, settings, and vector table",
                semantic_search,
            )
        )

    if not args.skip_map:
        map_data = [
            py,
            "knowledge_base/map/pipeline/generate_data.py",
            "--fastembed-device",
            args.fastembed_device,
        ]
        if args.map_backend != "auto":
            map_data.extend(["--backend", args.map_backend])
        if args.force:
            map_data.append("--force")
        if args.skip_force_layout:
            map_data.append("--skip-force-layout")
        steps.append(
            Step("Generate", "Map data", "Regenerate Map embeddings, layout, map-data.js, and sidecar", map_data)
        )

    if not args.skip_audit:
        steps.append(
            Step(
                "Verify",
                "Metadata audit",
                "Audit metadata and generated Map/Search assets",
                [py, "knowledge_base/scripts/audit_metadata.py", "knowledge_base", "--severity", args.audit_severity],
            )
        )

    if not args.skip_build:
        build = [py, "-m", "knowledge_base.dev_cli", "build"]
        if args.strict:
            build.append("--strict")
        steps.append(Step("Verify", "Zensical build", "Build Zensical site and generated assets", build))

    return steps


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Refresh offline generated data and validate site consistency.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Recompute Map and Semantic Search embeddings instead of using caches.",
    )
    parser.add_argument(
        "--map-backend",
        choices=("fastembed", "voyage", "auto"),
        default="fastembed",
        help=(
            "Map embedding backend. fastembed is the local default; auto lets "
            "generate_map_data.py choose, including Voyage when configured."
        ),
    )
    parser.add_argument(
        "--fastembed-device",
        choices=FASTEMBED_DEVICE_CHOICES,
        default="auto",
        help="Device for local fastembed inference in Map and Semantic Search: auto uses CUDA when available.",
    )
    parser.add_argument(
        "--skip-force-layout",
        action="store_true",
        help="Pass through to map/generate_map_data.py for quicker Map refreshes.",
    )
    parser.add_argument(
        "--audit-severity",
        choices=("error", "warning", "info"),
        default="error",
        help="Minimum metadata audit severity to print.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Enable Tree algorithm-label checks and Zensical strict mode.",
    )
    parser.add_argument(
        "--skip-map",
        action="store_true",
        help="Do not regenerate Map data.",
    )
    parser.add_argument(
        "--skip-semantic-search",
        action="store_true",
        help="Do not regenerate Semantic Search data.",
    )
    parser.add_argument(
        "--skip-audit",
        action="store_true",
        help="Do not run the metadata/map-data audit.",
    )
    parser.add_argument(
        "--skip-build",
        action="store_true",
        help="Do not run the final Zensical asset refresh build.",
    )
    parser.add_argument(
        "--full-build",
        action="store_true",
        help="Accepted for compatibility; Zensical builds always render generated paper detail pages.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the planned commands without running them.",
    )
    parser.add_argument(
        "--no-fast-path",
        action="store_true",
        help="Always run refresh steps even when the default hot-start no-op check is clean.",
    )
    return parser.parse_args()


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
