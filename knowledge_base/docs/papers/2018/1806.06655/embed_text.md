## Introduction

This paper considers the analysis of continuous-time gradient-based optimization through the lens of nonlinear contraction theory. It is motivated, in part, by recent observations in machine learning that arise in the application of gradient descent (or its stochastic counterpart) for the training of over-parameterized networks. Modern networks often possess many more parameters than training examples and can fit the labels perfectly, resulting in submanifold valleys of the parameter space with equal cost. Moreover, recent results suggest that highly-redundant networks experience few to no local optima that are not global optima. These observations may be surprising in light of the fact that the loss landscapes for these problems are rarely convex.

Although convex problems admit provable globally optimal solutions, other broader classes of functions share this same property. For example, Invex functions guarantee that any local optimum is a global optimum, although the utility of invexity conditions remains a point of contention. Functions satisfying the Polyak-Lojasiewicz (PL) inequality give rise to exponentially convergent gradient descent to a provably optimal solution. While the PL condition is, in general, difficult to verify without an a-priori known globally optimal solution, the existence of zero-loss solutions in over-parameterized learning makes it tractable in important special cases. Geodesic convexity generalizes convexity to a Riemannian setting, with applicability to optimization on manifolds, as well as to conventional Euclidean settings where ${\mathbb{R}}^{n}$ is endowed with a manifold structure through the definition of a metric. Here, we consider another class of conditions for the convergence of gradient and natural gradient descent to a globally optimal point. We do so through adopting the perspective of nonlinear contraction theory and analyzing gradient descent in continuous time.

Contraction theory allows the stability of nonlinear non-autonomous systems to be characterized through linear time-varying dynamics describing the propagation of infinitesimally small displacements along the systems' flow. The existence of a Riemannian metric that contracts these virtual displacements (i.e., elements in the tangent space) is necessary and sufficient for exponential convergence of any pair of trajectories. Contraction naturally yields methods for constructing stable systems of systems, including synchronization phenomena and consensus as well as other key building blocks that allow the construction of large contracting systems out of simpler elements. These properties provide opportunities to construct larger optimization structures from simpler elements (e.g., in distributed or competitive optimization settings).

The contribution of this paper is to apply these contraction tools for the analysis of gradient and natural gradient optimization. We consider optimization problems posed over ${\mathbb{R}}^{n}$ wherein no explicit manifold structure necessarily exists a-priori. Instead, we consider the analysis of optimization following endowing these problems with additional structure (a Riemannian metric), analyzing their convergence, and considering the use of contraction tools to build larger optimization structures out of smaller ones. Analysis proceeds in continuous time. While this approach is limited, in part, by the fact that computational optimization algorithms require a discrete implementation, a continuous perspective has yielded insight on important phenomena such as in the analysis, discrete implementations, and extensions of Nesterov's accelerated gradient descent method. It has also enabled analysis of primal-dual algorithms, where an absolute time reference is obtained by introducing additional fast dynamics or delays using a singular perturbation framework. Recent results provide principled tools to derive discrete-time implementations that preserve specific continuous-time convergence rates.

The paper is organized as follows. Section 2 provides our main results, detailing the applicability of contraction theory to analyze gradient descent in continuous time. We show that convex functions represent the special case of contraction in the identity metric. The flexibility afforded by state-dependent contraction metrics, however, enables significant extra freedom for guaranteeing that all local optima are globally optimal. We then consider the extensions of these results to natural gradient descent, where geodesic convexity of a function corresponds to contraction of its natural gradient system in the natural metric. In both cases, results highlight the topology of the set of optimizers in the case of semi-contraction, which would have most direct applicability to over-parameterized networks. New results also show how semi-contraction may be combined with specific additional information to reach broad conclusions about a dynamical system. Section 3 details extensions of these results to the case of primal-dual type dynamics that appear in mixed convex/concave saddle systems, and shows how a broad class of natural adaptive control laws can be interpreted as a primal-dual system. Section 4 discusses the special case of g-convex functions and associated combination properties for interfacing with other models. Section 5 provides an outlook on potential future advances that may stem from these connections.

