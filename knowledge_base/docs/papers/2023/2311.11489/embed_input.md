<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Beyond Nonconvexity: A Universal Trust-Region Method with New Analyses

Topics include Convex optimization, Nonconvex optimization, Robustness, Optimization, Nonconvexity, TR, Stationary point.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The trust-region (TR) method is renowned historically for its robustness in nonconvex problems and extraordinary numerical performance, but the study of its performance in convex optimization is somehow limited. This paper complements the existing literature by presenting a universal trust-region method that simultaneously incorporates the quadratic regularization and ball constraint. In particular, we introduce a novel descent property tailored for trust-region-type algorithms, enabling us to unify and streamline the analysis for both convex and nonconvex optimization. Our method exhibits an iteration complexity of tilde O(epsilon^(-3/2)) to find an epsilon-approximate second-order stationary point for nonconvex optimization. Meanwhile, the analysis reveals that the universal method attains an O(1/sqrt(epsilon)) complexity bound for convex optimization. Finally, we develop an adaptive universal method to address practical implementations. The numerical results show the effectiveness of our method in both nonconvex and convex problems.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Second-order methods are renowned for their faster convergence compared to first-order methods, and the capability to find second-order stationary points, see Cartis et al., Nocedal and Wright, Nesterov, Carmon et al.. Among these methods, the trust-region (TR) method stands out as a representative approach due to its robustness in nonconvex problems and extraordinary numerical performance. Many linear or nonlinear programming solvers are using the trust-region method as an important building block, to name a few, Knitro, IPOPT, and PDFO, etc. Also, in the machine learning field, it inspires the well-known trust-region policy optimization.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recall that the TR method operates on the local quadratic approximation of objective function $f:\mathbb{R}^{n}\to\mathbb{R}$ within a TR ball constraint: | | $\displaystyle\min_{d\in\mathbb{R}^{n}}$ | $\displaystyle m_{k}(d)=\nabla f(x_{k})^{T}d+\frac{1}{2}d^{T}\nabla^{2}f(x_{k})d,$ | | (1.1) | | | $\displaystyle\operatorname{s.t.}$ | $\displaystyle\|d\|\leq\Delta_{k}.$ | | | Once the TR step $d_{k}$ is generated, the TR method decides whether to update or adjust the radius $\Delta_{k}$ based on the so-called ratio test: Despite its success in practice as mentioned above, the theoretical development of the TR method is somehow incomplete.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

For instance, results in the early literature only established (asymptotic) local convergence to $\epsilon$-approximate second-order stationary points ($\epsilon$-SOSP). These results also implied that TR has a nonasymptotic iteration complexity of $O(\epsilon^{-2})$ for $\epsilon$-SOSPs. However, such convergence rate is no better than first-order methods for $\epsilon$-approximate first-order stationary points ($\epsilon$-FOSP), and an improved convergence rate is not aware for convex functions.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In contrast, as another representative second-order method, the Cubic Regularized (CR) Newton method has the updating rule This method was originally proposed by Griewank and further analyzed by Nesterov and Polyak. Later, Cartis et al. proposed the adaptive version of this method. It shows a convergence rate of $O(\epsilon^{-3/2})$ to find $\epsilon$-SOSPs for nonconvex functions and $O(\epsilon^{-1/2})$ for convex case simultaneously.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, classical TR exhibits a clear gap to these convergence properties. This arises possibly due to two aspects: first, the classic TR method does not fully exploit the curvature information of Hessian; second, the ratio test (1.2) does not explicitly quantify the desired decrease for the TR steps \[10 for nonconvex optimization")\]; both are crucial in modern complexity analysis.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Therefore, a plethora of TR variants (e.g., \[10 for nonconvex optimization"), 9, 19, 23\]) have been proposed to improve iteration complexity over the years. The fixed-radius variant by Luenberger and Ye achieves a complexity of $O(\epsilon^{-3/2})$ for finding $\epsilon$-SOSPs by controlling the stepsize proportionally to the tolerance ${\epsilon}^{1/2}$. However, this variant tends to be conservative for practical applications. By designing a contraction and expansion mechanism, Curtis et al. \[10 for nonconvex optimization")\] introduced the first adaptive trust-region method (TRACE) matching the $\tilde{O}(\epsilon^{-3/2})$ complexity for finding $\epsilon$-SOSPs, where $\tilde{O}$ means there is a logarithmic term hidden in the complexity. Later, Curtis et al. proposed another simplified variant of \[10 for nonconvex optimization")\] while retaining the same dependency on $\epsilon$.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

