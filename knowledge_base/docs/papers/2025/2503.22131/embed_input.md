Newton-PIPG: A Fast Hybrid Algorithm for Quadratic Programs in Optimal Control

We propose Newton-PIPG, an efficient method for solving quadratic programming (QP) problems arising in optimal control, subject to additional set constraints. Newton-PIPG integrates the Proportional-Integral Projected Gradient (PIPG) method with the Newton method, thereby achieving both global convergence and local quadratic convergence. The PIPG method, an operator-splitting algorithm, seeks a fixed point of the PIPG operator. Under mild assumptions, we demonstrate that this operator is locally smooth, enabling the application of the Newton method to solve the corresponding nonlinear fixed-point equation. Furthermore, we prove that the linear system associated with the Newton method is locally nonsingular under strict complementarity conditions. To enhance efficiency, we design a specialized matrix factorization technique that leverages the typical sparsity of optimal control problems in such systems. Numerical experiments demonstrate that Newton-PIPG achieves high accuracy and reduces computation time, particularly when feasibility is easily guaranteed.

## Introduction

The development of techniques for solving Quadratic programming (QP) problems is a key enabler for advancing optimal control research, as efficiently solving these problems is often essential and a bottleneck in real-world optimal control applications. For example, Model Predictive Control (MPC), a framework for implementing optimal control, often relies on solving a series of QP problems. In addition, Sequential Convex Programming (SCP), a widely used algorithm for nonlinear optimal control, also relies on solving QP problems....

We consider the following QP problem, which includes additional set constraints and frequently arises in optimal control applications:\

In conclusion, we introduced the Newton-PIPG method for solving optimal control QP problems, which combines an operator splitting method, PIPG, with second-order Newton steps. We demonstrated the convergence of this algorithm and provided an efficient technique for solving the linear system in the Newton step. Our numerical experiments showed that our algorithm performs well compared to other state-of-the-art algorithms in solving quadratic optimal control problems.

For future research, we will incorporate infeasibility detection for Newton-PIPG and extend our algorithm to handle more general constraints. Additionally, the current Newton-PIPG software is written in Matlab, and we expect that a pure C/C++ implementation could further reduce computation time.

Under Assumptions 3.3, 3.3, and 3.14, $I - {J_{T}{(z,w)}}$ is a smooth function of $(z,w)$ in a local neighborhood of $(z^{\star},w^{\star})$, the fixed point of the PIPG operator. Moreover, $I - {J_{T}{(z,w)}}$ is smooth for $(z,w)$ in that neighborhood.

On the other hand, since projections are Lipschitz functions with Lipschitz constants equal to one \[, Exercise 7.5\], all eigenvalues of $J{(z)}$ need to be less than or equal to one. Otherwise, we would have

If ${Fix}{(T)}$ is nonempty, we plug in arbitrary $y$ from this fixed point set. Since $y \in {{Fix}{(\overset{\sim}{T})}}$ as well, we have

Additionally, we require that both $H_{E}$ and $H_{I}$ follows the pattern below:

The sparsity patterns of $H_{E}$ and $H_{I}$ are typical for optimal control optimization problems. These matrices define equality and inequality constraints among consecutive time points, while the set ${\mathbb{D}}_{ij}$ includes...
