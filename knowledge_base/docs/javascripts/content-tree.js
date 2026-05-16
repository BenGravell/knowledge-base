'use strict';

(function () {
  const app = document.getElementById('ct-app');
  if (!app) return;

  const data = window.contentTreeData;
  const searchInput = document.getElementById('ct-search');
  const stats = document.getElementById('ct-tree-stats');
  const currentSummary = document.getElementById('ct-current-summary');
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

  hydrate(data.root, null);
  const initialId = readHashId();
  currentId = initialId && nodes.has(initialId) ? initialId : data.root.id;
  render();

  app.addEventListener('click', function (event) {
    const target = event.target.closest('[data-ct-select]');
    if (!target || !app.contains(target)) return;
    event.preventDefault();
    selectNode(target.getAttribute('data-ct-select'));
  });

  searchInput.addEventListener('input', function () {
    renderSearch();
  });

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
    node.searchText = normalized([node.label, node.path.join(' '), node.source || '', authors, paper.year || ''].join(' '));
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

  function selectNode(id) {
    const node = nodes.get(id);
    if (!node) return;
    if (id === currentId) {
      if (node.kind !== 'branch') return;
      currentId = node.parent ? node.parent.id : data.root.id;
    } else {
      currentId = id;
    }

    const url = new URL(window.location.href);
    url.hash = 'ct=' + encodeURIComponent(currentId);
    window.history.pushState(null, '', url);
    render();
  }

  function render() {
    const node = nodes.get(currentId) || data.root;
    stats.textContent = plural(data.meta.totalLeaves, 'item') + ' in ' + plural(data.meta.totalBranches, 'branch', 'branches');
    currentSummary.textContent = '';
    renderBreadcrumbs(node);
    renderAncestorChain(node);
    renderSearch();
    centerCurrentTreeNode(node);
  }

  function renderBreadcrumbs(node) {
    breadcrumbs.innerHTML = node.pathNodes.map(function (pathNode, index) {
      const separator = index === 0 ? '' : '<span class="ct-crumb-separator">/</span>';
      const current = pathNode.id === node.id ? ' aria-current="page"' : '';
      return separator + '<button type="button" data-ct-select="' + escAttr(pathNode.id) + '"' + current + '>' + esc(pathDisplayLabel(pathNode, index)) + '</button>';
    }).join('');
  }

  function renderAncestorChain(node) {
    const pathIds = new Set(node.pathNodes.map(function (pathNode) { return pathNode.id; }));
    ancestorChain.innerHTML = [
      '<ul class="ct-tree-list ct-tree-root">',
      data.root.children.map(function (child) {
        return renderTreeNode(child, node, pathIds, 0);
      }).join(''),
      '</ul>',
    ].join('');
  }

  function renderTreeNode(treeNode, currentNode, pathIds, depth) {
    const isCurrent = treeNode.id === currentNode.id;
    const isAncestor = pathIds.has(treeNode.id) && !isCurrent;
    const isParent = Boolean(currentNode.parent && treeNode.id === currentNode.parent.id);
    const isSuccessor = Boolean(treeNode.parent && treeNode.parent.id === currentNode.id);
    const hasChildren = treeNode.children.length > 0;
    const isExpanded = hasChildren && pathIds.has(treeNode.id);
    const isMuted = !isCurrent && !isAncestor && !isParent && !isSuccessor;
    const details = isCurrent ? renderCurrentNodeDetails(treeNode) : '';
    const classes = [
      'ct-tree-node',
      'ct-tree-kind-' + treeNode.kind,
      isCurrent ? 'is-current' : '',
      isAncestor ? 'is-ancestor' : '',
      isParent ? 'is-parent' : '',
      isSuccessor ? 'is-successor' : '',
      isExpanded ? 'is-expanded' : '',
      isMuted ? 'is-muted' : '',
    ].filter(Boolean).join(' ');
    const children = isExpanded
      ? '<ul class="ct-tree-list">' + treeNode.children.map(function (child) {
        return renderTreeNode(child, currentNode, pathIds, depth + 1);
      }).join('') + '</ul>'
      : '';

    return [
      '<li class="' + escAttr(classes) + '" style="--ct-depth:' + depth + '">',
      '<button type="button" class="ct-tree-button" data-ct-select="' + escAttr(treeNode.id) + '"' + branchExpandedAttr(hasChildren, isExpanded) + '>',
      '<span class="ct-tree-rail" aria-hidden="true"><span class="ct-tree-dot"></span></span>',
      '<span class="ct-tree-copy">',
      '<span class="ct-tree-label">' + esc(treeNode.label) + '</span>',
      '<span class="ct-tree-meta">' + esc(treeNodeMeta(treeNode)) + '</span>',
      '</span>',
      '</button>',
      details,
      children,
      '</li>',
    ].join('');
  }

  function renderCurrentNodeDetails(node) {
    if (node.kind === 'paper') return renderPaperDetails(node);
    if (!node.url) return '';
    return '<a class="ct-tree-open-link" href="' + escAttr(node.url) + '">Open page</a>';
  }

  function branchExpandedAttr(hasChildren, isExpanded) {
    return hasChildren ? ' aria-expanded="' + (isExpanded ? 'true' : 'false') + '"' : '';
  }

  function renderPaperDetails(node) {
    const paper = node.paper || {};
    const abstract = paper.abstract || 'No abstract recorded yet.';
    const detailUrl = node.url || '';
    const mindMapUrl = paper.mindMapUrl || mindMapUrlFromSource(node.source);
    const actions = [
      detailUrl
        ? '<a class="paper-link-pill paper-link-pill--internal" href="' + escAttr(detailUrl) + '"><span class="paper-link-pill__label">Open detail page</span></a>'
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

  function mindMapUrlFromSource(source) {
    const match = String(source || '').match(/^papers\/(.+)\.md$/);
    return match ? '../mind-map/#paper=' + encodeURIComponent(match[1]) : '';
  }

  function paperIdFromSource(source) {
    const match = String(source || '').match(/^papers\/(.+)\.md$/);
    return match ? match[1] : '';
  }

  function renderSearch() {
    const query = searchInput.value.trim();
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
      });
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

  function nodeSummary(node) {
    if (node.kind !== 'branch') return kindLabel(node);
    return plural(node.leafCount, 'item') + ' across ' + plural(node.children.length, 'next choice', 'next choices');
  }

  function treeNodeMeta(node) {
    if (node.kind === 'branch') {
      return plural(node.leafCount, 'item') + ' / ' + plural(node.children.length, 'child', 'children');
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
    const author = authors.length ? authors[0] + (authors.length > 1 ? ' et al.' : '') : '';
    return [author, year].filter(Boolean).join(' · ');
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
