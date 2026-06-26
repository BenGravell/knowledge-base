<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations

Topics include Robustness, Uncertainty, Datasets, Optimization, Wasserstein distances, Metric, Wasserstein metric, Robust optimization, Probability distribution, Optimization problem.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider stochastic programs where the distribution of the uncertain parameters is only observable through a finite training dataset. Using the Wasserstein metric, we construct a ball in the space of (multivariate and non-discrete) probability distributions centered at the uniform distribution on the training samples, and we seek decisions that perform best in view of the worst-case distribution within this Wasserstein ball. The state-of-the-art methods for solving the resulting distributionally robust optimization problems rely on global optimization techniques, which quickly become computationally excruciating. In this paper we demonstrate that, under mild assumptions, the distributionally robust optimization problems over Wasserstein balls can in fact be reformulated as finite convex programs - in many interesting cases even as tractable linear programs. Leveraging recent measure concentration results, we also show that their solutions enjoy powerful finite-sample performance guarantees. Our theoretical results are exemplified in mean-risk portfolio optimization as well as uncertainty quantification.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stochastic programming is a powerful modeling paradigm for optimization under uncertainty. The goal of a generic single-stage stochastic program is to find a decision $x \in {\mathbb{R}}^{n}$ that minimizes an expected cost ${\mathbb{E}}^{\mathbb{P}}{\lbrack{h{(x,\xi)}}\rbrack}$, where the expectation is taken with respect to the distribution $\mathbb{P}$ of the continuous random vector $\xi \in {\mathbb{R}}^{m}$. However, classical stochastic programming is challenged by the large-scale decision problems encountered in today's increasingly interconnected world. First, the distribution $\mathbb{P}$ is never observable but must be inferred from data. However, if we calibrate a stochastic program to a given dataset and evaluate its optimal decision on a different dataset, then the resulting out-of-sample performance is often disappointing---even if the two datasets are generated from the same distribution.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This phenomenon is termed the optimizer's curse and is reminiscent of overfitting effects in statistics. Second, in order to evaluate the objective function of a stochastic program for a fixed decision $x$, we need to compute a multivariate integral, which is #P-hard even if $h{(x,\xi)}$ constitutes the positive part of an affine function, while $\xi$ is uniformly distributed on the unit hypercube \[24, Corollary 1\].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Distributionally robust optimization is an alternative modeling paradigm, where the objective is to find a decision $x$ that minimizes the worst-case expected cost $\sup_{{\mathbb{Q}} \in \mathcal{P}}{{\mathbb{E}}^{\mathbb{Q}}{\lbrack{h{(x,\xi)}}\rbrack}}$. Here, the worst-case is taken over an ambiguity set $\mathcal{P}$, that is, a family of distributions characterized through certain known properties of the unknown data-generating distribution $\mathbb{P}$. Distributionally robust optimization problems have been studied since Scarf's seminal treatise on the ambiguity-averse newsvendor problem in 1958, but the field has gained thrust only with the advent of modern robust optimization techniques in the last decade. Distributionally robust optimization has the following striking benefits. First, adopting a worst-case approach regularizes the optimization problem and thereby mitigates the optimizer's curse characteristic for stochastic programming.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, distributionally robust models are often tractable even though the corresponding stochastic model with the true data-generating distribution (which is generically continuous) are $\#P$-hard. So even if the data-generating distribution was known, the corresponding stochastic program could not be solved efficiently.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The ambiguity set $\mathcal{P}$ is a key ingredient of any distributionally robust optimization model. A good ambiguity set should be rich enough to contain the true data-generating distribution with high confidence. On the other hand, the ambiguity set should be small enough to exclude pathological distributions, which would incentivize overly conservative decisions. The ambiguity set should also be easy to parameterize from data, and---ideally---it should facilitate a tractable reformulation of the distributionally robust optimization problem as a structured mathematical program that can be solved with off-the-shelf optimization software.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Distributionally robust optimization models where $\xi$ has finitely many realizations are reviewed. This paper focuses on situations where $\xi$ can have a continuum of realizations. In this setting, the existing literature has studied three types of ambiguity sets. Moment ambiguity sets contain all distributions that satisfy certain moment constraints, see for example or the references therein. An attractive alternative is to define the ambiguity set as a ball in the space of probability distributions by using a probability distance function such as the Prohorov metric, the Kullback-Leibler divergence, or the Wasserstein metric etc. Such metric-based ambiguity sets contain all distributions that are close to a nominal or most likely distribution with respect to the prescribed probability metric. By adjusting the radius of the ambiguity set, the modeler can thus control the degree of conservatism of the underlying optimization problem. If the radius drops to zero, then the ambiguity set shrinks to a singleton that contains only the nominal distribution, in which case the distributionally robust problem reduces to an ambiguity-free stochastic program. In addition, ambiguity sets can also be defined as confidence regions of goodness-of-fit tests.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we study distributionally robust optimization problems with a Wasserstein ambiguity set centered at the uniform distribution ${\hat{\mathbb{P}}}_{N}$ on $N$ independent and identically distributed training samples. The Wasserstein distance of two distributions ${\mathbb{Q}}_{1}$ and ${\mathbb{Q}}_{2}$ can be viewed as the minimum transportation cost for moving the probability mass from ${\mathbb{Q}}_{1}$ to ${\mathbb{Q}}_{2}$, and the Wasserstein ambiguity set contains all (continuous or discrete) distributions that are sufficiently close to the (discrete) empirical distribution ${\hat{\mathbb{P}}}_{N}$ with respect to the Wasserstein metric.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Modern measure concentration results from statistics guarantee that the unknown data-generating distribution $\mathbb{P}$ belongs to the Wasserstein ambiguity set around ${\hat{\mathbb{P}}}_{N}$ with confidence $1 - \beta$ if its radius is a sublinearly growing function of ${\log{({1/\beta})}}/N$. The optimal value of the distributionally robust problem thus provides an upper confidence bound on the achievable out-of-sample cost.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

While Wasserstein ambiguity sets offer powerful out-of-sample performance guarantees and enable the decision maker to control the model's conservativeness, moment-based ambiguity sets appear to display better tractability properties. Specifically, there is growing evidence that distributionally robust models with moment ambiguity sets are more tractable than the corresponding stochastic models because the intractable high-dimensional integrals in the objective function are replaced with tractable (generalized) moment problems. In contrast, distributionally robust models with Wasserstein ambiguity sets are believed to be harder than their stochastic counterparts. Indeed, the state-of-the-art method for computing the worst-case expectation over a Wasserstein ambiguity set $\mathcal{P}$ relies on global optimization techniques. Exploiting the fact that the extreme points of $\mathcal{P}$ are discrete distributions with a fixed number of atoms, one may reformulate the original worst-case expectation problem as a finite-dimensional non-convex program, which can be solved via "difference of convex programming" methods, see or \[36, Section 7.1\]. However, the computational effort is reported to be considerable, and there is no guarantee to find the global optimum.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Nevertheless, tractability results are available for special cases. Specifically, the worst case of a convex law-invariant risk measure with respect to a Wasserstein ambiguity set $\mathcal{P}$ reduces to the sum of the nominal risk and a regularization term whenever $h{(x,\xi)}$ is affine in $\xi$ and $\mathcal{P}$ does not include any support constraints. Moreover, while this paper was under review we became aware of the PhD thesis, which reformulates a distributionally robust two-stage unit commitment problem over a Wasserstein ambiguity set as a semi-infinite linear program, which is subsequently solved using a Benders decomposition algorithm.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main contribution of this paper is to demonstrate that the worst-case expectation over a Wasserstein ambiguity set can in fact be computed efficiently via convex optimization techniques for numerous loss functions of practical interest. Furthermore, we propose an efficient procedure for constructing an extremal distribution that attains the worst-case expectation---provided that such a distribution exists. Otherwise, we construct a sequence of distributions that attain the worst-case expectation asymptotically. As a by-product, our analysis shows that many interesting distributionally robust optimization problems with Wasserstein ambiguity sets can be solved in polynomial time. We also investigate the out-of-sample performance of the resulting optimal decisions---both theoretically and experimentally---and analyze its dependence on the number of training samples. We highlight the following main contributions of this paper.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We prove that the worst-case expectation of an uncertain loss $\ell{(\xi)}$ over a Wasserstein ambiguity set coincides with the optimal value of a finite-dimensional convex program if $\ell{(\xi)}$ constitutes a pointwise maximum of finitely many concave functions. Generalizations to convex functions or to sums of maxima of concave functions are also discussed. We conclude that worst-case expectations can be computed efficiently to high precision via modern convex optimization algorithms.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

We describe a supplementary finite-dimensional convex program whose optimal (near-optimal) solutions can be used to construct exact (approximate) extremal distributions for the infinite-dimensional worst-case expectation problem.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that the worst-case expectation reduces to the optimal value of an explicit linear program if the $1$-norm or the $\infty$-norm is used in the definition of the Wasserstein metric and if $\ell{(\xi)}$ belongs to any of the following function classes: a pointwise maximum or minimum of affine functions; the indicator function of a closed polytope or the indicator function of the complement of an open polytope; the optimal value of a parametric linear program whose cost or right-hand side coefficients depend linearly on $\xi$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

