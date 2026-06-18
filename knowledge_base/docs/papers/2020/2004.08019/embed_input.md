Robust Control Design for Linear Systems via Multiplicative Noise

Topics include Robust control, Multiplicative noise, Linear systems, Stochastic systems, Uncertainty descriptions.

Algorithms for synthesizing robust controllers for linear systems using multiplicative noise as a design-time device. Leverages theoretical results on the equivalence of robustness to structured determinstic and stochastic uncertainties.

Robust stability and stochastic stability have separately seen intense study in control theory for many decades. In this work we establish relations between these properties for discrete-time systems and employ them for robust control design. Specifically, we examine a multiplicative noise framework which models the inherent uncertainty and variation in the system dynamics which arise in model-based learning control methods such as adaptive control and reinforcement learning. We provide results which guarantee robustness margins in terms of perturbations on the nominal dynamics as well as algorithms which generate maximally robust controllers.

## Introduction

Model-based learning control, which encompasses classical system identification (e.g. ) and adaptive control (e.g. ) as well as branches of modern reinforcement learning (e.g. ), universally uses a stochastic data model, where a model is estimated from data corrupted by random noise. A salient perennial issue in these methods is ensuring stability despite the presence of concomitant model errors; this is the problem of *robustness*.

Alternatively, in this paper we explore the connection between a special type of *stochastic stability* and *robust stability* and exploit this connection for robust control design. In particular, we use a *multiplicative noise* model where the noise is viewed as a representation of uncertainty in the nominal system model. This framework is naturally disposed toward trading off performance and robustness according to uncertainty directions and magnitudes which can be estimated from trajectory data during model-based learning control. The study of multiplicative noise models has a long history in control theory.

In this paper we consider a fundamental question:\
*What is the set of perturbations to the system matrix where the perturbed system can be guaranteed stable, given knowledge only of the nominal system dynamics and stochastic stability of a system with multiplicative noise?*

We develop a result utilizing shared Lyapunov functions that establishes robust stability of a set of deterministic systems given stochastic (mean-square) stability of another system with multiplicative noise (Theorem 3.2).

## Conclusion and Future Work

This work gives an effective methodology for certifying robustness and designing robust controllers with favorable properties and flexibility relative to competing approaches.

Direct extensions to this work include finding sharper bounds, e.g., via alternate auxiliary systems analogous to the one used in Section 4, and handling nonlinear dependence of the dynamics and/or noise on states and inputs. Future work will integrate the results of this work with adaptive model-based learning control for an end-to-end control framework which gracefully transitions from maximal robustness to maximal performance according to empirical uncertainties.
