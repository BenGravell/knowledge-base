<!-- arxiv-full-text:v1 {"arxiv_id": "0712.2887", "source": "ar5iv"} -->

## Introduction

Stability of discrete linear inclusions has been a topic of major research over the past two decades. Such systems can be represented as a switched linear system of the form ${x{({k + 1})}} = {A_{\sigma{(k)}}x{(k)}}$, where $\sigma$ is a mapping from the integers to a given set of indices. The above model, and its many variations, has been studied extensively across multiple disciplines including control theory, theory of non-negative matrices and Markov chains, subdivision schemes and wavelet theory, dynamical systems, etc. The fundamental question of interest is to determine whether $x{(k)}$ converges to a limit, or equivalently, whether the infinite matrix products chosen from the set of matrices converge \[\]. The research on convergence of infinite products of matrices spans across four decades. A majority of results in this area has been provided in the special case of non-negative and/or stochastic matrices. A non-exhaustive list of related research providing several necessary and sufficient conditions for convergence of infinite products and their applications includes \[\]. Despite the wealth of research in this area, finding algorithms that can unambiguously decide convergence remains elusive. Much of the difficulty of this problem stems from the hardness in computation or efficient approximation of the joint spectral radius of a finite set of matrices. This notion was introduced by Rota and Strang via the definition and represents the maximum growth rate that can be achieved by taking arbitrary products of the matrices $A_{i}$. As in the case of the classical spectral radius, the value of this expression is independent of the choice of norm. Daubechies and Lagarias conjectured that the joint spectral radius is equal to a related quantity, the generalized spectral radius, which is defined in a similar way except for the fact that the norm of the product is replaced by the spectral radius. Berger and Wang proved this conjecture to be true for finite sets of matrices. Blondel and Tsitsiklis have shown that computing $\rho$ is hard from a computational complexity viewpoint, and even approximating it is difficult \[, \]. In particular, it follows from their results that the problem "Is $\rho \leq 1$?" is undecidable. For rational matrices, the joint spectral radius is not a semialgebraic function of the data, thus ruling out a very large class of methods for its exact computation. We refer the reader to the survey \[, §3.5\] for further results and references on the computational complexity of the joint spectral radius.

It turns out that a necessary and sufficient condition for the stability of a linear difference inclusion is for the corresponding matrices to have a subunit joint spectral radius, i.e., ${\rho{(A_{1},\ldots,A_{m})}} < 1$; see e.g. \[, Thm. 1\] and. A subunit joint spectral radius is equivalent to the existence of a common norm with respect to which all matrices in the set are contractive \[ \]; unfortunately, this common norm is in general not finitely constructible. In fact a similar result, due to Dayawansa and Martin, holds for nonlinear systems that undergo switching. A popular approach towards approximating the joint spectral radius or showing that it is indeed subunit has been to try to prove simultaneous contractibility (i.e., existence of a common norm with respect to which matrices are contractive), by searching for a common ellipsoidal norm, or equivalently, a common quadratic Lyapunov function. The benefit of this approach is due to the fact that the search for a common ellipsoidal norm can be posed as a semidefinite program and solved efficiently using interior point techniques. However, it is not too difficult to generate examples where the discrete inclusion is absolutely asymptotically stable, i.e., asymptotically stable for all switching sequences, but a common quadratic Lyapunov function, (or equivalently a common ellipsoidal norm) does not exist.

