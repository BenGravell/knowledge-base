---
hide:
  - navigation
  - toc
---

# Mind Map

<style>
/* ── Derived vars: transparency adjustments on MkDocs palette tokens ─────── */
:root {
  --mm-edge-color:       #333333;
  --mm-edge-highlighted: color-mix(in srgb, var(--md-accent-fg-color)  80%, transparent);
}
[data-md-color-scheme="slate"] {
  --mm-edge-color:       #cccccc;
}

/* ── Remove MkDocs Material layout constraints for full-screen canvas ─────── */
h1                  { display: none; }
.md-content         { padding: 0 !important; }
.md-content__inner  { margin: 0 !important; padding: 0 !important; max-width: 100% !important; }
.md-grid            { max-width: 100% !important; }
.md-main            { overflow: hidden !important; }
.md-main__inner     { height: 100% !important; margin-top: 0 !important; }

/* ── Prevent page-level scrolling ─────────────────────────────────────────── */
html, body          { overflow: hidden !important; height: 100vh !important; }

/* ── Lock footer to bottom of viewport, always visible ────────────────────── */
.md-footer {
  position: fixed !important;
  bottom: 0 !important;
  left: 0 !important;
  right: 0 !important;
  z-index: 300 !important; /* must exceed #mm-panel z-index: 200 */
}

/* ── App shell ────────────────────────────────────────────────────────────── */
#mm-app {
  position: relative;
  display: flex;
  flex-direction: row;
  width:  100%;
  height: calc(100vh - var(--mm-header-h, 56px) - var(--mm-footer-h, 36px));
  overflow: hidden;
  background: var(--md-default-bg-color);
  font-family: "Atkinson Hyperlegible Next", "Segoe UI", sans-serif;
}

/* ── Cytoscape canvas ─────────────────────────────────────────────────────── */
#cy {
  flex: 1;
  min-width: 0;
  height: 100%;
}

/* ── Loading overlay ──────────────────────────────────────────────────────── */
#mm-loading {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  background: color-mix(in srgb, var(--md-default-bg-color) 88%, transparent);
  color: var(--md-default-fg-color--light);
  font-size: 0.9rem;
  gap: 1rem;
  z-index: 500;
  pointer-events: none;
}
#mm-loading svg {
  color: var(--md-primary-fg-color);
  animation: mm-spin 1.2s linear infinite;
  opacity: 0.7;
}
@keyframes mm-spin { to { transform: rotate(360deg); } }

/* ── Control panel ────────────────────────────────────────────────────────── */

/* Header: always visible, absolutely positioned over the app so it survives
   the panel collapsing to width:0. Clicking it toggles the panel body. */
#mm-panel-header {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 50;
  width: min(400px, 100vw);
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.65rem 1rem;
  gap: 0.5rem;
  background: color-mix(in srgb, var(--md-code-bg-color) 94%, transparent);
  border-bottom: 1px solid var(--md-default-fg-color--lightest);
  backdrop-filter: blur(14px);
  cursor: pointer;
  user-select: none;
}
#mm-panel-header:hover { background: color-mix(in srgb, var(--md-default-fg-color) 6%, transparent); }
#mm-panel-header h3 {
  margin: 0;
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--md-default-fg-color);
  white-space: nowrap;
}

#mm-panel-hide-btn {
  background: none;
  border: none;
  color: var(--md-default-fg-color--light);
  font-size: 0.78rem;
  padding: 2px 6px;
  border-radius: 4px;
  line-height: 1;
  flex-shrink: 0;
  pointer-events: none;
}

/* Panel overlays the canvas so #cy is always full-width and never moves */
#mm-panel {
  position: absolute;
  left: 0;
  top: 44px;
  height: calc(100% - 44px);
  width: min(400px, 100vw);
  z-index: 40;
  background: color-mix(in srgb, var(--md-code-bg-color) 94%, transparent);
  border-right: 1px solid var(--md-default-fg-color--lighter);
  backdrop-filter: blur(14px);
  color: var(--md-default-fg-color);
  font-size: 0.82rem;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: width 0.25s ease;
}
#mm-panel.body-collapsed {
  width: 0;
  border-right: none;
}

#mm-panel-body {
  padding: 0.8rem 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
  flex: 1;
  overflow-y: auto;
  scrollbar-width: thin;
  scrollbar-color: var(--md-default-fg-color--lighter) transparent;
}

/* ── Panel sections ───────────────────────────────────────────────────────── */
.mm-section {}
.mm-section-label {
  display: block;
  font-size: 0.68rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--md-default-fg-color--light);
  font-weight: 600;
  margin-bottom: 5px;
}

/* Search */
#mm-search {
  width: 100%;
  box-sizing: border-box;
  background: var(--md-default-fg-color--lightest);
  border: 1px solid var(--md-default-fg-color--lighter);
  color: var(--md-default-fg-color);
  padding: 6px 10px;
  border-radius: 7px;
  font-size: 0.82rem;
  outline: none;
}
#mm-search::placeholder { color: var(--md-default-fg-color--lighter); }
#mm-search:focus {
  border-color: var(--md-accent-fg-color);
  background: var(--md-default-fg-color--lightest);
}

