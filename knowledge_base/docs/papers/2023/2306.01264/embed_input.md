Convex and Non-convex Optimization under Generalized Smoothness

Classical analysis of convex and non-convex optimization methods often requires the Lipshitzness of the gradient, which limits the analysis to functions bounded by quadratics. Recent work relaxed this requirement to a non-uniform smoothness condition with the Hessian norm bounded by an affine function of the gradient norm, and proved convergence in the non-convex setting via gradient clipping, assuming bounded noise. In this paper, we further generalize this non-uniform smoothness condition and develop a simple, yet powerful analysis technique that bounds the gradients along the trajectory, thereby leading to stronger results for both convex and non-convex optimization problems. In particular, we obtain the classical convergence rates for (stochastic) gradient descent and Nesterov's accelerated gradient method in the convex and/or non-convex setting under this general smoothness condition. The new analysis approach does not require gradient clipping and allows heavy-tailed noise with bounded variance in the stochastic setting.

## Introduction

In this paper, we study the following *unconstrained* optimization problem

where $\mathcal{X} \subseteq {\mathbb{R}}^{d}$ is the domain of $f$. Classical textbook analyses of often require the Lipschitz smoothness condition, which assumes $\left\| {{\nabla^{2}f}{(x)}} \right\| \leq L$ almost everywhere for some $L \geq 0$ called the smoothness constant. This condition, however, is rather restrictive and only satisfied by functions that are both upper and lower bounded by quadratic functions.

In this paper, we significantly generalize the $(L_{0},L_{1})$-smoothness condition to the $\ell$-smoothness condition which assumes $\left\| {{\nabla^{2}f}{(x)}} \right\| \leq {\ell{(\left\| {{\nabla f}{(x)}} \right\|)}}$ for some non-decreasing continuous function $\ell$. We develop a simple, yet powerful approach, which allows us to obtain stronger results for *both convex and non-convex* optimization problems when $\ell$ is sub-quadratic (i.e., ${\lim_{u\rightarrow\infty}{{\ell{(u)}}/u^{2}}} = 0$) or even more general.

## Conclusion

In this paper, we generalize the standard Lipschitz smoothness as well as the $(L_{0},L_{1})$-smoothness conditions to the $\ell$-smoothness condition, and develop a new approach for analyzing the convergence under this condition. The approach uses different techniques for several methods and settings to bound the gradient along the optimization trajectory, which allows us to obtain stronger results for both convex and non-convex problems. We obtain the classical rates for GD/SGD/NAG methods in the convex and/or non-convex setting. Our results challenge the folklore belief on the necessity of adaptive methods for generalized smooth functions.

There are several interesting future directions following this work. First, the $\ell$-smoothness can perhaps be further generalized by allowing $\ell$ to also depend on potential functions in each setting, besides the gradient norm. In addition, it would also be interesting to see if the techniques of bounding gradients along the trajectory that we have developed in this and the concurrent work can be further generalized to other methods and problems and to see whether more efficient algorithms can be obtained.
