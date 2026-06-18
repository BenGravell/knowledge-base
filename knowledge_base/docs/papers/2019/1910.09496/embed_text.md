## Introduction

Recent years have witnessed tremendous success of reinforcement learning (RL) in various sequential decision-making applications and continuous control tasks. Interestingly, most successes hinge on the algorithmic framework of *policy optimization* (PO), umbrellaing policy gradient (PG) methods, actor-critic methods, trust-region and proximal PO methods, etc. This inspires an increasing interest in studying the convergence theory, especially global convergence to optimal policies, of PO methods; see recent progresses in both classical RL contexts, and continuous control benchmarks.

Indeed, PO provides a general framework for control design.^11^1Hereafter, we will mostly adhere to the terminologies and notational convention in the control literature, which are equivalent to, and can be easily translated to those in the RL literature, e.g., cost v.s. reward, control v.s. action, etc. Consider a general control design problem for the following discrete-time nonlinear dynamical system

where $x_{k}$ is the state, $u_{k}$ is the control input, and $w_{k}$ is the process noise. Formally, PO is a constrained optimization problem ${\min_{K \in \mathcal{K}}\mathcal{J}}{(K)}$, where the decision variable $K$ is determined by the controller parameterization, the cost function $\mathcal{J}{(K)}$ is a pre-specified control performance measure, and the feasible set $\mathcal{K}$ carries the information of the constraints on the controller $K$. These concepts are briefly reviewed as follows.

Optimization variable $K$: The control input $u_{k}$ is typically determined by a feedback law $K$ which is also termed as a *controller*. In the simplest case where a LTI state-feedback controller is used, $K$ is parameterized as a static matrix and $u_{k}$ is given as $u_{k} = {- {Kx_{k}}}$. Then this matrix $K$ becomes the decision variable of the PO problem. For the so-called linear output feedback case where the state $x_{k}$ is not directly measured, the controller can be either a memoryless mapping or an LTI dynamical system. Hence, $K$ can be parameterized by either a static matrix or some state/input/output matrices $(A_{K},B_{K},C_{K},D_{K})$. It is also possible to deploy nonlinear controllers and parameterize $K$ as either polynomials, kernels, or deep neural networks.

Objective function $\mathcal{J}{(K)}$: $\mathcal{J}{(K)}$ is specified to assess the performance of a given controller $K$. The cost function design is more of an art than a science. Popular choices of such cost functions include $\mathcal{H}_{2}$ or $\mathcal{H}_{\infty}$-norm (or some related upper bounds) for the resultant feedback systems. For standard RL models that are based on Markov decision processes (MDPs), the cost $\mathcal{J}{(K)}$ usually has an additive structure over time. For instance, in the classical linear quadratic regulator (LQR) or state-feedback LQ Gaussian (LQG) problems, the cost is ${\mathcal{J}{(K)}}:={\sum_{t = 0}^{\infty}{E{\lbrack{{x_{t}^{\top}Qx_{t}} + {u_{t}^{\top}Ru_{t}}}\rbrack}}}$, which also has an $\mathcal{H}_{2}$-norm interpretation. Nevertheless, $\mathcal{J}{(K)}$ does not necessarily have an additive structure. We will further discuss the specification of $\mathcal{J}{(K)}$ in §2.2.

Feasible set $\mathcal{K}$: Constraints on the decision variable $K$ are posed to account for either the stability, robustness, or safety concerns on the system. A common, though sometimes implicit, example in continuous control tasks is the stability constraint, i.e. $K$ is required to stabilize the closed-loop dynamics. There are also other constraints related to robustness or safety concerns in control design. The constraints will naturally confine the policy search to a feasible set $\mathcal{K}$. The cost function $\mathcal{J}{(K)}$ is either $\infty$ or just undefined for $K\mathcal{K}$.

To ensure the feasibility of $K$ on the fly as the PO methods proceed, projection of the iterates onto the set $\mathcal{K}$ seems to be the first natural approach that comes to mind. However, such a projection may not be computationally efficient or even tractable. For example, projection onto the stability constraint in LQR problems can hardly be computed, as the set $\mathcal{K}$ therein is well known to be nonconvex. Fortunately, such a projection is not needed to preserve the feasibility of the iterates in PG-based methods, as recently reported by Fazel et al.; Bu et al.. In particular, Bu et al. has identified that the cost of LQR has the *coercive* property, such that it diverges to infinity as the controller $K$ approaches the boundary of the feasible set $\mathcal{K}$. In other words, the cost of LQR serves as a barrier function on $\mathcal{K}$. This way, the level set of the cost becomes compact, and the decrease of the cost ensures the next iterate to stay inside the level set, which further implies the stay inside $\mathcal{K}$. This desired property is further illustrated in Figure 1(a), where $K$ and $K^{\prime}$ are two consecutive iterates, and the level set $\left. \{\overset{\sim}{K} \middle| {{\mathcal{J}{(\overset{\sim}{K})}} \leq {\mathcal{J}{(K)}}}\} \right.$ is always separated from the set $\mathcal{K}^{c}$ by some distance $\delta > 0$. Hence, as long as ${\|{K - K^{\prime}}\|} < \delta$, the next iterate $K^{\prime}$ still stays in the set $\mathcal{K}$. More importantly, such a separation distance $\delta$ can be re-used for the next iterate, as the next level set is at least $\delta$ away from $\mathcal{K}^{c}$. By induction, this allows the existence of a constant stepsize that can guarantee the controllers' stability along the iterations. It is worth emphasizing that such a property is *algorithm-agnostic*, in the sense that it is dictated by the cost, and independent of the algorithms adopted, as long as they follow any descent directions of the cost.

Besides the stability constraint, another commonly used one in the control literature is the so-called *$\mathcal{H}_{\infty}$ constraints*. This type of constraints plays a fundamental role in robust control and risk-sensitive control. Based on the well-known small gain theorem, such constraints can be used to guarantee robust stability/performance of the closed-loop systems when model uncertainty is at presence. Compared with LQR under the stability constraint, control synthesis under the $\mathcal{H}_{\infty}$ constraint leads to a fundamentally different optimization landscape, over which the behaviors of PO methods have not been fully investigated yet. In this paper, we take an initial step towards understanding the theoretical aspects of policy-based RL methods on robust/risk-sensitive control problems.

Specifically, we establish a convergence theory for PO methods on $\mathcal{H}_{2}$ linear control problems with $\mathcal{H}_{\infty}$ constraints, referred to as *mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ state-feedback control design* in the robust control literature. As the name suggests, the goal of mixed design is to find a robust stabilizing controller that minimizes an upper bound for the $\mathcal{H}_{2}$-norm, under the restriction that the $\mathcal{H}_{\infty}$-norm on a certain input-output channel is less than a pre-specified value. The $\mathcal{H}_{\infty}$ constraint is explicitly posed here to guarantee the robustness of the closed-loop system to some extent. This general framework also includes risk-sensitive linear control, modeled as linear exponential quadratic Gaussian (LEQG) problems as a special case, when a certain upper bound of $\mathcal{H}_{2}$-norm is used. Detailed formulation for such $\mathcal{H}_{2}$ linear control with $\mathcal{H}_{\infty}$ constraint is provided in §2. In contrast to LQR, two challenges exist in the analysis of PO methods for mixed design problems. First, by definition of $\mathcal{H}_{\infty}$-norm, the constraint is defined in the frequency domain, and is hard to impose, for instance, by directly projecting the iterates in that domain, especially in the context of RL when the system model is unknown. Note that preserving the constraint bound of $\mathcal{H}_{\infty}$-norm as the controller updates is critical in practice, since violation of it can cause catastrophic consequences on the system. Second, more importantly, the coercive property of LQR fails to hold for mixed design problems, as illustrated in Figure 1(b) (and formally established later). Particularly, the cost value, though undefined outside the set $\mathcal{K}$, remains *finite* around the boundary of $\mathcal{K}$. Hence, the decrease of cost from $K$ to $K^{\prime}$ cannot guarantee that the iterate does not travel towards, and even beyond the feasibility boundary. With no strict separation between the cost level set and $\mathcal{K}^{c}$, there may not exist a constant stepsize that induces global convergence to the optimal policy.

These two challenges naturally raise the question: does there exist any computationally tractable PO method, which preserves the robustness constraint along the iterations, and enjoys (hopefully global) convergence guarantees? We provide a positive answer to this question in the present work. Our key contribution is three-fold: First, we study the landscape of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design problems for both discrete- and continuous-time settings, and propose three policy-gradient based methods, inspired by those for LQR. Second, we prove that two of them (the Gauss-Newton method and the natural PG method) enjoy the *implicit regularization* property, such that the iterates are automatically biased to satisfy the required $\mathcal{H}_{\infty}$ constraint. Third, we establish the global convergence of those two PO methods to the *globally optimal* policy with *globally sublinear* and *locally (super-)linear* rates under certain conditions, despite the nonconvexity of the problem. In particular, the two policy search directions always lead to convergence to the global optimum, without getting stuck at any spurious stationary point/local optima. Along the way, we also derive new results on linear risk-sensitive control, i.e., LEQG problems, and discuss the connection of mixed design to zero-sum LQ dynamic games, for designing model-free versions of the algorithms. We expect our work to help pave the way for rigorous understanding of PO methods for general optimal control with $\mathcal{H}_{\infty}$ robustness guarantees.

(b) Landscape of Mixed ℋ2/ℋ∞ Control

Figure 1: Comparison of the landscapes of LQR and mixed ℋ2/ℋ∞ control design that illustrates the hardness of showing convergence of the latter. The dashed lines represent the boundaries of the constraint sets 𝒦. For (a) LQR, 𝒦 is the set of all linear stabilizing state-feedback controllers; for (b) mixed ℋ2/ℋ∞ control, 𝒦 is set of all linear stabilizing state-feedback controllers satisfying an extra ℋ∞ constraint on some input-output channel. The solid lines represent the contour lines of the cost 𝒥 (K). K and K′ denote the control gain of two consecutive iterates; denotes the global optimizer.

Note that the concept of (implicit) regularization has been adopted in many recent works on nonconvex optimization, including training neural networks, phase retrieval, matrix completion, and blind deconvolution, referring to any scheme that biases the search direction of the optimization algorithms. The term *implicit* emphasizes that the algorithms without regularization may behave as if they are regularized. This property has been advocated as an important feature of gradient-based methods for solving aforementioned nonconvex problems. We emphasize that it is a feature of both the *problem* and the *algorithm*, i.e., it holds for certain algorithms that solve certain problems. This is precisely the case in the present work. The specific search directions of the Gauss-Newton and the natural PG methods bias the iterates towards the set of the stabilizing controllers satisfying the $\mathcal{H}_{\infty}$ constraint, although no explicit regularization, e.g., projection, is adopted, which contrasts to that the stability-preserving of PO methods for LQR problems is algorithm-agnostic. To the best of our knowledge, our work appears to be the first studying the implicit regularization properties of PO methods for *learning-based control* in general.

### Related Work

Mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ & Risk-Sensitive Control. The history of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control design dates back to the seminal works Bernstein and Haddad; Khargonekar and Rotea for continuous-time settings, built upon the Riccati equation approach and the convex optimization approach, respectively. Such a formula can be viewed as a surrogate/sub-problem of the more challenging $\mathcal{H}_{\infty}$-control problem, where the goal is to find the optimal controller that minimizes the $\mathcal{H}_{\infty}$-norm. These formulation and approaches were then investigated for discrete-time systems in Mustafa and Bernstein; Kaminer et al.. A non-smooth constrained optimization perspective for solving mixed design problems was adopted in Apkarian et al., with proximity control algorithm designed to handle the constraints explicitly, and convergence guarantees to stationary-point controllers. Numerically, there also exist other packages for multi-objective $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control that are based on non-smooth nonconvex optimization. However, in spite of achieving impressive numerical performance, these methods have no theoretical guarantees for either the global convergence or the $\mathcal{H}_{\infty}$-norm constraint violation. It is also not clear yet how these methods can be made *model-free*. On the other hand, risk-sensitive control with exponential performance measure was originally proposed by Jacobson for the linear quadratic case, and then generalized in Whittle; Fleming and Hernández-Hernández; Borkar and Meyn; Jaśkiewicz et al.. Under certain conditions on the cost, noise, and risk factor, convex optimization perspectives on linear risk sensitive control have been reported in Dvijotham et al.. Recently, first-order optimization methods have also been applied to finite-horizon risk sensitive nonlinear control, but the control inputs (instead of the policy) are treated as decision variables. Convergence to stationary points was shown therein for the iterative LEQG algorithm. Interestingly, there is a relationship between mixed design and risk-sensitive control, as established in Glover and Doyle; Whittle. These two classes of problems can also be unified with maximum-entropy $\mathcal{H}_{\infty}$ control and zero-sum dynamic games. Besides these direct controller/policy search methods, general mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control can also be tackled via Youla-parameterization based approaches, which lead to convex programming problems that can be solved numerically. However, actual implementation of these approaches either require a finite-horizon *truncation* of system impulse responses, which loses optimality guarantees, or require solution of (a large enough sequence of ) semi-definite programs or linear matrix inequalities with lifted dimensions, which may not be computationally efficient for large-scale dynamical systems. More importantly, it is not clear yet how to implement these approaches in the data-driven regime, without identifying the model. In contrast, the direct search methods can easily be made model-free, see e.g., our recent attempt Zhang et al. for robust control design.

