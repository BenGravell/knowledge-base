Learning-based Predictive Control for Linear Systems: A Unitary Approach

Topics include Model predictive control, Predictive control, Robustness, Uncertainty, Datasets, Control, Learning, Learning-based model predictive control, Constraint satisfaction, Robust control.

A comprehensive approach addressing identification and control for learningbased Model Predictive Control (MPC) for linear systems is presented. The design technique yields a data-driven MPC law, based on a dataset collected from the working plant. The method is indirect, i.e. it relies on a model learning phase and a model-based control design one, devised in an integrated manner. In the model learning phase, a twofold outcome is achieved: first, different optimal p-steps ahead prediction models are obtained, to be used in the MPC cost function; secondly, a perturbed state-space model is derived, to be used for robust constraint satisfaction. Resorting to Set Membership techniques, a characterization of the bounded model uncertainties is obtained, which is a key feature for a successful application of the robust control algorithm. In the control design phase, a robust MPC law is proposed, able to track piece-wise constant reference signals, with guaranteed recursive feasibility and convergence properties....

## Introduction

The idea of combining identification and control for efficient and reliable control systems design, starting from data collected on the plant, has a long standing history, see the survey paper. Indirect approaches are characterized by an initial phase aimed at estimating the model of the plant, while a following one concerns the model-based control synthesis. In this framework different solutions have been proposed, as thoroughly discussed in....

## Notation

## Conclusions

The proposed unitary approach to learning-based MPC for linear systems allows one to design a control law based on a dataset collected from the working plant. The obtained data-driven controller is able to effectively deal with constraints and track desired output references. The method relies on two phases: model learning and model-based control design, that are conceived to limit conservativeness while still robustly guaranteeing constraint satisfaction. To achieve this result, multi-step predictors and the related uncertainty bounds are derived and exploited to compute the state-space model employed in the MPC design....

### Proof 2

For any $p \in {\lbrack 1,\overline{p}\rbrack}$, consider a given value of ${\hat{\theta}}^{(p)}$. From and, the error between the true system output and the predicted one is, for all $k \in {\mathbb{Z}}$:

### State observer and tube-based control approach

$k$ is the discrete time index and $\mathbb{Z}$ is the set of non negative integers. The transpose of matrix $M$ is $M^{T}$. We denote with $\mathbf{1}_{x}$ a column vector with all its elements equal to one and of dimension $x$, and with $0_{x,y}$ a matrix of zeros with $x$ rows and $y$ columns, wheras $I_{x}$ denotes the identity matrix of dimension $x$....

## Problem formulation: a unitary approach to learning-based MPC

We consider a discrete-time, linear time-invariant (LTI), single-input/single-output (SISO) system of order $n$ described by the following autoregressive exogenous (ARX) structure ($\cdot^{T}$ is the matrix transpose operator):

where $z$ is the output, $v$ an additive process disturbance, $y$ the output measure, and $d$ an additive measurement noise. For a given integer $p \geq 1$, the regressor ${\varphi_{z}^{(p)}{(k)}} \in {\mathbb{R}}^{{{2n} + p} - 1}$ is defined as:
