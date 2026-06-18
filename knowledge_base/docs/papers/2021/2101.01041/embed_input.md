<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Derivative-Free Policy Optimization for Linear Risk-Sensitive and Robust Control Design: Implicit Regularization and Sample Complexity

Topics include Nonconvex optimization, Policy gradients, Reinforcement learning, Multi-agent systems, Safety, Robustness, Attention mechanisms, Sample complexity, Optimization, Control, Learning, Sampling, Design, Multi-agent reinforcement learning, Optimization problem.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Direct policy search serves as one of the workhorses in modern reinforcement learning (RL), and its applications in continuous control tasks have recently attracted increasing attention. In this work, we investigate the convergence theory of policy gradient (PG) methods for learning the linear risk-sensitive and robust controller. In particular, we develop PG methods that can be implemented in a derivative-free fashion by sampling system trajectories, and establish both global convergence and sample complexity results in the solutions of two fundamental settings in risk-sensitive and robust control: the finite-horizon linear exponential quadratic Gaussian, and the finite-horizon linear-quadratic disturbance attenuation problems. As a by-product, our results also provide the first sample complexity for the global convergence of PG methods on solving zero-sum linear-quadratic dynamic games, a nonconvex-nonconcave minimax optimization problem that serves as a baseline setting in multi-agent reinforcement learning (MARL) with continuous spaces. One feature of our algorithms is that during the learning phase, a certain level of robustness/risk-sensitivity of the controller is preserved, which we termed as the implicit regularization property, and is an essential requirement in safety-critical control systems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent years have witnessed the rapid development of reinforcement learning (RL) methods in handling continuous control tasks. Central to the success of RL are policy optimization (PO) methods, including policy gradient (PG), actor-critic, and other variants. Progress reported in the literature has clearly shown an increasing interest in understanding theoretical properties of PO methods for relatively simple baseline problems such as various linear control problems. However, the theory of model-free PO methods on *risk-sensitive/robust* control remains underdeveloped in the literature. Since risk-sensitivity and robustness are important issues for designing safety-critical systems, it is natural to bring up the questions of whether and how model-free PO methods would converge for these continuous control tasks.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our work in this paper is motivated by the above concern, and studies the sample complexity of model-free PG methods on two important baseline problems in risk-sensitive/robust control, namely the linear exponential quadratic Gaussian (LEQG), and the linear quadratic (LQ) disturbance attenuation problems. The former covers a fundamental setting in risk-sensitive control, and the latter is an important baseline for robust control. Based on the well-known equivalence between these problems and LQ dynamic games, we develop a *unified* PO perspective for both. A common feature for the above two problems is that their optimization landscapes are by nature more challenging than that of the linear quadratic regulator (LQR) problem, and existing proof techniques for model-free PG methods are no longer effective due to lack of coercivity of the objective functions. Specifically, when applying PG methods to LQR, the feasible set for the resultant constrained optimization problem is the set of all linear state-feedback controllers that *stabilize* the closed-loop dynamics.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The objective function of LQR is coercive on this feasible set and serves as a barrier function itself, guaranteeing for the PG iterates to stay in the feasible set and converge to the globally optimal controller. For the LEQG and LQ disturbance attenuation problems, the risk-sensitivity/robustness conditions have reshaped the feasible set in a way that the objective function becomes non-coercive, i.e. the objective value can remain finite while approaching the boundary. The objective is no longer a barrier function, and new proof techniques are needed to show that model-free PG iterates will stay in the feasible set. This is significant for safety-critical control systems with model uncertainty, as the iterates' feasibility here is equivalent to *risk-sensitivity/robustness* of the controller (cf. Remark 3.9), and the failure to preserve robustness during learning can cause catastrophic effects, e.g., destabilizing the system in face of disturbances.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The most relevant result was developed, which proposes implicit regularization (IR) arguments to show the convergence of several PG methods on the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control design problem (which can be viewed as the infinite-horizon variant of the LQ disturbance attenuation problem studied in this paper). The main finding there is that two specific PG search directions (with perfect model information) are automatically biased towards the interior of the robustness-related feasible set. In, it is emphasized that IR is a feature of both the *problem* and the *algorithm*, contrasting to that the stability-preserving nature of PG methods for LQR problems is based on the barrier function property of the objective and hence is *algorithm-agnostic*. Although the idea of IR is relevant to PO problems with non-coercive objective functions, the arguments in only apply to the setting with a *known* model, since they rely on a specialized perturbation technique which may potentially generate arbitrarily small "margins". However, in the model-free setting, a uniform margin is required for provable tolerance of statistical errors.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, for the LEQG and LQ disturbance attenuation problems, we overcome the above margin issue and obtain the first IR result in the model-free setting. This enables the first model-free PG method that provably solves these control problems with a finite number of samples. We highlight our contributions as follows.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contributions", "weight": 1.0} -->

We provide the first sample complexity results for model-free PG methods for solving linear control problems with risk-sensitivity/robustness concerns (the LEQG and LQ disturbance attenuation problems), which was viewed as an important open problem in the seminal work. From the robust control perspective, one feature of our algorithms is that, during the learning process, a certain level of *robustness/risk-sensitivity* of the controller is proved to be preserved. This has generalized the results in with a known model, and has thus enabled the finite-sample convergence guarantees of PO methods for risk-sensitive/robust control design. Our algorithms and sample complexity results also address two-player zero-sum LQ dynamic games in the finite-horizon time-varying setting, which are among the first sample complexity results for the global convergence of policy-based methods for competitive multi-agent RL. Second, in the context of minimax optimization, our results address a class of nonconvex-nonconcave minimax constrained optimization problems, using *zeroth-order* multi-step gradient descent-ascent methods.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contributions", "weight": 1.0} -->

