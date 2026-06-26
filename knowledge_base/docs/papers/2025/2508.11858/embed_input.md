<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimality of Linear Policies in Distributionally Robust Linear Quadratic Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study a generalization of the classical discrete-time, Linear-Quadratic-Gaussian (LQG) control problem where the noise distributions affecting the states and observations are unknown and chosen adversarially from divergence-based ambiguity sets centered around a known nominal distribution. For a finite horizon model with Gaussian nominal noise and a structural assumption on the divergence that is satisfied by many examples - including 2-Wasserstein distance, Kullback-Leibler divergence, moment-based divergences, entropy-regularized optimal transport, or Fisher (score-matching) divergence - we prove that a control policy that is affine in the observations is optimal and the adversary's corresponding worst-case optimal distribution is Gaussian. When the nominal means are zero (as in the classical LQG model), we show that the adversary should optimally set the distribution's mean to zero and the optimal control policy becomes linear. Moreover, the adversary should optimally ``inflate" the noise by choosing covariance matrices that dominate the nominal covariance in Loewner order.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Exploiting these structural properties, we develop a Frank-Wolfe algorithm whose inner step solves standard LQG subproblems via Kalman filtering and dynamic programming and show that the implementation consistently outperforms semidefinite-programming reformulations of the problem. All structural and algorithmic results extend to an infinite-horizon, average-cost formulation, yielding stationary linear policies and a time-invariant Gaussian distribution for the adversary. Lastly, we show that when the divergence is 2-Wasserstein, the entire framework remains valid when the nominal distributions are elliptical rather than Gaussian.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Linear Quadratic Gaussian (LQG) control problem has served as a fundamental building block for a wide range of applications in management \Bensoussan et al., [2007, Holt et al., 1955\], economics \Hansen and Sargent finance \Abeille et al. engineering \Auger et al., [2013, Chen, 2012\], or medicine \Patek et al., [2007, Chakravarty et al., 2020, Kazemian et al., 2019, Todorov and Jordan, 2002\].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The discrete-time, finite-horizon formulation considers the problem of minimizing the expected costs incurred when controlling a linear dynamical system over a finite number of periods $t\in\{0,1,\dots,T-1\}$. The system evolves according to the equations where $x_{t}\in\mathbb{R}^{n}$ denotes the system states, $u_{t}\in\mathbb{R}^{m}$ denotes the control inputs, $w_{t}\in\mathbb{R}^{n}$ denotes an exogenous noise process, and the system matrices $A_{t}\in\mathbb{R}^{n\times n}$ and $B_{t}\in\mathbb{R}^{n\times m}$ are known.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The decision maker only has access to imperfect state measurements corrupted by exogenous observation noise $v_{t}\in\mathbb{R}^{p}$, where $C_{t}\in\mathbb{R}^{p\times n}$ and usually $p\leq n$ (so that observing $y_{t}$ does not allow perfectly reconstructing $x_{t}$ even without observation noise).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The control inputs $u_{t}$ are *causal*, i.e., depend on the past observations $y_{0},\ldots,y_{t}$ but not on the future observations $y_{t+1},\ldots,y_{T-1}$, so that the set of feasible control inputs $\mathcal{U}_{y}$ is the set of random vectors $u=(u_{0},u_{1},\dots,u_{T-1})$ such that $u_{t}=\varphi_{t}(y_{0},\ldots,y_{t})$ for every $t$, where $\varphi_{t}:\mathbb{R}^{p(t+1)}\rightarrow\mathbb{R}^{m}$ is a measurable control policy.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Controlling the system generates quadratic costs: where $Q_{t}\in\mathbb{R}^{n\times n}$ are positive semidefinite matrices governing the state costs, and $R_{t}\in\mathbb{R}^{m\times m}$ are positive definite matrices governing the input costs. Under the assumption that the joint probability distribution $\mathbb{P}$ for the noise terms is known, the classical LQG problem seeks causal control inputs that minimize the expected costs under the distribution $\mathbb{P}$, i.e., $\inf_{u\in\mathcal{U}_{y}}\mathbb{E}_{\mathbb{P}}[J(u)]$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

To prove structural results and design tractable algorithms for solving this problem, several assumptions on the probability distribution $\mathbb{P}$ are typically needed. Under the premise that all noise terms have zero means and are mutually independent, it is known that the problem admits an optimal control policy of the form $u^{\star}_{t}=K_{t}\hat{x}_{t}$ for every $t\in\{0,\dots,T-1\}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Here, the feedback gain matrices $K_{t}\in\mathbb{R}^{m\times n}$ only depend on the system and cost matrices $\{A_{\tau},B_{\tau},Q_{\tau},R_{\tau}\}_{\tau\geq t}$ and can be obtained by solving a set of recursive equations for a system without noise, and $\hat{x}_{t}=\mathbb{E}_{\mathbb{P}}[x_{t}|y_{0},\ldots,y_{t}]$ is the minimum mean-squared-error (MMSE) estimator of the state $x_{t}$ given the history of observations $y_{0},\dots,y_{t}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

This *separation principle* holds regardless of the specific probability distribution $\mathbb{P}$, but does not readily lead to tractable algorithms because calculating the MMSE estimator $\hat{x}_{t}$ is intractable for general probability distributions $\mathbb{P}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

As such, the LQG model also makes the additional assumption that $\mathbb{P}$ is *Gaussian*^11^1Note that if $\mathbb{P}$ is a multivariate Gaussian distribution, the requirement that noise terms are independent can be relaxed to only requiring that they are uncorrelated, i.e., $\mathbb{E}_{\mathbb{P}}[z^{\prime}z^{\top}]=0$ for all $z\neq z^{\prime}\in\{x_{0},w_{0},\ldots,w_{T-1},v_{0},\ldots,v_{T-1}\}$., in which case the optimal state estimator $\hat{x}_{t}$ depends linearly on the history of observations $y_{0},\dots,y_{t}$ and can be obtained efficiently with Kalman filtering techniques.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

(We refer the reader to Appendix A for an overview and to Bertsekas for a detailed discussion of these classical results.)

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by practical settings where noise distributions may not be readily available or may not be Gaussian, we consider a generalization of the discrete-time LQG model where an adversary chooses the noise distributions from an ambiguity set $\mathcal{B}$ characterized by a divergence $\mathds{D}$ and centered around a known nominal distribution $\hat{\mathbb{P}}$, and the decision maker's goal is to minimize the costs incurred under the worst-case distribution, $\sup_{\mathbb{P}\in\mathcal{B}}\mathbb{E}_{\mathbb{P}}[J(u)]$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

This optimization problem -- which we refer to as the distributionally-robust linear quadratic (DRLQ) problem -- is challenging: both the decision maker and nature are optimizing over infinite-dimensional spaces, and the ambiguity set $\mathcal{B}$ contains many non-Gaussian distributions, so it is not obvious which structural results from the LQG model would continue to hold or how one could compute an optimal control policy.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

