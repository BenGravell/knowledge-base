---
name: raw-metadata-audit
description: Audit and fix raw paper metadata in the knowledge-base repository. Use when asked to run the raw metadata audit, resolve audit_metadata.py findings, or clean metadata entries still marked audit_status raw.
---

# Raw Metadata Audit

## Dependencies

Read these first:

- `../core/SKILL.md`
- `../ponytail/SKILL.md`

When an audit issue requires paper research, source verification, arXiv lookup, or metadata reconstruction, also read:

- `../arxiv-version/SKILL.md`
- `../paper-metadata/SKILL.md`

## Workflow

Run from `knowledge_base/`:

```bash
python scripts/list_raw_papers.py | python scripts/audit_metadata.py
```

Resolve all reported issues in the affected `metadata.yml` files.

Use the single-paper metadata skill for field semantics, path rules, and source-verification standards. Do not invent missing bibliographic data.

## Audit Status

Agents may change `audit_status: raw` to `audit_status: partial` after meaningful manual correction or verification.

Do not set `audit_status: reviewed`.

## Verification

After fixes, rerun the raw metadata audit command from `knowledge_base/` and resolve remaining actionable issues.