A notable recent trust-region method introduced by Hamad and Hinder achieves $O(\epsilon^{-3/2})$ complexity and improves the complexity's dependency over Lipschitz constants by putting together the upper and lower bounds on the stepsizes. However, their algorithm only converges to an $\epsilon$-FOSP. Generally, these novel variants transcend the classic ones to bring a per-step sufficient decrease As a result, $O(\epsilon^{-3/2})$ rate of convergence can be achieved. However, for TR-type algorithms, such sufficient decrease (1.4) is highly nontrivial, due to its heavy dependence on the posterior dual multiplier of the subproblem (1.1), which is difficult to control in advance. As a price to overcome this challenge, these algorithms rely on complicated feedback to adjust the dual multiplier and may need additional assumptions. Moreover, these TR-type methods are initially designed for nonconvex optimization, and the associated convergence analysis in convex optimization is largely missing.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, even in many nonconvex problems, the objective function quickly turns weakly convex near some stationary points, which makes the study of TR-type methods in convex optimization equally important.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We summarize the above TR variants and other mainstream second-order methods in Table 1. As an observation, existing research fails to unleash the full potential of trust-region methods: $(a)$ While all aforementioned TR variants have improved complexity guarantee in the nonconvex case, to the best of our knowledge, neither of the nonasymptotic analyses extends to the convex case. Thus, whether a TR method has a global $O(\epsilon^{-1/2})$ convergence rate in convex optimization remains open. $(b)$ On the practical side, the existing *adaptive* trust-region methods tend to be complicated compared to other second-order methods \[26, 24 Convergence"), 36\], embedding different subroutines and nested loops. There is a clear mismatch between the theoretical guarantees and conciseness of implementation, thus calling for a simpler trust-region method with state-of-the-art complexity rates.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Standard Trust-Region Method Gradient-Regularized Newton Method Damped Newton Method Cubic Regularized Newton Method † The method does not provide local convergence analysis. We believe this should be true following standard analysis. ‡ The method assumes the objective function is strictly convex and uses a stronger version of the self-concordance.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contributions", "weight": 1.0} -->

The feature of the subproblem above is incorporating gradient regularization in the local quadratic model and setting the trust-region radius proportional to the square root of the gradient norm. As a result, the $d_{k}$ generated by (1.5) exhibits a powerful feature referred to as Function-or-Stationarity-Decrease (FOSD, Property 2.2. ‣ 2.1 Overview of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.")), i.e., after one successful update, either the function value decreases sufficiently or the gradient norm shrinks linearly. Different from (1.4), this desirable property enables a concise and clean algorithm which does not need sophisticated inner loop to control the posterior multiplier $\lambda_{k}$, and the associated complexity results have the state-of-the-art dependency over both the tolerance $\epsilon$ and the Lipschitz constant, requiring only the most standard assumptions.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Contributions", "weight": 1.0} -->

More specifically, with explicit information on the Hessian Lipschitz constant, we propose a simple strategy to choose parameters $(\sigma_{k},r_{k})$ (Strategy 2.1. ‣ Basic Principle of Choosing (𝜎_𝑘,𝑟_𝑘) ‣ 2.2 Basic Properties of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.")), and UTR converges to an $\epsilon$-FOSP within $\tilde{O}(\epsilon^{-3/2})$ iterations. Surprisingly, we also find that UTR exhibits an improved $O(\epsilon^{-1/2})$ complexity when the objective function is convex. To the best of our knowledge, this is the first nonasymptotic analysis of TR-type methods in convex optimization.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Contributions", "weight": 1.0} -->

