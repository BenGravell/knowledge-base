Data-Driven Chance Constrained Programs over Wasserstein Balls

We provide an exact deterministic reformulation for data-driven chance constrained programs over Wasserstein balls. For individual chance constraints as well as joint chance constraints with right-hand side uncertainty, our reformulation amounts to a mixed-integer conic program. In the special case of a Wasserstein ball with the 1-norm or the infinity-norm, the cone is the nonnegative orthant, and the chance constrained program can be reformulated as a mixed-integer linear program. Our reformulation compares favourably to several state-of-the-art data-driven optimization schemes in our numerical experiments.

## Introduction

Distributionally robust optimization is a powerful modeling paradigm for optimization under uncertainty, where the distribution of the uncertain problem parameters is itself uncertain, and where the performance of a decision is assessed in view of the worst-case distribution from a prescribed ambiguity set. The earlier literature on distributionally robust optimization has focused on moment ambiguity sets which contain all distributions that obey certain (standard or generalized) moment conditions; see, e.g., Delage and Ye, Goh and Sim and Wiesemann et al.....

One can think of the Wasserstein radius $\theta$ as a budget on the transportation cost. Indeed, any member distribution in $\mathcal{F}{(\theta)}$ can be obtained by rearranging the reference distribution $\hat{\mathbb{P}}$ at a transportation cost of at most $\theta$. If only a finite training dataset ${\{{\hat{\mathbf{ξ}}}_{i}\}}_{i \in {\lbrack N\rbrack}}$ is available, a natural choice for $\hat{\mathbb{P}}$ is the empirical distribution $\hat{\mathbb{P}} = {\frac{1}{N}{\sum_{i = 1}^{N}\delta_{{\hat{\mathbf{ξ}}}_{i}}}}$, which represents the uniform distribution on the training samples....

Figure 9: Probability of meeting the safety conditions (left) and transportation costs (right) for several data-driven approaches in our transportation problem with exponentially distributed demands. Both figures present median quantities over 100 random instances.

We next compare the out-of-sample performance of our ambiguous chance constrained program, where the risk threshold $\varepsilon \in {\{ 0.1,\, 0.05,\, 0.01\}}$ and the Wasserstein radius $\theta \in {\{{{1E} - i}:{i = {2,3,\ldots,6}}\}}$ are selected using a $7$-fold cross-validation on the training dataset ('DRO'), with *(i)* the classical chance constrained program, where the risk threshold is fixed to $\varepsilon = 0.1$ ('SAA'), *(ii)* a variant of the classical chance constrained program, where the risk threshold $\varepsilon \in {{\{{{1E} - i}:{i = {1,2,\ldots,5}}\}} \cup {\{ 0.05\}}}$ is selected using a $7$-fold cross-validation...

where we adopt the convention that ${0/0} = 0$, and thus Theorem 2.5 allows us to reformulate problem as the deterministic optimization problem

We can re-express problem as the univariate discrete optimization problem

### Proposition 2.11
