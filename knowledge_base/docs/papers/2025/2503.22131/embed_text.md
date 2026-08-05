<!-- arxiv-full-text:v1 {"arxiv_id": "2503.22131", "source": "arxiv-html"} -->

## Introduction

The development of techniques for solving Quadratic programming (QP) problems is a key enabler for advancing optimal control research, as efficiently solving these problems is often essential and a bottleneck in real-world optimal control applications. For example, Model Predictive Control (MPC), a framework for implementing optimal control, often relies on solving a series of QP problems. In addition, Sequential Convex Programming (SCP), a widely used algorithm for nonlinear optimal control, also relies on solving QP problems. Fast QP solvers are particularly beneficial in these applications, especially in scenarios requiring real-time implementation.

We consider the following QP problem, which includes additional set constraints and frequently arises in optimal control applications:\where $z_{ij} \in {\mathbb{R}}^{n_{z_{ij}}}$, $z_{i} = \left(z_{i1},z_{i2},\cdots,z_{im_{i}} \right) \in {\mathbb{R}}^{n_{z_{i}}}$, and $z = \left(z_{0},z_{1},\ldots,z_{N + 1} \right) \in {\mathbb{R}}^{n_{z}}$. Here, $z_{i}$ represents the combination of state and input variables at the $i$-th time point. The vector $z_{i}$ consists of $m_{i}$ components, where each component $z_{ij}$ has a quadratic weight $\rho_{ij} > 0$, The notations $\preceq$ and $\succeq$ denote element-wise inequalities for vectors. Vectors $q \in {\mathbb{R}}^{n_{z}}$, $g_{E} \in {\mathbb{R}}^{n_{E}}$, and $g_{I} \in {\mathbb{R}}^{n_{I}}$, as well as matrices $H_{E} \in {\mathbb{R}}^{n_{E} \times n_{z}}$ and $H_{I} \in {\mathbb{R}}^{n_{I} \times n_{z}}$, are constants. The function $\Phi_{ij}$ is a smooth vector-valued function on ${\mathbb{R}}^{n_{z_{ij}}}$, defining the convex set ${\mathbb{D}}_{ij}$ for additional constraints. We will later add requirements on $\Phi_{ij}$ to include commonly used sets, such as balls, second-order cones, boxes, and half-spaces.

Additionally, we require that both $H_{E}$ and $H_{I}$ follows the pattern below: where $A_{i}$ and $B_{i}$ are constant matrices. The number of columns of $A_{i}$ is $n_{z_{i}}$ and that of $B_{i}$ is $n_{z_{i + 1}}$. The number of rows for $A_{i}$ and $B_{i}$ are determined by the linear equality ${{H_{E}z} + g_{E}} = 0$ and the inequality ${{H_{I}z} + g_{I}} \geq 0$. We denote these numbers as $n_{E_{i}}$ for the equalities and $n_{I_{i}}$ for the inequalities in the $i$-th row of the block matrices $H_{E}$ and $H_{I}$, respectively.

The sparsity patterns of $H_{E}$ and $H_{I}$ are typical for optimal control optimization problems. These matrices define equality and inequality constraints among consecutive time points, while the set ${\mathbb{D}}_{ij}$ includes constraints for states and inputs at each time point.

There are a few differences between Problem 1 and general optimal control QP problems. First, our objective function requires strong convexity, and the quadratic term must be homogeneous with respect to the constraint ${\mathbb{D}}_{ij}$. Specifically, for dimensions of $z$ constrained by the same set ${\mathbb{D}}_{ij}$, the corresponding quadratic cost coefficients must be identical. Second, we restrict the set ${\mathbb{D}}_{ij}$ to specific families of convex sets. Possible relaxations of these requirements are discussed in Section 5.

Widely used methods for solving Problem 1 fall into two primary categories: second-order methods and operator-splitting methods, each with their own advantages and disadvantages. Second-order methods, such as interior-point methods and active-set methods, utilize the curvature information of the optimization problem. These methods typically converge in a modest number of iterations and are robust when the problem approaches infeasibility. Commonly used software in this category includes MOSEK, Gurobi, and ECOS. For further theoretical discussions on second-order methods, we refer the reader to.

One drawback of second-order methods lies in their high computational cost per iteration, as each step requires solving a linear system. This issue becomes significant as the dimension of the optimization variables increases. Additionally, while interior-point solvers are generally effective, they typically cannot directly handle Problem 1 in its original form and require the use of parsers, such as Yamlip or CVX, to transform the problem into a solver-compatible form. This transformation process adds overhead and increases the effort needed for verification, validation, and maintenance.

Another approach to solving Problem 1 is the operator-splitting method, which constructs an update operator applied at each iteration, ensuring that the iterations converge to the fixed point of this operator. Unlike interior-point methods, operator-splitting methods eliminate the need for matrix factorization, resulting in significantly lower per-iteration computational costs. Additionally, these methods do not require external parsers and are typically implemented with a smaller codebase. For a comprehensive review of operator-splitting methods, see. However, one drawback of operator-splitting methods is that they often require a large number of iterations to converge, especially when the problem is ill-conditioned.

Our main contribution is the development of Newton-PIPG, a hybrid method that integrates the Proportional-Integral Projected Gradient (PIPG) method, a representative operator-splitting approach, with the Newton method. This approach is motivated by the insight that finding a fixed point for the updating operator in operator-splitting methods is equivalent to solving a nonlinear fixed point equation. Given the Newton method's effectiveness in solving such equations, we design a Newton step for this fixed-point problem, with PIPG providing a warm start to ensure global convergence. Compared to second-order methods, Newton-PIPG reduces the need for matrix factorization and avoids the requirement for additional parsers. Additionally, in contrast to operator-splitting methods, the Newton step reduces the number of iterations required, enhancing both accuracy and speed.

We also provide theoretical guarantees for the Newton-PIPG method. Specifically, we demonstrate that under an extended linear independence constraint qualification and strict complementarity condition, the Newton step is well-defined, the associated matrix is nonsingular, and the Newton-PIPG algorithm enjoys global convergence with local quadratic convergence behavior.

Furthermore, we tailor our algorithm for optimal control problems. Recognizing that the most computationally expensive step is solving a large linear system in the Newton method, we exploit the sparsity inherent in optimal control problems to design an efficient factorization strategy, significantly reducing computation time.

### Related Work

Several studies have focused on integrating operator splitting methods with Newton-type methods. These approaches include directly using BFGS to solve the fixed-point equation from the proximal point method, and employing the ADMM method in conjunction with a semi-smooth Newton method, where linear systems are solved using GMRES. Other approaches involve hybridizing operator-splitting methods with quasi-Newton methods to balance global convergence and local acceleration. Popular choices for quasi-Newton methods include BFGS and Anderson acceleration.

The main difference between our work and others is that we focus on a specific type of optimal control QP problem. This focus provides several advantages for our method. First, we demonstrate that, under mild assumption, the update operator in PIPG is differentiable in a neighborhood of the solution. This suggests that the semi-smooth Newton method essentially acts as a Newton method, offering a quadratic convergence guarantee. Details of this differentiability are presented in Theorem 3.15.

Second, rather than using quasi-Newton methods or iterative solvers, we directly handle the linear system in the Newton step using an efficient matrix factorization technique. This approach leverages the sparsity pattern of the matrix, resulting in faster computation.

Third, our algorithm offers a stronger theoretical guarantee. We prove, rather than assume as in \[2, Assumption A6\], that the matrix involved in the Newton step is nonsingular in a local neighborhood of the solution under a generalized Linearly Independent Constraint Qualification (LICQ) assumption, which ensures the robustness of the algorithm. Moreover, our algorithm guarantees convergence even when certain key assumptions are not satisfied.

Beyond these distinctions, our method can also be viewed as an extension of existing Interior Point approaches, particularly the algorithm . The matrix factorization technique used in the Newton step is inspired by the blocked Cholesky decomposition method introduced . Other methods, such as, handle similar matrices with different linear algebra techniques but maintain the same computational complexity order for matrix factorization as. A key distinction between our approach and those in is our use of operator-splitting methods. This strategy not only ensures the applicability of our method to QPs with additional set constraints but also reduces the number of matrix factorizations required for convergence.

### Road Map

The structure of this paper is as follows. Section 2 reviews the PIPG method and the Newton method. Section 3 presents the Newton step for the PIPG operator, its theoretical properties, and an efficient factorization method for the matrix involved in the Newton step. Section 4 discusses the global and local convergence of the Newton-PIPG algorithm. Section 5 outlines the restrictions of our algorithm and possible relaxations. Section 6 provides implementation details, including the design of termination criteria, and presents numerical experiments comparing our method with other state-of-the-art QP solvers.

### Notation

We use the following notation throughout the paper. $\mathbb{R}$ denotes the set of real numbers, with ${\mathbb{R}}_{+}$ and ${\mathbb{R}}_{-}$ representing nonnegative and nonpositive real numbers, respectively. The set of $n \times m$ real matrices is ${\mathbb{R}}^{n \times m}$, and ${\mathbb{R}}^{n}$ denotes $n$-dimensional real vectors. The identity matrix is $I$, and the zero vector in ${\mathbb{R}}^{n}$ is $0^{n}$. Vectors are treated as columns, and we write $\left( v_{1},v_{2},\ldots,v_{n} \right)$ for a vertically stacked column vector when unambiguous. For the $i$-th element of a vector $v$, we use the notation ${v_{(i)} \in {\mathbb{R}}}.$ For the element on the $i$-th row and the $j$-th column of a matrix $M$, we denote it as $M_{(i,j)} \in {\mathbb{R}}$. We define vector inequalities as element-wise comparisons. For example, for vectors $a$ and $b$, $a \preceq b$ indicates that $a_{(i)} \leq b_{(i)}$ for all $i$, and $a \succeq b$ indicates that $a_{(i)} \geq b_{(i)}$ for all $i$. We use ${blkdiag}{(A_{1},A_{2},\cdots,A_{n})}$ to build a block diagonal matrix with $A_{1}$ to $A_{n}$ as the diagonal block matrices. $\parallel \cdot \parallel$ denotes the Euclidean norm for vectors and matrices. For a convex set $\mathbb{D}$, we denote $\Pi_{\mathbb{D}}{(z)}$ as the projection of $z$ onto set $\mathbb{D}$ and for $z \in {\mathbb{D}}$, we denote the normal cone of $\mathbb{D}$ at the point $z$ as $N_{\mathbb{D}}{(z)}$. For the definition of the normal cone, we refer to \[5, Chapter 2.1\]. For general closed set $\mathbb{D}$, we denote the distance of a point $z_{0}$ to $\mathbb{D}$ as ${d_{\mathbb{D}} = {\min{\{{\left. {\|{z - z_{0}}\|} \middle| z \right. \in {\mathbb{D}}}\}}}},$ and we use ${ri}{\mathbb{D}}$ as the relative interior of ${\mathbb{D}}.$ We denote ${\mathbb{D}}_{1} \times {\mathbb{D}}_{2}$ as the direct product of set ${\{{\mathbb{D}}_{1},{\mathbb{D}}_{2}\}},$ and $\prod_{i = 0}^{N}{\mathbb{D}}_{i}$ as the direct product of set $\{{\mathbb{D}}_{1},{\mathbb{D}}_{2},\cdots,{\mathbb{D}}_{N}\}$. We use the notation $o{(\epsilon)}$ to denote a function $f{(\epsilon)}$ that ${\lim_{\epsilon\rightarrow 0}\frac{f{(\epsilon)}}{\epsilon}} = 0$. We use $\lbrack 1,n\rbrack_{\mathbb{N}}$ for the integer set ${\{ 1,2,\cdots,n\}}.$ We denote ${span}{(v)}$ as the set of all linear combinations of the vectors in the set $v$.

