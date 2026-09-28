<!-- arxiv-full-text:v1 {"arxiv_id": "math/0103170", "source": "arxiv-html"} -->

## Introduction

This is an expository and experimental paper concerned with the following basic problem. Given a multivariate polynomial function $\,f\in\mathbb{R}[x_{1},\ldots,x_{n}]\,$ which is bounded below on $\mathbb{R}^{n}$, find the global minimum $f^{*}$ and a point $p^{*}$ attaining it: Exact algebraic algorithms for this task find all the critical points and then identifying the smallest value of $f$ at any critical point. Such methods will be discussed in Section 2. The techniques include Gröbner bases, resultants, eigenvalues of companion matrices, and numerical homotopy methods, \[Ver\].

An entirely different approach was introduced by N.Z. Shor and further developed in the dissertation of the first author. The idea is to compute the largest real number $\lambda$ such that $f(x)-\lambda$ is a sum of squares in $\mathbb{R}[x_{1},\ldots,x_{n}]$. Clearly, $\lambda$ is a lower bound for the optimal value $f^{*}$. We show in Section 3 that, when the degree of $f$ is fixed, the lower bound $\lambda$ can be computed in polynomial time using semidefinite programming. If $\lambda=f^{*}$ holds then this is certified by semidefinite programming duality, and the certificate yields the optimal point $p^{*}$. In our computational experiments, to be presented in Section 5, we found that $\lambda=f^{*}$ almost always holds, and we solved problems up to $n=15$.

The objective of this article is to provide a bridge between mathematical programming and algebraic geometry, demonstrating that algorithms from the former have the potential to play a major role in future algorithms in the latter. This will be underlined in Section 6, where we present open problems, and in Section 7 where we show that semidefinite programming in conjunction with the Positivstellensatz is applicable to a wide range of computational problems in real algebraic geometry.

## Computational Algebra

In this section we discuss the following approach to our problem (1.1). Form the partial derivatives of the given polynomial $f$ and consider the ideal they generate: The zeros of the ideal $I$ in complex $n$-space $\mathbb{C}^{n}$ are the critical points of $f$. Their number (counting multiplicity) is the dimension over $\mathbb{R}$ of the residue ring: We shall assume that $\mu$ is finite. (If $\mu=+\infty$ then one can apply perturbation techniques to reduce to the case $\mu<+\infty$). For instance, if $f$ is a dense polynomial of even degree $2d$ then it follows from Bézout's Theorem that $\,\mu\,=\,(2d-1)^{n}$.

Consider the subset of real critical points: This set is usually much smaller than the set of all complex critical points, i.e., typically we have $\nu\ll\mu$. If we know the set $\mathcal{V}_{\mathbb{R}}(I)$, then our problem is solved.

### Lemma 2.1

The optimal value is attained at a critical point: The three techniques to be described in this section all compute the set $\mathcal{V}_{\mathbb{R}}(I)$ of real critical points. We will illustrate then for the following example: The optimal value for this problem is $\,f^{*}\,=\,-2.112913882$, and, disregarding symmetry, there are three optimal points $(x^{*},y^{*},z^{*})$ attaining this value:

### Gröbner bases and eigenvalues

We review the method of solving polynomial equations by means of Gröbner bases and eigenvalues \[, §2.4\]. We are free to choose an arbitrary term order $\prec$ on the polynomial ring $\mathbb{R}[x_{1},\ldots\!,x_{n}]$. Let $\mathcal{G}$ be a Gröbner basis for the critical ideal $I$ with respect to $\prec$. While computing Gröbner bases is a time-consuming task in general, this is not an issue in this paper, since in all our examples the $n$ given generators $\,{\partial f}/{\partial x_{i}}\,$ already form a Gröbner basis in the total degree order. In our example the Gröbner basis is A monomial $x_{1}^{u_{1}}\!\cdots x_{n}^{u_{n}}$ is standard if it is not divisible by the leading term of any element in the Gröbner basis $\mathcal{G}$. The set $\mathcal{B}$ of standard monomials is an $\mathbb{R}$-basis for the residue ring $\mathbb{R}[{\bf x}]/I$. The standard monomials for (2.3) are: For any polynomial $g\in\mathbb{R}[{\bf x}]$ consider the $\mathbb{R}$-linear endomorphism: This endomorphism is represented in the basis $\mathcal{B}$ by a real $\mu\times\mu$-matrix ${\rm T}_{g}$. The entry of ${\rm T}_{g}$ with row index ${\bf x}^{u}\in\mathcal{B}$ and column index ${\bf x}^{v}\in\mathcal{B}$ is the coefficient of ${\bf x}^{v}$ in the normal form of $\,{\bf x}^{u}\cdot g({\bf x})\,$ with respect to $\mathcal{G}$.

### Proposition 2.2

