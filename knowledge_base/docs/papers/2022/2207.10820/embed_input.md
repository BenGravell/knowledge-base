Mean Robust Optimization

Topics include Robustness, Uncertainty, Clustering, Optimization, Control, Wasserstein distances, Robust optimization.

Robust optimization is a tractable and expressive technique for decision-making under uncertainty, but it can lead to overly conservative decisions when pessimistic assumptions are made on the uncertain parameters. Wasserstein distributionally robust optimization can reduce conservatism by being data-driven, but it often leads to very large problems with prohibitive solution times. We introduce mean robust optimization, a general framework that combines the best of both worlds by providing a trade-off between computational effort and conservatism. We propose uncertainty sets constructed based on clustered data rather than on observed data points directly thereby significantly reducing problem size. By varying the number of clusters, our method bridges between robust and Wasserstein distributionally robust optimization. We show finite-sample performance guarantees and explicitly control the potential additional pessimism introduced by any clustering procedure. In addition, we prove conditions for which, when the uncertainty enters linearly in the constraints, clustering does not affect the optimal solution....

## Introduction

Robust optimization (RO) and distributionally robust optimization (DRO) are popular tools for decision-making under uncertainty due to their high expressiveness and versatility. The main idea of RO is to define an uncertainty set and to minimize the worst-case cost across possible uncertainty realizations in that set. However, while RO often leads to tractable formulations, it can be overly-conservative. To reduce conservatism, DRO takes a probabilistic approach, by modeling the uncertainty as a random variable following a probability distribution known only to belong to an uncertainty set (also called ambiguity set) of distributions....

Traditional approaches design uncertainty sets based on theoretical assumptions on the uncertainty distributions. While these methods have been quite successful, they rely on a priori assumptions that are difficult to verify in practice. On the other hand, the last decade has seen an explosion in the availability of data. This change has brought a shift in focus from a priori assumptions on the probability distributions to data-driven methods in operations research and decision sciences. In RO and DRO, this new paradigm has fostered data-driven methods where uncertainty sets are shaped directly from data....

Figure 23: Newsvendor. Left: in-sample objective values vs ϵ for K = 100. Right: objective value vs β for K = 100.

Figure 24: Newsvendor. Left: the difference in the value of the uncertain objective between using N and K clusters, calculated as ${{\overline{g}}^{N}{(x)}} - {{\overline{g}}^{K}{(x)}}$, compared with the theoretical upper bound δ (K,z,γ) from Corollary 4.2.1. Solid lines are the difference, dotted lines are the upper bounds. Right: solve time.

## Worst-case value of the uncertain constraint

with each $- g_{j}$ being proper, convex, and lower-semicontinuous in $u$ for all $x$. When we take $J = 1$, we arrive back at the formulations given in Section 2. Note that any problem with multiple uncertain constraints ${{{g_{j}{(u,x)}},j} = 1},{\ldots,J}$, where we assume the usual conditions on $g_{j}$, can be combined to create a joint constraint of this maximum-of-concave form. As mentioned in Section 2.1, this can also be used to model $\operatorname{\mathbf{C}\mathbf{V}\mathbf{a}\mathbf{R}}$ constraints, which has a maximum-of-concave analytical form.

### Choosing $K$
