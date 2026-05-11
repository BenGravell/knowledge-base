/* mind-map.js - Sigma.js paper mind-map visualisation
 *
 * Loaded by mind-map.md after:
 *   1. graphology.umd.min.js (sets window.graphology)
 *   2. sigma.min.js          (sets window.Sigma)
 *   3. mind-map-data.js      (sets window.mindMapData, includes UMAP positions)
 */

'use strict';

(function () {

  /* -------------------------------------------------------------------------
   * Hierarchy-aware category colours.
   *
   * Black is reserved for uncategorized papers only. Categorized papers derive
   * their colour from the content-tree hierarchy:
   *   super-category -> distinct hue family
   *   sibling category -> slight hue/lightness variation
   *   Motion Planning sub-category -> smaller variation around its category
   * -------------------------------------------------------------------------*/
  const UNCATEGORIZED_CATEGORY = 'Uncategorized';
  const UNCATEGORIZED_CATEGORIES = new Set([UNCATEGORIZED_CATEGORY, 'Other']);

  const SUPER_CATEGORY_PALETTE = [
    { h: 213, s: 76, l: 42 },
    { h: 152, s: 70, l: 35 },
    { h:  31, s: 82, l: 43 },
    { h: 271, s: 62, l: 44 },
    { h: 334, s: 58, l: 44 },
    { h:  12, s: 72, l: 42 },
    { h: 188, s: 72, l: 36 },
  ];
  const categoryHslCache = new Map();
  const categoryColorCache = new Map();
  const subCategoryColorCache = new Map();

  /* -------------------------------------------------------------------------
   * Guard: dependencies and data must be present
   * -------------------------------------------------------------------------*/
  const graphContainer = document.getElementById('mm-graph');

  if (!graphContainer) {
    hideLoading();
    return;
  }

  if (typeof mindMapData === 'undefined') {
    graphContainer.innerHTML =
      '<p style="padding:2em;color:#ccc">No mind-map data found.<br>' +
      'Run <code>python generate_mind_map_data.py</code> from the repo root first.</p>';
    hideLoading();
    return;
  }

  if (typeof window.graphology === 'undefined' || typeof window.Sigma === 'undefined') {
    const missing = [
      typeof window.graphology === 'undefined' ? 'Graphology' : null,
      typeof window.Sigma === 'undefined' ? 'Sigma' : null,
    ].filter(Boolean).join(' and ');
    graphContainer.innerHTML =
      `<p style="padding:2em;color:#ccc">Mind-map viewer libraries failed to load: ${missing}.</p>`;
    hideLoading();
    return;
  }

  const DATA = mindMapData;
  const NODE_RADIUS_CLEARANCE_RATIO = 0.5;
  const NODE_SCREEN_RADIUS_CAP = 5;
  const NODE_SCREEN_RADIUS_MIN = 1;
  const NODE_SCREEN_RADIUS_FALLBACK = 4.5;
  const NODE_LABEL_FONT_SIZE = 11;
  const NODE_LABEL_LINE_HEIGHT = 11.5;
  const SELECTED_NODE_RADIUS_SCALE = 1.12;

  /* -------------------------------------------------------------------------
   * State
   * -------------------------------------------------------------------------*/
  let graph = null;
  let renderer = null;
  let currentThreshold = DATA.meta.threshold;
  let activeCategories = new Set();
  let currentSearch = '';
  let pinnedNode = null;
  let hoveredNode = null;
  let hoveredEdge = null;
  let focus = { active: false, nodes: new Set(), edges: new Set(), mode: null };
  let theme = readTheme();
  let nodeScreenRadius = NODE_SCREEN_RADIUS_FALLBACK;

  /* -------------------------------------------------------------------------
   * Utility
   * -------------------------------------------------------------------------*/
  function hideLoading() {
    const el = document.getElementById('mm-loading');
    if (el) el.style.display = 'none';
  }

  function nodeColor(category, subCategory) {
    if (isUncategorizedCategory(category)) return '#000000';

    if (subCategory) {
      const key = `${category}::${subCategory}`;
      if (!subCategoryColorCache.has(key)) {
        subCategoryColorCache.set(key, hslToHex(subCategoryHsl(category, subCategory)));
      }
      return subCategoryColorCache.get(key);
    }

    if (!categoryColorCache.has(category)) {
      categoryColorCache.set(category, hslToHex(categoryHsl(category)));
    }
    return categoryColorCache.get(category);
  }

  function isUncategorizedCategory(category) {
    return !category || UNCATEGORIZED_CATEGORIES.has(category);
  }

  function categoryHsl(category) {
    if (categoryHslCache.has(category)) return categoryHslCache.get(category);

    const superCategory = categorySuperCategory(category) || category;
    const base = superCategoryHsl(superCategory);
    const siblings = categoriesForSuper(superCategory, category);
    const index = Math.max(siblings.indexOf(category), 0);
    const center = (siblings.length - 1) / 2;
    const hueStep = siblings.length > 1 ? Math.min(7, 18 / (siblings.length - 1)) : 0;
    const hsl = {
      h: normalizeHue(base.h + (index - center) * hueStep),
      s: clamp(base.s + (index % 2 === 0 ? 2 : -2), 48, 86),
      l: clamp(base.l + (index - center) * 2.2, 32, 58),
    };

    categoryHslCache.set(category, hsl);
    return hsl;
  }

  function subCategoryHsl(category, subCategory) {
    const base = categoryHsl(category);
    const subCategoryOrder = (DATA.meta || {}).subCategoryOrder || {};
    const ordered = (subCategoryOrder[category] || []).filter(Boolean);
    const siblings = ordered.includes(subCategory)
      ? ordered
      : ordered.concat(subCategory).sort((a, b) => a.localeCompare(b));
    const index = Math.max(siblings.indexOf(subCategory), 0);
    const center = (siblings.length - 1) / 2;
    const hueStep = siblings.length > 1 ? Math.min(4, 14 / (siblings.length - 1)) : 0;

    return {
      h: normalizeHue(base.h + (index - center) * hueStep),
      s: clamp(base.s + (index % 2 === 0 ? 3 : -3), 45, 88),
      l: clamp(base.l + (index - center) * 1.5 + (index % 2 === 0 ? 1 : -1), 32, 60),
    };
  }

  function categorySuperCategory(category) {
    const explicit = ((DATA.meta || {}).categorySuperCategory || {})[category];
    if (explicit) return explicit;

    const node = DATA.nodes.find(n =>
      n.data.category === category && n.data.super_category
    );
    return node ? node.data.super_category : null;
  }

  function categoryOrder() {
    const configured = (DATA.meta || {}).categoryOrder || [];
    const dataCategories = new Set(DATA.nodes.map(n => n.data.category).filter(Boolean));
    const ordered = configured.filter(cat => dataCategories.has(cat));

    [...dataCategories]
      .sort((a, b) => a.localeCompare(b))
      .forEach(cat => {
        if (!ordered.includes(cat)) ordered.push(cat);
      });

    return ordered;
  }

  function superCategoryOrder() {
    const ordered = [...((DATA.meta || {}).superCategoryOrder || [])];

    categoryOrder().forEach(cat => {
      if (isUncategorizedCategory(cat)) return;
      const superCategory = categorySuperCategory(cat) || cat;
      if (superCategory && !ordered.includes(superCategory)) {
        ordered.push(superCategory);
      }
    });

    DATA.nodes.forEach(node => {
      const superCategory = node.data.super_category;
      if (superCategory && !ordered.includes(superCategory)) {
        ordered.push(superCategory);
      }
    });

    return ordered;
  }

  function superCategoryHsl(superCategory) {
    const order = superCategoryOrder();
    const index = Math.max(order.indexOf(superCategory), 0);
    const paletteIndex = index % SUPER_CATEGORY_PALETTE.length;
    const cycle = Math.floor(index / SUPER_CATEGORY_PALETTE.length);
    const base = SUPER_CATEGORY_PALETTE[paletteIndex];

    return {
      h: normalizeHue(base.h + cycle * 19),
      s: base.s,
      l: base.l,
    };
  }

  function superCategoryColor(superCategory) {
    return hslToHex(superCategoryHsl(superCategory));
  }

  function categoriesForSuper(superCategory, currentCategory) {
    const siblings = categoryOrder().filter(cat =>
      (categorySuperCategory(cat) || cat) === superCategory
    );

    if (!siblings.includes(currentCategory)) siblings.push(currentCategory);
    return siblings;
  }

  function clamp(value, min, max) {
    return Math.min(Math.max(value, min), max);
  }

  function normalizeHue(hue) {
    return ((hue % 360) + 360) % 360;
  }

  function hslToHex({ h, s, l }) {
    const hue = normalizeHue(h) / 360;
    const sat = clamp(s, 0, 100) / 100;
    const light = clamp(l, 0, 100) / 100;

    if (sat === 0) {
      const gray = Math.round(light * 255);
      return rgbToHex(gray, gray, gray);
    }

    const q = light < 0.5
      ? light * (1 + sat)
      : light + sat - light * sat;
    const p = 2 * light - q;
    const r = hueToRgb(p, q, hue + 1 / 3);
    const g = hueToRgb(p, q, hue);
    const b = hueToRgb(p, q, hue - 1 / 3);

    return rgbToHex(
      Math.round(r * 255),
      Math.round(g * 255),
      Math.round(b * 255)
    );
  }

  function hueToRgb(p, q, t) {
    let next = t;
    if (next < 0) next += 1;
    if (next > 1) next -= 1;
    if (next < 1 / 6) return p + (q - p) * 6 * next;
    if (next < 1 / 2) return q;
    if (next < 2 / 3) return p + (q - p) * (2 / 3 - next) * 6;
    return p;
  }

  function rgbToHex(r, g, b) {
    const toHex = value => value.toString(16).padStart(2, '0').toUpperCase();
    return `#${toHex(r)}${toHex(g)}${toHex(b)}`;
  }

  function readTheme() {
    const cs = getComputedStyle(document.body);
    const v = name => cs.getPropertyValue(name).trim();
    const alphaScale = parseFloat(v('--mm-edge-alpha-scale')) || 1;
    return {
      edgeColor: v('--mm-edge-color') || '#333333',
      edgeHighlighted: normalizedCssColor(v('--mm-edge-highlighted')) || '#D9A316',
      edgeAlphaScale: alphaScale,
      edgeAlphaMin: parseFloat(v('--mm-edge-alpha-min')) || 0,
      edgeAlphaMax: parseFloat(v('--mm-edge-alpha-max')) || 0.22,
      nodeMuted: normalizedCssColor(v('--mm-node-muted')) || '#8A949E',
      nodeMutedRelated: normalizedCssColor(v('--mm-node-muted-related')) || '#737D88',
      mutedLabel: normalizedCssColor(v('--mm-muted-label')) || '#4B5563',
      selectedLabel: normalizedCssColor(v('--mm-selected-label')) || '#111111',
      selectedRing: normalizedCssColor(v('--mm-selected-ring')) || '#D9A316',
    };
  }

  function normalizedCssColor(color) {
    const c = String(color || '').trim();
    return c && !c.startsWith('color-mix(') ? c : null;
  }

  function colorWithAlpha(color, alpha) {
    const c = normalizedCssColor(color) || '#333333';
    const a = Math.max(0, Math.min(alpha, 1));
    let m;

    if ((m = c.match(/^#([0-9a-f]{3})$/i))) {
      const hex = m[1].split('').map(ch => ch + ch).join('');
      return hexToRgba(hex, a);
    }
    if ((m = c.match(/^#([0-9a-f]{6})$/i))) {
      return hexToRgba(m[1], a);
    }
    if ((m = c.match(/^rgba?\(([^)]+)\)$/i))) {
      const parts = m[1].split(',').map(p => p.trim());
      if (parts.length >= 3) return `rgba(${parts[0]},${parts[1]},${parts[2]},${a})`;
    }

    return a >= 1 ? c : `rgba(51,51,51,${a})`;
  }

  function hexToRgba(hex, alpha) {
    const r = parseInt(hex.slice(0, 2), 16);
    const g = parseInt(hex.slice(2, 4), 16);
    const b = parseInt(hex.slice(4, 6), 16);
    return `rgba(${r},${g},${b},${alpha})`;
  }

  function edgeSize(weight) {
    const t = Math.max(0, Math.min((weight - 0.5) / 0.5, 1));
    return 0.22 + t * 0.95;
  }

  function currentNodeRadius() {
    return nodeScreenRadius;
  }

  /* -------------------------------------------------------------------------
   * Format node label: split "Author [et al.] YEAR" onto two lines so the
   * text fits squarer over the circular node.
   * -------------------------------------------------------------------------*/
  function formatLabel(label) {
    const m = String(label || '').match(/^(.+?)\s+(\d{4})$/);
    return m ? `${m[1]}\n${m[2]}` : String(label || '');
  }

  function filterKey(category, subCategory) {
    return subCategory ? `${category}::${subCategory}` : category;
  }

  function nodeKey(attrs) {
    return filterKey(attrs.category, attrs.sub_category);
  }

  function nodeVisible(node) {
    return activeCategories.has(nodeKey(graph.getNodeAttributes(node)));
  }

  function edgeVisible(edge) {
    const attrs = graph.getEdgeAttributes(edge);
    return attrs.weight >= currentThreshold &&
      nodeVisible(graph.source(edge)) &&
      nodeVisible(graph.target(edge));
  }

  function nodeMatchesSearch(attrs) {
    if (!currentSearch) return false;
    return attrs.title.toLowerCase().includes(currentSearch) ||
      (attrs.tags || []).some(t => t.toLowerCase().includes(currentSearch)) ||
      (attrs.summary || '').toLowerCase().includes(currentSearch);
  }

  function escHtml(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  /* -------------------------------------------------------------------------
   * Build the Graphology graph. Sigma renders directly from node/edge attrs.
   * -------------------------------------------------------------------------*/
  function buildGraph() {
    const GraphCtor = window.graphology.UndirectedGraph || window.graphology.Graph;
    const g = new GraphCtor();

    DATA.nodes.forEach(n => {
      const attrs = n.data;
      const color = nodeColor(attrs.category, attrs.sub_category);
      g.addNode(attrs.id, {
        ...attrs,
        x: n.position.x,
        y: n.position.y,
        size: currentNodeRadius(),
        color,
        baseColor: color,
        label: formatLabel(attrs.label),
        fullLabel: attrs.label,
        labelColor: '#ffffff',
        labelOutlineColor: color,
        forceLabel: false,
      });
    });

    DATA.edges.forEach(e => {
      const attrs = e.data;
      const edgeAttrs = {
        ...attrs,
        size: edgeSize(attrs.weight),
        color: colorWithAlpha(theme.edgeColor, Math.min((attrs.edgeAlpha || 0.2) * theme.edgeAlphaScale, 1)),
        type: 'line',
      };

      if (typeof g.addUndirectedEdgeWithKey === 'function') {
        g.addUndirectedEdgeWithKey(attrs.id, attrs.source, attrs.target, edgeAttrs);
      } else {
        g.addEdgeWithKey(attrs.id, attrs.source, attrs.target, edgeAttrs);
      }
    });

    return g;
  }

  /* -------------------------------------------------------------------------
   * Sigma reducers: apply filtering, dimming and highlights at render time.
   * -------------------------------------------------------------------------*/
  function nodeReducer(node, attrs) {
    if (!nodeVisible(node)) return { ...attrs, hidden: true };

    const highlighted = focus.nodes.has(node);
    const primaryFocus = highlighted && (
      node === pinnedNode ||
      node === hoveredNode ||
      focus.mode === 'edge' ||
      focus.mode === 'search'
    );
    const muted = focus.active && !primaryFocus;
    const forceLabel =
      node === pinnedNode ||
      node === hoveredNode ||
      (highlighted && focus.mode === 'edge');

    if (muted) {
      const mutedColor = highlighted ? theme.nodeMutedRelated : theme.nodeMuted;
      return {
        ...attrs,
        size: currentNodeRadius(),
        color: mutedColor,
        labelColor: theme.mutedLabel,
        labelOutlineColor: colorWithAlpha(mutedColor, 0.55),
        forceLabel: false,
        zIndex: highlighted ? 1 : 0,
      };
    }

    if (primaryFocus) {
      return {
        ...attrs,
        size: currentNodeRadius() * SELECTED_NODE_RADIUS_SCALE,
        color: attrs.baseColor,
        labelColor: theme.selectedLabel,
        labelOutlineColor: theme.selectedRing,
        ringColor: theme.selectedRing,
        highlighted: true,
        forceLabel,
        zIndex: 3,
      };
    }

    return {
      ...attrs,
      size: currentNodeRadius(),
      color: attrs.baseColor,
      labelColor: '#ffffff',
      labelOutlineColor: attrs.baseColor,
      highlighted: false,
      forceLabel: false,
      zIndex: 1,
    };
  }

  function edgeReducer(edge, attrs) {
    if (!edgeVisible(edge)) return { ...attrs, hidden: true };

    const highlighted = focus.edges.has(edge);
    const dimmed = focus.active && !highlighted;
    const baseAlpha = Math.min(
      Math.max((attrs.edgeAlpha || 0.2) * theme.edgeAlphaScale, theme.edgeAlphaMin),
      theme.edgeAlphaMax
    );

    if (dimmed) {
      return {
        ...attrs,
        color: colorWithAlpha(theme.edgeColor, 0.025),
        size: Math.max(attrs.size * 0.35, 0.18),
        zIndex: 0,
      };
    }

    if (highlighted) {
      return {
        ...attrs,
        color: theme.edgeHighlighted,
        size: Math.max(Math.min(attrs.size * 1.35, 1.65), 1.15),
        zIndex: 2,
      };
    }

    return {
      ...attrs,
      color: colorWithAlpha(theme.edgeColor, baseAlpha),
      size: attrs.size,
      zIndex: 1,
    };
  }

  function drawNodeHover(context, data) {
    const ringColor = data.ringColor || theme.selectedRing;
    const radius = Math.max(data.size + 3.5, 6);

    context.save();
    context.beginPath();
    context.arc(data.x, data.y, radius, 0, Math.PI * 2);
    context.lineWidth = Math.max(2, Math.min(3.25, data.size * 0.55));
    context.strokeStyle = ringColor;
    context.shadowColor = colorWithAlpha(ringColor, 0.32);
    context.shadowBlur = 5;
    context.stroke();
    context.restore();
  }

  function drawNodeLabel(context, data) {
    if (!data.label) return;

    const lines = String(data.label).split('\n');
    const startY = data.y - ((lines.length - 1) * NODE_LABEL_LINE_HEIGHT) / 2;

    context.save();
    context.font = `650 ${NODE_LABEL_FONT_SIZE}px "Atkinson Hyperlegible Next", "Segoe UI", sans-serif`;
    context.textAlign = 'center';
    context.textBaseline = 'middle';
    context.lineJoin = 'round';
    context.miterLimit = 2;
    context.lineWidth = 3.25;
    context.strokeStyle = data.labelOutlineColor || data.color || '#000000';
    context.fillStyle = data.labelColor || '#ffffff';

    lines.forEach((line, i) => {
      const y = startY + i * NODE_LABEL_LINE_HEIGHT;
      context.strokeText(line, data.x, y);
      context.fillText(line, data.x, y);
    });

    context.restore();
  }

  /* -------------------------------------------------------------------------
   * Focus helpers
   * -------------------------------------------------------------------------*/
  function setNeighborhoodFocus(node, mode) {
    const nodes = new Set([node]);
    const edges = new Set();

    graph.forEachNeighbor(node, neighbor => {
      if (nodeVisible(neighbor)) nodes.add(neighbor);
    });

    graph.forEachEdge(node, edge => {
      if (edgeVisible(edge)) edges.add(edge);
    });

    focus = { active: true, nodes, edges, mode };
  }

  function setEdgeFocus(edge) {
    if (!edgeVisible(edge)) {
      focus = { active: false, nodes: new Set(), edges: new Set(), mode: null };
      return;
    }
    focus = {
      active: true,
      nodes: new Set([graph.source(edge), graph.target(edge)]),
      edges: new Set([edge]),
      mode: 'edge',
    };
  }

  function applySearchFocus() {
    const nodes = new Set();

    graph.forEachNode((node, attrs) => {
      if (nodeVisible(node) && nodeMatchesSearch(attrs)) nodes.add(node);
    });

    focus = {
      active: currentSearch.length > 0,
      nodes,
      edges: new Set(),
      mode: currentSearch.length > 0 ? 'search' : null,
    };
  }

  function recomputeFocus() {
    if (pinnedNode) {
      setNeighborhoodFocus(pinnedNode, 'pinned');
    } else if (hoveredNode) {
      setNeighborhoodFocus(hoveredNode, 'hover');
    } else if (hoveredEdge) {
      setEdgeFocus(hoveredEdge);
    } else {
      applySearchFocus();
    }
  }

  function refreshView() {
    recomputeFocus();
    if (renderer) renderer.scheduleRefresh();
    updateStats();
  }

  /* -------------------------------------------------------------------------
   * Initialise Sigma
   * -------------------------------------------------------------------------*/
  function initSigma() {
    graph = buildGraph();

    try {
      renderer = new window.Sigma(graph, graphContainer, {
        minCameraRatio: 0.04,
        maxCameraRatio: 6,
        zIndex: true,
        enableEdgeEvents: true,
        hideEdgesOnMove: true,
        renderLabels: true,
        renderEdgeLabels: false,
        enableCameraRotation: false,
        labelRenderedSizeThreshold: 0,
        labelDensity: 1,
        labelGridCellSize: 100,
        labelFont: '"Atkinson Hyperlegible Next", "Segoe UI", sans-serif',
        labelSize: NODE_LABEL_FONT_SIZE,
        itemSizesReference: 'screen',
        minEdgeThickness: 0.35,
        zoomToSizeRatioFunction: ratio => Math.max(ratio, 1e-6),
        stagePadding: 30,
        nodeReducer,
        edgeReducer,
        defaultDrawNodeLabel: drawNodeLabel,
        defaultDrawNodeHover: drawNodeHover,
      });
    } catch (err) {
      const rawMessage = err && err.message ? err.message : String(err);
      const message = rawMessage.includes('blendFunc')
        ? 'WebGL is unavailable or disabled in this browser.'
        : rawMessage;
      if (window.console && console.error) console.error('Mind-map viewer failed to initialise:', err);
      graphContainer.innerHTML =
        `<p style="padding:2em;color:#ccc">Mind-map viewer failed to initialise: ${escHtml(message)}</p>`;
      hideLoading();
      return;
    }

    hideLoading();
    setupGraphEvents();
    updateStats();
    window.setTimeout(() => fitVisible(0), 0);
  }

  function setupGraphEvents() {
    renderer.on('enterNode', payload => {
      if (pinnedNode) return;
      hoveredNode = payload.node;
      hoveredEdge = null;
      showNodeTooltip(payload.node, eventPosition(payload), false);
      refreshView();
    });

    renderer.on('leaveNode', () => {
      if (pinnedNode) return;
      hoveredNode = null;
      hideTooltip();
      refreshView();
    });

    renderer.on('enterEdge', payload => {
      if (pinnedNode) return;
      hoveredEdge = payload.edge;
      hoveredNode = null;
      showEdgeTooltip(payload.edge, eventPosition(payload));
      refreshView();
    });

    renderer.on('leaveEdge', () => {
      if (pinnedNode) return;
      hoveredEdge = null;
      hideTooltip();
      refreshView();
    });

    renderer.on('clickNode', payload => {
      const node = payload.node;
      if (pinnedNode === node) {
        pinnedNode = null;
        hoveredNode = null;
        hideTooltip();
      } else {
        pinnedNode = node;
        hoveredNode = null;
        hoveredEdge = null;
        showNodeTooltip(node, eventPosition(payload), true);
      }
      refreshView();
    });

    renderer.on('clickStage', () => {
      pinnedNode = null;
      hoveredNode = null;
      hoveredEdge = null;
      hideTooltip();
      refreshView();
    });
  }

  function eventPosition(payload) {
    if (payload && payload.event) return { x: payload.event.x, y: payload.event.y };
    return { x: graphContainer.clientWidth / 2, y: graphContainer.clientHeight / 2 };
  }

  /* -------------------------------------------------------------------------
   * Tooltip
   * -------------------------------------------------------------------------*/
  const tooltip = document.getElementById('mm-tooltip');

  function showNodeTooltip(node, pos, pinned) {
    const d = graph.getNodeAttributes(node);
    const authors = (d.authors || []).join(', ') || 'Unknown';
    const tags = (d.tags || []).slice(0, 7).join(' · ');
    const url = `../papers/${d.id}/`;
    tooltip.innerHTML =
      `<div class="tt-title">${escHtml(d.title)}</div>` +
      `<a class="tt-link" href="${url}" target="_blank" rel="noopener">Open -&gt;</a>` +
      `<div class="tt-meta">${escHtml(authors)}&nbsp;&nbsp;${d.year || ''}</div>` +
      (tags ? `<div class="tt-tags">${escHtml(tags)}</div>` : '') +
      (d.summary ? `<div class="tt-summary">${escHtml(d.summary)}</div>` : '') +
      (!pinned ? `<div class="tt-hint">Click to pin</div>` : `<div class="tt-hint">Click node again to unpin</div>`);
    tooltip.classList.toggle('pinned', pinned);
    placeTooltip(pos);
  }

  function showEdgeTooltip(edge, pos) {
    const src = graph.getNodeAttribute(graph.source(edge), 'fullLabel') || '';
    const tgt = graph.getNodeAttribute(graph.target(edge), 'fullLabel') || '';
    const pct = (graph.getEdgeAttribute(edge, 'weight') * 100).toFixed(1);
    tooltip.innerHTML =
      `<div class="tt-title">Similarity: ${pct}%</div>` +
      `<div class="tt-meta">${escHtml(src)}</div>` +
      `<div class="tt-meta">&lt;-&gt;</div>` +
      `<div class="tt-meta">${escHtml(tgt)}</div>`;
    placeTooltip(pos);
  }

  function placeTooltip(pos) {
    const MARGIN = 12;
    const graphRect = graphContainer.getBoundingClientRect();

    tooltip.classList.add('visible');
    const W = tooltip.offsetWidth;
    const H = tooltip.offsetHeight;

    let x = graphRect.left + pos.x + MARGIN;
    let y = graphRect.top + pos.y + MARGIN;

    if (x + W + MARGIN > window.innerWidth) x = graphRect.left + pos.x - W - MARGIN;
    if (y + H + MARGIN > window.innerHeight) y = graphRect.top + pos.y - H - MARGIN;

    x = Math.max(MARGIN, Math.min(x, window.innerWidth - W - MARGIN));
    y = Math.max(MARGIN, Math.min(y, window.innerHeight - H - MARGIN));

    tooltip.style.left = `${x}px`;
    tooltip.style.top = `${y}px`;
  }

  function hideTooltip() {
    tooltip.classList.remove('visible', 'pinned');
  }

  /* -------------------------------------------------------------------------
   * Filters
   * -------------------------------------------------------------------------*/
  function applyThreshold(t) {
    currentThreshold = t;
    refreshView();
  }

  function applyCategoryFilter() {
    if (pinnedNode && !nodeVisible(pinnedNode)) {
      pinnedNode = null;
      hideTooltip();
    }
    refreshView();
  }

  function applySearch(query) {
    currentSearch = query.toLowerCase().trim();
    refreshView();
  }

  /* -------------------------------------------------------------------------
   * Stats
   * -------------------------------------------------------------------------*/
  function updateStats() {
    if (!graph) return;

    let vn = 0;
    let ve = 0;

    graph.forEachNode(node => {
      if (nodeVisible(node)) vn += 1;
    });
    graph.forEachEdge(edge => {
      if (edgeVisible(edge)) ve += 1;
    });

    document.getElementById('mm-node-count').textContent = vn;
    document.getElementById('mm-edge-count').textContent = ve;
  }

  /* -------------------------------------------------------------------------
   * Fit to visible graph, leaving space for the overlay panel when open.
   * -------------------------------------------------------------------------*/
  function visibleBBoxes() {
    let rawXmin = Infinity;
    let rawXmax = -Infinity;
    let rawYmin = Infinity;
    let rawYmax = -Infinity;
    let framedXmin = Infinity;
    let framedXmax = -Infinity;
    let framedYmin = Infinity;
    let framedYmax = -Infinity;

    graph.forEachNode((node, attrs) => {
      if (!nodeVisible(node)) return;

      const displayAttrs = renderer && typeof renderer.getNodeDisplayData === 'function'
        ? renderer.getNodeDisplayData(node)
        : null;
      const framedPoint = displayAttrs &&
        Number.isFinite(displayAttrs.x) &&
        Number.isFinite(displayAttrs.y)
          ? displayAttrs
          : attrs;

      rawXmin = Math.min(rawXmin, attrs.x);
      rawXmax = Math.max(rawXmax, attrs.x);
      rawYmin = Math.min(rawYmin, attrs.y);
      rawYmax = Math.max(rawYmax, attrs.y);
      framedXmin = Math.min(framedXmin, framedPoint.x);
      framedXmax = Math.max(framedXmax, framedPoint.x);
      framedYmin = Math.min(framedYmin, framedPoint.y);
      framedYmax = Math.max(framedYmax, framedPoint.y);
    });

    if (!Number.isFinite(rawXmin) || !Number.isFinite(framedXmin)) return null;

    if (rawXmin === rawXmax) {
      rawXmin -= 1;
      rawXmax += 1;
    }
    if (rawYmin === rawYmax) {
      rawYmin -= 1;
      rawYmax += 1;
    }
    if (framedXmin === framedXmax) {
      framedXmin -= 0.01;
      framedXmax += 0.01;
    }
    if (framedYmin === framedYmax) {
      framedYmin -= 0.01;
      framedYmax += 0.01;
    }

    const rawPadX = Math.max((rawXmax - rawXmin) * 0.04, 1);
    const rawPadY = Math.max((rawYmax - rawYmin) * 0.04, 1);
    const framedPadX = Math.max((framedXmax - framedXmin) * 0.04, 0.01);
    const framedPadY = Math.max((framedYmax - framedYmin) * 0.04, 0.01);

    return {
      raw: {
        x: [rawXmin - rawPadX, rawXmax + rawPadX],
        y: [rawYmin - rawPadY, rawYmax + rawPadY],
      },
      framed: {
        x: [framedXmin - framedPadX, framedXmax + framedPadX],
        y: [framedYmin - framedPadY, framedYmax + framedPadY],
      },
    };
  }

  function minimumVisibleScreenDistance(cameraState) {
    if (!renderer || !graph) return Infinity;

    const points = [];
    graph.forEachNode((node, attrs) => {
      if (!nodeVisible(node)) return;
      const p = renderer.graphToViewport(
        { x: attrs.x, y: attrs.y },
        cameraState ? { cameraState } : undefined
      );
      points.push(p);
    });

    let minDistance = Infinity;
    for (let i = 0; i < points.length; i += 1) {
      const a = points[i];
      for (let j = i + 1; j < points.length; j += 1) {
        const b = points[j];
        const dx = a.x - b.x;
        const dy = a.y - b.y;
        const d = Math.sqrt(dx * dx + dy * dy);
        if (d < minDistance) minDistance = d;
      }
    }

    return minDistance;
  }

  function calibrateNodeRadius(cameraState) {
    const minDistance = minimumVisibleScreenDistance(cameraState);
    if (!Number.isFinite(minDistance)) return;

    const target = minDistance / (2 + NODE_RADIUS_CLEARANCE_RATIO);
    const nextRadius = Math.max(
      NODE_SCREEN_RADIUS_MIN,
      Math.min(NODE_SCREEN_RADIUS_CAP, Math.floor(target * 10) / 10)
    );

    if (Math.abs(nextRadius - nodeScreenRadius) < 0.05) return;

    nodeScreenRadius = nextRadius;
    if (renderer) renderer.refresh();
  }

  function fitVisible(duration) {
    if (!renderer || !graph) return;

    renderer.resize(true);

    const bboxes = visibleBBoxes();
    if (!bboxes) return;

    const PAD = 30;
    const dims = renderer.getDimensions();
    if (!dims.width || !dims.height) return;

    const panel = document.getElementById('mm-panel');
    const panelOpen = panel && !panel.classList.contains('body-collapsed');
    const rawPanelWidth = panelOpen ? panel.offsetWidth || 0 : 0;
    const panelWidth = rawPanelWidth < dims.width * 0.72
      ? Math.min(rawPanelWidth, Math.max(0, dims.width - PAD * 2))
      : 0;
    const left = panelWidth + PAD;
    const right = dims.width - PAD;
    const stagePadding = PAD;
    const desiredX = left < right ? (left + right) / 2 : dims.width / 2;
    const desiredY = dims.height / 2;
    const bboxCenterX = (bboxes.framed.x[0] + bboxes.framed.x[1]) / 2;
    const bboxCenterY = (bboxes.framed.y[0] + bboxes.framed.y[1]) / 2;
    const baseState = { x: bboxCenterX, y: bboxCenterY, ratio: 1, angle: 0 };

    renderer.setCustomBBox(bboxes.raw);
    renderer.setSetting('stagePadding', stagePadding);

    const framedAtDesiredCenter = renderer.viewportToFramedGraph(
      { x: desiredX, y: desiredY },
      { cameraState: baseState, padding: stagePadding }
    );

    const target = {
      x: baseState.x + (bboxCenterX - framedAtDesiredCenter.x),
      y: baseState.y + (bboxCenterY - framedAtDesiredCenter.y),
      ratio: 1,
      angle: 0,
    };

    calibrateNodeRadius(target);

    if (duration === 0) renderer.getCamera().setState(target);
    else renderer.getCamera().animate(target, { duration: duration || 260 });
  }

  /* -------------------------------------------------------------------------
   * Category filter panel
   * -------------------------------------------------------------------------*/
  function makeCatItem(key, labelText, color, count, onChildChange) {
    const label = document.createElement('label');
    label.className = 'mm-cat-item';
    label.innerHTML =
      `<input type="checkbox" checked data-cat="${escHtml(key)}">` +
      `<span class="mm-cat-dot" style="background:${color}"></span>` +
      `<span class="mm-cat-name">${escHtml(labelText)}</span>` +
      `<span class="mm-cat-count">${count}</span>`;
    label.querySelector('input').addEventListener('change', e => {
      if (e.target.checked) activeCategories.add(key);
      else activeCategories.delete(key);
      if (onChildChange) onChildChange();
      applyCategoryFilter();
    });
    return label;
  }

  function makeFilterGroup(name, count, color, expanded, className) {
    const groupEl = document.createElement('div');
    groupEl.className = className;

    const header = document.createElement('div');
    header.className = 'mm-cat-group-header';

    const groupCb = document.createElement('input');
    groupCb.type = 'checkbox';
    groupCb.className = 'mm-cat-group-cb';
    groupCb.checked = true;

    const toggleEl = document.createElement('span');
    toggleEl.className = 'mm-cat-group-toggle';
    toggleEl.innerHTML =
      `<span class="mm-cat-group-arrow">${expanded ? '▾' : '▸'}</span>` +
      `<span class="mm-cat-dot" style="background:${color}"></span>` +
      `<span class="mm-cat-group-name">${escHtml(name)}</span>` +
      `<span class="mm-cat-count">${count}</span>`;

    const itemsEl = document.createElement('div');
    itemsEl.className = 'mm-cat-group-items';
    itemsEl.style.display = expanded ? '' : 'none';

    toggleEl.addEventListener('click', () => {
      const collapsed = itemsEl.style.display === 'none';
      itemsEl.style.display = collapsed ? '' : 'none';
      toggleEl.querySelector('.mm-cat-group-arrow').textContent = collapsed ? '▾' : '▸';
    });

    header.appendChild(groupCb);
    header.appendChild(toggleEl);
    groupEl.appendChild(header);
    groupEl.appendChild(itemsEl);

    return { groupEl, groupCb, itemsEl };
  }

  function syncGroupCheckbox(groupCb, itemsEl) {
    const childCbs = itemsEl.querySelectorAll('input[data-cat]');
    const checkedCount = [...childCbs].filter(cb => cb.checked).length;
    groupCb.indeterminate = checkedCount > 0 && checkedCount < childCbs.length;
    groupCb.checked = childCbs.length > 0 && checkedCount === childCbs.length;
  }

  function setLeafCheckbox(cb, checked) {
    cb.checked = checked;
    if (checked) activeCategories.add(cb.dataset.cat);
    else activeCategories.delete(cb.dataset.cat);
  }

  function buildCategoryEntry(cat, subCatOrderNav, onChildChange) {
    const dataSubCatSet = new Set(
      DATA.nodes
        .filter(n => n.data.category === cat && n.data.sub_category)
        .map(n => n.data.sub_category)
    );
    const subCatOrder = subCatOrderNav[cat] || [];
    const subCats = subCatOrder.filter(s => dataSubCatSet.has(s));
    [...dataSubCatSet].sort((a, b) => a.localeCompare(b)).forEach(s => {
      if (!subCats.includes(s)) subCats.push(s);
    });

    const totalCount = DATA.nodes.filter(n => n.data.category === cat).length;

    if (subCats.length === 0) {
      const key = filterKey(cat);
      activeCategories.add(key);
      return makeCatItem(key, cat, nodeColor(cat), totalCount, onChildChange);
    }

    const { groupEl, groupCb, itemsEl } = makeFilterGroup(
      cat,
      totalCount,
      nodeColor(cat),
      false,
      'mm-cat-group'
    );

    function syncCategoryCb() {
      syncGroupCheckbox(groupCb, itemsEl);
      if (onChildChange) onChildChange();
    }

    groupCb.addEventListener('change', () => {
      groupCb.indeterminate = false;
      itemsEl.querySelectorAll('input[data-cat]').forEach(cb => {
        setLeafCheckbox(cb, groupCb.checked);
      });
      if (onChildChange) onChildChange();
      applyCategoryFilter();
    });

    subCats.forEach(subCat => {
      const key = filterKey(cat, subCat);
      activeCategories.add(key);
      const color = nodeColor(cat, subCat);
      const count = DATA.nodes.filter(n =>
        n.data.category === cat && n.data.sub_category === subCat
      ).length;
      itemsEl.appendChild(makeCatItem(key, subCat, color, count, syncCategoryCb));
    });

    const orphanCount = DATA.nodes.filter(n =>
      n.data.category === cat && !n.data.sub_category
    ).length;
    if (orphanCount > 0) {
      const key = filterKey(cat);
      activeCategories.add(key);
      itemsEl.appendChild(makeCatItem(key, cat, nodeColor(cat), orphanCount, syncCategoryCb));
    }

    syncGroupCheckbox(groupCb, itemsEl);
    return groupEl;
  }

  function buildSuperCategoryGroup(superCategory, cats, subCatOrderNav) {
    const catSet = new Set(cats);
    const totalCount = DATA.nodes.filter(n => catSet.has(n.data.category)).length;
    const { groupEl, groupCb, itemsEl } = makeFilterGroup(
      superCategory,
      totalCount,
      superCategoryColor(superCategory),
      true,
      'mm-cat-group mm-super-group'
    );

    function syncSuperCb() {
      syncGroupCheckbox(groupCb, itemsEl);
    }

    groupCb.addEventListener('change', () => {
      groupCb.indeterminate = false;
      itemsEl.querySelectorAll('input[data-cat]').forEach(cb => {
        setLeafCheckbox(cb, groupCb.checked);
      });
      itemsEl.querySelectorAll('.mm-cat-group-cb').forEach(cb => {
        cb.checked = groupCb.checked;
        cb.indeterminate = false;
      });
      applyCategoryFilter();
    });

    cats.forEach(cat => {
      itemsEl.appendChild(buildCategoryEntry(cat, subCatOrderNav, syncSuperCb));
    });

    syncGroupCheckbox(groupCb, itemsEl);
    return groupEl;
  }

  function buildCategoryFilters() {
    const container = document.getElementById('mm-category-filters');
    const subCatOrderNav = (DATA.meta || {}).subCategoryOrder || {};
    container.innerHTML = '';

    const allCats = categoryOrder().filter(Boolean);
    const catsBySuper = new Map();
    const uncategorizedCats = [];

    allCats.forEach(cat => {
      if (isUncategorizedCategory(cat)) {
        uncategorizedCats.push(cat);
        return;
      }

      const superCategory = categorySuperCategory(cat) || cat;
      if (!catsBySuper.has(superCategory)) catsBySuper.set(superCategory, []);
      catsBySuper.get(superCategory).push(cat);
    });

    const orderedSupers = superCategoryOrder().filter(superCategory =>
      catsBySuper.has(superCategory)
    );
    [...catsBySuper.keys()].sort((a, b) => a.localeCompare(b)).forEach(superCategory => {
      if (!orderedSupers.includes(superCategory)) orderedSupers.push(superCategory);
    });

    orderedSupers.forEach(superCategory => {
      container.appendChild(
        buildSuperCategoryGroup(superCategory, catsBySuper.get(superCategory), subCatOrderNav)
      );
    });

    uncategorizedCats.forEach(cat => {
      container.appendChild(buildCategoryEntry(cat, subCatOrderNav));
    });
  }

  /* -------------------------------------------------------------------------
   * Wire up controls
   * -------------------------------------------------------------------------*/
  function setupControls() {
    const slider = document.getElementById('mm-threshold-slider');
    const label = document.getElementById('mm-threshold-val');
    slider.value = Math.round(currentThreshold * 100);
    label.textContent = currentThreshold.toFixed(2);
    slider.addEventListener('input', e => {
      const t = parseInt(e.target.value, 10) / 100;
      label.textContent = t.toFixed(2);
      applyThreshold(t);
    });

    const search = document.getElementById('mm-search');
    let debounce;
    search.addEventListener('input', e => {
      clearTimeout(debounce);
      debounce = setTimeout(() => applySearch(e.target.value), 180);
    });

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

    document.getElementById('mm-fit-btn').addEventListener('click', () => fitVisible());

    const panel = document.getElementById('mm-panel');
    const header = document.getElementById('mm-panel-header');
    const hideBtn = document.getElementById('mm-panel-hide-btn');
    header.addEventListener('click', () => {
      const collapsed = panel.classList.toggle('body-collapsed');
      hideBtn.textContent = collapsed ? 'Show Settings' : 'Hide Settings';
      header.title = collapsed ? 'Show Settings' : 'Hide Settings';
      window.setTimeout(() => fitVisible(), 280);
    });
  }

  /* -------------------------------------------------------------------------
   * Bootstrap
   * -------------------------------------------------------------------------*/
  buildCategoryFilters();
  setupControls();
  initSigma();

  const themeObserver = new MutationObserver(() => {
    theme = readTheme();
    if (renderer) renderer.refresh();
  });
  themeObserver.observe(document.documentElement, {
    attributes: true, attributeFilter: ['data-md-color-scheme'],
  });
  if (document.body) {
    themeObserver.observe(document.body, {
      attributes: true, attributeFilter: ['data-md-color-scheme'],
    });
  }

  window.addEventListener('resize', () => {
    if (renderer) window.setTimeout(() => fitVisible(0), 0);
  });

  // Expose a small debugging/control surface.
  window._mindMap = {
    graph: () => graph,
    renderer: () => renderer,
    fit: fitVisible,
    metrics: () => ({
      nodeScreenRadius,
      minimumVisibleScreenDistance: minimumVisibleScreenDistance(),
      clearanceRatio: NODE_RADIUS_CLEARANCE_RATIO,
    }),
  };

})();
