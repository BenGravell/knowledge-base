<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Newton-PIPG: A Fast Hybrid Algorithm for Quadratic Programs in Optimal Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose Newton-PIPG, an efficient method for solving quadratic programming (QP) problems arising in optimal control, subject to additional set constraints. Newton-PIPG integrates the Proportional-Integral Projected Gradient (PIPG) method with the Newton method, thereby achieving both global convergence and local quadratic convergence. The PIPG method, an operator-splitting algorithm, seeks a fixed point of the PIPG operator. Under mild assumptions, we demonstrate that this operator is locally smooth, enabling the application of the Newton method to solve the corresponding nonlinear fixed-point equation. Furthermore, we prove that the linear system associated with the Newton method is locally nonsingular under strict complementarity conditions. To enhance efficiency, we design a specialized matrix factorization technique that leverages the typical sparsity of optimal control problems in such systems. Numerical experiments demonstrate that Newton-PIPG achieves high accuracy and reduces computation time, particularly when feasibility is easily guaranteed.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

The development of techniques for solving Quadratic programming (QP) problems is a key enabler for advancing optimal control research, as efficiently solving these problems is often essential and a bottleneck in real-world optimal control applications. For example, Model Predictive Control (MPC), a framework for implementing optimal control, often relies on solving a series of QP problems. In addition, Sequential Convex Programming (SCP), a widely used algorithm for nonlinear optimal control, also relies on solving QP problems. Fast QP solvers are particularly beneficial in these applications, especially in scenarios requiring real-time implementation.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

We consider the following QP problem, which includes additional set constraints and frequently arises in optimal control applications:\

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

The sparsity patterns of $H_{E}$ and $H_{I}$ are typical for optimal control optimization problems. These matrices define equality and inequality constraints among consecutive time points, while the set ${\mathbb{D}}_{ij}$ includes constraints for states and inputs at each time point.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are a few differences between Problem and general optimal control QP problems. First, our objective function requires strong convexity, and the quadratic term must be homogeneous with respect to the constraint ${\mathbb{D}}_{ij}$. Specifically, for dimensions of $z$ constrained by the same set ${\mathbb{D}}_{ij}$, the corresponding quadratic cost coefficients must be identical. Second, we restrict the set ${\mathbb{D}}_{ij}$ to specific families of convex sets. Possible relaxations of these requirements are discussed in Section.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Widely used methods for solving Problem fall into two primary categories: second-order methods and operator-splitting methods, each with their own advantages and disadvantages. Second-order methods, such as interior-point methods and active-set methods, utilize the curvature information of the optimization problem. These methods typically converge in a modest number of iterations and are robust when the problem approaches infeasibility. Commonly used software in this category includes MOSEK, Gurobi, and ECOS. For further theoretical discussions on second-order methods, we refer the reader to.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

One drawback of second-order methods lies in their high computational cost per iteration, as each step requires solving a linear system. This issue becomes significant as the dimension of the optimization variables increases. Additionally, while interior-point solvers are generally effective, they typically cannot directly handle Problem 1 in its original form and require the use of parsers, such as Yamlip or CVX, to transform the problem into a solver-compatible form. This transformation process adds overhead and increases the effort needed for verification, validation, and maintenance.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another approach to solving Problem is the operator-splitting method, which constructs an update operator applied at each iteration, ensuring that the iterations converge to the fixed point of this operator. Unlike interior-point methods, operator-splitting methods eliminate the need for matrix factorization, resulting in significantly lower per-iteration computational costs. Additionally, these methods do not require external parsers and are typically implemented with a smaller codebase. For a comprehensive review of operator-splitting methods, see. However, one drawback of operator-splitting methods is that they often require a large number of iterations to converge, especially when the problem is ill-conditioned.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our main contribution is the development of Newton-PIPG, a hybrid method that integrates the Proportional-Integral Projected Gradient (PIPG) method, a representative operator-splitting approach, with the Newton method. This approach is motivated by the insight that finding a fixed point for the updating operator in operator-splitting methods is equivalent to solving a nonlinear fixed point equation. Given the Newton method's effectiveness in solving such equations, we design a Newton step for this fixed-point problem, with PIPG providing a warm start to ensure global convergence. Compared to second-order methods, Newton-PIPG reduces the need for matrix factorization and avoids the requirement for additional parsers. Additionally, in contrast to operator-splitting methods, the Newton step reduces the number of iterations required, enhancing both accuracy and speed.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

