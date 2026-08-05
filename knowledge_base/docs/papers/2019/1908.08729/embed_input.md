<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Wasserstein Distributionally Robust Optimization: Theory and Applications in Machine Learning

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Many decision problems in science, engineering and economics are affected by uncertain parameters whose distribution is only indirectly observable through samples. The goal of data-driven decision-making is to learn a decision from finitely many training samples that will perform well on unseen test samples. This learning task is difficult even if all training and test samples are drawn from the same distribution - especially if the dimension of the uncertainty is large relative to the training sample size. Wasserstein distributionally robust optimization seeks data-driven decisions that perform well under the most adverse distribution within a certain Wasserstein distance from a nominal distribution constructed from the training samples. In this tutorial we will argue that this approach has many conceptual and computational benefits. Most prominently, the optimal decisions can often be computed by solving tractable convex optimization problems, and they enjoy rigorous out-of-sample and asymptotic consistency guarantees. We will also show that Wasserstein distributionally robust optimization has interesting ramifications for statistical learning and motivates new approaches for fundamental learning tasks such as classification, regression, maximum likelihood estimation or minimum mean square error estimation, among others.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider a decision problem under uncertainty, where each admissible decision results in an uncertain loss that is modeled by a measurable extended real-valued loss function $\ell(\xi)$. We assume that the random vector $\xi\in\mathbb{R}^m$ captures all decision-relevant risk factors and is governed by a probability distribution $\mathds{P}$. The feasible set of all available loss functions is denoted by $\mathcal{L}$.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The risk of a decision $\ell\in\mathcal{L}$ is defined as the expected loss under $\mathds{P}$, that is, $$\mathcal{R} (\mathds{P}, \ell) = \mathds{E}^{\mathds{P}} [\ell(\xi)],$$ and the optimal risk is defined as the risk of the least risky admissible loss function, that is, $$\mathcal{R}(\mathds{P}, \mathcal{L}) = \inf_{\ell \in \mathcal{L}} ~ \mathcal{R} (\mathds{P}, \ell).$$ To ensure that the expectations in[eq:risk] and[eq:opt:risk] are defined for all measurable loss functions, we set $\mathds{E}^{\mathds{P}} [\ell(\xi)]=\infty$ whenever the expectations of the positive and negative parts of $\ell(\xi)$are both

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

infinite. This convention means that infeasibility trumps unboundedness.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In most real decision-making situations, the distribution $\mathds{P}$ is fundamentally unknown. However, $\mathds{P}$ may be indirectly observable through training samples $\widehat \xi_i$, $i\in\{1, \ldots, N\}$, drawn independently from $\mathds{P}$. In addition, some structural properties of $\mathds{P}$ may be known. For example, if $\xi$ represents a vector of uncertain prices, then $\mathds{P}$ must be supported on the nonnegative orthant$\mathbb{R}^m_+$. Alternatively, $\mathds{P}$ may be known to display certain symmetry or unimodality properties, or it may even be known to belong to some parametric distributionfamily. $\mathds{P}$ is unknown, we lack an important input parameter for the risk evaluation problem[eq:risk] and the decision problem[eq:opt:risk].

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this case, the unknown true distribution$\mathds{P}$ could be replaced with a nominal distribution $\widehat \PP_N$ estimated from the $N$ training samples. Note that unlike $\mathds{P}$, the nominal distribution $\widehat \PP_N$ is accessible as it is constructed from observable quantities. Therefore, the nominal risk evaluation and decision problems (that is, problems[eq:risk] and[eq:opt:risk] with $\widehat \PP_N$ instead of $\mathds{P}$) are at least in principle solvable. The following example showcases common methods for constructing the nominal distribution$\widehat \PP_N$.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the remainder we will primarily work with the following non-parametric and parametric models for the nominal distribution.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

- In the absence of any structural information, it is convenient to set $\widehat \PP_N$ to the discrete empirical distribution, that is, the uniform distribution on the $N$ training samples, $$\widehat \PP_N = \frac{1}{N} \sum_{i=1}^N \delta_{\widehat \xi_i},$$ - where $\delta_{\widehat \xi_i}$ denotes the Dirac point mass at the $i^{\rm th}$ training sample $\widehat \xi_i$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

- We say that $\mathds{Q}=\mathcal{E}_g(\mu, \Sigma)$ is an elliptical probability distribution if it has a density function of the form $f(\xi) = C \det(\Sigma)^{-1} \, g((\xi-\mu) \Sigma^{-1} (\xi-\mu))$ with density generator $g(u)\ge 0$ for all $u\ge 0$, normalization constant $C>0$, mean vector $\mu\in\mathbb{R}^m$ and covariance matrix $\Sigma\in\mathbb{S}_{++}^m$. Examples of elliptical distributions are reported in Table[tabel:elliptical] of Appendix[sect:elliptical].

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the presence of structural information, it is often convenient to set $\widehat \PP_N$ to an elliptical distribution with a structure-dependent density generator $g$, that is, $$\widehat \PP_N = \mathcal{E}_g(\widehat\m, \widehat\cov),$$ - where only the mean vector $\widehat\m$ and the covariance matrix $\widehat\cov$ depend on the training samples and are constructed via maximum likelihood estimation.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

As a function of the training data, the nominal distribution $\widehat \PP_N$ constitutes itself a random object, which is governed by the distribution $\mathds{P}^N$ of the $N$ independent training samples.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Even if the most sophisticated statistical tools are deployed, the nominal distribution $\widehat \PP_N$ will invariably differ from the unknown true distribution $\mathds{P}$ that generated the training samples. Moreover, if $\widehat \PP_N$ is used instead of $\mathds{P}$, the solutions of the risk evaluation problem[eq:risk] and the decision problem[eq:opt:risk] are likely to inherit any estimation errors in$\widehat \PP_N$. In the context of financial portfolio theory it has even been observed that estimation errors in the input parameters of an optimization problem are often amplified by the optimization [chopra2011errors, michaud1989enigma]. To make things worse, one can generally show that even if the distributional input parameters of a decision problem are unbiased, the optimization results tend to be optimistically biased. Thus, implementing the optimal decisions leads to disappointment in out-of-sample tests.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

In decision analysis this phenomenon is sometimes termed the optimizer's curse [smith2006curse], and in stochastic optimization it is referred to as the optimization bias [homemdemello2014, shapiro2003].

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Let $\widehat \PP_N$ be an unbiased estimator for $\mathds{P}$. Thus, we have $\mathds{E}^{\mathds{P}^N}[\widehat \PP_N]=\mathds{P}$, where the expectation is taken with respect to the distribution $\mathds{P}^N$ of the $N$ independent training samples.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Then, the risk of a fixed loss function $\ell\in\mathcal{L}$ satisfies $$\mathds{E}^{\mathds{P}^N}\left[\mathcal{R}(\widehat \PP_N,\ell) \right] = \mathds{E}^{\mathds{P}^N}\left[\mathds{E}^{\widehat \PP_N} [\ell(\xi)]\right] = \mathds{E}^{\mathds{P}} [\ell(\xi)] = \mathcal{R}(\mathds{P},\ell),$$ where the second equality holds because the inner expectation is linear in $\widehat \PP_N$. This implies that $\mathcal{R}(\widehat \PP_N,\ell)$ constitutes an unbiased estimator for the true risk $\mathcal{R}(\mathds{P},\ell)$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

Hence, $\mathcal{R}(\widehat \PP_N,\mathcal{L})$ constitutes an optimistically biased estimator for $\mathcal{R}(\mathds{P},\mathcal{L})$, i.e., it underestimates the true risk. On the other hand, any optimizer $\ell^\star\in\arg\min_{\ell\in\mathcal{L}} \mathcal{R}(\widehat \PP_N,\ell)$ satisfies \mathcal{R}(\mathds{P},\ell^\star)\ge \inf_{\ell\in\mathcal{L}} ~\mathcal{R}(\mathds{P},\ell) = \mathcal{R}(\mathds{P}, \mathcal{L}).$$ The above observations can be interpreted as follows.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

Someone solving the nominal decision problem thinks that the risk of $\ell^\star$ amounts to $\mathcal{R}(\widehat \PP_N,\ell^\star) = \mathcal{R}(\widehat \PP_N,\mathcal{L})$ (the in-sample risk), which is typically smaller than the optimal risk $\mathcal{R}(\mathds{P},\mathcal{L})$ attainable under full knowledge of$\mathds{P}$. However, the actual risk $\mathcal{R}(\mathds{P},\ell^\star)$ of the optimizer$\ell^\star$ under the true distribution (the out-of-sample risk) is always larger than $\mathcal{R}(\mathds{P},\mathcal{L})$. The difference between the out-of-sample risk and the in-sample risk is termed the post-decision disappointment. The optimizer's curse refers to the observation that the post-decision disappointment is positive on average.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

In order to quantify the sensitivity of $\mathcal{R} (\mathds{P}, \ell)$ and $\mathcal{R}(\mathds{P}, \mathcal{L})$ with respect to the unknown true distribution $\mathds{P}$, we must introduce a distance measure between probability distributions. As we will argue below, the Wasserstein distance is a particularly convenient choice.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

One can show that the Wasserstein distance is a metric, that is, it is nonnegative, symmetric and subadditive, and it vanishes only if $\mathds{Q}=\mathds{Q}'$ [villani2008optimal]. One can further show that $W_p(\mathds{Q}, \mathds{Q}')$ is finite whenever both $\mathds{Q}$ and $\mathds{Q}'$ have finite $p^{\rm th}$-order moments [villani2008optimal].

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

The optimal value of the optimization problem in [eq:wasserstein] can be interpreted as the minimum cost of turning one pile of dirt represented by$\mathds{Q}$ into another pile of dirt represented by$\mathds{Q}'$, where the cost of moving a unit mass from $\xi$ to $\xi'$ amounts to $\|\xi-\xi'\|^p$. The decision variable $\pi$ thus encodes a transportation plan, that is, for any measurable sets $A,B\subseteq \mathbb{R}^m$ the probability $\pi(A\times B)$ reflects the amount of mass that is moved from the source region$A$ to the target region$B$. Because of this interpretation, the Wasserstein distance is often referred to as the earth mover's distance in statistics and computer science[rubner2000earth]. The theory of optimal transport was pioneered by Monge in 1781 [monge1781memoire] and formalized by Kantorovich in 1942 [kantorovich1942translocation].

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

Accordingly, the Wasserstein distance is often referred to as the Monge-Kantorovich distance[villani2008optimal]. The Wasserstein distance is used in many areas of science.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Introduction", "weight": 1.5} -->

In the wider context of machine learning, for instance, the Wasserstein distance is used for the analysis of mixture models[kolouri2018sliced, nguyen2013convergence] as well as for image processing[alvarez2018structured, ferradans2014regularized, kolouri2015transport, papadakis2017convex, tartavel2016wasserstein], computer vision and graphics[pele2008linear, pele2009fast, rubner2000earth, solomon2015convolutional, solomon2014earth], data-driven bioengineering[feydy2017optimal, kundu2018discovery, wang2011optimal], clustering[ho2017multilevel], dimensionality reduction[cazelles2018geodesic, flamary2018wasserstein, rolet2016fast, schmitz2018wasserstein, seguy2015principal], deep learning with generative adversarial networks[arjovsky2017wasserstein, genevay2018learning,

<!-- chunk {"id": "body-0024", "role": "body", "section": "Introduction", "weight": 1.5} -->

gulrajani2017improved], domain adaptation[courty2017optimal, murez2018image], signal processing[thorpe2017transportation], etc. For a comprehensive survey of different applications of the optimal transport problem see[kolouri2017optimal, peyre2018computational].

<!-- chunk {"id": "body-0025", "role": "body", "section": "Introduction", "weight": 1.5} -->

The optimization problem in [eq:wasserstein] constitutes an infinite-dimensional linear program over the transportation plan$\pi$. This linear program admits a strong dual, which in turn provides an alternative characterization of the Wasserstein distance.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Introduction", "weight": 1.5} -->

