## Introduction

Let $b_{k}:{D\rightarrow{\mathbb{R}}}$ $({{k = {0,1,\ldots,N}};{N \in {\mathbb{N}}}})$ be real-valued multivariable functions such that

for ${\mathbf{t}} \in C \subseteq D$.

Let us define the rational parametric object $\text{S}_{N}:{C\rightarrow{\mathbb{E}}^{d}}$ $({d \in {\mathbb{N}}})$ by

with the weights $\omega_{k} > 0$, and control points $\text{W}_{k} \in {\mathbb{E}}^{d}$ $({0 \leq k \leq N})$. If $\omega_{0} = \omega_{1} = \ldots = \omega_{N}$, then

In the sequel, we prove that for a given ${\mathbf{t}} \in C$, the point ${\text{S}_{N}{({\mathbf{t}})}} \in {\mathbb{E}}^{d}$ can be computed by Algorithm 1.1.

5: $h_{k}\leftarrow\left( {1 + \frac{\omega_{k - 1}b_{k - 1}({\mathbf{t}})}{h_{k - 1}\omega_{k}b_{k}({\mathbf{t}})}} \right)^{- 1}$

### Remark 1.1

Let us fix $\mathbf{t} \in C$. Suppose that there exists $1 \leq k \leq N$ such that ${b_{k}{(\mathbf{t})}} = 0$. Then one has the division by $0$ in the line 5 of Algorithm 1.1. Such special cases should be considered separately. Observe that it is always possible because at least for one $0 \leq j \leq N$ we have ${b_{j}{(\mathbf{t})}} > 0$ (cf. (1.1)).

### Theorem 1.2

The quantities $h_{k}$ and $\text{Q}_{k}$ $({0 \leq k \leq N})$ computed by Algorithm 1.1 have the following properties:

$\text{Q}_{k} \in C_{k} \equiv {\text{conv}{\{\text{W}_{0},\text{W}_{1},\ldots,\text{W}_{k}\}}}$ (i.e., ${\text{conv}{\{\text{Q}_{0},\text{Q}_{1},\ldots,\text{Q}_{k}\}}} \subseteq C_{k}$).

Moreover, ${\text{S}_{N}{(\mathbf{t})}} = \text{Q}_{N}$.

### Proof

It is clear that $h_{k} \in {\lbrack 0,1\rbrack}$, $\text{Q}_{k} \in {\mathbb{E}}^{d}$ for $0 \leq k \leq N$, $h_{0} = 1$, $\text{W}_{0} = \text{Q}_{0}$, and ${\text{S}_{N}{({\mathbf{t}})}} = \text{Q}_{N}$. Certainly,

To end the proof, it is enough to check that:

for $1 \leq k \leq N$ (cf. lines 5, 6 in Algorithm 1.1). ∎

Let us notice that Algorithm 1.1 has a geometric interpretation, uses only convex combinations of control points of $\text{S}_{N}$ and has linear complexity with respect to $N$ --- under the assumption that all quotients of two consecutive basis functions can be computed in the total time $O{(N)}$.

### Remark 1.3

It may be worth mentioning that

for $1 \leq k \leq N$. Using this simple relation, one can propose a subtraction-free version of Algorithm 1.1. Such formulation can be important for numerical reasons (cf. the problem of cancellation of digits; see, e.g., \[2, §2.3.4\]).

We use relation (1.3) in the proof of the following theorem which shows an important property of Algorithm 1.1.

### Theorem 1.4

Let us fix ${\mathbf{t},\mathbf{u}} \in C$. Assume that the numbers $h_{k}$ $({1 \leq k \leq N})$ computed by Algorithm 1.1 are non-zero. Suppose that

Then the point ${\text{S}_{N}{(\mathbf{u})}} \in {\mathbb{E}}^{d}$ is in the convex hull of the points $\text{Q}_{0},\text{Q}_{1},\ldots,\text{Q}_{N}$ computed by Algorithm 1.1.

### Proof

Let the numbers $h_{k}$ and the points $\text{Q}_{k}$ $({0 \leq k \leq N})$ be computed by Algorithm 1.1 for a fixed ${\mathbf{t}} \in C$.

Using relation (1.3) and the assumption that $h_{k} \neq 0$ $({1 \leq k \leq N})$, observe that

