<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We establish a collection of closed-loop guarantees and propose a scalable optimization algorithm for distributionally robust model predictive control (DRMPC) applied to linear systems, convex constraints, and quadratic costs. Via standard assumptions for the terminal cost and constraint, we establish distribtionally robust long-term and stage-wise performance guarantees for the closed-loop system. We further demonstrate that a common choice of the terminal cost, i.e., via the discrete-algebraic Riccati equation, renders the origin input-to-state stable for the closed-loop system. This choice also ensures that the exact long-term performance of the closed-loop system is independent of the choice of ambiguity set for the DRMPC formulation. Thus, we establish conditions under which DRMPC does not provide a long-term performance benefit relative to stochastic MPC. To solve the DRMPC optimization problem, we propose a Newton-type algorithm that empirically achieves superlinear convergence and guarantees the feasibility of each iterate. We demonstrate the implications of the closed-loop guarantees and the scalability of the proposed algorithm via two examples.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

To facilitate the reproducibility of the results, we also provide open-source code to implement the proposed algorithm and generate the figures.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Model predictive control (MPC) defines an implicit control law via a finite horizon optimal control problem. This optimal control problem is defined by the stage cost $\ell{(x,u)}$, state/input constraints, and a linear discrete-time dynamical model

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

in which $x$ is the state, $u$ is the manipulated input, and $w$ is the disturbance. The primary difference between variants of MPC (e.g., nominal, robust, and stochastic MPC) is their approach to modeling the disturbance $w$ in the optimization problem.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In nominal MPC, the optimization problem uses a nominal dynamical model, i.e., $w = 0$. Nonetheless, feedback affords nominal MPC a nonzero margin of inherent robustness to disturbances. This nonzero margin, however, may be insufficient in certain safety-critical applications with high uncertainty. Robust MPC (RMPC) and stochastic MPC (SMPC) offer a potential means to improve on the inherent robustness of nominal MPC by characterizing the disturbance and including this information in the optimal control problem.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

RMPC describes the disturbance via a set $\mathbb{W}$ and requires that the state and input constraints in the optimization problem are satisfied for all possible realizations of $w \in {\mathbb{W}}$. The objective function of RMPC considers only the nominal system ($w = 0$) and these methods are sometimes called tube-based MPC if the constraint tightening is computed offline.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

SMPC includes a stochastic description of the disturbance $w \sim {\mathbb{P}}$ ($w$ is distributed according to the probability distribution $\mathbb{P}$) and defines the objective function based on the expected value of the cost function subject to this distribution. The performance of SMPC therefore depends on the disturbance distribution $\mathbb{P}$. This stochastic description of the disturbance also permits the use of so-called chance constraints. While SMPC refers to a range of methods, characterized by their use of a distribution in the optimization problem, we focus specifically on SMPC for linear systems, quadratic costs, robust constraints, and with expected value objective functions. We do not consider chance constraints. Analogous to nominal MPC, feedback affords SMPC a small margin of inherent distributional robustness, i.e., robustness to inaccuracies in the disturbance distribution. If this distribution is identified from limited data, however, there may be significant distributional uncertainty. Therefore, a distributionally robust (DR) approach to the SMPC optimization problem may provide desirable benefits in applications with high uncertainty and limited data.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Advances in distributionally robust optimization (DRO) have inspired a range of distributionally robust MPC (DRMPC) formulations. In general, these problems take the form

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

in which $x$ is the current state of the system, $\theta$ defines the control inputs for the MPC horizon (potentially as parameters in a previously defined feedback law), ${\mathbb{E}}_{\mathbb{P}}\lbrack \cdot \rbrack$ denotes the expected value with respect to the distribution $\mathbb{P}$, and $\mathcal{P}$ is the ambiguity set for the distribution $\mathbb{P}$ of the disturbances $\mathbf{w}$. The goal is to select $\theta$ to minimize the worst-case expected value of the cost function $J{( \cdot )}$ and satisfy the constraints embedded in the set $\Pi{(x)}$. Note that SMPC and RMPC are special cases of DRMPC via specific choices of $\mathcal{P}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The key feature of all MPC formulations is that the finite horizon optimal control problem in is solved with an updated state estimate at each time step, i.e., a rolling horizon approach. With this approach, DRMPC defines an implicit feedback control law $\kappa{(x)}$ and the closed-loop system

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

The performance of this controller is ultimately defined by this closed-loop system and the stage cost. In particular, we often define performance based on the expected average closed-loop stage cost at time $k \geq 1$, i.e.,

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

in which $\phi{(i)}$ is the closed-loop state trajectory defined by and $\mathbb{P}$ is the distribution for the closed-loop disturbance.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we focus on DRMPC formulations for linear systems with additive disturbances and quadratic costs. We note that there are also DRMPC formulations that consider parameteric uncertainty and piecewise affine cost functions are also considered. In both cases, the proposed DRMPC formulation solves for only a single input trajectory for all realizations of the disturbance.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

To better address the realization of uncertainty in the open-loop trajectory, RMPC/SMPC formulations typically solve for a trajectory of parameterized control policies instead of a single input trajectory. A common choice of this parameterization is the state-feedback law $u = {{Kx} + v}$ in which $K$ is the fixed feedback gain and the parameter to be optimized is $v$. Using this parameterization, several DRMPC formulations were proposed to tighten probabilistic constraints for linear systems based on different ambiguity sets. In these formulations, however, the cost function is unaltered from the corresponding SMPC formulation due to the fixed feedback gain in the control law parameterization.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

