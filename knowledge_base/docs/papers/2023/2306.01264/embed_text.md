## Introduction

In this paper, we study the following *unconstrained* optimization problem where $\mathcal{X} \subseteq {\mathbb{R}}^{d}$ is the domain of $f$. Classical textbook analyses of often require the Lipschitz smoothness condition, which assumes $\left\| {{\nabla^{2}f}{(x)}} \right\| \leq L$ almost everywhere for some $L \geq 0$ called the smoothness constant. This condition, however, is rather restrictive and only satisfied by functions that are both upper and lower bounded by quadratic functions.

Recently, Zhang et al. proposed the more general $(L_{0},L_{1})$-smoothness condition, which assumes $\left\| {{\nabla^{2}f}{(x)}} \right\| \leq {L_{0} + {L_{1}\left\| {{\nabla f}{(x)}} \right\|}}$ for some constants ${L_{0},L_{1}} \geq 0$, motivated by their extensive language model experiments. This notion generalizes the standard Lipschitz smoothness condition and also contains e.g. univariate polynomial and exponential functions. For *non-convex* and $(L_{0},L_{1})$-smooth functions, they prove convergence of gradient descent (GD) and stochastic gradient descent (SGD) *with gradient clipping* and also provide a complexity lower bound for *constant-stepsize* GD/SGD without clipping. Based on these results, they claim gradient clipping or other forms of adaptivity *provably* accelerate the convergence for $(L_{0},L_{1})$-smooth functions. Perhaps due to the lower bound, all the follow-up works under this condition that we are aware of limit their analyses to adaptive methods. Most of these focus on non-convex functions. See Section 2 for more discussions of related works.

In this paper, we significantly generalize the $(L_{0},L_{1})$-smoothness condition to the $\ell$-smoothness condition which assumes $\left\| {{\nabla^{2}f}{(x)}} \right\| \leq {\ell{(\left\| {{\nabla f}{(x)}} \right\|)}}$ for some non-decreasing continuous function $\ell$. We develop a simple, yet powerful approach, which allows us to obtain stronger results for *both convex and non-convex* optimization problems when $\ell$ is sub-quadratic (i.e., ${\lim_{u\rightarrow\infty}{{\ell{(u)}}/u^{2}}} = 0$) or even more general. The $\ell$-smooth function class with a sub-quadratic $\ell$ also contains e.g. univariate rational and double exponential functions. In particular, we prove the convergence of *constant-stepsize* GD/SGD and Nesterov's accelerated gradient method (NAG) in the convex or non-convex settings. For each method and setting, we obtain the classical convergence rate, under a certain requirement of $\ell$. In addition, we relax the assumption of bounded noise to the weaker one of bounded variance with the simple SGD method. See Table 1 for a summary of our results and assumptions for each method and setting. At first glance, our results "contradict" the lower bounds on constant-stepsize GD/SGD ; this will be reconciled in Section 5.3.

Our approach analyzes boundedness of gradients along the optimization trajectory. The idea behind it can be informally illustrated by the following "circular" reasoning. On the one hand, if gradients along the trajectory are bounded by a constant $G$, then the Hessian norms are bounded by the constant $\ell{(G)}$. Informally speaking, we essentially have the standard Lipschitz smoothness condition^11^1This statement is informal because we can only bound Hessian norms *along the trajectory*, rather than almost everywhere within a convex set as in the standard Lipschitz smoothness condition. For example, even if the Hessian norm is bounded at both $x_{t}$ and $x_{t + 1}$, it does not directly mean the Hessian norm is also bounded over the line segment between them, which is required in classical analysis. A more formal statement will need Lemma 3.3 presented later in the paper. and can apply classical textbook analyses to prove convergence, which implies that gradients converge to zero. On the other hand, if gradients converge, they must be bounded, since any convergent sequence is bounded. In other words, the bounded gradient condition implies convergence, and convergence also implies the condition back, which forms a circular argument. If we can break this circularity of reasoning in a rigorous way, both the bounded gradient condition and convergence are proved. In this paper, we will show how to break the circularity using induction or contradiction arguments for different methods and settings in Sections 4 and 5. We note that the idea of bounding gradients can be applied to the analysis of other optimization methods, e.g., the concurrent work by subset of the authors, which uses a similar idea to obtain a rigorous and improved analysis of the Adam method.

Contributions. In light of the above discussions, we summarize our main contributions as follows.

We generalize the standard Lipschitz smoothness and also the $(L_{0},L_{1})$-smoothness condition to the $\ell$-smoothness condition, and develop a new approach for analyzing convergence under this condition by bounding the gradients along the optimization trajectory.

We prove the convergence of *constant-stepsize* GD/SGD/NAG in the convex and non-convex settings, and obtain the classical rates for all of them, as summarized in Table 1.

Besides the generalized smoothness condition and the new approach, our results are also novel in the following aspects.

The convergence results of *constant-stepsize* methods challenge the folklore belief on the necessity of adaptive stepsize for generalized smooth functions.

We obtain new convergence results for GD and NAG in the convex setting under the generalized smoothness condition.

We relax the assumption of bounded noise to the weaker one of bounded variance of noise in the stochastic setting with the simple SGD method.

