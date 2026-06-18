Optimal Sampling-based Planning for Linear-quadratic Kinodynamic Systems

Topics include Robotics, Motion planning.

Adapts RRT* to kinodynamic planning by using finite-horizon LQR as both the cost metric and steering method in state-time space. The paper proves almost-sure convergence to optimal solutions for affine dynamics with quadratic costs, then extends the method by local linearization to nonlinear systems and demonstrates it on constrained examples such as pendulum swing-up.

We propose a new method for applying RRT* to kinodynamic motion planning problems by using finite-horizon linear quadratic regulation (LQR) to measure cost and to extend the tree. First, we introduce the method in the context of arbitrary affine dynamical systems with quadratic costs. For these systems, the algorithm is shown to converge to optimal solutions almost surely. Second, we extend the algorithm to non-linear systems with non-quadratic costs, and demonstrate its performance experimentally.
