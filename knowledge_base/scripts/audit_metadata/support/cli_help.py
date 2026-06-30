"""Long CLI help text for the metadata auditor."""

CHECKS_EPILOG = """
Checks performed on each metadata.yml:
  unknown   - ERROR for any field not in the VALID_FIELDS schema
  required  - ERROR if any of title, authors, year, abstract, type, audit_status missing
  title     - ERROR if empty; ERROR if not in title case; ERROR for raw YAML character escapes like \\u2014; ERROR/WARN for corrupt characters or likely misspellings
  algorithm - ERROR if the algorithm label is generic; WARN if a broad family label appears to hide a narrower variant/contribution, or if a bare concrete method label appears to describe analysis/application of an existing method rather than the proposing paper
  authors   - ERROR if not a non-empty list of non-blank strings; ERROR if entries look like Last, First order, single-token names, known organization names, other non-individual names, suspicious Unicode corruption/control characters, or names that are not normalized to the native 26 English letters
  tags      - ERROR if tags are missing from normalization/tags.yml, differ from its canonical full-spelling form, duplicate after database or plural normalization, contain forbidden generic values, leading articles, more than 4 words, non-capital-case ordinary English words, or sentence-like prose debris copied from an abstract
  year      - ERROR if not a 4-digit integer
  arxiv     - ERROR if arxiv_id is present but not a valid arXiv ID
  abstract  - ERROR if placeholder-like, contains scraped page text, publisher/copyright notices, or PDF extraction artifacts; ERROR if near-empty unless audit_status is reviewed; WARN if empty, or for dollar math, copied "abstract" headings, likely misspellings, high-confidence OCR artifacts, or OCR word splits
  escape    - ERROR if string fields contain HTML/entity escapes like &#39; or &amp;, or if title contains raw YAML character escapes like \\u2014
  url       - ERROR if URLs appear in title, algorithm, authors, year, source, type, doi, arxiv_id, tags, or audit_status; ERROR if links contain garbled HTML/XML markup
  multiline - ERROR if one-line scalar fields span multiple YAML lines, or if title/abstract/summary do not use folded `>` YAML style with a single content line
  source    - ERROR if the source/venue field contains a publication year
  type      - ERROR if not a recognised paper type
  status    - ERROR if audit_status is not one of: raw, partial, reviewed
  path      - ERROR if YEAR/SLUG do not match metadata or expected slug format; ERROR if generated Map or Semantic Search IDs/sidecars are stale, missing, malformed, or inconsistent
  summary   - ERROR if it has substantial verbatim overlap with the abstract or known low-signal generated boilerplate; WARN if missing or empty unless audit_status is raw, or if likely misspelled
  optional  - INFO for each optional field that is not populated
  dash      - ERROR if any string field contains ASCII multi-dash punctuation like -- or ---
  whitespace - ERROR if any string field contains 3 or more consecutive spaces, or acronym-like parentheticals are joined to a preceding word without a space

By default, every check runs. Use --check to opt into a smaller set:
  --check abstract escape

Use --severity to filter reported issues by severity threshold:
  --severity error    # ERROR only
  --severity warning  # WARNING and ERROR
  --severity info     # INFO, WARNING, and ERROR

Available --check names:
  unknown required title algorithm authors tags year arxiv abstract escape url multiline source type status path summary optional dash whitespace
"""

__all__ = ["CHECKS_EPILOG"]
