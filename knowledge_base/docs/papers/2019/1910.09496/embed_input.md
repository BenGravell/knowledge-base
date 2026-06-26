<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Policy Optimization for H2 Linear Control with H∞ Robustness Guarantee: Implicit Regularization and Global Convergence

Topics include Nonconvex optimization, Policy gradients, Reinforcement learning, Optimal control, Stability analysis, Safety, Robustness, Optimization, Control, Learning, Policy optimization, PO, Linear quadratic regulator.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Policy optimization (PO) is a key ingredient for reinforcement learning (RL). For control design, certain constraints are usually enforced on the policies to optimize, accounting for either the stability, robustness, or safety concerns on the system. Hence, PO is by nature a constrained (nonconvex) optimization in most cases, whose global convergence is challenging to analyze in general. More importantly, some constraints that are safety-critical, e.g., the H_infinity-norm constraint that guarantees the system robustness, are difficult to enforce as the PO methods proceed. Recently, policy gradient methods have been shown to converge to the global optimum of linear quadratic regulator (LQR), a classical optimal control problem, without regularizing/projecting the control iterates onto the stabilizing set, its (implicit) feasible set. This striking result is built upon the coercive property of the cost, ensuring that the iterates remain feasible as the cost decreases. In this paper, we study the convergence theory of PO for H_2 linear control with H_infinity-norm robustness guarantee.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

One significant new feature of this problem is the lack of coercivity, i.e., the cost may have finite value around the feasible set boundary, breaking the existing analysis for LQR. Interestingly, we show that two PO methods enjoy the implicit regularization property, i.e., the iterates preserve the H_infinity robustness constraint as if they are regularized by the algorithms. Furthermore, despite the nonconvexity of the problem, we show that these algorithms converge to the globally optimal policies with globally sublinear rates, avoiding all suboptimal stationary points/local minima, and with locally (super-)linear rates under certain conditions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent years have witnessed tremendous success of reinforcement learning (RL) in various sequential decision-making applications and continuous control tasks. Interestingly, most successes hinge on the algorithmic framework of *policy optimization* (PO), umbrellaing policy gradient (PG) methods, actor-critic methods, trust-region and proximal PO methods, etc. This inspires an increasing interest in studying the convergence theory, especially global convergence to optimal policies, of PO methods; see recent progresses in both classical RL contexts, and continuous control benchmarks.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Indeed, PO provides a general framework for control design.^11^1Hereafter, we will mostly adhere to the terminologies and notational convention in the control literature, which are equivalent to, and can be easily translated to those in the RL literature, e.g., cost v.s. reward, control v.s. action, etc. Consider a general control design problem for the following discrete-time nonlinear dynamical system where $x_{k}$ is the state, $u_{k}$ is the control input, and $w_{k}$ is the process noise. Formally, PO is a constrained optimization problem ${\min_{K \in \mathcal{K}}\mathcal{J}}{(K)}$, where the decision variable $K$ is determined by the controller parameterization, the cost function $\mathcal{J}{(K)}$ is a pre-specified control performance measure, and the feasible set $\mathcal{K}$ carries the information of the constraints on the controller $K$. These concepts are briefly reviewed as follows.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimization variable $K$: The control input $u_{k}$ is typically determined by a feedback law $K$ which is also termed as a *controller*. In the simplest case where a LTI state-feedback controller is used, $K$ is parameterized as a static matrix and $u_{k}$ is given as $u_{k} = {- {Kx_{k}}}$. Then this matrix $K$ becomes the decision variable of the PO problem. For the so-called linear output feedback case where the state $x_{k}$ is not directly measured, the controller can be either a memoryless mapping or an LTI dynamical system. Hence, $K$ can be parameterized by either a static matrix or some state/input/output matrices $(A_{K},B_{K},C_{K},D_{K})$. It is also possible to deploy nonlinear controllers and parameterize $K$ as either polynomials, kernels, or deep neural networks.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Objective function $\mathcal{J}{(K)}$: $\mathcal{J}{(K)}$ is specified to assess the performance of a given controller $K$. The cost function design is more of an art than a science. Popular choices of such cost functions include $\mathcal{H}_{2}$ or $\mathcal{H}_{\infty}$-norm (or some related upper bounds) for the resultant feedback systems. For standard RL models that are based on Markov decision processes (MDPs), the cost $\mathcal{J}{(K)}$ usually has an additive structure over time.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

For instance, in the classical linear quadratic regulator (LQR) or state-feedback LQ Gaussian (LQG) problems, the cost is ${\mathcal{J}{(K)}}:={\sum_{t = 0}^{\infty}{E{\lbrack{{x_{t}^{\top}Qx_{t}} + {u_{t}^{\top}Ru_{t}}}\rbrack}}}$, which also has an $\mathcal{H}_{2}$-norm interpretation. Nevertheless, $\mathcal{J}{(K)}$ does not necessarily have an additive structure. We will further discuss the specification of $\mathcal{J}{(K)}$ in §2.2.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Feasible set $\mathcal{K}$: Constraints on the decision variable $K$ are posed to account for either the stability, robustness, or safety concerns on the system. A common, though sometimes implicit, example in continuous control tasks is the stability constraint, i.e. $K$ is required to stabilize the closed-loop dynamics. There are also other constraints related to robustness or safety concerns in control design. The constraints will naturally confine the policy search to a feasible set $\mathcal{K}$. The cost function $\mathcal{J}{(K)}$ is either $\infty$ or just undefined for $K\mathcal{K}$.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

To ensure the feasibility of $K$ on the fly as the PO methods proceed, projection of the iterates onto the set $\mathcal{K}$ seems to be the first natural approach that comes to mind. However, such a projection may not be computationally efficient or even tractable. For example, projection onto the stability constraint in LQR problems can hardly be computed, as the set $\mathcal{K}$ therein is well known to be nonconvex. Fortunately, such a projection is not needed to preserve the feasibility of the iterates in PG-based methods, as recently reported by Fazel et al.; Bu et al.. In particular, Bu et al. has identified that the cost of LQR has the *coercive* property, such that it diverges to infinity as the controller $K$ approaches the boundary of the feasible set $\mathcal{K}$. In other words, the cost of LQR serves as a barrier function on $\mathcal{K}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

This way, the level set of the cost becomes compact, and the decrease of the cost ensures the next iterate to stay inside the level set, which further implies the stay inside $\mathcal{K}$. This desired property is further illustrated in Figure 1(a), where $K$ and $K'$ are two consecutive iterates, and the level set $\left. \{\overset{\sim}{K} \middle| {{\mathcal{J}{(\overset{\sim}{K})}} \leq {\mathcal{J}{(K)}}}\} \right.$ is always separated from the set $\mathcal{K}^{c}$ by some distance $\delta > 0$. Hence, as long as ${\|{K - K'}\|} < \delta$, the next iterate $K'$ still stays in the set $\mathcal{K}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

