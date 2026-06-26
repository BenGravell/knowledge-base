## Introduction

This paper considers the analysis of continuous-time gradient-based optimization through the lens of nonlinear contraction theory. It is motivated, in part, by recent observations in machine learning that arise in the application of gradient descent (or its stochastic counterpart) for the training of over-parameterized networks. Modern networks often possess many more parameters than training examples and can fit the labels perfectly, resulting in submanifold valleys of the parameter space with equal cost. Moreover, recent results suggest that highly-redundant networks experience few to no local optima that are not global optima. These observations may be surprising in light of the fact that the loss landscapes for these problems are rarely convex.

Although convex problems admit provable globally optimal solutions, other broader classes of functions share this same property. For example, Invex functions guarantee that any local optimum is a global optimum, although the utility of invexity conditions remains a point of contention. Functions satisfying the Polyak-Lojasiewicz (PL) inequality give rise to exponentially convergent gradient descent to a provably optimal solution. While the PL condition is, in general, difficult to verify without an a-priori known globally optimal solution, the existence of zero-loss solutions in over-parameterized learning makes it tractable in important special cases. Geodesic convexity generalizes convexity to a Riemannian setting, with applicability to optimization on manifolds, as well as to conventional Euclidean settings where ${\mathbb{R}}^{n}$ is endowed with a manifold structure through the definition of a metric. Here, we consider another class of conditions for the convergence of gradient and natural gradient descent to a globally optimal point. We do so through adopting the perspective of nonlinear contraction theory and analyzing gradient descent in continuous time.

Contraction theory allows the stability of nonlinear non-autonomous systems to be characterized through linear time-varying dynamics describing the propagation of infinitesimally small displacements along the systems' flow. The existence of a Riemannian metric that contracts these virtual displacements (i.e., elements in the tangent space) is necessary and sufficient for exponential convergence of any pair of trajectories. Contraction naturally yields methods for constructing stable systems of systems, including synchronization phenomena and consensus as well as other key building blocks that allow the construction of large contracting systems out of simpler elements. These properties provide opportunities to construct larger optimization structures from simpler elements (e.g., in distributed or competitive optimization settings).

The contribution of this paper is to apply these contraction tools for the analysis of gradient and natural gradient optimization. We consider optimization problems posed over ${\mathbb{R}}^{n}$ wherein no explicit manifold structure necessarily exists a-priori. Instead, we consider the analysis of optimization following endowing these problems with additional structure (a Riemannian metric), analyzing their convergence, and considering the use of contraction tools to build larger optimization structures out of smaller ones. Analysis proceeds in continuous time. While this approach is limited, in part, by the fact that computational optimization algorithms require a discrete implementation, a continuous perspective has yielded insight on important phenomena such as in the analysis, discrete implementations, and extensions of Nesterov's accelerated gradient descent method. It has also enabled analysis of primal-dual algorithms, where an absolute time reference is obtained by introducing additional fast dynamics or delays using a singular perturbation framework. Recent results provide principled tools to derive discrete-time implementations that preserve specific continuous-time convergence rates.

The paper is organized as follows. Section 2 provides our main results, detailing the applicability of contraction theory to analyze gradient descent in continuous time. We show that convex functions represent the special case of contraction in the identity metric. The flexibility afforded by state-dependent contraction metrics, however, enables significant extra freedom for guaranteeing that all local optima are globally optimal. We then consider the extensions of these results to natural gradient descent, where geodesic convexity of a function corresponds to contraction of its natural gradient system in the natural metric. In both cases, results highlight the topology of the set of optimizers in the case of semi-contraction, which would have most direct applicability to over-parameterized networks. New results also show how semi-contraction may be combined with specific additional information to reach broad conclusions about a dynamical system. Section 3 details extensions of these results to the case of primal-dual type dynamics that appear in mixed convex/concave saddle systems, and shows how a broad class of natural adaptive control laws can be interpreted as a primal-dual system. Section 4 discusses the special case of g-convex functions and associated combination properties for interfacing with other models. Section 5 provides an outlook on potential future advances that may stem from these connections.

## Contraction Analysis of Gradient Systems

We first recall basic definitions and facts on convex optimization and show how a contraction analysis of gradient-based optimization considerably generalizes the class of functions that admit a unique global optimum. Following this presentation, results are generalized to the case of geodesically-convex optimization, which is particularly suited to analysis via contraction tools. Throughout this analysis, given a differentiable function $\mathbf{h}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m}}$, we denote the Jacobian of $\mathbf{h}{(\mathbf{x})}$ by In the special case of a scalar-valued function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ we denote the gradient of $f{(\mathbf{x})}$ by and its Hessian by ${\nabla^{2}f}{(\mathbf{x})}$. Unless otherwise stated, we assume all functions are sufficiently smooth such that derivatives of the necessary order exist and are continuous.

Before we embark on this discussion, let us note that of course, as illustrated, e.g., in and in the following example, continuous-time analysis tools in general may be used to conceptually illuminate the mechanisms involved in discrete-time algorithms. As this paper will show, contraction tools give particularly simple insights into important classes of optimization problems, such as, e.g., geodesically-convex optimization.

### Example 1

The Polyak-Lojasiewicz (PL) inequality is one of the most general sufficient conditions for discrete-time gradient descent to exhibit linear convergence rates without strong convexity of the cost. A function is said to satisfy the PL inequality if it has a (typically unknown) global minimum value $f^{\ast}$ and there exists a constant $\mu > 0$ such that Consider gradient descent on the cost function $f{(\mathbf{x})}$ from a continuous-time point of view, Using $V = {{f{(\mathbf{x})}} - f^{\ast}}$ as a Lyapunov-like function, and then requiring that $V$ converges exponentially with rate $\mu$, yields The inequality above is exactly the PL condition. Thus, we see that the PL condition is nothing but the condition for exponential convergence of the residual cost $V = {{f{(\mathbf{x})}} - f^{\ast}}$.

Similarly, imposing $\overset{˙}{V} \leq {- {\mu\sqrt{V}}}$, corresponding to finite-time convergence (in time less than ${2\sqrt{V{}}}/\mu$), would require a modified PL-like condition while imposing $\overset{˙}{V} \leq {- {\muV^{2}}}$ would require By comparison, the results pursued via contraction analysis in this paper will ensure exponential convergence of any pair of trajectories for gradient descent, but likewise will ensure convergence of those solutions to a global optimum.

### Relationships Between Convexity and Contraction

### Definition 1 (Strong Convexity)

A twice differentiable function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is $\alpha$-strongly convex with $\alpha > 0$ if its Hessian matrix ${\nabla^{2}f}{(\mathbf{x})}$ satisfies the matrix inequality As its name suggests, a function that is strongly convex is convex in the usual sense, while the converse is not always true. From a dynamic systems perspective, strong convexity provides exponential convergence of gradient flows:

### Proposition 1 (Exponential Convergence of Gradient Systems for Strongly Convex Functions)

If a twice differentiable function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is $\alpha$-strongly convex, then its gradient system converges to the unique global minimum of $f$ exponentially with rate $\alpha$.

Toward proving this proposition, we will consider stability analysis through the application of nonlinear contraction theory.

### Definition 2 (Contraction Metric )

A system $\overset{˙}{\mathbf{x}} = {\mathbf{h}{(\mathbf{x},t)}}$ is said to be contracting at rate $\alpha > 0$ with respect to a symmetric positive definite metric $\mathbf{M}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n \times n}}$, if for all $t \in {\mathbb{R}}$ and all $\mathbf{x} \in {\mathbb{R}}^{n}$, where ${\mathbf{A}{(\mathbf{x},t)}} = \frac{\partial\mathbf{h}}{\partial\mathbf{x}}$ is the system Jacobian and $\overset{˙}{\mathbf{M}} = {\sum_{i}{\left({\partial{\mathbf{M}/{\partial x_{i}}}} \right)h_{i}{(\mathbf{x},t)}}}$. The system is said to be semi-contracting with respect to $\mathbf{M}$ when (2. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) holds with $\alpha = 0$.

Given an $\alpha$-contracting system and an arbitrary pair of initial conditions $\mathbf{x}_{1}{}$ and $\mathbf{x}_{2}{}$, the solutions $\mathbf{x}_{1}{(t)}$ and $\mathbf{x}_{2}{(t)}$ converge to one another exponentially where $d_{\mathcal{M}}{(\cdot, \cdot)}$ denotes the geodesic distance on the Riemannian manifold $\mathcal{M} = {({\mathbb{R}}^{n},\mathbf{M})}$. This property can be shown by considering the evolution of differential displacements $\delta\mathbf{x}$, which describe the evolution of nearby trajectories and coincide with the notion of virtual displacements in Lagrangian mechanics. More precisely, letting $\mathbf{x}{(t;\mathbf{x}_{0},t_{0})}$ denote the solution of $\overset{˙}{\mathbf{x}} = {\mathbf{h}{(\mathbf{x},t)}}$ from initial condition ${\mathbf{x}{(t_{0})}} = \mathbf{x}_{0}$, differential displacements evolve according to Property follows from the evolution of the squared length of these differential displacements, which verifies Furthermore, if a system is $\alpha$-contracting in a metric $\mathbf{M}$ that satisfies ${\mathbf{M}{(\mathbf{x})}} \succeq {\beta\mathbf{I}}$ uniformly for some constant $\beta > 0$, then any two solutions verify

### Example 2

Consider an $\alpha$-strongly convex function $f$ and its associated gradient descent system (1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")). Since $f$ is strongly convex, it has a unique global minimum $\mathbf{x}^{\ast}$, which is a equilibrium point of (1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")). It can be verified that the gradient descent dynamics of $f$ are contracting in the identity metric $\mathbf{M} = \mathbf{I}$ with rate $\alpha$. Since geodesic distances are just Euclidean distances in this metric, immediately implies that thus proving Proposition 1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems").

From this example, it is clear that strongly convex functions are a special case of ones whose gradient systems are contracting. The following proposition shows that one does not lose the convergence properties to a global optimum on this more general class of functions.

