Dueling Network Architectures for Deep Reinforcement Learning

Topics include Reinforcement learning, Neural networks, Convolutional networks, Learning, Network architecture.

In recent years there have been many successes of using deep representations in reinforcement learning. Still, many of these applications use conventional architectures, such as convolutional networks, LSTMs, or auto-encoders. In this paper, we present a new neural network architecture for model-free reinforcement learning. Our dueling network represents two separate estimators: one for the state value function and one for the state-dependent action advantage function. The main benefit of this factoring is to generalize learning across actions without imposing any change to the underlying reinforcement learning algorithm. Our results show that this architecture leads to better policy evaluation in the presence of many similar-valued actions. Moreover, the dueling architecture enables our RL agent to outperform the state-of-the-art on the Atari 2600 domain.

## Introduction

Over the past years, deep learning has contributed to dramatic advances in scalability and performance of machine learning. One exciting application is the sequential decision-making setting of reinforcement learning (RL) and control. Notable examples include deep Q-learning, deep visuomotor policies, attention with recurrent networks, and model predictive control with embeddings. Other recent successes include massively parallel frameworks and expert move prediction in the game of Go, which produced policies matching those of Monte Carlo tree search programs, and squarely beaten a professional player when combined with search.

In the experiments, we demonstrate that the dueling architecture can more quickly identify the correct action during policy evaluation as redundant or similar actions are added to the learning problem.

## Discussion

The advantage of the dueling architecture lies partly in its ability to learn the state-value function efficiently. With every update of the $Q$ values in the dueling architecture, the value stream $V$ is updated -- this contrasts with the updates in a single-stream architecture where only the value for one of the actions is updated, the values for all other actions remain untouched. This more frequent updating of the value stream in our approach allocates more resources to $V$, and thus allows for better approximation of the state values, which in turn need to be accurate for temporal-difference-based methods like Q-learning to work.

Furthermore, the differences between $Q$-values for a given state are often very small relative to the magnitude of $Q$. For example, after training with DDQN on the game of Seaquest, the average action gap (the gap between the $Q$ values of the best and the second best action in a given state) across visited states is roughly $0.04$, whereas the average state value across those states is about $15$. This difference in scales can lead to small amounts of noise in the updates can lead to reorderings of the actions, and thus make the nearly greedy policy switch abruptly.