Ω(exp. in cond #) (Theorem 5.4) $\mathcal{O}{({1/\sqrt{\epsilon}})}$11footnotemark: 1 (Theorem 4.4) Table 1: Summary of the results. ϵ denotes the sub-optimality gap of the function value in convex settings, and the gradient norm in non-convex settings. “*” denotes optimal rates.

## Related work

Gradient-based optimizaiton. The classical gradient-based optimization problems for the standard Lipschitz smooth functions have been well studied for both convex and non-convex functions. In the convex setting, the goal is to reach an $\epsilon$-sub-optimal point $x$ satisfying ${{f{(x)}} - {\inf_{x}{f{(x)}}}} \leq \epsilon$. It is well known that GD achieves the $\mathcal{O}{({1/\epsilon})}$ gradient complexity and NAG achieves the accelerated $\mathcal{O}{({1/\sqrt{\epsilon}})}$ complexity which is optimal among all gradient-based methods. For strongly convex functions, GD and NAG achieve the $\mathcal{O}{({\kappa{\log{({1/\epsilon})}}})}$ and $\mathcal{O}{({\sqrt{\kappa}{\log{({1/\epsilon})}}})}$ complexity respectively, where $\kappa$ is the condition number and the latter is again optimal. In the non-convex setting, the goal is to find an $\epsilon$-stationary point $x$ satisfying $\left\| {{\nabla f}{(x)}} \right\| \leq \epsilon$, since finding a global minimum is NP-hard in general. It is well known that GD achieves the optimal $\mathcal{O}{({1/\epsilon^{2}})}$ complexity which matches the lower bound . In the stochastic setting for unbiased stochastic gradient with bounded variance, SGD achieves the optimal $\mathcal{O}{({1/\epsilon^{4}})}$ complexity, matching the lower bound . In this paper, we obtain the classical rates in terms of $\epsilon$ for all the above-mentioned methods and settings, under a far more general smoothness condition.

Generalized smoothness. The $(L_{0},L_{1})$-smoothness condition proposed by Zhang et al. was studied by many follow-up works. Under the same condition, considers momentum in the updates and improves the constant dependency of the convergence rate for SGD with clipping derived . studies gradient clipping in incremental gradient methods, studies stochastic normalized gradient descent, and studies a generalized SignSGD method, under the $(L_{0},L_{1})$-smoothess condition. studies variance reduction for $(L_{0},L_{1})$-smooth functions. proposes a new notion of $\alpha$-symmetric generalized smoothness, which is roughly as general as $(L_{0},L_{1})$-smoothness. analyzes convergence of Adam and provides a lower bound which shows non-adaptive SGD may diverge. In the stochastic setting, the above-mentioned works either consider the strong assumption of bounded gradient noise or require a very large batch size that depends on $\epsilon$, which essentially reduces the analysis to the deterministic setting. proposes an AdaGrad-type algorithm in order to relax the bounded noise assumption. Perhaps due to the lower bounds , all the above works study methods with an adaptive stepsize. In this and our concurrent work, we further generalize the smoothness condition and analyze various methods under this condition through bounding the gradients along the trajectory.

## Function class

In this section, we discuss the function class of interest where the objective function $f$ lies. We start with the following two standard assumptions in the literature of unconstrained optimization, which will be assumed throughout Sections 4 and 5 unless explicitly stated.

### Assumption 1

The objective function $f$ is differentiable and *closed* within its *open* domain $\mathcal{X}$.

### Assumption 2

The objective function $f$ is bounded from below, i.e., $f^{\ast}:={\inf_{x \in \mathcal{X}}{f{(x)}}} > {- \infty}$.

A function $f$ is said to be closed if its sub-level set $\{{x \in {\operatorname{dom}{(f)}}}\mid{{f{(x)}} \leq a}\}$ is closed for each $a \in {\mathbb{R}}$. A continuous function $f$ with an open domain is closed if and only $f{(x)}$ tends to positive infinity when $x$ approaches the boundary of its domain. Assumption 1 is necessary for our analysis to ensure that the iterates of a method with a reasonably small stepsize stays within the domain $\mathcal{X}$. Note that for $\mathcal{X} = {\mathbb{R}}^{d}$ considered in most unconstrained optimization papers, the assumption is trivially satisfied as all continuous functions over ${\mathbb{R}}^{d}$ are closed. We consider a more general domain which may not be the whole space because that is the case for some interesting examples in our function class of interest (see Section 3.1.3). However, it actually brings us some additional technical difficulties especially in the stochastic setting, as we need to make sure the iterates do not go outside of the domain.

### Generalized smoothness

In this section, we formally define the generalized smoothness condition, and present its properties and examples.

### Definitions

Definitions 1. ‣ 3.1.1 Definitions ‣ 3.1 Generalized smoothness ‣ 3 Function class ‣ Convex and Non-convex Optimization Under Generalized Smoothness") and 2-smoothness). ‣ 3.1.1 Definitions ‣ 3.1 Generalized smoothness ‣ 3 Function class ‣ Convex and Non-convex Optimization Under Generalized Smoothness") below are two equivalent ways of stating the definition, where we use $\mathcal{B}{(x,R)}$ to denote the Euclidean ball with radius $R$ centered at $x$.

### Definition 1 ($\ell$-smoothness)

