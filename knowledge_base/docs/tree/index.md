---
hide:
  - toc
---

<div id="ct-app" class="ct-page">
  <section id="ct-settings" class="ct-settings is-collapsed" aria-label="Tree settings">
    <div class="ct-settings-header kb-app-header">
      <div class="ct-settings-title">
        <span class="kb-app-header-title">Tree</span>
        <details class="ct-note">
          <summary aria-label="About this tree" aria-controls="ct-note-body">
            <span class="ct-note-icon" aria-hidden="true">i</span>
          </summary>
        </details>
      </div>
      <button id="ct-settings-toggle" class="ct-settings-toggle kb-app-header-action" type="button" aria-expanded="false" aria-controls="ct-settings-body">
        <span id="ct-settings-state">Show Settings</span>
      </button>
      <p id="ct-note-body" class="ct-note-body">
        This tree is my personal interpretation of how to organize the collection in a hierarchical way.
        Multiple alternative organizations are possible.
        The content itself does not literally have a tree structure, and many of the real associations live in a more general graph of ideas, methods, and problems.
        The value of the tree is that it gives readers some structure and encodes my opinion about which connections are currently the most relevant or important.
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

  <div class="ct-workspace">
    <section id="ct-sunburst-panel" class="ct-sunburst-panel" aria-label="Tree sunburst navigator">
      <div class="ct-sunburst-body">
        <div id="ct-sunburst" class="ct-sunburst" role="group" aria-label="Tree sunburst">
          <div class="ct-sunburst-actions">
            <button id="ct-sunburst-root" class="ct-sunburst-action" type="button" aria-label="Move to root" title="Root">
              <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">
                <path d="M12 3 3 10.6l1.3 1.5 1.2-1V20h5.5v-5h2v5h5.5v-8.9l1.2 1 1.3-1.5zm4.5 15H15v-5H9v5H7.5v-8.6L12 5.6l4.5 3.8z"></path>
              </svg>
            </button>
          </div>
          <div id="ct-sunburst-stage" class="ct-sunburst-stage"></div>
        </div>
      </div>
    </section>

    <section class="ct-browser" aria-label="Focused tree browser">
      <section class="ct-chain" aria-label="Focused tree">
        <div id="ct-ancestor-chain"></div>
      </section>
    </section>
  </div>

  <section id="ct-selection-details" class="ct-selection-details" aria-live="polite" hidden></section>
</div>

<script src="../javascripts/tree-data.js"></script>
<script src="../javascripts/tree.js"></script>
