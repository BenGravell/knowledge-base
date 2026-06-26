<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Fast and Certifiable Trajectory Optimization

Topics include Semidefinite programming, Nonconvex optimization, Trajectory optimization, Robotics, Vehicles, Real-time systems, Optimization, STROM, PSD.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose semidefinite trajectory optimization (STROM), a framework that computes fast and certifiably optimal solutions for nonconvex trajectory optimization problems defined by polynomial objectives and constraints. STROM employs sparse second-order Lasserre's hierarchy to generate semidefinite program (SDP) relaxations of trajectory optimization. Different from existing tools (e.g., YALMIP and SOSTOOLS in Matlab), STROM generates chain-like multiple-block SDPs with only positive semidefinite (PSD) variables. Moreover, STROM does so two orders of magnitude faster. Underpinning STROM is cuADMM, the first ADMM-based SDP solver implemented in CUDA and runs in GPUs (with C/C++ extension). cuADMM builds upon the symmetric Gauss-Seidel ADMM algorithm and leverages GPU parallelization to speedup solving sparse linear systems and projecting onto PSD cones.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In five trajectory optimization problems (inverted pendulum, cart-pole, vehicle landing, flying robot, and car back-in), cuADMM computes optimal trajectories (with certified suboptimality below 1%) in minutes (when other solvers take hours or run out of memory) and seconds (when others take minutes). Further, when warmstarted by data-driven initialization in the inverted pendulum problem, cuADMM delivers real-time performance: providing certifiably optimal trajectories in 0.66 seconds despite the SDP has 49,500 variables and 47,351 constraints.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Trajectory optimization designs dynamical system trajectories by optimizing a performance measure subject to constraints, finding extensive applications in motion planning of robotic, aerospace, and manufacturing systems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Let $N$ be the number of steps (with ${\lbrack N\rbrack}:={\{ 1,\ldots,N\}}$), ${\{ x_{k}\}}_{k = 0}^{N} \subset {\mathbb{R}}^{d_{x}}$ be the state trajectory, and ${\{ u_{k}\}}_{k = 0}^{N - 1} \subset {\mathbb{R}}^{d_{u}}$ be the control trajectory, we consider the following trajectory optimization problem: where ${{l_{k},k} = 0},{\ldots,N}$ are the instantaneous and terminal loss functions; $x_{\text{init}}$ is the initial state; $F_{k}$ represents the discretized system dynamics in the form of a differential algebraic equation (*e.g.,* obtained from the continuous-time dynamics via multiple shooting, *cf.* Example 1 ‣ 2 Sparse Moment Relaxation ‣ Fast and Certifiable Trajectory

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimization") and §5); and $\mathcal{C}_{k}$ imposes constraints on $u_{k - 1}$ and $x_{k}$ (*e.g.,* control limits, obstacle avoidance).

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Trajectory optimization computes open-loop control; when paired with receding horizon control (*i.e.,* execute only part of the optimal control sequence and repeatedly solve), leads to closed-loop control with implicit feedback known as *model predictive control* (MPC). In the case of linear system dynamics, (convex) quadratic losses, and polytopic sets, problem reduces to a quadratic program, *i.e.,* constrained linear quadratic regulator (LQR).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we assume $l_{k}$ and $F_{k}$ are polynomial functions and $\mathcal{C}_{k}$ are basic semialgebraic sets (*i.e.,* described by polynomial constraints), in which case problem is an instance of *polynomial optimization* (POP) that is nonconvex and NP-hard in general. We briefly review solution methods for problem.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Local Solver. Most efforts over the past decades have focused on developing solvers that efficiently find local solutions, such as iterative LQR, differential dynamic programming, sequential quadratic programming and other nonlinear programming algorithms. Recent efforts design local solvers on GPUs, embedded systems, and make them end-to-end differentiable. Despite success in numerous applications, local solvers can get stuck in bad local minima and heavily rely on high-quality initial guesses, which require significant engineering heuristics and can be difficult to obtain.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Global Solver. Under restrictive conditions (*e.g.,* global optimality attained in the convex hull of the feasible set), problem can be equivalently solved as a convex optimization problem, known as lossless convexification. Further, if the only nonconvexity is combinatorial and can be modelled by integer variables (*e.g.,* in graph of convex neighbors/sets ), then problem can be solved by off-the-shelf mixed-integer programming solvers, albeit the runtime is worst-case exponential. We focus on generic nonconvex trajectory optimization whose nonconvexity is not combinatorial and cannot be losslessly convexified.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