## Background

To simplify the notation, we rewrite Problem 1 as follows\Here, the matrix $H$ is constructed by rearranging the rows of the matrix $H_{E}$ and $H_{I}$, resulting in the following form: In this formulation, the notation $(A_{i},B_{i})$ is reused to represent the block matrices that combine the original blocks from $H_{E}$ and $H_{I}$, corresponding to the equality and inequality constraint coefficients at the $i$-th time point. Setting $n_{i} = {n_{E_{i}} + n_{I_{i}}}$, the matrices $A_{i} \in {\mathbb{R}}^{n_{i} \times n_{z_{i}}}$ and $B_{i} \in {\mathbb{R}}^{n_{i} \times n_{z_{i + 1}}}$. The cone $\mathbb{K}$ is defined as $\prod_{i = 0}^{N}{({0^{n_{E_{i}}} \times {\mathbb{R}}_{+}^{n_{I_{i}}}})}$, and the vector $g$ is from vectors $g_{E}\text{~and~}g_{I}$, ensuring that ${{Hz} - g} \in {\mathbb{K}}$ enforces both ${{H_{E}z} + g_{E}} = 0$ and ${{H_{I}z} + g_{I}} \geq 0$. From now, $A_{i}$ and $B_{i}$ refer to the combined blocks in $H$.

The set $\mathbb{D}$ is defined as $\prod_{i = 0}^{N + 1}{\prod_{j = 0}^{m_{i}}{\mathbb{D}}_{ij}}$. The dual cone ${\mathbb{K}}^{\circ}$ is $\prod_{i = 0}^{N}{({{\mathbb{R}}^{n_{E_{i}}} \times {\mathbb{R}}_{-}^{n_{I_{i}}}})}$. The dimension of $\mathbb{K}$ is denoted by $n_{w} = {{\sum_{i = 0}^{N}n_{E_{i}}} + n_{I_{i}}}$.

### Proportional-Integral Projected Gradient

As discussed in the introduction, we propose a new method that combines the Proportional-Integral Projected Gradient (PIPG) method with the Newton method. In this section, we provide a brief overview of the PIPG method.

Developed, the PIPG algorithm's update rule for Problem 2 is defined as: | \(4\) | | | $z^{k + 1} = {\pi_{\mathbb{D}}\left\lbrack {z^{k} - {\alpha\left({{Pz^{k}} + q + {H^{\top}w^{k}}} \right)}} \right\rbrack}$ | | | | | | $w^{k + 1} = {\pi_{{\mathbb{K}}^{\circ}}\left\lbrack {w^{k} + {\beta\left({{H\left({{2z^{k + 1}} - z^{k}} \right)} - g} \right)}} \right\rbrack}$ | | where $\pi_{\mathbb{D}}:{{\mathbb{R}}^{n_{z}}\rightarrow{\mathbb{R}}^{n_{z}}}$ is the projection operator on to set ${\mathbb{D}},$ and $\pi_{{\mathbb{K}}^{\circ}}:{{\mathbb{R}}^{n_{w}}\rightarrow{\mathbb{R}}^{n_{w}}}$ is the projection operator on to set ${{\mathbb{K}}^{\circ} = {\prod_{i = 0}^{N}{{\mathbb{R}}^{n_{E_{i}}} \times {\mathbb{R}}_{-}^{n_{I_{i}}}}}}.$ We denote the operator $T:{{{\mathbb{R}}^{n_{z}} \times {\mathbb{R}}^{n_{w}}}\rightarrow{\mathbb{R}}^{n_{z} + n_{w}}}$ for the PIPG operator and express the PIPG update in as Let ${Fix}{(T)}$ denote the set of fixed points of operator $T$, that is, ${{Fix}{(T)}} = {\{{{(z,w)} \in {\mathbb{R}}^{n_{z} + n_{w}}}\mid{{(z,w)} = {T{(z,w)}}}\}}$. The following theorem for the convergence of the PIPG method is a direct consequence of Theorem 3.3, Theorem 4.3, and Theorem 4.4, discussed later in Section 4:

### Theorem 2.1

Suppose assumptions in Theorem 3.3 hold. Let $(z^{k},w^{k})$ be computed as, ${\alpha,\beta} > 0$ and ${{\alpha{\| P\|}} + {\alpha\beta{\| H\|}^{2}}} < 1$. If ${Fix}{(T)}$ is nonempty, the sequence $(z^{k},w^{k})$ will converge to a point ${(z^{\star},w^{\star})} \in {{Fix}{(T)}}$, and $z^{\star}$ is a solution of Problem 2.

For a fixed point ${(z^{\star},w^{\star})} \in {{Fix}{(T)}}$, we denote $z^{\star}$ as a primal solution and $w^{\star}$ as a dual solution to Problem 2. The pair $(z^{\star},w^{\star})$ will be referred to as a primal-dual solution pair to Problem 2. Notably, for a point ${(z^{\star},w^{\star})} \in {{Fix}{(T)}}$, we have Here the second equation is a consequence of the fact that ${N_{{\mathbb{K}}^{\circ}}{(w^{\star})}} \subset K$

### Newton Method

Theorem 2.1 indicates that PIPG solves a nonlinear fixed-point equation ${{(z^{\star},w^{\star})} - {T{(z^{\star},w^{\star})}}} = 0$. Consequently, we consider applying the Newton method directly to solve this equation, given its fast local convergence rate. In this section, we provide a brief review of the Newton method.

The Newton method is designed to solve where $R:{{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}^{n}}$ is a continuously differentiable function with a Jacobian matrix $J{(x)}$. At iteration $x_{k}$, a linear approximation for $R{(x_{k})}$ is ${{R{({x_{k} + p})}} \approx {{R{(x_{k})}} + {J{(x_{k})}p}}}.$ The Newton method chooses $p_{k}$ such that the linear approximation of $R$ equals zero, i.e., $p_{k} = {- {J{(x_{k})}^{- 1}R{(x_{k})}}}$. The next iteration $x_{k + 1}$ is defined as ${x_{k + 1} = {x_{k} + p_{k}}}.$ The Newton method is known for its locally quadratic convergence rate, but it also has three major disadvantages: the requirement of a nonsingular Jacobian matrix, the high computational cost of computing a factorization of the Jacobian matrix, and the lack of a global convergence guarantee. Additionally, in order to apply the Newton method to the fixed-point equation of $T$, we need to assess the differentiability of the operator $T$.

In the next section, we will define the Newton step for the PIPG operator $T$. We will show that the Jacobian of the PIPG exists and that the matrix appearing in the Newton step is invertible in the neighborhood of $T$'s fixed point under some mild assumptions. Hence, the linear equation in the Newton step has a local solution. Additionally, we will provide a factorization strategy for the Jacobian matrix that leverages its sparse structure. The global convergence result is deferred to Section 4.

## Newton Step for PIPG

We start with a formal definition of the Newton step for PIPG. Consider the case where both $\pi_{\mathbb{D}}$ and $\pi_{{\mathbb{K}}^{\circ}}$ are differentiable. In this case, the Jacobian of the PIPG operator can be computed using the chain rule: and $J_{\mathbb{D}}$ and $J_{{\mathbb{K}}^{\circ}}$ are the Jacobians of projections $\pi_{\mathbb{D}}$ and $\pi_{{\mathbb{K}}^{\circ}},$ evaluated at $z^{k} - {\alpha\left({{Pz^{k}} + q + {H^{\top}w^{k}}} \right)}$ and $w^{k} + {\beta\left({{H\left({{2z^{k + 1}} - z^{k}} \right)} - g} \right)}$ respectively.

If $\pi_{\mathbb{D}}$ and $\pi_{{\mathbb{K}}^{\circ}}$ are not differentiable or if $I - J_{T}$ is singular, we will simply set $J_{T}$ as a zero matrix of the same shape. We will later show that regardless of the choice of $J_{T}$, the global convergence of our algorithm will not be affected and, with mild assumptions, it will also not affect the local convergence rate. Also, note that projections are functions that are almost everywhere differentiable.

With $J_{T}$ being well-defined for all $(z,w)$, we have the definition of the Newton step

### Definition 3.1

The update rule for the Newton step is given by where $({\Delta z},{\Delta w})$ is the solution of the linear system Here, $J_{T}{(z^{k},w^{k})}$ is defined as in if $J_{\mathbb{D}}$ and $J_{{\mathbb{K}}^{\circ}}$ exist and $I - J_{T}$ is nonsingular; otherwise, we set $J_{T} = 0$.

### Extended Linearly Independent Constraint Qualification

In this section, we introduce the constraint qualification for our problem, which ensures the matrix in the Newton step is locally nonsingular. Such nonsingularity requires the fixed point set of the PIPG operator to be a single point. This, in turn, implies the uniqueness of both the primal and dual solutions: the strong convexity of Problem 1 guarantees a unique primal solution, while we need additional constraint qualifications to ensure the uniqueness of the dual solution.

The linearly independent constraint qualification (LICQ) is commonly used to ensure the uniqueness of the dual variable. However, LICQ is trivially violated for some important cases in Problem 1.

One example where LICQ fails is when ${\mathbb{D}}_{ij}$ is a second-order cone and the optimal solution $z_{ij} = 0$. Note that the second-order cone is defined as When $x = 0$, the gradient of ${\| x\|}^{2} - y$ is a zero vector, causing LICQ to automatically fail.