Using recent measure concentration results from statistics, we demonstrate that the optimal value of a distributionally robust optimization problem over a Wasserstein ambiguity set provides an upper confidence bound on the out-of-sample cost of the worst-case optimal decision. We validate this theoretical performance guarantee in numerical tests.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

If the uncertain parameter vector $\xi$ is confined to a fixed finite subset of ${\mathbb{R}}^{m}$, then the worst-case expectation problems over Wasserstein ambiguity sets simplify substantially and can often be reformulated as tractable conic programs by leveraging ideas from robust optimization. An elegant second-order conic reformulation has been discovered, for instance, in the context of distributionally robust regression analysis, and a comprehensive list of tractable reformulations of distributionally robust risk constraints for various risk measures is provided. Our paper extends these tractability results to the practically relevant case where $\xi$ has uncountably many possible realizations---without resorting to space tessellation or discretization techniques that are prone to the curse of dimensionality.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

When $\ell{(\xi)}$ is linear and the distribution of $\xi$ ranges over a Wasserstein ambiguity set without support constraints, one can derive a concise closed-form expression for the worst-case risk of $\ell{(\xi)}$ for various convex risk measures. However, these analytical solutions come at the expense of a loss of generality. We believe that the results of this paper may pave the way towards an efficient computational procedure for evaluating the worst-case risk of $\ell{(\xi)}$ in more general settings where the loss function may be non-linear and $\xi$ may be subject to support constraints.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

Among all metric-based ambiguity sets studied to date, the Kullback-Leibler ambiguity set has attracted most attention from the robust optimization community. It has first been used in financial portfolio optimization to capture the distributional uncertainty of asset returns with a Gaussian nominal distribution. Subsequent work has focused on Kullback-Leibler ambiguity sets for discrete distributions with a fixed support, which offer additional modeling flexibility without sacrificing computational tractability. It is also known that distributionally robust chance constraints involving a generic Kullback-Leibler ambiguity set are equivalent to the respective classical chance constraints under the nominal distribution but with a rescaled violation probability. Moreover, closed-form counterparts of distributionally robust expectation constraints with Kullback-Leibler ambiguity sets have been derived.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, Kullback-Leibler ambiguity sets typically fail to represent confidence sets for the unknown distribution $\mathbb{P}$. To see this, assume that $\mathbb{P}$ is absolutely continuous with respect to the Lebesgue measure and that the ambiguity set is centered at the discrete empirical distribution ${\hat{\mathbb{P}}}_{N}$. Then, any distribution in a Kullback-Leibler ambiguity set around ${\hat{\mathbb{P}}}_{N}$ must assign positive probability mass to each training sample. As $\mathbb{P}$ has a density function, it must therefore reside outside of the Kullback-Leibler ambiguity set irrespective of the training samples.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

Thus, Kullback-Leibler ambiguity sets around ${\hat{\mathbb{P}}}_{N}$ contain $\mathbb{P}$ with probability 0. In contrast, Wasserstein ambiguity sets centered at ${\hat{\mathbb{P}}}_{N}$ contain discrete as well as continuous distributions and, if properly calibrated, represent meaningful confidence sets for $\mathbb{P}$. We will exploit this property in Section 3 to derive finite-sample guarantees. A comparison and critical assessment of various metric-based ambiguity sets is provided. Specifically, it is shown that worst-case expectations over Kullback-Leibler and other divergence-based ambiguity sets are law invariant. In contrast, worst-case expectations over Wasserstein ambiguity sets are not. The law invariance can be exploited to evaluate worst-case expectations via the sample average approximation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Introduction", "weight": 1.5} -->

The models proposed in this paper fall within the scope of data-driven distributionally robust optimization. Closest in spirit to our work is the robust sample average approximation, which seeks decisions that are robust with respect to the ambiguity set of all distributions that pass a prescribed statistical hypothesis test. Indeed, the distributions within the Wasserstein ambiguity set could be viewed as those that pass a multivariate goodness-of-fit test in light of the available training samples. This amounts to interpreting the Wasserstein distance between the empirical distribution ${\hat{\mathbb{P}}}_{N}$ and a given hypothesis $\mathbb{Q}$ as a test statistic and the radius of the Wasserstein ambiguity set as a threshold that needs to be chosen in view of the test's desired significance level $\beta$. The Wasserstein distance has already been used in tests for normality and to devise nonparametric homogeneity tests.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Introduction", "weight": 1.5} -->

The rest of the paper proceeds as follows. Section 2 sketches a generic framework for data-driven distributionally robust optimization, while Section 3 introduces our specific approach based on Wasserstein ambiguity sets and establishes its out-of-sample performance guarantees. In Section 4 we demonstrate that many worst-case expectation problems over Wasserstein ambiguity sets can be reduced to finite-dimensional convex programs, and we develop a systematic procedure for constructing worst-case distributions. Explicit linear programming reformulations of distributionally robust single and two-stage stochastic programs as well as uncertainty quantification problems are derived in Section 5. Section 6 extends the scope of the basic approach to broader classes of objective functions, and Section 7 reports on numerical results.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Data-Driven Stochastic Programming", "weight": 1.0} -->

Consider the stochastic program with feasible set ${\mathbb{X}} \subseteq {\mathbb{R}}^{n}$, uncertainty set $\Xi \subseteq {\mathbb{R}}^{m}$ and loss function $h:{{{\mathbb{R}}^{n} \times {\mathbb{R}}^{m}}\rightarrow\overline{\mathbb{R}}}$. The loss function depends both on the decision vector $x \in {\mathbb{R}}^{n}$ and the random vector $\xi \in {\mathbb{R}}^{m}$, whose distribution $\mathbb{P}$ is supported on $\Xi$. Problem can be viewed as the first-stage problem of a two-stage stochastic program, where $h{(x,\xi)}$ represents the optimal value of a subordinate second-stage problem. Alternatively, problem may also be interpreted as a generic learning problem in the spirit of.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Data-Driven Stochastic Programming", "weight": 1.0} -->

Unfortunately, in most situations of practical interest, the distribution $\mathbb{P}$ is not precisely known, and therefore we miss essential information to solve problem exactly. However, $\mathbb{P}$ is often partially observable through a finite set of $N$ independent samples, e.g., past realizations of the random vector $\xi$. We denote the training dataset comprising these samples by ${\hat{\Xi}}_{N} ≔ {\{{\hat{\xi}}_{i}\}}_{i \leq N} \subseteq \Xi$. We emphasize that---before its revelation---the dataset ${\hat{\Xi}}_{N}$ can be viewed as a random object governed by the distribution ${\mathbb{P}}^{N}$ supported on $\Xi^{N}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Data-Driven Stochastic Programming", "weight": 1.0} -->

A data-driven solution for problem is a feasible decision ${\hat{x}}_{N} \in {\mathbb{X}}$ that is constructed from the training dataset ${\hat{\Xi}}_{N}$. Throughout this paper, we notationally suppress the dependence of ${\hat{x}}_{N}$ on the training samples in order to avoid clutter. Instead, we reserve the superscript ' $\hat{}$ ' for objects that depend on the training data and thus constitute random objects governed by the product distribution ${\mathbb{P}}^{N}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Data-Driven Stochastic Programming", "weight": 1.0} -->

The out-of-sample performance of ${\hat{x}}_{N}$ is defined as ${\mathbb{E}}^{\mathbb{P}}\left\lbrack {h{({\hat{x}}_{N},\xi)}} \right\rbrack$ and can thus be viewed as the expected cost of ${\hat{x}}_{N}$ under a new sample $\xi$ that is independent of the training dataset. As $\mathbb{P}$ is unknown, however, the exact out-of-sample performance cannot be evaluated in practice, and the best we can hope for is to establish performance guarantees in the form of tight bounds.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Data-Driven Stochastic Programming", "weight": 1.0} -->

The feasibility of ${\hat{x}}_{N}$ in implies $J^{\star} \leq {{\mathbb{E}}^{\mathbb{P}}\left\lbrack {h{({\hat{x}}_{N},\xi)}} \right\rbrack}$, but this lower bound is again of limited use as $J^{\star}$ is unknown and as our primary concern is to bound the costs from above. Thus, we seek data-driven solutions ${\hat{x}}_{N}$ with performance guarantees of the type where ${\hat{J}}_{N}$ constitutes an upper bound that may depend on the training dataset, and $\beta \in {}$ is a *significance parameter* with respect to the distribution ${\mathbb{P}}^{N}$, which governs both ${\hat{x}}_{N}$ and ${\hat{J}}_{N}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Data-Driven Stochastic Programming", "weight": 1.0} -->

Hereafter we refer to ${\hat{J}}_{N}$ as a certificate for the out-of-sample performance of ${\hat{x}}_{N}$ and to the probability on the left-hand side of as its reliability. Our ideal goal is to find a data-driven solution with the lowest possible out-of-sample performance. This is impossible, however, as $\mathbb{P}$ is unknown, and the out-of-sample performance cannot be computed. We thus pursue the more modest but achievable goal to find a data-driven solution with a low certificate and a high reliability.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Data-Driven Stochastic Programming", "weight": 1.0} -->

