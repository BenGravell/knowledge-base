Stochastic Zeroth-Order Optimization under Strongly Convexity and Lipschitz Hessian: Minimax Sample Complexity

Topics include Regret bounds, Online algorithms, Sample complexity, Optimization, Learning, Sampling, Hessian.

Optimization of convex functions under stochastic zeroth-order feedback has been a major and challenging question in online learning. In this work, we consider the problem of optimizing second-order smooth and strongly convex functions where the algorithm is only accessible to noisy evaluations of the objective function it queries. We provide the first tight characterization for the rate of the minimax simple regret by developing matching upper and lower bounds. We propose an algorithm that features a combination of a bootstrapping stage and a mirror-descent stage. Our main technical innovation consists of a sharp characterization for the spherical-sampling gradient estimator under higher-order smoothness conditions, which allows the algorithm to optimally balance the bias-variance tradeoff, and a new iterative method for the bootstrapping stage, which maintains the performance for unbounded Hessian.

## Introduction

Stochastic optimization of an unknown function with access to only noisy function evaluations is a fundamental problem in operations research, optimization, simulation and bandit optimization research, commonly known as *zeroth-order optimization*, *derivative-free optimization* (Conn et al. Rios & Sahinidis, ) or *bandit optimization*. In this problem, an optimization algorithm interacts sequentially with an oracle and obtains noisy function evaluations at queried points every time.

Existing

Convex functions. In the first thread of research, the unknown objective function to be optimized is assumed to be *concave* (for maximization problems) or *convex* (for minimization problems). For these problems, with minimal smoothness (e.g. objective function being Lipschitz continuous) it is possible to achieve a sample complexity of $\overset{\sim}{O}{(\varepsilon^{- 2})}$ for an expected optimization error or $\varepsilon$, which is also a polynomial function of domain dimension $d$; see for example the works of Agarwal et al.; Lattimore & Gyorgy; Bubeck et al.;

Smooth functions. In the second thread of research, the unknown objective function to be optimized is assumed to be highly *smooth*, but not necessary concave/convex. Typical results assume the objective function is Hölder smooth of order $k \geq 1$, meaning that the $({k - 1})$-th derivative of the objective function is Lipschitz continuous. Without additional conditions, the optimal sample complexity with such smoothness assumptions is $\overset{\sim}{O}{(\varepsilon^{- {({2 + {d/k}})}})}$, which scales exponentially with the domain dimension $d$.

In this paper, we study the optimal sample complexity of stochastic zeroth-order optimization when the objective function exhibits both (strong) convexity and a high degree of smoothness. As we have remarked in the first bullet point above, with convexity and Hölder smoothness of order $k = 1$ (equivalent to the objective function being Lipschitz continuous), the works of Agarwal et al.; Lattimore & Gyorgy; Bubeck et al. established an $\overset{\sim}{O}{(\varepsilon^{- 2})}$ upper bound.
