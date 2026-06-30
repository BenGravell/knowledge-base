"""Metadata path move and reference-rewrite helpers."""

import re
import shutil
from pathlib import Path

from rich.console import Console

from knowledge_base.scripts.audit_metadata.support.model import PathFix
from knowledge_base.scripts.audit_metadata.support.slugs import expected_slug
from knowledge_base.scripts.audit_metadata.support.yaml_support import _yaml_safe_load

console = Console(highlight=False)
err_console = Console(stderr=True, highlight=False)


_REFERENCE_SKIP_DIRS = {
    ".git",
    ".mypy_cache",
    ".pytest_cache",
    ".ruff_cache",
    ".venv",
    "__pycache__",
    "node_modules",
    "site",
}
_REFERENCE_TEXT_SUFFIXES = {
    ".css",
    ".html",
    ".js",
    ".json",
    ".md",
    ".py",
    ".txt",
    ".yaml",
    ".yml",
}


def _path_parts(path: Path) -> tuple[Path, str, str] | None:
    parts = path.parts
    try:
        papers_idx = next(i for i, p in enumerate(parts) if p == "papers")
        papers_root = Path(*parts[: papers_idx + 1])
        path_year_str = parts[papers_idx + 1]
        path_slug = "/".join(parts[papers_idx + 2 : -1])
    except (StopIteration, IndexError):
        return None
    if not path_slug:
        return None
    return papers_root, path_year_str, path_slug


def _path_fix_for(path: Path, kb_root: Path) -> PathFix | None:
    try:
        raw = path.read_text(encoding="utf-8")
        data = _yaml_safe_load(raw)
    except Exception:
        return None
    if not isinstance(data, dict):
        return None

    parsed = _path_parts(path)
    if parsed is None:
        return None
    papers_root, path_year_str, path_slug = parsed

    meta_year = data.get("year")
    if isinstance(meta_year, int | str):
        try:
            year = int(meta_year)
        except ValueError:
            if not re.match(r"^\d{4}$", path_year_str):
                return None
            year = int(path_year_str)
    else:
        if not re.match(r"^\d{4}$", path_year_str):
            return None
        year = int(path_year_str)

    if not (1000 <= year <= 9999):
        return None

    title = str(data.get("title") or "").strip()
    authors_raw = data.get("authors")
    authors: list[str] = [str(author) for author in authors_raw] if isinstance(authors_raw, list) else []
    arxiv_id = str(data.get("arxiv_id") or "").strip()
    if not title or not authors:
        return None

    new_slug = expected_slug(year, arxiv_id, title, authors)
    if path_year_str == str(year) and path_slug == new_slug:
        return None

    new_path = papers_root / str(year) / Path(new_slug) / path.name
    old_resolved = path.resolve()
    new_resolved = new_path.resolve()
    if old_resolved == new_resolved:
        return None

    try:
        old_rel = old_resolved.relative_to(kb_root.resolve()).as_posix()
        new_rel = new_resolved.relative_to(kb_root.resolve()).as_posix()
    except ValueError:
        old_rel = path.as_posix()
        new_rel = new_path.as_posix()

    return PathFix(path, new_path, old_rel, new_rel)


def _replacement_search_root(kb_root: Path) -> Path:
    parent = kb_root.resolve().parent
    if kb_root.name == "knowledge_base" and (parent / "README.md").exists():
        return parent
    return kb_root


def _should_scan_reference_file(path: Path) -> bool:
    if any(part in _REFERENCE_SKIP_DIRS for part in path.parts):
        return False
    return path.is_file() and path.suffix.lower() in _REFERENCE_TEXT_SUFFIXES


def _reference_replacements(path_fix: PathFix) -> list[tuple[str, str]]:
    old_abs = path_fix.old_path.resolve().as_posix()
    new_abs = path_fix.new_path.resolve().as_posix()
    old_rel = path_fix.old_rel
    new_rel = path_fix.new_rel
    old_slug = old_rel.removeprefix("docs/papers/").removesuffix("/metadata.yml")
    new_slug = new_rel.removeprefix("docs/papers/").removesuffix("/metadata.yml")
    if "/" in old_slug:
        old_slug = "/".join(old_slug.split("/")[1:])
    if "/" in new_slug:
        new_slug = "/".join(new_slug.split("/")[1:])
    old_id = re.sub(r"[^a-zA-Z0-9]+", "_", old_slug.lower()).strip("_")
    new_id = re.sub(r"[^a-zA-Z0-9]+", "_", new_slug.lower()).strip("_")
    replacements = [
        (old_abs, new_abs),
        (old_rel, new_rel),
    ]
    if old_id and new_id and old_id != new_id:
        replacements.extend(
            [
                (f"papers/{old_id}.md", f"papers/{new_id}.md"),
                (old_id, new_id),
            ]
        )
    if not old_rel.startswith("./"):
        replacements.append((f"./{old_rel}", f"./{new_rel}"))
    if old_rel.startswith("docs/papers/"):
        replacements.append(
            (
                f"../knowledge_base/{old_rel}",
                f"../knowledge_base/{new_rel}",
            )
        )
    return replacements


def _rewrite_path_references(path_fix: PathFix, kb_root: Path) -> int:
    changed = 0
    search_root = _replacement_search_root(kb_root)
    replacements = _reference_replacements(path_fix)
    for candidate in search_root.rglob("*"):
        if not _should_scan_reference_file(candidate):
            continue
        try:
            raw = candidate.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        new_raw = raw
        for old, new in replacements:
            new_raw = new_raw.replace(old, new)
        if new_raw == raw:
            continue
        candidate.write_text(new_raw, encoding="utf-8")
        changed += 1
    return changed


def _prune_empty_dirs(start: Path, stop: Path) -> None:
    current = start
    stop = stop.resolve()
    while current.resolve() != stop and current.exists():
        try:
            current.rmdir()
        except OSError:
            return
        current = current.parent


def _apply_path_fix(path_fix: PathFix, kb_root: Path) -> bool:
    old_dir = path_fix.old_path.parent
    new_dir = path_fix.new_path.parent
    if path_fix.new_path.exists():
        err_console.print(
            f"[red]Error fixing path {path_fix.old_path}:[/] destination already exists: {path_fix.new_path}"
        )
        return False

    try:
        new_dir.parent.mkdir(parents=True, exist_ok=True)
        moved_whole_dir = not new_dir.exists()
        if new_dir.exists():
            shutil.move(str(path_fix.old_path), str(path_fix.new_path))
        else:
            shutil.move(str(old_dir), str(new_dir))
        references_changed = _rewrite_path_references(path_fix, kb_root)
        parsed = _path_parts(path_fix.old_path)
        if parsed is not None:
            papers_root, path_year_str, _ = parsed
            prune_start = old_dir.parent if moved_whole_dir else old_dir
            _prune_empty_dirs(prune_start, papers_root / path_year_str)
        console.print(f"[green]Moved:[/] {path_fix.old_rel} [green]->[/] {path_fix.new_rel}")
        console.print(f"  updated references in {references_changed} file(s)")
        return True
    except Exception as exc:
        err_console.print(f"[red]Error fixing path {path_fix.old_path}:[/] {exc}")
        return False
