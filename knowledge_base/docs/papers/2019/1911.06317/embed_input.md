Gradientless Descent: High-Dimensional Zeroth-Order Optimization

Topics include Benchmarks, Optimization, GLD.

Zeroth-order optimization is the process of minimizing an objective f(x), given oracle access to evaluations at adaptively chosen inputs x. In this paper, we present two simple yet powerful GradientLess Descent (GLD) algorithms that do not rely on an underlying gradient estimate and are numerically stable. We analyze our algorithm from a novel geometric perspective and present a novel analysis that shows convergence within an epsilon-ball of the optimum in O(kQlog(n)log(R/epsilon)) evaluations, for any monotone transform of a smooth and strongly convex objective with latent dimension k < n, where the input dimension is n, R is the diameter of the input space and Q is the condition number. Our rates are the first of its kind to be both 1) poly-logarithmically dependent on dimensionality and 2) invariant under monotone transformations. We further leverage our geometric perspective to show that our analysis is optimal. Both monotone invariance and its ability to utilize a low latent dimensionality are key to the empirical success of our algorithms, as demonstrated on BBOB and MuJoCo benchmarks.

## Introduction

We consider the problem of zeroth-order optimization (also known as gradient-free optimization, or bandit optimization), where our goal is to minimize an objective function $f:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}}$ with as few evaluations of $f{(x)}$ as possible. For many practical and interesting objective functions, gradients are difficult to compute and there is still a need for zeroth-order optimization in applications such as reinforcement learning \[, SHC^+^17, CRS^+^18\], attacking neural networks \[CZS^+^17, PMG^+^17\], hyperparameter tuning of deep networks \[\], and network control \[\].\
The standard approach to...

### Our contributions

## Conclusion

We introduced GLD, a robust zeroth-order optimization algorithm that is simple, efficient, and we show strong theoretical convergence bounds via our novel geometric analysis. As demonstrated by our experiments on BBOB and MuJoCo benchmarks, GLD performs very robustly even in the non-convex setting and its monotone and affine invariance properties give theoretical insight on its practical efficiency.\
GLD is very flexible and allows easy modifications....

### Theorem 10

The GLD template can be summarized as follows: given a sampling distribution $\mathcal{D}$, we start at $x_{0}$ and in iteration $t$, we choose a scalar radii $r_{t}$ and we sample $y_{t}$ from a distribution $r_{t}\mathcal{D}$ centered around $x_{t}$, where $r_{t}$ provides the scaling of $\mathcal{D}$. Then, if ${f{(x_{t + 1})}} < x_{t}$, we update $x_{t + 1} = y_{t}$; otherwise, we set $x_{t + 1} = x_{t}$....

Although the sampling distribution $\mathcal{D}$ is fixed, we have a choice of radii for each iteration of the algorithm. We can apply a binary search procedure to ensure progress. The most straightforward version of our algorithm is thus with a naive binary sweep across an interval in $\lbrack r,R\rbrack$ that is unchanged throughout the algorithm. This allows us to give convergence guarantees without previous knowledge of the condition number at a cost of an extra factor of $\log{({n/\epsilon})}$.

In this paper, we present GradientLess Descent (GLD), a class of truly gradient-free algorithms (also known as direct search algorithms) that are parameter free and provably fast....
