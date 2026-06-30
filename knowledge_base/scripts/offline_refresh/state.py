"""Hot-start state and freshness checks."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections.abc import Callable, Sequence
from pathlib import Path


def site_has_paper_pages(kb_dir: Path) -> bool:
    papers_dir = kb_dir / "site" / "papers"
    return papers_dir.exists() and next(papers_dir.rglob("index.html"), None) is not None


def state_fingerprint_paths(repo_root: Path, status_paths: Sequence[str]) -> tuple[list[Path], str | None]:
    tracked = subprocess.run(
        ["git", "ls-files", "--cached", "--", *status_paths],
        cwd=repo_root,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
    )
    if tracked.returncode:
        return [], "git ls-files failed"

    return sorted(repo_root / line for line in tracked.stdout.splitlines() if line), None


def refresh_state_fingerprint(
    repo_root: Path,
    status_paths: Sequence[str],
    state_version: int,
) -> tuple[dict[str, object], str | None]:
    paths, error = state_fingerprint_paths(repo_root, status_paths)
    if error:
        return {}, error

    digest = hashlib.sha256()
    file_count = 0
    missing_count = 0
    byte_count = 0
    for path in paths:
        rel_path = path.relative_to(repo_root).as_posix()
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
        "version": state_version,
        "digest": digest.hexdigest(),
        "file_count": file_count,
        "missing_count": missing_count,
        "byte_count": byte_count,
    }, None


def refresh_state_status(
    state_path: Path,
    repo_root: Path,
    status_paths: Sequence[str],
    state_version: int,
) -> tuple[str, str]:
    if not state_path.exists():
        return "missing", "no refresh state stamp"
    try:
        saved = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return "stale", f"refresh state stamp is unreadable: {exc}"
    current, error = refresh_state_fingerprint(repo_root, status_paths, state_version)
    if error:
        return "stale", error
    if saved == current:
        return "match", "refresh state stamp matches current tracked files"
    return "stale", "refresh state stamp is stale"


def write_refresh_state(
    state_path: Path,
    repo_root: Path,
    status_paths: Sequence[str],
    state_version: int,
) -> str | None:
    state, error = refresh_state_fingerprint(repo_root, status_paths, state_version)
    if error:
        return error
    state_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = state_path.with_suffix(".json.tmp")
    try:
        temporary.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        temporary.replace(state_path)
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


def hot_start_fast_path(
    args: argparse.Namespace,
    *,
    repo_root: Path,
    status_paths: Sequence[str],
    required_files: Sequence[Path],
    site_has_paper_pages: Callable[[], bool],
    refresh_state_status: Callable[[], tuple[str, str]],
) -> tuple[bool, str]:
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

    missing = [path for path in required_files if not path.exists()]
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
        ["git", "status", "--porcelain=v1", "--untracked-files=no", "--", *status_paths],
        cwd=repo_root,
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
