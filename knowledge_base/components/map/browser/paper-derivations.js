/* browser/paper-derivations.js - derived paper fields for the browser map. */

'use strict';

(function () {
  function clamp(value, min, max) {
    return Math.min(Math.max(value, min), max);
  }

  function createMapPaperDerivations(options = {}) {
    const uncategorizedCategory = options.uncategorizedCategory || 'Uncategorized';
    const paperSuperCategory = typeof options.paperSuperCategory === 'function'
      ? options.paperSuperCategory
      : attrs => attrs.super_category || attrs.category || uncategorizedCategory;
    const aggregateLevelCount = typeof options.aggregateLevelCount === 'function'
      ? options.aggregateLevelCount
      : () => Number(options.aggregateLevelCount || 0);

    function navPathFilterKey(path) {
      return `path:${JSON.stringify((path || []).map(part => String(part || '')))}`;
    }

    function paperNavPath(attrs) {
      if (!attrs) return [uncategorizedCategory];
      if (attrs._mmNavPath) return attrs._mmNavPath;

      const rawPath = Array.isArray(attrs.nav_path)
        ? attrs.nav_path
        : [paperSuperCategory(attrs), attrs.category, attrs.sub_category].filter(Boolean);
      const path = rawPath.map(part => String(part || '').trim()).filter(Boolean);
      attrs._mmNavPath = path.length ? path : [uncategorizedCategory];
      return attrs._mmNavPath;
    }

    function paddedPaperNavPath(attrs) {
      if (attrs && attrs._mmPaddedNavPath) return attrs._mmPaddedNavPath.slice();

      const path = paperNavPath(attrs);
      const branchDepth = Math.max(0, Number(aggregateLevelCount()) || 0);
      if (!branchDepth) return path.slice();

      const fallback = path[path.length - 1] || uncategorizedCategory;
      const padded = path.slice();

      while (padded.length < branchDepth) {
        padded.push(fallback);
      }

      if (attrs) attrs._mmPaddedNavPath = padded.slice(0, branchDepth);
      return padded.slice(0, branchDepth);
    }

    function paperFilterKey(attrs) {
      if (!attrs) return navPathFilterKey([uncategorizedCategory]);
      if (attrs._mmFilterKey) return attrs._mmFilterKey;
      if (attrs.filterKey) return attrs.filterKey;
      attrs._mmFilterKey = navPathFilterKey(paperNavPath(attrs));
      return attrs._mmFilterKey;
    }

    function nodeKey(attrs) {
      if (!attrs) return navPathFilterKey([uncategorizedCategory]);
      return attrs._mmFilterKey || attrs.filterKey || paperFilterKey(attrs);
    }

    function itemTypeKey(attrs) {
      if (!attrs) return 'Unspecified';
      if (attrs._mmItemType) return attrs._mmItemType;
      attrs._mmItemType = attrs.item_type || attrs.type || 'Unspecified';
      return attrs._mmItemType;
    }

    function paperSearchText(attrs) {
      if (!attrs) return '';
      if (attrs._mmSearchText) return attrs._mmSearchText;
      attrs._mmSearchText = [
        attrs.title,
        attrs.label,
        attrs.category,
        attrs.sub_category,
        attrs.super_category,
        itemTypeKey(attrs),
        ...(attrs.tags || []),
        attrs.summary,
      ].filter(Boolean).join(' ').toLowerCase();
      return attrs._mmSearchText;
    }

    function quantile(values, q) {
      const sorted = values
        .filter(value => Number.isFinite(value))
        .sort((a, b) => a - b);
      if (!sorted.length) return null;
      if (sorted.length === 1) return sorted[0];

      const index = clamp(q, 0, 1) * (sorted.length - 1);
      const lower = Math.floor(index);
      const upper = Math.ceil(index);
      const t = index - lower;
      return sorted[lower] * (1 - t) + sorted[upper] * t;
    }

    return {
      clamp,
      navPathFilterKey,
      paperFilterKey,
      nodeKey,
      itemTypeKey,
      paperNavPath,
      paddedPaperNavPath,
      paperSearchText,
      quantile,
    };
  }

  window.kbMapPaperDerivations = {
    createMapPaperDerivations,
    clamp,
  };
}());