Constrained MDP & Safe RL. The mixed design formulation is also pertinent to constrained dynamic control problems, usually modeled as constrained MDPs (CMDPs). However, the constraint in CMDPs is generally imposed on either the expected long-term cost, which shares the additive-in-time structure as the objective, or some risk-related constraint. Those constraints are in contrast to the $\mathcal{H}_{\infty}$ robustness constraint considered here. Under the CMDP model, various *safe RL* algorithms, especially PO-based ones, have been developed. It is worth mentioning that except Achiam et al.; Chow et al., other algorithms cannot guarantee the constraint to be satisfied during the learning iterations, as opposed to our on-the-fly implicit regularization property. Recently, safety constraint has also been incorporated into the LQR model for *model-based* learning control. Several recent model-based safe RL algorithms include Garcia and Fernández; Aswani et al.; Akametalu et al.; Berkenkamp et al..

PO for LQR. PO for LQR stemmed from the adaptive policy iteration algorithm in Bradtke et al.. Lately, studying the global convergence of policy-gradient based methods for LQR has drawn increasing attention. Specifically, Fazel et al. first identified the landscape of PO for LQR problems that stationary point implies global optimum, which motivated the development of first-order methods for solving this nonconvex problem. A more comprehensive landscape characterization was then reinforced in Bu et al., where the *coercive* property of LQR cost was explicitly mentioned. Based on these, Malik et al. advocated two-point zeroth-order methods to improve the sample complexity of model-free PG; Yang et al. proposed actor-critic algorithms with non-asymptotic convergence guarantees; Tu and Recht compared the asymptotic behavior of model-based and model-free PG methods, with focus on *finite-horizon* LQR problems. Recently, the continuous-time setup has been considered in Mohammadi et al., and the extensions to Markov jump linear quadratic control have been presented in Jansch-Porto et al.. Moreover, Gravell et al. considered LQR with multiplicative noises, in order to improve the controller's robustness. The robustness issue for the output feedback case has been further discussed in Venkataraman and Seiler.

Robust RL. Robustness with respect to the model uncertainty/misspecification has long been a significant concern in RL. Indeed, the early attempt for robust RL was based on the notion of $\mathcal{H}_{\infty}$ robustness considered here, where the uncertainty was modeled as the control of an adversarial agent playing against the nominal controller. This game-theoretic perspective, as we will also discuss in §6.1, enabled the development of actor-critic based algorithms therein, though without theoretical analysis. Such an idea has recently been carried forward in the empirical work Pinto et al., which proposed PO methods alternating between the two agents. Another line of work follows the *robust MDP* framework, with RL algorithms developed in Lim et al.; Lim and Autef; Tessler et al.; Mankowitz et al.. However, these algorithms apply to only tabular/small-scale MDPs (not continuous control tasks) and/or do not belong to PO methods that guarantee robustness during learning. More recently, linear control design against adversarial disturbances has also been placed in the online learning context to achieve nearly-optimal regret, where either the dynamics or the cost functions are adversarially changing. Model-based methods also exist for continuous control tasks.

### Notation

For two matrices $A$ and $B$ of proper dimensions, we use $\operatorname{Tr}{({AB})}$ to denote the trace of $AB$. For any $X \in R^{d \times m}$, we use ${\text{vec}{(X)}} \in {R^{dm},{\rho{(X)}},{\| X\|},{\| X\|}_{F},{\sigma_{\max}{(X)}},{\sigma_{\min}{(X)}}}$ to denote the vectorization, the spectral radius, the operator norm, the Frobenius norm, the largest and smallest singular values of $X$, respectively. If $X \in R^{m \times m}$ is square, we use $X > 0$ (resp. $X \geq 0$) to denote that $X$ is positive definite (resp. nonnegative definite), i.e., for any nonzero vector $v \in R^{n}$, ${v^{\top}{({X^{\top} + X})}v} > 0$ (resp. ${v^{\top}{({X^{\top} + X})}v} \geq 0$). For a symmetric matrix $X$, we use $\lambda_{\max}{(X)}$ and $\lambda_{\min}{(X)}$ to denote, respectively, its largest and smallest eigenvalues. We use $\otimes$ to denote the Kronecker product. We use $I$ and $0$ to denote the identity matrix and all-zero matrix of proper dimensions. We use $\mathcal{N}{(\mu,)}$ to denote the Gaussian distribution with mean $\mu$ and covariance matrix. For any integer $m > 0$, we use $\lbrack m\rbrack$ to denote the set of integers $\{ 1,\cdots,m\}$. For any complex number $c \in C$, we use $\Re c$ to denote the real part of $c$. We use $G:=\begin{bmatrix}
\end{bmatrix}$ to denote the input-output transfer function of the following state-space linear dynamical systems:

which can also be written as ${G{(z)}} = {{C{({{zI} - A})}^{- 1}B} + D}$ and ${G{(s)}} = {{C{({{sI} - A})}^{- 1}B} + D}$ for discrete- and continuous-time systems, respectively. The $\mathcal{H}_{\infty}$-norm ${\| G\|}_{\infty}$ is then defined as

## Preliminaries

We first provide some preliminary results on $\mathcal{H}_{2}$ linear control with $\mathcal{H}_{\infty}$ robustness guarantees. Throughout this section, and the following sections in the main text, we will focus on systems in discrete time. Counterparts of these results for continuous-time systems are included in Appendix §A.

### Motivating Example: LEQG

We start with an example of *risk-sensitive* control, the *infinite-horizon state-feedback linear exponential quadratic Gaussian* problem^22^2Unless otherwise noted, we will just refer to this problem as LEQG hereafter., which is motivating in that: i) it is closely related to the well-known linear optimal control problems, e.g., LQR and state-feedback LQG; ii) it illustrates the idea of mixed control design, especially introducing the $\mathcal{H}_{\infty}$-norm constraint, though implicit, that guarantees robustness. The latter manifests the challenge in the convergence analysis of PO methods for this problem.

Specifically, at time $t \geq 0$, the agent takes an action $u_{t} \in R^{d}$ at state $x_{t} \in R^{m}$, which leads the system to a new state $x_{t + 1}$ by a linear dynamical system

where $A$ and $B$ are matrices of proper dimensions, $x_{0} \in R^{m}$ and ${w_{t} \in R^{m}},{{\forall t} \geq 0}$ are independent zero-mean Gaussian random variables with positive-definite covariance matrices $X_{0}$ and $W$, respectively. The one-stage cost of applying control $u$ at state $x$ is given by ${c{(x,u)}} = {{x^{\top}Qx} + {u^{\top}Ru}}$, where $Q$ and $R$ are positive-definite matrices. Then, the long-term cost to minimize is

where $\beta$ is the parameter that describes the intensity of risk-sensitivity, and the expectation is taken over the randomness of both $x_{0}$ and $w_{t}$ for all $t \geq 0$. The intuition behind the objective (2.1) is that by Taylor series expansion around $\beta = 0$,

Hence, if $\beta > 0$, the control is *risk-averse* since minimization also places positive weight on the variance, in addition to the expectation, of the cost; in contrast, if $\beta < 0$, the control is referred to as *risk-seeking*, which encourages the variance to be large. As $\beta\rightarrow 0$, the objective (2.1) reduces to the *risk-neutral* objective of LQR/state-feedback LQG. Usually LEQG problems consider the case of $\beta > 0$. In this sense, LEQG can be viewed as a generalization of LQR/state-feedback LQG problems.

The goal of LEQG is to find the optimal control policy $\mu_{t}:{{{({R^{m} \times R^{d}})}^{t} \times R^{m}}\rightarrow R^{d}}$, which in general is a mapping from the history of state-action pairs till time $t$ and current state $x_{t}$, to the action $u_{t}$ in $R^{d}$, that minimizes the cost in (2.1). By assuming that such an optimal policy exists, the $\operatorname{lim\ sup}$ in (2.1) can be replaced by $\lim$. Moreover, we can show, see a formal statement in Lemma C.2 in §C, that the optimal control has a desired property of being memoryless and *stationary*, i.e., *linear time-invariant* (LTI), and current *state-feedback*, i.e., ${{\mu_{t}{(x_{0:t},u_{0:{t - 1}})}} = {\mu{(x_{t})}} = {- {Kx_{t}}}},$ for some $K \in R^{d \times m}$. Hence, it suffices to optimize over the control gain $K$, without loss of optimality, i.e.,

### Cost Closed-Form

To solve (2.2) with PO methods, it is necessary to establish the closed-form of the objective with respect to $K$. To this end, we introduce the following algebraic Riccati equation

for given control gain $K$. If $\beta\rightarrow 0$, (2.3) reduces to the Lyapunov equation of policy evaluation for given $K$ in LQR problems. For notational simplicity, we also define ${\overset{\sim}{P}}_{K}$ as

Then, the objective $\mathcal{J}{(K)}$ can be expressed by the solution to (2.3), $P_{K}$, as follows.

### Lemma 2.1

For any stabilizing LTI state-feedback controller $u_{t} = {- {Kx_{t}}}$, such that the Riccati equation (2.3) admits a solution $P_{K} \geq 0$ that: i) is stabilizing, i.e., ${\rho\left( {{({A - {BK}})}^{\top}{({I - {\betaP_{K}W}})}^{- 1}} \right)} < 1$, and ii) satisfies ${W^{- 1} - {\betaP_{K}}} > 0$, $\mathcal{J}{(K)}$ has the form of

Note that when $\beta\rightarrow 0$, the objective (2.5) reduces to $\operatorname{Tr}{({P_{K}W})}$, the cost function for LQG problems.

### Remark 2.2 (New Results on LEQG)

To the best of our knowledge, our results on that the optimal controller is LTI state-feedback in Lemma C.2, and on the form of the objective $\mathcal{J}{(K)}$ in Lemma 2.1, though expected, have not been rigorously established for LEQG problems in the literature. For completeness, we present a self-contained proof in §C. Interestingly, the former argument has been hypothesized in Section $3$ of Glover and Doyle; while the form of $\mathcal{J}{(K)}$ in (2.5) connects to the performance criterion for more general optimal control problems with robustness guarantees, as to be shown shortly.

### Implicit Constraint on $\mathcal{H}_{\infty}$-Norm

Seemingly, (2.2) is an unconstrained optimization over $K$. However, as identified by Glover and Doyle, there is an implicit constraint set for this problem, which corresponds to the lower-level set of the $\mathcal{H}_{\infty}$-norm of the closed-loop transfer function under the linear stabilizing controller $u = {- {Kx}}$. We reiterate the result as follows.

### Lemma 2.3 (Glover and Doyle (1988))

Consider the LEQG problem in (2.2) that finds the optimal stationary state-feedback control gain $K$, and a closed-loop transfer function from the noise $\{ w_{t}\}$ to the output, $\mathcal{T}{(K)}$, as

Then, the feasible set of $\mathcal{J}{(K)}$ is the intersection of the set of linear stabilizing feedback controllers and the $1/\sqrt{\beta}$-lower-level set of the $\mathcal{H}_{\infty}$-norm of $\mathcal{T}{(K)}$, i.e., $\left\{ K \middle| {{{\rho{({A - {BK}})}{<{1,\text{and}}\parallel}\mathcal{T}{(K)}}\parallel}_{\infty} < {1/\sqrt{\beta}}} \right\}$.

### Proof

The result follows by applying the results in Section $3$ in Glover and Doyle, writing out the transfer function, and replacing the $\theta$ therein by the $- \beta$ here. ∎

We note that the feasible set for LEQG in Lemma 2.3). ‣ 2.1.2 Implicit Constraint on ℋ_∞-Norm ‣ 2.1 Motivating Example: LEQG ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") may not necessarily be bounded. This feasible set, though quite concise to characterize, is hard to enforce directly onto the control gain $K$, since it is a frequency-domain characterization using the $\mathcal{H}_{\infty}$-norm. To develop PO algorithms for finding $K$, the time-domain characterization in Lemma 2.1 is more useful. Interestingly, as we will show shortly, the conditions that lead to the form of $\mathcal{J}{(K)}$ in Lemma 2.1 are indeed equivalent to the feasible set given by $\mathcal{H}_{\infty}$-norm constraint in Lemma 2.3). ‣ 2.1.2 Implicit Constraint on ℋ_∞-Norm ‣ 2.1 Motivating Example: LEQG ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"); see Remark 2.8. ‣ 2.3 Bounded Real Lemma ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence").

