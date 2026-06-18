## Introduction

Performance and robustness are two central objectives in control design: $\mathcal{H}_{2}$ control optimizes average performance, whereas $\mathcal{H}_{\infty}$ control guarantees safety against worst-case scenarios. Mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control provides a principled framework to balance the two, leading to a variety of formulations studied across decades. A particularly influential formulation designs a stabilizing controller that minimizes an $\mathcal{H}_{2}$ cost bound subject to an $\mathcal{H}_{\infty}$ constraint. Classical solutions based on coupled Riccati equations or linear matrix inequalities (LMIs) are well established, but they provide little understanding of the underlying optimization landscape. Moreover, these methods are inherently model-based and scale poorly with system dimension, limiting their applicability in large-scale or data-driven settings.

In contrast, policy optimization has emerged as a promising alternative for controller design, inspired by the success of reinforcement learning in sequential decision-making and continuous control tasks. Despite the nonconvexity of policy spaces, recent studies have revealed benign landscapes in various control problems such as stabilization, linear quadratic regulation (LQR), linear quadratic Gaussian (LQG) \[39 control"), 48 control"), 7\], and dynamic filtering. For these control problems, stationary points can be globally optimal, and gradient-based methods can achieve global convergence under mild assumptions.

A key insight behind these benign landscape results is that many nonconvex control problems can be reformulated as convex ones via appropriate changes of variables. In particular, LMI-based synthesis methods, despite involving auxiliary Lyapunov variables, provide a lens for analyzing the geometry of policy optimization \[37, 30, 39 control"), 13, 42, 16\]. This perspective has been formalized in the Extended Convex Lifting ($\mathtt{E}\mathtt{C}\mathtt{L}$) framework, which systematically bridges classical convex reformulations and modern nonconvex policy optimization. The $\mathtt{E}\mathtt{C}\mathtt{L}$ framework is broadly applicable, encompassing state-feedback and output-feedback $\mathcal{H}_{2}$ and $\mathcal{H}_{\infty}$ control as well as distributed control.

In this work, we revisit the classical mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control design from a modern policy optimization perspective. Building on the classical formulations of, we analyze both the general two-channel case and its single-channel specialization, and provide a systematic study of the associated nonconvex optimization landscapes. Our results reveal hidden convexity and establish the absence of spurious stationary points. Beyond new theoretical insights into nonconvex optimization in modern control, these results will facilitate the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design in large-scale and/or model-free data-driven settings.

### Our contributions

This paper presents a systematic study of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ state-feedback control through the lens of modern nonconvex optimization. Technically, our main contributions are:

Basic landscape properties. We analyze the geometry of the nonconvex feasible set. It is known that this set is open and path-connected (Lemma 2). We further precisely characterize its boundary as the set of policies that exactly saturate the $\mathcal{H}_{\infty}$ constraint (Theorem 1 and Corollary 1). We also examine the landscape of the mixed cost function. This cost function is real analytic in the interior, and continuous on the closure of its domain (Theorem 2 and Lemma 3). Thus, the mixed cost function is smooth, and we provide its explicit gradient formulas (Lemmas 4 and 5). These results underpin our analysis of stationarity, global optimality, and solvability of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control.

Global optimality of stationary points. We investigate the global optimality of the two-channel mixed control. This includes the single-channel setting in as a special case. Despite its nonconvexity, we establish that no spurious stationary points exist (Theorem 3). This property, along with the gradient expressions, recovers the classical optimality conditions (Corollaries 2 and 3). We further analyze existence and uniqueness, showing that the single-channel case always admits a unique stationary point (Theorem 4.5), whereas the two-channel case may not (Fact 1). Nevertheless, we prove that a stationary point exists when the robustness constraint is sufficiently relaxed (Theorem 4.4).

Analysis techniques via $\mathtt{E}\mathtt{C}\mathtt{L}$. We explicitly construct an extended convex lifting ($\mathtt{E}\mathtt{C}\mathtt{L}$) for the two-channel mixed control (Theorem 5.13). While relying on classical LMI techniques, our convex lifting construction is non-trivial since we need to employ non-strict Riccati inequalities and LMIs, in contrast to classical suboptimal controller synthesis based on strict inequalities. This key distinction enables the $\mathtt{E}\mathtt{C}\mathtt{L}$ framework to certify the global optimality of stationary points over the entire feasible set. Moreover, the resulting convex reformulation (Theorem 5.16) not only preserves the optimal value of the original nonconvex problem, but also guarantees solvability when incorporating boundary policies (Proposition 5.17).

### Related work

Mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control. The study of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control dates back to the seminal works of, which formulated the problem of minimizing an $\mathcal{H}_{2}$ cost bound subject to an $\mathcal{H}_{\infty}$ constraint. Solvability of this formulation was first established in via coupled Riccati equations, and later proposed a more tractable approach for suboptimal controller synthesis. A special case was later shown in to coincide with the maximum entropy $\mathcal{H}_{\infty}$ control. A Nash game formulation was also developed , framing the mixed design as a two-player game with the optimal controller characterized by coupled Riccati equations. Beyond analytical methods, a non-smooth optimization approach was proposed , ensuring convergence to a stationary point controller via a proximity control algorithm. Furthermore, LMI-based methods have also been developed , providing numerical solutions through semidefinite programming. More recently, studied policy gradient methods for the single-channel case, showing that the iterates implicitly preserve the $\mathcal{H}_{\infty}$ constraint throughout optimization and converge to globally optimal policies. Although their analysis proves global optimality of stationary points, it applies only to a special single-channel case of the broader formulation , and relies on a game-theoretic argument that may be less accessible to those unfamiliar with dynamic game theory.

Policy optimization in control. Recent years have seen growing interest in direct policy search for controlling dynamical systems. For classical LQR, the cost is coercive and gradient dominant, yielding global convergence of policy gradient methods. Similar benign landscapes have been established for Markovian jump LQR, distributed LQR, LQ games, and mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design. For nonsmooth $\mathcal{H}_{\infty}$ optimization, global convergence is established for state feedback, and convergence to Goldstein stationary points is shown for static output feedback. Partial observation and dynamic output feedback introduce more intricate landscapes: in LQG, controllable and observable stationary points are globally optimal though saddle points may exist \[40 control"), 49\], motivating saddle-escaping \[48 control")\] and Riemannian gradient methods. For dynamic output feedback $\mathcal{H}_{\infty}$, stabilizing controllers are nonconvex and may form a disconnected set, but all nondegenerate Clarke stationary points are globally optimal. We refer to for two recent surveys.

Convex lifting for nonconvex control. A growing line of work has leveraged convex reformulations to analyze nonconvex control landscapes \[30, 44, 37, 13, 42, 39 control")\]. Many classical control problems admit LMI-based reformulations, which explain the benign geometry observed in policy optimization. For example, convex reparameterizations yield global convergence in continuous-time LQR, and certify global optimality of Clarke stationary points in discrete-time $\mathcal{H}_{\infty}$ control. Extensions to output feedback settings include convex lifting strategy for dynamic estimation and global optimality results for $\mathcal{H}_{\infty}$ control \[40 control")\]. Most recently, the $\mathtt{E}\mathtt{C}\mathtt{L}$ framework unifies these perspectives, accommodating static and dynamic policies, smooth and nonsmooth costs, and distinguishing degenerate from nondegenerate policies based on non-strict LMIs.

### Paper outline

The rest of this paper is organized as follows. Section 2 formulates the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ policy optimization. Section 3 examines the geometry of the feasible set and the structural properties of the cost function. Section 4 establishes our main global optimality result, along with characterizations of optimality conditions and the existence and uniqueness of stationary points. Section 5 presents the $\mathtt{E}\mathtt{C}\mathtt{L}$ framework underlying our analysis and develops a tailored $\mathtt{E}\mathtt{C}\mathtt{L}$ for mixed control. Section 6 reports numerical results, and Section 7 concludes the paper. Technical proofs are provided in the appendices.

