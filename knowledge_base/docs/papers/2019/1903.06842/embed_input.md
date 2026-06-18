Formulas for Data-Driven Control: Stabilization, Optimality, and Robustness

Topics include Data-driven control, Willems' fundamental lemma, Linear matrix inequalities, Stabilization, Linear quadratic regulation, Robust control, Output feedback, Nonlinear equilibria.

Turns the fundamental lemma into explicit LMI-based formulas for direct stabilization, LQR, output feedback, and noisy-data robustness. The paper is a core reference for direct data-driven control as a convex controller-synthesis problem rather than an identification-then-control pipeline.

In a paper by Willems and coauthors it was shown that persistently exciting data can be used to represent the input-output behavior of a linear system. Based on this fundamental result, we derive a parametrization of linear feedback systems that paves the way to solve important control problems using data-dependent Linear Matrix Inequalities only. The result is remarkable in that no explicit system's matrices identification is required. The examples of control problems we solve include the state and output feedback stabilization, and the linear quadratic regulation problem. We also discuss robustness to noise-corrupted measurements and show how the approach can be used to stabilize unstable equilibria of nonlinear systems.

## Introduction

Learning from data is essential to every area of science. It is the core of statistics and artificial intelligence, and is becoming ever more prevalent also in the engineering domain. Control engineering is one of the domains where learning from data is now considered as a prime issue.

Learning from data is actually not novel in control theory. System identification is one of the major developments of this paradigm, where modeling based on first principles is replaced by data-driven learning algorithms. Prediction error, maximum likelihood as well as subspace methods are all data-driven techniques which can be now regarded as standard for what concerns modeling. The learning-from-data paradigm has been widely pursued also for control design purposes. A main question is how to design control systems directly from process data with no intermediate system identification step....

Consider next the terms on the right hand side of and. By applying again with $\varepsilon = 0.5$, $X = X_{1,T}$, $F = I$ and $Y = {- W_{1,T}}$, we obtain

This gives the claim. $\blacksquare$

*(Feasibility of (V-A) under noise-free data)* In the noise-free case, that is when $Z_{0,T} = X_{0,T}$ and $Z_{1,T} = X_{1,T}$, the formulations and coincide. Suppose then that is feasible and let $\overline{Q}$ be a solution. Since positive definiteness is preserved under small perturbations, ${(Q,\alpha)} = {(\overline{Q},\overline{\beta})}$ will be a solution to the first of (V-A) for a sufficiently small $\overline{\beta} > 0$. Hence ${(Q,\alpha)} = {({\delta\overline{Q}},{\delta\overline{\beta}})}$ will remain feasible for the first of (V-A) for all $\delta > 0$....

### Remark 1

Assumptions 4 and 5 parallel the assumptions considered for the case of noisy data. In particular, Assumptions 5 is the counterpart of Assumption 2 (or Assumption 3) and it amounts to requiring that the experiment is carried out sufficiently close to the system equilibrium so that the effect of the nonlinearities (namely the disturbance $d$) becomes small enough compared with $\deltax$ (*cf.* ).

Contributions to data-driven control can be traced back to the pioneering work by Ziegler and Nichols, direct adaptive control and neural networks theories. Since then, many techniques have been developed under the heading *data-driven* and *model-free* control....
