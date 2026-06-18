<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Semidefinite Approximations of the Matrix Logarithm

Topics include Convex optimization, Semidefinite programming, Optimization, Matrix function.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The matrix logarithm, when applied to Hermitian positive definite matrices, is concave with respect to the positive semidefinite order. This operator concavity property leads to numerous concavity and convexity results for other matrix functions, many of which are of importance in quantum information theory. In this paper we show how to approximate the matrix logarithm with functions that preserve operator concavity and can be described using the feasible regions of semidefinite optimization problems of fairly small size. Such approximations allow us to use off-the-shelf semidefinite optimization solvers for convex optimization problems involving the matrix logarithm and related functions, such as the quantum relative entropy. The basic ingredients of our approach apply, beyond the matrix logarithm, to functions that are operator concave and operator monotone. As such, we introduce strategies for constructing semidefinite approximations that we expect will be useful, more generally, for studying the approximation power of functions with small semidefinite representations.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Semidefinite optimization problems are convex optimization problems that take the form

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $\mathbf{H}_{+}^{d}$ is the cone of $d \times d$ Hermitian positive semidefinite matrices, and $L \subseteq \mathbf{H}^{d}$ is an affine subspace of $d \times d$ Hermitian matrices (thought of as a real vector space). A convex function $f$ is said to have a *semidefinite representation* of size $d$ if its epigraph $\{{(x,t)}:{{f{(x)}} \leq t}\}$ can be expressed in the form $\pi{({L \cap \mathbf{H}_{+}^{d}})}$ where $\pi$ is a linear map. The existence of such representations for many convex functions explains the importance of semidefinite programming as a class of convex optimization problems. Understanding which convex sets and functions do and do not have small semidefinite descriptions has been a focus of considerable recent research effort in real algebraic geometry, optimization, and theoretical computer science (see, e.g., ).

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

One fundamental limitation is that the feasible regions of semidefinite optimization problems are necessarily semialgebraic sets, i.e., they can be expressed as finite unions of sets defined by polynomial inequalities. As such, we cannot hope to *exactly* model non-semialgebraic convex sets and functions, such as the logarithm, using semidefinite programming. This leads us to consider the problem of understanding which general convex sets and functions can be *approximated* with high accuracy by sets with small semidefinite representations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Semidefinite approximations", "weight": 1.0} -->

One starting point is to consider the approximation of univariate convex or concave functions from the point of view of semidefinite optimization. *How well can we approximate a given univariate concave function with a function that is not just concave, but also has a semidefinite representation of a given size?* This is distinct from questions in classical approximation theory, both due to its emphasis on preserving concavity, and also because the complexity of the approximating function is defined in terms of the size of a semidefinite description, rather than the degree of a polynomial or rational approximation. A key motivation for the study of univariate approximation theory is its relevance for computing matrix functions. If $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}}$ then the corresponding matrix function can be defined for positive definite Hermitian matrices $\mathbf{H}_{+ +}^{n}$ by

<!-- chunk {"id": "body-0007", "role": "body", "section": "Semidefinite approximations", "weight": 1.0} -->

where $X = {U{{diag}{(\lambda_{1},\ldots,\lambda_{n})}}U^{\ast}}$ is an eigendecomposition of $X$. To generalize our semidefinite approximation point of view to matrix functions, we focus on functions that have a natural dimension-free concavity property known as operator concavity. A function $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}}$ is *operator concave* if the corresponding matrix function satisfies Jensen's inequality in the positive semidefinite (Löwner) order, i.e.,

<!-- chunk {"id": "body-0008", "role": "body", "section": "Semidefinite approximations", "weight": 1.0} -->

for all $n$, all ${X_{1},X_{2}} \in \mathbf{H}_{+ +}^{n}$ and all $\lambda \in {\lbrack 0,1\rbrack}$. Associated with any operator concave function $g$ and a positive integer $n$ is a convex set $\{{{(X,T)} \in {\mathbf{H}_{+ +}^{n} \times \mathbf{H}^{n}}}:{{g{(X)}} \succeq T}\}$, the *matrix hypograph* of $g$. A good introduction to operator concave functions is.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Semidefinite approximations", "weight": 1.0} -->

Among the most familiar and important operator concave functions is the logarithm. The operator concavity of the logarithm has remarkable consequences. For example, it can be used to establish joint convexity of the (Umegaki) quantum relative entropy function,

<!-- chunk {"id": "body-0010", "role": "body", "section": "Semidefinite approximations", "weight": 1.0} -->

using an appropriate generalization of the perspective transform (the *noncommutative perspective*, to be defined later). The function $D$ plays a fundamental role in quantum information theory, and its joint convexity was first established by Lieb and Ruskai building on an earlier result of Lieb.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Contributions", "weight": 1.0} -->

In this paper we develop techniques to construct accurate approximations, with small semidefinite descriptions, for the matrix logarithm. A key motivation for doing so is that using this basic building block, we can approximate other important convex and concave functions arising in quantum information, such as the quantum relative entropy. The same basic principles we use to approximate the matrix logarithm apply in greater generality. Our methods partly generalize to yield high accuracy semidefinite approximations for functions that are operator monotone and operator concave, as well as their matrix analogues. Furthermore, the full power of our approximation methods for the matrix logarithm extend to operator concave functions that satisfy functional equations of a particular form. As examples in this direction we show how to obtain semidefinite approximations of the logarithmic mean, and the arithmetic-geometric mean of Gauss.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Contributions", "weight": 1.0} -->

