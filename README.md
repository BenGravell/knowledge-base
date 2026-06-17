# knowledge-base

Distilled knowledge on a variety of topics.

The public site is published at
<https://bengravell.github.io/knowledge-base/>.

## Repo layout

- `knowledge_base/docs/` contains the MkDocs source pages and paper metadata.
- `knowledge_base/docs/papers/**/metadata.yml` drives generated paper pages.
- `knowledge_base/tree.yml` is the editable Tree navigation and classification source.
- `knowledge_base/apps/` contains Streamlit apps.
- `knowledge_base/scripts/` contains maintenance, audit, placement, and prefill entrypoints.
- `knowledge_base/map/` contains graph generation, preview, and MkDocs asset publishing.
- `knowledge_base/semantic_search/` contains client-side semantic search index generation and asset publishing.
- `knowledge_base/tree/` contains the Tree model, validation helpers, MkDocs nav plugin, and Tree data generator.
- `knowledge_base/utils/` contains shared DOI, arXiv, and prefill helpers.
- Map, Timeline, Tree, and Semantic Search are derived from metadata plus Tree placement.
- `todo/PAPERS_FUNNEL.md` and `todo/papers/*.md` hold incoming paper URLs before ingest.
- `docs/` contains repository docs for maintainers; it is not the published site content.
  - [Setup and development](docs/DEVELOPMENT.md)
  - [Content ingest workflow](docs/CONTENT_WORKFLOW.md)
  - [Site generation and derived features](docs/SITE_GENERATION.md)

## Spin up from scratch

Prerequisites: Python `>=3.11,<3.14` and Poetry.

```bash
git clone https://github.com/BenGravell/knowledge-base.git
cd knowledge-base
poetry install
poetry run mkdocs serve -f knowledge_base/mkdocs.yml
```

Open the URL printed by MkDocs, usually <http://127.0.0.1:8000/>.

## Common workflows

### Serve the site locally

Run `poetry run mkdocs serve -f knowledge_base/mkdocs.yml` from the repo root.

### Add papers

Put URLs in `todo/PAPERS_FUNNEL.md`, route them, prefill metadata, audit it, then place entries in `knowledge_base/tree.yml`.

### Develop Python scripts or site helpers

Work from the repo root, use Poetry, and run the narrowest check that covers the change.

### Refresh offline data

If local generated data is stale, refresh it from the repo root:

```bash
poetry run python knowledge_base/scripts/refresh_offline_data.py
```

### Deploy

Run `poetry run mkdocs gh-deploy -f knowledge_base/mkdocs.yml` from the repo root.