/* Threshold */
.mm-threshold-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 4px;
}
#mm-threshold-val {
  font-variant-numeric: tabular-nums;
  color: var(--md-primary-fg-color);
}
#mm-threshold-slider {
  width: 100%;
  accent-color: var(--md-accent-fg-color);
}

/* Categories */
.mm-cat-links {
  display: flex;
  gap: 0.4rem;
  margin-bottom: 5px;
}
.mm-cat-links button {
  background: none;
  border: 1px solid var(--md-default-fg-color--lighter);
  color: var(--md-default-fg-color--light);
  padding: 1px 7px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.7rem;
}
.mm-cat-links button:hover { color: var(--md-default-fg-color); border-color: var(--md-default-fg-color--light); }

#mm-category-filters {
  display: flex;
  flex-direction: column;
  gap: 3px;
}
.mm-cat-item {
  display: flex;
  align-items: center;
  gap: 7px;
  cursor: pointer;
  padding: 2px 0;
}
.mm-cat-item:hover .mm-cat-name { color: var(--md-default-fg-color); }
.mm-cat-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  flex-shrink: 0;
}
.mm-cat-name {
  flex: 1;
  color: var(--md-default-fg-color--light);
  font-size: 0.8rem;
}
.mm-cat-count {
  color: var(--md-default-fg-color--lighter);
  font-size: 0.72rem;
}
.mm-cat-item input[type="checkbox"] {
  accent-color: var(--md-accent-fg-color);
  margin: 0;
  flex-shrink: 0;
}

/* Category group (collapsible, for categories with sub-categories) */
.mm-cat-group {
  margin-bottom: 1px;
}
.mm-cat-group-header {
  display: flex;
  align-items: center;
  gap: 5px;
  padding: 3px 0;
}
.mm-cat-group-cb {
  flex-shrink: 0;
  cursor: pointer;
  margin: 0;
}
.mm-cat-group-toggle {
  display: flex;
  align-items: center;
  flex: 1;
  gap: 5px;
  cursor: pointer;
  user-select: none;
  min-width: 0;
}
.mm-cat-group-toggle:hover .mm-cat-group-name { color: var(--md-default-fg-color); }
.mm-cat-group-arrow {
  font-size: 0.65rem;
  color: var(--md-default-fg-color--lighter);
  flex-shrink: 0;
  width: 10px;
}
.mm-cat-group-name {
  flex: 1;
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--md-default-fg-color--light);
  letter-spacing: 0.04em;
}
.mm-cat-group-items {
  padding-left: 14px;
}

/* Action buttons */
.mm-actions {
  display: flex;
  gap: 0.4rem;
}
.mm-actions button {
  flex: 1;
  background: var(--md-default-fg-color--lightest);
  border: 1px solid var(--md-default-fg-color--lighter);
  color: var(--md-default-fg-color--light);
  padding: 5px 0;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.78rem;
  transition: background 0.15s;
}
.mm-actions button:hover { background: var(--md-default-fg-color--lighter); }

/* Stats */
#mm-stats {
  text-align: center;
  color: var(--md-default-fg-color--lighter);
  font-size: 0.72rem;
  border-top: 1px solid var(--md-default-fg-color--lightest);
  padding-top: 0.5rem;
}

/* ── Tooltip ──────────────────────────────────────────────────────────────── */
#mm-tooltip {
  position: fixed;
  z-index: 1000;
  display: none;
  background: var(--md-code-bg-color);
  border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 10px;
  padding: 11px 14px;
  max-width: 30vw;
  max-height: 65vh;
  overflow-y: hidden;
  pointer-events: none;
  backdrop-filter: blur(10px);
  box-shadow: var(--md-shadow-z2);
  font-family: "Atkinson Hyperlegible Next", "Segoe UI", sans-serif;
}
#mm-tooltip.visible { display: block; }
#mm-tooltip.pinned  { pointer-events: auto; border-color: var(--md-accent-fg-color--transparent); overflow-y: auto; scrollbar-width: thin; scrollbar-color: var(--md-default-fg-color--lighter) transparent; }

.tt-title   { font-size: 0.83rem; font-weight: 600; color: var(--md-default-fg-color); line-height: 1.35; margin-bottom: 4px; }
.tt-link    { display: block; font-size: 0.75rem; color: var(--md-typeset-a-color); text-decoration: none; margin-bottom: 7px; }
.tt-link:hover { color: var(--md-primary-fg-color--dark); text-decoration: underline; }
.tt-meta    { font-size: 0.73rem; color: var(--md-default-fg-color--light); margin-bottom: 2px; }
.tt-tags    { font-size: 0.7rem;  color: var(--md-primary-fg-color--light); margin: 5px 0; line-height: 1.5; }
.tt-summary { font-size: 0.73rem; color: var(--md-default-fg-color--light); margin-top: 6px; line-height: 1.45; }
.tt-hint    { font-size: 0.68rem; color: var(--md-default-fg-color--lighter); margin-top: 8px; font-style: italic; }
</style>

