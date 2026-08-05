<!-- arxiv-full-text:v1 {"arxiv_id": "2509.25633", "source": "arxiv-html"} -->

## Introduction

Ensuring robustness against unknown disturbances is crucial in control systems. In this context, $\mathcal{H}_{\infty}$ control has served as a cornerstone in robust control, which aims to design a stabilizing policy that minimizes the $\mathcal{H}_{\infty}$ norm of the closed-loop system. It has long been recognized that policy optimization for robust control naturally leads to nonconvex and nonsmooth optimization problems. While Riccati equation-based and LMI-based methods have been developed to circumvent these difficulties, they are typically limited to unstructured and model-based controller design. To address this, some recent works have proposed local search algorithms that directly optimize the original nonconvex nonsmooth problem. In particular, the authors in have implemented two official MATLAB solvers, hinfstruct and systune, for structured $\mathcal{H}_{\infty}$ control, with successful real-world applications (e.g., a space probe by the ESA ).

However, owing to the inherent nonconvexity and nonsmoothness, the theoretical understanding remains limited, particularly regarding the non-asymptotic convergence of local search algorithms. The works proposed deterministic local search algorithms with some structure exploitation, but only admit at most asymptotic convergence. As a probabilistic approach, presented an open-source package HIFOO based on a randomized gradient sampling strategy, which was also limited to asymptotic guarantees. Recently, presented algorithms with a non-asymptotic convergence rate in a probabilistic sense using recent randomization-based techniques . However, such probabilistic guarantees are subject to a risk of failure, which may lead to concerns in safety-critical systems. To our knowledge, deterministic non-asymptotic convergence rates are still largely open for $\mathcal{H}_{\infty}$ optimization.

This work addresses the aforementioned issue of convergence rates via weak convexity, and establishes a non-asymptotic convergence rate for the simple subgradient method. Recent studies demonstrate that weakly convex functions are arguably one of the broadest classes in nonsmooth nonconvex optimization that admits deterministic non-asymptotic rates, which cover various practical functions (e.g., convex, smooth, the composite of a convex function and a smooth map). Building on the recent advances, we first establish weak convexity of the ${\mathcal{H}_{\infty}}$ cost for discrete-time systems with static output-feedback. While previous works pointed out a relevant property, called lower-$C^{2}$, we demonstrate that the ${\mathcal{H}_{\infty}}$ cost is more structured than lower-$C^{2}$. With this property, we present a non-asymptotic convergence rate for the subgradient method under the assumption that the cost remains finite. Further, we present a weak Polyak-Łojasiewicz (PL) inequality for the full state-feedback case, ensuring the global optimality of stationary points despite the nonconvexity.

Our major technical contributions are threefold: Weak convexity. Since the stability constraint on feedback gains is inherently nonconvex, the standard definition of weak convexity is not applicable. Thus, we instead show $m$-weak convexity with some $m>0$ over any convex subset of a sublevel set. Notably, the constant $m$ is uniform over the sublevel set, which allows for a straightforward extension of the standard weakly convex case; A weak Polyak-Lojasiewicz (PL) inequality. In the full state measurement case, we present a weak PL inequality, guaranteeing the global optimality of stationary points. Unlike the differentiability-based result, our proof applies to the nonsmooth $\mathcal{H}_{\infty}$ cost. The argument leverages an analogous idea to the extended convex lifting to analyze the nonsmooth $\mathcal{H}_{\infty}$ landscape beyond standard stationarity; The subgradient method. Building on weak convexity, we extend the convergence analysis of to the constrained nonconvex $\mathcal{H}_{\infty}$ optimization setting. In particular, we show that an $\epsilon$-inexact stationary point can be obtained after $T=\mathcal{O}(1/\epsilon^{4})$ iterations, provided the cost remains bounded along the iterates. To our knowledge, this is the first deterministic complexity guarantee for subgradient methods in robust control.

The remainder of this paper is organized as follows. Section II formulates the ${\mathcal{H}_{\infty}}$ optimization problem and provides the problem statement. Then, Section III presents a review of landscape properties and our main results, such as the weak convexity and weak PL condition. In Section IV, we discuss the subgradient method. Section V provides numerical results. Finally, Section VI concludes this paper.

## Preliminaries and Problem Statement

### II-A Robust $\mathcal{H}_{\infty}$ optimization with static output-feedback

Consider a discrete-time linear time-invariant system^11^1We focus on the class of discrete-time systems, since it is practical and might also be the simplest case in ${\mathcal{H}_{\infty}}$ optimization, due to the coercivity; see \[4, Lem. 3.2\] and \[7, Example 2.3\]. See also Remark 1. ‣ III-A Basic landscape properties ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"). where $x_{t}\in\mathbb{R}^{n_{x}}$ is the system state, $u_{t}\in\mathbb{R}^{n_{u}}$ is the control input, $y_{t}\in\mathbb{R}^{n_{y}}$ is the output measurement, and $w_{t}\in\mathbb{R}^{n_{w}}$ is the disturbance, respectively. The system matrices are $A\in\mathbb{R}^{n_{x}\times n_{x}},B\in\mathbb{R}^{n_{x}\times n_{u}}$, $B_{w}\in\mathbb{R}^{n_{x}\times n_{w}}$, and $C\in\mathbb{R}^{n_{y}\times n_{x}}$. The system's initial condition is fixed as $x_{0}=0$.

