---
hide:
  - toc
render_macros: true
---

# Explorer

<div id="kb-explorer" class="ct-page kb-app-page kb-app-page--bleed" data-mode="map">
  <div id="mm-panel-header" class="kb-app-header">
    <div class="kb-mode-switch" role="group" aria-label="Explorer view">
      <button type="button" class="is-active" data-explorer-mode="map" aria-pressed="true" aria-controls="mm-app">
        <span class="kb-mode-switch-icon" aria-hidden="true">{{ site_icon('lucide/map') }}</span>
        Map
      </button>
      <button type="button" data-explorer-mode="tree" aria-pressed="false" aria-controls="ct-sunburst-panel">
        <span class="kb-mode-switch-icon" aria-hidden="true">{{ site_icon('lucide/folder-tree') }}</span>
        Tree
      </button>
    </div>
--8<-- "knowledge_base/docs/templates/map-controls.html"
  </div>

  <div id="kb-explorer-workspace">
    <div id="kb-explorer-main">
--8<-- "knowledge_base/docs/templates/map.html"
--8<-- "knowledge_base/docs/templates/tree.html"
    </div>
    <div id="mm-branch-dock">
      <aside id="mm-branch-panel" class="body-collapsed" aria-label="Branch selector" inert>
        <div class="ct-browser">
          <section class="ct-chain" aria-label="Focused tree">
            <div id="ct-ancestor-chain"></div>
          </section>
          <section id="ct-selection-details" class="ct-selection-details" aria-live="polite" hidden></section>
        </div>
      </aside>
      <button id="mm-panel-hide-btn" type="button" title="Show Branch Selector" aria-label="Show Branch Selector" aria-expanded="false" aria-controls="mm-branch-panel">
        <span aria-hidden="true">{{ site_icon('lucide/panel-right-open') }}{{ site_icon('lucide/panel-right-close') }}</span>
      </button>
    </div>
  </div>
</div>

<!-- kb:app-scripts explorer -->
<!-- /kb:app-scripts -->