Under the guidance of the simple strategy, we develop an adaptive approach (Strategy 4.1. ‣ 4.1 The Adaptive Framework ‣ 4 The Adaptive Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.")) that is more practical without relying on the Lipschitz constant. By fully exploiting the curvature information of the Hessian, this adaptive approach provides a convergence guarantee with an iteration complexity of $\tilde{O}(\epsilon^{-3/2})$ for finding $\epsilon$-SOSPs.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Contributions", "weight": 1.0} -->

Finally, in numerical experiments, our method is compared against ARC, the newly proposed TR variant, and the recent gradient regularized Newton method \[24 Convergence")\], demonstrating the effectiveness of UTR.

<!-- chunk {"id": "body-0017", "role": "body", "section": "The Universal Trust-Region Method", "weight": 1.0} -->

In this paper, we consider the following unconstrained optimization problem where $f:\mathbb{R}^{n}\to\mathbb{R}$ is twice differentiable and is bounded below, i.e., $f^{*}:=\inf_{x\in\mathbb{R}^{n}}f(x)>-\infty$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Assumption 2.1", "weight": 1.0} -->

The Hessian $\nabla^{2}f(x)$ of the objective function is Lipschitz continuous with constant $M>0$, i.e., As a consequence, Assumption 2.1 implies the following results.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Overview of the Method", "weight": 1.0} -->

Now we introduce the universal trust-region method in Algorithm 1.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Overview of the Method", "weight": 1.0} -->

Data: Initial point x0 ∈ ℝn 2 Adjust (σk, rk) by a proper strategy; 3 Solve the subproblem (1.5) and obtain the direction dk; 4 if dk is good enough then Algorithm 1 A Universal Trust-Region Method (UTR) In particular, at each iteration $k$, we solve the subproblem (1.5). The mechanism of our trust-region method is straightforward, comprising only three major steps: setting the appropriate parameters $\sigma_{k}$ and $r_{k}$ by some strategy, solving the trust-region subproblem (1.5), and updating the iterate whenever $d_{k}$ is good enough.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Overview of the Method", "weight": 1.0} -->

The crux of our method lies in the selection of proper parameters $\sigma_{k}$ and $r_{k}$. This choice guides the model (1.5) to generate good steps that meet favorable descent properties to establish our iteration complexity bounds, i.e., the number of iterations $T$ required to find the desired solutions. We define the following properties which are tailored for the universal trust-region method.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Property 2.1 (Monotone-Decrease)", "weight": 1.0} -->

The step decreases the value of the objective function, that is for each iteration $k$,

<!-- chunk {"id": "body-0023", "role": "body", "section": "Property 2.2 (Function-or-Stationarity-Decrease)", "weight": 1.0} -->

For some $0<\xi<1$, $\kappa>0$, the step $d_{k}$ either decreases the value of the objective function or decreases the gradient norm sufficiently, that is for each iteration $k$, For Property 2.1. ‣ 2.1 Overview of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026."), it serves as a safeguard to ensure that the algorithm never discards the progress made in the previous iterations. Property 2.2. ‣ 2.1 Overview of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.") is novel in the sense that we do not force every iteration to bring about a sufficient decrease in the function value but instead allow a linear contraction of the norm of the gradient as an alternative. Consequently, our analysis is largely simplified compared to other TR variants and uses only the most standard assumptions.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Property 2.2 (Function-or-Stationarity-Decrease)", "weight": 1.0} -->

Moreover, our analysis is almost unified for both convex and nonconvex optimization.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Property 2.2 (Function-or-Stationarity-Decrease)", "weight": 1.0} -->

Unlike the classic ratio test, we design a new mechanism (Strategy 2.1. ‣ Basic Principle of Choosing (𝜎_𝑘,𝑟_𝑘) ‣ 2.2 Basic Properties of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.")) to ensure monotonicity: when we know the Lipschitz constant $M$. We show that the ratio test can be removed and every step is a good step. Moreover, even if we do not know the constant, we can perform a simple search procedure to ensure monotonicity.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Property 2.2 (Function-or-Stationarity-Decrease)", "weight": 1.0} -->

We later prove the complexity results by establishing (2.7. ‣ 2.1 Overview of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.")) and (2.8. ‣ 2.1 Overview of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.")), and their modifications for convex functions (Property 3.1) as well as adaptiveness in choosing the parameters (Property 4.1). Moreover, we give general principles where parameter selection can be designed based on the information available at hand.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Basic Properties of the Method", "weight": 1.0} -->

