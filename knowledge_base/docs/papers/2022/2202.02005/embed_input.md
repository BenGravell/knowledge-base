BC-Z: Zero-Shot Task Generalization with Robotic Imitation Learning

Topics include Imitation learning, Robotics, Generalization, Learning, BC-Z.

In this paper, we study the problem of enabling a vision-based robotic manipulation system to generalize to novel tasks, a long-standing challenge in robot learning. We approach the challenge from an imitation learning perspective, aiming to study how scaling and broadening the data collected can facilitate such generalization. To that end, we develop an interactive and flexible imitation learning system that can learn from both demonstrations and interventions and can be conditioned on different forms of information that convey the task, including pre-trained embeddings of natural language or videos of humans performing the task. When scaling data collection on a real robot to more than 100 distinct tasks, we find that this system can perform 24 unseen manipulation tasks with an average success rate of 44%, without any robot demonstrations for those tasks.

## Introduction

One of the grand challenges in robotics is to create a general-purpose robot capable of performing a multitude of tasks in unstructured environments based on arbitrary user commands. The key challenge in this endeavour is *generalization*: the robot must handle new environments, recognize and manipulate objects it has not seen before, and understand the intent of a command it has never been asked to execute. End-to-end learning from pixels is a flexible choice for modeling the behavior of such generalist robots, as it has minimal assumptions about the state representation of the world.

We develop an interactive imitation learning system with two key properties that enable high-quality data collection and generalization to entirely new tasks. First, our system incorporates shared autonomy into teleoperation to allow us to collect both raw demonstration data and human interventions to correct the robot's current policy. Second, our system flexibly conditions the policy on different forms of task specification, including a language instruction or a video of a person performing the task.

## Discussion

We presented a multi-task imitation learning system that combines flexible task embeddings with large-scale training on a 100-task demonstration dataset, enabling it to generalize to entirely new tasks that were not seen in training based on user-provided language or video commands. Our evaluation covered 29 unseen vision-based manipulation tasks with a variety of objects and scenes. The key conclusion of our empirical study is that simple imitation learning approaches can be scaled in a way that facilitates generalization to new tasks with zero additional robot data of those tasks.

Our system does have a number of limitations. First, the performance on novel tasks varies significantly. However, even for tasks that are less successful, the robot often exhibits behavior suggesting that it understands at least part of the task, reaching for the right object or performing a semantically related motion. This suggests that an exciting direction for future work is to use our policies as a general-purpose initialization for finetuning of downstream tasks, where additional training, perhaps with autonomous RL, could lead to significantly better performance.
