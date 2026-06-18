Second-Order Constrained Dynamic Optimization

Topics include Differential dynamic programming, Second-order methods, Constrained optimization, Trajectory optimization.

Comparative study over the variations of differential dynamic programming for constrained trajectory optimization problems, including interior-point, augmented Lagrangian, primal-dual, and sequential quadratic programming techniques.

This paper provides an overview, analysis, and comparison of second-order dynamic optimization algorithms, i.e., constrained Differential Dynamic Programming (DDP) and Sequential Quadratic Programming (SQP). Although a variety of these algorithms have been proposed and used successfully, there exists a gap in understanding the key differences and advantages, which we aim to provide in this work. For constrained DDP, we choose methods that incorporate nonlinear programming techniques to handle state and control constraints, including Augmented Lagrangian (AL), Interior Point, Primal-Dual Augmented Lagrangian (PDAL), and Alternating Direction Method of Multipliers (ADMM). Both DDP and SQP are provided in single- and multiple-shooting formulations, where constraints that arise from dynamics are encoded implicitly and explicitly, respectively. As a byproduct of the review, we propose a single-shooting PDAL DDP that has more favorable properties than the standard AL variant, such as the robustness to the growth of penalty parameters.

## Introduction

Second-order dynamic optimization methods are powerful optimization techniques used for optimal control of systems with nonlinear dynamics and non-quadratic cost functions. Dynamic systems with these characteristics can be found in robotics, aerospace and transportation systems, economics, biology and computational neuroscience, etc. There exist two main families of methods for dynamic optimization, namely Differential Dynamic Programming (DDP) and Sequential Quadratic Programming (SQP).

## Differential Dynamic Programming

Using Bellman's principle of optimality, dynamic programming (DP) divides the original optimization problem into a sequence of smaller subproblems at each time step. Nevertheless, DP is known to suffer from "curse of dimensionality" because its computational and memory demands explode as the dimension of the problem increases. DDP solves this issue by considering a local approximation around the nominal trajectory. Moreover, DDP can implicitly satisfy dynamic constraints thanks to its backward and forward nature. Furthermore, DDP provides feedback gains as a byproduct of optimization.

In practical applications, state and control constraints are of great importance. These include actuation limits and obstacles in robotics and autonomy, flow constraints in transportation systems, and positivity constraints in biology and computational neuroscience. To handle these constraints, variants of DDP have been extensively studied in the literature. In early work, active constraints were captured in the value and state-action $Q$ function during the backward pass of DDP.

## Conclusion

In this paper, we have reviewed two families of algorithms for constrained dynamic optimization: constrained DDP derived based on NLP techniques and SQP for dynamical systems. We have also discussed two distinct representations of these methods, namely, single- and multiple-shooting formulations. In addition, we derived a novel single-shooting PDAL DDP and added it to the comparison.
