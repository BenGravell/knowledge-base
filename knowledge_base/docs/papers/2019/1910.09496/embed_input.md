<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Policy Optimization for H2 Linear Control with H∞ Robustness Guarantee: Implicit Regularization and Global Convergence

Topics include Nonconvex optimization, Policy gradients, Reinforcement learning, Optimal control, Stability analysis, Safety, Robustness, Optimization, Control, Learning, Policy optimization, PO, Linear quadratic regulator.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Policy optimization (PO) is a key ingredient for reinforcement learning (RL). For control design, certain constraints are usually enforced on the policies to optimize, accounting for either the stability, robustness, or safety concerns on the system. Hence, PO is by nature a constrained (nonconvex) optimization in most cases, whose global convergence is challenging to analyze in general. More importantly, some constraints that are safety-critical, e.g., the H_infinity-norm constraint that guarantees the system robustness, are difficult to enforce as the PO methods proceed. Recently, policy gradient methods have been shown to converge to the global optimum of linear quadratic regulator (LQR), a classical optimal control problem, without regularizing/projecting the control iterates onto the stabilizing set, its (implicit) feasible set. This striking result is built upon the coercive property of the cost, ensuring that the iterates remain feasible as the cost decreases. In this paper, we study the convergence theory of PO for H_2 linear control with H_infinity-norm robustness guarantee.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

One significant new feature of this problem is the lack of coercivity, i.e., the cost may have finite value around the feasible set boundary, breaking the existing analysis for LQR. Interestingly, we show that two PO methods enjoy the implicit regularization property, i.e., the iterates preserve the H_infinity robustness constraint as if they are regularized by the algorithms. Furthermore, despite the nonconvexity of the problem, we show that these algorithms converge to the globally optimal policies with globally sublinear rates, avoiding all suboptimal stationary points/local minima, and with locally (super-)linear rates under certain conditions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recent years have witnessed tremendous success of reinforcement learning (RL) in various sequential decision-making applications [silver2016mastering,OpenAI\_dota,alphastarblog] and continuous control tasks [lillicrap2015continuous,schulman2015high,levine2016end,recht2019tour].

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Interestingly, most successes hinge on the algorithmic framework of policy optimization (PO), umbrellaing policy gradient (PG) methods [sutton2000policy,kakade2002natural], actor-critic methods [konda2000actor,bhatnagar2009natural], trust-region [schulman2015trust] and proximal PO [schulman2017proximal] methods, etc. This inspires an increasing interest in studying the convergence theory, especially global convergence to optimal policies, of PO methods; see recent progresses in both classical RL contexts [bhandari2019global,zhang2019global,wang2019neural,agarwal2019optimality,shani2019adaptive], and continuous control benchmarks [fazel2018global,bu2019LQR,malik2019derivative,tu2018gap,zhang2019policy,matni2019self].

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Indeed, PO provides a general framework for control design.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Hereafter, we will mostly adhere to the terminologies and notational convention in the control literature, which are equivalent to, and can be easily translated to those in the RL literature, e.g., cost v.s. reward, control v.s. action, etc.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Consider a general control design problem for the following discrete-time nonlinear dynamical system where $x_k$ is the state, $u_k$ is the control input, and $w_k$ is the process noise. Formally, PO is a constrained optimization problem $\min_{K\in \mathcal{K}} \cJ(K)$, where the decision variable $K$ is determined by the controller parameterization, the cost function $\cJ(K)$ is a pre-specified control performance measure, and the feasible set $\mathcal{K}$ carries the information of the constraints on the controller $K$. These concepts are briefly reviewed as follows.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

- Optimization variable $K$: The control input $u_k$ is typically determined by a feedback law $K$ which is also termed as a controller. In the simplest case where a LTI state-feedback controller is used, $K$ is parameterized as a static matrix and $u_k$ is given as $u_k=-K x_k$. Then this matrix $K$ becomes the decision variable of the PO problem. For the so-called linear output feedback case where the state $x_k$ is not directly measured, the controller can be either a memoryless mapping or an LTI dynamical system. Hence, $K$ can be parameterized by either a static matrix [rautert1997computational] or some state/input/output matrices $(A_K, B_K, C_K, D_K)$ [apkarian2008mixed]. It is also possible to deploy nonlinear controllers and parameterize $K$ as either polynomials, kernels, or deep neural networks [topcu2008local, levine2016end].

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

- Objective function $\cJ(K)$: $\cJ(K)$ is specified to assess the performance of a given controller $K$. The cost function design is more of an art than a science. Popular choices of such cost functions include $\mathcal{H}_2$ or $\mathcal{H}_\infty$-norm (or some related upper bounds) for the resultant feedback systems [zhou1996robust, skogestad2007multivariable, dullerud2013course]. For standard RL models that are based on Markov decision processes (MDPs), the cost $\cJ(K)$ usually has an additive structure over time.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

For instance, in the classical linear quadratic regulator (LQR) or state-feedback LQ Gaussian (LQG) problems, the cost is $\cJ(K):=\sum_{t=0}^{\infty} \EE[x_t^\top Q x_t+u_t^\top R u_t]$, which also has an $\cH_2$-norm interpretation [zhou1996robust]. Nevertheless, $\cJ(K)$ does not necessarily have an additive structure. We will further discuss the specification of $\cJ(K)$ in [sec:formulation]. - Feasible set $\mathcal{K}$: Constraints on the decision variable $K$ are posed to account for either the stability, robustness, or safety concerns on the system. A common, though sometimes implicit, example in continuous control tasks is the stability constraint, i.e. $K$ is required to stabilize the closed-loop dynamics [makila1987computational,bu2019LQR].

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are also other constraints related to robustness or safety concerns in control design [skogestad2007multivariable, dullerud2013course,apkarian2008mixed]. The constraints will naturally confine the policy search to a feasible set $\mathcal{K}$. The cost function $\cJ(K)$ is either $\infty$ or just undefined for $K\notin \mathcal{K}$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

To ensure the feasibility of $K$ on the fly as the PO methods proceed, projection of the iterates onto the set $\cK$ seems to be the first natural approach that comes to mind. However, such a projection may not be computationally efficient or even tractable. For example, projection onto the stability constraint in LQR problems can hardly be computed, as the set $\cK$ therein is well known to be nonconvex [fazel2018global,bu2019topological]. Fortunately, such a projection is not needed to preserve the feasibility of the iterates in PG-based methods, as recently reported by [fazel2018global,bu2019LQR]. In particular, [bu2019LQR] has identified that the cost of LQR has the coercive property, such that it diverges to infinity as the controller $K$ approaches the boundary of the feasible set $\cK$. In other words, the cost of LQR serves as a barrier function on $\cK$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

This way, the level set of the cost becomes compact, and the decrease of the cost ensures the next iterate to stay inside the level set, which further implies the stay inside $\cK$. This desired property is further illustrated in Figure [fig:illust\_hardness](a), where $K$ and $K'$ are two consecutive iterates, and the level set $\{\tilde{K}\given \cJ(\tilde{K})\leq \cJ(K)\}$ is always separated from the set $\cK^c$ by some distance $\delta>0$. Hence, as long as $\norm{K-K'}<\delta$, the next iterate $K'$ still stays in the set $\mathcal{K}$. More importantly, such a separation distance $\delta$ can be re-used for the next iterate, as the next level set is at least $\delta$ away from $\cK^c$. By induction, this allows the existence of a constant stepsize that can guarantee the controllers' stability along the iterations.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is worth emphasizing that such a property is algorithm-agnostic, in the sense that it is dictated by the cost, and independent of the algorithms adopted, as long as they follow any descent directions of the cost.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Besides the stability constraint, another commonly used one in the control literature is the so-called $\cH_\infty$ constraints. This type of constraints plays a fundamental role in robust control [zhou1996robust, skogestad2007multivariable, dullerud2013course,apkarian2008mixed] and risk-sensitive control [whittle1990risk,glover1988state]. Based on the well-known small gain theorem [zames1966input,zhou1996robust], such constraints can be used to guarantee robust stability/performance of the closed-loop systems when model uncertainty is at presence. Compared with LQR under the stability constraint, control synthesis under the $\cH_\infty$ constraint leads to a fundamentally different optimization landscape, over which the behaviors of PO methods have not been fully investigated yet. In this paper, we take an initial step towards understanding the theoretical aspects of policy-based RL methods on robust/risk-sensitive control problems.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

Specifically, we establish a convergence theory for PO methods on $\cH_2$ linear control problems with $\cH_\infty$ constraints, referred to as mixed $\cH_2/\cH_\infty$ state-feedback control design in the robust control literature [glover1988state,khargonekar1991mixed,kaminer1993mixed,mustafa1990minimum,mustafa1991lqg,mustafa1989relations,apkarian2008mixed]. As the name suggests, the goal of mixed design is to find a robust stabilizing controller that minimizes an upper bound for the $\cH_2$-norm, under the restriction that the $\cH_\infty$-norm on a certain input-output channel is less than a pre-specified value. The $\mathcal{H}_\infty$ constraint is explicitly posed here to guarantee the robustness of the closed-loop system to some extent.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

This general framework also includes risk-sensitive linear control, modeled as linear exponential quadratic Gaussian (LEQG) [jacobson1973optimal, whittle1990risk] problems as a special case, when a certain upper bound of $\cH_2$-norm is used. Detailed formulation for such $\cH_2$ linear control with $\cH_\infty$ constraint is provided in [sec:formulation0]. In contrast to LQR, two challenges exist in the analysis of PO methods for mixed design problems. First, by definition of $\mathcal{H}_\infty$-norm [zhou1996robust], the constraint is defined in the frequency domain, and is hard to impose, for instance, by directly projecting the iterates in that domain, especially in the context of RL when the system model is unknown. Note that preserving the constraint bound of $\cH_\infty$-norm as the controller updates is critical in practice, since violation of it can cause catastrophic consequences on the system.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second, more importantly, the coercive property of LQR fails to hold for mixed design problems, as illustrated in Figure [fig:illust\_hardness](b) (and formally established later). Particularly, the cost value, though undefined outside the set $\cK$, remains finite around the boundary of $\cK$. Hence, the decrease of cost from $K$ to $K'$ cannot guarantee that the iterate does not travel towards, and even beyond the feasibility boundary. With no strict separation between the cost level set and $\cK^c$, there may not exist a constant stepsize that induces global convergence to the optimal policy.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

These two challenges naturally raise the question: does there exist any computationally tractable PO method, which preserves the robustness constraint along the iterations, and enjoys (hopefully global) convergence guarantees? We provide a positive answer to this question in the present work. Our key contribution is three-fold: First, we study the landscape of mixed $\cH_2/\cH_\infty$ design problems for both discrete- and continuous-time settings, and propose three policy-gradient based methods, inspired by those for LQR [fazel2018global,bu2019LQR]. Second, we prove that two of them (the Gauss-Newton method and the natural PG method) enjoy the implicit regularization property, such that the iterates are automatically biased to satisfy the required $\cH_\infty$ constraint. Third, we establish the global convergence of those two PO methods to the globally optimal policy with globally sublinear and locally (super-)linear rates under certain conditions, despite the nonconvexity of the problem.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, the two policy search directions always lead to convergence to the global optimum, without getting stuck at any spurious stationary point/local optima. Along the way, we also derive new results on linear risk-sensitive control, i.e., LEQG problems, and discuss the connection of mixed design to zero-sum LQ dynamic games, for designing model-free versions of the algorithms. We expect our work to help pave the way for rigorous understanding of PO methods for general optimal control with $\cH_\infty$robustness guarantees.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Introduction", "weight": 1.5} -->

| 0ptwidth=0.4 figs/contour_LQR.png | 16ptwidth=0.4 figs/contour_LEQR.png | Comparison of the landscapes of LQR and mixed $\cH_2/\cH_\infty$ control design that illustrates the hardness of showing convergence of the latter. The dashed lines represent the boundaries of the constraint sets $\mathcal{K}$. For (a) LQR, $\mathcal{K}$ is the set of all linear stabilizing state-feedback controllers; for (b) mixed $\cH_2/\cH_\infty$ control, $\mathcal{K}$ is set of all linear stabilizing state-feedback controllers satisfying an extra $\cH_\infty$ constraint on some input-output channel. The solid lines represent the contour lines of the cost $ \cJ(K)$. $K$ and $K'$ denote the control gain of two consecutive iterates; $\bigstar$ denotes the global optimizer.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Introduction", "weight": 1.5} -->

Note that the concept of (implicit) regularization has been adopted in many recent works on nonconvex optimization, including training neural networks [allen2018learning,kubo2019implicit], phase retrieval [chen2015solving,ma2017implicit], matrix completion [chen2015fast,zheng2016convergence], and blind deconvolution [li2019rapid], referring to any scheme that biases the search direction of the optimization algorithms. The term implicit emphasizes that the algorithms without regularization may behave as if they are regularized. This property has been advocated as an important feature of gradient-based methods for solving aforementioned nonconvex problems. We emphasize that it is a feature of both the problem and the algorithm, i.e., it holds for certain algorithms that solve certain problems. This is precisely the case in the present work.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Introduction", "weight": 1.5} -->

