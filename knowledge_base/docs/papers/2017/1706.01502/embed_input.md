UCB Exploration via Q-Ensembles

We show how an ensemble of Q^*-functions can be leveraged for more effective exploration in deep reinforcement learning. We build on well established algorithms from the bandit setting, and adapt them to the Q-learning setting. We propose an exploration strategy based on upper-confidence bounds (UCB). Our experiments show significant gains on the Atari benchmark.

## Introduction

Deep reinforcement learning seeks to learn mappings from high-dimensional observations to actions. Deep $Q$-learning (Mnih et al. ) is a leading technique that has been used successfully, especially for video game benchmarks. However, fundamental challenges remain, for example, improving sample efficiency and ensuring convergence to high quality solutions. Provably optimal solutions exist in the bandit setting and for small MDPs, and at the core of these solutions are exploration schemes. However these provably optimal exploration techniques do not extend to deep RL in a straightforward way.

Bootstrapped DQN (Osband et al. ) is a previous attempt at adapting a theoretically verified approach to deep RL. In particular, it draws inspiration from *posterior sampling for reinforcement learning* (PSRL, Osband et al., Osband and Van Roy ), which has near-optimal regret bounds. PSRL samples an MDP from its posterior each episode and exactly solves $Q^{\ast}$, its optimal $Q$-function. However, in high-dimensional settings, both approximating the posterior over MDPs and solving the sampled MDP are intractable....

## Conclusion

We proposed a $Q$-ensemble approach to deep $Q$-learning, a computationally practical algorithm inspired by Bayesian reinforcement learning that outperforms Double DQN and bootstrapped DQN, as evaluated on Atari. The key ingredient is the UCB exploration strategy, inspired by bandit algorithms. Our experiments show that the exploration strategy achieves improved learning performance on the majority of Atari games.

We first derive a lower bound of the the posterior $\overset{\sim}{p}{(\left. Q_{k,{i + 1}} \middle| \tau \right.)}$:

### Bayesian update for ${\mathbf{Q}}^{\ast}$

We present Algorithm 2, which incorporates the UCB exploration. The hyperparemeter $\lambda$ controls the degrees of exploration. In Section 5, we compare the performance of our algorithms on Atari games using a consistent set of parameters.

In this paper, we design new algorithms that build on the $Q$-ensemble approach from Osband et al.. However, instead of using posterior sampling for exploration, we use the uncertainty estimates from the $Q$-ensemble. Specifically, we propose the UCB exploration strategy. This strategy is inspired by established UCB algorithms in the bandit setting and constructs uncertainty estimates of the $Q$-values....
