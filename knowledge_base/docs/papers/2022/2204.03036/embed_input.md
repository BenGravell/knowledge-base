First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems

In this paper, we derive first-order Pontryagin optimality conditions for risk-averse stochastic optimal control problems subject to final time inequality constraints, and whose costs are general, possibly non-smooth finite coherent risk measures. Unlike preexisting contributions covering this situation, our analysis holds for classical stochastic differential equations driven by standard Brownian motions. In addition, it presents the advantages of neither involving second-order adjoint equations, nor leading to the so-called weak version of the PMP, in which the maximization condition with respect to the control variable is replaced by the stationarity of the Hamiltonian.

## Introduction

In the last decades, risk-averse stochastic optimal control has seen a surge of interest as a tool for designing control laws that enjoy robustness properties against uncertainties. Relevant applications of this theory encompass broad research fields, ranging from risk-averse financial investments to the safe control of autonomous systems, as evidenced e.g. by the recent monographs and their bibliography....

To the best of our knowledge, the derivation of a risk-averse PMP was attempted firstly in, where appropriate adjoint equations and maximality conditions formulated in terms of the so-called $G$-Stochastic calculus are introduced in order to cope with the presence of risk measures. This framework was originally introduced by Peng, and developed by the stochastic control community later on, see e.g.....

In this paper, we developed a new method for proving a first-order version of the Pontryagin Maximum Principle for non-smooth risk-averse optimal control problems, based on set-valued linearisations. The main incentive to do so was to produce optimality conditions that could encompass typical risk functions such as the AV@R, which is merely directionally differentiable. In the future, we aim at furthering these investigations in three main directions.

Firstly, we want to see whether it is feasible to weaken or remove the convexity assumptions on the dynamics. Owing to the lack of relaxation property for sollutions of (SDI) illustrated in Remark 2.15. ‣ 2.4 Stochastic Differential Inclusions ‣ 2 Preliminaries ‣ First-Order Pontryagin Maximum Principle for Risk-Averse Stochastic Optimal Control Problems"), this will most likely call for innovative proof strategies. Secondly, we want to leverage the optimality conditions proposed here to design efficient numerical methods for solving risk-averse optimal control problems, such as indirect risk-averse shooting methods....

has nonempty compact and convex images, and thus admits progressive selections

In the sequel given an integrably bounded and progressively measurable-Lipschitz set-valued mapping $F:{{{\lbrack 0,T\rbrack} \times \Omega \times {\mathbb{R}}^{n}}\rightrightarrows{\mathbb{R}}^{n}}$ along with a diffusion map $\sigma:{{{\lbrack 0,T\rbrack} \times \Omega \times {\mathbb{R}}^{n}}\rightarrow{\mathbb{R}}^{n}}$ satisfying the relevant parts of Assumptions (MSD)....
