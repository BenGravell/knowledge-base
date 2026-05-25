(function () {
  'use strict';

  const app = document.getElementById('semantic-search-app');
  if (!app) return;

  const workerUrl = '../javascripts/semantic-search-worker.js';
  const defaultQuery = new URLSearchParams(window.location.search).get('q') || '';
  let worker = null;
  let ready = false;
  let loading = false;
  let lastQuery = '';

  app.innerHTML =
    appHeader('Semantic Search') +
    '<section class="tag-search-hero semantic-search-hero">' +
      '<div>' +
        '<span class="tag-search-kicker">Exploratory Search</span>' +
        '<h1>Find papers by meaning</h1>' +
        '<p>Type a phrase, method, problem, or research direction.</p>' +
      '</div>' +
      '<div id="semantic-search-count" class="tag-search-count"><strong>0</strong><span>results</span></div>' +
    '</section>' +
    '<section class="tag-search-settings semantic-search-settings" aria-label="Semantic Search settings">' +
      '<div class="tag-search-settings-body semantic-search-settings-body">' +
        '<form id="semantic-search-form" class="tag-search-form semantic-search-form" role="search">' +
          '<label for="semantic-search-input">Search Phrase</label>' +
          '<div class="tag-search-input-row semantic-search-input-row">' +
            `<input id="semantic-search-input" type="search" autocomplete="off" value="${escAttr(defaultQuery)}">` +
            '<button type="submit">Search</button>' +
          '</div>' +
        '</form>' +
        '<div class="semantic-search-status-wrap">' +
          '<span class="tag-search-kicker">Status</span>' +
          '<p id="semantic-search-status" class="semantic-search-status">Ready.</p>' +
        '</div>' +
      '</div>' +
    '</section>' +
    '<section id="semantic-search-results-panel" class="tag-search-selection semantic-search-results-panel">' +
      '<div class="tag-search-selection-empty">' +
        '<h2>No Query Yet</h2>' +
        '<p>Search for a concept such as "safe motion planning with uncertainty" or "model predictive control for agile robots".</p>' +
      '</div>' +
    '</section>';

  const form = app.querySelector('#semantic-search-form');
  const input = app.querySelector('#semantic-search-input');
  const status = app.querySelector('#semantic-search-status');
  const count = app.querySelector('#semantic-search-count');
  const panel = app.querySelector('#semantic-search-results-panel');

  form.addEventListener('submit', event => {
    event.preventDefault();
    runQuery(input.value.trim(), true);
  });

  input.addEventListener('keydown', event => {
    if (event.key !== 'Escape' || !input.value) return;
    input.value = '';
    renderEmpty('No Query Yet', 'Search for a concept such as "safe motion planning with uncertainty" or "model predictive control for agile robots".');
    syncUrl('');
  });

  if (defaultQuery) {
    runQuery(defaultQuery, false);
  }

  function ensureWorker() {
    if (worker) return worker;
    worker = new Worker(workerUrl, { type: 'module' });
    worker.addEventListener('message', event => {
      const message = event.data || {};
      if (message.type === 'ready') {
        ready = true;
        loading = false;
        setStatus(`Ready. ${message.count || 0} papers indexed with ${message.model || 'the browser model'}.`);
        if (lastQuery) worker.postMessage({ type: 'query', query: lastQuery, limit: 24 });
      } else if (message.type === 'status') {
        setStatus(message.message || 'Working...');
      } else if (message.type === 'results') {
        loading = false;
        renderResults(message.query, message.results || [], message.elapsedMs);
      } else if (message.type === 'error') {
        loading = false;
        renderError(message.message || 'Semantic search failed.');
      }
    });
    worker.addEventListener('error', event => {
      loading = false;
      renderError(event.message || 'Semantic search worker failed.');
    });
    return worker;
  }

  function runQuery(query, updateUrl) {
    if (!query) {
      renderEmpty('No Query Yet', 'Type a phrase to search by semantic similarity.');
      syncUrl('');
      return;
    }
    lastQuery = query;
    loading = true;
    renderLoading(query);
    if (updateUrl) syncUrl(query);
    const activeWorker = ensureWorker();
    if (ready) {
      activeWorker.postMessage({ type: 'query', query, limit: 24 });
    } else {
      activeWorker.postMessage({ type: 'init' });
    }
  }

  function renderLoading(query) {
    setStatus(ready ? 'Embedding query...' : 'Loading embedding model and vector index...');
    count.innerHTML = '<strong>...</strong><span>searching</span>';
    panel.innerHTML =
      '<div class="tag-search-selection-empty">' +
        '<h2>Searching</h2>' +
        `<p>${esc(query)}</p>` +
      '</div>';
  }

  function renderResults(query, results, elapsedMs) {
    const resultLabel = results.length === 1 ? 'result' : 'results';
    count.innerHTML = `<strong>${results.length}</strong><span>${resultLabel}</span>`;
    setStatus(`Searched ${resultLabel} in ${Math.max(1, Math.round(elapsedMs || 0))} ms after embedding.`);
    if (!results.length) {
      renderEmpty('No Results', `No indexed papers matched "${query}".`);
      return;
    }

    panel.innerHTML =
      '<section class="tag-search-selected-head">' +
        '<div>' +
          '<span class="tag-search-kicker">Query</span>' +
          `<h2>${esc(query)}</h2>` +
        '</div>' +
        `<div class="tag-search-count"><strong>${results.length}</strong><span>${resultLabel}</span></div>` +
      '</section>' +
      `<div class="tag-search-results">${results.map(renderResult).join('')}</div>`;
  }

  function renderEmpty(title, message) {
    loading = false;
    count.innerHTML = '<strong>0</strong><span>results</span>';
    setStatus('Ready.');
    panel.innerHTML =
      '<div class="tag-search-selection-empty">' +
        `<h2>${esc(title)}</h2>` +
        `<p>${esc(message)}</p>` +
      '</div>';
  }

  function renderError(message) {
    count.innerHTML = '<strong>!</strong><span>error</span>';
    setStatus(message);
    panel.innerHTML =
      '<div class="tag-search-selection-empty semantic-search-error">' +
        '<h2>Search Unavailable</h2>' +
        `<p>${esc(message)}</p>` +
      '</div>';
  }

  function renderResult(row, index) {
    const paper = row.paper || {};
    const score = Number.isFinite(row.score)
      ? `<span>${Math.round(row.score * 100)}% match</span>`
      : '';
    const tags = (paper.tags || [])
      .slice(0, 8)
      .map(tag => `<a href="../tag-search/?tag=${encodeURIComponent(tag)}">${esc(tag)}</a>`)
      .join('');
    return (
      '<article class="tag-search-card">' +
        '<div class="tag-search-rank">' + String(index + 1) + '</div>' +
        '<div class="tag-search-card-main">' +
          '<div class="tag-search-meta">' +
            `<span>${esc(paper.year || 'Undated')}</span>` +
            score +
          '</div>' +
          `<h2><a href="${escAttr(paper.url || '#')}">${esc(paperTitle(paper))}</a></h2>` +
          (paper.label && paper.label !== paper.title ? `<p class="tag-search-label">${esc(paper.label)}</p>` : '') +
          (paper.summary ? `<p class="tag-search-summary">${esc(paper.summary)}</p>` : '') +
          (tags ? `<div class="tag-search-tags">${tags}</div>` : '') +
          '<div class="paper-link-pills tag-search-actions">' +
            actionLink(paper.url, 'Open Detail Page') +
            actionLink(paper.mapUrl, 'Open in Map') +
            actionLink(paper.treeUrl, 'Open in Tree') +
          '</div>' +
        '</div>' +
      '</article>'
    );
  }

  function actionLink(url, label) {
    return url
      ? `<a class="paper-link-pill paper-link-pill--internal" href="${escAttr(url)}"><span class="paper-link-pill__label">${esc(label)}</span></a>`
      : '';
  }

  function setStatus(message) {
    status.textContent = loading ? message : message || 'Ready.';
  }

  function syncUrl(query) {
    const nextUrl = new URL(window.location.href);
    nextUrl.search = '';
    if (query) nextUrl.searchParams.set('q', query);
    window.history.pushState({}, '', nextUrl);
  }

  function appHeader(title) {
    return (
      '<header class="kb-app-header kb-app-header--static tag-search-header">' +
        `<h1 class="kb-app-header-title">${esc(title)}</h1>` +
      '</header>'
    );
  }

  function paperTitle(paper) {
    return paper.title || paper.label || paper.id || 'Untitled Paper';
  }

  function esc(value) {
    return String(value || '').replace(/[&<>"']/g, char => ({
      '&': '&amp;',
      '<': '&lt;',
      '>': '&gt;',
      '"': '&quot;',
      "'": '&#39;',
    }[char]));
  }

  function escAttr(value) {
    return esc(value).replace(/`/g, '&#96;');
  }
})();
