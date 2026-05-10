'use strict';

(function () {
  const app = document.getElementById('ct-app');
  if (!app) return;

  const data = window.contentTreeData;
  const form = document.getElementById('ct-search-form');
  const searchInput = document.getElementById('ct-search');
  const rootButton = document.getElementById('ct-root-btn');
  const stats = document.getElementById('ct-tree-stats');
  const currentSummary = document.getElementById('ct-current-summary');
  const searchResults = document.getElementById('ct-search-results');
  const breadcrumbs = document.getElementById('ct-breadcrumbs');
  const ancestorChain = document.getElementById('ct-ancestor-chain');
  const currentNode = document.getElementById('ct-current-node');
  const childNodes = document.getElementById('ct-child-nodes');

  if (!data || !data.root) {
    app.innerHTML = '<p class="ct-error">Content tree data is unavailable. Run <code>mkdocs build</code> to regenerate it.</p>';
    return;
  }

  const nodes = new Map();
  const searchableNodes = [];
  let currentId = data.root.id;
  let lastMatches = [];

  hydrate(data.root, null);
  currentId = nodes.has(readHashId()) ? readHashId() : data.root.id;
  render();

  app.addEventListener('click', function (event) {
    const target = event.target.closest('[data-ct-select]');
    if (!target || !app.contains(target)) return;
    event.preventDefault();
    selectNode(target.getAttribute('data-ct-select'));
  });

  form.addEventListener('submit', function (event) {
    event.preventDefault();
    const match = lastMatches[0] || getMatches(searchInput.value)[0];
    if (match) selectNode(match.id);
  });

  searchInput.addEventListener('input', function () {
    renderSearch();
  });

  rootButton.addEventListener('click', function () {
    searchInput.value = '';
    if (currentId === data.root.id) {
      render();
    } else {
      selectNode(data.root.id);
    }
  });

  window.addEventListener('popstate', function () {
    const hashId = readHashId();
    if (hashId && nodes.has(hashId)) {
      currentId = hashId;
      render();
    }
  });

  function hydrate(node, parent) {
    node.parent = parent;
    node.children = Array.isArray(node.children) ? node.children : [];
    node.pathNodes = parent ? parent.pathNodes.concat(node) : [node];
    node.searchText = normalized([node.label, node.path.join(' '), node.source || ''].join(' '));
    nodes.set(node.id, node);
    searchableNodes.push(node);
    node.children.forEach(function (child) {
      hydrate(child, node);
    });
  }

  function selectNode(id) {
    if (!nodes.has(id) || id === currentId) return;
    currentId = id;
    const url = new URL(window.location.href);
    url.hash = 'ct=' + encodeURIComponent(id);
    window.history.pushState(null, '', url);
    render();
  }

  function render() {
    const node = nodes.get(currentId) || data.root;
    stats.textContent = plural(data.meta.totalLeaves, 'item') + ' in ' + plural(data.meta.totalBranches, 'branch', 'branches');
    currentSummary.textContent = nodeSummary(node);
    renderBreadcrumbs(node);
    renderAncestorChain(node);
    renderCurrentNode(node);
    renderChildren(node);
    renderSearch();
  }

  function renderBreadcrumbs(node) {
    breadcrumbs.innerHTML = node.pathNodes.map(function (pathNode, index) {
      const separator = index === 0 ? '' : '<span class="ct-crumb-separator">/</span>';
      const current = pathNode.id === node.id ? ' aria-current="page"' : '';
      return separator + '<button type="button" data-ct-select="' + escAttr(pathNode.id) + '"' + current + '>' + esc(pathNode.label) + '</button>';
    }).join('');
  }

  function renderAncestorChain(node) {
    ancestorChain.innerHTML = node.pathNodes.map(function (pathNode) {
      const isCurrent = pathNode.id === node.id;
      return [
        '<button type="button" class="ct-chain-item' + (isCurrent ? ' is-current' : '') + '" data-ct-select="' + escAttr(pathNode.id) + '">',
        '<span class="ct-chain-label">' + esc(pathNode.label) + '</span>',
        '<span class="ct-chain-meta">' + esc(compactNodeSummary(pathNode)) + '</span>',
        '</button>',
      ].join('');
    }).join('');
  }

  function renderCurrentNode(node) {
    const parentButton = node.parent
      ? '<button type="button" class="ct-secondary-action" data-ct-select="' + escAttr(node.parent.id) + '">Parent</button>'
      : '';
    const openLink = node.url
      ? '<a class="ct-primary-link" href="' + escAttr(node.url) + '">Open page</a>'
      : '';
    const descendants = node.children.length
      ? '<p class="ct-current-preview">' + esc(node.children.slice(0, 5).map(function (child) { return child.label; }).join(' / ')) + '</p>'
      : '';

    currentNode.innerHTML = [
      '<div class="ct-current-header">',
      '<span class="ct-kind">' + esc(kindLabel(node)) + '</span>',
      '<span class="ct-depth">' + esc(depthLabel(node)) + '</span>',
      '</div>',
      '<h2>' + esc(node.label) + '</h2>',
      '<p class="ct-current-path">' + esc(node.path.join(' / ')) + '</p>',
      '<p class="ct-current-counts">' + esc(nodeSummary(node)) + '</p>',
      descendants,
      '<div class="ct-actions">',
      parentButton,
      openLink,
      '</div>',
    ].join('');
  }

  function renderChildren(node) {
    if (!node.children.length) {
      childNodes.innerHTML = [
        '<div class="ct-section-heading">',
        '<h2>No deeper branch</h2>',
        '<p>Open this page, search for another item, or move back up the path.</p>',
        '</div>',
      ].join('');
      return;
    }

    const cards = node.children.map(function (child) {
      const preview = child.children.length
        ? '<span class="ct-node-preview">' + esc(child.children.slice(0, 4).map(function (grandchild) { return grandchild.label; }).join(' / ')) + '</span>'
        : '';
      return [
        '<button type="button" class="ct-node-card ct-kind-' + escAttr(child.kind) + '" data-ct-select="' + escAttr(child.id) + '">',
        '<span class="ct-node-topline">',
        '<span class="ct-kind">' + esc(kindLabel(child)) + '</span>',
        '<span class="ct-node-count">' + esc(compactNodeSummary(child)) + '</span>',
        '</span>',
        '<strong>' + esc(child.label) + '</strong>',
        preview,
        '</button>',
      ].join('');
    }).join('');

    childNodes.innerHTML = [
      '<div class="ct-section-heading">',
      '<h2>Next choices</h2>',
      '<p>Only successors of the current node are shown here; unrelated branches stay out of the way.</p>',
      '</div>',
      '<div class="ct-child-grid">',
      cards,
      '</div>',
    ].join('');
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
          '<span>' + esc(node.path.join(' / ')) + '</span>',
          '</button>',
        ].join('');
      }).join(''),
      '</div>',
    ].join('');
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
    if (!hash.startsWith('ct=')) return null;
    try {
      return decodeURIComponent(hash.slice(3));
    } catch (error) {
      return null;
    }
  }

  function nodeSummary(node) {
    if (node.kind !== 'branch') return kindLabel(node);
    return plural(node.leafCount, 'item') + ' across ' + plural(node.children.length, 'next choice', 'next choices');
  }

  function compactNodeSummary(node) {
    if (node.kind !== 'branch') return kindLabel(node);
    return plural(node.leafCount, 'item');
  }

  function depthLabel(node) {
    return node.parent ? 'Level ' + (node.pathNodes.length - 1) : 'Root';
  }

  function kindLabel(node) {
    if (node.kind === 'branch') return 'Branch';
    if (node.kind === 'paper') return 'Paper';
    if (node.kind === 'page') return 'Page';
    return 'Link';
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
