MPPI-IPDDP: Hybrid Method of Collision-Free Smooth Trajectory Generation for Autonomous Robots

Topics include Trajectory optimization, Model predictive path integral control, Differential dynamic programming, Interior point, Collision avoidance, Hybrid trajectory optimization.

Hybrid method combining MPPI for global, collision-free trajectory generation with Interior Point DDP (IPDDP) for smooth, dynamically optimal local refinement, leveraging the complementary strengths of sampling and gradient-based trajectory optimization.

This paper presents a hybrid trajectory optimization method designed to generate collision-free, smooth trajectories for autonomous mobile robots. By combining sampling-based Model Predictive Path Integral (MPPI) control with gradient-based Interior-Point Differential Dynamic Programming (IPDDP), we leverage their respective strengths in exploration and smoothing. The proposed method, MPPI-IPDDP, involves three steps: First, MPPI control is used to generate a coarse trajectory. Second, a collision-free convex corridor is constructed. Third, IPDDP is applied to smooth the coarse trajectory, utilizing the collision-free corridor from the second step. To demonstrate the effectiveness of our approach, we apply the proposed algorithm to trajectory optimization for differential-drive wheeled mobile robots and point-mass quadrotors. In comparisons with other MPPI variants and continuous optimization-based solvers, our method shows superior performance in terms of computational robustness and trajectory smoothness.

## Introduction

Path planning is a critical problem for autonomous vehicles and robots. Several considerations need to be addressed simultaneously in robot path planning and navigation, such as specifying mission goals, ensuring dynamic feasibility, avoiding collisions, and considering internal constraints.

Optimization-based methods for path planning can explicitly handle these tasks. Two popular optimal path planning methods for autonomous robots are gradient-based and sampling-based methods. Gradient-based methods assume that the objective and constraint functions in the planning problem are differentiable, allowing for a fast, locally optimal smooth trajectory. These methods typically rely on nonlinear programming solvers such as IPOPT \[\] and SNOPT \[\]. On the other hand, sampling-based methods do not require function differentiability, making them more suitable for modeling obstacles of various shapes....

## Conclusions

In this paper, we introduced MPPI-IPDDP, a new hybrid optimization-based local path planning method designed to generate collision-free, smooth, and optimal trajectories. Through two case studies, we demonstrated the effectiveness of the proposed MPPI-IPDDP in environments with complex obstacle layouts. However, there is still room for improvement. As discussed, incorporating Stein Variational Gradient Descent (SVGD) could enhance exploration capabilities. Additionally, addressing planning under uncertainty remains a key challenge....

where the indicator function for a radial collision-free corridor is defined as

with the intermediate parameters and vectors

Table I: Parameters for trajectory optimization of a wheeled mobile robot in Section IV-A.

The optimization-based trajectory generation architecture known as model predictive control (MPC) has been extensively applied to robotic trajectory generation and planning problems. Deep reinforcement learning-based trajectory generation for mobile robots is another popular approach \[\]. A comparison of the continuous optimal control and reinforcement learning frameworks for trajectory generation of autonomous drone racing is provided in \[\]. Combining MPC with learning schemes has drawn noticeable attention to the robotics and control community....

This paper proposes a hybrid trajectory optimization method that modularly incorporates sampling-based and gradient-based...