The specific search directions of the Gauss-Newton and the natural PG methods bias the iterates towards the set of the stabilizing controllers satisfying the $\cH_\infty$ constraint, although no explicit regularization, e.g., projection, is adopted, which contrasts to that the stability-preserving of PO methods for LQR problems is algorithm-agnostic. To the best of our knowledge, our work appears to be the first studying the implicit regularization properties of PO methods for learning-based control in general.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Introduction", "weight": 1.5} -->

Mixed $\cH_2/\cH_\infty$ & Risk-Sensitive Control. The history of mixed $\cH_2/\cH_\infty$ control design dates back to the seminal works [bernstein1989lqg,khargonekar1991mixed] for continuous-time settings, built upon the Riccati equation approach and the convex optimization approach, respectively. Such a formula can be viewed as a surrogate/sub-problem of the more challenging $\cH_\infty$-control problem, where the goal is to find the optimal controller that minimizes the $\cH_\infty$-norm [doyle1988state]. These formulation and approaches were then investigated for discrete-time systems in [mustafa1991lqg,kaminer1993mixed]. A non-smooth constrained optimization perspective for solving mixed design problems was adopted in [apkarian2008mixed], with proximity control algorithm designed to handle the constraints explicitly, and convergence guarantees to stationary-point controllers.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Introduction", "weight": 1.5} -->

Numerically, there also exist other packages for multi-objective $\cH_2/\cH_\infty$ control [gumussoy2009multiobjective,arzelier2011h2] that are based on non-smooth nonconvex optimization. However, in spite of achieving impressive numerical performance, these methods have no theoretical guarantees for either the global convergence or the $\cH_\infty$-norm constraint violation. It is also not clear yet how these methods can be made model-free. On the other hand, risk-sensitive control with exponential performance measure was originally proposed by [jacobson1973optimal] for the linear quadratic case, and then generalized in [whittle1981risk,fleming1997risk,borkar2002risk,jaskiewicz2007average]. Under certain conditions on the cost, noise, and risk factor, convex optimization perspectives on linear risk sensitive control have been reported.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, first-order optimization methods have also been applied to finite-horizon risk sensitive nonlinear control, but the control inputs (instead of the policy) are treated as decision variables [roulet2019convergence]. Convergence to stationary points was shown therein for the iterative LEQG algorithm. Interestingly, there is a relationship between mixed design and risk-sensitive control, as established in [glover1988state,whittle1990risk]. These two classes of problems can also be unified with maximum-entropy $\cH_\infty$ control [glover1988state,mustafa1989relations] and zero-sum dynamic games [jacobson1973optimal,bacsar1995h]. Besides these direct controller/policy search methods, general mixed $\cH_2/\cH_\infty$ control can also be tackled via Youla-parameterization based approaches, which lead to convex programming problems that can be solved numerically.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, actual implementation of these approaches either require a finite-horizon truncation of system impulse responses, which loses optimality guarantees, or require solution of (a large enough sequence of) semi-definite programs or linear matrix inequalities with lifted dimensions, which may not be computationally efficient for large-scale dynamical systems. More importantly, it is not clear yet how to implement these approaches in the data-driven regime, without identifying the model. In contrast, the direct search methods can easily be made model-free, see e.g., our recent attempt for robust control design.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Introduction", "weight": 1.5} -->

Constrained MDP & Safe RL. The mixed design formulation is also pertinent to constrained dynamic control problems, usually modeled as constrained MDPs (CMDPs) [altman1999constrained]. However, the constraint in CMDPs is generally imposed on either the expected long-term cost [borkar2005actor,achiam2017constrained,chow2018lyapunov], which shares the additive-in-time structure as the objective, or some risk-related constraint [di2012policy,chow2015risk,chow2017risk]. Those constraints are in contrast to the $\cH_\infty$ robustness constraint considered here. Under the CMDP model, various safe RL algorithms, especially PO-based ones, have been developed [borkar2005actor,geibel2005risk,di2012policy,chow2015risk,achiam2017constrained,chow2018lyapunov,yu2019convergent].

<!-- chunk {"id": "body-0030", "role": "body", "section": "Introduction", "weight": 1.5} -->

It is worth mentioning that except [achiam2017constrained,chow2018lyapunov], other algorithms cannot guarantee the constraint to be satisfied during the learning iterations, as opposed to our on-the-fly implicit regularization property. Recently, safety constraint has also been incorporated into the LQR model for model-based learning control [dean2019safely]. Several recent model-based safe RL algorithms include [garcia2012safe,aswani2013provably,akametalu2014reachability,berkenkamp2017safe].

<!-- chunk {"id": "body-0031", "role": "body", "section": "Introduction", "weight": 1.5} -->

PO for LQR stemmed from the adaptive policy iteration algorithm in [bradtke1994adaptive]. Lately, studying the global convergence of policy-gradient based methods for LQR [fazel2018global,tu2018gap,malik2019derivative,bu2019LQR,gravell2019learning, mohammadi2019global, mohammadi2019convergence, jansch2020convergence, venkataraman2019recovering] has drawn increasing attention. Specifically, [fazel2018global] first identified the landscape of PO for LQR problems that stationary point implies global optimum, which motivated the development of first-order methods for solving this nonconvex problem. A more comprehensive landscape characterization was then reinforced in [bu2019LQR], where the coercive property of LQR cost was explicitly mentioned.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Introduction", "weight": 1.5} -->

Based on these, [malik2019derivative] advocated two-point zeroth-order methods to improve the sample complexity of model-free PG; [yang2019global] proposed actor-critic algorithms with non-asymptotic convergence guarantees; [tu2018gap] compared the asymptotic behavior of model-based and model-free PG methods, with focus on finite-horizon LQR problems. Recently, the continuous-time setup has been considered in [mohammadi2019global, mohammadi2019convergence], and the extensions to Markov jump linear quadratic control have been presented in [jansch2020convergence]. [gravell2019learning] considered LQR with multiplicative noises, in order to improve the controller's robustness. The robustness issue for the output feedback case has been further discussed in [venkataraman2019recovering].

<!-- chunk {"id": "body-0033", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robustness with respect to the model uncertainty/misspecification has long been a significant concern in RL. Indeed, the early attempt for robust RL was based on the notion of $\cH_\infty$ robustness considered here [morimoto2005robust], where the uncertainty was modeled as the control of an adversarial agent playing against the nominal controller. This game-theoretic perspective, as we will also discuss in [subsec:connection\_to\_games], enabled the development of actor-critic based algorithms therein, though without theoretical analysis. Such an idea has recently been carried forward in the empirical work [pinto2017robust], which proposed PO methods alternating between the two agents. Another line of work follows the robust MDP framework [nilim2005robust,iyengar2005robust], with RL algorithms developed in [lim2013reinforcement,lim2019kernel,chen2019action,mankowitz2019robust].

<!-- chunk {"id": "body-0034", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, these algorithms apply to only tabular/small-scale MDPs (not continuous control tasks) and/or do not belong to PO methods that guarantee robustness during learning. More recently, linear control design against adversarial disturbances has also been placed in the online learning context [cohen2018online,agarwal2019online,agarwal2019logarithmic] to achieve nearly-optimal regret, where either the dynamics or the cost functions are adversarially changing. Model-based methods also exist for continuous control tasks [berkenkamp2015safe,dean2019robust].

<!-- chunk {"id": "body-0035", "role": "body", "section": "Motivating Example: LEQG", "weight": 1.0} -->

We start with an example of risk-sensitive control, the infinite-horizon state-feedback linear exponential quadratic Gaussian problem Unless otherwise noted, we will just refer to this problem as LEQG hereafter. [jacobson1973optimal], which is motivating in that: is closely related to the well-known linear optimal control problems, e.g., LQR and state-feedback LQG; ii) it illustrates the idea of mixed control design, especially introducing the $\cH_\infty$-norm constraint, though implicit, that guarantees robustness. The latter manifests the challenge in the convergence analysis of PO methods for this problem.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Motivating Example: LEQG", "weight": 1.0} -->

Specifically, at time $t\geq 0$, the agent takes an action $u_t\in\RR^d$ at state $x_t\in\RR^m$, which leads the system to a new state $x_{t+1}$ by a linear dynamical system where $A$ and $B$ are matrices of proper dimensions, $x_0\in\RR^{m}$ and $w_t\in\RR^{m},\forall t\geq 0$ are independent zero-mean Gaussian random variables with positive-definite covariance matrices $X_0$ and $W$, respectively. The one-stage cost of applying control $u$ at state $x$ is given by $ where $Q$ and $R$ are positive-definite matrices. Then, the long-term cost to minimize is where $\beta$ is the parameter that describes the intensity of risk-sensitivity, and the expectation is taken over the randomness of both $x_0$ and $w_t$ for all $t\geq 0$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Motivating Example: LEQG", "weight": 1.0} -->

The intuition behind the objective [equ:def_obj] is that by Taylor series expansion around $\beta=0$, Hence, if $\beta>0$, the control is risk-averse since minimization also places positive weight on the variance, in addition to the expectation, of the cost; in contrast, if $\beta<0$, the control is referred to as risk-seeking, which encourages the variance to be large. As $\beta\to 0$, the objective [equ:def_obj] reduces to the risk-neutral objective of LQR/state-feedback LQG. Usually LEQG problems consider the case of $\beta>0$. In this sense, LEQG can be viewed as a generalization of LQR/state-feedback LQG problems.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Motivating Example: LEQG", "weight": 1.0} -->

The goal of LEQG is to find the optimal control policy $\mu_t:(\RR^m\times \RR^d)^{t}\times\RR^m\to \RR^d$, which in general is a mapping from the history of state-action pairs till time $t$ and current state $x_t$, to the action $u_t$ in $\RR^d$, that minimizes the cost in [equ:def\_obj]. By assuming that such an optimal policy exists, the $\limsup$ in [equ:def\_obj] can be replaced by $\lim$. Moreover, we can show, see a formal statement in Lemma [lemma:optimal] in [sec:aux\_res], that the optimal control has a desired property of being memoryless and stationary, i.e., linear time-invariant (LTI), and current state-feedback, i.e., $ for some $K\in\RR^{d\times m}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Motivating Example: LEQG", "weight": 1.0} -->

Hence, it suffices to optimize over the control gain $K$, without loss of optimality, i.e.,

<!-- chunk {"id": "body-0040", "role": "body", "section": "Cost Closed-Form", "weight": 1.0} -->

[eq:obj\_K] with PO methods, it is necessary to establish the closed-form of the objective with respect to $K$. To this end, we introduce the following algebraic Riccati equation for given control gain $K$. If $\beta\rightarrow 0$, [equ:def\_mod\_Bellman\_ori] reduces to the Lyapunov equation of policy evaluation for given $K$ in LQR problems. For notational simplicity, we also define $\tP_K$ as Then, the objective $\cJ(K)$ can be expressed by the solution to [equ:def\_mod\_Bellman\_ori], $P_K$, as follows.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Cost Closed-Form", "weight": 1.0} -->

For any stabilizing LTI state-feedback controller $u_t=-Kx_t$, such that the Riccati equation [equ:def\_mod\_Bellman\_ori] admits a solution $P_K\geq 0$ that: i) is stabilizing, i.e., $\rho\big((A-BK)^\top(I-\beta P_KW)^{-1}\big)<1$, and ii) satisfies $W^{-1}-\beta P_K>0$, $\cJ(K)$ has the form of Note that when $\beta\to 0$, the objective [equ:obj\_logdet\_form] reduces to $\tr (P_KW)$, the cost function for LQG problems.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Cost Closed-Form", "weight": 1.0} -->

To the best of our knowledge, our results on that the optimal controller is LTI state-feedback in Lemma [lemma:optimal], and on the form of the objective $\cJ(K)$ in Lemma [lemma:LEQR\_obj\_form\_for\_K], though expected, have not been rigorously established for LEQG problems in the literature. For completeness, we present a self-contained proof in [sec:aux\_res]. Interestingly, the former argument has been hypothesized in Section $3$ of [glover1988state]; while the form of $\cJ(K)$ in [equ:obj\_logdet\_form] connects to the performance criterion for more general optimal control problems with robustness guarantees, as to be shown shortly.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Implicit Constraint on $\\cH_\\infty$-Norm", "weight": 1.0} -->

[eq:obj\_K] is an unconstrained optimization over $K$. However, as identified by [glover1988state], there is an implicit constraint set for this problem, which corresponds to the lower-level set of the $\cH_{\infty}$-norm of the closed-loop transfer function under the linear stabilizing controller $u=-Kx$. We reiterate the result as follows.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Implicit Constraint on $\\cH_\\infty$-Norm", "weight": 1.0} -->

