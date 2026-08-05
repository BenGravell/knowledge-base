<!-- arxiv-full-text:v1 {"arxiv_id": "1812.04074", "source": "ar5iv"} -->

## Introduction

### Geometric and generalized geometric programs

A geometric program (GP) is a nonlinear mathematical optimization problem in which all the variables are positive and the objective and constraint functions are either monomial functions or posynomial functions. A monomial is any real-valued function given by $x\mapsto{cx_{1}^{a_{1}}x_{2}^{a_{2}}\cdotsx_{n}^{a_{n}}}$, where $x = {(x_{1},x_{2},\ldots,x_{n})}$ is a vector of positive real variables, the coefficient $c$ is positive, and the exponents $a_{i}$ are real; a posynomial function is any sum of monomial functions. A GP is an optimization problem of the form where the functions $f_{i}$ are posynomials, the functions $g_{i}$ are monomials, and $x \in \text{R}_{+ +}^{n}$ is the decision variable. ($\text{R}_{+ +}$ denotes the set of positive reals.)

The problem is not convex, but it can be transformed to a convex optimization problem by a well-known transformation. We can make the change of variables $u = {\log x}$ (meant elementwise) and take the logarithm of the objective and constraint functions to obtain the equivalent problem which can be verified to be convex \[, §4.5.3\]. (The exponential $e^{u}$ is meant elementwise.) Because GPs are reducible to convex programs, they can be solved efficiently and reliably using any algorithm for convex optimization, such as interior-point methods or first-order methods \[BPC+11\]. When all $f_{i}$ are monomials, the problem reduces to a general linear program (LP), so GP is a generalization of LP.

Since its introduction four decades ago, geometric programming has found application in chemical engineering, environment quality control, digital circuit design \[BKP+05\], analog and RF circuit design \[, LGX+04, \], transformer design, communication systems \[ CTP+07\], biotechnology \[MSVGA+07, VGAMS+10\], epidemiology \[PZE+14\], optimal gas flow \[MFB+15\], tree-water-network control, and aircraft design \[ \]. This list is far from exhaustive; for many other examples, see §10.3 of \[BKV+07\].

Evidently monomials and posynomials are closed under various operations. For example, monomials are closed under multiplication, division, and taking powers, while posynomials are closed under addition, multiplication, and division by monomials. A *generalized posynomial* is defined as a function formed from monomials using the operations addition, multiplication, positive power, and maximum. Generalized posynomials, which include posynomials, are also convex under a logarithmic change of variable, after taking the log of the function. It follows that a *generalized geometric program* (GGP), i.e., a problem of the form, with $f_{i}$ generalized posynomials and $g_{i}$ monomials, transforms to a convex problem in \[BKV+07, §5\], and therefore is tractable.

### Log-log convex programs

Figure 1: Hierarchy of optimization problems.

For a function $f:{D\rightarrow\text{R}_{+ +}}$, with $D \subseteq \text{R}_{+ +}^{n}$, we refer to the function ${F{(u)}} = {{\log f}{(e^{u})}}$, with domain $\{ u\mid{e^{u} \in D}\}$, as its *log-log transformation*. We refer to a function $f$ as *log-log convex* if $F$ is convex, *log-log concave* if $F$ is concave, and *log-log affine* if $F$ is affine. As in convex analysis, we can consider the analog of extended-value extensions \[, §3.1.2\]: we allow a log-log convex function to take the value $+ \infty$, and a log-log concave function to take the value zero, which corresponds to $F$ taking the value $- \infty$. A function is log-log affine if and only if it is a monomial; posynomials and generalized posynomials are log-log convex, but there are log-log convex functions that are not generalized posynomials (examples are given in §2.3 and §2.4).

An optimization problem of the form, with $f_{i}$ log-log convex and $g_{i}$ log-log affine, is called a *log-log convex program* (LLCP). The set of LLCPs is a strict superset of GGPs. The hierarchy of LPs, GPs, GGPs, and LLCPs is shown in figure 1.

Log-log convexity is also known as geometric convexity or multiplicative convexity, since it is equivalent to convexity with respect to the geometric mean (see §2.1). studied the class of log-log convex functions many decades ago, in the context of subharmonic functions. More recently, developed a theory of inequalities derived from log-log convexity, parallel to the theory of convex functions, studied the log-log convexity of certain operator polynomials, and examined the log-log concavity of various univariate probability distributions. See also \[ ÖYG14\] for related work.

