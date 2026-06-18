Rainbow: Combining Improvements in Deep Reinforcement Learning

Topics include Reinforcement learning, Benchmarks, Learning, Rainbow.

The deep reinforcement learning community has made several independent improvements to the DQN algorithm. However, it is unclear which of these extensions are complementary and can be fruitfully combined. This paper examines six extensions to the DQN algorithm and empirically studies their combination. Our experiments show that the combination provides state-of-the-art performance on the Atari 2600 benchmark, both in terms of data efficiency and final performance. We also provide results from a detailed ablation study that shows the contribution of each component to overall performance.

## Introduction

The many recent successes in scaling reinforcement learning (RL) to complex sequential decision-making problems were kick-started by the Deep Q-Networks algorithm (DQN; ? ?, ?). Its combination of Q-learning with convolutional neural networks and experience replay enabled it to learn, from raw pixels, how to play many Atari games at human-level performance. Since then, many extensions have been proposed that enhance its speed or stability.

Double DQN (DDQN; ? ?) addresses an overestimation bias of Q-learning (?), by decoupling selection and evaluation of the bootstrap action. Prioritized experience replay (?) improves data efficiency, by replaying more often transitions from which there is more to learn. The dueling network architecture (?) helps to generalize across actions by separately representing state values and action advantages. Learning from multi-step bootstrap targets (?; ?), as used in A3C (?), shifts the bias-variance trade-off and helps to propagate newly observed rewards faster to earlier visited states....

The state representation could also be made more efficient by exploiting auxiliary tasks such as pixel control or feature control (?), supervised predictions (?) or successor features (?).

To evaluate Rainbow fairly against the baselines, we have followed the common domain modifications of clipping rewards, fixed action-repetition, and frame-stacking, but these might be removed by other learning algorithm improvements. Pop-Art normalization (?) allows reward clipping to be removed, while preserving a similar level of performance. Fine-grained action repetition (?) enabled to learn how to repeat actions. A recurrent state network (?) can learn a temporal state representation, replacing the fixed stack of observation frames....

Figure 2: Each plot shows, for several agents, the number of games where they have achieved at least a given fraction of human performance, as a function of time. From left to right we consider the 20%, 50%, 100%, 200% and 500% thresholds. On the first row we compare Rainbow to the baselines. On the second row we compare Rainbow to its ablations.

### Distributional RL

The hyper-parameters (see Table 1) are identical across all 57 games, i.e., the Rainbow agent really is a *single* agent setup that performs well across all the games.
