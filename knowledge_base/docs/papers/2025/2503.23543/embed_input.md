<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Distributionally Robust Optimization over Wasserstein Balls with I.i.d. Structure

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider distributionally robust optimization problems where the uncertainty is modeled via a structured Wasserstein ambiguity set. Specifically, the ambiguity is restricted to product measures P^(otimes) N, where P lies within a Wasserstein ball centered at an empirical distribution widehatP. This structure reflects the assumption of independent and identically distributed (i.i.d.) uncertainty components and yields a non-convex ambiguity set that is strictly contained in its unstructured counterpart, thereby reducing conservatism. The resulting optimization problem is generally intractable due to the loss of convexity. We address this by introducing a sequence of tractable convex relaxations, each admitting strong duality, and prove that this sequence converges to the original problem value under suitable conditions. Numerical examples are provided to illustrate the effectiveness of the proposed approach. As a byproduct of our proofs, we establish a novel formula, of independent interest, relating the Wasserstein distance of a mixture of product distributions to the Wasserstein distance between its constituent measures.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In stochastic optimization a common goal is to minimize an objective $\Psi$ over a set of feasible decisions $\Theta$, where the objective $\Psi$ is defined as an average of a family of individual uncertainty-affected loss functions $\ell:\Theta\times X\to\mathbb{R}$, with $X$ being a random vector of uncertain parameters defined on a probability space $(X,\Sigma,P)$. In mathematical terms, a stochastic optimization method evaluates To avoid trivialities, we assume throughout that the feasible set $\Theta\subseteq\mathbb{R}^{m}$ and the support set $X\subseteq\mathbb{R}^{d}$ are non-empty and closed.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Problem is ubiquitous in the areas of machine learning, operation research, economics, and automatic control. Unfortunately, the practical deployment of is complicated by the fact that the precise form of the underlying distribution $P$ is often unknown and can only be inferred indirectly from past data in the form of a finite number of samples $x_{1},\ldots,x_{n}\in X$. In this case, one can employ statistical methods to infer an estimated (parametric or non-parametric) distribution $\widehat{P}$ from the available data. However, solving with the estimated $P=\widehat{P}$ may yield solutions that display poor out-of-sample performance due to the unavoidable mismatch between the true underlying distribution and $\widehat{P}$.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In distributionally robust (stochastic) optimization (DRO), the decision-maker hedges against this mismatch by minimizing the worst-case expected loss $\Psi_{\operatorname{WC}}$ with respect to all distributions in a neighborhood of $\widehat{P}$; namely the (unstructured) DRO problem is formulated as where $\mathcal{W}\subseteq\mathcal{P}(X)$ is a set of distributions, called ambiguity set, on the space $\mathcal{P}(X)$ of all distributions supported on $X$. If appropriately chosen, the set $\mathcal{W}$ contains the true underlying distribution, which implies that any solution $\theta_{*}$ to will provide an objective value of $\Psi(\theta_{*})$ lower or equal to $\Psi_{\operatorname{WC}}(\theta_{*})$.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Consequently, the quality of this robust approach heavily depends on the form of the ambiguity set $\mathcal{W}$: while it should be "large enough" to include the true distribution (with high confidence), it should not contain superfluous distributions that cannot realistically appear in the problem at hand as this would lead to unnecessarily conservative solutions. Typical ambiguity sets that appear in the literature include support-, moment-, or distance-based sets of distributions or mixtures thereof. While the first two types of ambiguity sets contain all distributions complying with a specified support and moment information (generally, first and second moments), the distance-based sets include all distributions that are within a certain given "distance" of a fixed nominal distribution. In the latter setting, the nominal distribution is often obtained through statistical techniques from available empirical data, while the distance, commonly expressed in terms of e.g. the $\phi-$divergence, the total variation norm, the kernel mean embedding, or optimal transport based-distances including the celebrated Wasserstein distance, signifies the "trust" in the statistical methods used as well as the obtained data at hand.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Due to the favorable properties of Wasserstein distance in terms of expressivity and statistical properties allowing for finite-sample guarantees, a significant proportion of the recent literature has focused on so-called Wasserstein balls $\mathcal{W}=\mathbb{B}_{\rho}(\widehat{P})$, i.e., sets containing all distributions that are within some Wasserstein-distance $\rho>0$ from a nominal distribution $\widehat{P}$. For finitely supported nominal distributions $\widehat{P}$, the optimization of an expectation over a Wasserstein ball, which is convex, can often be reformulated into a finite-dimensional optimization program by means of Lagrange duality, and solved efficiently via off-the-shelf solvers.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, in several applications, the distributional uncertainty does not enter the problem at hand in an arbitrary fashion, but rather in a *structured* manner. One common structure consists of a set $x=(x_{1},\ldots,x_{N})$ of identically and independently distributed (i.i.d.) random variables $x_{1},\ldots,x_{N}\sim P$, where $P$ is again assumed to belong to a Wasserstein ball $\mathbb{B}_{\rho}(\widehat{P})$. This results in the *structured Wasserstein distributionally robust optimization* problem of the form is a *structured Wasserstein ambiguity set* containing product distributions of the form $\overline{P}=P^{\otimes N}=P\otimes\cdots\otimes P$ only.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Problem arises across several domains, such as (i) control of uncertain dynamical systems, which has traditionally assumed stationarity and independence of the additive noise affecting the system dynamics; (ii) strategically robust game theory, where irrationality in the opponents' actions is captured via a distributionally robust "best response map" that, in case of disjoint agents action sets, takes the form of; (iii) supply chain optimization and/or inventory management of goods with uniform popularity across buyers and shared demand drivers may be approximated as.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the popularity of this structure in stochastic optimization, handling Problem is computationally challenging. In fact, contrary to the problem of evaluating $\Psi_{\operatorname{WC}}(\theta)$, the evaluation of $\Psi_{\operatorname{S}}(\theta)$ now involves optimizing over the non-convex set $\mathcal{W}$ (the non-convexity arises from the nonlinearity in the expectation operator due to the product structure). In turn, this prohibits the use of standard (strong) duality tools to reformulate as an equivalent finite-dimensional optimization program.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Outline and contributions of the paper", "weight": 1.0} -->

