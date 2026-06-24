---
hide:
  - toc
---

# Map

<style>
/* ── Derived vars: transparency adjustments on site palette tokens ───────── */
:root {
  --mm-node-muted:         #a3adb8;
  --mm-node-muted-related: #7f8b97;
  --mm-node-ghost:         #edf1f5;
  --mm-node-ghost-border:  #b8c2cc;
  --mm-node-border:        #e1e7ee;
  --mm-muted-label:        #475569;
  --mm-selected-ring:      #005ab5;
  --mm-selected-label:     #111111;
  --mm-blue:               var(--kb-color-blue);
  --mm-teal:               var(--kb-color-teal);
  --mm-rose:               var(--kb-color-rose);
  --mm-gold:               var(--kb-color-gold);
  --mm-border:             color-mix(in srgb, var(--md-default-fg-color) 15%, transparent);
  --mm-soft-border:        color-mix(in srgb, var(--md-default-fg-color) 9%, transparent);
  --mm-panel:              color-mix(in srgb, var(--md-code-bg-color) 70%, var(--md-default-bg-color));
}
[data-md-color-scheme="default"] {
  --mm-node-muted:         #a3adb8;
  --mm-node-muted-related: #7f8b97;
  --mm-node-ghost:         #edf1f5;
  --mm-node-ghost-border:  #b8c2cc;
  --mm-node-border:        #e1e7ee;
  --mm-muted-label:        #475569;
  --mm-selected-ring:      #005ab5;
  --mm-selected-label:     #111111;
  --mm-blue:               var(--kb-color-blue);
  --mm-teal:               var(--kb-color-teal);
  --mm-rose:               var(--kb-color-rose);
  --mm-gold:               var(--kb-color-gold);
  --mm-border:             color-mix(in srgb, var(--md-default-fg-color) 15%, transparent);
  --mm-soft-border:        color-mix(in srgb, var(--md-default-fg-color) 9%, transparent);
  --mm-panel:              color-mix(in srgb, var(--md-code-bg-color) 70%, var(--md-default-bg-color));
}
[data-md-color-scheme="slate"] {
  --mm-node-muted:         #66717d;
  --mm-node-muted-related: #8b96a2;
  --mm-node-ghost:         #222a33;
  --mm-node-ghost-border:  #56616d;
  --mm-node-border:        #242b35;
  --mm-muted-label:        #c8d0d8;
  --mm-selected-ring:      #f1c232;
  --mm-selected-label:     #111111;
  --mm-blue:               var(--kb-color-blue);
  --mm-teal:               var(--kb-color-teal);
  --mm-rose:               var(--kb-color-rose);
  --mm-gold:               var(--kb-color-gold);
  --mm-border:             color-mix(in srgb, var(--md-default-fg-color) 15%, transparent);
  --mm-soft-border:        color-mix(in srgb, var(--md-default-fg-color) 9%, transparent);
  --mm-panel:              color-mix(in srgb, var(--md-code-bg-color) 82%, #050910);
}

/* ── Remove site layout constraints for full-screen canvas ───────────────── */
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
  --mm-ribbon-h: clamp(12rem, 28vh, 17rem);
  --mm-ribbon-max-h: var(--mm-ribbon-h);
  --mm-ribbon-header-h: 2.65rem;
  --mm-branch-panel-w: clamp(18rem, 32vw, 25rem);
  --mm-overlay-gap: 0.55rem;
  --mm-control-height: 2.12rem;
  --mm-settings-tile-bg: color-mix(in srgb, var(--md-default-fg-color) 5%, var(--md-default-bg-color));
  --mm-settings-tile-border: color-mix(in srgb, var(--md-default-fg-color) 13%, transparent);
  --kb-app-border: var(--mm-border);
  --kb-app-panel: var(--mm-panel);
  --kb-app-header-bg: color-mix(in srgb, var(--md-code-bg-color) 82%, var(--kb-app-panel));
  position: relative;
  isolation: isolate;
  z-index: 0;
  width:  100%;
  height: calc(100vh - var(--mm-header-h, 56px) - var(--mm-footer-h, 0px) - var(--kb-app-top-gap, 1rem));
  margin-top: var(--kb-app-top-gap, 1rem);
  overflow: hidden;
  background: var(--md-default-bg-color);
  font-family: "Atkinson Hyperlegible Next", "Segoe UI", sans-serif;
}

