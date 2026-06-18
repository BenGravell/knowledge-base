How to Escape Saddle Points Efficiently

Topics include Matrix factorization, Convex optimization, Gradient descent, Deep learning, Optimization, Learning, Saddle point, Stationary point.

This paper shows that a perturbed form of gradient descent converges to a second-order stationary point in a number iterations which depends only poly-logarithmically on dimension (i.e., it is almost "dimension-free"). The convergence rate of this procedure matches the well-known convergence rate of gradient descent to first-order stationary points, up to log factors. When all saddle points are non-degenerate, all second-order stationary points are local minima, and our result thus shows that perturbed gradient descent can escape saddle points almost for free. Our results can be directly applied to many machine learning applications, including deep learning. As a particular concrete example of such an application, we show that our results can be used directly to establish sharp global convergence rates for matrix factorization. Our results rely on a novel characterization of the geometry around saddle points, which may be of independent interest to the non-convex optimization community.

## Introduction

Given

where $\eta > 0$ is a step size. Gradient descent and its variants (e.g., stochastic gradient) are widely used in machine learning applications due to their favorable computational properties. This is notably true in the deep learning setting, where gradients can be computed efficiently via back-propagation.

In non-convex settings, however, convergence to first-order stationary points is not satisfactory. For non-convex functions, first-order stationary points can be global minima, local minima, saddle points or even local maxima. Finding a global minimum can be hard, but fortunately, for many non-convex problems, it is sufficient to find a local minimum. Indeed, a line of recent results show that, in many problems of interest, either all local minima are global minima (e.g., in tensor decomposition, dictionary learning, phase retrieval, matrix sensing, matrix completion, and certain classes of deep neural networks ).

Though these results establish that gradient descent can find local minima in a polynomial number of iterations, they are still far from being efficient. For instance, the number of iterations required in Ge et al. is at least $\Omega{(d^{4})}$, where $d$ is the underlying dimension. This is significantly suboptimal compared to rates of convergence to first-order stationary points, where the iteration complexity is dimension-free. This motivates the following question: Can gradient descent escape saddle points and converge to local minima in a number of iterations that is (almost) dimension-free?

## Conclusion

This paper presents the first (nearly) dimension-free result for gradient descent in a general non-convex setting. We present a general convergence result and show how it can be further strengthened when combined with further structure such as strict saddle conditions and/or local regularity/convexity.

There are still many related open problems. First, in the presence of constraints, it is worthwhile to study whether gradient descent still admits similar sharp convergence results. Another important question is whether similar techniques can be applied to accelerated gradient descent. We hope that this result could serve as a first step towards a more general theory with strong, almost dimension free guarantees for non-convex optimization.