We consider $\mathbf{w}=\{w_{0},w_{1},\ldots\}$ as an adversarial disturbance with bounded energy. Let $\ell^{k}_{2}$ be the set of square-summable (bounded energy) signals of dimension $k$, i.e., Robust $\mathcal{H}_{\infty}$ control aims to select the control sequence $\mathbf{u}=\{u_{0},u_{1},\ldots\}$ to minimize the quadratic performance $\sum_{t=0}^{\infty}(x_{t}^{{\mathsf{T}}}Qx_{t}+u_{t}^{{\mathsf{T}}}Ru_{t})$ against the worst disturbance of bounded energy $\|\mathbf{w}\|_{2}\leq 1$. Without loss of generality, we consider the energy bound on $\mathbf{w}$ to be 1, and we can formulate robust $\mathcal{H}_{\infty}$ control with any $\mathbf{w}\in\ell^{n_{w}}_{2}$. We thus consider the following min-max robust control problem Throughout this paper, we make the following assumption

### Assumption 1

The system matrices $(A,B)$ are stabilizable, and $B_{w}$ and $C$ are row full-rank. The weight matrices $Q,R$ are positive definite, and the controller has access only to the output sequence $\mathbf{y}:=\{y_{0},y_{1},\ldots\}$.

Under Assumption 1, if full state measurements are available (i.e., $C=I_{n_{x}}$ in 1), it is well known that the optimal solution of 2 is a static state-feedback policy $u_{t}=Kx_{t}$, where $K\in\mathbb{R}^{n_{u}\times n_{x}}$ is a constant gain matrix. The general output-feedback $\mathcal{H}_{\infty}$ problem, however, is substantially more challenging. In this work, we restrict attention to linear static output-feedback policies of the form and study the following policy optimization problem: | | $\displaystyle\min_{K\in\mathbb{R}^{n_{u}\times n_{y}}}\;\max_{\|\mathbf{w}\|_{2}\leq 1}$ | $\displaystyle\sum_{t=0}^{\infty}(x_{t}^{{\mathsf{T}}}Qx_{t}+u_{t}^{{\mathsf{T}}}Ru_{t})$ | | \(4\) | | | subject to | $\displaystyle\text{\lx@cref{creftypeplural~refnum}{eq:dynamic} and\nobreakspace\lx@cref{refnum}{eq:static-policies}},\,x_{0}=0.$ | | | Given any feedback gain $K\in\mathbb{R}^{n_{u}\times n_{y}}$, the closed-loop dynamics from 1 and 3 becomes $x_{t}\!=\!(A+BKC)x_{t}+B_{w}w_{t},\,x_{0}=0.$ We denote the set of stabilizing gains as where $\rho(\cdot)$ denotes the spectral radius.

### Assumption 2

The set $\mathcal{K}$ is non-empty.

If $K\in\mathcal{K}$, then the state trajectory $\mathbf{x}=\{x_{0},x_{1},\ldots\}$ belongs to $\ell_{2}^{n_{x}}$ for any bounded disturbance $\mathbf{w}\in\ell_{2}^{n_{w}}$. Let a performance signal be $z_{t}=(Q+C^{{\mathsf{T}}}K^{{\mathsf{T}}}RKC)^{1/2}x_{t}$ and $\mathbf{z}=\{z_{0},z_{1},z_{2},\ldots\}$. Then, we have For any $K\in\mathcal{K}$, the closed-loop system defined by 1 and 3 can be viewed as a bounded linear operator mapping disturbances $\mathbf{w}\in\ell_{2}^{n_{w}}$ to performance signals $\mathbf{z}\in\ell_{2}^{n_{x}}$. We denote this linear operator as $\mathbb{T}_{zw}(K)$, and define the $\ell_{2}\to\ell_{2}$ induced norm as Since $\mathbb{T}_{zw}(K)$ is linear, it is not difficult to see that problem 4 is equivalent to $\min_{K\in\mathcal{K}}\,\|\mathbb{T}_{zw}(K)\|^{2}$. This linear operator 6 is expressed in the time domain, and it also admits a frequency-domain representation via transfer functions. Denote transfer function matrix $\mathbf{T}_{zw}(K,\omega)$ from $\mathbf{w}$ to $\mathbf{z}$ as where $\omega\in[0,2\pi]$ is a frequency variable. Its $\mathcal{H}_{\infty}$ norm is where $\sigma_{\max}(\cdot)$ is the maximum singular value. The $\ell_{2}\to\ell_{2}$ induced norm coincides with the $\mathcal{H}_{\infty}$ norm \[1, Th. 4.4\], i.e., $\|\mathbb{T}_{zw}(K)\|\!=\!\|{\mathbf{T}}_{zw}(K)\|_{{\mathcal{H}_{\infty}}},\,\forall K\in\mathcal{K}.$ Problem 4 is thus often called $\mathcal{H}_{\infty}$ optimization with static feedback policies, which can be equivalently written as where $J(K):=\|{\mathbf{T}}_{zw}(K)\|_{{\mathcal{H}_{\infty}}}$ is defined in 7. We remark that problem 4 minimizes $J(K)^{2}$, whereas 8 minimizes $J(K)$. Although the objective values differ by a square, the two problems clearly share the same set of optimal solutions.

### II-B Problem statement

Robust $\mathcal{H}_{\infty}$ control is a cornerstone of control theory and has been studied extensively since the 1980s; see e.g., the classical textbook. In the state-feedback setting, standard approaches solve 8 either through Riccati-based iterative methods or via convex reformulations with Lyapunov variables. The static output-feedback is substantially more challenging, and no method is known to compute its globally optimal solution. Both Lyapunov- and Riccati-based approaches rely on explicit knowledge of the system model.

More recently, several works have explored direct optimization over the policy space $\mathcal{K}$ using local search methods. These approaches are typically more scalable, and some of them are better-suited to model-free settings. However, direct policy optimization for $\mathcal{H}_{\infty}$ control in 8 is inherently a nonsmooth and nonconvex problem, even in the state-feedback setting. Because of these difficulties, the early work provided no convergence-rate guarantees, while more recent studies established global optimality in the state-feedback case but relied on substantially more intricate algorithmic frameworks, often involving advanced randomized techniques.