Notations. We denote the set of $k \times k$ real symmetric matrices by ${\mathbb{S}}^{k}$. For ${M_{1},M_{2}} \in {\mathbb{S}}^{k}$, we write $M_{1} \prec {{( \preceq )}M_{2}}$ and $M_{2} \succ {{( \succeq )}M_{1}}$ if $M_{2} - M_{1}$ is positive (semi)definite. The Frobenius norm for matrices is denoted by $\parallel \cdot \parallel$. We use $I_{n}$ and $0_{m \times n}$ for the $n \times n$ identity and $m \times n$ zero matrices, respectively, omitting their subscripts when clear. For a subset $S$ of a topological space, ${int}{(S)}$ denote its interior and ${cl}{(S)}$ its closure.

## Preliminaries

This section introduces the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control problem and presents our problem statement.

### System dynamics and robustness

Consider the continuous-time linear dynamical system

where ${x{(t)}} \in {\mathbb{R}}^{n}$ is the state, ${u{(t)}} \in {\mathbb{R}}^{m}$ is the control input, ${w{(t)}} \in {\mathbb{R}}^{n}$ is the disturbance. We focus on static state feedback policies of the form ${u{(t)}} = {Kx{(t)}}$, where $K \in {\mathbb{R}}^{m \times n}$. The set of stabilizing policies is defined as

We henceforth denote $A_{K}:={A + {BK}}$ and $W:={B_{w}B_{w}^{\mathsf{T}}}$.

In standard LQR, the disturbance $w{(t)}$ is modeled as zero-mean white Gaussian noise with identity covariance, i.e., ${{\mathbb{E}}{\lbrack{w{(t)}w{(\tau)}}\rbrack}} = {\delta{({t - \tau})}I_{n}}$. The objective is to find a stabilizing policy $K \in \mathcal{K}$ that minimizes the averaged cost ${\lim_{T\rightarrow\infty}{{\mathbb{E}}\left\lbrack {{\frac{1}{T}{\int_{0}^{T}{x{(t)}^{\mathsf{T}}Q_{2}x{(t)}}}} + {u{(t)}^{\mathsf{T}}R_{2}u{(t)}dt}} \right\rbrack}},$ where $Q_{2} \succeq 0$ and $R_{2} \succ 0$ are performance weight matrices. It is known that LQR can be equivalently cast as $\mathcal{H}_{2}$ optimal control: $\min_{K \in \mathcal{K}}{\|{\mathbf{T}_{2}{(K)}}\|}_{\mathcal{H}_{2}}^{2}$, where $z_{2}$ defines the $\mathcal{H}_{2}$ performance output and $\mathbf{T}_{2}{(K)}$ denotes the transfer function from $w$ to $z_{2}$ as follows

On the other hand, $\mathcal{H}_{\infty}$ robust control treats the disturbance $w{(t)}$ as an adversarial input with bounded energy. The aim is to design a stabilizing policy $K \in \mathcal{K}$ that minimizes the worst-case cost ${\sup{\int_{0}^{\infty}{x{(t)}^{\mathsf{T}}Q_{\infty}x{(t)}}}} + {u{(t)}^{\mathsf{T}}R_{\infty}u{(t)}dt}$ subject to ${\| w\|}_{\ell_{2}}^{2} = {\int_{0}^{\infty}{w^{\mathsf{T}}{(t)}w{(t)}{dt}}} \leq 1$ and ${x{}} = 0$, where $Q_{\infty} \succ 0$ and $R_{\infty} \succ 0$. This problem is equivalent to $\mathcal{H}_{\infty}$ optimal control: $\inf_{K \in \mathcal{K}}{\|{\mathbf{T}_{\infty}{(K)}}\|}_{\mathcal{H}_{\infty}}$, where $z_{\infty}$ defines the $\mathcal{H}_{\infty}$ performance output and $\mathbf{T}_{\infty}{(K)}$ denotes the transfer function from $w$ to $z_{\infty}$ as follows

One may also consider a mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design

where $\beta$ is a prescribed bound. Here, the $\mathcal{H}_{2}$ channel captures nominal performance, while the $\mathcal{H}_{\infty}$ channel enforces system robustness. It is worth noting that these two channels may be distinct or identical. We define the feasible set of $\mathcal{H}_{\infty}$-constrained stabilizing policies as

Note that a strict $\mathcal{H}_{\infty}$ bound is commonly used to ensure a well-defined stabilizing Riccati solution.

### Policy optimization for mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design

Despite simple formulation, problem is challenging to solve. A classical approach from is to minimize an upper bound on the $\mathcal{H}_{2}$ cost over the feasible set $\mathcal{K}_{\beta}$.

Recall that the $\mathcal{H}_{2}$ cost for any stabilizing policy $K \in \mathcal{K}$ is ${\|{\mathbf{T}_{2}{(K)}}\|}_{\mathcal{H}_{2}}^{2} = {{tr}{({{({Q_{2} + {K^{\mathsf{T}}R_{2}K}})}{\hat{X}}_{K}})}}$, where ${\hat{X}}_{K}$ is the unique solution to the Lyapunov equation

To enforce the $\mathcal{H}_{\infty}$ constraint , we instead consider the stabilizing solution $X_{K}$ to the Riccati equation

where $S_{K}:={Q_{\infty} + {K^{\mathsf{T}}R_{\infty}K}}$. By the bounded real lemma (see Lemma 1. ‣ 3.1 Geometry of the ℋ_∞ constrained domain ‣ 3 Basic Landscape Properties ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality")), a policy $K \in \mathcal{K}_{\beta}$ if and only if admits a unique stabilizing solution $X_{K} \succeq 0$ such that the matrix $A_{K} + {\beta^{- 2}X_{K}S_{K}}$ is Hurwitz. Subtracting from gives

Since $A_{K}$ is Hurwitz and the last term is positive semidefinite, it follows that ${X_{K} - {\hat{X}}_{K}} \succeq 0$, and hence the $\mathcal{H}_{2}$ cost admits an upper bound ${\|{\mathbf{T}_{2}{(K)}}\|}_{\mathcal{H}_{2}}^{2} \leq {{tr}{({{({Q_{2} + {K^{\mathsf{T}}R_{2}K}})}X_{K}})}}$ for all $K \in \mathcal{K}_{\beta}$. Therefore, we define the mixed cost

where $X_{K}$ is the unique stabilizing solution to.

In sum, we consider the following mixed design

Unlike the $\mathcal{H}_{2}$ cost, $J_{mix}$ is evaluated using the Riccati solution $X_{K}$ from rather than the Lyapunov solution ${\hat{X}}_{K}$ . Since the cost and constraint in are in general defined by distinct signals $z_{2}$ and $z_{\infty}$, we refer to this formulation as the two-channel mixed $\mathcal{H}_{2}$/$\mathcal{H}_{\infty}$ design.

We make the following standard assumption throughout.

### Assumption 1

$(A,B)$ is stabilizable and $(Q_{2}^{1/2},A)$ is detectable. In addition, the robustness parameter satisfies $\beta > \beta^{\ast}:={\inf_{K \in \mathcal{K}}{\|{\mathbf{T}_{\infty}{(K)}}\|}_{\mathcal{H}_{\infty}}}$.

We make another assumption for analysis.

### Assumption 2

The matrix $Q_{2}$ is positive semidefinite. The matrices $W$, $Q_{\infty}$, $R_{2}$, and $R_{\infty}$ are positive definite.

### Remark 1 (Single-channel case)

When the $\mathcal{H}_{2}$ and $\mathcal{H}_{\infty}$ channels share the same performance output, $J_{mix}$ in simplifies. Specifically, let $Q:=Q_{2} = Q_{\infty}$ and $R:=R_{2} = R_{\infty}$ in and, so that $z_{2} = z_{\infty}$. Under Assumption 1,

with $A_{K} + {\beta^{- 2}WP_{K}}$ Hurwitz.

We give further details in Appendix A.1 ‣ Appendix A Proofs in Sections 2 and 3 ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality"). As we will see, this reformulation yields a simpler gradient formula and a closed-form optimum. ∎

### Problem statement

Classical solutions to mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design primarily rely on Riccati equations or LMIs. While effective for small- to medium-scale systems, these techniques offer limited insight into the optimization landscape, and may face challenges in high-dimensional or data-driven settings.

In this work, we revisit the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control in from a nonconvex optimization perspective. Our goal is to uncover key structural properties and lay a theoretical foundation for policy optimization, focusing on three aspects:

Geometry of the optimization landscape. We study the geometry of the $\mathcal{H}_{\infty}$-constrained feasible domain $\mathcal{K}_{\beta}$ , and analyze key properties of the mixed cost function , including continuity, analyticity, and gradient expressions.

Global optimality of stationary points. We investigate whether problem admits spurious stationary points. We further derive the optimality conditions, and analyze the existence and uniqueness of stationary points.

Analysis via the $\mathtt{E}\mathtt{C}\mathtt{L}$ framework. We explore if the hidden convexity in problem can be revealed via an appropriate convex lifting. In particular, we ask if an extended convex lifting ($\mathtt{E}\mathtt{C}\mathtt{L}$) can be constructed to certify the global optimality of stationary points.

Collectively, our results provide a renewed understanding of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control through nonconvex optimization and convex lifting, and offer guidance for the design of principled policy optimization algorithms in large-scale or model-free settings.

## Basic Landscape Properties

In this section, we investigate the optimization landscape of, i.e., the geometry of the feasible set $\mathcal{K}_{\beta}$ and structural properties of the mixed cost function $J_{mix}$.

### Geometry of the $\mathcal{H}_{\infty}$ constrained domain

We start with a version of the Bounded Real Lemma, which connects a Riccati equation (or inequality) to an upper bound on the $\mathcal{H}_{\infty}$ norm. Here, we slightly abuse the notation for the matrices $A$, $B$, and $C$, but this should cause no confusion in the context.

### Lemma 1 (Bounded real lemma \[51, Corollary 13.24\])

Consider the transfer function ${\mathbf{G}{(s)}} = {C{({{sI} - A})}^{- 1}B}$, with $A \in {\mathbb{R}}^{n \times n}$, $B \in {\mathbb{R}}^{n \times m}$, and $C \in {\mathbb{R}}^{p \times n}$. Then, for any $\beta > 0$, the following statements are equivalent.

The matrix $A$ is Hurwitz and ${\|{\mathbf{G}{(s)}}\|}_{\mathcal{H}_{\infty}} < \beta$.

There exists an $X \succ 0$ satisfying the Riccati inequality

The Riccati equation

admits a unique stabilizing solution $X$ (i.e., $A + {\beta^{- 2}XC^{\mathsf{T}}C}$ is Hurwitz) satisfying $X \succeq 0$. If $(A,B)$ is further controllable, we have $X \succ 0$.

From \[51, Corollary 13.13\], the stabilizing solution $X$ to (13. ‣ 3.1 Geometry of the ℋ_∞ constrained domain ‣ 3 Basic Landscape Properties ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality")) is also minimal, i.e., $X \preceq \hat{X}$ for any other symmetric solution $\hat{X}$ to (13. ‣ 3.1 Geometry of the ℋ_∞ constrained domain ‣ 3 Basic Landscape Properties ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality")). This property clarifies the stabilizing solution in defining the mixed cost function, as it provides the tightest upper bound on the corresponding $\mathcal{H}_{2}$ norm.