## Contraction Analysis of Gradient Systems

We first recall basic definitions and facts on convex optimization and show how a contraction analysis of gradient-based optimization considerably generalizes the class of functions that admit a unique global optimum. Following this presentation, results are generalized to the case of geodesically-convex optimization, which is particularly suited to analysis via contraction tools. Throughout this analysis, given a differentiable function $\mathbf{h}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m}}$, we denote the Jacobian of $\mathbf{h}{(\mathbf{x})}$ by

In the special case of a scalar-valued function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ we denote the gradient of $f{(\mathbf{x})}$ by

and its Hessian by ${\nabla^{2}f}{(\mathbf{x})}$. Unless otherwise stated, we assume all functions are sufficiently smooth such that derivatives of the necessary order exist and are continuous.

Before we embark on this discussion, let us note that of course, as illustrated, e.g., in and in the following example, continuous-time analysis tools in general may be used to conceptually illuminate the mechanisms involved in discrete-time algorithms. As this paper will show, contraction tools give particularly simple insights into important classes of optimization problems, such as, e.g., geodesically-convex optimization.

### Example 1

The Polyak-Lojasiewicz (PL) inequality is one of the most general sufficient conditions for discrete-time gradient descent to exhibit linear convergence rates without strong convexity of the cost. A function is said to satisfy the PL inequality if it has a (typically unknown) global minimum value $f^{\ast}$ and there exists a constant $\mu > 0$ such that

Consider gradient descent on the cost function $f{(\mathbf{x})}$ from a continuous-time point of view,

Using $V = {{f{(\mathbf{x})}} - f^{\ast}}$ as a Lyapunov-like function, and then requiring that $V$ converges exponentially with rate $\mu$, yields

The inequality above is exactly the PL condition. Thus, we see that the PL condition is nothing but the condition for exponential convergence of the residual cost $V = {{f{(\mathbf{x})}} - f^{\ast}}$.

Similarly, imposing $\overset{˙}{V} \leq {- {\mu\sqrt{V}}}$, corresponding to finite-time convergence (in time less than ${2\sqrt{V{}}}/\mu$ ), would require a modified PL-like condition

while imposing $\overset{˙}{V} \leq {- {\muV^{2}}}$ would require

By comparison, the results pursued via contraction analysis in this paper will ensure exponential convergence of any pair of trajectories for gradient descent, but likewise will ensure convergence of those solutions to a global optimum.

### Relationships Between Convexity and Contraction

### Definition 1 (Strong Convexity)

A twice differentiable function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is $\alpha$-strongly convex with $\alpha > 0$ if its Hessian matrix ${\nabla^{2}f}{(\mathbf{x})}$ satisfies the matrix inequality

As its name suggests, a function that is strongly convex is convex in the usual sense, while the converse is not always true. From a dynamic systems perspective, strong convexity provides exponential convergence of gradient flows:

### Proposition 1 (Exponential Convergence of Gradient Systems for Strongly Convex Functions)

If a twice differentiable function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is $\alpha$-strongly convex, then its gradient system

converges to the unique global minimum of $f$ exponentially with rate $\alpha$.

Toward proving this proposition, we will consider stability analysis through the application of nonlinear contraction theory.

### Definition 2 (Contraction Metric \[15\])

A system $\overset{˙}{\mathbf{x}} = {\mathbf{h}{(\mathbf{x},t)}}$ is said to be contracting at rate $\alpha > 0$ with respect to a symmetric positive definite metric $\mathbf{M}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n \times n}}$, if for all $t \in {\mathbb{R}}$ and all $\mathbf{x} \in {\mathbb{R}}^{n}$,

where ${\mathbf{A}{(\mathbf{x},t)}} = \frac{\partial\mathbf{h}}{\partial\mathbf{x}}$ is the system Jacobian and $\overset{˙}{\mathbf{M}} = {\sum_{i}{\left( {\partial{\mathbf{M}/{\partial x_{i}}}} \right)h_{i}{(\mathbf{x},t)}}}$. The system is said to be semi-contracting with respect to $\mathbf{M}$ when (2. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) holds with $\alpha = 0$.

