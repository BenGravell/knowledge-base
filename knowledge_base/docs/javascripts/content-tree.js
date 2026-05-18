'use strict';

(function () {
  const app = document.getElementById('ct-app');
  if (!app) return;

  const data = window.contentTreeData;
  const settings = document.getElementById('ct-settings');
  const settingsToggle = document.getElementById('ct-settings-toggle');
  const settingsState = document.getElementById('ct-settings-state');
  const searchInput = document.getElementById('ct-search');
  const sourceTypeSelect = document.getElementById('ct-source-type');
  const yearStartInput = document.getElementById('ct-year-start');
  const yearEndInput = document.getElementById('ct-year-end');
  const resetButton = document.getElementById('ct-reset');
  const searchResults = document.getElementById('ct-search-results');
  const breadcrumbs = document.getElementById('ct-breadcrumbs');
  const ancestorChain = document.getElementById('ct-ancestor-chain');

  if (!data || !data.root) {
    app.innerHTML = '<p class="ct-error">Content tree data is unavailable. Run <code>mkdocs build</code> to regenerate it.</p>';
    return;
  }

  const nodes = new Map();
  const paperNodes = new Map();
  const searchableNodes = [];
  let currentId = data.root.id;
  let lastMatches = [];
  let filterMemo = new Map();
  const state = {
    query: '',
    yearStart: null,
    yearEnd: null,
    sourceType: '',
  };

  hydrate(data.root, null);
  const paperYears = searchableNodes
    .map(function (node) { return paperYear(node); })
    .filter(Number.isInteger);
  const minYear = paperYears.length ? Math.min.apply(null, paperYears) : null;
  const maxYear = paperYears.length ? Math.max.apply(null, paperYears) : null;
  const sourceTypes = Array.from(new Set(searchableNodes
    .filter(function (node) { return node.kind === 'paper'; })
    .map(function (node) { return paperType(node); })
    .filter(Boolean))).sort(function (a, b) { return a.localeCompare(b); });

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
    selectNode(target.getAttribute('data-ct-select'));
  });

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

  if (sourceTypeSelect) {
    sourceTypeSelect.addEventListener('change', function () {
      state.sourceType = sourceTypeSelect.value;
      render();
    });
  }

  if (resetButton) {
    resetButton.addEventListener('click', function () {
      state.query = '';
      state.yearStart = minYear;
      state.yearEnd = maxYear;
      state.sourceType = '';
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

  function hydrate(node, parent) {
    const paper = node.paper || {};
    const authors = Array.isArray(paper.authors) ? paper.authors.join(' ') : '';
    node.parent = parent;
    node.children = Array.isArray(node.children) ? node.children : [];
    node.pathNodes = parent ? parent.pathNodes.concat(node) : [node];
    node.searchText = normalized([node.label, node.path.join(' '), node.source || '', authors, paper.year || '', paper.type || '', paper.sourceName || ''].join(' '));
    nodes.set(node.id, node);
    if (node.kind === 'paper') {
      const paperId = paper.id || paperIdFromSource(node.source);
      if (paperId) paperNodes.set(String(paperId), node.id);
    }
    searchableNodes.push(node);
    node.children.forEach(function (child) {
      hydrate(child, node);
    });
  }

  function initControls() {
    if (sourceTypeSelect) {
      sourceTypeSelect.innerHTML = '<option value="">All source types</option>' + sourceTypes.map(function (type) {
        return '<option value="' + escAttr(type) + '">' + esc(type) + '</option>';
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

  function updateFilterControls() {
    if (yearStartInput) yearStartInput.value = Number.isInteger(state.yearStart) ? state.yearStart : '';
    if (yearEndInput) yearEndInput.value = Number.isInteger(state.yearEnd) ? state.yearEnd : '';
    if (sourceTypeSelect) sourceTypeSelect.value = state.sourceType;
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

  function selectNode(id) {
    const node = nodes.get(id);
    if (!node) return;
    currentId = id;

    const url = new URL(window.location.href);
    url.hash = 'ct=' + encodeURIComponent(currentId);
    window.history.pushState(null, '', url);
    render();
  }

  function render() {
    const node = nodes.get(currentId) || data.root;
    filterMemo = new Map();
    renderBreadcrumbs(node);
    renderFocusedTree(node);
    renderSearch();
    updateSettingsState();
    centerCurrentTreeNode(node);
  }

  function renderBreadcrumbs(node) {
    breadcrumbs.innerHTML = node.pathNodes.map(function (pathNode, index) {
      const separator = index === 0 ? '' : '<span class="ct-crumb-separator">/</span>';
      const current = pathNode.id === node.id ? ' aria-current="page"' : '';
      return separator + '<button type="button" data-ct-select="' + escAttr(pathNode.id) + '"' + current + '>' + esc(pathDisplayLabel(pathNode, index)) + '</button>';
    }).join('');
  }

  function renderFocusedTree(node) {
    const ancestors = node.pathNodes.slice(0, -1);
    const parent = node.parent;
    const siblings = parent ? visibleChildren(parent).filter(function (child) {
      return child.id !== node.id;
    }) : [];
    const children = visibleChildren(node);
    const html = [
      '<div class="ct-focus-stack">',
      ancestors.length ? renderNodeSection('Path', ancestors, 'path', node) : '',
      renderNodeSection('Selected', [node], 'ego', node),
      parent ? renderNodeSection('Sibling Choices', siblings, 'siblings', node) : '',
      renderNodeSection('Direct Children', children, 'children', node),
      '</div>',
    ].filter(Boolean).join('');
    ancestorChain.innerHTML = html;
  }

  function renderNodeSection(title, rows, sectionKind, currentNode) {
    const empty = sectionKind === 'children'
      ? 'No direct children match the current filters.'
      : 'No matching siblings.';
    return [
      '<section class="ct-focus-section ct-focus-section--' + escAttr(sectionKind) + '">',
      '<div class="ct-focus-section-head">',
      '<h2>' + esc(title) + '</h2>',
      '<span>' + esc(plural(rows.length, 'item')) + '</span>',
      '</div>',
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
    const details = isCurrent ? renderCurrentNodeDetails(treeNode) : '';
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
      '<button type="button" class="ct-tree-button" data-ct-select="' + escAttr(treeNode.id) + '"' + branchHintAttr(hasChildren) + '>',
      '<span class="ct-tree-rail" aria-hidden="true"><span class="ct-tree-dot"></span></span>',
      '<span class="ct-tree-copy">',
      '<span class="ct-tree-label">' + esc(treeNode.label) + '</span>',
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
    const mindMapUrl = paper.mindMapUrl || mindMapUrlFromSource(node.source);
    const actions = [
      detailUrl
        ? '<a class="paper-link-pill paper-link-pill--internal" href="' + escAttr(detailUrl) + '"><span class="paper-link-pill__label">Open Detail Page</span></a>'
        : '',
      mindMapUrl
        ? '<a class="paper-link-pill paper-link-pill--internal" href="' + escAttr(mindMapUrl) + '"><span class="paper-link-pill__label">Open in Mind Map</span></a>'
        : '',
    ].filter(Boolean).join('');

    return [
      '<div class="ct-paper-details">',
      '<p class="ct-paper-abstract">' + esc(abstract) + '</p>',
      actions ? '<div class="ct-paper-actions paper-link-pills">' + actions + '</div>' : '',
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
      return !state.sourceType && !yearFilterActive();
    }

    if (state.sourceType && paperType(node) !== state.sourceType) return false;
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
          '<button type="button" class="ct-result" data-ct-select="' + escAttr(node.id) + '">',
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
    settingsState.textContent = settings.classList.contains('is-collapsed') ? 'Show Settings' : filterStatus();
  }

  function filterStatus() {
    const count = filteredLeafCount(data.root);
    const parts = [plural(count, 'matching item')];
    if (state.sourceType) parts.push(state.sourceType);
    if (yearFilterActive()) parts.push(state.yearStart + '-' + state.yearEnd);
    return parts.join(' / ');
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

  function mindMapUrlFromSource(source) {
    const match = String(source || '').match(/^papers\/(.+)\.md$/);
    return match ? '../mind-map/#paper=' + encodeURIComponent(match[1]) : '';
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

  function pathDisplayLabel(pathNode, index) {
    return index === 0 && pathNode.id === data.root.id ? 'Root' : pathNode.label;
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