A real-valued differentiable function $f:{\mathcal{X}\rightarrow{\mathbb{R}}}$ is $\ell$-smooth for some non-decreasing continuous function $\ell:{{\lbrack 0,{+ \infty})}\rightarrow{(0,{+ \infty})}}$ if $\left\| {{\nabla^{2}f}{(x)}} \right\| \leq {\ell{(\left\| {{\nabla f}{(x)}} \right\|)}}$ *almost everywhere* (with respect to the Lebesgue measure) in $\mathcal{X}$.

### Remark 3.1

Definition 1. ‣ 3.1.1 Definitions ‣ 3.1 Generalized smoothness ‣ 3 Function class ‣ Convex and Non-convex Optimization Under Generalized Smoothness") reduces to the classical $L$-smoothness when $\ell \equiv L$ is a constant function. It reduces to the $(L_{0},L_{1})$-smoothness proposed in when ${\ell{(u)}} = {L_{0} + {L_{1}u}}$ is an affine function.

### Definition 2 ($(r,\ell)$-smoothness)

A real-valued differentiable function $f:{\mathcal{X}\rightarrow{\mathbb{R}}}$ is $(r,\ell)$-smooth for continuous functions ${r,\ell}:{{\lbrack 0,{+ \infty})}\rightarrow{(0,{+ \infty})}}$ where $\ell$ is non-decreasing and $r$ is non-increasing, if it satisfies 1) for any $x \in \mathcal{X}$, ${\mathcal{B}{(x,{r{(\left\| {{\nabla f}{(x)}} \right\|)}})}} \subseteq \mathcal{X}$, and 2) for any ${x_{1},x_{2}} \in {\mathcal{B}{(x,{r{(\left\| {{\nabla f}{(x)}} \right\|)}})}}$, $\left\| {{{\nabla f}{(x_{1})}} - {{\nabla f}{(x_{2})}}} \right\| \leq {{\ell{(\left\| {{\nabla f}{(x)}} \right\|)}} \cdot \left\| {x_{1} - x_{2}} \right\|}$.

The requirements that $\ell$ is non-decreasing and $r$ is non-increasing do not cause much loss in generality. If these conditions are not satisfied, one can replace $\ell$ and $r$ with the non-increasing function ${\overset{\sim}{r}{(u)}}:={\inf_{0 \leq v \leq u}{r{(v)}}} \leq {r{(u)}}$ and non-decreasing function ${\overset{\sim}{\ell}{(u)}}:={\sup_{0 \leq v \leq u}{\ell{(v)}}} \geq {\ell{(u)}}$ in Definitions 1. ‣ 3.1.1 Definitions ‣ 3.1 Generalized smoothness ‣ 3 Function class ‣ Convex and Non-convex Optimization Under Generalized Smoothness") and 2-smoothness). ‣ 3.1.1 Definitions ‣ 3.1 Generalized smoothness ‣ 3 Function class ‣ Convex and Non-convex Optimization Under Generalized Smoothness"). Then the only requirement is $\overset{\sim}{r} > 0$ and $\overset{\sim}{\ell} < \infty$.

Next, we prove that the above two definitions are equivalent in the following proposition, whose proof is involved and deferred to Appendix A.2.

### Proposition 3.2

An $(r,\ell)$-smooth function is $\ell$-smooth; and an $\ell$-smooth function satisfying Assumption 1 is $(r,m)$-smooth where ${m{(u)}}:={\ell{({u + a})}}$ and ${r{(u)}}:={{a/m}{(u)}}$ for any $a > 0$.

The condition in Definition 1. ‣ 3.1.1 Definitions ‣ 3.1 Generalized smoothness ‣ 3 Function class ‣ Convex and Non-convex Optimization Under Generalized Smoothness") is simple and one can easily check whether it is satisfied for a given example function. On the other hand, Definition 2-smoothness). ‣ 3.1.1 Definitions ‣ 3.1 Generalized smoothness ‣ 3 Function class ‣ Convex and Non-convex Optimization Under Generalized Smoothness") is a local Lipschitz condition on the gradient that is harder to verify. However, it is useful for deriving several useful properties in the next section.

### Properties

First, we provide the following lemma which is very useful in our analyses of all the methods considered in this paper. Its proof is deferred to Appendix A.3.

### Lemma 3.3

If $f$ is $(r,\ell)$-smooth, for any $x \in \mathcal{X}$ satisfying $\left\| {{\nabla f}{(x)}} \right\| \leq G$, we have 1) ${\mathcal{B}{(x,{r{(G)}})}} \subseteq \mathcal{X}$, and 2) for any ${x_{1},x_{2}} \in {\mathcal{B}{(x,{r{(G)}})}}$, where $L:={\ell{(G)}}$ is the *effective smoothness constant*.

### Remark 3.4

Since we have shown the equivalence between $\ell$-smoothness and $(r,\ell)$-smoothness, Lemma 3.3 also applies to $\ell$-smooth functions, for which we have $L = {\ell{({2G})}}$ and ${r{(G)}} = {G/L}$ if choosing $a = G$ in Proposition 3.2.

Lemma 3.3 states that, if the gradient at $x$ is bounded by some constant $G$, then within its neighborhood with a *constant* radius, we can obtain, the same inequalities that were derived in the textbook analysis under the standard Lipschitz smoothness condition. With, the analysis for generalized smoothness is not much harder than that for standard smoothness. Since we mostly choose $x = x_{2} = x_{t}$ and $x_{1} = x_{t + 1}$ in the analysis, in order to apply Lemma 3.3, we need two conditions: $\left\| {{\nabla f}{(x_{t})}} \right\| \leq G$ and $\left\| {x_{t + 1} - x_{t}} \right\| \leq {r{(G)}}$ for some constant $G$. The latter is usually directly implied by the former for most deterministic methods with a small enough stepsize, and the former can be obtained with our new approach that bounds the gradients along the trajectory.

