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
  const PAPER_NODE_RADIUS_CLEARANCE_RATIO = 0.30;
  const PAPER_NODE_RADIUS = 12;
  const NODE_LABEL_FONT_SIZE = 11;
  const NODE_LABEL_LINE_HEIGHT_RATIO = 1.1;
  const NODE_LABEL_ZOOM_REFERENCE_RATIO = 1;
  const NODE_LABEL_ZOOM_EXPONENT = 0.22;
  const NODE_LABEL_ZOOM_SCALE_MIN = 0.68;
  const NODE_LABEL_ZOOM_SCALE_MAX = 1.55;
  const SELECTED_NODE_RADIUS_SCALE = 1;
  const EDGE_NODE_DIAMETER_RATIO = 0.2;
  const LEVEL_TRANSITION_MS = 260;
  const LEVEL_TRANSITION_MAX_SCREEN_TRAVEL = 160;
  const LEVEL_TRANSITION_DRILLDOWN_TRAVEL_RATIO = 0.58;
  const VIEWPORT_PADDING = 30;
  const PANEL_MAX_FOCUS_WIDTH_RATIO = 0.72;
  const FOCUSED_PAPER_CAMERA_RATIO = 0.32;
  const HIERARCHY_LEVELS = [
    { id: 'super_category', label: 'Super-category', shortLabel: 'Super-category', aggregate: true, filter: true },
    { id: 'category', label: 'Category', shortLabel: 'Category', aggregate: true, filter: true },
    { id: 'sub_category', label: 'Sub-category', shortLabel: 'Sub-category', aggregate: true, filter: true },
    { id: 'paper', label: 'Papers', shortLabel: 'Papers', aggregate: false, filter: false },
  ];
  const HIERARCHY_LEVEL_BY_ID = new Map(HIERARCHY_LEVELS.map(level => [level.id, level]));
  const DETAIL_LEVELS = HIERARCHY_LEVELS.map(level => level.id);
  const ALWAYS_LABELED_DETAIL_LEVELS = new Set(['super_category', 'category']);
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
  let activeCategories = new Set();
  let currentSearch = '';
  let pinnedNode = null;
  let hoveredNode = null;
  let focus = { active: false, nodes: new Set(), edges: new Set(), mode: null };
  let theme = readTheme();
  let hierarchyData = null;
  let activeLevelTransition = null;
  let focusLabelContext = null;
  let lastLevelTransitionMetrics = null;

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
    return PAPER_NODE_RADIUS;
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
    };
  }

  function detailLevelLabel(levelId, short = false) {
    const level = hierarchyLevel(levelId);
    return short ? (level.shortLabel || level.label) : level.label;
  }

  function aggregateNodeSize(count, level) {
    const n = Math.max(Number(count) || 1, 1);
    const scale = Math.sqrt(n);
    if (level === 'super_category') return clamp(110 + scale * 7.5, 125, 210);
    if (level === 'category') return clamp(78 + scale * 5.2, 88, 160);
    return clamp(56 + scale * 4.3, 68, 130);
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

    if (attrs && attrs.kind === 'aggregate') {
      const countBoost = Math.log1p(Number(attrs.aggregateCount) || 1) * 0.2;
      return (1.15 + countBoost) * (0.9 + t * 0.28);
    }

    const paperEdgeRadius = Math.min(currentNodeRadius(), 3);
    const targetWidth = paperEdgeRadius * 2 * EDGE_NODE_DIAMETER_RATIO;
    return targetWidth * (0.9 + t * 0.2);
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

  function paperSuperCategory(attrs) {
    if (isUncategorizedCategory(attrs.category)) return UNCATEGORIZED_CATEGORY;
    return attrs.super_category ||
      categorySuperCategory(attrs.category) ||
      attrs.category ||
      UNCATEGORIZED_CATEGORY;
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
    color,
    parent = null,
    isCategoryLeaf = false,
  }) {
    const pathParts = [superCategory, category, subCategory || (isCategoryLeaf ? category : null)]
      .filter(Boolean);
    return {
      key: `${level}:${pathParts.join('::')}`,
      level,
      label,
      superCategory,
      category,
      subCategory,
      color,
      parent,
      isCategoryLeaf,
      children: [],
      childMap: new Map(),
      leafIds: [],
      filterKeys: new Set(),
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
    group.searchParts.add(paperSearchText(attrs));
    group.x += Number(paperNode.position.x) || 0;
    group.y += Number(paperNode.position.y) || 0;
    if (group.previewTitles.length < 4 && attrs.title) group.previewTitles.push(attrs.title);
  }

  function hierarchySortKey(group) {
    if (group.level === 'super_category') {
      const order = superCategoryOrder();
      const index = order.indexOf(group.label);
      return [index < 0 ? Number.MAX_SAFE_INTEGER : index, group.label];
    }

    if (group.level === 'category') {
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
        color: group.color,
        count,
        leafIds: group.leafIds,
        filterKeys: [...group.filterKeys],
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

  function buildAggregateEdges(level, groupsByLeafId) {
    const edgeMap = new Map();

    DATA.edges.forEach(edge => {
      const attrs = edge.data;
      const sourceGroup = groupsByLeafId.get(attrs.source);
      const targetGroup = groupsByLeafId.get(attrs.target);
      if (!sourceGroup || !targetGroup || sourceGroup === targetGroup) return;

      const sourceId = aggregateNodeId(level, sourceGroup);
      const targetId = aggregateNodeId(level, targetGroup);
      const source = sourceId < targetId ? sourceId : targetId;
      const target = sourceId < targetId ? targetId : sourceId;
      const key = `${source}||${target}`;
      const weight = Number(attrs.weight) || 0;
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

    return [...edgeMap.values()]
      .sort((a, b) => `${a.source}${a.target}`.localeCompare(`${b.source}${b.target}`))
      .map((edge, index) => {
        const meanWeight = edge.count ? edge.weightSum / edge.count : edge.maxWeight;
        return {
          data: {
            id: `agg-edge:${level}:${index}`,
            kind: 'aggregate',
            detailLevel: level,
            source: edge.source,
            target: edge.target,
            weight: Math.round(edge.maxWeight * 10000) / 10000,
            meanWeight: Math.round(meanWeight * 10000) / 10000,
            aggregateCount: edge.count,
            undirected: true,
            edgeAlpha: 0.24,
          },
        };
      });
  }

  function buildHierarchyData() {
    if (hierarchyData) return hierarchyData;

    const roots = [];
    const rootMap = new Map();
    const groupsByLevel = {
      super_category: [],
      category: [],
      sub_category: [],
    };
    const paperToGroups = new Map();
    const paperAncestors = {};
    const aggregateNodes = [];
    const aggregateEdges = [];

    DATA.nodes.forEach(paperNode => {
      const attrs = paperNode.data;
      const superCategory = paperSuperCategory(attrs);
      const category = attrs.category || superCategory || UNCATEGORIZED_CATEGORY;
      const subCategory = attrs.sub_category || null;

      const superGroup = ensureHierarchyChild(null, superCategory, {
        rootMap,
        roots,
        level: 'super_category',
        label: superCategory,
        superCategory,
        category: null,
        subCategory: null,
        color: isUncategorizedCategory(category) ? '#000000' : superCategoryColor(superCategory),
      });

      const categoryGroup = ensureHierarchyChild(superGroup, category, {
        level: 'category',
        label: category,
        superCategory,
        category,
        subCategory: null,
        color: nodeColor(category),
      });

      const leafKey = subCategory || `__category_leaf__:${category}`;
      const leafGroup = ensureHierarchyChild(categoryGroup, leafKey, {
        level: 'sub_category',
        label: subCategory || category,
        superCategory,
        category,
        subCategory,
        color: nodeColor(category, subCategory),
        isCategoryLeaf: !subCategory,
      });

      [superGroup, categoryGroup, leafGroup].forEach(group => {
        accumulateHierarchyGroup(group, paperNode);
      });

      paperToGroups.set(attrs.id, {
        super_category: superGroup,
        category: categoryGroup,
        sub_category: leafGroup,
      });
      paperAncestors[attrs.id] = {
        super_category: aggregateNodeId('super_category', superGroup),
        category: aggregateNodeId('category', categoryGroup),
        sub_category: aggregateNodeId('sub_category', leafGroup),
      };
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
        const groupsByLeafId = new Map();

        DATA.nodes.forEach(paperNode => {
          const paperGroups = paperToGroups.get(paperNode.data.id);
          if (paperGroups && paperGroups[level.id]) {
            groupsByLeafId.set(paperNode.data.id, paperGroups[level.id]);
          }
        });

        groups.forEach(group => aggregateNodes.push(buildAggregateNode(group, level.id)));
        aggregateEdges.push(...buildAggregateEdges(level.id, groupsByLeafId));
      });

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
    if (attrs.kind === 'aggregate') {
      return (attrs.filterKeys || []).some(key => activeCategories.has(key));
    }

    return activeCategories.has(nodeKey(attrs));
  }

  function nodeVisibleAt(node, level) {
    const attrs = graph.getNodeAttributes(node);
    return attrs.detailLevel === level && nodeAllowedByFilters(attrs);
  }

  function nodeVisible(node) {
    return nodeVisibleAt(node, currentDetailLevel);
  }

  function edgeVisible(edge) {
    const attrs = graph.getEdgeAttributes(edge);
    return attrs.detailLevel === currentDetailLevel &&
      attrs.weight >= currentThreshold &&
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
        color: colorWithAlpha(theme.edgeColor, Math.min((attrs.edgeAlpha || 0.2) * theme.edgeAlphaScale, 1)),
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
    const highlighted = focus.nodes.has(node);
    const primaryFocus = highlighted && (
      node === pinnedNode ||
      node === hoveredNode ||
      focus.mode === 'search'
    );
    const muted = focus.active && !primaryFocus;
    const forceLabel = levelAlwaysShowsLabels(attrs) ||
      node === pinnedNode ||
      node === hoveredNode;

    if (muted) {
      const mutedColor = highlighted ? theme.nodeMutedRelated : theme.nodeMuted;
      return {
        ...attrs,
        size,
        color: mutedColor,
        labelColor: theme.mutedLabel,
        labelOutlineColor: colorWithAlpha(mutedColor, 0.55),
        forceLabel,
        zIndex: highlighted ? 1 : 0,
      };
    }

    if (primaryFocus) {
      return {
        ...attrs,
        size: size * SELECTED_NODE_RADIUS_SCALE,
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
      size,
      color: attrs.baseColor,
      labelColor: '#ffffff',
      labelOutlineColor: attrs.baseColor,
      highlighted: false,
      forceLabel,
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
    const size = edgeDisplaySize(attrs.weight, attrs);

    if (dimmed) {
      return {
        ...attrs,
        color: colorWithAlpha(theme.edgeColor, 0.025),
        size: Math.max(size * 0.35, 0.18),
        zIndex: 0,
      };
    }

    if (highlighted) {
      return {
        ...attrs,
        color: theme.edgeHighlighted,
        size: size * 1.25,
        zIndex: 2,
      };
    }

    return {
      ...attrs,
      color: colorWithAlpha(theme.edgeColor, baseAlpha),
      size,
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

  function focusedLabelNodes() {
    const nodes = [];

    [pinnedNode, hoveredNode].forEach(node => {
      if (!node || nodes.includes(node) || !graphHasNode(node) || !nodeVisible(node)) return;
      nodes.push(node);
    });

    return nodes;
  }

  function drawFocusLabelOverlay() {
    if (!focusLabelContext || !renderer || !graph) return;

    clearFocusLabelOverlay();
    focusedLabelNodes().forEach(node => {
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

  function refreshView() {
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
        renderLabels: true,
        renderEdgeLabels: false,
        enableCameraRotation: false,
        labelRenderedSizeThreshold: 0,
        labelDensity: 1,
        labelGridCellSize: 100,
        labelFont: '"Atkinson Hyperlegible Next", "Segoe UI", sans-serif',
        labelSize: NODE_LABEL_FONT_SIZE,
        itemSizesReference: 'positions',
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
      const nextLevel = attrs.kind === 'aggregate'
        ? nextDetailLevel(attrs.detailLevel)
        : null;

      if (nextLevel) {
        applyDetailLevel(nextLevel);
        return;
      }

      if (pinnedNode === node) {
        pinnedNode = null;
        hoveredNode = null;
        hideTooltip();
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

  function formatAuthors(authors) {
    const names = Array.isArray(authors) ? authors.filter(Boolean) : [];
    if (!names.length) return 'Unknown';
    return names.length > 1 ? `${names[0]} et al.` : names[0];
  }

  function showNodeTooltip(node, pos, pinned) {
    const d = graph.getNodeAttributes(node);
    if (d.kind === 'aggregate') {
      showAggregateTooltip(d, pos, pinned);
      return;
    }

    const authors = formatAuthors(d.authors);
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

  function showAggregateTooltip(d, pos, pinned) {
    const level = detailLevelLabel(d.detailLevel);
    const titles = (d.previewTitles || [])
      .map(title => `<li>${escHtml(title)}</li>`)
      .join('');
    const nextIndex = DETAIL_LEVELS.indexOf(d.detailLevel) + 1;
    const nextLabel = DETAIL_LEVELS[nextIndex]
      ? detailLevelLabel(DETAIL_LEVELS[nextIndex])
      : null;

    tooltip.innerHTML =
      `<div class="tt-title">${escHtml(d.fullLabel || d.title)}</div>` +
      `<div class="tt-meta">${escHtml(level)} group&nbsp;&nbsp;${d.count || 0} items</div>` +
      (titles ? `<ul class="tt-list">${titles}</ul>` : '') +
      (nextLabel ? `<div class="tt-hint">Click to reveal ${escHtml(nextLabel)}</div>` : '') +
      (!nextLabel && !pinned ? `<div class="tt-hint">Click to pin</div>` : '') +
      (!nextLabel && pinned ? `<div class="tt-hint">Click node again to unpin</div>` : '');
    tooltip.classList.toggle('pinned', pinned);
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
      syncUrlToPinnedNode();
    }
    refreshView();
  }

  function applySearch(query) {
    currentSearch = query.toLowerCase().trim();
    refreshView();
  }

  function applyDetailLevel(level) {
    if (!DETAIL_LEVELS.includes(level) || currentDetailLevel === level) return;
    const previousLevel = currentDetailLevel;

    finishLevelTransition();
    const transitionNodes = renderer
      ? prepareLevelTransition(previousLevel, level)
      : [];

    currentDetailLevel = level;
    pinnedNode = null;
    hoveredNode = null;
    hideTooltip();
    syncUrlToPinnedNode();
    updateDetailButtons();
    refreshView();
    startLevelTransition(transitionNodes);
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
    const levelLabel = document.getElementById('mm-level-label');
    if (levelLabel) levelLabel.textContent = detailLevelLabel(currentDetailLevel, true);
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

  function minimumVisibleGraphDistance() {
    if (!graph) return Infinity;

    const points = [];
    graph.forEachNode((node, attrs) => {
      if (!nodeVisible(node)) return;
      points.push({ x: attrs.x, y: attrs.y });
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
    if (group.level === 'sub_category') {
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

  function buildDetailControls() {
    const container = document.getElementById('mm-detail-controls');
    if (!container) return;

    container.innerHTML = '';
    HIERARCHY_LEVELS.forEach(level => {
      const button = document.createElement('button');
      button.type = 'button';
      button.dataset.level = level.id;
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

    buildDetailControls();
    document.querySelectorAll('#mm-detail-controls button[data-level]').forEach(button => {
      button.addEventListener('click', () => applyDetailLevel(button.dataset.level));
    });
    updateDetailButtons();

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
    metrics: () => ({
      nodeGraphRadius: currentNodeRadius(),
      nodeScreenRadius: renderer && typeof renderer.scaleSize === 'function'
        ? renderer.scaleSize(currentNodeRadius())
        : currentNodeRadius(),
      minimumVisibleGraphDistance: minimumVisibleGraphDistance(),
      minimumVisibleScreenDistance: minimumVisibleScreenDistance(),
      clearanceRatio: PAPER_NODE_RADIUS_CLEARANCE_RATIO,
      lastLevelTransition: lastLevelTransitionMetrics,
    }),
  };

})();
