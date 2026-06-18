Automatic Repair of Convex Optimization Problems

Given an infeasible, unbounded, or pathological convex optimization problem, a natural question to ask is: what is the smallest change we can make to the problem's parameters such that the problem becomes solvable? In this paper, we address this question by posing it as an optimization problem involving the minimization of a convex regularization function of the parameters, subject to the constraint that the parameters result in a solvable problem. We propose a heuristic for approximately solving this problem that is based on the penalty method and leverages recently developed methods that can efficiently evaluate the derivative of the solution of a convex cone program with respect to its parameters. We illustrate our method by applying it to examples in optimal control and economics.

## Parametrized convex optimization

We consider parametrized convex optimization problems, which have the form

## Solvable problems

We allow $p^{\star}$ to take on the extended values $\pm \infty$. Roughly speaking, we say that is *solvable* if $p^{\star}$ is finite and attainable. (We will define solvable formally below, when we canonicalize into a cone program.) When the problem is unsolvable, it falls into one of three cases: it is *infeasible* if $p^{\star} = {+ \infty}$, *unbounded below* if $p^{\star} = {- \infty}$, and *pathological* if $p^{\star}$ is finite, but not attainable by any $x$, or strong duality does not hold . Unsolvable problems are often undesirable since, in many cases, there does not exist a solution.

## Performance metric

The goal in this paper is to repair an unsolvable problem by adjusting the parameter $\theta$ so that it becomes solvable. We will judge the desirability of a new parameter $\theta$ by a (convex) performance metric function $r:{\text{R}^{k}\rightarrow{\text{R} \cup {\{{+ \infty}\}}}}$, which we would like to be small. (Infinite values of $r$ denote constraints on the parameter.) A simple example of $r$ is the Euclidean distance to an initial parameter vector $\theta_{0}$, or ${r{(\theta)}} = {\|{\theta - \theta_{0}}\|}_{2}$.

## Repairing a convex optimization problem

In this paper, we consider the problem of repairing a convex optimization problem, as measured by the performance metric, by solving the problem