In fact, this reformulation of LEQG as a constrained optimization problem, belongs to a general class problems, *mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control design* with state-feedback.

### Bigger Picture: Mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ Control Synthesis

Consider the following discrete-time linear dynamical system with a single input-output channel

where ${x_{t} \in R^{m}},{u_{t} \in R^{d}}$ denote the states and controls, respectively, $w_{t} \in R^{n}$ is the disturbance, $z_{t} \in R^{l}$ is the controlled output, and $A,B,C,D,E$ are matrices of proper dimensions. Consider the *admissible* control policy $\mu_{t}$ to be a mapping from the history of state-action pairs till time $t$ and the current state $x_{t}$ to action $u_{t}$. It has been shown in Kaminer et al. that, *LTI* state-feedback controller (without memory) suffices to achieve the optimal performance of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design under this *state-feedback* information structure^33^3For discrete-time settings, if both the (exogenous) disturbance $w_{t}$ and the state $x_{t}$ are available, i.e., under the *full-information* feedback case, LTI controllers may not be optimal. Interestingly, for continuous-time settings, LTI controllers are indeed optimal.. As a consequence, it suffices to consider only stationary, current state-feedback controller parametrized as $u_{t} = {- {Kx_{t}}}$.

### Remark 2.4 (Justification of LTI Control for LEQG)

As to be shown shortly, LEQG is a special case of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design. Hence, the result we derived in Lemma C.2, i.e., the optimal controller of LEQG is indeed LTI, is consistent with this earlier result on mixed design from Khargonekar and Rotea; Kaminer et al..

In accordance with this parametrization, the transfer function from the disturbance $w_{t}$ to the output $z_{t}$ can be represented as

In common with Glover and Doyle; Khargonekar and Rotea; Başar and Bernhard, we make the following assumption on the matrices $A,B,C,D$ and $E$.

### Assumption 2.5

The matrices $A,B,C,D,E$ in (2.9) satisfy ${E^{\top}{\lbrack{CE}\rbrack}} = {\lbrack{0R}\rbrack}$ for some $R > 0$.

Assumption 2.5 is fairly standard, which clarifies the exposition substantially by normalising the control weighting and eliminating cross-weightings between control signal and state. Hence, the transfer function in (2.9) has the equivalent form^44^4Strictly speaking, the transfer functions for (2.9) and (2.12) are equivalent in the sense that the values of $\mathcal{T}^{\sim}{(K)}\mathcal{T}{(K)}$ are the same for all the points on the unit circle. of

Hence, robustness of the designed controller can be guaranteed by the constraint on the $\mathcal{H}_{\infty}$-norm, i.e., ${\|{\mathcal{T}{(K)}}\|}_{\infty} < \gamma$ for some $\gamma > 0$. The intuition behind the constraint, which follows from small gain theorem, is that the constraint on ${\|{\mathcal{T}{(K)}}\|}_{\infty}$ implies that the closed-loop system is *robustly stable* in that any stable transfer function satisfying $\parallel \parallel_{\ell_{2}\rightarrow\ell_{2}} < 1/\gamma$ may be connected from $z_{t}$ back to $w_{t}$ without destablizing the system. For more background on $\mathcal{H}_{\infty}$ control, see Başar and Bernhard; Zhou et al.. For notational convenience, we define the feasible set of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control design as

We note that the set $\mathcal{K}$ may be unbounded.

In addition to the constraint, the objective of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design is usually an upper bound of the $\mathcal{H}_{2}$ norm of the closed-loop system. By a slight abuse of notation, let $\mathcal{J}{(K)}$ be the cost function of mixed design. Then the common forms of $\mathcal{J}{(K)}$ include Mustafa; Mustafa and Bernstein

where $P_{K}$ is the solution to the following Riccati equation

with ${\overset{\sim}{P}}_{K}$ defined as

### Remark 2.6 (LEQG as a Special Case of Mixed-Design)

By Lemma 2.3). ‣ 2.1.2 Implicit Constraint on ℋ_∞-Norm ‣ 2.1 Motivating Example: LEQG ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"), replacing $\beta$, $W$, and $Q$ in LEQG by $\gamma^{- 2}$, $DD^{\top}$ and $C^{\top}C$, respectively, yields the formulation of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design. In particular, the closed-form cost of LEQG that we derived for the first time, see Lemma 2.1, is identical to the cost in (2.15); and the implicit constraint of LEQG in Lemma 2.3). ‣ 2.1.2 Implicit Constraint on ℋ_∞-Norm ‣ 2.1 Motivating Example: LEQG ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") is exactly the $\mathcal{H}_{\infty}$-norm constraint in (2.13). Thus, LEQG is a mixed-design problem with $D = W^{1/2}$ and $\mathcal{J}{(K)}$ being (2.15). Note that ${DD^{\top}} = W > 0$ for LEQG.

All three objectives in (2.14)-(2.16) are upper bounds of the $\mathcal{H}_{2}$-norm. In particular, cost (2.14) has been adopted in Bernstein and Haddad; Haddad et al., which resembles the standard $\mathcal{H}_{2}$ control/LQG control objective, but with $P_{K}$ satisfying a Riccati equation instead of a Lyapunov equation. Cost (2.15) is closely related to maximum entropy $\mathcal{H}_{\infty}$-control, see the detailed relationship between the two in Mustafa and Glover. In addition, cost (2.16) can also be connected to the cost of LQG using a different Riccati equation. As $\gamma\rightarrow\infty$, the costs in all (2.14)-(2.16) reduce to the cost for LQG, i.e., $\mathcal{H}_{2}$ control design problems.

In sum, the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control design can be formulated as

with $\mathcal{J}{(K)}$ and $\mathcal{K}$ defined in (2.14)-(2.16) and (2.13), respectively.

### Bounded Real Lemma

Though the constraint (2.13) is concise, it is hard to enforce over $K$ in policy optimization, since the constraint is defined in the frequency domain. Interestingly, by using a significant result in robust control theory, i.e., *Bounded Real Lemma* constraint (2.13) can be related to the solution of a Riccati equation and a Riccati inequality. We formally introduce the result as follows, whose proof is deferred to §B.1.

### Lemma 2.7 (Discrete-Time Bounded Real Lemma)

Consider a discrete-time transfer function $\mathcal{T}{(K)}$ defined in (2.12), suppose $K$ is stabilizing, i.e., ${\rho{({A - {BK}})}} < 1$, then the following conditions are equivalent:

${\|{\mathcal{T}{(K)}}\|}_{\infty} < \gamma$, which, due to ${\rho{({A - {BK}})}} < 1$, further implies $K \in \mathcal{K}$ with $\mathcal{K}$ defined in (2.13).

The Riccati equation (2.17) admits a unique stabilizing solution $P_{K} \geq 0$ such that: i) ${I - {\gamma^{- 2}D^{\top}P_{K}D}} > 0$; ii) ${({I - {\gamma^{- 2}P_{K}DD^{\top}}})}^{- \top}{({A - {BK}})}$ is stable;

There exists some $P > 0$, such that

where $\overset{\sim}{P}:={P + {PD{({{\gamma^{2}I} - {D^{\top}PD}})}^{- 1}D^{\top}P}}$.

The three equivalent conditions in Lemma 2.7. ‣ 2.3 Bounded Real Lemma ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") will be frequently used in the ensuing analysis. Note that the unique stabilizing solution to (2.17) for any $K \in \mathcal{K}$, is also *minimal*, if the pair $({A - {BK}},D)$ is stabilizable, see. This holds since $K \in \mathcal{K}$ is indeed stabilizing. Thus, the optimal control that minimizes (2.14)-(2.16), which are all monotonically increasing with respect to $P_{K}$, only involves the stabilizing solution $P_{K}$. Hence, it suffices to consider only stabilizing solution $P_{K}$ of the Riccati equation (2.17) for LEQG.

### Remark 2.8 (Necessity of Lemma 2.1)

By Lemma 2.7. ‣ 2.3 Bounded Real Lemma ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") and Remark 2.6. ‣ 2.2 Bigger Picture: Mixed ℋ₂/ℋ_∞ Control Synthesis ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"), the conditions in Lemma 2.1 are equivalent to the $\mathcal{H}_{\infty}$-norm constraint in (2.13) for LEQG. This implies that these conditions are not only *sufficient* for the form of $\mathcal{J}{(K)}$ in Lemma 2.1 to hold, but also *necessary*. In other words, any feasible $K \in \mathcal{K}$ should lead to the form of $\mathcal{J}{(K)}$ in (2.5).

Next, we develop policy optimization algorithms for solving the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control problem in (2.19).

## Landscape and Algorithms

In this section, we investigate the optimization landscape of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control design, and develop policy optimization algorithms with convergence guarantees. In particular, we study both discrete- and continuous-time settings focusing on two representative example costs $\mathcal{J}{(K)}$ from (2.15) and (2.14), respectively.^55^5Although only two example settings are studied in detail, the techniques developed can also be applied to other combinations of settings, e.g., cost (2.14) in discrete-time settings. The first combination of settings also by chance solves the discrete-time LEQG problems introduced in §2.1. The second combination for continuous-time settings is discussed in §A.

### Optimization Landscape

We start by showing that, regardless of the cost $\mathcal{J}{(K)}$, the mixed-design problem in (2.19) is a *nonconvex* optimization problem.

### Lemma 3.1 (Nonconvexity of Discrete-Time Mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ Design)

The discrete-time mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design problem (2.19) is nonconvex.

The proof of Lemma 3.1. ‣ 3.1 Optimization Landscape ‣ 3 Landscape and Algorithms ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") is deferred to §B.2. In particular, we show by an easily-constructed example that the convex combination of two control gains $K$ and $K^{\prime}$ in $\mathcal{K}$ may no longer lie in $\mathcal{K}$. As a result, this nonconvexity poses challenges in solving (2.19) using standard policy gradient-based approaches. Note that similar nonconvexity of the constraint set also exists in LQR problems, and has been recognized as one of the main challenges to address. Still, the landscape of LQR has some desired property of being *coercive*, which played a significant role in the analysis of PO methods for LQR. However, we establish in the following lemma that such a coercivity does not hold for mixed design problems.

### Lemma 3.2 (No Coercivity of Discrete-Time Mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ Design)

The cost functions (2.14)-(2.16) for discrete-time mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design are not coercive. Particularly, as $K\rightarrow{\partial\mathcal{K}}$, where $\partial\mathcal{K}$ is the boundary of the constraint set $\mathcal{K}$, the cost $\mathcal{J}{(K)}$ does not necessarily approach infinity.

The proof of Lemma 3.2. ‣ 3.1 Optimization Landscape ‣ 3 Landscape and Algorithms ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") is provided in §B.3. The key of the argument is that for given $K \in \mathcal{K}$, the *policy evaluation* equation for mixed design problems is a Riccati equation, see (2.17) (a quadratic equation of $P_{K}$ in $1$-dimensional case); while for LQR problems, the policy evaluation equation is a Lyapunov equation, which is essentially linear. Hence, some additional condition on $K$ is required for the existence of the solution, which can be *restricter* than the conditions on $K$ and $P_{K}$ that makes the cost $\mathcal{J}{(K)}$ finite. In this case, the existence condition of the solution characterizes the boundary of $\mathcal{K}$, which leads to a well-defined $P_{K}$, and thus a finite value of the cost $\mathcal{J}{(K)}$, even when $K$ approaches the boundary $\partial\mathcal{K}$.

The lack of coercivity turns out to be the greatest challenge when analyzing the stability/feasibility of PO methods for mixed control design, in contrast to LQR problems. Detailed discussion on this is provided in §4.1. The illustration in Figure 1 in §1 of the landscape of mixed design problems was actually based on Lemmas 3.1. ‣ 3.1 Optimization Landscape ‣ 3 Landscape and Algorithms ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") and 3.2. ‣ 3.1 Optimization Landscape ‣ 3 Landscape and Algorithms ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"). We then show the differentiability of $\mathcal{J}{(K)}$ at each $K$ within the feasible set $\mathcal{K}$, and provide the closed-form of the policy gradient. Here we focus on the most complicated objective defined in (2.15) among the three in (2.14)-(2.16), due to its direct connection to the risk-sensitive control problem; see Remark 2.6. ‣ 2.2 Bigger Picture: Mixed ℋ₂/ℋ_∞ Control Synthesis ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"). We note that the proof can be used directly to establish similar results for the other two objectives, namely, (2.14) and (2.16), too.

### Lemma 3.3

The cost $\mathcal{J}{(K)}$ defined in (2.15) is differentiable in $K$ for any $K \in \mathcal{K}$, and the policy gradient has the following form:

where ${}_{}^{}R^{m \times m}$ is a matrix given by

and ${\overset{\sim}{P}}_{K}$ is defined in (2.18).

