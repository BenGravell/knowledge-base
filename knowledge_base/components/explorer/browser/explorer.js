'use strict';

(function () {
  const app = document.getElementById('kb-explorer');
  if (!app) return;
  const mapView = window.kbMapView;
  const treeView = window.kbTreeView;
  const map = document.getElementById('mm-app');
  const tree = document.getElementById('ct-sunburst-panel');
  const controls = document.querySelector('.mm-header-controls');
  const branch = document.getElementById('mm-branch-panel');
  const toggle = document.getElementById('mm-panel-hide-btn');
  const buttons = [...app.querySelectorAll('[data-explorer-mode]')];

  function showMode() {
    const mode = new URLSearchParams(location.search).get('mode') === 'tree' ? 'tree' : 'map';
    app.dataset.mode = mode;
    [[map, mode !== 'map'], [tree, mode !== 'tree'], [controls, mode !== 'map']].forEach(([el, hidden]) => {
      el.inert = hidden;
      el.setAttribute('aria-hidden', String(hidden));
    });
    buttons.forEach(button => {
      const active = button.dataset.explorerMode === mode;
      button.classList.toggle('is-active', active);
      button.setAttribute('aria-pressed', String(active));
    });
    if (mode === 'map') mapView?.resize();
  }

  function writeSelection(selection, method) {
    const url = new URL(location.href);
    ['ct', 'paper'].forEach(key => url.searchParams.delete(key));
    url.hash = selection.paperId
      ? 'paper=' + encodeURIComponent(selection.paperId)
      : 'ct=' + encodeURIComponent(selection.id);
    if (url.href !== location.href) history[method](null, '', url);
  }

  function restoreSelection(initial = false) {
    showMode();
    if (!treeView) return;
    const previousId = treeView.selection().id;
    const params = new URLSearchParams(location.hash.slice(1) || location.search);
    const nodeId = params.get('ct');
    const paperId = params.get('paper');
    const selected = nodeId
      ? treeView.selectNode(nodeId, { notify: false })
      : paperId && treeView.selectPaper(paperId, { notify: false });
    if (!selected) treeView.selectNode(treeView.rootId, { notify: false });
    if (initial || treeView.selection().id !== previousId) mapView?.select(treeView.selection());
  }

  window.addEventListener('kb-tree-select', event => {
    mapView?.select(event.detail);
    writeSelection(event.detail, 'pushState');
  });
  window.addEventListener('kb-map-select', event => {
    if (!treeView) return;
    const previous = treeView.selection();
    if (event.detail.paperId) treeView.selectPaper(event.detail.paperId, { notify: false });
    else treeView.selectPath(event.detail.path, { notify: false });
    writeSelection(treeView.selection(), event.detail.paperId || previous.paperId ? 'replaceState' : 'pushState');
  });

  buttons.forEach(button => button.addEventListener('click', () => {
    if (button.dataset.explorerMode === app.dataset.mode) return;
    const url = new URL(location.href);
    url.searchParams.set('mode', button.dataset.explorerMode);
    history.pushState(null, '', url);
    showMode();
  }));

  toggle.addEventListener('click', () => {
    const collapsed = branch.classList.toggle('body-collapsed');
    branch.inert = collapsed;
    app.classList.toggle('is-branch-open', !collapsed);
    toggle.title = collapsed ? 'Show Branch Selector' : 'Hide Branch Selector';
    toggle.setAttribute('aria-label', toggle.title);
    toggle.setAttribute('aria-expanded', String(!collapsed));
  });

  function sizeWorkspace() {
    const header = document.querySelector('.md-header');
    const footer = document.querySelector('.md-footer');
    document.documentElement.style.setProperty('--mm-header-h', (header?.getBoundingClientRect().height || 56) + 'px');
    document.documentElement.style.setProperty('--mm-footer-h', (footer?.getBoundingClientRect().height || 0) + 'px');
  }
  sizeWorkspace();
  const chromeSizes = new ResizeObserver(sizeWorkspace);
  document.querySelectorAll('.md-header, .md-footer').forEach(el => chromeSizes.observe(el));
  window.addEventListener('resize', sizeWorkspace);

  // Hidden views keep their dimensions; changing modes never rebuilds either view.
  new ResizeObserver(() => {
    if (app.dataset.mode === 'map') mapView?.resize(true);
  }).observe(document.getElementById('kb-explorer-main'));
  window.addEventListener('popstate', () => restoreSelection());
  window.addEventListener('hashchange', () => restoreSelection());
  restoreSelection(true);
})();
