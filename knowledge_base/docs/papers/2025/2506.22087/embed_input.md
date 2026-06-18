An Introduction to Zero-Order Optimization Techniques for Robotics

Topics include Trajectory optimization, Robotics, Optimization.

Zero-order optimization techniques are becoming increasingly popular in robotics due to their ability to handle non-differentiable functions and escape local minima. These advantages make them particularly useful for trajectory optimization and policy optimization. In this work, we propose a mathematical tutorial on random search. It offers a simple and unifying perspective for understanding a wide range of algorithms commonly used in robotics. Leveraging this viewpoint, we classify many trajectory optimization methods under a common framework and derive novel competitive RL algorithms.

## Introduction

In recent years, zero-order (or derivative-free) optimization techniques \[\] have gained a lot of popularity in the robotics community. While zero-order optimization is a well-established field, its widespread deployment in robotics has only been made possible by recent advances in parallel computing and GPU hardware. These improvements have made it possible to deploy sampling-based Model Predictive Control (MPC) on complex robotic systems. In parallel, Reinforcement Learning (RL) has emerged as a powerful tool and has demonstrated state-of-the-art capabilities in locomotion or manipulation.

While these approaches may appear unrelated at first, they share a common property: they do not require access to the simulator's gradients. This characteristic allows them to optimize non-smooth objective functions, which typically arise in problems involving contact, such as locomotion or manipulation. Another benefit is that it avoids the tedious development of efficient gradient implementations. Furthermore, while deterministic gradient-based algorithms, such as gradient descent or Newton's method, are prone to getting stuck in local minima, zero-order techniques are mostly stochastic, which can help escape local minima.

## Conclusion

In this work, we have demonstrated how random search provides a unifying perspective on zero-order algorithms commonly used in robotics. We also discussed theoretical concepts that help explain why sampling-based zero-order techniques can escape local minima. Leveraging this understanding, we proposed novel and competitive RL algorithms. These algorithms are only examples of the potential outcomes enabled by this unified viewpoint. In the future, we hope this tutorial will help the robotics community tackle open challenges such as constrained zero-order optimization and the search for global solutions.

As ${({x + \epsilon_{k}})} \sim {\mathcal{N}{(x,\Sigma)}}$, we recover the MPPI update. Furthermore, if $\Sigma = {\sigma^{2}I}$, then $\frac{\sigma^{2}}{\lambda} \leq \frac{1}{L}$, where $L$ is the Lipschitz function of the surrogate function \[\]. Therefore, the step size chosen by MPPI can be interpreted as a conservative estimate of the standard optimal step size from convex optimization \[\].

So far, we have seen that performing random approximate gradient descent can be sample efficient in the convex...