<div id="mm-app">

  <!-- Loading spinner shown while the graph initialises -->
  <div id="mm-loading">
    <svg width="40" height="40" viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="3">
      <circle cx="20" cy="20" r="16" stroke-opacity="0.25"/>
      <path d="M20 4 a16 16 0 0 1 16 16" stroke-linecap="round"/>
    </svg>
    Loading…
  </div>

  <!-- Panel header: always visible, overlays app corner to survive panel collapse -->
  <div id="mm-panel-header">
    <h3>Mind Map</h3>
    <button id="mm-panel-hide-btn">Hide</button>
  </div>

  <!-- Panel body: collapses to width:0 on hide -->
  <div id="mm-panel">
    <div id="mm-panel-body">

      <div class="mm-section mm-actions">
        <button id="mm-fit-btn">Fit view</button>
      </div>

      <div class="mm-section">
        <div class="mm-threshold-row">
          <span class="mm-section-label" style="margin:0">Similarity threshold</span>
          <span id="mm-threshold-val">0.77</span>
        </div>
        <input id="mm-threshold-slider" type="range" min="75" max="99" step="1">
      </div>

      <div class="mm-section">
        <span class="mm-section-label">Search</span>
        <input id="mm-search" type="text" placeholder="Title, tag or keyword…">
      </div>

      <div class="mm-section">
        <span class="mm-section-label">Categories</span>
        <div class="mm-cat-links">
          <button id="mm-all-cats">All</button>
          <button id="mm-no-cats">None</button>
        </div>
        <div id="mm-category-filters"></div>
      </div>

      <div id="mm-stats">
        <span id="mm-node-count">…</span> items &nbsp;·&nbsp;
        <span id="mm-edge-count">…</span> connections
      </div>

    </div>
  </div>

  <!-- Tooltip (positioned by JS) -->
  <div id="mm-tooltip"></div>

  <!-- Cytoscape canvas -->
  <div id="cy"></div>

</div>

<!-- Cytoscape core -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.29.2/cytoscape.min.js"></script>
<!-- Generated mind-map data (run generate_mind_map_data.py to regenerate) -->
<script src="../javascripts/mind-map-data.js"></script>
<!-- Visualisation logic -->
<script src="../javascripts/mind-map.js"></script>
<script>
(function () {
  function applyMmSizes() {
    var header = document.querySelector('.md-header');
    var footer = document.querySelector('.md-footer');
    var hh = header ? header.getBoundingClientRect().height : 56;
    var fh = footer ? footer.getBoundingClientRect().height : 36;
    document.documentElement.style.setProperty('--mm-header-h', hh + 'px');
    document.documentElement.style.setProperty('--mm-footer-h', fh + 'px');
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', applyMmSizes);
  } else {
    applyMmSizes();
  }
  window.addEventListener('resize', applyMmSizes);
})();
</script>
<script>
(function () {
  var panel   = document.getElementById('mm-panel');
  var header  = document.getElementById('mm-panel-header');
  var hideBtn = document.getElementById('mm-panel-hide-btn');
  var PAD = 30;

  function fitBesidePanel(cy) {
    var eles = cy.elements(':visible');
    if (!eles.length) return;
    var bb     = eles.boundingBox();
    var left   = panel.offsetWidth + PAD;
    var right  = cy.width()  - PAD;
    var top    = PAD;
    var bottom = cy.height() - PAD;
    var zoom   = Math.min((right - left) / bb.w, (bottom - top) / bb.h);
    cy.viewport({
      zoom: zoom,
      pan: {
        x: left + (right - left) / 2 - (bb.x1 + bb.x2) / 2 * zoom,
        y: top  + (bottom - top) / 2 - (bb.y1 + bb.y2) / 2 * zoom
      }
    });
  }

  /* Fit to the visible canvas region on initial load */
  var cy = window._cy && window._cy();
  if (cy) {
    if (panel.classList.contains('body-collapsed')) {
      cy.fit(cy.elements(':visible'), PAD);
    } else {
      fitBesidePanel(cy);
    }
  }

  header.addEventListener('click', function () {
    var collapsed = panel.classList.toggle('body-collapsed');
    hideBtn.textContent = collapsed ? 'Show Settings' : 'Hide Settings';
    header.title        = collapsed ? 'Show Settings'  : 'Hide Settings';
  });

  document.getElementById('mm-fit-btn').addEventListener('click', function () {
    var fitCy = window._cy && window._cy();
    if (!fitCy) return;
    if (panel.classList.contains('body-collapsed')) {
      fitCy.fit(fitCy.elements(':visible'), PAD);
    } else {
      fitBesidePanel(fitCy);
    }
  });
})();
</script>
