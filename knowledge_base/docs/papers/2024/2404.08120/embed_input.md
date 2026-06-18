A Least-square Method for Non-asymptotic Identification in Linear Switching Control

The focus of this paper is on linear system identification in the setting where it is known that the underlying partially-observed linear dynamical system lies within a finite collection of known candidate models. We first consider the problem of identification from a given trajectory, which in this setting reduces to identifying the index of the true model with high probability. We characterize the finite-time sample complexity of this problem by leveraging recent advances in the non-asymptotic analysis of linear least-square methods in the literature. In comparison to the earlier results that assume no prior knowledge of the system, our approach takes advantage of the smaller hypothesis class and leads to the design of a learner with a dimension-free sample complexity bound. Next, we consider the switching control of linear systems, where there is a candidate controller for each of the candidate models and data is collected through interaction of the system with a collection of potentially destabilizing controllers. We develop a dimension-dependent criterion that can detect those destabilizing controllers in finite time.

## Introduction

System identification --- the problem of estimating the parameters of an unknown dynamical system from a single trajectory of input/output data --- plays an important role in many problem domains such as control theory, robotics, and reinforcement learning. There has been tremendous progress in analyzing the performance of various system identification schemes --- classical results showed asymptotic convergence, whereas recent advances in non-asymptotic theory quantified the sample complexity of learning accurate estimates from data.

In this paper, we consider a collection of discrete-time, partially-observed linear systems ${\{{(C_{i},A_{i},B_{i})}\}}_{i = 1}^{N}$ containing the unknown true system parameters $(C_{\star},A_{\star},B_{\star})$.

where the dimensions are ${x_{t} \in {\mathbb{R}}^{d_{x}}},{u_{t} \in {\mathbb{R}}^{d_{u}}}$ and $y_{t} \in {\mathbb{R}}^{d_{y}}$. We assume that the initial state $x_{1} \sim {\mathcal{N}{(0,I_{d_{x} \times d_{x}})}}$, process noise $w_{t} \sim {\mathcal{N}{(0,{\sigma_{w}^{2}I_{d_{x} \times d_{x}}})}}$, and observation noise $\eta_{t} \sim {\mathcal{N}{(0,{\sigma_{\eta}^{2}I_{d_{y} \times d_{y}}})}}$ come from Gaussian distributions.

## Conclusion

In this paper, we study the problem of non-asymptotic system identification in the context of linear switching control. We derive a data-driven approach by leveraging ideas from both non-asymptotic system identification and switching control.

We reject any controller that is destabilizing the underlying open-loop dynamics by comparing the observations with our explicit bound on the input-to-output gain of stable systems

These ingredients lead to a non-asymptotic guarantee on the sample complexity for learning the unknown system parameters. From our main results, we reveal new implications on the classical estimator-based supervisory control, particularly regarding to a more precise characterization of the notion of dwell times and the effects of transient behaviors from switching.
