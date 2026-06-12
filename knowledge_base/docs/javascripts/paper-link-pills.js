(function () {
  if (window.kbSiteLinks && typeof window.kbSiteLinks.hydrate === 'function') {
    if (document.body) window.kbSiteLinks.hydrate(document.body);
    return;
  }

  const data = window.kbSiteLinkData || {};
  const linkSpecs = Array.isArray(data.links) ? data.links : [];
  const fallbackIcons = data.fallbackIcons || {};
  const externalIconSvg = fallbackIcons.external || '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3m-2 16H5V5h7V3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7h-2z"></path></svg>';
  const internalIconSvg = fallbackIcons.internal || '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M8.59 16.58 13.17 12 8.59 7.41 10 6l6 6-6 6z"></path></svg>';
  const specsByKey = new Map();
  const specsByLabel = new Map();
  let observerStarted = false;

  linkSpecs.forEach(function (spec) {
    const key = normalizeKey(spec.key);
    if (!key) return;
    specsByKey.set(key, spec);
    specsByLabel.set(normalizeLabel(spec.label), spec);
  });

  function normalizeKey(value) {
    return String(value || '').trim().toLowerCase();
  }

  function normalizeLabel(value) {
    return String(value || '').trim().toLowerCase();
  }

  function escapeHtml(value) {
    return String(value == null ? '' : value)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function escapeAttr(value) {
    return escapeHtml(value).replace(/`/g, '&#96;');
  }

  function linkUrl(link) {
    const href = link.getAttribute('href');
    if (!href || href.startsWith('#')) return null;
    try {
      return new URL(href, window.location.href);
    } catch (_) {
      return null;
    }
  }

  function urlFromString(url) {
    if (!url || String(url).startsWith('#')) return null;
    try {
      return new URL(String(url), window.location.href);
    } catch (_) {
      return null;
    }
  }

  function isOutsideKnowledgeBase(link) {
    if (link.target === '_blank') return true;
    const url = linkUrl(link);
    if (!url || url.protocol === 'mailto:' || url.protocol === 'tel:') return false;
    if (url.origin !== window.location.origin) return true;
    return window.location.pathname.startsWith('/knowledge-base/') &&
      !url.pathname.startsWith('/knowledge-base/');
  }

  function isExternalUrl(url, explicitExternal) {
    if (explicitExternal) return true;
    const parsed = urlFromString(url);
    if (!parsed || parsed.protocol === 'mailto:' || parsed.protocol === 'tel:') return false;
    if (parsed.origin !== window.location.origin) return true;
    return window.location.pathname.startsWith('/knowledge-base/') &&
      !parsed.pathname.startsWith('/knowledge-base/');
  }

  function keyFromPath(pathname) {
    const cleanPath = String(pathname || '').replace(/\/+$/, '');
    const parts = cleanPath.split('/').filter(Boolean);
    const last = parts[parts.length - 1] || '';
    const beforeLast = parts[parts.length - 2] || '';

    if (last === 'map') return 'map';
    if (last === 'tree' || beforeLast === 'tree') return 'tree';
    if (last === 'timeline') return 'timeline';
    if (last === 'search') return 'search';
    if (beforeLast === 'papers' || parts.includes('papers')) return 'detail';
    return '';
  }

  function specFor(options) {
    const key = normalizeKey(options && options.key);
    if (key && specsByKey.has(key)) return specsByKey.get(key);

    const label = normalizeLabel(options && options.label);
    if (label && specsByLabel.has(label)) return specsByLabel.get(label);

    const parsed = urlFromString(options && options.url);
    const urlKey = parsed ? keyFromPath(parsed.pathname) : '';
    return urlKey ? specsByKey.get(urlKey) : null;
  }

  function renderIcon(svg, kind) {
    if (!svg) return '';
    return '<span class="paper-link-pill__icon paper-link-pill__icon--' + escapeAttr(kind) + '" aria-hidden="true">' + svg + '</span>';
  }

  function renderAttrs(attrs) {
    return Object.keys(attrs || {}).map(function (name) {
      const value = attrs[name];
      if (value === false || value == null) return '';
      if (value === true) return ' ' + escapeAttr(name);
      return ' ' + escapeAttr(name) + '="' + escapeAttr(value) + '"';
    }).join('');
  }

  function renderPill(options) {
    const opts = options || {};
    const url = String(opts.url || '').trim();
    if (!url) return '';

    const external = isExternalUrl(url, opts.external);
    const spec = external ? null : specFor(opts);
    const label = String(opts.label || (spec && spec.label) || '').trim();
    if (!label) return '';

    const variant = String(opts.variant || (external ? 'primary' : 'internal')).trim() || 'internal';
    const iconSvg = external ? externalIconSvg : (spec && spec.iconSvg) || internalIconSvg;
    const iconKind = external ? 'external' : 'internal';
    const detail = String(opts.detail || '').trim();
    const attrs = Object.assign({}, opts.attrs || {});
    if (spec && spec.key) attrs['data-kb-site-link'] = spec.key;
    if (detail) {
      attrs['aria-label'] = detail;
      attrs.title = detail;
    }

    return '<a class="paper-link-pill paper-link-pill--' + escapeAttr(variant) + '" href="' + escapeAttr(url) + '"' +
      (external ? ' target="_blank" rel="noopener noreferrer"' : '') +
      renderAttrs(attrs) + '>' +
      '<span class="paper-link-pill__label">' + escapeHtml(label) + '</span>' +
      renderIcon(iconSvg, iconKind) +
      '</a>';
  }

  function paperUrl(paper, key) {
    const source = paper || {};
    if (key === 'detail') return source.url || source.detailUrl || '';
    if (key === 'map') return source.mapUrl || source.map_url || '';
    if (key === 'tree') return source.treeUrl || source.tree_url || '';
    if (key === 'timeline') return source.timelineUrl || source.timeline_url || '';
    if (key === 'search') return source.searchUrl || source.search_url || '';
    return '';
  }

  function includeKey(options, key) {
    const opts = options || {};
    const prop = 'include' + key.charAt(0).toUpperCase() + key.slice(1);
    return opts[prop] !== false;
  }

  function renderPaperSiteLinks(paper, options) {
    return linkSpecs.map(function (spec) {
      const key = normalizeKey(spec.key);
      if (!key || !includeKey(options, key)) return '';
      const url = paperUrl(paper, key);
      return renderPill({
        key: key,
        label: spec.label,
        url: url,
        detail: 'Open in ' + spec.label,
        variant: 'internal',
        external: false,
      });
    }).join('');
  }

  function hydratePill(link) {
    if (link.querySelector('.paper-link-pill__icon')) return;
    const labelNode = link.querySelector('.paper-link-pill__label');
    const label = labelNode ? labelNode.textContent : link.textContent;
    const href = link.getAttribute('href') || '';
    const external = isOutsideKnowledgeBase(link);
    const spec = external ? null : specFor({
      key: link.getAttribute('data-kb-site-link') || '',
      label: label,
      url: href,
    });
    if (spec && spec.key) {
      link.setAttribute('data-kb-site-link', spec.key);
    }
    const iconSvg = external ? externalIconSvg : (spec && spec.iconSvg) || internalIconSvg;
    link.insertAdjacentHTML('beforeend', renderIcon(iconSvg, external ? 'external' : 'internal'));
  }

  function hydrateNavExternal(link) {
    if (!isOutsideKnowledgeBase(link) || link.querySelector('.kb-nav-external-icon')) return;
    link.insertAdjacentHTML(
      'beforeend',
      '<span class="kb-nav-external-icon" aria-hidden="true">' + externalIconSvg + '</span>'
    );
  }

  function hydrate(root) {
    if (!root || root.nodeType !== 1) return;
    if (root.matches && root.matches('.paper-link-pill')) hydratePill(root);
    if (root.matches && root.matches('a.md-nav__link')) hydrateNavExternal(root);
    root.querySelectorAll?.('.paper-link-pill').forEach(hydratePill);
    root.querySelectorAll?.('a.md-nav__link').forEach(hydrateNavExternal);
  }

  function start() {
    hydrate(document.body);
    if (observerStarted) return;
    observerStarted = true;
    const observer = new MutationObserver(function (mutations) {
      mutations.forEach(function (mutation) {
        mutation.addedNodes.forEach(hydrate);
      });
    });
    observer.observe(document.body, { childList: true, subtree: true });
  }

  window.kbSiteLinks = {
    renderPill: renderPill,
    renderPaperSiteLinks: renderPaperSiteLinks,
    hydrate: hydrate,
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }
})();
