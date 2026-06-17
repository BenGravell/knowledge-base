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

### Audit Rule

Stable metadata-audit fact behind a reported issue: rule code, field, optional list index, severity, human message, and suggestion.
Fix routing should use the Audit Rule identity and indexed location rather than parsing prose messages.

_Avoid_: message prefix, fix heuristic, regex-routed audit case

### Tree

Human-maintained hierarchical navigation and classification source rooted at `knowledge_base/tree.yml`.
It names branches and leaves that locate metadata-backed entries and supporting pages in the public knowledge base.

_Avoid_: MkDocs nav, category list, site menu

### Tree Placement

Normalized Tree fact that locates an `Entry` at a leaf: branch path, leaf label, source, and generated paper ID when the leaf is metadata-backed.
Map categories, Timeline groupings, validation coverage, and placement reports are projections of Tree Placement rather than independent category models.

_Avoid_: category info, nav row, paper category, super/category/subcategory tuple

### Tree Model

Canonical in-process view of the `Tree`, containing ordered branches, leaves, source normalization, Tree Placement lookup, and Tree distance/order facts.
Browser Tree data, Map categories, Timeline order, validation reports, and Tree scripts remain adapter-specific projections.

_Avoid_: nav parser, tree helper, tree.yml wrapper

### Embedding Workbench

Canonical in-process module for refreshing paper embedding caches from ordered embedding rows: stable paper ID, embedding text, and content hash.
It owns cache loading, cache shape normalization, model-change rebuilds, stale paper pruning, changed-row detection, embedding writeback, and ordered matrix assembly.
Map layout, Semantic Search vector output, browser settings, and generated asset publication remain adapter-specific projections.

_Avoid_: map cache helper, semantic search cache helper, embedding script glue
