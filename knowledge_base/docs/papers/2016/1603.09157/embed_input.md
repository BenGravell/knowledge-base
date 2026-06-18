Linear System Identification via EM with Latent Disturbances and Lagrangian Relaxation

Topics include Convex optimization, Semidefinite programming, Nonconvex optimization, System identification, Optimization, Lagrangian relaxation.

In the application of the Expectation Maximization algorithm to identification of dynamical systems, internal states are typically chosen as latent variables, for simplicity. In this work, we propose a different choice of latent variables, namely, system disturbances. Such a formulation elegantly handles the problematic case of singular state space models, and is shown, under certain circumstances, to improve the fidelity of bounds on the likelihood, leading to convergence in fewer iterations. To access these benefits we develop a Lagrangian relaxation of the nonconvex optimization problems that arise in the latent disturbances formulation, and proceed via semidefinite programming.

## Introduction

Linear time invariant (LTI) state-space models provide a useful approximation of dynamical system behavior in a multitude of applications. In situations where models cannot be derived from first principles, some form of data-driven modeling, i.e. system identification, is appropriate. This paper is concerned with identification of discrete-time LTI models of the form

where $x_{t} \in {\mathbb{R}}^{n_{x}}$ denotes the system state, and $u_{t} \in {\mathbb{R}}^{n_{u}}$, $y_{t} \in {\mathbb{R}}^{n_{y}}$ denote the observed input and output, respectively. The disturbances (a.k.a. process noise), $w_{t} \in^{n_{w}}$ and measurement noise, $v_{t}$, are modeled as zero mean Gaussian white noise processes, while the uncertainty in the initial condition $x_{1}$ is modeled by a normal distribution, i.e.

Extension of this approach to the identification of nonlinear models shall be the subject of future research. In the nonlinear case, two major challenges arise during the formulation of EM with latent disturbances. First, the E step (c.f. Section 3.1) now involves a nonlinear disturbance smoothing problem, for which no closed form solution is known to exist. In recent decades, *sequential Monte Carlo* (SMC) methods have emerged as effective tools for overcoming similar difficulties, having already proved useful in nonlinear, non-Gaussian *state smoothing* and *disturbance filtering* problems.

Second, nonlinearity of the model complicates the Lagrangian relaxation of the M step; e.g. the bound ${\hat{J}}_{\lambda}{(\eta)}$ cannot be evaluated analytically, as the supremum (in ) requires optimization of a function that is no longer quadratic in $x$. To proceed, one might approximate the simulation error terms in $Q_{3}{(\gamma,\theta_{k})}$ with the *linearized simulation error*, introduced in, to which the Lagrangian relaxation presented in this work can be applied with little modification....

We introduce $\eta = {\{ E,F,K,L,C,D,\Sigma_{v},P\}}$ to group the implicit model parameters, $\Sigma_{v}$ and $P \in {\mathbb{S}}_{+ +}^{n_{x}}$, into a single variable. Here $P$ represents a model stability certificate, the role of which is made precise in Lemma 6. Henceforth, ${\overline{J}}_{\lambda}{(\eta)}$ denotes Lagrangian relaxation with the implicit dynamics constraint....
