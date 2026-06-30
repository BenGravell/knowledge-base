"""HTML fixture for home title gradient verification."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def html() -> str:
    css = "\n".join(
        [
            (ROOT / "knowledge_base/docs/stylesheets/extra/tokens.css").read_text(),
            (ROOT / "knowledge_base/docs/stylesheets/extra/home.css").read_text(),
            """
            :root {
              --md-default-bg-color: #ffffff;
              --md-default-fg-color: #1b1f29;
              --md-default-fg-color--light: #56616d;
              --md-code-bg-color: #f3f5f7;
              --md-primary-fg-color: #005eb8;
            }
            [data-md-color-scheme="slate"] {
              --md-default-bg-color: #1b1f29;
              --md-default-fg-color: #ffffff;
              --md-default-fg-color--light: #c7d0dc;
              --md-code-bg-color: #111822;
              --md-primary-fg-color: #83bfff;
            }
            html,
            body {
              margin: 0;
              min-height: 100%;
              background: transparent;
              font-family: Arial, sans-serif;
            }
            .md-content__inner:has(.kb-home-bento) {
              padding: 1rem 0;
            }
            .md-content__inner:has(.kb-home-bento) > h1:first-child {
              animation: none !important;
              font-size: 92px;
              margin: 0 auto;
            }
            .kb-home-bento {
              display: block;
              width: 1px;
              height: 1px;
            }
            """,
        ]
    )
    return f"""<!doctype html>
<meta charset="utf-8">
<style>{css}</style>
<main class="md-typeset">
  <div class="md-content__inner">
    <h1 id="title">Knowledge Base</h1>
    <div class="kb-home-bento" aria-hidden="true"></div>
  </div>
</main>
"""