### Proposition 2 (Exponential Convergence of Contracting Gradient Systems)

Consider again gradient descent as in equation (1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")). The system converges exponentially to a unique global minimum if it is contracting in *some* metric.

### Proof

Because (1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) is autonomous and contracting, it converges exponentially to a unique equilibrium $\mathbf{x}^{\star}$. Furthermore, this equilibrium must be a global minimum since $f$ can only decrease along trajectories, with $\overset{˙}{f} = {- {{\nabla f}{(\mathbf{x})}^{\top}{\nabla f}{(\mathbf{x})}}} < 0$ for ${\mathbf{x} \neq \mathbf{x}^{\star}}.$ ∎ The above result, which emphasizes contraction rather than convexity as a sufficient condition to converge to a global minimum, can be extended to the semi-contracting case as follows.

### Proposition 3 (Asymptotic Convergence of Semi-Contracting Gradient Systems)

Consider a twice differentiable function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, a symmetric positive definite metric $\mathbf{M}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n \times n}}$, and the associated gradient system Assume that dynamics (5. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) is semi-contracting in *some* metric, and furthermore that one trajectory of the system is known to be bounded. Then, (a) $f$ has at least one stationary point, (b) any local minimum of $f$ is a global minimum, (c) all global minima of $f$ are path-connected, and (d) all trajectories asymptotically converge to a global minimum of $f$.

### Proof

\(a\) By assumption, there exists some initial condition $\mathbf{x}_{0}$ such that $\mathbf{x}{(t;\mathbf{x}_{0})}$ remains bounded. This, in turn, implies that the $\omega$-limit set $\omega{\lbrack{\mathbf{x}{(t;\mathbf{x}_{0})}}\rbrack}$ is non-empty, compact, forward invariant, and that Let $\mathbf{x}^{\ast}$ denote an element of $\omega{\lbrack{\mathbf{x}{(t;\mathbf{x}_{0})}}\rbrack}$. Since (5. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) is a gradient system, Theorem 15.0.3 of guarantees that $\mathbf{x}^{\ast}$ must be an equilibrium point of (5. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")). This proves that $f$ has at least one stationary point.

Let us now show that $\omega{\lbrack{\mathbf{x}{(t;\mathbf{x}_{0})}}\rbrack}$ consists only of the single point $\mathbf{x}^{\ast}$, by contradiction. Let $\mathbf{x}_{1}^{\ast}$ and $\mathbf{x}_{2}^{\ast}$ be distinct elements in $\omega{\lbrack{\mathbf{x}{(t;\mathbf{x}_{0})}}\rbrack}$. Further let $\epsilon = {d_{\mathbf{M}}{(\mathbf{x}_{1}^{\ast},\mathbf{x}_{2}^{\ast})}}$ the geodesic distance between $\mathbf{x}_{1}^{\ast}$ and $\mathbf{x}_{2}^{\ast}$. Then, the geodesic balls $\mathcal{B}_{1}:={\mathcal{B}_{\mathbf{M}}{(\mathbf{x}_{1}^{\ast},\frac{\epsilon}{3})}}$ and $\mathcal{B}_{\mathbf{M}}{(\mathbf{x}_{2}^{\ast},\frac{\epsilon}{3})}$ are disjoint. Further, since the system is semi-contracting these geodesic balls are forward invariant. Yet, since $\mathbf{x}_{1}^{\ast}$ a limit point, $\mathbf{x}{(t;\mathbf{x}_{0})}$ arrives within $\mathcal{B}_{1}$ at some point, and never leaves. Likewise, since $\mathbf{x}_{2}^{\ast}$ is a limit point, $\mathbf{x}{(t;\mathbf{x}_{0})}$ arrives within $\mathcal{B}_{2}$ at some point, and never leaves. Thus, we have a contradiction, and the limit set must consist of a single point.

\(b\) and (c): Consider now two equilibrium points of (5. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")), $\mathbf{x}_{1}^{\ast}$ and $\mathbf{x}_{2}^{\ast}$, and a smooth path ${\mathbf{γ}}{(s)}$ such that ${{\mathbf{γ}}{}} = \mathbf{x}_{1}^{\ast}$ and ${{\mathbf{γ}}{}} = \mathbf{x}_{2}^{\ast}$. Since the gradient dynamics are semi-contracting, for each $s$ the solution $\mathbf{x}{(t;{{\mathbf{γ}}{(s)}})}$ remains bounded. Thus, by the same reasoning as above, each $\mathbf{x}{(t;{{\mathbf{γ}}{(s)}})}$ converges to some equilibrium $\mathbf{x}^{\ast}{(s)}$ as $t\rightarrow{+ \infty}$. Since ${{\nabla f}{({\mathbf{x}^{\ast}{(s)}})}} = 0$ for each $s$, and $\mathbf{x}^{\ast}{(s)}$ smoothly connects $\mathbf{x}_{1}^{\ast}$ and $\mathbf{x}_{2}^{\ast}$, it follows that ${f{(\mathbf{x}_{1}^{\ast})}} = {f{(\mathbf{x}_{2}^{\ast})}}$. That is, all solutions converge to the same value for $f$.

(d): That all solutions of (1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) asymptotically converge to a global minimum of $f$ follows from that fact that $f$ decreases along all solutions, and all solutions converge to the same value for $f$. ∎

### Remark 1

In the case that a contraction metric needs to be found numerically, note that the conditions (2. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) for certifying contraction or semi-contraction are convex criteria. Thus, in many instances, the process of finding a metric numerically to verify contraction may be accomplished via convex optimization approaches, such as those based on sums-of-squares programming.

### Relationship Between Geodesic Convexity and Contraction

Geodesic convexity generalizes conventional notions of convexity to the case where the domain of a function is equipped with a Riemannian metric. A special case occurs in geometric programming (GP). In GP, a non-convex problem over positive variables ${\{ x_{i}\}}_{i = 1}^{N}$ can be transformed into a convex problem by a change of variables $y_{i} = {\log{(x_{i})}}$. Alternately GP can be formulated over the positive reals viewed as a Riemannian manifold by measuring differential length elements $ds$ in a relative sense Geodesically-convex optimization generalizes this transformation strategy to a broader class of problems. However, beyond special cases (see, e.g.,), generative procedures remain lacking to formulate g-convex optimization problems or recognize g-convexity.

To introduce g-convexity more formally, consider a function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ and a positive definite metric $\mathbf{M}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n \times n}}$. We note that geodesic convexity of $f$ is not an intrinsic property of the function itself, but rather is a property of $f$ defined on the Riemannian manifold $({\mathbb{R}}^{n},\mathbf{M})$.

### Definition 3 (g-Strong Convexity )

A twice differentiable function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is said to be geodesically $\alpha$-strongly convex (with $\alpha > 0$) in a symmetric positive definite metric $\mathbf{M}$ if its Riemannian Hessian matrix $\mathbf{H}{(\mathbf{x})}$ satisfies: The elements of the Riemannian Hessian are given as where ${\partial_{ij}f} = \frac{\partial^{2}f}{\partial{x_{i}{\partial x_{j}}}}$ provide the elements of the conventional (Euclidean) Hessian and $\Gamma_{ij}^{k}$ denotes the Christoffel symbols of the second kind with ${M^{ij}{(\mathbf{x})}} = {({\mathbf{M}{(\mathbf{x})}^{- 1}})}_{ij}$. The function $f$ is g-convex when (7. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) holds with $\alpha = 0$.

The Riemannian Hessian generalizes the notion of the Hessian from a Euclidean context and captures the curvature of $f$ along geodesics. Likewise, the natural gradient generalizes the notion of a Euclidean gradient to the Riemannian context in the following sense.

### Definition 4 (Natural Gradient )

Consider ${\mathbb{R}}^{n}$ equipped with a Riemannian metric $\mathbf{M}$. The natural gradient of a differentiable function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is the direction of steepest ascent on the manifold and is given in coordinates by $\mathbf{M}{(\mathbf{x})}^{- 1}{\nabla f}{(\mathbf{x})}$.

### Remark 2

When $\mathbf{M}{(\mathbf{x})}$ is the Hessian of some twice differentiable strictly convex scalar function $\psi{(\mathbf{x})}$, natural gradient descent coincides with the continuous-time limit of mirror descent \[34, Sec. 2.3\] with potential $\psi{(\mathbf{x})}$.

### Remark 3

From a differential geometric viewpoint, the first covariant derivative of $f$ is a covector field given in coordinates by ${\nabla f}{(\mathbf{x})}$, while the natural gradient is a vector field given in coordinates by $\mathbf{M}{(\mathbf{x})}^{- 1}{\nabla f}{(\mathbf{x})}$. In a Euclidean context, where $\mathbf{M}{(\mathbf{x})}$ is identity, this distinction between covariant (covector) and contravariant (vector) representations of the gradient is immaterial.

Similarly, the Riemannian Hessian $\mathbf{H}$ represents in coordinates the second covariant derivative of $f$.

When $\mathbf{M}$ is the identity metric, geodesic $\alpha$-strong convexity naturally coincides with the definition of $\alpha$-strong convexity in Definition 1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems"). The natural gradient can be used to directly mirror Proposition 1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems") within the Riemannian context.

### Theorem 1 (Equivalence between g-Strong Convexity and Contraction of Natural Gradient)

Consider a twice differentiable function $f:{{{\mathbb{R}}^{n} \times {\mathbb{R}}}\rightarrow{\mathbb{R}}}$, a symmetric positive definite metric $\mathbf{M}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n \times n}}$, and the natural gradient system Then, $f$ is $\alpha$-strongly g-convex in the metric $\mathbf{M}$ for each $t$ if and only if (9. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) is contracting with rate $\alpha$ in the metric $\mathbf{M}$. More specifically, the Riemannian Hessian verifies where $\mathbf{A} = \frac{\partial\mathbf{h}}{\partial\mathbf{x}}$.

Appendix 1 provides a self-contained proof using conventional tensor analysis methods, whose relationship with contraction conditions have been noted previously. The same relationships drive coordinate-free versions of the result .