The optimal value $f^{*}$ is the smallest real eigenvalue of the matrix ${\rm T}_{f}$. Any eigenvector of ${\rm T}_{f}$ with eigenvalue $f^{*}$ defines an optimal point $p^{*}=(p_{1}^{*},\ldots,p_{n}^{*})$ by the eigenvector identities $\,{\rm T}_{x_{i}}\cdot v=p_{i}\cdot v\,$ for $i=1,\ldots,n$.

### Proof

This follows from Lemma 2.1 and Theorem (4.5) in the book of Cox-Little-O'Shea; see also \[, Exercise 17, page 62\]. ∎ The resulting algorithm is to compute symbolically the matrices ${\rm T}_{f}$ and ${\rm T}_{x_{i}}$ for $i=1,\ldots,n$, then compute numerically its eigenvalues (and matching eigenvectors) of ${\rm T}_{f}$, and finally determine $f^{*}$ and $p^{*}$ as in the proposition.

In our example the matrix ${\rm T}_{f}$ has format $27\times 27$ with rows and columns indexed by (2.4). Of its $729$ entries only $178$ are nonzero. For instance, the column indexed by $xyz$ has four nonzero entries, namely, the coefficients of The matrix ${\rm T}_{f}$ has maximal rank $27$. Of its eigenvalues only three are real: The three real eigenvalues have multiplicity $3$,$1$, and $3$ respectively.

### Resultants and discriminants

One algebraic method for solving polynomial equations is to use resultants. Closely related to resultants are discriminants. They express the condition on a hypersurface to have a singularity, by means of a polynomial in the coefficients its defining equation. Let $t$ be a new indeterminate and form the discriminant of the polynomial $\,f(x)-t\,$ with respect to $x_{1},\ldots,x_{n}$: Here $\Delta_{x}$ refers to the $A$-discriminant, defined in \[, Chapter 9\], where $A$ is the support of $f$ together with the origin. From \[, §10.1.H\] we conclude that the discriminant $\delta(t)$ equals the characteristic polynomial of the matrix ${\rm T}_{f}$.

### Corollary 2.3

The optimal value $f^{*}$ is the smallest real root of $\delta(t)$.

In our example, $\delta(t)$ is $256t^{3}-512t^{2}-96t+473$ times the third power of The optimal value $f^{*}=-2.11...$ is a root of this sextic. This sextic has Galois group $S_{6}$, so $f^{*}$ cannot be expressed in radicals over the rationals.

The suggested algorithm is to compute $\delta(t)$, and minimal polynomials for the coordinates $x_{i}^{*}$ of the optimal point, by elimination of variables using matrix formulas for resultants and discriminants \[, Chapter 13\]. The subsequent numerical computation is to find the roots of a univariate polynomial.

### Homotopy methods

The critical equations form a square system: $n$ equations in $n$ variables having finitely many roots. Such a system is well-suited for numerical homotopy continuation methods. For an introduction to this subject see the papers of Li and Verschelde \[Ver\]. The basic idea is to introduce a deformation parameter $\tau$ into the given system. For instance, we might replace (2.3) by the following system which depends on a complex parameter $\tau$: The solutions $\,\bigl(x(\tau),y(\tau),z(\tau)\bigr)\,$ are algebraic functions of $\tau$. Our goal is to find them for $\tau=1$. It is easy to find the solutions for $\tau=0$: Homotopy methods trace the full set of solutions from $\tau=0$ to $\tau=1$ along a suitable path in the complex $\tau$-plane. We determine $f^{*}$ by evaluating the objective function $f(x,y,z)$ at all the real solutions for $\tau=1$.

Homotopy methods are frequently set up so that the system at $\tau=0$ breaks up into several systems, each of which consists of binomials. If the input polynomials are sparse, then these are the polyhedral homotopies which take the Newton polytopes of the given equations into consideration. In the sparse case, the number $\mu$ will be the mixed volume of the Newton polytopes. For an introduction to these polyhedral methods see \[, Chapter 7\] and the references given there.

### How large is the Bézout number ?

A common feature of all three algebraic algorithms in this section is that their running time is controlled by the number $\mu$ of complex critical points. In the eigenvalue method we must perform linear algebra on matrices of size $\mu\times\mu$, in the discriminant method we must find and solve a univariate polynomial of degree $\mu$, and in the homotopy method, we are forced to trace $\mu$ paths from $\tau=0$ to $\tau=1$. Each of these three methods becomes infeasible if the number $\mu$ is too big; for instance, $\,\mu\geq 10,000\,$ might be too big.

Suppose that the given polynomial $f$ in $\mathbb{R}[x_{1},\ldots,x_{n}]$ has even degree $2d$ and is dense. This will be the case in the family of examples studied in Section 5. Then $\mu$ coincides with the Bézout number $(2d-1)^{n}$. Some small values for the Bézout number are listed in Table 1. Most entries in this table are bigger than $10,000$. We are led to believe that the algebraic methods will be infeasible for quartics if $n\geq 8$.

Each entry in the first row of Table 1 is a one. This means we can minimize quadratic polynomial functions by solving a system of linear equations (in polynomial time). The punchline of this paper is to reduce our problem to a semidefinite programming problem which can also be solved in polynomial time for fixed $d$.