Finally, part of our results provide the sample complexity analysis for PG methods that solve the finite-horizon time-varying LQR problem with system noises and a possibly *indefinite* state-weighting matrix.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Notations", "weight": 1.0} -->

For a square matrix $X$ of proper dimension, we use $\text{Tr}{(X)}$ to denote its trace. We also use $\| X\|$ and ${\| X\|}_{F}$ to denote, respectively, the operator norm and the Frobenius norm of $X$. If $X$ is further symmetric, we use $X > 0$ to denote that $X$ is positive definite. Similarly, $X \geq 0$, $X \leq 0$, and $X < 0$ are used to denote $X$ being positive semi-definite, negative semi-definite, and negative definite, respectively. Further, again for a symmetric matrix $X$, $\lambda_{\min}{(X)}$ and $\lambda_{\max}{(X)}$ are used to denote, respectively, the smallest and the largest eigenvalues of $X$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Notations", "weight": 1.0} -->

Moreover, we use ${\langle X,Y\rangle}:={\text{Tr}{({X^{\top}Y})}}$ to denote the standard matrix inner product and use $diag{(X_{0},\cdots,X_{N})}$ to denote the block-diagonal matrix with $X_{0},\cdots,X_{N}$ on the diagonal block entries. In the case where $X_{0} = X_{1} = \cdots = X_{N} = X$, we further denote it as $diag{(X^{N})}$. We use $x \sim {\mathcal{N}{(\mu,\Sigma)}}$ to denote a Gaussian random variable with mean $\mu$ and covariance $\Sigma$ and use $\| v\|$ to denote the Euclidean norm of a vector $v$. Lastly, we use $\mathbf{I}$ and $\mathbf{0}$ to denote the identity and zero matrices with appropriate dimensions.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Linear Exponential Quadratic Gaussian", "weight": 1.0} -->

We first consider a fundamental setting of risk-sensitive optimal control, known as the LEQG problem, in the finite-horizon setting.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Linear Exponential Quadratic Gaussian", "weight": 1.0} -->

where $x_{t} \in {\mathbb{R}}^{m}$ represents the system state; $u_{t} \in {\mathbb{R}}^{d}$ is the control input; $w_{t} \in {\mathbb{R}}^{m}$ is an independent (across time) Gaussian random noise drawn from $w_{t} \sim {\mathcal{N}{(\mathbf{0},W)}}$ for some $W > 0$; the initial state $x_{0} \sim {\mathcal{N}{(\mathbf{0},X_{0})}}$ is a Gaussian random vector for some $X_{0} > 0$, independent of the sequence $\{ w_{t}\}$; and $A_{t}$, $B_{t}$ are time-varying system matrices with appropriate dimensions. The objective function is given by

<!-- chunk {"id": "body-0014", "role": "body", "section": "Linear Exponential Quadratic Gaussian", "weight": 1.0} -->

where $Q_{t} \geq 0$ and $R_{t} > 0$, for all $t \in {\{ 0,\cdots,{N - 1}\}}$, and $Q_{N} \geq 0$ are symmetric weighting matrices; and $\beta > 0$ is a parameter capturing the degree of risk-sensitivity, which is upper-bounded by some $\beta^{\ast} > 0$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "LQ Disturbance Attenuation", "weight": 1.0} -->

Second, we introduce the *optimal* LQ disturbance attenuation problem, again for finite-horizon settings, with time-varying (deterministic) dynamical systems described by

<!-- chunk {"id": "body-0016", "role": "body", "section": "LQ Disturbance Attenuation", "weight": 1.0} -->

where $\gamma^{\ast} = \sqrt{{(\beta^{\ast})}^{- 1}} > 0$ is the *optimal* (*minimax*) level of disturbance attenuation at the output, and recall that $\beta^{\ast}$ is the upper bound for the risk-sensitivity parameter in LEQG. It is known that under closed-loop perfect-state information pattern, the existence of a sequence $\{\mu_{t}^{\ast}\}$, $t \in {\{ 0,\cdots,{N - 1}\}}$, is always guaranteed and $\mu_{t}^{\ast}$ is linear state-feedback, i.e., ${\mu^{\ast}{(h_{t})}} = {- {K_{t}^{\ast}x_{t}}}$ (; Theorem 3.5).

<!-- chunk {"id": "body-0017", "role": "body", "section": "LQ Disturbance Attenuation", "weight": 1.0} -->

The problem (2.5) can be challenging to solve to the optimum. Moreover, in practice, due to the inevitable uncertainty in modeling the system, the robust controller that achieves the optimal attenuation level can be too sensitive to the model uncertainty to use. Hence, a reasonable surrogate of the optimal LQ disturbance attenuation problem is the following: Given a $\gamma > \gamma^{\ast}$, find a control policy $\mu_{t} = {- {K_{t}x_{t}}}$, for all $t \in {\{ 0,\cdots,{N - 1}\}}$, that solves

<!-- chunk {"id": "body-0018", "role": "body", "section": "LQ Disturbance Attenuation", "weight": 1.0} -->

