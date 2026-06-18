Rainbow: Combining Improvements in Deep Reinforcement Learning

Topics include Reinforcement learning, Benchmarks, Learning, Rainbow.

The deep reinforcement learning community has made several independent improvements to the DQN algorithm. However, it is unclear which of these extensions are complementary and can be fruitfully combined. This paper examines six extensions to the DQN algorithm and empirically studies their combination. Our experiments show that the combination provides state-of-the-art performance on the Atari 2600 benchmark, both in terms of data efficiency and final performance. We also provide results from a detailed ablation study that shows the contribution of each component to overall performance.

## Introduction

The many recent successes in scaling reinforcement learning (RL) to complex sequential decision-making problems were kick-started by the Deep Q-Networks algorithm (DQN; ? ?, ?). Its combination of Q-learning with convolutional neural networks and experience replay enabled it to learn, from raw pixels, how to play many Atari games at human-level performance. Since then, many extensions have been proposed that enhance its speed or stability.

Double DQN (DDQN; ? ?) addresses an overestimation bias of Q-learning (?), by decoupling selection and evaluation of the bootstrap action. Prioritized experience replay (?) improves data efficiency, by replaying more often transitions from which there is more to learn. The dueling network architecture (?) helps to generalize across actions by separately representing state values and action advantages. Learning from multi-step bootstrap targets (?; ?), as used in A3C (?), shifts the bias-variance trade-off and helps to propagate newly observed rewards faster to earlier visited states.

Each of these algorithms enables substantial performance improvements in isolation. Since they do so by addressing radically different issues, and since they build on a shared framework, they could plausibly be combined. In some cases this has been done: Prioritized DDQN and Dueling DDQN both use double Q-learning, and Dueling DDQN was also combined with prioritized experience replay. In this paper we propose to study an agent that combines all the aforementioned ingredients. We show how these different ideas can be integrated, and that they are indeed largely complementary.

## Discussion

We have demonstrated that several improvements to DQN can be successfully integrated into a single learning algorithm that achieves state-of-the-art performance. Moreover, we have shown that within the integrated algorithm, all but one of the components provided clear performance benefits. There are many more algorithmic components that we were not able to include, which would be promising candidates for further experiments on integrated agents. Among the many possible candidates, we discuss several below.

We have focused here on value-based methods in the Q-learning family. We have not considered purely policy-based RL algorithms such as trust-region policy optimisation (?), nor actor-critic methods (?; ?).