/* ── Sigma canvas ─────────────────────────────────────────────────────────── */
#mm-graph {
  position: absolute;
  inset: 0;
  z-index: 0;
  min-width: 0;
  min-height: 0;
  width: 100%;
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
  z-index: 6;
  pointer-events: none;
}
#mm-loading svg {
  color: var(--md-primary-fg-color);
  animation: mm-spin 1.2s linear infinite;
  opacity: 0.7;
}
@keyframes mm-spin { to { transform: rotate(360deg); } }

/* ── Settings ribbon ──────────────────────────────────────────────────────── */
#mm-panel-header {
  position: absolute;
  top: 0;
  left: var(--kb-app-page-gutter, 0.8rem);
  right: var(--kb-app-page-gutter, 0.8rem);
  z-index: 5;
  width: auto;
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 2.65rem;
  padding: 0.62rem 0.85rem;
  gap: 0.75rem;
  background: var(--kb-app-header-bg);
  border: 1px solid var(--mm-border);
  border-radius: 8px;
  user-select: none;
  font: inherit;
  text-align: left;
}
#mm-panel-title {
  margin: 0;
  font-size: 0.88rem;
  font-weight: 850;
  color: var(--md-default-fg-color);
  white-space: nowrap;
}

#mm-panel {
  position: absolute;
  top: calc(var(--mm-ribbon-header-h) + 0.35rem);
  left: var(--kb-app-page-gutter, 0.8rem);
  right: calc(var(--kb-app-page-gutter, 0.8rem) + var(--mm-branch-panel-w) + var(--mm-overlay-gap));
  width: auto;
  height: var(--mm-ribbon-h);
  max-height: var(--mm-ribbon-max-h);
  z-index: 4;
  background: var(--mm-panel);
  border: 1px solid var(--mm-border);
  border-radius: 8px;
  color: var(--md-default-fg-color);
  font-size: 0.82rem;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: opacity 0.18s ease, border-color 0.18s ease;
}
#mm-panel.body-collapsed {
  height: 0;
  max-height: 0;
  opacity: 0;
  pointer-events: none;
  border-color: transparent;
}

#mm-branch-panel {
  position: absolute;
  top: calc(var(--mm-ribbon-header-h) + 0.35rem);
  right: var(--kb-app-page-gutter, 0.8rem);
  bottom: var(--kb-app-page-gutter, 0.8rem);
  z-index: 4;
  display: flex;
  flex-direction: column;
  width: var(--mm-branch-panel-w);
  box-sizing: border-box;
  min-height: 0;
  padding: 0.62rem;
  border: 1px solid var(--mm-border);
  border-radius: 8px;
  background: var(--mm-panel);
  color: var(--md-default-fg-color);
  overflow: hidden;
  transform-origin: top;
  transition: opacity 0.18s ease, transform 0.18s ease, border-color 0.18s ease;
}
#mm-branch-panel.body-collapsed {
  opacity: 0;
  pointer-events: none;
  border-color: transparent;
  transform: scaleY(0);
}
.mm-branch-panel-head {
  flex: 0 0 auto;
  margin-bottom: 0.45rem;
}

#mm-panel-body {
  padding: 0.62rem;
  display: grid;
  gap: 0.52rem;
  align-content: start;
  flex: 1;
  min-height: 0;
  max-height: none;
  overflow-y: auto;
  overflow-x: clip;
  min-width: 0;
  box-sizing: border-box;
  scrollbar-width: thin;
  scrollbar-color: var(--md-default-fg-color--lighter) transparent;
}