where ${\overset{\sim}{P}}_{K_{t + 1}}:={P_{K_{t + 1}} + {P_{K_{t + 1}}{({{\gamma^{2}{\mathbf{I}}} - {D_{t}^{\top}P_{K_{t + 1}}D_{t}}})}^{- 1}P_{K_{t + 1}}}}$. Then, two upper bounds of $\mathcal{J}$ and their corresponding PGs can be expressed in terms of solutions to (2.7) (if exist). In particular, (2.8) below is closely related to the objective function of LEQG in (2.1), and (2.9) is connected to the objective function of zero-sum LQ dynamic games to be introduced shortly.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Remark 2.3", "weight": 1.0} -->

It seems tempting to tackle LEQG or the LQ disturbance attenuation problem directly using derivative-free PG methods, e.g., vanilla PG or natural PG methods by sampling the system trajectories as. However, there are several challenges. First, when attempting to sample the LEQG objective (2.1) using system trajectories (and then to estimate PGs), the bias of gradient estimates can be difficult to control uniformly with a fixed sample size per iterate, as the $\log$ function is not globally Lipschitz^33^3One workaround for mitigating this bias might be to remove the $\log$ operator in the objective (2.1), and only minimize the terms after the ${\mathbb{E}}{\exp{( \cdot )}}$ function. However, it is not clear yet if derivative-free methods provably converge for this objective, as $\exp$ function is neither globally smooth nor Lipschitz. We have left this direction in our future work, as our goal in the present work is to provide a unified way to solve all three classes of problems..

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 2.3", "weight": 1.0} -->

Moreover, for the vanilla PG method, even with exact PG accesses, the iterates may not preserve a certain level of risk-sensitivity/disturbance attenuation, i.e., remain feasible, along the iterations, which can make the disturbance input drive the cost to arbitrarily large values (see the numerical examples in for the infinite-horizon LTI setting). This failure will only be exacerbated in the derivative-free setting with accesses to only noisy PG estimates. Lastly, developing a derivative-free natural PG method (which we will show in §3.3 that it can preserve a prescribed attenuation level along the iterations) is also challenging, because the expressions of $\Sigma_{K_{t}}$ in Lemmas 2.1 and 2.2 cannot be sampled from system trajectories directly. Therefore, the game-theoretic approach to be introduced next is rather one workaround.

<!-- chunk {"id": "body-0021", "role": "body", "section": "An Equivalent Dynamic Game Formulation", "weight": 1.0} -->

Lastly, and more importantly, we describe an equivalent dynamic game formulation to the LEQG and the LQ disturbance attenuation problems introduced above. Under certain conditions to be introduced in Lemma 2.6, the saddle-point gain matrix of the minimizing player in the dynamic game (if exists) also addresses the LEQG and the LQ disturbance attenuation problem, providing an alternative route to overcome the challenges reported in Remark 2.3. Specifically, we consider a zero-sum LQ stochastic dynamic game (henceforth, game) model with closed-loop perfect-state information pattern, which can also be viewed as a benchmark setting of MARL for two competing agents, as the role played by LQR for single-agent RL. The linear time-varying system dynamics follow

<!-- chunk {"id": "body-0022", "role": "body", "section": "An Equivalent Dynamic Game Formulation", "weight": 1.0} -->

The independent process noises are denoted by $\xi_{t} \sim \mathcal{D}$ and $A_{t}$, $B_{t}$, $D_{t}$ are system matrices with proper dimensions. Further, we assume $x_{0} \sim \mathcal{D}$ to be independent of the process noises, and the distribution $\mathcal{D}$ has zero mean and a positive-definite covariance. We also assume that ${{\| x_{0}\|},{\|\xi_{t}\|}} \leq \vartheta$, for all $t \in {\{ 0,\cdots,{N - 1}\}}$, almost surely, for some constant $\vartheta$^55^5The assumption on the boundedness of distribution is only for ease of analysis. Extensions to sub-Gaussian distributions are standard and do not affect the sample complexity result, as noted.. The goal of the minimizing (resp. maximizing) player is to minimize (resp.

<!-- chunk {"id": "body-0023", "role": "body", "section": "An Equivalent Dynamic Game Formulation", "weight": 1.0} -->

maximize) a quadratic objective function, namely to solve the zero-sum game

<!-- chunk {"id": "body-0024", "role": "body", "section": "An Equivalent Dynamic Game Formulation", "weight": 1.0} -->

where $Q_{t} \geq 0$, ${R_{t}^{u},R_{t}^{w}} > 0$ are symmetric weighting matrices and the system transitions follow (2.11). Whenever the solution to (2.12) exists such that the $\inf$ and $\sup$ operators in (2.12) are interchangeable, then the value (2.12) is the *value* of the game, and the corresponding policies of the players are known as saddle-point policies. To characterize the solution to (2.12),

<!-- chunk {"id": "body-0025", "role": "body", "section": "An Equivalent Dynamic Game Formulation", "weight": 1.0} -->

where $P_{t + 1}^{\ast}$, $t \in {\{ 0,\cdots,{N - 1}\}}$, is the sequence of p.s.d. matrices generated by (2.13). We next introduce a standard assumption that suffices to ensure the existence of the value of the game, following from Theorem 3.2 of and Theorem 6.7 of.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 2.5", "weight": 1.0} -->

