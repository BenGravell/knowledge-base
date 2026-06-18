Dueling Network Architectures for Deep Reinforcement Learning

Topics include Reinforcement learning, Neural networks, Convolutional networks, Learning, Network architecture.

In recent years there have been many successes of using deep representations in reinforcement learning. Still, many of these applications use conventional architectures, such as convolutional networks, LSTMs, or auto-encoders. In this paper, we present a new neural network architecture for model-free reinforcement learning. Our dueling network represents two separate estimators: one for the state value function and one for the state-dependent action advantage function. The main benefit of this factoring is to generalize learning across actions without imposing any change to the underlying reinforcement learning algorithm. Our results show that this architecture leads to better policy evaluation in the presence of many similar-valued actions. Moreover, the dueling architecture enables our RL agent to outperform the state-of-the-art on the Atari 2600 domain.

## Introduction

Over the past years, deep learning has contributed to dramatic advances in scalability and performance of machine learning. One exciting application is the sequential decision-making setting of reinforcement learning (RL) and control. Notable examples include deep Q-learning, deep visuomotor policies, attention with recurrent networks, and model predictive control with embeddings. Other recent successes include massively parallel frameworks and expert move prediction in the game of Go, which produced policies matching those of Monte Carlo tree search programs, and squarely beaten a professional player when combined with search.

In spite of this, most of the approaches for RL use standard neural networks, such as convolutional networks, MLPs, LSTMs and autoencoders. The focus in these recent advances has been on designing improved control and RL algorithms, or simply on incorporating existing neural network architectures into RL methods. Here, we take an *alternative but complementary approach* of focusing primarily on innovating a neural network architecture that is better suited for model-free RL. This approach has the benefit that the new network can be easily combined with existing and future algorithms for RL....

## Conclusions

We introduced a new neural network architecture that decouples value and advantage in deep $Q$-networks, while sharing a common feature learning module. The new dueling architecture, in combination with some algorithmic improvements, leads to dramatic improvements over existing approaches for deep RL in the challenging Atari domain. The results presented in this paper are the new state-of-the-art in this popular domain.

On the one hand this loses the original semantics of $V$ and $A$ because they are now off-target by a constant, but on the other hand it increases the stability of the optimization: with the advantages only need to change as fast as the mean, instead of having to compensate any change to the optimal action's advantage in. We also experimented with a softmax version of equation, but found it to deliver similar results to the simpler module of equation. Hence, all the experiments reported in this paper use the module of equation.

### Prioritized Replay

### General Atari Game-Playing