If the control law parameterization is chosen as a more flexible feedback affine policy, first proposed for MPC formulations, distributional uncertainty in the cost function is nontrivial to the DRMPC problem. Van Parys et al. propose a tractable method to solve linear quadratic control problems with unconstrained inputs and a distributionally robust chance constraint on the state. Coppens and Patrinos consider a disturbance feedback affine parameterization with conic representable ambiguity sets and demonstrate a tractable reformulation of the DRMPC problem. Mark and Liu consider a similar formulation with a simplified ambiguity set and also establish some performance guarantees for the closed-loop system. Taşkesen et al. demonstrate that for *unconstrained* linear systems, additive disturbances, and quadratic costs, a linear feedback law is optimal and can be found via a semidefinite program (SDP). Pan and Faulwasser use polynomial chaos expansion to approximate and solve the DRO problem.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

While these new formulations are interesting, there remain important questions about the efficacy of including yet another layer of uncertainty in the MPC problem. For example, what properties should DRMPC provide to the closed-loop system in ? And what conditions are required to achieve these properties? Due to the rolling horizon nature of DRMPC, distributionally robust closed-loop properties are not necessarily obtained by simply solving a DRO problem. Moreover, if SMPC has an incorrect distribution, the conditions under which DRMPC may provide closed-loop performance benefits relative to this SMPC implementation are not well understood.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

One of the main contributions of this paper is to provide greater insight into these questions. The focus is on the performance benefits and guarantees that may be obtained by considering distributional uncertainty in the cost function. Chance constraints are therefore not considered in the proposed DRMPC formulation or analysis.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

DRMPC is also limited by practical concerns related to the computational cost of solving DRO problems. While these DRMPC problems can often be reformulated as convex optimization problems, in particular SDPs, these optimization problems are often significantly more difficult to solve relative to the quadratic programs (QPs) that are ubiquitous in nominal, robust, and stochastic MPC problems.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we consider a DRMPC formulation for linear dynamical models, additive disturbances, robust (convex) constraints, and quadratic costs. This DRMPC formulation uses a Gelbrich ambiguity set with fixed first moment (zero mean) as a conservative approximation for a Wasserstein ball of the same radius. The key contributions of this work are (informally) summarized in the following two categories.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