Another example is when ${\mathbb{D}}_{ij}$ is an affine subspace. According to our definition of ${\mathbb{D}}_{ij}$, an affine subspace is formed as For any point $z_{ij} \in {\mathbb{D}}_{ij}$, LICQ is automatically violated.

To include both types of set constraints in our discussion, we consider the following extended LICQ:

### Definition 3.2 (Extended-LICQ)

Problem 1 satisfies the extended Linearly Independent Constraint Qualification (extended-LICQ) if and the matrix $\lbrack H_{E}^{\top},H_{A_{I}}^{\top}\rbrack$ has full column rank. Here, ${range}{(\cdot)}$ denotes the column space of a matrix. Moreover, $z^{\star}$ is the optimal solution of Problem 1, and $H_{A_{I}}$ consists of rows from $H_{I}$ that activate (achieve equality) at $z^{\star}$.

The extended-LICQ, or its equivalent forms, are commonly used constraint qualifications for problems that involve second-order cones. For instance, the extended LICQ is equivalent to the second-order constraint qualification defined .

Now, we need to show that under extended-LICQ, all solutions to Problem 2 satisfy the Karush-Kuhn-Tucker (KKT) condition:

### Theorem 3.3

Under the extended-LICQ assumption, $z^{\star}$ is a solution to Problem 2 if and only if $z^{\star}$ is feasible for Problem 2 and there exists a dual variable $w^{\star} \in {\mathbb{K}}^{\circ}$ such that Moreover, if the solution $z^{\star}$ to Problem 2 exists, $(z^{\star},w^{\star})$ is unique.

### Proof 3.4

For the if part, by the definition of $N_{{\mathbb{K}}^{\circ}}$, ${{Hz^{\star}} - g} \in {N_{{\mathbb{K}}^{\circ}}{(w^{\star})}}$ is equivalent to Furthermore, ensures that, by \[5, Proposition 2.1.2\], $z^{\star}$ is a minimizer of the function where ${\mathbb{I}}_{\mathbb{D}}{(z^{\star})}$ is the indicator function of the set $\mathbb{D}$, taking the value $0$ if $z^{\star} \in {\mathbb{D}}$ and $+ \infty$ otherwise.

Since $w^{\star} \in {\mathbb{K}}^{\circ}$, $w^{\star \top}{({{Hz} - g})}$ is non-positive for all $z$ feasible to Problem 2, and thus for all feasible $z$. Thus, $z^{\star}$ is the solution to Problem 2.

For the only if part, \[8, Theorem 10.47\] ensures the existence of $w^{\star} \in {\mathbb{K}}^{\circ}$, $\eta = 0$ or $1$, and ${(w^{\star},\eta)} \neq 0$ such that The extended LICQ condition ensures that $\eta = 1$. Suppose instead that $\eta = 0$, then $w^{\star} \neq 0$. From Eq. 10, we have ${H^{\top}w^{\star}} \in {{range}{({\lbrack H_{E}^{\top},H_{A_{I}}^{\top}\rbrack})}}$, and the extended LICQ condition ensures that $\lbrack H_{E}^{\top},H_{A_{I}}^{\top}\rbrack$ has full rank, which implies ${H^{\top}w^{\star}} \neq 0$ for any $w^{\star} \neq 0$. However, also implies that ${H^{\top}w^{\star}} \in {{span}{({N_{\mathbb{D}}{(z^{\star})}})}}$, which contradicts the extended LICQ condition.

The uniqueness of $z^{\star}$ follows from the strong convexity of Problem 2. The uniqueness of $w^{\star}$ can be shown by contradiction. Suppose there exist $w_{1}^{\star}$ and $w_{2}^{\star}$ satisfying. Then, Hence, similar to the proof for the "only if" part, we have which contradicts the extended LICQ condition.

### Remark 3.5

In the proof of Theorem 3.3, the extended LICQ is not required for the "if" direction. Meanwhile, for any fixed point $(z^{\star},w^{\star})$ of the PIPG operator, we have ${- \left({{Pz^{\star}} + q + {H^{\top}w^{\star}}} \right)} \in {N_{\mathbb{D}}{(z^{\star})}}$, ${{H{(z^{\star})}} - g} \in {N_{{\mathbb{K}}^{\circ}}{(w^{\star})}}$, Therefore, Theorem 3.3 ensures that every fixed point $(z^{\star},w^{\star})$ of the PIPG operator is a solution to Problem 2, regardless of whether the extended LICQ holds.

### Properties of Projections to Convex Sets

In this section, we discuss the properties of projections onto convex sets. These properties are useful for subsequent proofs. To start, we discuss the eigenvalues of Jacobians of projection functions.

### Lemma 3.6

For a convex set $\mathbb{D}$ and a point $z$ outside $\mathbb{D}$, let $\pi{(z)}$ denote the projection of $z$ onto $\mathbb{D}$. If the Jacobian of this projection, denoted $J{(z)}$, exists and is symmetric, then the eigenvalues of $J{(z)}$ are real, non-negative, and do not exceed one.

### Proof 3.7

Since $J{(z)}$ is symmetric, all eigenvalues of $J{(z)}$ are real numbers.

Suppose that $\lambda$ is an eigenvalue of $J{(z)}$, and let $v$ be a corresponding eigenvector. We have Thus ${{\pi{({z + {\varepsilon v}})}} = {{\pi{(z)}} + {\lambda\varepsilon v} + {o{(\varepsilon)}}}}.$ Since ${{\pi{(z)}} \in {\mathbb{D}}},$ the definition of projection ensures that By the convexity of set $\mathbb{D}$, ${\langle{{\pi{({z + {\varepsilon v}})}} - {\pi{(z)}}},{z - {\pi{(z)}}}\rangle} \leq 0$(\[8, Proposition 7.4\]). We have Dividing $\varepsilon^{2}$ from both sides, Hence, $\lambda \geq 0$.

On the other hand, since projections are Lipschitz functions with Lipschitz constants equal to one \[8, Exercise 7.5\], all eigenvalues of $J{(z)}$ need to be less than or equal to one. Otherwise, we would have for some $\lambda$ and $v$, Then we have ${\|{{\pi{({z + {\varepsilon v}})}} - {\pi{(z)}}}\|} > {\|{\varepsilon v}\|}$ for $\varepsilon$ sufficiently small, violating the Lipschitz property of projections.

Lemma 3.6 requires $J{(z)}$ to be symmetric. This assumption holds for many types of convex sets. For example, projections onto points, boxes, balls, second-order cones, and half-spaces have symmetric Jacobians. These sets cover many applications in optimal control.

Next, we explore the smoothness of projections onto ${\mathbb{D}}_{ij}$. Based on Corollary $4.13$ in and Theorem $3.3$ , we have the following theorem.

### Theorem 3.8

Consider a point $z_{0}$ in a convex set where $\Phi_{i}:{{\mathbb{R}}^{n_{\mathbb{E}}}\rightarrow{\mathbb{R}}}$ are smooth convex functions. Denote ${{I_{\mathbb{E}}{(z_{0})}} = \left\{ k:{{\Phi_{k}{(z_{0})}} = 0} \right\}}.$ Assume that $\left\{ {{\nabla\Phi_{k}}\left(z_{0} \right)}:{k \in {I_{\mathbb{E}}{(z_{0})}}} \right\}$ is a linearly independent set or an empty set. For any normal vector $\overline{n}$ in $riN_{\mathbb{E}}{(z_{0})}$, there exists a sufficiently small open neighborhood $K$ of $z_{0} + \overline{n}$ such that the projection mapping $\pi_{\mathbb{E}}$ from $K$ to set $\mathbb{E}$ is a smooth function.

Let $\pi_{\mathbb{M}}$ be the projection function onto $\mathbb{M}$. It follows that for all points in $K$.

Based on Theorem 3.8, we have:

### Theorem 3.9

Consider the set $\mathbb{E}$, point $z_{0}$, vector $\overline{n}$, and neighborhood $K$ in Theorem 3.8. Under assumptions in Theorem 3.8, the projection $\pi_{\mathbb{E}}{(y)}$ is a smooth function for $y \in K$. The null space of the Jacobian of $\pi_{\mathbb{E}}{({z_{0} + \overline{n}})}$ is a subset of ${{span}N_{\mathbb{E}}}{(z_{0})}$, the set of all linear combinations of the vectors in the set $N_{\mathbb{E}}{(z_{0})}$.

### Proof 3.10

Set $y_{0} = {z_{0} + \overline{n}}$. If ${I_{\mathbb{E}}{(z_{0})}}:={\{ k\mid{{\Phi_{k}{(z_{0})}} = 0}\}}$ is empty, then $z_{0} \in {{int}{\mathbb{E}}}$ and thus $\overline{n} = 0$. Consequently, the Jacobian of the projection is the identity matrix, and the conclusion holds automatically.

When $I_{\mathbb{E}}{(z_{0})}$ is nonempty, without loss of generality, we assume that ${I_{\mathbb{E}}{(z_{0})}} = {\{ 1,\ldots,m\}}$, i.e., only the first $m$ inequalities defining $\mathbb{E}$ are satisfied as equalities at $z_{0}$.

For any $y \in K$, Theorem 3.8 ensures that ${\pi_{\mathbb{E}}{(y)}} = {\pi_{\mathbb{M}}{(y)}}$. Since ${\pi_{\mathbb{M}}{(y)}} = {{argmin}{\{{{{\frac{1}{2}{\|{\overline{y} - y}\|}^{2}} \mid \overline{y}} \in {\mathbb{M}}}\}}}$, the linear independence condition in Theorem 3.8 ensures the following KKT condition: there exists a dual variable ${\lambda{(y)}} = {(\lambda_{1},\cdots,\lambda_{m})} \in {\mathbb{R}}^{m}$ such that Denote the matrix $F{(y)}$ as According to the assumptions in Theorem 3.8, the columns of $F{(y_{0})}$ are linearly independent. Thus, $F{(y_{0})}$ has full column rank, and the number of rows in $F{(y_{0})}$ is not less than the number of columns. Therefore, we can choose $m$ rows of $F{(y)}$, denoted as $k_{1},k_{2},\ldots,k_{m}$, to form a matrix $\overset{\sim}{F}{(y)}$ such that $\overset{\sim}{F}{(y_{0})}$ is invertible.

