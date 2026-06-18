<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Multiple-Shooting Differential Dynamic Programming Algorithm. Part 1: Theory

Topics include Differential dynamic programming, Multiple shooting, Trajectory optimization, Spacecraft, Optimal control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Develops a rigorous multiple-shooting formulation of DDP with theoretical convergence analysis, establishing connections to classical multiple-shooting methods.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Multiple-shooting benefits a wide variety of optimal control algorithms by alleviating large sensitivities present in highly nonlinear problems, improving robustness to initial guesses, and increasing the potential for parallel implementation. In this paper series, motivated by the challenges of optimizing highly sensitive spacecraft trajectories, the multiple-shooting approach is embedded for the first time in the formulation of a Differential Dynamic Programming algorithm. Contrary to traditional nonlinear programming methods which necessitate minimal modification of the formulation in order to incorporate multiple-shooting principles, DDP requires novel non-trivial derivations, in order to include the initial conditions of the multiple-shooting subintervals and track their sensitivities. The initial conditions are updated in a necessary additional algorithmic step. A null-space trust-region method is used for the solution of the quadratic subproblems, and equality and inequality path and terminal constraints are handled through a general augmented Lagrangian approach. The propagation of the trajectory and the optimization of its controls are decoupled through the use of State-Transition Matrices. Part 1 of the paper series provides the necessary theoretical developments and implementation details for the algorithm. Part 2 contains validation and application cases.