Given an $\alpha$-contracting system and an arbitrary pair of initial conditions $\mathbf{x}_{1}{}$ and $\mathbf{x}_{2}{}$, the solutions $\mathbf{x}_{1}{(t)}$ and $\mathbf{x}_{2}{(t)}$ converge to one another exponentially

where $d_{\mathcal{M}}{( \cdot, \cdot )}$ denotes the geodesic distance on the Riemannian manifold $\mathcal{M} = {({\mathbb{R}}^{n},\mathbf{M})}$. This property can be shown by considering the evolution of differential displacements $\delta\mathbf{x}$, which describe the evolution of nearby trajectories and coincide with the notion of virtual displacements in Lagrangian mechanics. More precisely, letting $\mathbf{x}{(t;\mathbf{x}_{0},t_{0})}$ denote the solution of $\overset{˙}{\mathbf{x}} = {\mathbf{h}{(\mathbf{x},t)}}$ from initial condition ${\mathbf{x}{(t_{0})}} = \mathbf{x}_{0}$, differential displacements evolve according to

Property follows from the evolution of the squared length of these differential displacements, which verifies

Furthermore, if a system is $\alpha$-contracting in a metric $\mathbf{M}$ that satisfies ${\mathbf{M}{(\mathbf{x})}} \succeq {\beta\mathbf{I}}$ uniformly for some constant $\beta > 0$, then any two solutions verify

### Example 2

Consider an $\alpha$-strongly convex function $f$ and its associated gradient descent system (1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")). Since $f$ is strongly convex, it has a unique global minimum $\mathbf{x}^{\ast}$, which is a equilibrium point of (1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")). It can be verified that the gradient descent dynamics of $f$ are contracting in the identity metric $\mathbf{M} = \mathbf{I}$ with rate $\alpha$. Since geodesic distances are just Euclidean distances in this metric, immediately implies that

thus proving Proposition 1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems").

From this example, it is clear that strongly convex functions are a special case of ones whose gradient systems are contracting. The following proposition shows that one does not lose the convergence properties to a global optimum on this more general class of functions.

### Proposition 2 (Exponential Convergence of Contracting Gradient Systems)

Consider again gradient descent as in equation (1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")). The system converges exponentially to a unique global minimum if it is contracting in *some* metric.

### Proof

Because (1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) is autonomous and contracting, it converges exponentially to a unique equilibrium $\mathbf{x}^{\star}$. Furthermore, this equilibrium must be a global minimum since $f$ can only decrease along trajectories, with $\overset{˙}{f} = {- {{\nabla f}{(\mathbf{x})}^{\top}{\nabla f}{(\mathbf{x})}}} < 0$ for ${\mathbf{x} \neq \mathbf{x}^{\star}}.$ ∎

The above result, which emphasizes contraction rather than convexity as a sufficient condition to converge to a global minimum, can be extended to the semi-contracting case as follows.

### Proposition 3 (Asymptotic Convergence of Semi-Contracting Gradient Systems)

Consider a twice differentiable function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, a symmetric positive definite metric $\mathbf{M}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n \times n}}$, and the associated gradient system

Assume that dynamics (5. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) is semi-contracting in *some* metric, and furthermore that one trajectory of the system is known to be bounded. Then, (a) $f$ has at least one stationary point, (b) any local minimum of $f$ is a global minimum, (c) all global minima of $f$ are path-connected, and (d) all trajectories asymptotically converge to a global minimum of $f$.

### Proof

\(a\) By assumption, there exists some initial condition $\mathbf{x}_{0}$ such that $\mathbf{x}{(t;\mathbf{x}_{0})}$ remains bounded. This, in turn, implies that the $\omega$-limit set $\omega{\lbrack{\mathbf{x}{(t;\mathbf{x}_{0})}}\rbrack}$ is non-empty, compact, forward invariant, and that

