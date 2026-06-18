Optimizing Trajectories with Closed-Loop Dynamic SQP

Topics include Trajectory optimization, Sequential quadratic programming, Closed-loop, Nonlinear optimization, Robot control.

Introduces closed-loop dynamic SQP, which integrates feedback gain computation within the SQP iteration structure, improving robustness and convergence for trajectory optimization compared to open-loop sequential approaches.

Indirect trajectory optimization methods such as Differential Dynamic Programming (DDP) have found considerable success when only planning under dynamic feasibility constraints. Meanwhile, nonlinear programming (NLP) has been the state-of-the-art approach when faced with additional constraints (e.g., control bounds, obstacle avoidance). However, a naïve implementation of NLP algorithms, e.g., shooting-based sequential quadratic programming (SQP), may suffer from slow convergence - caused from natural instabilities of the underlying system manifesting as poor numerical stability within the optimization. Re-interpreting the DDP closed-loop rollout policy as a sensitivity-based correction to a second-order search direction, we demonstrate how to compute analogous closedloop policies (i.e., feedback gains) for constrained problems. Our key theoretical result introduces a novel dynamic programmingbased constraint-set recursion that augments the canonical “cost-to-go” backward pass. On the algorithmic front, we develop a hybrid-SQP algorithm incorporating DDP-style closedloop rollouts, enabled via efficient parallelized computation of the feedback gains....

## Introduction

Trajectory optimization forms the backbone of model-based optimal control with myriad applications in robot mobility and manipulation. The problem formulation is as follows: consider a robotic system with state $x \in {\mathbb{R}}^{n}$, control input $u \in {\mathbb{R}}^{m}$, subject to the discrete-time dynamics:

Let $N \in {\mathbb{N}}_{> 0}$ be some fixed planning horizon. Given some initial state $x_{0}$, the trajectory optimization problem is as follows:

In this work, we re-interpret DDP rollout policies from a perspective of sensitivity-based corrections, and use this insight to develop algorithms for computing analogous policies for constrained problems. We incorporate the resulting closed-loop rollouts within a shooting-based SQP framework, and demonstrate significant improvements in convergence speed over a standard SQP implementation using open-loop rollouts.

Our work opens several avenues for future research. First, a key bottleneck of SQP involves solving the QP sub-problem at each iteration to compute a "nominal" perturbation sequence. This may be achieved with fast, but potentially, less-accurate unconstrained solvers (e.g., augmented-Lagrangian iLQR), that additionally compute the desired sensitivity gains using an efficient Riccati recursion. Second, leveraging recent results on differentiating through the solution of *general* convex problems, the sensitivity-based computations may be applied to the sequential-*convex*-programming algorithm....

We now characterize the correctness of this DP recursion in the following theorem; the proof is provided in Appendix D.

Since $\delta{\breve{\pi}}_{k}^{\ast}{({\deltax_{k}})}$ is the solution of an unconstrained convex quadratic, the argument $0$ is redundant for the sensitivity matrix $K_{k}$. This will not be the case in the constrained setting.

Practically, we compute the Jacobians $K_{k}^{u}{(\gamma)}$ efficiently using iLQR and a straightforward application of the Implicit Function Theorem. We initialized the solver with the QP sub-problem solution ${\mathbf{δ}}{\mathbf{u}}^{\ast}$, and found only a handful of iterations were needed to converge, particularly since problem (III-C) is convex.

Solution methods generally fall into one of two approaches: optimal control-based (indirect methods), or optimization-based (direct methods)....
