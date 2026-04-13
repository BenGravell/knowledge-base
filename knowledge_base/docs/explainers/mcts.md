# Monte Carlo Tree Search (MCTS)

*Monte Carlo Tree Search (MCTS)* is a lookahead planning algorithm that builds a search tree incrementally by simulating future trajectories and backing up value estimates. *Upper Confidence Tree (UCT)* is the dominant variant, using a principled exploration bonus to balance exploiting promising branches versus exploring uncertain ones.

MCTS saw great success when applied towards playing the board game "Go" with the AlphaGo, AlphaGo Zero, and AlphaZero, ultimately achieving superhuman performance through pure self-play by combining MCTS with neural networks serving as policy and value functions.

Learn more with these resources:

- [Monte Carlo tree search - Wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search)
- [Bandit based Monte-Carlo Planning (Kocsis & Szepesvári, 2006)](https://link.springer.com/chapter/10.1007/11871842_29) — the paper introducing UCT, the dominant MCTS variant
- [A Survey of Monte Carlo Tree Search Methods (Browne et al., 2012)](https://ieeexplore.ieee.org/document/6145622) — comprehensive overview of variants and applications
- [Mastering the game of Go with deep neural networks and tree search (Silver et al., 2016)](https://www.nature.com/articles/nature16961) — AlphaGo
- [Mastering the game of Go without human knowledge (Silver et al., 2017)](https://www.nature.com/articles/nature24270) — AlphaGo Zero
- [A general reinforcement learning algorithm that masters chess, shogi, and Go through self-play (Silver et al., 2018)](https://www.science.org/doi/10.1126/science.aar6404) — AlphaZero, generalizing to multiple games
