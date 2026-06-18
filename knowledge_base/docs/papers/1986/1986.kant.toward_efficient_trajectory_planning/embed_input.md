<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Toward Efficient Trajectory Planning: The Path-Velocity Decomposition

Topics include Path-velocity decomposition, Trajectory planning, Motion planning, Dynamic obstacles, Path-time space, Graph search, Robotics.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Kant and Zucker introduce path-velocity decomposition for trajectory planning in dynamic environments: first plan a collision-free path through static obstacles, then plan velocity along that path to avoid moving obstacles. The paper's path-time-space formulation became a classic way to separate geometric planning from timing decisions.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a novel approach to solving the trajectory planning problem (TPP) in time-varying environments. The essence of our approach lies in a heuristic but natural decomposition of TPP into two subproblems: planning a path to avoid collision with static obstacles and planning the velocity along the path to avoid collision with moving obstacles. We call the first subproblem the path planning problem (PPP) and the second the velocity planning problem (VPP). Thus, our decomposition is summarized by the equation TPP => PPP + VPP. The symbol => indicates that the decomposition holds under certain assumptions, e.g., when obstacles are moving independently of, i.e., not tracking, the robot. Furthermore, we pose the VPP in path-time space, where time is explicitly represented as an extra dimension, and reduce it to a graph search in this space. In fact, VPP is transformed to a two-dimensional PPP in path-time space with some additional constraints. Algorithms are then presented to solve the VPP with different optimality criteria: minimum length in path-time space, and minimum time.
