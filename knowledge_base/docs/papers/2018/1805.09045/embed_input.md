When Simple Exploration Is Sample Efficient: Identifying Sufficient Conditions for Random Exploration to Yield PAC RL Algorithms

Topics include Reinforcement learning, Benchmarks, Sample complexity, Learning, Efficient.

Efficient exploration is one of the key challenges for reinforcement learning (RL) algorithms. Most traditional sample efficiency bounds require strategic exploration. Recently many deep RL algorithms with simple heuristic exploration strategies that have few formal guarantees, achieve surprising success in many domains. These results pose an important question about understanding these exploration strategies such as e-greedy, as well as understanding what characterize the difficulty of exploration in MDPs. In this work we propose problem specific sample complexity bounds of Q learning with random walk exploration that rely on several structural properties. We also link our theoretical results to some empirical benchmark domains, to illustrate if our bound gives polynomial sample complexity in these domains and how that is related with the empirical performance.

## Introduction

An important challenge for reinforcement learning is to balance exploration and exploitation. There have been many strategic exploration algorithms, yet many of the recent successes in deep reinforcement learning rely on algorithms with simple exploration mechanisms. While some of these approaches also require many samples, this still highlights an important question: when is exploration easy?...

Some restrictions on the decision process are needed: there exist challenging Markov decision processes where relying on random exploration will require an exponential bound (in the MDP parameters) on the sample complexity, in contrast to the polynomial dependence required for the algorithm to be PAC. In some such domains, like the combination lock setting), any greedy actions will (for a very long time) cause the agent to undo productive exploration towards finding the optimal policy, and therefore $\epsilon$-greedy (for any $\epsilon$) will be no better and likely worse than random exploration, and therefore will also not have PAC...

## Conclusion

In this paper we present several structural properties of MDPs that give upper bound on the sample complexity of $Q$ learning with random exploration followed by exploitation. We also link these properties to some conceptual testing domains as well as empirical benchmark domains, towards understanding the recent empirical success. We hope the knowledge of these properties might help guide practitioners in selecting exploration strategy, and understanding whether and when strategic exploration is necessary.

where $\Phi$ is a diagonal matrix with entries ${\Phi{(s,s)}} = {\phi{(s)}}$. Usually the graph Laplacian is only defined on undirected graph, and the intuition in is that take the average of transition matrix $P$ and its transpose to define an undirected graph, then normalized the transition matrix, to introduce the Laplacian for weighted directed graph. The smallest eigenvalue of Laplacian $\mathcal{L}$ is zero. Let $\lambda$ be the smallest non-zero eigenvalue. In the following theorem, we will bound the covering time of random walk policy by the eigenvalues of $\mathcal{L}$ and the stationary distribution $\phi$.

The covering length, denoted by $L$, is the number of time steps we need to visit all state-action pairs at least once with probability at least $1/2$, starting from any $(s,a)$.