Consider the LEQG problem in [eq:obj\_K] that finds the optimal stationary state-feedback control gain $K$, and a closed-loop transfer function from the noise $\{w_t\}$ to the output, $\cT(K)$, as Then, the feasible set of $\cJ(K)$ is the intersection of the set of linear stabilizing feedback controllers and the $1/\sqrt{\beta}$-lower-level set of the $\cH_{\infty}$-norm of $\cT(K)$, i.e., $\big\{K\biggiven \rho(A-BK)<1, \,\,\mbox{and}\,\,\|\cT(K)\|_{\infty}<1/\sqrt{\beta}\big\}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Implicit Constraint on $\\cH_\\infty$-Norm", "weight": 1.0} -->

The result follows by applying the results in Section $3$ in [glover1988state], writing out the transfer function, and replacing the $\theta$ therein by the $-\beta$ here.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Implicit Constraint on $\\cH_\\infty$-Norm", "weight": 1.0} -->

We note that the feasible set for LEQG in Lemma [lemma:LEQR\_feasible\_set] may not necessarily be bounded. This feasible set, though quite concise to characterize, is hard to enforce directly onto the control gain $K$, since it is a frequency-domain characterization using the $\cH_\infty$-norm. To develop PO algorithms for finding $K$, the time-domain characterization in Lemma [lemma:LEQR\_obj\_form\_for\_K] is more useful. Interestingly, as we will show shortly, the conditions that lead to the form of $\cJ(K)$ in Lemma [lemma:LEQR\_obj\_form\_for\_K] are indeed equivalent to the feasible set given by $\cH_\infty$-norm constraint in Lemma [lemma:LEQR\_feasible\_set]; see Remark [remark:necess\_lemma\_LEQR\_obj].

<!-- chunk {"id": "body-0047", "role": "body", "section": "Implicit Constraint on $\\cH_\\infty$-Norm", "weight": 1.0} -->

In fact, this reformulation of LEQG as a constrained optimization problem, belongs to a general class problems, mixed $\cH_{2}/\cH_{\infty}$ control designwith state-feedback.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Bigger Picture: Mixed $\\cH_2/\\cH_{\\infty}$ Control Synthesis", "weight": 1.0} -->

Consider the following discrete-time linear dynamical system with a single input-output channel where $x_t\in\RR^{m},u_t\in\RR^d$ denote the states and controls, respectively, $w_t\in\RR^n$ is the disturbance, $z_t\in\RR^l$ is the controlled output, and $A,B,C,D,E$ are matrices of proper dimensions. Consider the admissible control policy $\mu_t$ to be a mapping from the history of state-action pairs till time $t$ and the current state $x_t$ to action $u_t$. It has been shown in [kaminer1993mixed] that, LTI state-feedback controller (without memory) suffices to achieve the optimal performance of mixed $\cH_2/\cH_\infty$ design under this state-feedback information structure For discrete-time settings, if both the (exogenous) disturbance $w_t$ and the state $x_t$ are available, i.e., under the full-information feedback case, LTI controllers may not be optimal.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Bigger Picture: Mixed $\\cH_2/\\cH_{\\infty}$ Control Synthesis", "weight": 1.0} -->

Interestingly, for continuous-time settings, LTI controllers are indeed optimal.. As a consequence, it suffices to consider only stationary, current state-feedback controller parametrized as $u_t=-Kx_t$. [Justification of LTI Control for LEQG] As to be shown shortly, LEQG is a special case of mixed $\cH_2/\cH_\infty$ design. Hence, the result we derived in Lemma [lemma:optimal], i.e., the optimal controller of LEQG is indeed LTI, is consistent with this earlier result on mixed design from [khargonekar1991mixed,kaminer1993mixed].

<!-- chunk {"id": "body-0050", "role": "body", "section": "Bigger Picture: Mixed $\\cH_2/\\cH_{\\infty}$ Control Synthesis", "weight": 1.0} -->

In accordance with this parametrization, the transfer function from the disturbance $w_t$ to the output $z_t$ can be represented as In common with [glover1988state,khargonekar1991mixed,bacsar1995h], we make the following assumption on the matrices $A,B,C,D$ and $E$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Bigger Picture: Mixed $\\cH_2/\\cH_{\\infty}$ Control Synthesis", "weight": 1.0} -->

The matrices $A,B,C,D,E$ in [equ:mixed\_design\_transfer] satisfy $E^\top [C ~~ E]=[0~~ R]$ for some $R>0$. [assum:coeff\_matrices] is fairly standard, which clarifies the exposition substantially by normalising the control weighting and eliminating cross-weightings between control signal and state [bacsar1995h]. Hence, the transfer function in [equ:mixed\_design\_transfer] has the equivalent form Strictly speaking, the transfer functions for equ:mixed\_design\_transfer and equ:mixed\_design\_transfer2 are equivalent in the sense that the values of $\cT^{\sim}(K) \cT(K)$ are the same for all the points on the unit circle.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Bigger Picture: Mixed $\\cH_2/\\cH_{\\infty}$ Control Synthesis", "weight": 1.0} -->

Hence, robustness of the designed controller can be guaranteed by the constraint on the $\cH_\infty$-norm, i.e., $\|\cT(K)\|_{\infty}<\gamma$ for some $\gamma>0$. The intuition behind the constraint, which follows from small gain theorem [zames1966input], is that the constraint on $\|\cT(K)\|_{\infty}$ implies that the closed-loop system is robustly stable in that any stable transfer function $\Delta$ satisfying $\|\Delta\|_{\ell_2\to\ell_2}<1/\gamma$ may be connected from $z_t$ back to $w_t$ without destablizing the system. For more background on $\cH_\infty$ control, see [bacsar1995h,zhou1996robust].

<!-- chunk {"id": "body-0053", "role": "body", "section": "Bigger Picture: Mixed $\\cH_2/\\cH_{\\infty}$ Control Synthesis", "weight": 1.0} -->

For notational convenience, we define the feasible set of mixed $\cH_{2}/\cH_{\infty}$ control design as We note that the set $\cK$may be unbounded.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Bigger Picture: Mixed $\\cH_2/\\cH_{\\infty}$ Control Synthesis", "weight": 1.0} -->

In addition to the constraint, the objective of mixed $\cH_{2}/\cH_{\infty}$ design is usually an upper bound of the $\cH_2$ norm of the closed-loop system. By a slight abuse of notation, let $\cJ(K)$ be the cost function of mixed design. Then the common forms of $\cJ(K)$ include [mustafa1989relations,mustafa1991lqg] where $P_K$ is the solution to the following Riccati equation (A-BK)^\_K (A-BK)+C^C+K^RK-P\_K=0, By Lemma [lemma:LEQR\_feasible\_set], replacing $\beta$, $W$, and $Q$ in LEQG by $\gamma^{-2}$, $DD^\top$ and $C^\top C$, respectively, yields the formulation of mixed $\cH_{2}/\cH_{\infty}$ design.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Bigger Picture: Mixed $\\cH_2/\\cH_{\\infty}$ Control Synthesis", "weight": 1.0} -->

In particular, the closed-form cost of LEQG that we derived for the first time, see Lemma [lemma:LEQR\_obj\_form\_for\_K], is identical to the cost in [equ:form\_J2]; and the implicit constraint of LEQG in Lemma [lemma:LEQR\_feasible\_set] is exactly the $\cH_\infty$-norm constraint in [equ:define\_cK]. Thus, LEQG is a mixed-design problem with $D=W^{1/2}$ and $\cJ(K)$ being [equ:form\_J2]. Note that $DD^\top =W>0$ for LEQG.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Bigger Picture: Mixed $\\cH_2/\\cH_{\\infty}$ Control Synthesis", "weight": 1.0} -->

All three objectives in [equ:form\_J1]-[equ:form\_J3] are upper bounds of the $\cH_2$-norm [mustafa1989relations,mustafa1991lqg]. In particular, cost [equ:form\_J1] has been adopted in [bernstein1989lqg,haddad1991mixed], which resembles the standard $\cH_2$ control/LQG control objective, but with $P_K$ satisfying a Riccati equation instead of a Lyapunov equation. Cost [equ:form\_J2] is closely related to maximum entropy $\cH_\infty$-control, see the detailed relationship between the two in [mustafa1990minimum]. In addition, cost [equ:form\_J3] can also be connected to the cost of LQG using a different Riccati equation [mustafa1991lqg].

<!-- chunk {"id": "body-0057", "role": "body", "section": "Bigger Picture: Mixed $\\cH_2/\\cH_{\\infty}$ Control Synthesis", "weight": 1.0} -->

As $\gamma\to \infty$, the costs in all [equ:form\_J1]-[equ:form\_J3] reduce to the cost for LQG, i.e., $\cH_2$control design problems.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Bigger Picture: Mixed $\\cH_2/\\cH_{\\infty}$ Control Synthesis", "weight": 1.0} -->

In sum, the mixed $\cH_2/\cH_\infty$ control design can be formulated as with $\cJ(K)$ and $\cK$ defined in [equ:form\_J1]-[equ:form\_J3] and [equ:define\_cK], respectively.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Bounded Real Lemma", "weight": 1.0} -->

Though the constraint [equ:define\_cK] is concise, it is hard to enforce over $K$ in policy optimization, since the constraint is defined in the frequency domain. Interestingly, by using a significant result in robust control theory, i.e., Bounded Real Lemma [bacsar1995h], [zhou1996robust,rantzer1996kalman], constraint [equ:define\_cK] can be related to the solution of a Riccati equation and a Riccati inequality. We formally introduce the result as follows, whose proof is deferred to [sec:proof\_lemma\_bounded\_real\_lemma].

<!-- chunk {"id": "body-0060", "role": "body", "section": "Bounded Real Lemma", "weight": 1.0} -->

Consider a discrete-time transfer function $\cT(K)$ defined in [equ:mixed\_design\_transfer2], suppose $K$ is stabilizing, i.e.,

<!-- chunk {"id": "body-0061", "role": "body", "section": "Bounded Real Lemma", "weight": 1.0} -->

- $\|\cT(K)\|_{\infty}<{\gamma}$, which, due to $\rho(A-BK)<1$, further implies $K\in\cK$ with $\cK$ defined in [equ:define\_cK]. - The Riccati equation [equ:discret\_riccati] admits a unique stabilizing solution $P_K\geq 0$ such that: i) $I-\gamma^{-2}D^\top P_K D>0$; ii) $(I-\gamma^{-2} P_KDD^\top)^{-\top}(A-BK)$ is stable; - There exists some $P> 0$, such that where $\tP:=P+PD(\gamma^2I-D^\top P D)^{-1}D^\top P$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Bounded Real Lemma", "weight": 1.0} -->

The three equivalent conditions in Lemma [lemma:discrete\_bounded\_real\_lemma] will be frequently used in the ensuing analysis. Note that the unique stabilizing solution to [equ:discret\_riccati] for any $K\in\cK$, is also minimal, if the pair $(A-BK,D)$ is stabilizable, see [ran1988existence]. This holds since $K\in\cK$ is indeed stabilizing. Thus, the optimal control that minimizes [equ:form\_J1]-[equ:form\_J3], which are all monotonically increasing with respect to $P_K$, only involves the stabilizing solution $P_K$. Hence, it suffices to consider only stabilizing solution $P_K$ of the Riccati equation [equ:discret\_riccati]for LEQG.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Bounded Real Lemma", "weight": 1.0} -->

By Lemma [lemma:discrete\_bounded\_real\_lemma] and Remark [remark:special\_case], the conditions in Lemma [lemma:LEQR\_obj\_form\_for\_K] are equivalent to the $\cH_\infty$-norm constraint in [equ:define\_cK] for LEQG. This implies that these conditions are not only sufficient for the form of $\cJ(K)$ in Lemma [lemma:LEQR\_obj\_form\_for\_K] to hold, but also necessary. In other words, any feasible $K\in\cK$ should lead to the form of $\cJ(K)$ in [equ:obj\_logdet\_form]. develop policy optimization algorithms for solving the mixed $\cH_2/\cH_\infty$ control problem in [equ:def\_mixed\_formulation].

<!-- chunk {"id": "body-0064", "role": "body", "section": "Bounded Real Lemma", "weight": 1.0} -->

- The control gain $K$ lies in $\cK$ defined in [equ:define\_cK], i.e., $\|\cT(K)\|_{\infty}<1/\sqrt{\gamma}$; - The modified Bellman equations [equ:def\_PK]-[equ:def\_tPK] admit a unique stabilizing solution $P_K> 0$ such that: i) $W^{-1}-\gamma P_K>0$; ii) $(A-BK)^\top(I-\gamma P_KW)^{-1}$ is stable; - There exists some $P>0$, such that where $\tilde{P}:=P+\gamma P(W^{-1}-\gamma P)^{-1}P$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Bounded Real Lemma", "weight": 1.0} -->