### Remark 4

Theorem 1. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems") can also be viewed as a special case of contraction analysis for complex Hamilton-Jacobi dynamics. A reorganization of (9. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) as may be recognized as the generalized momentum being the negative covariant gradient within a Hamiltonian mechanics context.

### Remark 5

While Theorem 1. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems") applies to $\alpha$-strong convexity, the link between the Riemannian Hessian and the contraction condition (2. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) also provides immediate equivalence between g-convexity of a function and semi-contraction of its natural gradient dynamics.

### Remark 6

Equation (10. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) provides an alternate way to compute the geodesic Hessian $\mathbf{H}$, and, as expected, leaves it invariant when the metric $\mathbf{M}$ is scaled by a strictly positive constant. Because of the structure of the natural gradient dynamics, scaling $\mathbf{M}$ is akin to scaling time and implies inversely scaling the contraction rate $\alpha$, consistently with (7. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")).\By contrast, note that given a *fixed* dynamics $\mathbf{h}$, the contraction metric analyzing it can always be arbitrarily scaled while leaving the contraction rate unchanged.

Similar to in Section 2.1 where convexity corresponded to contraction of gradient in the identity metric, we likewise see that Thm. 1. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems") imposes g-convexity via a particular choice of contraction metric for the natural gradient dynamics. Mirroring Prop. 2. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems"), removing this restriction on the contraction metric leads to significant additional flexibility for guaranteeing convergence to a globally optimal point.

### Proposition 4 (Exponential Convergence of Contracting Natural Gradient Systems)

Consider again natural gradient descent as in equation (9. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")). The system converges exponentially to a unique global minimum if it is contracting in *some* metric.

### Proof

The proof follows immediately from the same logic as the proof of Proposition 2. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems"). ∎

### Remark 7

Note that contraction also provides robustness. Consider perturbed dynamics $\overset{˙}{\mathbf{x}} = {{\mathbf{h}{(\mathbf{x},t)}} + {\mathbf{d}{(t)}}}$ with $\sqrt{\mathbf{d}{(t)}^{\top}\mathbf{M}{(\mathbf{x})}\mathbf{d}{(t)}} < R$ uniformly. If the dynamics are contracting with rate $\lambda$, then all trajectories contract to a geodesic ball of radius $R/\lambda$. This observation implies favorable properties for algorithms where an exact gradient may be difficult or intractable to compute, with approximation methods used in their place.

### Theorem 2 (Semi-Contraction for Natural Gradient)

Consider a twice differentiable function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, a symmetric positive definite metric $\mathbf{M}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n \times n}}$, and the associated natural gradient system Assume that dynamics (11. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) is semi-contracting in *some* metric, and furthermore that one trajectory of the system is known to be bounded. Then, (a) $f$ has at least one stationary point, (b) any local minimum of $f$ is a global minimum, (c) all global minima of $f$ are path-connected, and (d) all trajectories asymptotically converge to a global minimum of $f$.

### Proof

The proof follows the exact same line of logic as the proof to Prop. 3. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems"). The result of Theorem 15.0.3 of, which guarantees that any $\omega$-limit point of gradient descent (5. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) is an equilibrium point, generalizes immediately to the case of natural gradient descent (11. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")). ∎

### Remark 8

The topology of global optimizers satisfying this semi-contraction condition is the same as those observed when training over-parameterized networks. However, empirical loss functions in these networks often also experience multiple saddle points. The attractor sets associated with strict saddles have measure zero under discrete gradient descent with sufficiently small stepsize (i.e., with adequately close approximation to the continuous time case), while the dimensionality of the attractor sets can be further reduced via smoothed versions of the gradient.

While the presence of strict saddles precludes the ability of a gradient system to be globally semi-contracting, any of the results given here can be generalized to forward invariant contraction or semi-contraction regions. In principle, saddles could then be treated by excluding their measure zero attractor sets from suitably chosen contraction or semi-contraction regions.

The topology of equilibria in semi-contracting gradient systems immediately implies the following result.

### Corollary 1

Consider an autonomous, semi-contracting natural gradient system. If the linearization at some equilibrium point is strictly stable, then all system trajectories tend to this global minimizer.

More generally, if some equilibrium is locally asymptotically stable, all trajectories tend to this global minimizer.

### Proof

We prove the second part, the first then follows directly from Lyapunov's linearization method. Existence of an equilibrium implies existence of a bounded trajectory. Furthermore, by definition, there exists a ball around the equilibrium point $\mathbf{x}^{\star}$ such that all trajectories initiated in that ball tend to $\mathbf{x}^{\star}$. If there was another equilibrium, the path connecting it to $\mathbf{x}^{\star}$ would intersect that ball, which is a contradiction since the path is itself composed of equilibria via Thm. 2. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems"). ∎

### Remark 9

Strict stability of a natural gradient system at an equilibrium point can of course be established simply by ensuring that all eigenvalues of its Jacobian at this point are strictly in the left-half complex plane. This condition is equivalent to requiring that the Hessian of the objective function is positive definite at $\mathbf{x}^{\star}$.

Indeed, given the natural gradient dynamics (11. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) with ${\mathbf{h}{(\mathbf{x})}} = {- {\mathbf{M}{(\mathbf{x})}^{- 1}{\nabla f}{(\mathbf{x})}}}$, the Jacobian at any equilibrium $\mathbf{x}^{\star}$ is Applying a similarity transformation with the symmetric square root of $\mathbf{M}{(\mathbf{x}^{\star})}$ yields All eigenvalues of the symmetric matrix above are real, and they are all strictly negative if and only if the Hessian ${\nabla^{2}f}{(\mathbf{x}^{\star})}$ is positive definite.

Note that this condition is equivalent to the geodesic Hessian at $\mathbf{x}^{\star}$ being positive definite in any metric, as the Euclidean Hessian is numerically equal to the geodesic Hessian in any metric in this case, due to all terms multiplying the Christoffel symbols in (8. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) being zero.

### Corollary 2

Consider an autonomous semi-contracting natural gradient system, and assume that the system has more than one equilibrium. Then, at any equilibrium, both the Jacobian matrix of the dynamics and the Hessian of the objective have at least one zero eigenvalue.

### Proof

Consider an equilibrium $\mathbf{x}^{\star}$, and an equilibrium path connecting it to some other equilibrium. The unit tangent vector at $\mathbf{x}^{\star}$ along this path is an eigenvector of the Jacobian with eigenvalue zero. Given the algebraic relation between the Jacobian and the objective Hessian pointed out in Remark 9, this shows in turn that the objective Hessian has a zero eigenvalue. ∎

### Examples

Let us illustrate Theorem 1. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems") using the classical nonconvex Rosenbrock function: This function has a unique global optimum at $\mathbf{x}^{\ast} = {\lbrack 1,1\rbrack}^{\top}$, which is located along a long, shallow, parabolic-shaped valley.

### Example 3

Consider the Rosenbrock function and the metric The metric $\mathbf{M}{(\mathbf{x})}$ satisfies ${{tr}{({\mathbf{M}{(\mathbf{x})}})}} = {{400x_{1}^{2}} + 101} > 0$ and ${\det{({\mathbf{M}{(\mathbf{x})}})}} = 100 > 0$, and thus ${\mathbf{M}{(\mathbf{x})}} \succ 0$. Note that $\mathbf{M}{(\mathbf{x})}$ is not the Hessian of $f{(\mathbf{x})}$. The natural gradient dynamics follows It can be verified algebraically that which shows that natural gradient descent is contracting with rate $\alpha = 2$. This implies that the natural gradient dynamics satisfy where $\mathbf{x}^{\ast} = {\lbrack 1,1\rbrack}^{\top}$. Equivalently, the Rosenbrock function is geodesically $\alpha$-strongly convex with $\alpha = 2$.

The Rosenbrock metric $\mathbf{M}{(\mathbf{x})}$ can be viewed as following from a differential change of variables where $\mathbf{M} = {\mathbf{\Theta}^{\top}\mathbf{\Theta}}$ yields ${\delta\mathbf{x}^{\top}\mathbf{M}\delta\mathbf{x}} = {\delta\mathbf{z}^{\top}\delta\mathbf{z}}$. This differential change of variables is integrable, so that g-convexity of the Rosenbrock can be shown using the explicit nonlinear coordinate change $z_{1} = {{10x_{1}^{2}} - {10x_{2}}}$ and $z_{2} = {x_{1} - 1}$ that provides $f = {z_{1}^{2} + z_{2}^{2}}$.

### Example 4

Mirror descent provides another example of a metric corresponding to an explicit state transformation, with Newton's method as a special case.

Consider a twice differentiable scalar objective function $f{(\mathbf{x})}$, and a smooth strictly convex scalar function $\psi{(\mathbf{x})}$. Denoting by ${\mathbf{H}_{f}{(\mathbf{x})}} = {{\nabla^{2}f}{(\mathbf{x})}}$ and $\mathbf{H}_{\psi} = {\nabla^{2}\psi}$ the Hessians of these functions, continuous-time mirror descent of $f{(\mathbf{x})}$ under potential $\psi{(\mathbf{x})}$ corresponds to natural gradient in the Hessian metric $\mathbf{H}_{\psi}$ \[34, Sec. 2.3\] Consider the explicit change of variables $\mathbf{z} = {{\nabla\psi}{(\mathbf{x})}}$, which can be written in differential form as ${\delta\mathbf{z}} = {\mathbf{H}_{\psi}\delta\mathbf{x}}$. The dynamics can be viewed in the mirror space as Letting ${\mathbf{M}{(\mathbf{x})}} = \mathbf{H}_{\psi}^{2}$, this yields Thus, continuous mirror descent is contracting with rate $\lambda > 0$ in the metric ${\mathbf{M}{(\mathbf{x})}} = \mathbf{H}_{\psi}^{2}$ if In the particular case when $f$ is $\alpha$-strongly convex and the potential function is chosen as ${\psi{(\mathbf{x})}} = {f{(\mathbf{x})}}$, equation simply corresponds to Newton's method, and verifies that Newton's method is contracting with rate 1 in the squared Hessian metric ${\mathbf{M}{(\mathbf{x})}} = {\mathbf{H}_{f}^{2}{(\mathbf{x})}}$.