Table 1. The Bézout number μ = (2d − 1)n for the critical equations.

## Sums of Squares and Semidefinite Programming

We present the method introduced by N.Z. Shor, and further extended by the first author, for minimizing polynomial functions. This method is a relaxation: it always produces a lower bound for the value of $f^{*}$. However, as we shall see in Section 5, this bound very frequently agrees with $f^{*}$.

We may assume that the given polynomial $f(x_{1},\ldots,x_{n})$ has even degree $2d$. Let $X$ denote the column vector whose entries are all the monomials in $\,x_{1},\ldots,x_{n}$ of degree at most $d$. The length of the vector $X$ equals the binomial coefficient Let $\mathcal{L}_{f}$ denote the set of all real symmetric $N\times N$-matrices $A$ such that $f({\bf x})=X^{T}\cdot A\cdot X$. This is an affine subspace in the space of real symmetric $N\times N$-matrices. Assume that the constant monomial $1$ is the first entry of $X$. Let $E_{11}$ denote the matrix unit whose only nonzero entry is a one in the upper left corner.

### Lemma 3.1

For any real number $\lambda$, the following two are equivalent: The polynomial $\,f({\bf x})-\lambda\,$ is a sum of squares in $\mathbb{R}[{\bf x}]$.

There is a matrix $A\in\mathcal{L}_{f}$ such that $\,A-\lambda\cdot E_{11}\,$ is positive semidefinite, that is, all eigenvalues of this symmetric matrix are non-negative reals.

### Proof

The matrix $\,A-\lambda\cdot E_{11}\,$ is positive semidefinite if and only if there exists a real Cholesky factorization $\,A-\lambda\cdot E_{11}\,=\,B^{T}\cdot B$. If this holds then is a sum of squares, and every sum of squares representation arises in this way. ∎ We write $f^{sos}$ for the largest real number $\lambda$ for which the two equivalent conditions are satisfied. We always have $\,f^{*}\geq f^{sos}$. This inequality may be strict. It is even possible that $\,f^{sos}=-\infty$. An example of this form is Motzkin's polynomial It satisfies $m(x,y)\geq-1$, but $m(x,y)-\lambda$ is not a sum of squares for *any* $\lambda\in\mathbb{R}$. We refer to for an excellent survey of the problem of representing a polynomial as a sum of squares, and the important role played by Motzkin's example.

Sums of squares are crucial for us because of the following complexity result.

### Theorem 3.2

Fix ${\rm deg}(f)=2d$ and let the number of variables $n$ vary. Then there exists a polynomial-time algorithm, based on semidefinite programming, for computing $f^{sos}$ from $f$. The same statement holds if $n$ is fixed and $d$ varies.

Semidefinite programming (SDP) is the study of optimization problems over the cone of all positive semidefinite matrices. This branch of optimization has received a lot of attention in recent years, both for its theoretical elegance and its practical applications. Semidefinite programs can be solved in *polynomial time*, using interior point methods; see. This complexity result (together with Lemma 3.1) implies Theorem 3.2 because the quantity $\,N=\binom{n+d}{d}=\binom{n+d}{n}\,$ grows polynomially if either $n$ or $d$ is fixed. This result appears.

Table 2. The matrix size $N=\binom{n+d}{d}$ for the semidefinite programs.

Available implementations of interior-point methods for semidefinite programming perform extremely well in practice, say, for problems involving matrices up to $500$ rows and columns (provided there are not too many variables). This allows for the efficient computation of $f^{sos}$, and as we shall see in Section 4, SDP duality furnishes a polynomial-time test to check whether $f^{*}=f^{sos}$ and for computing the optimal point $p^{*}$ in the affirmative case. A comparison of Tables 1 and 2 suggests that SDP has the potential to compute much larger instances than algebraic methods. Section 5 will show that this is indeed the case.

Our example (2.2) has parameters $d=2,n=3$. The affine space $\mathcal{L}_{f}$ consists of all $10\times 10$-matrices $A(\lambda,{\bf c})$ with $\lambda=0$ and $c_{i}\in\mathbb{R}$ arbitrary in the family The rows and columns of this matrix are indexed by the entries of the vector We invite the reader to check the identity The lower bound $f^{sos}$ is the largest real number $\lambda$ such that, for some choice of $c_{1},\ldots,c_{20}\in\mathbb{R}$, the matrix $\,A({\bf c},\lambda)\,$ has all eigenvalues nonnegative. We find that and the optimal matrix (to five digits) is given: This matrix is positive semidefinite. By computing a factorization $\,B^{T}\cdot B\,$ as in the proof of Lemma 3.1, we can express $f-f^{sos}$ as a sum of squares. In the next section we show how to recover the points at which the optimal value is achieved.

Note that the number $20$ of free parameters is the case "$n=3,d=2$" of:

### Remark 3.3

