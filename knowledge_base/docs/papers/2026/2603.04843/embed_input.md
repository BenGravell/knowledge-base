<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Policy Optimization of Mixed H2/H-infinity Control: Benign Nonconvexity and Global Optimality

Topics include Convex optimization, Nonconvex optimization, Policy iteration, Robustness, Optimization, Control, Policy optimization, Mixed H2/H-infinity control, ECL.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Mixed H2/H-infinity control balances performance and robustness by minimizing an H2 cost bound subject to an H-infinity constraint. However, classical Riccati/LMI solutions offer limited insight into the nonconvex optimization landscape and do not readily scale to large-scale or data-driven settings. In this paper, we revisit mixed H2/H-infinity control from a modern policy optimization viewpoint, including the general two-channel and single-channel cases. One central result is that both cases enjoy a benign nonconvex structure: every stationary point is globally optimal. We characterize the H-infinity-constrained feasible set, which is open, path-connected, with boundary given exactly by policies saturating the H-infinity constraint. We also show that the mixed objective is real analytic in the interior with explicit gradient formulas. Our key analysis builds on an Extended Convex Lifting (ECL) framework that bridges nonconvex policy optimization and convex reformulations. The ECL constructions rely on non-strict Riccati inequalities that allow us to characterize global optimality.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

These insights reveal hidden convexity in mixed H2/H-infinity control and facilitate the design of scalable policy iteration methods in large-scale settings.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Performance and robustness are two central objectives in control design: $\mathcal{H}_{2}$ control optimizes average performance, whereas $\mathcal{H}_{\infty}$ control guarantees safety against worst-case scenarios. Mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control provides a principled framework to balance the two, leading to a variety of formulations studied across decades. A particularly influential formulation designs a stabilizing controller that minimizes an $\mathcal{H}_{2}$ cost bound subject to an $\mathcal{H}_{\infty}$ constraint. Classical solutions based on coupled Riccati equations or linear matrix inequalities (LMIs) are well established, but they provide little understanding of the underlying optimization landscape. Moreover, these methods are inherently model-based and scale poorly with system dimension, limiting their applicability in large-scale or data-driven settings.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, policy optimization has emerged as a promising alternative for controller design, inspired by the success of reinforcement learning in sequential decision-making and continuous control tasks. Despite the nonconvexity of policy spaces, recent studies have revealed benign landscapes in various control problems such as stabilization, linear quadratic regulation (LQR), linear quadratic Gaussian (LQG) \[39 control"), 48 control"), 7\], and dynamic filtering. For these control problems, stationary points can be globally optimal, and gradient-based methods can achieve global convergence under mild assumptions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A key insight behind these benign landscape results is that many nonconvex control problems can be reformulated as convex ones via appropriate changes of variables. In particular, LMI-based synthesis methods, despite involving auxiliary Lyapunov variables, provide a lens for analyzing the geometry of policy optimization \[37, 30, 39 control"), 13, 42, 16\]. This perspective has been formalized in the Extended Convex Lifting ($\mathtt{E}\mathtt{C}\mathtt{L}$) framework, which systematically bridges classical convex reformulations and modern nonconvex policy optimization. The $\mathtt{E}\mathtt{C}\mathtt{L}$ framework is broadly applicable, encompassing state-feedback and output-feedback $\mathcal{H}_{2}$ and $\mathcal{H}_{\infty}$ control as well as distributed control.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we revisit the classical mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control design from a modern policy optimization perspective. Building on the classical formulations of, we analyze both the general two-channel case and its single-channel specialization, and provide a systematic study of the associated nonconvex optimization landscapes. Our results reveal hidden convexity and establish the absence of spurious stationary points. Beyond new theoretical insights into nonconvex optimization in modern control, these results will facilitate the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design in large-scale and/or model-free data-driven settings.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Our contributions", "weight": 1.0} -->