for $1 \leq k \leq N$. Thus, after simple algebra, we obtain

where ${D_{N}{({\mathbf{u}})}}:={\sum_{k = 0}^{N}{\omega_{k}b_{k}{({\mathbf{u}})}}} > 0$.

Now, from our assumptions, it easily follows that the point $\text{S}_{N}{({\mathbf{u}})}$ belongs to the set $\text{conv}{\{\text{Q}_{0},\text{Q}_{1},\ldots,\text{Q}_{N}\}}$, because the $h_{k}$ $({0 \leq k \leq N})$ are positive (cf. Theorem 1.2). ∎

The main aim of this article is to use the presented results to propose a new method for evaluating a polynomial or rational Bézier curve, which has a geometric interpretation, linear complexity with respect to the number of control points, good numerical properties and computes only convex combinations of points from ${\mathbb{E}}^{d}$. See Section 2.

A similar approach can also be used for the evaluation of polynomial and rational tensorproduct, as well as triangular, Bézier surfaces. Some remarks on this issue are given, without technical details and rigorous algorithms, in Section 3.

## New algorithm for evaluating Bézier curves

Let there be given points ${\text{W}_{0},\text{W}_{1},\ldots,\text{W}_{n}} \in {\mathbb{E}}^{d}$ $({{n,d} \in {\mathbb{N}}})$. Let us consider the (polynomial) Bézier curve of the form

where $B_{k}^{n}$ is the $k$th Bernstein polynomial of degree $n$,

For a given $t \in {\lbrack 0,1\rbrack}$, the point ${\text{P}_{n}{(t)}} \in {\mathbb{E}}^{d}$ can be computed by famous the de Casteljau algorithm (see, e.g., \[3, §4.2\] and Appendix), which has good numerical properties, a simple geometric interpretation and computes only convex combinations of control points $\text{W}_{k}$ $({0 \leq k \leq n})$. However, the computational complexity of this method is $O{({dn^{2}})}$, which makes it quite expensive.

Probably, the fastest way to compute the coordinates of the point ${\text{P}_{n}{(t)}} \in {\mathbb{E}}^{d}$ is to use the algorithm proposed in for evaluating a polynomial $p$ given in the form

$d$ times (once for each dimension). This method has $O{({dn})}$ computational complexity and $O{}$ memory complexity. It uses the concept of Horner's rule (see, e.g., \[2, Eq. (1.2.2)\]).

Note that some other methods for evaluating a Bézier curve are also known. See, e.g., or, where the case of Bézier surfaces was also studied (cf. Section 3), and papers cited therein.

Let $\text{R}_{n}$ be a rational Bézier curve in ${\mathbb{E}}^{d}$,

with the weights ${\omega_{0},\omega_{1},\ldots,\omega_{n}} \in {\mathbb{R}}_{+}$. To compute the point ${\text{R}_{n}{(t)}} \in {\mathbb{E}}^{d}$ for a given $t \in {\lbrack 0,1\rbrack}$, one can use the rational de Casteljau algorithm (see, e.g., \[3, §13.2\] and Appendix), which also has $O{({dn^{2}})}$ computational complexity, good numerical properties, a geometric interpretation and computes only convex combinations of the control points $\text{W}_{k}$ $({0 \leq k \leq n})$, or use the idea from, which leads to linear-time method at the cost of losing some geometric properties.

The main purpose of this section is to propose a new efficient method for computing a point on a Bézier curve and on a rational Bézier curve. The given algorithm has:

quite good numerical properties, i.e., they are safe for floating-point computations,

linear computational complexity, i.e., $O{({dn})}$, and $O{}$ memory complexity,

and computes only

convex combinations of control points.

As we show later, the new method combines the advantages of de Casteljau algorithms and the low complexity of methods based on.

### New method

Let $\text{R}_{n}$ be the rational Bézier curve (2.3). Let us fix: a parameter $t \in {\lbrack 0,1\rbrack}$, a natural number $n$, weights ${\omega_{0},\omega_{1},\ldots,\omega_{n}} > 0$ and control points ${\text{W}_{0},\text{W}_{1},\ldots,\text{W}_{n}} \in {\mathbb{E}}^{d}$ $({d \in {\mathbb{N}}})$.

