<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Anytime Motion Planning Using the RRT*

Topics include Motion planning, Anytime, Asymptotically optimal, Probabilistically complete, Rapidly-exploring random tree star.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

This was a companion to the original RRT* paper, and introduced key innovations for anytime motion planning including the "committed trajectory" and a "branch-and-bound" technique for periodically pruning obviously suboptimal nodes from the tree.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The Rapidly-exploring Random Tree (RRT) algorithm, based on incremental sampling, efficiently computes motion plans. Although the RRT algorithm quickly produces candidate feasible solutions, it tends to converge to a solution that is far from optimal. Practical applications favor "anytime" algorithms that quickly identify an initial feasible plan, then, given more computation time available during plan execution, improve the plan toward an optimal solution. This paper describes an anytime algorithm based on the RRT* which (like the RRT) finds an initial feasible solution quickly, but (unlike the RRT) almost surely converges to an optimal solution. We present two key extensions to the RRT% committed trajectories and branch-and-bound tree adaptation, that together enable the algorithm to make more efficient use of computation time online, resulting in an anytime algorithm for real-time implementation. We evaluate the method using a series of Monte Carlo runs in a high-fidelity simulation environment, and compare the operation of the RRT and RRT* methods. We also demonstrate experimental results for an outdoor wheeled robotic vehicle.