We first consider the finite-horizon case when the nominal distribution $\hat{\mathbb{P}}$ is Gaussian with zero mean, as in the classical LQG model. We construct ambiguity sets containing all distributions whose "distance" from the nominal distribution -- measured according to a divergence $\mathds{D}$ -- is not too large. We restrict attention to distributions under which the exogenous noise terms are allowed to have non-zero means, but are required to have finite second moments that satisfy an orthogonality condition requiring cross second moments to vanish. When noise terms are zero-mean, this second-moment orthogonality (SMO) condition is equivalent to requiring the noise terms to be uncorrelated, which is also a standard requirement in the classical LQG model. We require the divergence $\mathds{D}$ to satisfy a key condition, which we verify for several important examples such as 2-Wasserstein distance, Kullback-Leibler divergence, moment-based divergences, entropy-regularized optimal transport, and Fisher divergence. (The first three examples are discussed in the main text and the last two in the Appendix.)

<!-- chunk {"id": "body-0017", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

Within this framework, we prove that an optimal control policy exists that is *affine* in the observations, $u_{t}^{\star}=q_{t}+\sum_{\tau=0}^{t}U_{t,\tau}y_{\tau}$ for $q_{t}\in\mathbb{R}^{m}$ and $U_{t,\tau}\in\mathbb{R}^{m\times p}$, and that the associated worst-case optimal distribution $\mathbb{P}^{\star}$ is *Gaussian*. Our proof is novel and does not rely on traditional recursive dynamic programming arguments. Instead, we re-parameterize the control policy using purified observations and derive an upper bound for the resulting minimax formulation by relaxing the ambiguity set (to an outer approximation determined by the first two moments) while simultaneously restricting the decision maker to affine policies. We then use convex duality to show that the upper bound matches a lower bound obtained by restricting the ambiguity set (to Gaussian distributions) in the dual of the minimax formulation.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

The matching bounds then certify the optimality of affine output-feedback policies for the decision maker and of Gaussian distributions for the adversary.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

Under two mild and intuitive assumptions that hold for every divergence we consider, we derive additional structural results that yield sharp managerial insights and facilitate computation.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

The first result concerns the means of the noise terms. We prove that the adversary's worst-case distribution $\mathbb{P}^{\star}$ sets the noise mean to zero, and thus the worst-case exogenous noise terms are uncorrelated. Whereas the vast majority of papers formulating robust LQG models restrict attention to zero-mean (and uncorrelated) noise for simplicity or in keeping with the classical LQG assumptions, our findings provide a different justification: this assumption/choice is *conservative*, because allowing the adversary to use zero means gives the adversary more power and results in the worst-case costs for the decision maker. Moreover, we prove that when noise is zero-mean, the optimal control policy becomes purely *linear* in the outputs, $u_{t}^{\star}=\sum_{\tau=0}^{t}U_{t,\tau}y_{\tau}$. The intuition is straightforward: any deterministic bias that nature may introduce can be anticipated and neutralized by a suitable affine shift in the control policy, so it offers the adversary no advantage.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

In equilibrium, neither player employs predictable offsets, so when the nominal means are zero, the decision maker also sets the intercepts to zero without incurring any optimality loss.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

The second result pertains to the covariance of the noise terms. Restricting attention to zero-mean distributions and linear control policies, we prove that nature's optimal choice of covariance matrix $\Sigma^{\star}$ dominates the covariance matrix of the nominal distribution $\hat{\Sigma}$ in Loewner order, $\Sigma^{\star}\succeq\hat{\Sigma}$. Nature therefore spends its ambiguity budget by suitably "inflating" the nominal covariance matrix $\hat{\Sigma}$, which increases the noise level and, consequently, the decision maker's optimal costs. This finding formalizes the familiar principle that higher variance entails greater uncertainty, extending it to the dynamic setting of distributionally robust LQG control. A practical implication follows immediately: when model misspecification is a concern, a simple yet effective safeguard (even against adversarial distributional ambiguity) is to up-scale the nominal covariance matrix and solve a nominal model under the resulting noisier Gaussian distribution.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

We leverage these structural results to design efficient algorithms for finding optimal control policies in the DRLQ problem. We propose an algorithm based on a Frank-Wolfe first-order method that solves at each iteration sub-problems corresponding to classical LQG control problems, using Kalman filtering and dynamic programming. We show that this algorithm enjoys a sublinear convergence rate and is susceptible to parallelization. Our PyTorch implementation, which relies on automatic differentiation, yields uniformly lower runtime than a direct method based on semidefinite programming, outperforming it across every problem horizon and instance we tested. Moreover, the optimal robust policy significantly reduces worst-case costs while exhibiting virtually no performance loss when the nominal distribution is in fact correct.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

We then extend our structural results to an infinite-horizon formulation of the DRLQ problem with average-cost objective, time-invariant system matrices, and time-invariant nominal distribution $\hat{\mathbb{P}}$. Importantly, we do not require the control policies or all distributions in the ambiguity set to be stationary. This setting raises additional technical hurdles that require strengthening the assumptions of the finite-horizon case. However, under assumptions that mirror the classical LQG assumptions for infinite-horizon models, we prove that a time-invariant, *stationary*, linear control policy $u^{\star}$ is optimal and that the worst-case distribution $\mathbb{P}^{\star}$ is a *time-invariant* Gaussian distribution. The result not only generalizes our finite-horizon findings but also aligns seamlessly with the structural insights long-observed in traditional infinite-horizon LQG settings with known distributions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

The Appendix elaborates on several extensions of the framework. §F and §G confirm that all our structural results hold when the divergence $\mathds{D}$ is chosen as the entropy-regularized optimal transport divergence or as the Fisher divergence (also known as score-matching distance), respectively. §H then replaces the nominal Gaussian distribution with an *elliptical* nominal distribution $\hat{\mathbb{P}}$ with finite second moments -- a family that includes many non-Gaussian laws such as the Laplace, logistic, or hyperbolic distributions. Focusing on the 2-Wasserstein distance, we show that all our structural results hold and our scalable Frank-Wolfe algorithm is applicable.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Literature Review", "weight": 1.0} -->

Our work is related to the literature on distributionally robust control, which seeks control policies that minimize expected costs under the worst-case system evolution. Kim and Yang prove the optimality of linear state-feedback control policies for a related minimax LQR model with a Wasserstein distance but with perfect state observations. With perfect observations and zero-mean noise, the optimal policies in the classical LQR formulation are independent of the noise distribution and are thus inherently robust, so considering imperfect observations and non-zero mean noise is what makes the problem more challenging in our case. Closest to our work, Taşkesen et al. study the finite-horizon version of our model with a 2-Wasserstein distance and all noise distributions *required* to be zero-mean and Lanzetti et al. consider an infinite-horizon formulation with 2-Wasserstein distance and all noise distributions required to be *stationary and zero-mean*, and both papers prove that *affine* output-feedback policies are optimal. Our work unifies and extends these previous results.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Literature Review", "weight": 1.0} -->

We provide a unifying description of the ambiguity set via a divergence $\mathds{D}$ that is required to satisfy a key property, which we verify for all the aforementioned examples considered in the literature and new examples that we identify. (Indeed, to the best of our knowledge, this is the first paper to consider entropy-regularized optimal transport or Fisher divergence for distributionally robust control problems.) Moreover, we do not restrict noise distributions to be zero mean in the finite-horizon case or stationary in the infinite-horizon case; instead, we allow the adversary more freedom and we prove -- under mild assumptions -- that such restrictions are without loss of optimality. Lastly, we draw a sharper distinction between affine and linear control policies and we characterize precisely when each class is optimal and how this is related to the adversary's choices.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Literature Review", "weight": 1.0} -->

We note that several papers in the literature have also considered robust formulations (with imperfect observations) for *constrained* systems, e.g., Ben-Tal et al., Van Parys et al., Kotsalis et al., Brouillon et al.; these models are more challenging and the common approach is to restrict attention to affine feedback policies for computational tractability and without proving their optimality.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Literature Review", "weight": 1.0} -->

Our work is also related to the literature on distributionally robust filtering for linear dynamical systems, which considers formulations without controls and focuses on the problem of estimating states. Zorzi studies a model based on $\tau$-divergences (a class that includes Kullback-Leibler divergence as a special instance) and Han considers a model based on 2-Wasserstein distance, for which tractable convex reformulations are derived. Within this stream, the closest works to ours are Shafieezadeh-Abadeh et al., Nguyen et al., which consider the problem of minimax mean-squared-error estimation when ambiguity is modeled with a 2-Wasserstein distance from a nominal Gaussian distribution, and Kargin et al., which relaxes the assumption that noise terms are iid and investigates both finite and infinite-horizon models, proving the optimality of linear filters when the nominal distribution is Gaussian and providing tractable convex reformulations using frequency-domain techniques.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Literature Review", "weight": 1.0} -->

For the case with Wasserstein distance, our proof relies on some ideas from these papers (such as using the Gelbrich distance to construct upper bounds), which we combine with ideas from control theory on purified output feedback to obtain the construction.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Literature Review", "weight": 1.0} -->

Our paper is also related to literature that documents the optimality of linear/affine policies in (distributionally) robust dynamic optimization models. Bertsimas et al., Iancu et al. prove optimality for one-dimensional linear systems affected by additive noise and with perfect state observations, but with general convex state and/or control costs. Hadjiyiannis et al., Van Parys et al. provide computationally tractable approaches for quantifying the suboptimality of affine control policies in finite- or infinite-horizon settings, and Bertsimas and Goyal, El Housni and Goyal, Georghiou et al. characterize the performance of affine policies in two-stage (distributionally) robust dynamic models.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Literature Review", "weight": 1.0} -->

Our proposed algorithm for solving the DRLQ problem is a variant of the classical Frank-Wolfe algorithm for solving convex optimization problems. The original paper introducing the ideas is Frank and Wolfe, and \Taşkesen et al., also rely on these ideas to construct a tractable algorithm for the finite-horizon, 2-Wasserstein DRLQ formulation. We extend that construction and generalize it to other ambiguity sets.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Ambiguity Model, Assumptions, and Examples", "weight": 1.0} -->

We consider a discrete-time, linear dynamical system like the one described in §1 and assume that the initial state $x_{0}$ and the noise terms $\{w_{t}\}_{t=0}^{T-1}$ and $\{v_{t}\}_{t=0}^{T-1}$ are exogenously determined and governed by an unknown probability distribution. Because all random vectors appearing in our model are functions of these exogenous uncertainties, we set the sample space without loss of generality as $\Omega=\mathbb{R}^{n}\times\mathbb{R}^{n\times T}\times\mathbb{R}^{p\times T}$. We use $\mathcal{F}$ to denote the Borel $\sigma$-algebra on $\Omega$ and $\mathbb{P}$ to denote the joint probability distribution of these random vectors. The joint distribution $\mathbb{P}$ is only known to belong to an ambiguity set $\mathcal{B}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Ambiguity Model, Assumptions, and Examples", "weight": 1.0} -->

we construct the ambiguity set $\mathcal{B}$ as: where, for all $z\in\mathcal{Z}$ and for finite $\rho_{z}\geq 0$, We refer to the requirement that $\mathbb{E}_{\mathbb{P}}[z^{\prime}z^{\top}]=0$ for any $z\neq z^{\prime}\in\mathcal{Z}$ as the *second moment orthogonality* (SMO) condition.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Ambiguity Model, Assumptions, and Examples", "weight": 1.0} -->

Note that if $\mathbb{E}_{\mathbb{P}}[z]=\mathbb{E}_{\mathbb{P}}[z^{\prime}]=0$, this is equivalent to requiring that $z,z^{\prime}$ are uncorelated. Subsequently, for every $z\in\mathcal{Z}$, we use $\mu_{z},M_{z}$, and $\Sigma_{z}$ to denote the mean, second moment, and covariance matrix, respectively, under a generic distribution $\mathbb{P}\in\mathcal{B}$, and use $\hat{\mu}_{z},\hat{M}_{z}$, and $\hat{\Sigma}_{z}$ to denote these quantities, respectively, under the nominal distribution $\hat{\mathbb{P}}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumptions for Tractability", "weight": 1.0} -->

To maintain tractability and rule out uninteresting cases, we impose a few assumptions on the nominal distribution $\hat{\mathbb{P}}$ and on the structure of the ambiguity set $\mathcal{B}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Requiring $\hat{\mathbb{P}}$ to be Gaussian renders our model computationally tractable for several cases of practical interest and is consistent with the assumptions in the classical LQG model. Appendix §H shows that when the divergence $\mathds{D}$ corresponds to a 2-Wasserstein distance, our results also hold for any *elliptical* nominal distribution $\hat{\mathbb{P}}$ with finite second moments -- a class that includes many *non*-Gaussian distributions such as the Laplace, logistic, or hyperbolic distributions. In general, computing the optimal control policy for an *arbitrary* distribution $\mathbb{P}$ would be very difficult because even computing the state estimator $\hat{x}_{t}$ is hard in that case, as formalized in the following result.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Assumption 2 holds in several important cases (see §2.2) and admits an intuitive interpretation. Requirement (i) readily holds if the divergence $\mathds{D}(\mathbb{P}_{z},\hat{\mathbb{P}}_{z})$ depends only on the first two moments of the distributions $\mathbb{P}_{z},\hat{\mathbb{P}}_{z}$. If the divergence is based on an information-theoretic principle related to uncertainty, the Gaussian distribution may satisfy requirement (i) because it is the "most uncertain" (maximum-entropy) distribution for a given set of first and second moments; this happens in two of our examples, corresponding to the Kullback-Leibler and Fisher divergences.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

More broadly, (i) can be thought of as restricting attention to ambiguity sets $\mathcal{B}_{z}$ that are "dense in Gaussians": the requirement is satisfied if for any $0\leq\rho\leq\rho_{z}$, the set of distributions in $\mathcal{B}_{z}$ with "distance" of at most $\rho$ from the nominal distribution -- if nonempty -- contains at least one Gaussian distribution. Part (ii) requires that the set of first and second moments characterizing all Gaussian distributions in the ambiguity set $\mathcal{B}_{z}$ is "well behaved," i.e., it is convex and compact. This enables us to evaluate worst-case expectations of *quadratic* functions of $z$ (prominent in the LQG model) over the ambiguity set $\mathcal{B}_{z}$ by solving finite-dimensional, convex optimization problems.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Examples", "weight": 1.0} -->

Assumption 2 holds in several important instances, which we describe below. The formal results and proofs that help verify these properties are all included in Appendix §B.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Wasserstein Ambiguity Sets", "weight": 1.0} -->

Consider an ambiguity set where $\mathds{D}$ corresponds to the 2-Wasserstein distance $\mathds{W}$, defined as follows.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Kullback-Leibler Ambiguity Sets", "weight": 1.0} -->

Next, consider an ambiguity set where the divergence $\mathds{D}$ corresponds to the Kullback-Leibler (KL) divergence $\mathds{K}$, defined as follows.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Moment Ambiguity Sets", "weight": 1.0} -->

Lastly, we consider moment ambiguity sets where the divergence $\mathds{D}$ between two probability distributions relies only on the first two moments of the distributions.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Moment Ambiguity Sets", "weight": 1.0} -->

The ambiguity set $\mathcal{B}_{z}$ for the random variable $z$ with nominal distribution $\hat{\mathbb{P}}_{z}$ (with mean $\hat{\mu}_{z}$ and second moment matrix $\hat{M}_{z}$) can therefore be expressed as: Assumption 2-(i) holds because every distribution (including a Gaussian distribution) with the same mean and second moment would yield the same divergence from the nominal distribution $\hat{\mathbb{P}}_{z}$ and would therefore minimize the divergence from $\hat{\mathbb{P}}_{z}$. Assumption 2-(ii) holds if the sublevel sets of the function $\mathds{M}\bigl(\cdot,\hat{m}_{z}\bigr)$ restricted to its first variable are convex and compact (for the given $\hat{m}_{z}=(\hat{\mu}_{z},\hat{M}_{z})$).

<!-- chunk {"id": "body-0045", "role": "body", "section": "Moment Ambiguity Sets", "weight": 1.0} -->

Any restriction of $\mathds{M}$ that is quasiconvex and coercive would satisfy the requirement.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Nash Equilibrium and Optimality of Linear Policies and Gaussians", "weight": 1.0} -->

This section proves our main structural results concerning the DRLQ problem. We view this problem as a game between the decision maker, who chooses causal control inputs, and nature, which chooses a distribution $\mathbb{P}\in\mathcal{B}$. We show that this game admits a Nash equilibrium under our standing assumptions, wherein nature's strategy is a Gaussian distribution, $\mathbb{P}_{z}^{\star}=\mathcal{N}(\mu_{z}^{\star},M_{z}^{\star})$ for any $z\in\mathcal{Z}$, and the decision maker's strategy is an affine output feedback policy.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Nash Equilibrium and Optimality of Linear Policies and Gaussians", "weight": 1.0} -->

Under mild additional assumptions, we also prove that nature's optimal distribution has a mean of zero, in which case the decision maker's optimal strategy becomes *linear* and nature's optimal strategy entails choosing a covariance matrix for the noise terms $\Sigma_{z}^{\star}$ that dominates the nominal covariance matrix $\hat{\Sigma}_{z}$ in Loewner order, $\Sigma_{z}^{\star}\succeq\hat{\Sigma}_{z}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Reformulation with Purified Observations", "weight": 1.0} -->

We first simplify the problem formulation by re-parametrizing the control inputs in a more convenient form. Note that the control inputs in the formulation are subject to cyclic dependencies, as $u$ depends on $y$, while $y$ depends on $x$ through, and $x$ depends again on $u$ through, etc. Because these dependencies make the problem hard to analyze, it is preferable to instead consider the controls as functions of a new set of so-called purified observations instead of the actual observations $y_{t}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Reformulation with Purified Observations", "weight": 1.0} -->

Specifically, we first introduce a fictitious noise-free system with states $x^{\prime}_{t}\in\mathbb{R}^{n}$ and outputs $y^{\prime}_{t}\in\mathbb{R}^{p}$, which is initialized with $x^{\prime}_{0}=0$ and controlled by the same inputs $u_{t}$ as the original system. We then define the purified observation at time $t$ as $\eta_{t}=y_{t}-{y}^{\prime}_{t}$ and we use $\eta=(\eta_{0},\dots,\eta_{T-1})$ to denote the trajectory of all purified observations.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Reformulation with Purified Observations", "weight": 1.0} -->

Because the inputs $u_{t}$ are causal, the decision maker can compute the fictitious state $x^{\prime}_{t}$ and output $y^{\prime}_{t}$ from the observations $y_{0},\ldots,y_{t}$. Thus, $\eta_{t}$ is representable as a function of $y_{0},\ldots,y_{t}$. Conversely, one can show by induction that $y_{t}$ can also be represented as a function of $\eta_{0},\ldots,\eta_{t}$. Moreover, any measurable function of $y_{0},\ldots,y_{t}$ can be expressed as a measurable function of $\eta_{0},\ldots,\eta_{t}$ and vice-versa \Hadjiyiannis et al., [2011, Proposition II.1\].

<!-- chunk {"id": "body-0051", "role": "body", "section": "Reformulation with Purified Observations", "weight": 1.0} -->

So if we define $\mathcal{U}_{\eta}$ as the set of all control inputs $(u_{0},u_{1},\dots,u_{T-1})$ so that $u_{t}=\phi_{t}(\eta_{0},\dots,\eta_{t})$ for some measurable function $\phi_{t}:\mathbb{R}^{p(t+1)}\rightarrow\mathbb{R}^{m}$ for every $t\in[T-1]$, the above reasoning implies that $\mathcal{U}_{\eta}=\mathcal{U}_{y}$. Moreover, the class of causal control policies that are affine (respectively, linear) in $\eta$ is equivalent to the class of causal control policies that are affine (respectively, linear) in $y$ (see Ben-Tal et al., Skaf and Boyd and Lemma E in §A.3 for a concise proof).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Reformulation with Purified Observations", "weight": 1.0} -->

Therefore, in interpreting all our results, the existence of optimal affine (linear) policies $u^{\star}\in\mathcal{U}_{\eta}$ is equivalent to the existence of optimal affine (respectively, linear) policies $u^{\star}\in\mathcal{U}_{y}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Reformulation with Purified Observations", "weight": 1.0} -->

The latter reformulation involving the purified observations $\eta$ is useful for two reasons. First, the purified outputs are independent of the inputs $u$. Indeed, by recursively combining the equations of the original and the noise-free systems, one can show that $\eta=Dw+v$ for some block triangular matrix $D$ (see Appendix §A.2 for the construction). So the purified observations depend (affinely) on the exogenous uncertainties but do not depend on the control inputs $u$, and hence, the cyclic dependencies complicating the original system are eliminated. Second and more importantly, the purified observations will allow us to reformulate the non-convex DRLQ problem as a *convex* optimization problem, as will become obvious subsequently.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Reformulation with Purified Observations", "weight": 1.0} -->

Our results also rely on the dual of, defined as We prove that $p^{\star}=d^{\star}$ and that a Nash equilibrium for our game exists wherein $\mathbb{P}^{\star}$ is Gaussian and $u^{\star}$ is affine. The classical minimax inequality implies that $p^{\star}\geq d^{\star}$. To prove that $p^{\star}=d^{\star}$, we construct an upper bound for $p^{\star}$ and a lower bound for $d^{\star}$, and then argue that these bounds match.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Upper Bound for Primal", "weight": 1.0} -->

To finalize our construction of the upper bound on $p^{\star}$, we focus on affine policies of the form $u=q+U\eta=q+U(Dw+v)$, where $q=(q_{0},\dots,q_{T-1})$, and $U$ is a block lower triangular matrix The block lower triangularity of $U$ ensures that the corresponding control policy is causal, which in turn ensures that $u\in\mathcal{U}_{\eta}$. In the following, we denote by $\mathcal{U}$ the set of all block lower triangular matrices of the form.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Upper Bound for Primal", "weight": 1.0} -->

An upper bound on problem can now be obtained by *restricting* the decision maker's feasible set to causal control policies that are *affine* in the purified observations $\eta$ and by *relaxing* nature's feasible set to the outer approximation $\overline{\mathcal{B}}$ of $\mathcal{B}$. The resulting upper bound is given: Because we obtained by restricting the feasible set of the outer minimization problem and relaxing the feasible set of the inner maximization problem, it is clear that $\overline{p}^{\star}\geq p^{\star}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Upper Bound for Primal", "weight": 1.0} -->

Although problem is still an infinite-dimensional, zero-sum game because nature's choices are over distributions $\mathbb{P}$, important simplifications are possible. Specifically, note that for any fixed $U,q$, the control policies $u$ and induced states $x=Hu+Gw$ are affine functions on the noise terms $w,v$, and therefore the expected value of the objective, $\mathbb{E}_{\mathbb{P}}\bigl[u^{\top}Ru+x^{\top}Qx\big]$, only depends on the first two moments of the random vector $(w,v)$ under distribution $\mathbb{P}$. This implies that problem can be rewritten as a finite-dimensional zero-sum game, as formalized in the following result.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Lower Bound for Dual", "weight": 1.0} -->

To derive a tractable lower bound on $d^{\star}$, we restrict nature's feasible set to the family $\mathcal{B}_{\mathcal{N}}$ of all Gaussian distributions in the ambiguity set $\mathcal{B}$. The resulting bounding problem is thus given by As we obtained by restricting the feasible set of the outer maximization problem, it is clear that $\underline{d}^{\star}\leq d^{\star}$. Next, by leveraging the fact that the inner minimization problem in is solved by an affine control policy for any fixed Gaussian distribution in $\mathcal{B}_{\mathcal{N}}$, we show that can be recast as a finite-dimensional zero-sum game.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Optimality of Affine Policies and Gaussian Distributions", "weight": 1.0} -->

The next result leverages the primal and dual relaxations to prove our main result that the primal DRLQ problem in and its dual in actually have the same optimal value.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Optimality of Linear Policies and Zero-Mean Distributions", "weight": 1.0} -->

Under some additional mild assumptions on the ambiguity sets, we can further refine the structural results concerning the decision maker's and nature's Nash strategies. We first state an additional assumption on the set of first two moments $\mathcal{M}_{(\mu_{z},M_{z})}$ defined in Assumption 2.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

The assumption bears an intuitive interpretation. Formulated as a feasibility condition on the ambiguity set $\mathcal{B}_{z}$, it states that if a Gaussian distribution $\mathbb{P}_{z}=\mathcal{N}(\mu_{z},M_{z})$ belongs to $\mathcal{B}_{z}$, then the "centered" Gaussian $\mathbb{P}^{\prime}_{z}=\mathcal{N}(0,M_{z})$ -- obtained by setting the mean to zero while keeping the second moment unchanged -- should also be feasible, $\mathbb{P}^{\prime}_{z}\in\mathcal{B}_{z}$. In other words, the adversary may always transfer deterministic bias into additional variance without leaving $\mathcal{B}_{z}$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

Because this transformation raises the covariance from $M_{z}-\mu_{z}\mu_{z}^{\top}$ to $M_{z}$ and the latter dominates the former in the Loewner (positive semidefinite) order, the key intuition behind the assumption is to allow the adversary to "inflate" uncertainty (while holding the second moment fixed).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

The validity of Assumption 3 depends on three key inputs: the divergence $\mathds{D}$, the nominal distribution $\hat{\mathbb{P}}_{z}=\mathcal{N}(\hat{\mu}_{z},\hat{M}_{z})$, and the radius $\rho_{z}$ of the ambiguity set. The following result shows that all our examples from §2.2 satisfy Assumption 3 under very mild conditions if the nominal distribution has zero mean.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Worst-Case Covariance Matrix", "weight": 1.0} -->

Our final structural result further develops the intuition above and shows that nature's optimal distribution $\mathbb{P}^{\star}$ entails suitably "inflating" the covariance matrix of the nominal distribution $\hat{\mathbb{P}}$. Because any zero-mean Gaussian distribution $\mathbb{P}_{z}$ is fully specified through the second moment/covariance matrix $M_{z}^{\star}=\Sigma_{z}^{\star}$, we can shorten notation by using $\mathcal{M}_{\Sigma_{z}}$ to denote the sets $\mathcal{M}_{(\mu_{z}=0,M_{z})}$ defined in Assumption 2.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Worst-Case Covariance Matrix", "weight": 1.0} -->

Our final result requires a mild condition on the sets $\mathcal{M}_{\Sigma_{z}}$ that further refines Assumption 3.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

Proposition 10 ‣ C Proofs for Section 3 ‣ Optimality of Linear Policies in Distributionally Robust Linear Quadratic Control") in Appendix §C.4.1 ‣ C Proofs for Section 3 ‣ Optimality of Linear Policies in Distributionally Robust Linear Quadratic Control") shows that Assumption 4 is satisfied by all examples in §2.2 if $\rho_{z}>0$ (and, for the case of the moment-based ambiguity, if the divergence $\mathds{M}$ satisfies a mild condition). The key requirements are intuitive if one takes $g(\Sigma_{z})$ as a (convex, increasing) transformation of the distance $\mathds{D}(\mathbb{P}_{z},\hat{\mathbb{P}}_{z})$ between a distribution $\mathbb{P}_{z}=\mathcal{N}(0,\Sigma_{z})$ and the nominal $\hat{\mathbb{P}}_{z}=\mathcal{N}(0,\hat{\Sigma}_{z})$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