This paper presents a systematic study of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ state-feedback control through the lens of modern nonconvex optimization.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Basic landscape properties. We analyze the geometry of the nonconvex feasible set. It is known that this set is open and path-connected (Lemma 2). We further precisely characterize its boundary as the set of policies that exactly saturate the $\mathcal{H}_{\infty}$ constraint (Theorem 1 and Corollary 1). We also examine the landscape of the mixed cost function. This cost function is real analytic in the interior, and continuous on the closure of its domain (Theorem 2 and Lemma 3). Thus, the mixed cost function is smooth, and we provide its explicit gradient formulas (Lemmas 4 and 5). These results underpin our analysis of stationarity, global optimality, and solvability of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Global optimality of stationary points. We investigate the global optimality of the two-channel mixed control. This includes the single-channel setting in as a special case. Despite its nonconvexity, we establish that no spurious stationary points exist (Theorem 3). This property, along with the gradient expressions, recovers the classical optimality conditions (Corollaries 2 and 3). We further analyze existence and uniqueness, showing that the single-channel case always admits a unique stationary point (Theorem 4.5), whereas the two-channel case may not (Fact 1). Nevertheless, we prove that a stationary point exists when the robustness constraint is sufficiently relaxed (Theorem 4.4).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Our contributions", "weight": 1.0} -->

Analysis techniques via $\mathtt{E}\mathtt{C}\mathtt{L}$. We explicitly construct an extended convex lifting ($\mathtt{E}\mathtt{C}\mathtt{L}$) for the two-channel mixed control (Theorem 5.13). While relying on classical LMI techniques, our convex lifting construction is non-trivial since we need to employ non-strict Riccati inequalities and LMIs, in contrast to classical suboptimal controller synthesis based on strict inequalities. This key distinction enables the $\mathtt{E}\mathtt{C}\mathtt{L}$ framework to certify the global optimality of stationary points over the entire feasible set. Moreover, the resulting convex reformulation (Theorem 5.16) not only preserves the optimal value of the original nonconvex problem, but also guarantees solvability when incorporating boundary policies (Proposition 5.17).

<!-- chunk {"id": "body-0012", "role": "body", "section": "Paper outline", "weight": 1.0} -->

Notations. We denote the set of $k \times k$ real symmetric matrices by ${\mathbb{S}}^{k}$. For ${M_{1},M_{2}} \in {\mathbb{S}}^{k}$, we write $M_{1} \prec {{( \preceq )}M_{2}}$ and $M_{2} \succ {{( \succeq )}M_{1}}$ if $M_{2} - M_{1}$ is positive (semi)definite. The Frobenius norm for matrices is denoted by $\parallel \cdot \parallel$. We use $I_{n}$ and $0_{m \times n}$ for the $n \times n$ identity and $m \times n$ zero matrices, respectively, omitting their subscripts when clear. For a subset $S$ of a topological space, ${int}{(S)}$ denote its interior and ${cl}{(S)}$ its closure.

<!-- chunk {"id": "body-0013", "role": "body", "section": "System dynamics and robustness", "weight": 1.0} -->

Consider the continuous-time linear dynamical system

<!-- chunk {"id": "body-0014", "role": "body", "section": "System dynamics and robustness", "weight": 1.0} -->

One may also consider a mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design

<!-- chunk {"id": "body-0015", "role": "body", "section": "System dynamics and robustness", "weight": 1.0} -->

where $\beta$ is a prescribed bound. Here, the $\mathcal{H}_{2}$ channel captures nominal performance, while the $\mathcal{H}_{\infty}$ channel enforces system robustness. It is worth noting that these two channels may be distinct or identical. We define the feasible set of $\mathcal{H}_{\infty}$-constrained stabilizing policies as

<!-- chunk {"id": "body-0016", "role": "body", "section": "System dynamics and robustness", "weight": 1.0} -->

Note that a strict $\mathcal{H}_{\infty}$ bound is commonly used to ensure a well-defined stabilizing Riccati solution.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Policy optimization for mixed $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ design", "weight": 1.0} -->

Despite simple formulation, problem is challenging to solve. A classical approach from is to minimize an upper bound on the $\mathcal{H}_{2}$ cost over the feasible set $\mathcal{K}_{\beta}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Policy optimization for mixed $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ design", "weight": 1.0} -->

To enforce the $\mathcal{H}_{\infty}$ constraint, we instead consider the stabilizing solution $X_{K}$ to the Riccati equation

