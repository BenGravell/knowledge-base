/* browser/rendering.js - Sigma rendering helpers for the paper map. */

'use strict';

(function () {
  const WCAG_NORMAL_TEXT_CONTRAST = 4.5;
  const NODE_LABEL_LIGHT = '#FFFFFF';
  const NODE_LABEL_DARK = '#000000';
  const VISIBILITY_BRANCH_PALETTE_CSS_PREFIX = '--kb-map-node-color-';
  const VISIBILITY_BRANCH_PALETTE_SIZE = 12;
  const VISIBILITY_BRANCH_PALETTE_FALLBACKS = {
    light: [
      '#005AB5',
      '#A52A00',
      '#00735C',
      '#8F3B76',
      '#8A5A00',
      '#006A8E',
      '#5E3C99',
      '#6B4E16',
      '#005F73',
      '#9B2226',
      '#3A6B15',
      '#7B3294',
    ],
    dark: [
      '#6BB6FF',
      '#FF9B5C',
      '#5FE0B5',
      '#F39BD4',
      '#F6C85F',
      '#8EDAEF',
      '#C6A4FF',
      '#D6B46D',
      '#7CD9D0',
      '#FF8A94',
      '#A7D96D',
      '#D6A0F7',
    ],
  };

  const LABEL_RENDERED_SIZE_THRESHOLD = 3;
  const LABEL_DENSITY = 0.08;
  const LABEL_GRID_CELL_SIZE = 112;
  const NODE_LABEL_FONT_SIZE = 11;
  const NODE_LABEL_FONT_SIZE_MIN = 9;
  const NODE_LABEL_FONT_SIZE_MAX = 24;
  const NODE_LABEL_DIAMETER_EXPONENT = 0.34;
  const NODE_LABEL_LINE_HEIGHT_RATIO = 1.1;
  const NODE_LABEL_MAX_LINE_CHARS = 15;
  const NODE_LABEL_MAX_LINES = 4;
  const NODE_LABEL_ZOOM_REFERENCE_RATIO = 1;
  const NODE_LABEL_ZOOM_EXPONENT = 0.22;
  const NODE_LABEL_ZOOM_SCALE_MIN = 0.68;
  const NODE_LABEL_ZOOM_SCALE_MAX = 1.55;
  const NODE_BORDER_WIDTH_RATIO = 0.08;
  const BORDERED_NODE_TYPE = 'bordered';
  const SELECTED_NODE_RADIUS_SCALE = 1;

  function createMapRendering(deps = {}) {
    const clamp = deps.clamp || ((value, min, max) => Math.max(min, Math.min(value, max)));
    const viewState = deps.viewState;
    let theme = readTheme();
    let visibilityPaletteCache = null;
    let graphToViewportRatioCache = null;
    let topLabelContext = null;

    function graph() {
      return typeof deps.getGraph === 'function' ? deps.getGraph() : null;
    }

    function renderer() {
      return typeof deps.getRenderer === 'function' ? deps.getRenderer() : null;
    }

    function hexToRgb(hexColor) {
      const color = normalizedCssColor(hexColor);
      let m;
      if ((m = String(color || '').match(/^#([0-9a-f]{3})$/i))) {
        const hex = m[1].split('').map(ch => ch + ch).join('');
        return {
          r: parseInt(hex.slice(0, 2), 16),
          g: parseInt(hex.slice(2, 4), 16),
          b: parseInt(hex.slice(4, 6), 16),
        };
      }
      if ((m = String(color || '').match(/^#([0-9a-f]{6})$/i))) {
        const hex = m[1];
        return {
          r: parseInt(hex.slice(0, 2), 16),
          g: parseInt(hex.slice(2, 4), 16),
          b: parseInt(hex.slice(4, 6), 16),
        };
      }
      return null;
    }

    function linearizedSrgb(channel) {
      const c = clamp(channel, 0, 255) / 255;
      return c <= 0.03928
        ? c / 12.92
        : Math.pow((c + 0.055) / 1.055, 2.4);
    }

    function relativeLuminance(color) {
      const rgb = hexToRgb(color);
      if (!rgb) return null;

      return 0.2126 * linearizedSrgb(rgb.r) +
        0.7152 * linearizedSrgb(rgb.g) +
        0.0722 * linearizedSrgb(rgb.b);
    }

    function contrastRatio(a, b) {
      const la = relativeLuminance(a);
      const lb = relativeLuminance(b);
      if (la === null || lb === null) return 1;

      const lighter = Math.max(la, lb);
      const darker = Math.min(la, lb);
      return (lighter + 0.05) / (darker + 0.05);
    }

    function accessibleNodeLabelColor(nodeColorValue) {
      const lightContrast = contrastRatio(nodeColorValue, NODE_LABEL_LIGHT);
      const darkContrast = contrastRatio(nodeColorValue, NODE_LABEL_DARK);
      const best = lightContrast >= darkContrast ? NODE_LABEL_LIGHT : NODE_LABEL_DARK;
      const bestContrast = Math.max(lightContrast, darkContrast);

      if (bestContrast >= WCAG_NORMAL_TEXT_CONTRAST) return best;
      return theme && theme.colorScheme === 'dark' ? NODE_LABEL_LIGHT : NODE_LABEL_DARK;
    }

    function currentColorScheme() {
      const explicit = (
        document.body && document.body.getAttribute('data-md-color-scheme')
      ) || document.documentElement.getAttribute('data-md-color-scheme');
      if (explicit === 'slate') return 'dark';
      if (explicit === 'default') return 'light';
      if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
        return 'dark';
      }
      return 'light';
    }

    function currentVisibilityPalette() {
      const colorScheme = currentColorScheme();
      if (visibilityPaletteCache && visibilityPaletteCache.colorScheme === colorScheme) {
        return visibilityPaletteCache.palette;
      }

      const cssPalette = cssVisibilityPalette();
      const palette = cssPalette.length >= VISIBILITY_BRANCH_PALETTE_SIZE
        ? cssPalette
        : VISIBILITY_BRANCH_PALETTE_FALLBACKS[colorScheme] ||
        VISIBILITY_BRANCH_PALETTE_FALLBACKS.light;

      visibilityPaletteCache = { colorScheme, palette };
      return palette;
    }

    function cssVisibilityPalette() {
      const styleSources = [];
      if (document.body) styleSources.push(getComputedStyle(document.body));
      styleSources.push(getComputedStyle(document.documentElement));

      const palette = [];
      for (let index = 1; index <= VISIBILITY_BRANCH_PALETTE_SIZE; index += 1) {
        const property = `${VISIBILITY_BRANCH_PALETTE_CSS_PREFIX}${index}`;
        const raw = styleSources
          .map(styles => styles.getPropertyValue(property).trim())
          .find(Boolean);
        const color = normalizedCssColor(raw);
        if (color) palette.push(color);
      }

      return palette;
    }

    function readTheme() {
      const cs = getComputedStyle(document.body);
      const v = name => cs.getPropertyValue(name).trim();
      const colorScheme = currentColorScheme();
      return {
        colorScheme,
        nodeMuted: normalizedCssColor(v('--mm-node-muted')) || '#8A949E',
        nodeMutedRelated: normalizedCssColor(v('--mm-node-muted-related')) || '#737D88',
        nodeGhost: normalizedCssColor(v('--mm-node-ghost')) ||
          (colorScheme === 'dark' ? '#222A33' : '#EDF1F5'),
        nodeGhostBorder: normalizedCssColor(v('--mm-node-ghost-border')) ||
          (colorScheme === 'dark' ? '#56616D' : '#B8C2CC'),
        nodeBorder: normalizedCssColor(v('--mm-node-border')) ||
          (colorScheme === 'dark' ? '#242B35' : '#E1E7EE'),
        selectedRing: normalizedCssColor(v('--mm-selected-ring')) || '#D9A316',
      };
    }

    function refreshTheme() {
      visibilityPaletteCache = null;
      theme = readTheme();
      return theme;
    }

    function invalidateVisibilityPalette() {
      visibilityPaletteCache = null;
    }

    function normalizedCssColor(color) {
      const c = String(color || '').trim();
      return c && !c.startsWith('color-mix(') && !c.startsWith('var(') ? c : null;
    }

    function colorWithAlpha(color, alpha) {
      const c = normalizedCssColor(color) || '#333333';
      const a = Math.max(0, Math.min(alpha, 1));
      let m;

      if ((m = c.match(/^#([0-9a-f]{3})$/i))) {
        const hex = m[1].split('').map(ch => ch + ch).join('');
        return hexToRgba(hex, a);
      }
      if ((m = c.match(/^#([0-9a-f]{6})$/i))) {
        return hexToRgba(m[1], a);
      }
      if ((m = c.match(/^rgba?\(([^)]+)\)$/i))) {
        const parts = m[1].split(',').map(p => p.trim());
        if (parts.length >= 3) return `rgba(${parts[0]},${parts[1]},${parts[2]},${a})`;
      }

      return a >= 1 ? c : `rgba(51,51,51,${a})`;
    }

    function hexToRgba(hex, alpha) {
      const r = parseInt(hex.slice(0, 2), 16);
      const g = parseInt(hex.slice(2, 4), 16);
      const b = parseInt(hex.slice(4, 6), 16);
      return `rgba(${r},${g},${b},${alpha})`;
    }

    function currentNodeRadius() {
      return typeof deps.currentNodeRadius === 'function'
        ? deps.currentNodeRadius()
        : 12;
    }

    function currentCameraRatio() {
      const r = renderer();
      if (!r || typeof r.getCamera !== 'function') {
        return NODE_LABEL_ZOOM_REFERENCE_RATIO;
      }

      const camera = r.getCamera();
      const state = camera && typeof camera.getState === 'function'
        ? camera.getState()
        : null;
      const ratio = state && Number(state.ratio);
      return Number.isFinite(ratio) && ratio > 0
        ? ratio
        : NODE_LABEL_ZOOM_REFERENCE_RATIO;
    }

    function graphToViewportRatioForCurrentCamera() {
      const r = renderer();
      if (!r || typeof r.graphToViewport !== 'function') return null;

      const camera = typeof r.getCamera === 'function'
        ? r.getCamera()
        : null;
      const cameraState = camera && typeof camera.getState === 'function'
        ? camera.getState()
        : null;
      const dims = typeof r.getDimensions === 'function'
        ? r.getDimensions()
        : { width: 0, height: 0 };
      const graphDims = typeof r.getGraphDimensions === 'function'
        ? r.getGraphDimensions()
        : { width: 0, height: 0 };
      const padding = typeof r.getSetting === 'function'
        ? r.getSetting('stagePadding')
        : 0;
      const ratio = cameraState && Number(cameraState.ratio);
      const key = [
        Number.isFinite(ratio) ? ratio : NODE_LABEL_ZOOM_REFERENCE_RATIO,
        dims.width || 0,
        dims.height || 0,
        graphDims.width || 0,
        graphDims.height || 0,
        padding || 0,
      ].join(':');

      if (graphToViewportRatioCache && graphToViewportRatioCache.key === key) {
        return graphToViewportRatioCache.value;
      }

      const options = cameraState ? { cameraState, padding } : { padding };
      const a = r.graphToViewport({ x: 0, y: 0 }, options);
      const b = r.graphToViewport({ x: 1, y: 1 }, options);
      const value = Math.sqrt((a.x - b.x) * (a.x - b.x) + (a.y - b.y) * (a.y - b.y)) / Math.SQRT2;

      graphToViewportRatioCache = {
        key,
        value: Number.isFinite(value) && value > 0 ? value : null,
      };
      return graphToViewportRatioCache.value;
    }

    function invalidateGraphToViewportRatio() {
      graphToViewportRatioCache = null;
    }

    function nodeSizeWithMinimumScreenRadius(size) {
      const baseSize = Number.isFinite(size) && size > 0 ? size : currentNodeRadius();
      const graphToViewportRatio = graphToViewportRatioForCurrentCamera();
      if (!Number.isFinite(graphToViewportRatio) || graphToViewportRatio <= 0) return baseSize;

      const screenRadius = softMinimumScreenRadius(
        baseSize * graphToViewportRatio,
        minimumNodeScreenRadius()
      );
      return screenRadius / graphToViewportRatio;
    }

    function softMinimumScreenRadius(radius, minimum) {
      if (!Number.isFinite(radius) || radius <= 0) return minimum;

      const blend = minimum * (deps.minNodeScreenRadiusBlendRatio || 0.5);
      if (!Number.isFinite(blend) || blend <= 0) return Math.max(radius, minimum);

      const distance = Math.abs(radius - minimum);
      if (distance >= blend) return Math.max(radius, minimum);

      return Math.max(radius, minimum) + ((blend - distance) * (blend - distance)) / (blend * 4);
    }

    function minimumNodeScreenRadius() {
      return deps.mobileViewport && deps.mobileViewport()
        ? deps.mobileMinNodeScreenRadius
        : deps.minNodeScreenRadius;
    }

    function currentNodeLabelZoomScale() {
      return nodeLabelZoomScaleForRatio(currentCameraRatio());
    }

    function nodeLabelZoomScaleForRatio(ratio) {
      const safeRatio = Number.isFinite(ratio) && ratio > 0
        ? ratio
        : NODE_LABEL_ZOOM_REFERENCE_RATIO;
      return clamp(
        Math.pow(NODE_LABEL_ZOOM_REFERENCE_RATIO / safeRatio, NODE_LABEL_ZOOM_EXPONENT),
        NODE_LABEL_ZOOM_SCALE_MIN,
        NODE_LABEL_ZOOM_SCALE_MAX
      );
    }

    function currentNodeLabelMetrics(data, zoomScale = currentNodeLabelZoomScale()) {
      const baseFontSize = Number.isFinite(data.labelFontSize)
        ? data.labelFontSize
        : NODE_LABEL_FONT_SIZE;
      const baseLineHeight = Number.isFinite(data.labelLineHeight)
        ? data.labelLineHeight
        : baseFontSize * NODE_LABEL_LINE_HEIGHT_RATIO;
      const fontSize = baseFontSize * zoomScale;

      return {
        fontSize,
        lineHeight: baseLineHeight * zoomScale,
        outlineWidth: clamp(fontSize * 0.18, 1.25, 3),
      };
    }

    function median(values) {
      const sorted = values
        .filter(value => Number.isFinite(value))
        .sort((a, b) => a - b);
      if (!sorted.length) return null;

      const mid = Math.floor(sorted.length / 2);
      return sorted.length % 2
        ? sorted[mid]
        : (sorted[mid - 1] + sorted[mid]) / 2;
    }

    function labelFontSizeForDiskDiameter(diameter) {
      const referenceDiameter = deps.paperNodeRadiusTarget * 2;
      const ratio = Math.max(Number(diameter) || referenceDiameter, 1) / referenceDiameter;
      return clamp(
        NODE_LABEL_FONT_SIZE * Math.pow(ratio, NODE_LABEL_DIAMETER_EXPONENT),
        NODE_LABEL_FONT_SIZE_MIN,
        NODE_LABEL_FONT_SIZE_MAX
      );
    }

    function precomputeNodeLabelMetrics(nodeSpecs) {
      const diametersByLevel = new Map();

      nodeSpecs.forEach(spec => {
        const level = spec.detailLevel || 'paper';
        const radius = Number.isFinite(spec.baseSize) ? spec.baseSize : deps.paperNodeRadiusTarget;
        if (!diametersByLevel.has(level)) diametersByLevel.set(level, []);
        diametersByLevel.get(level).push(radius * 2);
      });

      const metricsByLevel = new Map();
      deps.detailLevels.forEach(level => {
        const diameter = median(diametersByLevel.get(level) || []) || (deps.paperNodeRadiusTarget * 2);
        const fontSize = Math.round(labelFontSizeForDiskDiameter(diameter) * 10) / 10;
        metricsByLevel.set(level, {
          fontSize,
          lineHeight: Math.round(fontSize * NODE_LABEL_LINE_HEIGHT_RATIO * 10) / 10,
          sourceDiskDiameter: Math.round(diameter * 10) / 10,
        });
      });

      return metricsByLevel;
    }

    function nodeDisplaySize(attrs) {
      if (attrs.kind === 'aggregate') {
        return Number.isFinite(attrs.staticSize)
          ? attrs.staticSize
          : deps.aggregateNodeSize(attrs.count, attrs.detailLevel);
      }
      return currentNodeRadius();
    }

    function wrapLabelLine(line, maxChars) {
      const words = String(line || '').trim().split(/\s+/).filter(Boolean);
      const lines = [];
      let current = '';

      words.forEach(word => {
        if (!current) {
          current = word;
        } else if ((current.length + 1 + word.length) <= maxChars) {
          current += ` ${word}`;
        } else {
          lines.push(current);
          current = word;
        }
      });

      if (current) lines.push(current);
      return lines.length ? lines : [''];
    }

    function limitLabelLines(lines, maxLines = NODE_LABEL_MAX_LINES) {
      if (lines.length <= maxLines) return lines;

      const limited = lines.slice(0, maxLines);
      const last = limited[limited.length - 1];
      limited[limited.length - 1] = last.length > NODE_LABEL_MAX_LINE_CHARS - 1
        ? `${last.slice(0, Math.max(1, NODE_LABEL_MAX_LINE_CHARS - 1))}...`
        : `${last}...`;
      return limited;
    }

    function formatLabel(label) {
      const text = String(label || '').trim();
      const explicitLines = text.split(/\n+/).map(line => line.trim()).filter(Boolean);
      let suffixLine = null;
      let base = text;

      if (explicitLines.length > 1 && /^\d+$/.test(explicitLines[explicitLines.length - 1])) {
        suffixLine = explicitLines.pop();
        base = explicitLines.join(' ');
      } else {
        const m = text.match(/^(.+?)\s+(\d{4})$/);
        if (m) {
          base = m[1];
          suffixLine = m[2];
        }
      }

      if (!suffixLine) return limitLabelLines(wrapLabelLine(base, NODE_LABEL_MAX_LINE_CHARS)).join('\n');

      const bodyLines = wrapLabelLine(base, NODE_LABEL_MAX_LINE_CHARS);
      const limitedBody = limitLabelLines(bodyLines, NODE_LABEL_MAX_LINES - 1);
      return limitedBody.concat(suffixLine).join('\n');
    }

    function nodeReducer(node, attrs) {
      if (!deps.nodeVisible(node)) {
        if (deps.nodeGhostVisible(node)) {
          const size = nodeSizeWithMinimumScreenRadius(nodeDisplaySize(attrs)) * 0.72;
          return {
            ...attrs,
            label: '',
            size,
            color: theme.nodeGhost,
            borderColor: theme.nodeGhost,
            labelColor: theme.nodeGhostBorder,
            labelOutlineColor: theme.nodeGhost,
            highlighted: false,
            forceLabel: false,
            ghosted: true,
            zIndex: Math.max(0, deps.detailLevelZIndex(attrs.detailLevel) - 8),
          };
        }

        return { ...attrs, hidden: true };
      }

      const size = nodeSizeWithMinimumScreenRadius(nodeDisplaySize(attrs));
      const baseZIndex = deps.detailLevelZIndex(attrs.detailLevel);
      const highlighted = viewState.focus.nodes.has(node);
      const primaryFocus = highlighted && (
        node === viewState.pinnedNode ||
        node === viewState.hoveredNode
      );
      const muted = viewState.focus.active && viewState.focus.mode !== 'hover' && !primaryFocus;
      const focusLabel = node === viewState.pinnedNode || node === viewState.hoveredNode;
      const forceLabel = focusLabel;
      const label = (viewState.showNodeLabels || focusLabel) ? attrs.label : '';

      if (muted) {
        const mutedColor = highlighted ? theme.nodeMutedRelated : theme.nodeMuted;
        return {
          ...attrs,
          label,
          size,
          color: mutedColor,
          borderColor: theme.nodeBorder,
          labelColor: accessibleNodeLabelColor(mutedColor),
          labelOutlineColor: colorWithAlpha(mutedColor, 0.55),
          forceLabel,
          zIndex: baseZIndex + (highlighted ? 20 : 0),
        };
      }

      if (primaryFocus) {
        return {
          ...attrs,
          label,
          size: size * SELECTED_NODE_RADIUS_SCALE,
          color: attrs.baseColor,
          borderColor: theme.nodeBorder,
          labelColor: accessibleNodeLabelColor(attrs.baseColor),
          labelOutlineColor: theme.selectedRing,
          ringColor: theme.selectedRing,
          highlighted: true,
          forceLabel,
          zIndex: baseZIndex + 40,
        };
      }

      return {
        ...attrs,
        label,
        size,
        color: attrs.baseColor,
        borderColor: theme.nodeBorder,
        labelColor: accessibleNodeLabelColor(attrs.baseColor),
        labelOutlineColor: attrs.baseColor,
        highlighted: false,
        forceLabel,
        zIndex: baseZIndex,
      };
    }

    function drawNodeHover(context, data) {
      if (data.ghosted) return;

      const ringColor = data.ringColor || theme.selectedRing;
      const radius = Math.max(data.size + 3.5, 6);

      context.save();
      context.beginPath();
      context.arc(data.x, data.y, radius, 0, Math.PI * 2);
      context.lineWidth = Math.max(2, Math.min(3.25, data.size * 0.55));
      context.strokeStyle = ringColor;
      context.shadowColor = colorWithAlpha(ringColor, 0.32);
      context.shadowBlur = 5;
      context.stroke();
      context.restore();
    }

    function drawNodeLabel(context, data) {
      if (!data.label) return;

      const lines = String(data.label).split('\n');
      const { fontSize, lineHeight, outlineWidth } = currentNodeLabelMetrics(data, data.labelZoomScale);
      const startY = data.y - ((lines.length - 1) * lineHeight) / 2;

      context.save();
      context.font = `650 ${fontSize}px "Atkinson Hyperlegible Next", "Segoe UI", sans-serif`;
      context.textAlign = 'center';
      context.textBaseline = 'middle';
      context.lineJoin = 'round';
      context.miterLimit = 2;
      context.lineWidth = outlineWidth;
      context.strokeStyle = data.labelOutlineColor || data.color || '#000000';
      context.fillStyle = data.labelColor || '#ffffff';

      lines.forEach((line, i) => {
        const y = startY + i * lineHeight;
        context.strokeText(line, data.x, y);
        context.fillText(line, data.x, y);
      });

      context.restore();
    }

    function drawNodeLabelNoop() {
      // Sigma still runs its label-grid selection; the top overlay does the draw.
    }

    function drawGhostNodeDashedBorder(context, data) {
      const lineWidth = Math.max(1, data.size * NODE_BORDER_WIDTH_RATIO);
      const radius = Math.max(1, data.size - lineWidth / 2);

      context.save();
      context.beginPath();
      context.arc(data.x, data.y, radius, 0, Math.PI * 2);
      context.setLineDash([Math.max(2, lineWidth * 2.4), Math.max(2, lineWidth * 1.7)]);
      context.lineWidth = lineWidth;
      context.strokeStyle = theme.nodeGhostBorder;
      context.globalAlpha = theme.colorScheme === 'dark' ? 0.58 : 0.72;
      context.stroke();
      context.restore();
    }

    function borderedNodeProgramSupported() {
      return Boolean(
        window.Sigma &&
        window.Sigma.rendering &&
        typeof window.Sigma.rendering.createNodeBorderProgram === 'function'
      );
    }

    function nodeProgramClasses() {
      if (!borderedNodeProgramSupported()) return {};

      return {
        [BORDERED_NODE_TYPE]: window.Sigma.rendering.createNodeBorderProgram({
          borders: [
            {
              size: { value: NODE_BORDER_WIDTH_RATIO },
              color: { attribute: 'borderColor', defaultValue: theme.nodeBorder },
            },
            {
              size: { fill: true },
              color: { attribute: 'color' },
            },
          ],
          drawHover: drawNodeHover,
          drawLabel: drawNodeLabelNoop,
        }),
      };
    }

    function setupTopLabelOverlay() {
      const r = renderer();
      if (!r || typeof r.createCanvasContext !== 'function') return;

      try {
        r.createCanvasContext('topLabels', {
          afterLayer: 'hoverNodes',
          style: { pointerEvents: 'none' },
        });
        r.resize(true);

        const canvases = typeof r.getCanvases === 'function'
          ? r.getCanvases()
          : {};
        topLabelContext = canvases.topLabels
          ? canvases.topLabels.getContext('2d')
          : null;
      } catch (err) {
        topLabelContext = null;
        if (window.console && console.warn) console.warn('Could not create top label overlay:', err);
      }

      if (topLabelContext) {
        r.on('afterRender', drawTopLabelOverlay);
      }
    }

    function clearTopLabelOverlay() {
      const r = renderer();
      if (!topLabelContext || !r) return;

      const dims = r.getDimensions();
      topLabelContext.clearRect(0, 0, dims.width, dims.height);
    }

    function topLabelOverlayNodes() {
      const r = renderer();
      const g = graph();
      if (!r || !g) return [];
      if (typeof r.getNodeDisplayedLabels !== 'function') return [];

      const nodes = [...r.getNodeDisplayedLabels()];
      return nodes
        .filter(node => {
          if (!deps.nodeVisible(node)) return false;

          const display = typeof r.getNodeDisplayData === 'function'
            ? r.getNodeDisplayData(node)
            : null;
          return Boolean(display && !display.hidden && display.label);
        })
        .map(node => {
          const display = r.getNodeDisplayData(node);
          return { node, zIndex: Number(display.zIndex) || 0 };
        })
        .sort((a, b) => a.zIndex - b.zIndex)
        .map(item => item.node);
    }

    function drawTopLabelOverlay() {
      const r = renderer();
      const g = graph();
      if (!topLabelContext || !r || !g) return;

      clearTopLabelOverlay();
      const labelZoomScale = currentNodeLabelZoomScale();
      g.forEachNode(node => {
        if (!deps.nodeGhostVisible(node)) return;

        const attrs = g.getNodeAttributes(node);
        const display = r.getNodeDisplayData(node);
        if (!display || display.hidden) return;

        const point = r.graphToViewport({ x: attrs.x, y: attrs.y });
        const size = typeof r.scaleSize === 'function'
          ? r.scaleSize(display.size)
          : display.size;

        drawGhostNodeDashedBorder(topLabelContext, {
          ...display,
          x: point.x,
          y: point.y,
          size,
        });
      });

      topLabelOverlayNodes().forEach(node => {
        const attrs = g.getNodeAttributes(node);
        const display = r.getNodeDisplayData(node);
        if (!display || display.hidden || !display.label) return;

        const point = r.graphToViewport({ x: attrs.x, y: attrs.y });
        const size = typeof r.scaleSize === 'function'
          ? r.scaleSize(display.size)
          : display.size;

        drawNodeLabel(topLabelContext, {
          ...display,
          x: point.x,
          y: point.y,
          size,
          labelZoomScale,
        });
      });
    }

    return {
      constants: {
        LABEL_RENDERED_SIZE_THRESHOLD,
        LABEL_DENSITY,
        LABEL_GRID_CELL_SIZE,
        NODE_LABEL_FONT_SIZE,
        NODE_LABEL_LINE_HEIGHT_RATIO,
        BORDERED_NODE_TYPE,
      },
      theme: () => theme,
      refreshTheme,
      invalidateVisibilityPalette,
      currentVisibilityPalette,
      accessibleNodeLabelColor,
      borderedNodeProgramSupported,
      colorWithAlpha,
      currentNodeLabelMetrics,
      drawNodeHover,
      drawNodeLabelNoop,
      formatLabel,
      invalidateGraphToViewportRatio,
      minimumNodeScreenRadius,
      nodeDisplaySize,
      nodeLabelZoomScaleForRatio,
      nodeProgramClasses,
      nodeReducer,
      nodeSizeWithMinimumScreenRadius,
      precomputeNodeLabelMetrics,
      setupTopLabelOverlay,
    };
  }

  window.kbMapRendering = {
    createMapRendering,
  };
}());