Many functions can be well-approximated by log-log convex functions \[BKV+07 \], but the lack of a coherent modeling framework for LLCPs has hindered their use in practical applications. The point of this paper is to close that gap.

### Domain-specific languages for convex optimization

Disciplined convex programming (DCP) describes a subset of convex programs generated by a single rule and a set of *atoms*, functions with known curvature (convex, concave, or affine) and monotonicity. DCP is a natural starting point for building a domain-specific language (DSL) for convex optimization, i.e., a programming language that parses convex optimization problems expressed in a human-readable form, rewrites them into canonical forms, and supplies the lowered representations to numerical solvers. By abstracting away solvers, DSLs make optimization accessible to researchers and engineers who are not experts in the details of optimization algorithms. Most DSLs for convex optimization have DCP as their foundation; examples include CVX, CVXPY \[, AVD+18\], Convex.jl \[UMZ+14\], and CVXR. For a survey of DSLs for convex optimization, see \[AVD+18, §1\]. Some DSLs, like CVX and Yalmip \[Löf04\], can also parse GPs and GGPs. There also exist DSLs specifically for GPs, including GPKit and GGPLAB \[MKK+06\]. These software packages parse and rewrite GPs and GGPs.

In this paper, we introduce the analog of DCP for log-log convex problems. We refer to our analog of DCP as *disciplined geometric programming* (DGP). Like DCP, every disciplined geometric program is generated by a single rule and a library of atoms. The class of disciplined geometric problems is a subclass of log-log convex problems (and of course depends on the library of atoms), and, with a sensible atom library, a strict superset of both geometric programming and generalized geometric programming. In §2, we characterize log-log convexity and give many examples of log-log convex functions, some obvious and some less so; when appropriate, we also supply graph implementations. In §3, we present DGP, along with a verification procedure that we articulate in terms of mathematical expression trees. We close in §4 by describing an implementation of DGP as a reduction to disciplined convex programs in CVXPY 1.0.

## Log-log convexity

### Properties

### Convexity with respect to the geometric mean

Log-log convex functions obey a variant of Jensen's inequality: a function $f$ is log-log convex if and only if for all $x,y$ in the domain of $f$, and for each $\theta \in {\lbrack 0,1\rbrack}$, where $\circ$ is the Hadamard (elementwise) product and the powers are meant elementwise.

### Scalar log-log convex functions

A scalar function $f:{D\rightarrow\text{R}_{+ +}}$, $D \subseteq \text{R}_{+ +}$, is log-log convex if its graph has positive curvature on a log-log plot, as shown in figure 2. If $f$ is additionally twice-differentiable, then it is log-log convex if and only if for all $x \in D$,

### Epigraph

If the set $\{ u\mid{e^{u} \in D}\}$ is convex, $D \subseteq \text{R}_{+ +}^{n}$, we say that $D$ is a *log-convex* set. The domain of a log-log convex function $f$ is of course a log-convex set. Its epigraph is also a log-convex set. The converse is true as well: if the epigraph of a function is a log-convex set, then the function is log-log convex. These facts follow from the similar rules for convex functions and epigraphs \[, §3.1.7\].

Figure 2: Two log-log convex functions and one log-log concave function.

### Relationship to log-convexity

Log-log convex functions are related to log-convex functions, which are real-valued functions $f$ for which $\log f$ is convex \[, §3.5\]. If $f$ is log-convex and nondecreasing in each of its arguments, then its log-log transformation ${F{(u)}} = {{\log f}{(e^{u})}}$ is log-log convex, as can be seen via the vector composition rule for convex functions \[, §3.2.4\]. Similarly, if $f$ is log-concave and nonincreasing in its arguments, then its log-log transformation is log-log concave. Since every positive concave function is log-concave, it follows that every positive concave function that is nonincreasing in its arguments is also log-log concave.

In some cases, log-log convexity implies log-convexity. A function $f$ is log-convex if and only if for all $x$ and $y$ in its domain and for each $\theta \in {\lbrack 0,1\rbrack}$, In light of this fact and the AM-GM inequality, every nonincreasing log-log convex function is also log-convex, and every nondecreasing log-log concave function is also log-concave.

### Partial minimization

If $f$ is log-log convex in the variables $x$ and $y$, and if $D$ is a log-convex set, then the function is also log-log convex. A similar result holds for log-log concave functions: if $f{(x,y)}$ is log-log concave and $D$ is a log-convex set, then ${g{(x)}} = {\sup_{y \in D}{f{(x,y)}}}$ is log-log concave. These results are translations of identical results for convex functions \[, §3.2.5\].

