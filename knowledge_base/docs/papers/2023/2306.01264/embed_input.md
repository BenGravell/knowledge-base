<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Convex and Non-convex Optimization under Generalized Smoothness

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Classical analysis of convex and non-convex optimization methods often requires the Lipshitzness of the gradient, which limits the analysis to functions bounded by quadratics. Recent work relaxed this requirement to a non-uniform smoothness condition with the Hessian norm bounded by an affine function of the gradient norm, and proved convergence in the non-convex setting via gradient clipping, assuming bounded noise. In this paper, we further generalize this non-uniform smoothness condition and develop a simple, yet powerful analysis technique that bounds the gradients along the trajectory, thereby leading to stronger results for both convex and non-convex optimization problems. In particular, we obtain the classical convergence rates for (stochastic) gradient descent and Nesterov's accelerated gradient method in the convex and/or non-convex setting under this general smoothness condition. The new analysis approach does not require gradient clipping and allows heavy-tailed noise with bounded variance in the stochastic setting.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we study the following *unconstrained* optimization problem where $\mathcal{X} \subseteq {\mathbb{R}}^{d}$ is the domain of $f$. Classical textbook analyses of often require the Lipschitz smoothness condition, which assumes $\left\| {{\nabla^{2}f}{(x)}} \right\| \leq L$ almost everywhere for some $L \geq 0$ called the smoothness constant. This condition, however, is rather restrictive and only satisfied by functions that are both upper and lower bounded by quadratic functions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Recently, Zhang et al. proposed the more general $(L_{0},L_{1})$-smoothness condition, which assumes $\left\| {{\nabla^{2}f}{(x)}} \right\| \leq {L_{0} + {L_{1}\left\| {{\nabla f}{(x)}} \right\|}}$ for some constants ${L_{0},L_{1}} \geq 0$, motivated by their extensive language model experiments. This notion generalizes the standard Lipschitz smoothness condition and also contains e.g. univariate polynomial and exponential functions. For *non-convex* and $(L_{0},L_{1})$-smooth functions, they prove convergence of gradient descent (GD) and stochastic gradient descent (SGD) *with gradient clipping* and also provide a complexity lower bound for *constant-stepsize* GD/SGD without clipping.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Based on these results, they claim gradient clipping or other forms of adaptivity *provably* accelerate the convergence for $(L_{0},L_{1})$-smooth functions. Perhaps due to the lower bound, all the follow-up works under this condition that we are aware of limit their analyses to adaptive methods. Most of these focus on non-convex functions. See Section 2 for more discussions of related works.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we significantly generalize the $(L_{0},L_{1})$-smoothness condition to the $\ell$-smoothness condition which assumes $\left\| {{\nabla^{2}f}{(x)}} \right\| \leq {\ell{(\left\| {{\nabla f}{(x)}} \right\|)}}$ for some non-decreasing continuous function $\ell$. We develop a simple, yet powerful approach, which allows us to obtain stronger results for *both convex and non-convex* optimization problems when $\ell$ is sub-quadratic (i.e., ${\lim_{u\rightarrow\infty}{{\ell{(u)}}/u^{2}}} = 0$) or even more general. The $\ell$-smooth function class with a sub-quadratic $\ell$ also contains e.g. univariate rational and double exponential functions.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In particular, we prove the convergence of *constant-stepsize* GD/SGD and Nesterov's accelerated gradient method (NAG) in the convex or non-convex settings. For each method and setting, we obtain the classical convergence rate, under a certain requirement of $\ell$. In addition, we relax the assumption of bounded noise to the weaker one of bounded variance with the simple SGD method. See Table 1 for a summary of our results and assumptions for each method and setting. At first glance, our results "contradict" the lower bounds on constant-stepsize GD/SGD; this will be reconciled in Section 5.3.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our approach analyzes boundedness of gradients along the optimization trajectory. The idea behind it can be informally illustrated by the following "circular" reasoning. On the one hand, if gradients along the trajectory are bounded by a constant $G$, then the Hessian norms are bounded by the constant $\ell{(G)}$. Informally speaking, we essentially have the standard Lipschitz smoothness condition^11^1This statement is informal because we can only bound Hessian norms *along the trajectory*, rather than almost everywhere within a convex set as in the standard Lipschitz smoothness condition. For example, even if the Hessian norm is bounded at both $x_{t}$ and $x_{t + 1}$, it does not directly mean the Hessian norm is also bounded over the line segment between them, which is required in classical analysis. A more formal statement will need Lemma 3.3 presented later in the paper. and can apply classical textbook analyses to prove convergence, which implies that gradients converge to zero. On the other hand, if gradients converge, they must be bounded, since any convergent sequence is bounded.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In other words, the bounded gradient condition implies convergence, and convergence also implies the condition back, which forms a circular argument. If we can break this circularity of reasoning in a rigorous way, both the bounded gradient condition and convergence are proved. In this paper, we will show how to break the circularity using induction or contradiction arguments for different methods and settings in Sections 4 and 5. We note that the idea of bounding gradients can be applied to the analysis of other optimization methods, e.g., the concurrent work by subset of the authors, which uses a similar idea to obtain a rigorous and improved analysis of the Adam method.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. In light of the above discussions, we summarize our main contributions as follows.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We generalize the standard Lipschitz smoothness and also the $(L_{0},L_{1})$-smoothness condition to the $\ell$-smoothness condition, and develop a new approach for analyzing convergence under this condition by bounding the gradients along the optimization trajectory.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We prove the convergence of *constant-stepsize* GD/SGD/NAG in the convex and non-convex settings, and obtain the classical rates for all of them, as summarized in Table 1.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Besides the generalized smoothness condition and the new approach, our results are also novel in the following aspects.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

