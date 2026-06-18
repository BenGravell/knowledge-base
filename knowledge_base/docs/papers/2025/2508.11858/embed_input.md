<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimality of Linear Policies in Distributionally Robust Linear Quadratic Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We study a generalization of the classical discrete-time, Linear-Quadratic-Gaussian (LQG) control problem where the noise distributions affecting the states and observations are unknown and chosen adversarially from divergence-based ambiguity sets centered around a known nominal distribution. For a finite horizon model with Gaussian nominal noise and a structural assumption on the divergence that is satisfied by many examples - including 2-Wasserstein distance, Kullback-Leibler divergence, moment-based divergences, entropy-regularized optimal transport, or Fisher (score-matching) divergence - we prove that a control policy that is affine in the observations is optimal and the adversary's corresponding worst-case optimal distribution is Gaussian. When the nominal means are zero (as in the classical LQG model), we show that the adversary should optimally set the distribution's mean to zero and the optimal control policy becomes linear. Moreover, the adversary should optimally ``inflate" the noise by choosing covariance matrices that dominate the nominal covariance in Loewner order.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Exploiting these structural properties, we develop a Frank-Wolfe algorithm whose inner step solves standard LQG subproblems via Kalman filtering and dynamic programming and show that the implementation consistently outperforms semidefinite-programming reformulations of the problem. All structural and algorithmic results extend to an infinite-horizon, average-cost formulation, yielding stationary linear policies and a time-invariant Gaussian distribution for the adversary. Lastly, we show that when the divergence is 2-Wasserstein, the entire framework remains valid when the nominal distributions are elliptical rather than Gaussian.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The Linear Quadratic Gaussian (LQG) control problem has served as a fundamental building block for a wide range of applications in management \[Bensoussan et al. Holt et al., \], economics \[Hansen and Sargent, \], finance \[Abeille et al., \], engineering \[Auger et al. Chen, \], or medicine \[Patek et al. Chakravarty et al. Kazemian et al. Todorov and Jordan, \].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The discrete-time, finite-horizon formulation considers the problem of minimizing the expected costs incurred when controlling a linear dynamical system over a finite number of periods $t \in \left\{ 0,1,\ldots,{T - 1} \right\}$. The system evolves according to the equations

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $x_{t} \in {\mathbb{R}}^{n}$ denotes the system states, $u_{t} \in {\mathbb{R}}^{m}$ denotes the control inputs, $w_{t} \in {\mathbb{R}}^{n}$ denotes an exogenous noise process, and the system matrices $A_{t} \in {\mathbb{R}}^{n \times n}$ and $B_{t} \in {\mathbb{R}}^{n \times m}$ are known. The decision maker only has access to imperfect state measurements

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

corrupted by exogenous observation noise $v_{t} \in {\mathbb{R}}^{p}$, where $C_{t} \in {\mathbb{R}}^{p \times n}$ and usually $p \leq n$ (so that observing $y_{t}$ does not allow perfectly reconstructing $x_{t}$ even without observation noise).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The control inputs $u_{t}$ are *causal*, i.e., depend on the past observations $y_{0},\ldots,y_{t}$ but not on the future observations $y_{t + 1},\ldots,y_{T - 1}$, so that the set of feasible control inputs $\mathcal{U}_{y}$ is the set of random vectors $u = \left( u_{0},u_{1},\ldots,u_{T - 1} \right)$ such that $u_{t} = {\varphi_{t}\left( y_{0},\ldots,y_{t} \right)}$ for every $t$, where $\varphi_{t}:{{\mathbb{R}}^{p{({t + 1})}}\rightarrow{\mathbb{R}}^{m}}$ is a measurable control policy.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $Q_{t} \in {\mathbb{R}}^{n \times n}$ are positive semidefinite matrices governing the state costs, and $R_{t} \in {\mathbb{R}}^{m \times m}$ are positive definite matrices governing the input costs. Under the assumption that the joint probability distribution $\mathbb{P}$ for the noise terms is known, the classical LQG problem seeks causal control inputs that minimize the expected costs under the distribution $\mathbb{P}$, i.e., $\inf_{u \in \mathcal{U}_{y}}{{\mathbb{E}}_{\mathbb{P}}\left\lbrack {J(u)} \right\rbrack}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To prove structural results and design tractable algorithms for solving this problem, several assumptions on the probability distribution $\mathbb{P}$ are typically needed. Under the premise that all noise terms have zero means and are mutually independent, it is known that the problem admits an optimal control policy of the form $u_{t}^{\star} = {K_{t}{\hat{x}}_{t}}$ for every $t \in \left\{ 0,\ldots,{T - 1} \right\}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Here, the feedback gain matrices $K_{t} \in {\mathbb{R}}^{m \times n}$ only depend on the system and cost matrices $\left\{ A_{\tau},B_{\tau},Q_{\tau},R_{\tau} \right\}_{\tau \geq t}$ and can be obtained by solving a set of recursive equations for a system without noise, and ${\hat{x}}_{t} = {{\mathbb{E}}_{\mathbb{P}}\left\lbrack x_{t} \middle| {y_{0},\ldots,y_{t}} \right\rbrack}$ is the minimum mean-squared-error (MMSE) estimator of the state $x_{t}$ given the history of observations $y_{0},\ldots,y_{t}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

