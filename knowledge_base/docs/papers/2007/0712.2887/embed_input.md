<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Approximation of the Joint Spectral Radius Using Sum of Squares

Topics include Joint spectral radius, Sum of squares, Lyapunov functions, Semidefinite programming, Switched systems, Approximation bounds.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Uses sum-of-squares polynomial Lyapunov functions to approximate the joint spectral radius of a set of matrices. The paper gives asymptotically tight approximation bounds and connects computational SDP relaxations to stability analysis for switched systems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We provide an asymptotically tight, computationally efficient approximation of the joint spectral radius of a set of matrices using sum of squares (SOS) programming. The approach is based on a search for an SOS polynomial that proves simultaneous contractibility of a finite set of matrices. We provide a bound on the quality of the approximation that unifies several earlier results and is independent of the number of matrices. Additionally, we present a comparison between our approximation scheme and earlier techniques, including the use of common quadratic Lyapunov functions and a method based on matrix liftings. Theoretical results and numerical investigations show that our approach yields tighter approximations.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Stability of discrete linear inclusions has been a topic of major research over the past two decades. Such systems can be represented as a switched linear system of the form ${x{({k + 1})}} = {A_{\sigma{(k)}}x{(k)}}$, where $\sigma$ is a mapping from the integers to a given set of indices. The above model, and its many variations, has been studied extensively across multiple disciplines including control theory, theory of non-negative matrices and Markov chains, subdivision schemes and wavelet theory, dynamical systems, etc. The fundamental question of interest is to determine whether $x{(k)}$ converges to a limit, or equivalently, whether the infinite matrix products chosen from the set of matrices converge. The research on convergence of infinite products of matrices spans across four decades. A majority of results in this area has been provided in the special case of non-negative and/or stochastic matrices. A non-exhaustive list of related research providing several necessary and sufficient conditions for convergence of infinite products and their applications includes.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the wealth of research in this area, finding algorithms that can unambiguously decide convergence remains elusive. Much of the difficulty of this problem stems from the hardness in computation or efficient approximation of the joint spectral radius of a finite set of matrices. This notion was introduced by Rota and Strang via the definition

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

and represents the maximum growth rate that can be achieved by taking arbitrary products of the matrices $A_{i}$. As in the case of the classical spectral radius, the value of this expression is independent of the choice of norm. Daubechies and Lagarias conjectured that the joint spectral radius is equal to a related quantity, the generalized spectral radius, which is defined in a similar way except for the fact that the norm of the product is replaced by the spectral radius. Berger and Wang proved this conjecture to be true for finite sets of matrices. Blondel and Tsitsiklis have shown that computing $\rho$ is hard from a computational complexity viewpoint, and even approximating it is difficult. In particular, it follows from their results that the problem "Is $\rho \leq 1$?" is undecidable. For rational matrices, the joint spectral radius is not a semialgebraic function of the data, thus ruling out a very large class of methods for its exact computation. We refer the reader to the survey \[, §3.5\] for further results and references on the computational complexity of the joint spectral radius.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

