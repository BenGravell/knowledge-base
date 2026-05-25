(function () {
  'use strict';

  const app = document.getElementById('tag-search-app') || document.getElementById('search-app');
  const data = window.tagSearchData;
  if (!app) return;

  if (!data || !data.papers) {
    app.innerHTML = '<p class="tag-search-empty">Search data is unavailable. Run <code>mkdocs build</code> to regenerate it.</p>';
    return;
  }

  const workerUrl = '../javascripts/semantic-search-worker.js';
  const semanticLimit = 80;
  const modeLabels = {
    metadata: 'Metadata',
    semantic: 'Semantic',
    site: 'Site',
  };
  const fieldConfig = {
    tag: {
      label: 'Tag',
      plural: 'Tags',
      getValues: paper => paper.tags || [],
    },
    author: {
      label: 'Author',
      plural: 'Authors',
      getValues: paper => paper.authors || [],
    },
    year: {
      label: 'Year',
      plural: 'Years',
      getValues: paper => paper.year ? [String(paper.year)] : [],
    },
    source: {
      label: 'Source',
      plural: 'Sources',
      getValues: paper => paper.source ? [paper.source] : [],
    },
    type: {
      label: 'Type',
      plural: 'Types',
      getValues: paper => paper.type ? [paper.type] : [],
    },
  };

  const papers = Object.values(data.papers).map(paper => {
    const authors = Array.isArray(paper.authors) ? paper.authors : [];
    const tags = Array.isArray(paper.tags) ? paper.tags : [];
    return Object.assign({}, paper, {
      authors,
      tags,
      searchText: normalizeText([
        paper.title,
        paper.label,
        paper.algorithm,
        authors.join(' '),
        paper.year,
        paper.source,
        paper.type,
        tags.join(' '),
        paper.summary,
      ].join(' ')),
    });
  });
  const papersById = new Map(papers.map(paper => [paper.id, paper]));
  const facetIndex = buildFacetIndex(papers);

  let state = parseState();
  let worker = null;
  let workerReady = false;
  let workerLoading = false;
  let lastSemanticQuery = '';
  let latestSemanticRows = null;
  let semanticRequestId = 0;

  app.innerHTML =
    appHeader('Search') +
    '<section class="tag-search-settings unified-search-settings" aria-label="Search settings">' +
      '<div class="tag-search-settings-body unified-search-settings-body">' +
        '<div class="unified-search-query-section">' +
          '<form id="unified-search-form" class="tag-search-form unified-search-form" role="search">' +
            '<label for="unified-search-input">Search</label>' +
            '<div class="tag-search-input-row unified-search-input-row">' +
              '<input id="unified-search-input" type="search" autocomplete="off" placeholder="Search papers, authors, tags, sources, or concepts">' +
              '<button type="submit">Search</button>' +
            '</div>' +
          '</form>' +
          '<div class="unified-search-mode" aria-label="Search mode">' +
            Object.entries(modeLabels).map(([mode, label]) => (
              `<button type="button" data-search-mode="${escAttr(mode)}">${esc(label)}</button>`
            )).join('') +
          '</div>' +
        '</div>' +
        '<section class="unified-search-filter-section" aria-label="Metadata filters">' +
          '<div class="unified-search-section-title">Filters</div>' +
          '<div class="unified-search-filters">' +
            filterControl('author') +
            filterControl('year') +
            filterControl('source') +
            filterControl('type') +
          '</div>' +
          '<div id="unified-search-active" class="unified-search-active"></div>' +
        '</section>' +
        '<section class="unified-search-status-section" aria-label="Search status">' +
          '<div class="unified-search-section-title">Status</div>' +
          '<div class="semantic-search-status-wrap unified-search-status-wrap">' +
            '<p id="unified-search-status" class="semantic-search-status">Ready.</p>' +
          '</div>' +
        '</section>' +
        '<div id="unified-search-count" class="tag-search-count"><strong>0</strong><span>results</span></div>' +
      '</div>' +
    '</section>' +
    '<section id="unified-search-results-panel" class="tag-search-selection semantic-search-results-panel is-empty"></section>' +
    datalistMarkup('author') +
    datalistMarkup('year') +
    datalistMarkup('source') +
    datalistMarkup('type');

  const form = app.querySelector('#unified-search-form');
  const input = app.querySelector('#unified-search-input');
  const modeButtons = Array.from(app.querySelectorAll('[data-search-mode]'));
  const filterInputs = {
    author: app.querySelector('#unified-search-author'),
    year: app.querySelector('#unified-search-year'),
    source: app.querySelector('#unified-search-source'),
    type: app.querySelector('#unified-search-type'),
  };
  const activeFilters = app.querySelector('#unified-search-active');
  const status = app.querySelector('#unified-search-status');
  const count = app.querySelector('#unified-search-count');
  const panel = app.querySelector('#unified-search-results-panel');

  form.addEventListener('submit', event => {
    event.preventDefault();
    state.q = input.value.trim();
    syncUrl(true);
    render();
  });

  input.addEventListener('keydown', event => {
    if (event.key !== 'Escape') return;
    if (!state.q && !input.value) return;
    input.value = '';
    state.q = '';
    syncUrl(true);
    render();
  });

  modeButtons.forEach(button => {
    button.addEventListener('click', () => {
      state.mode = button.getAttribute('data-search-mode') || 'metadata';
      state.q = input.value.trim();
      if (state.mode !== 'metadata') state.paper = '';
      syncUrl(true);
      render();
      if (state.mode === 'site') openMaterialSearch(state.q);
    });
  });

  Object.entries(filterInputs).forEach(([field, element]) => {
    element.addEventListener('change', () => {
      state[field] = element.value.trim();
      if (field !== 'tag') state.paper = '';
      syncUrl(true);
      render();
    });
    element.addEventListener('keydown', event => {
      if (event.key !== 'Escape') return;
      element.value = '';
      state[field] = '';
      state.paper = '';
      syncUrl(true);
      render();
    });
  });

  panel.addEventListener('click', event => {
    const facetButton = event.target.closest('[data-search-facet]');
    if (facetButton) {
      const field = facetButton.getAttribute('data-search-facet');
      const value = facetButton.getAttribute('data-search-value') || '';
      if (field && Object.hasOwn(fieldConfig, field)) {
        state[field] = value;
        state.paper = '';
        if (field === 'tag') state.tag = value;
        syncUrl(true);
        render();
      }
      return;
    }

    const clearButton = event.target.closest('[data-search-clear]');
    if (clearButton) {
      clearState();
      syncUrl(true);
      render();
    }
  });

  activeFilters.addEventListener('click', event => {
    const button = event.target.closest('[data-clear-filter]');
    if (!button) return;
    const field = button.getAttribute('data-clear-filter');
    if (field === 'all') {
      clearState();
    } else if (Object.hasOwn(state, field)) {
      state[field] = '';
      if (field === 'tag') state.paper = '';
    }
    syncUrl(true);
    render();
  });

  window.addEventListener('popstate', () => {
    state = parseState();
    render();
  });

  render();

  function render() {
    syncControls();
    if (state.mode === 'semantic') {
      renderSemantic();
    } else if (state.mode === 'site') {
      renderSiteSearch();
    } else {
      renderMetadataSearch();
    }
  }

  function renderMetadataSearch() {
    workerLoading = false;
    const rows = metadataRows();
    const resultLabel = rows.length === 1 ? 'result' : 'results';
    count.innerHTML = `<strong>${rows.length}</strong><span>${resultLabel}</span>`;
    setStatus(metadataStatus(rows.length));
    panel.classList.remove('is-empty');

    const title = metadataTitle();
    panel.innerHTML =
      '<section class="tag-search-selected-head unified-search-result-head">' +
        '<div>' +
          `<span class="tag-search-kicker">${esc(metadataKicker())}</span>` +
          `<h2>${esc(title)}</h2>` +
        '</div>' +
        `<div class="tag-search-count"><strong>${rows.length}</strong><span>${resultLabel}</span></div>` +
      '</section>' +
      '<div class="unified-search-layout">' +
        renderFacetRail(rows.map(row => row.paper)) +
        '<div class="tag-search-results unified-search-results">' +
          (rows.length
            ? rows.slice(0, 160).map(renderMetadataCard).join('')
            : emptyBlock('No Results', 'No papers match the current query and filters.')) +
        '</div>' +
      '</div>';
  }

  function renderSemantic() {
    if (!state.q) {
      latestSemanticRows = null;
      lastSemanticQuery = '';
      count.innerHTML = '<strong>0</strong><span>results</span>';
      setStatus('Ready.');
      panel.classList.remove('is-empty');
      panel.innerHTML = emptyBlock('Semantic Search', 'Enter a concept or natural-language phrase, then run the search.');
      return;
    }

    if (latestSemanticRows && lastSemanticQuery === state.q) {
      renderSemanticRows(latestSemanticRows);
      return;
    }

    const requestId = ++semanticRequestId;
    lastSemanticQuery = state.q;
    latestSemanticRows = null;
    workerLoading = true;
    count.innerHTML = '<strong>...</strong><span>searching</span>';
    panel.classList.remove('is-empty');
    panel.innerHTML = emptyBlock('Searching', state.q);
    setStatus(workerReady ? 'Embedding query...' : 'Loading embedding model and vector index...');

    const activeWorker = ensureWorker(requestId);
    if (workerReady) {
      activeWorker.postMessage({ type: 'query', query: state.q, limit: semanticLimit });
    } else {
      activeWorker.postMessage({ type: 'init' });
    }
  }

  function renderSemanticRows(rows) {
    const enrichedRows = rows.map(row => {
      const semanticPaper = row.paper || {};
      const metadataPaper = papersById.get(semanticPaper.id) || {};
      return Object.assign({}, row, {
        paper: Object.assign({}, semanticPaper, metadataPaper),
      });
    });
    const filteredRows = enrichedRows
      .filter(row => matchesFilters(row.paper, { includeQuery: false }))
      .slice(0, 36);
    const resultLabel = filteredRows.length === 1 ? 'result' : 'results';
    count.innerHTML = `<strong>${filteredRows.length}</strong><span>${resultLabel}</span>`;
    setStatus(`Semantic ranking for "${state.q}".`);
    panel.classList.remove('is-empty');
    panel.innerHTML =
      '<section class="tag-search-selected-head unified-search-result-head">' +
        '<div>' +
          '<span class="tag-search-kicker">Semantic</span>' +
          `<h2>${esc(state.q)}</h2>` +
        '</div>' +
        `<div class="tag-search-count"><strong>${filteredRows.length}</strong><span>${resultLabel}</span></div>` +
      '</section>' +
      '<div class="unified-search-layout">' +
        renderFacetRail(filteredRows.map(row => row.paper)) +
        '<div class="paper-similar-list semantic-search-result-list unified-search-results">' +
          (filteredRows.length
            ? filteredRows.map(renderSemanticCard).join('')
            : emptyBlock('No Results', 'No semantic matches remain after applying the metadata filters.')) +
        '</div>' +
      '</div>';
  }

  function renderSiteSearch() {
    const label = state.q ? `Open the Material site search for "${state.q}".` : 'Open the Material site search for full-text page search.';
    count.innerHTML = '<strong>-</strong><span>site</span>';
    setStatus('Material site search is available from the header search bar.');
    panel.classList.remove('is-empty');
    panel.innerHTML =
      '<div class="tag-search-selection-empty unified-search-site-mode">' +
        '<h2>Material Site Search</h2>' +
        `<p>${esc(label)}</p>` +
        '<button type="button" id="unified-search-open-site">Open Site Search</button>' +
      '</div>';
    const button = panel.querySelector('#unified-search-open-site');
    button.addEventListener('click', () => openMaterialSearch(state.q));
  }

  function metadataRows() {
    const tagKey = normalizeFacet(state.tag);
    const ego = state.paper ? papersById.get(state.paper) : null;

    if (ego && tagKey) {
      return ((data.related && data.related[`${ego.id}::${tagKey}`]) || [])
        .map(item => ({ item, paper: papersById.get(item.id) }))
        .filter(row => row.paper && matchesFilters(row.paper, { includeQuery: true }));
    }

    return papers
      .filter(paper => matchesFilters(paper, { includeQuery: true }))
      .sort(comparePapers)
      .map(paper => ({ item: {}, paper }));
  }

  function matchesFilters(paper, options) {
    if (!paper) return false;
    if (options.includeQuery) {
      const terms = normalizeText(state.q).split(' ').filter(Boolean);
      if (terms.length && !terms.every(term => paper.searchText.includes(term))) return false;
    }
    return ['tag', 'author', 'year', 'source', 'type'].every(field => {
      const value = normalizeFacet(state[field]);
      if (!value) return true;
      return fieldConfig[field].getValues(paper).some(item => normalizeFacet(item) === value);
    });
  }

  function renderFacetRail(sourcePapers) {
    const sections = ['tag', 'author', 'year', 'source', 'type']
      .map(field => renderFacetSection(field, sourcePapers))
      .filter(Boolean)
      .join('');
    return `<aside class="unified-search-facet-rail" aria-label="Search facets">${sections}</aside>`;
  }

  function renderFacetSection(field, sourcePapers) {
    const counts = new Map();
    sourcePapers.forEach(paper => {
      const seen = new Set();
      fieldConfig[field].getValues(paper).forEach(value => {
        const label = clean(value);
        const key = normalizeFacet(label);
        if (!key || seen.has(key)) return;
        seen.add(key);
        if (!counts.has(key)) counts.set(key, { label, count: 0 });
        counts.get(key).count += 1;
      });
    });
    const rows = Array.from(counts.values())
      .sort((a, b) => b.count - a.count || a.label.localeCompare(b.label))
      .slice(0, field === 'tag' ? 18 : 12);
    if (!rows.length) return '';
    return (
      '<section class="unified-search-facet-section">' +
        `<h3>${esc(fieldConfig[field].plural)}</h3>` +
        '<div class="unified-search-facet-list">' +
          rows.map(row => (
            `<button type="button" data-search-facet="${escAttr(field)}" data-search-value="${escAttr(row.label)}">` +
              `<span>${esc(row.label)}</span><strong>${row.count}</strong>` +
            '</button>'
          )).join('') +
        '</div>' +
      '</section>'
    );
  }

  function renderMetadataCard(row, index) {
    const paper = row.paper;
    const score = Number.isFinite(row.item.score)
      ? `<span>${Math.round(row.item.score * 100)}% similar</span>`
      : '';
    const tags = (paper.tags || [])
      .slice(0, 8)
      .map(tag => `<a href="?tag=${encodeURIComponent(tag)}">${esc(tag)}</a>`)
      .join('');
    const authors = (paper.authors || []).slice(0, 3).join(', ');
    const meta = [
      paper.year || 'Undated',
      paper.type,
      paper.source,
      authors,
    ].filter(Boolean);

    return (
      '<article class="tag-search-card">' +
        '<div class="tag-search-rank">' + String(index + 1) + '</div>' +
        '<div class="tag-search-card-main">' +
          '<div class="tag-search-meta">' +
            meta.map(item => `<span>${esc(item)}</span>`).join('') +
            score +
          '</div>' +
          `<h2><a href="${escAttr(paper.url)}">${esc(paperTitle(paper))}</a></h2>` +
          (paper.label && paper.label !== paper.title ? `<p class="tag-search-label">${esc(paper.label)}</p>` : '') +
          (paper.summary ? `<p class="tag-search-summary">${esc(paper.summary)}</p>` : '') +
          (tags ? `<div class="tag-search-tags">${tags}</div>` : '') +
          '<div class="paper-link-pills tag-search-actions">' +
            actionLink(paper.url, 'Detail') +
            actionLink(paper.mapUrl, 'Map') +
            actionLink(paper.treeUrl, 'Tree') +
          '</div>' +
        '</div>' +
      '</article>'
    );
  }

  function renderSemanticCard(row, index) {
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

  function ensureWorker(requestId) {
    if (worker) return worker;
    worker = new Worker(workerUrl, { type: 'module' });
    worker.addEventListener('message', event => {
      const message = event.data || {};
      if (message.type === 'ready') {
        workerReady = true;
        workerLoading = false;
        setStatus(`Ready. ${message.count || 0} papers indexed with ${message.model || 'the browser model'}.`);
        if (lastSemanticQuery) worker.postMessage({ type: 'query', query: lastSemanticQuery, limit: semanticLimit });
      } else if (message.type === 'status') {
        setStatus(message.message || 'Working...');
      } else if (message.type === 'results') {
        if (requestId !== semanticRequestId && message.query !== state.q) return;
        workerLoading = false;
        latestSemanticRows = message.results || [];
        lastSemanticQuery = message.query || state.q;
        renderSemanticRows(latestSemanticRows);
      } else if (message.type === 'error') {
        workerLoading = false;
        renderError(message.message || 'Semantic search failed.');
      }
    });
    worker.addEventListener('error', event => {
      workerLoading = false;
      renderError(event.message || 'Semantic search worker failed.');
    });
    return worker;
  }

  function openMaterialSearch(query) {
    const toggle = document.getElementById('__search');
    const searchInput = document.querySelector('.md-search__input');
    if (toggle) toggle.checked = true;
    if (!searchInput) return;
    searchInput.focus();
    if (query) {
      searchInput.value = query;
      searchInput.dispatchEvent(new Event('input', { bubbles: true }));
      searchInput.dispatchEvent(new KeyboardEvent('keyup', { bubbles: true }));
    }
  }

  function syncControls() {
    input.value = state.q || '';
    Object.entries(filterInputs).forEach(([field, element]) => {
      element.value = state[field] || '';
    });
    modeButtons.forEach(button => {
      const active = button.getAttribute('data-search-mode') === state.mode;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    activeFilters.innerHTML = renderActiveFilters();
  }

  function renderActiveFilters() {
    const filters = ['tag', 'author', 'year', 'source', 'type']
      .filter(field => state[field])
      .map(field => (
        `<button type="button" data-clear-filter="${escAttr(field)}">` +
          `<span>${esc(fieldConfig[field].label)}: ${esc(state[field])}</span>` +
        '</button>'
      ));
    if (state.q) {
      filters.unshift(
        `<button type="button" data-clear-filter="q"><span>Query: ${esc(state.q)}</span></button>`
      );
    }
    if (!filters.length) return '<span class="unified-search-active-empty">No active filters</span>';
    filters.push('<button type="button" data-clear-filter="all" class="unified-search-clear-all">Clear All</button>');
    return filters.join('');
  }

  function filterControl(field) {
    const id = `unified-search-${field}`;
    const type = field === 'year' ? 'number' : 'text';
    return (
      '<label class="unified-search-filter">' +
        `<span>${esc(fieldConfig[field].label)}</span>` +
        `<input id="${escAttr(id)}" type="${type}" list="${escAttr(id)}-list" autocomplete="off">` +
      '</label>'
    );
  }

  function datalistMarkup(field) {
    const id = `unified-search-${field}-list`;
    const rows = Array.from(facetIndex[field].values())
      .sort((a, b) => b.count - a.count || a.label.localeCompare(b.label))
      .slice(0, field === 'author' ? 260 : 180);
    return `<datalist id="${escAttr(id)}">${rows.map(row => `<option value="${escAttr(row.label)}"></option>`).join('')}</datalist>`;
  }

  function buildFacetIndex(items) {
    const index = {};
    Object.keys(fieldConfig).forEach(field => {
      index[field] = new Map();
    });
    items.forEach(paper => {
      Object.entries(fieldConfig).forEach(([field, config]) => {
        const seen = new Set();
        config.getValues(paper).forEach(value => {
          const label = clean(value);
          const key = normalizeFacet(label);
          if (!key || seen.has(key)) return;
          seen.add(key);
          if (!index[field].has(key)) index[field].set(key, { label, count: 0 });
          index[field].get(key).count += 1;
        });
      });
    });
    return index;
  }

  function parseState() {
    const params = new URLSearchParams(window.location.search);
    const defaultMode = app.dataset.defaultMode || 'metadata';
    const rawMode = params.get('mode') || defaultMode;
    const mode = Object.hasOwn(modeLabels, rawMode) ? rawMode : 'metadata';
    return {
      mode,
      q: params.get('q') || '',
      tag: params.get('tag') || '',
      author: params.get('author') || '',
      year: params.get('year') || '',
      source: params.get('source') || '',
      type: params.get('type') || params.get('source_type') || '',
      paper: params.get('paper') || '',
    };
  }

  function syncUrl(push) {
    const nextUrl = new URL(window.location.href);
    nextUrl.search = '';
    if (state.mode !== 'metadata') nextUrl.searchParams.set('mode', state.mode);
    if (state.q) nextUrl.searchParams.set('q', state.q);
    ['tag', 'author', 'year', 'source', 'type'].forEach(field => {
      if (state[field]) nextUrl.searchParams.set(field, state[field]);
    });
    if (state.paper && state.tag) nextUrl.searchParams.set('paper', state.paper);
    if (push) {
      window.history.pushState({}, '', nextUrl);
    } else {
      window.history.replaceState({}, '', nextUrl);
    }
  }

  function clearState() {
    state.q = '';
    state.tag = '';
    state.author = '';
    state.year = '';
    state.source = '';
    state.type = '';
    state.paper = '';
    latestSemanticRows = null;
    lastSemanticQuery = '';
  }

  function metadataTitle() {
    if (state.paper && state.tag) {
      const ego = papersById.get(state.paper);
      const paper = ego ? paperTitle(ego) : 'Selected Paper';
      return `${state.tag} near ${paper}`;
    }
    const active = ['tag', 'author', 'year', 'source', 'type']
      .filter(field => state[field])
      .map(field => `${fieldConfig[field].label}: ${state[field]}`);
    if (state.q) active.unshift(state.q);
    return active.length ? active.join(' / ') : 'All Papers';
  }

  function metadataKicker() {
    if (state.paper && state.tag) return 'Related Tag';
    if (state.tag) return 'Tag';
    if (state.author) return 'Author';
    if (state.year) return 'Year';
    if (state.source) return 'Source';
    if (state.type) return 'Type';
    return 'Metadata';
  }

  function metadataStatus(total) {
    if (state.paper && state.tag) return 'Showing related papers ranked by shared-tag similarity when available.';
    if (state.q || state.tag || state.author || state.year || state.source || state.type) {
      return `Matched ${total} papers across metadata fields.`;
    }
    return 'Ready.';
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

  function emptyBlock(title, message) {
    return (
      '<div class="tag-search-selection-empty">' +
        `<h2>${esc(title)}</h2>` +
        `<p>${esc(message)}</p>` +
      '</div>'
    );
  }

  function actionLink(url, label) {
    return url
      ? `<a class="paper-link-pill paper-link-pill--internal" href="${escAttr(url)}"><span class="paper-link-pill__label">${esc(label)}</span></a>`
      : '';
  }

  function appHeader(title) {
    return (
      '<header class="kb-app-header kb-app-header--static tag-search-header">' +
        `<h1 class="kb-app-header-title">${esc(title)}</h1>` +
      '</header>'
    );
  }

  function setStatus(message) {
    status.textContent = workerLoading ? message : message || 'Ready.';
  }

  function comparePapers(a, b) {
    return paperYear(b) - paperYear(a) || paperTitle(a).localeCompare(paperTitle(b));
  }

  function paperYear(paper) {
    const year = Number.parseInt(paper.year, 10);
    return Number.isFinite(year) ? year : 0;
  }

  function paperTitle(paper) {
    return paper.title || paper.label || paper.id || 'Untitled paper';
  }

  function paperYearByline(paper) {
    const authors = Array.isArray(paper.authors) ? paper.authors : [];
    const author = authors.length ? authors[0] + (authors.length > 1 ? ' et al.' : '') : '';
    return [author, paper.year].filter(Boolean).join(' / ');
  }

  function clean(value) {
    return String(value == null ? '' : value).trim();
  }

  function normalizeText(value) {
    return clean(value).replace(/\s+/g, ' ').toLowerCase();
  }

  function normalizeFacet(value) {
    return normalizeText(value);
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
    return esc(value).replace(/`/g, '&#96;');
  }
})();
