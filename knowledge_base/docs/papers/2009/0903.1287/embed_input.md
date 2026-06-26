<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Convex Polynomial That Is Not sos-convex

Topics include Convex polynomials, Sos-convexity, Sum of squares, Semidefinite programming, Polynomial optimization, Counterexamples.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Constructs a convex polynomial that is not Sos-convex, separating ordinary convexity from the Sos-verifiable sufficient condition. The counterexample is important for understanding the conservatism of semidefinite relaxations in polynomial optimization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

A multivariate polynomial p(x)=p(x_1,...,x_n) is sos-convex if its Hessian H(x) can be factored as H(x)=M^T(x)M(x) with a possibly nonsquare polynomial matrix M(x). It is easy to see that sos-convexity is a sufficient condition for convexity of p(x). Moreover, the problem of deciding sos-convexity of a polynomial can be cast as the feasibility of a semidefinite program, which can be solved efficiently. Motivated by this computational tractability, it has been recently speculated whether sos-convexity is also a necessary condition for convexity of polynomials. In this paper, we give a negative answer to this question by presenting an explicit example of a trivariate homogeneous polynomial of degree eight that is convex but not sos-convex. Interestingly, our example is found with software using sum of squares programming techniques and the duality theory of semidefinite optimization.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

As a byproduct of our numerical procedure, we obtain a simple method for searching over a restricted family of nonnegative polynomials that are not sums of squares.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In many problems in applied and computational mathematics, we would like to *decide* whether a multivariate polynomial is convex or to *parameterize* a family of convex polynomials. Perhaps the most obvious instance appears in optimization. It is well known that in the absence of convexity, global minimization of polynomials is generally NP-hard. However, if we somehow know a priori that the polynomial is convex, nonexistence of local minima is guaranteed, and simple gradient descent methods can find a global minimum. In many other practical settings, we might want to parameterize a family of convex polynomials that have certain properties, e.g., that serve as a convex envelope for a non-convex function, approximate a more complicated function, or fit some data points with minimum error. To address many questions of this type, we need to have an understanding of the algebraic structure of the set of convex polynomials.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Over a decade ago, Pardalos and Vavasis put the following question proposed by Shor on the list of seven most important open problems in complexity theory for numerical optimization: "Given a degree-$4$ polynomial in $n$ variables, what is the complexity of determining whether this polynomial describes a convex function?" To the best of our knowledge, the question remains open but the general belief is that the problem should be hard (see the related work in ). Not surprisingly, if testing membership to the set of convex polynomials is hard, searching and optimizing over them also turns out to be a hard problem.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

