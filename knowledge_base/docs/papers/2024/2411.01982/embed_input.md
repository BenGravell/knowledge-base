Learning Controlled Stochastic Differential Equations

Identification of nonlinear dynamical systems is crucial across various fields, facilitating tasks such as control, prediction, optimization, and fault detection. Many applications require methods capable of handling complex systems while providing strong learning guarantees for safe and reliable performance. However, existing approaches often focus on simplified scenarios, such as deterministic models, known diffusion, discrete systems, one-dimensional dynamics, or systems constrained by strong structural assumptions such as linearity. This work proposes a novel method for estimating both drift and diffusion coefficients of continuous, multidimensional, nonlinear controlled stochastic differential equations with non-uniform diffusion. We assume regularity of the coefficients within a Sobolev space, allowing for broad applicability to various dynamical systems in robotics, finance, climate modeling, and biology. Leveraging the Fokker-Planck equation, we split the estimation into two tasks: (a) estimating system dynamics for a finite set of controls, and (b) estimating coefficients that govern those dynamics....

## Introduction

Modeling complex dynamical systems is pivotal across various fields, enabling tasks such as analysis, prediction, simulation, control, optimization, and fault detection. Deriving models from first principles---such as physical, electrical, mechanical, chemical, biological, or economic laws---requires extensive knowledge, which is often lacking in practice. In response, the literature has seen the emergence of data-driven modeling approaches since at least the 1970s, utilizing input-output data sets to identify the most suitable model within a hypothesis set of possible models \[\].

Stochastic differential equations (SDEs) are a general mathematical tool for modeling dynamical systems subject to random fluctuations. Let $X{(t)}$ be a controlled $n$-dimensional stochastic process whose dynamics are governed by the controlled SDE

### Step 2: Fokker-Planck matching

Same algorithm but adding additional dimensions for the controls. More precisely, closed-form are updated with $z = {(t,x,v)} \in {{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n} \times {\mathbb{R}}^{d}}$ instead of $z = {(t,x)} \in {{\lbrack 0,T\rbrack} \times {\mathbb{R}}^{n}}$. We store

Under Assumptions (A1) (Smooth SDE). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations") and (A3) (Calibrated sampling). ‣ 3.1 Fokker-Planck matching inequality ‣ 3 Proposed method ‣ Learning Controlled Stochastic Differential Equations"), there exists a constant $c > 0$ such that for any ${(\hat{b},{\hat{\sigma}}^{2})} \in \mathcal{F}$,

### Python open-source library

### Proof

We consider the problem of estimating a controlled SDE from a data set of sample paths generated under various controls from $\mathcal{H}$. Namely, our goal is to estimate $(b,\sigma^{2})$ from a data set

where $X_{u_{k}}$ denotes the solution of Eq. under the control $u_{k}:{{\lbrack 0,T\rbrack}\mapsto{\mathbb{R}}^{d}}$. By treating controls as inputs and sample paths as outputs, we frame system identification as a supervised learning problem.

While controlled SDEs cover a wide range of scenarios, estimating them poses significant statistical and computational challenges. Consequently, the existing literature on dynamical systems (see Section 1.1) imposes various limitations to develop practical methods....
