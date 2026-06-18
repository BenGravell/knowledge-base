iDb-RRT: Sampling-based Kinodynamic Motion Planning with Motion Primitives and Trajectory Optimization

Topics include Kinodynamic planning, Rapidly-exploring random tree, iDb-RRT, Motion primitives, Trajectory optimization, Discontinuity bounded.

Combines short motion primitives (allowing bounded discontinuities) with the RRT exploration strategy, iteratively repairing discontinuities via trajectory optimization. Finds solutions up to 10X faster than prior methods across a benchmark of 30 problems.

Rapidly-exploring Random Trees (RRT) and its variations have emerged as a robust and efficient tool for finding collision-free paths in robotic systems. However, adding dynamic constraints makes the motion planning problem significantly harder, as it requires solving two-value boundary problems (computationally expensive) or propagating random control inputs (uninformative). Alternatively, Iterative Discontinuity Bounded A* (iDb-A*), introduced in our previous study, combines search and optimization iteratively. The search step connects short trajectories (motion primitives) while allowing a bounded discontinuity between the motion primitives, which is later repaired in the trajectory optimization step. Building upon these foundations, in this paper, we present iDb-RRT, a sampling-based kinodynamic motion planning algorithm that combines motion primitives and trajectory optimization within the RRT framework. iDb-RRT is probabilistically complete and can be implemented in forward or bidirectional mode.

## Introduction

Kinodynamic motion planning is a fundamental problem in robotics where the goal is to find collision-free trajectories in high-dimensional, continuous, and non-convex spaces, while also considering actuation limits and dynamics of the robot. Over the last two decades, a wide variety of sampling-, search-, and optimization-based methods have been proposed to address (kinodynamic) motion planning problems.

Alternative approaches for kinodynamic motion planning are optimization-based methods, which scale polynomially instead of exponentially but require an initial guess and may fail to converge; and search-based methods, which provide strong theoretical guarantees but require a pre-defined discretization of the state or control space. More recently, hybrid methods have been proposed to merge the strengths of the three previous approaches to kinodynamic motion planning.

In this paper, we combine the strengths of the exploration of RRT with the concept of discontinuities between motion primitives and trajectory optimization. We present iDb-RRT (iterative Discontinuity-bounded RRT), a new kinodynamic motion planning algorithm that builds on the ideas of allowing discontinuities in an initial motion from iDb-A\*, and integrates the RRT exploration strategy with short motion primitives and trajectory optimization. iDb-RRT samples a random configuration, then expands the configuration that is closest using applicable motion primitives with bounded discontinuity.

## Limitations and future work

The main limitation of iDb-RRT, similar to iDb-A⁢, lies in its scalability to higher-dimensional systems. As the dimensionality increases, the number of motion primitives required to cover the state space with a small discontinuity grows exponentially. This issue can be partially mitigated by planning with larger discontinuities. In our benchmark, we successfully scaled to 13-DOF for the Quadrotor and 8-DOF for Rotor pole, thanks to leveraging translation invariance and the second-order linear velocity invariance of the dynamics.
