General Heuristics for Nonconvex Quadratically Constrained Quadratic Programming

We introduce the Suggest-and-Improve framework for general nonconvex quadratically constrained quadratic programs (QCQPs). Using this framework, we generalize a number of known methods and provide heuristics to get approximate solutions to QCQPs for which no specialized methods are available. We also introduce an open-source Python package QCQP, which implements the heuristics discussed in the paper.

## Introduction

In this paper we introduce the *Suggest-and-Improve* heuristic framework for general nonconvex quadratically constrained quadratic programs (QCQPs). This framework can be applied to general QCQPs for which there are no available specialized methods. We only briefly mention global methods for solving QCQPs in §1.4, as the exponential running time of these methods makes them unsuitable for medium- to large-scale problems. Our main focus, instead, will be on polynomial-time methods for obtaining approximate solutions.

### Quadratically constrained quadratic programming

The running time of the ADMM and penalty CCP *Improve* methods was heavily affected when they were unable to find feasible points. This issue can be addressed by specifying the maximum number of iterations performed by the methods, or prematurely terminating the methods when they reach a preset time limit.

Table 2: Objective value of the best point found (left), and total running time (right) of the Suggest-and-Improve heuristic on the secondary user multicast beamforming problem.

Lower bounds obtained from relaxations can be improved by adding additional quadratic inequalities to that are satisfied by any solution of the original problem. In particular, redundant inequalities that hold for all feasible points of can still tighten the relaxation. We note, however, that in order for these inequalities to be useful in practice, they must be computationally efficient to derive. For example, the inequality ${f_{0}{(x)}} \leq f^{\star}$ holds for every optimal point of the problem, but it cannot be added to the problem without knowing the value of $f^{\star}$....

First, we explore a relaxation of that is a generalized eigenvalue problem, hence the name *spectral relaxation*. This method generalizes eigenvalue bounds studied in. Let $\lambda \in \text{R}_{+}^{m}$ be an arbitrary vector in the nonnegative orthant, and consider the following optimization problem:

Formally, the penalty CCP method can be written as below.

A quadratically constrained quadratic program (QCQP) is an optimization problem that can be written in the following form:

where $x \in \text{R}^{n}$ is the optimization variable, and $P_{i} \in \text{R}^{n \times n}$, $q_{i} \in \text{R}^{n}$, $r_{i} \in \text{R}$ are given problem data, for $i = {0,1,\ldots,m}$....