It turns out that a necessary and sufficient condition for the stability of a linear difference inclusion is for the corresponding matrices to have a subunit joint spectral radius, i.e., ${\rho{(A_{1},\ldots,A_{m})}} < 1$; see e.g. \[, Thm. 1\] and. A subunit joint spectral radius is equivalent to the existence of a common norm with respect to which all matrices in the set are contractive; unfortunately, this common norm is in general not finitely constructible. In fact a similar result, due to Dayawansa and Martin, holds for nonlinear systems that undergo switching. A popular approach towards approximating the joint spectral radius or showing that it is indeed subunit has been to try to prove simultaneous contractibility (i.e., existence of a common norm with respect to which matrices are contractive), by searching for a common ellipsoidal norm, or equivalently, a common quadratic Lyapunov function. The benefit of this approach is due to the fact that the search for a common ellipsoidal norm can be posed as a semidefinite program and solved efficiently using interior point techniques.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, it is not too difficult to generate examples where the discrete inclusion is absolutely asymptotically stable, i.e., asymptotically stable for all switching sequences, but a common quadratic Lyapunov function, (or equivalently a common ellipsoidal norm) does not exist.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Ando and Shih describe a constructive procedure for generating a set of $m$ matrices whose joint spectral radius is equal to $\frac{1}{\sqrt{m}}$, but for which no quadratic Lyapunov function exists. They prove that the interval $\lbrack 0,\frac{1}{\sqrt{m}})$ is effectively the "optimal" range for the joint spectral radius necessary to guarantee simultaneous contractibility under an ellipsoidal norm for a finite collection of $m$ matrices. The range is denoted as optimal since it is the largest subset of $\lbrack 0,1)$ for which if the joint spectral radius is in this subset the collection of matrices is simultaneously contractible under an ellipsoidal norm. Furthermore, they show that the optimal joint spectral radius range for a bounded set of $n \times n$ matrices is the interval $\lbrack 0,\frac{1}{\sqrt{n}})$. The proof of this fact is based on John's ellipsoid theorem.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Roughly speaking, John's ellipsoid theorem implies that every convex body in $n$-dimensional Euclidean space that is symmetric with respect to the origin can be approximated by inner and outer ellipsoids, up to a factor of $\frac{1}{\sqrt{n}}$. Independently, Blondel, Nesterov and Theys showed a similar result (also based on John's ellipsoid theorem), that the best ellipsoidal norm approximation of the joint spectral radius provides a lower bound and an upper bound on the actual value. Given a set $\mathcal{M}$ of $n \times n$ matrices with joint spectral radius $\rho$, and best ellipsoidal norm approximation $\hat{\rho}$, it is shown there that

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

A major consequence of these results is that finding a common Lyapunov function becomes increasingly hard as the dimension goes up.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

There have been a number of earlier works proposing different numerical techniques for the effective computation of bounds on the joint spectral radius. A natural class of lower bounds is obtained by considering periodic switching sequences, in which case only a finite number of matrix norms need to be computed. Using a naive approach, the required computational efforts grow exponentially as $m^{k}$, where $k$ is the period of the sequence. Due to the cyclic property of the spectral radius, some terms are redundant, and Maesumi has shown using combinatorial techniques that the number of required products can be reduced to $m^{k}/k$. Another approach is the work of Gripenberg, who has introduced a branch-and-bound algorithm to produce upper and lower bounds on the joint spectral radius. Protasov has developed a geometric method to approximate this quantity, based on a polytopic approximation of a convex set that is invariant under the action of the linear operators $A_{i}$. This method has also been extended to the computation of the so-called $p$-radius.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

More recently, Blondel and Nesterov have proposed an alternative scheme to the computation of the joint spectral radius, by "lifting" the matrices using Kronecker products to provide better approximations. A common feature in many of these approaches is the presence of convexity-based methods to provide certificates of the desired system properties.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we develop a sum of squares (SOS) based scheme for the approximation of the joint spectral radius. The method computes, using the techniques of semidefinite programming, a homogeneous polynomial that serves as a Lyapunov-like function for the corresponding switched linear system. We prove several results on the quality of approximation of the proposed scheme. In particular, it will follow from Theorems 10 and 4.3 that our SOS-based approximation $\rho_{{SOS},{2d}}$ satisfies

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $\eta:={\min{\{ m,\binom{{n + d} - 1}{d}\}}}$. To prove this, we use two different techniques, one inspired by recent results of Barvinok on approximation of norms by polynomials, and the other one based on a convergent iteration similar to that used for Lyapunov inequalities. Our results provide a simple and unified derivation of most of the available bounds, including some new ones. We prove that the SOS-based approximation is always tighter than that obtained by the use of common quadratic Lyapunov functions, and than the one provided by Blondel and Nesterov. Furthermore, we show how to compute the bound using matrices that are exponentially smaller than those proposed there; this result also follows from the earlier work of Protasov. A preliminary version of some of our results has been presented.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

A description of the paper follows. In Section 2 we present a class of bounds on the joint spectral radius based on simultaneous contractivity with respect to a norm, followed by a sum of squares-based relaxation, and the corresponding suboptimality properties. In Section 3 we present some background material in multilinear algebra, necessary for our developments, and a derivation of a bound of the quality of the SOS relaxation. An alternative development is presented in Section 4, where a different bound on the performance of the SOS relaxation is given in terms of a very natural Lyapunov iteration, similar to the classical case. In Section 5 we make a comparison with earlier techniques and analyze a numerical example. Finally, in Section 6 we present our conclusions.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Bounds via polynomials and sums of squares", "weight": 1.0} -->

A natural way of bounding the joint spectral radius is to find a common norm that guarantees certain contractiveness properties for all the matrices. In this section, we first revisit this characterization, and introduce our method of using SOS relaxations to approximate this common norm.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Norms and the joint spectral radius", "weight": 1.0} -->

As we mentioned, there exists an intimate relationship between the spectral radius and the existence of a vector norm under which all the matrices are simultaneously contractive. This is summarized in the following theorem, a special case of Proposition 1 by Rota and Strang.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Joint spectral radius and polynomials", "weight": 1.0} -->

As the results presented above indicate, the joint spectral radius can be characterized by finding a common norm under which all the maps are simultaneously contractive. As opposed to the unit ball of a norm, the level sets of a homogeneous polynomial are not necessarily convex (see for instance Figure 1). Nevertheless, as the following theorem suggests, we can still obtain upper bounds on the joint spectral radius by replacing norms with homogeneous polynomials.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Semidefinite programming", "weight": 1.0} -->

SDP is a specific kind of convex optimization problem with very appealing numerical properties. An SDP problem corresponds to the optimization of a linear function over the intersection of an affine subspace and the cone of positive semidefinite matrices. For much more information about SDP and its many applications, we refer the reader to the surveys and the comprehensive treatment.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Semidefinite programming", "weight": 1.0} -->

where $C,A_{i}$ are symmetric $n \times n$ matrices, and ${X \bullet Y}:={{trace}{({XY})}}$. The symmetric matrix $X$ is the optimization variable over which the maximization is performed. The inequality in the second line means that the matrix $X$ must be positive semidefinite, i.e., all its eigenvalues should be greater than or equal to zero. The set of feasible solutions, i.e., the set of matrices $X$ that satisfy the constraints, is always a convex set. In the particular case when $C = 0$, the problem reduces to whether or not the inequality can be satisfied for some matrix $X$. In this case, the SDP is referred to as a *feasibility problem*.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Semidefinite programming", "weight": 1.0} -->

There are a number of sophisticated and reliable methods to numerically solve semidefinite programming problems. One of the most successful approaches is based on *primal-dual interior point methods*, that generalize many of the techniques used in linear programming. The interior-point approach to SDP typically involves the iterative solution of a perturbed version of the KKT optimality conditions. Each iteration requires the computation of the corresponding Newton direction, and the solution of a system of linear equations. A theoretical bound on the number of Newton iterations is $O{({\sqrt{n}{\log\frac{1}{\epsilon}}})}$ for an $\epsilon$-approximate solution. This estimate is signficantly more conservative than what is usually experienced in practice, where the dependence on $n$ is very mild (typically, 10-40 Newton iterations are enough for most problems). The cost of each iteration heavily depends on the structure and sparsity of the matrices $A_{i}$, and is dominated by the computation of the Hessian and the solution of the corresponding linear system.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Semidefinite programming", "weight": 1.0} -->

In the fully dense case, this cost is of the order of $\max{\{{mn^{3}},{m^{2}n^{2}},m^{3}\}}$, where the first two terms correspond to the construction of the Hessian, and the last one to the solution of the Newton system.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Sums of squares programming", "weight": 1.0} -->

Consider a given multivariate polynomial for which we want to decide whether a sum of squares decomposition exists. This question is equivalent to a semidefinite programming (SDP) problem, because of the following result, that has appeared in different forms in the work of Shor, Choi-Lam-Reznick, Nesterov, and Parrilo.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Example 2.4", "weight": 1.0} -->

Consider the quartic homogeneous polynomial in two variables described below, and define the vector of monomials as ${\lbrack x^{2},y^{2},{xy}\rbrack}^{T}$.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Example 2.4", "weight": 1.0} -->

A positive semidefinite $Q$ that satisfies the linear equalities can then be found using SDP.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Norms and SOS polynomials", "weight": 1.0} -->

The procedure described in the previous subsection can be easily adapted to the case where the polynomial $p{(x)}$ is not fixed, but instead we search for an SOS polynomial in a given affine family (for instance, all homogeneous polynomials of a given degree).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Norms and SOS polynomials", "weight": 1.0} -->

This line of thought immediately suggests the following SOS relaxation of the conditions in Theorem 2.2:

<!-- chunk {"id": "body-0029", "role": "body", "section": "Norms and SOS polynomials", "weight": 1.0} -->

where ${\mathbb{R}}_{2d}{\lbrack x\rbrack}$ is the set of homogeneous polynomials of degree $2d$.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 2.5", "weight": 1.0} -->

Theorem 2.2 requires a strictly positive polynomial $p{(x)}$, so it would be natural to add some strict positivity condition to the relaxation. For instance, one could require for the polynomial $p{(x)}$ to belong to the relative interior of the SOS cone. However, since interior-point methods by construction always produce solutions in the relative interior of the corresponding convex set, this is automatically satisfied if the problem is feasible. Alternatively, it is possible to give a formulation that includes terms of the form $\epsilon{\| x\|}^{2d}$, for small positive $\epsilon$. These modifications are unnecessary in practice.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 2.5", "weight": 1.0} -->

For any fixed degree $d$ and any given $\gamma$, the constraints in this problem are all of SOS type, and thus equivalent to semidefinite programming. Therefore, the computation of $\rho_{{SOS},{2d}}$ is a quasiconvex problem, and can be easily solved with a standard SDP solver, and a simple bisection method for the scalar variable $\gamma$. By Theorem 2.2, the solution of this relaxation yields an upper bound on the joint spectral radius

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 2.5", "weight": 1.0} -->

where $2d$ is the degree of the approximating polynomial.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Quality of approximation", "weight": 1.0} -->

What can be said about the quality of the bounds produced by the SOS relaxation? We present next some results to answer this question; a more complete characterization is developed in Section 3.1.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Planar systems", "weight": 1.0} -->

The first case corresponds to two-dimensional (planar) systems, i.e., when $n = 2$. In this case, it always holds that nonnegative homogeneous bivariate polynomials are SOS (e.g., ).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Quadratic Lyapunov functions", "weight": 1.0} -->

In the quadratic case (i.e., ${2d} = 2$), it is also true that nonnegative quadratic forms are sums of squares. Since

<!-- chunk {"id": "body-0036", "role": "body", "section": "Quadratic Lyapunov functions", "weight": 1.0} -->

follows. This bound exactly coincides with the results of Ando and Shih or Blondel, Nesterov and Theys. This is perhaps not surprising, since in this case both Ando and Shih's proof and Barvinok's theorem rely on the use of John's ellipsoid to approximate the same underlying convex set.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Level sets and convexity", "weight": 1.0} -->

Unlike the norms that appear in Theorem 2.1. ‣ Norms and the joint spectral radius. ‣ 2 Bounds via polynomials and sums of squares ‣ Approximation of the joint spectral radius using sum of squares"), an appealing feature of the SOS-based method is that we are not constrained to use polynomials with convex level sets. This enables in some cases much better bounds than what is promised by the theorems above, as illustrated in the following example.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Example 2.8", "weight": 1.0} -->

