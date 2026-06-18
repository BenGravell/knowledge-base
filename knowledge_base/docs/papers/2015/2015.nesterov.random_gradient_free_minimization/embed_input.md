<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Random Gradient-Free Minimization of Convex Functions

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we prove new complexity bounds for methods of convex optimization based only on computation of the function value. The search directions of our schemes are normally distributed random Gaussian vectors. It appears that such methods usually need at most n times more iterations than the standard gradient methods, where n is the dimension of the space of variables. This conclusion is true for both nonsmooth and smooth problems. For the latter class, we present also an accelerated scheme with the expected rate of convergence O(n^2/k^2), where k is the iteration counter. For stochastic optimization, we propose a zero-order scheme and justify its expected rate of convergence O(n/sqrt(k)). We give also some bounds for the rate of convergence of the random gradient-free methods to stationary points of nonconvex functions, for both smooth and nonsmooth cases. Our theoretical results are supported by preliminary computational experiments.