Table 1 shows some of the functions implemented in the package.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Contributions", "weight": 1.0} -->

op_rel_entr_epi_cone
m + k LMIs of size 2 n × 2 n each

<!-- chunk {"id": "body-0014", "role": "body", "section": "Contributions", "weight": 1.0} -->

ρ ↦ Tr[σ log ρ] (σ ≽ 0 fixed; Concave)
m + k LMIs of size 2 n × 2 n each

<!-- chunk {"id": "body-0015", "role": "body", "section": "Contributions", "weight": 1.0} -->

quantum_rel_entr
(ρ,σ) ↦ Tr[ρ (log ρ−log σ)] (Convex)

<!-- chunk {"id": "body-0016", "role": "body", "section": "Contributions", "weight": 1.0} -->

Our functions can be combined with existing functions in CVX to solve problems involving a mixture of constraints modeled with the (operator) relative entropy cone, linear inequalities, and second-order and semidefinite cone constraints.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Key ideas", "weight": 1.0} -->

We now summarize the main ideas behind our approach to constructing semidefinite approximations and illustrate them with the central example of the paper, the logarithm.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Approximating integral representations via quadrature", "weight": 1.0} -->

The first main idea is to use integral representations of functions as the basis for approximation. In general, suppose a concave function $g$ has an integral representation of the form

<!-- chunk {"id": "body-0019", "role": "body", "section": "Approximating integral representations via quadrature", "weight": 1.0} -->

where $\mu$ is a positive measure and, for any fixed $t$, $f_{t}{(x)}$ is a semidefinite representable concave function of $x$. If we approximate the integral via a quadrature rule with positive weights (see Appendix A), we obtain an approximation of $g$ as

<!-- chunk {"id": "body-0020", "role": "body", "section": "Approximating integral representations via quadrature", "weight": 1.0} -->

which is again semidefinite representable. Integral representations of the form are guaranteed to exist for certain operator concave functions by a result of Löwner. In the case of the logarithm, the integral representation is simply

<!-- chunk {"id": "body-0021", "role": "body", "section": "Approximating integral representations via quadrature", "weight": 1.0} -->

For fixed $t$, it turns out that the integrand is itself operator concave and its matrix hypograph has a semidefinite representation. Approximating the integral via a quadrature rule (such as Gaussian quadrature) we obtain an approximation of $\log$ that is operator concave and semidefinite representable.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Using functional equations to improve approximations", "weight": 1.0} -->

The logarithm also satisfies the functional equation ${\log{(x^{1/2})}} = {\frac{1}{2}{\log{(x)}}}$, allowing us to express $\log{(x)}$ in terms of the logarithm of $\sqrt{x}$. This is helpful because the square root brings points closer to $x = 1$, where the approximations via quadrature are more accurate. Because the square root is also operator monotone, operator concave, and semidefinite representable, we can compose our rational approximations obtained via quadrature with this functional equation. Doing so we obtain improved approximations that still have all of these desirable properties.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Using functional equations to improve approximations", "weight": 1.0} -->

This additional idea may seem specific to the logarithm. In fact, there are other operator monotone and operator concave functions obeying functional equations that relate the function at a point to the function value at a point closer to $x = 1$. Moreover the functional equations have appropriate monotonicity and concavity properties, allowing us to use a similar strategy to obtain improved approximations. Functions defined as the limits of mean iterations, such as the arithmetic-geometric mean function of Gauss, have the appropriate properties to be approximated in this way.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Extending to bivariate matrix functions via perspectives", "weight": 1.0} -->

We can further extend our semidefinite approximations of matrix concave functions to certain bivariate matrix functions via a noncommutative notion of the perspective of a function. Given a function $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}}$, its *perspective* transform is defined as ${(x,y)} \in {\mathbb{R}}_{+ +}^{2}\mapsto{yg{({x/y})}}$. It is a well-known result in convex analysis that if $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}}$ is concave then its perspective is also concave. The definition of the perspective transform extends to functions of positive definite matrices.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Extending to bivariate matrix functions via perspectives", "weight": 1.0} -->

If $X$ and $Y$ are scalars, the noncommutative perspective coincides with the usual scalar definition of perspective transform. A remarkable property of the noncommutative perspective is that it is jointly concave in $(X,Y)$ whenever $g$ is operator concave, i.e.,

<!-- chunk {"id": "body-0026", "role": "body", "section": "Extending to bivariate matrix functions via perspectives", "weight": 1.0} -->

The noncommutative perspective of the negative logarithm function is known as *operator relative entropy*, which we denote by $D_{\text{op}}$:^11^1We define $D_{\text{op}}$ as ${D_{\text{op}}{({X \parallel Y})}} = {- {P_{\log}{(Y,X)}}}$ to match the conventional order of arguments in information theory.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Extending to bivariate matrix functions via perspectives", "weight": 1.0} -->

