Super-Universal Regularized Newton Method

Topics include Universal regularized Newton method.

We analyze the performance of a variant of Newton method with quadratic regularization for solving composite convex minimization problems. At each step of our method, we choose regularization parameter proportional to a certain power of the gradient norm at the current point. We introduce a family of problem classes characterized by Hölder continuity of either the second or third derivative. Then we present the method with a simple adaptive search procedure allowing an automatic adjustment to the problem class with the best global complexity bounds, without knowing specific parameters of the problem. In particular, for the class of functions with Lipschitz continuous third derivative, we get the global O(1/k^) rate, which was previously attributed to third-order tensor methods. When the objective function is uniformly convex, we justify an automatic acceleration of our scheme, resulting in a faster global rate and local superlinear convergence. The switching between the different rates (sublinear, linear, and superlinear) is automatic. Again, for that, no a priori knowledge of parameters is needed.

## Motivation

Newton's method is one of the most important tools in Numerical Analysis and Continuous Optimization. It has a reputation for being a powerful algorithm, especially due to its ability to solve ill-conditioned problems. The method has a local quadratic convergence, thus converging extremely fast in a neighbourhood of the solution. However, the global behaviour of Newton's method has been remaining an active area of research for several decades.

Later , adaptive and universal second-order methods based on cubic regularization with an adjustment of the Lipschitz constant were developed. In, it was shown that the adaptive search makes the CNM work properly on functions with Hölder continuous Hessian, automatically achieving the correct global complexity, and in the universality of CNM was studied on uniformly convex functions.

## Discussion

In this paper, we have developed and analyzed the Super-Universal Newton Method based on regularization of the second-order model by the square of Euclidean norm. The regularization parameter is proportional to a power of the gradient norm. Each step of our method is easily computable, employing in the unconstrained case just the standard matrix inversion.

We have proved that using a simple adaptive search procedure in each iteration, the method has a universal global convergence rate among problem classes with Hölder continuous second or third derivatives. If the problem is uniformly convex, the method automatically switches between sublinear, linear, and superlinear rates, adjusting to the best possible problem class.

Another important direction is the creation of methods that are suitable for non-Euclidean geometry. In our method we fix the Euclidean norm as a regularizer, while it is also possible to use for that a contraction of the feasible domain, leading to affine-invariant contracting-point methods, or an appropriate Bregman divergence (see also for the framework of relative smoothness).

For solving large-scale problems, our method can be equipped with modern stochastic techniques which are able to keep versatile convergence guarantees. Another potential way to make the methods more applicable to high-dimensional objectives is to consider quasi-Newton updates, which at the moment seems to be very challenging due to the lack of theoretical results on their global behavior.
