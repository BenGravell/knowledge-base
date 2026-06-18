<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Beyond Convexity - Contraction and Global Convergence of Gradient Descent

Topics include Convex optimization, Gradient descent, Natural gradients, Online algorithms, Optimization.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper considers the analysis of continuous time gradient-based optimization algorithms through the lens of nonlinear contraction theory. It demonstrates that in the case of a time-invariant objective, most elementary results on gradient descent based on convexity can be replaced by much more general results based on contraction. In particular, gradient descent converges to a unique equilibrium if its dynamics are contracting in any metric, with convexity of the cost corresponding to the special case of contraction in the identity metric. More broadly, contraction analysis provides new insights for the case of geodesically-convex optimization, wherein non-convex problems in Euclidean space can be transformed to convex ones posed over a Riemannian manifold. In this case, natural gradient descent converges to a unique equilibrium if it is contracting in any metric, with geodesic convexity of the cost corresponding to contraction in the natural metric. New results using semi-contraction provide additional insights into the topology of the set of optimizers in the case when multiple optima exist. Furthermore, they show how semi-contraction may be combined with specific additional information to reach broad conclusions about a dynamical system. The contraction perspective also easily extends to time-varying optimization settings and allows one to recursively build large optimization structures out of simpler elements.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Extensions to natural primal-dual optimization and game-theoretic contexts further illustrate the potential reach of these new perspectives.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper considers the analysis of continuous-time gradient-based optimization through the lens of nonlinear contraction theory. It is motivated, in part, by recent observations in machine learning that arise in the application of gradient descent (or its stochastic counterpart) for the training of over-parameterized networks. Modern networks often possess many more parameters than training examples and can fit the labels perfectly, resulting in submanifold valleys of the parameter space with equal cost. Moreover, recent results suggest that highly-redundant networks experience few to no local optima that are not global optima. These observations may be surprising in light of the fact that the loss landscapes for these problems are rarely convex.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although convex problems admit provable globally optimal solutions, other broader classes of functions share this same property. For example, Invex functions guarantee that any local optimum is a global optimum, although the utility of invexity conditions remains a point of contention. Functions satisfying the Polyak-Lojasiewicz (PL) inequality give rise to exponentially convergent gradient descent to a provably optimal solution. While the PL condition is, in general, difficult to verify without an a-priori known globally optimal solution, the existence of zero-loss solutions in over-parameterized learning makes it tractable in important special cases. Geodesic convexity generalizes convexity to a Riemannian setting, with applicability to optimization on manifolds, as well as to conventional Euclidean settings where ${\mathbb{R}}^{n}$ is endowed with a manifold structure through the definition of a metric. Here, we consider another class of conditions for the convergence of gradient and natural gradient descent to a globally optimal point. We do so through adopting the perspective of nonlinear contraction theory and analyzing gradient descent in continuous time.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contraction theory allows the stability of nonlinear non-autonomous systems to be characterized through linear time-varying dynamics describing the propagation of infinitesimally small displacements along the systems' flow. The existence of a Riemannian metric that contracts these virtual displacements (i.e., elements in the tangent space) is necessary and sufficient for exponential convergence of any pair of trajectories. Contraction naturally yields methods for constructing stable systems of systems, including synchronization phenomena and consensus as well as other key building blocks that allow the construction of large contracting systems out of simpler elements. These properties provide opportunities to construct larger optimization structures from simpler elements (e.g., in distributed or competitive optimization settings).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The contribution of this paper is to apply these contraction tools for the analysis of gradient and natural gradient optimization. We consider optimization problems posed over ${\mathbb{R}}^{n}$ wherein no explicit manifold structure necessarily exists a-priori. Instead, we consider the analysis of optimization following endowing these problems with additional structure (a Riemannian metric), analyzing their convergence, and considering the use of contraction tools to build larger optimization structures out of smaller ones. Analysis proceeds in continuous time. While this approach is limited, in part, by the fact that computational optimization algorithms require a discrete implementation, a continuous perspective has yielded insight on important phenomena such as in the analysis, discrete implementations, and extensions of Nesterov's accelerated gradient descent method. It has also enabled analysis of primal-dual algorithms, where an absolute time reference is obtained by introducing additional fast dynamics or delays using a singular perturbation framework. Recent results provide principled tools to derive discrete-time implementations that preserve specific continuous-time convergence rates.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The paper is organized as follows. Section 2 provides our main results, detailing the applicability of contraction theory to analyze gradient descent in continuous time. We show that convex functions represent the special case of contraction in the identity metric. The flexibility afforded by state-dependent contraction metrics, however, enables significant extra freedom for guaranteeing that all local optima are globally optimal. We then consider the extensions of these results to natural gradient descent, where geodesic convexity of a function corresponds to contraction of its natural gradient system in the natural metric. In both cases, results highlight the topology of the set of optimizers in the case of semi-contraction, which would have most direct applicability to over-parameterized networks. New results also show how semi-contraction may be combined with specific additional information to reach broad conclusions about a dynamical system. Section 3 details extensions of these results to the case of primal-dual type dynamics that appear in mixed convex/concave saddle systems, and shows how a broad class of natural adaptive control laws can be interpreted as a primal-dual system. Section 4 discusses the special case of g-convex functions and associated combination properties for interfacing with other models.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Section 5 provides an outlook on potential future advances that may stem from these connections.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Contraction Analysis of Gradient Systems", "weight": 1.0} -->