The semidefinite approximations of the scalar logarithm function can be used to approximate $D_{\text{op}}$. In turn this allows us to get semidefinite approximations of the quantum relative entropy ${D{({\rho \parallel \sigma})}} = {{Tr}{\lbrack{\rho{({{\log\rho} - {\log\sigma}})}}\rbrack}}$.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Computing the matrix logarithm", "weight": 1.0} -->

The problem of numerically computing the (matrix) logarithm has a long history in numerical analysis. Among the most successful methods is the so-called *inverse scaling and squaring*, or *Briggs-Padé*, method (see, e.g., ). This method uses the approximation ${\log{(X)}} \approx {2^{k}r_{m}{(X^{1/2^{k}})}}$ where $r_{m}$ is the $m$th diagonal Padé approximant of $\log{(x)}$ at $x = 1$, which turns out to be precisely the approximation we consider in this paper. The literature on computing the matrix logarithm via these methods does not seem to investigate the concavity properties of this approximation method. Our central observation is that this method for computing matrix logarithm "preserves" the concavity properties of logarithm, and can be modeled using semidefinite programming constraints.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Computing the matrix logarithm", "weight": 1.0} -->

This in turn leads to efficient algorithms, via semidefinite programming, for problems much more complex than simply computing the matrix logarithm (see, e.g., ).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Other approximations", "weight": 1.0} -->

A simple approximation for logarithm is ${\log{(x)}} \approx {\frac{1}{h}{({x^{h} - 1})}}$, where $0 < h < 1$, with equality when $h\rightarrow 0$. This can be seen as the combination of a Taylor linearization ${\log{(x)}} \approx {x - 1}$ with the fact that ${\log{(x^{h})}} = {\frac{1}{h}{\log{(x^{h})}}}$. In previous work by the first two authors, it was shown that this approach can be used to get a semidefinite approximation of the matrix logarithm and the quantum relative entropy. In general, however, the quality of this approximation is relatively poor and is much less accurate than the rational approximations considered here. Another idea of approximating the scalar relative entropy cone via second-order cone programming is considered in unpublished work by Glineur.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Other approximations", "weight": 1.0} -->

The approach taken by Glineur involves using an approximation for the logarithm via the arithmetic-geometric-mean iteration, and then giving an approximation of a convex cone related to the arithmetic-geometric-mean with convex quadratic inequalities.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Successive approximation", "weight": 1.0} -->

To make up for the poor approximation quality of ${\log{(x)}} \approx {\frac{1}{h}{({x^{h} - 1})}}$, one method is to successively refine the linearization point and use, more generally, ${\log{(x)}} \approx {{\log{(a)}} + {\frac{1}{h}{({{({x/a})}^{h} - 1})}}}$. This is the approach taken by CVX. It requires the solution of multiple second-order cone programs to update the linearization point. One drawback of this approach, however, is that it does not generalize to matrices, since there is no natural analogue of the identity ${\log{({ax})}} = {{\log{(a)}} + {\log{(x)}}}$ for matrices.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Approximating second-order cone programs with linear programs", "weight": 1.0} -->

The most prominent example of approximating a family of conic optimization problems with another, is the work of Ben-Tal and Nemirovski, giving a systematic method to approximate any second-order cone program with a linear program. The number of linear inequalities in the approximating linear programs of Ben-Tal and Nemirovski grow logarithmically with $1/\epsilon$ where $\epsilon$ is a notion of approximation quality. The fundamental construction underlying this approximation is a description of the regular $2^{n}$-gon in the plane as the projection of a higher-dimensional polyhedron with $2n$ facets. Using this technique Ben-Tal and Nemirovski give a polyhedral approximation to the exponential cone, via first constructing a second-order cone based approximation to the exponential cone \[, Example 4\]. This approximation is based on a degree four truncation of the Taylor series for $\exp{({2^{- k}x})}$. Unlike our approximations, this approach works with the exponential, which is not operator convex and so does not generalize to matrices.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Outline", "weight": 1.0} -->

To make the presentation as accessible as possible, we focus first on the case of the logarithm function (Sections 2 and 3) before explaining the general approach for operator concave functions (Section 4). In Section 2 we describe the basic ideas behind our approximations, focusing on the scalar logarithm and the relative entropy cone. In Section 3 we state and prove our main result (Theorem 3. ‣ 3.2 Approximating the operator relative entropy cone ‣ 3 Operator concavity, noncommutative perspectives and the operator relative entropy cone ‣ Semidefinite approximations of the matrix logarithm")), giving an explicit family of semidefinite approximations to the operator relative entropy. We conclude the section by giving semidefinite approximations of the epigraph of the quantum relative entropy function. In Section 4 we explain how our approach can be used to approximate other operator concave functions. In Section 5 we present some numerical experiments to test the accuracy of our approximations and give comparison with the successive approximation method of CVX. Finally we conclude in Section 6.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Approximating logarithm", "weight": 1.0} -->

In this section we describe the main ingredients for our semidefinite approximations of the logarithm. For simplicity we restrict ourselves, here, to the case of scalar logarithm. Nevertheles, our construction remains valid for matrices---we explain this is in more detail in the following section. Our approximation of the logarithm function relies on the following ingredients: an integral representation of $\log$, Gaussian quadrature, and the following functional relation satisfied by $\log$: ${\log{(x)}} = {\frac{1}{h}{\log{(x^{h})}}}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Integral representation", "weight": 1.0} -->

