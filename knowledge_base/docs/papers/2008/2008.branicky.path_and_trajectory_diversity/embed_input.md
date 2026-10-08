<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Path and Trajectory Diversity: Theory and Algorithms

Topics include Path diversity, Trajectory diversity, Motion planning, Path-set pruning, Obstacle avoidance, Reachability.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Defines path diversity through survival probabilities across obstacle environments and derives exact formulas. Inner-product and inclusion-exclusion heuristics prune large precomputed path sets while preserving reachability, and the framework extends to spatiotemporal trajectory diversity.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present heuristic algorithms for pruning large sets of candidate paths or trajectories down to smaller subsets that maintain desirable characteristics in terms of overall reachability and path length. Consider the example of a set of candidate paths in an environment that is the result of a forward search tree built over a set of actions or behaviors. The tree is precomputed and stored in memory to be used online to compute collision-free paths from the root of the tree to a particular goal node. In general, such a set of paths may be quite large, growing exponentially in the depth of the search tree. In practice, however, many of these paths may be close together and could be pruned without a loss to the overall problem of path-finding. The best such pruning for a given resulting tree size is the one that maximizes path diversity, which is quantified as the probability of the survival of paths, averaged over all possible obstacle environments. We formalize this notion and provide formulas for computing it exactly. We also present experimental results for two approximate algorithms for path set reduction that are efficient and yield desirable properties in terms of overall path diversity.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The exact formulas and approximate algorithms generalize to the computation and maximization of spatio-temporal diversity for trajectories.
