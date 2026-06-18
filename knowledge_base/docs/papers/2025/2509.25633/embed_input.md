<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Robust control seeks stabilizing policies that perform reliably under adversarial disturbances, with H_infinity control as a classical formulation. It is known that policy optimization of robust H_infinity control naturally lead to nonsmooth and nonconvex problems. This paper builds on recent advances in nonsmooth optimization to analyze discrete-time static output-feedback H_infinity control. We show that the H_infinity cost is weakly convex over any convex subset of a sublevel set. This structural property allows us to establish the first non-asymptotic deterministic convergence rate for the subgradient method under suitable assumptions. In addition, we prove a weak Polyak-Łojasiewicz (PL) inequality in the state-feedback case, implying that all stationary points are globally optimal. We finally present a few numerical examples to validate the theoretical results.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Ensuring robustness against unknown disturbances is crucial in control systems. In this context, $\mathcal{H}_{\infty}$ control has served as a cornerstone in robust control, which aims to design a stabilizing policy that minimizes the $\mathcal{H}_{\infty}$ norm of the closed-loop system. It has long been recognized that policy optimization for robust control naturally leads to nonconvex and nonsmooth optimization problems. While Riccati equation-based and LMI-based methods have been developed to circumvent these difficulties, they are typically limited to unstructured and model-based controller design. To address this, some recent works have proposed local search algorithms that directly optimize the original nonconvex nonsmooth problem. In particular, the authors in have implemented two official MATLAB solvers, hinfstruct and systune, for structured $\mathcal{H}_{\infty}$ control, with successful real-world applications (e.g., a space probe by the ESA ).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, owing to the inherent nonconvexity and nonsmoothness, the theoretical understanding remains limited, particularly regarding the non-asymptotic convergence of local search algorithms. The works proposed deterministic local search algorithms with some structure exploitation, but only admit at most asymptotic convergence. As a probabilistic approach, presented an open-source package HIFOO based on a randomized gradient sampling strategy, which was also limited to asymptotic guarantees. Recently, presented algorithms with a non-asymptotic convergence rate in a probabilistic sense using recent randomization-based techniques. However, such probabilistic guarantees are subject to a risk of failure, which may lead to concerns in safety-critical systems. To our knowledge, deterministic non-asymptotic convergence rates are still largely open for $\mathcal{H}_{\infty}$ optimization.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

This work addresses the aforementioned issue of convergence rates via weak convexity, and establishes a non-asymptotic convergence rate for the simple subgradient method. Recent studies demonstrate that weakly convex functions are arguably one of the broadest classes in nonsmooth nonconvex optimization that admits deterministic non-asymptotic rates, which cover various practical functions (e.g., convex, smooth, the composite of a convex function and a smooth map). Building on the recent advances, we first establish weak convexity of the $\mathcal{H}_{\infty}$ cost for discrete-time systems with static output-feedback. While previous works pointed out a relevant property, called lower-$C^{2}$, we demonstrate that the $\mathcal{H}_{\infty}$ cost is more structured than lower-$C^{2}$. With this property, we present a non-asymptotic convergence rate for the subgradient method under the assumption that the cost remains finite.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Further, we present a weak Polyak-Łojasiewicz (PL) inequality for the full state-feedback case, ensuring the global optimality of stationary points despite the nonconvexity.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Weak convexity. Since the stability constraint on feedback gains is inherently nonconvex, the standard definition of weak convexity is not applicable. Thus, we instead show $m$-weak convexity with some $m > 0$ over any convex subset of a sublevel set. Notably, the constant $m$ is uniform over the sublevel set, which allows for a straightforward extension of the standard weakly convex case;

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A weak Polyak-Lojasiewicz (PL) inequality. In the full state measurement case, we present a weak PL inequality, guaranteeing the global optimality of stationary points. Unlike the differentiability-based result, our proof applies to the nonsmooth $\mathcal{H}_{\infty}$ cost. The argument leverages an analogous idea to the extended convex lifting to analyze the nonsmooth $\mathcal{H}_{\infty}$ landscape beyond standard stationarity;

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The subgradient method. Building on weak convexity, we extend the convergence analysis of to the constrained nonconvex $\mathcal{H}_{\infty}$ optimization setting. In particular, we show that an $\epsilon$-inexact stationary point can be obtained after $T = {\mathcal{O}{({1/\epsilon^{4}})}}$ iterations, provided the cost remains bounded along the iterates. To our knowledge, this is the first deterministic complexity guarantee for subgradient methods in robust control.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of this paper is organized as follows. Section II formulates the $\mathcal{H}_{\infty}$ optimization problem and provides the problem statement. Then, Section III presents a review of landscape properties and our main results, such as the weak convexity and weak PL condition. In Section IV, we discuss the subgradient method. Section V provides numerical results. Finally, Section VI concludes this paper.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Robust $\\mathcal{H}_{\\infty}$ optimization with static output-feedback", "weight": 1.0} -->

