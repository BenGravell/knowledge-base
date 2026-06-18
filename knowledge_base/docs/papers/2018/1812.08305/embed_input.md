Derivative-Free Methods for Policy Optimization: Guarantees for Linear Quadratic Systems

Topics include Optimization, Derivative-free, Policy optimization.

We study derivative-free methods for policy optimization over the class of linear policies. We focus on characterizing the convergence rate of these methods when applied to linear-quadratic systems, and study various settings of driving noise and reward feedback. We show that these methods provably converge to within any pre-specified tolerance of the optimal policy with a number of zero-order evaluations that is an explicit polynomial of the error tolerance, dimension, and curvature properties of the problem. Our analysis reveals some interesting differences between the settings of additive driving noise and random initialization, as well as the settings of one-point and two-point reward feedback. Our theory is corroborated by extensive simulations of derivative-free methods on these systems. Along the way, we derive convergence rates for stochastic zero-order optimization algorithms when applied to a certain class of non-convex problems.

## Introduction

Recent years have witnessed a number of successes in applying modern reinforcement learning (RL) methods to many fields, including robotics and competitive gaming. Impressively, most of these successes have been achieved by using general-purpose RL methods that are applicable to a host of problems.

A literature that is closely related to model-free RL is that of *zero-order or derivative-free* methods for stochastic optimization; see the book by for an overview. Here, the goal is to optimize an unknown function from noisy observations of its values at judiciously chosen points. While most analytical results in this space apply to convex optimization, many of the procedures themselves rely on moving along randomized approximations to the directional derivatives of the function being optimized, and are thus applicable even to non-convex problems.

## Discussion

In this paper, we studied the model-free control problem over linear policies through the lens of derivative-free optimization. We derived quantitative convergence rates for various zero-order methods when applied to learn optimal policies based on data from noisy linear systems with quadratic costs. In particular, we showed that one-point and two-point variants of a canonical derivative-free optimization method achieve fast rates of convergence for the non-convex LQR problem.

While this paper analyzes a canonical zero-order optimization algorithm for model-free control of linear quadratic systems, many open questions remain. One such question concerns lower bounds for LQR problems in the model-free setting, thereby showing quantitative gaps between such a setting and that of model-based control. While we conjecture that the convergence bounds of Corollaries 1. ‣ 3.3 Consequences for LQR optimization ‣ 3 Main results"), 2. ‣ 3.3 Consequences for LQR optimization ‣ 3 Main results"), and 3.
