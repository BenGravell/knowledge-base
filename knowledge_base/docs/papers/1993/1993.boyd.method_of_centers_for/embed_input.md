<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Method of Centers for Minimizing Generalized Eigenvalues

Topics include Convex optimization, Generalized eigenvalues, Interior-point methods, Semidefinite programming, Matrix inequalities, Self-concordant barriers, Control theory.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Applies a method-of-centers interior-point approach to minimizing the largest generalized eigenvalue of affine symmetric matrix pencils. The paper connects quasiconvex generalized-eigenvalue optimization with matrix inequalities, stopping criteria, and control applications such as Lyapunov decay-rate estimates.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider the problem of minimizing the largest generalized eigenvalue of a pair of symmetric matrices, each of which depends affinely on the decision variables. Although this problem may appear specialized, it is in fact quite general, and includes for example all linear, quadratic, and linear fractional programs. Many problems arising in control theory can be cast in this form. The problem is nondifferentiable but quasiconvex, so methods such as Kelley's cutting-plane algorithm or the ellipsoid algorithm of Shor, Nemirovksy, and Yudin are guaranteed to minimize it. In this paper we describe relevant background material and a simple interior point method that solves such problems more efficiently. The algorithm is a variation on Huard's method of centers, using a self-concordant barrier for matrix inequalities developed by Nesterov and Nemirovsky. Since the problem is quasiconvex but not convex, devising a non-heuristic stopping criterion, i.e., one that guarantees a given accuracy, is more difficult than in the convex case.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We describe several non-heuristic stopping criteria that are based on the dual of a related convex problem and a new ellipsoidal approximation that is slightly sharper, in some cases, than a more general result due to Nesterov and Nemirovsky. The algorithm is demonstrated on an example: determining the quadratic Lyapunov function that optimizes a decay rate estimate for a differential inclusion.