We start with the following integral representation of the logarithm function

<!-- chunk {"id": "body-0037", "role": "body", "section": "Integral representation", "weight": 1.0} -->

Here, the second equality comes from the change of variable $s = {{t{({x - 1})}} + 1}$. A key property of this integral representation is that for any fixed $t \in {\lbrack 0,1\rbrack}$, the function $x\mapsto{f_{t}{(x)}}$ is concave. (The representation thus establishes the concavity of $\log$ in a way that generalizes nicely to the setting of matrix functions.)

<!-- chunk {"id": "body-0038", "role": "body", "section": "Gaussian quadrature", "weight": 1.0} -->

To obtain an approximation of $\log$ that retains concavity, we discretize the integral using Gaussian quadrature (see Appendix A for more information about Gaussian quadrature). This gives an approximation of the form

<!-- chunk {"id": "body-0039", "role": "body", "section": "Gaussian quadrature", "weight": 1.0} -->

where $t_{j} \in {\lbrack 0,1\rbrack}$ are the quadrature nodes, and $w_{j} > 0$ are the quadrature weights.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Gaussian quadrature", "weight": 1.0} -->

The key property of $r_{m}$ is that it is concave and semidefinite representable: this is because it is a nonnegative combination of functions that are each semidefinite representable (see ). It is also interesting to note that the function $r_{m}$ coincides precisely with the Padé approximant of $\log$ of type $(m,m)$: in particular $r_{m}$ agrees with the first ${2m} + 1$ Taylor coefficients of the logarithm function. This has in fact been already observed, e.g., in \[, Theorem 4.3\] (see also Appendix B for a proof that works for a more general class of functions).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Exponentiation", "weight": 1.0} -->

Note that when $0 < h < 1$, $x^{h}$ is closer to 1 than $x$ is, and thus the rational approximation is of better quality at $x^{h}$ than at $x$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Exponentiation", "weight": 1.0} -->

The approximation $r_{m,k}$ should be understood as a composition of two steps for a given $x$: take the $2^{k}$th root of $x$ to bring it closer to 1; and apply the approximation $r_{m}$ and scale back by $2^{k}$ accordingly. One can show that $r_{m,k}$ is concave and semidefinite representable: indeed it is known that power functions of the form $x\mapsto x^{1/2^{k}}$ are concave and semidefinite representable (in fact second-order cone representable), see. Since the function $r_{m}$ is concave, semidefinite representable, and monotone it easily follows that $r_{m,k}$ is concave and semidefinite representable. An explicit semidefinite representation appears as a special case of Theorem 3.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Exponentiation", "weight": 1.0} -->

‣ 3.2 Approximating the operator relative entropy cone ‣ 3 Operator concavity, noncommutative perspectives and the operator relative entropy cone ‣ Semidefinite approximations of the matrix logarithm") in Section 3.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Error bounds", "weight": 1.0} -->

One can derive bounds on the error between $r_{m,k}$ and $\log$. Since $r_{m}$ is defined in terms of Gaussian quadrature applied to the rational function $f_{t}{(x)}$, such error bounds can be derived by studying the Chebyshev coefficients of $t\mapsto{f_{t}{(x)}}$. In fact these can be computed exactly and lead to the following error bounds.

<!-- chunk {"id": "body-0045", "role": "body", "section": "The (scalar) relative entropy cone", "weight": 1.0} -->

The relative entropy is defined as the perspective function of the negative logarithm: ${(x,y)} \in {{\mathbb{R}}_{+ +} \times {\mathbb{R}}_{+ +}}\mapsto{x{\log{({x/y})}}}$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "The (scalar) relative entropy cone", "weight": 1.0} -->

Using the perspective of $r_{m,k}$ one can obtain a semidefinite approximation of $K_{\text{re}}$. Let

<!-- chunk {"id": "body-0047", "role": "body", "section": "The (scalar) relative entropy cone", "weight": 1.0} -->

The following theorem gives an approximation error for the cone $K_{m,k}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Operator concavity, noncommutative perspectives and the operator relative entropy cone", "weight": 1.0} -->

The main goal of this section is to show that the ideas presented in the previous section are still valid when working with matrices. The main result of this section (and of the paper) is Theorem 3. ‣ 3.2 Approximating the operator relative entropy cone ‣ 3 Operator concavity, noncommutative perspectives and the operator relative entropy cone ‣ Semidefinite approximations of the matrix logarithm"), which gives an explicit semidefinite programming approximation of the *operator relative entropy cone*, a matrix generalization of the relative entropy cone.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Operator concavity, noncommutative perspectives and the operator relative entropy cone", "weight": 1.0} -->

We begin by showing that the approximation $r_{m,k}$, defined, is operator concave, just like the logarithm function. We then show how to use the noncommutative perspective of $r_{m,k}$ to approximate the operator relative entropy. This leads to our explicit semidefinite approximation of the operator relative entropy cone. We then show how this can be used to approximate the quantum relative entropy.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Operator concavity of logarithm and its approximation", "weight": 1.0} -->

We have already mentioned in the introduction that the logarithm function is *operator concave*. The next proposition will allow us to show this, as well as the operator concavity of the rational function $r_{m}$ that we considered in the previous section.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Operator concavity of $r_{m,k}$", "weight": 1.0} -->