<!-- chunk {"id": "body-0019", "role": "body", "section": "Policy optimization for mixed $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ design", "weight": 1.0} -->

where $S_{K}:={Q_{\infty} + {K^{\mathsf{T}}R_{\infty}K}}$. By the bounded real lemma (see Lemma 1. ‣ 3.1 Geometry of the ℋ_∞ constrained domain ‣ 3 Basic Landscape Properties ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality")), a policy $K \in \mathcal{K}_{\beta}$ if and only if admits a unique stabilizing solution $X_{K} \succeq 0$ such that the matrix $A_{K} + {\beta^{- 2}X_{K}S_{K}}$ is Hurwitz. Subtracting from gives

<!-- chunk {"id": "body-0020", "role": "body", "section": "Policy optimization for mixed $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ design", "weight": 1.0} -->

where $X_{K}$ is the unique stabilizing solution to.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Policy optimization for mixed $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ design", "weight": 1.0} -->

In sum, we consider the following mixed design

<!-- chunk {"id": "body-0022", "role": "body", "section": "Policy optimization for mixed $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ design", "weight": 1.0} -->

Unlike the $\mathcal{H}_{2}$ cost, $J_{mix}$ is evaluated using the Riccati solution $X_{K}$ from rather than the Lyapunov solution ${\hat{X}}_{K}$. Since the cost and constraint in are in general defined by distinct signals $z_{2}$ and $z_{\infty}$, we refer to this formulation as the two-channel mixed $\mathcal{H}_{2}$/$\mathcal{H}_{\infty}$ design.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Policy optimization for mixed $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ design", "weight": 1.0} -->

We make the following standard assumption throughout.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

We make another assumption for analysis.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The matrix $Q_{2}$ is positive semidefinite. The matrices $W$, $Q_{\infty}$, $R_{2}$, and $R_{\infty}$ are positive definite.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 1 (Single-channel case)", "weight": 1.0} -->

We give further details in Appendix A.1 ‣ Appendix A Proofs in Sections 2 and 3 ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality"). As we will see, this reformulation yields a simpler gradient formula and a closed-form optimum. ∎

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Classical solutions to mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design primarily rely on Riccati equations or LMIs. While effective for small- to medium-scale systems, these techniques offer limited insight into the optimization landscape, and may face challenges in high-dimensional or data-driven settings.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem statement", "weight": 1.0} -->

In this work, we revisit the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control in from a nonconvex optimization perspective.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Geometry of the optimization landscape. We study the geometry of the $\mathcal{H}_{\infty}$-constrained feasible domain $\mathcal{K}_{\beta}$, and analyze key properties of the mixed cost function, including continuity, analyticity, and gradient expressions.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Global optimality of stationary points. We investigate whether problem admits spurious stationary points. We further derive the optimality conditions, and analyze the existence and uniqueness of stationary points.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Analysis via the $\mathtt{E}\mathtt{C}\mathtt{L}$ framework. We explore if the hidden convexity in problem can be revealed via an appropriate convex lifting. In particular, we ask if an extended convex lifting ($\mathtt{E}\mathtt{C}\mathtt{L}$) can be constructed to certify the global optimality of stationary points.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Problem statement", "weight": 1.0} -->

Collectively, our results provide a renewed understanding of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control through nonconvex optimization and convex lifting, and offer guidance for the design of principled policy optimization algorithms in large-scale or model-free settings.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Basic Landscape Properties", "weight": 1.0} -->

In this section, we investigate the optimization landscape of, i.e., the geometry of the feasible set $\mathcal{K}_{\beta}$ and structural properties of the mixed cost function $J_{mix}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Geometry of the $\\mathcal{H}_{\\infty}$ constrained domain", "weight": 1.0} -->

We start with a version of the Bounded Real Lemma, which connects a Riccati equation (or inequality) to an upper bound on the $\mathcal{H}_{\infty}$ norm. Here, we slightly abuse the notation for the matrices $A$, $B$, and $C$, but this should cause no confusion in the context.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Example 1", "weight": 1.0} -->

This implies that for any $\beta > 1.1$, $\mathcal{K}_{\beta}$ is unbounded.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Example 1", "weight": 1.0} -->

Fig. 1(a) plots $\mathcal{K}_{\beta}$ restricted to the subspace $k_{11} = k_{22} = 0$ for $\beta = 3.5$, $6$, and $\infty$ (i.e., the unconstrained stabilizing set $\mathcal{K}$). The policies $K_{1}$, $K_{2}$, and $K_{3}$, marked in red, demonstrate the nonconvexity for $\beta = 3.5$. As expected, the feasible set $\mathcal{K}_{\beta}$ becomes larger as $\beta$ increases. ∎

<!-- chunk {"id": "body-0037", "role": "body", "section": "Example 1", "weight": 1.0} -->

We next characterize the boundary of $\mathcal{K}_{\beta}$. This will be useful as we later discuss the properties of $J_{mix}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Analyticity of the mixed $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ cost function", "weight": 1.0} -->

We now examine some properties of the cost function. It is clear from Lemma 2 that $J_{mix}$ is nonconvex. Our next result shows that it is real analytic (and hence infinitely differentiable) on the feasible set $\mathcal{K}_{\beta}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Example 2 (Non-coercivity)", "weight": 1.0} -->

Theorem 2 ensures that $J_{mix}$ is infinitely differentiable. In particular, we have the following gradient formulas.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 2 (Comparison with LQR)", "weight": 1.0} -->

Lemmas 4 and 5 show that computing $\nabla J_{mix}$ requires solving one Riccati and one Lyapunov equation, slightly more involved than the LQR case, which only needs two Lyapunov equations \[26, Section IV\]. Note that as $\beta\rightarrow\infty$, $J_{mix}$ in and (11. ‣ 2.2 Policy optimization for mixed ℋ₂/ℋ_∞ design ‣ 2 Preliminaries ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality")) reduces to $J_{LQR}$, and both gradient formulas simplify to $\nabla J_{LQR}$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 2 (Comparison with LQR)", "weight": 1.0} -->

This is expected as reduces to LQR as $\beta\rightarrow\infty$. ∎

<!-- chunk {"id": "body-0042", "role": "body", "section": "No Spurious Stationary Points", "weight": 1.0} -->

In this section, we characterize the global optimality of the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Any stationary point is globally optimal", "weight": 1.0} -->

Since $\mathcal{K}_{\beta}$ is open, any local minimizer of $J_{mix}$ must lie in its interior and thus must be a stationary point. Despite nonconvexity, we establish a key result that every stationary point (when it exists) of is globally optimal.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 3 (Connection to LQR)", "weight": 1.0} -->

As $\beta\rightarrow\infty$, both optimality conditions in the single- and two-channel cases, and, reduce to the classical LQR Riccati equation

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 3 (Connection to LQR)", "weight": 1.0} -->

with the optimal policy $K = {- {R^{- 1}B^{\mathsf{T}}P}}$, where $P$ is the stabilizing solution. ∎

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark 4 (Connection to $\\mathcal{H}_{\\infty}$ suboptimal control)", "weight": 1.0} -->

The Riccati equation (22b) is closely tied to state-feedback $\mathcal{H}_{\infty}$ suboptimal control. By \[51, Theorem 17.6\] and \[25, Theorem 20.2.1\], it admits a unique stabilizing solution $P$ if and only if there exists a policy $K \in \mathcal{K}_{\beta}$. One suboptimal policy is given by $K = {- {R^{- 1}B^{\mathsf{T}}P}}$. As shown in Corollary 3, this $K$ also solves problem with $z_{2} = z_{\infty}$. This highlights the close connection of to several classical formulations, including maximum entropy $\mathcal{H}_{\infty}$ control, risk-sensitive control, and zero-sum dynamic games. ∎

<!-- chunk {"id": "body-0047", "role": "body", "section": "Existence of stationary points", "weight": 1.0} -->

Theorem 3 and Corollaries 2-3 do not ensure the existence of stationary points. In particular, the optimality conditions may be infeasible. We summarize this fact below.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Fact 1", "weight": 1.0} -->

Under Assumptions 1 and 2, the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control may admit no stationary points in $\mathcal{K}_{\beta}$, and its optimal value may not be attained within $\mathcal{K}_{\beta}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Fact 1", "weight": 1.0} -->

In fact, the infeasibility of stems from an overly stringent robustness requirement. Relaxing the constraint by increasing $\beta$ ensures the existence of a stationary point.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Example 4.7", "weight": 1.0} -->

Case 3 (single-channel): $\beta = 1$. We consider $Q = 0$ and $R = 1$, which preserves the LQR cost but alters the $\mathcal{H}_{\infty}$ constraint (blue curve in Figure 2(c)). Here, $J_{mix}$ always admits a stationary point, showing that problem structure beyond $\beta$ also affects the existence of optimal policies.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Analysis via Extended Convex Lifting", "weight": 1.0} -->

This section exploits the recent $\mathtt{E}\mathtt{C}\mathtt{L}$ framework to prove the global optimality result in Theorem 3, details the $\mathtt{E}\mathtt{C}\mathtt{L}$ construction for problem, and discusses the solvability of the associated convex reformulation.

<!-- chunk {"id": "body-0052", "role": "body", "section": "A framework of Extended Convex Lifting", "weight": 1.0} -->

The $\mathtt{E}\mathtt{C}\mathtt{L}$ framework studies a class of nonconvex optimization problems using convex tools. The key idea is simple and based on a change of variables. Let $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ be smooth and nonconvex. Suppose there exists a smooth bijection $y = {\phi{(x)}}$ such that ${g{(y)}}:={f{({\phi^{- 1}{(y)}})}}$ becomes convex. It is then clear that ${{\min f}{(x)}} = {{\min g}{(y)}}$ and every stationary point of $f$ is globally optimal. Here, the mapping $y = {\phi{(x)}}$ acts as direct convexification.

<!-- chunk {"id": "body-0053", "role": "body", "section": "A framework of Extended Convex Lifting", "weight": 1.0} -->

The $\mathtt{E}\mathtt{C}\mathtt{L}$ generalizes this idea to a broader class of constrained nonconvex problems that may not admit direct convexification. Indeed, such problems frequently arise in control, including. We first review the definitions and key results of $\mathtt{E}\mathtt{C}\mathtt{L}$, presenting a simplified version tailored for clarity and relevance to our setting.

<!-- chunk {"id": "body-0054", "role": "body", "section": "A framework of Extended Convex Lifting", "weight": 1.0} -->

For a function $f:{\mathcal{D}\rightarrow{\mathbb{R}}}$ with an open domain $D \subseteq {\mathbb{R}}^{d}$, we define its strict and non-strict epigraphs by

<!-- chunk {"id": "body-0055", "role": "body", "section": "Remark 5.14 (Another valid $\\mathtt{E}\\mathtt{C}\\mathtt{L}$)", "weight": 1.0} -->

In constructing $\mathcal{L}_{lft}$ in (25a), the nonstrict Riccati inequality is crucial for establishing ${{epi}_{\geq}{(J_{mix})}} \subseteq {\pi_{K,\gamma}{(\mathcal{L}_{lft})}}$. If instead the strict Riccati inequality is used, the construction still yields a valid $\mathtt{E}\mathtt{C}\mathtt{L}$, but only ensures the weaker inclusion ${{epi}_{>}{(J_{mix})}} \subseteq {\pi_{K,\gamma}{(\mathcal{L}_{lft})}}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Remark 5.14 (Another valid $\\mathtt{E}\\mathtt{C}\\mathtt{L}$)", "weight": 1.0} -->

By Lemma 5.10. ‣ 5.1 A framework of Extended Convex Lifting ‣ 5 Analysis via Extended Convex Lifting ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality"), an $\mathtt{E}\mathtt{C}\mathtt{L}$ certifies the global optimality of any non-degenerate stationary points. According to Definition 5.9. ‣ 5.1 A framework of Extended Convex Lifting ‣ 5 Analysis via Extended Convex Lifting ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality") and the inclusion ${{epi}_{\geq}{(J_{mix})}} \subseteq {\pi_{K,\gamma}{(\mathcal{L}_{lft})}}$ shown in Theorem 5.13, we have the following desirable property.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Convex reformulation and its solvability", "weight": 1.0} -->