Lemma 1. ‣ 3.1 Geometry of the ℋ_∞ constrained domain ‣ 3 Basic Landscape Properties ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality") plays a crucial role in understanding the feasible set and cost function of the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design. We summarize several basic properties of $\mathcal{K}_{\beta}$ below.

### Lemma 2

Suppose Assumptions 1 and 2 hold. The set $\mathcal{K}_{\beta}$ in satisfies the properties below:

It is always nonempty, open, and path-connected;

It is, in general, nonconvex and unbounded.

### Proof

The nonemptiness of $\mathcal{K}_{\beta}$ follows directly from Assumption 1. To establish openness, we apply Lemma 1. ‣ 3.1 Geometry of the ℋ_∞ constrained domain ‣ 3 Basic Landscape Properties ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality") to the transfer function $\mathbf{T}_{\infty}{(K)}$. This ensures that $K \in \mathcal{K}_{\beta}$ if and only if there exists $X \succ 0$ (the positive definiteness is ensured by $W \succ 0$) satisfying the strict Riccati inequality

Since the inequality is strict, the same $X \succ 0$ ensures that the inequality holds for all $K^{\prime}$ in a sufficiently small neighborhood around $K$. Hence, $\mathcal{K}_{\beta}$ is open.

Path-connectivity can be established using a strategy similar to that in \[16, Section III A\]. By applying the Schur complement to and introducing the change of variables $K = {YX^{- 1}}$, we see that $K \in \mathcal{K}_{\beta}$ if and only if there exist matrices $X \succ 0$ and $Y$ satisfying ${\mathbb{F}}_{cvx} \prec 0$, where

The above inequalities define a convex set in the lifted variables $(X,Y)$, and since the map $K = {YX^{- 1}}$ is continuous, it follows that $\mathcal{K}_{\beta}$ is path-connected.

While the nonconvexity of $\mathcal{K}_{\beta}$ is well-known, its unboundedness has not been discussed^11^1The set $\mathcal{K}_{\beta}$ in the discrete-time is bounded due to the coercivity of the discrete-time $\mathcal{H}_{\infty}$ function.. The example below illustrates the nonconvexity and unboundedness of $\mathcal{K}_{\beta}$. ∎

(b) Nonconvex noncoercive Jmix

(c) Nonconvex coercive JLQR

Figure 1: (a) Nonconvex 𝒦β with k11 = k22 = 0 for different β in Example 1. (b)-(c) Nonconvexity and (non)coercivity of the costs in Example 2, with feasible sets 𝒦3.5 and 𝒦∞ for (b) and (c) respectively. Red dots highlight global minima.

### Example 1

Consider ${{A = {- I_{2}}},{B = B_{w} = Q_{\infty} = R_{\infty} = I_{2}}},$ and policies of the form $K = \begin{bmatrix}
\end{bmatrix}$ for $\mathcal{K}_{\beta}$ . Let $\beta = 3.5$. We numerically verify that

but $K_{3} = {\frac{1}{2}{({K_{1} + K_{2}})}} \notin \mathcal{K}_{\beta}$. To see the unboundedness of $\mathcal{K}_{\beta}$, we analytically compute the $\mathcal{H}_{\infty}$ norm below

This implies that for any $\beta > 1.1$, $\mathcal{K}_{\beta}$ is unbounded.

Fig. 1(a) plots $\mathcal{K}_{\beta}$ restricted to the subspace $k_{11} = k_{22} = 0$ for $\beta = 3.5$, $6$, and $\infty$ (i.e., the unconstrained stabilizing set $\mathcal{K}$). The policies $K_{1}$, $K_{2}$, and $K_{3}$, marked in red, demonstrate the nonconvexity for $\beta = 3.5$. As expected, the feasible set $\mathcal{K}_{\beta}$ becomes larger as $\beta$ increases. ∎

We next characterize the boundary of $\mathcal{K}_{\beta}$. This will be useful as we later discuss the properties of $J_{mix}$.

### Theorem 1

Let ${cl}{(\mathcal{K}_{\beta})}$ denote the closure of $\mathcal{K}_{\beta}$ defined . Under Assumptions 1 and 2, we have

Theorem 1 may seem obvious, but the argument is in fact subtle. For instance, consider ${f{(x)}} = {x^{2}{({x + 1})}}$ and $C_{1} = {\{{x \in {\mathbb{R}}}\mid{{f{(x)}} < 0}\}}$, $C_{2} = {\{{x \in {\mathbb{R}}}\mid{{f{(x)}} \leq 0}\}}$. Clearly, $C_{2} \nsubseteq {{cl}{(C_{1})}}$ since $0 \in C_{2}$ cannot be approached by any sequence in $C_{1}$. In fact, Theorem 1 relies on fundamental properties of the $\mathcal{H}_{\infty}$ norm to handle the above issue as well as marginally stabilizing policies. We present the full details in Appendix A.2.

Theorem 1 implies that the boundary of $\mathcal{K}_{\beta}$, denoted ${\partial\mathcal{K}_{\beta}}:={{{cl}{(\mathcal{K}_{\beta})}} \smallsetminus \mathcal{K}_{\beta}}$, is the set of stabilizing policies whose $\mathcal{H}_{\infty}$ norm equals $\beta$. Note that $\partial\mathcal{K}_{\beta}$ may be unbounded.

### Corollary 1

