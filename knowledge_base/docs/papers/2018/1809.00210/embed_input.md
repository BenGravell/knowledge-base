<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-Driven Chance Constrained Programs over Wasserstein Balls

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We provide an exact deterministic reformulation for data-driven chance constrained programs over Wasserstein balls. For individual chance constraints as well as joint chance constraints with right-hand side uncertainty, our reformulation amounts to a mixed-integer conic program. In the special case of a Wasserstein ball with the 1-norm or the infinity-norm, the cone is the nonnegative orthant, and the chance constrained program can be reformulated as a mixed-integer linear program. Our reformulation compares favourably to several state-of-the-art data-driven optimization schemes in our numerical experiments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Distributionally robust optimization is a powerful modeling paradigm for optimization under uncertainty, where the distribution of the uncertain problem parameters is itself uncertain, and where the performance of a decision is assessed in view of the worst-case distribution from a prescribed ambiguity set. The earlier literature on distributionally robust optimization has focused on moment ambiguity sets which contain all distributions that obey certain (standard or generalized) moment conditions; see, e.g., Delage and Ye, Goh and Sim and Wiesemann et al.. Pflug and Wozabal were the first to propose an ambiguity set of the form of a ball in the space of distributions with respect to the celebrated Wasserstein, Kanthorovich or optimal transport distance.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Wasserstein ambiguity set $\mathcal{F}{(\theta)}$ is then defined as a ball of radius $\theta \geq 0$ with respect to the Wasserstein distance, centered at a prescribed reference distribution $\hat{\mathbb{P}}$: One can think of the Wasserstein radius $\theta$ as a budget on the transportation cost. Indeed, any member distribution in $\mathcal{F}{(\theta)}$ can be obtained by rearranging the reference distribution $\hat{\mathbb{P}}$ at a transportation cost of at most $\theta$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

While it has been recognized early on that Wasserstein ambiguity sets offer many conceptual advantages (*e.g.*, their member distributions do not need to be absolutely continuous with respect to $\hat{\mathbb{P}}$ and, if properly calibrated, they constitute confidence regions for the unknown true data-generating distribution), it was believed that they almost invariably lead to hard global optimization problems. Recently, Mohajerin Esfahani and Kuhn and Zhao and Guan discovered that many interesting distributionally robust optimization problems over Wasserstein ambiguity sets can actually be reformulated as tractable convex programs---provided that $\hat{\mathbb{P}}$ is discrete and that the problem's objective function satisfies certain convexity properties. These reformulations have subsequently been generalized to Polish spaces and non-discrete reference distributions by Blanchet and Murthy and Gao and Kleywegt. Since then, distributionally robust optimization models over Wasserstein ambiguity sets have been proposed for many applications, including transportation and machine learning.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we study distributionally robust chance constrained programs of the form where the goal is to find a decision $\mathbf{x}$ from within a compact polyhedron $\mathcal{X} \subseteq {\mathbb{R}}^{L}$ that minimizes a linear cost function ${\mathbf{c}}^{\top}{\mathbf{x}}$ and ensures that the exogenous random vector $\overset{\sim}{\mathbf{ξ}}$ falls within a decision-dependent safety set ${\mathcal{S}{({\mathbf{x}})}} \subseteq {\mathbb{R}}^{K}$ with high probability $1 - \varepsilon$ under every distribution ${\mathbb{P}} \in {\mathcal{F}{(\theta)}}$.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since the reference distribution $\hat{\mathbb{P}}$ in is the empirical distribution over the training dataset ${\{{\hat{\mathbf{ξ}}}_{i}\}}_{i \in {\lbrack N\rbrack}}$, we refer to as a *data-driven* chance constrained program.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To date, the literature on data-driven chance constraints has focused primarily on variants of problem where the Wasserstein ambiguity set $\mathcal{F}{(\theta)}$ is replaced with an ambiguity set $\mathcal{G}{(\theta)}$ that contains all distributions close to the empirical distribution $\hat{\mathbb{P}}$ with respect to a $\phi$-divergence (such as the Kullback-Leibler divergence or the $\chi^{2}$-distance): where $\phi:{{\mathbb{R}}_{+}\rightarrow{\mathbb{R}}}$ is the divergence function. Hu and Hong show that a distributionally robust chance constrained program over a Kullback-Leibler ambiguity set reduces to a classical chance constrained progam over the reference distribution $\hat{\mathbb{P}}$ and an adjusted risk threshold $\varepsilon' < \varepsilon$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