### Integration

If $f:{{\lbrack 0,a)}\rightarrow{\lbrack 0,\infty)}}$ is continuous and log-log convex (log-log concave) on $(0,a)$, then is also log-log convex (log-log concave) on $(0,a)$ \[, \]. As an example, if $X$ is a real-valued random variable with a continuous log-log concave density $f$ defined on $\lbrack 0,a)$, then the probability that $X$ lies between $0$ and some $x \in {(0,a)}$ is a log-log concave function of $x$. Several common distributions, including the Gaussian, Gibrat, and the Student's $t$, have log-log concave densities \[, §5\].

### Composition rule

A basic result of convex analysis is that a nondecreasing convex function of a convex function is convex. (Similarly, a nonincreasing convex function of a concave function is convex.) These results, along with similar ones for concave functions, are special cases of just one result on the curvature of function compositions, and it is on this single result that DCP is based \[, §6.4\]. An analogous composition rule holds for log-log convex functions, which we provide in full generality below. Its proof is an elementary exercise in convex analysis.

Suppose $h:{D\rightarrow{\text{R}_{+ +} \cup {\{\infty\}}}}$, $D \subseteq \text{R}_{+ +}^{k}$, is log-log convex, nondecreasing in its $i$th argument for each $i$ in an index set $I \subseteq {\{ 1,2,\ldots,k\}}$, and nonincreasing in the arguments indexed by $I^{c}$. For $i = {1,2,\ldots,k}$, let $g_{i}:{D_{i} \subseteq \text{R}_{+ +}^{n}\rightarrow\text{R}_{+ +}}$. Let $f:{{\bigcap D_{i}}\rightarrow{\text{R}_{+ +} \cup {\{\infty\}}}}$ be given by If $g_{i}$ is log-log convex for $i \in I$ and log-log concave for $i \in I^{c}$, then the function $f$ is log-log convex.

A symmetric result holds when $h:{D\rightarrow\text{R}_{+}}$, $D \subseteq \text{R}_{+}^{k}$, is log-log concave: If $g_{i}$ is log-log concave for $i \in I$ and log-log convex for $i \in I^{c}$, then ${f{(x)}} = {h{({g_{1}{(x)}},\ldots,{g_{k}{(x)}})}}$ is log-log concave.

### Some simple examples

We have already seen that monomials are log-log affine and that posynomials and generalized posynomials are log-log convex. In this section we provide several other examples of log-log convex and log-log concave functions.

### Product

The product ${f{(x_{1},x_{2})}} = {x_{1}x_{2}}$ is log-log affine, since ${F{(u)}} = {\log{({e^{u_{1}}e^{u_{2}}})}} = {u_{1} + u_{2}}$ is affine. (This is also clear since $f$ is a monomial.) It follows that the product of log-log affine functions is log-log affine, and (since the product is monotone increasing) the product of log-log convex functions is log-log convex, and the product of log-log concave functions is log-log concave.

### Ratio

The ratio ${f{(x_{1},x_{2})}} = {x_{1}/x_{2}}$ is log-log affine (since it is a monomial), increasing in its first argument and decreasing in its second argument. It follows that the ratio of a log-log convex and a log-log concave function is log-log convex, and that the ratio of log-log concave and a log-log convex function is log-log concave.

### Power

For $a \in \text{R}$, the function given by $x^{a}$ is log-log affine in $x$, since ${\log{(e^{ax})}} = {ax}$. It follows that a power of a log-log affine function is log-log affine. For $a \geq 0$, the power of a log-log convex function is log-log convex, and the power of a log-log concave function is log-log concave. For $a < 0$, the power of a log-log convex function is log-log concave, and the power of a log-log concave function is log-log convex.

### Sum

The function ${f{(x_{1},x_{2})}} = {x_{1} + x_{2}}$ is log-log convex since ${F{(u)}} = {\log{({e^{u_{1}} + e^{u_{2}}})}}$ is convex. It follows that the sum of log-log convex functions is log-log convex. Log-log concavity is *not* in general preserved under addition.

### Max and min

The function ${f{(x)}} = {\max_{i}x_{i}}$ is log-log convex, and the function ${f{(x)}} = {\min_{i}x_{i}}$ is log-log concave. Since both are nondecreasing, it follows that the max of log-log convex functions is log-log convex, and the min of log-log concave functions is log-log concave.

