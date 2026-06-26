## Introduction

Semidefinite optimization problems are convex optimization problems that take the form where $\mathbf{H}_{+}^{d}$ is the cone of $d \times d$ Hermitian positive semidefinite matrices, and $L \subseteq \mathbf{H}^{d}$ is an affine subspace of $d \times d$ Hermitian matrices (thought of as a real vector space). A convex function $f$ is said to have a *semidefinite representation* of size $d$ if its epigraph $\{{(x,t)}:{{f{(x)}} \leq t}\}$ can be expressed in the form $\pi{({L \cap \mathbf{H}_{+}^{d}})}$ where $\pi$ is a linear map. The existence of such representations for many convex functions explains the importance of semidefinite programming as a class of convex optimization problems. Understanding which convex sets and functions do and do not have small semidefinite descriptions has been a focus of considerable recent research effort in real algebraic geometry, optimization, and theoretical computer science (see, e.g.,).

One fundamental limitation is that the feasible regions of semidefinite optimization problems are necessarily semialgebraic sets, i.e., they can be expressed as finite unions of sets defined by polynomial inequalities. As such, we cannot hope to *exactly* model non-semialgebraic convex sets and functions, such as the logarithm, using semidefinite programming. This leads us to consider the problem of understanding which general convex sets and functions can be *approximated* with high accuracy by sets with small semidefinite representations.

### Semidefinite approximations

One starting point is to consider the approximation of univariate convex or concave functions from the point of view of semidefinite optimization. *How well can we approximate a given univariate concave function with a function that is not just concave, but also has a semidefinite representation of a given size?* This is distinct from questions in classical approximation theory, both due to its emphasis on preserving concavity, and also because the complexity of the approximating function is defined in terms of the size of a semidefinite description, rather than the degree of a polynomial or rational approximation. A key motivation for the study of univariate approximation theory is its relevance for computing matrix functions \[, \]. If $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}}$ then the corresponding matrix function can be defined for positive definite Hermitian matrices $\mathbf{H}_{+ +}^{n}$ by where $X = {U{{diag}{(\lambda_{1},\ldots,\lambda_{n})}}U^{\ast}}$ is an eigendecomposition of $X$. To generalize our semidefinite approximation point of view to matrix functions, we focus on functions that have a natural dimension-free concavity property known as operator concavity. A function $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}}$ is *operator concave* if the corresponding matrix function satisfies Jensen's inequality in the positive semidefinite (Löwner) order, i.e., for all $n$, all ${X_{1},X_{2}} \in \mathbf{H}_{+ +}^{n}$ and all $\lambda \in {\lbrack 0,1\rbrack}$. Associated with any operator concave function $g$ and a positive integer $n$ is a convex set $\{{{(X,T)} \in {\mathbf{H}_{+ +}^{n} \times \mathbf{H}^{n}}}:{{g{(X)}} \succeq T}\}$, the *matrix hypograph* of $g$. A good introduction to operator concave functions is.

Among the most familiar and important operator concave functions is the logarithm. The operator concavity of the logarithm has remarkable consequences. For example, it can be used to establish joint convexity of the (Umegaki) quantum relative entropy function, using an appropriate generalization of the perspective transform (the *noncommutative perspective*, to be defined later). The function $D$ plays a fundamental role in quantum information theory, and its joint convexity was first established by Lieb and Ruskai building on an earlier result of Lieb.

### Contributions

In this paper we develop techniques to construct accurate approximations, with small semidefinite descriptions, for the matrix logarithm. A key motivation for doing so is that using this basic building block, we can approximate other important convex and concave functions arising in quantum information, such as the quantum relative entropy. The same basic principles we use to approximate the matrix logarithm apply in greater generality. Our methods partly generalize to yield high accuracy semidefinite approximations for functions that are operator monotone and operator concave, as well as their matrix analogues. Furthermore, the full power of our approximation methods for the matrix logarithm extend to operator concave functions that satisfy functional equations of a particular form. As examples in this direction we show how to obtain semidefinite approximations of the logarithmic mean, and the arithmetic-geometric mean of Gauss. We have implemented our constructions in the MATLAB-based modeling language CVX and they are available online on the website: Table 1 shows some of the functions implemented in the package. op_rel_entr_epi_cone m + k LMIs of size 2 n × 2 n each m + k LMIs of size 2 n × 2 n each ρ ↦ Tr[σ log ρ] (σ ≽ 0 fixed; Concave) m + k LMIs of size 2 n × 2 n each quantum_rel_entr (ρ, σ) ↦ Tr[ρ (log ρ − log σ)] (Convex) and k LMIs of size 2 n2 × 2 n2 each Table 1: List of functions available in the package CvxQuad. The last column gives the size of the semidefinite representations (here LMI stands for Linear Matrix Inequality, and corresponds to a constraint of the form in). The parameters m and k control the accuracy of the approximation (see Proposition 1) and n is the size of the matrix arguments.

Our functions can be combined with existing functions in CVX to solve problems involving a mixture of constraints modeled with the (operator) relative entropy cone, linear inequalities, and second-order and semidefinite cone constraints.

### Key ideas

We now summarize the main ideas behind our approach to constructing semidefinite approximations and illustrate them with the central example of the paper, the logarithm.

### Approximating integral representations via quadrature

The first main idea is to use integral representations of functions as the basis for approximation. In general, suppose a concave function $g$ has an integral representation of the form where $\mu$ is a positive measure and, for any fixed $t$, $f_{t}{(x)}$ is a semidefinite representable concave function of $x$. If we approximate the integral via a quadrature rule with positive weights (see Appendix A), we obtain an approximation of $g$ as which is again semidefinite representable. Integral representations of the form are guaranteed to exist for certain operator concave functions by a result of Löwner. In the case of the logarithm, the integral representation is simply For fixed $t$, it turns out that the integrand is itself operator concave and its matrix hypograph has a semidefinite representation. Approximating the integral via a quadrature rule (such as Gaussian quadrature) we obtain an approximation of $\log$ that is operator concave and semidefinite representable.

### Using functional equations to improve approximations

The logarithm also satisfies the functional equation ${\log{(x^{1/2})}} = {\frac{1}{2}{\log{(x)}}}$, allowing us to express $\log{(x)}$ in terms of the logarithm of $\sqrt{x}$. This is helpful because the square root brings points closer to $x = 1$, where the approximations via quadrature are more accurate. Because the square root is also operator monotone, operator concave, and semidefinite representable, we can compose our rational approximations obtained via quadrature with this functional equation. Doing so we obtain improved approximations that still have all of these desirable properties.

This additional idea may seem specific to the logarithm. In fact, there are other operator monotone and operator concave functions obeying functional equations that relate the function at a point to the function value at a point closer to $x = 1$. Moreover the functional equations have appropriate monotonicity and concavity properties, allowing us to use a similar strategy to obtain improved approximations. Functions defined as the limits of mean iterations, such as the arithmetic-geometric mean function of Gauss, have the appropriate properties to be approximated in this way.

### Extending to bivariate matrix functions via perspectives