Let $\mathbf{x}^{\ast}$ denote an element of $\omega{\lbrack{\mathbf{x}{(t;\mathbf{x}_{0})}}\rbrack}$. Since (5. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) is a gradient system, Theorem 15.0.3 of guarantees that $\mathbf{x}^{\ast}$ must be an equilibrium point of (5. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")). This proves that $f$ has at least one stationary point.

Let us now show that $\omega{\lbrack{\mathbf{x}{(t;\mathbf{x}_{0})}}\rbrack}$ consists only of the single point $\mathbf{x}^{\ast}$, by contradiction. Let $\mathbf{x}_{1}^{\ast}$ and $\mathbf{x}_{2}^{\ast}$ be distinct elements in $\omega{\lbrack{\mathbf{x}{(t;\mathbf{x}_{0})}}\rbrack}$. Further let $\epsilon = {d_{\mathbf{M}}{(\mathbf{x}_{1}^{\ast},\mathbf{x}_{2}^{\ast})}}$ the geodesic distance between $\mathbf{x}_{1}^{\ast}$ and $\mathbf{x}_{2}^{\ast}$. Then, the geodesic balls $\mathcal{B}_{1}:={\mathcal{B}_{\mathbf{M}}{(\mathbf{x}_{1}^{\ast},\frac{\epsilon}{3})}}$ and $\mathcal{B}_{\mathbf{M}}{(\mathbf{x}_{2}^{\ast},\frac{\epsilon}{3})}$ are disjoint. Further, since the system is semi-contracting these geodesic balls are forward invariant. Yet, since $\mathbf{x}_{1}^{\ast}$ a limit point, $\mathbf{x}{(t;\mathbf{x}_{0})}$ arrives within $\mathcal{B}_{1}$ at some point, and never leaves. Likewise, since $\mathbf{x}_{2}^{\ast}$ is a limit point, $\mathbf{x}{(t;\mathbf{x}_{0})}$ arrives within $\mathcal{B}_{2}$ at some point, and never leaves. Thus, we have a contradiction, and the limit set must consist of a single point.

\(b\) and (c): Consider now two equilibrium points of (5. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")), $\mathbf{x}_{1}^{\ast}$ and $\mathbf{x}_{2}^{\ast}$, and a smooth path ${\mathbf{γ}}{(s)}$ such that ${{\mathbf{γ}}{}} = \mathbf{x}_{1}^{\ast}$ and ${{\mathbf{γ}}{}} = \mathbf{x}_{2}^{\ast}$. Since the gradient dynamics are semi-contracting, for each $s$ the solution $\mathbf{x}{(t;{{\mathbf{γ}}{(s)}})}$ remains bounded. Thus, by the same reasoning as above, each $\mathbf{x}{(t;{{\mathbf{γ}}{(s)}})}$ converges to some equilibrium $\mathbf{x}^{\ast}{(s)}$ as $t\rightarrow{+ \infty}$. Since ${{\nabla f}{({\mathbf{x}^{\ast}{(s)}})}} = 0$ for each $s$, and $\mathbf{x}^{\ast}{(s)}$ smoothly connects $\mathbf{x}_{1}^{\ast}$ and $\mathbf{x}_{2}^{\ast}$, it follows that ${f{(\mathbf{x}_{1}^{\ast})}} = {f{(\mathbf{x}_{2}^{\ast})}}$. That is, all solutions converge to the same value for $f$.

(d): That all solutions of (1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) asymptotically converge to a global minimum of $f$ follows from that fact that $f$ decreases along all solutions, and all solutions converge to the same value for $f$. ∎

### Remark 1

In the case that a contraction metric needs to be found numerically, note that the conditions (2. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) for certifying contraction or semi-contraction are convex criteria. Thus, in many instances, the process of finding a metric numerically to verify contraction may be accomplished via convex optimization approaches, such as those based on sums-of-squares programming.

### Relationship Between Geodesic Convexity and Contraction

Geodesic convexity generalizes conventional notions of convexity to the case where the domain of a function is equipped with a Riemannian metric. A special case occurs in geometric programming (GP). In GP, a non-convex problem over positive variables ${\{ x_{i}\}}_{i = 1}^{N}$ can be transformed into a convex problem by a change of variables $y_{i} = {\log{(x_{i})}}$. Alternately GP can be formulated over the positive reals viewed as a Riemannian manifold by measuring differential length elements $ds$ in a relative sense

Geodesically-convex optimization generalizes this transformation strategy to a broader class of problems. However, beyond special cases (see, e.g., ), generative procedures remain lacking to formulate g-convex optimization problems or recognize g-convexity.

To introduce g-convexity more formally, consider a function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ and a positive definite metric $\mathbf{M}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n \times n}}$. We note that geodesic convexity of $f$ is not an intrinsic property of the function itself, but rather is a property of $f$ defined on the Riemannian manifold $({\mathbb{R}}^{n},\mathbf{M})$.

