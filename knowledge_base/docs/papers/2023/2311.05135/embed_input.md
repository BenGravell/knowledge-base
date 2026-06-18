Improving Computational Efficiency for Powered Descent Guidance via Transformer-based Tight Constraint Prediction

Topics include Trajectory optimization, Safety, Neural networks, Transformers, Attention mechanisms, Time series, Computational complexity, Optimization, T-PDG, Powered descent.

In this work, we present Transformer-based Powered Descent Guidance (T-PDG), a scalable algorithm for reducing the computational complexity of the direct optimization formulation of the spacecraft powered descent guidance problem. T-PDG uses data from prior runs of trajectory optimization algorithms to train a transformer neural network, which accurately predicts the relationship between problem parameters and the globally optimal solution for the powered descent guidance problem. The solution is encoded as the set of tight constraints corresponding to the constrained minimum-cost trajectory and the optimal final time of landing. By leveraging the attention mechanism of transformer neural networks, large sequences of time series data can be accurately predicted when given only the spacecraft state and landing site parameters. When applied to the real problem of Mars powered descent guidance, T-PDG reduces the time for computing the 3 degree of freedom fuel-optimal trajectory, when compared to lossless convexification, from an order of 1-8 seconds to less than 500 milliseconds....

## Introduction

NASA's Moon to Mars Strategy establishes precision landing capabilities as one of the major technologies required for robust exploration and a sustained lunar presence. To accomplish precision landing in uncertain planetary entry, descent, and landing scenarios, safe and autonomous guidance trajectories must be computed on the order of milliseconds. Currently, precision guidance algorithms fall into two categories: direct and indirect methods. Direct methods discretize the continuous optimization problem and solve it as a parameter optimization problem by numerical optimization (often by primal-dual interior point methods (IPMs))....

Approaches for improving the computational efficiency of onboard direct guidance algorithms include custom solver implementations, storing previously-computed solutions in lookup tables, and informed initial guess strategies; Dueri et al. develop a custom second-order cone-programming (SOCP) IPM in C which exploits the structure of the planetary pinpoint landing powered descent problem to decrease run times by two to three orders of magnitude....

## Conclusion

This work presents T-PDG, a transformer-based approach to predict the solution of LCvx problems for real-time powered descent guidance. By leveraging the attention mechanism of transformer neural networks, T-PDG enables the millisecond-level prediction of optimal strategies which reduce the average runtime of the LCvx from over 1.5 seconds to under 500 milliseconds. Moreover, T-PDG ensures the feasibility of the final solution through a feasibility check and worst-case full solve....

Additional linear layers, dropout, and LayerNorm layers are also present in the transformer encoder layer. The full model was designed in PyTorch using torch.nn. The implemented tight constraints and optimal final time NNs for the 3-DoF PDG application (Section 5) both have $1 \times 9$-dimensional inputs which include the 3-dimensional initial velocity, 3-dimensional initial position, pointing angle, engine angle, and glideslope angle. Note that the final position and velocity are kept at zero since this application is a powered descent landing problem and reference frames can be adjusted accordingly for a varying final position....

### Identifying Optimal Strategies for Solving the Powered Descent Guidance Problem

Min allowed thrust of single engine (T1)