We present some preliminary analysis of our method. Similar to the standard trust-region method, the optimality conditions of (1.5) are provided as follows.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Basic Principle of Choosing $(\\sigma_{k},r_{k})$", "weight": 1.0} -->

The aforementioned Lemma 2.3 and Lemma 2.4 offer a valuable principle of selecting $\sigma_{k}$ and $r_{k}$ to guarantee that the step satisfies Property 2.1. ‣ 2.1 Overview of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.") and Property 2.2. ‣ 2.1 Overview of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026."). In particular, it suffices to control for some $\kappa>0,\xi<1$. Thus, the choice of $\sigma_{k}$ and $r_{k}$ could be very flexible.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Basic Principle of Choosing $(\\sigma_{k},r_{k})$", "weight": 1.0} -->

For example, a vanilla approach can be constructed by discarding the term $\frac{1}{2r_{k}}\cdot\frac{\lambda_{k}}{\|\nabla f(x_{k})\|^{1/2}}$ in (2.15a ‣ 2.2 Basic Properties of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.")). Suppose the Lipschitz constant $M$ is given, we show that a strategy that fits (2.15 ‣ 2.2 Basic Properties of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.")) exists; namely, we can adopt a fixed rule of selecting $\sigma_{k}$ and $r_{k}$ as follows.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Strategy 2.1 (The Simple Strategy)", "weight": 1.0} -->

With the knowledge of Lipschitz constant $M$, we set for all $k$ in Algorithm 1.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Strategy 2.1 (The Simple Strategy)", "weight": 1.0} -->

The universal trust-region method (Algorithm 1) equipped with such a simple choice reveals the following results.

<!-- chunk {"id": "body-0032", "role": "body", "section": "The Universal Trust-Region Method with a Simple Strategy", "weight": 1.0} -->

In this section, we give a convergence analysis of the universal method with the simple Strategy 2.1. ‣ Basic Principle of Choosing (𝜎_𝑘,𝑟_𝑘) ‣ 2.2 Basic Properties of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.") to an $\epsilon$-approximate FOSP (see Definition 2.1) with an iteration complexity of $\tilde{O}\left(\epsilon^{-3/2}\right)$. The local convergence of this method is shown to be superlinear. Furthermore, the complexity can be further improved to $O\left(\epsilon^{-1/2}\right)$ for convex functions.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Global Convergence Rate for Nonconvex Optimization", "weight": 1.0} -->

For the nonconvex functions, we introduce the notation $x_{j_{f}}$ representing the first iterate satisfying We derive the convergence results according to Property 2.1. ‣ 2.1 Overview of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.") and Property 2.2. ‣ 2.1 Overview of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026."). Based on the FOSD Property 2.2.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Global Convergence Rate for Nonconvex Optimization", "weight": 1.0} -->

‣ 2.1 Overview of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026."), we define the following index sets to classify the iteration generated by Algorithm 1, | | | $\displaystyle\mathcal{F}_{j_{f}}=\left\{k<j_{f}:f(x_{k}+d_{k})-f(x_{k})\leq-\frac{\kappa}{\sqrt{M}}\|\nabla f(x_{k})\|^{3/2}\right\},\ \text{and}$ | | (3.1) | | | | $\displaystyle\mathcal{G}_{j_{f}}=\left\{k<j_{f}:\|\nabla f(x_{k}+d_{k})\|\leq\xi\|\nabla

<!-- chunk {"id": "body-0035", "role": "body", "section": "Global Convergence Rate for Nonconvex Optimization", "weight": 1.0} -->

From Corollary 2.1 ‣ 2.2 Basic Properties of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026."), we know each iteration in Algorithm 1 with Strategy 2.1. ‣ Basic Principle of Choosing (𝜎_𝑘,𝑟_𝑘) ‣ 2.2 Basic Properties of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.") belongs to at least one of the above sets with $\kappa=\frac{1}{81}$ and $\xi=\frac{1}{6}$. If an iteration happens to belong to both, we assign it to set $\mathcal{F}_{j_{f}}$ for simplicity.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Global Convergence Rate for Nonconvex Optimization", "weight": 1.0} -->