The main challenge is that the $\mathcal{H}_{\infty}$ cost function is both nonconvex and nonsmooth, with the nonsmoothness stemming from the maximization of the largest singular value in 7. While it is known that this function is subdifferentially regular, such regularity is too broad to yield efficient algorithmic guarantees. At the same time, the function is more structured than a generic nonsmooth, nonconvex objective: it is naturally a lower-$C^{2}$ function, as can be seen directly from its definition 7.

This observation raises two central questions in this paper: What additional structure (beyond subdifferential regularity) can be identified in the nonsmooth and nonconvex landscape of $\mathcal{H}_{\infty}$ policy optimization?

Given this structure, what are the simplest algorithms that can provably handle the nonconvex, nonsmooth nature of the $\mathcal{H}_{\infty}$ policy optimization problem?

To address the first question, we will show that the $\mathcal{H}_{\infty}$ cost function admits a form of weak convexity, and in the state-feedback case, even satisfies a weak Polyak--Łojasiewicz (PL) condition. To address the second, we will demonstrate that classical first-order methods, such as the simple subgradient method, can achieve deterministic non-asymptotic convergence rates that match the best-known complexity for weakly convex functions, while avoiding randomized or overly complex procedures as .

## Weak Convexity in ${\mathcal{H}_{\infty}}$ Optimization

We first summarize some basic landscape properties in 8, then establish the notion of weak convexity, and finally discuss fundamental properties of its stationary points.

### III-A Basic landscape properties

We here summarize the basic landscape properties of 8.

Figure 1: Nonconvex and nonsmooth landscape in ℋ∞ optimization. (a)–(b) Nonsmoothness of the cost functions J in Example 1; (c) Disconnectivity of 𝒦 in Example 2 with α = 0.13; (d) Nonconvexity of J in Example 2 with α = 0.13.

### Lemma 1

Suppose Assumptions 1 and 2 hold. Consider the $\mathcal{H}_{\infty}$ optimization problem with static linear policies in 8. Then the following statements hold: The stabilizing set $\mathcal{K}$ is open and, in general, nonconvex. If full state information is available (i.e., $C=I_{n_{x}}$), the set $\mathcal{K}$ is always path-connected, but in the general output-feedback case, it can be disconnected.

The $\mathcal{H}_{\infty}$ cost function $J:\mathcal{K}\to\mathbb{R}_{+}$ is coercive: The function $J$ is generally nonsmooth and nonconvex.

On any sublevel set $\mathcal{K}_{\nu}:=\{K\in\mathcal{K}\mid J(K)\leq\nu\}$, $J$ is $\beta_{\nu}$-Lipschitz continuous for some constant $\beta_{\nu}>0$.

These landscape properties are known in the literature; see, e.g.,. We do not reproduce the proofs here, but instead highlight several insights and illustrative examples.

First, it is straightforward to construct examples showing that $\mathcal{K}$ is nonconvex (as Examples 2. ‣ III-A Basic landscape properties ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods") and 4. ‣ III-C Stationary points and weak PL property ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods") below). When $C=I_{n_{x}}$, path-connectivity of $\mathcal{K}$ follows from an equivalent convex reformulation, since convex sets are always path-connected. Second, the coercivity of $J$ can be established by deriving a global quadratic lower bound; see \[4, Lem. 3.2\] for details. This property is crucial because it ensures that each sublevel set $\mathcal{K}_{\nu}:=\{K\in\mathcal{K}\mid J(K)\leq\nu\}$ is compact. Third, $J$ is naturally nonconvex since its domain $\mathcal{K}$ is already nonconvex. Its nonsmoothness arises from two sources in the definition 7: (i) the maximum singular value of a complex matrix, and (ii) the maximization over the frequency variable. Finally, while the local Lipschitz continuity of $J$ is well known, identifying a uniform Lipschitz constant on a sublevel set $\mathcal{K}_{\nu}$ is more subtle. Previous works such as \[3, Th. 5\] and \[4, Sec. 3\] assume this $\beta_{\nu}$-Lipschitz property directly. In fact, it can be rigorously established by explicitly characterizing the Clarke subdifferential of $J$.

We next present two examples to illustrate Lemma 1.

### Example 1 (Nonsmoothness of function $J$)

with $u_{k}=kx_{k}$ and $Q=R=1$. It is clear that $\mathcal{K}=\{k\mid|1+k|<1\}=(-2,0).$ It is easy to see and thus the ${\mathcal{H}_{\infty}}$ cost can be obtained explicitly as The function $J$ is clearly nonsmooth at $k=-1$, as illustrated in Figure 1(a). Moreover, $J(k)\to\infty$ as $k\to 0$ or $k\to-2$, which demonstrates the coercivity property.

Consider another state-feedback system with $Q=\mathrm{diag}(1,10^{-3})$ and $R=1$. From the classical $\mathcal{H}_{\infty}$ theory, we can compute the optimal value of $J(K)$ to be $J^{*}\approx 8.327$. We plot the function $J$ for $K=[k_{1},k_{2}]$ in Figure 1(b). We can see nonsmooth points on the landscape.

### Example 2 (Nonconvexity of domain $\mathcal{K}$ and function $J$)

Consider the following problem data: For this system, the static output-feedback gain is of the form $K=[k_{1},k_{2}]$. When $\alpha\approx 0.05\sim 0.13$, the feasible region $\mathcal{K}$ is disconnected, which directly leads to the nonconvex landscape. We plot set $\mathcal{K}$ and the function $J$ for $\alpha=0.13$ in Figure 1(c) and Figure 1(d), respectively.

