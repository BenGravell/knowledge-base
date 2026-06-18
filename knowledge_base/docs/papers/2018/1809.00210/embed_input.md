Data-Driven Chance Constrained Programs over Wasserstein Balls

We provide an exact deterministic reformulation for data-driven chance constrained programs over Wasserstein balls. For individual chance constraints as well as joint chance constraints with right-hand side uncertainty, our reformulation amounts to a mixed-integer conic program. In the special case of a Wasserstein ball with the 1-norm or the infinity-norm, the cone is the nonnegative orthant, and the chance constrained program can be reformulated as a mixed-integer linear program. Our reformulation compares favourably to several state-of-the-art data-driven optimization schemes in our numerical experiments.

## Introduction

Distributionally robust optimization is a powerful modeling paradigm for optimization under uncertainty, where the distribution of the uncertain problem parameters is itself uncertain, and where the performance of a decision is assessed in view of the worst-case distribution from a prescribed ambiguity set. The earlier literature on distributionally robust optimization has focused on moment ambiguity sets which contain all distributions that obey certain (standard or generalized) moment conditions; see, e.g., Delage and Ye, Goh and Sim and Wiesemann et al..

One can think of the Wasserstein radius $\theta$ as a budget on the transportation cost. Indeed, any member distribution in $\mathcal{F}{(\theta)}$ can be obtained by rearranging the reference distribution $\hat{\mathbb{P}}$ at a transportation cost of at most $\theta$. If only a finite training dataset ${\{{\hat{\mathbf{ξ}}}_{i}\}}_{i \in {\lbrack N\rbrack}}$ is available, a natural choice for $\hat{\mathbb{P}}$ is the empirical distribution $\hat{\mathbb{P}} = {\frac{1}{N}{\sum_{i = 1}^{N}\delta_{{\hat{\mathbf{ξ}}}_{i}}}}$, which represents the uniform distribution on the training samples.

While it has been recognized early on that Wasserstein ambiguity sets offer many conceptual advantages (*e.g.*, their member distributions do not need to be absolutely continuous with respect to $\hat{\mathbb{P}}$ and, if properly calibrated, they constitute confidence regions for the unknown true data-generating distribution), it was believed that they almost invariably lead to hard global optimization problems.

In this paper we study distributionally robust chance constrained programs of the form

Despite their tremendous success and widespread adoption in recent years, the use of $\phi$-divergences can lead to undesirable side effects in some applications: they compare distributions on a "scenario-by-scenario" basis and thus do not consider the possibility of noisy measurements, and they generically fail to be probability metrics as they typically violate symmetry as well as the triangle inequality. Moreover, as we show next, $\phi$-divergence ambiguity sets may be overly optimistic when only few training samples are available.
