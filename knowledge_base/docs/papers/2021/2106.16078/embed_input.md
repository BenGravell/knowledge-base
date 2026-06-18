<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Identification of Linear Systems with Multiplicative Noise from Multiple Trajectory Data

Topics include System identification, Linear systems, Multiplicative noise, Stochastic systems, Multiple trajectory data, Least-squares estimation, Covariance estimation, Identifiability, Second-moment dynamics, Asymptotic consistency, Non-asymptotic, High-probability, Sample complexity, Excitation conditions, Controllability, Data-driven control.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Extends the asymptotic results of 2002.06613 to rigorous non-asymptotic finite-sample results, using basically the same system identification / parameter estimation algorithm.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The paper studies identification of linear systems with multiplicative noise from multiple-trajectory data. An algorithm based on the least-squares method and multiple-trajectory data is proposed for joint estimation of the nominal system matrices and the covariance matrix of the multiplicative noise. The algorithm does not need prior knowledge of the noise or stability of the system, but requires only independent inputs with pre-designed first and second moments and relatively small trajectory length. The study of identifiability of the noise covariance matrix shows that there exists an equivalent class of matrices that generate the same second-moment dynamic of system states. It is demonstrated how to obtain the equivalent class based on estimates of the noise covariance. Asymptotic consistency of the algorithm is verified under sufficiently exciting inputs and system controllability conditions. Non-asymptotic performance of the algorithm is also analyzed under the assumption that the system is bounded. The analysis provides high-probability bounds vanishing as the number of trajectories grows to infinity. The results are illustrated by numerical simulations.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The study of stochastic systems with multiplicative noise (i.e., system states and inputs multiplied by noise) has a long history in control theory, and is re-emerging in the context of complex networked systems and learning-based control. In contrast to the additive-noise setting, the multiplicative-noise modeling framework has the ability to capture the coupling between noise and system states. This situation occurs in modern control systems as diverse as robotics with distance-dependent sensor errors, networked systems with noisy communication channels, modern power networks with high penetration of intermittent renewables, turbulent fluid flow, and neuronal brain networks. Linear systems with multiplicative noise are particularly attractive as a stochastic modeling framework because they remain simple enough to admit closed-form expressions for stabilization and optimal control.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is important to study identification of linear systems with multiplicative noise, because, when solving problems such as control design of multiplicative-noise linear quadratic regulator (LQR), system parameters including the nominal system matrices and the noise covariance matrix, especially the latter, generally need be known. In contrast, for the design problem of additive-noise LQR, the covariance matrix of additive noise needs not be known. Moreover, the identification problem requires further investigation; for instance, it is unclear how to formally quantify identifiability issues resulting from coupling between system states and multiplicative noise, and how to design identification algorithms to efficiently tackle the influence of multiplicative noise.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another issue that must be addressed is how to perform system identification based on multiple-trajectory data, rather than on single-trajectory data. Multiple-trajectory data arises in two broad situations: episodic tasks where a system is reset to an initial state after a finite run time, as encountered in iterative learning control and reinforcement learning; and data collected from multiple identical systems in parallel, for example, robotic-grasping dataset collected by Google running several robot arms concurrently. For multiple-trajectory data, the length of each trajectory may be small, but the number of trajectories can be large. However, the classic literature of system identification mainly focuses on studying online estimation over a single trajectory, so there is a need to study how to identify systems based on multiple-trajectory data. In addition, system identification based on multiple trajectories can be a pre-step of conducting other tasks such as control design of LQR. Thus, studying the performance of identification algorithms based on multiple trajectories is necessary for obtaining performance guarantees of later tasks.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contributions", "weight": 1.0} -->

This paper considers identification of linear systems with multiplicative noise from multiple-trajectory data.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

An algorithm (Algorithm 1) based on the least-squares method and multiple-trajectory data is proposed for joint identification of the nominal system matrices and the multiplicative noise covariance from multiple-trajectory data. The algorithm does not need prior knowledge of the noise or stability of the system, but requires only independent inputs with pre-designed first and second moments, relatively small length for each trajectory, and the assumption of independent and identically distributed (i.i.d.) noise with finite first and second moments. It is theoretically shown that, under the preceding conditions, the algorithm solves the identification problem.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contributions", "weight": 1.0} -->