### Sum largest

For $x \in \text{R}_{+ +}^{n}$, the sum of the $r$ largest elements in $x$ is log-log convex, since it can be represented as $\max{\{{{x_{i_{1}} + x_{i_{2}} + \cdots + {x_{i_{r}} \mid i_{1}}} < i_{2} < \cdots < i_{r}}\}}$, which is the max of a finite number of log-log convex functions.

### One-minus

The function ${f{(x)}} = {1 - x}$ with domain $$ is log-log concave, as can be seen by noting that $f$ is concave and decreasing in $x$, or by the fact that the second derivative of its log-log transformation is negative. It is also decreasing in $x$, so we conclude that if $g$ is log-log convex, ${f{({g{(x)}})}} = {1 - {g{(x)}}}$ is log-log concave (with domain $\{ x\mid{{g{(x)}} < 1}\}$).

### Difference

The function ${f{(x)}} = {x_{1} - x_{2}}$, with domain $\{{x > 0}\mid{{x_{1} - x_{2}} > 0}\}$, is log-log concave, increasing in its first argument and decreasing in its second. It follows that the difference of a log-log concave function and a log-log convex function (with obvious domain) is log-log concave.

### Geometric mean

The geometric mean ${f{(x)}} = \left( {\prod_{i = 1}^{n}x_{i}} \right)^{1/n}$ is log-log affine, i.e., a monomial. The geometric mean of log-log convex functions is log-log convex, and likewise for log-log concave functions.

### Harmonic mean

The harmonic mean ${f{(x)}} = {n{({{1/x_{1}} + {1/x_{2}} + \cdots + {1/x_{n}}})}^{- 1}}$ is log-log concave, since it is the reciprocal of a log-log convex function.

### $\ell_{p}$-norm

The $\ell_{p}$-norm ${\| x\|}_{p} = {({{|x_{1}|}^{p} + {|x_{2}|}^{p} + \cdots + {|x_{n}|}^{p}})}^{1/p}$, $p \geq 1$, is log-log convex for $x \in \text{R}_{+ +}^{n}$, since ${\| x\|}_{p}$ with the absolute values removed is a posynomial raised to $1/p$.

### Exponential and logarithm

The function $f$ given by ${f{(x)}} = e^{x}$ for $x > 0$ is log-log convex, since ${F{(u)}} = {{\log f}{(e^{u})}} = e^{u}$, which is convex. Similarly, the logarithm function restricted to $(1,\infty)$ is log-log concave.

### Entropy

The function ${f{(x)}} = {- {x{\log x}}}$ with domain $$ is log-log concave, as can be seen via the composition rule.

### Functions with positive Taylor expansions

Suppose $f:{\text{R}\rightarrow\text{R}}$ is given by a power series ${f{(x)}} = {a_{0} + {a_{1}x} + {a_{2}x^{2}} + \cdots}$, with $a_{i} \geq 0$ and radius of convergence $R$. We restrict $f$ to the domain $(0,R)$. Then $f$ is log-log convex. This is readily shown by noting that the partial sums are posynomials, so $f$ is the pointwise limit of log-log convex functions. As examples, the functions $\sinh$ and $\cosh$ restricted to $(0,\infty)$, $\tan$, $\sec$, and $\csc$ restricted to $(0,{\pi/2})$, $\arcsin$ restricted to $(0,1\rbrack$, and $\log{({{({1 + x})}/{({1 - x})}})}$ restricted to $$ are all log-log convex.

### Complementary CDF of a log-concave density

The complementary cumulative distribution function (CCDF) of a log-concave density is log-log concave. This follows from the fact that the CCDF of a log-concave density is log-concave \[, §3.5.2\] and nonincreasing. As an example, the CCDF of a Gaussian is log-log concave on $(0,\infty)$. The densities of many common distributions, including the uniform, exponential, chi-squared, and beta distributions, are log-concave. For several other examples, see \[, Table 1\].

### Gamma function

The Gamma function is log-convex and nondecreasing for $x \geq 1$ \[, §3.5\]. Hence, the restriction ${\Gamma|}_{\lbrack 1,\infty)}$ is log-log convex.

### Functions of positive matrices