Note that the well-known result that the transformation $\mathbf{z} = {{\nabla\phi}{(\mathbf{x})}}$ is one-to-one (given the strict convexity of $\psi$) can also be shown by constructing, for a given $\mathbf{z}$, the system which is autonomous and contracting in the identity metric and thus must reach a unique equilibrium point.

The following proposition provides further insight into the case when the contraction metric is related to an explicit change of variables more generally.

### Proposition 5 (Relationship between gradient and natural gradient under a diffeomorphic change of variables)

Consider a diffeomorphic change of variables $\mathbf{z} = {\mathbf{g}{(\mathbf{x})}}$, and the associated metric ${\mathbf{M}{(\mathbf{x})}} = {\mathbf{\Theta}{(\mathbf{x})}^{\top}\mathbf{\Theta}{(\mathbf{x})}}$, with ${\mathbf{\Theta}{(\mathbf{x})}} = \frac{\partial\mathbf{g}}{\partial\mathbf{x}}$. For any twice differentiable function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$, natural gradient descent in $\mathbf{x}$ is equivalent to gradient descent in $\mathbf{z}$

### Proof

In the $\mathbf{z}$ coordinates we have

### Proposition 6

Consider a metric $\mathbf{M}{(\mathbf{x})}$ and suppose there exists a diffeomorphic change of variables $\mathbf{z} = {\mathbf{g}{(\mathbf{x})}}$ such that ${\mathbf{M}{(\mathbf{x})}} = {\mathbf{\Theta}{(\mathbf{x})}^{\top}\mathbf{\Theta}{(\mathbf{x})}}$, with ${\mathbf{\Theta}{(\mathbf{x})}} = \frac{\partial\mathbf{g}}{\partial\mathbf{x}}$. Then, the associated Riemannian curvature tensor with components $R_{ik\ellm}$ must be identically zero.

### Proof

Note that since ${\delta\mathbf{z}} = {\mathbf{\Theta}{(\mathbf{x})}\delta\mathbf{x}}$, it follows that ${\delta\mathbf{z}^{\top}\delta\mathbf{z}} = {\delta\mathbf{x}^{\top}\mathbf{M}{(\mathbf{x})}\delta\mathbf{x}}$ and thus the Riemannian metric tensor expressed in the $\mathbf{z}$ coordinates is the identity. Since the components of the Riemannian metric tensor are constant in these transformed coordinates, it follows that the components of the Riemannian curvature tensor are identically zero. Transformation laws for tensors ensure that the components of the curvature tensor remain zero under arbitrary coordinate change, thus $R_{ik\ellm} = 0$. ∎ The general freedom to consider differential changes of coordinates ${\delta\mathbf{z}} = {\mathbf{\Theta}{(\mathbf{x})}\delta\mathbf{x}}$ where $\mathbf{\Theta}$ is non-integrable provides additional flexibility and generality to both contraction analysis and g-convexity, as illustrated by the following examples.

### Example 5

Consider the non-convex function which has a global minimum at $\mathbf{x} = \mathbf{0}$. Contours of the function are shown in Fig. 1. Gradient descent can be shown to be contracting at rate $\lambda = 2$ in the metric Fig. 1 shows two solutions and plots their geodesic distance. The decay is, as expected, at a rate faster than the exponentially decreasing upper bound as derived. The curvature tensor for this metric has some non-zero components, such as From Proposition 6, this shows that this metric cannot be derived from an explicit change of coordinates.

Fig 1: Contracting gradient descent corresponding to Example 5.

### Example 6

Consider the function and natural gradient descent with a given natural metric $\mathbf{\Theta}{(\mathbf{z})}^{\top}\mathbf{\Theta}{(\mathbf{z})}$, where This natural gradient dynamics is verified semi-contracting in the metric Similar to Example 5, this metric has non-zero Riemannian curvature, and thus cannot be derived from a change of coordinates. Figure 2 shows the contours of $f$ and two solutions of natural gradient descent. Figure 3 shows that the the geodesic distance between these two solutions is non-increasing. Since the system is only semi-contracting, the distance between solutions does not tend toward zero. It can be verified that $f$ is a sum of squares and thus ${f{(\mathbf{z})}} \geq 0$, and that ${f{(\mathbf{z})}} = 0$ when $z_{2} = {z_{1}^{3} - z_{1}}$. Both initial conditions asymptotically lead to this path connected set of global optima.

Fig 2: Semi-Contracting Natural Gradient Descent for Example 6.

Fig 3: Semi-Contracting Natural Gradient Descent for Example 6.

### Example 7

Geodesically-convex optimization can also be used to carry out manifold-constrained optimization in an unconstrained fashion via recasting problems over a Riemannian manifold directly. Taking an intrinsic view of the manifold, coordinate free results are available, however, for the purposes of computation, we assume a global coordinate chart here. Consider for instance optimization over the set ${\mathbb{S}}_{+}^{n}$ of $n \times n$ positive definite matrices, and specifically the problem of finding the Karcher mean of $m$ matrices $\mathbf{A}_{i} \in {\mathbb{S}}_{+}^{n}$, which minimizes the objective function where ${\|\mathbf{A}\|}_{F} = \sqrt{{tr}{({\mathbf{A}^{\top}\mathbf{A}})}}$ denotes the Frobenius norm of a matrix $\mathbf{A}$. The function $f{(\mathbf{X})}$ is $m$-strongly convex on ${\mathbb{S}}_{+}^{n}$in the metric that measures symmetric differential displacements as Naturally, the requirement that $\delta\mathbf{X}$ be symmetric makes it an element of the tangent space to the manifold of symmetric positive definite matrices.

This metric generalizes the GP case, and coincides with the second-order terms in the Taylor series of the log barrier $- {{logdet}{(\mathbf{X})}}$. The gradient of $f{(\mathbf{X})}$ can be written and accordingly the natural gradient can be shown to satisfy From Theorem 1. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems"), any trajectory with arbitrary initial condition ${\mathbf{X}{}} \in {\mathbb{S}}_{+}^{n}$ will remain within ${\mathbb{S}}_{+}^{n}$ under the natural gradient descent dynamics since (intuitively) the Riemannian metric makes any element on the boundary of the positive definite cone an infinite distance away from any one in the interior, and contraction of the natural gradient dynamics ensures that geodesic distances decrease exponentially.

### Example 8

An approximation to the Riemannian distance of two positive definite (PD) matrices on the PD cone is given by the Bregman LogDet divergence on ${\mathbb{S}}_{+}^{n}$ The metric is convex in its first argument, and can be shown to be geodesically convex in the second. We illustrate the connection with contraction to show this property. Note that so that the natural gradient descent dynamics are simply with differential dynamics where the differential displacement $\delta\mathbf{X}$ must be symmetric. Considering the rate of change in length of these differential displacements and defining the differential change of variables ${\delta\mathbf{Z}} = {\mathbf{X}^{- \frac{1}{2}}\delta\mathbf{X}\mathbf{X}^{- \frac{1}{2}}}$, one has ${{tr}{({\delta\mathbf{Z}^{2}})}} = {{tr}\left({({\mathbf{X}^{- 1}\delta\mathbf{X}})}^{2} \right)}$ and for all ${\delta\mathbf{Z}} \neq \mathbf{0}$. Hence, considering only the second argument to LogDet divergence, its Riemannian Hessian is positive definite, thus proving g-convexity via Thm. 1. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems").

### Non-autonomous Systems and Virtual Systems

In our optimization context, the fact that contraction analysis is directly applicable to non-autonomous systems can be exploited in a variety of ways. As we shall detail later, a key aspect is that it allows feedback combinations or hierarchies of contracting modules to be exploited to address more elaborate optimization problems or architectures. Also, it makes the construction of *virtual* systems possible to potentially extend results beyond natural-gradient descent.

### Remark 10

The natural gradient $\mathbf{M}^{- 1}{(\mathbf{x})}{\nabla_{\mathbf{x}}f}{(\mathbf{x},t)}$ represents the direction of steepest ascent on the manifold at any given time. With this in mind, Remark 7 on robustness enables convergence analysis for natural gradient descent within time-varying optimization contexts. Let $\mathbf{x}^{\ast}{(t)}$ denote the optimum of a time-varying $\alpha$-strongly g-convex function. If $\sqrt{{\overset{˙}{\mathbf{x}}}^{\ast}{(t)}^{\top}\mathbf{M}{(\mathbf{x})}{\overset{˙}{\mathbf{x}}}^{\ast}{(t)}} < R$, then the natural gradient will track ${\overset{˙}{\mathbf{x}}}^{\ast}{(t)}$ with accuracy $R/\alpha$ after exponential transient.

### Remark 11