We consider data-driven DRO problems with Wasserstein ambiguity sets, where the uncertainty affects the problem in an i.i.d. fashion, as. Specifically, we first examine the problem of evaluating the inner supremum of for a fixed, given $\theta\in\Theta$, i.e. computing the so-called *(primal) uncertainty quantification (UQ) problem* where $\mathcal{W}$ is defined. After introducing the necessary background in Section 2, we establish conditions under which is finite and attains its optimum in Section 3.1. Moreover, there we also show that can be upper-bounded by a standard Wasserstein uncertainty quantification problem. Next, in Section 3.2 we show that the latter upper bound is in general conservative and propose a potentially tighter upper bound based on symmetrization of the corresponding loss $\ell$ that allows for strong duality. Further, in Section 3.4, using the concept of lifting and based on the previous bound, we introduce a nonincreasing sequence of upper bounds (relaxations) on that admit strong duality.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Outline and contributions of the paper", "weight": 1.0} -->

We investigate the properties of this sequence of relaxations in Section 3.5. As a main result, in Section 3.6, we show in Theorem 10 that the gap between the lower bound of the relaxation sequence and vanishes if $\ell$ is concave. Additionally, in Section 3.7 we show that for sets of the form $\mathcal{W}$ our upper bound established in Section 3.2 is not more conservative than an upper bound provided. Furthermore, in Section 4 we turn back to Problem 3 and show that if $\ell=\ell(\theta,x)$ is convex-concave, then the minimizers of the sequence of relaxed problems, if existent, converge to the set of minimizers of Problem 3. Finally, in Section 5 we formulate the strong duality for the relaxation sequence as a second order cone program whenever $\ell$ is a polyhedral loss function and provide some numerical examples.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Wasserstein distributionally robust optimization", "weight": 1.0} -->