Ando and Shih describe a constructive procedure for generating a set of $m$ matrices whose joint spectral radius is equal to $\frac{1}{\sqrt{m}}$, but for which no quadratic Lyapunov function exists. They prove that the interval $\lbrack 0,\frac{1}{\sqrt{m}})$ is effectively the "optimal" range for the joint spectral radius necessary to guarantee simultaneous contractibility under an ellipsoidal norm for a finite collection of $m$ matrices. The range is denoted as optimal since it is the largest subset of $\lbrack 0,1)$ for which if the joint spectral radius is in this subset the collection of matrices is simultaneously contractible under an ellipsoidal norm. Furthermore, they show that the optimal joint spectral radius range for a bounded set of $n \times n$ matrices is the interval $\lbrack 0,\frac{1}{\sqrt{n}})$. The proof of this fact is based on John's ellipsoid theorem. Roughly speaking, John's ellipsoid theorem implies that every convex body in $n$-dimensional Euclidean space that is symmetric with respect to the origin can be approximated by inner and outer ellipsoids, up to a factor of $\frac{1}{\sqrt{n}}$. Independently, Blondel, Nesterov and Theys showed a similar result (also based on John's ellipsoid theorem), that the best ellipsoidal norm approximation of the joint spectral radius provides a lower bound and an upper bound on the actual value. Given a set $\mathcal{M}$ of $n \times n$ matrices with joint spectral radius $\rho$, and best ellipsoidal norm approximation $\hat{\rho}$, it is shown there that A major consequence of these results is that finding a common Lyapunov function becomes increasingly hard as the dimension goes up.

There have been a number of earlier works proposing different numerical techniques for the effective computation of bounds on the joint spectral radius. A natural class of lower bounds is obtained by considering periodic switching sequences, in which case only a finite number of matrix norms need to be computed. Using a naive approach, the required computational efforts grow exponentially as $m^{k}$, where $k$ is the period of the sequence. Due to the cyclic property of the spectral radius, some terms are redundant, and Maesumi has shown using combinatorial techniques that the number of required products can be reduced to $m^{k}/k$. Another approach is the work of Gripenberg, who has introduced a branch-and-bound algorithm to produce upper and lower bounds on the joint spectral radius. Protasov \[, \] has developed a geometric method to approximate this quantity, based on a polytopic approximation of a convex set that is invariant under the action of the linear operators $A_{i}$. This method has also been extended to the computation of the so-called $p$-radius. More recently, Blondel and Nesterov have proposed an alternative scheme to the computation of the joint spectral radius, by "lifting" the matrices using Kronecker products to provide better approximations. A common feature in many of these approaches is the presence of convexity-based methods to provide certificates of the desired system properties.

In this paper, we develop a sum of squares (SOS) based scheme for the approximation of the joint spectral radius. The method computes, using the techniques of semidefinite programming, a homogeneous polynomial that serves as a Lyapunov-like function for the corresponding switched linear system. We prove several results on the quality of approximation of the proposed scheme. In particular, it will follow from Theorems 10 and 4.3 that our SOS-based approximation $\rho_{{SOS},{2d}}$ satisfies where $\eta:={\min{\{ m,\binom{{n + d} - 1}{d}\}}}$. To prove this, we use two different techniques, one inspired by recent results of Barvinok on approximation of norms by polynomials, and the other one based on a convergent iteration similar to that used for Lyapunov inequalities. Our results provide a simple and unified derivation of most of the available bounds, including some new ones. We prove that the SOS-based approximation is always tighter than that obtained by the use of common quadratic Lyapunov functions, and than the one provided by Blondel and Nesterov. Furthermore, we show how to compute the bound using matrices that are exponentially smaller than those proposed there; this result also follows from the earlier work of Protasov. A preliminary version of some of our results has been presented.

A description of the paper follows. In Section 2 we present a class of bounds on the joint spectral radius based on simultaneous contractivity with respect to a norm, followed by a sum of squares-based relaxation, and the corresponding suboptimality properties. In Section 3 we present some background material in multilinear algebra, necessary for our developments, and a derivation of a bound of the quality of the SOS relaxation. An alternative development is presented in Section 4, where a different bound on the performance of the SOS relaxation is given in terms of a very natural Lyapunov iteration, similar to the classical case. In Section 5 we make a comparison with earlier techniques and analyze a numerical example. Finally, in Section 6 we present our conclusions.

## Bounds via polynomials and sums of squares

A natural way of bounding the joint spectral radius is to find a common norm that guarantees certain contractiveness properties for all the matrices. In this section, we first revisit this characterization, and introduce our method of using SOS relaxations to approximate this common norm.

### Norms and the joint spectral radius

As we mentioned, there exists an intimate relationship between the spectral radius and the existence of a vector norm under which all the matrices are simultaneously contractive. This is summarized in the following theorem, a special case of Proposition 1 by Rota and Strang.

### Theorem 2.1

Consider a finite set of matrices $\mathcal{A} = {\{ A_{1},\ldots,A_{m}\}}$. For any $\epsilon > 0$, there exists a norm $\parallel \cdot \parallel$ in ${\mathbb{R}}^{n}$ (denoted as JSR norm hereafter) such that The theorem appears in this form, for instance, in Proposition 4 of. The main idea in our approach is to replace the JSR norm that approximates the joint spectral radius with a homogeneous SOS polynomial $p{(x)}$ of degree $2d$. As we will see in the next sections, we can produce arbitrarily tight SOS approximations, while still being able to prove a bound on the resulting estimate.

### Joint spectral radius and polynomials

As the results presented above indicate, the joint spectral radius can be characterized by finding a common norm under which all the maps are simultaneously contractive. As opposed to the unit ball of a norm, the level sets of a homogeneous polynomial are not necessarily convex (see for instance Figure 1). Nevertheless, as the following theorem suggests, we can still obtain upper bounds on the joint spectral radius by replacing norms with homogeneous polynomials.

### Theorem 2.2

Let $p{(x)}$ be a strictly positive homogeneous polynomial of degree $2d$ that satisfies Then, ${\rho{(A_{1},\ldots,A_{m})}} \leq \gamma$.

### Proof

If $p{(x)}$ is strictly positive, then by compactness of the unit ball in ${\mathbb{R}}^{n}$ and continuity of $p{(x)}$, there exist constants $0 < \alpha \leq \beta$, such that From the definition of the joint spectral radius in equation, by taking $k$th roots and the limit $k\rightarrow\infty$ we immediately have the upper bound ${\rho{(A_{1},\ldots,A_{m})}} \leq \gamma$. ∎ The condition in Theorem 2.2 involves positive polynomials, which are computationally hard to characterize. A useful scheme, introduced in \[, \] and relatively well-known by now, relaxes the nonnegativity constraints to a much more tractable *sum of squares* (SOS) condition, where $p{(x)}$ is required to have a decomposition as ${p{(x)}} = {\sum_{i}{p_{i}{(x)}^{2}}}$. The SOS condition can be equivalently expressed in terms of a semidefinite programming (SDP) constraint. In what follows, we briefly describe the basic ideas behind SDP and sum of squares programming, and their applications to our problem.

### Semidefinite programming

SDP is a specific kind of convex optimization problem with very appealing numerical properties. An SDP problem corresponds to the optimization of a linear function over the intersection of an affine subspace and the cone of positive semidefinite matrices. For much more information about SDP and its many applications, we refer the reader to the surveys \[, \] and the comprehensive treatment.

An SDP problem in standard primal form is usually written as: | | ${minimize}\quad C \bullet$ | $X\quad$ | $\text{subject to}\quad{A_{i} \bullet X}$ | ${= b_{i}},{i = {1,\ldots,m}}$ | | where $C,A_{i}$ are symmetric $n \times n$ matrices, and ${X \bullet Y}:={{trace}{({XY})}}$. The symmetric matrix $X$ is the optimization variable over which the maximization is performed. The inequality in the second line means that the matrix $X$ must be positive semidefinite, i.e., all its eigenvalues should be greater than or equal to zero. The set of feasible solutions, i.e., the set of matrices $X$ that satisfy the constraints, is always a convex set. In the particular case when $C = 0$, the problem reduces to whether or not the inequality can be satisfied for some matrix $X$. In this case, the SDP is referred to as a *feasibility problem*.

There are a number of sophisticated and reliable methods to numerically solve semidefinite programming problems. One of the most successful approaches is based on *primal-dual interior point methods*, that generalize many of the techniques used in linear programming. The interior-point approach to SDP typically involves the iterative solution of a perturbed version of the KKT optimality conditions. Each iteration requires the computation of the corresponding Newton direction, and the solution of a system of linear equations. A theoretical bound on the number of Newton iterations is $O{({\sqrt{n}{\log\frac{1}{\epsilon}}})}$ for an $\epsilon$-approximate solution. This estimate is signficantly more conservative than what is usually experienced in practice, where the dependence on $n$ is very mild (typically, 10-40 Newton iterations are enough for most problems). The cost of each iteration heavily depends on the structure and sparsity of the matrices $A_{i}$, and is dominated by the computation of the Hessian and the solution of the corresponding linear system. In the fully dense case, this cost is of the order of $\max{\{{mn^{3}},{m^{2}n^{2}},m^{3}\}}$, where the first two terms correspond to the construction of the Hessian, and the last one to the solution of the Newton system.

### Sums of squares programming

Consider a given multivariate polynomial for which we want to decide whether a sum of squares decomposition exists. This question is equivalent to a semidefinite programming (SDP) problem, because of the following result, that has appeared in different forms in the work of Shor, Choi-Lam-Reznick, Nesterov, and Parrilo \[, \].

### Theorem 2.3

A homogeneous multivariate polynomial $p{(x)}$ of degree $2d$ is a sum of squares if and only if where $x^{\lbrack d\rbrack}$ is a vector whose entries are (possibly scaled) monomials of degree $d$ in the variables $x_{i}$, and $Q$ is a symmetric positive semidefinite matrix.

Since in general the entries of $x^{\lbrack d\rbrack}$ are not algebraically independent, the matrix $Q$ in the representation *is not unique*. In fact, there is an affine subspace of matrices $Q$ that satisfy the equality, as can be easily seen by expanding the right-hand side and equating term by term. To obtain an SOS representation, we need to find a positive semidefinite matrix in this affine subspace. Therefore, the problem of checking if a polynomial can be decomposed as a sum of squares is *equivalent* to verifying whether a certain affine matrix subspace intersects the cone of positive definite matrices, and hence an SDP feasibility problem.

### Example 2.4

Consider the quartic homogeneous polynomial in two variables described below, and define the vector of monomials as ${\lbrack x^{2},y^{2},{xy}\rbrack}^{T}$.

For the left- and right-hand sides to be identical, the following linear equations should hold: A positive semidefinite $Q$ that satisfies the linear equalities can then be found using SDP. A particular solution is given: and therefore we have the sum of squares decomposition:

### Norms and SOS polynomials

The procedure described in the previous subsection can be easily adapted to the case where the polynomial $p{(x)}$ is not fixed, but instead we search for an SOS polynomial in a given affine family (for instance, all homogeneous polynomials of a given degree).

This line of thought immediately suggests the following SOS relaxation of the conditions in Theorem 2.2: where ${\mathbb{R}}_{2d}{\lbrack x\rbrack}$ is the set of homogeneous polynomials of degree $2d$.

### Remark 2.5

Theorem 2.2 requires a strictly positive polynomial $p{(x)}$, so it would be natural to add some strict positivity condition to the relaxation. For instance, one could require for the polynomial $p{(x)}$ to belong to the relative interior of the SOS cone. However, since interior-point methods by construction always produce solutions in the relative interior of the corresponding convex set, this is automatically satisfied if the problem is feasible. Alternatively, it is possible to give a formulation that includes terms of the form $\epsilon{\| x\|}^{2d}$, for small positive $\epsilon$. These modifications are unnecessary in practice.

For any fixed degree $d$ and any given $\gamma$, the constraints in this problem are all of SOS type, and thus equivalent to semidefinite programming. Therefore, the computation of $\rho_{{SOS},{2d}}$ is a quasiconvex problem, and can be easily solved with a standard SDP solver, and a simple bisection method for the scalar variable $\gamma$. By Theorem 2.2, the solution of this relaxation yields an upper bound on the joint spectral radius where $2d$ is the degree of the approximating polynomial.

### Quality of approximation

What can be said about the quality of the bounds produced by the SOS relaxation? We present next some results to answer this question; a more complete characterization is developed in Section 3.1. An inspiring result in this direction is the following theorem of Barvinok, that quantifies how tightly SOS polynomials can approximate norms:

### Theorem 2.6 (, p. 221)

Let $|| \cdot ||$ be a norm in ${\mathbb{R}}^{n}$. For any integer $d \geq 1$ there exists a homogeneous polynomial $p{(x)}$ in $n$ variables of degree $2d$ such that The polynomial $p{(x)}$ is a sum of squares.

For all $x \in {\mathbb{R}}^{n}$, where ${k{(n,d)}}:=\binom{{n + d} - 1}{d}^{\frac{1}{2d}}$.

For fixed state dimension $n$, by increasing the degree $d$ of the approximating polynomials, the factor in the upper bound can be made arbitrarily close to one. In fact, for large $d$, we have the approximation To apply these results to our problem, consider the following. If ${\rho{(A_{1},\ldots,A_{m})}} < \gamma$, by Theorem 2.1. ‣ Norms and the joint spectral radius. ‣ 2 Bounds via polynomials and sums of squares ‣ Approximation of the joint spectral radius using sum of squares") (and sharper results in \[\]) there exists a norm $\parallel \cdot \parallel$ such that By Theorem 2.6. ‣ 2.2 Quality of approximation ‣ 2 Bounds via polynomials and sums of squares ‣ Approximation of the joint spectral radius using sum of squares"), we can therefore approximate this norm with a homogeneous SOS polynomial $p{(x)}$ of degree $2d$ that will then satisfy and thus we know that there exists a feasible solution of for $\alpha = {k{(n,d)}\rho{(A_{1},\ldots,A_{m})}}$.

