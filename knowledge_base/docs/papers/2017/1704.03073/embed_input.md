Data-efficient Deep Reinforcement Learning for Dexterous Manipulation

Deep learning and reinforcement learning methods have recently been used to solve a variety of problems in continuous control domains. An obvious application of these techniques is dexterous manipulation tasks in robotics which are difficult to solve using traditional control theory or hand-engineered approaches. One example of such a task is to grasp an object and precisely stack it on another. Solving this difficult and practically relevant problem in the real world is an important long-term goal for the field of robotics. Here we take a step towards this goal by examining the problem in simulation and providing models and techniques aimed at solving it. We introduce two extensions to the Deep Deterministic Policy Gradient algorithm (DDPG), a model-free Q-learning based method, which make it significantly more data-efficient and scalable. Our results show that by making extensive use of off-policy data and replay, it is possible to find control policies that robustly grasp objects and stack them. Further, our results hint that it may soon be feasible to train successful stacking policies by collecting interactions on real robots.

## Introduction

Dexterous manipulation is a fundamental challenge in robotics. Researchers have long been seeking a way to enable robots to robustly and flexibly interact with fixed and free objects of different shapes, materials, and surface properties in the context of a broad range of tasks and environmental conditions. Such flexibility is very difficult to achieve with manually designed controllers. The recent resurgence of neural networks and "deep learning" has inspired hope that these methods will be as effective in the control domain as they are for perception....

While the flexibility and generality of learning approaches is promising for robotics, these methods typically require a large amount of data that grows with the complexity of the task. What is feasible on a simulated system, where hundreds of millions of control steps are possible, does not necessarily transfer to real robot applications due to unrealistic learning times. One solution to this problem is to restrict the generality of the controller by incorporating task specific knowledge, e.g. in the form of dynamic movement primitives, or in the form of strong teaching signals, e.g. kinesthetic teaching of trajectories....

It is of course a challenge to judge the transfer of results in simulation to the real world. We have taken care to design a physically realistic simulation, and in initial experiments, which we have performed both in simulation and on the physical robot, we generally find a good correspondence of performance and learning speed between simulation and real world. This makes us optimistic that our performance numbers also hold when going to the real world....

We view the algorithms and techniques presented here as an important step towards applying versatile deep reinforcement learning methods for real-robot dexterous manipulation with perception.

### Asynchronous DPG

## Task and experimental setup

One commonly used solution to this problem is to provide informative shaping rewards that allow a learning signal to be obtained even with simple exploration strategies, e.g. by embedding information about the value function in the reward function for every transition acquired from the environment. For instance, for a simple reaching problem with a robotic arm we could define a shaping reward that takes into account the distance between the end-effector and the target.
