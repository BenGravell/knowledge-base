Learning-based Predictive Control for Linear Systems: A Unitary Approach

Topics include Model predictive control, Predictive control, Robustness, Uncertainty, Datasets, Control, Learning, Learning-based model predictive control, Constraint satisfaction, Robust control.

A comprehensive approach addressing identification and control for learningbased Model Predictive Control (MPC) for linear systems is presented. The design technique yields a data-driven MPC law, based on a dataset collected from the working plant. The method is indirect, i.e. it relies on a model learning phase and a model-based control design one, devised in an integrated manner. In the model learning phase, a twofold outcome is achieved: first, different optimal p-steps ahead prediction models are obtained, to be used in the MPC cost function; secondly, a perturbed state-space model is derived, to be used for robust constraint satisfaction. Resorting to Set Membership techniques, a characterization of the bounded model uncertainties is obtained, which is a key feature for a successful application of the robust control algorithm. In the control design phase, a robust MPC law is proposed, able to track piece-wise constant reference signals, with guaranteed recursive feasibility and convergence properties.

## Introduction

The idea of combining identification and control for efficient and reliable control systems design, starting from data collected on the plant, has a long standing history, see the survey paper. Indirect approaches are characterized by an initial phase aimed at estimating the model of the plant, while a following one concerns the model-based control synthesis. In this framework different solutions have been proposed, as thoroughly discussed .

## Problem formulation: a unitary approach to learning-based MPC

We

where $z$ is the output, $v$ an additive process disturbance, $y$ the output measure, and $d$ an additive measurement noise.

here $u$ is the system input. In, ${\overline{\theta}}^{} \in {\mathbb{R}}^{{{2n} + p} - 1}$ is a vector of unknown system parameters. The value of $n$ is not known a priori as well.