Requirement (i) simply asks that $\hat{\Sigma}_{z}$ is an interior point of the set of valid covariances $\mathcal{M}_{z}$, which holds in all our examples provided there is ambiguity, $\rho_{z}>0$. Requirement (ii) is readily satisfied because $\mathds{D}(\mathbb{P}_{z},\hat{\mathbb{P}}_{z})\geq\mathds{D}(\hat{\mathbb{P}}_{z},\hat{\mathbb{P}}_{z})$ for any divergence $\mathds{D}$. Lastly, (iii) asks that the gradient map $\nabla g$ be order-reflecting, i.e., that gradients that dominate in the Loewner (positive semidefinite) order should correspond to (distributions whose) covariances also dominate in the Loewner order. Put more intuitively, this means that "noisier" gradient maps should come from "noisier" distributions.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Efficient Numerical Solution of DRLQ Problems", "weight": 1.0} -->

Our duality results in Theorem 3.1. ‣ 3.4 Optimality of Affine Policies and Gaussian Distributions ‣ 3 Nash Equilibrium and Optimality of Linear Policies and Gaussians ‣ Optimality of Linear Policies in Distributionally Robust Linear Quadratic Control") lead to immediate algorithms for computing optimal strategies: the optimal value in the DRLQ problem is the same as the optimal value in problems and, and the latter problems are finite-dimensional, convex-concave problems with smooth objectives, which are amenable to saddle-point methods \Juditsky and Nemirovski, [2022, Schiele et al., 2024\]. However, such approaches would fail to exploit the temporal structure of the original control problem and would generally result in large-dimensional optimization problems.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Efficient Numerical Solution of DRLQ Problems", "weight": 1.0} -->

