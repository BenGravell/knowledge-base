---
name: paper-metadata
description: Create or update a single paper metadata.yml entry in the knowledge-base repository. Use for adding one paper, repairing one metadata file, filling missing fields, choosing a metadata path, or normalizing paper metadata.
---

# Paper Metadata

## Dependencies

Read these first:

- `../core/SKILL.md`
- `../ponytail/SKILL.md`
- `../arxiv-version/SKILL.md`

## Workflow

1. Use `knowledge_base/docs/templates/metadata.yml` as the field template.
2. Run the arXiv-version workflow before choosing the metadata path.
3. Reuse existing files and information when a matching entry already exists.
4. Place metadata at `knowledge_base/docs/papers/<YEAR>/<SLUG>/metadata.yml`.
5. Fill all metadata fields in the template.
6. Keep the entry consistent with `knowledge_base/metadata.py` and its generated reference, `docs/METADATA.md`.

## Path Rules

Use this path shape:

```text
knowledge_base/docs/papers/<YEAR>/<SLUG>/metadata.yml
```

Choose:

- `YEAR`: four-digit year of the earliest published version. If an arXiv preprint exists, use its year.
- `SLUG`: arXiv ID when one exists or is found, using new-style `YYMM.NNNNN` or old-style `archive/YYMMNNN`; otherwise use `YEAR.first_author_last_name_lowercase.title_first_four_words`.

## Field Rules

Read `docs/METADATA.md` for field meanings, allowed values, defaults, and editorial guidance.
It is generated from the model's descriptions so field rules have one source of truth.
Agents may use `raw` or `partial` for `audit_status`, but must not set `reviewed`.

## Quality Checks

Before finishing, compare the metadata against the actual source. Do not invent abstracts, DOIs, venues, arXiv IDs, author names, or code links.
