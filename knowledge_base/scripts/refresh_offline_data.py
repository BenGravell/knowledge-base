"""Refresh local generated data needed by the static knowledge-base site.

Run from ``knowledge_base/``:

    python scripts/refresh_offline_data.py

Or from the repository root:

    python knowledge_base/scripts/refresh_offline_data.py

The script intentionally avoids ingest, prefill, and online enrichment flows.
It regenerates local Map/Semantic Search data and their sidecars, validates
metadata placement, and runs a final MkDocs build so gen-files assets are
republished together.
"""

from __future__ import annotations

import argparse
import os
import shlex
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

from knowledge_base.scripts.build_metrics import (
    DEFAULT_METRICS_DIR,
    StepTiming,
    utc_now,
    utc_stamp,
    write_build_metrics,
)

KB_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = KB_DIR.parent


@dataclass(frozen=True)
class Step:
    name: str
    command: list[str]


def format_command(command: list[str]) -> str:
    return shlex.join(command)


def subprocess_env() -> dict[str, str]:
    env = os.environ.copy()
    pythonpath_parts = [str(REPO_ROOT)]
    if env.get("PYTHONPATH"):
        pythonpath_parts.append(env["PYTHONPATH"])
    env["PYTHONPATH"] = os.pathsep.join(pythonpath_parts)
    return env


def run_step(step: Step, *, index: int, total: int, dry_run: bool, run_start_ns: int) -> StepTiming:
    print(f"\n[{index}/{total}] {step.name}")
    print(f"$ {format_command(step.command)}")
    step_start_ns = time.perf_counter_ns()
    started_at = utc_stamp()
    if dry_run:
        return StepTiming(
            step.name,
            step.command,
            started_at,
            0.0,
            0.0,
            0,
        )

    error = None
    try:
        result = subprocess.run(step.command, cwd=KB_DIR, env=subprocess_env(), check=False)
        returncode = result.returncode
    except OSError as exc:
        returncode = 127
        error = str(exc)
    elapsed_s = (time.perf_counter_ns() - step_start_ns) / 1_000_000_000
    timing = StepTiming(
        step.name,
        step.command,
        started_at,
        (step_start_ns - run_start_ns) / 1_000_000_000,
        elapsed_s,
        returncode,
        error,
    )
    if error:
        print(f"\nStep failed after {elapsed_s:.1f}s: {step.name}: {error}", file=sys.stderr)
    elif returncode:
        print(f"\nStep failed after {elapsed_s:.1f}s: {step.name}", file=sys.stderr)
    else:
        print(f"Done in {elapsed_s:.1f}s.")
    return timing


def should_write_metrics(args: argparse.Namespace) -> bool:
    return not args.dry_run and (not os.environ.get("CI") or Path(args.metrics_dir) != DEFAULT_METRICS_DIR)


def build_steps(args: argparse.Namespace) -> list[Step]:
    py = sys.executable
    steps: list[Step] = []

    validate_tree = [py, "scripts/validate_tree.py"]
    if args.strict:
        validate_tree.append("--check-algorithm-labels")
    steps.append(Step("Validate Tree nav links and paper coverage", validate_tree))

    steps.append(
        Step(
            "Check that every metadata-backed paper is in the Tree",
            [
                py,
                "scripts/list_unplaced_papers.py",
                "--neighbors",
                "0",
                "--fail-on-missing",
            ],
        )
    )

    if not args.skip_semantic_search:
        semantic_search = [py, "semantic_search/generate_semantic_search_index.py"]
        if args.force:
            semantic_search.append("--force")
        steps.append(Step("Regenerate Semantic Search index, settings, and vector table", semantic_search))

    if not args.skip_map:
        map_data = [py, "map/generate_map_data.py"]
        if args.map_backend != "auto":
            map_data.extend(["--backend", args.map_backend])
        if args.force:
            map_data.append("--force")
        if args.skip_force_layout:
            map_data.append("--skip-force-layout")
        steps.append(Step("Regenerate Map embeddings, layout, map-data.js, and sidecar", map_data))

    if not args.skip_audit:
        steps.append(
            Step(
                "Audit metadata and generated Map/Search assets",
                [py, "scripts/audit_metadata.py", "--severity", args.audit_severity],
            )
        )

    if not args.skip_build:
        mkdocs = [py, "-m", "mkdocs", "build"]
        if args.strict:
            mkdocs.append("--strict")
        steps.append(Step("Build MkDocs site and republish gen-files assets", mkdocs))

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
        help="Enable Tree algorithm-label checks and MkDocs strict mode.",
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
        help="Do not run the final MkDocs build.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the planned commands without running them.",
    )
    parser.add_argument(
        "--metrics-dir",
        type=Path,
        default=DEFAULT_METRICS_DIR,
        help="Directory for append-only build timing records and Chrome Trace JSON.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    steps = build_steps(args)
    run_started_at = utc_now()
    run_start_ns = time.perf_counter_ns()
    timings: list[StepTiming] = []
    returncode = 0
    print(f"Working directory: {KB_DIR}")
    if args.dry_run:
        print("Dry run: no commands will be executed.")

    for index, step in enumerate(steps, start=1):
        timing = run_step(step, index=index, total=len(steps), dry_run=args.dry_run, run_start_ns=run_start_ns)
        timings.append(timing)
        if timing.returncode:
            returncode = timing.returncode
            break

    run_duration_s = (time.perf_counter_ns() - run_start_ns) / 1_000_000_000
    status = "dry-run" if args.dry_run else "success" if returncode == 0 else "failed"
    if should_write_metrics(args):
        write_build_metrics(
            args=args,
            run_started_at=run_started_at,
            run_duration_s=run_duration_s,
            status=status,
            returncode=returncode,
            steps=timings,
        )
    elif not args.dry_run:
        print("\nBuild metrics skipped under CI.")
    if returncode:
        return returncode

    if args.dry_run:
        print("\nDry run complete.")
    else:
        print("\nOffline generated data is refreshed and the consistency checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
