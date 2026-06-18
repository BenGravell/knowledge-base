Convex Hulls of Reachable Sets

We study the convex hulls of reachable sets of nonlinear systems with bounded disturbances and uncertain initial conditions. Reachable sets play a critical role in control, but remain notoriously challenging to compute, and existing over-approximation tools tend to be conservative or computationally expensive. In this work, we characterize the convex hulls of reachable sets as the convex hulls of solutions of an ordinary differential equation with initial conditions on the sphere. This finite-dimensional characterization unlocks an efficient sampling-based estimation algorithm to accurately over-approximate reachable sets. We also study the structure of the boundary of the reachable convex hulls and derive error bounds for the estimation algorithm. We give applications to neural feedback loop analysis and robust MPC.

## Introduction

Forward reachability analysis plays a critical role in control theory and robust controller design. Generally, it entails characterizing all states that a system can reach at any time in the future. As such, reachability analysis allows certifying the performance of feedback loops under disturbances and designing controllers with robustness properties. In robust model predictive control (MPC) for instance, it is used to construct tubes around nominal state trajectories to ensure that constraints are satisfied in the presence of external disturbances.

In this work, we study the following reachability analysis problem. Let $n \in {\mathbb{N}}$ be the state dimension, $f:{{{\mathbb{R}} \times {\mathbb{R}}^{n}}\rightarrow{\mathbb{R}}^{n}}$ and $g:{{{\mathbb{R}} \times {\mathbb{R}}^{n}}\rightarrow{\mathbb{R}}^{n \times n}}$ be functions for the dynamics, and ${\mathcal{W},\mathcal{X}_{0}} \subset {\mathbb{R}}^{n}$ be bounded sets of disturbances and initial conditions. Given a time $T > 0$ and an initial state $x^{0} \in \mathcal{X}_{0}$, we consider systems defined by the ordinary differential equation (ODE)

We showed that estimating the convex hulls of reachable sets of nonlinear systems with disturbances and uncertain initial conditions is equivalent to studying the solutions of an ODE with initial conditions on the sphere. This result is a significantly simpler finite-dimensional characterization of the convex hulls of reachable sets that could inform the design of efficient reachability analysis algorithms for nonlinear systems.

Algorithm LABEL:alg:1 has two main limitations. First, the accuracy of sampling-based techniques decreases as the number of uncertain variables increases. Thanks to our characterization result, the sample space is only of dimension $({n - 1})$ as opposed to an infinite-dimensional space of disturbances. However, obtaining provably-accurate approximations for high-dimensional systems in reasonable computation time remains difficult. This limitation is unfortunately shared by other reachability analysis algorithms for nonlinear systems....

### Corollary 6.6 (Naive error bound)

The Pontryagin Maximum Principle (PMP) \[Pontryagin1987, Agrachev2004, Trelat2012\] gives necessary conditions of optimality for $\text{OCP}_{d}$....