A natural approach to generate data-driven solutions ${\hat{x}}_{N}$ is to approximate $\mathbb{P}$ with the discrete empirical probability distribution that is, the uniform distribution on ${\hat{\Xi}}_{N}$. This amounts to approximating the original stochastic program with the *sample-average approximation* (SAA) problem If the feasible set $\mathbb{X}$ is compact and the loss function is uniformly continuous in $x$ across all $\xi \in \Xi$, then the optimal value and optimal solutions of the SAA problem converge almost surely to their counterparts of the true problem as $N$ tends to infinity \[46, Theorem 5.3\]. Even though finite sample performance guarantees of the type can be obtained under additional assumptions such as Lipschitz continuity of the loss function (see e.g., \[47, Theorem 1\]), the SAA problem has been conceived primarily for situations where the distribution $\mathbb{P}$ is known and additional samples can be acquired cheaply via random number generation.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Data-Driven Stochastic Programming", "weight": 1.0} -->

However, the optimal solutions of the SAA problem tend to display a poor out-of-sample performance in situations where $N$ is small and where the acquisition of additional samples would be costly.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Data-Driven Stochastic Programming", "weight": 1.0} -->

In this paper we address problem with an alternative approach that explicitly accounts for our ignorance of the true data-generating distribution $\mathbb{P}$, and that offers attractive performance guarantees even when the acquisition of additional samples from $\mathbb{P}$ is impossible or expensive. Specifically, we use ${\hat{\Xi}}_{N}$ to design an ambiguity set ${\hat{\mathcal{P}}}_{N}$ containing all distributions that could have generated the training samples with high confidence. This ambiguity set enables us to define the certificate ${\hat{J}}_{N}$ as the optimal value of a distributionally robust optimization problem that minimize the worst-case expected cost.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Data-Driven Stochastic Programming", "weight": 1.0} -->

Following, we construct ${\hat{\mathcal{P}}}_{N}$ as a ball around the empirical distribution with respect to the Wasserstein metric. In the remainder of the paper we will demonstrate that the optimal value ${\hat{J}}_{N}$ as well as any optimal solution ${\hat{x}}_{N}$ (if it exists) of the distributionally robust problem satisfy the following conditions.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Data-Driven Stochastic Programming", "weight": 1.0} -->

Finite sample guarantee: For a carefully chosen size of the ambiguity set, the certificate ${\hat{J}}_{N}$ provides a $1 - \beta$ confidence bound of the type on the out-of-sample performance of ${\hat{x}}_{N}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Data-Driven Stochastic Programming", "weight": 1.0} -->

Asymptotic consistency: As $N$ tends to infinity, the certificate ${\hat{J}}_{N}$ and the data-driven solution ${\hat{x}}_{N}$ converge---in a sense to be made precise below---to the optimal value $J^{\star}$ and an optimizer $x^{\star}$ of the stochastic program, respectively.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Data-Driven Stochastic Programming", "weight": 1.0} -->

Tractability: For many loss functions $h{(x,\xi)}$ and sets $\mathbb{X}$, the distributionally robust problem is computationally tractable and admits a reformulation reminiscent of the SAA problem.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Data-Driven Stochastic Programming", "weight": 1.0} -->

Conditions (i) ‣ 2. Data-Driven Stochastic Programming ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")--(iii) ‣ 2. Data-Driven Stochastic Programming ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") have been identified in as desirable properties of data-driven solutions for stochastic programs. Precise statements of these conditions will be provided in the remainder. In Section 3 we will use the Wasserstein metric to construct ambiguity sets of the type ${\hat{\mathcal{P}}}_{N}$ satisfying the conditions (i) ‣ 2. Data-Driven Stochastic Programming ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") and (ii) ‣ 2. Data-Driven Stochastic Programming ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations").

<!-- chunk {"id": "body-0039", "role": "body", "section": "Data-Driven Stochastic Programming", "weight": 1.0} -->

In Section 4, we will demonstrate that these ambiguity sets also fulfill the tractability condition (iii) ‣ 2. Data-Driven Stochastic Programming ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations"). We see this last result as the main contribution of this paper because the state-of-the-art method for solving distributionally robust problems over Wasserstein ambiguity sets relies on global optimization algorithms.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Wasserstein Metric and Measure Concentration", "weight": 1.0} -->

Probability metrics represent distance functions on the space of probability distributions. One of the most widely used examples is the Wasserstein metric, which is defined on the space $\mathcal{M}{(\Xi)}$ of all probability distributions $\mathbb{Q}$ supported on $\Xi$ with ${{\mathbb{E}}^{\mathbb{Q}}\left\lbrack {\|\xi\|} \right\rbrack} = {\int_{\Xi}{{\|\xi\|}{\mathbb{Q}}{({d\xi})}}} < \infty$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Assumption 3.3 (Light-tailed distribution)", "weight": 1.0} -->

There exists an exponent $a > 1$ such that Assumption 3.3. ‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") essentially requires the tail of the distribution $\mathbb{P}$ to decay at an exponential rate. Note that this assumption trivially holds if $\Xi$ is compact. Heavy-tailed distributions that fail to meet Assumption 3.3. ‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") are difficult to handle even in the context of the classical sample average approximation. Indeed, under a heavy-tailed distribution the sample average of the loss corresponding to any fixed decision $x \in {\mathbb{X}}$ may not even converge to the expected loss; see e.g.. The following modern measure concentration result provides the basis for establishing powerful finite sample guarantees.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Example 1 (Necessity of regularity conditions)", "weight": 1.0} -->

Upper semicontinuity of $\xi\mapsto{h{(x,\xi)}}$ in Theorem 3.6. ‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") (i) ‣ Theorem 3.6 (Asymptotic consistency). ‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations"):\Set $\Xi = {\lbrack 0,1\rbrack}$, ${\mathbb{P}} = \delta_{0}$ and ${h{(x,\xi)}} = {\mathbb{1}_{(0,1\rbrack}{(\xi)}}$, whereby $J^{\star} = 0$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Example 1 (Necessity of regularity conditions)", "weight": 1.0} -->

‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") (i) ‣ Theorem 3.6 (Asymptotic consistency). ‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations"):\Set $\Xi = {\mathbb{R}}$, ${\mathbb{P}} = \delta_{0}$ and ${h{(x,\xi)}} = \xi^{2}$, which implies that $J^{\star} = 0$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Example 1 (Necessity of regularity conditions)", "weight": 1.0} -->

‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") (ii) ‣ Theorem 3.6 (Asymptotic consistency). ‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations"):\Set ${\mathbb{X}} = {\lbrack 0,1\rbrack}$ and ${h{(x,\xi)}} = {\mathbb{1}_{\lbrack 0.5,1\rbrack}{(x)}}$, whereby $J^{\star} = 0$ irrespective of $\mathbb{P}$. As the objective is independent of $\xi$, the distributionally robust optimization problem is equivalent to.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Example 1 (Necessity of regularity conditions)", "weight": 1.0} -->

Then, ${\hat{x}}_{N} = \frac{N - 1}{2N}$ is a sequence of minimizers for whose accumulation point $x^{\star} = \frac{1}{2}$ fails to be optimal.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Example 1 (Necessity of regularity conditions)", "weight": 1.0} -->

A convergence result akin to Theorem 3.6. ‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") for goodness-of-fit-based ambiguity sets is discussed in \[7, Section 4\]. This result is complementary to Theorem 3.6. ‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations"). Indeed, Theorem 3.6. ‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")(i) requires $h{(x,\xi)}$ to be upper semicontinuous in $\xi$, which is a necessary condition in our setting (see Example 1. ‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")) that is absent. Moreover, Theorem 3.6.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Example 1 (Necessity of regularity conditions)", "weight": 1.0} -->

‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")(ii) only requires $h{(x,\xi)}$ to be lower semicontinuous in $x$, while asks for equicontinuity of this mapping. This stronger requirement provides a stronger result, that is, the almost sure convergence of $\sup_{{\mathbb{Q}} \in {\hat{\mathcal{P}}}_{N}}{{\mathbb{E}}^{\mathbb{Q}}{\lbrack{h{(x,\xi)}}\rbrack}}$ to ${\mathbb{E}}^{\mathbb{P}}{\lbrack{h{(x,\xi)}}\rbrack}$ uniformly in $x$ on any compact subset of $\mathbb{X}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Example 1 (Necessity of regularity conditions)", "weight": 1.0} -->

Theorems 3.5. ‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") and 3.6. ‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") indicate that a careful a priori design of the Wasserstein ball results in attractive finite sample and asymptotic guarantees for the distributionally robust solutions.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Example 1 (Necessity of regularity conditions)", "weight": 1.0} -->

In practice, however, setting the Wasserstein radius to $\varepsilon_{N}{(\beta)}$ yields over-conservative solutions for the following reasons: Even though the constants $c_{1}$ and $c_{2}$ in can be computed based on the proof of \[21, Theorem 2\], the resulting Wasserstein ball is larger than necessary, i.e., ${\mathbb{P}} \notin {{\mathbb{B}}_{\varepsilon_{N}{(\beta)}}{({\hat{\mathbb{P}}}_{N})}}$ with probability $\ll \beta$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Example 1 (Necessity of regularity conditions)", "weight": 1.0} -->