Consider a contracting natural gradient system of the form (9. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")). In the autonomous case, equations governing the differential displacement follow which has a similar structure to the time evolution of $\mathbf{h}{(\mathbf{x})}$ Thus, for natural gradient descent of an $\alpha$-strong g-convex function $f{(\mathbf{x})}$, the same algebra leading to also gives so that the Krasovskii-like function can be viewed as an exponentially converging Lyapunov function, with global minimum $V = 0$ at the unique minimum of $f{(\mathbf{x})}$. Of course, remains valid for *non-autonomous* systems as well, while does not.

The use of virtual contracting systems allows guaranteed exponential convergence to a unique minimum to be extended to classes of dynamics which are not pure natural gradient. For instance, it is common in optimization to adjust the learning rate as the descent progresses. Consider a natural gradient descent with the function $f{(\mathbf{x})}$ $\alpha$-strongly g-convex in metric $\mathbf{M}{(\mathbf{x})}$, and define the new system where the smooth scalar function $p{(\mathbf{x},t)}$ modulates the learning rate and is uniformly positive definite, Let us show that this system tends exponentially to the minimum $\mathbf{x}^{\ast}$ of $f{(\mathbf{x})}$.

Consider the auxiliary, *virtual* system, For this system, $p{({\mathbf{x}{(t)}},t)}$ is an external, uniformly positive definite function of time, and thus so that the contraction of (9. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) with rate $\alpha$ implies the contraction of with rate $\alphap_{min}$. Since both $\mathbf{x}{(t)}$ and $\mathbf{x}^{\ast}$ are particular solutions of, this implies in turn that $\mathbf{x}{(t)}$ tends to $\mathbf{x}^{\ast}$ with rate $\alphap_{min}$.

Note that since we only assumed that $p{(\mathbf{x},t)}$ is uniformly positive definite, in general the actual system is not contracting with respect to the metric $\mathbf{M}{(\mathbf{x})}$.

### Remark 12

The learning rate may also be selected to improve the numerical properties of the algorithm in a discrete time implementation. For example, $p{(\mathbf{x},t)}$ could vary as the inverse of the condition number of ${\nabla^{2}f}{(\mathbf{x})}$ to improve numeric conditioning without impact on stability guarantees.

### Contraction $+$

Corollary 1 above points to a more general class of results where contraction or semi-contraction properties are combined with other information, such as a stable local linearization or a decreasing cost, to provide global results.

### Contraction is attractive

As we now show, Corollary 1 extends more generally to autonomous semi-contracting systems. An instance of this result in the case of an identity metric was derived .

### Proposition 7

Consider an autonomous system semi-contracting in a bounded metric $\mathbf{M}{(\mathbf{x})}$, If a system equilibrium is locally asymptotically stable, then it is globally asymptotically stable. In particular, if the system linearization at some equilibrium point is strictly stable, then all system trajectories tend to this equilibrium.

### Proof

The result is a particular case of Theorem 3, to be discussed next. ∎

### Theorem 3

Consider a non-autonomous system, semi-contracting in a bounded metric $\mathbf{M}{(\mathbf{x})}$, Assume that a *specific* trajectory $\mathbf{x}^{\star}{(t)}$ is locally attractive. Then all trajectories tend asymptotically to $\mathbf{x}^{\star}{(t)}$.

In particular, if contraction holds (possibly in a different bounded metric) along a specific trajectory $\mathbf{x}^{\star}{(t)}$, and within a tube of constant size around it, then all trajectories tend asymptotically to $\mathbf{x}^{\star}{(t)}$.

### Proof

The first part generalizes the equilibrium argument from to arbitrary trajectories and arbitrary metrics. Assume that $\mathbf{x}^{\ast}{(t)}$ is locally attractive, by which we mean there exists some $\epsilon > 0$ such that, for any initial time $t_{0}$ and initial condition $\mathbf{x}_{0} \in {\mathcal{B}_{\mathbf{I}}{({\mathbf{x}^{\ast}{(t_{0})}},\epsilon)}}$, one has ${\mathbf{x}{({t_{0} + T};\mathbf{x}_{0},t_{0})}}\rightarrow{\mathbf{x}^{\ast}{({t_{0} + T})}}$ as $T\rightarrow{+ \infty}$. Without loss of generality, we assume $t_{0} = 0$.

Consider some generic initial condition $\mathbf{x}_{0}$ with ${d_{\mathbf{I}}{(\mathbf{x}_{0},{\mathbf{x}^{\ast}{}})}} > \epsilon$. We will argue that there is always a finite time window over which the geodesic distance from $\mathbf{x}{(t;\mathbf{x}_{0})}$ to $\mathbf{x}^{\ast}{(t)}$ decreases by a fixed finite increment.

Consider a geodesic connecting $\mathbf{x}_{0}$ and $\mathbf{x}^{\ast}{}$ and denote by $\underset{¯}{\mathbf{x}}$ the unique point on this geodesic that is a geodesic distance $\beta_{0}\epsilon$ away from $\mathbf{x}^{\ast}{}$. Due to the uniform positive definiteness of $\mathbf{M}$, this condition implies that $\underset{¯}{\mathbf{x}} \in {\mathcal{B}_{\mathbf{I}}{({\mathbf{x}^{\ast}{}},\epsilon)}}$.

Because of the local attractivity of $\mathbf{x}^{\ast}{(t)}$, there exists a time $t_{1} > 0$ such that which further implies that In addition, since the system is semi-contracting, we have and so by the triangle inequality This implies that so long as ${d_{\mathbf{I}}{(\mathbf{x}_{0},{\mathbf{x}^{\ast}{}})}} > \epsilon$, the trajectory from $\mathbf{x}_{0}$ will eventually decrease its geodesic distance by a fixed finite increment. Since this process can be repeated, it follows that there must exist some time $T$ such that ${\mathbf{x}{(T;\mathbf{x}_{0})}} \in {\mathcal{B}_{\mathbf{I}}{({\mathbf{x}^{\ast}{(T)}},\epsilon)}}$.

To complete the second part of the proof we proceed to show that if contraction (2. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) holds within a tube of constant size around trajectory $\mathbf{x}^{\ast}{(t)}$, for some bounded metric ${{(\beta_{0}^{\star})}^{2}\mathbf{I}} \preceq {\mathbf{M}^{\star}{(\mathbf{x})}} \preceq {{(\beta_{1}^{\star})}^{2}\mathbf{I}}$ and some rate $\alpha^{\star} > 0$, then that trajectory is locally attractive. By condition (2. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) holding within a tube we mean that there exists some $\epsilon > 0$ such that (2. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) holds for any time $t$ and any $\mathbf{x} \in {\mathcal{B}_{\mathbf{I}}{({\mathbf{x}^{\ast}{(t)}},\epsilon)}}$. From boundedness of the metric, we have so that any initial condition $\mathbf{x}_{0}$ satisfying necessarily starts within this tube. Further, since (2. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) holds within the tube, it follows that the geodesic ball of radius $\epsilon\beta_{0}^{\star}$ around $\mathbf{x}^{\star}{(t)}$ is forward invariant. Since this ball is contained within a contraction region, this implies that for any $\mathbf{x}_{0} \in {\mathcal{B}_{\mathbf{M}}{({\mathbf{x}^{\star}{}},{\beta_{0}^{\star}\epsilon})}}$ which proves local asymptotic stability of $\mathbf{x}^{\star}{(t)}$. ∎

### Remark 13

The condition regarding contraction within a tube of fixed size is included to avoid pathological cases where the region of contraction shrinks to zero as $t\rightarrow{+ \infty}$. For example, the system $\overset{˙}{x} = {{- x} + {tx^{3}}}$ is contracting with rate $1$ at the origin for all time, yet the origin is not locally asymptotically stable.

### Remark 14

Intuitively, the result can be understood by analogy with a shrinking rope. Consider a path of initial conditions connecting $\mathbf{x}^{\star}{}$ to any $\mathbf{x}_{0}$. As this path flows forward in time, at $t = 0$, only a portion of this path of states is within the basin of attraction for $\mathbf{x}^{\star}{(t)}$. Viewing this path as a rope, the semi-contraction property ensures that no part of the rope can increase in length as it flows forward through the dynamics. Yet, due to local attractivity at one end of the rope, a portion of it is guaranteed to have shrinking length, pulling the rest of the rope toward the the region of attraction.

### Remark 15

Numerical tools for determining contraction metrics are based on the fact that contraction conditions (2. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) are convex in the metric for a fixed contraction rate. In practice, these methods often involve an outer search procedure for the contraction rate (e.g., via a binary search). In this sense, the use of semi-contraction is desirable as it does not require this additional search.

### Remark 16

These results have analogs in the context of controller design using control contraction metrics (CCMs). In this setting, one can impose a semi-contracting closed-loop metric everywhere, except in a tube along a desired trajectory where a strict contraction condition would be required, possibly in a different metric. Since the existence of an exponential (resp. semi) CCM implies that the closed-loop plant can be rendered contracting (resp. semi-contracting), Theorem 3 would then imply asymptotic stabilizability of the desired trajectory.

This extension likewise has analogs for manifold convergence results \[48, Section 5\] and convergence to a limit cycle by transverse contraction, both of which are special cases of CCM results applied to suitably constructed virtual control systems. In either case, a semi-contracting CCM everywhere can be combined with a contracting CCM condition on the manifold (or limit cycle) and within a neighborhood of it to assert asymptotic stability of the manifold (or limit cycle). In the limit cycle case for autonomous systems, the contracting CCM condition needs only be enforced on the limit cycle itself, as its satisfaction within some neighborhood is then guaranteed by compactness. Likewise, for convergence to a compact manifold (e.g., an eggshell) in an autonomous system, the contracting CCM condition needs only be considered on the manifold itself.

### Contraction as minimization

Similarly, Proposition 2. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems") may be viewed as a particular instance of the following results, which use contraction properties to minimize a cost or Lyapunov-like function.

### Proposition 8 (Exponential Cost Minimization)

Consider an autonomous contracting system, and a scalar cost function $V{(\mathbf{x})}$ such that ${\overset{˙}{V}{(\mathbf{x})}} \leq 0$ for all $\mathbf{x}$. Then all trajectories tend exponentially to a global minimum of $V$.

### Proof

Because the system is contracting and autonomous, it tends exponentially to a unique equilibrium $\mathbf{x}^{\star}$. Consider now an arbitrary $\mathbf{x}$, and the system trajectory initialized at $\mathbf{x}$. Since the cost $V$ can only decrease along the trajectory, this implies that ${V{(\mathbf{x}^{\star})}} \leq {V{(\mathbf{x})}}$, for all $\mathbf{x}$. ∎

### Proposition 9

Consider an autonomous semi-contracting system in a bounded metric $\mathbf{M}{(\mathbf{x})}$, and a scalar cost function $V{(\mathbf{x})}$ such that ${\overset{˙}{V}{(\mathbf{x})}} \leq 0$ for all $\mathbf{x}$. Assume that one system equilibrium $\mathbf{x}^{\star}$ is locally attractive (e.g., that linearization at $\mathbf{x}^{\star}$ is strictly stable). Then this equilibrium is unique, it is a global minimum of $V$, and all trajectories converge to it asymptotically.

### Proof

Applying Proposition 7 shows that all trajectories asymptotically tend to $\mathbf{x}^{\star}$, which also implies that the equilibrium is unique. By the same reasoning as in Proposition 8. ‣ 2.5.2 Contraction as minimization ‣ 2.5 Contraction + ‣ 2 Contraction Analysis of Gradient Systems"), since $V$ can only decrease, $V{(\mathbf{x}^{\star})}$ must be a global minimum. ∎

### Remark 17

These results extend readily to the case where a system is semi-contracting within some forward invariant region, as opposed to globally. These generalizations may have applicability e.g., to the continuous-time limit of trained neural networks, wherein semi-contraction regions represent basins of attraction that are free of saddles. Metrics may become singular as they approach the boundary of these open sets \[15, Section 3.9\], allowing the semi-contraction region to cover the entire basin.

Proposition 9 can be stated more generally as follows.

### Theorem 4 (Asymptotic Cost Minimization)

Consider an autonomous semi-contracting system in a bounded metric $\mathbf{M}{(\mathbf{x})}$, and a scalar cost function $V{(\mathbf{x})}$ such that ${\overset{˙}{V}{(\mathbf{x})}} \leq 0$ for all $\mathbf{x}$. Assume that one trajectory is known to be bounded. Let $\mathcal{I}$ be a forward invariant set where $\overset{˙}{V} = 0$, and assume that the contraction condition (2. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) holds on $\mathcal{I}$ for some (possibly different) metric.

Then $\mathcal{I}$ is path connected, all system trajectories converge to a unique equilibrium $\mathbf{x}^{\star} \in \mathcal{I}$, and $V$ is globally minimized at $\mathbf{x}^{\star}$.

### Proof

Let us first show that $\mathcal{I}$ is path connected, by contradiction. Assume $\mathcal{I}$ is not path connected, then it can be decomposed into two disjoints subsets, $\mathcal{I}_{1}$ and $\mathcal{I}_{2}$. Because $\mathcal{I}$ is invariant and the subsets are disjoint, each of the subsets must be invariant. Strict contraction on $\mathcal{I}_{1}$ and $\mathcal{I}_{2}$ then implies that each subset contains at least one locally stable equilibrium point (note that each of the subsets may themselves be disconnected and thus may contain more than one stable equilibrium point). The existence of two equilibrium points contradicts Proposition 9, and thus $\mathcal{I}$ is path connected.

Next, on the connected invariant set $\mathcal{I}$, contraction implies that the geodesic distance between any two points shrinks exponentially. By the same reasoning as in Proposition 8. ‣ 2.5.2 Contraction as minimization ‣ 2.5 Contraction + ‣ 2 Contraction Analysis of Gradient Systems"), this in turn implies convergence to a global minimum of $V$. ∎

### Remark 18

Note that for a system where a scalar cost $V$ satisfies $\overset{˙}{V} \leq 0$, radial unboundedness of $V$ is a sufficient condition for all trajectories to be bounded, ensuring the existence of a bounded trajectory as necessary in Thm. 4. ‣ 2.5.2 Contraction as minimization ‣ 2.5 Contraction + ‣ 2 Contraction Analysis of Gradient Systems").

### Remark 19

In the case of mechanical systems, $V$ may often be chosen as the total energy of the system, so that Proposition 8. ‣ 2.5.2 Contraction as minimization ‣ 2.5 Contraction + ‣ 2 Contraction Analysis of Gradient Systems") implies exponential convergence of the total energy, and, in turn, that potential energy is exponentially minimized. Similarly, Theorem 4. ‣ 2.5.2 Contraction as minimization ‣ 2.5 Contraction + ‣ 2 Contraction Analysis of Gradient Systems") implies that potential energy is asymptotically minimized.

