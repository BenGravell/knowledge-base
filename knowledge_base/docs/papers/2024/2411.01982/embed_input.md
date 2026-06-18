Learning Controlled Stochastic Differential Equations

Identification of nonlinear dynamical systems is crucial across various fields, facilitating tasks such as control, prediction, optimization, and fault detection. Many applications require methods capable of handling complex systems while providing strong learning guarantees for safe and reliable performance. However, existing approaches often focus on simplified scenarios, such as deterministic models, known diffusion, discrete systems, one-dimensional dynamics, or systems constrained by strong structural assumptions such as linearity. This work proposes a novel method for estimating both drift and diffusion coefficients of continuous, multidimensional, nonlinear controlled stochastic differential equations with non-uniform diffusion. We assume regularity of the coefficients within a Sobolev space, allowing for broad applicability to various dynamical systems in robotics, finance, climate modeling, and biology. Leveraging the Fokker-Planck equation, we split the estimation into two tasks: (a) estimating system dynamics for a finite set of controls, and (b) estimating coefficients that govern those dynamics.

## Introduction

Modeling complex dynamical systems is pivotal across various fields, enabling tasks such as analysis, prediction, simulation, control, optimization, and fault detection. Deriving models from first principles---such as physical, electrical, mechanical, chemical, biological, or economic laws---requires extensive knowledge, which is often lacking in practice. In response, the literature has seen the emergence of data-driven modeling approaches since at least the 1970s, utilizing input-output data sets to identify the most suitable model within a hypothesis set of possible models.

Stochastic differential equations (SDEs) are a general mathematical tool for modeling dynamical systems subject to random fluctuations. Let $X{(t)}$ be a controlled $n$-dimensional stochastic process whose dynamics are governed by the controlled SDE

We consider the problem of estimating a controlled SDE from a data set of sample paths generated under various controls from $\mathcal{H}$. Namely, our goal is to estimate $(b,\sigma^{2})$ from a data set

where $X_{u_{k}}$ denotes the solution of Eq. under the control $u_{k}:{{\lbrack 0,T\rbrack}\mapsto{\mathbb{R}}^{d}}$. By treating controls as inputs and sample paths as outputs, we frame system identification as a supervised learning problem.

## Conclusion

In this work, we address the problem of estimating continuous, multidimensional nonlinear controlled SDEs with non-uniform diffusion---a previously unaddressed challenge. We demonstrate how dynamical system identification can be approached through (a) density estimation of the dynamics for a finite set of controls, followed by (b) least-squares regression to estimate governing coefficients, using the Fokker-Planck matching inequality. This formulation enables us to derive strong theoretical guarantees by leveraging the rich and well-established literature on nonparametric least-squares regression.

Combining all bounds, we conclude that there exist constants ${c_{1},c_{2}} > 0$ that do not depend on $N,K,\delta$, such that, for any $\delta \in {(0,1\rbrack}$, with probability at least $1 - \delta$