The notion of *sos-convexity* has recently been proposed as a tractable relaxation for convexity based on semidefinite programming. Broadly speaking, the requirement of positive semidefiniteness of the Hessian matrix is replaced with the existence of an appropriately defined sum of squares decomposition. As we will briefly review in this paper, by drawing some appealing connections between real algebra and numerical optimization, the latter problem can be reduced to the feasibility of a semidefinite program. Besides its computational implications, sos-convexity is an appealing concept since it bridges the *geometric* and *algebraic* aspects of convexity. Indeed, while the usual definition of convexity is concerned only with the geometry of the epigraph, in sos-convexity this geometric property (or the nonnegativity of the Hessian) must be *certified* through a "simple" algebraic identity, namely the sum of squares factorization of the Hessian.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Despite the relative recency of the concept of sos-convexity, it has already appeared in a number of theoretical and practical settings. In, Helton and Nie use sos-convexity to give sufficient conditions for semidefinite representability of semialgebraic sets. In, Lasserre uses sos-convexity to extend Jensen's inequality in convex analysis to linear functionals that are not necessarily probability measures, and to give sufficient conditions for a polynomial to belong to the quadratic module generated by a set of polynomials. More on the practical side, Magnani, Lall, and Boyd have used sum of squares programming to find sos-convex polynomials that best fit a set of data points or to find minimum volume convex sets, given by sub-level sets of sos-convex polynomials, that contain a set of points in space.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Even though it is well-known that sum of squares and nonnegativity are not equivalent, because of the special structure of the Hessian matrix, sos-convexity and convexity could potentially turn out to be equivalent. This speculation has been bolstered by the fact that finding a counterexample has shown to be difficult and attempts at giving a non-constructive proof of its existence have seen no success either. Our contribution in this paper is to give the first such counterexample, i.e., the first explicit example of a polynomial that is convex but not sos-convex. This example is presented in Theorem 3.2. Our result further supports the hypothesis that deciding convexity of polynomials should be a difficult problem. We hope that our counterexample, in a similar way to what other celebrated counterexamples have achieved, will help stimulate further research and clarify the relationships between the geometric and algebraic aspects of positivity and convexity.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The organization of the paper is as follows. Section 2 is devoted to mathematical preliminaries required for understanding the remainder of this paper. We begin this section by introducing the cone of nonnegative and sum of squares polynomials. We briefly discuss the connection between sum of squares decomposition and semidefinite programming highlighting also the dual problem. Formal definitions of sos-convex polynomials and sos-matrices are also given in this section. In Section 3, we present our main result, which is an explicit example of a convex polynomial that is not sos-convex. Finally, we explain in Section 4 how we have utilized sos-programming together with semidefinite programming duality theory to find the example presented in Section 3. We comment on how one can use the same methodology to search for a restricted class of nonnegative polynomials that are not sos.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Nonnegativity and sum of squares", "weight": 1.0} -->

We denote by ${\mathbb{K}}{\lbrack x\rbrack}: = {\mathbb{K}}{\lbrack x_{1},\ldots,x_{n}\rbrack}$ the ring of polynomials in $n$ variables with coefficients in the field $\mathbb{K}$. Throughout the paper, we will have ${\mathbb{K}} = {\mathbb{R}}$ or ${\mathbb{K}} = {\mathbb{Q}}$. A polynomial ${p{(x)}} \in {{\mathbb{R}}{\lbrack x\rbrack}}$ is said to be nonnegative or positive semidefinite (psd) if ${p{(x)}} \geq 0$ for all $x \in {\mathbb{R}}^{n}$. Clearly, a necessary condition for a polynomial to be psd is for its total degree to be even.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Nonnegativity and sum of squares", "weight": 1.0} -->

We say that $p{(x)}$ is a sum of squares (sos), if there exist polynomials ${q_{1}{(x)}},\ldots,{q_{m}{(x)}}$ such that It is clear that $p{(x)}$ being sos implies that $p{(x)}$ is psd. In 1888, David Hilbert proved that the converse is true for a polynomial in $n$ variables and of degree $d$ *only* in the following cases: $n = 1$ (univariate polynomials of any degree) $d = 2$ (quadratic polynomials in any number of variables) Hilbert showed that in all other cases there exist polynomials that are psd but not sos. Explicit examples of such polynomials appeared nearly 80 years later, starting with the celebrated example of Motzkin, followed by more examples by Robinson, Choi and Lam, and Lax-Lax and Schmüdgen. See for an outstanding exposition of these counterexamples.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Nonnegativity and sum of squares", "weight": 1.0} -->

A polynomial $p{(x)}$ of degree $d$ in $n$ variables has $l = \binom{n + d}{d}$ coefficients and can therefore be identified with the $l$-tuple of its coefficients, which we denote by $\overset{\rightarrow}{p} \in {\mathbb{R}}^{l}$. A polynomial where all the monomials have the same degree is called a *form*. A form $p{(x)}$ of degree $d$ is a homogenous function of degree $d$ (since it satisfies ${p{({\lambdax})}} = {\lambda^{d}p{(x)}}$), and has $\binom{{n + d} - 1}{d}$ coefficients. The set of forms in $n$ variables of degree $d$ is denoted by $\mathcal{H}_{n,d}$.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Nonnegativity and sum of squares", "weight": 1.0} -->