The proof of Lemma 3.3 is provided in §B.4. Note that Lemma 3.3 also implies some property on the landscape of $\mathcal{J}{(K)}$. Specifically, if ${}_{}^{}0$ is full-rank, then ${{\nabla\mathcal{J}}{(K)}} = 0$ admits a unique solution $K = {{({R + {B^{\top}{\overset{\sim}{P}}_{K}B}})}^{- 1}B^{\top}{\overset{\sim}{P}}_{K}A}$, which corresponds to the unique global optimum. Otherwise, if ${}_{}^{}0$ is not full-rank, there can be multiple stationary points. Yet, the global optimum is still of the same form. We formally establish this in the following proposition, which is proved in §B.6.

### Proposition 3.4

Suppose that the discrete-time mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design admits a global optimal solution $K^{\ast} \in \mathcal{K}$; then, one such solution has the form of $K^{\ast} = {{({R + {B^{\top}{\overset{\sim}{P}}_{K^{\ast}}B}})}^{- 1}B^{\top}{\overset{\sim}{P}}_{K^{\ast}}A}$. Additionally, if the pair $\left( {{({I - {\gamma^{- 2}P_{K}DD^{\top}}})}^{- \top}{({A - {BK}})}},D \right)$ is controllable at some stationary point of $\mathcal{J}{(K)}$, such that ${{\nabla\mathcal{J}}{(K)}} = 0$, then this is the unique stationary point, and corresponds to the unique global optimizer $K^{\ast}$.

The form of the optimal control gain $K^{\ast}$ above echoes back that of the solution to *finite-horizon* LEQG,. Note that for LEQG problems, $D = W^{1/2} > 0$ implies that the controllability condition holds automatically. Thus, this $K^{\ast}$ corresponds to the *unique* global optimizer. We also remark that the landscape result above can also be shown for the other two objectives (2.14) and (2.16). In fact, the key in proving Proposition 3.4 is to show that $P_{K^{\ast}}$ is *matrix-wise* minimal in the positive semi-definite sense for all $P_{K}$ with $K \in \mathcal{K}$. Note that since the objectives (2.14) and (2.16) are both monotonically non-decreasing in the eigenvalues of $P_{K}$, one can verify that the $K^{\ast}$ is also the global optimizer. Note that $K^{\ast}$ may not be the *unique* global minimizer without the controllability assumption. Finally, following the proof of Lemma 3.3, one can show that the policy gradients for (2.14) and (2.16) yield an almost identical form as in Lemma 3.3, except the definition of ~K~. Although the controllability assumption has been made in the literature, and is also satisfied automatically by LEQG problems, we will show next that our PO methods can find the global optimum $K^{\ast}$ even without this assumption.

### Policy Optimization Algorithms

Consider three policy-gradient based methods as follows. For simplicity, we define

We also suppress the iteration index, and use $K$ and $K^{\prime}$ to represent the control gain before and after one-step of the update.

where $\eta > 0$ is the stepsize. The updates are motivated by and resemble the policy optimization updates for LQR, but with $P_{K}$ therein replaced by ${\overset{\sim}{P}}_{K}$. The natural PG update is related to gradient over a Riemannian manifold; while the Gauss-Newton update is one type of quasi-Newton update, see Bu et al. for further justifications on the updates. In particular, with $\eta = {1/2}$, the Gauss-Newton update (3.5) can be viewed as the *policy iteration* update for infinite-horizon mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design. Model-free versions of the PG update (3.3) can be directly obtained, since the gradient ${\nabla\mathcal{J}}{(K)}$ can be estimated by sampled data, using for instance zeroth-order methods, as in Fazel et al.; Malik et al.. A direct model-free implementation of the natural PG update (3.4) using zeroth-order optimization methods requires estimating the matrix ~K~. It is not clear yet how to estimate it from the sampled trajectories. Instead, we propose one solution by the connections between mixed design and zero-sum linear quadratic games; see §6 for more details. Finally, as in LQR problems, the Gauss-Newton update (3.5) cannot yet be estimated using zeroth-order methods directly.

## Theoretical Results

In this section, we investigate the convergence of the PO methods proposed in §3.

### Implicit Regularization

The first key challenge in the convergence analysis for PO methods, is to ensure that the iterates remain *feasible* as the algorithms proceed, hopefully without the use of *projection*. This is especially significant in mixed design problems, as the feasibility here means *robust stability*, the violation of which can be catastrophic in practical *online* control design. We formally define the concept of *implicit regularization* to describe this feature.

### Definition 4.1 (Implicit Regularization)

For mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control design problem (2.19), suppose an iterative algorithm generates a sequence of control gains $\{ K_{n}\}$. If $K_{n} \in \mathcal{K}$ for all $n \geq 0$, this algorithm is called *regularized*; if it is regularized without projection onto $\mathcal{K}$ for any $n \geq 0$, this algorithm is called *implicitly regularized*.

### Remark 4.2

The concept of *(implicit) regularization* has been adopted in many recent studies on nonconvex optimization, including training neural networks, phase retrieval, matrix completion, and blind deconvolution, referring to any scheme that biases the search direction of gradient-based algorithms. Implicit regularization has been advocated as an important feature of (stochastic) gradient descent methods for solving these problems, which, as the name suggests, means that the algorithms without regularization may behave as if they are regularized. Note that the term *regularization* may refer to several different schemes in different problems, e.g., trimming/truncation the gradient, adding a regularization term in the objective, etc. Here we focus on the scheme of *projection*, as summarized in Ma et al.. Also note that implicit regularization is a feature of both the *problem* and the *algorithm*, i.e., it holds for certain algorithms that solve certain nonconvex problems.

One possible way for the iterates to remain feasible is to keep shrinking the stepsize, whenever the next iterate goes outside $\mathcal{K}$, following for example the Armijo rule. However, as the cost $\mathcal{J}{(K)}$ is not necessarily smooth (see Lemma 5.1. ‣ 5.2 Proof of Theorem 4.4 ‣ 5 Proofs of Main Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") and its discussion later), it may not converge within a finite number of iterations. Another option is to project the iterate onto $\mathcal{K}$. Nonetheless, it is challenging to perform projection onto the $\mathcal{H}_{\infty}$-norm constraint set directly in the frequency domain.

For LQR problems, due to the coercivity of the cost that as $K$ approaches the boundary of the stability/feasibility region $\left. \{{K \in R^{d \times m}} \middle| {{\rho{({A - {BK}})}} < 1}\} \right.$, i.e., as ${\rho{({A - {BK}})}}\rightarrow 1$, the cost blows up to infinity, and due to the fact that the cost is continuous with respect to $K$, the lower-level set of the cost is compact and is contained within the stability region. As a consequence, there is a strict separation between any lower-level set of the cost and the set $\left. \{{K \in R^{d \times m}} \middle| {{\rho{({A - {BK}})}} \geq 1}\} \right.$. Hence, as discussed in the introduction, there exists a *constant stepsize* such that as long as the initialization control is stabilizing, the iterates along the path remain stabilizing and keep decreasing the cost. Such a property is *algorithm-agnostic* in that it is dictated by the property of the cost, and independent of the algorithms adopted, as long as they follow any descent directions of the cost. The stability proofs in Fazel et al.; Bu et al. for LQR are essentially built upon this idea.

In contrast, for mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design problems, lack of coercivity invalidates the argument above, as the control approaching the robustness constraint boundary $\partial\mathcal{K}$ may incur a *finite* cost, and the descent direction may still drive the iterates out of the feasibility region. In addition, there may not exist a strict separation between all the lower-level sets of the cost and the complementary set $\mathcal{K}^{c}$. This difficulty has been illustrated in Figure 1 in the introduction, which compares the landscapes of the two problems. Interestingly, we show in the following theorem that the natural PG and Gauss-Newton methods in (3.4)-(3.5) enjoy the implicit regularization feature, with certain *constant* stepsize. We only highlight the idea of the proof here, and defer the details to §5.1. The proof includes two main steps. First, we directly use $P_{K}$ to construct a Lyapunov function for $K^{\prime}$ to show a non-strict Riccati inequality that guarantees ${\|{\mathcal{T}{(K^{\prime})}}\|}_{\infty} \leq \gamma$. Second, we further perturb $P_{K}$ in a specific way to show the strict inequality ${\|{\mathcal{T}{(K^{\prime})}}\|}_{\infty} < \gamma$. The perturbation argument is inspired by the proof of the Kalman-Yakubovich-Popov (KYP) Lemma.

### Theorem 4.3 (Implicit Regularization for Discrete-Time Mixed Design)

For any control gain $K \in \mathcal{K}$, i.e., ${\rho{({A - {BK}})}} < 1$ and ${\|{\mathcal{T}{(K)}}\|}_{\infty} < \gamma$, with ${\| K\|} < \infty$, suppose that the stepsize $\eta$ satisfies:

Natural policy gradient (3.4): $\eta \leq {1/{({2{\|{R + {B^{\top}{\overset{\sim}{P}}_{K}B}}\|}})}}$,

Gauss-Newton (3.5): $\eta \leq {1/2}$.

Then the $K^{\prime}$ obtained from (3.4)-(3.5) also lies in $\mathcal{K}$. Equivalently, $K^{\prime}$ is stabilizing, i.e., ${\rho{({A - {BK^{\prime}}})}} < 1$, and satisfies that: i) there exists a solution $P_{K^{\prime}} \geq 0$ to the Riccati equation (2.17); ii) ${I - {\gamma^{- 2}D^{\top}P_{K^{\prime}}D}} > 0$; iii) ${\rho\left( {{({I - {\gamma^{- 2}P_{K^{\prime}}DD^{\top}}})}^{- \top}{({A - {BK^{\prime}}})}} \right)} < 1$.

Proof Sketch. The general idea, contrary to the coercivity-based idea that works for any descent direction, is that we focus on the feasibility of $K^{\prime}$ after an update along *certain directions*: either (3.4) or (3.5). By Bounded Real Lemma, i.e., Lemma 2.7. ‣ 2.3 Bounded Real Lemma ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"), the feasibility condition for $K^{\prime}$, if $K^{\prime}$ is stabilizing, is equivalent to the existence of $P > 0$ such that the linear matrix inequalities (LMIs) in (2.20. ‣ 2.3 Bounded Real Lemma ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence")) hold for $K^{\prime}$. Moreover, it is straightforward to see that such a $P > 0$, if exists, satisfies ${{{({A - {BK^{\prime}}})}^{\top}P{({A - {BK^{\prime}}})}} - P} < 0$, which can be used to show that $K^{\prime}$ is stabilizing. Thus, it now suffices to find such a $P$.

