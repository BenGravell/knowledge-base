"""Offline primary-link identity checks; mismatches require source verification."""

from pathlib import Path
from typing import Any
from urllib.parse import unquote, urlparse

from knowledge_base.scripts.audit_metadata.support.model import RULE_IDENTITY, Issue
from knowledge_base.scripts.audit_metadata.support.slugs import is_valid_arxiv_id
from knowledge_base.utils.arxiv_ids import normalize_arxiv_id


def find_identity_issues(path: Path, data: dict[str, Any]) -> list[Issue]:
    # Alternate links can legitimately identify separately registered versions.
    link = str(data.get("link") or "").strip()
    parsed = urlparse(link)
    host = (parsed.hostname or "").lower().removeprefix("www.")
    doi = str(data.get("doi") or "").strip().casefold()
    expected_doi = None
    evidence = "primary DOI URL"
    if host in {"doi.org", "dx.doi.org"}:
        expected_doi = unquote(parsed.path).lstrip("/")
    if doi and expected_doi and doi != expected_doi.casefold():
        return [
            Issue(
                path,
                "doi",
                f"Identity mismatch: stored {doi!r}, {evidence} indicates {expected_doi!r}",
                rule=RULE_IDENTITY,
            )
        ]

    if host == "arxiv.org" and parsed.path.startswith(("/abs/", "/pdf/", "/html/")):
        linked_id = normalize_arxiv_id(link)
        stored_id = normalize_arxiv_id(data.get("arxiv_id"))
        if is_valid_arxiv_id(linked_id) and is_valid_arxiv_id(stored_id) and linked_id != stored_id:
            return [
                Issue(
                    path,
                    "arxiv_id",
                    f"Identity mismatch: stored {stored_id!r}, primary arXiv URL identifies {linked_id!r}",
                    rule=RULE_IDENTITY,
                )
            ]
    return []