More importantly, such a separation distance $\delta$ can be re-used for the next iterate, as the next level set is at least $\delta$ away from $\mathcal{K}^{c}$. By induction, this allows the existence of a constant stepsize that can guarantee the controllers' stability along the iterations. It is worth emphasizing that such a property is *algorithm-agnostic*, in the sense that it is dictated by the cost, and independent of the algorithms adopted, as long as they follow any descent directions of the cost.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Besides the stability constraint, another commonly used one in the control literature is the so-called *$\mathcal{H}_{\infty}$ constraints*. This type of constraints plays a fundamental role in robust control and risk-sensitive control. Based on the well-known small gain theorem, such constraints can be used to guarantee robust stability/performance of the closed-loop systems when model uncertainty is at presence. Compared with LQR under the stability constraint, control synthesis under the $\mathcal{H}_{\infty}$ constraint leads to a fundamentally different optimization landscape, over which the behaviors of PO methods have not been fully investigated yet. In this paper, we take an initial step towards understanding the theoretical aspects of policy-based RL methods on robust/risk-sensitive control problems.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Specifically, we establish a convergence theory for PO methods on $\mathcal{H}_{2}$ linear control problems with $\mathcal{H}_{\infty}$ constraints, referred to as *mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ state-feedback control design* in the robust control literature. As the name suggests, the goal of mixed design is to find a robust stabilizing controller that minimizes an upper bound for the $\mathcal{H}_{2}$-norm, under the restriction that the $\mathcal{H}_{\infty}$-norm on a certain input-output channel is less than a pre-specified value. The $\mathcal{H}_{\infty}$ constraint is explicitly posed here to guarantee the robustness of the closed-loop system to some extent.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

This general framework also includes risk-sensitive linear control, modeled as linear exponential quadratic Gaussian (LEQG) problems as a special case, when a certain upper bound of $\mathcal{H}_{2}$-norm is used. Detailed formulation for such $\mathcal{H}_{2}$ linear control with $\mathcal{H}_{\infty}$ constraint is provided in §2. In contrast to LQR, two challenges exist in the analysis of PO methods for mixed design problems. First, by definition of $\mathcal{H}_{\infty}$-norm, the constraint is defined in the frequency domain, and is hard to impose, for instance, by directly projecting the iterates in that domain, especially in the context of RL when the system model is unknown. Note that preserving the constraint bound of $\mathcal{H}_{\infty}$-norm as the controller updates is critical in practice, since violation of it can cause catastrophic consequences on the system.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, more importantly, the coercive property of LQR fails to hold for mixed design problems, as illustrated in Figure 1(b) (and formally established later). Particularly, the cost value, though undefined outside the set $\mathcal{K}$, remains *finite* around the boundary of $\mathcal{K}$. Hence, the decrease of cost from $K$ to $K'$ cannot guarantee that the iterate does not travel towards, and even beyond the feasibility boundary. With no strict separation between the cost level set and $\mathcal{K}^{c}$, there may not exist a constant stepsize that induces global convergence to the optimal policy.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

These two challenges naturally raise the question: does there exist any computationally tractable PO method, which preserves the robustness constraint along the iterations, and enjoys (hopefully global) convergence guarantees? We provide a positive answer to this question in the present work. Our key contribution is three-fold: First, we study the landscape of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design problems for both discrete- and continuous-time settings, and propose three policy-gradient based methods, inspired by those for LQR. Second, we prove that two of them (the Gauss-Newton method and the natural PG method) enjoy the *implicit regularization* property, such that the iterates are automatically biased to satisfy the required $\mathcal{H}_{\infty}$ constraint. Third, we establish the global convergence of those two PO methods to the *globally optimal* policy with *globally sublinear* and *locally (super-)linear* rates under certain conditions, despite the nonconvexity of the problem.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, the two policy search directions always lead to convergence to the global optimum, without getting stuck at any spurious stationary point/local optima. Along the way, we also derive new results on linear risk-sensitive control, i.e., LEQG problems, and discuss the connection of mixed design to zero-sum LQ dynamic games, for designing model-free versions of the algorithms. We expect our work to help pave the way for rigorous understanding of PO methods for general optimal control with $\mathcal{H}_{\infty}$ robustness guarantees.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

(b) Landscape of Mixed ℋ2/ℋ∞ Control Figure 1: Comparison of the landscapes of LQR and mixed ℋ2/ℋ∞ control design that illustrates the hardness of showing convergence of the latter. The dashed lines represent the boundaries of the constraint sets 𝒦. For (a) LQR, 𝒦 is the set of all linear stabilizing state-feedback controllers; for (b) mixed ℋ2/ℋ∞ control, 𝒦 is set of all linear stabilizing state-feedback controllers satisfying an extra ℋ∞ constraint on some input-output channel. The solid lines represent the contour lines of the cost 𝒥 (K). K and K′ denote the control gain of two consecutive iterates; denotes the global optimizer.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

Note that the concept of (implicit) regularization has been adopted in many recent works on nonconvex optimization, including training neural networks, phase retrieval, matrix completion, and blind deconvolution, referring to any scheme that biases the search direction of the optimization algorithms. The term *implicit* emphasizes that the algorithms without regularization may behave as if they are regularized. This property has been advocated as an important feature of gradient-based methods for solving aforementioned nonconvex problems. We emphasize that it is a feature of both the *problem* and the *algorithm*, i.e., it holds for certain algorithms that solve certain problems. This is precisely the case in the present work. The specific search directions of the Gauss-Newton and the natural PG methods bias the iterates towards the set of the stabilizing controllers satisfying the $\mathcal{H}_{\infty}$ constraint, although no explicit regularization, e.g., projection, is adopted, which contrasts to that the stability-preserving of PO methods for LQR problems is algorithm-agnostic.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

To the best of our knowledge, our work appears to be the first studying the implicit regularization properties of PO methods for *learning-based control* in general.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Motivating Example: LEQG", "weight": 1.0} -->

We start with an example of *risk-sensitive* control, the *infinite-horizon state-feedback linear exponential quadratic Gaussian* problem^22^2Unless otherwise noted, we will just refer to this problem as LEQG hereafter., which is motivating in that: i) it is closely related to the well-known linear optimal control problems, e.g., LQR and state-feedback LQG; ii) it illustrates the idea of mixed control design, especially introducing the $\mathcal{H}_{\infty}$-norm constraint, though implicit, that guarantees robustness. The latter manifests the challenge in the convergence analysis of PO methods for this problem.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Motivating Example: LEQG", "weight": 1.0} -->

Specifically, at time $t \geq 0$, the agent takes an action $u_{t} \in R^{d}$ at state $x_{t} \in R^{m}$, which leads the system to a new state $x_{t + 1}$ by a linear dynamical system where $A$ and $B$ are matrices of proper dimensions, $x_{0} \in R^{m}$ and ${w_{t} \in R^{m}},{{\forall t} \geq 0}$ are independent zero-mean Gaussian random variables with positive-definite covariance matrices $X_{0}$ and $W$, respectively. The one-stage cost of applying control $u$ at state $x$ is given by ${c{(x,u)}} = {{x^{\top}Qx} + {u^{\top}Ru}}$, where $Q$ and $R$ are positive-definite matrices.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Motivating Example: LEQG", "weight": 1.0} -->

Then, the long-term cost to minimize is where $\beta$ is the parameter that describes the intensity of risk-sensitivity, and the expectation is taken over the randomness of both $x_{0}$ and $w_{t}$ for all $t \geq 0$. The intuition behind the objective (2.1) is that by Taylor series expansion around $\beta = 0$, Hence, if $\beta > 0$, the control is *risk-averse* since minimization also places positive weight on the variance, in addition to the expectation, of the cost; in contrast, if $\beta < 0$, the control is referred to as *risk-seeking*, which encourages the variance to be large. As $\beta\rightarrow 0$, the objective (2.1) reduces to the *risk-neutral* objective of LQR/state-feedback LQG. Usually LEQG problems consider the case of $\beta > 0$. In this sense, LEQG can be viewed as a generalization of LQR/state-feedback LQG problems.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Motivating Example: LEQG", "weight": 1.0} -->

