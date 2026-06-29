/* map.js - Sigma.js paper map visualisation
 *
 * Loaded by map.md after:
 *   1. graphology.umd.min.js (sets window.graphology)
 *   2. sigma.min.js          (sets window.Sigma)
 *   3. map-data.js           (sets window.mapData, includes UMAP positions)
 *   4. map-paper-derivations.js (sets window.kbMapPaperDerivations)
 *   5. browser-map-model.js  (sets window.kbBrowserMapModel)
 *   6. map-view-state.js     (sets window.kbMapViewState)
 */

'use strict';

(function () {

  /* -------------------------------------------------------------------------
   * Hierarchy-aware category colours.
   *
   * Black is reserved for uncategorized papers only. Static tree controls derive
   * their colour from the tree hierarchy:
   *   super-category -> distinct hue family
   *   sibling category -> slight hue/lightness variation
   *   sub-category -> smaller variation around its category
   *
   * Rendered nodes are recoloured dynamically from the shared CSS palette based
   * on the broadest branch split among the currently visible papers.
   * -------------------------------------------------------------------------*/
  const UNCATEGORIZED_CATEGORY = 'Uncategorized';
  const UNCATEGORIZED_CATEGORIES = new Set([UNCATEGORIZED_CATEGORY, 'Other']);

  const WCAG_NORMAL_TEXT_CONTRAST = 4.5;
  const NODE_LABEL_LIGHT = '#FFFFFF';
  const NODE_LABEL_DARK = '#000000';
  const VISIBILITY_BRANCH_PALETTE_CSS_PREFIX = '--kb-map-node-color-';
  const VISIBILITY_BRANCH_PALETTE_SIZE = 12;
  const VISIBILITY_BRANCH_PALETTE_FALLBACKS = {
    light: [
      '#005AB5',
      '#A52A00',
      '#00735C',
      '#8F3B76',
      '#8A5A00',
      '#006A8E',
      '#5E3C99',
      '#6B4E16',
      '#005F73',
      '#9B2226',
      '#3A6B15',
      '#7B3294',
    ],
    dark: [
      '#6BB6FF',
      '#FF9B5C',
      '#5FE0B5',
      '#F39BD4',
      '#F6C85F',
      '#8EDAEF',
      '#C6A4FF',
      '#D6B46D',
      '#7CD9D0',
      '#FF8A94',
      '#A7D96D',
      '#D6A0F7',
    ],
  };

  /* -------------------------------------------------------------------------
   * Guard: dependencies and data must be present
   * -------------------------------------------------------------------------*/
  const graphContainer = document.getElementById('mm-graph');
  setupSettingsPanelToggle();

  if (!graphContainer) {
    hideLoading();
    return;
  }

  if (typeof mapData === 'undefined') {
    graphContainer.innerHTML =
      '<p style="padding:2em;color:#ccc">No map data found.<br>' +
      'Run <code>python generate_map_data.py</code> from the repo root first.</p>';
    hideLoading();
    return;
  }

  if (typeof window.graphology === 'undefined' || typeof window.Sigma === 'undefined') {
    const missing = [
      typeof window.graphology === 'undefined' ? 'Graphology' : null,
      typeof window.Sigma === 'undefined' ? 'Sigma' : null,
    ].filter(Boolean).join(' and ');
    graphContainer.innerHTML =
      `<p style="padding:2em;color:#ccc">Map viewer libraries failed to load: ${missing}.</p>`;
    hideLoading();
    return;
  }

  const DATA = mapData;
  const MAP_SCRIPT_URL = document.currentScript && document.currentScript.src
    ? document.currentScript.src
    : window.location.href;
  const NODE_DIAMETER_SCALE = 2;
  const PAPER_NODE_RADIUS_CLEARANCE_RATIO = 0.30;
  const PAPER_NODE_RADIUS_TARGET = 12 * NODE_DIAMETER_SCALE;
  const MIN_CAMERA_RATIO = 0.04;
  const FALLBACK_MAX_CAMERA_RATIO = 6;
  const MAX_ZOOM_OUT_OVERSCAN_RATIO = 1.12;
  const MIN_NODE_SCREEN_DIAMETER = 4;
  const MIN_NODE_SCREEN_RADIUS = MIN_NODE_SCREEN_DIAMETER / 2;
  const MIN_NODE_SCREEN_RADIUS_BLEND_RATIO = 0.5;
  const MOBILE_MIN_NODE_SCREEN_DIAMETER = 4.4;
  const MOBILE_MIN_NODE_SCREEN_RADIUS = MOBILE_MIN_NODE_SCREEN_DIAMETER / 2;
  const AGGREGATE_EXTRA_AREA_UNITS_BY_LEVEL = [18, 12, 8, 5, 3];
  const AGGREGATE_EXTRA_AREA_FALLBACK_UNITS = 2;
  const AGGREGATE_MIN_RADIUS_RATIO = 1.7;
  const LABEL_RENDERED_SIZE_THRESHOLD = 3;
  const LABEL_DENSITY = 0.08;
  const LABEL_GRID_CELL_SIZE = 112;
  const NODE_LABEL_FONT_SIZE = 11;
  const NODE_LABEL_FONT_SIZE_MIN = 9;
  const NODE_LABEL_FONT_SIZE_MAX = 24;
  const NODE_LABEL_DIAMETER_EXPONENT = 0.34;
  const NODE_LABEL_LINE_HEIGHT_RATIO = 1.1;
  const NODE_LABEL_MAX_LINE_CHARS = 15;
  const NODE_LABEL_MAX_LINES = 4;
  const NODE_LABEL_ZOOM_REFERENCE_RATIO = 1;
  const NODE_LABEL_ZOOM_EXPONENT = 0.22;
  const NODE_LABEL_ZOOM_SCALE_MIN = 0.68;
  const NODE_LABEL_ZOOM_SCALE_MAX = 1.55;
  const NODE_BORDER_WIDTH_RATIO = 0.08;
  const BORDERED_NODE_TYPE = 'bordered';
  const SELECTED_NODE_RADIUS_SCALE = 1;
  const DEFAULT_RELEVANCE_SIMILARITY = 0.79;
  const DEFAULT_RELEVANCE_TREE_PROXIMITY = 0.79;
  const RELEVANCE_SLIDER_EXPANDED_THRESHOLD = 0.70;
  const RELEVANCE_SLIDER_EXPANDED_POSITION = 0.20;
  const RELEVANCE_SLIDER_EXPONENT = Math.log(1 - RELEVANCE_SLIDER_EXPANDED_THRESHOLD) /
    Math.log(1 - RELEVANCE_SLIDER_EXPANDED_POSITION);
  const LEVEL_TRANSITION_MS = 260;
  const LEVEL_TRANSITION_MAX_SCREEN_TRAVEL = 160;
  const LEVEL_TRANSITION_DRILLDOWN_TRAVEL_RATIO = 0.58;
  const AGGREGATE_POSITION_OUTER_QUANTILE = 0.84;
  const AGGREGATE_POSITION_BIAS_BY_LEVEL = [0.68, 0.52, 0.36, 0.24];
  const VIEWPORT_PADDING = 30;
  const PANEL_MAX_FOCUS_WIDTH_RATIO = 0.72;
  const FOCUSED_PAPER_CAMERA_RATIO = 0.32;
  const PAN_CLICK_DRAG_THRESHOLD = 6;
  const PAN_CLICK_SUPPRESS_MS = 350;
  const LEGACY_BRANCH_LEVEL_IDS = ['super_category', 'category', 'sub_category'];
  const BRANCH_FILTER_ALL = '__all__';
  const BRANCH_FILTER_PAPER_PREFIX = 'paper:';
  const categorySuperCategoryLookup = new Map();
  const categoryOrderCache = { value: null };
  const superCategoryOrderCache = { value: null };
  const stableBranchLabelCache = new Map();
  const NAV_PATH_ORDER = ((DATA.meta || {}).navPathOrder || [])
    .filter(path => Array.isArray(path))
    .map(path => path.map(part => String(part || '').trim()).filter(Boolean))
    .filter(path => path.length);
  const navPathOrderIndex = new Map(
    NAV_PATH_ORDER.map((path, index) => [path.join('::'), index])
  );
  if (
    !window.kbMapPaperDerivations ||
    typeof window.kbMapPaperDerivations.createMapPaperDerivations !== 'function' ||
    !window.kbBrowserMapModel ||
    typeof window.kbBrowserMapModel.createBrowserMapModel !== 'function' ||
    !window.kbMapViewState ||
    typeof window.kbMapViewState.createMapViewState !== 'function'
  ) {
    graphContainer.innerHTML =
      '<p style="padding:2em;color:#ccc">Map viewer model scripts failed to load.</p>';
    hideLoading();
    return;
  }
  let aggregateLevelCount = 0;
  const paperDerivations = window.kbMapPaperDerivations.createMapPaperDerivations({
    uncategorizedCategory: UNCATEGORIZED_CATEGORY,
    paperSuperCategory,
    aggregateLevelCount: () => aggregateLevelCount,
  });
  const {
    clamp,
    paperNavPath,
    paperSearchText,
  } = paperDerivations;
  const HIERARCHY_LEVELS = buildHierarchyLevels();
  const HIERARCHY_LEVEL_BY_ID = new Map(HIERARCHY_LEVELS.map(level => [level.id, level]));
  const DETAIL_LEVELS = HIERARCHY_LEVELS.map(level => level.id);
  const DETAIL_CONTROL_LEVELS = buildDetailControlLevels();
  const AGGREGATE_LEVELS = new Set(
    HIERARCHY_LEVELS.filter(level => level.aggregate).map(level => level.id)
  );
  aggregateLevelCount = AGGREGATE_LEVELS.size;

  /* -------------------------------------------------------------------------
   * State
   * -------------------------------------------------------------------------*/
  let graph = null;
  let renderer = null;
  const viewState = window.kbMapViewState.createMapViewState({
    initialDetailLevel: HIERARCHY_LEVELS[0].id,
    branchFilterAll: BRANCH_FILTER_ALL,
    defaultRelevanceSimilarity: DEFAULT_RELEVANCE_SIMILARITY,
    relevanceFilter: {
      treeProximity: null,
    },
  });
  let theme = readTheme();
  let relevanceEvaluationCache = null;
  let relevanceRefreshFrame = null;
  let activeLevelTransition = null;
  let topLabelContext = null;
  let lastLevelTransitionMetrics = null;
  let cachedPaperNodeRadius = PAPER_NODE_RADIUS_TARGET;
  let visibilityColorContext = null;
  let visibilityPaletteCache = null;
  let graphToViewportRatioCache = null;
  let lastCameraRenderRatio = null;
  let graphPanGesture = null;
  let suppressGraphClickUntil = 0;
  let interactionRefreshFrame = null;

  /* -------------------------------------------------------------------------
   * Utility
   * -------------------------------------------------------------------------*/
  function hideLoading() {
    const el = document.getElementById('mm-loading');
    if (el) el.style.display = 'none';
  }

  function isUncategorizedCategory(category) {
    return !category || UNCATEGORIZED_CATEGORIES.has(category);
  }

  function categorySuperCategory(category) {
    if (categorySuperCategoryLookup.has(category)) {
      return categorySuperCategoryLookup.get(category);
    }

    const explicit = ((DATA.meta || {}).categorySuperCategory || {})[category];
    if (explicit) {
      categorySuperCategoryLookup.set(category, explicit);
      return explicit;
    }

    const node = DATA.nodes.find(n =>
      n.data.category === category && n.data.super_category
    );
    const superCategory = node ? node.data.super_category : null;
    categorySuperCategoryLookup.set(category, superCategory);
    return superCategory;
  }

  function categoryOrder() {
    if (categoryOrderCache.value) return categoryOrderCache.value;

    const configured = (DATA.meta || {}).categoryOrder || [];
    const dataCategories = new Set(DATA.nodes.map(n => n.data.category).filter(Boolean));
    const ordered = configured.filter(cat => dataCategories.has(cat));

    [...dataCategories]
      .sort((a, b) => a.localeCompare(b))
      .forEach(cat => {
        if (!ordered.includes(cat)) ordered.push(cat);
      });

    categoryOrderCache.value = ordered;
    return ordered;
  }

  function superCategoryOrder() {
    if (superCategoryOrderCache.value) return superCategoryOrderCache.value;

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

    superCategoryOrderCache.value = ordered;
    return ordered;
  }

  function hexToRgb(hexColor) {
    const color = normalizedCssColor(hexColor);
    let m;
    if ((m = String(color || '').match(/^#([0-9a-f]{3})$/i))) {
      const hex = m[1].split('').map(ch => ch + ch).join('');
      return {
        r: parseInt(hex.slice(0, 2), 16),
        g: parseInt(hex.slice(2, 4), 16),
        b: parseInt(hex.slice(4, 6), 16),
      };
    }
    if ((m = String(color || '').match(/^#([0-9a-f]{6})$/i))) {
      const hex = m[1];
      return {
        r: parseInt(hex.slice(0, 2), 16),
        g: parseInt(hex.slice(2, 4), 16),
        b: parseInt(hex.slice(4, 6), 16),
      };
    }
    return null;
  }

  function linearizedSrgb(channel) {
    const c = clamp(channel, 0, 255) / 255;
    return c <= 0.03928
      ? c / 12.92
      : Math.pow((c + 0.055) / 1.055, 2.4);
  }

  function relativeLuminance(color) {
    const rgb = hexToRgb(color);
    if (!rgb) return null;

    return 0.2126 * linearizedSrgb(rgb.r) +
      0.7152 * linearizedSrgb(rgb.g) +
      0.0722 * linearizedSrgb(rgb.b);
  }

  function contrastRatio(a, b) {
    const la = relativeLuminance(a);
    const lb = relativeLuminance(b);
    if (la === null || lb === null) return 1;

    const lighter = Math.max(la, lb);
    const darker = Math.min(la, lb);
    return (lighter + 0.05) / (darker + 0.05);
  }

  function accessibleNodeLabelColor(nodeColorValue) {
    const lightContrast = contrastRatio(nodeColorValue, NODE_LABEL_LIGHT);
    const darkContrast = contrastRatio(nodeColorValue, NODE_LABEL_DARK);
    const best = lightContrast >= darkContrast ? NODE_LABEL_LIGHT : NODE_LABEL_DARK;
    const bestContrast = Math.max(lightContrast, darkContrast);

    if (bestContrast >= WCAG_NORMAL_TEXT_CONTRAST) return best;
    return theme && theme.colorScheme === 'dark' ? NODE_LABEL_LIGHT : NODE_LABEL_DARK;
  }

  function currentColorScheme() {
    const explicit = (
      document.body && document.body.getAttribute('data-md-color-scheme')
    ) || document.documentElement.getAttribute('data-md-color-scheme');
    if (explicit === 'slate') return 'dark';
    if (explicit === 'default') return 'light';
    if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
      return 'dark';
    }
    return 'light';
  }

  function currentVisibilityPalette() {
    const colorScheme = currentColorScheme();
    if (visibilityPaletteCache && visibilityPaletteCache.colorScheme === colorScheme) {
      return visibilityPaletteCache.palette;
    }

    const cssPalette = cssVisibilityPalette();
    const palette = cssPalette.length >= VISIBILITY_BRANCH_PALETTE_SIZE
      ? cssPalette
      : VISIBILITY_BRANCH_PALETTE_FALLBACKS[colorScheme] ||
      VISIBILITY_BRANCH_PALETTE_FALLBACKS.light;

    visibilityPaletteCache = { colorScheme, palette };
    return palette;
  }

  function cssVisibilityPalette() {
    const styleSources = [];
    if (document.body) styleSources.push(getComputedStyle(document.body));
    styleSources.push(getComputedStyle(document.documentElement));

    const palette = [];
    for (let index = 1; index <= VISIBILITY_BRANCH_PALETTE_SIZE; index += 1) {
      const property = `${VISIBILITY_BRANCH_PALETTE_CSS_PREFIX}${index}`;
      const raw = styleSources
        .map(styles => styles.getPropertyValue(property).trim())
        .find(Boolean);
      const color = normalizedCssColor(raw);
      if (color) palette.push(color);
    }

    return palette;
  }

  function readTheme() {
    const cs = getComputedStyle(document.body);
    const v = name => cs.getPropertyValue(name).trim();
    const colorScheme = currentColorScheme();
    return {
      colorScheme,
      nodeMuted: normalizedCssColor(v('--mm-node-muted')) || '#8A949E',
      nodeMutedRelated: normalizedCssColor(v('--mm-node-muted-related')) || '#737D88',
      nodeGhost: normalizedCssColor(v('--mm-node-ghost')) ||
        (colorScheme === 'dark' ? '#222A33' : '#EDF1F5'),
      nodeGhostBorder: normalizedCssColor(v('--mm-node-ghost-border')) ||
        (colorScheme === 'dark' ? '#56616D' : '#B8C2CC'),
      nodeBorder: normalizedCssColor(v('--mm-node-border')) ||
        (colorScheme === 'dark' ? '#242B35' : '#E1E7EE'),
      selectedRing: normalizedCssColor(v('--mm-selected-ring')) || '#D9A316',
    };
  }

  function normalizedCssColor(color) {
    const c = String(color || '').trim();
    return c && !c.startsWith('color-mix(') && !c.startsWith('var(') ? c : null;
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

  function graphToViewportRatioForCurrentCamera() {
    if (!renderer || typeof renderer.graphToViewport !== 'function') return null;

    const camera = typeof renderer.getCamera === 'function'
      ? renderer.getCamera()
      : null;
    const cameraState = camera && typeof camera.getState === 'function'
      ? camera.getState()
      : null;
    const dims = typeof renderer.getDimensions === 'function'
      ? renderer.getDimensions()
      : { width: 0, height: 0 };
    const graphDims = typeof renderer.getGraphDimensions === 'function'
      ? renderer.getGraphDimensions()
      : { width: 0, height: 0 };
    const padding = typeof renderer.getSetting === 'function'
      ? renderer.getSetting('stagePadding')
      : 0;
    const ratio = cameraState && Number(cameraState.ratio);
    const key = [
      Number.isFinite(ratio) ? ratio : NODE_LABEL_ZOOM_REFERENCE_RATIO,
      dims.width || 0,
      dims.height || 0,
      graphDims.width || 0,
      graphDims.height || 0,
      padding || 0,
    ].join(':');

    if (graphToViewportRatioCache && graphToViewportRatioCache.key === key) {
      return graphToViewportRatioCache.value;
    }

    const options = cameraState ? { cameraState, padding } : { padding };
    const a = renderer.graphToViewport({ x: 0, y: 0 }, options);
    const b = renderer.graphToViewport({ x: 1, y: 1 }, options);
    const value = Math.sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y)) / Math.SQRT2;

    graphToViewportRatioCache = {
      key,
      value: Number.isFinite(value) && value > 0 ? value : null,
    };
    return graphToViewportRatioCache.value;
  }

  function nodeSizeWithMinimumScreenRadius(size) {
    const baseSize = Number.isFinite(size) && size > 0 ? size : PAPER_NODE_RADIUS_TARGET;
    const graphToViewportRatio = graphToViewportRatioForCurrentCamera();
    if (!Number.isFinite(graphToViewportRatio) || graphToViewportRatio <= 0) return baseSize;

    const screenRadius = softMinimumScreenRadius(
      baseSize * graphToViewportRatio,
      minimumNodeScreenRadius()
    );
    return screenRadius / graphToViewportRatio;
  }

  function softMinimumScreenRadius(radius, minimum) {
    if (!Number.isFinite(radius) || radius <= 0) return minimum;

    const blend = minimum * MIN_NODE_SCREEN_RADIUS_BLEND_RATIO;
    if (!Number.isFinite(blend) || blend <= 0) return Math.max(radius, minimum);

    const distance = Math.abs(radius - minimum);
    if (distance >= blend) return Math.max(radius, minimum);

    // Smooth max: dots stay proportional until near the floor, then ease into it.
    return Math.max(radius, minimum) + ((blend - distance) * (blend - distance)) / (blend * 4);
  }

  function minimumNodeScreenRadius() {
    return mobileViewport()
      ? MOBILE_MIN_NODE_SCREEN_RADIUS
      : MIN_NODE_SCREEN_RADIUS;
  }

  function currentNodeLabelZoomScale() {
    return nodeLabelZoomScaleForRatio(currentCameraRatio());
  }

  function nodeLabelZoomScaleForRatio(ratio) {
    const safeRatio = Number.isFinite(ratio) && ratio > 0
      ? ratio
      : NODE_LABEL_ZOOM_REFERENCE_RATIO;
    return clamp(
      Math.pow(NODE_LABEL_ZOOM_REFERENCE_RATIO / safeRatio, NODE_LABEL_ZOOM_EXPONENT),
      NODE_LABEL_ZOOM_SCALE_MIN,
      NODE_LABEL_ZOOM_SCALE_MAX
    );
  }

  function currentNodeLabelMetrics(data, zoomScale = currentNodeLabelZoomScale()) {
    const baseFontSize = Number.isFinite(data.labelFontSize)
      ? data.labelFontSize
      : NODE_LABEL_FONT_SIZE;
    const baseLineHeight = Number.isFinite(data.labelLineHeight)
      ? data.labelLineHeight
      : baseFontSize * NODE_LABEL_LINE_HEIGHT_RATIO;
    const fontSize = baseFontSize * zoomScale;

    return {
      fontSize,
      lineHeight: baseLineHeight * zoomScale,
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
    const maxDepth = Math.max(4, configuredDepth || 0, dataDepth);
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

  function buildDetailControlLevels() {
    const fixedAggregateLevels = HIERARCHY_LEVELS
      .filter(level => level.aggregate && level.pathIndex < 4);
    const itemLevel = HIERARCHY_LEVEL_BY_ID.get('paper');

    return itemLevel
      ? fixedAggregateLevels.concat(itemLevel)
      : fixedAggregateLevels;
  }

  function activeBranchDetailFloorIndex() {
    const group = viewState.branchFilterGroups.get(viewState.activeBranchFilterKey);
    return group ? Math.max(Number(group.pathIndex) || 0, 0) : 0;
  }

  function detailLevelAllowedForActiveBranch(levelId) {
    return (Number(hierarchyLevel(levelId).pathIndex) || 0) >= activeBranchDetailFloorIndex();
  }

  function detailLevelForActiveBranch(levelId) {
    if (!DETAIL_LEVELS.includes(levelId)) return null;
    if (detailLevelAllowedForActiveBranch(levelId)) return levelId;

    const floorIndex = activeBranchDetailFloorIndex();
    const fallback = DETAIL_CONTROL_LEVELS.find(level => (Number(level.pathIndex) || 0) >= floorIndex);
    return fallback ? fallback.id : 'paper';
  }

  function detailLevelLabel(levelId, short = false) {
    const level = hierarchyLevel(levelId);
    return short ? (level.shortLabel || level.label) : level.label;
  }

  function aggregateNodeSize(count, level) {
    const n = Math.max(Number(count) || 1, 1);
    const index = Math.max(hierarchyLevel(level).pathIndex || 0, 0);
    const extraAreaUnits = AGGREGATE_EXTRA_AREA_UNITS_BY_LEVEL[index] ||
      AGGREGATE_EXTRA_AREA_FALLBACK_UNITS;
    const equivalentItemCount = n + extraAreaUnits;
    const radius = PAPER_NODE_RADIUS_TARGET * Math.sqrt(equivalentItemCount);
    const minRadius = PAPER_NODE_RADIUS_TARGET * AGGREGATE_MIN_RADIUS_RATIO;

    return Math.max(radius, minRadius);
  }

  function median(values) {
    const sorted = values
      .filter(value => Number.isFinite(value))
      .sort((a, b) => a - b);
    if (!sorted.length) return null;

    const mid = Math.floor(sorted.length / 2);
    return sorted.length % 2
      ? sorted[mid]
      : (sorted[mid - 1] + sorted[mid]) / 2;
  }

  function labelFontSizeForDiskDiameter(diameter) {
    const referenceDiameter = PAPER_NODE_RADIUS_TARGET * 2;
    const ratio = Math.max(Number(diameter) || referenceDiameter, 1) / referenceDiameter;
    return clamp(
      NODE_LABEL_FONT_SIZE * Math.pow(ratio, NODE_LABEL_DIAMETER_EXPONENT),
      NODE_LABEL_FONT_SIZE_MIN,
      NODE_LABEL_FONT_SIZE_MAX
    );
  }

  function precomputeNodeLabelMetrics(nodeSpecs) {
    const diametersByLevel = new Map();

    nodeSpecs.forEach(spec => {
      const level = spec.detailLevel || 'paper';
      const radius = Number.isFinite(spec.baseSize) ? spec.baseSize : PAPER_NODE_RADIUS_TARGET;
      if (!diametersByLevel.has(level)) diametersByLevel.set(level, []);
      diametersByLevel.get(level).push(radius * 2);
    });

    const metricsByLevel = new Map();
    DETAIL_LEVELS.forEach(level => {
      const diameter = median(diametersByLevel.get(level) || []) || (PAPER_NODE_RADIUS_TARGET * 2);
      const fontSize = Math.round(labelFontSizeForDiskDiameter(diameter) * 10) / 10;
      metricsByLevel.set(level, {
        fontSize,
        lineHeight: Math.round(fontSize * NODE_LABEL_LINE_HEIGHT_RATIO * 10) / 10,
        sourceDiskDiameter: Math.round(diameter * 10) / 10,
      });
    });

    return metricsByLevel;
  }

  function nodeDisplaySize(attrs) {
    if (attrs.kind === 'aggregate') {
      return Number.isFinite(attrs.staticSize)
        ? attrs.staticSize
        : aggregateNodeSize(attrs.count, attrs.detailLevel);
    }
    return currentNodeRadius();
  }

  /* -------------------------------------------------------------------------
   * Format node label: keep lines narrow so long labels stay compact around
   * node disks and participate more cleanly in Sigma's label deconfliction.
   * -------------------------------------------------------------------------*/
  function wrapLabelLine(line, maxChars) {
    const words = String(line || '').trim().split(/\s+/).filter(Boolean);
    const lines = [];
    let current = '';

    words.forEach(word => {
      if (!current) {
        current = word;
      } else if ((current.length + 1 + word.length) <= maxChars) {
        current += ` ${word}`;
      } else {
        lines.push(current);
        current = word;
      }
    });

    if (current) lines.push(current);
    return lines.length ? lines : [''];
  }

  function limitLabelLines(lines, maxLines = NODE_LABEL_MAX_LINES) {
    if (lines.length <= maxLines) return lines;

    const limited = lines.slice(0, maxLines);
    const last = limited[limited.length - 1];
    limited[limited.length - 1] = last.length > NODE_LABEL_MAX_LINE_CHARS - 1
      ? `${last.slice(0, Math.max(1, NODE_LABEL_MAX_LINE_CHARS - 1))}...`
      : `${last}...`;
    return limited;
  }

  function formatLabel(label) {
    const text = String(label || '').trim();
    const explicitLines = text.split(/\n+/).map(line => line.trim()).filter(Boolean);
    let suffixLine = null;
    let base = text;

    if (explicitLines.length > 1 && /^\d+$/.test(explicitLines[explicitLines.length - 1])) {
      suffixLine = explicitLines.pop();
      base = explicitLines.join(' ');
    } else {
      const m = text.match(/^(.+?)\s+(\d{4})$/);
      if (m) {
        base = m[1];
        suffixLine = m[2];
      }
    }

    if (!suffixLine) return limitLabelLines(wrapLabelLine(base, NODE_LABEL_MAX_LINE_CHARS)).join('\n');

    const bodyLines = wrapLabelLine(base, NODE_LABEL_MAX_LINE_CHARS);
    const limitedBody = limitLabelLines(bodyLines, NODE_LABEL_MAX_LINES - 1);
    return limitedBody.concat(suffixLine).join('\n');
  }

  function paperSuperCategory(attrs) {
    if (isUncategorizedCategory(attrs.category)) return UNCATEGORIZED_CATEGORY;
    return attrs.super_category ||
      categorySuperCategory(attrs.category) ||
      attrs.category ||
      UNCATEGORIZED_CATEGORY;
  }

  const mapModel = window.kbBrowserMapModel.createBrowserMapModel(DATA, {
    scriptUrl: MAP_SCRIPT_URL,
    helpers: paperDerivations,
    hierarchyLevels: HIERARCHY_LEVELS,
    navPathOrderIndex,
    categoryOrder,
    superCategoryOrder,
    groupId,
    branchColorForPath,
    paperSuperCategory,
    uncategorizedCategory: UNCATEGORIZED_CATEGORY,
    aggregatePositionBiasByLevel: AGGREGATE_POSITION_BIAS_BY_LEVEL,
    aggregatePositionOuterQuantile: AGGREGATE_POSITION_OUTER_QUANTILE,
    onSimilarityRowsLoaded: () => {
      relevanceEvaluationCache = null;
      if (relevanceFilterActive()) refreshView();
    },
  });

  function defaultTreeProximity() {
    return DEFAULT_RELEVANCE_TREE_PROXIMITY;
  }

  function relevanceSliderPositionToThreshold(position) {
    const clamped = clamp(Number(position) || 0, 0, 1);
    return 1 - Math.pow(1 - clamped, RELEVANCE_SLIDER_EXPONENT);
  }

  function relevanceThresholdToSliderPosition(threshold) {
    const clamped = clamp(Number(threshold) || 0, 0, 1);
    if (clamped >= 1) return 1;
    return 1 - Math.pow(1 - clamped, 1 / RELEVANCE_SLIDER_EXPONENT);
  }

  function relevanceThresholdToSliderValue(threshold) {
    return String(Math.round(relevanceThresholdToSliderPosition(threshold) * 100));
  }

  function relevanceSliderValueToThreshold(value) {
    return relevanceSliderPositionToThreshold(parseInt(value, 10) / 100);
  }

  function relevanceSliderValueLabel(value) {
    return (parseInt(value, 10) / 100).toFixed(2);
  }

  function selectedRelevanceEgo() {
    const paperId = paperIdForNode(viewState.pinnedNode);
    return paperId && mapModel.paper(paperId) ? paperId : null;
  }

  function relevanceFilterActive() {
    return viewState.relevanceFilter.enabled && Boolean(selectedRelevanceEgo());
  }

  function setSelectedNodeFilterEnabled(enabled) {
    const nextEnabled = Boolean(enabled);
    if (viewState.relevanceFilter.enabled === nextEnabled) return;

    viewState.relevanceFilter.enabled = nextEnabled;
    syncRelevanceControlValues();
  }

  function relevanceTreeThreshold() {
    return Number.isFinite(viewState.relevanceFilter.treeProximity)
      ? viewState.relevanceFilter.treeProximity
      : defaultTreeProximity();
  }

  function relevanceEvaluationKey(egoId, treeThreshold) {
    if (!viewState.relevanceFilter.enabled || !egoId) return 'off';

    return [
      egoId,
      viewState.relevanceFilter.semantic ? 1 : 0,
      viewState.relevanceFilter.taxonomy ? 1 : 0,
      viewState.relevanceFilter.mode,
      viewState.relevanceFilter.similarity,
      treeThreshold,
    ].join('|');
  }

  function relevanceMetricsForEgo(egoId) {
    return mapModel.relevanceMetrics(egoId);
  }

  function metricAllowedByRelevance(metric, egoId, treeThreshold) {
    if (metric.paperId === egoId) return true;

    const semanticEnabled = viewState.relevanceFilter.semantic;
    const taxonomyEnabled = viewState.relevanceFilter.taxonomy;
    if (!semanticEnabled && !taxonomyEnabled) return true;

    const semanticPass = !semanticEnabled || metric.semantic >= viewState.relevanceFilter.similarity;
    const taxonomyPass = !taxonomyEnabled || metric.treeProximity >= treeThreshold;

    return viewState.relevanceFilter.mode === 'or'
      ? semanticPass || taxonomyPass
      : semanticPass && taxonomyPass;
  }

  function relevanceEvaluation() {
    const egoId = selectedRelevanceEgo();
    if (!viewState.relevanceFilter.enabled || !egoId) {
      return {
        active: false,
        allowedPaperIds: null,
        count: DATA.nodes.length,
      };
    }

    const treeThreshold = relevanceTreeThreshold();
    const key = relevanceEvaluationKey(egoId, treeThreshold);
    if (relevanceEvaluationCache && relevanceEvaluationCache.key === key) {
      return relevanceEvaluationCache;
    }

    const allowedPaperIds = new Set();
    relevanceMetricsForEgo(egoId).forEach(metric => {
      if (metricAllowedByRelevance(metric, egoId, treeThreshold)) {
        allowedPaperIds.add(metric.paperId);
      }
    });

    relevanceEvaluationCache = {
      key,
      active: true,
      allowedPaperIds,
      count: allowedPaperIds.size,
    };
    return relevanceEvaluationCache;
  }

  function paperAllowedByRelevance(paperId) {
    const evaluation = relevanceEvaluation();
    return !evaluation.active || evaluation.allowedPaperIds.has(paperId);
  }

  function paperAllowedByCurrentFilters(attrs) {
    if (!attrs || !paperAllowedByRelevance(attrs.id)) return false;
    return viewState.activeCategories.has(mapModel.nodeKey(attrs));
  }

  function nodeAllowedByRelevance(attrs) {
    if (!relevanceFilterActive()) return true;
    const evaluation = relevanceEvaluation();
    if (!evaluation.active) return true;

    if (attrs.kind === 'aggregate') {
      return (attrs.leafIds || []).some(paperId => evaluation.allowedPaperIds.has(paperId));
    }
    return evaluation.allowedPaperIds.has(attrs.id);
  }

  function visiblePaperPathsForColoring() {
    const paperIds = new Set();

    if (!graph || !viewState.visibleNodes) return [];

    viewState.visibleNodes.forEach(node => {
      const attrs = graph.getNodeAttributes(node);
      if (attrs.kind === 'paper') {
        if (paperAllowedByCurrentFilters(attrs)) paperIds.add(attrs.id);
        return;
      }

      (attrs.leafIds || []).forEach(paperId => {
        const paper = mapModel.paper(paperId);
        if (paperAllowedByCurrentFilters(paper)) paperIds.add(paperId);
      });
    });

    return [...paperIds]
      .map(paperId => mapModel.paper(paperId))
      .filter(Boolean)
      .map(attrs => mapModel.paperPath(attrs));
  }

  function commonPathPrefix(paths) {
    if (!paths.length) return [];

    const prefix = [];
    const limit = Math.min(...paths.map(path => path.length));
    for (let i = 0; i < limit; i += 1) {
      const value = paths[0][i];
      if (!paths.every(path => path[i] === value)) break;
      prefix.push(value);
    }
    return prefix;
  }

  function pathBranchLabel(path, depth) {
    if (!path || !path.length) return UNCATEGORIZED_CATEGORY;
    if (depth < path.length) return path[depth] || UNCATEGORIZED_CATEGORY;
    return path[path.length - 1] || UNCATEGORIZED_CATEGORY;
  }

  function branchOrder(path) {
    const key = (path || []).join('::');
    return navPathOrderIndex.has(key)
      ? navPathOrderIndex.get(key)
      : Number.MAX_SAFE_INTEGER;
  }

  function orderedVisibleBranchLabels(paths, depth, prefix) {
    const branches = new Map();

    paths.forEach(path => {
      const label = pathBranchLabel(path, depth);
      if (!label) return;

      const branchPath = depth < path.length
        ? path.slice(0, depth + 1)
        : (prefix || []).concat(label);
      const order = branchOrder(branchPath);
      const existing = branches.get(label);
      if (!existing || order < existing.order) {
        branches.set(label, { label, order });
      }
    });

    return [...branches.values()]
      .sort((a, b) => a.order - b.order || a.label.localeCompare(b.label))
      .map(branch => branch.label);
  }

  function pathStartsWith(path, prefix) {
    return prefix.every((part, index) => path[index] === part);
  }

  function stableBranchLabelsForParent(depth, parentPrefix) {
    const cacheKey = `${depth}:${(parentPrefix || []).join('::')}`;
    if (stableBranchLabelCache.has(cacheKey)) {
      return stableBranchLabelCache.get(cacheKey).slice();
    }

    const branches = new Map();

    function addPath(path, orderHint = Number.MAX_SAFE_INTEGER) {
      if (!Array.isArray(path) || path.length <= depth) return;
      if (!pathStartsWith(path, parentPrefix)) return;

      const label = pathBranchLabel(path, depth);
      if (!label) return;

      const branchPath = path.slice(0, depth + 1);
      const order = Math.min(branchOrder(branchPath), orderHint);
      const existing = branches.get(label);
      if (!existing || order < existing.order) {
        branches.set(label, { label, order });
      }
    }

    NAV_PATH_ORDER.forEach((path, index) => addPath(path, index));
    DATA.nodes.forEach(node => addPath(mapModel.paperPath(node.data || {})));

    const labels = [...branches.values()]
      .sort((a, b) => a.order - b.order || a.label.localeCompare(b.label))
      .map(branch => branch.label);
    stableBranchLabelCache.set(cacheKey, labels);
    return labels.slice();
  }

  function orderedStableBranchLabels(paths, depth, prefix) {
    const parentPrefix = (prefix || []).slice(0, depth);
    const visibleLabels = new Set(orderedVisibleBranchLabels(paths, depth, prefix));
    const labels = stableBranchLabelsForParent(depth, parentPrefix);

    visibleLabels.forEach(label => {
      if (!labels.includes(label)) labels.push(label);
    });

    return labels;
  }

  function stableColorForPath(rawPath, preferredDepth = null) {
    const path = (Array.isArray(rawPath) ? rawPath : [])
      .map(part => String(part || '').trim())
      .filter(Boolean);
    if (!path.length) return '#000000';

    const category = path[1] || path[0];
    if (isUncategorizedCategory(category)) return '#000000';

    const maxDepth = path.length - 1;
    const depth = Number.isFinite(preferredDepth)
      ? clamp(Math.floor(preferredDepth), 0, maxDepth)
      : maxDepth;
    const labels = orderedStableBranchLabels([path], depth, path.slice(0, depth));
    const label = pathBranchLabel(path, depth);
    const index = Math.max(labels.indexOf(label), 0);
    const palette = currentVisibilityPalette();

    return palette[index % palette.length];
  }

  function visibilityColorDepth(paths, commonPrefix) {
    const maxDepth = Math.max(0, ...paths.map(path => path.length));

    for (let depth = commonPrefix.length; depth < maxDepth; depth += 1) {
      if (orderedVisibleBranchLabels(paths, depth, commonPrefix).length > 1) {
        return depth;
      }
    }

    return Math.max(0, Math.min(commonPrefix.length, maxDepth) - 1);
  }

  function buildVisibilityColorContext() {
    const paths = visiblePaperPathsForColoring();
    if (!paths.length) {
      return {
        depth: 0,
        prefix: [],
        colorByLabel: new Map(),
      };
    }

    const prefix = commonPathPrefix(paths);
    const depth = visibilityColorDepth(paths, prefix);
    const labels = orderedStableBranchLabels(paths, depth, prefix);
    const colorByLabel = new Map();
    const palette = currentVisibilityPalette();

    labels.forEach((label, index) => {
      colorByLabel.set(label, palette[index % palette.length]);
    });

    return { depth, prefix, colorByLabel };
  }

  function nodePathForColor(attrs) {
    return mapModel.paperPath(attrs);
  }

  function fallbackNodeColor(attrs) {
    return stableColorForPath(nodePathForColor(attrs));
  }

  function visibilityColorForNode(attrs) {
    const path = nodePathForColor(attrs);
    const category = path[1] || attrs.category || path[0];
    if (isUncategorizedCategory(category)) return '#000000';
    if (!visibilityColorContext) return fallbackNodeColor(attrs);

    const label = pathBranchLabel(path, visibilityColorContext.depth);
    return visibilityColorContext.colorByLabel.get(label) ||
      stableColorForPath(path, visibilityColorContext.depth);
  }

  function recomputeVisibilityColors() {
    if (!graph) return;

    visibilityColorContext = buildVisibilityColorContext();
    graph.forEachNode((node, attrs) => {
      const color = visibilityColorForNode(attrs);
      graph.setNodeAttribute(node, 'baseColor', color);
      graph.setNodeAttribute(node, 'color', color);
      graph.setNodeAttribute(node, 'labelOutlineColor', color);
    });
  }

  function branchColorForPath(path, index) {
    return stableColorForPath(path, index);
  }

  function groupId(level, parts) {
    return `agg:${level}:${parts.map(part => String(part || UNCATEGORIZED_CATEGORY)).join('::')}`;
  }

  function nodeAllowedByFilters(attrs) {
    if (!nodeAllowedByRelevance(attrs)) return false;
    return nodeAllowedByBaseFilters(attrs);
  }

  function nodeAllowedByBaseFilters(attrs) {
    const filterKeys = attrs.filterKeys || [mapModel.nodeKey(attrs)];
    return filterKeys.some(key => viewState.activeCategories.has(key));
  }

  function nodeVisibleAt(node, level, options = {}) {
    const attrs = graph.getNodeAttributes(node);
    const allowed = options.ignoreRelevance
      ? nodeAllowedByBaseFilters(attrs)
      : nodeAllowedByFilters(attrs);
    if (!allowed) return false;

    const baseIndex = DETAIL_LEVELS.indexOf(level);
    const nodeIndex = DETAIL_LEVELS.indexOf(attrs.detailLevel);
    return baseIndex >= 0 && nodeIndex === baseIndex;
  }

  function nodeVisible(node) {
    return viewState.visibleNodes ? viewState.visibleNodes.has(node) : nodeVisibleAt(node, viewState.currentDetailLevel);
  }

  function nodeGhostVisible(node) {
    return relevanceFilterActive() &&
      !nodeVisible(node) &&
      nodeVisibleAt(node, viewState.currentDetailLevel, { ignoreRelevance: true });
  }

  function escHtml(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  /* -------------------------------------------------------------------------
   * Build the Graphology graph. Sigma renders directly from node attrs.
   * -------------------------------------------------------------------------*/
  function buildGraph() {
    const g = window.graphology.UndirectedGraph ?
      new window.graphology.UndirectedGraph() :
      new window.graphology.Graph({ type: 'undirected' });
    const hierarchy = mapModel.hierarchy();
    const nodeSpecs = DATA.nodes.concat(hierarchy.nodes).map(n => {
      const attrs = n.data;
      const kind = attrs.kind || 'paper';
      const detailLevel = attrs.detailLevel || 'paper';
      const staticSize = kind === 'aggregate'
        ? aggregateNodeSize(attrs.count, detailLevel)
        : null;

      return {
        raw: n,
        attrs,
        kind,
        detailLevel,
        staticSize,
        baseSize: kind === 'aggregate' ? staticSize : PAPER_NODE_RADIUS_TARGET,
      };
    });
    const labelMetricsByLevel = precomputeNodeLabelMetrics(nodeSpecs);

    nodeSpecs.forEach(spec => {
      const { raw: n, attrs, kind, detailLevel, staticSize } = spec;
      const color = attrs.color || stableColorForPath(mapModel.paperPath(attrs));
      const labelMetrics = labelMetricsByLevel.get(detailLevel) || {};
      const x = n.position.x;
      const y = n.position.y;
      const ancestorIds = attrs.ancestorIds || hierarchy.paperAncestors[attrs.id] || {};
      const parentId = attrs.parentId || ancestorIds[previousDetailLevel(detailLevel)] || null;
      g.addNode(attrs.id, {
        ...attrs,
        kind,
        detailLevel,
        item_type: mapModel.itemType(attrs),
        parentId,
        ancestorIds,
        filterKeys: attrs.filterKeys || [mapModel.nodeKey(attrs)],
        searchText: attrs.searchText || paperSearchText(attrs),
        x,
        y,
        homeX: x,
        homeY: y,
        staticSize,
        size: kind === 'aggregate' ? staticSize : currentNodeRadius(),
        type: borderedNodeProgramSupported() ? BORDERED_NODE_TYPE : 'circle',
        color,
        borderColor: theme.nodeBorder,
        baseColor: color,
        staticBaseColor: color,
        label: formatLabel(attrs.label),
        fullLabel: attrs.fullLabel || attrs.label,
        labelFontSize: labelMetrics.fontSize || NODE_LABEL_FONT_SIZE,
        labelLineHeight: labelMetrics.lineHeight || (NODE_LABEL_FONT_SIZE * NODE_LABEL_LINE_HEIGHT_RATIO),
        labelSourceDiskDiameter: labelMetrics.sourceDiskDiameter || (PAPER_NODE_RADIUS_TARGET * 2),
        count: attrs.count || 1,
        labelColor: accessibleNodeLabelColor(color),
        labelOutlineColor: color,
        forceLabel: false,
      });
    });

    return g;
  }

  /* -------------------------------------------------------------------------
   * Sigma reducers: apply filtering, dimming and highlights at render time.
   * -------------------------------------------------------------------------*/
  function nodeReducer(node, attrs) {
    if (!nodeVisible(node)) {
      if (nodeGhostVisible(node)) {
        const size = nodeSizeWithMinimumScreenRadius(nodeDisplaySize(attrs)) * 0.72;
        return {
          ...attrs,
          label: '',
          size,
          color: theme.nodeGhost,
          borderColor: theme.nodeGhost,
          labelColor: theme.nodeGhostBorder,
          labelOutlineColor: theme.nodeGhost,
          highlighted: false,
          forceLabel: false,
          ghosted: true,
          zIndex: Math.max(0, detailLevelZIndex(attrs.detailLevel) - 8),
        };
      }

      return { ...attrs, hidden: true };
    }

    const size = nodeSizeWithMinimumScreenRadius(nodeDisplaySize(attrs));
    const baseZIndex = detailLevelZIndex(attrs.detailLevel);
    const highlighted = viewState.focus.nodes.has(node);
    const primaryFocus = highlighted && (
      node === viewState.pinnedNode ||
      node === viewState.hoveredNode
    );
    const muted = viewState.focus.active && viewState.focus.mode !== 'hover' && !primaryFocus;
    const focusLabel = node === viewState.pinnedNode || node === viewState.hoveredNode;
    const forceLabel = focusLabel;
    const label = (viewState.showNodeLabels || focusLabel) ? attrs.label : '';

    if (muted) {
      const mutedColor = highlighted ? theme.nodeMutedRelated : theme.nodeMuted;
      return {
        ...attrs,
        label,
        size,
        color: mutedColor,
        borderColor: theme.nodeBorder,
        labelColor: accessibleNodeLabelColor(mutedColor),
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
        borderColor: theme.nodeBorder,
        labelColor: accessibleNodeLabelColor(attrs.baseColor),
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
      borderColor: theme.nodeBorder,
      labelColor: accessibleNodeLabelColor(attrs.baseColor),
      labelOutlineColor: attrs.baseColor,
      highlighted: false,
      forceLabel,
      zIndex: baseZIndex,
    };
  }

  function drawNodeHover(context, data) {
    if (data.ghosted) return;

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
    const { fontSize, lineHeight, outlineWidth } = currentNodeLabelMetrics(data, data.labelZoomScale);
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

  function drawNodeLabelNoop() {
    // Sigma still runs its label-grid selection; the top overlay does the draw.
  }

  function drawGhostNodeDashedBorder(context, data) {
    const lineWidth = Math.max(1, data.size * NODE_BORDER_WIDTH_RATIO);
    const radius = Math.max(1, data.size - lineWidth / 2);

    context.save();
    context.beginPath();
    context.arc(data.x, data.y, radius, 0, Math.PI * 2);
    context.setLineDash([Math.max(2, lineWidth * 2.4), Math.max(2, lineWidth * 1.7)]);
    context.lineWidth = lineWidth;
    context.strokeStyle = theme.nodeGhostBorder;
    context.globalAlpha = theme.colorScheme === 'dark' ? 0.58 : 0.72;
    context.stroke();
    context.restore();
  }

  function borderedNodeProgramSupported() {
    return Boolean(
      window.Sigma &&
      window.Sigma.rendering &&
      typeof window.Sigma.rendering.createNodeBorderProgram === 'function'
    );
  }

  function nodeProgramClasses() {
    if (!borderedNodeProgramSupported()) return {};

    return {
      [BORDERED_NODE_TYPE]: window.Sigma.rendering.createNodeBorderProgram({
        borders: [
          {
            size: { value: NODE_BORDER_WIDTH_RATIO },
            color: { attribute: 'borderColor', defaultValue: theme.nodeBorder },
          },
          {
            size: { fill: true },
            color: { attribute: 'color' },
          },
        ],
        drawHover: drawNodeHover,
        drawLabel: drawNodeLabelNoop,
      }),
    };
  }

  function setupTopLabelOverlay() {
    if (!renderer || typeof renderer.createCanvasContext !== 'function') return;

    try {
      renderer.createCanvasContext('topLabels', {
        afterLayer: 'hoverNodes',
        style: { pointerEvents: 'none' },
      });
      renderer.resize(true);

      const canvases = typeof renderer.getCanvases === 'function'
        ? renderer.getCanvases()
        : {};
      topLabelContext = canvases.topLabels
        ? canvases.topLabels.getContext('2d')
        : null;
    } catch (err) {
      topLabelContext = null;
      if (window.console && console.warn) console.warn('Could not create top label overlay:', err);
    }

    if (topLabelContext) {
      renderer.on('afterRender', drawTopLabelOverlay);
    }
  }

  function clearTopLabelOverlay() {
    if (!topLabelContext || !renderer) return;

    const dims = renderer.getDimensions();
    topLabelContext.clearRect(0, 0, dims.width, dims.height);
  }

  function topLabelOverlayNodes() {
    if (!renderer || !graph) return [];
    if (typeof renderer.getNodeDisplayedLabels !== 'function') return [];

    const nodes = [...renderer.getNodeDisplayedLabels()];
    return nodes
      .filter(node => {
        if (!nodeVisible(node)) return false;

        const display = typeof renderer.getNodeDisplayData === 'function'
          ? renderer.getNodeDisplayData(node)
          : null;
        return Boolean(display && !display.hidden && display.label);
      })
      .map(node => {
        const display = renderer.getNodeDisplayData(node);
        return { node, zIndex: Number(display.zIndex) || 0 };
      })
      .sort((a, b) => a.zIndex - b.zIndex)
      .map(item => item.node);
  }

  function drawTopLabelOverlay() {
    if (!topLabelContext || !renderer || !graph) return;

    clearTopLabelOverlay();
    const labelZoomScale = currentNodeLabelZoomScale();
    graph.forEachNode(node => {
      if (!nodeGhostVisible(node)) return;

      const attrs = graph.getNodeAttributes(node);
      const display = renderer.getNodeDisplayData(node);
      if (!display || display.hidden) return;

      const point = renderer.graphToViewport({ x: attrs.x, y: attrs.y });
      const size = typeof renderer.scaleSize === 'function'
        ? renderer.scaleSize(display.size)
        : display.size;

      drawGhostNodeDashedBorder(topLabelContext, {
        ...display,
        x: point.x,
        y: point.y,
        size,
      });
    });

    topLabelOverlayNodes().forEach(node => {
      const attrs = graph.getNodeAttributes(node);
      const display = renderer.getNodeDisplayData(node);
      if (!display || display.hidden || !display.label) return;

      const point = renderer.graphToViewport({ x: attrs.x, y: attrs.y });
      const size = typeof renderer.scaleSize === 'function'
        ? renderer.scaleSize(display.size)
        : display.size;

      drawNodeLabel(topLabelContext, {
        ...display,
        x: point.x,
        y: point.y,
        size,
        labelZoomScale,
      });
    });
  }

  /* -------------------------------------------------------------------------
   * Focus helpers
   * -------------------------------------------------------------------------*/
  function setNeighborhoodFocus(node, mode) {
    const nodes = new Set([node]);
    viewState.setFocus(nodes, mode);
  }

  function recomputeVisibleNodes() {
    const nodes = new Set();
    const list = [];

    if (!graph) {
      viewState.setVisibleNodes(nodes, list);
      return;
    }

    graph.forEachNode((node, attrs) => {
      if (!nodeVisibleAt(node, viewState.currentDetailLevel)) return;
      nodes.add(node);
      list.push(node);
    });

    viewState.setVisibleNodes(nodes, list);
  }

  function recomputeFocus() {
    if (viewState.pinnedNode) {
      setNeighborhoodFocus(viewState.pinnedNode, 'pinned');
    } else if (viewState.hoveredNode) {
      setNeighborhoodFocus(viewState.hoveredNode, 'hover');
    } else {
      viewState.clearFocus();
    }
  }

  function refreshView() {
    if (interactionRefreshFrame !== null) {
      window.cancelAnimationFrame(interactionRefreshFrame);
      interactionRefreshFrame = null;
    }
    recomputeVisibleNodes();
    cachedPaperNodeRadius = paperNodeRadiusForCurrentView();
    recomputeVisibilityColors();
    recomputeFocus();
    if (renderer) renderer.scheduleRefresh();
    updateRelevancePanel();
    updateZoomOutLimit();
  }

  function refreshInteractionFocus() {
    recomputeFocus();
    if (!renderer || interactionRefreshFrame !== null) return;
    interactionRefreshFrame = window.requestAnimationFrame(() => {
      interactionRefreshFrame = null;
      if (renderer) renderer.scheduleRefresh();
    });
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

  function clearHoverClickNode(node = null) {
    if (!node || viewState.hoverClickNode === node) viewState.hoverClickNode = null;
  }

  function visibleNodeIds() {
    if (viewState.visibleNodes) return viewState.visibleNodeList.filter(node => graphHasNode(node));

    const nodes = [];
    if (!graph) return nodes;
    graph.forEachNode(node => {
      if (nodeVisible(node)) nodes.push(node);
    });
    return nodes;
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

  function rollUpOriginMap(targetLevel, previousLevel) {
    const origins = new Map();

    graph.forEachNode((node, attrs) => {
      if (attrs.detailLevel !== previousLevel || !nodeAllowedByFilters(attrs)) return;
      const targetNode = attrs.ancestorIds && attrs.ancestorIds[targetLevel];
      if (!targetNode) return;

      const point = nodePoint(node);
      const origin = origins.get(targetNode) || { x: 0, y: 0, count: 0 };
      origin.x += point.x;
      origin.y += point.y;
      origin.count += 1;
      origins.set(targetNode, origin);
    });

    origins.forEach((origin, node) => {
      origins.set(node, {
        x: origin.x / origin.count,
        y: origin.y / origin.count,
      });
    });

    return origins;
  }

  function prepareLevelTransition(previousLevel, nextLevel) {
    const direction = detailLevelDirection(previousLevel, nextLevel);
    const nodes = [];
    const cameraState = transitionCameraState();
    const rollUpOrigins = direction < 0 ? rollUpOriginMap(nextLevel, previousLevel) : null;
    let maxScreenTravel = 0;

    graph.forEachNode((node, attrs) => {
      if (attrs.detailLevel !== nextLevel || !nodeAllowedByFilters(attrs)) return;

      const to = homePoint(attrs);
      let from = null;

      if (direction > 0) {
        from = transitionOriginForDrillDown(attrs, previousLevel, to, cameraState);
      } else if (direction < 0) {
        from = rollUpOrigins.get(node) || homePoint(attrs);
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
        minCameraRatio: MIN_CAMERA_RATIO,
        maxCameraRatio: FALLBACK_MAX_CAMERA_RATIO,
        zIndex: true,
        hideLabelsOnMove: false,
        renderLabels: true,
        enableCameraRotation: false,
        labelRenderedSizeThreshold: LABEL_RENDERED_SIZE_THRESHOLD,
        labelDensity: LABEL_DENSITY,
        labelGridCellSize: LABEL_GRID_CELL_SIZE,
        labelFont: '"Atkinson Hyperlegible Next", "Segoe UI", sans-serif',
        labelSize: NODE_LABEL_FONT_SIZE,
        itemSizesReference: 'positions',
        zoomToSizeRatioFunction: ratio => Math.max(ratio, 1e-6),
        stagePadding: 30,
        nodeProgramClasses: nodeProgramClasses(),
        nodeReducer,
        defaultDrawNodeLabel: drawNodeLabelNoop,
        defaultDrawNodeHover: drawNodeHover,
      });
    } catch (err) {
      const rawMessage = err && err.message ? err.message : String(err);
      const message = rawMessage.includes('blendFunc')
        ? 'WebGL is unavailable or disabled in this browser.'
        : rawMessage;
      if (window.console && console.error) console.error('Map viewer failed to initialise:', err);
      graphContainer.innerHTML =
        `<p style="padding:2em;color:#ccc">Map viewer failed to initialise: ${escHtml(message)}</p>`;
      hideLoading();
      return;
    }

    setupTopLabelOverlay();
    renderer.on('afterRender', updateActiveTooltipPositions);
    hideLoading();
    setupGraphEvents();
    setupGraphDomEvents();
    setupCameraEvents();
    refreshView();
    window.setTimeout(() => {
      if (!focusPaperFromHash()) fitVisible(0);
    }, 0);
  }

  function setupCameraEvents() {
    const camera = renderer && typeof renderer.getCamera === 'function'
      ? renderer.getCamera()
      : null;
    if (camera && typeof camera.on === 'function') {
      camera.on('updated', () => {
        const state = typeof camera.getState === 'function' ? camera.getState() : null;
        const ratio = state && Number(state.ratio);
        const ratioChanged = Number.isFinite(ratio) && (
          lastCameraRenderRatio === null ||
          Math.abs(ratio - lastCameraRenderRatio) > 1e-5
        );

        updateActiveTooltipPositions();
        if (!ratioChanged) return;

        lastCameraRenderRatio = ratio;
        graphToViewportRatioCache = null;
        if (renderer) renderer.scheduleRefresh();
      });
    }
  }

  function setupGraphEvents() {
    renderer.on('enterNode', payload => {
      if (!nodeVisible(payload.node)) {
        clearHoverClickNode();
        hideHoverTooltip();
        if (!viewState.pinnedNode && viewState.hoveredNode) {
          viewState.hoveredNode = null;
          hideTooltip();
          refreshInteractionFocus();
        }
        return;
      }

      viewState.hoverClickNode = payload.node;
      if (viewState.pinnedNode) {
        if (payload.node !== viewState.pinnedNode) showHoverTooltip(payload.node);
        return;
      }
      viewState.hoveredNode = payload.node;
      if (graph.getNodeAttribute(payload.node, 'kind') === 'paper') {
        hideTooltip();
        showHoverTooltip(payload.node);
      } else {
        hideHoverTooltip();
        showNodeTooltip(payload.node, nodeTooltipPosition(payload.node) || eventPosition(payload), false);
      }
      refreshInteractionFocus();
    });

    renderer.on('leaveNode', () => {
      clearHoverClickNode();
      if (viewState.pinnedNode) {
        hideHoverTooltip();
        return;
      }
      viewState.hoveredNode = null;
      hideHoverTooltip();
      hideTooltip();
      refreshInteractionFocus();
    });

    renderer.on('clickNode', payload => {
      if (suppressGraphClickAfterPan()) return;

      const node = clickTargetNode(payload);
      if (!node) return;

      activateNode(node, payload);
    });

    renderer.on('clickStage', payload => {
      if (suppressGraphClickAfterPan()) return;

      const node = clickTargetNode(payload);
      if (node) {
        activateNode(node, payload);
        return;
      }

      clearGraphSelection();
    });
  }

  function setupGraphDomEvents() {
    if (window.PointerEvent) {
      graphContainer.addEventListener('pointerdown', handleGraphPointerStart, true);
      graphContainer.addEventListener('pointermove', handleGraphPointerMove, true);
      graphContainer.addEventListener('pointerup', handleGraphPointerEnd, true);
      graphContainer.addEventListener('pointercancel', clearGraphPanGesture, true);
      window.addEventListener('pointermove', handleGraphPointerMove, true);
      window.addEventListener('pointerup', handleGraphPointerEnd, true);
      window.addEventListener('pointercancel', clearGraphPanGesture, true);
    } else {
      graphContainer.addEventListener('mousedown', handleGraphMouseStart, true);
      graphContainer.addEventListener('mousemove', handleGraphPointerMove, true);
      graphContainer.addEventListener('mouseup', handleGraphPointerEnd, true);
      graphContainer.addEventListener('touchstart', handleGraphTouchStart, { capture: true, passive: true });
      graphContainer.addEventListener('touchmove', handleGraphTouchMove, { capture: true, passive: true });
      graphContainer.addEventListener('touchend', handleGraphTouchEnd, true);
      graphContainer.addEventListener('touchcancel', clearGraphPanGesture, true);
      window.addEventListener('mousemove', handleGraphPointerMove, true);
      window.addEventListener('mouseup', handleGraphPointerEnd, true);
      window.addEventListener('touchmove', handleGraphTouchMove, { capture: true, passive: true });
      window.addEventListener('touchend', handleGraphTouchEnd, true);
      window.addEventListener('touchcancel', clearGraphPanGesture, true);
    }

    graphContainer.addEventListener('click', event => {
      if (!renderer || !graph || event.defaultPrevented || event.button !== 0) return;

      if (suppressGraphClickAfterPan()) {
        event.preventDefault();
        event.stopImmediatePropagation();
        return;
      }

      const pos = domEventPosition(event);
      const node = clickTargetNode({ event: pos });

      event.preventDefault();
      event.stopImmediatePropagation();

      if (node) {
        activateNode(node, { event: pos });
      } else {
        clearGraphSelection();
      }
    }, true);
  }

  function startGraphPanGesture(event, point) {
    if (!point) return;
    if (event && 'button' in event && event.button !== 0) return;
    if (event && 'isPrimary' in event && event.isPrimary === false) return;

    blurActiveTextInputForGraphGesture();

    graphPanGesture = {
      pointerId: event && 'pointerId' in event ? event.pointerId : null,
      startX: point.clientX,
      startY: point.clientY,
      moved: false,
    };
  }

  function updateGraphPanGesture(event, point) {
    if (!graphPanGesture || !point) return;
    if (
      event &&
      graphPanGesture.pointerId !== null &&
      'pointerId' in event &&
      event.pointerId !== graphPanGesture.pointerId
    ) {
      return;
    }

    const dx = point.clientX - graphPanGesture.startX;
    const dy = point.clientY - graphPanGesture.startY;
    if (Math.sqrt(dx * dx + dy * dy) >= PAN_CLICK_DRAG_THRESHOLD) {
      graphPanGesture.moved = true;
    }
  }

  function endGraphPanGesture(event, point) {
    updateGraphPanGesture(event, point);
    if (graphPanGesture && graphPanGesture.moved) {
      suppressGraphClickUntil = Date.now() + PAN_CLICK_SUPPRESS_MS;
    }
    clearGraphPanGesture();
  }

  function clearGraphPanGesture() {
    graphPanGesture = null;
  }

  function suppressGraphClickAfterPan() {
    return Date.now() < suppressGraphClickUntil;
  }

  function blurActiveTextInputForGraphGesture() {
    const active = document.activeElement;
    if (!active || active === document.body || active === document.documentElement) return;
    if (typeof active.matches !== 'function' || typeof active.blur !== 'function') return;

    const editableSelector = [
      'input[type="email"]',
      'input[type="number"]',
      'input[type="password"]',
      'input[type="search"]',
      'input[type="tel"]',
      'input[type="text"]',
      'input[type="url"]',
      'input:not([type])',
      'textarea',
      '[contenteditable=""]',
      '[contenteditable="true"]',
    ].join(',');

    if (!active.matches(editableSelector)) return;
    if (active.disabled || active.readOnly) return;
    active.blur();
  }

  function eventClientPoint(event) {
    if (!event) return null;
    if (Number.isFinite(event.clientX) && Number.isFinite(event.clientY)) {
      return { clientX: event.clientX, clientY: event.clientY };
    }
    return null;
  }

  function touchClientPoint(event) {
    const touch = event && event.changedTouches && event.changedTouches[0];
    if (!touch) return null;
    return { clientX: touch.clientX, clientY: touch.clientY };
  }

  function handleGraphPointerStart(event) {
    startGraphPanGesture(event, eventClientPoint(event));
  }

  function handleGraphMouseStart(event) {
    startGraphPanGesture(event, eventClientPoint(event));
  }

  function handleGraphTouchStart(event) {
    const touch = event && event.touches && event.touches[0];
    startGraphPanGesture(event, touch ? { clientX: touch.clientX, clientY: touch.clientY } : null);
  }

  function handleGraphPointerMove(event) {
    updateGraphPanGesture(event, eventClientPoint(event));
  }

  function handleGraphTouchMove(event) {
    const touch = event && event.touches && event.touches[0];
    updateGraphPanGesture(event, touch ? { clientX: touch.clientX, clientY: touch.clientY } : null);
  }

  function handleGraphPointerEnd(event) {
    endGraphPanGesture(event, eventClientPoint(event));
  }

  function handleGraphTouchEnd(event) {
    endGraphPanGesture(event, touchClientPoint(event));
  }

  function activateNode(node, payload) {
    const attrs = graph.getNodeAttributes(node);

    if (attrs.kind === 'aggregate') {
      activateBranchNode(attrs, node);
      return;
    }

    if (viewState.pinnedNode === node) {
      viewState.clearSelection();
      setSelectedNodeFilterEnabled(false);
      hideHoverTooltip();
      hideTooltip();
      hidePaperModal();
    } else {
      viewState.selectNode(node);
      setSelectedNodeFilterEnabled(attrs.kind === 'paper');
      hideHoverTooltip();
      showNodeTooltip(node, nodeTooltipPosition(node) || eventPosition(payload), true);
    }
    syncUrlToPinnedNode();
    refreshView();
  }

  function clearGraphSelection() {
    viewState.clearSelection();
    setSelectedNodeFilterEnabled(false);
    clearHoverClickNode();
    hideHoverTooltip();
    hideTooltip();
    hidePaperModal();
    syncUrlToPinnedNode();
    refreshView();
  }

  function eventPosition(payload) {
    if (payload && payload.event) return { x: payload.event.x, y: payload.event.y };
    return { x: graphContainer.clientWidth / 2, y: graphContainer.clientHeight / 2 };
  }

  function domEventPosition(event) {
    const rect = graphContainer.getBoundingClientRect();
    return {
      x: event.clientX - rect.left,
      y: event.clientY - rect.top,
    };
  }

  function nodeScreenRadius(node) {
    if (!renderer || !graphHasNode(node)) return 0;

    const attrs = graph.getNodeAttributes(node);
    const display = typeof renderer.getNodeDisplayData === 'function'
      ? renderer.getNodeDisplayData(node)
      : null;
    const rawSize = display && Number.isFinite(display.size)
      ? display.size
      : nodeDisplaySize(attrs);

    return typeof renderer.scaleSize === 'function'
      ? renderer.scaleSize(rawSize)
      : rawSize;
  }

  function pointerLabelContext() {
    const labels = typeof renderer.getNodeDisplayedLabels === 'function'
      ? renderer.getNodeDisplayedLabels()
      : new Set();
    return {
      labels,
      index: null,
    };
  }

  function roughLabelHalfExtents(attrs) {
    const label = viewState.showNodeLabels ? attrs.label : '';
    if (!label) return { width: 0, height: 0 };

    const lines = String(label).split('\n');
    const maxChars = Math.max(0, ...lines.map(line => line.length));
    return {
      width: maxChars * 5.8 + 12,
      height: Math.max(1, lines.length) * 8 + 8,
    };
  }

  function pointerHitCandidateNodes(pos, labelContext) {
    const nodes = visibleNodeIds();
    if (nodes.length <= 320) return nodes;

    const candidates = [];
    nodes.forEach(node => {
      if (!graphHasNode(node)) return;

      const attrs = graph.getNodeAttributes(node);
      const point = renderer.graphToViewport({ x: attrs.x, y: attrs.y });
      const dx = pos.x - point.x;
      const dy = pos.y - point.y;
      const radius = Math.max(nodeScreenRadius(node), 6) + 18;
      const labelExtents = (labelContext.labels.has(node) || node === viewState.pinnedNode || node === viewState.hoveredNode)
        ? roughLabelHalfExtents(attrs)
        : { width: 0, height: 0 };
      const hitWidth = Math.max(radius, labelExtents.width);
      const hitHeight = Math.max(radius, labelExtents.height);

      if (Math.abs(dx) > hitWidth || Math.abs(dy) > hitHeight) return;
      candidates.push({
        node,
        distance: dx * dx + dy * dy,
      });
    });

    return candidates
      .sort((a, b) => a.distance - b.distance)
      .slice(0, 120)
      .map(candidate => candidate.node);
  }

  function nodePointerHit(node, pos, labelContext = null) {
    if (!renderer || !graphHasNode(node) || !nodeVisible(node) || !pos) return null;

    const attrs = graph.getNodeAttributes(node);
    const point = renderer.graphToViewport({ x: attrs.x, y: attrs.y });
    const dx = pos.x - point.x;
    const dy = pos.y - point.y;
    const radius = Math.max(nodeScreenRadius(node), 6) + 6;
    const distance = Math.sqrt(dx * dx + dy * dy);
    const diskHit = distance <= radius;
    const labelExtents = nodeLabelVisible(node, labelContext) ? labelTextHalfExtents(attrs) : { width: 0, height: 0 };
    const labelPad = 6;
    const labelWidth = labelExtents.width + labelPad;
    const labelHeight = labelExtents.height + labelPad;
    const labelHit = labelWidth > 0 &&
      Math.abs(dx) <= labelWidth &&
      Math.abs(dy) <= labelHeight;

    if (!diskHit && !labelHit) return null;

    const normalizedX = labelWidth > 0 ? Math.abs(dx) / labelWidth : Infinity;
    const normalizedY = labelHeight > 0 ? Math.abs(dy) / labelHeight : Infinity;

    return {
      node,
      attrs,
      distance,
      radius,
      diskHit,
      labelHit,
      labelPriority: labelHit ? nodeLabelDrawIndex(node, labelContext) : -1,
      distanceRatio: diskHit
        ? (radius ? distance / radius : Infinity)
        : Math.max(normalizedX, normalizedY) + 1,
      levelIndex: DETAIL_LEVELS.indexOf(attrs.detailLevel),
      screenSize: nodeScreenRadius(node),
    };
  }

  function nodeLabelVisible(node, labelContext = null) {
    if (!renderer || typeof renderer.getNodeDisplayData !== 'function') return false;

    const display = renderer.getNodeDisplayData(node);
    if (!display || !String(display.label || '').trim()) return false;
    if (display.forceLabel) return true;

    if (labelContext) return labelContext.labels.has(node);
    if (typeof renderer.getNodeDisplayedLabels !== 'function') return false;
    return renderer.getNodeDisplayedLabels().has(node);
  }

  function nodeLabelDrawIndex(node, labelContext = null) {
    if (labelContext) {
      if (!labelContext.index) {
        labelContext.index = new Map([...labelContext.labels].map((id, index) => [id, index]));
      }
      return labelContext.index.has(node) ? labelContext.index.get(node) : -1;
    }

    if (!renderer || typeof renderer.getNodeDisplayedLabels !== 'function') return -1;
    return [...renderer.getNodeDisplayedLabels()].indexOf(node);
  }

  function bestPointerHit(pos) {
    if (!renderer || !graph || !pos) return null;

    const labelContext = pointerLabelContext();
    const hits = pointerHitCandidateNodes(pos, labelContext)
      .map(node => nodePointerHit(node, pos, labelContext))
      .filter(Boolean);
    if (!hits.length) return null;

    hits.sort((a, b) => (
      Number(b.diskHit) - Number(a.diskHit) ||
      b.labelPriority - a.labelPriority ||
      b.levelIndex - a.levelIndex ||
      a.distanceRatio - b.distanceRatio ||
      a.screenSize - b.screenSize ||
      a.distance - b.distance
    ));

    return hits[0].node;
  }

  function clickTargetNode(payload) {
    const clicked = payload && payload.node && graphHasNode(payload.node) && nodeVisible(payload.node)
      ? payload.node
      : null;
    const hovered = viewState.hoverClickNode && graphHasNode(viewState.hoverClickNode)
      ? viewState.hoverClickNode
      : null;
    const pos = eventPosition(payload);

    if (hovered && nodePointerHit(hovered, pos)) return hovered;
    if (clicked) return clicked;
    return bestPointerHit(pos);
  }

  /* -------------------------------------------------------------------------
   * Tooltip
   * -------------------------------------------------------------------------*/
  const tooltip = document.getElementById('mm-tooltip');
  const hoverTooltip = document.getElementById('mm-hover-tooltip');
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

  function nodeTooltipPosition(node) {
    if (!renderer || !graphHasNode(node)) return null;

    const attrs = graph.getNodeAttributes(node);
    const display = typeof renderer.getNodeDisplayData === 'function'
      ? renderer.getNodeDisplayData(node)
      : null;
    const point = renderer.graphToViewport({ x: attrs.x, y: attrs.y });
    const rawSize = display && Number.isFinite(display.size)
      ? display.size
      : nodeDisplaySize(attrs);
    const size = typeof renderer.scaleSize === 'function'
      ? renderer.scaleSize(rawSize)
      : rawSize;
    const radius = Math.max(Number.isFinite(size) ? size : 0, minimumNodeScreenRadius());

    return {
      x: point.x,
      y: point.y - radius,
      placement: 'node-top',
      nodeDisk: {
        x: point.x,
        y: point.y,
        radius,
      },
    };
  }

  function nodeTooltipLabel(d) {
    return d.fullLabel || d.title || String(d.label || '').replace(/\s*\n\s*/g, ' ') || d.id || 'Untitled';
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

    const anchor = nodeTooltipPosition(node) || pos;
    const authors = formatAuthors(d.authors);
    const tags = (d.tags || []).slice(0, 7).join(' · ');
    const actions = paperActionLinks(d, { includeMap: false });
    const shortLabel = String(d.fullLabel || d.label || '').replace(/\s*\n\s*/g, ' ').trim();
    tooltip.innerHTML =
      `<div class="tt-title">${escHtml(d.title)}</div>` +
      (shortLabel && shortLabel !== d.title ? `<div class="tt-short-label">${escHtml(shortLabel)}</div>` : '') +
      `<div class="tt-meta">${escHtml(authors)}&nbsp;&nbsp;${d.year || ''}</div>` +
      (tags ? `<div class="tt-tags">${escHtml(tags)}</div>` : '') +
      (d.summary ? `<div class="tt-summary">${escHtml(d.summary)}</div>` : '') +
      (actions ? `<div class="tt-actions paper-link-pills">${actions}</div>` : '') +
      (!pinned ? `<div class="tt-hint">Click to pin</div>` : `<div class="tt-hint">Click node again to unpin</div>`);
    tooltip.classList.toggle('pinned', pinned);
    placeTooltip(anchor);
  }

  function showAggregateTooltip(d, pos, pinned) {
    const level = detailLevelLabel(d.detailLevel);
    const nextIndex = DETAIL_LEVELS.indexOf(d.detailLevel) + 1;
    const nextLabel = DETAIL_LEVELS[nextIndex]
      ? detailLevelLabel(DETAIL_LEVELS[nextIndex])
      : null;

    tooltip.innerHTML =
      `<div class="tt-title">${escHtml(d.fullLabel || d.title)}</div>` +
      `<div class="tt-meta">${escHtml(level)} group&nbsp;&nbsp;${d.count || 0} items</div>` +
      (nextLabel ? `<div class="tt-hint">Click to show ${escHtml(nextLabel)}</div>` : '') +
      (!nextLabel && !pinned ? `<div class="tt-hint">Click to pin</div>` : '') +
      (!nextLabel && pinned ? `<div class="tt-hint">Click node again to unpin</div>` : '');
    tooltip.classList.toggle('pinned', pinned);
    placeTooltip(pos);
  }

  function showHoverTooltip(node) {
    if (!hoverTooltip || mobileViewport() || !graphHasNode(node) || !nodeVisible(node)) return;

    const d = graph.getNodeAttributes(node);
    const pos = nodeTooltipPosition(node);
    if (!pos) return;
    const label = nodeTooltipLabel(d);
    const subtitle = d.kind === 'paper' && d.title && d.title !== label
      ? d.title
      : '';
    const meta = d.kind === 'aggregate'
      ? `${detailLevelLabel(d.detailLevel)} group · ${d.count || 0} items`
      : [formatAuthors(d.authors), d.year].filter(Boolean).join('  ');

    viewState.hoverTooltipNode = node;
    hoverTooltip.innerHTML =
      `<div class="tt-mini-title">${escHtml(label)}</div>` +
      (subtitle ? `<div class="tt-mini-subtitle">${escHtml(subtitle)}</div>` : '') +
      (meta ? `<div class="tt-mini-meta">${escHtml(meta)}</div>` : '');
    hoverTooltip.classList.add('visible');
    placeTooltip(pos, { element: hoverTooltip });
  }

  function hideHoverTooltip() {
    viewState.hoverTooltipNode = null;
    if (hoverTooltip) hoverTooltip.classList.remove('visible');
  }

  function updateActiveTooltipPositions() {
    if (viewState.pinnedNode && tooltip && tooltip.classList.contains('visible')) {
      const pos = nodeTooltipPosition(viewState.pinnedNode);
      if (pos) placeTooltip(pos);
    }

    if (viewState.hoverTooltipNode && hoverTooltip && hoverTooltip.classList.contains('visible')) {
      if (!graphHasNode(viewState.hoverTooltipNode) || !nodeVisible(viewState.hoverTooltipNode)) {
        hideHoverTooltip();
        return;
      }
      if (!viewState.pinnedNode && viewState.hoverTooltipNode !== viewState.hoveredNode) {
        hideHoverTooltip();
        return;
      }
      const pos = nodeTooltipPosition(viewState.hoverTooltipNode);
      if (pos) placeTooltip(pos, { element: hoverTooltip });
    }
  }

  function placeTooltip(pos, options = {}) {
    const el = options.element || tooltip;
    if (!el || !pos) return;

    const MARGIN = 12;
    const graphRect = graphContainer.getBoundingClientRect();

    el.classList.add('visible');
    const W = el.offsetWidth;
    const H = el.offsetHeight;

    const anchorX = graphRect.left + pos.x;
    const anchorY = graphRect.top + pos.y;
    const bounds = tooltipGraphViewportRect(MARGIN);
    const avoidRects = tooltipAvoidRects(bounds);
    const minX = Math.min(bounds.left, Math.max(bounds.left, bounds.right - W));
    const maxX = Math.max(minX, bounds.right - W);
    const minTop = Math.min(bounds.top, Math.max(bounds.top, bounds.bottom - H));
    const maxTop = Math.max(minTop, bounds.bottom - H);
    const clampX = value => Math.max(minX, Math.min(value, maxX));
    const clampY = value => Math.max(minTop, Math.min(value, maxTop));

    if (pos.placement === 'node-top') {
      placeNodeAnchoredTooltip(el, pos, {
        graphRect,
        bounds,
        avoidRects,
        margin: MARGIN,
        width: W,
        height: H,
        clampX,
        clampY,
      });
      return;
    }

    const rawCandidates = [
      { x: anchorX + MARGIN, y: anchorY + MARGIN },
      { x: anchorX + MARGIN, y: anchorY - H - MARGIN },
      { x: anchorX - W - MARGIN, y: anchorY + MARGIN },
      { x: anchorX - W - MARGIN, y: anchorY - H - MARGIN },
    ];

    const candidates = rawCandidates.map((candidate, index) => ({
      x: clampX(candidate.x),
      y: clampY(candidate.y),
      index,
    }));

    const best = candidates.reduce((winner, candidate) => {
      const overlap = tooltipCollisionArea(candidate.x, candidate.y, W, H, avoidRects);
      const distance = Math.abs(candidate.x - rawCandidates[candidate.index].x) +
        Math.abs(candidate.y - rawCandidates[candidate.index].y);
      const score = overlap * 1000 + distance + candidate.index;
      return !winner || score < winner.score ? { ...candidate, score } : winner;
    }, null);

    let x = best ? best.x : clampX(anchorX + MARGIN);
    let y = best ? best.y : clampY(anchorY + MARGIN);

    el.style.left = `${x}px`;
    el.style.top = `${y}px`;
  }

  function placeNodeAnchoredTooltip(el, pos, options) {
    const graphRect = options.graphRect;
    const margin = options.margin;
    const W = options.width;
    const H = options.height;
    const clampX = options.clampX;
    const clampY = options.clampY;
    const disk = pos.nodeDisk || null;

    if (!disk) {
      el.style.left = `${clampX(graphRect.left + pos.x - W / 2)}px`;
      el.style.top = `${clampY(graphRect.top + pos.y - H - margin)}px`;
      return;
    }

    const centerX = graphRect.left + disk.x;
    const centerY = graphRect.top + disk.y;
    const radius = Math.max(Number(disk.radius) || 0, minimumNodeScreenRadius());
    const gap = margin;
    const diskRect = {
      left: centerX - radius,
      right: centerX + radius,
      top: centerY - radius,
      bottom: centerY + radius,
    };
    const rawCandidates = [
      { x: centerX - W / 2, y: centerY - radius - H - gap },
      { x: centerX + radius + gap, y: centerY - H / 2 },
      { x: centerX - radius - gap - W, y: centerY - H / 2 },
      { x: centerX - W / 2, y: centerY + radius + gap },
      { x: centerX + radius + gap, y: centerY - radius - H - gap },
      { x: centerX - radius - gap - W, y: centerY - radius - H - gap },
      { x: centerX + radius + gap, y: centerY + radius + gap },
      { x: centerX - radius - gap - W, y: centerY + radius + gap },
    ];
    const candidates = rawCandidates.map((candidate, index) => ({
      x: clampX(candidate.x),
      y: clampY(candidate.y),
      index,
    }));

    const best = candidates.reduce((winner, candidate) => {
      const raw = rawCandidates[candidate.index];
      const diskOverlap = tooltipCollisionArea(candidate.x, candidate.y, W, H, [diskRect]);
      const blockerOverlap = tooltipCollisionArea(candidate.x, candidate.y, W, H, options.avoidRects);
      const displacement = Math.abs(candidate.x - raw.x) + Math.abs(candidate.y - raw.y);
      const score = diskOverlap * 100000 + blockerOverlap * 1000 + displacement * 4 + candidate.index;
      return !winner || score < winner.score ? { ...candidate, score } : winner;
    }, null);

    const x = best ? best.x : clampX(centerX - W / 2);
    const y = best ? best.y : clampY(centerY - radius - H - gap);

    el.style.left = `${x}px`;
    el.style.top = `${y}px`;
  }

  function visibleElementRect(el) {
    if (!el || el.hidden) return null;
    const style = getComputedStyle(el);
    if (style.display === 'none' || style.visibility === 'hidden' || style.pointerEvents === 'none') return null;
    const rect = el.getBoundingClientRect();
    if (rect.width <= 0 || rect.height <= 0) return null;
    return {
      left: rect.left,
      right: rect.right,
      top: rect.top,
      bottom: rect.bottom,
      width: rect.width,
      height: rect.height,
    };
  }

  function tooltipBoundaryRects() {
    const selectors = [
      '#mm-panel-header',
      '#mm-panel',
      '.md-header',
      '.md-tabs',
      '.md-sidebar--primary',
      '.md-sidebar--secondary',
    ];
    const elements = new Set();
    selectors.forEach(selector => {
      document.querySelectorAll(selector).forEach(el => elements.add(el));
    });

    return [...elements]
      .map(visibleElementRect)
      .filter(Boolean);
  }

  function rectOverlap(a, b) {
    return {
      x: Math.max(0, Math.min(a.right, b.right) - Math.max(a.left, b.left)),
      y: Math.max(0, Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top)),
    };
  }

  function tooltipGraphViewportRect(margin) {
    const graphRect = graphContainer.getBoundingClientRect();
    const rootStyle = getComputedStyle(document.documentElement);
    const headerHeight = parseFloat(rootStyle.getPropertyValue('--mm-header-h')) || 0;
    const footerHeight = parseFloat(rootStyle.getPropertyValue('--mm-footer-h')) || 0;
    const rect = {
      left: Math.max(margin, graphRect.left + margin),
      right: Math.min(window.innerWidth - margin, graphRect.right - margin),
      top: Math.max(margin, headerHeight + margin, graphRect.top + margin),
      bottom: Math.min(window.innerHeight - footerHeight - margin, graphRect.bottom - margin),
    };

    tooltipBoundaryRects().forEach(blocker => {
      const overlap = rectOverlap(rect, blocker);
      const width = Math.max(1, rect.right - rect.left);
      const height = Math.max(1, rect.bottom - rect.top);

      if (overlap.y > 0 && blocker.height > height * 0.25) {
        if (blocker.left <= rect.left + 1 && blocker.right > rect.left) {
          rect.left = Math.max(rect.left, blocker.right + margin);
        }
        if (blocker.right >= rect.right - 1 && blocker.left < rect.right) {
          rect.right = Math.min(rect.right, blocker.left - margin);
        }
      }

      if (overlap.x > 0 && blocker.width > width * 0.35) {
        if (blocker.top <= rect.top + 1 && blocker.bottom > rect.top) {
          rect.top = Math.max(rect.top, blocker.bottom + margin);
        }
        if (blocker.bottom >= rect.bottom - 1 && blocker.top < rect.bottom) {
          rect.bottom = Math.min(rect.bottom, blocker.top - margin);
        }
      }
    });

    if (rect.right <= rect.left) {
      rect.left = Math.max(margin, graphRect.left + margin);
      rect.right = Math.max(rect.left + 1, Math.min(window.innerWidth - margin, graphRect.right - margin));
    }
    if (rect.bottom <= rect.top) {
      rect.top = Math.max(margin, headerHeight + margin, graphRect.top + margin);
      rect.bottom = Math.max(rect.top + 1, Math.min(window.innerHeight - footerHeight - margin, graphRect.bottom - margin));
    }

    return rect;
  }

  function tooltipAvoidRects(bounds) {
    const canvasBounds = bounds || tooltipGraphViewportRect(12);
    return [
      ...tooltipBoundaryRects(),
    ].filter(rect => {
      const overlap = rectOverlap(canvasBounds, rect);
      return overlap.x > 0 && overlap.y > 0;
    });
  }

  function tooltipCollisionArea(left, top, width, height, rects) {
    return rects.reduce((area, rect) => {
      const overlapX = Math.max(0, Math.min(left + width, rect.right) - Math.max(left, rect.left));
      const overlapY = Math.max(0, Math.min(top + height, rect.bottom) - Math.max(top, rect.top));
      return area + overlapX * overlapY;
    }, 0);
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

  function paperTreeUrl(d) {
    return `../tree/#paper=${encodeURIComponent(d.id)}`;
  }

  function paperMapUrl(d) {
    return `#paper=${encodeURIComponent(d.id)}`;
  }

  function paperTimelineUrl(d) {
    return `../timeline/#paper=${encodeURIComponent(d.id)}`;
  }

  function paperSearchUrl(d) {
    return `../search/?paper=${encodeURIComponent(d.id)}`;
  }

  function paperActionLink(url, label, variant, external) {
    return window.kbSiteLinks.renderPill({
      url,
      label,
      variant: variant || 'internal',
      external: Boolean(external),
      detail: external ? '' : `Open in ${label}`,
    });
  }

  function paperActionLinks(d, options) {
    const includeMap = !options || options.includeMap !== false;
    return [
      paperActionLink(d.link, 'Document', 'primary', true),
      window.kbSiteLinks.renderPaperSiteLinks(
        {
          url: paperDetailUrl(d),
          mapUrl: paperMapUrl(d),
          treeUrl: paperTreeUrl(d),
          timelineUrl: paperTimelineUrl(d),
          searchUrl: paperSearchUrl(d),
        },
        { includeMap }
      ),
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
      paperActionLinks(d, { includeMap: false }) +
      `</div>`;
    modal.hidden = false;
    if (modalClose) modalClose.focus({ preventScroll: true });
  }

  function closePaperModalSelection() {
    if (!modal || modal.hidden) return;
    hidePaperModal();
    viewState.clearSelection();
    setSelectedNodeFilterEnabled(false);
    hideHoverTooltip();
    syncUrlToPinnedNode();
    refreshView();
  }

  /* -------------------------------------------------------------------------
   * Filters
   * -------------------------------------------------------------------------*/
  function applyCategoryFilter() {
    if (viewState.pinnedNode && !nodeVisibleAt(viewState.pinnedNode, viewState.currentDetailLevel)) {
      viewState.clearSelection();
      setSelectedNodeFilterEnabled(false);
      hideHoverTooltip();
      hideTooltip();
      hidePaperModal();
      syncUrlToPinnedNode();
    }
    refreshView();
  }

  function applyRelevanceFilter() {
    if (relevanceRefreshFrame !== null) return;

    relevanceRefreshFrame = window.requestAnimationFrame(() => {
      relevanceRefreshFrame = null;
      refreshView();
    });
  }

  function applyDetailLevel(level) {
    const nextLevel = detailLevelForActiveBranch(level);
    if (!nextLevel) return;
    if (viewState.currentDetailLevel === nextLevel) return;
    const previousLevel = viewState.currentDetailLevel;

    finishLevelTransition();
    const transitionNodes = renderer
      ? prepareLevelTransition(previousLevel, nextLevel)
      : [];

    viewState.currentDetailLevel = nextLevel;
    viewState.clearSelection();
    setSelectedNodeFilterEnabled(false);
    hideHoverTooltip();
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
    if (!graph || viewState.currentDetailLevel !== 'paper') return PAPER_NODE_RADIUS_TARGET;

    const minDistance = minimumVisiblePaperGraphDistance();
    if (!Number.isFinite(minDistance) || minDistance <= 0) return PAPER_NODE_RADIUS_TARGET;

    return Math.min(
      PAPER_NODE_RADIUS_TARGET,
      minDistance / (2 * (1 + PAPER_NODE_RADIUS_CLEARANCE_RATIO))
    );
  }

  function relevantPaperCount() {
    return relevanceEvaluation().count;
  }

  function updateRelevancePanel() {
    const panel = document.getElementById('mm-relevance-panel');
    if (!panel) return;

    const egoId = selectedRelevanceEgo();
    panel.hidden = !egoId;
    if (!egoId) return;

    const ego = mapModel.paper(egoId) || {};
    const title = document.getElementById('mm-relevance-ego');
    const count = document.getElementById('mm-relevance-match-count');
    const status = document.getElementById('mm-relevance-status');

    if (title) title.textContent = ego.title || ego.label || egoId;
    if (count) count.textContent = `${relevantPaperCount()} / ${DATA.nodes.length}`;
    if (status) {
      status.textContent = viewState.relevanceFilter.enabled
        ? `${viewState.relevanceFilter.mode.toUpperCase()} filter active`
        : 'Filter off';
    }
  }

  /* -------------------------------------------------------------------------
   * Fit to visible graph, leaving space for the overlay panel when open.
   * -------------------------------------------------------------------------*/
  function fitNodeEligible(attrs) {
    return HIERARCHY_LEVEL_BY_ID.has(attrs.detailLevel) && nodeAllowedByFilters(attrs);
  }

  function expandBBoxes(bboxes, rawPoint, framedPoint, rawRadius = 0) {
    const radius = Number.isFinite(rawRadius) ? Math.max(0, rawRadius) : 0;
    bboxes.rawXmin = Math.min(bboxes.rawXmin, rawPoint.x - radius);
    bboxes.rawXmax = Math.max(bboxes.rawXmax, rawPoint.x + radius);
    bboxes.rawYmin = Math.min(bboxes.rawYmin, rawPoint.y - radius);
    bboxes.rawYmax = Math.max(bboxes.rawYmax, rawPoint.y + radius);
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

  function rawBBoxForNodes(nodes) {
    const bboxes = {
      rawXmin: Infinity,
      rawXmax: -Infinity,
      rawYmin: Infinity,
      rawYmax: -Infinity,
    };

    nodes.forEach(node => {
      if (!graphHasNode(node)) return;
      const attrs = graph.getNodeAttributes(node);
      const point = homePoint(attrs);
      const radius = Math.max(Number(nodeDisplaySize(attrs)) || 0, 0);
      if (!Number.isFinite(point.x) || !Number.isFinite(point.y)) return;

      bboxes.rawXmin = Math.min(bboxes.rawXmin, point.x - radius);
      bboxes.rawXmax = Math.max(bboxes.rawXmax, point.x + radius);
      bboxes.rawYmin = Math.min(bboxes.rawYmin, point.y - radius);
      bboxes.rawYmax = Math.max(bboxes.rawYmax, point.y + radius);
    });

    if (!Number.isFinite(bboxes.rawXmin)) return null;

    if (bboxes.rawXmin === bboxes.rawXmax) {
      bboxes.rawXmin -= 1;
      bboxes.rawXmax += 1;
    }
    if (bboxes.rawYmin === bboxes.rawYmax) {
      bboxes.rawYmin -= 1;
      bboxes.rawYmax += 1;
    }

    const rawPadX = Math.max((bboxes.rawXmax - bboxes.rawXmin) * 0.04, 1);
    const rawPadY = Math.max((bboxes.rawYmax - bboxes.rawYmin) * 0.04, 1);

    return {
      x: [bboxes.rawXmin - rawPadX, bboxes.rawXmax + rawPadX],
      y: [bboxes.rawYmin - rawPadY, bboxes.rawYmax + rawPadY],
    };
  }

  function zoomOutRawBBox() {
    const nodes = [];
    graph.forEachNode((node, attrs) => {
      if (fitNodeEligible(attrs)) nodes.push(node);
    });
    if (nodes.length) return rawBBoxForNodes(nodes);

    const allNodes = [];
    graph.forEachNode(node => allNodes.push(node));
    return rawBBoxForNodes(allNodes);
  }

  function framedPointForRawPoint(point, padding) {
    const baseState = { x: 0.5, y: 0.5, ratio: 1, angle: 0 };
    const viewportPoint = renderer.graphToViewport(point, { cameraState: baseState, padding });
    return renderer.viewportToFramedGraph(viewportPoint, { cameraState: baseState, padding });
  }

  function viewportBBoxForRawBBox(rawBBox, cameraState, padding) {
    const points = [
      { x: rawBBox.x[0], y: rawBBox.y[0] },
      { x: rawBBox.x[1], y: rawBBox.y[0] },
      { x: rawBBox.x[0], y: rawBBox.y[1] },
      { x: rawBBox.x[1], y: rawBBox.y[1] },
    ].map(point => renderer.graphToViewport(point, { cameraState, padding }));

    const xs = points.map(point => point.x).filter(Number.isFinite);
    const ys = points.map(point => point.y).filter(Number.isFinite);
    if (!xs.length || !ys.length) return null;

    const left = Math.min(...xs);
    const right = Math.max(...xs);
    const top = Math.min(...ys);
    const bottom = Math.max(...ys);

    return {
      left,
      right,
      top,
      bottom,
      width: right - left,
      height: bottom - top,
    };
  }

  function zoomOutLimitForRawBBox(rawBBox, minAllowedRatio = 0) {
    if (!renderer || !rawBBox) return null;

    const dims = renderer.getDimensions();
    if (!dims.width || !dims.height) return null;

    const padding = VIEWPORT_PADDING;
    const usable = usableCanvasRect(padding);
    const usableWidth = Math.max(usable.right - usable.left, 1);
    const usableHeight = Math.max(usable.bottom - usable.top, 1);
    const rawCenter = {
      x: (rawBBox.x[0] + rawBBox.x[1]) / 2,
      y: (rawBBox.y[0] + rawBBox.y[1]) / 2,
    };
    const framedCenter = framedPointForRawPoint(rawCenter, padding);
    if (!Number.isFinite(framedCenter.x) || !Number.isFinite(framedCenter.y)) return null;

    const centeredState = {
      x: framedCenter.x,
      y: framedCenter.y,
      ratio: 1,
      angle: 0,
    };
    const screenBBox = viewportBBoxForRawBBox(rawBBox, centeredState, padding);
    if (!screenBBox) return null;

    const requiredRatio = Math.max(
      1,
      screenBBox.width / usableWidth,
      screenBBox.height / usableHeight,
      Number(minAllowedRatio) || 0
    );

    return Math.max(
      MIN_CAMERA_RATIO * 1.05,
      requiredRatio * MAX_ZOOM_OUT_OVERSCAN_RATIO
    );
  }

  function updateZoomOutLimit(minAllowedRatio = 0) {
    if (!renderer || !graph) return;

    const limit = zoomOutLimitForRawBBox(zoomOutRawBBox(), minAllowedRatio);
    if (!Number.isFinite(limit)) return;

    const currentLimit = Number(renderer.getSetting('maxCameraRatio'));
    if (Number.isFinite(currentLimit) && Math.abs(currentLimit - limit) < 1e-4) return;

    renderer.setSetting('maxCameraRatio', limit);
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
      const rawRadius = nodeDisplaySize(attrs);
      const displayAttrs = renderer && typeof renderer.getNodeDisplayData === 'function'
        ? renderer.getNodeDisplayData(node)
        : null;
      const framedPoint = displayAttrs &&
        Number.isFinite(displayAttrs.x) &&
        Number.isFinite(displayAttrs.y)
          ? displayAttrs
          : attrs;

      expandBBoxes(bboxes, rawPoint, framedPoint, rawRadius);
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

    const visit = (node, attrs) => {
      const rawRadius = nodeDisplaySize(attrs);
      const displayAttrs = renderer && typeof renderer.getNodeDisplayData === 'function'
        ? renderer.getNodeDisplayData(node)
        : null;
      const framedPoint = displayAttrs &&
        Number.isFinite(displayAttrs.x) &&
        Number.isFinite(displayAttrs.y)
          ? displayAttrs
          : attrs;

      expandBBoxes(bboxes, attrs, framedPoint, rawRadius);
    };

    if (viewState.visibleNodes) {
      viewState.visibleNodes.forEach(node => visit(node, graph.getNodeAttributes(node)));
    } else {
      graph.forEachNode((node, attrs) => {
        if (!nodeVisible(node)) return;
        visit(node, attrs);
      });
    }

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
    if (viewState.visibleNodes) {
      viewState.visibleNodes.forEach(node => {
        const attrs = graph.getNodeAttributes(node);
        points.push({ x: attrs.x, y: attrs.y });
      });
    } else {
      graph.forEachNode((node, attrs) => {
        if (!nodeVisible(node)) return;
        points.push({ x: attrs.x, y: attrs.y });
      });
    }

    return minimumPointDistance(points);
  }

  function minimumVisiblePaperGraphDistance() {
    if (!graph) return Infinity;

    const points = [];
    const visit = (node, attrs) => {
      if (attrs.kind !== 'paper') return;
      points.push({ x: attrs.x, y: attrs.y });
    };

    if (viewState.visibleNodes) {
      viewState.visibleNodes.forEach(node => visit(node, graph.getNodeAttributes(node)));
    } else {
      graph.forEachNode((node, attrs) => {
        if (!nodeVisible(node)) return;
        visit(node, attrs);
      });
    }

    return minimumPointDistance(points);
  }

  function minimumVisibleScreenDistance(cameraState) {
    if (!renderer || !graph) return Infinity;

    const points = [];
    const visit = attrs => {
      const p = renderer.graphToViewport(
        { x: attrs.x, y: attrs.y },
        cameraState ? { cameraState } : undefined
      );
      points.push(p);
    };

    if (viewState.visibleNodes) {
      viewState.visibleNodes.forEach(node => visit(graph.getNodeAttributes(node)));
    } else {
      graph.forEachNode((node, attrs) => {
        if (!nodeVisible(node)) return;
        visit(attrs);
      });
    }

    return minimumPointDistance(points);
  }

  function fitNodes() {
    if (!graph) return [];
    if (viewState.visibleNodes) return [...viewState.visibleNodes].filter(node => graphHasNode(node));

    const nodes = [];
    graph.forEachNode((node) => {
      if (nodeVisible(node)) nodes.push(node);
    });
    return nodes;
  }

  let fitMeasureContext = null;
  function labelMeasureContext() {
    if (fitMeasureContext) return fitMeasureContext;
    if (typeof document === 'undefined') return null;
    fitMeasureContext = document.createElement('canvas').getContext('2d');
    return fitMeasureContext;
  }

  function nodeViewportRadius(attrs, cameraState, padding) {
    const radius = nodeDisplaySize(attrs);
    if (!Number.isFinite(radius) || radius <= 0) return 0;

    const origin = { x: attrs.x, y: attrs.y };
    const edge = { x: attrs.x + radius, y: attrs.y };
    const options = { cameraState, padding };
    const a = renderer.graphToViewport(origin, options);
    const b = renderer.graphToViewport(edge, options);
    return Math.abs(b.x - a.x);
  }

  function labelTextHalfExtents(attrs, cameraState) {
    const label = viewState.showNodeLabels ? attrs.label : '';
    if (!label) return { width: 0, height: 0 };

    const context = labelMeasureContext();
    const lines = String(label).split('\n');
    const zoomScale = nodeLabelZoomScaleForRatio(cameraState && cameraState.ratio);
    const { fontSize, lineHeight, outlineWidth } = currentNodeLabelMetrics(attrs, zoomScale);
    let maxWidth = 0;

    if (context) {
      context.font = `650 ${fontSize}px "Atkinson Hyperlegible Next", "Segoe UI", sans-serif`;
      lines.forEach(line => {
        maxWidth = Math.max(maxWidth, context.measureText(line).width);
      });
    } else {
      lines.forEach(line => {
        maxWidth = Math.max(maxWidth, String(line).length * fontSize * 0.58);
      });
    }

    return {
      width: maxWidth / 2 + outlineWidth + 4,
      height: ((Math.max(lines.length, 1) - 1) * lineHeight + fontSize) / 2 + outlineWidth + 4,
    };
  }

  function screenContentBBox(cameraState, padding) {
    const nodes = fitNodes();
    if (!nodes.length) return null;

    const bounds = {
      left: Infinity,
      right: -Infinity,
      top: Infinity,
      bottom: -Infinity,
    };

    nodes.forEach(node => {
      const attrs = graph.getNodeAttributes(node);
      const point = renderer.graphToViewport({ x: attrs.x, y: attrs.y }, { cameraState, padding });
      if (!Number.isFinite(point.x) || !Number.isFinite(point.y)) return;

      const nodeRadius = nodeViewportRadius(attrs, cameraState, padding);
      const labelExtents = labelTextHalfExtents(attrs, cameraState);
      const halfWidth = Math.max(nodeRadius, labelExtents.width);
      const halfHeight = Math.max(nodeRadius, labelExtents.height);

      bounds.left = Math.min(bounds.left, point.x - halfWidth);
      bounds.right = Math.max(bounds.right, point.x + halfWidth);
      bounds.top = Math.min(bounds.top, point.y - halfHeight);
      bounds.bottom = Math.max(bounds.bottom, point.y + halfHeight);
    });

    if (!Number.isFinite(bounds.left)) return null;

    return {
      ...bounds,
      width: bounds.right - bounds.left,
      height: bounds.bottom - bounds.top,
    };
  }

  function usableCanvasCenter(usable, dims) {
    return {
      x: usable.left < usable.right ? (usable.left + usable.right) / 2 : dims.width / 2,
      y: usable.top < usable.bottom ? (usable.top + usable.bottom) / 2 : dims.height / 2,
    };
  }

  function recenterCameraOnScreenBBox(cameraState, screenBBox, desired, padding) {
    if (!screenBBox) return cameraState;

    const contentCenter = {
      x: (screenBBox.left + screenBBox.right) / 2,
      y: (screenBBox.top + screenBBox.bottom) / 2,
    };
    const framedContent = renderer.viewportToFramedGraph(contentCenter, { cameraState, padding });
    const framedDesired = renderer.viewportToFramedGraph(desired, { cameraState, padding });

    return {
      ...cameraState,
      x: cameraState.x + (framedContent.x - framedDesired.x),
      y: cameraState.y + (framedContent.y - framedDesired.y),
    };
  }

  function includeLabelsInFit(cameraState, usable, dims, padding) {
    let target = { ...cameraState };
    const desired = usableCanvasCenter(usable, dims);
    const usableWidth = Math.max(usable.right - usable.left, 1);
    const usableHeight = Math.max(usable.bottom - usable.top, 1);

    for (let i = 0; i < 4; i += 1) {
      const bounds = screenContentBBox(target, padding);
      if (!bounds) return target;

      const scale = Math.max(
        1,
        bounds.width / usableWidth,
        bounds.height / usableHeight
      );

      if (scale > 1.001) {
        target = {
          ...target,
          ratio: target.ratio * scale * 1.04,
        };
      }

      target = recenterCameraOnScreenBBox(target, screenContentBBox(target, padding), desired, padding);
    }

    return target;
  }

  function fitVisible(duration) {
    if (!renderer || !graph) return;

    finishLevelTransition();
    renderer.resize(true);
    renderer.refresh();

    const bboxes = visibleBBoxes() || allDetailBBoxes();
    if (!bboxes) return;

    const PAD = VIEWPORT_PADDING;
    const dims = renderer.getDimensions();
    if (!dims.width || !dims.height) return;

    const usable = usableCanvasRect(PAD);
    const stagePadding = PAD;
    const desired = usableCanvasCenter(usable, dims);
    const bboxCenterX = (bboxes.framed.x[0] + bboxes.framed.x[1]) / 2;
    const bboxCenterY = (bboxes.framed.y[0] + bboxes.framed.y[1]) / 2;
    const baseState = { x: bboxCenterX, y: bboxCenterY, ratio: 1, angle: 0 };

    renderer.setCustomBBox(bboxes.raw);
    renderer.setSetting('stagePadding', stagePadding);
    renderer.refresh();

    const framedAtDesiredCenter = renderer.viewportToFramedGraph(
      desired,
      { cameraState: baseState, padding: stagePadding }
    );

    let target = {
      x: baseState.x + (bboxCenterX - framedAtDesiredCenter.x),
      y: baseState.y + (bboxCenterY - framedAtDesiredCenter.y),
      ratio: 1,
      angle: 0,
    };
    target = includeLabelsInFit(target, usable, dims, stagePadding);
    updateZoomOutLimit(target.ratio);

    if (duration === 0) renderer.getCamera().setState(target);
    else renderer.getCamera().animate(target, { duration: duration || 260 });
  }

  function readFocusPaperId() {
    try {
      const query = new URLSearchParams(window.location.search);
      const paperId = query.get('paper') || query.get('node');
      if (paperId) return paperId;
    } catch (error) {
      // Keep supporting hash-only browsers/links if query parsing fails.
    }

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
    writeFocusPaperId(paperIdForNode(viewState.pinnedNode));
  }

  function clearPinnedPaperSelection() {
    if (!paperIdForNode(viewState.pinnedNode)) return false;

    viewState.clearSelection();
    setSelectedNodeFilterEnabled(false);
    hideHoverTooltip();
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

  function applyTopOverlayOcclusion(rect, bounds, dims, pad, maxHeightRatio = PANEL_MAX_FOCUS_WIDTH_RATIO) {
    if (!bounds || bounds.height >= dims.height * maxHeightRatio) return;

    const centerX = (rect.left + rect.right) / 2;
    const centerUnderOverlay = centerX >= bounds.left && centerX <= bounds.right;
    if (!centerUnderOverlay || bounds.bottom <= rect.top) return;

    rect.top = Math.max(rect.top, Math.min(bounds.bottom + pad, dims.height - pad));
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
    const branchPanel = document.getElementById('mm-branch-panel');
    const branchPanelOpen = branchPanel && !branchPanel.classList.contains('body-collapsed');
    const branchBounds = branchPanelOpen ? overlayBounds(branchPanel, graphRect, dims) : null;

    applyTopOverlayOcclusion(rect, panelBounds, dims, pad);

    if (branchBounds && branchBounds.right >= dims.width - pad && branchBounds.width < dims.width * 0.45) {
      rect.right = Math.min(rect.right, Math.max(branchBounds.left - pad, pad));
    } else {
      applyTopOverlayOcclusion(rect, branchBounds, dims, pad, 0.7);
    }

    const headerBounds = overlayBounds(document.getElementById('mm-panel-header'), graphRect, dims);
    applyTopOverlayOcclusion(rect, headerBounds, dims, pad, 0.5);

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
    const paperId = paperIdForNode(viewState.pinnedNode) || readFocusPaperId();
    if (!paperId || !graphHasNode(paperId)) return false;

    const attrs = graph.getNodeAttributes(paperId);
    if (attrs.kind !== 'paper') return false;

    focusCameraOnNode(paperId, duration);
    window.setTimeout(() => showFocusedPaperTooltip(paperId), (duration || 0) + 40);
    return true;
  }

  function showFocusedPaperTooltip(node) {
    if (!renderer || !graphHasNode(node)) return;
    showNodeTooltip(node, nodeTooltipPosition(node), true);
  }

  function focusPaperFromHash() {
    const paperId = readFocusPaperId();
    if (!paperId || !renderer || !graphHasNode(paperId)) return false;

    const attrs = graph.getNodeAttributes(paperId);
    if (attrs.kind !== 'paper') return false;

    viewState.currentDetailLevel = 'paper';
    selectBranchForPaper(attrs);
    viewState.selectNode(paperId);
    setSelectedNodeFilterEnabled(true);
    hideHoverTooltip();
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
  function collectBranchFilterGroups(group, groups) {
    if (!group.isCategoryLeaf) groups.push(group);
    group.children.forEach(child => collectBranchFilterGroups(child, groups));
  }

  function branchFilterChildren(group) {
    const children = group ? group.children : mapModel.hierarchy().roots;
    return children.filter(child => !child.isCategoryLeaf);
  }

  function branchFilterPaperChildren(group) {
    if (!group || branchFilterChildren(group).length) return [];
    return (group.leafIds || [])
      .map(mapModel.paper)
      .filter(Boolean);
  }

  function branchFilterName(group) {
    return group ? group.label : 'All branches';
  }

  function branchFilterPathLabel(group) {
    if (!group) return 'Map root';
    const path = Array.isArray(group.path) && group.path.length
      ? group.path
      : [group.label];
    return path.join(' / ');
  }

  function branchFilterItemCount(group) {
    return group ? group.leafIds.length : mapModel.allPaperNodes().length;
  }

  function branchFilterChildCount(group) {
    return branchFilterChildren(group).length;
  }

  function branchCountLabel(count, singular, pluralLabel = `${singular}s`) {
    return `${count} ${count === 1 ? singular : pluralLabel}`;
  }

  function activeBranchKeyForAggregate(attrs) {
    const path = mapModel.paperPath(attrs);
    const exactKey = `${attrs.hierarchyLevel || attrs.detailLevel}:${path.join('::')}`;
    if (viewState.branchFilterGroups.has(exactKey)) return exactKey;

    let best = null;
    viewState.branchFilterGroups.forEach((group, key) => {
      const groupPath = group.path || [];
      if (groupPath.length > path.length) return;
      if (!groupPath.every((part, index) => path[index] === part)) return;
      if (!best || groupPath.length > best.pathLength) {
        best = { key, pathLength: groupPath.length };
      }
    });
    return best ? best.key : BRANCH_FILTER_ALL;
  }

  function activateBranchNode(attrs, node) {
    clearHoverClickNode(node);
    setActiveBranchFilter(activeBranchKeyForAggregate(attrs));

    const nextLevel = nextDetailLevel(attrs.detailLevel);
    if (nextLevel) {
      applyDetailLevel(nextLevel);
      return;
    }

    applyCategoryFilter();
  }

  function syncBranchFilterWidget() {
    renderBranchFilterWidget();
  }

  function setActiveBranchFilter(key) {
    const nextKey = viewState.branchFilterGroups.has(key) ? key : BRANCH_FILTER_ALL;
    viewState.activeBranchFilterKey = nextKey;
    viewState.activeCategories.clear();

    if (nextKey === BRANCH_FILTER_ALL) {
      mapModel.allPaperNodes().forEach(node => viewState.activeCategories.add(mapModel.nodeKey(node.data || {})));
    } else {
      viewState.branchFilterGroups.get(nextKey).filterKeys.forEach(filterKeyValue => {
        viewState.activeCategories.add(filterKeyValue);
      });
    }

    syncBranchFilterWidget();
    enforceActiveBranchDetailFloor();
  }

  function enforceActiveBranchDetailFloor() {
    const nextLevel = detailLevelForActiveBranch(viewState.currentDetailLevel);
    if (nextLevel && nextLevel !== viewState.currentDetailLevel) {
      applyDetailLevel(nextLevel);
      return;
    }
    updateDetailButtons();
  }

  function selectBranchForPaper(attrs) {
    const key = mapModel.nodeKey(attrs);
    let best = null;
    viewState.branchFilterGroups.forEach((group, groupKey) => {
      if (!group.filterKeys.has(key)) return;
      if (!best || (group.path || []).length > (best.group.path || []).length) {
        best = { group, groupKey };
      }
    });
    setActiveBranchFilter(best ? best.groupKey : BRANCH_FILTER_ALL);
  }

  function buildCategoryFilters(selectedKey = viewState.activeBranchFilterKey) {
    const container = document.getElementById('mm-category-filters');
    if (!container) return;

    const model = mapModel.hierarchy();
    const groups = [];
    model.roots.forEach(root => collectBranchFilterGroups(root, groups));
    viewState.branchFilterGroups = new Map(groups.map(group => [group.key, group]));

    container.innerHTML = '';
    setActiveBranchFilter(selectedKey);
  }

  function renderBranchFilterWidget() {
    const container = document.getElementById('mm-category-filters');
    if (!container) return;

    const currentGroup = viewState.branchFilterGroups.get(viewState.activeBranchFilterKey) || null;
    const ancestors = branchFilterAncestors(currentGroup);
    const branchChildren = branchFilterChildren(currentGroup);
    const paperChildren = branchFilterPaperChildren(currentGroup);
    const sections = [];
    if (ancestors.length) sections.push(branchFilterSection('Ancestors', ancestors, 'path', currentGroup));
    sections.push(branchFilterSection('', [currentGroup], 'ego', currentGroup));
    sections.push(branchFilterChildrenSection(branchChildren, paperChildren, currentGroup));

    container.innerHTML = window.kbTreeNavigator.renderStack({
      density: 'compact',
      sections,
    });
    container.onclick = event => {
      const target = event.target.closest('[data-ct-select]');
      if (!target || !container.contains(target)) return;
      const key = target.getAttribute('data-ct-select') || BRANCH_FILTER_ALL;
      if (key.startsWith(BRANCH_FILTER_PAPER_PREFIX)) {
        focusPaperFromBranchFilter(key.slice(BRANCH_FILTER_PAPER_PREFIX.length));
        return;
      }
      if (viewState.activeBranchFilterKey === key) return;
      setActiveBranchFilter(key);
      applyCategoryFilter();
    };
  }

  function branchFilterAncestors(group) {
    if (!group) return [];
    const ancestors = [null];
    const lineage = [];
    let node = group && group.parent;
    while (node) {
      lineage.unshift(node);
      node = node.parent;
    }
    return ancestors.concat(lineage);
  }

  function branchFilterSection(title, groups, sectionKind, currentGroup) {
    return {
      title,
      kind: sectionKind,
      empty: 'No child branches.',
      rows: groups.map(group => branchFilterRow(group, currentGroup, sectionKind)),
    };
  }

  function branchFilterChildrenSection(branchGroups, papers, currentGroup) {
    const rows = branchGroups.length
      ? branchGroups.map(group => branchFilterRow(group, currentGroup, 'children'))
      : papers.map(branchFilterPaperRow);
    return {
      title: 'Children',
      kind: 'children',
      empty: 'No children.',
      rows,
    };
  }

  function branchFilterRow(group, currentGroup, sectionKind) {
    const key = group ? group.key : BRANCH_FILTER_ALL;
    const itemCount = branchFilterItemCount(group);
    const childCount = branchFilterChildCount(group);
    return {
      id: key,
      kind: 'branch',
      label: branchFilterName(group),
      current: key === viewState.activeBranchFilterKey,
      ancestor: sectionKind === 'path',
      parent: Boolean(currentGroup && (group
        ? currentGroup.parent && currentGroup.parent.key === group.key
        : !currentGroup.parent)),
      successor: sectionKind === 'children',
      hasChildren: childCount > 0,
      color: group && group.color,
      ariaLabel: `${branchFilterPathLabel(group)}, ${branchCountLabel(itemCount, 'item')}, ${branchCountLabel(childCount, 'child', 'children')}`,
      counters: [
        { kind: 'descendants', count: itemCount, singular: 'item' },
        { kind: 'children', count: childCount, singular: 'child', plural: 'children' },
      ],
    };
  }

  function branchFilterPaperRow(attrs) {
    const paperId = attrs.id;
    const authors = Array.isArray(attrs.authors) ? attrs.authors.filter(Boolean) : [];
    const author = authors.length ? authors[0] + (authors.length > 1 ? ' et al.' : '') : '';
    const meta = [author, attrs.year, mapModel.itemType(attrs)].filter(Boolean).join(' / ');
    const label = attrs.label || attrs.title || paperId;
    return {
      id: BRANCH_FILTER_PAPER_PREFIX + paperId,
      kind: 'paper',
      label,
      meta,
      successor: true,
      previewId: false,
      ariaLabel: [attrs.title || label, meta].filter(Boolean).join(', '),
      counters: [],
    };
  }

  function focusPaperFromBranchFilter(paperId) {
    if (!paperId || !graphHasNode(paperId)) return;

    applyDetailLevel('paper');
    viewState.selectNode(paperId);
    setSelectedNodeFilterEnabled(true);
    hideHoverTooltip();
    refreshView();
    focusCameraOnNode(paperId, 320);
    window.setTimeout(() => showFocusedPaperTooltip(paperId), 340);
    writeFocusPaperId(paperId);
  }

  function detailLevelIconMarkup(level) {
    const isItemLevel = level.id === 'paper' || !level.aggregate;
    if (isItemLevel) {
      return '<span class="mm-detail-icon mm-detail-icon--items" aria-hidden="true">' +
        '<svg viewBox="0 0 24 24" focusable="false">' +
        '<path d="M10 12c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zM6 8c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm0 8c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm12-8c1.1 0 2-.9 2-2s-.9-2-2-2-2 .9-2 2 .9 2 2 2zm-4 8c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm4-4c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm-4-4c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2zm-4-4c-1.1 0-2 .9-2 2s.9 2 2 2 2-.9 2-2-.9-2-2-2z"></path>' +
        '</svg>' +
        '</span>';
    }

    const dotCount = Math.min(Math.max((Number(level.pathIndex) || 0) + 1, 1), 4);
    return `<span class="mm-detail-icon mm-detail-icon--die mm-detail-icon--die-${dotCount}" aria-hidden="true">` +
      Array.from({ length: dotCount }, () => '<span class="mm-detail-dot"></span>').join('') +
      '</span>';
  }

  function detailControlLabel(level) {
    return (level.id === 'paper' || !level.aggregate) ? 'Items' : level.label;
  }

  function buildDetailControls() {
    const container = document.getElementById('mm-detail-controls');
    if (!container) return;

    container.innerHTML = '';
    DETAIL_CONTROL_LEVELS.forEach(level => {
      const button = document.createElement('button');
      const label = detailControlLabel(level);
      button.type = 'button';
      button.dataset.level = level.id;
      button.title = label;
      button.setAttribute('aria-label', `Level of detail: ${label}`);
      button.setAttribute('aria-pressed', level.id === viewState.currentDetailLevel ? 'true' : 'false');
      button.innerHTML = detailLevelIconMarkup(level);
      container.appendChild(button);
    });
  }

  function updateDetailButtons() {
    document.querySelectorAll('#mm-detail-controls button[data-level]').forEach(button => {
      const active = button.dataset.level === viewState.currentDetailLevel;
      const disabled = !detailLevelAllowedForActiveBranch(button.dataset.level);
      button.classList.toggle('active', active);
      button.setAttribute('aria-pressed', active ? 'true' : 'false');
      button.disabled = disabled;
      button.setAttribute('aria-disabled', disabled ? 'true' : 'false');
    });
  }

  function updateVisibilityButtons() {
    const labelsToggle = document.getElementById('mm-labels-toggle');

    if (labelsToggle) {
      labelsToggle.setAttribute('aria-checked', viewState.showNodeLabels ? 'true' : 'false');
      labelsToggle.setAttribute('aria-label', 'Node labels');
      labelsToggle.title = viewState.showNodeLabels ? 'Hide node labels' : 'Show node labels';
      const state = labelsToggle.querySelector('.mm-label-toggle-state');
      if (state) state.textContent = viewState.showNodeLabels ? 'On' : 'Off';
    }
  }

  function syncRelevanceControlValues() {
    const enabled = document.getElementById('mm-relevance-enabled');
    const semantic = document.getElementById('mm-relevance-semantic');
    const taxonomy = document.getElementById('mm-relevance-taxonomy');
    const mode = document.getElementById('mm-relevance-mode');
    const simSlider = document.getElementById('mm-relevance-similarity');
    const simVal = document.getElementById('mm-relevance-similarity-val');
    const treeSlider = document.getElementById('mm-relevance-distance');
    const treeVal = document.getElementById('mm-relevance-distance-val');

    if (!enabled || !semantic || !taxonomy || !mode || !simSlider || !treeSlider) return;

    simSlider.min = '0';
    simSlider.max = '100';
    simSlider.step = '1';
    treeSlider.min = '0';
    treeSlider.max = '100';
    treeSlider.step = '1';
    if (!Number.isFinite(viewState.relevanceFilter.treeProximity)) {
      viewState.relevanceFilter.treeProximity = defaultTreeProximity();
    }
    viewState.relevanceFilter.treeProximity = Math.min(
      Math.max(0, viewState.relevanceFilter.treeProximity),
      1
    );

    enabled.checked = viewState.relevanceFilter.enabled;
    semantic.checked = viewState.relevanceFilter.semantic;
    taxonomy.checked = viewState.relevanceFilter.taxonomy;
    mode.value = viewState.relevanceFilter.mode;
    simSlider.value = relevanceThresholdToSliderValue(viewState.relevanceFilter.similarity);
    treeSlider.value = relevanceThresholdToSliderValue(viewState.relevanceFilter.treeProximity);
    if (simVal) simVal.textContent = relevanceSliderValueLabel(simSlider.value);
    if (treeVal) treeVal.textContent = relevanceSliderValueLabel(treeSlider.value);
    updateRelevancePanel();
  }

  function setupRelevanceControls() {
    const enabled = document.getElementById('mm-relevance-enabled');
    const semantic = document.getElementById('mm-relevance-semantic');
    const taxonomy = document.getElementById('mm-relevance-taxonomy');
    const mode = document.getElementById('mm-relevance-mode');
    const simSlider = document.getElementById('mm-relevance-similarity');
    const simVal = document.getElementById('mm-relevance-similarity-val');
    const treeSlider = document.getElementById('mm-relevance-distance');
    const treeVal = document.getElementById('mm-relevance-distance-val');

    if (!enabled || !semantic || !taxonomy || !mode || !simSlider || !treeSlider) return;

    enabled.addEventListener('change', () => {
      viewState.relevanceFilter.enabled = enabled.checked;
      applyRelevanceFilter();
    });
    semantic.addEventListener('change', () => {
      viewState.relevanceFilter.semantic = semantic.checked;
      applyRelevanceFilter();
    });
    taxonomy.addEventListener('change', () => {
      viewState.relevanceFilter.taxonomy = taxonomy.checked;
      applyRelevanceFilter();
    });
    mode.addEventListener('change', () => {
      viewState.relevanceFilter.mode = mode.value === 'or' ? 'or' : 'and';
      applyRelevanceFilter();
    });
    simSlider.addEventListener('input', () => {
      viewState.relevanceFilter.similarity = relevanceSliderValueToThreshold(simSlider.value);
      if (simVal) simVal.textContent = relevanceSliderValueLabel(simSlider.value);
      applyRelevanceFilter();
    });
    treeSlider.addEventListener('input', () => {
      viewState.relevanceFilter.treeProximity = relevanceSliderValueToThreshold(treeSlider.value);
      if (treeVal) treeVal.textContent = relevanceSliderValueLabel(treeSlider.value);
      applyRelevanceFilter();
    });

    syncRelevanceControlValues();
  }

  /* -------------------------------------------------------------------------
   * Wire up controls
   * -------------------------------------------------------------------------*/
  function setupSettingsPanelToggle() {
    const panel = document.getElementById('mm-panel');
    const branchPanel = document.getElementById('mm-branch-panel');
    const hideBtn = document.getElementById('mm-panel-hide-btn');
    if (!panel || !hideBtn) return;
    if (window.matchMedia('(max-width: 700px)').matches) {
      panel.classList.add('body-collapsed');
      if (branchPanel) branchPanel.classList.add('body-collapsed');
      hideBtn.textContent = 'Show Settings';
      hideBtn.title = 'Show Settings';
      hideBtn.setAttribute('aria-expanded', 'false');
    }
    hideBtn.addEventListener('click', () => {
      const collapsed = panel.classList.toggle('body-collapsed');
      if (branchPanel) branchPanel.classList.toggle('body-collapsed', collapsed);
      hideBtn.textContent = collapsed ? 'Show Settings' : 'Hide Settings';
      hideBtn.title = collapsed ? 'Show Settings' : 'Hide Settings';
      hideBtn.setAttribute('aria-expanded', String(!collapsed));
      window.requestAnimationFrame(() => updateZoomOutLimit());
    });
  }

  function setupControls() {
    document.getElementById('mm-fit-btn').addEventListener('click', () => fitVisible());

    buildDetailControls();
    document.querySelectorAll('#mm-detail-controls button[data-level]').forEach(button => {
      button.addEventListener('click', () => applyDetailLevel(button.dataset.level));
    });
    updateDetailButtons();
    updateVisibilityButtons();
    setupRelevanceControls();

    const labelsToggle = document.getElementById('mm-labels-toggle');
    if (labelsToggle) {
      labelsToggle.addEventListener('click', () => {
        viewState.showNodeLabels = !viewState.showNodeLabels;
        updateVisibilityButtons();
        if (renderer) renderer.scheduleRefresh();
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

  }

  /* -------------------------------------------------------------------------
   * Bootstrap
   * -------------------------------------------------------------------------*/
  buildCategoryFilters();
  setupControls();
  initSigma();

  const themeObserver = new MutationObserver(() => {
    visibilityPaletteCache = null;
    theme = readTheme();
    const selectedBranch = viewState.activeBranchFilterKey;
    mapModel.invalidateHierarchy();
    buildCategoryFilters(selectedBranch);
    if (graph) recomputeVisibilityColors();
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
  window._map = {
    graph: () => graph,
    renderer: () => renderer,
    fit: fitVisible,
    detailLevel: () => viewState.currentDetailLevel,
    setDetailLevel: level => applyDetailLevel(level),
    labelsVisible: () => viewState.showNodeLabels,
    relevanceFilter: () => ({ ...viewState.relevanceFilter, active: relevanceFilterActive() }),
    colorContext: () => visibilityColorContext ? {
      colorScheme: theme.colorScheme,
      depth: visibilityColorContext.depth,
      prefix: visibilityColorContext.prefix.slice(),
      labels: [...visibilityColorContext.colorByLabel.keys()],
      colors: [...visibilityColorContext.colorByLabel.entries()],
    } : null,
    setRelevanceFilter: patch => {
      viewState.relevanceFilter = { ...viewState.relevanceFilter, ...(patch || {}) };
      syncRelevanceControlValues();
      refreshView();
    },
    setLabelsVisible: visible => {
      viewState.showNodeLabels = Boolean(visible);
      updateVisibilityButtons();
      if (renderer) renderer.scheduleRefresh();
    },
    metrics: () => ({
      nodeGraphRadius: currentNodeRadius(),
      nodeGraphRadiusTarget: PAPER_NODE_RADIUS_TARGET,
      nodeScreenRadius: renderer && typeof renderer.scaleSize === 'function'
        ? Math.max(renderer.scaleSize(currentNodeRadius()), minimumNodeScreenRadius())
        : currentNodeRadius(),
      nodeRawScreenRadius: renderer && typeof renderer.scaleSize === 'function'
        ? renderer.scaleSize(currentNodeRadius())
        : currentNodeRadius(),
      minimumVisibleGraphDistance: minimumVisibleGraphDistance(),
      minimumVisibleScreenDistance: minimumVisibleScreenDistance(),
      maxCameraRatio: renderer && typeof renderer.getSetting === 'function'
        ? renderer.getSetting('maxCameraRatio')
        : null,
      clearanceRatio: PAPER_NODE_RADIUS_CLEARANCE_RATIO,
      visibleNodeCount: viewState.visibleNodeCount,
      lastLevelTransition: lastLevelTransitionMetrics,
    }),
  };

})();
