Sparse Optimal Control of Networks with Multiplicative Noise via Policy Gradient

Topics include Optimal control, Multiplicative noise, Networks, Sensor placement, Actuator placement.

Showed that one can use policy gradient to automatically design the placement of sensors and actuators in a controller for linear systems with multiplicative noise. Achieved by encoding the preference for certain kinds of sparsity patterns with sparsity-promoting convex regularizers in the objective function.

We give algorithms for designing near-optimal sparse controllers using policy gradient with applications to control of systems corrupted by multiplicative noise, which is increasingly important in emerging complex dynamical networks. Various regularization schemes are examined and incorporated into the optimization by the use of gradient, subgradient, and proximal gradient methods. Numerical experiments on a large networked system show that the algorithms converge to performant sparse mean-square stabilizing controllers.

## Introduction

Emerging highly distributed networked dynamical systems, such as critical infrastructure for power, water, and transportation, are high-dimensional and increasingly instrumented with new sensing, actuation, and communication technologies. A key problem is to design high performance control architectures that limit the number of actuators, sensors, and actuator-sensor communication links to reduce complexity and cost. Sparse control architectures may be crucial for managing complexity in emerging complex networks, but require solution of extremely difficult mixed combinatorial-continuous optimization problems.

There is a variety of performance metrics and optimization methodology for sparse control architecture design in the recent literature. Examples include structural rank conditions from Liu et al.; Ruths and Ruths; Olshevsky, controllability and observability Gramians from Pasqualetti et al.; Summers et al.; Tzoumas et al.; Jadbabaie et al., and optimal and robust control metrics from Hassibi et al.; Polyak et al.; Jovanović and Dhingra; Summers; Taha et al.; Zare and Jovanović, which are optimized via greedy algorithms, convex and mixed-integer optimization, and randomization.

Here we develop methods for sparse optimal control design in dynamical networks with multiplicative noise via policy gradient algorithms with sparsity-inducing regularization. Multiplicative noise arises in many networked systems when the weights of edges connecting nodes are stochastic in time. The noise is thus on the system parameters themselves and has a fundamentally different effect on the state evolution than additive noise, and indeed can lead to dramatic robustness issues.

In Section 2 we formulate the problem and discusses a policy gradient approach to optimal control design for linear-quadratic systems with multiplicative noise. In Section 3 we propose several sparse control design methods for sensor and actuator selection and communication network design using gradient, subgradient, and proximal algorithms. In Section 4 we present numerical experiments to illustrate the results. Section 5 concludes.
