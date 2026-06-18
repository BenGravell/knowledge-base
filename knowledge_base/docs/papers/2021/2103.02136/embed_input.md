Toward a Scalable Upper Bound for a CVaR-LQ Problem

Topics include Optimal control, Control, Conditional value at risk, Dynamic programming.

We study a linear-quadratic, optimal control problem on a discrete, finite time horizon with distributional ambiguity, in which the cost is assessed via Conditional Value-at-Risk (CVaR). We take steps toward deriving a scalable dynamic programming approach to upper-bound the optimal value function for this problem. This dynamic program yields a novel, tunable risk-averse control policy, which we compare to existing state-of-the-art methods.

## Introduction

The standard approach to stochastic optimal control is to evaluate a random cumulative cost in expectation. However, this approach is not designed to protect against worst-case circumstances. This limitation motivates robust optimal control and related methods, such as minimax model predictive control and mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control.

Robust methods typically assume bounded disturbances, which excludes certain common noise models, such as Gaussian noise. A technique to alleviate this restriction is to use a *risk-averse* formulation, in which a random cost is assessed via *exponential utility*. Here, the objective takes the form ${\mathcal{J}_{\gamma}{(x,\pi)}}:={\frac{1}{\gamma}{\log\left( {E_{x}^{\pi}{(e^{{\gammaZ}/2})}} \right)}}$, where $Z \geq 0$ is a random cumulative cost, $\pi$ is a control policy, $x$ is an initial condition, and $\gamma > 0$ is a risk-aversion parameter.^11^1One may consider $\gamma < 0$, which corresponds to a *risk-seeking* perspective.

In the case of linear dynamics with Gaussian noise and quadratic costs, the problem of optimizing $\mathcal{J}_{\gamma}{(x,\pi)}$ is commonly called LEQR control. For a fixed $\gamma > 0$, a Riccati recursion is used to derive the optimal value functions and the optimal control law, which is linear state-feedback. At each step $t$ of the recursion, it must be the case that the matrix $\Sigma^{- 1} - {\gamma{\overline{P}}_{t + 1}}$ is positive definite, where $\Sigma$ is the covariance of the process noise, and ${\overline{P}}_{t + 1}$ is the matrix obtained from step $t + 1$.

The *Conditional Value-at-Risk* (CVaR) functional, which was invented in the early 2000s by the financial engineering community, has potential to alleviate the above issues. The CVaR of $Z$ at level $\alpha \in {(0,1\rbrack}$ represents the expectation of the $\alpha \cdot {100\%}$ largest values of $Z$. The intuitive interpretation of CVaR and its quantitative characterization of risk aversion (in terms of a *fraction* of worst-case outcomes) are two reasons for its popularity in financial engineering (see and the references therein) and its emerging popularity in control (e.g., see ).
