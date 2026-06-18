Improved Nonnegativity Testing in the Bernstein Basis via Geometric Means

Topics include Optimization and control.

We develop a new kind of nonnegativity certificate for univariate polynomials on an interval. In many applications, nonnegative Bernstein coefficients are often used as a simple way of certifying polynomial nonnegativity. Our proposed condition is instead an explicit lower bound for each Bernstein coefficient in terms of the geometric mean of its adjacent coefficients, which is provably less restrictive than the usual test based on nonnegative coefficients. We generalize to matrix-valued polynomials of arbitrary degree, and we provide numerical experiments suggesting the practical benefits of this condition. The techniques for constructing this inexpensive certificate could potentially be applied to other semialgebraic feasibility problems.

## Introduction

The cubic Bernstein polynomials (e.g., ) are

Suppose we have a polynomial $p{(x)}$ such that

We would like to find explicit conditions on the real numbers $p_{0},p_{1},p_{2},p_{3}$ (called Bernstein coefficients) that guarantee ${p{(x)}} \geq 0$ on $\lbrack 0,1\rbrack$. This task and its higher degree variants discussed in Section 4 are central questions in applied mathematics. Research on nonnegativity certificates of different kinds is a classical topic in real algebraic geometry, including well-known work by Sturm, Hilbert, Artin, and others; see e.g. and the references therein.

Exact characterizations: The Markov--Lukács Theorem (\[44, p. 4\]) gives a necessary and sufficient condition for nonnegativity on an interval. It states that a polynomial $p$ is nonnegative on $\lbrack 0,1\rbrack$ if and only if there exist polynomials $s_{1}$ and $s_{2}$ such that

## Conclusion

We developed novel simple and explicit conditions to certify nonnegativity of Bernstein polynomials. The new tests better balance the tradeoffs between exact but expensive conditions, and the commonly used test based on nonnegative Bernstein coefficients. The method is based on making explicit choices for the decision variables in the SDP/SOCP characterizations of nonnegativity, bypassing the need to solve them numerically.

There are several related open areas for potential further work. An open question is whether there are other reasonable low-complexity choices for the decision variables (that may violate the hypotheses of Proposition 3.2 or that may not satisfy the conditions of Theorem 3.2). Generalizing the basic idea of Proposition 3.2 to higher degrees and the polynomial matrix case is also future work. Finally, it would be interesting to do a more comprehensive evaluation of how well these techniques perform in different applied settings.