### Remark 20

Contraction criteria can also be expressed in non-Euclidean norms and their associated matrix measures (, section 3.7.ii). The results above extend immediately to these representations.

## Primal-Dual Optimization

Primal-Dual algorithms are widely used in optimization to determine saddle points and also appear naturally in constrained optimization, where Lagrange parameters play the role of dual variables. When a function is strictly convex in a subset of its variables, and strictly concave in the remaining, gradient descent/ascent dynamics converge to a unique saddle equilibrium. Within the context of constrained optimization, these dynamics are known as the primal-dual dynamics. Such dynamics play an important role e.g., in machine learning, for instance in adversarial training, in the information theory of deep networks, in reinforcement learning and actor-critic methods, and in support vector machine representations. More generally, they are central to a large class of practical min-max problems, such as problems in physics involving free energy, or, e.g., nonlinear electrical networks modeled in terms of Brayton-Moser mixed potentials.

Consider a scalar function $\mathcal{L}{(\mathbf{x},{\mathbf{λ}},t)}$, possibly time-dependent, and metrics $\mathbf{M}_{\mathbf{x}}{(\mathbf{x})}$ and $\mathbf{M}_{\mathbf{λ}}{({\mathbf{λ}})}$. Consider the natural primal-dual dynamics, which we define as In contrast to Remark 8, wherein spurious saddle equilibrium points presented an obstacle to global contraction, here the target equilibrium points of these dynamics are, by construction, chosen to be the saddle points of the function $\mathcal{L}$. Using the metrics $\mathbf{M}_{\mathbf{x}}{(\mathbf{x})}$ and $\mathbf{M}_{\mathbf{λ}}{({\mathbf{λ}})}$ extends the standard case, where they would be replaced by constant, symmetric positive definite matrices. The practical relevance of this extension is illustrated by the following example in the case of natural adaptive control.

### Primal Dual Dynamics in Natural Adaptive Control

This section illustrates the presence of natural primal-dual dynamics embedded in the application of natural adaptive control laws. Consider a system given by with configuration $\mathbf{x} \in {\mathbb{R}}^{N}$, control $\mathbf{u} \in {\mathbb{R}}^{N}$, and unknown parameters $\mathbf{a} \in \mathcal{A} \subset {\mathbb{R}}^{p}$. The regressor $\mathbf{Y} \in {\mathbb{R}}^{N \times p}$ and symmetric matrix $\mathbf{J} \in {\mathbb{R}}^{N \times N}$ may depend nonlinearly on the state and its derivatives. We assume that the matrix $\mathbf{J}$ remains positive definite for all $\mathbf{a} \in \mathcal{A}$ and that it is linear in $\mathbf{a}$. As a result, there exists a regressor function $\mathbf{W}$ such that and a regressor function $\mathbf{Q}$ such that for any $\mathbf{s} \in {\mathbb{R}}^{N}$ Consider a desired trajectory $\mathbf{x}_{d}{(t)}$ and the associated sliding variable where $\overset{\sim}{\mathbf{x}} = {\mathbf{x} - \mathbf{x}_{d}}$. With this sliding variable, we define a reference $\mathbf{x}_{r}^{({n - 1})}$ for the order $n - 1$ derivative of the state.

Choosing the control law where $\mathbf{x}_{r}^{(n)} = {\frac{d}{dt}\mathbf{x}_{r}^{({n - 1})}}$ provides the closed-loop dynamics Inspired by the elegant modification of the Slotine and Li adaptive robot controller introduced by Lee et al., we consider the Lyapunov-like function where $d_{f}{(\mathbf{a}||\hat{\mathbf{a}})}$ denotes the Bregman divergence of a function $f$ assumed convex on $\mathcal{A}$ and given by Note that the LogDet divergence from follows this form for ${f{(\mathbf{X})}} = {- {{logdet}{(\mathbf{X})}}}$. Here, we consider the case when $\mathcal{A}$ is open and $f$ is chosen as a convex barrier function on $\mathcal{A}$, such that the Hessian metric $\mathbf{H} = {{\nabla^{2}f}{(\mathbf{x})}}$ endows $\mathcal{A}$ with a barrier Hessian manifold structure. Note that if $f$ is a second-order function $\frac{1}{2}\mathbf{a}^{T}{\mathbf{P}\mathbf{a}}$, the Bregman divergence is simply $\frac{1}{2}{\overset{\sim}{\mathbf{a}}}^{\top}\mathbf{P}\overset{\sim}{\mathbf{a}}$, with $\mathbf{H}^{- 1}$ equal to the constant matrix $\mathbf{P}^{- \mathbf{1}}$ similar to the standard adaptive algorithm.

A quick calculation shows that the derivative of the Bregman divergence is simply ${\overset{˙}{\hat{\mathbf{a}}}}^{\top}\mathbf{H}\overset{\sim}{\mathbf{a}}$, so that the adaptation law Considering a virtual system with $\mathbf{W}$ and $\mathbf{Q}$ as externally provided functions of time, the dynamics and are equivalent to natural primal-dual over the function in the decoupled metric $\mathbf{M}_{\mathbf{s}} = \mathbf{J}$ and $\mathbf{M}_{\hat{\mathbf{a}}} = {\mathbf{H}{(\hat{\mathbf{a}})}}$. Overall, this construction enables the results in natural adaptive robot control to be extended to the broader class.

### Remark 21

Note that a similar construction could be applied to provide natural adaptation within recent applications of nonlinear adaptive control \[67, Thm. 2\] based on control contraction metrics.

### Natural Primal Dual

Continuous-time convex primal-dual optimization is analyzed from a nonlinear contraction perspective , building on a earlier result of. As we now show, Theorem 1. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems") yields a natural extension to geodesic primal-dual optimization, where convexity in terms of primal and dual variables is replaced by g-convexity, thus broadening the above results to state-dependent metrics.

### Theorem 5

Consider a scalar function $\mathcal{L}{(\mathbf{x},{\mathbf{λ}},t)}$, with $\mathcal{L}$ g-strongly convex over $\mathbf{x}$ and g-strongly concave over $\mathbf{λ}$ in metrics $\mathbf{M}_{\mathbf{x}}{(\mathbf{x})}$ and $\mathbf{M}_{\mathbf{λ}}{({\mathbf{λ}})}$ respectively. Then, the geodesic primal-dual dynamics is globally contracting, in metric