This is based on a construction by Ando and Shih.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Example 2.8", "weight": 1.0} -->

For these matrices, it can be easily shown that ${\rho{(A_{1},A_{2})}} = 1$. Using a common quadratic Lyapunov function (i.e., the case $d = 2$), the upper bound on the joint spectral radius is equal to $\sqrt{2}$. However, a simple quartic SOS Lyapunov function is enough to prove an upper bound of $1 + \epsilon$ for every $\epsilon > 0$, since the SOS polynomial

<!-- chunk {"id": "body-0040", "role": "body", "section": "Example 2.8", "weight": 1.0} -->

The corresponding level sets of $V{(x)}$ are plotted in Figure 1, and are clearly non-convex.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Symmetric algebra and induced matrices", "weight": 1.0} -->

We present next some further bounds on the quality of the SOS relaxation, either by a more refined analysis of the SOS polynomials in Barvinok's theorem or by explicitly producing an SOS Lyapunov function of guaranteed suboptimality properties. These constructions are quite natural, and parallel some lifting ideas as well as the classical iteration used in the solution of discrete-time Lyapunov inequalities. Before proceeding further, we briefly revisit some classical notions from multilinear algebra.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Example 3.1", "weight": 1.0} -->

The main motivation for this specific scaling of the components, is to ensure that the lifting preserves some of the properties of the underlying normed space. In particular, if $|| \cdot ||$ denotes the standard Euclidean norm, it can be easily verified that ${\| x^{\lbrack d\rbrack}\|} = {\| x\|}^{d}$. Thus, the lifting operation provides a norm-preserving (up to power) embedding of ${\mathbb{R}}^{n}$ into ${\mathbb{R}}^{N}$. When the original space is projective, this is the so-called *Veronese* embedding.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Example 3.1", "weight": 1.0} -->