Let the quantities $h_{k}$ and $\text{Q}_{k}$ $({0 \leq k \leq n})$ be computed recursively by formulas

### Theorem 2.1

For all $k = {0,1,\ldots,n}$, the quantities $h_{k}$ and $\text{Q}_{k}$ satisfy:

$\text{Q}_{k} \in C_{k} \equiv {\text{conv}{\{\text{W}_{0},\text{W}_{1},\ldots,\text{W}_{k}\}}}$ (i.e., ${\text{conv}{\{\text{Q}_{0},\text{Q}_{1},\ldots,\text{Q}_{k}\}}} \subseteq C_{k}$).

Moreover, we have ${\text{R}_{n}{(t)}} = \text{Q}_{n}$.

### Proof

The proof goes in a similar way to that of Theorem 1.2, where $N:=n$, ${b_{k}{({\mathbf{t}})}}:={B_{k}^{n}{(t)}}$.

Note that this method is robust --- special cases $t = 0$ and $t = 1$ do not cause division by zero (cf. Remark 1.1) and yield $\text{W}_{0}$ and $\text{W}_{n}$, respectively. ∎

In each step of the new method, the point $\text{Q}_{k}$, which is a convex combination of points $\text{Q}_{k - 1}$ and $\text{W}_{k}$, is computed. The last point $\text{Q}_{n}$ is equal to the point $\text{R}_{n}{(t)}$. Thus, we obtain the new linear-time geometric algorithm for computing a point on a rational Bézier curve which computes only convex combinations of control points. For efficient implementations, see Section 2.2.

Note that if all weights $\omega_{k}$ are equal then $\text{Q}_{n} = {\text{P}_{n}{(t)}}$ (cf. (2.1)) --- the new method can also be used to evaluate a polynomial Bézier curve.

Figure 2.1 illustrates the new method in case of a planar polynomial Bézier curve of degree $n = 5$.

Figure 2.1: Computation of a point on a planar polynomial Bézier curve of degree n = 5 using the new method.

Using Theorem 1.4, one can prove the following result which tells even more about geometric properties of the new method.

### Theorem 2.2

Let the numbers $h_{k}$ and the points $\text{Q}_{k}$ $({0 \leq k \leq n})$ be computed by (2.4) for a given $0 \leq t \leq 1$. The point $\text{R}_{n}{(u)}$, where $u \in {\lbrack 0,1\rbrack}$, is in the convex hull of the points $\text{Q}_{0},\text{Q}_{1},\ldots,\text{Q}_{n}$ if and only if $u \leq t$. It means that

Let us notice that the proposed method can also be used for the subdivision of Bézier curve (cf., e.g., \[3, §5.4\]). For example, let us fix $u \in {}$, it is well-known that the points

are the control points of the polynomial Bézier curve $\text{P}_{n}^{L}$ being the left part of the Bézier curve (2.1) with $t \in {\lbrack 0,u\rbrack}$. One can check that

$\text{V}_{n} = \text{Q}_{n}$, where the numbers $h_{j}$ and the points $\text{Q}_{j}$ $({0 \leq j \leq n})$ are computed using (2.4) with $t:=u$, $\omega_{0} = \omega_{1} = \ldots = \omega_{n}:=1$.

### Implementation and cost

Let us give efficient and numerically safe implementations of the new method which have $O{({dn})}$ computational complexity and $O{}$ memory complexity.

Algorithm 2.1 First implementation

The implementation provided in Algorithm 2.1 requires ${{({{3d} + 8})}n} + 1$ floating-point arithmetic operations (flops) to compute a point on a rational Bézier curve of degree $n$ in ${\mathbb{E}}^{d}$.

Algorithm 2.2 Second implementation

