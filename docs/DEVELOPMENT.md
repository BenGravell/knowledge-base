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
poetry shell
cd knowledge_base
mkdocs serve
```

Build the site from `knowledge_base/`:

```bash
mkdocs build
```

Deploy to GitHub Pages from `knowledge_base/`:

```bash
mkdocs gh-deploy
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
`knowledge_base/`:

```bash
python scripts/refresh_offline_data.py
```

Use `--force` to recompute cached embeddings, or `--strict` to also fail on
Tree algorithm-label drift and MkDocs warnings.

Each non-dry-run local refresh appends timing metadata to
`knowledge_base/.build-metrics/builds.jsonl` and writes a Chrome Trace JSON
file beside it for phase drilldown. The script prints an `Open trace UI`
command that serves a local Perfetto UI and opens the trace in it. Under
`CI=true`, the default local metrics write is skipped unless a custom
`--metrics-dir` is passed.

Build a pinned local Perfetto UI once and point the opener at its built
`ui/out/dist` directory:

```bash
git clone --depth 1 --branch v56.1 https://github.com/google/perfetto.git knowledge_base/.tools/perfetto-v56.1
(cd knowledge_base/.tools/perfetto-v56.1 && tools/install-build-deps --ui && ui/build)
ln -sfn perfetto-v56.1/ui/out/dist knowledge_base/.tools/perfetto-ui
```

## Streamlit apps

Generate and edit a `metadata.yml` entry from an arXiv ID from `knowledge_base/`:

```bash
streamlit run apps/generator_app.py
```

Run the metadata analyzer from `knowledge_base/`:

```bash
streamlit run apps/analyzer_app.py
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