Under Assumptions 1 and 2, the boundary of $\mathcal{K}_{\beta}$ satisfies ${{\partial\mathcal{K}_{\beta}} \subseteq \left\{ {K \in \mathcal{K}}\mid{{\|{\mathbf{T}_{\infty}{(K)}}\|}_{\mathcal{H}_{\infty}} = \beta} \right\}}.$

### Analyticity of the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ cost function

We now examine some properties of the cost function. It is clear from Lemma 2 that $J_{mix}$ is nonconvex. Our next result shows that it is real analytic (and hence infinitely differentiable) on the feasible set $\mathcal{K}_{\beta}$.

### Theorem 2

Under Assumption 1, the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ cost function $J_{mix}$ in is real analytic on $\mathcal{K}_{\beta}$.

Note that $J_{mix}$ is defined through the stabilizing solution $X_{K}$ of, which admits no closed form. Instead, we use the Implicit Function Theorem \[23, Theorem 2.3.5\] to show that $X_{K}$ depends analytically on $K \in \mathcal{K}_{\beta}$. Thus, the cost $J_{mix}$ is real analytic. Proof details are provided in Appendix A.4.

Since $\mathcal{K}_{\beta}$ is open, the optimal value of problem may not be attained but only approached at the boundary $\partial\mathcal{K}_{\beta}$. To capture this limiting behavior, we extend $J_{mix}$ to $\partial\mathcal{K}_{\beta}$. By Corollary 1, any $K \in {\partial\mathcal{K}_{\beta}}$ satisfies ${\|{\mathbf{T}_{\infty}{(K)}}\|}_{\mathcal{H}_{\infty}} = \beta$, so Lemma 1. ‣ 3.1 Geometry of the ℋ_∞ constrained domain ‣ 3 Basic Landscape Properties ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality") no longer applies and does not admit stabilizing solution. Nonetheless, it is known that still admits a unique minimal solution $X_{K}$ with eigenvalues of $A_{K} + {\beta^{- 2}X_{K}S_{K}}$ in the closed left half-plane \[51, Corollary 13.13, Lemma 13.17\]. We thus define the boundary cost as

where $X_{K}$ is the minimal solution to.

The above extension is continuous: as $K \in \mathcal{K}_{\beta}$ approaches a boundary point $K_{0} \in {\partial\mathcal{K}_{\beta}}$, the cost converges to ${\overset{\sim}{J}}_{mix}{(K_{0})}$.

### Lemma 3

Suppose Assumptions 1 and 2 hold. Given any boundary point $K_{0} \in {\partial\mathcal{K}_{\beta}}$, we have

The proof relies on a nontrivial continuity result for Riccati minimal solutions \[25, Theorem 11.2.1\], with details deferred to Appendix A.3. As a direct consequence of Lemma 3, the cost $J_{mix}$ is non-coercive, remaining finite as $K$ with ${\| K\|} < \infty$ approaches the boundary of $\mathcal{K}_{\beta}$. Nevertheless, since $J_{mix}$ serves as a pointwise upper bound on the coercive LQR cost, it exhibits partial coercivity: ${J_{mix}{(K)}}\rightarrow\infty$ as ${\| K\|}\rightarrow\infty$.

### Example 2 (Non-coercivity)

Consider the problem instance from Example 1. We set $\beta = 3.5$ and $Q_{2} = R_{2} = I_{2}$ to define $J_{mix}$. For comparison, we also consider the limiting case $\beta = \infty$, which reduces to the LQR cost $J_{LQR}$. The global optima are $K^{\ast} = {- {0.4193I_{2}}}$ for $J_{mix}$ and $K_{LQR}^{\ast} = {{({1 - \sqrt{2}})}I_{2}}$ for $J_{LQR}$. Fig. 1(b) depicts $J_{mix}$ for $K = {K^{\ast} + \begin{bmatrix}
\end{bmatrix}}$, while Fig. 1(c) plots $J_{LQR}$ for $K = {K_{LQR}^{\ast} + \begin{bmatrix}
\end{bmatrix}}$. As shown in Fig. 1(b), the cost $J_{mix}$ stays bounded as $K$ with ${\| K\|} < \infty$ approaches the boundary $\partial\mathcal{K}_{\beta}$, unlike $J_{LQR}$ which diverges in Fig. 1(c). ∎

Theorem 2 ensures that $J_{mix}$ is infinitely differentiable. In particular, we have the following gradient formulas.

### Lemma 4

Suppose Assumption 1 holds. For any $K \in \mathcal{K}_{\beta}$, the policy gradient of $J_{mix}$ is given by

