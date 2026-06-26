<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Data-Driven Inverse Reinforcement Learning of Linear Systems with Model Uncertainty: A Convex Optimization View

Topics include Inverse reinforcement learning, Data-driven control, Linear systems, Model uncertainty, Convex optimization, Optimal control, Robustness.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Frames inverse reinforcement learning for uncertain linear systems as a convex optimization problem over data-consistent models and objectives. The work is useful because it connects reward recovery, model uncertainty, and data-driven control synthesis in a single tractable view.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Inverse reinforcement learning (IRL) for linear systems seeks a cost function whose optimal controller reproduces an expert policy from data. Existing data-driven methods for discrete-time linear systems are largely built on iterative policy/value updates, repeated matrix inversions, and, in some cases, an initial stabilizing controller, which can limit numerical robustness and practical applicability. This paper develops a convex-optimization framework for data-driven inverse reinforcement learning of discrete-time linear systems with model uncertainty. For nominal systems, we derive a semidefinite characterization of inverse optimality and a relaxed formulation that recovers an equivalent state-cost matrix together with a stabilizing controller from expert trajectories. We then obtain a model-free, off-policy reformulation by replacing the unknown system matrices with a regressed kernel matrix identified from local input-state data. For uncertain local systems, we show that a standard LQR cost is generally insufficient to represent every stabilizing target gain and therefore introduce a generalized LQR cost with a state-input cross term.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Based on this model, we develop a convex data-driven inverse-RL method and extend it to robust cost design over a population of perturbations via differentiable semidefinite programming and stochastic approximation. Simulations on a discrete-time power-system example show accurate recovery of expert behavior, improved robustness to gain-estimation error and model mismatch, and a simpler computational pipeline than classical iterative inverse-RL schemes.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Inverse reinforcement learning (IRL) has become an important tool for recovering implicit performance criteria from expert behavior and then reproducing that behavior on a local system. In linear systems, this objective is closely related to inverse optimal control for quadratic costs, where the goal is to identify a cost function whose optimal controller explains a demonstrated state-feedback law. Because linear quadratic regulation (LQR) provides a precise connection among cost functions, Riccati equations, and stabilizing feedback policies, it offers a natural foundation for studying IRL in control applications lewis2012optimal. Such an inverse viewpoint is useful for imitation control, controller interpretation, and data-driven design when expert trajectories are available but the underlying objective function is not xue2021inverse; xue2021inverseQlearning; lian2022inverse.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent work has shown that IRL can be formulated effectively for several classes of linear control problems. Inverse optimal control has been studied for tracking problems in xue2021inverse, discrete-time inverse reinforcement Q-learning through expert imitation has been developed in xue2021inverseQlearning, and inverse-RL formulations for linear multiplayer games have been investigated in lian2022inverse. More recently, inverse value-iteration and Q-learning methods with stability and robustness analysis were reported in lian2024inverse, a modified Kleinman-iteration approach was proposed in wu2026inverse, and output-feedback discounted IRL for continuous-time linear systems was studied in wu2026output. These works demonstrate the growing maturity of linear IRL, but they also reveal a common structural feature: many existing methods rely on repeated policy evaluation, value iteration, or policy-improvement loops.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although iterative IRL schemes are effective in many settings, they can be computationally demanding and numerically sensitive. Repeated matrix inversions may amplify approximation and estimation errors, and some formulations require an initial stabilizing controller, which may be unavailable in practice xue2021inverseQlearning; lian2022inverse; lian2024inverse; wu2026inverse. In addition, when expert and local systems are not identical, the recovered target controller may fail to admit a standard inverse-LQR interpretation. These issues become particularly important in data-driven settings, where the expert gain and closed-loop matrix must themselves be estimated from finite trajectory data.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A natural way to address these limitations is to revisit inverse RL from a convex-optimization viewpoint. For forward LQR design, the relationship among Riccati equations, linear matrix inequalities (LMIs), and convex optimization is well established boyd1994linear; balakrishnan1995connections. This viewpoint has also influenced data-driven and model-free optimal control, including semidefinite-programming approaches to data-driven LQR rotulo2020data and Q-function-based or primal--dual learning methods lee2018primal; farjadnasab2022model. These developments suggest that convex structure can be exploited not only for forward controller synthesis but also for inverse RL, with the potential to reduce iteration and improve numerical robustness.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motivated by this observation, this paper develops a data-driven IRL framework for discrete-time linear systems with model uncertainty. We consider both nominal local systems and uncertain local systems that match the expert only at the closed-loop level. For the uncertain case, we show that a standard LQR cost may be too restrictive because not every stabilizing feedback gain can be represented as the optimal controller of a standard discrete-time LQR problem. We therefore introduce a generalized quadratic cost with a state--input cross term, following the generalized LQR framework in heij2007introduction, and then formulate a robust cost-design problem over a population of perturbed plants. To solve the robust problem, we combine semidefinite programming with differentiable convex optimization layers agrawal2019differentiable and stochastic approximation robbins1951stochastic.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main contributions of this paper are summarized as follows.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We derive a model-based convex inverse-RL formulation for nominal discrete-time linear systems. The resulting semidefinite conditions recover an equivalent state-cost matrix and, through a relaxed gain-matching formulation, a stabilizing controller that reproduces the expert behavior.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop a model-free, off-policy reformulation by replacing the unknown system matrices with a regressed kernel matrix obtained from local input--state data. Under noise-free identifiability conditions, this formulation is an exact data-driven counterpart of the nominal convex inverse-RL problem.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We extend the framework to local systems with model uncertainty. In this setting, we show why a generalized LQR cost with a cross term is needed, and we derive a convex data-driven inverse-RL formulation that recovers both a generalized cost pair and a stabilizing controller.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We formulate a robust inverse-RL design problem over a distribution of plant perturbations and solve it through differentiable semidefinite programming and stochastic approximation. This extension allows the learned cost to account for model variability rather than fitting a single nominal perturbation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Compared with classical two-loop and single-loop inverse-RL schemes, the proposed Algorithms 1--3 remove repeated inverse-RL policy/value iterations and do not require an initial stabilizing gain, which leads to a simpler and more numerically stable computational pipeline.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of the paper is organized as follows. Section 2 formulates the inverse-RL problems for the expert and local systems. Section 3 presents the model-based convex inverse-RL methodology. Section 4 develops the data-driven methods for nominal and uncertain systems and introduces the robust design extension. Section 5 compares the proposed framework with related data-driven inverse-RL methods, and Section 6 reports simulation results. Finally, Section 7 concludes the paper Notation: For a symmetric matrix $M$, the relations $M\succ 0$ and $M\succeq 0$ denote positive definiteness and positive semidefiniteness, respectively. The Frobenius norm is denoted by $\|\cdot\|_{F}$, $\mathrm{vec}(\cdot)$ stacks the columns of a matrix into a vector, and $\otimes$ denotes the Kronecker product.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation and Preliminaries", "weight": 1.0} -->

