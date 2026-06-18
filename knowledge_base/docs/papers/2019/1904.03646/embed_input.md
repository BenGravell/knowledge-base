Policy Gradient Search: Online Planning and Expert Iteration without Search Trees

Monte Carlo Tree Search (MCTS) algorithms perform simulation-based search to improve policies online. During search, the simulation policy is adapted to explore the most promising lines of play. MCTS has been used by state-of-the-art programs for many problems, however a disadvantage to MCTS is that it estimates the values of states with Monte Carlo averages, stored in a search tree; this does not scale to games with very high branching factors. We propose an alternative simulation-based search method, Policy Gradient Search (PGS), which adapts a neural network simulation policy online via policy gradient updates, avoiding the need for a search tree. In Hex, PGS achieves comparable performance to MCTS, and an agent trained using Expert Iteration with PGS was able defeat MoHex 2.0, the strongest open-source Hex agent, in 9x9 Hex.

## Introduction

The value of Monte Carlo Tree Search (MCTS) for achieving maximal test-time performance in games such as Go and Hex has long been known. More recent works have also shown that incorporating planning into the training of reinforcement learning (RL) agents with Expert Iteration (ExIt) allows a pure RL approach to achieve state-of-the-art performance tabula rasa in many classical board games.

In contrast, Monte Carlo Search (MCS) algorithms have no such requirement. Whereas MCTS uses value estimates in each node to adapt the simulation policy, MCS algorithms have a fixed simulation policy throughout the search. However, because MCS does not improve the quality of simulations during search, it produces significantly weaker play than MCTS.

To adapt simulation policies in problems where we don't visit states multiple times, we can search over a restricted version of the problem, where multiple visits to states do occur, or we can generalise knowledge between different states during search. We take the latter approach. To this end, we propose Policy Gradient Search (PGS) a search algorithm which trains its simulation policy during search using policy gradient RL. This gives the advantages of an adaptive simulation policy, without requiring an explicit search tree to be built.

Section 2 covers background material, and section 3 describes the PGS algorithm. In section 4 we assess the strength of PGS as a test-time decision maker, while in section 5 we show results from using PGS within ExIt. Sections 6 and 7 discuss connections to previous works and future directions.

## Discussion and Future Work

In this work, we have presented Policy Gradient Search, a search algorithm for online planning that does not require an explicit search tree. We have shown that PGS is an effective planning algorithm. In our tests, it was slightly weaker than, but competitive , MCTS, while significantly outperforming MCS for test-time decision making, in both 9x9 and 13x13 Hex.

PGS is also effective during training when used within the Expert Iteration framework, resulting in the first competitive Hex agent trained tabula rasa without use of a search tree. In contrast, similar Reinforce algorithm alone was previously been found to not be competitve with an ExIt algorithm that used MCTS experts.
