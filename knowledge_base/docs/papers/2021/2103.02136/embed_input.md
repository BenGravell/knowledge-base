Toward a Scalable Upper Bound for a CVaR-LQ Problem

Topics include Optimal control, Control, Conditional value at risk, Dynamic programming.

We study a linear-quadratic, optimal control problem on a discrete, finite time horizon with distributional ambiguity, in which the cost is assessed via Conditional Value-at-Risk (CVaR). We take steps toward deriving a scalable dynamic programming approach to upper-bound the optimal value function for this problem. This dynamic program yields a novel, tunable risk-averse control policy, which we compare to existing state-of-the-art methods.

## Introduction

The standard approach to stochastic optimal control is to evaluate a random cumulative cost in expectation. However, this approach is not designed to protect against worst-case circumstances. This limitation motivates robust optimal control and related methods, such as minimax model predictive control and mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control.

Robust methods typically assume bounded disturbances, which excludes certain common noise models, such as Gaussian noise. A technique to alleviate this restriction is to use a *risk-averse* formulation, in which a random cost is assessed via *exponential utility*. Here, the objective takes the form ${\mathcal{J}_{\gamma}{(x,\pi)}}:={\frac{1}{\gamma}{\log\left( {E_{x}^{\pi}{(e^{{\gammaZ}/2})}} \right)}}$, where $Z \geq 0$ is a random cumulative cost, $\pi$ is a control policy, $x$ is an initial condition, and $\gamma > 0$ is a risk-aversion parameter.^11^1One may consider $\gamma < 0$, which corresponds to a *risk-seeking* perspective....

Potential areas for future work include studying the infinite-horizon case, characterizing the extent to which the upper bound approximation parameterized by $L$ is tight, and elucidating the connections between the choice of $L$ and the maximal covariance $\Sigma$.

Further numerical experiments, potentially with higher-dimensional or more realistic application-specific examples, are needed to ascertain whether the proposed approach may be a superior alternative to LEQR in certain application domains.

### Definition 4.7 ($\overline{\Gamma}$)

a *scalable* upper bound to a CVaR linear-quadratic optimal control problem with distributional ambiguity.

### Proof 4.14 (Theorem 4.8. ‣ 4 Analysis of a Value Iteration Algorithm ‣ Toward a Scalable Upper Bound for a CVaR-LQ Problem"))

In the case of linear dynamics with Gaussian noise and quadratic costs, the problem of optimizing $\mathcal{J}_{\gamma}{(x,\pi)}$ is commonly called LEQR control. For a fixed $\gamma > 0$, a Riccati recursion is used to derive the optimal value functions and the optimal control law, which is linear state-feedback....