For any $p \in [1, \infty)$, the $p^{\rm th}$ power of the type-$p$ Wasserstein distance between $\mathds{Q}$ and $\mathds{Q}'$ admits the dual representation \displaystyle W_p^p(\mathds{Q}, \mathds{Q}') =~ \sup & \displaystyle \int_{\mathbb{R}^m} \psi(\xi') \, \mathds{Q}'(\diff \xi') - \int_{\mathbb{R}^m} \phi(\xi) \, \mathds{Q}(\diff \xi) \\ [1em] \st & \phi \text{ and }\psi \text{ are bounded continuous functions on $\mathbb{R}^m$ with} \\ [0.5em] & \displaystyle \psi(\xi)-\phi(\xi') \leq \| \xi - \xi' \|^p \quad \forall \xi,

<!-- chunk {"id": "body-0027", "role": "body", "section": "Introduction", "weight": 1.5} -->

For a proof of Theorem [thm:dual-kantorovich] see[villani2008optimal]. The dual problem can be interpreted as the profit maximization problem of a third party that reallocates the dirt from $\mathds{Q}$ to $\mathds{Q}'$ on behalf of the problem owner by buying dirt at the origin $\xi$ at unit price $\phi(\xi)$ and selling dirt at the destination $\xi'$ at unit price $\psi(\xi')$. The constraints ensure that the problem owner prefers to use the services of the third party for every origin-destination pair $(\xi,\xi')$ instead of reallocating the dirt independently at her own transportation cost $\|\xi-\xi'\|^p$. The optimal price functions $\phi^\star$ and $\psi^\star$if they existare called Kantorovich potentials [villani2008optimal]. $p=1$, the dual problem can be further simplified.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Introduction", "weight": 1.5} -->

To see this, we define the Lipschitz modulus of an extended real-valued function $\phi$ on $\mathbb{R}^m$ with respect to the norm $ \| \cdot \|$ as $$\Lip(\phi) = \sup_{\xi \neq \xi'} ~ \frac{|\phi(\xi)-\phi(\xi')|}{\| \xi - \xi'\|}.$$ The Lipschitz modulus can be viewed as the slope of the steepest line segment connecting any two points on the graph of $\phi$. The following result simplifies Theorem[thm:dual-kantorovich] for $p=1$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Introduction", "weight": 1.5} -->

The type-1 Wasserstein distance between $\mathds{Q}$ and $\mathds{Q}'$ admits the dual representation $$W_1(\mathds{Q},\mathds{Q}') = \sup_{\Lip(\phi) \leq 1} ~ \int_{\mathbb{R}^m} \phi(\xi) \, \mathds{Q}(\diff \xi) - \int_{\mathbb{R}^m} \phi(\xi') \, \mathds{Q}'(\diff \xi').$$ Kantorovich and Rubinstein [kantorovich1958space] originally established this result for compactly supported distributions. A modern proof for arbitrary distributions can be found in[villani2008optimal].

<!-- chunk {"id": "body-0030", "role": "body", "section": "Introduction", "weight": 1.5} -->

Theorem[thm:kantorovich-rubinstein] asserts that the type-1 Wasserstein distance between $\mathds{Q}$ and $\mathds{Q}'$ equals the difference between the expected values of a test function $\phi$ under $\mathds{Q}$ and $\mathds{Q}'$, respectively, maximized across all Lipschitz-continuous test functions with Lipschitz modulus of at most1.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Kantorovich-Rubinstein theorem enables us to estimate the sensitivity of $\mathcal{R} (\mathds{P}, \ell)$ and $\mathcal{R}(\mathds{P}, \mathcal{L})$ with respect to the unknown true distribution $\mathds{P}$. To see this, assume that the type-1 Wasserstein distance between $\mathds{P}$ and its noisy estimate $\widehat \PP_N$ is known to be at most $\varepsilon$. Thus, $\varepsilon$ can be viewed as a measure of the estimation error. Assume further that a fixed loss function $\ell(\xi)$ is Lipschitz-continuous with Lipschitz constant $L$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Introduction", "weight": 1.5} -->

The risk of $\ell$ then satisfies $$\left| \mathcal{R}(\widehat \PP_N, \ell)-\mathcal{R}(\mathds{P}, \ell) \right| = L\cdot \left| \mathds{E}^{\widehat \PP_N}[\ell(\xi)/L] - \mathds{E}^{\mathds{P}}[\ell(\xi)/L] \right| \le L\cdot W_1(\widehat \PP_N, \mathds{P})\le L\cdot\varepsilon,$$ where the equality holds due to the definition of the risk, while the first inequality follows from the Kantorovich-Rubinstein theorem, which applies because $\Lip(\ell/L)\le 1$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Introduction", "weight": 1.5} -->

Moreover, if all loss functions $\ell\in\mathcal{L}$ are Lipschitz continuous with the same Lipschitz constant $L$, then a similar reasoning implies that the optimal risk satisfies $| \mathcal{R}(\widehat \PP_N, \mathcal{L})-\mathcal{R}(\mathds{P}, \mathcal{L}) | \le L\cdot \varepsilon$. This analysis offers a rough understanding of how estimation errors in the input distribution are propagated to the (optimal) risk: they are amplified at most by the Lipschitz constant of the involved loss functions. Arguments of this type are central to the stability theory of stochastic programming. For example, it is known that under standard regularity conditions, the optimal values of two-stage stochastic programs with random right hand sides are Lipschitz continuous in the distribution of the uncertainty with respect to the Wasserstein distance[roemisch1991stability]. Classical stability results in stochastic programming are surveyed in[dupacova1990stability,roemisch2003].

<!-- chunk {"id": "body-0034", "role": "body", "section": "Introduction", "weight": 1.5} -->

The above reasoning suggests that in order to approximate the (optimal) risk well, one should construct an estimator $\widehat \PP_N$ that has a small Wasserstein distance to the unknown true distribution $\mathds{P}$with high confidence. Unfortunately, however, estimators are subject to fundamental performance limitations and cannot be improved beyond a certain level. [Limitations of estimator performance] Depending on the available structural information on $\mathds{P}$, the nominal distributions portrayed in Example[ex:nominal-distribution], which will be used throughout this tutorial, are essentially optimal within certain estimator families.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Introduction", "weight": 1.5} -->

- Discrete distributions: Assume that $\mathds{P}$ is only known to be supported on a compact set $\Xi\subseteq \mathbb{R}^m$, and let $\mathcal P_N$ be the family of all discrete distributions on $\Xi$ with $N$ atoms. The theory of optimal quantization shows that there exist $\underline N\in\mathbb N$ and $\underline c>0$ such that $\inf_{\mathds{Q}\in\mathcal P_N}W_1(\mathds{Q},\mathds{P})\ge \underline c N^{-1/m}$ for all $N\ge \underline N$ [canas2012learning]. Thus, the type-1 Wasserstein distance between $\mathds{P}$ and its closest $N$-point distribution cannot decay faster than $N^{-1/m}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Introduction", "weight": 1.5} -->

Maybe surprisingly, the empirical distribution $\widehat \PP_N = \frac{1}{N} \sum_{i=1}^N \delta_{\widehat \xi_i}$ attains this optimal decay rate in a probabilistic sense even though it is constructed from $N$ random samples but without knowledge of $\mathds{P}$. Indeed, [fournier2015rate] implies that for every $\eta\in$ there exist $\overline N\in\mathbb N$ and $\overline c>0$ such that $W_1(\widehat \PP_N,\mathds{P})\le \overline c N^{-1/m}$ with confidence $1-\eta$ for every $N\ge \overline N$. Thus, if we aim to approximate $\mathds{P}$ with a sequence of discrete distributions, the empirical distribution $\widehat \PP_N$ is essentially optimal in the sense that it attains the best possible convergence rate at any desired confidencelevel.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Introduction", "weight": 1.5} -->

- Elliptical distributions: Assume that $\mathds{P}$ is known to be an elliptical distribution with a known density generator $g$ but unknown mean vector $\mu$ and covariance matrix$\Sigma$. In this case, the problem of finding an estimator $\widehat \PP_N$ for the distribution $\mathds{P}$ reduces to finding an estimator $\widehat \theta_N$ for the vector $\theta=(\mu,\Sigma)$ of unknown distribution parameters. Under mild regularity conditions, the Cramer-Rao inequality guarantees that the covariance matrix of $\sqrt{N}\cdot \widehat\theta_N$ exceeds the inverse Fisher information matrix in a positive semidefinite sense for any unbiased estimator $\widehat \theta_N$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Introduction", "weight": 1.5} -->

As the maximum likelihood estimator $\widehat \theta_N^{\, \rm ML}$ is asymptotically unbiased and efficient, i.e., the mean of $\widehat\theta_N^{\, \rm ML}$ converges to$\theta$ and the variance of $\sqrt{N}\cdot \widehat\theta_N^{\, \rm ML}$ converges to the inverse Fisher information matrix as $N$ grows, it is asymptotically optimal among all conceivable unbiased estimators.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Introduction", "weight": 1.5} -->

We emphasize that, by mobilising more powerful results from statistics, the above optimality guarantees could be extended to even larger families of estimators. [ex:estimator-limitations] suggests that the accuracy of the nominal distribution cannot be increased beyond some fundamental limit by tuning the estimator. The only remaining option to reduce the estimation error is to increase the sample size$N$, which may be expensive or impossible. Indeed, additional training samples may only become available in the future. Thus, the optimizer's curse illustrated in Example[ex:optimizers-curse] is fundamental and cannot be eliminated. However, once the potential to improve the estimator $\widehat \PP_N$ is exhausted, it may still be possible to mitigate the optimizer's curse by altering the risk evaluation and decision problems[eq:risk] and[eq:opt:risk] directly. Specifically, we propose here to robustify these problems against the uncertainty about the true distribution $\mathds{P}$. Distributional uncertainty is often referred to as ambiguity or Knightian uncertainty and is conveniently captured by an ambiguity set, that is, an uncertainty set in the space of probability distributions.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Introduction", "weight": 1.5} -->

To formalize this idea, we let $\Xi\subseteq\mathbb{R}^m$ be a closed set that is known to contain the support of$\mathds{P}$. In the absence of any structural information, we may simply set $\Xi=\mathbb{R}^m$. Moreover, we denote by$\mathcal P(\Xi)$ the family of all probability distributions supported on $\Xi$, and we define the ambiguity set $$\mathbb{B}_{\varepsilon,p}(\widehat \PP_N) = \left\{ \mathds{Q} \in \mathcal P(\Xi): W_p(\mathds{Q}, \widehat \PP_N) \leq \varepsilon \right\}$$ as the ball of radius $\varepsilon\ge 0$ in $\mathcal P(\Xi)$ centered at the nominal distribution $\widehat \PP_N$ with respect to the type-$p$ Wasserstein distance.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Introduction", "weight": 1.5} -->

By construction, this ambiguity set contains all distributions supported on $\Xi$ that can be obtained by reshaping the nominal distribution$\widehat \PP_N$ at a transportation cost of at most $\varepsilon$. We can think of $\mathbb{B}_{\varepsilon,p}(\widehat \PP_N)$ as the set of all distributions for which the estimation erroras measured by the type-$p$ Wasserstein distanceis at most $\varepsilon$, and we can interpret $\varepsilon$as the maximum estimation error against which we seek protection.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Introduction", "weight": 1.5} -->

Using the proposed ambiguity set, we define the $$\mathcal{R}_{\varepsilon, p}(\widehat \PP_N, \ell) = \sup_{\mathds{Q} \in \mathbb{B}_{\varepsilon,p}(\widehat \PP_N)} ~ \mathcal{R}(\mathds{Q}, \ell)$$ and the worst-case optimal risk as $$\mathcal{R}_{\varepsilon, p}(\widehat \PP_N, \mathcal{L}) = \inf_{\ell \in \mathcal{L}} ~ \mathcal{R}_{\varepsilon, p}(\widehat \PP_N, \ell).$$ Problem[eq:dro] constitutes a distributionally robust optimization problem. It seeks decisions that have minimum risk under the most adverse distributions in the ambiguity set.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Introduction", "weight": 1.5} -->

Intuitively, problem[eq:dro] can thus be viewed as a zero-sum game, where the decision-maker first selects an admissible loss function with the goal to minimize the risk, in response to which some fictitious adversary or `nature' selects a distribution from within the ambiguity set with the goal to maximize the risk. The hope is that by minimizing the worst-case risk, we actually push down the risk under all distributions in the ambiguity setin particular under the unknown true distribution $\mathds{P}$, which is contained in the ambiguity set if $\varepsilon$ is large enough. Thus, there is reason to hope that the solutions of distributionally robust optimization problems with carefully calibrated ambiguity sets display low out-of-samplerisk.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Introduction", "weight": 1.5} -->

The distributionally robust risk evaluation and decision problems [eq:worst:risk] and[eq:dro]are attractive for a multitude of diverse reasons.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Introduction", "weight": 1.5} -->

- Fidelity: Distributionally robust models are more `honest' than their nominal counterparts as they acknowledge the presence of distributional uncertainty. They also benefit from information about the type and magnitude of the estimation errors, which is conveniently encoded in the geometry and size of the ambiguity set. - Managing expectations: Due to the optimizer's curse, the solutions of nominal decision problems equipped with noisy estimators display an optimistic in-sample risk, which cannot be realized out of sample; see Example[ex:optimizers-curse]. In contrast, the solutions of distributionally robust decision problems are guaranteed to display an out-of-sample risk that falls below the worst-case optimal risk whenever the ambiguity set contains the unknown true distribution. Thus, nominal decision problems over-promise and under-deliver, while distributionally robust decision problems under-promise and over-deliver. - Computational tractability: The distributionally robust problems[eq:worst:risk] and[eq:dro] can often be reformulated as (or tightly approximated by) finite convex programs that are solvable in polynomial time. Section[sect:computation] will showcase some key tractability results.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Introduction", "weight": 1.5} -->

- Performance guarantees: For judiciously calibrated ambiguity sets, one can prove that the worst-case optimal risk for any fixed sample size $N$ provides an upper confidence bound on the out-of-sample risk attained by the optimizers of[eq:dro] (finite sample guarantee) and that the optimizers of[eq:dro] converge almost surely to an optimizer of[eq:opt:risk] as $N$ tends to infinity (asymptotic guarantee); see Section[sect:guarantees]. - Regularization by robustification: The optimizer's curse is reminiscent of overfitting phenomena that plague most statistical learning models. One can show that distributionally robust learning models equipped with a Wasserstein ambiguity set are often equivalent to regularized learning models that minimize the sum of a nominal objective and a norm term that penalizes hypothesis complexity. Similarly, one can show that some distributionally robust maximum likelihood estimation models produce shrinkage estimators. Thus, Wasserstein distributional robustness offers new probabilistic interpretations for popular regularization techniques.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Introduction", "weight": 1.5} -->

The empirical success of regularization methods in statistics fuels hope that Wasserstein distributionally robust models can effectively combat the optimizer's curse across many application areas. Connections between robustification and regularization will be explored in Section[sect:app]. - Anticipating black swans: If uncertainty is modeled by the empirical distribution, then the nominal decision problem evaluates the admissible loss functions only at the training samples. However, possible future uncertainty realizations that differ from all training samples but could have devastating consequences (`black swans') are ignored. If the empirical distribution may be perturbed within a Wasserstein ball with a positive radius, on the other hand, then (possibly small amounts of) probability mass can be moved anywhere in the support set$\Xi$. Thus, the Wasserstein distributionally robust decision problem faithfully anticipates the possibility of black swans. We emphasize that all distributions in a Kullback-Leibler divergence ball must be absolutely continuous with respect to the nominal distribution, which implies that the corresponding distributionally robust decision problems ignore the possibility of black swans.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Introduction", "weight": 1.5} -->

- Axiomatic justification: If the random vector $\xi$ may follow any distribution in some ambiguity set $\mathcal Q$ (e.g., a Wasserstein ball), then the scalar random variable $\ell(\xi)$ corresponding to a fixed loss function $\ell\in\mathcal{L}$ may follow any distribution in the induced ambiguity set $\ell_*(\mathcal Q)=\{\ell_*(\mathds{Q}): \mathds{Q}\in\mathcal Q\}$, where $\ell_*(\mathds{Q})$ is the pushforward measure of $\mathds{Q}$ under $\ell$. We call a loss function $\ell\in\mathcal{L}$ unambiguous if $\ell_*(\mathcal Q)$ is a singleton.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Introduction", "weight": 1.5} -->

Assume now that $\ell$ is preferred to $\ell'$ under any of the following natural conditions: (i)$\ell$ and $\ell'$ are unambiguous, and $\mathcal{R}(\mathds{Q},\ell)\le\mathcal{R}(\mathds{Q},\ell')$ for some $\mathds{Q}\in\mathcal Q$; (ii)$\ell_*(\mathcal Q)\subseteq \ell'_*(\mathcal Q)$; (iii)$\mathcal{R}(\mathds{Q},\ell)\le \mathcal{R}(\mathds{Q},\ell')$ for every $\mathds{Q}\in\mathcal Q$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Introduction", "weight": 1.5} -->

Under a mild technical condition, the loss functions must then be ranked by the worst-case risk $\sup_{\mathds{Q}\in\mathcal Q}\mathcal{R}(\mathds{Q},\ell)$ [delage2019dicesion]. This result provides an axiomatic justification for adopting a distributionally robust approach. - Optimality principle: Data-driven optimization aims to use the training data directly to construct an estimator for the objective of problem[eq:opt:risk] (a predictor) and a decision that minimizes this predictor (a prescriptor) without the detour of constructing an estimator for $\mathds{P}$. It has been shown that optimal predictors and the corresponding prescriptors can be constructed by solving a meta-optimization model that minimizes the in-sample risk of the predictor-prescriptor pairs subject to constraints guaranteeing that the in-sample risk is actually attainable out of sample.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Introduction", "weight": 1.5} -->

It has been shown that this meta-optimization problem admits a unique solution: the best predictor-prescriptor pair is obtained by solving a distributionally robust optimization problem over all distributions in some neighborhood of the empirical distribution [vanparys2019optimal]. Thus, if one aims to transform training data to decisions, it is in some precise sense optimal to do this by solving a data-driven distributionally robust optimization problem.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Introduction", "weight": 1.5} -->

Distributionally robust optimization models with Wasserstein ambiguity sets were introduced in [pflug2007ambiguity]. Reformulations of these models as nonconvex optimization problems as well as initial attempts to solve these problems via algorithms from global optimization are reported in [wozabal2012framework] and [pflug2014multistage]. In the next section we will review convex reformulations and approximations that were discovered in[esfahani2018data, zhao2018data] and significantly generalized in[blanchet2016quantifying, gao2016distributionally].

<!-- chunk {"id": "body-0053", "role": "body", "section": "Introduction", "weight": 1.5} -->

The conjugate of a function $\ell(\xi)$ on $\mathbb{R}^m$ is defined as $\ell^*(z) = \sup_{\xi} z^\top \xi - \ell(\xi)$. The indicator function of a set $\Xi \subseteq \mathbb{R}^m$ is defined as $\delta_\Xi(\xi) = 0$ if $\xi \in \Xi$ and $\delta_\Xi(\xi)= \infty$ if $\xi\notin\Xi$. The conjugate $\sigma_\Xi(z) = \sup_{\xi \in \Xi} z^\top \xi$ of the indicator function is termed the support function. If $ \| \xi \| $ represents the norm of$\xi\in\mathbb{R}^m$, then $ \| z \|_* =\sup_{\| \xi \| \leq 1} z^\top \xi$ denotes the corresponding dual norm.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Introduction", "weight": 1.5} -->

The set of all symmetric (positive semidefinite) matrices $A \in \mathbb{R}^{m \times m}$ is denoted by$\mathbb{S}^m$ ($\mathbb{S}_{+}^m$). For $A,B\in\mathbb S^m$, the relation $A\succeq B$ ($A\succ B$) means that $A-B$ is positive semidefinite (positive definite). The trace of $A\in \mathbb{R}^{m \times m}$ is denoted by $\Tr{A}$, the smallest and largest eigenvalues of $A \in \mathbb{S}^m$ are denoted by $\lambda_{\min}(A)$ and $\lambda_{\max}(A)$, respectively, and the Moore-Penrose pseudoinverse of $A \in \mathbb{S}_{+}^m$ is denoted by $A^\dagger$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Computation", "weight": 1.0} -->

The aim of this section is to show that the worst-case risk evaluation problem[eq:worst:risk] and the distributionally robust decision problem[eq:dro] are computationally tractable in many situations of practical interest. Note first that checking whether a fixed distribution $\mathds{Q}$ is feasible in[eq:worst:risk] requires computing the Wasserstein distance $W_p(\mathds{Q},\widehat \PP_N)$. It is therefore instructive to study the complexity of evaluating Wasserstein distances between arbitrary distributions.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Computation", "weight": 1.0} -->

Computing the Wasserstein distance between two discrete distributions amounts to solving a tractable linear program that is susceptible to the network simplex algorithm [bertsekas1998network] as well as dual ascent methods[bertsimas1997introduction] or specialized auction algorithms[bertsekas1981new, bertsekas1992auction], etc. The set of feasible transportation plans is termed the transportation polytope and displays many useful theoretical properties, which are surveyed in[brualdi2006combinatorial]. The need to evaluate Wasserstein distances between increasingly fine-grained histograms has recently motivated efficient approximation schemes. When augmented with an entropic regularization term, for instance, the finite-dimensional transportation problem can be solved quickly by using Sinkhorn's algorithm[chizat2018scaling, cuturi2013sinkhorn, karlsson2017generalized, peyre2015entropic, peyre2017quantum, schmitzer2016sparse, solomon2015convolutional].

<!-- chunk {"id": "body-0057", "role": "body", "section": "Computation", "weight": 1.0} -->

Variants of this approach use Tikhonov regularizers[essid2018quadratically], Bregman divergences[benamou2015iterative] or Tsallis entropies[muzellec2017tsallis] instead of the entropic regularization term. A survey of algorithms for the finite-dimensional transportation problem is provided in[peyre2018computational].

<!-- chunk {"id": "body-0058", "role": "body", "section": "Computation", "weight": 1.0} -->

As soon as at least one of the two involved distributions ceases to be discrete, the Wasserstein distance can no longer be evaluated in polynomial time. Even in the simplest imaginable scenario where one distribution is uniform on a hypercube and the other distribution is discrete with two atoms, computing the Wasserstein distance becomes intractable Computing the type-$p$ Wasserstein distance between two distributions $\mathds{Q}$ and $\mathds{Q}'$ is #P-hard even if $\|\cdot\|$ is the Euclidean norm, $\mathds{Q}$ is the uniform distribution on the standard hypercube $^m$, and $\mathds{Q}'$ is a discrete distribution supported on only two points. $p=2$ and $\|\cdot\|$ is the Euclidean norm, then the Wasserstein distance admits an analytical lower bound that depends only on the distributions' first- and second-order moments. This bound is available for anypair of distributions even if their exact Wasserstein distance cannot be computed efficiently. Moreover, the bound is exact for elliptical distributions.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Computation", "weight": 1.0} -->

[eq:gelbrich-bound] may be loose if $\mathds{Q}$ and $\mathds{Q}'$ are elliptical distributions with different density generators. Maybe unexpectedly, however, the Wasserstein distance between two elliptical distributions with the same density generator $g$ is actually independent of $g$. In its general form, Theorem[theorem:gelbrich] is due to Gelbrich[gelbrich1990formula]. The exact formula for the type-2 Wasserstein distance between normal distributions has been discovered earlier in [dowson1982frechet, givens1984class, olkin1982distance].

<!-- chunk {"id": "body-0060", "role": "body", "section": "Computation", "weight": 1.0} -->

As any Wasserstein ball with a strictly positive radius contains non-discrete distributions (the nominal distribution can be smeared out even if the transportation budget is small), it is perhaps surprising that the worst-case risk evaluation problem [eq:worst:risk] may be tractable at all. Indeed, Theorem[theorem:hard] indicates that checking feasibility is already hard in general. We will see below, however, that the extremal distributions determining the worst-case risk are often structurally equivalent to the nominal distribution. Thus, there is hope that problems[eq:worst:risk] and[eq:dro] become tractable if we choose a nominal distribution with a particularly simple structure (e.g., a discrete or an elliptical distribution).

<!-- chunk {"id": "body-0061", "role": "body", "section": "Computation", "weight": 1.0} -->

In order to ensure that any admissible loss function $\ell\in\mathcal{L}$ has a finite expected value under the nominal distribution, we impose the following technical regularity condition borrowed from[blanchet2016quantifying], which will tacitly be assumed to hold throughout the rest of the paper.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Computation", "weight": 1.0} -->

Any loss function $\ell \in \mathcal{L}$ is upper semicontinuous and integrable with respect to the nominal distribution $\widehat \PP_N$, that is, $ \int_{\mathbb{R}^m} |\ell(\xi)| \, \widehat \PP_N(\diff \xi) < \infty. $ In the remainder of this section, we will first review tractable bounds on the worst-case risk and present a strong duality result that paves the way towards exact tractable reformulations (Section[sec:wc-risk-any-p]). Next, we will delineate efficient methods to compute the worst-case risk as well as the underlying worst-case distributions in situations when the nominal distribution is discrete (Section[sec:wc-risk-empirical]) or elliptical (Section[sec:wc-risk-elliptical]).

<!-- chunk {"id": "body-0063", "role": "body", "section": "General Analysis of the Worst-Case Risk", "weight": 1.0} -->

Before attempting to derive exact tractable reformulations for the worst-case risk[eq:worst:risk], we focus on the simpler task of establishing efficiently computable upper and lower bounds. To derive a pessimistic upper bound, we note that the transportation cost $\|\xi-\xi'\|^p$ is a convex function of the random variable $\|\xi-\xi'\|$ for any $p\ge 1$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "General Analysis of the Worst-Case Risk", "weight": 1.0} -->

Jensen's inequality thus implies $$W_p(\mathds{Q}, \widehat \PP_N) \geq W_1(\mathds{Q}, \widehat \PP_N) \quad \forall \mathds{Q}\in\mathcal P(\Xi)\quad \implies \quad \mathbb{B}_{\varepsilon,p}(\widehat \PP_N) \subseteq \mathbb{B}_{\varepsilon,1}(\widehat \PP_N).$$ Hence, the worst-case risk of a loss function $\ell\in\mathcal{L}$ over the type-$p$ Wasserstein ball satisfies \mathcal{R}_{\varepsilon, p}(\widehat \PP_N, \ell) \leq \mathcal{R}_{\varepsilon, 1}(\widehat \PP_N, \ell) &= \mathds{E}^{\widehat

<!-- chunk {"id": "body-0065", "role": "body", "section": "General Analysis of the Worst-Case Risk", "weight": 1.0} -->

\PP_N}[\ell(\xi)] + \sup_{\mathds{Q}\in \mathbb{B}_{\varepsilon,1}(\widehat \PP_N) } \mathds{E}^{\mathds{Q}}[\ell(\xi)] - \mathds{E}^{\widehat \PP_N}[\ell(\xi)] \\& \le \mathcal{R}(\widehat \PP_N, \ell) + \varepsilon\cdot \Lip(\ell), where the equality follows from the definition of the worst-case risk, while the second inequality is a direct consequence of the Kantorovich-Rubinstein theorem (see Theorem[thm:kantorovich-rubinstein]). We summarize the above reasoning in the following theorem.

<!-- chunk {"id": "body-0066", "role": "body", "section": "General Analysis of the Worst-Case Risk", "weight": 1.0} -->

The worst-case risk[eq:worst:risk] of any fixed loss function $\ell\in\mathcal{L}$ is bounded above by the Lipschitz-regularized nominal risk, that is, $$\mathcal{R}_{\varepsilon, p}(\widehat \PP_N, \ell) \leq \mathcal{R}(\widehat \PP_N, \ell) + \varepsilon\cdot \Lip(\ell).$$ If the loss function $\ell$ fails to be Lipschitz continuous (i.e., $\Lip(\ell) = \infty$), then Theorem[theorem:lipschitz] is trivially satisfied. Note that $\mathcal{R}(\widehat \PP_N, \ell)$ is linear in $\ell$ for any choice of the nominal distribution and that $\Lip(\ell)$ is a convex function of $\ell$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "General Analysis of the Worst-Case Risk", "weight": 1.0} -->