We can further extend our semidefinite approximations of matrix concave functions to certain bivariate matrix functions via a noncommutative notion of the perspective of a function. Given a function $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}}$, its *perspective* transform is defined as ${(x,y)} \in {\mathbb{R}}_{+ +}^{2}\mapsto{yg{({x/y})}}$. It is a well-known result in convex analysis that if $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}}$ is concave then its perspective is also concave. The definition of the perspective transform extends to functions of positive definite matrices. Given a function $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}}$, its *noncommutative perspective* is $P_{g}:{{\mathbf{H}_{+ +}^{n} \times \mathbf{H}_{+ +}^{n}}\rightarrow\mathbf{H}^{n}}$ defined by If $X$ and $Y$ are scalars, the noncommutative perspective coincides with the usual scalar definition of perspective transform. A remarkable property of the noncommutative perspective is that it is jointly concave in $(X,Y)$ whenever $g$ is operator concave, i.e., for any $\lambda \in {\lbrack 0,1\rbrack}$ and ${X_{1},Y_{1},X_{2},Y_{2}} \in \mathbf{H}_{+ +}^{n}$, see \[\]. The semidefinite approximations we construct in this paper can be suitably *homogenized* to give semidefinite approximations of the noncommutative perspective, or more precisely of the associated hypograph cone: The noncommutative perspective of the negative logarithm function is known as *operator relative entropy*, which we denote by $D_{\text{op}}$:^11^1We define $D_{\text{op}}$ as ${D_{\text{op}}{({X \parallel Y})}} = {- {P_{\log}{(Y,X)}}}$ to match the conventional order of arguments in information theory.

The semidefinite approximations of the scalar logarithm function can be used to approximate $D_{\text{op}}$. In turn this allows us to get semidefinite approximations of the quantum relative entropy ${D{({\rho \parallel \sigma})}} = {{Tr}{\lbrack{\rho{({{\log\rho} - {\log\sigma}})}}\rbrack}}$.

### Related work

### Computing the matrix logarithm

The problem of numerically computing the (matrix) logarithm has a long history in numerical analysis. Among the most successful methods is the so-called *inverse scaling and squaring*, or *Briggs-Padé*, method (see, e.g., \[ \]). This method uses the approximation ${\log{(X)}} \approx {2^{k}r_{m}{(X^{1/2^{k}})}}$ where $r_{m}$ is the $m$th diagonal Padé approximant of $\log{(x)}$ at $x = 1$, which turns out to be precisely the approximation we consider in this paper. The literature on computing the matrix logarithm via these methods does not seem to investigate the concavity properties of this approximation method. Our central observation is that this method for computing matrix logarithm "preserves" the concavity properties of logarithm, and can be modeled using semidefinite programming constraints. This in turn leads to efficient algorithms, via semidefinite programming, for problems much more complex than simply computing the matrix logarithm (see, e.g., ).

### Other approximations

A simple approximation for logarithm is ${\log{(x)}} \approx {\frac{1}{h}{({x^{h} - 1})}}$, where $0 < h < 1$, with equality when $h\rightarrow 0$. This can be seen as the combination of a Taylor linearization ${\log{(x)}} \approx {x - 1}$ with the fact that ${\log{(x^{h})}} = {\frac{1}{h}{\log{(x^{h})}}}$. In previous work by the first two authors, it was shown that this approach can be used to get a semidefinite approximation of the matrix logarithm and the quantum relative entropy. In general, however, the quality of this approximation is relatively poor and is much less accurate than the rational approximations considered here. Another idea of approximating the scalar relative entropy cone via second-order cone programming is considered in unpublished work by Glineur. The approach taken by Glineur involves using an approximation for the logarithm via the arithmetic-geometric-mean iteration, and then giving an approximation of a convex cone related to the arithmetic-geometric-mean with convex quadratic inequalities.

### Successive approximation

To make up for the poor approximation quality of ${\log{(x)}} \approx {\frac{1}{h}{({x^{h} - 1})}}$, one method is to successively refine the linearization point and use, more generally, ${\log{(x)}} \approx {{\log{(a)}} + {\frac{1}{h}{({{({x/a})}^{h} - 1})}}}$. This is the approach taken by CVX. It requires the solution of multiple second-order cone programs to update the linearization point. One drawback of this approach, however, is that it does not generalize to matrices, since there is no natural analogue of the identity ${\log{({ax})}} = {{\log{(a)}} + {\log{(x)}}}$ for matrices.

### Approximating second-order cone programs with linear programs

The most prominent example of approximating a family of conic optimization problems with another, is the work of Ben-Tal and Nemirovski, giving a systematic method to approximate any second-order cone program with a linear program. The number of linear inequalities in the approximating linear programs of Ben-Tal and Nemirovski grow logarithmically with $1/\epsilon$ where $\epsilon$ is a notion of approximation quality. The fundamental construction underlying this approximation is a description of the regular $2^{n}$-gon in the plane as the projection of a higher-dimensional polyhedron with $2n$ facets. Using this technique Ben-Tal and Nemirovski give a polyhedral approximation to the exponential cone, via first constructing a second-order cone based approximation to the exponential cone \[, Example 4\]. This approximation is based on a degree four truncation of the Taylor series for $\exp{({2^{- k}x})}$. Unlike our approximations, this approach works with the exponential, which is not operator convex and so does not generalize to matrices.

### Outline

