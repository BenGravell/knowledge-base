Suboptimal Coverings for Continuous Spaces of Control Tasks

Topics include Control, Learning.

We propose the α-suboptimal covering number to characterize multi-task control problems where the set of dynamical systems and/or cost functions is infinite, analogous to the cardinality of finite task sets. This notion may help quantify the function class expressiveness needed to represent a good multi-task policy, which is important for learning-based control methods that use parameterized function approximation. We study suboptimal covering numbers for linear dynamical systems with quadratic cost (LQR problems) and construct a class of multi-task LQR problems amenable to analysis. For the scalar case, we show logarithmic dependence on the "breadth" of the space. For the matrix case, we present experiments 1) measuring the efficiency of a particular constructive cover, and 2) visualizing the behavior of two candidate systems for the lower bound.

## Introduction

An advanced control system such as a mobile robot may be required to perform many different tasks. If the task set is finite, like selecting between "map an environment" and "deliver a package", then its size is naturally quantified by the number of tasks. If the task set is infinite, like delivering packages with arbitrary mass and inertial properties, then its size is not so easily quantified. Even if the task space is equipped with a metric or measure, these structures may be only weakly linked to the diversity of behavior required for good performance on all tasks.

Our interest in this issue is motivated by multi-task paradigms in learning-based control, where the policy is selected from a parameterized family of functions that map state and task parameters directly to actions. As the task space expands from a singleton set, we expect to need a more expressive class of functions to represent a good multi-task policy. In this work, we propose the *$\alpha$-suboptimal covering number* to capture this idea....

In this paper, we introduced and motivated the $\alpha$-suboptimal covering number to quantify infinite task spaces for multi-task control problems. We defined a particular class of multi-task linear-quadratic regulator problems amenable to analysis of the $\alpha$-suboptimal covering number, and showed logarithmic dependency on the problem "breadth" parameter $\theta$ in the scalar case. Towards analogous results for the matrix case, we presented empirical studies intended to shed light on possible proof techniques....

After extending our current results to the matrix case, in future work the analysis can be applied to other classes of multi-task LQR problems including variations in $A,Q,R$, discrete time, and stochastic dynamics. It will be interesting to see if there are major differences between LQR variants. We also hope that suboptimal covers and covering numbers will be a useful tool for analyzing how the size of the task space affects the required expressiveness of function classes used in practice as multi-task policies, such as neural networks.

In the scalar system, the GCC matrix Riccati equation. ‣ 3 Theoretical results ‣ Suboptimal coverings for continuous spaces of control tasks")) reduces to the quadratic equation
