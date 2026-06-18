<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

RRT*-Connect: Faster, Asymptotically Optimal Motion Planning

Topics include Motion planning, Sampling-based planning, Asymptotic optimality, Bidirectional search, Rapidly-exploring random tree star, Rapidly-exploring random tree connect.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

RRT*-Connect merges the bidirectional search strategy of RRT-Connect with the asymptotic optimality guarantees of RRT*, growing two trees simultaneously from start and goal and connecting them greedily while rewiring for cost minimization. The result finds initial solutions significantly faster than RRT* while still converging toward the optimal path, combining the speed advantage of bidirectional search with provable optimality guarantees.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present an efficient asymptotically-optimal randomized motion planning algorithm solving single-query path planning problems using a bidirectional search. The algorithm combines the benefits from the widely known algorithms RRT-Connect and RRT* and scores better than both by finding a solution faster than RRT*, and - unlike RRT-Connect - converging towards a theoretical optimum. We outline the proposed algorithm and proof its optimality. The efficiency and robustness is demonstrated in a number of real world applications which benefit from the bidirectional approach: planning car trajectories in a parking garage for the autonomous vehicle CoCar, generating cost-efficient trajectories for the multi-legged walking robot LAURON V in a planetary exploration scenario and performing mobile manipulation tasks for our highly actuated service robot HoLLiE. Moreover, we compare and show the improvements over “vanilla” RRT in a set of challenging benchmarks. RRT*-Connect will contribute to increase the performance of autonomous robots and vehicles due to the reduced motion planning time in complex environments.