To show this, we first study the case with stepsizes being the upper bound in the theorem, i.e., $\eta = {1/2}$ for Gauss-Newton and $\eta = {1/{({2{\|{R + {B^{\top}{\overset{\sim}{P}}_{K}B}}\|}})}}$ for natural PG. As the solution to the Riccati equation (2.17) under $K$, $P_{K} \geq 0$ satisfies ${I - {\gamma^{- 2}D^{\top}P_{K}D}} > 0$, the first LMI in (2.20. ‣ 2.3 Bounded Real Lemma ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence")). Hence, it may be possible to perturb $P_{K}$ to obtain a $P > 0$, such that the equality in (2.17) becomes a strict inequality of the second LMI in (2.20. ‣ 2.3 Bounded Real Lemma ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence")), while preserving the first LMI. Moreover, if $K^{\prime}$ is not too far away from $K$, such a perturbed $P_{K}$ should also work for $K^{\prime}$. Such an observation motivates the use of $P_{K}$ as the candidate of $P$ for the LMIs in (2.20. ‣ 2.3 Bounded Real Lemma ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence")) under $K^{\prime}$.

Indeed, it can be shown that substituting $P = P_{K}$ makes the second LMI in (2.20. ‣ 2.3 Bounded Real Lemma ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence")) under $K^{\prime}$ *non-strict*, namely, the left-hand side (LHS) $\leq 0$; see (5.1) in the detailed proof. To make it strict, consider the perturbed $P = {P_{K} + {\alpha\overline{P}}}$ for some $\alpha > 0$, where $\overline{P} > 0$ is the solution to some Lyapunov equation

Such a Lyapunov equation (4.1) always admits a solution $\overline{P} > 0$, since $K \in \mathcal{K}$ implies that ${({I - {\gamma^{- 2}DD^{\top}P_{K}}})}^{- 1}{({A - {BK}})}$ is stable. The intuition of choosing (4.1) is as follows. First, the LHS of the second LMI in (2.20. ‣ 2.3 Bounded Real Lemma ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence")) under $K^{\prime}$ can be separated as

By some algebra, the first term is of order $o{(\alpha)}$. Since for small $\alpha$,

this, combined with the Riccati equation (2.17) and (4.1), makes the second term $= {{- {\alphaI}} + {o{(\alpha)}}}$. Hence, there exists small enough $\alpha > 0$ such that ${+} < 0$, ensuring that the updated $K^{\prime}$ is feasible. Lastly, by the linearity of LMIs, any interpolation of $K^{\prime}$ with a smaller stepsize is also feasible/robustly stable, thus completing the proof.

Note that theoretically, it is not clear yet if vanilla PG enjoys implicit regularization. In the worst-case, as discussed right after Remark 4.2, vanilla PG may take infinitely many iterations to converge. Hence, hereafter, we only focus on the global convergence of natural PG method (3.4) and Gauss-Newton method (3.5), with constant stepsizes.

### Global Convergence

The term *global convergence* here refers to two notions: i) the convergence performance of the algorithms starting from *any feasible initialization* point $K_{0} \in \mathcal{K}$; ii) convergence to the *global optimal* policy under certain conditions. We formally establish the results for the natural PG (3.4) and Gauss-Newton (3.5) updates in the following theorem.

### Theorem 4.4 (Global Convergence for Discrete-Time Mixed Design)

Suppose that $K_{0} \in \mathcal{K}$ and ${\| K_{0}\|} < \infty$. Then, under the stepsize choices^66^6In fact, for natural PG (3.4), it suffices to require the stepsize $\eta \leq {1/{({2{\|{R + {B^{\top}{\overset{\sim}{P}}_{K_{0}}B}}\|}})}}$ for the initial $K_{0}$. as in Theorem 4.3. ‣ 4.1 Implicit Regularization ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"), both updates (3.4) and (3.5) converge to the global optimum $K^{\ast} = {{({R + {B^{\top}{\overset{\sim}{P}}_{K^{\ast}}B}})}^{- 1}B^{\top}{\overset{\sim}{P}}_{K^{\ast}}A}$, in the sense that the average of $\{{\| E_{K_{n}}\|}_{F}^{2}\}$ over iterations converges to zero with $O{({1/N})}$ rate.

The proof of Theorem 4.4. ‣ 4.2 Global Convergence ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") is detailed in §5.2. We remark that, the controllability assumption made in Proposition 3.4 is not required for the global convergence here. Remarkably, there might be multiple stationary points such that ${{\nabla\mathcal{J}}{(K)}} = 0$, while the two specific policy search directions (3.4) and (3.5) provably avoid the suboptimal local minima, and always converge to the global optimum $K^{\ast}$. This can be viewed as another implication of *implicit regularization*, in that (3.4) and (3.5) always bias the iterates towards a certain global optimal solution, without getting stuck at spurious local minima. The key reason is that, without using the curvature information in ~K~, these two PO methods can converge to the specific and optimal stationary point such that $E_{K} = 0$, instead of any arbitrary stationary point.

Moreover, in contrast to the results for LQR, only globally *sublinear* $O{({1/N})}$, instead of *linear*, convergence rate can be obtained so far. This $O{({1/N})}$ rate of the (iteration average) gradient norm square matches the *global* convergence rate of gradient descent and second order algorithms to stationary points for general nonconvex optimization, either under the smoothness assumption of the objective, or for a class of non-smooth objectives.

### Remark 4.5 (Robust Initial Controller)

Our global convergence requires the initial controller to satisfy the $\mathcal{H}_{\infty}$-norm robustness constraint, which, as the assumption on the initial controller being stabilizing for LQR, is inherent to PO methods with iterative local search. Complementary to Fazel et al.; Bu et al., our iterates not only improve the performance criterion, but also preserve the robustness.

Though sublinear globally, much faster rates, i.e., (super-)linear rates, can be shown locally around the optimum as below. Proof of the following theorem is deferred to §5.3.

### Theorem 4.6 (Local (Super-)Linear Convergence for Discrete-Time Mixed Design)

Suppose that the conditions in Theorem 4.4. ‣ 4.2 Global Convergence ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") hold, and additionally ${DD^{\top}} > 0$ holds. Then, under the stepsize choices as in Theorem 4.4. ‣ 4.2 Global Convergence ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"), both updates (3.4) and (3.5) converge to the optimal control gain $K^{\ast}$ with *locally linear* rate, in the sense that the objective $\{{\mathcal{J}{(K_{n})}}\}$ defined in (2.15) converges to $\mathcal{J}{(K^{\ast})}$ with a linear rate. In addition, if $\eta = {1/2}$, the Gauss-Newton update (3.5) converges to $K^{\ast}$ with a locally *Q-quadratic* rate.

Key to the locally linear rates is that the property of *gradient dominance* holds locally around the optimum for mixed design problems. Such a property has been shown to hold globally for LQR problems, and also hold locally for zero-sum LQ games. The Q-quadratic rate echoes back the rate of Gauss-Newton with $\eta = {1/2}$ for LQR problems. This globally sublinear and locally (super-)linear convergence resembles the behavior of (Quasi)-Newton methods for nonconvex optimization, and policy gradient methods for zero-sum LQ games.

### Remark 4.7 (Comparison to Zhang et al. (2019b))

Due to the close relationship between mixed design and zero-sum LQ games, see §6, one may compare the convergence results and find the rates here (*globally sublinear and locally linear*) not improved over Zhang et al.. However, one key difference is that an extra *projection* step is required to guarantee the *stability* of the system in Zhang et al., which is essentially to *regularize* the iterates *explicitly*. More importantly, such a projection can only be calculated under more restrictive assumptions (see Assumption 2.1 therein), which, though cover a class of LQ games, are not standard in robust control. Here, similar convergence results are established, without projections or non-standard assumptions in robust control, thanks to *implicit regularization*. Moreover, we have established the local "superlinear" rate for the Gauss-Newton update, and whole new set of results for the "continuous-time" setup, which were not studied in Zhang et al..

## Proofs of Main Results

In this section, we provide detailed proofs for the main results of the paper.

### Proof of Theorem 4.3. ‣ 4.1 Implicit Regularization ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence")

To show that $K^{\prime}$ lies in $\mathcal{K}$, we first argue that it suffices to find some $P > 0$ such that

where $\overset{\sim}{P}:={P + {PD{({{\gamma^{2}I} - {D^{\top}PD}})}^{- 1}D^{\top}P}}$. By Schur complement, showing (5.1)-(5.2) is also equivalent to showing

Obviously, if such a $P$ exists, we denote the LHS of (5.2) by ${- M} < 0$. Thus, (5.1) and (5.2) imply

which shows that $K^{\prime}$ is stabilizing, i.e., ${\rho{({A - {BK^{\prime}}})}} < 1$. Thus, Lemma 2.7. ‣ 2.3 Bounded Real Lemma ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") can be applied to $K^{\prime}$. Then, (5.1) and (5.2) are identical to (2.20. ‣ 2.3 Bounded Real Lemma ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence")), which further shows that ${\|{\mathcal{T}{(K^{\prime})}}\|}_{\infty} < \gamma$ and thus shows $K^{\prime} \in \mathcal{K}$. Hereafter we will focus on finding such a $P > 0$.

We first show that for the Gauss-Newton update (3.5) with stepsize $\eta = {1/2}$, (5.1) and (5.2) hold for some $P > 0$. Specifically, we have

Since $P_{K} \geq 0$ satisfies the conditions i)-iii), and $K$ and $K^{\prime}$ are close to each other, we can choose $P_{K}$ as a candidate of $P$. Hence, by Riccati equation (2.17), the LHS of (5.2) can be written as

where we substitute $K^{\prime}$ from (5.6), and the last equation is due to completion of the squares.

Now we need to perturb $P_{K}$ to obtain a $P$, such that (5.1) holds with a *strict* inequality. To this end, we define $\overline{P} > 0$ as the solution to the Lyapunov equation

and let $P = {P_{K} + {\alpha\overline{P}}} > 0$ for some $\alpha > 0$. By Lemma 2.7. ‣ 2.3 Bounded Real Lemma ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"), ${({I - {\gamma^{- 2}DD^{\top}P_{K}}})}^{- 1}{({A - {BK}})}$ is stable, and thus the solution $\overline{P} > 0$ exists. For (5.1) to hold, we need a small $\alpha > 0$ to satisfy

Moreover, the LHS of (5.2) now can be written as

where we aim to show that there exists some $\alpha > 0$ such that ${+} < 0$. Note that $\overset{\sim}{P}$ can be written as

where the first equation follows from definition, and the second one uses the fact that

for small perturbation $Y$ around the matrix $X$. Thus, can be written as

where the inequality follows by completing squares. By substituting in $K^{\prime}$ from (5.6), we further have

Note that by (5.1), we have

where $O{(\alpha)}$ denotes the quantities that have the order of $\alpha$. By plugging (5.1) into (5.1), we obtain that $= {o{(\alpha)}}$.

Moreover, by (5.1), can be written as

where the first equation uses (5.1), the second one uses the Riccati equation (2.17), and the last one uses (5.8). Therefore, for small enough $\alpha > 0$ such that ${+} < 0$, and also satisfies (5.9), there exists some $P > 0$ such that both (5.1) and (5.2) hold for $K^{\prime}$ obtained with stepsize $\eta = {1/2}$. On the other hand, such a $P$ also makes the LMI (5.5) hold for $K$, i.e.,

as now in (5.1) is null, and the same $\alpha$ above makes $< 0$. For $\eta \in {\lbrack 0,{1/2}\rbrack}$, let $K_{\eta} = {K + {2\eta{({K^{\prime} - K})}}}$ be the interpolation between $K$ and $K^{\prime}$. Combining (5.5) and (5.18) yields

for any $\eta \in {\lbrack 0,{1/2}\rbrack}$. The second inequality in (5.20) uses the convexity of the quadratic form. Hence, (5.20) shows that for any stepsize $\eta \in {\lbrack 0,{1/2}\rbrack}$, $K_{\eta}$ that lies between $K$ and $K^{\prime}$ satisfies the conditions i)-iii) in the theorem.

Now we prove a similar result for the natural PG update (3.4). Recall that

As before, we first choose $P = P_{K}$. Then, the LHS of (5.2) under $K^{\prime}$ can be written as:

where the equation holds by adding and subtracting ${\lbrack{K - {{({R + {B^{\top}{\overset{\sim}{P}}_{K}B}})}^{- 1}B^{\top}{\overset{\sim}{P}}_{K}A}}\rbrack}^{\top}{({R + {B^{\top}{\overset{\sim}{P}}_{K}B}})}{\lbrack{K^{\prime} - {{({R + {B^{\top}{\overset{\sim}{P}}_{K}B}})}^{- 1}B^{\top}{\overset{\sim}{P}}_{K}A}}\rbrack}$. Substituting (5.26) into (5.1) yields

By requiring the stepsize $\eta$ to satisfy

namely, letting $P = P_{K}$ leads to the desired LMI that is not strict.

Now suppose that $P = {P_{K} + {\alpha\overline{P}}}$ for some $\alpha > 0$, where $\overline{P} > 0$ is the solution to (5.8). Note that $\alpha$ first still needs to satisfy (5.9). Also, the LHS of (5.2) can still be separated into and as in (5.1). From the LHS of the inequality in (5.1), we have

where the first equation follows by adding and subtracting ${\lbrack{{{({R + {B^{\top}\overset{\sim}{P}B}})}^{- 1}B^{\top}\overset{\sim}{P}A} - K}\rbrack}^{\top}{({R + {B^{\top}\overset{\sim}{P}B}})}{\lbrack{{{({R + {B^{\top}\overset{\sim}{P}B}})}^{- 1}B^{\top}\overset{\sim}{P}A} - K^{\prime}}\rbrack}$, and the second one follows from the definition of $K^{\prime}$ in (5.26). Suppose that $\eta$ satisfies (5.29), then we have

where the equation follows by separating $\overset{\sim}{P}$ as ${\overset{\sim}{P}}_{K} + {\alpha\overline{P}}$ in (5.1). Notice that the first two terms on the right-hand side (RHS) of (5.32) are identical to the RHS of (5.1). Thus, the inequality (5.33) is due to (5.1). Moreover, notice that

which combined with (5.33) further yields

By assumption ${\| K\|} < \infty$ and $P_{K} \geq 0$ exists, we know that ${\overset{\sim}{P}}_{K}$ is bounded, and so is $K^{\prime}$ obtained from (5.26) using a finite stepsize $\eta$. Also, $\overline{P}$ has bounded norm. Thus, in (5.34) is $o{(\alpha)}$. Thus, there exists small enough $\alpha > 0$ such that ${+} < 0$, since from (5.1), $= {{- {\alphaI}} + {o{(\alpha)}}}$. In words, there exists some $P > 0$ such that (5.5) holds for $K^{\prime}$ obtained from (5.26) with stepsize satisfying (5.29). This completes the proof of the first argument.

Lastly, by Lemma 2.7. ‣ 2.3 Bounded Real Lemma ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"), we equivalently have that the conditions i)-iii) in the theorem hold for $K^{\prime}$, which completes the proof.

### Proof of Theorem 4.4. ‣ 4.2 Global Convergence ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence")

