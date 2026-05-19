(function () {
  'use strict';

  const app = document.getElementById('tag-search-app');
  const data = window.tagSearchData;
  if (!app) return;

  if (!data || !data.papers) {
    app.innerHTML = '<p class="tag-search-empty">Related-paper data is unavailable. Run <code>mkdocs build</code> to regenerate it.</p>';
    return;
  }

  const papers = Object.values(data.papers);
  const tagIndex = buildTagIndex(papers);
  const tagOrder = Array.from(tagIndex.values()).sort((a, b) =>
    b.papers.length - a.papers.length || a.label.localeCompare(b.label)
  );
  const params = new URLSearchParams(window.location.search);
  const egoId = params.get('paper') || '';
  const rawTag = params.get('tag') || '';
  const tagKey = normalizeTag(rawTag);
  const ego = data.papers[egoId];

  if (ego && tagKey) {
    renderRelatedSearch(ego, tagKey, rawTag);
    return;
  }

  renderTagBrowser(tagKey, rawTag);

  function renderRelatedSearch(ego, tagKey, rawTag) {
    const results = ((data.related && data.related[`${ego.id}::${tagKey}`]) || [])
      .map(item => ({ item, paper: data.papers[item.id] }))
      .filter(row => row.paper);
    const tag = tagIndex.get(tagKey);
    const tagLabel = tag ? tag.label : tagLabelFor(tagKey, rawTag);
    const resultLabel = results.length === 1 ? 'paper' : 'papers';

    app.innerHTML =
      '<section class="tag-search-hero">' +
        '<div>' +
          '<span class="tag-search-kicker">Tag</span>' +
          `<h1>${esc(tagLabel)}</h1>` +
          `<p>Most similar papers to <a href="${escAttr(ego.url)}">${esc(paperTitle(ego))}</a> that share this tag.</p>` +
          `<p class="tag-search-hero-link"><a href="?tag=${encodeURIComponent(tagLabel)}">View all papers with this tag</a></p>` +
        '</div>' +
        `<div class="tag-search-count"><strong>${results.length}</strong><span>${resultLabel}</span></div>` +
      '</section>' +
      (results.length
        ? `<div class="tag-search-results">${results.map(renderResult).join('')}</div>`
        : '<p class="tag-search-empty">No other papers currently share this tag.</p>');
  }

  function renderTagBrowser(initialTagKey, rawTag) {
    const requestedTag = Boolean(initialTagKey);
    const initialMatch = tagIndex.get(initialTagKey);
    const initialSelection = initialMatch
      ? initialMatch.key
      : (!requestedTag && tagOrder[0] ? tagOrder[0].key : '');
    const initialQuery = initialMatch ? initialMatch.label : rawTag;

    app.innerHTML =
      '<section class="tag-search-browser">' +
        '<aside class="tag-search-panel">' +
          '<form class="tag-search-form" role="search">' +
            '<label for="tag-search-input">Search Tags</label>' +
            '<div class="tag-search-input-row">' +
              `<input id="tag-search-input" type="search" autocomplete="off" list="tag-search-options" value="${escAttr(initialQuery)}">` +
              '<button type="submit">Search</button>' +
            '</div>' +
            '<datalist id="tag-search-options">' +
              tagOrder.map(tag => `<option value="${escAttr(tag.label)}"></option>`).join('') +
            '</datalist>' +
          '</form>' +
          '<div class="tag-search-panel-head">' +
            '<span>Tags</span>' +
            '<strong id="tag-search-visible-count"></strong>' +
          '</div>' +
          '<div id="tag-search-tag-list" class="tag-search-tag-list"></div>' +
        '</aside>' +
        '<section id="tag-search-selection" class="tag-search-selection"></section>' +
      '</section>';

    const form = app.querySelector('.tag-search-form');
    const input = app.querySelector('#tag-search-input');
    const tagList = app.querySelector('#tag-search-tag-list');
    const visibleCount = app.querySelector('#tag-search-visible-count');
    const selection = app.querySelector('#tag-search-selection');
    let selectedTagKey = initialSelection;
    let visibleTags = [];

    form.addEventListener('submit', event => {
      event.preventDefault();
      const query = input.value.trim();
      const exact = tagIndex.get(normalizeTag(query));
      const next = exact || visibleTags[0];
      if (next) {
        selectTag(next.key, true);
      } else {
        selectedTagKey = '';
        renderSelection(null, query);
        syncTagButtons();
      }
    });

    input.addEventListener('input', () => renderTagList(input.value));

    tagList.addEventListener('click', event => {
      const button = event.target.closest('button[data-tag-key]');
      if (!button) return;
      selectTag(button.getAttribute('data-tag-key'), true);
    });

    window.addEventListener('popstate', () => {
      const currentParams = new URLSearchParams(window.location.search);
      const currentRawTag = currentParams.get('tag') || '';
      const currentTag = tagIndex.get(normalizeTag(currentRawTag));
      selectedTagKey = currentTag ? currentTag.key : '';
      input.value = currentTag ? currentTag.label : currentRawTag;
      renderTagList(input.value);
      renderSelection(currentTag, currentRawTag);
    });

    renderTagList(input.value);
    renderSelection(tagIndex.get(selectedTagKey), initialQuery);
    syncTagButtons();

    function renderTagList(query) {
      const terms = normalizeTag(query).split(' ').filter(Boolean);
      visibleTags = tagOrder.filter(tag =>
        terms.every(term => tag.searchText.includes(term))
      );
      const visible = visibleTags.slice(0, 96);
      tagList.innerHTML = visible.length
        ? visible.map(tag => (
          `<button type="button" data-tag-key="${escAttr(tag.key)}" class="tag-search-tag-option">` +
            `<span>${esc(tag.label)}</span>` +
            `<strong>${tag.papers.length}</strong>` +
          '</button>'
        )).join('')
        : '<p class="tag-search-empty">No matching tags.</p>';
      visibleCount.textContent = visibleTags.length === visible.length
        ? String(visible.length)
        : `${visible.length} / ${visibleTags.length}`;
      syncTagButtons();
    }

    function selectTag(tagKey, updateUrl) {
      const tag = tagIndex.get(tagKey);
      if (!tag) return;
      selectedTagKey = tag.key;
      input.value = '';
      renderSelection(tag, '');
      renderTagList('');
      if (updateUrl) {
        const nextUrl = new URL(window.location.href);
        nextUrl.search = '';
        nextUrl.searchParams.set('tag', tag.label);
        window.history.pushState({}, '', nextUrl);
      }
    }

    function renderSelection(tag, fallbackQuery) {
      if (!tag) {
        selection.innerHTML = (
          '<div class="tag-search-selection-empty">' +
            '<h2>No Tag Selected</h2>' +
            (fallbackQuery ? `<p>No tag matches "${esc(fallbackQuery)}".</p>` : '<p>Select a tag to show matching papers.</p>') +
          '</div>'
        );
        return;
      }

      const resultLabel = tag.papers.length === 1 ? 'paper' : 'papers';
      selection.innerHTML =
        '<section class="tag-search-selected-head">' +
          '<div>' +
            '<span class="tag-search-kicker">Selected Tag</span>' +
            `<h2>${esc(tag.label)}</h2>` +
          '</div>' +
          `<div class="tag-search-count"><strong>${tag.papers.length}</strong><span>${resultLabel}</span></div>` +
        '</section>' +
        `<div class="tag-search-results">${tag.papers.map((paper, index) => renderResult({ paper, item: {} }, index)).join('')}</div>`;
    }

    function syncTagButtons() {
      tagList.querySelectorAll('button[data-tag-key]').forEach(button => {
        button.classList.toggle('tag-search-tag-option--active', button.getAttribute('data-tag-key') === selectedTagKey);
      });
    }
  }

  function renderResult(row, index) {
    const paper = row.paper;
    const score = Number.isFinite(row.item.score)
      ? `<span>${Math.round(row.item.score * 100)}% similar</span>`
      : '';
    const tags = (paper.tags || [])
      .slice(0, 8)
      .map(tag => `<a href="?tag=${encodeURIComponent(tag)}">${esc(tag)}</a>`)
      .join('');
    return (
      '<article class="tag-search-card">' +
        '<div class="tag-search-rank">' + String(index + 1) + '</div>' +
        '<div class="tag-search-card-main">' +
          '<div class="tag-search-meta">' +
            `<span>${esc(paper.year || 'Undated')}</span>` +
            score +
          '</div>' +
          `<h2><a href="${escAttr(paper.url)}">${esc(paperTitle(paper))}</a></h2>` +
          (paper.label && paper.label !== paper.title ? `<p class="tag-search-label">${esc(paper.label)}</p>` : '') +
          (paper.summary ? `<p class="tag-search-summary">${esc(paper.summary)}</p>` : '') +
          (tags ? `<div class="tag-search-tags">${tags}</div>` : '') +
          '<div class="paper-link-pills tag-search-actions">' +
            actionLink(paper.url, 'Open Detail Page') +
            actionLink(paper.mindMapUrl, 'Open in Mind Map') +
            actionLink(paper.contentTreeUrl, 'Open in Content Tree') +
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

  function buildTagIndex(papers) {
    const index = new Map();
    papers.forEach(paper => {
      const seen = new Set();
      (paper.tags || []).forEach(tagValue => {
        const label = String(tagValue || '').trim();
        const key = normalizeTag(label);
        if (!key || seen.has(key)) return;
        seen.add(key);
        if (!index.has(key)) {
          index.set(key, {
            key,
            label: tagLabelFor(key, label),
            papers: [],
            searchText: '',
          });
        }
        index.get(key).papers.push(paper);
      });
    });
    index.forEach(tag => {
      tag.papers.sort(comparePapers);
      tag.searchText = normalizeTag(tag.label);
    });
    return index;
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

  function tagLabelFor(tagKey, fallback) {
    return (data.tags && data.tags[tagKey]) || fallback || tagKey;
  }

  function normalizeTag(tag) {
    return String(tag || '').trim().replace(/\s+/g, ' ').toLowerCase();
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