Consider now an uncertainty quantification problem of the type where $\ell:X\to\mathbb{R}$ is a Borel measurable loss functional and corresponds to the inner problem of with $\ell=\ell(\theta,\cdot)$ for a fixed $\theta$. To study the finiteness and existence of optimizers, define the set of functions with sublinear growth as and consider the following function growth classes: The following result establishes the well-posedness of the problem formulation in ([7).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Structured Uncertainty Quantification", "weight": 1.0} -->

In this section, we are interested in the inner optimization problems of, namely for some $N\in\mathbb{N}$, Borel measurable $\ell:X^{N}\to\mathbb{R}$ and In its stated form problem is non-convex, since the set $\mathcal{W}$ is non-convex. The following subsections investigate different aspects of this problem in more detail. We confine the proofs of the subsequent results to the appendix for expositional clarity. Unless stated otherwise, we assume that the transportation cost $c$ is proper and $\widehat{P}\in\mathcal{P}_{c}(X)$ throughout.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Finiteness and existence of optimizers", "weight": 1.0} -->

First we delve into when is well-defined, finite and attains its solution on $\mathcal{W}$. For $N\in\mathbb{N}$ we write $c^{N}:X^{N}\times X^{N}\to[0,\infty):(x,y)\mapsto\sum_{i=1}^{N}c(x_{i},y_{i})$ for the $N$-lift of the transport cost $c$. In some cases we will omit the superscript $N$ and write again $c$ instead of $c^{N}$ for brevity.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Finiteness and existence of optimizers", "weight": 1.0} -->

To start, we note that for $N\in\mathbb{N}$ the set $\mathcal{W}$ can be overestimated by an ordinary Wasserstein ball w.r.t. the lifted transportation cost.

<!-- chunk {"id": "body-0017", "role": "body", "section": "A convex upper bound", "weight": 1.0} -->

In the previous section we have seen that states an upper bound. In general this bound will be conservative as the following example shows.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Example 1", "weight": 1.0} -->

Let $X=\mathbb{R}$, $N=2$, $c(x_{1},x_{2})=\lvert x_{1}-x_{2}\rvert^{2}$, $\widehat{P}=\delta_{0}$ and $\ell(x_{1},x_{2})=\frac{1}{2}(x_{1}-x_{2})^{2}$. Then the value of the structured problem is with $P=\frac{1}{2}\delta_{-\sqrt{\rho}}+\frac{1}{2}\delta_{\sqrt{\rho}}$ showing that in fact the latter bound is attained. On the other hand, the value of the right hand side of can be computed using Theorem 2. ‣ 2.2. Wasserstein distributionally robust optimization ‣ 2. Notation and Preliminaries ‣ Distributionally Robust Optimization over Wasserstein Balls with i.i.d.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Example 1", "weight": 1.0} -->

Structure") and is given by The next example shows that the conservatism of this bound can be arbitrary large in a relative sense.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Example 2", "weight": 1.0} -->

Let $X=\mathbb{R}$, $N=2$, $c(x_{1},x_{2})=\lvert x_{1}-x_{2}\rvert^{2}$, $\widehat{P}=\frac{1}{2}\delta_{1}+\frac{1}{2}\delta_{-1}$ and $\ell(x_{1},x_{2})=-x_{1}x_{2}$. Then the value of the structured problem is The value of the right hand side of is, after some elementary calculations, given by Hence, while the value of the structured problem is constant, the value of the latter bound grows asymptotically linearly as the ball radius increases.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Example 2", "weight": 1.0} -->

In view of the last two examples we turn to the question whether we can obtain better bounds on than. This corresponds to obtaining tighter convex overestimations of the set $\mathcal{W}$ than the one given. Clearly, the best such overestimation is the convex hull $\operatorname{conv}\mathcal{W}$ and indeed even more is true.

<!-- chunk {"id": "body-0022", "role": "body", "section": "A tighter convex upper bound", "weight": 1.0} -->

While the bound can be quite conservative, we can establish tighter bounds by using the following, general, principle: Suppose that there exists some class $\mathcal{F}$ of transformations $F:\mathbb{R}^{X^{N}}\to\mathbb{R}^{X^{N}}$ such that $\operatorname{id}\in\mathcal{F}$, $F(\ell)$ is Borel measurable for any Borel measurable $\ell:X^{N}\to\mathbb{R}$ and Then, for any Borel $\ell:X^{N}\to\mathbb{R}$, it holds that is a potentially tighter upper bound on $\operatorname{S}(\ell)$ than $\operatorname{U}(\ell)$. Similar arguments have been used in to obtain convex upper bounds on the structured singular value in the domain of control theory.