It is easy to show that if a form of degree $d$ is sos, then $d$ is even, and the polynomials $q_{i}$ in the sos decomposition are forms of degree $d/2$. We also denote the set of psd (resp. sos) forms of degree $d$ in $n$ variables by $P_{n,d}$ (resp. $\Sigma_{n,d}$). Both $P_{n,d}$ and $\Sigma_{n,d}$ are closed convex cones, and we have the relation $\Sigma_{n,d} \subseteq P_{n,d} \subset \mathcal{H}_{n,d}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Nonnegativity and sum of squares", "weight": 1.0} -->

Any form of degree $d$ in $n$ variables can be dehomogenized into a polynomial of degree $\leq d$ in $n - 1$ variables by setting $x_{n} = 1$. Conversely, any polynomial $p$ of degree $d$ in $n$ variables can be homogenized into a form $p_{h}$ of degree $d$ in $n + 1$ variables, by adding a new variable $y$, and letting The properties of being psd and sos are preserved under homogenization and dehomogenization.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Nonnegativity and sum of squares", "weight": 1.0} -->

An important related problem is Hilbert's 17th problem, which asks if every psd form must be a sum of squares of rational functions. In 1927, Artin answered Hilbert's question in the affirmative. This result implies that if a polynomial $p{(x)}$ is psd, then there must exist an sos polynomial $g{(x)}$, such that $p{(x)}g{(x)}$ is sos. Moreover, Reznick showed in that if $p{(x)}$ is *positive definite*, one can always take ${g{(x)}} = {({\sum_{i}x_{i}^{2}})}^{r}$, for sufficiently large $r$. We will make use of this key fact in the derivation of our example.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Nonnegativity and sum of squares", "weight": 1.0} -->

To make the ideas presented so far more concrete, we end this section by discussing the example of Motzkin. Interestingly enough, this example will reappear in Section 4 where it serves as a starting point in the numerical procedure that leads to our example.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Example 2.1", "weight": 1.0} -->

The Motzkin polynomial is historically the first known example of a polynomial that is psd but not sos. Positive semidefiniteness follows from the arithmetic-geometric inequality, and the nonexistence of an sos decomposition can be shown by some clever algebraic manipulations (see for details). We can homogenize this polynomial and obtain the Motzkin form which belongs to $P_{3,6}\backslash\Sigma_{3,6}$ as expected. An alternative proof of nonnegativity of $M_{h}$ (resp. $M$) is obtained by showing that $M_{h}{(x)}{({x_{1}^{2} + x_{2}^{2} + x_{3}^{2}})}$ (resp. $M{(x)}{({x_{1}^{2} + x_{2}^{2} + 1})}$) is sos. An explicit sos decomposition can be found.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Example 2.1", "weight": 1.0} -->

In the sequel, we will explain how we can give an alternative proof of the fact that the Motzkin polynomial is not sos, by appealing to sos-programming duality.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Sum of squares, semidefinite programming, and duality", "weight": 1.0} -->

Deciding nonnegativity of polynomials is an important problem that arises in many areas of applied and computational mathematics. Unfortunately, this problem is known to be NP-hard even when the degree of the polynomial is equal to four,. On the other hand, deciding whether a given polynomial admits an sos decomposition turns out to be a tractable problem. This tractability stems from the underlying convexity of the problem as first pointed out. More specifically, it was shown in that one can reduce the problem of deciding whether a polynomial is sos to feasibility of a *semidefinite program* (SDP). Semidefinite programs are a well-studied subclass of convex optimization problems that can be efficiently solved in polynomial time using interior point algorithms. Because our space is limited, we refrain from further discussing SDPs and refer the interested reader to the review papers. The main theorem that establishes the link between sum of squares and semidefinite programming is the following.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Sum of squares matrices and sos-convexity", "weight": 1.0} -->

