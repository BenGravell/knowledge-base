# Development

This file is the maintainer command reference for the repository.
Run commands from the repository root unless a section says otherwise.

## Development checks

Lint and type-check Python code from the repository root:

```bash
kb lint
kb format-check
kb typecheck
```

Run unit tests from the repository root:

```bash
kb test
```

Install the pre-commit hooks once:

```bash
pre-commit install
```

Run all pre-commit hooks manually:

```bash
pre-commit run --all-files
```

Pre-commit also runs Vulture for high-confidence dead-code findings, Import
Linter for architecture contracts, and Radon for new F-ranked complexity.

## Local generated data

Refresh local generated data and validate that the site is self-consistent from
the repository root:

```bash
kb refresh
```

Use `--force` to recompute cached embeddings, or `--strict` to also fail on
Tree algorithm-label drift and Zensical warnings.

The refresh script prints elapsed seconds for each step and a compact grouped
timing report at the end. For deeper profiling, wrap it with `/usr/bin/time`.

## Streamlit apps

Generate and edit a `metadata.yml` entry from an arXiv ID:

```bash
streamlit run dev_apps/generator_app.py
```

Review Tree and metadata algorithm-label disagreements interactively:

```bash
streamlit run dev_apps/tree_label_review_app.py
```

The Tree Label Review app uses the same suggestions as
`python -m knowledge_base.scripts.suggest_tree_algorithm_labels`.

It shows the current Tree label, metadata `algorithm`, paper context, nearby
`tree.yml` lines, and candidate canonical labels.

Applying a label writes back to `knowledge_base/tree.yml`, the affected
`metadata.yml`, or both, so review the resulting diff before committing.

## Develop Python scripts or site helpers

For a script-only change, run a syntax/import check on the edited file:

```bash
kb py-compile knowledge_base/scripts/refresh_offline_data.py
```

Replace the path with the file you changed. If the change affects Zensical
rendering, navigation, or generated site assets, run:

```bash
kb build
```

## Repo layout

- `knowledge_base/docs/` contains Zensical markdown content, generated paper
  pages, paper metadata, and templates.
- `knowledge_base/docs/papers/` contains paper entries.
- `knowledge_base/docs/templates/metadata.yml` is the paper metadata template.
- `knowledge_base/tree.yml` is the editable Tree nav source.
- `dev_apps/` contains Streamlit apps.
- `knowledge_base/components/` contains browser component source and Map/Search
  adapters.
- `knowledge_base/tree/` contains the Tree model, validation helpers, and Tree
  data generator.
- `knowledge_base/publishing/` contains generated-site asset contracts and
  publishing adapters.
- `knowledge_base/prefill/` contains the metadata prefill workflow and
  source-specific importers.
- `knowledge_base/scripts/` contains maintenance, audit, placement, and prefill entrypoints.
- `knowledge_base/components/map/` contains graph generation and site asset
  publishing.
- `knowledge_base/components/semantic_search/` contains client-side semantic
  search index generation and asset publishing.
- `knowledge_base/utils/` contains small shared helpers.
- `knowledge_base/site/` is generated output. Do not edit it directly.