### Proof

Letting $\mathbf{z} = {\lbrack\mathbf{x}^{\top},{\mathbf{λ}}{{}_{}^{\top}\rbrack}}^{\top}$ and $\overset{˙}{\mathbf{z}} = {\mathbf{f}{(\mathbf{z},t)}}$ denote the overall system dynamics, the system's Jacobian can be written so that, using Theorem 1. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems"),

### Proposition 10

Consider the primal dual dynamics for a scalar cost function $\mathcal{L}{(\mathbf{x},{\mathbf{λ}})}$, with $\mathcal{L}$ g-strongly convex over $\mathbf{x}$ and g-concave (not necessarily strongly so) over $\mathbf{λ}$ in metrics $\mathbf{M}_{\mathbf{x}}{(\mathbf{x})}$ and $\mathbf{M}_{\mathbf{λ}}{({\mathbf{λ}})}$ respectively. Suppose also that one solution of is known to be bounded. Then, for any initial condition, the geodesic primal-dual dynamics converge to an equilibrium $\mathbf{x}^{\ast}$, ${\mathbf{λ}}^{\ast}$. Moreover, $\mathbf{x}^{\ast}$ is independent of initial conditions.

### Proof

The proof is given as a corollary to Theorem 6 in the next section. ∎

### Remark 22

The above proposition highlights that contraction of the PD dynamics (e.g., as developed in ) is not necessary to guarantee convergence to a unique primal solution. Note however, that the above results only guarantee asymptotic convergence toward the unique primal equilibrium, as opposed to exponential convergence when contraction can be shown for the PD dynamics as a whole.

This proposition is reminiscent of results in adaptive control wherein the error dynamics of a certainty-equivalent controller may be asymptotically stable despite the fact that an associated adaptation law may not converge to the actual unknown parameters, with adaptation occurring on a "need-to-know" basis in that sense. Conceptually, this principle can apply to more general contexts involving concurrent control and learning, when effective control is the main goal (e.g., in reinforcement learning).

### Remark 23

Note that this analogy between adaptive control and primal-dual optimization also enables recent results in distributed adaptive control to be applied in a distributed primal-dual setting. These results also include straightforward strategies for stably handling communication delays (e.g., using a wave variable formulation ) which would find additional motivation in distributed primal-dual optimization applications.

## Applying Contraction Tools to G-Convex Optimization

Theorem 1. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems") immediately implies that existing combination properties from contraction analysis can be directly applied in the context of g-convex optimization. While these properties derive from simple matrix algebra and in principle could be proven directly from the definition of geodesic convexity, as we will see most rely for their practical relevance on the flexibility afforded by the contraction analysis point of view.

### Sum of g-convex

If two functions $f_{1}{(\mathbf{x},t)}$ and $f_{2}{(\mathbf{x},t)}$ are g-convex in the same metric for each $t$, then their sum ${f_{1}{(\mathbf{x},t)}} + {f_{2}{(\mathbf{x},t)}}$ is g-convex in the same metric.

### Example 9

Consider a function $f_{1}{(\mathbf{x}_{1},\mathbf{y}_{1},t)}$ g-convex for each $t$ in a block diagonal metric ${BlkDiag}{({\mathbf{M}_{x_{1}}{(\mathbf{x}_{1})}},{\mathbf{M}_{y}{(\mathbf{y}_{1})}})}$ and a function $f_{2}{(\mathbf{x}_{2},\mathbf{y}_{2},t)}$ g-convex for each $t$ in a block diagonal metric ${BlkDiag}{({\mathbf{M}_{x_{2}}{(\mathbf{x}_{2})}},{\mathbf{M}_{y}{(\mathbf{y}_{2})}})}$. Then, the function: is g-convex in metric ${BlkDiag}{(\mathbf{M}_{x_{1}},\mathbf{M}_{x_{2}},\mathbf{M}_{y})}$ for each $t$.

### Skew-Symmetric Feedback Coupling

Assume that a scalar function $f_{1}{(\mathbf{x}_{1},\mathbf{x}_{2})}$ is $\alpha_{1}$-strongly g-convex in $\mathbf{x}_{1}$ in a metric $\mathbf{M}_{1}{(\mathbf{x}_{1})}$ for each fixed $\mathbf{x}_{2}$, and similarly that a scalar function $f_{2}{(\mathbf{x}_{1},\mathbf{x}_{2})}$ is $\alpha_{2}$-strongly g-convex in a metric $\mathbf{M}_{2}{(\mathbf{x}_{2})}$ for each fixed $\mathbf{x}_{1}$. If $f_{1}$ and $f_{2}$ satisfy the scaled skew-symmetry property where $k$ is some strictly positive constant, then the natural gradient dynamics is contracting with rate $\min{(\alpha_{1},\alpha_{2})}$ in metric ${\mathbf{M}{(\mathbf{x}_{1},\mathbf{x}_{2})}} = {{BlkDiag}{({\mathbf{M}_{1}{(\mathbf{x}_{1})}},{k\mathbf{M}_{2}{(\mathbf{x}_{2})}})}}$. Since the overall system is both contracting and autonomous, it tends to a unique equilibrium $(\mathbf{x}_{1}^{\ast},\mathbf{x}_{2}^{\ast})$ which satisfies the Nash-like conditions Note that the result can be broadened to cases where the scaled skew-symmetry property is not exactly satisfied, by using the small-gain extension. Taking again the machine learning context as a potential example, such two-player game dynamics can occur in certain types of adversarial training.

The result extends to a game with an arbitrary number of players. Consider $n$ functions ${\{{f_{i}{(\mathbf{x}_{1},\ldots,\mathbf{x}_{n})}}\}}_{i = 1}^{n}$ such that each $f_{i}$ is $\alpha_{i}$-strongly g-convex over $\mathbf{x}_{i}$ in a metric $\mathbf{M}_{i}{(\mathbf{x}_{i})}$. If the functions satisfy the skew-symmetry conditions for each $j > i$, then the suitable generalizations of result in a coupled system that is contracting with rate $\min{(\alpha_{1},\ldots,\alpha_{n})}$ in the metric The overall system converges to a unique Nash-like equilibrium satisfying and a similar relation for each other player.

Likewise, the result can be extended to the case when the natural gradient dynamics for each individual player may only be semi-contracting.

### Theorem 6

Consider the two player case, wherein (a) $f_{1}$ is $\alpha_{1}$-strongly g-convex with $\alpha_{1} > 0$ in a uniformly positive definite metric $\mathbf{M}_{1}{(\mathbf{x}_{1})}$ for each $\mathbf{x}_{2}$ (b) the Riemannian Hessian $\mathbf{H}_{2}{(\mathbf{x}_{1},\mathbf{x}_{2})}$ of $f_{2}{(\mathbf{x}_{1},\mathbf{x}_{2})}$ in $\mathbf{x}_{2}$ is only positive semi-definite for each $\mathbf{x}_{1}$ in a uniformly positive definite metric $\mathbf{M}_{2}{(\mathbf{x}_{2})}$ and (c) the skew-symmetry property holds. Assume that one trajectory of is known to be bounded. Then, every trajectory of converges to a Nash equilibrium $\mathbf{x}_{1}^{\ast}$, $\mathbf{x}_{2}^{\ast}$. Moreover, $\mathbf{x}_{1}^{\ast}$ does not depend on initial conditions (i.e., every Nash has the same strategy for player 1).

### Proof

It can be shown that virtual displacements evolve such that which implies, by Barbalat's lemma, Via the same argument as follows, it follows that ${{\nabla_{\mathbf{x}_{1}}f_{1}}{({\mathbf{x}_{1}{(t)}},{\mathbf{x}_{2}{(t)}})}}\rightarrow 0$ as $t\rightarrow\infty$. So, for each initial condition, $\mathbf{x}_{1}{(t)}$ must converge to some equilibrium $\mathbf{x}_{1}^{\ast}$ of the $\mathbf{x}_{1}$ dynamics. Furthermore, since any ${\delta\mathbf{x}_{1}}\rightarrow 0$, $\mathbf{x}_{1}^{\ast}$ must be unique and independent of initial conditions. Let us now turn to the behavior of the $\mathbf{x}_{2}$ dynamics. Given an arbitrary initial condition $(\mathbf{x}_{1,0}$, $\mathbf{x}_{2,0})$, let $L^{+}$ denote its $\omega$-limit set. Any point in ${(\mathbf{x}_{1},\mathbf{x}_{2})} \in L^{+}$ must satisfy $\mathbf{x}_{1} = \mathbf{x}_{1}^{\ast}$. Since the dynamics are autonomous, $L^{+}$ is composed of trajectories of the system Moreover, $L^{+}$ must be closed and bounded. Since is a natural gradient system of a g-convex function, Thm. 2. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems") ensures that any trajectory of must converge to an equilibrium point that is a global minimizer for $f_{2}{(\mathbf{x}_{1}^{\ast},\mathbf{x}_{2})}$. Considering any initial condition of that begins in $L^{+}$, we denote ${(\mathbf{x}_{1}^{\ast},\mathbf{x}_{2}^{\ast})} \in L^{+}$ as the resulting equilibrium point. However, since is semi-contracting, any geodesic ball around $(\mathbf{x}_{1}^{\ast},\mathbf{x}_{2}^{\ast})$ is forward invariant, which implies that $L^{+} = {\{{(\mathbf{x}_{1}^{\ast},\mathbf{x}_{2}^{\ast})}\}}$. Thus, ${\mathbf{x}_{2}{(t)}}\rightarrow\mathbf{x}_{2}^{\ast}$ as $t\rightarrow\infty$. Note again that, while $\mathbf{x}_{2}^{\ast}$ depends on initial conditions, $\mathbf{x}_{1}^{\ast}$ does not. ∎

### Corollary 3

