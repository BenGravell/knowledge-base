<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Deterministic Sampling-Based Motion Planning: Optimality, Complexity, and Performance

Topics include Sampling-based planning, Deterministic sampling, Low-dispersion sequences, PRM, FMT*, Asymptotic optimality, Motion planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Shows that sampling-based planners can retain optimality guarantees with deterministic low-dispersion sequences, often with better complexity constants and certification properties than iid sampling. It is a useful theoretical bridge between lattice-like planners and PRM/FMT-style algorithms.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Probabilistic sampling-based algorithms, such as the probabilistic roadmap (PRM) and the rapidly-exploring random tree (RRT) algorithms, represent one of the most successful approaches to robotic motion planning, due to their strong theoretical properties (in terms of probabilistic completeness or even asymptotic optimality) and remarkable practical performance. Such algorithms are probabilistic in that they compute a path by connecting independently and identically distributed random points in the configuration space. Their randomization aspect, however, makes several tasks challenging, including certification for safety-critical applications and use of offline computation to improve real-time execution. Hence, an important open question is whether similar (or better) theoretical guarantees and practical performance could be obtained by considering deterministic, as opposed to random sampling sequences. The objective of this paper is to provide a rigorous answer to this question.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Specifically, we first show that PRM, for a certain selection of tuning parameters and deterministic low-dispersion sampling sequences, is deterministically asymptotically optimal, i.e., it returns a path whose cost converges deterministically to the optimal one as the number of points goes to infinity. Second, we characterize the convergence rate, and we find that the factor of sub-optimality can be very explicitly upper-bounded in terms of the l2-dispersion of the sampling sequence and the connection radius of PRM. Third, we show that an asymptotically optimal version of PRM exists with computational and space complexity arbitrarily close to O(n). Fourth, we show that our theoretical results and insights extend to other batch-processing algorithms such as FMT*, to non-uniform sampling strategies, to k-nearest-neighbor implementations, and to differentially-constrained problems. Finally, through numerical experiments, we show that planning with deterministic low-dispersion sampling generally provides superior performance in terms of path cost and success rate.
