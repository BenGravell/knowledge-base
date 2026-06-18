## Introduction

In this paper we introduce the *Suggest-and-Improve* heuristic framework for general nonconvex quadratically constrained quadratic programs (QCQPs). This framework can be applied to general QCQPs for which there are no available specialized methods. We only briefly mention global methods for solving QCQPs in §1.4, as the exponential running time of these methods makes them unsuitable for medium- to large-scale problems. Our main focus, instead, will be on polynomial-time methods for obtaining approximate solutions.

### Quadratically constrained quadratic programming

A quadratically constrained quadratic program (QCQP) is an optimization problem that can be written in the following form:

where $x \in \text{R}^{n}$ is the optimization variable, and $P_{i} \in \text{R}^{n \times n}$, $q_{i} \in \text{R}^{n}$, $r_{i} \in \text{R}$ are given problem data, for $i = {0,1,\ldots,m}$. Throughout the paper, we will use $f^{\star}$ to denote the optimal value of, and $x^{\star}$ to denote an optimal point, i.e., that attains the objective value of $f^{\star}$, while satisfying all the constraints. For simplicity, we assume that all $P_{i}$ matrices are symmetric, but we do not assume any other conditions such as definiteness. This means that, in general, is a nonconvex optimization problem.

The constraint ${f_{i}{(x)}} \leq 0$ is affine if $P_{i} = 0$. If we need to handle affine constraints differently from quadratic ones, we collect all affine constraints and explicitly write them as a single inequality ${Ax} \leq b$, where $A \in \text{R}^{p \times n}$ and $b \in \text{R}^{p}$ are of appropriate dimensions, and the inequality $\leq$ is elementwise. Then, is expressed as:

where $\overset{\sim}{m} = {m - p}$ is the number of nonaffine constraints. When all constraints are affine (i.e., $\overset{\sim}{m} = 0$), the problem is a (nonconvex) quadratic program (QP).

Even though we set up in terms of inequality constraints only, it also allows quadratic equality constraints of the form ${h_{i}{(x)}} = 0$ to be added, as they can be expressed as two quadratic inequality constraints:

An important example of quadratic equality constraint is $x_{i}^{2} = 1$, which forces $x_{i}$ to be either $+ 1$ or $- 1$, and thus encoding a Boolean variable.

There are alternative formulations of that are all equivalent. We start with the *epigraph form* of, which makes the objective function linear (hence convex) without loss of generality, by introducing an additional scalar variable $t \in \text{R}$:

It is also possible to write a problem equivalent to that only has quadratic equality constraints, by introducing an additional variable $s \in \text{R}^{m}$:

The *homogeneous form* of is a QCQP with $n + 1$ variables and $m + 1$ constraints, where the objective function and lefthand side of every constraint is a quadratic form in the variable, i.e., there are no linear terms in the variable \[LMS^+^10\]. For $i = {0,\ldots,m}$, define

The homogeneous form of is given by:

with variable $z \in \text{R}^{n + 1}$. Note that the variable dimension and the number of constraints of is one larger than that of. This problem is homogeneous in the sense that scaling $z$ by a factor of $t \in \text{R}$ scales both the objective and lefthand sides of the constraints by a factor of $t^{2}$. It is easy to check that if $z^{\star}$ is a solution of, then the vector $({z_{1}^{\star}/z_{n + 1}^{\star}},\ldots,{z_{n}^{\star}/z_{n + 1}^{\star}})$ is a solution of.

### Tractable cases

The class of problems that can be written in the form of is very broad, and as we will see in §2, QCQPs are NP-hard in general. However, there are a number of special cases which we can solve efficiently.

### Convex QCQP

When all $P_{i}$ matrices are positive semidefinite, problem is convex and thus easily solvable in polynomial time \[, §4.4\].

### QCQP with one variable

If the problem has only one variable, i.e., $n = 1$, then the feasible set is explicitly computable using only elementary algebra. The feasible set in this case is a collection of at most $m + 1$ disjoint, closed intervals on R. It is possible to compute these intervals in $O{({m{\log m}})}$ time (using a binary search tree, for example). Then, minimizing a quadratic function in this feasible set can be done by evaluating the objective at the endpoints of the intervals, as well as checking the unconstrained minimizer (if there is one).

While one-variable problems are rarely interesting by themselves, we will take advantage of their solvability in §4.2 to develop a greedy heuristic for. For more details on the solution method and time complexity analysis, see Appendix A.

### QCQP with one constraint

Consider QCQPs with a single constraint (i.e., $m = 1$):

Even when $f_{0}$ and $f_{1}$ are both nonconvex, is solvable in polynomial time \[ LMS^+^10\]. This result, also known as the $S$-procedure in control theory \[, \], states that even though is not convex, strong duality holds and the Lagrangian relaxation produces the optimal value $f^{\star}$. A variant of with an equality constraint ${f_{1}{(x)}} = 0$ is also efficiently solvable.

In Appendix B, we derive a solution method for the special case of, where the objective function is given by ${f_{0}{(x)}} = {\|{x - z}\|}_{2}^{2}$. This particular form will be used extensively in §4.4. Refer to \[ \] for the solution methods for the general case.

### QCQP with one interval constraint

Consider a variant of, with an interval constraint:

Solving this variant reduces to solving twice, once with the upper bound constraint ${f_{1}{(x)}} \leq u$ only, and once with the lower bound constraint ${f_{1}{(x)}} \geq l$ only \[, \]. One of the solutions is guaranteed to be an optimal point of.

### QCQP with homogeneous constraints with one negative eigenvalue

Consider a homogeneous constraint of the form ${x^{T}Px} \leq 0$, where $P$ has exactly one negative eigenvalue. This constraint can be rewritten as a disjunction of two second-order cone (SOC) constraints \[\]. Let $P = {Q\LambdaQ^{T}}$ be the eigenvalue decomposition of $P$, with $\lambda_{1} < 0$. Then, ${x^{T}Px} \leq 0$ if and only if

where $q_{1},\ldots,q_{n}$ are the columns of $Q$. Depending on the sign of $q_{1}^{T}x$, one of the following SOC inequalities is true if and only if ${x^{T}Px} \leq 0$:

Suppose that the constraint ${x^{T}Px} \leq 0$ was the only nonconvex constraint of. Then, we can solve two convex problems, one where the nonconvex constraint is replaced with, and the other where the same constraint is replaced with. The one that attains a better solution is optimal. Note that if the sign of $q_{1}^{T}x$ of any solution is known, then that information can be used to avoid solving both and. For example, if it is known a priori that some solution $x$ satisfies ${q_{1}^{T}x} \geq 0$, then only needs to be solved.

This approach generalizes to the case where there are multiple constraints in the form of ${x^{T}Px} \leq 0$, where $P$ has exactly one negative eigenvalue. With $k$ such constraints, one needs to solve $2^{k}$ convex problems.

### Algorithm

We introduce the *Suggest-and-Improve* framework, which is a simple but flexible idea that encapsulates all of our heuristics. The overall algorithm can be summarized in two high-level steps, as shown in Algorithm 1.3.

Algorithm 1.1 *Suggest-and-Improve algorithm.*

For Algorithm 1.3 to be well-defined, we need the notion of better points used in the *Improve* step. While there are other reasonable ways to define this, we use the following definition throughout the paper. Let $p_{+} = {\max{\{ p,0\}}}$ denote the positive part of $p \in \text{R}$, and

denote the maximum constraint violation of $x \in \text{R}^{n}$. We say $z \in \text{R}^{n}$ is *better* than $x \in \text{R}^{n}$ if one of the following conditions is met:

Maximum constraint violation of $z$ is smaller than that of $x$, i.e., ${v{(z)}} < {v{(x)}}$.

Maximum constraint violation of $z$ and $x$ are the same, and the objective function attains smaller value at $z$ than at $x$, i.e., ${v{(z)}} = {v{(x)}}$ and ${f_{0}{(z)}} < {f_{0}{(x)}}$.

In other words, we are defining better points in terms of the lexicographic order of the pair $({v{(x)}},{f_{0}{(x)}})$. This definition easily extends to the notion of a best point in the set of points (note that there can be multiple best points in a given set).

The candidate points returned from the *Suggest* method serve as starting points of local methods in the *Improve* step, and we do not require any condition on them in terms of feasibility. *Suggest* methods can be randomized, and parallelized to produce multiple candidate points. *Improve* methods attempt to produce better points (as defined above) than the candidate points. *Improve* methods can be applied in a flexible manner. For example, note that composition of any number of *Improve* methods is also an *Improve* method. One can also apply different *Improve* methods to a single candidate point in parallel. Similarly, given multiple candidate points, one can apply multiple *Improve* methods on each candidate point and take a best one.

There are many different ways to implement the *Suggest* and *Improve* methods, and how they are implemented determines the running time, suboptimality, and various other properties of the overall algorithm. Essentially, they can be considered as modules that one can choose from a collection of alternatives. Throughout the paper, we will explore different options to implement them.

To motivate the discussions, we start by recognizing a wide variety of well-known problem classes and examples that can be formulated as QCQPs, in §2. In §3, we explore ways to implement the *Suggest* step. Our focus is on the *relaxation* technique, which is typically used to approximate the solution to computationally intractable problems by replacing constraints with some other constraints that are easier to handle. We will discuss various relaxations of for finding reasonable candidate points, as well as obtaining a lower bound on the optimal value $f^{\star}$. Then, in §4, we discuss local optimization methods for improving a given candidate point. We will start with specialized methods for some subclasses of QCQP, and give three methods that can be applied to general QCQPs. Finally, we introduce an open-source implementation of these methods in §5, and show several numerical examples in §6.

### Previous work

### Quadratic programming

Research on QP began in the 1950s (see, e.g., \[, \]). Several hardness results on QP were published once the concept of NP-completeness and NP-hardness was established in the early 1970s \[, \]. In particular, \[\] showed that QP with a negative definite quadratic term is NP-hard. On the other hand, QP with convex objective function was shown to be polynomial-time solvable \[\].

### Quadratically constrained quadratic programming

Van de Panne \[\] studied a special class of QCQPs, which is to optimize an affine function subject to a single quadratic constraint over a polyhedron. While problems with a quadratic objective function and multiple quadratic constraints were introduced as early as 1951 in \[\], duality results and cutting plane algorithms for solving them were developed later \[\].

### QCQP with one constraint

Problem arises from many optimization algorithms, and most notably, in trust region methods \[ \]. Eigenvalue or singular value problems are also formulated in this form \[ \]. The strong duality result is known under various names in different disciplines. The term $\mathcal{S}$-procedure is from control theory \[, \]. Variations of the $\mathcal{S}$-procedure are known in linear algebra in the context of simultaneous diagonalization of symmetric matrices \[, \]. Many related results and additional references can be found in \[, §1.8\], and \[, §4.10.5\].

### Semidefinite programming

Semidefinite programming (SDP) and semidefinite programming relaxation (SDR) are closely related to QCQPs. The study of SDPs started since the early 1990s \[, \], and subsequent research during the 1990s was driven by various applications, including combinatorial problems \[\], control \[ \], communications and signal processing \[ MDW^+^02\], and many other areas of engineering. For more extensive overviews and bibliographies of SDPs, refer to \[ \]. The idea of SDR for QCQPs was suggested as early as 1979 in \[\], but the work that started a rapid development of the technique was \[\], which applied SDR to the maximum cut problem and derived a data-independent approximation factor of $0.87856$. Since then, SDR has also been applied outside the domain of combinatorial optimization problems \[, LMS^+^10\].

### Global methods

Global methods for nonconvex problems always find an optimal point and certify it, but are often slow; the worst-case running time grows exponentially with problem size (unless P is NP). Many known algorithms for globally solving are based on the *branch-and-bound* framework. Branch-and-bound generally works by recursively splitting the feasible set into multiple parts and solving the problem restricted in each of the subdivision, typically via relaxation techniques. For more details on the branch-and-bound scheme, see \[ \]. A popular variant of the branch-and-bound scheme is the *branch-and-cut* method, which incorporates cutting planes \[\] to tighten the subproblems generated from branching \[, \]. See, for example, \[\] for a branch-and-cut method for solving. Linderoth \[\] proposes an algorithm that partitions the feasible region into the Cartesian product of two-dimensional triangles and rectangles. Burer and Vandenbussche \[\] shows an algorithm that uses SDR as a subroutine. A variant of the method tailored for nonconvex QPs also exists \[\].

### Existing solvers

There are a number of off-the-shelf software packages that can handle various subclasses of QCQP. We mention some of the solvers here: GloMIQO \[\], BARON \[\], Ipopt \[\], Couenne \[\], and others provide global methods for (mixed-integer) QCQPs. Gurobi \[\], CPLEX \[\], MOSEK \[\], and SCIP \[\] provide global methods for mixed-integer nonlinear programs, with limited support for nonconvex constraints. Packages such as ANTIGONE \[\], KNITRO \[\], and NLopt \[\] provide global and local optimization methods for nonlinear optimization problems.

## Examples and applications

In this section, we show various subclasses of QCQP, as well as several applications that are more specific.

### Examples

### Polynomial problems

A polynomial optimization problem seeks to minimize a polynomial over a set defined by polynomial inequalities:

Here, each $p_{i}:{\text{R}^{n}\rightarrow\text{R}}$ is a polynomial in $x$. All polynomial optimization problems can be converted to QCQPs by introducing additional variables that represent the product of two terms, and appropriate equality constraints that describe these relations. For example, in order to represent a term $x_{1}^{2}x_{2}$, one can introduce additional variables, say, $u$ and $v$, and add constraints $u = x_{1}^{2}$ and $v = {ux_{2}}$. Then we can simply write $v$ in place of $x_{1}^{2}x_{2}$. In general, at most $d - 1$ new variables and constraints are sufficient to describe any term of order $d$. By applying these transformations iteratively, we can transform the original polynomial problem into a QCQP with additional variables. As a concrete example, suppose that we want to solve the following polynomial problem:

in the variables ${x,y,z} \in \text{R}$. We introduce two new variables ${u,v} \in \text{R}$ along with two equality constraints:

The problem then becomes:

which is now a QCQP in the variables ${x,y,z,u,v} \in \text{R}$.

### Box-constrained mixed-integer quadratic programming

Mixed-integer quadratic programming (MIQP) is the problem of optimizing a quadratic function over a polyhedron, where some variables are constrained to be integer-valued. Typically, MIQP comes with a box constraint that specifies lower and upper bounds on $x$, in the form of $l \leq x \leq u$. Formally, it can be written as the following:

We can write the integer constraints as a set of nonconvex quadratic inequalities. For example, $x_{1} \in {\{ l_{1},{l_{1} + 1},\ldots,u_{1}\}}$ if and only if $l_{1} \leq x_{1} \leq u_{1}$ and

for all $k = {l_{1},{l_{1} + 1},\ldots,{u_{1} - 1}}$. By replacing the integer constraints in this way, we can write in the form of.

### Rank-constrained problems

Let $X \in \text{R}^{p \times q}$ be a matrix-valued variable. The rank constraint ${\operatorname{\mathbf{R}\mathbf{a}\mathbf{n}\mathbf{k}}{(X)}} \leq k$ can be written as a quadratic constraint by introducing auxiliary matrix variables $U \in \text{R}^{p \times k}$ and $V \in \text{R}^{k \times q}$, and adding an equality constraint $X = {UV}$. Note that this is a set of $pq$ equality constraints that are quadratic in the elements of $X$, $U$, and $V$:

### Applications

### Boolean least squares

The Boolean least squares problem has the following form:

in the variable $x \in \text{R}^{n}$, where $A \in \text{R}^{m \times n}$ and $b \in \text{R}^{m}$. This is a basic problem in digital communications (maximum likelihood estimation for digital signals). By writing the Boolean constraint $x_{i} \in {\{{- 1},1\}}$ as $x_{i}^{2} = 1$, we get a QCQP equivalent to:

### Two-way partitioning problems

The two-way partitioning problem can be written as the following \[, §5.1.5\]:

with variable $x \in \text{R}^{n}$, where $W \in \text{R}^{n \times n}$ is symmetric. This problem is directly a nonconvex QCQP of the form. (Notice, however, that this is a maximization problem, equivalent to minimizing the negative of the objective.) Since the constraints restrict the possible values of each $x_{i}$ to $+ 1$ or $- 1$, each feasible $x$ naturally corresponds to the partition

The matrix coefficient $W_{ij}$ can be interpreted as the utility of having the elements $i$ and $j$ in the same cluster, with $- W_{ij}$ the utility of having $i$ and $j$ in different clusters. Then, problem can be interpreted as finding the partition that maximizes the total utility over all pairs of elements.

It is possible to generalize this formulation to $k$-way partitioning problems. In this variant, we would like to partition the set $\{ 1,\ldots,n\}$ into $k$ clusters, where there is utility associated between every pair of elements not belonging to the same cluster:

Here, the matrices $W^{(u,v)}$ describe utility between clusters $u$ and $v$. The variables $x^{(u)}$ can be considered as indicator variables that represent which elements belong to cluster $u$. The first set of equality constraints limit each $x_{i}^{(u)}$ to be either $0$ or $1$. The second set of equality constraints states that element $i$ belongs to exactly one of the $k$ clusters.

### Maximum cut

The maximum cut problem is a classic problem in graph theory and network optimization, and is an instance of two-way partitioning problem. On an $n$-node graph $G = {(V,E)}$, where the nodes are numbered from $1$ to $n$, we define weights $W_{ij}$ associated with each edge ${(i,j)} \in E$. If no edge connects $i$ and $j$, we define $W_{ij} = 0$. The maximum cut problem seeks to find a cut of the graph with the largest possible weight, i.e., a partition of the set of nodes $V$ in two clusters $V_{1}$ and $V_{2}$ such that the total weight of all edges linking these clusters is maximized. Given an assignment $x \in {\{{- 1},{+ 1}\}}^{n}$ of nodes to the clusters, the value of the cut is defined by

which is also equal to

Here, $\mathbf{1}$ represents a vector with all components equal to one. The maximum cut problem, then, can be written as:

We can further rewrite so that the objective function is homogeneous in $x$. Let $L$ be the Laplacian matrix of the underlying graph $G$, which is given by

If the edge weights $W_{ij}$ are all nonnegative, the Laplacian $L$ is positive semidefinite (see, e.g., \[, §13.1\]). Using the Laplacian (and ignoring the constant factor), the maximum cut problem can be written in the same form as:

The *maximum graph bisection problem* is a variant of the maximum cut problem, which has an additional constraint that the two clusters $V_{1}$ and $V_{2}$ must have the same size, i.e., ${\mathbf{1}^{T}x} = 0$. (In this variant, we assume that $n$ is even.)

### Maximum clique

The maximum clique problem is to find the complete subgraph of the maximum cardinality in a given graph. The problem can be formulated as a QCQP:

Here, $A \in {\{ 0,1\}}^{n \times n}$ is the adjacency matrix of the given graph, where $A_{ii}$ is defined as $1$ for $i = {1,\ldots,n}$, for convenience. The first set of constraints can be interpreted as: "if nodes $i$ and $j$ are both in the clique, i.e., $x_{i} = x_{j} = 1$, then they must be connected by an edge, i.e., $A_{ij} = 1$."

### 3-satisfiability

The 3-satisfiability (3-SAT) problem is an NP-complete problem, which is to find an assignment to a set of Boolean variables $x_{1},\ldots,x_{n}$ that makes a given logical expression true. The given expression is a conjunction of $r$ logical expressions called *clauses*, each of which is a disjuction of three variables, with optional negations. This can be formulated as a quadratically constrained feasibility problem as the following:

Note that this is a feasibility problem, and thus an arbitrary objective function can be optimized (such as $\mathbf{1}^{T}x$). Here, the matrix $A \in \text{R}^{r \times n}$ and vector $b \in \text{R}^{r}$ encode the $r$ clauses in the following way:

Without loss of generality, we assume that no clause contains a variable and its negation at the same time, because such a clause can be left out without changing the problem. Each $b_{i}$ is set as the number of negated variables in the $i$th clause. For example, the inequality corresponding to a clause $({x_{1} \vee {\neg x_{4}} \vee x_{6}})$ would be

### Phase retrieval

The phase retrieval problem is to recover a general signal such as an image from the magnitude of its Fourier transform. There are many application areas of the phase retrieval problem, including, but not limited to: X-ray crystallography, diffraction imaging, optics, astronomical imaging, and microscopy \[ QSH^+^16 SEC^+^15\]. While there are different ways to formulate the problem, we give one in the form of a feasibility problem:

Here, the optimization variable is $x \in \text{R}^{n}$, and the problem data are ${a_{1},\ldots,a_{m}} \in \text{R}^{n}$ and ${b_{1},\ldots,b_{m}} \in \text{R}$.

### Multicast downlink transmit beamforming

In the context of communications, the downlink beamforming problem seeks to design a multiple-input multiple-output wireless communication system that minimizes the total power consumption, while guaranteeing that the users receive certain signal-to-interference noise ratio. (For more details, refer to \[GSS^+^10 LMS^+^10 \].) This problem can be formulated as a QCQP:

in the variable $x \in \text{R}^{n}$, where each $P_{i} \in \text{R}^{n \times n}$ is positive semidefinite.

### Power system state estimation

In power systems, fundamental laws such as Ohm's and Kirchhoff's laws dictate that all power quantities in power systems are quadratic functions of the voltages. Many power engineering problems, therefore, are naturally written as QCQPs \[, \]. For example, the power system state estimation problem can be formulated as a weighted nonlinear least squares problem:

in the variable $x \in \text{R}^{n}$, where $P_{i} \in \text{R}^{n \times n}$ and ${v,w} \in \text{R}^{m}$ are given data. This is a polynomial optimization problem, which can be reformulated as a QCQP.

## Relaxations and bounds

A *relaxation* of an optimization problem is obtained by taking a set of constraints and replacing it with a different set of constraints, such that the resulting feasible set contains the feasible set of the original problem. Relaxations have a property that the optimal value $f^{rl}$ gives a lower bound on the optimal value $f^{\star}$ of the original problem. Tractable relaxations are of particular interest, since we can solve them to compute a lower bound on $f^{\star}$ of intractable optimization problems. While a solution $x^{rl}$ of a relaxation is generally infeasible in the original problem, it can still serve as a reasonable starting point of various local methods (which we discuss in §4). But if $x^{rl}$ is feasible in the original problem, then it is also a solution of the original problem.

Our main goal of the section is to implement the *Suggest* method of Algorithm 1.3 via various tractable relaxations of. As a byproduct, we also get a lower bound on $f^{\star}$.

### Spectral relaxation

First, we explore a relaxation of that is a generalized eigenvalue problem, hence the name *spectral relaxation*. This method generalizes eigenvalue bounds studied in \[ \]. Let $\lambda \in \text{R}_{+}^{m}$ be an arbitrary vector in the nonnegative orthant, and consider the following optimization problem:

Since $\lambda$ is elementwise nonnegative, every feasible point $x$ of is also feasible in. Thus, is a relaxation of, and its optimal value $f^{rl}$ is a lower bound on $f^{\star}$. Since is a QCQP with one constraint, it is a tractable problem that can be solved using methods via matrix pencil, for example \[ \]. It is easy to see that the same idea extends to problems with equality constraints. Below, we derive and show an explicit bound on $f^{\star}$ for some examples.

### Two-way partitioning problem

Let us derive a spectral relaxation of. Note that via relaxation, we are seeking an upper bound on $f^{\star}$ as opposed to a lower bound, since is a maximization problem. With $\lambda = \mathbf{1}$, the relaxation is:

It is easy to see that a solution $x^{rl}$ of this relaxation is given by

where $v$ is the eigenvector of unit length corresponding to the maximum eigenvalue $\lambda_{\max}$ of $W$. With this value of $x^{rl}$, we have $f^{rl} = {n\lambda_{\max}}$, which is an upper bound on $f^{\star}$.

We also note that by taking the sign of each entry of $x^{rl}$, we get a feasible point $z$ of. Then, evaluating the objective $z^{T}Wz$ gives a lower bound on $f^{\star}$. Thus, we get both lower and upper bounds on $f^{\star}$, simply by finding the largest eigenvalue and the corresponding eigenvector of $W$. In §4, we revisit this idea, and discuss various other methods for finding feasible points of general QCQPs in greater detail.

### Multicast downlink transmit beamforming

The spectral relaxation of with $\lambda = \mathbf{1}$ is:

Here, $\overline{P} = {{({1/m})}{({\sum_{i = 1}^{m}P_{i}})}}$. Let $\lambda_{\max}$ be the largest eigenvalue of $\overline{P}$, and $v$ be the corresponding eigenvector. Except in the pathological case where $\overline{P} = 0$, we have $\lambda_{\max} > 0$. By observing that the shortest vector $x^{rl}$ satisfying the constraint must be a multiple of $v$, we get

It is also possible to find a feasible point $z \in \text{R}^{n}$ from $x^{rl}$. Let

It is easy to check that $\hat{x}$ is a feasible point of. By evaluating the objective at this point, we get an upper bound on $f^{\star}$:

### Lagrangian relaxation

The Lagrangian relaxation provides another way to find a lower bound on $f^{\star}$, and it can be considered as a generalization of the spectral relaxation. See \[, §5\] or \[, §5\] for more background on Lagrangian duality results. In this section, we derive the Lagrangian relaxation of, which has been studied since the 1980s by Shor and others \[\]. To simplify notation, we first define, for $\lambda \in \text{R}_{+}^{m}$,

The *Lagrangian* of is given by

The *Lagrangian dual function* is then

where $\overset{\sim}{P}{(\lambda)}^{\dagger}$ and $\mathcal{R}{({\overset{\sim}{P}{(\lambda)}})}$ denote the Moore--Penrose pseudoinverse and range of $\overset{\sim}{P}{(\lambda)}$, respectively \[, §A.5\]. Using the Schur complement, we can write the Lagrangian dual problem as a semidefinite program (SDP):

with variables $\lambda \in \text{R}^{n}$, $\alpha \in \text{R}$.

Lagrangian relaxation and spectral relaxation are closely related techniques. We can show that solving the Lagrangian relaxation is equivalent to finding the value of $\lambda$ that achieves the best spectral bound. This property also implies a natural way of obtaining a candidate point $x^{rl}$; we first solve to obtain a solution $\lambda^{\star}$. Then, using the value of $\lambda^{\star}$, we solve the spectral relaxation. Its solution can be taken as a candidate point $x^{rl}$.

### Theorem 1

Let $d_{\lambda}$ be the optimal value of for a given $\lambda \in \text{R}_{+}^{m}$, and $d^{\star}$ be the optimal value of. Then,

### Proof

We first use the fact that strong duality holds for. The dual problem of can be derived in the same way we derived:

with variables ${\eta,\gamma} \in \text{R}$. Due to strong duality, has the same optimal value $d_{\lambda}$ as. Note that taking the supremum over $\lambda$ of $d_{\lambda}$ for all possible $\lambda \in \text{R}_{+}^{m}$ is equivalent to making $\lambda$ in an additional variable in $\text{R}_{+}^{m}$, and solving the resulting problem. In other words, $\sup_{\lambda \in \mathbf{R}_{+}^{m}}d_{\lambda}$ is the optimal value of the following optimization problem:

with variables ${\eta,\gamma} \in \text{R}$, $\lambda \in \text{R}^{m}$. Since both $\eta$ and $\lambda$ are constrained to be nonnegative, we can eliminate $\eta$ by replacing $\eta\lambda$ with $\lambda$ and keeping the nonnegativity constraint on $\lambda$. The resulting problem is then equivalent to, which proves the identity. ∎

### Semidefinite relaxation

In this section, we derive a semidefinite relaxation (SDR) using a technique called *lifting*. This SDR and the Lagrangian dual problem are Lagrangian duals of each other. To derive the SDR, we start by introducing a new variable $X = {xx^{T}}$ and rewriting the problem as:

in the variables $X \in \text{R}^{n \times n}$ and $x \in \text{R}^{n}$. This rewriting is called a *lifting*, as we have embedded the original problem with $n$ variables to a much larger space (of $n^{2} + n$ dimensions). By lifting, we obtain an additional property that the objective and constraints are affine in $X$ and $x$, except the last constraint $X = {xx^{T}}$ which is nonconvex. When we replace this intractable constraint with $X \succeq {xx^{T}}$, we get a convex relaxation. By rewriting it using the Schur complement, we obtain an SDR:

The optimal value $f^{sdr}$ of problem is then a lower bound on the optimal value $f^{\star}$ of. Under mild assumptions (e.g., feasibility of the original problem), has the same optimal value as. If an optimal point $(X^{\star},x^{\star})$ of satisfies $X^{\star} = {x^{\star}x^{\star T}}$ (or equivalently, the rank of $Z{(X^{\star},x^{\star})}$ is one), then $x^{\star}$ is a solution of the original problem.

It may look like we have created too much slack by lifting the problem to a higher-dimensional space, followed by relaxing the equality constraint $X = {xx^{T}}$ to a semidefinite cone constraint. However, we can show that the SDR is tight when the original problem is convex.

### Lemma 1

Let $(X,x)$ be any feasible point of. Then, $x$ satisfies every convex constraint of.

### Proof

It is enough to verify the claim for any arbitrary convex constraint ${{x^{T}Px} + {q^{T}x} + r} \leq 0$ with $P \succeq 0$. Since $(X,x)$ is a feasible point of, we have $X \succeq {xx^{T}}$. Then,

Thus, if the righthand side is nonpositive, so is the lefthand side. The claim follows. ∎

### Lemma 2

If problem is convex, then its SDR is tight, i.e., $f^{\star} = f^{sdr}$.

### Proof

Lemma 1 implies that if is convex, then for any feasible point $(X,x)$ of, replacing $X$ with $xx^{T}$ gives another feasible point with lower or equal objective value, i.e., there exists an optimal point of that satisfies $X = {xx^{T}}$. Thus, adding an additional constraint $X = {xx^{T}}$ to, which makes the problem equivalent to, does not change the set of solutions, nor the optimal value. ∎

While the SDR bound is not tight in general, in some cases, it is possible to give a lower bound on $f^{sdr}$ in terms of $f^{\star}$, which effectively gives both lower and upper bounds on $f^{\star}$. The famous result by \[\] guarantees a data-independent approximation factor of $0.87856$ to the maximum cut problem. Their analysis is based on the fact that the SDR can be interpreted as a stochastic version of \[, LMS^+^10\]. This interpretation gives a natural probability distribution to sample points from, which can be used to implement a randomized *Suggest* method in step 1 of Algorithm 1.3. There are other problem instances where similar approximation factors can be given. These approximation factors, however, greatly depend on the underlying problems. We refer the readers to \[LMS^+^10\] for a summary of some major results on SDR approximation factors.

Let $(X^{\star},x^{\star})$ be any optimal solution of. Suppose $x \in \text{R}^{n}$ is a Gaussian random variable with mean $\mu$ and covariance $\Sigma$. Then, $\mu = x^{\star}$ and $\Sigma = {X^{\star} - {x^{\star}x^{\star T}}}$ solve the following problem of minimizing the expected value of a quadratic form, subject to quadratic inequalities:

in variables $\mu \in \text{R}^{n}$ and $\Sigma \in \text{R}^{n \times n}$. Intuitively, minimizing the expected objective value promotes $\mu$ to move closer to the minimizer of $f_{0}$ and $\Sigma$ to be "small," the constraints counteract this and promote $\Sigma$ to be "large" enough that the constraints hold in expectation. Since the constraints are satisfied only in expectation, there is no guarantee that sampling points directly from $\mathcal{N}{(\mu,\Sigma)}$ gives feasible points of at all. In particular, if includes an equality constraint, then it will almost certainly fail. However, recall that the *Suggest* methods do not require feasibility; sampling candidate points from $\mathcal{N}{(\mu,\Sigma)}$ is a reasonable choice for the *Suggest* method. These candidate points then serve as good starting points for the *Improve* methods, which we discuss in detail in §4.

In certain cases, the probabilistic interpretation also allows us to get a hard bound on the gap between the optimal values $f^{\star}$ of the original problem and $f^{sdr}$ of its SDR. A classic example is that of the maximum cut bound described in \[\], which states that for an undirected graph with nonnegative edge weights, the SDR of the maximum cut problem attains the following bound:

for $\alpha \approx 0.87856$. (Note that this is a maximization problem.)

Here, we derive a similar bound of $\alpha = {2/\pi} \approx 0.63661$. This result, also known as Nesterov's $\pi/2$ theorem, extends the result of \[\] to any two-way partitioning problem with $W \succeq 0$. Note that we do not require the off-diagonal entries of $W$ to be nonpositive, which is necessary to get the stronger bound of $\alpha \approx 0.87856$ in \[\].

### Theorem 2 (Nesterov \[Nes98a, Nes98b\])

Let $f^{sdr}$ be the optimal value of the SDR of, where $W \succeq 0$. Then,

### Proof