In Section 2 we saw that one can get an improved approximation of $\log$ by considering ${r_{m,k}{(x)}}:={2^{k}r_{m}{(x^{1/2^{k}})}}$. We now show that $r_{m,k}$ is also operator concave. The argument directly generalizes the proof that $r_{m,k}$ is concave (in the usual sense). For the generalization we need the notion of *operator monotonicity*. A function $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}}$ is called *operator monotone* if whenever $X \succeq Y$ then ${g{(X)}} \succeq {g{(Y)}}$, where ${X,Y} \in \mathbf{H}_{+ +}^{n}$ for any $n$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Approximating the operator relative entropy cone", "weight": 1.0} -->

We know that $D_{\text{op}}$ is jointly matrix concave in $(X,Y)$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Approximating the operator relative entropy cone", "weight": 1.0} -->

We saw, in Proposition 3, that $r_{m,k}$ is operator concave. It thus follows that the noncommutative perspective of $r_{m,k}$ is jointly concave. Our approximation of the cone $K_{\text{re}}^{n}$ will be the epigraph cone of $- P_{r_{m,k}}$, the noncommutative perspective of $- r_{m,k}$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Approximating the operator relative entropy cone", "weight": 1.0} -->

The next theorem, which is the main result of this paper, gives an explicit semidefinite representation of the cone.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Quantum relative entropy", "weight": 1.0} -->

In this section, we see how to use the results from the previous section to approximate the (Umegaki) quantum relative entropy function, defined by

<!-- chunk {"id": "body-0056", "role": "body", "section": "Quantum relative entropy", "weight": 1.0} -->

The next proposition, which appears, shows how to express the epigraph of $D$ using the operator relative entropy cone (defined in Equation ).

<!-- chunk {"id": "body-0057", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Note that the linear map $\phi$ in Proposition 4. ‣ 3.3 Quantum relative entropy ‣ 3 Operator concavity, noncommutative perspectives and the operator relative entropy cone ‣ Semidefinite approximations of the matrix logarithm") is given by ${\phi{(Z)}} = {w^{\ast}Zw}$ for $Z \in {\mathbb{C}}^{n^{2} \times n^{2}}$, where $w \in {\mathbb{C}}^{n^{2}}$ is the vector obtained by stacking the columns of the $n \times n$ identity matrix. It follows that $\phi$ is a positive linear map, in the sense that if $Z \succeq 0$ then ${\phi{(Z)}} \geq 0$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "A smaller representation", "weight": 1.0} -->

One can exploit the special structure of the linear map $\phi$ in (21. ‣ 3.3 Quantum relative entropy ‣ 3 Operator concavity, noncommutative perspectives and the operator relative entropy cone ‣ Semidefinite approximations of the matrix logarithm")), to reduce the size of the semidefinite approximation of $D{({A \parallel B})}$ from having $m + k$ blocks of size ${{2n^{2}} \times 2}n^{2}$, to having $m$ blocks of size ${({n^{2} + 1})} \times {({n^{2} + 1})}$ and $k$ blocks of size ${{2n^{2}} \times 2}n^{2}$.

<!-- chunk {"id": "body-0059", "role": "body", "section": "A smaller representation", "weight": 1.0} -->

The main idea for this reduction is to observe that the rational function $f_{t}$, which is the main building block of our approximations, can be expressed as a Schur complement, namely we have ${tP_{f_{t}}{(X,Y)}} = {Y - {Y{({Y + {t{({X - Y})}}})}^{- 1}Y}}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "A smaller representation", "weight": 1.0} -->

This representation clearly has size ${({n + 1})} \times {({n + 1})}$. Combining this with the fact that $\phi$ has the form ${\phi{\lbrack X\rbrack}} = {w^{\ast}Xw}$ (see Remark 1), allows us to reduce the semidefinite approximation of $D{({A \parallel B})}$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Approximating operator concave functions", "weight": 1.0} -->

The approximations to the relative entropy cone developed in Section 3 used the facts that

<!-- chunk {"id": "body-0062", "role": "body", "section": "Approximating operator concave functions", "weight": 1.0} -->

the logarithm is an integral of (semidefinite representable) rational functions, which can be approximated via quadrature; and

<!-- chunk {"id": "body-0063", "role": "body", "section": "Approximating operator concave functions", "weight": 1.0} -->

In this section we show how to generalize these ideas, allowing us to give semidefinite approximations for convex cones of the form

<!-- chunk {"id": "body-0064", "role": "body", "section": "Approximating operator concave functions", "weight": 1.0} -->

for a range of operator concave functions $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}}$, where $P_{g}{(X,Y)}$ is the noncommutative perspective of $g$ defined. In Section 4.1, we discuss functions that admit similar integral representations to the logarithm, which can be approximated via quadrature. In Section 4.2, we present examples of functions with perspectives $P_{g}$ that obey functional equations of the form ${P_{g} \circ \Phi} = P_{g}$ where $\Phi$ is a map with certain monotonicity properties, and use these to obtain smaller semidefinite approximations.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Approximations via Löwner's theorem", "weight": 1.0} -->

