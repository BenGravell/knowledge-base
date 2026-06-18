State Space Models vs. Multi-step Predictors in Predictive Control: Are State Space Models Complicating Safe Data-driven Designs?

Topics include Optimal control, Predictive control, Safety, Uncertainty, System identification, Control, State space.

This paper contrasts recursive state space models and direct multi-step predictors for linear predictive control. We provide a tutorial exposition for both model structures to solve the following problems: 1. stochastic optimal control; 2. system identification; 3. stochastic optimal control based on the estimated model. Throughout the paper, we provide detailed discussions of the benefits and limitations of these two model parametrizations for predictive control and highlight the relation to existing works. Additionally, we derive a novel (partially tight) constraint tightening for stochastic predictive control with parametric uncertainty in the multi-step predictor.

## Introduction

Model predictive control (MPC) is an optimization-based control strategy, which is applicable to general MIMO systems and directly accounts for state and input constraints \[. Typically, first a parametric prediction model is identified. In addition to noise and disturbances, the resulting parametric error then needs to be considered to ensure satisfaction of safety critical constraints. In this paper, we study data-driven predictive control problems using two different model parametrizations: state space models and multi-step predictors, i.e., models that skip the sequential state propagation and directly predict $k$-steps into the future.

### Related work

### Open-issues

Lemma 3 could be improved by directly using $\theta_{k} \sim {\mathcal{N}{({\hat{\theta}}_{k},\Sigma_{\theta,k})}}$. Numerical comparisons regarding computational complexity and closed-loop performance would be beneficial. Given the respective benefits, unifying the parametrizations in a hybrid model structure is a promising research direction (cf., DiRec/DIRMO strategies ).

The state space identification problem becomes simpler if we assume noise-free state measurements (cf. Cor. 1). On the other hand, the identification of multi-step predictors (Lemma 2) for long horizons ($k \gg 1$) simplifies if only measurement noise is present. For comparison, early MPC approaches based on impulse responses, e.g. dynamic matrix control, are restricted to "disturbances on the output". OBFs, a structured parametrization of, also allow for a simple identification under measurement noise....

### Proof

For the derived mean and variance bound, there exist parameters ${\overset{\sim}{\theta}}_{k} \in \Theta_{\delta,k}$, such that the bounds hold individually with equality (although the combined bound is not tight). Computing the constants requires maximizing a quadratic function over an ellipsoid, which is an SDP \[45, Prop. 2.2\], and a simple upper bound is given by:

Historically, MPC emerged from the process control industry using impulse/step response models, which are simple to identify/adapt. These approaches have early been extended to robustly account for the parametric uncertainty of such finite impulse response (FIR) models....