Consider a discrete-time linear time-invariant system^11^1We focus on the class of discrete-time systems, since it is practical and might also be the simplest case in $\mathcal{H}_{\infty}$ optimization, due to the coercivity; see \[4, Lem. 3.2\] and \[7, Example 2.3\]. See also Remark 1. ‣ III-A Basic landscape properties ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods").

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-A Robust $\\mathcal{H}_{\\infty}$ optimization with static output-feedback", "weight": 1.0} -->

We consider $\mathbf{w} = {\{ w_{0},w_{1},\ldots\}}$ as an adversarial disturbance with bounded energy. Let $\ell_{2}^{k}$ be the set of square-summable (bounded energy) signals of dimension $k$, i.e.,

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-A Robust $\\mathcal{H}_{\\infty}$ optimization with static output-feedback", "weight": 1.0} -->

Throughout this paper, we make the following assumption

<!-- chunk {"id": "body-0014", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The system matrices $(A,B)$ are stabilizable, and $B_{w}$ and $C$ are row full-rank. The weight matrices $Q,R$ are positive definite, and the controller has access only to the output sequence $\mathbf{y}:={\{ y_{0},y_{1},\ldots\}}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Under Assumption 1, if full state measurements are available (i.e., $C = I_{n_{x}}$ in 1), it is well known that the optimal solution of 2 is a static state-feedback policy $u_{t} = {Kx_{t}}$, where $K \in {\mathbb{R}}^{n_{u} \times n_{x}}$ is a constant gain matrix. The general output-feedback $\mathcal{H}_{\infty}$ problem, however, is substantially more challenging. In this work, we restrict attention to linear static output-feedback policies of the form

<!-- chunk {"id": "body-0016", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

where $\rho{( \cdot )}$ denotes the spectral radius.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

For any $K \in \mathcal{K}$, the closed-loop system defined by 1 and 3 can be viewed as a bounded linear operator mapping disturbances $\mathbf{w} \in \ell_{2}^{n_{w}}$ to performance signals $\mathbf{z} \in \ell_{2}^{n_{x}}$. We denote this linear operator as ${\mathbb{T}}_{zw}{(K)}$, and define the $\ell_{2}\rightarrow\ell_{2}$ induced norm as

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Since ${\mathbb{T}}_{zw}{(K)}$ is linear, it is not difficult to see that problem 4 is equivalent to $\min_{K \in \mathcal{K}}{\|{{\mathbb{T}}_{zw}{(K)}}\|}^{2}$. This linear operator 6 is expressed in the time domain, and it also admits a frequency-domain representation via transfer functions. Denote transfer function matrix $\mathbf{T}_{zw}{(K,\omega)}$ from $\mathbf{w}$ to $\mathbf{z}$ as

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

where $\omega \in {\lbrack 0,{2\pi}\rbrack}$ is a frequency variable. Its $\mathcal{H}_{\infty}$ norm is

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

Problem 4 is thus often called $\mathcal{H}_{\infty}$ optimization with static feedback policies, which can be equivalently written as

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

where ${J{(K)}}:={\|{\mathbf{T}_{zw}{(K)}}\|}_{\mathcal{H}_{\infty}}$ is defined in 7. We remark that problem 4 minimizes $J{(K)}^{2}$, whereas 8 minimizes $J{(K)}$. Although the objective values differ by a square, the two problems clearly share the same set of optimal solutions.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B Problem statement", "weight": 1.0} -->

Robust $\mathcal{H}_{\infty}$ control is a cornerstone of control theory and has been studied extensively since the 1980s; see e.g., the classical textbook. In the state-feedback setting, standard approaches solve 8 either through Riccati-based iterative methods or via convex reformulations with Lyapunov variables. The static output-feedback is substantially more challenging, and no method is known to compute its globally optimal solution. Both Lyapunov- and Riccati-based approaches rely on explicit knowledge of the system model.

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B Problem statement", "weight": 1.0} -->

More recently, several works have explored direct optimization over the policy space $\mathcal{K}$ using local search methods. These approaches are typically more scalable, and some of them are better-suited to model-free settings. However, direct policy optimization for $\mathcal{H}_{\infty}$ control in 8 is inherently a nonsmooth and nonconvex problem, even in the state-feedback setting. Because of these difficulties, the early work provided no convergence-rate guarantees, while more recent studies established global optimality in the state-feedback case but relied on substantially more intricate algorithmic frameworks, often involving advanced randomized techniques.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B Problem statement", "weight": 1.0} -->

The main challenge is that the $\mathcal{H}_{\infty}$ cost function is both nonconvex and nonsmooth, with the nonsmoothness stemming from the maximization of the largest singular value in 7. While it is known that this function is subdifferentially regular, such regularity is too broad to yield efficient algorithmic guarantees. At the same time, the function is more structured than a generic nonsmooth, nonconvex objective: it is naturally a lower-$C^{2}$ function, as can be seen directly from its definition 7.

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B Problem statement", "weight": 1.0} -->

What additional structure (beyond subdifferential regularity) can be identified in the nonsmooth and nonconvex landscape of $\mathcal{H}_{\infty}$ policy optimization?

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B Problem statement", "weight": 1.0} -->

Given this structure, what are the simplest algorithms that can provably handle the nonconvex, nonsmooth nature of the $\mathcal{H}_{\infty}$ policy optimization problem?

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-B Problem statement", "weight": 1.0} -->

To address the first question, we will show that the $\mathcal{H}_{\infty}$ cost function admits a form of weak convexity, and in the state-feedback case, even satisfies a weak Polyak--Łojasiewicz (PL) condition. To address the second, we will demonstrate that classical first-order methods, such as the simple subgradient method, can achieve deterministic non-asymptotic convergence rates that match the best-known complexity for weakly convex functions, while avoiding randomized or overly complex procedures as.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Weak Convexity in $\\mathcal{H}_{\\infty}$ Optimization", "weight": 1.0} -->

We first summarize some basic landscape properties in 8, then establish the notion of weak convexity, and finally discuss fundamental properties of its stationary points.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A Basic landscape properties", "weight": 1.0} -->

We here summarize the basic landscape properties of 8.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Example 1 (Nonsmoothness of function $J$)", "weight": 1.0} -->

and thus the $\mathcal{H}_{\infty}$ cost can be obtained explicitly as

<!-- chunk {"id": "body-0031", "role": "body", "section": "Example 1 (Nonsmoothness of function $J$)", "weight": 1.0} -->

The function $J$ is clearly nonsmooth at $k = {- 1}$, as illustrated in Figure 1(a). Moreover, ${J{(k)}}\rightarrow\infty$ as $k\rightarrow 0$ or $k\rightarrow{- 2}$, which demonstrates the coercivity property.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Example 1 (Nonsmoothness of function $J$)", "weight": 1.0} -->

with $Q = {{diag}{(1,10^{- 3})}}$ and $R = 1$. From the classical $\mathcal{H}_{\infty}$ theory, we can compute the optimal value of $J{(K)}$ to be $J^{\ast} \approx 8.327$. We plot the function $J$ for $K = {\lbrack k_{1},k_{2}\rbrack}$ in Figure 1(b). We can see nonsmooth points on the landscape.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Example 2 (Nonconvexity of domain $\\mathcal{K}$ and function $J$)", "weight": 1.0} -->

For this system, the static output-feedback gain is of the form $K = {\lbrack k_{1},k_{2}\rbrack}$. When $\alpha \approx 0.05 \sim 0.13$, the feasible region $\mathcal{K}$ is disconnected, which directly leads to the nonconvex landscape. We plot set $\mathcal{K}$ and the function $J$ for $\alpha = 0.13$ in Figure 1(c) and Figure 1(d), respectively.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 1 ($\\mathcal{H}_{\\infty}$ optimization in continuous-time systems)", "weight": 1.0} -->

The continuous-time counterpart of 8 is likewise nonsmooth and nonconvex. The set of stabilizing gains remains nonconvex, is path-connected when $C = I_{n_{x}}$, and can be path-disconnected in general. However, unlike the discrete-time case, the coercivity of $J$ does not necessarily hold in continuous time (see \[7, Example 2.3\]). As a result, its sublevel sets may fail to be compact, and it is unclear whether $J$ is $\beta_{\nu}$-Lipschitz continuous on such sets. $\square$

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B Lower-$C^{2}$ and weak convexity", "weight": 1.0} -->

We now establish a key technical result: although the $\mathcal{H}_{\infty}$ cost $J$ is nonconvex, it is in fact weakly convex. A precise statement will be given later in Theorem 1. ‣ III-B Lower-C² and weak convexity ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"). Recall that a function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is $\rho$-weakly convex if the function $x\mapsto{{f{(x)}} + {\frac{\rho}{2}{\| x\|}^{2}}}$ is convex. Weak convexity provides a broad framework that subsumes convex, smooth, and many composite nonconvex functions, and enables principled first-order algorithm design.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-B Lower-$C^{2}$ and weak convexity", "weight": 1.0} -->

Another related notion is that of lower-$C^{2}$ functions. Roughly speaking, a lower-$C^{2}$ function may be nonsmooth, but its nonsmoothness arises solely from taking a supremum of smooth $C^{2}$ components, making it significantly more structured than generic nonsmooth functions. Note that a function $f:{\mathcal{D}\rightarrow{\mathbb{R}}}$ is of class $C^{2}$ if it is twice differentiable on its open domain $\mathcal{D}$ and both $\nabla f$ and $\nabla^{2}f$ are continuous. The formal definition of lower-$C^{2}$ functions is as follows.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Example 3 (Weak convexity)", "weight": 1.0} -->

This function is slightly different from the $\mathcal{H}_{\infty}$ cost 7, as it has no frequency variable. However, it captures the essential composition of $\sigma_{\max}$ with a smooth function. Indeed, on any bounded interval $V \subset {({- 1},\infty)}$, the mapping $c{( \cdot )}$ is $L_{V}$-smooth for some $L_{V} > 0$, and thus $f{( \cdot )}$ is $m_{V}$-weakly convex on $V$ with some $m_{V} > 0$. To illustrate, we plot $f{(x)}$ and ${f{(x)}} + {\frac{5}{4}{\|{x - 1}\|}^{2}}$ on $V = {\lbrack 0,5\rbrack}$ in Figure 2.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Example 3 (Weak convexity)", "weight": 1.0} -->

‣ III-B Lower-C² and weak convexity ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"). Clearly, $f{(x)}$ is convexified by adding a quadratic perturbation $\frac{5}{4}{\|{x - 1}\|}^{2}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-C Stationary points and weak PL property", "weight": 1.0} -->