Certifiable Solver. A generic recipe to design polynomial-time algorithms for solving nonconvex optimization while offering strong performance guarantees is through *convex relaxation*, where a relaxed convex problem is solved to provide a *lower bound* and a feasible solution of the nonconvex problem provides an *upper bound*. The relative error between the lower and upper bounds provides a *certificate of (sub)optimality* (to be made precise in ). Lasserre's moment and sums-of-squares (SOS) hierarchy --relaxing a polynomial optimization as a hierarchy of convex *semidefinite programs* (SDPs) of increasing size-- is arguably the method of choice for designing convex relaxations, as it guarantees a certificate of suboptimality that converges to zero (then the relaxation is called *tight* or *exact*). Khadir *et al.* applied the moment-SOS hierarchy to compute shortest piece-wise linear paths among obstacles without considering robot dynamics.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

Teng *et al.* explored the Markovian property of dynamical systems and applied a *sparse* variant of the moment-SOS hierarchy to trajectory optimization and observed the *second-order* SDP relaxation is empirically tight, echoing similar findings in perception. Huang *et al.* proposed sparse SDP relaxations with homogenization to allow unbounded feasible sets and solved simple trajectory optimization problems with *tight* *second-order* relaxation.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

Computational Challenges. Despite the ability to compute *certifiably optimal* trajectories, the second-order (and higher) moment-SOS relaxation is notoriously expensive to solve, rendering its practicality in robotics questionable.^11^1Tackling the second-order relaxation is necessary, because the first-order relaxation, unfortunately, is very loose in trajectory optimization, see and §0.B. Indeed the commercial solver mosek is chosen to solve SDPs due to its robustness and high accuracy. However, as a generic-purpose implementation of the interior point method, mosek has three drawbacks. (*i*) mosek has poor scalability due to high memory complexity and per-iteration time complexity. Even for small-scale problems like minimum-work block-moving and inverted pendulum (*cf.* §5), mosek's runtime is around 10 seconds. As problems get larger (*cf.* examples in and §5), it easily takes runtime in the order of hours and goes out of memory.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

(*ii*) mosek cannot be warmstarted, which means its runtime online cannot be reduced even if many similar problems have been solved offline (*e.g.,* in an MPC setup ). (*iii*) It does not fully exploit the special structure in SDPs generated from sparse moment-SOS relaxations.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

*Can the moment-SOS hierarchy ever be practical for trajectory optimization?* We believe the answer is affirmative if and only if one can design a customized SDP solver that is scalable, exploits problem structures, and can be warmstarted.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Contributions. We present STROM (semidefinite trajectory optimization), a fast and certifiable trajectory optimization framework that checks the merits.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

Faster sparse moment relaxation. Unlike existing tools in Matlab such as sostools and yalmip that generate sparse second-order SDP relaxations of problem from the dual SOS perspective, we develop a C++ tool to generate SDP relaxations from the *primal moment* perspective. Our POP-SDP conversion reveals the special *chain-like sparsity pattern* in the relaxed multiple-cone SDP (*cf.* Fig. 1). It is two orders of magnitude faster than yalmip and sostools, and on par with the Julia package tssos.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Introduction", "weight": 1.5} -->

Algorithmic backbone: sGS-ADMM. We choose the *symmetric Gauss-Seidel ADMM* (sGS-ADMM) as the algorithmic backbone to design a scalable SDP solver that can be warmstarted. As a first-order method, sGS-ADMM inherits low per-iteration cost from ADMM and offers empirical advantages in solving degenerate SDPs from high-order relaxations.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Introduction", "weight": 1.5} -->

GPU speedup: cuADMM. At each iteration, sGS-ADMM alternates between (a) performing projection onto positive semidefinite (PSD) cones, and (b) solving sparse linear systems. Due to the existence of many small-to-medium-scale PSD cones in the SDP relaxation, we engineer a highly optimized GPU-based implementation of sGS-ADMM in CUDA, named cuADMM and achieves up to $10 \times$ speedup compared to existing ADMM solvers such as cdcs and sdpnal+. cuADMM is the first ADMM-based SDP solver that runs in GPUs and we demonstrate its ability to solve five trajectory optimization applications (inverted pendulum, cart-pole, vehicle landing, flying robot, and car back-in with obstacle avoidance): cuADMM solves them with optimality certificates (suboptimality below $1\%$) in minutes (when other solvers take hours and run out of memory) and seconds (when others take minutes).

<!-- chunk {"id": "body-0020", "role": "body", "section": "Introduction", "weight": 1.5} -->

Data-driven initialization: real-time certifiable optimization. To show the potential to warmstart cuADMM, we perform a case study in inverted pendulum: using a vanilla $k$-nearest neighbor search to initialize cuADMM. The result is the first certifiably optimal swing-up of the pendulum computed in subseconds (*i.e.,* $0.66$ seconds with a below $1\%$ optimality certificate).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Introduction", "weight": 1.5} -->

