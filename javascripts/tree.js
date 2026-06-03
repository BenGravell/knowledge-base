'use strict';

(function () {
  const app = document.getElementById('ct-app');
  if (!app) return;

  const data = window.treeData;
  const settings = document.getElementById('ct-settings');
  const settingsToggle = document.getElementById('ct-settings-toggle');
  const settingsState = document.getElementById('ct-settings-state');
  const searchInput = document.getElementById('ct-search');
  const itemTypeTrigger = document.getElementById('ct-item-type-trigger');
  const itemTypeDialog = document.getElementById('ct-item-type-dialog');
  const itemTypeClose = document.getElementById('ct-item-type-close');
  const itemTypeButtons = document.getElementById('ct-item-type');
  const itemTypeAllButton = document.getElementById('ct-all-types');
  const itemTypeNoneButton = document.getElementById('ct-no-types');
  const itemTypeSummary = document.getElementById('ct-item-type-summary');
  const yearStartInput = document.getElementById('ct-year-start');
  const yearEndInput = document.getElementById('ct-year-end');
  const resetButton = document.getElementById('ct-reset');
  const searchResults = document.getElementById('ct-search-results');
  const ancestorChain = document.getElementById('ct-ancestor-chain');
  const selectionDetails = document.getElementById('ct-selection-details');
  const sunburst = document.getElementById('ct-sunburst');
  const sunburstStage = document.getElementById('ct-sunburst-stage') || sunburst;
  const sunburstRootButton = document.getElementById('ct-sunburst-root');
  const focusCoreSingleColumnQuery = '(max-width: 720px)';
  const focusCoreSingleColumn = typeof window.matchMedia === 'function'
    ? window.matchMedia(focusCoreSingleColumnQuery)
    : { matches: false };

  if (!data || !data.root) {
    app.innerHTML = '<p class="ct-error">Tree data is unavailable. Run <code>mkdocs build</code> to regenerate it.</p>';
    return;
  }

  const nodes = new Map();
  const paperNodes = new Map();
  const searchableNodes = [];
  const sunburstLayoutCache = new Map();
  const sunburstLayoutCacheLimit = 36;
  let currentId = data.root.id;
  let lastMatches = [];
  let filterMemo = new Map();
  let currentFilterKey = 'all';
  let currentFilterTerms = [];
  let currentFiltersActive = false;
  let sunburstAnimationFrame = 0;
  let sunburstAnimationToken = 0;
  let lastSunburstSnapshot = null;
  let currentSunburstColors = new Map();
  let previewTargetsByNodeId = new Map();
  let sunburstPreviewTargets = [];
  let sunburstHitTargetPreviewTargets = [];
  let activePreviewClasses = [];
  let previewNodeId = null;
  let hydrateIndex = 0;
  const state = {
    query: '',
    yearStart: null,
    yearEnd: null,
    itemTypes: new Set(),
    noItemTypes: false,
  };
  const sunburstPaletteVars = [
    '--kb-map-node-color-1',
    '--kb-map-node-color-2',
    '--kb-map-node-color-3',
    '--kb-map-node-color-4',
    '--kb-map-node-color-5',
    '--kb-map-node-color-6',
    '--kb-map-node-color-7',
    '--kb-map-node-color-8',
    '--kb-map-node-color-9',
    '--kb-map-node-color-10',
    '--kb-map-node-color-11',
    '--kb-map-node-color-12',
  ];
  const sunburstLabelFontSize = 10;
  const sunburstCenterCircleRadius = 58;
  const sunburstCenterRadius = 64;
  const sunburstCenterLabelMaxChars = 15;
  const sunburstCenterLabelMaxLines = 3;

  hydrate(data.root, null, 0);
  const paperYears = searchableNodes
    .map(function (node) { return paperYear(node); })
    .filter(Number.isInteger);
  const minYear = paperYears.length ? Math.min.apply(null, paperYears) : null;
  const maxYear = paperYears.length ? Math.max.apply(null, paperYears) : null;
  const itemTypes = Array.from(new Set(searchableNodes
    .filter(function (node) { return node.kind === 'paper'; })
    .map(function (node) { return paperType(node); })
    .filter(Boolean))).sort(function (a, b) { return a.localeCompare(b); });
  const itemTypeCounts = itemTypes.reduce(function (counts, type) {
    counts.set(type, 0);
    return counts;
  }, new Map());
  searchableNodes.forEach(function (node) {
    if (node.kind !== 'paper') return;
    const type = paperType(node);
    itemTypeCounts.set(type, (itemTypeCounts.get(type) || 0) + 1);
  });

  state.yearStart = minYear;
  state.yearEnd = maxYear;
  initControls();

  const initialId = readHashId();
  currentId = initialId && nodes.has(initialId) ? initialId : data.root.id;
  render();

  app.addEventListener('click', function (event) {
    const target = event.target.closest('[data-ct-select]');
    if (!target || !app.contains(target)) return;
    event.preventDefault();
    selectNode(target.getAttribute('data-ct-select'), {
      centerTree: Boolean(target.closest('#ct-search-results')),
      animateSunburst: true,
    });
  });

  app.addEventListener('keydown', function (event) {
    if (event.key !== 'Enter' && event.key !== ' ') return;
    const target = event.target.closest('[data-ct-select]');
    if (!target || !app.contains(target)) return;
    event.preventDefault();
    selectNode(target.getAttribute('data-ct-select'), {
      centerTree: Boolean(target.closest('#ct-search-results')),
      animateSunburst: true,
    });
  });

  app.addEventListener('pointerover', function (event) {
    const target = event.target.closest('[data-ct-preview-node]');
    if (!target || !app.contains(target) || eventTargetContains(target, event.relatedTarget)) return;
    setPreviewNode(target.getAttribute('data-ct-preview-node'));
  });

  app.addEventListener('pointerout', function (event) {
    const target = event.target.closest('[data-ct-preview-node]');
    if (!target || !app.contains(target) || eventTargetContains(target, event.relatedTarget)) return;
    clearPreviewNode();
  });

  app.addEventListener('focusin', function (event) {
    const target = event.target.closest('[data-ct-preview-node]');
    if (!target || !app.contains(target)) return;
    setPreviewNode(target.getAttribute('data-ct-preview-node'));
  });

  app.addEventListener('focusout', function (event) {
    const target = event.target.closest('[data-ct-preview-node]');
    if (!target || !app.contains(target)) return;
    clearPreviewNode();
  });

  if (sunburstRootButton) {
    sunburstRootButton.addEventListener('click', function () {
      selectNode(data.root.id, { animateSunburst: true });
    });
  }

  if (settingsToggle && settings) {
    settingsToggle.addEventListener('click', function () {
      const collapsed = settings.classList.toggle('is-collapsed');
      settingsToggle.setAttribute('aria-expanded', String(!collapsed));
      updateSettingsState();
    });
  }

  if (searchInput) {
    searchInput.addEventListener('input', function () {
      state.query = searchInput.value.trim();
      render();
    });
  }

  if (yearStartInput) yearStartInput.addEventListener('change', syncYearInputs);
  if (yearEndInput) yearEndInput.addEventListener('change', syncYearInputs);

  if (itemTypeTrigger && itemTypeDialog) {
    itemTypeTrigger.addEventListener('click', function () {
      openItemTypeDialog();
    });
  }

  if (itemTypeClose) {
    itemTypeClose.addEventListener('click', closeItemTypeDialog);
  }

  if (itemTypeDialog) {
    itemTypeDialog.addEventListener('click', function (event) {
      if (event.target === itemTypeDialog) closeItemTypeDialog();
    });
    itemTypeDialog.addEventListener('close', function () {
      if (itemTypeTrigger) {
        itemTypeTrigger.setAttribute('aria-expanded', 'false');
        itemTypeTrigger.focus();
      }
    });
  }

  if (itemTypeButtons) {
    itemTypeButtons.addEventListener('click', function (event) {
      const button = event.target.closest('[data-ct-item-type]');
      if (!button || !itemTypeButtons.contains(button)) return;
      const type = button.getAttribute('data-ct-item-type') || '';

      if (allItemTypesSelected()) {
        state.itemTypes = new Set(itemTypes.filter(function (candidate) { return candidate !== type; }));
        state.noItemTypes = state.itemTypes.size === 0;
      } else if (state.itemTypes.has(type)) {
        state.itemTypes.delete(type);
        state.noItemTypes = state.itemTypes.size === 0;
      } else {
        state.noItemTypes = false;
        state.itemTypes.add(type);
      }
      updateFilterControls();
      render();
    });
  }

  if (itemTypeAllButton) {
    itemTypeAllButton.addEventListener('click', function () {
      state.itemTypes.clear();
      state.noItemTypes = false;
      updateFilterControls();
      render();
    });
  }

  if (itemTypeNoneButton) {
    itemTypeNoneButton.addEventListener('click', function () {
      state.itemTypes.clear();
      state.noItemTypes = true;
      updateFilterControls();
      render();
    });
  }

  if (resetButton) {
    resetButton.addEventListener('click', function () {
      state.query = '';
      state.yearStart = minYear;
      state.yearEnd = maxYear;
      state.itemTypes.clear();
      state.noItemTypes = false;
      if (searchInput) searchInput.value = '';
      updateFilterControls();
      render();
    });
  }

  window.addEventListener('popstate', function () {
    const hashId = readHashId();
    if (hashId && nodes.has(hashId)) {
      currentId = hashId;
      render();
    }
  });

  if (typeof focusCoreSingleColumn.addEventListener === 'function') {
    focusCoreSingleColumn.addEventListener('change', render);
  } else if (typeof focusCoreSingleColumn.addListener === 'function') {
    focusCoreSingleColumn.addListener(render);
  }

  function hydrate(node, parent, siblingIndex) {
    const paper = node.paper || {};
    const authors = Array.isArray(paper.authors) ? paper.authors.join(' ') : '';
    node.parent = parent;
    node.siblingIndex = Number.isInteger(siblingIndex) ? siblingIndex : 0;
    node.children = Array.isArray(node.children) ? node.children : [];
    node.pathNodes = parent ? parent.pathNodes.concat(node) : [node];
    node.searchText = normalized([node.label, node.path.join(' '), node.source || '', authors, paper.year || '', paper.type || '', paper.sourceName || ''].join(' '));
    node.preorderStart = hydrateIndex;
    hydrateIndex += 1;
    nodes.set(node.id, node);
    if (node.kind === 'paper') {
      const paperId = paper.id || paperIdFromSource(node.source);
      if (paperId) paperNodes.set(String(paperId), node.id);
    }
    searchableNodes.push(node);
    let totalLeafCount = node.kind === 'paper' ? 1 : 0;
    let subtreeDepth = 0;
    node.children.forEach(function (child, index) {
      const childStats = hydrate(child, node, index);
      totalLeafCount += childStats.leafCount;
      subtreeDepth = Math.max(subtreeDepth, childStats.depth + 1);
    });
    node.totalLeafCount = totalLeafCount;
    node.subtreeDepth = subtreeDepth;
    node.preorderEnd = hydrateIndex;
    return {
      leafCount: totalLeafCount,
      depth: subtreeDepth,
    };
  }

  function initControls() {
    if (itemTypeButtons) {
      itemTypeButtons.innerHTML = itemTypes.map(function (type) {
        return renderItemTypeButton(type, type, itemTypeCounts.get(type) || 0, itemTypeAbbreviation(type));
      }).join('');
    }
    if (yearStartInput && Number.isInteger(minYear)) {
      yearStartInput.min = minYear;
      yearStartInput.max = maxYear;
      yearStartInput.placeholder = String(minYear);
    }
    if (yearEndInput && Number.isInteger(maxYear)) {
      yearEndInput.min = minYear;
      yearEndInput.max = maxYear;
      yearEndInput.placeholder = String(maxYear);
    }
    updateFilterControls();
    updateSettingsState();
  }

  function renderItemTypeButton(type, label, count, abbr) {
    return [
      '<button type="button" class="kb-type-option" data-ct-item-type="' + escAttr(type) + '" aria-pressed="false">',
      '<span class="kb-type-chip">' + esc(abbr) + '</span>',
      '<span class="kb-type-name">' + esc(label) + '</span>',
      '<span class="kb-type-count">' + esc(count) + '</span>',
      '</button>',
    ].join('');
  }

  function itemTypeAbbreviation(type) {
    if (type === 'Unspecified') return 'None';
    const parts = String(type || '')
      .split(/[\s/&+-]+/)
      .map(function (part) { return part.trim(); })
      .filter(Boolean);
    if (!parts.length) return 'NA';
    if (parts.length === 1) return parts[0].slice(0, 2).toUpperCase();
    return parts.slice(0, 2).map(function (part) { return part[0]; }).join('').toUpperCase();
  }

  function openItemTypeDialog() {
    if (!itemTypeDialog) return;
    if (!itemTypeDialog.open) {
      if (typeof itemTypeDialog.showModal === 'function') {
        itemTypeDialog.showModal();
      } else {
        itemTypeDialog.setAttribute('open', '');
      }
    }
    if (itemTypeTrigger) itemTypeTrigger.setAttribute('aria-expanded', 'true');
    window.requestAnimationFrame(function () {
      const selected = itemTypeDialog.querySelector('[aria-pressed="true"]');
      const first = itemTypeDialog.querySelector('[data-ct-item-type], .ct-item-type-actions button');
      (selected || first || itemTypeClose || itemTypeDialog).focus();
    });
  }

  function closeItemTypeDialog() {
    if (!itemTypeDialog || !itemTypeDialog.open) return;
    if (typeof itemTypeDialog.close === 'function') {
      itemTypeDialog.close();
    } else {
      itemTypeDialog.removeAttribute('open');
      if (itemTypeTrigger) {
        itemTypeTrigger.setAttribute('aria-expanded', 'false');
        itemTypeTrigger.focus();
      }
    }
  }

  function updateFilterControls() {
    if (yearStartInput) yearStartInput.value = Number.isInteger(state.yearStart) ? state.yearStart : '';
    if (yearEndInput) yearEndInput.value = Number.isInteger(state.yearEnd) ? state.yearEnd : '';
    if (itemTypeAllButton) itemTypeAllButton.setAttribute('aria-pressed', String(!state.noItemTypes && !state.itemTypes.size));
    if (itemTypeNoneButton) itemTypeNoneButton.setAttribute('aria-pressed', String(state.noItemTypes));
    if (itemTypeButtons) {
      itemTypeButtons.querySelectorAll('[data-ct-item-type]').forEach(function (button) {
        const type = button.getAttribute('data-ct-item-type') || '';
        const selected = !state.noItemTypes && (!state.itemTypes.size || state.itemTypes.has(type));
        button.setAttribute('aria-pressed', String(selected));
      });
    }
    if (itemTypeSummary) itemTypeSummary.textContent = itemTypeSummaryText();
  }

  function syncYearInputs() {
    if (!Number.isInteger(minYear) || !Number.isInteger(maxYear)) return;
    const rawStart = parseInt(yearStartInput.value, 10);
    const rawEnd = parseInt(yearEndInput.value, 10);
    const start = Number.isInteger(rawStart) ? clamp(rawStart, minYear, maxYear) : minYear;
    const end = Number.isInteger(rawEnd) ? clamp(rawEnd, minYear, maxYear) : maxYear;
    state.yearStart = Math.min(start, end);
    state.yearEnd = Math.max(start, end);
    updateFilterControls();
    render();
  }

  function selectNode(id, options) {
    const node = nodes.get(id);
    if (!node) return;
    currentId = id;

    const url = new URL(window.location.href);
    url.hash = 'ct=' + encodeURIComponent(currentId);
    window.history.pushState(null, '', url);
    render(options);
  }

  function render(options) {
    const node = nodes.get(currentId) || data.root;
    clearPreviewHighlights();
    previewNodeId = null;
    currentFilterKey = filterStateKey();
    currentFilterTerms = normalized(state.query).split(/\s+/).filter(Boolean);
    currentFiltersActive = currentFilterKey !== 'all';
    filterMemo = new Map();
    renderSunburst(node, options);
    renderFocusedTree(node);
    renderSelectionDetails(node);
    renderSearch();
    updateSettingsState();
    indexPreviewTargets();
    if (options && options.centerTree) centerCurrentTreeNode(node);
  }

  function renderSunburst(node, options) {
    if (!sunburstStage) return;
    cancelSunburstAnimation();

    const viewRoot = sunburstRootFor(node);
    const model = getSunburstModel(viewRoot);
    const hierarchy = model.hierarchy;
    const depthMax = model.depthMax;
    const radius = 184;
    const centerRadius = sunburstCenterRadius;
    const ringCount = Math.max(1, depthMax);
    const ringWidth = (radius - centerRadius) / ringCount;
    const entries = model.entries;

    const palette = sunburstPalette();
    const pathNodes = new Set((node.pathNodes || []).map(function (pathNode) { return pathNode.id; }));
    const snapshot = getSunburstSnapshot(viewRoot, model, centerRadius, ringWidth, palette);
    currentSunburstColors = sunburstColorMap(snapshot);
    const shouldAnimate = shouldAnimateSunburst(options, lastSunburstSnapshot);
    const arcs = entries.map(function (entry, index) {
      return renderSunburstArc(entry, snapshot, pathNodes, index);
    }).join('');
    const leafMarks = entries.map(function (entry) {
      return renderSunburstLeafMark(entry, snapshot);
    }).join('');
    const navigationTargets = hierarchy.children.map(function (entry) {
      return renderSunburstHitTarget(entry, snapshot, centerRadius, radius, pathNodes);
    }).join('');
    const labels = hierarchy.children.map(function (entry) {
      return renderSunburstLabel(entry, snapshot, centerRadius, radius, ringWidth);
    }).join('');
    const transitionExtras = shouldAnimate
      ? renderSunburstTransitionExtras(lastSunburstSnapshot, snapshot)
      : '';

    const svgClasses = ['ct-sunburst-svg', shouldAnimate ? 'is-unfolding' : ''].filter(Boolean).join(' ');

    sunburstStage.innerHTML = [
      '<svg class="' + escAttr(svgClasses) + '" viewBox="-205 -205 410 410" aria-hidden="false" focusable="false">',
      '<g class="ct-sunburst-rings">',
      arcs,
      '</g>',
      '<g class="ct-sunburst-transition" aria-hidden="true">',
      transitionExtras,
      '</g>',
      '<g class="ct-sunburst-leaf-rim" aria-hidden="true">',
      leafMarks,
      '</g>',
      '<g class="ct-sunburst-hit-targets">',
      navigationTargets,
      '</g>',
      '<g class="ct-sunburst-labels" aria-hidden="true">',
      labels,
      '</g>',
      renderSunburstCenter(viewRoot),
      '</svg>',
    ].join('');

    if (shouldAnimate) {
      animateSunburstMorph(lastSunburstSnapshot, snapshot);
    }

    lastSunburstSnapshot = snapshot;
    if (sunburstRootButton) sunburstRootButton.disabled = viewRoot.id === data.root.id;
  }

  function cancelSunburstAnimation() {
    sunburstAnimationToken += 1;
    if (sunburstAnimationFrame) {
      window.cancelAnimationFrame(sunburstAnimationFrame);
      sunburstAnimationFrame = 0;
    }
  }

  function sunburstRootFor(node) {
    if (!node) return data.root;
    if (node.children && node.children.length) return node;
    return node.parent || node;
  }

  function getSunburstModel(viewRoot) {
    const cacheKey = sunburstLayoutCacheKey(viewRoot);
    const cached = sunburstLayoutCache.get(cacheKey);
    if (cached) return cached;

    const hierarchy = buildSunburstHierarchy(viewRoot, 0);
    const entries = [];
    layoutSunburstEntries(hierarchy, -Math.PI / 2, (Math.PI * 3) / 2, entries);

    const model = {
      hierarchy: hierarchy,
      depthMax: hierarchy.maxDepth,
      entries: entries,
      snapshotCache: null,
    };
    sunburstLayoutCache.set(cacheKey, model);
    if (sunburstLayoutCache.size > sunburstLayoutCacheLimit) {
      const oldestKey = sunburstLayoutCache.keys().next().value;
      sunburstLayoutCache.delete(oldestKey);
    }
    return model;
  }

  function sunburstLayoutCacheKey(viewRoot) {
    return [
      viewRoot.id,
      currentFilterKey,
      currentFiltersActive ? currentId : '',
    ].join('|');
  }

  function buildSunburstHierarchy(node, depth) {
    const children = visibleChildren(node).map(function (child) {
      return buildSunburstHierarchy(child, depth + 1);
    }).filter(function (child) {
      return child.value > 0 || child.node.id === currentId;
    });
    const childValue = children.reduce(function (sum, child) {
      return sum + child.value;
    }, 0);
    const ownValue = Math.max(filteredLeafCount(node), node.id === currentId ? 1 : 0);
    const maxDepth = children.reduce(function (largestDepth, child) {
      return Math.max(largestDepth, child.maxDepth);
    }, depth);

    return {
      node: node,
      depth: depth,
      value: children.length ? Math.max(childValue, ownValue) : ownValue,
      childValue: childValue,
      maxDepth: maxDepth,
      children: children,
    };
  }

  function layoutSunburstEntries(entry, startAngle, endAngle, entries) {
    const total = Number.isFinite(entry.childValue) ? entry.childValue : entry.children.reduce(function (sum, child) {
      return sum + child.value;
    }, 0);
    if (total <= 0) return;

    let cursor = startAngle;
    entry.children.forEach(function (child, index) {
      const isLast = index === entry.children.length - 1;
      const span = (endAngle - startAngle) * (child.value / total);
      child.startAngle = cursor;
      child.endAngle = isLast ? endAngle : cursor + span;
      child.colorGroupIndex = entry.depth === 0 ? index : entry.colorGroupIndex;
      entries.push(child);
      layoutSunburstEntries(child, child.startAngle, child.endAngle, entries);
      cursor = child.endAngle;
    });
  }

  function getSunburstSnapshot(viewRoot, model, centerRadius, ringWidth, palette) {
    const cacheKey = [
      fmt(centerRadius),
      fmt(ringWidth),
      palette.join('\u001f'),
    ].join('|');
    if (model.snapshotCache && model.snapshotCache.key === cacheKey) {
      return model.snapshotCache.snapshot;
    }

    const snapshot = createSunburstSnapshot(viewRoot, model.entries, centerRadius, ringWidth, palette);
    model.snapshotCache = {
      key: cacheKey,
      snapshot: snapshot,
    };
    return snapshot;
  }

  function createSunburstSnapshot(viewRoot, entries, centerRadius, ringWidth, palette) {
    const entryMap = new Map();
    const colorMap = new Map();

    entries.forEach(function (entry, index) {
      const colorGroupIndex = Number.isInteger(entry.colorGroupIndex) ? entry.colorGroupIndex : 0;
      const fill = palette[colorGroupIndex % palette.length];
      const geometry = sunburstArcGeometry(entry, centerRadius, ringWidth);
      const isLeaf = !entry.children.length;
      const visualLength = sunburstArcLength(geometry);
      const path = sunburstShapePath(geometry);
      const opacity = isLeaf
        ? clamp(0.96 + (entry.depth * 0.006) + (visualLength < 2.5 ? 0.04 : 0), 0.96, 1)
        : 0.9;
      colorMap.set(entry.node.id, fill);
      entryMap.set(entry.node.id, {
        node: entry.node,
        geometry: geometry,
        path: path,
        fill: fill,
        opacity: opacity,
        index: index,
        depth: entry.depth,
        isLeaf: isLeaf,
        visualLength: visualLength,
      });
    });

    return {
      rootId: viewRoot.id,
      rootNode: viewRoot,
      entries: entryMap,
      colors: colorMap,
      center: {
        node: viewRoot,
        geometry: sunburstCenterGeometry(),
      },
    };
  }

  function sunburstColorMap(snapshot) {
    if (snapshot.colors) return snapshot.colors;
    const colors = new Map();
    snapshot.entries.forEach(function (entry, id) {
      colors.set(id, entry.fill);
    });
    return colors;
  }

  function sunburstReducedMotion() {
    return typeof window.matchMedia === 'function' && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  function shouldAnimateSunburst(options, previousSnapshot) {
    return Boolean(options && options.animateSunburst && previousSnapshot && !sunburstReducedMotion());
  }

  function sunburstArcGeometry(entry, centerRadius, ringWidth) {
    const radialGap = sunburstRadialGap(entry, ringWidth);
    const innerRadius = centerRadius + (entry.depth - 1) * ringWidth + radialGap;
    const outerRadius = centerRadius + entry.depth * ringWidth - radialGap;

    return {
      innerRadius: innerRadius,
      outerRadius: outerRadius,
      startAngle: entry.startAngle,
      endAngle: entry.endAngle,
    };
  }

  function sunburstRadialGap(entry, ringWidth) {
    const isLeaf = !entry.children.length;
    const maxGap = isLeaf && entry.depth >= 4 ? 0.95 : 1.55;
    return clamp(ringWidth * 0.1, 0.35, maxGap);
  }

  function sunburstCenterGeometry() {
    return {
      startAngle: -Math.PI / 2,
      endAngle: (Math.PI * 3) / 2,
      innerRadius: 0,
      outerRadius: sunburstCenterCircleRadius,
    };
  }

  function renderSunburstArc(entry, snapshot, pathNodes, index) {
    const node = entry.node;
    const snapshotEntry = snapshot.entries.get(node.id);
    const path = snapshotEntry.path;
    if (!path) return '';

    const visualLength = snapshotEntry.visualLength;
    const isLeaf = snapshotEntry.isLeaf;
    const classes = [
      'ct-sunburst-segment',
      node.kind === 'paper' ? 'ct-sunburst-segment--paper' : 'ct-sunburst-segment--branch',
      isLeaf ? 'ct-sunburst-segment--leaf' : '',
      snapshotEntry.depth >= 4 ? 'is-deep' : '',
      visualLength < 4.5 ? 'is-tight' : '',
      visualLength < 1.6 ? 'is-micro' : '',
      node.id === currentId ? 'is-current' : '',
      pathNodes.has(node.id) && node.id !== currentId ? 'is-path' : '',
    ].filter(Boolean).join(' ');
    return [
      '<path class="' + escAttr(classes) + '"',
      ' d="' + escAttr(path) + '"',
      ' fill="' + escAttr(snapshotEntry.fill) + '"',
      ' fill-opacity="' + escAttr(snapshotEntry.opacity.toFixed(2)) + '"',
      ' data-ct-sunburst-index="' + escAttr(String(index)) + '"',
      ' data-ct-preview-node="' + escAttr(node.id) + '"',
      ' data-ct-sunburst-node="' + escAttr(node.id) + '"',
      ' aria-hidden="true">',
      '</path>',
    ].join('');
  }

  function renderSunburstHitTarget(entry, snapshot, centerRadius, radius, pathNodes) {
    const node = entry.node;
    const snapshotEntry = snapshot.entries.get(node.id);
    const geometry = sunburstBlockGeometry(entry, centerRadius, radius);
    const path = sunburstShapePath(geometry);
    if (!path || !snapshotEntry) return '';

    const classes = [
      'ct-sunburst-hit-target',
      node.kind === 'paper' ? 'ct-sunburst-hit-target--paper' : 'ct-sunburst-hit-target--branch',
      node.id === currentId ? 'is-current' : '',
      pathNodes.has(node.id) && node.id !== currentId ? 'is-path' : '',
    ].filter(Boolean).join(' ');
    const label = sunburstNodeAriaLabel(node);

    return [
      '<path class="' + escAttr(classes) + '"',
      ' d="' + escAttr(path) + '"',
      ' fill="' + escAttr(snapshotEntry.fill) + '"',
      ' stroke="' + escAttr(snapshotEntry.fill) + '"',
      ' style="--ct-sunburst-target-color: ' + escAttr(snapshotEntry.fill) + ';"',
      ' data-ct-select="' + escAttr(node.id) + '"',
      ' data-ct-preview-node="' + escAttr(node.id) + '"',
      ' data-ct-sunburst-node="' + escAttr(node.id) + '"',
      ' tabindex="0"',
      ' role="button"',
      ' aria-label="' + escAttr(label) + '">',
      '<title>' + esc(label) + '</title>',
      '</path>',
    ].join('');
  }

  function renderSunburstLeafMark(entry, snapshot) {
    if (entry.children.length) return '';

    const snapshotEntry = snapshot.entries.get(entry.node.id);
    if (!snapshotEntry) return '';

    const geometry = snapshotEntry.geometry;
    const visualLength = snapshotEntry.visualLength;
    if (entry.depth < 5 && visualLength >= 3.2) return '';

    const span = geometry.endAngle - geometry.startAngle;
    const midAngle = (geometry.startAngle + geometry.endAngle) / 2;
    const markRadius = Math.min(186.2, geometry.outerRadius + 1.2);
    const markWidth = visualLength < 1.6 ? 0.68 : 0.86;
    const markOpacity = visualLength < 1.6 ? 0.46 : 0.42;
    const minDashSpan = 0.85 / markRadius;
    const markStart = span * markRadius >= 0.85
      ? geometry.startAngle
      : midAngle - minDashSpan / 2;
    const markEnd = span * markRadius >= 0.85
      ? geometry.endAngle
      : midAngle + minDashSpan / 2;

    return [
      '<path class="ct-sunburst-leaf-mark"',
      ' d="' + escAttr(arcStrokePath(markStart, markEnd, markRadius)) + '"',
      ' stroke="' + escAttr(snapshotEntry.fill) + '"',
      ' stroke-width="' + escAttr(fmt(markWidth)) + '"',
      ' stroke-opacity="' + escAttr(fmt(markOpacity)) + '">',
      '</path>',
    ].join('');
  }

  function renderSunburstTransitionExtras(previousSnapshot, snapshot) {
    const previousRootEntry = previousSnapshot.entries.get(snapshot.rootId);
    if (!previousRootEntry) return '';

    return [
      '<path class="ct-sunburst-center-morph"',
      ' d="' + escAttr(sunburstShapePath(previousRootEntry.geometry)) + '"',
      ' fill="' + escAttr(previousRootEntry.fill) + '"',
      ' fill-opacity="' + escAttr(previousRootEntry.opacity.toFixed(2)) + '"',
      ' data-ct-sunburst-center-morph="' + escAttr(snapshot.rootId) + '">',
      '</path>',
    ].join('');
  }

  function animateSunburstMorph(previousSnapshot, snapshot) {
    if (typeof window.requestAnimationFrame !== 'function') return;

    const token = sunburstAnimationToken;
    const startTime = window.performance && typeof window.performance.now === 'function'
      ? window.performance.now()
      : Date.now();
    const duration = 760;
    const pathTransitions = [];

    Array.from(sunburstStage.querySelectorAll('.ct-sunburst-segment')).forEach(function (path) {
      const id = path.getAttribute('data-ct-sunburst-node');
      const target = snapshot.entries.get(id);
      if (!target) return;

      const start = sunburstMorphStart(target.node, target.geometry, previousSnapshot);
      pathTransitions.push({
        element: path,
        from: start.geometry,
        to: target.geometry,
        fromOpacity: start.opacity,
        toOpacity: target.opacity,
      });
      path.setAttribute('d', sunburstShapePath(start.geometry));
      path.style.opacity = String(start.opacity);
    });

    const centerMorph = sunburstStage.querySelector('.ct-sunburst-center-morph');
    const centerMorphEntry = centerMorph ? previousSnapshot.entries.get(snapshot.rootId) : null;
    const centerGroup = sunburstStage.querySelector('.ct-sunburst-center');
    const labelsGroup = sunburstStage.querySelector('.ct-sunburst-labels');
    const hitTargetsGroup = sunburstStage.querySelector('.ct-sunburst-hit-targets');
    const leafRimGroup = sunburstStage.querySelector('.ct-sunburst-leaf-rim');
    const svg = sunburstStage.querySelector('.ct-sunburst-svg');

    if (centerGroup) centerGroup.style.opacity = '0';
    if (labelsGroup) labelsGroup.style.opacity = '0';
    if (hitTargetsGroup) hitTargetsGroup.style.opacity = '0';
    if (leafRimGroup) leafRimGroup.style.opacity = '0';
    if (centerMorph && centerMorphEntry) {
      centerMorph.setAttribute('d', sunburstShapePath(centerMorphEntry.geometry));
      centerMorph.style.opacity = String(centerMorphEntry.opacity);
    }

    function tick(now) {
      if (token !== sunburstAnimationToken) return;

      const rawProgress = clamp((now - startTime) / duration, 0, 1);
      const eased = easeSunburstMorph(rawProgress);
      const centerOpacity = clamp((rawProgress - 0.64) / 0.28, 0, 1);

      pathTransitions.forEach(function (transition) {
        const geometry = interpolateSunburstGeometry(transition.from, transition.to, eased);
        const opacity = lerp(transition.fromOpacity, transition.toOpacity, eased);
        transition.element.setAttribute('d', sunburstShapePath(geometry));
        transition.element.style.opacity = String(opacity);
      });

      if (centerMorph && centerMorphEntry) {
        const geometry = interpolateSunburstGeometry(centerMorphEntry.geometry, snapshot.center.geometry, eased);
        centerMorph.setAttribute('d', sunburstShapePath(geometry));
        centerMorph.style.opacity = String(centerMorphEntry.opacity * (1 - centerOpacity));
      }

      if (centerGroup) centerGroup.style.opacity = String(centerOpacity);
      if (labelsGroup) labelsGroup.style.opacity = String(clamp((rawProgress - 0.5) / 0.28, 0, 1));
      if (hitTargetsGroup) hitTargetsGroup.style.opacity = String(clamp((rawProgress - 0.5) / 0.28, 0, 1));
      if (leafRimGroup) leafRimGroup.style.opacity = String(clamp((rawProgress - 0.38) / 0.34, 0, 1));

      if (rawProgress >= 1) {
        pathTransitions.forEach(function (transition) {
          transition.element.setAttribute('d', sunburstShapePath(transition.to));
          transition.element.style.opacity = '';
        });
        if (centerMorph) centerMorph.remove();
        if (centerGroup) centerGroup.style.opacity = '';
        if (labelsGroup) labelsGroup.style.opacity = '';
        if (hitTargetsGroup) hitTargetsGroup.style.opacity = '';
        if (leafRimGroup) leafRimGroup.style.opacity = '';
        if (svg) svg.classList.remove('is-unfolding');
        sunburstAnimationFrame = 0;
        return;
      }

      sunburstAnimationFrame = window.requestAnimationFrame(tick);
    }

    sunburstAnimationFrame = window.requestAnimationFrame(tick);
  }

  function sunburstMorphStart(node, targetGeometry, previousSnapshot) {
    const previousEntry = previousSnapshot.entries.get(node.id);
    if (previousEntry) {
      return {
        geometry: previousEntry.geometry,
        opacity: previousEntry.opacity,
      };
    }

    if (node.id === previousSnapshot.rootId) {
      return {
        geometry: previousSnapshot.center.geometry,
        opacity: 0.9,
      };
    }

    return {
      geometry: collapsedSunburstGeometry(targetGeometry),
      opacity: 0,
    };
  }

  function collapsedSunburstGeometry(geometry) {
    const angle = (geometry.startAngle + geometry.endAngle) / 2;
    return {
      startAngle: angle - 0.0001,
      endAngle: angle + 0.0001,
      innerRadius: geometry.innerRadius,
      outerRadius: geometry.outerRadius,
    };
  }

  function interpolateSunburstGeometry(from, to, progress) {
    return {
      startAngle: lerp(from.startAngle, to.startAngle, progress),
      endAngle: lerp(from.endAngle, to.endAngle, progress),
      innerRadius: lerp(from.innerRadius, to.innerRadius, progress),
      outerRadius: lerp(from.outerRadius, to.outerRadius, progress),
    };
  }

  function easeSunburstMorph(value) {
    const t = clamp(value, 0, 1);
    return t < 0.5
      ? 4 * t * t * t
      : 1 - Math.pow(-2 * t + 2, 3) / 2;
  }

  function lerp(from, to, progress) {
    return from + (to - from) * progress;
  }

  function sunburstShapePath(geometry) {
    const startAngle = geometry.startAngle;
    const endAngle = geometry.endAngle;
    const innerRadius = Math.max(0, geometry.innerRadius);
    const outerRadius = Math.max(innerRadius, geometry.outerRadius);
    const span = endAngle - startAngle;
    if (span <= 0 || outerRadius <= 0) return '';

    if (innerRadius <= 0.1) {
      return diskSectorPath(startAngle, endAngle, outerRadius);
    }

    return arcPath(startAngle, endAngle, innerRadius, outerRadius);
  }

  function sunburstBlockGeometry(entry, centerRadius, radius) {
    return {
      innerRadius: centerRadius + 0.8,
      outerRadius: radius,
      startAngle: entry.startAngle,
      endAngle: entry.endAngle,
    };
  }

  function diskSectorPath(startAngle, endAngle, radius) {
    const span = endAngle - startAngle;
    if (span >= Math.PI * 2 - 0.001) {
      const start = polarPoint(startAngle, radius);
      const middle = polarPoint(startAngle + Math.PI, radius);
      return [
        'M', fmt(start.x), fmt(start.y),
        'A', fmt(radius), fmt(radius), 0, 1, 1, fmt(middle.x), fmt(middle.y),
        'A', fmt(radius), fmt(radius), 0, 1, 1, fmt(start.x), fmt(start.y),
        'Z',
      ].join(' ');
    }

    const outerStart = polarPoint(startAngle, radius);
    const outerEnd = polarPoint(endAngle, radius);
    const largeArc = span > Math.PI ? 1 : 0;

    return [
      'M', 0, 0,
      'L', fmt(outerStart.x), fmt(outerStart.y),
      'A', fmt(radius), fmt(radius), 0, largeArc, 1, fmt(outerEnd.x), fmt(outerEnd.y),
      'Z',
    ].join(' ');
  }

  function renderSunburstLabel(entry, snapshot, centerRadius, radius, ringWidth) {
    const label = treeNodeDisplayLabel(entry.node);
    const snapshotEntry = snapshot.entries.get(entry.node.id);
    const layout = sunburstLabelLayout(entry, centerRadius, radius, ringWidth, label);
    if (!layout) return '';

    return [
      '<text class="ct-sunburst-label' + (layout.outside ? ' is-outside' : '') + '"',
      ' x="' + escAttr(fmt(layout.point.x)) + '"',
      ' y="' + escAttr(fmt(layout.firstLineY)) + '"',
      snapshotEntry ? ' style="--ct-sunburst-label-stroke: ' + escAttr(snapshotEntry.fill) + ';"' : '',
      ' text-anchor="' + escAttr(layout.anchor) + '" dominant-baseline="central">',
      '<title>' + esc(label) + '</title>',
      layout.lines.map(function (line, index) {
        return [
          '<tspan x="' + escAttr(fmt(layout.point.x)) + '"',
          ' y="' + escAttr(fmt(layout.firstLineY + index * layout.lineHeight)) + '">',
          esc(line),
          '</tspan>',
        ].join('');
      }).join(''),
      '</text>',
    ].join('');
  }

  function sunburstLabelLayout(entry, centerRadius, radius, ringWidth, label) {
    const text = String(label || '').trim();
    if (!text) return null;

    const span = entry.endAngle - entry.startAngle;
    const radialSpan = radius - centerRadius;
    if (span <= 0 || radialSpan <= 0) return null;

    const angle = span >= Math.PI * 2 - 0.01
      ? Math.PI / 2
      : (entry.startAngle + entry.endAngle) / 2;
    const narrowness = clamp((0.82 - span) / 0.82, 0, 1);
    const labelRadius = centerRadius + radialSpan * (0.58 + narrowness * 0.27);
    const point = polarPoint(angle, labelRadius);
    const chordWidth = span >= Math.PI
      ? radius * 1.22
      : 2 * labelRadius * Math.sin(span / 2);
    const arcWidth = span * labelRadius;
    const availableWidth = clamp(Math.max(chordWidth, arcWidth * 0.66) * 1.03, 18, radius * 1.28);
    const availableHeight = clamp(radialSpan * (0.36 + narrowness * 0.12), 14, 58);

    if (availableWidth >= 18 && span * labelRadius >= 15) {
      const lineHeight = sunburstLabelFontSize * 1.14;
      const maxLines = clamp(Math.floor(availableHeight / lineHeight), 1, 4);
      const maxChars = Math.max(4, Math.floor(availableWidth / (sunburstLabelFontSize * 0.56)));
      const lines = wrapSunburstLabel(text, maxChars, maxLines, false);
      if (lines && lines.join(' ') === text && lines.length <= maxLines) {
        return sunburstLabelResult(point, lineHeight, lines, {
          anchor: 'middle',
          outside: false,
        });
      }
    }

    return sunburstOuterLabelLayout(entry, centerRadius, radius, ringWidth, text);
  }

  function sunburstOuterLabelLayout(entry, centerRadius, radius, ringWidth, text) {
    const span = entry.endAngle - entry.startAngle;
    const angle = span >= Math.PI * 2 - 0.01
      ? Math.PI / 2
      : (entry.startAngle + entry.endAngle) / 2;
    const directionX = Math.cos(angle);
    const sectorOuterRadius = sunburstSectorOuterRadius(entry, centerRadius, radius, ringWidth);
    const outsideRadius = sectorOuterRadius + 8 + clamp((0.22 - span) * 28, 0, 7);
    const point = polarPoint(angle, outsideRadius);
    let anchor = 'middle';
    let availableWidth = 110;

    if (directionX > 0.28) {
      anchor = 'start';
      point.x += 4;
      availableWidth = 94;
    } else if (directionX < -0.28) {
      anchor = 'end';
      point.x -= 4;
      availableWidth = 94;
    }

    const lineHeight = sunburstLabelFontSize * 1.12;
    const maxLines = 4;
    const maxChars = Math.max(5, Math.floor(availableWidth / (sunburstLabelFontSize * 0.55)));
    const fullLines = wrapSunburstLabel(text, maxChars, maxLines, false);
    if (fullLines && fullLines.join(' ') === text) {
      return sunburstLabelResult(point, lineHeight, fullLines, {
        anchor: anchor,
        outside: true,
      });
    }

    const fallbackLineHeight = sunburstLabelFontSize * 1.12;
    const fallbackChars = Math.max(5, Math.floor(availableWidth / (sunburstLabelFontSize * 0.55)));
    const lines = wrapSunburstLabel(text, fallbackChars, 4, true);
    return sunburstLabelResult(point, fallbackLineHeight, lines, {
      anchor: anchor,
      outside: true,
    });
  }

  function sunburstSectorOuterRadius(entry, centerRadius, radius, ringWidth) {
    const depth = Number.isFinite(entry.maxDepth) ? entry.maxDepth : entry.depth;
    return clamp(centerRadius + depth * ringWidth, centerRadius, radius);
  }

  function sunburstLabelResult(point, lineHeight, lines, options) {
    const labelOptions = options || {};
    return {
      point: point,
      lineHeight: lineHeight,
      firstLineY: point.y - ((lines.length - 1) * lineHeight) / 2,
      lines: lines,
      anchor: labelOptions.anchor || 'middle',
      outside: Boolean(labelOptions.outside),
    };
  }

  function wrapSunburstLabel(text, maxChars, maxLines, allowEllipsis) {
    const words = String(text || '').split(/\s+/).filter(Boolean);
    const lines = [];
    let current = '';

    words.forEach(function (word) {
      if (!current) {
        current = word;
        return;
      }

      const candidate = current + ' ' + word;
      if (candidate.length <= maxChars) {
        current = candidate;
        return;
      }

      lines.push(current);
      current = word;
    });

    if (current) lines.push(current);

    if (!allowEllipsis) {
      if (lines.length > maxLines) return null;
      return lines.every(function (line) { return line.length <= maxChars; }) ? lines : null;
    }

    const visibleLines = lines.slice(0, maxLines);
    if (lines.length > maxLines && visibleLines.length) {
      visibleLines[visibleLines.length - 1] = truncateLabel(visibleLines[visibleLines.length - 1], maxChars);
    }

    return visibleLines.map(function (line) {
      return truncateLabel(line, maxChars);
    });
  }

  function renderSunburstCenter(node) {
    const labelLines = centerLabelLines(treeNodeDisplayLabel(node));
    const count = filteredLeafCount(node);
    const canMoveUp = Boolean(node.parent);
    const lineHeight = 12;
    const firstLineY = Math.round(-(labelLines.length * lineHeight) / 2 - 2);
    const metaY = firstLineY + labelLines.length * lineHeight + (labelLines.length === 1 ? 9 : 10);
    const centerAttributes = [
      'class="ct-sunburst-center' + (canMoveUp ? '' : ' is-static') + '"',
      canMoveUp ? 'data-ct-select="' + escAttr(node.parent.id) + '"' : '',
      'data-ct-preview-node="' + escAttr(node.id) + '"',
      'data-ct-sunburst-node="' + escAttr(node.id) + '"',
      canMoveUp ? 'tabindex="0"' : '',
      canMoveUp ? 'role="button"' : '',
      'aria-label="' + escAttr(canMoveUp ? 'Move to parent branch, ' + treeNodeDisplayLabel(node.parent) : sunburstNodeAriaLabel(node)) + '"',
    ].filter(Boolean).join(' ');

    return [
      '<g ' + centerAttributes + '>',
      '<circle r="' + escAttr(fmt(sunburstCenterCircleRadius)) + '"></circle>',
      '<text text-anchor="middle" dominant-baseline="middle">',
      labelLines.map(function (line, index) {
        return '<tspan x="0" y="' + escAttr(fmt(firstLineY + index * lineHeight)) + '">' + esc(line) + '</tspan>';
      }).join(''),
      '<tspan class="ct-sunburst-center-meta" x="0" y="' + escAttr(fmt(metaY)) + '">' + esc(plural(count, 'item')) + '</tspan>',
      '</text>',
      '</g>',
    ].join('');
  }

  function setPreviewNode(id) {
    const node = nodes.get(id);
    if (!node) return;

    previewNodeId = id;
    syncPreviewHighlights(node);
  }

  function clearPreviewNode() {
    previewNodeId = null;
    clearPreviewHighlights();
  }

  function indexPreviewTargets() {
    previewTargetsByNodeId = new Map();
    sunburstPreviewTargets = [];
    sunburstHitTargetPreviewTargets = [];

    Array.from(app.querySelectorAll('[data-ct-preview-node]')).forEach(function (element) {
      const node = nodes.get(element.getAttribute('data-ct-preview-node'));
      if (!node) return;

      const target = {
        element: element,
        node: node,
      };
      if (!previewTargetsByNodeId.has(node.id)) previewTargetsByNodeId.set(node.id, []);
      previewTargetsByNodeId.get(node.id).push(target);

      if (element.closest('#ct-sunburst')) sunburstPreviewTargets.push(target);
      if (element.classList.contains('ct-sunburst-hit-target')) sunburstHitTargetPreviewTargets.push(target);
    });
  }

  function syncPreviewHighlights(node) {
    clearPreviewHighlights();
    if (!node) return;

    const exactElements = new Set();
    (previewTargetsByNodeId.get(node.id) || []).forEach(function (target) {
      exactElements.add(target.element);
      addPreviewClass(target.element, 'is-preview');
    });

    sunburstPreviewTargets.forEach(function (target) {
      if (!exactElements.has(target.element) && isNodeWithin(target.node, node)) {
        addPreviewClass(target.element, 'is-preview-descendant');
      }
    });

    sunburstHitTargetPreviewTargets.forEach(function (target) {
      if (!exactElements.has(target.element) && isNodeWithin(node, target.node)) {
        addPreviewClass(target.element, 'is-preview-ancestor');
      }
    });
  }

  function clearPreviewHighlights() {
    activePreviewClasses.forEach(function (entry) {
      entry.element.classList.remove(entry.className);
    });
    activePreviewClasses = [];
  }

  function addPreviewClass(element, className) {
    element.classList.add(className);
    activePreviewClasses.push({
      element: element,
      className: className,
    });
  }

  function isNodeWithin(candidate, ancestor) {
    if (!candidate || !ancestor) return false;
    return candidate.preorderStart >= ancestor.preorderStart
      && candidate.preorderStart < ancestor.preorderEnd;
  }

  function sunburstNodeAriaLabel(node) {
    return [
      treeNodeDisplayLabel(node),
      kindLabel(node),
      plural(filteredLeafCount(node), 'descendent', 'descendents'),
    ].filter(Boolean).join(', ');
  }

  function sunburstPalette() {
    const style = window.getComputedStyle(app);
    const palette = sunburstPaletteVars.map(function (name) {
      return style.getPropertyValue(name).trim();
    }).filter(Boolean);
    return palette.length ? palette : ['#2276c9', '#12877f', '#c33d80', '#b66d18', '#4c8a2f'];
  }

  function arcPath(startAngle, endAngle, innerRadius, outerRadius) {
    if (endAngle <= startAngle || outerRadius <= innerRadius) return '';
    const span = endAngle - startAngle;

    if (span >= Math.PI * 2 - 0.001) {
      const outerStart = polarPoint(startAngle, outerRadius);
      const outerMiddle = polarPoint(startAngle + Math.PI, outerRadius);
      const innerStart = polarPoint(startAngle, innerRadius);
      const innerMiddle = polarPoint(startAngle + Math.PI, innerRadius);

      return [
        'M', fmt(outerStart.x), fmt(outerStart.y),
        'A', fmt(outerRadius), fmt(outerRadius), 0, 1, 1, fmt(outerMiddle.x), fmt(outerMiddle.y),
        'A', fmt(outerRadius), fmt(outerRadius), 0, 1, 1, fmt(outerStart.x), fmt(outerStart.y),
        'L', fmt(innerStart.x), fmt(innerStart.y),
        'A', fmt(innerRadius), fmt(innerRadius), 0, 1, 0, fmt(innerMiddle.x), fmt(innerMiddle.y),
        'A', fmt(innerRadius), fmt(innerRadius), 0, 1, 0, fmt(innerStart.x), fmt(innerStart.y),
        'Z',
      ].join(' ');
    }

    const outerStart = polarPoint(startAngle, outerRadius);
    const outerEnd = polarPoint(endAngle, outerRadius);
    const innerEnd = polarPoint(endAngle, innerRadius);
    const innerStart = polarPoint(startAngle, innerRadius);
    const largeArc = span > Math.PI ? 1 : 0;

    return [
      'M', fmt(outerStart.x), fmt(outerStart.y),
      'A', fmt(outerRadius), fmt(outerRadius), 0, largeArc, 1, fmt(outerEnd.x), fmt(outerEnd.y),
      'L', fmt(innerEnd.x), fmt(innerEnd.y),
      'A', fmt(innerRadius), fmt(innerRadius), 0, largeArc, 0, fmt(innerStart.x), fmt(innerStart.y),
      'Z',
    ].join(' ');
  }

  function arcStrokePath(startAngle, endAngle, radius) {
    if (endAngle <= startAngle || radius <= 0) return '';

    const start = polarPoint(startAngle, radius);
    const end = polarPoint(endAngle, radius);
    const largeArc = endAngle - startAngle > Math.PI ? 1 : 0;

    return [
      'M', fmt(start.x), fmt(start.y),
      'A', fmt(radius), fmt(radius), 0, largeArc, 1, fmt(end.x), fmt(end.y),
    ].join(' ');
  }

  function sunburstArcLength(geometry) {
    const radius = (geometry.innerRadius + geometry.outerRadius) / 2;
    return Math.max(0, geometry.endAngle - geometry.startAngle) * radius;
  }

  function polarPoint(angle, radius) {
    return {
      x: Math.cos(angle) * radius,
      y: Math.sin(angle) * radius,
    };
  }

  function centerLabelLines(label) {
    const text = String(label || '').trim() || 'Root';
    const lines = wrapSunburstLabel(text, sunburstCenterLabelMaxChars, sunburstCenterLabelMaxLines, false);
    if (lines && lines.join(' ') === text) return lines;
    return wrapSunburstLabel(text, sunburstCenterLabelMaxChars, sunburstCenterLabelMaxLines, true);
  }

  function truncateLabel(label, maxLength) {
    const text = String(label || '').trim();
    if (text.length <= maxLength) return text;
    return text.slice(0, Math.max(1, maxLength - 3)).replace(/\s+$/, '') + '...';
  }

  function fmt(value) {
    return Number(value).toFixed(3).replace(/\.?0+$/, '');
  }

  function renderFocusedTree(node) {
    const ancestors = node.pathNodes.slice(0, -1);
    const children = visibleChildren(node);
    const ego = node.kind === 'paper'
      ? ''
      : [
        '<div class="ct-focus-core">',
        renderNodeSection('', [node], 'ego', node),
        '</div>',
      ].join('');
    const html = [
      '<div class="ct-focus-stack">',
      ancestors.length ? renderNodeSection('Ancestors', ancestors, 'path', node) : '',
      ego,
      node.children.length ? renderNodeSection('Children', children, 'children', node) : '',
      '</div>',
    ].filter(Boolean).join('');
    ancestorChain.innerHTML = html;
  }

  function renderNodeSection(title, rows, sectionKind, currentNode) {
    const empty = sectionKind === 'children'
      ? 'No children match the current filters.'
      : 'No descendents match the current filters.';
    const label = title ? ' aria-label="' + escAttr(title) + '"' : '';
    return [
      '<section class="ct-focus-section ct-focus-section--' + escAttr(sectionKind) + '"' + label + '>',
      rows.length
        ? '<ul class="ct-tree-list">' + rows.map(function (row, index) {
          return renderTreeNode(row, currentNode, sectionKind, index, rows.length);
        }).join('') + '</ul>'
        : '<p class="ct-empty">' + esc(empty) + '</p>',
      '</section>',
    ].join('');
  }

  function renderTreeNode(treeNode, currentNode, sectionKind, index, total) {
    const isCurrent = treeNode.id === currentNode.id;
    const isAncestor = currentNode.pathNodes.some(function (pathNode) { return pathNode.id === treeNode.id; }) && !isCurrent;
    const isParent = Boolean(currentNode.parent && treeNode.id === currentNode.parent.id);
    const isSuccessor = Boolean(treeNode.parent && treeNode.parent.id === currentNode.id);
    const hasChildren = treeNode.children.length > 0;
    const details = isCurrent && treeNode.kind !== 'paper' ? renderCurrentNodeDetails(treeNode) : '';
    const visibleLeafCount = filteredLeafCount(treeNode);
    const classes = [
      'ct-tree-node',
      'ct-tree-kind-' + treeNode.kind,
      'ct-tree-section-' + sectionKind,
      isCurrent ? 'is-current' : '',
      isAncestor ? 'is-ancestor' : '',
      isParent ? 'is-parent' : '',
      isSuccessor ? 'is-successor' : '',
      index === 0 ? 'is-first' : '',
      index === total - 1 ? 'is-last' : '',
    ].filter(Boolean).join(' ');
    const colorStyle = treeNodeListColorStyle(treeNode);

    return [
      '<li class="' + escAttr(classes) + '"' + colorStyle + '>',
      '<button type="button" class="ct-tree-button" data-ct-select="' + escAttr(treeNode.id) + '" data-ct-preview-node="' + escAttr(treeNode.id) + '"' + branchHintAttr(hasChildren) + '>',
      '<span class="ct-tree-rail" aria-hidden="true"><span class="ct-tree-dot"></span></span>',
      '<span class="ct-tree-copy">',
      '<span class="ct-tree-label">' + esc(treeNodeDisplayLabel(treeNode)) + '</span>',
      '<span class="ct-tree-meta">' + esc(treeNodeMeta(treeNode, visibleLeafCount)) + '</span>',
      '</span>',
      '</button>',
      details,
      '</li>',
    ].join('');
  }

  function treeNodeListColorStyle(treeNode) {
    const color = currentSunburstColors.get(treeNode.id);
    return color ? ' style="--ct-tree-node-color: ' + escAttr(color) + ';"' : '';
  }

  function renderCurrentNodeDetails(node) {
    if (node.kind === 'paper') return renderPaperDetails(node);
    if (!node.url) return '';
    return '<a class="ct-tree-open-link" href="' + escAttr(node.url) + '">Open page</a>';
  }

  function branchHintAttr(hasChildren) {
    return hasChildren ? ' data-ct-has-children="true"' : '';
  }

  function renderPaperDetails(node) {
    const paper = node.paper || {};
    const abstract = paper.abstract || 'No abstract recorded yet.';
    const detailUrl = node.url || '';
    const mapUrl = paper.mapUrl || mapUrlFromSource(node.source);
    const actions = [
      detailUrl
        ? '<a class="paper-link-pill paper-link-pill--internal" href="' + escAttr(detailUrl) + '"><span class="paper-link-pill__label">Open Detail Page</span></a>'
        : '',
      mapUrl
        ? '<a class="paper-link-pill paper-link-pill--internal" href="' + escAttr(mapUrl) + '"><span class="paper-link-pill__label">Open in Map</span></a>'
        : '',
    ].filter(Boolean).join('');

    return [
      '<div class="ct-paper-details">',
      '<p class="ct-paper-abstract">' + esc(abstract) + '</p>',
      actions ? '<div class="ct-paper-actions paper-link-pills">' + actions + '</div>' : '',
      '</div>',
    ].join('');
  }

  function renderSelectionDetails(node) {
    if (!selectionDetails) return;

    if (!node || node.kind !== 'paper') {
      selectionDetails.hidden = true;
      selectionDetails.innerHTML = '';
      return;
    }

    selectionDetails.hidden = false;
    selectionDetails.innerHTML = renderPaperSelectionDetails(node);
  }

  function renderPaperSelectionDetails(node) {
    const paper = node.paper || {};
    const title = treeNodeDisplayLabel(node);
    const path = displayPath(node.path).join(' / ');
    const authors = paperAuthorsLine(paper);
    const meta = [
      paper.year || '',
      paper.type || '',
      paper.sourceName || paper.source || '',
    ].filter(Boolean);

    return [
      '<div class="ct-selection-details-head">',
      '<div class="ct-selection-details-title">',
      '<h2>' + esc(title) + '</h2>',
      authors ? '<p class="ct-selection-authors">' + esc(authors) + '</p>' : '',
      '<p class="ct-selection-path">' + esc(path) + '</p>',
      meta.length ? '<div class="ct-selection-meta">' + meta.map(function (item) {
        return '<span>' + esc(item) + '</span>';
      }).join('') + '</div>' : '',
      '</div>',
      '</div>',
      '<div class="ct-selection-details-body">',
      renderPaperDetails(node),
      '</div>',
    ].join('');
  }

  function visibleChildren(node) {
    if (!currentFiltersActive) return node.children || [];
    return (node.children || []).filter(function (child) {
      return filteredLeafCount(child) > 0 || child.id === currentId;
    });
  }

  function filteredLeafCount(node) {
    if (!node) return 0;
    if (!currentFiltersActive) return node.totalLeafCount || 0;
    if (filterMemo.has(node.id)) return filterMemo.get(node.id);
    let count;
    if (!node.children.length) {
      count = nodeMatchesFilters(node) ? 1 : 0;
    } else {
      count = node.children.reduce(function (sum, child) {
        return sum + filteredLeafCount(child);
      }, 0);
    }
    filterMemo.set(node.id, count);
    return count;
  }

  function nodeMatchesFilters(node) {
    const matchesQuery = !currentFilterTerms.length || currentFilterTerms.every(function (term) {
      return node.searchText.includes(term);
    });
    if (!matchesQuery) return false;

    if (node.kind !== 'paper') {
      return !itemTypeFilterActive() && !yearFilterActive();
    }

    if (state.noItemTypes) return false;
    if (state.itemTypes.size && !state.itemTypes.has(paperType(node))) return false;
    if (yearFilterActive()) {
      const year = paperYear(node);
      if (!Number.isInteger(year)) return false;
      if (year < state.yearStart || year > state.yearEnd) return false;
    }
    return true;
  }

  function renderSearch() {
    if (!searchInput) return;
    const query = state.query;
    if (!query) {
      lastMatches = [];
      searchResults.hidden = true;
      searchResults.innerHTML = '';
      return;
    }

    lastMatches = getMatches(query).slice(0, 18);
    if (!lastMatches.length) {
      searchResults.hidden = false;
      searchResults.innerHTML = '<p class="ct-empty">No matches found.</p>';
      return;
    }

    searchResults.hidden = false;
    searchResults.innerHTML = [
      '<div class="ct-result-grid">',
      lastMatches.map(function (node) {
        return [
          '<button type="button" class="ct-result" data-ct-select="' + escAttr(node.id) + '" data-ct-preview-node="' + escAttr(node.id) + '">',
          '<span class="ct-kind">' + esc(kindLabel(node)) + '</span>',
          '<strong>' + esc(node.label) + '</strong>',
          '<span>' + esc(displayPath(node.path).join(' / ')) + '</span>',
          '</button>',
        ].join('');
      }).join(''),
      '</div>',
    ].join('');
  }

  function centerCurrentTreeNode(node) {
    if (node.id === data.root.id) return;
    window.requestAnimationFrame(function () {
      const current = ancestorChain.querySelector('.ct-tree-node.is-current > .ct-tree-button');
      if (!current) return;
      current.scrollIntoView({ block: 'center', inline: 'nearest' });
    });
  }

  function eventTargetContains(target, relatedTarget) {
    if (!target || !relatedTarget || typeof target.contains !== 'function') return false;
    try {
      return target.contains(relatedTarget);
    } catch (error) {
      return false;
    }
  }

  function getMatches(query) {
    const terms = normalized(query).split(/\s+/).filter(Boolean);
    if (!terms.length) return [];
    return searchableNodes.filter(function (node) {
      return terms.every(function (term) {
        return node.searchText.includes(term);
      }) && filteredLeafCount(node) > 0;
    }).sort(function (a, b) {
      if (a.id === currentId) return -1;
      if (b.id === currentId) return 1;
      if (a.kind !== b.kind) return a.kind === 'branch' ? -1 : 1;
      return a.path.length - b.path.length || a.label.localeCompare(b.label);
    });
  }

  function readHashId() {
    const hash = window.location.hash.slice(1);
    try {
      const params = new URLSearchParams(hash);
      const nodeId = params.get('ct');
      if (nodeId) return nodeId;

      const paperId = params.get('paper');
      if (paperId && paperNodes.has(paperId)) return paperNodes.get(paperId);
    } catch (error) {
      return null;
    }
    return null;
  }

  function updateSettingsState() {
    if (!settingsState || !settings) return;
    settingsState.textContent = settings.classList.contains('is-collapsed') ? 'Show Settings' : 'Hide Settings';
  }

  function itemTypeFilterActive() {
    return state.noItemTypes || state.itemTypes.size > 0;
  }

  function filterStateKey() {
    const queryKey = normalized(state.query).trim();
    const typeKey = state.noItemTypes
      ? 'none'
      : (state.itemTypes.size
        ? Array.from(state.itemTypes).sort(function (a, b) { return a.localeCompare(b); }).join('\u001f')
        : 'all');
    const yearKey = yearFilterActive() ? state.yearStart + '-' + state.yearEnd : 'all';
    if (!queryKey && typeKey === 'all' && yearKey === 'all') return 'all';
    return [queryKey, typeKey, yearKey].join('|');
  }

  function allItemTypesSelected() {
    return !state.noItemTypes && state.itemTypes.size === 0;
  }

  function itemTypeSummaryText() {
    if (state.noItemTypes) return 'No item types';
    if (!itemTypeFilterActive()) return 'All item types';
    const selected = Array.from(state.itemTypes).sort(function (a, b) { return a.localeCompare(b); });
    if (selected.length === 1) return selected[0];
    return selected.length + ' item types';
  }

  function yearFilterActive() {
    return Number.isInteger(minYear)
      && Number.isInteger(maxYear)
      && (state.yearStart !== minYear || state.yearEnd !== maxYear);
  }

  function paperYear(node) {
    const paper = node && node.paper ? node.paper : {};
    const value = paper.yearValue != null ? paper.yearValue : paper.year;
    const year = parseInt(value, 10);
    return Number.isInteger(year) ? year : null;
  }

  function paperType(node) {
    const paper = node && node.paper ? node.paper : {};
    return String(paper.type || 'Unspecified').trim() || 'Unspecified';
  }

  function mapUrlFromSource(source) {
    const match = String(source || '').match(/^papers\/(.+)\.md$/);
    return match ? '../map/#paper=' + encodeURIComponent(match[1]) : '';
  }

  function paperIdFromSource(source) {
    const match = String(source || '').match(/^papers\/(.+)\.md$/);
    return match ? match[1] : '';
  }

  function treeNodeMeta(node, visibleLeafCount) {
    if (node.kind === 'branch') {
      const childCount = visibleChildren(node).length;
      return plural(visibleLeafCount, 'descendent', 'descendents') + ' / ' + plural(childCount, 'child', 'children');
    }
    if (node.kind === 'paper') {
      return paperCitationMeta(node) || kindLabel(node);
    }
    return kindLabel(node);
  }

  function treeNodeDisplayLabel(node) {
    return node.id === data.root.id ? 'Root' : node.label;
  }

  function paperCitationMeta(node) {
    const paper = node.paper || {};
    const authors = paperAuthors(paper);
    const year = String(paper.year || '').trim();
    const type = paperType(node);
    const author = authors.length ? authors[0] + (authors.length > 1 ? ' et al.' : '') : '';
    return [author, year, type].filter(Boolean).join(' / ');
  }

  function paperAuthors(paper) {
    return Array.isArray(paper.authors)
      ? paper.authors.map(function (author) { return String(author || '').trim(); }).filter(Boolean)
      : [];
  }

  function paperAuthorsLine(paper) {
    return paperAuthors(paper).join(', ');
  }

  function kindLabel(node) {
    if (node.kind === 'branch') return 'Branch';
    if (node.kind === 'paper') return 'Paper';
    if (node.kind === 'page') return 'Page';
    return 'Link';
  }

  function displayPath(path) {
    return path.map(function (label, index) {
      return index === 0 && label === data.root.label ? 'Root' : label;
    });
  }

  function plural(count, singular, pluralLabel) {
    return count + ' ' + (count === 1 ? singular : (pluralLabel || singular + 's'));
  }

  function clamp(value, min, max) {
    return Math.max(min, Math.min(max, value));
  }

  function normalized(value) {
    return String(value || '').toLowerCase().normalize('NFKD').replace(/[\u0300-\u036f]/g, '');
  }

  function esc(value) {
    return String(value == null ? '' : value)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function escAttr(value) {
    return esc(value);
  }
})();