We next analyze the stationary points of $\mathcal{H}_{\infty}$ cost $J$. As is typical in nonconvex optimization, spurious stationary points such as local minima and saddle points may arise in the general output-feedback $\mathcal{H}_{\infty}$ setting.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Example 4 (Saddle points)", "weight": 1.0} -->

Consider the problem data in Example 2. ‣ III-A Basic landscape properties ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"). For $\alpha = 0.13$, the set $\mathcal{K}$ consists of two disconnected components (see Figure 1(c)). At $\alpha = 0.14$, these components merge, and $\mathcal{K}$ becomes connected, as shown in Figure 3(a). In this case, we observe a saddle point in $J$ (see Figure 3(b)), as well as at least one local minimum.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Example 4 (Saddle points)", "weight": 1.0} -->

In the full-state measurement case ($C = I_{n_{x}}$), the $\mathcal{H}_{\infty}$ optimization exhibits a much more tractable landscape, with a connected feasible region and convex-like shape as Figures 1(a) and 1(b) ‣ Figure 1 ‣ III-A Basic landscape properties ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"). Indeed, we can establish a weak PL condition that ensures the global optimality of stationary points.

<!-- chunk {"id": "body-0042", "role": "body", "section": "III-D Proof of Theorem 1. ‣ III-B Lower-C² and weak convexity ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods\")", "weight": 1.0} -->