To make the presentation as accessible as possible, we focus first on the case of the logarithm function (Sections 2 and 3) before explaining the general approach for operator concave functions (Section 4). In Section 2 we describe the basic ideas behind our approximations, focusing on the scalar logarithm and the relative entropy cone. In Section 3 we state and prove our main result (Theorem 3. ‣ 3.2 Approximating the operator relative entropy cone ‣ 3 Operator concavity, noncommutative perspectives and the operator relative entropy cone ‣ Semidefinite approximations of the matrix logarithm")), giving an explicit family of semidefinite approximations to the operator relative entropy. We conclude the section by giving semidefinite approximations of the epigraph of the quantum relative entropy function. In Section 4 we explain how our approach can be used to approximate other operator concave functions. In Section 5 we present some numerical experiments to test the accuracy of our approximations and give comparison with the successive approximation method of CVX. Finally we conclude in Section 6.

## Approximating logarithm

In this section we describe the main ingredients for our semidefinite approximations of the logarithm. For simplicity we restrict ourselves, here, to the case of scalar logarithm. Nevertheles, our construction remains valid for matrices---we explain this is in more detail in the following section. Our approximation of the logarithm function relies on the following ingredients: an integral representation of $\log$, Gaussian quadrature, and the following functional relation satisfied by $\log$: ${\log{(x)}} = {\frac{1}{h}{\log{(x^{h})}}}$.

### Integral representation

We start with the following integral representation of the logarithm function Here, the second equality comes from the change of variable $s = {{t{({x - 1})}} + 1}$. A key property of this integral representation is that for any fixed $t \in {\lbrack 0,1\rbrack}$, the function $x\mapsto{f_{t}{(x)}}$ is concave. (The representation thus establishes the concavity of $\log$ in a way that generalizes nicely to the setting of matrix functions.) One can easily show that the function $x\mapsto{f_{t}{(x)}}$ is semidefinite representable:

### Gaussian quadrature

To obtain an approximation of $\log$ that retains concavity, we discretize the integral using Gaussian quadrature (see Appendix A for more information about Gaussian quadrature). This gives an approximation of the form where $t_{j} \in {\lbrack 0,1\rbrack}$ are the quadrature nodes, and $w_{j} > 0$ are the quadrature weights. We denote by $r_{m}{(x)}$ the right-hand side of, a rational function whose numerator and denominator have degree $m$: The key property of $r_{m}$ is that it is concave and semidefinite representable: this is because it is a nonnegative combination of functions that are each semidefinite representable (see). It is also interesting to note that the function $r_{m}$ coincides precisely with the Padé approximant of $\log$ of type $(m,m)$: in particular $r_{m}$ agrees with the first ${2m} + 1$ Taylor coefficients of the logarithm function. This has in fact been already observed, e.g., in \[, Theorem 4.3\] (see also Appendix B for a proof that works for a more general class of functions).

### Exponentiation

The approximation is best around $x = 1$. A common technique to get good quality approximations when $x$ is farther away from $1$ is to exploit the following important property of the logarithm function: Note that when $0 < h < 1$, $x^{h}$ is closer to 1 than $x$ is, and thus the rational approximation is of better quality at $x^{h}$ than at $x$. Taking $h$ of the form $h = {1/2^{k}}$ we define: The approximation $r_{m,k}$ should be understood as a composition of two steps for a given $x$: take the $2^{k}$th root of $x$ to bring it closer to 1; and apply the approximation $r_{m}$ and scale back by $2^{k}$ accordingly. One can show that $r_{m,k}$ is concave and semidefinite representable: indeed it is known that power functions of the form $x\mapsto x^{1/2^{k}}$ are concave and semidefinite representable (in fact second-order cone representable), see. Since the function $r_{m}$ is concave, semidefinite representable, and monotone it easily follows that $r_{m,k}$ is concave and semidefinite representable. An explicit semidefinite representation appears as a special case of Theorem 3. ‣ 3.2 Approximating the operator relative entropy cone ‣ 3 Operator concavity, noncommutative perspectives and the operator relative entropy cone ‣ Semidefinite approximations of the matrix logarithm") in Section 3.

### Error bounds

One can derive bounds on the error between $r_{m,k}$ and $\log$. Since $r_{m}$ is defined in terms of Gaussian quadrature applied to the rational function $f_{t}{(x)}$, such error bounds can be derived by studying the Chebyshev coefficients of $t\mapsto{f_{t}{(x)}}$. In fact these can be computed exactly and lead to the following error bounds.

### Proposition 1

Let $r_{m,k}$ be the function defined . Then for any $x > 0$ we have

### Proof

By making appropriate choices of $m$ and $k$ in Proposition 1, we obtain a result showing how the size of our representation grows as the approximation quality improves.

### Theorem 1

For any (fixed) $a > 1$ and any $\epsilon > 0$, there exists a function $r$ such that ${|{{r{(x)}} - {\log{(x)}}}|} \leq \epsilon$ for all $x \in {\lbrack{1/a},a\rbrack}$, and $r$ has a semidefinite representation of size $O{(\sqrt{\log_{e}{({1/\epsilon})}})}$.

### Proof

The main point here is that it is the combination of Padé approximants with successive square rooting that allows us to get a rate of $O{(\sqrt{\log{({1/\epsilon})}})}$. Using either technique individually gives us a rate of $O{({\log{({1/\epsilon})}})}$. Figure 1 shows the error $|{{r_{m,k}{(x)}} - {\log{(x)}}}|$ for different choices of $(m,k)$.

Figure 1: Plot of the error |rm, k (x) − log (x)| for different choices of (m, k). Left: m = k. Right: pairs (m, k) such that m + k = 6.

### The (scalar) relative entropy cone

The relative entropy is defined as the perspective function of the negative logarithm: ${(x,y)} \in {{\mathbb{R}}_{+ +} \times {\mathbb{R}}_{+ +}}\mapsto{x{\log{({x/y})}}}$. The epigraph of this function is known as the *relative entropy cone*: Using the perspective of $r_{m,k}$ one can obtain a semidefinite approximation of $K_{\text{re}}$. Let The following theorem gives an approximation error for the cone $K_{m,k}$.

### Theorem 2 (Approximation error for $K_{\text{re}}$)

Let $a > 1$ and $\epsilon > 0$. Then there exist $m$ and $k$ with ${m + k} = {O{(\sqrt{\log_{e}{({1/\epsilon})}})}}$ such that: if $0 < {a^{- 1}y} \leq x \leq {ay}$ and ${(x,y,t)} \in K_{\text{re}}$ then ${(x,y,{t + {x\epsilon}})} \in K_{m,k}$ if $0 < {a^{- 1}y} \leq x \leq {ay}$ and ${(x,y,t)} \in K_{m,k}$ then ${(x,y,{t + {x\epsilon}})} \in K_{\text{re}}$.

### Proof

The proof is straightforward using Theorem 1. Theorem 1 says that there exist $(m,k)$ with ${m + k} = {O{(\sqrt{\log_{e}{({1/\epsilon})}})}}$ such that ${|{{r_{m,k}{(x)}} - {\log{(x)}}}|} < \epsilon$ on $\lbrack a^{- 1},a\rbrack$. Now, if ${(x,y,t)} \in K_{\text{re}}$ this means that ${x{\log{({x/y})}}} \leq t$. Since ${x/y} \in {\lbrack a^{- 1},a\rbrack}$, we get that which means that ${(x,y,{t + {x\epsilon}})} \in K_{m,k}$. The other direction is similar. ∎ A semidefinite representation of $K_{m,k}$ appears as the case $n = 1$ of Theorem 3. ‣ 3.2 Approximating the operator relative entropy cone ‣ 3 Operator concavity, noncommutative perspectives and the operator relative entropy cone ‣ Semidefinite approximations of the matrix logarithm") to follow. Note that, in this scalar case, the approximation involves only $2 \times 2$ linear matrix inequalities and thus can be formulated using second-order cone programming.

## Operator concavity, noncommutative perspectives and the operator relative entropy cone

The main goal of this section is to show that the ideas presented in the previous section are still valid when working with matrices. The main result of this section (and of the paper) is Theorem 3. ‣ 3.2 Approximating the operator relative entropy cone ‣ 3 Operator concavity, noncommutative perspectives and the operator relative entropy cone ‣ Semidefinite approximations of the matrix logarithm"), which gives an explicit semidefinite programming approximation of the *operator relative entropy cone*, a matrix generalization of the relative entropy cone.

We begin by showing that the approximation $r_{m,k}$, defined , is operator concave, just like the logarithm function. We then show how to use the noncommutative perspective of $r_{m,k}$ to approximate the operator relative entropy. This leads to our explicit semidefinite approximation of the operator relative entropy cone. We then show how this can be used to approximate the quantum relative entropy.

### Operator concavity of logarithm and its approximation

We have already mentioned in the introduction that the logarithm function is *operator concave*. The next proposition will allow us to show this, as well as the operator concavity of the rational function $r_{m}$ that we considered in the previous section.

### Proposition 2

For $t \in {\lbrack 0,1\rbrack}$ let $f_{t}$ be the rational function defined . Then $f_{t}$ is operator concave. In fact we have the following semidefinite representation of its matrix hypograph:

### Proof

The fact that $f_{t}$ is operator concave will follow directly once we establish, since it will show that the matrix hypograph of $f_{t}$ is a convex set. The proof of is based on Schur complements, and is given in Appendix C. ∎ We can now directly see that $\log$ is operator concave, since it is a nonnegative (integral) combination of the $f_{t}$. The same is also true for $r_{m}$, since it is defined as a finite nonnegative combination of the $f_{t}$. Since $f_{t}$ is semidefinite representable, we can also get a semidefinite representation of the matrix hypograph of $r_{m}$, i.e., $\{{(Y,U)}:{{r_{m}{(Y)}} \succeq U}\}$. This is the special case of Theorem 3. ‣ 3.2 Approximating the operator relative entropy cone ‣ 3 Operator concavity, noncommutative perspectives and the operator relative entropy cone ‣ Semidefinite approximations of the matrix logarithm") with ${k = 0},{U = {- T}}$ and $X = I$.

### Operator concavity of $r_{m,k}$

In Section 2 we saw that one can get an improved approximation of $\log$ by considering ${r_{m,k}{(x)}}:={2^{k}r_{m}{(x^{1/2^{k}})}}$. We now show that $r_{m,k}$ is also operator concave. The argument directly generalizes the proof that $r_{m,k}$ is concave (in the usual sense). For the generalization we need the notion of *operator monotonicity*. A function $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}}$ is called *operator monotone* if whenever $X \succeq Y$ then ${g{(X)}} \succeq {g{(Y)}}$, where ${X,Y} \in \mathbf{H}_{+ +}^{n}$ for any $n$.

