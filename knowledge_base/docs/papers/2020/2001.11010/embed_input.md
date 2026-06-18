Automatic Repair of Convex Optimization Problems

Given an infeasible, unbounded, or pathological convex optimization problem, a natural question to ask is: what is the smallest change we can make to the problem's parameters such that the problem becomes solvable? In this paper, we address this question by posing it as an optimization problem involving the minimization of a convex regularization function of the parameters, subject to the constraint that the parameters result in a solvable problem. We propose a heuristic for approximately solving this problem that is based on the penalty method and leverages recently developed methods that can efficiently evaluate the derivative of the solution of a convex cone program with respect to its parameters. We illustrate our method by applying it to examples in optimal control and economics.

## Introduction

### Parametrized convex optimization

We consider parametrized convex optimization problems, which have the form

This idea is exploited by the Mosek \[13, §14.2\] and Gurobi solvers whenever a user would like to repair an infeasible or unbounded linear program. Automatic repair for linear programs appears to have been first suggested in. This was later studied more generally in the case of linear programs as irreducibly inconsistent systems (IIS), first defined in, with some further automated repair algorithms in, and in the more general case of linearly-constrained programs in.

The problem that we consider can also be interpreted as automatic program repair, where the program we are repairing solves a convex optimization problem. To the best of our knowledge, this paper is the first to consider automatic convex program repair.

where the proximal operator is defined as

with variables $t$, $x$, $y$, and $s$. This problem is guaranteed to be feasible since, for any $\theta \in \text{R}^{k}$, setting $x = 0$, $y = 0$, $s = 0$, and $t = {\|{({b{(\theta)}},{c{(\theta)}})}\|}_{2}$ yields a feasible point. The problem is also guaranteed to be bounded from below, since the objective is nonnegative. Taken together, this implies that problem always has a solution, assuming it is not pathological.

where $m > 0$ is the spacecraft mass, ${x{(t)}} \in \text{R}^{3}$ is the spacecraft position, ${f{(t)}} \in \text{R}^{3}$ is the force applied by the thruster, $g > 0$ is the gravitational acceleration, and $e_{3} = {}$.

### Solvable problems

We allow $p^{\star}$ to take on the extended values $\pm \infty$. Roughly speaking, we say that is *solvable* if $p^{\star}$ is finite and attainable. (We will define solvable formally below, when we canonicalize into a cone program.) When the problem is unsolvable, it falls into one of three cases: it is *infeasible* if $p^{\star} = {+ \infty}$, *unbounded below* if $p^{\star} = {- \infty}$, and *pathological* if $p^{\star}$ is finite, but not attainable by any $x$, or strong duality does not hold for. Unsolvable problems are often undesirable since, in many cases, there does not exist a solution.

### Performance metric

The goal in this paper is to repair an unsolvable problem by adjusting the parameter $\theta$ so that it becomes solvable....