To establish Theorem 1. ‣ III-B Lower-C² and weak convexity ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"), we first rewrite the $\mathcal{H}_{\infty}$ cost as the composition of $\sigma_{\max}{( \cdot )}$ and a real-valued mapping using Lemma 4 below, which follows from a famous fact \[29, Exercise 4.42\] in complex SDPs. We thereby identify the weakly convex constant $m_{\nu} > 0$ via the compactness of $\mathcal{K}_{\nu}$ from Lemma 1. The proof of Lemma 4 is presented in Section -A due to the page limit.

<!-- chunk {"id": "body-0043", "role": "body", "section": "The Subgradient Method", "weight": 1.0} -->

In this section, we discuss the subgradient method to solve the $\mathcal{H}_{\infty}$ optimization 8. Thanks to the weak convexity in Theorem 1. ‣ III-B Lower-C² and weak convexity ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"), we provide a non-asymptotic convergence rate under mild assumptions, by adapting the recent result.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-A The subgradient method", "weight": 1.0} -->

Given an initial point $K_{0} \in \mathcal{K}$, the subgradient method simply follows the update below

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-A The subgradient method", "weight": 1.0} -->

where $\partial{J{(K)}}$ is the Clarke subdifferential of $J{( \cdot )}$ at $K \in \mathcal{K}$. This is arguably the simplest algorithm for nonsmooth nonconvex optimization. Thanks to its simplicity, we may implement in a model-free manner relatively easily, only with a subgradient oracle.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-B Non-asymptotic convergence guarantees", "weight": 1.0} -->

