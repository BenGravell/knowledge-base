Linear Quadratic Control with Risk Constraints

We propose a new risk-constrained formulation of the classical Linear Quadratic (LQ) stochastic control problem for general partially-observed systems. Our framework is motivated by the fact that the risk-neutral LQ controllers, although optimal in expectation, might be ineffective under relatively infrequent, yet statistically significant extreme events. To effectively trade between average and extreme event performance, we introduce a new risk constraint, which explicitly restricts the total expected predictive variance of the state penalty by a user-prescribed level. We show that, under certain conditions on the process noise, the optimal risk-aware controller can be evaluated explicitly and in closed form. In fact, it is affine relative to the minimum mean square error (mmse) state estimate. The affine term pushes the state away from directions where the noise exhibits heavy tails, by exploiting the third-order moment~(skewness) of the noise.

## Introduction

In the problem of Linear Quadratic (LQ) stochastic control, one is typically interested in optimizing average control performance for linear systems of the form

where $x_{t} \in {\mathbb{R}}^{n}$ is the state, $y_{t} \in {\mathbb{R}}^{m}$ is the measured output, $u_{t}$ is input, and $w_{t}$, $v_{t}$ are process and measurement noise disturbances. A standard approach is to minimize the expectation of the following quadratic cost comprising of stage-wise input and state penalties up to a horizon $N$

where matrices $Q,R$ are design choices.

--New Risk-Constrained Formulation. We introduce a new risk-constrained formulation for the problem of LQ control in the case of partially-observed systems. The standard LQ objective is minimized subject to a total expected predictive variance risk constraint with respect to the state penalties. By tuning the risk constraint, we can trade between average performance and statistical variability of the state penalties.

--General Noise Models. Contrary to the LEQG approach, our risk-constrained formulation is well-defined for general noise distributions, provided the associated fourth-order moments of the process noise are finite; thus, heavy-tailed or skewed noises are supported within our framework. For fully-observed systems, the optimal control law can be explicitly characterized under the same condition of finite fourth-order moments. In the case of general partially-observed systems, in order to characterize the optimal controller, we require the additional sufficient condition that all higher-order moments of the process noise exist.

## Conclusion

We studied a novel risk-aware formulation of the classical Linear Quadratic control problem, where we minimize average performance, subject to predictive variance constraints. This gives rise to risk-aware controllers which trade between average performance and protection against uncommon but strong random disturbances. Our formulation is well-defined for general noise distributions, without requiring the existence of the respective moment generating functions. We characterized the optimal control laws for general partially-observed systems, which are affine with respect to the minimum mean-square state estimate.