(Unique Feedback Nash (Saddle-point) Equilibrium) By, Assumption 2.4 is sufficient to guarantee the *existence* of feedback Nash (equivalently, saddle-point) equilibrium in zero-sum LQ dynamic games (game), under which it is also unique. Besides sufficiency, Assumption 2.4 is also "almost necessary", and "quite tight" as noted in Remark 6.8 of. In particular, if the sequence of matrices $R_{t}^{w} - {D_{t}^{\top}P_{t + 1}^{\ast}D_{t}}$ for $t \in {\{ 0,\cdots,{N - 1}\}}$ in Assumption 2.4 admits any negative eigenvalues, then the upper value of the game becomes unbounded.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 2.5", "weight": 1.0} -->

In the context of LEQG and LQ disturbance attenuation (LQDA), suppose we set the system parameters of LEQG, LQDA, and game according to Lemma 2.6, and in particular set $\beta^{- 1}\mathbf{I}$ in LEQG, $\gamma^{2}\mathbf{I}$ in LQDA, and $\mathbf{R}^{w}$ in the game to be the same. Then these three problems are equivalent as far as their optimum solutions go (which is what we seek). Due to this equivalence, Assumption 2.4 is a sufficient and "almost necessary" condition for the existence of a solution to the equivalent LEQG/LQDA.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 2.5", "weight": 1.0} -->

Specifically, if the sequence of matrices $R_{t}^{w} - {D_{t}^{\top}P_{t + 1}^{\ast}D_{t}}$ for $t \in {\{ 0,\cdots,{N - 1}\}}$ in Assumption 2.4 admits any negative eigenvalues, then no state-feedback controller can achieve a $\gamma$-level of disturbance attenuation in the equivalent LQDA, and no state-feedback controller can achieve a $\beta$-degree of risk-sensitivity in the equivalent LEQG.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 2.5", "weight": 1.0} -->

Lastly, we formally state the well-known equivalence conditions between LEQG, LQ disturbance attenuation, and zero-sum LQ stochastic dynamic games in the following lemma, and provide a short proof in §A.4.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Policy Gradient Methods", "weight": 1.0} -->

For ease of analysis, we first present the following compact notations for the game.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Policy Gradient Methods", "weight": 1.0} -->

We re-derive the earlier game formulation with linear state-feedback policies for the players using compact notations in §A.1 and show that they are equivalent to the recursive ones in §2.3. Now, using the compact notations, we develop PG methods with access to the *exact* policy gradient that provably converges to the Nash equilibrium of the game, ${({\mathbf{K}}^{\ast},{\mathbf{L}}^{\ast})} \in {{{\mathcal{S}{(d,m,N)}} \times \mathcal{S}}{(n,m,N)}}$, where $\mathcal{S}{(d,m,N)}$ and $\mathcal{S}{(n,m,N)}$ are the subspaces that we confine our searches of $\mathbf{K}$ and $\mathbf{L}$ to, respectively.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Policy Gradient Methods", "weight": 1.0} -->

In particular, we only search over ${\mathbf{K}} \in {\mathbb{R}}^{{{Nd} \times {({N + 1})}}m}$ and ${\mathbf{L}} \in {\mathbb{R}}^{{{Nn} \times {({N + 1})}}m}$, and ${\mathbf{K}},{\mathbf{L}}$ satisfy the sparsity patterns shown in (3.1), as they suffice to attain the Nash equilibrium. The degrees of freedom of $\mathcal{S}{(d,m,N)}$ and $\mathcal{S}{(n,m,N)}$ are $d \times m \times N$ and $n \times m \times N$, respectively.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Double-Loop Scheme", "weight": 1.0} -->

We start by introducing our *double-loop* update scheme. Specifically, we first fix an outer-loop control gain matrix $\mathbf{K}$, and solve for the optimal $\mathbf{L}$ by maximizing the objective $\mathcal{G}{({\mathbf{K}}, \cdot )}$ over ${\mathbf{L}} \in {\mathcal{S}{(n,m,N)}}$. We denote the inner-loop solution for a fixed $\mathbf{K}$, if exists, by ${\mathbf{L}}{({\mathbf{K}})}$. After obtaining the inner-loop solution, the outer-loop $\mathbf{K}$ is then updated to minimize the objective $\mathcal{G}{({\mathbf{K}},{{\mathbf{L}}{({\mathbf{K}})}})}$ over ${\mathbf{K}} \in {\mathcal{S}{(d,m,N)}}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Double-Loop Scheme", "weight": 1.0} -->

For each fixed $\mathbf{K}$, the inner-loop is an *indefinite* LQR problem where the state-weighting matrix, i.e., ${- {\mathbf{Q}}} - {{\mathbf{K}}^{\top}{\mathbf{R}}^{u}{\mathbf{K}}}$, is not p.s.d. Our goal is to find, via PG methods, the optimal linear state-feedback controller ${{\mathbf{w}}{({\mathbf{K}})}} = {- {{\mathbf{L}}{({\mathbf{K}})}{\mathbf{x}}}}$, which suffices to attain the optimal performance for the inner loop, whenever the objective function $\mathcal{G}{({\mathbf{K}}, \cdot )}$ admits a finite upper bound value (depending on the choice of the outer-loop $\mathbf{K}$).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Double-Loop Scheme", "weight": 1.0} -->