Identifiability of the noise covariance matrix is investigated (Propositions 1 and 2). It is shown that there exists an equivalent class of covariance matrices that generate the same second-moment dynamic of system states. In addition, it is studied when such equivalent class has a unique element, meaning that the covariance matrix can be uniquely determined. An explicit expression of the equivalent class is provided for the recovery of the noise covariance based on estimates given by the proposed algorithm.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contributions", "weight": 1.0} -->

Asymptotic consistency of the proposed algorithm is verified (Theorem 3.10), under sufficiently exciting inputs and system controllability conditions. Non-asymptotic estimation performance is also analyzed under the assumption that the system is bounded. This analysis provides high-probability error bounds, which vanish as the number of trajectories grows to infinity (Theorems 3.16 and 3.17).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contributions", "weight": 1.0} -->

Compared with Di and Lamperski the current paper provides high-probability error bounds, for the proposed algorithm, that converge to zero as the number of trajectories increases. In addition, identifiability of the noise covariance matrix is thoroughly studied, and conditions, under which the covariance matrix is uniquely determined, are provided. In our problem, because of the complicated structure of the second-moment dynamic of system states, both analysis of the error bounds and study of the identifiability require more elaborate use of tools from linear algebra and high-dimensional probability theory. The differences between this paper and its conference version are as follows. This paper studies identifiability of the noise covariance matrix in detail, demonstrating a framework to recover the equivalent class of covariance matrices. Moreover, sharper bounds for the required length of each trajectory are obtained. Finally, finite sample analysis of the proposed algorithm is provided.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Outline", "weight": 1.0} -->

The remainder of the paper is organized as follows. The problem is formulated in Section 2. In Section 3 the algorithm is introduced and theoretical results are given. Numerical simulation results are presented in Section 4. Section 5 concludes the paper. Some proofs are postponed to Appendix.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Outline", "weight": 1.0} -->

Denote the $n$-dimensional Euclidean space by ${\mathbb{R}}^{n}$, and the set of $n \times m$ real matrices by ${\mathbb{R}}^{n \times m}$. Let $\mathbb{N}$ stand for the set of nonnegative integers, and ${\mathbb{N}}^{+}:={{\mathbb{N}} \smallsetminus {\{ 0\}}}$. Let ${\lbrack k\rbrack}:={\{ 1,2,\ldots,k\}}$, $k \in {\mathbb{N}}^{+}$. We use $\parallel \cdot \parallel$ to denote the Euclidean norm for vectors, and use $\parallel \cdot \parallel_{F}$ and $\parallel \cdot \parallel_{2}$ to denote the Frobenius and spectral norm for matrices.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Outline", "weight": 1.0} -->

