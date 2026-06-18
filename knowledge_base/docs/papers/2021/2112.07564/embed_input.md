Linear Quadratic Control with Risk Constraints

We propose a new risk-constrained formulation of the classical Linear Quadratic (LQ) stochastic control problem for general partially-observed systems. Our framework is motivated by the fact that the risk-neutral LQ controllers, although optimal in expectation, might be ineffective under relatively infrequent, yet statistically significant extreme events. To effectively trade between average and extreme event performance, we introduce a new risk constraint, which explicitly restricts the total expected predictive variance of the state penalty by a user-prescribed level. We show that, under certain conditions on the process noise, the optimal risk-aware controller can be evaluated explicitly and in closed form. In fact, it is affine relative to the minimum mean square error (mmse) state estimate. The affine term pushes the state away from directions where the noise exhibits heavy tails, by exploiting the third-order moment~(skewness) of the noise....

## Introduction

In the problem of Linear Quadratic (LQ) stochastic control, one is typically interested in optimizing average control performance for linear systems of the form

where $x_{t} \in {\mathbb{R}}^{n}$ is the state, $y_{t} \in {\mathbb{R}}^{m}$ is the measured output, $u_{t}$ is input, and $w_{t}$, $v_{t}$ are process and measurement noise disturbances. A standard approach is to minimize the expectation of the following quadratic cost comprising of stage-wise input and state penalties up to a horizon $N$

We studied a novel risk-aware formulation of the classical Linear Quadratic control problem, where we minimize average performance, subject to predictive variance constraints. This gives rise to risk-aware controllers which trade between average performance and protection against uncommon but strong random disturbances. Our formulation is well-defined for general noise distributions, without requiring the existence of the respective moment generating functions. We characterized the optimal control laws for general partially-observed systems, which are affine with respect to the minimum mean-square state estimate....

Moving forward, there are numerous interesting research directions. First, our formulation places more emphasis on regulating the state at the cost of increased control effort. To mitigate this, we could potentially include input power constraints in the quadratic formulation (6. ‣ 3 Quadratic Reformulation of Risk-Constrained LQ Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.")). Another open problem is explicitly computing the optimal control (29....

As a result, for every $t \geq 0$, it is true that, as $N\rightarrow\infty$,

If $\mu^{\ast}$ is finite, then the policy $u^{\ast}{(\mu^{\ast})}$ is optimal for the primal problem (6. ‣ 3 Quadratic Reformulation of Risk-Constrained LQ Control ‣ Linear Quadratic Control with Risk Constraints This work was supported by the AFOSR under grant FA9550-19-1-0265 (Assured Autonomy in Contested Environments) and by the ARL under grant DCIST CRA W911NF-17-2-0181.")), and this is the case as long as (6....

### Theorem 5 (LQ Risk-Aware Controllers)

where matrices $Q,R$ are design choices.