This concept can be directly extended from vectors to linear transformations. Consider a linear map in ${\mathbb{R}}^{n}$, and the associated $n \times n$ matrix $A$. Then, the lifting described above naturally induces an associated map in ${\mathbb{R}}^{N}$, that makes the corresponding diagram commute. The matrix representing this linear transformation is the *$d$-th induced matrix* of $A$, denoted by $A^{\lbrack d\rbrack}$, which is the unique $N \times N$ matrix that satisfies

<!-- chunk {"id": "body-0044", "role": "body", "section": "Example 3.1", "weight": 1.0} -->

In systems and control, these classical constructions of multilinear algebra have been used under different names in several works, among them and (implicitly). Although not mentioned in the Control literature, there exists a simple explicit formula for the entries of these induced matrices; see. The $d$-th induced matrix $A^{\lbrack d\rbrack}$ has dimensions $N \times N$. Its entries are given by

<!-- chunk {"id": "body-0045", "role": "body", "section": "Example 3.1", "weight": 1.0} -->

where the indices $\alpha,\beta$ are all the $d$-element multisets of $\{ 1,\ldots,n\}$, the notation $per$ indicates the *permanent*^11^1The permanent of a matrix $A \in {\mathbb{R}}^{n \times n}$ is defined as ${\text{per}{(A)}}:={\sum_{\sigma \in \Pi_{n}}{\prod_{i = 1}^{n}a_{i,{\sigma{(i)}}}}}$, where $\Pi_{n}$ is the set of all permutations in $n$ elements. of a square matrix, and $\mu{(S)}$ is the product of the factorials of the multiplicities of the elements of the multiset $S$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Example 3.2", "weight": 1.0} -->

