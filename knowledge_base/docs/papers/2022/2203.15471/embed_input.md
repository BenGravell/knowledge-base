State Space Models vs. Multi-step Predictors in Predictive Control: Are State Space Models Complicating Safe Data-driven Designs?

Topics include Optimal control, Predictive control, Safety, Uncertainty, System identification, Control, State space.

This paper contrasts recursive state space models and direct multi-step predictors for linear predictive control. We provide a tutorial exposition for both model structures to solve the following problems: 1. stochastic optimal control; 2. system identification; 3. stochastic optimal control based on the estimated model. Throughout the paper, we provide detailed discussions of the benefits and limitations of these two model parametrizations for predictive control and highlight the relation to existing works. Additionally, we derive a novel (partially tight) constraint tightening for stochastic predictive control with parametric uncertainty in the multi-step predictor.

## Introduction

Model predictive control (MPC) is an optimization-based control strategy, which is applicable to general MIMO systems and directly accounts for state and input constraints \[. Typically, first a parametric prediction model is identified. In addition to noise and disturbances, the resulting parametric error then needs to be considered to ensure satisfaction of safety critical constraints. In this paper, we study data-driven predictive control problems using two different model parametrizations: state space models and multi-step predictors, i.e., models that skip the sequential state propagation and directly predict $k$-steps into the future.

## Contribution

We consider a stochastic optimal control problem for linear systems, as typically arising in MPC, and provide a tutorial-style exposition based on state space models and multi-step predictors, respectively.^11^1Although MPC relies on a receding horizon implementation, we initially focus on the open-loop problem to simplify the exposition. Closed-loop implementations with corresponding caveats are discussed in Section IV-D. First, we reformulate this problem as equivalent quadratic programs (QPs) for both parametrizations (Sec. II). Then, we use a maximum likelihood estimate (MLE) for the system identification (Sec. III).

## Stochastic predictive control

We first state the control problem (Sec. II-A) and convert it into a deterministic QP (Sec. II-B). Then, we introduce the multi-step predictors, derive an equivalent QP (Sec. II-C), and provide a discussion (Sec. II-D).

## II-A Problem setup

We consider a linear discrete-time system of the form

## Conclusion

We have provided a tutorial-style exposition of data-driven stochastic predictive control using state space models or multi-step predictors. In particular, we have investigated the challenges associated with parametric uncertainty in both model parametrizations. Tube-based methods for state space models need to trade-off computational complexity and conservatism, and require additional offline designs with various free design parameters. On the other hand, we derived simple (partially tight) bounds for multi-step predictors (Lemma 3), which do not suffer from similar conservatism.

scalability for long prediction horizons;