/* ── Panel sections ───────────────────────────────────────────────────────── */
.mm-section {
  min-width: 0;
  max-width: 100%;
}
.mm-section-label {
  display: block;
  font-size: 0.68rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  color: var(--md-default-fg-color--light);
  font-weight: 600;
  margin-bottom: 5px;
}
.mm-section--actions {
  min-width: 5.8rem;
}
.mm-section--detail {
  flex: 1 1 17rem;
}
.mm-section--visibility {
  min-width: 8.4rem;
}

/* Settings layout */
.mm-settings-section {
  display: grid;
  min-width: 0;
  min-height: 0;
  gap: 0.5rem;
}
.mm-settings-grid {
  display: grid;
  min-width: 0;
  min-height: 0;
  gap: 0.46rem;
  grid-template-columns: minmax(11.75rem, 1fr) minmax(5.8rem, 0.4fr) minmax(8.4rem, 0.5fr);
  grid-template-areas:
    "detail fit labels"
    "relevance relevance relevance";
  align-items: end;
}
.mm-settings-grid > .mm-section--detail { grid-area: detail; }
.mm-settings-grid > .mm-section--actions { grid-area: fit; }
.mm-settings-grid > .mm-section--visibility { grid-area: labels; }
.mm-settings-grid > .mm-relevance-panel { grid-area: relevance; }
.mm-bento-tile {
  min-width: 0;
  min-height: 0;
  box-sizing: border-box;
  padding: 0.56rem;
  border: 1px solid var(--mm-soft-border);
  border-radius: 8px;
  overflow: hidden;
}
.mm-settings-section .mm-bento-tile {
  background: var(--mm-settings-tile-bg);
  border-color: var(--mm-settings-tile-border);
}
/* Selected-node relevance filter */
.mm-relevance-panel {
  flex: 1 1 100%;
  padding: 0.6rem;
  border: 1px solid var(--mm-soft-border);
  border-radius: 8px;
  background: color-mix(in srgb, var(--md-default-bg-color) 42%, transparent);
}
.mm-relevance-panel[hidden] { display: none; }
.mm-relevance-head,
.mm-relevance-options,
.mm-filter-row,
.mm-relevance-foot {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
}
.mm-relevance-ego {
  margin: 0.42rem 0 0.5rem;
  color: var(--md-default-fg-color);
  font-size: 0.76rem;
  font-weight: 700;
  line-height: 1.3;
}
.mm-switch,
.mm-filter-toggle {
  display: inline-flex;
  align-items: center;
  gap: 0.28rem;
  color: var(--md-default-fg-color--light);
  font-size: 0.72rem;
  cursor: pointer;
}
.mm-switch input,
.mm-filter-toggle input {
  margin: 0;
  accent-color: var(--md-accent-fg-color);
}
.mm-relevance-options {
  flex-wrap: wrap;
  justify-content: flex-start;
  margin-bottom: 0.5rem;
}
.mm-relevance-options select {
  margin-left: auto;
  min-height: 1.45rem;
  border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 6px;
  background: var(--md-default-fg-color--lightest);
  color: var(--md-default-fg-color);
  font-size: 0.72rem;
}
.mm-filter-toggle {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
  align-items: stretch;
  gap: 0.55rem;
  width: 100%;
}
.mm-filter-toggle + .mm-filter-toggle { margin-top: 0.42rem; }
.mm-filter-check {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 2.55rem;
  padding-right: 0.22rem;
}
.mm-filter-check input[type="checkbox"] {
  width: 2.25rem;
  height: 2.25rem;
  flex: 0 0 auto;
}
.mm-filter-body {
  display: grid;
  gap: 0.2rem;
  min-width: 0;
}
.mm-filter-row,
.mm-relevance-foot {
  color: var(--md-default-fg-color--light);
  font-size: 0.7rem;
}
.mm-filter-row span:last-child,
.mm-relevance-foot span:last-child {
  color: var(--md-primary-fg-color);
  font-variant-numeric: tabular-nums;
}
#mm-relevance-similarity,
#mm-relevance-distance {
  width: 100%;
  accent-color: var(--md-accent-fg-color);
}

