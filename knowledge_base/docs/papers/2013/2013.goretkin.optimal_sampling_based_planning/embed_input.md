<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimal Sampling-based Planning for Linear-quadratic Kinodynamic Systems

Topics include Robotics, Motion planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Adapts RRT* to kinodynamic planning by using finite-horizon LQR as both the cost metric and steering method in state-time space. The paper proves almost-sure convergence to optimal solutions for affine dynamics with quadratic costs, then extends the method by local linearization to nonlinear systems and demonstrates it on constrained examples such as pendulum swing-up.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a new method for applying RRT* to kinodynamic motion planning problems by using finite-horizon linear quadratic regulation (LQR) to measure cost and to extend the tree. First, we introduce the method in the context of arbitrary affine dynamical systems with quadratic costs. For these systems, the algorithm is shown to converge to optimal solutions almost surely. Second, we extend the algorithm to non-linear systems with non-quadratic costs, and demonstrate its performance experimentally.
