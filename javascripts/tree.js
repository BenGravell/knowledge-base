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
  const selectionConnector = document.getElementById('ct-selection-connector');
  const sunburst = document.getElementById('ct-sunburst');
  const sunburstStage = document.getElementById('ct-sunburst-stage') || sunburst;
  const sunburstFocus = document.getElementById('ct-sunburst-focus');
  const sunburstPath = document.getElementById('ct-sunburst-path');
  const sunburstStats = document.getElementById('ct-sunburst-stats');
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
  let currentId = data.root.id;
  let lastMatches = [];
  let filterMemo = new Map();
  let sunburstAnimationFrame = 0;
  let sunburstAnimationToken = 0;
  let lastSunburstSnapshot = null;
  let selectionConnectorFrame = 0;
  let previewNodeId = null;
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
      animateSunburst: Boolean(target.closest('#ct-sunburst')),
    });
  });

  app.addEventListener('keydown', function (event) {
    if (event.key !== 'Enter' && event.key !== ' ') return;
    const target = event.target.closest('[data-ct-select]');
    if (!target || !app.contains(target)) return;
    event.preventDefault();
    selectNode(target.getAttribute('data-ct-select'), {
      centerTree: Boolean(target.closest('#ct-search-results')),
      animateSunburst: Boolean(target.closest('#ct-sunburst')),
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

  window.addEventListener('resize', scheduleSelectionConnector);

  function hydrate(node, parent, siblingIndex) {
    const paper = node.paper || {};
    const authors = Array.isArray(paper.authors) ? paper.authors.join(' ') : '';
    node.parent = parent;
    node.siblingIndex = Number.isInteger(siblingIndex) ? siblingIndex : 0;
    node.children = Array.isArray(node.children) ? node.children : [];
    node.pathNodes = parent ? parent.pathNodes.concat(node) : [node];
    node.searchText = normalized([node.label, node.path.join(' '), node.source || '', authors, paper.year || '', paper.type || '', paper.sourceName || ''].join(' '));
    nodes.set(node.id, node);
    if (node.kind === 'paper') {
      const paperId = paper.id || paperIdFromSource(node.source);
      if (paperId) paperNodes.set(String(paperId), node.id);
    }
    searchableNodes.push(node);
    node.children.forEach(function (child, index) {
      hydrate(child, node, index);
    });
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
    previewNodeId = null;
    filterMemo = new Map();
    renderSunburst(node, options);
    renderFocusedTree(node);
    renderSelectionDetails(node);
    renderSearch();
    updateSettingsState();
    scheduleSelectionConnector();
    if (options && options.centerTree) centerCurrentTreeNode(node);
  }

  function renderSunburst(node, options) {
    if (!sunburstStage) return;
    cancelSunburstAnimation();

    const viewRoot = sunburstRootFor(node);
    const hierarchy = buildSunburstHierarchy(viewRoot, 0);
    const depthMax = maxSunburstDepth(hierarchy);
    const radius = 184;
    const centerRadius = 53;
    const ringCount = Math.max(1, depthMax);
    const ringWidth = (radius - centerRadius) / ringCount;
    const entries = [];
    layoutSunburstEntries(hierarchy, -Math.PI / 2, (Math.PI * 3) / 2, entries);

    const palette = sunburstPalette();
    const pathNodes = new Set((node.pathNodes || []).map(function (pathNode) { return pathNode.id; }));
    const snapshot = createSunburstSnapshot(viewRoot, entries, centerRadius, ringWidth, palette);
    const shouldAnimate = Boolean(options && options.animateSunburst && lastSunburstSnapshot && !sunburstReducedMotion());
    const arcs = entries.map(function (entry, index) {
      return renderSunburstArc(entry, snapshot, pathNodes, index);
    }).join('');
    const leafMarks = entries.map(function (entry) {
      return renderSunburstLeafMark(entry, snapshot);
    }).join('');
    const labels = entries.map(function (entry) {
      return renderSunburstLabel(entry, centerRadius, ringWidth);
    }).join('');
    const transitionExtras = shouldAnimate
      ? renderSunburstTransitionExtras(lastSunburstSnapshot, snapshot)
      : '';

    const svgClasses = ['ct-sunburst-svg', shouldAnimate ? 'is-unfolding' : ''].filter(Boolean).join(' ');

    sunburstStage.innerHTML = [
      '<svg class="' + escAttr(svgClasses) + '" viewBox="-190 -190 380 380" aria-hidden="false" focusable="false">',
      '<g class="ct-sunburst-rings">',
      arcs,
      '</g>',
      '<g class="ct-sunburst-transition" aria-hidden="true">',
      transitionExtras,
      '</g>',
      '<g class="ct-sunburst-leaf-rim" aria-hidden="true">',
      leafMarks,
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
    updateSunburstReadout(node, false);
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

    return {
      node: node,
      depth: depth,
      value: children.length ? Math.max(childValue, ownValue) : ownValue,
      children: children,
    };
  }

  function maxSunburstDepth(entry) {
    if (!entry.children.length) return entry.depth;
    return entry.children.reduce(function (maxDepth, child) {
      return Math.max(maxDepth, maxSunburstDepth(child));
    }, entry.depth);
  }

  function layoutSunburstEntries(entry, startAngle, endAngle, entries) {
    const total = entry.children.reduce(function (sum, child) {
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

  function createSunburstSnapshot(viewRoot, entries, centerRadius, ringWidth, palette) {
    const entryMap = new Map();

    entries.forEach(function (entry, index) {
      const colorGroupIndex = Number.isInteger(entry.colorGroupIndex) ? entry.colorGroupIndex : 0;
      const fill = palette[colorGroupIndex % palette.length];
      const geometry = sunburstArcGeometry(entry, centerRadius, ringWidth);
      const isLeaf = !entry.children.length;
      const visualLength = sunburstArcLength(geometry);
      const opacity = isLeaf
        ? clamp(0.96 + (entry.depth * 0.006) + (visualLength < 2.5 ? 0.04 : 0), 0.96, 1)
        : 0.9;
      entryMap.set(entry.node.id, {
        node: entry.node,
        geometry: geometry,
        fill: fill,
        opacity: opacity,
        index: index,
      });
    });

    return {
      rootId: viewRoot.id,
      rootNode: viewRoot,
      entries: entryMap,
      center: {
        node: viewRoot,
        geometry: sunburstCenterGeometry(),
      },
    };
  }

  function sunburstReducedMotion() {
    return typeof window.matchMedia === 'function' && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  function sunburstArcGeometry(entry, centerRadius, ringWidth) {
    const radialGap = sunburstRadialGap(entry, ringWidth);
    const innerRadius = centerRadius + (entry.depth - 1) * ringWidth + radialGap;
    const outerRadius = centerRadius + entry.depth * ringWidth - radialGap;
    const span = entry.endAngle - entry.startAngle;
    const isLeaf = !entry.children.length;
    const isDeepLeaf = isLeaf && entry.depth >= 4;
    const padLimit = isDeepLeaf ? 0.0018 : 0.006;
    const padRatio = isDeepLeaf ? 0.035 : 0.13;
    const pad = Math.min(padLimit, span * padRatio);

    return {
      innerRadius: innerRadius,
      outerRadius: outerRadius,
      startAngle: entry.startAngle + pad,
      endAngle: entry.endAngle - pad,
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
      outerRadius: 48,
    };
  }

  function renderSunburstArc(entry, snapshot, pathNodes, index) {
    const node = entry.node;
    const snapshotEntry = snapshot.entries.get(node.id);
    const geometry = snapshotEntry.geometry;
    const path = sunburstShapePath(geometry);
    if (!path) return '';

    const visualLength = sunburstArcLength(geometry);
    const isLeaf = !entry.children.length;
    const classes = [
      'ct-sunburst-segment',
      node.kind === 'paper' ? 'ct-sunburst-segment--paper' : 'ct-sunburst-segment--branch',
      isLeaf ? 'ct-sunburst-segment--leaf' : '',
      entry.depth >= 4 ? 'is-deep' : '',
      visualLength < 4.5 ? 'is-tight' : '',
      visualLength < 1.6 ? 'is-micro' : '',
      node.id === currentId ? 'is-current' : '',
      pathNodes.has(node.id) && node.id !== currentId ? 'is-path' : '',
    ].filter(Boolean).join(' ');
    const label = sunburstNodeAriaLabel(node);

    return [
      '<path class="' + escAttr(classes) + '"',
      ' d="' + escAttr(path) + '"',
      ' fill="' + escAttr(snapshotEntry.fill) + '"',
      ' fill-opacity="' + escAttr(snapshotEntry.opacity.toFixed(2)) + '"',
      ' data-ct-sunburst-index="' + escAttr(String(index)) + '"',
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
    const visualLength = sunburstArcLength(geometry);
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
    const leafRimGroup = sunburstStage.querySelector('.ct-sunburst-leaf-rim');
    const svg = sunburstStage.querySelector('.ct-sunburst-svg');

    if (centerGroup) centerGroup.style.opacity = '0';
    if (labelsGroup) labelsGroup.style.opacity = '0';
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
      if (leafRimGroup) leafRimGroup.style.opacity = String(clamp((rawProgress - 0.38) / 0.34, 0, 1));

      if (rawProgress >= 1) {
        pathTransitions.forEach(function (transition) {
          transition.element.setAttribute('d', sunburstShapePath(transition.to));
          transition.element.style.opacity = '';
        });
        if (centerMorph) centerMorph.remove();
        if (centerGroup) centerGroup.style.opacity = '';
        if (labelsGroup) labelsGroup.style.opacity = '';
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

  function renderSunburstLabel(entry, centerRadius, ringWidth) {
    const span = entry.endAngle - entry.startAngle;
    if (span < 0.2 || entry.depth > 3) return '';

    const innerRadius = centerRadius + (entry.depth - 1) * ringWidth + 2;
    const outerRadius = centerRadius + entry.depth * ringWidth - 2;
    const radius = (innerRadius + outerRadius) / 2;
    const angle = (entry.startAngle + entry.endAngle) / 2;
    const point = polarPoint(angle, radius);
    const degrees = normalizedDegrees((angle * 180) / Math.PI);
    const rotation = degrees > 90 && degrees < 270 ? degrees + 180 : degrees;
    const maxChars = clamp(Math.floor((span * radius) / 7), 4, 24);
    const label = truncateLabel(treeNodeDisplayLabel(entry.node), maxChars);

    return [
      '<text class="ct-sunburst-label"',
      ' transform="translate(' + fmt(point.x) + ' ' + fmt(point.y) + ') rotate(' + fmt(rotation) + ')"',
      ' text-anchor="middle" dominant-baseline="middle">',
      esc(label),
      '</text>',
    ].join('');
  }

  function renderSunburstCenter(node) {
    const label = centerLabelLines(treeNodeDisplayLabel(node));
    const count = filteredLeafCount(node);
    const canMoveUp = Boolean(node.parent);
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
      '<circle r="48"></circle>',
      '<text text-anchor="middle" dominant-baseline="middle">',
      '<tspan x="0" y="-8">' + esc(label[0]) + '</tspan>',
      label[1] ? '<tspan x="0" y="8">' + esc(label[1]) + '</tspan>' : '',
      '<tspan class="ct-sunburst-center-meta" x="0" y="' + (label[1] ? 24 : 12) + '">' + esc(plural(count, 'item')) + '</tspan>',
      '</text>',
      '</g>',
    ].join('');
  }

  function setPreviewNode(id) {
    const node = nodes.get(id);
    if (!node) return;

    previewNodeId = id;
    updateSunburstReadout(node, true);
    syncPreviewHighlights(node);
  }

  function clearPreviewNode() {
    previewNodeId = null;
    clearPreviewHighlights();
    updateSunburstReadout(nodes.get(currentId) || data.root, false);
  }

  function syncPreviewHighlights(node) {
    clearPreviewHighlights();
    if (!node) return;

    Array.from(app.querySelectorAll('[data-ct-preview-node]')).forEach(function (element) {
      const id = element.getAttribute('data-ct-preview-node');
      const candidate = nodes.get(id);
      if (!candidate) return;

      if (candidate.id === node.id) {
        element.classList.add('is-preview');
      } else if (element.closest('#ct-sunburst') && isNodeWithin(candidate, node)) {
        element.classList.add('is-preview-descendant');
      }
    });
  }

  function clearPreviewHighlights() {
    Array.from(app.querySelectorAll('.is-preview, .is-preview-descendant')).forEach(function (element) {
      element.classList.remove('is-preview', 'is-preview-descendant');
    });
  }

  function isNodeWithin(candidate, ancestor) {
    if (!candidate || !ancestor) return false;
    return candidate.pathNodes.some(function (pathNode) {
      return pathNode.id === ancestor.id;
    });
  }

  function updateSunburstReadout(node, isPreview) {
    if (!sunburstFocus || !node) return;
    const visibleLeafCount = filteredLeafCount(node);
    const root = sunburstRootFor(nodes.get(currentId) || data.root);
    const path = displayPath(node.path).join(' / ');
    const stats = [
      '<span>' + esc(isPreview ? 'Preview' : kindLabel(node)) + '</span>',
      '<span>' + esc(plural(visibleLeafCount, 'matching item')) + '</span>',
      node.kind === 'branch' ? '<span>' + esc(plural(visibleChildren(node).length, 'choice')) + '</span>' : '',
      root.id !== node.id ? '<span>Rooted at ' + esc(treeNodeDisplayLabel(root)) + '</span>' : '',
    ].filter(Boolean).join('');

    sunburstFocus.textContent = treeNodeDisplayLabel(node);
    if (sunburstPath) sunburstPath.textContent = path;
    if (sunburstStats) sunburstStats.innerHTML = stats;
  }

  function sunburstNodeAriaLabel(node) {
    return [
      treeNodeDisplayLabel(node),
      kindLabel(node),
      plural(filteredLeafCount(node), 'matching item'),
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
    const outerStart = polarPoint(startAngle, outerRadius);
    const outerEnd = polarPoint(endAngle, outerRadius);
    const innerEnd = polarPoint(endAngle, innerRadius);
    const innerStart = polarPoint(startAngle, innerRadius);
    const largeArc = endAngle - startAngle > Math.PI ? 1 : 0;

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
    const words = String(label || '').split(/\s+/).filter(Boolean);
    if (!words.length) return ['Root', ''];
    if (words.length === 1) return [truncateLabel(words[0], 12), ''];
    const first = [];
    const second = [];
    words.forEach(function (word) {
      const target = first.join(' ').length <= second.join(' ').length ? first : second;
      target.push(word);
    });
    return [
      truncateLabel(first.join(' '), 12),
      truncateLabel(second.join(' '), 12),
    ];
  }

  function truncateLabel(label, maxLength) {
    const text = String(label || '').trim();
    if (text.length <= maxLength) return text;
    return text.slice(0, Math.max(1, maxLength - 3)).replace(/\s+$/, '') + '...';
  }

  function normalizedDegrees(value) {
    return ((value % 360) + 360) % 360;
  }

  function fmt(value) {
    return Number(value).toFixed(3).replace(/\.?0+$/, '');
  }

  function renderFocusedTree(node) {
    const ancestors = node.pathNodes.slice(0, -1);
    const children = visibleChildren(node);
    const html = [
      '<div class="ct-focus-stack">',
      ancestors.length ? renderNodeSection('Ancestors', ancestors, 'path', node) : '',
      '<div class="ct-focus-core">',
      renderNodeSection('', [node], 'ego', node, { hideHeader: true }),
      '</div>',
      node.children.length ? renderNodeSection('Children', children, 'children', node) : '',
      '</div>',
    ].filter(Boolean).join('');
    ancestorChain.innerHTML = html;
  }

  function renderNodeSection(title, rows, sectionKind, currentNode, options) {
    const hideHeader = Boolean(options && options.hideHeader);
    const empty = sectionKind === 'children'
      ? 'No children match the current filters.'
      : 'No matching items.';
    const header = hideHeader
      ? ''
      : [
        '<div class="ct-focus-section-head">',
        '<h2>' + esc(title) + '</h2>',
        '<span>' + esc(plural(rows.length, 'item')) + '</span>',
        '</div>',
      ].join('');
    return [
      '<section class="ct-focus-section ct-focus-section--' + escAttr(sectionKind) + '">',
      header,
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

    return [
      '<li class="' + escAttr(classes) + '">',
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
      selectionDetails.style.removeProperty('--ct-selection-anchor-x');
      clearSelectionConnector();
      return;
    }

    selectionDetails.hidden = false;
    selectionDetails.innerHTML = renderPaperSelectionDetails(node);
  }

  function renderPaperSelectionDetails(node) {
    const paper = node.paper || {};
    const title = treeNodeDisplayLabel(node);
    const abstract = paper.abstract || 'No abstract recorded yet.';
    const path = displayPath(node.path).join(' / ');
    const meta = [
      paper.year || '',
      paper.type || '',
      paper.sourceName || paper.source || '',
    ].filter(Boolean);

    return [
      '<div class="ct-selection-details-head">',
      '<div class="ct-selection-details-title">',
      '<span class="ct-selection-kicker">Paper</span>',
      '<h2>' + esc(title) + '</h2>',
      '<p>' + esc(path) + '</p>',
      '</div>',
      meta.length ? '<div class="ct-selection-meta">' + meta.map(function (item) {
        return '<span>' + esc(item) + '</span>';
      }).join('') + '</div>' : '',
      '</div>',
      '<div class="ct-selection-details-body">',
      renderPaperDetails(node),
      '</div>',
    ].join('');
  }

  function visibleChildren(node) {
    return (node.children || []).filter(function (child) {
      return filteredLeafCount(child) > 0 || child.id === currentId;
    });
  }

  function filteredLeafCount(node) {
    if (!node) return 0;
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
    const terms = normalized(state.query).split(/\s+/).filter(Boolean);
    const matchesQuery = !terms.length || terms.every(function (term) {
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
      scheduleSelectionConnector();
    });
  }

  function scheduleSelectionConnector() {
    if (!selectionConnector || !selectionDetails) return;
    if (selectionConnectorFrame) window.cancelAnimationFrame(selectionConnectorFrame);
    selectionConnectorFrame = window.requestAnimationFrame(function () {
      selectionConnectorFrame = 0;
      updateSelectionConnector();
    });
  }

  function clearSelectionConnector() {
    if (selectionConnector) selectionConnector.innerHTML = '';
  }

  function updateSelectionConnector() {
    if (!selectionConnector || !selectionDetails || selectionDetails.hidden) {
      clearSelectionConnector();
      return;
    }

    const node = nodes.get(currentId);
    if (!node || node.kind !== 'paper') {
      clearSelectionConnector();
      return;
    }

    const source = ancestorChain.querySelector('.ct-tree-node.is-current > .ct-tree-button .ct-tree-dot')
      || ancestorChain.querySelector('.ct-tree-node.is-current > .ct-tree-button');
    if (!source) {
      clearSelectionConnector();
      return;
    }

    const appRect = app.getBoundingClientRect();
    const sourceRect = source.getBoundingClientRect();
    const detailRect = selectionDetails.getBoundingClientRect();
    if (!appRect.width || !appRect.height || !detailRect.width || detailRect.top <= sourceRect.bottom) {
      clearSelectionConnector();
      return;
    }

    const appWidth = Math.ceil(app.scrollWidth || appRect.width);
    const appHeight = Math.ceil(app.scrollHeight || appRect.height);
    const detailLeft = detailRect.left - appRect.left;
    const detailRight = detailRect.right - appRect.left;
    const startX = sourceRect.left + sourceRect.width / 2 - appRect.left;
    const startY = sourceRect.bottom - appRect.top + 5;
    const targetX = clamp(startX, detailLeft + 28, detailRight - 28);
    const targetY = detailRect.top - appRect.top - 1;
    const controlY = startY + Math.max(34, (targetY - startY) * 0.58);
    const detailAnchorX = targetX - detailLeft;
    const path = [
      'M', fmt(startX), fmt(startY),
      'C', fmt(startX), fmt(controlY), fmt(targetX), fmt(controlY), fmt(targetX), fmt(targetY),
    ].join(' ');

    selectionDetails.style.setProperty('--ct-selection-anchor-x', fmt(detailAnchorX) + 'px');
    selectionConnector.setAttribute('viewBox', '0 0 ' + appWidth + ' ' + appHeight);
    selectionConnector.setAttribute('width', String(appWidth));
    selectionConnector.setAttribute('height', String(appHeight));
    selectionConnector.innerHTML = [
      '<path class="ct-selection-connector-path" d="' + escAttr(path) + '"></path>',
      '<circle class="ct-selection-connector-source" cx="' + escAttr(fmt(startX)) + '" cy="' + escAttr(fmt(startY)) + '" r="3.2"></circle>',
      '<circle class="ct-selection-connector-target" cx="' + escAttr(fmt(targetX)) + '" cy="' + escAttr(fmt(targetY)) + '" r="4.2"></circle>',
    ].join('');
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
      return plural(visibleLeafCount, 'matching item') + ' / ' + plural(childCount, 'choice');
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
    const authors = Array.isArray(paper.authors) ? paper.authors.filter(Boolean) : [];
    const year = String(paper.year || '').trim();
    const type = paperType(node);
    const author = authors.length ? authors[0] + (authors.length > 1 ? ' et al.' : '') : '';
    return [author, year, type].filter(Boolean).join(' / ');
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