<!-- chunk {"id": "body-0023", "role": "body", "section": "A tighter convex upper bound", "weight": 1.0} -->

To obtain such a class $\mathcal{F}$ for our problem, we make the following, crucial observation: If $\pi\in\mathcal{S}_{N}$ is a permutation, then the transformation $F_{\pi}:\ell\mapsto\ell_{\pi}$ with $\ell_{\pi}(x)=\ell(\pi(x))$, where $\pi(x)=(x_{\pi},\ldots,x_{\pi(N)})$ for $x\in X^{N}$, satisfies since $\pi\#P^{\otimes N}=P^{\otimes N}$ for any permutation $\pi$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "A tighter convex upper bound", "weight": 1.0} -->

Moreover, since $\mathbb{E}_{x\sim\overline{P}}\ell$ is linear in $\ell$, it follows that holds for where $\Delta^{\mathcal{S}_{N}}=\{\alpha=(\alpha_{\pi})_{\pi\in\mathcal{S}_{N}}\in^{\mathcal{S}_{N}}\mid\sum_{\pi\in\mathcal{S}_{N}}\alpha_{\pi}=1\}$ is the standard simplex in the $N!$-dimensional Euclidean space. This implies that holds for the above class $\mathcal{F}$ of transformations. In this specific case we can actually establish the following

<!-- chunk {"id": "body-0025", "role": "body", "section": "Example 3", "weight": 1.0} -->

Let $X=\mathbb{R}$, $N=2$, $c(x_{1},x_{2})=\lvert x_{1}-x_{2}\rvert^{2}$, $\widehat{P}=\frac{1}{2}\delta_{1}+\frac{1}{2}\delta_{-1}$ and $\ell(x_{1},x_{2})=-2x_{1}^{2}-2x_{1}x_{2}$. Then the value of the structured problem is given by The value of the unstructured bound is, after some elementary calculations, while the value of the symmetrized bound is See Figure 1(a) for a graphical illustration.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Example 3", "weight": 1.0} -->

(a) Objective values for Example 3 (b) Objective values for Example 4 Figure 1. Objective values for Examples 3 and 4 For the purpose of interpreting the upper bound $\operatorname{U}(\ell_{\operatorname{sym}})$ in terms of an overestimation of the set $\overline{\operatorname{conv}}^{\operatorname{w}}\mathcal{W}$ we need the following

<!-- chunk {"id": "body-0027", "role": "body", "section": "Sequence of convex relaxations", "weight": 1.0} -->

It is interesting to ask now whether we can find even tighter overestimations of $\overline{\operatorname{conv}}^{\operatorname{w}}\mathcal{W}$ than $\mathbb{B}_{N\rho}^{c^{N}}(P^{\otimes N})_{\operatorname{sym}}$. In view of the latter question is equivalent to determining a property that distinguishes powers of measures in the set of all symmetric measures. The crucial observation is that powers of powers of measures are again powers of measures and hence symmetric, while the same does not have to be true for general symmetric measures.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Sequence of convex relaxations", "weight": 1.0} -->

This latter viewpoint hints us to lift our problem and consider instead of the problem where $N\leq M\leq\infty$ is a "lifting parameter" and $\operatorname{pr}_{1:N}^{M}:X^{M}\to X^{N}$ is the projection onto the first $N$ components, i.e. in we see the function $\ell$ on $X^{N}$ as a function $\widehat{\ell}=\ell\circ\operatorname{pr}_{1:N}^{M}$ on $X^{M}$. Analogously we define the quantities Note that has the same optimal value as, since integrating w.r.t. extra factors $P$ does not change the value of the integral, i.e. $\operatorname{S}_{N}(\ell)=\operatorname{S}_{M}(\ell\circ\operatorname{pr}_{1:N}^{M})$ for any $M\geq N$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Sequence of convex relaxations", "weight": 1.0} -->

In view of it then follows that Note that here $\widehat{\ell}_{\operatorname{sym}}$ denotes the symmetrization of $\ell$ viewed as a function $X^{M}\to\mathbb{R}$ and thus itself depends on $M$. To summarize, for each $M\geq N$ we obtain an upper bound on $\operatorname{S}(\ell)$. It then holds that^33^3the use of the notation $\operatorname{U}_{\infty}^{\operatorname{sym}}(\ell)$ is justified by Lemma 4 stated below.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Sequence of convex relaxations", "weight": 1.0} -->

