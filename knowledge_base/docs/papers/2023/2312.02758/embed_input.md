Stochastic Data-Driven Predictive Control: Regularization, Estimation, and Constraint Tightening

Topics include Predictive control, Control, Stochastic data-driven predictive control.

Data-driven predictive control methods based on the Willems' fundamental lemma have shown great success in recent years. These approaches use receding horizon predictive control with nonparametric data-driven predictors instead of model-based predictors. This study addresses three problems of applying such algorithms under unbounded stochastic uncertainties: 1) tuning-free regularizer design, 2) initial condition estimation, and 3) reliable constraint satisfaction, by using stochastic prediction error quantification. The regularizer is designed by leveraging the expected output cost. An initial condition estimator is proposed by filtering the measurements with the one-step-ahead stochastic data-driven prediction. A novel constraint-tightening method, using second-order cone constraints, is presented to ensure high-probability chance constraint satisfaction. Numerical results demonstrate that the proposed methods lead to satisfactory control performance in terms of both control cost and constraint satisfaction, with significantly improved initial condition estimation.

## Introduction

Classical model-based control enables simple but powerful control design by considering typically parametric mathematical abstractions of system behaviors, known as models. However, this comes at the cost of additional modeling and identification effort, which constitutes the majority of the budget in model-based control design, in terms of both time and cost. In this regard, the concept of data-driven control provides an appealing alternative that designs the controller directly from data without parametric identification.

In this work, we focus on data-driven predictive control (DDPC), the data-driven counterpart to model predictive control (MPC). Similar to MPC, it solves a finite-horizon optimal control problem in a receding horizon fashion, but with nonparametric data-driven predictors instead of model-based predictors. Data-driven predictors for linear systems can be constructed by using the so-called Willems' fundamental lemma, which characterizes all possible system behaviors with finite data.

While these predictors work well with deterministic data, showing equivalence to model-based design, they become ill-defined with stochastic data. Multiple works have stressed this issue by introducing an inner problem that finds the 'optimal' predictor under some statistical principle, e.g., Fiedler and Lucia; Yin et al.; Breschi et al.. This idea is known as indirect DDPC.

## Conclusion

This work discusses several modifications in stochastic data-driven predictive control (DDPC) algorithms. They provide a tuning-free regularizer design in the control cost, improved initial condition estimation, and reliable constraint satisfaction. These are achieved by evaluating the expected cost, designing a Kalman filter, and formulating convex constraint tightening terms, respectively. These modifications pave the way for providing theoretical guarantees for DDPC algorithms under general unbounded stochasticity.