Consider the case $n = 2$, $d = 3$. The corresponding 3-element multisets are $\{ 1,1,1\}$, $\{ 1,1,2\}$, $\{ 1,2,2\}$ and $\{ 2,2,2\}$. The third induced matrix is then

<!-- chunk {"id": "body-0047", "role": "body", "section": "Example 3.2", "weight": 1.0} -->

It can be shown that these operations define an algebra homomorphism, i.e., they respect the structure of matrix multiplication.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Example 3.2", "weight": 1.0} -->

Furthermore, there is a simple and appealing relationship between the eigenvalues of $A^{\lbrack d\rbrack}$ and those of $A$. Concretely, if $\lambda_{1},\ldots,\lambda_{n}$ are the eigenvalues of $A$, then the eigenvalues of $A^{\lbrack d\rbrack}$ are given by $\prod_{j \in S}\lambda_{j}$ where ${S \subseteq {\{ 1,\ldots,n\}}},{{|S|} = d}$; there are exactly $\binom{{n + d} - 1}{d}$ such multisets. A similar relationship holds for the corresponding eigenvectors. Essentially, as explained below in more detail, the induced matrices are the symmetry-reduced version of the $d$-fold Kronecker product.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Example 3.2", "weight": 1.0} -->

The symmetric algebra and associated induced matrices are classical objects of multilinear algebra. Induced matrices, as defined above, as well as the more usual *compound matrices*, correspond to two specific isotypic components of the decomposition of the $d$-fold tensor product under the action of the symmetric group $S^{d}$ (i.e., the *symmetric* and *skew-symmetric* algebras). Compound matrices are associated with the alternating character (hence their relationship with determinants), while induced matrices correspond instead to the trivial character, thus the connection with permanents. Similar constructions can be given for any other character of the symmetric group, by replacing the permanent in with the suitable immanants; see for additional details.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Bounds on the quality of $\\rho_{{SOS},{2d}}$", "weight": 1.0} -->