We formally state the precise condition for the solution to the inner-loop maximization problem to be *well-defined* as follows, with its proof being deferred to §A.7.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 3.4", "weight": 1.0} -->

(Double-Loop Scheme) Our double-loop scheme, which has also been used before, is pertinent to the descent-multi-step-ascent scheme and the gradient descent-ascent (GDA) scheme with two-timescale stepsizes for solving nonconvex-(non)concave minimax optimization problems, with the number of multi-steps of ascent going to infinity, or the ratio between the fast and slow stepsizes going to infinity (the $\tau$-GDA scheme with $\tau\rightarrow\infty$ ). Another variant is the alternating GDA (AGDA) scheme, which has been investigated in to address nonconvex-nonconcave problems with two-sided PL condition. However, unlike this literature, one key condition for establishing convergence, the *global smoothness* of the objective function, does not hold in our control setting with *unbounded* decision spaces and objective functions. In fact, as per Lemma 3.3, a non-judicious choice of $\mathbf{K}$ may lead to an undefined inner-loop maximization problem with unbounded objective.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 3.4", "weight": 1.0} -->

Hence, one has to carefully control the update-rule here, to ensure that the iterates do not yield unbounded/undefined values along iterations. As we will show in §5.4, it is not hard to construct cases where descent-multi-step-ascent/AGDA/$\tau$-GDA diverges even with infinitesimal stepsizes, similar to the negative results reported in the infinite-horizon setting. These results suggest that it seems challenging to provably show that other candidate update schemes converge to the global NE in zero-sum LQ games, except the double-loop one, as we will show next.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Optimization Landscape", "weight": 1.0} -->

For a fixed $\mathbf{K}$, the optimization landscape of the inner-loop subproblem is summarized in the following lemma, with its proof being deferred to §A.8.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Update Rules and Global Convergence", "weight": 1.0} -->

In this section, we introduce three PG-based update rules. We use ${l,k} \geq 0$ to represent the iteration indices of the inner- and outer-loop updates, respectively, and we additionally define

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 3.9", "weight": 1.0} -->

(Preserving the Robustness of $\mathbf{K}_{0}$) Suppose that the initial control gain matrix satisfies $\mathbf{K}_{0} \in \mathcal{K}$. Then Lemma 2.6 shows that $\mathbf{K}_{0}$ is the control gain matrix that attains a $\gamma$-level of disturbance attenuation. By the implicit regularization property in Theorem 3.8, every iterate $\mathbf{K}_{k} \in \mathcal{K}$ for all $k \geq 0$ following the NPG (3.19) or the GN (3.20) update rules will thus preserve this $\gamma$-level of disturbance attenuation throughout the policy optimization (learning) process. Theorem 3.8 thus provides some provable robustness guarantees for two specific policy search directions, (3.19) and (3.20), which is important for safety-critical control systems in the presence of adversarial disturbances, since otherwise, the system performance index can be driven to arbitrarily large values.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Remark 3.9", "weight": 1.0} -->

Based on Theorem 3.8, we now establish the convergence result for the outer loop.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Derivative-Free Policy Gradient Methods", "weight": 1.0} -->

We present the sample complexity of our double-loop algorithm, when the exact PG is not accessible, and can only be estimated through samples of system trajectories. In particular, we propose a zeroth-order NPG (ZO-NPG) algorithm with a (zeroth-order) maximization oracle that approximately solves the inner-loop subproblem (cf. Algorithms 1 and 2). In the following Remark, we comment on how to construct Algorithms 1 and 2 when explicit knowledge on the system parameters is not available.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

When solving LEQG and LQ disturbance attenuation (LQDA) problems using the proposed double-loop derivative-free PG methods (cf. Algorithms 1 and 2), we exploited the equivalence relationships in Lemma 2.6 to construct and solve an equivalent zero-sum LQ game. We comment on how to construct such an equivalent game problem in the model-free setting where only oracle-level accesses to the LEQG and LQDA models are available.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

Suppose that one would like to solve the LQDA problem by solving the equivalent zero-sum game; then, the only information needed is oracle-level accesses to the LQDA model (cf. §2.2). In particular, for a fixed sequence of gains $K_{t}$ and any sequence of disturbances $w_{t}$, we assume that this LQDA oracle can return the $\| z\|$ as defined in §2.2. Then, the LQDA oracle with an additionally injected sequence of independent Gaussian noise (with any positive definite covariance matrix) suffices to serve as the oracle for our double-loop derivative-free PG algorithms (for the stochastic game). Therefore, no explicit knowledge on the system parameters ($A_{t}$, $B_{t}$, $D_{t}$, $C_{t}$, $E_{t}$, $\gamma$) is needed.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

However, if one would like to solve the LEQG problem by solving an equivalent zero-sum game, one will need knowledge of $W$ (to build-up the black-box sampling oracle/simulator, but still, the exact value of $W$ is not revealed to the learning agent) in addition to oracle-level accesses to the original LEQG model (cf. §2.1). Also, explicit knowledge of the parameters ($A_{t}$, $B_{t}$, $Q_{t}$, $R_{t}$, $\beta$) is not required. We would like to note that the assumption on the knowledge (and/or the availability of the estimate) of $W$ is reasonable for a large family of control applications where system dynamics and disturbance can be studied separately. For example, consider the risk-sensitive control of a wind turbine. The turbine dynamics and the wind information can be gathered separately. One can identify $W$ by looking at the past wind data. Similar situations hold for many aerospace applications where the properties of process noise (e.g. wind gust) can be estimated beforehand.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Inner-Loop Maximization Oracle", "weight": 1.0} -->