### Remark 1 ($\mathcal{H}_{\infty}$ optimization in continuous-time systems)

The continuous-time counterpart of 8 is likewise nonsmooth and nonconvex. The set of stabilizing gains remains nonconvex, is path-connected when $C=I_{n_{x}}$, and can be path-disconnected in general. However, unlike the discrete-time case, the coercivity of $J$ does not necessarily hold in continuous time (see \[7, Example 2.3\]). As a result, its sublevel sets may fail to be compact, and it is unclear whether $J$ is $\beta_{\nu}$-Lipschitz continuous on such sets. $\square$

### III-B Lower-$C^{2}$ and weak convexity

We now establish a key technical result: although the $\mathcal{H}_{\infty}$ cost $J$ is nonconvex, it is in fact weakly convex. A precise statement will be given later in Theorem 1. ‣ III-B Lower-C² and weak convexity ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"). Recall that a function $f:\mathbb{R}^{n}\to\mathbb{R}$ is $\rho$-weakly convex if the function $x\mapsto f(x)+\frac{\rho}{2}\|x\|^{2}$ is convex. Weak convexity provides a broad framework that subsumes convex, smooth, and many composite nonconvex functions, and enables principled first-order algorithm design.

Another related notion is that of lower-$C^{2}$ functions. Roughly speaking, a lower-$C^{2}$ function may be nonsmooth, but its nonsmoothness arises solely from taking a supremum of smooth $C^{2}$ components, making it significantly more structured than generic nonsmooth functions. Note that a function $f:\mathcal{D}\to\mathbb{R}$ is of class $C^{2}$ if it is twice differentiable on its open domain $\mathcal{D}$ and both $\nabla f$ and $\nabla^{2}f$ are continuous. The formal definition of lower-$C^{2}$ functions is as follows.

### Definition 1 (Lower-$C^{2}$ )

We say a function $f:\mathcal{D}\to\mathbb{R}$, defined on an open domain $\mathcal{D}\subset\mathbb{R}^{n}$, is lower-$C^{2}$, if for each $\bar{x}\in\mathcal{D}$, there exist a neighborhood $V$ of $\bar{x}$, a compact set $\mathcal{T}$, and a mapping $\varphi:\mathcal{T}\times V\to\mathbb{R}$ such that where, for each $t\in\mathcal{T}$, the function $\varphi(t,\cdot)$ is $C^{2}$ in $x$, and the mappings $\varphi(\cdot,\cdot)$, $\nabla_{x}\varphi(\cdot,\cdot)$, and $\nabla_{x}^{2}\varphi(\cdot,\cdot)$ are jointly continuous on $(t,x)\in\mathcal{T}\times V$.

Note that the smooth functions $\varphi(t,\cdot)$ in 11. ‣ III-B Lower-C² and weak convexity ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods") may depend on the point $\bar{x}$. Thus, a lower-$C^{2}$ function can be *locally* represented as the maximum of a family of smooth $C^{2}$ functions. We will show that the $\mathcal{H}_{\infty}$ cost $J$ is lower-$C^{2}$.

Before doing so, let us recall some simple examples. First, any quadratic function is lower-$C^{2}$, and so is the maximum of finitely many quadratics^22^2In this case, we regard $\mathcal{T}$ as a subset of a discrete topological space., e.g., $f(x)=\max_{t\in\{1,\ldots,p\}}f_{t}(x)$. Second, the maximum eigenvalue function of symmetric matrices $\lambda_{\max}(\cdot)$ is also lower-$C^{2}$, as where each component $\varphi(u,X)=u^{\top}Xu$ is linear in $X$ and hence $C^{2}$. Finally, the maximum singular value of a real matrix $Y\in\mathbb{R}^{p\times m}$ is lower-$C^{2}$, because where where $\Re(\cdot)$ represents the real part and, each component $\varphi(u,v,Y)=\Re({u^{{\mathsf{H}}}}Yv)$ is linear (hence $C^{2}$) in $Y$. These examples illustrate that many spectral functions naturally fall into the lower-$C^{2}$ class, which enables our analysis of the $\mathcal{H}_{\infty}$ cost below; recall its definition 7.

Formally, we have the following result.

### Lemma 2

Suppose Assumptions 1 and 2 hold. Consider the $\mathcal{H}_{\infty}$ cost function $J:\mathcal{K}\to\mathbb{R}_{+}$ defined in 8. Then the following properties hold: $J$ is *locally weakly convex*: for every $K_{0}\in\mathcal{K}$, there exist constants $m>0$ and $r>0$ such that is convex over $\mathbb{B}_{r}(K_{0}):=\{K\mid\|K-K_{0}\|_{F}\leq r\}$. $J$ is *subdifferentially regular*, i.e., its directional derivative coincides with its Clarke directional derivative at every point.

### Proof

