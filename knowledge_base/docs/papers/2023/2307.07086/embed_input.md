Value-Gradient Iteration with Quadratic Approximate Value Functions

Topics include Real-time systems, Control, Value-gradient iteration.

We propose a method for designing policies for convex stochastic control problems characterized by random linear dynamics and convex stage cost. We consider policies that employ quadratic approximate value functions as a substitute for the true value function. Evaluating the associated control policy involves solving a convex problem, typically a quadratic program, which can be carried out reliably in real-time. Such policies often perform well even when the approximate value function is not a particularly good approximation of the true value function. We propose value-gradient iteration, which fits the gradient of value function, with regularization that can include constraints reflecting known bounds on the true value function. Our value-gradient iteration method can yield a good approximate value function with few samples, and little hyperparameter tuning. We find that the method can find a good policy with computational effort comparable to that required to just evaluate a control policy via simulation.

## Introduction

We consider convex approximate dynamic programming (ADP) policies for convex stochastic control problems, which involve systems with known random linear dynamics and convex stage costs. Evaluating an ADP policy reduces to solving a convex optimization problem involving a convex approximate value function. We focus on fitting quadratic approximate value functions, and refer to the associated policies as quadratic approximate dynamic programming (QADP) policies. While QADP policies are optimal for problems with convex quadratic stage cost, they can also serve as effective heuristics for other problem types....

In this work, we propose an approximate value iteration method for finding quadratic approximate value functions for convex stochastic control problems, which we refer to as *value-gradient iteration* (VGI). In principle, an optimal value function may be found by iterating the Bellman operator, which maps real-valued functions on the state space to real-valued functions on the state space \[\]. Since it is not possible in general to exactly represent functions on $\text{R}^{n}$, we incorporate a function approximation step after each application of the Bellman operator, a general approach called fitted value iteration (FVI)....

## Conclusion

In this work, we propose value-gradient iteration, a method for finding a quadratic approximate value function for convex stochastic control. The method is an approximation of value iteration, and we show how we may compute the gradient of the Bellman operator image to fit the gradient of the approximate value function in each iteration. By fitting the gradient of the approximate value function instead of the approximate value function itself, we can find a good policy using far less simulation data....

### Ridge regularization

### Quadratic approximate value functions

In this section, we present three numerical examples, which involve a box-constrained LQR problem, a commitment planning problem with an alternative investments fund, and a supply chain optimization problem. Comparisons with other ADP methods are given in §7.

It is sufficient to approximate the gradient since constant offsets in the value function have no impact on the associated ADP policy. In addition, the gradient of the value function carries more information than the value function itself....
