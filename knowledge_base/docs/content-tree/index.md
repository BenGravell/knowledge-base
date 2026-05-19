---
hide:
  - toc
---

<div id="ct-app" class="ct-page">
  <section id="ct-settings" class="ct-settings is-collapsed" aria-label="Content Tree settings">
    <div class="ct-settings-header">
      <div class="ct-settings-title">
        <span>Content Tree</span>
        <details class="ct-note">
          <summary aria-label="About this content tree" aria-controls="ct-note-body">
            <span class="ct-note-icon" aria-hidden="true">i</span>
          </summary>
        </details>
      </div>
      <button id="ct-settings-toggle" class="ct-settings-toggle" type="button" aria-expanded="false" aria-controls="ct-settings-body">
        <span id="ct-settings-state">Show Settings</span>
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
      <div class="ct-control-group ct-item-type-control">
        <label for="ct-item-type-trigger">Item Types</label>
        <button id="ct-item-type-trigger" class="ct-item-type-trigger" type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="ct-item-type-dialog">
          <span id="ct-item-type-summary">All item types</span>
        </button>
        <dialog id="ct-item-type-dialog" class="ct-item-type-dialog" aria-labelledby="ct-item-type-title">
          <div class="ct-item-type-panel">
            <div class="ct-item-type-head">
              <h2 id="ct-item-type-title">Item Types</h2>
              <button id="ct-item-type-close" class="ct-item-type-close" type="button" aria-label="Close item types filter">
                <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">
                  <path d="M18.3 5.71 12 12l6.3 6.29-1.41 1.41L10.59 13.41 4.29 19.7 2.88 18.29 9.17 12 2.88 5.71 4.29 4.3l6.3 6.29 6.3-6.29z"></path>
                </svg>
              </button>
            </div>
            <div class="ct-item-type-actions">
              <button id="ct-all-types" type="button">All</button>
              <button id="ct-no-types" type="button">None</button>
            </div>
            <div id="ct-item-type" class="ct-item-type-buttons" role="group" aria-label="Item types"></div>
          </div>
        </dialog>
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