The formula for $\varepsilon_{N}{(\beta)}$ in is independent of the training data. Allowing for random Wasserstein radii, however, results in a more efficient use of the available training data.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Example 1 (Necessity of regularity conditions)", "weight": 1.0} -->

While Theorems 3.5. ‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") and 3.6. ‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") provide strong theoretical justification for using Wasserstein ambiguity sets, in practice, it is prudent to calibrate the Wasserstein radius via bootstrapping or cross-validation instead of using the conservative a priori bound $\varepsilon_{N}{(\beta)}$; see Section 7.2 for further details. A similar approach has been advocated in to determine the sizes of ambiguity sets that are constructed via goodness-of-fit tests.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Example 1 (Necessity of regularity conditions)", "weight": 1.0} -->

So far we have seen that the Wasserstein metric allows us to construct ambiguity sets with favorable asymptotic and finite sample guarantees. In the remainder of the paper we will further demonstrate that the distributionally robust optimization problem with a Wasserstein ambiguity set is not significantly harder to solve than the corresponding SAA problem.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Solving Worst-Case Expectation Problems", "weight": 1.0} -->

We now demonstrate that the inner worst-case expectation problem in over the Wasserstein ambiguity set can be reformulated as a finite convex program for many loss functions $h{(x,\xi)}$ of practical interest. For ease of notation, throughout this section we suppress the dependence on the decision variable $x$. Thus, we examine a generic worst-case expectation problem involving a decision-independent loss function ${\ell{(\xi)}} ≔ {{\max_{k \leq K}\ell_{k}}{(\xi)}}$, which is defined as the pointwise maximum of more elementary measurable functions $\ell_{k}:{{\mathbb{R}}^{m}\rightarrow\overline{\mathbb{R}}}$, $k \leq K$. The focus on loss functions representable as pointwise maxima is non-restrictive unless we impose some structure on the functions $\ell_{k}$. Many tractability results in the remainder of this paper are predicated on the following convexity assumption.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Assumption 4.1 (Convexity)", "weight": 1.0} -->

The uncertainty set $\Xi \subseteq {\mathbb{R}}^{m}$ is convex and closed, and the negative constituent functions $- \ell_{k}$ are proper, convex, and lower semicontinuous for all $k \leq K$. Moreover, we assume that $\ell_{k}$ is not identically $- \infty$ on $\Xi$ for all $\leq K$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Assumption 4.1 (Convexity)", "weight": 1.0} -->

Assumption 4.1. ‣ 4. Solving Worst-Case Expectation Problems ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") essentially stipulates that $\ell{(\xi)}$ can be written as a maximum of concave functions. As we will showcase in Section 5, this mild restriction does not sacrifice much modeling power. Moreover, generalizations of this setting will be discussed in Section 6. We proceed as follows. Subsection 4.1 addresses the reduction of to a finite convex program, while Subsection 4.2 describes a technique for constructing worst-case distributions.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Reduction to a Finite Convex Program", "weight": 1.0} -->

The worst-case expectation problem constitutes an infinite-dimensional optimization problem over probability distributions and thus appears to be intractable. However, we will now demonstrate that can be re-expressed as a finite-dimensional convex program by leveraging tools from robust optimization.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Extremal Distributions", "weight": 1.0} -->

Stress test experiments are instrumental to assess the quality of candidate decisions in stochastic optimization. Meaningful stress tests require a good understanding of the extremal distributions from within the Wasserstein ball that achieve the worst-case expectation for various loss functions. We now show that such extremal distributions can be constructed systematically from the solution of a convex program akin to (18. ‣ 4.1. Reduction to a Finite Convex Program ‣ 4. Solving Worst-Case Expectation Problems ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")).

<!-- chunk {"id": "body-0058", "role": "body", "section": "Example 2 (Non-existence of a worst-case distribution)", "weight": 1.0} -->

‣ 4.2. Extremal Distributions ‣ 4. Solving Worst-Case Expectation Problems ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")) reduces to The supremum on the right-hand side amounts to $\varepsilon$ and is attained, for instance, by the sequence ${\alpha_{11}{(r)}} = {1 - \frac{1}{k}}$, ${\alpha_{12}{(r)}} = \frac{1}{k}$, ${q_{11}{(r)}} = 0$, ${q_{12}{(r)}} = {- \varepsilon}$ for $k \in {\mathbb{N}}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Example 2 (Non-existence of a worst-case distribution)", "weight": 1.0} -->

Define with ${{\xi_{11}{(r)}} = {{\hat{\xi}}_{1} - \frac{q_{11}{(r)}}{\alpha_{11}{(r)}}} = 0},$ and ${\xi_{12}{(r)}} = {{\hat{\xi}}_{1} - \frac{q_{12}{(r)}}{\alpha_{12}{(r)}}} = {\varepsilonk}$. By Theorem 4.4. ‣ 4.2. Extremal Distributions ‣ 4. Solving Worst-Case Expectation Problems ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations"), the two-point distributions ${\mathbb{Q}}_{r}$ reside within the Wasserstein ball of radius $\varepsilon$ around $\delta_{0}$ and asymptotically attain the supremum in the worst-case expectation problem.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Example 2 (Non-existence of a worst-case distribution)", "weight": 1.0} -->

However, this sequence has no weak limit as ${\xi_{12}{(r)}} = {\varepsilonk}$ tends to infinity, see Figure 1. In fact, no single distribution can attain the worst-case expectation. Assume for the sake of contradiction that there exists ${\mathbb{Q}}^{\star} \in {{\mathbb{B}}_{\varepsilon}{(\delta_{0})}}$ with ${{\mathbb{E}}^{{\mathbb{Q}}^{\star}}{\lbrack{\ell{(\xi)}}\rbrack}} = \varepsilon$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Example 2 (Non-existence of a worst-case distribution)", "weight": 1.0} -->

Then, we find $\varepsilon = {{\mathbb{E}}^{{\mathbb{Q}}^{\star}}{\lbrack{\ell{(\xi)}}\rbrack}} < {{\mathbb{E}}^{{\mathbb{Q}}^{\star}}{\lbrack{|\xi|}\rbrack}} \leq \varepsilon$, where the strict inequality follows from the relation ${\ell{(\xi)}} < {|\xi|}$ for all $\xi \neq 0$ and the observation that ${\mathbb{Q}}^{\star} \neq \delta_{0}$, while the second inequality follows from Theorem 3.2. ‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations"). Thus, ${\mathbb{Q}}^{\star}$ does not exist.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Example 2 (Non-existence of a worst-case distribution)", "weight": 1.0} -->

The existence of a worst-case distribution can, however, be guaranteed in some special cases.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Remark 4.7 (Weak coupling)", "weight": 1.0} -->

We highlight that the convex program (25. ‣ 4.2. Extremal Distributions ‣ 4. Solving Worst-Case Expectation Problems ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")) is amenable to decomposition and parallelization techniques as the decision variables associated with different sample points are only coupled through the norm constraint. We expect the resulting scenario decomposition to offer a substantial speedup of the solution times for problems involving large datasets. Efficient decomposition algorithms that could be used for solving the convex program (25. ‣ 4.2. Extremal Distributions ‣ 4. Solving Worst-Case Expectation Problems ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")) are described, for example, in and \[5, Chapter 4\].

<!-- chunk {"id": "body-0064", "role": "body", "section": "Special Loss Functions", "weight": 1.0} -->

We now demonstrate that the convex optimization problems (18. ‣ 4.1. Reduction to a Finite Convex Program ‣ 4. Solving Worst-Case Expectation Problems ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")) and (25. ‣ 4.2. Extremal Distributions ‣ 4. Solving Worst-Case Expectation Problems ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")) reduce to computationally tractable conic programs for several loss functions of practical interest.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Piecewise Affine Loss Functions", "weight": 1.0} -->

We first investigate the worst-case expectations of convex and concave piecewise affine loss functions, which arise, for example, in option pricing, risk management and in generic two-stage stochastic programming. Moreover, piecewise affine functions frequently serve as approximations of smooth convex or concave loss functions.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Uncertainty Quantification", "weight": 1.0} -->

A problem of great practical interest is to ascertain whether a physical, economic or engineering system with an uncertain state $\xi$ satisfies a number of safety constraints with high probability. In the following we denote by $\mathbb{A}$ the set of states in which the system is safe. Our goal is to quantify the probability of the event $\xi \in {\mathbb{A}}$ ($\xi \notin {\mathbb{A}}$) under an ambiguous state distribution that is only indirectly observable through a finite training dataset. More precisely, we aim to calculate the worst-case probability of the system being unsafe, i.e.,

<!-- chunk {"id": "body-0067", "role": "body", "section": "Two-Stage Stochastic Programming", "weight": 1.0} -->

A major challenge in linear two-stage stochastic programming is to evaluate the expected recourse costs, which are only implicitly defined as the optimal value of a linear program whose coefficients depend linearly on the uncertain problem parameters \[46, Section 2.1\]. The following corollary shows how we can evaluate the worst-case expectation of the recourse costs with respect to an ambiguous parameter distribution that is only observable through a finite training dataset. For ease of notation and without loss of generality, we suppress here any dependence on the first-stage decisions.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Remark 5.5 (Computational tractability)", "weight": 1.0} -->