We first introduce the following lemma that can be viewed as the counterpart of the *Cost Difference Lemma* in Fazel et al.. Unlike the equality relation given in the lemma in Fazel et al., we establish both lower and upper bounds for the difference of two matrices $P_{K^{\prime}}$ and $P_{K}$. The proof of the lemma is provided in §B.7.

### Lemma 5.1 (Discrete-Time Cost Difference Lemma)

Suppose that both ${K,K^{\prime}} \in \mathcal{K}$. Then, we have the following upper bound:

where $E_{K}$ is defined in (3.2). If additionally ${\rho\left( {{({A - {BK^{\prime}}})}^{\top}{({I - {\gamma^{- 2}P_{K}DD^{\top}}})}^{- 1}} \right)} < 1$, then we also have the lower bound:

Notice that Lemma 5.1. ‣ 5.2 Proof of Theorem 4.4 ‣ 5 Proofs of Main Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") also resembles the "Almost Smoothness Condition" (Lemma $9$) in Fazel et al., which characterizes how the difference between $P_{K}$ and $P_{K^{\prime}}$ relies on the difference between $K$ and $K^{\prime}$. Due to the difference between ${\overset{\sim}{P}}_{K}$ and $P_{K}$, we have to establish lower and upper bounds of $P_{K^{\prime}} - P_{K}$ separately. One can still identify that the leading terms in both bounds depend on $\|{K^{\prime} - K}\|$, with the remaining terms being in the order of $o{({\|{K^{\prime} - K}\|})}$ if $K^{\prime}$ is close to $K$.

Recall that for the Gauss-Newton update, $K^{\prime} = {K - {2\eta{({R + {B^{\top}{\overset{\sim}{P}}_{K}B}})}^{- 1}E_{K}}}$. By Theorem 4.3. ‣ 4.1 Implicit Regularization ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"), $K^{\prime}$ also lies in $\mathcal{K}$ if $\eta \leq {1/2}$. Then, by the upper bound in (5.35. ‣ 5.2 Proof of Theorem 4.4 ‣ 5 Proofs of Main Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence")), we know that if $\eta \in {\lbrack 0,{1/2}\rbrack}$,

which implies the monotonic decrease of $P_{K}$ (matrix-wise) along the update. Since $P_{K}$ is lower-bounded, such a monotonic sequence of $\{ P_{K_{n}}\}$ along the iterations must converges to some $P_{K_{\infty}} \in \mathcal{K}$. Now we show that this $P_{K_{\infty}}$ is indeed $P_{K^{\ast}}$. By multiplying both sides of (5.2) with any matrix $M > 0$, and then taking the trace, we have that if $\eta \in {\lbrack 0,{1/2}\rbrack}$

where the second inequality follows by keeping only the first term in the infinite summation of positive definite matrices, the third one uses that ${\operatorname{Tr}{({PA})}} \geq {\sigma_{\min}{(A)}{\operatorname{Tr}{(P)}}}$, and the last one is due to the monotonic decrease of $P_{K}$, and the monotonicity of ${\overset{\sim}{P}}_{K}$ with respect to $P_{K}$, with $K_{0} \in \mathcal{K}$ being the initialization of $K$ at iteration $0$. From iterations $n = 0$ to $N - 1$, replacing $M$ by $I$, summing over both sides of (5.2), and dividing by $N$, we further have

namely, the sequence $\{ K_{n}\}$ converges to the stationary point $K$ such that $E_{K} = 0$ with $O{({1/N})}$ rate. By Proposition 3.4, this is towards the global optimal control gain $K^{\ast}$.

Natural Policy Gradient:

Recall that the natural PG update follows $K^{\prime} = {K - {2\etaE_{K}}}$. By Theorem 4.3. ‣ 4.1 Implicit Regularization ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"), $K^{\prime}$ also lies in $\mathcal{K}$ if $\eta \leq {1/{({2{\|{R + {B^{\top}{\overset{\sim}{P}}_{K}B}}\|}})}}$. By the upper bound (5.35. ‣ 5.2 Proof of Theorem 4.4 ‣ 5 Proofs of Main Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence")), this stepsize yields that

which also implies the matrix-wise monotonic decrease of $P_{K}$ along the update. Suppose the convergent matrix is $P_{K_{\infty}}$. As before, multiplying both sides of (5.2) by $M > 0$, and taking the trace, yields

for any $M > 0$, where the inequality follows by only keeping the first term in the infinite summation. Letting $M = I$, summing up (5.40) from $n = 0$ to $n = {N - 1}$, and dividing by $N$, we conclude that

namely, $\{ K_{n}\}$ converges to the stationary point $K$ such that $E_{K} =$ with $O{({1/N})}$ rate, which is also the global optimum. In addition, since $\{ P_{K_{n}}\}$ is monotonically decreasing, it suffices to require the stepsize

which completes the proof.

### Proof of Theorem 4.6Linear Convergence for Discrete-Time Mixed Design). ‣ 4.2 Global Convergence ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence")

To ease the analysis, we show the convergence rate of a surrogate value $\operatorname{Tr}{({P_{K}DD^{\top}})}$. This is built upon the following relationship between the objective value $\mathcal{J}{(K)}$ and $\operatorname{Tr}{({P_{K}DD^{\top}})}$.

### Lemma 5.2

Suppose that both ${K,K^{\prime}} \in \mathcal{K}$ and $P_{K} \geq P_{K^{\prime}}$. Then, it follows that

### Proof

First, by Sylvester's determinant theorem, $\mathcal{J}{(K)}$ can be re-written as

By the mean value theorem, for any matrices $A$ and $B$ with ${{\det{(A)}},{\det{(B)}}} > 0$, we have

for some $0 \leq \tau \leq 1$. This leads to

where $X = {({I - {\gamma^{- 2}\tauD^{\top}P_{K^{\prime}}D} - {\gamma^{- 2}{({1 - \tau})}D^{\top}P_{K}D}})}^{- 1}$, and the inequality uses the facts $P_{K} \geq P_{K^{\prime}}$ and ${\operatorname{Tr}{({PA})}} \leq {{\| A\|} \cdot {\operatorname{Tr}{(P)}}}$ for any real symmetric $P \geq 0$. Note that by $P_{K} \geq P_{K^{\prime}}$,

This completes the proof. ∎

Lemma 5.2 implies that in order to show the convergence of $\mathcal{J}{(K)}$, it suffices to study the convergence of $\operatorname{Tr}{({P_{K}DD^{\top}})}$, as long as $\|{({I - {\gamma^{- 2}D^{\top}P_{K}D}})}^{- 1}\|$ is bounded along the iterations. This is indeed the case since by (5.2) and (5.2), $P_{K}$ is monotone along both updates (3.4) and (3.5). By induction, if $K_{0} \in \mathcal{K}$, i.e., ${I - {\gamma^{- 2}D^{\top}P_{K_{0}}D}} > 0$, then ${I - {\gamma^{- 2}D^{\top}P_{K_{n}}D}} \geq {I - {\gamma^{- 2}D^{\top}P_{K_{0}}D}} > 0$ holds for all iterations $n \geq 1$. This further yields that for all $n \geq 1$, ${\|{({I - {\gamma^{- 2}D^{\top}P_{K_{n}}D}})}^{- 1}\|} \leq {\|{({I - {\gamma^{- 2}D^{\top}P_{K_{0}}D}})}^{- 1}\|}$, namely, $\|{({I - {\gamma^{- 2}D^{\top}P_{K}D}})}^{- 1}\|$ is uniformly bounded.