In this section we present a bound on the approximation properties of the SOS approximation, based on the ideas introduced above. As we will see, the techniques based on the lifting described will exactly yield the factor $k{(n,d)}^{- 1}$ suggested by Barvinok's theorem.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Bounds on the quality of $\\rho_{{SOS},{2d}}$", "weight": 1.0} -->

We first prove a preliminary result on the behavior of the joint spectral radius under $d$-lifting.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Sum of squares Lyapunov iteration", "weight": 1.0} -->

We describe next an alternative approach to obtain bounds on the quality of the SOS approximation. As opposed to the results in the previous section, the bounds now explicitly depend on the number of matrices, but will usually be tighter in the case of small $m$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Sum of squares Lyapunov iteration", "weight": 1.0} -->

where $Q{(x)}$ is a fixed $n$-variate homogeneous polynomial of degree $2d$ and $\beta > 0$. The iteration defines an affine map in the space of homogeneous polynomials of degree $2d$. As usual, the iteration will converge under certain assumptions on the spectral radius of this linear operator.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Comparison with earlier techniques", "weight": 1.0} -->

In this section we compare the $\rho_{{SOS},{2d}}$ approach with some earlier bounds from the literature. We show that our bound is never weaker than those obtained by all the other procedures.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Methods of Protasov and Blondel-Nesterov", "weight": 1.0} -->

Protasov has shown that an upper bound on the "standard" joint spectral radius can be computed via the so-called joint $p$-radius, a generalization of the definition involving $p$-norms. Furthermore, he has shown that in the case of even integer $p$, the value of the $p$-radius of an irreducible finite set of matrices exactly corresponds to the spectral radius of a single operator, that can in principle be constructed based on the matrices $A_{i}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Methods of Protasov and Blondel-Nesterov", "weight": 1.0} -->

Independently, Blondel and Nesterov developed a technique based on the calculation of the spectral radius of "lifted" matrices. In fact, they present two different lifting procedures ("Kronecker" and "semidefinite" liftings), and in Section 5 of their paper, they describe a family of bounds obtained by arbitrary combinations of these two liftings.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Methods of Protasov and Blondel-Nesterov", "weight": 1.0} -->

Both of these methods are in fact equivalent to our construction of $\rho_{{SR},{2d}}$ in Section 4, in the sense that they all yield exactly the same numerical value. By Theorem 4.2, they are thus also weaker than the SOS-based construction. The bound defined by $\rho_{{SR},{2d}}$ in relies on a single canonically defined lifting, and requires much less numerical effort than the Blondel-Nesterov construction. Furthermore, instead of the somewhat more complicated construction of Protasov, the expression of the entries of the lifted matrices are given by the simple formula, making a computer implementation straightforward, with no irreducibility assumptions being required.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Methods of Protasov and Blondel-Nesterov", "weight": 1.0} -->

