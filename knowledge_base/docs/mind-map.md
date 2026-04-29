---
hide:
  - navigation
  - toc
---

# Mind Map

<style>
/* ── Remove MkDocs Material layout constraints for full-screen canvas ─────── */
h1                  { display: none; }
.md-content         { padding: 0 !important; }
.md-content__inner  { margin: 0 !important; padding: 0 !important; max-width: 100% !important; }
.md-grid            { max-width: 100% !important; }
.md-main            { overflow: hidden !important; }
.md-main__inner     { height: 100% !important; margin-top: 0 !important; }

/* ── App shell ────────────────────────────────────────────────────────────── */
#mm-app {
  position: relative;
  width:  100%;
  height: calc(100vh - 56px); /* 56px = Material header */
  overflow: hidden;
  background: #0a0a18;
  font-family: "Atkinson Hyperlegible Next", "Segoe UI", sans-serif;
}

/* ── Cytoscape canvas ─────────────────────────────────────────────────────── */
#cy {
  width:  100%;
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
  background: rgba(10,10,24,0.85);
  color: #aac;
  font-size: 0.9rem;
  gap: 1rem;
  z-index: 500;
  pointer-events: none;
}
#mm-loading svg {
  animation: mm-spin 1.2s linear infinite;
  opacity: 0.7;
}
@keyframes mm-spin { to { transform: rotate(360deg); } }

/* ── Control panel ────────────────────────────────────────────────────────── */
#mm-panel {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  width: 400px;
  background: rgba(14,14,30,0.93);
  border-left: 1px solid rgba(255,255,255,0.12);
  border-radius: 12px 0 0 12px;
  z-index: 200;
  backdrop-filter: blur(14px);
  box-shadow: -8px 0 36px rgba(0,0,0,0.55);
  color: #d0d4f8;
  font-size: 0.82rem;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

#mm-panel-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0.65rem 1rem;
  border-bottom: 1px solid rgba(255,255,255,0.1);
  gap: 0.5rem;
}
#mm-panel-header h3 {
  margin: 0;
  font-size: 0.88rem;
  font-weight: 600;
  color: #e8ecff;
  white-space: nowrap;
}
#mm-toggle-panel {
  background: none;
  border: 1px solid rgba(255,255,255,0.22);
  color: #99a;
  padding: 2px 9px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 0.72rem;
  flex-shrink: 0;
}
#mm-toggle-panel:hover { background: rgba(255,255,255,0.08); }

#mm-panel-body {
  padding: 0.8rem 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
  flex: 1;
  overflow-y: auto;
  scrollbar-width: thin;
  scrollbar-color: rgba(255,255,255,0.15) transparent;
}

/* ── Panel sections ───────────────────────────────────────────────────────── */
.mm-section {}
.mm-section-label {
  display: block;
  font-size: 0.68rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: #778;
  font-weight: 600;
  margin-bottom: 5px;
}

/* Search */
#mm-search {
  width: 100%;
  box-sizing: border-box;
  background: rgba(255,255,255,0.07);
  border: 1px solid rgba(255,255,255,0.18);
  color: #e8ecff;
  padding: 6px 10px;
  border-radius: 7px;
  font-size: 0.82rem;
  outline: none;
}
#mm-search::placeholder { color: #556; }
#mm-search:focus {
  border-color: rgba(100,150,255,0.55);
  background: rgba(255,255,255,0.1);
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
  color: #a8c0ff;
}
#mm-threshold-slider {
  width: 100%;
  accent-color: #4488ff;
}

