Informed RRT*: Optimal Sampling-based Path Planning Focused via Direct Sampling of an Admissible Ellipsoidal Heuristic

Topics include Motion planning, Sampling-based planning, Asymptotic optimality, Informed rapidly-exploring random tree star, Rapidly-exploring random tree star, Heuristic search, Informed set.

Informed RRT* accelerates convergence of RRT* by restricting sampling to the prolate hyperspheroid (ellipsoidal) subset of the state space that can possibly improve the current best solution, rather than sampling the entire domain. This focused sampling preserves RRT*'s probabilistic completeness and asymptotic optimality guarantees while significantly improving convergence rate and final solution quality, especially in high-dimensional spaces or large environments. However, the ellipsoidal region is only valid for path planning where the cost is the Euclidean path length; for other costs or kindodynamic planning the informed set has some other geometry that is not generally known to be computable in closed form.

Rapidly-exploring random trees (RRTs) are popular in motion planning because they find solutions efficiently to single-query problems. Optimal RRTs (RRT*s) extend RRTs to the problem of finding the optimal solution, but in doing so asymptotically find the optimal path from the initial state to every state in the planning domain. This behaviour is not only inefficient but also inconsistent with their single-query nature. For problems seeking to minimize path length, the subset of states that can improve a solution can be described by a prolate hyperspheroid. We show that unless this subset is sampled directly, the probability of improving a solution becomes arbitrarily small in large worlds or high state dimensions. In this paper, we present an exact method to focus the search by directly sampling this subset. The advantages of the presented sampling technique are demonstrated with a new algorithm, Informed RRT*. This method retains the same probabilistic guarantees on completeness and optimality as RRT* while improving the convergence rate and final solution quality....

## Introduction

The motion-planning problem is commonly solved by first discretizing the continuous state space with either a grid for graph-based searches or through random sampling for stochastic incremental searches. Graph-based searches, such as A\*, are often *resolution complete* and *resolution optimal*. They are guaranteed to find the optimal solution, if a solution exists, and return failure otherwise (up to the resolution of the discretization). These graph-based algorithms do not scale well with problem size (e.g., state dimension or problem range).

Stochastic searches, such as RRTs, PRMs, and Expansive Space Trees, use sampling-based methods to avoid requiring a discretization of the state space. This allows them to scale more effectively with problem size and to directly consider kinodynamic constraints; however, the result is a less-strict completeness guarantee. RRTs are *probabilistically complete*, guaranteeing that the probability of finding a solution, if one exists, approaches unity as the number of iterations approaches infinity.

Informed RRT\* uses heuristics to shrink the planning problem to subsets of the original domain. This makes it inherently dependent on the current solution cost, as it cannot focus the search when the associated prolate hyperspheroid is larger than the planning problem itself. Similarly, it can only shrink the subset down to the lower bound defined by the optimal solution. We are currently investigating techniques to focus the search without requiring an initial solution. These techniques, such as Batch Informed Trees (BIT\*), incrementally *increase* the search subset. By doing so, they prioritize the initial search of low-cost solutions.

An open motion planning library (OMPL) implementation of Informed RRT\* is described at

with $\zeta_{n}$ being the volume of a unit $n$-ball.

### II-B2 Heuristic-based Sample Rejection

The rotation from the hyperellipsoid frame to the world frame, $\mathbf{C} \in {SO(n)}$, can be solved directly as a general Wahba problem. It has been shown that a valid solution can be found even when the problem is underspecified. The rotation matrix is given by

Until recently, these sampling-based algorithms made no claims about the optimality of the solution. Urmson and Simmons had found that using a heuristic to bias sampling improved RRT solutions, but did not formally...
