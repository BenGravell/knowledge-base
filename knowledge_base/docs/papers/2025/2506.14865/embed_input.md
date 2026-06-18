Efficient and Real-Time Motion Planning for Robotics Using Projection-Based Optimization

Topics include Trajectory optimization, Constrained optimization, Projection methods, Real-time, Robot motion planning.

Uses geometric projection operations to efficiently handle motion constraints in real-time robot trajectory optimization, avoiding full constraint Jacobian computations and achieving significant speedups over augmented Lagrangian approaches.

Generating motions for robots interacting with objects of various shapes is a complex challenge, further complicated by the robot geometry and multiple desired behaviors. While current robot programming tools (such as inverse kinematics, collision avoidance, and manipulation planning) often treat these problems as constrained optimization, many existing solvers focus on specific problem domains or do not exploit geometric constraints effectively. We propose an efficient first-order method, Augmented Lagrangian Spectral Projected Gradient Descent (ALSPG), which leverages geometric projections via Euclidean projections, Minkowski sums, and basis functions. We show that by using geometric constraints rather than full constraints and gradients, ALSPG significantly improves real-time performance. Compared to second-order methods like iLQR, ALSPG remains competitive in the unconstrained case. We validate our method through toy examples and extensive simulations, and demonstrate its effectiveness on a 7-axis Franka robot, a 6-axis P-Rob robot and a 1:10 scale car in real-world experiments. Source codes, experimental data and videos are available on the project webpage: this https URL

## Introduction

Many robotics tasks are framed as constrained optimization problems. For example, inverse kinematics (IK) seeks a robot configuration that matches a desired pose while respecting constraints like joint limits or stability. Motion planning and optimal control aim to determine trajectories or control commands that satisfy task-specific dynamics and environmental constraints. Model predictive control (MPC) solves real-time optimal control problems by addressing simplified, short-horizon constrained optimization problems.

Several second-order solvers such as SNOPT \[\], SLSQP \[\], LANCELOT \[\], and IPOPT \[\]---are commonly used to solve general constrained optimization problems. In robotics, however, most research focuses on solvers tailored to specific problems. For instance, constrained versions of differential dynamic programming (DDP) \[\], iterative linear quadratic regulator (iLQR) \[\], TrajOpt \[\], and CHOMP \[\] are used for motion planning. However, many of these solvers are not open-source, making them difficult to benchmark and improve....

## Conclusion

In this work, we presented a fast first-order constrained optimization framework based on geometric projections, and applied it to various robotics problems ranging from inverse kinematics to motion planning. We showed that many of the geometric constraints can be rewritten as a logical combination of geometric primitives onto which the projections admit analytical expressions. We built an augmented Lagrangian method with spectral projected gradient descent as a subproblem solver for constrained optimization....

### IV-C Optimal Control with ALSPG

When the shape of the object is implicit and cannot be expressed using hyperplanes, learning-based techniques can be employed to design the projections. Bernstein polynomial basis functions are efficient for learning the implicit shape. The advantage of this approach lies in the availability of analytical and smooth gradient information....

Robust IK: In this experiment, we would like to achieve a task of reaching and staying in the half-space under a plane whose slope is stochastic because, for example, of the uncertainties in the measurements of the vision system....
