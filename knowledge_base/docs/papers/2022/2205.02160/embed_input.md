Making SGD Parameter-Free

Topics include Convex optimization, Regret bounds, Online algorithms, Optimization, SCO, Rate of convergence.

We develop an algorithm for parameter-free stochastic convex optimization (SCO) whose rate of convergence is only a double-logarithmic factor larger than the optimal rate for the corresponding known-parameter setting. In contrast, the best previously known rates for parameter-free SCO are based on online parameter-free regret bounds, which contain unavoidable excess logarithmic terms compared to their known-parameter counterparts. Our algorithm is conceptually simple, has high-probability guarantees, and is also partially adaptive to unknown gradient norms, smoothness, and strong convexity. At the heart of our results is a novel parameter-free certificate for SGD step size choice, and a time-uniform concentration result that assumes no a-priori bounds on SGD iterates.

## Introduction

Stochastic convex optimization (SCO) is a cornerstone of both the theory and practice of machine learning. Consequently, there is intense interest in developing SCO algorithms that require little to no prior knowledge of the problem parameters, and hence little to no tuning. In this work we consider the fundamental problem of non-smooth SCO (in a potentially unbounded domain) and seek methods that are adaptive to a key problem parameter: the initial distance to optimality.

Current approaches for tackling this problem focus on the more general online learning problem of *parameter-free regret minimization*, where the goal is to to obtain regret guarantees that are valid for comparators with arbitrary norms. Research on parameter-free regret minimization has lead to practical algorithms for stochastic optimization, methods that are able to adapt to many problem parameters simultaneously and methods that can work with any norm.

In this paper we show it is possible to obtain stronger parameter-free rates for SCO by moving beyond the regret minimization abstraction. In particular, for any $\varepsilon > 0$ and $\delta \in {}$, we a obtain probability $1 - \delta$ optimality gap bounds of

Our method also provides high probability guarantees on the suboptimality gap. This resolves an open problem in parameter-free optimization; see and \[, §7\]. We are able to form high probability bounds because, unlike other parameter-free SCO algorithms, we prove a strong localization guarantee: our output $\overline{x}$ satisfies ${\|{\overline{x} - x_{\star}}\|} = {O{({\|{x_{0} - x_{\star}}\|})}}$, and key intermediate points satisfy a similar bound as well.

## Limitations of online-to-batch conversion

To the best of our knowledge, the only previous example of an SCO rate that is provably unachievable by online to batch conversion of a (uniform) regret bound occurs for strongly-convex optimization. Specifically, any online strongly-convex optimization algorithm must have logarithmic regret (implying suboptimality ${({\log T})}/T$ via online to batch conversion), while Hazan and Kale and others have achieved the optimal $1/T$ rate for stochastic strongly-convex optimization.
