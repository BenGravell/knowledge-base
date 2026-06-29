/* browser/branch-filter.js - Tree branch filter widget for the map. */

'use strict';

(function () {
  function createMapBranchFilter(deps = {}) {
    const mapModel = deps.mapModel;
    const viewState = deps.viewState;
    const branchFilterAll = deps.branchFilterAll;
    const paperPrefix = deps.paperPrefix;

    function collectBranchFilterGroups(group, groups) {
      if (!group.isCategoryLeaf) groups.push(group);
      group.children.forEach(child => collectBranchFilterGroups(child, groups));
    }

    function branchFilterChildren(group) {
      const children = group ? group.children : mapModel.hierarchy().roots;
      return children.filter(child => !child.isCategoryLeaf);
    }

    function branchFilterPaperChildren(group) {
      if (!group || branchFilterChildren(group).length) return [];
      return (group.leafIds || [])
        .map(mapModel.paper)
        .filter(Boolean);
    }

    function branchFilterName(group) {
      return group ? group.label : 'All branches';
    }

    function branchFilterPathLabel(group) {
      if (!group) return 'Map root';
      const path = Array.isArray(group.path) && group.path.length
        ? group.path
        : [group.label];
      return path.join(' / ');
    }

    function branchFilterItemCount(group) {
      return group ? group.leafIds.length : mapModel.allPaperNodes().length;
    }

    function branchFilterChildCount(group) {
      return branchFilterChildren(group).length;
    }

    function branchCountLabel(count, singular, pluralLabel = `${singular}s`) {
      return `${count} ${count === 1 ? singular : pluralLabel}`;
    }

    function activeBranchKeyForAggregate(attrs) {
      const path = mapModel.paperPath(attrs);
      const exactKey = `${attrs.hierarchyLevel || attrs.detailLevel}:${path.join('::')}`;
      if (viewState.branchFilterGroups.has(exactKey)) return exactKey;

      let best = null;
      viewState.branchFilterGroups.forEach((group, key) => {
        const groupPath = group.path || [];
        if (groupPath.length > path.length) return;
        if (!groupPath.every((part, index) => path[index] === part)) return;
        if (!best || groupPath.length > best.pathLength) {
          best = { key, pathLength: groupPath.length };
        }
      });
      return best ? best.key : branchFilterAll;
    }

    function activateBranchNode(attrs, node) {
      deps.clearHoverClickNode(node);
      setActiveBranchFilter(activeBranchKeyForAggregate(attrs));

      const nextLevel = deps.nextDetailLevel(attrs.detailLevel);
      if (nextLevel) {
        deps.applyDetailLevel(nextLevel);
        return;
      }

      deps.applyCategoryFilter();
    }

    function syncBranchFilterWidget() {
      renderBranchFilterWidget();
    }

    function setActiveBranchFilter(key) {
      const nextKey = viewState.branchFilterGroups.has(key) ? key : branchFilterAll;
      viewState.activeBranchFilterKey = nextKey;
      viewState.activeCategories.clear();

      if (nextKey === branchFilterAll) {
        mapModel.allPaperNodes().forEach(node => viewState.activeCategories.add(mapModel.nodeKey(node.data || {})));
      } else {
        viewState.branchFilterGroups.get(nextKey).filterKeys.forEach(filterKeyValue => {
          viewState.activeCategories.add(filterKeyValue);
        });
      }

      syncBranchFilterWidget();
      enforceActiveBranchDetailFloor();
    }

    function enforceActiveBranchDetailFloor() {
      const nextLevel = deps.detailLevelForActiveBranch(viewState.currentDetailLevel);
      if (nextLevel && nextLevel !== viewState.currentDetailLevel) {
        deps.applyDetailLevel(nextLevel);
        return;
      }
      deps.updateDetailButtons();
    }

    function selectBranchForPaper(attrs) {
      const key = mapModel.nodeKey(attrs);
      let best = null;
      viewState.branchFilterGroups.forEach((group, groupKey) => {
        if (!group.filterKeys.has(key)) return;
        if (!best || (group.path || []).length > (best.group.path || []).length) {
          best = { group, groupKey };
        }
      });
      setActiveBranchFilter(best ? best.groupKey : branchFilterAll);
    }

    function buildCategoryFilters(selectedKey = viewState.activeBranchFilterKey) {
      const container = document.getElementById('mm-category-filters');
      if (!container) return;

      const model = mapModel.hierarchy();
      const groups = [];
      model.roots.forEach(root => collectBranchFilterGroups(root, groups));
      viewState.branchFilterGroups = new Map(groups.map(group => [group.key, group]));

      container.innerHTML = '';
      setActiveBranchFilter(selectedKey);
    }

    function renderBranchFilterWidget() {
      const container = document.getElementById('mm-category-filters');
      if (!container) return;

      const currentGroup = viewState.branchFilterGroups.get(viewState.activeBranchFilterKey) || null;
      const ancestors = branchFilterAncestors(currentGroup);
      const branchChildren = branchFilterChildren(currentGroup);
      const paperChildren = branchFilterPaperChildren(currentGroup);
      const sections = [];
      if (ancestors.length) sections.push(branchFilterSection('Ancestors', ancestors, 'path', currentGroup));
      sections.push(branchFilterSection('', [currentGroup], 'ego', currentGroup));
      sections.push(branchFilterChildrenSection(branchChildren, paperChildren, currentGroup));

      container.innerHTML = window.kbTreeNavigator.renderStack({
        density: 'compact',
        sections,
      });
      container.onclick = event => {
        const target = event.target.closest('[data-ct-select]');
        if (!target || !container.contains(target)) return;
        const key = target.getAttribute('data-ct-select') || branchFilterAll;
        if (key.startsWith(paperPrefix)) {
          focusPaperFromBranchFilter(key.slice(paperPrefix.length));
          return;
        }
        if (viewState.activeBranchFilterKey === key) return;
        setActiveBranchFilter(key);
        deps.applyCategoryFilter();
      };
    }

    function branchFilterAncestors(group) {
      if (!group) return [];
      const ancestors = [null];
      const lineage = [];
      let node = group && group.parent;
      while (node) {
        lineage.unshift(node);
        node = node.parent;
      }
      return ancestors.concat(lineage);
    }

    function branchFilterSection(title, groups, sectionKind, currentGroup) {
      return {
        title,
        kind: sectionKind,
        empty: 'No child branches.',
        rows: groups.map(group => branchFilterRow(group, currentGroup, sectionKind)),
      };
    }

    function branchFilterChildrenSection(branchGroups, papers, currentGroup) {
      const rows = branchGroups.length
        ? branchGroups.map(group => branchFilterRow(group, currentGroup, 'children'))
        : papers.map(branchFilterPaperRow);
      return {
        title: 'Children',
        kind: 'children',
        empty: 'No children.',
        rows,
      };
    }

    function branchFilterRow(group, currentGroup, sectionKind) {
      const key = group ? group.key : branchFilterAll;
      const itemCount = branchFilterItemCount(group);
      const childCount = branchFilterChildCount(group);
      return {
        id: key,
        kind: 'branch',
        label: branchFilterName(group),
        current: key === viewState.activeBranchFilterKey,
        ancestor: sectionKind === 'path',
        parent: Boolean(currentGroup && (group
          ? currentGroup.parent && currentGroup.parent.key === group.key
          : !currentGroup.parent)),
        successor: sectionKind === 'children',
        hasChildren: childCount > 0,
        color: group && group.color,
        ariaLabel: `${branchFilterPathLabel(group)}, ${branchCountLabel(itemCount, 'item')}, ${branchCountLabel(childCount, 'child', 'children')}`,
        counters: [
          { kind: 'descendants', count: itemCount, singular: 'item' },
          { kind: 'children', count: childCount, singular: 'child', plural: 'children' },
        ],
      };
    }

    function branchFilterPaperRow(attrs) {
      const paperId = attrs.id;
      const authors = Array.isArray(attrs.authors) ? attrs.authors.filter(Boolean) : [];
      const author = authors.length ? authors[0] + (authors.length > 1 ? ' et al.' : '') : '';
      const meta = [author, attrs.year, mapModel.itemType(attrs)].filter(Boolean).join(' / ');
      const label = attrs.label || attrs.title || paperId;
      return {
        id: paperPrefix + paperId,
        kind: 'paper',
        label,
        meta,
        successor: true,
        previewId: false,
        ariaLabel: [attrs.title || label, meta].filter(Boolean).join(', '),
        counters: [],
      };
    }

    function focusPaperFromBranchFilter(paperId) {
      if (!paperId || !deps.graphHasNode(paperId)) return;

      deps.applyDetailLevel('paper');
      viewState.selectNode(paperId);
      deps.setSelectedNodeFilterEnabled(true);
      deps.hideHoverTooltip();
      deps.refreshView();
      deps.focusCameraOnNode(paperId, 320);
      window.setTimeout(() => deps.showFocusedPaperTooltip(paperId), 340);
      deps.writeFocusPaperId(paperId);
    }

    return {
      activateBranchNode,
      buildCategoryFilters,
      renderBranchFilterWidget,
      selectBranchForPaper,
      setActiveBranchFilter,
      syncBranchFilterWidget,
    };
  }

  window.kbMapBranchFilter = {
    createMapBranchFilter,
  };
}());
