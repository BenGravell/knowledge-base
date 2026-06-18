Beyond Convexity - Contraction and Global Convergence of Gradient Descent

Topics include Convex optimization, Gradient descent, Natural gradients, Online algorithms, Optimization.

This paper considers the analysis of continuous time gradient-based optimization algorithms through the lens of nonlinear contraction theory. It demonstrates that in the case of a time-invariant objective, most elementary results on gradient descent based on convexity can be replaced by much more general results based on contraction. In particular, gradient descent converges to a unique equilibrium if its dynamics are contracting in any metric, with convexity of the cost corresponding to the special case of contraction in the identity metric. More broadly, contraction analysis provides new insights for the case of geodesically-convex optimization, wherein non-convex problems in Euclidean space can be transformed to convex ones posed over a Riemannian manifold. In this case, natural gradient descent converges to a unique equilibrium if it is contracting in any metric, with geodesic convexity of the cost corresponding to contraction in the natural metric. New results using semi-contraction provide additional insights into the topology of the set of optimizers in the case when multiple optima exist....

## Introduction

This paper considers the analysis of continuous-time gradient-based optimization through the lens of nonlinear contraction theory. It is motivated, in part, by recent observations in machine learning that arise in the application of gradient descent (or its stochastic counterpart) for the training of over-parameterized networks. Modern networks often possess many more parameters than training examples and can fit the labels perfectly, resulting in submanifold valleys of the parameter space with equal cost. Moreover, recent results suggest that highly-redundant networks experience few to no local optima that are not global optima....

Although convex problems admit provable globally optimal solutions, other broader classes of functions share this same property. For example, Invex functions guarantee that any local optimum is a global optimum, although the utility of invexity conditions remains a point of contention. Functions satisfying the Polyak-Lojasiewicz (PL) inequality give rise to exponentially convergent gradient descent to a provably optimal solution....

### Theorem 1 (Equivalence between g-Strong Convexity and Contraction of Natural Gradient)

Then, $f$ is $\alpha$-strongly g-convex in the metric $\mathbf{M}$ for each $t$ if and only if (9. ‣ 2.2 Relationship Between Geodesic Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) is contracting with rate $\alpha$ in the metric $\mathbf{M}$. More specifically, the Riemannian Hessian verifies

From this example, it is clear that strongly convex functions are a special case of ones whose gradient systems are contracting. The following proposition shows that one does not lose the convergence properties to a global optimum on this more general class of functions.

If a twice differentiable function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ is $\alpha$-strongly convex, then its gradient system

Let $\mathbf{x}^{\ast}$ denote an element of $\omega{\lbrack{\mathbf{x}{(t;\mathbf{x}_{0})}}\rbrack}$. Since (5. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems")) is a gradient system, Theorem 15.0.3 of guarantees that $\mathbf{x}^{\ast}$ must be an equilibrium point of (5. ‣ 2.1 Relationships Between Convexity and Contraction ‣ 2 Contraction Analysis of Gradient Systems"))....
