# Knowledge Base Context

This context names the project-specific concepts used by architecture work in the knowledge base.

## Language

### Catalog

Canonical in-process view of a collection of metadata-backed entries in `knowledge_base/catalog.py`: a `Catalog` containing ordered `Entry` objects, indexed by stable ID, metadata path, and generated path.

_Avoid_: paper loader, metadata helper, papers dict, metadata index

### Entry

One metadata-backed entry in the `Catalog`.

It owns stable IDs, cleaned metadata, common derived fields, stable local links such as detail, Tree, Map, Timeline, and Search URLs, and embedding text as the canonical answer to what text represents a paper; generated-page presentation link sections, embedding vectors, Map layout, Search vector output, and Tree branch output remain adapter-specific projections.
Author, source, and tag normalization stays adapter-specific because the normalization databases carry audit policy.

Every field needed by adapters belongs on the `Entry` interface from day one; do not preserve raw metadata as a migration escape hatch.

_Avoid_: Item, paper dict, metadata row
