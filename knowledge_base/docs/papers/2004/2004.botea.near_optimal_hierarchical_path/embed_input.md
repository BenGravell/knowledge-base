Near Optimal Hierarchical Path-Finding

Topics include Path planning, Hierarchical planning, A* search, Graph search, Game artificial intelligence, Grid maps.

Introduces HPA* (Hierarchical Pathfinding A*), which pre-computes cluster-level abstractions to reduce A* search cost dramatically. Achieves up to 10× speedup with paths within 1% of optimal, making it practical for real-time game AI and large grid environments.

We present HPA* (Hierarchical Path-Finding A*), a hierarchical approach for reducing problem complexity in path-finding on grid-based maps. The technique abstracts a map into linked local clusters. At the local level, the optimal distances for crossing each cluster are pre-computed and cached. At the global level, clusters are traversed in a single big step. A hierarchy can be extended to more than two levels. Compared to a highly-optimized A*, HPA* is shown to be up to 10 times faster, while finding paths that are within 1% of optimal.