A general class of functions that admit integral representations are operator monotone functions, of which the logarithm is a special case. Recall that these are functions $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}}$ that satisfy ${g{(X)}} \preceq {g{(Y)}}$ whenever $X \preceq Y$ for ${X,Y} \in \mathbf{H}_{+ +}^{n}$ and any $n \geq 1$. The following theorem, due to Löwner, shows that any operator monotone function admits an integral representation in terms of the rational functions $f_{t}$ that we saw earlier (see Appendix D).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Positive-valued functions", "weight": 1.0} -->

In the special case when $g$ takes only positive values, one can prove (see Appendix D) an alternative integral representation, that has additional nice properties and takes the form

<!-- chunk {"id": "body-0067", "role": "body", "section": "Positive-valued functions", "weight": 1.0} -->

Here, $\mu$ is a probability measure on $\lbrack 0,1\rbrack$ and $f_{t}^{+}$ is the rational function ${f_{t}^{+}{(x)}} = {({{{({1 - t})}x^{- 1}} + t})}^{- 1}$. The main advantage of using this new integral representation instead of (24. ‣ 4.1 Approximations via Löwner’s theorem ‣ 4 Approximating operator concave functions ‣ Semidefinite approximations of the matrix logarithm")), is that the noncommutative perspective of $f_{t}^{+}$ is monotone with respect to both arguments, unlike $f_{t}$. This means that the perspective $P_{g}$ of any positive operator monotone function $g$, is monotone with respect to both arguments. Approximating $g$ by applying quadrature to ensures this property is preserved.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Examples", "weight": 1.0} -->

More information about operator monotone functions and their integral representations can be found in the books by Bhatia.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Improved approximations via functional equations", "weight": 1.0} -->

The functional equation ${\log{(x^{1/2})}} = {{({1/2})}{\log{(x)}}}$ for the logarithm gives rise to a functional equation for the perspective, ${P_{\log}{(x,y)}} = {y{\log{({x/y})}}}$, of the logarithm. Indeed if we define

<!-- chunk {"id": "body-0070", "role": "body", "section": "Improved approximations via functional equations", "weight": 1.0} -->

In Section 2 we constructed rational approximations $r_{m}$ for the logarithm, and then improved the approximation quality by successive square-rooting, defining ${r_{m,k}{(x)}} = {2^{k}r_{m}{(x^{1/2^{k}})}}$. At the level of perspectives, we have that

<!-- chunk {"id": "body-0071", "role": "body", "section": "Improved approximations via functional equations", "weight": 1.0} -->

where $\Phi^{(k)}$ denotes the composition of $\Phi$ with itself $k$ times.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Improved approximations via functional equations", "weight": 1.0} -->

A similar approach is possible for operator monotone functions $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}_{+ +}}$, that satisfy a functional equation of the form ${P_{g} \circ \Phi} = P_{g}$, as long as $\Phi$ has certain monotonicity and contraction properties. In these cases, we can obtain semidefinite representable approximations to $g$ that have smaller descriptions, for a given approximation accuracy, than the approximations by rational functions given in Theorem 5. ‣ 4.1 Approximations via Löwner’s theorem ‣ 4 Approximating operator concave functions ‣ Semidefinite approximations of the matrix logarithm"). We make this precise in Theorem 7 to follow. For simplicity of notation, we work in the scalar setting, but our arguments all extend to the matrix setting.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Improved approximations via functional equations", "weight": 1.0} -->

Examples of operator monotone functions obeying a functional equation of the desired form come from the logarithmic mean and the arithmetic-geometric mean.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Improved approximations via functional equations", "weight": 1.0} -->

: In Section 4.1 we saw that the function ${g{(x)}} = \frac{x - 1}{\log{(x)}}$ is operator monotone.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Improved approximations via functional equations", "weight": 1.0} -->

a function that arises naturally in problems of heat transfer, and in the Riemannian geometry of positive semidefinite matrices (see, e.g., \[, Section 4.5\]).

<!-- chunk {"id": "body-0076", "role": "body", "section": "Improved approximations via functional equations", "weight": 1.0} -->

The logarithmic mean also satisfies other functional equations that are closely related to Borchardt's algorithm and variants for computing the logarithm. These could also be used in the present context, but we focus on for simplicity.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Improved approximations via functional equations", "weight": 1.0} -->

: The arithmetic-geometric mean of a pair of positive scalars $x,y$, is defined as the common limit of the pair of (convergent) sequences $x_{0} = x$, $y_{0} = y$,

<!-- chunk {"id": "body-0078", "role": "body", "section": "Improved approximations via functional equations", "weight": 1.0} -->

This limit is denoted $\text{AGM}{(x,y)}$, and is the perspective of the positive, operator monotone function, ${g{(x)}} = {\text{AGM}{(x,1)}}$. Remarkably (see, e.g., \[, Equation (1.7)\]), the arithmetic-geometric mean is related to the complete elliptic integral of the first kind, $K{(x)}$, via

<!-- chunk {"id": "body-0079", "role": "body", "section": "Improved approximations via functional equations", "weight": 1.0} -->

Since it is defined as the limit of an iterative process, if ${\Phi{(x,y)}} = {({{({x + y})}/2},\sqrt{xy})}$ then

<!-- chunk {"id": "body-0080", "role": "body", "section": "Improved approximations via functional equations", "weight": 1.0} -->

