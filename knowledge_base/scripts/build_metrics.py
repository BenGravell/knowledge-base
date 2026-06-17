"""Small JSONL/trace writer for local build timing history."""

from __future__ import annotations

import argparse
import json
import os
import platform
import shlex
import subprocess
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

KB_DIR = Path(__file__).resolve().parents[1]
REPO_ROOT = KB_DIR.parent
DEFAULT_METRICS_DIR = KB_DIR / ".build-metrics"


@dataclass(frozen=True)
class StepTiming:
    name: str
    command: list[str]
    started_at: str
    start_offset_s: float
    duration_s: float
    returncode: int
    error: str | None = None


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def utc_stamp() -> str:
    return utc_now().isoformat(timespec="milliseconds").replace("+00:00", "Z")


def git_text(args: list[str]) -> str | None:
    result = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    if result.returncode:
        return None
    return result.stdout.strip()


def total_memory_mb() -> int | None:
    meminfo = Path("/proc/meminfo")
    if not meminfo.exists():
        return None
    for line in meminfo.read_text(encoding="utf-8").splitlines():
        if line.startswith("MemTotal:"):
            return int(line.split()[1]) // 1024
    return None


def record_metadata() -> dict[str, object]:
    git_status = git_text(["status", "--short"])
    return {
        "timestamp_utc": utc_stamp(),
        "git": {
            "commit": git_text(["rev-parse", "HEAD"]),
            "short_commit": git_text(["rev-parse", "--short", "HEAD"]),
            "branch": git_text(["branch", "--show-current"]),
            "dirty": bool(git_status),
        },
        "machine": {
            "node": platform.node(),
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine(),
            "processor": platform.processor(),
            "cpu_count": os.cpu_count(),
            "memory_mb": total_memory_mb(),
        },
        "python": {
            "version": platform.python_version(),
            "executable": sys.executable,
        },
    }


def json_args(args: argparse.Namespace) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in vars(args).items():
        result[key] = str(value) if isinstance(value, Path) else value
    return result


def resolved_metrics_dir(path: Path) -> Path:
    return path if path.is_absolute() else KB_DIR / path


def trace_payload(record: dict[str, object]) -> dict[str, object]:
    steps = record.get("steps")
    if not isinstance(steps, list):
        steps = []
    trace_events = [
        {
            "name": step["name"],
            "cat": "refresh_offline_data",
            "ph": "X",
            "ts": int(step["start_offset_s"] * 1_000_000),
            "dur": int(step["duration_s"] * 1_000_000),
            "pid": 1,
            "tid": 1,
            "args": {
                "command": shlex.join(step["command"]),
                "returncode": step["returncode"],
                "error": step["error"],
            },
        }
        for step in steps
        if isinstance(step, dict)
    ]
    return {
        "displayTimeUnit": "ms",
        "traceEvents": trace_events,
        "metadata": {
            "run_id": record["run_id"],
            "status": record["status"],
            "duration_s": record["duration_s"],
            "git": record["git"],
            "machine": record["machine"],
        },
    }


def write_build_metrics(
    *,
    args: argparse.Namespace,
    run_started_at: datetime,
    run_duration_s: float,
    status: str,
    returncode: int,
    steps: list[StepTiming],
) -> dict[str, object]:
    metadata = record_metadata()
    short_commit = metadata["git"]["short_commit"] if isinstance(metadata["git"], dict) else None
    run_id = f"{run_started_at:%Y%m%dT%H%M%SZ}-{short_commit or 'nogit'}-{os.getpid()}"
    metrics_dir = resolved_metrics_dir(args.metrics_dir)
    trace_name = f"{run_id}.trace.json"
    record = {
        "schema": "knowledge-base-build-metrics-v1",
        "run_id": run_id,
        "kind": "refresh_offline_data",
        "started_at": run_started_at.isoformat(timespec="milliseconds").replace("+00:00", "Z"),
        "ended_at": utc_stamp(),
        "duration_s": run_duration_s,
        "status": status,
        "returncode": returncode,
        "command": [sys.executable, *sys.argv],
        "args": json_args(args),
        "git": metadata["git"],
        "machine": metadata["machine"],
        "python": metadata["python"],
        "steps": [asdict(step) for step in steps],
        "trace_file": trace_name,
    }

    metrics_dir.mkdir(parents=True, exist_ok=True)
    history_path = metrics_dir / "builds.jsonl"
    trace_path = metrics_dir / trace_name
    with history_path.open("a", encoding="utf-8") as out:
        out.write(json.dumps(record, sort_keys=True, separators=(",", ":")) + "\n")
    trace_path.write_text(json.dumps(trace_payload(record), separators=(",", ":")), encoding="utf-8")
    open_trace = shlex.join([sys.executable, str(KB_DIR / "scripts" / "open_build_trace.py"), str(trace_path)])
    print(f"\nBuild metrics: {history_path}")
    print(f"Trace file: {trace_path} (Perfetto trace)")
    print(f"Open trace UI: {open_trace}")
    return record