As $\pi_{\mathbb{E}}$ is a smooth function locally, there exists an open neighborhood $\overset{\sim}{K} \subseteq K$ of $y_{0}$ such that for any $y \in \overset{\sim}{K}$, $\overset{\sim}{F}{(y)}$ is invertible. Therefore, implies that Using Cramer's rule, ${\overset{\sim}{F}}^{- 1}{(y)}$, and thus $\lambda{(y)}$, are smooth functions for $y \in \overset{\sim}{K}$. We then compute the Jacobian of evaluated at the point $y_{0}$, leading to where $J_{\mathbb{E}}{(y)}$ is the Jacobian of ${\pi_{\mathbb{E}}{(y)}}.$ In, $J_{\mathbb{E}},\lambda_{i}$ and $\nabla\lambda_{i}$ are evaluated at $y_{0}$, and $\nabla\Phi_{i}$ and $\nabla^{2}\Phi_{i}$ are evaluated at $z_{0}$.

Let $v$ be a vector in the null space of $J_{\mathbb{E}}{(y_{0})}$, i.e. ${J_{\mathbb{E}}{(y_{0})}v} = 0$. Multiplying both sides of by $v$, we obtain The last equality follows from the fact that ${N_{\mathbb{E}}{(z_{0})}} = {\{{\sum_{k}{\eta_{k}{\nabla\Phi_{k}}{(z_{0})}}}\mid{{\eta_{k} \geq 0},{k \in {I_{\mathbb{E}}{(z_{0})}}}}\}}$\[8, Thm. 10.39, Cor. 10.44, Thm. 10.45\].

Although Theorem 3.8 covers most sets of interest, it excludes projections onto second-order cones and affine subspaces, as both violate its assumptions. To incorporate these cases into our algorithm, we must ensure the smoothness guaranteed by Theorem 3.8 also holds. Projections onto affine subspaces are linear and explicitly computable via projection matrices, ensuring smoothness and the validity of Theorem 3.9. For second-order cones, smoothness is only an issue when the projection lands at the origin, leading to the following lemma.

### Lemma 3.11

Consider a second-order cone where $t \in {\mathbb{R}}_{+}$ is fixed. Then and ${{{span}N_{\mathbb{E}}}{}} = {\mathbb{R}}^{n_{x} + 1}$. For any $\overline{n} \in {{{ri}N_{\mathbb{E}}}{}}$, there exists an open neighborhood $K$ around $\overline{n}$ such that ${\pi_{\mathbb{E}}{(v)}} = 0$ for all $v \in K$, ensuring the smoothness of $\pi_{\mathbb{E}}$ in $K$.

### Proof 3.12

The form of the normal cones can be verified using the definition of normal cones to convex sets. Clearly, ${span}{({N_{\mathbb{E}}{}})}$ encompasses the entire space and ${{{ri}N_{\mathbb{E}}}{}} = {{int}{({N_{\mathbb{E}}{}})}}$. Moreover, if $\overline{n} \in {{int}{({N_{\mathbb{E}}{}})}}$, there exists a neighborhood $K$ such that for any $v$ in $K$, $v \in {N_{\mathbb{E}}{}}$ and ${\pi_{\mathbb{E}}{(v)}} = 0$, according to the properties of the normal cone.

### Nonsingularity of the Newton Step Matrix

In this section, we will show that the Newton step is well defined in a local neighborhood of $(z^{\star},w^{\star})$, i.e., $T$ is differentiable and $I - {J_{T}{(z^{k},w^{k})}}$ is invertible.

We start with the following lemma, which is also a major component of the algorithm. This lemma ensures that the linear system, which involves a nonsymmetric matrix, can be transformed into a symmetric linear system. We will later show that this symmetric linear system exhibits a desirable sparsity pattern.

### Lemma 3.13

Assume that $J_{\mathbb{D}}$ in is symmetric and has an eigenvalue decomposition $J_{\mathbb{D}} = {Q_{\mathbb{D}}\Lambda_{\mathbb{D}}Q_{\mathbb{D}}^{\top}}$. Then, the matrix ${I - \Lambda_{\mathbb{D}}} + {\alpha\Lambda_{\mathbb{D}}P}$ is invertible. Denote Solving is thus equivalent to solving The coefficients $\alpha$ and $\beta$ are from the PIPG operator.

### Proof 3.14

The invertibility of ${I - \Lambda_{\mathbb{D}}} + {\alpha\Lambda_{\mathbb{D}}P}$ is a direct consequence of Lemma 3.6 and the fact that $P$ is a diagonal matrix with positive diagonal elements.

We start by simplifying to show the second result. Using the definition of $J_{T}$, one can verify that on both sides of, we obtain the following equivalent Newton step: | | | | {- {2J_{{\mathbb{K}}^{\circ}}\beta H}} & I | | | | | | \end{bmatrix}{({I - {J_{T}{(z^{k},w^{k})}}})}\begin{pmatrix} | | | | | | {I - {J_{\mathbb{D}}{({I - {\alpha P}})}}} & {\alpha J_{\mathbb{D}}H^{\top}} \\ | | | | | | {- {J_{{\mathbb{K}}^{\circ}}\beta H}} & {I - J_{{\mathbb{K}}^{\circ}}} | | | | | | \end{bmatrix}\begin{pmatrix} | | | | | | {- {2J_{{\mathbb{K}}^{\circ}}\beta H}} & I | | | | | | \end{bmatrix}\left({{T{(z^{k},w^{k})}} - {(z^{k},w^{k})}} \right)}$ | | where ${\overset{\sim}{R}}_{z}^{k} \in {\mathbb{R}}^{n_{z}}$ and ${\overset{\sim}{R}}_{w}^{k} \in {\mathbb{R}}^{n_{w}}$.

Hence, solving 7 is equivalent to solving the following linear system: We solve this linear system by eliminating $\Delta z$ using the first row and obtaining an equation involving only $\Delta w$. To do so, we need the inverse of $I - {J_{\mathbb{D}}{({I - {\alpha P}})}}$. Noticing that the specific structure in Problem 1 ensures that ${Q_{\mathbb{D}}P} = {PQ_{\mathbb{D}}}$, we have Solving the first row of, we have Substituting this into the second row of, using, and applying the definitions of $W_{\mathbb{D}}$ and ${\overline{R}}_{w}^{k}$, we obtain Because of the specific form of ${\mathbb{K}}^{\circ}$, $J_{{\mathbb{K}}^{\circ}}$ is a diagonal matrix with only zeros and ones on the diagonal. Therefore, ${{({I - J_{{\mathbb{K}}^{\circ}}})}J_{{\mathbb{K}}^{\circ}}} = 0$, and we have Summing both equations, we have an equivalent linear equation Lemma 3.13 indicates that the nonsingularity of $I - J_{T}$ is equivalent to the nonsingularity of ${\overset{\sim}{W}}_{\mathbb{D}}$. To demonstrate the nonsingularity of the latter, we need to make a few assumptions.

The solution $z^{\star}$ of Problem 2 satisfies the extended LICQ condition. Moreover, in Problem 1, each set ${\mathbb{D}}_{ij}$ is either a second-order cone, an affine subspace, or satisfies the linear independence condition in Theorem 3.8 at all points.

The Jacobian of projections onto set $\mathbb{D}$, when it exists, is a symmetric matrix.

Since $\mathbb{D}$ is the direct product of sets ${\mathbb{D}}_{ij}$, Assumption 3.3 is satisfied if and only if the Jacobians of projections onto ${\mathbb{D}}_{ij}$ are symmetric. Many sets of interest in optimal control have this property, including balls, second-order cones, boxes, points, half-spaces, hyperplanes, affine spaces, and polytopes. This ensures the applicability of our algorithm to a wide range of problems.

To ensure the differentiability of the PIPG operator, we need the following assumption: \[Strict Complementarity\] For the fixed point $(z^{\star},w^{\star})$ of the PIPG operator, we require ${- \left({{Pz^{\star}} + q + {H^{\top}w^{\star}}} \right)} \in {{{ri}N_{\mathbb{D}}}{(z^{\star})}}$ ${{H{(z^{\star})}} - g} \in {{{ri}N_{{\mathbb{K}}^{\circ}}}{(w^{\star})}}$ Assumption 3.14 is closely related to the conventional strict complementarity condition \[15, Example 4.4\], which is usually required for a fast convergence rate in Newton-type methods \[26, Assumption 19.1\].

Additionally, Assumption 3.14 is generally satisfied in practice. When $(z^{\star},w^{\star})$ are fixed and the vectors $q$ and $g$ are sampled from a Gaussian distribution, Assumption 3.14 is violated only if $q$ lies on the relative boundary of the set ${N_{\mathbb{D}}{(z^{\star})}} + {Pz^{\star}} + {H^{\top}w^{\star}}$, or if $- g$ lies on the relative boundary of ${N_{{\mathbb{K}}^{\circ}}{(w^{\star})}} - {Hz^{\star}}$. The conditional probability of violating Assumption 3.14 for fixed $(z^{\star},w^{\star})$ is zero since the relative boundary has measure zero under the distributions of $q$ and $g$. Furthermore, integrating over all $(z^{\star},w^{\star})$ outcomes, the probability of violation remains zero. Of course, $q$ and $g$ may be generated by other types of mechanisms, and it is possible that Assumption 3.14 may be violated. In that case, our algorithm will still ensure convergence, though the theoretical convergence rate may not be quadratic.

We are now ready to introduce the theorem for the nonsingularity of ${I - {J_{T}{(z,w)}}}.$

### Theorem 3.15

Under Assumptions 3.3, 3.3, and 3.14, $I - {J_{T}{(z,w)}}$ is a smooth function of $(z,w)$ in a local neighborhood of $(z^{\star},w^{\star})$, the fixed point of the PIPG operator. Moreover, $I - {J_{T}{(z,w)}}$ is smooth for $(z,w)$ in that neighborhood.

### Proof 3.16

We start with the differentiability of $I - {J_{T}{(z,w)}}$. Utilizing the following fact \[28, Section 6\], and according to Theorem 3.8, Lemma 3.11, Assumption 3.3 and Assumption 3.14, it is ensured that $\pi_{\mathbb{D}}$ is a smooth function in a neighborhood of $z^{\star} - {\alpha{({{Pz^{\star}} + q + {H^{\top}w^{\star}}})}}$. Similarly, $\pi_{{\mathbb{K}}^{\circ}}$ is a smooth function in a neighborhood of $w^{\star} + {\beta{({{H{(z^{\star})}} - g})}}$. Hence, $I - {J_{T}{(z,w)}}$ is also a smooth function in a neighborhood of $(z^{\star},w^{\star})$.

