When Should We Prefer Offline Reinforcement Learning over Behavioral Cloning?

Topics include Offline reinforcement learning, Behavior cloning, Imitation learning, Expert demonstrations, Sparse rewards, Long-horizon tasks, Suboptimal data, Robotic manipulation.

Analyzes when offline RL can outperform behavioral cloning even when the dataset resembles expert demonstrations. The paper identifies conditions such as sparse rewards, long horizons, and useful noise or suboptimality where value-based improvement can exploit data better than direct imitation, then validates the story across diagnostic and high-dimensional domains.

Offline reinforcement learning (RL) algorithms can acquire effective policies by utilizing previously collected experience, without any online interaction. It is widely understood that offline RL is able to extract good policies even from highly suboptimal data, a scenario where imitation learning finds suboptimal solutions that do not improve over the demonstrator that generated the dataset. However, another common use case for practitioners is to learn from data that resembles demonstrations. In this case, one can choose to apply offline RL, but can also use behavioral cloning (BC) algorithms, which mimic a subset of the dataset via supervised learning. Therefore, it seems natural to ask: when can an offline RL method outperform BC with an equal amount of expert data, even when BC is a natural choice? To answer this question, we characterize the properties of environments that allow offline RL methods to perform better than BC methods, even when only provided with expert data. Additionally, we show that policies trained on sufficiently noisy suboptimal data can attain better performance than even BC algorithms with expert data, especially on long-horizon problems....

### Introduction

Offline reinforcement learning (RL) algorithms aim to leverage large existing datasets of previously collected data to produce effective policies that generalize across a wide range of scenarios, without the need for costly active data collection. Many recent offline RL algorithms can work well even when provided with highly suboptimal data, and a number of these approaches have been studied theoretically....

To our knowledge, there has not been a rigorous characterization of when offline RL perform better than imitation learning. Existing *empirical* studies comparing offline RL to imitation learning have come to mixed conclusions. Some works show that offline RL methods appear to greatly outperform imitation learning, specifically in environments that require "stitching" parts of suboptimal trajectories. In contrast, a number of recent works have argued that BC performs better than offline RL on both expert and suboptimal demonstration data over a variety of tasks....

### Discussion

We sought to understand if offline RL is at all preferable over running BC, even provided with expert or near-expert data. While in the worst case, both approaches attain similar performance on expert data, additional assumptions on the environment can provide certain offline RL methods with an advantage. We also show that running RL on noisy-expert, suboptimal data attains more favorable guarantees compared to running BC on expert data for the same task, using equal amounts of data. Empirically, we observe that offline-tuned offline RL can outperform BC on various practical problem domains, with different kinds of expert policies....

In navigation, as we pictorially illustrate in Figure 1, there may exist multiple paths that end at the same goal, particularly in large, unobstructed areas. For example, while navigating through a wide tunnel, the exact direction the agent takes may not matter so much as multiple directions will take the agent through the tunnel, and identifying these good-enough actions using reward information is easy. However, there are "critical states" like narrow doorways where taking a specific action is important....

Under Conditions 3.1. ‣ 3 Problem Setup and Preliminaries ‣ When Should We Prefer Offline Reinforcement Learning Over Behavioral Cloning?") and 3.2....
