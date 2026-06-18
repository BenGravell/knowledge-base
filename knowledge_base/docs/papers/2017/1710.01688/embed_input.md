On the Sample Complexity of the Linear Quadratic Regulator

This paper addresses the optimal control problem known as the Linear Quadratic Regulator in the case when the dynamics are unknown. We propose a multi-stage procedure, called Coarse-ID control, that estimates a model from a few experimental trials, estimates the error in that model with respect to the truth, and then designs a controller using both the model and uncertainty estimate. Our technique uses contemporary tools from random matrix theory to bound the error in the estimation procedure. We also employ a recently developed approach to control synthesis called System Level Synthesis that enables robust control design by solving a convex optimization problem. We provide end-to-end bounds on the relative error in control cost that are nearly optimal in the number of parameters and that highlight salient properties of the system to be controlled such as closed-loop sensitivity and optimal control magnitude. We show experimentally that the Coarse-ID approach enables efficient computation of a stabilizing controller in regimes where simple control schemes that do not take the model uncertainty into account fail to stabilize the true system.

## Introduction

Having surpassed human performance in video games and Go, there has been a renewed interest in applying machine learning techniques to planning and control. In particular, there has been a considerable amount of effort in developing new techniques for *continuous control* where an autonomous system interacts with a physical environment. A tremendous opportunity lies in deploying these data-driven systems in more demanding interactive tasks including self-driving vehicles, distributed sensor networks, and agile robotics....

Unfortunately, there are no clean baselines delineating the possible control performance achievable given a fixed amount of data collected from a system. Such baselines would enable comparisons of different techniques and would allow engineers to trade off between data collection and action in scenarios with high uncertainty. Typically, a key difficulty in establishing baselines is in proving *lower bounds* that state the minimum amount of knowledge needed to achieve a particular performance, regardless of method....

There are two parallel problems here. First, it would be of interest to determine system identification algorithms that are tuned to particular control tasks. In the Coarse-ID control approach, the estimation and control are completely decoupled. However, it may be beneficial to inform the identification algorithm about the desired cost, resulting in improved sample complexity.

From a different perspective, Policy Gradient and Q-Learning methods applied to LQR could yield important insights about the pros and cons of such methods. There are classic papers on Q-Learning for LQR, but these use asymptotic analysis. Recently, the first such analysis for Policy Gradient has appeared, though the precise scaling with respect to system parameters is not yet understood. Providing clean nonasymptotic bounds here could help provide a rapprochement between machine learning and adaptive control, with optimization negotiating the truce.

### Corollary 3.3

The last inequality uses (2.7) combined with the inequality ${({a + b})}^{2} \leq {2{({a^{2} + b^{2}})}}$. Furthermore, by Lemma 2.1 and (2.7), with probability at least $1 - {\delta/2}$,

### Theorem 4.1

In this paper, we attempt to build a foundation for a theoretical understanding of how machine learning interfaces with control by analyzing one of the most...
