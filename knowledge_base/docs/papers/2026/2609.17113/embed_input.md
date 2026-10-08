<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

The Price of Distributional Robustness in Linear Quadratic Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Distributionally robust (DR) optimization seeks decisions that perform best under the most adverse law within a given ambiguity set, enabling the design of data-driven controllers with strong out-of-sample guarantees in the face of uncertainty. In this paper, we study the conservatism introduced by safeguarding against distributional ambiguity. Specifically, we consider the data-driven Wasserstein DR linear quadratic control problem, and we analyze the suboptimality of the corresponding solution relative to the oracle controller computed with foreknowledge of the underlying unknown uncertainty distribution. We present a sample complexity bound that characterizes the number of samples required to ensure that the true cost of the DR solution exceeds that of the oracle controller by at most a user-defined tolerance factor. Our analysis reveals that the suboptimality of the DR solution increases at most linearly with the Wasserstein radius for sufficiently small distributional ambiguity, and at most quadratically away from this local regime. Numerical simulations validate our bounds on the price of distributional robustness.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Modern intelligent systems, such as microgrid controllers and autonomous vehicles, must make dependable decisions to ensure reliable operation in the face of uncertainty. In many applications, however, the probability distribution governing the uncertain problem parameters is itself uncertain and only indirectly observable through samples. This is the case, for instance, when renewable generation forecast errors and demand fluctuations are inferred from historical data, or when the future behavior of nearby traffic agents is estimated from limited observations of merging, braking, and lane-changing maneuvers.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

In these scenarios, classical stochastic optimal control methods do not readily apply, as they generally require full knowledge of the underlying uncertainty distribution. In addition, common workarounds, such as replacing the unknown true distribution with a nominal estimate, often fail to provide satisfactory performance, since the optimization process can amplify estimation errors in the input model---a phenomenon referred to in the literature as the optimizer's curse. To address this challenge, the emerging paradigm of distributionally robust (DR) control aims to design policies that perform best under the most averse law within a given family of distributions. Different approaches have been proposed to construct this ambiguity set, for instance by leveraging prior information about finitely many moments of the true distribution, or by bounding the dissimilarity from a nominal law using $\phi$-divergences, optimal transport discrepancies, or combinations thereof.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Among these different choices, optimal transport ambiguity sets---and Wasserstein balls in particular---have recently received considerable attention due to their favorable computational and statistical properties. They naturally propagate through dynamical transformation and often yield DR optimization problems that admit computationally tractable strong dual reformulations. In addition, in data-driven settings where the nominal distribution is empirical, Wasserstein DR control policies enjoy rigorous out-of-sample guarantees. Specifically, under a light-tailed assumption on the true law and with a judicious choice of the Wasserstein radius, measure concentration results ensure that the Wasserstein ball centered at the empirical distribution contains the true law with high probability. Hence, the DR objective of any admissible control policy provides an upper confidence bound on the corresponding true cost under the unknown data-generating distribution.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

These finite-sample guarantees make DR optimization a principled framework for data-driven control under uncertainty. At the same time, however, they leave open a fundamental question: how suboptimal is the DR policy relative to the oracle controller designed with foreknowledge of the true distribution? Quantifying this gap is key to understanding the underlying design tradeoffs, namely, whether distributional robustness comes at a negligible or significant loss in performance, and in which regimes using additional samples can yield meaningful performance improvements relative to the added computational effort required to solve larger DR optimal control problem instances.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we study the price of distributional robustness in data-driven Wasserstein DR linear quadratic control and provide quantitative answers to these questions. In particular, we first characterize the growth rate of the suboptimality of the DR solution and prove that the performance loss relative to the oracle controller converges to zero approximately as a linear function of the Wasserstein radius. Building on this characterization, we then derive explicit bounds on the Wasserstein radius and the number of samples required to ensure that the excess cost of the DR solution remains below a user-defined tolerance factor with high probability. Our analysis combines concentration bounds for empirical measures and subgaussian random variables with a novel outer approximation of the Wasserstein ambiguity set of zero mean distributions in a neighborhood of the centered empirical law, constructed by ignoring higher-order moment information. Last, we discuss how the considered data-driven Wasserstein DR optimal control problem can be solved via convex programming, using duality to restrict the adversary's choice to zero mean laws, and present numerical experiments validating our theoretical findings.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