The dimension of $\mathcal{L}_{f}$ equals the number of linearly independent quadratic relations among the monomials of degree $\leq d$ in $n$ variables. It equals The codimension (with respect to the space of symmetric matrices) is equal to

## Semidefinite Programming Duality

In Section 3 we demonstrated that computing $f^{sos}$ is equivalent to minimizing a linear functional over the intersection of the affine space $\mathcal{L}_{f}$ with the cone of positive semidefinite $N\times N$-matrices. In our discussion we have represented the space $\mathcal{L}_{f}$ by a spanning set of matrices. For numerical efficiency reasons it is usually preferable to represent $\mathcal{L}_{f}$ by its defining equations (unless $n$ and $d$ are very small).

Duality is a crucial feature of semidefinite programming. It plays an important role in designing the most efficient interior-point algorithms. In what follows we review the textbook formulation of SDP duality, in terms of matrices. Thereafter we present a reformulation in algebraic geometry language, and we then explain how to test the condition $f^{sos}=f^{*}$ and how to recover the optimal point $p^{*}$.

### Matrix Formulation

Let $\mathcal{S}^{N}$ denote the real vector space of symmetric $N\times N$-matrices, with the inner product $A\bullet B:=\mbox{trace }(A\,B)$, and the Löwner partial order given by $A\preceq B$ if $B-A$ is *positive semidefinite*. Recall that $A\in\mathcal{S}^{N}$ is positive semidefinite if $x^{T}Ax\geq 0$, for all $x\in\mathbb{R}^{N}$. This condition is equivalent to nonnegativity of all eigenvalues of $A$, and to nonnegativity of all principal minors.

The general SDP problem can be expressed in the form: where $X,F\in\mathcal{S}^{N}$, $b\in\mathbb{R}^{M}$, and $\mathcal{G}:\mathcal{S}^{N}\longrightarrow\mathbb{R}^{M}$ is a linear operator. This is usually called the *primal* form, in analogy with the linear programming (LP) case.

Notice that (4.1) is a *convex* optimization problem, since the objective function is linear and the feasible set is convex. There is an associated *dual* problem: where $y\in\mathbb{R}^{M}$ and $\mathcal{G}^{*}:\mathbb{R}^{M}\longrightarrow\mathcal{S}^{N}$ is the operator adjoint to $\mathcal{G}$. Any feasible solution of the dual problem is a lower bound of the optimal value of the primal: The last inequality holds since the inner product of two positive semidefinite matrices is nonnegative. The converse statement (primal feasible solutions give upper bounds on the optimal dual value) is obviously also true. The inequality above is called *weak duality*. Under certain conditions (notably, the existence of strictly feasible solutions), *strong duality* also holds: the optimal values of the primal and the dual problems coincide. If strong duality holds, then at optimality the matrix $\,X\cdot(F-\mathcal{G}^{*}y)\,$ is zero, since $A,B\succeq 0,\mbox{trace}(AB)=0$ implies $AB=0$. This can be interpreted as a generalization of the usual *complementary slackness* LP conditions.

Practical implementations of SDP (we will use SeDuMi ) simultaneously compute both the optimal matrix $X$ for (4.1) and the optimal vector $y$ for (4.2).

### Polynomial Formulation

We set $m=N-1$ and we identify $\mathcal{S}^{N}$ with the real vector space $\,\mathbb{R}[x]_{2}=\mathbb{R}[x_{0},x_{1},\ldots,x_{m}]_{2}\,$ of quadratic forms in $m+1$ variables. The vector space dual to $\mathcal{S}^{N}$ is now denoted $\,\mathbb{R}[\partial]_{2}=\mathbb{R}[\partial_{0},\partial_{1},\ldots,\partial_{m}]_{2}$. The dual pairing is given by differentiation and is denoted $\bullet$. For any $f\in\,\mathbb{R}[\partial]_{2}\,$ and any real vector $p=(p_{0},\ldots,p_{m})\in\mathbb{R}^{m+1}$, the following familiar identity holds: We consider the general quadratic programming problem: where $f,g_{0},\ldots,g_{r}\in\mathbb{R}[\partial]_{2}$ are given and we are looking for an optimal point $p\in\mathbb{R}^{m+1}$. This problem can be relaxed to the following primal SDP: The inequality $\,q(x)\succeq 0\,$ means that $q$ is non-negative on $\mathbb{R}^{m+1}$, i.e., $q$ is in the positive semidefinite cone in $\mathbb{R}[x]_{2}$. In view of (4.3), the optimal value of (4.4) is greater than or equal to the optimal value of the primal SDP, and equality holds if and only if there is an optimal solution of the form $q(x)=\frac{1}{2}(\sum_{i=0}^{m}p_{i}x_{i})^{2}$.

Every semidefinite programming problem comes with a dual problem, as in the previous subsection; see also. In our case the dual SDP takes the form: Assuming the existence of a strictly feasible primal solution, the maximum value in the dual SDP is always equal to the minimum value in the primal SDP. Under this regularity assumption, which is easy to satisfy in our application, we conclude:

### Proposition 4.1