More examples can be obtained by considering operator monotone functions constructed via operator mean iterations, discussed, for instance,.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Structure of approximations", "weight": 1.0} -->

Suppose $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}_{+ +}}$ is positive and operator monotone, and let $r_{m}^{+}$ be the rational, positive, operator monotone approximation to $g$ obtained by applying Gaussian quadrature (with respect to the measure $\mu$) to the integral representation. If, in addition, ${P_{g} \circ \Phi} = P_{g}$ for some map $\Phi:{{\mathbb{R}}_{+ +}^{2}\rightarrow{\mathbb{R}}_{+ +}^{2}}$, then we can define a two-parameter family of approximations by

<!-- chunk {"id": "body-0082", "role": "body", "section": "Structure of approximations", "weight": 1.0} -->

It makes sense to do this as long as $\Phi$ maps points 'closer' to the ray generated by $$ (in a way made precise in Theorem 7, to follow), and the approximation $r_{m}^{+}$ of $g$ is accurate near $x = 1$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Structure of approximations", "weight": 1.0} -->

From now on we assume that $\Phi$ has the form

<!-- chunk {"id": "body-0084", "role": "body", "section": "Structure of approximations", "weight": 1.0} -->

where ${h_{1},h_{2}}:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}_{+ +}}$ are positive, operator monotone, functions. Observe that $\Phi$ has this form for the examples of the logarithmic mean and the arithmetic-geometric mean. If $\Phi$ has the form, then $P_{r_{m,k}}{(x,y)}$ (defined in ) is positive, jointly concave, and jointly monotone for all $k \geq 0$ and $m \geq 1$. In particular, these monotonicity and concavity properties ensure that the cones $K_{m,k}:=K_{r_{m,k}}$ can be (recursively) expressed as $K_{m,0} = K_{r_{m}^{+}}$ and

<!-- chunk {"id": "body-0085", "role": "body", "section": "Approximation error", "weight": 1.0} -->

The following result shows that if $\Phi$ has contraction and monotonicity properties, we can obtain smaller semidefinite approximations of nonnegative operator monotone functions $g$ satisfying a functional equation of the form ${P_{g} \circ \Phi} = P_{g}$. It allows us to get semidefinite approximations of size $O{(\sqrt{\log{({1/\epsilon})}})}$ if $\Phi$ contracts at a linear rate, and $O{({\log{\log{({1/\epsilon})}}})}$ if $\Phi$ contracts quadratically, where $\epsilon$ is the approximation accuracy.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Remark 2", "weight": 1.0} -->

The condition says that ${d_{H}{({\Phi{(x,y)}},{})}} \leq {c^{- 1}d_{H}{({(x,y)},{})}}$ where $d_{H}{( \cdot, \cdot )}$ is the *Hilbert metric* on rays of the cone ${\mathbb{R}}_{+ +}^{2}$ (see, e.g., ). This is the precise sense in which $\Phi$ maps points 'closer' to the ray generated by $$.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Remark 2", "weight": 1.0} -->

We now apply the theorem to the logarithmic mean and the arithmetic-geometric mean.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Remark 3", "weight": 1.0} -->

As stated, both the construction of the functions $r_{m,k}$ in Section 4.2.1, and the statement of Theorem 7, are only valid when $g$ takes positive values. If $g$ is operator monotone but not positive-valued (as is the case for the logarithm), similar results apply if certain modifications are made. First, the rational functions $r_{m}$ (from Section 4.1) should be used in place of $r_{m}^{+}$. Second, we need the additional assumption that the second argument of $\Phi$ is linear (i.e., $h_{2}{(x)}$ is affine). This is required because $P_{r_{m}}$ is, in general, not monotone in its second argument.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Numerical experiments", "weight": 1.0} -->

We first evaluate our approximation method for the scalar relative entropy cone, and compare it with the successive approximation scheme of CVX, to solve maximum entropy problems and geometric programs. To assess the quality of the returned solutions, we use the solver Mosek, which has a dedicated routine for entropy problems and geometric programming (mskenopt and mskgpopt respectively). Note, however, that this solver only deals with scalar problems, and has no facility for matrix problems involving quantum relative entropy, for instance. To evaluate our method for matrices, we test it on a variational formula for trace. More numerical experiments using CvxQuad related to problems in quantum information theory appear.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Entropy problems", "weight": 1.0} -->

We consider optimization problems of the form

<!-- chunk {"id": "body-0091", "role": "body", "section": "Entropy problems", "weight": 1.0} -->

and we compare the performance of our method with the successive approximation scheme implemented in CVX. Table 2 shows the results of the comparison for randomly generated data $A \in {\mathbb{R}}^{\ell \times n}$ and $b \in {\mathbb{R}}^{\ell}$ of different sizes. We use the solution returned by the built-in maximum entropy solver in Mosek (mskenopt) as "true solution" and we measure the quality of either approximation method (successive approximation or ours) via the gap between optimal values. We use the notation $p_{sa}$ and $p_{Pade}$ respectively for the optimal values returned by the successive approximation scheme and our method.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Geometric programming", "weight": 1.0} -->

