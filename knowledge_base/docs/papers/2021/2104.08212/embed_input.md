MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale

Topics include Reinforcement learning, Robotics, Learning, MT-Opt.

General-purpose robotic systems must master a large repertoire of diverse skills to be useful in a range of daily tasks. While reinforcement learning provides a powerful framework for acquiring individual behaviors, the time needed to acquire each skill makes the prospect of a generalist robot trained with RL daunting. In this paper, we study how a large-scale collective robotic learning system can acquire a repertoire of behaviors simultaneously, sharing exploration, experience, and representations across tasks. In this framework new tasks can be continuously instantiated from previously learned tasks improving overall performance and capabilities of the system. To instantiate this system, we develop a scalable and intuitive framework for specifying new tasks through user-provided examples of desired outcomes, devise a multi-robot collective learning system for data collection that simultaneously collects experience for multiple tasks, and develop a scalable and generalizable multi-task deep reinforcement learning method, which we call MT-Opt....

## Introduction

Today's deep reinforcement learning (RL) methods, when applied to real-world robotic tasks, provide an effective but expensive way of learning skills. While existing methods are effective and able to generalize, they require considerable on-robot training time, as well as extensive engineering effort for setting up each task and ensuring that the robot can attempt the task repeatedly. For example, the QT-Opt system can learn vision-based robotic grasping, but it requires over $500,000$ trials collected across multiple robots....

Figure 1: A) Multi-task data collection. B) Training objects. C) Sample of tasks that the system is trained on. D) Sample of behaviorally and visually distinct tasks such as covering, chasing, alignment, which we show our method can adapt to. MT-Opt learns new tasks faster (potentially zero-shot if there is sufficient overlap with existing tasks), and with less data compared to learning the new task in isolation.

## Conclusion

We presented a general multi-task learning framework, MT-Opt, that encompasses a number of elements: a multi-task data collection system that simultaneously collects data for multiple tasks, a scalable success detector framework, and a multi-task deep RL method that is able to effectively utilize the multi-task data. With real-world experiments, we carefully evaluate various design decisions and show the benefits of sharing weights between the tasks and sharing data using our task impersonation and data re-balancing strategies....

Figure 3: Path of episodes through task impersonation, where episodes are routed to train relevant tasks, and data re-balancing where the ratio of success (S) and failure (F) episodes and proportion of data per task is controlled. Pale blue and pale red indicates additional task training data coming from other tasks. The height of a bar indicates very different amount of data across tasks and across successful outcomes.

where ${Q_{T}{(\mathbf{s},\mathbf{a},\mathbf{s}^{\prime})}} = {{r{(\mathbf{s},\mathbf{a})}} + {\gammaV{(\mathbf{s}^{\prime})}}}$ is a target Q-value and $D$ is a divergence metric, such as cross-entropy, $\gamma$ is a discount factor, $V{(\mathbf{s}^{\prime})}$ is the target value function of the next state computed using stochastic optimization of the form ${V{(\mathbf{s}^{\prime})}} =...