This section introduces the expert system and the nominal local system. The inverse reinforcement learning (IRL) problem is formulated for the nominal local system, while extensions to local systems with uncertainty are addressed in subsequent sections.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Expert Target Discrete-Time System", "weight": 1.0} -->

Consider the target discrete-time (DT) linear system where $A\in\mathbb{R}^{n\times n}$, $B\in\mathbb{R}^{n\times m}$ and $x_{e}\in\mathbb{R}^{n}$, $u_{e}\in\mathbb{R}^{m}$ denote the state and control input of the expert system, respectively. Moreover, the expert input is generated by a linear state-feedback control law $u_{e}(k)=K_{e,1}x_{e}(k)$, which minimizes the infinite-horizon quadratic cost function where $Q_{e}\in\mathbb{R}^{n\times n}\succeq 0$ and $R_{e}\in\mathbb{R}^{m\times m}\succ 0$ are the state and input weighting matrices, respectively.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Expert Target Discrete-Time System", "weight": 1.0} -->

In addition, we assume that $(A,B)$ is controllable and that the pair $(A,\sqrt{Q_{e}})$ is observable.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Expert Target Discrete-Time System", "weight": 1.0} -->

The minimization of corresponds to a standard linear quadratic regulator (LQR) problem, according to optimal control theory in lewis2012optimal, whose solution is given by

<!-- chunk {"id": "body-0021", "role": "body", "section": "Nominal Local Discrete-Time System", "weight": 1.0} -->

Consider a nominal local system with dynamics identical to the expert system, where $x\in\mathbb{R}^{n}$ and $u\in\mathbb{R}^{m}$ denote the state and control input of the local system, respectively.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Nominal Local Discrete-Time System", "weight": 1.0} -->

The local system is associated with an arbitrary infinite-horizon quadratic cost function where $Q\in\mathbb{R}^{n\times n}\succeq 0$ and $R\in\mathbb{R}^{m\times m}\succ 0$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Nominal Local Discrete-Time System", "weight": 1.0} -->

Analogously to Subsection 2.1, the optimal control law and value function are given by

<!-- chunk {"id": "body-0024", "role": "body", "section": "Inverse Reinforcement Learning Formulation", "weight": 1.0} -->

The inverse reinforcement learning problem is defined under the following standard assumptions.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The system matrices $(A,B)$ in and, the cost matrices $(Q_{e},R_{e})$, and the expert controller gain $K_{e,1}$ in are unknown.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The trajectories $(x_{e}(k),u_{e}(k))$ of and $(x(k),u(k))$ of are available.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem 1", "weight": 1.0} -->

Given Assumptions 1--2, select $R\in\mathbb{R}^{m\times m}\succ 0$ and determine a cost matrix $Q$ equivalent to $Q_{e}$ such that the resulting optimal controller gain coincides with the expert controller $K_{e,1}$, as defined in Definition 1.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Model-Based Inverse RL Methodology", "weight": 1.0} -->

This section presents a model-based inverse reinforcement learning (IRL) method based on convex programming.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Model-Based Inverse RL Methodology", "weight": 1.0} -->