More broadly, our analysis is also related to recent suboptimality and sample-complexity results for learning linear quadratic regulators from data. While our derivations share some technical tools with this line of work, the source of uncertainty is fundamentally different: these works study on the effect of parametric model uncertainty on the closed-loop system, whereas our focus is on distributional ambiguity.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

We consider a discrete-time linear time-varying dynamical system described by the state-space equations where $x_{t}\in\mathbb{R}^{n}$ is the system state, $u_{t}\in\mathbb{R}^{m}$ is the control input, $y_{t}\in\mathbb{R}^{p}$ is the measurable output, and $w_{t}\in\mathbb{R}^{n}$ and $v_{t}\in\mathbb{R}^{p}$ denote stochastic process and measurement disturbances, respectively.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

We study the evolution of over a finite-time control horizon of length $T\in\mathbb{N}$, and collect all exogenous random variables in the vector $\bm{\xi}=(\mathbf{w},\mathbf{v})\in\mathbb{R}^{d}$ for compactness, where $\mathbf{w}=(x_{0},w_{0},\dots,w_{T-2})$ and $\mathbf{v}=(v_{0},\dots,v_{T-1})$. We denote the true distribution of $\bm{\xi}$ by $\mathbb{P}^{\star}$, and only assume partial information about $\mathbb{P}^{\star}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Our objective is to characterize the price of distributional robustness by establishing a bound on the number of samples $N$ needed to ensure that the cost of a DR controller constructed from $\mathcal{D}$ exceeds the cost of the $\mathbb{P}^{\star}$-optimal controller by at most a tolerance factor $\epsilon\in\mathbb{R}_{>0}$. Toward formalizing this objective, we first restrict our attention to linear feedback policies of the form $\mathbf{u}=\mathbf{K}\mathbf{y}$, where $\mathbf{u}=(u_{0},\dots,u_{T-1})$, $\mathbf{y}=(y_{0},\dots,y_{T-1})$, and the dynamic controller $\mathbf{K}$ is given by a lower block-triangular matrix due to causality.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Then, for any $\mathbb{P}\in\mathcal{P}$, we introduce the standard performance criterion where $\mathbf{x}=(x_{0},\dots,x_{T-1})$, $\mathbf{Q}\succeq 0$, and $\mathbf{R}\succ 0$. We define the $\mathbb{P}^{\star}$-optimal controller $\mathbf{K}^{\star}$ as where $\mathcal{K}$ represents the set of all feedback matrices complying with the lower block-triangular causality sparsity pattern.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

As $\mathbb{P}^{\star}$ is only indirectly observable from the samples $\bm{\xi}^{k}\in\mathcal{D}$, computing the $\mathbb{P}^{\star}$-optimal controller $\mathbf{K}^{\star}$ in is in general not possible. We therefore adopt a data-driven DR approach and design a controller that performs best under the most averse distribution that lies sufficiently close to the empirical law $\hat{\mathbb{P}}$ constructed from the samples $\bm{\xi}^{k}\in\mathcal{D}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Specifically, as $\mathbb{P}^{\star}\in\mathcal{P}$ is zero mean by assumption, we let where $\delta(\bm{\xi})$ is the Dirac delta distribution at the point $\bm{\xi}\in\mathbb{R}^{d}$ and $\bar{\bm{\xi}}=\frac{1}{N}\sum_{k=1}^{N}\bm{\xi}_{k}$ denotes the empirical mean. To mitigate the optimizer's curse, we then robustify our decision against all distributions $\mathbb{P}$ whose Wasserstein distance $\mathbb{W}(\hat{\mathbb{P}},\mathbb{P})$ from $\hat{\mathbb{P}}$ is at most $\rho\in\mathbb{R}_{\geq 0}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Formally, let where $\Pi(\hat{\mathbb{P}},\mathbb{P})$ denotes the set of all joint distributions of $\hat{\bm{\xi}}$ and $\bm{\xi}$ with marginal distributions $\hat{\mathbb{P}}$ and $\mathbb{P}$, respectively.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