### Proposition 3

The function $r_{m,k}$ is operator concave.

### Proof

One can show that the functions $f_{t}$, for each fixed $t \in {}$, are operator monotone in addition to being operator concave: this follows from the fact that $X \succeq Y \succ 0\Longrightarrow X^{- 1} \preceq Y^{- 1}$. Since $r_{m}$ is a nonnegative combination of the $f_{t}$ it is also operator monotone and operator concave. It is well-known that the power functions $x\mapsto x^{1/2^{k}}$ are operator concave, see e.g.,. Finally it is not hard to show that the composition of an operator concave and monotone function, with an operator concave function, yields an operator concave function. Thus this proves operator concavity of $r_{m,k}$. ∎ We will see, by setting $X = I$ and $U = {- T}$ in Theorem 3. ‣ 3.2 Approximating the operator relative entropy cone ‣ 3 Operator concavity, noncommutative perspectives and the operator relative entropy cone ‣ Semidefinite approximations of the matrix logarithm") to follow, how to get an explicit semidefinite representation of the matrix hypograph, $\{{(Y,U)}:{{r_{m,k}{(Y)}} \succeq U}\}$, of $r_{m,k}$.

### Approximating the operator relative entropy cone

Recall that the operator relative entropy is the noncommutative perspective of the negative logarithm function: We know that $D_{\text{op}}$ is jointly matrix concave in $(X,Y)$. In particular, this means that the epigraph cone associated to $D_{\text{op}}$ is a convex cone: We saw, in Proposition 3, that $r_{m,k}$ is operator concave. It thus follows that the noncommutative perspective of $r_{m,k}$ is jointly concave. Our approximation of the cone $K_{\text{re}}^{n}$ will be the epigraph cone of $- P_{r_{m,k}}$, the noncommutative perspective of $- r_{m,k}$. We will denote this cone by $K_{m,k}^{n}$: The next theorem, which is the main result of this paper, gives an explicit semidefinite representation of the cone.

### Theorem 3 (Main: semidefinite approximation of $K_{\text{re}}^{n}$)

The cone $K_{m,k}^{n}$ defined in has the following semidefinite description: where $w_{j}$ and $t_{j}$ ($j = {1,\ldots,m}$) are the weights and nodes for the $m$-point Gauss-Legendre quadrature on the interval $\lbrack 0,1\rbrack$.

### Proof

To prove this theorem we need the notion of *weighted matrix geometric mean*. For $0 < h < 1$, the $h$-weighted matrix geometric mean of ${A,B} \succ 0$ is denoted $A\#_{h}B$ and defined: Note that $A\#_{h}B$ is the noncommutative perspective of the power function $x\mapsto x^{h}$. The weighted matrix geometric mean is operator concave in $(A,B)$ and semidefinite representable. Semidefinite representations of $A\#_{h}B$ for any rational $h$ are shown in \[, \].