The convergence results of *constant-stepsize* methods challenge the folklore belief on the necessity of adaptive stepsize for generalized smooth functions.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

We obtain new convergence results for GD and NAG in the convex setting under the generalized smoothness condition.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

We relax the assumption of bounded noise to the weaker one of bounded variance of noise in the stochastic setting with the simple SGD method.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

Ω(exp. in cond #) (Theorem 5.4) $\mathcal{O}{({1/\sqrt{\epsilon}})}$11footnotemark: 1 (Theorem 4.4) Table 1: Summary of the results. ϵ denotes the sub-optimality gap of the function value in convex settings, and the gradient norm in non-convex settings. “*” denotes optimal rates.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Function class", "weight": 1.0} -->

In this section, we discuss the function class of interest where the objective function $f$ lies. We start with the following two standard assumptions in the literature of unconstrained optimization, which will be assumed throughout Sections 4 and 5 unless explicitly stated.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The objective function $f$ is differentiable and *closed* within its *open* domain $\mathcal{X}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

A function $f$ is said to be closed if its sub-level set $\{{x \in {\operatorname{dom}{(f)}}}\mid{{f{(x)}} \leq a}\}$ is closed for each $a \in {\mathbb{R}}$. A continuous function $f$ with an open domain is closed if and only $f{(x)}$ tends to positive infinity when $x$ approaches the boundary of its domain. Assumption 1 is necessary for our analysis to ensure that the iterates of a method with a reasonably small stepsize stays within the domain $\mathcal{X}$. Note that for $\mathcal{X} = {\mathbb{R}}^{d}$ considered in most unconstrained optimization papers, the assumption is trivially satisfied as all continuous functions over ${\mathbb{R}}^{d}$ are closed. We consider a more general domain which may not be the whole space because that is the case for some interesting examples in our function class of interest (see Section 3.1.3).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

However, it actually brings us some additional technical difficulties especially in the stochastic setting, as we need to make sure the iterates do not go outside of the domain.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Generalized smoothness", "weight": 1.0} -->

In this section, we formally define the generalized smoothness condition, and present its properties and examples.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Definitions", "weight": 1.0} -->

Definitions 1. ‣ 3.1.1 Definitions ‣ 3.1 Generalized smoothness ‣ 3 Function class ‣ Convex and Non-convex Optimization Under Generalized Smoothness") and 2-smoothness). ‣ 3.1.1 Definitions ‣ 3.1 Generalized smoothness ‣ 3 Function class ‣ Convex and Non-convex Optimization Under Generalized Smoothness") below are two equivalent ways of stating the definition, where we use $\mathcal{B}{(x,R)}$ to denote the Euclidean ball with radius $R$ centered at $x$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 3.1", "weight": 1.0} -->

