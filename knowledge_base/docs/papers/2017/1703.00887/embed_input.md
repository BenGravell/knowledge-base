How to Escape Saddle Points Efficiently

Topics include Matrix factorization, Convex optimization, Gradient descent, Deep learning, Optimization, Learning, Saddle point, Stationary point.

This paper shows that a perturbed form of gradient descent converges to a second-order stationary point in a number iterations which depends only poly-logarithmically on dimension (i.e., it is almost "dimension-free"). The convergence rate of this procedure matches the well-known convergence rate of gradient descent to first-order stationary points, up to log factors. When all saddle points are non-degenerate, all second-order stationary points are local minima, and our result thus shows that perturbed gradient descent can escape saddle points almost for free. Our results can be directly applied to many machine learning applications, including deep learning. As a particular concrete example of such an application, we show that our results can be used directly to establish sharp global convergence rates for matrix factorization. Our results rely on a novel characterization of the geometry around saddle points, which may be of independent interest to the non-convex optimization community.

## Introduction

Given a function $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$, gradient descent aims to minimize the function via the following iteration:

where $\eta > 0$ is a step size. Gradient descent and its variants (e.g., stochastic gradient) are widely used in machine learning applications due to their favorable computational properties. This is notably true in the deep learning setting, where gradients can be computed efficiently via back-propagation.

This paper presents the first (nearly) dimension-free result for gradient descent in a general non-convex setting. We present a general convergence result and show how it can be further strengthened when combined with further structure such as strict saddle conditions and/or local regularity/convexity.

There are still many related open problems. First, in the presence of constraints, it is worthwhile to study whether gradient descent still admits similar sharp convergence results. Another important question is whether similar techniques can be applied to accelerated gradient descent. We hope that this result could serve as a first step towards a more general theory with strong, almost dimension free guarantees for non-convex optimization.

### Assumption A1

Under an $\ell$-smoothness assumption, it is well known that by choosing the step size $\eta = \frac{1}{\ell}$, gradient descent converges to first-order stationary points.

The convergence rate in Theorem 3 is polynomial in $\epsilon$, which is similar to that of Theorem 2). ‣ 2.2 Gradient Descent ‣ 2 Preliminaries ‣ How to Escape Saddle Points Efficiently"), but is worse than the rate of Theorem 1 because of the lack of strong convexity. Although global strong convexity does not hold in the non-convex setting that is our focus, in many machine learning problems the objective function may have a favorable local structure in the neighborhood of local minima. Exploiting this property can lead to much faster convergence (linear convergence) to local minima....

Gradient descent is especially useful in high-dimensional settings because the number of iterations required to reach a point with small gradient is independent of the dimension ("dimension-free")....
