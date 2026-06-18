# knowledge-base

Distilled knowledge on a variety of topics.

The public site is published at
<https://bengravell.github.io/knowledge-base/>.

## Repo layout

- `knowledge_base/` contains the published site source and supporting tools.
  - `docs/` contains the Zensical source pages and paper metadata.
    - `papers/**/metadata.yml` drives generated paper pages.
    - `papers/**/embed_text.md` may contain cleaned arXiv/ar5iv HTML conversions for embeddings.
  - `tree.yml` is the editable Tree navigation and classification source.
  - `apps/` contains Streamlit apps.
  - `scripts/` contains maintenance, audit, placement, and prefill entrypoints.
  - `map/` contains graph generation, preview, and site asset publishing.
  - `semantic_search/` contains client-side semantic search index generation and asset publishing.
  - `tree/` contains the Tree model, validation helpers, and Tree data generator.
  - `utils/` contains shared DOI, arXiv, and prefill helpers.
  - `map/`, `tree/`, and `semantic_search/` derive Map, Timeline, Tree, and Semantic Search from `docs/papers/**/metadata.yml` plus `tree.yml`.
- `todo/PAPERS_FUNNEL.md` and `todo/papers/*.md` hold incoming paper URLs before ingest.
- `docs/` contains repository docs for maintainers; it is not the published site content.
  - [Setup and development](docs/DEVELOPMENT.md)
  - [Content ingest workflow](docs/CONTENT_WORKFLOW.md)
  - [Site generation and derived features](docs/SITE_GENERATION.md)

## Spin up from scratch

Needs `git` plus `curl` or `wget`.
No Python or global Pixi install is required.
The `./dev` wrapper installs Pixi locally on first use, then uses the checked-in `pixi.lock`.

```bash
git clone https://github.com/BenGravell/knowledge-base.git
cd knowledge-base
./dev install
eval "$(./dev shell-hook)"
kb serve
```

Run `eval "$(./dev shell-hook)"` once per terminal, or let VS Code use the configured Pixi interpreter.

Open the URL printed by Zensical, usually <http://127.0.0.1:8000/>.

## Common workflows

### Serve the site locally

From the repo root, run

```bash
kb serve
```

### Add papers

Put URLs in `todo/PAPERS_FUNNEL.md`, route them, prefill metadata, audit it, then place entries in `knowledge_base/tree.yml`.

```bash
# Route URLs into todo/papers/<SOURCE>.md or todo/PAPERS_MISC.md.
python knowledge_base/scripts/funnel_papers.py

# List prefill sources, then run the populated ones.
python -m knowledge_base.scripts.prefill --help
python -m knowledge_base.scripts.prefill arxiv
python -m knowledge_base.scripts.prefill openreview

# Audit raw metadata after prefill and fix reported files.
python knowledge_base/scripts/audit_metadata.py knowledge_base --audit-status raw

# Find unplaced papers, edit knowledge_base/tree.yml, then verify.
python knowledge_base/scripts/list_unplaced_papers.py --neighbors 3
python knowledge_base/scripts/list_unplaced_papers.py --neighbors 0 --fail-on-missing
kb build
```

Use the source names printed by the prefill help, such as `ieee`, `mlr`, or `taylor_francis`; replace the example source commands with whichever `todo/papers/*.md` files the funnel populated.

### Ingest arXiv embed text

Some paper entries can have an optional `embed_text.md` sidecar next to `metadata.yml`.
These sidecars are cleaned Markdown conversions of arXiv/ar5iv HTML for embedding and agentic search only.
They are not the canonical e-print, PDF, or LaTeX source of truth, and this repo intentionally does not store PDFs, LaTeX source archives, images, or other rich paper assets.
Reuse of paper text remains governed by each paper's original license and rights holder terms.

Run the ingest script from the repo root:

```bash
python knowledge_base/scripts/ingest_arxiv_full_text.py --id 2402.08954
```

The script requires `pandoc` on `PATH`, skips existing sidecars unless `--force` is passed, and probes only entries with `arxiv_id`. It strips author blocks, references, source chrome, images, and obvious table/math noise before writing `embed_text.md`.

### Develop Python scripts or site helpers

For a script-only change, run a syntax/import check on the edited file:

```bash
python -m py_compile knowledge_base/scripts/refresh_offline_data.py
```

Replace the path with the file you changed. If the change affects Zensical rendering, navigation, or generated site assets, run:

```bash
kb build
```

### Refresh offline data

If local generated data is stale, refresh it from the repo root:

```bash
kb refresh
```

### Deploy

Run `kb build` from the repo root, then publish `knowledge_base/site/` with the GitHub Pages workflow.
