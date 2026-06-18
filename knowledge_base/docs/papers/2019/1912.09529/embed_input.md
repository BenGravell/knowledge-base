Learning Convex Optimization Control Policies

Many control policies used in various applications determine the input or action by solving a convex optimization problem that depends on the current state and some parameters. Common examples of such convex optimization control policies (COCPs) include the linear quadratic regulator (LQR), convex model predictive control (MPC), and convex control-Lyapunov or approximate dynamic programming (ADP) policies. These types of control policies are tuned by varying the parameters in the optimization problem, such as the LQR weights, to obtain good performance, judged by application-specific metrics. Tuning is often done by hand, or by simple methods such as a crude grid search. In this paper we propose a method to automate this process, by adjusting the parameters using an approximate gradient of the performance metric with respect to the parameters. Our method relies on recently developed methods that can efficiently evaluate the derivative of the solution of a convex optimization problem with respect to its parameters. We illustrate our method on several examples.

## Introduction

### Convex optimization control policies

We consider the control of a stochastic dynamical system with known dynamics, using a control policy that determines the input or action by solving a convex optimization problem. We call such policies *convex optimization control policies* (COCPs). Many practical policies have this form, including the first modern control policy, the linear quadratic regulator (LQR). In LQR, the convex optimization problem has quadratic objective and linear equality constraints, and so can be solved explicitly, yielding the familiar linear control policy....

### Nonconvex optimization control policies (NCOCPs)

An NCOCP is an optimization-based control policy that is evaluated by solving a *nonconvex* optimization problem. Parameters in NCOCPs can be tuned in the same way that we tune COCPs in this paper. Although the solution to a nonconvex optimization problem might be nonunique or hard to find, one can differentiate a local solution map to a smooth nonconvex optimization problem by implicitly differentiating the KKT conditions. This is done in, where the authors define an MPC-based NCOCP.

In the numerical instances, we pick the number of simulations $K$ so that the variance of $\hat{J}{(\theta)}$ is sufficiently small, and we tune the step-size schedule $\alpha^{k}$ for each problem. BPTT is susceptible to exploding and vanishing gradients, which can make learning difficult. This issue can be mitigated by gradient clipping and regularization, which we do in some of our experiments.

## Examples of COCPs

with variables $w^{+}$ and $z$ and parameters $\theta = {(\mu,\gamma,S)}$, where $\mu \in \text{R}^{n}$, $\gamma \in \text{R}_{+}$, and $S \in \text{R}^{n \times n}$. In a Markowitz formulation, $\mu$ is set to the empirical mean $\mu^{mark}$ of the returns, and $S$ is set to the square root of the return covariance $\Sigma^{mark}$. With these values for the parameters, the linear term in the objective represents the expected return of the post-trade portfolio $w^{+}$, and the quadratic term represents the risk. A trade-off between the risk and return is determined by the choice of the risk-aversion parameter $\gamma$....

Control policies in general, and COCPs in particular, are judged by application-specific metrics; these metrics are evaluated using simulation with historical or simulated values of the...