/* Detail level and visibility toggles */
.mm-detail-controls,
.mm-visibility-controls {
  display: grid;
  gap: 4px;
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
}
.mm-detail-controls {
  --mm-detail-button-size: var(--mm-control-height);
  grid-template-columns: repeat(5, var(--mm-detail-button-size));
  justify-content: start;
}
.mm-visibility-controls {
  grid-template-columns: minmax(0, 1fr);
}
.mm-detail-controls button,
.mm-visibility-controls button {
  min-width: 0;
  width: 100%;
  max-width: 100%;
  box-sizing: border-box;
  background: var(--md-default-fg-color--lightest);
  border: 1px solid var(--md-default-fg-color--lighter);
  color: var(--md-default-fg-color--light);
  min-height: var(--mm-control-height);
  padding: 4px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.72rem;
  line-height: 1.1;
  white-space: nowrap;
}
.mm-detail-controls button {
  display: grid;
  place-items: center;
  width: var(--mm-detail-button-size);
  height: var(--mm-detail-button-size);
  min-height: 0;
  aspect-ratio: 1;
}
.mm-label-toggle {
  display: grid;
  grid-template-columns: minmax(0, 1fr) auto;
  align-items: center;
  gap: 0.46rem;
  text-align: left;
}
.mm-label-toggle-track {
  position: relative;
  display: inline-grid;
  align-items: center;
  width: 2.35rem;
  height: 1.05rem;
  padding-inline: 0.34rem;
  border-radius: 999px;
  background: color-mix(in srgb, currentColor 18%, transparent);
  box-shadow: inset 0 0 0 1px color-mix(in srgb, currentColor 30%, transparent);
  font-size: 0.58rem;
  font-weight: 850;
  line-height: 1;
  text-transform: uppercase;
}
.mm-label-toggle-thumb {
  position: absolute;
  top: 0.16rem;
  left: 0.16rem;
  width: 0.6rem;
  height: 0.6rem;
  border-radius: 999px;
  background: currentColor;
  transition: transform 0.16s ease;
}
.mm-label-toggle[aria-checked="true"] .mm-label-toggle-thumb {
  transform: translateX(1.28rem);
}
.mm-label-toggle-text {
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
}
.mm-label-toggle-state {
  justify-self: end;
}
.mm-detail-controls button:hover,
.mm-visibility-controls button:hover {
  color: var(--md-default-fg-color);
  border-color: var(--md-default-fg-color--light);
}
.mm-detail-controls button.active,
.mm-visibility-controls button[aria-checked="true"] {
  background: color-mix(in srgb, var(--md-accent-fg-color) 16%, var(--md-default-bg-color));
  border-color: var(--md-accent-fg-color);
  color: var(--md-default-fg-color);
  font-weight: 600;
}
.mm-detail-controls button:disabled {
  cursor: not-allowed;
  opacity: 0.38;
}
.mm-detail-icon {
  position: relative;
  display: grid;
  width: 1.45rem;
  height: 1.45rem;
  color: currentColor;
}
.mm-detail-dot {
  display: block;
  width: 0.5rem;
  height: 0.5rem;
  border-radius: 999px;
  background: currentColor;
  box-shadow: 0 0 0 1px color-mix(in srgb, currentColor 18%, transparent);
}
.mm-detail-icon--die {
  grid-template-columns: repeat(3, 1fr);
  grid-template-rows: repeat(3, 1fr);
  align-items: center;
  justify-items: center;
}
.mm-detail-icon--die-1 .mm-detail-dot:nth-child(1) { grid-area: 2 / 2; }
.mm-detail-icon--die-2 .mm-detail-dot:nth-child(1) { grid-area: 2 / 1; }
.mm-detail-icon--die-2 .mm-detail-dot:nth-child(2) { grid-area: 2 / 3; }
.mm-detail-icon--die-3 .mm-detail-dot:nth-child(1) { grid-area: 1 / 2; }
.mm-detail-icon--die-3 .mm-detail-dot:nth-child(2) { grid-area: 3 / 1; }
.mm-detail-icon--die-3 .mm-detail-dot:nth-child(3) { grid-area: 3 / 3; }
.mm-detail-icon--die-4 .mm-detail-dot:nth-child(1) { grid-area: 1 / 1; }
.mm-detail-icon--die-4 .mm-detail-dot:nth-child(2) { grid-area: 1 / 3; }
.mm-detail-icon--die-4 .mm-detail-dot:nth-child(3) { grid-area: 3 / 1; }
.mm-detail-icon--die-4 .mm-detail-dot:nth-child(4) { grid-area: 3 / 3; }
.mm-detail-icon--items {
  width: 1.72rem;
  height: 1.72rem;
}
.mm-detail-icon--items svg {
  display: block;
  width: 100%;
  height: 100%;
  fill: currentColor;
  pointer-events: none;
}