This *separation principle* holds regardless of the specific probability distribution $\mathbb{P}$, but does not readily lead to tractable algorithms because calculating the MMSE estimator ${\hat{x}}_{t}$ is intractable for general probability distributions $\mathbb{P}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

As such, the LQG model also makes the additional assumption that $\mathbb{P}$ is *Gaussian*^11^1Note that if $\mathbb{P}$ is a multivariate Gaussian distribution, the requirement that noise terms are independent can be relaxed to only requiring that they are uncorrelated, i.e., ${{\mathbb{E}}_{\mathbb{P}}{\lbrack{z^{\prime}z^{\top}}\rbrack}} = 0$ for all $z \neq z^{\prime} \in {\{ x_{0},w_{0},\ldots,w_{T - 1},v_{0},\ldots,v_{T - 1}\}}$., in which case the optimal state estimator ${\hat{x}}_{t}$ depends linearly on the history of observations $y_{0},\ldots,y_{t}$ and can be obtained efficiently with Kalman filtering techniques.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by practical settings where noise distributions may not be readily available or may not be Gaussian, we consider a generalization of the discrete-time LQG model where an adversary chooses the noise distributions from an ambiguity set $\mathcal{B}$ characterized by a divergence $\mathbb{D}$ and centered around a known nominal distribution $\hat{\mathbb{P}}$, and the decision maker's goal is to minimize the costs incurred under the worst-case distribution, $\sup_{{\mathbb{P}} \in \mathcal{B}}{{\mathbb{E}}_{\mathbb{P}}\left\lbrack {J(u)} \right\rbrack}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

This optimization problem -- which we refer to as the distributionally-robust linear quadratic (DRLQ) problem -- is challenging: both the decision maker and nature are optimizing over infinite-dimensional spaces, and the ambiguity set $\mathcal{B}$ contains many non-Gaussian distributions, so it is not obvious which structural results from the LQG model would continue to hold or how one could compute an optimal control policy.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

We first consider the finite-horizon case when the nominal distribution $\hat{\mathbb{P}}$ is Gaussian with zero mean, as in the classical LQG model. We construct ambiguity sets containing all distributions whose "distance" from the nominal distribution -- measured according to a divergence $\mathbb{D}$ -- is not too large. We restrict attention to distributions under which the exogenous noise terms are allowed to have non-zero means, but are required to have finite second moments that satisfy an orthogonality condition requiring cross second moments to vanish. When noise terms are zero-mean, this second-moment orthogonality (SMO) condition is equivalent to requiring the noise terms to be uncorrelated, which is also a standard requirement in the classical LQG model. We require the divergence $\mathbb{D}$ to satisfy a key condition, which we verify for several important examples such as 2-Wasserstein distance, Kullback-Leibler divergence, moment-based divergences, entropy-regularized optimal transport, and Fisher divergence. (The first three examples are discussed in the main text and the last two in the Appendix.)