Recall that $P_{r_{m}}$ is the noncommutative perspective of $r_{m}$. Since ${r_{m,k}{(X)}} = {2^{k}r_{m}{(X^{1/2^{k}})}}$, it is not difficult to verify that the noncommutative perspective $P_{r_{m,k}}$ of $r_{m,k}$ can be expressed as: The semidefinite representation (16. ‣ 3.2 Approximating the operator relative entropy cone ‣ 3 Operator concavity, noncommutative perspectives and the operator relative entropy cone ‣ Semidefinite approximations of the matrix logarithm")) then follows from the following three facts: *Semidefinite representation of weighted matrix geometric means*: For any ${X,Y} \succ 0$ and $V \in \mathbf{H}^{n}$ and $k \geq 1$ we have ${X\#_{2^{- k}}Y} \succeq V$ if and only if there exist ${Z_{0},\ldots,Z_{k}} \in \mathbf{H}^{n}$ that satisfy: This is the case $h = {1/2^{k}}$ of the semidefinite representation that appears. This construction hinges on the fact that $X\#_{2^{- k}}Y$ can be expressed in terms of $k$ nested geometric means as $X\#_{1/2}{({X\#_{1/2}{({\ldots{({X\#_{1/2}Y})}})}})}$, the fact that and operator monotonicity of the geometric mean with respect to its arguments.

*Semidefinite representation of $P_{r_{m}}$*: For any ${V,X} \succ 0$ and $T \in \mathbf{H}^{n}$ we have ${P_{r_{m}}{(V,X)}} \succeq T$ if and only if there exist $T_{1},\ldots,T_{m}$ that satisfy: This follows directly from the semidefinite representation of $P_{f_{t}}$ given in Proposition 8 (Appendix C) and the fact that $r_{m} = {\sum_{j = 1}^{m}{w_{j}f_{t_{j}}}}$. $P_{r_{m}}$ is monotone in its first argument. This easily follows from the monotonicity of $r_{m}$.

Combining these three ingredients, and using the expression of $P_{r_{m,k}}$ in Equation, yields the desired semidefinite representation (16. ‣ 3.2 Approximating the operator relative entropy cone ‣ 3 Operator concavity, noncommutative perspectives and the operator relative entropy cone ‣ Semidefinite approximations of the matrix logarithm")). ∎

### Quantum relative entropy

In this section, we see how to use the results from the previous section to approximate the (Umegaki) quantum relative entropy function, defined by The next proposition, which appears, shows how to express the epigraph of $D$ using the operator relative entropy cone (defined in Equation).

### Proposition 4 (\[, Section 8.8\])

Let $D$ be the relative entropy function and $D_{\text{op}}$ be the operator relative entropy. Then for any ${A,B} \succ 0$ we have where $\phi$ is the unique linear map from ${\mathbb{C}}^{n^{2} \times n^{2}}$ to $\mathbb{C}$ that satisfies ${\phi{({X \otimes Y})}} = {{Tr}{\lbrack{XY^{T}}\rbrack}}$, and $\overline{B}$ is the entrywise complex conjugate of $B$.

### Proof

We reproduce the proof in \[, Section 8.8\]. Observe that $A \otimes I$ and $I \otimes \overline{B}$ commute and, as such, ${D_{\text{op}}{({{A \otimes I} \parallel {I \otimes \overline{B}}})}} = {{({A \otimes I})}{({{\log{({A \otimes I})}} - {\log{({I \otimes \overline{B}})}}})}}$. Using the fact that ${\log{({X \otimes Y})}} = {{{({\log X})} \otimes I} + {I \otimes {({\log Y})}}}$, the previous equation simplifies to ${D_{\text{op}}{({{A \otimes I} \parallel {I \otimes \overline{B}}})}} = {{{({A{\log A}})} \otimes I} - {A \otimes {({\log\overline{B}})}}}$. Now, using the fact ${\phi{({X \otimes Y})}} = {{Tr}{\lbrack{XY^{T}}\rbrack}}$, we immediately see that (21. ‣ 3.3 Quantum relative entropy ‣ 3 Operator concavity, noncommutative perspectives and the operator relative entropy cone ‣ Semidefinite approximations of the matrix logarithm")) holds. ∎ The previous proposition allows us to express the epigraph of the quantum relative entropy function in terms of the operator relative entropy cone. This is the object of the next statement.

### Corollary 1

For any ${A,B} \succ 0$ and $\tau \in {\mathbb{R}}$ we have:

### Proof

Straightforward from (21. ‣ 3.3 Quantum relative entropy ‣ 3 Operator concavity, noncommutative perspectives and the operator relative entropy cone ‣ Semidefinite approximations of the matrix logarithm")), and the fact that $X \preceq Y$ implies ${\phi{(X)}} \leq {\phi{(Y)}}$ (see Remark 1 below). ∎ One can then get a semidefinite approximation of the constraint ${D{({A \parallel B})}} \leq \tau$ by using the approximation given in of the cone $K_{\text{re}}^{n^{2}}$ and plugging it. Note that the semidefinite approximation we thus get uses blocks of size ${{2n^{2}} \times 2}n^{2}$, because of the tensor product construction of Equation (21. ‣ 3.3 Quantum relative entropy ‣ 3 Operator concavity, noncommutative perspectives and the operator relative entropy cone ‣ Semidefinite approximations of the matrix logarithm")).

### Remark 1

Note that the linear map $\phi$ in Proposition 4. ‣ 3.3 Quantum relative entropy ‣ 3 Operator concavity, noncommutative perspectives and the operator relative entropy cone ‣ Semidefinite approximations of the matrix logarithm") is given by ${\phi{(Z)}} = {w^{\ast}Zw}$ for $Z \in {\mathbb{C}}^{n^{2} \times n^{2}}$, where $w \in {\mathbb{C}}^{n^{2}}$ is the vector obtained by stacking the columns of the $n \times n$ identity matrix. It follows that $\phi$ is a positive linear map, in the sense that if $Z \succeq 0$ then ${\phi{(Z)}} \geq 0$.

### A smaller representation

One can exploit the special structure of the linear map $\phi$ in (21. ‣ 3.3 Quantum relative entropy ‣ 3 Operator concavity, noncommutative perspectives and the operator relative entropy cone ‣ Semidefinite approximations of the matrix logarithm")), to reduce the size of the semidefinite approximation of $D{({A \parallel B})}$ from having $m + k$ blocks of size ${{2n^{2}} \times 2}n^{2}$, to having $m$ blocks of size ${({n^{2} + 1})} \times {({n^{2} + 1})}$ and $k$ blocks of size ${{2n^{2}} \times 2}n^{2}$. The main idea for this reduction is to observe that the rational function $f_{t}$, which is the main building block of our approximations, can be expressed as a Schur complement, namely we have ${tP_{f_{t}}{(X,Y)}} = {Y - {Y{({Y + {t{({X - Y})}}})}^{- 1}Y}}$. From this observation, one can get the following representation for the hypograph $v^{\ast}P_{f_{t}}{(X,Y)}v$, where $v \in {\mathbb{C}}^{n}$: This representation clearly has size ${({n + 1})} \times {({n + 1})}$. Combining this with the fact that $\phi$ has the form ${\phi{\lbrack X\rbrack}} = {w^{\ast}Xw}$ (see Remark 1), allows us to reduce the semidefinite approximation of $D{({A \parallel B})}$.

## Approximating operator concave functions

The approximations to the relative entropy cone developed in Section 3 used the facts that the logarithm is an integral of (semidefinite representable) rational functions, which can be approximated via quadrature; and the logarithm obeys the functional equation ${\log{(\sqrt{x})}} = {\frac{1}{2}{\log{(x)}}}$.

In this section we show how to generalize these ideas, allowing us to give semidefinite approximations for convex cones of the form for a range of operator concave functions $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}}$, where $P_{g}{(X,Y)}$ is the noncommutative perspective of $g$ defined. In Section 4.1, we discuss functions that admit similar integral representations to the logarithm, which can be approximated via quadrature. In Section 4.2, we present examples of functions with perspectives $P_{g}$ that obey functional equations of the form ${P_{g} \circ \Phi} = P_{g}$ where $\Phi$ is a map with certain monotonicity properties, and use these to obtain smaller semidefinite approximations.

### Approximations via Löwner's theorem

A general class of functions that admit integral representations are operator monotone functions, of which the logarithm is a special case. Recall that these are functions $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}}$ that satisfy ${g{(X)}} \preceq {g{(Y)}}$ whenever $X \preceq Y$ for ${X,Y} \in \mathbf{H}_{+ +}^{n}$ and any $n \geq 1$. The following theorem, due to Löwner, shows that any operator monotone function admits an integral representation in terms of the rational functions $f_{t}$ that we saw earlier (see Appendix D).

### Theorem 4 (Löwner)

If $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}}$ is a non-constant operator monotone function then there is a unique probability measure $\nu$ supported on $\lbrack 0,1\rbrack$ such that where $f_{t}$ is the rational function defined.

The logarithm function corresponds to the case where the measure $\nu$, in (24. ‣ 4.1 Approximations via Löwner’s theorem ‣ 4 Approximating operator concave functions ‣ Semidefinite approximations of the matrix logarithm")), is the Lebesgue measure on $\lbrack 0,1\rbrack$. One corollary of Löwner's theorem is that any operator monotone function on ${\mathbb{R}}_{+ +}$ is necessarily operator concave, since the $f_{t}$ are operator concave, as we already saw. Given an operator monotone function $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}}$ (which is necessarily also operator concave) one can apply Gaussian quadrature on (24. ‣ 4.1 Approximations via Löwner’s theorem ‣ 4 Approximating operator concave functions ‣ Semidefinite approximations of the matrix logarithm")) (with respect to the measure $\nu$) to obtain a rational approximation of $g$. If we use $m$ quadrature nodes, we denote the corresponding rational function $r_{m}$. In Appendix B, we establish an error bound on the resulting approximation, which allows us to prove the following general theorem on semidefinite approximations of operator monotone functions.

### Theorem 5 (Semidefinite approximation of operator monotone functions)

Let $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}}$ be an operator monotone (and hence operator concave) function and let $a > 1$. Then for any $\epsilon > 0$ there is a rational function $r$ such that ${|{{r{(x)}} - {g{(x)}}}|} \leq \epsilon$ for all $x \in {\lbrack{1/a},a\rbrack}$, and $r$ has a semidefinite representation of size $O{({\log{({1/\epsilon})}})}$.

### Proof

