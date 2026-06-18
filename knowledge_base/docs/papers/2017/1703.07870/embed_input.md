General Heuristics for Nonconvex Quadratically Constrained Quadratic Programming

We introduce the Suggest-and-Improve framework for general nonconvex quadratically constrained quadratic programs (QCQPs). Using this framework, we generalize a number of known methods and provide heuristics to get approximate solutions to QCQPs for which no specialized methods are available. We also introduce an open-source Python package QCQP, which implements the heuristics discussed in the paper.

## Introduction

In this paper we introduce the *Suggest-and-Improve* heuristic framework for general nonconvex quadratically constrained quadratic programs (QCQPs). This framework can be applied to general QCQPs for which there are no available specialized methods. We only briefly mention global methods for solving QCQPs in §1.4, as the exponential running time of these methods makes them unsuitable for medium- to large-scale problems. Our main focus, instead, will be on polynomial-time methods for obtaining approximate solutions.

## Quadratically constrained quadratic programming

A

where $x \in \text{R}^{n}$ is the optimization variable, and $P_{i} \in \text{R}^{n \times n}$, $q_{i} \in \text{R}^{n}$, $r_{i} \in \text{R}$ are given problem data, for $i = {0,1,\ldots,m}$. Throughout the paper, we will use $f^{\star}$ to denote the optimal value of, and $x^{\star}$ to denote an optimal point, i.e., that attains the objective value of $f^{\star}$, while satisfying all the constraints. For simplicity, we assume that all $P_{i}$ matrices are symmetric, but we do not assume any other conditions such as definiteness. This means that, in general, is a nonconvex optimization problem.

The constraint ${f_{i}{(x)}} \leq 0$ is affine if $P_{i} = 0$. If we need to handle affine constraints differently from quadratic ones, we collect all affine constraints and explicitly write them as a single inequality ${Ax} \leq b$, where $A \in \text{R}^{p \times n}$ and $b \in \text{R}^{p}$ are of appropriate dimensions, and the inequality $\leq$ is elementwise.