Definition 1. ‣ 3.1.1 Definitions ‣ 3.1 Generalized smoothness ‣ 3 Function class ‣ Convex and Non-convex Optimization Under Generalized Smoothness") reduces to the classical $L$-smoothness when $\ell \equiv L$ is a constant function. It reduces to the $(L_{0},L_{1})$-smoothness proposed in when ${\ell{(u)}} = {L_{0} + {L_{1}u}}$ is an affine function.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Properties", "weight": 1.0} -->

First, we provide the following lemma which is very useful in our analyses of all the methods considered in this paper. Its proof is deferred to Appendix A.3.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 3.4", "weight": 1.0} -->

Since we have shown the equivalence between $\ell$-smoothness and $(r,\ell)$-smoothness, Lemma 3.3 also applies to $\ell$-smooth functions, for which we have $L = {\ell{({2G})}}$ and ${r{(G)}} = {G/L}$ if choosing $a = G$ in Proposition 3.2.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 3.4", "weight": 1.0} -->

Lemma 3.3 states that, if the gradient at $x$ is bounded by some constant $G$, then within its neighborhood with a *constant* radius, we can obtain, the same inequalities that were derived in the textbook analysis under the standard Lipschitz smoothness condition. With, the analysis for generalized smoothness is not much harder than that for standard smoothness. Since we mostly choose $x = x_{2} = x_{t}$ and $x_{1} = x_{t + 1}$ in the analysis, in order to apply Lemma 3.3, we need two conditions: $\left\| {{\nabla f}{(x_{t})}} \right\| \leq G$ and $\left\| {x_{t + 1} - x_{t}} \right\| \leq {r{(G)}}$ for some constant $G$. The latter is usually directly implied by the former for most deterministic methods with a small enough stepsize, and the former can be obtained with our new approach that bounds the gradients along the trajectory.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 3.4", "weight": 1.0} -->

With Lemma 3.3, we can derive the following useful lemma which is the reverse direction of a generalized Polyak-Lojasiewicz (PL) inequality, whose proof is deferred to Appendix A.3.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Examples", "weight": 1.0} -->

The most important subset of $\ell$-smooth (or $(r,\ell)$-smooth) functions are those with a polynomial $\ell$, and can be characterized by the $(\rho,L_{0},L_{\rho})$-smooth function class defined below.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Convex setting", "weight": 1.0} -->

In this section, we present the convergence results of gradient descent (GD) and Nesterov's accelerated gradient method (NAG) in the convex setting. Formally, we define convexity as follows.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Gradient descent", "weight": 1.0} -->

The gradient descent method with a constant stepsize $\eta$ is defined via the following update rule As discussed below Lemma 3.3, the key in the convergence analysis is to show $\left\| {{\nabla f}{(x_{t})}} \right\| \leq G$ for all $t \geq 0$ and some constant $G$. We will prove it by induction relying on the following lemma whose proof is deferred to Appendix B.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Nesterov's accelerated gradient method", "weight": 1.0} -->

0: A convex and ℓ-smooth function f, stepsize η, initial point x0 3: $B_{t + 1} = {B_{t} + {\frac{1}{2}\left({1 + \sqrt{{4B_{t}} + 1}} \right)}}$ Algorithm 1 Nesterov’s Accelerated Gradient Method (NAG) In the case of convex and standard Lipschitz smooth functions, it is well known that Nesterov's accelerated gradient method (NAG) achieves the optimal $\mathcal{O}{({1/T^{2}})}$ rate.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Nesterov's accelerated gradient method", "weight": 1.0} -->

In this section, we show that under the $\ell$-smoothness condition with a *sub-quadratic* $\ell$, the optimal $\mathcal{O}{({1/T^{2}})}$ rate can be achieved by a slightly modified version of NAG shown in Algorithm 1, the only difference between which and the classical NAG is that the latter directly sets $A_{t + 1} = B_{t + 1}$ in Line 4. Formally, we have the following theorem, whose proof is deferred to Appendix C.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Non-convex setting", "weight": 1.0} -->

In this section, we present convergence results of gradient descent (GD) and stochastic gradient descent (SGD) in the non-convex setting.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Gradient descent", "weight": 1.0} -->