Sample complexities of zeroth-order PG algorithms for solving standard infinite-horizon LQR have been investigated in both discrete-time and continuous-time settings. Our inner-loop maximization oracle extends the sample complexity result to finite-horizon time-varying LQR with system noises and a possibly *indefinite* state-weighting matrix.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Inner-Loop Maximization Oracle", "weight": 1.0} -->

where $\eta > 0$ is the stepsize to be chosen, $l \in {\{ 0,\cdots,{L - 1}\}}$ is the iteration index, ${\overline{\nabla}}_{\mathbf{L}}\mathcal{G}{({\mathbf{K}},{\mathbf{L}})}$ and ${\overline{\Sigma}}_{{\mathbf{K}},{\mathbf{L}}}$ are the noisy estimates of ${\nabla_{\mathbf{L}}\mathcal{G}}{({\mathbf{K}},{\mathbf{L}})}$ and $\Sigma_{{\mathbf{K}},{\mathbf{L}}}$, respectively, obtained through zeroth-order oracles. The procedure of our inner-loop maximization oracle is presented in Algorithm 1 and we formally establish its sample complexity in the following theorems.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Outer-Loop ZO-NPG", "weight": 1.0} -->

where $\alpha > 0$ is the stepsize, $k \geq 0$ is the iteration index, and ${\overline{\nabla}}_{\mathbf{K}}\mathcal{G}{({\mathbf{K}},{\overline{\mathbf{L}}{({\mathbf{K}})}})}$ and ${\overline{\Sigma}}_{{\mathbf{K}},{\overline{\mathbf{L}}{({\mathbf{K}})}}}$ are the estimated PG and state correlation matrices, obtained from Algorithm 2. Similar to the modification in §4.1, we estimate the correlation matrix $\overline{\Sigma}{({\mathbf{K}},{{\mathbf{L}}{({\mathbf{K}})}})}$ using the state sequence generated by the *unperturbed* gain matrices,

<!-- chunk {"id": "body-0049", "role": "body", "section": "Outer-Loop ZO-NPG", "weight": 1.0} -->

$({\mathbf{K}},{\overline{\mathbf{L}}{({\mathbf{K}})}})$, to avoid the estimation bias induced by the perturbations on the gain matrices.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Outer-Loop ZO-NPG", "weight": 1.0} -->

In the following theorem, whose proof is deferred to §A.15 and a short sketch is provided below, we first prove that the implicit regularization studied in Theorem 3.8 also holds in the derivative-free setting, with high probability.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Simulations", "weight": 1.0} -->

In this section, we provide simulation results to complement our theories. In particular, we present convergence (divergence) results in the following four scenarios where we apply PG updates in Algorithms 1 and 2 to solve a finite-horizon zero-sum LQ dynamic game with time-invariant system parameters: (i) double-loop update scheme with both the inner- and outer-loop solved exactly; (ii) double-loop scheme with the inner-loop solved in the derivative-free scheme by sampling system trajectories while the outer-loop solved exactly; (iii) double-loop scheme with the inner-loop solved exactly while the outer-loop solved in the derivative-free scheme by sampling system trajectories; (iv) descent-multi-step-ascent/AGDA/$\tau$-GDA with exact gradient accesses diverge. Subsequently, we extend our numerical experiments to a setting with *time-varying* system parameters in §5.5, and demonstrate the convergence results of double-loop PG updates.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Simulations", "weight": 1.0} -->

Simulation Setup. All the experiments are executed on a desktop computer equipped with a 3.7 GHz Hexa-Core Intel Core i7-8700K processor with Matlab R2019b. The device also has two 8GB 3000MHz DDR4 memories and a NVIDIA GeForce GTX 1080 8GB GDDR5X graphic card. In all settings except the one used in §5.5, we set the horizon of the problem to $N = 5$ and test a linear time-invariant system with the set of system matrices being $A_{t} = A$, $B_{t} = B$, $D_{t} = D$, $Q_{t} = Q$, $R_{t}^{u} = R^{u}$, and $R_{t}^{w} = R^{w}$, where $R^{w} = {5 \cdot {\mathbf{I}}}$ and

<!-- chunk {"id": "body-0053", "role": "body", "section": "Exact Double-Loop Updates", "weight": 1.0} -->

Case 1: We demonstrate in Figure 4 the convergence of three update combinations, namely PG-NPG, NPG-NPG, and GN-GN, for the inner and outer loop, respectively. The stepsizes are chosen to be ${(\eta,\alpha)} = {({1 \times 10^{- 4}},{3 \times 10^{- 6}})}$ for PG-NPG, ${(\eta,\alpha)} = {(0.0635,{3 \times 10^{- 6}})}$ for NPG-NPG, and ${(\eta,\alpha)} = {(0.5,{5 \times 10^{- 4}})}$ for GN-GN. Also, we require the approximate inner-loop solution to have the accuracy of $\epsilon_{1} = 0.001$. As shown in the top of Figure 4, the double-loop algorithm with all three update combinations successfully converges to the unique Nash equilibrium of the game.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Exact Double-Loop Updates", "weight": 1.0} -->