In the following exposition, all inequalities should be interpreted elementwise. For any two vectors $x,y$ in $\text{R}^{n}$, $x \leq y$ if and only if the entries of $y - x$ are all nonnegative, and for any two matrices ${A,B} \in \text{R}^{m \times n}$, we write $A \leq B$ to mean that the entries of $B - A$ are nonnegative. Similarly, $x < y$ means that the entries of $y - x$ are positive, and likewise for $A < B$. If $A > 0$, we will say that $A$ is a positive matrix.

Let $\text{R}_{+ +}^{m \times n}$ denote the set of positive $m$-by-$n$ matrices. The log-log transformation of a function $f:{D \subseteq \text{R}_{+ +}^{m \times n}\rightarrow\text{R}_{+ +}^{p \times q}}$ is ${F{(U)}} = {{\log f}{(e^{U})}}$, defined on $\{ U\mid{e^{U} \in D}\}$, where the logarithm and exponential are meant elementwise. We say that $f$ is log-log convex if $F$ is convex with respect to $\leq$, i.e., if for any $U$, $V$ in the domain of $F$, $\theta \in {\lbrack 0,1\rbrack}$ Equivalently, $f$ is log-log convex if for any ${X,Y} \in D$, $\theta \in {\lbrack 0,1\rbrack}$, where $\circ$ denotes the Hadamard product and the powers are meant elementwise. Informally, we say that $f$ is log-log convex if $f{(X)}$ has log-log convex entries for each $X \in D$.

Of course, the trace of a positive matrix and the product of positive matrices are both log-log convex functions. More interesting is the link between log-log convexity and the Perron-Frobenius theorem, which states, among other things, that every positive square matrix has a positive eigenvalue equal to its spectral radius. We provide a few examples below.

### Spectral radius

Let $X \in \mathbf{R}^{n \times n}$ have positive entries. The Perron-Frobenius theorem states that $X$ has a positive real eigenvalue $\lambda_{\text{pf}}$ equal to its spectral radius, i.e., the magnitude of its largest eigenvalue. It turns out that $\lambda_{\text{pf}}$ is a log-log convex function of $X$. This can be seen by the fact that where the inequalities are elementwise, which implies that $\lambda_{\text{pf}} \leq \lambda$ if and only if The lefthand side of the above inequality is a posynomial in $X_{ij}$, $v_{i}$, and $\lambda$, hence the epigraph of $\lambda_{\text{pf}}$ is log convex. This result is described in more detail in \[, §4.5.4\]. For related material, see \[\].

### Eye-minus-inverse

Let $D$ be the set of positive matrices in $\text{R}^{n \times n}$ with spectral radius $\rho{(X)}$ less than $1$. The function $f:{D\rightarrow\text{R}^{n \times n}}$ given by is log-log convex in $X$, i.e., $f{(X)}$ has log-log convex entries. The function $f$ is well-defined: for any square matrix $X \in D$, the power series $I + X + X^{2} + \cdots$ converges to ${({I - X})}^{- 1}$. One intuitive way to see that $f$ is log-log convex is to note that every partial sum ${s_{n}{(X)}} = {\sum_{i = 0}^{n}X^{i}}$ with $n \geq 1$ has posynomial entries, and therefore is log-log convex. Because $s_{n}\rightarrow f$, we obtain that $f$ is log-log convex.

We can also prove that the function $f$ is log-log convex by studying its epigraph. Let $X > 0$ and $T$ be matrices. Then if and only if there exists a matrix $Y \geq 0$ such that The equivalence between and shows that the epigraph of $f$ is log convex: the set of matrices $X$, $Y$, and $T$ satisfying is log convex, and the epigraph of $f$ is the projection of this set onto its first and third (matrix) coordinates. It is clear that implies, for if $X$ and $T$ satisfy, then $X$, $Y = {({I - X})}^{- 1}$, and $T$ satisfy. For the other direction, assume that the matrices $X > 0$, $Y \geq 0$, and $T$ satisfy. Let $\lambda_{\text{pf}} = {\rho{(X)}} > 0$ be the Perron-Frobenius eigenvalue of $X$ and let $v > 0$ be a corresponding right eigenvector. Multiplying both sides of by $v$, we obtain that $v \leq {{({1 - \lambda_{\text{pf}}})}Tv}$. This necessitates that $\lambda_{\text{pf}} = {\rho{(X)}} < 1$, which together with the fact that $X > 0$ implies that ${({I - X})}^{- 1}$ exists and is positive. Multiplying both sides of by ${({I - X})}^{- 1}$ yields.

### Resolvent