If the Wasserstein metric is defined in terms of the $1$-norm (i.e., ${\|\xi\|} = {\sum_{k = 1}^{m}{|\xi_{k}|}}$) or the $\infty$-norm (i.e., ${\|\xi\|} = {\max_{k \leq m}{|\xi_{k}|}}$), then the optimization problems (27e ‣ Corollary 5.1 (Piecewise affine loss functions). ‣ 5.1. Piecewise Affine Loss Functions ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")), (27l ‣ Corollary 5.1 (Piecewise affine loss functions).

<!-- chunk {"id": "body-0069", "role": "body", "section": "Remark 5.5 (Computational tractability)", "weight": 1.0} -->

‣ 5.1. Piecewise Affine Loss Functions ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")), (29g ‣ Corollary 5.3 (Uncertainty quantification). ‣ 5.2. Uncertainty Quantification ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")), (29n ‣ Corollary 5.3 (Uncertainty quantification). ‣ 5.2. Uncertainty Quantification ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")), (30f ‣ Corollary 5.4 (Two-stage stochastic programming). ‣ 5.3. Two-Stage Stochastic Programming ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")) and (30k ‣ Corollary 5.4 (Two-stage stochastic programming).

<!-- chunk {"id": "body-0070", "role": "body", "section": "Remark 5.5 (Computational tractability)", "weight": 1.0} -->

‣ 5.3. Two-Stage Stochastic Programming ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")) all reduce to linear programs whose sizes scale with the number $N$ of data points and the number $J$ of affine pieces of the underlying loss functions.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Remark 5.5 (Computational tractability)", "weight": 1.0} -->

Except for the two-stage stochastic program with right-hand side uncertainty in (30k ‣ Corollary 5.4 (Two-stage stochastic programming). ‣ 5.3. Two-Stage Stochastic Programming ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")), the resulting linear programs scale polynomially in the problem description and are therefore computationally tractable. As the number of vertices $v_{k}$, $k \leq K$, of the polytope $\{{\theta \geq 0}:{{W^{\intercal}\theta} = q}\}$ may be exponential in the number of its facets, however, the linear program (30k ‣ Corollary 5.4 (Two-stage stochastic programming). ‣ 5.3. Two-Stage Stochastic Programming ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")) has generically exponential size.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Remark 5.5 (Computational tractability)", "weight": 1.0} -->

Inspecting (27e ‣ Corollary 5.1 (Piecewise affine loss functions). ‣ 5.1. Piecewise Affine Loss Functions ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")), one easily verifies that the distributionally robust optimization problem reduces to a finite convex program if $\mathbb{X}$ is convex and ${h{(x,\xi)}} = {{\max_{k \leq K}\left\langle {a_{k}{(x)}},\xi \right\rangle} + {b_{k}{(x)}}}$, while the gradients $a_{k}{(x)}$ and the intercepts $b_{k}{(x)}$ depend linearly on $x$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Remark 5.5 (Computational tractability)", "weight": 1.0} -->

‣ 5.3. Two-Stage Stochastic Programming ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")) and (30k ‣ Corollary 5.4 (Two-stage stochastic programming). ‣ 5.3. Two-Stage Stochastic Programming ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")), respectively. In contrast, problems (27l ‣ Corollary 5.1 (Piecewise affine loss functions). ‣ 5.1. Piecewise Affine Loss Functions ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")), (29g ‣ Corollary 5.3 (Uncertainty quantification).

<!-- chunk {"id": "body-0074", "role": "body", "section": "Remark 5.5 (Computational tractability)", "weight": 1.0} -->

‣ 5.2. Uncertainty Quantification ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")) and (29n ‣ Corollary 5.3 (Uncertainty quantification). ‣ 5.2. Uncertainty Quantification ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")) result in non-convex optimization problems when their data depends on $x$.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Remark 5.5 (Computational tractability)", "weight": 1.0} -->

We emphasize that the computational complexity of all convex programs examined in this section is independent of the radius $\varepsilon$ of the Wasserstein ball.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Tractable Extensions", "weight": 1.0} -->

We now demonstrate that through minor modifications of the proofs, Theorems 4.2. ‣ 4.1. Reduction to a Finite Convex Program ‣ 4. Solving Worst-Case Expectation Problems ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") and 4.4. ‣ 4.2. Extremal Distributions ‣ 4. Solving Worst-Case Expectation Problems ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") extend to worst-case expectation problems involving even richer classes of loss functions. First, we investigate problems where the uncertainty can be viewed as a stochastic process and where the loss function is additively separable. Next, we study problems whose loss functions are convex in the uncertain variables and are therefore not necessarily representable as finite maxima of concave functions as postulated by Assumption 4.1. ‣ 4. Solving Worst-Case Expectation Problems ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations").

<!-- chunk {"id": "body-0077", "role": "body", "section": "Stochastic Processes with a Separable Cost", "weight": 1.0} -->

Consider a variant of the worst-case expectation problem, where the uncertain parameters can be interpreted as a stochastic process $\xi = \left(\xi_{1},\ldots,\xi_{T} \right)$, and assume that $\xi_{t} \in \Xi_{t}$, where $\Xi_{t} \subseteq {\mathbb{R}}^{m}$ is non-empty and closed for any $t \leq T$. Moreover, assume that the loss function is additively separable with respect to the temporal structure of $\xi$, that is, where $\ell_{tk}:{{\mathbb{R}}^{m}\rightarrow\overline{\mathbb{R}}}$ is a measurable function for any $k \leq K$ and $t \leq T$. Such loss functions appear, for instance, in open-loop stochastic optimal control or in multi-item newsvendor problems.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Stochastic Processes with a Separable Cost", "weight": 1.0} -->

Consider a process norm $\left\| \xi \right\|_{T} = {\sum_{t = 1}^{T}{\|\xi_{t}\|}}$ associated with the base norm $\parallel \cdot \parallel$ on ${\mathbb{R}}^{m}$, and assume that its induced metric is the one used in the definition of the Wasserstein distance. Note that if $\parallel \cdot \parallel$ is the 1-norm on ${\mathbb{R}}^{m}$, then $\left. \parallel \cdot \parallel{}_{T} \right.$ reduces to the 1-norm on ${\mathbb{R}}^{mT}$.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Stochastic Processes with a Separable Cost", "weight": 1.0} -->

By interchanging summation and maximization, the loss function can be re-expressed as where the maximum runs over all $K^{T}$ combinations of ${k_{1},\ldots,k_{T}} \leq K$. Under this representation, Theorem 4.2. ‣ 4.1. Reduction to a Finite Convex Program ‣ 4. Solving Worst-Case Expectation Problems ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") remains applicable. However, the resulting convex optimization problem would involve $\mathcal{O}{(K^{T})}$ decision variables and constraints, indicating that an efficient solution may not be available. Fortunately, this deficiency can be overcome by modifying Theorem 4.2. ‣ 4.1. Reduction to a Finite Convex Program ‣ 4. Solving Worst-Case Expectation Problems ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations").

<!-- chunk {"id": "body-0080", "role": "body", "section": "Convex Loss Functions", "weight": 1.0} -->

Consider now another variant of the worst-case expectation problem, where the loss function $\ell$ is proper, convex and lower semicontinuous. Unless $\ell$ is piecewise affine, we cannot represent such a loss function as a pointwise maximum of finitely many concave functions, and thus Theorem 4.2. ‣ 4.1. Reduction to a Finite Convex Program ‣ 4. Solving Worst-Case Expectation Problems ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") may only provide a loose upper bound on the worst-case expectation. The following theorem provides an alternative upper bound that admits new insights into distributionally robust optimization with Wasserstein balls and becomes exact for $\Xi = {\mathbb{R}}^{m}$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Remark 6.4 (Radius of effective domain)", "weight": 1.0} -->

The parameter $\kappa$ can be viewed as the radius of the smallest ball containing the effective domain of the conjugate function $\ell^{\ast}$ in terms of the dual norm. By the standard conventions of extended arithmetic, the term $\kappa\varepsilon$ in (54. ‣ 6.2. Convex Loss Functions ‣ 6. Tractable Extensions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")) is interpreted as $0$ if $\kappa = \infty$ and $\varepsilon = 0$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Remark 6.6 (Consistent formulations)", "weight": 1.0} -->

If $\Xi = {\mathbb{R}}^{m}$ and the loss function is given by ${\ell{(\xi)}} = {\max_{k \leq K}{\{{\left\langle a_{k},\xi \right\rangle + b_{k}}\}}}$, then both Corollary 5.1. ‣ 5.1. Piecewise Affine Loss Functions ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") and Theorem 6.3. ‣ 6.2. Convex Loss Functions ‣ 6. Tractable Extensions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") offer an exact reformulation of the worst-case expectation in terms of a finite-dimensional convex program. On the one hand, Corollary 5.1.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Remark 6.6 (Consistent formulations)", "weight": 1.0} -->