Distributionally robust long-term performance. We establish sufficient conditions for DRMPC, in particular the terminal cost and constraint, such that the closed-loop system satisfies a distributionally robust long-term performance bound (Theorem 3.1. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms")), i.e., we define a function $C{({\mathbb{P}})}$ such that

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

for all ${\mathbb{P}} \in \mathcal{P}$. This bound is distributionally robust because it holds for all distributions ${\mathbb{P}} \in \mathcal{P}$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Introduction", "weight": 1.5} -->

Distributionally robust stage-wise performance. If the stage cost is also positive definite, we establish that the closed-loop system satisfies a distributionally robust stage-wise performance bound (Theorem 3.2. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms")), i.e., there exists $\lambda \in {}$ and ${c,\gamma} > 0$ such that

<!-- chunk {"id": "body-0024", "role": "body", "section": "Introduction", "weight": 1.5} -->

for all ${\mathbb{P}} \in \mathcal{P}$. Moreover, this result directly implies that the closed-loop system is distributionally robust, mean-squared input-to-state stable (ISS) (Corollary 3.3. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms")), i.e., the left-hand side of ‣ Item 1 ‣ 1. Introduction ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") becomes ${\mathbb{E}}_{\mathbb{P}}\left\lbrack {|{\phi{(k)}}|}^{2} \right\rbrack$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Introduction", "weight": 1.5} -->

Pathwise input-to-state stability. A common approach in MPC design is to select the terminal cost via the discrete-algebraic riccati equation (DARE) for the linear system. Under these conditions, we establish that the closed-loop system is in fact (pathwise) ISS (Theorem 3.4. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms")), a stronger property than mean-squared ISS.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Introduction", "weight": 1.5} -->

Exact long-term performance. Given this stronger property of (pathwise) ISS, we can further establish an exact value for the long-term performance of DRMPC based on this terminal cost and the closed-loop disturbance distribution (Theorem 3.5. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms")), i.e.,

<!-- chunk {"id": "body-0027", "role": "body", "section": "Introduction", "weight": 1.5} -->

for all distributions $\mathbb{P}$ supported on $\mathbb{W}$. Of particular interest is the fact that this result is independent of the choice of ambiguity set $\mathcal{P}$. Thus, the long-term performance of DRMPC, SMPC, and RMPC are equivalent for this choice of terminal cost (Corollary 3.6. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms")).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Introduction", "weight": 1.5} -->

Scalable Newton-type (NT) algorithm. We present a novel optimization algorithm tailored to solve the DRMPC problem of interest (Algorithm 1). In contrast to Frank-Wolfe (FW) algorithms previously proposed to solve DRO problems (e.g., ), the proposed algorithm solves a QP at each iteration instead of an LP. The NT algorithm achieves superlinear (potentially quadratic) convergence in numerical experiments (Figure 1) and reduces computation time by more than 50% compared to solving the DRMPC problem as an LMI optimization problem with state-of-the art solvers, i.e., MOSEK (Figure 2). The proposed NT algorithm and code to generate the figures in this paper can be found in the GitHub Repository

<!-- chunk {"id": "body-0029", "role": "body", "section": "Organization", "weight": 1.0} -->

In Section 2, we introduce the DRMPC problem formulation and associated DRO problem. In Section 3, we present the main technical results on closed-loop guarantees. In Section 4, we provide the technical proofs and supporting lemmata for these results. In Section 5, we discuss the DRO problem of interest and introduce the proposed NT algorithm. In Section 6, we study two examples to demonstrate the closed-loop properties established in Section 3 and the scalability of the proposed algorithm.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We consider the linear system with additive disturbances

<!-- chunk {"id": "body-0031", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

and terminal constraint ${\mathbb{X}}_{f} \subseteq {\mathbb{R}}^{n}$ that satisfy the following assumption throughout this paper.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Assumption 2.1 (Dynamics regularities)", "weight": 1.0} -->

Disturbance statistics: The disturbances $w$ in (6a) are zero mean random variables, independent in time, and satisfy $w \in {\mathbb{W}}$ with probability one.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Assumption 2.1 (Dynamics regularities)", "weight": 1.0} -->

Convex state-input constraints: The sets $\mathbb{U}$, $\mathbb{W}$, $\mathbb{Z}$, and ${\mathbb{X}}_{f}$ in (6b) are closed, convex, and contain the origin. The sets $\mathbb{U}$ and $\mathbb{W}$ are bounded and $\mathbb{W}$ contains the origin in its interior.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Assumption 2.1 (Dynamics regularities)", "weight": 1.0} -->

Since we are permitting input constraints and open-loop unable systems, we require a bounded support $\mathbb{W}$ for the disturbance.^11^1If we consider only open-loop stable systems and chance constraints, we can potentially included unbounded disturbances. While convex sets are not strictly required for some of the following theoretical results, they are important for efficient computation. To ensure constraint satisfaction, we use a disturbance feedback parameterization as

<!-- chunk {"id": "body-0035", "role": "body", "section": "Assumption 2.1 (Dynamics regularities)", "weight": 1.0} -->

and the constraints for this parameterization are given by

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumption 2.1 (Dynamics regularities)", "weight": 1.0} -->

That is, if ${(\mathbf{M},\mathbf{v})} \in {\Pi{(x)}}$ then the constraints in 6b are satisfied for all realizations of the disturbance trajectory $\mathbf{w} \in {\mathbb{W}}^{N}$. We also define the feasible set

<!-- chunk {"id": "body-0037", "role": "body", "section": "Assumption 2.1 (Dynamics regularities)", "weight": 1.0} -->

and note that, by definition, $\Pi{(x)}$ is nonempty for all $x \in \mathcal{X}$. To streamline notation, we define

<!-- chunk {"id": "body-0038", "role": "body", "section": "Assumption 2.2 (Positive semidefinite cost)", "weight": 1.0} -->

The matrices $Q$, $R$, and $P$ are positive semidefinite (${Q,R,P} \succeq 0$).

<!-- chunk {"id": "body-0039", "role": "body", "section": "Assumption 2.2 (Positive semidefinite cost)", "weight": 1.0} -->

If we embed the disturbance feedback parameterization in this cost function, we have from Assumption 2.2. ‣ 2. Problem Formulation ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms")

<!-- chunk {"id": "body-0040", "role": "body", "section": "Assumption 2.2 (Positive semidefinite cost)", "weight": 1.0} -->

with constant matrices $H_{x}$, $H_{u}$, and $H_{w}$. Let $\mathcal{M}{({\mathbb{W}})}$ denote all probability distributions of $w$ with zero mean and $w \in {\mathbb{W}}$ with probability one, i.e.,

<!-- chunk {"id": "body-0041", "role": "body", "section": "Assumption 2.2 (Positive semidefinite cost)", "weight": 1.0} -->

Note that $L{(x,\theta,\mathbf{\Sigma})}$ is quadratic in $\theta$ and linear in $\mathbf{\Sigma}$. In SMPC, we minimize $L{(x,\theta,\mathbf{\Sigma})}$ for a specific covariance $\mathbf{\Sigma}$ and the current state $x$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Assumption 2.2 (Positive semidefinite cost)", "weight": 1.0} -->

For DRMPC, we instead consider a worst-case version of the SMPC problem in which $\mathbb{P}$ takes the worst value within some ambiguity set. To define this ambiguity set, we first consider the Gelbrich ball for the covariance of a single disturbance $w \in {\mathbb{R}}^{q}$ centered at the nominal covariance $\hat{\Sigma} \in {\mathbb{R}}^{q \times q}$ with radius $\varepsilon \geq 0$ defined as

<!-- chunk {"id": "body-0043", "role": "body", "section": "Assumption 2.2 (Positive semidefinite cost)", "weight": 1.0} -->

We further assume that this Gelbrich ambiguity set is compatible with $\mathbb{W}$, i.e., all covariances $\Sigma \in {\mathbb{B}}_{d}$ can be achieved by at least one distribution ${\mathbb{P}} \in {\mathcal{M}{({\mathbb{W}})}}$. For example, in the extreme case that ${\mathbb{W}} = {\{ 0\}}$ then $\mathcal{M}{({\mathbb{W}})}$ contains only one distribution with all the weight at zero and the only reasonable Gelbrich ball to consider is ${\mathbb{B}}_{d} = {\{ 0\}}$. Formally, we consider only ambiguity parameters $d \in \mathcal{D}$ with

<!-- chunk {"id": "body-0044", "role": "body", "section": "Assumption 2.2 (Positive semidefinite cost)", "weight": 1.0} -->

The worst-case expected cost is defined as

<!-- chunk {"id": "body-0045", "role": "body", "section": "Assumption 2.2 (Positive semidefinite cost)", "weight": 1.0} -->

The two maximization problems in are equal because $d \in \mathcal{D}$. We now define the DRO problem for DRMPC as

<!-- chunk {"id": "body-0046", "role": "body", "section": "Assumption 2.2 (Positive semidefinite cost)", "weight": 1.0} -->

where the function $L$ in (13b) is defined, and the set $\theta_{d}^{0}{(x)}$ in (13c) denotes the solution set of the (outer) minimization of the worst-case expected loss ${V_{d}{(x,\theta)}}:={{\max_{\mathbf{\Sigma} \in {\mathbb{B}}_{d}^{N}}L}{(x,\theta,\mathbf{\Sigma})}}$. Note that SMPC ($d = {(0,\hat{\Sigma})}$) and RMPC ($d = {}$) are special cases of the optimization problem. Thus, all subsequent statements about DRMPC include SMPC and RMPC as special cases of $d \in \mathcal{D}$. Fundamental mathematical properties for this optimization problem are provided in Appendix C.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Assumption 2.2 (Positive semidefinite cost)", "weight": 1.0} -->

In Appendix C, we establish existence (but not uniqueness) of a minimizer, continuity of $V_{d}^{0}{(x)}$ w.r.t. $x \in \mathcal{X}$, and measurability of (set-valued) mapping $\theta_{d}^{0}{(x)}$ w.r.t. $x \in \mathcal{X}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Main results and key technical assumptions", "weight": 1.0} -->

The subsequent analysis uses concepts from nominal, robust, min-max, and stochastic MPC, with a particular focus on results.To establish desirable properties for the closed-loop system, we consider the following assumption for the terminal cost ${V_{f}{(x)}} = {x^{\prime}Px}$ and constraint ${\mathbb{X}}_{f}$. This assumption is also used in SMPC and RMPC analysis.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Assumption 3.1 (Terminal cost and constraint)", "weight": 1.0} -->

The matrix $P \succeq 0$ is chosen such that there exists $K_{f} \in {\mathbb{R}}^{m \times n}$ satisfying

<!-- chunk {"id": "body-0050", "role": "body", "section": "Assumption 3.1 (Terminal cost and constraint)", "weight": 1.0} -->

Verifying Assumption 3.1. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") is tantamount to finding a stabilizing linear control law $u = {K_{f}x}$, i.e., $A + {BK_{f}}$ is Schur stable, that satisfies the required constraints ${(x,{K_{f}x})} \in {\mathbb{Z}}$ within some robustly positive invariant neighborhood of the origin ${\mathbb{X}}_{f}$. With this stabilizing linear control law, we can then construct an appropriate terminal cost matrix $P$, e.g., solving a discrete time Lyapunov equation.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Assumption 3.1 (Terminal cost and constraint)", "weight": 1.0} -->

With this assumption, we can guarantee that the feasible set $\mathcal{X}$ is RPI and establish the following distributionally robust long-term performance guarantee. This performance guarantee is a distributionally robust version of the stochastic performance guarantee typically derived for SMPC (e.g., ).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Assumption 3.2 (Positive definite stage cost)", "weight": 1.0} -->

The matrix $Q$ is positive definite, i.e., $Q \succ 0$. Moreover, the feasible set $\mathcal{X}$ is bounded or ${\mathbb{X}}_{f} = {\mathbb{R}}^{n}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Assumption 3.2 (Positive definite stage cost)", "weight": 1.0} -->

By also including Assumption 3.2. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms"), we can establish a distributionally robust stage-wise performance guarantee.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Assumption 3.3 (DARE terminal cost)", "weight": 1.0} -->

The matrices $R$ and $P$ are positive definite (${R,P} \succ 0$) and we have

<!-- chunk {"id": "body-0055", "role": "body", "section": "Assumption 3.3 (DARE terminal cost)", "weight": 1.0} -->

With this stronger assumption, we can establish significantly stronger properties for the DRMPC controller, similar to results for SMPC reported in \[, Lemma 4.18\]. In particular, we can establish that the closed-loop system is (pathwise) ISS.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Remark 3.1 (Detectable stage cost)", "weight": 1.0} -->

We can also weaken Assumption 3.2. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") to $Q \succeq 0$ and $(A,Q^{1/2})$ detectable. By defining an input-output-to-state stability (IOSS) Lyapunov function we can apply the same approach used for nominal MPC, e.g., \[, Thm. 2.24\], to establish Theorems 3.2. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms"), 3.3. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms"), 3.4. ‣ 3.2. Main results and key technical assumptions ‣ 3.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark 3.1 (Detectable stage cost)", "weight": 1.0} -->

Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms"), 3.5. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") and 3.6. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") for DRMPC under this weaker restriction for $Q$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Distributionally robust long-term performance", "weight": 1.0} -->