The notions of positive semidefiniteness and sum of squares of scalar polynomials can be naturally extended to polynomial matrices, i.e., matrices with entries in ${\mathbb{R}}{\lbrack x\rbrack}$. We say that a symmetric polynomial matrix ${P{(x)}} \in {{\mathbb{R}}{\lbrack x\rbrack}^{m \times m}}$ is PSD if $P{(x)}$ is PSD for all $x \in {\mathbb{R}}^{n}$. It is straightforward to see that this condition holds if and only if the polynomial $y^{T}H{(x)}y$ in $m + n$ variables $\lbrack x;y\rbrack$ is psd. The definition of an sos-matrix is as follows.

<!-- chunk {"id": "body-0022", "role": "body", "section": "A polynomial that is convex but not sos-convex", "weight": 1.0} -->

We start this section with a lemma that will appear in the proof of our main result.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Remark 3.1", "weight": 1.0} -->

The converse of Lemma 3.1 does not hold. The Choi matrix serves as a counterexample. It is easy to check that all $7$ principal minors of $C{(x)}$ are sos polynomials and yet it is not an sos-matrix. This is in contrast with the fact that a polynomial matrix is PSD if and only if all its principal minors are psd polynomials. The latter statement follows almost immediately from the well-known fact that a constant matrix is PSD if and only if all its principal minors are nonnegative.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Remark 3.1", "weight": 1.0} -->

We are now ready to state our main result.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Remark 3.2", "weight": 1.0} -->

The Gram matrices in the sos decomposition of (presented in the Appendix) are positive definite. This shows that for all nonzero $x$, the Hessian $H{(x)}$ is positive definite and hence $p{(x)}$ is in fact *strictly convex*; i.e.,

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 3.3", "weight": 1.0} -->

Because of strict convexity and the fact that $H_{1,1}$ is *strictly* separated from $\Sigma_{3,6}$ (see ), it follows that $p{(x)}$ is in the interior of the set of trivariate forms of degree $8$ that are convex but not sos-convex. In other words, there exists a neighborhood of polynomials around $p{(x)}$, such that *every* polynomial in this neighborhood is also convex but not sos-convex.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 3.4", "weight": 1.0} -->

As explained in Section 2.1, we can dehomogenize the form in into a polynomial in two variables by letting The bivariate polynomial $p_{dh}$ has degree $8$ and we can check that it is still convex but not sos-convex. It is interesting to note that $p_{dh}$ is an example with the minimum possible number of variables since we know that all convex univariate polynomials are sos-convex. As for minimality in the degree, we do not know if an example with lower degree exists. However, we should note that a bivariate form of degree $4$ cannot be convex but not sos-convex. The reason is that the entries of the Hessian of such polynomial would be bivariate quadratic forms. It is known that a matrix with such entries is PSD if and only if it is an sos-matrix.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 3.5", "weight": 1.0} -->

Unlike nonnegativity and sum of squares, sos-convexity may not be preserved under homogenization. To give a concrete example, one can check that ${\overline{p}}_{dh}{(x_{2},x_{3})}: = p{(1,x_{2},x_{3})}$ is sos-convex, i.e., the $2 \times 2$ Hessian of ${\overline{p}}_{dh}{(x_{2},x_{3})}$ is an sos-matrix.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 3.6", "weight": 1.0} -->

It is easy to argue that the polynomial $p$ in must itself be nonnegative. Since $p$ is strictly convex, it has a unique global minimum. Clearly, the gradient of $p$ has no constant terms and hence vanishes at the origin. Therefore, $x = 0$ must be the unique global minimum of $p$. Because we have ${p{}} = 0$, it follows that $p$ is in fact positive definite.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 3.7", "weight": 1.0} -->

In, Helton and Nie prove that if a nonnegative polynomial is sos-convex, then it must be sos. Since $p$ is not sos-convex, we cannot directly use their result to claim that $p$ is sos. However, we have independently checked that this is the case simply by getting an explicit sos decomposition of $p$ using SOSTOOLS.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Our procedure for finding the example", "weight": 1.0} -->

As we mentioned in Section 2.2, one of the main strengths of sos-programming is in its ability to *search* over sos polynomials in a convex family of polynomials. Our main example in has in fact been found by solving an sos-program. In this section, we explain how this has been exactly done.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Our procedure for finding the example", "weight": 1.0} -->

