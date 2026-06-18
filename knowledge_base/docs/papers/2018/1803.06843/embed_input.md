<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Linear-time Geometric Algorithm for Evaluating Bézier Curves

Topics include Computational complexity, Control, Bezier curves, Control point.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A new algorithm for computing a point on a polynomial or rational curve in Bézier form is proposed. The method has a geometric interpretation and uses only convex combinations of control points. The new algorithm's computational complexity is linear with respect to the number of control points and its memory complexity is O. Some remarks on similar methods for surfaces in rectangular and triangular Bézier form are also given.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Remark 1.1", "weight": 1.0} -->

Let us fix $\mathbf{t} \in C$. Suppose that there exists $1 \leq k \leq N$ such that ${b_{k}{(\mathbf{t})}} = 0$. Then one has the division by $0$ in the line 5 of Algorithm 1.1. Such special cases should be considered separately. Observe that it is always possible because at least for one $0 \leq j \leq N$ we have ${b_{j}{(\mathbf{t})}} > 0$ (cf. (1.1)).

<!-- chunk {"id": "body-0004", "role": "body", "section": "Remark 1.3", "weight": 1.0} -->

for $1 \leq k \leq N$. Using this simple relation, one can propose a subtraction-free version of Algorithm 1.1. Such formulation can be important for numerical reasons (cf. the problem of cancellation of digits; see, e.g., \[2, §2.3.4\]).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Remark 1.3", "weight": 1.0} -->

We use relation (1.3) in the proof of the following theorem which shows an important property of Algorithm 1.1.

<!-- chunk {"id": "body-0006", "role": "body", "section": "New algorithm for evaluating Bézier curves", "weight": 1.0} -->

where $B_{k}^{n}$ is the $k$th Bernstein polynomial of degree $n$,

<!-- chunk {"id": "body-0007", "role": "body", "section": "New algorithm for evaluating Bézier curves", "weight": 1.0} -->

For a given $t \in {\lbrack 0,1\rbrack}$, the point ${\text{P}_{n}{(t)}} \in {\mathbb{E}}^{d}$ can be computed by famous the de Casteljau algorithm (see, e.g., \[3, §4.2\] and Appendix), which has good numerical properties, a simple geometric interpretation and computes only convex combinations of control points $\text{W}_{k}$ $({0 \leq k \leq n})$. However, the computational complexity of this method is $O{({dn^{2}})}$, which makes it quite expensive.

<!-- chunk {"id": "body-0008", "role": "body", "section": "New algorithm for evaluating Bézier curves", "weight": 1.0} -->

Probably, the fastest way to compute the coordinates of the point ${\text{P}_{n}{(t)}} \in {\mathbb{E}}^{d}$ is to use the algorithm proposed in for evaluating a polynomial $p$ given in the form

<!-- chunk {"id": "body-0009", "role": "body", "section": "New algorithm for evaluating Bézier curves", "weight": 1.0} -->

$d$ times (once for each dimension). This method has $O{({dn})}$ computational complexity and $O{}$ memory complexity. It uses the concept of Horner's rule (see, e.g., \[2, Eq. (1.2.2)\]).

<!-- chunk {"id": "body-0010", "role": "body", "section": "New algorithm for evaluating Bézier curves", "weight": 1.0} -->

Note that some other methods for evaluating a Bézier curve are also known. See, e.g., or, where the case of Bézier surfaces was also studied (cf. Section 3), and papers cited therein.

<!-- chunk {"id": "body-0011", "role": "body", "section": "New algorithm for evaluating Bézier curves", "weight": 1.0} -->

with the weights ${\omega_{0},\omega_{1},\ldots,\omega_{n}} \in {\mathbb{R}}_{+}$. To compute the point ${\text{R}_{n}{(t)}} \in {\mathbb{E}}^{d}$ for a given $t \in {\lbrack 0,1\rbrack}$, one can use the rational de Casteljau algorithm (see, e.g., \[3, §13.2\] and Appendix), which also has $O{({dn^{2}})}$ computational complexity, good numerical properties, a geometric interpretation and computes only convex combinations of the control points $\text{W}_{k}$ $({0 \leq k \leq n})$, or use the idea, which leads to linear-time method at the cost of losing some geometric properties.

<!-- chunk {"id": "body-0012", "role": "body", "section": "New algorithm for evaluating Bézier curves", "weight": 1.0} -->

