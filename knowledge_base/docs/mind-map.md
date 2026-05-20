---
hide:
  - toc
---

# Mind Map

<style>
/* ── Derived vars: transparency adjustments on MkDocs palette tokens ─────── */
:root {
  --mm-node-muted:         #a3adb8;
  --mm-node-muted-related: #7f8b97;
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
  --mm-muted-label:        #c8d0d8;
  --mm-selected-ring:      #f1c232;
  --mm-selected-label:     #111111;
  --mm-blue:               var(--kb-color-blue);
  --mm-teal:               var(--kb-color-teal);
  --mm-rose:               var(--kb-color-rose);
  --mm-gold:               var(--kb-color-gold);
  --mm-border:             color-mix(in srgb, var(--md-default-fg-color) 18%, transparent);
  --mm-soft-border:        color-mix(in srgb, var(--md-default-fg-color) 11%, transparent);
  --mm-panel:              color-mix(in srgb, var(--md-code-bg-color) 82%, #050910);
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
  --mm-ribbon-max-h: min(38vh, 28rem);
  --mm-ribbon-header-h: 2.65rem;
  position: relative;
  isolation: isolate;
  z-index: 0;
  width:  100%;
  height: calc(100vh - var(--mm-header-h, 56px) - var(--mm-footer-h, 0px));
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
  left: 0;
  right: 0;
  z-index: 5;
  width: 100%;
  box-sizing: border-box;
  display: flex;
  align-items: center;
  justify-content: space-between;
  min-height: 2.65rem;
  padding: 0.62rem 0.85rem;
  gap: 0.75rem;
  background: color-mix(in srgb, var(--md-code-bg-color) 94%, transparent);
  border: 1px solid var(--mm-border);
  border-left: 0;
  border-right: 0;
  backdrop-filter: blur(14px);
  cursor: pointer;
  user-select: none;
}
#mm-panel-header:hover { background: color-mix(in srgb, var(--md-default-fg-color) 6%, transparent); }
#mm-panel-header h3 {
  margin: 0;
  font-size: 0.88rem;
  font-weight: 850;
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

#mm-panel {
  position: absolute;
  top: var(--mm-ribbon-header-h);
  left: 0;
  right: 0;
  width: 100%;
  max-height: var(--mm-ribbon-max-h);
  z-index: 4;
  background: color-mix(in srgb, var(--md-code-bg-color) 94%, transparent);
  border-bottom: 1px solid var(--mm-border);
  backdrop-filter: blur(14px);
  color: var(--md-default-fg-color);
  font-size: 0.82rem;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  transition: max-height 0.25s ease, opacity 0.18s ease, border-color 0.18s ease;
}
#mm-panel.body-collapsed {
  max-height: 0;
  opacity: 0;
  pointer-events: none;
  border-color: transparent;
}

#mm-panel-body {
  padding: 0.85rem;
  display: flex;
  flex-wrap: wrap;
  align-items: end;
  gap: 0.65rem;
  flex: 1;
  max-height: var(--mm-ribbon-max-h);
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
  flex: 1 1 12rem;
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
  flex: 0 0 7rem;
}
.mm-section--detail {
  flex: 1 1 17rem;
}
.mm-section--visibility {
  flex: 0 1 9rem;
}
.mm-section--search {
  flex: 2 1 18rem;
}
.mm-section--categories {
  flex: 2 1 28rem;
}
.mm-section--types {
  flex: 1 1 13rem;
}