With Lemma 3.3, we can derive the following useful lemma which is the reverse direction of a generalized Polyak-Lojasiewicz (PL) inequality, whose proof is deferred to Appendix A.3.

### Lemma 3.5

If $f$ is $\ell$-smooth, then $\left\| {{\nabla f}{(x)}} \right\|^{2} \leq {{2\ell{({2\left\| {{\nabla f}{(x)}} \right\|})}} \cdot {({{f{(x)}} - f^{\ast}})}}$ for any $x \in \mathcal{X}$.

Lemma 3.5 provides an inequality involving the gradient norm and the sub-optimality gap. For example, when ${\ell{(u)}} = u^{\rho}$ for some $0 \leq \rho < 2$, this lemma suggests $\left\| {{\nabla f}{(x)}} \right\| \leq {\mathcal{O}\left( {({{f{(x)}} - f^{\ast}})}^{1/{({2 - \rho})}} \right)}$, which means the gradient norm is bounded whenever the function value is bounded. The following corollary provides a more formal statement for general sub-quadratic $\ell$ (i.e., ${\lim_{u\rightarrow\infty}{{\ell{(u)}}/u^{2}}} = 0$), and we defer its proof to Appendix A.3.

### Corollary 3.6

Suppose $f$ is $\ell$-smooth where $\ell$ is sub-quadratic. If ${{f{(x)}} - f^{\ast}} \leq F$ for some $x \in \mathcal{X}$ and $F \geq 0$, denoting $G:={\sup{\{{u \geq 0}\mid{u^{2} \leq {{2\ell{({2u})}} \cdot F}}\}}}$, then they satisfy $G^{2} = {{2\ell{({2G})}} \cdot F}$ and we have $\left\| {{\nabla f}{(x)}} \right\| \leq G < \infty$.

Therefore, in order to bound the gradients along the trajectory as we discussed below Lemma 3.3, it suffices to bound the function values, which is usually easier.

### Examples

The most important subset of $\ell$-smooth (or $(r,\ell)$-smooth) functions are those with a polynomial $\ell$, and can be characterized by the $(\rho,L_{0},L_{\rho})$-smooth function class defined below.

### Definition 3 ($(\rho,L_{0},L_{\rho})$-smoothness)

A real-valued differentiable function $f$ is $(\rho,L_{0},L_{\rho})$-smooth for constants ${\rho,L_{0},L_{\rho}} \geq 0$ if it is $\ell$-smooth with ${\ell{(u)}} = {L_{0} + {L_{\rho}u^{\rho}}}$.

Definition 3-smoothness). ‣ 3.1.3 Examples ‣ 3.1 Generalized smoothness ‣ 3 Function class ‣ Convex and Non-convex Optimization Under Generalized Smoothness") reduces to the standard Lipschitz smoothness condition when $\rho = 0$ or $L_{\rho} = 0$ and to the $(L_{0},L_{1})$-smoothness proposed in when $\rho = 1$. We list several univariate examples of $(\rho,L_{0},L_{\rho})$-smooth functions for different $\rho$s in Table 2 with their rigorous justifications in Appendix A.1. Note that when $x$ goes to infinity, polynomial and exponential functions corresponding to $\rho = 1$ grow much faster than quadratic functions corresponding to $\rho = 0$. Rational and logarithmic functions for $\rho > 1$ grow even faster as they can blow up to infinity near finite points. Note that the domains of such functions are not ${\mathbb{R}}^{d}$, which is why we consider the more general Assumption 1 instead of simply assuming $\mathcal{X} = {\mathbb{R}}^{d}$.

Aside from logarithmic functions, the $(2,L_{0},L_{2})$-smooth function class also includes other univariate *self-concordant* functions. This is an important function class in the analysis of Interior Point Methods and coordinate-free analysis of the Newton method. More specifically, a convex function $h:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ is self-concordant if $\left| {h^{\operatorname{\prime\prime\prime}}{(x)}} \right| \leq {2h^{\operatorname{\prime\prime}}{(x)}^{3/2}}$ for all $x \in {\mathbb{R}}$. Formally, we have the following proposition whose proof is deferred to Appendix A.1.

### Proposition 3.7

If $h:{{\mathbb{R}}\rightarrow{\mathbb{R}}}$ is a self-concordant function satisfying ${h^{\operatorname{\prime\prime}}{(x)}} > 0$ over the interval $(a,b)$, then $h$ restricted on $(a,b)$ is $(2,L_{0},2)$-smooth for some $L_{0} > 0$.

Table 2: Examples of univariate (ρ, L0, Lρ) smooth functions for different ρs. The parameters a, b, p are real numbers (not necessarily integers) satisfying a, b > 1 and p < 1 or p ≥ 2. We use 1+ to denote any real number slightly larger than 1.

## Convex setting

In this section, we present the convergence results of gradient descent (GD) and Nesterov's accelerated gradient method (NAG) in the convex setting. Formally, we define convexity as follows.

### Definition 4

