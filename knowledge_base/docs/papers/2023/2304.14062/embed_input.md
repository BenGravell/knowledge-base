Comparison of Optimization-Based Methods for Energy-Optimal Quadrotor Motion Planning

Topics include Nonconvex optimization, Trajectory optimization, Motion planning, Robotics, Aerial robotics, Benchmarks, Online algorithms, Optimization, Planning, Control, Optimization problem.

Quadrotors are agile flying robots that are challenging to control. Considering the full dynamics of quadrotors during motion planning is crucial to achieving good solution quality and small tracking errors during flight. Optimization-based methods scale well with high-dimensional state spaces and can handle dynamic constraints directly, therefore they are often used in these scenarios. The resulting optimization problem is notoriously difficult to solve due to its nonconvex constraints. In this work, we present an analysis of four solvers for nonlinear trajectory optimization (KOMO, direct collocation with SCvx, direct collocation with CasADi, Crocoddyl) and evaluate their performance in scenarios where the solvers are tasked to find minimum-effort solutions to geometrically complex problems and problems requiring highly dynamic solutions. Benchmarking these methods helps to determine the best algorithm structures for these kinds of problems.

## Introduction

In recent years, multirotors have risen in popularity in academia and industry due to their exceptional agility and simple mechanical design. However, motion planning for these under-actuated systems requires to consider the dynamical constraints and is computationally expensive. While sampling- and search-based approaches to motion planning have strong theoretical guarantees regarding completeness, they suffer from the curse of dimensionality and scale exponentially with the dimension of the state space....

## Approach

To objectively compare and evaluate different trajectory optimization techniques we need standard benchmarks. To this end, we benchmark four different optimization-based solvers on dynamically and geometrically challenging scenarios of multirotor flight. We tune each solver, since the performance highly depends on the choice of user-defined weights and the parameters of the algorithms. Our results show that KOMO achieves the lowest objective function values across all scenarios, while DDP requires the least amount of time and iterations....

For the obtained optimal values, the cause for the consistent computation of the higher-cost solutions of DDP in Scenario 4 should be investigated. One conjecture is that this is related to small differences in the constraint formulation and slight violations of some constraints in the other solvers. For the computational effort, comparing the number of iterations can be misleading since the effort for DDP iterations and Newton iterations is not identical and we do not account for the number of line search iterations for Newton's method....

### II-C3 Differential Dynamic Programming (DDP)

The discrete problem is implemented in four different trajectory optimization frameworks. These use different transcriptions and algorithms for solving the nonlinear problem. All methods discretize the continuous-time problem at $N = 100$ time points.

Figure 1: Example trajectories for the chosen scenarios. The black quadrotors represent a possible trajectory solving the problem and the red arrows indicate the z-axis of the model.

### II-A Quadrotor Model

We consider a quadrotor model with state vector $x = {\lbrack p,v,q,\omega_{B}\rbrack}^{T} \in {\mathbb{R}}^{13}$, where $p \in {\mathbb{R}}^{3}$ is the position, $v \in {\mathbb{R}}^{3}$ is the velocity (both in the inertial frame), $q \in...