The task of finding a polynomial $p{(x)}$ that is convex but not sos-convex is equivalent to finding a polynomial matrix $H{(x)}$ that is a *valid Hessian* (i.e., it is a matrix of second derivatives), and satisfies the following requirement on the scalar polynomial $y^{T}H{(x)}y$ in $\lbrack x;y\rbrack$: Indeed, if such a matrix $H{(x)}$ is found, the desired polynomial $p{(x)}$ can be recovered from it by integration. Unfortunately, a constraint of type that requires a polynomial to be psd but *not* sos cannot be easily handled, since it is a non-convex constraint. This is easy to see from a geometric viewpoint, since as Theorem 2.1. ‣ 2.2 Sum of squares, semidefinite programming, and duality ‣ 2 Background ‣ A convex polynomial that is not sos-convex") suggests, an sos-program can be converted to an equivalent semidefinite program.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Our procedure for finding the example", "weight": 1.0} -->

We know that the feasible set of a semidefinite program is always a convex set. On the other hand, for a fixed degree and dimension, the set of psd polynomials that are not sos is generally non-convex. Nevertheless, we are going to see that by making use of dual functionals of the sos cone along with Reznick's result on Hilbert's 17th problem, we can formulate an sos-program that searches over a *convex subset* of the set of polynomials that are psd but not sos. The idea behind our algorithm closely resembles the proof of Theorem 3.2.

<!-- chunk {"id": "body-0034", "role": "body", "section": "The algorithm", "weight": 1.0} -->

The sos-program which has led to our main result in can be written in pseudo-code as follows.

<!-- chunk {"id": "body-0035", "role": "body", "section": "The algorithm", "weight": 1.0} -->

1:Parameterize p (x) as a form of degree 8 in 3 variables. 2:Compute the Hessian ${H{(x)}} = \frac{\partial^{2}p}{\partial x^{2}}$. 3:Impose the constraint for some integer r ≥ 1. 4:Impose the constraint for some (carefully chosen) dual functional μ ∈ Σ3, 6*.

<!-- chunk {"id": "body-0036", "role": "body", "section": "The algorithm", "weight": 1.0} -->

The decision variables of this sos-program are the coefficients of the polynomial $p{(x)}$ that also appear in the entries of the Hessian matrix $H{(x)}$. The scalar $r$ and the dual functional $\mu$ must be fixed *a priori* as explained in the sequel. Note that the constraints and are linear in the decision variables and indeed the feasible set described by these constraints is a convex set.

<!-- chunk {"id": "body-0037", "role": "body", "section": "The algorithm", "weight": 1.0} -->

We claim that if this sos-program is feasible, the solution $p{(x)}$ will be convex but not sos-convex. The requirement of $H{(x)}$ being a valid Hessian is met by construction since $H{(x)}$ is obtained by twice differentiating a polynomial. It is also easy to see that if the constraint in is satisfied, then $y^{T}H{(x)}y$ will be psd. The same implication would hold if instead of ${({x_{1}^{2} + x_{2}^{2} + x_{3}^{2}})}^{r}$ we used any other positive definite polynomial. As discussed in Section 2.1, the reason for using this particular form is due to the result of Reznick, which states that if $y^{T}H{(x)}y$ is positive definite, then must be satisfied for sufficiently large $r$. In our case, it was sufficient to take $r = 1$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "The algorithm", "weight": 1.0} -->

In order to guarantee that $y^{T}H{(x)}y$ is not sos, by Lemma 3.1 it suffices to require at least one of the principal minors of $H{(x)}$ not to be sos (though they must all be psd because of and Remark 3.1). The constraint in is imposing this requirement on the first diagonal element $H_{1,1}$. Since $p{(x)}$ is a form of degree $8$ in $3$ variables, $H_{1,1}$ will be a form of degree $6$ in $3$ variables. The role of the dual functional $\mu \in \Sigma_{3,6}^{\ast}$ in is to separate $H_{1,1}$ from $\Sigma_{3,6}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "The algorithm", "weight": 1.0} -->