While this result holds for any reference distribution, $\phi$-divergence ambiguity sets only contain distributions that are absolutely continuous with respect to $\hat{\mathbb{P}}$, that is, any distribution in $\mathcal{G}{(\theta)}$ only assigns positive probability to those measurable subsets $A \subseteq {\mathbb{R}}^{K}$ for which ${\hat{\mathbb{P}}{\lbrack{\overset{\sim}{\mathbf{ξ}} \in A}\rbrack}} > 0$. This is undesirable for problems with a large dimension $K$ and/or few training data, where it is unlikely that every possible value of $\overset{\sim}{\mathbf{ξ}}$ has been observed in ${\{{\hat{\mathbf{ξ}}}_{i}\}}_{i \in {\lbrack N\rbrack}}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

This shortcoming is addressed by Jiang and Guan, who replace the reference distribution with a Kernel density estimator.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite their tremendous success and widespread adoption in recent years, the use of $\phi$-divergences can lead to undesirable side effects in some applications: they compare distributions on a "scenario-by-scenario" basis and thus do not consider the possibility of noisy measurements, and they generically fail to be probability metrics as they typically violate symmetry as well as the triangle inequality. Moreover, as we show next, $\phi$-divergence ambiguity sets may be overly optimistic when only few training samples are available.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

If we replace the Wasserstein ambiguity set $\mathcal{F}{(\theta)}$ with the ambiguity $\mathcal{G}{(\theta)}$ of any $\phi$-divergence, on the other hand, then we can bound the reliability from *above* by Here, the first inequality holds since all distributions in $\mathcal{G}{(\theta)}$ share a common support with $\hat{\mathbb{P}}$, and the second inequality follows from the definition of ${\mathbb{P}}_{0}\text{-VaR}_{\varepsilon}{(\overset{\sim}{\xi})}$. We highlight that this probability bound holds for every radius $\theta$ of the $\phi$-divergence ball $\mathcal{G}{(\theta)}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

While preparing this paper for publication, we became aware of the independent work by Xie, which derives similar reformulations for distributionally individual and joint chance constraints over Wasserstein ambiguity sets. In contrast to our work, however, Xie assumes that each safety condition ${{\mathbf{a}}_{m}^{\top}{\mathbf{x}}} < {b_{m}{({\mathbf{ξ}})}}$, $m \in {\lbrack M\rbrack}$, in the joint chance constraint depends on a subvector of $\mathbf{ξ}$, and that these subvectors are pairwise disjoint for different safety conditions. In other words, different safety conditions of the joint chance constraints studied by Xie must depend on different random variables. Furthermore, the reformulations of Xie are derived via duality theory, whereas our reformulations directly leverage the structural insights into the worst-case distributions.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

This enables us to keep our reformulations largely independent of the selected ground metric for the Wasserstein ball, which opens up possibilities to incorporate other cost functions in our definition of the Wasserstein distance. Since the initial submission of this paper, our exact reformulation for data-driven chance constrained program over Wasserstein balls has been further studied and tightened; see, for instance, Ho-Nguyen et al., Shen and Jiang and Zhang and Dong. Along with these theoretical extensions, our reformulation has also been applied in several domains, including risk sharing in finance, network design for humanitarian operations and optimal power flows in energy systems.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Exact Reformulation of Data-Driven Chance Constraints", "weight": 1.0} -->

