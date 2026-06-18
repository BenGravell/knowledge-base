Small Errors in Random Zeroth-order Optimization Are Imaginary

Topics include Optimization.

Most zeroth-order optimization algorithms mimic a first-order algorithm but replace the gradient of the objective function with some gradient estimator that can be computed from a small number of function evaluations. This estimator is constructed randomly, and its expectation matches the gradient of a smooth approximation of the objective function whose quality improves as the underlying smoothing parameter delta is reduced. Gradient estimators requiring a smaller number of function evaluations are preferable from a computational point of view. While estimators based on a single function evaluation can be obtained by use of the divergence theorem from vector calculus, their variance explodes as delta tends to 0. Estimators based on multiple function evaluations, on the other hand, suffer from numerical cancellation when delta tends to 0. To combat both effects simultaneously, we extend the objective function to the complex domain and construct a gradient estimator that evaluates the objective at a complex point whose coordinates have small imaginary parts of the order delta. As this estimator requires only one function evaluation, it is immune to cancellation....

## Introduction

We study optimization problems of the form

where $f:{\mathcal{D}\rightarrow{\mathbb{R}}}$ is a real analytic and thus smooth objective function defined on an open set $\mathcal{D} \subseteq {\mathbb{R}}^{n}$, and $\mathcal{X} \subseteq \mathcal{D}$ is a non-empty closed feasible set. Throughout the paper we assume that problem (1.1) admits a global minimizer $x^{\star}$ and that the objective function $f$ can only be accessed through a deterministic zeroth-order oracle, which outputs function evaluations at prescribed test points....

## Conclusions and future work

The cancellation effects that plague all multi-point gradient estimators tend to have a detrimental effect on the numerical stability and the convergence behavior of zeroth-order algorithms. These numerical problems can sometimes be mitigated by replacing the terminal iterate $x_{K}$ with the averaged iterate ${\overline{x}}_{K} = {\frac{1}{K}{\sum_{k = 1}^{K}x_{k}}}$, at the cost of slower convergence. The single-point complex-step gradient estimator thus provides an attractive alternative to the classical gradient estimators because it leads to provably fast and numerically stable algorithms....

where the two equalities hold because the sought covariance matrix must be isotropic and because ${\| y\|}_{2} = 1$ for all $y \in {\mathbb{S}}^{n - 1}$, respectively. Thus, the gradient of $f$ can be represented as ${{\nabla f}{(x)}} = {n{\int_{{\mathbb{S}}^{n - 1}}{{\langle{{\nabla f}{(x)}},y\rangle}y\sigma{({dy})}}}}$. Together with Proposition 3.3. ‣ 3 A smoothed complex-step approximation ‣ Small errors in random zeroth-order optimization are imaginary"), this yields the estimate

To showcase the power of the complex-step method and to expose the numerical difficulties encountered by finite-difference methods, we approximate the derivative of ${f{(x)}} = x^{3}$ at $x \in {\{{- 1},0,10\}}$ via a forward-difference ($\mathsf{f}\mathsf{d}$), central-difference ($\mathsf{c}\mathsf{d}$) and complex-step ($\mathsf{c}\mathsf{s}$) method, that is, for small values of $\delta$ we compare ${f_{\mathsf{f}\mathsf{d}}{(x,\delta)}} = {\frac{1}{\delta}{({{f{({x + \delta})}} - {f{(x)}}})}}$, ${f_{\mathsf{c}\mathsf{d}}{(x,\delta)}} = {\frac{1}{2\delta}{({{f{({x + \delta})}} - {f{({x - \delta})}}})}}$ and...

### Theorem 5.1 (Convergence rate of Algorithm 4.1 for strongly convex optimization)