We stress again that, contrary to the original problem $\operatorname{S}(\ell)$, *we can evaluate each* $\operatorname{U}_{M}^{\operatorname{sym}}(\ell)$ via Theorem 2. ‣ 2.2. Wasserstein distributionally robust optimization ‣ 2. Notation and Preliminaries ‣ Distributionally Robust Optimization over Wasserstein Balls with i.i.d. Structure") by using the relation (see also Section 5.1). For notational brevity we also set $\operatorname{U}_{0}^{\operatorname{sym}}(\ell):=\operatorname{U}(\ell)$ for the non-symmetrized bound defined as the right side of. The following theorem establishes when $\operatorname{U}_{M}^{\operatorname{sym}}(\ell)$ is finite and attained.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Example 4", "weight": 1.0} -->

Let $X$, $N$, $c$, $\widehat{P}$ and $\ell$ be as in Example 2. After some elementary calculations (see Appendix) we obtain i.e. for a fixed $\rho>0$ it follows $\lim_{M\to\infty}\operatorname{U}_{M}^{\operatorname{sym}}(\ell)=0=\operatorname{S}(\ell)$. See Figure 1(b) for a graphical illustration.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Example 4", "weight": 1.0} -->

In view of Example 4 it is now natural to ask under which conditions the inequality in is an equality, i.e. when the sequence of *relaxations* is tight and there is no relaxation gap. For this we will investigate this gap in the next section in more detail.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Relaxation gap", "weight": 1.0} -->

To understand the gap between $\operatorname{S}(\ell)$ and $\operatorname{U}_{\infty}^{\operatorname{sym}}(\ell)$ it is helpful to first understand the lifting relaxation $\operatorname{U}_{M}^{\operatorname{sym}}(\ell)$ in terms of overestimations of $\overline{\operatorname{conv}}^{\operatorname{w}}\mathcal{W}$. For this purpose we unfold the definitions to obtain i.e. we overestimate $\overline{\operatorname{conv}}^{\operatorname{w}}\mathcal{W}$ by sets of the form, which consist of all marginal distributions onto the first $N$ factors of symmetric distributions in $\mathbb{B}_{M\rho}^{c^{M}}(\widehat{P}^{\otimes M})$. The following lemma establishes some properties of the sets.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Example 5", "weight": 1.0} -->

Note that in this example $\ell$ does not satisfy the growth assumption $\ell\in\mathcal{G}_{c^{2}}(X^{2})$, which is sufficient for the finiteness of the unstructured UQ problem, but not necessary for the finiteness of the structured version. The question of whether there exists an example with a non-zero relaxation gap such that is finite, remains open.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Tightness of the relaxation sequence", "weight": 1.0} -->

Intuitively, replacing a constraint by its average will not increase the optimal value if any "average feasible" point can be replaced by a single point that satisfies the original constraint without decreasing its objective value. If the latter "replacement" is done by taking the average, i.e. taking the mean $\mathbb{E}_{x\sim\nu}x$ of $\nu$ itself, then Jensen's inequality shows that concavity of the objective function $F$ is sufficient for the absence of a relaxation gap. The following theorem gives a sufficient condition for the function $F_{\ell}(P)=\int\ell\,\text{d}P^{\otimes N}$ to be convex in the sense of the usual linear structure on $\mathcal{P}(X)$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Tightness of the relaxation sequence", "weight": 1.0} -->

For this we need to introduce the following notion \[41, Definition 8.1\]: A function $k:X\times X\to\mathbb{R}$ is said to be conditionally negative definite (c.n.d.) if for any $n\in\mathbb{N}$, $\gamma\in\mathbb{R}^{n}$ and $x\in X^{n}$ the matrix $(k(x_{i},x_{j}))_{i,j=1}^{n}$ is negative semi-definite on the subspace $\mathbbm{1}^{\top}\gamma=0$, i.e. if The result reads now as follows.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Example 6", "weight": 1.0} -->