Section 2.1 reviews a previously established result on the quantification of uncertainty over Wasserstein balls. We use this result to derive an exact reformulation of generic data-driven chance constrained programs in Section 2.2. We finally specialize this generic reformulation to the subclasses of data-driven individual chance constrained programs as well as data-driven joint chance constrained programs with right-hand side uncertainty in Sections 2.3 and 2.4, respectively.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Uncertainty Quantification over Wasserstein Balls", "weight": 1.0} -->

Consider an open safety set $\mathcal{S} \subseteq {\mathbb{R}}^{K}$, and denote by $\overline{\mathcal{S}} = {{\mathbb{R}}^{K} \smallsetminus \mathcal{S}}$ its closed complement. The uncertainty quantification problem computes the worst (largest) probability of the system under consideration being unsafe, which is the case whenever the random vector $\overset{\sim}{\mathbf{ξ}}$ attains a value in the unsafe set $\overline{\mathcal{S}}$. Throughout the rest of the paper, we exclude trivial special cases and assume that $\theta > 0$ and $\varepsilon \in {}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Uncertainty Quantification over Wasserstein Balls", "weight": 1.0} -->

Blanchet and Murthy as well as Gao and Kleywegt have characterized the solution to the uncertainty quantification problem in closed form. To keep our paper self-contained, we reproduce their findings without proof in Theorem 2.1 below.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

We now develop deterministic reformulations for the distributionally robust chance constrained program. To this end, we focus on the ambiguous chance constraint For any fixed decision ${\mathbf{x}} \in \mathcal{X}$, we let $\mathcal{S}{({\mathbf{x}})}$ be an arbitrary open safety set, and we denote by $\overline{\mathcal{S}}{({\mathbf{x}})}$ its closed complement, which comprises all unsafe scenarios.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

Every fixed training dataset ${\{{\hat{\mathbf{ξ}}}_{i}\}}_{i \in {\lbrack N\rbrack}}$ then induces a (decision-dependent) permutation ${\mathbf{π}}{({\mathbf{x}})}$ of $\lbrack N\rbrack$ that orders the training samples in increasing distance to the unsafe set, that is, We first show that a fixed decision $\mathbf{x}$ satisfies the ambiguous chance constraint over the Wasserstein ambiguity set if and only if the partial sum of the $\varepsilonN$ smallest transportation distances to the unsafe set multiplied by the mass $1/N$ of a training sample exceeds $\theta$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 2.3", "weight": 1.0} -->

Theorem 2.2 establishes that a decision ${\mathbf{x}} \in \mathcal{X}$ satisfies the ambiguous chance constraint if and only if the sum of the $\varepsilonN$ smallest distances of the training samples to the unsafe set $\overline{\mathcal{S}}{({\mathbf{x}})}$ weakly exceeds $\thetaN$. This result is of computational interest because the sum of the $\varepsilonN$ smallest out of $N$ real numbers is concave in those real numbers (while being convex in $\varepsilon$). This reveals that the constraint is convex in the decision-dependent distances ${\{{{\mathbf{d}\mathbf{i}\mathbf{s}\mathbf{t}}{({\hat{\mathbf{ξ}}}_{i},{\overline{\mathcal{S}}{({\mathbf{x}})}})}}\}}_{i \in {\lbrack N\rbrack}}$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Remark 2.3", "weight": 1.0} -->

In the remainder we develop an efficient reformulation of this convex constraint that does not require an enumeration of all possible sums of $\varepsilonN$ different distances between the training samples and the unsafe set. This reformulation is based on the following auxiliary lemma.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Reformulation of Individual Chance Constraints", "weight": 1.0} -->

