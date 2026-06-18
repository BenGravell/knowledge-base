Linear-time Geometric Algorithm for Evaluating Bézier Curves

Topics include Computational complexity, Control, Bezier curves, Control point.

A new algorithm for computing a point on a polynomial or rational curve in Bézier form is proposed. The method has a geometric interpretation and uses only convex combinations of control points. The new algorithm's computational complexity is linear with respect to the number of control points and its memory complexity is O. Some remarks on similar methods for surfaces in rectangular and triangular Bézier form are also given.

## Remark 1.1

Let us fix $\mathbf{t} \in C$. Suppose that there exists $1 \leq k \leq N$ such that ${b_{k}{(\mathbf{t})}} = 0$. Then one has the division by $0$ in the line 5 of Algorithm 1.1. Such special cases should be considered separately. Observe that it is always possible because at least for one $0 \leq j \leq N$ we have ${b_{j}{(\mathbf{t})}} > 0$ (cf. (1.1)).

## Remark 1.3

for $1 \leq k \leq N$. Using this simple relation, one can propose a subtraction-free version of Algorithm 1.1. Such formulation can be important for numerical reasons (cf. the problem of cancellation of digits; see, e.g., \[2, §2.3.4\]).

We use relation (1.3) in the proof of the following theorem which shows an important property of Algorithm 1.1.

## New algorithm for evaluating Bézier curves

where $B_{k}^{n}$ is the $k$th Bernstein polynomial of degree $n$,