The $\mathtt{E}\mathtt{C}\mathtt{L}$ construction also leads to a convex reformulation, which offers further insight into problem.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In this section, we present numerical experiments evaluating the performance of different methods for solving the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control and in both small and large-scale cases.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Numerical approaches and setup", "weight": 1.0} -->

Analytical solution: For the single-channel case, we solve the Riccati equation (22b) and obtain the optimal policy from (22a).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Numerical approaches and setup", "weight": 1.0} -->

Policy iteration: Inspired by the optimality conditions in Corollaries 2 and 3, we apply iterative policy updates to solve and its single-channel case. The details are given below.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Numerical approaches and setup", "weight": 1.0} -->

LMI-based convex optimization: Solve the convex reformulation in with the conic solver MOSEK.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Numerical approaches and setup", "weight": 1.0} -->

HIFOO: A sophisticated nonsmooth optimization package (v3.501 with Hanso 2.01) for fixed-order $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ controller synthesis.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Numerical approaches and setup", "weight": 1.0} -->

Policy iteration. The method starts from a feasible policy and alternates between policy evaluation (solving a Riccati equation) and policy improvement. It can be viewed as a fixed-point iteration for solving a stationary point ${{\nabla J_{mix}}{( \cdot )}} = 0$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Numerical approaches and setup", "weight": 1.0} -->

