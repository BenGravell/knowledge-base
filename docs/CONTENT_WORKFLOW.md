# Content ingest workflow

The starting point for adding new items is ingestion. Commands in this file run
from the repository root.

## Manual ingest

Create a new directory under `knowledge_base/docs/papers/` and add a
`metadata.yml` based on `knowledge_base/docs/templates/metadata.yml`.

After metadata exists:

```bash
kb audit-metadata
kb validate-tree
```

## Batch funnel

Place paper URLs in `todo/PAPERS_FUNNEL.md`, one URL per line. Then route them
into source-specific files under `todo/papers/`, or into `todo/PAPERS_MISC.md`
when the source is unknown:

```bash
kb funnel --dry-run
kb funnel
```

## Source prefill scripts

Source-specific prefill scripts read URL or ID lists from `todo/papers/*.md`,
fetch initial metadata, and write
`knowledge_base/docs/papers/<YEAR>/<SLUG>/metadata.yml`.

Generated metadata starts as `audit_status: raw` and should be reviewed with
`python -m knowledge_base.scripts.audit_metadata`. Agents may move reviewed entries to
`audit_status: partial`; `reviewed` is reserved for human review.

Run a prefill script with its default input file:

```bash
kb prefill arxiv
kb prefill ieee
```

Common options shared by the prefill scripts:

```bash
kb prefill <source> --input todo/papers/<SOURCE>.md
kb prefill <source> --first 5
kb prefill <source> --list-skipped
kb prefill <source> --overwrite
kb prefill <source> --reingest
```

## Metadata audit

Audit all paper metadata files:

```bash
kb audit-metadata
```

Audit only entries marked `audit_status: partial`:

```bash
kb audit-metadata --audit-status partial
```

List entries still marked `audit_status: raw`:

```bash
kb list-raw
```

Add `audit_status` to older metadata files that do not have it yet:

```bash
kb add-audit-status --dry-run
kb add-audit-status
```

## Tree placement

The Tree nav itself is edited in `knowledge_base/tree.yml`. Paper entries still
use metadata paths relative to `knowledge_base/`, such as:

```yaml
docs/papers/2025/2506.11513/metadata.yml
```

The build converts those paths to generated `papers/<slug>.md` pages behind the
scenes.

Validate `knowledge_base/tree.yml` local links and paper placement:

```bash
kb validate-tree
kb validate-tree --check-algorithm-labels
```

Suggest likely fixes for Tree and metadata algorithm-label disagreements:

```bash
kb suggest-tree-labels
kb suggest-tree-labels --min-confidence high
kb suggest-tree-labels --format json
streamlit run dev_apps/tree_label_review_app.py
```

Find generated paper pages that are missing from the Tree nav:

```bash
kb list-unplaced --neighbors 3
kb list-unplaced --format paths
kb list-unplaced --neighbors 0 --fail-on-missing
```
