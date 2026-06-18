<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Lifelong Planning A*

Topics include Lifelong planning A*, Incremental search, A* search, Path planning, Dynamic graphs, Heuristic search, Shortest path.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Develops Lifelong Planning A* as a full incremental heuristic-search algorithm for repeated shortest-path problems on changing graphs. The paper formalizes its relationship to A*, proves key properties, and shows when reusing previous search information accelerates replanning.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Heuristic search methods promise to find shortest paths for path-planning problems faster than uninformed search methods. Incremental search methods, on the other hand, promise to find shortest paths for series of similar path-planning problems faster than is possible by solving each path-planning problem from scratch. In this article, we develop Lifelong Planning A* (LPA*), an incremental version of A* that combines ideas from the artificial intelligence and the algorithms literature. It repeatedly finds shortest paths from a given start vertex to a given goal vertex while the edge costs of a graph change or vertices are added or deleted. Its first search is the same as that of a version of A* that breaks ties in favor of vertices with smaller g-values but many of the subsequent searches are potentially faster because it reuses those parts of the previous search tree that are identical to the new one. We present analytical results that demonstrate its similarity to A* and experimental results that demonstrate its potential advantage in two different domains if the path-planning problems change only slightly and the changes are close to the goal.