The probability of an event $E$ is denoted by ${\mathbb{P}}{\{ E\}}$, and the expectation of a random vector $x$ is represented by ${\mathbb{E}}{\{ x\}}$. An event happening almost surely (a.s.) means that it happens with probability one. Let $A \times B$ be the Cartesian product of sets $A$ and $B$, namely, ${A \times B} = {\{{(a,b)}:{{a \in A},{b \in B}}\}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Outline", "weight": 1.0} -->

Let $a_{ij}$ or ${\lbrack A\rbrack}_{ij}$ represent the $(i,j)$-th entry of $A \in {\mathbb{R}}^{n \times m}$. Denote the $n$-dimensional all-one vector and all-zero vector by $\mathbf{1}_{n}$ and $\mathbf{0}_{n}$, respectively. The $n$-dimensional unit vector with $i$-th component being one is represented by $\mathbf{e}_{i}^{n}$. $I_{n}$ is the $n$-dimensional identity matrix.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Outline", "weight": 1.0} -->

For two symmetric matrices ${A,B} \in {\mathbb{R}}^{n \times n}$, $A \succeq 0$ ($A \succ 0$) means that $A$ is positive semidefinite (positive definite), and $A \succeq B$ ($A \succ B$) means that ${A - B} \succeq 0$ (${A - B} \succ 0$). For a matrix $A \in {\mathbb{R}}^{n \times n}$, $\rho{(A)}$ represents the spectral radius of $A$. For a symmetric matrix $A \in {\mathbb{R}}^{n}$, denote its smallest and largest eigenvalue by $\lambda_{\min}{(A)}$ and $\lambda_{\max}{(A)}$ respectively.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Consider the linear system with multiplicative noise

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

An example of System is the following system studied in the optimal control literature,

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In the rest of the paper, a trajectory sample is referred to as a *rollout*.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

$n_{r}$ is the number of rollouts. The problem considered in this paper is as follows.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Identification Algorithm Based on Least-Squares and Multiple-Trajectory Data", "weight": 1.0} -->

In this section, we propose and study an identification algorithm solving the considered problem. Section 3.1 studies identifiability of the noise covariance matrix, paving the way to algorithm design. Consistency of the algorithm is given by Theorem 3.10 in Section 3.2. Finally, sample complexity of the algorithm is studied in Section 3.3, and the results are provided in Theorems 3.16 and 3.17.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Moment Dynamics and Algorithm Design", "weight": 1.0} -->

In this subsection, we propose an algorithm based on multiple trajectories collected independently to estimate system parameters. Before algorithm design, the effect of multiplicative noise on moment dynamics is studied, and identifiability of the noise covariance matrix is clarified.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Moment Dynamics and Algorithm Design", "weight": 1.0} -->

Note that ${\overset{\sim}{X}}_{t}$ and ${\overset{\sim}{U}}_{t}$ have no redundant entries but are able to capture the second-moment dynamic of system states. By the definition of Kronecker product, $\Sigma_{A}^{\prime}$ and $\Sigma_{B}^{\prime}$ have the following structures.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 3.1", "weight": 1.0} -->

We may only estimate the sum of these two entries out of $X_{t}$, rather than their exact values, since realizations of ${\overline{A}}_{t}$ and ${\overline{B}}_{t}$ are not observed directly but indirectly through their effect on system states.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 3.1", "weight": 1.0} -->

Critically, since these identifiable quantities uniquely generate the second-moment dynamic of system states, it suffices to estimate ${\overset{\sim}{\Sigma}}_{A}^{\prime}$ and ${\overset{\sim}{\Sigma}}_{B}^{\prime}$ for LQR design. This fact can be verified by expanding the Bellman equation; we omit the details to keep the paper concise.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Example 3.2", "weight": 1.0} -->

According to the previously discussed simplification, from

<!-- chunk {"id": "body-0027", "role": "body", "section": "Example 3.2", "weight": 1.0} -->

In this example, $\Sigma_{B}$ is unique, but based on the covariance matrix $\Sigma_{A}{(\alpha)}$, equivalent to $\Sigma_{A}$, is given by

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 3.4", "weight": 1.0} -->

Now we are ready to propose our estimation algorithm. Following the previous discussion, we introduce an algorithm based on the first- and second-moment dynamics and. Since the exact moment dynamics are unavailable, we average over multiple independent rollouts to obtain their estimates. To get persistently exciting inputs, it is necessary to design their first and second moments in advance, in either a deterministic or a stochastic way. For example, generate the two moments from standard Gaussian and Wishart distributions, respectively, or set them periodically. The initial states of different rollouts are assumed to be i.i.d. subject to a same distribution $\mathcal{X}_{0}$ with finite second moment (see Section 3.2.2). The overall algorithm is shown in Algorithm 1, where the superscript $(k)$ represents the $k$-th rollout. Note that Algorithm 1 is different from classic recursive identification algorithms. The recursive least-squares algorithm, for example, uses only one trajectory of a system. In contrast, Algorithm 1 is based on multiple trajectories with finite length.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 3.4", "weight": 1.0} -->

Based on the estimates ${\hat{\overset{\sim}{\Sigma}}}_{A}^{\prime}$ and ${\hat{\overset{\sim}{\Sigma}}}_{B}^{\prime}$, it is able to obtain an estimate ${\hat{S}}_{\Sigma}^{\ast}$ of the equivalent class, via replacing ${\overset{\sim}{\Sigma}}_{A}^{\prime}$ and ${\overset{\sim}{\Sigma}}_{B}^{\prime}$ in the definition by their estimates. If the linear matrix inequalities are infeasible (i.e., ${\hat{S}}_{\Sigma}^{\ast} = \varnothing$), then project the estimates onto the positive semidefinite cone. However this situation is unlikely to happen when $n_{r}$ is large, because of the consistency of Algorithm 1 given in the next section.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 3.4", "weight": 1.0} -->

1:Input: Rollout length ℓ and the number of rollouts nr.
2:Output: [Â B̂], $\lbrack{{\hat{\overset{\sim}{\Sigma}}}_{A}^{\prime}{\hat{\overset{\sim}{\Sigma}}}_{B}^{\prime}}\rbrack$.
5: Generate νt ∈ ℝm and ${\overline{U}}_{t} \in {\mathbb{R}}^{m \times m}$ with ${\overline{U}}_{t} \succeq 0$.
9: Generate x0(k) independently from the initial multivariate distribution 𝒳0.
11: Generate ut(k) independently from a multivariate distribution with first moment νt and second central

<!-- chunk {"id": "body-0031", "role": "body", "section": "Performance of Algorithm 1", "weight": 1.0} -->

This section analyzes performance of Algorithm 1 by investigating the moment dynamics and.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Moment Dynamics and Input Design", "weight": 1.0} -->

Provided that $\mu_{t}$ and ${\overset{\sim}{X}}_{t}$ are known, it is possible to recover the parameters via least-squares as in lines $14$-$16$ in Algorithm 1. Denote

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 3.5", "weight": 1.0} -->

The proposition shows that for large enough rollout length, the full row rankness of $\mathbf{Z}$ can be guaranteed for almost all ${\lbrack{\nu_{0}^{\intercal}\cdots\nu_{\ell - 1}^{\intercal}}\rbrack}^{\intercal} \in {\mathbb{R}}^{m\ell}$. The controllability of $(A,B)$ plays a key role in the proof, similar to classic results on identification of linear systems. The condition $\ell \geq {n + m}$ is necessary for the invertibility of ${\mathbf{Z}\mathbf{Z}}^{\intercal}$. This lower bound is much smaller than that given in Xing et al.,. According to the proposition, ${\mathbf{Z}\mathbf{Z}}^{\intercal}$ is invertible with probability one if the first moments of inputs are generated i.i.d.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 3.5", "weight": 1.0} -->

from a distribution absolutely continuous with respect to Lebesgue measure (e.g., Gaussian distribution or uniform distribution). This proposition can be seen as a generalization of the single-input case studied in Schmidt et al.,.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 3.6", "weight": 1.0} -->

The controllability condition in Proposition 4 reflects the nature of the multiplicative noise (i.e., coupling between ${\overline{A}}_{t}$ and $x_{t}$, and that between ${\overline{B}}_{t}$ and $u_{t}$). The result indicates that a controllability condition on may be necessary to ensure successful identification. The lower bound for $\ell$ is necessary for the invertibility of ${\mathbf{D}\mathbf{D}}^{\intercal}$, and is much smaller than that given in Xing et al.,.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 3.6", "weight": 1.0} -->

We summarize the preceding two results in the following corollary.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 3.8", "weight": 1.0} -->

The corollary implies that the existence of ${({\mathbf{Z}\mathbf{Z}}^{\intercal})}^{- 1}$ and ${({\mathbf{D}\mathbf{D}}^{\intercal})}^{- 1}$ can be guaranteed with probability one, as long as both $\nu_{t}$ and ${\overline{U}}_{t}$ are independently generated from distributions that is absolutely continuous with respect to Lebesgue measure. For example, the entries of $\nu_{t}$ are generated i.i.d. from a non-degenerate Gaussian distribution and then ${\overline{U}}_{t}$ is generated i.i.d. from a non-degenerate Wishart distribution, $0 \leq t \leq {\ell - 1}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Asymptotic Consistency", "weight": 1.0} -->

In this subsection, we assume that the expectations and covariance matrices of inputs have been generated as discussed in the previous section, and that both ${\mathbf{Z}\mathbf{Z}}^{\intercal}$ and ${\mathbf{D}\mathbf{D}}^{\intercal}$ have been designed to be invertible. The closed-form estimates generated by Algorithm 1 are

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 3.9", "weight": 1.0} -->

From Corollary 3.7, the lower bound of the rollout length in Assumption 1 (i) is necessary for estimating the noise covariance matrix, whereas, from Proposition 3, trajectories with length $\ell \geq {n + m}$ may be enough for estimating the nominal system matrix. The initial states of different trajectories need not start with the same value, but it is required that they have the same first and second moments (Assumption 1 (ii)). The mutual independence of noise at different time steps in one trajectory is a standard assumption (Assumption 1 (iii)), but the results in this paper still hold, if the noise sequence in the same trajectory is dependent, but the noise sequences in different trajectories are mutually independent and the noise has zero mean and the same second moment. The physical meaning of the independence between the noise and the inputs in Assumption 1 (iv) is that the former is an intrinsic part of the system and cannot be influenced by inputs.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 3.9", "weight": 1.0} -->

To keep the analysis concise, we separately discuss the input design (Section 3.2.1) and the performance of Algorithm 1. Assumption 1 (v) indicates that the input design yields invertible ${\mathbf{Z}\mathbf{Z}}^{\intercal}$ and ${\mathbf{D}\mathbf{D}}^{\intercal}$, but note that it implicitly assumes the controllability of the first- and second-moment dynamics of system states.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 3.9", "weight": 1.0} -->

Under Assumption 1 the rollouts $\lbrack x_{0}^{(k)},\ldots,x_{l}^{(k)}\rbrack$, $k \in {\lbrack n_{r}\rbrack}$, are i.i.d., so the following consistency result can be obtained from strong law of large numbers.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 3.11", "weight": 1.0} -->

This theorem indicates that consistency of Algorithm 1 may hold even when the rollout length is relatively small. In Di and Lamperski the estimation of the first and second moments of multiplicative noise is decoupled, whereas here the estimate of $\lbrack{{\overset{\sim}{\Sigma}}_{A}^{\prime}{\overset{\sim}{\Sigma}}_{B}^{\prime}}\rbrack$ relies on $\lbrack{\hat{A}\hat{B}}\rbrack$. The coupling exists because here the noise covariance matrix, which from definition depends on the mean of the noise, is estimated. Note that $\ell$ is assumed to be fixed and we do not consider the case where $\ell\rightarrow\infty$, since an averaging step is used in Algorithm 1. Study of the case with increasing rollout length is left to future work.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Finite-Sample Analysis", "weight": 1.0} -->

This subsection studies finite-sample performance of Algorithm 1, demonstrating its non-asymptotic behavior. The existence of multiplicative noise complicates the analysis, so the following assumptions, ensuring that the system is bounded a.s., are introduced.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

For all rollouts indexed by $k \in {\lbrack n_{r}\rbrack}$, the following conditions hold.\
(i) The initial state is bounded a.s. for all $k \in {\lbrack n_{r}\rbrack}$ as

<!-- chunk {"id": "body-0045", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

\(ii\) The inputs are bounded a.s. for all $0 \leq t \leq {\ell - 1}$ and $k \in {\lbrack n_{r}\rbrack}$ as

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark 3.12", "weight": 1.0} -->

The assumption of bounded multiplicative noise is reasonable for physical systems, which cannot have infinite variations. For example, in interconnected systems, the noise represents randomly varying topologies of subsystems, and is naturally bounded.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Remark 3.12", "weight": 1.0} -->

Introduce the state- and input-deviation quantities

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 3.12", "weight": 1.0} -->

The next proposition is a natural consequence of Assumption 2.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Remark 3.13", "weight": 1.0} -->

This proposition captures the deviations of random components of System from their expectations. Using the bounds in Assumption 2 one could upper-bound these deviations, for instance,

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 3.13", "weight": 1.0} -->

However, these bounds may not depend on those in Assumption 2. For example, when $x_{0}^{(k)}$ is a nonzero constant, $c_{\mu} = 0$ but $c_{X}$ is positive.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 3.13", "weight": 1.0} -->

The boundedness of the states and state-deviations follows from Assumptions 1 and 2 according to the following statement.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Remark 3.15", "weight": 1.0} -->

The quantity $c_{M}$ can be interpreted as a bound on the radius from the origin to the outer boundary of the set of reachable states from any valid $x_{0}$ over $\ell$ time steps. If the system is not robustly stable in the sense that $c_{A} > 1$, then the limit as $\ell\rightarrow\infty$ of $c_{M}$ could be infinite. However, since we consider only finite-length rollouts, $c_{M}$ is finite regardless of the stability properties of the system.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Remark 3.15", "weight": 1.0} -->

Analogous interpretations follow for the quantity $c_{N}$ and the reachable state-deviations. Notice that the constants $c_{N}$ grows with increasing maximum initial state and input deviations $c_{\mu}$ and $c_{\nu}$, and maximum noise magnitudes $c_{\overline{A}}$ and $c_{\overline{B}}$. Conversely, $c_{N}$ vanishes as those quantities become smaller, i.e. in the case that the initial state $x_{0}$ is a fixed deterministic value, the inputs $u_{t}$ follow a deterministic sequence, and there is no multiplicative noise. Likewise, $c_{F}$ vanishes in such a scenario, so that $c_{\DeltaX} = c_{FX} = c_{FU} = c_{FXU} = 0$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Remark 3.15", "weight": 1.0} -->

The following theorems state finite-sample results for the estimates of $\lbrack{AB}\rbrack$ and $\lbrack{{\overset{\sim}{\Sigma}}_{A}^{\prime}{\overset{\sim}{\Sigma}}_{B}^{\prime}}\rbrack$, whose proofs are given in Appendices F and G, respectively.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Remark 3.18", "weight": 1.0} -->

In Theorems 3.16 and 3.17, high-probability upper bounds are given for the estimates of $\lbrack{AB}\rbrack$ and $\lbrack{{\overset{\sim}{\Sigma}}_{A}^{\prime}{\overset{\sim}{\Sigma}}_{B}^{\prime}}\rbrack$. It can be observed that these bounds shrink as $\mathcal{O}\left( {1/\sqrt{n_{r}}} \right)$ with the number of rollouts, and converge to zero as the number of rollouts grows to infinity, indicating the consistency of the estimators. Note that the bounds are deterministic, although they depend on the failure probability $\delta$. The theorems also indicate that the probability of the estimation error exceeding an arbitrary positive constant decays exponentially fast with the number of rollouts, which is illustrated in Section 4.1.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Remark 3.18", "weight": 1.0} -->

The $\mathcal{O}{( \cdot )}$ notation hides the coefficients of the error bounds, and the polynomial and exponential factors of $n$ and $m$ in the logarithm term. Their explicit forms are given in Appendices F and G, respectively. The coefficient of the estimation error of $\lbrack{AB}\rbrack$ increases with ${\|\mathbf{Y}\|}_{2}$, ${\|\mathbf{Z}\|}_{2}$, and the bound of the system, but decreases with the minimum eigenvalue of ${\mathbf{Z}\mathbf{Z}}^{\intercal}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark 3.18", "weight": 1.0} -->

It also increases with ${\| A\|}_{2}$, ${\| B\|}_{2}$, and quantities related to the second-moment dynamic of system states, because of the dependence of $\lbrack{{\hat{\overset{\sim}{\Sigma}}}_{A}^{\prime}{\hat{\overset{\sim}{\Sigma}}}_{B}^{\prime}}\rbrack$ on $\lbrack{\hat{A}\hat{B}}\rbrack$. From definition, $\mathbf{Y}$, $\mathbf{Z}$, $\mathbf{C}$, and $\mathbf{D}$ depend on system parameters and inputs, so proper input design could reduce the estimation error. It remains for future study how to design the moments of inputs so that the coefficients of the bounds can achieve their smallest values, and how to obtain data-dependent bounds, because the nominal system matrix is unknown.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark 3.18", "weight": 1.0} -->

In Di and Lamperski the authors study identification of System from single-trajectory data, by developing error bounds for a least-squares algorithm, but it is unclear under what conditions of System these error bounds converge to zero. In contrast, our analysis provides sufficient conditions under which the error bounds for estimates given by Algorithm 1 vanish. The results show that a relatively small rollout length is enough to guarantee consistency, but the current bounds imply that longer rollout length $\ell$ may lead to worse performance, which seems to be contrary to the intuition that longer trajectory provides more information. This could result from the averaging step which eliminates some excitation. Future work will consider how to use the data more efficiently.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Numerical Simulations", "weight": 1.0} -->

In this section we empirically validate the theoretical results for Algorithm 1, and compare its performance with the recursive least-squares algorithm based on single-trajectory data.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Consistency and Finite-Sample Result", "weight": 1.0} -->

This subsection considers identification of the $2$-dimensional system discussed in Example 3.2 with parameters

<!-- chunk {"id": "body-0061", "role": "body", "section": "Consistency and Finite-Sample Result", "weight": 1.0} -->

According to the reshaping operator $G$ defined in the notation section and the discussion in Example 3.2, it holds that

<!-- chunk {"id": "body-0062", "role": "body", "section": "Consistency and Finite-Sample Result", "weight": 1.0} -->

A simulated experiment is conducted with rollout data of length $\ell = 4$. For $0 \leq t \leq 3$, $\nu_{t}$ is generated independently from uniform distribution $\mathcal{U}{({\lbrack 0,1\rbrack})}$ and then fixed. Three types of inputs are considered: Gaussian, uniform, and deterministic inputs. An identical sequence of input covariances, independently generated from $1$-dimensional Wishart distribution $W_{p}{(0.1,1)}$ and then fixed, is used in the former two cases. For the case of deterministic inputs, the covariances are set to be zero (i.e., ${\overline{U}}_{t} = 0$).

<!-- chunk {"id": "body-0063", "role": "body", "section": "Consistency and Finite-Sample Result", "weight": 1.0} -->

In this setting ${\mathbf{D}\mathbf{D}}^{\intercal}$ can be invertible because the second moment of the input at time $t$ satisfies that $U_{t} = {{\overline{U}}_{t} + {\nu_{t}\nu_{t}^{\intercal}}}$, and the generation of $\nu_{t}$ provides randomness. For each case, Algorithm 1 is run for $50$ times. The mean of estimation error in each case is shown in Fig. 1. It can be seen that Algorithm 1 converges with convergence rate $\mathcal{O}{({1/\sqrt{n_{r}}})}$, and performs similarly under all three types of inputs. The algorithm fluctuates when the number of rollouts is small, which may result from the averaging step.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Consistency and Finite-Sample Result", "weight": 1.0} -->

From Remark 3.1 and, it follows that defines an equivalent class of covariance matrices that generates the same second-moment dynamic of system states. In the current example, $\Sigma_{B}$ is unique, but the following covariance matrix is equivalent to $\Sigma_{A}$,

<!-- chunk {"id": "body-0065", "role": "body", "section": "Consistency and Finite-Sample Result", "weight": 1.0} -->

It can be observed that the dynamics defined by $(\Sigma_{A},\Sigma_{B})$ and $({\Sigma_{A}{}},\Sigma_{B})$ are identical, and the dynamic defined by the estimates from Algorithm 1 is close to the former.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Consistency and Finite-Sample Result", "weight": 1.0} -->

It is assumed that there is no additive noise in System, but Algorithm 1 can also be applied to identifying linear systems with both multiplicative and additive noise. If additive noise $w_{t}$, independent of the inputs and the multiplicative noise, exists, then write the system as

<!-- chunk {"id": "body-0067", "role": "body", "section": "Consistency and Finite-Sample Result", "weight": 1.0} -->

In other words, $w_{t}$ can be considered as a part of multiplicative noise corresponding to a constant input equal to one. Consider the above $2$-dimensional system with Gaussian noise $w_{t} \sim {\mathcal{N}{(\mathbf{0}_{2},{\sigma^{2}I_{2}})}}$ and previously designed Gaussian inputs. Note that in this case $\ell = 6$ is needed because the dimension of inputs increases by one, compared with the original system. Fig. 4 shows the consistency of Algorithm 1 under the presence of additive noise.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Performance Comparison", "weight": 1.0} -->

The recursive form of the ordinary least-squares (OLS), namely, the recursive least-squares (RLS), is widely used in identification of dynamic systems. It is possible to apply RLS to identify System if certain conditions hold. Note that from System, we have that

<!-- chunk {"id": "body-0069", "role": "body", "section": "Performance Comparison", "weight": 1.0} -->

A mild condition for $w_{t}^{}$ to ensure convergence of RLS in literature is that ${\sup_{t}{{\mathbb{E}}{\{\left. {\| w_{t}^{}\|}^{\beta} \middle| \mathcal{F}_{t - 1} \right.\}}}} < \infty$ holds a.s. for some $\beta > 2$. However in our case $w_{t}^{}$ is state-dependent, so certain stability assumption is needed to ensure this boundedness condition. This fact means that RLS could fail if the nominal part of System is marginally stable (${\rho{(A)}} = 1$) or unstable (${\rho{(A)}} > 1$). In contrast, Algorithm 1 can handle this situation with the help of multiple-trajectory data. Similarly, the noise covariance matrix of System may be estimated using the following dynamic

<!-- chunk {"id": "body-0070", "role": "body", "section": "Performance Comparison", "weight": 1.0} -->

It can be verified that, under Assumption 1, despite state-dependent, $\{ w_{t}^{},\mathcal{F}_{t}\}$ is also a martingale difference sequence. To estimate the covariance matrix of the multiplicative noise, Di and Lamperski, apply OLS, which is equivalent to RLS. Note that, when using OLS or RLS, one estimates the second moments of $A + {\overline{A}}_{t}$ and $B + {\overline{B}}_{t}$, rather than their covariance matrices, which are $\Sigma_{A}$ and $\Sigma_{B}$ in our context.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Performance Comparison", "weight": 1.0} -->

To compare the performance of RLS and Algorithm 1, we consider four systems. In the first case, the nominal system matrices are

<!-- chunk {"id": "body-0072", "role": "body", "section": "Performance Comparison", "weight": 1.0} -->

and both $\Sigma_{A}$ and $\Sigma_{B}$ are zero matrices. That is, a linear system without noise and ${\rho{(A)}} = 0.6$, where $\rho{(A)}$ is the spectral radius of $A$. We use this case to show the consistency of RLS. In the other three cases, the matrix $A$ is set to be

<!-- chunk {"id": "body-0073", "role": "body", "section": "Performance Comparison", "weight": 1.0} -->

respectively. $B$ is the same as the first case, while $\Sigma_{A}$ and $\Sigma_{B}$ in Section 4.1 are adopted to be the covariance matrices. The implementation of Algorithm 1 is the same as in Section 4.1. That is, $\nu_{t}$ and ${\overline{U}}_{t}$ are randomly generated, and then fixed in all runs of the entire numerical experiment. The input $u_{t}$ at time $0 \leq t \leq {\ell - 1}$ in each rollout is generated from Gaussian distribution $\mathcal{N}{(\nu_{t},{\overline{U}}_{t})}$, and $\ell = 4$. Since RLS is based on single-trajectory data, the length of the trajectory is set to be $\elln_{r}$, so that the number of samples that RLS uses is the same as that of Algorithm 1. RLS with independent standard Gaussian inputs is considered as a baseline.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Performance Comparison", "weight": 1.0} -->

In order to rule out the effect of different input design, we also run RLS with periodic inputs (RLSp) satisfying that, in each period, the inputs are generated in the same way as those in a rollout of Algorithm 1.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Performance Comparison", "weight": 1.0} -->

For each system, the three algorithms, RLS, RLSp, and Algorithm 1 are run for $50$ times, respectively. The mean of estimation error in each case is presented in Fig. 5. It can be observed that RLS and RLSp perform similarly in all cases. When multiplicative noise is absent, they converge slightly faster than Algorithm 1. They are also a little better than Algorithm 1, in the case ${\rho{(A)}} = 0.6$ with noise, for the estimation of $\lbrack{AB}\rbrack$, indicating OLS could be applied to Algorithm 1 as a way to estimate $\lbrack{AB}\rbrack$. However, Algorithm 1 surpasses RLS and RLSp when identifying the noise covariance matrix. Moreover, the performance of RLS gets worse as $\rho{(A)}$ grows. Interestingly, in the case of ${\rho{(A)}} = 0.8$, although the nominal system is stable, the second-moment dynamic of system states is not.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Performance Comparison", "weight": 1.0} -->

This instability leads to degraded performance of RLS estimating $\lbrack{AB}\rbrack$ and divergence of RLS estimating the covariance matrix. In the marginally stable case, namely ${\rho{(A)}} = 1$, RLS and RLSp explode in finite time. In contrast, Algorithm 1 behaves almost identically for all cases (the consistency of Algorithm 1 in the marginally stable case is shown in Fig. 1). To sum up, Algorithm 1 can deal with the estimation of noise covariance matrix better and relies less on the stability of both the nominal system and the second-moment dynamic of system states.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In this paper an identification algorithm based on multiple-trajectory data was proposed for linear systems with multiplicative noise. With appropriately designed exciting inputs, the proposed algorithm is able to jointly estimate the nominal system and the multiplicative noise covariance. The asymptotic and non-asymptotic performance of the algorithm was analyzed theoretically, and illustrated by numerical experiments. Future work include studying more efficient algorithms that can be used in online settings, optimal and adaptive input design, sparsity-promoting regularization for identification of networked systems, end-to-end finite-sample performance guarantees for identification-based optimal control, and applications to identification of cyber-physical systems with coupling between noise and inputs.