We also provide theoretical guarantees for the Newton-PIPG method. Specifically, we demonstrate that under an extended linear independence constraint qualification and strict complementarity condition, the Newton step is well-defined, the associated matrix is nonsingular, and the Newton-PIPG algorithm enjoys global convergence with local quadratic convergence behavior.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Furthermore, we tailor our algorithm for optimal control problems. Recognizing that the most computationally expensive step is solving a large linear system in the Newton method, we exploit the sparsity inherent in optimal control problems to design an efficient factorization strategy, significantly reducing computation time.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Road Map", "weight": 1.0} -->

The structure of this paper is as follows. Section reviews the PIPG method and the Newton method. Section presents the Newton step for the PIPG operator, its theoretical properties, and an efficient factorization method for the matrix involved in the Newton step. Section discusses the global and local convergence of the Newton-PIPG algorithm. Section outlines the restrictions of our algorithm and possible relaxations. Section provides implementation details, including the design of termination criteria, and presents numerical experiments comparing our method with other state-of-the-art QP solvers.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Proportional-Integral Projected Gradient", "weight": 1.0} -->

As discussed in the introduction, we propose a new method that combines the Proportional-Integral Projected Gradient (PIPG) method with the Newton method. In this section, we provide a brief overview of the PIPG method.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Proportional-Integral Projected Gradient", "weight": 1.0} -->

Let ${Fix}{(T)}$ denote the set of fixed points of operator $T$, that is, ${{Fix}{(T)}} = {\{{{(z,w)} \in {\mathbb{R}}^{n_{z} + n_{w}}}\mid{{(z,w)} = {T{(z,w)}}}\}}$. The following theorem for the convergence of the PIPG method is a direct consequence of Theorem 3.3, Theorem 4.3, and Theorem 4.4,

<!-- chunk {"id": "body-0016", "role": "body", "section": "Newton Method", "weight": 1.0} -->

Theorem 2.1 indicates that PIPG solves a nonlinear fixed-point equation ${{(z^{\star},w^{\star})} - {T{(z^{\star},w^{\star})}}} = 0$. Consequently, we consider applying the Newton method directly to solve this equation, given its fast local convergence rate. In this section, we provide a brief review of the Newton method.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Newton Method", "weight": 1.0} -->

The Newton method is designed to solve

<!-- chunk {"id": "body-0018", "role": "body", "section": "Newton Method", "weight": 1.0} -->

The Newton method is known for its locally quadratic convergence rate, but it also has three major disadvantages: the requirement of a nonsingular Jacobian matrix, the high computational cost of computing a factorization of the Jacobian matrix, and the lack of a global convergence guarantee. Additionally, in order to apply the Newton method to the fixed-point equation of $T$, we need to assess the differentiability of the operator $T$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Newton Method", "weight": 1.0} -->

In the next section, we will define the Newton step for the PIPG operator $T$. We will show that the Jacobian of the PIPG exists and that the matrix appearing in the Newton step is invertible in the neighborhood of $T$'s fixed point under some mild assumptions. Hence, the linear equation in the Newton step has a local solution. Additionally, we will provide a factorization strategy for the Jacobian matrix that leverages its sparse structure. The global convergence result is deferred to Section.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Newton Step for PIPG", "weight": 1.0} -->

We start with a formal definition of the Newton step for PIPG. Consider the case where both $\pi_{\mathbb{D}}$ and $\pi_{{\mathbb{K}}^{\circ}}$ are differentiable.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Newton Step for PIPG", "weight": 1.0} -->

If $\pi_{\mathbb{D}}$ and $\pi_{{\mathbb{K}}^{\circ}}$ are not differentiable or if $I - J_{T}$ is singular, we will simply set $J_{T}$ as a zero matrix of the same shape. We will later show that regardless of the choice of $J_{T}$, the global convergence of our algorithm will not be affected and, with mild assumptions, it will also not affect the local convergence rate. Also, note that projections are functions that are almost everywhere differentiable.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Newton Step for PIPG", "weight": 1.0} -->

With $J_{T}$ being well-defined for all $(z,w)$, we have the definition of the Newton step

<!-- chunk {"id": "body-0023", "role": "body", "section": "Extended Linearly Independent Constraint Qualification", "weight": 1.0} -->

In this section, we introduce the constraint qualification for our problem, which ensures the matrix in the Newton step is locally nonsingular. Such nonsingularity requires the fixed point set of the PIPG operator to be a single point. This, in turn, implies the uniqueness of both the primal and dual solutions: the strong convexity of Problem guarantees a unique primal solution, while we need additional constraint qualifications to ensure the uniqueness of the dual solution.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Extended Linearly Independent Constraint Qualification", "weight": 1.0} -->

