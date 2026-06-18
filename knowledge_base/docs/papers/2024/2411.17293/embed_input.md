SIL-RRT*: Learning Sampling Distribution through Self Imitation Learning

Topics include Imitation learning, Motion planning, Robotics, Safety, Neural networks, Sampling-based methods, Planning, Learning, Sampling.

Efficiently finding safe and feasible trajectories for mobile objects is a critical field in robotics and computer science. In this paper, we propose SIL-RRT*, a novel learning-based motion planning algorithm that extends the RRT* algorithm by using a deep neural network to predict a distribution for sampling at each iteration. We evaluate SIL-RRT* on various 2D and 3D environments and establish that it can efficiently solve high-dimensional motion planning problems with fewer samples than traditional sampling-based algorithms. Moreover, SIL-RRT* is able to scale to more complex environments, making it a promising approach for solving challenging robotic motion planning problems.

## Introduction

Motion planning is a crucial field of study in robotics and computer science that focuses on finding a feasible and safe trajectory for a robot to achieve a desired goal. It involves determining a sequence of actions that will guide the robot from its initial state to the target, while avoiding collisions and satisfying various constraints, such as kinematic limitations, time constraints, and performance criteria. The significance of motion planning lies in its ability to enable robots to interact safely with their environment and carry out various tasks autonomously.

In this study, we introduce SIL-RRT\*, a novel approach that enhances the Rapidly-exploring Random Tree Star (RRT\*) algorithm through the utilization of deep learning techniques. Unlike traditional methods that rely on Convolutional Neural Networks (CNNs) or Graph Neural Networks (GNNs), we adopt a Transformer-based architecture to capture the relationships between the state space and paths. This choice of architecture allows for greater flexibility and extensibility, enabling SIL-RRT\* to handle motion planning tasks across different dimensions.

## Conclusion and Limitation

This study introduces SIL-RRT\*, an innovative sampling-based algorithm developed to augment the efficiency of the Rapidly-exploring Random Tree (RRT) algorithm. Central to SIL-RRT\* are two transformer architecture neural networks, serving as the sampler and estimator networks. These networks are responsible for generating samples and forecasting the length of solutions, respectively. To enhance SIL-RRT\*'s performance, we implement a weighting mechanism that assigns values to each solution, predicated on the deviation between the actual solution length and its predicted counterpart.

The empirical investigations conducted across diverse environments and configurations unequivocally demonstrate SIL-RRT\*'s superior performance relative to competing methodologies. The findings reveal that SIL-RRT\* markedly enhances the convergence rate, diminishes the requisite number of samples, and facilitates the generation of solutions of superior quality. Collectively, these results position our proposed method as a notably promising solution to the motion planning quandary in robotics.
