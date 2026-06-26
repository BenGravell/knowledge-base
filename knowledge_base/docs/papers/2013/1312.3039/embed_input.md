<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Conic Optimization via Operator Splitting and Homogeneous Self-Dual Embedding

Topics include Conic optimization, Operator splitting, Homogeneous self-dual embedding, Alternating-direction method of multipliers, First-order methods, SCS, Infeasibility certificates, Large-scale optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces SCS, a first-order cone solver that applies operator splitting to a homogeneous self-dual embedding of the cone program. The design trades high-accuracy interior-point behavior for scalability and robustness: the same iterations can return primal or dual solutions or infeasibility certificates, support several cone families, and solve large SOCP, SDP, exponential-cone, and power-cone problems with direct or indirect linear algebra.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We introduce a first order method for solving very large convex cone programs. The method uses an operator splitting method, the alternating directions method of multipliers, to solve the homogeneous self-dual embedding, an equivalent feasibility problem involving finding a nonzero point in the intersection of a subspace and a cone. This approach has several favorable properties. Compared to interior-point methods, first-order methods scale to very large problems, at the cost of requiring more time to reach very high accuracy. Compared to other first-order methods for cone programs, our approach finds both primal and dual solutions when available or a certificate of infeasibility or unboundedness otherwise, is parameter-free, and the per-iteration cost of the method is the same as applying a splitting method to the primal or dual alone. We discuss efficient implementation of the method in detail, including direct and indirect methods for computing projection onto the subspace, scaling the original problem data, and stopping criteria. We describe an open-source implementation, which handles the usual (symmetric) non-negative, second-order, and semidefinite cones as well as the (non-self-dual) exponential and power cones and their duals.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We report numerical results that show speedups over interior-point cone solvers for large problems, and scaling to very large general cone programs.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we develop a method for solving convex cone optimization problems that can (a) provide primal or dual certificates of infeasibility when relevant and (b) scale to large problem sizes. The general idea is to use a first-order method to solve the homogeneous self-dual embedding of the primal-dual pair; the homogeneous self-dual embedding provides the necessary certificates, and first-order methods scale well to large problem sizes.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

The homogeneous self-dual embedding is a single convex feasibility problem that encodes the primal-dual pair of optimization problems. Solving the embedded problem involves finding a nonzero point in the intersection of two convex sets, a convex cone and a subspace. If the original pair is solvable, then a solution can be recovered from any nonzero solution to the embedding; otherwise, a certificate of infeasibility is generated that proves that the primal or dual is infeasible (and the other one unbounded). The homogeneous self-dual embedding has been widely used with interior-point methods Ye:11; sedumi; SY:12.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We solve the embedded problem with an operator splitting method known as the *alternating direction method of multipliers* (ADMM) GlM:75; GaM:76; G:83; Eck:89; see BP:11 for a recent survey. It can be viewed as a simple variation of the classical alternating projections algorithm for finding a point in the intersection of two convex sets. Roughly speaking, ADMM adds a dual state variable to the basic method, which can substantially improve convergence. The overall method can reliably provide solutions to modest accuracy after a relatively small number of iterations and can solve large problems far more quickly than interior-point methods. (It may not be suitable if high accuracy is required, due to the slow 'tail convergence' of first order methods in general, and ADMM in particular HY:12b.) To the best of our knowledge, this is the first application of a first-order method to solving such embeddings. The approach described in this paper combines a number of different ideas that are well-established in the literature, such as cone programming and operator splitting methods. We highlight various dimensions along which our method can be compared to others.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Some methods for solving cone programs only return primal solutions, while others can return primal-dual pairs. In addition, some methods can only handle feasible problems, while other methods can also return certificates of infeasibility or unboundedness. The idea of homogeneous self-dual embedding is due to Ye and others YT:94; XH:96. Self-dual embeddings have generally been solved via interior-point methods NeN:94, while the literature on other algorithms has generally yielded methods that cannot return certificates of infeasibility; see, e.g., WGY:10; LLR:11; AI:13.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our approach involves converting a primal-dual pair into a convex feasibility problem involving finding a point in the intersection of two convex sets. There are many projection algorithms that could be used to solve this kind of problem, such as the classical alternating directions method or Dykstra's alternating projections method BD:86; BB:94, amongst others CCCH:12; CE:94. For a further discussion of these and many other projection methods, see Bauschke and Koch BK:13. Any of these methods could be used to solve the problem in homogeneous self-dual embedding form.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Operator splitting techniques go back to the 1950s; ADMM itself was developed in the mid-1970s GlM:75; GaM:76. Since then a rich literature has developed around ADMM and related methods G:83; Eck:89; EB:92; CP:12; C:13; KP:14; GT:89; LM:79; G:84; FG:83. Many equivalences exist between ADMM and other operator splitting methods. It was shown in G:83 that ADMM is equivalent to the variant of Douglas-Rachford splitting presented in LM:79 (the original, more restrictive, form of Douglas-Rachford splitting was presented in DR:56 ) applied to the dual problem, which itself is equivalent to Rockafellar's proximal point algorithm R:76; EB:92.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Douglas-Rachford splitting is also equivalent to Spingarn's 'method of partial inverses' Spi:83; Spi:85a; Spi:85b when one of the operators is the normal cone map of a linear subspace Eck:88; Eck:89. In this paper we apply ADMM to a problem where one of the functions is the indicator of a linear subspace, so our algorithm can also be viewed as an application of Spingarn's method. Another closely related technique is the 'split-feasibility problem', which seeks two points related by a linear mapping, each of which is constrained to be in a convex set CE:94; B:02; CMS:07; C:01.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

In Eck:89 and MW:14 it was shown that equivalences exist between ADMM applied to the primal problem, the dual problem, and a saddle point formulation of the problem; in other words, ADMM is (in a sense) itself self-dual.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

These techniques have been used in a broad range of applications including imaging Com:96; GO:09; OV:13, control jovanovic:10; annergren:12; oper_splt_ctrl; MX:12; BOD:12, estimation admm_tv_est, signal processing CW:06; CoP:07; CP:09; YZ:11, finance port_opt_bound, distributed optimization PB:12; K:13, and many others.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

There are several different ways to apply ADMM to solve cone programs WGY:10; BP:11. In some cases, these are applied to the original cone program (or its dual) and yield methods that can return primal-dual pairs, but cannot handle infeasible or unbounded problems.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

