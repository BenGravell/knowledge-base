Low-Complexity Learning of Linear Quadratic Regulators from Noisy Data

Topics include Data-driven control, Linear quadratic regulator, Noisy data, Semidefinite programming, Direct linear quadratic regulator, Robust control, Reinforcement learning, Sample complexity.

Designs LQR controllers directly from noisy trajectory data with finite-sample, relative-error guarantees and an SDP implementation. It is a concise data-driven LQR counterpart to the noiseless LMI formulas, emphasizing robustness without a probabilistic noise model.

This paper considers the Linear Quadratic Regulator problem for linear systems with unknown dynamics, a central problem in data-driven control and reinforcement learning. We propose a method that uses data to directly return a controller without estimating a model of the system. Sufficient conditions are given under which this method returns a stabilizing controller with guaranteed relative error when the data used to design the controller are affected by noise. This method has low complexity as it only requires a finite number of samples of the system response to a sufficiently exciting input, and can be efficiently implemented as a semi-definite program. Further, the method does not require assumptions on the noise statistics, and the relative error nicely scales with the noise magnitude.

## Introduction

Control theory is witnessing an increasing renewed interest towards *data-driven* (*data-based*) control. This terminology refers to all those cases where the dynamics of the system are unknown and the control law must be designed using data alone. This can be done either by identifying a model of the system from data and then use the model for control design, or by directly designing the control law bypassing the system identification (ID) step....

*The Linear Quadratic Regulator problem*

## Concluding remarks

The design of (optimal) controllers from noisy data is a very challenging and largely unsolved problem. In this paper we took some steps in this direction for the LQR problem. By resorting to a convex SDP formulation of the LQR problem, we proposed two novel methods that explicitly account for noise through an augmented cost function which favours noise-robust solutions. Both method provides finite sample stability guarantees, and do not require specific noise models such as the noise being white.\
A great leap forward would come from extending the ideas of this paper to incorporate state and input *safety* constraints....

Suppose that is feasible. Let $(\overline{\gamma},\overline{Q},\overline{P},\overline{L},\overline{V})$ be any optimal solution and let $\overline{K} = U_{0}\overline{Q}\overline{P}^{- 1}$. Let $\eta_{1} \geq 1$ be a constant. If condition is satisfied then $\overline{K}$ stabilises system and

### Stability and performance analysis

*Proof*. Similarly to the proof of Lemma 4, the idea is to let ${(\hat{\gamma},\hat{Q},\hat{P},\hat{L})}:={\eta_{1}{(\overline{\gamma},\overline{Q},\overline{P},\overline{L})}}$ and show that it satisfies the first constraint in. In fact, by multiplying the first constraint in by the vector $x^{\top}\left\lbrack {ID_{0}} \right\rbrack$ on the left and its transpose on the right, it is straightforward to see that implies

This paper considers the *infinite horizon* Linear Quadratic Regulator (LQR) problem for linear time-invariant systems, which is one of the problems more studied in the control literature. Besides its practical relevance, this problem is a prime example of the challenges encountered in data-driven control....