The main purpose of this section is to propose a new efficient method for computing a point on a Bézier curve and on a rational Bézier curve.

<!-- chunk {"id": "body-0013", "role": "body", "section": "New algorithm for evaluating Bézier curves", "weight": 1.0} -->

quite good numerical properties, i.e., they are safe for floating-point computations,

<!-- chunk {"id": "body-0014", "role": "body", "section": "New algorithm for evaluating Bézier curves", "weight": 1.0} -->

linear computational complexity, i.e., $O{({dn})}$, and $O{}$ memory complexity,

<!-- chunk {"id": "body-0015", "role": "body", "section": "New algorithm for evaluating Bézier curves", "weight": 1.0} -->

As we show later, the new method combines the advantages of de Casteljau algorithms and the low complexity of methods based.

<!-- chunk {"id": "body-0016", "role": "body", "section": "New method", "weight": 1.0} -->

Let the quantities $h_{k}$ and $\text{Q}_{k}$ $({0 \leq k \leq n})$ be computed recursively by formulas

<!-- chunk {"id": "body-0017", "role": "body", "section": "Implementation and cost", "weight": 1.0} -->

Let us give efficient and numerically safe implementations of the new method which have $O{({dn})}$ computational complexity and $O{}$ memory complexity.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Implementation and cost", "weight": 1.0} -->

The implementation provided in Algorithm 2.1 requires ${{({{3d} + 8})}n} + 1$ floating-point arithmetic operations (flops) to compute a point on a rational Bézier curve of degree $n$ in ${\mathbb{E}}^{d}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Implementation and cost", "weight": 1.0} -->

