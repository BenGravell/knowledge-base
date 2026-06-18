Pinet: Optimizing Hard-constrained Neural Networks with Orthogonal Projection Layers

Topics include Motion planning, Vehicles, Robustness, Neural networks, Accuracy, Optimization, Planning, Learning, PInet, Optimization problem.

We introduce an output layer for neural networks that ensures satisfaction of convex constraints. Our approach, Pinet, leverages operator splitting for rapid and reliable projections in the forward pass, and the implicit function theorem for backpropagation. We deploy Pinet as a feasible-by-design optimization proxy for parametric constrained optimization problems and obtain modest-accuracy solutions faster than traditional solvers when solving a single problem, and significantly faster for a batch of problems. We surpass state-of-the-art learning approaches by orders of magnitude in terms of training time, solution quality, and robustness to hyperparameter tuning, while maintaining similar inference times. Finally, we tackle multi-vehicle motion planning with non-convex trajectory preferences and provide Pinet as a GPU-ready package implemented in JAX.

## Introduction

In

where $y \in {\mathbb{R}}^{d}$ is the decision variable, $x \in {\mathbb{R}}^{p}$ is the context (or parameter) of the problem instance, $\varphi:{{{\mathbb{R}}^{d} \times {\mathbb{R}}^{p}}\rightarrow{\mathbb{R}}}$ is the objective function, and ${\mathcal{C}{(x)}} \subseteq {\mathbb{R}}^{d}$ is a non-empty, closed, convex set for all $x$. We provide a pedagogical example to explain this formulation in Appendix˜A.

Constrained optimization has universal applicability, from safety-critical applications such as the optimal power flow in electrical grids nellikkath2022physics, to logistics and scheduling bengio2021machine, and even biology, where enforcing priors on the solution can enhance its interpretability balcerak2025energy; terpin2024learning.

Rather than solving each problem instance from scratch, the mapping from contexts to solutions can be learned with NNs.

## Limitations

The main limitation of our work is the requirement of convex constraint sets. Despite the numerous applications involving only convex constraints boyd2004convex, and the numerous applications that can be losslessly convexified malyuta2022convex, we acknowledge that future work should investigate how to relax this structural assumption. One potential approach could involve sequential convexification of non-convex constraints, similar to the algorithm in lastrucci2025enforce that addresses non-linear equality constraints.
