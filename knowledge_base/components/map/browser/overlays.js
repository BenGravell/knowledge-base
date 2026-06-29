/* browser/overlays.js - tooltip and paper modal overlays for the map. */

'use strict';

(function () {
  function createMapOverlays(deps = {}) {
    const graphContainer = deps.graphContainer;
    const viewState = deps.viewState;
    const tooltip = document.getElementById('mm-tooltip');
    const hoverTooltip = document.getElementById('mm-hover-tooltip');
    const modal = document.getElementById('mm-modal');
    const modalTitle = document.getElementById('mm-modal-title');
    const modalBody = document.getElementById('mm-modal-body');
    const modalClose = document.getElementById('mm-modal-close');

    function graph() {
      return typeof deps.getGraph === 'function' ? deps.getGraph() : null;
    }

    function renderer() {
      return typeof deps.getRenderer === 'function' ? deps.getRenderer() : null;
    }

    function graphHasNode(node) {
      return typeof deps.graphHasNode === 'function' && deps.graphHasNode(node);
    }

    function nodeVisible(node) {
      return typeof deps.nodeVisible === 'function' && deps.nodeVisible(node);
    }

    function mobileViewport() {
      return typeof deps.mobileViewport === 'function' && deps.mobileViewport();
    }

    function escHtml(value) {
      return typeof deps.escHtml === 'function'
        ? deps.escHtml(value)
        : String(value || '');
    }

    function formatAuthors(authors) {
      const names = Array.isArray(authors) ? authors.filter(Boolean) : [];
      if (!names.length) return 'Unknown';
      return names.length > 1 ? `${names[0]} et al.` : names[0];
    }

    function nodeTooltipPosition(node) {
      const r = renderer();
      const g = graph();
      if (!r || !g || !graphHasNode(node)) return null;

      const attrs = g.getNodeAttributes(node);
      const display = typeof r.getNodeDisplayData === 'function'
        ? r.getNodeDisplayData(node)
        : null;
      const point = r.graphToViewport({ x: attrs.x, y: attrs.y });
      const rawSize = display && Number.isFinite(display.size)
        ? display.size
        : deps.nodeDisplaySize(attrs);
      const size = typeof r.scaleSize === 'function'
        ? r.scaleSize(rawSize)
        : rawSize;
      const radius = Math.max(Number.isFinite(size) ? size : 0, deps.minimumNodeScreenRadius());

      return {
        x: point.x,
        y: point.y - radius,
        placement: 'node-top',
        nodeDisk: {
          x: point.x,
          y: point.y,
          radius,
        },
      };
    }

    function nodeTooltipLabel(d) {
      return d.fullLabel || d.title || String(d.label || '').replace(/\s*\n\s*/g, ' ') || d.id || 'Untitled';
    }

    function showNodeTooltip(node, pos, pinned) {
      const g = graph();
      if (!g || !tooltip || !graphHasNode(node)) return;

      const d = g.getNodeAttributes(node);
      if (mobileViewport()) {
        if (pinned && d.kind === 'paper') showPaperModal(d);
        else hideTooltip();
        return;
      }

      if (d.kind === 'aggregate') {
        showAggregateTooltip(d, pos, pinned);
        return;
      }

      const anchor = nodeTooltipPosition(node) || pos;
      const authors = formatAuthors(d.authors);
      const tags = (d.tags || []).slice(0, 7).join(' · ');
      const actions = paperActionLinks(d, { includeMap: false });
      const shortLabel = String(d.fullLabel || d.label || '').replace(/\s*\n\s*/g, ' ').trim();
      tooltip.innerHTML =
        `<div class="tt-title">${escHtml(d.title)}</div>` +
        (shortLabel && shortLabel !== d.title ? `<div class="tt-short-label">${escHtml(shortLabel)}</div>` : '') +
        `<div class="tt-meta">${escHtml(authors)}&nbsp;&nbsp;${d.year || ''}</div>` +
        (tags ? `<div class="tt-tags">${escHtml(tags)}</div>` : '') +
        (d.summary ? `<div class="tt-summary">${escHtml(d.summary)}</div>` : '') +
        (actions ? `<div class="tt-actions paper-link-pills">${actions}</div>` : '') +
        (!pinned ? `<div class="tt-hint">Click to pin</div>` : `<div class="tt-hint">Click node again to unpin</div>`);
      tooltip.classList.toggle('pinned', pinned);
      placeTooltip(anchor);
    }

    function showAggregateTooltip(d, pos, pinned) {
      if (!tooltip) return;

      const level = deps.detailLevelLabel(d.detailLevel);
      const nextIndex = deps.detailLevels.indexOf(d.detailLevel) + 1;
      const nextLabel = deps.detailLevels[nextIndex]
        ? deps.detailLevelLabel(deps.detailLevels[nextIndex])
        : null;

      tooltip.innerHTML =
        `<div class="tt-title">${escHtml(d.fullLabel || d.title)}</div>` +
        `<div class="tt-meta">${escHtml(level)} group&nbsp;&nbsp;${d.count || 0} items</div>` +
        (nextLabel ? `<div class="tt-hint">Click to show ${escHtml(nextLabel)}</div>` : '') +
        (!nextLabel && !pinned ? `<div class="tt-hint">Click to pin</div>` : '') +
        (!nextLabel && pinned ? `<div class="tt-hint">Click node again to unpin</div>` : '');
      tooltip.classList.toggle('pinned', pinned);
      placeTooltip(pos);
    }

    function showHoverTooltip(node) {
      const g = graph();
      if (!hoverTooltip || mobileViewport() || !g || !graphHasNode(node) || !nodeVisible(node)) return;

      const d = g.getNodeAttributes(node);
      const pos = nodeTooltipPosition(node);
      if (!pos) return;
      const label = nodeTooltipLabel(d);
      const subtitle = d.kind === 'paper' && d.title && d.title !== label
        ? d.title
        : '';
      const meta = d.kind === 'aggregate'
        ? `${deps.detailLevelLabel(d.detailLevel)} group · ${d.count || 0} items`
        : [formatAuthors(d.authors), d.year].filter(Boolean).join('  ');

      viewState.hoverTooltipNode = node;
      hoverTooltip.innerHTML =
        `<div class="tt-mini-title">${escHtml(label)}</div>` +
        (subtitle ? `<div class="tt-mini-subtitle">${escHtml(subtitle)}</div>` : '') +
        (meta ? `<div class="tt-mini-meta">${escHtml(meta)}</div>` : '');
      hoverTooltip.classList.add('visible');
      placeTooltip(pos, { element: hoverTooltip });
    }

    function hideHoverTooltip() {
      viewState.hoverTooltipNode = null;
      if (hoverTooltip) hoverTooltip.classList.remove('visible');
    }

    function updateActiveTooltipPositions() {
      if (viewState.pinnedNode && tooltip && tooltip.classList.contains('visible')) {
        const pos = nodeTooltipPosition(viewState.pinnedNode);
        if (pos) placeTooltip(pos);
      }

      if (viewState.hoverTooltipNode && hoverTooltip && hoverTooltip.classList.contains('visible')) {
        if (!graphHasNode(viewState.hoverTooltipNode) || !nodeVisible(viewState.hoverTooltipNode)) {
          hideHoverTooltip();
          return;
        }
        if (!viewState.pinnedNode && viewState.hoverTooltipNode !== viewState.hoveredNode) {
          hideHoverTooltip();
          return;
        }
        const pos = nodeTooltipPosition(viewState.hoverTooltipNode);
        if (pos) placeTooltip(pos, { element: hoverTooltip });
      }
    }

    function placeTooltip(pos, options = {}) {
      const el = options.element || tooltip;
      if (!el || !pos || !graphContainer) return;

      const MARGIN = 12;
      const graphRect = graphContainer.getBoundingClientRect();

      el.classList.add('visible');
      const W = el.offsetWidth;
      const H = el.offsetHeight;

      const anchorX = graphRect.left + pos.x;
      const anchorY = graphRect.top + pos.y;
      const bounds = tooltipGraphViewportRect(MARGIN);
      const avoidRects = tooltipAvoidRects(bounds);
      const minX = Math.min(bounds.left, Math.max(bounds.left, bounds.right - W));
      const maxX = Math.max(minX, bounds.right - W);
      const minTop = Math.min(bounds.top, Math.max(bounds.top, bounds.bottom - H));
      const maxTop = Math.max(minTop, bounds.bottom - H);
      const clampX = value => Math.max(minX, Math.min(value, maxX));
      const clampY = value => Math.max(minTop, Math.min(value, maxTop));

      if (pos.placement === 'node-top') {
        placeNodeAnchoredTooltip(el, pos, {
          graphRect,
          bounds,
          avoidRects,
          margin: MARGIN,
          width: W,
          height: H,
          clampX,
          clampY,
        });
        return;
      }

      const rawCandidates = [
        { x: anchorX + MARGIN, y: anchorY + MARGIN },
        { x: anchorX + MARGIN, y: anchorY - H - MARGIN },
        { x: anchorX - W - MARGIN, y: anchorY + MARGIN },
        { x: anchorX - W - MARGIN, y: anchorY - H - MARGIN },
      ];

      const candidates = rawCandidates.map((candidate, index) => ({
        x: clampX(candidate.x),
        y: clampY(candidate.y),
        index,
      }));

      const best = candidates.reduce((winner, candidate) => {
        const overlap = tooltipCollisionArea(candidate.x, candidate.y, W, H, avoidRects);
        const distance = Math.abs(candidate.x - rawCandidates[candidate.index].x) +
          Math.abs(candidate.y - rawCandidates[candidate.index].y);
        const score = overlap * 1000 + distance + candidate.index;
        return !winner || score < winner.score ? { ...candidate, score } : winner;
      }, null);

      const x = best ? best.x : clampX(anchorX + MARGIN);
      const y = best ? best.y : clampY(anchorY + MARGIN);

      el.style.left = `${x}px`;
      el.style.top = `${y}px`;
    }

    function placeNodeAnchoredTooltip(el, pos, options) {
      const graphRect = options.graphRect;
      const margin = options.margin;
      const W = options.width;
      const H = options.height;
      const clampX = options.clampX;
      const clampY = options.clampY;
      const disk = pos.nodeDisk || null;

      if (!disk) {
        el.style.left = `${clampX(graphRect.left + pos.x - W / 2)}px`;
        el.style.top = `${clampY(graphRect.top + pos.y - H - margin)}px`;
        return;
      }

      const centerX = graphRect.left + disk.x;
      const centerY = graphRect.top + disk.y;
      const radius = Math.max(Number(disk.radius) || 0, deps.minimumNodeScreenRadius());
      const gap = margin;
      const diskRect = {
        left: centerX - radius,
        right: centerX + radius,
        top: centerY - radius,
        bottom: centerY + radius,
      };
      const rawCandidates = [
        { x: centerX - W / 2, y: centerY - radius - H - gap },
        { x: centerX + radius + gap, y: centerY - H / 2 },
        { x: centerX - radius - gap - W, y: centerY - H / 2 },
        { x: centerX - W / 2, y: centerY + radius + gap },
        { x: centerX + radius + gap, y: centerY - radius - H - gap },
        { x: centerX - radius - gap - W, y: centerY - radius - H - gap },
        { x: centerX + radius + gap, y: centerY + radius + gap },
        { x: centerX - radius - gap - W, y: centerY + radius + gap },
      ];
      const candidates = rawCandidates.map((candidate, index) => ({
        x: clampX(candidate.x),
        y: clampY(candidate.y),
        index,
      }));

      const best = candidates.reduce((winner, candidate) => {
        const raw = rawCandidates[candidate.index];
        const diskOverlap = tooltipCollisionArea(candidate.x, candidate.y, W, H, [diskRect]);
        const blockerOverlap = tooltipCollisionArea(candidate.x, candidate.y, W, H, options.avoidRects);
        const displacement = Math.abs(candidate.x - raw.x) + Math.abs(candidate.y - raw.y);
        const score = diskOverlap * 100000 + blockerOverlap * 1000 + displacement * 4 + candidate.index;
        return !winner || score < winner.score ? { ...candidate, score } : winner;
      }, null);

      const x = best ? best.x : clampX(centerX - W / 2);
      const y = best ? best.y : clampY(centerY - radius - H - gap);

      el.style.left = `${x}px`;
      el.style.top = `${y}px`;
    }

    function visibleElementRect(el) {
      if (!el || el.hidden) return null;
      const style = getComputedStyle(el);
      if (style.display === 'none' || style.visibility === 'hidden' || style.pointerEvents === 'none') return null;
      const rect = el.getBoundingClientRect();
      if (rect.width <= 0 || rect.height <= 0) return null;
      return {
        left: rect.left,
        right: rect.right,
        top: rect.top,
        bottom: rect.bottom,
        width: rect.width,
        height: rect.height,
      };
    }

    function tooltipBoundaryRects() {
      const selectors = [
        '#mm-panel-header',
        '#mm-panel',
        '.md-header',
        '.md-tabs',
        '.md-sidebar--primary',
        '.md-sidebar--secondary',
      ];
      const elements = new Set();
      selectors.forEach(selector => {
        document.querySelectorAll(selector).forEach(el => elements.add(el));
      });

      return [...elements]
        .map(visibleElementRect)
        .filter(Boolean);
    }

    function rectOverlap(a, b) {
      return {
        x: Math.max(0, Math.min(a.right, b.right) - Math.max(a.left, b.left)),
        y: Math.max(0, Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top)),
      };
    }

    function tooltipGraphViewportRect(margin) {
      const graphRect = graphContainer.getBoundingClientRect();
      const rootStyle = getComputedStyle(document.documentElement);
      const headerHeight = parseFloat(rootStyle.getPropertyValue('--mm-header-h')) || 0;
      const footerHeight = parseFloat(rootStyle.getPropertyValue('--mm-footer-h')) || 0;
      const rect = {
        left: Math.max(margin, graphRect.left + margin),
        right: Math.min(window.innerWidth - margin, graphRect.right - margin),
        top: Math.max(margin, headerHeight + margin, graphRect.top + margin),
        bottom: Math.min(window.innerHeight - footerHeight - margin, graphRect.bottom - margin),
      };

      tooltipBoundaryRects().forEach(blocker => {
        const overlap = rectOverlap(rect, blocker);
        const width = Math.max(1, rect.right - rect.left);
        const height = Math.max(1, rect.bottom - rect.top);

        if (overlap.y > 0 && blocker.height > height * 0.25) {
          if (blocker.left <= rect.left + 1 && blocker.right > rect.left) {
            rect.left = Math.max(rect.left, blocker.right + margin);
          }
          if (blocker.right >= rect.right - 1 && blocker.left < rect.right) {
            rect.right = Math.min(rect.right, blocker.left - margin);
          }
        }

        if (overlap.x > 0 && blocker.width > width * 0.35) {
          if (blocker.top <= rect.top + 1 && blocker.bottom > rect.top) {
            rect.top = Math.max(rect.top, blocker.bottom + margin);
          }
          if (blocker.bottom >= rect.bottom - 1 && blocker.top < rect.bottom) {
            rect.bottom = Math.min(rect.bottom, blocker.top - margin);
          }
        }
      });

      if (rect.right <= rect.left) {
        rect.left = Math.max(margin, graphRect.left + margin);
        rect.right = Math.max(rect.left + 1, Math.min(window.innerWidth - margin, graphRect.right - margin));
      }
      if (rect.bottom <= rect.top) {
        rect.top = Math.max(margin, headerHeight + margin, graphRect.top + margin);
        rect.bottom = Math.max(rect.top + 1, Math.min(window.innerHeight - footerHeight - margin, graphRect.bottom - margin));
      }

      return rect;
    }

    function tooltipAvoidRects(bounds) {
      const canvasBounds = bounds || tooltipGraphViewportRect(12);
      return [
        ...tooltipBoundaryRects(),
      ].filter(rect => {
        const overlap = rectOverlap(canvasBounds, rect);
        return overlap.x > 0 && overlap.y > 0;
      });
    }

    function tooltipCollisionArea(left, top, width, height, rects) {
      return rects.reduce((area, rect) => {
        const overlapX = Math.max(0, Math.min(left + width, rect.right) - Math.max(left, rect.left));
        const overlapY = Math.max(0, Math.min(top + height, rect.bottom) - Math.max(top, rect.top));
        return area + overlapX * overlapY;
      }, 0);
    }

    function hideTooltip() {
      if (tooltip) tooltip.classList.remove('visible', 'pinned');
    }

    function hidePaperModal() {
      if (!modal) return;
      modal.hidden = true;
      if (modalBody) modalBody.innerHTML = '';
      if (modalTitle) modalTitle.textContent = 'Paper';
    }

    function paperDetailUrl(d) {
      return `../papers/${d.id}/`;
    }

    function paperTreeUrl(d) {
      return `../tree/#paper=${encodeURIComponent(d.id)}`;
    }

    function paperMapUrl(d) {
      return `#paper=${encodeURIComponent(d.id)}`;
    }

    function paperTimelineUrl(d) {
      return `../timeline/#paper=${encodeURIComponent(d.id)}`;
    }

    function paperSearchUrl(d) {
      return `../search/?paper=${encodeURIComponent(d.id)}`;
    }

    function paperActionLink(url, label, variant, external) {
      return window.kbSiteLinks.renderPill({
        url,
        label,
        variant: variant || 'internal',
        external: Boolean(external),
        detail: external ? '' : `Open in ${label}`,
      });
    }

    function paperActionLinks(d, options) {
      const includeMap = !options || options.includeMap !== false;
      return [
        paperActionLink(d.link, 'Document', 'primary', true),
        window.kbSiteLinks.renderPaperSiteLinks(
          {
            url: paperDetailUrl(d),
            mapUrl: paperMapUrl(d),
            treeUrl: paperTreeUrl(d),
            timelineUrl: paperTimelineUrl(d),
            searchUrl: paperSearchUrl(d),
          },
          { includeMap }
        ),
      ].join('');
    }

    function showPaperModal(d) {
      if (!modal || !modalBody || !modalTitle) return;

      const title = d.title || d.fullLabel || d.label || 'Untitled';
      const year = d.year || 'Undated';
      const summary = d.summary || 'No summary recorded yet.';
      const abstract = d.abstract || 'No abstract recorded yet.';
      const tags = (d.tags || [])
        .slice(0, 10)
        .map(tag => `<span>${escHtml(tag)}</span>`)
        .join('');

      hideTooltip();
      modalTitle.textContent = title;
      modalBody.innerHTML =
        `<div class="mm-detail-kicker">${escHtml(year)}</div>` +
        (d.label && d.label !== title ? `<p class="mm-detail-title">${escHtml(d.label)}</p>` : '') +
        `<div class="mm-modal-section-title">Abstract</div>` +
        `<p class="mm-abstract">${escHtml(abstract)}</p>` +
        `<div class="mm-modal-section-title">Summary</div>` +
        `<p class="mm-summary">${escHtml(summary)}</p>` +
        (tags ? `<div class="mm-tags">${tags}</div>` : '') +
        `<div class="mm-detail-actions paper-link-pills">` +
        paperActionLinks(d, { includeMap: false }) +
        `</div>`;
      modal.hidden = false;
      if (modalClose) modalClose.focus({ preventScroll: true });
    }

    function closePaperModalSelection() {
      if (!modal || modal.hidden) return;
      hidePaperModal();
      viewState.clearSelection();
      if (typeof deps.setSelectedNodeFilterEnabled === 'function') {
        deps.setSelectedNodeFilterEnabled(false);
      }
      hideHoverTooltip();
      if (typeof deps.syncUrlToPinnedNode === 'function') deps.syncUrlToPinnedNode();
      if (typeof deps.refreshView === 'function') deps.refreshView();
    }

    function setupModalControls() {
      if (modalClose) modalClose.addEventListener('click', closePaperModalSelection);
      if (modal) {
        modal.addEventListener('click', event => {
          if (event.target === modal) closePaperModalSelection();
        });
      }
      window.addEventListener('keydown', event => {
        if (event.key === 'Escape' && modal && !modal.hidden) closePaperModalSelection();
      });
    }

    function showFocusedPaperTooltip(node) {
      const r = renderer();
      if (!r || !graphHasNode(node)) return;
      showNodeTooltip(node, nodeTooltipPosition(node), true);
    }

    return {
      closePaperModalSelection,
      hideHoverTooltip,
      hidePaperModal,
      hideTooltip,
      nodeTooltipPosition,
      setupModalControls,
      showFocusedPaperTooltip,
      showHoverTooltip,
      showNodeTooltip,
      updateActiveTooltipPositions,
    };
  }

  window.kbMapOverlays = {
    createMapOverlays,
  };
}());