The linearly independent constraint qualification (LICQ) is commonly used to ensure the uniqueness of the dual variable. However, LICQ is trivially violated for some important cases in Problem.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Extended Linearly Independent Constraint Qualification", "weight": 1.0} -->

One example where LICQ fails is when ${\mathbb{D}}_{ij}$ is a second-order cone and the optimal solution $z_{ij} = 0$. Note that the second-order cone is defined as

<!-- chunk {"id": "body-0026", "role": "body", "section": "Extended Linearly Independent Constraint Qualification", "weight": 1.0} -->

When $x = 0$, the gradient of ${\| x\|}^{2} - y$ is a zero vector, causing LICQ to automatically fail.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Extended Linearly Independent Constraint Qualification", "weight": 1.0} -->

Another example is when ${\mathbb{D}}_{ij}$ is an affine subspace. According to our definition of ${\mathbb{D}}_{ij}$, an affine subspace is formed as

<!-- chunk {"id": "body-0028", "role": "body", "section": "Extended Linearly Independent Constraint Qualification", "weight": 1.0} -->

For any point $z_{ij} \in {\mathbb{D}}_{ij}$, LICQ is automatically violated.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 3.5", "weight": 1.0} -->

In the proof of Theorem 3.3, the extended LICQ is not required for the "if" direction. Meanwhile, for any fixed point $(z^{\star},w^{\star})$ of the PIPG operator, we have

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 3.5", "weight": 1.0} -->

Therefore, Theorem 3.3 ensures that every fixed point $(z^{\star},w^{\star})$ of the PIPG operator is a solution to Problem, regardless of whether the extended LICQ holds.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Properties of Projections to Convex Sets", "weight": 1.0} -->

In this section, we discuss the properties of projections onto convex sets. These properties are useful for subsequent proofs. To start, we discuss the eigenvalues of Jacobians of projection functions.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Nonsingularity of the Newton Step Matrix", "weight": 1.0} -->

In this section, we will show that the Newton step is well defined in a local neighborhood of $(z^{\star},w^{\star})$, i.e., $T$ is differentiable and $I - {J_{T}{(z^{k},w^{k})}}$ is invertible.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Nonsingularity of the Newton Step Matrix", "weight": 1.0} -->

We start with the following lemma, which is also a major component of the algorithm. This lemma ensures that the linear system, which involves a nonsymmetric matrix, can be transformed into a symmetric linear system. We will later show that this symmetric linear system exhibits a desirable sparsity pattern.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Remark 3.17", "weight": 1.0} -->

$I - J_{T}$ may not be invertible if the current iteration is not close to the primal-dual solution pair. For methods to handle the singular $I - J_{T}$, see Section. Importantly, this non-invertibility does not compromise the global convergence or the local convergence rate.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Efficient Computation of Linear System in Newton Step", "weight": 1.0} -->

To efficiently factorize the invertible matrix

<!-- chunk {"id": "body-0036", "role": "body", "section": "Efficient Computation of Linear System in Newton Step", "weight": 1.0} -->

we use an approach. This approach leverages the sparsity inherent in the optimal control problem, reducing computational costs to a linear function of the total number of time points $N$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Efficient Computation of Linear System in Newton Step", "weight": 1.0} -->

Next, we compute the Cholesky decomposition ${\overset{\sim}{W}}_{\mathbb{D}} = {LL^{\top}}$ using the factorization technique, where $L$ is lower triangular. The Cholesky factor $L$ has a lower bidiagonal block structure.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Efficient Computation of Linear System in Newton Step", "weight": 1.0} -->

To compute $L_{00}$, we employ the Cholesky decomposition on ${\overset{\sim}{W}}_{00}$. Subsequently, $L_{10}$ is determined through forward substitution from the equation ${L_{00}L_{10}^{\top}} = {\overset{\sim}{W}}_{01}$. Next, $L_{11}$ is obtained by performing Cholesky decomposition on the matrix ${\overset{\sim}{W}}_{11} - {L_{10}L_{10}^{\top}}$. This procedure is repeated iteratively to construct the entire $L$ matrix.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Efficient Computation of Linear System in Newton Step", "weight": 1.0} -->

We summarize the procedure for computing the Newton step in Algorithm. It combines the insights from Lemma 3.13 with the Cholesky factorization. Details of implementations are left to Section.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Global Convergence for Newton-PIPG", "weight": 1.0} -->