The first step is to identify the target controller gain and the target closed-loop dynamics of the expert system. The target closed-loop dynamics are defined as Both the target closed-loop matrix and the expert controller gain can be estimated from the expert trajectory data $(x_{e}(k),u_{e}(k))$ using the least-squares method described in xue2021inverse: Here, $N_{\mathrm{d}}>n$ denotes the number of data groups.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Model-Based Inverse RL Methodology", "weight": 1.0} -->

Suppose that the optimal cost matrix $Q$ corresponding to a selected $R\succ 0$ is obtained as a solution to Problem 1. It is well known that the solution must satisfy the following conditions lian2022inverse; xue2021inverse; xue2021inverseQlearning: where $K_{e,1}$ is the expert controller gain.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Model-Based Inverse RL Methodology", "weight": 1.0} -->

Substituting the definition of the target closed-loop dynamics into -- yields the equivalent single condition Since is linear with respect to the matrix variables $P$ and $Q$, a feasibility problem can be formulated using semidefinite programming.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Model-Based Inverse RL Methodology", "weight": 1.0} -->

est_target_gain},\quad\hat{F}_{e,1}\ \text{satisfies est_target_dyna}.$ | | | The feasibility problem can be solved using standard convex optimization solvers such as MOSEK, SCS, or CVXOPT. Any feasible solution satisfies, which is equivalent to and, and therefore constitutes a valid solution to Problem 1.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 1", "weight": 1.0} -->

It is well known that the feasibility problem admits infinitely many solutions $(P,Q)$ satisfying and when $\mathrm{rank}(B^{\top})\neq n$, which is a fundamental property of inverse reinforcement learning lian2022inverse; lewis2012optimal.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Although the inverse RL solution is characterized, the feasibility of depends on the accuracy of the least-squares estimates and. Consequently, a feasible solution may not exist when these estimates are inaccurate. To address this issue, the optimization problem will be modified in to improve robustness with respect to estimation errors in the target dynamics and controller gain.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Thus, the constraint in is relaxed by incorporating it into the objective function, leading to the following optimization problem: | | | $\displaystyle\underset{P,Q}{\mathrm{minimize}}$ | | $\displaystyle w_{1}\lVert f_{1}(P,Q)\rVert_{F}^{2}+w_{2}\lVert f_{2}(P)\rVert_{F}^{2}$ | | \(22\) | | | | $\displaystyle\mathrm{subject\ to}$ | | $\displaystyle Q\succeq 0,\quad P\succ 0,$ | | | | | | $\displaystyle\hat{K}_{e,1}\ \text{satisfies est_target_gain},\quad\hat{F}_{e,1}\ \text{satisfies est_target_dyna}.$ | | | Here, $w_{1}$ and $w_{2}$ are positive scalar weights that balance the relative importance of the objective

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 1", "weight": 1.0} -->

terms, $f_{1}(P,Q)$ and $f_{2}(P)$ correspond to the relaxed constraint in and the optimality condition, respectively, defined as The optimization problem is convex and can therefore be solved using standard convex programming techniques.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 1", "weight": 1.0} -->

If the objective of Problem 1 is solely to recover a cost matrix equivalent to $Q_{e}$, the procedure may terminate at this stage. However, to additionally obtain a stabilizing controller gain $K_{1}^{\star}$ derived from $Q$ that is close to the expert gain $K_{e,1}$, further steps are required. This setting corresponds to the inverse RL imitation problem studied in xue2021inverseQlearning.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Problem 2", "weight": 1.0} -->

Given Assumptions 1--2, select $R\in\mathbb{R}^{m\times m}\succ 0$ and determine a cost matrix $Q$ equivalent to $Q_{e}$ such that the resulting optimal controller gain coincides with the expert gain $K_{e,1}$, as defined in Definition 1. Moreover, determine a stabilizing controller gain $K_{1}^{\star}$ obtained from the optimal control problem with cost matrix $Q$ that satisfies $K_{1}^{\star}=K_{e,1}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Problem 2", "weight": 1.0} -->

The optimization problem alone is insufficient to solve Problem 2, as it does not explicitly characterize a stabilizing controller gain close to the expert controller $K_{e,1}$. While the estimated gain $\hat{K}_{e,1}$ is available, it does not necessarily stabilize the local system. Consequently, solving the optimal control problem associated with the recovered cost matrix $Q$ is necessary to obtain a stabilizing gain while preserving proximity to $K_{e,1}$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Problem 2", "weight": 1.0} -->

The LQR problem can be interpreted as determining the tightest lower bound of the cost function, which can be reformulated as a linear matrix inequality (LMI), as stated in the following lemma.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Data-Driven Inverse RL", "weight": 1.0} -->

Algorithm 1 provides a general pipeline for solving the inverse RL imitation control problem. However, this approach requires explicit knowledge of the system dynamics $(A,B)$, which constitutes a strong and often impractical assumption. In this section, a model-free implementation of Algorithm 1 is developed, relying solely on data trajectories from the local and expert systems. Moreover, the proposed framework is extended to accommodate local systems with model uncertainty.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The optimization problem is a semidefinite program and hence convex. The constraint must yield a sufficient number of independent linear equations to uniquely identify the regressed kernel matrix $\hat{H}$. Specifically, the data matrix $[X^{k\top},U^{k\top}]\otimes[X^{k\top},U^{k\top}]$ must have rank at least $(n+m)(n+m+1)/2$. This condition is satisfied when the input signal $\bar{u}(k)$ persistently excites the system.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 3", "weight": 1.0} -->

