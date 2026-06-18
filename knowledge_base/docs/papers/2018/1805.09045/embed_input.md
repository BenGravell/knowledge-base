When Simple Exploration Is Sample Efficient: Identifying Sufficient Conditions for Random Exploration to Yield PAC RL Algorithms

Topics include Reinforcement learning, Benchmarks, Sample complexity, Learning, Efficient.

Efficient exploration is one of the key challenges for reinforcement learning (RL) algorithms. Most traditional sample efficiency bounds require strategic exploration. Recently many deep RL algorithms with simple heuristic exploration strategies that have few formal guarantees, achieve surprising success in many domains. These results pose an important question about understanding these exploration strategies such as e-greedy, as well as understanding what characterize the difficulty of exploration in MDPs. In this work we propose problem specific sample complexity bounds of Q learning with random walk exploration that rely on several structural properties. We also link our theoretical results to some empirical benchmark domains, to illustrate if our bound gives polynomial sample complexity in these domains and how that is related with the empirical performance.

## Introduction

An important challenge for reinforcement learning is to balance exploration and exploitation. There have been many strategic exploration algorithms, yet many of the recent successes in deep reinforcement learning rely on algorithms with simple exploration mechanisms. While some of these approaches also require many samples, this still highlights an important question: when is exploration easy?

Rather than focusing on new algorithmic contributions, in this paper we seek to explore sufficient conditions on the domains that ensure that random exploration then exploitation methods will quickly lead to high performance, as formalized by satisfying the PAC criteria. Our work is related to recent work which considered structural properties of Markov decision processes that bound the loss when performing shallow planning: in contrast to their work, our work focused on the structural properties of MDPs that enable simple exploration to quickly enable good performance during learning.

As our main contribution, we introduce new structural properties of MDPs, and prove that when these parameters scales with a polynomial function of the domain parameters, then a random explore then exploit approach is PAC. Our key properties are $\phi{(s)}$, a state's stationary occupancy distribution under random walk, and eigenvalues of a graph Laplacian. Though making an assumption of the occupancy distribution under a random walk might seem to be presuming the conclusion, we note that this assumption only applies to the asymptotic, stationary distribution but our result yields finite sample bounds.

## Conclusion

In this paper we present several structural properties of MDPs that give upper bound on the sample complexity of $Q$ learning with random exploration followed by exploitation. We also link these properties to some conceptual testing domains as well as empirical benchmark domains, towards understanding the recent empirical success. We hope the knowledge of these properties might help guide practitioners in selecting exploration strategy, and understanding whether and when strategic exploration is necessary.
