---
hide:
  - toc
---

<div id="ct-app" class="ct-page kb-app-page">
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
      <section id="ct-selection-details" class="ct-selection-details" aria-live="polite" hidden></section>
    </section>
  </div>
</div>

<!-- kb:app-scripts tree -->
<!-- /kb:app-scripts -->