Therefore, our goal is to provide an upper bound for the cardinality of sets $\mathcal{F}_{j_{f}}$ and $\mathcal{G}_{j_{f}}$. To begin, we analyze $|\mathcal{F}_{j_{f}}|$ by evaluating the decrease in function value.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Minimizing Convex Functions", "weight": 1.0} -->

In this subsection, we show that the universal trust-region method can achieve the state-of-the-art $O(\epsilon^{-1/2})$ iteration complexity making it comparable to other second-order methods when the objective function enjoys convexity, see Nesterov and Polyak, Doikov et al., Doikov and Nesterov, Mishchenko \[24 Convergence")\]. Before delving into the analysis, we impose an additional property in this case.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Property 3.1", "weight": 1.0} -->

The norm of the gradient at the next iterate is upper bounded as where $0<\xi<1$ is the same as that defined in Property 2.2. ‣ 2.1 Overview of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.").

<!-- chunk {"id": "body-0039", "role": "body", "section": "Property 3.1", "weight": 1.0} -->

The above property is a safeguard for the iterates so that the gradient is bounded even in the case where $\lambda_{k}\neq 0$, cf. (2.8. ‣ 2.1 Overview of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.")). We can again establish the validness of such property, for example, Strategy 2.1. ‣ Basic Principle of Choosing (𝜎_𝑘,𝑟_𝑘) ‣ 2.2 Basic Properties of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.").

<!-- chunk {"id": "body-0040", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

The diameter of the sublevel set $\mathcal{L}_{f}:=\left\{x:f(x)\leq f\left(x_{0}\right)\right\}$ is bounded by some constant $D>0$, which means that for any $x$ satisfying $f(x)\leq f\left(x_{0}\right)$ we have $\left\|x-x^{*}\right\|\leq D$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Assumption 3.1", "weight": 1.0} -->

For the convex optimization, we still adopt the notation $x_{j_{f}}$ representing the first iterate satisfying (2.4). Recalling the definition of the index sets in (3.1), we provide an upper bound for the cardinality of $\mathcal{F}_{j_{f}}$ in the following lemma.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Local Convergence", "weight": 1.0} -->

We now move to the local performance of Algorithm 1, we show that the method has superlinear local convergence when $\sigma_{k},r_{k}$ is updated as in Strategy 2.1. ‣ Basic Principle of Choosing (𝜎_𝑘,𝑟_𝑘) ‣ 2.2 Basic Properties of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026."). We first make a standard assumption in local analysis.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Assumption 3.2", "weight": 1.0} -->

Denoting the sequence generated by the algorithm as $\{x_{k}\}$, we assume that $x_{k}\to x^{*}$, $k\to+\infty$, where $x^{*}$ satisfies First, we prove that under Assumption 3.2, when $k$ is sufficiently large, the trust-region constraint (2.9a) will be inactive in reminiscences of the classical results.

<!-- chunk {"id": "body-0044", "role": "body", "section": "The Adaptive Universal Trust-Region Method", "weight": 1.0} -->

In the above sections, we have provided a concise analysis of the universal trust-region method that applies uniformly to both convex and nonconvex optimization. Nevertheless, the limitation of Property 2.2. ‣ 2.1 Overview of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.") lies in its reliance on the unknown Lipschitz constant, which brings the challenge for efficient implementation. To enhance the capability of our method in practice, we provide an adaptive universal trust-region method (Algorithm 2), we show that it can preserve the global complexity of the simple strategy and find $\epsilon$-SOSPs. Also, the local convergence can be improved to quadratic.

<!-- chunk {"id": "body-0045", "role": "body", "section": "The Adaptive Framework", "weight": 1.0} -->

To avoid using the Lipschitz constant $M$, several revisions should be made to our previous strategies of accepting the directions and tuning the parameters. In Algorithm 2, we impose an inner loop, indexed by $j$, for $(\sigma^{(j)}_{k},r^{(j)}_{k})$ parameterized by $\rho_{k}^{(j)}$. We terminate the loop $j$ until the iterates satisfy Property 4.1, which is defined as follows.