While a formal convergence analysis remains open, we conjecture that the method converges for sufficiently large $\beta$, and leave this as future work.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Numerical approaches and setup", "weight": 1.0} -->

Setup. All experiments are conducted in MATLAB R2024b. The stabilizing Riccati solution is computed using MATLAB's icare. Policy iteration is run until convergence ${\|{K^{\prime} - K}\|} < 10^{- 5}$. For LMI-based methods, we use MOSEK with its default high-accuracy stopping criteria.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Numerical approaches and setup", "weight": 1.0} -->

We compare these methods in terms of 1) the runtime complexity; 2) the square root of $J_{mix}$ of the converged policy; 3) the resulting $\mathcal{H}_{2}$ and $\mathcal{H}_{\infty}$ norms.

<!-- chunk {"id": "body-0067", "role": "body", "section": "A low-dimensional example", "weight": 1.0} -->

We begin with a low-dimensional example (instance $0$) with a $3 \times 3$ policy matrix. The problem parameters are

<!-- chunk {"id": "body-0068", "role": "body", "section": "A low-dimensional example", "weight": 1.0} -->

The performance matrices for the $\mathcal{H}_{2}$ and $\mathcal{H}_{\infty}$ channels are

<!-- chunk {"id": "body-0069", "role": "body", "section": "A low-dimensional example", "weight": 1.0} -->

