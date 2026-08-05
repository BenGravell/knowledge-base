<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-Driven Chance Constrained Programs over Wasserstein Balls

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We provide an exact deterministic reformulation for data-driven chance constrained programs over Wasserstein balls. For individual chance constraints as well as joint chance constraints with right-hand side uncertainty, our reformulation amounts to a mixed-integer conic program. In the special case of a Wasserstein ball with the 1-norm or the infinity-norm, the cone is the nonnegative orthant, and the chance constrained program can be reformulated as a mixed-integer linear program. Our reformulation compares favourably to several state-of-the-art data-driven optimization schemes in our numerical experiments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Distributionally robust optimization is a powerful modeling paradigm for optimization under uncertainty, where the distribution of the uncertain problem parameters is itself uncertain, and where the performance of a decision is assessed in view of the worst-case distribution from a prescribed ambiguity set. The earlier literature on distributionally robust optimization has focused on moment ambiguity sets which contain all distributions that obey certain (standard or generalized) moment conditions; see, e.g., [Delage\_Ye\_2010], [Goh\_Sim\_2010] and [Wiesemann\_Kuhn\_Sim\_2014]. [Pflug\_Wozabal\_2007] were the first to propose an ambiguity set of the form of a ball in the space of distributions with respect to the celebrated Wasserstein, Kanthorovich or optimal transport distance.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The type-1 Wasserstein distance $d_{\rm W}(\mathbb{P}_1,\mathbb{P}_2)$ between two distributions $\mathbb{P}_1$ and $\mathbb{P}_2$ on $\mathbb{R}^K$, equipped with a general norm $\|\cdot\|$, is defined as the minimal transportation cost of moving $\mathbb{P}_1$ to $\mathbb{P}_2$ under the premise that the cost of moving a Dirac point mass from $\bm\xi_1$ to $\bm\xi_2$ amounts to $\|\bm{\xi}_1 - \bm{\xi}_2\|$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Wasserstein ambiguity set $\mathcal{F}(\theta)$ is then defined as a ball of radius $\theta\ge 0$ with respect to the Wasserstein distance, centered at a prescribed reference distribution$\hat{\mathbb{P}}$: $$\mathcal{F}(\theta) = \{\mathbb{P} \in \mathcal{P}(\mathbb{R}^K) \mid d_{\rm W}(\mathbb{P}, \hat{\mathbb{P}}) \leq \theta\}.$$ One can think of the Wasserstein radius $\theta$ as a budget on the transportation cost. Indeed, any member distribution in $\mathcal{F}(\theta)$ can be obtained by rearranging the reference distribution $\hat{\mathbb{P}}$ at a transportation cost of at most $\theta$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

If only a finite training dataset $\{\bmh{\xi}_i\}_{i \in [N]}$ is available, a natural choice for $\hat{\mathbb{P}}$ is the empirical distribution $\hat{\mathbb{P}} = \frac{1}{N}\sum_{i = 1}^N \delta_{\bmh{\xi}_i}$, which represents the uniform distribution on the training samples. Throughout the paper, we will assume that $\hat{\mathbb{P}}$is the empirical distribution.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

While it has been recognized early on that Wasserstein ambiguity sets offer many conceptual advantages (e.g., their member distributions do not need to be absolutely continuous with respect to $\hat{\mathbb{P}}$ and, if properly calibrated, they constitute confidence regions for the unknown true data-generating distribution), it was believed that they almost invariably lead to hard global optimization problems. Recently, [Esfahani\_Kuhn\_2017] and [Zhao\_Guan\_2018] discovered that many interesting distributionally robust optimization problems over Wasserstein ambiguity sets can actually be reformulated as tractable convex programsprovided that $\hat{\mathbb{P}}$ is discrete and that the problem's objective function satisfies certain convexity properties. These reformulations have subsequently been generalized to Polish spaces and non-discrete reference distributions by [blanchet2019quantifying] and [Gao\_Kleywegt\_2016].

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since then, distributionally robust optimization models over Wasserstein ambiguity sets have been proposed for many applications, including transportation (carlsson2018wasserstein) and machine learning (blanchet2019robust, gao2017distributional, shafieezadeh2019regularization and sinha2017certifiable).

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we study distributionally robust chance constrained programs of the form $$\begin{array}{cll} \displaystyle \min_{\bm{x} \in \mathcal{X}} &~\bm{c}^\top\bm{x} \\{\rm s.t.} &~\displaystyle \mathbb{P}[\bmt{\xi} \in \mathcal{S}(\bm{x})] \geq 1-\varepsilon &~\forall \mathbb{P} \in \mathcal{F}(\theta), where the goal is to find a decision $\bm{x}$ from within a compact polyhedron $\mathcal{X} \subseteq \mathbb{R}^L$ that minimizes a linear cost function $\bm{c}^\top\bm{x}$ and ensures that the exogenous random vector $\bmt{\xi}$ falls within a decision-dependent safety set $\mathcal{S}(\bm{x})

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

\subseteq \mathbb{R}^K$ with high probability $1-\varepsilon$ under every distribution $\mathbb{P} \in \mathcal{F}(\theta)$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Since the reference distribution $\hat{\mathbb{P}}$ in[prob:cc general] is the empirical distribution over the training dataset $\{\bmh{\xi}_i\}_{i \in [N]}$, we refer to[prob:cc general] as a data-drivenchance constrained program.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