We show that $r = r_{m}$ has the desired properties. In Appendix B, Equation, we show that the error $|{{r_{m}{(x)}} - {g{(x)}}}|$ for $x \in {\lbrack{1/a},a\rbrack}$ decays linearly in $m$, i.e., is $O{(\rho^{m})}$ for some constant $0 < \rho < 1$ depending on $a$. In other words if we take $m = {O{({\log{({1/\epsilon})}})}}$ we get ${|{{r_{m}{(x)}} - {g{(x)}}}|} \leq \epsilon$ for all $x \in {\lbrack{1/a},a\rbrack}$. Since each rational function $f_{t}$ has a semidefinite representation of size $2 \times 2$ (see) it follows that $r_{m}$ has a semidefinite representation of size ${O{(m)}} = {O{({\log{({1/\epsilon})}})}}$ as a sum of $m$ such functions. ∎ The approximation $r$ we produce in Theorem 5. ‣ 4.1 Approximations via Löwner’s theorem ‣ 4 Approximating operator concave functions ‣ Semidefinite approximations of the matrix logarithm") is also operator monotone and operator concave, and can be used to approximate the matrix hypograph of $g$, as well as its noncommutative perspective, just like for the logarithm function. The following result quantifies the error for the approximation of the cone $K_{g}^{n}$ (defined in) we obtain this way.

### Theorem 6 (Approximation error for $K_{g}^{n}$)

Let $a > 1$ and $\epsilon > 0$ and let $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}}$ be operator monotone (and hence operator concave). Then there exists $m$ with $m = {O{({\log_{e}{({1/\epsilon})}})}}$ such that: if $0 \prec {a^{- 1}Y} \preceq X \preceq {aY}$ and ${(X,Y,T)} \in K_{g}^{n}$ then ${(X,Y,{T + {X\epsilon}})} \in K_{r_{m}}^{n}$ if $0 \prec {a^{- 1}Y} \leq X \preceq {aY}$ and ${(X,Y,T)} \in K_{r_{m}}^{n}$ then ${(X,Y,{T + {X\epsilon}})} \in K_{g}^{n}$.

### Proof

The proof is a straightforward matrix generalization of the proof of Theorem 2. ‣ The (scalar) relative entropy cone ‣ 2 Approximating logarithm ‣ Semidefinite approximations of the matrix logarithm"). We establish only the first statement, since the second is similar.

If $0 \prec {a^{- 1}Y} \preceq X \preceq {aY}$ then ${a^{- 1}I} \preceq {X^{- {1/2}}YX^{- {1/2}}} \preceq {aI}$. By Theorem 5. ‣ 4.1 Approximations via Löwner’s theorem ‣ 4 Approximating operator concave functions ‣ Semidefinite approximations of the matrix logarithm") there is $m = {O{({\log_{e}{({1/\epsilon})}})}}$ such that ${|{{r_{m}{(x)}} - {g{(x)}}}|} \leq \epsilon$. Hence ${{- {r_{m}{({X^{- {1/2}}YX^{- {1/2}}})}}} + {g{({X^{- {1/2}}YX^{- {1/2}}})}}} \preceq {\epsilonI}$ and so, multiplying on the left and right by $X^{1/2}$, we see that ${{- {P_{r_{m}}{(X,Y)}}} + {P_{g}{(X,Y)}}} \preceq {\epsilonX}$. Since ${(X,Y,T)} \in K_{g}^{n}$, it follows that ${- {P_{g}{(X,Y)}}} \preceq T$ and so that ${- {P_{r_{m}}{(X,Y)}}} \preceq {T + {\epsilonX}}$. This shows that ${(X,Y,{T + {\epsilonX}})} \in K_{r_{m}}^{n}$. ∎ Theorem 5. ‣ 4.1 Approximations via Löwner’s theorem ‣ 4 Approximating operator concave functions ‣ Semidefinite approximations of the matrix logarithm") shows that, by just using Gaussian quadrature on (24. ‣ 4.1 Approximations via Löwner’s theorem ‣ 4 Approximating operator concave functions ‣ Semidefinite approximations of the matrix logarithm")), we can get semidefinite approximations of size $O{({\log{({1/\epsilon})}})}$ for any operator monotone function $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}}$. In the next section we will see that if the function $g$ satisfies additional functional relations, then we can obtain approximations of order $O{(\sqrt{\log{({1/\epsilon})}})}$ or smaller. Before doing so, we consider certain positive-valued functions that will be useful later.

### Positive-valued functions

In the special case when $g$ takes only positive values, one can prove (see Appendix D) an alternative integral representation, that has additional nice properties and takes the form Here, $\mu$ is a probability measure on $\lbrack 0,1\rbrack$ and $f_{t}^{+}$ is the rational function ${f_{t}^{+}{(x)}} = {({{{({1 - t})}x^{- 1}} + t})}^{- 1}$. The main advantage of using this new integral representation instead of (24. ‣ 4.1 Approximations via Löwner’s theorem ‣ 4 Approximating operator concave functions ‣ Semidefinite approximations of the matrix logarithm")), is that the noncommutative perspective of $f_{t}^{+}$ is monotone with respect to both arguments, unlike $f_{t}$. This means that the perspective $P_{g}$ of any positive operator monotone function $g$, is monotone with respect to both arguments. Approximating $g$ by applying quadrature to ensures this property is preserved.

### Examples

The function ${g{(x)}} = x^{1/2}$ is known to be operator monotone and has the integral representation with the measure $\mu$ given by the *arcsine distribution*: Another function known to be operator monotone is ${g{(x)}} = {{({x - 1})}/{\log{(x)}}}$. In this case one can show that the measure $\mu$ in is: More information about operator monotone functions and their integral representations can be found in the books by Bhatia \[, \].

### Improved approximations via functional equations

The functional equation ${\log{(x^{1/2})}} = {{({1/2})}{\log{(x)}}}$ for the logarithm gives rise to a functional equation for the perspective, ${P_{\log}{(x,y)}} = {y{\log{({x/y})}}}$, of the logarithm. Indeed if we define In Section 2 we constructed rational approximations $r_{m}$ for the logarithm, and then improved the approximation quality by successive square-rooting, defining ${r_{m,k}{(x)}} = {2^{k}r_{m}{(x^{1/2^{k}})}}$. At the level of perspectives, we have that where $\Phi^{(k)}$ denotes the composition of $\Phi$ with itself $k$ times.

A similar approach is possible for operator monotone functions $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}_{+ +}}$, that satisfy a functional equation of the form ${P_{g} \circ \Phi} = P_{g}$, as long as $\Phi$ has certain monotonicity and contraction properties. In these cases, we can obtain semidefinite representable approximations to $g$ that have smaller descriptions, for a given approximation accuracy, than the approximations by rational functions given in Theorem 5. ‣ 4.1 Approximations via Löwner’s theorem ‣ 4 Approximating operator concave functions ‣ Semidefinite approximations of the matrix logarithm"). We make this precise in Theorem 7 to follow. For simplicity of notation, we work in the scalar setting, but our arguments all extend to the matrix setting.

Examples of operator monotone functions obeying a functional equation of the desired form come from the logarithmic mean and the arithmetic-geometric mean.: In Section 4.1 we saw that the function ${g{(x)}} = \frac{x - 1}{\log{(x)}}$ is operator monotone. Its perspective is the *logarithmic mean*: a function that arises naturally in problems of heat transfer, and in the Riemannian geometry of positive semidefinite matrices (see, e.g., \[, Section 4.5\]). If we define ${\Phi{(x,y)}} = {({{({x + \sqrt{xy}})}/2},{{({y + \sqrt{xy}})}/2})}$ then the logarithmic mean obeys the functional equation: The logarithmic mean also satisfies other functional equations that are closely related to Borchardt's algorithm and variants for computing the logarithm. These could also be used in the present context, but we focus on for simplicity.

