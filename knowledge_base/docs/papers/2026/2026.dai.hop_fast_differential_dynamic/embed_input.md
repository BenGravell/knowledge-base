<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

HOP: Fast Differential Dynamic Programming for Horizon-Optimal Trajectory Planning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper considers a Horizon-Optimal Control problem that seeks a dynamically feasible trajectory while minimizing the planning horizon, which is a fundamental problem in robotics with numerous applications. While many famous optimal control methods, such as LQR, iLQR/DDP, are well studied and deployed on various robots, they often have a fixed planning horizon, and their horizon-optimal counterparts are still undiscovered. The best result in the literature solves the horizon-optimal LQR problem by shifting the horizon and reusing the value functions computed by the Riccati recursion, which leads to an efficient algorithm. However, this approach is limited to LQR with time-invariant dynamics and costs only. This paper finds that the Riccati recursion can be reformulated into a form of Linear Fractional Transformation (LFT), which enjoys the structure that enables efficient computational reuse even for non-stationary dynamics and costs. Based on this insight, we develop a new efficient algorithm to solve Horizon-Optimal Time-Varying LQR problem to optimality, and further fuse it with DDP to handle general non-quadratic costs and nonlinear dynamics.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Results show, our approach always finds the same optimal solution as a naive brute force baseline method, while running up to 40 times faster. For nonlinear dynamics, our method always finds better solutions than approximation using time-invariant LQR.