The block LMI embedded in can be interpreted as the primal representation of the dual approaches in farjadnasab2022model; lee2018primal, as established in balakrishnan1995connections.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Algorithm 2 summarizes the complete model-free implementation of the proposed inverse RL framework.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 3", "weight": 1.0} -->

1:Select an arbitrary matrix R ≻ 0 and estimate K̂e, 1 using. 2:Collect data groups (Uk, Xk, Xk + 1) from the local system driven by ū(k) satisfying persistent excitation. 3:Solve for (P, Ĥ) using. 4:Return the cost matrix Q⋆ computed from and the controller gain K1⋆ = −(R + Ĥuu⋆)−1Ĥxu⋆⊤. Algorithm 2 Model-Free Inverse RL Imitation Control

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark 4", "weight": 1.0} -->

The proposed algorithm is non-iterative and consists of a single convex optimization problem. Unlike iterative inverse RL methods xue2021inverse; xue2021inverseQlearning; lian2022inverse; wu2026output, which involve repeated matrix inversions and are therefore susceptible to numerical instability, the proposed formulation avoids error accumulation across iterations. This structural property improves numerical robustness and reduces computational complexity. Furthermore, the method eliminates the need for an initial stabilizing gain, which is required in lian2022inverse and may be impractical to obtain in practice.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Data-Driven Inverse RL for Local Systems with Model Uncertainty", "weight": 1.0} -->

In practical scenarios, expert data are often collected from a system that shares a similar structure with the local system but is not identical. Such discrepancies may arise due to model degradation, unmodeled dynamics, or differences across production versions. As a result, it is reasonable to assume that the local system exhibits model uncertainty when compared with the expert system. Specifically, the local system dynamics are given by where $D\in\mathbb{R}^{m\times n}$ is an unknown model perturbation matrix, and $\gamma_{1},\gamma_{2}>0$ are unknown scaling factors.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Data-Driven Inverse RL for Local Systems with Model Uncertainty", "weight": 1.0} -->

In this setting, our goal is to recover a target controller gain $K_{\mathrm{tar},2}$ such that the closed-loop dynamics of the uncertain system coincide with the expert closed-loop dynamics, i.e., Under model uncertainty, the target controller recovered from data may fail to be inverse-optimal for a standard LQR cost of the form. To enlarge the class of admissible inverse-optimal controllers, we therefore adopt the generalized LQR cost as in heij2007introduction | | | $\displaystyle\sum_{k=0}^{\infty}\left(x^{\top}(k)Qx(k)+2x^{\top}(k)N^{\top}u(k)+u^{\top}(k)Ru(k)\right),$ | | | where $N\in\mathbb{R}^{m\times n}$ and that the block matrix satisfied To motivate the use of the generalized LQR framework instead of the standard LQR formulation, we first establish the following lemma.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Assumption 3", "weight": 1.0} -->

The system matrices $(A,B)$ in and $(A+\gamma_{1},\gamma_{2}B)$, the cost matrices $(Q_{e},R_{e})$, and the expert controller gain $K_{e,1}$ in are all unknown.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

The state--input trajectory pairs $(x(k),u(k))$ of the local system are available. The expert state trajectory $x_{e}(k)$ is available, and the expert input trajectory $u_{e}(k)$ is also available.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Problem 3", "weight": 1.0} -->

Given Assumptions 3--4, select $R\in\mathbb{R}^{m\times m}\succ 0$ and define the closed-loop dynamics of the uncertain local system as Determine a generalized cost pair $(Q,N)$ equivalent to $Q_{e}$ such that the resulting closed-loop matrix $F_{2}$ coincides with the expert closed-loop matrix $F_{e,1}$, as defined in Definition 2. Furthermore, determine a stabilizing controller gain $K_{2}^{\star}$ obtained from the corresponding generalized optimal control problem.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Problem 3", "weight": 1.0} -->

We show that the general pipeline for deriving a solution to Problem 3 closely follows that for Problem 2. Specifically, we first derive the target controller gain $\hat{K}_{\mathrm{tar},2}$ and then solve a modified optimization problem to obtain the inverse-optimal weights $(Q,N)$. However, unlike in Problem 2, the target controller gain $\hat{K}_{\mathrm{tar},2}$ cannot be obtained, because it must also satisfy the consistency condition. Deriving $\hat{K}_{\mathrm{tar},2}$ therefore normally requires knowledge of the local system dynamics. Instead, we avoid using the explicit system model by exploiting state--input trajectory data collected from the local system.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Problem 3", "weight": 1.0} -->