<!-- chunk {"id": "body-0046", "role": "body", "section": "The Adaptive Framework", "weight": 1.0} -->

Data: Initial point x0 ∈ ℝn, tolerance ϵ > 0, decreasing constant $0<\eta<\frac{1}{32}$, $\frac{1}{4}<\xi<1$, initial penalty ρ0 > 0, minimal penalty ρmin > 0, penalty increasing parameter γ1 > 1, penalty decreasing parameter γ2 > 1; 4 Update σk(j), rk(j) using Strategy 4.1; 5 Solve the trust-region subproblem (1.5) and obtain the direction dk(j); 6 if Property 2.1 and Property 4.1 hold then 15 Update xk + 1 = xk + dk(j), ρk + 1 = max {ρmin, ρk(j)/γ2}; Algorithm 2 An Adaptive Universal Trust-Region Method

<!-- chunk {"id": "body-0047", "role": "body", "section": "Property 4.1", "weight": 1.0} -->

Given $\frac{1}{4}<\xi<1$, $0<\eta<\frac{1}{32}$, the step $d_{k}^{(j)}$ satisfies where $\eta$ and $\rho_{k}^{(j)}$ are defined in Algorithm 2. If $f$ is nonconvex, the step $d_{k}^{(j)}$ additionally satisfies If $f$ is convex, the step $d_{k}^{(j)}$ should satisfy Compared to Property 2.2. ‣ 2.1 Overview of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026."), we allow no dependence on the Lipschitz constant $M$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Property 4.1", "weight": 1.0} -->

The premise of this rule is that we can find a sufficiently large regularization $\sigma_{k}$ (or equivalently, sufficiently small $r_{k}$) based on Lemma 2.3 and Lemma 2.4 similar to other adaptive methods, see Cartis et al., Curtis et al. \[10 for nonconvex optimization")\], He et al.. Besides, we proceed with the algorithm when the gradient norm is small so that one can find $\epsilon$-SOSPs.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Property 4.1", "weight": 1.0} -->

As for the $(\sigma_{k}^{(j)},r_{k}^{(j)})$, we recall the principle (2.15a ‣ 2.2 Basic Properties of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.")) that motivates the aforementioned simple strategy. As we directly ignore the curvature information, it only converges to a first-order stationary point when $f(x)$ is nonconvex. Therefore we propose the following adaptive strategy (Strategy 4.1. ‣ 4.1 The Adaptive Framework ‣ 4 The Adaptive Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.")) to allow convergence to second-order stationary points.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Strategy 4.1 (The Strategy for Second-order Stationary Points)", "weight": 1.0} -->

In the Line 5 of Algorithm 2, we apply the following strategy in Table 2. ‣ 4.1 The Adaptive Framework ‣ 4 The Adaptive Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.").

<!-- chunk {"id": "body-0051", "role": "body", "section": "Strategy 4.1 (The Strategy for Second-order Stationary Points)", "weight": 1.0} -->

We later justify that the direction $d_{k}^{(j)}$ will gradually be accepted at some $j$ (see Lemma 4.1). As shown in the next subsection, the adaptive method converges to $\epsilon$-SOSPs with the same complexity as the previous conceptual version. Furthermore, the adaptive version also allows us to adjust the regularization $\sigma_{k}$, which leads to a faster speed of local convergence. Certainly, such a strategy relies on additional information from the smallest eigenvalue. As the trust-region method very often utilizes a Lanczo-type method to solve the subproblems, e.g., Cartis et al., Conn et al., using the smallest eigenvalue of the Hessian incurs no significant cost, see Gratton et al., Hamad and Hinder.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Strategy 4.1 (The Strategy for Second-order Stationary Points)", "weight": 1.0} -->

If instead we use a factorization-based method, the Cholesky factorization can also serve the purpose of the eigenvalue test: we may increase the dual-variable $\lambda_{k}$ if the factorization fails, in which case, an estimate of the smallest eigenvalue can be built from $\lambda_{k}$ and $\sigma_{k}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Global Convergence", "weight": 1.0} -->