Next, we move to the invertibility. According Lemma 3.13, $I - {J_{T}{(z^{\star},w^{\star})}}$ is invertible if and only if is invertible. Let $v$ be a vector such that ${{\overset{\sim}{W}}_{\mathbb{D}}v} = 0$. Since $J_{{\mathbb{K}}^{\circ}}$ is a diagonal matrix with zeros and ones on the diagonal, and is positive semi-definite, we have | | | $\Lambda_{\mathbb{D}}Q_{\mathbb{D}}^{\top}H^{\top}J_{{\mathbb{K}}^{\circ}}v$ | ${= 0}.$ | | Observe that the null space of $\Lambda_{\mathbb{D}}Q_{\mathbb{D}}$ coincides with the null space of $J_{\mathbb{D}}$. Additionally, $J_{\mathbb{D}}$ is a block diagonal matrix. The null space for each diagonal block is a subset of ${span}{({N_{{\mathbb{D}}_{ij}}{(z_{ij}^{\star})}})}$, as ensured by Assumption 3.3, Theorem 3.9 and Lemma 3.11. Hence, the null space of $J_{\mathbb{D}}$ is a subset of and ${H^{\top}J_{{\mathbb{K}}^{\circ}}v} \in {{span}{({N_{\mathbb{D}}{(z)}})}}$. Meanwhile, $H^{\top}J_{{\mathbb{K}}^{\circ}}$ shares the same column space with $\lbrack H_{E}^{\top},H_{A_{I}}^{\top}\rbrack$, where $H_{E}$ and $H_{A_{I}}$ are defined in the extended LICQ assumption. Hence, the extended LICQ ensures that ${J_{{\mathbb{K}}^{\circ}}v} = 0$. Since ${{({I - J_{{\mathbb{K}}^{\circ}}})}v} = 0$, it follows that $v = 0$ and thus $I - J_{T}$ is invertible at $(z^{\star},w^{\star})$. As $I - J_{T}$ is a smooth function of $(z,w)$ in a neighborhood of $(z^{\star},w^{\star})$, it remains invertible in some neighborhood of $(z^{\star},w^{\star})$.

### Remark 3.17

$I - J_{T}$ may not be invertible if the current iteration is not close to the primal-dual solution pair. For methods to handle the singular $I - J_{T}$, see Section 6. Importantly, this non-invertibility does not compromise the global convergence or the local convergence rate.

### Efficient Computation of Linear System in Newton Step

To efficiently factorize the invertible matrix we use an approach. This approach leverages the sparsity inherent in the optimal control problem, reducing computational costs to a linear function of the total number of time points $N$.

Since $Q_{\mathbb{D}}{({{I - \Lambda_{\mathbb{D}}} + {\Lambda_{\mathbb{D}}\alpha P}})}^{- 1}\Lambda_{\mathbb{D}}Q_{\mathbb{D}}$ is a block diagonal matrix, we can write it as: where $U_{i} \in {\mathbb{R}}^{n_{z_{i}} \times n_{z_{i}}}$. Hence, $W_{\mathbb{D}}$ will have the following pattern: where ${W_{i,i} \in {\mathbb{R}}^{n_{i} \times n_{i}}},$ $W_{i,{i + 1}} \in {\mathbb{R}}^{n_{i} \times n_{i + 1}}$, $W_{{i + 1},i} \in {\mathbb{R}}^{n_{i + 1} \times n_{i}}$ given that ${n_{i} = {n_{E_{i}} + n_{I_{i}}}}.$ Using the definition of $H$, we have Since $J_{{\mathbb{K}}^{\circ}}$ is a diagonal matrix with only zeros and ones on its diagonal, ${\overset{\sim}{W}}_{\mathbb{D}}$ will follow exactly the same pattern as $W_{\mathbb{D}}$. Denote $m_{k} = {\sum_{i = 0}^{k - 1}n_{i}}$ for $k = {\lbrack 1,N\rbrack}_{\mathbb{N}}$, $m_{0} = 0$, and $J_{{\mathbb{K}}_{i}^{\circ}} \in {\mathbb{R}}^{n_{i} \times n_{i}}$ being a diagonal matrix whose diagonal elements equal the $m_{i}$ to $m_{i + 1}$ elements of $J_{{\mathbb{K}}^{\circ}}$. Then we have Next, we compute the Cholesky decomposition ${\overset{\sim}{W}}_{\mathbb{D}} = {LL^{\top}}$ using the factorization technique, where $L$ is lower triangular. The Cholesky factor $L$ has a lower bidiagonal block structure. where ${L_{i,i} \in {\mathbb{R}}^{n_{i} \times n_{i}}},$ ${L_{{i + 1},i} \in {\mathbb{R}}^{n_{i + 1} \times n_{i}}}.$ Specifically, $L_{ii}$ are lower triangular matrices. Since ${LL^{\top}} = {\overset{\sim}{W}}_{\mathbb{D}}$, we have | \(28\) | | $L_{00}L_{00}^{\top}$ | $= {\overset{\sim}{W}}_{00}$ | | | | | $L_{i,i}L_{{i + 1},i}^{\top}$ | ${{= {\overset{\sim}{W}}_{i,{i + 1}}}\quad{i \in \left\lbrack 0,{N - 1} \right\rbrack_{\mathbb{N}}}},$ | | | | | $L_{i,i}L_{i,i}^{\top}$ | ${{= {{\overset{\sim}{W}}_{ii} - {L_{i,{i - 1}}L_{i,{i - 1}}^{\top}}}},{i \in \lbrack 1,N\rbrack_{\mathbb{N}}}}.$ | | To compute $L_{00}$, we employ the Cholesky decomposition on ${\overset{\sim}{W}}_{00}$. Subsequently, $L_{10}$ is determined through forward substitution from the equation ${L_{00}L_{10}^{\top}} = {\overset{\sim}{W}}_{01}$. Next, $L_{11}$ is obtained by performing Cholesky decomposition on the matrix ${\overset{\sim}{W}}_{11} - {L_{10}L_{10}^{\top}}$. This procedure is repeated iteratively to construct the entire $L$ matrix.

We summarize the procedure for computing the Newton step in Algorithm 1. It combines the insights from Lemma 3.13 with the Cholesky factorization. Details of implementations are left to Section 6.