Despite its simplicity, the subgradient method is classically known to achieve sublinear convergence only for convex and/or smooth problems. Its behavior in the nonsmooth nonconvex setting was far less understood because (i) stationary concepts in convex and/or smooth cases can no longer be used, and (ii) the subgradient update 17 does not guarantee monotonic decrease of the cost; it is indeed possible even in the nonsmooth convex case that ${J{(K_{t + 1})}} > {J{(K_{t})}}$ for any $\alpha_{t} > 0$. Recently, established the first non-asymptotic rate for minimizing unconstrained weakly convex functions. In this work, we extend their analysis to the $\mathcal{H}_{\infty}$ optimization 8 involving *a nonconvex stabilizing constraint* $\mathcal{K}$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-B Non-asymptotic convergence guarantees", "weight": 1.0} -->

One key concept is the Moreau envelope, which allows for quantifying the performance of 17 even in the absence of a function value decrease.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark 2", "weight": 1.0} -->

Theorem 3 presents a non-asymptotic convergence rate for the subgradient method 17. Notice that the boundedness of the cost is directly assumed, as it is often empirically true for sufficiently small $\{\alpha_{t}\}$ but not formally guaranteed in 17. Under this assumption, we can ensure the feasibility ${\{ K_{t}\}} \subset \mathcal{K}$ by the coercivity in Lemma 1, bypassing the nonconvex constraint set $\mathcal{K}$ through a careful choice of the parameter $\rho$. To alleviate the assumption on the cost, one may use other algorithms that can generate a descent direction (e.g., the proximal bundle method ). We leave it as our future work. $\square$

