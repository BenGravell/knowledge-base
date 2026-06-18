Stochastic Zeroth-Order Optimization under Strongly Convexity and Lipschitz Hessian: Minimax Sample Complexity

Topics include Regret bounds, Online algorithms, Sample complexity, Optimization, Learning, Sampling, Hessian.

Optimization of convex functions under stochastic zeroth-order feedback has been a major and challenging question in online learning. In this work, we consider the problem of optimizing second-order smooth and strongly convex functions where the algorithm is only accessible to noisy evaluations of the objective function it queries. We provide the first tight characterization for the rate of the minimax simple regret by developing matching upper and lower bounds. We propose an algorithm that features a combination of a bootstrapping stage and a mirror-descent stage. Our main technical innovation consists of a sharp characterization for the spherical-sampling gradient estimator under higher-order smoothness conditions, which allows the algorithm to optimally balance the bias-variance tradeoff, and a new iterative method for the bootstrapping stage, which maintains the performance for unbounded Hessian.

## Introduction

Stochastic optimization of an unknown function with access to only noisy function evaluations is a fundamental problem in operations research, optimization, simulation and bandit optimization research, commonly known as *zeroth-order optimization*, *derivative-free optimization* (Conn et al. Rios & Sahinidis, ) or *bandit optimization*. In this problem, an optimization algorithm interacts sequentially with an oracle and obtains noisy function evaluations at queried points every time....

Existing works and results on stochastic zeroth-order optimization could be broadly categorized into two classes:

where f2 is the Taylor polynomial of f expanded at x up to the quadratic terms. Consequently, inequality (4.2) implies

where the expectations are taken of u ∼ Unif(Sd − 1), and the last equality is due to the well-known fact that ${{\mathbb{E}}\left\lbrack {{\mathbf{u}}{\mathbf{u}}^{\intercal}} \right\rbrack} = {\frac{1}{d}I_{d}}$.
5 Conclusion and Future Work
In this work, we achieve the first minimax simple regret for bandit optimization of second-order smooth and strongly convex functions. We derived the matching upper and lower bounds and proposed an algorithm that integrates a bootstrapping stage with a mirror-descent stage....

We postpone the proof of the above theorems to Section 4.2 and Appendix C and proceed to describe how these results are used in the algorithm.
For brevity, let $\epsilon \triangleq {\frac{\rho^{\frac{2}{3}}}{M}dT^{- \frac{2}{3}}}$ be the minimax regret we aim to achieve, and let xB denote the estimator x stored at the end of the first stage. The role of the final stage is to ensure that if f(xB) − f(x*) is sufficiently small with high probability, the final result of the proposed algorithm achieves the stated simple regret guarantees. Formally, we require that

In the rest of this paper, we let ℱ(ρ,M,R) denote the set of all second-order differentiable functions that satisfy the above conditions, with corresponding constants given by ρ, M, and R. We aim to find algorithms to achieve asymptotically the following minimax simple regret, which measures the expected difference of the objective function on xT and the optimum.

To prove inequality, we investigate the following function

Convex functions. In the first thread of research, the unknown objective function to be optimized is assumed to be *concave* (for...