Also, the sequence ${\{{\lambda_{\min}{({\mathbf{H}}_{{\mathbf{K}}_{k},{{\mathbf{L}}{({\mathbf{K}}_{k})}}})}}\}}_{k \geq 0}$ is monotonically non-decreasing, which matches the implicit regularization property we introduced in Theorem 3.8 for the outer-loop NPG and GN updates. As ${\mathbf{K}}_{0}^{1} \in \mathcal{K}$, we can guarantee that all future iterates will stay inside $\mathcal{K}$. The convergences of the average gradient norms with respect to both $\mathbf{L}$ and $\mathbf{K}$ are also presented in the bottom of Figure 4.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Exact Double-Loop Updates", "weight": 1.0} -->

Case 2: When the initial gain matrix ${\mathbf{K}}_{0}^{2}$ is closer to the boundary of $\mathcal{K}$, one non-judicious update could easily drive the gain matrix outside of $\mathcal{K}$. In this case, we present two combinations of updates, namely NPG-NPG and GN-GN, for the inner and outer loop, respectively. We use the stepsizes ${(\eta,\alpha)} = {(0.0635,{2.48 \times 10^{- 7}})}$ for NPG-NPG and ${(\eta,\alpha)} = {(0.5,{2.5 \times 10^{- 4}})}$ for GN-GN. Similarly, we set $\epsilon_{1} = 0.001$. The convergence patterns presented in Figure 5 are similar to those of Case 1.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Derivative-Free Inner-Loop Oracles", "weight": 1.0} -->

We provide two sets of experiments to validate Theorems 4.2 and 4.3. We consider the same example as the one in §5.1, but using derivative-free updates (4.1)-(4.2) by sampling system trajectories to approximately solve the inner-loop subproblem, as proposed in §4.1. Note that the inner-loop subproblem is essentially an indefinite LQR, as introduced in §3. The outer-loop problem is solved using the exact NPG update (3.19). Note that according to Theorem 4.5, one can also use the outer-loop ZO-NPG (4.3) together with the inner-loop derivative-free updates to achieve the same convergence pattern. However, we use an exact outer-loop update, as it suffices to illustrate our idea here and also has better computational efficiency.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Derivative-Free Inner-Loop Oracles", "weight": 1.0} -->

Inner-Loop ZO-PG: When we use the inner-loop ZO-PG update (4.1) in Algorithm 1, we choose $M_{1} = 10^{6}$ and $r_{1} = 1$. Moreover, we set the stepsizes of the inner-loop ZO-PG and the outer-loop exact NPG to be ${(\eta,\alpha)} = {({8 \times 10^{- 3}},{4.5756 \times 10^{- 4}})}$, respectively. The desired accuracy level of the double-loop algorithm is picked to be ${(\epsilon_{1},\epsilon_{2})} = {(0.8,0.5)}$. As shown in the left of Figure 6, the inner-loop ZO-PG (4.2) successfully converges for every fixed outer-loop update, validating our results in Theorem 4.2. Also, the double-loop algorithm converges to the unique Nash equilibrium of the game.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Derivative-Free Inner-Loop Oracles", "weight": 1.0} -->

Inner-Loop ZO-NPG: When the inner-loop subproblem is solved via the ZO-NPG update (4.2), we choose the same $M_{1},r_{1},\alpha,\epsilon_{1},\epsilon_{2}$ as the ones used in the inner-loop ZO-PG update but in contrast we set $\eta = {5 \times 10^{- 2}}$. Similar convergence patterns can be observed in the right of Figure 6.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Derivative-Free Outer-Loop NPG", "weight": 1.0} -->

We set $\Sigma_{0} = {0.05 \cdot {\mathbf{I}}}$. We present convergence results following the initial gain matrix ${\mathbf{K}}_{0} = \left\lbrack {diag{(K^{5})}\mathbf{0}_{15 \times 3}} \right\rbrack$, where $K = \begin{bmatrix}
\end{bmatrix}$ and ${\lambda_{\min}\left( {\mathbf{H}}_{{\mathbf{K}}_{0},{{\mathbf{L}}{({\mathbf{K}}_{0})}}} \right)} = 3.2325$. The convergence of Algorithm 2 is implemented for two cases, with the inner-loop oracle being implemented using (i) the exact solution as computed by (3.10); and (ii) the approximate inner-loop solution following the exact NPG update (3.16).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Derivative-Free Outer-Loop NPG", "weight": 1.0} -->

As proved by Theorems 4.2 and 4.3, the inner loop can also be solved approximately using either ZO-PG or ZO-NPG updates, which has been verified via the simulation results presented in §5.2. The parameters of Algorithm 2 in both cases are set to $M_{2} = {5 \times 10^{5}}$, $r_{2} = 0.08$, ${(\eta,\alpha)} = {(0.1,{4.67 \times 10^{- 5}})}$, and ${(\epsilon_{1},\epsilon_{2})} = {(10^{- 4},0.8)}$. Figure 7 illustrates the behaviors of the objective function and the smallest eigenvalue of ${\mathbf{H}}_{{\mathbf{K}},{\mathbf{L}}}$ following the double-loop update scheme.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Derivative-Free Outer-Loop NPG", "weight": 1.0} -->

It is shown that iterates of the outer-loop gain matrix ${\{{\mathbf{K}}_{k}\}}_{k \geq 0}$ stay within the feasible set $\mathcal{K}$ along with the double-loop update, which preserves a certain disturbance attenuation level in the view of Remark 3.9. Moreover, in both cases, we have Algorithm 2 converging sublinearly to the unique Nash equilibrium.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Divergent Cases", "weight": 1.0} -->

