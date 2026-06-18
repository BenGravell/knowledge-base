Convex Hulls of Reachable Sets

We study the convex hulls of reachable sets of nonlinear systems with bounded disturbances and uncertain initial conditions. Reachable sets play a critical role in control, but remain notoriously challenging to compute, and existing over-approximation tools tend to be conservative or computationally expensive. In this work, we characterize the convex hulls of reachable sets as the convex hulls of solutions of an ordinary differential equation with initial conditions on the sphere. This finite-dimensional characterization unlocks an efficient sampling-based estimation algorithm to accurately over-approximate reachable sets. We also study the structure of the boundary of the reachable convex hulls and derive error bounds for the estimation algorithm. We give applications to neural feedback loop analysis and robust MPC.

## Introduction

Forward reachability analysis plays a critical role in control theory and robust controller design. Generally, it entails characterizing all states that a system can reach at any time in the future. As such, reachability analysis allows certifying the performance of feedback loops under disturbances and designing controllers with robustness properties. In robust model predictive control (MPC) for instance, it is used to construct tubes around nominal state trajectories to ensure that constraints are satisfied in the presence of external disturbances.

that characterizes all states that are reachable at time $t$ for some disturbance $w$ and initial state $x^{0}$.

Our main contribution is a new characterization of the convex hulls of reachable sets of dynamical systems of the form, under smoothness assumptions of $f$, $g$, $\mathcal{W}$, and $\mathcal{X}_{0}$ (see Assumptions LABEL:assumption:f-LABEL:assumption:X0). Specifically, denoting by $\text{H}{(A)}$ the convex hull of a set $A \subset {\mathbb{R}}^{n}$, we show that

This result unlocks an approach (Algorithm LABEL:alg:1) to efficiently estimate the convex hulls $\text{H}{(\mathcal{X}_{t})}$ by integrating an ODE from a sample of initial conditions. This approach allows efficiently tackling challenging problems such as analyzing the robustness of neural network controllers (see Section 11). This characterization also informs the design of a robust MPC controller (see Algorithm LABEL:alg:mpc) that we demonstrate on a robust spacecraft control task.

## Discussion and insights

In Table 1, we summarize the different problems used to derive $\text{ODE}_{d^{0}}$ and ultimately prove Theorem LABEL:thm:hull_F.

At first sight, $\text{OCP}_{d}$ and $\text{BVP}_{d}$ to ℝ^𝑛 ‣ 5 Proof of Theorem ‣ Convex Hulls of Reachable Sets") suggest using Algorithm LABEL:alg:2 to reconstruct the convex hull of the reachable set $\text{H}{(\mathcal{X}_{T})}$ (similar ideas are investigated in \[Gornov2015\] and in \[Baier2009\]). However, this procedure can be computationally expensive. Also, $\text{OCP}_{d}$ is generally non-convex, so Algorithm LABEL:alg:2 could be prone to local minima and under-estimating the reachable sets. Thus, Algorithm LABEL:alg:2 may be unsuitable for applications that require efficient reachable set over-approximations.