For the special case $z_{2} = z_{\infty}$, we set $Q = R = I_{3}$. The minimal achievable robustness level (i.e., the optimal $\mathcal{H}_{\infty}$ norm) is $\beta^{\ast} \approx 5.24$. We evaluate all methods with $\beta = 6$, $14$, and $18$. One can verify that Assumptions 1 and 2 are satisfied. For reference, in the single-channel case, the optimal LQR policy achieves an $\mathcal{H}_{\infty}$ norm $\approx 9.26$ (with the optimal LQR cost $\approx 9.92$); in the two-channel case, the corresponding values are around $19.15$ and $4.65$, respectively. Therefore, our chosen $\beta$ values are small enough so that problem cannot be solved analytically for the two-channel case.

<!-- chunk {"id": "body-0070", "role": "body", "section": "A low-dimensional example", "weight": 1.0} -->

Table 1 summarizes the performance of all four approaches. The ARE row shows that solving (22b) is the most efficient and serves as the benchmark when $z_{2} = z_{\infty}$. From the PI row, we observe that the single-channel update in (28a) performs reliably, requiring only about $10$ times the runtime of solving (22b). In the two-channel setting, the policy iteration in (28b) converges for $\beta = 18$, maintaining feasibility throughout and achieving the optimal policy of, consistent with the LMI-based solution. However, for smaller values of $\beta$, (28b) fails to converge, an observation consistent with our conjecture. For $\beta = 6$, the iterates leave the feasible set $\mathcal{K}_{\beta}$ and the procedure terminates (e.g., at some iteration $t$, the $\mathcal{H}_{\infty}$ norm of $K_{t}$ exceeds $6$).

