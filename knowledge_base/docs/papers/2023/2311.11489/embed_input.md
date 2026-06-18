Beyond Nonconvexity: A Universal Trust-Region Method with New Analyses

Topics include Convex optimization, Nonconvex optimization, Robustness, Optimization, Nonconvexity, TR, Stationary point.

The trust-region (TR) method is renowned historically for its robustness in nonconvex problems and extraordinary numerical performance, but the study of its performance in convex optimization is somehow limited. This paper complements the existing literature by presenting a universal trust-region method that simultaneously incorporates the quadratic regularization and ball constraint. In particular, we introduce a novel descent property tailored for trust-region-type algorithms, enabling us to unify and streamline the analysis for both convex and nonconvex optimization. Our method exhibits an iteration complexity of tilde O(epsilon^(-3/2)) to find an epsilon-approximate second-order stationary point for nonconvex optimization. Meanwhile, the analysis reveals that the universal method attains an O(1/sqrt(epsilon)) complexity bound for convex optimization. Finally, we develop an adaptive universal method to address practical implementations. The numerical results show the effectiveness of our method in both nonconvex and convex problems.

## Introduction

Second-order methods are renowned for their faster convergence compared to first-order methods, and the capability to find second-order stationary points, see Cartis et al., Nocedal and Wright, Nesterov, Carmon et al.. Among these methods, the trust-region (TR) method stands out as a representative approach due to its robustness in nonconvex problems and extraordinary numerical performance. Many linear or nonlinear programming solvers are using the trust-region method as an important building block, to name a few, Knitro, IPOPT, and PDFO, etc. Also, in the machine learning field, it inspires the well-known trust-region policy optimization.

Recall

Once

Despite its success in practice as mentioned above, the theoretical development of the TR method is somehow incomplete.

Therefore, a plethora of TR variants \]) have been proposed to improve iteration complexity over the years. The fixed-radius variant by Luenberger and Ye achieves a complexity of $O\left( \epsilon^{- {3/2}} \right)$ for finding $\epsilon$-SOSPs by controlling the stepsize proportionally to the tolerance $\epsilon^{1/2}$. However, this variant tends to be conservative for practical applications.

We summarize the above TR variants and other mainstream second-order methods in Table 1. As an observation, existing research fails to unleash the full potential of trust-region methods: $(a)$ While all aforementioned TR variants have improved complexity guarantee in the nonconvex case, to the best of our knowledge, neither of the nonasymptotic analyses extends to the convex case. Thus, whether a TR method has a global $O\left( \epsilon^{- {1/2}} \right)$ convergence rate in convex optimization remains open.
