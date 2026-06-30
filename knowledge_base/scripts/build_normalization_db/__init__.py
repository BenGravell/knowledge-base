"""Import-compatible surface for normalization database generation."""

from knowledge_base.scripts.build_normalization_db.authors import (
    author_quality,
    build_author_entries,
    choose_author_canonical,
    merge_aliases,
)
from knowledge_base.scripts.build_normalization_db.cli import main
from knowledge_base.scripts.build_normalization_db.collect import (
    as_list,
    collect_values,
    existing_entries,
    load_metadata,
)
from knowledge_base.scripts.build_normalization_db.config import (
    AUTHORS_DB,
    AUTHORS_HEADER,
    METADATA_ROOT,
    NORMALIZATION_DIR,
    SOURCES_DB,
    SOURCES_HEADER,
    TAGS_DB,
    TAGS_HEADER,
)
from knowledge_base.scripts.build_normalization_db.sources import build_source_entries
from knowledge_base.scripts.build_normalization_db.tags import (
    _is_short_acronym_tag,
    _tag_canonical_score,
    build_tag_entries,
    choose_tag_canonical,
)

__all__ = [
    "AUTHORS_DB",
    "AUTHORS_HEADER",
    "METADATA_ROOT",
    "NORMALIZATION_DIR",
    "SOURCES_DB",
    "SOURCES_HEADER",
    "TAGS_DB",
    "TAGS_HEADER",
    "_is_short_acronym_tag",
    "_tag_canonical_score",
    "as_list",
    "author_quality",
    "build_author_entries",
    "build_source_entries",
    "build_tag_entries",
    "choose_author_canonical",
    "choose_tag_canonical",
    "collect_values",
    "existing_entries",
    "load_metadata",
    "main",
    "merge_aliases",
]
