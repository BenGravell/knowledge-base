# Setup and development

This file is the maintainer command reference for the repository. Run commands
from the repository root unless a section says otherwise.

## Fresh checkout

Prerequisites:

- Python `>=3.11,<3.14`
- Poetry

```bash
git clone https://github.com/BenGravell/knowledge-base.git
cd knowledge-base
poetry install
poetry run mkdocs serve -f knowledge_base/mkdocs.yml
```

Build the site from the repository root:

```bash
poetry run mkdocs build -f knowledge_base/mkdocs.yml
```

Deploy to GitHub Pages from the repository root:

```bash
poetry run mkdocs gh-deploy -f knowledge_base/mkdocs.yml
```

## Development checks

Lint and type-check Python code from the repository root:

```bash
poetry run ruff check knowledge_base tests
poetry run ruff format --check knowledge_base tests
poetry run pyrefly check
```

Run unit tests from the repository root:

```bash
poetry run python -m unittest discover -s tests -p 'test_*.py'
```

Install the pre-commit hooks once:

```bash
pre-commit install
```

Run all pre-commit hooks manually:

```bash
pre-commit run --all-files
```

## Local generated data

Refresh local generated data and validate that the site is self-consistent from
the repository root:

```bash
poetry run python knowledge_base/scripts/refresh_offline_data.py
```

Use `--force` to recompute cached embeddings, or `--strict` to also fail on
Tree algorithm-label drift and MkDocs warnings.

The refresh script prints elapsed seconds for each step and a compact grouped
timing report at the end. For deeper profiling, wrap it with `/usr/bin/time`.

## Streamlit apps

Generate and edit a `metadata.yml` entry from an arXiv ID:

```bash
poetry run streamlit run knowledge_base/apps/generator_app.py
```

Run the metadata analyzer:

```bash
poetry run streamlit run knowledge_base/apps/analyzer_app.py
```

## Repo layout

- `knowledge_base/docs/` contains MkDocs markdown content, generated paper pages, paper metadata, and templates.
- `knowledge_base/docs/papers/` contains paper entries.
- `knowledge_base/docs/templates/metadata.yml` is the paper metadata template.
- `knowledge_base/tree.yml` is the editable Tree nav source.
- `knowledge_base/apps/` contains Streamlit apps.
- `knowledge_base/scripts/` contains maintenance, audit, placement, and prefill entrypoints.
- `knowledge_base/scripts/prefill/` contains source-specific paper metadata importers.
- `knowledge_base/map/` contains graph generation, preview, and MkDocs asset publishing.
- `knowledge_base/semantic_search/` contains client-side semantic search index generation and asset publishing.
- `knowledge_base/tree/` contains the Tree model, validation helpers, MkDocs nav plugin, and Tree data generator.
- `knowledge_base/utils/` contains shared DOI, arXiv, and prefill helpers.
- `knowledge_base/site/` is generated output. Do not edit it directly.