/* Branch filter */
#mm-category-filters {
  display: block;
  flex: 1 1 auto;
  width: 100%;
  min-width: 0;
  min-height: 0;
  padding: 0.12rem 0.75rem 0.55rem;
  box-sizing: border-box;
  overflow: auto;
  scrollbar-width: thin;
}

/* Action buttons */
.mm-actions {
  display: grid;
  align-items: end;
  gap: 0.4rem;
  min-height: 0;
}
.mm-actions button {
  width: 100%;
  background: var(--md-default-fg-color--lightest);
  border: 1px solid var(--md-default-fg-color--lighter);
  color: var(--md-default-fg-color--light);
  height: var(--mm-control-height);
  min-height: var(--mm-control-height);
  padding: 0.48rem;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.78rem;
  transition: background 0.15s;
}
.mm-actions button:hover { background: var(--md-default-fg-color--lighter); }

/* ── Tooltip ──────────────────────────────────────────────────────────────── */
#mm-tooltip,
#mm-hover-tooltip {
  position: fixed;
  z-index: 7;
  display: none;
  background: var(--md-code-bg-color);
  border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 10px;
  padding: 11px 14px;
  box-sizing: border-box;
  overflow-y: hidden;
  pointer-events: none;
  backdrop-filter: blur(10px);
  box-shadow: var(--md-shadow-z2);
  font-family: "Atkinson Hyperlegible Next", "Segoe UI", sans-serif;
}
#mm-tooltip {
  max-width: min(34rem, calc(100vw - 24px));
  max-height: 65vh;
}
#mm-hover-tooltip {
  z-index: 8;
  max-width: min(18rem, calc(100vw - 24px));
  max-height: 40vh;
  padding: 7px 10px;
  border-radius: 8px;
  background: color-mix(in srgb, var(--md-code-bg-color) 96%, transparent);
  box-shadow: 0 8px 22px color-mix(in srgb, #000 18%, transparent);
}
#mm-tooltip.visible { display: block; }
#mm-hover-tooltip.visible { display: block; }
#mm-tooltip.pinned  { pointer-events: auto; border-color: var(--md-accent-fg-color--transparent); overflow-y: auto; scrollbar-width: thin; scrollbar-color: var(--md-default-fg-color--lighter) transparent; }

.tt-title   { font-size: 0.83rem; font-weight: 600; color: var(--md-default-fg-color); line-height: 1.35; margin-bottom: 4px; }
.tt-short-label { font-size: 0.74rem; font-weight: 750; color: var(--md-primary-fg-color); line-height: 1.25; margin: -1px 0 5px; }
.tt-link    { display: block; font-size: 0.75rem; color: var(--md-typeset-a-color); text-decoration: none; margin-bottom: 7px; }
.tt-link:hover { color: var(--md-primary-fg-color--dark); text-decoration: underline; }
.tt-meta    { font-size: 0.73rem; color: var(--md-default-fg-color--light); margin-bottom: 2px; }
.tt-tags    { font-size: 0.7rem;  color: var(--md-primary-fg-color--light); margin: 5px 0; line-height: 1.5; }
.tt-summary { font-size: 0.73rem; color: var(--md-default-fg-color--light); margin-top: 6px; line-height: 1.45; }
.tt-actions { margin-top: 0.62rem; }
.tt-hint    { font-size: 0.68rem; color: var(--md-default-fg-color--lighter); margin-top: 8px; font-style: italic; }
.tt-list    { margin: 7px 0 0; padding-left: 1rem; color: var(--md-default-fg-color--light); font-size: 0.72rem; line-height: 1.35; }
.tt-list li { margin-bottom: 3px; }
.tt-mini-title { font-size: 0.76rem; font-weight: 700; color: var(--md-default-fg-color); line-height: 1.25; }
.tt-mini-subtitle { font-size: 0.69rem; color: var(--md-default-fg-color--light); line-height: 1.25; margin-top: 3px; }
.tt-mini-meta  { font-size: 0.68rem; color: var(--md-default-fg-color--light); line-height: 1.25; margin-top: 2px; }