<!-- chunk {"id": "body-0049", "role": "body", "section": "Numerical results", "weight": 1.0} -->

Here, we run the subgradient method 17 with fixed step sizes $\alpha_{t} = \alpha^{1}$ or $\alpha^{2}$, where ${(\alpha^{1},\alpha^{2})} = {(10^{- 3},10^{- 4})}$, for both full state-feedback and static output-feedback cases. The following results demonstrate the effectiveness of the subgradient method 17 and validate our theoretical results.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Numerical results", "weight": 1.0} -->

Full state-feedback. For the system 10. ‣ III-A Basic landscape properties ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods") in Example 1. ‣ III-A Basic landscape properties ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"), we test 17 with different parameter choices. Specifically, we use $K_{0} = K_{0}^{1} = {\lbrack 0,{- 1.9}\rbrack}$ or $K_{0}^{2} = {\lbrack 0.2,{- 2}\rbrack}$. We plot the simulation result in Figure 4(a), where the vertical axis shows the best relative objective residual $\min_{t}{{|{{J{(K_{t})}} - J^{\star}}|}/J^{\star}}$ at $t$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Numerical results", "weight": 1.0} -->

In all the cases, the subgradient method generates feasible iterates, which implies that the assumptions in Theorem 3 are satisfied. In addition, as expected, we obtained a globally optimal solution for both initial conditions with favorable accuracy, especially when $\alpha_{t} = \alpha^{2}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Numerical results", "weight": 1.0} -->

Static output-feedback. For Example 4. ‣ III-C Stationary points and weak PL property ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"), we similarly run 17 with four different choices of the initial condition and step size. In particular, we use $K_{0} = K_{0}^{1}$ or $K_{0}^{2}$ with ${K_{0}^{1} = {\lbrack 0,0\rbrack}},{K_{0}^{2} = {\lbrack{- 5},{- 2}\rbrack}}$. The simulation result is presented in Figure 4(b). It can be seen that the feasibility is satisfied in all the cases. Regarding the performance, the cost value converged to a smaller value in the case of $K_{0} = K_{0}^{1}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Numerical results", "weight": 1.0} -->

In addition, when $K_{0} = K_{0}^{2}$, we observe that the subgradient also converged nearly to a stationary point. When $K_{0} = K_{0}^{1}$ in Figure 4(b), the magnitude of the subgradient remained larger despite the smaller cost value. This is due to a zigzagging behavior around a stationary point and may happen when it is nonsmooth. For example, ${f{(x)}} = {|x|}$ takes the minimum at $x = 0$, but the origin is nonsmooth and ${\partial{f{}}} = {\lbrack{- 1},1\rbrack} \neq {\{ 0\}}$, which may lead to such behavior.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This study addressed the $\mathcal{H}_{\infty}$ optimization problem for discrete-time linear systems with static output-feedback. We first proved the weak convexity and further established the weak PL condition in the full state-feedback case. Then, we also discussed the subgradient method from a weak convexity perspective, presenting the first non-asymptotic convergence rate. The numerical simulations validated our theoretical analysis and demonstrated the effectiveness of the subgradient method. Our future work includes alleviating the assumption of the cost value boundedness in the convergence rate result, for example, through the proximal bundle method.
