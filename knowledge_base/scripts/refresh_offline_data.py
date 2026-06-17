"""Refresh local generated data needed by the static knowledge-base site.

Run from the repository root:

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

KB_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = KB_DIR.parent


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


def subprocess_env() -> dict[str, str]:
    env = os.environ.copy()
    pythonpath_parts = [str(REPO_ROOT)]
    if env.get("PYTHONPATH"):
        pythonpath_parts.append(env["PYTHONPATH"])
    env["PYTHONPATH"] = os.pathsep.join(pythonpath_parts)
    return env


def site_has_paper_pages() -> bool:
    papers_dir = KB_DIR / "site" / "papers"
    return papers_dir.exists() and next(papers_dir.rglob("index.html"), None) is not None


def run_step(step: Step, *, index: int, total: int, dry_run: bool) -> StepResult:
    print(f"\n[{index}/{total}] {step.name}", flush=True)
    print(f"$ {format_command(step.command)}", flush=True)
    if dry_run:
        return StepResult(step, 0.0, 0)

    step_start_ns = time.perf_counter_ns()
    error = None
    try:
        result = subprocess.run(step.command, cwd=REPO_ROOT, env=subprocess_env(), check=False)
        returncode = result.returncode
    except OSError as exc:
        returncode = 127
        error = str(exc)
    elapsed_s = (time.perf_counter_ns() - step_start_ns) / 1_000_000_000
    if error:
        print(f"\nStep failed after {format_duration(elapsed_s)}: {step.name}: {error}", file=sys.stderr)
    elif returncode:
        print(f"\nStep failed after {format_duration(elapsed_s)}: {step.name}", file=sys.stderr)
    else:
        print(f"Done in {format_duration(elapsed_s)}.", flush=True)
    return StepResult(step, elapsed_s, returncode)


def print_timing_report(results: list[StepResult], total_s: float, *, failed: bool) -> None:
    print("\nTiming report" + (" (failed)" if failed else ""))
    for group in dict.fromkeys(result.step.group for result in results):
        group_results = [result for result in results if result.step.group == group]
        print(f"  {group}: {format_duration(sum(result.duration_s for result in group_results))}")
        for result in group_results:
            status = " failed" if result.returncode else ""
            print(f"    - {result.step.label}: {format_duration(result.duration_s)}{status}")
    print(f"  Total: {format_duration(total_s)}")


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
        semantic_search = [py, "knowledge_base/semantic_search/generate_semantic_search_index.py"]
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
        map_data = [py, "knowledge_base/map/generate_map_data.py"]
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
        use_full_build = args.full_build or not site_has_paper_pages()
        mkdocs_config = "knowledge_base/mkdocs.yml" if use_full_build else "knowledge_base/mkdocs.refresh.yml"
        mkdocs = [py, "-m", "mkdocs", "build", "-f", mkdocs_config]
        if not use_full_build:
            mkdocs.extend(["--dirty", "--quiet"])
        if args.strict:
            mkdocs.append("--strict")
        label = "MkDocs full build" if use_full_build else "MkDocs refresh build"
        name = "Build full MkDocs site" if use_full_build else "Refresh MkDocs generated assets"
        steps.append(Step("Verify", label, name, mkdocs))

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
        help="Do not run the final MkDocs asset refresh build.",
    )
    parser.add_argument(
        "--full-build",
        action="store_true",
        help="Render every MkDocs page, including generated paper detail pages.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the planned commands without running them.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    steps = build_steps(args)
    run_start_ns = time.perf_counter_ns()
    returncode = 0
    results: list[StepResult] = []
    print(f"Working directory: {REPO_ROOT}", flush=True)
    if args.dry_run:
        print("Dry run: no commands will be executed.", flush=True)

    for index, step in enumerate(steps, start=1):
        result = run_step(step, index=index, total=len(steps), dry_run=args.dry_run)
        results.append(result)
        returncode = result.returncode
        if returncode:
            break

    run_duration_s = (time.perf_counter_ns() - run_start_ns) / 1_000_000_000
    if not args.dry_run:
        print_timing_report(results, run_duration_s, failed=bool(returncode))
    if returncode:
        return returncode

    if args.dry_run:
        print("\nDry run complete.")
    else:
        print("\nOffline generated data is refreshed and the consistency checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
