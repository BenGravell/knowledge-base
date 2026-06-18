Low-Complexity Learning of Linear Quadratic Regulators from Noisy Data

Topics include Data-driven control, Linear quadratic regulator, Noisy data, Semidefinite programming, Direct linear quadratic regulator, Robust control, Reinforcement learning, Sample complexity.

Designs LQR controllers directly from noisy trajectory data with finite-sample, relative-error guarantees and an SDP implementation. It is a concise data-driven LQR counterpart to the noiseless LMI formulas, emphasizing robustness without a probabilistic noise model.

This paper considers the Linear Quadratic Regulator problem for linear systems with unknown dynamics, a central problem in data-driven control and reinforcement learning. We propose a method that uses data to directly return a controller without estimating a model of the system. Sufficient conditions are given under which this method returns a stabilizing controller with guaranteed relative error when the data used to design the controller are affected by noise. This method has low complexity as it only requires a finite number of samples of the system response to a sufficiently exciting input, and can be efficiently implemented as a semi-definite program. Further, the method does not require assumptions on the noise statistics, and the relative error nicely scales with the noise magnitude.

## Introduction

Control theory is witnessing an increasing renewed interest towards *data-driven* (*data-based*) control. This terminology refers to all those cases where the dynamics of the system are unknown and the control law must be designed using data alone. This can be done either by identifying a model of the system from data and then use the model for control design, or by directly designing the control law bypassing the system identification (ID) step.

*The Linear Quadratic Regulator problem*

This paper considers the *infinite horizon* Linear Quadratic Regulator (LQR) problem for linear time-invariant systems, which is one of the problems more studied in the control literature. Besides its practical relevance, this problem is a prime example of the challenges encountered in data-driven control. Specifically, we consider the problem of computing the solution to the LQR problem from a finite set of (noisy) data collected from the system.\
Early data-driven methods for LQR can be traced back to the theory of adaptive control systems, and include the popular *self-tuning regulators* and *policy iteration* schemes.

Our contribution is a new approach to design LQ controllers from noisy data with guaranteed performance.

*Stability and performance guarantees*. As long as the noise satisfies suitable inequalities our method returns a stabilizing controller with quantitative *relative error* (gap between the computed solution and the unknown optimal controller) and the error nicely scales with the noise magnitude.

As , we focus on non-iterative methods which do not require an initial stabilizing controller, as instead typically assumed in iterative methods. The main difference with respect to is that our method is direct and assumes no noise model.\
The advantage of not relying on noise statistics is twofold. Although the solution to LQR can be interpreted as the one minimizing the variance of the system's output in response to white noise, experimental data need not comply with such setting, and show correlation and dependence (dependence breaks the *i.i.d.* assumption used in ).
