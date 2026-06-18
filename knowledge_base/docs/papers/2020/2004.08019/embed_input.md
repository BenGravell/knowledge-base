Robust Control Design for Linear Systems via Multiplicative Noise

Topics include Robust control, Multiplicative noise, Linear systems, Stochastic systems, Uncertainty descriptions.

Algorithms for synthesizing robust controllers for linear systems using multiplicative noise as a design-time device. Leverages theoretical results on the equivalence of robustness to structured determinstic and stochastic uncertainties.

Robust stability and stochastic stability have separately seen intense study in control theory for many decades. In this work we establish relations between these properties for discrete-time systems and employ them for robust control design. Specifically, we examine a multiplicative noise framework which models the inherent uncertainty and variation in the system dynamics which arise in model-based learning control methods such as adaptive control and reinforcement learning. We provide results which guarantee robustness margins in terms of perturbations on the nominal dynamics as well as algorithms which generate maximally robust controllers.

## Introduction

Model-based learning control, which encompasses classical system identification (e.g. ) and adaptive control (e.g. ) as well as branches of modern reinforcement learning (e.g. ), universally uses a stochastic data model, where a model is estimated from data corrupted by random noise. A salient perennial issue in these methods is ensuring stability despite the presence of concomitant model errors; this is the problem of *robustness*.

Traditional methods for designing robust controllers include $\mathcal{H}_{\infty}$ control design, which treats modeling error as a worst-case or adversarial disturbance, robust optimization over parametric state-space uncertainty sets, which typically involve searching for shared Lyapunov functions via convex semidefinite programming, and certainty-equivalent control, which utilizes only a nominal model and ignores modeling error entirely....

This work gives an effective methodology for certifying robustness and designing robust controllers with favorable properties and flexibility relative to competing approaches.

Direct extensions to this work include finding sharper bounds, e.g., via alternate auxiliary systems analogous to the one used in Section 4, and handling nonlinear dependence of the dynamics and/or noise on states and inputs. Future work will integrate the results of this work with adaptive model-based learning control for an end-to-end control framework which gracefully transitions from maximal robustness to maximal performance according to empirical uncertainties.

Giving up optimization over $P$ and instead choosing $Q$ arbitrarily (later in Sec. 5, $Q$ will be chosen as the cost matrix of an LQR control design) and calculating the associated $P$, we obtain the following result:

If $B$ is singular, then $\lambda_{\max}$ becomes infinite.

Summing over all the noises,

Alternatively, in this paper we explore the connection between a special type of *stochastic stability* and *robust stability* and exploit this connection for robust control design. In particular, we use a *multiplicative noise* model where the noise is viewed as a representation of uncertainty in the nominal system model....
