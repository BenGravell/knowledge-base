Making SGD Parameter-Free

Topics include Convex optimization, Regret bounds, Online algorithms, Optimization, SCO, Rate of convergence.

We develop an algorithm for parameter-free stochastic convex optimization (SCO) whose rate of convergence is only a double-logarithmic factor larger than the optimal rate for the corresponding known-parameter setting. In contrast, the best previously known rates for parameter-free SCO are based on online parameter-free regret bounds, which contain unavoidable excess logarithmic terms compared to their known-parameter counterparts. Our algorithm is conceptually simple, has high-probability guarantees, and is also partially adaptive to unknown gradient norms, smoothness, and strong convexity. At the heart of our results is a novel parameter-free certificate for SGD step size choice, and a time-uniform concentration result that assumes no a-priori bounds on SGD iterates.

## Introduction

Stochastic convex optimization (SCO) is a cornerstone of both the theory and practice of machine learning. Consequently, there is intense interest in developing SCO algorithms that require little to no prior knowledge of the problem parameters, and hence little to no tuning. In this work we consider the fundamental problem of non-smooth SCO (in a potentially unbounded domain) and seek methods that are adaptive to a key problem parameter: the initial distance to optimality.

Current approaches for tackling this problem focus on the more general online learning problem of *parameter-free regret minimization*, where the goal is to to obtain regret guarantees that are valid for comparators with arbitrary norms. Research on parameter-free regret minimization has lead to practical algorithms for stochastic optimization, methods that are able to adapt to many problem parameters simultaneously \[\] and methods that can work with any norm \[\]....

For any $\varepsilon > 0$, $\delta \in {}$, and $M \in {\mathbb{N}}$, computing $x^{(M)}$ in the procedure described above requires at most $B = 2^{M + 1}$ gradient queries. If $f$ is $\mu$-strongly convex and has a stochastic gradient oracle bounded by $L$, then with probability at least $1 - \delta$ we have

See proof in Section C.2. Compared to results obtained via parameter-free strongly-convex regret bounds \[, Thm. 7\], we remove a squared logarithmic factor, breaking two regret minimization barriers at once.

Let us briefly summarize our findings so far. When RootFindingBisection returns at algorithm 1, Proposition 2 provide a bound similar to the best achievable when $d_{0}$ is known, with only a factor $O{({\log{\log\frac{\eta_{hi}}{\eta_{lo}}}})}$ complexity increase. If instead the lower limit of the bisection is invalid, i.e., $\eta_{lo} > {\phi{(\eta_{lo})}}$, our bound becomes the optimal rate plus a term proportional to $\eta_{lo}$....

The proof of Proposition 1 hinges on two lemmas. The first is a variant of the standard SGD error bound (recall that ${\Delta_{i}{(\eta)}} = {{g_{i}{(\eta)}} - {{\nabla f}{({x_{i}{(\eta)}})}}}$ is zero in the noiseless setting).

With this definition in hand, slightly modified versions of our key lemmas from the deterministic analysis (Lemma, Proposition, Lemma ) continue to hold....