Let $X$, $N$, $c$ and $\ell$ be as in Example 4, $\ell(x_{1},x_{2})=-x_{1}x_{2}$. Then $\ell$ is (conditionally) negative definite, since if $x\in X^{n}$ and $\gamma\in\mathbb{R}^{n}$ are such that $\mathbbm{1}^{\top}\gamma=0$, then Thus, the conclusion of Theorem 9 is consistent with Example 4.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Example 6", "weight": 1.0} -->

Unfortunately, verifying conditional negative definiteness in practice can be challenging. It turns out, however, that if $X$ is additionally a vector space and $\ell:X^{N}\to\mathbb{R}$ is concave, then $F_{\ell}$ is *geodesically concave* in the sense of the Wasserstein space on $\mathcal{P}_{c}(X)$. We will not introduce the concepts of geodesic convexity or concavity here, since they will not be needed any further in this paper, but just note that the so-called *Wasserstein geodesics* provide a way of interpolating between two distributions $P_{1}$ and $P_{2}$ in $\mathcal{P}_{c}(X)$ that is *different* from $\alpha P_{1}+(1-\alpha)P_{2}$. Thus, if the average w.r.t.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Example 6", "weight": 1.0} -->

$\nu$ is understood in a different, namely *geodesic* sense, then we can indeed show the relaxation gap again to be zero. The price to pay, however, is that the underlying feasible set $\mathbb{B}_{\rho}^{c}(\widehat{P})$ is convex w.r.t. this new notion of convexity as well, which requires an additional assumption on the transportation cost $c$. The following theorem summarizes these observations and is the main result of this section.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Note that Theorem [9 and Theorem 10 are not subcases of each other and rely on different notions of convex interpolation. The problem of determining the largest class of functions $\ell$ with a zero relaxation gap remains open.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Comparison to", "weight": 1.0} -->

As already noted in the introduction to this section, Wasserstein ambiguity sets with additional structure have not been considered much in the literature with one notable exception given, where non-convex uncertainty sets of the form are considered and termed Wasserstein hyperrectangles^55^5in fact, allows for different spaces $X_{k}$ in each coordinate, but we will focus on the case $X_{k}=X$ for all $k=1,\ldots,N$. Note that even in the case of $\rho_{i}=\rho$, $c_{i}=c$ and $\widehat{P}_{i}=\widehat{P}$ for all $i=1,\ldots,N$ sets of the form are different from sets in that they allow each factor $P_{i}\in\mathbb{B}_{\rho}^{c}(\widehat{P})$ to depend on the index $i$. Thus clearly in this case Now, in a duality result is established for UQ problems w.r.t.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Comparison to", "weight": 1.0} -->

sets and functions $\ell:X^{N}\to\mathbb{R}$ that are additively and multiplicatively *separable*, i.e. are of the form for some $\ell_{k}:X\to\mathbb{R}$, $k=1,\ldots,N$, respectively. However, this requirement of the loss $\ell$ is very restrictive and in this case which implies that the structured UQ problem splits into $N$ decoupled and unstructured problems of the form. For this reason we will not state the latter duality here explicitly.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Comparison to", "weight": 1.0} -->

Further also consider the so-called *multitransport hyperrectangles* that are defined for given $\check{P}\in\mathcal{P}(X^{N})$, costs $c_{k}$ and radii $\rho_{k}$ as^66^6Here $\operatorname{pr}_{k,k}:X^{N}\times X^{N}\to X\times X$ is the projection onto the $k$-th coordinates in each $X^{N}$. See Appendix A for additional notation.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Relaxations of the distributionally robust optimization problem", "weight": 1.0} -->

In this section we return to the problem and examine the implications of replacing its inner uncertainty quantification problem by its relaxed version, i.e. replacing, where $\Psi_{\operatorname{S}}(\theta)=\operatorname{S}(\ell(\theta,\cdot))$ in the notation of the previous section, by the problem where this time we explicitly see $\ell:\Theta\times X^{N}\to\mathbb{R}$ as a function of two arguments $(\theta,x)\in\Theta\times X^{N}$. The following result relates the solutions of the relaxed problem to solutions of.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The uniform integrability assumption on $\{-\min\{\ell(\theta,\cdot),0\}\}_{\theta\in\Theta}$ is used to establish the lower semi-continuity of $\Psi_{\operatorname{S}}$ on $\Theta$ only and is satisfied if e.g. there exists a constant $C>0$ and $x_{0}\in X^{N}$ such that i.e. $-\ell(\theta,\cdot)$ "belong uniformly in $\theta\in\Theta$" to the class $\mathcal{G}_{c^{N}}(X^{N})$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Thus Theorem 13 provides a guarantee that (possibly suboptimal) solutions of the relaxed problem will approximate the true minimizers of if $\ell$ is a saddle (i.e. convex-concave) function with certain integrability and continuity properties. Note, however, that even without any convexity or concavity assumptions on $\ell$, it can be beneficial to solve as a substitute to. Indeed, suppose that we want to find a decision vector $\theta^{*}\in\Theta$ that satisfies a robustness margin given by a threshold $R\in\mathbb{R}$, i.e.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Remark 2", "weight": 1.0} -->

If we now solve instead for some fixed $M\geq N$ to (sub)optimality and obtain a decision vector $\theta_{M}^{*}\in\Theta$ with an objective value $\Psi_{\operatorname{U}}^{M}(\theta_{M}^{*})\leq R$, then after implementing $\theta_{M}^{*}$ in our original problem, we obtain i.e. we can take $\theta^{*}=\theta_{M}^{*}$ to meet the desired specifications.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Tractable reformulations and numerical examples", "weight": 1.0} -->

In this section we reformulate each uncertainty quantification problem in the proposed sequence of relaxations into an explicit finite-dimensional convex program and provide some numerical examples.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Finite-dimensional reformulations using Lagrange duality", "weight": 1.0} -->

When the nominal distribution $\widehat{P}$ is discrete, i.e. the value of $\operatorname{U}_{M}^{\operatorname{sym}}(\ell)$ as defined in can be evaluated for any $M\geq N$ by reformulating into a semi-infinite program via Theorem 2. ‣ 2.2. Wasserstein distributionally robust optimization ‣ 2. Notation and Preliminaries ‣ Distributionally Robust Optimization over Wasserstein Balls with i.i.d. Structure") in the following way.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Finite-dimensional reformulations using Lagrange duality", "weight": 1.0} -->