/* Categories */
.mm-cat-links {
  display: flex;
  gap: 0.4rem;
  margin-bottom: 5px;
}
.mm-cat-links button {
  background: none;
  border: 1px solid rgba(255,255,255,0.18);
  color: #778;
  padding: 1px 7px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.7rem;
}
.mm-cat-links button:hover { color: #aab; border-color: rgba(255,255,255,0.3); }

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
.mm-cat-item:hover .mm-cat-name { color: #e8ecff; }
.mm-cat-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  flex-shrink: 0;
}
.mm-cat-name {
  flex: 1;
  color: #b0b8d8;
  font-size: 0.8rem;
}
.mm-cat-count {
  color: #556;
  font-size: 0.72rem;
}
.mm-cat-item input[type="checkbox"] {
  accent-color: #4488ff;
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
  cursor: pointer;
  user-select: none;
}
.mm-cat-group-header:hover .mm-cat-group-name { color: #e8ecff; }
.mm-cat-group-arrow {
  font-size: 0.65rem;
  color: #556;
  flex-shrink: 0;
  width: 10px;
}
.mm-cat-group-name {
  flex: 1;
  font-size: 0.75rem;
  font-weight: 600;
  color: #99aac4;
  text-transform: uppercase;
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
  background: rgba(255,255,255,0.07);
  border: 1px solid rgba(255,255,255,0.18);
  color: #b0b8d8;
  padding: 5px 0;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.78rem;
  transition: background 0.15s;
}
.mm-actions button:hover { background: rgba(255,255,255,0.14); }

/* Stats */
#mm-stats {
  text-align: center;
  color: #556;
  font-size: 0.72rem;
  border-top: 1px solid rgba(255,255,255,0.07);
  padding-top: 0.5rem;
}

/* ── Tooltip ──────────────────────────────────────────────────────────────── */
#mm-tooltip {
  position: fixed;
  z-index: 1000;
  display: none;
  background: rgba(8,8,22,0.96);
  border: 1px solid rgba(255,255,255,0.18);
  border-radius: 10px;
  padding: 11px 14px;
  max-width: 30vw;
  max-height: 65vh;
  overflow-y: hidden;
  pointer-events: none;
  backdrop-filter: blur(10px);
  box-shadow: 0 6px 28px rgba(0,0,0,0.6);
  font-family: "Atkinson Hyperlegible Next", "Segoe UI", sans-serif;
}
#mm-tooltip.visible { display: block; }
#mm-tooltip.pinned  { pointer-events: auto; border-color: rgba(255,215,0,0.35); overflow-y: auto; scrollbar-width: thin; scrollbar-color: rgba(255,255,255,0.15) transparent; }

.tt-title   { font-size: 0.83rem; font-weight: 600; color: #dce4ff; line-height: 1.35; margin-bottom: 4px; }
.tt-link    { display: block; font-size: 0.75rem; color: #4d9fff; text-decoration: none; margin-bottom: 7px; }
.tt-link:hover { color: #80bfff; text-decoration: underline; }
.tt-meta    { font-size: 0.73rem; color: #778; margin-bottom: 2px; }
.tt-tags    { font-size: 0.7rem;  color: #5588bb; margin: 5px 0; line-height: 1.5; }
.tt-summary { font-size: 0.73rem; color: #99a; margin-top: 6px; line-height: 1.45; }
.tt-hint    { font-size: 0.68rem; color: #445; margin-top: 8px; font-style: italic; }
</style>

<div id="mm-app">

  <!-- Loading spinner shown while fcose layout runs -->
  <div id="mm-loading">
    <svg width="40" height="40" viewBox="0 0 40 40" fill="none" stroke="#7090d0" stroke-width="3">
      <circle cx="20" cy="20" r="16" stroke-opacity="0.25"/>
      <path d="M20 4 a16 16 0 0 1 16 16" stroke-linecap="round"/>
    </svg>
    Computing layout…
  </div>

  <!-- Control panel -->
  <div id="mm-panel">
    <div id="mm-panel-header">
      <h3>Mind Map</h3>
      <button id="mm-toggle-panel">Hide</button>
    </div>
    <div id="mm-panel-body">

      <div class="mm-section">
        <span class="mm-section-label">Search</span>
        <input id="mm-search" type="text" placeholder="Title, tag or keyword…">
      </div>

      <div class="mm-section">
        <div class="mm-threshold-row">
          <span class="mm-section-label" style="margin:0">Similarity threshold</span>
          <span id="mm-threshold-val">0.80</span>
        </div>
        <input id="mm-threshold-slider" type="range" min="80" max="99" step="1">
      </div>

      <div class="mm-section">
        <span class="mm-section-label">Categories</span>
        <div class="mm-cat-links">
          <button id="mm-all-cats">All</button>
          <button id="mm-no-cats">None</button>
        </div>
        <div id="mm-category-filters"></div>
      </div>

      <div class="mm-section mm-actions">
        <button id="mm-fit-btn">Fit view</button>
        <button id="mm-relayout-btn">Re-layout</button>
      </div>

      <div id="mm-stats">
        <span id="mm-node-count">…</span> papers &nbsp;·&nbsp;
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
<!-- fcose layout plugin — served locally (v2.x requires layout-base and cose-base as separate globals) -->
<script src="../javascripts/vendor/layout-base.js"></script>
<script src="../javascripts/vendor/cose-base.js"></script>
<script src="../javascripts/vendor/cytoscape-fcose.js"></script>
<!-- Generated mind-map data (run generate_mind_map_data.py to regenerate) -->
<script src="../javascripts/mind-map-data.js"></script>
<!-- Visualisation logic -->
<script src="../javascripts/mind-map.js"></script>