The proof follows by letting $C^\top C$ in [XXX] be $Q+K^\top RK$, and $B$ in [XXX] be $W^{1/2}$, and applying Lemma [lemma:discrete\_bounded\_real\_lemma]. Note that both $P_K$ and $P$ are positive definite, since [coro:discrete\_equiva\_set\_cK] shows that the conditions in Lemma [lemma:LEQR\_obj\_form\_for\_K] are not only sufficient, but also necessary for the existence of $\cJ(K)$ for LEQR problems. Also, the form of the objective $\cJ(K)$ we derived in Lemma lemma:LEQR\_obj\_form\_for\_K coincides with one of the commonly used performance criteria $\cJ_3$ in XXX for mixed design.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Landscape and", "weight": 1.0} -->

In this section, we investigate the optimization landscape of mixed $\cH_2/\cH_\infty$ control design, and develop policy optimization algorithms with convergence guarantees. In particular, we study both discrete- and continuous-time settings focusing on two representative example costs $\cJ(K)$ from [equ:form\_J2] and [equ:form\_J1], respectively.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Landscape and", "weight": 1.0} -->

Although only two example settings are studied in detail, the techniques developed can also be applied to other combinations of settings, e.g., cost equ:form\_J1 in discrete-time settings.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Landscape and", "weight": 1.0} -->

The first combination of settings also by chance solves the discrete-time LEQG problems introduced in [sec:mot\_example]. The second combination for continuous-time settings is discussed in [sec:aux\_cont\_res].

<!-- chunk {"id": "body-0069", "role": "body", "section": "Optimization Landscape", "weight": 1.0} -->

We start by showing that, regardless of the cost $\cJ(K)$, the mixed-design problem in [equ:def\_mixed\_formulation] is a nonconvexoptimization problem.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Optimization Landscape", "weight": 1.0} -->

The discrete-time mixed $\cH_{2}/\cH_{\infty}$ design problem [equ:def\_mixed\_formulation] is nonconvex.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Optimization Landscape", "weight": 1.0} -->

The proof of Lemma [lemma:nonconvex\_Hinf\_norm\_set] is deferred to [sec:proof\_lemma:nonconvex]. In particular, we show by an easily-constructed example that the convex combination of two control gains $K$ and $K'$ in $\cK$ may no longer lie in $\cK$. As a result, this nonconvexity poses challenges in solving [equ:def\_mixed\_formulation] using standard policy gradient-based approaches. Note that similar nonconvexity of the constraint set also exists in LQR problems [fazel2018global,bu2019LQR], and has been recognized as one of the main challenges to address. Still, the landscape of LQR has some desired property of being coercive [bu2019LQR], which played a significant role in the analysis of PO methods for LQR. However, we establish in the following lemma that such a coercivity does not hold for mixed design problems.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Optimization Landscape", "weight": 1.0} -->

The cost functions [equ:form\_J1]-[equ:form\_J3] for discrete-time mixed $\cH_{2}/\cH_{\infty}$ design are not coercive. Particularly, as $K\to \partial \cK$, where $\partial \cK$ is the boundary of the constraint set $\cK$, the cost $\cJ(K)$ does not necessarily approach infinity.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Optimization Landscape", "weight": 1.0} -->

The proof of Lemma [lemma:mixed\_design\_no\_coercivity] is provided in [sec:proof\_lemma\_mixed\_design\_no\_coercivity]. The key of the argument is that for given $K\in\cK$, the policy evaluation equation for mixed design problems is a Riccati equation, see [equ:discret\_riccati] (a quadratic equation of $P_K$ in $1$-dimensional case); while for LQR problems, the policy evaluation equation is a Lyapunov equation, which is essentially linear. Hence, some additional condition on $K$ is required for the existence of the solution, which can be restricter than the conditions on $K$ and $P_K$ that makes the cost $\cJ(K)$ finite. In this case, the existence condition of the solution characterizes the boundary of $\cK$, which leads to a well-defined $P_K$, and thus a finite value of the cost $\cJ(K)$, even when $K$ approaches the boundary $\partial \cK$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Optimization Landscape", "weight": 1.0} -->

The lack of coercivity turns out to be the greatest challenge when analyzing the stability/feasibility of PO methods for mixed control design, in contrast to LQR problems. Detailed discussion on this is provided in [subsec:implicit\_reg]. The illustration in Figure [fig:illust\_hardness] in [sec:intro] of the landscape of mixed design problems was actually based on Lemmas [lemma:nonconvex\_Hinf\_norm\_set] and [lemma:mixed\_design\_no\_coercivity]. We then show the differentiability of $\cJ(K)$ at each $K$ within the feasible set $\cK$, and provide the closed-form of the policy gradient. Here we focus on the most complicated objective defined in [equ:form\_J2] among the three in [equ:form\_J1]-[equ:form\_J3], due to its direct connection to the risk-sensitive control problem; see Remark [remark:special\_case].

<!-- chunk {"id": "body-0075", "role": "body", "section": "Optimization Landscape", "weight": 1.0} -->

We note that the proof can be used directly to establish similar results for the other two objectives, namely, [equ:form\_J1] and [equ:form\_J3], too.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Optimization Landscape", "weight": 1.0} -->

The cost $\cJ(K)$ defined in [equ:form\_J2] is differentiable in $K$ for any $K\in\cK$, and the policy gradient has the following form: where $\Delta_K\in\RR^{m\times m}$ is a matrix given by and $\tP_K$ is defined in [equ:def\_tP\_K].

<!-- chunk {"id": "body-0077", "role": "body", "section": "Optimization Landscape", "weight": 1.0} -->

The proof of Lemma [lemma:differentiability\_policy\_grad] is provided in [sec:proof\_lemma\_differentiability\_policy\_grad]. Note that Lemma [lemma:differentiability\_policy\_grad] also implies some property on the landscape of $\cJ(K)$. Specifically, if $\Delta_K>0$ is full-rank, then $\nabla \cJ(K)=0$ admits a unique solution $K=(R+B^\top \tP_{K} B)^{-1}B^\top \tP_{K} A$, which corresponds to the unique global optimum. Otherwise, if $\Delta_K\geq 0$ is not full-rank, there can be multiple stationary points. Yet, the global optimum is still of the same form. We formally establish this in the following proposition, which is proved in [proof:coro\_opt\_control\_form].

<!-- chunk {"id": "body-0078", "role": "body", "section": "Optimization Landscape", "weight": 1.0} -->

Suppose that the discrete-time mixed $\cH_2/\cH_\infty$ design admits a global optimal solution $K^*\in\cK$; then, one such solution has the form of $K^*=(R+B^\top \tP_{K^*} B)^{-1}B^\top \tP_{K^*} A$. Additionally, if the pair $\big((I-\gamma^{-2} P_KDD^\top)^{-\top}(A-BK),D\big)$ is controllable at some stationary point of $\cJ(K)$, such that $\nabla \cJ(K)=0$, then this is the unique stationary point, and corresponds to the unique global optimizer $K^*$.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Optimization Landscape", "weight": 1.0} -->

The form of the optimal control gain $K^*$ above echoes back that of the solution to finite-horizon LEQG [jacobson1973optimal], [whittle1990risk]. Note that for LEQG problems, $D=W^{1/2}>0$ implies that the controllability condition holds automatically. Thus, this $K^*$ corresponds to the unique global optimizer. We also remark that the landscape result above can also be shown for the other two objectives [equ:form\_J1] and [equ:form\_J3]. In fact, the key in proving Proposition [coro:opt\_control\_form\_discrete] is to show that $P_{K^*}$ is matrix-wise minimal in the positive semi-definite sense for all $P_K$ with $K\in\cK$.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Optimization Landscape", "weight": 1.0} -->

Note that since the objectives [equ:form\_J1] and [equ:form\_J3] are both monotonically non-decreasing in the eigenvalues of $P_K$, one can verify that the $K^*$ is also the global optimizer. Note that $K^*$ may not be the unique global minimizer without the controllability assumption. Finally, following the proof of Lemma [lemma:differentiability\_policy\_grad], one can show that the policy gradients for [equ:form\_J1] and [equ:form\_J3] yield an almost identical form as in Lemma [lemma:differentiability\_policy\_grad], except the definition of $\Delta_K$. Although the controllability assumption has been made in the literature [mustafa1991lqg], and is also satisfied automatically by LEQG problems, we will show next that our PO methods can find the global optimum $K^*$ even without this assumption.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Policy Optimization Algorithms", "weight": 1.0} -->

Consider three policy-gradient based methods as follows. For simplicity, we define We also suppress the iteration index, and use $K$ and $K'$ to represent the control gain before and after one-step of the update.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Policy Optimization Algorithms", "weight": 1.0} -->

The updates are motivated by and resemble the policy optimization updates for LQR [fazel2018global,bu2019LQR], but with $P_K$ therein replaced by $\tP_K$. The natural PG update is related to gradient over a Riemannian manifold; while the Gauss-Newton update is one type of quasi-Newton update, see [bu2019LQR] for further justifications on the updates. In particular, with $\eta=1/2$, the Gauss-Newton update [eq:exact\_gn] can be viewed as the policy iteration update for infinite-horizon mixed $\cH_2/\cH_\infty$ design. Model-free versions of the PG update [eq:exact\_pg] can be directly obtained, since the gradient $\nabla\cJ(K)$ can be estimated by sampled data, using for instance zeroth-order methods, as in [fazel2018global,malik2019derivative].

<!-- chunk {"id": "body-0083", "role": "body", "section": "Policy Optimization Algorithms", "weight": 1.0} -->

A direct model-free implementation of the natural PG update [eq:exact\_npg] using zeroth-order optimization methods requires estimating the matrix $\Delta_K$. It is not clear yet how to estimate it from the sampled trajectories. Instead, we propose one solution by the connections between mixed design and zero-sum linear quadratic games; see [sec:discussion] for more details. Finally, as in LQR problems, the Gauss-Newton update [eq:exact\_gn]cannot yet be estimated using zeroth-order methods directly.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Policy Optimization Algorithms", "weight": 1.0} -->

Model-free versions of the policy gradient update eq:exact\_pg and the natural PG update eq:exact\_npg can be obtained, if the gradient $\nabla\cJ(K)$ and the matrix $\Delta_K$ can be estimated by sampled data, using for instance zeroth-order methods, as. Nevertheless, as in LQR problems, the Gauss-Newton update eq:exact\_gn cannot yet be estimated using zeroth-order methods directly.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Policy Optimization Algorithms", "weight": 1.0} -->

BinComment: I think we need to be honest about whether the natural policy gradient can be directly made into a model-free version or not. I edited the above colored text as follows.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Policy Optimization Algorithms", "weight": 1.0} -->

Model-free versions of the policy gradient update eq:exact\_pg for LEQR can be directly obtained, since the gradient $\nabla\cJ(K)$ can be estimated by sampled data, using for instance zeroth-order methods, as. A direct model-free implementation of the natural PG update eq:exact\_npg using the zeroth-order optimization requires estimating the matrix $\Delta_K$ from the sampled trajectories of $\{x_t\}$. Currently we are unaware of such an estimator and we will investigate this issue in the future. We partially resolve this issue by developing a model-free implementation of the natural PG update using the connections between LEQR and the linear quadratic games. This is discussed in Section sec:discussion. Finally, as in LQR problems, the Gauss-Newton update eq:exact\_gn cannot yet be estimated using zeroth-order methods directly.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Theoretical Results", "weight": 1.0} -->

In this section, we investigate the convergence of the PO methods proposed in

<!-- chunk {"id": "body-0088", "role": "body", "section": "Implicit Regularization", "weight": 1.0} -->

The first key challenge in the convergence analysis for PO methods, is to ensure that the iterates remain feasible as the algorithms proceed, hopefully without the use of projection. This is especially significant in mixed design problems, as the feasibility here means robust stability, the violation of which can be catastrophic in practical online control design. We formally define the concept of implicit regularizationto describe this feature.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Implicit Regularization", "weight": 1.0} -->

For mixed $\cH_2/\cH_\infty$ control design problem [equ:def\_mixed\_formulation], suppose an iterative algorithm generates a sequence of control gains $\{K_n\}$. If $K_n\in\cK$ for all $n\geq 0$, this algorithm is called regularized; if it is regularized without projection onto $\cK$ for any $n\geq 0$, this algorithm is called implicitly regularized.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Implicit Regularization", "weight": 1.0} -->

The concept of (implicit) regularization has been adopted in many recent studies on nonconvex optimization, including training neural networks [allen2018learning,kubo2019implicit], phase retrieval [chen2015solving,ma2017implicit], matrix completion [chen2015fast,zheng2016convergence], and blind deconvolution [li2019rapid], referring to any scheme that biases the search direction of gradient-based algorithms. Implicit regularization has been advocated as an important feature of (stochastic) gradient descent methods for solving these problems, which, as the name suggests, means that the algorithms without regularization may behave as if they are regularized. Note that the term regularization may refer to several different schemes in different problems, e.g., trimming/truncation the gradient, adding a regularization term in the objective, etc. Here we focus on the scheme of projection, as summarized in [ma2017implicit].

