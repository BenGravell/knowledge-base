Stochastic Variance Reduction Methods for Policy Evaluation

Topics include Datasets, Benchmarks, Learning, Variance reduction, Saddle point, Reinforcement learning.

Policy evaluation is a crucial step in many reinforcement-learning procedures, which estimates a value function that predicts states' long-term value under a given policy. In this paper, we focus on policy evaluation with linear function approximation over a fixed dataset. We first transform the empirical policy evaluation problem into a (quadratic) convex-concave saddle point problem, and then present a primal-dual batch gradient method, as well as two stochastic variance reduction methods for solving the problem. These algorithms scale linearly in both sample size and feature dimension. Moreover, they achieve linear convergence even when the saddle-point problem has only strong concavity in the dual variables but no strong convexity in the primal variables. Numerical experiments on benchmark problems demonstrate the effectiveness of our methods.

## Introduction

Reinforcement learning (RL) is a powerful learning paradigm for sequential decision making. An RL agent interacts with the environment by repeatedly observing the current state, taking an action according to a certain policy, receiving a reward signal and transitioning to a next state. A policy specifies which action to take given the current state. *Policy evaluation* estimates a value function that predicts expected cumulative reward the agent would receive by following a fixed policy starting at a certain state....

There has been substantial work on policy evaluation, with *temporal-difference* (TD) methods being perhaps the most popular. These methods use the Bellman equation to bootstrap the estimation process. Different cost functions are formulated to exploit this idea, leading to different policy evaluation algorithms; see Dann et al. for a comprehensive survey. In this paper, we study policy evaluation by minimizing the mean squared projected Bellman error (MSPBE) with linear approximation of the value function. We focus on the batch setting where a fixed, finite dataset is given....

In this paper, we reformulated the EM-MSPBE minimization problem in policy evaluation into an empirical saddle-point problem, and developed and analyzed a batch gradient method and two first-order stochastic variance reduction methods to solve the problem. An important result we obtained is that even when the reformulated saddle-point problem lacks strong convexity in primal variables and has only strong concavity in dual variables, the proposed algorithms are still able to achieve a linear convergence rate. We are not aware of any similar results for primal-dual batch gradient methods or stochastic variance reduction methods....

This work leads to several interesting directions for research. First, we believe it is important to extend the stochastic variance reduction methods to nonlinear approximation paradigms, especially with deep neural networks. Moreover, it remains an important open problem how to apply stochastic variance reduction techniques to policy optimization.

Moreover, even if $\rho > 0$, it will be inefficient to solve problem using primal-dual algorithms based on proximal mappings of the strongly convex and concave terms....