Once an ordering on the monomials of $H_{1,1}$ is fixed, the inequality in can be written as where $b \in {\mathbb{R}}^{28}$ represents our separating hyperplane and must be fixed *a priori*. We explain next our specific choice of the dual functional $\mu$.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Finding a separating hyperplane", "weight": 1.0} -->

There are several ways to obtain a separating hyperplane for $\Sigma_{3,6}$. In particular, we can find a dual functional that separates the Motzkin form in from $\Sigma_{3,6}$. This can be done in at least a couple of different ways. For example, we can formulate a semidefinite program that requires the Motzkin form to be sos. This program is clearly infeasible. A feasible solution to its dual semidefinite program will give us the desired separating hyperplane. Most SDP solvers, such as SeDuMi, use primal-dual interior point algorithms to solve an SDP. Therefore, once the primal SDP is infeasible, a dual feasible solution can readily be recovered from the solver.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Finding a separating hyperplane", "weight": 1.0} -->

Another way to obtain a separating hyperplane for the Motzkin form $M_{h}{(x)}$ is to find its (Euclidean) projection $M_{h}^{p}{(x)}$ onto the cone $\Sigma_{3,6}$. Since the projection is done onto a convex set, the hyperplane tangent to $\Sigma_{3,6}$ at $M_{h}^{p}{(x)}$ will be supporting $\Sigma_{3,6}$. The projection $M_{h}^{p}{(x)}$ can be obtained by searching for an sos polynomial that is closest in the $2$-norm of the coefficients to the Motzkin form. This search can be formulated as the following sos-program: Here, $q{(x)}$ is parameterized as a degree $6$ form in $3$ variables. The objective function in can be converted to a semidefinite constraint using standard tricks; see e.g..

<!-- chunk {"id": "body-0042", "role": "body", "section": "Finding a separating hyperplane", "weight": 1.0} -->

We have used SOSTOOLS and SeDuMi to obtain a feasible solution to SOS-Program 1 with $r = 1$ and the dual function $\mu$ computed using the projection approach described above. In order to end up with the form in which has integer coefficients, some post-processing has been done on this feasible solution. This procedure includes truncation of the coefficients and some linear coordinate transformations.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Finding a separating hyperplane", "weight": 1.0} -->

We shall end our discussion with a couple of remarks.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Remark 4.1", "weight": 1.0} -->

If the constraints and the objective function of a semidefinite program possess some type of symmetry, the same symmetry will generally be inherited in the solution returned by interior point algorithms. For example, consider the sos-program. The Motzkin form $M_{h}{(x)}$ is symmetric in $x_{1}$ and $x_{2}$; see. Therefore, it turns out that the optimal solution $M_{h}^{p}{(x)}$ is also symmetric in $x_{1}$ and $x_{2}$. On the other hand, our main example $p{(x)}$ in and its dehomogenized version $p_{dh}{(x)}$ in are not symmetric in $x_{1}$ and $x_{2}$. Even though constraint and the dual functional $b$ possess this symmetry, the symmetry is being broken by imposing constraint on the second partial derivative with respect to $x_{1}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Remark 4.2", "weight": 1.0} -->

Perhaps of independent interest, the methodology explained in this section can be employed to search or optimize over a restricted family of psd polynomials that are not sos using sos-programming. In particular, we can use this technique to simply find more instances of such polynomials. In order to impose a constraint that some polynomial $q{(x)}$ must belong to $P_{n,d}\backslash\Sigma_{n,d}$, we can use a dual functional $\eta \in \Sigma_{n,d}^{\ast}$ to separate $q{(x)}$ from $\Sigma_{n,d}$, and then require $q{(x)}{({\sum_{i = 1}^{n}x_{i}^{2}})}^{r}$ to be sos, so that $q{(x)}$ stays in $P_{n,d}$.
