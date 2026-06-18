Robust Multi-rate Predictive Control Using Multi-step Prediction Models Learned from Data

Topics include Predictive control, Stability analysis, Robustness, Uncertainty, Control.

This note extends a recently proposed algorithm for model identification and robust MPC of asymptotically stable, linear time-invariant systems subject to process and measurement disturbances. Independent output predictors for different steps ahead are estimated with Set Membership methods. It is here shown that the corresponding prediction error bounds are the least conservative in the considered model class. Then, a new multi-rate robust MPC algorithm is developed, employing said multi-step predictors to robustly enforce constraints and stability against disturbances and model uncertainty, and to reduce conservativeness. A simulation example illustrates the effectiveness of the approach.

## Introduction

In a recent paper, we presented a unitary approach to model identification and robust Model Predictive Control (MPC) design for linear, asymptotically stable, discrete time systems subject to process and measurement disturbances. A Set Membership (SM) identification approach was used to obtain multi-step prediction models used in the cost function definition, while state and control constraints were tightened by propagating the uncertainty bound of a simulation model, tuned using the knowledge of the multi-step models and the associated error intervals....

## Problem statement, identification algorithm, and error bounds

Figure 3: Input variable. Dash-dotted line: $\overline{U}{(k)}$, solid line: U (k), dashed lines: tightened constraints (23b), dotted lines: absolute constraints.

Figure 4: Output variable. Solid line: z (k), dashed line: $\hat{\overline{Z}}{(j)}$, line with circles: open loop response.

The input $\overline{U}{(j)}$ will be computed by MPC, while the term $K{({{X{(j)}} - {\overline{X}{(j)}}})}$ aims to reduce the error between the state $\overline{X}{(j)}$ of a suitably defined nominal dynamic system and the actual value of $X{(j)}$, available at time $k = {j\overline{p}}$. The gain $K$ is chosen such that $\overline{F} = {\overline{A} + {\overline{B}K}}$ is Schur stable, which is possible thanks to Assumption 3.\
The nominal dynamic system is defined based on:

The multi-step models previously introduced can not be directly used in existing robust MPC schemes. Therefore we propose a new multirate MPC approach where the predicted behavior of the system is optimized by considering a prediction/control horizon of $N_{p}$ "long" steps, with index ${j \in {\mathbb{N}}},$ each one consisting of $\overline{p}$ "short" sampling times with index $k$. Note that the "short" sampling interval is the one assumed for the true system. The optimal control problem is thus solved at every long step $j$ (i.e....

For consistency, the following assumption is required.

with $p \in {\mathbb{N}}$. The system can be expressed in ARX (autoregressive-exogenous) form as

### Assumption 1

The value of $\overline{d}$ is assumed to be available from prior knowledge, and/or it can also be estimated from data, see e.g., whereas $\overline{v}$ is not necessarily known.\
Using the SM method presented in, the following predictors of order $o$ can...