3: Compute $\begin{pmatrix} \end{pmatrix} = {\begin{bmatrix} 5: Compute ${{\overline{R}}_{w}^{k} = {{J_{{\mathbb{K}}^{\circ}}\beta HV_{\mathbb{D}}{\overset{\sim}{R}}_{z}^{k}} + {\overset{\sim}{R}}_{w}^{k}}}.$ 6: Compute matrix ${\overset{\sim}{W}}_{\mathbb{D}}$ using Q𝔻 and Λ𝔻 7: Compute L for ${\overset{\sim}{W}}_{\mathbb{D}}$ using $${\Delta w} = {\left(L^{\top} \right)^{- 1}L^{- 1}{({I - {\alpha\beta^{2}J_{{\mathbb{K}}^{\circ}}W_{\mathbb{D}}\left({I - J_{{\mathbb{K}}^{\circ}}} \right)}})}{\overline{R}}_{w}^{k}}$$ 9: Compute ${\Delta z} = {V_{\mathbb{D}}\left({{\overset{\sim}{R}}_{z}^{k} - {\alpha J_{\mathbb{D}}H^{\top}\Delta w}} \right)}$ Algorithm 1 Newton step for PIPG

## Global Convergence for Newton-PIPG

In this section, we introduce the Newton-PIPG algorithm, a hybrid of the PIPG operator and the Newton step.

We define the residual of the PIPG operator as and we denote ${Fix}{(T)}$ the fixed point set of $T.$ Rather than employing the conventional Euclidean norm as the convergence criterion, we adopt an alternative norm: ${\| z\|}_{M}:=\sqrt{\langle z,{Mz}\rangle}$, where $M$ is a positive definite matrix expressed as The positive definiteness of $M$ is proved later in Lemma 4.1. The associated inner product with this matrix is given: and the norm $\parallel \cdot \parallel_{M}$ for a given matrix $A$ is defined as The norm $\parallel \cdot \parallel_{M}$ is intrinsic to the proof of PIPG's convergence, rendering it a convenient choice for establishing convergence for the Newton-PIPG algorithm. Due to the equivalence among norms on finite-dimension problems, the convergence in $\parallel \cdot \parallel_{M}$ is equivalent to that in the Euclidean norm.

In order to ensure the convergence of the Newton method, we design Algorithm 2 that combines the PIPG with the Newton step, inspired . In this algorithm, the PIPG algorithm will be a safeguard to ensure global convergence, while the Newton step will be used to accelerate PIPG locally.

1: Require c ∈ [0, 1), e ≥ 0, t > 0, Initial iteration (z0, w0) 3: while termination criteria not satisfied do 4: Compute an update pk = (Δzk, Δwk) either be zero or from the Newton step Algorithm 2 provides flexibility in choosing the update $p^{k}$ while ensuring global convergence, as demonstrated in Theorem 4.3. In practice, $p^{k}$ can be set to zero or to the solution of the Newton step. When $p^{k}$ is zero, the Newton update is disabled. To achieve fast computation, we periodically activate the Newton step instead of using it at each iteration. Details on selecting $p^{k}$ are available in Section 6.

The termination criteria for Algorithm 2 is discussed in Section 6.2. The coefficient $\sigma$ in Algorithm 2 is a safeguard ensuring that the Newton update does not move $(z^{k},w^{k})$ to a point far away from the current iteration. The use of such a coefficient $\sigma$ is inspired .

### Convergence Analysis of Newton-PIPG

First, we show the positive definiteness of $M$.

### Lemma 4.1

Assuming ${\alpha,\beta} > 0$, and ${\alpha{({{\| P\|} + {\beta{\| H\|}^{2}}})}} < 1$, $M$ is a positive definite matrix.

### Proof 4.2

Consider any vector ${v = \left\lbrack \begin{array}{l} \end{array} \right\rbrack},$ where $v_{1} \in {\mathbb{R}}^{n_{z}}$ and ${v_{2} \in {\mathbb{R}}^{n_{x}{({N + 1})}}}.$ We have according to the assumption ${\alpha,\beta} > 0$ and ${\alpha{({{\| P\|} + {\beta{\| H\|}^{2}}})}} < 1$. The equality holds only when ${v = 0}.$ To simplify the notation, we set ${{\overset{\sim}{z}}^{k} = {(z^{k},w^{k})}},{{T\overset{\sim}{z}} = {T{(z,w)}}}$ and ${{R\overset{\sim}{z}} = {R{(z,w)}}}.$ The following theorem, taken from \[37, Lemma 2\], indicates a key property for the PIPG operator.

### Theorem 4.3

Under the assumption in Lemma 4.1, for the PIPG operator $T,$ there exists a non-expansive operator $\overset{\sim}{T}$, i.e. ${\|{{\overset{\sim}{T}x} - {\overset{\sim}{T}y}}\|}_{M} \leq {\|{x - y}\|}_{M}$, such that $T = {{\frac{1}{2}I} + {\frac{1}{2}\overset{\sim}{T}}}$.

We present the following theorem, which is a standard result concerning the convergence of algorithms based on nonexpansive operators. The proof, originally from \[4, Theorem 5.14\], is included here for completeness.

### Theorem 4.4

Suppose that $T$ satisfies $T = {{\lambda I} + {{({1 - \lambda})}\overset{\sim}{T}}}$, where $\overset{\sim}{T}$ is nonexpansive, i.e. ${\|{{\overset{\sim}{T}x} - {\overset{\sim}{T}y}}\|}_{M} \leq {\|{x - y}\|}_{M}$. Considering an algorithm that ${\overset{\sim}{z}}^{k + 1} = {T{\overset{\sim}{z}}^{k}}$. Then, the operator $R = {I - T}$ is continuous, and ${\|{R{\overset{\sim}{z}}^{k}}\|}_{M}$ is decreasing. Furthermore, if the fixed point set of $T$ is nonempty, the following hold: ${\|{{\overset{\sim}{z}}^{k + 1} - y}\|}_{M}^{2} \leq {{\|{{\overset{\sim}{z}}^{k} - y}\|}_{M}^{2} - {\lambda\left({1 - \lambda} \right){\|{R{\overset{\sim}{z}}^{k}}\|}_{M}^{2}}}$ for any $y \in {{Fix}{(T)}}$ ${\|{R{\overset{\sim}{z}}^{k}}\|}_{M}$ converges to zero. ${\overset{\sim}{z}}^{k}$ will converge to a fixed point of $T.$

### Proof 4.5

We start with some facts related to $T$ and $\overset{\sim}{T}$. Firstly, $T$ is nonexpansive as Secondly, $y \in {{Fix}{(T)}}$ if and only if ${y \in {{Fix}{(\overset{\sim}{T})}}}.$ This is proved by plugging $y$ into $T = {{\lambda I} + {{({1 - \lambda})}\overset{\sim}{T}}}$.

For the first conclusion, we know that, by the convexity of norm function, Therefore, $R$ is a Lipschitz continuous operator.

Meanwhile, since $T$ is nonexpansive, This proves the second half of the conclusion.

Now we work on the other conclusions. For arbitrary $y$, We can expand and simplify this equation: Here, we have used the fact that If ${Fix}{(T)}$ is nonempty, we plug in arbitrary $y$ from this fixed point set. Since $y \in {{Fix}{(\overset{\sim}{T})}}$ as well, we have A summation of both sides of this inequality for all iterations will show that ${\|{R{\overset{\sim}{z}}^{k}}\|}^{2}$ is summable and thus it will converge to zero. At the meantime $\left\| {{\overset{\sim}{z}}^{k} - y} \right\|_{M}^{2}$ is decreasing in $k$ and thus ${\overset{\sim}{z}}^{k}$ is bounded. We can therefore find a subsequence ${\overset{\sim}{z}}^{k_{i}}$ converging to a point ${\overset{\sim}{z}}^{\star}$ by compactness. As ${\|{R{\overset{\sim}{z}}^{k_{i}}}\|}_{M}$ convergence to zero and $R$ is continuous, we have that ${T{\overset{\sim}{z}}^{\star}} = {\overset{\sim}{z}}^{\star}$. Since ${\overset{\sim}{z}}^{\star}$ is a fixed point, we plug in ${\overset{\sim}{z}}^{\star}$ in the place of $y$ and get $\left\| {{\overset{\sim}{z}}^{k + 1} - {\overset{\sim}{z}}^{\star}} \right\|_{M}^{2} \leq \left\| {{\overset{\sim}{z}}^{k} - {\overset{\sim}{z}}^{\star}} \right\|_{M}^{2}$ for all $k$, and ${\lim_{i}\left\| {{\overset{\sim}{z}}^{k_{i}} - {\overset{\sim}{z}}^{\star}} \right\|_{M}^{2}} = 0$. Thus ${\lim_{n}{\overset{\sim}{z}}^{k}} = {\overset{\sim}{z}}^{\star}$ We now proceed to establish the convergence of Newton-PIPG and start with the local convergence result.

### Theorem 4.6

With Assumptions 3.3, 3.3, and 3.14, consider the unique fixed point ${\overset{\sim}{z}}^{\star}$ of the operator $T$. There exists a neighborhood $K$ of ${\overset{\sim}{z}}^{\star}$ such that ${{\nabla R}{(\overset{\sim}{z})}} = {I - {J_{T}{(\overset{\sim}{z})}}}$ for any $\overset{\sim}{z} \in K$. Consider vector $p$ for $\overset{\sim}{z} \in K$ and There exist constants $C_{0}$ and $C_{1}$ such that

### Proof 4.7

According to Theorem 3.15, there exists a compact neighborhood $K$ such that ${{\nabla R}{(\overset{\sim}{z})}} = {I - J_{T}}$ exists and is invertible. Within this neighborhood, ${\nabla R}{(\overset{\sim}{z})}$ is a smooth function and hence a $\gamma$-Lipschitz function for some constant $\gamma > 0$ with respect to the norm $\parallel \cdot \parallel_{M}$. The invertibility and smoothness of $\nabla R$ ensure that there exist constants $\mu > 0$ such that for any vector $\xi \in {\mathbb{R}}^{n_{z} + n_{w}}$ and any $\overset{\sim}{z} \in K$, we have Then for any $\overset{\sim}{z} \in K$ and $p \in {\mathbb{R}}^{n_{z} + n_{w}}$ such that ${{\nabla R}{(\overset{\sim}{z})}p} = {- {R{(\overset{\sim}{z})}}}$, we have where the last inequality is a consequence of ${{\|{R{(z)}}\|}_{M} = {\|{{\nabla R}{(\overset{\sim}{z})}p}\|}_{M} \geqslant {\mu{\| p\|}_{M}}}.$ Therefore, Eq. 30 is satisfied with ${C_{0} = {{\gamma/2}\mu^{2}}}.$ Next, we show the validity of. Setting $\eta = {\overset{\sim}{z} - {\overset{\sim}{z}}^{\star}}$ and using that ${R{({\overset{\sim}{z}}^{\star})}} = 0$, we have Using $\eta = {\overset{\sim}{z} - {\overset{\sim}{z}}^{\star}}$, we have which proves equality. Here, the second inequality follows, while the last inequality is a result of the Lipschitz continuity of ${\nabla R}{(\overset{\sim}{z})}$.

Now we prove the global convergence of Newton-PIPG:

### Theorem 4.8

Suppose the conditions of Lemma 4.1 hold and ${Fix}{(T)}$ is non-empty. If the algorithm runs indefinitely, disregarding the termination criteria in line 3 of Algorithm 2, the following properties hold: ${R{\overset{\sim}{z}}^{k}}\rightarrow 0$.

Given Assumptions 3.3, 3.3, and 3.14, if $\sigma$ is sufficiently large and $p_{k}$ is computed using for each iteration unless $I - J_{T}$ is singular, Newton-PIPG converges to the unique fixed point ${\overset{\sim}{z}}^{\star}$ of $T$, with a quadratic local convergence rate.

### Proof 4.9

For the first result, consider a proof by contradiction. Given Theorem 4.4 and the restriction on the Newton step, ${\|{R{\overset{\sim}{z}}^{k}}\|}_{M}$ is monotonically decreasing. If $R{\overset{\sim}{z}}^{k}$ doesn't converge to zero, it implies that the Newton step is eventually disabled, leading us to the same algorithm as described in Theorem 4.4. The convergence results from Theorem 4.3 and Theorem 4.4 then imply a contradiction. Hence, ${R{\overset{\sim}{z}}^{k}}\rightarrow 0$.

For the second result, let ${\overset{\sim}{z}}^{\star}$ be the unique fixed point of the PIPG operator. The uniqueness of the fixed point is guaranteed by extended-LICQ and the strong convexity of Problem 1. To start, we aim to show that ${\|{{\overset{\sim}{z}}^{k} - {\overset{\sim}{z}}^{\star}}\|}_{M}$ is bounded.

In the $k$-th iteration, if the PIPG update is used, then as per Theorem 4.4. If the Newton update is accepted, the criteria in line 5 of Algorithm 2 ensures that Here, $q_{k}$ is the number of times the Newton step has been activated since the first iteration. Coefficients $c$ and $\sigma$ are defined in Algorithm 2.

Summing over $k$, we obtain Given that $c < 1$, we infer that ${\overset{\sim}{z}}^{k}$ is bounded.

According to Theorem 4.6, there exists a neighborhood $K$ such that equations and hold. Therefore, we can find an $M$-norm ball $K' \subset K$ such that for any $\overset{\sim}{z} \in K'$ and vector $p$ such that ${{\nabla R}{(\overset{\sim}{z})}p_{k}} = {- {R{(\overset{\sim}{z})}}}$, we have where $c$ is defined in Algorithm 2. Hence, for any ${\overset{\sim}{z}}^{k} \in K'$, we have ${{\overset{\sim}{z}}^{k} + p_{k}} \in K'$.

Therefore, if $\sigma$ is sufficiently large, specifically $\sigma \geq {\sup_{z \in K}{\|{\nabla R^{- 1}}\|}_{M}}$, we will have ${\| p_{k}\|}_{M} \leq {\sigma{\|{R{({\overset{\sim}{z}}^{k})}}\|}_{M}}$ for all ${\overset{\sim}{z}}^{k} \in K$.

By the compactness of ${\overset{\sim}{z}}^{k}$, the continuity of $R$, and that ${R{\overset{\sim}{z}}^{k}}\rightarrow 0$, there exists a converging subsequence of ${\overset{\sim}{z}}^{k}$ that converges to the unique fixed point ${\overset{\sim}{z}}^{\star}$. Then, when ${\overset{\sim}{z}}^{k} \in K'$, the Newton step will be accepted as it leads to a sufficient amount of decrease in $R{({\overset{\sim}{z}}^{k})}$, and ${\| p_{k}\|}_{M} \leq {\sigma{\|{R{({\overset{\sim}{z}}^{k})}}\|}_{M}}$. Further, ${\overset{\sim}{z}}^{k + 1} \in K'$, ensuring that the PIPG will not be activated again. In that case, in Theorem 4.6 ensures a quadratic convergence rate.

### Remark 4.10

The quadratic convergence result in Theorem 4.8 can be further strengthened to convergence within finite iterations if $J_{\mathbb{D}}$ and $J_{{\mathbb{K}}^{\circ}}$ are piecewise constant functions. This scenario occurs when $J_{\mathbb{D}}$ consists of boxes, halfspaces, and affine subspaces. In these cases, $J_{T}$ will also be a piecewise constant function of the primal and dual variables. Within a local neighborhood of the fixed point $(z^{\star},w^{\star})$, the PIPG operator will be a linear function, allowing the Newton step to find the fixed point within one iteration.

### Remark 4.11

The proof method in Theorem 4.8 is inspired . The difference between the proof in Theorem 4.8 and the convergence analysis in is that we establish convergence for a hybrid approach combining the Newton method, instead of the quasi-Newton method, with the operator splitting method, thus achieving a better convergence rate. Furthermore, the invertibility of $I - J_{T}$ guarantees the existence of the coefficient $\sigma$ in our proof (corresponding to $D$ in \[33, Assumption 2\]), eliminating the requirement of \[33, Assumption 2\], which is not commonly used in optimization research.

## Restrictions and Relaxation

In this section, we point out several restrictions in Problem 2 compared to general optimal control quadratic programming problems, and we discuss the possibility of relaxing such restrictions.

In Problem 2, we require $P$ to be a diagonal matrix with positive diagonal elements. This requirement ensures the invertibility of ${I - J_{\mathbb{D}}} + {\alpha J_{\mathbb{D}}P}$, which is necessary for the linear algebra technique outlined in Lemma 3.13. Although this choice of $P$ is suitable for many optimal control problems, it does not encompass all scenarios. In particular, it does not cover QPs arising in the sequential convexification of nonconvex optimal control problems that utilize the $L_{1}$-exact penalty. When applying the $L_{1}$ exact penalty, transforming the linearized subproblems into QP form requires the introduction of slack variables. Consequently, the resulting QP no longer has a positive definite quadratic term; the quadratic matrix contains zeros on the diagonal for positions that correspond to these slack variables. To address this issue, we propose adding an additional squared $L_{2}$-norm to the penalty. This modification not only maintains the exactness but also ensures our algorithm's compatibility with the subproblems from the sequential convexification.

Besides the form of $P$, we also require $J_{\mathbb{D}} = J_{\mathbb{D}}^{\top}$, ${Q_{\mathbb{D}}P} = {PQ_{\mathbb{D}}}$, and ${\mathbb{K}} = {\prod_{i = 0}^{N}{({0^{n_{E_{i}}} \times {\mathbb{R}}_{+}^{n_{I_{i}}}})}}$. Generalizing these constraints introduces several challenges. If $J_{\mathbb{D}}$ is not symmetric or ${Q_{\mathbb{D}}P} \neq {PQ_{\mathbb{D}}}$, the relationship $\left( {I - {J_{\mathbb{D}}{({I - {\alpha P}})}}} \right)^{- 1} = V_{\mathbb{D}}$ in Lemma 3.13 will no longer hold. Furthermore, if we generalize $\mathbb{K}$ to a general cone, ${J_{{\mathbb{K}}^{\circ}}{({I - J_{{\mathbb{K}}^{\circ}}})}} = 0$ will not be satisfied. In either case, the linear matrix appearing in the Newton step will not be symmetric. Consequently, the Cholesky decomposition will not be applicable, and the proof for the nonsingularity of $I - J_{T}$ will be invalid.

If generalization is necessary, one can directly compute the factorization for $I - J_{T}$ at some Newton steps and use iterative methods such as GMRES for other Newton steps. In this approach, previous factorizations can be used as preconditioners for subsequent iterations.

## Implementation and Numerical Experiments

We demonstrate the implementation details of the Newton-PIPG algorithm and compare its performance with other state-of-the-art solvers.

### Implementation Details for Newton-PIPG

Algorithm 2 provides a framework for the Newton-PIPG algorithm, allowing flexibility in choosing the form of $p^{k}$. This flexibility leads to different strategies for implementing the Newton-PIPG algorithm. Here are some strategies we use to optimize computation speed.

First, we reduce the use of Newton steps by applying them only when PIPG iterations stagnate. A heuristic waiting period, typically 3-10 PIPG iterations, is employed. If both $J_{{\mathbb{K}}^{\circ}}$ and the active manifold of $\pi_{\mathbb{D}}$ remain unchanged during this period, the algorithm switches to the Newton step.

Second, after each computationally intensive Newton step, a line search is performed to monitor the reduction in the PIPG residual $R{(z^{k},w^{k})}$. This line search, typically executed 3-5 times per Newton step, improves practical convergence speed without affecting the convergence properties of the Newton-PIPG algorithm. The line search result that reduces the residual norm by a factor of $c$, as defined in Algorithm 2, is accepted. The coefficient $c$ is generally close to 1; for instance, we use $c = 0.99$. If the line search fails to sufficiently reduce the residual, the result is discarded, and a PIPG update is performed instead. Moreover, in the case of a failed line search, the waiting period is extended until either $J_{{\mathbb{K}}^{\circ}}$ or the active manifold of $\pi_{\mathbb{D}}$ is updated.

Third, to improve the conditioning of the optimization problem, we rescale the matrix $H$ so that the norm of each row is of the same magnitude. This rescaling does not affect the optimal solution. For a detailed discussion, we refer interested readers to.

Fourth, $I - J_{T}$ can become singular when the current iteration is not in a local neighborhood of the primal-dual solution pair $(z^{\star},w^{\star})$. To obtain useful results from the Newton step, we add an additional perturbation to the matrix $I - J_{T}$. The perturbation we choose is an identity matrix multiplied by a coefficient proportional to the norm of the residual $R{(z^{k},w^{k})}$, so that the perturbation becomes negligible when the current iteration is close to $(z^{\star},w^{\star})$.

Fifth, we monitor the convergence of the residual using the Euclidean norm instead of $\parallel \cdot \parallel_{M}$, as the Euclidean norm is more efficient to compute. In our experiments, using the Euclidean norm did not compromise the algorithm's convergence. However, in situations where it might, one may consider using $\parallel \cdot \parallel_{M}$ to validate the Newton step for a more robust implementation.

Finally, we optimize the matrix-vector multiplication by partitioning the sparse matrix $H$ into zero blocks and dense, nonzero blocks. Instead of performing sparse matrix multiplication, we treat $H$ as a collection of dense block matrices. Using for-loops, we compute the matrix-vector product as a series of dense matrix-vector multiplications. This approach is also applied when computing the factorization in the Newton step. A similar method is used .

### Termination Criteria

In this section, we propose the termination criteria for both PIPG and Newton-PIPG. We claim that monitoring the magnitude of ${\|{R{(z^{k},w^{k})}}\|} = {\|{{(z^{k + 1},w^{k + 1})} - {(z^{k},w^{k})}}\|}$ provides a good criterion for stopping the PIPG algorithm. Here, $(z^{k},w^{k})$ and $(z^{k + 1},w^{k + 1})$ are consecutive PIPG iterations. Since Newton-PIPG requires iteratively calling the PIPG operator, we can use the same termination criteria for the Newton-PIPG algorithm as well.

To start, we show that $\|{{(z^{k + 1},w^{k + 1})} - {(z^{k},w^{k})}}\|$ is a good indicator of the quality of $(z^{k + 1},w^{k + 1})$ in terms of the KKT condition in Theorem 3.3. Specifically, we set ${\Delta z} = {z^{k + 1} - z^{k}}$ and ${\Delta w} = {w^{k + 1} - w^{k}}$ and show that:

### Theorem 6.1

When both ${\|{\Delta z}\|} \leq \epsilon$ and ${\|{\Delta w}\|} \leq \epsilon$ for $\epsilon > 0$, we have the following relationship:

### Proof 6.2

The PIPG iterations trivially guarantees $z^{k + 1} \in {{\mathbb{D}}andw^{k + 1}} \in {\mathbb{K}}^{\circ}$. The PIPG iteration ensures that Using properties of projections to a convex set, we obtain Using the fact that ${\|{\Delta z}\|} \leq \epsilon$ and ${\|{\Delta w}\|} \leq \epsilon$, we achieve Setting $\gamma_{p} = {\frac{1}{\alpha} + {\| P\|} + {\| H^{\top}\|}}$ and $\gamma_{d} = {\frac{1}{\beta} + {\| H\|}}$, Theorem 6.1 indicates that $\gamma_{p}{\|{\Delta z}\|}$ and $\gamma_{d}{\|{\Delta w}\|}$ measure the KKT satisfaction for the current iteration $(z^{k},w^{k})$. Hence, we propose the following termination condition for both PIPG and Newton-PIPG: given an absolute tolerance $\epsilon_{abs}$ and a relative accuracy tolerance $\epsilon_{rel}$, the algorithm will be terminated if

### Numerical Experiment Introduction

We test the performance of the Newton-PIPG algorithm via two example problems. The first example is an oscillating masses problem that involves only linear constraints. The second example is a powered-descent guidance problem that includes various types of constraints, such as linear inequality, ball constraints and second-order cones. We compare the results against benchmark algorithms such as ECOS and OSQP, among others.

The numerical experiment is conducted using MATLAB. The Newton-PIPG code was initially written in MATLAB and then converted into executable C code using MATLAB Coder. The computational experiments were carried out on a computer equipped with an AMD Ryzen 7 5700G 8-Core CPU and 16GB of RAM. The results here are generated with code : github.com/UW-ACL/NEWTON-PIPG-for-QP-Problems.

### Oscillating Masses

We use a benchmark oscillating masses problem to evaluate the performance of our algorithm in comparison to other state-of-the-art algorithms. Consider a mechanical system comprising $m = 16$ masses connected in a one-dimensional line, shown in figure 1. Each mass is defined by its 1-D velocity and position, resulting in a total of $n_{x} = 16$ state variables. To control this mechanical system, we assign one control variable to each mass. Hence the dimension of control at each time point is ${n_{u} = 8}.$ Time is discretized using a step size of $\Delta$. The total number of time points is denoted by N, and we set ${\Delta = {3/N}},$ i.e. this equation describes a system among $\lbrack 0,3\rbrack$. In our experiment, we set $N = {20,50,100}$ to show the scalability of our algorithm.

Figure 1: The oscillating masses system After discretization, we have the following optimization problem: Here, the matrices $P$ and $Q$ are identity matrices and matrices $A$ and $B$ are defined as where the matrix ${\mathbb{L}} \in {\mathbb{R}}^{m \times m}$ is a tridiagonal matrix with 2's on the diagonal and -1's on the subdiagonal and superdiagonal entries.

The initial conditions ${\hat{x}}_{0}$ are randomly generated. In our experiments, we set $x_{\text{min}} = {- 1}$ and $x_{\text{max}} = 1$. The initial condition is generated from a normal distribution with mean zero and a standard deviation of 0.3 then projected to $\lbrack x_{\text{min}},x_{\text{max}}\rbrack$. This ensures that the values of $x$ are spread within the range of $\lbrack{- 1},1\rbrack$, without too many values equal to -1 or 1.

In our numerical experiments, we compared our algorithm with several prominent solvers: OSQP, SCS, SCS-Anderson, PIPG, and ECOS, using their respective MATLAB packages. OSQP and SCS are ADMM-based methods. SCS-Anderson represents methods that combine operator-splitting operators with quasi-Newton methods. Lastly, ECOS stands as an example of an interior-point method.

Since our current algorithm does not have feasibility detection capacity, we only consider problems with feasible solutions. In practice, we run OSQP and SCS before the Newton-PIPG and Newton-PIPG will only be used to solve problems that are characterized as feasible by both OSQP and SCS.

For our numerical experiments, we set the tolerance level of all competing solvers to $10^{- 8}$ in their respective software settings, and for PIPG we set ${\epsilon_{abs} = 10^{- 8}},$ and $\epsilon_{rel} = 0$. The Newton-PIPG algorithm does not require a specific termination criterion, as it converges within a finite number of iterations when the optimization problem is linear. Post-computation, we measure and report the difference between each solver's solution and that of Newton-PIPG using the $L_{2}$ norm.

We set ${(u_{\text{min}},u_{\text{max}})} \in {\{{({- 1},1)},{({- 0.4},0.4)}\}}$ and then randomly generate 100 initial conditions for each combination of $N$ and $(u_{\text{min}},u_{\text{max}})$. The average time consumption is shown in Table 1, measured in milliseconds. In this table, the SCS-And refers to the SCS-Anderson algorithm, while the N-PIPG denotes the Newton-PIPG. These time consumption are reported by the Matlab package of each solver. When the maximum control magnitude is set to 1, we observed that all randomly generated problems are feasible. When the control magnitude is set to 0.4, approximately 95% of the randomly generated problems are feasible, and we only apply the Newton-PIPG algorithm to these problems.

When set to ${(u_{\text{min}},u_{\text{max}})} = {({- 1},1)}$ and $N = 20$, our algorithm outperforms others by a factor of five. Such a ratio persists with larger problem sizes. With respect to the post-computation error tolerance, ECOS attains $10^{- 5}$ in $L_{2}$ norm in all cases. At ${N = 20},$ all other solver achieves $10^{- 8}$ in accuracy. At $N = 50$ and $N = 100$, algorithms other than PIPG and ECOS achieve accuracy of $10^{- 6}$. PIPG reaches the target accuracy for all cases.

The Newton-PIPG algorithm achieves rapid QP solution primarily because the PIPG step rapidly identifies the correct active constraints of $\mathbb{D}$ in situations where the constraints are not tight. Thus, it usually requires a single Newton step and a small number of PIPG steps to solve the problem. To evaluate scenarios where more Newton steps are needed, we set ${(u_{\text{min}},u_{\text{max}})} = {({- 0.4},0.4)}$. With more inequality constraints activated, more Newton steps are expected. As predicted, Newton-PIPG slows down but is still 30% faster than the best of the other algorithms.

We also compare Newton-PIPG with SCS-Anderson, as both methods hybridize operator-splitting and second-order approaches. SCS-Anderson does speed up SCS, but the increase is limited. However, adding the Newton step to PIPG dramatically improves its speed, both at $u = 1$ and $u = 0.4$. This indicates that the Newton step has better performance compared to quasi-Newton methods.

We presented a typical plot (Figure 2) comparing the computation time between the Newton-PIPG method and the PIPG method. The plot tracks the computation time and the norm of the residual after each PIPG and Newton step, with $N = 20$ and ${(u_{\text{min}},u_{\text{max}})} = {({- 0.4},0.4)}$. The y-axis represents the logarithm of the norm of the difference between two consecutive iterations, and the x-axis represents the solve time in milliseconds. Figure 2 shows that the Newton step is activated twice and is more efficient compared to PIPG iterations.

Figure 2: Comparison of residuals versus solve time for Newton-PIPG and PIPG algorithms for the oscillating masses example.

Table 1: Performance for different method on the oscillating mass example (All times in milliseconds.)

### Powered-Descent Guidance Problem

Our second numerical example considers a powered-descent guidance (PDG) problem for soft-landing a rocket-powered vehicle on a planetary body. Specifically, we consider the reference trajectory tracking problem . This problem can be formulated to fit within the form of Problem 1 and can be solved using the Newton-PIPG method. We use this problem to demonstrate the efficiency of Newton-PIPG on complex problems with various types of constraints and to compare Newton-PIPG with interior-point solvers, which are the only methods among those used in the previous numerical example capable of directly solving such problems.

In the PDG problem, the rocket-powered vehicle is initially located at $r_{\text{init}} \in {\mathbb{R}}^{3}$ with an initial velocity $v_{\text{init}} \in {\mathbb{R}}^{3}$. The goal is to land this vehicle at the origin with a final velocity of zero. There are seven state variables describing the problem at each time point: three variables for location, three variables for velocity, and one variable for the log of the vehicle mass. Meanwhile, there are four control variables at each time point: three variables for a three-dimensional thrust and one slack variable to implement the lossless convexification technique. In our numerical problem, we choose the amount of time points as 30.

Constraints of the PDG problem include second-order cone constraints on the four-dimensional control variable and the location variables separately, ball constraints on velocity, linear equalities for the dynamics, linear inequalities for the relationship between log-mass and thrust, and box constraints on log-mass. For the exact form and discussion of this problem, refer to \[11, Problem 3\].

Compared to the original form of \[11, Problem 3\], we made several modifications. First, since some dimensions of the optimal solution are a few magnitudes larger than others, we adjusted the quadratic coefficients in the objective function to ensure that each dimension of the optimal solution contributes similarly to the objective function. This adjustment is primarily to enhance the performance of the interior-point method. Without this change, the solution obtained by the interior-point method exhibited large relative errors on some dimensions of the solution, making the comparison between the interior-point method and Newton-PIPG less meaningful.

Secondly, we retained most of the coefficients listed in \[11, Table 3\], modifying only $r_{\text{init}}$, the initial location of the vehicle. We set $r_{\text{init}_{}} = {0\text{m}}$ and $r_{\text{init}_{}} = {2000\text{m}}$, while $r_{\text{init}_{}}$ follows an arithmetic sequence from 0 m to 2900 m, with a common difference of 50 m. The optimization problem becomes infeasible when $r_{\text{init}_{}}$ exceeds 2950 m. As the second component of $r_{\text{init}}$ increases, the problem approaches infeasibility, allowing us to test our algorithm in both scenarios where feasibility is easily guaranteed and where the problem is nearly infeasible.

In the numerical experiment, we compared the performance of Newton-PIPG with ECOS and PIPG. To use ECOS, we employed Yamlip to transform the original problem into a cone programming problem where ECOS is applicable. For the termination conditions, the termination criteria were set to $\epsilon_{\text{abs}} = 10^{- 12}$ and $\epsilon_{\text{rel}} = 0$ for Newton-PIPG. Similarly, we set the accuracy to $10^{- 12}$ for ECOS. The post-computation error for ECOS, compared to the Newton-PIPG result, ranged from $3 \times 10^{- 6}$ to $5 \times 10^{- 7}$ for different choices of $r_{\text{init}}$. For PIPG, we used two different termination criteria: $\epsilon_{\text{abs}} = 10^{- 4}$ and $\epsilon_{\text{abs}} = 10^{- 8}$, with $\epsilon_{\text{rel}} = 0$. The computed errors for PIPG showed that the algorithm achieved the assigned accuracy.

The wall time of the three algorithms under different initial conditions is shown in Figure 3, with a logarithmic time axis. In this figure, the line labeled "PIPG low accuracy" represents the results of the PIPG algorithm with a tolerance of $10^{- 4}$, while "PIPG high accuracy" corresponds to a tolerance of $10^{- 8}$. For $r_{\text{init}}$ values greater than 2250 meters in the second dimension, PIPG did not converge within 50,000 iterations. As a result, we used hollow markers to represent these non-converging points, which are not explicitly mentioned in the legend. The line labeled "ECOS" shows the wall time reported by Yamlip, excluding Yamlip's compile time.

Figure 3: Comparison of execution times for ECOS, Newton-PIPG, and PIPG with low accuracy (tolerance 10−4) and high accuracy (tolerance 10−8) across different initial y locations. Hollow markers represent non-converged points, which are omitted from the legend.

Comparing the computation speed between Newton-PIPG and ECOS, we observed that Newton-PIPG is notably faster than ECOS when the problem is not close to infeasibility. However, as the problem approaches infeasibility, especially when the second dimension of $r_{\text{init}}$ is larger than 2400 meters, the computation time of Newton-PIPG increases dramatically, while the speed of the interior-point methods appears unaffected by the proximity to infeasibility. Therefore, our numerical experiments suggest that Newton-PIPG is preferred when a highly accurate solution is required or when the problem is not close to infeasibility.

Figure 4 compares the residuals of Newton-PIPG and PIPG versus wall time, with $r_{\text{init}} = {}$ meters, using the same method as Figure 3. Newton-PIPG requires six Newton steps to converge below the threshold of $10^{- 12}$, with the last three Newton steps contributing most to the significant decrease in the residual norm, consistent with theoretical expectations.

Figure 4: Comparison of residuals versus solve time for Newton-PIPG and PIPG algorithms for the PDG example, with rinit = meters.

## Conclusion and Future Work

In conclusion, we introduced the Newton-PIPG method for solving optimal control QP problems, which combines an operator splitting method, PIPG, with second-order Newton steps. We demonstrated the convergence of this algorithm and provided an efficient technique for solving the linear system in the Newton step. Our numerical experiments showed that our algorithm performs well compared to other state-of-the-art algorithms in solving quadratic optimal control problems.

For future research, we will incorporate infeasibility detection for Newton-PIPG and extend our algorithm to handle more general constraints. Additionally, the current Newton-PIPG software is written in Matlab, and we expect that a pure C/C++ implementation could further reduce computation time.