To establish Theorem 3.1. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms"), we begin by establishing that feasible set $\mathcal{X}$ is RPI and providing a distributionally robust expected cost decrease condition.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Remark 4.1 (Key distinction from SMPC analysis)", "weight": 1.0} -->

In the proof of Lemma 4.1. ‣ 4.1. Distributionally robust long-term performance ‣ 4. Closed-loop guarantees: Technical proofs ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms"), we show that for the candidate solution the worst case covariance, defined as $\mathbf{\Sigma}^{+}$, is independent of $w{}$. This independence is essential to establish Lemma 4.1. ‣ 4.1. Distributionally robust long-term performance ‣ 4. Closed-loop guarantees: Technical proofs ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") and is derived from the affine control law parameterization. As such, these results may not hold for other (nonlinear) control law parameterizations.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Remark 4.1 (Key distinction from SMPC analysis)", "weight": 1.0} -->

We can then apply Lemma 4.1. ‣ 4.1. Distributionally robust long-term performance ‣ 4. Closed-loop guarantees: Technical proofs ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") to prove Theorem 3.1. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms").

<!-- chunk {"id": "body-0061", "role": "body", "section": "Distributionally robust stage-wise performance", "weight": 1.0} -->

To establish Theorem 3.2. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms"), we first establish the following upper bound for the optimal cost function.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Pathwise input-to-state stability", "weight": 1.0} -->

To establish Theorem 3.4. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms"), we first establish the following interesting property for the DRMPC control law within the terminal region ${\mathbb{X}}_{f}$, similar to \[, Lemma 4.18\].