In this subsection, we begin with the complexity analysis in the nonconvex case. We demonstrate that Algorithm 2 requires no more than $\tilde{O}\left(\epsilon^{-3/2}\right)$ iterations to converge to an $\epsilon$-approximate second-order stationary point satisfying (2.2) and (2.3). The following lemma shows that there exists an upper bound on the penalty parameter $\rho_{k}^{(j)}$, leading to the termination of the inner loop.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Nonconvex Functions", "weight": 1.0} -->

Now we are ready to give a formal iteration complexity analysis of Algorithm 2. We show that for the nonconvex objective function with Lipschitz continuous Hessian, Algorithm 2 takes $\tilde{O}\left(\epsilon^{-3/2}\right)$ to find an $\epsilon$-approximate second-order stationary point $x$ satisfying (2.2) and (2.3).

<!-- chunk {"id": "body-0055", "role": "body", "section": "Nonconvex Functions", "weight": 1.0} -->

Similar to the previous section, the following analysis is standard.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Nonconvex Functions", "weight": 1.0} -->

| | | and denote $x_{p_{s}}$ as the first iteration satisfying (2.2) and (2.3).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Nonconvex Functions", "weight": 1.0} -->

Then by the mechanism of the Algorithm 2, all indices belong to one of the sets defined in (4.5), and thus we only need to provide an upper bound for the summation Similar to the previous section, we first show that the norm of the gradient of the iterates have an uniform upper bound, with the proof deferred to Appendix A.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Convex Functions", "weight": 1.0} -->

For the case where the objective function is convex, we are satisfied with points such that the norm of the gradient less than $\epsilon$, then the two sets becomes The following analysis is the same as Algorithm 1 with Strategy 2.1. ‣ Basic Principle of Choosing (𝜎_𝑘,𝑟_𝑘) ‣ 2.2 Basic Properties of the Method ‣ 2 The Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026."). We directly provide the convergence result here.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Local Convergence", "weight": 1.0} -->

In this subsection, we give the local performance of Algorithm 2 with Strategy 4.1. ‣ 4.1 The Adaptive Framework ‣ 4 The Adaptive Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.") under Assumption 3.2, and show that the method has a local quadratic rate of convergence when $(\sigma_{k},r_{k})$ is updated as in Strategy 4.1. ‣ 4.1 The Adaptive Framework ‣ 4 The Adaptive Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.").

<!-- chunk {"id": "body-0060", "role": "body", "section": "Local Convergence", "weight": 1.0} -->

Since in the local scenario, we can regard $\epsilon\to 0$, and $\rho_{k}^{(j)}$ has a uniform upper bound, then Strategy 4.1. ‣ 4.1 The Adaptive Framework ‣ 4 The Adaptive Universal Trust-Region Method ‣ Beyond Nonconvexity: A Universal Trust-Region Method with New AnalysesAccepted by Journal of Scientific Computing, 2026.") will persist in the case when $k$ is sufficiently large: in which we always set $(\sigma_{k}^{(j)},r_{k}^{(j)})=(0,1/2\rho_{k}^{(j)})$. The rest of the cases are irrelevant to our discussion. Similar to the previous discussion, we show that when $k$ is sufficiently large, the trust-region constraint (2.9a) will be inactive.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In this section, we present numerical experiments. We implement the adaptive UTR (Algorithm 2) in Julia programming language. All experiments are performed on a MacBook Pro with Apple M2 Chip and 24GB LPDDR5 Memory. To enable efficient routines for trust-region subproblems, we implement two options. The first option utilizes the standard Cholesky factorization \[28, Algorithm 4.3\] and uses a hybrid bisection and Newton method to find the dual variable. When using this option, we name the method after UTR. The second option is an indirect method (so it is referred to as iUTR) by Krylov subspace iterations, which is consistent with the open-source implementation of classical trust-region method and adaptive cubic regularized Newton method. Motivated from Curtis and Wang and Cartis et al. \[6, Chapter 10\], we use the Lanczos method with inexactness of subproblem solutions.

<!-- chunk {"id": "body-0062", "role": "body", "section": "CUTEst benchmarks", "weight": 1.0} -->