‣ 5.1. Piecewise Affine Loss Functions ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") implies that is equivalent to which is obtained by setting $C = 0$ and $d = 0$ in (27e ‣ Corollary 5.1 (Piecewise affine loss functions). ‣ 5.1. Piecewise Affine Loss Functions ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")). At optimality we have $\lambda^{\star} = {\max_{k \leq K}{\| a_{k}\|}_{\ast}}$, which corresponds to the (best) Lipschitz constant of $\ell{(\xi)}$ with respect to the norm $\parallel \cdot \parallel$. On the other hand, Theorem 6.3.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Remark 6.6 (Consistent formulations)", "weight": 1.0} -->

‣ 6.2. Convex Loss Functions ‣ 6. Tractable Extensions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") implies that is equivalent to (54. ‣ 6.2. Convex Loss Functions ‣ 6. Tractable Extensions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")) with $\kappa = \lambda^{\star}$. Thus, Corollary 5.1. ‣ 5.1. Piecewise Affine Loss Functions ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") and Theorem 6.3. ‣ 6.2. Convex Loss Functions ‣ 6. Tractable Extensions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") are consistent.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Remark 6.7 ($\\varepsilon$-insensitive optimizers^33^3We are indepted to Vishal Gupta who has brought this interesting observation to our attention.)", "weight": 1.0} -->

Consider a loss function $h{(x,\xi)}$ that is convex in $\xi$, and assume that $\Xi = {\mathbb{R}}^{m}$. In this case Theorem 6.3. ‣ 6.2. Convex Loss Functions ‣ 6. Tractable Extensions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") remains valid, but the steepness parameter $\kappa{(x)}$ may depend on $x$. For loss functions whose Lipschitz modulus with respect to $\xi$ is independent of $x$ (e.g., the newsvendor loss), however, $\kappa{(x)}$ is constant. In this case the distributionally robust optimization problem and the SAA problem share the same minimizers irrespective of the Wasserstein radius $\varepsilon$. This phenomenon could explain why the SAA solutions tend to display a surprisingly strong out-of-sample performance in these problems.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

We validate the theoretical results of this paper in the context of a stylized portfolio selection problem. The subsequent simulation experiments are designed to provide additional insights into the performance guarantees of the proposed distributionally robust optimization scheme.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Mean-Risk Portfolio Optimization", "weight": 1.0} -->

Consider a capital market consisting of $m$ assets whose yearly returns are captured by the random vector $\xi = {\lbrack\xi_{1},\ldots,\xi_{m}\rbrack}^{\intercal}$. If short-selling is forbidden, a portfolio is encoded by a vector of percentage weights $x = {\lbrack x_{1},\ldots,x_{m}\rbrack}^{\intercal}$ ranging over the probability simplex ${\mathbb{X}} = {\{{x \in {\mathbb{R}}_{+}^{m}}:{{\sum_{i = 1}^{m}x_{i}} = 1}\}}$. As portfolio $x$ invests a percentage $x_{i}$ of the available capital in asset $i$ for each $i = {1,\ldots,m}$, its return amounts to $\left\langle x,\xi \right\rangle$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Mean-Risk Portfolio Optimization", "weight": 1.0} -->

In the remainder we aim to solve the single-stage stochastic program which minimizes a weighted sum of the mean and the conditional value-at-risk (CVaR) of the portfolio loss $- \left\langle x,\xi \right\rangle$, where $\alpha \in {(0,1\rbrack}$ is referred to as the confidence level of the CVaR, and $\rho \in {\mathbb{R}}_{+}$ quantifies the investor's risk-aversion. Intuitively, the CVaR at level $\alpha$ represents the average of the $\alpha \times {100\%}$ worst (highest) portfolio losses under the distribution $\mathbb{P}$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Mean-Risk Portfolio Optimization", "weight": 1.0} -->

An investor who is unaware of the distribution $\mathbb{P}$ but has observed a dataset ${\hat{\Xi}}_{N}$ of $N$ historical samples from $\mathbb{P}$ and knows that the support of $\mathbb{P}$ is contained in $\Xi = {\{{\xi \in {\mathbb{R}}^{m}}:{{C\xi} \leq d}\}}$ might solve the distributionally robust counterpart of with respect to the Wasserstein ambiguity set ${\mathbb{B}}_{\varepsilon}{({\hat{\mathbb{P}}}_{N})}$, that is, where we make the dependence on the Wasserstein radius $\varepsilon$ explicit. By Corollary 5.1.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Mean-Risk Portfolio Optimization", "weight": 1.0} -->

‣ 5.1. Piecewise Affine Loss Functions ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") we know that Before proceeding with the numerical analysis of this problem, we provide some analytical insights into its optimal solutions when there is significant ambiguity. In what follows we keep the training data set fixed and let ${\hat{x}}_{N}{(\varepsilon)}$ be an optimal distributionally robust portfolio corresponding to the Wasserstein ambiguity set of radius $\varepsilon$. We will now show that, for natural choices of the ambiguity set, ${\hat{x}}_{N}{(\varepsilon)}$ converges to the equally weighted portfolio $\frac{1}{m}e$ as $\varepsilon$ tends to infinity, where $e ≔ {(1,\ldots,1)}^{\intercal}$. The optimality of the equally weighted portfolio under high ambiguity has first been demonstrated in using analytical methods. We identify this result here as an immediate consequence of Theorem 4.2.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Mean-Risk Portfolio Optimization", "weight": 1.0} -->

‣ 4.1. Reduction to a Finite Convex Program ‣ 4. Solving Worst-Case Expectation Problems ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations"), which is primarily a computational result.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Simulation Results: Portfolio Optimization", "weight": 1.0} -->

Our experiments are based on a market with $m = 10$ assets considered in \[7, Section 7.5\]. In view of the capital asset pricing model we may assume that the return $\xi_{i}$ is decomposable into a systematic risk factor $\psi \sim {\mathcal{N}{(0,{2\%})}}$ common to all assets and an unsystematic or idiosyncratic risk factor $\zeta_{i} \sim {\mathcal{N}{({i \times {3\%}},{i \times {2.5\%}})}}$ specific to asset $i$. Thus, we set $\xi_{i} = {\psi + \zeta_{i}}$, where $\psi$ and the idiosyncratic risk factors $\zeta_{i}$, $i = {1,\ldots,m}$, constitute independent normal random variables. By construction, assets with higher indices promise higher mean returns at a higher risk.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Simulation Results: Portfolio Optimization", "weight": 1.0} -->

Note that the given moments of the risk factors completely determine the distribution $\mathbb{P}$ of $\xi$. This distribution has support $\Xi = {\mathbb{R}}^{m}$ and satisfies Assumption 3.3. ‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") for the tail exponent $a = 1$, say. We also set $\alpha = {20\%}$ and $\rho = 10$ in all numerical experiments, and we use the $1$-norm to measure distances in the uncertainty space. Thus, $\parallel \cdot \parallel_{\ast}$ is the $\infty$-norm, whereby reduces to a linear program.

<!-- chunk {"id": "body-0094", "role": "body", "section": "7.2.A. Impact of the Wasserstein Radius", "weight": 1.0} -->

In the first experiment we investigate the impact of the Wasserstein radius $\varepsilon$ on the optimal distributionally robust portfolios and their out-of-sample performance. We solve problem using training datasets of cardinality $N \in {\{ 30,300,3000\}}$. Figure 4 visualizes the corresponding optimal portfolio weights ${\hat{x}}_{N}{(\varepsilon)}$ as a function of $\varepsilon$, averaged over $200$ independent simulation runs. Our numerical results confirm the theoretical insight of Proposition 7.2. ‣ 7.1. Mean-Risk Portfolio Optimization ‣ 7. Numerical Results ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") that the optimal distributionally robust portfolios converge to the equally weighted portfolio as the Wasserstein radius $\varepsilon$ increases; see also.

<!-- chunk {"id": "body-0095", "role": "body", "section": "7.2.A. Impact of the Wasserstein Radius", "weight": 1.0} -->

The out-of-sample performance of any fixed distributionally robust portfolio ${\hat{x}}_{N}{(\varepsilon)}$ can be computed analytically as $\mathbb{P}$ constitutes a normal distribution by design, see, e.g., \[41, p. 29\]. Figure 5 shows the tubes between the 20% and 80% quantiles (shaded areas) and the means (solid lines) of the out-of-sample performance $J\left({{\hat{x}}_{N}{(\varepsilon)}} \right)$ as a function of $\varepsilon$---estimated using $200$ independent simulation runs. We observe that the out-of-sample performance improves (decreases) up to a critical Wasserstein radius $\varepsilon_{crit}$ and then deteriorates (increases). This stylized fact was observed consistently across all of simulations and provides an empirical justification for adopting a distributionally robust approach.

<!-- chunk {"id": "body-0096", "role": "body", "section": "7.2.B. Portfolios Driven by Out-of-Sample Performance", "weight": 1.0} -->

The holdout method is computationally cheaper, but cross validation has superior statistical properties. There are several other methods to estimate the best Wassertein radius ${\hat{\varepsilon}}_{N}^{opt}$. By construction, however, no method can provide a radius ${\hat{\varepsilon}}_{N}$ such that ${\hat{x}}_{N}{({\hat{\varepsilon}}_{N})}$ has a better out-of-sample performance than ${\hat{x}}_{N}{({\hat{\varepsilon}}_{N}^{opt})}$.

