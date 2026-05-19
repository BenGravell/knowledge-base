---
hide:
  - toc
---

<div id="ct-app" class="ct-page">
  <section id="ct-settings" class="ct-settings" aria-label="Content Tree settings">
    <div class="ct-settings-header">
      <div class="ct-settings-title">
        <span>Content Tree</span>
        <details class="ct-note">
          <summary aria-label="About this content tree" aria-controls="ct-note-body">
            <span class="ct-note-icon" aria-hidden="true">i</span>
          </summary>
        </details>
      </div>
      <button id="ct-settings-toggle" class="ct-settings-toggle" type="button" aria-expanded="true" aria-controls="ct-settings-body">
        <span id="ct-settings-state">Hide Settings</span>
      </button>
      <p id="ct-note-body" class="ct-note-body">
        This content tree is my personal interpretation of how to organize these items in a hierarchical way.
        Multiple alternative organizations are possible. The content itself does not literally have a tree
        structure, and many of the real associations live in a more general graph of ideas, methods, and problems.
        The value of the tree is that it gives newcomers some structure and encodes my opinion about which
        connections are currently the most relevant or important.
      </p>
    </div>
    <div id="ct-settings-body" class="ct-controls">
      <div class="ct-search-field">
        <label for="ct-search">Search</label>
        <input id="ct-search" type="search" autocomplete="off" placeholder="Search titles, branches, or paths">
      </div>
      <div class="ct-control-group ct-year-control">
        <label for="ct-year-start">Year Range</label>
        <div>
          <input id="ct-year-start" type="number" inputmode="numeric" aria-label="Start year">
          <span aria-hidden="true">to</span>
          <input id="ct-year-end" type="number" inputmode="numeric" aria-label="End year">
        </div>
      </div>
      <div class="ct-control-group ct-source-type-control">
        <label for="ct-source-type">Source Type</label>
        <details id="ct-source-type-widget" class="ct-source-type-widget">
          <summary>
            <span id="ct-source-type-summary">All source types</span>
          </summary>
          <div id="ct-source-type" class="ct-source-type-buttons" role="group" aria-label="Source type"></div>
        </details>
      </div>
      <div class="ct-control-group ct-reset-control">
        <button id="ct-reset" type="button">Reset All</button>
      </div>
    </div>
  </section>

  <div id="ct-search-results" class="ct-search-results" hidden></div>

  <section class="ct-browser" aria-label="Focused content tree browser">
    <section class="ct-chain" aria-label="Focused content tree">
      <div id="ct-ancestor-chain"></div>
    </section>
  </section>
</div>

<script src="../javascripts/content-tree-data.js"></script>
<script src="../javascripts/content-tree.js"></script>