Consider the uncertain system driven by a persistently exciting input $\bar{u}(k)$: Let the data matrices $U^{k}$, $X^{k}$, and $X^{k+1}$ be defined as in --, using data collected, and suppose that the resulting data satisfy the persistent excitation condition in Remark 2. Following rotulo2020data, the closed-loop dynamics during data collection can be expressed as Using this representation, we obtain | | $\displaystyle\bar{A}+\bar{B}\hat{K}_{\mathrm{tar},2}$ | $\displaystyle=[\bar{A}\quad\bar{B}]\begin{bmatrix}I_{n}\\ | | \(70\) | | | | \hat{K}_{\mathrm{tar},2}\end{bmatrix}$ | | | | | | $\displaystyle=X^{k+1}\begin{bmatrix}X^{k}\\ | | | | | |

<!-- chunk {"id": "body-0054", "role": "body", "section": "Remark 5", "weight": 1.0} -->

Equation is written in a pseudo-inverse form; however, it can equivalently be interpreted as a least-squares problem when $\hat{M}_{2}$ is not full column rank. Moreover, since the optimization-based approach proposed later does not require an exact estimate of $\hat{K}_{\mathrm{tar},2}$, the method remains effective even with an inaccurate target gain. It is also worth noting that the derivation of $\hat{K}_{\mathrm{tar},2}$ in -- involves two pseudo-inverse (or least-squares) computations, which may be computationally expensive for large-scale systems. In such cases, alternative methods such as gradient descent, recursive least squares, or singular value decomposition (SVD) can be employed.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Robust cost design from the nominal inverse-RL solution", "weight": 1.0} -->

Throughout this paper, the goal of inverse reinforcement learning is not only to recover an expert controller, but also to identify a cost representation that explains the expert behavior and can be reused for related control-design tasks. This point becomes especially important for a population of systems that share the same nominal structure but are subject to different perturbations. Although the method in Subsection 4.2 can be applied to each perturbed system separately, doing so is inefficient and does not exploit the common structure across the population. Motivated by this limitation, we now seek a nominal cost design that is robust in an ensemble sense, so that a single recovered cost transfers well on average across the perturbed systems.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Assumption 5", "weight": 1.0} -->

The expert trajectory data $(x_{e}(k),u_{e}(k))$ for the system are available and satisfy the persistent excitation condition stated in Remark 2.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Assumption 6", "weight": 1.0} -->

The population of perturbed systems is described by where $D_{j}\in\mathbb{R}^{m\times n}$ are i.i.d. random perturbation matrices with known distribution, zero mean, and finite second moment.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Problem 4", "weight": 1.0} -->

Given Assumptions 5--6 and a prescribed matrix $R\in\mathbb{R}^{m\times m}\succ 0$, determine a nominal generalized cost pair $(Q,N)$ such that the expected mismatch between the expert closed-loop matrix and the forward-LQR closed-loop matrices of the perturbed plants is minimized.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Problem 4", "weight": 1.0} -->

Specifically, for each realization $D_{j}$, define where $P_{j}$ is the stabilizing solution of the generalized Riccati equation | | $\displaystyle P_{j}$ | $\displaystyle=Q+A_{j}^{\top}P_{j}A_{j}$ | | \(79\) | | | | $\displaystyle\quad-(A_{j}^{\top}P_{j}B+N^{\top})\left(R+B^{\top}P_{j}B\right)^{-1}(B^{\top}P_{j}A_{j}+N).$ | | | The objective is to solve In practice, the target matrix $F_{e,1}$ in can be replaced by its estimate $\hat{F}_{e,1}$ obtained, while the nominal matrices in the forward problem can be replaced by the data-driven estimates $(\hat{M}_{1},\hat{M}_{2})$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Problem 4", "weight": 1.0} -->

A natural approach is therefore Monte Carlo optimization: sample perturbations $D_{j}$, solve the forward generalized LQR problem for each realization, and minimize the empirical version of.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Problem 4", "weight": 1.0} -->

To keep the forward map numerically stable, we use the extended LMI characterization in Lemma 1 instead of the iterative schemes used in xue2021inverse; xue2021inverseQlearning; lian2022inverse; wu2026output, as follows: | | | $\displaystyle\underset{P}{\mathrm{maximize}}$ | | $\displaystyle\operatorname{tr}(P)$ | | \(82\) | | | | $\displaystyle\mathrm{subject\ to}$ | | $\displaystyle P\succ 0,$ | | | | | | $\displaystyle\begin{bmatrix}A^{\top}PA+Q-P&A^{\top}PB+N^{\top}\\ | | | | | | B^{\top}PA+N&B^{\top}PB+R\end{bmatrix}\succ 0.$ | | | This optimization requires gradients of an SDP-defined forward map with respect to $(Q,N)$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Problem 4", "weight": 1.0} -->

Rather than differentiating through the solver iterations, we use differentiable convex optimization layers, such as CVXPYLayers agrawal2019differentiable, and compute gradients by implicit differentiation of the optimality conditions. This approach remains numerically stable and yields exact gradients under standard regularity assumptions.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Problem 4", "weight": 1.0} -->

The main drawback of a full Monte Carlo formulation is its computational cost: achieving an estimation error of order $\mathcal{O}(\varepsilon)$ typically requires $\mathcal{O}(\varepsilon^{-2})$ samples. We therefore adopt a stochastic approximation approach using stochastic gradient descent (SGD), where $(Q,N)$ are updated based on gradients computed from a small batch of perturbation samples at each iteration. This substantially reduces the per-iteration cost while preserving scalability. The overall pipeline is summarized in Fig 1.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Remark 6", "weight": 1.0} -->

