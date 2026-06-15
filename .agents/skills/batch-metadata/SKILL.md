---
name: batch-metadata
description: Generate metadata for a group, list, or source file of papers in the knowledge-base repository. Use when processing multiple paper URLs, todo paper lists, sectioned source lists, or batches that need metadata entries and tree placement.
---

# Batch Metadata

## Dependencies

Read these first:

- `../core/SKILL.md`
- `../arxiv-version/SKILL.md`
- `../paper-metadata/SKILL.md`
- `../tree-placement/SKILL.md`

## Workflow

1. Collect papers from the user-provided location or file.
2. Use subsection headers and surrounding context from the source list to infer where each paper belongs in `knowledge_base/tree.yml`.
3. For each paper, run the arXiv-version workflow.
4. For each paper, run the single-paper metadata workflow.
5. Add or update each `metadata.yml` file under `knowledge_base/docs/papers/`.
6. Place the new entries in the Tree using literal metadata paths in `knowledge_base/tree.yml`.

## Placement Guidance

When source headings conflict with the paper itself, prefer the paper's primary contribution as shown by title, abstract, tags, and summary.

Use existing Tree categories when they fit. Create a new category only when the paper's abstract and tags make existing branches a poor conceptual fit.

## Verification

After a batch that changes metadata or tree placement, run the verification commands from the tree-placement skill when practical.
