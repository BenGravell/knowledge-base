Policy Gradient Search: Online Planning and Expert Iteration without Search Trees

Monte Carlo Tree Search (MCTS) algorithms perform simulation-based search to improve policies online. During search, the simulation policy is adapted to explore the most promising lines of play. MCTS has been used by state-of-the-art programs for many problems, however a disadvantage to MCTS is that it estimates the values of states with Monte Carlo averages, stored in a search tree; this does not scale to games with very high branching factors. We propose an alternative simulation-based search method, Policy Gradient Search (PGS), which adapts a neural network simulation policy online via policy gradient updates, avoiding the need for a search tree. In Hex, PGS achieves comparable performance to MCTS, and an agent trained using Expert Iteration with PGS was able defeat MoHex 2.0, the strongest open-source Hex agent, in 9x9 Hex.

## Introduction

The value of Monte Carlo Tree Search (MCTS) for achieving maximal test-time performance in games such as Go and Hex has long been known. More recent works have also shown that incorporating planning into the training of reinforcement learning (RL) agents with Expert Iteration (ExIt) allows a pure RL approach to achieve state-of-the-art performance tabula rasa in many classical board games.

However, MCTS builds an explicit search tree, storing visit counts and value estimates at each node - in other words, creating a tabular value function. To be effective, this requires that nodes in the search tree are visited multiple times. This is true in many classical board games, but many real world problems have large branching factors that make MCTS hard to use. Large branching factors can be caused by very large action spaces, or chance nodes. In the case of large action spaces, a prior policy can be used to discount weak actions, reducing the effective branching factor....

The results presented in this work are on the deterministic, discrete action space domain of Hex. This allowed for direct comparison to MCTS, but the most exciting potential applications of PGS are to problems where MCTS cannot be readily used, such as problems with stochastic state transitions or continuous action spaces. We leave extending PGS and PGS-ExIt to such domains to future work.

The implementation of PGS presented in this work is in some ways rudimentary, using vanilla REINFORCE with stochastic gradient descent. Policy gradient algorithms for model-free RL have benefited from the use of more advanced optimisation algorithms such as ADAM, and enhancements such as PPO. Similar techniques might also improve the performance of PGS.

During search, the input distribution is substantially changed to consist of many highly correlated states. Using mini-batch statistics for batch normalisation therefore results in a large shift in the policy. So during PGS we freeze the parameters for batch normalisation, and calculate the normalisation using population rather than mini-batch statistics, as is usual for inference.

Policy Gradient Search works by applying a model-free RL algorithm to adapt the simulations in Monte Carlo Search. We will assume that a prior policy $\pi$ and a prior value function $V$ are provided, which have been trained on the full MDP.

### Results
