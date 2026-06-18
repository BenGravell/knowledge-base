Data-driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations

Topics include Robustness, Uncertainty, Datasets, Optimization, Wasserstein distances, Metric, Wasserstein metric, Robust optimization, Probability distribution, Optimization problem.

We consider stochastic programs where the distribution of the uncertain parameters is only observable through a finite training dataset. Using the Wasserstein metric, we construct a ball in the space of (multivariate and non-discrete) probability distributions centered at the uniform distribution on the training samples, and we seek decisions that perform best in view of the worst-case distribution within this Wasserstein ball. The state-of-the-art methods for solving the resulting distributionally robust optimization problems rely on global optimization techniques, which quickly become computationally excruciating. In this paper we demonstrate that, under mild assumptions, the distributionally robust optimization problems over Wasserstein balls can in fact be reformulated as finite convex programs - in many interesting cases even as tractable linear programs. Leveraging recent measure concentration results, we also show that their solutions enjoy powerful finite-sample performance guarantees. Our theoretical results are exemplified in mean-risk portfolio optimization as well as uncertainty quantification.

## Introduction

Stochastic programming is a powerful modeling paradigm for optimization under uncertainty. The goal of a generic single-stage stochastic program is to find a decision $x \in {\mathbb{R}}^{n}$ that minimizes an expected cost ${\mathbb{E}}^{\mathbb{P}}{\lbrack{h{(x,\xi)}}\rbrack}$, where the expectation is taken with respect to the distribution $\mathbb{P}$ of the continuous random vector $\xi \in {\mathbb{R}}^{m}$. However, classical stochastic programming is challenged by the large-scale decision problems encountered in today's increasingly interconnected world....

Distributionally robust optimization is an alternative modeling paradigm, where the objective is to find a decision $x$ that minimizes the worst-case expected cost $\sup_{{\mathbb{Q}} \in \mathcal{P}}{{\mathbb{E}}^{\mathbb{Q}}{\lbrack{h{(x,\xi)}}\rbrack}}$. Here, the worst-case is taken over an ambiguity set $\mathcal{P}$, that is, a family of distributions characterized through certain known properties of the unknown data-generating distribution $\mathbb{P}$....

Figure 10. Dependence of the confidence bounds and the Wasserstein radius on N

Figure 10(b) shows the Wasserstein radius ${\hat{\varepsilon}}_{N}^{cv}$ obtained via $k$-fold cross validation (both for ${\hat{J}}_{N}^{+}$ and ${\hat{J}}_{N}^{-}$). As usual, all results are averaged across 300 independent simulation runs. A comparison with Figure 8 reveals that the data-driven Wasserstein radii in uncertainty quantification display a similar but faster polynomial decay than in portfolio optimization. We conjecture that this is due to the absence of decisions, which implies that uncertainty quantification is less susceptible to the optimizer's curse....

where the last equality follows again from strong linear programming duality, which holds since the primal maximization problem is feasible. Assertion (ii) then follows by substituting ${\lbrack{- \ell}\rbrack}^{\ast}$ as well as the formula for $\sigma_{\Xi}$ from the proof of assertion (i) into (18. ‣ 4.1. Reduction to a Finite Convex Program ‣ 4. Solving Worst-Case Expectation Problems ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")). ∎

### Extremal Distributions

If $\Xi_{t}$ and ${\{\ell_{tk}\}}_{k \leq K}$ satisfy the convexity Assumption 4.1. ‣ 4....
