Revisiting Maximum Entropy Inverse Reinforcement Learning: New Perspectives and Algorithms

Topics include Reinforcement learning, Inverse reinforcement learning, Datasets, Learning.

We provide new perspectives and inference algorithms for Maximum Entropy (MaxEnt) Inverse Reinforcement Learning (IRL), which provides a principled method to find a most non-committal reward function consistent with given expert demonstrations, among many consistent reward functions. We first present a generalized MaxEnt formulation based on minimizing a KL-divergence instead of maximizing an entropy. This improves the previous heuristic derivation of the MaxEnt IRL model (for stochastic MDPs), allows a unified view of MaxEnt IRL and Relative Entropy IRL, and leads to a model-free learning algorithm for the MaxEnt IRL model. Second, a careful review of existing inference algorithms and implementations showed that they approximately compute the marginals required for learning the model. We provide examples to illustrate this, and present an efficient and exact inference algorithm. Our algorithm can handle variable length demonstrations; in addition, while a basic version takes time quadratic in the maximum demonstration length L, an improved version of this algorithm reduces this to linear using a padding trick....

## Introduction

Inverse Reinforcement Learning (IRL) searches for a reward or cost function to rationalize observed behaviour. This is challenging because the same reward may be optimized by different behaviors, and optimizing different reward functions can lead to the same behavior. In their seminal work Ziebart et al. developed a principled solution using the Maximum Entropy (MaxEnt) principle to choose the most non-committal consistent reward -- i.e. a reward which matches demonstrated feature counts but makes no additional assumptions about the demonstrated behaviour....

Despite the long line of works based on the original MaxEnt IRL paper, we believe that the full value of the original MaxEnt IRL model might not have been fully realized yet, for two reasons. First, while the MaxEnt IRL model for deterministic Markov Decision Processes (MDPs) has been rigorously derived from the MaxEnt principle, the corresponding model for stochastic MDPs was based on a heuristic argument....

We presented new perspective and algorithms, including a new interpretation that unifies MaxEnt IRL and RE-IRL with several implications, and an efficient exact algorithm that leads to improved reward learning and is capable of scaling up to a large real-world dataset. We make an optimized implementation compatible with OpenAI Gym environments publicly available to facilitate further research and applications.

We plan to follow up this work with some further developments. First, as mentioned in Section 2, we can develop exact algorithms to handle more complex features by adapting the sum-product algorithm. This can potentially lead to further performance improvement when complex features are indeed necessary. Second, we pointed out that our new interpretation of MaxEnt IRL suggests that we can directly adapt the model-free importance sampling learning algorithm for RE-IRL to MaxEnt IRL. While this may be biased towards short demonstrations, this allows us to deal with continuous MDPs....

*All* states (including terminal states and the auxiliary state) now feature the auxiliary action and state state in their children set

### Backward message passing variable

This algorithm computes the same (exact) gradients as the basic algorithm described above in Section 5.4, however has linear time complexity in the size of the longest demonstration path...
