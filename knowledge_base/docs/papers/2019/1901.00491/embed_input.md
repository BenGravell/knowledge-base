Optimal Control of the Double Integrator with Minimum Total Variation

Topics include Optimal control, Control, Control variable.

We study the well-known minimum-energy control of the double integrator, along with the simultaneous minimization of the total variation in the control variable. We derive the optimality conditions and obtain the unique optimal solution to the combined problem, where the initial and terminal boundary points are specified. We study the problem from a multi-objective optimal control viewpoint, constructing the Pareto front. We show that the unique asymptotic optimal control function, for the minimization of the total variation alone, is piecewise constant with one switching at the midpoint of the time horizon. For any instance of the boundary conditions of the problem, we prove that the asymptotic optimal total variation is exactly 2/3 of the total variation of the minimum-energy control. We illustrate the results for a particular instance of the problem and include a link to a video which animates the solutions while moving along the Pareto front.

## Introduction

The double integrator is a mathematical model for a point mass, typically idealizing a car in rectilinear motion on a flat and frictionless plane as schematically illustrated in Figure 1. It also constitutes a model for analogous rotational-mechanical and electrical systems. One should recall that a cubic curve between two oriented points, which minimizes its averaged acceleration, or more precisely, the $L^{2}$-norm of its acceleration, serves as a building block for cubic splines. This latter case can be represented as the energy-minimizing double integrator.

Due to its simplicity, optimal control of the double integrator is studied virtually in every course of lectures on optimal control theory. In the teaching of optimal control theory and its applications, although the minimum-energy, minimum-effort and minimum-time control of the double integrator are widely studied, minimization of total variation is not even considered, presumably because a maximum principle for the control minimizing its total variation does not exist.

It should be noted that the problem we have studied in the current paper fits into the above problem description (LQPTV) with $n = 2$, $m = 1$, $Q = 0$ and $R = 1$, and the appropriate constant system and control matrices $A$ and $B$.

The general linear quadratic problem is a convex problem, so the weighted-sum scalarization can still be used (see ) when it is combined with the minimization of total variation. However, for a generalization to nonconvex problems, a scalarization different from the weighted-sum scalarization needs to be considered. This requires specialized numerical techniques in obtaining a solution---see and the pertaining discussion therein for problems which also have constraints on the state and control variables.

### Multi-Objective Optimal Control

where $\alpha > 0$ is referred to as the weight. We assume that $u$ is absolutely continuous on $\lbrack 0,1\rbrack$, in other words, $u \in {W^{1,1}{({\lbrack 0,1\rbrack})}}$. Then we define the new control variable ${v{(t)}}:={\overset{˙}{u}{(t)}}$ for a.e. $t \in {\lbrack 0,1\rbrack}$. Using, Problem (Ptv) can now be reformulated by incorporating the new variable as

### Theorem 1 (Solution of Problem (Ptv))

\psfrag{u}{u(t)}\psfrag{x10}{x1 = s0}\psfrag{x1}{x1(t):= y(t)}\psfrag{x2}{x2(t):=...