### Definition 3 (g-Strong Convexity \[32\])

A twice differentiable function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is said to be geodesically $\alpha$-strongly convex (with $\alpha > 0$) in a symmetric positive definite metric $\mathbf{M}$ if its Riemannian Hessian matrix $\mathbf{H}{(\mathbf{x})}$ satisfies:

The elements of the Riemannian Hessian are given as

where ${\partial_{ij}f} = \frac{\partial^{2}f}{\partial{x_{i}{\partial x_{j}}}}$ provide the elements of the conventional (Euclidean) Hessian and $\Gamma_{ij}^{k}$ denotes the Christoffel symbols of the second kind

with ${M^{ij}{(\mathbf{x})}} = {({\mathbf{M}{(\mathbf{x})}^{- 1}})}_{ij}$. The function $f$ is g-convex when (7. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) holds with $\alpha = 0$.

The Riemannian Hessian generalizes the notion of the Hessian from a Euclidean context and captures the curvature of $f$ along geodesics. Likewise, the natural gradient generalizes the notion of a Euclidean gradient to the Riemannian context in the following sense.

### Definition 4 (Natural Gradient \[33\])

Consider ${\mathbb{R}}^{n}$ equipped with a Riemannian metric $\mathbf{M}$. The natural gradient of a differentiable function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is the direction of steepest ascent on the manifold and is given in coordinates by $\mathbf{M}{(\mathbf{x})}^{- 1}{\nabla f}{(\mathbf{x})}$.

### Remark 2

When $\mathbf{M}{(\mathbf{x})}$ is the Hessian of some twice differentiable strictly convex scalar function $\psi{(\mathbf{x})}$, natural gradient descent coincides with the continuous-time limit of mirror descent \[34, Sec. 2.3\] with potential $\psi{(\mathbf{x})}$.

### Remark 3

From a differential geometric viewpoint, the first covariant derivative of $f$ is a covector field given in coordinates by ${\nabla f}{(\mathbf{x})}$, while the natural gradient is a vector field given in coordinates by $\mathbf{M}{(\mathbf{x})}^{- 1}{\nabla f}{(\mathbf{x})}$. In a Euclidean context, where $\mathbf{M}{(\mathbf{x})}$ is identity, this distinction between covariant (covector) and contravariant (vector) representations of the gradient is immaterial.

Similarly, the Riemannian Hessian $\mathbf{H}$ represents in coordinates the second covariant derivative of $f$.

When $\mathbf{M}$ is the identity metric, geodesic $\alpha$-strong convexity naturally coincides with the definition of $\alpha$-strong convexity in Definition 1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems"). The natural gradient can be used to directly mirror Proposition 1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems") within the Riemannian context.

### Theorem 1 (Equivalence between g-Strong Convexity and Contraction of Natural Gradient)

Consider a twice differentiable function $f:{{{\mathbb{R}}^{n} \times {\mathbb{R}}}\rightarrow{\mathbb{R}}}$, a symmetric positive definite metric $\mathbf{M}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n \times n}}$, and the natural gradient system

Then, $f$ is $\alpha$-strongly g-convex in the metric $\mathbf{M}$ for each $t$ if and only if (9. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) is contracting with rate $\alpha$ in the metric $\mathbf{M}$. More specifically, the Riemannian Hessian verifies

where $\mathbf{A} = \frac{\partial\mathbf{h}}{\partial\mathbf{x}}$.
