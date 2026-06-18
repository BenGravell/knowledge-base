<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Generation of Collision-Free Trajectories for a Quadrocopter Fleet: A Sequential Convex Programming Approach

Topics include Quadrocopter fleets, Collision avoidance, Trajectory generation, Sequential convex programming, Mixed-integer constraints, Multi-robot planning, Real-time replanning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Formulates multi-quadrocopter trajectory generation as a nonconvex optimization problem and solves it through sequential convex programming with collision and vehicle constraints. The paper's practical contribution is showing that coordinated, three-dimensional, collision-free trajectories for multiple vehicles can be generated within seconds, making centralized fleet planning viable for lab-scale aerial robots.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents an algorithm that generates collision-free trajectories in three dimensions for multiple vehicles within seconds. The problem is cast as a non-convex optimization problem, which is iteratively solved using sequential convex programming that approximates non-convex constraints by using convex ones. The method generates trajectories that account for simple dynamics constraints and is thus independent of the vehicle's type. An extensive a posteriori vehicle-specific feasibility check is included in the algorithm. The algorithm is applied to a quadrocopter fleet. Experimental results are shown.
