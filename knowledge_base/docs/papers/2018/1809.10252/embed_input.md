Deeply Informed Neural Sampling for Robot Motion Planning

Topics include Motion planning, Robotics, Neural networks, Autoencoders, Computational complexity, Scalability, Sampling-based methods, Generalization, Planning, Sampling, Configuration space, Adaptive sampling.

Sampling-based Motion Planners (SMPs) have become increasingly popular as they provide collision-free path solutions regardless of obstacle geometry in a given environment. However, their computational complexity increases significantly with the dimensionality of the motion planning problem. Adaptive sampling is one of the ways to speed up SMPs by sampling a particular region of a configuration space that is more likely to contain an optimal path solution. Although there are a wide variety of algorithms for adaptive sampling, they rely on hand-crafted heuristics; furthermore, their performance decreases significantly in high-dimensional spaces. In this paper, we present a neural network-based adaptive sampler for motion planning called Deep Sampling-based Motion Planner (DeepSMP). DeepSMP generates samples for SMPs and enhances their overall speed significantly while exhibiting efficient scalability to higher-dimensional problems....

## Introduction

Sampling-based Motion Planners (SMPs) have emerged as a promising framework for solving high-dimensional, constrained motion planning problems. SMPs ensure probabilistic completeness, which implies that a probability of finding a feasible path solution, if one exists, approaches to one as the limit of the number of randomly drawn samples from an obstacle-free space increases to infinity....

In this paper, we propose a neural network-based adaptive sampler that generates samples in particular regions of a configuration space where there is likely to exist an optimal path solution. Our method consists of two neural models, i.e., an obstacle-space encoder and random samples generator. We use a Contractive AutoEncoder (CAE) for the encoding of an obstacle-space into an invariant, robust feature space....

In this paper, we present a deep neural network based sampling method called DeepSMP which generates samples for Sampling-based Motion Planning algorithms to compute optimal paths rapidly and efficiently. The proposed method 1) adaptively samples a selective region of a configuration space that most likely contains an optimal path solution, 2) combined with SMP methods consistently demonstrate mean execution time of about 2 second in all presented experiments, and 3) generalizes to new unseen environments.

In our future work, we plan to propose an incremental online learning method that begins with an SMP method, and trains DeepSMP simultaneously to gradually switch from uniform sampling to adaptive sampling. To speed up the incremental online learning process, we plan to propose a method that prioritizes experiences to learn from selectively fewer training examples.

### IV-D1 Workspaces

### IV-B Deep Sampler

Figure 4: DeepSMP generating samples in complex 3D environments (c3D). The obstacles, indicated as blocks in beige color, are made slightly transparent to display path profiles behind them.

## Related Work

Many biased-sampling heuristics have been proposed to enhance the computational speed of RRT and its variants. For instance, Rickert et al. used gradient information to balance exploration and exploitation. Urmson and Simmons method heuristically biased samples in RRT while Ferguson and Stentz presented the anytime RRT algorithm by using multiple independent RRTs....
