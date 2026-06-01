---
hide:
  - title
  - toc
---

<h1>Knowledge Base</h1>

*Curated research you can actually navigate.*

<div class="kb-home-bento" aria-label="Knowledge Base quick start">
  <a class="kb-bento-card kb-bento-card--map" href="map/">
    <h3>
      <span class="kb-bento-title-icon" aria-hidden="true">
        {{ material_icon(config.extra.nav_icons.map) }}
      </span>
      <span>Map</span>
    </h3>
    <p>Browse in semantic similarity space.</p>
    <span class="kb-bento-visual kb-bento-visual--map" aria-hidden="true">
      <span class="kb-map-node kb-map-node--a"></span>
      <span class="kb-map-node kb-map-node--b"></span>
      <span class="kb-map-node kb-map-node--c"></span>
      <span class="kb-map-node kb-map-node--d"></span>
      <span class="kb-map-node kb-map-node--e"></span>
      <span class="kb-map-edge kb-map-edge--a"></span>
      <span class="kb-map-edge kb-map-edge--b"></span>
      <span class="kb-map-edge kb-map-edge--c"></span>
      <span class="kb-map-edge kb-map-edge--d"></span>
      <span class="kb-map-edge kb-map-edge--e"></span>
      <span class="kb-map-edge kb-map-edge--f"></span>
    </span>
  </a>

  <a class="kb-bento-card kb-bento-card--tree" href="tree/">
    <h3>
      <span class="kb-bento-title-icon" aria-hidden="true">
        {{ material_icon(config.extra.nav_icons.tree) }}
      </span>
      <span>Tree</span>
    </h3>
    <p>Walk the taxonomy.</p>
    <span class="kb-bento-visual kb-bento-visual--tree" aria-hidden="true">
      <span class="kb-tree-root"></span>
      <span class="kb-tree-branch kb-tree-branch--one"></span>
      <span class="kb-tree-branch kb-tree-branch--two"></span>
      <span class="kb-tree-branch kb-tree-branch--three"></span>
    </span>
  </a>

  <a class="kb-bento-card kb-bento-card--timeline" href="timeline/">
    <h3>
      <span class="kb-bento-title-icon" aria-hidden="true">
        {{ material_icon(config.extra.nav_icons.timeline) }}
      </span>
      <span>Timeline</span>
    </h3>
    <p>Explore chronology and trends.</p>
    <span class="kb-bento-visual kb-bento-visual--timeline" aria-hidden="true">
      {{ timeline_preview() }}
    </span>
  </a>

  <a class="kb-bento-card kb-bento-card--search" href="search/">
    <h3>
      <span class="kb-bento-title-icon" aria-hidden="true">
        {{ material_icon(config.extra.nav_icons.search) }}
      </span>
      <span>Search</span>
    </h3>
    <p>Find entries by meaning and metadata.</p>
    <span class="kb-bento-visual kb-bento-visual--search" aria-hidden="true">
      <span class="kb-search-window">
        <span class="kb-search-pill">safe motion planning</span>
        <span class="kb-search-result kb-search-result--one"></span>
        <span class="kb-search-result kb-search-result--two"></span>
        <span class="kb-search-result kb-search-result--three"></span>
      </span>
    </span>
  </a>

</div>

<div class="kb-home-expanders" aria-label="Additional Knowledge Base context">
  <details class="kb-home-expander kb-home-expander--analytics">
    <summary>
      <span class="kb-bento-title-icon" aria-hidden="true">
        {{ material_icon(config.extra.nav_icons.analytics) }}
      </span>
      <span class="kb-home-expander-summary-text">
        <span class="kb-home-expander-title">Analytics</span>
      </span>
    </summary>
    <div class="kb-home-expander-content">
      <div id="an-app" class="an-page"></div>
    </div>
  </details>

  <details class="kb-home-expander kb-home-expander--about">
    <summary>
      <span class="kb-bento-title-icon" aria-hidden="true">
        {{ material_icon(config.extra.nav_icons.about) }}
      </span>
      <span class="kb-home-expander-summary-text">
        <span class="kb-home-expander-title">About</span>
      </span>
    </summary>
    <div class="kb-home-expander-content kb-home-about">
      <h2>Why does this exist?</h2>

      <p>Paper indexes, citation databases, search engines, and literature review tools are already good at retrieval. I wanted something a little different: a place where a curated corpus could be explored through several complementary lenses.</p>

      <p>The collection is meant to be browsed, searched, compared, and revisited from different angles. Together, those views make it easier to wander, follow threads, notice relationships, and build a feel for the surrounding landscape.</p>

      <div class="kb-about-compare">
        <section class="kb-about-compare-panel kb-about-compare-panel--is">
          <h3>What This Is</h3>
          <p>A moderately sized collection of items that have passed my personal sniff test and manual triage.</p>
          <ul>
            <li>Papers, ideas, and methods I find useful, intriguing, or worth returning to.</li>
            <li>Stronger coverage in areas I know, work near, or especially admire.</li>
          </ul>
        </section>
        <div class="kb-about-compare-divider" aria-hidden="true">vs</div>
        <section class="kb-about-compare-panel kb-about-compare-panel--not">
          <h3>What This Is Not</h3>
          <p>A neutral encyclopedia, universal index, or replacement for general retrieval tools.</p>
          <ul>
            <li>Not every single paper in the universe.</li>
            <li>Not a claim that I have read every detail of every paper.</li>
            <li>Not a complete bibliography of every author or field.</li>
            <li>Not a balanced tree where every branch has equal depth or maturity.</li>
          </ul>
        </section>
      </div>

      <h2>Reach Out</h2>

      <p>If you'd like to suggest papers, discuss an idea, or share feedback, feel free to reach out on <a href="https://github.com/BenGravell">GitHub</a> or <a href="https://www.linkedin.com/in/benjamin-gravell/">LinkedIn</a>.</p>

      <h2>Credits</h2>

      <p>This site was built with the following tools:</p>

      <ul>
        <li><a href="https://squidfunk.github.io/mkdocs-material/">Material for MkDocs</a></li>
        <li><a href="https://www.mkdocs.org/">MkDocs</a></li>
        <li><a href="https://www.mathjax.org/">MathJax</a></li>
        <li><a href="https://www.brailleinstitute.org/freefont/">Atkinson Hyperlegible</a></li>
        <li><a href="https://openai.com/codex/">Codex</a></li>
        <li><a href="https://claude.com/product/claude-code">Claude Code</a></li>
      </ul>
    </div>
  </details>
</div>

<script src="javascripts/analytics-data.js"></script>
<script src="javascripts/analytics.js"></script>