We first recall basic definitions and facts on convex optimization and show how a contraction analysis of gradient-based optimization considerably generalizes the class of functions that admit a unique global optimum. Following this presentation, results are generalized to the case of geodesically-convex optimization, which is particularly suited to analysis via contraction tools. Throughout this analysis, given a differentiable function $\mathbf{h}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{m}}$, we denote the Jacobian of $\mathbf{h}{(\mathbf{x})}$ by

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contraction Analysis of Gradient Systems", "weight": 1.0} -->

In the special case of a scalar-valued function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ we denote the gradient of $f{(\mathbf{x})}$ by

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contraction Analysis of Gradient Systems", "weight": 1.0} -->

and its Hessian by ${\nabla^{2}f}{(\mathbf{x})}$. Unless otherwise stated, we assume all functions are sufficiently smooth such that derivatives of the necessary order exist and are continuous.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contraction Analysis of Gradient Systems", "weight": 1.0} -->

Before we embark on this discussion, let us note that of course, as illustrated, e.g., in and in the following example, continuous-time analysis tools in general may be used to conceptually illuminate the mechanisms involved in discrete-time algorithms. As this paper will show, contraction tools give particularly simple insights into important classes of optimization problems, such as, e.g., geodesically-convex optimization.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Example 1", "weight": 1.0} -->

The Polyak-Lojasiewicz (PL) inequality is one of the most general sufficient conditions for discrete-time gradient descent to exhibit linear convergence rates without strong convexity of the cost. A function is said to satisfy the PL inequality if it has a (typically unknown) global minimum value $f^{\ast}$ and there exists a constant $\mu > 0$ such that

<!-- chunk {"id": "body-0015", "role": "body", "section": "Example 1", "weight": 1.0} -->

Consider gradient descent on the cost function $f{(\mathbf{x})}$ from a continuous-time point of view,

<!-- chunk {"id": "body-0016", "role": "body", "section": "Example 1", "weight": 1.0} -->

Using $V = {{f{(\mathbf{x})}} - f^{\ast}}$ as a Lyapunov-like function, and then requiring that $V$ converges exponentially with rate $\mu$, yields

<!-- chunk {"id": "body-0017", "role": "body", "section": "Example 1", "weight": 1.0} -->

The inequality above is exactly the PL condition. Thus, we see that the PL condition is nothing but the condition for exponential convergence of the residual cost $V = {{f{(\mathbf{x})}} - f^{\ast}}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Example 1", "weight": 1.0} -->

Similarly, imposing $\overset{˙}{V} \leq {- {\mu\sqrt{V}}}$, corresponding to finite-time convergence (in time less than ${2\sqrt{V{}}}/\mu$ ), would require a modified PL-like condition

<!-- chunk {"id": "body-0019", "role": "body", "section": "Example 1", "weight": 1.0} -->