Algorithm 2.2 decreases the number of flops to ${{({{3d} + 7})}n} + 2$. However, for numerical reasons (cf. lines 7 and 15 in Algorithm 2.2), it is necessary to use a conditional statement. More precisely, one has to check whether $t \in {\lbrack 0,0.5\rbrack}$ or $t \in {(0.5,1\rbrack}$, which can be easily done (it is enough to check an exponent of a floating-point number $t$).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Implementation and cost", "weight": 1.0} -->

Note that in the case of polynomial Bézier curves (2.1), one only needs to set $\omega_{k}:=1$ $({0 \leq k \leq n})$ in the given algorithms, thus simplifying used formulas. Then the number of flops is equal to ${{({{3d} + 6})}n} + 1$ in Algorithm 2.1 and ${{({{3d} + 5})}n} + 2$ in Algorithm 2.2.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Implementation and cost", "weight": 1.0} -->

The numbers of flops for the new algorithms, as well as for de Casteljau algorithms (see Appendix), which also have a geometric interpretation and compute only convex combinations of control points, are given in Table 2.1.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Example 2.3", "weight": 1.0} -->

Table 2.2 shows the comparison between the running times of de Casteljau algorithm and Algorithm 2.2 both for Bézier curves and rational Bézier curves (in the case of Bézier curves, Algorithm 2.2 has been simplified), for $d \in {\{ 2,3\}}$. The results have been obtained on a computer with Intel Core i5-2540M CPU at 2.60GHz processor and 4GB RAM, using GNU C Compiler 7.4.0 (single precision).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Example 2.3", "weight": 1.0} -->

More precisely, we made the following numerical experiments. For a fixed $n$, $10000$ curves of degree $n$ are generated. Their control points $\text{W}_{k} \in {\lbrack{- 1},1\rbrack}^{d}$ and---in the rational case---weights $\omega_{k} \in {\lbrack 0.01,1\rbrack}$ $({0 \leq k \leq n})$ have been generated using the rand C function. Each curve is then evaluated at 501 points $t_{i}:={i/500}$ $({0 \leq i \leq 500})$. Each algorithm is tested using the same curves. Table 2.2 shows the total running time of all $501 \times 10000$ evaluations.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example 2.3", "weight": 1.0} -->

new method (cf. Alg. 2.2)
new method (cf. Alg. 2.2)

<!-- chunk {"id": "body-0025", "role": "body", "section": "Example 2.3", "weight": 1.0} -->

Table 2.2: Running times comparison (in seconds) for Example 2.3. The source code in C which was used to perform the tests is available at

<!-- chunk {"id": "body-0026", "role": "body", "section": "Example 2.3", "weight": 1.0} -->

Observe that in the case of Bézier curves, the quantities $h$, which are computed in the new algorithms, do not depend on the control points. One can use this fact in the fast evaluation of $M$ Bézier curves of the same degree $n$ for the same value of the parameter $t$. Such a method requires ${{({{3dM} + 5})}n} + 2$ flops while the direct use of the de Casteljau algorithm means that all computations have to be repeated $M$ times, i.e., the number of flops is equal to ${{3Mdn{({n + 1})}}/2} + 1$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 2.4", "weight": 1.0} -->

In rather rare cases $({h_{k} \approx 1})$, the problem of cancellation of digits (\[2, §2.3.4\]) can occur while $1 - h_{k}$ is computed (cf. $h_{1}$ in Algorithms 2.1, 2.2). One can avoid this problem using the relation

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 2.4", "weight": 1.0} -->

if computations with high accuracy are necessary.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remarks on evaluation of Bézier surfaces", "weight": 1.0} -->

The method of evaluation described in Section 1 can also be applied to the rational rectangular and triangular Bézier surfaces.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remarks on evaluation of Bézier surfaces", "weight": 1.0} -->

Both surface types are, in fact, rational parametric objects (cf. (1.2)). Thus, one can apply Algorithm 1.1 to propose the methods which have geometric interpretations, compute only convex combinations of points and allow to evaluate Bézier surfaces in linear time with respect to the number of control points, i.e., $O{({nm})}$ in the rectangular case and $O{(n^{2})}$ in the triangular case. To do so, it is necessary to rearrange the sets of control points, corresponding weights and basis functions (cf. (1.1)) into one-dimensional sequences --- but since the method is agnostic of the ordering, the chosen ordering is only a matter of preference. Taking into account that the computations can be performed in many ways, we do not present rigorous algorithms and we pass some technical details.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remarks on evaluation of Bézier surfaces", "weight": 1.0} -->

In this section, to present a concise formulation of the methods, we choose the row-by-row order. For the reader's convenience, the analogues of quantities $h_{k}$ and points $\text{Q}_{k}$ from Algorithm 1.1 have two indices instead, to correspond with the surfaces' structure.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Rational rectangular Bézier surfaces", "weight": 1.0} -->

In this case, one can interpret the set of control points as a rectangular grid having $m + 1$ rows with $n + 1$ points in each row.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Rational rectangular Bézier surfaces", "weight": 1.0} -->

the sequence begins with $\text{W}_{00}$,

<!-- chunk {"id": "body-0034", "role": "body", "section": "Rational rectangular Bézier surfaces", "weight": 1.0} -->

It is well-known that if $(s,t)$ belongs to the boundary of the square ${\lbrack 0,1\rbrack}^{2}$ then the point $\text{S}_{mn}{(s,t)}$ lies on the boundary rational Bézier curve with boundary control points and weights. Thus, the method described in Section 2.1 can be used in this case.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Rational rectangular Bézier surfaces", "weight": 1.0} -->

Let us fix ${(s,t)} \in {}^{2}$. Now, based on Algorithm 1.1,

<!-- chunk {"id": "body-0036", "role": "body", "section": "Rational triangular Bézier surfaces", "weight": 1.0} -->

The method described below is analogous to the one for rectangular Bézier surfaces. The main difference is that, in this case, the set of the control points can be seen as a triangular grid, i.e., the number of control points in each row depends on the row number. Namely, there are ${n - i} + 1$ points in the $i$th row $({0 \leq i \leq n})$ of this triangular grid.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Rational triangular Bézier surfaces", "weight": 1.0} -->

the sequence begins with $\text{V}_{00}$,

<!-- chunk {"id": "body-0038", "role": "body", "section": "Rational triangular Bézier surfaces", "weight": 1.0} -->

We set the sequences of weights $v_{ij}$ and basis functions $B_{ij}^{n}{(s,t)}$ $({0 \leq {i + j} \leq n})$ in the same way.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Rational triangular Bézier surfaces", "weight": 1.0} -->

Assume $(s,t)$ is on the boundary of the triangle $T$. Then the point $\text{T}_{n}{(s,t)}$ lies on the boundary rational Bézier curve having known control points and weights and, again, one can compute this point using the method presented in Section 2.1.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Rational triangular Bézier surfaces", "weight": 1.0} -->

Let us fix a point $(s,t)$ inside the triangle $T$. Similarly, based on Algorithm 1.1,