<!-- chunk {"id": "body-0097", "role": "body", "section": "7.2.B. Portfolios Driven by Out-of-Sample Performance", "weight": 1.0} -->

In all experiments we compare the distributionally robust approach based on the Wasserstein ambiguity set with the classical sample average approximation (SAA) and with a state-of-the-art data-driven distributionally robust approach, where the ambiguity set is defined via a linear-convex ordering (LCX)-based goodness-of-fit test \[7, Section 3.3.2\]. The size of the LCX ambiguity set is determined by a single parameter, which should be tuned to optimize the out-of-sample performance. While the best parameter value is unavailable, it can again be estimated using the holdout method or via cross validation. To our best knowledge, the LCX approach represents the only existing data-driven distributionally robust approach for continuous uncertainty spaces that enjoys strong finite-sample guarantees, asymptotic consistency as well as computational tractability.^44^4Much like worst-case expectations over Wasserstein balls, worst-case expectations over LCX ambiguity sets can be reformulated as finite convex programs whenever the underlying loss function represents a pointwise maximum of $K$ concave component functions. Unlike problem (18.

<!-- chunk {"id": "body-0098", "role": "body", "section": "7.2.B. Portfolios Driven by Out-of-Sample Performance", "weight": 1.0} -->

‣ 4.1. Reduction to a Finite Convex Program ‣ 4. Solving Worst-Case Expectation Problems ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")) in Theorem 4.2. ‣ 4.1. Reduction to a Finite Convex Program ‣ 4. Solving Worst-Case Expectation Problems ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations"), however, the resulting convex program scales exponentially with $K$.

<!-- chunk {"id": "body-0099", "role": "body", "section": "7.2.B. Portfolios Driven by Out-of-Sample Performance", "weight": 1.0} -->

To keep the computational burden manageable, in all experiments we select the Wasserstein radius as well as the LCX size parameter from within the discrete set $\mathcal{E} = {\{{\varepsilon = {b \cdot 10^{c}}}:{{b \in {\{ 0,\ldots,9\}}},{c \in {\{{- 3},{- 2},{- 1}\}}}}\}}$ instead of ${\mathbb{R}}_{+}$. We have verified that refining or extending $\mathcal{E}$ has only a marginal impact on our results, which indicates that $\mathcal{E}$ provides a sufficiently rich approximation of ${\mathbb{R}}_{+}$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "7.2.B. Portfolios Driven by Out-of-Sample Performance", "weight": 1.0} -->

(d) k-fold cross validation (e) k-fold cross validation (f) k-fold cross validation Figure 6. Out-of-sample performance J (x̂N), certificate ĴN, and certificate reliability ℙN [J (x̂N) ≤ ĴN] for the performance-driven SAA, LCX and Wasserstein solutions as a function of N In Figures 6(a)--6(c) the sizes of the (LCX and Wasserstein) ambiguity sets are determined via the holdout method, where $80\%$ of the data are used for training and $20\%$ for validation.

<!-- chunk {"id": "body-0101", "role": "body", "section": "7.2.B. Portfolios Driven by Out-of-Sample Performance", "weight": 1.0} -->

Figure 6(a) visualizes the tube between the $20\%$ and $80\%$ quantiles (shaded areas) as well as the mean value (solid lines) of the out-of-sample performance $J{({\hat{x}}_{N})}$ as a function of the sample size $N$ and based on 200 independent simulation runs, where ${\hat{x}}_{N}$ is set to the minimizer of the SAA (blue), LCX (purple) and Wasserstein (green) problems, respectively. The constant dashed line represents the optimal value $J^{\star}$ of the original stochastic program, which is computed through an SAA problem with $N = 10^{6}$ samples. We observe that the Wasserstein solutions tend to be superior to the SAA and LCX solutions in terms of out-of-sample performance.

<!-- chunk {"id": "body-0102", "role": "body", "section": "7.2.B. Portfolios Driven by Out-of-Sample Performance", "weight": 1.0} -->

Figures 6(d)--6(f) show the same graphs as Figures 6(a)--6(c), but now the sizes of the ambiguity sets are determined via $k$-fold cross validation with $k = 5$. In this case, the out-of-sample performance of both distributionally robust methods improves slightly, while the corresponding certificates and their reliabilities increase significantly with respect to the naïve holdout method. However, these improvements come at the expense of a $k$-fold increase in the computational cost.

<!-- chunk {"id": "body-0103", "role": "body", "section": "7.2.B. Portfolios Driven by Out-of-Sample Performance", "weight": 1.0} -->

One could think of numerous other statistical methods to select the size of the Wasserstein ambiguity set. As discussed above, however, if the ultimate goal is to minimize the out-of-sample performance of ${\hat{x}}_{N}{(\varepsilon)}$, then the best possible choice is $\varepsilon = {\hat{\varepsilon}}_{N}^{opt}$. Similarly, one can construct a size parameter for the LCX ambiguity set that leads to the best possible out-of-sample performance of any LCX solution. We emphasize that these optimal Wasserstein radii and LCX size parameters are not available in practice because computing $J{({{\hat{x}}_{N}{(\varepsilon)}})}$ requires knowledge of the data-generating distribution.

<!-- chunk {"id": "body-0104", "role": "body", "section": "7.2.B. Portfolios Driven by Out-of-Sample Performance", "weight": 1.0} -->

In our experiments we evaluate $J{({{\hat{x}}_{N}{(\varepsilon)}})}$ to high accuracy for every fixed $\varepsilon \in \mathcal{E}$ using $2 \cdot 10^{5}$ validation samples, which are independent from the (much fewer) training samples used to compute ${\hat{x}}_{N}{(\varepsilon)}$. Figures 6(g)--6(i) show the same graphs as Figures 6(a)--6(c) for optimally sized ambiguity sets. By construction, no method for sizing the Wasserstein or LCX ambiguity sets can result in a better out-of-sample performance, respectively. In this sense, the graphs in Figure 6(g) capture the fundamental limitations of the different distributionally robust schemes.

<!-- chunk {"id": "body-0105", "role": "body", "section": "7.2.C. Portfolios Driven by Reliability", "weight": 1.0} -->

In Section 7.2.B the Wasserstein radii and LCX size parameters were calibrated with the goal to achieve the best out-of-sample performance. Figures 6(c), 6(f) and 6(i) reveal, however, that by optimizing the out-of-sample performance one may sacrifice reliability. An alternative objective more in line with the general philosophy of Section 2 would be to choose Wasserstein radii that guarantee a prescribed reliability level. Thus, for a given $\beta \in {\lbrack 0,1\rbrack}$ we should find the smallest Wasserstein radius $\varepsilon \geq 0$ for which the optimal value ${\hat{J}}_{N}{(\varepsilon)}$ of provides an upper $1 - \beta$ confidence bound on the out-of-sample performance $J{({{\hat{x}}_{N}{(\varepsilon)}})}$ of its optimal solution.

<!-- chunk {"id": "body-0106", "role": "body", "section": "7.2.C. Portfolios Driven by Reliability", "weight": 1.0} -->

As the true distribution $\mathbb{P}$ is unknown, however, the optimal Wasserstein radius corresponding to a given $\beta$ cannot be computed exactly. Instead, we must derive an estimator ${\hat{\varepsilon}}_{N}^{\beta}$ that depends on the training data. We construct ${\hat{\varepsilon}}_{N}^{\beta}$ and the corresponding reliability-driven portfolio via bootstrapping as follows: Construct $k$ resamples of size $N$ (with replacement) from the original training dataset. It is well known that, as $N$ grows, the probability that any fixed training data point appears in a particular resample converges to $\frac{e - 1}{e} \approx \frac{2}{3}$. Thus, about $\frac{N}{3}$ training samples are absent from any resample. We collect all unused samples in a validation dataset.

<!-- chunk {"id": "body-0107", "role": "body", "section": "7.2.C. Portfolios Driven by Reliability", "weight": 1.0} -->

For each resample $\kappa = {1,\ldots,k}$ and $\varepsilon \geq 0$, solve problem using the Wasserstein ball of radius $\varepsilon$ around the empirical distribution ${\hat{\mathbb{P}}}_{N}^{\kappa}$ on the $\kappa$-th resample. The resulting optimal decision and optimal value are denoted as ${\hat{x}}_{N}^{\kappa}{(\varepsilon)}$ and ${\hat{J}}_{N}^{\kappa}{(\varepsilon)}$, respectively. Next, estimate the out-of-sample performance $J{({{\hat{x}}_{N}^{\kappa}{(\varepsilon)}})}$ of ${\hat{x}}_{N}^{\kappa}{(\varepsilon)}$ using the sample average over the $\kappa$-th validation dataset.

<!-- chunk {"id": "body-0108", "role": "body", "section": "7.2.C. Portfolios Driven by Reliability", "weight": 1.0} -->