Despite these appealing results, notice that in general we cannot yet conclude from this that the proposed SOS relaxation will always obtain a solution that is within $k{(n,d)}^{- 1}$ from the true spectral radius. The reason is that even though we can prove the existence of a $p{(x)}$ that is SOS and for which ${\alpha^{2d}p{(x)}} - {p{({A_{i}x})}}$ are nonnegative for all $i$, it is unclear whether the last $m$ expressions are actually SOS. We will show later in the paper that this is indeed the case. Before doing this, we concentrate first on two important cases of interest, where the described approach guarantees a good quality of approximation.

### Planar systems

The first case corresponds to two-dimensional (planar) systems, i.e., when $n = 2$. In this case, it always holds that nonnegative homogeneous bivariate polynomials are SOS (e.g., ). Thus, we have the following result:

### Theorem 2.7

Let ${\{ A_{1},\ldots,A_{m}\}} \subset {\mathbb{R}}^{2 \times 2}$. Then, the SOS relaxation always produces a solution satisfying: This result is *independent* of the number $m$ of matrices.

### Quadratic Lyapunov functions

In the quadratic case (i.e., ${2d} = 2$), it is also true that nonnegative quadratic forms are sums of squares. Since follows. This bound exactly coincides with the results of Ando and Shih or Blondel, Nesterov and Theys. This is perhaps not surprising, since in this case both Ando and Shih's proof and Barvinok's theorem rely on the use of John's ellipsoid to approximate the same underlying convex set.