The goal of LEQG is to find the optimal control policy $\mu_{t}:{{{({R^{m} \times R^{d}})}^{t} \times R^{m}}\rightarrow R^{d}}$, which in general is a mapping from the history of state-action pairs till time $t$ and current state $x_{t}$, to the action $u_{t}$ in $R^{d}$, that minimizes the cost in (2.1). By assuming that such an optimal policy exists, the $\operatorname{lim\ sup}$ in (2.1) can be replaced by $\lim$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Motivating Example: LEQG", "weight": 1.0} -->

Moreover, we can show, see a formal statement in Lemma C.2 in §C, that the optimal control has a desired property of being memoryless and *stationary*, i.e., *linear time-invariant* (LTI), and current *state-feedback*, i.e., ${{\mu_{t}{(x_{0:t},u_{0:{t - 1}})}} = {\mu{(x_{t})}} = {- {Kx_{t}}}},$ for some $K \in R^{d \times m}$. Hence, it suffices to optimize over the control gain $K$, without loss of optimality, i.e.,

<!-- chunk {"id": "body-0027", "role": "body", "section": "Cost Closed-Form", "weight": 1.0} -->

To solve (2.2) with PO methods, it is necessary to establish the closed-form of the objective with respect to $K$. To this end, we introduce the following algebraic Riccati equation for given control gain $K$. If $\beta\rightarrow 0$, (2.3) reduces to the Lyapunov equation of policy evaluation for given $K$ in LQR problems. For notational simplicity, we also define ${\overset{\sim}{P}}_{K}$ as Then, the objective $\mathcal{J}{(K)}$ can be expressed by the solution to (2.3), $P_{K}$, as follows.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 2.2 (New Results on LEQG)", "weight": 1.0} -->

To the best of our knowledge, our results on that the optimal controller is LTI state-feedback in Lemma C.2, and on the form of the objective $\mathcal{J}{(K)}$ in Lemma 2.1, though expected, have not been rigorously established for LEQG problems in the literature. For completeness, we present a self-contained proof in §C. Interestingly, the former argument has been hypothesized in Section $3$ of Glover and Doyle; while the form of $\mathcal{J}{(K)}$ in (2.5) connects to the performance criterion for more general optimal control problems with robustness guarantees, as to be shown shortly.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Implicit Constraint on $\\mathcal{H}_{\\infty}$-Norm", "weight": 1.0} -->

Seemingly, (2.2) is an unconstrained optimization over $K$. However, as identified by Glover and Doyle, there is an implicit constraint set for this problem, which corresponds to the lower-level set of the $\mathcal{H}_{\infty}$-norm of the closed-loop transfer function under the linear stabilizing controller $u = {- {Kx}}$. We reiterate the result as follows.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Bigger Picture: Mixed $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ Control Synthesis", "weight": 1.0} -->

Consider the following discrete-time linear dynamical system with a single input-output channel where ${x_{t} \in R^{m}},{u_{t} \in R^{d}}$ denote the states and controls, respectively, $w_{t} \in R^{n}$ is the disturbance, $z_{t} \in R^{l}$ is the controlled output, and $A,B,C,D,E$ are matrices of proper dimensions. Consider the *admissible* control policy $\mu_{t}$ to be a mapping from the history of state-action pairs till time $t$ and the current state $x_{t}$ to action $u_{t}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Bigger Picture: Mixed $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ Control Synthesis", "weight": 1.0} -->

It has been shown in Kaminer et al. that, *LTI* state-feedback controller (without memory) suffices to achieve the optimal performance of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design under this *state-feedback* information structure^33^3For discrete-time settings, if both the (exogenous) disturbance $w_{t}$ and the state $x_{t}$ are available, i.e., under the *full-information* feedback case, LTI controllers may not be optimal. Interestingly, for continuous-time settings, LTI controllers are indeed optimal.. As a consequence, it suffices to consider only stationary, current state-feedback controller parametrized as $u_{t} = {- {Kx_{t}}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 2.4 (Justification of LTI Control for LEQG)", "weight": 1.0} -->

As to be shown shortly, LEQG is a special case of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design. Hence, the result we derived in Lemma C.2, i.e., the optimal controller of LEQG is indeed LTI, is consistent with this earlier result on mixed design from Khargonekar and Rotea; Kaminer et al..

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 2.4 (Justification of LTI Control for LEQG)", "weight": 1.0} -->

In accordance with this parametrization, the transfer function from the disturbance $w_{t}$ to the output $z_{t}$ can be represented as In common with Glover and Doyle; Khargonekar and Rotea; Başar and Bernhard, we make the following assumption on the matrices $A,B,C,D$ and $E$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

Assumption 2.5 is fairly standard, which clarifies the exposition substantially by normalising the control weighting and eliminating cross-weightings between control signal and state. Hence, the transfer function in (2.9) has the equivalent form^44^4Strictly speaking, the transfer functions for (2.9) and (2.12) are equivalent in the sense that the values of $\mathcal{T}^{\sim}{(K)}\mathcal{T}{(K)}$ are the same for all the points on the unit circle. of Hence, robustness of the designed controller can be guaranteed by the constraint on the $\mathcal{H}_{\infty}$-norm, i.e., ${\|{\mathcal{T}{(K)}}\|}_{\infty} < \gamma$ for some $\gamma > 0$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

The intuition behind the constraint, which follows from small gain theorem, is that the constraint on ${\|{\mathcal{T}{(K)}}\|}_{\infty}$ implies that the closed-loop system is *robustly stable* in that any stable transfer function satisfying $\parallel \parallel_{\ell_{2}\rightarrow\ell_{2}} < 1/\gamma$ may be connected from $z_{t}$ back to $w_{t}$ without destablizing the system. For more background on $\mathcal{H}_{\infty}$ control, see Başar and Bernhard; Zhou et al.. For notational convenience, we define the feasible set of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control design as We note that the set $\mathcal{K}$ may be unbounded.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Assumption 2.5", "weight": 1.0} -->

In addition to the constraint, the objective of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design is usually an upper bound of the $\mathcal{H}_{2}$ norm of the closed-loop system. By a slight abuse of notation, let $\mathcal{J}{(K)}$ be the cost function of mixed design. Then the common forms of $\mathcal{J}{(K)}$ include Mustafa; Mustafa and Bernstein where $P_{K}$ is the solution to the following Riccati equation with ${\overset{\sim}{P}}_{K}$ defined as

<!-- chunk {"id": "body-0037", "role": "body", "section": "Remark 2.6 (LEQG as a Special Case of Mixed-Design)", "weight": 1.0} -->

By Lemma 2.3). ‣ 2.1.2 Implicit Constraint on ℋ_∞-Norm ‣ 2.1 Motivating Example: LEQG ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"), replacing $\beta$, $W$, and $Q$ in LEQG by $\gamma^{- 2}$, $DD^{\top}$ and $C^{\top}C$, respectively, yields the formulation of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design. In particular, the closed-form cost of LEQG that we derived for the first time, see Lemma 2.1, is identical to the cost in (2.15); and the implicit constraint of LEQG in Lemma 2.3).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Remark 2.6 (LEQG as a Special Case of Mixed-Design)", "weight": 1.0} -->

