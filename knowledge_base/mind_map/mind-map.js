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
   *   sub-category -> smaller variation around its category
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
  const NODE_DIAMETER_SCALE = 2;
  const PAPER_NODE_RADIUS_CLEARANCE_RATIO = 0.30;
  const PAPER_NODE_RADIUS_TARGET = 12 * NODE_DIAMETER_SCALE;
  const NODE_LABEL_FONT_SIZE = 11;
  const NODE_LABEL_LINE_HEIGHT_RATIO = 1.1;
  const NODE_LABEL_ZOOM_REFERENCE_RATIO = 1;
  const NODE_LABEL_ZOOM_EXPONENT = 0.22;
  const NODE_LABEL_ZOOM_SCALE_MIN = 0.68;
  const NODE_LABEL_ZOOM_SCALE_MAX = 1.55;
  const SELECTED_NODE_RADIUS_SCALE = 1;
  const EDGE_NODE_DIAMETER_RATIO = 0.30;
  const MIN_EDGE_THICKNESS = 1;
  const MAX_DIRECT_BRANCH_PAPER_EXPANSION = 40;
  const LEVEL_TRANSITION_MS = 260;
  const LEVEL_TRANSITION_MAX_SCREEN_TRAVEL = 160;
  const LEVEL_TRANSITION_DRILLDOWN_TRAVEL_RATIO = 0.58;
  const VIEWPORT_PADDING = 30;
  const PANEL_MAX_FOCUS_WIDTH_RATIO = 0.72;
  const FOCUSED_PAPER_CAMERA_RATIO = 0.32;
  const LEGACY_BRANCH_LEVEL_IDS = ['super_category', 'category', 'sub_category'];
  const HIERARCHY_LEVELS = buildHierarchyLevels();
  const HIERARCHY_LEVEL_BY_ID = new Map(HIERARCHY_LEVELS.map(level => [level.id, level]));
  const DETAIL_LEVELS = HIERARCHY_LEVELS.map(level => level.id);
  const ALWAYS_LABELED_DETAIL_LEVELS = new Set(
    HIERARCHY_LEVELS.filter(level => level.aggregate && level.pathIndex < 2).map(level => level.id)
  );
  const AGGREGATE_LEVELS = new Set(
    HIERARCHY_LEVELS.filter(level => level.aggregate).map(level => level.id)
  );

  /* -------------------------------------------------------------------------
   * State
   * -------------------------------------------------------------------------*/
  let graph = null;
  let renderer = null;
  let currentThreshold = DATA.meta.threshold;
  let currentDetailLevel = HIERARCHY_LEVELS[0].id;
  let expandedAggregateNodes = new Set();
  let activeCategories = new Set();
  let activeItemTypes = new Set();
  let showNodeLabels = true;
  let showEdges = true;
  let currentSearch = '';
  let pinnedNode = null;
  let hoveredNode = null;
  let focus = { active: false, nodes: new Set(), edges: new Set(), mode: null };
  let theme = readTheme();
  let hierarchyData = null;
  let activeLevelTransition = null;
  let focusLabelContext = null;
  let lastLevelTransitionMetrics = null;
  let cachedPaperNodeRadius = PAPER_NODE_RADIUS_TARGET;
  let visibleNodeCount = 0;
  let visibleEdgeCount = 0;
  let searchMatchCount = 0;

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

  function currentNodeRadius() {
    return cachedPaperNodeRadius;
  }

  function currentCameraRatio() {
    if (!renderer || typeof renderer.getCamera !== 'function') {
      return NODE_LABEL_ZOOM_REFERENCE_RATIO;
    }

    const camera = renderer.getCamera();
    const state = camera && typeof camera.getState === 'function'
      ? camera.getState()
      : null;
    const ratio = state && Number(state.ratio);
    return Number.isFinite(ratio) && ratio > 0
      ? ratio
      : NODE_LABEL_ZOOM_REFERENCE_RATIO;
  }

  function currentNodeLabelMetrics() {
    const zoomScale = clamp(
      Math.pow(NODE_LABEL_ZOOM_REFERENCE_RATIO / currentCameraRatio(), NODE_LABEL_ZOOM_EXPONENT),
      NODE_LABEL_ZOOM_SCALE_MIN,
      NODE_LABEL_ZOOM_SCALE_MAX
    );
    const fontSize = NODE_LABEL_FONT_SIZE * zoomScale;

    return {
      fontSize,
      lineHeight: fontSize * NODE_LABEL_LINE_HEIGHT_RATIO,
      outlineWidth: clamp(fontSize * 0.18, 1.25, 3),
    };
  }

  function hierarchyLevel(levelId) {
    return HIERARCHY_LEVEL_BY_ID.get(levelId) || {
      id: levelId,
      label: String(levelId || ''),
      shortLabel: String(levelId || ''),
      pathIndex: DETAIL_LEVELS.indexOf(levelId),
    };
  }

  function buildHierarchyLevels() {
    const configuredDepth = Number((DATA.meta || {}).maxBranchDepth);
    const dataDepth = Math.max(
      0,
      ...DATA.nodes.map(node => paperNavPath(node.data || {}).length)
    );
    const maxDepth = Math.max(3, configuredDepth || 0, dataDepth);
    const branchLevels = [];

    for (let i = 0; i < maxDepth; i += 1) {
      branchLevels.push({
        id: LEGACY_BRANCH_LEVEL_IDS[i] || `branch_${i + 1}`,
        label: `Level ${i + 1}`,
        shortLabel: String(i + 1),
        aggregate: true,
        filter: true,
        pathIndex: i,
      });
    }

    branchLevels.push({
      id: 'paper',
      label: 'Papers',
      shortLabel: 'Items',
      aggregate: false,
      filter: false,
      pathIndex: maxDepth,
    });
    return branchLevels;
  }

  function detailLevelLabel(levelId, short = false) {
    const level = hierarchyLevel(levelId);
    return short ? (level.shortLabel || level.label) : level.label;
  }

  function aggregateNodeSize(count, level) {
    const n = Math.max(Number(count) || 1, 1);
    const scale = Math.sqrt(n);
    const index = Math.max(hierarchyLevel(level).pathIndex || 0, 0);
    if (index === 0) return clamp(110 + scale * 7.5, 125, 210) * NODE_DIAMETER_SCALE;
    if (index === 1) return clamp(78 + scale * 5.2, 88, 160) * NODE_DIAMETER_SCALE;
    return clamp(56 + scale * Math.max(2.9, 4.3 - index * 0.35), 62, 130) * NODE_DIAMETER_SCALE;
  }

  function nodeDisplaySize(attrs) {
    return attrs.kind === 'aggregate'
      ? aggregateNodeSize(attrs.count, attrs.detailLevel)
      : currentNodeRadius();
  }

  function levelAlwaysShowsLabels(attrs) {
    return attrs.kind === 'aggregate' && ALWAYS_LABELED_DETAIL_LEVELS.has(attrs.detailLevel);
  }

  function edgeDisplaySize(weight, attrs) {
    const numericWeight = Number(weight);
    const t = Number.isFinite(numericWeight)
      ? Math.max(0, Math.min((numericWeight - 0.5) / 0.5, 1))
      : 0.5;
    const referenceRadius = edgeReferenceNodeRadius(attrs);
    const targetWidth = referenceRadius * 2 * EDGE_NODE_DIAMETER_RATIO;

    if (attrs && attrs.kind === 'aggregate') {
      const countBoost = Math.log1p(Number(attrs.aggregateCount) || 1) * 0.035;
      return Math.max(targetWidth * (0.88 + t * 0.18 + countBoost), MIN_EDGE_THICKNESS);
    }

    return Math.max(targetWidth * (0.9 + t * 0.2), MIN_EDGE_THICKNESS);
  }

  function edgeReferenceNodeRadius(attrs) {
    if (attrs && graph && attrs.source && attrs.target && graphHasNode(attrs.source) && graphHasNode(attrs.target)) {
      const source = graph.getNodeAttributes(attrs.source);
      const target = graph.getNodeAttributes(attrs.target);
      return (nodeDisplaySize(source) + nodeDisplaySize(target)) / 2;
    }

    if (attrs && attrs.kind === 'aggregate') {
      return aggregateNodeSize(1, attrs.detailLevel);
    }

    return currentNodeRadius();
  }

  function edgeAlpha(attrs) {
    const baseAlpha = Math.min(
      Math.max((attrs.edgeAlpha || 0.2) * theme.edgeAlphaScale, theme.edgeAlphaMin),
      theme.edgeAlphaMax
    );
    const density = visibleNodeCount > 0 ? visibleEdgeCount / visibleNodeCount : 1;
    const densityScale = clamp(Math.sqrt(2.4 / Math.max(density, 0.25)), 0.42, 1.18);
    const levelScale = attrs.kind === 'aggregate' ? 1.12 : 1;

    return Math.min(Math.max(baseAlpha * densityScale * levelScale, theme.edgeAlphaMin), theme.edgeAlphaMax);
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

  function itemTypeKey(attrs) {
    return attrs.item_type || attrs.type || 'Unspecified';
  }

  function itemTypeLabel(type) {
    return String(type || 'Unspecified');
  }

  function paperSuperCategory(attrs) {
    if (isUncategorizedCategory(attrs.category)) return UNCATEGORIZED_CATEGORY;
    return attrs.super_category ||
      categorySuperCategory(attrs.category) ||
      attrs.category ||
      UNCATEGORIZED_CATEGORY;
  }

  function paperNavPath(attrs) {
    const rawPath = Array.isArray(attrs.nav_path)
      ? attrs.nav_path
      : [paperSuperCategory(attrs), attrs.category, attrs.sub_category].filter(Boolean);
    const path = rawPath.map(part => String(part || '').trim()).filter(Boolean);
    if (path.length) return path;
    return [UNCATEGORIZED_CATEGORY];
  }

  function paddedPaperNavPath(attrs) {
    const path = paperNavPath(attrs);
    const branchDepth = AGGREGATE_LEVELS.size;
    const fallback = path[path.length - 1] || UNCATEGORIZED_CATEGORY;

    while (path.length < branchDepth) {
      path.push(fallback);
    }

    return path.slice(0, branchDepth);
  }

  function branchColorForPath(path, index) {
    const superCategory = path[0] || UNCATEGORIZED_CATEGORY;
    const category = path[1] || superCategory;
    const label = path[index] || category;

    if (isUncategorizedCategory(category)) return '#000000';
    if (index === 0) return superCategoryColor(superCategory);
    if (index === 1) return nodeColor(category);
    return nodeColor(category, label);
  }

  function groupId(level, parts) {
    return `agg:${level}:${parts.map(part => String(part || UNCATEGORIZED_CATEGORY)).join('::')}`;
  }

  function paperSearchText(attrs) {
    return [
      attrs.title,
      attrs.label,
      attrs.category,
      attrs.sub_category,
      attrs.super_category,
      itemTypeKey(attrs),
      ...(attrs.tags || []),
      attrs.summary,
    ].filter(Boolean).join(' ').toLowerCase();
  }

  function aggregateLabel(label, count) {
    return `${label}\n${count}`;
  }

  function createHierarchyGroup({
    level,
    label,
    superCategory,
    category,
    subCategory,
    path = [],
    pathIndex = 0,
    color,
    parent = null,
    isCategoryLeaf = false,
  }) {
    const pathParts = path.length
      ? path
      : [superCategory, category, subCategory || (isCategoryLeaf ? category : null)].filter(Boolean);
    return {
      key: `${level}:${pathParts.join('::')}`,
      level,
      label,
      superCategory,
      category,
      subCategory,
      path,
      pathIndex,
      color,
      parent,
      isCategoryLeaf,
      children: [],
      childMap: new Map(),
      leafIds: [],
      filterKeys: new Set(),
      itemTypes: new Set(),
      searchParts: new Set([label, superCategory, category, subCategory].filter(Boolean)),
      previewTitles: [],
      x: 0,
      y: 0,
    };
  }

  function ensureHierarchyChild(parent, key, spec) {
    const map = parent ? parent.childMap : spec.rootMap;
    if (map.has(key)) return map.get(key);

    const group = createHierarchyGroup({ ...spec, parent });
    map.set(key, group);
    if (parent) parent.children.push(group);
    else spec.roots.push(group);
    return group;
  }

  function accumulateHierarchyGroup(group, paperNode) {
    const attrs = paperNode.data;
    group.leafIds.push(attrs.id);
    group.filterKeys.add(nodeKey(attrs));
    group.itemTypes.add(itemTypeKey(attrs));
    group.searchParts.add(paperSearchText(attrs));
    group.x += Number(paperNode.position.x) || 0;
    group.y += Number(paperNode.position.y) || 0;
    if (group.previewTitles.length < 4 && attrs.title) group.previewTitles.push(attrs.title);
  }

  function hierarchySortKey(group) {
    const pathOrder = ((DATA.meta || {}).navPathOrder || [])
      .map(path => Array.isArray(path) ? path.join('::') : '')
      .filter(Boolean);
    const pathKey = (group.path || []).join('::');
    const pathIndex = pathOrder.indexOf(pathKey);
    if (pathIndex >= 0) return [pathIndex, group.label];

    if ((group.pathIndex || 0) === 0) {
      const order = superCategoryOrder();
      const index = order.indexOf(group.label);
      return [index < 0 ? Number.MAX_SAFE_INTEGER : index, group.label];
    }

    if ((group.pathIndex || 0) === 1) {
      const order = categoryOrder();
      const index = order.indexOf(group.category);
      return [index < 0 ? Number.MAX_SAFE_INTEGER : index, group.label];
    }

    const subOrder = ((DATA.meta || {}).subCategoryOrder || {})[group.category] || [];
    const index = group.subCategory ? subOrder.indexOf(group.subCategory) : -1;
    return [index < 0 ? Number.MAX_SAFE_INTEGER : index, group.label];
  }

  function sortHierarchyGroups(groups) {
    groups.sort((a, b) => {
      const ak = hierarchySortKey(a);
      const bk = hierarchySortKey(b);
      return ak[0] - bk[0] || String(ak[1]).localeCompare(String(bk[1]));
    });

    groups.forEach(group => sortHierarchyGroups(group.children));
  }

  function aggregateNodeId(detailLevel, group) {
    return groupId(detailLevel, [group.key]);
  }

  function groupAncestorIds(group) {
    const ancestors = {};
    let cursor = group.parent;

    while (cursor) {
      ancestors[cursor.level] = aggregateNodeId(cursor.level, cursor);
      cursor = cursor.parent;
    }

    return ancestors;
  }

  function buildAggregateNode(group, detailLevel) {
    const count = group.leafIds.length || 1;
    const ancestorIds = groupAncestorIds(group);
    const parentId = group.parent
      ? aggregateNodeId(group.parent.level, group.parent)
      : null;

    return {
      data: {
        id: aggregateNodeId(detailLevel, group),
        kind: 'aggregate',
        detailLevel,
        hierarchyLevel: group.level,
        parentId,
        ancestorIds,
        label: aggregateLabel(group.label, count),
        fullLabel: group.label,
        title: group.label,
        authors: [],
        year: null,
        super_category: group.superCategory,
        category: group.category,
        sub_category: group.subCategory,
        nav_path: group.path,
        color: group.color,
        count,
        leafIds: group.leafIds,
        filterKeys: [...group.filterKeys],
        itemTypes: [...group.itemTypes],
        previewTitles: group.previewTitles,
        tags: [],
        summary: `${count} ${count === 1 ? 'paper' : 'papers'}`,
        searchText: [...group.searchParts].join(' ').toLowerCase(),
      },
      position: {
        x: Math.round((group.x / count) * 10) / 10,
        y: Math.round((group.y / count) * 10) / 10,
      },
    };
  }

  function edgeAccumulatorToData(edgeMap, idPrefix, edgeAlpha = 0.24) {
    return [...edgeMap.values()]
      .sort((a, b) => `${a.source}${a.target}`.localeCompare(`${b.source}${b.target}`))
      .map((edge, index) => {
        const meanWeight = edge.count ? edge.weightSum / edge.count : edge.maxWeight;
        return {
          data: {
            id: `${idPrefix}:${index}`,
            kind: 'aggregate',
            detailLevel: 'mixed',
            source: edge.source,
            target: edge.target,
            weight: Math.round(edge.maxWeight * 10000) / 10000,
            meanWeight: Math.round(meanWeight * 10000) / 10000,
            aggregateCount: edge.count,
            undirected: true,
            edgeAlpha,
          },
        };
      });
  }

  function buildMixedAggregateEdges(paperAncestors) {
    const edgeMap = new Map();

    function displayNodeForPaper(paperId, level) {
      return level === 'paper'
        ? paperId
        : paperAncestors[paperId] && paperAncestors[paperId][level];
    }

    DATA.edges.forEach(edge => {
      const attrs = edge.data;
      const weight = Number(attrs.weight) || 0;

      DETAIL_LEVELS.forEach(sourceLevel => {
        DETAIL_LEVELS.forEach(targetLevel => {
          if (sourceLevel === 'paper' && targetLevel === 'paper') return;

          const rawSource = displayNodeForPaper(attrs.source, sourceLevel);
          const rawTarget = displayNodeForPaper(attrs.target, targetLevel);
          if (!rawSource || !rawTarget || rawSource === rawTarget) return;

          const source = rawSource < rawTarget ? rawSource : rawTarget;
          const target = rawSource < rawTarget ? rawTarget : rawSource;
          const key = `${source}||${target}`;
          let aggregate = edgeMap.get(key);

          if (!aggregate) {
            aggregate = {
              source,
              target,
              maxWeight: weight,
              weightSum: 0,
              count: 0,
            };
            edgeMap.set(key, aggregate);
          }

          aggregate.maxWeight = Math.max(aggregate.maxWeight, weight);
          aggregate.weightSum += weight;
          aggregate.count += 1;
        });
      });
    });

    return edgeAccumulatorToData(edgeMap, 'mixed-agg-edge');
  }

  function buildHierarchyData() {
    if (hierarchyData) return hierarchyData;

    const roots = [];
    const rootMap = new Map();
    const branchLevels = HIERARCHY_LEVELS.filter(level => level.aggregate);
    const groupsByLevel = Object.fromEntries(branchLevels.map(level => [level.id, []]));
    const paperAncestors = {};
    const aggregateNodes = [];
    const aggregateEdges = [];

    DATA.nodes.forEach(paperNode => {
      const attrs = paperNode.data;
      const path = paddedPaperNavPath(attrs);
      const superCategory = path[0] || paperSuperCategory(attrs);
      const category = path[1] || attrs.category || superCategory || UNCATEGORIZED_CATEGORY;
      const subCategory = path[2] || attrs.sub_category || null;
      let parent = null;
      const ancestors = {};

      branchLevels.forEach((level, index) => {
        const label = path[index] || path[path.length - 1] || UNCATEGORIZED_CATEGORY;
        const pathPrefix = path.slice(0, index + 1);
        const group = ensureHierarchyChild(parent, label, {
          rootMap,
          roots,
          level: level.id,
          label,
          superCategory,
          category,
          subCategory: index >= 2 ? label : subCategory,
          path: pathPrefix,
          pathIndex: index,
          color: branchColorForPath(path, index),
          isCategoryLeaf: index >= paperNavPath(attrs).length,
        });
        accumulateHierarchyGroup(group, paperNode);
        ancestors[level.id] = aggregateNodeId(level.id, group);
        parent = group;
      });

      paperAncestors[attrs.id] = ancestors;
    });

    sortHierarchyGroups(roots);

    function collect(group) {
      if (groupsByLevel[group.level]) groupsByLevel[group.level].push(group);
      group.children.forEach(collect);
    }
    roots.forEach(collect);

    HIERARCHY_LEVELS
      .filter(level => level.aggregate)
      .forEach(level => {
        const groups = groupsByLevel[level.id] || [];
        groups.forEach(group => aggregateNodes.push(buildAggregateNode(group, level.id)));
      });

    aggregateEdges.push(...buildMixedAggregateEdges(paperAncestors));

    hierarchyData = {
      roots,
      levels: HIERARCHY_LEVELS,
      groupsByLevel,
      paperAncestors,
      nodes: aggregateNodes,
      edges: aggregateEdges,
    };
    return hierarchyData;
  }

  function nodeAllowedByFilters(attrs) {
    const categoryAllowed = attrs.kind === 'aggregate'
      ? (attrs.filterKeys || []).some(key => activeCategories.has(key))
      : activeCategories.has(nodeKey(attrs));
    if (!categoryAllowed) return false;

    if (attrs.kind === 'aggregate') {
      return (attrs.itemTypes || []).some(type => activeItemTypes.has(type));
    }

    return activeItemTypes.has(itemTypeKey(attrs));
  }

  function nodeVisibleAt(node, level) {
    const attrs = graph.getNodeAttributes(node);
    if (!nodeAllowedByFilters(attrs)) return false;

    const baseIndex = DETAIL_LEVELS.indexOf(level);
    const nodeIndex = DETAIL_LEVELS.indexOf(attrs.detailLevel);
    if (baseIndex < 0 || nodeIndex < baseIndex) return false;

    for (let i = baseIndex; i < nodeIndex; i += 1) {
      const ancestorLevel = DETAIL_LEVELS[i];
      const ancestorId = attrs.detailLevel === ancestorLevel
        ? node
        : attrs.ancestorIds && attrs.ancestorIds[ancestorLevel];
      if (!ancestorId || !expandedAggregateNodes.has(ancestorId)) return false;
    }

    return !(attrs.kind === 'aggregate' && expandedAggregateNodes.has(node));
  }

  function nodeVisible(node) {
    return nodeVisibleAt(node, currentDetailLevel);
  }

  function edgeVisible(edge) {
    if (!showEdges) return false;

    const attrs = graph.getEdgeAttributes(edge);
    return attrs.weight >= currentThreshold &&
      nodeVisible(graph.source(edge)) &&
      nodeVisible(graph.target(edge));
  }

  function nodeMatchesSearch(attrs) {
    if (!currentSearch) return false;
    if (attrs.searchText) return attrs.searchText.includes(currentSearch);
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
    const g = window.graphology.UndirectedGraph ?
      new window.graphology.UndirectedGraph() :
      new window.graphology.Graph({ type: 'undirected' });
    const hierarchy = buildHierarchyData();

    DATA.nodes.concat(hierarchy.nodes).forEach(n => {
      const attrs = n.data;
      const kind = attrs.kind || 'paper';
      const detailLevel = attrs.detailLevel || 'paper';
      const color = attrs.color || nodeColor(attrs.category, attrs.sub_category);
      const x = n.position.x;
      const y = n.position.y;
      const ancestorIds = attrs.ancestorIds || hierarchy.paperAncestors[attrs.id] || {};
      g.addNode(attrs.id, {
        ...attrs,
        kind,
        detailLevel,
        item_type: itemTypeKey(attrs),
        parentId: attrs.parentId || ancestorIds[previousDetailLevel(detailLevel)] || null,
        ancestorIds,
        filterKeys: attrs.filterKeys || [nodeKey(attrs)],
        searchText: attrs.searchText || paperSearchText(attrs),
        x,
        y,
        homeX: x,
        homeY: y,
        size: nodeDisplaySize({ ...attrs, kind, detailLevel }),
        color,
        baseColor: color,
        label: formatLabel(attrs.label),
        fullLabel: attrs.fullLabel || attrs.label,
        count: attrs.count || 1,
        labelColor: '#ffffff',
        labelOutlineColor: color,
        forceLabel: levelAlwaysShowsLabels({ ...attrs, kind, detailLevel }),
      });
    });

    DATA.edges.concat(hierarchy.edges).forEach(e => {
      const attrs = e.data;
      const kind = attrs.kind || 'paper';
      const detailLevel = attrs.detailLevel || 'paper';
      const edgeAttrs = {
        ...attrs,
        kind,
        detailLevel,
        size: edgeDisplaySize(attrs.weight, { ...attrs, kind, detailLevel }),
        color: colorWithAlpha(theme.edgeColor, edgeAlpha({ ...attrs, kind, detailLevel })),
        type: 'line',
      };

      if (typeof g.addUndirectedEdgeWithKey !== 'function') {
        throw new Error('Mind map graph must support undirected edges.');
      }
      g.addUndirectedEdgeWithKey(attrs.id, attrs.source, attrs.target, edgeAttrs);
    });

    return g;
  }

  /* -------------------------------------------------------------------------
   * Sigma reducers: apply filtering, dimming and highlights at render time.
   * -------------------------------------------------------------------------*/
  function nodeReducer(node, attrs) {
    if (!nodeVisible(node)) return { ...attrs, hidden: true };

    const size = nodeDisplaySize(attrs);
    const baseZIndex = detailLevelZIndex(attrs.detailLevel);
    const highlighted = focus.nodes.has(node);
    const primaryFocus = highlighted && (
      node === pinnedNode ||
      node === hoveredNode ||
      focus.mode === 'search'
    );
    const muted = focus.active && !primaryFocus;
    const focusLabel = node === pinnedNode ||
      node === hoveredNode ||
      (focus.mode === 'search' && highlighted);
    const forceLabel = (showNodeLabels && levelAlwaysShowsLabels(attrs)) ||
      focusLabel;
    const label = (showNodeLabels || focusLabel) ? attrs.label : '';

    if (muted) {
      const mutedColor = highlighted ? theme.nodeMutedRelated : theme.nodeMuted;
      return {
        ...attrs,
        label,
        size,
        color: mutedColor,
        labelColor: theme.mutedLabel,
        labelOutlineColor: colorWithAlpha(mutedColor, 0.55),
        forceLabel,
        zIndex: baseZIndex + (highlighted ? 20 : 0),
      };
    }

    if (primaryFocus) {
      return {
        ...attrs,
        label,
        size: size * SELECTED_NODE_RADIUS_SCALE,
        color: attrs.baseColor,
        labelColor: theme.selectedLabel,
        labelOutlineColor: theme.selectedRing,
        ringColor: theme.selectedRing,
        highlighted: true,
        forceLabel,
        zIndex: baseZIndex + 40,
      };
    }

    return {
      ...attrs,
      label,
      size,
      color: attrs.baseColor,
      labelColor: '#ffffff',
      labelOutlineColor: attrs.baseColor,
      highlighted: false,
      forceLabel,
      zIndex: baseZIndex,
    };
  }

  function edgeReducer(edge, attrs) {
    if (!edgeVisible(edge)) return { ...attrs, hidden: true };

    const highlighted = focus.edges.has(edge);
    const dimmed = focus.active && !highlighted;
    const baseAlpha = edgeAlpha(attrs);
    const size = edgeDisplaySize(attrs.weight, attrs);

    if (dimmed) {
      return {
        ...attrs,
        color: colorWithAlpha(theme.edgeColor, 0.025),
        size: Math.max(size * 0.35, MIN_EDGE_THICKNESS),
        zIndex: 0,
      };
    }

    if (highlighted) {
      return {
        ...attrs,
        color: theme.edgeHighlighted,
        size: Math.max(size * 1.25, MIN_EDGE_THICKNESS),
        zIndex: 2,
      };
    }

    return {
      ...attrs,
      color: colorWithAlpha(theme.edgeColor, baseAlpha),
      size: Math.max(size, MIN_EDGE_THICKNESS),
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
    const { fontSize, lineHeight, outlineWidth } = currentNodeLabelMetrics();
    const startY = data.y - ((lines.length - 1) * lineHeight) / 2;

    context.save();
    context.font = `650 ${fontSize}px "Atkinson Hyperlegible Next", "Segoe UI", sans-serif`;
    context.textAlign = 'center';
    context.textBaseline = 'middle';
    context.lineJoin = 'round';
    context.miterLimit = 2;
    context.lineWidth = outlineWidth;
    context.strokeStyle = data.labelOutlineColor || data.color || '#000000';
    context.fillStyle = data.labelColor || '#ffffff';

    lines.forEach((line, i) => {
      const y = startY + i * lineHeight;
      context.strokeText(line, data.x, y);
      context.fillText(line, data.x, y);
    });

    context.restore();
  }

  function setupFocusLabelOverlay() {
    if (!renderer || typeof renderer.createCanvasContext !== 'function') return;

    try {
      renderer.createCanvasContext('focusLabels', {
        afterLayer: 'hoverNodes',
        style: { pointerEvents: 'none' },
      });
      renderer.resize(true);

      const canvases = typeof renderer.getCanvases === 'function'
        ? renderer.getCanvases()
        : {};
      focusLabelContext = canvases.focusLabels
        ? canvases.focusLabels.getContext('2d')
        : null;
    } catch (err) {
      focusLabelContext = null;
      if (window.console && console.warn) console.warn('Could not create focus label overlay:', err);
    }

    if (focusLabelContext) {
      renderer.on('afterRender', drawFocusLabelOverlay);
    }
  }

  function clearFocusLabelOverlay() {
    if (!focusLabelContext || !renderer) return;

    const dims = renderer.getDimensions();
    focusLabelContext.clearRect(0, 0, dims.width, dims.height);
  }

  function labelOverlayNodes() {
    const nodes = [];

    graph.forEachNode((node, attrs) => {
      if (!nodeVisible(node)) return;
      const display = renderer && typeof renderer.getNodeDisplayData === 'function'
        ? renderer.getNodeDisplayData(node)
        : null;
      if (!display || display.hidden || !display.label) return;
      nodes.push(node);
    });

    return nodes;
  }

  function drawFocusLabelOverlay() {
    if (!focusLabelContext || !renderer || !graph) return;

    clearFocusLabelOverlay();
    labelOverlayNodes().forEach(node => {
      const attrs = graph.getNodeAttributes(node);
      const display = renderer.getNodeDisplayData(node);
      if (!display || display.hidden) return;

      const point = renderer.graphToViewport({ x: attrs.x, y: attrs.y });
      const size = typeof renderer.scaleSize === 'function'
        ? renderer.scaleSize(display.size)
        : display.size;

      drawNodeLabel(focusLabelContext, {
        ...display,
        x: point.x,
        y: point.y,
        size,
      });
    });
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

  function applySearchFocus() {
    const nodes = new Set();

    graph.forEachNode((node, attrs) => {
      if (nodeVisible(node) && nodeMatchesSearch(attrs)) nodes.add(node);
    });

    searchMatchCount = nodes.size;
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
    } else {
      applySearchFocus();
    }
  }

  function countSearchMatches() {
    if (!graph || !currentSearch) return 0;

    let matches = 0;
    graph.forEachNode((node, attrs) => {
      if (nodeVisible(node) && nodeMatchesSearch(attrs)) matches += 1;
    });
    return matches;
  }

  function refreshView() {
    cachedPaperNodeRadius = paperNodeRadiusForCurrentView();
    recomputeVisibleStats();
    searchMatchCount = countSearchMatches();
    recomputeFocus();
    if (renderer) renderer.scheduleRefresh();
    updateStats();
  }

  function nextDetailLevel(level) {
    const index = DETAIL_LEVELS.indexOf(level);
    return index >= 0 && index < DETAIL_LEVELS.length - 1
      ? DETAIL_LEVELS[index + 1]
      : null;
  }

  function previousDetailLevel(level) {
    const index = DETAIL_LEVELS.indexOf(level);
    return index > 0 ? DETAIL_LEVELS[index - 1] : null;
  }

  function detailLevelZIndex(level) {
    const index = DETAIL_LEVELS.indexOf(level);
    return index >= 0 ? (index + 1) * 10 : 0;
  }

  function detailLevelDirection(fromLevel, toLevel) {
    return DETAIL_LEVELS.indexOf(toLevel) - DETAIL_LEVELS.indexOf(fromLevel);
  }

  function graphHasNode(node) {
    return graph && typeof graph.hasNode === 'function' && graph.hasNode(node);
  }

  function nodePoint(node) {
    const attrs = graph.getNodeAttributes(node);
    return {
      x: Number.isFinite(attrs.x) ? attrs.x : attrs.homeX,
      y: Number.isFinite(attrs.y) ? attrs.y : attrs.homeY,
    };
  }

  function homePoint(attrs) {
    return {
      x: Number.isFinite(attrs.homeX) ? attrs.homeX : attrs.x,
      y: Number.isFinite(attrs.homeY) ? attrs.homeY : attrs.y,
    };
  }

  function transitionCameraState() {
    if (!renderer || typeof renderer.getCamera !== 'function') return null;
    const camera = renderer.getCamera();
    return camera && typeof camera.getState === 'function'
      ? camera.getState()
      : null;
  }

  function screenDistance(a, b, cameraState = null) {
    if (!renderer) return Infinity;
    const options = cameraState ? { cameraState } : undefined;
    const av = renderer.graphToViewport(a, options);
    const bv = renderer.graphToViewport(b, options);
    const dx = av.x - bv.x;
    const dy = av.y - bv.y;
    return Math.sqrt(dx * dx + dy * dy);
  }

  function limitTransitionOriginTravel(from, to, cameraState = null) {
    if (!renderer) return from;

    const options = cameraState ? { cameraState } : undefined;
    const fromView = renderer.graphToViewport(from, options);
    const toView = renderer.graphToViewport(to, options);
    const dx = fromView.x - toView.x;
    const dy = fromView.y - toView.y;
    const distance = Math.sqrt(dx * dx + dy * dy);
    const maxTravel = Math.min(
      LEVEL_TRANSITION_MAX_SCREEN_TRAVEL,
      Math.max(24, distance * LEVEL_TRANSITION_DRILLDOWN_TRAVEL_RATIO)
    );

    if (!Number.isFinite(distance) || distance <= maxTravel || !distance) return from;

    const scale = maxTravel / distance;
    const boundedView = {
      x: toView.x + dx * scale,
      y: toView.y + dy * scale,
    };

    if (typeof renderer.viewportToGraph === 'function') {
      return renderer.viewportToGraph(boundedView, options);
    }

    return {
      x: to.x + (from.x - to.x) * scale,
      y: to.y + (from.y - to.y) * scale,
    };
  }

  function finishLevelTransition() {
    if (!activeLevelTransition) return;
    window.cancelAnimationFrame(activeLevelTransition.raf);
    activeLevelTransition.nodes.forEach(item => {
      if (!graphHasNode(item.node)) return;
      graph.setNodeAttribute(item.node, 'x', item.to.x);
      graph.setNodeAttribute(item.node, 'y', item.to.y);
    });
    activeLevelTransition = null;
  }

  function transitionOriginForDrillDown(attrs, previousLevel, to, cameraState) {
    const parentLevel = previousDetailLevel(attrs.detailLevel);
    const ancestorId = attrs.ancestorIds && (
      attrs.ancestorIds[parentLevel] ||
      attrs.ancestorIds[previousLevel]
    );
    if (ancestorId && graphHasNode(ancestorId)) {
      return limitTransitionOriginTravel(nodePoint(ancestorId), to, cameraState);
    }
    return homePoint(attrs);
  }

  function transitionOriginForRollUp(targetNode, targetLevel, previousLevel) {
    const points = [];

    graph.forEachNode((node, attrs) => {
      if (attrs.detailLevel !== previousLevel || !nodeAllowedByFilters(attrs)) return;
      if (!attrs.ancestorIds || attrs.ancestorIds[targetLevel] !== targetNode) return;
      points.push(nodePoint(node));
    });

    if (!points.length) return null;

    return {
      x: points.reduce((sum, p) => sum + p.x, 0) / points.length,
      y: points.reduce((sum, p) => sum + p.y, 0) / points.length,
    };
  }

  function prepareLevelTransition(previousLevel, nextLevel) {
    const direction = detailLevelDirection(previousLevel, nextLevel);
    const nodes = [];
    const cameraState = transitionCameraState();
    let maxScreenTravel = 0;

    graph.forEachNode((node, attrs) => {
      if (attrs.detailLevel !== nextLevel || !nodeAllowedByFilters(attrs)) return;

      const to = homePoint(attrs);
      let from = null;

      if (direction > 0) {
        from = transitionOriginForDrillDown(attrs, previousLevel, to, cameraState);
      } else if (direction < 0) {
        from = transitionOriginForRollUp(node, nextLevel, previousLevel) || homePoint(attrs);
      }

      if (!from) return;
      maxScreenTravel = Math.max(maxScreenTravel, screenDistance(from, to, cameraState));
      nodes.push({ node, from, to });
    });

    lastLevelTransitionMetrics = {
      fromLevel: previousLevel,
      toLevel: nextLevel,
      direction,
      nodeCount: nodes.length,
      maxScreenTravel,
      maxAllowedScreenTravel: direction > 0 ? LEVEL_TRANSITION_MAX_SCREEN_TRAVEL : null,
    };

    return nodes;
  }

  function startLevelTransition(nodes) {
    if (!nodes.length) return;

    nodes.forEach(item => {
      graph.setNodeAttribute(item.node, 'x', item.from.x);
      graph.setNodeAttribute(item.node, 'y', item.from.y);
    });

    const start = window.performance.now();
    const duration = LEVEL_TRANSITION_MS;

    function ease(t) {
      return 1 - Math.pow(1 - t, 3);
    }

    function step(now) {
      const t = Math.min((now - start) / duration, 1);
      const k = ease(t);

      nodes.forEach(item => {
        graph.setNodeAttribute(item.node, 'x', item.from.x + (item.to.x - item.from.x) * k);
        graph.setNodeAttribute(item.node, 'y', item.from.y + (item.to.y - item.from.y) * k);
      });

      if (renderer) renderer.scheduleRefresh();

      if (t < 1) {
        activeLevelTransition.raf = window.requestAnimationFrame(step);
      } else {
        activeLevelTransition = null;
      }
    }

    activeLevelTransition = {
      nodes,
      raf: window.requestAnimationFrame(step),
    };
  }

  function prepareBranchExpansionTransition(parentNode, childLevel) {
    const parentPoint = nodePoint(parentNode);
    const cameraState = transitionCameraState();
    const nodes = [];

    graph.forEachNode((node, attrs) => {
      if (attrs.detailLevel !== childLevel || attrs.parentId !== parentNode) return;
      if (!nodeAllowedByFilters(attrs)) return;

      const to = homePoint(attrs);
      nodes.push({
        node,
        from: limitTransitionOriginTravel(parentPoint, to, cameraState),
        to,
      });
    });

    return nodes;
  }

  function expandBranchNode(node) {
    const attrs = graph.getNodeAttributes(node);
    const childLevel = attrs.kind === 'aggregate'
      ? nextDetailLevel(attrs.detailLevel)
      : null;

    if (!childLevel) return false;
    if (childLevel === 'paper' && Number(attrs.count) > MAX_DIRECT_BRANCH_PAPER_EXPANSION) {
      return false;
    }

    finishLevelTransition();
    const transitionNodes = renderer
      ? prepareBranchExpansionTransition(node, childLevel)
      : [];

    expandedAggregateNodes.add(node);
    pinnedNode = null;
    hoveredNode = null;
    hideTooltip();
    hidePaperModal();
    syncUrlToPinnedNode();
    refreshView();
    startLevelTransition(transitionNodes);
    return true;
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
        enableEdgeEvents: false,
        hideEdgesOnMove: true,
        renderLabels: false,
        renderEdgeLabels: false,
        enableCameraRotation: false,
        labelRenderedSizeThreshold: 0,
        labelDensity: 1,
        labelGridCellSize: 100,
        labelFont: '"Atkinson Hyperlegible Next", "Segoe UI", sans-serif',
        labelSize: NODE_LABEL_FONT_SIZE,
        itemSizesReference: 'positions',
        minEdgeThickness: MIN_EDGE_THICKNESS,
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
    setupFocusLabelOverlay();
    setupGraphEvents();
    setupCameraEvents();
    updateStats();
    window.setTimeout(() => {
      if (!focusPaperFromHash()) fitVisible(0);
    }, 0);
  }

  function setupCameraEvents() {
    // Paper disks are expressed in graph coordinates, so camera movement should
    // not mutate node radii.
  }

  function setupGraphEvents() {
    renderer.on('enterNode', payload => {
      if (pinnedNode) return;
      hoveredNode = payload.node;
      showNodeTooltip(payload.node, eventPosition(payload), false);
      refreshView();
    });

    renderer.on('leaveNode', () => {
      if (pinnedNode) return;
      hoveredNode = null;
      hideTooltip();
      refreshView();
    });

    renderer.on('clickNode', payload => {
      const node = payload.node;
      const attrs = graph.getNodeAttributes(node);

      if (attrs.kind === 'aggregate' && expandBranchNode(node)) {
        return;
      }

      if (pinnedNode === node) {
        pinnedNode = null;
        hoveredNode = null;
        hideTooltip();
        hidePaperModal();
      } else {
        pinnedNode = node;
        hoveredNode = null;
        showNodeTooltip(node, eventPosition(payload), true);
      }
      syncUrlToPinnedNode();
      refreshView();
    });

    renderer.on('clickStage', () => {
      pinnedNode = null;
      hoveredNode = null;
      hideTooltip();
      hidePaperModal();
      syncUrlToPinnedNode();
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
  const modal = document.getElementById('mm-modal');
  const modalTitle = document.getElementById('mm-modal-title');
  const modalBody = document.getElementById('mm-modal-body');
  const modalClose = document.getElementById('mm-modal-close');

  function mobileViewport() {
    return window.matchMedia && window.matchMedia('(max-width: 700px)').matches;
  }

  function formatAuthors(authors) {
    const names = Array.isArray(authors) ? authors.filter(Boolean) : [];
    if (!names.length) return 'Unknown';
    return names.length > 1 ? `${names[0]} et al.` : names[0];
  }

  function showNodeTooltip(node, pos, pinned) {
    const d = graph.getNodeAttributes(node);
    if (mobileViewport()) {
      if (pinned && d.kind === 'paper') showPaperModal(d);
      else hideTooltip();
      return;
    }

    if (d.kind === 'aggregate') {
      showAggregateTooltip(d, pos, pinned);
      return;
    }

    const authors = formatAuthors(d.authors);
    const tags = (d.tags || []).slice(0, 7).join(' · ');
    const actions = paperActionLinks(d, { includeMindMap: false });
    tooltip.innerHTML =
      `<div class="tt-title">${escHtml(d.title)}</div>` +
      `<div class="tt-meta">${escHtml(authors)}&nbsp;&nbsp;${d.year || ''}</div>` +
      (tags ? `<div class="tt-tags">${escHtml(tags)}</div>` : '') +
      (d.summary ? `<div class="tt-summary">${escHtml(d.summary)}</div>` : '') +
      (actions ? `<div class="tt-actions paper-link-pills">${actions}</div>` : '') +
      (!pinned ? `<div class="tt-hint">Click to pin</div>` : `<div class="tt-hint">Click node again to unpin</div>`);
    tooltip.classList.toggle('pinned', pinned);
    placeTooltip(pos);
  }

  function showAggregateTooltip(d, pos, pinned) {
    const level = detailLevelLabel(d.detailLevel);
    const titles = (d.previewTitles || [])
      .map(title => `<li>${escHtml(title)}</li>`)
      .join('');
    const nextIndex = DETAIL_LEVELS.indexOf(d.detailLevel) + 1;
    const nextLabel = DETAIL_LEVELS[nextIndex]
      ? detailLevelLabel(DETAIL_LEVELS[nextIndex])
      : null;
    const directPaperOverflow = DETAIL_LEVELS[nextIndex] === 'paper' &&
      Number(d.count) > MAX_DIRECT_BRANCH_PAPER_EXPANSION;

    tooltip.innerHTML =
      `<div class="tt-title">${escHtml(d.fullLabel || d.title)}</div>` +
      `<div class="tt-meta">${escHtml(level)} group&nbsp;&nbsp;${d.count || 0} items</div>` +
      (titles ? `<ul class="tt-list">${titles}</ul>` : '') +
      (nextLabel && !directPaperOverflow ? `<div class="tt-hint">Click to expand into ${escHtml(nextLabel)}</div>` : '') +
      (directPaperOverflow ? `<div class="tt-hint">Use search, filters, or Items LOD to inspect papers.</div>` : '') +
      (!nextLabel && !pinned ? `<div class="tt-hint">Click to pin</div>` : '') +
      (!nextLabel && pinned ? `<div class="tt-hint">Click node again to unpin</div>` : '');
    tooltip.classList.toggle('pinned', pinned);
    placeTooltip(pos);
  }

  function placeTooltip(pos) {
    const MARGIN = 12;
    const graphRect = graphContainer.getBoundingClientRect();
    const rootStyle = getComputedStyle(document.documentElement);
    const headerHeight = parseFloat(rootStyle.getPropertyValue('--mm-header-h')) || 0;
    const footerHeight = parseFloat(rootStyle.getPropertyValue('--mm-footer-h')) || 0;
    const minY = Math.max(MARGIN, headerHeight + MARGIN);
    const maxY = Math.max(minY, window.innerHeight - footerHeight - MARGIN);

    tooltip.classList.add('visible');
    const W = tooltip.offsetWidth;
    const H = tooltip.offsetHeight;

    let x = graphRect.left + pos.x + MARGIN;
    let y = graphRect.top + pos.y + MARGIN;

    if (x + W + MARGIN > window.innerWidth) x = graphRect.left + pos.x - W - MARGIN;
    if (y + H + MARGIN > maxY) y = graphRect.top + pos.y - H - MARGIN;

    x = Math.max(MARGIN, Math.min(x, window.innerWidth - W - MARGIN));
    y = Math.max(minY, Math.min(y, maxY - H));

    tooltip.style.left = `${x}px`;
    tooltip.style.top = `${y}px`;
  }

  function hideTooltip() {
    tooltip.classList.remove('visible', 'pinned');
  }

  function hidePaperModal() {
    if (!modal) return;
    modal.hidden = true;
    if (modalBody) modalBody.innerHTML = '';
    if (modalTitle) modalTitle.textContent = 'Paper';
  }

  function paperDetailUrl(d) {
    return `../papers/${d.id}/`;
  }

  function paperContentTreeUrl(d) {
    return `../content-tree/#paper=${encodeURIComponent(d.id)}`;
  }

  function paperMindMapUrl(d) {
    return `#paper=${encodeURIComponent(d.id)}`;
  }

  function paperActionLink(url, label, variant, external) {
    if (!url) return '';
    return `<a class="paper-link-pill paper-link-pill--${escHtml(variant || 'internal')}" href="${escHtml(url)}"` +
      (external ? ' target="_blank" rel="noopener noreferrer"' : '') +
      `><span class="paper-link-pill__label">${escHtml(label)}</span></a>`;
  }

  function paperActionLinks(d, options) {
    const includeMindMap = !options || options.includeMindMap !== false;
    return [
      paperActionLink(d.link, 'Open Document (external)', 'primary', true),
      paperActionLink(paperDetailUrl(d), 'Open Detail Page', 'internal', false),
      includeMindMap ? paperActionLink(paperMindMapUrl(d), 'Open in Mind Map', 'internal', false) : '',
      paperActionLink(paperContentTreeUrl(d), 'Open in Content Tree', 'internal', false),
    ].join('');
  }

  function showPaperModal(d) {
    if (!modal || !modalBody || !modalTitle) return;

    const title = d.title || d.fullLabel || d.label || 'Untitled';
    const year = d.year || 'Undated';
    const summary = d.summary || 'No summary recorded yet.';
    const abstract = d.abstract || 'No abstract recorded yet.';
    const tags = (d.tags || [])
      .slice(0, 10)
      .map(tag => `<span>${escHtml(tag)}</span>`)
      .join('');

    hideTooltip();
    modalTitle.textContent = title;
    modalBody.innerHTML =
      `<div class="mm-detail-kicker">${escHtml(year)}</div>` +
      (d.label && d.label !== title ? `<p class="mm-detail-title">${escHtml(d.label)}</p>` : '') +
      `<div class="mm-modal-section-title">Abstract</div>` +
      `<p class="mm-abstract">${escHtml(abstract)}</p>` +
      `<div class="mm-modal-section-title">Summary</div>` +
      `<p class="mm-summary">${escHtml(summary)}</p>` +
      (tags ? `<div class="mm-tags">${tags}</div>` : '') +
      `<div class="mm-detail-actions paper-link-pills">` +
      paperActionLinks(d, { includeMindMap: true }) +
      `</div>`;
    modal.hidden = false;
    if (modalClose) modalClose.focus({ preventScroll: true });
  }

  function closePaperModalSelection() {
    if (!modal || modal.hidden) return;
    hidePaperModal();
    pinnedNode = null;
    hoveredNode = null;
    syncUrlToPinnedNode();
    refreshView();
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
      hidePaperModal();
      syncUrlToPinnedNode();
    }
    refreshView();
  }

  function applyItemTypeFilter() {
    if (pinnedNode && !nodeVisible(pinnedNode)) {
      pinnedNode = null;
      hideTooltip();
      hidePaperModal();
      syncUrlToPinnedNode();
    }
    refreshView();
  }

  function applySearch(query) {
    currentSearch = query.toLowerCase().trim();
    refreshView();
  }

  function applyDetailLevel(level) {
    if (!DETAIL_LEVELS.includes(level)) return;
    if (currentDetailLevel === level) {
      if (!expandedAggregateNodes.size) return;
      finishLevelTransition();
      expandedAggregateNodes.clear();
      pinnedNode = null;
      hoveredNode = null;
      hideTooltip();
      hidePaperModal();
      syncUrlToPinnedNode();
      refreshView();
      return;
    }
    const previousLevel = currentDetailLevel;

    finishLevelTransition();
    const transitionNodes = renderer
      ? prepareLevelTransition(previousLevel, level)
      : [];

    currentDetailLevel = level;
    expandedAggregateNodes.clear();
    pinnedNode = null;
    hoveredNode = null;
    hideTooltip();
    hidePaperModal();
    syncUrlToPinnedNode();
    updateDetailButtons();
    refreshView();
    startLevelTransition(transitionNodes);
  }

  /* -------------------------------------------------------------------------
   * Stats
   * -------------------------------------------------------------------------*/
  function paperNodeRadiusForCurrentView() {
    if (!graph || currentDetailLevel !== 'paper') return PAPER_NODE_RADIUS_TARGET;

    const minDistance = minimumVisiblePaperGraphDistance();
    if (!Number.isFinite(minDistance) || minDistance <= 0) return PAPER_NODE_RADIUS_TARGET;

    return Math.min(
      PAPER_NODE_RADIUS_TARGET,
      minDistance / (2 * (1 + PAPER_NODE_RADIUS_CLEARANCE_RATIO))
    );
  }

  function recomputeVisibleStats() {
    let nodes = 0;
    let edges = 0;

    if (!graph) {
      visibleNodeCount = nodes;
      visibleEdgeCount = edges;
      return;
    }

    graph.forEachNode(node => {
      if (nodeVisible(node)) nodes += 1;
    });
    graph.forEachEdge(edge => {
      if (edgeVisible(edge)) edges += 1;
    });

    visibleNodeCount = nodes;
    visibleEdgeCount = edges;
  }

  function updateStats() {
    if (!graph) return;

    recomputeVisibleStats();

    document.getElementById('mm-node-count').textContent = visibleNodeCount;
    document.getElementById('mm-edge-count').textContent = visibleEdgeCount;
    const levelLabel = document.getElementById('mm-level-label');
    if (levelLabel) levelLabel.textContent = detailLevelLabel(currentDetailLevel, true);
    const searchCount = document.getElementById('mm-search-count');
    if (searchCount) {
      searchCount.hidden = !currentSearch;
      searchCount.textContent = currentSearch
        ? ` · ${searchMatchCount} ${searchMatchCount === 1 ? 'match' : 'matches'}`
        : '';
    }
  }

  /* -------------------------------------------------------------------------
   * Fit to visible graph, leaving space for the overlay panel when open.
   * -------------------------------------------------------------------------*/
  function fitNodeEligible(attrs) {
    return HIERARCHY_LEVEL_BY_ID.has(attrs.detailLevel) && nodeAllowedByFilters(attrs);
  }

  function expandBBoxes(bboxes, rawPoint, framedPoint) {
    bboxes.rawXmin = Math.min(bboxes.rawXmin, rawPoint.x);
    bboxes.rawXmax = Math.max(bboxes.rawXmax, rawPoint.x);
    bboxes.rawYmin = Math.min(bboxes.rawYmin, rawPoint.y);
    bboxes.rawYmax = Math.max(bboxes.rawYmax, rawPoint.y);
    bboxes.framedXmin = Math.min(bboxes.framedXmin, framedPoint.x);
    bboxes.framedXmax = Math.max(bboxes.framedXmax, framedPoint.x);
    bboxes.framedYmin = Math.min(bboxes.framedYmin, framedPoint.y);
    bboxes.framedYmax = Math.max(bboxes.framedYmax, framedPoint.y);
  }

  function finalBBoxes(bboxes) {
    let {
      rawXmin,
      rawXmax,
      rawYmin,
      rawYmax,
      framedXmin,
      framedXmax,
      framedYmin,
      framedYmax,
    } = bboxes;

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

  function allDetailBBoxes() {
    const bboxes = {
      rawXmin: Infinity,
      rawXmax: -Infinity,
      rawYmin: Infinity,
      rawYmax: -Infinity,
      framedXmin: Infinity,
      framedXmax: -Infinity,
      framedYmin: Infinity,
      framedYmax: -Infinity,
    };

    graph.forEachNode((node, attrs) => {
      if (!fitNodeEligible(attrs)) return;

      const rawPoint = homePoint(attrs);
      const displayAttrs = renderer && typeof renderer.getNodeDisplayData === 'function'
        ? renderer.getNodeDisplayData(node)
        : null;
      const framedPoint = displayAttrs &&
        Number.isFinite(displayAttrs.x) &&
        Number.isFinite(displayAttrs.y)
          ? displayAttrs
          : attrs;

      expandBBoxes(bboxes, rawPoint, framedPoint);
    });

    return finalBBoxes(bboxes);
  }

  function visibleBBoxes() {
    let rawXmin = Infinity;
    let rawXmax = -Infinity;
    let rawYmin = Infinity;
    let rawYmax = -Infinity;
    let framedXmin = Infinity;
    let framedXmax = -Infinity;
    let framedYmin = Infinity;
    let framedYmax = -Infinity;

    const bboxes = {
      rawXmin,
      rawXmax,
      rawYmin,
      rawYmax,
      framedXmin,
      framedXmax,
      framedYmin,
      framedYmax,
    };

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

      expandBBoxes(bboxes, attrs, framedPoint);
    });

    return finalBBoxes(bboxes);
  }

  function minimumPointDistance(points) {
    if (!Array.isArray(points) || points.length < 2) return Infinity;

    const sorted = points
      .filter(p => Number.isFinite(p.x) && Number.isFinite(p.y))
      .sort((a, b) => a.x - b.x || a.y - b.y);

    if (sorted.length < 2) return Infinity;

    let minDistSq = Infinity;
    let left = 0;

    for (let i = 0; i < sorted.length; i += 1) {
      const p = sorted[i];
      const currentMin = Number.isFinite(minDistSq) ? Math.sqrt(minDistSq) : Infinity;

      while (left < i && Number.isFinite(currentMin) && p.x - sorted[left].x > currentMin) {
        left += 1;
      }

      for (let j = left; j < i; j += 1) {
        const q = sorted[j];
        const dy = p.y - q.y;
        if (dy * dy >= minDistSq) continue;

        const dx = p.x - q.x;
        const distSq = dx * dx + dy * dy;
        if (distSq < minDistSq) {
          if (distSq === 0) return 0;
          minDistSq = distSq;
        }
      }
    }

    return Number.isFinite(minDistSq) ? Math.sqrt(minDistSq) : Infinity;
  }

  function minimumVisibleGraphDistance() {
    if (!graph) return Infinity;

    const points = [];
    graph.forEachNode((node, attrs) => {
      if (!nodeVisible(node)) return;
      points.push({ x: attrs.x, y: attrs.y });
    });

    return minimumPointDistance(points);
  }

  function minimumVisiblePaperGraphDistance() {
    if (!graph) return Infinity;

    const points = [];
    graph.forEachNode((node, attrs) => {
      if (attrs.kind !== 'paper' || !nodeVisible(node)) return;
      points.push({ x: attrs.x, y: attrs.y });
    });

    return minimumPointDistance(points);
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

    return minimumPointDistance(points);
  }

  function fitVisible(duration) {
    if (!renderer || !graph) return;

    finishLevelTransition();
    renderer.resize(true);
    renderer.refresh();

    const bboxes = allDetailBBoxes() || visibleBBoxes();
    if (!bboxes) return;

    const PAD = VIEWPORT_PADDING;
    const dims = renderer.getDimensions();
    if (!dims.width || !dims.height) return;

    const usable = usableCanvasRect(PAD);
    const left = usable.left;
    const right = usable.right;
    const stagePadding = PAD;
    const desiredX = left < right ? (left + right) / 2 : dims.width / 2;
    const desiredY = usable.top < usable.bottom ? (usable.top + usable.bottom) / 2 : dims.height / 2;
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

    if (duration === 0) renderer.getCamera().setState(target);
    else renderer.getCamera().animate(target, { duration: duration || 260 });
  }

  function readFocusPaperId() {
    const hash = window.location.hash.slice(1);
    if (!hash) return null;

    const params = new URLSearchParams(hash);
    return params.get('paper') || params.get('node');
  }

  function writeFocusPaperId(paperId) {
    const params = new URLSearchParams(window.location.hash.slice(1));

    if (paperId) {
      if (params.get('paper') === paperId && !params.has('node')) return;
      params.set('paper', paperId);
      params.delete('node');
    } else {
      if (!params.has('paper') && !params.has('node')) return;
      params.delete('paper');
      params.delete('node');
    }

    const url = new URL(window.location.href);
    url.hash = params.toString();
    window.history.replaceState(null, '', url);
  }

  function paperIdForNode(node) {
    if (!node || !graphHasNode(node)) return null;
    const attrs = graph.getNodeAttributes(node);
    return attrs.kind === 'paper' ? node : null;
  }

  function syncUrlToPinnedNode() {
    writeFocusPaperId(paperIdForNode(pinnedNode));
  }

  function clearPinnedPaperSelection() {
    if (!paperIdForNode(pinnedNode)) return false;

    pinnedNode = null;
    hoveredNode = null;
    hideTooltip();
    hidePaperModal();
    refreshView();
    return true;
  }

  function overlayBounds(el, graphRect, dims) {
    if (!el) return null;

    const rect = el.getBoundingClientRect();
    const left = clamp(rect.left - graphRect.left, 0, dims.width);
    const right = clamp(rect.right - graphRect.left, 0, dims.width);
    const top = clamp(rect.top - graphRect.top, 0, dims.height);
    const bottom = clamp(rect.bottom - graphRect.top, 0, dims.height);

    if (right <= left || bottom <= top) return null;
    return { left, right, top, bottom, width: right - left, height: bottom - top };
  }

  function usableCanvasRect(pad = VIEWPORT_PADDING) {
    const dims = renderer.getDimensions();
    const graphRect = graphContainer.getBoundingClientRect();
    const minWidth = Math.min(dims.width, pad * 2 + 1);
    const minHeight = Math.min(dims.height, pad * 2 + 1);
    const rect = {
      left: Math.min(pad, dims.width / 2),
      top: Math.min(pad, dims.height / 2),
      right: Math.max(dims.width - pad, minWidth),
      bottom: Math.max(dims.height - pad, minHeight),
    };

    const panel = document.getElementById('mm-panel');
    const panelOpen = panel && !panel.classList.contains('body-collapsed');
    const panelBounds = panelOpen ? overlayBounds(panel, graphRect, dims) : null;

    if (panelBounds && panelBounds.left <= pad && panelBounds.width < dims.width * PANEL_MAX_FOCUS_WIDTH_RATIO) {
      rect.left = Math.max(rect.left, Math.min(panelBounds.right + pad, dims.width - pad));
    }

    const headerBounds = overlayBounds(document.getElementById('mm-panel-header'), graphRect, dims);
    if (headerBounds) {
      const centerX = (rect.left + rect.right) / 2;
      const centerUnderHeader = centerX >= headerBounds.left && centerX <= headerBounds.right;
      if (centerUnderHeader && headerBounds.height < dims.height * 0.5) {
        rect.top = Math.max(rect.top, Math.min(headerBounds.bottom + pad, dims.height - pad));
      }
    }

    if (rect.right <= rect.left) {
      rect.left = Math.min(pad, dims.width / 2);
      rect.right = Math.max(dims.width - pad, rect.left + 1);
    }
    if (rect.bottom <= rect.top) {
      rect.top = Math.min(pad, dims.height / 2);
      rect.bottom = Math.max(dims.height - pad, rect.top + 1);
    }

    return rect;
  }

  function focusCameraOnNode(node, duration) {
    if (!renderer || !graphHasNode(node)) return;

    renderer.resize(true);

    const attrs = graph.getNodeAttributes(node);
    const dims = renderer.getDimensions();
    const usable = usableCanvasRect();
    const desiredX = usable.left < usable.right ? (usable.left + usable.right) / 2 : dims.width / 2;
    const desiredY = usable.top < usable.bottom ? (usable.top + usable.bottom) / 2 : dims.height / 2;
    const ratio = FOCUSED_PAPER_CAMERA_RATIO;
    const nodeViewportPoint = renderer.graphToViewport({ x: attrs.x, y: attrs.y });
    const framedNode = renderer.viewportToFramedGraph(nodeViewportPoint);
    const baseState = { x: framedNode.x, y: framedNode.y, ratio, angle: 0 };
    const framedAtDesiredCenter = renderer.viewportToFramedGraph(
      { x: desiredX, y: desiredY },
      { cameraState: baseState, padding: VIEWPORT_PADDING }
    );
    const target = {
      x: baseState.x + (framedNode.x - framedAtDesiredCenter.x),
      y: baseState.y + (framedNode.y - framedAtDesiredCenter.y),
      ratio,
      angle: 0,
    };

    if (duration === 0) renderer.getCamera().setState(target);
    else renderer.getCamera().animate(target, { duration: duration || 300 });
  }

  function refocusPinnedPaper(duration) {
    const paperId = paperIdForNode(pinnedNode) || readFocusPaperId();
    if (!paperId || !graphHasNode(paperId)) return false;

    const attrs = graph.getNodeAttributes(paperId);
    if (attrs.kind !== 'paper') return false;

    focusCameraOnNode(paperId, duration);
    window.setTimeout(() => showFocusedPaperTooltip(paperId), (duration || 0) + 40);
    return true;
  }

  function showFocusedPaperTooltip(node) {
    if (!renderer || !graphHasNode(node)) return;
    const attrs = graph.getNodeAttributes(node);
    const pos = renderer.graphToViewport({ x: attrs.x, y: attrs.y });
    showNodeTooltip(node, pos, true);
  }

  function focusPaperFromHash() {
    const paperId = readFocusPaperId();
    if (!paperId || !renderer || !graphHasNode(paperId)) return false;

    const attrs = graph.getNodeAttributes(paperId);
    if (attrs.kind !== 'paper') return false;

    currentDetailLevel = 'paper';
    expandedAggregateNodes.clear();
    activeCategories.add(nodeKey(attrs));
    pinnedNode = paperId;
    hoveredNode = null;
    updateDetailButtons();
    refreshView();
    focusCameraOnNode(paperId, 320);
    window.setTimeout(() => showFocusedPaperTooltip(paperId), 340);
    writeFocusPaperId(paperId);
    return true;
  }

  function syncPaperFocusFromHash() {
    if (readFocusPaperId()) {
      const focused = focusPaperFromHash();
      if (!focused) {
        clearPinnedPaperSelection();
        writeFocusPaperId(null);
      }
      return focused;
    }

    return clearPinnedPaperSelection();
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

  function filterLeafKey(group) {
    return [...group.filterKeys][0] || filterKey(group.category, group.subCategory);
  }

  function renderFilterLeaf(group, onChildChange, labelOverride = null, colorOverride = null) {
    const key = filterLeafKey(group);
    activeCategories.add(key);
    return makeCatItem(
      key,
      labelOverride || group.label,
      colorOverride || group.color,
      group.leafIds.length,
      onChildChange
    );
  }

  function renderFilterGroup(group, expanded, className, onChildChange) {
    const { groupEl, groupCb, itemsEl } = makeFilterGroup(
      group.label,
      group.leafIds.length,
      group.color,
      expanded,
      className
    );

    function syncThisGroup() {
      syncGroupCheckbox(groupCb, itemsEl);
      if (onChildChange) onChildChange();
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
      if (onChildChange) onChildChange();
      applyCategoryFilter();
    });

    group.children.forEach(child => {
      itemsEl.appendChild(renderFilterNode(child, syncThisGroup));
    });

    syncGroupCheckbox(groupCb, itemsEl);
    return groupEl;
  }

  function renderFilterNode(group, onChildChange = null) {
    if (!group.children.length) {
      return renderFilterLeaf(group, onChildChange);
    }

    if (group.level === 'category') {
      const onlyCategoryLeaf = group.children.length === 1 && group.children[0].isCategoryLeaf;
      if (onlyCategoryLeaf) {
        return renderFilterLeaf(group.children[0], onChildChange, group.label, group.color);
      }
      return renderFilterGroup(group, false, 'mm-cat-group', onChildChange);
    }

    return renderFilterGroup(group, false, 'mm-cat-group mm-super-group', onChildChange);
  }

  function buildCategoryFilters() {
    const container = document.getElementById('mm-category-filters');
    const model = buildHierarchyData();
    container.innerHTML = '';
    activeCategories.clear();

    model.roots.forEach(root => {
      container.appendChild(renderFilterNode(root));
    });
  }

  function makeTypeItem(type, count) {
    const label = document.createElement('label');
    label.className = 'mm-cat-item mm-type-item';
    label.innerHTML =
      `<input type="checkbox" checked data-type="${escHtml(type)}">` +
      `<span class="mm-type-chip">${escHtml(type === 'Unspecified' ? 'None' : type.split(/\s+/).map(part => part[0]).join('').slice(0, 3))}</span>` +
      `<span class="mm-cat-name">${escHtml(itemTypeLabel(type))}</span>` +
      `<span class="mm-cat-count">${count}</span>`;
    label.querySelector('input').addEventListener('change', e => {
      if (e.target.checked) activeItemTypes.add(type);
      else activeItemTypes.delete(type);
      applyItemTypeFilter();
    });
    return label;
  }

  function buildTypeFilters() {
    const container = document.getElementById('mm-type-filters');
    if (!container) return;

    const counts = new Map();
    DATA.nodes.forEach(node => {
      const type = itemTypeKey(node.data || {});
      counts.set(type, (counts.get(type) || 0) + 1);
    });

    const configured = ((DATA.meta || {}).itemTypeOrder || []).filter(type => counts.has(type));
    const ordered = configured.concat(
      [...counts.keys()]
        .filter(type => !configured.includes(type))
        .sort((a, b) => itemTypeLabel(a).localeCompare(itemTypeLabel(b)))
    );

    container.innerHTML = '';
    activeItemTypes.clear();
    ordered.forEach(type => {
      activeItemTypes.add(type);
      container.appendChild(makeTypeItem(type, counts.get(type)));
    });
  }

  function buildDetailControls() {
    const container = document.getElementById('mm-detail-controls');
    if (!container) return;

    container.innerHTML = '';
    HIERARCHY_LEVELS.forEach(level => {
      const button = document.createElement('button');
      button.type = 'button';
      button.dataset.level = level.id;
      button.title = level.label;
      button.setAttribute('aria-label', `Level of detail: ${level.label}`);
      button.setAttribute('aria-pressed', level.id === currentDetailLevel ? 'true' : 'false');
      button.textContent = level.shortLabel || level.label;
      container.appendChild(button);
    });
  }

  function updateDetailButtons() {
    document.querySelectorAll('#mm-detail-controls button[data-level]').forEach(button => {
      const active = button.dataset.level === currentDetailLevel;
      button.classList.toggle('active', active);
      button.setAttribute('aria-pressed', active ? 'true' : 'false');
    });
  }

  function updateVisibilityButtons() {
    const labelsToggle = document.getElementById('mm-labels-toggle');
    const edgesToggle = document.getElementById('mm-edges-toggle');

    if (labelsToggle) {
      labelsToggle.setAttribute('aria-pressed', showNodeLabels ? 'true' : 'false');
    }
    if (edgesToggle) {
      edgesToggle.setAttribute('aria-pressed', showEdges ? 'true' : 'false');
    }
  }

  /* -------------------------------------------------------------------------
   * Wire up controls
   * -------------------------------------------------------------------------*/
  function setupControls() {
    const slider = document.getElementById('mm-threshold-slider');
    const label = document.getElementById('mm-threshold-val');
    let thresholdRaf = null;
    let pendingThreshold = currentThreshold;
    slider.value = Math.round(currentThreshold * 100);
    label.textContent = currentThreshold.toFixed(2);
    slider.addEventListener('input', e => {
      const t = parseInt(e.target.value, 10) / 100;
      label.textContent = t.toFixed(2);
      pendingThreshold = t;
      if (thresholdRaf !== null) return;

      thresholdRaf = window.requestAnimationFrame(() => {
        thresholdRaf = null;
        applyThreshold(pendingThreshold);
      });
    });

    const search = document.getElementById('mm-search');
    const clearSearch = document.getElementById('mm-search-clear');
    let debounce;
    function updateSearchClearButton() {
      if (clearSearch) clearSearch.hidden = !search.value;
    }
    search.addEventListener('input', e => {
      clearTimeout(debounce);
      updateSearchClearButton();
      debounce = setTimeout(() => applySearch(e.target.value), 180);
    });
    search.addEventListener('keydown', e => {
      if (e.key !== 'Escape' || !search.value) return;
      clearTimeout(debounce);
      search.value = '';
      updateSearchClearButton();
      applySearch('');
    });
    if (clearSearch) {
      clearSearch.addEventListener('click', () => {
        clearTimeout(debounce);
        search.value = '';
        updateSearchClearButton();
        applySearch('');
        search.focus();
      });
    }
    updateSearchClearButton();

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

    document.getElementById('mm-all-types').addEventListener('click', () => {
      document.querySelectorAll('#mm-type-filters input[data-type]').forEach(cb => {
        cb.checked = true;
        activeItemTypes.add(cb.dataset.type);
      });
      applyItemTypeFilter();
    });

    document.getElementById('mm-no-types').addEventListener('click', () => {
      document.querySelectorAll('#mm-type-filters input[data-type]').forEach(cb => {
        cb.checked = false;
        activeItemTypes.delete(cb.dataset.type);
      });
      applyItemTypeFilter();
    });

    const surveyType = document.querySelector('#mm-type-filters input[data-type="Survey Paper"]');
    if (surveyType) {
      surveyType.title = 'Uncheck to exclude surveys';
    }

    document.getElementById('mm-fit-btn').addEventListener('click', () => fitVisible());

    buildDetailControls();
    document.querySelectorAll('#mm-detail-controls button[data-level]').forEach(button => {
      button.addEventListener('click', () => applyDetailLevel(button.dataset.level));
    });
    updateDetailButtons();
    updateVisibilityButtons();

    const labelsToggle = document.getElementById('mm-labels-toggle');
    if (labelsToggle) {
      labelsToggle.addEventListener('click', () => {
        showNodeLabels = !showNodeLabels;
        updateVisibilityButtons();
        if (renderer) renderer.scheduleRefresh();
      });
    }

    const edgesToggle = document.getElementById('mm-edges-toggle');
    if (edgesToggle) {
      edgesToggle.addEventListener('click', () => {
        showEdges = !showEdges;
        updateVisibilityButtons();
        refreshView();
      });
    }

    if (modalClose) modalClose.addEventListener('click', closePaperModalSelection);
    if (modal) {
      modal.addEventListener('click', event => {
        if (event.target === modal) closePaperModalSelection();
      });
    }
    window.addEventListener('keydown', event => {
      if (event.key === 'Escape' && modal && !modal.hidden) closePaperModalSelection();
    });

    const panel = document.getElementById('mm-panel');
    const header = document.getElementById('mm-panel-header');
    const hideBtn = document.getElementById('mm-panel-hide-btn');
    if (window.matchMedia('(max-width: 700px)').matches) {
      panel.classList.add('body-collapsed');
      hideBtn.textContent = 'Show Settings';
      header.title = 'Show Settings';
    }
    header.addEventListener('click', () => {
      const collapsed = panel.classList.toggle('body-collapsed');
      hideBtn.textContent = collapsed ? 'Show Settings' : 'Hide Settings';
      header.title = collapsed ? 'Show Settings' : 'Hide Settings';
      window.setTimeout(() => {
        if (!refocusPinnedPaper(220)) fitVisible();
      }, 280);
    });
  }

  /* -------------------------------------------------------------------------
   * Bootstrap
   * -------------------------------------------------------------------------*/
  buildCategoryFilters();
  buildTypeFilters();
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
    if (renderer) {
      window.setTimeout(() => {
        if (!refocusPinnedPaper(0)) fitVisible(0);
      }, 0);
    }
  });

  window.addEventListener('hashchange', () => {
    syncPaperFocusFromHash();
  });

  // Expose a small debugging/control surface.
  window._mindMap = {
    graph: () => graph,
    renderer: () => renderer,
    fit: fitVisible,
    detailLevel: () => currentDetailLevel,
    setDetailLevel: level => applyDetailLevel(level),
    labelsVisible: () => showNodeLabels,
    edgesVisible: () => showEdges,
    setLabelsVisible: visible => {
      showNodeLabels = Boolean(visible);
      updateVisibilityButtons();
      if (renderer) renderer.scheduleRefresh();
    },
    setEdgesVisible: visible => {
      showEdges = Boolean(visible);
      updateVisibilityButtons();
      refreshView();
    },
    metrics: () => ({
      nodeGraphRadius: currentNodeRadius(),
      nodeGraphRadiusTarget: PAPER_NODE_RADIUS_TARGET,
      nodeScreenRadius: renderer && typeof renderer.scaleSize === 'function'
        ? renderer.scaleSize(currentNodeRadius())
        : currentNodeRadius(),
      minimumVisibleGraphDistance: minimumVisibleGraphDistance(),
      minimumVisibleScreenDistance: minimumVisibleScreenDistance(),
      clearanceRatio: PAPER_NODE_RADIUS_CLEARANCE_RATIO,
      edgeNodeDiameterRatio: EDGE_NODE_DIAMETER_RATIO,
      minEdgeThickness: MIN_EDGE_THICKNESS,
      visibleNodeCount,
      visibleEdgeCount,
      lastLevelTransition: lastLevelTransitionMetrics,
    }),
  };

})();
