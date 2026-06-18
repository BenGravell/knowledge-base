Convex Structured Controller Design

Topics include Structured control, Convex controller synthesis, Finite-horizon control, Decentralized control, Feedback constraints, Variable impedance, Nonlinear extensions.

Proposes a finite-horizon control objective that makes linear feedback synthesis convex even under arbitrary convex structure constraints on the feedback matrices. The paper is important because it sidesteps the usual nonconvexity of structured LQR, H2, and Hinf-like design by optimizing a surrogate tied to the inverse closed-loop map, enabling sparse, delayed, decentralized, and variable-impedance feedback designs with global solutions for the surrogate.

We consider the problem of synthesizing optimal linear feedback policies subject to arbitrary convex constraints on the feedback matrix. This is known to be a hard problem in the usual formulations (Htwo,Hinf,LQR) and previous works have focused on characterizing classes of structural constraints that allow efficient solution through convex optimization or dynamic programming techniques. In this paper, we propose a new control objective and show that this formulation makes the problem of computing optimal linear feedback matrices convex under arbitrary convex constraints on the feedback matrix. This allows us to solve problems in decentralized control (sparsity in the feedback matrices), control with delays and variable impedance control. Although the control objective is nonstandard, we present theoretical and empirical evidence that it agrees well with standard notions of control. We also present an extension to nonlinear control affine systems. We present numerical experiments validating our approach.

## INTRODUCTION

Linear feedback control synthesis is a classical topic in control theory and has been extensively studied in the literature. From the perspective of stochastic optimal control theory, the classical result is the existence of an optimal linear feedback controller for systems with linear dynamics, quadratic costs and gaussian noise (LQG systems) that can be computed via dynamic programming. However, if one imposes additional constraints on the feedback matrix (such as a sparse structure arising from the need to implement control in a decentralized fashion), the dynamic programming approach is no longer applicable.

## PROBLEM FORMULATION

Consider

Here $t = {0,1,2,\ldots,N}$ is the discrete time index, $x_{t} \in \mathbf{R}^{n}$ is the plant state, $w_{t} \in \mathbf{R}^{n}$ is an exogenous disturbance and $u_{t} \in \mathbf{R}^{n_{u}}$ is the control input.

Let

## Discussion and Related Work

There have been three major classes of prior work in synthesizing structured controllers: Frequency domain approaches, dynamic programming and nonconvex optimization approaches. We compare the relative merits of the different approaches in this section.

In

where $\parallel \cdot \parallel$ is typically the $\mathcal{H}_{2}$ or $\mathcal{H}_{\infty}$ norm. In general, these are solved by reparameterizing the problem in terms of a Youla parameter (via a nonlinear transformation), and imposing special conditions on $\mathcal{C}$ (like quadratic invariance) that guarantee that the constraints $\mathcal{C}$ can be translated into convex constraints on the Youla parameter. There are multiple limitations of these approaches:\
Only specific kinds of constraints can be imposed on the controller.
