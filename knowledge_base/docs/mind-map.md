---
hide:
  - navigation
  - toc
---

# Mind Map

<style>
/* ── Theme tokens — light (default) ──────────────────────────────────────── */
:root {
  --mm-canvas-bg:           #eef0f8;
  --mm-overlay-bg:          rgba(230,233,245,0.88);
  --mm-overlay-color:       #4a5478;
  --mm-overlay-stroke:      #4466b0;
  --mm-panel-bg:            rgba(246,247,253,0.96);
  --mm-panel-border:        rgba(0,0,0,0.10);
  --mm-panel-shadow:        rgba(0,0,0,0.15);
  --mm-divider:             rgba(0,0,0,0.08);
  --mm-text-primary:        #1a1e36;
  --mm-text-secondary:      #2e3a5a;
  --mm-text-muted:          #5a6888;
  --mm-text-dim:            #8898b4;
  --mm-surface-bg:          rgba(0,0,0,0.05);
  --mm-surface-border:      rgba(0,0,0,0.14);
  --mm-surface-hover-bg:    rgba(0,0,0,0.08);
  --mm-surface-hover-border:rgba(60,100,220,0.45);
  --mm-scrollbar:           rgba(0,0,0,0.14);
  --mm-accent:              #2255cc;
  --mm-threshold-val:       #1a44bb;
  --mm-cat-name:            #2e3a5a;
  --mm-cat-count:           #8898b4;
  --mm-group-name:          #4a5878;
  --mm-edge-color:          rgba(60,80,180,0.38);
  --mm-edge-highlighted:    rgba(180,100,0,0.85);
  --mm-tt-bg:               rgba(252,253,255,0.97);
  --mm-tt-border:           rgba(0,0,0,0.12);
  --mm-tt-shadow:           rgba(0,0,0,0.16);
  --mm-tt-pinned-border:    rgba(160,100,0,0.40);
  --mm-tt-title:            #1a1e36;
  --mm-tt-link:             #1a6fd4;
  --mm-tt-link-hover:       #1044a8;
  --mm-tt-meta:             #5a6888;
  --mm-tt-tags:             #1a50a8;
  --mm-tt-summary:          #3a4a68;
  --mm-tt-hint:             #8898b4;
}

/* ── Theme tokens — dark (MkDocs Material "slate") ───────────────────────── */
[data-md-color-scheme="slate"] {
  --mm-canvas-bg:           #0a0a18;
  --mm-overlay-bg:          rgba(10,10,24,0.85);
  --mm-overlay-color:       #aaaacc;
  --mm-overlay-stroke:      #7090d0;
  --mm-panel-bg:            rgba(14,14,30,0.93);
  --mm-panel-border:        rgba(255,255,255,0.12);
  --mm-panel-shadow:        rgba(0,0,0,0.55);
  --mm-divider:             rgba(255,255,255,0.07);
  --mm-text-primary:        #e8ecff;
  --mm-text-secondary:      #d0d4f8;
  --mm-text-muted:          #778899;
  --mm-text-dim:            #556677;
  --mm-surface-bg:          rgba(255,255,255,0.07);
  --mm-surface-border:      rgba(255,255,255,0.18);
  --mm-surface-hover-bg:    rgba(255,255,255,0.10);
  --mm-surface-hover-border:rgba(100,150,255,0.55);
  --mm-scrollbar:           rgba(255,255,255,0.15);
  --mm-accent:              #4488ff;
  --mm-threshold-val:       #a8c0ff;
  --mm-cat-name:            #b0b8d8;
  --mm-cat-count:           #556677;
  --mm-group-name:          #99aac4;
  --mm-edge-color:          rgba(180,200,255,0.35);
  --mm-edge-highlighted:    rgba(255,215,0,0.80);
  --mm-tt-bg:               rgba(8,8,22,0.96);
  --mm-tt-border:           rgba(255,255,255,0.18);
  --mm-tt-shadow:           rgba(0,0,0,0.60);
  --mm-tt-pinned-border:    rgba(255,215,0,0.35);
  --mm-tt-title:            #dce4ff;
  --mm-tt-link:             #4d9fff;
  --mm-tt-link-hover:       #80bfff;
  --mm-tt-meta:             #778899;
  --mm-tt-tags:             #5588bb;
  --mm-tt-summary:          #9999aa;
  --mm-tt-hint:             #445566;
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
  width:  100%;
  height: calc(100vh - var(--mm-header-h, 56px) - var(--mm-footer-h, 36px));
  overflow: hidden;
  background: var(--mm-canvas-bg);
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
  background: var(--mm-overlay-bg);
  color: var(--mm-overlay-color);
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
  background: var(--mm-panel-bg);
  border-left: 1px solid var(--mm-panel-border);
  border-radius: 12px 0 0 12px;
  z-index: 200;
  backdrop-filter: blur(14px);
  box-shadow: -8px 0 36px var(--mm-panel-shadow);
  color: var(--mm-text-secondary);
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
  border-bottom: 1px solid var(--mm-divider);
  gap: 0.5rem;
}
#mm-panel-header h3 {
  margin: 0;
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--mm-text-primary);
  white-space: nowrap;
}