For a differentiable implementation based on CVXPYLayers, the constraint $\begin{bmatrix}Q&N^{\top}\\N&R\end{bmatrix}\succeq 0$ should be enforced through a factorized parameterization. Let $C$ be a fixed Cholesky factor of the prescribed matrix $R$, so that $R=CC^{\top}$, and write Then $Q=L_{Q}L_{Q}^{\top}+L_{N}L_{N}^{\top}$ and $N=CL_{N}^{\top}$, so the semidefinite constraint is satisfied automatically for all factor variables $(L_{Q},L_{N})$. Moreover, although is convex, it is not disciplined parametrized programming (DPP) compliant. For differentiation through the SDP layer, we therefore use the equivalent DPP-compatible formulation.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Remark 6", "weight": 1.0} -->

A practical stochastic-approximation implementation of the robust inverse-RL design is summarized in Algorithm 4.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Remark 6", "weight": 1.0} -->

1:Select a prescribed matrix R ≻ 0, compute a Cholesky factor C such that R = CC⊤, and choose a mini-batch size Nb, step sizes {ηt}t = 0T − 1, and a maximum number of SGD iterations T. 2:Estimate the expert closed-loop matrix F̂e, 1 using and estimate [M̂1 M̂2] using the regression in from expert trajectory data. 3:Compute K̂tar, 2 from and construct initial factors (LQ, LN) according to Remark 6. 4:For t = 0, 1, …, T − 1, repeat the following steps.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Remark 6", "weight": 1.0} -->

6:Draw a mini-batch of perturbation samples {Dj}j = 1Nb from the distribution in Assumption 6. 7:For each sampled perturbation, solve the forward generalized-LQR problem by the DPP-compatible SDP and compute Fj(Q(t), N(t)). 8:Form the mini-batch empirical loss $$\widehat{\mathcal{L}}_{t}=\frac{1}{N_{b}}\sum_{j=1}^{N_{b}}\left\|F_{j}(Q^{(t)},N^{(t)})-\hat{F}_{e,1}\right\|_{F}^{2}.$$ 9:Compute the gradients of $\widehat{\mathcal{L}}_{t}$ with respect to (LQ, LN) by implicit differentiation through the SDP layer. 10:Update (LQ(t), LN(t)) using an SGD step with stepsize ηt.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Remark 6", "weight": 1.0} -->

11:Recover (Q(T), N(T)) from the final factors and return the robust generalized cost pair (Q(T), N(T)). Algorithm 4 Robust Data-Driven Inverse RL via Stochastic Approximation Algorithm 4 fits naturally into the classical stochastic-approximation framework of robbins1951stochastic. Indeed, if we define the parameter vector by then the SGD step in Algorithm 4 can be written as where $g(\theta_{t},w_{t}):=-\nabla_{\theta}\widehat{\mathcal{L}}_{t}$ and $w_{t}$ denotes the random mini-batch of perturbation samples used at iteration $t$. Hence, the randomness in our method comes from the sampled perturbations $\{D_{j}\}$, while the batch loss $\widehat{\mathcal{L}}_{t}$ serves as a stochastic approximation of the expected objective.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Remark 6", "weight": 1.0} -->

Moreover, because $(Q,N)$ are parameterized through $(L_{Q},L_{N})$ with fixed $R=CC^{\top}$, the semidefinite feasibility constraint is enforced automatically, so no explicit projection term is required in our implementation. Therefore, Algorithm 4 is a projected-free SGD instance of stochastic approximation. In particular, if the step sizes satisfy and if the associated mean dynamics $\dot{\theta}=\mathbb{E}_{w}[g(\theta,w)]$ are asymptotically stable at a fixed point $\theta^{\star}$, then classical stochastic-approximation theory implies convergence of the iterates to $\theta^{\star}$ under standard regularity assumptions.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Comparison with Related Data-Driven Inverse RL Methods", "weight": 1.0} -->

This section compares the proposed inverse-RL schemes with representative data-driven approaches in xue2021inverse; lian2022inverse; lian2024inverse; wu2026inverse. The structural comparison is summarized in Fig. 2.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Comparison with Related Data-Driven Inverse RL Methods", "weight": 1.0} -->

Existing data-driven inverse-RL methods can be broadly classified into two-loop and single-loop architectures. In two-loop methods, a forward RL problem is repeatedly solved inside an outer cost-update loop. Single-loop methods simplify this structure by incorporating the weight update step into the value-iteration or policy-iteration loop. In contrast, Algorithms 1--3 proposed in this paper solve the inverse-RL problem after the required regression step through a single convex program and are therefore iteration-free at the Inverse RL stage. Algorithm 4 introduces a loop only because the robust objective is optimized by stochastic approximation.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Comparison with Related Data-Driven Inverse RL Methods", "weight": 1.0} -->