A real-valued differentiable function $f:{\mathcal{X}\rightarrow{\mathbb{R}}}$ is $\mu$-strongly-convex for $\mu \geq 0$ if $\mathcal{X}$ is a convex set and ${{f{(y)}} - {f{(x)}}} \geq {\left\langle {{\nabla f}{(x)}},{y - x} \right\rangle + {\frac{\mu}{2}\left\| {y - x} \right\|^{2}}}$ for any ${x,y} \in \mathcal{X}$. A function is convex if it is $\mu$-strongly-convex with $\mu = 0$.

We assume the existence of a global optimal point $x^{\ast}$ throughout this section, as in the following assumption. However, we want to note that, for gradient descent, this assumption is just for simplicity rather than necessary.

### Assumption 3

There exists a point $x^{\ast} \in \mathcal{X}$ such that ${f{(x^{\ast})}} = f^{\ast} = {\inf_{x \in \mathcal{X}}{f{(x)}}}$.

### Gradient descent

The gradient descent method with a constant stepsize $\eta$ is defined via the following update rule As discussed below Lemma 3.3, the key in the convergence analysis is to show $\left\| {{\nabla f}{(x_{t})}} \right\| \leq G$ for all $t \geq 0$ and some constant $G$. We will prove it by induction relying on the following lemma whose proof is deferred to Appendix B.

### Lemma 4.1

For any $x \in \mathcal{X}$ satisfying $\left\| {{\nabla f}{(x)}} \right\| \leq G$, define $x^{+}:={x - {\eta{\nabla f}{(x)}}}$. If $f$ is convex and $(r,\ell)$-smooth, and $\eta \leq {\min\left\{ \frac{2}{\ell{(G)}},\frac{r{(G)}}{2G} \right\}}$, we have $x^{+} \in \mathcal{X}$ and $\left\| {{\nabla f}{(x^{+})}} \right\| \leq \left\| {{\nabla f}{(x)}} \right\| \leq G$.

Lemma 4.1 suggests that for gradient descent with a small enough stepsize, if the gradient norm at $x_{t}$ is bounded by $G$, then we have $\left\| {{\nabla f}{(x_{t + 1})}} \right\| \leq \left\| {{\nabla f}{(x_{t})}} \right\| \leq G$, i.e., the gradient norm is also bounded by $G$ at $t + 1$. In other words, the gradient norm is indeed a non-increasing potential function for gradient descent in the convex setting. With a standard induction argument, we can show that $\left\| {{\nabla f}{(x_{t})}} \right\| \leq \left\| {{\nabla f}{(x_{0})}} \right\|$ for all $t \geq 0$. As discussed below Lemma 3.3, then we can basically apply the classical analysis to obtain the convergence guarantee in the convex setting as in the following theorem, whose proof is deferred to Appendix B.

### Theorem 4.2

Suppose $f$ is convex and $(r,\ell)$-smooth. Denote $G:=\left\| {{\nabla f}{(x_{0})}} \right\|$ and $L:={\ell{(G)}}$, then the iterates generated by with $\eta \leq {\min\left\{ \frac{1}{L},\frac{r{(G)}}{2G} \right\}}$ satisfy $\left\| {{\nabla f}{(x_{t})}} \right\| \leq G$ for all $t \geq 0$ and Since $\eta$ is a constant independent of $\epsilon$ or $T$, Theorem 4.2 achieves the classical $\mathcal{O}{({1/T})}$ rate, or $\mathcal{O}{({1/\epsilon})}$ gradient complexity to achieve an $\epsilon$-sub-optimal point, under the generalized smoothness condition. Since strongly convex functions are a subset of convex functions, Lemma 4.1 still holds for them. Then we immediately obtain the following result in the strongly convex setting, whose proof is deferred to Appendix B.

### Theorem 4.3

Suppose $f$ is $\mu$-strongly-convex and $(r,\ell)$-smooth. Denote $G:=\left\| {{\nabla f}{(x_{0})}} \right\|$ and $L:={\ell{(G)}}$, then the iterates generated by with $\eta \leq {\min\left\{ \frac{1}{L},\frac{r{(G)}}{2G} \right\}}$ satisfy $\left\| {{\nabla f}{(x_{t})}} \right\| \leq G$ for all $t \geq 0$ and Theorem 4.3 gives a linear convergence rate and the $\mathcal{O}{({{({\eta\mu})}^{- 1}{\log{({1/\epsilon})}}})}$ gradient complexity to achieve an $\epsilon$-sub-optimal point. Note that for $\ell$-smooth functions, we have $\frac{r{(G)}}{G} = \frac{1}{L}$ (see Remark 3.4), which means we can choose $\eta = \frac{1}{2L}$. Then we obtain the $\mathcal{O}{({\kappa{\log{({1/\epsilon})}}})}$ rate, where $\kappa:={L/\mu}$ is the local condition number around the initial point $x_{0}$. For standard Lipschitz smooth functions, it reduces to the classical rate of gradient descent.

### Nesterov's accelerated gradient method