Assume now that problem accommodates an individual chance constraint defined through the safety set ${\mathcal{S}{({\mathbf{x}})}} = {\{{{\mathbf{ξ}} \in {\mathbb{R}}^{K}}\mid{{{({{{\mathbf{A}}{\mathbf{ξ}}} + {\mathbf{a}}})}^{\top}{\mathbf{x}}} < {{{\mathbf{b}}^{\top}{\mathbf{ξ}}} + b}}\}}$. Individual chance constrained programs have been studied, among others, in network design, vehicle routing and portfolio optimization. By Lemma A.1 in the appendix, we have where we adopt the convention that ${0/0} = 0$, and thus Theorem 2.5 allows us to reformulate problem as the deterministic optimization problem Unfortunately, problem fails to be convex as its constraints involve fractions of convex functions. Below we show, however, that problem can be reformulated as a mixed integer conic program.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 2.7", "weight": 1.0} -->

If, finally, an optimal solution $(\mathbf{q}^{\star},\mathbf{s}^{\star},t^{\star},\mathbf{x}^{\star})$ to problem satisfies ${\mathbf{A}^{\top}\mathbf{x}^{\star}} = \mathbf{b}$ and ${\mathbf{a}^{\top}\mathbf{x}^{\star}} \geq b$, then one would ideally like to solve a variant of problem that includes the additional constraint This variant of problem can be solved by solving ${2K} + 1$ versions of problem, where each version includes exactly one of the constraints ${\lbrack{\mathbf{A}^{\top}\mathbf{x}}\rbrack}_{k} > {\lbrack\mathbf{b}\rbrack}_{k}$,

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 2.7", "weight": 1.0} -->

One readily verifies that the solution that attains the least objective value amongst these ${2K} + 1$ versions of problem is an optimal solution to problem with the added constraint.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 2.8", "weight": 1.0} -->

The mixed-integer conic program simplifies to a mixed-integer linear program whenever $\parallel \cdot \parallel$ represents the $1$-norm or the $\infty$-norm, and it can be reformulated as a mixed-integer second-order cone program whenever $\parallel \cdot \parallel$ represents a $p$-norm for some $p \in {\mathbb{Q}}$, $p > 1$, see Section 2.3.1 in Ben-Tal and Nemirovski.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 2.9", "weight": 1.0} -->

The deterministic reformulation is remarkably parsimonious. For an $L$-dimensional feasible region $\mathcal{X} \subseteq {\mathbb{R}}^{L}$ and an empirical distribution $\hat{\mathbb{P}}$ with $N$ data points, our reformulation has $N$ binary variables, $L + N + 1$ continuous decisions as well as ${2N} + 1$ constraints (excluding those that describe $\mathcal{X}$). In comparison, a classical chance constrained formulation, which is tantamount to setting the Wasserstein radius to $\theta = 0$ in problem, has $N$ binary variables, $L$ continuous decisions as well as $N + 1$ constraints. Thus, adding distributional robustness only requires an additional $N + 1$ continuous decisions as well as $N$ further constraints.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 2.10", "weight": 1.0} -->

The deterministic reformulation requires the specification of a sufficiently large constant $M$, which can typically be determined by an investigation of the structure of problem. Alternatively, many commercial solver packages allow to directly specify the following reformulation of problem via the use of piecewise linear constraints: This formulation has the advantage that it does not require the specification of the constant $M$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Reformulation of Joint Chance Constraints with Right-Hand Side Uncertainty", "weight": 1.0} -->

Indeed, if ${\mathbf{b}}_{m} = \mathbf{0}$, then the $m^{th}$ safety condition in the chance constraint becomes independent of the uncertainty and can thus be absorbed in $\mathcal{X}$. Joint chance constrained programs with right-hand side uncertainty have been proposed, among others, for problems in transportation, lot-sizing, unit commitment and project management.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 2.12", "weight": 1.0} -->

