Temporal Parallelization of Dynamic Programming and Linear Quadratic Control

This article proposes a general formulation for temporal parallelization of dynamic programming for optimal control problems. We derive the elements and associative operators to be able to use parallel scans to solve these problems with logarithmic time complexity rather than linear time complexity. We apply this methodology to problems with finite state and control spaces, linear quadratic tracking control problems, and to a class of nonlinear control problems. The computational benefits of the parallel methods are demonstrated via numerical simulations run on a graphics processing unit.

## Introduction

Optimal control theory (see, e.g., ) is concerned with designing control signals to steer a system such that a given cost function is minimised, or equivalently, a performance measure is maximised. The system can be, for example, an airplane or autonomous vehicle which is steered to follow a given trajectory, an inventory system, a chemical reaction, or a mobile robot.

Dynamic programming, in the form first introduced by Bellman 1950's, is a general method for determining feedback laws for optimal control and other sequential decision problems, and it also forms the basis of reinforcement learning, which is a subfield of machine learning. The classic dynamic programming algorithm is a sequential procedure that proceeds backwards from the final time step to the initial time step, and determines the value (cost-to-go) function as well as the optimal control law in time complexity of $O{(T)}$, where $T$ is the number of time steps....

Making the gradient of this function w.r.t. $\lambda$ equal to zero, we obtain that the maximum is obtained for

Substituting into, we obtain, which finishes the proof of Lemma 15.

### Extension to more general cost functions

### Conditional value functions and combination rules

We would like to point out that, as we are using TensorFlow with GPUs, the matrix operations on the individual time steps of the sequential algorithms are parallelised. Therefore, the sequential LQT algorithms can be interpreted as a TensorFlow parallel implementation of the Riccati recursion.

However, the complexity $O{(T)}$ is only optimal in a computer with one single-core central processing unit (CPU). Nowadays, even general-purpose computers typically have multi-core CPUs with tens of cores and higher-end computers can have hundreds of them. Furthermore, graphics processing units (GPUs) have become common accessories of general-purpose computers and current high-end GPUs can have tens of thousands of computational cores that can be used to parallelise computations and lower the time-complexity.

Dynamic programming algorithms that parallelise computations at each time step, but operate sequentially, are provided in for discrete states, and in for the Riccati recursion in linear quadratic problems....