As in Section 7.2.B, we compare the Wasserstein approach with the LCX and SAA approaches. Specifically, by using bootstrapping, we calibrate the size of the LCX ambiguity set so as to guarantee a desired reliability level $1 - \beta$. The SAA problem, on the other hand, has no free parameter that can be tuned to meet a prescribed reliability target. Nevertheless, we can construct a meaningful certificate of the form ${{\hat{J}}_{N}{(\Delta)}}:={{\hat{J}}_{SAA} + \Delta}$ for the SAA portfolio by adding a non-negative constant to the optimal value of the SAA problem.

<!-- chunk {"id": "body-0109", "role": "body", "section": "7.2.C. Portfolios Driven by Reliability", "weight": 1.0} -->

Our aim is to find the smallest offset $\Delta \geq 0$ with the property that ${\hat{J}}_{N}{(\Delta)}$ provides an upper $1 - \beta$ confidence bound on the out-of-sample performance $J{({\hat{x}}_{SAA})}$ of the optimal SAA portfolio ${\hat{x}}_{SAA}$. The optimal offset corresponding to a given $\beta$ cannot be computed exactly. Instead, we must derive an estimator ${\hat{\Delta}}_{N}^{\beta}$ that depends on the training data. Such an estimator can be found through a simple variant of the above bootstrapping procedure.

<!-- chunk {"id": "body-0110", "role": "body", "section": "7.2.D. Impact of the Sample Size on the Wasserstein Radius", "weight": 1.0} -->

It is instructive to analyze the dependence of the Wasserstein radii on the sample size $N$ for different data-driven schemes. As for the performance-driven portfolios from Section 7.2.B, Figure 8 depicts the best possible Wasserstein radius ${\hat{\varepsilon}}_{N}^{opt}$ as well as the Wasserstein radii ${\hat{\varepsilon}}_{N}^{hm}$ and ${\hat{\varepsilon}}_{N}^{cv}$ obtained by the holdout method and via $k$-fold cross validation, respectively. As for the reliability-driven portfolios from Section 7.2.C, Figure 8 further depicts the Wasserstein radii ${\hat{\varepsilon}}_{N}^{\beta}$, for $\beta \in {\{{10\%},{25\%}\}}$, obtained by bootstrapping. All results are averaged across 200 independent simulation runs. As expected from Theorem 3.6.

<!-- chunk {"id": "body-0111", "role": "body", "section": "7.2.D. Impact of the Sample Size on the Wasserstein Radius", "weight": 1.0} -->

‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations"), all Wasserstein radii tend to zero as $N$ increases. Moreover, the convergence rate is approximately equal to $N^{- \frac{1}{2}}$. This rate is likely to be optimal. Indeed, if $\mathbb{X}$ is a singleton, then every quantile of the sample average estimator ${\hat{J}}_{SAA}$ converges to $J^{\star}$ at rate $N^{- \frac{1}{2}}$ due to the central limit theorem.

<!-- chunk {"id": "body-0112", "role": "body", "section": "7.2.D. Impact of the Sample Size on the Wasserstein Radius", "weight": 1.0} -->

Thus, if ${\hat{\varepsilon}}_{N} = {o{(N^{- \frac{1}{2}})}}$, then ${\hat{J}}_{N}$ also converges to $J^{\star}$ at leading order $N^{- \frac{1}{2}}$ by Theorem 6.3. ‣ 6.2. Convex Loss Functions ‣ 6. Tractable Extensions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations"), which applies as the loss function is convex. This indicates that the a priori rate $N^{- \frac{1}{m}}$ suggested by Theorem 3.4. ‣ 3. Wasserstein Metric and Measure Concentration ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations") is too pessimistic in practice.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Simulation Results: Uncertainty Quantification", "weight": 1.0} -->

Investors often wish to determine the probability that a given portfolio will outperform various benchmark indices or assets. Our results on uncertainty quantification developed in Section 5.2 enable us to compute this probability in a meaningful way---solely on the basis of the training dataset.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Simulation Results: Uncertainty Quantification", "weight": 1.0} -->

Assume for example that we wish to quantify the probability that any data-driven portfolio ${\hat{x}}_{N}$ outperforms the three most risky assets in the market jointly. Thus, we should compute the probability of the closed polytope As the true distribution $\mathbb{P}$ is unknown, the probability ${\mathbb{P}}{\lbrack{\xi \in \hat{\mathbb{A}}}\rbrack}$ cannot be evaluated exactly. Note that $\hat{\mathbb{A}}$ as well as ${\mathbb{P}}{\lbrack{\xi \in \hat{\mathbb{A}}}\rbrack}$ constitute random objects that depend on ${\hat{x}}_{N}$ and thus on the training data.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Simulation Results: Uncertainty Quantification", "weight": 1.0} -->

Using the same training dataset that was used to compute ${\hat{x}}_{N}$, however, we may estimate ${\mathbb{P}}{\lbrack{\xi \in \hat{\mathbb{A}}}\rbrack}$ from above and below by respectively. Indeed, recall that the true data-generating probability distribution resides in the Wasserstein ball of radius $\varepsilon_{N}{(\beta)}$ defined in with probability $1 - \beta$. Therefore, we have where ${\mathfrak{B}}{(\Xi)}$ denotes the set of all Borel subsets of $\Xi$. The data-dependent set ${\hat{\mathbb{A}}}_{N}$ can now be viewed as a (measurable) mapping from ${\hat{\Xi}}_{N}$ to the subsets in ${\mathfrak{B}}{(\Xi)}$.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Simulation Results: Uncertainty Quantification", "weight": 1.0} -->

The upper confidence bound can be computed by solving the linear program (29g ‣ Corollary 5.3 (Uncertainty quantification). ‣ 5.2. Uncertainty Quantification ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")). Replacing $\hat{\mathbb{A}}$ with its interior in the lower confidence bound leads to another (potentially weaker) lower bound that can be computed by solving the linear program (29n ‣ Corollary 5.3 (Uncertainty quantification). ‣ 5.2. Uncertainty Quantification ‣ 5. Special Loss Functions ‣ Data-Driven Distributionally Robust Optimization Using the Wasserstein Metric: Performance Guarantees and Tractable Reformulations")). We denote these computable bounds by ${\hat{J}}_{N}^{+}{(\varepsilon)}$ and ${\hat{J}}_{N}^{-}{(\varepsilon)}$, respectively.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Simulation Results: Uncertainty Quantification", "weight": 1.0} -->

In all subsequent experiments ${\hat{x}}_{N}$ is set to a solution of the distributionally robust program calibrated via $k$-fold cross validation as described in Section 7.2.B.

<!-- chunk {"id": "body-0118", "role": "body", "section": "7.3.B. Impact of the Sample Size", "weight": 1.0} -->

We propose a variant of the $k$-fold cross validation procedure for selecting $\varepsilon$ in uncertainty quantification. Partition ${\hat{\xi}}_{1},\ldots,{\hat{\xi}}_{N}$ into $k$ subsets and repeat the following holdout method $k$ times. Select one of the subsets as the validation set of size $N_{V}$ and merge the remaining $k - 1$ subsets to a training dataset of size $N_{T} = {N - N_{V}}$. Use the validation set to compute the SAA estimator of ${\mathbb{P}}{\lbrack\hat{\mathbb{A}}\rbrack}$, and use the training dataset to compute ${\hat{J}}_{N_{T}}^{+}{(\varepsilon)}$ for a large but finite number of candidate radii $\varepsilon$.

<!-- chunk {"id": "body-0119", "role": "body", "section": "7.3.B. Impact of the Sample Size", "weight": 1.0} -->

The data-driven lower bound ${\hat{J}}_{N}^{-}$ is constructed analogously in the obvious way.

<!-- chunk {"id": "body-0120", "role": "body", "section": "7.3.B. Impact of the Sample Size", "weight": 1.0} -->

(a) Excess ${\hat{J}}_{N}^{+} - {{\mathbb{P}}{\lbrack\hat{\mathbb{A}}\rbrack}}$ and shortfall ${\hat{J}}_{N}^{-} - {{\mathbb{P}}{\lbrack\hat{\mathbb{A}}\rbrack}}$ of the data-driven confidence bounds for ${\mathbb{P}}{\lbrack\hat{\mathbb{A}}\rbrack}$ (b) Data-driven Wasserstein radius ε̂Ncv obtained via k-fold cross validation Figure 10. Dependence of the confidence bounds and the Wasserstein radius on N Figure 10(b) shows the Wasserstein radius ${\hat{\varepsilon}}_{N}^{cv}$ obtained via $k$-fold cross validation (both for ${\hat{J}}_{N}^{+}$ and

<!-- chunk {"id": "body-0121", "role": "body", "section": "7.3.B. Impact of the Sample Size", "weight": 1.0} -->

As usual, all results are averaged across 300 independent simulation runs. A comparison with Figure 8 reveals that the data-driven Wasserstein radii in uncertainty quantification display a similar but faster polynomial decay than in portfolio optimization. We conjecture that this is due to the absence of decisions, which implies that uncertainty quantification is less susceptible to the optimizer's curse. Thus, nature (i.e., the fictitious adversary choosing the distribution in the ambiguity set) only has to compensate for noise but not for bias. A smaller Wasserstein radius seems to be sufficient for this purpose.