Arithmetic-geometric mean (AGM): The arithmetic-geometric mean of a pair of positive scalars $x,y$, is defined as the common limit of the pair of (convergent) sequences $x_{0} = x$, $y_{0} = y$, This limit is denoted $\text{AGM}{(x,y)}$, and is the perspective of the positive, operator monotone function, ${g{(x)}} = {\text{AGM}{(x,1)}}$. Remarkably (see, e.g., \[, Equation (1.7)\]), the arithmetic-geometric mean is related to the complete elliptic integral of the first kind, $K{(x)}$, via Since it is defined as the limit of an iterative process, if ${\Phi{(x,y)}} = {({{({x + y})}/2},\sqrt{xy})}$ then More examples can be obtained by considering operator monotone functions constructed via operator mean iterations, discussed, for instance,.

### Structure of approximations

Suppose $g:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}_{+ +}}$ is positive and operator monotone, and let $r_{m}^{+}$ be the rational, positive, operator monotone approximation to $g$ obtained by applying Gaussian quadrature (with respect to the measure $\mu$) to the integral representation. If, in addition, ${P_{g} \circ \Phi} = P_{g}$ for some map $\Phi:{{\mathbb{R}}_{+ +}^{2}\rightarrow{\mathbb{R}}_{+ +}^{2}}$, then we can define a two-parameter family of approximations by It makes sense to do this as long as $\Phi$ maps points 'closer' to the ray generated by $$ (in a way made precise in Theorem 7, to follow), and the approximation $r_{m}^{+}$ of $g$ is accurate near $x = 1$.

From now on we assume that $\Phi$ has the form where ${h_{1},h_{2}}:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}_{+ +}}$ are positive, operator monotone, functions. Observe that $\Phi$ has this form for the examples of the logarithmic mean and the arithmetic-geometric mean. If $\Phi$ has the form, then $P_{r_{m,k}}{(x,y)}$ (defined in) is positive, jointly concave, and jointly monotone for all $k \geq 0$ and $m \geq 1$. In particular, these monotonicity and concavity properties ensure that the cones $K_{m,k}:=K_{r_{m,k}}$ can be (recursively) expressed as $K_{m,0} = K_{r_{m}^{+}}$ and for all $k \geq 1$. If the cones $K_{h_{1}}$ and $K_{h_{2}}$ associated with $h_{1}$ and $h_{2}$ have semidefinite descriptions of size $s_{1}$ and $s_{2}$ respectively, then $K_{m,k}$ has a semidefinite description of size ${2m} + {k{({s_{1} + s_{2}})}}$.

### Approximation error

The following result shows that if $\Phi$ has contraction and monotonicity properties, we can obtain smaller semidefinite approximations of nonnegative operator monotone functions $g$ satisfying a functional equation of the form ${P_{g} \circ \Phi} = P_{g}$. It allows us to get semidefinite approximations of size $O{(\sqrt{\log{({1/\epsilon})}})}$ if $\Phi$ contracts at a linear rate, and $O{({\log{\log{({1/\epsilon})}}})}$ if $\Phi$ contracts quadratically, where $\epsilon$ is the approximation accuracy.

### Theorem 7

Let ${g,h_{1},h_{2}}:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}_{+ +}}$ be operator monotone (and hence operator concave) functions such that Suppose that $h_{1}$ and $h_{2}$ are semidefinite representable.

If there exists a constant $c > 1$ such that then for any $a > 1$ and any $\epsilon > 0$ there is a function $r$ such that ${|{{r{(x)}} - {g{(x)}}}|} \leq \epsilon$ for all $x \in {\lbrack{1/a},a\rbrack}$ and $r$ has a semidefinite representation of size $O{(\sqrt{\log_{c}{({1/\epsilon})}})}$.

If, in addition, there exists a constant $c_{0} > 1$ such that then for any $a > 1$ and any $\epsilon > 0$ there is a function $r$ such that ${|{{r{(x)}} - {g{(x)}}}|} \leq \epsilon$ for all $x \in {\lbrack{1/a},a\rbrack}$ and $r$ has a semidefinite representation of size $O{({\log_{2}{\log_{c_{0}}{({1/\epsilon})}}})}$.

### Proof

We provide a proof in Appendix B.2.3. In each case we choose $r$ to be of the form ${r_{m,k}{(x)}} = {P_{r_{m,k}}{(x,1)}}$ (defined in ) for sufficiently large $m$ and $k$, and use the fact that $r_{m,k}$ has a semidefinite representation of size $O{({m + k})}$. ∎

### Remark 2

The condition says that ${d_{H}{({\Phi{(x,y)}},{})}} \leq {c^{- 1}d_{H}{({(x,y)},{})}}$ where $d_{H}{( \cdot, \cdot )}$ is the *Hilbert metric* on rays of the cone ${\mathbb{R}}_{+ +}^{2}$ (see, e.g., ). This is the precise sense in which $\Phi$ maps points 'closer' to the ray generated by $$.

We now apply the theorem to the logarithmic mean and the arithmetic-geometric mean.

### Logarithmic mean

In this case ${g{(x)}} = \frac{x - 1}{\log{(x)}}$, ${h_{1}{(x)}} = {{({x + \sqrt{x}})}/2}$, and ${h_{2}{(x)}} = {{({1 + \sqrt{x}})}/2}$. By a direct computation we see that Theorem 7 tells us that given $a > 1$, there is a function $r:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}_{+ +}}$ with a semidefinite representation of size $O{(\sqrt{\log_{2}{({1/\epsilon})}})}$, such that ${|{{r{(x)}} - {{({x - 1})}/{\log{(x)}}}}|} \leq \epsilon$ for all $x \in {\lbrack{1/a},a\rbrack}$.

### Arithmetic-Geometric mean

Furthermore, since ${\log{\cosh{(z)}}} \leq {|z|}$ for all $z$ and ${\log{\cosh{(z)}}} \leq {z^{2}/2}$ for all $z$, it follows that Theorem 7 tells us that given $a > 1$, there is a function $r:{{\mathbb{R}}_{+ +}\rightarrow{\mathbb{R}}_{+ +}}$ with a semidefinite representation of size $O{({\log_{2}{\log_{8}{({1/\epsilon})}}})}$ such that ${|{{r{(x)}} - {\text{AGM}{(x,1)}}}|} \leq \epsilon$ for all $x \in {\lbrack{1/a},a\rbrack}$.

### Remark 3

As stated, both the construction of the functions $r_{m,k}$ in Section 4.2.1, and the statement of Theorem 7, are only valid when $g$ takes positive values. If $g$ is operator monotone but not positive-valued (as is the case for the logarithm), similar results apply if certain modifications are made. First, the rational functions $r_{m}$ (from Section 4.1) should be used in place of $r_{m}^{+}$ . Second, we need the additional assumption that the second argument of $\Phi$ is linear (i.e., $h_{2}{(x)}$ is affine). This is required because $P_{r_{m}}$ is, in general, not monotone in its second argument.

## Numerical experiments

We first evaluate our approximation method for the scalar relative entropy cone, and compare it with the successive approximation scheme of CVX, to solve maximum entropy problems and geometric programs. To assess the quality of the returned solutions, we use the solver Mosek, which has a dedicated routine for entropy problems and geometric programming (mskenopt and mskgpopt respectively). Note, however, that this solver only deals with scalar problems, and has no facility for matrix problems involving quantum relative entropy, for instance. To evaluate our method for matrices, we test it on a variational formula for trace. More numerical experiments using CvxQuad related to problems in quantum information theory appear.

