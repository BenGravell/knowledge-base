Is Behavior Cloning All You Need? Understanding Horizon in Imitation Learning

Topics include Imitation learning, Robotics, Autonomous driving, Neural networks, Supervised learning, Online algorithms, Offline algorithms, Sample complexity, Control, Learning, Horizon, Behavior cloning.

Imitation learning (IL) aims to mimic the behavior of an expert in a sequential decision making task by learning from demonstrations, and has been widely applied to robotics, autonomous driving, and autoregressive text generation. The simplest approach to IL, behavior cloning (BC), is thought to incur sample complexity with unfavorable quadratic dependence on the problem horizon, motivating a variety of different online algorithms that attain improved linear horizon dependence under stronger assumptions on the data and the learner's access to the expert. We revisit the apparent gap between offline and online IL from a learning-theoretic perspective, with a focus on the realizable/well-specified setting with general policy classes up to and including deep neural networks. Through a new analysis of behavior cloning with the logarithmic loss, we show that it is possible to achieve horizon-independent sample complexity in offline IL whenever (i) the range of the cumulative payoffs is controlled, and (ii) an appropriate notion of supervised learning complexity for the policy class is controlled.

## Introduction

Imitation learning (IL) is the problem of emulating an expert policy for sequential decision making by learning from demonstrations. Compared to reinforcement learning (RL), the learner in IL does not observe reward-based feedback, and must imitate the expert's behavior based on demonstrations alone; their objective is to achieve performance close to that of the expert on an *unobserved* reward function.

Imitation learning is motivated by the observation that in many domains, demonstrating the desired behavior for a task (e.g., robotic grasping) is simple, while designing a reward function to elicit the desired behavior can be challenging. IL is also often preferable to RL because it removes the need for exploration, leading to empirically reduced sample complexity and often much more stable training.

In more detail, imitation learning algorithms can be loosely grouped into *offline* and *online* approaches. Offline imitation learning algorithms only require access to a dataset of logged trajectories from the expert, making them broadly applicable. The most widely used approach, *behavior cloning*, reduces imitation learning to a standard supervised learning problem in which the learner attempts to predict the expert's actions from observations given the collected trajectories.

## Discussion

We conclude with additional technical remarks and directions for future research.

## Conclusion and Future Work

Our results clarify the role of horizon in offline and online imitation learning, and show that---at least under standard assumptions in theoretical research into imitation learning---the gap between online and offline IL is smaller than previously thought. Instabilities of offline IL and benefits of online IL may indeed arise in practice, but existing assumptions in theoretical research on imitation learning appear be too coarse to give insights into the true nature of these phenomena, highlighting the need to develop a fine-grained, problem-dependent understanding of algorithms and complexity for IL.
