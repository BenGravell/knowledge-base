"""Project Catalog entries into Map pipeline rows."""

from __future__ import annotations

from typing import Any

from knowledge_base.catalog import Catalog
from knowledge_base.components.map.pipeline.settings import METADATA_ROOT, UNCATEGORIZED_CATEGORY
from knowledge_base.embedding_workbench import EmbeddingRow, embedding_rows_for_entry
from knowledge_base.progress import emit_progress


def collect_map_papers(
    paper_to_category: dict[str, dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[EmbeddingRow]]:
    papers: list[dict[str, Any]] = []
    rows: list[EmbeddingRow] = []
    catalog = Catalog.from_metadata_root(METADATA_ROOT, write_embedding_input_sidecars=True)

    for index, entry in enumerate(catalog.entries, start=1):
        rows.extend(embedding_rows_for_entry(entry))
        cat_info = paper_to_category.get(
            entry.id,
            {
                "super_category": None,
                "category": UNCATEGORIZED_CATEGORY,
                "sub_category": None,
                "nav_path": [UNCATEGORIZED_CATEGORY],
            },
        )
        papers.append(
            {
                "id": entry.id,
                "title": entry.title,
                "label": entry.label,
                "authors": list(entry.author_last_names[:3]),
                "year": entry.year,
                "item_type": entry.type or "Unspecified",
                "super_category": cat_info["super_category"],
                "category": cat_info["category"],
                "sub_category": cat_info["sub_category"],
                "nav_path": cat_info.get("nav_path") or [cat_info["category"]],
                "tags": list(entry.tags),
                "summary": entry.summary,
                "abstract": entry.abstract,
                "link": entry.primary_link,
                "embed_text": entry.embedding_text,
                "hash": entry.embedding_hash,
            }
        )
        emit_progress(index, len(catalog.entries), "Build map rows", every=100)

    return papers, rows