/* ── Mobile modal: same paper-detail pattern as Timeline ─────────────────── */
.mm-modal {
  position: fixed;
  inset: var(--mm-header-h, 56px) 0 var(--mm-footer-h, 0px) 0;
  z-index: 80;
  display: grid;
  place-items: center;
  padding: 1rem;
  background: color-mix(in srgb, #000 48%, transparent);
  backdrop-filter: blur(3px);
}
.mm-modal[hidden] { display: none; }
.mm-modal-card {
  display: grid;
  grid-template-rows: auto minmax(0, 1fr);
  width: min(48rem, calc(100vw - 1.2rem));
  max-height: min(82vh, calc(100vh - var(--mm-header-h, 56px) - var(--mm-footer-h, 0px) - 2rem), 48rem);
  max-height: min(82vh, calc(100dvh - var(--mm-header-h, 56px) - var(--mm-footer-h, 0px) - 2rem), 48rem);
  border: 1px solid var(--mm-border);
  border-radius: 8px;
  background: var(--md-default-bg-color);
  box-shadow: 0 22px 60px color-mix(in srgb, #000 34%, transparent);
  overflow: hidden;
}
.mm-modal-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  padding: 0.82rem 0.95rem;
  border-bottom: 1px solid var(--mm-border);
  background: var(--mm-panel);
}
.mm-modal-head h2 {
  margin: 0;
  font-size: 1rem;
  line-height: 1.25;
}
.mm-modal-close {
  display: grid;
  place-items: center;
  flex: 0 0 auto;
  width: 2rem;
  height: 2rem;
  border: 1px solid var(--mm-border);
  border-radius: 999px;
  background: var(--md-default-bg-color);
  color: var(--md-default-fg-color);
  font: inherit;
  font-size: 1.1rem;
  line-height: 1;
  cursor: pointer;
}
.mm-modal-close:hover {
  border-color: var(--mm-blue);
  background: color-mix(in srgb, var(--mm-blue) 8%, transparent);
}
.mm-modal-body {
  min-height: 0;
  overflow: auto;
  padding: 0.9rem 0.95rem 1rem;
  scrollbar-width: thin;
}
.mm-modal-body p {
  margin: 0.55rem 0 0;
  color: var(--md-default-fg-color--light);
  font-size: 0.84rem;
  line-height: 1.55;
}
.mm-detail-kicker {
  margin-bottom: 0.25rem;
  color: var(--mm-gold);
  font-size: 0.72rem;
  font-weight: 900;
}
.mm-detail-title,
.mm-summary,
.mm-abstract {
  color: var(--md-default-fg-color) !important;
}
.mm-detail-title { font-weight: 700; }
.mm-modal-section-title {
  margin: 0.9rem 0 0.25rem;
  color: var(--md-default-fg-color--light);
  font-size: 0.7rem;
  font-weight: 900;
  text-transform: uppercase;
}
.mm-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.28rem;
  margin-top: 0.72rem;
}
.mm-tags span {
  padding: 0.16rem 0.42rem;
  border: 1px solid var(--mm-soft-border);
  border-radius: 999px;
  background: color-mix(in srgb, var(--mm-teal) 8%, transparent);
  color: var(--md-default-fg-color--light);
  font-size: 0.68rem;
}
.mm-detail-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.42rem;
  margin-top: 0.9rem;
}

