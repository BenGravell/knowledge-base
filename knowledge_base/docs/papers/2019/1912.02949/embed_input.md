Scalable Semidefinite Programming

Semidefinite programming (SDP) is a powerful framework from convex optimization that has striking potential for data science applications. This paper develops a provably correct randomized algorithm for solving large, weakly constrained SDP problems by economizing on the storage and arithmetic costs. Numerical evidence shows that the method is effective for a range of applications, including relaxations of MaxCut, abstract phase retrieval, and quadratic assignment. Running on a laptop equivalent, the algorithm can handle SDP instances where the matrix variable has over 10^ entries.

## Abstract

Semidefinite programming (SDP) is a powerful framework from convex optimization that has striking potential for data science applications. This paper develops a provably correct randomized algorithm for solving large, weakly constrained SDP problems by economizing on the storage and arithmetic costs. Numerical evidence shows that the method is effective for a range of applications, including relaxations of MaxCut, abstract phase retrieval, and quadratic assignment. Running on a laptop equivalent, the algorithm can handle SDP instances where the matrix variable has over $10^{14}$ entries.

## keywords

Augmented Lagrangian, conditional gradient method, convex optimization, dimension reduction, first-order method, randomized linear algebra, semidefinite programming, sketching.

## Abstract form of the model problem

Let us instate compact notation for the linear constraints in the model problem Eq. 1.5 under the European Union’s Horizon 2020 research and innovation program under the grant agreement number 725594 (time-data) and the Swiss National Science Foundation (SNSF) under the grant number 200021_178865/1. JAT gratefully acknowledges ONR Awards N00014-11-1-0025, N00014-17-1-2146, and N00014-18-1-2363. MU gratefully acknowledges DARPA Award FA8750-17-2-0101. Part of this research is conducted while AY is at Massachusetts Institute of Technology, Cambridge, MA, USA.

## Conclusion

We have presented a practical, new approach for solving SDPs at scale. Our algorithm, SketchyCGAL, combines a primal--dual optimization method with randomized linear algebra techniques to achieve unprecedented guarantees when the problem is weakly constrained and the solution is approximately low rank. We hope that our ideas lead to further algorithmic advances and support new applications of semidefinite programming.

SketchyCGAL is currently limited by the arithmetic cost of solving large eigenvalue problems to increasing accuracy. It also falters for SDPs with a large number of constraints because it depends on a primal--dual approach. Moreover, our analysis does not fully explain the observed behavior of the algorithm, including the rate of convergence of the primal variable or the convergence of the dual variable and the surrogate duality gap. These topics merit further research.
