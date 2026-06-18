Stochastic Recursive Momentum for Policy Gradient Methods

Topics include Sample complexity, Policy gradients, STORM-PG.

In this paper, we propose a novel algorithm named STOchastic Recursive Momentum for Policy Gradient (STORM-PG), which operates a SARAH-type stochastic recursive variance-reduced policy gradient in an exponential moving average fashion. STORM-PG enjoys a provably sharp O(1/epsilon^) sample complexity bound for STORM-PG, matching the best-known convergence rate for policy gradient algorithm. In the mean time, STORM-PG avoids the alternations between large batches and small batches which persists in comparable variance-reduced policy gradient methods, allowing considerably simpler parameter tuning. Numerical experiments depicts the superiority of our algorithm over comparative policy gradient algorithms.

## Introduction

Reinforcement Learning (RL) is a dynamic learning approach that interacts with the environment and execute actions according to the current state, so that a particular measure of cumulative rewards is maximized. Model-free deep reinforcement learning algorithms have achieved remarkable performance in a range of challenging tasks, including stochastic control, autonomous driving, games, continuous robot control tasks, etc.

Generally, there are two aspects of methods of solving a model-free RL problem: value-based methods such as Q-Learning, SARSA, etc., as well as policy-based methods such as Policy Gradient (PG) algorithm. PG algorithm models the state-to-action transition probabilities as a parameterized family, and the cumulative rewards can be regarded as a function of the parameters. Thus, policy gradient based problem shares a formulation that is analogous to the traditional stochastic optimization problem.

## Final Remarks

In this paper, we propose a new STORM-PG algorithm that adopts a recently proposed variance-reduced gradient method called STORM. STORM-PG enjoys advantage both theoretically and experimentally. From the final experimental results, our STORM-PG algorithm is significantly better than all other baseline methods, both in aspects of training stability and parameter tuning (the user time of tuning STORM-PG is much shorter)....

### Lemma 6 (Lemma A.1 in )

When $\alpha = 1$, the STORM-PG estimator reduces to the vanilla stochastic gradient estimator and when $\alpha = 0$, the STORM-PG esimator reduces to the SARAH estimator. As our $\alpha$ is chosen between $$, the estimator is a combination of an variance reduced biased estimator and an unbiased estimator. In addition, can be rewritten as

The detailed analysis of the convergence rate is shown in the next section. Corollary 12 is a direct result after Theorem 11. By controlling the estimated gradient to be in the $\epsilon$-neighborhood of 0, and minimizing $S_{0}$, we get the IFO complexity bound of STORM-PG algorithm:

One critical challenge of reinforcement learning algorithms compared to traditional gradient based algorithms lies on the issue of distribution shift, that is, the data sample distribution encounters distributional changes throughout the learning dynamics....
