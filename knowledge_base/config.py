"""Configuration for the Knowledge Base."""

# All recognised field names for metadata.yml, in canonical order.
VALID_FIELDS: tuple[str, ...] = (
    "title",
    "algorithm",
    "authors",
    "year",
    "source",
    "type",
    "doi",
    "arxiv_id",
    "tags",
    "abstract",
    "summary",
    "link",
    "links_alt",
    "audit_status",
)

# Which of the above must be present (non-null) in every metadata.yml.
# Derived from VALID_FIELDS so membership is structurally enforced.
_REQUIRED: frozenset[str] = frozenset({"title", "authors", "year", "abstract", "type", "audit_status"})
REQUIRED_FIELDS: tuple[str, ...] = tuple(f for f in VALID_FIELDS if f in _REQUIRED)

# Valid values for the "type" field of a research item.
VALID_TYPES: list[str] = [
    "Conference Paper",
    "Journal Paper",
    "Workshop Paper",
    "Preprint",
    "Technical Report",
    "PhD Dissertation",
    "Survey Paper",
    "Blog Post",
    "Other",
]

# Audit status lifecycle for metadata.yml files.
AUDIT_STATUS_FIELD = "audit_status"

# Audit lifecycle statuses (in order):
#  raw       - auto-generated/imported, never manually reviewed
#  partial   - some fields manually reviewed or corrected, but not complete
#  reviewed  - all key fields verified, good summary present
VALID_AUDIT_STATUSES: tuple[str, ...] = ("raw", "partial", "reviewed")

DEFAULT_AUDIT_STATUS = "raw"
