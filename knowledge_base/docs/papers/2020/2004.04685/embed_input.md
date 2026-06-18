Risk-Constrained Linear-Quadratic Regulators

We propose a new risk-constrained reformulation of the standard Linear Quadratic Regulator (LQR) problem. Our framework is motivated by the fact that the classical (risk-neutral) LQR controller, although optimal in expectation, might be ineffective under relatively infrequent, yet statistically significant (risky) events. To effectively trade between average and extreme event performance, we introduce a new risk constraint, which explicitly restricts the total expected predictive variance of the state penalty by a user-prescribed level. We show that, under rather minimal conditions on the process noise (i.e., finite fourth-order moments), the optimal risk-aware controller can be evaluated explicitly and in closed form. In fact, it is affine relative to the state, and is always internally stable regardless of parameter tuning. Our new risk-aware controller: i) pushes the state away from directions where the noise exhibits heavy tails, by exploiting the third-order moment (skewness) of the noise; ii) inflates the state penalty in riskier directions, where both the noise covariance and the state penalty are simultaneously large.

## Introduction

Achieving good performance in expectation is often insufficient in the design of stochastic control systems, especially when dealing with modern, critical applications. Examples appear naturally in many areas, including wireless industrial control, energy, finance, robotics, networking, and safety, to name a few. Indeed, occurrence of less probable, non-typical or unexpected events might lead the underlying dynamical system to experience shocks with possibly catastrophic consequences, e.g., a drone diverging too much from a given trajectory in a hostile environment, or an autonomous vehicle crashing onto a wall or hitting a pedestrian.

where $\mu$ controls the trade-off between average performance and risk. As $\mu$ increases, we move from the risk-neutral to the maximally risk-aware controller ${u_{t}^{\ast}{(\infty)}} = {{- x_{t}} - {\beta/2}}$, which treats the noise as adversarial---see Fig. 1.

In this paper, we propose a new risk-aware reformulation of the LQR problem, in which the standard LQR objective is minimized subject to an explicit and tunable risk constraint. Our contributions are as follows.

--New Risk Measure. We introduce the cumulative expected one-step predictive variance of the associated state penalty as a new risk measure for LQR control. In this way, our risk-constraint formulation ensures not only a small LQR cost, but also guaranteed statistical variability of the state penalty.

## Conclusion and Future Work

We presented a new risk-aware reformulation of the classical LQR problem, where we introduce a new risk measure to be used as an explicit and tunable risk constraint, along with the standard LQR objective. By restricting the expected cumulative predictive variance of the state penalties, we can decrease the variability of the state at will, protecting the system against uncommon but strong random disturbances. The optimal controller enjoys a simple closed-form expression with clear interpretation, is always stable and is easy to tune.

Moving forward, our framework opens up many directions for extensions and future research. First, we would like to note that our analysis does not depend on the constraints having the same matrix $Q$ as in the cost. In fact, we can define our risk constraint as
