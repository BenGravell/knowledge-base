---
name: paper-metadata
description: Create or update a single paper metadata.yml entry in the knowledge-base repository. Use for adding one paper, repairing one metadata file, filling missing fields, choosing a metadata path, or normalizing paper metadata.
---

# Paper Metadata

## Dependencies

Read these first:

- `../core/SKILL.md`
- `../arxiv-version/SKILL.md`

## Workflow

1. Use `knowledge_base/docs/templates/metadata.yml` as the field template.
2. Run the arXiv-version workflow before choosing the metadata path.
3. Reuse existing files and information when a matching entry already exists.
4. Place metadata at `knowledge_base/docs/papers/<YEAR>/<SLUG>/metadata.yml`.
5. Fill all metadata fields in the template.
6. Keep the entry consistent with `knowledge_base/config.py`.

## Path Rules

Use this path shape:

```text
knowledge_base/docs/papers/<YEAR>/<SLUG>/metadata.yml
```

Choose:

- `YEAR`: four-digit year of the earliest published version. If an arXiv preprint exists, use its year.
- `SLUG`: arXiv ID when one exists or is found, using new-style `YYMM.NNNNN` or old-style `archive/YYMMNNN`; otherwise use `YEAR.first_author_last_name_lowercase.title_first_four_words`.

## Field Rules

- `title`: full paper title, copied verbatim and then written in title case, as a double-quoted string.
- `algorithm`: short name of the primary algorithm, technique, or method introduced by the paper.
- `authors`: authors in paper order, one per item. Use full names where possible, including middle initials when given. Prefer the 26 English letters for easier search and pattern matching.
- `year`: year of first publication. If there is an arXiv preprint, use the arXiv year.
- `source`: most official venue, usually a conference or journal name. Omit years from this field.
- `type`: one of `VALID_TYPES` in `knowledge_base/config.py`.
- `doi`: DOI for the formally published item. Never use the arXiv DOI.
- `arxiv_id`: arXiv ID as a double-quoted string, or blank when no clear match exists.
- `tags`: short, commonly pattern-matched phrases, one per line. Limit to about 5-20 entries. Capitalize the first word.
- `abstract`: full abstract reproduced verbatim from the source. Prefer arXiv abstract, then formal published abstract, then other available source. Leave blank only if there truly is no abstract.
- `summary`: short external-observer summary of the main contributions and important secondary contributions.
- `link`: primary paper link. Use the arXiv PDF when available. Prefer freely openable links; use paywalled links only as a final resort.
- `links_alt`: alternate links, with freely openable paper links first and paywalled links last. Include supporting code, packages, or project pages associated with the item.
- `audit_status`: use a valid status from `VALID_AUDIT_STATUSES`. Agents may use `raw` or `partial`, but must not set `reviewed`.

## Quality Checks

Before finishing, compare the metadata against the actual source. Do not invent abstracts, DOIs, venues, arXiv IDs, author names, or code links.