#mm-panel-body {
  padding: 0.8rem 1rem;
  display: flex;
  flex-direction: column;
  gap: 0.85rem;
  flex: 1;
  overflow-y: auto;
  scrollbar-width: thin;
  scrollbar-color: var(--mm-scrollbar) transparent;
}

/* ── Panel sections ───────────────────────────────────────────────────────── */
.mm-section {}
.mm-section-label {
  display: block;
  font-size: 0.68rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--mm-text-muted);
  font-weight: 600;
  margin-bottom: 5px;
}

/* Search */
#mm-search {
  width: 100%;
  box-sizing: border-box;
  background: var(--mm-surface-bg);
  border: 1px solid var(--mm-surface-border);
  color: var(--mm-text-primary);
  padding: 6px 10px;
  border-radius: 7px;
  font-size: 0.82rem;
  outline: none;
}
#mm-search::placeholder { color: var(--mm-text-dim); }
#mm-search:focus {
  border-color: var(--mm-surface-hover-border);
  background: var(--mm-surface-hover-bg);
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
  color: var(--mm-threshold-val);
}
#mm-threshold-slider {
  width: 100%;
  accent-color: var(--mm-accent);
}

/* Categories */
.mm-cat-links {
  display: flex;
  gap: 0.4rem;
  margin-bottom: 5px;
}
.mm-cat-links button {
  background: none;
  border: 1px solid var(--mm-surface-border);
  color: var(--mm-text-muted);
  padding: 1px 7px;
  border-radius: 4px;
  cursor: pointer;
  font-size: 0.7rem;
}
.mm-cat-links button:hover { color: var(--mm-text-secondary); border-color: var(--mm-surface-hover-border); }

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
.mm-cat-item:hover .mm-cat-name { color: var(--mm-text-primary); }
.mm-cat-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  flex-shrink: 0;
}
.mm-cat-name {
  flex: 1;
  color: var(--mm-cat-name);
  font-size: 0.8rem;
}
.mm-cat-count {
  color: var(--mm-cat-count);
  font-size: 0.72rem;
}
.mm-cat-item input[type="checkbox"] {
  accent-color: var(--mm-accent);
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
.mm-cat-group-header:hover .mm-cat-group-name { color: var(--mm-text-primary); }
.mm-cat-group-arrow {
  font-size: 0.65rem;
  color: var(--mm-text-dim);
  flex-shrink: 0;
  width: 10px;
}
.mm-cat-group-name {
  flex: 1;
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--mm-group-name);
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
  background: var(--mm-surface-bg);
  border: 1px solid var(--mm-surface-border);
  color: var(--mm-text-secondary);
  padding: 5px 0;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.78rem;
  transition: background 0.15s;
}
.mm-actions button:hover { background: var(--mm-surface-hover-bg); }

/* Stats */
#mm-stats {
  text-align: center;
  color: var(--mm-text-dim);
  font-size: 0.72rem;
  border-top: 1px solid var(--mm-divider);
  padding-top: 0.5rem;
}

/* ── Tooltip ──────────────────────────────────────────────────────────────── */
#mm-tooltip {
  position: fixed;
  z-index: 1000;
  display: none;
  background: var(--mm-tt-bg);
  border: 1px solid var(--mm-tt-border);
  border-radius: 10px;
  padding: 11px 14px;
  max-width: 30vw;
  max-height: 65vh;
  overflow-y: hidden;
  pointer-events: none;
  backdrop-filter: blur(10px);
  box-shadow: 0 6px 28px var(--mm-tt-shadow);
  font-family: "Atkinson Hyperlegible Next", "Segoe UI", sans-serif;
}
#mm-tooltip.visible { display: block; }
#mm-tooltip.pinned  { pointer-events: auto; border-color: var(--mm-tt-pinned-border); overflow-y: auto; scrollbar-width: thin; scrollbar-color: var(--mm-scrollbar) transparent; }

.tt-title   { font-size: 0.83rem; font-weight: 600; color: var(--mm-tt-title); line-height: 1.35; margin-bottom: 4px; }
.tt-link    { display: block; font-size: 0.75rem; color: var(--mm-tt-link); text-decoration: none; margin-bottom: 7px; }
.tt-link:hover { color: var(--mm-tt-link-hover); text-decoration: underline; }
.tt-meta    { font-size: 0.73rem; color: var(--mm-tt-meta); margin-bottom: 2px; }
.tt-tags    { font-size: 0.7rem;  color: var(--mm-tt-tags); margin: 5px 0; line-height: 1.5; }
.tt-summary { font-size: 0.73rem; color: var(--mm-tt-summary); margin-top: 6px; line-height: 1.45; }
.tt-hint    { font-size: 0.68rem; color: var(--mm-tt-hint); margin-top: 8px; font-style: italic; }
</style>

<div id="mm-app">

  <!-- Loading spinner shown while fcose layout runs -->
  <div id="mm-loading">
    <svg width="40" height="40" viewBox="0 0 40 40" fill="none" stroke="var(--mm-overlay-stroke)" stroke-width="3">
      <circle cx="20" cy="20" r="16" stroke-opacity="0.25"/>
      <path d="M20 4 a16 16 0 0 1 16 16" stroke-linecap="round"/>
    </svg>
    Computing layout…
  </div>

  <!-- Control panel -->
  <div id="mm-panel">
    <div id="mm-panel-header">
      <h3>Mind Map</h3>
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
