(function () {
  'use strict';

  const app = document.getElementById('tag-search-app') || document.getElementById('search-app');
  const data = window.tagSearchData;
  if (!app) return;

  if (!data || !data.papers) {
    app.innerHTML = '<p class="tag-search-empty">Search data is unavailable. Run <code>kb build</code> to regenerate it.</p>';
    return;
  }

  const scriptUrl = new URL(
    document.currentScript && document.currentScript.src ? document.currentScript.src : '../javascripts/search.js',
    window.location.href
  );
  const workerUrl = new URL('semantic-search-worker.js', scriptUrl).href;
  const semanticSettingsUrl = new URL('semantic-search-settings.json', scriptUrl).href;
  const semanticLimit = 80;
  const semanticDisplayLimit = 20;
  const semanticWarmupDelayMs = 800;
  const semanticQueryWarmupDelayMs = 250;
  const semanticQueryCacheLimit = 8;
  const fallbackSemanticScoreThreshold = 0.25;
  const metadataConnectorWords = new Set(['and']);
  const modeLabels = {
    metadata: 'Metadata',
    semantic: 'Semantic',
  };
  const configuredDefaultMode = app.dataset.defaultMode || '';
  const defaultMode = Object.hasOwn(modeLabels, configuredDefaultMode)
    ? configuredDefaultMode
    : 'metadata';
  const settingsDefault = app.dataset.settingsDefault || 'closed';
  const settingsOpenByDefault = settingsDefault === 'open';
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
  const filterFields = ['tag', 'author', 'year', 'source', 'type'];
  const icons = {
    search: '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="m21 21-4.35-4.35"></path><circle cx="10.5" cy="10.5" r="6.5"></circle></svg>',
    metadata: '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><ellipse cx="12" cy="5" rx="7" ry="3"></ellipse><path d="M5 5v6c0 1.66 3.13 3 7 3s7-1.34 7-3V5"></path><path d="M5 11v6c0 1.66 3.13 3 7 3s7-1.34 7-3v-6"></path></svg>',
    semantic: '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 3l1.6 4.4L18 9l-4.4 1.6L12 15l-1.6-4.4L6 9l4.4-1.6L12 3z"></path><path d="M19 15l.8 2.2L22 18l-2.2.8L19 21l-.8-2.2L16 18l2.2-.8L19 15z"></path><path d="M5 14l.7 1.8L7.5 16.5l-1.8.7L5 19l-.7-1.8-1.8-.7 1.8-.7L5 14z"></path></svg>',
    abstract: '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M4 6h16"></path><path d="M4 12h16"></path><path d="M4 18h10"></path></svg>',
    tags: '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M20.59 13.41 13.42 20.58a2 2 0 0 1-2.83 0L3 13V3h10l7.59 7.59a2 2 0 0 1 0 2.82z"></path><path d="M7 7h.01"></path></svg>',
  };

  const papers = Object.values(data.papers).map(paper => {
    const authors = Array.isArray(paper.authors) ? paper.authors : [];
    const tags = Array.isArray(paper.tags) ? paper.tags : [];
    return Object.assign({}, paper, {
      authors,
      tags,
      searchText: metadataSearchText([
        paper.title,
        paper.label,
        paper.algorithm,
        paper.id,
        paper.doi,
        paper.arxiv_id,
        Array.isArray(paper.identifiers) ? paper.identifiers.join(' ') : '',
        authors.join(' '),
        paper.year,
        paper.source,
        paper.type,
        tags.join(' '),
        paper.abstract,
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
  let workerWarmupStarted = false;
  let workerWarmupTimer = null;
  let semanticQueryWarmupTimer = null;
  let pendingSemanticWarmQuery = '';
  let lastSemanticQuery = '';
  let latestSemanticRows = null;
  const semanticRowsCache = new Map();
  const semanticRowsInFlight = new Set();
  let semanticSuggestedScoreThreshold = null;
  let semanticScoreThreshold = fallbackSemanticScoreThreshold;
  let semanticThresholdTouched = false;
  let semanticSettingsLoaded = false;

  app.innerHTML =
    `<section id="unified-search-settings" class="tag-search-settings unified-search-settings${settingsOpenByDefault ? '' : ' is-collapsed'}" aria-label="Search settings">` +
      '<div class="tag-search-settings-header unified-search-settings-header kb-app-header">' +
        '<span class="kb-app-header-title">Search</span>' +
        '<form id="unified-search-form" class="tag-search-form unified-search-form unified-search-header-form" role="search">' +
          '<div class="tag-search-input-row unified-search-input-row">' +
            '<input id="unified-search-input" type="search" autocomplete="off" aria-label="Search papers, authors, tags, sources, or concepts" placeholder="Search papers">' +
            `<button class="unified-search-submit" type="submit" aria-label="Search">${icons.search}</button>` +
          '</div>' +
        '</form>' +
        `<div class="unified-search-mode" aria-label="Search mode" data-active-mode="${escAttr(state.mode)}">` +
          Object.entries(modeLabels).map(([mode, label]) => (
            `<button type="button" data-search-mode="${escAttr(mode)}">` +
              `<span class="unified-search-mode-icon">${icons[mode] || ''}</span>` +
              `<span>${esc(label)}</span>` +
            '</button>'
          )).join('') +
        '</div>' +
        `<button id="unified-search-settings-toggle" class="kb-app-header-action" type="button" aria-expanded="${settingsOpenByDefault ? 'true' : 'false'}" aria-controls="unified-search-settings-body">` +
          `<span id="unified-search-settings-state">${settingsOpenByDefault ? 'Hide Settings' : 'Show Settings'}</span>` +
        '</button>' +
      '</div>' +
      '<div id="unified-search-settings-body" class="tag-search-settings-body unified-search-settings-body">' +
        '<section class="unified-search-filter-section" aria-label="Metadata filters">' +
          '<div class="unified-search-section-title">Filters</div>' +
          `<div id="unified-search-facet-filters" class="unified-search-filters">${filterFields.map(filterExpander).join('')}</div>` +
          '<div id="unified-search-active" class="unified-search-active"></div>' +
        '</section>' +
        '<section class="unified-search-threshold-section" aria-label="Semantic similarity threshold">' +
          '<div class="unified-search-threshold-header">' +
            '<label class="unified-search-threshold-label" for="unified-search-threshold">' +
              '<span>Semantic Similarity Cutoff</span>' +
              '<strong id="unified-search-threshold-value">...</strong>' +
            '</label>' +
            '<button id="unified-search-threshold-reset" class="unified-search-threshold-reset" type="button" disabled>Suggested <span>...</span></button>' +
          '</div>' +
          '<input id="unified-search-threshold" class="unified-search-threshold-slider" type="range" min="0" max="100" step="5" value="0" aria-describedby="unified-search-threshold-reset" disabled>' +
        '</section>' +
      '</div>' +
    '</section>' +
    '<section id="unified-search-results-panel" class="tag-search-selection semantic-search-results-panel is-empty">' +
      '<div id="unified-search-count" class="tag-search-count unified-search-panel-count"><strong>0</strong><span>results</span></div>' +
      '<div id="unified-search-results-body" class="unified-search-results-body"></div>' +
    '</section>' +
    filterFields.map(datalistMarkup).join('');

  const form = app.querySelector('#unified-search-form');
  const input = app.querySelector('#unified-search-input');
  const settings = app.querySelector('#unified-search-settings');
  const settingsToggle = app.querySelector('#unified-search-settings-toggle');
  const settingsState = app.querySelector('#unified-search-settings-state');
  const modeControl = app.querySelector('.unified-search-mode');
  const modeButtons = Array.from(app.querySelectorAll('[data-search-mode]'));
  const filterInputs = Object.fromEntries(
    filterFields.map(field => [field, app.querySelector(`#unified-search-${field}`)])
  );
  const facetFilters = app.querySelector('#unified-search-facet-filters');
  const activeFilters = app.querySelector('#unified-search-active');
  const thresholdInput = app.querySelector('#unified-search-threshold');
  const thresholdValue = app.querySelector('#unified-search-threshold-value');
  const thresholdReset = app.querySelector('#unified-search-threshold-reset');
  const thresholdSuggested = app.querySelector('#unified-search-threshold-reset span');
  const count = app.querySelector('#unified-search-count');
  const panel = app.querySelector('#unified-search-results-panel');
  const resultsBody = app.querySelector('#unified-search-results-body');

  syncThresholdControl();
  loadSemanticSettings();

  if (settingsToggle && settings) {
    settingsToggle.addEventListener('click', () => {
      const collapsed = settings.classList.toggle('is-collapsed');
      settingsToggle.setAttribute('aria-expanded', String(!collapsed));
      updateSettingsState();
    });
    updateSettingsState();
  }

  form.addEventListener('submit', event => {
    event.preventDefault();
    state.q = input.value.trim();
    syncUrl(true);
    render();
  });

  input.addEventListener('focus', () => scheduleSemanticWarmup(0), { once: true });
  input.addEventListener('input', () => {
    scheduleSemanticWarmup(0);
    scheduleSemanticQueryWarmup();
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
      state.mode = button.getAttribute('data-search-mode') || defaultMode;
      state.q = input.value.trim();
      if (state.mode !== 'metadata') state.paper = '';
      syncUrl(true);
      render();
    });
  });

  Object.entries(filterInputs).forEach(([field, element]) => {
    element.addEventListener('change', () => {
      state[field] = element.value.trim();
      state.paper = '';
      useMetadataModeForEmptyQuery();
      syncUrl(true);
      render();
    });
    element.addEventListener('keydown', event => {
      if (event.key !== 'Escape') return;
      element.value = '';
      state[field] = '';
      state.paper = '';
      useMetadataModeForEmptyQuery();
      syncUrl(true);
      render();
    });
  });

  if (thresholdInput) {
    thresholdInput.addEventListener('input', () => {
      semanticThresholdTouched = true;
      semanticScoreThreshold = readSemanticScoreThreshold(Number(thresholdInput.value) / 100, semanticScoreThreshold);
      syncThresholdControl();
      if (state.mode === 'semantic' && latestSemanticRows && lastSemanticQuery === state.q) {
        renderSemanticRows(latestSemanticRows);
      }
    });
  }

  if (thresholdReset) {
    thresholdReset.addEventListener('click', () => {
      const previous = semanticScoreThreshold;
      semanticThresholdTouched = false;
      semanticScoreThreshold = semanticSuggestedScoreThreshold;
      syncThresholdControl();
      if (
        semanticScoreThreshold !== previous &&
        state.mode === 'semantic' &&
        latestSemanticRows &&
        lastSemanticQuery === state.q
      ) {
        renderSemanticRows(latestSemanticRows);
      }
    });
  }

  facetFilters.addEventListener('click', event => {
    if (handleFacetClick(event)) return;
  });

  panel.addEventListener('click', event => {
    if (handleFacetClick(event)) return;
    const resultToggle = event.target.closest('[data-result-toggle]');
    if (resultToggle) {
      toggleResultPanel(resultToggle);
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
    useMetadataModeForEmptyQuery();
    syncUrl(true);
    render();
  });

  window.addEventListener('popstate', () => {
    state = parseState();
    render();
  });

  render();
  scheduleSemanticWarmup(semanticWarmupDelayMs);

  function render() {
    syncControls();
    if (state.mode === 'semantic') {
      renderSemantic();
    } else {
      renderMetadataSearch();
    }
  }

  function renderMetadataSearch() {
    workerLoading = false;
    const rows = metadataRows();
    renderFacetFilters(rows.map(row => row.paper));
    const resultLabel = rows.length === 1 ? 'result' : 'results';
    renderCount(rows.length, resultLabel);
    panel.classList.remove('is-empty');

    const title = metadataTitle();
    const kicker = metadataKicker();
    resultsBody.innerHTML =
      '<section class="tag-search-selected-head unified-search-result-head">' +
        '<div>' +
          (kicker === 'Metadata' ? '' : `<span class="tag-search-kicker">${esc(kicker)}</span>`) +
          `<h2>${esc(title)}</h2>` +
        '</div>' +
      '</section>' +
      '<div class="tag-search-results unified-search-results">' +
        (rows.length
          ? rows.slice(0, 160).map(renderMetadataCard).join('')
          : emptyBlock('', 'No items match the current query and filters.')) +
      '</div>';
  }

  function renderSemantic() {
    renderFacetFilters(papers);
    if (!state.q) {
      workerLoading = false;
      latestSemanticRows = null;
      lastSemanticQuery = '';
      renderCount(0, 'results');
      panel.classList.remove('is-empty');
      resultsBody.innerHTML = '';
      return;
    }

    if (latestSemanticRows && lastSemanticQuery === state.q) {
      renderSemanticRows(latestSemanticRows);
      return;
    }

    const cachedRows = cachedSemanticRows(state.q);
    if (cachedRows) {
      latestSemanticRows = cachedRows;
      lastSemanticQuery = state.q;
      workerLoading = false;
      renderSemanticRows(cachedRows);
      return;
    }

    lastSemanticQuery = state.q;
    latestSemanticRows = null;
    workerLoading = true;
    renderCount('...', 'searching');
    panel.classList.remove('is-empty');
    renderProgress(workerReady ? 'Embedding query...' : 'Loading embedding model and vector index...');

    const activeWorker = ensureWorker();
    if (workerReady) {
      requestSemanticRows(state.q);
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
      .filter(row => Number(row.score) >= semanticScoreThreshold)
      .filter(row => matchesFilters(row.paper, { includeQuery: false }));
    const displayedRows = filteredRows.slice(0, semanticDisplayLimit);
    const hiddenCount = Math.max(0, filteredRows.length - displayedRows.length);
    renderFacetFilters(filteredRows.map(row => row.paper));
    const resultLabel = displayedRows.length === 1 ? 'result' : 'results';
    renderCount(displayedRows.length, resultLabel, hiddenCount);
    panel.classList.remove('is-empty');
    resultsBody.innerHTML =
      '<div class="paper-similar-list semantic-search-result-list unified-search-results">' +
        (displayedRows.length
          ? displayedRows.map(renderSemanticCard).join('')
          : emptyBlock('No Results', `No semantic matches remain above the ${semanticThresholdPercent()}% threshold after applying the metadata filters.`)) +
      '</div>';
  }

  function renderCount(value, label, hiddenCount = 0) {
    const hidden = Math.max(0, Number(hiddenCount) || 0);
    const limitNote = hidden
      ? `<small class="unified-search-limit-note">${hidden} more not displayed</small>`
      : '';
    count.innerHTML = `<strong>${esc(String(value))}</strong><span>${esc(label)}</span>${limitNote}`;
    panel.classList.toggle('has-hidden-results', hidden > 0);
  }

  function metadataRows() {
    const tagKey = normalizeFacet(state.tag);
    const ego = state.paper ? papersById.get(state.paper) : null;

    if (ego && tagKey) {
      return ((data.related && data.related[`${ego.id}::${tagKey}`]) || [])
        .map(item => ({ item, paper: papersById.get(item.id) }))
        .filter(row => row.paper && matchesFilters(row.paper, { includeQuery: true }));
    }

    if (ego) {
      return matchesFilters(ego, { includeQuery: true })
        ? [{ item: {}, paper: ego }]
        : [];
    }

    return papers
      .filter(paper => matchesFilters(paper, { includeQuery: true }))
      .sort(comparePapers)
      .map(paper => ({ item: {}, paper }));
  }

  function matchesFilters(paper, options) {
    if (!paper) return false;
    if (options.includeQuery) {
      const terms = metadataQueryTokens(state.q);
      if (terms.length && !terms.every(term => paper.searchText.includes(` ${term} `))) return false;
    }
    return filterFields.every(field => {
      const value = normalizeFacet(state[field]);
      if (!value) return true;
      return fieldConfig[field].getValues(paper).some(item => normalizeFacet(item) === value);
    });
  }

  function renderFacetFilters(sourcePapers) {
    filterFields.forEach(field => {
      const expander = facetFilters.querySelector(`[data-filter-expander="${escAttr(field)}"]`);
      const list = facetFilters.querySelector(`[data-search-facet-list="${escAttr(field)}"]`);
      const count = facetFilters.querySelector(`[data-search-facet-count="${escAttr(field)}"]`);
      if (!expander || !list || !count) return;
      const rows = facetRows(field, sourcePapers);
      list.innerHTML = rows.map(row => (
        `<button type="button" class="${normalizeFacet(state[field]) === normalizeFacet(row.label) ? 'is-active' : ''}" data-search-facet="${escAttr(field)}" data-search-value="${escAttr(row.label)}">` +
          `<span>${esc(row.label)}</span><strong>${row.count}</strong>` +
        '</button>'
      )).join('');
      count.textContent = String(rows.length);
      if (state[field]) expander.open = true;
    });
  }

  function facetRows(field, sourcePapers) {
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
    return rows;
  }

  function renderMetadataCard(row, index) {
    return renderResultCard(row.paper, index, null);
  }

  function renderSemanticCard(row, index) {
    return renderResultCard(row.paper || {}, index, row.score);
  }

  function renderResultCard(paper, index, score) {
    const algorithm = clean(paper.algorithm || (paper.label !== paper.title ? paper.label : ''));
    const abstract = clean(paper.abstract || paper.summary);
    const byline = paper.byline || paperYearByline(paper);
    const tags = (paper.tags || [])
      .slice(0, 8)
      .map(tag => `<a href="?tag=${encodeURIComponent(tag)}">${highlightSearchMatches(tag)}</a>`)
      .join('');
    const panelItems = [
      tags ? { kind: 'tags', label: 'Tags', icon: icons.tags, content: `<div class="tag-search-tags paper-similar-card__tags">${tags}</div>` } : null,
      abstract ? { kind: 'abstract', label: 'Abstract', icon: icons.abstract, content: `<p class="paper-similar-card__abstract">${highlightSearchMatches(abstract)}</p>` } : null,
    ].filter(Boolean);
    const toggles = panelItems.map(renderResultToggle).join('');
    const panels = panelItems.map(renderResultPanel).join('');
    return (
      '<article class="paper-similar-card">' +
        renderResultRank(index, score) +
        '<div class="paper-similar-card__body">' +
          `<h3><a href="${escAttr(paper.url || '#')}">${highlightSearchMatches(paperTitle(paper))}</a></h3>` +
          (algorithm ? `<p class="paper-similar-card__label">${highlightSearchMatches(algorithm)}</p>` : '') +
          (byline ? `<div class="paper-similar-card__meta"><span>${highlightSearchMatches(byline)}</span></div>` : '') +
          '<div class="paper-similar-card__actions">' +
            '<div class="paper-similar-card__action-row">' +
              '<div class="paper-link-pills paper-similar-card__action-links">' +
                window.kbSiteLinks.renderPaperSiteLinks(paper) +
              '</div>' +
              (toggles ? `<div class="paper-similar-card__toggles">${toggles}</div>` : '') +
            '</div>' +
            (panels ? `<div class="paper-similar-card__panels">${panels}</div>` : '') +
          '</div>' +
        '</div>' +
      '</article>'
    );
  }

  function renderResultToggle(item) {
    return (
      `<button class="paper-similar-card__toggle paper-similar-card__toggle--${escAttr(item.kind)}" type="button" ` +
        `data-result-toggle="${escAttr(item.kind)}" aria-expanded="false" aria-label="Show ${escAttr(item.label)}" title="${escAttr(item.label)}">` +
        `<span class="paper-similar-card__expander-icon">${item.icon}</span>` +
      '</button>'
    );
  }

  function renderResultPanel(item) {
    return (
      `<div class="paper-similar-card__panel paper-similar-card__panel--${escAttr(item.kind)}" data-result-panel="${escAttr(item.kind)}" hidden>` +
        item.content +
      '</div>'
    );
  }

  function toggleResultPanel(button) {
    const kind = button.getAttribute('data-result-toggle');
    const card = button.closest('.paper-similar-card');
    if (!kind || !card) return;
    const panelElement = Array.from(card.querySelectorAll('[data-result-panel]'))
      .find(panelItem => panelItem.getAttribute('data-result-panel') === kind);
    if (!panelElement) return;
    const nextExpanded = button.getAttribute('aria-expanded') !== 'true';
    const label = button.getAttribute('title') || kind;
    button.setAttribute('aria-expanded', String(nextExpanded));
    button.setAttribute('aria-label', `${nextExpanded ? 'Hide' : 'Show'} ${label}`);
    panelElement.hidden = !nextExpanded;
  }

  function renderResultRank(index, score) {
    const rank = String(index + 1);
    if (!Number.isFinite(score)) {
      return (
        `<div class="paper-similar-card__rank paper-similar-card__rank--number-only" aria-label="Result ${escAttr(rank)}">` +
          `<div class="paper-similar-card__rank-top">${rank}</div>` +
        '</div>'
      );
    }

    const scorePercent = Math.max(0, Math.min(100, Math.round(score * 100)));
    const scoreGaugeDegrees = Math.round(scorePercent * 1.8 * 10) / 10;
    const scoreLabel = `Result ${rank}, ${scorePercent}% match`;
    return (
      `<div class="paper-similar-card__rank" style="--paper-similar-gauge: ${scoreGaugeDegrees}deg;" aria-label="${escAttr(scoreLabel)}">` +
        `<div class="paper-similar-card__rank-top">${rank}</div>` +
        '<div class="paper-similar-card__rank-bottom">' +
          `<span>${scorePercent}%</span>` +
        '</div>' +
      '</div>'
    );
  }

  function ensureWorker() {
    if (worker) return worker;
    worker = new Worker(workerUrl, { type: 'module' });
    worker.addEventListener('message', event => {
      const message = event.data || {};
      if (message.type === 'ready') {
        workerReady = true;
        applyWorkerSemanticScoreSuggestion(message.scoreThreshold);
        if (lastSemanticQuery && state.mode === 'semantic' && state.q === lastSemanticQuery) {
          workerLoading = true;
          renderProgress('Embedding query...');
          requestSemanticRows(lastSemanticQuery);
        } else {
          workerLoading = false;
          warmPendingSemanticQuery();
        }
      } else if (message.type === 'status') {
        renderProgress(message.message || 'Working...');
      } else if (message.type === 'results') {
        const query = message.query || '';
        const rows = message.results || [];
        semanticRowsInFlight.delete(semanticQueryKey(query));
        cacheSemanticRows(query, rows);
        if (state.mode !== 'semantic') return;
        if (query !== state.q) return;
        workerLoading = false;
        applyWorkerSemanticScoreSuggestion(message.scoreThreshold);
        latestSemanticRows = rows;
        lastSemanticQuery = query || state.q;
        renderSemanticRows(latestSemanticRows);
      } else if (message.type === 'error') {
        semanticRowsInFlight.clear();
        if (state.mode !== 'semantic') return;
        workerLoading = false;
        renderError(message.message || 'Semantic search failed.');
      }
    });
    worker.addEventListener('error', event => {
      semanticRowsInFlight.clear();
      if (state.mode !== 'semantic') return;
      workerLoading = false;
      renderError(event.message || 'Semantic search worker failed.');
    });
    return worker;
  }

  function scheduleSemanticWarmup(delay) {
    if (workerReady || workerWarmupStarted || !window.Worker) return;
    if (workerWarmupTimer) {
      window.clearTimeout(workerWarmupTimer);
      workerWarmupTimer = null;
    }
    if (!delay) {
      warmSemanticSearch();
      return;
    }
    workerWarmupTimer = window.setTimeout(() => {
      workerWarmupTimer = null;
      if ('requestIdleCallback' in window) {
        window.requestIdleCallback(warmSemanticSearch, { timeout: 2000 });
      } else {
        warmSemanticSearch();
      }
    }, delay);
  }

  function warmSemanticSearch() {
    if (workerReady || workerWarmupStarted || !window.Worker) return;
    workerWarmupStarted = true;
    ensureWorker().postMessage({ type: 'init' });
  }

  function scheduleSemanticQueryWarmup() {
    if (semanticQueryWarmupTimer) {
      window.clearTimeout(semanticQueryWarmupTimer);
      semanticQueryWarmupTimer = null;
    }
    if (state.mode !== 'semantic') return;
    const query = input.value.trim();
    if (query.length < 2) return;
    pendingSemanticWarmQuery = query;
    semanticQueryWarmupTimer = window.setTimeout(() => {
      semanticQueryWarmupTimer = null;
      warmPendingSemanticQuery();
    }, semanticQueryWarmupDelayMs);
  }

  function warmPendingSemanticQuery() {
    const query = pendingSemanticWarmQuery.trim();
    if (!query || state.mode !== 'semantic' || input.value.trim() !== query) return;
    if (workerLoading) return;
    if (!workerReady || cachedSemanticRows(query, { touch: false })) return;
    requestSemanticRows(query);
  }

  function requestSemanticRows(query) {
    const key = semanticQueryKey(query);
    if (!key || semanticRowsInFlight.has(key)) return;
    semanticRowsInFlight.add(key);
    ensureWorker().postMessage({ type: 'query', query, limit: semanticLimit });
  }

  function cacheSemanticRows(query, rows) {
    const key = semanticQueryKey(query);
    if (!key) return;
    if (semanticRowsCache.has(key)) semanticRowsCache.delete(key);
    semanticRowsCache.set(key, rows);
    while (semanticRowsCache.size > semanticQueryCacheLimit) {
      semanticRowsCache.delete(semanticRowsCache.keys().next().value);
    }
  }

  function cachedSemanticRows(query, options = {}) {
    const key = semanticQueryKey(query);
    if (!key || !semanticRowsCache.has(key)) return null;
    const rows = semanticRowsCache.get(key);
    if (options.touch !== false) {
      semanticRowsCache.delete(key);
      semanticRowsCache.set(key, rows);
    }
    return rows;
  }

  function semanticQueryKey(query) {
    return normalizeText(query);
  }

  function syncControls() {
    input.value = state.q || '';
    if (modeControl) modeControl.dataset.activeMode = state.mode;
    Object.entries(filterInputs).forEach(([field, element]) => {
      element.value = state[field] || '';
    });
    modeButtons.forEach(button => {
      const active = button.getAttribute('data-search-mode') === state.mode;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    activeFilters.innerHTML = renderActiveFilters();
    syncThresholdControl();
  }

  function updateSettingsState() {
    if (!settingsState || !settings || !settingsToggle) return;
    const collapsed = settings.classList.contains('is-collapsed');
    const label = collapsed ? 'Show Settings' : 'Hide Settings';
    settingsState.textContent = label;
    settingsToggle.title = label;
  }

  function readSemanticScoreThreshold(value, fallback) {
    const threshold = Number(value);
    if (!Number.isFinite(threshold)) return fallback;
    const stepped = Math.round((Math.max(0, Math.min(1, threshold)) * 100) / 5) * 5;
    return Math.max(0, Math.min(100, stepped)) / 100;
  }

  function applySemanticScoreSuggestion(value) {
    const previous = semanticScoreThreshold;
    const fallback = semanticSuggestedScoreThreshold ?? fallbackSemanticScoreThreshold;
    const next = readSemanticScoreThreshold(value, fallback);
    semanticSuggestedScoreThreshold = next;
    if (!semanticThresholdTouched) semanticScoreThreshold = next;
    syncThresholdControl();
    if (
      semanticScoreThreshold !== previous &&
      state.mode === 'semantic' &&
      latestSemanticRows &&
      lastSemanticQuery === state.q
    ) {
      renderSemanticRows(latestSemanticRows);
    }
  }

  function applyWorkerSemanticScoreSuggestion(value) {
    if (semanticSettingsLoaded) return;
    applySemanticScoreSuggestion(value);
  }

  function syncThresholdControl() {
    const currentPercent = semanticThresholdPercent();
    const hasSuggestion = semanticSuggestedScoreThreshold !== null;
    const suggestedPercent = hasSuggestion ? Math.round(semanticSuggestedScoreThreshold * 100) : null;
    if (thresholdInput) thresholdInput.value = String(currentPercent);
    if (thresholdInput) thresholdInput.disabled = !hasSuggestion;
    if (thresholdValue) thresholdValue.textContent = hasSuggestion ? `${currentPercent}%` : '...';
    if (thresholdSuggested) thresholdSuggested.textContent = hasSuggestion ? `${suggestedPercent}%` : '...';
    if (thresholdReset) {
      thresholdReset.disabled = !hasSuggestion;
      thresholdReset.classList.toggle('is-current', hasSuggestion && currentPercent === suggestedPercent);
      if (hasSuggestion) {
        thresholdReset.setAttribute('aria-label', `Reset similarity cutoff to suggested ${suggestedPercent}%`);
        thresholdReset.title = `Reset to suggested ${suggestedPercent}%`;
      } else {
        thresholdReset.setAttribute('aria-label', 'Suggested similarity cutoff is loading');
        thresholdReset.title = '';
      }
    }
  }

  function loadSemanticSettings() {
    fetch(semanticSettingsUrl)
      .then(response => (response.ok ? response.json() : null))
      .then(settingsData => {
        if (!settingsData) {
          applySemanticScoreSuggestion(fallbackSemanticScoreThreshold);
          return;
        }
        const settingsScoreThreshold = Number(settingsData.scoreThreshold);
        if (!Number.isFinite(settingsScoreThreshold) || settingsScoreThreshold < 0 || settingsScoreThreshold > 1) {
          applySemanticScoreSuggestion(fallbackSemanticScoreThreshold);
          return;
        }
        semanticSettingsLoaded = true;
        applySemanticScoreSuggestion(settingsScoreThreshold);
      })
      .catch(() => {
        applySemanticScoreSuggestion(fallbackSemanticScoreThreshold);
      });
  }

  function semanticThresholdPercent() {
    return Math.round(semanticScoreThreshold * 100);
  }

  function renderActiveFilters() {
    const filters = filterFields
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
    if (state.paper) {
      const paper = papersById.get(state.paper);
      filters.push(
        `<button type="button" data-clear-filter="paper"><span>Paper: ${esc(paper ? paperTitle(paper) : state.paper)}</span></button>`
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

  function filterExpander(field) {
    const isOpen = state[field] ? ' open' : '';
    return (
      `<details class="unified-search-filter-expander" data-filter-expander="${escAttr(field)}"${isOpen}>` +
        '<summary>' +
          `<span>${esc(fieldConfig[field].plural)}</span>` +
          `<strong data-search-facet-count="${escAttr(field)}">0</strong>` +
        '</summary>' +
        filterControl(field) +
        `<div class="unified-search-facet-list" data-search-facet-list="${escAttr(field)}"></div>` +
      '</details>'
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
    const rawMode = params.get('mode');
    const inferredMode = rawMode || inferDefaultMode(params);
    const mode = Object.hasOwn(modeLabels, inferredMode) ? inferredMode : inferDefaultMode(params);
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

  function inferDefaultMode(params) {
    return filterFields.concat(['source_type', 'paper']).some(field => params.get(field))
      ? 'metadata'
      : defaultMode;
  }

  function syncUrl(push) {
    const nextUrl = new URL(window.location.href);
    const hasMetadataFilters = filterFields.some(field => state[field]) || Boolean(state.paper);
    nextUrl.search = '';
    if (state.mode !== defaultMode || (state.mode === 'semantic' && hasMetadataFilters)) {
      nextUrl.searchParams.set('mode', state.mode);
    }
    if (state.q) nextUrl.searchParams.set('q', state.q);
    filterFields.forEach(field => {
      if (state[field]) nextUrl.searchParams.set(field, state[field]);
    });
    if (state.paper) nextUrl.searchParams.set('paper', state.paper);
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

  function handleFacetClick(event) {
    const facetButton = event.target.closest('[data-search-facet]');
    if (!facetButton) return false;
    const field = facetButton.getAttribute('data-search-facet');
    const value = facetButton.getAttribute('data-search-value') || '';
    if (field && Object.hasOwn(fieldConfig, field)) {
      state[field] = value;
      state.paper = '';
      useMetadataModeForEmptyQuery();
      syncUrl(true);
      render();
    }
    return true;
  }

  function useMetadataModeForEmptyQuery() {
    if (state.mode === 'semantic' && !state.q && filterFields.some(field => state[field])) {
      state.mode = 'metadata';
    }
  }

  function metadataTitle() {
    if (state.paper && state.tag) {
      const ego = papersById.get(state.paper);
      const paper = ego ? paperTitle(ego) : 'Selected Paper';
      return `${state.tag} near ${paper}`;
    }
    if (state.paper) {
      const paper = papersById.get(state.paper);
      return paper ? paperTitle(paper) : 'Selected Paper';
    }
    const active = filterFields
      .filter(field => state[field])
      .map(field => `${fieldConfig[field].label}: ${state[field]}`);
    if (active.length) return active.join(' / ');
    return state.q ? 'Results' : 'All Papers';
  }

  function metadataKicker() {
    if (state.paper && state.tag) return 'Related Tag';
    if (state.paper) return 'Paper';
    if (state.tag) return 'Tag';
    if (state.author) return 'Author';
    if (state.year) return 'Year';
    if (state.source) return 'Source';
    if (state.type) return 'Type';
    return 'Metadata';
  }

  function renderError(message) {
    renderCount('!', 'error');
    panel.classList.remove('is-empty');
    resultsBody.innerHTML =
      '<div class="tag-search-selection-empty semantic-search-error">' +
        '<h2>Search Unavailable</h2>' +
        `<p>${esc(message)}</p>` +
      '</div>';
  }

  function emptyBlock(title, message) {
    return (
      '<div class="tag-search-selection-empty">' +
        (title ? `<h2>${esc(title)}</h2>` : '') +
        `<p>${esc(message)}</p>` +
      '</div>'
    );
  }

  function renderProgress(message) {
    if (!workerLoading || state.mode !== 'semantic' || !state.q) return;
    if (latestSemanticRows && lastSemanticQuery === state.q) return;
    panel.classList.remove('is-empty');
    resultsBody.innerHTML =
      '<div class="tag-search-selection-empty semantic-search-progress" role="status" aria-live="polite">' +
        '<h2>Searching</h2>' +
        `<p>${esc(message || 'Working...')}</p>` +
      '</div>';
  }

  function comparePapers(a, b) {
    const rankDelta = metadataSearchRank(b) - metadataSearchRank(a);
    return rankDelta || paperYear(b) - paperYear(a) || paperTitle(a).localeCompare(paperTitle(b));
  }

  function metadataSearchRank(paper) {
    const query = normalizeText(state.q);
    const queryTokens = searchTokens(query);
    if (!queryTokens.length) return 0;

    const algorithm = clean(paper.algorithm || '');
    const title = paperTitle(paper);
    const tags = Array.isArray(paper.tags) ? paper.tags.join(' ') : '';

    return (
      (fieldAlgorithmExactMatch(algorithm, query) ? 6000 : 0) +
      (fieldDecoratedAlgorithmMatch(algorithm, query) ? 700 : 0) +
      (fieldExactMatch(title, query) ? 5000 : 0) +
      fieldSearchRank(algorithm, query, queryTokens, 1000, fieldAlgorithmExactMatch) +
      fieldSearchRank(title, query, queryTokens, 100) +
      fieldSearchRank(tags, query, queryTokens, 40)
    );
  }

  function fieldSearchRank(value, query, queryTokens, weight, isExactMatch = fieldExactMatch) {
    const text = normalizeText(value);
    const textTokens = searchTokens(text);
    if (!textTokens.length) return 0;
    if (isExactMatch(text, query)) return weight * 4;
    if (containsTokenSequence(textTokens, queryTokens)) return weight * 3;
    if (queryTokens.every(token => textTokens.includes(token))) return weight * 2;
    if (queryTokens.some(token => textTokens.includes(token))) return weight;
    return 0;
  }

  function fieldAlgorithmExactMatch(value, query) {
    const text = normalizeText(value);
    if (fieldStrictExactMatch(text, query)) return true;
    if (!text || searchKey(text) !== searchKey(query)) return false;
    return searchTokens(text).length > searchTokens(query).length;
  }

  function fieldDecoratedAlgorithmMatch(value, query) {
    const text = normalizeText(value);
    return Boolean(text) &&
      !fieldAlgorithmExactMatch(text, query) &&
      text.startsWith(query) &&
      searchKey(text) === searchKey(query);
  }

  function fieldExactMatch(value, query) {
    const text = normalizeText(value);
    return Boolean(text) && (fieldStrictExactMatch(text, query) || searchKey(text) === searchKey(query));
  }

  function fieldStrictExactMatch(value, query) {
    return normalizeText(value) === query;
  }

  function containsTokenSequence(tokens, sequence) {
    if (!sequence.length || sequence.length > tokens.length) return false;
    return tokens.some((_, index) => sequence.every((token, offset) => tokens[index + offset] === token));
  }

  function searchTokens(value) {
    return normalizeText(value).split(/[^a-z0-9]+/).filter(Boolean);
  }

  function searchKey(value) {
    return searchTokens(value).join('');
  }

  function metadataSearchText(value) {
    return ` ${searchTokens(value).join(' ')} `;
  }

  function metadataQueryTokens(value) {
    const tokens = searchTokens(value);
    const filtered = tokens.filter(token => !metadataConnectorWords.has(token));
    return filtered.length ? filtered : tokens;
  }

  function highlightSearchMatches(value) {
    const text = clean(value);
    const pattern = searchHighlightPattern();
    if (!text || !pattern) return esc(text);

    const ranges = [];
    for (const match of text.matchAll(pattern)) {
      const prefix = match[1] || '';
      const exact = match[2] || '';
      if (!exact) continue;
      ranges.push({
        start: match.index + prefix.length,
        end: match.index + prefix.length + exact.length,
      });
    }
    if (!ranges.length) return esc(text);

    ranges.sort((a, b) => a.start - b.start || b.end - a.end);
    const merged = [];
    ranges.forEach(range => {
      const previous = merged[merged.length - 1];
      if (previous && range.start <= previous.end) {
        previous.end = Math.max(previous.end, range.end);
      } else {
        merged.push(range);
      }
    });

    let cursor = 0;
    const parts = [];
    merged.forEach(range => {
      parts.push(esc(text.slice(cursor, range.start)));
      parts.push(`<mark class="unified-search-match">${esc(text.slice(range.start, range.end))}</mark>`);
      cursor = range.end;
    });
    parts.push(esc(text.slice(cursor)));
    return parts.join('');
  }

  function searchHighlightPattern() {
    const tokens = searchTokens(state.q);
    if (!tokens.length) return null;
    const alternatives = [];
    alternatives.push(tokens.map(escapeRegExp).join('[^A-Za-z0-9]+'));
    if (tokens.length > 1) {
      tokens.forEach(token => alternatives.push(escapeRegExp(token)));
    }
    return new RegExp(`(^|[^A-Za-z0-9])(${alternatives.join('|')})(?=$|[^A-Za-z0-9])`, 'gi');
  }

  function escapeRegExp(value) {
    return String(value).replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
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
