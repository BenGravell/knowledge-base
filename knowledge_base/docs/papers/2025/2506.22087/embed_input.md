An Introduction to Zero-Order Optimization Techniques for Robotics

Topics include Trajectory optimization, Robotics, Optimization.

Zero-order optimization techniques are becoming increasingly popular in robotics due to their ability to handle non-differentiable functions and escape local minima. These advantages make them particularly useful for trajectory optimization and policy optimization. In this work, we propose a mathematical tutorial on random search. It offers a simple and unifying perspective for understanding a wide range of algorithms commonly used in robotics. Leveraging this viewpoint, we classify many trajectory optimization methods under a common framework and derive novel competitive RL algorithms.

## Introduction

In recent years, zero-order (or derivative-free) optimization techniques have gained a lot of popularity in the robotics community. While zero-order optimization is a well-established field, its widespread deployment in robotics has only been made possible by recent advances in parallel computing and GPU hardware. These improvements have made it possible to deploy sampling-based Model Predictive Control (MPC) on complex robotic systems. In parallel, Reinforcement Learning (RL) has emerged as a powerful tool and has demonstrated state-of-the-art capabilities in locomotion or manipulation.

Recently, introduced Gaussian smoothing and understood random search from an optimization perspective. Inspired by this work, we propose a unified perspective to understand the zero-order optimization techniques that are popular in the robotics community.

Overall, a broad perspective connecting gradient-free approaches in TO and RL is missing. To bridge this gap, we propose a mathematical introduction to zero-order optimization algorithms used in robotics. This unified treatment provides a simple way to understand techniques such as MPPI, Covariance Matrix Adaptation (CMA), and RL policy gradient methods. In addition, we show how this unified view allows us to naturally derive novel competitive methods as a byproduct. Lastly, we discuss the theoretical concepts explaining why stochastic algorithms are well-suited to avoid getting stuck in local minima.

## Conclusion

In this work, we have demonstrated how random search provides a unifying perspective on zero-order algorithms commonly used in robotics. We also discussed theoretical concepts that help explain why sampling-based zero-order techniques can escape local minima. Leveraging this understanding, we proposed novel and competitive RL algorithms. These algorithms are only examples of the potential outcomes enabled by this unified viewpoint. In the future, we hope this tutorial will help the robotics community tackle open challenges such as constrained zero-order optimization and the search for global solutions.
