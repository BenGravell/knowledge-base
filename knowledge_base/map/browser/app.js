/* browser/app.js - Sigma.js paper map visualisation.
 * Published as javascripts/map.js.
 *
 * Loaded by map.md after:
 *   1. graphology.umd.min.js (sets window.graphology)
 *   2. sigma.min.js          (sets window.Sigma)
 *   3. map-data.js           (sets window.mapData, includes UMAP positions)
 *   4. map-paper-derivations.js (sets window.kbMapPaperDerivations)
 *   5. browser-map-model.js  (sets window.kbBrowserMapModel)
 *   6. map-view-state.js     (sets window.kbMapViewState)
 *   7. map-*.js helper modules (sets window.kbMap...)
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
      'Run <code>python knowledge_base/map/generate_map_data.py</code> from the repo root first.</p>';
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
    typeof window.kbMapViewState.createMapViewState !== 'function' ||
    !window.kbMapRendering ||
    typeof window.kbMapRendering.createMapRendering !== 'function' ||
    !window.kbMapRelevanceFilter ||
    typeof window.kbMapRelevanceFilter.createMapRelevanceFilter !== 'function' ||
    !window.kbMapOverlays ||
    typeof window.kbMapOverlays.createMapOverlays !== 'function' ||
    !window.kbMapCamera ||
    typeof window.kbMapCamera.createMapCamera !== 'function' ||
    !window.kbMapBranchFilter ||
    typeof window.kbMapBranchFilter.createMapBranchFilter !== 'function'
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
    defaultRelevanceSimilarity: window.kbMapRelevanceFilter.DEFAULT_RELEVANCE_SIMILARITY,
    relevanceFilter: {
      treeProximity: null,
    },
  });
  let mapRendering = null;
  let mapRelevanceFilter = null;
  let mapOverlays = null;
  let mapCamera = null;
  let mapBranchFilter = null;
  let theme = null;
  let activeLevelTransition = null;
  let lastLevelTransitionMetrics = null;
  let cachedPaperNodeRadius = PAPER_NODE_RADIUS_TARGET;
  let visibilityColorContext = null;
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

  function initializeMapModules() {
    mapRendering = window.kbMapRendering.createMapRendering({
      clamp,
      viewState,
      getGraph: () => graph,
      getRenderer: () => renderer,
      currentNodeRadius,
      aggregateNodeSize,
      detailLevels: DETAIL_LEVELS,
      detailLevelZIndex,
      mobileViewport,
      nodeGhostVisible,
      nodeVisible,
      paperNodeRadiusTarget: PAPER_NODE_RADIUS_TARGET,
      minNodeScreenRadius: MIN_NODE_SCREEN_RADIUS,
      mobileMinNodeScreenRadius: MOBILE_MIN_NODE_SCREEN_RADIUS,
      minNodeScreenRadiusBlendRatio: MIN_NODE_SCREEN_RADIUS_BLEND_RATIO,
    });
    theme = mapRendering.theme();

    mapRelevanceFilter = window.kbMapRelevanceFilter.createMapRelevanceFilter({
      data: DATA,
      mapModel,
      viewState,
      clamp,
      paperIdForNode,
      refreshView,
    });

    mapOverlays = window.kbMapOverlays.createMapOverlays({
      graphContainer,
      viewState,
      getGraph: () => graph,
      getRenderer: () => renderer,
      graphHasNode,
      nodeVisible,
      nodeDisplaySize,
      minimumNodeScreenRadius,
      mobileViewport,
      detailLevelLabel,
      detailLevels: DETAIL_LEVELS,
      escHtml,
      setSelectedNodeFilterEnabled,
      syncUrlToPinnedNode,
      refreshView,
    });

    mapCamera = window.kbMapCamera.createMapCamera({
      graphContainer,
      viewState,
      clamp,
      getGraph: () => graph,
      getRenderer: () => renderer,
      graphHasNode,
      nodeVisible,
      nodeAllowedByFilters,
      nodeDisplaySize,
      homePoint,
      currentNodeLabelMetrics,
      nodeLabelZoomScaleForRatio,
      hierarchyLevelById: HIERARCHY_LEVEL_BY_ID,
      finishLevelTransition,
      setSelectedNodeFilterEnabled,
      hideHoverTooltip,
      hideTooltip,
      hidePaperModal,
      refreshView,
      updateDetailButtons,
      selectBranchForPaper,
      showFocusedPaperTooltip,
      viewportPadding: VIEWPORT_PADDING,
      panelMaxFocusWidthRatio: PANEL_MAX_FOCUS_WIDTH_RATIO,
      focusedPaperCameraRatio: FOCUSED_PAPER_CAMERA_RATIO,
      minCameraRatio: MIN_CAMERA_RATIO,
      maxZoomOutOverscanRatio: MAX_ZOOM_OUT_OVERSCAN_RATIO,
    });

    mapBranchFilter = window.kbMapBranchFilter.createMapBranchFilter({
      mapModel,
      viewState,
      branchFilterAll: BRANCH_FILTER_ALL,
      paperPrefix: BRANCH_FILTER_PAPER_PREFIX,
      clearHoverClickNode,
      nextDetailLevel,
      applyDetailLevel,
      applyCategoryFilter,
      detailLevelForActiveBranch,
      updateDetailButtons,
      graphHasNode,
      setSelectedNodeFilterEnabled,
      hideHoverTooltip,
      refreshView,
      focusCameraOnNode,
      showFocusedPaperTooltip,
      writeFocusPaperId,
    });
  }

  function currentNodeRadius() {
    return cachedPaperNodeRadius;
  }

  function currentVisibilityPalette() {
    return mapRendering.currentVisibilityPalette();
  }

  function nodeSizeWithMinimumScreenRadius(size) {
    return mapRendering.nodeSizeWithMinimumScreenRadius(size);
  }

  function minimumNodeScreenRadius() {
    return mapRendering.minimumNodeScreenRadius();
  }

  function nodeLabelZoomScaleForRatio(ratio) {
    return mapRendering.nodeLabelZoomScaleForRatio(ratio);
  }

  function currentNodeLabelMetrics(data, zoomScale) {
    return mapRendering.currentNodeLabelMetrics(data, zoomScale);
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

  function precomputeNodeLabelMetrics(nodeSpecs) {
    return mapRendering.precomputeNodeLabelMetrics(nodeSpecs);
  }

  function nodeDisplaySize(attrs) {
    return mapRendering.nodeDisplaySize(attrs);
  }

  function formatLabel(label) {
    return mapRendering.formatLabel(label);
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
      if (mapRelevanceFilter) mapRelevanceFilter.invalidate();
      if (relevanceFilterActive()) refreshView();
    },
  });

  initializeMapModules();

  function relevanceFilterActive() {
    return mapRelevanceFilter ? mapRelevanceFilter.active() : false;
  }

  function setSelectedNodeFilterEnabled(enabled) {
    if (mapRelevanceFilter) mapRelevanceFilter.setSelectedNodeFilterEnabled(enabled);
  }

  function paperAllowedByCurrentFilters(attrs) {
    return mapRelevanceFilter ? mapRelevanceFilter.paperAllowedByCurrentFilters(attrs) : false;
  }

  function nodeAllowedByRelevance(attrs) {
    return mapRelevanceFilter ? mapRelevanceFilter.nodeAllowedByRelevance(attrs) : true;
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
    const renderingConstants = mapRendering.constants;
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
        type: borderedNodeProgramSupported() ? renderingConstants.BORDERED_NODE_TYPE : 'circle',
        color,
        borderColor: theme.nodeBorder,
        baseColor: color,
        staticBaseColor: color,
        label: formatLabel(attrs.label),
        fullLabel: attrs.fullLabel || attrs.label,
        labelFontSize: labelMetrics.fontSize || renderingConstants.NODE_LABEL_FONT_SIZE,
        labelLineHeight: labelMetrics.lineHeight ||
          (renderingConstants.NODE_LABEL_FONT_SIZE * renderingConstants.NODE_LABEL_LINE_HEIGHT_RATIO),
        labelSourceDiskDiameter: labelMetrics.sourceDiskDiameter || (PAPER_NODE_RADIUS_TARGET * 2),
        count: attrs.count || 1,
        labelColor: mapRendering.accessibleNodeLabelColor(color),
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
    return mapRendering.nodeReducer(node, attrs);
  }

  function drawNodeHover(context, data) {
    return mapRendering.drawNodeHover(context, data);
  }

  function drawNodeLabelNoop() {
    return mapRendering.drawNodeLabelNoop();
  }

  function borderedNodeProgramSupported() {
    return mapRendering.borderedNodeProgramSupported();
  }

  function nodeProgramClasses() {
    return mapRendering.nodeProgramClasses();
  }

  function setupTopLabelOverlay() {
    return mapRendering.setupTopLabelOverlay();
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
    const renderingConstants = mapRendering.constants;

    try {
      renderer = new window.Sigma(graph, graphContainer, {
        minCameraRatio: MIN_CAMERA_RATIO,
        maxCameraRatio: FALLBACK_MAX_CAMERA_RATIO,
        zIndex: true,
        hideLabelsOnMove: false,
        renderLabels: true,
        enableCameraRotation: false,
        labelRenderedSizeThreshold: renderingConstants.LABEL_RENDERED_SIZE_THRESHOLD,
        labelDensity: renderingConstants.LABEL_DENSITY,
        labelGridCellSize: renderingConstants.LABEL_GRID_CELL_SIZE,
        labelFont: '"Atkinson Hyperlegible Next", "Segoe UI", sans-serif',
        labelSize: renderingConstants.NODE_LABEL_FONT_SIZE,
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
        mapRendering.invalidateGraphToViewportRatio();
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
  function mobileViewport() {
    return window.matchMedia && window.matchMedia('(max-width: 700px)').matches;
  }

  function nodeTooltipPosition(node) {
    return mapOverlays ? mapOverlays.nodeTooltipPosition(node) : null;
  }

  function showNodeTooltip(node, pos, pinned) {
    if (mapOverlays) mapOverlays.showNodeTooltip(node, pos, pinned);
  }

  function showHoverTooltip(node) {
    if (mapOverlays) mapOverlays.showHoverTooltip(node);
  }

  function hideHoverTooltip() {
    if (mapOverlays) mapOverlays.hideHoverTooltip();
  }

  function updateActiveTooltipPositions() {
    if (mapOverlays) mapOverlays.updateActiveTooltipPositions();
  }

  function hideTooltip() {
    if (mapOverlays) mapOverlays.hideTooltip();
  }

  function hidePaperModal() {
    if (mapOverlays) mapOverlays.hidePaperModal();
  }

  function closePaperModalSelection() {
    if (mapOverlays) mapOverlays.closePaperModalSelection();
  }

  function showFocusedPaperTooltip(node) {
    if (mapOverlays) mapOverlays.showFocusedPaperTooltip(node);
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
    if (mapRelevanceFilter) mapRelevanceFilter.apply();
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
    return mapRelevanceFilter ? mapRelevanceFilter.relevantPaperCount() : DATA.nodes.length;
  }

  function updateRelevancePanel() {
    if (mapRelevanceFilter) mapRelevanceFilter.updatePanel();
  }

  /* -------------------------------------------------------------------------
   * Fit to visible graph, leaving space for the overlay panel when open.
   * -------------------------------------------------------------------------*/
  function fitVisible(duration) {
    if (mapCamera) mapCamera.fitVisible(duration);
  }

  function updateZoomOutLimit(minAllowedRatio = 0) {
    if (mapCamera) mapCamera.updateZoomOutLimit(minAllowedRatio);
  }

  function minimumVisibleGraphDistance() {
    return mapCamera ? mapCamera.minimumVisibleGraphDistance() : Infinity;
  }

  function minimumVisiblePaperGraphDistance() {
    return mapCamera ? mapCamera.minimumVisiblePaperGraphDistance() : Infinity;
  }

  function minimumVisibleScreenDistance(cameraState) {
    return mapCamera ? mapCamera.minimumVisibleScreenDistance(cameraState) : Infinity;
  }

  function labelTextHalfExtents(attrs, cameraState) {
    return mapCamera ? mapCamera.labelTextHalfExtents(attrs, cameraState) : { width: 0, height: 0 };
  }

  function focusCameraOnNode(node, duration) {
    if (mapCamera) mapCamera.focusCameraOnNode(node, duration);
  }

  function refocusPinnedPaper(duration) {
    return mapCamera ? mapCamera.refocusPinnedPaper(duration) : false;
  }

  function focusPaperFromHash() {
    return mapCamera ? mapCamera.focusPaperFromHash() : false;
  }

  function syncPaperFocusFromHash() {
    return mapCamera ? mapCamera.syncPaperFocusFromHash() : false;
  }

  function readFocusPaperId() {
    return mapCamera ? mapCamera.readFocusPaperId() : null;
  }

  function writeFocusPaperId(paperId) {
    if (mapCamera) mapCamera.writeFocusPaperId(paperId);
  }

  function paperIdForNode(node) {
    return mapCamera ? mapCamera.paperIdForNode(node) : null;
  }

  function syncUrlToPinnedNode() {
    if (mapCamera) mapCamera.syncUrlToPinnedNode();
  }

  /* -------------------------------------------------------------------------
   * Category filter panel
   * -------------------------------------------------------------------------*/
  function activateBranchNode(attrs, node) {
    if (mapBranchFilter) mapBranchFilter.activateBranchNode(attrs, node);
  }

  function setActiveBranchFilter(key) {
    if (mapBranchFilter) mapBranchFilter.setActiveBranchFilter(key);
  }

  function selectBranchForPaper(attrs) {
    if (mapBranchFilter) mapBranchFilter.selectBranchForPaper(attrs);
  }

  function buildCategoryFilters(selectedKey) {
    if (mapBranchFilter) mapBranchFilter.buildCategoryFilters(selectedKey);
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
    if (mapRelevanceFilter) mapRelevanceFilter.syncControlValues();
  }

  function setupRelevanceControls() {
    if (mapRelevanceFilter) mapRelevanceFilter.setupControls();
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

    if (mapOverlays) mapOverlays.setupModalControls();
  }

  /* -------------------------------------------------------------------------
   * Bootstrap
   * -------------------------------------------------------------------------*/
  buildCategoryFilters();
  setupControls();
  initSigma();

  const themeObserver = new MutationObserver(() => {
    theme = mapRendering.refreshTheme();
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
      if (mapRelevanceFilter) mapRelevanceFilter.setFilter(patch);
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