To date, the literature on data-driven chance constraints has focused primarily on variants of problem [prob:cc general] where the Wasserstein ambiguity set $\mathcal{F} (\theta)$ is replaced with an ambiguity set $\mathcal{G} (\theta)$ that contains all distributions close to the empirical distribution $\hat{\mathbb{P}}$ with respect to a $\phi$-divergence (such as the Kullback-Leibler divergence or the $\chi^2$-distance): $$\mathcal{G}(\theta) = \bigg\{\mathbb{P} \in \mathcal{P}(\mathbb{R}^K) ~\bigg|~\mathbb{P}\ll \hat{\mathbb{P}}, \;\; \int_{\mathbb{R}^K} \phi\bigg(\dfrac{{\rm d}\mathbb{P}(\bm{\xi})}{{\rm

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

[Hu\_Hong\_2013] show that a distributionally robust chance constrained program over a Kullback-Leibler ambiguity set reduces to a classical chance constrained progam over the reference distribution $\hat{\mathbb{P}}$ and an adjusted risk threshold $\varepsilon' < \varepsilon$. While this result holds for any reference distribution, $\phi$-divergence ambiguity sets only contain distributions that are absolutely continuous with respect to $\hat{\mathbb{P}}$, that is, any distribution in $\mathcal{G} (\theta)$ only assigns positive probability to those measurable subsets $A \subseteq \mathbb{R}^K$ for which $\hat{\mathbb{P}} [\tilde{\bm{\xi}} \in A] > 0$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

This is undesirable for problems with a large dimension $K$ and/or few training data, where it is unlikely that every possible value of $\tilde{\bm{\xi}}$ has been observed in $\{\bmh{\xi}_i\}_{i \in [N]}$. This shortcoming is addressed by [Jiang\_Guan\_2016, jiang2018risk], who replace the reference distribution with a Kernel density estimator.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite their tremendous success and widespread adoption in recent years, the use of $\phi$-divergences can lead to undesirable side effects in some applications: they compare distributions on a scenario-by-scenario" basis and thus do not consider the possibility of noisy measurements [Gao\_Kleywegt\_2016], and they generically fail to be probability metrics as they typically violate symmetry as well as the triangle inequality. Moreover, as we show next, $\phi$-divergence ambiguity sets may be overly optimistic when only few training samples are available.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Consider the arguably simplest instance of the data-driven optimization problem[prob:cc general], which estimates the worst-case value-at-risk $\sup_{\mathbb{P} \in \mathcal{F} (\theta)} \, \mathbb{P}\text{-VaR}_\varepsilon (\tilde{\xi})$ of a scalar random variable $\tilde{\xi}$ at level $\varepsilon$ from a limited set of i.i.d.training samples $\{ \hat{\xi}_i \}_{i = 1}^N$ of $\tilde{\xi}$ under the unknown data-generating distribution $\mathbb{P}_0$ that are summarized by the empirical distribution $\hat{\mathbb{P}} = \frac{1}{N}\sum_{i = 1}^N \delta_{\hat{\xi}_i}$ at the centre of the Wasserstein ball $\mathcal{F} (\theta)$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

To avoid technicalities, we assume that $\mathbb{P}_0$ is atomless.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

reliability of the aforementioned worst-case value-at-risk, that is, the probability that it weakly exceeds the unknown true value-at-risk $\mathbb{P}_0\text{-VaR}_\varepsilon (\tilde{\xi})$, can be bounded from below by \mathbb{P}_0^N \left[\sup_{\mathbb{P} \in \mathcal{F} (\theta)} \, \mathbb{P}\text{-VaR}_\varepsilon (\tilde{\xi}) \; \geq \; \mathbb{P}_0\text{-VaR}_{\varepsilon} (\tilde{\xi}) \right] \mathbb{P}^N_0 \left[\mathbb{P}^\dag\text{-VaR}_\varepsilon (\tilde{\xi}) \; \geq \; \mathbb{P}_0\text{-VaR}_\varepsilon

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

The first inequality holds since $\mathbb{P}^\dag$ is contained in $\mathcal{F} (\theta)$. The first equality holds since $\mathbb{P}^\dag\text{-VaR}_\varepsilon (\tilde{\xi}) = \hat{\mathbb{P}}\text{-VaR}_\varepsilon (\tilde{\xi}) + \theta / \varepsilon$ by construction of $\mathbb{P}^\dag$, and the last inequality is due to a standard concentration inequality for empirical quantiles (see, e.g., Theorem2.3.2 of serfling2009approximation).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

If we replace the Wasserstein ambiguity set $\mathcal{F} (\theta)$ with the ambiguity $\mathcal{G} (\theta)$ of any $\phi$-divergence, on the other hand, then we can bound the reliability from above by \mathbb{P}_0^N \left[\sup_{\mathbb{P} \in \mathcal{G} (\theta)} \, \mathbb{P}\text{-VaR}_\varepsilon (\tilde{\xi}) \; \geq \; \mathbb{P}_0\text{-VaR}_{\varepsilon} (\tilde{\xi}) \right] 1 - \mathbb{P}^N_0 \left[\sup_{\mathbb{P} \in \mathcal{G} (\theta)} \, \mathbb{P}\text{-VaR}_\varepsilon (\tilde{\xi}) \; < \;

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

\mathbb{P}_0\text{-VaR}_{\varepsilon} (\tilde{\xi}) \right] \\1 - \mathbb{P}^N_0 \left[\hat{\xi}_1, \hat{\xi}_2, \ldots, \hat{\xi}_N \; < \; \mathbb{P}_0\text{-VaR}_{\varepsilon} (\tilde{\xi}) \right] \\Here, the first inequality holds since all distributions in $\mathcal{G} (\theta)$ share a common support with $\hat{\mathbb{P}}$, and the second inequality follows from the definition of $\mathbb{P}_0\text{-VaR}_{\varepsilon} (\tilde{\xi})$. We highlight that this probability bound holds for every radius $\theta$ of the $\phi$-divergence ball $\mathcal{G} (\theta)$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

Reliability bounds for the Wasserstein (worst-case) and $\phi$-divergence (best-case) ambiguity sets when approximating the VaR at level $\varepsilon = 0.1$ (left), $\varepsilon =0.05$ (middle) and $\varepsilon =0.01$ (right). We choose the radius $\theta = 1/\sqrt{N}$ for the Wassestein ball (see, e.g., Esfahani\_Kuhn\_2017). [fig:bound] compares the worst-case reliability offered by the Wasserstein ambiguity set with the best-case reliability of the $\phi$-divergence ambiguity set for a uniform distribution over the interval$$. We observe that in low-sample regimes, $\phi$-divergence ambiguity sets may underestimate the true VaR with high probability.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Introduction", "weight": 1.5} -->

To our best knowledge, the paper of [xie2020bicriteria] is the only previous work on data-driven chance constraints over Wasserstein ambiguity sets. The authors study the special class of covering problems, where the feasible region $\mathcal{X}$ satisfies $\eta \mathcal{X} \subseteq \mathcal{X}$ for every $\eta \geq 1$. This problem class encompasses, among others, portfolio optimization problems without budgetary restrictions and lot-sizing problems in the absence of setup costs. The authors prove that the resulting individual chance constrained program is NP-hard. They also demonstrate that two popular approximation schemes, the CVaR approximation as well as the scenario approximation, can perform arbitrarily poorly for classical individual chance constraints, that is, when the Wasserstein radius is $\theta = 0$. Based on this insight, the authors propose a bicriteria approximation scheme for covering problems with classical as well as distributionally robust individual chance constraints over moment and Wasserstein ambiguity sets.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Introduction", "weight": 1.5} -->

This bicriteria approximation scheme determines solutions that trade off a higher risk threshold $\varepsilon' > \varepsilon$ in the chance constraint with a smaller optimality gap $\varepsilon' / (\varepsilon' - \varepsilon)$. This is achieved by solving a tractable convex relaxation of the chance constrained problem (using, e.g., a Markovian or Bernstein generator) and subsequently scaling the solution to this relaxation so that it becomes feasible for the chance constraint with the higher risk threshold $\varepsilon'$. By design, the performance guarantee of the bicriteria approximation scheme becomes weaker (and eventually trivial) as the selected risk threshold $\varepsilon'$ approaches the risk threshold $\varepsilon$ of the original problem formulation.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we study distributionally robust chance constrained programs over the Wasserstein ambiguity set [set:Wasserstein].

<!-- chunk {"id": "body-0026", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our reformulations are mixed-integer conic programs that reduce to mixed-integer linear programs when the norm $\left \lVert \cdot \right \rVert$ on $\mathbb{R}^K$ is the $1$-norm or the $\infty$-norm.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Introduction", "weight": 1.5} -->

While preparing this paper for publication, we became aware of the independent work by [xie2019distributionally], which derives similar reformulations for distributionally individual and joint chance constraints over Wasserstein ambiguity sets. In contrast to our work, however, [xie2019distributionally] assumes that each safety condition $\bm{a}_m^\top \bm{x} < b_m (\bm{\xi})$, $m \in [M]$, in the joint chance constraint depends on a subvector of $\bm{\xi}$, and that these subvectors are pairwise disjoint for different safety conditions. In other words, different safety conditions of the joint chance constraints studied by [xie2019distributionally] must depend on different random variables. Furthermore, the reformulations of [xie2019distributionally] are derived via duality theory, whereas our reformulations directly leverage the structural insights into the worst-case distributions.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Introduction", "weight": 1.5} -->

This enables us to keep our reformulations largely independent of the selected ground metric for the Wasserstein ball, which opens up possibilities to incorporate other cost functions in our definition of the Wasserstein distance. Since the initial submission of this paper, our exact reformulation for data-driven chance constrained program over Wasserstein balls has been further studied and tightened; see, for instance, [ho2020strong, ho2021distributionally], [shen2021convex] and [zhang2021building]. Along with these theoretical extensions, our reformulation has also been applied in several domains, including risk sharing in finance [chen2021sharing], network design for humanitarian operations [jiang2021distributionally] and optimal power flows in energy systems [arrigo2022wasserstein].

<!-- chunk {"id": "body-0029", "role": "body", "section": "Exact Reformulation of Data-Driven Chance Constraints", "weight": 1.0} -->

[sec:uq\_wasserstein] reviews a previously established result on the quantification of uncertainty over Wasserstein balls. We use this result to derive an exact reformulation of generic data-driven chance constrained programs in Section[sec:ref\_generic]. We finally specialize this generic reformulation to the subclasses of data-driven individual chance constrained programs as well as data-driven joint chance constrained programs with right-hand side uncertainty in Sections[sec:ref\_indiv\_cc] and[sec:ref\_joint\_cc], respectively.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Uncertainty Quantification over Wasserstein Balls", "weight": 1.0} -->

Consider an open safety set $\mathcal{S} \subseteq \mathbb{R}^K $, and denote by $\bar{\mathcal{S}} = \mathbb{R}^K \setminus \mathcal{S}$ its closed complement. The uncertainty quantification problem $$\sup_{\mathbb{P} \in \mathcal{F}(\theta)} \mathbb{P}[\bmt{\xi} \notin \mathcal{S}]$$ computes the worst (largest) probability of the system under consideration being unsafe, which is the case whenever the random vector $\bmt{\xi}$ attains a value in the unsafe set $\bar{\mathcal{S}}$. Throughout the rest of the paper, we exclude trivial special cases and assume that $\theta > 0$ and $\varepsilon \in $.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Uncertainty Quantification over Wasserstein Balls", "weight": 1.0} -->

To solve the uncertainty quantification problem [prob:uncertainty quantification], denote by $\mathbf{dist}(\bmh{\xi}_i, \bar{\mathcal{S}})$ the distance of the $i^\text{th}$ data point $\bmh{\xi}_i \in \mathbb{R}^K$ of the empirical distribution $\hat{\mathbb{P}}$ to the unsafe set $\bar{\mathcal{S}}$. This distance is based on a norm $\left \lVert \cdot \right \rVert$, which we keep generic at this stage.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Uncertainty Quantification over Wasserstein Balls", "weight": 1.0} -->

[blanchet2019quantifying] as well as [Gao\_Kleywegt\_2016] have characterized the solution to the uncertainty quantification problem[prob:uncertainty quantification] in closed form. To keep our paper self-contained, we reproduce their findings without proof in Theorem[thm:uncertainty-quantification]below.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Uncertainty Quantification over Wasserstein Balls", "weight": 1.0} -->

Intuitively speaking, the worst-case distribution $\mathbb{P}^\star$ in Theorem[thm:uncertainty-quantification] transports the training dataset $\{\bmh{\xi}_i\}_{i \in [N]}$ to the unsafe set $\bar{\mathcal{S}}$ in a greedy fashion, see Figure[fig:greedy]. The data points $\bmh{\xi}_1,\dots,\bmh{\xi}_I$ are already unsafe and hence do not need to be transported. The subsequent data points $\bmh{\xi}_{I+1}, \ldots, \bmh{\xi}_{j^\star + 1}$ are closest to the unsafe set and are thus transported from $\mathcal{S}$ to $\bar{\mathcal{S}}$. Due to the limited transportation budget $\theta$, the data point $\bmh{\xi}_{j^\star + 1}$ is only partially transported.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Uncertainty Quantification over Wasserstein Balls", "weight": 1.0} -->

The safe samples $\bmh{\xi}_{j^\star + 2}, \ldots \bmh{\xi}_N$, finally, are too far away from the unsafe set $\bar{\mathcal{S}}$ and are thus left unchanged. Note that the distribution characterized in Theorem[thm:uncertainty-quantification] may not be the only distribution that solves problem[prob:uncertainty quantification].

<!-- chunk {"id": "body-0035", "role": "body", "section": "Uncertainty Quantification over Wasserstein Balls", "weight": 1.0} -->

Empirical and worst-case distributions. The left graph visualizes the empirical distribution $\hat{\mathbb{P}}$, whose light grey (dark grey) data points are contained in (outside of) the safety set $\mathcal{S}$ shown as an equilateral triangle (dashed lines). The right graph shows the corresponding worst-case distribution $\mathbb{P}^\star$, which moves the data points $\bmh{\xi}_1$ and $\bmh{\xi}_2$ entirely as well as the data point $\bmh{\xi}_3$ partially to the unsafe set $\bar{\mathcal{S}}$. Each transported data point is projected onto the boundary of the closest halfspace defining the safety set $\mathcal{S}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

We now develop deterministic reformulations for the distributionally robust chance constrained program [prob:cc general]. To this end, we focus on the ambiguous chance constraint $$\sup_{\mathbb{P} \in \mathcal{F}(\theta)} \mathbb{P}[\bmt{\xi} \notin \mathcal{S}(\bm{x})] \leq \varepsilon.$$ For any fixed decision $\bm x\in \mathcal{X}$, we let $\mathcal{S}(\bm{x})$ be an arbitrary open safety set, and we denote by $\bar{\mathcal{S}}(\bm{x})$ its closed complement, which comprises all unsafe scenarios.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

\bar{\mathcal{S}}(\bm{x})).$$ We first show that a fixed decision $\bm{x}$ satisfies the ambiguous chance constraint[prob:worst-case cc] over the Wasserstein ambiguity set[set:Wasserstein] if and only if the partial sum of the $\varepsilon N$ smallest transportation distances to the unsafe set multiplied by the mass $1/N$ of a training sample exceeds$\theta$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

For any fixed decision $\bm{x}\in \mathcal{X}$, the ambiguous chance constraint[prob:worst-case cc] over the Wasserstein ambiguity set[set:Wasserstein] is equivalent to the deterministic inequality $$\dfrac{1}{N}\sum_{i = 1}^{\varepsilon N} \mathbf{dist}(\bmh{\xi}_{\pi_i(\bm{x})}, \bar{\mathcal{S}}(\bm{x})) \ge \theta.$$ The left-hand side of [equivalence:theta positive] can be interpreted as the minimum cost of moving a fraction $\varepsilon$ of the training samples to the unsafe set. If this cost exceeds the prescribed transportation budget $\theta$, then no distribution in the Wasserstein ambiguity set can assign the unsafe set a probability of more than $\varepsilon$, which means that the distributionally robust chance constraint[prob:worst-case cc]is satisfied.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

Indeed, the solution $(j, p) = (j^\star, p^\star)$ is feasible in[eq:bivariate\_mixed\_integer] by definition of $j^\star$ and $p^\star$. Moreover, we have $j + p < j^\star + p^\star$ for any other feasible solution $(j, p)$ that satisfies $j = j^\star$ and $p \neq p^\star$. Assume now that the optimal solution $(j, p)$ to[eq:bivariate\_mixed\_integer] would satisfy $j > j^\star$. Any such solution would violate the first constraint since $\sum_{i = 1}^j \mathbf{dist}(\bmh{\xi}_{\pi_i (\bm{x})}, \bar{\mathcal{S}} (\bm{x})) > \theta N$ by definition of $j^\star$ while $p \geq 0$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

Similarly, any solution $(j, p)$ with $j < j^\star$ cannot be optimal in[eq:bivariate\_mixed\_integer] since $j \leq j^\star - 1$ while $p < p^\star + 1$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

We can re-express problem [eq:bivariate\_mixed\_integer] as the univariate discrete optimization problem $$\max \bigg\{ j \in [0, N] ~\bigg|~ \sum_{i = 1}^{\lfloor j \rfloor} \mathbf{dist}(\bmh{\xi}_{\pi_i (\bm{x})}, \bar{\mathcal{S}} (\bm{x})) \; + \; (j - \lfloor j \rfloor) \cdot \mathbf{dist}(\bmh{\xi}_{\pi_{\lfloor j \rfloor + 1} (\bm{x})}, \bar{\mathcal{S}} (\bm{x})) \leq \theta N \bigg\}.$$ Using our definition of partial sums, we observe that this problem is equivalent to $$\max \bigg\{ j \in [0, N]

<!-- chunk {"id": "body-0042", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

It therefore affords the right inverse $\vartheta^{-1} (t) = \max \{ j \in [0, N] \mid \vartheta(j) \leq t \}$ that satisfies $\vartheta \circ \vartheta^{-1} (t) = t$ for all $t \in [0, \vartheta(N)]$. Figure[fig:inverse\_function] visualizes the relationship between $\vartheta$ and $\vartheta^{-1}$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

We thus conclude that the ambiguous chance constraint[prob:worst-case cc] is satisfied if and only if \max \bigg\{ j \in [0, N] ~\bigg|~ \sum_{i = 1}^j \mathbf{dist}(\bmh{\xi}_{\pi_i (\bm{x})}, \bar{\mathcal{S}} (\bm{x})) \leq \theta N \bigg\} \leq \varepsilon N \quad &\Longleftrightarrow \quad \max \{ j \in [0, N] ~|~ \vartheta (j) \leq \theta N \} \leq \varepsilon N \\&\Longleftrightarrow \quad \vartheta^{-1} (\theta N) \leq \varepsilon N \\&\Longleftrightarrow \quad \theta N \leq \vartheta (\varepsilon N), where the last equivalence follows from $\vartheta

<!-- chunk {"id": "body-0044", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

\circ \vartheta^{-1} (\theta N) = \theta N$, which holds because $\theta N \leq \vartheta(N)$ for $j^\star < N$, as well as the fact that $\vartheta$ is monotonically nondecreasing. By definition, the right-hand side of the last equivalence holds if and only if[equivalence:theta positive] in the statement of the theorem is satisfied.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

Relationship between $\vartheta$ and $\vartheta^{-1}$. The left graph shows a feasible solution $\bm{x}$ satisfying the ambiguous chance constraintprob:worst-case cc; in this case, we have $\vartheta (\varepsilon N) \geq \theta N$. The infeasible solution $\bm{x}'$ in the right graph, on the other hand, violates the ambiguous chance constraintprob:worst-case cc, and we have $\vartheta (\varepsilon N) < \theta N$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

We emphasize that the inequality[equivalence:theta positive] fails to be equivalent to the ambiguous chance constraint[prob:worst-case cc] when $\theta = 0$, in which case the Wasserstein ball collapses to the singleton set $\mathcal{F} = \{\hat{\mathbb{P}}\}$. To see this, suppose that $\bmh{\xi}_{\pi_i(\bm{x})} \in \bar{\mathcal{S}}(\bm{x})$ for all $i=1,\ldots,I$ and $\bmh{\xi}_{\pi_i(\bm{x})} \in \mathcal{S}(\bm{x})$ for all $i=I+1,\ldots,N$, where $I\ge 1$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

If $\varepsilon < I/N$, then the chance constraint[prob:worst-case cc] is violated because $$\hat{\mathbb{P}}[\bmt{\xi} \notin \mathcal{S}(\bm{x})] = \frac{I}{N}>\varepsilon,$$ while the inequality[equivalence:theta positive] holds trivially because $\sum_{i = 1}^{\varepsilon N} \mathbf{dist}(\bmh{\xi}_{\pi_i(\bm{x})}, \bar{\mathcal{S}}(\bm{x})) \ge 0$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

[thm:cc equivalent] establishes that a decision $\bm{x} \in \mathcal{X}$ satisfies the ambiguous chance constraint[prob:worst-case cc] if and only if the sum of the $\varepsilon N$ smallest distances of the training samples to the unsafe set $\bar{\mathcal{S}}(\bm{x})$ weakly exceeds $\theta N$. This result is of computational interest because the sum of the $\varepsilon N$ smallest out of $N$ real numbers is concave in those real numbers (while being convex in $\varepsilon$). This reveals that the constraint[equivalence:theta positive] is convex in the decision-dependent distances $\{\mathbf{dist}(\bmh{\xi}_{i}, \bar{\mathcal{S}}(\bm{x}))\}_{i \in [N]}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

In the remainder we develop an efficient reformulation of this convex constraint that does not require an enumeration of all possible sums of $\varepsilon N$different distances between the training samples and the unsafe set. This reformulation is based on the following auxiliary lemma.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

For any $\varepsilon \in $, the sum of the $\varepsilon N$ smallest out of $N$ real numbers $k_1,\dots,k_N$ coincides with the optimal value of the linear program $$\begin{array}{cll} \displaystyle \max_{\bm{s}, t} & \varepsilon N t - \bm{e}^\top\bm{s} \\Proof of Lemmalem:sum of smallest.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

$\;$ By definition, the sum of the $\varepsilon N$ smallest elements of the set $\{k_1,\dots,k_N\}$ corresponds to the optimal value of the (manifestly feasible) linear program \displaystyle \min_{\bm{v}} & \displaystyle \sum_{i \in [N]} k_i v_i \\ \text{s.t.} & \bm{0} \leq \bm{v} \leq \bm{e}, ~\bm{e}^\top\bm{v} = \varepsilon N.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

The claim now follows from strong linear programming duality.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

Armed with Theorem [thm:cc equivalent] and Lemma[lem:sum of smallest], we are now ready to reformulate the chance constrained program[prob:cc general]as a deterministic optimization problem.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

The chance constrained program[prob:cc general] is equivalent to $$\begin{array}{cll} \displaystyle \min_{\bm{s}, t, \bm{x}} & \bm{c}^\top\bm{x} \\{\rm s.t.} & \varepsilon N t - \bm{e}^\top\bm{s} \geq \theta N \\& \mathbf{dist}(\bmh{\xi}_i, \bar{\mathcal{S}}(\bm{x})) \geq t - s_i &~\forall i \in [N] \\Proof of Theoremthm:cc-deterministic.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

$\;$ The claim follows immediately by using Theorem[thm:cc equivalent] to reformulate the chance constraint[prob:worst-case cc] as the inequality[equivalence:theta positive], using Lemma[lem:sum of smallest] to express the left-hand side of[equivalence:theta positive] as a linear maximization problem and substituting the resulting constraint back into[prob:cc general].

<!-- chunk {"id": "body-0056", "role": "body", "section": "Reformulation of Generic Chance Constraints", "weight": 1.0} -->

We emphasize that the reformulation offered by Theorem [thm:cc-deterministic] is independent of the selected ground metric $\mathbf{dist} (\cdot, \cdot)$. In the remainder, we assume that the ground metric is based on a norm $\lVert \cdot \rVert$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Reformulation of Individual Chance Constraints", "weight": 1.0} -->

Assume now that problem [prob:cc general] accommodates an individual chance constraint defined through the safety set $\mathcal{S}(\bm{x}) = \{\bm{\xi} \in \mathbb{R}^K \mid (\bm{A}\bm{\xi} + \bm{a})^\top \bm{x} < \bm{b}^\top\bm{\xi} + b\}$. Individual chance constrained programs have been studied, among others, in network design [wang2007beta], vehicle routing [gounaris2013robust, ghosal2020distributionally] and portfolio optimization [rujeerapaiboon2016robust, dert2000optimal].

<!-- chunk {"id": "body-0058", "role": "body", "section": "Reformulation of Individual Chance Constraints", "weight": 1.0} -->

By Lemma[lem:distance to the union of closed half-spaces] in the appendix, we have $$\mathbf{dist}(\bmh{\xi}_i, \bar{\mathcal{S}}(\bm x)) = \dfrac{((\bm{b} - \bm{A}^\top\bm{x})^\top\bmh{\xi}_i + b - \bm{a}^\top\bm{x})^+}{\|\bm{b} - \bm{A}^\top\bm{x}\|_*} ~~\forall i \in [N],$$ where we adopt the convention that $0 / 0 = 0$, and thus Theorem[thm:cc-deterministic] allows us to reformulate problem[prob:cc reformulation] as the deterministic optimization problem $$\begin{array}{cll} \displaystyle \min_{\bm{s}, t, \bm{x}} &

<!-- chunk {"id": "body-0059", "role": "body", "section": "Reformulation of Individual Chance Constraints", "weight": 1.0} -->

\bm{c}^\top\bm{x} \\{\rm s.t.} & \varepsilon N t - \bm{e}^\top\bm{s} \geq \theta N \\& \dfrac{((\bm{b} - \bm{A}^\top\bm{x})^\top\bmh{\xi}_i + b - \bm{a}^\top\bm{x})^+}{\|\bm{b} - \bm{A}^\top\bm{x}\|_*} \geq t - s_i &~\forall i \in [N] \\Unfortunately, problem[prob:individual cc reformulation] fails to be convex as its constraints involve fractions of convex functions. Below we show, however, that problem[prob:individual cc reformulation] can be reformulated as a mixed integer conic program.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Reformulation of Individual Chance Constraints", "weight": 1.0} -->

Proof of Propositionprop:individual cc. $\;$ We already know that the chance constrained program[prob:cc general] is equivalent to the non-convex optimization problem[prob:individual cc reformulation]. A complicating feature of this problem is the appearance of the maximum operator in the second constraint group, which evaluates the positive part of $(\bm{b} - \bm{A}^\top\bm{x})^\top\bmh{\xi}_i + b - \bm{a}^\top\bm{x}$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Reformulation of Individual Chance Constraints", "weight": 1.0} -->

Intuitively, $q_i$ thus activates the less restrictive one of the two auxiliary constraints in[eq:big-M]. Next, we apply the variable substitutions $t\leftarrow t/\|\bm{b} - \bm{A}^\top\bm{x}\|_*$ and $\bm{s}\leftarrow \bm{s}/\|\bm{b} - \bm{A}^\top\bm{x}\|_*$, which is admissible because $\bm{A}^\top\bm{x} \ne \bm{b}$ for all $\bm{x} \in \mathcal{X}$. This change of variables yields the postulated reformulation[prob:individual cc reformulation linearization].

<!-- chunk {"id": "body-0062", "role": "body", "section": "Reformulation of Individual Chance Constraints", "weight": 1.0} -->

To see that a finite value of $\rm M$ is sufficient for our reformulation to be exact, we show that the expression $((\bm{b} - \bm{A}^\top\bm{x})^\top\bmh{\xi}_i + b - \bm{a}^\top\bm{x}) / \|\bm{b} - \bm{A}^\top\bm{x}\|_*$ as well as the values of $t$ and $s_i$, $i \in [N]$, in[eq:big-M] can all be bounded without affecting the optimal value of problem[prob:individual cc reformulation linearization]. This is clear for the fraction as $\mathcal{X}$ is compact and the denominator is non-zero for all $\bm{x} \in \mathcal{X}$. Moreover, $t$ is nonnegative as otherwise the first constraint in[prob:individual cc reformulation linearization] would be violated.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Reformulation of Individual Chance Constraints", "weight": 1.0} -->

Indeed, for sufficiently large (but finite) $t$, the slope of $\varepsilon N t - \bm{e}^\top \bm{s}^\star (\bm{x}, t)$ on the left-hand side of the first constraint in[prob:individual cc reformulation linearization] is $- (1 - \varepsilon) N$. Since $\varepsilon < 1$, we thus conclude that this constraint is violated for large values of $t$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Reformulation of Individual Chance Constraints", "weight": 1.0} -->

The condition that $\bm{A}^\top\bm{x} \ne \bm{b}$ for all $\bm{x} \in \mathcal{X}$ does not restrict the generality of our formulation. Indeed, if an optimal solution $(\bm{q}^\star, \bm{s}^\star, t^\star, \bm{x}^\star)$ to problem[prob:individual cc reformulation linearization] satisfies $\bm{A}^\top\bm{x}^\star \ne \bm{b}$, then $\bm{x}^\star$ solves problem[prob:cc general] since our argument in the proof of Proposition[prop:individual cc] applies to $\bm{x}^\star$ even if $\bm{A}^\top\bm{x} = \bm{b}$ for some $\bm{x} \in \mathcal{X}$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Reformulation of Individual Chance Constraints", "weight": 1.0} -->

Assume now that an optimal solution $(\bm{q}^\star, \bm{s}^\star, t^\star, \bm{x}^\star)$ to problem[prob:individual cc reformulation linearization] satisfies $\bm{A}^\top\bm{x}^\star = \bm{b}$. In that case, the ambiguous chance constraint in problem[prob:cc general] requires that $\bm{a}^\top \bm{x}^\star < b$. If that is the case for $\bm{x}^\star$, it is optimal in problem[prob:cc general].

<!-- chunk {"id": "body-0066", "role": "body", "section": "Reformulation of Individual Chance Constraints", "weight": 1.0} -->

If, finally, an optimal solution $(\bm{q}^\star, \bm{s}^\star, t^\star, \bm{x}^\star)$ to problem[prob:individual cc reformulation linearization] satisfies $\bm{A}^\top\bm{x}^\star = \bm{b}$ and $\bm{a}^\top \bm{x}^\star \geq b$, then one would ideally like to solve a variant of problem[prob:individual cc reformulation linearization] that includes the additional constraint $$\bm{A}^\top \bm{x} \neq \bm{b} \quad \text{or} \quad \bm{a}^\top \bm{x} < b.$$ This variant of problem[prob:individual cc reformulation linearization] can be solved by solving $2 K + 1$ versions of problem[prob:individual cc reformulation linearization], where each version includes exactly one of the constraints

<!-- chunk {"id": "body-0067", "role": "body", "section": "Reformulation of Individual Chance Constraints", "weight": 1.0} -->

One readily verifies that the solution that attains the least objective value amongst these $2K + 1$ versions of problem[prob:individual cc reformulation linearization] is an optimal solution to problem[prob:individual cc reformulation linearization] with the added constraint[rem2\_constraint].

<!-- chunk {"id": "body-0068", "role": "body", "section": "Reformulation of Individual Chance Constraints", "weight": 1.0} -->

The mixed-integer conic program[prob:individual cc reformulation linearization] simplifies to a mixed-integer linear program whenever $\|\cdot\|$ represents the $1$-norm or the $\infty$-norm, and it can be reformulated as a mixed-integer second-order cone program whenever $\|\cdot\|$ represents a $p$-norm for some $p \in \mathbb{Q}$, $p>1$, see Section2.3.1 in [Ben-tal\_Nemirovski\_book].

<!-- chunk {"id": "body-0069", "role": "body", "section": "Reformulation of Individual Chance Constraints", "weight": 1.0} -->

The deterministic reformulation[prob:individual cc reformulation linearization] is remarkably parsimonious. For an $L$-dimensional feasible region $\mathcal{X} \subseteq \mathbb{R}^L$ and an empirical distribution $\hat{\mathbb{P}}$ with $N$ data points, our reformulation[prob:individual cc reformulation linearization] has $N$ binary variables, $L + N + 1$ continuous decisions as well as $2N + 1$ constraints (excluding those that describe $\mathcal{X}$). In comparison, a classical chance constrained formulation, which is tantamount to setting the Wasserstein radius to $\theta = 0$ in problem[prob:cc general], has $N$ binary variables, $L$ continuous decisions as well as $N + 1$ constraints. Thus, adding distributional robustness only requires an additional $N + 1$ continuous decisions as well as $N$ further constraints.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Reformulation of Individual Chance Constraints", "weight": 1.0} -->

The deterministic reformulation[prob:individual cc reformulation linearization] requires the specification of a sufficiently large constant $\mathrm{M}$, which can typically be determined by an investigation of the structure of problem[prob:individual cc reformulation linearization].

<!-- chunk {"id": "body-0071", "role": "body", "section": "Reformulation of Individual Chance Constraints", "weight": 1.0} -->

Alternatively, many commercial solver packages allow to directly specify the following reformulation of problem[prob:individual cc reformulation linearization] via the use of piecewise linear constraints: $$\begin{array}{rcll} Z^\star_{\rm ICC} =& \displaystyle \min_{\bm{q}, \bm{s}, t, \bm{x}} & \bm{c}^\top\bm{x} \\&{\rm s.t.} & \varepsilon N t - \bm{e}^\top\bm{s} \geq \theta N \|\bm{b} - \bm{A}^\top\bm{x}\|_* \\&& ((\bm{b} - \bm{A}^\top\bm{x})^\top\bmh{\xi}_i + b - \bm{a}^\top\bm{x})^+ \geq t - s_i &~\forall i \in

<!-- chunk {"id": "body-0072", "role": "body", "section": "Reformulation of Individual Chance Constraints", "weight": 1.0} -->

[N] \\This formulation has the advantage that it does not require the specification of the constant $\mathrm{M}$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Reformulation of Joint Chance Constraints with Right-Hand Side Uncertainty", "weight": 1.0} -->

Assume next that problem [prob:cc general] accommodates a joint chance constraint defined through the safety set $\mathcal{S}(\bm{x}) = \{\bm{\xi} \in \mathbb{R}^K \mid \bm{a}^\top_m \bm{x} < \bm{b}^\top_m\bm{\xi} + b_m ~\forall m \in [M]\}$, in which the uncertainty affects only the right-hand sides of the safety conditions. Without loss of generality, we may assume that $\bm{b}_m \ne \bm{0}$ for all $m \in [M]$. Indeed, if $\bm{b}_m = \bm{0}$, then the $m^{\rm th}$ safety condition in the chance constraint becomes independent of the uncertainty and can thus be absorbed in $\mathcal{X}$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Reformulation of Joint Chance Constraints with Right-Hand Side Uncertainty", "weight": 1.0} -->

Joint chance constrained programs with right-hand side uncertainty have been proposed, among others, for problems in transportation [luedtke2010], lot-sizing [beraldi2002branch, kuccukyavuz2012mixing], unit commitment [yanagisawa\_2013] and project management [wiesemann2012multi].

<!-- chunk {"id": "body-0075", "role": "body", "section": "Reformulation of Joint Chance Constraints with Right-Hand Side Uncertainty", "weight": 1.0} -->

Proof of Propositionprop:joint cc. $\;$ By Theorem[thm:cc-deterministic], the chance constrained program[prob:cc general] is equivalent to[prob:cc reformulation].

<!-- chunk {"id": "body-0076", "role": "body", "section": "Reformulation of Joint Chance Constraints with Right-Hand Side Uncertainty", "weight": 1.0} -->

M} q_i \geq t - s_i &~\forall m \in [M]\\A similar argument as in the proof of Proposition[prop:individual cc] shows that a finite value of $\rm M$ is sufficient for our reformulation to be exact.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Reformulation of Joint Chance Constraints with Right-Hand Side Uncertainty", "weight": 1.0} -->

[rem:piecewise\_linear] in the previous section, many commercial solvers allow to directly specify a reformulation of problem[prob:joint cc reformulation M linearization] that replaces the constant $\mathrm{M}$with piecewise linear constraints.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Reformulation of Joint Chance Constraints with Right-Hand Side Uncertainty", "weight": 1.0} -->

The deterministic reformulation[prob:joint cc reformulation M linearization] has $N$ binary variables, $L + N + 1$ continuous decisions as well as $(M + 1) N + 1$ constraints (excluding those that describe $\mathcal{X}$). In comparison, the corresponding classical chance constrained formulation has $N$ binary variables, $L$ continuous decisions as well as $MN + 1$ constraints. Thus, adding distributional robustness requires an additional $N + 1$ continuous decisions as well as $N$ further (linear) constraints.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We compare our exact reformulation of the ambiguous chance constrained program [prob:cc general] with the bicriteria approximation scheme of [xie2020bicriteria] on a portfolio optimization problem in Section[sec:portfolio] as well as with a classical (non-ambiguous) chance constrained formulation and a Kernel density estimator based version of the ambiguous chance constrained program over a $\phi$-divergence ambiguity set on a transportation problem in Section[sec:transportation]. Our goal is to investigate the computational scalability of our reformulation as well as its out-of-sample performance in a data-driven setting. All results were produced on an Intel Xeon 2.66GHz processor with 8GB memory in single-core mode using CPLEX 12.8. Following Remark[rem:piecewise\_linear], we avoid the specification of the constant $\mathrm{M}$in our ambiguous chance constrained program through the use of piecewise linear constraints.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Portfolio Optimization", "weight": 1.0} -->

We consider a portfolio optimization problem studied by [xie2020bicriteria]. The problem asks for the minimum-cost portfolio investment $\bm{x}$ into $K$ assets with random returns $\tilde{\xi}_1, \ldots, \tilde{\xi}_K$ that exceeds a pre-specified target return $w$ with high probability $1 - \varepsilon$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Portfolio Optimization", "weight": 1.0} -->

The problem can be cast as the following instance of the ambiguous chance constrained program[prob:cc general]: $$\begin{array}{cll} \displaystyle \min_{\bm{x}} & \bm{c}^\top\bm{x} \\{\rm s.t.} &\displaystyle \mathbb{P}[\bmt{\xi}^\top\bm{x} > w] \geq 1-\varepsilon &~\forall \mathbb{P} \in \mathcal{F}(\theta)\\We compare our exact reformulation of problem [eq:portfolio] with the $(\sigma, \gamma)$-bicriteria approximation scheme of [xie2020bicriteria], which produces solutions that satisfy the ambiguous chance constraint in[eq:portfolio] with probability $1 - \sigma \varepsilon$, $\sigma > 1$, and whose costs are guaranteed to exceed the optimal costs in[eq:portfolio] by a factor of at most $\gamma = \sigma / (\sigma -

<!-- chunk {"id": "body-0082", "role": "body", "section": "Portfolio Optimization", "weight": 1.0} -->

Since the bicriteria approximation scheme can readily utilize support information for the random vector $\bmt{\xi}$, we replace the ambiguity set $\mathcal{F}(\theta)$ with $\bar{\mathcal{F}}(\theta) = \mathcal{F}(\theta) \cap \{\mathbb{P} \mid \mathbb{P}[\bmt{\xi} \in \mathbb{R}^K_+] = 1\}$ in their approach. Contrary to the experiments conducted by [xie2020bicriteria], we set $\sigma = 1$. This is to the disadvantage of their approach, as it does not provide any approximation guarantees in that case, but it allows us to compare the resulting portfolios as they provide the same return guarantees. For the performance of the bicriteria approximation scheme with $\sigma > 1$, we refer to Section6.2 of [xie2020bicriteria].

<!-- chunk {"id": "body-0083", "role": "body", "section": "Portfolio Optimization", "weight": 1.0} -->

In our numerical experiments, we consider a similar setting as [xie2020bicriteria]. We set $K = 50$, $w = 1$ and choose the cost coefficients $c_1, \ldots, c_{50}$ uniformly at random from $\{ 1, \ldots, 100 \}$. Each asset return $\tilde{\xi}_i$ is governed by a uniform distribution on $[0.8, 1.5]$, and we assume that $N = 100$ training samples $\bmh{\xi}_1, \ldots, \bmh{\xi}_{100}$ are available. We use the $2$-norm Wasserstein ambiguity set, which implies that our exact reformulation of problem[eq:portfolio] is a mixed-integer second-order cone program, and set the Wasserstein radius to $\theta \in \{0.05, 0.1, 0.2\}$. The risk threshold is set to $\varepsilon \in \{0.05, 0.1\}$.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Portfolio Optimization", "weight": 1.0} -->

| 2*$(\varepsilon, \theta)$ | 3cRatio of objective values | 3cRatio of runtimes | | | | | Objective and runtime ratios of the bicriteria approximation scheme for different values of $\varepsilon$ and $\theta$. For each parameter setting, we report the $5\%$, $50\%$ and $95\%$ quantiles over 50 randomly generated instances.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Portfolio Optimization", "weight": 1.0} -->

Runtimes (left) and reciprocal runtime ratios (right) of our exact reformulation and the bicriteria approximation scheme for $(\varepsilon, \theta) = (0.10,0.05)$ and different sample sizes $N$. The shaded regions cover the $5\%$ to $95\%$ quantiles of $50$ randomly generated instances, whereas the solid lines describe the median statistics. [table:bicteria] compares the objective values and runtimes of our exact reformulation and the bicriteria approximation scheme for various combinations of the risk threshold $\varepsilon$ and Wasserstein radius $\theta$. The table shows that despite incorporating additional support information, the bicriteria approximation scheme determines solutions whose costs significantly exceed those of the solutions found by our exact reformulation. Perhaps more surprisingly, the bicriteria approximation scheme is also computationally more expensive.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Portfolio Optimization", "weight": 1.0} -->

As Figure[fig:runtime] shows, however, this is an artifact of the small sample size $N$ employed in the experiments of [xie2020bicriteria], and the bicriteria approximation scheme is faster than our exact reformulation for larger samples sizes.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Transportation", "weight": 1.0} -->

We consider a probabilistic transportation problem studied by [luedtke2010] and [yanagisawa\_2013]. The problem asks for the cost-optimal distribution of a single good from a set of factories $f \in [F]$ to a set of distribution centers $d \in [D]$. Each factory $f \in [F]$ has an individual production capacity $m_f$, and each distribution center $d \in [D]$ faces a random aggregate customer demand $\tilde{\xi}_d$. The cost of shipping one unit of the good from factory $f$ to distribution center $d$ is denoted by $c_{fd}$. We aim to find a transportation plan that minimizes the shipping costs, respects the production capacity of each factory and satisfies the demand at each distribution center with high probability.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Transportation", "weight": 1.0} -->

The problem can be cast as the following instance of problem[prob:cc general]: $$\begin{array}{cl@{\quad}l} \displaystyle \min_{\bm{x}} & \bm{c}^\top\bm{x} \\{\rm s.t.} & \displaystyle \mathbb{P} \Bigg[\sum_{f \in [F]} x_{fd} \geq \tilde{\xi}_d \quad \forall d \in [D] \Bigg] \geq 1 - \varepsilon &~ \forall \mathbb{P} \in \mathcal{F}(\theta) \\[5mm] & \displaystyle \sum_{d \in [D]} x_{fd} \leq m_f &~ \forall f \in [F] \\Here, $x_{fd}$ denotes the quantity shipped from factory $f \in [F]$ to distribution center $d \in [D]$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Transportation", "weight": 1.0} -->

Problem[eq:amb\_transp\_prob] is an ambiguous joint chance constrained program with right-hand side uncertainty. Since each safety condition in[eq:amb\_transp\_prob] contains a single random variable with coefficient $1$ on the right-hand side, our exact reformulation reduces to the same mixed-integer linear program for any norm $\lVert \cdot \rVert$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Transportation", "weight": 1.0} -->

In our first experiment, we investigate the scalability of the exact reformulation of problem [eq:amb\_transp\_prob] that is offered by Proposition[prop:joint cc]. To this end, we generate random test instances with $5$ factories and $10, 20, \ldots, 50$ distribution centers that are located uniformly at random on the Euclidean plane $^2$. We identify the transportation costs $c_{fd}$ with the Euclidean distances between the factories and distribution centers. The demand vector $\bmt{\xi}$ is described by $50$, $100$ or $150$ samples from a uniform distribution that is supported on $[0.8 \bm{\mu}, 1.2 \bm{\mu}]$, where the expected demand $\mu_d$ at distribution center $d \in [D]$ is picked uniformly at random from the interval $$. The capacity of each factory is chosen uniformly at random, and the capacities are subsequently scaled so that the factories can jointly produce up to $150\%$ of the maximum cumulative demand.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Transportation", "weight": 1.0} -->

For each instance, we choose $10$ ascending Wasserstein radii $\theta_1 < \ldots < \theta_{10}$ uniformly so that $\theta_1 = 0.001$ and $\theta_{10}$ is the smallest radius for which the corresponding instance of problem[eq:amb\_transp\_prob] becomes infeasible. We fix $\varepsilon = 0.1$.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Transportation", "weight": 1.0} -->

[table:scalability\_50][table:scalability\_150] and Figure[fig:case] compare the runtimes of our ambiguous chance constrained program with those of the classical chance constrained formulation of problem[eq:amb\_transp\_prob], $$\begin{array}{cl@{\quad}l} \displaystyle \min_{\bm{x}, \bm{y}} & \bm{c}^\top\bm{x} \\{\rm s.t.} & \displaystyle \sum_{f \in [F]} x_{fd} + \mathrm{M} y_i \geq \hat{\xi}_{id} & \forall d \in [D], ~i \in [N] \\& \displaystyle \bm{e}^\top \bm{y} \leq \lfloor \varepsilon N \rfloor \\& \displaystyle \sum_{d \in [D]} x_{fd} \leq m_f

<!-- chunk {"id": "body-0093", "role": "body", "section": "Transportation", "weight": 1.0} -->

& \displaystyle \forall f \in [F] \\where $\mathrm{M}$ is a sufficiently large positive constant.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Transportation", "weight": 1.0} -->

The results show that for the smallest Wasserstein radius $\theta_1 = 0.001$, the ambiguous chance constrained program[eq:amb\_transp\_prob] isas expectedmore difficult to solve than the corresponding classical chance constrained program[eq:classical\_transp\_prob]. Interestingly, the ambiguous chance constrained program becomes considerably easier to solve than the classical chance constrained program for the larger Wasserstein radii $\theta_2, \ldots, \theta_{10}$. This surprising result is explained in Figure[fig:radius], which shows that the feasible region of the ambiguous chance constrained program tends to convexify as the Wasserstein radius $\theta$ increases. In fact, one can show that the set of vectors $\bm{q} \in \{ 0, 1 \}^N$ that are feasible in the deterministic reformulation of problem[eq:amb\_transp\_prob] shrinks monotonically with $\theta$.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Transportation", "weight": 1.0} -->

Since it is the presence of these binary vectors that causes the non-convexity of problem[eq:amb\_transp\_prob], one can expect the problem to become better behaved as $\theta$increases.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Transportation", "weight": 1.0} -->

| $\#$ of distribution centers | CC | $\theta_1$ | $\theta_2$ | $\theta_3$ | $\theta_4$ | $\theta_5$ | $\theta_6$ | $\theta_7$ | $\theta_8$ | $\theta_9$ | $\theta_{10}$ | Solution times in seconds for $N = 50$ training samples. `CC' and `$\theta_i$' refer to problemeq:classical\_transp\_prob and problemeq:amb\_transp\_prob with different Wasserstein radii, respectively. We present median results over 100 random instances. Where the median solution time exceeds 3,600s, we report the median optimality gap in brackets.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Transportation", "weight": 1.0} -->

Median solution times (below dashed lines) and optimality gaps (above dashed lines) for $D = 10$ and $N = 50$ (left), $D = 30$ and $N = 100$ (middle) and $D = 50$ and $N = 150$ (right).

<!-- chunk {"id": "body-0098", "role": "body", "section": "Transportation", "weight": 1.0} -->

For a transportation problem with $F = 1$ factory, $D = 2$ distribution centers and $N = 10$ training samples, the graphs visualize the feasible regions of the classical chance constrained formulationeq:classical\_transp\_prob (left) and the ambiguous chance constrained problemeq:amb\_transp\_prob for a small (middle) and a large (right) value of $\theta$.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Transportation", "weight": 1.0} -->

Probability of meeting the safety conditions (left) and transportation costs (right) for several data-driven approaches in our transportation problem with uniformly distributed demands. Both figures present median quantities over $100$ random instances.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Transportation", "weight": 1.0} -->

Probability of meeting the safety conditions (left) and transportation costs (right) for several data-driven approaches in our transportation problem with normally distributed demands. Both figures present median quantities over $100$ random instances.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Transportation", "weight": 1.0} -->

Probability of meeting the safety conditions (left) and transportation costs (right) for several data-driven approaches in our transportation problem with exponentially distributed demands. Both figures present median quantities over $100$ random instances.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Transportation", "weight": 1.0} -->

We next compare the out-of-sample performance of our ambiguous chance constrained program [eq:amb\_transp\_prob], where the risk threshold $\varepsilon \in \{ 0.1, \, 0.05, \, 0.01 \}$ and the Wasserstein radius $\theta \in \{ 1\mathrm{E}-i \,: \, i = 2, 3, \ldots, 6 \}$ are selected using a $7$-fold cross-validation on the training dataset (`DRO'), with (i) the classical chance constrained program[eq:classical\_transp\_prob], where the risk threshold is fixed to $\varepsilon = 0.1$ (`SAA'), (ii) a variant of the classical chance constrained program[eq:classical\_transp\_prob], where the risk threshold $\varepsilon \in \{ 1\mathrm{E}-i \,: \, i = 1, 2, \ldots, 5 \} \cup \{ 0.05

<!-- chunk {"id": "body-0103", "role": "body", "section": "Transportation", "weight": 1.0} -->

\}$ is selected using a $7$-fold cross-validation on the training dataset (`CCT'), as well as (iii) a Kernel density estimator based version of the ambiguous chance constrained program over a $\phi$-divergence ambiguity set, where the risk threshold $\varepsilon \in \{ 0.1, \, 0.05, \, 0.01 \}$ and the bandwidth $h \in \{ 1\mathrm{E}-i \,: \, i = -2, -1, \ldots, 3 \}$ of the Gaussian kernel are selected using a $7$-fold cross-validation on the training dataset (`KDE'; see Jiang\_Guan\_2016).

<!-- chunk {"id": "body-0104", "role": "body", "section": "Transportation", "weight": 1.0} -->

We note that CCT can be regarded as a cross-validated version of the `best data-driven reformulation' proposed by [lam:best]. We generate random problem instances with $5$ factories, $20$ distribution centers and $25$, $30$ $250$ training samples.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Transportation", "weight": 1.0} -->

In all experiments, the expected demand $\mu_d$ at distribution center $d \in [D]$ is picked uniformly at random from the interval $$, whereas the actual demands follow a uniform distribution that is supported on $[0.8 \bm{\mu}, 1.2 \bm{\mu}]$ (Figure[fig:uniform]), a normal distribution with mean $\bm{\mu}$ and covariance matrix $0.1 \cdot \text{diag} (\bm{\mu})$ (Figure[fig:normal\_unbounded]) or an exponential distribution where each distribution center $d \in [D]$ faces a demand $(1 + 0.4 \cdot [\tilde{\zeta}_d - 0.5]) \cdot \mu_d$, where $\tilde{\zeta}_d$ follows an exponential distribution with parameter $\lambda = 2$ (Figure[fig:exponential\_unbounded]). In all cases, the demands are truncated to the non-negative real line.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Transportation", "weight": 1.0} -->

Our results indicate that the classical chance constrained program[eq:classical\_transp\_prob] generates solutions that significantly violate the chance constraint, even if we select the risk threshold $\varepsilon$ out-of-sample. The two ambiguous chance constrained formulations, on the other hand, achieve the desired risk threshold, often at a modest increase in transportation costs. While our approach and the $\phi$-divergence ambiguity set perform similarly, our formulation appears to result in lower transportation costs, especially when data is scarce.
