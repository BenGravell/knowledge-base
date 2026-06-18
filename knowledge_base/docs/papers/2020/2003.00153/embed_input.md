Learning near Optimal Policies with Low Inherent Bellman Error

Topics include Low-rank models, Reinforcement learning, Bellman equations, Value iteration, Bandits, Regret bounds, Online algorithms, Learning.

We study the exploration problem with approximate linear action-value functions in episodic reinforcement learning under the notion of low inherent Bellman error, a condition normally employed to show convergence of approximate value iteration. First we relate this condition to other common frameworks and show that it is strictly more general than the low rank (or linear) MDP assumption of prior work. Second we provide an algorithm with a high probability regret bound widetilde O(sum_t = 1^(H) d_t sqrt(K) + sum_t = 1^(H) sqrt(d_t) IBE K) where H is the horizon, K is the number of episodes, IBE is the value if the inherent Bellman error and d_t is the feature dimension at timestep t. In addition, we show that the result is unimprovable beyond constants and logs by showing a matching lower bound. This has two important consequences: 1) it shows that exploration is possible using only batch assumptions with an algorithm that achieves the optimal statistical rate for the setting we consider, which is more general than prior work on low-rank MDPs 2) the lack of closedness (measured by the inherent Bellman error) is only amplified by sqrt(d_t) despite working in the online setting....

## Introduction

Improving the sample efficiency of reinforcement learning (RL) algorithms through effective exploration-exploitation strategies is a major focus of the recent theoretical literature. Strong results are available with a generative model as well as in the *online* setting when the learning performance is measured by the cumulative regret, i.e., the difference between the performance of the optimal policy and the reward accumulated by the learner. For finite horizon problems, UCBVI achieves worst-case optimal regret, while algorithms with domain adaptive bounds have been introduced by and....

Approximate dynamic programming. While the results for tabular settings are encouraging, function approximation is normally required to tackle problems where the state or action spaces may be intractably large. In this case, even when the Bellman operator can be applied exactly, simple dynamic programming algorithms coupled with linear architectures may diverge, thus suggesting that effective approximate RL may not be feasible in the general case.

## Conclusion

We have introduced an algorithm for online exploration with linear approximators under the notion of low-inherent Bellman error with an optimal regret bound with regards to statistical rates and the lack of closedness of the Bellman operator. The construction reveals that a shift to global optimization might be unavoidable with more general linear approximators than prior low-rank work, making computational tractability harder to achieve....

Although Eleanor is proved to be near optimal, it is difficult to implement the algorithm efficiently. This should not be seen as a fundamental barrier, however. The issue of computational tractability arises even for tabular problems, but of course the problem is more pronounced when function approximators are implemented, and even for low-rank MDPs the first regret result has been obtained at the expense of a practical algorithm. Fortunately, later work has made progress on the computational aspects for many of these settings. For now, we leave this to future work.

However, there exists an MPD and a linear approximator with feature extractor $\phi$ which satisfies the above display but there exists no $\psi_{t}$ such that LABEL:eqn:LinearMDPequations holds.