### Level sets and convexity

Unlike the norms that appear in Theorem 2.1. ‣ Norms and the joint spectral radius. ‣ 2 Bounds via polynomials and sums of squares ‣ Approximation of the joint spectral radius using sum of squares"), an appealing feature of the SOS-based method is that we are not constrained to use polynomials with convex level sets. This enables in some cases much better bounds than what is promised by the theorems above, as illustrated in the following example.

Figure 1: Level sets of the quartic homogeneous polynomial V (x1, x2). These define a Lyapunov function, under which both A1 and A2 are (1 + ϵ)-contractive. The value of ϵ is here equal to 0.01.

### Example 2.8

This is based on a construction by Ando and Shih. Consider the problem of proving a bound on the joint spectral radius of the following matrices: For these matrices, it can be easily shown that ${\rho{(A_{1},A_{2})}} = 1$. Using a common quadratic Lyapunov function (i.e., the case $d = 2$), the upper bound on the joint spectral radius is equal to $\sqrt{2}$. However, a simple quartic SOS Lyapunov function is enough to prove an upper bound of $1 + \epsilon$ for every $\epsilon > 0$, since the SOS polynomial The corresponding level sets of $V{(x)}$ are plotted in Figure 1, and are clearly non-convex.

## Symmetric algebra and induced matrices