The indirect version of our method interacts with the data solely by multiplication by the data matrix or its adjoint, which we can informally refer to as a 'scientific computing' style algorithm; it is also called a 'matrix-free method'. There are several other methods that share similar characteristics, such as CP:11; BCG:10; Gon:12; MOS:13; MOS:14a; MOS:14b; ZST:10; OC:12, as well as some techniques for solving the split-feasibility problem B:02. See Esser et al. EZC:10 for a detailed discussion of various first-order methods and the relationships between them, and Parikh and Boyd PB:14 for a survey of proximal algorithms in particular.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Outline", "weight": 1.0} -->

In Sect. 2 we review convex cone optimization, conditions for optimality, and the homogeneous self-dual embedding. In Sect. 3, we derive an algorithm that solves using ADMM applied to the homogeneous self-dual embedding of a cone program. In Sect. 4, we discuss how to perform the sub-steps of the procedure efficiently. In Sect. 5 we introduce a scaling procedure that greatly improves convergence in practice. We conclude with some numerical examples in Sect. 6, including (when applicable, i.e., the problems are small enough and involve only symmetric cones) a comparison of our approach with a state-of-the-art interior-point method, both in quality of solution and solution time.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Conic Optimization", "weight": 1.0} -->

Consider the *primal-dual pair* of (convex) cone optimization problems Here $x \in {\mathbb{R}}^{n}$ and $s \in {\mathbb{R}}^{m}$ (with $n \leq m$) are the primal variables, and $r \in {\mathbb{R}}^{n}$ and $y \in {\mathbb{R}}^{m}$ are the dual variables We refer to $x$ as the primal variable, $s$ as the primal slack variable, $y$ as the dual variable, and $r$ as the dual residual.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Conic Optimization", "weight": 1.0} -->

The primal and dual optimal values are denoted $p^{\star}$ and $d^{\star}$, respectively; we allow the cases when these are infinite: $p^{\star} = {+ \infty}$ ($- \infty$) indicates primal infeasibility (unboundedness), and $d^{\star} = {- \infty}$ ($+ \infty$) indicates dual infeasibility (unboundedness). It is easy to show weak duality, i.e., $d^{\star} \leq p^{\star}$, with no assumptions on the data. We will assume that strong duality holds, i.e., $p^{\star} = d^{\star}$, including the cases when they are infinite.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Optimality Conditions", "weight": 1.0} -->

When strong duality holds, the KKT (Karush-Kuhn-Tucker) conditions are necessary and sufficient for optimality. Explicitly, $(x^{\star},s^{\star},r^{\star},y^{\star})$ satisfies the KKT conditions, and so is primal-dual optimal, when i.e., when $(x^{\star},s^{\star})$ is primal feasible, $(r^{\star},y^{\star})$ is dual feasible, and the complementary slackness condition ${{(y^{\star})}^{T}s^{\star}} = 0$ holds. The complementary slackness condition can equivalently be replaced by the condition which explicitly forces the *duality gap*, ${c^{T}x} + {b^{T}y}$, to be zero.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Certificates of Infeasibility", "weight": 1.0} -->

If strong duality holds, then exactly one of the sets is nonempty, a result known as a *theorem of strong alternatives* (BV:04 Sect. 5.8). Since the set $\mathcal{P}$ encodes primal feasibility, this implies that any dual variable $y \in \mathcal{D}$ serves as a *proof* or *certificate* that the set $\mathcal{P}$ is empty, i.e., that the problem is primal infeasible. Intuitively, the set $\mathcal{D}$ encodes the requirements for the dual problem to be feasible but unbounded.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Certificates of Infeasibility", "weight": 1.0} -->

Similarly, exactly one of the following two sets is nonempty: Any primal variable $x \in \overset{\sim}{\mathcal{P}}$ is a certificate of dual infeasibility.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Homogeneous Self-Dual Embedding", "weight": 1.0} -->

The original pair of problems can be converted into a single feasibility problem by embedding the KKT conditions into a single system of equations and inclusions that the primal and dual optimal points must jointly satisfy. The embedding is as follows: Any $(x^{\star},s^{\star},r^{\star},y^{\star})$ that satisfies is optimal. However, if is primal or dual infeasible, then has no solution.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Homogeneous Self-Dual Embedding", "weight": 1.0} -->

The homogeneous self-dual embedding YT:94 addresses this shortcoming: This embedding introduces two new variables, $\tau$ and $\kappa$, that are non-negative and complementary, i.e., at most one is nonzero. To see complementarity note that the inner product between $(x,y,\tau)$ and $(r,s,\kappa)$ at any solution must be zero due to the skew symmetry of the matrix, and the individual components $x^{T}r$, $y^{T}s$, and $\tau\kappa$ must each be non-negative by the definition of dual cones.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Homogeneous Self-Dual Embedding", "weight": 1.0} -->

The reason for using this embedding is that the different possible values of $\tau$ and $\kappa$ encode the different possible outcomes. If $\tau$ is nonzero at the solution, then it serves as a scaling factor that can be used to recover the solutions to; otherwise, if $\kappa$ is nonzero, then the original problem is primal or dual infeasible. In particular, if $\tau = 1$ and $\kappa = 0$ then the self-dual embedding reduces to the simpler embedding.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Homogeneous Self-Dual Embedding", "weight": 1.0} -->

Any solution of the self-dual embedding $(x,s,r,y,\tau,\kappa)$ falls into one of three cases: $\tau > 0$ and $\kappa = 0$. The point satisfies the KKT conditions of and so is a primal-dual solution. $\tau = 0$ and $\kappa > 0$. This implies that the gap ${c^{T}x} + {b^{T}y}$ is negative, which immediately tells us that the problem is either primal or dual infeasible.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Homogeneous Self-Dual Embedding", "weight": 1.0} -->

If ${b^{T}y} < 0$, then $\hat{y} = {y/{({b^{T}y})}}$ is a certificate of primal infeasibility (i.e., $\mathcal{D}$ is nonempty) since If ${c^{T}x} < 0$, then $\hat{x} = {x/{({- {c^{T}x}})}}$ is a certificate of dual infeasibility (i.e., $\overset{\sim}{\mathcal{P}}$ is nonempty) since If both ${c^{T}x} < 0$ and ${b^{T}y} < 0$, then the problem is both primal and dual infeasible (but the strong duality assumption is violated). $\tau = \kappa = 0$. If one of $c^{T}x$ or $b^{T}y$ is negative, then it can be used to derive a certificate of primal or dual infeasibility.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Homogeneous Self-Dual Embedding", "weight": 1.0} -->

