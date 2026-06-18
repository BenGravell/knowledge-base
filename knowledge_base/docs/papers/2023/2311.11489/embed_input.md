Beyond Nonconvexity: A Universal Trust-Region Method with New Analyses

Topics include Convex optimization, Nonconvex optimization, Robustness, Optimization, Nonconvexity, TR, Stationary point.

The trust-region (TR) method is renowned historically for its robustness in nonconvex problems and extraordinary numerical performance, but the study of its performance in convex optimization is somehow limited. This paper complements the existing literature by presenting a universal trust-region method that simultaneously incorporates the quadratic regularization and ball constraint. In particular, we introduce a novel descent property tailored for trust-region-type algorithms, enabling us to unify and streamline the analysis for both convex and nonconvex optimization. Our method exhibits an iteration complexity of tilde O(epsilon^(-3/2)) to find an epsilon-approximate second-order stationary point for nonconvex optimization. Meanwhile, the analysis reveals that the universal method attains an O(1/sqrt(epsilon)) complexity bound for convex optimization. Finally, we develop an adaptive universal method to address practical implementations. The numerical results show the effectiveness of our method in both nonconvex and convex problems.

## Introduction

Second-order methods are renowned for their faster convergence compared to first-order methods, and the capability to find second-order stationary points, see Cartis et al. \[\], Nocedal and Wright \[\], Nesterov \[\], Carmon et al.. Among these methods, the trust-region (TR) method \[\] stands out as a representative approach due to its robustness in nonconvex problems and extraordinary numerical performance. Many linear or nonlinear programming solvers are using the trust-region method as an important building block, to name a few, Knitro \[\], IPOPT \[\], and PDFO \[\], etc....

Recall that the TR method operates on the local quadratic approximation of objective function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ within a TR ball constraint:

to fit the observed data under (5.2), where $D_{i,j}$ denotes the observed data recorded at time $i$ and day $j$. The dataset used for this study is sourced from Ausgrid \[\] that deals with the matrix size of $48 \times 30$, $r = 9$, all algorithms are terminated at $\left\| {{\nabla f}\left( x_{k} \right)} \right\| \leq 10^{- 7}$. We vary $\lambda \in \left\lbrack 10^{- 2},10^{- 3},10^{- 4} \right\rbrack$ to test the robustness under small regularizations. The results are presented in Table 4. While smaller $\lambda$ induces harder instances, iUTR has the best performance among competing algorithms in all instances....

Table 4: Performance of different algorithms on Matrix Completion. Here, we present the average iteration number, function, and gradient evaluations of five runs. We limit the run time to 1,000 seconds.

The above property is a safeguard for the iterates so that the gradient is bounded even in the case where $\lambda_{k} \neq 0$, cf. (2.8. ‣ 2.1 Overview of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.")). We can again establish the validness of such property by, for example, Strategy 2.1....

## The Universal Trust-Region Method with a Simple Strategy

Now we are ready to prove the local superlinear convergence of our algorithm.

Once the TR step $d_{k}$ is generated, the TR method decides whether to update or adjust the radius $\Delta_{k}$ based on the so-called ratio test:
