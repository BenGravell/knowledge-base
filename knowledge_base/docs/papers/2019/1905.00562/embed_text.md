<!-- arxiv-full-text:v1 {"arxiv_id": "1905.00562", "source": "ar5iv"} -->

## Introduction

A real-valued function $f$ is *quasiconvex* if its domain $C$ is convex, and for any $\alpha \in \text{R}$, its $\alpha$-sublevel sets $\{{x \in C}\mid{{f{(x)}} \leq \alpha}\}$ are convex \[, §3.4\]. A function $f$ is quasiconcave if $- f$ is quasiconvex, and it is quasilinear if it is both quasiconvex and quasiconcave. A *quasiconvex program* (QCP) is a mathematical optimization problem in which the objective is to minimize a quasiconvex function over a convex set. Because every convex function is also quasiconvex, QCPs generalize convex programs. Though QCPs are in general nonconvex, many can nonetheless be solved efficiently by a bisection method that involves solving a sequence of convex programs \[, §4.2.5\], or by subgradient methods \[, \].

The study of quasiconvex functions is several decades old \[ \]. Quasiconvexity has been of particular interest in economics, where it arose in the study of competitive equilibria and the modeling of utility functions \[, \]. More recently, quasiconvex programming has been applied to control \[ \], model order reduction, computer vision \[, \], computational geometry, and machine learning. While QCPs have many applications, it remains difficult for non-experts to specify and solve them in practice. The point of this paper is to close that gap.

Domain-specific languages (DSLs) have made convex optimization widely accessible. DSLs let users specify their programs in natural mathematical notation, abstracting away the process of canonicalizing problems to standard forms for numerical solvers. The syntax of most DSLs for convex optimization, including CVX, CVXPY \[, AVD+18\], Convex.jl \[UMZ+14\], and CVXR, is determined by a grammar known as *disciplined convex programming* (DCP). DCP includes a set of functions with known curvature (affine, convex, or concave) and monotonicity, and a composition rule for combining the functions to produce expressions that are also convex or concave. Some software does exist for solving quasiconvex problems (e.g., YALMIP \[Löf04\]), but no DSLs exist for specifying them in a way that guarantees quasiconvexity.

In this paper, we introduce *disciplined quasiconvex programming* (DQCP), an analog of DCP for quasiconvex optimization. Like DCP, DQCP is a grammar that consists of a set of functions and rules for combining them. A contribution of this paper is the development of a theorem for the composition of a quasiconvex function with convex (and concave) functions that guarantees quasiconvexity of the composition. This rule includes as a special case the composition rule for convex functions upon which DCP is based. The class of programs producible by DQCP is a subset of QCPs (and depends on the function library), and a superset of the class corresponding to DCP.

In §2, we review properties of quasiconvex functions, state our composition theorem, and provide several examples of quasiconvex functions. In §3, we describe a bisection method for solving QCPs. In §4, we present DQCP, and in §5, we describe an implementation of DQCP in CVXPY 1.0.

## Quasiconvexity

### Properties

In this section, we review basic properties of quasiconvex functions, many of which are parallels of properties of convex functions; see for many more.

### Jensen's inequality

Quasiconvex functions are characterized by a kind of Jensen's inequality: a function $f$ mapping a set $C$ into R is quasiconvex if and only if $C$ is convex and, for any ${x,y} \in C$ and $\theta \in {\lbrack 0,1\rbrack}$, Similarly, $f$ is quasiconcave if and only if $C$ is convex and ${f{({{\thetax} + {{({1 - \theta})}y}})}} \geq {\min{\{{f{(x)}},{f{(y)}}\}}}$, for all ${x,y} \in C$ and $\theta \in {\lbrack 0,1\rbrack}$.

### Functions on the real line

For $f:{C \subseteq \text{R}\rightarrow\text{R}}$, quasiconvexity can be described in simple terms: $f$ is quasiconvex if it is nondecreasing, nonincreasing, or nonincreasing over $C \cap {(\infty,t\rbrack}$ and nondecreasing over ${\lbrack t,\infty)} \cap C$, for some $t \in C$.

### Representation via a family of convex functions

The sublevel sets of a quasiconvex function can be represented as inequalities of convex functions. In this sense, every quasiconvex function can be represented by a family of convex functions. If $f:{C\rightarrow\text{R}}$ is quasiconvex, then there exists a family of convex functions $\phi_{t}:{C\rightarrow\text{R}}$, indexed by $t \in \text{R}$, such that The indicator functions for the sublevel sets of $f$, generate one such family. As another example, if the sublevel sets of $f$ are closed, a suitable family is ${\phi_{t}{(x)}} = {\inf_{z \in {\{ z\mid{{f{(z)}} \leq t}\}}}{\|{x - z}\|}}$. We are typically interested in finding families that possess nice properties. For the purpose of DQCP, we seek functions $\phi_{t}$ whose $0$-sublevel sets can be represented by convex cones over which optimization is tractable.

### Partial minimization

Minimizing a quasiconvex function over a convex set with respect to some of its variables yields another quasiconvex function.

### Supremum of quasiconvex functions

The supremum of a family of quasiconvex functions is quasiconvex, as can be easily verified \[, §3.4.4\]; similarly, the infimum of quasiconcave functions is quasiconcave.

### Composition with monotone functions

If $g:{C\rightarrow\text{R}}$ is quasiconvex and $h$ is a nondecreasing real-valued function on the real line, then $f = {h \circ g}$ is quasiconvex. This can be seen by observing that for any $\alpha \in \text{R}$, a point $x$ (belonging to the domain of $f$) is in the $\alpha$-sublevel set of $f$ if and only if Because $g$ is quasiconvex, this shows that the sublevel sets of $f$ are convex. Similarly, a nonincreasing function of a quasiconvex function is is quasiconcave, a nondecreasing function of a quasiconcave function is quasiconcave, and a nonincreasing function of a quasiconcave function is quasiconvex.

### Composition theorem

A basic result from convex analysis is that a nondecreasing convex function of a convex function is convex; DCP is based on a generalization of this result. The composition rule for convex functions admits a partial extension for quasiconvex functions, which we state below as a theorem. Though the theorem is straightforward, we are unaware of any references to it in the literature. Of course, the analog of the theorem for quasiconcave functions also holds.

In the statement of the theorem, when considering a function $g$ mapping a subset of $\text{R}^{n}$ into $\text{R}^{k}$, we use $g_{1},g_{2},\ldots,g_{k}$ to denote the components of $g$. These components are the real functions defined by for $x$ in the domain of $g$.

### Theorem 1

Suppose $h$ is a quasiconvex mapping of a subset $C$ of $\text{R}^{k}$ into $\text{R} \cup \infty$, and $\{ I_{1},I_{2},I_{3}\}$ is a partition of $\{ 1,2,\ldots,k\}$ such that $h$ is nondecreasing in the arguments indexed by $I_{1}$ and nonincreasing in the arguments indexed by $I_{2}$. Suppose also that $g$ maps a subset of $\text{R}^{n}$ into $\text{R}^{k}$ in such a way that its components $g_{i}$ are convex for $i \in I_{1}$, concave for $i \in I_{2}$, and affine for $i \in I_{3}$. Then the composition is quasiconvex. If additionally $h$ is convex, then $f$ is convex as well.

The final statement of the theorem is just the well-known composition rule for convex functions.

We provide two proofs of this result. The first proof directly verifies that the domain of $f$ is convex and that $f$ satisfies the modified Jensen's inequality. This proof is almost identical to a proof of the composition theorem for convex functions. The only difference is that an application of Jensen's inequality for convex functions is replaced with its variant for quasiconvex functions. The second proof just applies the composition theorem for convex functions to the representation of a quasiconvex function via a family of convex functions.

### Proof via Jensen's inequality

Assume $x,y$ are in the domain of $f$, and $\theta \in {\lbrack 0,1\rbrack}$. Since the components of $g$ are convex or concave (or affine), the convex combination ${\thetax} + {{({1 - \theta})}y}$ is in the domain of $g$. For $i \in I_{1}$, the components are convex, so For $i \in I_{2}$, the inequality is reversed, and for $i \in I_{3}$, it is an equality. Since $x$ and $y$ are in the domain of $f$, $g{(x)}$ and $g{(y)}$ are in the domain $C$ of $h$, and ${{\thetag{(x)}} + {{({1 - \theta})}g{(y)}}} \in C$. Let $e_{i}$ denote the $i$th standard basis vector of $\text{R}^{k}$. Since $h$ is an extended-value function and in light of its per-argument monotonicities, $C$ extends infinitely in the directions $- e_{i}$ for $i \in I_{1}$ and $e_{i}$ for $i \in I_{2}$. This fact, combined with the inequalities involving the components of $g$ and the fact that ${{\thetag{(x)}} + {{({1 - \theta})}g{(y)}}} \in C$, shows that ${g{({{\thetax} + {{({1 - \theta})}y}})}} \in C$. Hence the domain of $f$ is convex.

By the monotonicity of $h$ and Jensen's inequality applied to the components of $g$,

### Proof via representation by convex functions

Let $\phi_{t}:{C\rightarrow\text{R}}$ be a member of a family of convex functions, indexed by $t$, such that ${\phi_{t}{(x)}} \leq 0$ if and only if ${h{(x)}} \leq t$. Assume without loss of generality that the per-argument monotonicities of $\phi_{t}$ match those of $h$ (*e.g.*, take $\phi_{t}$ to be the indicator function for the $t$-sublevel set of $h$). Then ${f{(x)}} = {h{({g{(x)}})}} \leq t$ if and only if ${\phi_{t}{({g{(x)}})}} \leq 0$. By the composition theorem for convex functions, $\phi_{t} \circ g$ is convex. We therefore conclude that the sublevel sets of $f$ are convex, *i.e.*, $f$ is quasiconvex. ∎

### Examples

### Product

The scalar product ${f{(x,y)}} = {xy}$ is quasiconcave when restricted to either $\text{R}_{+}^{2}$ or $\text{R}_{-}^{2}$, where $\text{R}_{+}^{n}$ denotes the set of nonnegative real $n$-vectors and $\text{R}_{-}^{n}$ the set of nonpositive real $n$-vectors. The product is quasiconvex when one variable is nonnegative and the other is nonpositive. From this fact and the composition rule, one can deduce that the product of two nonnegative concave functions is quasiconcave (see also \[, \]), and the product of a nonnegative concave function with a nonpositive convex function is quasiconvex.

### Ratio

The ratio ${f{(x,y)}} = {x/y}$ is quasilinear on $\text{R} \times \text{R}_{+ +}$, as well as on $\text{R} \times \text{R}_{- -}$ (but not on $\text{R}^{2}$), where $\text{R}_{+ +}^{n}$ and $\text{R}_{- -}^{n}$ denote the sets of positive and negative real $n$-vectors, respectively. When $x \geq 0$ and $y > 0$, $f$ is increasing in $x$ and decreasing in $y$. Hence the ratio of a nonnegative convex function and a positive concave function is quasiconvex, and the ratio of a nonnegative concave function and a positive convex function is quasiconcave. The problem of maximizing the ratio of a nonnegative concave function and a positive convex function is known as concave-fractional programming \[, \].

### Linear-fractional function

is quasilinear when the denominator is positive. This can be seen by the composition rule, since the ratio $x/y$ is quasilinear when $y > 0$. It is also quasilinear when restricted to negative denominators. The problem of minimizing a linear-fractional function over a polyhedron is known as linear-fractional programming. Though linear-fractional programming is often described as a generalization of linear programming, linear-fractional programs can be reduced to linear programs.

### Distance ratio function

is quasiconvex on the halfspace $\{{x \in \text{R}^{n}}\mid{{\|{x - a}\|}_{2} \leq {\|{x - b}\|}_{2}}\}$. This result cannot be derived by applying the composition rule to the ratio function, but it is simple to show that its sublevel sets are Euclidean balls \[, §3.4\].

### Monotone functions on the real line

Monotone functions whose domains are convex subsets of R are quasilinear; examples include the exponential function, logarithm, square root, and positive odd powers.

### Generalized eigenvalue

The maximum eigenvalue of a symmetric matrix is convex, since it can be written as the supremum of a family of linear functions. Analogously, the maximum generalized eigenvalue $\lambda_{\max}{(A,B)}$ of a pair of symmetric matrices $(A,B)$ (with $B$ positive definite) is quasiconvex, since is the supremum of a family of linear-fractional functions \[, §3.4\]. Another way to see this is to note that the inequality is satisfied if and only if ${tB} - A$ is positive semidefinite. Similarly, the minimum generalized eigenvector is quasiconcave in $A$ and $B$.

### Integer-valued functions

### Ceiling and floor

The functions ${\lceil x\rceil} = {\inf{\{{z \in \text{Z}}\mid{z \geq x}\}}}$ and ${\lfloor x\rfloor} = {\sup{\{{z \in \text{Z}}\mid{z \leq x}\}}}$ are quasilinear, because they are monotone functions on the real line.

### Sign

The function mapping a real number to $- 1$ if it is negative and $+ 1$ otherwise is quasilinear.

### Rectangle

The rectangle function $f:{\text{R}\rightarrow\text{R}}$ given by

### Length of a vector

The length of a vector in $\text{R}^{n}$ is defined as the largest index corresponding to a nonzero component: This function is quasiconvex on $\text{R}^{n}$ because its sublevel sets are subspaces. The inequality ${f{(x)}} \leq \alpha$ implies $x_{i} = 0$ for $i = {{{\lfloor\alpha\rfloor} + 1},\ldots,n}$.

### Cardinality of a nonnegative vector

The function ${card}{(x)}$, which gives the number of nonzero components in the vector $x$, is quasiconcave on $\text{R}_{+}^{n}$: ${{card}{({x + y})}} \geq {\min{\{{{card}{(x)}},{{card}{(y)}}\}}}$ for nonnegative $x$ and $y$.

### Matrix rank

The matrix rank is quasiconcave on the set of positive semidefinite matrices, since the rank of a sum of positive semidefinite matrices is at least the minimum of the ranks of the matrices.

## Solution method

The problem of minimizing a quasiconvex function $f:{C\rightarrow\text{R}}$ can be solved in many ways \[\]. Here, we describe a simple method that reduces a QCP to a sequence of convex feasibility problems \[, §4.2.5\]. Suppose the interval $\lbrack\alpha,\beta\rbrack$ is known to contain the optimal value $p^{\star}$. Put $t = {{({\alpha + \beta})}/2}$, and let $\phi_{t}:{C\rightarrow\text{R}}$ be a family of convex functions indexed by $t \in \text{R}$ such that ${f{(x)}} \leq t$ if and only if ${\phi_{t}{(x)}} \leq 0$. Consider the convex feasibility problem If this problem yields a feasible point $x$, then $p^{\star} \leq t$ and in particular $p^{\star} \in {\lbrack\alpha,{f{(x)}}\rbrack}$; otherwise, $p^{\star} \in {\lbrack t,\beta\rbrack}$. In either case, solving the feasibility problem yields an interval containing the optimal value, with width half as large as the original interval. To obtain an $\epsilon$-suboptimal solution to the QCP, we repeat this process until the width of the interval is at most $\epsilon$, which requires at most $\lceil{{\log_{2}{({\beta - \alpha})}}/\epsilon}\rceil$ iterations.

### Finding an initial interval for bisection

The optimal value $p^{\star}$ is usually not known before solving a QCP. In such cases, a simple heuristic can be employed to find an interval containing it, assuming that the QCP is feasible (which can be checked by solving a single convex feasibility problem). Start with a candidate interval $\lbrack\alpha,\beta\rbrack$, where $\alpha < 0$ and $\beta > 0$. If the problem $$ is feasible for $t = \beta$ and infeasible for $t = \alpha$, then $p^{\star} \in {\lbrack\alpha,\beta\rbrack}$. Otherwise, if the problem is infeasible for $t = \beta$, put $\alpha:=\beta$ and $\beta:={2\beta}$. If on the other hand the problem is feasible for $t = \alpha$, put $\beta:=\alpha$ and $\alpha:={2\alpha}$. Repeating this process will eventually produce an interval containing $p^{\star}$, provided that the QCP is not unbounded.

## Disciplined quasiconvex programming

DQCP is a grammar for constructing QCPs from a set of functions, or *atoms*, with known curvature (affine, convex, concave, quasiconvex, or quasiconcave) and per-argument monotonicities. A program produced using DQCP is called a disciplined quasiconvex program; we say that such programs are DQCP-compliant, or just DQCP, for short. DQCP guarantees that every function appearing in a disciplined quasiconvex program is affine, convex, concave, quasiconvex, or quasiconcave.

A disciplined quasiconvex program is an optimization problem of the form The functions $f_{i}$ must be quasiconvex, $g_{i}$ must be quasiconcave, ${\overset{\sim}{f}}_{i}$ must be convex, ${\overset{\sim}{g}}_{i}$ must be concave, and $h_{i}$, ${\overset{\sim}{h}}_{i}$ must be affine; $\alpha_{i}$ and $\beta_{i}$ must be constants. All of the functions appearing in must be produced from atoms, using only the composition rule from Theorem 1 and the rules governing the maximum of quasiconvex functions, the minimum of quasiconcave functions, and composition with monotone functions (see §2.1). Because Theorem 1 includes the composition rule for convex functions as a special case, DQCP is a modest extension of DCP.

A mathematical expression is verifiably quasiconvex under DQCP if it is a quasiconvex atom, applied to a variable or constant; the max of quasiconvex expressions; a nondecreasing function of a quasiconvex expression, or a nonincreasing function of a quasiconcave expression; the composition of a quasiconvex atom with convex, concave, and affine expressions that satisfies the hypotheses of Theorem 1.

These rules are applied recursively, with the recursion bottoming out at variables and constants. For example, if $\exp{(\cdot)}$ and the generalized eigenvalue $\lambda_{\max}{(\cdot, \cdot)}$ are atoms, and $X$ and $Y$ are matrix variables, then the expressions are all verifiably quasiconvex under DQCP, since $\exp{(\cdot)}$ is increasing and $\lambda_{\max}{(\cdot, \cdot)}$ is quasiconvex. Likewise, an expression is quasiconcave under DQCP if it is a concave expression, a quasiconcave atom applied to a variable or constant, the min of quasiconcave functions, a nondecreasing function of a quasiconcave function, a nonincreasing function of a quasiconvex function, or a valid composition of a quasiconcave function with convex, concave, and affine functions. Whether an expression is convex, concave, or affine under DQCP is precisely the same as under DCP.

A DQCP program is naturally represented as a collection of expression trees, one for the objective and one for each constraint. Verifying whether a program is DCQP amounts to recursively verifying that each expression tree is DQCP. For example, the program can be represented by the trees shown in figure 1. This program is DQCP when $y$ is known to be positive, because the ratio of a nonnegative concave functions and a positive convex function is quasiconcave, and the negation of a quasiconcave function is quasiconvex. The atoms in this program are the functions $\exp{(\cdot)}$, $\sqrt{\cdot}$, and $\cdot / \cdot$.

Every disciplined quasiconvex program is a QCP, but the converse is not true. This is not a limitation in practice, since the atom library is extensible.

Figure 1: Expression trees representing the program.

### The grammar

Table 1 specifies the DQCP grammar, in the programming languages sense \[ALS+06, §4\]. In the specification, $S$ denotes the start symbol. The symbols are nonterminals used to represent affine, convex, concave, quasiconvex, and quasiconcave expressions producible by DQCP. Their lowercase counterparts represent atoms, *e.g.*, $cvx$ stands for a convex atom. Atoms can have multiple curvatures. For example, every affine atom is also a convex atom and a concave atom. The symbols denote nondecreasing and nonincreasing functions, respectively, denote numerical constants and optimization variables, and denotes a composition of a convex atom with convex, concave, and affine expressions that can be certified as convex via Theorem 1. Because DQCP is a grammar for QCPs, it can be used to define the syntax of a DSL for quasiconvex optimization.

→ aff (AFF, …, AFF) → cvx (CVX, …, CVX, CCV, …, CCV, AFF, …, AFF) → ccv (CCV, …, CCV, CVX, …, CVX, AFF, …, AFF) → qcvx (CVX, …, CVX, CCV, …, CCV, AFF, …, AFF) → max {QCVX, …, QCVX} → qccv (CCV, …, CCV, CVX, …, CVX, AFF, …, AFF) → min {QCCV, …, QCCV} Table 1: The DQCP grammar, which extends DCP. The rules for compositions with convex, concave, and affine expressions denote compositions satisfying the hypotheses of Theorem 1.

## Implementation

We have implemented DQCP in CVXPY 1.0, a Python-embedded DSL for convex optimization \[, AVD+18\]. Our implementation, which is available at makes CVXPY the first DSL for quasiconvex optimization. Because DQCP is a generalization of DCP, it fits seamlessly into CVXPY, which parses problems using DCP by default. Our atom library includes many of the functions presented in §2.3. We have also implemented the bisection method described in §3.

### Canonicalization

The process of rewriting a problem to an equivalent standard form is called canonicalization. In CVXPY 1.0, canonicalization is facilitated by Reduction objects, which rewrite problems of one form into equivalent problems of another form.

We have implemented a reduction called Dqcp2Dcp that canonicalizes DQCP problems by converting them into an equivalent one-parameter family of DCP feasibility problems. When applied to a DQCP problem, this reduction first introduces a scalar parameter and constrains the problem's objective to be no greater than the parameter. It recursively processes this constraint and every other constraint, representing the sublevel sets of quasiconvex expressions and superlevel sets of quasiconcave expressions in DCP-complaint ways. The reduction then emits a parameterized DCP problem. The constraints of the emitted problem are the canonicalized constraints of the original problem, and the objective is to find an assignment to the variables that satisfies the constraints. A solution to the original problem can be obtained by running bisection on the emitted problem.

### Bisection

We have implemented the bisection routine described in §3. Our method first checks whether the original problem is feasible by solving a convex feasibility problem. If the problem is feasible, our routine automatically finds an interval containing the optimal value and then runs bisection. Our bisection routine tightens the boundaries of the bisection interval depending on the values of the original problem's objective function. For example, when the objective is integer-valued, our implementation will tighten a lower bound $\alpha$ to $\lceil\alpha\rceil$, and an upper bound $\beta$ to $\lfloor\beta\rfloor$.

### Examples

### Hello, world

Below is an example of how to use CVXPY 1.0 to specify and solve the problem, meant to highlight the syntax of our modeling language. More interesting examples are subsequently presented. [⬇](data:text/plain;base64,aW1wb3J0IGN2eHB5IGFzIGNwCgp4ID0gY3AuVmFyaWFibGUoKQp5ID0gY3AuVmFyaWFibGUocG9zPVRydWUpCm9iamVjdGl2ZV9mbiA9IC1jcC5zcXJ0KHgpL3kKb2JqZWN0aXZlID0gY3AuTWluaW1pemUob2JqZWN0aXZlX2ZuKQpjb25zdHJhaW50ID0gY3AuZXhwKHgpIDw9IHkKcHJvYmxlbSA9IGNwLlByb2JsZW0ob2JqZWN0aXZlLCBbY29uc3RyYWludF0pCnByb2JsZW0uc29sdmUocWNwPVRydWUpCnByaW50KCJPcHRpbWFsIHZhbHVlOiAiLCBwcm9ibGVtLnZhbHVlKQpwcmludCgieDogIiwgeC52YWx1ZSkKcHJpbnQoInk6ICIsIHkudmFsdWUp){download=""} 4y = cp.Variable(pos=True) 6objective = cp.Minimize(objective_fn) 8problem = cp.Problem(objective, \[constraint\]) 9problem.solve(qcp=True) 10print(\"Optimal value: \", problem.value) The optimization problem problem has two scalar variables, x and y. Notice that y is declared as positive in line 3, with pos=True. The objective is to minimize the ratio of $- \sqrt{x}$ and $y$, which is quasiconvex since the ratio is quasiconcave when the numerator is a nonnegative concave expression and the denominator is a positive convex expression. Line 6 constructs the objective of the problem. In line 7, exp(x) is constrained to be no larger than y via the relational operator \<=. Line 8 constructs problem, which represents the optimization problem as two expression trees, one for objective_fn and one for constraint. The internal nodes in these expression trees are the atoms sqrt, exp, ratio (/), and negation $(\text{-})$. The problem is DQCP, which can be verified by asserting problem.is_dqcp. Line 9 canonicalizes problem, parsing it as a DQCP (qcp=True), and then solves it by bisection. The optimal value of the problem and the values of the variables are printed in lines 10-12, yielding the following output. [⬇](data:text/plain;base64,T3B0aW1hbCB2YWx1ZTogIC0wLjQyODg4MjEyMjAzOTc5NDkKeDogIDAuNDk5OTk3MzcxNDMwMDQ3MTMKeTogIDEuNjQ4NzE3NzI0ODQ1MDA3){download=""} As this example makes clear, users do not need to know how canonicalization or bisection work. All they need to know is how to construct DQCP problems. Calling the solve method on a Problem instance with the keyword argument qcp=True canonicalizes the problem and retrieves a solution. If the user forgets to type qcp=True when her problem is DQCP (and not DCP), a helpful error message is raised to alert her of the omission.

### Generalized eigenvalue matrix completion

We have implemented the maximum generalized eigenvalue as an atom. As an example, we can use CVXPY 1.0 to formulate and solve a generalized eigenvalue matrix completion problem. In this problem, we are given some entries of two symmetric matrices $A$ and $B$, and the goal is to choose the missing entries so as to minimize the maximum generalized eigenvalue $\lambda_{\max}{(A,B)}$. Letting $\Omega$ denote the set of indices $(i,j)$ for which $A_{ij}$ and $B_{ij}$ are known, the optimization problem is which is a QCP. Below is an implementation of this problem, with specific problem data (The question marks denote the missing entries.) [⬇](data:text/plain;base64,aW1wb3J0IGN2eHB5IGFzIGNwCgpYID0gY3AuVmFyaWFibGUoKDMsIDMpKQpZID0gY3AuVmFyaWFibGUoKDMsIDMpKQpnZW5fbGFtYmRhX21heCA9IGNwLmdlbl9sYW1iZGFfbWF4KFgsIFkpCm9tZWdhID0gdHVwbGUoemlwKCpbWzAsIDBdLCBbMCwgMl0sIFsxLCAxXV0pKQpjb25zdHJhaW50cyA9IFsKICBYW29tZWdhXSA9PSBbMS4wLCAxLjksIDAuOF0sCiAgWVtvbWVnYV0gPT0gWzMuMCwgMS40LCAwLjJdLApdCnByb2JsZW0gPSBjcC5Qcm9ibGVtKGNwLk1pbmltaXplKGdlbl9sYW1iZGFfbWF4KSwgY29uc3RyYWludHMpCnByb2JsZW0uc29sdmUocWNwPVRydWUpCnByaW50KCJHZW5lcmFsaXplZCBlaWdlbnZhbHVlOiAiLCBnZW5fbGFtYmRhX21heC52YWx1ZSkKcHJpbnQoIlg6ICIsIFgudmFsdWUpCnByaW50KCJZOiAiLCBZLnZhbHVlKQ==){download=""} 5gen_lambda_max = cp.gen_lambda_max(X, Y) 6omega = tuple(zip(\*\[\])) 11problem = cp.Problem(cp.Minimize(gen_lambda_max), constraints) 12problem.solve(qcp=True) 13print(\"Generalized eigenvalue: \", gen_lambda_max.value) Executing the above code prints the below output. [⬇](data:text/plain;base64,T2JqZWN0aXZlOiAgNC4wMDAwMDI3MTY0MTE2NTMKWDogIFtbOS45OTk5OTc2N2UtMDEgOS44NjE1NDYxNmUtMTYgMS44OTk5OTk1OWUrMDBdCiBbOS44NjE1NDYxNmUtMTYgNy45OTk5OTc2MWUtMDEgNS4xOTEyNjUzNWUtMTVdCiBbMS44OTk5OTkxMWUrMDAgNS4xOTEyNjUzNWUtMTUgMS4yNTczMzY5MmUrMDBdXQpZOiAgW1sgMi45OTk5OTk4MGUrMDAgLTIuNzg4MTAxMzVlLTE2ICAxLjQwMDAwMDE1ZSswMF0KIFstMi43ODgxMDEzNWUtMTYgIDEuOTk5OTk4MDRlLTAxICAyLjE0NDczMDk4ZS0xNl0KIFsgMS40MDAwMDAxNWUrMDAgIDIuMTQ0NzMwOThlLTE2ICAxLjE0MDM4NTUxZSswMF1d){download=""} Notice that the gen_lambda_max atom automatically enforced the symmetry and positive definiteness constraints on $X$ and $Y$.

### Minimum length least squares

Our atom library includes several integer-valued functions, including the length function. As an example, the following QCP finds a minimum-length vector $x \in \text{R}^{n}$ that has small mean-square error for a particular least squares problem: The problem data are $A \in \text{R}^{n \times n}$, $b \in \text{R}^{n}$, and $\epsilon \in \text{R}$. Below is an implementation of this problem in CVXPY. [⬇](data:text/plain;base64,aW1wb3J0IGN2eHB5IGFzIGNwCmltcG9ydCBudW1weSBhcyBucApucC5zZXRfcHJpbnRvcHRpb25zKHByZWNpc2lvbj0yKQoKbiA9IDEwCm5wLnJhbmRvbS5zZWVkKDEpCkEgPSBucC5yYW5kb20ucmFuZG4obiwgbikKeF9zdGFyID0gbnAucmFuZG9tLnJhbmRuKG4pCmIgPSBBIEAgeF9zdGFyCmVwc2lsb24gPSAxZS0yCgp4ID0gY3AuVmFyaWFibGUobikKbXNlID0gY3Auc3VtX3NxdWFyZXMoQSBAIHggLSBiKS9uCnByb2JsZW0gPSBjcC5Qcm9ibGVtKGNwLk1pbmltaXplKGNwLmxlbmd0aCh4KSksIFttc2UgPD0gZXBzaWxvbl0pCnByb2JsZW0uc29sdmUocWNwPVRydWUpCnByaW50KCJMZW5ndGggb2YgeDogIiwgcHJvYmxlbS52YWx1ZSkKcHJpbnQoIk1TRTogIiwgbXNlLnZhbHVlKQpwcmludCgieDogIiwgeC52YWx1ZSkKcHJpbnQoInhfc3RhcjogIiwgeF9zdGFyKQ==){download=""} 3np.set_printoptions(precision=2) 8x_star = np.random.randn(n) 13mse = cp.sum_squares(A @ x - b)/n 14problem = cp.Problem(cp.Minimize(cp.length(x)), \[mse \<= epsilon\]) 15problem.solve(qcp=True) 16print(\"Length of x: \", problem.value) 17print(\"MSE: \", mse.value) 19print(\"x_star: \", x_star) Running the code produces the following output. [⬇](data:text/plain;base64,TGVuZ3RoIG9mIHg6ICA4LjAKTVNFOiAgMC4wMDkyNjAwOTMyODc3NTU2NAp4OiAgWy0wLjI2ICAxLjM4ICAwLjIxICAwLjk0IC0xLjE1ICAwLjE1ICAwLjY2IC0xLjE2IC0wLiAgIC0wLiAgXQp4X3N0YXI6ICBbLTAuNDUgIDEuMjIgIDAuNCAgIDAuNTkgLTEuMDkgIDAuMTcgIDAuNzQgLTAuOTUgLTAuMjcgIDAuMDNd){download=""}