We present next some further bounds on the quality of the SOS relaxation, either by a more refined analysis of the SOS polynomials in Barvinok's theorem or by explicitly producing an SOS Lyapunov function of guaranteed suboptimality properties. These constructions are quite natural, and parallel some lifting ideas as well as the classical iteration used in the solution of discrete-time Lyapunov inequalities. Before proceeding further, we briefly revisit some classical notions from multilinear algebra.

### Symmetric algebra of a vector space

Consider a vector $x \in {\mathbb{R}}^{n}$, and an integer $d \geq 1$. We define its $d$-lift $x^{\lbrack d\rbrack}$ as a vector in ${\mathbb{R}}^{N}$, where $N:=\binom{{n + d} - 1}{d}$, with components ${\{{\sqrt{\alpha!}x^{\alpha}}\}}_{\alpha}$, where $\alpha = {(\alpha_{1},\ldots,\alpha_{n})}$, ${|\alpha|}:={\sum_{i}\alpha_{i}} = d$, and $\alpha!$ denotes the multinomial coefficient ${\alpha!}:=\binom{d}{\alpha_{1},\alpha_{2},\ldots,\alpha_{n}} = \frac{d!}{{\alpha_{1}!}{\alpha_{2}!}\ldots{\alpha_{n}!}}$. That is, the components of the lifted vector are the monomials of degree $d$, scaled by the square root of the corresponding multinomial coefficients.

### Example 3.1

Let $n = 2$, and $x = {\lbrack u,v\rbrack}^{T}$. Then, we have The main motivation for this specific scaling of the components, is to ensure that the lifting preserves some of the properties of the underlying normed space. In particular, if $|| \cdot ||$ denotes the standard Euclidean norm, it can be easily verified that ${\| x^{\lbrack d\rbrack}\|} = {\| x\|}^{d}$. Thus, the lifting operation provides a norm-preserving (up to power) embedding of ${\mathbb{R}}^{n}$ into ${\mathbb{R}}^{N}$. When the original space is projective, this is the so-called *Veronese* embedding.

This concept can be directly extended from vectors to linear transformations. Consider a linear map in ${\mathbb{R}}^{n}$, and the associated $n \times n$ matrix $A$. Then, the lifting described above naturally induces an associated map in ${\mathbb{R}}^{N}$, that makes the corresponding diagram commute. The matrix representing this linear transformation is the *$d$-th induced matrix* of $A$, denoted by $A^{\lbrack d\rbrack}$, which is the unique $N \times N$ matrix that satisfies In systems and control, these classical constructions of multilinear algebra have been used under different names in several works, among them \[, \] and (implicitly). Although not mentioned in the Control literature, there exists a simple explicit formula for the entries of these induced matrices; see \[, \]. The $d$-th induced matrix $A^{\lbrack d\rbrack}$ has dimensions $N \times N$. Its entries are given by where the indices $\alpha,\beta$ are all the $d$-element multisets of $\{ 1,\ldots,n\}$, the notation $per$ indicates the *permanent*^11^1The permanent of a matrix $A \in {\mathbb{R}}^{n \times n}$ is defined as ${\text{per}{(A)}}:={\sum_{\sigma \in \Pi_{n}}{\prod_{i = 1}^{n}a_{i,{\sigma{(i)}}}}}$, where $\Pi_{n}$ is the set of all permutations in $n$ elements. of a square matrix, and $\mu{(S)}$ is the product of the factorials of the multiplicities of the elements of the multiset $S$.

### Example 3.2

Consider the case $n = 2$, $d = 3$. The corresponding 3-element multisets are $\{ 1,1,1\}$, $\{ 1,1,2\}$, $\{ 1,2,2\}$ and $\{ 2,2,2\}$. The third induced matrix is then It can be shown that these operations define an algebra homomorphism, i.e., they respect the structure of matrix multiplication. In particular, for any matrices $A,B$ of compatible dimensions, the following identities hold: Furthermore, there is a simple and appealing relationship between the eigenvalues of $A^{\lbrack d\rbrack}$ and those of $A$. Concretely, if $\lambda_{1},\ldots,\lambda_{n}$ are the eigenvalues of $A$, then the eigenvalues of $A^{\lbrack d\rbrack}$ are given by $\prod_{j \in S}\lambda_{j}$ where ${S \subseteq {\{ 1,\ldots,n\}}},{{|S|} = d}$; there are exactly $\binom{{n + d} - 1}{d}$ such multisets. A similar relationship holds for the corresponding eigenvectors. Essentially, as explained below in more detail, the induced matrices are the symmetry-reduced version of the $d$-fold Kronecker product.

