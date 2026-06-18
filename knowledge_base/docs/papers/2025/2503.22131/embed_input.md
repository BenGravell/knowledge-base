Newton-PIPG: A Fast Hybrid Algorithm for Quadratic Programs in Optimal Control

We propose Newton-PIPG, an efficient method for solving quadratic programming (QP) problems arising in optimal control, subject to additional set constraints. Newton-PIPG integrates the Proportional-Integral Projected Gradient (PIPG) method with the Newton method, thereby achieving both global convergence and local quadratic convergence. The PIPG method, an operator-splitting algorithm, seeks a fixed point of the PIPG operator. Under mild assumptions, we demonstrate that this operator is locally smooth, enabling the application of the Newton method to solve the corresponding nonlinear fixed-point equation. Furthermore, we prove that the linear system associated with the Newton method is locally nonsingular under strict complementarity conditions. To enhance efficiency, we design a specialized matrix factorization technique that leverages the typical sparsity of optimal control problems in such systems. Numerical experiments demonstrate that Newton-PIPG achieves high accuracy and reduces computation time, particularly when feasibility is easily guaranteed.

## Introduction

The development of techniques for solving Quadratic programming (QP) problems is a key enabler for advancing optimal control research, as efficiently solving these problems is often essential and a bottleneck in real-world optimal control applications. For example, Model Predictive Control (MPC), a framework for implementing optimal control, often relies on solving a series of QP problems. In addition, Sequential Convex Programming (SCP), a widely used algorithm for nonlinear optimal control, also relies on solving QP problems.

We consider the following QP problem, which includes additional set constraints and frequently arises in optimal control applications:\

Additionally,

Widely used methods for solving Problem fall into two primary categories: second-order methods and operator-splitting methods, each with their own advantages and disadvantages. Second-order methods, such as interior-point methods and active-set methods, utilize the curvature information of the optimization problem. These methods typically converge in a modest number of iterations and are robust when the problem approaches infeasibility. Commonly used software in this category includes MOSEK, Gurobi, and ECOS. For further theoretical discussions on second-order methods, we refer the reader to.

Another approach to solving Problem is the operator-splitting method, which constructs an update operator applied at each iteration, ensuring that the iterations converge to the fixed point of this operator. Unlike interior-point methods, operator-splitting methods eliminate the need for matrix factorization, resulting in significantly lower per-iteration computational costs. Additionally, these methods do not require external parsers and are typically implemented with a smaller codebase. For a comprehensive review of operator-splitting methods, see.

## Conclusion and Future Work

In conclusion, we introduced the Newton-PIPG method for solving optimal control QP problems, which combines an operator splitting method, PIPG, with second-order Newton steps. We demonstrated the convergence of this algorithm and provided an efficient technique for solving the linear system in the Newton step. Our numerical experiments showed that our algorithm performs well compared to other state-of-the-art algorithms in solving quadratic optimal control problems.