In this section, we introduce the Newton-PIPG algorithm, a hybrid of the PIPG operator and the Newton step.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Global Convergence for Newton-PIPG", "weight": 1.0} -->

We define the residual of the PIPG operator as

<!-- chunk {"id": "body-0042", "role": "body", "section": "Global Convergence for Newton-PIPG", "weight": 1.0} -->

and we denote ${Fix}{(T)}$ the fixed point set of $T.$ Rather than employing the conventional Euclidean norm as the convergence criterion, we adopt an alternative norm: ${\| z\|}_{M}:=\sqrt{\langle z,{Mz}\rangle}$, where $M$ is a positive definite matrix expressed as

<!-- chunk {"id": "body-0043", "role": "body", "section": "Global Convergence for Newton-PIPG", "weight": 1.0} -->

The positive definiteness of $M$ is proved later in Lemma 4.1.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Global Convergence for Newton-PIPG", "weight": 1.0} -->

and the norm $\parallel \cdot \parallel_{M}$ for a given matrix $A$ is defined as

<!-- chunk {"id": "body-0045", "role": "body", "section": "Global Convergence for Newton-PIPG", "weight": 1.0} -->

The norm $\parallel \cdot \parallel_{M}$ is intrinsic to the proof of PIPG's convergence, rendering it a convenient choice for establishing convergence for the Newton-PIPG algorithm. Due to the equivalence among norms on finite-dimension problems, the convergence in $\parallel \cdot \parallel_{M}$ is equivalent to that in the Euclidean norm.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Global Convergence for Newton-PIPG", "weight": 1.0} -->

In order to ensure the convergence of the Newton method, we design Algorithm that combines the PIPG with the Newton step, inspired. In this algorithm, the PIPG algorithm will be a safeguard to ensure global convergence, while the Newton step will be used to accelerate PIPG locally.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Global Convergence for Newton-PIPG", "weight": 1.0} -->

1: Require c ∈ [0, 1), e ≥ 0, t &gt; 0, Initial iteration (z0,w0)
3: while termination criteria not satisfied do
4: Compute an update pk = (Δzk,Δwk) either be zero or from the Newton step

<!-- chunk {"id": "body-0048", "role": "body", "section": "Global Convergence for Newton-PIPG", "weight": 1.0} -->

Algorithm provides flexibility in choosing the update $p^{k}$ while ensuring global convergence, as demonstrated in Theorem 4.3. In practice, $p^{k}$ can be set to zero or to the solution of the Newton step. When $p^{k}$ is zero, the Newton update is disabled. To achieve fast computation, we periodically activate the Newton step instead of using it at each iteration. Details on selecting $p^{k}$ are available in Section.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Global Convergence for Newton-PIPG", "weight": 1.0} -->

The termination criteria for Algorithm is discussed in Section 6.2. The coefficient $\sigma$ in Algorithm is a safeguard ensuring that the Newton update does not move $(z^{k},w^{k})$ to a point far away from the current iteration. The use of such a coefficient $\sigma$ is inspired.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Convergence Analysis of Newton-PIPG", "weight": 1.0} -->

First, we show the positive definiteness of $M$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 4.10", "weight": 1.0} -->

The quadratic convergence result in Theorem 4.8 can be further strengthened to convergence within finite iterations if $J_{\mathbb{D}}$ and $J_{{\mathbb{K}}^{\circ}}$ are piecewise constant functions. This scenario occurs when $J_{\mathbb{D}}$ consists of boxes, halfspaces, and affine subspaces. In these cases, $J_{T}$ will also be a piecewise constant function of the primal and dual variables. Within a local neighborhood of the fixed point $(z^{\star},w^{\star})$, the PIPG operator will be a linear function, allowing the Newton step to find the fixed point within one iteration.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Remark 4.11", "weight": 1.0} -->

The proof method in Theorem 4.8 is inspired. The difference between the proof in Theorem 4.8 and the convergence analysis is that we establish convergence for a hybrid approach combining the Newton method, instead of the quasi-Newton method, with the operator splitting method, thus achieving a better convergence rate. Furthermore, the invertibility of $I - J_{T}$ guarantees the existence of the coefficient $\sigma$ in our proof, eliminating the requirement of \[, Assumption 2\], which is not commonly used in optimization research.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Restrictions and Relaxation", "weight": 1.0} -->

In this section, we point out several restrictions in Problem compared to general optimal control quadratic programming problems, and we discuss the possibility of relaxing such restrictions.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Restrictions and Relaxation", "weight": 1.0} -->

