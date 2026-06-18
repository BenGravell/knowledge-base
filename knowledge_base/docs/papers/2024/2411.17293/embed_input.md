SIL-RRT*: Learning Sampling Distribution through Self Imitation Learning

Topics include Imitation learning, Motion planning, Robotics, Safety, Neural networks, Sampling-based methods, Planning, Learning, Sampling.

Efficiently finding safe and feasible trajectories for mobile objects is a critical field in robotics and computer science. In this paper, we propose SIL-RRT*, a novel learning-based motion planning algorithm that extends the RRT* algorithm by using a deep neural network to predict a distribution for sampling at each iteration. We evaluate SIL-RRT* on various 2D and 3D environments and establish that it can efficiently solve high-dimensional motion planning problems with fewer samples than traditional sampling-based algorithms. Moreover, SIL-RRT* is able to scale to more complex environments, making it a promising approach for solving challenging robotic motion planning problems.

## Introduction

Motion planning is a crucial field of study in robotics and computer science that focuses on finding a feasible and safe trajectory for a robot to achieve a desired goal. It involves determining a sequence of actions that will guide the robot from its initial state to the target, while avoiding collisions and satisfying various constraints, such as kinematic limitations, time constraints, and performance criteria. The significance of motion planning lies in its ability to enable robots to interact safely with their environment and carry out various tasks autonomously.

As robots become more widely used and their applications increasingly complex, the motion planning problem demands algorithms that are both computationally tractable and efficient. This has led to the development of sampling-based algorithms, such as Probabilistic Roadmaps (PRM) \[\], Rapidly-exploring Random Trees (RRT) \[\], and RRT\* \[\]. These algorithms typically employ a uniform sampler, but when the dimension of the environment increases, the number of samples needed to find a feasible solution may also raise....

While SIL-RRT\* has exhibited commendable performance using a constrained dataset and demonstrated the capacity to learn from generated paths, its dependency on substantial datasets for training remains a notable limitation. Procuring such extensive datasets becomes increasingly difficult in complex scenarios. As a prospective avenue for research, we propose exploring the integration of adaptive reinforcement learning (RL) techniques with the RRT\* framework....

A notable limitation of SIL-RRT\* lies in its presupposition of uniformity in the size and form of point-mass and rigid-body objects, a constraint that complicates applications involving robots of varying sizes or shapes. The algorithm's ability to generalize its learned knowledge to larger robots is, consequently, hindered. To surmount this challenge, our forthcoming research endeavors will involve the integration of robot size and shape considerations into our models....

In this study, we utilize feasible paths, denoted as $\tau = {x_{0},x_{1},x_{2},\ldots,x_{t}}$, sourced from planning algorithms or expert demonstrations, to guide our model. To enhance the diversity of our dataset, we introduce a novel data augmentation technique that involves random reversals of these paths....