Now we show the local linear convergence rate of $\operatorname{Tr}{({P_{K}DD^{\top}})}$. By (5.36. ‣ 5.2 Proof of Theorem 4.4 ‣ 5 Proofs of Main Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence")), for any $K^{\prime}$ such that ${({I - {\gamma^{- 2}P_{K}DD^{\top}}})}^{- \top}{({A - {BK^{\prime}}})}$ is stabilizing, we have

where the second inequality follows from completion of squares. By taking traces on both sides of (5.3), and letting $K^{\prime} = K^{\ast}$, we have

where $\mathcal{W}_{K,K^{\ast}}$ is defined as

Note that $K^{\ast} \in \mathcal{K}$ and thus ${({I - {\gamma^{- 2}P_{K^{\ast}}DD^{\top}}})}^{- \top}{({A - {BK^{\ast}}})}$ is stabilizing. Let $\epsilon:={1 - {\rho\left( {{({I - {\gamma^{- 2}P_{K^{\ast}}DD^{\top}}})}^{- \top}{({A - {BK^{\ast}}})}} \right)}}$, and note that $\epsilon > 0$. By the continuity of $P_{K}$, and that of $\rho{( \cdot )}$, there exists a ball ${\mathcal{B}{(K^{\ast},r)}} \subseteq \mathcal{K}$, centered at $K^{\ast}$ with radius $r > 0$, such that for any $K \in {\mathcal{B}{(K^{\ast},r)}}$,

By Theorem 4.4. ‣ 4.2 Global Convergence ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"), $\{ K_{n}\}$ approaches $K^{\ast}$. Thus, there exists some $K_{n} \in {\mathcal{B}{(K^{\ast},r)}}$. Let $K = K_{n}$ and thus $K^{\prime} = K_{n + 1}$. Replacing $M$ in (5.2) by ${DD^{\top}} > 0$ and combining (5.42), we have

which further implies that

(5.44) shows that the sequence $\{{\operatorname{Tr}{({P_{K_{n + p}}DD^{\top}})}}\}$ decreases to $\operatorname{Tr}{({P_{K^{\ast}}DD^{\top}})}$ starting from some $K_{n} \in {\mathcal{B}{(K^{\ast},r)}}$. By continuity, there must exists a close enough $K_{n + p}$, such that the lower-level set $\left. \{ K \middle| {{\operatorname{Tr}{({P_{K}DD^{\top}})}} \leq {\operatorname{Tr}{({K_{n + p}DD^{\top}})}}}\} \right. \subseteq {\mathcal{B}{(K^{\ast},r)}}$. Hence, starting from $K_{n + p}$, the iterates will never leave $\mathcal{B}{(K^{\ast},r)}$. By (5.43), $\mathcal{W}_{K,K^{\ast}}$, as the unique solution to the Lyapunov equation

must have its norm bounded by some constant ${\overline{\mathcal{W}}}_{r} > {\|{DD^{\top}}\|}$ for all $K \in {\mathcal{B}{(K^{\ast},r)}}$. Replacing the term $\|\mathcal{W}_{K,K^{\ast}}\|$ in (5.44) by ${\overline{\mathcal{W}}}_{r}$ gives the uniform local linear contraction of $\{{\operatorname{Tr}{({P_{K_{n}}DD^{\top}})}}\}$, which further leads to the local linear rate of $\{{\mathcal{J}{(K_{n})}}\}$ by Lemma 5.2.

In addition, by the upper bound (5.35. ‣ 5.2 Proof of Theorem 4.4 ‣ 5 Proofs of Main Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence")) and $E_{K^{\ast}} = 0$, we have

For $\eta = {1/2}$, suppose that some $K = K_{n} \in {\mathcal{B}{(K^{\ast},r)}}$. Then, $K^{\prime} = K_{n + 1} = {{({R + {B^{\top}{\overset{\sim}{P}}_{K}B}})}^{- 1}B^{\top}{\overset{\sim}{P}}_{K}A}$ yields that

Moreover, notice that

which, combined with (5.46), gives

for some constant $c > 0$. Combining (5.3) and (5.48) yields

for some constant $c^{\prime}$. Note that from some $p \geq 0$ such that $K_{n + p}$ onwards never leaves $\mathcal{B}{(K^{\ast},r)}$, the constant $c^{\prime}$ is uniformly bounded, which proves the Q-quadratic convergence rate of $\{{\operatorname{Tr}{({P_{K_{n}}DD^{\top}})}}\}$, and thus the rate of $\{{\mathcal{J}{(K_{n})}}\}$, around $K^{\ast}$.

Natural Policy Gradient:

Replacing $M$ in (5.40) by ${DD^{\top}} > 0$ and combining (5.40) and (5.42) yield

Using similar argument as above, one can establish the local linear rate of $\{{\mathcal{J}{(K_{n})}}\}$ with a different contracting factor. This concludes the proof.

## Discussions

We now provide additional discussions on the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control design problem.

### Connection to Zero-Sum LQ Games

It is well known that minimizing the risk-sensitive cost as (2.1), which is the logarithm of the expected values of exponential functions with quadratic forms, can be equivalent to solving a zero-sum dynamic game, for both general settings, and in particular for LQ settings. Due to the connection between LEQG and mixed design, as discussed in §2.2, the latter can be related to a zero-sum LQ game as well.

Specifically, consider the system that follows linear dynamics^77^7The notation in this section might be slightly abused, considering the notations used in the main text, but shall be self-evident by the context.

with the system state being $x_{t} \in R^{d}$, the control inputs of players $1$ and $2$ being $u_{t} \in R^{m_{1}}$ and $v_{t} \in R^{m_{2}}$, respectively. The matrices $A,B$, and $D$ all have proper dimensions. The objective of player $1$ (player $2$) is to minimize (maximize) the infinite-horizon value function,

where the initial state $x_{0} \sim \mathcal{D}$ for some distribution $\mathcal{D}$, the matrices $Q \in R^{d \times d}$, $R^{u} \in R^{m_{1} \times m_{1}}$, and $R^{v} \in R^{m_{2} \times m_{2}}$ are all positive definite. *Value* of the game, i.e., the value of (6.1) when the $\inf$ and $\sup$ can interchange, is characterized by $E_{x_{0} \sim \mathcal{D}}{({x_{0}^{\top}P^{\ast}x_{0}})}$, where $P^{\ast}$ is the solution to the generalized algebraic Riccati equation (GARE)

Moreover, under the standard assumption that ${R^{v} - {D^{\top}P^{\ast}D}} > 0$, the solution policies, i.e., the *Nash equilibrium* (NE) policies that are stabilizing, of the two players have forms of LTI state-feedback, namely, $u_{t}^{\ast} = {- {K^{\ast}x_{t}}}$ and $v_{t}^{\ast} = {- {L^{\ast}x_{t}}}$ for some matrices $K^{\ast} \in R^{m_{1} \times d}$ and $L^{\ast} \in R^{m_{2} \times d}$. The corresponding values of $(K^{\ast},L^{\ast})$ are given by

As a consequence, it suffices to search over all stabilizing control gain pairs $(K,L)$ that solves

In fact, for any stabilizing $(K,L)$ that makes ${\rho{({A - {BK} - {DL}})}} < 1$, $\mathcal{C}{(K,L)} = \operatorname{Tr}{(P_{K,L}{}_{}^{}}$, where ${}_{}^{}E_{x_{0} \sim \mathcal{D}}{(x_{0}^{\top}x_{0})}$, and $P_{K,L}$ is the unique solution to the Lyapunov equation

Given $K$ that makes^88^8This condition on $K$ is necessary for finding the equilibrium policy since otherwise, the maximizer can drive the cost to infinity by choosing $L$. See Chapter $3$ of Başar and Bernhard for more discussions. ${R^{v} - {D^{\top}P_{K,L}D}} > 0$, maximizing over $L$ on the RHS of (6.5) yields

where $P_{K}^{\ast} = P_{K,{L{(K)}}}$ with $L{(K)}$ being the maximizer that satisfies

Notice that (6.6) is in fact a Riccati equation identical to (2.17), with $R^{v}$ replaced by $\gamma^{2}I$, $R^{u}$ replaced by $R$, and $Q$ replaced by $C^{\top}C$. Hence, the problem (6.4) is equivalent to minimizing $\mathcal{C}{(K,L{(K)})} = \operatorname{Tr}{(P_{K}^{\ast}{}_{}^{}}$, subject to (6.6), which coincides with the mixed design problem (2.19), where $\mathcal{J}{(K)}$ takes the form of (2.14) with $DD^{\top}$ replaced by ~0~. Furthermore, the minimizer of the RHS on (6.6) is

which equals the global optimum for the mixed design problems.

### Model-Free Algorithms

The connection above provides one angle to develop *model-free* RL algorithms for solving mixed design problems. Indeed, the natural PG in (3.4) cannot be sampled using trajectory data, due to the form of the matrix ~K~ in (3.1). Fortunately, solution of the game (6.4) can be obtained by model-free PG-based methods, see Zhang et al., and the more recent work Bu et al., which, by (6.8) and Proposition 3.4, is equivalent to the global optimum of mixed design problems. Hence, model-free algorithms that solve the LQ game (6.4) can also be used to solve the mixed design problem (2.19).

Specifically, by Lemma 3.3 of Zhang et al., under certain conditions, the stationary point $(K,L)$ where ${{\nabla_{K}\mathcal{C}}{(K,L)}} = 0$ and ${{\nabla_{L}\mathcal{C}}{(K,L)}} = 0$ coincides with the NE. Therefore, it is straightforward to develop PG-based updates to find the minimizer $L{(K)}$ for some $K$, and then perform PG-based algorithms to update $K$, which can both be implemented in a model-free fashion, using zeroth-order methods. Note that the PO methods in Zhang et al. are essentially also based on this idea, but with the order of $\max$ and $\min$ interchanged, and require a projection step for updating $L$. More recently, Bu et al. has developed double-loop PO methods that remove this projection. Two examples of PG-based methods can be written as

where ${\alpha,\eta} > 0$ are stepsizes, ${}_{K,L}^{}E_{x_{0} \sim \mathcal{D}}\sum_{t = 0}^{\infty}x_{t}x_{t}^{\top}$ with $u_{t} = {- {Kx_{t}}}$ and $v_{t} = {- {Lx_{t}}}$ is the correlation matrix under control pair $(K,L)$, $\hat{L{(K)}}$ is the estimate of $L{(K)}$ obtained by iterating either (6.9) or (6.11), ${\hat{\nabla}}_{L}\mathcal{C}{(K,L)}$, ${\hat{\nabla}}_{K}\mathcal{C}{(K,L)}$, and ${\hat{}}_{K,L}$ are the estimates of ${\nabla_{L}\mathcal{C}}{(K,L)}$, ${\nabla_{K}\mathcal{C}}{(K,L)}$, and ~K,L~ using sampled data, respectively.

Note that the simulator for the game (6.4) that generates the data samples can be obtained by the simulator for the mixed design problem (2.19), with the disturbance $w_{t}$ modeled as $w_{t} = {- {Lx_{t}}}$. This way, the updates of $L$ in (6.9) and (6.11) can be understood as improving the disturbance to find the *worst-case* one, which manifests the idea of $\mathcal{H}_{\infty}$ norm. Also, Bu et al. has verified that in zero-sum LQ games, given a fixed $K$, such an update of $L$ converges to the best-response disturbance $L{(K)}$ given in (6.7). This justifies the feasibility of our algorithms (6.9)-(6.12).

In addition, by the form of the policy gradients for the game, see Lemma 3.2 in Zhang et al., the exact natural PG update on the LHS of (6.12) is identical to that for mixed design problems in (3.4). In other words, the natural PG update (3.4) can be implemented in a model-free way by virtue of that outer-loop update of $K$ in a zero-sum LQ game. As shown in Bu et al., such an outer-loop update over $K$ converges to the NE of the game. Details of the model-free algorithms are deferred to Algorithms 1, 2, and 3 in §D.

## Simulations

In this section, we present some simulation results to corroborate our theory. We mainly focus on the convergence properties for the discrete-time settings. We have also included extensive numerical comparisons with existing packages for solving $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ mixed design, which can only handle the continuous-time settings. The problem setup, PO algorithms, and their analyses, for the continuous-time settings can be found in §A. We show that our PO methods outperform these existing packages in many aspects, though the latter ones can handle more general setups.

### Implicit Regularization & Global/Local Convergence

Figure 2: Convergence of the gradient norm square ∥EK∥F2 and the objective {𝒥 (K)}, behaviors of the ℋ∞-norm ∥𝒯 (K)∥∞, and the smallest eigenvalue of γ2 I − D⊤ PK D, for PG, NPG, and Gauss-Newtons with stepsizes 1 × 10−7, 1 × 10−4, 0.01, and 0.5, respectively.

Figure 3: Linear, linear and super-linear convergence rates for the NPG update with η = 10−4, the GN update with η = 10−2, and the GN update with η = 0.5, respectively.

We first consider the following example, denoted by Case 1, whose parameters are:

and ${DD^{\top}} = I$. Note that all matrices $C^{\top}C$, $E^{\top}E$, and $DD^{\top}$ are positive definite. This $DD^{\top}$ satisfies both the controllability assumption in Proposition 3.4, and the assumption ${DD^{\top}} > 0$ in Theorem 4.6Linear Convergence for Discrete-Time Mixed Design). ‣ 4.2 Global Convergence ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"). We first randomly generate $K_{0}$ with each element uniformly generated from $\lbrack{- 0.25},0.25\rbrack$, such that $K_{0}$ is stabilizing (i.e., ${\rho{({A - {BK_{0}}})}} < 1$). Then, the $\mathcal{H}_{\infty}$-norm ${\|{\mathcal{T}{(K_{0})}}\|}_{\infty}$ under $K_{0}$ is calculated. The value of $\gamma$ is then chosen as $1.00001 \cdot {\|{\mathcal{T}{(K_{0})}}\|}_{\infty}$, making sure that $K_{0} \in \mathcal{K}$. We then perform all three algorithms (3.3)-(3.5) in §3.2 on the above problem setting, and illustrate the convergence of both the gradient norm square ${\| E_{K}\|}_{F}^{2}$, and the objective difference $\{{{\mathcal{J}{(K_{n})}} - {\mathcal{J}{(K^{\ast})}}}\}$. The stepsizes $\eta$ for the PG, NPG, and Gauss-Newton updates are $1 \times 10^{- 7}$, $1 \times 10^{- 4}$, and $0.01$, respectively. We have also used $\eta = {1/2}$ for the Gauss-Newton update.

As shown in Figure 2, for both performance criteria, all four update rules converge successfully. At the beginning of the iterations, NPG and Gauss-Newton with $\eta = 10^{- 2}$ indeed yield sublinear convergence of the gradient norm square; as the iterations proceed, linear convergence rate appears. Moreover, for Gauss-Newton with $\eta = {1/2}$, super-linear convergence rate has also been observed. These observations corroborate our theory in both Theorems 4.4. ‣ 4.2 Global Convergence ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") and 4.6Linear Convergence for Discrete-Time Mixed Design). ‣ 4.2 Global Convergence ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence").

Moreover, we have also illustrated the behaviors of the $\mathcal{H}_{\infty}$-norm ${\|{\mathcal{T}{(K)}}\|}_{\infty}$ and the smallest eigenvalue of ${\gamma^{2}I} - {D^{\top}P_{K}D}$, denoted by $\lambda_{\min}{({{\gamma^{2}I} - {D^{\top}P_{K}D}})}$, in Figure 2. It is seen that along the iterations, with the stepsizes that guarantee convergence, the $\mathcal{H}_{\infty}$-norm is below the bound $\gamma = 15.45$ for all four update rules, which validates the implicit regularization result we have in Theorem 4.3. ‣ 4.1 Implicit Regularization ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"). As another evidence for implicit regularization in accordance to Lemma 2.7. ‣ 2.3 Bounded Real Lemma ‣ 2 Preliminaries ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"), it is shown that the matrix ${{\gamma^{2}I} - {D^{\top}P_{K}D}} > 0$ along iterations.

Notice that the initialization $K_{0}$ is very close to the boundary, as $\gamma = {1.00001 \cdot {\|{\mathcal{T}{(K_{0})}}\|}_{\infty}}$. It is shown that the vanilla PG update, even though with infinitesimal stepsize ($10^{- 7}$), still violates the $\mathcal{H}_{\infty}$-norm constraint and fails to converge. We do observe, however, in several other numerical examples, that vanilla PG update converges successfully. It is thus not clear whether there exists a *constant* stepsize choice for the *global convergence* and *robustness perservation* of the vanilla PG iterates, which is left for future investigation.

To further verify our local convergence rates, we have also initialized our algorithms by randomly searching over $R^{3 \times 3}$ to find a $K_{0} \in \mathcal{K}$ such that ${\|{K_{0} - K^{\ast}}\|}_{F} \leq 0.3$. The convergence patterns are presented in Figure 3, which clearly demonstrates the faster local rates.

### Escaping Suboptimal Stationary Points

Figure 4: Convergence of the NPG and GN updates to K*, when there exists an infinite number of stationary points (i.e. K s.t. ∇𝒥 (K) = 0). The stepsizes for the PG, NPG, and GN updates are 10−3, 10−2, and 0.5, respectively.

We also investigate the setting where the controllability assumption in Proposition 3.4, and the assumption ${DD^{\top}} > 0$ in Theorem 4.6Linear Convergence for Discrete-Time Mixed Design). ‣ 4.2 Global Convergence ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") do not hold. In this case, there might exist multiple stationary points, many of which are suboptimal.

Specifically, consider the following problem parameter, which is denoted by Case 2:

Note that the system is open-loop unstable, as ${\rho{(A)}} > 1$. We choose $\gamma = 10$. Then, one can verify that the above mixed design problem admits an optimum $K^{\ast} = {{({R + {B^{\top}{\overset{\sim}{P}}_{K^{\ast}}B}})}^{- 1}B^{\top}{\overset{\sim}{P}}_{K^{\ast}}A} = \begin{bmatrix}
\end{bmatrix}$. Moreover, there exist an infinite number of stationary points, which share the form of $K = \begin{bmatrix}
\end{bmatrix}$ for any $c \in R$, and make ${{\nabla\mathcal{J}}{(K)}} = 0$. Despite this, following Theorem 4.4. ‣ 4.2 Global Convergence ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence"), the NPG and GN updates provably converge to $K^{\ast}$, which automatically escape other suboptimal stationary points. We numerically evaluate the convergence to $K^{\ast}$ in Figure 4, for both the NPG and GN updates. For each of the 50 trails, we fix a random seed and initialize the algorithm by randomly searching a $K_{0} \in R^{2 \times 2}$ that satisfies $K_{0} \in \mathcal{K}$. It can be observed that two PG methods converge to $K^{\ast}$ in all trails. In start contrast, the vanilla PG update can easily get stuck at these suboptimal stationary points, depending on its initialization.