With this notation at hand, we construct the ambiguity set and formulate the Wasserstein DR optimal control problem as We remark that, as we only include zero mean distributions $\mathbb{P}\in\mathcal{P}$ in the Wasserstein ambiguity set $\mathbb{B}_{\mathbb{W}}^{\rho}(\hat{\mathbb{P}})$ as per, using a centered empirical distribution as per is crucial to ensure that $\mathbb{B}_{\mathbb{W}}^{\rho}(\hat{\mathbb{P}})$ is non-empty and that the optimal control problem is thus well-posed for every $\rho\in\mathbb{R}_{\geq 0}$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

We are now ready to state our main research questions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Statement", "weight": 1.0} -->

Below, we present a suboptimality and sample complexity analysis to provide quantitative answers to these two questions.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Main Results", "weight": 1.0} -->

We now present our main results. In Section III-A, we first construct an outer approximation of the Wasserstein ambiguity set $\mathbb{B}_{\mathbb{W}}^{\rho}(\hat{\mathbb{P}})$ in by ignoring any higher-order moment information, and, for a given policy $\mathbf{K}$, we bound the DR cost $J_{\text{dr}}(\mathbf{K})$ in in terms of the average cost $J(\mathbf{K},\hat{\mathbb{P}})$ incurred by the *same* policy on the nominal distribution $\hat{\mathbb{P}}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Main Results", "weight": 1.0} -->

Then, leveraging standard concentration results for empirical laws and subgaussian random variables, we answer questions 1) and 2) above by showing that the price of distributional robustness admits a global quadratic upper bound in $\rho$, and that, for sufficiently small $\rho$, the number of samples $N$ required to meet an $\epsilon$ suboptimality factor scales with $\frac{1}{\epsilon^{d}}$. Last, in Section III-B, we discuss how the DR optimal control problem can be solved using semidefinite programming, leveraging duality theory to restrict the adversary's choice to zero mean laws in the inner supremum.

<!-- chunk {"id": "body-0021", "role": "body", "section": "III-A Suboptimality and sample complexity analysis", "weight": 1.0} -->

We begin our analysis by introducing an equivalent characterization of the quadratic performance objective in terms of the closed-loop system responses induced by a feedback controller $\mathbf{K}\in\mathcal{K}$. To this end, we first compactly rewrite the dynamics over a control horizon of length $T\in\mathbb{N}$ as where $\mathbf{Z}$ denotes the block-downshift operator, namely, a matrix with identity matrices along its first block sub-diagonal and zeros elsewhere, $\mathbf{A}=\operatorname{blkdiag}(A_{0},\dots,A_{T-1})$, $\mathbf{B}=\operatorname{blkdiag}(B_{0},\dots,B_{T-1})$, and $\mathbf{C}=\operatorname{blkdiag}(C_{0},\dots,C_{T-1})$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "III-A Suboptimality and sample complexity analysis", "weight": 1.0} -->

Then, we observe that the feedback interconnection of with a linear policy $\mathbf{u}=\mathbf{K}\mathbf{y}$ yields the relations where the closed-loop maps $\bm{\Phi}_{xx}$, $\bm{\Phi}_{xy}$, $\bm{\Phi}_{ux}$, and $\bm{\Phi}_{uy}$ above are defined as In particular, we remark that there exists $\mathbf{K}\in\mathcal{K}$ such that holds if and only if the closed-loop maps $\bm{\Phi}_{xx}$, $\bm{\Phi}_{xy}$, $\bm{\Phi}_{ux}$, and $\bm{\Phi}_{uy}$ are causal and lie in the affine subspace defined by accordingly, we say that a set of closed-loop maps $\bm{\Phi}_{xx}$,

<!-- chunk {"id": "body-0023", "role": "body", "section": "III-A Suboptimality and sample complexity analysis", "weight": 1.0} -->

In Section III-B, we will leverage this parametrization of dynamic controllers $\mathbf{K}\in\mathcal{K}$ to derive an equivalent reformulation of as a convex optimization problem. With this notation in place, we can now rewrite the objective as a weighted squared Frobenius norm of the closed-loop responses following.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Our next result shows how to calibrate the Wasserstein radius $\rho$ by leveraging concentration results for empirical measures and subgaussian random variables. For simplicity, we assume in the following that $d>4$; a similar result also holds true without this assumption but requires a more complicated formula for $\rho^{\star}_{w}$ in Lemma 2 below, see also.

