Scalable Semidefinite Programming

Semidefinite programming (SDP) is a powerful framework from convex optimization that has striking potential for data science applications. This paper develops a provably correct randomized algorithm for solving large, weakly constrained SDP problems by economizing on the storage and arithmetic costs. Numerical evidence shows that the method is effective for a range of applications, including relaxations of MaxCut, abstract phase retrieval, and quadratic assignment. Running on a laptop equivalent, the algorithm can handle SDP instances where the matrix variable has over 10^ entries.

## Abstract

Semidefinite programming (SDP) is a powerful framework from convex optimization that has striking potential for data science applications. This paper develops a provably correct randomized algorithm for solving large, weakly constrained SDP problems by economizing on the storage and arithmetic costs. Numerical evidence shows that the method is effective for a range of applications, including relaxations of MaxCut, abstract phase retrieval, and quadratic assignment. Running on a laptop equivalent, the algorithm can handle SDP instances where the matrix variable has over $10^{14}$ entries.

### keywords

We have presented a practical, new approach for solving SDPs at scale. Our algorithm, SketchyCGAL, combines a primal--dual optimization method with randomized linear algebra techniques to achieve unprecedented guarantees when the problem is weakly constrained and the solution is approximately low rank. We hope that our ideas lead to further algorithmic advances and support new applications of semidefinite programming.

SketchyCGAL is currently limited by the arithmetic cost of solving large eigenvalue problems to increasing accuracy. It also falters for SDPs with a large number of constraints because it depends on a primal--dual approach. Moreover, our analysis does not fully explain the observed behavior of the algorithm, including the rate of convergence of the primal variable or the convergence of the dual variable and the surrogate duality gap. These topics merit further research.

where ^†^ is the pseudoinverse. This reconstruction is called a *Nyström approximation*. We often truncate $\hat{\mathbf{X}}$ by replacing it with its best rank-$r$ approximation ${⟦\hat{\mathbf{X}}⟧}_{r}$ for some $r \leq R$.

### The CGAL iteration

## Numerical examples

Augmented Lagrangian, conditional gradient method, convex optimization, dimension reduction, first-order method, randomized linear algebra, semidefinite programming, sketching.

## Motivation

For a spectrum of challenges in data science, methodologies based on semidefinite programming offer remarkable performance both in theory and for small problem instances. Even so, practitioners often critique this approach by asserting that it is impossible to solve semidefinite programs (SDPs) at the scale demanded by real-world applications....