<!-- chunk {"id": "body-0063", "role": "body", "section": "Exact long-term performance", "weight": 1.0} -->

For the class of disturbances in $\mathcal{Q}$, Munoz-Carpintero and Cannon established that ISS systems converge to the minimal RPI set for the system with probability one. By Assumption 3.3. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms"), the terminal set must contain the minimal RPI set for the system. Thus, we have the following result adapted from \[, Thm. 5\].

<!-- chunk {"id": "body-0064", "role": "body", "section": "Scalable algorithms", "weight": 1.0} -->

We assume for the subsequent discussion that $\varepsilon > 0$ and $\theta$ is in a vectorized form, i.e., $\mathbf{M}$ is converted to a vector. We first present an exact reformulation of the DRO problem in and then describe the proposed NT algorithm. The Frank-Wolfe algorithm and additional details regarding the step-size are provided in Appendix D.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Exact reformulation", "weight": 1.0} -->

Using existing results in \[, Prop. 2.8\] and \[, Thm. 16\], we provide an exact reformulation of via linear matrix inequalities (LMIs) to serve as a baseline for the NT algorithm.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 5.1 (Saddle point)", "weight": 1.0} -->

The set of saddle points $(\theta^{\ast},\mathbf{\Sigma}^{\ast})$ for the min-max problem 13b is non-empty and compact for any $x \in \mathcal{X}$ and $d \in \mathcal{D}$. This fact is a classical result for the convex-concave function $L{(x, \cdot )}$ ensured by the convexity and compactness of $\Pi{(x)}$ (Lemma 2.1. ‣ 2. Problem Formulation ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms")) and ${\mathbb{B}}_{d}^{N}$ \[, Lemma A.6\], see for instance \[, Prop. 5.5.7\].

<!-- chunk {"id": "body-0067", "role": "body", "section": "Newton-type saddle point algorithm", "weight": 1.0} -->

We introduce a new algorithm that exploits the structure of the min-max problem (13b) through a Newton-type step. Additional information regarding the stepsize is provided in Appendix D. Code to implement this algorithm is available in the GitHub repository

<!-- chunk {"id": "body-0068", "role": "body", "section": "Newton-type saddle point algorithm", "weight": 1.0} -->

We subsequently assume that $\hat{\Sigma} \succ 0$. For notational simplicity, given any (fixed) $x \in \mathcal{X}$ and $d \in \mathcal{D}$, we use the shorthand notation for the constraint $\theta \in \Pi:={\Pi{(x)}}$ and objective function ${L_{x}{( \cdot )}} = {L{(x, \cdot )}}$ in to rewrite the min-max (13b) concisely as

<!-- chunk {"id": "body-0069", "role": "body", "section": "Newton-type saddle point algorithm", "weight": 1.0} -->

The structure of the set ${\mathbb{B}}_{d}^{N}$ in allows us to expand as

<!-- chunk {"id": "body-0070", "role": "body", "section": "Newton-type saddle point algorithm", "weight": 1.0} -->

where the matrix ${Z_{k}{(\theta)}} \in {\mathbb{R}}^{q \times q}$ is the $k$^th^ block diagonal of ${({{H_{u}\mathbf{M}} + H_{w}})}^{\prime}{({{H_{u}\mathbf{M}} + H_{w}})}$. Each maximization in can be solved in finite time using a bisection algorithm detailed in \[, Alg. 2, Thm. 6.4\]. Hence, we have access to

<!-- chunk {"id": "body-0071", "role": "body", "section": "Newton-type saddle point algorithm", "weight": 1.0} -->

Since the solution to is unique for $\hat{\Sigma} \succ 0$ \[, Prop. A.2\], we have from Danskin's theorem that $f{(\theta)}$ is convex and ${{\nabla f}{(\theta)}} = {{\nabla_{\theta}L_{x}}{(\theta,{\mathbf{\Sigma}^{0}{(\theta)}})}}$, i.e., the gradient of $f$ at $\theta$ is given by the gradient of $L_{x}{( \cdot )}$ with respect to $\theta$, evaluated at $(\theta,{\mathbf{\Sigma}^{0}{(\theta)}})$. Frank-Wolfe (FW) algorithms that exploit this property of the min-max program in have shown promising results for DRO problems (e.g., ).

<!-- chunk {"id": "body-0072", "role": "body", "section": "Newton-type saddle point algorithm", "weight": 1.0} -->

However, FW algorithms are often limited to sublinear convergence rates for MPC optimization problems (see Figure 1 in the numerical section) because the constraint set $\Pi$ is not strongly convex (e.g., polytope) and the minimizer is frequently on the boundary of $\Pi$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Newton-type saddle point algorithm", "weight": 1.0} -->

With the above approximation, at each iteration we solve

<!-- chunk {"id": "body-0074", "role": "body", "section": "Newton-type saddle point algorithm", "weight": 1.0} -->

When $\Pi$ is a polytope, the oracle is a QP. Recall that our objective function $L_{x}$ in (originally defined in ) is a quadratic function in $\theta$, and therefore ${F{(\theta)}} = {{\arg{\min_{\vartheta \in \Pi}L_{x}}}{(\vartheta,{\mathbf{\Sigma}^{\ast}{(\theta)}})}}$. The solution in defines the search direction for the iteration through the update rule

<!-- chunk {"id": "body-0075", "role": "body", "section": "Newton-type saddle point algorithm", "weight": 1.0} -->

in which the stepsize $\eta_{t}$ is chosen according to either the adaptive or fully adaptive step-size rules determined by

<!-- chunk {"id": "body-0076", "role": "body", "section": "Newton-type saddle point algorithm", "weight": 1.0} -->

The parameter $\beta$ in is a conservative estimate of the *global* smoothness parameter for the function $f$. The fully adaptive stepsize, first proposed, instead determines a local value of $\beta$ via backtracking line search and a quadratic sufficient decrease condition. In Algorithm 1, we summarize the NT algorithm with fully adaptive stepsize in pseudocode.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Newton-type saddle point algorithm", "weight": 1.0} -->

Input: Initial θ0 ∈ Π, smoothness parameter β−1 &gt; 0, line search parameters ζ, τ &gt; 1
while stopping criterion not met do
solve ${\overset{\sim}{\theta}}_{t} = {F{(\theta_{t})}}$
set $d_{t}\leftarrow{{\overset{\sim}{\theta}}_{t} - \theta_{t}}$ and gt ← −dt′∇f(θt)
set βt ← βt − 1/ζ and ηt ← min {1, gt/(βt|dt|2)}
set βt ← τβt and ηt ← min {1, gt/(βt|dt|2)}
Algorithm 1 NT algorithm (fully adaptive stepsize)

<!-- chunk {"id": "body-0078", "role": "body", "section": "Numerical Examples", "weight": 1.0} -->

We present two examples. The first is a small-scale (2 state) example that is used to demonstrate the closed-loop performance guarantees presented in Section 3 and investigate the computational performance of the proposed NT algorithm. The second is a large-scale (20 state) example, based on the Shell oil fractionator case study in Maciejowski \[, s. 9.1\], that is used to demonstrate the scalability of the proposed NT algorithm. All optimization problems (LP, QP, or LMI) are solved with MOSEK with default parameter settings. Code to generate all figures for the small-scale example is available in the GitHub repository

<!-- chunk {"id": "body-0079", "role": "body", "section": "Small-scale example", "weight": 1.0} -->

We consider a two-state, two-input system in which

<!-- chunk {"id": "body-0080", "role": "body", "section": "Small-scale example", "weight": 1.0} -->

and $\varepsilon = 0.1$ for DRMPC. We choose

<!-- chunk {"id": "body-0081", "role": "body", "section": "Small-scale example", "weight": 1.0} -->

and define $P \succ 0$ as the solution to the the Lyapunov equation for this system with $u = 0$, i.e., $P \succ 0$ satisfies ${{A^{\prime}PA} - P} = {- Q}$. This DRMPC formulation satisfies Assumptions 2.1. ‣ 2. Problem Formulation ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms"), 2.2. ‣ 2. Problem Formulation ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms"), 3.1. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") and 3.2. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms"), but not Assumption 3.3. ‣ 3.2. Main results and key technical assumptions ‣ 3.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Small-scale example", "weight": 1.0} -->

Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms"). Recall from Corollary 3.6. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") that DRMPC formulations that satisfy Assumption 3.3. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") will produce the same long-term performance as SMPC even if SMPC has an incorrect disturbance distribution.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Computational performance", "weight": 1.0} -->