<!-- chunk {"id": "body-0091", "role": "body", "section": "Implicit Regularization", "weight": 1.0} -->

Also note that implicit regularization is a feature of both the problem and the algorithm, i.e., it holds for certain algorithms that solve certain nonconvex problems.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Implicit Regularization", "weight": 1.0} -->

One possible way for the iterates to remain feasible is to keep shrinking the stepsize, whenever the next iterate goes outside $\cK$, following for example the Armijo rule [bertsekas1976goldstein]. However, as the cost $\cJ(K)$ is not necessarily smooth (see Lemma [lemma:cost\_diff] and its discussion later), it may not converge within a finite number of iterations [hintermuller2010nonlinear]. Another option is to project the iterate onto $\cK$. Nonetheless, it is challenging to perform projection onto the $\cH_\infty$-norm constraint set directly in the frequency domain.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Implicit Regularization", "weight": 1.0} -->

For LQR problems, due to the coercivity of the cost that as $K$ approaches the boundary of the stability/feasibility region $\{K\in\RR^{d\times m}\given \rho(A-BK)<1\}$, i.e., as $\rho(A-BK)\to 1$, the cost blows up to infinity, and due to the fact that the cost is continuous with respect to $K$, the lower-level set of the cost is compact [makila1987computational] and is contained within the stability region. As a consequence, there is a strict separation between any lower-level set of the cost and the set $\{K\in\RR^{d\times m}\given \rho(A-BK)\ge 1\}$. Hence, as discussed in the introduction, there exists a constant stepsize such that as long as the initialization control is stabilizing, the iterates along the path remain stabilizing and keep decreasing the cost.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Implicit Regularization", "weight": 1.0} -->

Such a property is algorithm-agnostic in that it is dictated by the property of the cost, and independent of the algorithms adopted, as long as they follow any descent directions of the cost. The stability proofs in [fazel2018global,bu2019LQR]for LQR are essentially built upon this idea.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Implicit Regularization", "weight": 1.0} -->

In contrast, for mixed $\cH_2/\cH_\infty$ design problems, lack of coercivity invalidates the argument above, as the control approaching the robustness constraint boundary $\partial \cK$ may incur a finite cost, and the descent direction may still drive the iterates out of the feasibility region. In addition, there may not exist a strict separation between all the lower-level sets of the cost and the complementary set $\mathcal{K}^c$. This difficulty has been illustrated in Figure [sec:intro] in the introduction, which compares the landscapes of the two problems. Interestingly, we show in the following theorem that the natural PG and Gauss-Newton methods in [eq:exact\_npg]-[eq:exact\_gn] enjoy the implicit regularization feature, with certain constant stepsize. We only highlight the idea of the proof here, and defer the details to [sec:proof\_thm\_stability\_update]. The proof includes two main steps.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Implicit Regularization", "weight": 1.0} -->

First, we directly use $P_K$ to construct a Lyapunov function for $K'$ to show a non-strict Riccati inequality that guarantees $\|\cT(K')\|_\infty\le{\gamma}$. Second, we further perturb $P_K$ in a specific way to show the strict inequality $\|\cT(K')\|_\infty<{\gamma}$. The perturbation argument is inspired by the proof of the Kalman-Yakubovich-Popov (KYP) Lemma [dullerud2013course].

<!-- chunk {"id": "body-0097", "role": "body", "section": "Implicit Regularization", "weight": 1.0} -->

Then the $K'$ obtained from [eq:exact\_npg]-[eq:exact\_gn] also lies in $\cK$. Equivalently, $K'$ is stabilizing, i.e., $\rho(A-BK')<1$, and satisfies that: i) there exists a solution $P_{K'}\geq 0$ to the Riccati equation [equ:discret\_riccati]; ii) $I-\gamma^{-2}D^\top P_{K'} D>0$; iii) $\rho\big((I-\gamma^{-2} P_{K'}DD^\top)^{-\top}(A-BK')\big)<1$.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Implicit Regularization", "weight": 1.0} -->

The general idea, contrary to the coercivity-based idea that works for any descent direction, is that we focus on the feasibility of $K'$ after an update along certain directions: either [eq:exact\_npg] or [eq:exact\_gn]. By Bounded Real Lemma, i.e., Lemma [lemma:discrete\_bounded\_real\_lemma], the feasibility condition for $K'$, if $K'$ is stabilizing, is equivalent to the existence of $P> 0$ such that the linear matrix inequalities (LMIs) in [equ:discrete\_equiva\_set\_cK\_cond] hold for $K'$. Moreover, it is straightforward to see that such a $P>0$, if exists, satisfies $(A-BK')^\top P (A-BK')-P<0$, which can be used to show that $K'$ is stabilizing [boyd1994linear]. Thus, it now suffices to find such a $P$.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Implicit Regularization", "weight": 1.0} -->

To show this, we first study the case with stepsizes being the upper bound in the theorem, i.e., $\eta=1/2$ for Gauss-Newton and $\eta= {1}/{(2\|R+B^\top \tP_K B\|)}$ for natural PG. As the solution to the Riccati equation [equ:discret\_riccati] under $K$, $P_K\geq 0$ satisfies $I-\gamma^{-2}D^\top P_K D>0$, the first LMI in [equ:discrete\_equiva\_set\_cK\_cond]. Hence, it may be possible to perturb $P_K$ to obtain a $P>0$, such that the equality in [equ:discret\_riccati] becomes a strict inequality of the second LMI in [equ:discrete\_equiva\_set\_cK\_cond], while preserving the first LMI.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Implicit Regularization", "weight": 1.0} -->

Moreover, if $K'$ is not too far away from $K$, such a perturbed $P_K$ should also work for $K'$. Such an observation motivates the use of $P_K$ as the candidate of $P$ for the LMIs in [equ:discrete\_equiva\_set\_cK\_cond] under $K'$.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Implicit Regularization", "weight": 1.0} -->

Indeed, it can be shown that substituting $P=P_K$ makes the second LMI in [equ:discrete\_equiva\_set\_cK\_cond] under $K'$ non-strict, namely, the left-hand side (LHS) $\leq 0$; see [equ:before\_perturb\_GN] in the detailed proof. To make it strict, consider the perturbed $P=P_K+\alpha \bar P$ for some $\alpha>0$, where $\bar P>0$ is the solution to some Lyapunov equation Such a Lyapunov equation [equ:def\_bar\_P\_sketch] always admits a solution $\bar P>0$, since $K\in\cK$ implies that $(I-\gamma^{-2} DD^\top P_K)^{-1}(A-BK)$ is stable. The intuition of choosing [equ:def\_bar\_P\_sketch] is as follows.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Implicit Regularization", "weight": 1.0} -->

First, the LHS of the second LMI in [equ:discrete\_equiva\_set\_cK\_cond] under $K'$ can be separated as =[(A-BK')^P(A-BK')-(A-BK)^P(A-BK)] +K'^R K'-K^R K\_1 By some algebra, the first term $\circled{1}$ is of order $o(\alpha)$. Since for small $\alpha$, this, combined with the Riccati equation [equ:discret\_riccati] and [equ:def\_bar\_P\_sketch], makes the second term $\circled{2}=-\alpha I+o(\alpha)$. Hence, there exists small enough $\alpha>0$ such that $\circled{1}+\circled{2}<0$, ensuring that the updated $K'$ is feasible.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Implicit Regularization", "weight": 1.0} -->

Lastly, by the linearity of LMIs, any interpolation of $K'$ with a smaller stepsize is also feasible/robustly stable, thus completing the proof. theoretically, it is not clear yet if vanilla PG enjoys implicit regularization. In the worst-case, as discussed right after Remark [remark:def\_implicit\_reg], vanilla PG may take infinitely many iterations to converge. Hence, hereafter, we only focus on the global convergence of natural PG method [eq:exact\_npg] and Gauss-Newton method [eq:exact\_gn], with constant stepsizes.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Implicit Regularization", "weight": 1.0} -->

The proof of Theorem [thm:stability\_update] is deferred to [sec:proof\_thm\_stability\_update]. Need to add a proof sketch. We note that the stability analysis here is more challenging to establish compared to that for linear quadratic regulators, see e.g. [fazel2018global]. Specifically, as pointed out earlier in [makila1987computational], and later in [bu2019LQR], the cost function of LQR has the desired property that as the control gain $K$ approaches the stability boundary, i.e., as $\rho(A-BK)\to 1$, the cost approaches infinity. This property, together with the fact that the cost is continuous with respect to $K$, one can conclude that the lower-level set of the cost is compact [makila1987computational] and is contained in the open set $\{K\in\RR^{d\times m}\given \rho(A-BK)<1\}$.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Implicit Regularization", "weight": 1.0} -->

Therefore, the stability argument follows since as long as the LQR cost is non-increasing along the iteration, the control gain $K$ remains to lie in the set $\{K\in\RR^{d\times m}\given \rho(A-BK)<1\}$, and thus remains stabilizing. This is recognized as the coercive property of LQR [bu2019LQR], and has played a significant role in showing the stability of policy gradient updates for LQR problems [bu2019LQR]. In addition, it is worth mentioning that such an idea of showing stability has been exploited and known as the homotopy argument in the robust control literature. [lemma:mixed\_design\_no\_coercivity], such a coercive property does not hold for mixed $\cH_2/\cH_\infty$ design. As a consequence, even if the cost is decreased along the iterations, it is still not guaranteed that the updated $K'$ lies in the feasible set, since it may incur a finite cost even beyond the feasible set.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Implicit Regularization", "weight": 1.0} -->

Hence, instead of using a homotopy argument that only considers the decrease of the cost (without concerning the descent direction), we here study the robustness of $K'$ by accounting for the specific descent directions that the updates [eq:exact\_npg]-[eq:exact\_gn] follow. Specifically, we use the linear matrix inequality theory to establish the robustness guarantees of the updates. See more details of the proof in [sec:proof\_thm\_stability\_update]. In this aspect, the last argument in Theorem [thm:stability\_update] shows that the updates [eq:exact\_npg]-[eq:exact\_gn] indeed enjoy the property of implicit regularization.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Global Convergence", "weight": 1.0} -->

global convergence here refers to two notions: i) the convergence performance of the algorithms starting from any feasible initialization point $K_0\in\cK$; ii) convergence to the global optimal policy under certain conditions. We formally establish the results for the natural PG [eq:exact\_npg] and Gauss-Newton [eq:exact\_gn]updates in the following theorem. and $\|K_0\|<\infty$. Then, under the In fact, for natural PG eq:exact\_npg, it suffices to require the stepsize $\eta\leq{1}/{(2\|R+B^\top \tP_{K_0} B\|)}$ for the initial $K_0$.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Global Convergence", "weight": 1.0} -->

as in Theorem [thm:stability\_update], both updates [eq:exact\_npg] and [eq:exact\_gn] converge to the global optimum $K^*=(R+B^\top \tP_{K^*} B)^{-1}B^\top \tP_{K^*} A$, in the sense that the average of $\{\|E_{K_n}\|_F^2\}$ over iterations converges to zero with $O(1/N)$ rate.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Global Convergence", "weight": 1.0} -->

The proof of Theorem [theorem:global\_exact\_conv] is detailed in [sec:proof\_theorem:global\_exact\_conv]. We remark that, the controllability assumption made in Proposition [coro:opt\_control\_form\_discrete] is not required for the global convergence here. Remarkably, there might be multiple stationary points such that $\nabla \cJ(K)=0$, while the two specific policy search directions [eq:exact\_npg] and [eq:exact\_gn] provably avoid the suboptimal local minima, and always converge to the global optimum $K^*$. This can be viewed as another implication of implicit regularization, in that [eq:exact\_npg] and [eq:exact\_gn] always bias the iterates towards a certain global optimal solution, without getting stuck at spurious local minima.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Global Convergence", "weight": 1.0} -->

The key reason is that, without using the curvature information in $\Delta_K$, these two PO methods can converge to the specific and optimal stationary point such that $E_{K}=0$, instead of any arbitrary stationary point.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Global Convergence", "weight": 1.0} -->

Moreover, in contrast to the results for LQR [fazel2018global], sublinear $O(1/N)$, instead of linear, convergence rate can be obtained so far. This $O(1/N)$ rate of the (iteration average) gradient norm square matches the global convergence rate of gradient descent and second order algorithms to stationary points for general nonconvex optimization, either under the smoothness assumption of the objective [cartis2010complexity,cartis2017worst], or for a class of non-smooth objectives [khamaru2018convergence].

<!-- chunk {"id": "body-0112", "role": "body", "section": "Global Convergence", "weight": 1.0} -->

Our global convergence requires the initial controller to satisfy the $\cH_\infty$-norm robustness constraint, which, as the assumption on the initial controller being stabilizing for LQR [fazel2018global,bu2019LQR], is inherent to PO methods with iterative local search. Complementary to [fazel2018global,bu2019LQR], our iterates not only improve the performance criterion, but also preserve the robustness.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Global Convergence", "weight": 1.0} -->