Otherwise nothing can be concluded about the original problem. Note that zero is always a solution to, but steps can be taken to avoid it, as we discuss in Section 3.4.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Homogeneous Self-Dual Embedding", "weight": 1.0} -->

The system is homogeneous because if $(x,s,r,y,\tau,\kappa)$ is a solution to the embedding, then so is $({tx},{ts},{tr},{ty},{t\tau},{t\kappa})$ for any $t \geq 0$, and when $t > 0$ this scaled value yields the same primal-dual solution or certificates. The embedding is also self-dual, which we show below.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Self-dual property", "weight": 1.0} -->

Let us show that the feasibility problem is self-dual. The Lagrangian has the form where the dual variables are $\nu,\lambda,\mu$, with $\lambda \in \mathcal{C}^{\ast}$, $\mu \in \mathcal{C}$. Minimizing over the primal variables $u,v$, we conclude that Eliminating $\nu = {- \mu}$ and using $Q^{T} = {- Q}$ we can write the dual problem as with variables $\mu,\lambda$. This is identical to.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Operator Splitting Method", "weight": 1.0} -->

The convex feasibility problem can be solved by many methods, ranging from simple alternating projections to sophisticated interior-point methods. We are interested in methods that scale to very large problems, so we will use an operator splitting method, the alternating direction method of multipliers (ADMM). There are many operator splitting methods (some of which are equivalent to ADMM) that could be used to solve the convex feasibility problem, such as Douglas-Rachford iteration, split feasibility methods, Spingarn's method of partial inverses, Dykstra's method, and others. While we have not tried these other methods, we suspect that many of them would yield comparable results to ADMM. Moreover, much of our discussion below, on simplifying the iterations and efficiently carrying out the required steps, would also apply to (some) other operator splitting methods.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Basic Method", "weight": 1.0} -->

ADMM is an operator splitting method that can solve convex problems of the form (ADMM can also solve problems where $x$ and $z$ are affinely related; see BP:11 and the references therein.) Here, $f$ and $g$ may be nonsmooth or take on infinite values to encode implicit constraints. The basic ADMM algorithm is where $\rho > 0$ is a step size parameter and $\lambda$ is the (scaled) dual variable associated with the constraint $x = z$, and the superscript $k$ denotes iteration number. The initial points $z^{0}$ and $\lambda^{0}$ are arbitrary, but are usually taken to be zero. Under some very mild conditions (BP:11 Sect.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Basic Method", "weight": 1.0} -->

3.2), ADMM converges to a solution, in the following sense: ${f{(x^{k})}} + {g{(z^{k})}}$ converges to the optimal value, $\lambda^{k}$ converges to an optimal dual variable, and $x^{k} - z^{k}$, the equality constraint residual, converges to zero. Additionally, for the restricted form we consider, we have the stronger guarantee that $x^{k}$ and $z^{k}$ converge to a common value; see, e.g., (EB:92 Sect. 5). We will mention later some variations on this basic ADMM algorithm with similar convergence guarantees.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Basic Method", "weight": 1.0} -->

To apply ADMM, we transform the embedding to ADMM form: where $I_{\mathcal{S}}$ denotes the indicator function (Roc:70 Sect. 4) of the set $\mathcal{S}$. A direct application of ADMM to the self-dual embedding, written as, yields the following algorithm: where $\Pi_{\mathcal{S}}{(x)}$ denotes the Euclidean projection of $x$ onto the set $\mathcal{S}$. Here, $\lambda$ and $\mu$ are dual variables for the equality constraints on $u$ and $v$, respectively.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Simplified Method", "weight": 1.0} -->

In this section we show that the basic ADMM algorithm given above can be simplified using properties of our specific problem.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Eliminating Dual Variables", "weight": 1.0} -->

If we initialize $\lambda^{0} = v^{0}$ and $\mu^{0} = u^{0}$, then $\lambda^{k} = v^{k}$ and $\mu^{k} = u^{k}$ for all subsequent iterations. This result allows us to eliminate the dual variable sequences above. This will also simplify the linear system in the first step and remove one of the cone projections.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Projection Onto Affine Set", "weight": 1.0} -->

Each iteration, the algorithm computes a projection onto $\mathcal{Q}$ by solving with variables $u$ and $v$. The KKT conditions for this problem are where $\mu \in {\mathbb{R}}^{m + n + 1}$ is the dual variable associated with the equality constraint ${{Qu} - v} = 0$. By eliminating $\mu$, we obtain The matrix $Q$ is skew-symmetric, so this simplifies to (The matrix $I + Q$ is guaranteed to be invertible since $Q$ is skew-symmetric.)

<!-- chunk {"id": "body-0037", "role": "body", "section": "Final Algorithm", "weight": 1.0} -->

Combining the simplifications of the previous sections, the final algorithm is The algorithm consists of three steps. The first step is projection onto a subspace, which involves solving a linear system with coefficient matrix $I + Q$; this is discussed in more detail in Section 4.1. The second step is projection onto a cone, a standard operation discussed in detail in (PB:14 Sect. 6.3).

<!-- chunk {"id": "body-0038", "role": "body", "section": "Final Algorithm", "weight": 1.0} -->

The last step is computationally trivial and has a simple interpretation: As the algorithm runs, the vectors $u^{k}$ and ${\overset{\sim}{u}}^{k}$ converge to each other, so $u^{k + 1} - {\overset{\sim}{u}}^{k + 1}$ can be viewed as the error at iteration $k + 1$. The last step shows that $v^{k + 1}$ is exactly the running sum of the errors. Roughly speaking, this running sum of errors is used to drive the error to zero, exactly as in integral control FPE:94.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Final Algorithm", "weight": 1.0} -->

We can also interpret the second and third steps as a combined Moreau decomposition of the point ${\overset{\sim}{u}}^{k + 1} - v^{k}$ into its projection onto $\mathcal{C}$ (which gives $u^{k + 1}$) and its projection onto $- \mathcal{C}^{\ast}$ (which gives $v^{k + 1}$).