We solve the DRMPC problem for this formulation using three different methods: 1) the LMI optimization problem. ‣ 5.1. Exact reformulation ‣ 5. Scalable algorithms ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") with MOSEK, 2) the FW algorithm, and 3) the proposed NT algorithm in Algorithm 1. To compare these algorithms, we use a fixed initial condition of $x_{0} = \begin{bmatrix}
\end{bmatrix}^{\prime}$ and horizon length $N = 10$. We plot the convergence rate in terms of suboptimality gap (${f{(\theta_{t})}} - f^{\ast}$) for the FW and NT algorithms in Figure 1. For this suboptimality gap, we determine $f^{\ast}$ via the LMI optimization problem. ‣ 5.1. Exact reformulation ‣ 5. Scalable algorithms ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms").

<!-- chunk {"id": "body-0084", "role": "body", "section": "Computational performance", "weight": 1.0} -->

For both FW and NT algorithms, we consider the adaptive (A) and fully adaptive (FA) step-size rules. We terminate when the duality gap is less than $10^{- 6}$.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Computational performance", "weight": 1.0} -->

First, we discuss the per-iteration convergence rate shown in the top of Figure 1. For the FW algorithm, the convergence rate is *sublinear* for both step-size rules and does not converge within $10^{3}$ iterations. By contrast, the NT algorithm appears to obtain a *superlinear* (perhaps quadratic) convergence rate near the optimal solution. This behavior is also observed for all other values of the initial condition and horizon length investigated. In fact, the fully adaptive NT algorithm typically converges in fewer than $5$ iterations. The significant improvement in per-iteration convergence rate ensures that the NT algorithm requires less computation time than FW despite solving a QP at each iteration (bottom plot of Figure 1).

<!-- chunk {"id": "body-0086", "role": "body", "section": "Computational performance", "weight": 1.0} -->

In Figure 2, we compare the computation times required to solve the small scale DRMPC problem for difference horizon lengths $N$ via 1) the LMI optimization problem. ‣ 5.1. Exact reformulation ‣ 5. Scalable algorithms ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") with MOSEK and 2) the NT algorithm. For $N \leq 5$, and therefore fewer variables and constraints, solving the DRMPC problem as an LMI optimization problem is faster. For $N > 5$, however, the NT algorithm is faster than the LMI formulation. For $N \geq 15$, the computation time to solve the DRMPC problem as an LMI optimization problem is more than twice the computation time required for the NT algorithm.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Closed-loop Performance", "weight": 1.0} -->

We initialize the state at ${x{}} = \begin{bmatrix}
\end{bmatrix}^{\prime}$ and use $N = 10$. In the following discussion, we consider three different controllers: DRMPC with $d = {(\varepsilon,\hat{\Sigma})}$, SMPC with $d = {(0,\hat{\Sigma})}$, and RMPC with $d = {}$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Closed-loop Performance", "weight": 1.0} -->