Consider any two equilibrium points $(\mathbf{x}_{1}^{\ast},\mathbf{x}_{21}^{\ast})$ and $(\mathbf{x}_{1}^{\ast},\mathbf{x}_{22}^{\ast})$ for a system that satisfies the condition of Theorem 6. Then, the geodesic between these points is comprised of extremal Nash equilibrium points, all of which have the same cost.

Further, if one equilibrium of is locally asymptotically stable, then it is necessarily globally attractive, and thus all trajectories of converge to this unique equilibrium $(\mathbf{x}_{1}^{\ast},\mathbf{x}_{2}^{\ast})$ regardless of initial conditions.

### Proof

Proof of the first part follows immediately from applying Corollary 3.1 of to the function $f_{2}{(\mathbf{x}_{1}^{\ast},\mathbf{x}_{2})}$. Proof of the second part follows immediately from the application of Corollary 1 herein. ∎

### Corollary 4

### Proof

Consider Thm. 6 with $f_{1} = {\mathcal{L}{(\mathbf{x},{\mathbf{λ}})}}$ and $f_{2} = {- {\mathcal{L}{(\mathbf{x},{\mathbf{λ}})}}}$. ∎

### Hierarchical Natural Gradient

Consider a function $f_{1}{(\mathbf{x}_{1})}$ $\alpha_{1}$-strongly g-convex in a metric $\mathbf{M}_{1}{(\mathbf{x}_{1})}$, and a function $f_{2}{(\mathbf{x}_{1},\mathbf{x}_{2})}$ $\alpha_{2}$-strongly g-convex in a metric $\mathbf{M}_{2}{(\mathbf{x}_{2})}$ for each given $\mathbf{x}_{1}$. Then, the hierarchical natural gradient dynamics is contracting with rate $\min{(\alpha_{1},\alpha_{2})}$ in metric ${\mathbf{M}{(\mathbf{x}_{1},\mathbf{x}_{2})}} = {{BlkDiag}{({\mathbf{M}_{1}{(\mathbf{x}_{1})}},{\mathbf{M}_{2}{(\mathbf{x}_{2})}})}}$, under the mild assumption that the coupling Jacobian is bounded. Since the overall system is both contracting and autonomous, it tends to a unique equilibrium at rate $\min{(\alpha_{1},\alpha_{2})}$, and thus to the unique solution of By recursion, this structure can be chained an arbitrary number of times, or applied to any cascade or directed acyclic graph of natural gradient dynamics. Such hierarchical optimization may play a role, for instance, in backpropagation of natural gradients in machine learning, with all descents occurring concurrently rather than in sequence.

### Remark 24

In large-scale optimization settings such as those appearing commonly in machine learning, natural gradient with a fully-dense metric can become intractable. In specific cases, such as natural gradient descent based on Fisher information, computationally effective approximations have been derived. In addition, the combination of simple (e.g., diagonal) metrics through hierarchical structures lends an opportunity to recover significant complexity at broad scale $-$ see, e.g., the hierarchical combination of scalar metrics to learn hierarchical representations of symbolic data . Such simpler metrics are also well motivated in the context of positive or monotone systems. In special cases of a dense Hessian metric ${\mathbf{M}{(\mathbf{x})}} = {{\nabla^{2}\psi}{(\mathbf{x})}}$ from a potential $\psi{(\mathbf{x})}$, note that continuous mirror descent (see also Proposition 5. ‣ 2.3 Examples ‣ 2 Contraction Analysis of Gradient Systems") and Example 4) provides an alternate method to compute continuous natural gradient. These methods can avoid the need to invert the metric in cases where there is an explicit inverse exists for the change of variables $\mathbf{z} = {{\nabla\psi}{(\mathbf{x})}}$, or when can be run at a fast time scale to invert the gradient map through dynamics.

## Conclusions

Overall, this paper has demonstrated that nonlinear contraction analysis provides a general perspective for analyzing and certifying the global convergence properties of gradient-based optimization algorithms. The common case of strong convexity corresponds to the special case of contracting gradient descent in the identity metric, while our analysis admits global convergence results in the significantly broader case of state-dependent metrics. This result has clear links to the case of geodesically-convex optimization wherein natural gradient descent converges to a unique equilibrium if it is contracting in any metric, broadening from the special case of g-convexity corresponding to contraction in the natural metric. Our analysis of semi-contraction of gradient systems, and the resulting smoothly connected sets of global optima may shed additional light on applications in learning with over parameterized networks where the set of optimizers is recognized to take the form of a low-dimensional manifold. Results on natural primal dual and the convergence to Nash equilibria showcase the broad reach of these fundamental results, where they may serve as the basis for the generation of larger scale distributed optimization algorithms in future work. A framework we call Contraction + shows how contraction or semi-contraction properties can be combined with specific but coarse information on a system, such as the local stability of a particular equilibrium or the weak decreasing of a cost or a Lyapunov-like function, to conclude on global convergence or minimization.

A natural next step for the application of contraction in optimization is to design geodesic quorum sensing algorithms for synchronization, as well as other consensus mechanisms considering time-delays, which may serve as the basis for distributed and large-scale optimization techniques on Riemannian manifolds. Other future applications will consider stochastic gradient descent in the Riemannian setting with quorum sensing extensions (as, e.g., in ). Such advances could have direct applications, e.g., in the context of machine learning, among others.

Acknowledgements We thank Nicholas Boffi for stimulating discussions. This research was supported in part by grant 1809314 from the National Science Foundation.

## Supporting Information

### Proof of Theorem 1

We precede the proof of Theorem 1 with a more general result that links contraction with the notion of taking covariant derivatives.

If we view ${\mathbf{h}{(\mathbf{x},t)}}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}}\rightarrow{\mathbb{R}}^{n}}$ as providing the components of a vector field, then its covariant derivative (w.r.t. the Riemannian connection $\overset{\mathbf{M}}{\nabla}$) along the $i$-th coordinate vector field has components: where $\Gamma_{ij}^{k}$ denotes the Christoffel symbol of the second kind and the usual Einstein summation convention is applied (implying, e.g., a sum over $k$ in the above equations).

By contrast, if we view a function ${\mathbf{g}{(\mathbf{x},t)}}:{{{\mathbb{R}}^{n} \times {\mathbb{R}}}\rightarrow{\mathbb{R}}^{n}}$ as giving the components of a co-vector field (i.e., a covariant vector field) we have: where the ^∗^ on $\overset{\mathbf{M}}{\nabla}^{\ast}$ denotes that we are considering $\mathbf{g}$ as giving the components of a co-vector field. In either case, we can collect these derivatives along each coordinate vector field into Jacobian-like matrices denoted: We are now prepared to state the main Proposition involved in proving Theorem 1.

### Proposition A.1

Consider a dynamical system $\overset{˙}{\mathbf{x}} = {\mathbf{h}{(\mathbf{x},t)}}$ which we re-write in the form: where $\mathbf{h} = {\mathbf{M}^{- 1}\mathbf{g}}$. Then, we have the equivalence:

### Proof

To assist the proof, we define First consider the partials of $\mathbf{h} = {\mathbf{M}^{- 1}\mathbf{g}}$, Using this result Noting that ${M_{ik}M^{kj}} = \delta_{ij}$, with $\delta_{ij}$ the Kronecker delta, Where the last line follows since $\Gamma_{ij}^{\ell} = \Gamma_{ji}^{\ell}$ for the symbols of the Riemmanian connection $\overset{\mathbf{M}}{\nabla}$. ∎

### Remark A.1

Following the setup for the previous proposition, the covariant derivatives can also be shown to satisfy: which immediately gives:

### Remark A.2

We consider the metric factored as $\mathbf{M} = {\mathbf{\Theta}^{\top}\mathbf{\Theta}}$ with the generalized Jacobian defined according to where we associate ${\delta\mathbf{z}} = {\Theta\delta\mathbf{x}}$ as a differential change of coordinates. The generalized Jacobian satisfies that, along the flow of the system, local perturbations evolve according to ${\frac{d}{dt}\delta\mathbf{z}} = {\mathbf{F}\delta\mathbf{z}}$.

Considering a similarity transform on $\mathbf{F}$ we see that the right-hand side takes a similar structural form to the covariant derivative, as noted originally. Indeed, defining some new connection coefficients: determines an affine connection with covariant derivatives uniquely specified according to where $\mathbf{e}_{j}$ gives the $j$-th unit vector. (Note this equation uses the symbols to sum over vectors, as opposed to components of vectors as previously.) While this new connection can be shown to be metric compatible (as defined in), it is not in general equal to the one provided by the Riemannian connection $\overset{\mathbf{M}}{\nabla}$ with the corresponding symbols $\Gamma_{jk}^{i}$ via. Any differences do not affect the final contraction analysis in the sense that relationship still holds when the Riemannian connection $\overset{\mathbf{M}}{\nabla}$ is replaced with any metric-compatible connection. However, and therefore does not hold in general.

We are now ready to prove Theorem 1 from the main text.

### Proof of Theorem 1

Recall that $\alpha$-strong geodesic convexity of $f{(\mathbf{x},t)}$ in the metric $\mathbf{M}{(\mathbf{x})}$ (for each $t$) is equivalent to the Riemannian Hessian of $f$, denoted $\mathbf{H}{(\mathbf{x},t)}$, satisfying: In coordinates, entries of $\mathbf{H}$ are given by which we see is directly related to taking the covariant derivative of the co-vector field with components $\partial_{k}f$. More specifically, defining ${\mathbf{g}{(\mathbf{x},t)}} = {- {{\nabla f}{(\mathbf{x},t)}}}$ we have: Via Proposition A.1, we thus have $\mathbf{Q} = {{\mathbf{M}\left(\frac{\partial\mathbf{h}}{\partial\mathbf{x}} \right)} + {\left(\frac{\partial\mathbf{h}}{\partial\mathbf{x}} \right)^{\top}\mathbf{M}} + \overset{˙}{\mathbf{M}}} = {- {2\mathbf{H}}}$ such that contraction of the natural gradient dynamics (9. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) with rate $\alpha$ under the inequality is equivalent to requiring $\mathbf{H} \succeq {\alpha\mathbf{M}}$.
