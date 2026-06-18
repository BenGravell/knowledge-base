Imitation Is Not Enough: Robustifying Imitation with Reinforcement Learning for Challenging Driving Scenarios

Topics include Imitation learning, Reinforcement learning, Autonomous driving, Robustness, Closed-loop evaluation, Safety.

Shows that large-scale behavior cloning for urban driving can be materially improved by reinforcement learning with simple safety- and reliability-oriented rewards. The paper is useful as evidence that imitation alone can under-handle rare and challenging driving scenarios even when the demonstration corpus is very large.

Imitation learning (IL) is a simple and powerful way to use high-quality human driving data, which can be collected at scale, to produce human-like behavior. However, policies based on imitation learning alone often fail to sufficiently account for safety and reliability concerns. In this paper, we show how imitation learning combined with reinforcement learning using simple rewards can substantially improve the safety and reliability of driving policies over those learned from imitation alone. In particular, we train a policy on over 100k miles of urban driving data, and measure its effectiveness in test scenarios grouped by different levels of collision likelihood. Our analysis shows that while imitation can perform well in low-difficulty scenarios that are well-covered by the demonstration data, our proposed approach significantly improves robustness on the most challenging scenarios (over 38% reduction in failures). To our knowledge, this is the first application of a combined imitation and reinforcement learning approach in autonomous driving that utilizes large amounts of real-world human driving data.

## INTRODUCTION

Building an autonomous driving system that is deployable at scale presents many difficulties. First and foremost is the challenge of handling the numerous rare and challenging edge cases that occur in real-world driving. To this end, imitative learning based approaches have been proposed that allow the performance of the method to scale with the amount of data available....

Reinforcement Learning (RL) has the potential to resolve this by leveraging explicit reward functions that tell the policy what constitutes safe or unsafe outcomes (e.g., collisions). Furthermore, because RL methods train in closed-loop, RL policies can establish causal relationships between observations, actions, and outcomes. This yields policies that are less vulnerable to covariate shifts and spurious correlations commonly seen in open loop IL, and aware of safety considerations encoded in their reward function, but which are only implicit in the demonstrations.

## CONCLUSIONS

We presented a method for robust autonomous driving in challenging driving scenarios, that combines imitation learning with RL (BC-SAC), paired with a simple safety reward, and trained on large datasets of real-world driving. Overall, the method significantly improves safety and reliability in challenging scenarios, resulting in more than 38% reduction in safety events of the most difficult scenarios compared to IL-only and RL-only baselines. Our extensive experiments examined the roles of training datasets, reward shaping and IL / RL objective terms....

### IV-C Forward and Inverse Vehicle Dynamics Models

In this work, we use an actor-critic method for training continuous control policies. Typical actor-critic methods alternate between training a critic $Q$ to minimize the Bellman error and an actor $\pi$ to maximize the value function. We use the entropy-regularized updates of Soft Actor-Critic (SAC):

Baselines. We compare our method to both open-loop (*BC* ) and closed-loop (*MGAIL* ) imitative methods. The latter takes advantage of closed loop training and the differentiability of the simulator dynamics. For completeness, we also include a SAC baseline to represent an RL-only approach.

However, relying on RL alone, e.g. is also problematic because it heavily depends on reward design, which is an open challenge in autonomous driving....
