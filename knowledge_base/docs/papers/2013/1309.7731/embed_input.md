Convex Structured Controller Design

Topics include Structured control, Convex controller synthesis, Finite-horizon control, Decentralized control, Feedback constraints, Variable impedance, Nonlinear extensions.

Proposes a finite-horizon control objective that makes linear feedback synthesis convex even under arbitrary convex structure constraints on the feedback matrices. The paper is important because it sidesteps the usual nonconvexity of structured LQR, H2, and Hinf-like design by optimizing a surrogate tied to the inverse closed-loop map, enabling sparse, delayed, decentralized, and variable-impedance feedback designs with global solutions for the surrogate.

We consider the problem of synthesizing optimal linear feedback policies subject to arbitrary convex constraints on the feedback matrix. This is known to be a hard problem in the usual formulations (Htwo,Hinf,LQR) and previous works have focused on characterizing classes of structural constraints that allow efficient solution through convex optimization or dynamic programming techniques. In this paper, we propose a new control objective and show that this formulation makes the problem of computing optimal linear feedback matrices convex under arbitrary convex constraints on the feedback matrix. This allows us to solve problems in decentralized control (sparsity in the feedback matrices), control with delays and variable impedance control. Although the control objective is nonstandard, we present theoretical and empirical evidence that it agrees well with standard notions of control. We also present an extension to nonlinear control affine systems. We present numerical experiments validating our approach.

## INTRODUCTION

Linear feedback control synthesis is a classical topic in control theory and has been extensively studied in the literature. From the perspective of stochastic optimal control theory, the classical result is the existence of an optimal linear feedback controller for systems with linear dynamics, quadratic costs and gaussian noise (LQG systems) that can be computed via dynamic programming. However, if one imposes additional constraints on the feedback matrix (such as a sparse structure arising from the need to implement control in a decentralized fashion), the dynamic programming approach is no longer applicable....

## PROBLEM FORMULATION

## CONCLUSION

We have argued that the framework developed seems promising and overcomes limitations of previous works on computationally tractable approaches to structured controller synthesis. Although the control objective used is non-standard, we have argued why it is a sensible objective, and we also presented numerical examples showing that it produces controllers outperforming other nonconvex approaches. Further, we proved suboptimality bounds that give guidance on when our solution is good even with respect to the original ($\mathcal{H}_{2}/\mathcal{H}_{\infty}$) metrics....

### Theorem III.3

### III-A PROOF OF CONVEXITY

The log-barrier for the semidefinite constraint can be rewritten as $\log\left( {\det\left( {t^{2} - {F(\mathbf{K})_{}^{- 1}F(\mathbf{K})^{- 1}}} \right)} \right)$ using Schur complements. The matrix $\left( {F(\mathbf{K})} \right)_{}^{- 1}\left( {F(\mathbf{K})} \right)^{- 1}$ is a symmetric positive definite block-tridiagonal matrix, which is a special case of a chordal sparsity pattern. This means that computing the gradient and Newton step for the log-barrier is efficient, with complexity growing as $O{(N)}$. Thus, at least for the case where the objective is the spectral norm, we can develop efficient interior point methods.

Consider a finite-horizon discrete-time linear system in state-space form:

Here $t = {0,1,2,\ldots,N}$ is the discrete time index, $x_{t} \in \mathbf{R}^{n}$ is the plant state, $w_{t} \in \mathbf{R}^{n}$ is an exogenous disturbance and $u_{t} \in \mathbf{R}^{n_{u}}$ is the control input. We employ static state feedback:

Let $\lambda_{\max}(M)$ denote the maximum eigenvalue of an $l \times l$ symmetric matrix $M$, $\lambda_{\min}(M)$ the minimum...
