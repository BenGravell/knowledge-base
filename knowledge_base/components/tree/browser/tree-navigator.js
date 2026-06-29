'use strict';

(function () {
  if (window.kbTreeNavigator) return;

  function esc(value) {
    return String(value == null ? '' : value)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function attr(name, value) {
    if (value == null || value === false) return '';
    return ' ' + name + '="' + esc(value === true ? 'true' : value) + '"';
  }

  function plural(count, singular, pluralLabel) {
    return String(count) + ' ' + (count === 1 ? singular : (pluralLabel || singular + 's'));
  }

  function renderStack(config) {
    const options = Array.isArray(config) ? {} : (config || {});
    const sections = Array.isArray(config) ? config : (options.sections || []);
    const density = options.density === 'compact' ? 'compact' : 'full';
    const className = [
      'ct-focus-stack',
      'ct-tree-navigator',
      'ct-tree-navigator--' + density,
      options.className,
    ].filter(Boolean).join(' ');
    return '<div class="' + esc(className) + '">' + sections.map(renderSection).join('') + '</div>';
  }

  function renderSection(section) {
    const rows = Array.isArray(section.rows) ? section.rows : [];
    const kind = section.kind || 'children';
    const title = section.title || '';
    const label = title ? attr('aria-label', title) : '';
    const empty = section.empty || 'No children.';
    return [
      '<section class="ct-focus-section ct-focus-section--' + esc(kind) + '"' + label + '>',
      rows.length
        ? '<ul class="ct-tree-list' + (rows.length === 1 ? ' is-single-child' : '') + '">' +
          rows.map(function (row, index) {
            return renderNode(row, kind, index, rows.length);
          }).join('') +
          '</ul>'
        : '<p class="ct-empty">' + esc(empty) + '</p>',
      '</section>',
    ].join('');
  }

  function renderNode(row, sectionKind, index, total) {
    const id = row.id == null ? '' : String(row.id);
    const kind = row.kind || 'branch';
    const counters = renderCounters(row.counters);
    const classes = [
      'ct-tree-node',
      'ct-tree-kind-' + kind,
      'ct-tree-section-' + sectionKind,
      row.current ? 'is-current' : '',
      row.ancestor ? 'is-ancestor' : '',
      row.parent ? 'is-parent' : '',
      row.successor ? 'is-successor' : '',
      index === 0 ? 'is-first' : '',
      index === total - 1 ? 'is-last' : '',
      row.className || '',
    ].filter(Boolean).join(' ');
    const buttonClasses = ['ct-tree-button', counters ? 'has-counters' : '', row.buttonClassName || '']
      .filter(Boolean)
      .join(' ');
    const style = row.color ? ' style="--ct-tree-node-color: ' + esc(row.color) + ';"' : '';
    const previewId = row.previewId === false ? null : (row.previewId || id);
    const meta = row.meta ? '<span class="ct-tree-meta">' + esc(row.meta) + '</span>' : '';
    const details = row.detailsHtml || '';

    return [
      '<li class="' + esc(classes) + '"' + style + '>',
      '<button type="button" class="' + esc(buttonClasses) + '"' +
        attr('data-ct-select', id) +
        attr('data-ct-preview-node', previewId) +
        attr('data-ct-has-children', row.hasChildren || null) +
        attr('aria-current', row.current || null) +
        attr('aria-label', row.ariaLabel || null) +
        '>',
      '<span class="ct-tree-rail" aria-hidden="true"><span class="ct-tree-dot"></span></span>',
      '<span class="ct-tree-copy">',
      '<span class="ct-tree-label">' + esc(row.label || '') + '</span>',
      meta,
      '</span>',
      counters,
      '</button>',
      details,
      '</li>',
    ].join('');
  }

  function renderCounters(counters) {
    if (!Array.isArray(counters) || !counters.length) return '';
    return '<span class="ct-tree-counts">' + counters.map(renderCountChip).join('') + '</span>';
  }

  function renderCountChip(counter) {
    const kind = counter.kind || 'children';
    const count = Number.isFinite(Number(counter.count)) ? Number(counter.count) : 0;
    const label = counter.label || plural(count, counter.singular || kind, counter.plural);
    return [
      '<span class="ct-tree-count ct-tree-count--' + esc(kind) + '" title="' + esc(label) + '" aria-label="' + esc(label) + '">',
      treeCountIcon(kind),
      '<span class="ct-tree-count-value">' + esc(count) + '</span>',
      '</span>',
    ].join('');
  }

  function treeCountIcon(kind) {
    const paths = {
      descendants: 'M11 3h2v4h5v5h-2V9h-3v6h5v6h-6v-6h-3v3H6v3H0v-6h6v1h1V9H4v3H2V7h9V3zm3 14v2h2v-2h-2zM2 17v2h2v-2H2z',
      children: 'M5 4h14v4H5V4zm6 4h2v3h5v3h-2v-1H8v1H6v-3h5V8zM4 16h6v4H4v-4zm10 0h6v4h-6v-4z',
    };
    const path = paths[kind] || paths.children;
    return [
      '<svg class="ct-tree-count-icon" viewBox="0 0 24 24" aria-hidden="true" focusable="false">',
      '<path d="' + esc(path) + '"></path>',
      '</svg>',
    ].join('');
  }

  window.kbTreeNavigator = {
    renderStack,
    renderSection,
    renderNode,
  };
})();