<!-- chunk {"id": "body-0071", "role": "body", "section": "A low-dimensional example", "weight": 1.0} -->

For $\beta = 14$, the iterates remain feasible in $\mathcal{K}_{\beta}$ but fail to converge, instead exhibiting a periodic behavior suggesting of a limit cycle.

<!-- chunk {"id": "body-0072", "role": "body", "section": "A low-dimensional example", "weight": 1.0} -->

From the LMI row, we see that the global minimum of $J_{mix}$ is attained by solving the convex reformulation, with the gradient $\nabla J_{mix}$ of the resulting policy nearly zero. Overall, when successful, all three methods (ARE, PI, LMI) yield almost identical solutions. Finally, the HIFOO solver is less reliable for smaller $\beta$, often triggering warnings or failing to return feasible solutions. Even at $\beta = 18$, its performance (especially the $\mathcal{H}_{\infty}$ norm) deviates noticeably from the other methods. This is expected as HIFOO relies on nonsmooth local optimization and does not guarantee global optimality. In contrast, our result in Theorem 3 ensures that stationary points found via gradient-based methods are globally optimal.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Higher-dimensional examples", "weight": 1.0} -->

We next consider three higher-dimensional examples, with policy matrices of sizes $15 \times 15$, $60 \times 60$, and $90 \times 90$, referred to as instances $1$, $2$, and $3$, respectively. The problem data for the single-channel formulations are adapted from \[45, Sec. 7.3\]. For the two-channel formulations, we retain the same $\mathcal{H}_{\infty}$ performance signals but specify the $\mathcal{H}_{2}$ performance with $Q_{2} = I$ and $R_{2} = {\frac{1}{4}R_{\infty}}$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Higher-dimensional examples", "weight": 1.0} -->

The minimum robustness level $\beta^{\ast}$ for instances $1$-$3$ are $\approx 0.067$, $0.098$, and $0.096$, respectively. Unlike the low-dimensional example (instance $0$), our focus here is on assessing the scalability of different methods. Accordingly, we test larger robustness levels, setting $\beta = 10$, $15$, and $20$. One can verify that all assumptions are satisfied.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Higher-dimensional examples", "weight": 1.0} -->

Table 2 summarizes the results on the higher-dimensional examples. As shown in the ARE row, solving the Riccati equation remains highly efficient for the single-channel case, even at larger scales. The PI row demonstrates that the updates in remain effective as the problem size increases. Notably, the two-channel update (28b) converges across all instances, with the resulting policies exhibiting nearly vanishing gradients, which empirically supports our conjecture. This behavior suggests that (28b) enjoys an implicit regularization property, maintaining feasibility and achieving convergence when $\beta$ is sufficiently large.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Higher-dimensional examples", "weight": 1.0} -->

The LMI row shows that the global minimum of $J_{mix}$ can be achieved by solving a convex reformulation. However, despite yielding policies with nearly zero gradients, the LMI method scales poorly: its runtimes for instance $2$ and $3$ are significantly longer than those of the analytical and policy iteration approaches. Overall, compared with the classical LMI-based methods, these results show that policy iteration can scale more favorably to large-scale problems.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Conclusions", "weight": 1.0} -->

In this paper, we examine the nonconvex optimization landscape of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control. We characterize the feasible set and cost function, showing that despite nonconvexity, every stationary point is globally optimal. Our analysis, grounded in the $\mathtt{E}\mathtt{C}\mathtt{L}$ framework, further clarifies the role of strict versus non-strict Riccati inequalities in certifying global optimality and ensuring solvability of the convex reformulation. Several open questions are worth further investigation. An important one is to establish convergence guarantees for policy iteration in the general two-channel case, particularly for large $\beta$. Another is to design principled, scalable policy optimization algorithms for mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design with provable performance guarantees.
