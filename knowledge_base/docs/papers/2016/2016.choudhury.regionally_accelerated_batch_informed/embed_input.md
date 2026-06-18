<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Regionally Accelerated Batch Informed Trees (RABIT*): A Framework to Integrate Local Information into Optimal Path Planning

Topics include Motion planning, Sampling-based planning, Asymptotic optimality, Anytime planning, RABIT*, BIT*, Hybrid planning, Local optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

RABIT* extends BIT* by hybridizing its global informed search with local gradient-based optimization (e.g. CHOMP). Rather than optimizing every edge, it selectively applies local optimization only to the subset of edges within the current informed set that are most likely to improve the solution, avoiding infeasible edges by finding alternative connections. This preserves asymptotic optimality while significantly accelerating convergence, particularly in problems with difficult-to-sample homotopy classes or narrow passages.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Sampling-based optimal planners, such as RRT*, almost-surely converge asymptotically to the optimal solution, but have provably slow convergence rates in high dimensions. This is because their commitment to finding the global optimum compels them to prioritize exploration of the entire problem domain even as its size grows exponentially. Optimization techniques, such as CHOMP, have fast convergence on these problems but only to local optima. This is because they are exploitative, prioritizing the immediate improvement of a path even though this may not find the global optimum of nonconvex cost functions. In this paper, we present a hybrid technique that integrates the benefits of both methods into a single search. A key insight is that applying local optimization to a subset of edges likely to improve the solution avoids the prohibitive cost of optimizing every edge in a global search. This is made possible by Batch Informed Trees (BIT*), an informed global technique that orders its search by potential solution quality. In our algorithm, Regionally Accelerated BIT* (RABIT*), we extend BIT* by using optimization to exploit local domain information and find alternative connections for edges in collision and accelerate the search.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This improves search performance in problems with difficult-to-sample homotopy classes (e.g., narrow passages) while maintaining almost-sure asymptotic convergence to the global optimum. Our experiments on simulated random worlds and real data from an autonomous helicopter show that on certain difficult problems, RABIT* converges 1.8 times faster than BIT*. Qualitatively, in problems with difficult-to-sample homotopy classes, we show that RABIT* is able to efficiently transform paths to avoid obstacles.
