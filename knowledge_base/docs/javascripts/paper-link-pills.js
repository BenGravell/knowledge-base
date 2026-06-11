(function () {
  const ICONS = {
    external: '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M14 3v2h3.59l-9.83 9.83 1.41 1.41L19 6.41V10h2V3m-2 16H5V5h7V3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7h-2z"></path></svg>',
    internal: '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M8.59 16.58 13.17 12 8.59 7.41 10 6l6 6-6 6z"></path></svg>',
  };

  function linkUrl(link) {
    const href = link.getAttribute('href');
    if (!href || href.startsWith('#')) return null;
    try {
      return new URL(href, window.location.href);
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

  function iconMarkup(kind, className) {
    return '<span class="' + className + '" aria-hidden="true">' + ICONS[kind] + '</span>';
  }

  function hydratePill(link) {
    if (link.querySelector('.paper-link-pill__icon')) return;
    const kind = isOutsideKnowledgeBase(link) ? 'external' : 'internal';
    link.insertAdjacentHTML(
      'beforeend',
      iconMarkup(kind, 'paper-link-pill__icon paper-link-pill__icon--' + kind)
    );
  }

  function hydrateNavExternal(link) {
    if (!isOutsideKnowledgeBase(link) || link.querySelector('.kb-nav-external-icon')) return;
    link.insertAdjacentHTML(
      'beforeend',
      iconMarkup('external', 'kb-nav-external-icon')
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
    const observer = new MutationObserver(function (mutations) {
      mutations.forEach(function (mutation) {
        mutation.addedNodes.forEach(hydrate);
      });
    });
    observer.observe(document.body, { childList: true, subtree: true });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }
})();