We next leverage our results from §3 to develop a set of more efficient algorithms to solve the DRLQ problem via Kalman filtering and DP techniques. Our algorithms will rely on all structural results from §3, as formalized in the next result.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Although the subproblems above can be reformulated as tractable SDPs that are amenable to off-the-shelf solvers, for specific divergences $\mathds{D}$ one may be able to further simplify this computation. For instance, for the Wasserstein and KL ambiguity sets from §2.2 (corresponding to divergences $\mathds{W}$ and $\mathds{K}$, respectively), the optimization problem in for a given $z\in\mathcal{Z}$ can be reduced to solving a univariate algebraic equation, which can be done to any desired accuracy $\delta>0$ by an efficient bisection algorithm. Appendix §D.2 provides details for this construction and a proof of all relevant results, that leverage existing results in the literature.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Remark 2 (Automatic differentiation)", "weight": 1.0} -->

Recall that $f(\Sigma_{w},\Sigma_{v})$ is the optimal value of the LQG problem corresponding to the Gaussian distribution $\mathbb{P}$ with the covariance matrices $\Sigma_{w}$ and $\Sigma_{v}$. By using the underlying dynamic programming equations, $f(\Sigma_{w},\Sigma_{v})$ can thus be expressed in closed form as a serial composition of $\mathcal{O}(T)$ rational functions (see Appendix §A for details). Hence, $\nabla_{\Sigma_{z}}f(\Sigma_{w},\Sigma_{v})$ can be calculated symbolically for any $z\in\mathcal{Z}$ by repeatedly applying the chain and product rules. However, the resulting formulas are lengthy and cumbersome. We thus compute the gradients numerically using backpropagation.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Remark 2 (Automatic differentiation)", "weight": 1.0} -->

