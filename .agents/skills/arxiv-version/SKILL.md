---
name: arxiv-version
description: Find, verify, and normalize arXiv versions for papers in the knowledge-base repository. Use whenever a paper arxiv_id is unknown, before choosing a metadata path, primary link, slug, or deciding that a paywalled source must be primary.
---

# Arxiv Version

## Dependencies

Read these first if repository context is not already loaded:

- `../core/SKILL.md`
- `../ponytail/SKILL.md`

## Workflow

Use this workflow whenever a paper's `arxiv_id` is unknown.

1. If the paper year is 1990 or earlier, do not search for an arXiv version. arXiv started in 1991.
2. If an existing source or metadata file already has a non-empty `arxiv_id`, do not search again. Reuse the known ID.
3. Normalize reused IDs as bare arXiv IDs with no `arXiv:` prefix and no version suffix. Preserve old-style archive prefixes such as `cond-mat/9910332`.
4. For papers from 1991 onward with no known `arxiv_id`, search for an arXiv version before finalizing metadata.
5. Start with the official title plus the first author.
6. If that fails, search alternate evidence: title without subtitle, distinctive abstract phrases, algorithm or method name, DOI, full author set, official publication title plus `arXiv`, official paper pages, author pages, lab pages, Semantic Scholar, OpenAlex, Google Scholar snippets, and arXiv search results when available.
7. Remember that an arXiv reprint may have a different title from the formally published version.

## Acceptance Standard

Accept a candidate only when authors, abstract, core contribution, and bibliographic clues make it clearly the same work.

Strong evidence includes:

- Matching authors plus matching abstract or contribution.
- An arXiv page that links to the DOI or venue version.
- An official or author page that links both versions.

If the match is ambiguous, leave `arxiv_id` blank and do not add an arXiv link. Prefer a known open non-arXiv link when one exists.

## Metadata Consequences

When an arXiv version is found while generating metadata:

- Use the arXiv ID as the metadata slug.
- Set `year` from the earliest arXiv version year.
- Use the arXiv PDF as `link`.
- Include formal publication DOI and source when available.