Note that, according to wu2026inverse, the overall computational complexity of the two-loop and single-loop algorithms are $\mathcal{O}\big((\tfrac{n(n+1)}{2}+nm)^{2}N_{1}\big)+\mathcal{O}\big((\tfrac{n(n+1)}{2})^{2}N_{2}\big)$ and $\mathcal{O}\big((n(n+1)+nm)^{2}N_{3}\big),$ respectively, where $N_{1}\geq\tfrac{n(n+1)}{2}+nm$, $N_{2}\geq\tfrac{n(n+1)}{2}$, and $N_{3}\geq n(n+1)+nm$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Comparison with Related Data-Driven Inverse RL Methods", "weight": 1.0} -->

Unlike other existing single-loop methods, the approach in wu2026inverse merges the cost weight update and policy evaluation steps into a single stage by solving an LMI-based optimization problem. The complexity of this step is characterized as $\mathcal{O}(\phi^{2.75}\rho^{1.5}),$ where $\phi=1.5,n(n+1)+2nm$ denotes the number of decision variables and $\rho=3$ is the number of LMI constraints.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Comparison with Related Data-Driven Inverse RL Methods", "weight": 1.0} -->

In our method, Algorithm 1 has $\phi=n(n+1)$ and $\rho=2$. Algorithm 2 has $\phi=\tfrac{n(n+1)}{2}+\tfrac{(n+m)(n+m+1)}{2},\quad\rho=2.$ However, in this case, the number of linear constraints scales with the data size $N_{\mathrm{d}}>\tfrac{(n+m)(n+m+1)}{2}$, which significantly affects the overall complexity. In particular, the dominant cost arises from handling these constraints, leading to a complexity of $\mathcal{O}(\phi^{2}N_{\mathrm{d}}).$ This makes the method computationally expensive, as each interior-point iteration requires processing $N_{\mathrm{d}}$ constraints, similar in structure to solving a large-scale least-squares problem. Although this optimization can become large, it is solved only once and does not require repeated policy/value iterations.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Comparison with Related Data-Driven Inverse RL Methods", "weight": 1.0} -->

For the model-based Algorithm 3, we have $\phi=\tfrac{n(n+1)}{2}+nm$ and $\rho=2$. Additionally, the pseudo-inverse step used to estimate $\hat{M}$ in has complexity $\mathcal{O}((n^{2}+mn)^{2}N_{\mathrm{d}}),$ when computed via SVD golub2013matrix. Since this step is decoupled from the optimization, it can be accelerated using more efficient techniques (see Remark 5), making it more scalable with respect to data compared to the model-free approach.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Comparison with Related Data-Driven Inverse RL Methods", "weight": 1.0} -->

Finally, Algorithm 4 has $\phi=\tfrac{n(n+1)}{2}+nm$ and $\rho=2$ per forward pass. Moreover, as discussed in agrawal2019differentiable, the backward pass obtained by implicit differentiation requires solving a linear system derived from the optimality conditions, and its cost is of the same order as that of the forward pass.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Remark 7", "weight": 1.0} -->

Note that in Algorithm 4, the matrix inversion of $R+B^{\top}P_{j}B$ in the discrete-time gain expression has complexity $\mathcal{O}(m^{3})$ for each forward solve. This cost could be reduced in a continuous-time counterpart of the method, where the optimal gain typically takes the form $K_{j}=R^{-1}(B^{\top}P_{j}+N)$. In that case, the only matrix that must be inverted is $R$, which is fixed and can therefore be computed once in advance and reused throughout the optimization loop.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Remark 7", "weight": 1.0} -->

Overall, the main advantage of the proposed framework is structural simplicity. Algorithms 1--3 remove the repeated inverse-RL policy/value updates that appear in existing two-loop and single-loop methods, while Algorithm 4 introduces iteration only for robust optimization. This preserves the numerical stability of the convex-optimization formulation and yields a simpler computational pipeline than classical iterative inverse-RL schemes.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Simulation", "weight": 1.0} -->

This section validates the proposed methods on the discrete-time power-system example in vamvoudakis2015asymptotically: where $\Delta\zeta$, $\Delta\mathcal{P}_{m}$, $\Delta f_{G}$, and $\Delta P_{c}$ denote the deviations in governor valve position, generator mechanical power output, frequency, and control input, respectively. The expert weighting matrices are chosen as $Q_{e}=I_{3}$ and $R_{e}=1$. The corresponding expert gain is All convex optimization problems are solved in the CVXPY framework with the MOSEK solver, except Algorithm 4, for which the ECOS solver is used.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Nominal cases", "weight": 1.0} -->

In the nominal case, we compare the methods proposed in this paper with the discrete-time inverse-RL algorithm in xue2021inverseQlearning, using a stopping tolerance of $10^{-8}$. The formulations and solve Problem 1, whereas and solve Problem 2. Table 1 reports the runtime and the gain-recovery error $\|\Delta K^{\star}\|_{F}$ for different levels of estimation error in $\hat{K}_{e,1}$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Nominal cases", "weight": 1.0} -->

