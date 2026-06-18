Is Behavior Cloning All You Need? Understanding Horizon in Imitation Learning

Topics include Imitation learning, Robotics, Autonomous driving, Neural networks, Supervised learning, Online algorithms, Offline algorithms, Sample complexity, Control, Learning, Horizon, Behavior cloning.

Imitation learning (IL) aims to mimic the behavior of an expert in a sequential decision making task by learning from demonstrations, and has been widely applied to robotics, autonomous driving, and autoregressive text generation. The simplest approach to IL, behavior cloning (BC), is thought to incur sample complexity with unfavorable quadratic dependence on the problem horizon, motivating a variety of different online algorithms that attain improved linear horizon dependence under stronger assumptions on the data and the learner's access to the expert. We revisit the apparent gap between offline and online IL from a learning-theoretic perspective, with a focus on the realizable/well-specified setting with general policy classes up to and including deep neural networks. Through a new analysis of behavior cloning with the logarithmic loss, we show that it is possible to achieve horizon-independent sample complexity in offline IL whenever (i) the range of the cumulative payoffs is controlled, and (ii) an appropriate notion of supervised learning complexity for the policy class is controlled....

### Introduction

Imitation learning (IL) is the problem of emulating an expert policy for sequential decision making by learning from demonstrations. Compared to reinforcement learning (RL), the learner in IL does not observe reward-based feedback, and must imitate the expert's behavior based on demonstrations alone; their objective is to achieve performance close to that of the expert on an *unobserved* reward function.

Imitation learning is motivated by the observation that in many domains, demonstrating the desired behavior for a task (e.g., robotic grasping) is simple, while designing a reward function to elicit the desired behavior can be challenging. IL is also often preferable to RL because it removes the need for exploration, leading to empirically reduced sample complexity and often much more stable training....

### Additional Results

Secondary results deferred to the appendix for space include (i) examples and additional guarantees for LogLossBC and LogLossDagger (Appendix C); and (ii) additional lower bounds and results concerning the tightness of Sections 2.4 and 3 (Appendix G).

To understand the dependence on horizon in Section 3, we restrict our attention to the "parameter sharing" case where ${\log{|\Pi|}} = {O{}}$, and separately discuss the sparse and dense reward settings (results summarized in Footnote 13).

To the best of our knowledge, this is the tightest available sample complexity guarantee for offline imitation learning with general policy classes. This bound improves upon the guarantee for indicator-loss behavior cloning in Eq. 4 by an $O{(H)}$ factor, and improves upon the guarantee for Dagger in Eq. 5 (replacing $H$ with $R \leq H$ under $r_{h} \in {\lbrack 0,1\rbrack}$) in the typical regime where $\mu = {\Omega{}}$.

As with Section 4, this example calls for a fine-grained policy class-dependent theory, which we hope to explore more deeply in future work.

In more detail, imitation learning algorithms can be loosely grouped into *offline* and *online* approaches. Offline imitation learning algorithms only require access to a dataset of logged trajectories from the expert, making them broadly applicable....