For any square matrix $X$ and any scalar $s > 0$ such that $s$ is not an eigenvalue of $X$, the matrix ${({{sI} - X})}^{- 1}$ is called the resolvent of $X$. The function ${(X,s)}\mapsto{({{sI} - X})}^{- 1}$ is log-log convex in both $s$ and $X$ whenever $X$ has positive entries and ${\rho{(X)}} < s$. This can be seen by writing ${({{sI} - X})}^{- 1}$ as $s^{- 1}{({I - {X/s}})}^{- 1}$.

## Disciplined geometric programming

While it is intractable to determine whether an arbitrary mathematical program is log-log convex, it is easy to check if a composition of atoms (functions with known log-log curvature and monotonicity) satisfies the composition rule given in §2.2. This fact motivates disciplined geometric programming (DGP), a methodology for constructing log-log convex programs from a set of atoms. A problem constructed via disciplined geometric programming is called a disciplined geometric program. If a problem is a disciplined geometric program, we colloquially say that the problem is DGP.

Like DCP, DGP has two key components: an atom library and a grammar for composing atoms. Every function appearing in a disciplined geometric program must be either an atom or a grammatical composition of atoms; a composition is grammatical if it satisfies the rule from §2.2. Concretely, a disciplined geometric program is an optimization problem of the form where the functions $f_{i}$ are log-log convex, the functions ${\overset{\sim}{f}}_{i}$ are log-log concave, the functions $g_{i}$ and ${\overset{\sim}{g}}_{i}$ are log-log affine, $x \in \text{R}_{+ +}^{n}$ is the decision variable, and all the functions are grammatical compositions of atoms. (A problem where the objective is to maximize a log-log concave function and the constraints are as in is also a disciplined geometric program.) Clearly, every disciplined geometric program is an LLCP, but the converse is not true. This is not a limitation in practice because atom libraries are extensible (i.e., the class of DGP is parameterized by the atom library), and because invalid compositions of atoms can often be appropriately re-expressed.

DGP offers an easy-to-understand prescription for constructing a large class of log-log convex problems. If the product, power, sum, and max functions are taken as atoms, then DGP is equivalent to generalized geometric programming. If other functions from §2.3 and §2.4 are also included, then the set of disciplined geometric programs becomes a strict superset of the set of GGPs. As we shall see in §4, DGP is easily supported in a DCP-based DSL for optimization. For these reasons, it seems sensible to suggest that DGP might replace GPs in the optimization modeling toolbelt.

Verifying whether an optimization problem is DGP involves representing the problem as a collection of mathematical expression trees (one for the objective and one for each constraint), and recursively verifying each expression tree. For example, the problem can be represented by the expression trees shown in figure 3; assuming that the variables $x$ and $y$ are positive, this problem is an LLCP, but it is neither a GP nor a GGP.

An expression tree for an objective is valid if its root is the minimize (maximize) operator and the subtree rooted at its child is a valid log-log convex (log-log concave) composition of atoms. A tree rooted at an atom is valid if the subtrees rooted at its children are valid compositions of atoms, and if the composition of the root with the subtrees of its children is grammatical. Likewise, a tree for an inequality constraint is valid if the left subtree is a valid log-log convex composition of atoms, and the right subtree is a valid log-log concave composition of atoms. A tree for an equality constraint is valid if both subtrees are log-log affine compositions of atoms. The recursion bottoms out at the leaves of each tree, which are variables or constants. Leaves are log-log affine provided that they are positive.

Figure 3: Expression trees representing the optimization problem.

## Implementation

We have implemented DGP in CVXPY 1.0, a Python-embedded, object-oriented DSL for convex optimization \[AVD+18\]. Our implementation, which is available at makes CVXPY 1.0 the first DSL for log-log convex programming.

Our atom library includes a number of the functions presented in §2.3 and §2.4, and our implementation of DGP is a strict superset of generalized geometric programming. CVXPY 1.0 can canonicalize any DGP problem and furnish a solution to it, along with the optimal dual values; it does this by reducing every DGP problem to a DCP problem, canonicalizing and solving the DCP problem, and retrieving a solution to the original problem.

### Canonicalization

In CVXPY 1.0, canonicalization is facilitated by Reduction objects, which rewrite problems of one form into equivalent problems of another form and record how to retrieve a solution to the source problem from a solution to the reduced-to problem. Canonicalizing DGP problems in CVXPY 1.0 is simple: we first reduce each DGP problem to a DCP problem, after which we apply the DCP canonicalization procedure.

