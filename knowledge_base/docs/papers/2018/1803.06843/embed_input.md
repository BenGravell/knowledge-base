Linear-time Geometric Algorithm for Evaluating Bézier Curves

Topics include Computational complexity, Control, Bezier curves, Control point.

A new algorithm for computing a point on a polynomial or rational curve in Bézier form is proposed. The method has a geometric interpretation and uses only convex combinations of control points. The new algorithm's computational complexity is linear with respect to the number of control points and its memory complexity is O. Some remarks on similar methods for surfaces in rectangular and triangular Bézier form are also given.

## Introduction

### Remark 1.1

Let us fix $\mathbf{t} \in C$. Suppose that there exists $1 \leq k \leq N$ such that ${b_{k}{(\mathbf{t})}} = 0$. Then one has the division by $0$ in the line 5 of Algorithm 1.1. Such special cases should be considered separately. Observe that it is always possible because at least for one $0 \leq j \leq N$ we have ${b_{j}{(\mathbf{t})}} > 0$ (cf. (1.1)).

Assume $(s,t)$ is on the boundary of the triangle $T$. Then the point $\text{T}_{n}{(s,t)}$ lies on the boundary rational Bézier curve having known control points and weights and, again, one can compute this point using the method presented in Section 2.1.

Let us fix a point $(s,t)$ inside the triangle $T$. Similarly, based on Algorithm 1.1, we introduce the sequences of quantities $g_{ij}$ and points $\text{U}_{ij} \in {\mathbb{E}}^{d}$ $({0 \leq {i + j} \leq n})$, which are computed in the order described above, by the following recurrent formulas:

Note that if all weights $\omega_{k}$ are equal then $\text{Q}_{n} = {\text{P}_{n}{(t)}}$ (cf. (2.1)) --- the new method can also be used to evaluate a polynomial Bézier curve.

$d$ times (once for each dimension). This method has $O{({dn})}$ computational complexity and $O{}$ memory complexity. It uses the concept of Horner's rule (see, e.g., \[2, Eq. (1.2.2)\]).

The numbers of flops for the new algorithms, as well as for de Casteljau algorithms (see Appendix), which also have a geometric interpretation and compute only convex combinations of control points, are given in Table 2.1.

### Theorem 1.2

The quantities $h_{k}$ and $\text{Q}_{k}$ $({0 \leq k \leq N})$ computed by Algorithm 1.1 have the following properties:

### Proof

To end the proof, it is enough to check that:

for $1 \leq k \leq N$ (cf. lines 5, 6 in Algorithm 1.1). ∎

Let us notice that Algorithm 1.1 has a geometric interpretation, uses only convex combinations of control points of $\text{S}_{N}$ and has linear complexity with respect to $N$ --- under the assumption that all quotients of two consecutive basis functions can be computed in the total time $O{(N)}$.

### Remark 1.3

for $1 \leq k \leq N$. Using this simple relation, one can propose a subtraction-free version of Algorithm 1.1. Such formulation can be important for numerical reasons (cf. the problem of cancellation of digits; see, e.g., \[2, §2.3.4\]).
