A Regularized Limited Memory BFGS Method for Large-Scale Unconstrained Optimization and Its Efficient Implementations

Topics include Robustness, Optimization, Limited memory BFGS, L-BFGS, Line search.

The limited memory BFGS (L-BFGS) method is one of the popular methods for solving large-scale unconstrained optimization. Since the standard L-BFGS method uses a line search to guarantee its global convergence, it sometimes requires a large number of function evaluations. To overcome the difficulty, we propose a new L-BFGS with a certain regularization technique. We show its global convergence under the usual assumptions. In order to make the method more robust and efficient, we also extend it with several techniques such as nonmonotone technique and simultaneous use of the Wolfe line search. Finally, we present some numerical results for test problems in CUTEst, which show that the proposed method is robust in terms of solving number of problems.

## Introduction

In

---l--- x∈R\^nf(x), where $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is a smooth function. For solving it, we focus on the quasi-Newton type method as

The standard solution methods to solve such as the steepest descent method, Newton's method and the BFGS method are not suitable for large-scale problems. This is because the steepest descent method generally converges slowly, while Newton's method needs to compute the Hessian matrix and solve linear equations at each iteration. Moreover, the BFGS method requires $O{(n^{2})}$ memory to store and calculate the approximate Hessian of $f$, which causes some difficulty for large-scale problem.

One of the popular quasi-Newton methods for solving large-scale problem is the limited memory BFGS(L-BFGS), which uses small memory to store an approximate Hessian of $f$. The L-BFGS method stores the last $m$ vector pairs of ${(s_{k - i},y_{k - i})},$ ${i = {0,1,\ldots,{m - 1}}},$ to compute a search direction $d_{k}$, where

The usual L-BFGS adopts the Wolfe line search to guarantee its global convergence. The line search sometimes needs a large number of function evaluations. Thus, it is preferable to reduce the number of function evaluations as much as possible.

The trust region method (TR-method) can guarantee the global convergence. It is known that the TR-method needs fewer function evaluations than the line search. The L-BFGS method combined with the TR-method produces good performance for many benchmark problems in terms of the number of function evaluations. However, the TR-method must solve the constrained subproblem

## Conclusion

In this paper we have proposed a combination of the L-BFGS and the regularization technique. We showed the global convergence under appropriate assumptions. We have also presented some efficient implementations. In numerical results, the overall comparison shows that the proposed method can solve more problems than the original L-BFGS. This result indicates that the proposed method is robust in terms of solving number of problems.

For future work, we may consider proposing the stochastic version of the proposed method to solve empirical risk minimization problems.