This can be understood as another meaning of *implicit regularization*: for this specific nonconvex problem, two certain search directions automatically bias the iterates to avoid bad local minima, and always towards the global optimal one.

### Comparison with Existing $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ Control Solvers

To better justify the superiority of our PO methods, we numerically compare their convergence properties with other numerical $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ mixed control design packages, including the HIFOO method and the h2hinfsyn method implemented in Matlab, which is based on linear matrix inequalities. Note that these full-fledged packages can only handle continuous-time settings. To make the comparison fair, we also implement our PO methods for the continuous-time settings as studied in §A.

We mainly compare them in terms of: 1) the $\mathcal{H}_{2}$ and $\mathcal{H}_{\infty}$ norms of the controller that the algorithms converge to; 2) the *computation complexity* (runtime); 3) the *$\mathcal{H}_{\infty}$-norm constraint violation*. We will validate that our PO methods indeed outperform HIFOO in these aspects. The larger-scale the dynamical system is, the more pronounced our advantages are, with provable robustness preserving guarantees.

Simulation Setup. All the experiments are executed on a MacBook Pro 2019 with a 2.8 GHz Quad-Core Intel Core i7 processor with Matlab R2020b. The device also has a 16GB 2133MHz LPDDR3 memory and an Intel Iris Plus 655 Graphics. To make the runtime comparison fair (or even in favor of HIFOO), we set the following parameters of HIFOO (version 3.501 with Hanso version 2.01): options.fast $= 1$ for using a *fast* optimization method; options.prtlevel $= 0$ to suppress unnecessary printing statements. Other parameters of HIFOO are set to be default. For Matlab's h2hinfsyn function, tol has been set to $10^{- 6}$. For our PO methods, we set the stepsizes of the NPG and GN updates to be $1/{({2{\| R\|}})}$ and $1/2$, respectively, and solve the following mixed design problems Cases 3-6 until ${{\mathcal{J}{(K)}} - {\mathcal{J}{(K^{\ast})}}} < 10^{- 6}$.

A Simple Example. We first consider a simple setting, denoted by Case 3. The time-invariant system dynamics are characterized by $\overset{˙}{x} = {{Ax} + {Bu} + {Dw}}$, $z = {{Cx} + {Eu}}$, where

One can verify that ${E^{\top}{\lbrack{CE}\rbrack}} = {\lbrack 0,I\rbrack}$, satisfying our assumption. Then, we solve

The simulations are run over 100 trails with the random seed being fixed at $1,\cdots,100$, respectively. The optimal (minimax) disturbance attenuation level of Case 3 is $\gamma^{\ast} \approx 0.53$, as computed/verified both by Matlab's hinfsyn function and HIFOO's hifoo(P, 'h') function. We summarize the following interesting findings based on the comparisons between HIFOO and our PO methods in Table 1:

(PO methods achieve lower $\mathcal{H}_{2}$ and $\mathcal{H}_{\infty}$ norms, faster). When $\gamma = 5$, both HIFOO and PO methods preserve the ${\|{\mathcal{T}{(K)}}\|}_{\infty} < \gamma$ constraint during the optimization process, and output some convergent gain matrix $K$. However, HIFOO converges to a *local* minimum due to that it is directly optimizing the $\mathcal{H}_{2}$ norm of the closed-loop transfer function, and the landscape for such an optimization problem is unclear. In contrast, our PO methods, by definition, optimize an *upper bound* of the $\mathcal{H}_{2}$-norm, and as proved theoretically, converge to the *global* minimum of the problem. The solution yields lower values for ${\|{\mathcal{T}{(K)}}\|}_{2}$ and ${\|{\mathcal{T}{(K)}}\|}_{\infty}$ compared to those of the HIFOO output. Indeed, this shows that minimizing the $\mathcal{H}_{2}$-norm upper bound as in Bernstein and Haddad; Mustafa and Bernstein and our paper can obtain reasonably good solutions. More importantly, the average runtimes of our PG methods average over 100 trails are around $5.93 \times$ faster than HIFOO.

(PO methods always preserve $\mathcal{H}_{\infty}$-norm constraint). When $\gamma = 3$ (which is still far from $\gamma^{\ast} \approx 0.53$), our methods consistently preserve the ${\|{\mathcal{T}{(K)}}\|}_{\infty} < \gamma$ constraint during the optimization process, validating our theoretical findings. However, the HIFOO iterates have reached ${\|{\mathcal{T}{(K)}}\|}_{\infty} = 3.4353 > 3$ along the way. Further, PO methods also find solutions that have lower ${\|{\mathcal{T}{(K)}}\|}_{2}$ and ${\|{\mathcal{T}{(K)}}\|}_{\infty}$ norms, with a $5.85 \times$ faster runtime.

(Smaller $\gamma$ leads to worse performance for HIFOO). When $\gamma = 1$, our PO methods still preserve the ${\|{\mathcal{T}{(K)}}\|}_{\infty} < \gamma$ constraint during the optimization process. Our PO methods also converge to the optimum point with both small $\mathcal{H}_{2}$ and $\mathcal{H}_{\infty}$ norms, while HIFOO's performance is degraded much more. We remark that in this case, the runtime of our methods is longer than that of HIFOO, however, the time was mostly consumed in finding the initialization that is robustly stable, by randomly generating $K_{0}$ in a certain region. This becomes harder to find for a smaller $\gamma$. Our simple initialization method takes more than 90% of the time, which might be less efficient than the advanced initialization technique used in HIFOO.

Table 1: Comparison average over 100 trails between HIFOO and two proposed PO methods, for solving the mixed design Case 3. All three methods initialize K0 on their own. For two PO methods, a K0 ∈ 𝒦 is found by randomly search over [−1, 1]3 × 3, which takes up &gt; 90% of the total runtime. In contrast, HIFOO uses an in-house method to find initial points. ∥𝒯 (K)∥2 Diff. and ∥𝒯 (K)∥∞ Diff. represent the difference of ℋ2 and ℋ∞ norms achieved by HIFOO and our PO methods (which are identical for NPG and GN, as our methods have guarantees for finding the global optimum of our mixed design problem).

Regarding the comparison with the h2hinfsyn function, we present the results in Table 2. It is shown that in this simple $3 \times 3$ problem, h2hinfsyn and our PG methods converge to nearly the same solution, while our computation time is around $4 \times$ faster. Next, we will show that h2hinfsyn scales poorly with respect to the problem dimensions, while our PO methods converge efficiently in high-dimensional problems.

Table 2: Comparison average over 100 trails between Matlab’s h2hinfsyn and two proposed PO methods, for solving the mixed design Case 3. For the two PO methods, a K0 ∈ 𝒦 is found by randomly search over [−1, 1]3 × 3, and the computation time for finding such an initial point is not taken into account for fair comparison. In contrast, h2hinfsyn implements a LMI-based synthesis procedure.

More Challenging Cases. We test some more challenging cases with higher dimensions to further demonstrate the efficiency of our PO methods. In Cases 4-6, the dimensions of the control gain matrices are ${15 \times 15},{60 \times 60},{90 \times 90}$, respectively, corresponding to the number of decision variables being $225$, $3600$, $8100$, respectively. Problem parameters are too long to enumerate here, and are provided at [here](https://www.dropbox.com/sh/mfrenjttwkidmbv/AACAWnmjL4NWgDa76Atc6DUya?dl=0), together with all the code and data.

The simulations are run over 10 trails with fixed random seeds. Both HIFOO, h2hinfsyn, and our PO methods converge to almost the same control gain matrices in these cases, without constraint violation. This again implies that minimizing the $\mathcal{H}_{2}$-norm upper bound (instead of $\mathcal{H}_{2}$-norm directly) can usually achieve quite competitive solutions. Notably, our PO methods are around $8 \times$, $47 \times$, $295 \times$ faster than HIFOO, respectively, in Cases 4-6, as reported in Table 3. Our PO methods are also much faster than h2hinfsyn, as it can hardly solve Cases 5-6 and fails to return a solution even after very long runtime.. This verifies that our PO algorithms indeed enjoy better scalability, and the higher the dimension is, the more pronounced our advantage is. These observations have justified that our PO methods are not only theoretically sound, but also numerically competitive.

Table 3: Average runtime comparison over 10 trails between HIFOO, Matlab’s h2hinfsyn function, and two proposed PO methods for solving Cases 4-6. The speedup times outside and inside the parenthesis denote the ones of our PO methods compared to HIFOO and Matlab, respectively.

Table 4: Average ∥𝒯 (K)∥2 reached over 10 trails between HIFOO, Matlab’s h2hinfsyn function, and two proposed PO methods for solving Cases 4-6.

Table 5: Average ∥𝒯 (K)∥∞ reached over 10 trails between HIFOO, Matlab’s h2hinfsyn function, and two proposed PO methods for solving Cases 4-6.

## Concluding Remarks

In this paper, we have investigated the convergence theory of policy optimization methods for $\mathcal{H}_{2}$ linear control with $\mathcal{H}_{\infty}$-norm robustness guarantees. Viewed as a constrained nonconvex optimization, this problem was addressed by PO methods with provable convergence to the global optimal policy. More importantly, we showed that the proposed PO methods enjoy the implicit regularization property, despite the lack of coercivity of the cost function. We expect the present work to serve as an initial step toward further understanding of RL algorithms on robust/risk-sensitive control tasks. We conclude this main part of the paper with several ongoing/potential research directions.

### Implicit regularization of other PO methods

It is of particular interests to investigate whether other PO methods enjoy similar implicit regularization properties. One important example that has not been analyzed in this paper is the PG method. Notice that the model-free implementation of the PG method, see update (3.3), does not require the connection between mixed design and zero-sum LQ games, as the gradient can be sampled via zeroth-order methods directly. Among other examples are quasi-Newton methods with pre-conditioning matrices other than that in (3.5), accelerated PG using the idea from Nesterov, and variance reduced PG methods.

### Linear quadratic games

Thanks to the connection discussed in §6.1, our LMI-based techniques for showing implicit regularization in Theorem 4.3. ‣ 4.1 Implicit Regularization ‣ 4 Theoretical Results ‣ Policy Optimization for ℋ₂ Linear Control with ℋ_∞ Robustness Guarantee: Implicit Regularization and Global Convergence") may be of independent interest to improve the convergence of nested policy gradient methods in Zhang et al., and even simultaneously-moving policy-gradient methods, for solving zero-sum LQ games using PO methods. This will place PO methods for multi-agent RL (MARL) under a more solid theoretical footing, as LQ games have served as a significant benchmark for MARL. Rigorous analysis for this setting have been partially addressed in our ongoing work, and in a more recent work Bu et al..

### Model-based v.s. model-free methods for robust control

There is an increasing literature in *model-based* learning-based control with robustness concerns. On the other hand, our work serves as an intermediate step toward establishing the sample complexity of model-free PO methods for this setting. Hence, it is natural and interesting to compare the data efficiency (sample complexity) and computational scalability of the two lines of work. Note that such a comparison has been made in Tu and Recht for LQR problems without addressing the issue of robustness.

### Beyond LTI systems and state-feedback controllers

It is possible to extend our analysis to the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control of other types of dynamical systems such as periodic systems, Markov jump linear systems, and switching systems. These more general system models are widely adopted in control applications, and extensions to these cases will significantly expand the utility of our theory. On the other hand, it is interesting while challenging to study PO for *output-feedback* mixed design, where a dynamic controller parameterized by $(A_{K},B_{K},C_{K},D_{K})$ is synthesized. This way, the PO landscape depends on the order of the parameterization, making the analysis more involved.

### PO landscape and algorithms for $\mathcal{H}_{\infty}$ control synthesis

Our algorithms are based on the condition that an initial policy satisfying the specified $\mathcal{H}_{\infty}$-norm constraint is available. To efficiently find such an initialization, it is natural to study the PO landscape of $\mathcal{H}_{\infty}$ control synthesis, where the goal is to find the controller that not only satisfies certain $\mathcal{H}_{\infty}$-norm bound, but also minimizes it. It seems that the cost function for $\mathcal{H}_{\infty}$ control is still coercive. However, the main challenge of PO for $\mathcal{H}_{\infty}$ control is that the cost function is non-smooth, which necessitates the use of subgradient methods. The LMI arguments developed here may shed new lights on the convergence analysis of these methods.