‣ 2.1.2 Implicit Constraint on ℋ_∞-Norm ‣ 2.1 Motivating Example: LEQG ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") is exactly the $\mathcal{H}_{\infty}$-norm constraint in (2.13). Thus, LEQG is a mixed-design problem with $D = W^{1/2}$ and $\mathcal{J}{(K)}$ being (2.15). Note that ${DD^{\top}} = W > 0$ for LEQG.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Remark 2.6 (LEQG as a Special Case of Mixed-Design)", "weight": 1.0} -->

All three objectives in (2.14)-(2.16) are upper bounds of the $\mathcal{H}_{2}$-norm. In particular, cost (2.14) has been adopted in Bernstein and Haddad; Haddad et al., which resembles the standard $\mathcal{H}_{2}$ control/LQG control objective, but with $P_{K}$ satisfying a Riccati equation instead of a Lyapunov equation. Cost (2.15) is closely related to maximum entropy $\mathcal{H}_{\infty}$-control, see the detailed relationship between the two in Mustafa and Glover. In addition, cost (2.16) can also be connected to the cost of LQG using a different Riccati equation. As $\gamma\rightarrow\infty$, the costs in all (2.14)-(2.16) reduce to the cost for LQG, i.e., $\mathcal{H}_{2}$ control design problems.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Remark 2.6 (LEQG as a Special Case of Mixed-Design)", "weight": 1.0} -->

In sum, the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control design can be formulated as with $\mathcal{J}{(K)}$ and $\mathcal{K}$ defined in (2.14)-(2.16) and (2.13), respectively.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Bounded Real Lemma", "weight": 1.0} -->

Though the constraint (2.13) is concise, it is hard to enforce over $K$ in policy optimization, since the constraint is defined in the frequency domain. Interestingly, by using a significant result in robust control theory, i.e., *Bounded Real Lemma* constraint (2.13) can be related to the solution of a Riccati equation and a Riccati inequality. We formally introduce the result as follows, whose proof is deferred to §B.1.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Remark 2.8 (Necessity of Lemma 2.1)", "weight": 1.0} -->

By Lemma 2.7. ‣ 2.3 Bounded Real Lemma ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") and Remark 2.6. ‣ 2.2 Bigger Picture: Mixed ℋ₂/ℋ_∞ Control Synthesis ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"), the conditions in Lemma 2.1 are equivalent to the $\mathcal{H}_{\infty}$-norm constraint in (2.13) for LEQG. This implies that these conditions are not only *sufficient* for the form of $\mathcal{J}{(K)}$ in Lemma 2.1 to hold, but also *necessary*. In other words, any feasible $K \in \mathcal{K}$ should lead to the form of $\mathcal{J}{(K)}$ in (2.5).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Remark 2.8 (Necessity of Lemma 2.1)", "weight": 1.0} -->

Next, we develop policy optimization algorithms for solving the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control problem in (2.19).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Landscape and Algorithms", "weight": 1.0} -->

In this section, we investigate the optimization landscape of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control design, and develop policy optimization algorithms with convergence guarantees. In particular, we study both discrete- and continuous-time settings focusing on two representative example costs $\mathcal{J}{(K)}$ from (2.15) and (2.14), respectively.^55^5Although only two example settings are studied in detail, the techniques developed can also be applied to other combinations of settings, e.g., cost (2.14) in discrete-time settings. The first combination of settings also by chance solves the discrete-time LEQG problems introduced in §2.1. The second combination for continuous-time settings is discussed in §A.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Optimization Landscape", "weight": 1.0} -->

We start by showing that, regardless of the cost $\mathcal{J}{(K)}$, the mixed-design problem in (2.19) is a *nonconvex* optimization problem.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Policy Optimization Algorithms", "weight": 1.0} -->

Consider three policy-gradient based methods as follows. For simplicity, we define We also suppress the iteration index, and use $K$ and $K'$ to represent the control gain before and after one-step of the update. where $\eta > 0$ is the stepsize. The updates are motivated by and resemble the policy optimization updates for LQR, but with $P_{K}$ therein replaced by ${\overset{\sim}{P}}_{K}$. The natural PG update is related to gradient over a Riemannian manifold; while the Gauss-Newton update is one type of quasi-Newton update, see Bu et al. for further justifications on the updates. In particular, with $\eta = {1/2}$, the Gauss-Newton update (3.5) can be viewed as the *policy iteration* update for infinite-horizon mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Policy Optimization Algorithms", "weight": 1.0} -->

Model-free versions of the PG update (3.3) can be directly obtained, since the gradient ${\nabla\mathcal{J}}{(K)}$ can be estimated by sampled data, using for instance zeroth-order methods, as in Fazel et al.; Malik et al.. A direct model-free implementation of the natural PG update (3.4) using zeroth-order optimization methods requires estimating the matrix ~K~. It is not clear yet how to estimate it from the sampled trajectories. Instead, we propose one solution by the connections between mixed design and zero-sum linear quadratic games; see §6 for more details. Finally, as in LQR problems, the Gauss-Newton update (3.5) cannot yet be estimated using zeroth-order methods directly.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Theoretical Results", "weight": 1.0} -->

In this section, we investigate the convergence of the PO methods proposed in §3.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Implicit Regularization", "weight": 1.0} -->

The first key challenge in the convergence analysis for PO methods, is to ensure that the iterates remain *feasible* as the algorithms proceed, hopefully without the use of *projection*. This is especially significant in mixed design problems, as the feasibility here means *robust stability*, the violation of which can be catastrophic in practical *online* control design. We formally define the concept of *implicit regularization* to describe this feature.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

The concept of *(implicit) regularization* has been adopted in many recent studies on nonconvex optimization, including training neural networks, phase retrieval, matrix completion, and blind deconvolution, referring to any scheme that biases the search direction of gradient-based algorithms. Implicit regularization has been advocated as an important feature of (stochastic) gradient descent methods for solving these problems, which, as the name suggests, means that the algorithms without regularization may behave as if they are regularized. Note that the term *regularization* may refer to several different schemes in different problems, e.g., trimming/truncation the gradient, adding a regularization term in the objective, etc. Here we focus on the scheme of *projection*, as summarized in Ma et al.. Also note that implicit regularization is a feature of both the *problem* and the *algorithm*, i.e., it holds for certain algorithms that solve certain nonconvex problems.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