As noted in Remark 3.4, it is unclear yet if descent-multi-step-ascent, AGDA, or $\tau$-GDA, where $\tau = {\eta/\alpha}$, can converge globally to the Nash equilibrium in our setting. In this section, we present some scenarios where descent-multi-step-ascent, AGDA, and $\tau$-GDA diverges even with infinitesimal stepsizes. We use the same example as §5.1 and initialize ${\mathbf{K}}_{0}^{4},{\mathbf{L}}_{0}^{4}$ to be time-invariant such that $K_{0,t}^{4} = K_{0}^{4} = \begin{bmatrix}
\end{bmatrix}$ and $L_{0,t}^{4} = L_{0}^{4} = \begin{bmatrix}
\end{bmatrix}$ for all $t$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Divergent Cases", "weight": 1.0} -->

Note that in descent-multi-step-ascent/AGDA/$\tau$-GDA, the maximizing problem with respect to $\mathbf{L}$ for a fixed $\mathbf{K}$ is no longer solved to a high accuracy for each iteration of the updates on $\mathbf{K}$. Thus, we can relax the constraint ${\mathbf{K}} \in \mathcal{K}$ since the maximizing player will not drive the cost to $\infty$ in such iterates under descent-multi-step-ascent/AGDA/$\tau$-GDA. Figure 8 illustrates the behaviors of the objective and the gradient norms with respect to $\mathbf{K}$ and $\mathbf{L}$ when applying alternating natural GDA (ANGDA), $\tau$-natural GDA ($\tau$-NGDA), and descent-multi-step-ascent with updates (3.16) and (3.19) to our problem.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Divergent Cases", "weight": 1.0} -->

The stepsizes for the ANGDA are chosen to be infinitesimal such that $\eta = \alpha = {1.7319 \times 10^{- 11}}$. However, we can still observe the diverging patterns from the top row of Figure 8, even with such tiny stepsizes. Further, we test the same example with the same initialization but use $\tau$-NGDA with $\tau = 10^{3}$. That is, $\eta = {10^{3} \cdot \alpha}$. In such case, it is shown in the middle row of Figure 8 that diverging behaviors still appear. Whether there exists a finite timescale separation $\tau^{\ast}$, similar to the one proved, such that $\tau$-GDA type algorithms with $\tau \in {(\tau^{\ast},\infty)}$ provably converge to the unique Nash equilibrium in our setting requires further investigation, and is left as our future work.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Divergent Cases", "weight": 1.0} -->

Lastly, we present a case where descent-multi-step-ascent with updates following (3.16) and (3.19) diverges. The stepsizes of the inner-loop and the outer-loop updates are chosen to be $\eta = \alpha = {1.7319 \times 10^{- 9}}$ and we run 10 iterations of (3.16) for each iteration of (3.19). The bottom row of Figure 8 demonstrates the diverging behaviors of this update scheme.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Time-Varying Systems", "weight": 1.0} -->

and set $R^{w} = {10 \cdot {\mathbf{I}}}$. Rest of the parameters are set to the same as in (5.1). The horizon of the problem is again set to $N = 5$ and we initialize our algorithm using $K_{0,t}^{5} = K_{0}^{5} = \begin{bmatrix}

<!-- chunk {"id": "body-0067", "role": "body", "section": "Time-Varying Systems", "weight": 1.0} -->

We demonstrate in Figure 9 the convergence of exact double-loop NPG updates. The stepsizes of the inner-loop and the outer-loop updates are chosen to be ${(\eta,\alpha)} = {(0.0097,{3.0372 \times 10^{- 5}})}$. Also, we require the approximate inner-loop solution to have the accuracy of $\epsilon_{1} = 0.001$. As shown at the top of Figure 9, the double-loop NPG updates successfully converge to the unique Nash equilibrium of the game.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Time-Varying Systems", "weight": 1.0} -->

Also, the minimum eigenvalue of ${\mathbf{R}}^{w} - {{\mathbf{D}}^{\top}{\mathbf{P}}_{{\mathbf{K}},{\mathbf{L}}}{\mathbf{D}}}$ is monotonically non-decreasing along the iterations of the outer-loop NPG update, which matches the implicit regularization property we introduced in Theorem 3.8. This guarantees that all future iterates of $\mathbf{K}$ will stay in the interior of $\mathcal{K}$ given that the initial $\mathbf{K}$ does. The convergences of the average gradient norms with respect to both $\mathbf{L}$ and $\mathbf{K}$ are presented at the bottom of Figure 9.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

In this paper, we have investigated derivative-free policy optimization methods for solving a class of risk-sensitive and robust control problems, covering three fundamental settings: LEQG, LQ disturbance attenuation, and zero-sum LQ dynamic games. This work aims towards combining two lines of research, robust control theory, and policy-based model-free RL methods. Several ongoing/future research directions include studying (i) nonlinear systems under nonquadratic performance indices; (ii) systems with delayed state information at the controller; (iii) the global convergence and sample complexity of PG methods for continuous-time and/or output-feedback risk-sensitive and robust control problems; (iv) the convergence properties of simultaneous or alternating descent-ascent type PG methods for zero-sum LQ dynamic games; and (v) other model-based approaches that may yield an improved sample complexity bound.
