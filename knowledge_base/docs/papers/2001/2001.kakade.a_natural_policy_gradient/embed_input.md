<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Natural Policy Gradient

Topics include Reinforcement learning, Policy gradients, Natural gradients, Fisher information matrix, Policy optimization, Markov decision process.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes using the natural gradient (Fisher information metric) for policy optimization in RL, showing it moves toward policy-iteration greedy actions rather than merely better actions. Motivated and formalized the use of the natural gradient in RL, directly inspiring later work on TRPO and NPG-based algorithms.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We provide a natural gradient method that represents the steepest descent direction based on the underlying structure of the parameter space. Although gradient methods cannot make large changes in the values of the parameters, we show that the natural gradient is moving toward choosing a greedy optimal action rather than just a better action. These greedy optimal actions are those that would be chosen under one improvement step of policy iteration with approximate, compatible value functions, as defined by Sutton et al. We then show drastic performance improvements in simple MDPs and in the more challenging MDP of Tetris.
