---
hide:
  - toc
---

<div id="ct-app" class="ct-page">
  <div class="ct-title-row">
    <h1>Content Tree</h1>
    <details class="ct-note">
      <summary aria-label="About this content tree" aria-controls="ct-note-body">
        <span class="ct-note-icon" aria-hidden="true">i</span>
      </summary>
    </details>
    <p id="ct-note-body" class="ct-note-body">
      This content tree is my personal interpretation of how to organize these items in a hierarchical way.
      Multiple alternative organizations are possible. The content itself does not literally have a tree
      structure, and many of the real associations live in a more general graph of ideas, methods, and problems.
      The value of the tree is that it gives newcomers some structure and encodes my opinion about which
      connections are currently the most relevant or important.
    </p>
  </div>

  <form id="ct-search-form" class="ct-search-panel">
    <div class="ct-search-field">
      <label for="ct-search">Find a topic or paper</label>
      <input id="ct-search" type="search" autocomplete="off" placeholder="Search titles, branches, or paths">
    </div>
    <button id="ct-search-submit" type="submit">Go</button>
    <button id="ct-root-btn" type="button">Root</button>
  </form>

  <div class="ct-meta-row" aria-live="polite">
    <span id="ct-tree-stats"></span>
    <span id="ct-current-summary"></span>
  </div>

  <div id="ct-search-results" class="ct-search-results" hidden></div>

  <nav id="ct-breadcrumbs" class="ct-breadcrumbs" aria-label="Content tree path"></nav>

  <section class="ct-browser" aria-label="Focused content tree browser">
    <section class="ct-chain" aria-label="Focused content tree">
      <div id="ct-ancestor-chain"></div>
    </section>
  </section>
</div>

<script src="../javascripts/content-tree-data.js"></script>
<script src="../javascripts/content-tree.js"></script>