<!-- chunk {"id": "body-0025", "role": "body", "section": "III-B Numerical implementation", "weight": 1.0} -->

As the average performance objective is nonconvex in $\mathbf{K}$ and the ambiguity set $\mathbb{B}_{\mathbb{W}}^{\rho}(\hat{\mathbb{P}})$ is infinite dimensional, directly solving the Wasserstein DR optimal control problem over controllers $\mathbf{K}\in\mathcal{K}$ is in general difficult. Our next result addresses these two challenges by instead optimizing over the closed-loop maps and using duality theory to derive a finite-dimensional reformulation of the adversary's subproblem over zero mean distributions $\mathbb{P}\in\mathbb{B}_{\mathbb{W}}^{\rho}(\hat{\mathbb{P}})\subset\mathcal{P}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Experiments", "weight": 1.0} -->

In this section, we present numerical simulations to validate our theoretical bounds on the price of distributional robustness in Theorem 1. For our experiments, we consider the open-loop unstable system described by the state-space equations We fix a control horizon of length $T=5$ and assume that the unknown true law $\mathbb{P}^{\star}$ of $\bm{\xi}=(x_{0},w_{0},\dots,w_{3},v_{0},\dots,v_{4})$ is a standard Gaussian distribution. Assuming full knowledge of $\mathbb{P}^{\star}$, we first compute the linear quadratic Gaussian (LQG) controller $\mathbf{K}^{\star}$ that minimizes the expected cost, where $\mathbf{R}$ is an identity matrix of appropriate dimensions and $\mathbf{Q}\succ 0$ is randomly selected.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Experiments", "weight": 1.0} -->

Then, we construct a training dataset $\mathcal{D}$ by drawing $N_{\max}=5\cdot 10^{4}$ independent samples $\bm{\xi}^{k}\sim\mathbb{P}^{\star}$, and repeatedly solve the semidefinite program for different Wasserstein radii $\rho\in[10^{-4},2]$ and training dataset sizes $N\in[50,N_{\max}]$ to obtain the corresponding DR optimal control policy $\mathbf{K}_{\text{dr}}^{\star}(\rho,N)$.^22^ 2 The source code that reproduces our numerical examples is available at github.com/andrea-martin/price-dro.git.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate the true average cost incurred by each controller using with $\mathbb{P}=\mathbb{P}^{\star}$, and compute their normalized suboptimality $\varsigma(\rho,N)$ relative to $\mathbf{K}^{\star}$ as We collect our results in Figure 1, which reports a comparison between the empirical suboptimality $\varsigma(\rho,N)$ and our theoretical upper bound. [width=]./figures/average_suboptimality.pdf Fig. 1: Empirical suboptimality 𝜍(ρ, N) of the DR optimal policy Kdr⋆ relative to the oracle controller K⋆ computed with foreknowledge of ℙ⋆, as a function of the Wasserstein radius ρ and the number N of training samples ξk ∼ ℙ⋆. Error bars indicate one standard deviation around the mean values, computed over 10 independent draws of Nmax training samples ξk ∼ ℙ⋆.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Experiments", "weight": 1.0} -->

While this experiment does not meet all conditions of Theorem 1---Assumption 1 imposes a decay rate for the tails of the true law $\mathbb{P}^{\star}$ that is faster than that of a standard Gaussian distribution, and the number of samples $N^{\star}(\rho,\zeta)$ required to ensure that $\mathbb{P}^{\star}\in\mathbb{B}_{\mathbb{W}}^{\rho}(\hat{\mathbb{P}})$ in Corollary 1 is prohibitively large since $\bm{\xi}\in\mathbb{R}^{14}$---Figure 1 highlights that our theoretical bound nevertheless captures the growth rate of $\varsigma(\rho,N)$. In fact, as $N$ increases, the dotted line representing becomes nearly parallel to the empirical suboptimality for $\rho$ approximately greater than $10^{-2}$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Experiments", "weight": 1.0} -->

