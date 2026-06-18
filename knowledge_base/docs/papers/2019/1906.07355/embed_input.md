Escaping from Saddle Points on Riemannian Manifolds

We consider minimizing a nonconvex, smooth function f on a Riemannian manifold M. We show that a perturbed version of Riemannian gradient descent algorithm converges to a second-order stationary point (and hence is able to escape saddle points on the manifold). The rate of convergence depends as 1/epsilon^ on the accuracy epsilon, which matches a rate known only for unconstrained smooth minimization. The convergence rate depends polylogarithmically on the manifold dimension d, hence is almost dimension-free. The rate also has a polynomial dependence on the parameters describing the curvature of the manifold and the smoothness of the function. While the unconstrained problem (Euclidean setting) is well-studied, our result is the first to prove such a rate for nonconvex, manifold-constrained problems.

## Introduction

We consider minimizing a non-convex smooth function on a smooth manifold $\mathcal{M}$,

where $\mathcal{M}$ is a $d$-dimensional smooth manifold^11^1Here $d$ is the dimension of the manifold itself; we do not consider $\mathcal{M}$ as a submanifold of a higher dimensional space. For instance, if $\mathcal{M}$ is a 2-dimensional sphere embedded in ${\mathbb{R}}^{3}$, its dimension is $d = 2$., and $f$ is twice differentiable, with a Hessian that is $\rho$-Lipschitz (assumptions are formalized in section 4). This framework includes a wide range of fundamental problems (often non-convex), such as PCA, dictionary learning, low rank matrix completion, and tensor factorization. Finding the global minimum to Eq....

We have shown that for the constrained optimization problem of minimizing $f{(x)}$ subject to a manifold constraint as long as the function and the manifold are appropriately smooth, a perturbed Riemannian gradient descent algorithm will escape saddle points with a rate of order $1/\epsilon^{2}$ in the accuracy $\epsilon$, polylog in manifold dimension $d$, and depends polynomially on the curvature and smoothness parameters.

A natural extension of our result is to consider other variants of gradient descent, such as the heavy ball method, Nesterov's acceleration, and the stochastic setting. The question is whether these algorithms with appropriate modification (with manifold constraints) would have a fast convergence to second-order stationary point (not just first-order stationary as studied in recent literature), and whether it is possible to show the relationship between convergence rate and smoothness of manifold.

### Lemma 2

### Assumption 3 (Bounded sectional curvature)

Finally we need the following corollary of the Ambrose-Singer theorem.

In the Euclidean space, it is known that with random initialization, gradient descent avoids saddle points asymptotically. Lee et al. (section 5.5) show that this is also true on smooth manifolds, although the result is expressed in terms of nonstandard manifold smoothness measures. Also, importantly, this line of work does not give quantitative rates for the algorithm's behaviour near saddle points.

Du et al. show gradient descent can be *exponentially slow* in the presence of saddle points. To alleviate this phenomenon, it is shown that for a $\beta$-gradient Lipschitz,...