Table 1 shows that when the estimate $\hat{K}_{e,1}$ is exact, the proposed optimization-based methods recover the expert gain to numerical precision, whereas the benchmark in xue2021inverseQlearning still exhibits a relatively large gain error. As the estimation error increases to $0.1$ and $0.5$, the relaxed model-free formulation remains highly accurate, while the exact formulations become increasingly sensitive to estimation error. In the large-error case $\|\hat{K}_{e,1}-K_{e,1}\|_{F}=2.5$, and become infeasible, whereas the relaxed formulations remain solvable and achieve smaller gain error than the benchmark. These results highlight the benefit of relaxing the gain-matching constraint when the expert-gain estimate is inaccurate.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Perturbed case", "weight": 1.0} -->

We next consider the perturbed system with $D=[1.105\quad-1.702\quad-2.888]$ and $\gamma_{1}=\gamma_{2}=2$. From Lemma 5, the estimated expert gain for this system is Applying Algorithm 3 with $R=1$ yields the following cost weights: The resulting controller achieves $\|K^{\star}_{e,2}-\hat{K}_{e,2}\|=1.6\times 10^{-6}$ and $\|\bar{A}+\bar{B}K^{\star}-F_{e,2}\|=3.8\times 10^{-7}$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Perturbed case", "weight": 1.0} -->

In contrast, the method in xue2021inverseQlearning yields an inverse controller with $\|K^{\star}_{e,2}-\hat{K}_{e,2}\|=10.788$ and $\|\bar{A}+\bar{B}K^{\star}-F_{e,2}\|=3.409$. This large performance gap is expected because, in the perturbed case, the target gain need not correspond exactly to an LQR-optimal controller; it may only be a stabilizing gain. Figure 3 compares the expert trajectories with those of the local system driven by the proposed inverse-RL controller from the same initial condition. The local responses closely follow the expert trajectories for all three states, which confirms that the recovered controller preserves the desired closed-loop behavior despite the perturbation.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Perturbed case", "weight": 1.0} -->

(a) Governor valve position Δζ (b) Generator mechanical power output Δ𝒫m Figure 3: Closed-loop state trajectories in the perturbed case.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Robust design", "weight": 1.0} -->

In this subsection, Algorithm 4 is used to learn a robust generalized cost from randomly generated perturbation matrices $D_{j}$, where each entry is sampled from the Gaussian distribution $\mathcal{N}(0,\sigma=1.0)$. The hyperparameters are chosen as batch size $N_{b}=526$, maximum iteration number $T=7000$, and $R=1$. Figure 4 shows the evolution of the Frobenius norms of $Q$ and $N$, together with the mini-batch mean loss. All three curves approach steady values after around 6000 iterations, indicating convergence of both the learned cost parameters and the training objective.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Robust design", "weight": 1.0} -->

The final robust cost pair obtained after training is To evaluate robustness, we compare the controller induced by the learned cost with the controller obtained from the true expert cost under three perturbation levels, namely $\sigma=1.0$, $\sigma=2.5$, and $\sigma=5.5$. Figure 5 reports the corresponding state trajectories. At the training noise level $\sigma=1.0$, the proposed robust controller exhibits a slightly larger bias in the mean response than the controller derived from the true expert cost, but its trajectory variance is consistently smaller for all three states. This behavior is expected because Algorithm 4 is designed to reduce sensitivity to perturbations rather than to fit a single nominal system exactly.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Robust design", "weight": 1.0} -->

As the perturbation level increases to $\sigma=2.5$ and $\sigma=5.5$, the advantage in variance reduction is preserved, while the mean bias of the robust controller becomes comparable to that of the true expert-cost controller. Hence, in the high-noise regime, the proposed method achieves nearly the same bias as the expert-cost design but with noticeably smaller dispersion.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This paper proposed a convex-optimization framework for data-driven inverse reinforcement learning of discrete-time linear systems with model uncertainty. For nominal systems, we derived a model-based semidefinite characterization of inverse optimality and a relaxed convex formulation that recovers an equivalent cost matrix together with a stabilizing controller from expert trajectory data. We then developed a model-free, off-policy reformulation by replacing the unknown system matrices with a regressed kernel matrix identified from local input--state data. For uncertain local systems, we showed that a standard LQR cost is generally too restrictive and introduced a generalized LQR formulation with a state--input cross term, which led to a convex data-driven inverse-RL method capable of recovering both a generalized cost pair and a stabilizing controller.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Conclusion", "weight": 1.5} -->

The paper also formulated a robust inverse-RL design problem over a distribution of plant perturbations and solved it using differentiable semidefinite programming and stochastic approximation. Simulation results on a discrete-time power-system example demonstrated accurate recovery of expert closed-loop behavior in both nominal and perturbed settings. In particular, the robust design produced smaller trajectory variance than the controller induced by the true expert cost, while achieving comparable bias in the high-noise regime. Overall, the proposed methods provide a simpler and more numerically stable alternative to classical iterative inverse-RL schemes because they avoid repeated inverse-RL policy/value updates and do not require an initial stabilizing gain. Future work will focus on extensions to output-feedback settings, more general classes of uncertain and nonlinear systems, and stronger theoretical guarantees under noisy data.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Declaration of Competing Interest", "weight": 1.0} -->

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this article.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Data availability", "weight": 1.0} -->

The data that has been used is confidential.