where $x \in {\mathbb{R}}^{n}$ is the decision variable. For $a \in {\mathbb{R}}_{+ +}^{n}$ the notation $x^{a}$ indicates $x^{a}:={\prod_{i = 1}^{n}x_{i}^{a_{i}}}$. The coefficients $c_{j,k}$ are assumed to be positive. Such problems can be converted into conic problems over the relative entropy (exponential) cone using the change of variables $y_{i} = {\log x_{i}}$. The current version of CVX (CVX 2.1) uses the successive approximation technique to deal with such problems. Our method based on Padé approximations can also be used in this case to obtain accurate approximations. We note that the solver Mosek has a dedicated routine for geometric programming (mskgpopt).

<!-- chunk {"id": "body-0093", "role": "body", "section": "Geometric programming", "weight": 1.0} -->

Table 3 shows a comparison of our method with the successive approximation method for randomly generated instances of. The instances were generated using the mkgp script contained in the ggplab package available at

<!-- chunk {"id": "body-0094", "role": "body", "section": "Variational formula for trace", "weight": 1.0} -->

We now evaluate our method for matrix functions. We consider the following variational expression for the trace function which appears in \[, Lemma 6\]. For any $Y \succ 0$

<!-- chunk {"id": "body-0095", "role": "body", "section": "Variational formula for trace", "weight": 1.0} -->

where $D$ is the quantum relative entropy function. We generate random positive definite matrices $Y$ and compare the solution of the right-hand side of with ${Tr}{\lbrack Y\rbrack}$. The right-hand side of can be implemented using the CVX code shown in Table 4. The results of running this piece of code using solver SDPT3 are shown in Table 4.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Variational formula for trace", "weight": 1.0} -->

3 maximize (trace(X) - quantum_rel_entr(X,Y))

<!-- chunk {"id": "body-0097", "role": "body", "section": "Lower bounds", "weight": 1.0} -->

It would be interesting to know what is the smallest possible second-order cone program that can approximate logarithm to within a fixed $\epsilon > 0$. To formalize this question, let $\mathcal{F}_{s}$ be the class of concave functions on ${\mathbb{R}}_{+ +}$ that admit a second-order cone representation of size at most $s$.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Lower bounds", "weight": 1.0} -->

Recall, from Theorem 1, that our construction yields ${s{(\epsilon)}} = {O{(\sqrt{\log{({1/\epsilon})}})}}$. This rate results from the combination of Padé approximation with successive square rooting. It would be interesting to produce lower bounds on $s{(\epsilon)}$.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Lower bounds", "weight": 1.0} -->

More generally one can define a notion of *$\epsilon$-approximate extension complexity* of a concave function $g:{{\lbrack a,b\rbrack}\rightarrow{\mathbb{R}}}$ in a similar way as. Well-known results in classical approximation theory relate the approximation quality using polynomials and rational functions of given degree to the smoothness of $g$. A natural question is to understand what corresponding properties of a concave function make it more or less difficult to approximate using second-order programs. We have phrased the question here in terms of second-order cone representations for concreteness but the same question for linear programming and semidefinite programming can also be considered.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Smaller semidefinite approximations for quantum relative entropy", "weight": 1.0} -->

The approximations for the epigraph of the quantum relative entropy $D{({A \parallel B})}$ we constructed in Section 3.3 involve linear matrix inequalities of size $O{(n^{2})}$ (where $n$ is the size of the matrices $A,B$). Is it possible to obtain approximations, of similar quality, to the quantum relative entropy using linear matrix inequalities of size $O{(n)}$?

<!-- chunk {"id": "body-0101", "role": "body", "section": "Self-concordant barriers for the operator relative entropy cone", "weight": 1.0} -->

A natural approach to conic optimization over the scalar relative entropy cone (or, equivalently, the exponential cone) is to use an interior point method that works directly with an efficiently computable self-concordant barrier for the cone (such as the barrier introduced by Nesterov ). Examples of such solvers include the extension of ECOS to the exponential cone, and the solver developed by Skajaa and Ye. We are not aware, however, of any barrier for the operator relative entropy cone that is known to be efficiently computable and self-concordant. If we had such a barrier, it could be used directly to solve conic optimization problems over the operator relative entropy cone using interior point methods, as an alternative to the semidefinite approximation-based approaches developed in this paper.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Approximating other families of convex functions via quadrature", "weight": 1.0} -->

One of the basic ideas of this paper is that if we can express a convex (or concave) function as ${g{(x)}} = {\int_{\alpha}^{\beta}{K{(x,t)}{d\mu}{(t)}}}$, where $x\mapsto{K{(x,t)}}$ has a simple semidefinite representation for fixed $t$, then we can obtain a semidefinite approximation of $g$ by quadrature. Operator monotone functions on ${\mathbb{R}}_{+ +}$, such as the logarithm, are just one class of functions with such a representation. Other such families of functions include Stieltjes functions, and certain hypergeometric functions.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Free semidefinite representation", "weight": 1.0} -->

The semidefinite representation given in this paper of the hypograph of $f_{t}$ (see ) is a "free linear matrix inequality" representation in the sense of. This is one reason why our representations also work for the noncommutative perspective of $f_{t}$. In fact one can show that if an operator concave function $f$ admits a free linear matrix inequality representation, then the noncommutative perspective of $f$ also has a free linear matrix inequality representation. An interesting question would be to understand the class of operator concave functions that admit a free LMI representation.