If the primal SDP has an optimal solution of the form $\,q(x)=\frac{1}{2}(\sum_{i=0}^{m}p_{i}x_{i})^{2}\,$ then the vector $(p_{0},\ldots,p_{m})$ is an optimal solution for (4.4).

### Minimizing Quadratic Functions over Toric Varieties

A toric variety is an algebraic variety, in affine space or projective space, which has a parametric representation by monomials. Equivalently, a toric variety is an irreducible variety which is cut out by binomial equations, that is, differences of monomials. Here we will be interested in those projective toric varieties which are defined by quadratic binomials. This class includes many examples from classical algebraic geometry, such as Veronese and Segre varieties. See for an introduction.

Let $X$ be a toric variety in projective $m$-space whose defining prime ideal is generated by quadratic binomials $g_{1},\ldots,g_{r}$ in $\mathbb{R}[\partial_{0},\ldots,\partial_{m}]$. Each generator has the form $\,\partial_{i}\partial_{j}-\partial_{k}\partial_{l}\,$ for some $i,j,k,l\in\{0,1,\ldots,m\}$. We set $\,g_{0}(\partial)=\partial_{0}^{2}$. Then the equation $\,g_{0}(\partial)=1\,$ on $X$ defines an affine toric variety $\tilde{X}$, such that $X$ is the projective closure of $\tilde{X}$. Every quadratic polynomial function on the affine variety $\tilde{X}$ is represented by a quadratic form $f\in\mathbb{R}[\partial]_{2}$ as above. This representation is unique modulo the $\mathbb{R}$-linear span of $g_{1},\ldots,g_{r}$. Our problem (4.4) is hence equivalent to minimizing a quadratic function over an affine toric variety defined by quadrics: The optimal value of the dual SDP relaxation in Subsection 4.2 is the largest real number $\lambda$ such that $f-\lambda$ is a sum of squares in the coordinate ring of $\tilde{X}$.

Let us now return to our original problem (1.1) where the given polynomial is dense of degree $2d$ in $n$ variables. Here $X$ is the Veronese variety in projective $N$-dimensional space which is parameterized by all monomials of degree at most $d$. (If the polynomial in (1.1) is sparse then another toric variety can be used.) Writing our given polynomial as a quadratic form in homogeneous coordinates on $X$, our minimization problem (1.1) is precisely the quadratic toric problem (4.5).

We solve (4.5) by simultaneously solving the primal and dual SDP relaxation in Subsection 4.2. If the optimal value $\lambda$ of the dual SDP agrees with the true minimum of $f$ over $\tilde{X}$ then the primal SDP has an optimal solution $\,q(x)=\frac{1}{2}(\sum_{i=0}^{m}p_{i}x_{i})^{2}$ which exhibits an optimal point $(p_{0},\ldots,p_{m})\in X$ at which $f$ is minimized.

In our running example, we have $m=9$ and $r=20$, and $X$ is the quadratic Veronese three-fold in projective $9$-space which is given parametrically as It is cut out by twenty quadratic binomials such as $\,x_{0}x_{5}-x_{1}x_{2}$. These binomials correspond to the parameters $c_{i}$ in the $10\times 10$-matrix $A(\lambda,{\bf c})$ in Section 2.

## Experimental Results

We now present our computational experience with Shor's relaxation for global minimization of polynomial functions. As mentioned earlier, the computational advantages of our method are based on the following three independent facts: The dimension $N$ of the matrix required in the sum of squares formulation is much smaller than the Bézout number $\mu$, since it only scales polynomially with the number of variables. See Tables 1 and 2 above.

Semidefinite programming provides an efficient algorithm for deciding whether a polynomial is a sum of squares, and to find such representations for polynomials whose coefficients may depend linearly on parameters.

The lower bound $f^{sos}$ very often coincides with the exact solution $f^{*}$ of our problem (1.1), at least for the class of problems analyzed here.

The experimental results in this section strongly support the validity of these facts.

### The test problems

For our computations, we fix a positive integer $K$, and we sample from the following family of polynomials of degree $2d$ in $n$ variables: where $g\in\mathbb{Z}[x_{1},\ldots,x_{n}]$ is a random polynomial of total degree $\leq 2d-1$ whose $\,\binom{n+2d-1}{n}\,$ coefficients are independently and uniformly distributed among integers between $-K$ and $K$. Thus our family depends on three parameters: $n$, $d$ and $K$.

This family has been selected to ensure three important properties:: The highest order terms $\,x_{i}^{2d}\,$ ensure that $f$ is bounded below, and that the minimum value $f^{*}$ is achieved at some point $\,p^{*}\in\mathbb{R}^{n}$.

Efficient basis computation:: When solving polynomial systems, the calculation of a Gröbner basis is a time-consuming task. The structure of the polynomial (5.1) allows us to bypass this expensive step, since the set of $n$ scaled partial derivatives $\,x_{i}^{2d-1}+\frac{1}{2d}\cdot\partial g/\partial x_{i}\,$ is already a Gröbner basis with respect to total degree; cf. \[, §2.9, Proposition 4\].: A main reason for this choice of model is its simplicity. While more sophisticated choices have other desirable mathematical properties (such as invariance under certain transformations), we preferred to analyze here, as a first step, a relatively easy to describe set of instances.

