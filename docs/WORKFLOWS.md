# Workflows

## `kb`

`kb` is a Python console script.
It is available whenever the active Python environment has this repo installed.

The examples below assume that commands are run from the repository root with
the project environment active. Otherwise, prefix `kb ...` with `./dev run`,
for example `./dev run kb serve`.

## Serve the site locally

```bash
kb serve
```

Open the URL printed by Zensical, usually <http://127.0.0.1:8000/>.

For more details about site generation, see [docs/SITE_GENERATION.md](../docs/SITE_GENERATION.md)

## Run pre-commit

Install the Git hooks once:

```bash
./dev run pre-commit install
```

Run the hooks manually:

```bash
./dev run pre-commit run --all-files
```

The hook set is configured in [.pre-commit-config.yaml](../.pre-commit-config.yaml).

To run only one hook e.g. while developing, pass its id and the files to check:

```bash
./dev run pre-commit run ruff-check --files knowledge_base/scripts/refresh_offline_data.py
```

## Add papers

The normal path is to funnel URLs into source queues, prefill metadata, review
it, place the papers in the Tree, and refresh generated data:

```bash
# Route URLs into todo/papers/<SOURCE>.md or todo/PAPERS_MISC.md.
kb funnel --dry-run
kb funnel

# Prefill every populated source queue automatically.
kb prefill

# Apply supported metadata fixes, then manually review the remaining findings.
kb audit-metadata --fix --metadata-only

# Refresh Map embeddings used for automatic placement.
python -m knowledge_base.components.map.pipeline.generate_data

# Place unplaced papers in knowledge_base/tree.yml, then verify the Tree.
kb list-unplaced --write-tree
kb validate-tree
kb list-unplaced --neighbors 0 --fail-on-missing

# Refresh generated data and build the site. Bypass the tracked-file fast path
# so this also sees new metadata files before they are staged in Git.
kb refresh --no-fast-path
```

Put one paper URL per line in `todo/PAPERS_FUNNEL.md`. Unknown sources are
routed to `todo/PAPERS_MISC.md`; supported sources go to
`todo/papers/<SOURCE>.md`.

To run or debug one source queue, use `kb prefill SOURCE`. Common options are:

```bash
kb prefill <source> --input todo/papers/<SOURCE>.md
kb prefill <source> --first 5
kb prefill <source> --list-skipped
kb prefill <source> --overwrite
kb prefill <source> --reingest
```

Run `kb prefill --help` for the current source list. Prefill removes handled
rows from its source queue and writes new entries below
`knowledge_base/docs/papers/` with `audit_status: raw`. Review the generated
metadata and resulting diff. Agents may promote meaningfully reviewed entries
to `partial`; only a human may set `reviewed`.

### Add one paper manually

Create `knowledge_base/docs/papers/<YEAR>/<SLUG>/metadata.yml` from
`knowledge_base/docs/templates/metadata.yml`, then audit that file:

```bash
kb audit-metadata --file knowledge_base/docs/papers/<YEAR>/<SLUG>/metadata.yml --metadata-only
```

Then refresh Map embeddings, place the paper, validate the Tree, and run `kb refresh --no-fast-path` as shown above.
Do not edit generated paper pages or anything under `knowledge_base/site/`.

### Focused metadata and Tree checks

Use focused commands when reviewing or repairing existing entries:

```bash
# Audit a lifecycle subset or list raw entries.
kb audit-metadata --audit-status partial
kb list-raw

# Backfill audit_status: raw on legacy entries that lack the field.
kb add-audit-status --dry-run
kb add-audit-status

# Check stricter Tree/metadata label consistency.
kb validate-tree --check-algorithm-labels

# Inspect likely label fixes in the terminal or review app.
kb suggest-tree-labels --min-confidence high
kb suggest-tree-labels --format json
streamlit run dev_apps/tree_label_review_app.py

# Inspect papers missing from the Tree without editing it.
kb list-unplaced --neighbors 3
kb list-unplaced --format paths
```

`knowledge_base/tree.yml` is the editable Tree source. Its paper paths are
relative to `knowledge_base/`, for example:

```yaml
docs/papers/2025/2506.11513/metadata.yml
```

The build turns those metadata entries into generated paper pages.

## Ingest arXiv embed text

Some paper entries have an optional `embed_text.md` sidecar next to `metadata.yml`.
These sidecars are cleaned Markdown conversions of arXiv HTML, LaTeX, or PDF sources for embedding and agentic search only.
They are not the canonical e-print, PDF, or LaTeX source of truth, and this
repo intentionally does not store PDFs, LaTeX source archives, images, or other
rich paper assets.
Reuse of paper text remains governed by each paper's original license and rights holder terms.

Run the ingest script from the repo root:

```bash
kb ingest-arxiv --id 2402.08954
```

The script skips existing sidecars unless `--force` is passed.
For arXiv entries it tries arXiv HTML, ar5iv HTML, arXiv LaTeX source, then the PDF
inferred from the arXiv ID. HTML conversion uses the Python environment's
project-managed `pandoc` CLI; LaTeX/PDF fallback uses the Python environment's
project-managed `docling` CLI.

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

## Refresh offline data

If local generated data is stale, refresh it from the repo root:

```bash
kb refresh
```

## Deploy

Push to `main`; the GitHub Pages workflow runs `kb build` and publishes `knowledge_base/site/`.
