<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Optimal Inequalities in Probability Theory: A Convex Optimization Approach

Topics include Moment inequalities, Semidefinite programming, Convex optimization, Probability bounds, Polynomial optimization, Distributionally robust optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Uses semidefinite optimization to derive tight probability bounds from finitely many moments when events and support sets are described by polynomial inequalities. The paper connects classical moment inequalities with convex optimization and characterizes when tight bound computation becomes computationally hard.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a semidefinite optimization approach to the problem of deriving tight moment inequalities for P(X in S), for a set S defined by polynomial inequalities and a random vector X defined on Omega subset R^n that has a given collection of up to kth-order moments. In the univariate case, we provide optimal bounds on P(X in S), when the first k moments of X are given, as the solution of a semidefinite optimization problem in k + 1 dimensions. In the multivariate case, if the sets S and Omega are given by polynomial inequalities, we obtain an improving sequence of bounds by solving semidefinite optimization problems of polynomial size in n, for fixed k. We characterize the complexity of the problem of deriving tight moment inequalities. We show that it is NP-hard to find tight bounds for k >= 4 and Omega = R^n and for k >= 2 and Omega = R^n_+, when the data in the problem is rational.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

For k = 1 and Omega = R^n_+ we show that we can find tight upper bounds by solving n convex optimization problems when the set S is convex, and we provide a polynomial time algorithm when S and Omega are unions of convex sets, over which linear functions can be optimized efficiently. For the case k = 2 and Omega = R^n, we present an efficient algorithm for finding tight bounds when S is a union of convex sets, over which convex quadratic functions can be optimized efficiently.