Let $X^{\star}$ be any solution of the SDR, and $f^{sdr} = {\operatorname{\mathbf{T}\mathbf{r}}{({WX^{\star}})}}$ be the optimal value of the SDR. Consider drawing $x$ from the Gaussian distribution $\mathcal{N}{(0,X^{\star})}$, and setting $z = {\operatorname{\mathbf{s}\mathbf{i}\mathbf{g}\mathbf{n}}{(x)}}$, where $\operatorname{\mathbf{s}\mathbf{i}\mathbf{g}\mathbf{n}}{( \cdot )}$ denotes the elementwise sign function. Note that $z$ is always a feasible point of. The special form of the objective function allows us to find the expected value of the objective $\mathbf{E}{({z^{T}Wz})}$ analytically:

where $\arcsin X^{\star}$ is a matrix obtained by taking elementwise $\arcsin$ of the entries of $X^{\star}$. Since ${\arcsin{(X^{\star})}} \succeq X^{\star}$ (see, e.g., \[, §3.4.1.6\]) and $W$ is positive semidefinite, we get

On the other hand, since $z$ is always feasible, we have

Together with the fact that the relaxation attains the optimal value $f^{sdr}$ no worse than $f^{\star}$, i.e., $f^{sdr} \geq f^{\star}$, we have

Note that this result not only bounds $f^{sdr}$ in terms of $f^{\star}$, but also shows an explicit procedure for generating feasible points that have the expected objective value of at least ${({2/\pi})}f^{sdr}$. In §4.1, we revisit this procedure in the context of *Improve* methods. In practice, sampling just a few points is enough to obtain a feasible solution that exceeds this theoretical lower bound.

### Tightening relaxations

Lower bounds obtained from relaxations can be improved by adding additional quadratic inequalities to that are satisfied by any solution of the original problem. In particular, redundant inequalities that hold for all feasible points of can still tighten the relaxation. We note, however, that in order for these inequalities to be useful in practice, they must be computationally efficient to derive. For example, the inequality ${f_{0}{(x)}} \leq f^{\star}$ holds for every optimal point of the problem, but it cannot be added to the problem without knowing the value of $f^{\star}$. All the valid inequalities we discuss below, therefore, will be restricted to the ones that can be derived efficiently.

Consider the set of affine inequalities ${Ax} \leq b$ in. For every vector $x$ satisfying ${Ax} \leq b$, we have

where the inequality is elementwise. Each entry of the lefthand side has the form

where $a_{i} \in \text{R}^{n}$ is the $i$th row of $A$ (considered as a column vector). These indefinite quadratic inequalities then can be added to the original QCQP without changing the set of solutions.

In certain special cases, there are other valid inequalities that can be derived directly from the structure of the feasible set. For example, take any Boolean problem where the feasible set is given by ${\{{- 1},{+ 1}\}}^{n}$. Since the entries of any feasible $x$ are integer-valued, for any $a \in \text{Z}^{n}$ and $b \in \text{Z}$, we have

While these are redundant inequalities, adding them to the problem can tighten its relaxations.

This technique can be generalized further; any exclusive-disjunction of two affine inequalities can be encoded as a quadratic inequality. Let ${a^{T}x} \leq b$ and ${c^{T}x} \leq d$ be two affine inequalities such that for every feasible point of, exactly one of them holds. Then,

is a redundant quadratic inequality that holds for every feasible point $x$.

### Relaxation of relaxations

The Lagrangian and semidefinite relaxations and are polynomial-time solvable, but in practice, can be expensive to solve as the dimension of the problem gets larger. In this section, we explore several ways to further relax the relaxation methods discussed above to obtain lower bounds on $f^{\star}$ more efficiently.

We first discuss how to further relax the Lagrangian relaxation. Weak duality implies that it is not necessary to solve optimally in order to obtain a lower bound on $f^{\star}$; any feasible point $(\lambda,\alpha)$ of induces a lower bound on $f^{\star}$. We note that $\alpha$ is easy to optimize given $\lambda$. In fact, when $\lambda$ is fixed, optimizing over $\alpha$ is equivalent to solving the spectral relaxation with the same value of $\lambda$.

Now, we discuss relaxation methods for the SDR. Note that the semidefinite constraint ${Z{(X,x)}} \succeq 0$ can be written as an infinite collection of affine constraint ${a^{T}Z{(X,x)}a} \geq 0$ for all $a \in \text{R}^{n + 1}$ of unit length, i.e., ${\| a\|}_{2} = 1$. For example, if $a$ is the $i$th unit vector, the resulting inequality states that $X_{ii}$ must be nonnegative. To approximate the optimal value $f^{sdr}$ of, one can generate affine inequalities to replace the semidefinite constraint and solve the resulting linear program (LP). While these affine inequalities can come directly from the valid inequalities we discussed in §3.4, it is also possible to adopt a cutting-plane method to generate them incrementally.

Algorithm 3.1 *Cutting-plane method for solving via LP relaxation.*

In step 4, vector $a \in \text{R}^{n + 1}$ satisfying the condition always exists, because ${Z{(X^{\star},x^{\star})}} \succeq 0$ is equivalent to $X^{\star} \succeq {x^{\star}x^{\star T}}$. For example, one can always take $a$ equal to the eigenvector corresponding to any negative eigenvalue of $Z{(X^{\star},x^{\star})}$. It is also possible to adapt the LDL factorization algorithm to verify whether $Z{(X^{\star},x^{\star})}$ is positive semidefinite, and terminate with a suitable vector $a$ in case it is not. We note that Algorithm 3.5, in general, need not converge, unless additional constraints are met, e.g., the vector $a$ in step 4 is the eigenvector corresponding to the minimum eigenvalue of $Z{(X^{\star},x^{\star})}$. However, at every iteration of step 2, we get a lower bound on $f^{\star}$ that is no worse than the value from the previous iteration. In practice, this means that the algorithm can terminate any time when a good enough lower bound is obtained.

It is also possible to write a second-order cone programming (SOCP) relaxation of, which can be thought of as a middle-point between LP and SDP relaxations \[\]. Second-order cone (SOC) constraints are more general than affine constraints, and can encode more sophisticated relations that hold for positive semidefinite matrices. For example, in order for $Z{(X,x)}$ to be positive semidefinite, every $2$-by-$2$ principal submatrices of it must be positive semidefinite, i.e., for every pair of indices $i$ and $j$,

These three inequalities are also equivalent to the following SOC inequalities \[, §4\]:

In general, in order for $Z{(X,x)}$ to be positive semidefinite, we must have, for every $({n + 1})$-by-$2$ matrix $A$,

which can be rewritten as SOC inequalities, just like. From this observation, it is simple to adapt Algorithm 3.5 to solve via SOCP relaxation.

## Local methods

In this section, we implement the *improve* method of Algorithm 1.3 using various local methods. These methods take an arbitrary point $x \in \text{R}^{n}$ that is not necessarily feasible in, and attempts to find a better point $z \in \text{R}^{n}$. Recall that in §1, we defined better points in terms of maximum constraint violation and objective value. In general, finding a feasible point is an NP-hard problem, for otherwise we can perform bisection on the optimal value of the epigraph form and find a solution to arbitrary precision in polynomial time. For this reason, we do not guarantee convergence of the methods or feasibility of the resulting points, except in some special cases discussed in §4.1.

### Special cases

We start by investigating some special cases, where we can directly exploit the problem structure and find a feasible point. Since we are guaranteed to find a feasible point with these methods, we also get an upper bound on $f^{\star}$ by evaluating the objective function at the resulting point. As it can be seen from the examples, these heuristics are highly problem dependent.

### Partitioning problems

The feasible set of the partitioning problem is

For any given $x \in \text{R}^{n}$, the point $z = {\operatorname{\mathbf{s}\mathbf{i}\mathbf{g}\mathbf{n}}{(x)}}$ is always feasible. It is easy to check that $z$ is a projection of $x$ onto $\mathcal{S}$, i.e., $z$ is the closest feasible point to $x$.

For the maximum graph bisection problem described in page 2.2, we can employ a slightly different method by \[\] to satisfy the additional constraint ${\mathbf{1}^{T}x} = 0$. Given $x \in \text{R}^{n}$, we find a feasible $z$ by setting $z_{i} = 1$ for indices $i$ corresponding to the $n/2$ largest entries in $x$, and $z_{i} = {- 1}$ for the other $n/2$ indices. (Ties are broken arbitrarily when some entries of $x$ have equal values.) It can be shown that $z$ is also a projection onto the set of feasible points.

### Multicast downlink transmit beamforming

The feasible set of is given by

Let $x \in \text{R}^{n}$ be an arbitrary point. By setting

