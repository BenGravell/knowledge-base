Deeply Informed Neural Sampling for Robot Motion Planning

Topics include Motion planning, Robotics, Neural networks, Autoencoders, Computational complexity, Scalability, Sampling-based methods, Generalization, Planning, Sampling, Configuration space, Adaptive sampling.

Sampling-based Motion Planners (SMPs) have become increasingly popular as they provide collision-free path solutions regardless of obstacle geometry in a given environment. However, their computational complexity increases significantly with the dimensionality of the motion planning problem. Adaptive sampling is one of the ways to speed up SMPs by sampling a particular region of a configuration space that is more likely to contain an optimal path solution. Although there are a wide variety of algorithms for adaptive sampling, they rely on hand-crafted heuristics; furthermore, their performance decreases significantly in high-dimensional spaces. In this paper, we present a neural network-based adaptive sampler for motion planning called Deep Sampling-based Motion Planner (DeepSMP). DeepSMP generates samples for SMPs and enhances their overall speed significantly while exhibiting efficient scalability to higher-dimensional problems.

## Introduction

Sampling-based Motion Planners (SMPs) have emerged as a promising framework for solving high-dimensional, constrained motion planning problems. SMPs ensure probabilistic completeness, which implies that a probability of finding a feasible path solution, if one exists, approaches to one as the limit of the number of randomly drawn samples from an obstacle-free space increases to infinity. However, despite their ability to compute motion plans irrespective of the obstacles geometry, these methods exhibit slow convergence to computing path solutions due to their reliance on the extensive exploration of a given obstacle-free configuration space.

In this paper, we propose a neural network-based adaptive sampler that generates samples in particular regions of a configuration space where there is likely to exist an optimal path solution. Our method consists of two neural models, i.e., an obstacle-space encoder and random samples generator. We use a Contractive AutoEncoder (CAE) for the encoding of an obstacle-space into an invariant, robust feature space.

## II-A Adaptive Sampling Methods

Gammell et al. proposed the Informed-RRT\* algorithm which takes an initial solution from RRT\* algorithm to define an ellipsoidal region from which new samples are drawn to minimize the initial solution for a given cost function. Although Informed-RRT\* demonstrated enhanced convergence towards an optimal solution, this method suffers in situations where finding an initial path solution takes most of the computation time. To address this limitation, Gammell et al. proposed Batch Informed Trees (BIT\*).

## II-B Learning-based Search Methods

Many approaches exist that use learning to improve classical SMPs computationally. A recent method called a Lightning Framework stored paths into a lookup table and used a learned heuristic to write new paths as well as to read and repair old paths. Another similar framework by Coleman et al. is an experience-based strategy to cache experiences in a graph instead of individual trajectories. Although these approaches exhibit superior performance in higher-dimensional spaces when compared to conventional planning methods, lookup tables are memory inefficient and incapable of generalizing well to new planning problems.
