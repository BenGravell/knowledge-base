Gradient Descent Converges to Minimizers

Topics include Gradient descent.

We show that gradient descent converges to a local minimizer, almost surely with random initialization. This is proved by applying the Stable Manifold Theorem from dynamical systems theory.

## Introduction

Saddle points have long been regarded as a tremendous obstacle for continuous optimization. There are many well known examples when worst case initialization of gradient descent provably converge to saddle points \[20, Section 1.2.3\], and hardness results which show that finding even a *local* minimizer of non-convex functions is NP-Hard in the worst case. However, such worst-case analyses have not daunted practitioners, and high quality solutions of continuous optimization problems are readily found by a variety of simple algorithms.

More

We call $x$ a critical point of $f$ if ${{\nabla f}{(x)}} = 0$, and say that $f$ satisfies the strict saddle property if each critical point $x$ of $f$ is either a local minimizer, or a "strict saddle", i.e, ${\nabla^{2}f}{(x)}$ has at least one strictly negative eigenvalue.

> If $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ is twice continuously differentiable and satisfies the strict saddle property, then gradient descent (Equation 1) with a random initialization and sufficiently small constant step size converges to a local minimizer or negative infinity almost surely.

## Conclusion

We have shown that gradient descent with random initialization and appropriate constant step size does not converge to a saddle point. Our analysis relies on a characterization of the local stable set from the theory of invariant manifolds. The geometric characterization is not specific to the gradient descent algorithm. To use Theorem 4.1, we simply need the update step of the algorithm to be a diffeomorphism. For example if $g$ is the mapping induced by the proximal point algorithm, then $g$ is a diffeomorphism with inverse given by gradient ascent on $- f$. Thus the results in Section 4 also apply to the proximal point algorithm.

It is not clear if the step size restriction ($\alpha < {1/L}$) is necessary to avoid saddle points. Most of the constructions where the gradient method converges to saddle points require fragile initial conditions as discussed in Section 3. It remains a possibility that methods that choose step sizes greedily, by Wolfe Line Search or backtracking, may still avoid saddle points provided the initial point is chosen at random. We leave such investigations for future work.
