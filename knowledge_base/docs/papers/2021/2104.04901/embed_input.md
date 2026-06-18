Global Convergence of Policy Gradient Primal-dual Methods for Risk-constrained LQRs

While the techniques in optimal control theory are often model-based, the policy optimization (PO) approach directly optimizes the performance metric of interest. Even though it has been an essential approach for reinforcement learning problems, there is little theoretical understanding on its performance. In this paper, we focus on the risk-constrained linear quadratic regulator (RC-LQR) problem via the PO approach, which requires addressing a challenging non-convex constrained optimization problem. To solve it, we first build on our earlier result that an optimal policy has a time-invariant affine structure to show that the associated Lagrangian function is coercive, locally gradient dominated and has local Lipschitz continuous gradient, based on which we establish strong duality. Then, we design policy gradient primal-dual methods with global convergence guarantees in both model-based and sample-based settings. Finally, we use samples of system trajectories in simulations to validate our methods.

## Introduction

The techniques in conventional optimal control theory often require an explicit dynamical model. Such a model-based idea is relatively easy to provide theoretical guarantees but is usually sensitive to modeling inaccuracy. Policy optimization (PO) methods, as an end-to-end approach, directly search for an optimal control policy to minimize a performance metric of interest and has advantages in scenarios where the dynamical model is complex and difficult to identify. In fact, it has been proved to be an essential approach for applications of reinforcement learning (RL), e.g., robotic in-hand manipulation.

However, there are only a few theoretical guarantees on PO methods as they often involve challenging non-convex optimization problems. To study their convergence and sample complexities, there has recently been a resurgent interest in PO methods for classical control problems. For example, the seminal work studies the well-known linear quadratic regulator (LQR) problem via PO methods. Though an optimal policy can be simply parameterized by a gain matrix, the quadratic cost is non-convex in the gain matrix space....

## Concluding Remarks

In this paper, we have proposed a policy gradient primal-dual framework with global convergence guarantees to solve the RC-LQR problem with a variance-like constraint. Specifically, we have shown here strong duality, to establish the global convergence, which in fact can be extended to the case of multiple constraints. Such a framework can also be utilized to study linear quadratic tracking.

### Proof

For any $\mu > 0$, $\mathcal{L}{(X,\mu)}$ is gradient dominated over its $\alpha$-sublevel set, i.e.,

Our model-based primal-dual method is summarized in Algorithm 1. In general, the primal iteration will not converge to a feasible solution unless the subdifferential of the dual function is a singleton. Fortunately, Theorem 1 implies that $X^{k}$ is the unique minimizer of $\mathcal{L}{(X,\mu^{k})}$. Since $X^{k}$ is always able to stabilize the system, the subgradient (actually gradient) $d^{k}$ and $\mu^{k}$ are uniformly bounded. Jointly with the concavity of $D{(\mu)}$, it follows from \[26, Theorem 3\] that Algorithm 1 converges globally.

Since the LQR problem only focuses on the quadratic regulation performance, the closed-loop system may be largely jeopardized by low-probability yet...