In Problem, we require $P$ to be a diagonal matrix with positive diagonal elements. This requirement ensures the invertibility of ${I - J_{\mathbb{D}}} + {\alpha J_{\mathbb{D}}P}$, which is necessary for the linear algebra technique outlined in Lemma 3.13. Although this choice of $P$ is suitable for many optimal control problems, it does not encompass all scenarios. In particular, it does not cover QPs arising in the sequential convexification of nonconvex optimal control problems that utilize the $L_{1}$-exact penalty. When applying the $L_{1}$ exact penalty, transforming the linearized subproblems into QP form requires the introduction of slack variables. Consequently, the resulting QP no longer has a positive definite quadratic term; the quadratic matrix contains zeros on the diagonal for positions that correspond to these slack variables. To address this issue, we propose adding an additional squared $L_{2}$-norm to the penalty. This modification not only maintains the exactness but also ensures our algorithm's compatibility with the subproblems from the sequential convexification.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Restrictions and Relaxation", "weight": 1.0} -->

If generalization is necessary, one can directly compute the factorization for $I - J_{T}$ at some Newton steps and use iterative methods such as GMRES for other Newton steps. In this approach, previous factorizations can be used as preconditioners for subsequent iterations.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Implementation and Numerical Experiments", "weight": 1.0} -->

We demonstrate the implementation details of the Newton-PIPG algorithm and compare its performance with other state-of-the-art solvers.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Implementation Details for Newton-PIPG", "weight": 1.0} -->

Algorithm provides a framework for the Newton-PIPG algorithm, allowing flexibility in choosing the form of $p^{k}$. This flexibility leads to different strategies for implementing the Newton-PIPG algorithm. Here are some strategies we use to optimize computation speed.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Implementation Details for Newton-PIPG", "weight": 1.0} -->

First, we reduce the use of Newton steps by applying them only when PIPG iterations stagnate. A heuristic waiting period, typically 3-10 PIPG iterations, is employed. If both $J_{{\mathbb{K}}^{\circ}}$ and the active manifold of $\pi_{\mathbb{D}}$ remain unchanged during this period, the algorithm switches to the Newton step.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Implementation Details for Newton-PIPG", "weight": 1.0} -->

Second, after each computationally intensive Newton step, a line search is performed to monitor the reduction in the PIPG residual $R{(z^{k},w^{k})}$. This line search, typically executed 3-5 times per Newton step, improves practical convergence speed without affecting the convergence properties of the Newton-PIPG algorithm. The line search result that reduces the residual norm by a factor of $c$, as defined in Algorithm, is accepted. The coefficient $c$ is generally close to 1; for instance, we use $c = 0.99$. If the line search fails to sufficiently reduce the residual, the result is discarded, and a PIPG update is performed instead. Moreover, in the case of a failed line search, the waiting period is extended until either $J_{{\mathbb{K}}^{\circ}}$ or the active manifold of $\pi_{\mathbb{D}}$ is updated.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Implementation Details for Newton-PIPG", "weight": 1.0} -->

Third, to improve the conditioning of the optimization problem, we rescale the matrix $H$ so that the norm of each row is of the same magnitude. This rescaling does not affect the optimal solution. For a detailed discussion, we refer interested readers to.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Implementation Details for Newton-PIPG", "weight": 1.0} -->

Fourth, $I - J_{T}$ can become singular when the current iteration is not in a local neighborhood of the primal-dual solution pair $(z^{\star},w^{\star})$. To obtain useful results from the Newton step, we add an additional perturbation to the matrix $I - J_{T}$. The perturbation we choose is an identity matrix multiplied by a coefficient proportional to the norm of the residual $R{(z^{k},w^{k})}$, so that the perturbation becomes negligible when the current iteration is close to $(z^{\star},w^{\star})$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Implementation Details for Newton-PIPG", "weight": 1.0} -->

Fifth, we monitor the convergence of the residual using the Euclidean norm instead of $\parallel \cdot \parallel_{M}$, as the Euclidean norm is more efficient to compute. In our experiments, using the Euclidean norm did not compromise the algorithm's convergence. However, in situations where it might, one may consider using $\parallel \cdot \parallel_{M}$ to validate the Newton step for a more robust implementation.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Implementation Details for Newton-PIPG", "weight": 1.0} -->

Finally, we optimize the matrix-vector multiplication by partitioning the sparse matrix $H$ into zero blocks and dense, nonzero blocks. Instead of performing sparse matrix multiplication, we treat $H$ as a collection of dense block matrices. Using for-loops, we compute the matrix-vector product as a series of dense matrix-vector multiplications. This approach is also applied when computing the factorization in the Newton step. A similar method is used.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Termination Criteria", "weight": 1.0} -->