Similar to 13, we can rewrite the $\mathcal{H}_{\infty}$ cost as Define $\varphi(\omega,u,v,K):=\Re\!\left[v^{{\mathsf{H}}}{\mathbf{T}}_{zw}(K,\omega)u\right].$ It is easy to verify that $\varphi$ is analytic in $K$ over the open set $\mathcal{K}$, and jointly continuous in $(\omega,u,v,K)$ on $[0,2\pi]\times\{u\in\mathbb{C}^{n_{w}}\mid\!\|u\|=1\}\times\{v\in\mathbb{C}^{n_{x}+n_{u}}\mid\!\|v\|=1\}\times\mathcal{K}$. Hence, we may represent $J$ as where $\Theta:=[0,2\pi]\times\{u\in\mathbb{C}^{n_{w}}:\|u\|=1\}\times\{v\in\mathbb{C}^{n_{x}+n_{u}}:\|v\|=1\}$ is compact. By Definition 1. ‣ III-B Lower-C² and weak convexity ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"), it follows that $J$ is lower-$C^{2}$. The local weak convexity 2) and subdifferential regularity 3) follow from \[23, Th. 10.31 and Th. 10.33\]. ∎ The proof above is inspired by the continuous-time case \[22, Lem. 9\]. Note that the local weak convexity 14 is a natural property of lower $C^{2}$ functions \[23, Th. 10.33\]. However, the weak convexity constant $m$ may depend on the point and its neighborhood, which may be hard to estimate.

It is worth noting that the smooth components in 12, 13 and 15 are *global*, in the sense that they do not vary with the choice of reference point $K$. This structure is considerably stronger than general lower-$C^{2}$ functions in Definition 1. ‣ III-B Lower-C² and weak convexity ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"). Consequently, we may anticipate better-behaved properties for the $\mathcal{H}_{\infty}$ cost than those established in Lemma 2. This is indeed the case: we can establish a uniform weak convexity constant over any convex subset in a sublevel set of $J$.

### Theorem 1 (Weak convexity)

Suppose Assumptions 1 and 2 hold. Consider the $\mathcal{H}_{\infty}$ cost function $J:\mathcal{K}\to\mathbb{R}_{+}$ defined in 8. Let $\nu>0$ and define a sublevel set $\mathcal{K}_{\nu}:=\{K\in\mathcal{K}\mid J(K)\leq\nu\}\neq\emptyset$. Then, for any nonempty convex subset $V\subset\mathcal{K}_{\nu}$, there exists a constant $m_{\nu}>0$ such that the function The proof is not difficult by recalling the fact that the composition of a convex function with an $L$-smooth function is weakly convex. In our case, the maximum singular value function $\sigma_{\max}(\cdot)$ is convex on $\mathbb{R}^{p\times n}$. We need to handle the complex transfer function and the maximization over the frequency variable $\omega$ in 7. For this, we first use a well-known result from complex SDPs \[29, Exercise 4.42\] to equivalently eliminate complex numbers in $f(\cdot,\omega):=\sigma_{\mathrm{max}}({\mathbf{T}}_{zw}(\cdot,\omega))$ for each fixed $\omega\in[0,2\pi]$. Then, since $\mathcal{K}_{\nu}$ is compact thanks to the coercivity, over any convex subset $V\subset\mathcal{K}_{\nu}$, we can view $f(\cdot,\omega)$ as a composition of a convex function with a real-valued $L_{\nu}$-smooth function with some $L_{\nu}>0$, which is thus $m_{\nu}$-weakly convex with some $m_{\nu}>0$ independent of $\omega$. Therefore, we have $J(K)+\frac{m_{\nu}}{2}\|K\|_{F}^{2}=\max_{\omega\in[0,2\pi]}\{f(K,\omega)+\frac{m_{\nu}}{2}\|K\|_{F}^{2}\}$ is convex on any convex subset of $\mathcal{K}_{\nu}$. A detailed proof is given in Section III-D.

### Example 3 (Weak convexity)

Consider $f:(-1,\infty)\to\mathbb{R}_{+}$: This function is slightly different from the $\mathcal{H}_{\infty}$ cost 7, as it has no frequency variable. However, it captures the essential composition of $\sigma_{\max}$ with a smooth function. Indeed, on any bounded interval $V\subset(-1,\infty)$, the mapping $c(\cdot)$ is $L_{V}$-smooth for some $L_{V}>0$, and thus $f(\cdot)$ is $m_{V}$-weakly convex on $V$ with some $m_{V}>0$. To illustrate, we plot $f(x)$ and $f(x)+\frac{5}{4}\|x-1\|^{2}$ on $V=$ in Figure 2. ‣ III-B Lower-C² and weak convexity ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"). Clearly, $f(x)$ is convexified by adding a quadratic perturbation $\frac{5}{4}\|x-1\|^{2}$.

Figure 2: Plots of f and $f+\frac{5}{4}\|\cdot-1\|^{2}$ on V = in Example 3.

### III-C Stationary points and weak PL property

We next analyze the stationary points of ${\mathcal{H}_{\infty}}$ cost $J$. As is typical in nonconvex optimization, spurious stationary points such as local minima and saddle points may arise in the general output-feedback $\mathcal{H}_{\infty}$ setting.

### Lemma 3

Suppose Assumptions 1 and 2 hold. Consider the $\mathcal{H}_{\infty}$ cost function $J:\mathcal{K}\to\mathbb{R}_{+}$ defined in 8. When $C\neq I_{n_{x}}$, the function $J$ may admit spurious stationary points, including local minima and saddle points.

We verify this result using Example 4. ‣ III-C Stationary points and weak PL property ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods") below. This is the same instance as Example 2. ‣ III-A Basic landscape properties ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods") with a different choice of $\alpha$. The example highlights that such spurious stationary points naturally emerge from the nonconvexity and potential disconnectedness of $\mathcal{K}$.

### Example 4 (Saddle points)

Consider the problem data in Example 2. ‣ III-A Basic landscape properties ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"). For $\alpha=0.13$, the set $\mathcal{K}$ consists of two disconnected components (see Figure 1(c)). At $\alpha=0.14$, these components merge, and $\mathcal{K}$ becomes connected, as shown in Figure 3(a). In this case, we observe a saddle point in $J$ (see Figure 3(b)), as well as at least one local minimum.