@media (max-width: 1260px) and (min-width: 761px) {
  .mm-settings-grid {
    grid-template-columns: minmax(11.75rem, 1fr) minmax(5.8rem, 0.45fr) minmax(8.4rem, 0.55fr);
    grid-template-areas:
      "detail fit labels"
      "relevance relevance relevance";
  }
}

@media (max-width: 760px) {
  #mm-app {
    --mm-ribbon-h: min(38vh, 18rem);
    --mm-ribbon-h: min(38dvh, 18rem);
    --mm-ribbon-max-h: var(--mm-ribbon-h);
    --mm-branch-panel-w: auto;
  }

  #mm-panel-header,
  #mm-panel,
  #mm-branch-panel {
    left: 0;
    right: 0;
  }

  #mm-panel {
    height: var(--mm-ribbon-h);
  }

  #mm-branch-panel {
    top: calc(var(--mm-ribbon-header-h) + var(--mm-ribbon-h) + 0.7rem);
    bottom: var(--mm-footer-h, 0px);
    width: auto;
    max-height: none;
    padding-inline: 0.5rem;
  }

  #mm-panel-body {
    display: grid;
    grid-template-columns: 1fr;
    align-items: stretch;
    padding-inline: 0.5rem;
  }

  #mm-panel-header {
    padding-inline: 0.55rem;
  }

  .mm-bento-tile,
  .mm-relevance-panel {
    padding-inline: 0.45rem;
  }

  .mm-settings-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    grid-template-areas:
      "detail detail"
      "fit labels"
      "relevance relevance";
    align-items: stretch;
  }

  .mm-detail-controls,
  .mm-visibility-controls {
    width: 100%;
  }

  #mm-tooltip {
    width: calc(100vw - 24px);
    max-width: calc(100vw - 24px);
    max-height: min(70vh, calc(100vh - var(--mm-header-h, 56px) - var(--mm-footer-h, 0px) - 24px));
    padding: 12px 14px;
  }
  .tt-title   { font-size: 0.9rem; line-height: 1.35; }
  .tt-short-label { font-size: 0.8rem; }
  .tt-link    { font-size: 0.8rem; }
  .tt-meta    { font-size: 0.78rem; }
  .tt-tags    { font-size: 0.76rem; line-height: 1.45; }
  .tt-summary { font-size: 0.78rem; line-height: 1.48; }
  .tt-hint    { font-size: 0.72rem; }
  .mm-modal {
    inset: 50vh 0 var(--mm-footer-h, 0px) 0;
    inset: 50dvh 0 var(--mm-footer-h, 0px) 0;
    place-items: stretch;
    padding: 0.42rem var(--kb-app-page-gutter, 0.32rem);
    background: transparent;
    backdrop-filter: none;
    pointer-events: none;
  }
  .mm-modal-card {
    align-self: end;
    width: calc(100vw - (2 * var(--kb-app-page-gutter, 0.32rem)));
    height: 100%;
    max-height: 100%;
    pointer-events: auto;
  }
  .mm-modal-head,
  .mm-modal-body {
    padding-inline: 0.55rem;
  }
}
</style>