In this section, we propose the termination criteria for both PIPG and Newton-PIPG. We claim that monitoring the magnitude of ${\|{R{(z^{k},w^{k})}}\|} = {\|{{(z^{k + 1},w^{k + 1})} - {(z^{k},w^{k})}}\|}$ provides a good criterion for stopping the PIPG algorithm. Here, $(z^{k},w^{k})$ and $(z^{k + 1},w^{k + 1})$ are consecutive PIPG iterations. Since Newton-PIPG requires iteratively calling the PIPG operator, we can use the same termination criteria for the Newton-PIPG algorithm as well.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Numerical Experiment Introduction", "weight": 1.0} -->

We test the performance of the Newton-PIPG algorithm via two example problems. The first example is an oscillating masses problem that involves only linear constraints. The second example is a powered-descent guidance problem that includes various types of constraints, such as linear inequality, ball constraints and second-order cones. We compare the results against benchmark algorithms such as ECOS and OSQP, among others.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Numerical Experiment Introduction", "weight": 1.0} -->

The numerical experiment is conducted using MATLAB. The Newton-PIPG code was initially written in MATLAB and then converted into executable C code using MATLAB Coder. The computational experiments were carried out on a computer equipped with an AMD Ryzen 7 5700G 8-Core CPU and 16GB of RAM. The results here are generated with code: github.com/UW-ACL/NEWTON-PIPG-for-QP-Problems.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Oscillating Masses", "weight": 1.0} -->

We use a benchmark oscillating masses problem to evaluate the performance of our algorithm in comparison to other state-of-the-art algorithms. Consider a mechanical system comprising $m = 16$ masses connected in a one-dimensional line, shown in figure. Each mass is defined by its 1-D velocity and position, resulting in a total of $n_{x} = 16$ state variables. To control this mechanical system, we assign one control variable to each mass. Hence the dimension of control at each time point is ${n_{u} = 8}.$ Time is discretized using a step size of $\Delta$. The total number of time points is denoted by N, and we set ${\Delta = {3/N}},$ i.e. this equation describes a system among $\lbrack 0,3\rbrack$. In our experiment, we set $N = {20,50,100}$ to show the scalability of our algorithm.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Oscillating Masses", "weight": 1.0} -->

Here, the matrices $P$ and $Q$ are identity matrices and matrices $A$ and $B$ are defined as

<!-- chunk {"id": "body-0069", "role": "body", "section": "Oscillating Masses", "weight": 1.0} -->

where the matrix ${\mathbb{L}} \in {\mathbb{R}}^{m \times m}$ is a tridiagonal matrix with 2's on the diagonal and -1's on the subdiagonal and superdiagonal entries.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Oscillating Masses", "weight": 1.0} -->

The initial conditions ${\hat{x}}_{0}$ are randomly generated. In our experiments, we set $x_{\text{min}} = {- 1}$ and $x_{\text{max}} = 1$. The initial condition is generated from a normal distribution with mean zero and a standard deviation of 0.3 then projected to $\lbrack x_{\text{min}},x_{\text{max}}\rbrack$. This ensures that the values of $x$ are spread within the range of $\lbrack{- 1},1\rbrack$, without too many values equal to -1 or 1.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Oscillating Masses", "weight": 1.0} -->

In our numerical experiments, we compared our algorithm with several prominent solvers: OSQP, SCS, SCS-Anderson, PIPG, and ECOS, using their respective MATLAB packages. OSQP and SCS are ADMM-based methods. SCS-Anderson represents methods that combine operator-splitting operators with quasi-Newton methods. Lastly, ECOS stands as an example of an interior-point method.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Oscillating Masses", "weight": 1.0} -->

Since our current algorithm does not have feasibility detection capacity, we only consider problems with feasible solutions. In practice, we run OSQP and SCS before the Newton-PIPG and Newton-PIPG will only be used to solve problems that are characterized as feasible by both OSQP and SCS.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Oscillating Masses", "weight": 1.0} -->

For our numerical experiments, we set the tolerance level of all competing solvers to $10^{- 8}$ in their respective software settings, and for PIPG we set ${\epsilon_{abs} = 10^{- 8}},$ and $\epsilon_{rel} = 0$. The Newton-PIPG algorithm does not require a specific termination criterion, as it converges within a finite number of iterations when the optimization problem is linear. Post-computation, we measure and report the difference between each solver's solution and that of Newton-PIPG using the $L_{2}$ norm.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Oscillating Masses", "weight": 1.0} -->