Lemma 4 applies to the general two-channel case. In the single-channel case where $z_{2} = z_{\infty}$, an alternative gradient expression can be derived using (11. ‣ 2.2 Policy optimization for mixed ℋ₂/ℋ_∞ design ‣ 2 Preliminaries ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality")).

### Lemma 5

Suppose Assumption 1 holds. If $z_{2} = z_{\infty}$ in and, the policy gradient of $J_{mix}$ can be evaluated as

${{{\hat{A}}_{K}\Lambda_{K}} + {\Lambda_{K}{\hat{A}}_{K}^{\mathsf{T}}} + W} = 0$ (18b)
with ${\hat{A}}_{K}:={A_{K} + {\beta^{- 2}WP_{K}}}$ being stable.

The formula in also applies to the single-channel case by setting $Q_{2} = Q_{\infty}$ and $R_{2} = R_{\infty}$. While mathematically equivalent, the alternative expression in is more useful for analysis. Our proofs of Lemmas 4 and 5 build on the strategy of \[39 control"), Appendix B.4\], adapting sensitivity analysis of Lyapunov equations to the Riccati settings. Details are provided in Appendices A.5.

### Remark 2 (Comparison with LQR)

Lemmas 4 and 5 show that computing $\nabla J_{mix}$ requires solving one Riccati and one Lyapunov equation, slightly more involved than the LQR case, which only needs two Lyapunov equations \[26, Section IV\]. Note that as $\beta\rightarrow\infty$, $J_{mix}$ in and (11. ‣ 2.2 Policy optimization for mixed ℋ₂/ℋ_∞ design ‣ 2 Preliminaries ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality")) reduces to $J_{LQR}$, and both gradient formulas simplify to $\nabla J_{LQR}$. In particular, we have ${{\nabla J_{LQR}}{(K)}} = {2{({{R_{2}K} + {B^{\mathsf{T}}\Gamma_{K}}})}X_{K}}$, where $X_{K}$ and $\Gamma_{K}$ are the solutions to the Lyapunov equations

This is expected as reduces to LQR as $\beta\rightarrow\infty$. ∎

## No Spurious Stationary Points

In this section, we characterize the global optimality of the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design.

### Any stationary point is globally optimal

Since $\mathcal{K}_{\beta}$ is open, any local minimizer of $J_{mix}$ must lie in its interior and thus must be a stationary point. Despite nonconvexity, we establish a key result that every stationary point (when it exists) of is globally optimal.

### Theorem 3

Suppose Assumptions 1 and 2 hold. For any policy $K \in \mathcal{K}_{\beta}$, if $K$ is a stationary point, i.e., ${{\nabla J_{mix}}{(K)}} = 0$, then $K$ is a global minimizer of.

Owing to the absence of spurious stationary points, the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design exhibits hidden convexity: every local minimum is globally optimal. This parallels recent results on benign nonconvexity in state-feedback problems such as LQR and $\mathcal{H}_{\infty}$ control.

Theorem 3 is most closely related to \[45, Proposition A.5\], which establishes the global optimality of all stationary points in the single-channel case. Its proof relies on a game-theoretic formulation, whose extension to the two-channel case remains unclear. In contrast, our approach builds on convex reformulations via the recently developed $\mathtt{E}\mathtt{C}\mathtt{L}$ framework, which provides greater transparency and directly deals with the general two-channel problem. In this sense, \[45, Proposition A.5\] appears as a special case of Theorem 3. Our proof involves an explicit $\mathtt{E}\mathtt{C}\mathtt{L}$ construction, which requires careful analysis of (non)strict Riccati inequalities. We provide the details in Section 5.

Building on Lemma 4 and Theorem 3, we further derive stationarity conditions that characterize global optima of problem. To simplify the expression, we assume $R_{\infty} = {\alpha^{2}R_{2}}$ with $\alpha \geq 0$ as a design parameter.

### Corollary 2

Suppose Assumptions 1 and 2 hold, and assume $R_{\infty} = {\alpha^{2}R_{2}}$ for some $\alpha \geq 0$. Then a policy $K \in \mathcal{K}_{\beta}$ is global optimal for if and only if there exist matrices $\Gamma \succeq 0$ and $X \succ 0$ satisfying the following conditions:

${K = {- {R_{2}^{- 1}B^{\mathsf{T}}\Gamma\left( {I + {\beta^{- 2}\alpha^{2}X\Gamma}} \right)^{- 1}}}},$ (20a)
${{{{\overset{\sim}{A}}_{K}^{\mathsf{T}}\Gamma} + {\Gamma{\overset{\sim}{A}}_{K}} + Q_{2} + {K^{\mathsf{T}}R_{2}K}} = 0},$ (20c)

where ${\overset{\sim}{A}}_{K}:={A_{K} + {\beta^{- 2}XS_{K}}}$ is further Hurwitz.

### Proof

We prove the equivalence in two directions.

$\Rightarrow$. Suppose $K \in \mathcal{K}_{\beta}$ is globally optimal . Since $\mathcal{K}_{\beta}$ is open, we must have ${{\nabla J_{mix}}{(K)}} = 0$. Using the gradient formula and setting ${{\nabla J_{mix}}{(K)}} = 0$ yields

where $X_{K}$ is the unique stabilizing solution to the Riccati equation and $\Gamma_{K}$ solves the Lyapunov equation (17b). Since $W \succ 0$, the bounded real lemma ensures that $X_{K} \succ 0$. In addition, (17b) implies that $\Gamma_{K} \succeq 0$. Thus, the matrix $I + {\beta^{- 2}\alpha^{2}X_{K}\Gamma_{K}}$ is invertible. Let $\Gamma:=\Gamma_{K}$ and $X:=X_{K}$. Then using $R_{\infty} = {\alpha^{2}R_{2}}$, we can rearrange to obtain (20a). It is clear that and (17b) corresponds to (20b) and (20c), respectively. Thus, all three optimality conditions are satisfied.

$\Leftarrow$. Suppose that there exist $X \succ 0$ and $\Gamma \succeq 0$ satisfying (20a) to (20c). From (20b) and the stability of ${\overset{\sim}{A}}_{K}$, Lemma 1. ‣ 3.1 Geometry of the ℋ_∞ constrained domain ‣ 3 Basic Landscape Properties ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality") implies that $K \in \mathcal{K}_{\beta}$. Substituting the expression for $K$ in (20a) into the gradient formula confirms that ${{\nabla J_{mix}}{(K)}} = 0$. We then conclude by Theorem 3 that $K$ is a global minimizer of. ∎

Corollary 2 provides necessary and sufficient conditions for a policy $K \in \mathcal{K}_{\beta}$ to be globally optimal. Similar conditions were derived in \[4, Theorem 4.1\] via Lagrange multipliers, but were only shown to be necessary.

Figure 2: Optimization landscapes of Jmix, J∞, and JLQR in Example 4.7. (a) Infimum J1* not attained (hollow red circle marks the boundary). (b) Minimum J2* attained (solid red dot). (c) Single-channel case: minimum attained (solid red dot).

Clearly, Corollary 2 also applies to the single-channel case. However, the alternative formulation in (11. ‣ 2.2 Policy optimization for mixed ℋ₂/ℋ_∞ design ‣ 2 Preliminaries ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality")) leads to a simpler gradient expression , further offering additional insight into global optimality. To see this, with $W \succ 0$, the solution $\Lambda_{K}$ to the Lyapunov equation (18b) is positive definite, and therefore, the stationarity condition ${{\nabla J_{mix}}{(K)}} = 0$ implies ${K = {- {R^{- 1}B^{\mathsf{T}}P_{K}}}}.$ Substituting this into the Riccati equation (11b. ‣ 2.2 Policy optimization for mixed ℋ₂/ℋ_∞ design ‣ 2 Preliminaries ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality")) results in a single Riccati equation, as summarized below.

### Corollary 3

Under Assumptions 1 and 2, if $z_{2} = z_{\infty}$ in and, a policy $K \in \mathcal{K}_{\beta}$ is globally optimal for if and only if there exists a matrix $P \succeq 0$ such that:

where $A + {{({{\beta^{- 2}W} - {BR^{- 1}B^{\mathsf{T}}}})}P}$ is further Hurwitz.

The proof is similar to that of Corollary 2. We give some details in Appendix B.1. Compared with the coupled conditions , the conditions in are much simpler, requiring solving only a single Riccati equation independent of $K$.

### Remark 3 (Connection to LQR)

As $\beta\rightarrow\infty$, both optimality conditions in the single- and two-channel cases, and, reduce to the classical LQR Riccati equation

with the optimal policy $K = {- {R^{- 1}B^{\mathsf{T}}P}}$, where $P$ is the stabilizing solution. ∎

### Remark 4 (Connection to $\mathcal{H}_{\infty}$ suboptimal control)

The Riccati equation (22b) is closely tied to state-feedback $\mathcal{H}_{\infty}$ suboptimal control. By \[51, Theorem 17.6\] and \[25, Theorem 20.2.1\], it admits a unique stabilizing solution $P$ if and only if there exists a policy $K \in \mathcal{K}_{\beta}$. One suboptimal policy is given by $K = {- {R^{- 1}B^{\mathsf{T}}P}}$. As shown in Corollary 3, this $K$ also solves problem with $z_{2} = z_{\infty}$. This highlights the close connection of to several classical formulations, including maximum entropy $\mathcal{H}_{\infty}$ control, risk-sensitive control, and zero-sum dynamic games. ∎

### Existence of stationary points

Theorem 3 and Corollaries 2-3 do not ensure the existence of stationary points. In particular, the optimality conditions may be infeasible. We summarize this fact below.

### Fact 1

Under Assumptions 1 and 2, the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control may admit no stationary points in $\mathcal{K}_{\beta}$, and its optimal value may not be attained within $\mathcal{K}_{\beta}$.

In fact, the infeasibility of stems from an overly stringent robustness requirement. Relaxing the constraint by increasing $\beta$ ensures the existence of a stationary point.

### Theorem 4.4

Under Assumption 1, there exists a threshold $\overline{\beta} > 0$ such that for all $\beta > \overline{\beta}$, problem admits a stationary point $K \in \mathcal{K}_{\beta}$. Equivalently, there exists $(K,X,\Gamma)$ satisfying where $X$ is the stabilizing solution to (20b).

Note that this existence result does not rely on the assumption $R_{\infty} = {\alpha^{2}R_{2}}$. The proof uses a perturbation argument around the LQR case. The key insight is that as $\beta\rightarrow\infty$, the optimality conditions converge to those of LQR (Remark 3. ‣ 4.1 Any stationary point is globally optimal ‣ 4 No Spurious Stationary Points ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality")), where a stationary point always exists. The details are technically involved, and we present them in Appendix B.2.

In contrast, the single-channel case always admits a stationary point attaining the optimal value, thanks to its connection to $\mathcal{H}_{\infty}$ suboptimal control (Remark 4. ‣ 4.1 Any stationary point is globally optimal ‣ 4 No Spurious Stationary Points ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality")).

### Theorem 4.5

Under Assumptions 1 and 2, the single-channel problem with $z_{2} = z_{\infty}$ admits a unique stationary point $K \in \mathcal{K}_{\beta}$, given by $K = {- {R^{- 1}B^{\mathsf{T}}P}}$, where $P$ is the stabilizing solution to the Riccati equation (22b).

### Proof 4.6

By \[51, Theorem 17.6\] and \[25, Theorem 20.2.1\], (22b) admits a stabilizing solution if and only if $\mathcal{K}_{\beta}$ is nonempty, satisfied by Assumption 1. Then, under Assumption 2, the stationary point is given by (22a), and its uniqueness follows from that of the stabilizing solution.

We provide a simple example illustrating Theorems 4.4 and 4.5, showing that the existence of stationary points depends on $\beta$.

### Example 4.7

Consider a scalar instance of with $A = {- 1}$, $B = B_{w} = 1$, $Q_{2} = 0$, $Q_{\infty} = 1$, $R_{2} = R_{\infty} = 1$. The stabilizing set is $\mathcal{K} = {\{{k \in {\mathbb{R}}}:{k < 1}\}}$. The $\mathcal{H}_{\infty}$ norm can be computed in closed form as ${J_{\infty}{(k)}}:={\|{\mathbf{T}_{\infty}{(k)}}\|}_{\mathcal{H}_{\infty}} = {\sqrt{1 + k^{2}}/{({1 - k})}}$ for all $k < 1$, which yields the feasible set

With ${J_{mix}{(k)}} = {k^{2}X_{k}}$ and $X_{k}$ the stabilizing solution to ${{\beta^{- 2}{({k^{2} + 1})}X_{k}^{2}} + {2{({k - 1})}X_{k}} + 1} = 0$, problem reads

Case 1: $\beta = 1$. We have $\mathcal{K}_{1} = {\{ k:{k < 0}\}}$. The infimum $J_{1}^{\ast} = 0$ is not attained in $\mathcal{K}_{1}$ but approached as $k\rightarrow 0^{-}$ and $X_{k}\rightarrow 1^{+}$ (see Figure 2(a)).

Case 2: $\beta = 2$. We have $\mathcal{K}_{2} = {\{ k:{k < {{({4 - \sqrt{7}})}/3}}\}}$. The infimum $J_{2}^{\ast} = 0$ is attained by the optimal policy $k^{\ast} = 0$ (see Figure 2(b)). One can verify by Lemma 4 ${{\nabla J_{mix}}{(k^{\ast})}} = 0$.

Case 3 (single-channel): $\beta = 1$. We consider $Q = 0$ and $R = 1$, which preserves the LQR cost but alters the $\mathcal{H}_{\infty}$ constraint (blue curve in Figure 2(c)). Here, $J_{mix}$ always admits a stationary point, showing that problem structure beyond $\beta$ also affects the existence of optimal policies.

## Analysis via Extended Convex Lifting

This section exploits the recent $\mathtt{E}\mathtt{C}\mathtt{L}$ framework to prove the global optimality result in Theorem 3, details the $\mathtt{E}\mathtt{C}\mathtt{L}$ construction for problem, and discusses the solvability of the associated convex reformulation.

### A framework of Extended Convex Lifting

The $\mathtt{E}\mathtt{C}\mathtt{L}$ framework studies a class of nonconvex optimization problems using convex tools. The key idea is simple and based on a change of variables. Let $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ be smooth and nonconvex. Suppose there exists a smooth bijection $y = {\phi{(x)}}$ such that ${g{(y)}}:={f{({\phi^{- 1}{(y)}})}}$ becomes convex. It is then clear that ${{\min f}{(x)}} = {{\min g}{(y)}}$ and every stationary point of $f$ is globally optimal. Here, the mapping $y = {\phi{(x)}}$ acts as direct convexification.

The $\mathtt{E}\mathtt{C}\mathtt{L}$ generalizes this idea to a broader class of constrained nonconvex problems that may not admit direct convexification. Indeed, such problems frequently arise in control, including. We first review the definitions and key results of $\mathtt{E}\mathtt{C}\mathtt{L}$, presenting a simplified version tailored for clarity and relevance to our setting.

For a function $f:{\mathcal{D}\rightarrow{\mathbb{R}}}$ with an open domain $D \subseteq {\mathbb{R}}^{d}$, we define its strict and non-strict epigraphs by

### Definition 5.8 (Extended Convex Lifting )

Let $f:{\mathcal{D}\rightarrow{\mathbb{R}}}$ be continuous, where $\mathcal{D} \subseteq {\mathbb{R}}^{d}$ is open. We say that a tuple $(\mathcal{L}_{lft},\mathcal{F}_{cvx},\Phi)$ is an $\mathtt{E}\mathtt{C}\mathtt{L}$ of $f$ if the following hold:

$\mathcal{L}_{lft} \subseteq {{\mathbb{R}}^{d} \times {\mathbb{R}} \times {\mathbb{R}}^{d_{\xi}}}$ is a lifted set with an extra variable $\xi \in {\mathbb{R}}^{d_{\xi}}$, such that its canonical projection onto the first $d + 1$ coordinates, given by ${{\pi_{x,\gamma}{(\mathcal{L}_{lft})}} = {\{{(x,\gamma)}:{{\exists\xi} \in {{\mathbb{R}}^{d_{\xi}}\text{s.t.}{(x,\gamma,\xi)}} \in \mathcal{L}_{lft}}\}}},$ satisfies

$\mathcal{F}_{cvx} \subseteq {{\mathbb{R}} \times {\mathbb{R}}^{d + d_{\epsilon}}}$ is a convex set and $\Phi$ is a $C^{2}$ diffeomorphism from $\mathcal{L}_{lft}$ to $\mathcal{F}_{cvx}$.

For any ${(x,\gamma,\xi)} \in \mathcal{L}_{lft}$, we have ${\Phi{(x,\gamma,\xi)}} = {(\gamma,\zeta_{1})} \in \mathcal{F}_{cvx}$ for some $\zeta_{1} \in {\mathbb{R}}^{d + d_{\epsilon}}$. In other words, the mapping $\Phi$ directly outputs $\gamma$ in the first component.

This procedure generalizes direct convexification by introducing epigraphs and a lifting variable $\xi$. The set inclusion (23. ‣ 5.1 A framework of Extended Convex Lifting ‣ 5 Analysis via Extended Convex Lifting ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality")) also adds flexibility. Similar to direct convexification, the existence of an $\mathtt{E}\mathtt{C}\mathtt{L}$ enables the minimization of $f$ over $\mathcal{D}$ to be reformulated as a convex problem. Specifically, we have the following equivalence

where the right-hand side is convex by the $\mathtt{E}\mathtt{C}\mathtt{L}$ construction.

We here define non-degenerate points of $f$.

### Definition 5.9 (Non-degenerate points )

Given an $\mathtt{E}\mathtt{C}\mathtt{L}$ $(\mathcal{L}_{lft},\mathcal{F}_{cvx},\Phi)$ for $f$, a point $x \in \mathcal{D}$ is called non-degenerate if ${{(x,{f{(x)}})} \in {\pi_{x,\gamma}{(\mathcal{L}_{lft})}}}.$

Lastly, the existence of an $\mathtt{E}\mathtt{C}\mathtt{L}$ certifies the global optimality of non-degenerate stationary points of $f$.

### Lemma 5.10 (\[50, Theorem 3.2\])

Let $f:{\mathcal{D}\rightarrow{\mathbb{R}}}$ be differentiable, where $\mathcal{D} \subseteq {\mathbb{R}}^{d}$ is open. Suppose $f$ admits an $\mathtt{E}\mathtt{C}\mathtt{L}$ $(\mathcal{L}_{lft},\mathcal{F}_{cvx},\Phi)$. Then, any non-degenerate stationary point $x^{\ast}$ satisfying ${{\nabla f}{(x^{\ast})}} = 0$ is a global minimizer of $f$ over $\mathcal{D}$.

### Proof of Theorem 3 via $\mathtt{E}\mathtt{C}\mathtt{L}$ construction

In this section, we construct an $\mathtt{E}\mathtt{C}\mathtt{L}$ for problem, and show that all feasible policies in $\mathcal{K}_{\beta}$ are non-degenerate under Assumptions 1 and 2. Theorem 3 then follows directly from Theorem 5.10. ‣ 5.1 A framework of Extended Convex Lifting ‣ 5 Analysis via Extended Convex Lifting ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality"). The $\mathtt{E}\mathtt{C}\mathtt{L}$ construction details are involved, which rely on the (non)-strict bounded real lemma.

We start by characterizing the non-strict epigraph of the extended cost ${\overset{\sim}{J}}_{mix}$, which is central to the $\mathtt{E}\mathtt{C}\mathtt{L}$ construction. Working with the extended cost simplifies the treatment of boundary cases and also facilitates subsequent proofs.

### Lemma 5.11

Consider the extended cost ${\overset{\sim}{J}}_{mix}:{{{cl}{(\mathcal{K}_{\beta})}}\rightarrow{\mathbb{R}}}$ defined . Under Assumptions 1 and 2, a pair ${(K,\gamma)} \in {{epi}_{\geq}{({\overset{\sim}{J}}_{mix})}}$ if and only if there exists some $X \succ 0$ such that

The proof of Lemma 5.11 is deferred to Appendix C.1. We now construct an $\mathtt{E}\mathtt{C}\mathtt{L}$ for in three steps.

Step 1: Lifted set. Motivated by Lemma 5.11, we introduce a lifted set $\mathcal{L}_{lft}$ with an extra variable $X$

Step 2: Convex set. We define a convex set

where ${\mathbb{F}}_{cvx}$ is defined .

Step 3: Diffeomorphism. Using the classical change of variables $Y = {KX}$, we define the mapping

Lemma 5.11 immediately yields the following key result, which validates the $\mathtt{E}\mathtt{C}\mathtt{L}$ construction.

### Corollary 5.12

Under Assumptions 1 and 2, we have

The following result validates that the constructed tuple $(\mathcal{L}_{lft},\mathcal{F}_{cvx},\Phi)$ forms an $\mathtt{E}\mathtt{C}\mathtt{L}$ .

### Theorem 5.13

Under Assumptions 1 and 2, the canonical projection of $\mathcal{L}_{lft}$ onto $(K,\gamma)$, denoted $\pi_{K,\gamma}{(\mathcal{L}_{lft})}$, satisfies

Moreover, the mapping $\Phi$ given by (25c) is a $C^{2}$ (and in fact $C^{\infty}$) diffeomorphism from $\mathcal{L}_{lft}$ in (25a) to $\mathcal{F}_{cvx}$ in (25b).

Note that the set inclusion in follows directly from Corollary 5.12, whereas proving the set identity in requires an additional argument showing that ${{epi}_{\geq}{({\overset{\sim}{J}}_{mix})}} = {{cl}{{epi}_{\geq}{(J_{mix})}}}$, with proof details given in Appendix C.2.

Since ${{epi}_{>}{(J_{mix})}} \subseteq {{epi}_{\geq}{(J_{mix})}}$, the inclusion in is stronger than that required by the $\mathtt{E}\mathtt{C}\mathtt{L}$ definition in (23. ‣ 5.1 A framework of Extended Convex Lifting ‣ 5 Analysis via Extended Convex Lifting ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality")), which enlarges the set of non-degenerate points and allows $\mathtt{E}\mathtt{C}\mathtt{L}$ to certify global optimality over $\mathcal{K}_{\beta}$.

### Remark 5.14 (Another valid $\mathtt{E}\mathtt{C}\mathtt{L}$)

In constructing $\mathcal{L}_{lft}$ in (25a), the nonstrict Riccati inequality is crucial for establishing ${{epi}_{\geq}{(J_{mix})}} \subseteq {\pi_{K,\gamma}{(\mathcal{L}_{lft})}}$. If instead the strict Riccati inequality is used, the construction still yields a valid $\mathtt{E}\mathtt{C}\mathtt{L}$, but only ensures the weaker inclusion ${{epi}_{>}{(J_{mix})}} \subseteq {\pi_{K,\gamma}{(\mathcal{L}_{lft})}}$.

By Lemma 5.10. ‣ 5.1 A framework of Extended Convex Lifting ‣ 5 Analysis via Extended Convex Lifting ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality"), an $\mathtt{E}\mathtt{C}\mathtt{L}$ certifies the global optimality of any non-degenerate stationary points. According to Definition 5.9. ‣ 5.1 A framework of Extended Convex Lifting ‣ 5 Analysis via Extended Convex Lifting ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality") and the inclusion ${{epi}_{\geq}{(J_{mix})}} \subseteq {\pi_{K,\gamma}{(\mathcal{L}_{lft})}}$ shown in Theorem 5.13, we have the following desirable property.

### Corollary 5.15

Using the $\mathtt{E}\mathtt{C}\mathtt{L}$ $(\mathcal{L}_{lft},\mathcal{F}_{cvx},\Phi)$ , any $K \in \mathcal{K}_{\beta}$ is non-degenerate.

Considering Fact 5.15 and the differentiability of $J_{mix}$ over $\mathcal{K}_{\beta}$ (Lemma 4), the global optimality established in Theorem 3 follows directly from the $\mathtt{E}\mathtt{C}\mathtt{L}$ guarantee in Lemma 5.10. ‣ 5.1 A framework of Extended Convex Lifting ‣ 5 Analysis via Extended Convex Lifting ‣ Policy Optimization of Mixed ℋ₂/ℋ_∞ Control: Benign Nonconvexity and Global Optimality").

### Convex reformulation and its solvability

The $\mathtt{E}\mathtt{C}\mathtt{L}$ construction also leads to a convex reformulation , which offers further insight into problem.

### Theorem 5.16

Consider problem and the convex set $\mathcal{F}_{cvx}$ in (25b). Under Assumptions 1 and 2, we have

We use "min" in to indicate that the optimum is always attained (see Proposition 5.17). Unlike optimizing $K$ over the policy space $\mathcal{K}_{\beta}$, the convex reformulation in optimizes $(\gamma,X,Y)$ over the higher-dimensional set $\mathcal{F}_{cvx}$.

The result most relevant to Theorem 5.16 is \[21, Theorem 4.3\], which gives a similar reformulation via strict LMIs (equations - therein). While the strict formulation yields the same optimal value, it does not capture the global optimality of all stationary points (Theorem 3).

We now address the solvability of the reformulation.

### Proposition 5.17

Let $\gamma^{\ast}$ be the (finite) optimal value of. Under Assumptions 1 and 2, the following statements hold.

The reformulation , i.e. $\min_{{(\gamma,X,Y)} \in \mathcal{F}_{cvx}}\gamma$, admits a solution. That is, there exists ${(\gamma^{\ast},X^{\ast},Y^{\ast})} \in \mathcal{F}_{cvx}$ attaining the minimum $\gamma^{\ast}$.

The corresponding policy $K^{\ast}:={Y^{\ast}{(X^{\ast})}^{- 1}}$ lies in ${cl}{(\mathcal{K}_{\beta})}$ with its extended cost value ${{\overset{\sim}{J}}_{mix}{(K^{\ast})}} = \gamma^{\ast}$.

### Proof 5.18

By Theorem 5.16, $\gamma^{\ast} = {\min_{{(\gamma,X,Y)} \in \mathcal{F}_{cvx}}\gamma}$. We first note that $\gamma^{\ast}$ cannot be attained as ${\| K\|}\rightarrow\infty$ since the corresponding cost diverges. Now consider the case where $\gamma^{\ast}$ is attained in $\mathcal{K}_{\beta}$, i.e., there exists $K^{\ast} \in \mathcal{K}_{\beta}$ with ${J_{mix}{(K^{\ast})}} = \gamma^{\ast}$. That is, ${(K^{\ast},\gamma^{\ast})} \in {{epi}_{\geq}{(J_{mix})}}$. By the inclusion ${{epi}_{\geq}{(J_{mix})}} \subseteq {\pi_{K,\gamma}{(\mathcal{L}_{lft})}}$ , there exists $X^{\ast}$ such that ${(K^{\ast},\gamma^{\ast},X^{\ast})} \in \mathcal{L}_{lft}$. Applying the diffeomorphism ${\Phi{(K^{\ast},\gamma^{\ast},X^{\ast})}} = {(\gamma^{\ast},X^{\ast},Y^{\ast})} \in \mathcal{F}_{cvx}$ then establishes solvability in this case.

Next, consider the case where $\gamma^{\ast}$ is not attained in $\mathcal{K}_{\beta}$. By the continuity in Lemma 3, there exists a boundary policy $K^{\ast} \in {\partial\mathcal{K}_{\beta}}$ with ${{\overset{\sim}{J}}_{mix}{(K^{\ast})}} = \gamma^{\ast}$. Crucially, the pair $(K^{\ast},\gamma^{\ast})$ still admits a valid lifting to $\mathcal{L}_{lft}$. This follows from Corollary 5.12, where ${{epi}_{\geq}{({\overset{\sim}{J}}_{mix})}} = {\pi_{K,\gamma}{(\mathcal{L}_{lft})}}$ guarantees the existence of $X^{\ast}$ such that ${(K^{\ast},\gamma^{\ast},X^{\ast})} \in \mathcal{L}_{lft}$. Applying the diffeomorphism ${\Phi{(K^{\ast},\gamma^{\ast},X^{\ast})}} = {(\gamma^{\ast},X^{\ast},Y^{\ast})} \in \mathcal{F}_{cvx}$ then shows solvability.

Combining both cases and noting that $K^{\ast} = {Y^{\ast}{(X^{\ast})}^{- 1}}$ since $Y^{\ast} = {K^{\ast}X^{\ast}}$, we conclude that there exists ${(\gamma^{\ast},X^{\ast},Y^{\ast})} \in \mathcal{F}_{cvx}$ with $K^{\ast} \in {{cl}{(\mathcal{K}_{\beta})}}$.

Proposition 5.17 guarantees solvability of the convex reformulation in as well as recovery of an optimal policy, even when the optimal value is not attained in $\mathcal{K}_{\beta}$, in which case the policy lies on the boundary $\partial\mathcal{K}_{\beta}$.

## Numerical Experiments

In this section, we present numerical experiments evaluating the performance of different methods for solving the mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control and in both small and large-scale cases.

### Numerical approaches and setup

We compare four approaches:

Analytical solution: For the single-channel case, we solve the Riccati equation (22b) and obtain the optimal policy from (22a).

Policy iteration: Inspired by the optimality conditions in Corollaries 2 and 3, we apply iterative policy updates to solve and its single-channel case. The details are given below.

LMI-based convex optimization: Solve the convex reformulation in with the conic solver MOSEK.

HIFOO: A sophisticated nonsmooth optimization package (v3.501 with Hanso 2.01) for fixed-order $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ controller synthesis.

Policy iteration. The method starts from a feasible policy and alternates between policy evaluation (solving a Riccati equation) and policy improvement. It can be viewed as a fixed-point iteration for solving a stationary point ${{\nabla J_{mix}}{( \cdot )}} = 0$. In the single-channel case with $z_{2} = z_{\infty}$, using, the update simplifies to:

While a formal convergence analysis remains open, we conjecture that the method converges for sufficiently large $\beta$, and leave this as future work.

Setup. All experiments are conducted in MATLAB R2024b. The stabilizing Riccati solution is computed using MATLAB's icare. Policy iteration is run until convergence ${\|{K^{\prime} - K}\|} < 10^{- 5}$. For LMI-based methods, we use MOSEK with its default high-accuracy stopping criteria.

We compare these methods in terms of 1) the runtime complexity; 2) the square root of $J_{mix}$ of the converged policy; 3) the resulting $\mathcal{H}_{2}$ and $\mathcal{H}_{\infty}$ norms.

### A low-dimensional example

We begin with a low-dimensional example (instance $0$) with a $3 \times 3$ policy matrix. The problem parameters are

The performance matrices for the $\mathcal{H}_{2}$ and $\mathcal{H}_{\infty}$ channels are

For the special case $z_{2} = z_{\infty}$, we set $Q = R = I_{3}$. The minimal achievable robustness level (i.e., the optimal $\mathcal{H}_{\infty}$ norm) is $\beta^{\ast} \approx 5.24$. We evaluate all methods with $\beta = 6$, $14$, and $18$. One can verify that Assumptions 1 and 2 are satisfied. For reference, in the single-channel case, the optimal LQR policy achieves an $\mathcal{H}_{\infty}$ norm $\approx 9.26$ (with the optimal LQR cost $\approx 9.92$); in the two-channel case, the corresponding values are around $19.15$ and $4.65$, respectively. Therefore, our chosen $\beta$ values are small enough so that problem cannot be solved analytically for the two-channel case.

Table 1 summarizes the performance of all four approaches. The ARE row shows that solving (22b) is the most efficient and serves as the benchmark when $z_{2} = z_{\infty}$. From the PI row, we observe that the single-channel update in (28a) performs reliably, requiring only about $10$ times the runtime of solving (22b). In the two-channel setting, the policy iteration in (28b) converges for $\beta = 18$, maintaining feasibility throughout and achieving the optimal policy of, consistent with the LMI-based solution. However, for smaller values of $\beta$, (28b) fails to converge, an observation consistent with our conjecture. For $\beta = 6$, the iterates leave the feasible set $\mathcal{K}_{\beta}$ and the procedure terminates (e.g., at some iteration $t$, the $\mathcal{H}_{\infty}$ norm of $K_{t}$ exceeds $6$). For $\beta = 14$, the iterates remain feasible in $\mathcal{K}_{\beta}$ but fail to converge, instead exhibiting a periodic behavior suggesting of a limit cycle.

From the LMI row, we see that the global minimum of $J_{mix}$ is attained by solving the convex reformulation, with the gradient $\nabla J_{mix}$ of the resulting policy nearly zero. Overall, when successful, all three methods (ARE, PI, LMI) yield almost identical solutions. Finally, the HIFOO solver is less reliable for smaller $\beta$, often triggering warnings or failing to return feasible solutions. Even at $\beta = 18$, its performance (especially the $\mathcal{H}_{\infty}$ norm) deviates noticeably from the other methods. This is expected as HIFOO relies on nonsmooth local optimization and does not guarantee global optimality. In contrast, our result in Theorem 3 ensures that stationary points found via gradient-based methods are globally optimal.

Table 1: Comparison of different methods on Instance 0. Results for the two- and single-channel cases are shown under 2-ch and 1-ch subcolumns, respectively. A dash (–) indicates unavailable results. Bold values mark the best runtime among all methods.

### Higher-dimensional examples

We next consider three higher-dimensional examples, with policy matrices of sizes $15 \times 15$, $60 \times 60$, and $90 \times 90$, referred to as instances $1$, $2$, and $3$, respectively. The problem data for the single-channel formulations are adapted from \[45, Sec. 7.3\]. For the two-channel formulations, we retain the same $\mathcal{H}_{\infty}$ performance signals but specify the $\mathcal{H}_{2}$ performance with $Q_{2} = I$ and $R_{2} = {\frac{1}{4}R_{\infty}}$.

The minimum robustness level $\beta^{\ast}$ for instances $1$-$3$ are $\approx 0.067$, $0.098$, and $0.096$, respectively. Unlike the low-dimensional example (instance $0$), our focus here is on assessing the scalability of different methods. Accordingly, we test larger robustness levels, setting $\beta = 10$, $15$, and $20$. One can verify that all assumptions are satisfied.

Table 2 summarizes the results on the higher-dimensional examples. As shown in the ARE row, solving the Riccati equation remains highly efficient for the single-channel case, even at larger scales. The PI row demonstrates that the updates in remain effective as the problem size increases. Notably, the two-channel update (28b) converges across all instances, with the resulting policies exhibiting nearly vanishing gradients, which empirically supports our conjecture. This behavior suggests that (28b) enjoys an implicit regularization property, maintaining feasibility and achieving convergence when $\beta$ is sufficiently large.

The LMI row shows that the global minimum of $J_{mix}$ can be achieved by solving a convex reformulation. However, despite yielding policies with nearly zero gradients, the LMI method scales poorly: its runtimes for instance $2$ and $3$ are significantly longer than those of the analytical and policy iteration approaches. Overall, compared with the classical LMI-based methods, these results show that policy iteration can scale more favorably to large-scale problems.

Table 2: Comparison of different methods on Instance 1-3 (denoted I1-3). Results for two- and single-channel cases are shown under 2-ch and 1-ch subcolumns, respectively. A dash (-) indicates unavailable results. Bold values mark the best runtime.

## Conclusions

In this paper, we examine the nonconvex optimization landscape of mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ control. We characterize the feasible set and cost function, showing that despite nonconvexity, every stationary point is globally optimal. Our analysis, grounded in the $\mathtt{E}\mathtt{C}\mathtt{L}$ framework, further clarifies the role of strict versus non-strict Riccati inequalities in certifying global optimality and ensuring solvability of the convex reformulation. Several open questions are worth further investigation. An important one is to establish convergence guarantees for policy iteration in the general two-channel case, particularly for large $\beta$. Another is to design principled, scalable policy optimization algorithms for mixed $\mathcal{H}_{2}/\mathcal{H}_{\infty}$ design with provable performance guarantees.