Figure 3: Spurious stationary points of J with the set 𝒦 in the case of static output-feedback in Example 4 (the same system as Example 2 with α = 0.14). It can be observed that J(K) possesses not only a local minimum but also a saddle point, represented by the red dot.

In the full-state measurement case ($C=I_{n_{x}}$), the $\mathcal{H}_{\infty}$ optimization exhibits a much more tractable landscape, with a connected feasible region and convex-like shape as Figures 1(a) and 1(b) ‣ Figure 1 ‣ III-A Basic landscape properties ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"). Indeed, we can establish a weak PL condition that ensures the global optimality of stationary points.

### Theorem 2 (Weak PL condition)

Suppose Assumptions 1 and 2 hold. If we have full state measurement, i.e., $C=I_{n_{x}}$, then, for $K\in\mathcal{K}$, there exists a constant $\mu_{K}>0$ such that where $\partial J$ denotes the Clarke subdifferential of $J$ and $J^{\star}=\min_{K\in\mathcal{K}}J(K)$.

The proof is provided in Section -B. We also provide an explicit form of the constant $\mu_{K}$ in 16. ‣ III-C Stationary points and weak PL property ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods") in the proof. This remarkable property has a tight connection to the well-known LMI reformulation via the bounded real lemma, which will be utilized in the proof. Our proof is motivated by the recent ECL framework and the result . The global optimality of stationary points follows as a corollary.

### Corollary 1 (Global optimality of stationary points)

Under the same assumptions as Theorem 2. ‣ III-C Stationary points and weak PL property ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"), we have $0\in\partial J(K)\Leftrightarrow K\in{\arg\min}_{K\in\mathcal{K}}J(K).$

### Proof

If $0\in\partial J(K)$, then we have $\mathrm{dist}(0,\partial J(K))=0$, which implies that $J(K)=J^{\star}$ by the weak PL 16. ‣ III-C Stationary points and weak PL property ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"). On the other hand, if $K\in{\arg\min}_{K\in\mathcal{K}}J(K)$, we must have $K$ to be stationary, and thus $0\in\partial J(K)$ \[23, Th. 10.1\]. ∎

### III-D Proof of Theorem 1. ‣ III-B Lower-C² and weak convexity ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods")

To establish Theorem 1. ‣ III-B Lower-C² and weak convexity ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"), we first rewrite the ${\mathcal{H}_{\infty}}$ cost as the composition of $\sigma_{\mathrm{max}}(\cdot)$ and a real-valued mapping using Lemma 4 below, which follows from a famous fact \[29, Exercise 4.42\] in complex SDPs. We thereby identify the weakly convex constant $m_{\nu}>0$ via the compactness of $\mathcal{K}_{\nu}$ from Lemma 1. The proof of Lemma 4 is presented in Section -A due to the page limit.

### Lemma 4

Let $X$ be a $q\times r$ hermitian matrix. We have where $\Psi(\cdot)$ is a real-valued linear mapping defined by where $\mathfrak{R}(X)$ and $\mathfrak{J}(X)$ represent the real and imaginary parts, respectively.

Recall the definition of the function $J(K)=\|{\mathbf{T}}_{zw}(K)\|_{{\mathcal{H}_{\infty}}}$ in 7. We first show the weak convexity of for any fixed $\omega\in[0,2\pi]$. Then, the weak convexity of $J=\max_{\omega\in[0,2\pi]}f(\cdot,\omega)$ follows from the standard result for point-wise maximum of convex functions \[29, Sec. 3.2.3\].

Fix an $\omega\in[0,2\pi]$. By applying Lemma 4, we have that It is clear that both $\mathfrak{R}({\mathbf{T}}_{zw}(K,\omega))$ and $\mathfrak{I}({\mathbf{T}}_{zw}(K,\omega))$ are real analytic on $\mathcal{K}\times[0,2\pi]$. Thus, the mapping $\Psi\circ{\mathbf{T}}_{zw}$ is also real analytical over $\mathcal{K}\times[0,2\pi]$. Then, the Hessian of $\Psi\circ{\mathbf{T}}_{zw}$ exists and is continuous w.r.t. $(K,\omega)$ over $\mathcal{K}\times[0,2\pi]$.

By the compactness of $\mathcal{K}_{\nu}$, we have the $L_{\nu}$-smoothness of $f(\cdot,\omega)$ on $\mathcal{K}_{\nu}$ with the following finite positive constant: where $\eta=n_{x}+n_{u}+n_{w}$. By recalling that $\lambda_{\max}(\cdot)$ is convex and $1$-Lipschitz, $f(K,\omega)$ is $m_{\nu}$-weakly convex over any convex subset of $K_{\nu}$ with $m_{\nu}=L_{\nu}$; see \[18, Sec. 2.1\].

Finally, it is straightforward to see that the function is convex on any convex subset of $\mathcal{K}_{\nu}$ from the $m_{\nu}$-weak convexity of each $f(K,\omega)$ \[29, Sec. 3.2.3\]. This leads to the desired $m_{\nu}$-weak convexity of $J(K)$. $\square$

## The Subgradient Method

In this section, we discuss the subgradient method to solve the $\mathcal{H}_{\infty}$ optimization 8. Thanks to the weak convexity in Theorem 1. ‣ III-B Lower-C² and weak convexity ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"), we provide a non-asymptotic convergence rate under mild assumptions, by adapting the recent result .

### IV-A The subgradient method

Given an initial point $K_{0}\in\mathcal{K}$, the subgradient method simply follows the update below where $\partial J(K)$ is the Clarke subdifferential of $J(\cdot)$ at $K\in\mathcal{K}$. This is arguably the simplest algorithm for nonsmooth nonconvex optimization. Thanks to its simplicity, we may implement in a model-free manner relatively easily, only with a subgradient oracle.