We set ${(u_{\text{min}},u_{\text{max}})} \in {\{{({- 1},1)},{({- 0.4},0.4)}\}}$ and then randomly generate 100 initial conditions for each combination of $N$ and $(u_{\text{min}},u_{\text{max}})$. The average time consumption is shown in Table, measured in milliseconds. In this table, the SCS-And refers to the SCS-Anderson algorithm, while the N-PIPG denotes the Newton-PIPG. These time consumption are reported by the Matlab package of each solver. When the maximum control magnitude is set to 1, we observed that all randomly generated problems are feasible. When the control magnitude is set to 0.4, approximately 95% of the randomly generated problems are feasible, and we only apply the Newton-PIPG algorithm to these problems.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Oscillating Masses", "weight": 1.0} -->

When set to ${(u_{\text{min}},u_{\text{max}})} = {({- 1},1)}$ and $N = 20$, our algorithm outperforms others by a factor of five. Such a ratio persists with larger problem sizes. With respect to the post-computation error tolerance, ECOS attains $10^{- 5}$ in $L_{2}$ norm in all cases. At ${N = 20},$ all other solver achieves $10^{- 8}$ in accuracy. At $N = 50$ and $N = 100$, algorithms other than PIPG and ECOS achieve accuracy of $10^{- 6}$. PIPG reaches the target accuracy for all cases.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Oscillating Masses", "weight": 1.0} -->

The Newton-PIPG algorithm achieves rapid QP solution primarily because the PIPG step rapidly identifies the correct active constraints of $\mathbb{D}$ in situations where the constraints are not tight. Thus, it usually requires a single Newton step and a small number of PIPG steps to solve the problem. To evaluate scenarios where more Newton steps are needed, we set ${(u_{\text{min}},u_{\text{max}})} = {({- 0.4},0.4)}$. With more inequality constraints activated, more Newton steps are expected. As predicted, Newton-PIPG slows down but is still 30% faster than the best of the other algorithms.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Oscillating Masses", "weight": 1.0} -->

We also compare Newton-PIPG with SCS-Anderson, as both methods hybridize operator-splitting and second-order approaches. SCS-Anderson does speed up SCS, but the increase is limited. However, adding the Newton step to PIPG dramatically improves its speed, both at $u = 1$ and $u = 0.4$. This indicates that the Newton step has better performance compared to quasi-Newton methods.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Oscillating Masses", "weight": 1.0} -->

We presented a typical plot comparing the computation time between the Newton-PIPG method and the PIPG method. The plot tracks the computation time and the norm of the residual after each PIPG and Newton step, with $N = 20$ and ${(u_{\text{min}},u_{\text{max}})} = {({- 0.4},0.4)}$. The y-axis represents the logarithm of the norm of the difference between two consecutive iterations, and the x-axis represents the solve time in milliseconds. Figure shows that the Newton step is activated twice and is more efficient compared to PIPG iterations.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Powered-Descent Guidance Problem", "weight": 1.0} -->

Our second numerical example considers a powered-descent guidance (PDG) problem for soft-landing a rocket-powered vehicle on a planetary body. Specifically, we consider the reference trajectory tracking problem. This problem can be formulated to fit within the form of Problem and can be solved using the Newton-PIPG method. We use this problem to demonstrate the efficiency of Newton-PIPG on complex problems with various types of constraints and to compare Newton-PIPG with interior-point solvers, which are the only methods among those used in the previous numerical example capable of directly solving such problems.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Powered-Descent Guidance Problem", "weight": 1.0} -->

In the PDG problem, the rocket-powered vehicle is initially located at $r_{\text{init}} \in {\mathbb{R}}^{3}$ with an initial velocity $v_{\text{init}} \in {\mathbb{R}}^{3}$. The goal is to land this vehicle at the origin with a final velocity of zero. There are seven state variables describing the problem at each time point: three variables for location, three variables for velocity, and one variable for the log of the vehicle mass. Meanwhile, there are four control variables at each time point: three variables for a three-dimensional thrust and one slack variable to implement the lossless convexification technique. In our numerical problem, we choose the amount of time points as 30.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Powered-Descent Guidance Problem", "weight": 1.0} -->

Constraints of the PDG problem include second-order cone constraints on the four-dimensional control variable and the location variables separately, ball constraints on velocity, linear equalities for the dynamics, linear inequalities for the relationship between log-mass and thrust, and box constraints on log-mass. For the exact form and discussion of this problem, refer to \[, Problem 3\].