<div id="mm-app" class="kb-app-page kb-app-page--bleed">

  <!-- Loading spinner shown while the graph initialises -->
  <div id="mm-loading">
    <svg width="40" height="40" viewBox="0 0 40 40" fill="none" stroke="currentColor" stroke-width="3">
      <circle cx="20" cy="20" r="16" stroke-opacity="0.25"/>
      <path d="M20 4 a16 16 0 0 1 16 16" stroke-linecap="round"/>
    </svg>
    Loading…
  </div>

  <!-- Settings ribbon header: always visible above the graph -->
  <div id="mm-panel-header" class="kb-app-header">
    <span id="mm-panel-title" class="kb-app-header-title">Map</span>
    <button id="mm-panel-hide-btn" class="kb-app-header-action" type="button" title="Show Settings" aria-expanded="false" aria-controls="mm-panel mm-branch-panel">Show Settings</button>
  </div>

  <!-- Settings ribbon body: collapses upward on hide -->
  <div id="mm-panel" class="body-collapsed">
    <div id="mm-panel-body">

      <section id="mm-settings" class="mm-settings-section" aria-label="Map settings">
        <div class="mm-settings-grid">
          <div class="mm-section mm-section--detail">
            <span class="mm-section-label">Level of Detail</span>
            <div id="mm-detail-controls" class="mm-detail-controls"></div>
          </div>

          <div class="mm-section mm-section--actions mm-actions">
            <button id="mm-fit-btn" type="button">Fit View</button>
          </div>

          <div class="mm-section mm-section--visibility">
            <div class="mm-visibility-controls">
              <button id="mm-labels-toggle" class="mm-label-toggle" type="button" role="switch" aria-checked="true" aria-label="Node labels" title="Hide node labels">
                <span class="mm-label-toggle-text">Node labels</span>
                <span class="mm-label-toggle-track" aria-hidden="true">
                  <span class="mm-label-toggle-state">On</span>
                  <span class="mm-label-toggle-thumb"></span>
                </span>
              </button>
            </div>
          </div>

          <div id="mm-relevance-panel" class="mm-section mm-relevance-panel" hidden>
            <div class="mm-relevance-head">
              <span class="mm-section-label" style="margin:0">Selected-node filter</span>
              <label class="mm-switch">
                <input id="mm-relevance-enabled" type="checkbox">
                <span>Enable</span>
              </label>
            </div>
            <div id="mm-relevance-ego" class="mm-relevance-ego"></div>
            <div class="mm-relevance-options">
              <select id="mm-relevance-mode" aria-label="Combine selected-node filters">
                <option value="and">And</option>
                <option value="or">Or</option>
              </select>
            </div>
            <label class="mm-filter-toggle">
              <span class="mm-filter-check">
                <input id="mm-relevance-semantic" type="checkbox" checked>
              </span>
              <span class="mm-filter-body">
                <span class="mm-filter-row">
                  <span>Semantic similarity</span>
                  <span id="mm-relevance-similarity-val">0.25</span>
                </span>
                <input id="mm-relevance-similarity" type="range" min="0" max="100" step="1" value="25">
              </span>
            </label>
            <label class="mm-filter-toggle">
              <span class="mm-filter-check">
                <input id="mm-relevance-taxonomy" type="checkbox" checked>
              </span>
              <span class="mm-filter-body">
                <span class="mm-filter-row">
                  <span>Tree proximity</span>
                  <span id="mm-relevance-distance-val">0.25</span>
                </span>
                <input id="mm-relevance-distance" type="range" min="0" max="100" step="1" value="25">
              </span>
            </label>
            <div class="mm-relevance-foot">
              <span id="mm-relevance-status">Filter off</span>
              <span id="mm-relevance-match-count">…</span>
            </div>
          </div>

        </div>
      </section>

    </div>
  </div>

  <aside id="mm-branch-panel" class="body-collapsed" aria-label="Map branch navigator">
    <div class="mm-branch-panel-head">
      <span class="mm-section-label">Branch</span>
    </div>
    <div id="mm-category-filters"></div>
  </aside>

  <!-- Tooltip (positioned by JS) -->
  <div id="mm-tooltip"></div>
  <div id="mm-hover-tooltip"></div>

  <div id="mm-modal" class="mm-modal" hidden>
    <article class="mm-modal-card" role="dialog" aria-modal="true" aria-labelledby="mm-modal-title">
      <header class="mm-modal-head">
        <h2 id="mm-modal-title">Paper</h2>
        <button id="mm-modal-close" class="mm-modal-close" type="button" aria-label="Close paper details">&times;</button>
      </header>
      <div id="mm-modal-body" class="mm-modal-body"></div>
    </article>
  </div>

  <!-- Sigma canvas -->
  <div id="mm-graph"></div>

</div>

<!-- kb:app-scripts map -->
<!-- /kb:app-scripts -->
<script>
(function () {
  function applyMmSizes() {
    var header = document.querySelector('.md-header');
    var footer = document.querySelector('.md-footer');
    var hh = header ? header.getBoundingClientRect().height : 56;
    var fh = footer ? footer.getBoundingClientRect().height : 0;
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
