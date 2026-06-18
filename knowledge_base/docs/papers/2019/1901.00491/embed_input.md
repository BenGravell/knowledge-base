Optimal Control of the Double Integrator with Minimum Total Variation

Topics include Optimal control, Control, Control variable.

We study the well-known minimum-energy control of the double integrator, along with the simultaneous minimization of the total variation in the control variable. We derive the optimality conditions and obtain the unique optimal solution to the combined problem, where the initial and terminal boundary points are specified. We study the problem from a multi-objective optimal control viewpoint, constructing the Pareto front. We show that the unique asymptotic optimal control function, for the minimization of the total variation alone, is piecewise constant with one switching at the midpoint of the time horizon. For any instance of the boundary conditions of the problem, we prove that the asymptotic optimal total variation is exactly 2/3 of the total variation of the minimum-energy control. We illustrate the results for a particular instance of the problem and include a link to a video which animates the solutions while moving along the Pareto front.

## Introduction

The double integrator is a mathematical model for a point mass, typically idealizing a car in rectilinear motion on a flat and frictionless plane as schematically illustrated in Figure 1. It also constitutes a model for analogous rotational-mechanical and electrical systems. One should recall that a cubic curve between two oriented points, which minimizes its averaged acceleration, or more precisely, the $L^{2}$-norm of its acceleration, serves as a building block for cubic splines. This latter case can be represented as the energy-minimizing double integrator.

Due to its simplicity, optimal control of the double integrator is studied virtually in every course of lectures on optimal control theory. In the teaching of optimal control theory and its applications, although the minimum-energy, minimum-effort and minimum-time control of the double integrator are widely studied, minimization of total variation is not even considered, presumably because a maximum principle for the control minimizing its total variation does not exist.

In this paper, we use a tutorial approach. First, in Section 2, we introduce the double integrator model as well as the problem of energy minimization as an optimal control problem. This is a standard problem in optimal control; so, we derive the optimal solution without going into details.

## Conclusion and Future Work

We have derived the unique solution to the optimal control problem of simultaneous minimization of energy and total variation in control for the double integrator. We obtained analytic expressions for the construction of the Pareto front. We have shown that the unique asymptotic optimal control function, for the minimization of the total variation alone, is piecewise constant with one switching at the midpoint of the time horizon. We computed the two constant levels of the asymptotic control function analytically.

The minimum-energy control problem which we have also considered is a special case of a general linear quadratic control problem. An approach similar to the one employed in the current paper can be employed for the more general linear quadratic control (or linear quadratic programming) problem where one is additionally concerned with the minimization of total variation, namely the problem