One possible way for the iterates to remain feasible is to keep shrinking the stepsize, whenever the next iterate goes outside $\mathcal{K}$, following for example the Armijo rule. However, as the cost $\mathcal{J}{(K)}$ is not necessarily smooth (see Lemma 5.1. ‣ 5.2 Proof of Theorem 4.4 ‣ 5 Proofs of Main Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") and its discussion later), it may not converge within a finite number of iterations. Another option is to project the iterate onto $\mathcal{K}$. Nonetheless, it is challenging to perform projection onto the $\mathcal{H}_{\infty}$-norm constraint set directly in the frequency domain.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

For LQR problems, due to the coercivity of the cost that as $K$ approaches the boundary of the stability/feasibility region $\left. \{{K \in R^{d \times m}} \middle| {{\rho{({A - {BK}})}} < 1}\} \right.$, i.e., as ${\rho{({A - {BK}})}}\rightarrow 1$, the cost blows up to infinity, and due to the fact that the cost is continuous with respect to $K$, the lower-level set of the cost is compact and is contained within the stability region. As a consequence, there is a strict separation between any lower-level set of the cost and the set $\left. \{{K \in R^{d \times m}} \middle| {{\rho{({A - {BK}})}} \geq 1}\} \right.$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

Hence, as discussed in the introduction, there exists a *constant stepsize* such that as long as the initialization control is stabilizing, the iterates along the path remain stabilizing and keep decreasing the cost. Such a property is *algorithm-agnostic* in that it is dictated by the property of the cost, and independent of the algorithms adopted, as long as they follow any descent directions of the cost. The stability proofs in Fazel et al.; Bu et al. for LQR are essentially built upon this idea.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

In contrast, for mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design problems, lack of coercivity invalidates the argument above, as the control approaching the robustness constraint boundary $\partial\mathcal{K}$ may incur a *finite* cost, and the descent direction may still drive the iterates out of the feasibility region. In addition, there may not exist a strict separation between all the lower-level sets of the cost and the complementary set $\mathcal{K}^{c}$. This difficulty has been illustrated in Figure 1 in the introduction, which compares the landscapes of the two problems. Interestingly, we show in the following theorem that the natural PG and Gauss-Newton methods in (3.4)-(3.5) enjoy the implicit regularization feature, with certain *constant* stepsize. We only highlight the idea of the proof here, and defer the details to §5.1. The proof includes two main steps.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

First, we directly use $P_{K}$ to construct a Lyapunov function for $K'$ to show a non-strict Riccati inequality that guarantees ${\|{\mathcal{T}{(K')}}\|}_{\infty} \leq \gamma$. Second, we further perturb $P_{K}$ in a specific way to show the strict inequality ${\|{\mathcal{T}{(K')}}\|}_{\infty} < \gamma$. The perturbation argument is inspired by the proof of the Kalman-Yakubovich-Popov (KYP) Lemma.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Global Convergence", "weight": 1.0} -->

The term *global convergence* here refers to two notions: i) the convergence performance of the algorithms starting from *any feasible initialization* point $K_{0} \in \mathcal{K}$; ii) convergence to the *global optimal* policy under certain conditions. We formally establish the results for the natural PG (3.4) and Gauss-Newton (3.5) updates in the following theorem.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark 4.5 (Robust Initial Controller)", "weight": 1.0} -->

Our global convergence requires the initial controller to satisfy the $\mathcal{H}_{\infty}$-norm robustness constraint, which, as the assumption on the initial controller being stabilizing for LQR, is inherent to PO methods with iterative local search. Complementary to Fazel et al.; Bu et al., our iterates not only improve the performance criterion, but also preserve the robustness.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Remark 4.5 (Robust Initial Controller)", "weight": 1.0} -->

Though sublinear globally, much faster rates, i.e., (super-)linear rates, can be shown locally around the optimum as below. Proof of the following theorem is deferred to §5.3.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Remark 4.7 (Comparison to Zhang et al. )", "weight": 1.0} -->

Due to the close relationship between mixed design and zero-sum LQ games, see §6, one may compare the convergence results and find the rates here (*globally sublinear and locally linear*) not improved over Zhang et al.. However, one key difference is that an extra *projection* step is required to guarantee the *stability* of the system in Zhang et al., which is essentially to *regularize* the iterates *explicitly*. More importantly, such a projection can only be calculated under more restrictive assumptions (see Assumption 2.1 therein), which, though cover a class of LQ games, are not standard in robust control. Here, similar convergence results are established, without projections or non-standard assumptions in robust control, thanks to *implicit regularization*. Moreover, we have established the local "superlinear" rate for the Gauss-Newton update, and whole new set of results for the "continuous-time" setup, which were not studied in Zhang et al..

<!-- chunk {"id": "body-0060", "role": "body", "section": "Proofs of Main Results", "weight": 1.0} -->

In this section, we provide detailed proofs for the main results of the paper.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Discussions", "weight": 1.0} -->

We now provide additional discussions on the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control design problem.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Connection to Zero-Sum LQ Games", "weight": 1.0} -->

It is well known that minimizing the risk-sensitive cost as (2.1), which is the logarithm of the expected values of exponential functions with quadratic forms, can be equivalent to solving a zero-sum dynamic game, for both general settings, and in particular for LQ settings. Due to the connection between LEQG and mixed design, as discussed in §2.2, the latter can be related to a zero-sum LQ game as well.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Connection to Zero-Sum LQ Games", "weight": 1.0} -->

Specifically, consider the system that follows linear dynamics^77^7The notation in this section might be slightly abused, considering the notations used in the main text, but shall be self-evident by the context. with the system state being $x_{t} \in R^{d}$, the control inputs of players $1$ and $2$ being $u_{t} \in R^{m_{1}}$ and $v_{t} \in R^{m_{2}}$, respectively. The matrices $A,B$, and $D$ all have proper dimensions.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Connection to Zero-Sum LQ Games", "weight": 1.0} -->

The objective of player $1$ (player $2$) is to minimize (maximize) the infinite-horizon value function, where the initial state $x_{0} \sim \mathcal{D}$ for some distribution $\mathcal{D}$, the matrices $Q \in R^{d \times d}$, $R^{u} \in R^{m_{1} \times m_{1}}$, and $R^{v} \in R^{m_{2} \times m_{2}}$ are all positive definite.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Connection to Zero-Sum LQ Games", "weight": 1.0} -->

*Value* of the game, i.e., the value of (6.1) when the $\inf$ and $\sup$ can interchange, is characterized by $E_{x_{0} \sim \mathcal{D}}{({x_{0}^{\top}P^{\ast}x_{0}})}$, where $P^{\ast}$ is the solution to the generalized algebraic Riccati equation (GARE) Moreover, under the standard assumption that ${R^{v} - {D^{\top}P^{\ast}D}} > 0$, the solution policies, i.e., the *Nash equilibrium* (NE) policies that are stabilizing, of the two players have forms of LTI state-feedback, namely, $u_{t}^{\ast} = {- {K^{\ast}x_{t}}}$ and $v_{t}^{\ast} = {- {L^{\ast}x_{t}}}$ for some matrices

<!-- chunk {"id": "body-0066", "role": "body", "section": "Connection to Zero-Sum LQ Games", "weight": 1.0} -->

The corresponding values of $(K^{\ast},L^{\ast})$ are given by As a consequence, it suffices to search over all stabilizing control gain pairs $(K,L)$ that solves In fact, for any stabilizing $(K,L)$ that makes ${\rho{({A - {BK} - {DL}})}} < 1$, $\mathcal{C}{(K,L)} = \operatorname{Tr}{(P_{K,L}{{}_{0}^{})}}$, where ${{}_{0}^{} =}E_{x_{0} \sim \mathcal{D}}{(x_{0}^{\top}x_{0})}$, and $P_{K,L}$ is the unique solution to the Lyapunov equation Given $K$ that makes^88^8This condition on $K$ is necessary for finding the equilibrium policy since otherwise, the maximizer can drive the cost to infinity by choosing

<!-- chunk {"id": "body-0067", "role": "body", "section": "Connection to Zero-Sum LQ Games", "weight": 1.0} -->

See Chapter $3$ of Başar and Bernhard for more discussions. ${R^{v} - {D^{\top}P_{K,L}D}} > 0$, maximizing over $L$ on the RHS of (6.5) yields where $P_{K}^{\ast} = P_{K,{L{(K)}}}$ with $L{(K)}$ being the maximizer that satisfies Notice that (6.6) is in fact a Riccati equation identical to (2.17), with $R^{v}$ replaced by $\gamma^{2}I$, $R^{u}$ replaced by $R$, and $Q$ replaced by $C^{\top}C$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Connection to Zero-Sum LQ Games", "weight": 1.0} -->

Hence, the problem (6.4) is equivalent to minimizing $\mathcal{C}{(K,L{(K)})} = \operatorname{Tr}{(P_{K}^{\ast}{{}_{0}^{})}}$, subject to (6.6), which coincides with the mixed design problem (2.19), where $\mathcal{J}{(K)}$ takes the form of (2.14) with $DD^{\top}$ replaced by ~0~. Furthermore, the minimizer of the RHS on (6.6) is which equals the global optimum for the mixed design problems.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Model-Free Algorithms", "weight": 1.0} -->

The connection above provides one angle to develop *model-free* RL algorithms for solving mixed design problems. Indeed, the natural PG in (3.4) cannot be sampled using trajectory data, due to the form of the matrix ~K~ in (3.1). Fortunately, solution of the game (6.4) can be obtained by model-free PG-based methods, see Zhang et al., and the more recent work Bu et al., which, by (6.8) and Proposition 3.4, is equivalent to the global optimum of mixed design problems. Hence, model-free algorithms that solve the LQ game (6.4) can also be used to solve the mixed design problem (2.19).

<!-- chunk {"id": "body-0070", "role": "body", "section": "Model-Free Algorithms", "weight": 1.0} -->

Specifically, by Lemma 3.3 of Zhang et al., under certain conditions, the stationary point $(K,L)$ where ${{\nabla_{K}\mathcal{C}}{(K,L)}} = 0$ and ${{\nabla_{L}\mathcal{C}}{(K,L)}} = 0$ coincides with the NE. Therefore, it is straightforward to develop PG-based updates to find the minimizer $L{(K)}$ for some $K$, and then perform PG-based algorithms to update $K$, which can both be implemented in a model-free fashion, using zeroth-order methods. Note that the PO methods in Zhang et al. are essentially also based on this idea, but with the order of $\max$ and $\min$ interchanged, and require a projection step for updating $L$. More recently, Bu et al. has developed double-loop PO methods that remove this projection.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Model-Free Algorithms", "weight": 1.0} -->

Note that the simulator for the game (6.4) that generates the data samples can be obtained by the simulator for the mixed design problem (2.19), with the disturbance $w_{t}$ modeled as $w_{t} = {- {Lx_{t}}}$. This way, the updates of $L$ in (6.9) and (6.11) can be understood as improving the disturbance to find the *worst-case* one, which manifests the idea of $\mathcal{H}_{\infty}$ norm. Also, Bu et al. has verified that in zero-sum LQ games, given a fixed $K$, such an update of $L$ converges to the best-response disturbance $L{(K)}$ given in (6.7). This justifies the feasibility of our algorithms (6.9)-(6.12).

<!-- chunk {"id": "body-0072", "role": "body", "section": "Model-Free Algorithms", "weight": 1.0} -->

In addition, by the form of the policy gradients for the game, see Lemma 3.2 in Zhang et al., the exact natural PG update on the LHS of (6.12) is identical to that for mixed design problems in (3.4). In other words, the natural PG update (3.4) can be implemented in a model-free way by virtue of that outer-loop update of $K$ in a zero-sum LQ game. As shown in Bu et al., such an outer-loop update over $K$ converges to the NE of the game. Details of the model-free algorithms are deferred to Algorithms 1, 2, and 3 in §D.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Simulations", "weight": 1.0} -->

In this section, we present some simulation results to corroborate our theory. We mainly focus on the convergence properties for the discrete-time settings. We have also included extensive numerical comparisons with existing packages for solving $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ mixed design, which can only handle the continuous-time settings. The problem setup, PO algorithms, and their analyses, for the continuous-time settings can be found in §A. We show that our PO methods outperform these existing packages in many aspects, though the latter ones can handle more general setups.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Implicit Regularization & Global/Local Convergence", "weight": 1.0} -->

We first consider the following example, denoted by Case 1, whose parameters are: and ${DD^{\top}} = I$. Note that all matrices $C^{\top}C$, $E^{\top}E$, and $DD^{\top}$ are positive definite. This $DD^{\top}$ satisfies both the controllability assumption in Proposition 3.4, and the assumption ${DD^{\top}} > 0$ in Theorem 4.6Linear Convergence for Discrete-Time Mixed Design). ‣ 4.2 Global Convergence ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"). We first randomly generate $K_{0}$ with each element uniformly generated from $\lbrack{- 0.25},0.25\rbrack$, such that $K_{0}$ is stabilizing (i.e., ${\rho{({A - {BK_{0}}})}} < 1$).

<!-- chunk {"id": "body-0075", "role": "body", "section": "Implicit Regularization & Global/Local Convergence", "weight": 1.0} -->

The stepsizes $\eta$ for the PG, NPG, and Gauss-Newton updates are $1 \times 10^{- 7}$, $1 \times 10^{- 4}$, and $0.01$, respectively. We have also used $\eta = {1/2}$ for the Gauss-Newton update.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Implicit Regularization & Global/Local Convergence", "weight": 1.0} -->

As shown in Figure 2, for both performance criteria, all four update rules converge successfully. At the beginning of the iterations, NPG and Gauss-Newton with $\eta = 10^{- 2}$ indeed yield sublinear convergence of the gradient norm square; as the iterations proceed, linear convergence rate appears. Moreover, for Gauss-Newton with $\eta = {1/2}$, super-linear convergence rate has also been observed. These observations corroborate our theory in both Theorems 4.4. ‣ 4.2 Global Convergence ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") and 4.6Linear Convergence for Discrete-Time Mixed Design). ‣ 4.2 Global Convergence ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence").