To demonstrate some differences between DRMPC, SMPC, and RMPC, we plot the first element of closed-loop state trajectory assuming the disturbance is zero, i.e., $w = 0$, in Figure 3. RMPC drives the closed-loop state to the origin. SMPC, however, does not drive the closed-loop state to the origin even though the disturbance is zero. Since $u_{2} \geq 0$, the SMPC controller keeps $x_{1}$ slightly below the origin to mitigate the effect of positive values for $w_{2}$. The amount of offset is determined by the covariance of the disturbance. Since DRMPC considers a worst-case covariance for the disturbances, the offset is larger. Thus, for ${\|\mathbf{w}_{\infty}\|} = 0$, the closed-loop state for DRMPC (SMPC) does not converge to the origin. The origin is therefore not ISS for DRMPC (SMPC), despite satisfying Assumptions 2.1. ‣ 2.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Closed-loop Performance", "weight": 1.0} -->

Problem Formulation ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms"), 2.2. ‣ 2. Problem Formulation ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms"), 3.1. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") and 3.2. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms"). By contrast, these assumptions render the origin ISS for the closed-loop system generated by RMPC \[, Thm. 23\]. To summarize: SMPC and DRMPC are hedging against uncertainty and thereby giving up the deterministic properties of RMPC, such as ISS, in the pursuit of improved performance in terms of the expected value of the stage cost, i.e., $\mathcal{J}_{k}{( \cdot )}$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Closed-loop Performance", "weight": 1.0} -->

We now investigate the performance of DRMPC relative to SMPC/RMPC for a distribution ${\mathbb{P}} \in \mathcal{P}_{d}^{\infty}$. Specifically, we consider $w{(k)}$ to be i.i.d. in time and defined as ${w{(k)}} = {\Sigma^{1/2}\omega{(k)}}$, in which ${\omega_{1}{(k)}},{\omega_{1}{(k)}}$ are independently sampled from a uniform distribution between $\lbrack{- \sqrt{3}},\sqrt{3}\rbrack$ and

<!-- chunk {"id": "body-0091", "role": "body", "section": "Closed-loop Performance", "weight": 1.0} -->

Thus, ${w{(k)}} \in {\mathbb{W}}$, is zero mean, and has a covariance of $\Sigma$. Note that the covariance $\hat{\Sigma}$ used in the SMPC formulation is different than the covariance of the disturbance encountered in the closed-loop system, i.e., $\hat{\Sigma} \neq \Sigma$.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Closed-loop Performance", "weight": 1.0} -->

We simulate $S = 100$ different realizations of the disturbance trajectory for each controller. For each simulation $s \in {\{ 1,\ldots,S\}}$, we define the closed-loop state and input trajectory $x^{s}{(k)}$ and $u^{s}{(k)}$, as well as the time-average cost

<!-- chunk {"id": "body-0093", "role": "body", "section": "Closed-loop Performance", "weight": 1.0} -->

In accordance with the results in Theorems 3.1. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") and 3.3. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms"), we consider the sample average approximations of ${\mathbb{E}}_{\mathbb{P}}\left\lbrack {|{\phi{(k;x,\mathbf{w}_{\infty})}}|} \right\rbrack$ and $\mathcal{J}_{k}{(x,d,{\mathbb{P}})}$ defined as

<!-- chunk {"id": "body-0094", "role": "body", "section": "Closed-loop Performance", "weight": 1.0} -->

In Figure 4, we plot ${\overset{\sim}{\mathbb{E}}}_{\mathbb{P}}\left\lbrack {|{x{(k)}}|}^{2} \right\rbrack$ and ${\overset{\sim}{\mathcal{J}}}_{k}$. For each algorithm, we observe an initial, exponential decay in the mean-squared distance ${\overset{\sim}{\mathbb{E}}}_{\mathbb{P}}\left\lbrack {|{x{(k)}}|}^{2} \right\rbrack$ towards a constant, but nonzero, value. These results for DRMPC are consistent with Corollary 3.3. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms").

<!-- chunk {"id": "body-0095", "role": "body", "section": "Closed-loop Performance", "weight": 1.0} -->

We note, however, that DRMPC produces the largest value of $\overset{\sim}{\mathbb{E}}{\lbrack{|{x{(k)}}|}^{2}\rbrack}$, i.e., the mean-squared distance between the closed-loop state and the setpoint is larger for DRMPC than for SMPC or RMPC. While this result may initially seem counter-intuitive, the objective prescribed to the DRMPC problem is to minimize the expected value of the stage cost, not the expected distance to the origin. In terms of the expected value of the stage cost, i.e., ${\overset{\sim}{\mathcal{J}}}_{k}$, the performance of DRMPC is better than SMPC, which is better than RMPC. This difference becomes more pronounced as $k\rightarrow\infty$.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Closed-loop Performance", "weight": 1.0} -->

We note that $\Sigma \in {\mathbb{B}}_{d}$ in this example is intentionally chosen to exacerbate the effect of the disturbance on $x_{2}$ and thereby increase the cost of the closed-loop trajectory, i.e., a worst-case distribution. Therefore, DRMPC produces a superior control law relative to SMPC. If the ambiguity set, however, becomes too large relative to this value of $\Sigma$, the additional conservatism of DRMPC can produce worse performance than SMPC in terms of ${\overset{\sim}{\mathcal{J}}}_{k}$ for a fixed value of $\Sigma$. To demonstrate this tradeoff, we consider the same closed-loop simulation and plot the value of ${\overset{\sim}{\mathcal{J}}}_{T}$ at $T = 500$ for various values of $\varepsilon$ and fixed $\hat{\Sigma}$.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Closed-loop Performance", "weight": 1.0} -->

