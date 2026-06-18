<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization

Topics include Convex optimization, Gradient descent, Optimization, II.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We provide a concise, self-contained proof that the Silver Stepsize Schedule proposed in Part I directly applies to smooth (non-strongly) convex optimization. Specifically, we show that with these stepsizes, gradient descent computes an epsilon-minimizer in O(epsilon^-log_rho 2) = O(epsilon^(-0).7864) iterations, where rho = 1+sqrt is the silver ratio. This is intermediate between the textbook unaccelerated rate O(epsilon^(-1)) and the accelerated rate O(1/sqrt(epsilon)) due to Nesterov in 1983. The Silver Stepsize Schedule is a simple explicit fractal: the i-th stepsize is 1+rho^(v)(i)-1 where v(i) is the 2-adic valuation of i. The design and analysis are conceptually identical to the strongly convex setting in Part I, but simplify remarkably in this specific setting.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

We revisit the classical problem of smooth convex optimization: solve ${\min_{x \in {\mathbb{R}}^{d}}f}{(x)}$ where $f$ is convex and $M$-smooth (i.e., its gradient is $M$-Lipschitz). A celebrated result is that with a prudent choice of stepsizes $\{\alpha_{t}\}$, the gradient descent algorithm (GD)

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

solves such a convex optimization problem to arbitrary accuracy from any initialization $x_{0}$. How quickly does GD converge? The mainstream approach (see e.g., the textbooks among many others) is to use a constant stepsize schedule $\alpha_{t} \equiv \overline{\alpha} \in {}$ since this ensures

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The main question posed in Part I was: can we accelerate the convergence of GD without changing the algorithm---just by judiciously choosing the stepsizes? Here we continue to investigate this question, now in the setting of smooth convex optimization. Note that this is markedly different from classical approaches to acceleration---starting from Nesterov's seminal result of 1983, those approaches modify the basic GD algorithm by adding momentum, internal dynamics, or other additional building blocks beyond just changing the stepsizes. For this reason, we do not discuss that line of work in detail, and instead refer to for a recent survey of this mainstream approach to acceleration, and to for a full discussion of the relations between these approaches.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Contribution", "weight": 1.0} -->

This paper provides a concise, self-contained proof that the Silver Stepsize Schedule proposed in Part I directly applies to smooth (non-strongly) convex optimization. This leads to faster convergence rates of GD for smooth convex optimization, as already pointed out in \[3, §1.1.4\].

<!-- chunk {"id": "body-0007", "role": "body", "section": "Contribution", "weight": 1.0} -->

In this setting, the Silver Stepsize Schedule is particularly simple. For any integer $n = {2^{k} - 1}$, we recursively construct the schedule $h_{{2n} + 1}$ of length ${2n} + 1$ from the schedule $h_{n}$ of length $n$ via

<!-- chunk {"id": "body-0008", "role": "body", "section": "Contribution", "weight": 1.0} -->

where $\rho:={1 + \sqrt{2}}$ denotes the silver ratio, and $h_{1}:={\lbrack\sqrt{2}\rbrack}$. This results in the simple pattern $\lbrack\sqrt{2},\;2,\sqrt{2},{\;1 + \sqrt{2}},\ldots\rbrack$ as depicted in Figure 1. This schedule is exactly the Silver Stepsize Schedule from in the limit that the strong convexity parameter vanishes (see Remark 2.2. ‣ 2 Silver Stepsize Schedule ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization") for details), and bears similarities to those; see §1.2.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Contribution", "weight": 1.0} -->

We show that these stepsizes yield an improved convergence rate (1.2) where $\frac{c}{n}$ is replaced by

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contribution", "weight": 1.0} -->

This bound gives the correct asymptotic scaling of $r_{k}$ since the inequality is asymptotically tight.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Indexing", "weight": 1.0} -->

Throughout, the horizon is $n = {2^{k} - 1}$. This correspondence between $n \in {\{ 1,3,7,15,\ldots\}}$ and $k \in {\{ 1,2,3,4,\ldots\}}$ allows re-indexing in a way that simplifies notation for the recursion.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Silver Stepsize Schedule", "weight": 1.0} -->

The Silver Stepsize Schedule is defined recursively in (1.3). Here we mention an equivalent direct expression and make several remarks. Let $\nu{(t)}$ denote the $2$-adic valuation of $t$, i.e., the smallest non-negative integer $i$ such that $2^{i}$ is in the binary expansion of $t$. For example, ${\nu{}} = 0$, ${\nu{}} = 1$, ${\nu{}} = 0$, ${\nu{}} = 2$, etc.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Remark 2.2 (Limit of Silver Stepsize Schedules in the strongly convex case)", "weight": 1.0} -->

The schedule (2.1. ‣ 2 Silver Stepsize Schedule ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization")) is simply the Silver Stepsize Schedule for smooth *strongly*-convex optimization in Part I, in the limit as the strong convexity parameter tends to $0$. The stepsizes simplify in the limit: they increase by a factor of $\rho$, shorter schedules are prefixes of longer schedules, neither $a_{1}$ nor any of the $b_{n}$ sequence in is needed, and they are non-periodic (hence why there is no rate saturation here).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Remark 2.2 (Limit of Silver Stepsize Schedules in the strongly convex case)", "weight": 1.0} -->

We also record a simple closed-form expression for the sum of the first $n = {2^{k} - 1}$ Silver Stepsizes.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Recursive gluing", "weight": 1.0} -->