<!-- chunk {"id": "body-0040", "role": "body", "section": "Final Algorithm", "weight": 1.0} -->

The algorithm is homogeneous: If we scale the initial points by some factor $\gamma > 0$, then all subsequent iterates are also scaled by $\gamma$ and the overall algorithm will give the same primal-dual solution or certificates, since the system being solved is also homogeneous.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Final Algorithm", "weight": 1.0} -->

A straightforward application of ADMM directly to the primal or dual problem in obtains an algorithm which requires one linear system solve involving $A^{T}A$ and one projection onto the cone $\mathcal{K}$, which has the same per-iteration cost as; see, e.g., WGY:10 for details.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Variations", "weight": 1.0} -->

There are many variants on the basic ADMM algorithm described above, and any of them can be employed with the homogeneous self-dual embedding. We briefly describe two important variations that we use in our reference implementation.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Over-relaxation", "weight": 1.0} -->

In the $u$- and $v$-updates, replace all occurrences of ${\overset{\sim}{u}}^{k + 1}$ with where $\alpha \in \rbrack 0,2\lbrack$ is a relaxation parameter GT:79; EB:92. When $\alpha = 1$, this reduces to the basic algorithm given above. When $\alpha > 1$, this is known as *over-relaxation*; when $\alpha < 1$, this is *under-relaxation*. Some numerical experiments suggest that values of $\alpha$ around $1.5$ can improve convergence, in practice Eck:94b; oper_splt_ctrl.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Approximate projection", "weight": 1.0} -->

Another variation replaces the subspace projection update with a suitable approximation R:76; GT:79; EB:92. We replace ${\overset{\sim}{u}}^{k + 1}$ in the first line of with any ${\overset{\sim}{u}}^{k + 1}$ that satisfies where $\zeta^{k} > 0$ satisfy ${\sum_{k}\zeta^{k}} < \infty$. This variation is particularly useful when an iterative method is used to compute ${\overset{\sim}{u}}^{k + 1}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Approximate projection", "weight": 1.0} -->

Note that is implied by the (more easily verified) inequality This follows from the fact that ${\|{({I + Q})}^{- 1}\|}_{2} \leq 1$, which holds since $Q$ is skew-symmetric. The left-hand side of is the norm of the residual in the equations that define ${\overset{\sim}{u}}^{k + 1}$ in the basic algorithm.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Algorithm convergence", "weight": 1.0} -->

We show that the algorithm converges, in the sense that it eventually produces a point for which the optimality conditions almost hold. For the basic algorithm, and the variant with over-relaxation and approximate projection, for all iterations $k > 0$ we have These follow from the last two steps of, and hold for any values of $v^{k - 1}$ and ${\overset{\sim}{u}}^{k}$. Since $u^{k + 1}$ is a projection onto $\mathcal{C}$, $u^{k} \in \mathcal{C}$ follows immediately. The condition $v^{k} \in \mathcal{C}^{\ast}$ holds since the last step can be rewritten as $v^{k + 1} = {\Pi_{\mathcal{C}^{\ast}}{({v^{k} - {\overset{\sim}{u}}^{k + 1}})}}$, as observed above.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Algorithm convergence", "weight": 1.0} -->

The last condition, ${{(u^{k})}^{T}v^{k}} = 0$, holds by our observation that these two points are the (orthogonal) Moreau decomposition of the same point.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Algorithm convergence", "weight": 1.0} -->

In addition to the three conditions, only one more condition must hold for $(u^{k},v^{k})$ to be optimal: ${Qu^{k}} = v^{k}$. This equality constraint holds asymptotically, that is, we have, as $k\rightarrow\infty$, (We show this from the convergence result for ADMM below.) Thus, the iterates $(u^{k},v^{k})$ satisfy three of the four optimality conditions at every step, and the fourth one is satisfied in the limit.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Algorithm convergence", "weight": 1.0} -->

To show that the equality constraint holds asymptotically we use general ADMM convergence theory; see, e.g., (BP:11 Sect. 3.4.3), or EB:92 for the case of approximate projections. This convergence theory tells us that as $k\rightarrow\infty$, even with over-relaxation and approximate projection. From the last step in we conclude that ${v^{k + 1} - v^{k}}\rightarrow 0$. From and ${v^{k + 1} - v^{k}}\rightarrow 0$, we obtain ${u^{k + 1} - u^{k}}\rightarrow 0$. and using we get From ${u^{k + 1} - u^{k}}\rightarrow 0$ and ${v^{k + 1} - v^{k}}\rightarrow 0$ we conclude which is what we wanted to show.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Eliminating convergence to zero", "weight": 1.0} -->

We can guarantee that the algorithm will not converge to zero if a nonzero solution exists, by proper selection of the initial point $(u^{0},v^{0})$, at least in the case of exact projection.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Eliminating convergence to zero", "weight": 1.0} -->

Denote by $(u^{\star},v^{\star})$ any nonzero solution to, which we assume satisfies either $u_{\tau}^{\star} > 0$ or $v_{\kappa}^{\star} > 0$, i.e., we can use it to derive an optimal point or a certificate. If we choose initial point $(u^{0},v^{0})$ with $u_{\tau}^{0} = 1$ and $v_{\kappa}^{0} = 1$, and all other entries zero, then we have Let $\phi$ denote the mapping that consists of one iteration of algorithm, i.e., ${(u^{k + 1},v^{k + 1})} = {\phi{(u^{k},v^{k})}}$.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Eliminating convergence to zero", "weight": 1.0} -->

We show in the appendix that the mapping $\phi$ is nonexpansive, i.e., for any $(u,v)$ and $(\hat{u},\hat{v})$ we have that (Nonexpansivity holds for ADMM more generally; see, e.g., G:83; FG:83; EB:92 for details.) Since $(u^{\star},v^{\star})$ is a solution to it is a fixed point of $\phi$, i.e., Since the problem is homogeneous, the point $\gamma{(u^{\star},v^{\star})}$ is also a solution for any positive $\gamma$, and is also a fixed point of $\phi$. Combining this, we have at iteration $k$ for any $\gamma > 0$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Eliminating convergence to zero", "weight": 1.0} -->

Expanding and setting which is positive by our choice of $(u^{0},v^{0})$, we obtain which implies that and applying Cauchy-Schwarz yields Thus, for $k = {1,2,\ldots}$, the iterates are bounded away from zero.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Normalization", "weight": 1.0} -->