we get a feasible point $z$ \[LMS^+^10\]. In other words, $z$ is the smallest multiple of $x$ that makes it feasible. (Recall that every $P_{i}$ is positive semidefinite.) Unlike in the case of partitioning problems, $z$ is not a projection of $x$ onto $\mathcal{S}$, even when $m = 1$.

### Maximum clique

Here, we adapt the main idea from the heuristic for the maximum graph bisection problem and generate a feasible point of the maximum clique problem from a given vector $x \in \text{R}^{n}$.

Algorithm 4.1 *Heuristic for finding a clique from a given vector.*

The intuition behind this heuristic is that $x_{i}$ with larger value should be more likely to be included in a clique. In particular, this heuristic always includes the node $i$ with the highest value of $x_{i}$. It is clear that at the end of Algorithm 4.1, $C$ is a clique. In addition, we can show that $C$ is a maximal clique, i.e., there is no node $k \notin C$ such that $C \cup {\{ k\}}$ is a clique.

### Lemma 3

The clique generated by Algorithm 4.1 is maximal.

### Proof

Assume on the contrary that the clique $C_{1}$ generated by Algorithm 4.1 is a proper subset of some other clique $C_{2}$. Choose an arbitrary $k \in {C_{2} \smallsetminus C_{1}}$. When $k$ is considered in Algorithm 4.1, the partial clique $C$ maintained by the algorithm is a subset of $C_{1}$. Since $C_{2}$ is a clique and $C_{1} \subset C_{2}$, $C \cup {\{ k\}}$ is a clique and thus $k$ must have been included in $C$, which leads to a contradiction. ∎

### Coordinate descent

From this section on, we consider general QCQPs that have no obvious structures that can be exploited as in §4.1. First, we show a *coordinate descent* heuristic for improving a given point. Coordinate descent is a simple and intuitive method for finding a local minimum of a function. For more results and references on general coordinate descent algorithms, see \[\].

Our greedy descent method is based on the fact that one-variable QCQPs are tractable. The algorithm consists of two phases:

### Phase I

The goal of the first phase is to reduce the maximum constraint violation and, if possible, reach a feasible point. Let $x \in \text{R}^{n}$ be a given candidate point. We repeatedly cycle over each coordinate $x_{j}$ of $x$, and update it to the value that minimizes the maximum constraint violation. In other words, at each step, we solve:

with variables ${x_{j},s} \in \text{R}$. For a fixed value of $s$, it is easy to adapt the method of Appendix A to check if is feasible in $x_{j}$. Therefore, by performing bisection on $s$, we can find the minimum possible value of $s$ to arbitrary precision, as well as a value of $x_{j}$ that attains the maximum violation of $s$. We note that in order to apply the method of Appendix A, we need to extract the quadratic, linear, and constant coefficients of each $f_{i}$ in $x_{j}$. If the $P_{i}$ matrices are not sparse, then evaluating these coefficients can dominate the running time.

When the optimal value of $s$ is zero or smaller, i.e., a feasible point is found, then phase I ends and phase II begins. On the other hand, if the maximum constraint violation cannot be improved for any $x_{j}$, then phase I terminates unsuccessfully (and needs a new candidate point).

### Phase II

Phase II starts once a feasible point is found. In this phase, we restrict ourselves to feasible points only, and look for another feasible point with strictly better objective value. Again, we cycle over each coordinate $x_{j}$ of $x$ and optimize the objective function while maintaining feasibility. In other words, we solve with all variables fixed but $x_{j}$. The implementation of phase II is a direct application of the method in Appendix A. While it is possible to run phase II until no improving direction is remaining, it can terminate at any point and will still yield a feasible point, as well as an upper bound on $f^{\star}$.

Phase II of the coordinate descent method generalizes local search methods for many combinatorial problems, such as the 1-opt local search heuristic, which have been studied since the 1950s \[\].

### Convex-concave procedure

The convex-concave procedure (CCP) is a powerful heuristic method for finding a local optimum of difference-of-convex (DC) programming problems, which have the following form:

where $f_{i}:{\text{R}^{n}\rightarrow\text{R}^{n}}$ and $g_{i}:{\text{R}^{n}\rightarrow\text{R}^{n}}$ for $i = {0,\ldots,m}$ are convex. We refer the readers to \[\] for extensive review and bibliography of CCP.

The main motivation for considering CCP to solve QCQPs is that any quadratic function can be easily rewritten as a DC expression. Consider, for example, an indefinite quadratic expression: ${x^{T}Px} + {q^{T}x} + r$. We decompose the matrix $P$ into the difference of two positive semidefinite matrices:

Such decomposition is always possible, by taking, for example, $P_{+} = {P + {tI}}$ and $P_{-} = {tI}$ for large enough $t > 0$. Then, we can explicitly rewrite the expression as the difference of two convex quadratic expressions:

Once is rewritten as a DC problem, any CCP method for locally solving DC problems can be applied. Here, we consider the penalty CCP method in \[\], which does not require the initial point to be feasible. The penalty CCP method seeks to optimize the convexified version of the objective, with an additional penalty on the convexified constraint violations. The method gradually increases the penalty on constraint violation over iterations. Convexification of the functions is done by linearizing each $g_{i}$ around the current iterate $x^{k}$:

Formally, the penalty CCP method can be written as below.

Algorithm 4.2 *Penalty CCP.*

There are a number of reasonable stopping criteria \[\]. For example, Algorithm 4.3 can terminate when a feasible point is found, or the maximum penalty parameter is reached, i.e., $\tau_{k} = \tau_{\max}$. When implementing Algorithm 4.3, there are other factors to consider than the initial point or the penalty parameters; the performance of the algorithm can vary depending on how indefinite quadratic functions are split into the difference of two convex quadratic expressions. In Appendix C, we discuss various ways of splitting quadratic functions into convex parts.

### Alternating directions method of multipliers

The alternating directions method of multipliers (ADMM) is an operator splitting algorithm that is originally devised to solve convex optimization problems \[BPC^+^11\]. However, due to the flexibility of the ADMM framework, it has been explored as a heuristic to solve nonconvex problems. (See, e.g., \[BPC^+^11, §9\], or \[, \].) Here, we consider an adaptation of the algorithm to the QCQP, as considered in \[\]. Note that due to nonconvexity of QCQPs, typical convergence results on ADMM do not apply.

Let $\mathcal{C} \subseteq \text{R}^{n}$ be a given set, and consider the following variant of:

With $\mathcal{C} = \text{R}^{n}$, problem is the same as. In this section, we use as our primary problem formulation rather than, and handle the last constraint $x \in \mathcal{C}$ differently from the other constraints.

To apply ADMM, we take and form an equivalent problem with a consensus constraint:

with variables ${z,x_{1},x_{2},\ldots,x_{m}} \in \text{R}^{n}$. It is important to note that $x_{i}$ does not represent the $i$th component of $x$; rather, it represents the $i$th copy of the variable $x$, all of which should be equal to each other. The function $\mathcal{I}_{\mathcal{C}}$ is the $0$--$\infty$ indicator of the set $\mathcal{C}$:

Similarly, $\mathcal{I}_{i}$ is the $0$--$\infty$ indicator function of the constraint ${f_{i}{(x)}} \leq 0$:

The augmented Lagrangian of the problem is:

where each $u_{i} \in \text{R}^{n}$ are *scaled dual variables* \[BPC^+^11, §3.1.1\]. The *penalty parameter* $\rho > 0$ controls the convergence behavior or ADMM. We postpone the discussion on how to choose the parameter, and describe the ADMM iteration first:

The update rules for $z$ and $x$ each involves solving an optimization problem, but some observations allow us to simplify them. To simplify the $z$-update, we ignore the terms in the augmented Lagrangian that do not depend on $z$. Then, $z^{k + 1}$ is given by the solution of the following QCQP:

in the variable $z \in \text{R}^{n}$. There are a number of cases where is tractable.

When the penalty parameter $\rho > 0$ satisfies

where $\lambda_{\min}$ is the smallest eigenvalue of $P_{0}$, then is a convex problem and thus is tractable.

If the constraint $z \in \mathcal{C}$ can be written as a single quadratic inequality constraint, then is a QCQP with a single constraint, which is tractable regardless of convexity of $\mathcal{C}$ or the value of $\rho$.

When $\mathcal{C} = \text{R}^{n}$ and the penalty parameter $\rho$ is chosen such that the objective function is strictly convex, i.e.,

then we can perform the $z$-update by solving a single linear system. To see this, rewrite the objective function of as