Structure") as well as the fact that is also discrete. By introducing slack variables $\sigma_{\boldsymbol{i}}\in\mathbb{R}$ for $\boldsymbol{i}\in\widehat{I}$, we obtain the semi-infinite program When $X=\mathbb{R}^{n}$ is Euclidean and the loss $\ell$ and cost $c$ belong to some particular classes of functions, the latter constraints can be reformulated more explicitly. In view of Theorem 10 we focus on concave polyhedral loss function $\ell$ and cost $c(x,y)=\lVert x-y\rVert$ for some norm $\lVert\cdot\rVert$ on $\mathbb{R}^{n}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Concave polyhedral loss", "weight": 1.0} -->

Suppose that $\ell:(\mathbb{R}^{n})^{N}\to\mathbb{R}$ concave and polyhedral, i.e. of the form where $\mathcal{H}\subseteq(\mathbb{R}^{n})^{N}\times\mathbb{R}$ is a polytope. Additionally, suppose that $c(x,y)=\lVert x-y\rVert$ for some norm $\lVert\cdot\rVert$ on $\mathbb{R}^{d}$. Before we state our reformulation, we need to introduce some additional notation.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Concave polyhedral loss", "weight": 1.0} -->

Let $\boldsymbol{\widehat{\mathcal{I}}}=\boldsymbol{\widehat{I}}/\sim$ be the set of equivalence classes with $\boldsymbol{\iota}=[\boldsymbol{i}]_{\sim}$ being the equivalence class of $\boldsymbol{i}$ and let $\upsilon:\boldsymbol{\widehat{\mathcal{I}}}\to\boldsymbol{\widehat{I}}$ denote an arbitrary, but fixed selection such that $\upsilon(\boldsymbol{\iota})\in\boldsymbol{\iota}$ for all $\boldsymbol{\iota}\in\boldsymbol{\widehat{\mathcal{I}}}$. Finally, for any norm $\lVert\cdot\rVert$ we denote by $\lVert\cdot\rVert_{*}$ its dual norm. The following result holds.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Remark 4", "weight": 1.0} -->