0: A convex and ℓ-smooth function f, stepsize η, initial point x0 3: $B_{t + 1} = {B_{t} + {\frac{1}{2}\left({1 + \sqrt{{4B_{t}} + 1}} \right)}}$ Algorithm 1 Nesterov’s Accelerated Gradient Method (NAG) In the case of convex and standard Lipschitz smooth functions, it is well known that Nesterov's accelerated gradient method (NAG) achieves the optimal $\mathcal{O}{({1/T^{2}})}$ rate. In this section, we show that under the $\ell$-smoothness condition with a *sub-quadratic* $\ell$, the optimal $\mathcal{O}{({1/T^{2}})}$ rate can be achieved by a slightly modified version of NAG shown in Algorithm 1, the only difference between which and the classical NAG is that the latter directly sets $A_{t + 1} = B_{t + 1}$ in Line 4. Formally, we have the following theorem, whose proof is deferred to Appendix C.

### Theorem 4.4

Suppose $f$ is convex and $\ell$-smooth where $\ell$ is sub-quadratic. Then there always exists a constant $G$ satisfying ${G \geq {\max\left\{ {8\sqrt{\ell{({2G})}{({{({{f{(x_{0})}} - f^{\ast}})} + \left\| {x_{0} - x^{\ast}} \right\|^{2}})}}},\left\| {{\nabla f}{(x_{0})}} \right\| \right\}}}.$ Denote $L:={\ell{({2G})}}$ and choose $\eta \leq {\min\left\{ \frac{1}{16L^{2}},\frac{1}{2L} \right\}}$. The iterates generated by Algorithm 1 satisfy It is easy to note that Theorem 4.4 achieves the accelerated $\mathcal{O}{({1/T^{2}})}$ convergence rate, or equivalently the $\mathcal{O}{({1/\sqrt{\epsilon}})}$ gradient complexity to find an $\epsilon$-sub-optimal point, which is optimal among gradient-based methods.

In order to prove Theorem 4.4, we also use induction to show the gradients along the trajectory of Algorithm 1 are bounded by $G$. However, unlike gradient descent, the gradient norm is no longer a potential function or monotonically non-increasing, which makes the induction analysis more challenging. Suppose that we have shown $\left\| {{\nabla f}{(y_{s})}} \right\| \leq G$ for $s < t$. To complete the induction, it suffices to prove $\left\| {{\nabla f}{(y_{t})}} \right\| \leq G$. Since $x_{t} = {y_{t - 1} - {\eta{\nabla f}{(y_{t - 1})}}}$ is a gradient descent step by Line 6 of Algorithm 1, Lemma 4.1 directly shows $\left\| {{\nabla f}{(x_{t})}} \right\| \leq G$. In order to also bound $\left\| {{\nabla f}{(y_{t})}} \right\|$, we try to control $\left\| {y_{t} - x_{t}} \right\|$, which is the most challenging part of our proof. Since $y_{t} - x_{t}$ can be expressed as a linear combination of past gradients ${\{{{\nabla f}{(y_{s})}}\}}_{s < t}$, it might grow linearly with $t$ if we simply apply $\left\| {{\nabla f}{(y_{s})}} \right\| \leq G$ for $s < t$. Fortunately, Lemma 3.5 allows us to control the gradient norm with the function value. Thus if the function value is decreasing sufficiently fast, which can be shown by following the standard Lyapunov analysis of NAG, we are able to obtain a good enough bound on $\left\| {{\nabla f}{(y_{s})}} \right\|$ for $s < t$, which allows us to control $\left\| {y_{t} - x_{t}} \right\|$. We defer the detailed proof to Appendix C.

Note that Theorem 4.4 requires a smaller stepsize $\eta = {\mathcal{O}{({1/L^{2}})}}$, compared to the classical $\mathcal{O}{({1/L})}$ stepsize for standard Lipschitz smooth functions. The reason is we require a small enough stepsize to get a good enough bound on $\left\| {y_{t} - x_{t}} \right\|$. However, if the function is further assumed to be $\ell$-smooth with a *sub-linear* $\ell$, the requirement of stepsize can be relaxed to $\eta = {\mathcal{O}{({1/L})}}$, similar to the classical requirement. See Appendix C for the details.

In the strongly convex setting, we can also prove convergence of NAG with different ${\{ A_{t}\}}_{t \geq 0}$ parameters when $f$ is $\ell$-smooth with a sub-quadratic $\ell$, or $(\rho,L_{0},L_{\rho})$-smooth with $\rho < 2$. The rate can be further improved when $\rho$ becomes smaller. However, since the constants $G$ and $L$ are different for GD and NAG, it is not clear whether the rate of NAG is faster than that of GD in the strongly convex setting. We will present the detailed result and analysis in Appendix D.

## Non-convex setting

In this section, we present convergence results of gradient descent (GD) and stochastic gradient descent (SGD) in the non-convex setting.

### Gradient descent

Similar to the convex setting, we still want to bound the gradients along the trajectory. However, in the non-convex setting, the gradient norm is not necessarily non-increasing. Fortunately, similar to the classical analyses, the function value is still non-increasing and thus a potential function, as formally shown in the following lemma, whose proof is deferred to Appendix E.

### Lemma 5.1

Suppose $f$ is $\ell$-smooth where $\ell$ is sub-quadratic. For any given $F \geq 0$, let $G:={\sup\left\{ {u \geq 0}\mid{u^{2} \leq {{2\ell{({2u})}} \cdot F}} \right\}}$ and $L:={\ell{({2G})}}$. For any $x \in \mathcal{X}$ satisfying ${{f{(x)}} - f^{\ast}} \leq F$, define $x^{+}:={x - {\eta{\nabla f}{(x)}}}$ where $\eta \leq {2/L}$, we have $x^{+} \in \mathcal{X}$ and ${f{(x^{+})}} \leq {f{(x)}}$.

