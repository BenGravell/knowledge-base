Gradientless Descent: High-Dimensional Zeroth-Order Optimization

Topics include Benchmarks, Optimization, GLD.

Zeroth-order optimization is the process of minimizing an objective f(x), given oracle access to evaluations at adaptively chosen inputs x. In this paper, we present two simple yet powerful GradientLess Descent (GLD) algorithms that do not rely on an underlying gradient estimate and are numerically stable. We analyze our algorithm from a novel geometric perspective and present a novel analysis that shows convergence within an epsilon-ball of the optimum in O(kQlog(n)log(R/epsilon)) evaluations, for any monotone transform of a smooth and strongly convex objective with latent dimension k < n, where the input dimension is n, R is the diameter of the input space and Q is the condition number. Our rates are the first of its kind to be both 1) poly-logarithmically dependent on dimensionality and 2) invariant under monotone transformations. We further leverage our geometric perspective to show that our analysis is optimal. Both monotone invariance and its ability to utilize a low latent dimensionality are key to the empirical success of our algorithms, as demonstrated on BBOB and MuJoCo benchmarks.

## Introduction

We consider the problem of zeroth-order optimization (also known as gradient-free optimization, or bandit optimization), where our goal is to minimize an objective function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ with as few evaluations of $f{(x)}$ as possible.

## Our contributions

In this paper, we present GradientLess Descent (GLD), a class of truly gradient-free algorithms (also known as direct search algorithms) that are parameter free and provably fast. Our algorithms are based on a simple intuition: for well-conditioned functions, if we start from a point and take a small step in a randomly chosen direction, there is a significant probability that we will reduce the objective function value. We present a novel analysis that relies on facts in high dimensional geometry and can thus be viewed as a geometric analysis of gradient-free algorithms, recovering the standard convergence rates and step sizes.

## Analysis of Descent Steps

The GLD template can be summarized as follows: given a sampling distribution $\mathcal{D}$, we start at $x_{0}$ and in iteration $t$, we choose a scalar radii $r_{t}$ and we sample $y_{t}$ from a distribution $r_{t}\mathcal{D}$ centered around $x_{t}$, where $r_{t}$ provides the scaling of $\mathcal{D}$. Then, if ${f{(x_{t + 1})}} < x_{t}$, we update $x_{t + 1} = y_{t}$; otherwise, we set $x_{t + 1} = x_{t}$. The analysis of GLD follows from the main observation that the sub-level set of a monotone transformation of a strongly convex and strongly smooth function contains a ball of sufficiently large radius tangent to the level set (Lemma 15).

## Conclusion

We introduced GLD, a robust zeroth-order optimization algorithm that is simple, efficient, and we show strong theoretical convergence bounds via our novel geometric analysis. As demonstrated by our experiments on BBOB and MuJoCo benchmarks, GLD performs very robustly even in the non-convex setting and its monotone and affine invariance properties give theoretical insight on its practical efficiency.\
GLD is very flexible and allows easy modifications. For example, it could use momentum terms to keep moving in the same direction that improved the objective, or sample from adaptively chosen ellipsoids similarly to adaptive gradient methods..