<!-- chunk {"id": "body-0017", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

Within this framework, we prove that an optimal control policy exists that is *affine* in the observations, $u_{t}^{\star} = {q_{t} + {\sum_{\tau = 0}^{t}{U_{t,\tau}y_{\tau}}}}$ for $q_{t} \in {\mathbb{R}}^{m}$ and $U_{t,\tau} \in {\mathbb{R}}^{m \times p}$, and that the associated worst-case optimal distribution ${\mathbb{P}}^{\star}$ is *Gaussian*. Our proof is novel and does not rely on traditional recursive dynamic programming arguments. Instead, we re-parameterize the control policy using purified observations and derive an upper bound for the resulting minimax formulation by relaxing the ambiguity set (to an outer approximation determined by the first two moments) while simultaneously restricting the decision maker to affine policies.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

We then use convex duality to show that the upper bound matches a lower bound obtained by restricting the ambiguity set (to Gaussian distributions) in the dual of the minimax formulation. The matching bounds then certify the optimality of affine output-feedback policies for the decision maker and of Gaussian distributions for the adversary.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

Under two mild and intuitive assumptions that hold for every divergence we consider, we derive additional structural results that yield sharp managerial insights and facilitate computation.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

The first result concerns the means of the noise terms. We prove that the adversary's worst-case distribution ${\mathbb{P}}^{\star}$ sets the noise mean to zero, and thus the worst-case exogenous noise terms are uncorrelated. Whereas the vast majority of papers formulating robust LQG models restrict attention to zero-mean (and uncorrelated) noise for simplicity or in keeping with the classical LQG assumptions, our findings provide a different justification: this assumption/choice is *conservative*, because allowing the adversary to use zero means gives the adversary more power and results in the worst-case costs for the decision maker. Moreover, we prove that when noise is zero-mean, the optimal control policy becomes purely *linear* in the outputs, $u_{t}^{\star} = {\sum_{\tau = 0}^{t}{U_{t,\tau}y_{\tau}}}$. The intuition is straightforward: any deterministic bias that nature may introduce can be anticipated and neutralized by a suitable affine shift in the control policy, so it offers the adversary no advantage.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

In equilibrium, neither player employs predictable offsets, so when the nominal means are zero, the decision maker also sets the intercepts to zero without incurring any optimality loss.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

The second result pertains to the covariance of the noise terms. Restricting attention to zero-mean distributions and linear control policies, we prove that nature's optimal choice of covariance matrix $\Sigma^{\star}$ dominates the covariance matrix of the nominal distribution $\hat{\Sigma}$ in Loewner order, $\Sigma^{\star} \succeq \hat{\Sigma}$. Nature therefore spends its ambiguity budget by suitably "inflating" the nominal covariance matrix $\hat{\Sigma}$, which increases the noise level and, consequently, the decision maker's optimal costs. This finding formalizes the familiar principle that higher variance entails greater uncertainty, extending it to the dynamic setting of distributionally robust LQG control. A practical implication follows immediately: when model misspecification is a concern, a simple yet effective safeguard (even against adversarial distributional ambiguity) is to up-scale the nominal covariance matrix and solve a nominal model under the resulting noisier Gaussian distribution.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

We leverage these structural results to design efficient algorithms for finding optimal control policies in the DRLQ problem. We propose an algorithm based on a Frank-Wolfe first-order method that solves at each iteration sub-problems corresponding to classical LQG control problems, using Kalman filtering and dynamic programming. We show that this algorithm enjoys a sublinear convergence rate and is susceptible to parallelization. Our PyTorch implementation, which relies on automatic differentiation, yields uniformly lower runtime than a direct method based on semidefinite programming, outperforming it across every problem horizon and instance we tested. Moreover, the optimal robust policy significantly reduces worst-case costs while exhibiting virtually no performance loss when the nominal distribution is in fact correct.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

We then extend our structural results to an infinite-horizon formulation of the DRLQ problem with average-cost objective, time-invariant system matrices, and time-invariant nominal distribution $\hat{\mathbb{P}}$. Importantly, we do not require the control policies or all distributions in the ambiguity set to be stationary. This setting raises additional technical hurdles that require strengthening the assumptions of the finite-horizon case. However, under assumptions that mirror the classical LQG assumptions for infinite-horizon models, we prove that a time-invariant, *stationary*, linear control policy $u^{\star}$ is optimal and that the worst-case distribution ${\mathbb{P}}^{\star}$ is a *time-invariant* Gaussian distribution. The result not only generalizes our finite-horizon findings but also aligns seamlessly with the structural insights long-observed in traditional infinite-horizon LQG settings with known distributions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Main Contributions", "weight": 1.0} -->

The Appendix elaborates on several extensions of the framework. §F and §G confirm that all our structural results hold when the divergence $\mathbb{D}$ is chosen as the entropy-regularized optimal transport divergence or as the Fisher divergence (also known as score-matching distance), respectively. §H then replaces the nominal Gaussian distribution with an *elliptical* nominal distribution $\hat{\mathbb{P}}$ with finite second moments -- a family that includes many non-Gaussian laws such as the Laplace, logistic, or hyperbolic distributions. Focusing on the 2-Wasserstein distance, we show that all our structural results hold and our scalable Frank-Wolfe algorithm is applicable.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Literature Review", "weight": 1.0} -->

Our work is related to the literature on distributionally robust control, which seeks control policies that minimize expected costs under the worst-case system evolution (see, e.g., Bertsimas et al. Kim and Yang Kotsalis et al. Petersen et al. Van Parys et al. Yang, and references therein). Kim and Yang prove the optimality of linear state-feedback control policies for a related minimax LQR model with a Wasserstein distance but with perfect state observations. With perfect observations and zero-mean noise, the optimal policies in the classical LQR formulation are independent of the noise distribution and are thus inherently robust, so considering imperfect observations and non-zero mean noise is what makes the problem more challenging in our case. Closest to our work, Taşkesen et al. study the finite-horizon version of our model with a 2-Wasserstein distance and all noise distributions *required* to be zero-mean and Lanzetti et al. consider an infinite-horizon formulation with 2-Wasserstein distance and all noise distributions required to be *stationary and zero-mean*, and both papers prove that *affine* output-feedback policies are optimal.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Literature Review", "weight": 1.0} -->

Our work unifies and extends these previous results. We provide a unifying description of the ambiguity set via a divergence $\mathbb{D}$ that is required to satisfy a key property, which we verify for all the aforementioned examples considered in the literature and new examples that we identify. (Indeed, to the best of our knowledge, this is the first paper to consider entropy-regularized optimal transport or Fisher divergence for distributionally robust control problems.) Moreover, we do not restrict noise distributions to be zero mean in the finite-horizon case or stationary in the infinite-horizon case; instead, we allow the adversary more freedom and we prove -- under mild assumptions -- that such restrictions are without loss of optimality. Lastly, we draw a sharper distinction between affine and linear control policies and we characterize precisely when each class is optimal and how this is related to the adversary's choices.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Literature Review", "weight": 1.0} -->

We note that several papers in the literature have also considered robust formulations (with imperfect observations) for *constrained* systems, e.g., Ben-Tal et al., Van Parys et al., Kotsalis et al., Brouillon et al.; these models are more challenging and the common approach is to restrict attention to affine feedback policies for computational tractability and without proving their optimality.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Literature Review", "weight": 1.0} -->

Our work is also related to the literature on distributionally robust filtering for linear dynamical systems, which considers formulations without controls and focuses on the problem of estimating states. Zorzi studies a model based on $\tau$-divergences (a class that includes Kullback-Leibler divergence as a special instance) and Han considers a model based on 2-Wasserstein distance, for which tractable convex reformulations are derived. Within this stream, the closest works to ours are Shafieezadeh-Abadeh et al., Nguyen et al., which consider the problem of minimax mean-squared-error estimation when ambiguity is modeled with a 2-Wasserstein distance from a nominal Gaussian distribution, and Kargin et al., which relaxes the assumption that noise terms are iid and investigates both finite and infinite-horizon models, proving the optimality of linear filters when the nominal distribution is Gaussian and providing tractable convex reformulations using frequency-domain techniques.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Literature Review", "weight": 1.0} -->

For the case with Wasserstein distance, our proof relies on some ideas from these papers (such as using the Gelbrich distance to construct upper bounds), which we combine with ideas from control theory on purified output feedback to obtain the construction.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Literature Review", "weight": 1.0} -->

Our paper is also related to literature that documents the optimality of linear/affine policies in (distributionally) robust dynamic optimization models. Bertsimas et al., Iancu et al. prove optimality for one-dimensional linear systems affected by additive noise and with perfect state observations, but with general convex state and/or control costs. Hadjiyiannis et al., Van Parys et al. provide computationally tractable approaches for quantifying the suboptimality of affine control policies in finite- or infinite-horizon settings, and Bertsimas and Goyal, El Housni and Goyal, Georghiou et al. characterize the performance of affine policies in two-stage (distributionally) robust dynamic models.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Literature Review", "weight": 1.0} -->

Our proposed algorithm for solving the DRLQ problem is a variant of the classical Frank-Wolfe algorithm for solving convex optimization problems. The original paper introducing the ideas is Frank and Wolfe, and \[Taşkesen et al., \] also rely on these ideas to construct a tractable algorithm for the finite-horizon, 2-Wasserstein DRLQ formulation. We extend that construction and generalize it to other ambiguity sets.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Ambiguity Model, Assumptions, and Examples", "weight": 1.0} -->

We consider a discrete-time, linear dynamical system like the one described in § and assume that the initial state $x_{0}$ and the noise terms $\left\{ w_{t} \right\}_{t = 0}^{T - 1}$ and $\left\{ v_{t} \right\}_{t = 0}^{T - 1}$ are exogenously determined and governed by an unknown probability distribution. Because all random vectors appearing in our model are functions of these exogenous uncertainties, we set the sample space without loss of generality as $\Omega = {{\mathbb{R}}^{n} \times {\mathbb{R}}^{n \times T} \times {\mathbb{R}}^{p \times T}}$. We use $\mathcal{F}$ to denote the Borel $\sigma$-algebra on $\Omega$ and $\mathbb{P}$ to denote the joint probability distribution of these random vectors.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Ambiguity Model, Assumptions, and Examples", "weight": 1.0} -->

The joint distribution $\mathbb{P}$ is only known to belong to an ambiguity set $\mathcal{B}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Ambiguity Model, Assumptions, and Examples", "weight": 1.0} -->

where, for all $z \in \mathcal{Z}$ and for finite $\rho_{z} \geq 0$,

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumptions for Tractability", "weight": 1.0} -->

To maintain tractability and rule out uninteresting cases, we impose a few assumptions on the nominal distribution $\hat{\mathbb{P}}$ and on the structure of the ambiguity set $\mathcal{B}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Requiring $\hat{\mathbb{P}}$ to be Gaussian renders our model computationally tractable for several cases of practical interest and is consistent with the assumptions in the classical LQG model. Appendix §H shows that when the divergence $\mathbb{D}$ corresponds to a 2-Wasserstein distance, our results also hold for any *elliptical* nominal distribution $\hat{\mathbb{P}}$ with finite second moments -- a class that includes many *non*-Gaussian distributions such as the Laplace, logistic, or hyperbolic distributions. In general, computing the optimal control policy for an *arbitrary* distribution $\mathbb{P}$ would be very difficult because even computing the state estimator ${\hat{x}}_{t}$ is hard in that case, as formalized in the following result.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Assumption holds in several important cases (see §2.2) and admits an intuitive interpretation. Requirement (i) readily holds if the divergence ${\mathbb{D}}\left( {\mathbb{P}}_{z},{\hat{\mathbb{P}}}_{z} \right)$ depends only on the first two moments of the distributions ${\mathbb{P}}_{z},{\hat{\mathbb{P}}}_{z}$. If the divergence is based on an information-theoretic principle related to uncertainty, the Gaussian distribution may satisfy requirement (i) because it is the "most uncertain" (maximum-entropy) distribution for a given set of first and second moments; this happens in two of our examples, corresponding to the Kullback-Leibler and Fisher divergences.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

More broadly, (i) can be thought of as restricting attention to ambiguity sets $\mathcal{B}_{z}$ that are "dense in Gaussians": the requirement is satisfied if for any $0 \leq \rho \leq \rho_{z}$, the set of distributions in $\mathcal{B}_{z}$ with "distance" of at most $\rho$ from the nominal distribution -- if nonempty -- contains at least one Gaussian distribution. Part (ii) requires that the set of first and second moments characterizing all Gaussian distributions in the ambiguity set $\mathcal{B}_{z}$ is "well behaved," i.e., it is convex and compact. This enables us to evaluate worst-case expectations of *quadratic* functions of $z$ (prominent in the LQG model) over the ambiguity set $\mathcal{B}_{z}$ by solving finite-dimensional, convex optimization problems.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Examples", "weight": 1.0} -->

Assumption holds in several important instances, which we describe below. The formal results and proofs that help verify these properties are all included in Appendix §B.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Wasserstein Ambiguity Sets", "weight": 1.0} -->

Consider an ambiguity set where $\mathbb{D}$ corresponds to the 2-Wasserstein distance $\mathbb{W}$, defined as follows.
