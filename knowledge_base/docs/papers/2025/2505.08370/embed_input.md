Distributionally Robust LQG with Kullback-Leibler Ambiguity Sets

Topics include Partial observability, Optimal control, Robustness, Uncertainty, Control, Linear quadratic Gaussian.

The Linear Quadratic Gaussian (LQG) controller is known to be inherently fragile to model misspecifications common in real-world situations. We consider discrete-time partially observable stochastic linear systems and provide a robustification of the standard LQG against distributional uncertainties on the process and measurement noise. Our distributionally robust formulation specifies the admissible perturbations by defining a relative entropy based ambiguity set individually for each time step along a finite-horizon trajectory, and minimizes the worst-case cost across all admissible distributions. We prove that the optimal control policy is still linear, as in standard LQG, and derive a computational scheme grounded on iterative best response that provably converges to the set of saddle points. Finally, we consider the case of endogenous uncertainty captured via decision-dependent ambiguity sets and we propose an approximation scheme based on dynamic programming.

## Introduction

The Linear Quadratic Regulator (LQG) is a cornerstone of control theory, and has been applied across several domains ranging from engineering, to economics, to computer science. It involves controlling a linear system subject to additive disturbances via the design of a control policy that minimizes a quadratic cost function. For linear systems, quadratic costs and additive Gaussian noise, it is well-known that the resulting optimal policy is linear in the observations. However, in practice, the system dynamics are often only approximately known, and the noise is not necessarily Gaussian....

We consider a generalization of the finite-horizon LQG framework for discrete-time linear stochastic systems subject to model mismatch. We interpret the problem as a zero-sum game between the controller and a distribution chosen from an ambiguity set that may change at each time step. Each ambiguity set is represented as a ball defined in the Kullback-Leibler (KL) divergence centered at a nominal Gaussian distribution. The goal of the control designer is then to synthesize a control policy that minimizes the worst-case expected cost. We refer to this problem as the Distributionally Robust LQG (DR-LQG) problem with KL ambiguity sets.

## Conclusions

For discrete-time stochastic linear systems, we propose an output feedback controller capable of robustifying the standard LQG approach against distributional ambiguity affecting both process and measurement noise by relying on KL ambiguity sets. Our analysis shows that linear policies are still optimal despite the added complexity; moreover, the worst-case distribution is still a Gaussian. These insights led us to design an iterated best response dyanmics scheme that provably convergences to the set of saddle points and admits closed-form expressions....

### Lemma 6

The bound in Proposition depends only on the covariance matrices $\Sigma_{p}$ and $\Sigma_{q}$, making it analogous to the Gelbrich bound for the type-2 Wasserstein distance. Further, the derivation can be easily extended to the case of non-zero mean distributions, since the differential entropy is translation invariant....
