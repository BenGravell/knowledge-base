(function () {
  'use strict';

  const app = document.getElementById('semantic-search-app');
  if (!app) return;

  const workerUrl = '../javascripts/semantic-search-worker.js';
  const defaultQuery = new URLSearchParams(window.location.search).get('q') || '';
  const queryPlaceholder = 'Search for a concept such as "safe motion planning with uncertainty" or "model predictive control for agile robots".';
  let worker = null;
  let ready = false;
  let loading = false;
  let lastQuery = '';

  app.innerHTML =
    appHeader('Semantic Search') +
    '<section class="tag-search-settings semantic-search-settings" aria-label="Semantic Search settings">' +
      '<div class="tag-search-settings-body semantic-search-settings-body">' +
        '<form id="semantic-search-form" class="tag-search-form semantic-search-form" role="search">' +
          '<label for="semantic-search-input">Search Phrase</label>' +
          '<div class="tag-search-input-row semantic-search-input-row">' +
            `<input id="semantic-search-input" type="search" autocomplete="off" placeholder="${escAttr(queryPlaceholder)}" value="${escAttr(defaultQuery)}">` +
            '<button type="submit">Search</button>' +
          '</div>' +
        '</form>' +
        '<div class="semantic-search-status-wrap">' +
          '<span class="tag-search-kicker">Status</span>' +
          '<p id="semantic-search-status" class="semantic-search-status">Ready.</p>' +
        '</div>' +
        '<div id="semantic-search-count" class="tag-search-count"><strong>0</strong><span>results</span></div>' +
      '</div>' +
    '</section>' +
    '<section id="semantic-search-results-panel" class="tag-search-selection semantic-search-results-panel is-empty"></section>';

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
    renderIdle();
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
      renderIdle();
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
    panel.classList.remove('is-empty');
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

    panel.classList.remove('is-empty');
    panel.innerHTML = `<div class="paper-similar-list semantic-search-result-list">${results.map(renderResult).join('')}</div>`;
  }

  function renderIdle() {
    loading = false;
    lastQuery = '';
    count.innerHTML = '<strong>0</strong><span>results</span>';
    setStatus('Ready.');
    panel.classList.add('is-empty');
    panel.innerHTML = '';
  }

  function renderEmpty(title, message) {
    loading = false;
    count.innerHTML = '<strong>0</strong><span>results</span>';
    setStatus('Ready.');
    panel.classList.remove('is-empty');
    panel.innerHTML =
      '<div class="tag-search-selection-empty">' +
        `<h2>${esc(title)}</h2>` +
        `<p>${esc(message)}</p>` +
      '</div>';
  }

  function renderError(message) {
    count.innerHTML = '<strong>!</strong><span>error</span>';
    setStatus(message);
    panel.classList.remove('is-empty');
    panel.innerHTML =
      '<div class="tag-search-selection-empty semantic-search-error">' +
        '<h2>Search Unavailable</h2>' +
        `<p>${esc(message)}</p>` +
      '</div>';
  }

  function renderResult(row, index) {
    const paper = row.paper || {};
    const scorePercent = Number.isFinite(row.score)
      ? Math.max(0, Math.min(100, Math.round(row.score * 100)))
      : 0;
    const scoreGaugeDegrees = Math.round(scorePercent * 1.8 * 10) / 10;
    const scoreLabel = `${scorePercent}% match`;
    const byline = paper.byline || paperYearByline(paper);
    return (
      '<article class="paper-similar-card">' +
        `<div class="paper-similar-card__rank" style="--paper-similar-gauge: ${scoreGaugeDegrees}deg;" aria-label="${escAttr(scoreLabel)}">` +
          `<div class="paper-similar-card__rank-top">${String(index + 1)}</div>` +
          '<div class="paper-similar-card__rank-bottom">' +
            `<span>${scorePercent}%</span>` +
          '</div>' +
        '</div>' +
        '<div class="paper-similar-card__body">' +
          `<h3><a href="${escAttr(paper.url || '#')}">${esc(paperTitle(paper))}</a></h3>` +
          (paper.label && paper.label !== paper.title ? `<p class="paper-similar-card__label">${esc(paper.label)}</p>` : '') +
          (byline ? `<div class="paper-similar-card__meta"><span>${esc(byline)}</span></div>` : '') +
          '<div class="paper-link-pills paper-similar-card__actions">' +
            actionLink(paper.url, 'Detail') +
            actionLink(paper.mapUrl, 'Map') +
            actionLink(paper.treeUrl, 'Tree') +
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

  function paperYearByline(paper) {
    return paper.year ? String(paper.year) : '';
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