Then using a standard induction argument, we can show ${f{(x_{t})}} \leq {f{(x_{0})}}$ for all $t \geq 0$. According to Corollary 3.6, it implies bounded gradients along the trajectory. Therefore, we can show convergence of gradient descent as in the following theorem, whose proof is deferred to Appendix E.

### Theorem 5.2

Suppose $f$ is $\ell$-smooth where $\ell$ is sub-quadratic. Let $G:={\sup\left\{ {u \geq 0}\mid{u^{2} \leq {{2\ell{({2u})}} \cdot {({{f{(x_{0})}} - f^{\ast}})}}} \right\}}$ and $L:={\ell{({2G})}}$. If $\eta \leq {1/L}$, the iterates generated by satisfy $\left\| {{\nabla f}{(x_{t})}} \right\| \leq G$ for all $t \geq 0$ and It is clear that Theorem 5.2 gives the classical $\mathcal{O}{({1/\epsilon^{2}})}$ gradient complexity to achieve an $\epsilon$-stationary point, which is optimal as it matches the lower bound.

### Stochastic gradient descent

In this part, we present the convergence result for stochastic gradient descent defined as follows. where $g_{t}$ is an estimate of the gradient ${\nabla f}{(x_{t})}$. We consider the following standard assumption on the gradient noise $\epsilon_{t}:={g_{t} - {{\nabla f}{(x_{t})}}}$.

### Assumption 4

${{\mathbb{E}}_{t - 1}{\lbrack\epsilon_{t}\rbrack}} = 0$ and ${{\mathbb{E}}_{t - 1}\left\lbrack \left\| \epsilon_{t} \right\|^{2} \right\rbrack} \leq \sigma^{2}$ for some $\sigma \geq 0$, where ${\mathbb{E}}_{t - 1}$ denotes the expectation conditioned on ${\{ g_{s}\}}_{s < t}$.

Under Assumption 4, we can obtain the following theorem.

### Theorem 5.3

Suppose $f$ is $\ell$-smooth where $\ell$ is sub-quadratic. For any $0 < \delta < 1$, we denote $F:={{8{({{{f{(x_{0})}} - f^{\ast}} + \sigma})}}/\delta}$ and $G:={\sup{\{{u \geq 0}\mid{u^{2} \leq {{2\ell{({2u})}} \cdot F}}\}}} < \infty$. Denote $L:={\ell{({2G})}}$ and choose $\eta \leq {\min\left\{ \frac{1}{2L},\frac{1}{4G\sqrt{T}} \right\}}$ and $T \geq \frac{F}{\eta\epsilon^{2}}$ for any $\epsilon > 0$. Then with probability at least $1 - \delta$, the iterates generated by satisfy $\left\| {{\nabla f}{(x_{t})}} \right\| \leq G$ for all $t < T$ and As we choose $\eta = {\mathcal{O}{({1/\sqrt{T}})}}$, Theorem 5.3 gives the classical $\mathcal{O}{({1/\epsilon^{4}})}$ gradient complexity, where we ignore non-leading terms. This rate is optimal as it matches the lower bound. The key to its proof is again to bound the gradients along the trajectory. However, bounding gradients in the stochastic setting is much more challenging than in the deterministic setting, especially with the heavy-tailed noise in Assumption 4. We briefly discuss some of the challenges as well as our approach below and defer the detailed proof of Theorem 5.3 to Appendix F.

First, due to the existence of heavy-tailed gradient noise as considered in Assumption 4, neither the gradient nor the function values is non-increasing. The induction analyses we have used in the deterministic setting hardly work. In addition, to apply Lemma 3.3, we need to control the update at each step and make sure $\left\| {x_{t + 1} - x_{t}} \right\| = {\eta\left\| g_{t} \right\|} \leq {G/L}$. However, $g_{t}$ might be unbounded due to the potentially unbounded gradient noise.

To overcome these challenges, we define the following random variable $\tau$. where we use $a \land b$ to denote $\min{\{ a,b\}}$ for any ${a,b} \in {\mathbb{R}}$. Then at least before time $\tau$, we know that the function value and gradient noise are bounded, where the former also implies bounded gradients according to Corollary 3.6. Therefore, it suffices to show the probability of $\tau < T$ is small, which means with a high probability, $\tau = T$ and thus gradients are always bounded before $T$.

Since both the gradient and noise are bounded for $t < \tau$, it is straightforward to bound the update $\left\| {x_{t + 1} - x_{t}} \right\|$, which allows us to use Lemma 3.3 and other useful properties. However, it is still non-trivial to upper bound ${\mathbb{E}}{\lbrack{{f{(x_{\tau})}} - f^{\ast}}\rbrack}$ as $\tau$ is a random variable instead of a fixed time step. Fortunately, $\tau$ is a stopping time with nice properties. That is because both $f{(x_{t + 1})}$ and $\epsilon_{t} = {g_{t} - {{\nabla f}{(x_{t})}}}$ only depend on ${\{ g_{s}\}}_{s \leq t}$, i.e., the stochastic gradients up to $t$. Therefore, for any fixed $t$, the events $\{{\tau > t}\}$ only depend on ${\{ g_{s}\}}_{s \leq t}$, which show $\tau$ is a stopping time. Then with a careful analysis, we are still able to obtain an upper bound on ${{\mathbb{E}}{\lbrack{{f{(x_{\tau})}} - f^{\ast}}\rbrack}} = {\mathcal{O}{}}$.