The program involves (for $M\to\infty$) decision variables and constraints. While this is polynomial in the lifting parameter $M$, it can be solved only for small values of $N$ and $n_{\widehat{P}}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Numerical results", "weight": 1.0} -->

We conclude this paper by illustrating the proposed method on synthetic examples.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Structured uncertainty quantification", "weight": 1.0} -->

In this case it holds^77^7In real practice this value is not known and the tuning of the radius of the ambiguity set is typically done via e.g. cross-validation $W_{c}(P^{\star},\widehat{P})\approx 0.19$. To hedge against the distributional ambiguity, we the structured ambiguity set $\mathcal{W}$ around $\widehat{P}$ with $\rho=0.2$. We compute the optimal value of the relaxed problem for different values of the lifting parameter $M$ using Theorem 14. For comparison, we compute the optimal value of the unstructured DRO problem that uses the ambiguity set in with the same radius. The results are shown in Figure 2. We observe that the relaxation gap decreases monotonically as $M\to\infty$, corroborating our theoretical findings. The substantial gap between the structured and the unstructured DRO value at $M=50$ when a plateau is reached confirms that is a loose over-approximation of the original non-convex structured ambiguity set.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Structured distributionally robust optimization", "weight": 1.0} -->

Consider $X=\mathbb{R}$, $N=2$, $c(x,y)=\lVert x-y\rVert_{2}$, $\Theta=\subseteq\mathbb{R}$ as well as where the polytope $\mathcal{H}(\theta)\subseteq\mathbb{R}^{3}$ is given by $\mathcal{H}(\theta)=\{h\in\mathbb{R}^{3}\mid Wh\leq g(\theta)\}$ for It is easily verified that $\ell$ is a saddle function and satisfies the assumptions of Theorem 13. Solving the relaxed problems with $\widehat{P}=\frac{1}{2}\delta_{1}+\frac{1}{2}\delta_{-1}$ and $\rho=1/4$ to optimality yields a sequence of decisions $(\theta_{M}^{*})_{M\geq N}\subseteq\Theta$ and objective

<!-- chunk {"id": "body-0057", "role": "body", "section": "Structured distributionally robust optimization", "weight": 1.0} -->

values $\Psi_{\operatorname{U}}^{M}(\theta_{M}^{*})=\inf_{\Theta}\Psi_{\operatorname{U}}^{M}$, which are depicted in Figure 3. We also depict the sequence of objective values $\Psi_{\operatorname{S}}(\theta_{M}^{*})$ of the original problem ^88^8Since we cannot exactly compute $\Psi_{\operatorname{S}}$, we approximate it by $\Psi_{\operatorname{U}}^{M}$ for a large, fixed $M\geq N$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Structured distributionally robust optimization", "weight": 1.0} -->

We observe that both $\Psi_{\operatorname{U}}^{M}(\theta_{M}^{*})$ and $\Psi_{\operatorname{S}}(\theta_{M}^{*})$ converge to a limiting value for $M\to\infty$, which, by Theorem 13, is equal to $\inf_{\Theta}\Psi_{\operatorname{S}}$. However, we can also see that the convergence is highly non-monotone in $M$, which motivates Remark 3.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Structured distributionally robust optimization", "weight": 1.0} -->

(a) Relaxted objective values ΨUM(θM*) and original objective values ΨS(θM*) (b) Optimal decision vector θM* ∈ Θ Figure 3. Objective values and optimal decision vectors for the example from Section 5.2.2.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusions and Outlook", "weight": 1.0} -->

In this paper, we focused on Wasserstein DRO formulations where the uncertain vector exhibits an i.i.d. structure. By exploiting this structure, we construct a structured ambiguity set that only contains product distributions. To solve the resulting non-convex program, we devise a sequence of convex relaxations that, under mild conditions on the loss function, converge to the optimal solution of the original non-convex problem. Our numerical results certify how structured ambiguity sets can capture uncertainty in a more effective manner than unstructured ambiguity sets, ultimately improving the overall decision-making. Future work includes (i) the analysis of the relaxation gap for convex loss functions, (ii) addressing the computational tractability issues of data-driven problems where the product of empirical distributions is supported on a exponential amount of points and finally (iii) extending the results to exploit invariance w.r.t. groups $G$ other than the symmetric group $\mathcal{S}_{N}$.
