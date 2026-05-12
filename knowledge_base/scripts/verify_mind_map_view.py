"""Browser smoke checks for the MkDocs/Sigma mind-map page.

The script talks to a local Chrome/Chromium instance over the Chrome DevTools
Protocol using only the Python standard library. It expects a served MkDocs
site URL, e.g. http://127.0.0.1:8123/mind-map/.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import secrets
import shutil
import socket
import struct
import subprocess
import sys
import tempfile
import time
import urllib.request
from dataclasses import dataclass
from typing import Any
from urllib.parse import quote, urlparse


JS_CHECKS = r"""
(async () => {
  const failures = [];
  const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
  const assert = (condition, message, detail) => {
    if (!condition) failures.push(detail ? `${message}: ${detail}` : message);
  };
  const colorIsWhite = color => {
    const c = String(color || '').trim().toLowerCase();
    return c === 'white' || c === '#fff' || c === '#ffffff' ||
      /^rgba?\(\s*255\s*,\s*255\s*,\s*255(?:\s*,\s*(?:1(?:\.0)?|0?\.\d+))?\s*\)$/.test(c);
  };
  const colorChannels = color => {
    const c = String(color || '').trim();
    let match = c.match(/^#([0-9a-f]{3})$/i);
    if (match) {
      return match[1].split('').map(ch => parseInt(ch + ch, 16)).concat(1);
    }
    match = c.match(/^#([0-9a-f]{6})$/i);
    if (match) {
      const hex = match[1];
      return [
        parseInt(hex.slice(0, 2), 16),
        parseInt(hex.slice(2, 4), 16),
        parseInt(hex.slice(4, 6), 16),
        1,
      ];
    }
    match = c.match(/^rgba?\(([^)]+)\)$/i);
    if (match) {
      const parts = match[1].split(',').map(part => Number(part.trim()));
      if (parts.length >= 3 && parts.slice(0, 3).every(Number.isFinite)) {
        return parts.slice(0, 3).concat(Number.isFinite(parts[3]) ? parts[3] : 1);
      }
    }
    return null;
  };
  const colorIsNeutralGrey = color => {
    const channels = colorChannels(color);
    if (!channels) return false;
    const [r, g, b] = channels;
    return Math.max(r, g, b) - Math.min(r, g, b) <= 1;
  };
  const colorAlpha = color => {
    const channels = colorChannels(color);
    return channels ? channels[3] : 0;
  };
  const edgeAlphaStats = edgeIds => {
    const alphas = edgeIds
      .map(id => renderer.getEdgeDisplayData(id))
      .filter(Boolean)
      .map(edge => colorAlpha(edge.color))
      .filter(Number.isFinite)
      .sort((a, b) => a - b);
    const pick = p => alphas[Math.min(alphas.length - 1, Math.max(0, Math.floor((alphas.length - 1) * p)))] || 0;
    return {
      min: alphas[0] || 0,
      p10: pick(0.10),
      median: pick(0.50),
      p90: pick(0.90),
      max: alphas[alphas.length - 1] || 0,
      count: alphas.length,
    };
  };
  const setScheme = scheme => {
    document.documentElement.setAttribute('data-md-color-scheme', scheme);
    document.body.setAttribute('data-md-color-scheme', scheme);
  };
  const cssVar = name => getComputedStyle(document.body).getPropertyValue(name).trim();
  const mm = window._mindMap;
  const graph = mm && mm.graph && mm.graph();
  const renderer = mm && mm.renderer && mm.renderer();
  const graphEl = document.getElementById('mm-graph');
  const panel = document.getElementById('mm-panel');

  assert(Boolean(mm && graph && renderer && graphEl), 'mind map debug surface is available');
  if (!(mm && graph && renderer && graphEl)) return { failures };

  const visibleNodes = () => graph.nodes().filter(id => {
    const data = renderer.getNodeDisplayData(id);
    return data && !data.hidden;
  });
  const visibleEdges = () => graph.edges().filter(id => {
    const data = renderer.getEdgeDisplayData(id);
    return data && !data.hidden;
  });
  const hashParams = () => new URLSearchParams(window.location.hash.slice(1));
  const canvasHasDarkPixelNear = (canvas, point) => {
    if (!canvas || !point || !Number.isFinite(point.x) || !Number.isFinite(point.y)) return false;
    const context = canvas.getContext('2d');
    if (!context) return false;

    const scaleX = canvas.width / Math.max(graphEl.clientWidth, 1);
    const scaleY = canvas.height / Math.max(graphEl.clientHeight, 1);
    const radiusX = Math.max(12, Math.round(58 * scaleX));
    const radiusY = Math.max(12, Math.round(32 * scaleY));
    const cx = Math.round(point.x * scaleX);
    const cy = Math.round(point.y * scaleY);
    const x = Math.max(0, cx - radiusX);
    const y = Math.max(0, cy - radiusY);
    const width = Math.min(canvas.width - x, radiusX * 2 + 1);
    const height = Math.min(canvas.height - y, radiusY * 2 + 1);
    if (width <= 0 || height <= 0) return false;

    const pixels = context.getImageData(x, y, width, height).data;
    let darkPixels = 0;
    for (let i = 0; i < pixels.length; i += 4) {
      const [r, g, b, a] = [pixels[i], pixels[i + 1], pixels[i + 2], pixels[i + 3]];
      if (a > 80 && r < 80 && g < 80 && b < 80) darkPixels += 1;
      if (darkPixels > 10) return true;
    }
    return false;
  };
  const overlayBounds = el => {
    if (!el) return null;
    const graphRect = graphEl.getBoundingClientRect();
    const rect = el.getBoundingClientRect();
    const left = Math.max(0, Math.min(rect.left - graphRect.left, graphEl.clientWidth));
    const right = Math.max(0, Math.min(rect.right - graphRect.left, graphEl.clientWidth));
    const top = Math.max(0, Math.min(rect.top - graphRect.top, graphEl.clientHeight));
    const bottom = Math.max(0, Math.min(rect.bottom - graphRect.top, graphEl.clientHeight));
    return right > left && bottom > top
      ? { left, right, top, bottom, width: right - left, height: bottom - top }
      : null;
  };
  const usableCanvasRect = (pad = 30) => {
    const rect = {
      left: Math.min(pad, graphEl.clientWidth / 2),
      top: Math.min(pad, graphEl.clientHeight / 2),
      right: Math.max(graphEl.clientWidth - pad, Math.min(graphEl.clientWidth, pad * 2 + 1)),
      bottom: Math.max(graphEl.clientHeight - pad, Math.min(graphEl.clientHeight, pad * 2 + 1)),
    };
    const panelOpen = Boolean(panel && !panel.classList.contains('body-collapsed'));
    const panelBounds = panelOpen ? overlayBounds(panel) : null;
    if (panelBounds && panelBounds.left <= pad && panelBounds.width < graphEl.clientWidth * 0.72) {
      rect.left = Math.max(rect.left, Math.min(panelBounds.right + pad, graphEl.clientWidth - pad));
    }
    const headerBounds = overlayBounds(document.getElementById('mm-panel-header'));
    if (headerBounds) {
      const centerX = (rect.left + rect.right) / 2;
      if (centerX >= headerBounds.left && centerX <= headerBounds.right && headerBounds.height < graphEl.clientHeight * 0.5) {
        rect.top = Math.max(rect.top, Math.min(headerBounds.bottom + pad, graphEl.clientHeight - pad));
      }
    }
    if (rect.right <= rect.left) {
      rect.left = Math.min(pad, graphEl.clientWidth / 2);
      rect.right = Math.max(graphEl.clientWidth - pad, rect.left + 1);
    }
    if (rect.bottom <= rect.top) {
      rect.top = Math.min(pad, graphEl.clientHeight / 2);
      rect.bottom = Math.max(graphEl.clientHeight - pad, rect.top + 1);
    }
    return rect;
  };
  const assertNodeCenteredInUsableCanvas = (node, label) => {
    const attrs = graph.getNodeAttributes(node);
    const point = renderer.graphToViewport({ x: attrs.x, y: attrs.y });
    const usable = usableCanvasRect();
    const expected = {
      x: (usable.left + usable.right) / 2,
      y: (usable.top + usable.bottom) / 2,
    };
    assert(Math.abs(point.x - expected.x) <= 36 && Math.abs(point.y - expected.y) <= 36,
      `${label} centers the paper in the usable canvas area`,
      JSON.stringify({ point, expected, usable }));
  };
  const viewportBBox = () => {
    const ids = visibleNodes();
    let minX = Infinity;
    let minY = Infinity;
    let maxX = -Infinity;
    let maxY = -Infinity;
    ids.forEach(id => {
      const attrs = graph.getNodeAttributes(id);
      const point = renderer.graphToViewport({ x: attrs.x, y: attrs.y });
      if (!Number.isFinite(point.x) || !Number.isFinite(point.y)) return;
      minX = Math.min(minX, point.x);
      minY = Math.min(minY, point.y);
      maxX = Math.max(maxX, point.x);
      maxY = Math.max(maxY, point.y);
    });
    return {
      minX, minY, maxX, maxY,
      width: graphEl.clientWidth,
      height: graphEl.clientHeight,
      count: ids.length,
      panelOpen: Boolean(panel && !panel.classList.contains('body-collapsed')),
      panelWidth: panel ? panel.offsetWidth : 0,
    };
  };
  const onScreenNodeIds = ids => ids.filter(id => {
    const attrs = graph.getNodeAttributes(id);
    const point = renderer.graphToViewport({ x: attrs.x, y: attrs.y });
    return Number.isFinite(point.x) &&
      Number.isFinite(point.y) &&
      point.x >= -120 &&
      point.x <= graphEl.clientWidth + 120 &&
      point.y >= -80 &&
      point.y <= graphEl.clientHeight + 80;
  });
  const assertAllVisibleLabelsForced = (level, label, requireOnScreenOnly = false) => {
    renderer.refresh();
    const ids = visibleNodes().filter(id => graph.getNodeAttribute(id, 'detailLevel') === level);
    const renderedIds = requireOnScreenOnly ? onScreenNodeIds(ids) : ids;
    const displayed = renderer.getNodeDisplayedLabels
      ? renderer.getNodeDisplayedLabels()
      : new Set();
    const unforced = ids.filter(id => {
      const data = renderer.getNodeDisplayData(id);
      return !data || data.forceLabel !== true;
    });

    assert(ids.length > 0, `${label} has visible nodes`, ids.length);
    assert(unforced.length === 0,
      `${label} forces all visible node labels`,
      JSON.stringify(unforced.slice(0, 8)));
    const missing = renderedIds.filter(id => !displayed.has(id));
    assert(missing.length === 0,
      requireOnScreenOnly
        ? `${label} renders every on-screen visible node label`
        : `${label} renders every visible node label`,
      JSON.stringify(missing.slice(0, 8)));
  };
  const assertAllVisibleLabelsForcedAcrossZoom = async (level, label) => {
    const before = { ...camera.getState() };
    assertAllVisibleLabelsForced(level, label);

    for (const ratioScale of [0.55, 1.85]) {
      camera.setState({ ratio: before.ratio * ratioScale });
      await sleep(50);
      renderer.refresh();
      assertAllVisibleLabelsForced(level, `${label} at ${ratioScale}x zoom`, true);
    }

    camera.setState(before);
    await sleep(50);
    renderer.refresh();
  };
  const assertPaperNodeClearance = label => {
    const metrics = mm.metrics && mm.metrics();
    const minDistance = metrics && metrics.minimumVisibleGraphDistance;
    const radius = metrics && metrics.nodeGraphRadius;
    const clearanceRatio = metrics && metrics.clearanceRatio;
    const requiredDistance = radius * (2 + clearanceRatio);

    assert(radius <= 12.1, `${label} uses reduced static paper disk radius`, radius);
    assert(minDistance + 0.05 >= requiredDistance,
      `${label} keeps at least the configured paper-node clearance`,
      JSON.stringify({ minDistance, radius, clearanceRatio, requiredDistance }));
  };
  const allDetailViewportBBox = () => {
    const detailLevels = new Set(['super_category', 'category', 'sub_category', 'paper']);
    const ids = graph.nodes().filter(id => detailLevels.has(graph.getNodeAttribute(id, 'detailLevel')));
    let minX = Infinity;
    let minY = Infinity;
    let maxX = -Infinity;
    let maxY = -Infinity;
    ids.forEach(id => {
      const attrs = graph.getNodeAttributes(id);
      const point = renderer.graphToViewport({
        x: Number.isFinite(attrs.homeX) ? attrs.homeX : attrs.x,
        y: Number.isFinite(attrs.homeY) ? attrs.homeY : attrs.y,
      });
      if (!Number.isFinite(point.x) || !Number.isFinite(point.y)) return;
      minX = Math.min(minX, point.x);
      minY = Math.min(minY, point.y);
      maxX = Math.max(maxX, point.x);
      maxY = Math.max(maxY, point.y);
    });
    return {
      minX, minY, maxX, maxY,
      width: graphEl.clientWidth,
      height: graphEl.clientHeight,
      count: ids.length,
      panelOpen: Boolean(panel && !panel.classList.contains('body-collapsed')),
      panelWidth: panel ? panel.offsetWidth : 0,
    };
  };
  const assertFittedBBox = (bbox, label) => {
    const reservePanel = bbox.panelOpen && bbox.panelWidth < bbox.width * 0.72 ? bbox.panelWidth : 0;
    const slack = 40;
    assert(bbox.count > 20, `${label} has visible nodes`, bbox.count);
    assert(bbox.minX >= reservePanel + 20 - slack,
      `${label} keeps nodes clear of the left/panel side`, JSON.stringify(bbox));
    assert(bbox.maxX <= bbox.width - 20 + slack,
      `${label} keeps nodes clear of the right side`, JSON.stringify(bbox));
    assert(bbox.minY >= 20 - slack,
      `${label} keeps nodes clear of the top side`, JSON.stringify(bbox));
    assert(bbox.maxY <= bbox.height - 20 + slack,
      `${label} keeps nodes clear of the bottom side`, JSON.stringify(bbox));
  };

  renderer.refresh();
  await sleep(80);

  const settings = renderer.getSettings();
  assert(settings.enableCameraRotation === false, 'camera rotation setting is disabled');
  assert(settings.enableEdgeEvents === false, 'edge hover/click events are disabled');
  assert(settings.minEdgeThickness <= 0.5, 'minimum edge thickness is subdued', settings.minEdgeThickness);
  assert(settings.itemSizesReference === 'positions',
    'node sizes are interpreted in graph coordinates', settings.itemSizesReference);

  const superGroups = [...document.querySelectorAll('#mm-category-filters > .mm-super-group')];
  assert(superGroups.length >= 2, 'sidebar has top-level super-category groups', superGroups.length);
  const detailControls = document.getElementById('mm-detail-controls');
  const detailLabel = detailControls &&
    detailControls.closest('.mm-section') &&
    detailControls.closest('.mm-section').querySelector('.mm-section-label');
  assert(detailLabel && detailLabel.textContent.trim() === 'Level-of-detail',
    'detail selector label reads Level-of-detail',
    detailLabel && detailLabel.textContent.trim());
  assert(superGroups.every(group => {
    const items = group.querySelector(':scope > .mm-cat-group-items');
    return items && getComputedStyle(items).display === 'none';
  }), 'sidebar super-category groups start collapsed');

  const camera = renderer.getCamera();
  const originalAngle = camera.getState().angle;
  camera.setState({ angle: originalAngle + 0.75 });
  await sleep(30);
  assert(Math.abs(camera.getState().angle - originalAngle) < 1e-8, 'camera rejects rotation changes');

  const initialLevel = mm.detailLevel && mm.detailLevel();
  let nodes = visibleNodes();
  let edges = visibleEdges();
  const initialSuperNodeCount = nodes.length;
  assert(initialLevel === 'super_category', 'mind map starts at the super-category detail level', initialLevel);
  assert(nodes.length >= 2 && nodes.length <= 20,
    'initial super-category node count is aggregated', nodes.length);
  assert(nodes.every(id => graph.getNodeAttribute(id, 'kind') === 'aggregate'),
    'initial visible nodes are aggregate nodes');
  await assertAllVisibleLabelsForcedAcrossZoom('super_category', 'super-category level');

  const cameraDelta = (a, b) =>
    Math.max(Math.abs(a.x - b.x), Math.abs(a.y - b.y), Math.abs(a.ratio - b.ratio));
  const beforeSuperClickCamera = { ...camera.getState() };
  const superNode = nodes[0];
  renderer.emit('clickNode', { node: superNode, event: { x: graphEl.clientWidth / 2, y: graphEl.clientHeight / 2 } });
  await sleep(420);
  renderer.refresh();
  await sleep(60);
  assert(cameraDelta(beforeSuperClickCamera, camera.getState()) < 1e-8,
    'drilling down from super-category keeps the camera stable',
    JSON.stringify({ before: beforeSuperClickCamera, after: camera.getState() }));
  const categoryNodeCount = visibleNodes().length;
  assert(mm.detailLevel && mm.detailLevel() === 'category',
    'clicking a super node reveals the category aggregation level',
    mm.detailLevel && mm.detailLevel());
  assert(categoryNodeCount > initialSuperNodeCount,
    'category level reveals more aggregate nodes than the super level',
    `${categoryNodeCount} vs ${initialSuperNodeCount}`);
  await assertAllVisibleLabelsForcedAcrossZoom('category', 'category level');

  nodes = visibleNodes();
  const beforeCategoryClickCamera = { ...camera.getState() };
  renderer.emit('clickNode', { node: nodes[0], event: { x: graphEl.clientWidth / 2, y: graphEl.clientHeight / 2 } });
  await sleep(420);
  renderer.refresh();
  await sleep(60);
  assert(cameraDelta(beforeCategoryClickCamera, camera.getState()) < 1e-8,
    'drilling down from category keeps the camera stable',
    JSON.stringify({ before: beforeCategoryClickCamera, after: camera.getState() }));
  assert(mm.detailLevel && mm.detailLevel() === 'sub_category',
    'clicking a category node reveals the sub-category aggregation level',
    mm.detailLevel && mm.detailLevel());

  const paperButton = document.querySelector('#mm-detail-controls button[data-level="paper"]');
  assert(Boolean(paperButton), 'paper detail level button exists');
  const beforePaperButtonCamera = { ...camera.getState() };
  paperButton && paperButton.click();
  await sleep(420);
  renderer.refresh();
  await sleep(60);
  assert(cameraDelta(beforePaperButtonCamera, camera.getState()) < 1e-8,
    'paper detail button keeps the camera stable',
    JSON.stringify({ before: beforePaperButtonCamera, after: camera.getState() }));
  assert(mm.detailLevel && mm.detailLevel() === 'paper',
    'paper button reveals paper nodes',
    mm.detailLevel && mm.detailLevel());
  const paperTransition = mm.metrics && mm.metrics().lastLevelTransition;
  assert(paperTransition && paperTransition.toLevel === 'paper',
    'paper drill-down records transition metrics',
    JSON.stringify(paperTransition));
  assert(paperTransition && paperTransition.maxScreenTravel <= paperTransition.maxAllowedScreenTravel + 1,
    'paper drill-down caps node travel to prevent explosive transitions',
    JSON.stringify(paperTransition));

  nodes = visibleNodes();
  edges = visibleEdges();
  assert(nodes.length > 20, 'visible node count is plausible', nodes.length);
  assert(edges.length > 20, 'visible edge count is plausible', edges.length);
  assertPaperNodeClearance('paper detail level');
  const paperRadiusBeforeZoom = mm.metrics && mm.metrics().nodeGraphRadius;
  const paperNodeBeforeZoom = nodes[0] && renderer.getNodeDisplayData(nodes[0]);
  const paperCameraBeforeZoom = { ...camera.getState() };
  camera.setState({ ratio: paperCameraBeforeZoom.ratio * 0.65 });
  await sleep(50);
  renderer.refresh();
  const paperRadiusAfterZoom = mm.metrics && mm.metrics().nodeGraphRadius;
  const paperNodeAfterZoom = nodes[0] && renderer.getNodeDisplayData(nodes[0]);
  assert(Math.abs(paperRadiusBeforeZoom - paperRadiusAfterZoom) < 1e-8,
    'paper node graph radius stays fixed while zooming',
    JSON.stringify({ paperRadiusBeforeZoom, paperRadiusAfterZoom }));
  assert(paperNodeBeforeZoom && paperNodeAfterZoom &&
    Math.abs(paperNodeBeforeZoom.size - paperNodeAfterZoom.size) < 1e-8,
    'paper node display size attribute stays fixed while zooming',
    JSON.stringify({
      before: paperNodeBeforeZoom && paperNodeBeforeZoom.size,
      after: paperNodeAfterZoom && paperNodeAfterZoom.size,
    }));
  camera.setState(paperCameraBeforeZoom);
  await sleep(50);
  renderer.refresh();

  setScheme('default');
  await sleep(90);
  renderer.refresh();
  await sleep(50);
  edges = visibleEdges();
  const defaultEdge = edges.length ? renderer.getEdgeDisplayData(edges[0]) : null;
  const defaultEdgeAlphaStats = edgeAlphaStats(edges);
  assert(!colorIsWhite(cssVar('--mm-edge-color')), 'default theme edge variable is not white', cssVar('--mm-edge-color'));
  assert(colorIsNeutralGrey(cssVar('--mm-edge-color')),
    'default theme edge variable is true neutral grey', cssVar('--mm-edge-color'));
  assert(colorIsNeutralGrey(cssVar('--mm-edge-highlighted')),
    'default highlighted edge variable is true neutral grey', cssVar('--mm-edge-highlighted'));
  assert(defaultEdge && !colorIsWhite(defaultEdge.color), 'default rendered edge is not white', defaultEdge && defaultEdge.color);
  assert(defaultEdge && colorIsNeutralGrey(defaultEdge.color),
    'default rendered edge is true neutral grey', defaultEdge && defaultEdge.color);
  assert(defaultEdgeAlphaStats.min >= 0.13,
    'default rendered edges have a visible opacity floor', JSON.stringify(defaultEdgeAlphaStats));
  assert(defaultEdgeAlphaStats.median >= 0.14,
    'default rendered edges have visible median opacity', JSON.stringify(defaultEdgeAlphaStats));
  assert(defaultEdge && defaultEdge.size <= 1.25, 'default rendered edge width is restrained', defaultEdge && defaultEdge.size);

  setScheme('slate');
  await sleep(90);
  renderer.refresh();
  await sleep(50);
  const slateEdge = edges.length ? renderer.getEdgeDisplayData(edges[0]) : null;
  const slateEdgeAlphaStats = edgeAlphaStats(edges);
  assert(!colorIsWhite(cssVar('--mm-edge-color')), 'slate theme edge variable is not pure white', cssVar('--mm-edge-color'));
  assert(colorIsNeutralGrey(cssVar('--mm-edge-color')),
    'slate theme edge variable is true neutral grey', cssVar('--mm-edge-color'));
  assert(colorIsNeutralGrey(cssVar('--mm-edge-highlighted')),
    'slate highlighted edge variable is true neutral grey', cssVar('--mm-edge-highlighted'));
  assert(slateEdge && !colorIsWhite(slateEdge.color), 'slate rendered edge is not pure white', slateEdge && slateEdge.color);
  assert(slateEdge && colorIsNeutralGrey(slateEdge.color),
    'slate rendered edge is true neutral grey', slateEdge && slateEdge.color);
  assert(slateEdgeAlphaStats.median <= 0.032,
    'slate rendered edges stay quiet at median opacity', JSON.stringify(slateEdgeAlphaStats));
  assert(slateEdgeAlphaStats.max <= 0.05,
    'slate rendered edges stay subdued at the high end', JSON.stringify(slateEdgeAlphaStats));

  setScheme('default');
  await sleep(90);
  renderer.refresh();
  await sleep(50);

  nodes = visibleNodes();
  const target = nodes[Math.floor(nodes.length / 2)];
  const other = nodes.find(id => id !== target);
  const otherBase = other ? graph.getNodeAttribute(other, 'baseColor') : null;
  renderer.emit('clickNode', { node: target, event: { x: graphEl.clientWidth / 2, y: graphEl.clientHeight / 2 } });
  await sleep(120);
  renderer.refresh();
  await sleep(60);

  const selected = renderer.getNodeDisplayData(target);
  const muted = other ? renderer.getNodeDisplayData(other) : null;
  const selectedRing = cssVar('--mm-selected-ring').toLowerCase();
  const mutedColors = [
    cssVar('--mm-node-muted').toLowerCase(),
    cssVar('--mm-node-muted-related').toLowerCase(),
  ];

  assert(selected && String(selected.labelColor).toLowerCase() === '#111111',
    'selected node label uses black text', selected && selected.labelColor);
  assert(selected && String(selected.labelOutlineColor).toLowerCase() === selectedRing,
    'selected node label outline uses the gold emphasis color',
    selected && `${selected.labelOutlineColor} vs ${selectedRing}`);
  assert(selected && selected.highlighted === true, 'selected node is marked for ring rendering');
  const focusLabelsCanvas = renderer.getCanvases && renderer.getCanvases().focusLabels;
  const targetAttrs = graph.getNodeAttributes(target);
  const targetPoint = renderer.graphToViewport({ x: targetAttrs.x, y: targetAttrs.y });
  assert(canvasHasDarkPixelNear(focusLabelsCanvas, targetPoint),
    'selected node label is redrawn on the final overlay above the emphasis disk',
    JSON.stringify({ hasCanvas: Boolean(focusLabelsCanvas), targetPoint }));
  assert(muted && String(muted.color).toLowerCase() !== String(otherBase).toLowerCase(),
    'non-selected node loses its category color while focus is active',
    muted && `${muted.color} vs ${otherBase}`);
  assert(muted && mutedColors.includes(String(muted.color).toLowerCase()),
    'non-selected node uses one of the muted grey colors',
    muted && `${muted.color} not in ${mutedColors.join(', ')}`);
  assert(hashParams().get('paper') === target,
    'clicking a paper updates the shareable mind-map URL',
    window.location.hash);

  renderer.emit('clickStage', {});
  await sleep(80);
  assert(!hashParams().get('paper') && !hashParams().get('node'),
    'clearing the selected paper removes stale paper URL state',
    window.location.hash);

  window.location.hash = `paper=${encodeURIComponent(target)}`;
  await sleep(420);
  renderer.refresh();
  await sleep(80);
  assert(mm.detailLevel && mm.detailLevel() === 'paper',
    'paper hash switches to the paper detail level',
    mm.detailLevel && mm.detailLevel());
  assert(hashParams().get('paper') === target,
    'paper hash remains canonical after focusing',
    window.location.hash);
  assert(camera.getState().ratio >= 0.24 && camera.getState().ratio <= 0.42,
    'paper hash uses a moderate zoom level',
    camera.getState().ratio);
  assertNodeCenteredInUsableCanvas(target, 'paper hash focus with menu shown');

  document.getElementById('mm-panel-header').click();
  await sleep(600);
  renderer.refresh();
  await sleep(80);
  assertNodeCenteredInUsableCanvas(target, 'paper hash focus after hiding the menu');

  camera.setState({ x: 0, y: 0, ratio: 5 });
  await sleep(30);
  document.getElementById('mm-fit-btn').click();
  await sleep(420);
  renderer.refresh();
  await sleep(60);
  const buttonFitState = camera.getState();
  const buttonAllDetailFitted = allDetailViewportBBox();
  assert(buttonFitState.ratio <= 1.15, 'Fit View button returns the camera to fitted zoom', buttonFitState.ratio);
  assertFittedBBox(buttonAllDetailFitted, 'single-click Fit View across all detail levels');

  camera.setState({ x: 0, y: 0, ratio: 5 });
  await sleep(30);
  mm.fit(0);
  await sleep(120);
  renderer.refresh();
  await sleep(60);
  const fitted = viewportBBox();
  const allDetailFitted = allDetailViewportBBox();
  assertFittedBBox(fitted, 'fit keeps current visible detail level inside viewport');
  assertFittedBBox(allDetailFitted, 'fit keeps every detail level inside viewport');

  return {
    failures,
    metrics: {
      nodes: nodes.length,
      edges: edges.length,
      defaultEdge,
      defaultEdgeAlphaStats,
      slateEdge,
      slateEdgeAlphaStats,
      fitted,
      allDetailFitted,
      buttonAllDetailFitted,
      buttonFitState,
      selected: {
        labelColor: selected && selected.labelColor,
        labelOutlineColor: selected && selected.labelOutlineColor,
        highlighted: selected && selected.highlighted,
      },
      muted: {
        color: muted && muted.color,
        baseColor: otherBase,
      },
      hierarchy: {
        initialLevel,
        initialSuperNodeCount,
        categoryNodeCount,
      },
    },
  };
})()
"""


@dataclass
class ChromeSession:
    process: subprocess.Popen[bytes]
    user_data_dir: str
    port: int


class CdpClient:
    def __init__(self, websocket_url: str) -> None:
        parsed = urlparse(websocket_url)
        if parsed.scheme != "ws":
            raise ValueError(f"Unsupported WebSocket URL: {websocket_url}")

        host = parsed.hostname or "127.0.0.1"
        port = parsed.port or 80
        path = parsed.path
        if parsed.query:
            path += f"?{parsed.query}"

        self.sock = socket.create_connection((host, port), timeout=10)
        self.sock.settimeout(10)
        key = base64.b64encode(secrets.token_bytes(16)).decode("ascii")
        request = (
            f"GET {path} HTTP/1.1\r\n"
            f"Host: {host}:{port}\r\n"
            "Upgrade: websocket\r\n"
            "Connection: Upgrade\r\n"
            f"Sec-WebSocket-Key: {key}\r\n"
            "Sec-WebSocket-Version: 13\r\n"
            "\r\n"
        )
        self.sock.sendall(request.encode("ascii"))
        response = self._read_http_response()
        if b" 101 " not in response.split(b"\r\n", 1)[0]:
            raise RuntimeError(f"WebSocket handshake failed: {response[:200]!r}")
        self.next_id = 0

    def close(self) -> None:
        try:
            self.sock.close()
        except OSError:
            pass

    def call(self, method: str, params: dict[str, Any] | None = None, timeout: float = 10) -> dict[str, Any]:
        self.next_id += 1
        message_id = self.next_id
        payload = {"id": message_id, "method": method}
        if params is not None:
            payload["params"] = params
        self._send_json(payload)

        deadline = time.time() + timeout
        while time.time() < deadline:
            message = self._recv_json(deadline - time.time())
            if message.get("id") != message_id:
                continue
            if "error" in message:
                raise RuntimeError(f"CDP {method} failed: {message['error']}")
            return message.get("result", {})
        raise TimeoutError(f"Timed out waiting for CDP method {method}")

    def evaluate(self, expression: str, timeout: float = 10) -> Any:
        result = self.call(
            "Runtime.evaluate",
            {
                "expression": expression,
                "awaitPromise": True,
                "returnByValue": True,
                "userGesture": True,
            },
            timeout=timeout,
        )
        if "exceptionDetails" in result:
            text = result["exceptionDetails"].get("text", "Runtime exception")
            raise RuntimeError(text)
        value = result.get("result", {})
        if "value" in value:
            return value["value"]
        return None

    def _read_http_response(self) -> bytes:
        chunks: list[bytes] = []
        data = b""
        while b"\r\n\r\n" not in data:
            chunk = self.sock.recv(4096)
            if not chunk:
                break
            chunks.append(chunk)
            data = b"".join(chunks)
        return data

    def _send_json(self, payload: dict[str, Any]) -> None:
        data = json.dumps(payload, separators=(",", ":")).encode("utf-8")
        mask = secrets.token_bytes(4)
        header = bytearray([0x81])
        length = len(data)
        if length < 126:
            header.append(0x80 | length)
        elif length < 65536:
            header.append(0x80 | 126)
            header.extend(struct.pack("!H", length))
        else:
            header.append(0x80 | 127)
            header.extend(struct.pack("!Q", length))
        masked = bytes(byte ^ mask[i % 4] for i, byte in enumerate(data))
        self.sock.sendall(bytes(header) + mask + masked)

    def _recv_json(self, timeout: float) -> dict[str, Any]:
        self.sock.settimeout(max(timeout, 0.1))
        while True:
            first = self._recv_exact(2)
            opcode = first[0] & 0x0F
            masked = bool(first[1] & 0x80)
            length = first[1] & 0x7F
            if length == 126:
                length = struct.unpack("!H", self._recv_exact(2))[0]
            elif length == 127:
                length = struct.unpack("!Q", self._recv_exact(8))[0]
            mask = self._recv_exact(4) if masked else b""
            payload = self._recv_exact(length) if length else b""
            if masked:
                payload = bytes(byte ^ mask[i % 4] for i, byte in enumerate(payload))
            if opcode == 0x8:
                raise RuntimeError("Chrome closed the DevTools WebSocket")
            if opcode == 0x9:
                self._send_pong(payload)
                continue
            if opcode == 0x1:
                return json.loads(payload.decode("utf-8"))

    def _send_pong(self, payload: bytes) -> None:
        mask = secrets.token_bytes(4)
        header = bytes([0x8A, 0x80 | len(payload)])
        masked = bytes(byte ^ mask[i % 4] for i, byte in enumerate(payload))
        self.sock.sendall(header + mask + masked)

    def _recv_exact(self, length: int) -> bytes:
        chunks: list[bytes] = []
        remaining = length
        while remaining:
            chunk = self.sock.recv(remaining)
            if not chunk:
                raise RuntimeError("Socket closed while reading WebSocket frame")
            chunks.append(chunk)
            remaining -= len(chunk)
        return b"".join(chunks)


def find_chrome(explicit: str | None) -> str:
    candidates = [explicit] if explicit else []
    candidates.extend(["google-chrome-stable", "google-chrome", "chromium", "chromium-browser"])
    for candidate in candidates:
        if not candidate:
            continue
        path = shutil.which(candidate) if os.path.basename(candidate) == candidate else candidate
        if path and os.path.exists(path):
            return path
    raise RuntimeError("Could not find Chrome. Pass --chrome /path/to/chrome.")


def free_port() -> int:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind(("127.0.0.1", 0))
        return int(sock.getsockname()[1])


def launch_chrome(chrome: str) -> ChromeSession:
    port = free_port()
    user_data_dir = tempfile.mkdtemp(prefix="kb-mind-map-chrome-")
    command = [
        chrome,
        "--headless=new",
        "--disable-gpu",
        "--disable-dev-shm-usage",
        "--disable-extensions",
        "--no-first-run",
        "--no-default-browser-check",
        "--enable-unsafe-swiftshader",
        f"--remote-debugging-port={port}",
        f"--user-data-dir={user_data_dir}",
        "about:blank",
    ]
    process = subprocess.Popen(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    session = ChromeSession(process=process, user_data_dir=user_data_dir, port=port)
    wait_for_json(session, "/json/version")
    return session


def wait_for_json(session: ChromeSession, path: str, timeout: float = 10) -> Any:
    url = f"http://127.0.0.1:{session.port}{path}"
    deadline = time.time() + timeout
    last_error: Exception | None = None
    while time.time() < deadline:
        if session.process.poll() is not None:
            raise RuntimeError("Chrome exited before DevTools became available")
        try:
            with urllib.request.urlopen(url, timeout=1) as response:
                return json.loads(response.read().decode("utf-8"))
        except Exception as exc:  # noqa: BLE001 - retry startup races
            last_error = exc
            time.sleep(0.1)
    raise TimeoutError(f"Timed out waiting for {url}: {last_error}")


def get_tab_websocket(session: ChromeSession, url: str) -> str:
    create_url = f"http://127.0.0.1:{session.port}/json/new?{quote('about:blank', safe='')}"
    request = urllib.request.Request(create_url, method="PUT")
    try:
        with urllib.request.urlopen(request, timeout=2) as response:
            tab = json.loads(response.read().decode("utf-8"))
            return str(tab["webSocketDebuggerUrl"])
    except Exception:
        tabs = wait_for_json(session, "/json/list")
        if not tabs:
            raise RuntimeError(f"Could not create a Chrome tab for {url}")
        return str(tabs[0]["webSocketDebuggerUrl"])


def wait_for_page_ready(client: CdpClient, timeout: float = 35) -> None:
    expression = """
    Boolean(
      window._mindMap &&
      window._mindMap.renderer &&
      window._mindMap.renderer() &&
      window._mindMap.graph &&
      window._mindMap.graph() &&
      (!document.getElementById('mm-loading') || document.getElementById('mm-loading').style.display === 'none')
    )
    """
    deadline = time.time() + timeout
    last_error: Exception | None = None
    while time.time() < deadline:
        try:
            if client.evaluate(expression, timeout=2):
                return
        except Exception as exc:  # noqa: BLE001 - page may still be navigating
            last_error = exc
        time.sleep(0.25)
    raise TimeoutError(f"Mind map did not become ready: {last_error}")


def run_viewport(client: CdpClient, url: str, width: int, height: int, mobile: bool) -> dict[str, Any]:
    client.call("Page.enable")
    client.call("Runtime.enable")
    client.call(
        "Emulation.setDeviceMetricsOverride",
        {
            "width": width,
            "height": height,
            "deviceScaleFactor": 1,
            "mobile": mobile,
        },
    )
    base_url, sep, hash_fragment = url.partition("#")
    query_sep = "&" if "?" in base_url else "?"
    nav_url = f"{base_url}{query_sep}_verify={width}x{height}_{int(mobile)}_{time.time_ns()}"
    if sep:
        nav_url = f"{nav_url}#{hash_fragment}"
    client.call("Page.navigate", {"url": nav_url})
    wait_for_page_ready(client)
    result = client.evaluate(JS_CHECKS, timeout=30)
    failures = result.get("failures", []) if isinstance(result, dict) else ["JS checks returned no result"]
    if failures:
        formatted = "\n".join(f"  - {failure}" for failure in failures)
        raise AssertionError(f"{width}x{height} failed:\n{formatted}")
    return result.get("metrics", {})


def shutdown_chrome(session: ChromeSession | None) -> None:
    if not session:
        return
    try:
        session.process.terminate()
        session.process.wait(timeout=3)
    except Exception:
        session.process.kill()
    shutil.rmtree(session.user_data_dir, ignore_errors=True)


def parse_viewport(value: str) -> tuple[int, int, bool]:
    parts = value.split(":")
    size = parts[0]
    width_s, height_s = size.lower().split("x", 1)
    mobile = len(parts) > 1 and parts[1].lower() == "mobile"
    return int(width_s), int(height_s), mobile


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify the mind-map page in headless Chrome")
    parser.add_argument("--url", required=True, help="Served MkDocs mind-map URL")
    parser.add_argument("--chrome", help="Path to Chrome/Chromium")
    parser.add_argument(
        "--viewport",
        action="append",
        default=["1366x900", "390x844:mobile"],
        help="Viewport to test, e.g. 1366x900 or 390x844:mobile. May be repeated.",
    )
    args = parser.parse_args()

    chrome = find_chrome(args.chrome)
    session: ChromeSession | None = None
    client: CdpClient | None = None
    try:
        session = launch_chrome(chrome)
        client = CdpClient(get_tab_websocket(session, args.url))
        all_metrics = {}
        for viewport in args.viewport:
            width, height, mobile = parse_viewport(viewport)
            metrics = run_viewport(client, args.url, width, height, mobile)
            all_metrics[viewport] = metrics
            fitted = metrics.get("fitted", {})
            print(
                f"PASS {viewport}: "
                f"{metrics.get('nodes')} nodes, {metrics.get('edges')} edges, "
                f"fit bbox x=[{fitted.get('minX'):.1f}, {fitted.get('maxX'):.1f}] "
                f"y=[{fitted.get('minY'):.1f}, {fitted.get('maxY'):.1f}]"
            )
        return 0
    finally:
        if client:
            client.close()
        shutdown_chrome(session)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # noqa: BLE001
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
