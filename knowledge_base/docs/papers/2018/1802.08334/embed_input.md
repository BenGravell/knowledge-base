Learning without Mixing: Towards a Sharp Analysis of Linear System Identification

Topics include System identification, Generalization, Learning, Mixing, Ordinary least squares, Linear systems, Linear dynamical system.

We prove that the ordinary least-squares (OLS) estimator attains nearly minimax optimal performance for the identification of linear dynamical systems from a single observed trajectory. Our upper bound relies on a generalization of Mendelson's small-ball method to dependent data, eschewing the use of standard mixing-time arguments. Our lower bounds reveal that these upper bounds match up to logarithmic factors. In particular, we capture the correct signal-to-noise behavior of the problem, showing that more unstable linear systems are easier to estimate. This behavior is qualitatively different from arguments which rely on mixing-time calculations that suggest that unstable systems are more difficult to estimate. We generalize our technique to provide bounds for a more general class of linear response time-series.

## Introduction

System identification---the problem of estimating the parameters of a dynamical system given a time series of its trajectories--- is a fundamental problem in time-series analysis, control theory, robotics, and reinforcement learning. Despite its importance, sharp, non-asymptotic analyses for the sample complexity of system identification are rare. In particular, it is not known how many trajectories required to identify the parameters of an unknown *linear* system.

We focus on the problem of identifying a discrete-time *linear dynamical system* from an observed trajectory. Such systems are described by two parameter matrices $A_{\ast}$ and $B_{\ast}$, and the dynamics evolve according to the law $X_{t + 1} = {{A_{\ast}X_{t}} + {B_{\ast}u_{t}} + \eta_{t}}$, where $X_{t} \in {\mathbb{R}}^{d}$ is the state of the system, $u_{t}$ is the input of the system, and $\eta_{t} \in {\mathbb{R}}^{d}$ denotes unobserved process noise.

In the statistics and machine learning literature, correlated data is usually dealt with using mixing-time arguments, which relies on fast convergence to a stationary distribution that allows correlated samples to be treated roughly as if they were independent. While this approach has been successfully used to develop generalization bounds for time-series data, a fundamental limitation of mixing-time arguments is that the bounds deteriorate when the underlying process is slower to mix. In the case of linear systems, this behavior is qualitatively incorrect.

## Discussion and future work

In this paper, we analyzed the the performance of the $\mathsf{O}\mathsf{L}\mathsf{S}$ estimator for the estimation of linear dynamics $X_{t + 1} = {{A_{\ast}X_{t}} + \eta_{t}}$ from a single trajectory $X_{0},X_{1},\ldots,X_{T}$, as a special case of linear estimation in time series. We show that, up to logarithmic factors, the $\mathsf{O}\mathsf{L}\mathsf{S}$ estimator attains an information-theoretic lower bound for ${\rho{(A_{\ast})}} < 1$, provided that $T \gtrsim \frac{d}{1 - {\rho{(A_{\ast})}}}$. Moreover, we present an analysis that eschews both mixing and concentration arguments for estimation in time series.

Our lower and upper bounds do not perfectly match, even when ${\rho{(A_{\ast})}} < 1$. We believe resolving these indiscrepancies may shed greater insight into learning in dynamical systems.