The symmetric algebra and associated induced matrices are classical objects of multilinear algebra. Induced matrices, as defined above, as well as the more usual *compound matrices*, correspond to two specific isotypic components of the decomposition of the $d$-fold tensor product under the action of the symmetric group $S^{d}$ (i.e., the *symmetric* and *skew-symmetric* algebras). Compound matrices are associated with the alternating character (hence their relationship with determinants), while induced matrices correspond instead to the trivial character, thus the connection with permanents. Similar constructions can be given for any other character of the symmetric group, by replacing the permanent in with the suitable immanants; see for additional details.

### Bounds on the quality of $\rho_{{SOS},{2d}}$

In this section we present a bound on the approximation properties of the SOS approximation, based on the ideas introduced above. As we will see, the techniques based on the lifting described will exactly yield the factor $k{(n,d)}^{- 1}$ suggested by Barvinok's theorem.

We first prove a preliminary result on the behavior of the joint spectral radius under $d$-lifting. The scaling properties described earlier can be applied to obtain the following:

### Lemma 3.3

Given matrices ${\{ A_{1},\ldots,A_{m}\}} \subset {\mathbb{R}}^{n \times n}$ and an integer $d \geq 1$, the following identity holds: The proof follows directly from the definition and the two properties ${({AB})}^{\lbrack d\rbrack} = {A^{\lbrack d\rbrack}B^{\lbrack d\rbrack}}$, ${\| x^{\lbrack d\rbrack}\|} = {\| x\|}^{d}$, and it is thus omitted.

Combining all these inequalities, we obtain the main result of this paper:

### Theorem 3.4

The SOS relaxation satisfies:

### Proof

Since the dimension of $A_{i}^{\lbrack d\rbrack}$ is $\binom{{n + d} - 1}{d}$, from Lemma 3.3 and inequality it follows that: Combining this with and the inequality (proven later in Theorem 13), the result follows. ∎

## Sum of squares Lyapunov iteration

We describe next an alternative approach to obtain bounds on the quality of the SOS approximation. As opposed to the results in the previous section, the bounds now explicitly depend on the number of matrices, but will usually be tighter in the case of small $m$.

Consider the iteration defined by where $Q{(x)}$ is a fixed $n$-variate homogeneous polynomial of degree $2d$ and $\beta > 0$. The iteration defines an affine map in the space of homogeneous polynomials of degree $2d$. As usual, the iteration will converge under certain assumptions on the spectral radius of this linear operator.

### Theorem 4.1

The iteration defined in converges for arbitrary $Q{(x)}$ if ${\rho{({A_{1}^{\lbrack{2d}\rbrack} + \cdots + A_{m}^{\lbrack{2d}\rbrack}})}} < \beta$.

### Proof

The vector space of homogenous polynomials ${\mathbb{R}}_{2d}{\lbrack x_{1},\ldots,x_{n}\rbrack}$ is naturally isomorphic to the space of linear functionals on ${({\mathbb{R}}^{n})}^{\lbrack{2d}\rbrack}$, via the identification ${V_{k}{(x)}} = {\langle v_{k},x^{\lbrack{2d}\rbrack}\rangle}$, where $v_{k} \in {\mathbb{R}}^{(\binom{{n + {2d}} - 1}{2d})}$ is the vector of (scaled) coefficients of $V_{k}{(x)}$. Then, since ${V_{k}{({A_{i}x})}} = {\langle v_{k},{({A_{i}x})}^{\lbrack{2d}\rbrack}\rangle} = {\langle v_{k},{A_{i}^{\lbrack{2d}\rbrack}x^{\lbrack{2d}\rbrack}}\rangle} = {\langle{{(A_{i}^{\lbrack{2d}\rbrack})}^{T}v_{k}},x^{\lbrack{2d}\rbrack}\rangle}$, the iteration can be simply expressed as: and it is well known that an affine iteration converges if the spectral radius of the linear term is less than one. ∎ For simplicity of notation, we define the following quantity, corresponding to the spectral radius of the sum of the $2d$-lifted matrices:

### Theorem 4.2

The following inequality holds:

### Proof

Choose a $Q{(x)}$ that is in the interior of the SOS cone, e.g., ${Q{(x)}}:={({\sum_{i = 1}^{n}x_{i}^{2}})}^{d}$, and let $\beta = {{\rho{({A_{1}^{\lbrack{2d}\rbrack} + \cdots + A_{m}^{\lbrack{2d}\rbrack}})}} + \epsilon}$. The iteration guarantees that $V_{k + 1}$ is SOS if $V_{k}$ is. By induction, all the iterates $V_{k}$ are SOS. By the choice of $\beta$ and Theorem 4.1, the $V_{k}$ converge to some homogeneous polynomial $V_{\infty}{(x)}$. By the closedness of the cone of SOS polynomials, the limit $V_{\infty}$ is also SOS. Furthermore, we have and therefore the expression on the left-hand side is SOS. This implies that ${p{(x)}}:={V_{\infty}{(x)}}$ is a feasible solution of the SOS relaxation. Taking $\epsilon\rightarrow 0$, the result follows. ∎ Notice that if the spectral radius condition in Theorem 4.1 is satisfied, then for any fixed $Q{(x)}$ the corresponding limit ${V_{\infty}{(x)}} = {\langle v_{\infty},x^{\lbrack{2d}\rbrack}\rangle}$ can be simply obtained by solving the nonsingular system of linear equations thus generalizing the standard Lyapunov equation. The iteration argument is only used to prove that the solution of this linear system yields a strictly positive SOS polynomial. A slightly different approach here is via the finite-dimensional version of the Krein-Rutman theorem (or generalized Perron-Frobenius); see for instance or.