Thus, minimizing the upper bound of Theorem[theorem:lipschitz] amounts to solving a convex optimization problem whenever $\mathcal{L}$is a convex set.

<!-- chunk {"id": "body-0068", "role": "body", "section": "General Analysis of the Worst-Case Risk", "weight": 1.0} -->

An optimistic lower bound on the worst-case risk can be obtained by replacing the Wasserstein ball in [eq:worst:risk] with a smaller ambiguity set. If the distributions in the restricted Wasserstein ball admit a finite parameterization, then the lower bounding problem coincides with a finite optimization problem. Depending on the parameterization, this problem may even be convex. If $\widehat \PP_N$ is the empirical distribution, for example, one may restrict the original Wasserstein ball to a subset that contains only perturbed empirical distributions of the form $$\mathds{Q}(\Theta) = \frac{1}{N} \sum_{i=1}^N \delta_{\widehat \xi_i+\theta_i},$$ where $\theta_i\in\mathbb{R}^m$ is the displacement of the $i^{\rm th}$ training sample.

<!-- chunk {"id": "body-0069", "role": "body", "section": "General Analysis of the Worst-Case Risk", "weight": 1.0} -->

Thus, all distributions in the restricted Wasserstein ball are encoded by a perturbation matrix $\Theta=(\theta_1,\ldots, \theta_N)\in\mathbb{R}^{m\times N}$. The requirement that $\mathds{Q}(\Theta)\in\mathcal P(\Xi)$ translates to $\widehat \xi_i + \theta_i \in \Xi$ for all $i\in[N]$, while the Wasserstein constraint $W_p(\mathds{Q}(\Theta),\widehat \PP_N)\le \varepsilon$ is equivalent to the inequality $\frac{1}{N} \sum_{i=1}^N \| \theta_i \|^p \leq \varepsilon^p$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "General Analysis of the Worst-Case Risk", "weight": 1.0} -->

If $\widehat \PP_N$ is the empirical distribution, then the worst-case risk[eq:worst:risk] of any fixed loss function $\ell\in\mathcal{L}$ is bounded below by the worst-case empirical loss, where the worst case is taken over all perturbation matrices $\Theta=(\theta_1,\ldots, \theta_N)\in\mathbb{R}^{m\times N}$ of the training samples in an $L_{p,1}$-norm uncertainty set, that is, we have \mathcal{R}_{\varepsilon, p}(\widehat \PP_N, \ell) ~\geq ~\sup & \DS \frac{1}{N} \sum_{i=1}^N \ell(\widehat \xi_i + \theta_i) \\ [3ex] \st & \theta_i \in \mathbb{R}^m & \forall i \in [N] \\ [0.5em] & \widehat

<!-- chunk {"id": "body-0071", "role": "body", "section": "General Analysis of the Worst-Case Risk", "weight": 1.0} -->

Note that if the loss function $\ell$ is concave, then the robust lower bounding problem of Theorem[thm:robust-lb] constitutes a finite convex optimization problem. In the remainder we will argue that both the upper bound of Theorem[theorem:lipschitz] as well as the lower bound of Theorem[thm:robust-lb] can become exact in situations of practical interest. To see this, we first derive the Lagrangian dual of the worst-case risk evaluation problem[eq:worst:risk].

<!-- chunk {"id": "body-0072", "role": "body", "section": "General Analysis of the Worst-Case Risk", "weight": 1.0} -->

The worst-case risk[eq:worst:risk] of any fixed $\ell\in\mathcal{L}$ satisfies $$\mathcal{R}_{\varepsilon, p}(\widehat \PP_N, \ell) = \inf_{\gamma \ge 0} ~ \mathds{E}^{\widehat \PP_N} \left[\ell_\gamma(\xi) \right] + \gamma \varepsilon^p,$$ where $ \ell_\gamma(\xi) = \sup_{z \in\Xi} ~ \ell(z) - \gamma \| z - \xi \|^p$ is a Moreau-Yosida regularization[parikh2014proximal] of $\ell(\xi)$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "General Analysis of the Worst-Case Risk", "weight": 1.0} -->

The minimization problem on the right hand side of [eq:strong-duality] can indeed be identified with the strong Lagrangian dual of problem[eq:worst:risk], where $\gamma\ge 0$ is the Lagrange multiplier of the Wasserstein constraint $W_p(\mathds{Q},\widehat \PP_N)\le \varepsilon$. We emphasize that the Moreau-Yosida regularization $\ell_\gamma(\xi)$ is jointly convex in $\gamma$ and $\ell$ for every fixed uncertainty realization $\xi$. Thus the dual problem[eq:strong-duality] represents a convex minimization problem whose optimal value is convex in$\ell$. One can further show that[eq:strong-duality] is solvable for any $\varepsilon>0$ under the mild assumption that there exists $C>0$ such that $|\ell(\xi)|\le C(1+\|\xi\|^p)$ for all $\xi\in\Xi$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "General Analysis of the Worst-Case Risk", "weight": 1.0} -->

For type-1 Wasserstein balls centered at the empirical distribution, Theorem[theorem:robust] is a corollary of [esfahani2018data] and [zhao2018data]. An extension of Theorem[theorem:robust] to situations where$\xi$ ranges over a Polish space is discussed in [blanchet2016quantifying, gao2016distributionally]. It has been shown that Theorem[theorem:robust] remains even valid if the transportation cost $\|\xi-\xi'\|^p$ in the definition of the Wasserstein distance is replaced with a general nonnegative and lower semicontinuous function $c(\xi, \xi')$ that vanishes if and only if$\xi = \xi'$ [blanchet2016quantifying]. Note that the Wasserstein distance may cease to be a metric in this case.

<!-- chunk {"id": "body-0075", "role": "body", "section": "General Analysis of the Worst-Case Risk", "weight": 1.0} -->

In the next sections we will describe specific settings in which [eq:worst:risk] and[eq:strong-duality]are tractable.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

Assume now that the Wasserstein ambiguity set is centered at the empirical distribution defined in[eq:empirical]. In this case, under a mild convexity assumption, the worst-case risk[eq:worst:risk]can be exactly expressed as the optimal value of a finite convex optimization problem.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

The assumptions of Theorem [thm:type1] are unrestrictive because any continuous function $\ell(\xi)$ on a compact set $\Xi$ can be uniformly approximated as closely as desired by a pointwise maximum of finitely many concave functions. Note that the loss function$\ell(\xi)$ and the support set$\Xi$ enter problem[eq:peyman] through the conjugates of the negative constituent functions $-\ell_j(\xi)$, $j\in[J]$, and the support function$\sigma_\Xi(z)$, all of which are convex. Moreover, the norm that determines the transportation cost in the definition of the Wasserstein distance enters[eq:peyman] via the dual norm$\|\cdot\|_*$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

The term $\gamma \| u_{ij}/\gamma \|_*^q$ can be identified with the perspective function of $\|u_{ij}\|_*^q$ and is thus jointly convex in $\gamma$ and $u_{ij}$ [boyd2004convex]. Therefore, problem[eq:peyman] is manifestly convex. Tables[table:conjugate][table:norm] in Appendix[sect:functions] list common conjugates, support functions and dual norms. By substituting[eq:peyman] into[eq:dro], one can reformulate the distributionally robust decision problem[eq:dro] as a single explicit minimization problem, which is convex whenever $\mathcal{L}$ is a convex set. To prove Theorem[thm:type1], one re-expresses the empirical expectation in the objective function of the dual problem[theorem:robust] as a finite sum and dualizes the maximization problems in the Moreau-Yosida regularization terms.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

For further details see[esfahani2018data] and [zhen2019distributionally].

