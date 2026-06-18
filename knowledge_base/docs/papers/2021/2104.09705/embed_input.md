Neural Tree Expansion for Multi-Robot Planning in Non-Cooperative Environments

Topics include Robotics, Neural networks, Real-time systems, Online algorithms, Planning, Control, Monte Carlo methods, Neural tree expansion, NTE, Monte Carlo tree search.

We present a self-improving, Neural Tree Expansion (NTE) method for multi-robot online planning in non-cooperative environments, where each robot attempts to maximize its cumulative reward while interacting with other self-interested robots. Our algorithm adapts the centralized, perfect information, discrete-action space method from AlphaZero to a decentralized, partial information, continuous action space setting for multi-robot applications. Our method has three interacting components: (i) a centralized, perfect-information "expert" Monte Carlo Tree Search (MCTS) with large computation resources that provides expert demonstrations, (ii) a decentralized, partial-information "learner" MCTS with small computation resources that runs in real-time and provides self-play examples, and (iii) policy & value neural networks that are trained with the expert demonstrations and bias both the expert and the learner tree growth. Our numerical experiments demonstrate Neural Tree Expansion's computational advantage by finding better solutions than a MCTS with 20 times more resources....

## Introduction

Multi-agent interactions in non-cooperative environments are ubiquitous in robotic applications such as self-driving, space exploration, urban air mobility, and human-robot collaboration. Planning, or sequential decision-making, in these settings requires a prediction model of the other agents, which can be generated through a game theoretic framework.

Recently, the success of AlphaZero at the game of Go has popularized a self-improving machine learning algorithm: bias a Monte Carlo Tree Search with value and policy neural networks, use the tree statistics to train the networks with supervised learning and then iterate over these two steps to improve the policy and value networks over time. However, this algorithm is designed for classical artificial intelligence tasks (e.g. chess or Go), and applications in multi-robot domains require different assumptions: continuous state-action, decentralized evaluation, partial information, and limited computational resources....

## Conclusion

We present a new approach for multi-robot planning in non-cooperative environments with an iterative search and learning method called Neural Tree Expansion. Our method bridges the gap between an AlphaZero-like method and real-world robotics applications by introducing a learner agent with decentralized evaluation, partial information, and limited computational resources. Our method outperforms the current state-of-the-art analytical baseline for the multi-robot double-integrator Reach-Target-Avoid game with dynamically sophisticated and coordinated strategies....

In order to specify the expert and learner policies, we first explain their common search tree algorithm shown in Algorithm 2 and adapted from to our setting. For a complete treatment of MCTS, we refer the reader to.

For each robot $i$ on team $A$ (${\forall i} \in \mathcal{I}_{A}$), the admissible state space has an additional constraint: avoid the robots on team $B$ by at least the tag radius:

Value Network: The value network is used to gather reward statistics in place of a policy rollout, and is called in the DefaultPolicy in Lines 2--2 of Algorithm 2. The value network uses an alternative state representation to be compatible with the estimated state for local computation:

Figure 1: We propose an AlphaZero-like method for multi-robot applications such as the Reach-Target-Avoid game....