with appropriate $\overset{\sim}{P} \in \text{R}^{n \times n}$, $\overset{\sim}{q} \in \text{R}^{n}$, and $\overset{\sim}{r} \in \text{R}$. Since $\overset{\sim}{P} \succ 0$, the minimizer of the expression above can be found by simply setting the gradient with respect to $z$ equal to zero:

Assuming that the value of $\rho$ is fixed for every iteration, the coefficient matrix $\overset{\sim}{P}$ on the lefthand side stays the same for every $z$-update. Using this observation, we can perform the $z$-update efficiently as follows: we compute the factorization of the coefficient matrix $\overset{\sim}{P}$ once, and for every subsequent $z$-update, use the cached factorization to carry out the back-solve. The improvement in running time is the most significant when $\overset{\sim}{P}$ is dense, as the cost of factorization is $O{(n^{3})}$, and each back-solve only takes $O{(n^{2})}$ time.

The $x$-updates can be simplified as well by ignoring terms that do not depend on $x_{i}$. Then, $x_{i}^{k + 1}$ is given by the solution of the following QCQP:

with variable $x_{i} \in \text{R}^{n}$. Note that is a special form of, which is tractable. We cover the solution methods for solving in Appendix B. Since only depends on $z^{k + 1}$ and $u_{i}^{k}$, all $x$-updates trivially parallelizes over $i = {1,\ldots,m}$.

Below, we discuss several extensions of the ADMM-based *Improve* method.

### Equality constraints

When some constraints are equality constraints, then only the corresponding $x$-updates need to be modified accordingly. For example, if the $i$th constraint is an equality constraint ${f_{i}{(x)}} = 0$, then in order to perform the $x$-update, we would solve

### Convex constraints

Note that any number of convex constraints of can be encoded in the constraint $x \in \mathcal{C}$. In general, this will change the behavior of the algorithm, including how quickly the $z$-update can be performed.

### Two-phase ADMM

While the ADMM update rules take a simple form and are easy to implement, it is still a heuristic applied to a nonconvex problem, and thus in practice, it may be more important to set the initial point and the penalty parameter $\rho$ carefully. Here, we show an adaptation of the two-phase ADMM method by Huang and Sidiropoulos \[\], that can attain faster convergence in practice. In phase I, much like the two-phase coordinate descent algorithm introduced in §4.2, the algorithm first focuses on finding a feasible point by ignoring the objective function. Once a feasible point is found, phase II begins. In phase II, the objective function is brought back into consideration and ADMM iterations are performed until convergence.

The only difference of the two phases is that in phase I, the objective function $f_{0}$ is completely ignored. This simplifies the $z$-update of phase I; in order to perform the $z$-update, we solve the following optimization problem:

with variable $z \in \text{R}^{n}$. Define

The solution of is simply given by the projection of $\overline{z}$ onto $\mathcal{C}$. As long as $\mathcal{C}$ is convex, the projection can be found efficiently. The $x$- and $u$-update rules stay the same. Notice that the new $z$-update rule is independent of $\rho$. In other words, the ADMM iterates in phase I are completely determined by the initial point.

We note that depending on the initialization, the iterates in phase I can be stuck in an infinite loop of period greater than 1, even for very small problems. Consider a $3$-dimensional two-way partitioning problem, which has three equality constraints

Consider the following initial points:

For this particular initialization, we get

and thus the iterates repeat themselves with period $2$. It can be verified that any initialization close to this will also fail to converge to a feasible point.

## Implementation

We introduce an open source Python package QCQP that accepts high-level description QCQPs as input and implements Algorithm 1.3. As our main platform, we used CVXPY, a domain-specific language for convex optimization \[\]. The source code repository for QCQP is available at https://github.com/cvxgrp/qcqp.

### Quadratic expressions

The CVXPY parser determines curvature, sign, and monotonicity of expressions according to the *disciplined convex programming* (DCP) rules \[\]. We have extended the parser so that it can also determine quadraticity of an expression, based on the rules that are similar to the DCP rules. The following list of expressions is directly recognized as quadratic by CVXPY:

any constant or affine expression

any affine transformation of a quadratic expression, e.g., the sum of quadratic expressions

product of two affine expressions

elementwise square `power(X, 2)` or `square(X)`, with affine `X`

`sum_squares(X)` with affine `X`, representing $\sum_{ij}X_{ij}^{2}$.

`quad_over_lin(X, c)` with affine `X` and positive constant `c`, representing ${({1/c})}{\sum_{ij}X_{ij}^{2}}$

`matrix_frac(x, P)` with affine `x` and symmetric constant `P`, representing $x^{T}P^{- 1}x$

`quad_form(x, P)` with affine `x` and symmetric constant `P`, representing $x^{T}Px$

### Constructing problem and applying heuristics

Our implementation can handle QCQPs constructed using the standard CVXPY syntax. As long as the objective function and both sides of the constraints are quadratic, the problem is accepted even when it is nonconvex. In order to apply the *Suggest-and-Improve* framework, a CVXPY problem object must be passed to the QCQP constructor first. For example, if `problem` is a CVXPY problem object, then the following code checks whether `problem` describes a QCQP, and if so, prepares the *Suggest* and *Improve* methods:

qcqp = QCQP(problem)Once the `qcqp` object is constructed, a number of different *Suggest* and *Improve* methods can be invoked on it. Currently, three *Suggest* methods are available:

`qcqp.suggest()` or `qcqp.suggest(RANDOM)` fills the values of the variables using independent and identically distributed Gaussian random variables.

`qcqp.suggest(SPECTRAL)` fills the values of the variables with a solution of the spectral relaxation. The spectral lower bound (or upper bound, in the case of a maximization problem) on the optimal value $f^{\star}$ is accessible via `qcqp.spectral_bound`.

`qcqp.suggest(SDR)` solves the SDR and fills the values of the variables according to the probabilistic interpretation discussed in page 3.3. The SDR bound on the optimal value is accessible via `qcqp.sdr_bound`.

Below is a list of available *Improve* methods:

`qcqp.improve(COORD_DESCENT)` performs the two-stage coordinate descent method, as described in §4.2.

`qcqp.improve(DCCP)` rewrites the problem in the DC form then runs the penalty CCP method in §4.3 using the open source Python package DCCP.

`qcqp.improve(ADMM)` runs the two-phase ADMM, as described in §4.4.

As mentioned in §1.3, composition of any number of *Improve* methods is also an *Improve* method. It is easy to apply a sequence of *Improve* methods by passing a list of methods to `improve()`:

qcqp.improve(method_sequence)This is equivalent to:

for method in method_sequence: qcqp.improve(method)Various parameters can be supplied to the *Suggest* and *Improve* method, such as the penalty parameter $\rho$ of the two-phase ADMM, penalty parameter $\tau$ of the penalty CCP, maximum number of iterations, and tolerance value for determining near-zero quantities. All *Suggest* and *Improve* methods return a pair $({f_{0}{(x)}},{v{(x)}})$, i.e., the objective value and maximum constraint violation at the current point $x$.

### Sample usage

In this section, we show a sample usage of the QCQP package with a small two-way partitioning problem with $n = 10$. We start by importing the necessary packages, and constructing a symmetric matrix $W \in \text{R}^{n \times n}$:

import numpy as np, cvxpy as cvxfrom qcqp import \*n = 10W0 = np.random.randn(n, n)W = 0.5\*(W0 + W0.T)For clarity, we imported NumPy and CVXPY with explicit namespaces. Next, we construct a CVXPY problem instance describing.

x = cvx.Variable(n)prob = cvx.Problem( cvx.Maximize(cvx.quad_form(x, W)), \[cvx.square(x) == 1\])While CVXPY allows defining `prob`, it is not possible to invoke the `solve()` method on it because the objective function is not concave, and the constraints are nonconvex. However, we can pass it as an argument to the QCQP constructor to indicate that `prob` is a QCQP:

qcqp = QCQP(prob)Now we can call `suggest()` and `improve()` methods on `qcqp`. Here, we solve the spectral relaxation with $\lambda = \mathbf{1}$, for which both the optimal value and solution are known. Although it is not necessary, we use the MOSEK solver \[\] for robustness.

qcqp.suggest(SPECTRAL, solver=cvx.MOSEK)This fills `x.value`, the numerical value of `x`, with the solution of the spectral relaxation. The spectral bound can be accessible via `qcqp.spectral_bound`. We print out this value and compare it with $f^{rl} = {n\lambda_{\max}}$ shown in §3.1.