We have added a class Dgp2Dcp that subclasses Reduction. Dgp2Dcp accepts exactly those problems that are DGP. When applied to a problem, the Dgp2Dcp reduction recursively replaces subexpressions with DCP log-log transformations or graph implementations. For example, constants are replaced with their logarithms, positive variables are replaced with unconstrained variables, products of two expressions are replaced with sums of the log-log transformations of those expressions, and sums of expressions are replaced with the log_sum_exp of their canonicalized expressions. This procedure makes sense because the log-log transformation of $f = {h \circ g}$ is equal to the composition of the log-log transformations of $h$ and $g$.

Atoms like eye_minus_inv whose log-log transformations are not DCP are replaced by their graph implementations (a graph implementation of eye_minus_inv is given in §2.4). For example, the expression trace(eye_minus_inv(X)) would be canonicalized to trace(Y), together with the log-log transformation of the constraint Y U + I \<= Y, where U is a variable representing log X.

### Solution retrieval

When a DGP problem $\mathcal{P}_{1}$ is reduced to a DCP problem $\mathcal{P}_{2}$, for each variable in $\mathcal{P}_{1}$, a variable representing its logarithm is instantiated in $\mathcal{P}_{2}$. Given a solution to $\mathcal{P}_{2}$, i.e., an assignment of numeric values to variables, we recover a solution to $\mathcal{P}_{1}$ by exponentiating the values of the variables in $\mathcal{P}_{2}$ and assigning the results to the corresponding variables in $\mathcal{P}_{1}$. When $\mathcal{P}_{2}$ is unbounded, $\mathcal{P}_{1}$ is unbounded as well, in which case the optimal value of the optimization problem is $0$ (if $\mathcal{P}_{1}$ is a minimization problem) or $+ \infty$ (if $\mathcal{P}_{1}$ is a maximization problem). Similarly, $\mathcal{P}_{1}$ is infeasible when $\mathcal{P}_{2}$ is infeasible.

The optimal dual values of $\mathcal{P}_{1}$ are the same as those of $\mathcal{P}_{2}$. Under certain assumptions, the optimal dual values of $\mathcal{P}_{2}$ represent fractional changes in the optimal objective given fractional changes in the constraints \[BKV+07, §3.3\].

### Examples

### Hello, World

