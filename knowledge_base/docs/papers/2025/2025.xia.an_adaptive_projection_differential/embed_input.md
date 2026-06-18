<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

An Adaptive Projection Differential Dynamic Programming Method for Control Constrained Trajectory Optimization

Topics include Differential dynamic programming, Constrained optimization, Control constraints, Projection methods, Trajectory optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes an adaptive projection method within the DDP framework for handling control constraints, using projection operators that adapt based on constraint activity to achieve efficient and convergent constrained trajectory optimization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

To address the issue of missing constraints on control variables in the trajectory optimization problem of the differential dynamic programming (DDP) method, the adaptive projection differential dynamic programming (AP-DDP) method is proposed. The core of the AP-DDP method is to introduce adaptive relaxation coefficients to dynamically adjust the smoothness of the projection function and to effectively solve the gradient disappearance problem that may occur when the control variable is close to the constraint boundary. Additionally, the iterative strategy of the relaxation coefficient accelerates the search for a feasible solution in the initial stage, thereby improving the algorithm’s efficiency. When applied to three trajectory optimization problems, compared with similar truncated DDP, projected DDP, and Box-DDP methods, the AP-DDP method found the optimal solution in the shortest computation time, thereby proving the efficiency of the proposed algorithm. While ensuring the iterative process reaches the global optimum, the computing time of the AP-DDP method was reduced by 32.8%, 13.3%, and 18.5%, respectively, in the three examples.
