/* browser/camera.js - camera fitting, URL focus, and distance measurements. */

'use strict';

(function () {
  function createMapCamera(deps = {}) {
    const graphContainer = deps.graphContainer;
    const viewState = deps.viewState;
    const clamp = deps.clamp || ((value, min, max) => Math.max(min, Math.min(value, max)));
    let fitMeasureContext = null;

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

    function fitNodeEligible(attrs) {
      return deps.hierarchyLevelById.has(attrs.detailLevel) && deps.nodeAllowedByFilters(attrs);
    }

    function expandBBoxes(bboxes, rawPoint, framedPoint, rawRadius = 0) {
      const radius = Number.isFinite(rawRadius) ? Math.max(0, rawRadius) : 0;
      bboxes.rawXmin = Math.min(bboxes.rawXmin, rawPoint.x - radius);
      bboxes.rawXmax = Math.max(bboxes.rawXmax, rawPoint.x + radius);
      bboxes.rawYmin = Math.min(bboxes.rawYmin, rawPoint.y - radius);
      bboxes.rawYmax = Math.max(bboxes.rawYmax, rawPoint.y + radius);
      bboxes.framedXmin = Math.min(bboxes.framedXmin, framedPoint.x);
      bboxes.framedXmax = Math.max(bboxes.framedXmax, framedPoint.x);
      bboxes.framedYmin = Math.min(bboxes.framedYmin, framedPoint.y);
      bboxes.framedYmax = Math.max(bboxes.framedYmax, framedPoint.y);
    }

    function finalBBoxes(bboxes) {
      let {
        rawXmin,
        rawXmax,
        rawYmin,
        rawYmax,
        framedXmin,
        framedXmax,
        framedYmin,
        framedYmax,
      } = bboxes;

      if (!Number.isFinite(rawXmin) || !Number.isFinite(framedXmin)) return null;

      if (rawXmin === rawXmax) {
        rawXmin -= 1;
        rawXmax += 1;
      }
      if (rawYmin === rawYmax) {
        rawYmin -= 1;
        rawYmax += 1;
      }
      if (framedXmin === framedXmax) {
        framedXmin -= 0.01;
        framedXmax += 0.01;
      }
      if (framedYmin === framedYmax) {
        framedYmin -= 0.01;
        framedYmax += 0.01;
      }

      const rawPadX = Math.max((rawXmax - rawXmin) * 0.04, 1);
      const rawPadY = Math.max((rawYmax - rawYmin) * 0.04, 1);
      const framedPadX = Math.max((framedXmax - framedXmin) * 0.04, 0.01);
      const framedPadY = Math.max((framedYmax - framedYmin) * 0.04, 0.01);

      return {
        raw: {
          x: [rawXmin - rawPadX, rawXmax + rawPadX],
          y: [rawYmin - rawPadY, rawYmax + rawPadY],
        },
        framed: {
          x: [framedXmin - framedPadX, framedXmax + framedPadX],
          y: [framedYmin - framedPadY, framedYmax + framedPadY],
        },
      };
    }

    function rawBBoxForNodes(nodes) {
      const g = graph();
      const bboxes = {
        rawXmin: Infinity,
        rawXmax: -Infinity,
        rawYmin: Infinity,
        rawYmax: -Infinity,
      };

      nodes.forEach(node => {
        if (!graphHasNode(node)) return;
        const attrs = g.getNodeAttributes(node);
        const point = deps.homePoint(attrs);
        const radius = Math.max(Number(deps.nodeDisplaySize(attrs)) || 0, 0);
        if (!Number.isFinite(point.x) || !Number.isFinite(point.y)) return;

        bboxes.rawXmin = Math.min(bboxes.rawXmin, point.x - radius);
        bboxes.rawXmax = Math.max(bboxes.rawXmax, point.x + radius);
        bboxes.rawYmin = Math.min(bboxes.rawYmin, point.y - radius);
        bboxes.rawYmax = Math.max(bboxes.rawYmax, point.y + radius);
      });

      if (!Number.isFinite(bboxes.rawXmin)) return null;

      if (bboxes.rawXmin === bboxes.rawXmax) {
        bboxes.rawXmin -= 1;
        bboxes.rawXmax += 1;
      }
      if (bboxes.rawYmin === bboxes.rawYmax) {
        bboxes.rawYmin -= 1;
        bboxes.rawYmax += 1;
      }

      const rawPadX = Math.max((bboxes.rawXmax - bboxes.rawXmin) * 0.04, 1);
      const rawPadY = Math.max((bboxes.rawYmax - bboxes.rawYmin) * 0.04, 1);

      return {
        x: [bboxes.rawXmin - rawPadX, bboxes.rawXmax + rawPadX],
        y: [bboxes.rawYmin - rawPadY, bboxes.rawYmax + rawPadY],
      };
    }

    function zoomOutRawBBox() {
      const g = graph();
      const nodes = [];
      g.forEachNode((node, attrs) => {
        if (fitNodeEligible(attrs)) nodes.push(node);
      });
      if (nodes.length) return rawBBoxForNodes(nodes);

      const allNodes = [];
      g.forEachNode(node => allNodes.push(node));
      return rawBBoxForNodes(allNodes);
    }

    function framedPointForRawPoint(point, padding) {
      const r = renderer();
      const baseState = { x: 0.5, y: 0.5, ratio: 1, angle: 0 };
      const viewportPoint = r.graphToViewport(point, { cameraState: baseState, padding });
      return r.viewportToFramedGraph(viewportPoint, { cameraState: baseState, padding });
    }

    function viewportBBoxForRawBBox(rawBBox, cameraState, padding) {
      const r = renderer();
      const points = [
        { x: rawBBox.x[0], y: rawBBox.y[0] },
        { x: rawBBox.x[1], y: rawBBox.y[0] },
        { x: rawBBox.x[0], y: rawBBox.y[1] },
        { x: rawBBox.x[1], y: rawBBox.y[1] },
      ].map(point => r.graphToViewport(point, { cameraState, padding }));

      const xs = points.map(point => point.x).filter(Number.isFinite);
      const ys = points.map(point => point.y).filter(Number.isFinite);
      if (!xs.length || !ys.length) return null;

      const left = Math.min(...xs);
      const right = Math.max(...xs);
      const top = Math.min(...ys);
      const bottom = Math.max(...ys);

      return {
        left,
        right,
        top,
        bottom,
        width: right - left,
        height: bottom - top,
      };
    }

    function zoomOutLimitForRawBBox(rawBBox, minAllowedRatio = 0) {
      const r = renderer();
      if (!r || !rawBBox) return null;

      const dims = r.getDimensions();
      if (!dims.width || !dims.height) return null;

      const padding = deps.viewportPadding;
      const usable = usableCanvasRect(padding);
      const usableWidth = Math.max(usable.right - usable.left, 1);
      const usableHeight = Math.max(usable.bottom - usable.top, 1);
      const rawCenter = {
        x: (rawBBox.x[0] + rawBBox.x[1]) / 2,
        y: (rawBBox.y[0] + rawBBox.y[1]) / 2,
      };
      const framedCenter = framedPointForRawPoint(rawCenter, padding);
      if (!Number.isFinite(framedCenter.x) || !Number.isFinite(framedCenter.y)) return null;

      const centeredState = {
        x: framedCenter.x,
        y: framedCenter.y,
        ratio: 1,
        angle: 0,
      };
      const screenBBox = viewportBBoxForRawBBox(rawBBox, centeredState, padding);
      if (!screenBBox) return null;

      const requiredRatio = Math.max(
        1,
        screenBBox.width / usableWidth,
        screenBBox.height / usableHeight,
        Number(minAllowedRatio) || 0
      );

      return Math.max(
        deps.minCameraRatio * 1.05,
        requiredRatio * deps.maxZoomOutOverscanRatio
      );
    }

    function updateZoomOutLimit(minAllowedRatio = 0) {
      const r = renderer();
      if (!r || !graph()) return;

      const limit = zoomOutLimitForRawBBox(zoomOutRawBBox(), minAllowedRatio);
      if (!Number.isFinite(limit)) return;

      const currentLimit = Number(r.getSetting('maxCameraRatio'));
      if (Number.isFinite(currentLimit) && Math.abs(currentLimit - limit) < 1e-4) return;

      r.setSetting('maxCameraRatio', limit);
    }

    function allDetailBBoxes() {
      const g = graph();
      const r = renderer();
      const bboxes = {
        rawXmin: Infinity,
        rawXmax: -Infinity,
        rawYmin: Infinity,
        rawYmax: -Infinity,
        framedXmin: Infinity,
        framedXmax: -Infinity,
        framedYmin: Infinity,
        framedYmax: -Infinity,
      };

      g.forEachNode((node, attrs) => {
        if (!fitNodeEligible(attrs)) return;

        const rawPoint = deps.homePoint(attrs);
        const rawRadius = deps.nodeDisplaySize(attrs);
        const displayAttrs = r && typeof r.getNodeDisplayData === 'function'
          ? r.getNodeDisplayData(node)
          : null;
        const framedPoint = displayAttrs &&
          Number.isFinite(displayAttrs.x) &&
          Number.isFinite(displayAttrs.y)
            ? displayAttrs
            : attrs;

        expandBBoxes(bboxes, rawPoint, framedPoint, rawRadius);
      });

      return finalBBoxes(bboxes);
    }

    function visibleBBoxes() {
      const g = graph();
      const r = renderer();
      const bboxes = {
        rawXmin: Infinity,
        rawXmax: -Infinity,
        rawYmin: Infinity,
        rawYmax: -Infinity,
        framedXmin: Infinity,
        framedXmax: -Infinity,
        framedYmin: Infinity,
        framedYmax: -Infinity,
      };

      const visit = (node, attrs) => {
        const rawRadius = deps.nodeDisplaySize(attrs);
        const displayAttrs = r && typeof r.getNodeDisplayData === 'function'
          ? r.getNodeDisplayData(node)
          : null;
        const framedPoint = displayAttrs &&
          Number.isFinite(displayAttrs.x) &&
          Number.isFinite(displayAttrs.y)
            ? displayAttrs
            : attrs;

        expandBBoxes(bboxes, attrs, framedPoint, rawRadius);
      };

      if (viewState.visibleNodes) {
        viewState.visibleNodes.forEach(node => visit(node, g.getNodeAttributes(node)));
      } else {
        g.forEachNode((node, attrs) => {
          if (!nodeVisible(node)) return;
          visit(node, attrs);
        });
      }

      return finalBBoxes(bboxes);
    }

    function minimumPointDistance(points) {
      if (!Array.isArray(points) || points.length < 2) return Infinity;

      const sorted = points
        .filter(p => Number.isFinite(p.x) && Number.isFinite(p.y))
        .sort((a, b) => a.x - b.x || a.y - b.y);

      if (sorted.length < 2) return Infinity;

      let minDistSq = Infinity;
      let left = 0;

      for (let i = 0; i < sorted.length; i += 1) {
        const p = sorted[i];
        const currentMin = Number.isFinite(minDistSq) ? Math.sqrt(minDistSq) : Infinity;

        while (left < i && Number.isFinite(currentMin) && p.x - sorted[left].x > currentMin) {
          left += 1;
        }

        for (let j = left; j < i; j += 1) {
          const q = sorted[j];
          const dy = p.y - q.y;
          if (dy * dy >= minDistSq) continue;

          const dx = p.x - q.x;
          const distSq = dx * dx + dy * dy;
          if (distSq < minDistSq) {
            if (distSq === 0) return 0;
            minDistSq = distSq;
          }
        }
      }

      return Number.isFinite(minDistSq) ? Math.sqrt(minDistSq) : Infinity;
    }

    function minimumVisibleGraphDistance() {
      const g = graph();
      if (!g) return Infinity;

      const points = [];
      if (viewState.visibleNodes) {
        viewState.visibleNodes.forEach(node => {
          const attrs = g.getNodeAttributes(node);
          points.push({ x: attrs.x, y: attrs.y });
        });
      } else {
        g.forEachNode((node, attrs) => {
          if (!nodeVisible(node)) return;
          points.push({ x: attrs.x, y: attrs.y });
        });
      }

      return minimumPointDistance(points);
    }

    function minimumVisiblePaperGraphDistance() {
      const g = graph();
      if (!g) return Infinity;

      const points = [];
      const visit = (node, attrs) => {
        if (attrs.kind !== 'paper') return;
        points.push({ x: attrs.x, y: attrs.y });
      };

      if (viewState.visibleNodes) {
        viewState.visibleNodes.forEach(node => visit(node, g.getNodeAttributes(node)));
      } else {
        g.forEachNode((node, attrs) => {
          if (!nodeVisible(node)) return;
          visit(node, attrs);
        });
      }

      return minimumPointDistance(points);
    }

    function minimumVisibleScreenDistance(cameraState) {
      const r = renderer();
      const g = graph();
      if (!r || !g) return Infinity;

      const points = [];
      const visit = attrs => {
        const p = r.graphToViewport(
          { x: attrs.x, y: attrs.y },
          cameraState ? { cameraState } : undefined
        );
        points.push(p);
      };

      if (viewState.visibleNodes) {
        viewState.visibleNodes.forEach(node => visit(g.getNodeAttributes(node)));
      } else {
        g.forEachNode((node, attrs) => {
          if (!nodeVisible(node)) return;
          visit(attrs);
        });
      }

      return minimumPointDistance(points);
    }

    function fitNodes() {
      const g = graph();
      if (!g) return [];
      if (viewState.visibleNodes) return [...viewState.visibleNodes].filter(node => graphHasNode(node));

      const nodes = [];
      g.forEachNode((node) => {
        if (nodeVisible(node)) nodes.push(node);
      });
      return nodes;
    }

    function labelMeasureContext() {
      if (fitMeasureContext) return fitMeasureContext;
      if (typeof document === 'undefined') return null;
      fitMeasureContext = document.createElement('canvas').getContext('2d');
      return fitMeasureContext;
    }

    function nodeViewportRadius(attrs, cameraState, padding) {
      const r = renderer();
      const radius = deps.nodeDisplaySize(attrs);
      if (!Number.isFinite(radius) || radius <= 0) return 0;

      const origin = { x: attrs.x, y: attrs.y };
      const edge = { x: attrs.x + radius, y: attrs.y };
      const options = { cameraState, padding };
      const a = r.graphToViewport(origin, options);
      const b = r.graphToViewport(edge, options);
      return Math.abs(b.x - a.x);
    }

    function labelTextHalfExtents(attrs, cameraState) {
      const label = viewState.showNodeLabels ? attrs.label : '';
      if (!label) return { width: 0, height: 0 };

      const context = labelMeasureContext();
      const lines = String(label).split('\n');
      const zoomScale = deps.nodeLabelZoomScaleForRatio(cameraState && cameraState.ratio);
      const { fontSize, lineHeight, outlineWidth } = deps.currentNodeLabelMetrics(attrs, zoomScale);
      let maxWidth = 0;

      if (context) {
        context.font = `650 ${fontSize}px "Atkinson Hyperlegible Next", "Segoe UI", sans-serif`;
        lines.forEach(line => {
          maxWidth = Math.max(maxWidth, context.measureText(line).width);
        });
      } else {
        lines.forEach(line => {
          maxWidth = Math.max(maxWidth, String(line).length * fontSize * 0.58);
        });
      }

      return {
        width: maxWidth / 2 + outlineWidth + 4,
        height: ((Math.max(lines.length, 1) - 1) * lineHeight + fontSize) / 2 + outlineWidth + 4,
      };
    }

    function screenContentBBox(cameraState, padding) {
      const r = renderer();
      const g = graph();
      const nodes = fitNodes();
      if (!nodes.length) return null;

      const bounds = {
        left: Infinity,
        right: -Infinity,
        top: Infinity,
        bottom: -Infinity,
      };

      nodes.forEach(node => {
        const attrs = g.getNodeAttributes(node);
        const point = r.graphToViewport({ x: attrs.x, y: attrs.y }, { cameraState, padding });
        if (!Number.isFinite(point.x) || !Number.isFinite(point.y)) return;

        const nodeRadius = nodeViewportRadius(attrs, cameraState, padding);
        const labelExtents = labelTextHalfExtents(attrs, cameraState);
        const halfWidth = Math.max(nodeRadius, labelExtents.width);
        const halfHeight = Math.max(nodeRadius, labelExtents.height);

        bounds.left = Math.min(bounds.left, point.x - halfWidth);
        bounds.right = Math.max(bounds.right, point.x + halfWidth);
        bounds.top = Math.min(bounds.top, point.y - halfHeight);
        bounds.bottom = Math.max(bounds.bottom, point.y + halfHeight);
      });

      if (!Number.isFinite(bounds.left)) return null;

      return {
        ...bounds,
        width: bounds.right - bounds.left,
        height: bounds.bottom - bounds.top,
      };
    }

    function usableCanvasCenter(usable, dims) {
      return {
        x: usable.left < usable.right ? (usable.left + usable.right) / 2 : dims.width / 2,
        y: usable.top < usable.bottom ? (usable.top + usable.bottom) / 2 : dims.height / 2,
      };
    }

    function recenterCameraOnScreenBBox(cameraState, screenBBox, desired, padding) {
      const r = renderer();
      if (!screenBBox) return cameraState;

      const contentCenter = {
        x: (screenBBox.left + screenBBox.right) / 2,
        y: (screenBBox.top + screenBBox.bottom) / 2,
      };
      const framedContent = r.viewportToFramedGraph(contentCenter, { cameraState, padding });
      const framedDesired = r.viewportToFramedGraph(desired, { cameraState, padding });

      return {
        ...cameraState,
        x: cameraState.x + (framedContent.x - framedDesired.x),
        y: cameraState.y + (framedContent.y - framedDesired.y),
      };
    }

    function includeLabelsInFit(cameraState, usable, dims, padding) {
      let target = { ...cameraState };
      const desired = usableCanvasCenter(usable, dims);
      const usableWidth = Math.max(usable.right - usable.left, 1);
      const usableHeight = Math.max(usable.bottom - usable.top, 1);

      for (let i = 0; i < 4; i += 1) {
        const bounds = screenContentBBox(target, padding);
        if (!bounds) return target;

        const scale = Math.max(
          1,
          bounds.width / usableWidth,
          bounds.height / usableHeight
        );

        if (scale > 1.001) {
          target = {
            ...target,
            ratio: target.ratio * scale * 1.04,
          };
        }

        target = recenterCameraOnScreenBBox(target, screenContentBBox(target, padding), desired, padding);
      }

      return target;
    }

    function fitVisible(duration) {
      const r = renderer();
      if (!r || !graph()) return;

      if (typeof deps.finishLevelTransition === 'function') deps.finishLevelTransition();
      r.resize(true);
      r.refresh();

      const bboxes = visibleBBoxes() || allDetailBBoxes();
      if (!bboxes) return;

      const PAD = deps.viewportPadding;
      const dims = r.getDimensions();
      if (!dims.width || !dims.height) return;

      const usable = usableCanvasRect(PAD);
      const stagePadding = PAD;
      const desired = usableCanvasCenter(usable, dims);
      const bboxCenterX = (bboxes.framed.x[0] + bboxes.framed.x[1]) / 2;
      const bboxCenterY = (bboxes.framed.y[0] + bboxes.framed.y[1]) / 2;
      const baseState = { x: bboxCenterX, y: bboxCenterY, ratio: 1, angle: 0 };

      r.setCustomBBox(bboxes.raw);
      r.setSetting('stagePadding', stagePadding);
      r.refresh();

      const framedAtDesiredCenter = r.viewportToFramedGraph(
        desired,
        { cameraState: baseState, padding: stagePadding }
      );

      let target = {
        x: baseState.x + (bboxCenterX - framedAtDesiredCenter.x),
        y: baseState.y + (bboxCenterY - framedAtDesiredCenter.y),
        ratio: 1,
        angle: 0,
      };
      target = includeLabelsInFit(target, usable, dims, stagePadding);
      updateZoomOutLimit(target.ratio);

      if (duration === 0) r.getCamera().setState(target);
      else r.getCamera().animate(target, { duration: duration || 260 });
    }

    function readFocusPaperId() {
      try {
        const query = new URLSearchParams(window.location.search);
        const paperId = query.get('paper') || query.get('node');
        if (paperId) return paperId;
      } catch (error) {
        // Keep supporting hash-only browsers/links if query parsing fails.
      }

      const hash = window.location.hash.slice(1);
      if (!hash) return null;

      const params = new URLSearchParams(hash);
      return params.get('paper') || params.get('node');
    }

    function writeFocusPaperId(paperId) {
      const params = new URLSearchParams(window.location.hash.slice(1));

      if (paperId) {
        if (params.get('paper') === paperId && !params.has('node')) return;
        params.set('paper', paperId);
        params.delete('node');
      } else {
        if (!params.has('paper') && !params.has('node')) return;
        params.delete('paper');
        params.delete('node');
      }

      const url = new URL(window.location.href);
      url.hash = params.toString();
      window.history.replaceState(null, '', url);
    }

    function paperIdForNode(node) {
      const g = graph();
      if (!node || !g || !graphHasNode(node)) return null;
      const attrs = g.getNodeAttributes(node);
      return attrs.kind === 'paper' ? node : null;
    }

    function syncUrlToPinnedNode() {
      writeFocusPaperId(paperIdForNode(viewState.pinnedNode));
    }

    function clearPinnedPaperSelection() {
      if (!paperIdForNode(viewState.pinnedNode)) return false;

      viewState.clearSelection();
      if (typeof deps.setSelectedNodeFilterEnabled === 'function') {
        deps.setSelectedNodeFilterEnabled(false);
      }
      if (typeof deps.hideHoverTooltip === 'function') deps.hideHoverTooltip();
      if (typeof deps.hideTooltip === 'function') deps.hideTooltip();
      if (typeof deps.hidePaperModal === 'function') deps.hidePaperModal();
      if (typeof deps.refreshView === 'function') deps.refreshView();
      return true;
    }

    function overlayBounds(el, graphRect, dims) {
      if (!el) return null;

      const rect = el.getBoundingClientRect();
      const left = clamp(rect.left - graphRect.left, 0, dims.width);
      const right = clamp(rect.right - graphRect.left, 0, dims.width);
      const top = clamp(rect.top - graphRect.top, 0, dims.height);
      const bottom = clamp(rect.bottom - graphRect.top, 0, dims.height);

      if (right <= left || bottom <= top) return null;
      return { left, right, top, bottom, width: right - left, height: bottom - top };
    }

    function applyTopOverlayOcclusion(rect, bounds, dims, pad, maxHeightRatio = deps.panelMaxFocusWidthRatio) {
      if (!bounds || bounds.height >= dims.height * maxHeightRatio) return;

      const centerX = (rect.left + rect.right) / 2;
      const centerUnderOverlay = centerX >= bounds.left && centerX <= bounds.right;
      if (!centerUnderOverlay || bounds.bottom <= rect.top) return;

      rect.top = Math.max(rect.top, Math.min(bounds.bottom + pad, dims.height - pad));
    }

    function usableCanvasRect(pad = deps.viewportPadding) {
      const r = renderer();
      const dims = r.getDimensions();
      const graphRect = graphContainer.getBoundingClientRect();
      const minWidth = Math.min(dims.width, pad * 2 + 1);
      const minHeight = Math.min(dims.height, pad * 2 + 1);
      const rect = {
        left: Math.min(pad, dims.width / 2),
        top: Math.min(pad, dims.height / 2),
        right: Math.max(dims.width - pad, minWidth),
        bottom: Math.max(dims.height - pad, minHeight),
      };

      const panel = document.getElementById('mm-panel');
      const panelOpen = panel && !panel.classList.contains('body-collapsed');
      const panelBounds = panelOpen ? overlayBounds(panel, graphRect, dims) : null;
      const branchPanel = document.getElementById('mm-branch-panel');
      const branchPanelOpen = branchPanel && !branchPanel.classList.contains('body-collapsed');
      const branchBounds = branchPanelOpen ? overlayBounds(branchPanel, graphRect, dims) : null;

      applyTopOverlayOcclusion(rect, panelBounds, dims, pad);

      if (branchBounds && branchBounds.right >= dims.width - pad && branchBounds.width < dims.width * 0.45) {
        rect.right = Math.min(rect.right, Math.max(branchBounds.left - pad, pad));
      } else {
        applyTopOverlayOcclusion(rect, branchBounds, dims, pad, 0.7);
      }

      const headerBounds = overlayBounds(document.getElementById('mm-panel-header'), graphRect, dims);
      applyTopOverlayOcclusion(rect, headerBounds, dims, pad, 0.5);

      if (rect.right <= rect.left) {
        rect.left = Math.min(pad, dims.width / 2);
        rect.right = Math.max(dims.width - pad, rect.left + 1);
      }
      if (rect.bottom <= rect.top) {
        rect.top = Math.min(pad, dims.height / 2);
        rect.bottom = Math.max(dims.height - pad, rect.top + 1);
      }

      return rect;
    }

    function focusCameraOnNode(node, duration) {
      const r = renderer();
      const g = graph();
      if (!r || !graphHasNode(node)) return;

      r.resize(true);

      const attrs = g.getNodeAttributes(node);
      const dims = r.getDimensions();
      const usable = usableCanvasRect();
      const desiredX = usable.left < usable.right ? (usable.left + usable.right) / 2 : dims.width / 2;
      const desiredY = usable.top < usable.bottom ? (usable.top + usable.bottom) / 2 : dims.height / 2;
      const ratio = deps.focusedPaperCameraRatio;
      const nodeViewportPoint = r.graphToViewport({ x: attrs.x, y: attrs.y });
      const framedNode = r.viewportToFramedGraph(nodeViewportPoint);
      const baseState = { x: framedNode.x, y: framedNode.y, ratio, angle: 0 };
      const framedAtDesiredCenter = r.viewportToFramedGraph(
        { x: desiredX, y: desiredY },
        { cameraState: baseState, padding: deps.viewportPadding }
      );
      const target = {
        x: baseState.x + (framedNode.x - framedAtDesiredCenter.x),
        y: baseState.y + (framedNode.y - framedAtDesiredCenter.y),
        ratio,
        angle: 0,
      };

      if (duration === 0) r.getCamera().setState(target);
      else r.getCamera().animate(target, { duration: duration || 300 });
    }

    function refocusPinnedPaper(duration) {
      const paperId = paperIdForNode(viewState.pinnedNode) || readFocusPaperId();
      if (!paperId || !graphHasNode(paperId)) return false;

      const attrs = graph().getNodeAttributes(paperId);
      if (attrs.kind !== 'paper') return false;

      focusCameraOnNode(paperId, duration);
      window.setTimeout(() => deps.showFocusedPaperTooltip(paperId), (duration || 0) + 40);
      return true;
    }

    function focusPaperFromHash() {
      const paperId = readFocusPaperId();
      if (!paperId || !renderer() || !graphHasNode(paperId)) return false;

      const attrs = graph().getNodeAttributes(paperId);
      if (attrs.kind !== 'paper') return false;

      viewState.currentDetailLevel = 'paper';
      deps.selectBranchForPaper(attrs);
      viewState.selectNode(paperId);
      deps.setSelectedNodeFilterEnabled(true);
      deps.hideHoverTooltip();
      deps.updateDetailButtons();
      deps.refreshView();
      focusCameraOnNode(paperId, 320);
      window.setTimeout(() => deps.showFocusedPaperTooltip(paperId), 340);
      writeFocusPaperId(paperId);
      return true;
    }

    function syncPaperFocusFromHash() {
      if (readFocusPaperId()) {
        const focused = focusPaperFromHash();
        if (!focused) {
          clearPinnedPaperSelection();
          writeFocusPaperId(null);
        }
        return focused;
      }

      return clearPinnedPaperSelection();
    }

    return {
      fitVisible,
      focusCameraOnNode,
      focusPaperFromHash,
      labelTextHalfExtents,
      minimumVisibleGraphDistance,
      minimumVisiblePaperGraphDistance,
      minimumVisibleScreenDistance,
      paperIdForNode,
      readFocusPaperId,
      refocusPinnedPaper,
      syncPaperFocusFromHash,
      syncUrlToPinnedNode,
      updateZoomOutLimit,
      usableCanvasRect,
      writeFocusPaperId,
    };
  }

  window.kbMapCamera = {
    createMapCamera,
  };
}());
