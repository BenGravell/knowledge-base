---
hide:
  - title
  - toc
render_macros: true
---

<h1>Knowledge Base</h1>

*Curated research you can actually navigate.*

<div class="kb-home-bento" aria-label="Knowledge Base quick start">
  <div class="kb-bento-card kb-bento-card--explorer">
    <h3>
      <a class="kb-bento-link" href="explorer/?mode=map">
        <span class="kb-bento-title-icon" aria-hidden="true">
          {{ site_icon(config.extra.nav_icons.explorer) }}
        </span>
        <span>Explorer</span>
      </a>
    </h3>
    <div class="kb-bento-preview" data-home-preview inert aria-hidden="true">
      <div class="kb-bento-preview-stage kb-bento-explorer-preview ct-page">
--8<-- "knowledge_base/docs/templates/tree.html"
        <div class="ct-browser">
          <section class="ct-chain">
            <div id="ct-ancestor-chain"></div>
          </section>
        </div>
      </div>
    </div>
  </div>

  <div class="kb-bento-card kb-bento-card--search">
    <h3>
      <a class="kb-bento-link" href="search/">
        <span class="kb-bento-title-icon" aria-hidden="true">
          {{ site_icon(config.extra.nav_icons.search) }}
        </span>
        <span>Search</span>
      </a>
    </h3>
    <div class="kb-bento-preview" data-home-preview inert aria-hidden="true">
      <div class="kb-bento-preview-stage">
        <div id="tag-search-app" class="tag-search-app unified-search-app semantic-search-app" data-default-mode="metadata"></div>
      </div>
    </div>
  </div>
</div>

<div class="kb-home-expanders" aria-label="Additional Knowledge Base context">
  <details class="kb-home-expander kb-home-expander--analytics">
    <summary>
      <span class="kb-bento-title-icon" aria-hidden="true">
        {{ site_icon(config.extra.nav_icons.analytics) }}
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
        {{ site_icon(config.extra.nav_icons.about) }}
      </span>
      <span class="kb-home-expander-summary-text">
        <span class="kb-home-expander-title">About</span>
      </span>
    </summary>
    <div class="kb-home-expander-content kb-home-about">
      <div class="kb-about-compare">
        <section class="kb-about-compare-panel kb-about-compare-panel--is">
          <h1>What This Is</h1>
          <p>My curated corpus of references organized for exploration across several complementary views.</p>
          <ul>
            <li>Only items that have passed my personal sniff test: papers, ideas, and methods I find useful, intriguing, or worth returning to.</li>
            <li>A way to follow threads, notice relationships, and build a feel for the surrounding landscape.</li>
            <li>Stronger coverage in areas I know, work near, or especially admire.</li>
          </ul>
        </section>
        <div class="kb-about-compare-divider" aria-hidden="true">vs</div>
        <section class="kb-about-compare-panel kb-about-compare-panel--not">
          <h1>What This Is Not</h1>
          <p>A neutral encyclopedia, universal index, or replacement for general retrieval tools.</p>
          <ul>
            <li>Not every single paper in the universe.</li>
            <li>Not a claim that I have read every detail of every paper.</li>
            <li>Not a complete bibliography of every author or field.</li>
            <li>Not a balanced tree where every branch has equal depth or maturity.</li>
          </ul>
        </section>
      </div>

      <h1>Why does this exist?</h1>

      <p>My goal is to make exploring research feel less like grasping at straws and more like (re-)discovering a world whose landmarks are slowly becoming familiar.</p>

      <h1>Why not use an existing tool?</h1>

      <p>Paper indexes, citation databases, search engines, and literature review tools are already good at retrieval. I wanted something a little different: a durable place for the special subset of references I have already triaged, cleaned up, summarized, and placed.</p>

      <p>There are other cool related tools such as <a href="https://www.connectedpapers.com/">Connected Papers</a>, <a href="https://openknowledgemaps.org/">Open Knowledge Maps</a>, <a href="https://www.researchrabbit.ai/">ResearchRabbit</a>, and <a href="https://incitefulmed.com/academic/">Inciteful</a>. They are useful for discovering literature from the outside in: start with a seed paper, query, collection, or citation graph, then expand into a much larger external corpus. Unfortunately there are some blockers for my use case:</p>

      <ul>
        <li>They are optimized for discovery sessions, not for maintaining a stable, hand-curated library with my own labels, summaries, tags, and placement decisions.</li>
        <li>Their maps are usually generated around a query, seed, or remote account state, while I wanted the same corpus to be available as a tree, map, search surface, and per-paper notes.</li>
        <li>They depend on live third-party services and external ranking logic; this site is static, inspectable, and rebuildable from local metadata.</li>
        <li>They can help find more papers, but they do not answer the quieter question: what have I already decided is worth keeping, and where does it sit relative to everything else I care about?</li>
      </ul>

      <h1>Reach Out</h1>

      <p>If you'd like to suggest papers, discuss an idea, or share feedback, feel free to reach out on <a href="https://github.com/BenGravell">GitHub</a> or <a href="https://www.linkedin.com/in/benjamin-gravell/">LinkedIn</a>.</p>

      <h1>Credits</h1>

      <p>This site was built with the following tools:</p>

      <h2>Site Framework</h2>

      <ul>
        <li><a href="https://zensical.org/">Zensical</a></li>
      </ul>

      <h2>Math Rendering</h2>

      <ul>
        <li><a href="https://www.mathjax.org/">MathJax</a></li>
      </ul>

      <h2>Fonts</h2>

      <ul>
        <li><a href="https://www.brailleinstitute.org/freefont/">Atkinson Hyperlegible Next</a></li>
        <li><a href="https://www.brailleinstitute.org/freefont/">Atkinson Hyperlegible Mono</a></li>
        <li><a href="https://fonts.google.com/specimen/Space+Grotesk">Space Grotesk</a></li>
      </ul>

      <h2>Build Assistance</h2>

      <ul>
        <li><a href="https://openai.com/codex/">Codex</a></li>
        <li><a href="https://claude.com/product/claude-code">Claude Code</a></li>
      </ul>
    </div>
  </details>
</div>

<!-- kb:app-scripts home -->
<!-- /kb:app-scripts -->