### Theorem 4.3

The SOS relaxation satisfies:

### Proof

This follows directly from inequality, and the fact that where the first inequality is Theorem 4.2, the second one follows from the general fact that ${\rho{({A_{1} + \cdots + A_{m}})}} \leq {m\rho{(A_{1},\ldots,A_{m})}}$ (see e.g., Corollary 1), and the third from Lemma 3.3. ∎ The iteration is the natural generalization of the Lyapunov recursion for the single matrix case, and of the construction by Ando and Shih for the quadratic case. By the remarks in Section 3 above, and as described in more detail in the next section, it can be shown that the quantity $\rho_{{SR},{2d}}$ is essentially equal to those defined by Protasov in \[, §4\] and Blondel and Nesterov. As a consequence of Theorem 4.2, the SOS-based approach will *always* produce estimates at least as good as the ones given by these procedures.

## Comparison with earlier techniques

In this section we compare the $\rho_{{SOS},{2d}}$ approach with some earlier bounds from the literature. We show that our bound is never weaker than those obtained by all the other procedures.

### Methods of Protasov and Blondel-Nesterov

Protasov has shown that an upper bound on the "standard" joint spectral radius can be computed via the so-called joint $p$-radius, a generalization of the definition involving $p$-norms. Furthermore, he has shown that in the case of even integer $p$, the value of the $p$-radius of an irreducible finite set of matrices exactly corresponds to the spectral radius of a single operator, that can in principle be constructed based on the matrices $A_{i}$.

Independently, Blondel and Nesterov developed a technique based on the calculation of the spectral radius of "lifted" matrices. In fact, they present two different lifting procedures ("Kronecker" and "semidefinite" liftings), and in Section 5 of their paper, they describe a family of bounds obtained by arbitrary combinations of these two liftings.

Both of these methods are in fact equivalent to our construction of $\rho_{{SR},{2d}}$ in Section 4, in the sense that they all yield exactly the same numerical value. By Theorem 4.2, they are thus also weaker than the SOS-based construction. The bound defined by $\rho_{{SR},{2d}}$ in relies on a single canonically defined lifting, and requires much less numerical effort than the Blondel-Nesterov construction. Furthermore, instead of the somewhat more complicated construction of Protasov, the expression of the entries of the lifted matrices are given by the simple formula, making a computer implementation straightforward, with no irreducibility assumptions being required.