### IV-B Non-asymptotic convergence guarantees

Despite its simplicity, the subgradient method is classically known to achieve sublinear convergence only for convex and/or smooth problems. Its behavior in the nonsmooth nonconvex setting was far less understood because (i) stationary concepts in convex and/or smooth cases can no longer be used, and (ii) the subgradient update 17 does not guarantee monotonic decrease of the cost; it is indeed possible even in the nonsmooth convex case that $J(K_{t+1})>J(K_{t})$ for any $\alpha_{t}>0$. Recently, established the first non-asymptotic rate for minimizing unconstrained weakly convex functions. In this work, we extend their analysis to the $\mathcal{H}_{\infty}$ optimization 8 involving *a nonconvex stabilizing constraint* $\mathcal{K}$.

One key concept is the Moreau envelope, which allows for quantifying the performance of 17 even in the absence of a function value decrease.

### Definition 2 (Moreau envelope)

For $K\in\mathcal{K}$ and $\rho>0$, the Moreau envelope $J_{\rho}(\cdot)$ is defined as $J_{\rho}(K):=\min_{M\in\mathcal{K}}J(M)+\frac{\rho}{2}\|M-K\|_{F}^{2}$.

By the coercivity in Lemma 1, there always exists a minimizer $\hat{K}\in\arg\min_{M\in\mathcal{K}}J(M)+\frac{\rho}{2}\|M-K\|_{F}^{2}$, but the minimizer may not be unique. By the definition, we have While the Moreau envelope is convenient in theory, computing the value of $J_{\rho}(\cdot)$ and $\hat{K}$ might be untractable in practice. If $\rho>0$ is sufficiently large, the minimizer $\hat{K}$ will be unique. We have the following result by adapting \[18, Sec. 2.2\].

### Lemma 5

Consider the $\mathcal{H}_{\infty}$ cost function $J:\mathcal{K}\to\mathbb{R}_{+}$ defined in 8. Fix any $K\in\mathcal{K}$. Let $\nu>J(K)$, and define $L>0$ and $m>0$ such that $J(\cdot)$ is $L$-Lipschitz over $\mathcal{K}_{\nu}$ and $m$-weakly convex over any convex subset of $\mathcal{K}_{\nu}$. Then, for $\rho>\max\{m,L/\mathrm{dist}(K,\partial\mathcal{K}_{\nu})\}$, we have where $\{\hat{K}\}=\arg\min_{M\in\mathcal{K}}J(M)+\frac{\rho}{2}\|M-K\|_{F}^{2}$.

### Proof

From the optimality condition of $\min_{M}J(M)+\frac{\rho}{2}\|M-K\|_{F}^{2}$, we have where $\hat{K}$ is any minimizer. The $L$-Lipschitzness of $J$ implies $\|K-\hat{K}\|_{F}\leq L/\rho\leq d:=\mathrm{dist}(K,\partial\mathcal{K}_{\nu})$, where the last inequality is by the choice of $\rho>\max\{m,L/\mathrm{dist}(K,\partial\mathcal{K}_{\nu})\}.$ Thus, minimizing $J$ over $\mathcal{K}$ is the same as minimizing $J$ over the ball $\mathbb{B}_{d}(K)$, i.e., $\arg\min_{M\in\mathcal{K}}\{J(M)+\frac{\rho}{2}\|M-K\|_{F}^{2}\}=\arg\min_{M\in\mathbb{B}_{d}(K)}\{J(M)+\frac{\rho}{2}\|M-K\|_{F}^{2}\}.$ Since $\mathbb{B}_{d}(K)\subseteq\mathcal{K}_{\nu}$ and $\rho>m$, we have $J(\cdot)+\frac{\rho}{2}\|\cdot-K\|_{F}^{2}$ being $(\rho-m)$-strongly convex over $\mathbb{B}_{d}(K)$. The minimizer is then unique. Hence, from \[18, Lem. 2.2\], the gradient of $J_{\rho}$ can be computed as $\nabla J_{\rho}(K)=\rho(K-\hat{K})$, and 18 shows $\mathrm{dist}(0,\partial J(\hat{K}))\leq\|\nabla J_{\rho}(K)\|_{F}$. ∎ We are now ready to state the convergence of 17 in terms of the Moreau envelope under a technical condition that the costs are bounded along the iterations.

### Theorem 3

Consider the $\mathcal{H}_{\infty}$ cost function $J:\mathcal{K}\to\mathbb{R}_{+}$ defined in 8. Let $\{K_{0},\ldots,K_{T+1}\}$ be a sequence generated by the subgradient method 17 with $K_{0}\in\mathcal{K}$ and step sizes $\{\alpha_{0},\ldots,\alpha_{T}\}$. Suppose $\max_{t\in\{0,\ldots,T+1\}}J(K_{t})<\tilde{J}<\infty$ and $\max_{t\in{0,\ldots,T}}\|G_{t}\|_{F}\leq H<\infty.$ Then, we have the feasibility of the iterates $\{K_{t}\}\subset\mathcal{K}$, and where $\kappa=\rho/(\rho-m)$ with some constant $m>0$, and $\rho>{\rho}_{\min}\in(m,\infty)$. Furthermore, if $\alpha_{0}=\cdots=\alpha_{T}=\alpha=\beta/\sqrt{T+1}$ with $\beta>0$, we have

### Proof

Consider the sublevel set $\mathcal{K}_{\tilde{J}}=\{K\in\mathcal{K}\mid J(K)\leq\tilde{J}\}$, which is compact due to the coercivity. By Theorems 1. ‣ III-B Lower-C² and weak convexity ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods") and 1, $J(\cdot)$ is $L$-Lipschitz over $\mathcal{K}_{\tilde{J}}$ and $m$-weakly convex over any convex subset of $\mathcal{K}_{\tilde{J}}$, with some $L,\,m>0$.

