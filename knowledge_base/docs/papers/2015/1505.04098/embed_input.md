Asymptotically Optimal Planning by Feasible Kinodynamic Planning in State-Cost Space

Topics include Kinodynamic planning, Asymptotic optimality, Meta algorithm.

AO-x meta-algorithm turns any feasible kinodynamic planner into an asymptotically optimal planner by lifting planning into a state-cost space.

This paper presents an equivalence between feasible kinodynamic planning and optimal kinodynamic planning, in that any optimal planning problem can be transformed into a series of feasible planning problems in a state-cost space, whose solutions approach the optimum. This transformation yields a meta-algorithm that produces an asymptotically optimal planner, given any feasible kinodynamic planner as a subroutine. The meta-algorithm is proven to be asymptotically optimal and a formula is derived relating expected running time and solution suboptimality. It is directly applicable to a wide range of optimal planning problems because it does not resort to the use of steering functions or numerical boundary-value problem solvers. On a set of benchmark problems, it is demonstrated to perform, using the expansive space tree (EST) and rapidly-exploring random tree (RRT) algorithms as subroutines, at a level that is superior or comparable to related planners.

## Introduction

Optimal motion planning is a highly active research topic in robotics, due to the pervasive need to compute paths that simultaneously avoid complex obstacles, satisfy dynamic constraints, and are high quality according to some cost function. Recent advances in sampling-based optimal motion planning build on decades of work in the topic of feasible motion planning, in which costs are ignored. However, the field is still some ways away from general-purpose optimal planning algorithms that accept arbitrary black-box constraints and costs as input....

This paper presents a new state-cost space formulation that transforms optimal motion planning problems into feasible kinodynamic (both kinematically- and differentially-constrained) motion planning problems. Using this formulation, we introduce a meta-algorithm, AO-$x$, to adapt any feasible kinodynamic planner $x$ into an asymptotically-optimal motion planner, provided that $x$ satisfies some relatively unrestrictive conditions, e.g., expected running time is finite....

This paper presents an equivalence between optimal motion planning problems (either kinodynamic or kinematic) and feasible kinodynamic motion planning problems using a state-cost space transformation. Despite the simplicity of the transformation, it is a powerful tool; we use it to develop an easily implemented, asymptotically-optimal, sampling-based meta-planner that accepts a sampling-based kinodynamic feasible planner as input. It purely uses control-based sampling, making it suitable for problems with general differential constraints and cost functions that do not admit a steering function....

We hope this new formulation will provide inspiration and theoretical justification for new approaches to optimal motion planning. As an example, an obvious way to improve convergence rate would be to run local optimizations on each trajectory found by the underlying planner; this method has been shown to work well for kinematic optimal path planning. We also obtained curious results regarding state-space vs cost-space weighting in the RRT distance metric. Following up on this work may also open up avenues of research in sampling strategies for state-cost space planning, e.g., in appropriate biasing strategies.

A more refined analysis gives a tighter bound

### Theorem 2
