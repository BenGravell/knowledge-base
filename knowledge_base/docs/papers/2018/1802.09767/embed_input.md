On Multi-step Prediction Models for Receding Horizon Control

Topics include Model predictive control, Predictive control, Robustness, Control, Multi-Step prediction models.

The derivation of multi-step-ahead prediction models from sampled data of a linear system is considered. A dedicated prediction model is built for each future time step of interest. In addition to a nominal model, the set of all models consistent with data and prior information is derived as well, making the approach suitable for robust control design within a Model Predictive Control framework. The resulting parameter identification problem is solved through a sequence of convex programs, overcoming the non-convexity arising when identifying 1-step prediction models with an output-error criterion. At the same time, the derived models guarantee a worst-case error which is always smaller than the one obtained by iterating models identified with a 1-step prediction error criterion.

## Introduction

This manuscript contains technical details of recent results developed by the authors on learning-based model predictive control for linear time invariant systems.

## Problem formulation

## Conclusions

We presented an approach to derive multi-step prediction models, and the related uncertainty bounds, for an unknown linear system affected by additive measurement disturbance. Under suitable assumptions, we demonstrated convergence of the bounds to their theoretical minimum based on the available information. The approach requires the solution to linear programs only. The derived models are particularly suited to robust model predictive control design, since they can predict the future trajectory of the system on a finite horizon and the related uncertainty intervals.

The following result shows that, under the considered working assumptions, the estimate converges to the optimal one, ${\overline{\epsilon}}_{p}^{0}$.

Derive a procedure to estimate the optimal error bound.

### Proof 3.2

Let us consider a single-input, single-output (SISO), open-loop stable, discrete-time, strictly proper linear time invariant (LTI) system with $n$ states, input ${u{(k)}} \in {\mathbb{R}}$ and output ${z{(k)}} \in {\mathbb{R}}$, where $k \in {\mathbb{Z}}$ is the discrete time variable. The measurement of the system output $y{(k)}$ is affected by a bounded additive disturbance $d{(k)}$:

### Assumption 1

The input $u{(k)}$ is measured with negligible noise. $\square$

### Assumption 2

Let us denote with $p \in {\mathbb{N}}$ a finite number of time steps in the future. We are interested in deriving a prediction model of the future output $z{({k + p})}$, exploiting the input and output measurements collected in the time interval $\lbrack{{k - o} + 1},k\rbrack$, where $o \in {\mathbb{N}}$ is the chosen order of the model, and the future (planned) inputs in the interval $\lbrack k,{{k + p} - 1}\rbrack$. Specifically, at any instant $k$ let us define the regressor ${\varphi_{p}{(k)}} \in {\mathbb{R}}^{{{2o} - 1} + p}$ as:

where ^T^ is the matrix transpose operation and

Then, we consider the following linear model structure:

where $\hat{z}{({k + p})}$ is the predicted output and $\theta_{p} \in {\mathbb{R}}^{{{2o} - 1} + p}$ is the model parameter vector....