Though sublinear globally, much faster rates, i.e., (super-)linear rates, can be shown locally around the optimum as below. Proof of the following theorem is deferred to [sec:proof\_theorem:local\_exact\_conv].

<!-- chunk {"id": "body-0114", "role": "body", "section": "Global Convergence", "weight": 1.0} -->

Suppose that the conditions in Theorem [theorem:global\_exact\_conv] hold, and additionally $DD^\top>0$ holds. Then, under the stepsize choices as in Theorem [theorem:global\_exact\_conv], both updates [eq:exact\_npg] and [eq:exact\_gn] converge to the optimal control gain $K^*$ with locally linear rate, in the sense that the objective $\{\cJ(K_n)\}$ defined in [equ:form\_J2] converges to $\cJ(K^*)$ with a linear rate. In addition, if $\eta=1/2$, the Gauss-Newton update [eq:exact\_gn] converges to $K^*$ with a locally Q-quadratic rate.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Global Convergence", "weight": 1.0} -->

Key to the locally linear rates is that the property of gradient dominance [polyak1963gradient,nesterov2006cubic] holds locally around the optimum for mixed design problems. Such a property has been shown to hold globally for LQR problems [fazel2018global], and also hold locally for zero-sum LQ games [zhang2019policy]. The Q-quadratic rate echoes back the rate of Gauss-Newton with $\eta=1/2$ for LQR problems [hewer1971iterative,bu2019LQR]. This globally sublinear and locally (super-)linear convergence resembles the behavior of (Quasi)-Newton methods for nonconvex optimization [nesterov2006cubic,ueda2010convergence], and policy gradient methods for zero-sum LQ games [zhang2019policy].

<!-- chunk {"id": "body-0116", "role": "body", "section": "Global Convergence", "weight": 1.0} -->

Due to the close relationship between mixed design and zero-sum LQ games, see [sec:discussion], one may compare the convergence results and find the rates here (globally sublinear and locally linear) not improved over [zhang2019policy]. However, one key difference is that an extra projection step is required to guarantee the stability of the system in [zhang2019policy], which is essentially to regularize the iterates explicitly. More importantly, such a projection can only be calculated under more restrictive assumptions (see Assumption 2.1 therein), which, though cover a class of LQ games, are not standard in robust control. Here, similar convergence results are established, without projections or non-standard assumptions in robust control, thanks to implicit regularization. Moreover, we have established the local superlinear rate for the Gauss-Newton update, and whole new set of results for the continuous-time setup, which were not studied in [zhang2019policy].

<!-- chunk {"id": "body-0117", "role": "body", "section": "Proofs of Main Results", "weight": 1.0} -->

In this section, we provide detailed proofs for the main results of the paper.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Discussions", "weight": 1.0} -->

We now provide additional discussions on the mixed $\cH_2/\cH_\infty$ control design problem.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Connection to Zero-Sum LQ Games", "weight": 1.0} -->

It is well known that minimizing the risk-sensitive cost as [equ:def\_obj], which is the logarithm of the expected values of exponential functions with quadratic forms, can be equivalent to solving a zero-sum dynamic game, for both general settings [whittle1990risk,fleming1992risk,fleming1997risk], and in particular for LQ settings [jacobson1973optimal]. Due to the connection between LEQG and mixed design, as discussed in [sec:formulation], the latter can be related to a zero-sum LQ game as well. the system that follows linear dynamics The notation in this section might be slightly abused, considering the notations used in the main text, but shall be self-evident by the context. with the system state being $x_t\in\RR^d$, the control inputs of players $1$ and $2$ being $u_t\in\RR^{m_1}$ and $v_t\in\RR^{m_2}$, respectively.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Connection to Zero-Sum LQ Games", "weight": 1.0} -->

The matrices $A,B$, and $D$ all have proper dimensions. The objective of player $1$ (player $2$) is to minimize (maximize) the infinite-horizon value function, where the initial state $x_0\sim \cD$ for some distribution $\cD$, the matrices $Q\in\RR^{d\times d}$, $R^u\in\RR^{m_1\times m_1}$, and $R^v\in\RR^{m_2\times m_2}$ are all positive definite.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Connection to Zero-Sum LQ Games", "weight": 1.0} -->

Value of the game, i.e., the value of [equ:minimax\_def] when the $\inf$ and $\sup$ can interchange, is characterized by $\EE_{x_0\sim\cD}(x_0^\top P^*x_0)$, where $P^*$ is the solution to the generalized algebraic Riccati equation (GARE) [bacsar1995h] Moreover, under the standard assumption that $R^v-D^\top P^*D>0$, the solution policies, i.e., the Nash equilibrium (NE) policies that are stabilizing, of the two players have forms of LTI state-feedback, namely, $u_t^*=-K^*x_t$ and $v_t^*=-L^*x_t$ for some matrices $K^*\in\RR^{m_1\times d}$ and $L^*\in\RR^{m_2\times d}$.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Connection to Zero-Sum LQ Games", "weight": 1.0} -->

The corresponding values of $(K^*,L^*)$ are given by As a consequence, it suffices to search over all stabilizing control gain pairs $(K,L)$ that solves In fact, for any stabilizing $(K,L)$ that makes $\rho(A-BK-DL)<1$, $\cC(K,L)=\tr(P_{K,L}\Sigma_0)$, where $\Sigma_0=\EE_{x_0\sim\cD}(x_0^\top x_0)$, and $P_{K,L}$ is the unique solution to the Lyapunov equation P\_K,L=Q+K^R^u K-L^R^v L+(A-BK-DL)^P\_K,L(A-BK-DL).

<!-- chunk {"id": "body-0123", "role": "body", "section": "Connection to Zero-Sum LQ Games", "weight": 1.0} -->

This condition on $K$ is necessary for finding the equilibrium policy since otherwise, the maximizer can drive the cost to infinity by choosing $L$. See Chapter $3$ of for more discussions.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Connection to Zero-Sum LQ Games", "weight": 1.0} -->

$R^v-D^\top P_{K,L} D>0$, maximizing over $L$ on the RHS of [equ:P\_KL\_Sol] yields P\_K^*=Q+K^R^u K+(A-BK)^[P\_K^*+P\_K^*D(R^v-D^P\_K^*D)^-1D^P\_K^*\_\_K^*](A-BK), where $P_{K}^*=P_{K,L(K)}$ with $L(K)$ being the maximizer that satisfies Notice that [equ:P\_KL\_Sol\_max\_L] is in fact a Riccati equation identical to [equ:discret\_riccati], with $R^v$ replaced by $\gamma^2 I$, $R^u$ replaced by $R$, and $Q$ replaced by $C^\top C$.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Connection to Zero-Sum LQ Games", "weight": 1.0} -->

Hence, the problem [equ:nonconvex\_concave\_def] is equivalent to minimizing $\cC(K,L(K))=\tr(P_K^*\Sigma_0)$, subject to [equ:P\_KL\_Sol\_max\_L], which coincides with the mixed design problem [equ:def\_mixed\_formulation], where $\cJ(K)$ takes the form of [equ:form\_J1] with $DD^\top$ replaced by $\Sigma_0$. Furthermore, the minimizer of the RHS on [equ:P\_KL\_Sol\_max\_L] is which equals the global optimum for the mixed design problems.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Model-Free Algorithms", "weight": 1.0} -->

The connection above provides one angle to develop model-free RL algorithms for solving mixed design problems. Indeed, the natural PG in [eq:exact\_npg] cannot be sampled using trajectory data, due to the form of the matrix $\Delta_K$ in [equ:def\_Delta]. Fortunately, solution of the game [equ:nonconvex\_concave\_def] can be obtained by model-free PG-based methods, see [zhang2019policy], and the more recent work [bu2019global], which, by [equ:Ks\_game\_NE] and Proposition [coro:opt\_control\_form\_discrete], is equivalent to the global optimum of mixed design problems. Hence, model-free algorithms that solve the LQ game [equ:nonconvex\_concave\_def] can also be used to solve the mixed design problem [equ:def\_mixed\_formulation]. the PG of $\cC(K,L)$ w.r.t.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Model-Free Algorithms", "weight": 1.0} -->

$K$ and $L$ can be written as [zhang2019policy] \Sigma\_{K,L}:=\EE\_{x\_0\sim\cD}\sum\_{t=0}^\infty x\_tx\_t^\top$ is the correlation matrix. By by Lemma 3.3 of [zhang2019policy], under certain conditions, the stationary point $(K,L)$ where $\nabla_K \cC(K,L)=0$ and $\nabla_L \cC(K,L)=0$ coincides with the NE.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Model-Free Algorithms", "weight": 1.0} -->

Indeed, $\nabla_L \cC(K,L)=0$ with the invertibility of $\Sigma_{K,L}$ yields the maximizer $L(K)$ in [equ:minimizer\_L\_given\_K], which combined with $\nabla_K \cC(K,L(K))=0$ in [equ:policy\_grad\_K\_form] gives the solution [equ:Ks\_game\_NE].

<!-- chunk {"id": "body-0129", "role": "body", "section": "Model-Free Algorithms", "weight": 1.0} -->

Therefore, it is straightforward to develop PG-based updates to find the minimizer $L(K)$ for some $K$, and then perform PG-based algorithms to update $K$, which can both be implemented in a model-free fashion, using zeroth-order methods [nesterov2017random,fazel2018global]. Note that the PO methods in [zhang2019policy] are essentially also based on this idea, but with the order of $\max$ and $\min$ interchanged, and require a projection step for updating $L$. More recently, [bu2019global] has developed double-loop PO methods that remove this projection.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Model-Free Algorithms", "weight": 1.0} -->

Two examples of PG-based methods can be written as where $\alpha,\eta>0$ are stepsizes, $ \Sigma_{K,L}:=\EE_{x_0\sim\cD}\sum_{t=0}^\infty x_tx_t^\top$ with $u_t=-Kx_t$ and $v_t=-Lx_t$ is the correlation matrix under control pair $(K,L)$, $\widehat{L(K)}$ is the estimate of $L(K)$ obtained by iterating either [equ:model_free_game_PG_L] or [equ:model_free_game_NPG_L], $\widehat{\nabla}_L\cC(K,L)$, $\widehat{\nabla}_K\cC(K,L)$, and $\widehat{\Sigma}_{K,L}$ are the estimates of $\nabla_L\cC(K,L)$,

<!-- chunk {"id": "body-0131", "role": "body", "section": "Model-Free Algorithms", "weight": 1.0} -->

$\nabla_K\cC(K,L)$, and $\Sigma_{K,L}$ using sampled data, respectively.

<!-- chunk {"id": "body-0132", "role": "body", "section": "Model-Free Algorithms", "weight": 1.0} -->

Note that the simulator for the game [equ:nonconvex\_concave\_def] that generates the data samples can be obtained by the simulator for the mixed design problem [equ:def\_mixed\_formulation], with the disturbance $w_t$ modeled as $w_t=-Lx_t$. This way, the updates of $L$ in [equ:model\_free\_game\_PG\_L] and [equ:model\_free\_game\_NPG\_L] can be understood as improving the disturbance to find the worst-case one, which manifests the idea of $\cH_\infty$ norm. Also, [bu2019global] has verified that in zero-sum LQ games, given a fixed $K$, such an update of $L$ converges to the best-response disturbance $L(K)$ given in [equ:minimizer\_L\_given\_K].

<!-- chunk {"id": "body-0133", "role": "body", "section": "Model-Free Algorithms", "weight": 1.0} -->

This justifies the feasibility of our algorithms [equ:model\_free\_game\_PG\_L]-[equ:model\_free\_game\_NPG\_K].

<!-- chunk {"id": "body-0134", "role": "body", "section": "Model-Free Algorithms", "weight": 1.0} -->

In addition, by the form of the policy gradients for the game, see Lemma 3.2 in [zhang2019policy], the exact natural PG update on the LHS of [equ:model\_free\_game\_NPG\_K] is identical to that for mixed design problems in [eq:exact\_npg]. In other words, the natural PG update [eq:exact\_npg] can be implemented in a model-free way by virtue of that outer-loop update of $K$ in a zero-sum LQ game. As shown in [bu2019global], such an outer-loop update over $K$ converges to the NE of the game. Details of the model-free algorithms are deferred to Algorithms [alg:est\_grad\_corre], [alg:model\_free\_inner\_NPG], and [alg:model\_free\_outer\_NPG] in [sec:pseudo\_code].

<!-- chunk {"id": "body-0135", "role": "body", "section": "Simulations", "weight": 1.0} -->

In this section, we present some simulation results to corroborate our theory. We mainly focus on the convergence properties for the discrete-time settings. We have also included extensive numerical comparisons with existing packages for solving $\cH_2/\cH_\infty$ mixed design, which can only handle the continuous-time settings [arzelier2011h2,mahmoud1996h]. The problem setup, PO algorithms, and their analyses, for the continuous-time settings can be found in [sec:aux\_cont\_res]. We show that our PO methods outperform these existing packages in many aspects, though the latter ones can handle more general setups.

