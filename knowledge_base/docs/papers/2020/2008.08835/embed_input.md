EGO-Planner: An ESDF-free Gradient-based Local Planner for Quadrotors

Topics include Trajectory optimization, Aerial robotics, Robustness, Benchmarks, Optimization, Planning, EGO-Planner, Euclidean signed distance field.

Gradient-based planners are widely used for quadrotor local planning, in which a Euclidean Signed Distance Field (ESDF) is crucial for evaluating gradient magnitude and direction. Nevertheless, computing such a field has much redundancy since the trajectory optimization procedure only covers a very limited subspace of the ESDF updating range. In this paper, an ESDF-free gradient-based planning framework is proposed, which significantly reduces computation time. The main improvement is that the collision term in the penalty function is formulated by comparing the colliding trajectory with a collision-free guiding path. The resulting obstacle information will be stored only if the trajectory hits new obstacles, making the planner only extract necessary obstacle information. Then, we lengthen the time allocation if dynamical feasibility is violated. An anisotropic curve fitting algorithm is introduced to adjust higher-order derivatives of the trajectory while maintaining the original shape. Benchmark comparisons and real-world experiments verify its robustness and high-performance. The source code is released as ROS packages.

## Introduction

In recent years, the emergence of quadrotor online planning methods has greatly pushed the boundary of aerial autonomy, making drones fly out of laboratories and appear in numerous real-world applications. Among these methods, gradient-based ones, which smooth a trajectory and utilize the gradient information to improve its clearance, have shown great potential and gain more and more popularity.

In this paper, we design an ESDF-free Gradient-based lOcal planning framework called EGO, and we incorporate careful engineering considerations to make it lightweight and robust. The proposed algorithm is composed of a gradient-based spline optimizer and a post-refinement procedure. Firstly, we optimize the trajectory with smoothness, collision, and dynamical feasibility terms. Unlike traditional approaches that query pre-computed ESDF, we model the collision cost by comparing the trajectory inside obstacles with a guiding collision-free path.

To the best knowledge of us, this method is the first to achieve gradient-based local planning without an ESDF. Compared to existing state-of-the-art works, the proposed method generates safe trajectories with comparable smoothness and aggressiveness, but lower computation time of over an order of magnitude by omitting the ESDF maintenance. We perform comprehensive tests in simulation and real-world to validate our method.

## Conclusion and Future Work

In this paper, we investigate the necessity of ESDF for gradient-based trajectory planning and propose an ESDF-free local planner. It achieves comparable performance to some state-of-the-art ESDF-based planners but reduces computation time for over an order of magnitude. Benchmark comparisons and real-world experiments validate that it is robust and highly efficient.

The proposed method still has some flaws, which are the local minimum introduced by A\* search and the conservative trajectories introduced by unified time re-allocation. Therefore, we will work on performing topological planning to escape the local minimum and re-formulating the problem to generate near-optimal trajectories. The planner is designed for static environments and can tackle slowly moving obstacles (below 0.5m/s) without any modification. We will work on dynamic environment navigation by moving object detection and topological planning in the future.