Algorithm 2.2 decreases the number of flops to ${{({{3d} + 7})}n} + 2$. However, for numerical reasons (cf. lines 7 and 15 in Algorithm 2.2), it is necessary to use a conditional statement. More precisely, one has to check whether $t \in {\lbrack 0,0.5\rbrack}$ or $t \in {(0.5,1\rbrack}$, which can be easily done (it is enough to check an exponent of a floating-point number $t$).

Note that in the case of polynomial Bézier curves (2.1), one only needs to set $\omega_{k}:=1$ $({0 \leq k \leq n})$ in the given algorithms, thus simplifying used formulas. Then the number of flops is equal to ${{({{3d} + 6})}n} + 1$ in Algorithm 2.1 and ${{({{3d} + 5})}n} + 2$ in Algorithm 2.2.

new method (cf. Alg. 2.2)

rational Bézier curve

Table 2.1: Numbers of flops.

The numbers of flops for the new algorithms, as well as for de Casteljau algorithms (see Appendix), which also have a geometric interpretation and compute only convex combinations of control points, are given in Table 2.1.

### Example 2.3

Table 2.2 shows the comparison between the running times of de Casteljau algorithm and Algorithm 2.2 both for Bézier curves and rational Bézier curves (in the case of Bézier curves, Algorithm 2.2 has been simplified), for $d \in {\{ 2,3\}}$. The results have been obtained on a computer with Intel Core i5-2540M CPU at 2.60GHz processor and 4GB RAM, using GNU C Compiler 7.4.0 (single precision).

More precisely, we made the following numerical experiments. For a fixed $n$, $10000$ curves of degree $n$ are generated. Their control points $\text{W}_{k} \in {\lbrack{- 1},1\rbrack}^{d}$ and---in the rational case---weights $\omega_{k} \in {\lbrack 0.01,1\rbrack}$ $({0 \leq k \leq n})$ have been generated using the rand() C function. Each curve is then evaluated at 501 points $t_{i}:={i/500}$ $({0 \leq i \leq 500})$. Each algorithm is tested using the same curves. Table 2.2 shows the total running time of all $501 \times 10000$ evaluations.

rational Bézier curve

new method (cf. Alg. 2.2)
new method (cf. Alg. 2.2)

Table 2.2: Running times comparison (in seconds) for Example 2.3. The source code in C which was used to perform the tests is available at http://www.ii.uni.wroc.pl/~pwo/programs/new-Bezier-eval-main.c.

Observe that in the case of Bézier curves, the quantities $h$, which are computed in the new algorithms, do not depend on the control points. One can use this fact in the fast evaluation of $M$ Bézier curves of the same degree $n$ for the same value of the parameter $t$. Such a method requires ${{({{3dM} + 5})}n} + 2$ flops while the direct use of the de Casteljau algorithm means that all computations have to be repeated $M$ times, i.e., the number of flops is equal to ${{3Mdn{({n + 1})}}/2} + 1$.

### Remark 2.4

In rather rare cases $({h_{k} \approx 1})$, the problem of cancellation of digits (\[2, §2.3.4\]) can occur while $1 - h_{k}$ is computed (cf. $h_{1}$ in Algorithms 2.1, 2.2). One can avoid this problem using the relation

if computations with high accuracy are necessary.

## Remarks on evaluation of Bézier surfaces

The method of evaluation described in Section 1 can also be applied to the rational rectangular and triangular Bézier surfaces.

Let $\text{S}_{mn}:{{\lbrack 0,1\rbrack}^{2}\rightarrow{\mathbb{E}}^{d}}$ $({{m,n,d} \in {\mathbb{N}}})$ be a rational rectangular Bézier surface with the control points $\text{W}_{ij} \in {\mathbb{E}}^{d}$ and weights $\omega_{ij} > 0$ $({{0 \leq i \leq m},{0 \leq j \leq n}})$,

Define $T:={\{{(s,t)}:{{{s,t} \geq 0},{{\, 1 - s - t} \geq 0}}\}}$. Let there be given the control points $\text{V}_{ij} \in {\mathbb{E}}^{d}$ and positive weights $v_{ij}$ $({0 \leq {i + j} \leq n})$. Let $B_{ij}^{n}$ denotes the triangular Bernstein polynomials,

where $0 \leq {i + j} \leq n$. Let us consider a rational triangular Bézier surface $\text{T}_{n}:{T\rightarrow{\mathbb{E}}^{d}}$ $({{n,d} \in {\mathbb{N}}})$ of the form

Both surface types are, in fact, rational parametric objects (cf. (1.2)). Thus, one can apply Algorithm 1.1 to propose the methods which have geometric interpretations, compute only convex combinations of points and allow to evaluate Bézier surfaces in linear time with respect to the number of control points, i.e., $O{({nm})}$ in the rectangular case and $O{(n^{2})}$ in the triangular case. To do so, it is necessary to rearrange the sets of control points, corresponding weights and basis functions (cf. (1.1)) into one-dimensional sequences --- but since the method is agnostic of the ordering, the chosen ordering is only a matter of preference. Taking into account that the computations can be performed in many ways, we do not present rigorous algorithms and we pass some technical details.

In this section, to present a concise formulation of the methods, we choose the row-by-row order. For the reader's convenience, the analogues of quantities $h_{k}$ and points $\text{Q}_{k}$ from Algorithm 1.1 have two indices instead, to correspond with the surfaces' structure.

### Rational rectangular Bézier surfaces

Let $\text{S}_{mn}$ $({{m,n} \in {\mathbb{N}}})$ be a rational rectangular Bézier surface with the weights $\omega_{ij}$ and control points $\text{W}_{ij}$ $({{0 \leq i \leq m},{\, 0 \leq j \leq n}})$.

In this case, one can interpret the set of control points as a rectangular grid having $m + 1$ rows with $n + 1$ points in each row. We set the sequence of control points so that:

the sequence begins with $\text{W}_{00}$,

$\text{W}_{i,{j - 1}}$ is followed by $\text{W}_{ij}$ $({{0 \leq i \leq m},{\, 1 \leq j \leq n}})$,

$\text{W}_{{i - 1},n}$ is followed by $\text{W}_{i0}$ $({1 \leq i \leq m})$.

In a similar way, we set the sequences of weights $\omega_{ij}$ and basis functions $B_{i}^{m}{(s)}B_{j}^{n}{(t)}$ $({{0 \leq i \leq m},{\, 0 \leq j \leq n}})$.

It is well-known that if $(s,t)$ belongs to the boundary of the square ${\lbrack 0,1\rbrack}^{2}$ then the point $\text{S}_{mn}{(s,t)}$ lies on the boundary rational Bézier curve with boundary control points and weights. Thus, the method described in Section 2.1 can be used in this case.

Let us fix ${(s,t)} \in {}^{2}$. Now, based on Algorithm 1.1, we define the sequences of quantities $h_{ij}$ and points $\text{Q}_{ij} \in {\mathbb{E}}^{d}$ $({{0 \leq i \leq m},{\, 0 \leq j \leq n}})$---determined in the order described above---in the following recurrent way:

Theorem 1.2 implies that ${\text{S}_{mn}{(s,t)}} = \text{Q}_{mn}$.

### Rational triangular Bézier surfaces

Suppose $\text{T}_{n}$ $({n \in {\mathbb{N}}})$ is a rational triangular Bézier surface associated with the weights $v_{ij}$ and control points $\text{V}_{ij}$ $({0 \leq {i + j} \leq n})$.

The method described below is analogous to the one for rectangular Bézier surfaces. The main difference is that, in this case, the set of the control points can be seen as a triangular grid, i.e., the number of control points in each row depends on the row number. Namely, there are ${n - i} + 1$ points in the $i$th row $({0 \leq i \leq n})$ of this triangular grid. We choose the following ordering of control points:

the sequence begins with $\text{V}_{00}$,

$\text{V}_{i,{j - 1}}$ is followed by $\text{V}_{ij}$ $(0 \leq i \leq n - 1,\, 1 \leq j \leq n - i$),

$\text{V}_{{i - 1},{{n - i} + 1}}$ is followed by $\text{V}_{i0}$ $({1 \leq i \leq n})$.

We set the sequences of weights $v_{ij}$ and basis functions $B_{ij}^{n}{(s,t)}$ $({0 \leq {i + j} \leq n})$ in the same way.

Assume $(s,t)$ is on the boundary of the triangle $T$. Then the point $\text{T}_{n}{(s,t)}$ lies on the boundary rational Bézier curve having known control points and weights and, again, one can compute this point using the method presented in Section 2.1.

Let us fix a point $(s,t)$ inside the triangle $T$. Similarly, based on Algorithm 1.1, we introduce the sequences of quantities $g_{ij}$ and points $\text{U}_{ij} \in {\mathbb{E}}^{d}$ $({0 \leq {i + j} \leq n})$, which are computed in the order described above, by the following recurrent formulas:

Then ${\text{T}_{n}{(s,t)}} = \text{U}_{n0}$, which follows from Theorem 1.2.