/* Search */
.mm-search-wrap {
  position: relative;
  display: flex;
  align-items: center;
}
#mm-search {
  width: 100%;
  box-sizing: border-box;
  background: var(--md-default-fg-color--lightest);
  border: 1px solid var(--md-default-fg-color--lighter);
  color: var(--md-default-fg-color);
  padding: 6px 2rem 6px 10px;
  border-radius: 7px;
  font-size: 0.82rem;
  outline: none;
}
#mm-search::placeholder { color: var(--md-default-fg-color--lighter); }
#mm-search:focus {
  border-color: var(--md-accent-fg-color);
  background: var(--md-default-fg-color--lightest);
}
#mm-search-clear {
  position: absolute;
  right: 4px;
  display: grid;
  place-items: center;
  width: 1.55rem;
  height: 1.55rem;
  border: 0;
  border-radius: 999px;
  background: transparent;
  color: var(--md-default-fg-color--light);
  cursor: pointer;
  font-size: 1rem;
  line-height: 1;
}
#mm-search-clear:hover {
  background: var(--md-default-fg-color--lightest);
  color: var(--md-default-fg-color);
}
#mm-search-clear[hidden] { display: none; }

/* Selected-node relevance filter */
.mm-relevance-panel {
  flex: 1 1 100%;
  padding: 0.72rem;
  border: 1px solid var(--mm-soft-border);
  border-radius: 8px;
  background: color-mix(in srgb, var(--md-default-bg-color) 42%, transparent);
}
.mm-relevance-panel[hidden] { display: none; }
.mm-relevance-panel[hidden] + .mm-settings-separator { display: none; }
.mm-settings-separator {
  display: none;
  flex: 1 1 100%;
  height: 1px;
  background: var(--mm-soft-border);
}
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
  grid-template-columns: repeat(5, minmax(0, 1fr));
}
.mm-visibility-controls {
  grid-template-columns: repeat(2, minmax(0, 1fr));
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
  padding: 5px 4px;
  border-radius: 6px;
  cursor: pointer;
  font-size: 0.72rem;
  line-height: 1.1;
  white-space: nowrap;
}
.mm-detail-controls button:hover,
.mm-visibility-controls button:hover {
  color: var(--md-default-fg-color);
  border-color: var(--md-default-fg-color--light);
}
.mm-detail-controls button.active,
.mm-visibility-controls button[aria-pressed="true"] {
  background: color-mix(in srgb, var(--md-accent-fg-color) 16%, var(--md-default-bg-color));
  border-color: var(--md-accent-fg-color);
  color: var(--md-default-fg-color);
  font-weight: 600;
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
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(12rem, 1fr));
  gap: 3px 0.7rem;
  max-height: 11rem;
  overflow: auto;
  padding-right: 0.25rem;
  scrollbar-width: thin;
}
#mm-type-filters {
  display: flex;
  flex-direction: column;
  gap: 3px;
}
.mm-type-trigger {
  position: relative;
  display: grid;
  grid-template-columns: minmax(0, 1fr) 0.7rem;
  align-items: center;
  gap: 0.62rem;
  box-sizing: border-box;
  width: 100%;
  min-height: 2.35rem;
  margin: 0;
  padding: 0.48rem 0.74rem;
  border: 1px solid var(--mm-border);
  border-radius: 8px;
  background: var(--md-default-fg-color--lightest);
  color: var(--md-default-fg-color);
  cursor: pointer;
  font: inherit;
  font-size: 0.78rem;
  font-weight: 700;
  line-height: 1.25;
}
.mm-type-trigger span {
  min-width: 0;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.mm-type-trigger::after {
  content: "";
  width: 0.48rem;
  height: 0.48rem;
  border-right: 2px solid currentColor;
  border-bottom: 2px solid currentColor;
  transform: rotate(45deg) translateY(-0.12rem);
  transition: transform 0.16s ease;
}
.mm-type-trigger[aria-expanded="true"] {
  border-color: var(--md-accent-fg-color);
  box-shadow: 0 0 0 4px color-mix(in srgb, var(--md-accent-fg-color) 12%, transparent);
}
.mm-type-trigger[aria-expanded="true"]::after {
  transform: rotate(225deg) translate(-0.08rem, -0.08rem);
}
.mm-type-dialog {
  position: fixed;
  inset-inline: 0;
  top: calc(var(--mm-header-h, 56px) + 0.75rem);
  bottom: calc(var(--mm-footer-h, 0px) + 0.75rem);
  width: min(25rem, calc(100vw - 2rem));
  height: auto;
  max-height: calc(100vh - var(--mm-header-h, 56px) - var(--mm-footer-h, 0px) - 1.5rem);
  max-height: calc(100dvh - var(--mm-header-h, 56px) - var(--mm-footer-h, 0px) - 1.5rem);
  margin: auto;
  padding: 0;
  border: 1px solid var(--mm-border);
  border-radius: 8px;
  background: var(--md-default-bg-color);
  color: var(--md-default-fg-color);
  box-shadow: 0 24px 60px color-mix(in srgb, #000000 30%, transparent);
}
.mm-type-dialog::backdrop {
  background: color-mix(in srgb, #000000 38%, transparent);
}
.mm-type-panel {
  display: grid;
  grid-template-rows: auto minmax(0, 1fr);
  max-height: inherit;
  overflow: hidden;
}
.mm-type-head {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  padding: 0.72rem 0.82rem;
  border-bottom: 1px solid var(--mm-border);
  background: color-mix(in srgb, var(--md-code-bg-color) 74%, var(--md-default-bg-color));
}
.mm-type-head h2 {
  margin: 0;
  color: var(--md-default-fg-color);
  font-size: 0.86rem;
  font-weight: 850;
  letter-spacing: 0;
}
.mm-type-close {
  display: grid;
  place-items: center;
  width: 2.05rem;
  height: 2.05rem;
  padding: 0;
  border: 1px solid color-mix(in srgb, var(--md-default-fg-color) 12%, transparent);
  border-radius: 999px;
  background: color-mix(in srgb, var(--md-default-fg-color) 7%, var(--md-default-bg-color));
  color: var(--md-default-fg-color);
  cursor: pointer;
  transition: border-color 0.16s ease, background 0.16s ease, color 0.16s ease, transform 0.16s ease;
}
.mm-type-close svg {
  width: 1.1rem;
  height: 1.1rem;
  fill: currentColor;
  pointer-events: none;
}
.mm-type-close:hover {
  border-color: var(--md-accent-fg-color);
  background: color-mix(in srgb, var(--md-accent-fg-color) 14%, var(--md-default-bg-color));
  color: var(--md-default-fg-color);
  transform: scale(1.04);
}
.mm-type-list {
  display: grid;
  grid-template-columns: 1fr;
  gap: 0.32rem;
  width: 100%;
  box-sizing: border-box;
  max-height: calc(100vh - var(--mm-header-h, 56px) - var(--mm-footer-h, 0px) - 8.2rem);
  max-height: calc(100dvh - var(--mm-header-h, 56px) - var(--mm-footer-h, 0px) - 8.2rem);
  padding: 0.68rem;
  overflow: auto;
}
.mm-type-actions {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.4rem;
  box-sizing: border-box;
  width: 100%;
  padding: 0.68rem 0.68rem 0.62rem;
  border-bottom: 1px solid var(--mm-soft-border);
}
.mm-type-actions button {
  width: 100%;
  min-height: 2.5rem;
  padding: 0.42rem 0.82rem;
  border: 1px solid var(--mm-border);
  border-radius: 8px;
  background: var(--md-default-bg-color);
  color: var(--md-default-fg-color);
  cursor: pointer;
  font: inherit;
  font-size: 0.76rem;
  font-weight: 800;
}
.mm-type-actions button:hover {
  border-color: var(--md-accent-fg-color);
  background: color-mix(in srgb, var(--md-accent-fg-color) 8%, transparent);
}
.mm-cat-item {
  display: flex;
  align-items: center;
  gap: 7px;
  cursor: pointer;
  padding: 2px 0;
}
.mm-cat-item:hover .mm-cat-name { color: var(--md-default-fg-color); }
.mm-type-item {
  width: 100%;
  min-height: 2.35rem;
  box-sizing: border-box;
  padding: 0.34rem 0.48rem;
  border: 1px solid var(--mm-soft-border);
  border-radius: 8px;
  background: var(--md-default-bg-color);
  color: var(--md-default-fg-color);
  font: inherit;
  line-height: 1.25;
  text-align: left;
}
.mm-type-item:hover {
  border-color: var(--md-accent-fg-color);
  background: color-mix(in srgb, var(--md-accent-fg-color) 7%, transparent);
}
.mm-type-item[aria-pressed="true"],
.mm-type-item.is-selected {
  border-color: color-mix(in srgb, var(--md-accent-fg-color) 58%, transparent);
  background: color-mix(in srgb, var(--md-accent-fg-color) 13%, var(--md-default-bg-color));
}
.mm-cat-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  flex-shrink: 0;
}
.mm-type-chip {
  display: grid;
  place-items: center;
  min-width: 2.7rem;
  min-height: 1.32rem;
  padding: 1px 5px;
  border: 1px solid var(--md-default-fg-color--lighter);
  border-radius: 999px;
  color: var(--md-default-fg-color--light);
  font-size: 0.62rem;
  font-weight: 700;
  line-height: 1.25;
  text-align: center;
}
.mm-type-item[aria-pressed="true"] .mm-type-chip,
.mm-type-item.is-selected .mm-type-chip {
  border-color: var(--md-accent-fg-color);
  color: var(--md-default-fg-color);
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
.mm-type-trigger:focus-visible,
.mm-type-item:focus-visible,
.mm-type-close:focus-visible,
.mm-type-actions button:focus-visible {
  border-color: var(--md-accent-fg-color);
  outline: 2px solid color-mix(in srgb, var(--md-accent-fg-color) 24%, transparent);
  outline-offset: 1px;
  box-shadow: 0 0 0 4px color-mix(in srgb, var(--md-accent-fg-color) 10%, transparent);
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
.mm-cat-group-toggle .mm-cat-dot {
  width: 9px;
  height: 9px;
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
.mm-super-group {
  margin: 3px 0 5px;
}
.mm-super-group > .mm-cat-group-header {
  padding-top: 5px;
}
.mm-super-group > .mm-cat-group-header .mm-cat-group-name {
  color: var(--md-default-fg-color);
  font-size: 0.78rem;
}
.mm-super-group > .mm-cat-group-items {
  border-left: 1px solid var(--md-default-fg-color--lightest);
  margin-left: 5px;
  padding-left: 12px;
}

/* Action buttons */
.mm-actions {
  display: flex;
  gap: 0.4rem;
  min-height: 2.35rem;
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

@media (max-width: 700px) {
  #mm-app {
    --mm-ribbon-max-h: min(58vh, 34rem);
  }

  #mm-panel-body {
    display: grid;
    grid-template-columns: 1fr;
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
  .tt-link    { font-size: 0.8rem; }
  .tt-meta    { font-size: 0.78rem; }
  .tt-tags    { font-size: 0.76rem; line-height: 1.45; }
  .tt-summary { font-size: 0.78rem; line-height: 1.48; }
  .tt-hint    { font-size: 0.72rem; }
  .mm-modal { padding: 0.55rem; }
  .mm-modal-card {
    width: calc(100vw - 1.1rem);
    max-height: min(88vh, calc(100vh - var(--mm-header-h, 56px) - var(--mm-footer-h, 0px) - 1.1rem));
    max-height: min(88vh, calc(100dvh - var(--mm-header-h, 56px) - var(--mm-footer-h, 0px) - 1.1rem));
  }
}
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

  <!-- Settings ribbon header: always visible above the graph -->
  <div id="mm-panel-header" title="Show Settings">
    <h3>Mind Map</h3>
    <button id="mm-panel-hide-btn">Show Settings</button>
  </div>

  <!-- Settings ribbon body: collapses upward on hide -->
  <div id="mm-panel" class="body-collapsed">
    <div id="mm-panel-body">

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
              <span id="mm-relevance-similarity-val">0.67</span>
            </span>
            <input id="mm-relevance-similarity" type="range" min="50" max="95" step="1" value="67">
          </span>
        </label>
        <label class="mm-filter-toggle">
          <span class="mm-filter-check">
            <input id="mm-relevance-taxonomy" type="checkbox" checked>
          </span>
          <span class="mm-filter-body">
            <span class="mm-filter-row">
              <span>Tree proximity</span>
              <span id="mm-relevance-distance-val">12</span>
            </span>
            <input id="mm-relevance-distance" type="range" min="0" max="14" step="1" value="12">
          </span>
        </label>
        <div class="mm-relevance-foot">
          <span id="mm-relevance-status">Filter off</span>
          <span id="mm-relevance-match-count">…</span>
        </div>
      </div>

      <div class="mm-settings-separator" aria-hidden="true"></div>

      <div class="mm-section mm-section--actions mm-actions">
        <button id="mm-fit-btn">Fit view</button>
      </div>

      <div class="mm-section mm-section--detail">
        <span class="mm-section-label">Level-of-detail</span>
        <div id="mm-detail-controls" class="mm-detail-controls"></div>
      </div>

      <div class="mm-section mm-section--visibility">
        <span class="mm-section-label">Visibility</span>
        <div class="mm-visibility-controls">
          <button id="mm-labels-toggle" type="button" aria-pressed="true">Node Labels</button>
        </div>
      </div>

      <div class="mm-section mm-section--search">
        <span class="mm-section-label">Search</span>
        <div class="mm-search-wrap">
          <input id="mm-search" type="text" placeholder="Title, tag or keyword…">
          <button id="mm-search-clear" type="button" aria-label="Clear search" hidden>&times;</button>
        </div>
      </div>

      <div class="mm-section mm-section--categories">
        <span class="mm-section-label">Categories</span>
        <div class="mm-cat-links">
          <button id="mm-all-cats">All</button>
          <button id="mm-no-cats">None</button>
        </div>
        <div id="mm-category-filters"></div>
      </div>

      <div class="mm-section mm-section--types">
        <span class="mm-section-label">Item Types</span>
        <button id="mm-type-trigger" class="mm-type-trigger" type="button" aria-haspopup="dialog" aria-expanded="false" aria-controls="mm-type-dialog">
          <span id="mm-type-summary">All item types</span>
        </button>
        <dialog id="mm-type-dialog" class="mm-type-dialog" aria-labelledby="mm-type-title">
          <div class="mm-type-panel">
            <div class="mm-type-head">
              <h2 id="mm-type-title">Item Types</h2>
              <button id="mm-type-close" class="mm-type-close" type="button" aria-label="Close item types filter">
                <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">
                  <path d="M18.3 5.71 12 12l6.3 6.29-1.41 1.41L10.59 13.41 4.29 19.7 2.88 18.29 9.17 12 2.88 5.71 4.29 4.3l6.3 6.29 6.3-6.29z"></path>
                </svg>
              </button>
            </div>
            <div class="mm-type-actions">
              <button id="mm-all-types" type="button">All</button>
              <button id="mm-no-types" type="button">None</button>
            </div>
            <div id="mm-type-filters" class="mm-type-list" role="group" aria-label="Item types"></div>
          </div>
        </dialog>
      </div>

      <div id="mm-stats">
        <span id="mm-node-count">…</span> items
        <span id="mm-search-count" hidden></span>
        <span id="mm-relevance-count" hidden></span>
      </div>

    </div>
  </div>

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

<!-- Sigma core and graph model -->
<script src="../javascripts/vendor/graphology.umd.min.js"></script>
<script src="../javascripts/vendor/sigma.min.js"></script>
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
