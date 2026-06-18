<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Deterministic Policy Gradient Algorithms

Topics include Reinforcement learning, Policy gradients, Deterministic policy, Actor-critic, Continuous action spaces, Model-free control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Derives a deterministic policy gradient (DPG) theorem for model-free RL with continuous action spaces, showing that the deterministic policy gradient equals the expected gradient of the action-value function and is computable without integrating over actions. Introduces compatible function approximation and off-policy actor-critic algorithms, forming the theoretical foundation for DDPG and related methods.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper we consider deterministic policy gradient algorithms for reinforcement learning with continuous actions. The deterministic policy gradient has a particularly appealing form: it is the expected gradient of the action-value function. This simple form means that the deterministic policy gradient can be estimated much more efficiently than the usual stochastic policy gradient. To ensure adequate exploration, we introduce an off-policy actor-critic algorithm that learns a deterministic target policy from an exploratory behaviour policy. Deterministic policy gradient algorithms outperformed their stochastic counterparts in several benchmark problems, particularly in high-dimensional action spaces.
