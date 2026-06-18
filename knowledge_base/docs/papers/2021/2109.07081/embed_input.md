Optimizing Trajectories with Closed-Loop Dynamic SQP

Topics include Trajectory optimization, Sequential quadratic programming, Closed-loop, Nonlinear optimization, Robot control.

Introduces closed-loop dynamic SQP, which integrates feedback gain computation within the SQP iteration structure, improving robustness and convergence for trajectory optimization compared to open-loop sequential approaches.

Indirect trajectory optimization methods such as Differential Dynamic Programming (DDP) have found considerable success when only planning under dynamic feasibility constraints. Meanwhile, nonlinear programming (NLP) has been the state-of-the-art approach when faced with additional constraints (e.g., control bounds, obstacle avoidance). However, a naïve implementation of NLP algorithms, e.g., shooting-based sequential quadratic programming (SQP), may suffer from slow convergence - caused from natural instabilities of the underlying system manifesting as poor numerical stability within the optimization. Re-interpreting the DDP closed-loop rollout policy as a sensitivity-based correction to a second-order search direction, we demonstrate how to compute analogous closedloop policies (i.e., feedback gains) for constrained problems. Our key theoretical result introduces a novel dynamic programmingbased constraint-set recursion that augments the canonical “cost-to-go” backward pass. On the algorithmic front, we develop a hybrid-SQP algorithm incorporating DDP-style closedloop rollouts, enabled via efficient parallelized computation of the feedback gains.

## Introduction

Trajectory optimization forms the backbone of model-based optimal control with myriad applications in robot mobility and manipulation.

Let $N \in {\mathbb{N}}_{> 0}$ be some fixed planning horizon.

Solution methods generally fall into one of two approaches: optimal control-based (indirect methods), or optimization-based (direct methods). The former leverages necessary conditions of optimality for optimal control, such as dynamic programming (DP), while the latter treats the problem as a pure mathematical optimization program.

Lacking constraints beyond dynamic feasibility, ubiquitous indirect methods such as Differential Dynamic Programming (DDP) and its Gauss-Newton relaxation, iterative Linear Quadratic Regulator (iLQR) rely upon the DP recursion to split the full-horizon planning problem into a sequence of one-step optimizations, and alternate between a backward and forward pass through the time-steps.

Re-interpreting the canonical DDP closed-loop rollout as a *sensitivity-based correction to a second-order search direction*, we demonstrate how to compute a locally affine approximation to the constrained perturbation policies, i.e., a set of feedback gains similar to those employed by the DDP rollouts. Our key theoretical result states that in the constrained setting, one must first compute an optimal perturbation sequence about the current trajectory iterate by solving a full-horizon QP (as opposed to the one-step DP backward recursion), and then augment the canonical cost-to-go backward pass with a constraint-set recursion.