Let ${\rho}_{\min}>\max\{m,L/\tilde{d}\},$ where Then, the same argument as Lemma 5 implies that $\mathbb{B}_{\tilde{d}}(K_{t})\subset\mathcal{K}_{\tilde{J}}$ for all $t$, and $\hat{K}_{t}\in\arg\min_{M}J(M)+\frac{\rho}{2}\|M-K_{t}\|_{F}^{2}$ is contained by the ball $\mathbb{B}_{\tilde{d}}(K_{t})$. Hence, we can regard $J(K)+\frac{\rho}{2}\|K-K_{t}\|_{F}^{2}$ as a $(\rho-m)$-strongly convex function over $\mathbb{B}_{\tilde{d}}({K}_{t})$, and this theorem follows from performing the same argument as \[18, Th. 3.1\]. The coercivity in Lemma 1 yields the feasibility of $\{K_{t}\}$. ∎ This theorem indicates that we can find an iterate $K_{t^{*}}$ satisfying $\|\nabla J_{\rho}(K_{t^{*}})\|\leq\epsilon$ after iterations, as long as the costs remain finite. For $K_{t^{*}}$, hold, where $\hat{K}_{t^{*}}={\arg\min}_{M\in\mathcal{K}}J(M)+\frac{\rho}{2}\|M-K_{t^{*}}\|_{F}^{2}$. Thus, the subgradient method 17 allows us to arrive at an approximation of a stationary point in the above sense.

### Remark 2

Theorem 3 presents a non-asymptotic convergence rate for the subgradient method 17. Notice that the boundedness of the cost is directly assumed, as it is often empirically true for sufficiently small $\{\alpha_{t}\}$ but not formally guaranteed in 17. Under this assumption, we can ensure the feasibility $\{K_{t}\}\subset\mathcal{K}$ by the coercivity in Lemma 1, bypassing the nonconvex constraint set $\mathcal{K}$ through a careful choice of the parameter $\rho$. To alleviate the assumption on the cost, one may use other algorithms that can generate a descent direction (e.g., the proximal bundle method ). We leave it as our future work. $\square$

## Numerical results

Here, we run the subgradient method 17 with fixed step sizes $\alpha_{t}=\alpha^{1}$ or $\alpha^{2}$, where $(\alpha^{1},\alpha^{2})=(10^{-3},10^{-4})$, for both full state-feedback and static output-feedback cases. The following results demonstrate the effectiveness of the subgradient method 17 and validate our theoretical results.

Figure 4: The simulation results of the subgradient method 17 with αt = α1 = 10−3 or α2 = 10−4: (a) The plot of mint|J(Kt) − J⋆|/J⋆ for the system 10 with a full state-feedback in Example 1 starting from K0 = K01 or K02, where K01 = [0, −1.9] and K02 = [0.2, −2]; (b) The plots of mintJ(Kt) (upper) and mint∥Gt∥F2 with Gt ∈ ∂J(Kt) (lower) for Example 4 with K0 = K01 = or K02 = [−5, −2].

Full state-feedback. For the system 10. ‣ III-A Basic landscape properties ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods") in Example 1. ‣ III-A Basic landscape properties ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"), we test 17 with different parameter choices. Specifically, we use $K_{0}=K_{0}^{1}=[0,-1.9]$ or $K_{0}^{2}=[0.2,-2]$. We plot the simulation result in Figure 4(a), where the vertical axis shows the best relative objective residual $\min_{t}|J(K_{t})-J^{\star}|/J^{\star}$ at $t$. In all the cases, the subgradient method generates feasible iterates, which implies that the assumptions in Theorem 3 are satisfied. In addition, as expected, we obtained a globally optimal solution for both initial conditions with favorable accuracy, especially when $\alpha_{t}=\alpha^{2}$.

Static output-feedback. For Example 4. ‣ III-C Stationary points and weak PL property ‣ III Weak Convexity in ℋ_∞ Optimization ‣ Policy Optimization in Robust Control: Weak Convexity and Subgradient Methods"), we similarly run 17 with four different choices of the initial condition and step size. In particular, we use $K_{0}=K_{0}^{1}$ or $K_{0}^{2}$ with $K_{0}^{1}=,\,K_{0}^{2}=$. The simulation result is presented in Figure 4(b). It can be seen that the feasibility is satisfied in all the cases. Regarding the performance, the cost value converged to a smaller value in the case of $K_{0}=K_{0}^{1}$. In addition, when $K_{0}=K_{0}^{2}$, we observe that the subgradient also converged nearly to a stationary point. When $K_{0}=K_{0}^{1}$ in Figure 4(b), the magnitude of the subgradient remained larger despite the smaller cost value. This is due to a zigzagging behavior around a stationary point and may happen when it is nonsmooth. For example, $f(x)=|x|$ takes the minimum at $x=0$, but the origin is nonsmooth and $\partial f=\neq\{0\}$, which may lead to such behavior.

## Conclusion

This study addressed the ${\mathcal{H}_{\infty}}$ optimization problem for discrete-time linear systems with static output-feedback. We first proved the weak convexity and further established the weak PL condition in the full state-feedback case. Then, we also discussed the subgradient method from a weak convexity perspective, presenting the first non-asymptotic convergence rate. The numerical simulations validated our theoretical analysis and demonstrated the effectiveness of the subgradient method. Our future work includes alleviating the assumption of the cost value boundedness in the convergence rate result, for example, through the proximal bundle method.