The vector given by satisfies the conditions given in for all iterations, and by combining with we have that in the exact projection case at least. In other words, the unit vector $({\hat{u}}^{k},{\hat{v}}^{k})$ eventually satisfies the optimality conditions for the homogeneous self-dual embedding to any desired accuracy.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Termination Criteria", "weight": 1.0} -->

In view of the discussion of the previous section, a stopping criterion of the form for some tolerance $\epsilon$, or alternatively a normalized criterion will work, i.e., the algorithm eventually stops. Here, we propose a different scheme that handles the components of $u$ and $v$ corresponding to primal and dual variables separately. This yields stopping criteria that are consistent with ones traditionally used for cone programming.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Termination Criteria", "weight": 1.0} -->

We terminate the algorithm when it finds a primal-dual optimal solution or a certificate of primal or dual infeasibility, up to some tolerances. If $u_{\tau}^{k} > 0$, then let be the candidate solution. This candidate is guaranteed to satisfy the cone constraints and complementary slackness condition. It thus suffices to check that the residuals are small. Explicitly, we terminate if and emit $(x^{k},s^{k},y^{k})$ as (approximately) primal-dual optimal. Here, quantities $\epsilon_{pri},\epsilon_{dual},\epsilon_{gap}$ are the primal residual, dual residual, and duality gap tolerances, respectively.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Termination Criteria", "weight": 1.0} -->

On the other hand, if the current iterates satisfy then $u_{x}^{k}/{({- {c^{T}u_{x}^{k}}})}$ is an approximate certificate of unboundedness with tolerance $\epsilon_{unbdd}$, or if they satisfy then $u_{y}^{k}/{({- {b^{T}u_{y}^{k}}})}$ is an approximate certificate of infeasibility with tolerance $\epsilon_{infeas}$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Termination Criteria", "weight": 1.0} -->

These stopping criteria are identical to those used by many other cone solvers and similar to those used by DIMACS dimacs; M:03 and the SeDuMi solver sedumi.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Efficient Subspace Projection", "weight": 1.0} -->

In this section we discuss how to efficiently compute the projection onto the subspace $\mathcal{Q}$, exactly and also approximately (for the approximate variation).

<!-- chunk {"id": "body-0060", "role": "body", "section": "Solving the Linear System", "weight": 1.0} -->

The first step is to solve the linear system ${{({I + Q})}{\overset{\sim}{u}}^{k}} = w$ for some $w$: To lighten notation, let where $M + {hh^{T}}$ is the Schur complement of the lower right block $1$ in $I + Q$. Applying the Sherman-Morrison-Woodbury formula (GvL:96 p. 50) to ${({M + {hh^{T}}})}^{- 1}$ yields Thus, in the first iteration, we compute and cache $M^{- 1}h$. To solve in subsequent iterations, it is only necessary to compute $M^{- 1}{(w_{x},w_{y})}$, which will require the bulk of the computational effort, and then to perform some simple vector operations using cached quantities.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Solving the Linear System", "weight": 1.0} -->

There are two main ways to solve linear equations of the form the system that needs to be solved once per iteration. The first method, a *direct method* that exactly solves the system, is to solve by computing a sparse permuted $LDL^{T}$ factorization davis_book of the matrix in before the first iteration, then to use this cached factorization to solve the system in subsequent steps. This technique, called factorization caching, is very effective in the common case when the factorization cost is substantially higher than the subsequent solve cost, so all iterations after the first one can be carried out quickly. Because the matrix is quasi-definite, the factorization is guaranteed to exist for any symmetric permutation Van:95.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Solving the Linear System", "weight": 1.0} -->

The second method, an *indirect method* that we use to approximately solve the system, involves first rewriting as by elimination. This system is then solved with the conjugate gradient method (CG) NW:06; GvL:96; Saad:03. Each iteration of conjugate gradient requires multiplying once by $A$ and once by $A^{T}$, each of which can be parallelized. If $A$ is very sparse, then these multiplications can be performed especially quickly; when $A$ is dense, it may be better to first form $G = {I + {A^{T}A}}$ in the setup phase. We warm-start CG by initializing each subsequent call with the solution obtained by the previous call. We terminate the CG iterations when the residual satisfies for some appropriate sequence $\zeta^{k}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Repeated Solves", "weight": 1.0} -->

If the cone problem must be solved more than once, then computation from the first solve can be re-used in subsequent solves by warm-starting: we set the initial point to $u^{0} = {(x^{\star},y^{\star},1)}$, $v^{0} = {(0,s^{\star},0)}$, where $x^{\star},s^{\star},y^{\star}$ are the optimal primal-dual variables from the previous solve. If the data matrix $A$ does not change and a direct method is being used, then the sparse permuted $LDL^{T}$ factorization can also be re-used across solves for additional savings. This arises in many practical situations, such as in control, statistics, and sequential convex programming.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Scaling Problem Data", "weight": 1.0} -->

Though the algorithm in has no explicit parameters, the relative scaling of the problem data can greatly affect the convergence. This suggests a pre-processing step where we scale the data to (hopefully) improve the convergence.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Scaling Problem Data", "weight": 1.0} -->

In particular, consider scaling vectors $b$ and $c$ by positive scalars $\sigma$ and $\rho$, respectively, and scaling the primal and dual equality constraints by diagonal positive definite matrices $D$ and $E$, respectively. This yields the following scaled primal-dual problem pair: with variables $\hat{x}$, $\hat{y}$, $\hat{r}$, and $\hat{s}$. After solving this new cone program with problem data $\hat{A} = {DAE}$, $\hat{b} = {\sigmaDb}$, and $\hat{c} = {\rhoEc}$, the solution to the original problem can be recovered from the scaled solution via Transformation by the matrix $D$ must preserve membership of the cone $\mathcal{K}$, to ensure that if $s \in \mathcal{K}$, then ${D^{- 1}s} \in \mathcal{K}$ (the same is not required of $E$).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Scaling Problem Data", "weight": 1.0} -->