An important question is if the structure of the polynomials (5.1) is somehow "biased" towards the application of sum of squares methods. This is a relevant issue, since the performance of algorithms on "random instances" sometimes provides more information on the problem family, rather than on the algorithm itself. Concerning this question, we limit ourselves to notice that, for $K$ sufficiently large, the family (5.1) does include polynomials $f$ with $f^{sos}<f^{*}$. A simple example is $f(x,y)=x^{8}+y^{8}+2700\,m(x,y)$, where $m(x,y)$ is the Motzkin polynomial (3.1).

The polynomials in our family have global minima that generally have large negative values, of the order of $-K^{2d}$. This leads to ill-conditioning of the symmetric matrices described in Lemma 3.1, and hence to numerical problems for the interior-point algorithm. Our remedy is a simple homogeneous scaling of the form Obviously, this does not affect the properties of being a sum of squares, or whether $f^{*}=f^{sos}$. However, as is generally the rule in numerical optimization, this scaling step greatly affects both the speed and the accuracy of the SDP solution.

### Algorithms and software

Most of the test examples were run on a Pentium III 733Mhz with 256 MB, running Linux version 2.2.16-3, and using MATLAB version 5.3. Because of physical memory limitations, our largest examples (quartics in fifteen variables), were run on a Pentium III 650Mhz with 320 MB, under Windows 2000. The semidefinite programs were solved using the SDP solver SeDuMi, written by Jos Sturm. It is currently one of the most efficient codes available, at least for the restricted class of problems relevant here. SeDuMi can be run from within MATLAB, and implements a self-dual embedding technique. The default parameters are used, and the solutions computed are typically exact to machine precision (SeDuMi provides an estimate of the quality of the solution).

The MATLAB Optimization toolbox was used for the implementation of a local search approach, to be described in Section 5.3. For the numerical homotopy method, we used the software PHCpack, written by Jan Verschelde. The computation of the sparse matrix ${\rm T}_{f}$ was done using Macaulay 2 \[GS\], and its eigenvalues were numerically computed using MATLAB.

We do not make strong claims about the efficiency of our implementations: while reasonable fast, for large scale problems considerable speedups are possible at the expense of customized algorithms. Nevertheless, we believe that the issues raised regarding the applicability of algebra-based techniques to problems with large Bézout number remain valid, independently of the particular software employed.

### Standard local optimization

An alternative approach to the problem is given by traditional (nonconvex) numerical optimization. There exist many variations, but arguably the most successful methods for relatively small problems such as the present ones are based on local gradient and Hessian information. Typical algorithms in this class employ an iterative scheme, combining the Newton search direction in combination with a line search. These methods are reasonably fast in converging to a *local* minimum. For the larger problems in our family, they usually converge to a stationary point within 10 seconds. However, they often end up in the wrong solution, unless a very accurate starting point is given.

The drawbacks of local optimization methods are well-known: lacking convexity, there are no guarantees of global (or even local) optimality. Worse, even if in the course of the optimization we actually reach the global minimum, there is usually no computationally feasible way of verifying optimality.

Nevertheless, local optimization is an important tool for polynomial problems, as is the use of homotopy methods to trace the optimal value under small changes in the input data. It would interesting to investigate how these local numerical techniques can be best combined with the computations to be described next.

### Experimental results using computational algebra

In Table 3 we present typical running times for the homotopy based approach, described in Section 2.3. These were obtained running PHCpack in "black-box" mode (phc -b), that requires no user-specified parameters. The software traces all solutions (not necessarily real), its number being equal to the Bézout number. Comparing with Table 1, we can notice the adverse effect of large Bézout numbers in the practical performance of the algorithm, in spite of Verschelde's impressive implementation.

Table 3. Running time (in seconds) for the homotopy method.

For the eigenvalue approach outlined in Section 2.1, we compute the matrix ${\rm T}_{f}$ using a straightforward implementation in Macaulay 2: the endomorphism ${\rm Times}_{f}$ is constructed, and applied to the elements of the monomial basis $\mathcal{B}$. The resulting matrix, in a sparse floating point representation, is sent to a file for further processing. We found that the construction of the matrix ${\rm T}_{f}$ takes a surprisingly long time. for instance, it took Macaulay 2 over $10$ minutes to produce the $125\times 125$-matrix for $2d=6$, $n=3$. The eigenvalue problem itself is solved using MATLAB; it exploits the sparsity of the matrix, and runs reasonably fast. However, it appears that even a more efficient implementation of this method will not be able to compete with the timings in Table 3, let alone the timings in Table 5.

After several discouraging attempts for small examples, we did not pursue a full implementation for the resultant-based methods sketched in Section 2.2.