<!-- chunk {"id": "body-0077", "role": "body", "section": "Implicit Regularization & Global/Local Convergence", "weight": 1.0} -->

Moreover, we have also illustrated the behaviors of the $\mathcal{H}_{\infty}$-norm ${\|{\mathcal{T}{(K)}}\|}_{\infty}$ and the smallest eigenvalue of ${\gamma^{2}I} - {D^{\top}P_{K}D}$, denoted by $\lambda_{\min}{({{\gamma^{2}I} - {D^{\top}P_{K}D}})}$, in Figure 2. It is seen that along the iterations, with the stepsizes that guarantee convergence, the $\mathcal{H}_{\infty}$-norm is below the bound $\gamma = 15.45$ for all four update rules, which validates the implicit regularization result we have in Theorem 4.3. ‣ 4.1 Implicit Regularization ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence").

<!-- chunk {"id": "body-0078", "role": "body", "section": "Implicit Regularization & Global/Local Convergence", "weight": 1.0} -->

As another evidence for implicit regularization in accordance to Lemma 2.7. ‣ 2.3 Bounded Real Lemma ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"), it is shown that the matrix ${{\gamma^{2}I} - {D^{\top}P_{K}D}} > 0$ along iterations.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Implicit Regularization & Global/Local Convergence", "weight": 1.0} -->