If $\mathcal{K} = {\mathcal{K}_{1} \times \cdots \times K_{q}}$, where $K_{i} \in {\mathbb{R}}^{m_{i}}$, then we could use, for example, We have observed that in practice, data which has been *equilibrated*, i.e., scaled to have better conditioning, admits better convergence Bauer:63; Bauer:69; Sluis:69; Ruiz:01. We have found that if the columns of $A$ and $b$ all have Euclidean norm close to one and the rows of $A$ and $c$ have similar norms, then the algorithm typically performs well. The scaling parameters $E$, $D$, $\sigma$, and $\rho$ can be chosen to (approximately) achieve this Osborne:60; Ruiz:01; PC:11, though the question of whether there is an optimal scaling remains open. There has recently been much work devoted to the question of choosing an optimal, or at least good diagonal scaling; see gb:14a; gb:15a.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Scaled termination criteria", "weight": 1.0} -->

When the algorithm is applied to the scaled problem, it is still desirable to terminate the procedure when the residuals for the *original* problem satisfy the stopping criteria defined in Sect. 3.5.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Scaled termination criteria", "weight": 1.0} -->

The original residuals can be expressed in terms of the scaled data as and the convergence checks can be applied as before. The stopping criteria for unboundedness and infeasibility then become

<!-- chunk {"id": "body-0069", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In this section we present numerical results for SCS, our implementation of the algorithm described above. We show results on four application problems, in each case instances that are small, medium, and large. To demonstrate scaling to extremely large problems, we also report results on randomly generated problems with known optimal value.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

We compare the results to SDPT3 SDPT3 and Sedumi sedumi, state-of-the-art interior-point solvers. We use this comparison for several purposes. First, the solution computed by these solvers is high accuracy, so we can use it to assess the quality of the solution found by SCS. Second, we can compare the computing times. Run-time comparison is not completely fair, since an interior-point method reliably computes a high accuracy solution, whereas SCS is meant only to compute a solution of modest accuracy and may take longer than an interior-point method if high accuracy is required. Third, Sedumi targets the same homogeneous self-dual embedding as SCS, so we can compare a first-order and a second-order method on the same embedding.

<!-- chunk {"id": "body-0071", "role": "body", "section": "SCS", "weight": 1.0} -->

Our implementation, which we call SCS for 'Splitting Conic Solver', is written in C and can solve cone programs involving any combination of non-negative, second-order, semidefinite, exponential, and power cones (and dual exponential and power cones) scs. It has multi-threaded and single-threaded versions, and computes the (approximate) projections onto the subspace using either a direct method or an iterative method. SCS is available online at along with the code to run the numerical examples. SCS can be used in other C, C++, Python, Matlab, R, Julia, Java, and Scala programs and is a supported solver in parser-solvers CVX cvx, CVXPY cvxpy, Convex.jl convexjl, and YALMIP yalmip. It is now the default solver for CVXPY and Convex.jl for problems that cannot be expressed using the standard symmetric cones.

<!-- chunk {"id": "body-0072", "role": "body", "section": "SCS", "weight": 1.0} -->

The direct implementation uses a single-threaded sparse permuted $LDL^{T}$ decomposition from the SuiteSparse package davis_book; ldl; amd. The sparse indirect implementation, which uses conjugate gradient, can perform the matrix multiplications on the CPU or on the GPU. The CPU version uses a basic sparse multiplication routine parallelized using OpenMP openmp08. The GPU version uses the sparse CUDA BLAS library cuda. The indirect solver uses $\zeta^{k} = {({1/k})}^{1.5}$ as the termination tolerance at iteration $k$, where the tolerance is defined.

<!-- chunk {"id": "body-0073", "role": "body", "section": "SCS", "weight": 1.0} -->

SCS handles the usual non-negative, second-order, and semidefinite cones, as well as the exponential cone and its dual (PB:14 Sect. 6.3.4), and the power cone and its dual nes:06; sy:14; KH:14, defined as for any $a \in {\lbrack 0,1\rbrack}$. Projections onto the semidefinite cone are performed using the LAPACK `dsyevr` method for computing the eigendecomposition; projections onto the other cones are implemented in C. The multi-threaded version computes the projections onto the cones in parallel.

<!-- chunk {"id": "body-0074", "role": "body", "section": "SCS", "weight": 1.0} -->

In the experiments reported below, we use the termination criteria described in Sect. 3.5 and Sect. 5, with the default values The objective value reported for SCS in the experiments below is the average of the primal and dual objectives at termination. The time required to do any preprocessing (such as the matrix factorization) and to carry out and undo the scaling are included in the total solve times.

<!-- chunk {"id": "body-0075", "role": "body", "section": "SCS", "weight": 1.0} -->

All the experiments were carried out on a system with 32 2.2GHz cores and 512Gb of RAM, running Linux. (The single-threaded versions, of course, do not make use of the multiple cores.) The GPU used was a Geforce GTX Titan X with 12Gb of memory.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Lasso", "weight": 1.0} -->

Consider the following optimization problem: over $z \in {\mathbb{R}}^{p}$, where $F \in {\mathbb{R}}^{q \times p}$, $g \in {\mathbb{R}}^{q}$ and $\mu \in {\mathbb{R}}_{+}$ are data. This problem, known as the *lasso* tibshirani:96, is widely studied in high-dimensional statistics, machine learning, and compressed sensing. Roughly speaking, seeks a sparse vector $z$ such that ${Fz} \approx g$, and the parameter $\mu$ trades off between quality of fit and sparsity. It has been observed that first-order methods can perform very well on lasso-type problems when the solution is sparse DDD:04; DZ:13.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Lasso", "weight": 1.0} -->

The lasso problem can be formulated as the SOCP lobo:98 with variables $z \in {\mathbb{R}}^{p}$, $t \in {\mathbb{R}}^{p}$ and $w \in {\mathbb{R}}$. This formulation is easily transformed in turn into the standard form.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Problem instances", "weight": 1.0} -->

We generated data for the numerical instances as follows. First, the entries of $F$ were sampled independently from a standard normal distribution. We randomly generated a sparse vector $\hat{z}$ with $p$ entries, only $p/10$ of which were nonzero. We then set $g = {{F\hat{z}} + w}$, where the entries in $w$ were sampled independently and identically from $\mathcal{N}{(0,0.1)}$. We chose $\mu = {0.1\mu^{\max}}$ for all instances, where $\mu^{\max} = {\|{F^{T}g}\|}_{\infty}$ is the smallest value of $\mu$ for which the solution to is zero.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Results", "weight": 1.0} -->

The results are summarized in Table 1. For the small, medium, and large instances, the fastest implementation of SCS, indirect on the GPU, provides a speedup of roughly $30 \times$, $190 \times$, and $1000 \times$, respectively over SDPT3 and Sedumi. In the largest case, SCS takes less than $4$ minutes compared to nearly 3 days for SDPT3 and Sedumi. In other words, not only is the degree of speedup dramatic in each case, but it also continues to increase as the problem size gets larger; this is consistent with our goal of solving problems outside the ability of traditional interior-point methods.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Results", "weight": 1.0} -->

SCS is meant to provide solutions of modest, not high, accuracy. However, we see that the solutions returned attain an objective value within 0.01% of the optimal value attained by SDPT3 and Sedumi, a negligible difference in applications.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Results", "weight": 1.0} -->

If we compare the direct and indirect CPU implementations of SCS, we see that for small problems the direct version of SCS is faster, but for larger problems the multi-threaded indirect method dominates. The sparsity pattern in this problem lends itself to an efficient multi-threaded matrix multiply since the columns in the data matrix $A$ have a similar number of nonzeros. This speed-up is even more pronounced when the matrix multiplications are performed on the GPU. std. form variables n std. form constraints m total solve time total solve time total solve time total solve time SCS indirect GPU: total solve time Table 1: Results for the lasso example.

<!-- chunk {"id": "body-0082", "role": "body", "section": "Portfolio Optimization", "weight": 1.0} -->

Consider a simple long-only portfolio optimization problem Markowitz1952; port_opt_bound, (BV:04 Sect. 4.4.1), in which we choose the relative weights of assets to maximize the expected risk-adjusted return of a portfolio: where the variable $z \in {\mathbb{R}}^{p}$ represents the portfolio of $p$ assets, $\mu \in {\mathbb{R}}^{p}$ is the vector of expected returns, $\gamma > 0$ is the *risk aversion parameter*, and $\Sigma \in {\mathbb{R}}^{p \times p}$ is the asset return covariance matrix (also known as the *risk model*). The risk model is expressed in *factor model form* where $F \in {\mathbb{R}}^{p \times q}$ is the *factor loading matrix* and $D \in {\mathbb{R}}^{p \times p}$ is a diagonal matrix representing 'idiosyncratic' or asset-specific risk.

<!-- chunk {"id": "body-0083", "role": "body", "section": "Portfolio Optimization", "weight": 1.0} -->

The number of risk factors $q$ is typically much less than the number of assets $p$. (The factor model form is widely used in practice.)

<!-- chunk {"id": "body-0084", "role": "body", "section": "Portfolio Optimization", "weight": 1.0} -->

This problem can be converted in the standard way into an SOCP: with variables $z \in {\mathbb{R}}^{p}$, $t \in {\mathbb{R}}$, $s \in {\mathbb{R}}$, $u \in {\mathbb{R}}$, and $v \in {\mathbb{R}}$. This can be transformed into standard form in turn.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Problem instances", "weight": 1.0} -->

The vector of log-returns, $\log{(\mu)}$, was sampled from a standard normal distribution, yielding log-normally distributed returns. The entries in $F$ were sampled independently from $\mathcal{N}{(0,0.1)}$, and the diagonal entries of $D$ were sampled independently from a uniform distribution on $\lbrack 0,0.1\rbrack$. For all problems, we chose $\gamma = 1$.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Results", "weight": 1.0} -->

The results are summarized in Table 2. In all cases the objective value attained by SCS was within $0.5\%$ of the optimal value. The worst budget constraint violation of the solution returned by SCS in any instance was only $0.002$ and the worst non-negativity constraint violation was only $5 \times 10^{- 7}$. SCS direct is more than $7$ times faster than SDPT3 on the largest instance, and much faster than Sedumi, which didn't manage to solve the largest instance after a week of computation.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Results", "weight": 1.0} -->

Unlike the previous example, the direct solver is faster than the indirect solver on the CPU for all instances. This is due to imbalance in the number of nonzeros per column which, for the simple multi-threaded matrix multiply we're using, leads to some threads handling much more data than others, and so the speedup provided by parallelization is modest. The indirect method on the GPU is fastest for the medium sized example. For the small example the cost of transferring the data to the GPU outweighs the benefits of performing the computation on the GPU, and the large example could not fit into the GPU memory. std. form variables n std. form constraints m total solve time total solve time total solve time total solve time SCS indirect GPU: total solve time Table 2: Results for the portfolio optimization example.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Robust Principal Components Analysis", "weight": 1.0} -->

This example considers the problem of recovering a low rank matrix from measurements that have been corrupted by sparse noise rpca; AGM:14. In rpca, the authors formulated this problem as follows: with variables $L \in {\mathbb{R}}^{p \times q}$ and $S \in {\mathbb{R}}^{p \times q}$, and with data $M \in {\mathbb{R}}^{p \times q}$ the matrix of measurements and $\mu \in {\mathbb{R}}_{+}$ a parameter that constrains the estimate of the corrupting noise term to be below a certain value. Here, $\parallel \cdot \parallel_{\ast}$ is the nuclear norm (dual of spectral norm) and $\parallel \cdot \parallel_{1}$ is the elementwise $\ell_{1}$ norm (i.e., sum of the absolute values of the entries).

<!-- chunk {"id": "body-0089", "role": "body", "section": "Robust Principal Components Analysis", "weight": 1.0} -->

Roughly speaking, the problem is a convex surrogate for decomposing the given matrix $M$ into the sum of a sparse matrix $S$ and a low-rank matrix $L$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Robust Principal Components Analysis", "weight": 1.0} -->

The problem can be converted into an SDP as follows FHB:01; VB:96: with variables $L \in {\mathbb{R}}^{p \times q}$, $S \in {\mathbb{R}}^{p \times q}$, $W_{1} \in {\mathbb{R}}^{p \times p}$, $W_{2} \in {\mathbb{R}}^{q \times q}$, and $t \in {\mathbb{R}}^{pq}$, where ${\mathbf{v}\mathbf{e}\mathbf{c}}{(S)}$ returns the columns of $S$ stacked as a single vector. The transformation of this problem into standard form is straightforward.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Problem instances", "weight": 1.0} -->

We set $M = {\hat{L} + \hat{S}}$ where $\hat{L}$ was a randomly generated rank-$r$ matrix and $\hat{S}$ was a sparse matrix with approximately $10\%$ nonzero entries. For all instances, we set $\mu$ to be equal to the sum of absolute values of the entries of $\hat{S}$ and generated the data with $r = 10$. For simplicity, we chose the matrices to be square, i.e., $p = q$, for all instances.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Results", "weight": 1.0} -->

The results are summarized in Table 3. On the two larger examples, SDPT3 and Sedumi both ran out of memory, so we cannot directly measure the suboptimality of the SCS solution. However, the reconstruction error where $\hat{L}$ is the true low-rank matrix used to generate the data and $L$ is the estimate returned by our algorithm, was less than $3 \times 10^{- 4}$ across all instances. Since this is the actual metric of interest in applications, this implies that the solutions returned were more than adequate.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Results", "weight": 1.0} -->

In this example the direct, indirect, and indirect GPU implementations of SCS take roughly the same amount of time. This is because the time required to project onto the semidefinite cone is the dominant cost per iteration (for the medium and large problems), rather than the linear system solve. std. form variables n std. form constraints m total solve time total solve time total solve time total solve time SCS indirect GPU: total solve time Table 3: Results for the robust PCA example.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Logistic Regression with $\\ell_{1}$-Regularization", "weight": 1.0} -->

In logistic regression the goal is to find the maximum likelihood fit of a logistic model to (binary) labeled data (BV:04 Sect. 7.1.1). In this problem we add an additional regularization term, which increases the sparsity of the solution. A fixed parameter $\mu \geq 0$ trades off the likelihood of the model and the model sparsity.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Problem instances", "weight": 1.0} -->

The data were generated as follows. First, we randomly selected a weights vector $w_{true} \in {\mathbb{R}}^{p}$ with at most $p/5$ of the entries nonzero. Then, each data point $z_{i}$ was sampled from a standard normal distribution and assigned a positive label with probability equal to the value of the logistic function applied to $w_{true}^{T}z_{i}$. For each instance we set $\mu = {0.1\mu^{\max}}$, where $\mu^{\max} = {{({1/2})}{\|{\sum_{i = 1}^{q}{y_{i}z_{i}}}\|}_{\infty}}$ is the smallest value of $\mu$ for which the solution to is zero.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Results", "weight": 1.0} -->

The results are summarized in table 4. Neither SDPT3 nor Sedumi can solve exponential cone programs, so we cannot make a direct comparison between SCS and the interior point solvers in this case. However, using CVX we can approximate an exponential cone program using a sequence of SDPs. With this technique SDPT3 is able to solve the smallest instance in a little under two hours, achieving an objective value of $3876.97$, a difference of less than $0.001\%$ when compared to SCS on the same problem. Despite this, SCS is able to solve the largest instance, with almost a billion nonzeros in the data matrix, in just a few hours using both direct and indirect solvers.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Results", "weight": 1.0} -->

In this example the sparsity pattern of the data matrix does not lend itself to efficient multi-threaded matrix multiplies when parallelizing over columns. Because of this the indirect method has little advantage over the direct method. The indirect method on the GPU is the fastest solver for the small and medium sized problems, but the GPU did not have enough memory to solve the large instance. std. form variables n std. form constraints m total solve time total solve time SCS indirect GPU: total solve time Table 4: Results for the ℓ1-regularized logistic regression example.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Random Cone Programs", "weight": 1.0} -->

In this subsection we describe how to generate a feasible bounded random cone program with known optimal objective value, given problem dimensions $n$ and $m$ and cone $\mathcal{K}$, and present SCS performance results on three random SOCPs. The procedure simultaneously generates the data $(A,b,c)$ and a primal-dual solution $(x^{\star},s^{\star},y^{\star})$. The solution need not be unique, so we do not expect to recover $(x^{\star},s^{\star},y^{\star})$; we do expect to recover nearly primal and dual feasible points with nearly the same objective value.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Random Cone Programs", "weight": 1.0} -->

First, we generate a random vector $z \in {\mathbb{R}}^{m}$ and set $s^{\star} = {\Pi_{\mathcal{K}}{(z)}}$ and $y^{\star} = {s^{\star} - z}$. This ensures conic feasibility, complementary slackness, and a zero duality gap by Moreau. Next we randomly generate the data matrix $A \in {\mathbb{R}}^{m \times n}$, with any desired sparsity pattern, and randomly generate the primal solution $x^{\star} \in {\mathbb{R}}^{n}$. Finally, we set $b = {{Ax^{\star}} + s^{\star}}$ and $c = {- {A^{T}y^{\star}}}$, which ensures equality constraint feasibility. The solution to the problem is not necessarily unique, but the optimal value is given by $c^{T}x^{\star}$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Random Cone Programs", "weight": 1.0} -->

A similar procedure can be used to generate infeasible or unbounded random cone programs by simultaneously generating the problem data and a certificate of primal or dual infeasibility. However, it is not as easy to ensure that the data matrix is sparse in those cases.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Random Cone Programs", "weight": 1.0} -->

We use this method to generate three SOCPs of different sizes. The data matrix $A$ was generated by selecting the nonzero entries uniformly at random, and generating the nonzero values by sampling from a standard normal distribution. Even the small instance is large; the large instance involves more than 100Gb of data, and is extremely large. We used the indirect linear system solver to solve these three problem instances.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Results", "weight": 1.0} -->

The results are given in table 5. The results indicate that even very large problems can be solved to modest accuracy with just a few thousand applications of the data matrix and its adjoint. total solve time total matrix multiplies Table 5: Results for randomly generated cone programs.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We presented an algorithm that can return primal and dual optimal points for convex cone programs when possible, and certificates of primal or dual infeasibility otherwise. The technique involves applying an operator splitting method, the alternating direction method of multipliers, to the homogeneous self-dual embedding of the original optimization problem. This embedding is a feasibility problem that involves finding a point in the intersection of an affine set and a convex cone, and each iteration of our method solves a system of linear equations and projects a point onto the cone. We showed how these individual steps can be implemented efficiently and are often amenable to parallelization. We discuss methods for automatic problem scaling, a critical step in making the method robust.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Conclusions", "weight": 1.0} -->

We provide a reference implementation of our algorithm in C, which we call SCS. We show that this solver can solve large instances of cone problems to modest accuracy quickly and is particularly well suited to solving large cone problems outside of the reach of standard interior-point methods. As far as we know, the problems reported in Sect. 6.6 are the largest general purpose cone problems solved to date.