### Experimental results using semidefinite programming

We ran several instances of polynomials in the family described above, for values of $K$ equal to 100, 1000, and 10000. In Table 5 the typical running times for the semidefinite programming based approach on a single instance are presented. These are fairly constant across instances, and no special structure is exploited (besides what SeDuMi does internally).

The number of random instances for each combination of the parameters is shown in Table 4. These values were chosen in order to keep the total computation time for a given category in the order of a few hours.

Table 4. Number of random instances in each category (K = 100, 1000, 10000).

Regarding the accuracy of the relaxation, in *all cases tested* the condition $f^{sos}=f^{*}$ was satisfied. As explained in the previous section, this can be numerically verified by checking if the solution of the corresponding SDP has rank one, from which a candidate global minimizer is obtained. Evaluating the polynomial at this point provides an upper bound on the optimal value, that can be compared with the lower bound $f^{sos}$. In all our instances, the difference between these two quantities was extremely small, and within the range of numerical error.

As an additional check, when we used different methods for solving the same instance, we have verified the solutions against each other. As expected, the solutions were numerically close, in many cases up to machine precision.

In particular, it is noted that the approach can handle in a reasonable time (less than 35 min.) the case of a quartic polynomial in thirteen variables. Our largest examples have the same degree ($2d=4$) and fifteen variables, correspond to an SDP with a matrix of dimensions $136\times 136$ with $3876$ auxiliary variables, and can be solved in a few hours. A quick glance at the corresponding Bézout number in Table 1 makes clear the advantages of the presented approach.

Table 5. Running time (in seconds) for the semidefinite programs. The marked instance was solved on a different machine.

## What Next ?

We have demonstrated that the sums of squares relaxation is a powerful and practical technique in polynomial optimization. There are many open questions, both algorithmic and mathematical, which are raised by our experimental results. One obvious question is how often does it occur that $f^{sos}=f^{*}$ ? This can be studied for our simple model (5.1), or, perhaps better, for various natural probability measures on the space of polynomials of bounded degree. This question is closely related to understanding the inclusion of the convex cone of forms that are sums of squares inside the cone of positive semidefinite forms. For the three-dimensional family of symmetric sextics, this problem was studied in detail by Choi, Lam and Reznick. Their work is an inspiration, but it also provides a warning as to how difficult the general case will be, even for ternary sextics without symmetry.

We hope to pursue some of the following directions of inquiry in the near future.

### Sparseness and Symmetry

Most polynomial systems one encounters are sparse in the sense that there are only few monomials with nonzero coefficients. Methods involving Newton polytopes, such as sparse resultants and polyhedral homotopies \[Ver\], are designed to deal with such problems. Symmetry with respect to finite matrix groups is another feature of many polynomial problems arising in practise. The book of Gatermann is an excellent first reference.

We wish to adapt our semidefinite programming approach to input polynomials $f$ which are sparse or symmetric or both. For instance, our polynomial example (2.2) is both sparse and invariant under permutation of the variables $x,y,z$. Both Newton polytope techniques and representation theory can be used to reduce the size of the matrices and the number of free parameters in the semi-definite programs.

### Higher degree relaxations

If we are unlucky, then the output produced by SeDuMi will not satisfy the hypothesis of Proposition 4.1, and we conclude that the bound $f^{sos}$ is probably strictly smaller than the optimal solution $f^{*}$. In that event we redo our computation in higher degree, now with a larger SDP. The key idea is that even though $f(x)-\lambda$ may not be a sum of squares, if there exists a positive polynomial $g(x)$ such that $g(x)\cdot(f(x)-\lambda)$ is a sum of squares, then $\lambda\leq f^{*}$. The choice of $g$ can be either made *a priori* (for instance, $g=\sum_{i=1}^{n}x_{i}^{2k}$), or as a result of an optimization step (see for details). The Positivstellensatz (see Section 7) ensures that $f^{*}$ will be found if the degree of $g$ is large enough.

### Solving polynomial equations

A natural application of Shor's relaxation, hinted , is solving polynomial systems $\,g_{1}(x)=\cdots=g_{r}(x)=0$. The polynomial $\,f(x):=\sum_{i=1}^{r}g^{2}_{i}(x)\,$ satisfies $\,f^{*}\geq f^{sos}\geq 0$, and $f^{*}=0$ holds if and only if the system has a real root. Clearly, $f^{sos}>0$ is a sufficient condition for the nonexistence of real roots. An important open problem, essentially raised, is to characterize inconsistent systems $\{g_{1},\ldots,g_{r}\}$ with $f^{sos}=0$. On the other hand, if $\,f^{*}=f^{sos}=0\,$ holds then it is possible, at least in principle, to obtain a numerical approximation of real roots using SDP. However, for a robust implementation, perturbation arguments are required and some important numerical issues arise, so the perspectives for practical applications are still unclear.

### Minimizing polynomials over polytopes