print (\"Spectral bound: %.4f\" % qcqp.spectral_bound)(w, v) = np.linalg.eig(W)print (\"n\*lambda_max: %.4f\" % (max(w)\*n))Indeed, we see that both values coincide:

Spectral bound: 31.2954n\*lambda_max: 31.2954We can also verify that the value `x.value` is correctly populated with the (scaled) eigenvector of $W$ corresponding to its maximum eigenvalue. Next, we apply the two-phase coordinate descent heuristic on `x.value`, and print out the objective value and maximum constraint violation at the resulting point.

f_cd, v_cd = qcqp.improve(COORD_DESCENT)print (\"Objective: %.4f\" % f_cd)print (\"Maximum violation: %.4f\" % v_cd)In this example, we get a feasible point:

Objective: 23.1687Maximum violation: 0.0000We can print out `x.value` and check that every coordinate is indeed $\pm 1$. Since $n$ is small, we can enumerate every one of $2^{n} = 1024$ feasible points and verify that `x.value` is a global solution of the problem. See Appendix D for the full version of the script.

## Numerical examples

In this section, we consider two numerical examples and perform the heuristics implemented in the QCQP package. In Appendix D, we give sample Python script for writing these example problems as QCQPs and applying the *Suggest-and-Improve* framework using our package. More examples can be found in the package repository.

### Specialized methods

We note that any kind of method tailored to particular problems, e.g., maximum cut, multicast beamforming, or other well-known problems described in §2, will almost certainly perform better than QCQP, and our objective is not to compete with these specialized methods. The primary goal of the package, instead, is to provide an easily accessible interface to various heuristics for NP-hard QCQPs that do not have specialized methods.

### Running time

Currently, QCQP supports minimal parallelism and introduces computational overhead by explicitly representing quadratic expressions by their coefficient matrices. The implementation can be improved further by better exploiting parallelism, and rewriting parts of the codes in low-level languages such as C. Further optimizing the performance of the heuristics is left as future work. The reported running times are CPU times (measured using the Python `time.clock()` function) based on experiments performed on a 3.40 GHz Intel Xeon machine, running Ubuntu 16.04.

### Boolean least squares

Here, we consider the Boolean least squares problem from §2.2.

### Problem instance

We generated a random problem instance with $n = 50$ and $m = 80$, where the entries of $A$ and $b$ are drawn IID from $\mathcal{N}{}$. The feasible set has $2^{n} \approx 10^{15}$ points.

### Results

We tested various combinations of *Suggest* and *Improve* methods. For each combination, we sampled 20 candidate points and improved them, and took the best point. In this example, we considered all three different *Suggest* methods in §5.2: random, spectral, and SDR. For the *Improve* methods, we considered three methods as follows:

Round: rounding the candidate point to the nearest feasible point, as discussed in §4.1.

CD: two-phase coordinate descent, as discussed in §4.2.

CCP: penalty CCP, as discussed in §4.3.

While it is possible to apply multiple *Improve* methods sequentially, we did not consider them in this experiment. We excluded the two-phase ADMM because it easily fails to generate a feasible point when applied to Boolean problems, as noted in page 4.4. For the penalty CCP heuristic, we used the penalty parameter of $\tau = 1$.

All three *Improve* methods yielded a feasible point for every candidate point generated by *Suggest* methods. In Table 1, we show, for every combination of the *Suggest* and *Improve* methods, the objective value of the best point found and the total running time (which includes the solve time of the relaxations).

Spectral and semidefinite relaxations yielded lower bounds of $228$ and $518$, respectively. The best feasible point found had the objective value of $988$, and it was obtained by performing coordinate descent on SDR-based candidate points. Since the problem instance was small enough to find the global solution, we used Gurobi \[\] to find the optimal value $f^{\star}$, which was $920$. As pointed out in \[, dB03\], this optimal value is closer to the best upper bound of $988$, rather than to the SDR bound of $518$.

Rounding a random point to the nearest feasible point is equivalent to choosing a random feasible point. As expected, this method performed the worst: the best objective value attained was $2719$. Significantly better points were obtained by changing the *Suggest* method: rounding the solution of the spectral relaxation gave a point with objective $1605$, and rounding the SDR-based candidate points gave the best objective of $1098$. The performance was further improved by performing the two-phase coordinate descent *Improve* method. With two-phase coordinate descent, even random candidate points yielded a better point than rounding SDR-based candidate points. This result is quite intuitive, because coordinate descent is a natural heuristic choice for Boolean problems. In fact, applying the two-phase coordinate descent in this setting reduces to a heuristic that performs well in practice \[\], which is to round the candidate point to the nearest point (phase I), and perform a 1-opt local search (phase II). In this example, the penalty CCP found the same feasible point for every given candidate point, regardless of the *Suggest* method.

In terms of the running time, we found, for this problem, that there is no benefit in running the penalty CCP or two-phase ADMM; the two-phase coordinate descent yielded the best point faster than them. We note that the running time of Gurobi for finding the optimal value was $1793$ seconds (CPU time).

Table 1: Objective value of the best point found (left), and total running time (right) of the Suggest-and-Improve heuristic on the Boolean least squares problem.

### Secondary user multicast beamforming

We consider the secondary user multicast beamforming problem, which is a variant of studied in \[, \]. The problem can be formulated as the following:

Here, $w \in \text{C}^{n}$ is the variable, and ${h_{i},g_{j}} \in \text{C}^{n}$ are given problem data, for $i = {1,\ldots,m}$ and $j = {1,\ldots,l}$. Since CVXPY and QCQP do not directly support complex-valued variables and data, we form an equivalent problem with real numbers only. For $i = {1,\ldots,m}$, let

be real-valued vectors in $\text{R}^{2n}$. (Here, ${\Re z} \in \text{R}^{n}$ and ${\Im z} \in \text{R}^{n}$ denote the real and imaginary parts of a complex-valued vector $z \in \text{C}^{n}$.) Similarly, for $j = {1,\ldots,l}$, define

By introducing another variable $x \in \text{R}^{2n}$ to represent the real and imaginary parts of $w$, we can rewrite using real-valued variables and data only:

### Problem instance

We considered a problem instance with $n = 50$, $m = 20$, and $l = 5$. The entries of the $a_{i}$, $b_{i}$, $c_{j}$, and $d_{j}$ were drawn IID from $\mathcal{N}{}$. The other parameters were set as $\tau = 20$ and $\eta = 2$.

### Results

As in §6.1, we used a combination of *Suggest* and *Improve* methods. The list of *Improve* method we used for is the following:

Scale: scaling the candidate point so that it satisfies the first set of constraints,

as discussed in §4.1. Unlike, this problem has a second set of constraints, and therefore, this method does not necessarily yield a feasible point.

For the two-phase ADMM, we chose the penalty parameter $\rho = \sqrt{m + l}$, as in \[\]. For the other heuristics, we used the default parameters. For each choice of *Suggest* and *Improve* methods, we sampled 10 candidate points and improved them, and took the best point.

In Table 2, we show, for every combination of the *Suggest* and *Improve* methods, the objective value of the best feasible point found and the total running time (which includes the solve time of the relaxations). The Scale *Improve* method never produced a feasible point for all three *Suggest* methods, and therefore we left it out from the table.

Spectral and semidefinite relaxations yielded lower bounds of $1.11$ and $1.27$, respectively. The best feasible point found had the objective value of $1.30$, obtained by performing the penalty CCP on SDR-based candidate points.

Unlike in §6.1, the two-phase coordinate descent did not produce a good feasible point. On random candidate points, the best feasible point it found had the objective value of $9.62$. Even with the SDR-based candidate points, the best objective value was $2.51$. The two-phase ADMM, on the other hand, produced a point with objective value $1.86$ when combined with the SDR *Suggest* method. The penalty CCP method showed a more consistent performance for both random and SDR *Suggest* methods, and it found the best point with objective $1.30$. However, it was unable to produce a feasible point from the solution of the spectral relaxation.

We note that running ADMM followed by coordinate descent performed better than applying only one of the heuristics. However, running the two heuristics in the other order did not find a good feasible point. This implies that depending on the problem, the individual *Improve* methods can be considered as building blocks for more sophisticated *Improve* sequences that can produce a better point.

The running time of the ADMM and penalty CCP *Improve* methods was heavily affected when they were unable to find feasible points. This issue can be addressed by specifying the maximum number of iterations performed by the methods, or prematurely terminating the methods when they reach a preset time limit.

Table 2: Objective value of the best point found (left), and total running time (right) of the Suggest-and-Improve heuristic on the secondary user multicast beamforming problem.
