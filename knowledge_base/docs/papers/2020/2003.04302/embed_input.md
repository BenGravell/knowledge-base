Stochastic Recursive Momentum for Policy Gradient Methods

Topics include Sample complexity, Policy gradients, STORM-PG.

In this paper, we propose a novel algorithm named STOchastic Recursive Momentum for Policy Gradient (STORM-PG), which operates a SARAH-type stochastic recursive variance-reduced policy gradient in an exponential moving average fashion. STORM-PG enjoys a provably sharp O(1/epsilon^) sample complexity bound for STORM-PG, matching the best-known convergence rate for policy gradient algorithm. In the mean time, STORM-PG avoids the alternations between large batches and small batches which persists in comparable variance-reduced policy gradient methods, allowing considerably simpler parameter tuning. Numerical experiments depicts the superiority of our algorithm over comparative policy gradient algorithms.

## Introduction

Reinforcement Learning (RL) is a dynamic learning approach that interacts with the environment and execute actions according to the current state, so that a particular measure of cumulative rewards is maximized. Model-free deep reinforcement learning algorithms have achieved remarkable performance in a range of challenging tasks, including stochastic control, autonomous driving, games, continuous robot control tasks, etc.

Generally, there are two aspects of methods of solving a model-free RL problem: value-based methods such as Q-Learning, SARSA, etc., as well as policy-based methods such as Policy Gradient (PG) algorithm. PG algorithm models the state-to-action transition probabilities as a parameterized family, and the cumulative rewards can be regarded as a function of the parameters. Thus, policy gradient based problem shares a formulation that is analogous to the traditional stochastic optimization problem.

One critical challenge of reinforcement learning algorithms compared to traditional gradient based algorithms lies on the issue of distribution shift, that is, the data sample distribution encounters distributional changes throughout the learning dynamics.

The problem of high sample complexity arises frequently in policy gradient based methods due to a combined effect of high variance incurred during the training phase and distribution shift, limiting the ability of model-free deep reinforcement learning algorithms. Such a combined effect signals the potential need of adopting variance-reduced gradient estimators to accelerate off-policy algorithms. Recently proposed variance-reduced policy gradient methods include SVRPG and SRVRPG theoretically improve the sample efficiency over PG.

Nevertheless compared to the vanilla PG method, one major drawback of the aforementioned variance-reduced policy gradient methods is their alternations between large and small batches of trajectory samples, spelled as the restarting mechanism, so the variance can be effectively controlled. In this paper, we circumvent such a restarting mechanism by introducing a new algorithm named STOchastic Recursive Momentum Policy Gradient (STORM-PG), which utilizes the idea of a recently proposed variance-reduced gradient method STORM and blends with policy gradient methods.