Notice that the initialization $K_{0}$ is very close to the boundary, as $\gamma = {1.00001 \cdot {\|{\mathcal{T}{(K_{0})}}\|}_{\infty}}$. It is shown that the vanilla PG update, even though with infinitesimal stepsize ($10^{- 7}$), still violates the $\mathcal{H}_{\infty}$-norm constraint and fails to converge. We do observe, however, in several other numerical examples, that vanilla PG update converges successfully. It is thus not clear whether there exists a *constant* stepsize choice for the *global convergence* and *robustness perservation* of the vanilla PG iterates, which is left for future investigation.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Implicit Regularization & Global/Local Convergence", "weight": 1.0} -->

To further verify our local convergence rates, we have also initialized our algorithms by randomly searching over $R^{3 \times 3}$ to find a $K_{0} \in \mathcal{K}$ such that ${\|{K_{0} - K^{\ast}}\|}_{F} \leq 0.3$. The convergence patterns are presented in Figure 3, which clearly demonstrates the faster local rates.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Escaping Suboptimal Stationary Points", "weight": 1.0} -->

We also investigate the setting where the controllability assumption in Proposition 3.4, and the assumption ${DD^{\top}} > 0$ in Theorem 4.6Linear Convergence for Discrete-Time Mixed Design). ‣ 4.2 Global Convergence ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") do not hold. In this case, there might exist multiple stationary points, many of which are suboptimal.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Escaping Suboptimal Stationary Points", "weight": 1.0} -->

Specifically, consider the following problem parameter, which is denoted by Case 2: Note that the system is open-loop unstable, as ${\rho{(A)}} > 1$. We choose $\gamma = 10$. Then, one can verify that the above mixed design problem admits an optimum $K^{\ast} = {{({R + {B^{\top}{\overset{\sim}{P}}_{K^{\ast}}B}})}^{- 1}B^{\top}{\overset{\sim}{P}}_{K^{\ast}}A} = \begin{bmatrix} \end{bmatrix}$. Moreover, there exist an infinite number of stationary points, which share the form of $K = \begin{bmatrix} \end{bmatrix}$ for any $c \in R$, and make ${{\nabla\mathcal{J}}{(K)}} = 0$. Despite this, following Theorem 4.4.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Escaping Suboptimal Stationary Points", "weight": 1.0} -->

‣ 4.2 Global Convergence ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"), the NPG and GN updates provably converge to $K^{\ast}$, which automatically escape other suboptimal stationary points. We numerically evaluate the convergence to $K^{\ast}$ in Figure 4, for both the NPG and GN updates. For each of the 50 trails, we fix a random seed and initialize the algorithm by randomly searching a $K_{0} \in R^{2 \times 2}$ that satisfies $K_{0} \in \mathcal{K}$. It can be observed that two PG methods converge to $K^{\ast}$ in all trails. In start contrast, the vanilla PG update can easily get stuck at these suboptimal stationary points, depending on its initialization.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Escaping Suboptimal Stationary Points", "weight": 1.0} -->

This can be understood as another meaning of *implicit regularization*: for this specific nonconvex problem, two certain search directions automatically bias the iterates to avoid bad local minima, and always towards the global optimal one.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Comparison with Existing $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ Control Solvers", "weight": 1.0} -->

To better justify the superiority of our PO methods, we numerically compare their convergence properties with other numerical $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ mixed control design packages, including the HIFOO method and the h2hinfsyn method implemented in Matlab, which is based on linear matrix inequalities. Note that these full-fledged packages can only handle continuous-time settings. To make the comparison fair, we also implement our PO methods for the continuous-time settings as studied in §A.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Comparison with Existing $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ Control Solvers", "weight": 1.0} -->

We mainly compare them in terms of: 1) the $\mathcal{H}_{2}$ and $\mathcal{H}_{\infty}$ norms of the controller that the algorithms converge to; 2) the *computation complexity* (runtime); 3) the *$\mathcal{H}_{\infty}$-norm constraint violation*. We will validate that our PO methods indeed outperform HIFOO in these aspects. The larger-scale the dynamical system is, the more pronounced our advantages are, with provable robustness preserving guarantees.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Comparison with Existing $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ Control Solvers", "weight": 1.0} -->

Simulation Setup. All the experiments are executed on a MacBook Pro 2019 with a 2.8 GHz Quad-Core Intel Core i7 processor with Matlab R2020b. The device also has a 16GB 2133MHz LPDDR3 memory and an Intel Iris Plus 655 Graphics. To make the runtime comparison fair (or even in favor of HIFOO), we set the following parameters of HIFOO (version 3.501 with Hanso version 2.01): options.fast $= 1$ for using a *fast* optimization method; options.prtlevel $= 0$ to suppress unnecessary printing statements. Other parameters of HIFOO are set to be default. For Matlab's h2hinfsyn function, tol has been set to $10^{- 6}$.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Comparison with Existing $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ Control Solvers", "weight": 1.0} -->

For our PO methods, we set the stepsizes of the NPG and GN updates to be $1/{({2{\| R\|}})}$ and $1/2$, respectively, and solve the following mixed design problems Cases 3-6 until ${{\mathcal{J}{(K)}} - {\mathcal{J}{(K^{\ast})}}} < 10^{- 6}$.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Comparison with Existing $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ Control Solvers", "weight": 1.0} -->

A Simple Example. We first consider a simple setting, denoted by Case 3. The time-invariant system dynamics are characterized by $\overset{˙}{x} = {{Ax} + {Bu} + {Dw}}$, $z = {{Cx} + {Eu}}$, where One can verify that ${E^{\top}{\lbrack{CE}\rbrack}} = {\lbrack 0,I\rbrack}$, satisfying our assumption. Then, we solve The simulations are run over 100 trails with the random seed being fixed at $1,\cdots,100$, respectively. The optimal (minimax) disturbance attenuation level of Case 3 is $\gamma^{\ast} \approx 0.53$, as computed/verified both by Matlab's hinfsyn function and HIFOO's hifoo(P, 'h') function.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Comparison with Existing $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ Control Solvers", "weight": 1.0} -->

We summarize the following interesting findings based on the comparisons between HIFOO and our PO methods in Table 1: (PO methods achieve lower $\mathcal{H}_{2}$ and $\mathcal{H}_{\infty}$ norms, faster). When $\gamma = 5$, both HIFOO and PO methods preserve the ${\|{\mathcal{T}{(K)}}\|}_{\infty} < \gamma$ constraint during the optimization process, and output some convergent gain matrix $K$. However, HIFOO converges to a *local* minimum due to that it is directly optimizing the $\mathcal{H}_{2}$ norm of the closed-loop transfer function, and the landscape for such an optimization problem is unclear. In contrast, our PO methods, by definition, optimize an *upper bound* of the $\mathcal{H}_{2}$-norm, and as proved theoretically, converge to the *global* minimum of the problem.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Comparison with Existing $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ Control Solvers", "weight": 1.0} -->

The solution yields lower values for ${\|{\mathcal{T}{(K)}}\|}_{2}$ and ${\|{\mathcal{T}{(K)}}\|}_{\infty}$ compared to those of the HIFOO output. Indeed, this shows that minimizing the $\mathcal{H}_{2}$-norm upper bound as in Bernstein and Haddad; Mustafa and Bernstein and our paper can obtain reasonably good solutions. More importantly, the average runtimes of our PG methods average over 100 trails are around $5.93 \times$ faster than HIFOO.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Comparison with Existing $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ Control Solvers", "weight": 1.0} -->

