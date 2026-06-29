/* browser/relevance-filter.js - semantic and Tree relevance filtering for the map. */

'use strict';

(function () {
  const DEFAULT_RELEVANCE_SIMILARITY = 0.79;
  const DEFAULT_RELEVANCE_TREE_PROXIMITY = 0.79;
  const RELEVANCE_SLIDER_EXPANDED_THRESHOLD = 0.70;
  const RELEVANCE_SLIDER_EXPANDED_POSITION = 0.20;
  const RELEVANCE_SLIDER_EXPONENT = Math.log(1 - RELEVANCE_SLIDER_EXPANDED_THRESHOLD) /
    Math.log(1 - RELEVANCE_SLIDER_EXPANDED_POSITION);

  function createMapRelevanceFilter(deps = {}) {
    const data = deps.data || { nodes: [] };
    const mapModel = deps.mapModel;
    const viewState = deps.viewState;
    const clamp = deps.clamp || ((value, min, max) => Math.max(min, Math.min(value, max)));
    let evaluationCache = null;
    let refreshFrame = null;

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

    function selectedEgo() {
      const paperId = typeof deps.paperIdForNode === 'function'
        ? deps.paperIdForNode(viewState.pinnedNode)
        : null;
      return paperId && mapModel.paper(paperId) ? paperId : null;
    }

    function active() {
      return viewState.relevanceFilter.enabled && Boolean(selectedEgo());
    }

    function invalidate() {
      evaluationCache = null;
    }

    function setSelectedNodeFilterEnabled(enabled) {
      const nextEnabled = Boolean(enabled);
      if (viewState.relevanceFilter.enabled === nextEnabled) return;

      viewState.relevanceFilter.enabled = nextEnabled;
      syncControlValues();
    }

    function treeThreshold() {
      return Number.isFinite(viewState.relevanceFilter.treeProximity)
        ? viewState.relevanceFilter.treeProximity
        : defaultTreeProximity();
    }

    function evaluationKey(egoId, threshold) {
      if (!viewState.relevanceFilter.enabled || !egoId) return 'off';

      return [
        egoId,
        viewState.relevanceFilter.semantic ? 1 : 0,
        viewState.relevanceFilter.taxonomy ? 1 : 0,
        viewState.relevanceFilter.mode,
        viewState.relevanceFilter.similarity,
        threshold,
      ].join('|');
    }

    function metricAllowed(metric, egoId, threshold) {
      if (metric.paperId === egoId) return true;

      const semanticEnabled = viewState.relevanceFilter.semantic;
      const taxonomyEnabled = viewState.relevanceFilter.taxonomy;
      if (!semanticEnabled && !taxonomyEnabled) return true;

      const semanticPass = !semanticEnabled || metric.semantic >= viewState.relevanceFilter.similarity;
      const taxonomyPass = !taxonomyEnabled || metric.treeProximity >= threshold;

      return viewState.relevanceFilter.mode === 'or'
        ? semanticPass || taxonomyPass
        : semanticPass && taxonomyPass;
    }

    function evaluation() {
      const egoId = selectedEgo();
      if (!viewState.relevanceFilter.enabled || !egoId) {
        return {
          active: false,
          allowedPaperIds: null,
          count: data.nodes.length,
        };
      }

      const threshold = treeThreshold();
      const key = evaluationKey(egoId, threshold);
      if (evaluationCache && evaluationCache.key === key) {
        return evaluationCache;
      }

      const allowedPaperIds = new Set();
      mapModel.relevanceMetrics(egoId).forEach(metric => {
        if (metricAllowed(metric, egoId, threshold)) {
          allowedPaperIds.add(metric.paperId);
        }
      });

      evaluationCache = {
        key,
        active: true,
        allowedPaperIds,
        count: allowedPaperIds.size,
      };
      return evaluationCache;
    }

    function paperAllowedByRelevance(paperId) {
      const result = evaluation();
      return !result.active || result.allowedPaperIds.has(paperId);
    }

    function paperAllowedByCurrentFilters(attrs) {
      if (!attrs || !paperAllowedByRelevance(attrs.id)) return false;
      return viewState.activeCategories.has(mapModel.nodeKey(attrs));
    }

    function nodeAllowedByRelevance(attrs) {
      if (!active()) return true;
      const result = evaluation();
      if (!result.active) return true;

      if (attrs.kind === 'aggregate') {
        return (attrs.leafIds || []).some(paperId => result.allowedPaperIds.has(paperId));
      }
      return result.allowedPaperIds.has(attrs.id);
    }

    function relevantPaperCount() {
      return evaluation().count;
    }

    function updatePanel() {
      const panel = document.getElementById('mm-relevance-panel');
      if (!panel) return;

      const egoId = selectedEgo();
      panel.hidden = !egoId;
      if (!egoId) return;

      const ego = mapModel.paper(egoId) || {};
      const title = document.getElementById('mm-relevance-ego');
      const count = document.getElementById('mm-relevance-match-count');
      const status = document.getElementById('mm-relevance-status');

      if (title) title.textContent = ego.title || ego.label || egoId;
      if (count) count.textContent = `${relevantPaperCount()} / ${data.nodes.length}`;
      if (status) {
        status.textContent = viewState.relevanceFilter.enabled
          ? `${viewState.relevanceFilter.mode.toUpperCase()} filter active`
          : 'Filter off';
      }
    }

    function syncControlValues() {
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
      updatePanel();
    }

    function apply() {
      if (refreshFrame !== null) return;

      refreshFrame = window.requestAnimationFrame(() => {
        refreshFrame = null;
        invalidate();
        if (typeof deps.refreshView === 'function') deps.refreshView();
      });
    }

    function setupControls() {
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
        apply();
      });
      semantic.addEventListener('change', () => {
        viewState.relevanceFilter.semantic = semantic.checked;
        apply();
      });
      taxonomy.addEventListener('change', () => {
        viewState.relevanceFilter.taxonomy = taxonomy.checked;
        apply();
      });
      mode.addEventListener('change', () => {
        viewState.relevanceFilter.mode = mode.value === 'or' ? 'or' : 'and';
        apply();
      });
      simSlider.addEventListener('input', () => {
        viewState.relevanceFilter.similarity = relevanceSliderValueToThreshold(simSlider.value);
        if (simVal) simVal.textContent = relevanceSliderValueLabel(simSlider.value);
        apply();
      });
      treeSlider.addEventListener('input', () => {
        viewState.relevanceFilter.treeProximity = relevanceSliderValueToThreshold(treeSlider.value);
        if (treeVal) treeVal.textContent = relevanceSliderValueLabel(treeSlider.value);
        apply();
      });

      syncControlValues();
    }

    function setFilter(patch) {
      viewState.relevanceFilter = { ...viewState.relevanceFilter, ...(patch || {}) };
      invalidate();
      syncControlValues();
      if (typeof deps.refreshView === 'function') deps.refreshView();
    }

    return {
      active,
      apply,
      evaluation,
      invalidate,
      nodeAllowedByRelevance,
      paperAllowedByCurrentFilters,
      paperAllowedByRelevance,
      relevantPaperCount,
      selectedEgo,
      setFilter,
      setSelectedNodeFilterEnabled,
      setupControls,
      syncControlValues,
      treeThreshold,
      updatePanel,
    };
  }

  window.kbMapRelevanceFilter = {
    DEFAULT_RELEVANCE_SIMILARITY,
    DEFAULT_RELEVANCE_TREE_PROXIMITY,
    createMapRelevanceFilter,
  };
}());