Below is an example of how to use CVXPY 1.0 to specify and solve the DGP problem, meant to highlight the syntax of our modeling language. A more interesting example is subsequently presented. [⬇](data:text/plain;base64,aW1wb3J0IGN2eHB5IGFzIGNwCgp4ID0gY3AuVmFyaWFibGUocG9zPVRydWUpCnkgPSBjcC5WYXJpYWJsZShwb3M9VHJ1ZSkKb2JqZWN0aXZlX2ZuID0geCAqIHkKb2JqZWN0aXZlID0gY3AuTWluaW1pemUob2JqZWN0aXZlX2ZuKQpjb25zdHJhaW50cyA9IFtjcC5leHAoeS94KSA8PSBjcC5sb2coeSldCnByb2JsZW0gPSBjcC5Qcm9ibGVtKG9iamVjdGl2ZSwgY29uc3RyYWludHMpCnByb2JsZW0uc29sdmUoZ3A9VHJ1ZSkKcHJpbnQoIk9wdGltYWwgdmFsdWU6ICIsIHByb2JsZW0udmFsdWUpCnByaW50KCJ4OiAiLCB4LnZhbHVlKQpwcmludCgieTogIiwgeS52YWx1ZSkKcHJpbnQoIkR1YWwgdmFsdWU6ICIsIGNvbnN0cmFpbnRzWzBdLmR1YWxfdmFsdWUp){download=""} 3x = cp.Variable(pos=True) 4y = cp.Variable(pos=True) 6objective = cp.Minimize(objective_fn) 7constraints = \[cp.exp(y/x) \<= cp.log(y)\] 8problem = cp.Problem(objective, constraints) 9problem.solve(gp=True) 10print(\"Optimal value: \", problem.value) 13print(\"Dual value: \", constraints.dual_value) The optimization problem problem has two scalar variables, x and y. For a problem to be DGP, every optimization variable must be declared as positive, as done here with pos=True. The objective is to minimize the product of $x$ and $y$, which is neither convex nor concave but is log-log affine, since the product atom is log-log affine. Every atom is an Expression object, which may in turn have references to other Expressions; i.e., each Expression represents a mathematical expression tree. In line 7, the Expressions are represented using three atoms: ratio (/), exp, and log. Also in line 7, exp(y/x) is constrained to be no larger than log(y) via the relational operator \<=, which constructs a Constraint object linking two Expressions. Line 8 constructs but does not solve problem, which encapsulates the expression trees for the objective and constraints. The problem is DGP (which can be verified by asserting problem.is_dgp), but it is not DCP (which can be verified by asserting not problem.is_dcp). Line 9 canonicalizes and solves problem. The optimal value of the problem, the values of the variables, and the optimal dual value are printed in lines 10-13, yielding the following output. [⬇](data:text/plain;base64,T3B0aW1hbCB2YWx1ZTogIDQ4LjgxMDI2ODk4NDQ3MzQzCng6ICAxMS43ODAwODk5MzI2MzU2NDUKeTogIDQuMTQzNDU0Njk4ODY4NTY0CkR1YWwgdmFsdWU6ICAyLjg0MzA1OTkxNzc0NzcwNg==){download=""} As this code example makes clear, users do not need to know how canonicalization works. All they need to know is how to construct DGP problems. Calling the solve method on a Problem instance with the keyword argument gp=True canonicalizes the problem and retrieves a solution. If the user forgets to type gp=True when her problem is DGP (and not DCP), a helpful error message is raised to alert her of the omission.

### Perron-Frobenius matrix completion

We have implemented several functions of positive matrices as atoms, including the trace, product, sum, Perron-Frobenius eigenvalue, and eye-minus-inverse. As an example, we can use CVXPY 1.0 to formulate and solve a Perron-Frobenius matrix completion problem. In this problem, we are given some entries of an elementwise positive matrix $A$, and the goal is to choose the missing entries so as to minimize the Perron-Frobenius eigenvalue or spectral radius. Letting $\Omega$ denote the set of indices $(i,j)$ for which $A_{ij}$ is known, the optimization problem is which is an LLCP. Below is an implementation of the problem, with specific problem data where the question marks denote the missing entries. [⬇](data:text/plain;base64,aW1wb3J0IGN2eHB5IGFzIGNwCgpuID0gMwprbm93bl92YWx1ZV9pbmRpY2VzID0gdHVwbGUoemlwKCpbWzAsIDBdLCBbMCwgMl0sIFsxLCAxXSwgWzIsIDBdLCBbMiwgMV1dKSkKa25vd25fdmFsdWVzID0gWzEuMCwgMS45LCAwLjgsIDMuMiwgNS45XQpYID0gY3AuVmFyaWFibGUoKG4sIG4pLCBwb3M9VHJ1ZSkKb2JqZWN0aXZlX2ZuID0gY3AucGZfZWlnZW52YWx1ZShYKQpjb25zdHJhaW50cyA9IFsKICBYW2tub3duX3ZhbHVlX2luZGljZXNdID09IGtub3duX3ZhbHVlcywKICBYWzAsIDFdICogWFsxLCAwXSAqIFhbMSwgMl0gKiBYWzIsIDJdID09IDEuMCwKXQpwcm9ibGVtID0gY3AuUHJvYmxlbShjcC5NaW5pbWl6ZShvYmplY3RpdmVfZm4pLCBjb25zdHJhaW50cykKcHJvYmxlbS5zb2x2ZShncD1UcnVlKQpwcmludCgiT3B0aW1hbCB2YWx1ZTogIiwgcHJvYmxlbS52YWx1ZSkKcHJpbnQoIlg6XG4iLCBYLnZhbHVlKQ==){download=""} 4known_value_indices = tuple(zip(\*\[\])) 6X = cp.Variable((n, n), pos=True) 9 X\[known_value_indices\] == known_values, 12problem = cp.Problem(cp.Minimize(objective_fn), constraints) 13problem.solve(gp=True) 14print(\"Optimal value: \", problem.value) Executing the above code prints the below output. [⬇](data:text/plain;base64,T3B0aW1hbCB2YWx1ZTogIDQuNzAyMzc0MjAzMjIxNTM1Clg6CltbMS4gICAgICAgICA0LjYzNjE2OTA3IDEuOSAgICAgICBdCiBbMC40OTk5MTc0NCAwLjggICAgICAgIDAuMzc3NzQxNDhdCiBbMy4yICAgICAgICA1LjkgICAgICAgIDEuMTQyMjE0NzZdXQ==){download=""}