It can be shown that our construction (or Protasov's) exactly corresponds to a fully symmetry-reduced version of the Blondel-Nesterov procedure, thus yielding equivalent bounds, but at a much smaller computational cost since the corresponding matrices are exponentially smaller (for fixed $n$, the size grows as $O{(d^{n - 1})}$ as opposed to $O{(n^{2d})}$). Therefore, even if no SDPs are to be solved (as would be required by the tighter bound $\rho_{{SOS},{2d}}$), the formulation in terms of the matrices $A_{i}^{\lbrack{2d}\rbrack}$ still has many advantages.

Table 1: Comparison of matrix sizes for the different lifting procedures to compute ρS R, 2 d. The matrix size for the Kronecker lifting is n2 d, while the recursive semidefinite lifting is given by the d-step recursion $s_{2k} = \binom{s_{k} + 1}{2}$ with s1 = n, and the size for the symmetric algebra approach is $\binom{{n + {2d}} - 1}{2d}$. The accuracy estimates correspond to the case of two matrices, i.e., m = 2.

As an illustrative comparison of the advantages of this reduced formulation, in Table 1 we present the sizes of the matrices required by the method (using the "Kronecker" and "recursive semidefinite" liftings) and our approach to $\rho_{{SR},{2d}}$ via the symmetric algebra. The data in Table 1 corresponds to that in \[, p. 266\] (with a minor misprint corrected).

### Common quadratic Lyapunov functions

This method corresponds to finding a common quadratic Lyapunov function, either directly for the matrices $A_{i}$, or for the lifted matrices $A_{i}^{\lbrack d\rbrack}$. Specifically, let This is essentially equivalent to what is discussed in Corollary 3 of, except that the matrices involved in our approach are exponentially smaller (of size $\binom{{n + d} - 1}{d}$ rather than $n^{d}$), as all the symmetries have been taken out^22^2There seems to be a typo in equation (7.4) of, as all the terms $A_{i}^{k}$ should likely read $A_{i}^{\otimes k}$.. Notice also that, as a consequence of their definitions, we have We can then collect most of these results in a single theorem:

### Theorem 5.1

The following inequalities between all the bounds hold:

### Proof

The left-most inequality is. The right-most inequality follows from a similar (but stronger) argument to the one given in Theorem 4.2 above, since the spectral radius condition ${\rho{({A_{1}^{\lbrack{2d}\rbrack} + \cdots + A_{m}^{\lbrack{2d}\rbrack}})}} < \beta$ actually implies the convergence of the matrix iteration in $\mathcal{S}^{N}$ given by For the middle inequality, let ${p{(x)}}:={{(x^{\lbrack d\rbrack})}^{T}Px^{\lbrack d\rbrack}}$. Since $P \succ 0$, it follows that $p{(x)}$ is SOS. From ${{\gamma^{2d}P} - {{(A_{i}^{\lbrack d\rbrack})}^{T}PA_{i}^{\lbrack d\rbrack}}} \succeq 0$, left- and right-multiplying by $x^{\lbrack d\rbrack}$, we have that ${\gamma^{2d}p{(x)}} - {p{({A_{i}x})}}$ is also SOS, and thus $p{(x)}$ is a feasible solution of, from where the result directly follows. ∎

### Remark 5.2

We always have $\rho_{{SOS},2} = \rho_{{CQ},2}$, since both correspond to the case of a common quadratic Lyapunov function for the matrices $A_{i}$.

### Computational cost

In this section we quantify the computational cost of the bound $\rho_{{SOS},{2d}}$. In the following calculations we keep $d$ fixed, and study the scaling behavior as a function of the dimension $n$.

As mentioned in Section 2, solving a semidefinite programming problem typically requires several Newton iterations, with the cost of each iteration being dominated by the construction of the Hessian and solution of the corresponding linear system. For the SOS bound $\rho_{{SOS},{2d}}$, the underlying SDP problem has $m + 1$ matrix inequalities corresponding to the SOS constraints , each of dimension $\binom{{n + d} - 1}{d} \approx {\frac{1}{d!} \cdot n^{d}}$, which is $O{(n^{d})}$ for fixed $d$. The number of decision variables is approximately ${m \cdot \binom{{n + {2d}} - 1}{2d}} \approx {m \cdot n^{2d}}$. Thus, using a simple bisection method for $\gamma$, exploiting the block-diagonal structure, and the fact that the number of Newton iterations is essentially constant, we obtain that the approximate cost of obtaining an $\epsilon$-approximate solution of $\rho_{{SOS},{2d}}$ is $O{({m \cdot n^{6d} \cdot {\log\frac{1}{\epsilon}}})}$, where $d$ is chosen such that $\epsilon \approx {\frac{n}{2}\frac{\log d}{d}}$ or $\epsilon \approx m^{- \frac{1}{2d}}$, depending on whether we use bounds that depend on the number of matrices (Theorem 4.3) or not (Theorem 10).

We remark that these quantities are a relatively coarse estimate of the best possible algorithmic complexity, since very little structure of the corresponding SDP problem is being exploited. It is known that for structured problems such as the ones appearing here much more efficient SDP-based algorithms can be developed. In particular, in the context of sum of squares problems several techniques are known to exploit some of the available structure for more efficient computation; see \[ \].

### Examples

We present next two numerical examples that compare the described techniques. In particular, we show that the bounds in Theorem 13 can all be strict.

### Example 5.3

Here we revisit the construction presented earlier in Example 2.8. For the matrices given there we have: | | $\rho_{{SOS},4}$ | ${= 1},$ | $\rho_{{CQ},4}$ | ${= 1}.$ | |

### Example 5.4

Consider the three $4 \times 4$ matrices (randomly generated) given: The value of the different approximations are presented in Table 2. A lower bound is ${\rho{({A_{1}A_{3}})}^{\frac{1}{2}}} \approx 8.9149$, which is extremely close (and perhaps exactly equal) to the upper bound $\rho_{{SOS},4}$. Notice from the $d = 2$ entry of Table 2 that all the inequalities can be strict.

Table 2: Comparison of the different approximations for Example 5.4.

## Conclusions

We introduced a novel scheme for the approximation of the joint spectral radius of a set of matrices using sum of squares programming. The method is based on the use of a multivariate polynomial to provide a norm-like quantity under which all matrices are contractive. We provided an asymptotically tight estimate for the quality of the bound, which is independent of the number of matrices. We also proposed an alternative bound, that depends on the number $m$ of matrices, based on a generalization of a Lyapunov iteration.

Our results can be alternatively interpreted in a simpler way as providing a trajectory-preserving lifting to a higher dimensional space, and proving contractiveness with respect to an ellipsoidal norm in that space. In this case, a weaker estimate can be obtained by computing the spectral radius of a fixed matrix. These results generalize earlier work of Ando and Shih, Blondel, Nesterov and Theys, and provide an improvement over the lifting procedure of Blondel and Nesterov. The good performance of our procedure was also verified using numerical examples.