<!-- chunk {"id": "body-0136", "role": "body", "section": "Implicit Regularization & Global/Local Convergence", "weight": 1.0} -->

Convergence of the gradient norm square $\|E_{K}\|_F^2$ and the objective $\{\cJ(K)\}$, behaviors of the $\cH_\infty$-norm $\|\cT(K)\|_\infty$, and the smallest eigenvalue of $\gamma^2 I-D^\top P_K D$, for PG, NPG, and Gauss-Newtons with stepsizes $1\times 10^{-7}$, $1\times 10^{-4}$, $0.01$, and $0.5$, respectively.

<!-- chunk {"id": "body-0137", "role": "body", "section": "Implicit Regularization & Global/Local Convergence", "weight": 1.0} -->

Linear, linear and super-linear convergence rates for the NPG update with $\eta = 10^{-4}$, the GN update with $\eta = 10^{-2}$, and the GN update with $\eta = 0.5$, respectively.

<!-- chunk {"id": "body-0138", "role": "body", "section": "Implicit Regularization & Global/Local Convergence", "weight": 1.0} -->

We first consider the following example, denoted by Case 1, whose parameters are: and $DD^\top= I$. Note that all matrices $C^\top C$, $E^\top E$, and $DD^\top$ are positive definite. This $DD^\top$ satisfies both the controllability assumption in Proposition [coro:opt\_control\_form\_discrete], and the assumption $DD^\top>0$ in Theorem [theorem:local\_exact\_conv]. We first randomly generate $K_0$ with each element uniformly generated from $[-0.25,0.25]$, such that $K_0$ is stabilizing (i.e., $\rho(A-BK_0)<1$). Then, the $\cH_\infty$-norm $\|\cT(K_0)\|_\infty$ under $K_0$ is calculated.

<!-- chunk {"id": "body-0139", "role": "body", "section": "Implicit Regularization & Global/Local Convergence", "weight": 1.0} -->

The value of $\gamma$ is then chosen as $1.00001\cdot \|\cT(K_0)\|_\infty$, making sure that $K_0\in\cK$. We then perform all three algorithms [eq:exact\_pg]-[eq:exact\_gn] in [sec:PO\_alg] on the above problem setting, and illustrate the convergence of both the gradient norm square $\|E_{K}\|_F^2$, and the objective difference $\{\cJ(K_n)-\cJ(K^*)\}$. The stepsizes $\eta$ for the PG, NPG, and Gauss-Newton updates are $1\times 10^{-7}$, $1\times 10^{-4}$, and $0.01$, respectively. We have also used $\eta=1/2$ for the Gauss-Newton update.

<!-- chunk {"id": "body-0140", "role": "body", "section": "Implicit Regularization & Global/Local Convergence", "weight": 1.0} -->

As shown in Figure [fig:conv\_main\_result\_Case\_2], for both performance criteria, all four update rules converge successfully. At the beginning of the iterations, NPG and Gauss-Newton with $\eta=10^{-2}$ indeed yield sublinear convergence of the gradient norm square; as the iterations proceed, linear convergence rate appears. Moreover, for Gauss-Newton with $\eta=1/2$, super-linear convergence rate has also been observed. These observations corroborate our theory in both Theorems [theorem:global\_exact\_conv] and [theorem:local\_exact\_conv].

<!-- chunk {"id": "body-0141", "role": "body", "section": "Implicit Regularization & Global/Local Convergence", "weight": 1.0} -->

Moreover, we have also illustrated the behaviors of the $\cH_\infty$-norm $\|\cT(K)\|_\infty$ and the smallest eigenvalue of $\gamma^2 I-D^\top P_K D$, denoted by $\lambda_{\min}(\gamma^2 I-D^\top P_K D)$, in Figure [fig:conv\_main\_result\_Case\_2]. It is seen that along the iterations, with the stepsizes that guarantee convergence, the $\cH_\infty$-norm is below the bound $\gamma=15.45$ for all four update rules, which validates the implicit regularization result we have in Theorem [thm:stability\_update]. As another evidence for implicit regularization in accordance to Lemma [lemma:discrete\_bounded\_real\_lemma], it is shown that the matrix $\gamma^2 I-D^\top P_K D>0$ along iterations.

<!-- chunk {"id": "body-0142", "role": "body", "section": "Implicit Regularization & Global/Local Convergence", "weight": 1.0} -->

Notice that the initialization $K_0$ is very close to the boundary, as $\gamma=1.00001\cdot \|\cT(K_0)\|_\infty$. It is shown that the vanilla PG update, even though with infinitesimal stepsize ($10^{-7}$), still violates the $\cH_\infty$-norm constraint and fails to converge. We do observe, however, in several other numerical examples, that vanilla PG update converges successfully. It is thus not clear whether there exists a constant stepsize choice for the global convergence and robustness perservationof the vanilla PG iterates, which is left for future investigation.

<!-- chunk {"id": "body-0143", "role": "body", "section": "Implicit Regularization & Global/Local Convergence", "weight": 1.0} -->

To further verify our local convergence rates, we have also initialized our algorithms by randomly searching over $\RR^{3\times 3}$ to find a $K_0\in\cK$ such that $\|K_0-K^*\|_F \leq 0.3$. The convergence patterns are presented in Figure [fig:local], which clearly demonstrates the faster local rates.

<!-- chunk {"id": "body-0144", "role": "body", "section": "Escaping Suboptimal Stationary Points", "weight": 1.0} -->

Convergence of the NPG and GN updates to $K^*$, when there exists an infinite number of stationary points (i.e. $K$ s.t. $\nabla\cJ(K) = 0$). The stepsizes for the PG, NPG, and GN updates are $10^{-3}$, $10^{-2}$, and $0.5$, respectively.

<!-- chunk {"id": "body-0145", "role": "body", "section": "Escaping Suboptimal Stationary Points", "weight": 1.0} -->

We also investigate the setting where the controllability assumption in Proposition [coro:opt\_control\_form\_discrete], and the assumption $DD^\top>0$ in Theorem [theorem:local\_exact\_conv] do not hold. In this case, there might exist multiple stationary points, many of which are suboptimal.

<!-- chunk {"id": "body-0146", "role": "body", "section": "Escaping Suboptimal Stationary Points", "weight": 1.0} -->

Specifically, consider the following problem parameter, which is denoted by A = \begin{bmatrix} 2 & 0\\ 0 & 0\end{bmatrix}, \quad B = D = \begin{bmatrix} 1 & 0\\ 0 & 0\end{bmatrix}, \quad C = \begin{bmatrix} 0 & 0\\ 0 & 0 \\ 1 & 2\end{bmatrix}, \quad E =\begin{bmatrix} 1 & 0\\ 0 & 1 \\ 0 & 0\end{bmatrix}, \quad \begin{bmatrix} C^{\top} \\ E^{\top} \end{bmatrix}\cdot\begin{bmatrix} C & E \end{bmatrix} = \begin{bmatrix} Q & \bm{0}_{2\times 2} \\ \bm{0}_{2\times 2} & R\end{bmatrix}.

<!-- chunk {"id": "body-0147", "role": "body", "section": "Escaping Suboptimal Stationary Points", "weight": 1.0} -->

Note that the system is open-loop unstable, as $\rho(A)>1$. We choose $\gamma = 10$. Then, one can verify that the above mixed design problem admits an optimum $K^* =(R+B^\top \tP_{K^*} B)^{-1}B^\top \tP_{K^*} A= \begin{bmatrix}1.6186 & 0 \\ 0 & 0\end{bmatrix}$. Moreover, there exist an infinite number of stationary points, which share the form of $K=\begin{bmatrix}1.6186 & 0 \\ 0 & c\end{bmatrix}$ for any $c\in \RR$, and make $\nabla\cJ(K) = 0$. Despite this, following Theorem [theorem:global\_exact\_conv], the NPG and GN updates provably converge to $K^*$, which automatically escape other suboptimal stationary points.

<!-- chunk {"id": "body-0148", "role": "body", "section": "Escaping Suboptimal Stationary Points", "weight": 1.0} -->

We numerically evaluate the convergence to $K^*$ in Figure [fig:star], for both the NPG and GN updates. For each of the 50 trails, we fix a random seed and initialize the algorithm by randomly searching a $K_0 \in \RR^{2\times 2}$ that satisfies $K_0 \in \cK$. It can be observed that two PG methods converge to $K^*$in all trails. In start contrast, the vanilla PG update can easily get stuck at these suboptimal stationary points, depending on its initialization.

<!-- chunk {"id": "body-0149", "role": "body", "section": "Escaping Suboptimal Stationary Points", "weight": 1.0} -->

This can be understood as another meaning of implicit regularization: for this specific nonconvex problem, two certain search directions automatically bias the iterates to avoid bad local minima, and always towards the global optimal one.

<!-- chunk {"id": "body-0150", "role": "body", "section": "Comparison with Existing $\\cH_2/\\cH_\\infty$ Control Solvers", "weight": 1.0} -->

To better justify the superiority of our PO methods, we numerically compare their convergence properties with other numerical $\cH_2/\cH_\infty$ mixed control design packages, including the HIFOO method [arzelier2011h2] and the h2hinfsyn method implemented in Matlab [mahmoud1996h], which is based on linear matrix inequalities. Note that these full-fledged packages can only handle continuous-time settings. To make the comparison fair, we also implement our PO methods for the continuous-time settings as studied in [sec:aux\_cont\_res].

<!-- chunk {"id": "body-0151", "role": "body", "section": "Comparison with Existing $\\cH_2/\\cH_\\infty$ Control Solvers", "weight": 1.0} -->

We mainly compare them in terms of: 1) the $\cH_2$ and $\cH_\infty$ norms of the controller that the algorithms converge to; 2) the computation complexity (runtime); 3) the $\cH_\infty$-norm constraint violation. We will validate that our PO methods indeed outperform HIFOO in these aspects. The larger-scale the dynamical system is, the more pronounced our advantages are, with provable robustness preserving guarantees.

<!-- chunk {"id": "body-0152", "role": "body", "section": "Comparison with Existing $\\cH_2/\\cH_\\infty$ Control Solvers", "weight": 1.0} -->

Simulation Setup. All the experiments are executed on a MacBook Pro 2019 with a 2.8 GHz Quad-Core Intel Core i7 processor with Matlab R2020b. The device also has a 16GB 2133MHz LPDDR3 memory and an Intel Iris Plus 655 Graphics. To make the runtime comparison fair (or even in favor of HIFOO), we set the following parameters of HIFOO (version 3.501 with Hanso version 2.01): options.fast $=1$ for using a fast optimization method; options.prtlevel $=0$ to suppress unnecessary printing statements. Other parameters of HIFOO are set to be default. For Matlab's h2hinfsyn function, tol has been set to $10^{-6}$.For our PO methods, we set the stepsizes of the NPG and GN updates to be $1/(2\|R\|)$ and $1/2$, respectively, and solve the following mixed design problems Cases 3-6 until $\cJ(K) - \cJ(K^*) < 10^{-6}$.

<!-- chunk {"id": "body-0153", "role": "body", "section": "Comparison with Existing $\\cH_2/\\cH_\\infty$ Control Solvers", "weight": 1.0} -->

We first consider a simple setting, denoted by Case 3. The time-invariant system dynamics are characterized by $\dot{x} = Ax+Bu+Dw$, $z = Cx+Eu$, where &A = \begin{bmatrix} 1 & 0 & -10\\ -1 &1 &0\\ 0 &0 &1\end{bmatrix}, \quad B = \begin{bmatrix} 1 & -10 & 0\\ 0 & 1 &0\\ -1 &0 &1\end{bmatrix}, \quad &\qquad\quad~~ D = \begin{bmatrix} 0.5 & 0 & 0\\ 0 & 0.5 &0\\ 0 &0 &0.5\end{bmatrix}, \quad E = \begin{bmatrix} 1 & 0 & 0\\ 0 &1 &0\\ 0 &0 &1 \\ 0 & 0 & 0\end{bmatrix}.

<!-- chunk {"id": "body-0154", "role": "body", "section": "Comparison with Existing $\\cH_2/\\cH_\\infty$ Control Solvers", "weight": 1.0} -->

One can verify that $E^{\top}[C \ E] = [{0}, \ {I}]$, satisfying our assumption. Then, we solve The simulations are run over 100 trails with the random seed being fixed at $1, \cdots, 100$, respectively. The optimal (minimax) disturbance attenuation level of Case 3 is $\gamma^* \approx 0.53$, as computed/verified both by Matlab's hinfsyn function and HIFOO's hifoo(P, 'h') function.

<!-- chunk {"id": "body-0155", "role": "body", "section": "Comparison with Existing $\\cH_2/\\cH_\\infty$ Control Solvers", "weight": 1.0} -->

