/* browser/model.js - canonical browser-side model for the paper map. */

'use strict';

(function () {
  function createBrowserMapModel(data, options = {}) {
    const helpers = options.helpers || {};
    const itemTypeKey = helpers.itemTypeKey;
    const nodeKey = helpers.nodeKey;
    const paddedPaperNavPath = helpers.paddedPaperNavPath;
    const paperNavPath = helpers.paperNavPath;
    const paperSearchText = helpers.paperSearchText;
    const quantile = helpers.quantile;
    const scriptUrl = options.scriptUrl || window.location.href;
    const hierarchyLevels = options.hierarchyLevels || [];
    const navPathOrderIndex = options.navPathOrderIndex || new Map();
    const categoryOrder = typeof options.categoryOrder === 'function'
      ? options.categoryOrder
      : () => [];
    const superCategoryOrder = typeof options.superCategoryOrder === 'function'
      ? options.superCategoryOrder
      : () => [];
    const groupId = typeof options.groupId === 'function'
      ? options.groupId
      : (level, parts) => `agg:${level}:${parts.join('::')}`;
    const branchColorForPath = typeof options.branchColorForPath === 'function'
      ? options.branchColorForPath
      : () => '#000000';
    const uncategorizedCategory = options.uncategorizedCategory || 'Uncategorized';
    const paperSuperCategory = typeof options.paperSuperCategory === 'function'
      ? options.paperSuperCategory
      : attrs => attrs.super_category || attrs.category || uncategorizedCategory;
    const aggregatePositionBiasByLevel = options.aggregatePositionBiasByLevel || [];
    const aggregatePositionOuterQuantile = Number.isFinite(options.aggregatePositionOuterQuantile)
      ? options.aggregatePositionOuterQuantile
      : 0.84;
    const onSimilarityRowsLoaded = typeof options.onSimilarityRowsLoaded === 'function'
      ? options.onSimilarityRowsLoaded
      : null;
    const paperDataById = new Map(data.nodes.map(node => [node.data.id, node.data]));
    const similarityData = data.similarity || {};
    const similarityScale = Number(similarityData.scale || (data.meta || {}).similarityScale || 1);
    const similarityIdIndex = new Map((similarityData.ids || []).map((id, index) => [id, index]));
    const similarityShape = Array.isArray(similarityData.shape) ? similarityData.shape.map(Number) : [];
    let similarityRows = Array.isArray(similarityData.rows) ? similarityData.rows : null;
    let hierarchyData = null;
    let maxTreeDistanceCache = null;
    let treeProximityScaleCache = null;
    const relevanceMetricsByEgo = new Map();

    loadSimilarityRows();

    function paper(paperId) {
      return paperDataById.get(paperId) || null;
    }

    function commonPrefixLength(a, b) {
      const limit = Math.min(a.length, b.length);
      let i = 0;
      while (i < limit && a[i] === b[i]) i += 1;
      return i;
    }

    function treeDistance(aId, bId) {
      if (aId === bId) return 0;
      const a = paper(aId);
      const b = paper(bId);
      if (!a || !b) return Infinity;

      const aPath = paperNavPath(a);
      const bPath = paperNavPath(b);
      const common = commonPrefixLength(aPath, bPath);
      return (aPath.length - common) + (bPath.length - common);
    }

    function semanticSimilarity(aId, bId) {
      if (aId === bId) return 1;
      const aIndex = similarityIdIndex.get(aId);
      const bIndex = similarityIdIndex.get(bId);
      if (aIndex === undefined || bIndex === undefined || !similarityRows) return null;

      const raw = similarityValueAt(aIndex, bIndex);
      const numeric = Number(raw);
      if (!Number.isFinite(numeric)) return null;
      return similarityScale ? numeric / similarityScale : numeric;
    }

    function similarityValueAt(row, col) {
      if (Array.isArray(similarityRows)) {
        const values = similarityRows[row];
        return values ? values[col] : null;
      }
      const width = Number(similarityShape[1] || similarityIdIndex.size || 0);
      if (!width || row < 0 || col < 0) return null;
      return similarityRows[row * width + col];
    }

    function loadSimilarityRows() {
      if (similarityRows || !similarityData.file) return;
      const height = Number(similarityShape[0] || similarityIdIndex.size || 0);
      const width = Number(similarityShape[1] || similarityIdIndex.size || 0);
      if (!height || !width) return;

      const url = new URL(String(similarityData.file), scriptUrl);
      fetch(url.href, { cache: 'no-cache' })
        .then(response => {
          if (!response.ok) throw new Error(`Could not load ${url.href}: ${response.status}`);
          return response.arrayBuffer();
        })
        .then(buffer => {
          const expectedBytes = height * width * Int16Array.BYTES_PER_ELEMENT;
          if (buffer.byteLength !== expectedBytes) {
            throw new Error(`Similarity matrix shape mismatch: expected ${expectedBytes} bytes, found ${buffer.byteLength}.`);
          }
          similarityRows = new Int16Array(buffer);
          relevanceMetricsByEgo.clear();
          if (onSimilarityRowsLoaded) onSimilarityRowsLoaded();
        })
        .catch(error => {
          console.warn('[map] Similarity matrix unavailable:', error);
        });
    }

    function maxTreeDistance() {
      if (maxTreeDistanceCache === null) {
        const depth = Math.max(
          1,
          ...data.nodes.map(node => paperNavPath(node.data || {}).length)
        );
        maxTreeDistanceCache = depth * 2;
      }
      return maxTreeDistanceCache;
    }

    function treeProximityScale() {
      if (treeProximityScaleCache) return treeProximityScaleCache;

      const configured = (data.meta || {}).treeProximity || {};
      const configuredScale = Array.isArray(configured.scale)
        ? configured.scale.map(value => Number(value)).filter(value => Number.isFinite(value))
        : [];

      treeProximityScaleCache = configuredScale.length
        ? configuredScale
        : Array.from({ length: maxTreeDistance() + 1 }, (_, distance) => (
          maxTreeDistance() ? 1 - distance / maxTreeDistance() : 1
        ));
      return treeProximityScaleCache;
    }

    function treeProximityForDistance(distance) {
      if (!Number.isFinite(distance)) return -Infinity;
      const scale = treeProximityScale();
      const index = Math.max(0, Math.min(scale.length - 1, Math.round(distance)));
      return scale[index];
    }

    function relevanceMetrics(egoId) {
      if (relevanceMetricsByEgo.has(egoId)) {
        return relevanceMetricsByEgo.get(egoId);
      }

      const metrics = data.nodes.map(node => {
        const paperId = node.data.id;
        const distance = treeDistance(egoId, paperId);
        return {
          paperId,
          semantic: semanticSimilarity(egoId, paperId) ?? -1,
          treeProximity: treeProximityForDistance(distance),
        };
      });

      relevanceMetricsByEgo.set(egoId, metrics);
      return metrics;
    }

    function aggregateLabel(label, count) {
      return `${label}\n${count}`;
    }

    function createHierarchyGroup({
      level,
      label,
      superCategory,
      category,
      subCategory,
      path = [],
      pathIndex = 0,
      color,
      parent = null,
      isCategoryLeaf = false,
    }) {
      const pathParts = path.length
        ? path
        : [superCategory, category, subCategory || (isCategoryLeaf ? category : null)].filter(Boolean);
      return {
        key: `${level}:${pathParts.join('::')}`,
        level,
        label,
        superCategory,
        category,
        subCategory,
        path,
        pathIndex,
        color,
        parent,
        isCategoryLeaf,
        children: [],
        childMap: new Map(),
        leafIds: [],
        filterKeys: new Set(),
        itemTypes: new Set(),
        searchParts: new Set([label, superCategory, category, subCategory].filter(Boolean)),
        previewTitles: [],
        x: 0,
        y: 0,
        layoutX: null,
        layoutY: null,
        leafPoints: [],
      };
    }

    function ensureHierarchyChild(parent, key, spec) {
      const map = parent ? parent.childMap : spec.rootMap;
      if (map.has(key)) return map.get(key);

      const group = createHierarchyGroup({ ...spec, parent });
      map.set(key, group);
      if (parent) parent.children.push(group);
      else spec.roots.push(group);
      return group;
    }

    function accumulateHierarchyGroup(group, paperNode) {
      const attrs = paperNode.data;
      group.leafIds.push(attrs.id);
      group.filterKeys.add(nodeKey(attrs));
      group.itemTypes.add(itemTypeKey(attrs));
      group.searchParts.add(paperSearchText(attrs));
      const x = Number(paperNode.position.x) || 0;
      const y = Number(paperNode.position.y) || 0;
      group.x += x;
      group.y += y;
      group.leafPoints.push({ x, y });
      if (group.previewTitles.length < 4 && attrs.title) group.previewTitles.push(attrs.title);
    }

    function hierarchyGroupCentroid(group) {
      const count = group.leafIds.length || 1;
      return {
        x: group.x / count,
        y: group.y / count,
      };
    }

    function aggregatePositionBias(group) {
      const index = Math.max(Number(group.pathIndex) || 0, 0);
      if (index < aggregatePositionBiasByLevel.length) {
        return aggregatePositionBiasByLevel[index];
      }
      return 0.18;
    }

    function biasedAggregatePosition(group, referencePoint) {
      const centroid = hierarchyGroupCentroid(group);
      const leafPoints = group.leafPoints || [];
      if (leafPoints.length < 2 || !referencePoint) return centroid;

      const dx = centroid.x - referencePoint.x;
      const dy = centroid.y - referencePoint.y;
      const distance = Math.sqrt(dx * dx + dy * dy);
      if (!Number.isFinite(distance) || distance < 1e-6) return centroid;

      const ux = dx / distance;
      const uy = dy / distance;
      const centroidProjection = dx * ux + dy * uy;
      const outerProjection = quantile(
        leafPoints.map(point => (point.x - referencePoint.x) * ux + (point.y - referencePoint.y) * uy),
        aggregatePositionOuterQuantile
      );

      if (!Number.isFinite(outerProjection) || outerProjection <= centroidProjection) {
        return centroid;
      }

      const bias = aggregatePositionBias(group);
      const offset = (outerProjection - centroidProjection) * bias;
      return {
        x: centroid.x + ux * offset,
        y: centroid.y + uy * offset,
      };
    }

    function aggregateLayoutKey(path) {
      return JSON.stringify((path || []).map(part => String(part || '')));
    }

    function precomputedAggregatePosition(group) {
      const layouts = ((data.meta || {}).aggregateLayouts || {})[group.level] || {};
      const raw = layouts[aggregateLayoutKey(group.path)];
      if (!raw) return null;

      const x = Array.isArray(raw) ? Number(raw[0]) : Number(raw.x);
      const y = Array.isArray(raw) ? Number(raw[1]) : Number(raw.y);
      return Number.isFinite(x) && Number.isFinite(y) ? { x, y } : null;
    }

    function computeAggregateLayoutPositions(roots) {
      const rootTotals = roots.reduce(
        (acc, group) => {
          const count = group.leafIds.length || 0;
          acc.x += group.x;
          acc.y += group.y;
          acc.count += count;
          return acc;
        },
        { x: 0, y: 0, count: 0 }
      );
      const globalCentroid = rootTotals.count
        ? { x: rootTotals.x / rootTotals.count, y: rootTotals.y / rootTotals.count }
        : { x: 0, y: 0 };

      function visit(group, parentCentroid = null) {
        const referencePoint = parentCentroid || globalCentroid;
        const position = precomputedAggregatePosition(group) ||
          biasedAggregatePosition(group, referencePoint);
        const centroid = hierarchyGroupCentroid(group);

        group.layoutX = position.x;
        group.layoutY = position.y;
        group.centroidX = centroid.x;
        group.centroidY = centroid.y;
        group.children.forEach(child => visit(child, centroid));
      }

      roots.forEach(root => visit(root));
    }

    function hierarchySortKey(group) {
      const pathKey = (group.path || []).join('::');
      const pathIndex = navPathOrderIndex.has(pathKey) ? navPathOrderIndex.get(pathKey) : -1;
      if (pathIndex >= 0) return [pathIndex, group.label];

      if ((group.pathIndex || 0) === 0) {
        const order = superCategoryOrder();
        const index = order.indexOf(group.label);
        return [index < 0 ? Number.MAX_SAFE_INTEGER : index, group.label];
      }

      if ((group.pathIndex || 0) === 1) {
        const order = categoryOrder();
        const index = order.indexOf(group.category);
        return [index < 0 ? Number.MAX_SAFE_INTEGER : index, group.label];
      }

      const subOrder = ((data.meta || {}).subCategoryOrder || {})[group.category] || [];
      const index = group.subCategory ? subOrder.indexOf(group.subCategory) : -1;
      return [index < 0 ? Number.MAX_SAFE_INTEGER : index, group.label];
    }

    function sortHierarchyGroups(groups) {
      groups.sort((a, b) => {
        const ak = hierarchySortKey(a);
        const bk = hierarchySortKey(b);
        return ak[0] - bk[0] || String(ak[1]).localeCompare(String(bk[1]));
      });

      groups.forEach(group => sortHierarchyGroups(group.children));
    }

    function aggregateNodeId(detailLevel, group) {
      return groupId(detailLevel, [group.key]);
    }

    function groupAncestorIds(group) {
      const ancestors = {};
      let cursor = group.parent;

      while (cursor) {
        ancestors[cursor.level] = aggregateNodeId(cursor.level, cursor);
        cursor = cursor.parent;
      }

      return ancestors;
    }

    function buildAggregateNode(group, detailLevel) {
      const count = group.leafIds.length || 1;
      const ancestorIds = groupAncestorIds(group);
      const parentId = group.parent
        ? aggregateNodeId(group.parent.level, group.parent)
        : null;

      return {
        data: {
          id: aggregateNodeId(detailLevel, group),
          kind: 'aggregate',
          detailLevel,
          hierarchyLevel: group.level,
          parentId,
          ancestorIds,
          label: aggregateLabel(group.label, count),
          fullLabel: group.label,
          title: group.label,
          authors: [],
          year: null,
          super_category: group.superCategory,
          category: group.category,
          sub_category: group.subCategory,
          nav_path: group.path,
          color: group.color,
          count,
          leafIds: group.leafIds,
          filterKeys: [...group.filterKeys],
          itemTypes: [...group.itemTypes],
          previewTitles: group.previewTitles,
          tags: [],
          summary: `${count} ${count === 1 ? 'paper' : 'papers'}`,
          searchText: [...group.searchParts].join(' ').toLowerCase(),
        },
        position: {
          x: Math.round((Number.isFinite(group.layoutX) ? group.layoutX : group.x / count) * 10) / 10,
          y: Math.round((Number.isFinite(group.layoutY) ? group.layoutY : group.y / count) * 10) / 10,
        },
      };
    }

    function buildHierarchyData() {
      if (hierarchyData) return hierarchyData;

      const roots = [];
      const rootMap = new Map();
      const branchLevels = hierarchyLevels.filter(level => level.aggregate);
      const groupsByLevel = Object.fromEntries(branchLevels.map(level => [level.id, []]));
      const paperAncestors = {};
      const aggregateNodes = [];

      data.nodes.forEach(paperNode => {
        const attrs = paperNode.data;
        const path = paddedPaperNavPath(attrs);
        const superCategory = path[0] || paperSuperCategory(attrs);
        const category = path[1] || attrs.category || superCategory || uncategorizedCategory;
        const subCategory = path[2] || attrs.sub_category || null;
        let parent = null;
        const ancestors = {};

        branchLevels.forEach((level, index) => {
          const label = path[index] || path[path.length - 1] || uncategorizedCategory;
          const pathPrefix = path.slice(0, index + 1);
          const group = ensureHierarchyChild(parent, label, {
            rootMap,
            roots,
            level: level.id,
            label,
            superCategory,
            category,
            subCategory: index >= 2 ? label : subCategory,
            path: pathPrefix,
            pathIndex: index,
            color: branchColorForPath(path, index),
            isCategoryLeaf: index >= paperNavPath(attrs).length,
          });
          accumulateHierarchyGroup(group, paperNode);
          ancestors[level.id] = aggregateNodeId(level.id, group);
          parent = group;
        });

        paperAncestors[attrs.id] = ancestors;
      });

      sortHierarchyGroups(roots);
      computeAggregateLayoutPositions(roots);

      function collect(group) {
        if (groupsByLevel[group.level]) groupsByLevel[group.level].push(group);
        group.children.forEach(collect);
      }
      roots.forEach(collect);

      hierarchyLevels
        .filter(level => level.aggregate)
        .forEach(level => {
          const groups = groupsByLevel[level.id] || [];
          groups.forEach(group => aggregateNodes.push(buildAggregateNode(group, level.id)));
        });

      hierarchyData = {
        roots,
        levels: hierarchyLevels,
        groupsByLevel,
        paperAncestors,
        nodes: aggregateNodes,
      };
      return hierarchyData;
    }

    function invalidateHierarchy() {
      hierarchyData = null;
    }

    return {
      allPaperNodes: () => data.nodes,
      paper,
      paperPath: attrs => paperNavPath(attrs),
      nodeKey,
      itemType: itemTypeKey,
      treeProximityForDistance,
      relevanceMetrics,
      hierarchy: buildHierarchyData,
      invalidateHierarchy,
    };
  }

  window.kbBrowserMapModel = {
    createBrowserMapModel,
  };
}());