### Entropy problems

We consider optimization problems of the form and we compare the performance of our method with the successive approximation scheme implemented in CVX. Table 2 shows the results of the comparison for randomly generated data $A \in {\mathbb{R}}^{\ell \times n}$ and $b \in {\mathbb{R}}^{\ell}$ of different sizes. We use the solution returned by the built-in maximum entropy solver in Mosek (mskenopt) as "true solution" and we measure the quality of either approximation method (successive approximation or ours) via the gap between optimal values. We use the notation $p_{sa}$ and $p_{Pade}$ respectively for the optimal values returned by the successive approximation scheme and our method.

Table 2: Maximum entropy optimization via our method and the successive approximation scheme of CVX on different random instances. We see that our method can be much faster than the successive approximation method while having the same accuracy. The accuracy of the different methods is measured via the difference |p − pMosek| where pMosek is the optimal value returned by the built-in Mosek solver for maximum entropy problems (mskenopt), and p is the optimal value returned by the considered approximation method. For our method we used the parameters (m, k) =. The last column also gives the gap between the optimal value returned by the two different approximation methods.

### Geometric programming

We consider now geometric programming problems of the form: where $x \in {\mathbb{R}}^{n}$ is the decision variable. For $a \in {\mathbb{R}}_{+ +}^{n}$ the notation $x^{a}$ indicates $x^{a}:={\prod_{i = 1}^{n}x_{i}^{a_{i}}}$. The coefficients $c_{j,k}$ are assumed to be positive. Such problems can be converted into conic problems over the relative entropy (exponential) cone using the change of variables $y_{i} = {\log x_{i}}$. The current version of CVX (CVX 2.1) uses the successive approximation technique to deal with such problems. Our method based on Padé approximations can also be used in this case to obtain accurate approximations. We note that the solver Mosek has a dedicated routine for geometric programming (mskgpopt).

Table 3 shows a comparison of our method with the successive approximation method for randomly generated instances of. The instances were generated using the mkgp script contained in the ggplab package available at Table 3: Geometric programming using our method (with (m, k) =) and the successive approximation scheme of CVX, on different random instances. The column “sp” indicates the sparsity of the power vectors aj, k (i.e., how many variables appear in each monomial terms). Also we used w0 = w1 = ⋯ = wℓ = 5 (i.e., the posynomial objective as well as the posynomial constraints all have 5 terms). Accuracy is measured via absolute error between the optimal value returned by the approximation and the built-in Mosek solver for geometric programs (mskgpopt).

### Variational formula for trace

We now evaluate our method for matrix functions. We consider the following variational expression for the trace function which appears in \[, Lemma 6\]. For any $Y \succ 0$ where $D$ is the quantum relative entropy function. We generate random positive definite matrices $Y$ and compare the solution of the right-hand side of with ${Tr}{\lbrack Y\rbrack}$. The right-hand side of can be implemented using the CVX code shown in Table 4. The results of running this piece of code using solver SDPT3 are shown in Table 4.

3 maximize (trace(X) - quantum_rel_entr(X,Y)) Table 4: Result of solving the optimization problem for different Hermitian positive definite matrices Y of size n × n with Tr[Y] = 1. The problems were implemented using CVX as shown above and solved using SDPT3. The accuracy column reports the quantity |p − 1| where p is the optimal value returned by the solver (note that the matrix Y is sampled to have trace one).

## Discussion

### Lower bounds

It would be interesting to know what is the smallest possible second-order cone program that can approximate logarithm to within a fixed $\epsilon > 0$. To formalize this question, let $\mathcal{F}_{s}$ be the class of concave functions on ${\mathbb{R}}_{+ +}$ that admit a second-order cone representation of size at most $s$.

Recall, from Theorem 1, that our construction yields ${s{(\epsilon)}} = {O{(\sqrt{\log{({1/\epsilon})}})}}$. This rate results from the combination of Padé approximation with successive square rooting. It would be interesting to produce lower bounds on $s{(\epsilon)}$.

More generally one can define a notion of *$\epsilon$-approximate extension complexity* of a concave function $g:{{\lbrack a,b\rbrack}\rightarrow{\mathbb{R}}}$ in a similar way as. Well-known results in classical approximation theory relate the approximation quality using polynomials and rational functions of given degree to the smoothness of $g$. A natural question is to understand what corresponding properties of a concave function make it more or less difficult to approximate using second-order programs. We have phrased the question here in terms of second-order cone representations for concreteness but the same question for linear programming and semidefinite programming can also be considered.

### Smaller semidefinite approximations for quantum relative entropy

The approximations for the epigraph of the quantum relative entropy $D{({A \parallel B})}$ we constructed in Section 3.3 involve linear matrix inequalities of size $O{(n^{2})}$ (where $n$ is the size of the matrices $A,B$). Is it possible to obtain approximations, of similar quality, to the quantum relative entropy using linear matrix inequalities of size $O{(n)}$?

### Self-concordant barriers for the operator relative entropy cone

A natural approach to conic optimization over the scalar relative entropy cone (or, equivalently, the exponential cone) is to use an interior point method that works directly with an efficiently computable self-concordant barrier for the cone (such as the barrier introduced by Nesterov ). Examples of such solvers include the extension of ECOS to the exponential cone, and the solver developed by Skajaa and Ye. We are not aware, however, of any barrier for the operator relative entropy cone that is known to be efficiently computable and self-concordant. If we had such a barrier, it could be used directly to solve conic optimization problems over the operator relative entropy cone using interior point methods, as an alternative to the semidefinite approximation-based approaches developed in this paper.

### Approximating other families of convex functions via quadrature

One of the basic ideas of this paper is that if we can express a convex (or concave) function as ${g{(x)}} = {\int_{\alpha}^{\beta}{K{(x,t)}{d\mu}{(t)}}}$, where $x\mapsto{K{(x,t)}}$ has a simple semidefinite representation for fixed $t$, then we can obtain a semidefinite approximation of $g$ by quadrature. Operator monotone functions on ${\mathbb{R}}_{+ +}$, such as the logarithm, are just one class of functions with such a representation. Other such families of functions include Stieltjes functions, and certain hypergeometric functions. For instance Stieltjes functions on ${\mathbb{R}}_{+ +}$ have the form ${g{(x)}} = {\int_{0}^{\infty}{\frac{1}{x + t}{d\mu}{(t)}}}$. Hypergeometric functions ${{}_{2}^{}F_{1}^{}}{(a,b;c;x)}$ for $x < 1$ and ${b,c} > 0$ have the form ${{{}_{2}^{}F_{1}^{}}{(a,b;c;x)}} = {\frac{1}{B{(b,{c - b})}}{\int_{0}^{1}{t^{b - 1}{({1 - t})}^{c - b - 1}{({1 - {xt}})}^{- a}{dt}}}}$ where $B{( \cdot, \cdot )}$ is the beta function. We expect such integral representations to be helpful in the study of approximate extension complexity of functions.

### Free semidefinite representation

The semidefinite representation given in this paper of the hypograph of $f_{t}$ (see ) is a "free linear matrix inequality" representation in the sense of. This is one reason why our representations also work for the noncommutative perspective of $f_{t}$. In fact one can show that if an operator concave function $f$ admits a free linear matrix inequality representation, then the noncommutative perspective of $f$ also has a free linear matrix inequality representation. An interesting question would be to understand the class of operator concave functions that admit a free LMI representation.