(PO methods always preserve $\mathcal{H}_{\infty}$-norm constraint). When $\gamma = 3$ (which is still far from $\gamma^{\ast} \approx 0.53$), our methods consistently preserve the ${\|{\mathcal{T}{(K)}}\|}_{\infty} < \gamma$ constraint during the optimization process, validating our theoretical findings. However, the HIFOO iterates have reached ${\|{\mathcal{T}{(K)}}\|}_{\infty} = 3.4353 > 3$ along the way. Further, PO methods also find solutions that have lower ${\|{\mathcal{T}{(K)}}\|}_{2}$ and ${\|{\mathcal{T}{(K)}}\|}_{\infty}$ norms, with a $5.85 \times$ faster runtime.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Comparison with Existing $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ Control Solvers", "weight": 1.0} -->

(Smaller $\gamma$ leads to worse performance for HIFOO). When $\gamma = 1$, our PO methods still preserve the ${\|{\mathcal{T}{(K)}}\|}_{\infty} < \gamma$ constraint during the optimization process. Our PO methods also converge to the optimum point with both small $\mathcal{H}_{2}$ and $\mathcal{H}_{\infty}$ norms, while HIFOO's performance is degraded much more. We remark that in this case, the runtime of our methods is longer than that of HIFOO, however, the time was mostly consumed in finding the initialization that is robustly stable, by randomly generating $K_{0}$ in a certain region. This becomes harder to find for a smaller $\gamma$. Our simple initialization method takes more than 90% of the time, which might be less efficient than the advanced initialization technique used in HIFOO.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Comparison with Existing $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ Control Solvers", "weight": 1.0} -->

Regarding the comparison with the h2hinfsyn function, we present the results in Table 2. It is shown that in this simple $3 \times 3$ problem, h2hinfsyn and our PG methods converge to nearly the same solution, while our computation time is around $4 \times$ faster. Next, we will show that h2hinfsyn scales poorly with respect to the problem dimensions, while our PO methods converge efficiently in high-dimensional problems.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Comparison with Existing $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ Control Solvers", "weight": 1.0} -->

More Challenging Cases. We test some more challenging cases with higher dimensions to further demonstrate the efficiency of our PO methods. In Cases 4-6, the dimensions of the control gain matrices are ${15 \times 15},{60 \times 60},{90 \times 90}$, respectively, corresponding to the number of decision variables being $225$, $3600$, $8100$, respectively. Problem parameters are too long to enumerate here, and are provided at here, together with all the code and data.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Comparison with Existing $\\mathcal{H}_{2}/\\mathcal{H}_{\\infty}$ Control Solvers", "weight": 1.0} -->

The simulations are run over 10 trails with fixed random seeds. Both HIFOO, h2hinfsyn, and our PO methods converge to almost the same control gain matrices in these cases, without constraint violation. This again implies that minimizing the $\mathcal{H}_{2}$-norm upper bound (instead of $\mathcal{H}_{2}$-norm directly) can usually achieve quite competitive solutions. Notably, our PO methods are around $8 \times$, $47 \times$, $295 \times$ faster than HIFOO, respectively, in Cases 4-6, as reported in Table 3. Our PO methods are also much faster than h2hinfsyn, as it can hardly solve Cases 5-6 and fails to return a solution even after very long runtime.. This verifies that our PO algorithms indeed enjoy better scalability, and the higher the dimension is, the more pronounced our advantage is. These observations have justified that our PO methods are not only theoretically sound, but also numerically competitive.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

In this paper, we have investigated the convergence theory of policy optimization methods for $\mathcal{H}_{2}$ linear control with $\mathcal{H}_{\infty}$-norm robustness guarantees. Viewed as a constrained nonconvex optimization, this problem was addressed by PO methods with provable convergence to the global optimal policy. More importantly, we showed that the proposed PO methods enjoy the implicit regularization property, despite the lack of coercivity of the cost function. We expect the present work to serve as an initial step toward further understanding of RL algorithms on robust/risk-sensitive control tasks. We conclude this main part of the paper with several ongoing/potential research directions.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Implicit regularization of other PO methods", "weight": 1.0} -->

It is of particular interests to investigate whether other PO methods enjoy similar implicit regularization properties. One important example that has not been analyzed in this paper is the PG method. Notice that the model-free implementation of the PG method, see update (3.3), does not require the connection between mixed design and zero-sum LQ games, as the gradient can be sampled via zeroth-order methods directly. Among other examples are quasi-Newton methods with pre-conditioning matrices other than that in (3.5), accelerated PG using the idea from Nesterov, and variance reduced PG methods.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Linear quadratic games", "weight": 1.0} -->

Thanks to the connection discussed in §6.1, our LMI-based techniques for showing implicit regularization in Theorem 4.3. ‣ 4.1 Implicit Regularization ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") may be of independent interest to improve the convergence of nested policy gradient methods in Zhang et al., and even simultaneously-moving policy-gradient methods, for solving zero-sum LQ games using PO methods. This will place PO methods for multi-agent RL (MARL) under a more solid theoretical footing, as LQ games have served as a significant benchmark for MARL. Rigorous analysis for this setting have been partially addressed in our ongoing work, and in a more recent work Bu et al..

<!-- chunk {"id": "body-0100", "role": "body", "section": "Model-based v.s. model-free methods for robust control", "weight": 1.0} -->

There is an increasing literature in *model-based* learning-based control with robustness concerns. On the other hand, our work serves as an intermediate step toward establishing the sample complexity of model-free PO methods for this setting. Hence, it is natural and interesting to compare the data efficiency (sample complexity) and computational scalability of the two lines of work. Note that such a comparison has been made in Tu and Recht for LQR problems without addressing the issue of robustness.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Beyond LTI systems and state-feedback controllers", "weight": 1.0} -->

It is possible to extend our analysis to the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control of other types of dynamical systems such as periodic systems, Markov jump linear systems, and switching systems. These more general system models are widely adopted in control applications, and extensions to these cases will significantly expand the utility of our theory. On the other hand, it is interesting while challenging to study PO for *output-feedback* mixed design, where a dynamic controller parameterized by $(A_{K},B_{K},C_{K},D_{K})$ is synthesized. This way, the PO landscape depends on the order of the parameterization, making the analysis more involved.

<!-- chunk {"id": "body-0102", "role": "body", "section": "PO landscape and algorithms for $\\mathcal{H}_{\\infty}$ control synthesis", "weight": 1.0} -->

Our algorithms are based on the condition that an initial policy satisfying the specified $\mathcal{H}_{\infty}$-norm constraint is available. To efficiently find such an initialization, it is natural to study the PO landscape of $\mathcal{H}_{\infty}$ control synthesis, where the goal is to find the controller that not only satisfies certain $\mathcal{H}_{\infty}$-norm bound, but also minimizes it. It seems that the cost function for $\mathcal{H}_{\infty}$ control is still coercive. However, the main challenge of PO for $\mathcal{H}_{\infty}$ control is that the cost function is non-smooth, which necessitates the use of subgradient methods. The LMI arguments developed here may shed new lights on the convergence analysis of these methods.