We conduct experiments on unconstrained problems with dimension $n\leq 5000$ in the CUTEst benchmarks. Since many of these problems are nonconvex, we focus on comparisons with the classical trust-region method and adaptive cubic regularized Newton method. All methods use Krylov approaches to solve subproblems. Specifically, the classical trust-region method uses the Steihaug-Toint conjugate gradient method. Since both the classical trust-region method (Newton-TR-STCG) and adaptive cubic regularized method (ARC) are well studied, we directly use the implementation in Dussault.

<!-- chunk {"id": "body-0063", "role": "body", "section": "CUTEst benchmarks", "weight": 1.0} -->

We present our results in Table 3. We report $\overline{t}_{G},\overline{k}_{G}$ as scaled geometric means of running time in seconds and iterations (scaled by 1 second and 50 iterations, respectively). We regard a successful instance if it is solved within 200 seconds with an iterate $x_{k}$ such that $\|\nabla f(x_{k})\|\leq 10^{-5}$. If an instance fails, its iteration number and running time are set to $20,000$. We set the total number of successful instances as $\mathcal{K}$. Then we present the number of function evaluations and gradient evaluations by $\overline{k}_{G}^{f}$ and $\overline{k}_{G}^{g}$, respectively, where $\overline{k}_{G}^{g}$ also includes the Hessian-vector evaluations.

<!-- chunk {"id": "body-0064", "role": "body", "section": "CUTEst benchmarks", "weight": 1.0} -->

In Table 3, iUTR has the most successful numbers, best running time as well as iteration performance. These results match the complexity analysis that unveils the benefits of gradient norm in both trust-region radii and regularization terms.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Logistic regression", "weight": 1.0} -->

For convex optimization, we test on logistic regression with $\ell_{2}$ penalty, where $a_{i}\in\mathbb{R}^{n},~b_{i}\in\{-1,1\}$, $i=1,2,\cdots,N.$ We set $\gamma=10^{-8}$ so that the Newton steps may fail at degenerate Hessians. Since the problem is convex, we focus on comparisons with the adaptive Newton method with cubics (ArC, Cartis et al.) and variants of the regularized Newton method \[24 Convergence")\]. We implement the regularized Newton method (RegNewton) with fixed regularization $\sigma_{k}\in\{10^{-3},5\times 10^{-4}\}$ and an adaptive version following Mishchenko \[24 Convergence"), Algorithm 2.3\] that is named after RegNewton-AdaN+.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Logistic regression", "weight": 1.0} -->

In Figure 1, we profile the performance of these methods in minimizing the gradient norm. The results show that the adaptive universal trust-region method is comparable to ArC and RegNewton-AdaN+, implying its competence in minimizing the convex functions.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Matrix Completion", "weight": 1.0} -->

A final experiment is conducted on matrix completion problems motivated by a recent TR method, CAT. The goal is to recover a power consumption matrix $D\in\mathbb{R}^{n_{1}\times n_{2}}$ using a partially observed set $\Omega=\{(i,j)\}$ and the low-rank representation $D=PQ^{T}$, where $P\in\mathbb{R}^{n_{1}\times r}$ and $Q\in\mathbb{R}^{n_{2}\times r}$ with $r\ll n_{1}$ and $r\ll n_{2}$. In the above $n_{1}$ represents the number of measurements taken per day within a 15 mins interval and $n_{2}$ represents the number of days. We allow the same baseline estimate as: where $\mu$ represents the average of all observed measurements, $r_{i},c_{j}$ captures the deviations during time $i$ and day $j$.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Matrix Completion", "weight": 1.0} -->

We focus on the following regularized problem: to fit the observed data under (5.2), where $D_{i,j}$ denotes the observed data recorded at time $i$ and day $j$. The dataset used for this study is sourced from Ausgrid that deals with the matrix size of $48\times 30$, $r=9$, all algorithms are terminated at $\|\nabla f(x_{k})\|\leq 10^{-7}$. We vary $\lambda\in[10^{-2},10^{-3},10^{-4}]$ to test the robustness under small regularizations. The results are presented in Table 4. While smaller $\lambda$ induces harder instances, iUTR has the best performance among competing algorithms in all instances. Since the CAT method only converges to $\epsilon$-FOSPs according to its theory, we only include its results when $\lambda=10^{-2}$.