By comparison, the results pursued via contraction analysis in this paper will ensure exponential convergence of any pair of trajectories for gradient descent, but likewise will ensure convergence of those solutions to a global optimum.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Example 2", "weight": 1.0} -->

Consider an $\alpha$-strongly convex function $f$ and its associated gradient descent system (1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")). Since $f$ is strongly convex, it has a unique global minimum $\mathbf{x}^{\ast}$, which is a equilibrium point of (1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")). It can be verified that the gradient descent dynamics of $f$ are contracting in the identity metric $\mathbf{M} = \mathbf{I}$ with rate $\alpha$. Since geodesic distances are just Euclidean distances in this metric, immediately implies that

<!-- chunk {"id": "body-0021", "role": "body", "section": "Example 2", "weight": 1.0} -->

thus proving Proposition 1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems").

<!-- chunk {"id": "body-0022", "role": "body", "section": "Example 2", "weight": 1.0} -->

From this example, it is clear that strongly convex functions are a special case of ones whose gradient systems are contracting. The following proposition shows that one does not lose the convergence properties to a global optimum on this more general class of functions.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 1", "weight": 1.0} -->

In the case that a contraction metric needs to be found numerically, note that the conditions (2. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) for certifying contraction or semi-contraction are convex criteria. Thus, in many instances, the process of finding a metric numerically to verify contraction may be accomplished via convex optimization approaches, such as those based on sums-of-squares programming.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Relationship Between Geodesic Convexity and Contraction", "weight": 1.0} -->

Geodesic convexity generalizes conventional notions of convexity to the case where the domain of a function is equipped with a Riemannian metric. A special case occurs in geometric programming (GP). In GP, a non-convex problem over positive variables ${\{ x_{i}\}}_{i = 1}^{N}$ can be transformed into a convex problem by a change of variables $y_{i} = {\log{(x_{i})}}$. Alternately GP can be formulated over the positive reals viewed as a Riemannian manifold by measuring differential length elements $ds$ in a relative sense

<!-- chunk {"id": "body-0025", "role": "body", "section": "Relationship Between Geodesic Convexity and Contraction", "weight": 1.0} -->

Geodesically-convex optimization generalizes this transformation strategy to a broader class of problems. However, beyond special cases (see, e.g., ), generative procedures remain lacking to formulate g-convex optimization problems or recognize g-convexity.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Relationship Between Geodesic Convexity and Contraction", "weight": 1.0} -->

To introduce g-convexity more formally, consider a function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ and a positive definite metric $\mathbf{M}:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n \times n}}$. We note that geodesic convexity of $f$ is not an intrinsic property of the function itself, but rather is a property of $f$ defined on the Riemannian manifold $({\mathbb{R}}^{n},\mathbf{M})$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 2", "weight": 1.0} -->

When $\mathbf{M}{(\mathbf{x})}$ is the Hessian of some twice differentiable strictly convex scalar function $\psi{(\mathbf{x})}$, natural gradient descent coincides with the continuous-time limit of mirror descent \[34, Sec. 2.3\] with potential $\psi{(\mathbf{x})}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 3", "weight": 1.0} -->

From a differential geometric viewpoint, the first covariant derivative of $f$ is a covector field given in coordinates by ${\nabla f}{(\mathbf{x})}$, while the natural gradient is a vector field given in coordinates by $\mathbf{M}{(\mathbf{x})}^{- 1}{\nabla f}{(\mathbf{x})}$. In a Euclidean context, where $\mathbf{M}{(\mathbf{x})}$ is identity, this distinction between covariant (covector) and contravariant (vector) representations of the gradient is immaterial.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 3", "weight": 1.0} -->

Similarly, the Riemannian Hessian $\mathbf{H}$ represents in coordinates the second covariant derivative of $f$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 3", "weight": 1.0} -->

When $\mathbf{M}$ is the identity metric, geodesic $\alpha$-strong convexity naturally coincides with the definition of $\alpha$-strong convexity in Definition 1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems"). The natural gradient can be used to directly mirror Proposition 1. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems") within the Riemannian context.