Organization. We present sparse moment relaxation in §2, sGS-ADMM in §3, and cuADMM in §4. We give numerical experiments in §5 and conclude in §6.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Sparse Moment Relaxation", "weight": 1.0} -->

We first introduce a special type of sparsity in polynomial optimization known as *chain-like* sparsity and show that problem satisfies this pattern (§2.1). We then present the sparse moment-SOS hierarchy (§2.2), followed by how to convert it to a standard semidefinite program (SDP) (§2.3).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Sparse Moment Relaxation", "weight": 1.0} -->

To provide a tutorial-style exposition of the mathematical machinery, we use a toy trajectory optimization problem as the running example.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Example 1 (Trajectory Optimization of A 1-D Nonlinear System)", "weight": 1.0} -->

Consider the nonlinear dynamical system adapted: Starting from $x_{\text{init}} = 2$, our goal is to regulate (2 ‣ 2 Sparse Moment Relaxation ‣ Fast and Certifiable Trajectory Optimization")) towards $x = 0$. We define a trajectory optimization problem with standard direct multiple shooting: where $P_{f} > 0$ is the terminal loss coefficient and $\Delta t$ is the time step size. $▲$

<!-- chunk {"id": "body-0025", "role": "body", "section": "Polynomial Optimization with Chain-like Sparsity", "weight": 1.0} -->

A chain-like sparsity pattern is a special case of the correlative sparsity pattern. Correlative sparsity corresponds to the variables of a POP forming a chordal graph; chain-like sparsity corresponds to a chain (or line) graph.

<!-- chunk {"id": "body-0026", "role": "body", "section": "The Sparse Moment-SOS Hierarchy", "weight": 1.0} -->

Associated with every vector space (of points) is its dual vector space of linear functionals. Viewing ${\mathbb{R}}{\lbrack z\rbrack}_{n}$ as a vector space (which is isomorphic to ${\mathbb{R}}^{s{(d,n)}}$ after fixing the basis ${\lbrack z\rbrack}_{n}$), its dual vector space ${{\mathbb{R}}{\lbrack z\rbrack}_{n}^{\ast}} \cong {\mathbb{R}}^{s{(d,n)}}$ contains linear functionals of polynomials.

<!-- chunk {"id": "body-0027", "role": "body", "section": "The Sparse Moment-SOS Hierarchy", "weight": 1.0} -->

Particularly, given a sequence of numbers $\varphi = {(\varphi_{\alpha})} \in {\mathbb{R}}^{s{(d,n)}}$ indexed by the (exponents of) monomials in ${\lbrack z\rbrack}_{n}$, we define a one-to-one linear map from ${\mathbb{R}}{\lbrack z\rbrack}_{n}$ to $\mathbb{R}$, known as the *Riesz linear functional* We can easily extend the notation of $\ell_{\varphi}$ from polynomials to polynomial vectors and matrices, as shown in the following example.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Example 2 (Riesz Functional)", "weight": 1.0} -->

Let ${d = 3},{I_{1} = \left\{ 2,3 \right\}}$. Then, $\lbrack z\rbrack_{1} = {\lbrack 1;z_{1};z_{2};z_{3}\rbrack}$ and $\left\lbrack {z{(I_{1})}} \right\rbrack_{2} = {\lbrack 1;z_{2};z_{3};z_{2}^{2};{z_{2}z_{3}};z_{3}^{2}\rbrack}$. Setting $n = 3$, we have where the application of $\ell_{\varphi}$ is element-wise. $▲$ We are ready to present the sparse moment-SOS hierarchy for the POP (5 ‣ 2.1 Polynomial Optimization with Chain-like Sparsity ‣ 2 Sparse Moment Relaxation ‣ Fast and Certifiable Trajectory Optimization")).

<!-- chunk {"id": "body-0029", "role": "body", "section": "Faster Conversion to Standard SDP", "weight": 1.0} -->

Solving the moment relaxation (10 ‣ 2.2 The Sparse Moment-SOS Hierarchy ‣ 2 Sparse Moment Relaxation ‣ Fast and Certifiable Trajectory Optimization")) is typically done by converting (10 ‣ 2.2 The Sparse Moment-SOS Hierarchy ‣ 2 Sparse Moment Relaxation ‣ Fast and Certifiable Trajectory Optimization")) into a standard linear conic optimization problem in the format of sedumi or mosek. The standard way to convert (10 ‣ 2.2 The Sparse Moment-SOS Hierarchy ‣ 2 Sparse Moment Relaxation ‣ Fast and Certifiable Trajectory Optimization")) into a conic program follows \[76, §5.7.1\] (*e.g.,* as in tssos, sostools, yalmip), which will generate a conic program with not only PSD variables but also free (unconstrained) variables.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Faster Conversion to Standard SDP", "weight": 1.0} -->

We advocate for a different conversion standard \[76, §5.7.2\] that generates *only* PSD variables and the resulting semidefinite program admits the same chain-like structure as the POP (*cf.* Fig. 1).

<!-- chunk {"id": "body-0031", "role": "body", "section": "Faster Conversion to Standard SDP", "weight": 1.0} -->

Focusing on the sparse moment relaxation (10 ‣ 2.2 The Sparse Moment-SOS Hierarchy ‣ 2 Sparse Moment Relaxation ‣ Fast and Certifiable Trajectory Optimization")), denote as the tuple of all moment and localizing matrices, which lives in a vector space $\Omega$ that is the Cartesian product of ${\{{\mathbb{S}}^{s{({|I_{k}|},\kappa)}}\}}_{k \in {\lbrack N\rbrack}}$ and ${\{{\mathbb{S}}^{s{({|I_{k}|},{\kappa - d_{k,i}^{g}})}}\}}_{{k \in {\lbrack N\rbrack}},{i \in \mathcal{G}_{k}}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Faster Conversion to Standard SDP", "weight": 1.0} -->

Let $\Omega_{+} \subset \Omega$ be the cone containing tuples $X$ whose elements are PSD, we claim the moment relaxation (10 ‣ 2.2 The Sparse Moment-SOS Hierarchy ‣ 2 Sparse Moment Relaxation ‣ Fast and Certifiable Trajectory Optimization")) can be written as a standard multi-block SDP for some $b \in {\mathbb{R}}^{m}$, $C \in \Omega$ and linear map ${\mathcal{A}{(X)}}:={(\left\langle A_{i},X \right\rangle)}_{i \in {\lbrack m\rbrack}}$ with $A_{i} \in \Omega$. The inner product in the space $\Omega$ is defined element-wise.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Faster Conversion to Standard SDP", "weight": 1.0} -->

Without detailing the conversion from (10 ‣ 2.2 The Sparse Moment-SOS Hierarchy ‣ 2 Sparse Moment Relaxation ‣ Fast and Certifiable Trajectory Optimization")) to in full generality (which we implement in C++), we present the high-level idea using Example (3 ‣ 2 Sparse Moment Relaxation ‣ Fast and Certifiable Trajectory Optimization")).

