(function () {
  'use strict';

  const app = document.getElementById('tag-search-app');
  const data = window.tagSearchData;
  if (!app) return;

  if (!data || !data.papers || !data.related) {
    app.innerHTML = '<p class="tag-search-empty">Related-paper data is unavailable. Run <code>mkdocs build</code> to regenerate it.</p>';
    return;
  }

  const params = new URLSearchParams(window.location.search);
  const egoId = params.get('paper') || '';
  const rawTag = params.get('tag') || '';
  const tagKey = normalizeTag(rawTag);
  const ego = data.papers[egoId];

  if (!ego || !tagKey) {
    app.innerHTML =
      '<p class="tag-search-empty">Open this page by clicking a tag on a paper detail page.</p>';
    return;
  }

  const results = (data.related[`${egoId}::${tagKey}`] || [])
    .map(item => ({ item, paper: data.papers[item.id] }))
    .filter(row => row.paper);

  const tagLabel = data.tags && data.tags[tagKey] ? data.tags[tagKey] : rawTag;
  const resultLabel = results.length === 1 ? 'paper' : 'papers';

  app.innerHTML =
    '<section class="tag-search-hero">' +
      '<div>' +
        '<span class="tag-search-kicker">Tag</span>' +
        `<h1>${esc(tagLabel)}</h1>` +
        `<p>Most similar papers to <a href="${escAttr(ego.url)}">${esc(paperTitle(ego))}</a> that share this tag.</p>` +
      '</div>' +
      `<div class="tag-search-count"><strong>${results.length}</strong><span>${resultLabel}</span></div>` +
    '</section>' +
    (results.length
      ? `<div class="tag-search-results">${results.map(renderResult).join('')}</div>`
      : '<p class="tag-search-empty">No other papers currently share this tag.</p>');

  function renderResult(row, index) {
    const paper = row.paper;
    const score = Number.isFinite(row.item.score)
      ? `<span>${Math.round(row.item.score * 100)}% similar</span>`
      : '';
    const tags = (paper.tags || [])
      .slice(0, 8)
      .map(tag => `<span>${esc(tag)}</span>`)
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
    return `<a class="paper-link-pill paper-link-pill--internal" href="${escAttr(url)}"><span class="paper-link-pill__label">${esc(label)}</span></a>`;
  }

  function paperTitle(paper) {
    return paper.title || paper.label || paper.id || 'Untitled paper';
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
