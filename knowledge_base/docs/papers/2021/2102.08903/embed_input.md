Provably Efficient Policy Optimization for Two-Player Zero-Sum Markov Games

Policy-based methods with function approximation are widely used for solving two-player zero-sum games with large state and/or action spaces. However, it remains elusive how to obtain optimization and statistical guarantees for such algorithms. We present a new policy optimization algorithm with function approximation and prove that under standard regularity conditions on the Markov game and the function approximation class, our algorithm finds a near-optimal policy within a polynomial number of samples and iterations. To our knowledge, this is the first provably efficient policy optimization algorithm with function approximation that solves two-player zero-sum Markov games.

## Introduction

Two-player zero-sum Markov game is a popular setting with many applications, such as Go, StarCraft II, and poker. In this setting, the goal of player one is to find a policy that achieves the maximum reward against player two who plays optimally to minimize the reward in response to player one's policy.

Policy optimization methods are widely used for solving zero-sum games. These algorithms often constrain the policy in a parametric form, and compute the gradient of the cumulative reward with respect to the parameters using the policy gradient theorem or its variants to update the parameters iteratively. Due to its flexibility, a wide range of successful results are attained by policy optimization methods. For example, Lockhart et al. performed direct policy optimization against worst-case opponents and empirically demonstrate their effectiveness in Kuhn Poker and Goofspiel card game. Foerster et al....

## Conclusion

This paper gave the first quantitative analysis of policy gradient methods for general two-player zero-sum Markov games with function approximation. We quantified the performance gap of the output policy in terms of the number of iterations, number of samples, concentrability coefficients, and approximation error. An interesting direction is to extend our results to more advanced PG methods such as PPO.

The second quantity measures how well a parameterized class can approximate in terms of a metric.

Since we are considering a learning problem, we need to collect samples from the environment. We assume we can stop and restart at any time. With this, we can have the following sampling oracle.

After obtaining $x^{k}$ from Greedy Step, the Iteration Step aims to evaluate the value function while fixing $x = x^{k}$. We run $T$ updates to find $f^{\ast} = {\arg{\min_{f}V^{x,f}}}$. In the competitive multi-agent RL literature, this step is equivalent to finding the *best response* of min player (namely, $f^{\ast}$) when fixing $x = x^{k}$. The intuition is that when the max player's policy is very close to its optimal policy at NE and $f$ takes $f^{\ast}$, their accumulative value function is also close to $V^{\ast}$ at NE. This step can be viewed as running NPG for a single-agent RL problem.

Despite the large body of empirical work using policy optimization methods for two-player zero-sum Markov games, theoretical studies...
