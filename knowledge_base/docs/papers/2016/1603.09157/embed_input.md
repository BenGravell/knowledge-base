Linear System Identification via EM with Latent Disturbances and Lagrangian Relaxation

Topics include Convex optimization, Semidefinite programming, Nonconvex optimization, System identification, Optimization, Lagrangian relaxation.

In the application of the Expectation Maximization algorithm to identification of dynamical systems, internal states are typically chosen as latent variables, for simplicity. In this work, we propose a different choice of latent variables, namely, system disturbances. Such a formulation elegantly handles the problematic case of singular state space models, and is shown, under certain circumstances, to improve the fidelity of bounds on the likelihood, leading to convergence in fewer iterations. To access these benefits we develop a Lagrangian relaxation of the nonconvex optimization problems that arise in the latent disturbances formulation, and proceed via semidefinite programming.

## Introduction

Linear time invariant (LTI) state-space models provide a useful approximation of dynamical system behavior in a multitude of applications. In situations where models cannot be derived from first principles, some form of data-driven modeling, i.e. system identification, is appropriate. This paper is concerned with identification of discrete-time LTI models of the form

For convenience, all unknown model parameters are denoted by the variable $\theta = {\{\mu,\Sigma_{1},\Sigma_{w},\Sigma_{v},}$\

The rewards for this additional complexity are threefold. First, the proposed method elegantly handles identification of *singular* state-space models (i.e. $n_{w} < n_{x}$), a case to which the standard formulation of EM over latent states is not applicable, without modification. Secondly, this approach naturally ensures stability of the model at each iteration. Finally, when the *magnitude* of the disturbances (i.e. $\Sigma_{w}$) is small, we show that use of latent disturbances produces better approximations to the likelihood, leading to convergence in fewer iterations.

## Conclusion

In this paper, we have formulated the EM algorithm over latent disturbances, rather than states, for the identification of linear dynamical systems. Our main contribution is the use of Lagrangian relaxation to obtain a convex approximation of the challenging maximization step, guaranteed not to decrease the likelihood at each iteration. Though more computationally complex, this formulation with latent disturbances allows EM to be applied to singular state-space models, where latent states based methods break down.

Extension of this approach to the identification of nonlinear models shall be the subject of future research. In the nonlinear case, two major challenges arise during the formulation of EM with latent disturbances. First, the E step (c.f. Section 3.1) now involves a nonlinear disturbance smoothing problem, for which no closed form solution is known to exist. In recent decades, *sequential Monte Carlo* (SMC) methods have emerged as effective tools for overcoming similar difficulties, having already proved useful in nonlinear, non-Gaussian *state smoothing* and *disturbance filtering* problems.
