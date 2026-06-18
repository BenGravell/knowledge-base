PIQP: A Proximal Interior-Point Quadratic Programming Solver

This paper presents PIQP, a high-performance toolkit for solving generic sparse quadratic programs (QP). Combining an infeasible Interior Point Method (IPM) with the Proximal Method of Multipliers (PMM), the algorithm can handle ill-conditioned convex QP problems without the need for linear independence of the constraints. The open-source implementation is written in C++ with interfaces to C, Python, Matlab, and R leveraging the Eigen3 library. The method uses a pivoting-free factorization routine and allocation-free updates of the problem data, making the solver suitable for embedded applications. The solver is evaluated on the Maros-Mészáros problem set and optimal control problems, demonstrating state-of-the-art performance for both small and large-scale problems, outperforming commercial and open-source solvers.

## Introduction

Convex quadratic programs are fundamental in many areas of applied mathematics and engineering. They are utilized in various applications, including portfolio optimization, optimal control, state estimation, and geometry processing. Furthermore, QPs are a crucial building block of powerful optimization techniques, such as sequential quadratic programming for nonlinear programming and branch-and-bound methods for mixed integer quadratic programming....

In recent decades, significant research efforts have focused on developing efficient QP solvers. Numerous algorithms have been proposed, such as the classical active-set and interior-point methods, first-order and second-order Newton-type methods, to design QP solvers that achieve high computational efficiency and scalability. As one of the most classical QP approaches, active-set based solvers, such as qpOASES, are known for their speed in solving small to medium-sized problems and the ability to warm-start using an estimate of the active constraint set....

We include the Dolan-Moré performance profiles for the high accuracy settings in Figure 2. The x-axis of the graphs shows the solve time normalized by the fastest solver, with a performance ratio of one indicating that the solver was the fastest and a performance ratio of ten indicating that the solver was ten times slower than the fastest solver for a particular problem. The y-axis of the graphs shows the ratio of problems solved. For instance, PIQP was the fastest solver for 65% of the problems and took at most five times longer for 96% of the problems.

Figure 2: Performance profiles on the Maros-Mészáros problem set for high accuracy settings.

## Numerical Implementation

Next, we present the three main steps of the Mehrotra predictor-corrector method:

To ensure that the LDL factorization of any symmetric permutation of the KKT matrix exists, it is sufficient if $K$ is quasi-definite. Although adding terms to the diagonal of through the proximal method of multipliers typically ensures that $K$ is almost certainly quasi-definite, there may be rare instances when it is not. In such cases, we slightly perturb the regularization parameters and retry the factorization....
