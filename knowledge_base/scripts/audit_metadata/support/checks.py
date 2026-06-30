"""Check-name constants shared by the metadata auditor CLI and rules."""

CHECK_UNKNOWN = "unknown"
CHECK_REQUIRED = "required"
CHECK_TITLE = "title"
CHECK_ALGORITHM = "algorithm"
CHECK_AUTHORS = "authors"
CHECK_TAGS = "tags"
CHECK_YEAR = "year"
CHECK_ARXIV = "arxiv"
CHECK_ABSTRACT = "abstract"
CHECK_ESCAPE = "escape"
CHECK_URL = "url"
CHECK_MULTILINE = "multiline"
CHECK_SOURCE = "source"
CHECK_TYPE = "type"
CHECK_STATUS = "status"
CHECK_PATH = "path"
CHECK_SUMMARY = "summary"
CHECK_OPTIONAL = "optional"
CHECK_DASH = "dash"
CHECK_WHITESPACE = "whitespace"
CHECKS: tuple[str, ...] = (
    CHECK_UNKNOWN,
    CHECK_REQUIRED,
    CHECK_TITLE,
    CHECK_ALGORITHM,
    CHECK_AUTHORS,
    CHECK_TAGS,
    CHECK_YEAR,
    CHECK_ARXIV,
    CHECK_ABSTRACT,
    CHECK_ESCAPE,
    CHECK_URL,
    CHECK_MULTILINE,
    CHECK_SOURCE,
    CHECK_TYPE,
    CHECK_STATUS,
    CHECK_PATH,
    CHECK_SUMMARY,
    CHECK_OPTIONAL,
    CHECK_DASH,
    CHECK_WHITESPACE,
)
