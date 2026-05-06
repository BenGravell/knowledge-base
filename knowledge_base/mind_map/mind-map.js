/* mind-map.js — Cytoscape.js paper mind-map visualisation
 *
 * Loaded by mind-map.md after:
 *   1. cytoscape.min.js  (sets window.cytoscape)
 *   2. mind-map-data.js  (sets window.mindMapData, includes UMAP positions)
 */

'use strict';

(function () {

  /* -------------------------------------------------------------------------
   * Category → colour mapping (Material Design 800-weight palette)
   * Keys must match the top-level nav section names in mkdocs.yml.
   * -------------------------------------------------------------------------*/
  const CATEGORY_COLORS = {
    'Motion Planning':               '#1565C0',
    'Motion Prediction':             '#2E7D32',
    'Control':                       '#BF360C',
    'Reinforcement Learning':        '#6A1B9A',
    'Optimization':                  '#E65100',
    'Machine Learning':              '#880E4F',
    'Safety, Testing & Verification':'#00695C',
    'Computer Graphics':             '#0277BD',
    'Software & Programming':        '#37474F',
    'Explainers':                    '#283593',
    'Just for Fun':                  '#4E342E',
    'Other':                         '#546E7A',
  };

  /* Sub-category colours for Motion Planning (one shade per 2nd-level nav section).
   * Keys must match the 2nd-level section names in mkdocs.yml. */
  const PLANNING_SUBCATEGORY_COLORS = {
    'Path Planning':                       '#0D47A1',
    'Trajectory Planning':                 '#1565C0',
    'Speed Planning':                      '#006064',
    'Interaction-aware Planning':          '#01579B',
    'Machine Learning in Motion Planning': '#4527A0',
    'Surveys & Comparative Studies':       '#546E7A',
    'Frameworks & Stack Architectures':    '#37474F',
  };

  /* -------------------------------------------------------------------------
   * Guard: data must be present
   * -------------------------------------------------------------------------*/
  if (typeof mindMapData === 'undefined') {
    document.getElementById('cy').innerHTML =
      '<p style="padding:2em;color:#ccc">No mind-map data found.<br>' +
      'Run <code>python generate_mind_map_data.py</code> from the repo root first.</p>';
    hideLoading();
    return;
  }

  const DATA = mindMapData;

  /* -------------------------------------------------------------------------
   * State
   * -------------------------------------------------------------------------*/
  let cy = null;
  let currentThreshold = DATA.meta.threshold;
  let activeCategories = new Set();
  let currentSearch = '';
  let pinnedNode = null;

  /* -------------------------------------------------------------------------
   * Utility
   * -------------------------------------------------------------------------*/
  function hideLoading() {
    const el = document.getElementById('mm-loading');
    if (el) el.style.display = 'none';
  }

  function nodeColor(category, subCategory) {
    if (subCategory) return PLANNING_SUBCATEGORY_COLORS[subCategory] || CATEGORY_COLORS[category] || CATEGORY_COLORS['Other'];
    return CATEGORY_COLORS[category] || CATEGORY_COLORS['Other'];
  }

  /* -------------------------------------------------------------------------
   * Build the Cytoscape element array respecting current filters
   * -------------------------------------------------------------------------*/
  function buildElements() {
    const visibleNodes = DATA.nodes.filter(n => {
      const key = n.data.sub_category || n.data.category;
      return activeCategories.has(key);
    });
    const visibleIds = new Set(visibleNodes.map(n => n.data.id));

    const nodesWithColor = visibleNodes.map(n => ({
      data: { ...n.data, color: nodeColor(n.data.category, n.data.sub_category) },
      position: n.position,
    }));

    const edges = DATA.edges
      .filter(e =>
        e.data.weight >= currentThreshold &&
        visibleIds.has(e.data.source) &&
        visibleIds.has(e.data.target)
      );

    return [...nodesWithColor, ...edges];
  }

  /* -------------------------------------------------------------------------
   * Cytoscape stylesheet — reads CSS variables so it responds to theme changes
   * -------------------------------------------------------------------------*/
  function buildStylesheet() {
    const cs = getComputedStyle(document.documentElement);
    const v  = name => cs.getPropertyValue(name).trim();

    return [
      {
        selector: 'node',
        style: {
          'background-color': 'data(color)',
          'label': 'data(label)',
          'font-size': 9,
          'font-family': '"Atkinson Hyperlegible Next", "Segoe UI", sans-serif',
          'color': '#ffffff',
          'text-outline-color': 'data(color)',
          'text-outline-width': 3,
          'text-wrap': 'ellipsis',
          'text-max-width': 110,
          'text-valign': 'center',
          'text-halign': 'center',
          'width': 28,
          'height': 28,
          'border-width': 1.5,
          'border-color': 'rgba(255,255,255,0.35)',
          'min-zoomed-font-size': 6,
          'transition-property': 'opacity, border-width, border-color',
          'transition-duration': '120ms',
        },
      },
      {
        selector: 'node:selected',
        style: { 'border-width': 4, 'border-color': '#FFD700' },
      },
      {
        selector: 'node.highlighted',
        style: { 'border-width': 3, 'border-color': '#FFD700', 'z-index': 10 },
      },
      {
        selector: 'node.dimmed',
        style: { 'opacity': 0.12 },
      },
      {
        selector: 'edge',
        style: {
          'width': 'mapData(weight, 0.50, 1.00, 0.4, 3.5)',
          'line-color': v('--mm-edge-color') || 'rgba(180,200,255,0.35)',
          'opacity': 1,
          'curve-style': 'bezier',
          'transition-property': 'opacity, line-color',
          'transition-duration': '120ms',
        },
      },
      {
        selector: 'edge.highlighted',
        style: {
          'line-color': v('--mm-edge-highlighted') || 'rgba(255,215,0,0.8)',
          'width': 2.5,
          'z-index': 10,
        },
      },
      {
        selector: 'edge.dimmed',
        style: { 'opacity': 0.04 },
      },
    ];
  }

  /* -------------------------------------------------------------------------
   * Initialise Cytoscape
   * -------------------------------------------------------------------------*/
  function initCy() {
    cy = cytoscape({
      container: document.getElementById('cy'),
      elements: buildElements(),
      style: buildStylesheet(),
      layout: { name: 'preset' },   // UMAP positions baked into each element
      minZoom: 0.04,
      maxZoom: 6,
      wheelSensitivity: 0.25,
    });

    hideLoading();

    // Hover: show tooltip + dim others (skip if a node is pinned)
    cy.on('mouseover', 'node', evt => {
      if (pinnedNode) return;
      showNodeTooltip(evt.target, evt.renderedPosition, false);
      dimExcept(evt.target.closedNeighborhood());
    });
    cy.on('mouseout', 'node', () => {
      if (pinnedNode) return;
      hideTooltip();
      clearDim();
    });

    // Hover on edge: show similarity tooltip (skip if a node is pinned)
    cy.on('mouseover', 'edge', evt => {
      if (pinnedNode) return;
      showEdgeTooltip(evt.target, evt.renderedPosition);
    });
    cy.on('mouseout', 'edge', () => {
      if (pinnedNode) return;
      hideTooltip();
    });

    // Click: pin node (keep detail view open); clicking same node unpins
    cy.on('tap', 'node', evt => {
      const node = evt.target;
      if (pinnedNode === node) {
        pinnedNode = null;
        hideTooltip();
        clearDim();
      } else {
        pinnedNode = node;
        showNodeTooltip(node, evt.renderedPosition, true);
        dimExcept(node.closedNeighborhood());
      }
    });

    // Click on background: clear pin + dim
    cy.on('tap', evt => {
      if (evt.target === cy) { pinnedNode = null; clearDim(); hideTooltip(); }
    });

    updateStats();
  }

  /* -------------------------------------------------------------------------
   * Tooltip
   * -------------------------------------------------------------------------*/
  const tooltip = document.getElementById('mm-tooltip');

  function showNodeTooltip(node, pos, pinned) {
    const d = node.data();
    const authors = (d.authors || []).join(', ') || 'Unknown';
    const tags = (d.tags || []).slice(0, 7).join(' · ');
    const url = `../papers/${d.id}/`;
    tooltip.innerHTML =
      `<div class="tt-title">${escHtml(d.title)}</div>` +
      `<a class="tt-link" href="${url}" target="_blank" rel="noopener">Open ↗</a>` +
      `<div class="tt-meta">${escHtml(authors)}&nbsp;&nbsp;${d.year || ''}</div>` +
      (tags ? `<div class="tt-tags">${escHtml(tags)}</div>` : '') +
      (d.summary ? `<div class="tt-summary">${escHtml(d.summary)}</div>` : '') +
      (!pinned ? `<div class="tt-hint">Click to pin</div>` : `<div class="tt-hint">Click node again to unpin</div>`);
    tooltip.classList.toggle('pinned', pinned);
    placeTooltip(pos);
  }

  function showEdgeTooltip(edge, pos) {
    const src = cy.getElementById(edge.data('source')).data('label') || '';
    const tgt = cy.getElementById(edge.data('target')).data('label') || '';
    const pct = (edge.data('weight') * 100).toFixed(1);
    tooltip.innerHTML =
      `<div class="tt-title">Similarity: ${pct}%</div>` +
      `<div class="tt-meta">${escHtml(src)}</div>` +
      `<div class="tt-meta">↔</div>` +
      `<div class="tt-meta">${escHtml(tgt)}</div>`;
    placeTooltip(pos);
  }

  function placeTooltip(pos) {
    const MARGIN = 12;
    const cy_rect = document.getElementById('cy').getBoundingClientRect();

    // Make visible first so the browser lays out the content and we can measure it.
    tooltip.classList.add('visible');
    const W = tooltip.offsetWidth;
    const H = tooltip.offsetHeight;

    let x = cy_rect.left + pos.x + MARGIN;
    let y = cy_rect.top  + pos.y + MARGIN;

    // Prefer flipping to the other side before clamping.
    if (x + W + MARGIN > window.innerWidth)  x = cy_rect.left + pos.x - W - MARGIN;
    if (y + H + MARGIN > window.innerHeight) y = cy_rect.top  + pos.y - H - MARGIN;

    // Hard clamp: never spill past any viewport edge.
    x = Math.max(MARGIN, Math.min(x, window.innerWidth  - W - MARGIN));
    y = Math.max(MARGIN, Math.min(y, window.innerHeight - H - MARGIN));

    tooltip.style.left = `${x}px`;
    tooltip.style.top  = `${y}px`;
  }

  function hideTooltip() { tooltip.classList.remove('visible', 'pinned'); }

  function escHtml(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  /* -------------------------------------------------------------------------
   * Highlight / dim helpers
   * -------------------------------------------------------------------------*/
  function dimExcept(keep) {
    cy.elements().difference(keep).addClass('dimmed').removeClass('highlighted');
    keep.addClass('highlighted').removeClass('dimmed');
  }

  function clearDim() {
    cy.elements().removeClass('highlighted dimmed');
  }

  /* -------------------------------------------------------------------------
   * Threshold slider — show/hide edges without re-layout
   * -------------------------------------------------------------------------*/
  function applyThreshold(t) {
    currentThreshold = t;
    cy.edges().forEach(e => {
      const show = e.data('weight') >= t &&
        cy.getElementById(e.data('source')).style('display') !== 'none' &&
        cy.getElementById(e.data('target')).style('display') !== 'none';
      e.style('display', show ? 'element' : 'none');
    });
    updateStats();
  }

  /* -------------------------------------------------------------------------
   * Category filter — show/hide nodes + their edges
   * -------------------------------------------------------------------------*/
  function applyCategoryFilter() {
    cy.nodes().forEach(n => {
      const key = n.data('sub_category') || n.data('category');
      n.style('display', activeCategories.has(key) ? 'element' : 'none');
    });
    cy.edges().forEach(e => {
      const srcOk = cy.getElementById(e.data('source')).style('display') !== 'none';
      const tgtOk = cy.getElementById(e.data('target')).style('display') !== 'none';
      e.style('display', srcOk && tgtOk && e.data('weight') >= currentThreshold ? 'element' : 'none');
    });
    updateStats();
  }

  /* -------------------------------------------------------------------------
   * Search — highlight matching nodes, dim everything else
   * -------------------------------------------------------------------------*/
  function applySearch(query) {
    currentSearch = query.toLowerCase().trim();
    if (!currentSearch) { clearDim(); return; }
    cy.nodes().forEach(n => {
      const d = n.data();
      const match =
        d.title.toLowerCase().includes(currentSearch) ||
        (d.tags || []).some(t => t.toLowerCase().includes(currentSearch)) ||
        (d.summary || '').toLowerCase().includes(currentSearch);
      if (match) n.removeClass('dimmed').addClass('highlighted');
      else        n.removeClass('highlighted').addClass('dimmed');
    });
    cy.edges().addClass('dimmed').removeClass('highlighted');
  }

  /* -------------------------------------------------------------------------
   * Stats
   * -------------------------------------------------------------------------*/
  function updateStats() {
    const vn = cy.nodes().filter(n => n.style('display') !== 'none').length;
    const ve = cy.edges().filter(e => e.style('display') !== 'none').length;
    document.getElementById('mm-node-count').textContent = vn;
    document.getElementById('mm-edge-count').textContent = ve;
  }

  /* -------------------------------------------------------------------------
   * Category filter panel
   * -------------------------------------------------------------------------*/
  function makeCatItem(key, color, count, onChildChange) {
    const label = document.createElement('label');
    label.className = 'mm-cat-item';
    label.innerHTML =
      `<input type="checkbox" checked data-cat="${escHtml(key)}">` +
      `<span class="mm-cat-dot" style="background:${color}"></span>` +
      `<span class="mm-cat-name">${escHtml(key)}</span>` +
      `<span class="mm-cat-count">${count}</span>`;
    label.querySelector('input').addEventListener('change', e => {
      if (e.target.checked) activeCategories.add(key);
      else                   activeCategories.delete(key);
      if (onChildChange) onChildChange();
      applyCategoryFilter();
    });
    return label;
  }

  function buildCategoryFilters() {
    const container = document.getElementById('mm-category-filters');
    const catOrderNav = DATA.meta.categoryOrder || Object.keys(CATEGORY_COLORS);
    const subCatOrderNav = DATA.meta.subCategoryOrder || {};

    const dataCatSet = new Set(DATA.nodes.map(n => n.data.category));
    const allCats = catOrderNav.filter(c => dataCatSet.has(c));
    dataCatSet.forEach(c => { if (!allCats.includes(c)) allCats.push(c); });

    allCats.forEach(cat => {
      const dataSubCatSet = new Set(
        DATA.nodes.filter(n => n.data.category === cat && n.data.sub_category)
          .map(n => n.data.sub_category)
      );
      const subCatOrder = subCatOrderNav[cat] || [];
      const subCats = subCatOrder.filter(s => dataSubCatSet.has(s));
      dataSubCatSet.forEach(s => { if (!subCats.includes(s)) subCats.push(s); });

      if (subCats.length > 0) {
        // Render as a collapsible group with nested sub-category items
        const groupEl = document.createElement('div');
        groupEl.className = 'mm-cat-group';

        const totalCount = DATA.nodes.filter(n => n.data.category === cat).length;
        const header = document.createElement('div');
        header.className = 'mm-cat-group-header';

        const groupCb = document.createElement('input');
        groupCb.type = 'checkbox';
        groupCb.className = 'mm-cat-group-cb';
        groupCb.checked = true;

        const toggleEl = document.createElement('span');
        toggleEl.className = 'mm-cat-group-toggle';
        toggleEl.innerHTML =
          `<span class="mm-cat-group-arrow">▸</span>` +
          `<span class="mm-cat-group-name">${escHtml(cat)}</span>` +
          `<span class="mm-cat-count">${totalCount}</span>`;

        header.appendChild(groupCb);
        header.appendChild(toggleEl);

        const itemsEl = document.createElement('div');
        itemsEl.className = 'mm-cat-group-items';
        itemsEl.style.display = 'none';

        toggleEl.addEventListener('click', () => {
          const collapsed = itemsEl.style.display === 'none';
          itemsEl.style.display = collapsed ? '' : 'none';
          toggleEl.querySelector('.mm-cat-group-arrow').textContent = collapsed ? '▾' : '▸';
        });

        function syncGroupCb() {
          const childCbs = itemsEl.querySelectorAll('input[type="checkbox"]');
          const checkedCount = [...childCbs].filter(cb => cb.checked).length;
          groupCb.indeterminate = checkedCount > 0 && checkedCount < childCbs.length;
          groupCb.checked = checkedCount === childCbs.length;
        }

        groupCb.addEventListener('change', () => {
          groupCb.indeterminate = false;
          itemsEl.querySelectorAll('input[type="checkbox"]').forEach(cb => {
            cb.checked = groupCb.checked;
            if (groupCb.checked) activeCategories.add(cb.dataset.cat);
            else                 activeCategories.delete(cb.dataset.cat);
          });
          applyCategoryFilter();
        });

        subCats.forEach(subCat => {
          activeCategories.add(subCat);
          const color = nodeColor(cat, subCat);
          const count = DATA.nodes.filter(n => n.data.sub_category === subCat).length;
          itemsEl.appendChild(makeCatItem(subCat, color, count, syncGroupCb));
        });

        // Fallback: papers in this category without a sub_category
        const orphanCount = DATA.nodes.filter(n => n.data.category === cat && !n.data.sub_category).length;
        if (orphanCount > 0) {
          activeCategories.add(cat);
          itemsEl.appendChild(makeCatItem(cat, nodeColor(cat), orphanCount, syncGroupCb));
        }

        groupEl.appendChild(header);
        groupEl.appendChild(itemsEl);
        container.appendChild(groupEl);
      } else {
        activeCategories.add(cat);
        const color = nodeColor(cat);
        const count = DATA.nodes.filter(n => n.data.category === cat).length;
        container.appendChild(makeCatItem(cat, color, count));
      }
    });
  }

  /* -------------------------------------------------------------------------
   * Wire up controls
   * -------------------------------------------------------------------------*/
  function setupControls() {
    // Threshold slider
    const slider = document.getElementById('mm-threshold-slider');
    const label  = document.getElementById('mm-threshold-val');
    slider.value = Math.round(currentThreshold * 100);
    label.textContent = currentThreshold.toFixed(2);
    slider.addEventListener('input', e => {
      const t = parseInt(e.target.value) / 100;
      label.textContent = t.toFixed(2);
      applyThreshold(t);
    });

    // Search
    const search = document.getElementById('mm-search');
    let debounce;
    search.addEventListener('input', e => {
      clearTimeout(debounce);
      debounce = setTimeout(() => applySearch(e.target.value), 180);
    });

    // Select all / none categories
    document.getElementById('mm-all-cats').addEventListener('click', () => {
      document.querySelectorAll('#mm-category-filters input[data-cat]').forEach(cb => {
        cb.checked = true;
        activeCategories.add(cb.dataset.cat);
      });
      document.querySelectorAll('#mm-category-filters .mm-cat-group-cb').forEach(cb => {
        cb.checked = true;
        cb.indeterminate = false;
      });
      applyCategoryFilter();
    });
    document.getElementById('mm-no-cats').addEventListener('click', () => {
      document.querySelectorAll('#mm-category-filters input[data-cat]').forEach(cb => {
        cb.checked = false;
        activeCategories.delete(cb.dataset.cat);
      });
      document.querySelectorAll('#mm-category-filters .mm-cat-group-cb').forEach(cb => {
        cb.checked = false;
        cb.indeterminate = false;
      });
      applyCategoryFilter();
    });
  }

  /* -------------------------------------------------------------------------
   * Bootstrap
   * -------------------------------------------------------------------------*/
  buildCategoryFilters();
  setupControls();
  initCy();

  // Re-apply Cytoscape stylesheet when MkDocs switches light ↔ dark
  const _themeObserver = new MutationObserver(() => {
    if (cy) cy.style(buildStylesheet());
  });
  _themeObserver.observe(document.documentElement, {
    attributes: true, attributeFilter: ['data-md-color-scheme'],
  });
  // Also observe body in case MkDocs sets the attribute there
  if (document.body) {
    _themeObserver.observe(document.body, {
      attributes: true, attributeFilter: ['data-md-color-scheme'],
    });
  }

  // Expose for debugging
  window._cy = () => cy;

})();
