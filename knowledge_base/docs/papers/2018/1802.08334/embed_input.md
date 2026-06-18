Learning without Mixing: Towards a Sharp Analysis of Linear System Identification

Topics include System identification, Generalization, Learning, Mixing, Ordinary least squares, Linear systems, Linear dynamical system.

We prove that the ordinary least-squares (OLS) estimator attains nearly minimax optimal performance for the identification of linear dynamical systems from a single observed trajectory. Our upper bound relies on a generalization of Mendelson's small-ball method to dependent data, eschewing the use of standard mixing-time arguments. Our lower bounds reveal that these upper bounds match up to logarithmic factors. In particular, we capture the correct signal-to-noise behavior of the problem, showing that more unstable linear systems are easier to estimate. This behavior is qualitatively different from arguments which rely on mixing-time calculations that suggest that unstable systems are more difficult to estimate. We generalize our technique to provide bounds for a more general class of linear response time-series.

## Introduction

System identification---the problem of estimating the parameters of a dynamical system given a time series of its trajectories--- is a fundamental problem in time-series analysis, control theory, robotics, and reinforcement learning. Despite its importance, sharp, non-asymptotic analyses for the sample complexity of system identification are rare. In particular, it is not known how many trajectories required to identify the parameters of an unknown *linear* system....

We focus on the problem of identifying a discrete-time *linear dynamical system* from an observed trajectory. Such systems are described by two parameter matrices $A_{\ast}$ and $B_{\ast}$, and the dynamics evolve according to the law $X_{t + 1} = {{A_{\ast}X_{t}} + {B_{\ast}u_{t}} + \eta_{t}}$, where $X_{t} \in {\mathbb{R}}^{d}$ is the state of the system, $u_{t}$ is the input of the system, and $\eta_{t} \in {\mathbb{R}}^{d}$ denotes unobserved process noise....

In many systems, we do not observe $X_{t}$ directly, but only view $CX_{t}$ for a short matrix $C \in {\mathbb{R}}^{n_{o} \times n}$, where $n_{0} \leq n$. Hazan et al. provide filtering techniques to minimize regret for diagonalizable matrices; it would be interesting to understand the sample complexity for estimating arbitrary matrices with these limited observations.

Ultimately, we would like to understand what sequences of control inputs $u_{t}$ yield the most accurate estimation of the system $(A_{\ast},B_{\ast})$. This would inform adaptive algorithms which adjust the sequence $u_{t}$ in a sequential fashion, and online algorithms which ensure low regret relative to a given cost functional over time.

### Lower Bounds for Linear System Identification

Scalar linear system. In this case the states $X_{t}$ and the parameter $A_{\ast}$ are scalars, and denoted $a_{\ast} = A_{\ast}$. For ${|a_{\ast}|} \leq 1$, we can apply Theorem 2.1 with block length $k = {\mathcal{O}{({T/{\log{({1/\delta})}}})}}$. This then guarantees that ${|{\hat{a} - a_{\ast}}|} \leq {\mathcal{O}\left( \sqrt{{\log{({1/\delta})}}/\left( {T{\sum_{t = 1}^{k_{\ast}}a_{\ast}^{2t}}} \right)} \right)}$ with probability $1 - \delta$....

The proof of Theorem 2.4 is outlined in Section 4, and technical details are deferred to Appendix D. We remark that the conclusion of Theorem 2.4 still holds if one replaces the $(k,\Gamma_{sb},p)$ small-ball...