- (PO methods achieve lower $\cH_2$ and $\cH_\infty$ norms, faster). When $\gamma = 5$, both HIFOO and PO methods preserve the $\|\cT(K)\|_{\infty} < \gamma$ constraint during the optimization process, and output some convergent gain matrix $K$. However, HIFOO converges to a local minimum due to that it is directly optimizing the $\cH_2$ norm of the closed-loop transfer function, and the landscape for such an optimization problem is unclear. In contrast, our PO methods, by definition, optimize an upper bound of the $\cH_2$-norm, and as proved theoretically, converge to the global minimum of the problem. The solution yields lower values for $\|\cT(K)\|_{2}$ and $\|\cT(K)\|_{\infty}$ compared to those of the HIFOO output.

<!-- chunk {"id": "body-0156", "role": "body", "section": "Comparison with Existing $\\cH_2/\\cH_\\infty$ Control Solvers", "weight": 1.0} -->

Indeed, this shows that minimizing the $\cH_2$-norm upper bound as in [bernstein1989lqg,mustafa1991lqg] and our paper can obtain reasonably good solutions. More importantly, the average runtimes of our PG methods average over 100 trails are around $5.93\times$ faster than HIFOO. - (PO methods always preserve $\cH_\infty$-norm constraint). When $\gamma = 3$ (which is still far from $\gamma^* \approx 0.53$), our methods consistently preserve the $\|\cT(K)\|_{\infty} < \gamma$ constraint during the optimization process, validating our theoretical findings. However, the HIFOO iterates have reached $\|\cT(K)\|_{\infty} = 3.4353>3$ along the way.

<!-- chunk {"id": "body-0157", "role": "body", "section": "Comparison with Existing $\\cH_2/\\cH_\\infty$ Control Solvers", "weight": 1.0} -->

Further, PO methods also find solutions that have lower $\|\cT(K)\|_{2}$ and $\|\cT(K)\|_{\infty}$ norms, with a $5.85\times$ faster runtime. - (Smaller $\gamma$ leads to worse performance for HIFOO). When $\gamma = 1$, our PO methods still preserve the $\|\cT(K)\|_{\infty} < \gamma$ constraint during the optimization process. Our PO methods also converge to the optimum point with both small $\cH_2$ and $\cH_\infty$ norms, while HIFOO's performance is degraded much more. We remark that in this case, the runtime of our methods is longer than that of HIFOO, however, the time was mostly consumed in finding the initialization that is robustly stable, by randomly generating $K_0$ in a certain region. This becomes harder to find for a smaller $\gamma$.

<!-- chunk {"id": "body-0158", "role": "body", "section": "Comparison with Existing $\\cH_2/\\cH_\\infty$ Control Solvers", "weight": 1.0} -->

Our simple initialization method takes more than 90% of the time, which might be less efficient than the advanced initialization technique used in HIFOO.

<!-- chunk {"id": "body-0159", "role": "body", "section": "Comparison with Existing $\\cH_2/\\cH_\\infty$ Control Solvers", "weight": 1.0} -->

| Case 3 w/ $\gamma = 5$ | HIFOO | NPG | GN | $\|\cT(K)\|_2$ Diff. | $\|\cT(K)\|_{\infty}$ Diff. | Speedup | | Case 3 w/ $\gamma = 3$ | HIFOO | NPG | GN | $\|\cT(K)\|_2$ Diff. | $\|\cT(K)\|_{\infty}$ Diff. | Speedup | | Case 3 w/ $\gamma = 1$ | HIFOO | NPG | GN | $\|\cT(K)\|_2$ Diff. | $\|\cT(K)\|_{\infty}$ Diff. | Speedup | Comparison average over 100 trails between HIFOO and two proposed PO methods, for solving the mixed design Case 3. All three methods initialize $K_0$ on their own.

<!-- chunk {"id": "body-0160", "role": "body", "section": "Comparison with Existing $\\cH_2/\\cH_\\infty$ Control Solvers", "weight": 1.0} -->

For two PO methods, a $K_0 \in \cK$ is found by randomly search over $^{3\times 3}$, which takes up $>90\%$ of the total runtime. In contrast, HIFOO uses an in-house method to find initial points. $\|\cT(K)\|_2$ Diff. and $\|\cT(K)\|_\infty$ Diff. represent the difference of $\cH_2$ and $\cH_\infty$ norms achieved by HIFOO and our PO methods (which are identical for NPG and GN, as our methods have guarantees for finding the global optimum of our mixed design problem).

<!-- chunk {"id": "body-0161", "role": "body", "section": "Comparison with Existing $\\cH_2/\\cH_\\infty$ Control Solvers", "weight": 1.0} -->

Regarding the comparison with the present the results in Table [matlab\_comparison]. It is shown that in this simple $3\times 3$ problem, h2hinfsyn and our PG methods converge to nearly the same solution, while our computation time is around $4\times$ faster. Next, we will show that $\texttt{h2hinfsyn}$ scales poorly with respect to the problem dimensions, while our PO methods converge efficiently in high-dimensional problems.

<!-- chunk {"id": "body-0162", "role": "body", "section": "Comparison with Existing $\\cH_2/\\cH_\\infty$ Control Solvers", "weight": 1.0} -->

| Case 3 w/ $\gamma = 5$ | Matlab | NPG | GN | Speedup | | Case 3 w/ $\gamma = 3$ | Matlab | NPG | GN | Speedup | | Case 3 w/ $\gamma = 1$ | Matlab | NPG | GN | Speedup | Comparison average over 100 trails between Matlab's h2hinfsyn and two proposed PO methods, for solving the mixed design Case 3. For the two PO methods, a $K_0 \in \cK$ is found by randomly search over $^{3\times 3}$, and the computation time for finding such an initial point is not taken into account for fair comparison. In contrast, h2hinfsyn implements a LMI-based synthesis procedure.

<!-- chunk {"id": "body-0163", "role": "body", "section": "Comparison with Existing $\\cH_2/\\cH_\\infty$ Control Solvers", "weight": 1.0} -->

More Challenging Cases. We test some more challenging cases with higher dimensions to further demonstrate the efficiency of our PO methods. In Cases 4-6, the dimensions of the control gain matrices are $15 \times 15, 60\times 60, 90\times 90$, respectively, corresponding to the number of decision variables being $225$, $3600$, $8100$, respectively. Problem parameters are too long to enumerate here, and are provided at together with all the code and data.

<!-- chunk {"id": "body-0164", "role": "body", "section": "Comparison with Existing $\\cH_2/\\cH_\\infty$ Control Solvers", "weight": 1.0} -->

The simulations are run over 10 trails with fixed random seeds. Both HIFOO, h2hinfsyn, and our PO methods converge to almost the same control gain matrices in these cases, without constraint violation. This again implies that minimizing the $\cH_2$-norm upper bound (instead of $\cH_2$-norm directly) can usually achieve quite competitive solutions. Notably, our PO methods are around $8\times$, $47 \times$, $295\times$ faster than HIFOO, respectively, in Cases 4-6, as reported in Table [table2]. Our PO methods are also much faster than h2hinfsyn, as it can hardly solve Cases 5-6 and fails to return a solution even after very long runtime.. This verifies that our PO algorithms indeed enjoy better scalability, and the higher the dimension is, the more pronounced our advantage is. These observations have justified that our PO methods are not only theoretically sound, but also numerically competitive.

<!-- chunk {"id": "body-0165", "role": "body", "section": "Comparison with Existing $\\cH_2/\\cH_\\infty$ Control Solvers", "weight": 1.0} -->

| Average runtime | 1c|HIFOO | 1c|Matlab | 1c|NPG | 1c|GN | Speedup | Average runtime comparison over 10 trails between HIFOO, Matlab's h2hinfsyn function, and two proposed PO methods for solving Cases 4-6. The speedup times outside and inside the parenthesis denote the ones of our PO methods compared to HIFOO and Matlab, respectively.

<!-- chunk {"id": "body-0166", "role": "body", "section": "Comparison with Existing $\\cH_2/\\cH_\\infty$ Control Solvers", "weight": 1.0} -->

| Average $\|\cT(K)\|_2$ reached w/ $K_0 = \bm{0}$ | 1c|HIFOO | 1c|Matlab | 1c|NPG | 1c|GN | Average $\|\cT(K)\|_2$ reached over 10 trails between HIFOO, Matlab's h2hinfsyn function, and two proposed PO methods for solving Cases 4-6.

<!-- chunk {"id": "body-0167", "role": "body", "section": "Comparison with Existing $\\cH_2/\\cH_\\infty$ Control Solvers", "weight": 1.0} -->

| Average $\|\cT(K)\|_{\infty}$ reached w/ $K_0 = \bm{0}$ | 1c|HIFOO | 1c|Matlab | 1c|NPG | 1c|GN | Average $\|\cT(K)\|_{\infty}$ reached over 10 trails between HIFOO, Matlab's h2hinfsyn function, and two proposed PO methods for solving Cases 4-6.

<!-- chunk {"id": "body-0168", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

In this paper, we have investigated the convergence theory of policy optimization methods for $\cH_2$ linear control with $\cH_\infty$-norm robustness guarantees. Viewed as a constrained nonconvex optimization, this problem was addressed by PO methods with provable convergence to the global optimal policy. More importantly, we showed that the proposed PO methods enjoy the implicit regularization property, despite the lack of coercivity of the cost function. We expect the present work to serve as an initial step toward further understanding of RL algorithms on robust/risk-sensitive control tasks. We conclude this main part of the paper with several ongoing/potential research directions.

<!-- chunk {"id": "body-0169", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

Implicit regularization of other PO methods: It is of particular interests to investigate whether other PO methods enjoy similar implicit regularization properties. One important example that has not been analyzed in this paper is the PG method. Notice that the model-free implementation of the PG method, see update [eq:exact\_pg], does not require the connection between mixed design and zero-sum LQ games, as the gradient can be sampled via zeroth-order methods directly. Among other examples are quasi-Newton methods with pre-conditioning matrices other than that in [eq:exact\_gn], accelerated PG using the idea from [nesterov1983method], and variance reduced PG methods [papini2018stochastic,xu2019improved].

<!-- chunk {"id": "body-0170", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

Linear quadratic games: Thanks to the connection discussed in [subsec:connection\_to\_games], our LMI-based techniques for showing implicit regularization in Theorem [thm:stability\_update] may be of independent interest to improve the convergence of nested policy gradient methods in [zhang2019policy], and even simultaneously-moving policy-gradient methods, for solving zero-sum LQ games using PO methods. This will place PO methods for multi-agent RL (MARL) under a more solid theoretical footing, as LQ games have served as a significant benchmark for MARL [chasnov2019convergence,mazumdar2019policy]. Rigorous analysis for this setting have been partially addressed in our ongoing work, and in a more recent work [bu2019global].

<!-- chunk {"id": "body-0171", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

Model-based v.s. model-free methods for robust control: There is an increasing literature in model-based learning-based control with robustness concerns [aswani2013provably,berkenkamp2015safe,berkenkamp2017safe,dean2017sample,dean2019safely]. On the other hand, our work serves as an intermediate step toward establishing the sample complexity of model-free PO methods for this setting. Hence, it is natural and interesting to compare the data efficiency (sample complexity) and computational scalability of the two lines of work. Note that such a comparison has been made in [tu2018gap]for LQR problems without addressing the issue of robustness.

<!-- chunk {"id": "body-0172", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

Beyond LTI systems and state-feedback controllers: It is possible to extend our analysis to the mixed $\cH_2/\cH_\infty$ control of other types of dynamical systems such as periodic systems [bittanti1996analysis], Markov jump linear systems [costa2006discrete], and switching systems [liberzon2003switching]. These more general system models are widely adopted in control applications, and extensions to these cases will significantly expand the utility of our theory. On the other hand, it is interesting while challenging to study PO for output-feedback mixed design, where a dynamic controller parameterized by $(A_K,B_K,C_K,D_K)$ is synthesized [apkarian2008mixed]. This way, the PO landscape depends on the order of the parameterization, making the analysis more involved.

<!-- chunk {"id": "body-0173", "role": "body", "section": "Concluding Remarks", "weight": 1.0} -->

PO landscape and algorithms for $\cH_\infty$ control synthesis: Our algorithms are based on the condition that an initial policy satisfying the specified $\cH_\infty$-norm constraint is available. To efficiently find such an initialization, it is natural to study the PO landscape of $\cH_\infty$ control synthesis [doyle1988state,gahinet1994linear,apkarian2006nonsmooth], where the goal is to find the controller that not only satisfies certain $\cH_\infty$-norm bound, but also minimizes it. It seems that the cost function for $\cH_\infty$ control is still coercive. However, the main challenge of PO for $\cH_\infty$ control is that the cost function is non-smooth [apkarian2006nonsmooth], which necessitates the use of subgradient methods. The LMI arguments developed here may shed new lights on the convergence analysis of these methods.