Consider a compact set where $\ell_{i}$ is a linear form plus a constant, say, $P$ is a polytope with $s$ facets. Handelman's Theorem states that every polynomial which is strictly positive on $P$ can be expressed as a positive linear combination of products $\,\ell_{1}(x)^{i_{1}}\cdots\ell_{s}(x)^{i_{s}}$. Suppose we wish to minimize a given polynomial function $f(x)$ over $P$. For $D\in\mathbb{N}$ we define the $D$-th Handelman bound $\,f^{(D)}\,$ to be the largest $\,\lambda\in\mathbb{R}\,$ such that Handelman's Theorem states that the increasing sequence $\,f^{(D)},\,f^{(D+1)},\,f^{(D+2)},\ldots\,$ converges to the minimum of $f$ over $P$. Each bound $f^{(D)}$ can be computed using linear programming only. It would be interesting to study the quality of these bounds, and the running time of these linear programs, and to see how things improve as we augment the approach with semidefinite programming techniques.

### Which semialgebraic sets are semidefinite ?

The feasible set of an SDP can be expressed by a linear matrix inequality, as in the dual formulation in Section 4.2. It would be interesting to study these feasible sets using techniques from real algebraic geometry, and to identify characteristic features of these sets. Here is a very concrete problem whose solution, to the best of our knowledge, is not known. Fix three real symmetric matrices $A,B$ and $C$ of size $N\times N$. Then is a closed, convex, semialgebraic subset of the plane $\mathbb{R}^{2}$. The problem is to find a good characterization of those subsets $S$. Given a semialgebraic subset $S\subset\mathbb{R}^{2}$ which is closed and convex, how to decide whether a "semidefinite representation" exists, and, in the affirmative case, how to find matrices $A,B,C$ of minimum size.

## Numerical Real Algebraic Geometry and The Positivstellensatz

The first part of the above title refers to a paper by Sommese and Wampler. This paper and other more recent ones suggest that numerical algorithms will play an increasingly important role in computational (complex) algebraic geometry, and that polynomial systems will become much more visible in the context of Scientific Computation. Along the same lines, the fastest software for computing Gröbner bases, due to Faugére, no longer uses the Buchberger algorithm but replaces it by sophisticated numerical linear algebra. Faugére's scheme has the potential of entering the standard repertoire of Scientific Computation.

Following we propose an analogous scheme for the field of real numbers: In what follows, we shall explain this relationship and why we see the Positivstellensatz as the main catalyst for a future role of real algebra in scientific computation.

The Positivstellensatz is a common generalization of Linear Programming Duality (for linear inequalities) and Hilbert's Nullstellensatz (for an algebraically closed field). It states that, for a system of polynomial equations and inequalities, either there exists a solution in $\mathbb{R}^{n}$, or there exists a certain polynomial identity which bears witness to the fact that no solution exists. For instance, a single polynomial inequality $f(x)<0$ either has a solution $x\in\mathbb{R}^{n}$, or there exists an identity $\,g(x)f(x)=h(x)\,$ where $g$ and $h$ are sums of squares. See for an exposition of the Positivstellensatz from the perspective of computational geometry. Finding a witness by linear programming is proposed in \[, §7.3\].

Here is our punchline, first stated in the dissertation of the first author: A Positivstellensatz witness of bounded degree can be computed by semidefinite programming. Here we can also optimize linear parameters in the coefficients. This suggests the following algorithm for deciding a system of polynomial equations and inequalities: decide whether there exists a witness for infeasibility of degree $\leq D$, for some $D\gg 0$. If our system is feasible, then we might like to minimize a polynomial $f(x)$ over the solution set. The $D$-th SDP relaxation would be to ask for the largest real number $\lambda$ such that the given system together with the inequality $\,f(x)-\lambda<0\,$ has an infeasibility witness of degree $D$. This generalizes what was proposed in Sections 6.2, 6.3 and 6.4.

It is possible, at least in principle, to use an a priori bound for the degree $D$ in the Positivestellensatz, however, the currently known bounds are still very large. Lombardi and Roy recently announced a bound which is triply-exponential in the number $n$ of variables. We hope that such bounds can be further improved, at least for some natural families of polynomial problems arising in optimization.

Here is a very simple example in the plane to illustrate our method: By the Positivstellensatz, the system $\,\{f\geq 0,\,g=0\}\,$ has no solution $\,(x,y)\in\mathbb{R}^{2}\,$ if and only if there exist polynomials $s_{1},s_{2},s_{3}\in\mathbb{R}[x,y]$ that satisfy the following: The $D$-th SDP relaxation of the polynomial problem $\,\{f\geq 0,\,g=0\}\,$ asks whether there exists a solution $(s_{1},s_{2},s_{3})$ to (7.2) where the polynomial $s_{1}$ has degree $\leq D$ and the polynomials $s_{2},s_{3}$ have degree $\leq D-2$. For each fixed integer $D>0$ this can be tested by semidefinite programming. For $D=2$ we find the solution The resulting identity (7.2) proves the inconsistency of the system $\,\{f\geq 0,\,g=0\}$.