Similar to the convex setting, we still want to bound the gradients along the trajectory. However, in the non-convex setting, the gradient norm is not necessarily non-increasing. Fortunately, similar to the classical analyses, the function value is still non-increasing and thus a potential function, as formally shown in the following lemma, whose proof is deferred to Appendix E.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Stochastic gradient descent", "weight": 1.0} -->

In this part, we present the convergence result for stochastic gradient descent defined as follows. where $g_{t}$ is an estimate of the gradient ${\nabla f}{(x_{t})}$. We consider the following standard assumption on the gradient noise $\epsilon_{t}:={g_{t} - {{\nabla f}{(x_{t})}}}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Assumption 4", "weight": 1.0} -->

Under Assumption 4, we can obtain the following theorem.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Reconciliation with existing lower bounds", "weight": 1.0} -->

In this section, we reconcile our convergence results for constant-stepsize GD/SGD in the non-convex setting with existing lower bounds in and, based on which the authors claim that adaptive methods such as GD/SGD with clipping and Adam are provably faster than non-adaptive GD/SGD. This may seem to contradict our convergence results. In fact, we show that any gain in adaptive methods is at most by constant factors, as GD and SGD already achieve the optimal rates in the non-convex setting. provides both upper and lower complexity bounds for constant-stepsize GD for $(L_{0},L_{1})$-smooth functions, and shows that its complexity is $\mathcal{O}{({M\epsilon^{- 2}})}$, where is the supremum gradient norm below the level set of the initial function value.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Reconciliation with existing lower bounds", "weight": 1.0} -->

If $M$ is very large, then the $\mathcal{O}{({M\epsilon^{- 2}})}$ complexity can be viewed as a negative result, and as evidence that constant-stepsize GD can be slower than GD with gradient clipping, since in the latter case, they obtain the $\mathcal{O}{(\epsilon^{- 2})}$ complexity without $M$. However, based on our Corollary 3.6, their $M$ can be actually bounded by our $G$, which is a constant. Therefore, the gain in adaptive methods is at most by constant factors. further provides a lower bound which shows non-adaptive GD may diverge for some examples. However, their counter-example does not allow the stepsize to depend on the initial sub-optimality gap. In contrast, our stepsize $\eta$ depends on the effective smoothness constant $L$, which depends on the initial sub-optimality gap through $G$. Therefore, there is no contradiction here either.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Reconciliation with existing lower bounds", "weight": 1.0} -->

We should point out that in the practice of training neural networks, the stepsize is usually tuned after fixing the loss function and initialization, so it does depend on the problem instance and initialization.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Lower bound", "weight": 1.0} -->

For $(\rho,L_{0},L_{\rho})$-smooth functions with $\rho < 2$, it is easy to verify that the constant $G$ in both Theorem 5.2 and Theorem 5.3 is a polynomial function of problem-dependent parameters like $L_{0},L_{\rho},{{f{(x_{0})}} - f^{\ast}},\sigma$, etc. In other words, GD and SGD are provably efficient methods in the non-convex setting for $\rho < 2$. In this section, we show that the requirement of $\rho < 2$ is necessary in the non-convex setting with the lower bound for GD in the following Theorem 5.4, whose proof is deferred in Appendix G. Since SGD reduces to GD when there is no gradient noise, it is also a lower bound for SGD.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we generalize the standard Lipschitz smoothness as well as the $(L_{0},L_{1})$-smoothness conditions to the $\ell$-smoothness condition, and develop a new approach for analyzing the convergence under this condition. The approach uses different techniques for several methods and settings to bound the gradient along the optimization trajectory, which allows us to obtain stronger results for both convex and non-convex problems. We obtain the classical rates for GD/SGD/NAG methods in the convex and/or non-convex setting. Our results challenge the folklore belief on the necessity of adaptive methods for generalized smooth functions.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Conclusion", "weight": 1.5} -->

There are several interesting future directions following this work. First, the $\ell$-smoothness can perhaps be further generalized by allowing $\ell$ to also depend on potential functions in each setting, besides the gradient norm. In addition, it would also be interesting to see if the techniques of bounding gradients along the trajectory that we have developed in this and the concurrent work can be further generalized to other methods and problems and to see whether more efficient algorithms can be obtained. Finally, although we justified the necessity of the requirement of $\ell$-smoothness with a *sub-quadratic* $\ell$ in the non-convex setting, it is not clear whether it is also necessary for NAG in the convex setting, another interesting open problem.