On the other hand, $\tau < T$ means either $\tau = \tau_{1} < T$ or $\tau = \tau_{2} < T$. If $\tau = \tau_{1} < T$, by its definition, we know ${{f{(x_{\tau + 1})}} - f^{\ast}} > F$. Roughly speaking, it also suggests ${{f{(x_{\tau})}} - f^{\ast}} > {F/2}$. If we choose $F$ such that it is much larger than the upper bound on ${\mathbb{E}}{\lbrack{{f{(x_{\tau})}} - f^{\ast}}\rbrack}$ we just obtained, by Markov's inequality, we can show the probability of $\tau = \tau_{1} < T$ is small. In addition, by union bound and Chebyshev's inequality, the probability of $\tau_{2} < T$ can also be bounded by a small constant. Therefore, we have shown $\tau < T$. Then the rest of the analysis is not too hard following the classical analysis.

### Reconciliation with existing lower bounds

In this section, we reconcile our convergence results for constant-stepsize GD/SGD in the non-convex setting with existing lower bounds in and, based on which the authors claim that adaptive methods such as GD/SGD with clipping and Adam are provably faster than non-adaptive GD/SGD. This may seem to contradict our convergence results. In fact, we show that any gain in adaptive methods is at most by constant factors, as GD and SGD already achieve the optimal rates in the non-convex setting. provides both upper and lower complexity bounds for constant-stepsize GD for $(L_{0},L_{1})$-smooth functions, and shows that its complexity is $\mathcal{O}{({M\epsilon^{- 2}})}$, where is the supremum gradient norm below the level set of the initial function value. If $M$ is very large, then the $\mathcal{O}{({M\epsilon^{- 2}})}$ complexity can be viewed as a negative result, and as evidence that constant-stepsize GD can be slower than GD with gradient clipping, since in the latter case, they obtain the $\mathcal{O}{(\epsilon^{- 2})}$ complexity without $M$. However, based on our Corollary 3.6, their $M$ can be actually bounded by our $G$, which is a constant. Therefore, the gain in adaptive methods is at most by constant factors. further provides a lower bound which shows non-adaptive GD may diverge for some examples. However, their counter-example does not allow the stepsize to depend on the initial sub-optimality gap. In contrast, our stepsize $\eta$ depends on the effective smoothness constant $L$, which depends on the initial sub-optimality gap through $G$. Therefore, there is no contradiction here either. We should point out that in the practice of training neural networks, the stepsize is usually tuned after fixing the loss function and initialization, so it does depend on the problem instance and initialization.

### Lower bound

For $(\rho,L_{0},L_{\rho})$-smooth functions with $\rho < 2$, it is easy to verify that the constant $G$ in both Theorem 5.2 and Theorem 5.3 is a polynomial function of problem-dependent parameters like $L_{0},L_{\rho},{{f{(x_{0})}} - f^{\ast}},\sigma$, etc. In other words, GD and SGD are provably efficient methods in the non-convex setting for $\rho < 2$. In this section, we show that the requirement of $\rho < 2$ is necessary in the non-convex setting with the lower bound for GD in the following Theorem 5.4, whose proof is deferred in Appendix G. Since SGD reduces to GD when there is no gradient noise, it is also a lower bound for SGD.

### Theorem 5.4

Given ${L_{0},L_{2},G_{0},\Delta_{0}} > 0$ satisfying ${L_{2}\Delta_{0}} \geq 10$, for any $\eta \geq 0$, there exists a $(2,L_{0},L_{2})$-smooth function $f$ that satisfies Assumptions 1 and 2, and initial point $x_{0}$ that satisfies ${\|{{\nabla f}{(x_{0})}}\|} \leq G_{0}$ and ${{f{(x_{0})}} - f^{\ast}} \leq \Delta_{0}$, such that gradient descent with stepsize $\eta$ either cannot reach a $1$-stationary point or takes at least ${\exp{({{L_{2}\Delta_{0}}/8})}}/6$ steps to reach a $1$-stationary point.

## Conclusion

In this paper, we generalize the standard Lipschitz smoothness as well as the $(L_{0},L_{1})$-smoothness conditions to the $\ell$-smoothness condition, and develop a new approach for analyzing the convergence under this condition. The approach uses different techniques for several methods and settings to bound the gradient along the optimization trajectory, which allows us to obtain stronger results for both convex and non-convex problems. We obtain the classical rates for GD/SGD/NAG methods in the convex and/or non-convex setting. Our results challenge the folklore belief on the necessity of adaptive methods for generalized smooth functions.

There are several interesting future directions following this work. First, the $\ell$-smoothness can perhaps be further generalized by allowing $\ell$ to also depend on potential functions in each setting, besides the gradient norm. In addition, it would also be interesting to see if the techniques of bounding gradients along the trajectory that we have developed in this and the concurrent work can be further generalized to other methods and problems and to see whether more efficient algorithms can be obtained. Finally, although we justified the necessity of the requirement of $\ell$-smoothness with a *sub-quadratic* $\ell$ in the non-convex setting, it is not clear whether it is also necessary for NAG in the convex setting, another interesting open problem.
