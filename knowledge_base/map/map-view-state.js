/* map-view-state.js - mutable browser view state for the paper map. */

'use strict';

(function () {
  function createMapViewState(options = {}) {
    const branchFilterAll = options.branchFilterAll || '__all__';
    let currentDetailLevel = options.initialDetailLevel || 'paper';
    let activeCategories = new Set();
    let activeBranchFilterKey = branchFilterAll;
    let branchFilterGroups = new Map();
    let relevanceFilter = {
      enabled: false,
      semantic: true,
      taxonomy: true,
      mode: 'and',
      similarity: Number(options.defaultRelevanceSimilarity || 0),
      treeProximity: null,
      ...(options.relevanceFilter || {}),
    };
    let showNodeLabels = options.showNodeLabels !== false;
    let pinnedNode = null;
    let hoveredNode = null;
    let hoverClickNode = null;
    let hoverTooltipNode = null;
    let focus = emptyFocus();
    let visibleNodes = null;
    let visibleNodeCount = 0;
    let visibleNodeList = [];

    function emptyFocus() {
      return { active: false, nodes: new Set(), mode: null };
    }

    function setVisibleNodes(nodes, list = null) {
      visibleNodes = nodes || null;
      visibleNodeList = list ? [...list] : (nodes ? [...nodes] : []);
      visibleNodeCount = nodes ? nodes.size : 0;
    }

    function clearVisibleNodes() {
      setVisibleNodes(null, []);
    }

    function setFocus(nodes, mode) {
      const focusedNodes = nodes || new Set();
      focus = {
        active: focusedNodes.size > 0,
        nodes: focusedNodes,
        mode,
      };
    }

    function clearFocus() {
      focus = emptyFocus();
    }

    function clearSelection() {
      pinnedNode = null;
      hoveredNode = null;
    }

    function selectNode(node) {
      pinnedNode = node || null;
      hoveredNode = null;
    }

    function relevanceSnapshot() {
      return { ...relevanceFilter };
    }

    const state = {
      setVisibleNodes,
      clearVisibleNodes,
      setFocus,
      clearFocus,
      clearSelection,
      selectNode,
      relevanceSnapshot,
    };

    Object.defineProperties(state, {
      currentDetailLevel: {
        get: () => currentDetailLevel,
        set: value => { currentDetailLevel = value; },
      },
      activeCategories: {
        get: () => activeCategories,
        set: value => { activeCategories = value instanceof Set ? value : new Set(value || []); },
      },
      activeBranchFilterKey: {
        get: () => activeBranchFilterKey,
        set: value => { activeBranchFilterKey = value || branchFilterAll; },
      },
      branchFilterGroups: {
        get: () => branchFilterGroups,
        set: value => { branchFilterGroups = value instanceof Map ? value : new Map(value || []); },
      },
      relevanceFilter: {
        get: () => relevanceFilter,
        set: value => { relevanceFilter = { ...relevanceFilter, ...(value || {}) }; },
      },
      showNodeLabels: {
        get: () => showNodeLabels,
        set: value => { showNodeLabels = Boolean(value); },
      },
      pinnedNode: {
        get: () => pinnedNode,
        set: value => { pinnedNode = value || null; },
      },
      hoveredNode: {
        get: () => hoveredNode,
        set: value => { hoveredNode = value || null; },
      },
      hoverClickNode: {
        get: () => hoverClickNode,
        set: value => { hoverClickNode = value || null; },
      },
      hoverTooltipNode: {
        get: () => hoverTooltipNode,
        set: value => { hoverTooltipNode = value || null; },
      },
      focus: {
        get: () => focus,
        set: value => { focus = value && value.nodes ? value : emptyFocus(); },
      },
      visibleNodes: {
        get: () => visibleNodes,
        set: value => { setVisibleNodes(value, value ? [...value] : []); },
      },
      visibleNodeCount: {
        get: () => visibleNodeCount,
        set: value => { visibleNodeCount = Math.max(0, Number(value) || 0); },
      },
      visibleNodeList: {
        get: () => visibleNodeList,
        set: value => { visibleNodeList = Array.isArray(value) ? value : []; },
      },
    });

    return state;
  }

  window.kbMapViewState = {
    createMapViewState,
  };
}());