The deterministic reformulation has $N$ binary variables, $L + N + 1$ continuous decisions as well as ${{({M + 1})}N} + 1$ constraints (excluding those that describe $\mathcal{X}$). In comparison, the corresponding classical chance constrained formulation has $N$ binary variables, $L$ continuous decisions as well as ${MN} + 1$ constraints. Thus, adding distributional robustness requires an additional $N + 1$ continuous decisions as well as $N$ further (linear) constraints.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We compare our exact reformulation of the ambiguous chance constrained program with the bicriteria approximation scheme of Xie and Ahmed on a portfolio optimization problem in Section 3.1 as well as with a classical (non-ambiguous) chance constrained formulation and a Kernel density estimator based version of the ambiguous chance constrained program over a $\phi$-divergence ambiguity set on a transportation problem in Section 3.2. Our goal is to investigate the computational scalability of our reformulation as well as its out-of-sample performance in a data-driven setting. All results were produced on an Intel Xeon 2.66GHz processor with 8GB memory in single-core mode using CPLEX 12.8. Following Remark 2.10, we avoid the specification of the constant $M$ in our ambiguous chance constrained program through the use of piecewise linear constraints.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Portfolio Optimization", "weight": 1.0} -->

We consider a portfolio optimization problem studied by Xie and Ahmed. The problem asks for the minimum-cost portfolio investment $\mathbf{x}$ into $K$ assets with random returns ${\overset{\sim}{\xi}}_{1},\ldots,{\overset{\sim}{\xi}}_{K}$ that exceeds a pre-specified target return $w$ with high probability $1 - \varepsilon$. The problem can be cast as the following instance of the ambiguous chance constrained program: We compare our exact reformulation of problem with the $(\sigma,\gamma)$-bicriteria approximation scheme of Xie and Ahmed, which produces solutions that satisfy the ambiguous chance constraint in with probability $1 - {\sigma\varepsilon}$, $\sigma > 1$, and whose costs are guaranteed to exceed the optimal costs in by a factor of at most $\gamma = {\sigma/{({\sigma - 1})}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Portfolio Optimization", "weight": 1.0} -->

Since the bicriteria approximation scheme can readily utilize support information for the random vector $\overset{\sim}{\mathbf{ξ}}$, we replace the ambiguity set $\mathcal{F}{(\theta)}$ with ${\overline{\mathcal{F}}{(\theta)}} = {{\mathcal{F}{(\theta)}} \cap {\{{\mathbb{P}}\mid{{{\mathbb{P}}{\lbrack{\overset{\sim}{\mathbf{ξ}} \in {\mathbb{R}}_{+}^{K}}\rbrack}} = 1}\}}}$ in their approach. Contrary to the experiments conducted by Xie and Ahmed, we set $\sigma = 1$. This is to the disadvantage of their approach, as it does not provide any approximation guarantees in that case, but it allows us to compare the resulting portfolios as they provide the same return guarantees.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Portfolio Optimization", "weight": 1.0} -->

For the performance of the bicriteria approximation scheme with $\sigma > 1$, we refer to Section 6.2 of Xie and Ahmed.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Portfolio Optimization", "weight": 1.0} -->

In our numerical experiments, we consider a similar setting as Xie and Ahmed. We set $K = 50$, $w = 1$ and choose the cost coefficients $c_{1},\ldots,c_{50}$ uniformly at random from $\{ 1,\ldots,100\}$. Each asset return ${\overset{\sim}{\xi}}_{i}$ is governed by a uniform distribution on $\lbrack 0.8,1.5\rbrack$, and we assume that $N = 100$ training samples ${\hat{\mathbf{ξ}}}_{1},\ldots,{\hat{\mathbf{ξ}}}_{100}$ are available. We use the $2$-norm Wasserstein ambiguity set, which implies that our exact reformulation of problem is a mixed-integer second-order cone program, and set the Wasserstein radius to $\theta \in {\{ 0.05,0.1,0.2\}}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Portfolio Optimization", "weight": 1.0} -->

The risk threshold is set to $\varepsilon \in {\{ 0.05,0.1\}}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Portfolio Optimization", "weight": 1.0} -->

Ratio of objective values Table 1: Objective and runtime ratios of the bicriteria approximation scheme for different values of ε and θ. For each parameter setting, we report the 5%, 50% and 95% quantiles over 50 randomly generated instances.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Portfolio Optimization", "weight": 1.0} -->

Table 1 compares the objective values and runtimes of our exact reformulation and the bicriteria approximation scheme for various combinations of the risk threshold $\varepsilon$ and Wasserstein radius $\theta$. The table shows that despite incorporating additional support information, the bicriteria approximation scheme determines solutions whose costs significantly exceed those of the solutions found by our exact reformulation. Perhaps more surprisingly, the bicriteria approximation scheme is also computationally more expensive. As Figure 4 shows, however, this is an artifact of the small sample size $N$ employed in the experiments of Xie and Ahmed, and the bicriteria approximation scheme is faster than our exact reformulation for larger samples sizes.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Transportation", "weight": 1.0} -->

We consider a probabilistic transportation problem studied by Luedtke et al. and Yanagisawa and Osogami. The problem asks for the cost-optimal distribution of a single good from a set of factories $f \in {\lbrack F\rbrack}$ to a set of distribution centers $d \in {\lbrack D\rbrack}$. Each factory $f \in {\lbrack F\rbrack}$ has an individual production capacity $m_{f}$, and each distribution center $d \in {\lbrack D\rbrack}$ faces a random aggregate customer demand ${\overset{\sim}{\xi}}_{d}$. The cost of shipping one unit of the good from factory $f$ to distribution center $d$ is denoted by $c_{fd}$. We aim to find a transportation plan that minimizes the shipping costs, respects the production capacity of each factory and satisfies the demand at each distribution center with high probability.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Transportation", "weight": 1.0} -->

The problem can be cast as the following instance of problem: Here, $x_{fd}$ denotes the quantity shipped from factory $f \in {\lbrack F\rbrack}$ to distribution center $d \in {\lbrack D\rbrack}$. Problem is an ambiguous joint chance constrained program with right-hand side uncertainty. Since each safety condition in contains a single random variable with coefficient $1$ on the right-hand side, our exact reformulation reduces to the same mixed-integer linear program for any norm $\parallel \cdot \parallel$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Transportation", "weight": 1.0} -->

In our first experiment, we investigate the scalability of the exact reformulation of problem that is offered by Proposition 2.11. To this end, we generate random test instances with $5$ factories and $10,20,\ldots,50$ distribution centers that are located uniformly at random on the Euclidean plane ${\lbrack 0,10\rbrack}^{2}$. We identify the transportation costs $c_{fd}$ with the Euclidean distances between the factories and distribution centers. The demand vector $\overset{\sim}{\mathbf{ξ}}$ is described by $50$, $100$ or $150$ samples from a uniform distribution that is supported on $\lbrack{0.8{\mathbf{μ}}},{1.2{\mathbf{μ}}}\rbrack$, where the expected demand $\mu_{d}$ at distribution center $d \in {\lbrack D\rbrack}$ is picked uniformly at random from the interval $\lbrack 0,10\rbrack$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Transportation", "weight": 1.0} -->

The capacity of each factory is chosen uniformly at random, and the capacities are subsequently scaled so that the factories can jointly produce up to $150\%$ of the maximum cumulative demand. For each instance, we choose $10$ ascending Wasserstein radii $\theta_{1} < \ldots < \theta_{10}$ uniformly so that $\theta_{1} = 0.001$ and $\theta_{10}$ is the smallest radius for which the corresponding instance of problem becomes infeasible. We fix $\varepsilon = 0.1$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Transportation", "weight": 1.0} -->

Tables 2--4 and Figure 5 compare the runtimes of our ambiguous chance constrained program with those of the classical chance constrained formulation of problem, where $M$ is a sufficiently large positive constant. The results show that for the smallest Wasserstein radius $\theta_{1} = 0.001$, the ambiguous chance constrained program is---as expected---more difficult to solve than the corresponding classical chance constrained program. Interestingly, the ambiguous chance constrained program becomes considerably *easier* to solve than the classical chance constrained program for the larger Wasserstein radii $\theta_{2},\ldots,\theta_{10}$. This surprising result is explained in Figure 6, which shows that the feasible region of the ambiguous chance constrained program tends to convexify as the Wasserstein radius $\theta$ increases. In fact, one can show that the set of vectors ${\mathbf{q}} \in {\{ 0,1\}}^{N}$ that are feasible in the deterministic reformulation of problem shrinks monotonically with $\theta$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Transportation", "weight": 1.0} -->

Since it is the presence of these binary vectors that causes the non-convexity of problem, one can expect the problem to become better behaved as $\theta$ increases.

<!-- chunk {"id": "body-0044", "role": "body", "section": "of distribution", "weight": 1.0} -->

We next compare the out-of-sample performance of our ambiguous chance constrained program, where the risk threshold $\varepsilon \in {\{ 0.1,\, 0.05,\, 0.01\}}$ and the Wasserstein radius $\theta \in {\{{{1E} - i}:{i = {2,3,\ldots,6}}\}}$ are selected using a $7$-fold cross-validation on the training dataset ('DRO'), with *(i)* the classical chance constrained program, where the risk threshold is fixed to $\varepsilon = 0.1$ ('SAA'), *(ii)* a variant of the classical chance constrained program, where the risk threshold $\varepsilon \in {{\{{{1E} - i}:{i = {1,2,\ldots,5}}\}} \cup {\{ 0.05\}}}$ is selected using a $7$-fold cross-validation on the training dataset ('CCT'), as well as

<!-- chunk {"id": "body-0045", "role": "body", "section": "of distribution", "weight": 1.0} -->

*(iii)* a Kernel density estimator based version of the ambiguous chance constrained program over a $\phi$-divergence ambiguity set, where the risk threshold $\varepsilon \in {\{ 0.1,\, 0.05,\, 0.01\}}$ and the bandwidth $h \in {\{{{1E} - i}:{i = {{- 2},{- 1},\ldots,3}}\}}$ of the Gaussian kernel are selected using a $7$-fold cross-validation on the training dataset.

<!-- chunk {"id": "body-0046", "role": "body", "section": "of distribution", "weight": 1.0} -->

We note that CCT can be regarded as a cross-validated version of the 'best data-driven reformulation' proposed by Lam. We generate random problem instances with $5$ factories, $20$ distribution centers and $25$, $30$,..., $250$ training samples.

<!-- chunk {"id": "body-0047", "role": "body", "section": "of distribution", "weight": 1.0} -->

In all experiments, the expected demand $\mu_{d}$ at distribution center $d \in {\lbrack D\rbrack}$ is picked uniformly at random from the interval $\lbrack 0,10\rbrack$, whereas the actual demands follow a uniform distribution that is supported on $\lbrack{0.8{\mathbf{μ}}},{1.2{\mathbf{μ}}}\rbrack$ (Figure 7), a normal distribution with mean $\mathbf{μ}$ and covariance matrix ${0.1 \cdot \text{diag}}{({\mathbf{μ}})}$ (Figure 8) or an exponential distribution where each distribution center $d \in {\lbrack D\rbrack}$ faces a demand ${({1 + {0.4 \cdot {\lbrack{{\overset{\sim}{\zeta}}_{d} - 0.5}\rbrack}}})} \cdot \mu_{d}$, where

<!-- chunk {"id": "body-0048", "role": "body", "section": "of distribution", "weight": 1.0} -->

${\overset{\sim}{\zeta}}_{d}$ follows an exponential distribution with parameter $\lambda = 2$ (Figure 9).

<!-- chunk {"id": "body-0049", "role": "body", "section": "of distribution", "weight": 1.0} -->

In all cases, the demands are truncated to the non-negative real line. Our results indicate that the classical chance constrained program generates solutions that significantly violate the chance constraint, even if we select the risk threshold $\varepsilon$ out-of-sample. The two ambiguous chance constrained formulations, on the other hand, achieve the desired risk threshold, often at a modest increase in transportation costs. While our approach and the $\phi$-divergence ambiguity set perform similarly, our formulation appears to result in lower transportation costs, especially when data is scarce.
