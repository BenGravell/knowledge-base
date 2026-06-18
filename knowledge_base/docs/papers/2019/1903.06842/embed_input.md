Formulas for Data-Driven Control: Stabilization, Optimality, and Robustness

Topics include Data-driven control, Willems' fundamental lemma, Linear matrix inequalities, Stabilization, Linear quadratic regulation, Robust control, Output feedback, Nonlinear equilibria.

Turns the fundamental lemma into explicit LMI-based formulas for direct stabilization, LQR, output feedback, and noisy-data robustness. The paper is a core reference for direct data-driven control as a convex controller-synthesis problem rather than an identification-then-control pipeline.

In a paper by Willems and coauthors it was shown that persistently exciting data can be used to represent the input-output behavior of a linear system. Based on this fundamental result, we derive a parametrization of linear feedback systems that paves the way to solve important control problems using data-dependent Linear Matrix Inequalities only. The result is remarkable in that no explicit system's matrices identification is required. The examples of control problems we solve include the state and output feedback stabilization, and the linear quadratic regulation problem. We also discuss robustness to noise-corrupted measurements and show how the approach can be used to stabilize unstable equilibria of nonlinear systems.

## Introduction

Learning from data is essential to every area of science. It is the core of statistics and artificial intelligence, and is becoming ever more prevalent also in the engineering domain. Control engineering is one of the domains where learning from data is now considered as a prime issue.

*Willems *et al.*'s fundamental lemma and paper contribution*

In this paper, we first revisit Willems *et al.*'s fundamental lemma, originally cast in the behavioral framework, through classic state-space descriptions (Lemma 2). Next, we show that this result can be used to get a data-dependent representation of the open-loop and closed-loop dynamics under a feedback interconnection. The first result (Theorem 1) indicates that the parametrization that emerges from the fundamental lemma is in fact the solution to a classic least-squares problem, and has clear connections with the so-called Dynamic Mode Decomposition.

## Discussion and conclusions

Persistently exciting data enable the construction of data-dependent matrices that can replace systems models. Adopting this paradigm proposed by we have shown the existence of a parametrization of feedback control systems that allows us to reduce the stabilization problem to an equivalent data-dependent linear matrix inequality. Since LMIs are ubiquitous in systems and control we expect that our approach could lead to data-driven solutions to many other control problems. As an example we have considered an LQR problem.

Studying how our approach can be used to systematically address control problems via data-dependent LMIs could be very rewarding, and lead to a methodical inclusion of data to analyze and design control systems. A great leap forward will come from systematically extending the methods of this paper to systems where identification is challenging, such as switched and nonlinear systems. The results of this paper show that our approach is concretely promising for nonlinear systems, but we have only touched the surface of this research area.