<!-- chunk {"id": "body-0082", "role": "body", "section": "Powered-Descent Guidance Problem", "weight": 1.0} -->

Compared to the original form of \[, Problem 3\], we made several modifications. First, since some dimensions of the optimal solution are a few magnitudes larger than others, we adjusted the quadratic coefficients in the objective function to ensure that each dimension of the optimal solution contributes similarly to the objective function. This adjustment is primarily to enhance the performance of the interior-point method. Without this change, the solution obtained by the interior-point method exhibited large relative errors on some dimensions of the solution, making the comparison between the interior-point method and Newton-PIPG less meaningful.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Powered-Descent Guidance Problem", "weight": 1.0} -->

Secondly, we retained most of the coefficients listed in \[, Table 3\], modifying only $r_{\text{init}}$, the initial location of the vehicle. We set $r_{\text{init}_{}} = {0\text{m}}$ and $r_{\text{init}_{}} = {2000\text{m}}$, while $r_{\text{init}_{}}$ follows an arithmetic sequence from 0 m to 2900 m, with a common difference of 50 m. The optimization problem becomes infeasible when $r_{\text{init}_{}}$ exceeds 2950 m. As the second component of $r_{\text{init}}$ increases, the problem approaches infeasibility, allowing us to test our algorithm in both scenarios where feasibility is easily guaranteed and where the problem is nearly infeasible.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Powered-Descent Guidance Problem", "weight": 1.0} -->

In the numerical experiment, we compared the performance of Newton-PIPG with ECOS and PIPG. To use ECOS, we employed Yamlip to transform the original problem into a cone programming problem where ECOS is applicable. For the termination conditions, the termination criteria were set to $\epsilon_{\text{abs}} = 10^{- 12}$ and $\epsilon_{\text{rel}} = 0$ for Newton-PIPG. Similarly, we set the accuracy to $10^{- 12}$ for ECOS. The post-computation error for ECOS, compared to the Newton-PIPG result, ranged from $3 \times 10^{- 6}$ to $5 \times 10^{- 7}$ for different choices of $r_{\text{init}}$. For PIPG, we used two different termination criteria: $\epsilon_{\text{abs}} = 10^{- 4}$ and $\epsilon_{\text{abs}} = 10^{- 8}$, with $\epsilon_{\text{rel}} = 0$.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Powered-Descent Guidance Problem", "weight": 1.0} -->

The computed errors for PIPG showed that the algorithm achieved the assigned accuracy.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Powered-Descent Guidance Problem", "weight": 1.0} -->

The wall time of the three algorithms under different initial conditions is shown in Figure, with a logarithmic time axis. In this figure, the line labeled "PIPG low accuracy" represents the results of the PIPG algorithm with a tolerance of $10^{- 4}$, while "PIPG high accuracy" corresponds to a tolerance of $10^{- 8}$. For $r_{\text{init}}$ values greater than 2250 meters in the second dimension, PIPG did not converge within 50,000 iterations. As a result, we used hollow markers to represent these non-converging points, which are not explicitly mentioned in the legend. The line labeled "ECOS" shows the wall time reported by Yamlip, excluding Yamlip's compile time.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Powered-Descent Guidance Problem", "weight": 1.0} -->

Comparing the computation speed between Newton-PIPG and ECOS, we observed that Newton-PIPG is notably faster than ECOS when the problem is not close to infeasibility. However, as the problem approaches infeasibility, especially when the second dimension of $r_{\text{init}}$ is larger than 2400 meters, the computation time of Newton-PIPG increases dramatically, while the speed of the interior-point methods appears unaffected by the proximity to infeasibility. Therefore, our numerical experiments suggest that Newton-PIPG is preferred when a highly accurate solution is required or when the problem is not close to infeasibility.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

In conclusion, we introduced the Newton-PIPG method for solving optimal control QP problems, which combines an operator splitting method, PIPG, with second-order Newton steps. We demonstrated the convergence of this algorithm and provided an efficient technique for solving the linear system in the Newton step. Our numerical experiments showed that our algorithm performs well compared to other state-of-the-art algorithms in solving quadratic optimal control problems.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Conclusion and Future Work", "weight": 1.5} -->

For future research, we will incorporate infeasibility detection for Newton-PIPG and extend our algorithm to handle more general constraints. Additionally, the current Newton-PIPG software is written in Matlab, and we expect that a pure C/C++ implementation could further reduce computation time.