It can be shown that our construction (or Protasov's) exactly corresponds to a fully symmetry-reduced version of the Blondel-Nesterov procedure, thus yielding equivalent bounds, but at a much smaller computational cost since the corresponding matrices are exponentially smaller (for fixed $n$, the size grows as $O{(d^{n - 1})}$ as opposed to $O{(n^{2d})}$). Therefore, even if no SDPs are to be solved (as would be required by the tighter bound $\rho_{{SOS},{2d}}$), the formulation in terms of the matrices $A_{i}^{\lbrack{2d}\rbrack}$ still has many advantages.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Methods of Protasov and Blondel-Nesterov", "weight": 1.0} -->

As an illustrative comparison of the advantages of this reduced formulation, in Table 1 we present the sizes of the matrices required by the method (using the "Kronecker" and "recursive semidefinite" liftings) and our approach to $\rho_{{SR},{2d}}$ via the symmetric algebra. The data in Table 1 corresponds to that in \[, p. 266\] (with a minor misprint corrected).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Common quadratic Lyapunov functions", "weight": 1.0} -->

This method corresponds to finding a common quadratic Lyapunov function, either directly for the matrices $A_{i}$, or for the lifted matrices $A_{i}^{\lbrack d\rbrack}$. Specifically, let

<!-- chunk {"id": "body-0061", "role": "body", "section": "Common quadratic Lyapunov functions", "weight": 1.0} -->

This is essentially equivalent to what is discussed in Corollary 3 of, except that the matrices involved in our approach are exponentially smaller (of size $\binom{{n + d} - 1}{d}$ rather than $n^{d}$), as all the symmetries have been taken out^22^2There seems to be a typo in equation (7.4) of, as all the terms $A_{i}^{k}$ should likely read $A_{i}^{\otimes k}$.. Notice also that, as a consequence of their definitions, we have

<!-- chunk {"id": "body-0062", "role": "body", "section": "Remark 5.2", "weight": 1.0} -->

We always have $\rho_{{SOS},2} = \rho_{{CQ},2}$, since both correspond to the case of a common quadratic Lyapunov function for the matrices $A_{i}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Computational cost", "weight": 1.0} -->

In this section we quantify the computational cost of the bound $\rho_{{SOS},{2d}}$. In the following calculations we keep $d$ fixed, and study the scaling behavior as a function of the dimension $n$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Computational cost", "weight": 1.0} -->

As mentioned in Section 2, solving a semidefinite programming problem typically requires several Newton iterations, with the cost of each iteration being dominated by the construction of the Hessian and solution of the corresponding linear system. For the SOS bound $\rho_{{SOS},{2d}}$, the underlying SDP problem has $m + 1$ matrix inequalities corresponding to the SOS constraints, each of dimension $\binom{{n + d} - 1}{d} \approx {\frac{1}{d!} \cdot n^{d}}$, which is $O{(n^{d})}$ for fixed $d$. The number of decision variables is approximately ${m \cdot \binom{{n + {2d}} - 1}{2d}} \approx {m \cdot n^{2d}}$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Computational cost", "weight": 1.0} -->

Thus, using a simple bisection method for $\gamma$, exploiting the block-diagonal structure, and the fact that the number of Newton iterations is essentially constant, we obtain that the approximate cost of obtaining an $\epsilon$-approximate solution of $\rho_{{SOS},{2d}}$ is $O{({m \cdot n^{6d} \cdot {\log\frac{1}{\epsilon}}})}$, where $d$ is chosen such that $\epsilon \approx {\frac{n}{2}\frac{\log d}{d}}$ or $\epsilon \approx m^{- \frac{1}{2d}}$, depending on whether we use bounds that depend on the number of matrices (Theorem 4.3) or not (Theorem 10).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Computational cost", "weight": 1.0} -->

We remark that these quantities are a relatively coarse estimate of the best possible algorithmic complexity, since very little structure of the corresponding SDP problem is being exploited. It is known that for structured problems such as the ones appearing here much more efficient SDP-based algorithms can be developed. In particular, in the context of sum of squares problems several techniques are known to exploit some of the available structure for more efficient computation; see.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Examples", "weight": 1.0} -->

We present next two numerical examples that compare the described techniques. In particular, we show that the bounds in Theorem 13 can all be strict.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Example 5.3", "weight": 1.0} -->

Here we revisit the construction presented earlier in Example 2.8.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Example 5.4", "weight": 1.0} -->

The value of the different approximations are presented in Table 2. A lower bound is ${\rho{({A_{1}A_{3}})}^{\frac{1}{2}}} \approx 8.9149$, which is extremely close (and perhaps exactly equal) to the upper bound $\rho_{{SOS},4}$. Notice from the $d = 2$ entry of Table 2 that all the inequalities can be strict.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We introduced a novel scheme for the approximation of the joint spectral radius of a set of matrices using sum of squares programming. The method is based on the use of a multivariate polynomial to provide a norm-like quantity under which all matrices are contractive. We provided an asymptotically tight estimate for the quality of the bound, which is independent of the number of matrices. We also proposed an alternative bound, that depends on the number $m$ of matrices, based on a generalization of a Lyapunov iteration.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Conclusions", "weight": 1.0} -->

Our results can be alternatively interpreted in a simpler way as providing a trajectory-preserving lifting to a higher dimensional space, and proving contractiveness with respect to an ellipsoidal norm in that space. In this case, a weaker estimate can be obtained by computing the spectral radius of a fixed matrix. These results generalize earlier work of Ando and Shih, Blondel, Nesterov and Theys, and provide an improvement over the lifting procedure of Blondel and Nesterov. The good performance of our procedure was also verified using numerical examples.
