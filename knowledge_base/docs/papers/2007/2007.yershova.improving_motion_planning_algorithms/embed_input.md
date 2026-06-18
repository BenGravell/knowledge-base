Improving Motion-Planning Algorithms by Efficient Nearest-Neighbor Searching

Topics include Motion planning, Nearest neighbors, Sampling-based planning, Data structures, High-dimensional search, Robotics.

Studies how nearest-neighbor data structures affect the practical speed of sampling-based motion planners. The contribution is a careful systems-level reminder that planner performance often depends as much on search infrastructure as on the planning heuristic itself.

The cost of nearest-neighbor (NN) calls is one of the bottlenecks in the performance of sampling-based motion-planning algorithms. Therefore, it is crucial to develop efficient techniques for NN searching in configuration spaces arising in motion planning. In this paper, we present and implement an algorithm for performing NN queries in Cartesian products of R, S 1, and RP 3, the most common topological spaces in the context of motion planning. Our approach extends the algorithm based on kd-trees, called ANN, developed by Arya and Mount for Euclidean spaces. We prove the correctness of the algorithm and illustrate substantial performance improvement over the brute-force approach and several existing NN packages developed for general metric spaces. Our experimental results demonstrate a clear advantage of using the proposed method for both probabilistic roadmaps and rapidly exploring random trees