Here we prove that the Silver Stepsize Schedule has convergence rate $r_{k}$ for smooth convex optimization. The analysis closely mirrors the strongly convex setting in Part I: we prove the advantage of time-varying stepsizes via multi-step descent rather than iterating the greedy 1-step bound, show multi-step descent by exploiting long-range consistency conditions along the GD trajectory, certify multi-step descent via recursive gluing, and recursively glue by combining the same three components in the same way. In the interest of brevity, we refer to for a detailed discussion of all these concepts.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Recursive gluing", "weight": 1.0} -->

Briefly, the idea behind multi-step descent is that it is essential to capture how different iterations affect other iterations' progress. We do this by exploiting long-range consistency conditions between the iterates along GD's trajectory, as encoded by the co-coercivities

<!-- chunk {"id": "body-0017", "role": "body", "section": "Recursive gluing", "weight": 1.0} -->

The significance of these co-coercivities is that the constraints ${\{{Q_{ij} \geqslant 0}\}}_{i \neq j \in {\{ 0,1,\ldots,n, \ast \}}}$ are necessary and sufficient for the existence of a $1$-smooth convex function $f$ satisfying $f_{i} = {f{(x_{i})}}$ and $g_{i} = {{\nabla f}{(x_{i})}}$ for each $i \in {\{ 0,1,\ldots,n, \ast \}}$. In other words, the co-coercivity conditions ${\{{Q_{ij} \geqslant 0}\}}_{i \neq j \in {\{ 0,1,\ldots,n, \ast \}}}$ generate all possible long-range consistency constraints on the objective function $f$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Recursive gluing", "weight": 1.0} -->

Or, said another way, the co-coercivity conditions generate all possible valid inequalities with which one can prove convergence rates for GD. For a further discussion, see \[3, §2.2\].

<!-- chunk {"id": "body-0019", "role": "body", "section": "Recursive gluing", "weight": 1.0} -->

Concretely, to prove Theorem 1.1. ‣ 1.1 Contribution ‣ 1 Introduction ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"), we exhibit explicit non-negative multipliers $\lambda_{ij}$ satisfying

<!-- chunk {"id": "body-0020", "role": "body", "section": "Remark 3.1 (The importance of a composable formulation)", "weight": 1.0} -->

We emphasize that while there are several alternative formulations to (3.2) that imply a rate like (3.3) after dropping terms, our formulation (3.2) is "canonical" because it composes well under recurrence (Theorem 3.4. ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization")). This enables a quite short and simple proof. Another reason this formulation is particularly nice is because the base case $n = 0$ amounts to a re-writing of the definition of $Q_{\ast 0}$, which is an improvement over the standard bound ${f_{0} - f^{\ast}} \leqslant {\frac{1}{2}{\|{x_{0} - x^{\ast}}\|}^{2}}$. In fact, this improvement is precisely what makes recursive gluing work so seamlessly.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Example 3.3 ($n = 1$)", "weight": 1.0} -->

For larger horizons $n$, we construct $\lambda_{ij}$ via the recursive gluing technique of. See Figure 3. Below, we say that the multipliers ${\{\sigma_{ij}\}}_{{i,j} \in {\{ 0,\ldots,n, \ast \}}}$ satisfy the $\ast$-sparsity property if $\sigma_{i \ast} = 0$ for all $i < n$. This is satisfied by construction and simplifies part of the proof (isolated in Lemma 3.5. ‣ 3.1 Helper lemmas ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization")).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Helper lemmas", "weight": 1.0} -->

Here we provide three helper lemmas for the proof of Theorem 3.4. ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"). The first lemma explicitly computes all multipliers involving $x^{\ast}$ for the $n$-step certificate.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Non-negativity", "weight": 1.0} -->

We verify $\lambda_{ij} \geqslant 0$ for all $i \neq j \in {\{ 0,\ldots,{{2n} + 1}, \ast \}}$. For nearly all entries, this is obvious since $\lambda_{ij}$ is constructed by adding and multiplying non-negative numbers. For the remaining entries where either $\Xi$ or $\Delta$ is negative, compute the corresponding entry of $\lambda$ by summing the corrections and using Lemma 3.5. ‣ 3.1 Helper lemmas ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization").

<!-- chunk {"id": "body-0024", "role": "body", "section": "Rate certificate", "weight": 1.0} -->

The identity (3.5. ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization")) has two components: a linear form in the function values and a quadratic form in the iterates and gradients. For the linear form, it suffices to verify ${e - s - \ell} = 0$ by Lemma 3.6. ‣ 3.1 Helper lemmas ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"), where ${e,s,\ell} \in {\mathbb{R}}^{3}$ are the vectors defined in Appendix A.1 ‣ Appendix A Deferred proof details ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"). This is obvious by inspection.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Rate certificate", "weight": 1.0} -->

For the quadratic form, it suffices to verify ${E - S - L} = 0$, where ${E,S,L} \in {\mathbb{R}}^{4 \times 4}$ are the matrices in Lemma 3.7. ‣ 3.1 Helper lemmas ‣ 3 Recursive gluing ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization") defined in Appendix A.2 ‣ Appendix A Deferred proof details ‣ Acceleration by Stepsize Hedging II: Silver Stepsize Schedule for Smooth Convex Optimization"). By plugging in the explicit values for $r_{k}$ and $\Delta$, this is straightforward to check by hand. For brevity, we provide a simple Mathematica script that verifies these identities at the URL.