<!-- chunk {"id": "body-0034", "role": "body", "section": "Faster Conversion to Standard SDP", "weight": 1.0} -->

Linear Objective $\left\langle C,X \right\rangle$. Recall the $k$-th clique contains variables ${z{(I_{k})}} = {(x_{k - 1},u_{k - 1},x_{k})}$. Set $k = 2$, with relaxation order $\kappa = 2$, the moment matrix (recall it is symmetric and hence we only write the upper triangular part) has rows (columns) indexed by ${\lbrack{z{(I_{2})}}\rbrack}_{2}$, *i.e.,* the vector of monomials in $z{(I_{2})}$ of degree up to $2$ (the first row in).

<!-- chunk {"id": "body-0035", "role": "body", "section": "Faster Conversion to Standard SDP", "weight": 1.0} -->

Clearly, $M_{2}$ contains the monomials in $z{(I_{2})}$ of degree up to $4$, and hence the objective $f_{2}{({z{(I_{2})}})}$, a polynomial of degree $2$, can be written as $\left\langle C_{2},M_{2} \right\rangle$ for some matrix $C_{2}$. This procedure can be done for every $k \in {\lbrack N\rbrack}$, thus, the objective of (3 ‣ 2 Sparse Moment Relaxation ‣ Fast and Certifiable Trajectory Optimization")) can be written as $\sum_{k = 1}^{N}\left\langle C_{k},M_{k} \right\rangle$, or compactly $\left\langle C,X \right\rangle$ (recall $X$ contains all moment matrices).

<!-- chunk {"id": "body-0036", "role": "body", "section": "Faster Conversion to Standard SDP", "weight": 1.0} -->

Moment constraints $\mathcal{A}_{\text{mom}}$. Due to the definition of the moment matrix $M_{k}$ (10c ‣ 2.2 The Sparse Moment-SOS Hierarchy ‣ 2 Sparse Moment Relaxation ‣ Fast and Certifiable Trajectory Optimization")), a single monomial can appear multiple times. For example, we have ${M_{2}{}} = {M_{2}{}} = {M_{2}{}}$ (highlighted in blue).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Faster Conversion to Standard SDP", "weight": 1.0} -->

Inequality constraints $\mathcal{A}_{\text{ineq}}$. Each element in $L_{k,i}$ can be expressed as a linear combination of elements in $M_{k}$. For example (3 ‣ 2 Sparse Moment Relaxation ‣ Fast and Certifiable Trajectory Optimization")), we can write down the localizing matrix generated by the inequality constraint ${1 - u_{1}^{2}} \geq 0$: and observe the linear constraints which can be repeated for every entry of $L_{2,1}$.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Faster Conversion to Standard SDP", "weight": 1.0} -->

Equality constraints $\mathcal{A}_{\text{eq}}$. Each linear constraint in (10e ‣ 2.2 The Sparse Moment-SOS Hierarchy ‣ 2 Sparse Moment Relaxation ‣ Fast and Certifiable Trajectory Optimization")) can be expressed by a linear combination of elements in $M_{k}$. For example, the linear constraints generated from ${h_{2,1}{({z{(I_{2})}})}} = 0$ are: which leads to $10$ linear constraints in $\mathcal{A}_{\text{eq}}$. The first one of them is which leads to the constraint Consensus constraints $\mathcal{A}_{\text{sen}}$. Since $I_{k}$ and $I_{k + 1}$ have overlapping elements, two adjacent moment matrices $M_{k}$ and $M_{k + 1}$ also have overlapping elements.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Faster Conversion to Standard SDP", "weight": 1.0} -->

For example (3 ‣ 2 Sparse Moment Relaxation ‣ Fast and Certifiable Trajectory Optimization")), we can write down the third moment matrix and observe that $M_{2}$ and $M_{3}$ share the same monomials highlighted in red: In summary, our conversion generates an SDP whose structure is illustrated on the right-hand side of Fig. 1, where the solid lines connect two PSD variables if and only if there exist linear constraints between them. In §0.D, we show our conversion package is the only one capable of real-time conversion in Matlab, compared to sostools and yalmip.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Algorithmic Backbone: sGS-ADMM", "weight": 1.0} -->

Solving the SDP using interior point solvers does not scale to practical trajectory optimization problems. We introduce the scalable sGS-ADMM algorithm.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Algorithmic Backbone: sGS-ADMM", "weight": 1.0} -->

Consider as the primal SDP. Let $y \in {\mathbb{R}}^{m}$ and denote $\mathcal{A}^{\ast}$ as the adjoint of $\mathcal{A}$ defined as ${\mathcal{A}^{\ast}y}:={\sum_{l \in {\lbrack m\rbrack}}{y_{l}A_{l}}}$. The Lagrangian dual of reads: sGS-ADMM can be seen as a semi-proximal ADMM method applied to the Augmented Lagrangian of. Without going deep into the theory, and denoting $\Pi_{\Omega_{+}}{(\cdot)}$ as the projection onto $\Omega_{+}$, we present sGS-ADMM in Algorithm 1. Global convergence of sGS-ADMM for the SDP pair - is established.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Algorithmic Backbone: sGS-ADMM", "weight": 1.0} -->

From Algorithm 1, we see two main computational tasks are solving linear systems with a fixed coefficient matrix $\mathcal{A}\mathcal{A}^{\ast}$ and computing the projection of a sequence of symmetric matrices onto the PSD cone. As we shall see in §4, these two tasks can be implemented efficiently in GPUs, resulting in significant speedups.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Algorithmic Backbone: sGS-ADMM", "weight": 1.0} -->

Terminal Conditions. We terminate Algorithm 1 if either of the following two terminal conditions are met: The maximum iteration number maxiter is reached. The standard max KKT residual $\eta:={\max\left\{ \eta_{p},\eta_{d},\eta_{g} \right\}}$ is below a certain threshold tol, where $\eta_{p},\eta_{d},\eta_{g}$ are defined as: Refined Certificate of Suboptimality. Unlike mosek, which can solve the KKT residual $\eta$ to machine precision and compute $p_{\kappa}^{\star}$ exactly for estimating the certificate of suboptimality, first-order methods can only achieve moderate accuracy ($\eta$ around $10^{- 3}$ to $10^{- 5}$) in our setting. Therefore, given an output triplet $(X,y,S)$ from Algorithm 1, we need to generate a valid lower bound of $p^{\star}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Algorithmic Backbone: sGS-ADMM", "weight": 1.0} -->

Given any $z \in {\mathbb{R}}^{d}$, define the rank-1 lifting operator at relaxation order $\kappa$: Let $X{(z)}$ be the aggregation of $M_{k}{(z)}$ and $L_{k,i}{(z)}$. Denote $\hat{z}$ as any feasible solution for the POP (5 ‣ 2.1 Polynomial Optimization with Chain-like Sparsity ‣ 2 Sparse Moment Relaxation ‣ Fast and Certifiable Trajectory Optimization")) such that ${\mathcal{A}{({X{(\hat{z})}})}} = b$ naturally holds. Let $X_{\beta}$ be the $\beta$-th symmetric matrix in $X$. The following inequality holds for any feasible $\hat{z}$ if $R_{\beta} \geq {{tr}\left({X{(\hat{z})}_{\beta}} \right)}$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Algorithmic Backbone: sGS-ADMM", "weight": 1.0} -->

Since $\hat{z}$ can be arbitrarily picked, we have The suboptimality gap $\xi$ is refined as: where the only difference from is the lower bound in (29c) is used instead of $p_{\kappa}^{\star}$. The feasible $\hat{z}$ is obtained with the extraction method presented in §2.2.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Algorithmic Backbone: sGS-ADMM", "weight": 1.0} -->

The certificate holds if an upper bound $R_{\beta}$ exists for the trace of each $X{(\hat{z})}_{\beta}$. We prove the existence of $R_{\beta}$ in §0.C ‣ Fast and Certifiable Trajectory Optimization").

<!-- chunk {"id": "body-0047", "role": "body", "section": "GPU Speedup: cuADMM", "weight": 1.0} -->

We now implement Algorithm 1 in C++ and CUDA. We will assume (*i*) relaxation order $\kappa = 2$; (*ii*) each clique has the same size, *i.e.,* ${|I|} = {|I_{1}|} = \cdots = {|I_{N}|}$; (*iii*) each polynomial inequality constraint is of degree $1$ or $2$, *i.e.,* ${d_{k,i}^{g} = 1},{{{\forall k} \in \lbrack N\rbrack},{i \in \mathcal{G}_{k}}}$. These assumptions hold for all applications considered in this paper. sGS-ADMM in Algorithm 1 involves three primary operations: (a) performing sparse matrix and dense vector multiplications (*cf.*), (b) solving sparse linear systems (*cf.* and), and (c) projecting onto the Cartesian product of multiple PSD cones (*cf.*).

<!-- chunk {"id": "body-0048", "role": "body", "section": "GPU Speedup: cuADMM", "weight": 1.0} -->

For (a), we sort matrix variables and linear constraints by clique indices. $X$ is stored by concatenating the symmetric vectorizations (svec) of $M_{k}$ and $L_{k,i}$. These arrangements ensure $\mathcal{A}$ and $\mathcal{A}^{\ast}$ exhibit low bandwidth and good locality during sparse matrix-dense vector multiplications. On GPUs, we use cuSPARSE for these operations.

<!-- chunk {"id": "body-0049", "role": "body", "section": "GPU Speedup: cuADMM", "weight": 1.0} -->

Hybrid Sparse Linear System Solver. For (b), we run sparse Cholesky decomposition with pre-permutation on $\mathcal{A}\mathcal{A}^{\ast}$ at the beginning and only once. Since $\mathcal{A}$ may be ill-conditioned, we add $\mathcal{A}\mathcal{A}^{\ast}$ by a scaled identity matrix $\epsilon I$ (with $\epsilon$ a small positive number) to enforce positive definiteness: Then, we can efficiently solve sparse triangular linear systems in and: $P$ is a permutation matrix whose multiplication with dense vectors can be done in parallel. Thus, we implement $w\leftarrow{P^{\mathsf{T}}r_{s}}$ and $y\leftarrow{Pw}$ on GPUs as 1-D reorderings.

<!-- chunk {"id": "body-0050", "role": "body", "section": "GPU Speedup: cuADMM", "weight": 1.0} -->

$w\leftarrow{\left({LDL^{\mathsf{T}}} \right)^{- 1}w}$ is not parallelizable, so we call CHOLMOD's $LDL^{\mathsf{T}}$ solver in CPU. This hybrid approach is approximately $4$ times faster than solving two sparse triangular systems on a GPU with cuSPARSE, and $10\%$ faster than performing two permutations on a CPU, even with the GPU-CPU transfer overhead. The hybrid linear system solver is depicted in Fig. 2 left side.

<!-- chunk {"id": "body-0051", "role": "body", "section": "GPU Speedup: cuADMM", "weight": 1.0} -->

For the moment relaxation (10 ‣ 2.2 The Sparse Moment-SOS Hierarchy ‣ 2 Sparse Moment Relaxation ‣ Fast and Certifiable Trajectory Optimization")), the number of moment matrices is $N$ and localizing matrices is $\sum_{k \in {\lbrack N\rbrack}}{|\mathcal{G}_{k}|}$. The size of the moment matrices is fixed at $s{({|I|},2)}$, and the size of the localizing matrices is fixed at $s{({|I|},1)}$. Based on two observations: $N \ll {\sum_{k \in {\lbrack N\rbrack}}{|\mathcal{G}_{k}|}}$ and ${s{({|I|},2)}} \gg {s{({|I|},1)}}$, we choose different eigenvalue decomposition routines for moment and localizing matrices.

<!-- chunk {"id": "body-0052", "role": "body", "section": "GPU Speedup: cuADMM", "weight": 1.0} -->

For localizing matrices, we use the batched-matrix eig interface with the Jacobi method in cuSOLVER, which is faster when the number of matrices is large and the matrix size is small. For moment matrices, we employ the single-matrix eig in cuSOLVER with the direct QR method and parallelize operations using multiple CUDA streams. Empirically in a single GPU, this approach is $10\%$ to $20\%$ faster than wrapping all moment matrices into the batched eig. If multiple GPUs are available, we distribute moment matrices for eig since this step dominates the runtime in Algorithm 1. After eigenvalue decomposition, we employ a mixture of custom kernel functions and batched matrix multiplication operators in cuBLAS to perform batched projection.

<!-- chunk {"id": "body-0053", "role": "body", "section": "GPU Speedup: cuADMM", "weight": 1.0} -->

Moreover, we frequently split $X$ in svec form to two batched matrix sequences ${\{ M_{k}\}}_{k \in {\lbrack N\rbrack}}$ and ${\{ L_{k,i}\}}_{{k \in {\lbrack N\rbrack}},{i \in \mathcal{G}_{k}}}$, and vice versa. Fast parallel mappings are implemented to minimize the cost. The parallel PSD cone projection is depicted in the right part of Fig. 2.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Experiments", "weight": 1.0} -->

General Setup. We consider five trajectory optimization problems: inverted pendulum, cart-pole, vehicle landing, flying robot, and car back-, as illustrated in Fig. 3. We rescale all polynomial variables and coefficients to $\lbrack{- 1},1\rbrack$ before moment relaxation for numerical stability. We unify the loss function design as the LQR-style loss, *i.e.,* denote the final state as $x_{f}$, the loss function (1a) is where $Q_{x}$ and $Q_{u}$ are designed to be identity matrices after rescaling.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Experiments", "weight": 1.0} -->

(a) Pendulum (b) Cart-pole (c) Landing (d) Flying robot (e) Car back-in Figure 3: Five trajectory optimization problems of dynamical systems.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Experiments", "weight": 1.0} -->

Baselines. For interior point methods, we choose the commercial solver mosek as our baseline. For first-order methods, we choose the state-of-the-art general SDP solvers cdcs and sdpnal+.^33^3We have tested scs but found its Matlab version to always generate wrong results for multiple-block SDP problems. We only use the ADMM solver in sdpnal+ because the semismooth Newton solver is not scalable. For first-order methods, tol is set as $10^{- 4}$ in Algorithm 1.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Experiments", "weight": 1.0} -->

Experiments were conducted on a high-performance workstation equipped with a 2.7 GHz AMD 64-Core sWRX8 Processor, two 2.5 GHz NVIDIA RTX 6000 Ada Generation GPUs, and 1 TB of RAM, to enable mosek to solve large-scale problems (with 64 CPU threads). In cuADMM, we set up 15 CUDA streams per GPU for eigenvalue decomposition of moment matrices. The suboptimality gap $\xi$ is defined, where $\hat{z}$ is obtained from the extraction method presented in §2.2 with Matlab fmincon as the local solver. We only report runtime of SDP solvers because the runtime of local solvers is negligible compared to the convex SDP solver, and better CPU and GPU local solvers are available, whose design is beyond the scope of this paper.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Experiments", "weight": 1.0} -->

Summary Results. For the pendulum problem, we tested the performance of four SDP solvers on 100 initial states generated by a dense grid. For the other four experiments, we assessed cuADMM's performance on 10 randomly generated initial states. Due to the significantly longer solving times of the other three solvers, we evaluated their performance on only one random initial state that cuADMM could solve, with a maximum running time set at 5 hours. Table 1 presents the problem scale, suboptimality gaps, and total running times.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Experiments", "weight": 1.0} -->

It shows that the mean and median suboptimality gaps from cuADMM are either well below $10^{- 2}$ (in all cases except for the car back-in) or near $10^{- 2}$ (for the car back-in); mosek can solve the pendulum and cart-pole problems very well, but cannot scale to other problems; Compared with other ADMM-based solvers, cuADMM achieves up to $10 \times$ speedup in large-scale SDP problems (with $m > {5 \times 10^{5}}$); In fact, the other ADMM solvers cannot produce $< {1\%}$ suboptimality certificates with the time presented in Table 1; With warmstart techniques, cuADMM can solve the pendulum problem to global optimality with an average cost of 0.66 seconds. We only list cuADMM and sdpnal+'s warm start results since cdcs does not support explicit initial guesses.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Experiments", "weight": 1.0} -->

#M

<!-- chunk {"id": "body-0061", "role": "body", "section": "Experiments", "weight": 1.0} -->

Detailed experimental results and analyses are presented in §0.E. *We encourage the reader to check out videos of the certifiably optimal trajectories computed by cuADMM on our project website*. Due to limited space, in the next we briefly analyze three examples out of five: pendulum, car back-, and flying robot.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Experiments", "weight": 1.0} -->

Inverted Pendulum. Denote pendulum's state as $(\theta,\overset{˙}{\theta})$, we first use the variational integrator to discretize the continuous-time dynamics on ${SO}{}$. See §0.E.1 for a detailed derivation of discretized dynamics and constraints.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Experiments", "weight": 1.0} -->

*Warmstarts with kNN*. To enable data-driven methods for warmstarts, we collect $60 \times 120$ mosek solutions in the state space ${(\theta,\overset{˙}{\theta})} \in {{\lbrack 0,\pi\rbrack} \times {\lbrack{- 5},5\rbrack}}$ off-line. Given a new initial state $(\theta_{0},{\overset{˙}{\theta}}_{0})$, we use Delaunay Triangulation to search for three nearest neighbors among the mosek's solutions. A convex combination of these three solutions is treated as the initial solution for cuADMM and sdpnal+.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Experiments", "weight": 1.0} -->

*Comparison with baselines*. In the state space ${(\theta,\overset{˙}{\theta})} \in {{\lbrack 0,\pi\rbrack} \times {\lbrack{- 5},5\rbrack}}$, we sample $10 \times 10$ initial states with a dense grid. Fig. 4 bottom shows the performance of different solvers. In almost all experiments, mosek achieved suboptimality gaps as low as $10^{- 7}$. Among the first-order solvers, cdcs struggled to get low dual infeasibility $\eta_{d}$, resulting in significantly higher suboptimality gaps. While sdpnal+ shows reliable performance, its per-iteration cost is $7$ times higher than cuADMM. With warmstarts, cuADMM solves the pendulum problem in less than $0.7$s on average, achieving $10 \times$ speedup compared to mosek. $10\%$ initial states are hard to solve for all solvers, which form a mysterious spiral line as discussed.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Experiments", "weight": 1.0} -->

*Model predictive control*. Fig. 4 top shows a simulated MPC case starting from ${\theta_{0} = 0.1},{\overset{˙}{\theta} = 0.0}$. We set the control frequency as $10$Hz. In almost all time steps, the suboptimality gap is below $10^{- 2}$, and the average solving time is $0.72$s.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Experiments", "weight": 1.0} -->

Car Back-. In car back-, we try to back-up a car (represented as a rectangle) between two square obstacles. To enforce obstacle avoidance using polynomial constraints, we adopt the separating hyperplane method. Since the separating hyperplane is in general not unique, the moment matrices will not be rank-one. However, heuristic methods still exist to extract globally optimal trajectories, see all the details in §0.E.3. We randomly select $10$ initial states for four solvers to test their performance. We set the maximal running time to $1$ hour. Results are recorded in the top panel of Fig. 5. cuADMM is the only solver to finish all experiments in one hour and generate certifiable results ($\xi$ near $10^{- 2}$). The bottom panel of Fig. 5 shows three globally optimal trajectories.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Experiments", "weight": 1.0} -->

Flying Robot. In this experiment, we want to send a flying robot with four boosters to the origin. The vehicle has six continuous-time states: 2-D position $(x,y)$, 2-D velocity $(\overset{˙}{x},\overset{˙}{y})$, angular position $\theta$ and velocity $\overset{˙}{\theta}$. The discretization procedure is similar to the pendulum case. Fig. 6 shows two globally optimal trajectories. Note that cuADMM is the only solver capable of computing optimal trajectories in this problem (*cf.* Table 1).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We presented STROM, a new framework for fast and certifiable trajectory optimization. STROM contains two modules: a C++ package that generates sparse moment relaxations, and a first-order ADMM-based SDP solver cuADMM directly implemented in CUDA. Our C++ package is two orders of magnitude faster than existing Matlab packages, and our cuADMM solves large-scale SDPs far beyond the reach of existing solvers. Moreover, we demonstrated the potential of real-time certifiable trajectory optimization in inverted pendulum using data-driven warmstarts. Several directions are worth exploring in future works, such as moment-cone-specific conic solvers and differentiable ADMM for integration with deep learning. We believe the time is now to make Lasserre's moment-SOS hierarchy a practical computational tool for robotics.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Acknowledgments. We thank Tianyun Tang, Kim-Chuan Toh, Jie Wang and Jean B. Lasserre for discussion about trajectory optimization and moment-SOS hierarchy. We thank Xin Jiang for discussion about ADMM. We thank Brian Plancher and Emre Adabag for offering advice for CUDA programming.
