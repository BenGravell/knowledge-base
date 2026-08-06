<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Kinodynamic Motion Planning

Topics include Kinodynamic planning, Motion planning, Robot dynamics, Obstacle avoidance, Computational geometry, Complexity theory.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Formulates kinodynamic motion planning as planning under simultaneous kinematic and dynamic constraints, including velocity, acceleration, obstacle clearance, and minimum-time objectives. The work established the term and problem class, connecting robot motion planning with dynamics-aware trajectory search and computational complexity.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Kinodynamic planning attempts to solve a robot motion problem subject to simultaneous kinematic and dynamics constraints. In the general problem, given a robot system, we must find a minimal-time trajectory that goes from a start position and velocity to a goal position and velocity while avoiding obstacles by a safety margin and respecting constraints on velocity and acceleration. We consider the simplified case of a point mass under Newtonian mechanics, together with velocity and acceleration bounds. The point must be flown from a start to a goal, amidst polyhedral obstacles in 2D or 3D. Although exact solutions to this problem are not known, we provide the first provably good approximation algorithm, and show that it runs in polynomial time.
