"""Configuration for the Knowledge Base."""

from pathlib import Path

# Stable path roots — import these instead of computing via __file__ chains.
KB_DIR: Path = Path(__file__).resolve().parent  # knowledge_base/
REPO_ROOT: Path = Path(__file__).resolve().parents[1]  # repository root
PAPERS_DIR: Path = KB_DIR / "docs" / "papers"
