MT-Opt: Continuous Multi-Task Robotic Reinforcement Learning at Scale

Topics include Reinforcement learning, Robotics, Learning, MT-Opt.

General-purpose robotic systems must master a large repertoire of diverse skills to be useful in a range of daily tasks. While reinforcement learning provides a powerful framework for acquiring individual behaviors, the time needed to acquire each skill makes the prospect of a generalist robot trained with RL daunting. In this paper, we study how a large-scale collective robotic learning system can acquire a repertoire of behaviors simultaneously, sharing exploration, experience, and representations across tasks. In this framework new tasks can be continuously instantiated from previously learned tasks improving overall performance and capabilities of the system. To instantiate this system, we develop a scalable and intuitive framework for specifying new tasks through user-provided examples of desired outcomes, devise a multi-robot collective learning system for data collection that simultaneously collects experience for multiple tasks, and develop a scalable and generalizable multi-task deep reinforcement learning method, which we call MT-Opt.

## Introduction

Today's deep reinforcement learning (RL) methods, when applied to real-world robotic tasks, provide an effective but expensive way of learning skills. While existing methods are effective and able to generalize, they require considerable on-robot training time, as well as extensive engineering effort for setting up each task and ensuring that the robot can attempt the task repeatedly. For example, the QT-Opt system can learn vision-based robotic grasping, but it requires over $500,000$ trials collected across multiple robots.

Prior work indicates that multi-task RL can indeed amortize the cost of single-task learning. In particular, insofar as the tasks share common structure, if that structure can be discovered by the learning algorithm, all of the tasks can in principle be learned much more efficiently than learning each of the tasks individually. Such shared representations can include basic visual features, as well as more complex concepts, such as learning how to pick up objects. In addition, by collecting experience simultaneously using controllers for a variety of tasks with different difficulty, the easier tasks can serve to "bootstrap" the harder tasks.

The main contribution of this paper is a general multi-task learning system, which we call MT-Opt, that realizes the hypothesized benefits of multi-task RL in the real world while addressing some of the associated challenges.

We show how our system can quickly acquire new tasks by taking advantage of prior tasks via shared representations, novel data-routing strategies, and learned policies.

We present our multi-task system as well as examples of some of the tasks that it is capable of performing in Fig. 1.

## Conclusion

We presented a general multi-task learning framework, MT-Opt, that encompasses a number of elements: a multi-task data collection system that simultaneously collects data for multiple tasks, a scalable success detector framework, and a multi-task deep RL method that is able to effectively utilize the multi-task data. With real-world experiments, we carefully evaluate various design decisions and show the benefits of sharing weights between the tasks and sharing data using our task impersonation and data re-balancing strategies.