The cost of evaluating $\nabla_{\Sigma_{z}}f(\Sigma_{w},\Sigma_{v})$ is then of the same order of magnitude as the cost of evaluating $f(\Sigma_{w},\Sigma_{v})$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Remark 2 (Automatic differentiation)", "weight": 1.0} -->

A detailed description of the proposed Frank-Wolfe method is given in Algorithm 1 below.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Remark 2 (Automatic differentiation)", "weight": 1.0} -->

1:Input: initial iterates Σw, Σv, nominal covariance matrices Σ̂w, Σ̂v, oracle precision δ ∈ 2:set initial iteration counter k = 0 3:while stopping criterion is not met do 6: compute Σz⋆ that solves to precision δ Algorithm 1 Frank-Wolfe algorithm for solving By Theorem 1 and Lemma 7 in Jaggi, which apply in view of Proposition 4, Algorithm 1 attains a suboptimality gap of $\epsilon$ within $\mathcal{O}(1/\epsilon)$ iterations. Its precise computational complexity is critically dependent on the tractability of 6 (this is very efficient for Wasserstein and KL ambiguity, by Remark 1).

<!-- chunk {"id": "body-0075", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We conduct numerical experiments to assess the merits of the DRLQ model and the effectiveness of the algorithms introduced in §4. We consider a class of dynamical systems with $n=m=p=d$ with $d\in\mathbb{N}_{+}$. We set $A_{t}=A$ where $A$ has $0.1$ on the main diagonal and the super-diagonal and zeroes elsewhere ($A_{i,j}=0.1$ if $i=j$ or $i=j-1$ and $A_{i,j}=0$ otherwise), and the other matrices to $B_{t}=C_{t}=Q_{t}=R_{t}=I_{d}$. The nominal covariance matrices $\hat{\Sigma}_{z}$ are constructed randomly and with eigenvalues in the interval $$ (to ensure they are positive definite). We construct ambiguity sets based on either Wasserstein or KL divergence.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

All experiments were conducted on an Apple M3 Max machine equipped with 64 GB of RAM. All linear SDP problems were formulated in Python (v3.8.6) using CVXPY (v1.6.1) \Agrawal et al., [2018, Diamond and Boyd, 2016\] and solved with MOSEK \MOSEK ApS, (v11.0.8). Additionally, the gradients of $f(\Sigma_{w},\Sigma_{v})$ were computed using Pymanopt (v2.2.1) \Townsend et al., in combination with PyTorch's automatic differentiation module (v2.6.0) \Paszke et al.,. The code is publicly available in the Github repository

<!-- chunk {"id": "body-0077", "role": "body", "section": "Computational Efficiency of Algorithm 1", "weight": 1.0} -->

We compare two approaches for finding the optimal value of the DRLQ problem: directly solving the SDP reformulation of with MOSEK and using our custom Frank-Wolfe method discussed in Algorithm 1. For these experiments, we set $d=10$ and the corresponding radii of the ambiguity sets as $\rho_{x_{0}}=\rho_{w_{t}}=\rho_{v_{t}}=10^{-1}$. We compare the two approaches in 10 problem instances (generated randomly and independently) and we compare performance as a function of the problem horizon $T$, which we vary. We set a stopping criterion corresponding to an optimality gap below $10^{-3}$ and we run the Frank-Wolfe method with $\delta=0.95$.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Worst-case Performance", "weight": 1.0} -->

We next evaluate the benefits of the robust approach. Let $u^{\star}$ denote the *robustly optimal* policy, i.e., the optimal policy in the DRLQ model, obtained by solving problem, and let $\hat{u}$ denote the *nominally optimal* policy, i.e., the policy that minimizes the expected cost under the nominal distribution, $\mathbb{E}_{\hat{\mathbb{P}}}[J(u)]$. To gauge the robustness and conservativeness of the policies $u^{\star}$ and $\hat{u}$, we compare them under the nominal distribution and under their respective worst-case distributions.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Worst-case Performance", "weight": 1.0} -->

Specifically, letting $\mathbb{P}^{\star}(u)$ denote the adversary's optimal choice of distribution $\mathbb{P}$ corresponding to a control policy $u$ and letting $J(u)$ denote the dependency of the cost on the control policy $u$, we calculate the following two performance gaps: In our experiments, we set $d=2$, $T=2$, $\rho_{x_{0}}=\rho_{w_{t}}=\rho_{v_{t}}=\rho$, and we vary the common radius $\rho$ from 0 to 10, calculating the "Worst-case-gap" and "Nominal-gap" for each value of $\rho$ in 10 independently generated random problem instances. The results are depicted in Figure 3, with the left panel corresponding to the Wasserstein ambiguity set and the right panel corresponding to the KL ambiguity set.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Worst-case Performance", "weight": 1.0} -->

The results indicate that using the optimal policy from the DRLQ model, $u^{\star}$, leads to dramatically lower worst-case costs, particularly as the ambiguity radius $\rho$ increases. Surprisingly, this improvement does not impact performance in the nominal scenario, where using $u^{\star}$ does not substantially increase costs relative to using the nominally optimal policy $\hat{u}$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Infinite-Horizon DRLQ Problems", "weight": 1.0} -->

We now extend the results of §3 to infinite-horizon control problems with an average cost criterion. Throughout this section, we restrict attention to linear *time-invariant* systems of the form and where $T=\infty$ and $A_{t}=A_{0}$, $B_{t}=B_{0}$ and $C_{t}=C_{0}$ for all $t\in\mathbb{N}$. All random variables emerging in our model are functions of the initial state $x_{0}$ and the noise terms $\{w_{t}\}_{t=0}^{\infty}$ and $\{v_{t}\}_{t=0}^{\infty}$.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Infinite-Horizon DRLQ Problems", "weight": 1.0} -->

In analogy to the finite-horizon theory, we define $x=(x_{t})_{t=0}^{\infty}$, $u=(u_{t})_{t=0}^{\infty}$, $y=(y_{t})_{t=0}^{\infty}$, $w=(x_{0},(w_{t})_{t=0}^{\infty})$ and $v=(v_{t})_{t=0}^{\infty}$ as well as infinite-dimensional block matrices $H$, $G$ and $C$ (whose definitions mirror those for the finite horizon and are omitted for brevity). With these conventions, the input, state and output processes are subject to the usual system equations $x=Hu+Gw$ and $y=Cx+v$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Infinite-Horizon DRLQ Problems", "weight": 1.0} -->

As before, we denote by $\mathcal{U}_{y}$ the set of control inputs $u$ such that $u_{t}=\varphi_{t}(y_{0},\ldots,y_{t})$ for every $t\in\mathbb{N}$, where $\varphi_{t}:\mathbb{R}^{p(t+1)}\rightarrow\mathbb{R}^{m}$ is a measurable control policy. To describe the distribution of the exogenous uncertainties, it is again convenient to set $\mathcal{Z}=\{x_{0},w_{0},v_{0},w_{1},v_{1},\ldots\}$. We then define $\mathcal{B}^{\infty}$ exactly as the ambiguity set $\mathcal{B}$ from §2.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Assumptions", "weight": 1.0} -->

To ensure that the problem is well posed under an infinite-horizon setting and average-cost criterion, we must slightly strengthen the assumptions in §2.1 and make a few additional mild assumptions.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Assumptions", "weight": 1.0} -->

First, we mirror the classical infinite-horizon LQG setting by stating an assumption on system and cost matrices. Recall that we already focus on time-invariant systems and costs. To state our additional requirement, we recall the following definition of a Schur-stable matrix.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Assumption 5", "weight": 1.0} -->

These assumptions are standard in the context of infinite-horizon control of linear dynamical systems. *Stabilizability* guarantees the existence of a stationary state-feedback control policy that makes the states of a noise-free system converge and allows deriving an optimal state-feedback control policy of the form $u_{t}^{\star}=K\hat{x}_{t}$, where $\hat{x}_{t}$ denotes the MMSE state estimator (see §A.4). However, even if $u_{t}$ stabilizes the noise-free system, the states under linear (purified) output feedback could diverge for large $t$ without the *detectability* assumption and without a strictly positive definite cost matrix $Q_{0}$.^33^3This suggests that the stability properties of a system are more difficult to analyze when the control policy is parametrized in terms of the purified outputs. In contrast, the convexity properties of the system are more difficult to analyze when policies are parametrized in terms of the original outputs.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Assumption 5", "weight": 1.0} -->

We also strengthen slightly our assumptions concerning the nominal distribution $\hat{\mathbb{P}}$ by requiring this to be zero-mean Gaussian and also time-invariant.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Assumption 6", "weight": 1.0} -->

The requirements in (i) concerning the nominal distribution are standard in infinite-horizon LQG control problems \Lancaster and Rodman, [1995, Bertsekas, 2017\]. Under a time-invariant, Gaussian noise distribution $\hat{\mathbb{P}}$, these requirements are only slightly stronger than those in Assumption 1, by asking that the covariance matrices for the state noise be positive definite, $\hat{\Sigma}_{x_{0}}\succ 0$ and $\hat{\Sigma}_{w_{t}}\succ 0$ for all $t\in\mathbb{N}$. Requirement (ii) is also aligned with time-invariance by asking that the corresponding ambiguity sets have the same radius. Lastly, the restriction to zero-mean distributions in (iii) simplifies exposition and is driven by our results in §3.5; this requirement can be relaxed and arguments mirroring those in §3.5 can be used to prove that nature will optimally choose zero-mean distributions, but we omit details for brevity and instead simply state this as a requirement.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Assumption 6", "weight": 1.0} -->

Throughout this section, Assumption 2 remains unchanged. Note that in view of Assumption 6, the sets of moments defined in Assumption 2 only involve the covariance matrices $\Sigma_{z}$ (as in §3.6 and §4) and are also time-invariant, so we define the following simpler notation: By Assumption 2, the sets $\mathcal{M}_{\Sigma_{w}}$ and $\mathcal{M}_{\Sigma_{v}}$ are convex and compact.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Assumption 6", "weight": 1.0} -->

Lastly, we preserve Assumption 4 suitably generalized to our infinite-horizon setting, so that where $g$ is a convex, differentiable function.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Construction of Primal and Dual and Their Bounds", "weight": 1.0} -->

With these preliminaries, the DRLQ problem can be formulated as: In analogy to §3, we define $\eta=(\eta_{t})_{t=0}^{\infty}$ as the trajectory of all purified observations that satisfies $\eta=Dw+v$, where $D=CG$, and $\mathcal{U}_{\eta}$ as the set of all control inputs $u$ so that $u_{t}=\phi_{t}(\eta_{0},\dots,\eta_{t})$ for some measurable function $\phi_{t}:\mathbb{R}^{p(t+1)}\rightarrow\mathbb{R}^{m}$ for every $t\in\mathbb{N}_{+}$.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Construction of Primal and Dual and Their Bounds", "weight": 1.0} -->

By \Hadjiyiannis et al., [2011, Proposition II.1\], we can rewrite the infinite-horizon DRLQ problem equivalently as Our results also rely on the dual of defined as In the remainder of this section, we demonstrate that, under mild assumptions, the primal DRLQ problem is solved by a *stationary, linear* control policy, the dual problem is solved by a *time-invariant, Gaussian* distribution, and strong duality holds. To establish these results, we proceed as in §3: we first construct an upper bound for the primal problem followed by a lower bound for the dual problem, and then show that the bounds coincide, which proves all three claims.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Upper Bound for Primal", "weight": 1.0} -->

Mirroring §3, we obtain an upper bound on $p^{\star}$ by inflating the ambiguity set $\mathcal{B}^{\infty}$ and restricting the control policies. We define the inflated ambiguity set $\overline{\mathcal{B}}{}^{\infty}$ exactly as the ambiguity set $\overline{\mathcal{B}}$ from Section 3, but we also add the additional condition that $\mathbb{E}_{\mathbb{P}_{z}}[z]=0$ for every $z\in\mathcal{Z}$ to mirror the new Assumption 6-(ii) on $\mathcal{B}^{\infty}$. For any divergence $\mathds{D}$ satisfying Assumption 2-(i), we can readily verify that $\mathcal{B}^{\infty}$ is a subset of $\overline{\mathcal{B}}{}^{\infty}$.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Upper Bound for Primal", "weight": 1.0} -->

Restricting the control policies $u$ requires more care in the infinite-horizon case, to ensure that long-run-average costs are finite and to enable our subsequent duality proof. To that end, we restrict attention (without loss of optimality) to a *subset* of the set of all *stationary* purified output control policies $u\in\mathcal{U}_{\eta}$ under which the covariance matrices of controls $u_{t}$ and states $x_{t}$ converge, which also guarantees that the long-run average costs converge to a finite value. To formalize these, we first define the set of block lower triangular Toeplitz matrices.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Lower Bound for Dual", "weight": 1.0} -->

The following proposition, which leverages the stabilizability and detectability Assumption 5 and classical results in infinite-horizon LQG control, will allow simplifying the formulation in by only considering stationary, linear policies.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Conclusions, Limitations, and Future Directions", "weight": 1.0} -->

This work formulated a distributionally robust version of the classical LQG problem by replacing the fixed disturbance model with a divergence ball around a nominal distribution. Under zero-mean Gaussian nominal noise, an orthogonality requirement on the second moments of the distributions (equivalent to uncorelatedness under zero means), and suitable structural requirements on the divergence, we proved that affine output-feedback policies and a Gaussian distribution form a Nash equilibrium in our mini-max game. We also showed that it is optimal for the adversary to set the mean of the distribution to zero, in which case the decision maker's policies become linear and the adversary optimally "inflates" the nominal covariance matrix. The results generalize and rationalize many results from the (robust) LQG literature, provide an intuitive rule of thumb to address distributional misspecification in practice, and enable a very efficient Frank-Wolfe algorithm whose iterations are standard LQG subproblems.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Conclusions, Limitations, and Future Directions", "weight": 1.0} -->

All results extend to an infinite-horizon, average-cost setting -- yielding stationary linear policies and a time-invariant Gaussian worst-case model -- and to entropy-regularized optimal transport, Fisher divergence, or an elliptical nominal distribution with 2-Wasserstein distance.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Conclusions, Limitations, and Future Directions", "weight": 1.0} -->

Future work could be aimed at extending this framework or addressing some of its limitations. For instance, one could leverage our results to compute control policies with performance guarantees when the disturbance noise distribution is known but otherwise *general*. More specifically, consider a distribution $\mathbb{Q}$ such that $\mathbb{Q}\in\mathcal{B}$ for some ambiguity set $\mathcal{B}$ that is compatible with our assumptions.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Conclusions, Limitations, and Future Directions", "weight": 1.0} -->

Then, the optimal solution in the DRLQ problem $\inf_{u\in\mathcal{U}_{y}}\sup_{\mathbb{P}\in\mathcal{B}}\mathbb{E}_{\mathbb{P}}[J(u)]$ will be feasible in the (intractable) linear quadratic control problem $\inf_{u\in\mathcal{U}_{y}}\mathbb{E}_{\mathbb{Q}}[J(u)]$, and its optimality gap will be upper bounded by the difference between the optimal value of the DRLQ model and the optimal value in the distributionally robust "optimistic" problem $\inf_{\mathbb{P}\in\mathcal{B}}\inf_{u\in\mathcal{U}_{y}}\mathbb{E}_{\mathbb{P}}[J(u)]$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Conclusions, Limitations, and Future Directions", "weight": 1.0} -->

For this procedure to be effective, one must be able to solve the latter problem (which may be non-convex) and also test whether a given distribution $\mathbb{Q}$ belongs to $\mathcal{B}$, and possibly adjust $\mathcal{B}$ to guarantee this, without significantly expanding the ambiguity set too much. These tasks are likely challenging for general distributions $\mathbb{Q}$, so future work could be devoted to identifying tractable cases and designing algorithms for membership testing, ambiguity set calibration, and solving the optimistic problem.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Conclusions, Limitations, and Future Directions", "weight": 1.0} -->

One could also consider distributionally robust formulations for other stochastic control problems that extend the LQR or LQG frameworks, such as the linear-exponential-quadratic Gaussian model due to Whittle or the one recently considered in de Zegher et al., or the model with affine dynamics and extended quadratic costs from Barratt and Boyd. Alternatively, one could consider formulations that involve state or control constraints and derive policies with provable performance guarantees, or consider control problems while learning the ambiguity set, as in Iancu et al. and related literature.