In Figure 5, we observe that $\varepsilon \approx 0.11$ achieves the minimum value of $\mathcal{J}_{T}$, with an approximately 13% decrease in the value of ${\overset{\sim}{\mathcal{J}}}_{T}$ compared to $\varepsilon = 0.01$. For values of $\varepsilon > 0.11$, the value of ${\overset{\sim}{\mathcal{J}}}_{T}$ increases significantly until leveling off around $\varepsilon = 1$. For large values of $\varepsilon$, DRMPC is too conservative because $\Sigma$ is now well within the interior of ${\mathbb{B}}_{d}$.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Closed-loop Performance", "weight": 1.0} -->

Another interesting feature in Figure 5 is that the range of values for $\mathcal{J}_{T}^{s}$ for each $s \in {\{ 1,\ldots,30\}}$, shown by the shaded region, decreases as $\varepsilon$ increases. This behavior might also be explained by the increased conservatism of DRMPC as $\varepsilon$ increases. As the value of $\varepsilon$ increase, we might expect DRMPC to drive the closed-loop system to an operating region that attenuates the effect of all disturbances on the closed-loop cost at the expense of nominal performance. Thus, the closed-loop system becomes less sensitive to disturbances and thereby decreases the variability in performance at the expense of an increase in average performance. In summary, we are left with the classic trade-off in robust controller design; If we choose $\varepsilon$ too large, the excessively conservative DRMPC may perform worse than SMPC ($\varepsilon = 0$) even if the disturbance distribution used for SMPC is incorrect.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Closed-loop Performance", "weight": 1.0} -->

Thus, the design goal for DRMPC is to select a value of $\varepsilon$ that balances these two extremes.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Large scale example: Shell oil fractionator", "weight": 1.0} -->

To demonstrate the applicability of the Newton-type algorithm to control problems of an industrially relevant size, we now consider the Shell oil fractionator example in Maciejowski \[, s. 9.1\] with $n = 20$ states, $m = 3$ inputs, and $p = 3$ outputs. We include two disturbances ($q = 2$): the intermediate reflux duty and the upper reflux duty.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Large scale example: Shell oil fractionator", "weight": 1.0} -->

The outputs $y$ satisfy $y = {Cx}$ and we define cost matrices as $Q = {C^{\prime}Q_{y}C}$ and $R = {0.1I_{3}}$ in which $Q_{y} = {\text{diag}{({\lbrack 20,10,1\rbrack})}}$. We then define the terminal cost matrix $P \succ 0$ as the solution to the Lyapunov equation ${{A^{\prime}PA} - P} = {- Q}$ because $A$ is Schur stable. This DRMPC problem formulation satisfies Assumptions 2.1. ‣ 2. Problem Formulation ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms"), 2.2. ‣ 2. Problem Formulation ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") and 3.1. ‣ 3.2. Main results and key technical assumptions ‣ 3.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Large scale example: Shell oil fractionator", "weight": 1.0} -->

Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") and $(A,Q^{1/2})$ is detectable (See Remark 3.1. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms")). However, this formulation does not satisfy Assumption 3.3. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") so the performance of DRMPC and SMPC may differ (see Corollary 3.6. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms")).

<!-- chunk {"id": "body-0103", "role": "body", "section": "Large scale example: Shell oil fractionator", "weight": 1.0} -->

We initialize the state at ${x{}} = 0$ and use $N = 10$. We consider the performance of the closed-loop system in which $w{(k)}$ is sampled from a zero-mean uniform distribution with a covariance of $\Sigma = {\text{diag}{({\lbrack 0.04,0.01\rbrack})}}$. Note that $\Sigma \in {\mathbb{B}}_{d}$ but $\Sigma \neq \hat{\Sigma}$. We simulate $T = 500$ time steps for $S = 30$ realizations of the disturbance trajectory. We plot ${\overset{\sim}{\mathcal{J}}}_{k}$ in Figure 6 for DRMPC, SMPC, and RMPC. At $T = 500$, we observe an almost negligible 0.2% decrease in ${\overset{\sim}{\mathcal{J}}}_{T}$ for DRMPC relative to SMPC.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Large scale example: Shell oil fractionator", "weight": 1.0} -->

The standard deviation of the closed-loop performance is also nearly identical for all three controllers. Longer horizons may increase this difference, but we expect the overall benefit of DRMPC to remain small and therefore not worth the extra computation.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Summary and comparison", "weight": 1.0} -->

In Table 1, we summarize some key observations from the theoretical analysis, algorithm development, and numerical examples covered in this work if Assumption 3.1. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") holds, but Assumption 3.3. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") does not hold. If Assumption 3.3. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms") also holds, then SMPC and DRMPC guarantee ISS (Theorem 3.4. ‣ 3.2. Main results and key technical assumptions ‣ 3.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Summary and comparison", "weight": 1.0} -->

Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms")) but only transient performance benefits are achievable regardless of the value of $\Sigma$ and $\hat{\Sigma}$ (Corollary 3.6. ‣ 3.2. Main results and key technical assumptions ‣ 3. Closed-loop guarantees: Main results ‣ Distributionally Robust Model Predictive Control: Closed-loop Guarantees and Scalable Algorithms")). The key characteristics of a control problem that may justify the extra computational expense of DRMPC are: the covariance of the disturbance is large, but not well known, the origin (target steady-state) is near input/state constraints, and performance in terms of stage cost is more important than ISS.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Summary and comparison", "weight": 1.0} -->

Σ is large, Σ̂ is poor estimate of Σ
SDP (several QPs)

<!-- chunk {"id": "body-0108", "role": "body", "section": "Summary and comparison", "weight": 1.0} -->

Table 1. Comparison between R/S/DRMPC with Assumption 3.1.
