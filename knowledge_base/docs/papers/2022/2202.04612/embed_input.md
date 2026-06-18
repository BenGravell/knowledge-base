Zeroth-Order Randomized Subspace Newton Methods

Topics include ZO-RSN.

Zeroth-order methods have become important tools for solving problems where we have access only to function evaluations. However, the zeroth-order methods only using gradient approximations are n times slower than classical first-order methods for solving n-dimensional problems. To accelerate the convergence rate, this paper proposes the zeroth order randomized subspace Newton (ZO-RSN) method, which estimates projections of the gradient and Hessian by random sketching and finite differences. This allows us to compute the Newton step in a lower dimensional subspace, with small computational costs. We prove that ZO-RSN can attain lower iteration complexity than existing zeroth order methods for strongly convex problems. Our numerical experiments show that ZO-RSN can perform black-box attacks under a more restrictive limit on the number of function queries than the state-of-the-art Hessian-aware zeroth-order method.

## Introduction

Several applications in machine learning, signal processing and communication networks can often be cast into optimization problems, where gradients are difficult or even infeasible to compute. Popular application examples include optimal hyper-parameter tuning for learning models, black-box adversarial attacks on neural network models and sensor selection problems in smart grids or wireless networks. This motivates the study of the zeroth-order methods. A prominent type of zeroth order methods uses function value differences to estimate the gradients \[10, Section 3.4\]....

Ye *et al.* developed the Hessian-aware zeroth order (ZOHA) methods, which integrate Hessian information into zeroth-order methods. The power-iteration based method ZOHA-PW has a lower query complexity than the gradient-estimating method by when the eigenvalues of the Hessian decay sufficiently quickly. However, the power iteration method requires $O{(n)}$ function queries per iteration for $n$-dimensional problems, which is expensive when $n$ is large. To decrease the query cost, they proposed the heuristic methods ZOHA-Gauss-DC and ZOHA-Diag-DC, which estimate the Hessian based on a limited number of random directions....

## Conclusions

We have proposed the ZO-RSN method, a Hessian-based zeroth-order method that approximates sketched gradients and Hessians by finite differences. Our results display a lower iteration complexity of the ZO-RSN method than existing zeroth-order methods for strongly convex problems. The experiments with un-targeted adversarial attacks on a CNN model illustrate that the modified ZO-RSN method named ZO-RSN-SQP attains an overall competitive performance and a higher stability, compared to ZOHA-Gauss-DC.

## Theoretical results

Consider the RSN method for solving Problem. If $\gamma \leq {1/\hat{L}}$, then

Now, we compare the complexity bounds for the ZO-RSN methods against the Hessian-aware zeroth-order method using the power iteration (ZOHA-PW), which previously has been compared favourably to the zeroth-order method in. Since the ZOHA-PW method also generates multiple random directions, here $m$ refers to the number of the generated directions. For $\mu$-strongly convex problems, the iteration complexity of ZOHA-PW is
