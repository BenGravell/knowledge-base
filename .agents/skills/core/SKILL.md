---
name: core
description: Shared project context for the knowledge-base repository. Use before editing or auditing MkDocs content, paper metadata, tree navigation, map scripts, or repository agent workflows in this personal publications knowledge base.
---

# Core

## Purpose

Use this skill first for repository context. Other knowledge-base skills depend on it.

## Project Shape

This is a personal knowledge base of publications, distilled notes, and paper summaries, published as a static site via MkDocs.

Important paths:

- `knowledge_base/docs/`: MkDocs markdown content, generated paper pages, paper metadata, and templates.
- `knowledge_base/docs/papers/`: paper entries. New entries go here.
- `knowledge_base/docs/templates/metadata.yml`: template for paper metadata.
- `knowledge_base/tree.yml`: editable Tree nav source injected into `mkdocs.yml` through the local `tree-nav` plugin.
- `knowledge_base/map/`: embedding, UMAP, and graph generation scripts.
- `knowledge_base/scripts/`: audit and utility scripts. Source-specific prefill entrypoints live in `knowledge_base/scripts/prefill/`.
- `knowledge_base/site/`: generated site output. Do not edit it directly.
- `todo/papers/`: source-specific paper URL tracking lists.

## Commands

Run repository commands from the repo root unless a command says otherwise.

Install and shell:

```bash
poetry install
poetry shell
```

Run MkDocs commands from `knowledge_base/`:

```bash
mkdocs serve
mkdocs build
mkdocs gh-deploy
```

Map utilities:

```bash
python map/generate_map_data.py
python map/preview_map.py
```

Human-oriented dev tools:

```bash
python scripts/audit_metadata.py
streamlit run apps/analyzer_app.py
streamlit run apps/generator_app.py
```

## Conventions

- Python is `>=3.11, <3.14` and managed with Poetry.
- New knowledge entries go under `knowledge_base/docs/` following the structure of existing files.
- Paper URL lists live under `todo/papers/<SOURCE>.md`.
- Source-specific prefill scripts live under `knowledge_base/scripts/prefill/<source>.py`.
- Valid metadata fields, item types, and audit statuses are defined in `knowledge_base/config.py`.
- Do not promote `audit_status` to `reviewed`. Agents may set it to `partial` after meaningful manual review or correction.
- There is no general test suite.
- Do not run programmatic tests except when a task skill explicitly requires a verification command or UX controls changed.
- When UX controls changed, verify with `mkdocs build` from `knowledge_base/` and check for warnings.