Furthermore, Figure 1 showcases that, for $N=50$ and $N=100$, the empirical suboptimality $\varsigma(\rho,N)$ initially decreases with $\rho$, validating the effectiveness of DR optimization in mitigating the optimizer's curse when only a limited number of training samples $\bm{\xi}^{k}\sim\mathbb{P}^{\star}$ are available for control design. For larger values of $N$, instead, the empirical distribution $\hat{\mathbb{P}}$ better approximates the true law $\mathbb{P}^{\star}$ and the price of distributional robustness increases monotonically with $\rho$ as predicted.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Experiments", "weight": 1.0} -->

At the same time, the fact that our theoretical bound is numerically valid even when $N$ does not exceeds $N^{\star}(\rho,\zeta)$ in Corollary 1 suggests that the bound can become loose when $d$ is large, due to the curse of dimensionality. This claim is supported by Figure 2, which displays a lower bound to $\mathbb{W}(\hat{\mathbb{P}},\mathbb{P}^{\star})$, showing that in our experiment the bound often holds true even when $\mathbb{P}^{\star}\not\in\mathbb{B}_{\mathbb{W}}^{\rho}(\hat{\mathbb{P}})$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Experiments", "weight": 1.0} -->

In particular, the blue line in Figure 2 represents a numerical approximation of the sliced Wasserstein distance $\mathbb{SW}(\hat{\mathbb{P}},\mathbb{P}^{\star})$, formally defined as where, for any $\bm{\psi}\in\mathbb{S}^{d-1}$ and $\mathbb{P}\in\mathcal{P}$, $\mathbb{P}_{\bm{\psi}}$ denotes the one-dimensional distribution of the projection $\langle\bm{\psi},\bm{\xi}\rangle$, $\bm{\xi}\sim\mathbb{P}$, and $\sigma$ is the uniform probability measure on the unit sphere $\mathbb{S}^{d-1}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Experiments", "weight": 1.0} -->

[width=]./figures/lb_distance_computational_time.pdf Fig. 2: Sliced Wasserstein distance $\mathbb{SW}(\hat{\mathbb{P}},\mathbb{P}^{\star})$ (on the left y-axis) and average computational time required to evaluate the DR optimal policy Kdr⋆ through the semidefinite program (on the right y-axis), as a function of the number N of samples ξk ∼ ℙ⋆ in the training dataset 𝒟. Error bars indicate one standard deviation around the mean values, computed over 10 independent draws of Nmax training samples ξk ∼ ℙ⋆.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Experiments", "weight": 1.0} -->

Last, we highlight that Figure 1 suggests that progressively increasing the number of training samples $\bm{\xi}^{k}\sim\mathcal{D}$ comes with diminishing returns, despite the considerably higher computational cost required to solve through convex programming when $N$ is large, as shown by the orange curve in Figure 2.^33^ 3 All optimization problems have been solved using MOSEK on a standard laptop computer with a 2.3 GHz Intel Core i9 CPU. For all $\rho\in[10^{-4},2]$, we in fact observe that the relative improvement in the empirical suboptimality $\varsigma(\rho,N)$ decreases as $N$ grows up where, for $\rho$ sufficiently large, the empirical suboptimality of all DR controllers $\mathbf{K}_{\text{dr}}^{\star}(\rho,N)$ converges to approximately the same value, irrespective of $N$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we studied the price of distributional robustness in data-driven Wasserstein DR linear quadratic control. Leveraging a novel outer approximation of data-driven Wasserstein ambiguity sets, constructed by ignoring higher-order moment information, we showed that the suboptimality of the DR controller relative to the oracle controller with knowledge of the true uncertainty distribution grows at most linearly with the Wasserstein radius for sufficiently small distributional ambiguity, and at most quadratically outside this local regime. We further established a sample complexity bound ensuring that the DR solution incurs a suboptimality no higher than a prescribed level with high probability. Finally, we showed that the resulting Wasserstein DR control problem admits a tractable reformulation as a semidefinite program, and we presented numerical experiments illustrating the qualitative behavior predicted by our theoretical bounds. Inspired by recent results, an interesting direction for future work is to derive less conservative finite-sample guarantees that mitigate the dependence of our concentration bounds on the dimensionality of the uncertainty.
