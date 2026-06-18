<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Superfast Second-Order Methods for Unconstrained Convex Optimization

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we present new second-order methods with convergence rate O( k^(-4)) O k - 4, where k is the iteration counter. This is faster than the existing lower bound for this type of schemes (Agarwal and Hazan in Proceedings of the 31st conference on learning theory, PMLR, pp. 774–792, 2018; Arjevani and Shiff in Math Program 178(1–2):327–360, 2019), which is O( k^(-7/2) ) O k - 7 / 2. Our progress can be explained by a finer specification of the problem class. The main idea of this approach consists in implementation of the third-order scheme from Nesterov using the second-order oracle. At each iteration of our method, we solve a nontrivial auxiliary problem by a linearly convergent scheme based on the relative non-degeneracy condition. During this process, the Hessian of the objective function is computed once, and the gradient is computed O( ln 1 over epsilon ) O ln 1 ϵ times, where epsilon ϵ is the desired accuracy of the solution for our problem.