<!-- chunk {"id": "body-0080", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

\end{array}\right.$$ For $p=1$, the constraints of the finite convex program[eq:peyman] are thus equivalent to $$\DS [-\ell_j]^* (u_{ij} - v_{ij}) + \sigma_\Xi(v_{ij}) - u_{ij}^\top \widehat \xi_i \leq s_i,\quad \|u_{ij}\|_*\le \gamma \quad \forall i\in[N],\; j \in [J].$$ In the opposite limit when $p$ tends to $\infty$ and $q$ to 1, the function $\varphi(q)$ converges to 1. One can then show that $\gamma=0$ at optimality and that the constraints of problem[eq:peyman] simplifyto $$\DS [-\ell_j]^* (u_{ij} - v_{ij}) + \sigma_\Xi(v_{ij})

<!-- chunk {"id": "body-0081", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

- u_{ij}^\top \widehat \xi_i + \varepsilon \left\| u_{ij} \right\|_* \leq s_i \quad \forall i\in[N],\; j \in [J].$$ We refer to [wang2022mean] for a formal proof.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

As it expresses the worst-case risk $\mathcal{R}_{\varepsilon, p}(\widehat \PP_N, \ell)$ as the optimal value of a minimization problem, Theorem[thm:type1] primarily serves as a vehicle to solve the distributionally robust decision problem[eq:dro]. In order to construct an extremal distribution that solves problem[eq:worst:risk], one may dualize the finite convex program[eq:peyman] to convert it back to a maximizationproblem.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

Similarly, the constraint $\widehat \xi_i + \theta_{ij}/0 \in \Xi$ means that $\theta_{ij}$ belongs to the recession cone of $\Xi$, and $0 \|\theta_{ij}/0\|^p$ is interpreted as $\lim_{\alpha_{ij}\downarrow 0} \alpha_{ij} \| \theta_{ij}/\alpha_{ij}\|^p$. [dual-dual] is the Lagrangian dual of[eq:peyman] and thus convex by construction. Convexity can also be verified directly. As the constituent functions $\ell_j(\xi)$, $j\in[J]$, are concave by assumption, the objective of[dual-dual] represents a sum of concave perspective functions and is thus concave [boyd2004convex].

<!-- chunk {"id": "body-0084", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

Also, the support constraints $\widehat \xi_i +\theta_{ij}/\alpha_{ij}\in \Xi$ require that$(\theta_{ij}, \alpha_{ij})$ belongs to the preimage of the convex set $\{\widehat \xi_i +\xi:\xi\in \Xi\}$ under the perspective transformation, which is known to be convex [boyd2004convex]. The term $\alpha_{ij} \| \theta_{ij}/\alpha_{ij} \|^p$ can be identified with the perspective function of $\|\theta_{ij}\|^p$ and is thus jointly convex in $\alpha_{ij}$ and $\theta_{ij}$[boyd2004convex].

<!-- chunk {"id": "body-0085", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

For a proof of Theorem [thm:type1:extrem] we refer to [esfahani2018data] and [zhen2019distributionally]. We emphasize that problem[dual-dual]is always solvable because it has a compact feasible set and an upper semicontinuous objective function, and thus the use of the maximization operator is justified. $J=1$, then the loss function $\ell(\xi)=\ell_1(\xi)$ is globally concave, and the penultimate constraint group in[dual-dual] simplifies to the requirement that $\alpha_{i1}=1$ for every $i\in[N]$. In this case, the convex program[dual-dual], which is equivalent to the worst-case risk evaluation problem[eq:worst:risk], reduces to the robust optimization problem[eq:robust], which maximizes only over perturbed empirical distributions in the Wasserstein ball.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

Thus, the robust lower bound portrayed in Theorem[thm:robust-lb] is exact if the loss function $\ell(\xi)$is concave.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

For $p=1$, the last constraint of[dual-dual] simplifies to $$\DS \frac{1}{N} \sum_{i=1}^N \sum_{j=1}^J \left\| \theta_{ij}\right\| \leq \varepsilon.$$ To analyze the limit when $p$ tends to $\infty$, we divide the last constraint of[dual-dual] by $\varepsilon^p$ and observe that $\| \theta_{ij}/(\varepsilon \, \alpha_{ij}) \|^p$ grows exponentially with $p$ if $\|\theta_{ij}/\alpha_{ij}\|> \varepsilon$. Otherwise, $\| \theta_{ij}/(\varepsilon \, \alpha_{ij}) \|^p$ remains bounded by 1 for all $p$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

For $p=\infty$, the last constraint of[dual-dual] is therefore equivalent to the requirement that $\|\theta_{ij}\|\le \varepsilon \,\alpha_{ij}$ for all $i\in [N]$ and $j\in[J]$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

An intimate connection between distributionally robust optimization with type- $\infty$ Wasserstein balls and classical robust optimization has first been discovered in[sturt2018data-driven].

<!-- chunk {"id": "body-0090", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

Even though problem [dual-dual] is guaranteed to have an optimal solution, the worst-case risk[eq:worst:risk] may not be attained by any distribution if $p=1$. An instance of problem[eq:worst:risk] that fails to be solvable is constructed in Example[eq:non-existence] below, which replicates[esfahani2018data]. [Non-existence of extremal distributions] Assume that $p=1$, $\Xi = \mathbb{R}$, $N = 1$ and $\widehat \xi_1 = 0$ implying that the nominal distribution $\widehat \PP_1$ reduces to the Dirac distribution at$0$. Set the norm on $\mathbb{R}$ to the absolute value $|\cdot|$, and set $\ell(\xi) = \max \{ 0, \xi-1 \}$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

As $\Lip(\ell)=1$, Theorem[theorem:lipschitz] implies that $\mathcal{R}_{\varepsilon, 1}(\widehat \PP_1, \ell) \le \varepsilon$. Next, define $\mathds{Q}_n = (1 - 1 /n) \, \delta_{0} + (1 / n) \, \delta_{\varepsilon n} $ for $n \in \mathbb N$, and note that the type-1 Wasserstein distance between $\mathds{Q}_n$ and $\widehat \PP_1$ amounts to$\varepsilon$, which is the cost of moving mass $1/n$ from $\varepsilon n$ to $0$. Thus, $\mathds{Q}_n\in\mathbb{B}_{\varepsilon,1}(\widehat \PP_1)$.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

Moreover, we have $\mathds{E}^{\mathds{Q}_n}[\ell(\xi)]=\max\{0,\varepsilon-1/n\}$, which implies that $\mathds{Q}_n$ attains the upper bound $\varepsilon$ on the worst-case risk asymptotically as $n$ tends to infinity. Thus, the sequence $\mathds{Q}_n$, $n\in\mathbb N$, is asymptotically optimal in[eq:worst:risk]. Next, we argue that the worst-case risk $\varepsilon$ is not attained. Suppose to the contrary that there exists $\mathds{Q}^\star \in \mathbb{B}_{\varepsilon, 1}(\widehat \PP_1)$ with $\mathds{E}^{\mathds{Q}^\star}[\ell(\xi)] = \varepsilon$.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

Thus, $\varepsilon = \mathds{E}^{\mathds{Q}^\star}[\ell(\xi)] < \mathds{E}^{\mathds{Q}^\star}[|\xi|] \leq \varepsilon$ where the strict inequality follows from the observation that $\ell(\xi) < |\xi|$ for any $\xi \neq 0$ and that $\mathds{Q}^\star \neq \delta_{0}$, and the second inequality follows from Theorem[thm:kantorovich-rubinstein] and the assumption that $\mathds{Q}^\star \in \mathbb{B}_{\varepsilon, 1}(\widehat \PP_1)$. The contradiction implies that $\mathds{Q}^\star$ cannot exist, and thus[eq:worst:risk] is not solvable.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

Fix now any maximizer $\{\alpha_{ij}^\star,\theta_{ij}^\star\}_{i,j}$ of problem[dual-dual]. This maximizer can be used to construct an extremal distribution $\mathds{Q}^\star$ that solves problem[eq:worst:risk] (if such a $\mathds{Q}^\star$ exists) or a sequence of asymptotically optimal distributions $\{\mathds{Q}_n\}_{n\in\mathbb N}$ (if such a $\mathds{Q}^\star$ does not exist). Before describing this construction, we remark that $\theta_{ij}^\star$ is a recession direction of the support set$\Xi$ whenever $\alpha_{ij}^\star=0$ (i.e., $\widehat\xi_i+t \, \theta_{ij}^\star\in\Xi$ for every $t\ge 0$).

<!-- chunk {"id": "body-0095", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

Thus, for $p>1$, the worst-case risk[eq:worst:risk] of a piecewise concave loss function is always attained by the discrete distribution $\mathds{Q}^\star$constructed above. $\nu_\infty\neq\emptyset$, which is only possible in the special case $p=1$, the distributions $$\mathds{Q}_n = \DS \sum_{(i,j)\in\nu_+\cup \nu_\infty} \!\!\!

<!-- chunk {"id": "body-0096", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

Intuitively, these distributions send some atoms with decaying probabilities to infinity along specific recession directions $\theta_{ij}^\star$, $(i,j)\in\nu_\infty$, of the support set. Note that moving an atom to infinity is possible even when only a finite (type-1) transportation budget is available provided that the probability mass transported is inversely proportional to the transportation distance. $p>1$, atoms can also migrate to infinity at a finite transportation cost provided that their probabilities are inversely proportional to the $p^{\rm th}$ power of the transportation distance. As piecewise concave loss functions grow at most linearly, however, the decay in probability always outweighs the increase in loss. This reasoning provides an intuitive explanation for our insight that $\nu_\infty=\emptyset$ and that the supremum in[eq:worst:risk] is always attained for$p>1$.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

Given the promising results for piecewise concave loss functions, it is natural to ask whether the convex reformulations of Theorems [thm:type1] and[thm:type1:extrem] can be generalized. Indeed, it has been discovered that similar results are available for convex (but not piecewise convex) loss functions under the additional condition that there are no support constraints ($\Xi=\mathbb{R}^m$).

<!-- chunk {"id": "body-0098", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

Assume that $ \Xi = \mathbb{R}^m$ and that the loss function $\ell(\xi)$ is convex. If $p=1$ and $\widehat \PP_N$ is the empirical distribution, then the worst-case risk[eq:worst:risk] coincides with the Lipschitz-regularized empirical loss, that is, $$\mathcal{R}_{\varepsilon, 1}(\widehat \PP_N, \ell) = \mathcal{R}(\widehat \PP_N, \ell) + \varepsilon \Lip(\ell).$$ For a proof of this result we refer to [esfahani2018data]. Theorem[thm:type1:convex] shows that the simple upper bound of Theorem[theorem:lipschitz] is exact if $p=1$, $\Xi=\mathbb{R}^m$ and the loss function $\ell$is convex.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

By Theorem[thm:type1:convex], computing the worst-case risk of a convex loss function $\ell(\xi)$ requires computing the Lipschitz modulus of$\ell(\xi)$ with respect to the prescribed norm $\|\cdot\|$ on $\mathbb{R}^m$. One can show that $$\Lip(\ell) = \sup \left\{ \|z\|_*: \ell^*(z)<\infty \right\},$$ that is, the Lipschitz modulus of $\ell(\xi)$ coincides with the radius of the smallest dual norm ball around 0 that encloses the domain of the conjugate loss function $\ell^*(z)$ [esfahani2018data]. Unfortunately, problem[eq:lipschitz-computation] maximizes a convex function over a convex set and is therefore hard.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

In order to compute the Lipschitz modulus of $\ell(\xi)$ with respect to the $\infty$-norm, for example, we thus need to solve an instance of problem[eq:lipschitz-computation] that maximizes the 1-norm over $\mathcal E$. As maximizing the 1-norm over an arbitrary ellipsoid is NP-hard [hanasusanto2015distributionally], we conclude that the worst-case risk evaluation problem[eq:worst:risk] is intractable even for polyhedral norms and for simple classes of (convex) conic quadratic loss functions.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

One can show that the supremum of the worst-case risk evaluation problem [eq:worst:risk] is never attained under the conditions of Theorem[thm:type1:convex], that is, any asymptotically optimal sequence of distributions must push some (decreasing amount of) probability mass to infinity. As in the case of a piecewise concave loss function, such a sequence can be constructed explicitly. To do so, choose a maximizer $z^\star$ of problem[eq:lipschitz-computation], which is generally intractable as pointed out in Remark[rem:lipschitz]. Moreover, select $i_0 \in [N]$ and $\xi^\star\in\arg\max_{\| \xi \| \leq 1} \xi^\top z^\star$.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

Assume next that $p=2$, the loss function $\ell(\xi)$ is quadratic and the transportation cost in the definition of the Wasserstein distance is induced by the Euclidean norm. Then, the worst-case risk[eq:worst:risk] coincides with the optimal value of a tractable semidefinite program(SDP).

<!-- chunk {"id": "body-0103", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

Assume that $\Xi = \mathbb{R}^m$ and that $\ell(\xi) = \xi^\top Q \xi + 2 q^\top \xi$ with $Q \in \mathbb S^m$ and $q \in \mathbb{R}^m$ is a (possibly indefinite) quadratic loss function.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

If $p = 2$, $\| \cdot\| = \| \cdot \|_2$ is the Euclidean norm on $\mathbb{R}^m$ and $\widehat \PP_N$ is the empirical distribution, then the worst-case risk[eq:worst:risk] coincides with the optimal value of a tractable SDP, that is, $$\optimize{\mathcal{R}_{\varepsilon, 2}(\widehat \PP_N, \ell) ~=~ \inf & \DS \gamma \varepsilon^2 + \frac{1}{N} \sum_{i=1}^N s_i \\\st & \gamma \in \mathbb{R}_+, \; s_i \in \mathbb{R} & \forall i \in [N] \\[1mm] \gamma I - Q & q + \gamma \widehat \xi_i \\ q^\top + \gamma \widehat \xi_i^\top & ~ s_i +\gamma

<!-- chunk {"id": "body-0105", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

\| \widehat \xi_i \|_2^2 \end{bmatrix} \succeq 0 & \forall i \in [N]\,.}$$ Note that substituting the SDP [eq:soroosh-convex] into the distributionally robust decision problem[eq:dro] yields a tractable SDP if the set $\mathcal{L}$ of admissible loss functions is defined through SDP constraints in $Q$ and $q$.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

In order to construct an extremal distribution that solves problem[eq:worst:risk] for a fixed convex quadratic loss function, it is useful to derive the dual of the SDP[eq:soroosh-convex].

<!-- chunk {"id": "body-0107", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

Suppose that all conditions of Theorem[theorem:convex:quadratic] hold.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

}$$ [eq:soroosh-convex-dual] represents a quadratically constrained quadratic program (QCQP) with a compact feasible set and is therefore solvable. As $Q$ is not necessarily negative semidefinite, problem[eq:soroosh-convex-dual] is generally nonconvex. This is perhaps puzzling because[eq:soroosh-convex-dual] is obtained by `massaging' the dual of[eq:soroosh-convex] and because dual optimization problems are convex by construction. The apparent contradiction is resolved by noting that nonconvex QCQPs of the form[eq:soroosh-convex-dual] with a single constraint are equivalent to convex SDPs by virtue of the celebrated $\mathcal S$-procedure [boyd2004convex]. [eq:soroosh-convex-dual] can be interpreted as a finite reduction of the worst-case risk evaluation problem[eq:worst:risk], which maximizes only over discrete distributions in the Wasserstein ball.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

Denoting by $v_{\rm max}(Q)$ an eigenvector corresponding to $\lambda_{\rm max}(Q)$, any such discrete distribution assigns probability $1/N$ to the perturbed training samples $\widehat \xi_i+ \theta_i$, $i\in[N]$, and a `vanishing' probability to an atom located `infinitely' far away in the direction of$v_{\rm max}(Q)$. More precisely, the product of the squared transportation distance and the probability of this last atom must converge to a finite value$\alpha\in\mathbb{R}_+$ (hence, the probability of this atom must be asymptotically proportional to the inverse of the squared transportation distance).

<!-- chunk {"id": "body-0110", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

The structure of the extremal distributions for the worst-case risk evaluation problem [eq:worst:risk] with general loss functions and nominal distributions as well as necessary and sufficient conditions for their existence have been studied in[gao2016distributionally, owhadi2017extreme, wozabal2012framework]. The special case of a Wasserstein ball centered at a discrete distribution with $N$ atoms has undergone particular scrutiny. Considerable effort was spent on proving the existence of discrete extremal distributions with as few atoms as possible. A first breakthrough was marked by the insight that the worst-case risk of any continuous bounded loss function is attained by a discrete distribution with at most $N+3$ atoms [wozabal2012framework].

<!-- chunk {"id": "body-0111", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

As any $(N+3)$-point distribution on $\mathbb{R}^m$ can be encoded by $(N+3)\cdot(m + 1)-1$ parameters (i.e., the coordinates and probabilities of the $N+3$ atoms), this result motivates a finite reduction: when searching for an extremal distribution, one may restrict attention to discrete distributions supported on $N+3$ points, which amounts to searching a finite-dimensional parameter space. It was later shown that one may actually focus on discrete distributions with $N+2$ atoms[owhadi2017extreme] or even only $N+1$ atoms[gao2016distributionally] without sacrificing optimality. These sharper results facilitate more parsimonious finite reductions that may be fruitfully used in algorithm design. Exact finite reductions involving fewer atoms are available only in special cases. For example, the discussion after Theorem[thm:type1:extrem] shows that the worst-case risk of a concave loss function is always attained by an $N$-point distribution.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

For more general loss functions, however, every $N$-point distribution may be suboptimal even if the worst-case risk is attained. [Non-existence of extremal distributions with $N$ atoms] Suppose that $\Xi = (-\infty, 2] $, $N = 1$ and $\widehat \xi_1 = 0$, which implies that $\widehat \PP_1$ is the Dirac distribution at$0$. Set the norm on $\mathbb{R}$ to the absolute value $|\cdot|$, select $\varepsilon\in$ and set $\ell(\xi) = \max \{ 0, \xi-1 \}$.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

Next, define $\mathds{Q}^\star = (1 - \varepsilon / 2) \, \delta_{0} + (\varepsilon / 2) \, \delta_{2} $, and note that the type-1 Wasserstein distance between $\widehat \PP_1$ and $\mathds{Q}^\star$ amounts to $\varepsilon$, which is the cost of moving mass $\varepsilon/2$ from 2 to 0. Thus, $\mathds{Q}^\star\in \mathbb{B}_{\varepsilon,1}(\widehat \PP_1)$. Moreover, we have $\mathds{E}^{\mathds{Q}^\star}[\ell(\xi)]= \varepsilon/2$, which provides a lower bound on the worst-case risk. In fact, by solving problem[dual-dual] one can show that $\mathds{Q}^\star$ is optimal in[eq:worst:risk].

<!-- chunk {"id": "body-0114", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

Any one-point distribution $\delta_z$ resides in the Wasserstein ball of radius $\varepsilon$ only if $|z|\le \varepsilon$, and therefore the maximum risk that any one-point distribution can attain is $\max\{0, \varepsilon-1\}$, which is strictly smaller than $\varepsilon/2$ for any $\varepsilon \in $. Thus, no one-point distribution can be extremal.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Tractability Results for Empirical Nominal Distributions", "weight": 1.0} -->

If the worst-case risk over a Wasserstein ball centered at the empirical distribution is attained, then there always exists an extremal distribution with $N+1$ atoms that can be characterized in quasi-closed form[gao2016distributionally]. In practice, however, it is often convenient to ignore this minimal representability and to search over candidate distributions with more than $N+1$ atoms, e.g., by solving a finite convex optimization problem such as[thm:type1:extrem]. For generic nominal distributions, necessary and sufficient conditions for the existence of an extremal distribution are detailed in[gao2016distributionally].

<!-- chunk {"id": "body-0116", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

We will now demonstrate that the worst-case risk evaluation problem [eq:worst:risk] and the distributionally robust decision problem[eq:dro] sometimes admit exact tractable reformulations or conservative tractable approximations even if the nominal distribution $\widehat \PP$ is continuous. To show this, we assume throughout this section that $\widehat \PP_N$ has mean vector $\widehat\m\in\mathbb{R}^m$ and covariance matrix $\widehat\cov\in \mathbb{S}_{+}^m$. Thus, we implicitly assume that$\widehat \PP_N$has finite second-order moments.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

We first define an uncertainty set in the space of mean vectors and covariance matrices.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

$$\mathcal U_{\varepsilon}(\widehat\m, \widehat\cov) = \left\{ (\mu,\Sigma) \in \mathbb{R}^m\times \mathbb{S}_{+}^m: \| \widehat\m - \mu \|_2^2 + \Tr{\widehat\cov + \Sigma - 2 \left(\widehat\cov^{\frac{1}{2}} \Sigma \widehat\cov^{\frac{1}{2}} \right)^{\frac{1}{2}} } \leq \varepsilon^2 \right\}$$ This uncertainty set is of interest because it covers the projection of the type-2 Wasserstein ball $\mathbb{B}_{\varepsilon,2}(\widehat \PP_N)$ onto the space of mean vectors and covariance matrices.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

Moreover, if the nominal distribution is elliptical, $\mathcal U_{\varepsilon}(\widehat\m, \widehat\cov)$ is actually equal to the projection of $\mathbb{B}_{\varepsilon,2}(\widehat \PP_N)$.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

\PP_N= \mathcal{E}_g(\widehat \mu, \widehat \Sigma)$ is an elliptical distribution.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

[prop:gelbrich-projection] follows immediately from Theorem[theorem:gelbrich]. The condition $\Xi=\mathbb{R}^m$ ensures that any elliptical distribution $\mathds{Q}= \mathcal{E}_g(\mu, \Sigma)$ with the same density generator as the nominal distribution and with $W_2(\mathds{Q},\widehat \PP_N)\le\varepsilon$ belongs to $\mathbb{B}_{\varepsilon,2}(\widehat \PP_N)$. One can show that$\mathcal U_{\varepsilon}(\widehat\m, \widehat\cov) $ is convex and compact[shafieezadeh2018wasserstein], which is expected as it is a projection of a (Wasserstein)ball.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

The uncertainty set $\mathcal U_{\varepsilon}(\widehat\m, \widehat\cov)$ can conveniently be used in classical robust optimization.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

Indeed, a robust constraint that requires a concave function $h(\mu,\Sigma)$ to be nonpositive for all $(\mu,\Sigma)\in \mathcal U_{\varepsilon}(\widehat\m, \widehat\cov)$ can be reformulated as a convex constraint that involves the conjugate of $-h(\mu,\Sigma)$ and the support function of the uncertainty set $\mathcal U_{\varepsilon}(\widehat\m, \widehat\cov)$ [ben2015deriving], thatis, $$h(\mu,\Sigma) \le 0\quad \forall (\mu,\Sigma)\in \mathcal U_{\varepsilon}(\widehat\m, \widehat\cov)\quad \iff\quad\left\{ \begin{array}{l} \exists q\in\mathbb{R}^m,\,Q\in\mathbb S^m:\\[1ex]

<!-- chunk {"id": "body-0124", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

(-h)^*(-q,-Q)+\sigma_{\mathcal U_{\varepsilon}(\widehat\m, \widehat\cov)}(q, Q)\le 0.\end{array}\right.$$ This constraint is computationally tractable for many commonly used constraint functions because the support function of $\mathcal U_{\varepsilon}(\widehat\m, \widehat\cov)$ is SDP-representable[nguyen2019distributionally].

<!-- chunk {"id": "body-0125", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

Unlike the mean vector $\mu= \mathds{E}^{\mathds{Q}}[\xi]$ and the second-order moment matrix $M=\mathds{E}^{\mathds{Q}}[\xi\xi^\top]$, both of which constitute linear functions of the underlying distribution $\mathds{Q}$, the covariance matrix $\Sigma=M-\mu\mu^\top$ is nonlinear in $\mathds{Q}$. The condition $(\mu,\Sigma)\in \mathcal U_\varepsilon(\widehat\m, \widehat\cov)$ thus appears to be nonconvex in $\mathds{Q}$.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

To gain a clearer understanding, it is instructive to introduce the uncertainty set$\mathcal V_{\varepsilon}(\widehat\m, \widehat\cov)$ for$(\mu,M)$ induced by the uncertainty set$\mathcal U_{\varepsilon}(\widehat\m, \widehat\cov)$ for$(\mu,\Sigma)$, that is, $$\mathcal V_{\varepsilon}(\widehat\m, \widehat\cov) = \left\{ (\mu,M) \in \mathbb{R}^m\times \mathbb{S}_{+}^m: (\mu, M-\mu\mu^\top) \in \mathcal U_{\varepsilon}(\widehat\m, \widehat\cov) \right\}.$$ Maybe surprisingly, even though it is defined as the pre-image of a convex set under a nonlinear transformation, one can prove that $\mathcal

<!-- chunk {"id": "body-0127", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

V_{\varepsilon}(\widehat\m, \widehat\cov)$ is convex.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

This implies, counterintuitively, that the condition $(\mu,\Sigma)\in \mathcal U_\varepsilon(\widehat\m, \widehat\cov)$ is actually convex in $\mathds{Q}$ because it is equivalent to the requirement $(\mu,M)\in \mathcal V_\varepsilon(\widehat\m, \widehat\cov)$ and because the moments $(\mu,M)$ are linear in $\mathds{Q}$.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

Thanks to its convexity, the uncertainty set $\mathcal V_{\varepsilon}(\widehat\m, \widehat\cov)$ can again conveniently be used in classical robust optimization. Indeed, a robust constraint that requires a concave function $h(\mu,M)$ to be nonpositive for all $(\mu,M)\in \mathcal V_{\varepsilon}(\widehat\m, \widehat\cov)$ can be reformulated as a simple convex constraint involving the conjugate of $-h(\mu,M)$ and the support function of $\mathcal V_{\varepsilon}(\widehat\m, \widehat\cov)$. This constraint is computationally tractable for many commonly used constraint functions because the support function of $\mathcal V_{\varepsilon}(\widehat\m, \widehat\cov)$ is SDP-representable[nguyen2019distributionally].

<!-- chunk {"id": "body-0130", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

A useful ambiguity set in the space of probability distributions is the Gelbrich hull, which is constructed as the pre-image of $\mathcal U_{\varepsilon}(\widehat\m, \widehat\cov)$under the mean-covariance projection.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

The Gelbrich hull is given by $$\mathbb{G}_{\varepsilon}(\widehat\m, \widehat\cov) = \left\{ \mathds{Q} \in \mathcal P(\Xi): \left(\mathds{E}^{\mathds{Q}}[\xi], \mathds{E}^\mathds{Q}[(\xi-\mathds{E}^{\mathds{Q}}[\xi])(\xi-\mathds{E}^{\mathds{Q}}[\xi])^\top] \right) \in \mathcal U_{\varepsilon}(\widehat\m, \widehat\cov) $\mathbb{G}_{\varepsilon}(\widehat\m, \widehat\cov)$ contains all distributions supported on $\Xi$ whose mean vectors and covariance matrices fall into the uncertainty set $\mathcal U_{\varepsilon}(\widehat\m,

<!-- chunk {"id": "body-0132", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

Equivalently, by the definition of the induced uncertainty set $\mathcal V_\varepsilon(\widehat\m, \widehat\cov)$, the Gelbrich hull can also be represented as $$\mathbb{G}_{\varepsilon}(\widehat\m, \widehat\cov) = \left\{ \mathds{Q} \in \mathcal P(\Xi): \left(\mathds{E}^{\mathds{Q}}[\xi], \mathds{E}^\mathds{Q}[\xi\xi^\top] \right) \in \mathcal V_{\varepsilon}(\widehat\m, \widehat\cov) \right\}.$$ Thus, the Gelbrich hull can be expressed as the pre-image of the convex set $\mathcal V_{\varepsilon}(\widehat\m, \widehat\cov)$ under a linear transformation, which shows that is is actually convex.

<!-- chunk {"id": "body-0133", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

We emphasize that convexity is not apparent from Definition[def:gelbrich-hull], which introduces the Gelbrich hull as the pre-image of a convex set under a nonlinear transformation.

<!-- chunk {"id": "body-0134", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

$ \mathcal P(\Xi,\mu,\Sigma)$ as the Chebyshev ambiguity set that contains all distributions on$\Xi$ with mean vector$\mu$ and covariance matrix$\Sigma$, then the Gelbrich hull can also be expressedas $$\mathbb{G}_{\varepsilon}(\widehat\m, \widehat\cov) = \bigcup_{(\mu,\Sigma) \in \mathcal U_{\varepsilon}(\widehat\m, \widehat\cov)} \mathcal P(\Xi,\mu,\Sigma).$$ From this representation it is evident that if $\mathbb{G}_{\varepsilon}(\widehat\m, \widehat\cov)$ contains a distribution $\mathds{Q}$, then it contains all distributions on $\Xi$ that have the same mean vector and covariance matrix as $\mathds{Q}$.

<!-- chunk {"id": "body-0135", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

It is easy to verify that the Gelbrich hull provides an outer approximation for any Wasserstein ball $\mathbb{B}_{\varepsilon,p}(\widehat \PP_N)$ with $p\ge 2$. Indeed, if $\mathbb{B}_{\varepsilon,p}(\widehat \PP_N)$ contains a distribution $\mathds{Q}$ with mean vector$\mu$ and covariance matrix$\Sigma$, then $(\mu,\Sigma)\in\mathcal U_{\varepsilon}(\widehat\m, \widehat\cov)$ by virtue of Proposition[prop:gelbrich-projection], which implies via[eq:gelbrich-union] that $\mathds{Q}\in \mathbb{G}_{\varepsilon}(\widehat\m, \widehat\cov)$. These insights culminate in the following theorem.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

If the nominal distribution $\widehat \PP_N$ has mean vector $\widehat\m \in \mathbb{R}^m$ and covariance matrix $\widehat\cov \in \mathbb{S}_{+}^m$, then we have $\mathbb{B}_{\varepsilon,p}(\widehat \PP_N) \subseteq \mathbb{G}_{\varepsilon}(\widehat\m, \widehat\cov)$ for every $p \geq 2$. [theorem:gelbrich:amb] shows that the Gelbrich hull provides an outer approximation for all Wasserstein balls $\mathbb{B}_{\varepsilon,p}(\widehat \PP_N)$ with $p\ge 2$ solely on the basis of mean and covariance information. Discarding all information about $\widehat \PP_N$ beyond its first- and second-order moments can be seen as a compression of the training dataset.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

This amounts to sacrificing higher-order moment information and may improve the tractability of the risk evaluation problem[eq:worst:risk] and the distributionally robust decision problem[eq:dro].

<!-- chunk {"id": "body-0138", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

To show this, we define the Gelbrich risk as $$\overline \mathcal{R}_{\varepsilon}(\widehat\m, \widehat\cov, \ell) = \sup_{\mathds{Q} \in \mathbb{G}_{\varepsilon}(\widehat\m, \widehat\cov)} ~ \mathcal{R}(\mathds{Q}, \ell)$$ and the optimal Gelbrich risk as $$\overline\mathcal{R}_{\varepsilon}(\widehat\m, \widehat\cov, \mathcal{L}) = \inf_{\ell \in \mathcal{L}} ~ \overline \mathcal{R}_{\varepsilon}(\widehat\m, \widehat\cov, \ell).$$ Theorem[theorem:gelbrich:amb] immediately implies that the (optimal) Gelbrich risk provides an upper bound on the (optimal) worst-case risk whenever

<!-- chunk {"id": "body-0139", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

If the nominal distribution $\widehat \PP_N$ has mean vector $\widehat\m \in \mathbb{R}^m$ and covariance matrix $\widehat\cov \in \mathbb{S}_{+}^m$ and if $p\ge 2$, then $$\mathcal{R}_{\varepsilon, p}(\widehat \PP_N, \ell)\le \overline \mathcal{R}_{\varepsilon}(\widehat\m, \widehat\cov, \ell)\quad \forall \ell\in\mathcal{L} \qquad \text{and}\qquad \mathcal{R}_{\varepsilon, p}(\widehat \PP_N, \mathcal{L}) \le \overline\mathcal{R}_{\varepsilon}(\widehat\m, \widehat\cov, \mathcal{L}).$$ [eq:gelbrich-union] of the

<!-- chunk {"id": "body-0140", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

Gelbrich hull as a union of Chebyshev ambiguity sets suggests that the Gelbrich risk of any fixed loss function$\ell(\xi)$ can be expressed as the optimal value of the following two-layer optimization problem[nguyen2019distributionally].

<!-- chunk {"id": "body-0141", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

\overline \mathcal{R}_{\varepsilon}(\widehat\m, \widehat\cov, \ell)~& = \sup\limits_{(\mu, \Sigma) \in \mathcal U_\varepsilon(\widehat\m, \widehat\cov)} ~\,\quad \sup\limits_{\mathds{Q} \in \mathcal P(\Xi,\mu,\Sigma)} \mathcal{R}(\mathds{Q}, \ell)\\& = \sup\limits_{(\mu, M) \in \mathcal V_\varepsilon(\widehat\m, \widehat\cov)} \, \sup\limits_{\mathds{Q} \in \mathcal P(\Xi,\mu,M-\mu\mu^\top)} \mathcal{R}(\mathds{Q}, \ell) Note that[eq:two-layer-b] follows immediately from the definition of the uncertainty set

<!-- chunk {"id": "body-0142", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

$\mathcal V_\varepsilon(\widehat\m, \widehat\cov)$ and the formula for the covariance matrix in terms of the mean vector and the second-order moment matrix.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

The inner problems in[eq:two-layer-a] and[eq:two-layer-b] both represent the same distributionally robust optimization problem over a Chebyshev ambiguity set but with different parameterizations. This problem can be viewed as an infinite-dimensional linear program over all probability distributions $\mathds{Q}$ that satisfy the linear equality constraints $\mathds{E}^\mathds{Q}[\xi]=\mu$ and $\mathds{E}^\mathds{Q}[\xi\xi^\top]=M$. Therefore, the optimal value of the inner maximization problem is concave in the right hand side parameters$\mu$ and$M$ but generally nonconcave in the alternative parameters $\mu$ and $\Sigma$. The outer problem in[eq:two-layer-a] hedges against ambiguity in the mean vector and the covariance matrix, while the one in[eq:two-layer-b] hedges against ambiguity in the first- and second-order moments.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

The formulation[eq:two-layer-a] is conceptually appealing because of its connection to the Wasserstein distance and because it is more natural to characterize a distribution in terms of its mean vector and covariance matrix. The formulation[eq:two-layer-b], on the other hand, is computationally attractive because it expresses the outer problem as a convex program that maximizes a manifestly concave function over the convex set $\mathcal V_\varepsilon(\widehat\m, \widehat\cov)$.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

Distributionally robust optimization problems akin to[eq:two-layer-a] and[eq:two-layer-b] that accommodate a second layer of robustness to account for moment ambiguity have been investigated in [delage2010distributionally, el-ghaoui2003wcvar, hanasusanto2015distributionally, natarajan2010utility, rujeerapaiboon2015robust, zymler2013wcvar], among others. As the optimal value of the inner maximization problem is always concave in$(\mu, M)$ but typically nonconcave in$(\mu,\Sigma)$, moment ambiguity has mostly been modeled through convex uncertainty sets for$(\mu,M)$, thereby ensuring convexity of the outer maximization problem.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

For example, uncertainty sets that force $\mu$ to lie in an ellipsoid and $M$ in the intersection of two positive semi-definite cones were studied in [delage2010distributionally], while box-type uncertainty sets for$(\mu,M)$ were proposed in[natarajan2010utility] and refined in[hanasusanto2015distributionally, zymler2013wcvar]. Convex uncertainty sets for $(\mu,\Sigma)$ were shown to render the outer maximization problems convex only in special cases, e.g., when evaluating a worst-case value-at-risk of a linear or quadratic loss function[el-ghaoui2003wcvar, rujeerapaiboon2015robust].

<!-- chunk {"id": "body-0147", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

The convex uncertainty set $\mathcal U_\varepsilon(\widehat\m, \widehat\cov)$ for $(\mu,\Sigma)$ is remarkable because it leads to a second-layer maximization problem in[eq:two-layer-a] that admits a convex reformulation for all loss functions$\ell(\xi)$. [eq:two-layer-b] of the Gelbrich risk evaluation problem into two consecutive maximization problems offers a systematic approach to derive convex reformulations for[eq:gelbrich:risk]. A tractable SDP reformulation is available, for example, when the loss function $\ell(\xi)$is a pointwise maximum of finitely many (possibly indefinite) quadratic functions.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

In order to construct an extremal distribution for the Gelbrich risk evaluation problem [eq:gelbrich:risk], it is again expedient to derive the dual of the SDP[eq:p.w.quad].

<!-- chunk {"id": "body-0149", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

\end{bmatrix} \succeq 0 \quad \forall j \in [J] \\ [3ex] & \DS \sum_{j=1}^J \alpha_{j} = 1,~ \DS \sum_{j=1}^J \theta_j = \mu,~ \DS \sum_{j=1}^J \Theta_{j} = \Sigma+ \mu \mu^\top, ~ (\mu,\Sigma)\in\mathcal U_\varepsilon(\widehat\m, \widehat\cov).}$$ Note that problem [theorem:p.w.quadratic2] has a continuous objective function as well as a compact feasible set and is therefore solvable.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

Any optimal solution $(\mu^\star,\Sigma^\star, \{\alpha_j^\star, \theta_j^\star, \Theta_j^\star \}_j)$ can in principle be used to construct an extremal distribution$\mathds{Q}^\star$ that attains the supremum in the Gelbrich risk evaluation problem[eq:gelbrich:risk].

<!-- chunk {"id": "body-0151", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

If $\nu_\infty = \emptyset$, it is easy to show that a mixture of Gaussian distributions is optimal in[eq:gelbrich:risk]. Specifically, define the distribution $\mathds{Q}^\star_j = \mathcal N(\theta^\star_j / \alpha^\star_j, \Theta^\star_j / \alpha^\star_j)$ for every $j \in \nu_+$. We next show that the mixture distribution $\mathds{Q}^\star = \sum_{j\in \nu_+} \alpha^\star_j \, \mathds{Q}^\star_j$ is optimal in[eq:gelbrich:risk]. By construction, $\mathds{Q}^\star$ has mean vector $\mu^\star$ and covariance matrix $\Sigma^\star$.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

Thus, we may conclude that $\mathds{Q}^\star \in \mathbb G_\varepsilon(\widehat\m, \widehat\cov)$. Furthermore, the definition of$\mathds{Q}^\star$ as a mixture distribution and the definition of$\ell$ as a pointwise maximum of quadratic component functions implies that \mathds{E}^{\mathds{Q}^\star}[\ell(\xi)] \geq \sum_{j \in \nu_+} \alpha_j^\star \, \mathds{E}^{\mathds{Q}_j^\star}[\xi^\top Q_j \xi + 2 q_j^\top \xi + q_j^0] = \sum_{j \in [J]} \Tr{Q_j \Theta_j^\star} + 2 q_j^\top \theta_j^\star + q_j^0 p_j^\star.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

Specifically, the inequality holds because $\ell(\xi) \geq \xi^\top Q_j \xi + 2 q_j^\top \xi + q_j^0$ for every$j\in[J]$, and the equality holds because $\nu_\infty = \emptyset$ and $\theta^\star_j = 0$ whenever $\alpha_j^\star = 0$. This ensures that $\mathds{Q}^\star$ solves the worst-case expectation problem[eq:gelbrich:risk].

<!-- chunk {"id": "body-0154", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

While exactly computable in polynomial time, the Gelbrich risk of a piecewise quadratic loss function may only provide a loose upper bound on the worst-case risk under the Wasserstein ambiguity set, which is often the actual quantity of interest. One can prove, however, that the Gelbrich risk [eq:gelbrich:risk] coincides with the worst-case risk[eq:worst:risk]with respect to a type-2 Wasserstein ball if the loss function is quadratic and the nominal distribution is elliptical.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

Assume that $\Xi = \mathbb{R}^m$ and that $\ell(\xi) = \xi^\top Q \xi + 2 q^\top \xi$ with $Q \in \mathbb S^m$ and $q \in \mathbb{R}^m$ is a quadratic loss function.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

If $\widehat\m\in \mathbb{R}^m$ and $\widehat\cov\in\mathbb{S}_{+}^m$, then the Gelbrich risk[eq:gelbrich:risk] is equal to the optimal value of a tractable SDP, that is, $$\begin{array}{rcl} \overline \mathcal{R}_{\varepsilon}(\widehat\m, \widehat\cov, \ell) ~=&\inf & \gamma \left(\varepsilon^2 - \|\widehat\m\|_2^2 - \mathop{\rm Tr}\, [\widehat\cov]\right) + z + \Tr{Z} \\[2ex] &\st &\gamma \in \mathbb{R}_+, \; z \in \mathbb{R}_+,\; Z \in \mathbb{S}_{+}^m \\[1ex] &&\begin{bmatrix} \gamma

<!-- chunk {"id": "body-0157", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

Moreover, if $\widehat \PP_N= \mathcal{E}_g(\widehat \mu, \widehat \Sigma)$ is an elliptical distribution with mean vector $\widehat\m$ and covariance matrix $\widehat\cov$, $p = 2$ and $\| \cdot\| = \| \cdot \|_2$ is the Euclidean norm on $\mathbb{R}^m$, then the worst-case risk[eq:worst:risk], the Gelbrich risk[eq:gelbrich:risk] and the optimal value of the SDP[eq:gelbrich:quad] are all equal. [eq:gelbrich:quad] is easily obtained from[eq:p.w.quad] by setting $J=1$ and noting that $Y=Q_1$, $y=q_1$ and $y_0=0$ at optimality.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

As usual, a discrete extremal distribution $\mathds{Q}^\star$ for the Gelbrich risk evaluation problem[eq:gelbrich:risk] can be derived from the dual of the SDP[eq:gelbrich:quad]. In the following we denote the mean vector and the covariance matrix of $\mathds{Q}^\star$ by$\mu^\star$ and$\Sigma^\star$, respectively. As $\mathds{Q}^\star\in\mathbb{G}_{\varepsilon}(\widehat\m, \widehat\cov)$, and as the Gelbrich hull is constructed solely on the basis of first- and second-order moment information, any distribution with mean vector $\mu^\star$ and covariance matrix $\Sigma^\star$ belongs to $\mathbb{G}_{\varepsilon}(\widehat\m, \widehat\cov)$, too.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

Moreover, as $\ell(\xi)$ is quadratic, the risk $\mathcal{R}(\mathds{Q}^\star,\ell)$ depends on $\mathds{Q}^\star$ only through its first- and second-order moments. This implies that any distribution with mean vector$\mu^\star$ and covariance matrix $\Sigma^\star$ is optimal in[eq:gelbrich:risk].

<!-- chunk {"id": "body-0160", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

Consider now the problem of evaluating the worst-case risk [eq:worst:risk] of the quadratic loss function $\ell(\xi)$ over a type-2 Wasserstein ball centered at an elliptical nominal distribution $\widehat \PP_N = \mathcal{E}_g(\widehat \mu, \widehat \Sigma)$. Theorem[theorem:gelbrich] ensures that all elliptical distributions in the Gelbrich hull with the same density generator as $\widehat \PP_N$ belong to the Wasserstein ball $\mathbb{B}_{\varepsilon,2}(\widehat \PP_N)$. This implies that the special elliptical distribution $\mathds{Q}^\star = \mathcal E_g(\mu^\star, \Sigma^\star)$ is feasible in[eq:worst:risk].

<!-- chunk {"id": "body-0161", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

Moreover, we have $$\overline \mathcal{R}_{\varepsilon}(\widehat\m, \widehat\cov, \ell) = \mathcal{R}(\mathds{Q}^\star,\ell)\le \mathcal{R}_{\varepsilon, p}(\widehat \PP_N, \ell)\le \overline \mathcal{R}_{\varepsilon}(\widehat\m, \widehat\cov, \ell),$$ where the equality holds because $\mathds{Q}^\star$ is optimal in the Gelbrich risk evaluation problem[eq:gelbrich:risk], while the two inequalities follow from the feasibility of $\mathds{Q}^\star$ in the worst-case risk evaluation problem[eq:worst:risk] and Corollary[cor:gelbrich-risk], respectively.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

Thus, all inequalities in the above expression are exact, which implies that $\mathds{Q}^\star$ is actually optimal in[eq:worst:risk].

<!-- chunk {"id": "body-0163", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

Next, we show how $\mathds{Q}^\star$ can be constructed from the optimality conditions of the SDP[eq:gelbrich:quad].

<!-- chunk {"id": "body-0164", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

If all conditions of Theorem[thm:single:quad] hold, $\widehat\cov \succ 0$ and there exists $\gamma^\star\ge 0$ with $\gamma^\star I \succ Q$ that solves the nonlinear algebraic equation \| \widehat \mu - (\gamma I -Q)^{-1} (q + \gamma \widehat \mu) \|_2^2 + \Tr{\widehat\cov \left(I - \gamma (\gamma I - Q)^{-1} \right)^2} =\varepsilon^2, then the Gelbrich risk[eq:gelbrich:risk] is attained by any distribution with mean vector \mu^\star = (\gamma^\star I - Q)^{-1} (\gamma^\star \widehat \mu + q) and covariance matrix \Sigma^\star = (\gamma^\star)^2 (\gamma^\star I - Q)^{-1} \widehat\cov (\gamma^\star I -

<!-- chunk {"id": "body-0165", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

Moreover, if $\widehat \PP_N = \mathcal{E}_g(\widehat \mu, \widehat \Sigma)$ is elliptical, $p = 2$ and $\| \cdot\| = \| \cdot \|_2$ is the Euclidean norm, then the elliptical distribution $\mathds{Q}^\star = \mathcal E_g(\mu^\star, \Sigma^\star)$ attains the worst-case risk in[eq:worst:risk].

<!-- chunk {"id": "body-0166", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

One can show that if $Q\succeq 0$, then $\gamma^\star$ exists and $\Sigma^\star \succeq \lambda_{\min}(\widehat\cov) I$. To give an intuition for Theorem[thm:extremal:easy], note that the SDP[eq:gelbrich:quad] can be converted to an equivalent nonlinear program (NLP) in the single decision variable $\gamma$ by using Schur complements to show that $$z=(q + \gamma \widehat\m)^\top(\gamma I-Q)^{-1} (q + \gamma \widehat\m)\quad \text{and} \quad Z= \gamma^2\; \widehat\cov^{\frac{1}{2}} (\gamma I-Q)^{-1} \widehat\cov^{\frac{1}{2}}$$ at optimality.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

The resulting NLP minimizes a strictly convex objective function that explodes as$\gamma$ drops to $ \lambda_{\max}(Q)$ or as $\gamma$ tends to infinity. Equation[eq:FOC:1] represents its first-order optimality condition, whose unique solution $\gamma^\star$ can be computed efficiently to any precision via bisection or the Newton-Raphson method. Using[eq:FOC:1], one can then show that any distribution with mean vector $\mu^\star$ and covariance matrix $\Sigma^\star$ as defined in[eq:extremal:m] and[eq:extremal:cov], respectively, is indeed feasible and optimal in[eq:gelbrich:risk].

<!-- chunk {"id": "body-0168", "role": "body", "section": "Tractability Results for Elliptical Nominal Distributions", "weight": 1.0} -->

It is instructive to contrast Theorem [thm:single:quad] with Theorem[theorem:convex:quadratic], both of which provide exact tractable SDP reformulations for the problem of evaluating the worst-case risk of a quadratic loss function with respect to a type-2 Wasserstein ball. We highlight that the SDP[eq:gelbrich:quad] derived in Theorem[thm:single:quad] for elliptical nominal distributions accommodates only two linear matrix inequalities, while the SDP[eq:soroosh-convex] derived in Theorem[theorem:convex:quadratic] for empirical nominal distributions involves $N$ linear matrix inequalities and may thus be considerably harder tosolve.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

We now argue that for judiciously calibrated Wasserstein ambiguity sets, the worst-case risk[eq:worst:risk] associated with a finite sample size $N$ provides an upper confidence bound on the true risk[eq:risk] for all admissible loss functions (finite sample guarantee) and that the worst-case optimal risk[eq:dro] converges almost surely to the true optimal risk[eq:opt:risk] as $N$ tends to infinity (asymptotic guarantee). Intuitively, the finite sample guarantee ensures that the out-of-sample risk will fall short of the worst-case risk with high confidence when we implement an optimizer of the distributionally robust decision probelm[eq:dro], while the asymptotic guarantee formalizes the simple intuition that more data enables us to make better decisions.

<!-- chunk {"id": "body-0170", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

Concentration inequalities for the nominal distribution $\widehat \PP_N$ and its moments can be used to derive finite sample and asymptotic guarantees. If $\widehat \PP_N$ is the empirical distribution, for instance, one can prove that$\widehat \PP_N$ converges exponentially fast to the data-generating distribution $\mathds{P}$, in probability with respect to the Wasserstein distance, as $N$tends to infinity.

<!-- chunk {"id": "body-0171", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

Suppose that $\widehat \PP_N$ is the empirical distribution, while $p \neq m/2$, and the unknown true distribution $\mathds{P}$ is light-tailed in the sense that there exist $\alpha > p$ and $A>0$ such that $\mathds{E}^{\mathds{P}} [\exp(\| \xi \|^\alpha)] \leq A$.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

\end{array}\right.$$ [theorem:concentration-empirical] generalizes[esfahani2018data] to arbitrary $p\ge 1$ and is a direct consequence of[fournier2015rate]. The result remains valid for $p = m/2$ but with a more complicated formula for $\varepsilon_{N}(\eta)$ [fournier2015rate]. Intuitively, Theorem[theorem:concentration-empirical] asserts that any Wasserstein ball $\mathbb{B}_{\varepsilon, p}(\widehat \PP_N)$ with radius$\varepsilon\ge \varepsilon_{N}(\eta)$ represents a $(1-\eta)$-confidence set for the unknown data-generating distribution$\mathds{P}$. For dimensions $m>2$, the critical radius$\varepsilon_{N}(\eta)$ of this confidence set decays as $\mathcal O(N^{-\frac{1}{m}})$.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

To reduce the critical radius by$50\%$, the sample size must increase by $2^m$. Unfortunately, this curse of dimensionality is fundamental, and the decay rate of $\varepsilon_{N}(\eta)$ is essentially optimal; see [fournier2015rate] or[weed2017sharp].

<!-- chunk {"id": "body-0174", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

The concentration inequality portrayed in Theorem [theorem:concentration-empirical] gives rise to the following finite sample guarantees.

<!-- chunk {"id": "body-0175", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

Assume that all conditions of Theorem[theorem:concentration-empirical] hold and $\varepsilon_{N}(\eta)$ is defined as in[eq:opt-radius-empirical].

<!-- chunk {"id": "body-0176", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

Then, for all $\eta \in $ and $\varepsilon \geq \varepsilon_N(\eta)$ wehave $$\mathds{P}^N \Big\{ \mathcal{R}(\mathds{P}, \ell) \leq \mathcal{R}_{\varepsilon, p}(\widehat \PP_N, \ell) \quad \forall \ell \in \mathcal L \Big\} \geq 1 - \eta.$$ Moreover, if $\ell^\star$ is an optimizer of the distributionally robust decision problem[eq:dro], which is a function of the training samples, then for all $\eta \in $ and $\varepsilon \geq \varepsilon_N(\eta)$ we have $$\mathds{P}^N \Big\{\mathcal{R}(\mathds{P},\ell^\star) \leq

<!-- chunk {"id": "body-0177", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

\mathcal{R}_{\varepsilon,p}(\widehat \PP_N, \ell^\star) \Big\} \geq 1 - \eta.$$ [thm:finite-sample] asserts that the worst-case risk[eq:worst:risk] provides an upper confidence bound on the true risk[eq:risk] under the unknown data-generating distribution uniformly across all loss functions$\ell\in\mathcal{L}$.

<!-- chunk {"id": "body-0178", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

Moreover, it also asserts that the optimal value of the distributionally robust decision problem[eq:dro] (i.e., the worst-case optimal risk) provides an upper confidence bound on the out-of-sample performance of its optimizers. Note that the probabilities in[eq:generalization-1] and[eq:generalization-2] are evaluated under the distribution $\mathds{P}^N$ of the $N$independent training samples.

<!-- chunk {"id": "body-0179", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

Requiring the Wasserstein ball to cover $\mathds{P}$ with high confidence is only a sufficient but not a necessary condition for the finite sample guarantees[eq:generalization-1] and[eq:generalization-2]. Indeed, these guarantees can be sustained even if the Wasserstein radius is reduced below $\varepsilon_{N}(\eta)$, which is essentially the smallest radius for which the Wasserstein ball represents a $(1-\eta)$-confidence set for $\mathds{P}$. The minimal Wasserstein radius that preserves the finite sample guarantees[eq:generalization-1] and[eq:generalization-2] often decays significantly faster than $\mathcal O(N^{-\frac{1}{m}})$ without suffering from a curse of dimensionality.

<!-- chunk {"id": "body-0180", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

If $p=1$, the data-generating distribution is absolutely continuous with respect to the Lebesgue measure and the set $\mathcal{L}$ of admissible loss functions admits a smooth parameterization, for example, one can show that a Wasserstein radius of the order $\mathcal{O}(\sqrt{\log m/N})$ maintains finite sample guarantees akin to[eq:generalization-1] and[eq:generalization-2], which is consistent with recent findings in the compressed sensing and high-dimensional statistics literature [blanchet2016robust]. $N$ of training samples grows, one can simultaneously reduce the Wasserstein radius $\varepsilon$ and the significance level $\eta$ without sacrificing the finite sample guarantees[eq:generalization-1] and[eq:generalization-2], which allows us to prove asymptotic consistency [esfahani2018data].

<!-- chunk {"id": "body-0181", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

Assume that all conditions of Theorem[theorem:concentration-empirical] hold. Select $\eta_N \in (0, 1]$ and set $\varepsilon_N= \varepsilon_{N}(\eta_N)$ as in[eq:opt-radius-empirical], $N\in\mathbb N$, such that $\sum_{N=1}^\infty \eta_N < \infty$ and $\lim_{N \to \infty} \varepsilon_N = 0$.

<!-- chunk {"id": "body-0182", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

A possible choice is $\eta_N = \exp(-\sqrt{N})$.

<!-- chunk {"id": "body-0183", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

If there exists $C > 0$ with $|\ell(\xi)| \leq C (1 + \| \xi \|^p)$ for all $\ell \in \mathcal L$ and $\xi \in \Xi$, then we have $\mathds{P}^\infty$-almost surely that $\mathcal{R}_{\varepsilon_N, p}(\widehat \PP_N, \mathcal L) \downarrow \mathcal{R}(\mathds{P}, \mathcal L)$ as $N$ tends to infinity.

<!-- chunk {"id": "body-0184", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

Next, we describe a concentration inequality for the sample mean and the sample covariance matrix that has ramifications for the Gelbrich risk minimization problem Suppose that the unknown true distribution $\mathds{P}$ has mean vector $\mu$ and covariance matrix $\Sigma$ and that there are $\alpha > 2$ and $A>0$ such that $\mathds{E}^{\mathds{P}} [\exp(\| \xi \|_2^\alpha)] \leq A$.

<!-- chunk {"id": "body-0185", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

Then, there is $c>1$ that depends on $\mathds{P}$ only through $\mu$, $\Sigma$, $\alpha$, $A$, and $m$ such that for any $\eta \in (0, 1]$ the sample mean$\widehat\m$ and the sample covariance matrix$\widehat\cov$ satisfy the concentration inequality $\mathds{P}^N[(\mu,\Sigma)\in\mathcal U_\varepsilon(\widehat\m,\widehat\cov)] \geq 1-\eta$ whenever $\varepsilon$ exceeds $$\varepsilon_{N}(\eta) = \frac{\log (c /\eta)}{\sqrt{N}}.%\varepsilon_{N}(\eta) =\left(\frac{\log (c_1 /\eta)}{c_2 N} \right)^{1/2}.$$ [theorem:concentration-elliptical] asserts that the uncertainty set

<!-- chunk {"id": "body-0186", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

$\mathcal U_\varepsilon(\widehat\m,\widehat\cov)$ with radius $\varepsilon\ge \varepsilon_{N}(\eta)$ represents a $(1-\eta)$-confidence set for the mean vector and covariance matrix of the unknown data-generating distribution$\mathds{P}$.

<!-- chunk {"id": "body-0187", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

The critical radius $\varepsilon_{N}(\eta)$ of this confidence set decays as $\mathcal O(N^{-\frac{1}{2}})$ and is thereforeunlike the critical radius[eq:opt-radius-empirical]notsubject to a curse of dimensionality. [theorem:concentration-elliptical] strengthens [rippl2016limit], which leverages a generalized central limit theorem to show that the type-2 Wasserstein distance between two normal distributions with true and empirical moments, respectively, decays asymptotically as $\mathcal O(N^{-\frac{1}{2}})$. A generalization of this result to elliptical distributions is discussed in [rippl2016limit].

<!-- chunk {"id": "body-0188", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

Assume that all conditions of Theorem[theorem:concentration-elliptical] hold and $\varepsilon_{N}(\eta)$ is defined as in[eq:opt-radius-elliptical].

<!-- chunk {"id": "body-0189", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

Then, for all $\eta \in $ and $\varepsilon \geq \varepsilon_N(\eta)$ wehave $$\mathds{P}^N \Big\{ \mathcal{R}(\mathds{P}, \ell) \leq \overline \mathcal{R}_{\varepsilon}(\widehat\m, \widehat\cov, \ell) \quad \forall \ell \in \mathcal L \Big\} \geq 1 - \eta.$$ Moreover, if $\ell^\star$ is an optimizer of the Gelbrich risk optimization problem[eq:gelbrich-dro], which is a function of the training samples, then for all $\eta \in $ and $\varepsilon \geq \varepsilon_N(\eta)$ we have $$\mathds{P}^N \Big\{\mathcal{R}(\mathds{P},\ell^\star) \leq \overline

<!-- chunk {"id": "body-0190", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

\mathcal{R}_{\varepsilon}(\widehat\m, \widehat\cov, \ell^\star) \Big\} \geq 1 - \eta.$$ [thm:finite-sample-Gelbrich] asserts that the Gelbrich risk[eq:gelbrich:risk] offers an upper confidence bound on the true risk[eq:risk] under the unknown data-generating distribution uniformly across all loss functions.

<!-- chunk {"id": "body-0191", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

It also asserts that the optimal value of the Gelbrich risk optimization problem[eq:gelbrich-dro]provides an upper confidence bound on the out-of-sample performance of its optimizers.

<!-- chunk {"id": "body-0192", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

Asymptotic consistency of the Gelbrich risk optimization problem can only be established if the unknown true distribution is elliptical, $\Xi=\mathbb{R}^m$ and all admissible loss functions are quadratic. By Theorem[thm:single:quad], these conditions imply that the Gelbrich risk optimization problem[eq:gelbrich-dro] is equivalent to the Wasserstein distributionally robust optimization problem[eq:dro] equipped with a type-2 Wasserstein ball centered at an elliptical nominal distribution, where the Wasserstein distance is induced by the Euclidean norm.

<!-- chunk {"id": "body-0193", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

Assume that all conditions of Theorem[theorem:concentration-elliptical] hold. Select $\eta_N \in (0, 1]$ and set $\varepsilon_N= \varepsilon_{N}(\eta_N)$ as in[eq:opt-radius-elliptical], $N\in\mathbb N$, such that $\sum_{N=1}^\infty \eta_N < \infty$ and $\lim_{N \to \infty} \varepsilon_N = 0$.

<!-- chunk {"id": "body-0194", "role": "body", "section": "Performance Guarantees", "weight": 1.0} -->

If $\mathds{P}$ is an elliptical distribution, $\Xi=\mathbb{R}^m$ and $\ell(\xi)$ is quadratic for all $\ell\in\mathcal{L}$, then we have $\mathds{P}^\infty$-almost surely that $\overline \mathcal{R}_{\varepsilon_N, p}(\widehat\m, \widehat\cov, \mathcal L) \downarrow \mathcal{R}(\mathds{P}, \mathcal L)$ as $N$ tends to infinity.

<!-- chunk {"id": "body-0195", "role": "body", "section": "Distributionally Robust Optimization in Machine Learning", "weight": 1.0} -->

We now demonstrate that the theory of data-driven distributionally robust optimization with Wasserstein ambiguity sets has interesting ramifications for statistical learning and motivates new approaches for addressing fundamental learning tasks such as classification (Section[sec:classification]), regression (Section[sec:regression]), maximum likelihood estimation (Section[sec:mle]) or minimum mean square error estimation (Section[sec:mmse]). We conclude with an overview of other applications of distributionally robust optimization in machine learning (Section[sec:other-applications]).

<!-- chunk {"id": "body-0196", "role": "body", "section": "Distributionally Robust Classification", "weight": 1.0} -->

In binary classification problems the central object of study is a random vector$\xi=(x,y)$, where$x \in \mathbb{R}^{n}$ is termed the input, and$y\in\{-1,+1\}$ is referred to as the output. The distribution$\mathds{P}$ of$\xi$ is unknown but indirectly observable through finitely many training samples $\widehat\xi_i=(\widehat{x}_i, \widehat{y}_i)$, $i \in[N]$. The goal of binary classification is to predict the output$y$ corresponding to a given input$x$. The classifier with the lowest possible misclassification probability is the one that predicts $y=1$ if $\mathds{P}[y=1|x]\ge 0.5$ and $y=-1$ otherwise. Unfortunately, this classifier is not implementable when$\mathds{P}$is unknown.

<!-- chunk {"id": "body-0197", "role": "body", "section": "Distributionally Robust Classification", "weight": 1.0} -->

Statistical learning aims to construct classifiers solely on the basis of the training data. One of the most popular approaches in practice is to construct a linear scoring function$w^\top x$, encoded by a weight vector $w\in\mathbb{R}^n$, and to predict $y$ as the sign of $w^\top x$. In hindsight, the prediction was correct if the actual output $y$ coincides with the predicted output $\mathop{\rm sign}(w^\top x)$ or, equivalently, if the product $y\cdot w^\top x$ is positive. The realized prediction error can thus be quantified by $L (y\cdot w^\top x)$, where $L(z)$ is some nonnegative and non-increasing univariate loss function that is large for negative and small for positive values of$z$. Examples of popular loss functions are listed in Table[table:classification].

<!-- chunk {"id": "body-0198", "role": "body", "section": "Distributionally Robust Classification", "weight": 1.0} -->

The best scoring function for a given choice of $L(z)$ is the one whose weight vector$w$ minimizes the expected prediction error $\mathds{E}^\mathds{P}[L (y\cdot w^\top x)]$. Unfortunately, the expectation is evaluated under the unknown distribution $\mathds{P}$, and thus the optimal scoring function cannot be computed. Promising near-optimal scoring functions can be found, however, by solving a distributionally robust classification model that minimizes the worst-case expected prediction error with respect to a type-1 Wasserstein ball, that is, \inf\limits_{w\in \mathbb{R}^n} \sup\limits _ {\mathds{Q} \in \mathbb{B}_{\varepsilon, 1}(\widehat \PP_N)} \mathds{E} ^ \mathds{Q} \left[L (y\cdot w^\top x) \right], where $\widehat \PP_N$ is the empirical distribution on the training samples.

<!-- chunk {"id": "body-0199", "role": "body", "section": "Distributionally Robust Classification", "weight": 1.0} -->

We assume here that all distributions in the Wasserstein ball are supported on $\Xi=\mathbb X \times\mathbb Y$, where $\mathbb X\subseteq\mathbb{R}^n$ is convex and closed, while $\mathbb Y=\{-1,+1\}$. We also assume that the norm on the input-output space used in the definition of the Wasserstein distance is additively separable, that is, $\| \xi \| = \|x\|+ \frac{\kappa}{2} |y|$, whereby slight abuse of notation$\|x\|$ stands for an arbitrary norm on the input space, while $\kappa>0$quantifies the relative importance of outputs versus inputs.

<!-- chunk {"id": "body-0200", "role": "body", "section": "Distributionally Robust Classification", "weight": 1.0} -->

Commonly used loss functions for binary classification. name $L(z)$ learning model hinge loss $\max\{0, 1-z\}$ support vector machine1ex smooth hinge loss $\left\{ \frac{1}{2} - z & \text{if } z \leq 0 \\[0.5ex] \frac{1}{2} \left(1 - z\right)^2 & \text{if } 0 <z < 1 \\[0.5ex] \end{array} \right.$ smooth support vector machine4ex logloss $\log(1+ \exp(-z))$ logistic regression The classification model [eq:classification] is easily recognized as an instance of the distributionally robust decision problem[eq:dro] that optimizes over all (multivariate) loss functions of the form $\ell(\xi)=L(y\cdot w^\top x)$ parameterized by$w\in\mathbb{R}^n$.

<!-- chunk {"id": "body-0201", "role": "body", "section": "Distributionally Robust Classification", "weight": 1.0} -->

By leveraging Theorem[thm:type1], problem[eq:classification] can be recast as a finite convex program if $L(z)$ is convex and piecewise linear, while $\mathbb X$ is convex and closed. An alternative convex reformulation can be obtained from Theorem[thm:type1:convex] if $L(z)$ is convex (but not necessarily piecewise linear), while $\mathbb X=\mathbb{R}^n$. For all univariate loss functions listed in Table[table:classification], the convex reformulations of problem[eq:classification] are equivalent to tractable conic programs. Explicit formulations of these conic programs are reported in [shafieezadeh2017regularization].

<!-- chunk {"id": "body-0202", "role": "body", "section": "Distributionally Robust Classification", "weight": 1.0} -->

The distributionally robust classification problem [eq:classification] encapsulates two interesting special cases. First, if the Wasserstein radius is set to $\varepsilon=0$, then[eq:classification] collapses to the standard empirical risk minimization problem that minimizes the average prediction error across the training samples. Moreover, if the parameter $\kappa$ appearing in the definition of the norm tends to infinity, then[eq:classification] reduces to a classical regularizedempirical risk minimization problem.

<!-- chunk {"id": "body-0203", "role": "body", "section": "Distributionally Robust Classification", "weight": 1.0} -->

If $L(z)$ is any of the loss functions of Table[table:classification], $\mathbb{X} = \mathbb{R}^{n}$ and $\kappa = \infty$, then problem[eq:classification] is equivalent to \inf_{w\in\mathbb{R}^n}~ \frac{1}{N} \sum_{i =1}^N L(\widehat{y}_i \cdot w^\top \widehat{x}_i) + \varepsilon\cdot \| w\|_*.

<!-- chunk {"id": "body-0204", "role": "body", "section": "Distributionally Robust Classification", "weight": 1.0} -->

Recall that the norm $\| \xi \| = \|x\| + \frac{\kappa}{2} |y|$ on the input-output space encodes the transportation cost in the definition of the Wasserstein distance. Thus, $\kappa$ can be viewed as the cost of switching an output from $+1$ to $-1$ or vice versa. If $\kappa=\infty$, then all distributions in the Wasserstein ball are obtained by perturbing the empirical distribution along the input space because perturbations along the output space would be infinitely expensive. By setting $\kappa=\infty$, one thus postulates that there is only input uncertainty but no output uncertainty. [prop:regularization1] gives commonly used regularization techniques a robustness interpretation, which applies under the premise that there is no output uncertainty. It identifies the regularization weight with the Wasserstein radius $\varepsilon$ and the regularization function with the dualof the norm that determines the transportation cost along the input space.

<!-- chunk {"id": "body-0205", "role": "body", "section": "Distributionally Robust Classification", "weight": 1.0} -->

[prop:regularization1] can be deduced from Theorem[thm:type1] by observing that the Lipschitz modulus of the multivariate loss function $\ell(\xi)=L(y\cdot w^\top x)$ is given by $\Lip(L)\cdot\|w\|_*$ and that $\Lip(L)=1$ for all univariate loss functions of Table[table:classification]. Distributionally robust classification models with Wasserstein ambiguity sets were first studied in the context of logistic regression [shafieezadeh2015distributionally]. Extensions to other classification models are discussed in [blanchet2016robust, gao2017wasserstein, shafieezadeh2017regularization].

<!-- chunk {"id": "body-0206", "role": "body", "section": "Distributionally Robust Regression", "weight": 1.0} -->

The goal of regression is a to predict a real (as opposed to a categorical) output$y\in\mathbb{R}$ corresponding to a given input $x\in\mathbb{R}^n$. The regressor that attains the lowest possible mean squared error is the one that predicts the output as $\mathds{E}^\mathds{P}[y|x]$. Unfortunately, this regressor is not implementable when the distribution$\mathds{P}$ of the random vector $\xi=(x,y)$is unknown.

<!-- chunk {"id": "body-0207", "role": "body", "section": "Distributionally Robust Regression", "weight": 1.0} -->

In practice it is often convenient to construct a linear regressor that predicts the output by a linear function $w^\top x$ encoded by a weight vector $w\in\mathbb{R}^n$. The realized prediction error can thus be quantified by $L (w^\top x-y)$, where $L(z)$ is some nonnegative univariate loss function that is large when$z$ deviates from0. Examples of popular loss functions for regression are listed in Table[table:regression].

<!-- chunk {"id": "body-0208", "role": "body", "section": "Distributionally Robust Regression", "weight": 1.0} -->

The best linear regressor that minimizes the expected prediction error $\mathds{E}^\mathds{P}[L (w^\top x-y)]$ cannot be computed when $\mathds{P}$ is unknown, but promising near-optimal linear regressors can be found by solving the distributionally robust regression model \inf\limits_{w\in\mathbb{R}^n} \sup\limits _ {\mathds{Q} \in \mathbb{B}_{\varepsilon, p}(\widehat \PP_N)} \mathds{E} ^ \mathds{Q} \left[L (w^\top x - y) \right], which minimizes the worst-case expected prediction error in view of all distributions on a convex closed set $\Xi=\mathbb X \times\mathbb Y\subseteq \mathbb{R}^n\times \mathbb{R}$ within a type-$p$ Wasserstein ball around the empirical distribution on $N$ training samples.

<!-- chunk {"id": "body-0209", "role": "body", "section": "Distributionally Robust Regression", "weight": 1.0} -->

By Theorem[thm:type1], problem[eq:regression] can be reformulated as a finite convex program if $p=1$, $L(z)$ is convex and piecewise linear, and $\mathbb X$ and $\mathbb Y$ are convex and closed. A convex reformulation can also be obtained from Theorem[thm:type1] if $p=1$, $L(z)$ is convex (but not necessarily piecewise linear), while $\mathbb X=\mathbb{R}^n$ and $\mathbb Y=\mathbb{R}$. Moreover, problem[eq:regression] can be reformulated as a finite convex program by using Theorem[theorem:convex:quadratic] if $p=2$, $L(z)$ is convex quadratic, $\mathbb X=\mathbb{R}^n$ and $\mathbb Y=\mathbb{R}$. For details see [shafieezadeh2017regularization] and [blanchet2016robust].

<!-- chunk {"id": "body-0210", "role": "body", "section": "Distributionally Robust Regression", "weight": 1.0} -->

Commonly used loss functions for regression name $L(z)$ parameter learning model squared error $z^2$ n/a ordinary least squares 1ex Huber loss $\left\{ \begin{array}{ll} \frac{1}{2} \xi^2 & \text{if } |z| \leq \delta \\ \delta (|z| - \frac{1}{2} \delta) & \text{otherwise} \end{array} \right.$ $\delta\in\mathbb{R}_+$ Huber regression3ex $\delta$-insensitive loss $\max \{0, |z| - \delta\}$ $\delta\in\mathbb{R}_+$ support vector regression1ex pinball loss $\max\{-\delta z, (1-\delta)z\}$ $\delta\in$ quantile regression Assume now that the norm on the input-output space satisfies $\| \xi \| = \|x\|+ \frac{\kappa}{2} |y|$, where

<!-- chunk {"id": "body-0211", "role": "body", "section": "Distributionally Robust Regression", "weight": 1.0} -->

$\|x\|$ is an arbitrary norm on the input space, while $\kappa>0$ quantifies the relative importance of outputs versus inputs. In the absence of output uncertainty (that is, for $\kappa=\infty$), there is again an intimate relation between robustification and regularization.

<!-- chunk {"id": "body-0212", "role": "body", "section": "Distributionally Robust Regression", "weight": 1.0} -->

Moreover, if $L(z)$ is the square error and $p=2$, then problem[eq:regression] reduces to \inf_{w\in\mathbb{R}^n}~ \Big[\Big(\frac{1}{N} \sum_{i =1}^N L(w^\top \widehat{x}_i-\widehat{y}_i)\Big)^{\frac{1}{2}}+ \varepsilon \cdot \| w\|_*\Big]^2. [prop:regularization2] asserts that if there is no output uncertainty, then the distributionally robust regression problem[eq:regression] reduces to a regularized empirical risk minimization problem, where the regularization function is given by the dual of the norm on the input space.

<!-- chunk {"id": "body-0213", "role": "body", "section": "Distributionally Robust Regression", "weight": 1.0} -->

For Lipschitz continuous univariate loss functions $L(z)$ and for $p=1$, one simply minimizes the sum of the empirical risk and the regularization term weighted by the product of Wasserstein radius and the Lipschitz modulus of $L(z)$. Note that the Huber loss, the $\delta$-insensitive loss and the pinball loss are all Lipschitz continuous with Lipschitz moduli $\delta$, 1 and $\max\{\delta,1-\delta\}$, respectively. For the squared loss we need to set $p=2$ because the type-2 Wasserstein ball is the largest Wasserstein ball for which the worst-case expected loss is finite. In this case, one minimizes a combination of the square root of the empirical loss and the regularization term. If one measures distances in the input space using the $\infty$-norm, then this convex program reduces to the so-called generalized LASSO (Least Absolute Shrinkage and Selection Operator) estimation problem.

<!-- chunk {"id": "body-0214", "role": "body", "section": "Distributionally Robust Regression", "weight": 1.0} -->

For further details on distributionally robust regression see [blanchet2016robust, gao2017wasserstein, shafieezadeh2017regularization].

<!-- chunk {"id": "body-0215", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

Consider now the problem of estimating the mean vector $\mu\in\mathbb{R}^m$ and the covariance matrix $\Sigma\in\mathbb S_+^m$ of a random vector $\xi\in\mathbb{R}^m$ from independent training samples $\widehat \xi_i$, $i\in[N]$.

<!-- chunk {"id": "body-0216", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

The simplest estimators for $\mu$ and $\Sigma$ are the sample mean $\widehat\m$ and the sample covariance matrix $\widehat\cov$, which we define as the actual mean and covariance matrix of the empirical distribution,i.e., $$\widehat\m = \frac{1}{N} \sum_{i=1}^N \widehat{\xi}_i \qquad \text{and} \qquad \widehat\cov = \frac{1}{N} \sum_{i=1}^N (\widehat{\xi}_i - \widehat\m)(\widehat{\xi}_i - \widehat\m)^\top.$$ While $\Sigma$ serves as an input for many problems in engineering, science or economics, it is often the precision matrix $\Sigma^{-1}$ that appears in their solutions.

<!-- chunk {"id": "body-0217", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

For example, in mean-variance portfolio analysis the portfolio variance to be minimized depends on the covariance matrix of the asset returns, while the optimal portfolio weights depend on the precision matrix. Similarly, linear discriminant analysis uses the covariance matrix of the features as an input and outputs a maximum likelihood classifier that depends on the precision matrix. Moreover, the optimal fingerprint method for climate change detection requires the covariance matrix of the internal climate variability as an input and outputs a climate change signal depending on the precision matrix. Thus, it is often more important to know the precision matrix than the covariance matrix. To ensure that the precision matrix is well defined, we will henceforth assume that $\Sigma\succ 0$. Unfortunately, the sample covariance matrix is rank-deficient in the big-data regime when the dimension of $\xi$ exceeds the sample size ($m>N$) even if $\Sigma$ has full rank. In this case, one cannot invert $\widehat\cov$to obtain a meaningful precision matrix estimator.

<!-- chunk {"id": "body-0218", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

From now on we will assume that the unknown true distribution $\mathds{P}$ of $\xi$ is normal. Thus, the problem of maximizing the log-likelihood of the training samples reduces to the following convex program over all candidate mean vectors $\mu$ and precision matrices $X$ [boyd2004convex].

<!-- chunk {"id": "body-0219", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

$$\inf\limits_{\mu \in \mathbb{R}^m, \, X \in \mathbb S_{+}^m} \left\{ -\log\det X + \frac{1}{N} \sum_{i=1}^N (\widehat{\xi}_i - \mu)^\top X (\widehat{\xi}_i - \mu) \right\}$$ Unfortunately, this maximum likelihood estimation (MLE) problem is unbounded for $N\le m$ and (almost surely) solved by $\mu^\star=\widehat\m$ and $X^\star=\widehat\cov^{-1}$ for $N>m$. Thus, we fail again to find an estimator in the big-data regime and simply recover the sample mean and the sample covariance matrix in the small-data regime.

<!-- chunk {"id": "body-0220", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

To overcome this deficiency, we robustify the MLE problem against all distributions within a type-2 Wasserstein ball centered at the normal nominal distribution $\widehat \PP_N=\mathcal N(\widehat\m,\widehat\cov)$, that is, we solve the robust MLE problem \inf\limits_{\mu \in\mathbb{R}^m,\,X\in \mathbb{S}_{+}^m } \left\{ -\log \det X + \sup\limits_{\mathbb Q \in \mathbb{B}_{\varepsilon, 2}(\widehat \PP_N)} \mathds{E}^{\mathbb Q} \left[(\xi-\mu)^\top X (\xi-\mu) \right] \right\}.

<!-- chunk {"id": "body-0221", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

If $\varepsilon=0$, then the robust MLE problem[eq:wise] reduces to the nominal MLE problem[eq:unwise] becauseby the definition of the sample mean and the sample covariance matrixthe (normal) nominal distribution has the same first- and second-order moments as the (discrete) empirical distribution and because the loss function in the expectation is quadratic in $\xi$. One can show via Theorem[thm:single:quad] that[eq:wise] is equivalent to a convex SDP with a determinant term in the objective function. Provided that the Wasserstein radius $\varepsilon$ is strictly positive, this SDP is solvable even in the big-data regime when $m>N$. Thus, it yields a valid precision matrix estimator even if the sample covariance matrix is rank-deficient. Moreover, as SDPs are tractable, the optimal estimator can be computed in polynomial time. In fact, the SDP at hand is highly symmetric and can therefore even be solved in closed form [nguyen2018distributionally].

<!-- chunk {"id": "body-0222", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

If $\varepsilon > 0$ and $\widehat\cov\in\mathbb{S}_{+}^m$ admits the spectral decomposition $\widehat\cov = \sum_{i=1}^m \lambda_i\cdot v_i v_i^\top$ with eigenvalues $\lambda_i \geq 0$ and corresponding orthonormal eigenvectors$v_i$, $i \in[m]$, then the unique minimizer of the robust MLE problem[eq:wise] is given by $\mu^\star = \widehat\m$ and $X^\star = \sum_{i=1}^m x^\star_i \cdot v_i v_i^\top$, where $$x^\star_i = \gamma^\star \left[1 - \frac{1}{2} \left(\sqrt{\lambda_i^2 (\gamma^\star)^2 + 4 \lambda_i \gamma^\star } - \lambda_i

<!-- chunk {"id": "body-0223", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

\gamma^\star \right) \right] \qquad \forall i \in [m],$$ and $\gamma^\star>0$ is the unique positive solution of the algebraic equation $$\bigg(\varepsilon^2 - \frac{1}{2} \sum_{i=1}^m \lambda_i \bigg) \gamma - m + \frac{1}{2} \sum_{i=1}^m \sqrt{\lambda_i^2 \gamma^2 + 4 \lambda_i \gamma } = 0.$$ Theorem[thm:wise:solution] asserts that the robust MLE estimator$\mu^\star$ for the mean vector coincides with the sample mean$\widehat\m$.

<!-- chunk {"id": "body-0224", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

More interestingly, it further asserts that the robust MLE estimator$X^\star$ for the precision matrix has the same eigenvectors$v_i$ as the sample covariance matrix$\widehat\cov$, while its eigenvalues$x^\star_i$ are obtained by applying the nonlinear transformation[eq:wise:x] to the corresponding eigenvalues$\lambda_i$ of $\widehat\cov$. This transformation involves a single unknown parameter$\gamma^\star$, which is the unique positive solution of the algebraic equation[eq:wise:gamma]. As $X^\star$ is obtained by transforming the eigenvalues of the sample covariance matrix, it can be interpreted as a nonlinear shrinkage estimator. We thus refer to it as the Wasserstein shrinkage estimator.

<!-- chunk {"id": "body-0225", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

$X^\star$ and $\widehat\cov$ share the same eigenvectors, $X^\star$ is rotation-equivariant, that is, the estimator applied to the rotated data $R\,\widehat\xi_i$, $i\in[N]$, coincides with the rotated estimator $RX^\star R$ of the original data for every possible rotation matrix $R$. Moreover, as all eigenvalues of $X^\star$ are strictly positive, the estimator is always invertible. Finally, Theorem[thm:wise:solution] indicates that$X^\star$ can be computed highly efficiently by computing the spectral decomposition of $\widehat\cov$ and by solving the scalar algebraic equation[eq:wise:gamma], which can be accomplished by bisection.

<!-- chunk {"id": "body-0226", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

One can show that the Wasserstein shrinkage estimator displays numerous desirable properties [nguyen2018distributionally]. First, its eigenvalues $x_i^\star$ decrease with$\varepsilon$ and eventually converge to0. This makes intuitive sense as for large values of $\varepsilon$ nothing is known about$\xi$, and thus the safest bet is that all of its components have high variance and low precision. Moreover, one can show that the order of the eigenvalues $x_i^\star$ matches the order of the inverse sample eigenvalues $1/\lambda_i$ irrespective of $\varepsilon>0$, which is expected in the absence of any structural information. Finally, one can show that the condition number of $X^\star$ decreases monotonically to1 as $\varepsilon$ grows. Thus, the condition number of $X^\star$improves with the level of ambiguity.

<!-- chunk {"id": "body-0227", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

A statistical theory that shows how to optimally choose $\varepsilon$ is developed in [blanchet2019inverse]. Surprisingly, the Wasserstein radius that attains the lowest possible out-of-sample loss scales as $\varepsilon\propto 1/N$instead of the canonical inverse square-root scaling, which may be expected for this problem.

<!-- chunk {"id": "body-0228", "role": "body", "section": "Distributionally Robust Maximum Likelihood Estimation", "weight": 1.0} -->

So far we have assumed that there is no structural information about the distribution of $\xi$ besides normality. In some practical situation, however, the precision matrix $X$ may have a known sparsity pattern. Indeed, one can show that an element $X_{ij}$ of the precision matrix vanishes if and only if the random variables $\xi_i$ and $\xi_j$ are conditionally independent given all other components of $\xi$. Conditional independencies of this type naturally arise, for example, in the analysis of spatio-temporal data. In the presence of sparsity information, the robust MLE problem is still equivalent to a tractable SDP. Even though it loses its analytical solvability, one can devise a tailored sequential quadratic approximation algorithm with rigorous convergence guarantees to solve the problem numerically, see[nguyen2018distributionally].

<!-- chunk {"id": "body-0229", "role": "body", "section": "Distributionally Robust Minimum Mean Square Error Estimation", "weight": 1.0} -->

Consider next the problem of estimating a signal $x\in \mathbb{R}^{m_x}$ from a noisy observation $y \in\mathbb{R}^{m_y}$ under the premise that the distribution of the random vector $\xi = [x^\top, y^\top]^\top \in \mathbb{R}^m$, $m=m_x+m_y$, is ambiguous and only known to belong to a type-2 Wasserstein ball centered at an elliptical nominal distribution $\widehat \PP_N =\mathcal E_g(\widehat\m, \widehat\cov)$ with nominal mean vector $\widehat\m \in\mathbb{R}^m$, nominal covariance matrix $\widehat\cov\in\mathbb{S}_{+}^m$ and density generator $g$.

<!-- chunk {"id": "body-0230", "role": "body", "section": "Distributionally Robust Minimum Mean Square Error Estimation", "weight": 1.0} -->

This elementary problem is fundamental for numerous applications in engineering (e.g., linear systems theory [golnaraghi2017automatic, ogata2009modern]), econometrics (e.g., linear regression [stock2015introduction, wooldridge2010econometric], time series analysis [chatfield2016analysis, hamilton1994time]), machine learning and signal processing (e.g., Kalman filtering [kay1993fundamentals, murphy2012machine, oppenheim2015signals]) or information theory (e.g., multiple-input multiple-output systems [cover2012elements, mackay2003information]), etc. To formalize the estimation problem, we define an estimator as a measurable function $\psi(y)$ that maps the observation $y$ to a prediction of the signal $x$, and we denote by $\Psi$ the family of all possible estimators.

<!-- chunk {"id": "body-0231", "role": "body", "section": "Distributionally Robust Minimum Mean Square Error Estimation", "weight": 1.0} -->

Moreover, we define the distributionally robust minimum mean square error (MMSE) estimator as an optimizer of $$\inf\limits_{\psi\in\Psi} \sup\limits_{\mathbb Q \in \mathbb{B}_{\varepsilon, 2}(\widehat \PP_N)} \mathds{E}^{\mathbb Q} \left[\| x - \psi(y) \|_2^2 \right].$$ Note that[eq:mmse] constitutes an infinite-dimensional functional optimization problem and thus appears to be hard. However, by establishing a minimax theorem for[eq:mmse] and exploiting the properties of elliptical distributions, one can show that the outer infimum in[eq:mmse] is attained by an affine estimator. Combining this structural insight with Theorem[thm:single:quad] allows us to prove that the estimation problem[eq:mmse] is in fact equivalent to a convex program[shafieezadeh2018wasserstein].

<!-- chunk {"id": "body-0232", "role": "body", "section": "Distributionally Robust Minimum Mean Square Error Estimation", "weight": 1.0} -->

It is possible to eliminate all nonlinearities in [eq:mmse:dual] by using Schur complements and to reformulate the nonlinear convex SDP as a standard linear SDP, which is formally tractable. However, larger problem instances quickly exceed the capabilities of general-purpose solvers.

<!-- chunk {"id": "body-0233", "role": "body", "section": "Distributionally Robust Minimum Mean Square Error Estimation", "weight": 1.0} -->

Instead, there is merit in addressing the nonlinear SDP[eq:mmse:dual] directly with a customized first-order Frank-Wolfe algorithm, which starts at $S^{}=\widehat\cov$ and constructs iterates $$S^{(k+1)}=\alpha_k D^{(k)} + (1-\alpha_k)S^{(k)} \qquad \forall k=0,1,2,\ldots$$ with stepsize $\alpha_k$, where $D^{(k)}\in\mathbb S^m$ is the unique solution of the direction-finding subproblem \max_{D\in\mathbb S^m} \quad & \Tr{D \; \nabla f(S^{(k)})} \\\st \quad & \Tr{D + \widehat\cov - 2 \left(\widehat\cov^{\frac{1}{2}} D \widehat\cov^{\frac{1}{2}}

<!-- chunk {"id": "body-0234", "role": "body", "section": "Distributionally Robust Minimum Mean Square Error Estimation", "weight": 1.0} -->

The Frank-Wolfe algorithm is highly efficient because the direction-finding subproblem[eq:mmse:direction], which linearizes the objective function $f(S)$ of[eq:mmse:dual] around the current iterate $S^{(k)}$, can be solved in closed form.

<!-- chunk {"id": "body-0235", "role": "body", "section": "Distributionally Robust Minimum Mean Square Error Estimation", "weight": 1.0} -->

Indeed, using Theorem[thm:extremal:easy] one can show that[eq:mmse:direction] is solved by $$D^{(k)} = (\gamma^\star)^2 \left(\gamma^\star I- \nabla f(S^{(k)}) \right)^{-1} \widehat\cov \left(\gamma^\star I- \nabla f(S^{(k)}) \right)^{-1},$$ where $\gamma^\star$ is the unique solution with $\gamma^\star I \succ \nabla f(S^{(k)})$ of the algebraic equation $$\Tr{ \widehat\cov \left(I- \gamma (\gamma I - \nabla f(S^{(k)}))^{-1}\right)^2}=\varepsilon^2,$$ which can be solved via bisection [shafieezadeh2018wasserstein].

<!-- chunk {"id": "body-0236", "role": "body", "section": "Distributionally Robust Minimum Mean Square Error Estimation", "weight": 1.0} -->

For a judiciously chosen step-size rule, the Frank-Wolfe algorithm also offers rigorous convergence guarantees [shafieezadeh2018wasserstein].

<!-- chunk {"id": "body-0237", "role": "body", "section": "Distributionally Robust Minimum Mean Square Error Estimation", "weight": 1.0} -->

If $\widehat\cov\succ 0$, $\varepsilon>0$ and $\alpha_k=\frac{2}{k+2}$ for every $k\in\mathbb N$, then the $k^{\rm th}$ iterate $S^{(k)}$ of the Frank-Wolfe algorithm is feasible in[eq:mmse:dual] and satisfies $f(S^\star) - f(S^{(k)}) \le \frac{C}{k+2}$, where $C$ depends only on $\widehat\cov$ and $\varepsilon$, and $S^\star$ is a maximizer of[eq:mmse:dual].

<!-- chunk {"id": "body-0238", "role": "body", "section": "Distributionally Robust Minimum Mean Square Error Estimation", "weight": 1.0} -->

In some applications one has additional structural information about the relation between the signal $x$ and the observation$y$ (e.g., the measurement noise may be known to be independent of the signal, or the observation may be governed by a linear measurement model, etc.). Such structural information can be used to restrict the Wasserstein ambiguity set in[eq:mmse], thereby reducing the conservativeness of the distributionally robust MMSE estimator[nguyen2019bridging].

<!-- chunk {"id": "body-0239", "role": "body", "section": "Other Applications in Machine Learning", "weight": 1.0} -->

Ideas from distributionally robust optimization also permeate several other areas of statistics and machine learning. For example, a distributionally robust optimization model involving two Wasserstein balls centered at two distinct empirical distributions can be used to develop a computationally tractable convex approximation for the minimax robust hypothesis testing problem that aims to minimize the maximum of the worst-case type-I and type-II errors of a prescribed hypothesis test [gao2018robust]. Another example is data-driven inverse optimization, where one observes random signals as well as optimal solutions of an optimization problem parameterized by these signals. The aim is to predict the solution corresponding to a new unseen signal from $N$ independent historical observations without any knowledge of the optimization problem's objective function. This problem can be framed as a structural regression problem that minimizes the worst-case expected prediction loss with respect to a Wasserstein ambiguity set over a space of candidate objective functions[esfahani2018inverse]. Data-driven inverse optimization lends itself, for example, to learning the purchasing behavior of consumers, the production costs of electricity generators, the route choice preferences of passengers in a multimodal transportation system or the hidden optimality principles governing a biological system.

<!-- chunk {"id": "body-0240", "role": "body", "section": "Other Applications in Machine Learning", "weight": 1.0} -->

As a third example, distributionally robust optimization models with Wasserstein ambiguity sets can be used to efficiently compute the worst-case misclassification probability of a given classifier, which amounts to evaluating the worst-case expectation of the (nonconvex) zero-one loss [shafieezadeh2017regularization, shafieezadeh2015distributionally]. Using similar techniques, one can also efficiently compute the worst-case probability of an undesirable event described by the conjunction or disjunction of several linear inequalities for the random vector$\xi$ [hanasusanto2015perspective, esfahani2018data]. If the undesirable event can be influenced so as drive its worst-case probability below a prescribed tolerance, we face a distributionally robust chance constraint. Even though distributionally robust chance constrained programs with Wasserstein ambiguity sets around the empirical distribution are intractable in general, they are sometimes equivalent to mixed-integer linear programs that can be solved with off-the-shelf software [chen2018drocc, xie2018drocc].

<!-- chunk {"id": "body-0241", "role": "body", "section": "Other Applications in Machine Learning", "weight": 1.0} -->

In contrast, distributionally robust chance constrained programs with moment ambiguity sets can often be reformulated as (or tightly approximated by) tractable conic programs [calafiore2006distributionally, cheung2012linear, hanasusanto2015perspective, zymler2013distributionally].

<!-- chunk {"id": "body-0242", "role": "body", "section": "Other Applications in Machine Learning", "weight": 1.0} -->

To conclude, we highlight two opportunities for tailoring a distributionally robust decision problem with a Wasserstein ambiguity set around the empirical distribution to a given training dataset. Recall first that finite sample guarantees hold whenever$\varepsilon$ is large enough for the Wasserstein ball to contain the unknown data-generating distribution with high confidence$1-\beta$. Recall also that the distributionally robust decision problem can often be reformulated as a tractable convex program whose size scales with the sample size $N$. If the computational burden is unmanageable for the given sample size, we can select $K\ll N$, approximate $\widehat \PP_N$ with the closest $K$-point distribution $\mathds{Q}^\star_K$ in Wasserstein distance and replace the original Wasserstein ball of radius $\varepsilon$ around $\widehat \PP_N$ with a new inflated Wasserstein ball of radius $\varepsilon + W_p(\widehat \PP_N, \mathds{Q}^\star_K)$ around $\mathds{Q}^\star_K$.

<!-- chunk {"id": "body-0243", "role": "body", "section": "Other Applications in Machine Learning", "weight": 1.0} -->

By construction, the inflated Wasserstein ball contains the data-generating distribution with the same confidence $1-\beta$. But the size of the corresponding decision problem is only proportional to $K$. This approach provides a systematic method for reducing the computational burden without sacrificing robustness guarantees (but at the expense of increasing the model's level of conservatism). The approximation of a rich $N$-point distribution with a sparse $K$-point distribution is referred to as scenario reduction in the stochastic programming literature. While the exact computation of$\mathds{Q}^\star_K$ is hard, there exist efficient approximation algorithms for scenario reduction[rujeerapaiboon2018scenario].

<!-- chunk {"id": "body-0244", "role": "body", "section": "Other Applications in Machine Learning", "weight": 1.0} -->

An important input for any distributionally robust optimization model with a Wasserstein ambiguity set is the norm that determines the transportation cost in the definition of the Wasserstein distance. The flexibility to choose this norm could be exploited to improve the out-of-sample performance of the model's optimizers. A method for learning the best Mahalanobis norm from the training data is described in [blanchet2017data]. It is shown that this metric learning framework encompasses adaptive regularizationas a special case.

<!-- chunk {"id": "body-0245", "role": "body", "section": "Other Applications in Machine Learning", "weight": 1.0} -->

Acknowledgments. This research was funded by the SNSF grant BSCGI0\_157733. We are grateful to Erick Delage, Bart Van Parys and Shuhao Yan for pointing out errors in the published version [kuhn2019wasserstein] of this paper.

<!-- chunk {"id": "body-0246", "role": "body", "section": "Elliptical Distributions", "weight": 1.0} -->

We say that $\mathds{Q}=\mathcal{E}_g(\mu, \Sigma)$ is an elliptical probability distribution if it has a density function of the form $f(\xi) = C \det(\Sigma)^{-1} \, g((\xi-\mu) \Sigma^{-1} (\xi-\mu))$ with density generator $g(u)\ge 0$ for all $u\ge 0$, normalization constant $C>0$, mean vector $\mu\in\mathbb{R}^m$ and covariance matrix $\Sigma\in\mathbb{S}_{++}^m$.

<!-- chunk {"id": "body-0247", "role": "body", "section": "Elliptical Distributions", "weight": 1.0} -->

Examples of elliptical distributions distribution family density generator $g(u)$ normalization constant $C$ Gaussian distribution $\exp(-u/2)$ $(2\pi)^{-m/2}$1.5ex Logistic distribution $\DS \frac{\exp(-u)}{(1+\exp(-u))^2}$ $ \DS \frac{\pi^{m/2}}{\Gamma(m/2)} \int_0^\infty \frac{y^{m/2 - 1} \exp(-y)}{(1 + \exp(-y))^2} \mathrm{d}y$ 2ex $t$-distribution $\DS \left(1 + u / (\nu-2) \right)^{-\frac{m + \nu}{2}}$ $\DS \frac{\nu^{m/2} \Gamma((m+\nu)/2)}{\pi^{m/2} \Gamma(\nu/2)

<!-- chunk {"id": "body-0248", "role": "body", "section": "Elliptical Distributions", "weight": 1.0} -->

(\nu-2)^m} $ 2ex $\nu > 2$ denotes the degrees of freedom of the $t$-distribution, and $\Gamma$ is the gammafunction.

<!-- chunk {"id": "body-0249", "role": "body", "section": "Conjugates, Support Functions and Dual Norms", "weight": 1.0} -->

The indicator function of a set $\Xi\subseteq \mathbb{R}^m$ is a function $\delta_\Xi(\xi)$ on $\mathbb{R}^m$ defined through $\delta_\Xi(\xi)= 0$ if $\xi\in\Xi$ and $\delta_\Xi(\xi)=\infty$ if $\xi\notin \Xi$. The support function of $\Xi\subseteq \mathbb{R}^m$ is a function $\sigma_\Xi(z)$ on $\mathbb{R}^m$ defined through $\sigma_\Xi(z) = \sup_{\xi \in \Xi} z^\top \xi$. The support function of $\Xi$ coincides with the conjugate of the indicator function of $\Xi$, that is, $\delta_\Xi^*(z)=\sigma_\Xi(z)$.

<!-- chunk {"id": "body-0250", "role": "body", "section": "Conjugates, Support Functions and Dual Norms", "weight": 1.0} -->

If $\Xi$ is convex and closed, then the conjugate of the support function of $\Xi$ coincides with the indicator function of $\Xi$, that is, $\sigma_\Xi^*(\xi)=\delta_\Xi(\xi)$ [rockafellar1997convex].
