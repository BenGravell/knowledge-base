Bandit Based Monte-Carlo Planning

Topics include Monte Carlo planning, Tree search, Bandit algorithms, Upper confidence bounds, Reinforcement learning, MDPs.

Introduces UCT, which applies upper-confidence bandit selection inside Monte Carlo tree search. The paper gives consistency and finite-sample analysis for planning in large MDPs and became a central ancestor of modern MCTS systems.

For large state-space Markovian Decision Problems Monte-Carlo planning is one of the few viable approaches to find near-optimal solutions. In this paper we introduce a new algorithm, UCT, that applies bandit ideas to guide Monte-Carlo planning. In finite-horizon or discounted MDPs the algorithm is shown to be consistent and finite sample bounds are derived on the estimation error due to sampling. Experimental results show that in several domains, UCT is significantly more efficient than its alternatives.
