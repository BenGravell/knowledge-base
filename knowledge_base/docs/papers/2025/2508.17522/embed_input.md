<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Differentiating through a Quadratic Cone Program

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Quadratic cone programs are rapidly becoming the standard canonical form for convex optimization problems. In this paper we address the question of differentiating the solution map for such problems, generalizing previous work for linear cone programs. We follow a similar path, using the implicit function theorem applied to the optimality conditions for a homogenous primal-dual embedding. Along with our proof of differentiability, we present methods for efficiently evaluating the derivative operator and its adjoint at a vector. Additionally, we present an open-source implementation of these methods, named \texttt{diffqcp}, that can execute on CPUs and GPUs. GPU-compatibility is already of consequence as it enables convex optimization solvers to be integrated into neural networks with reduced data movement, but we go a step further demonstrating that \texttt{diffqcp}'s performance on GPUs surpasses the performance of its CPU-based counterpart for larger quadratic cone programs.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

A quadratic cone program (QCP) is an optimization problem which minimizes a convex quadratic function over the intersection of a subspace and a convex cone. Quadratic cone programming is the generalization of both quadratic programming and (linear) cone programming, which date to the 1950s and 1990s \[, Chapter 4\], respectively. Specifically, a quadratic program (QP) is a QCP whose cone is restricted to the product of $\{ 0\}$, R, and $\text{R}_{+}$, while a (linear) cone program is a QCP restricted to having a linear objective.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Quadratic programs, despite their limited modeling power, have been studied extensively as they arise ubiquitously across many disciplines---from classical engineering contexts to finance. Cone programming, on the other hand, has been studied for its generality---all convex optimization problems can be equivalently written as a cone program. Along with their rich theory, signficant development has gone into specialized solvers for both quadratic programs and cone programs. Moreover, domain specific languages, such as CVXPY and CVXR, have been designed to enable easy modeling with both classes of programs.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Perturbation and sensitivity analysis has also been thoroughly developed for QPs and cone programs. Clasically, this analysis centered on the Lagrange multipliers. In recent years, differentiable optimization---the derivative of the solution map between an optimization problem's parameters and its solution---has been developed. The gradients of the solution map of a quadratic program (with respect to the problem data) were derived by exploiting the problem structure. Subsequently, proposed a technique for differentiating the solution map of a cone program using a more general approach based on the implicit function theorem. Differentiable optimization has found applications across energy systems, statistics, control, and in neural networks.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In recent years, specialized solvers for QCPs have been developed and have demonstrated significant speedups on problems previously solved via cone programs or quadratic programs. As a result, QCPs are emerging as a practical alternative to cone programs for many convex optimization problems. Further, there has been success at GPU-accelerating these QCP solvers. However, the theory of differentiating the solution map of QCPs has remained undeveloped.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Our contribution", "weight": 1.0} -->

Closely following, we derive conditions for when the derivative, and its adjoint, of the primal-dual solution map to a QCP with respect to the QCP's parameters exists. We then present an extension to to evaluate Jacobian-vector and vector-Jacobian products with these derivatives via projection onto cones and sparse linear system solves. We then describe our GPU-accelerated Python implementation of this method in §, which forms the derivative of the solution map as an abstract linear operator. Additionally, in §A we present a unified reference of cone projection operators and their derivatives. Notably, this reference and our implementation includes the power cone, which has previously been neglected in the differentiable optimization literature.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Solution map and its derivative", "weight": 1.0} -->

Following, we consider the mapping from the numerical data defining the primal and dual problems of a QCP to its solutions. This solution map is in general set-valued, but in neighborhoods where it is single-valued it is an implicit function of the problem data. In the sequel, we present a system of equations that implicitly define the solution map of a QCP when it is single-valued. Applying the implicit function theorem to this system, we obtain regularity conditions on the problem data that guarantee when the solution map is single-valued and its derivative exists. Finally, we provide an expression for the derivative at points where these conditions are satisfied.

<!-- chunk {"id": "body-0009", "role": "body", "section": "QCPs and implicit functions", "weight": 1.0} -->

The primal and dual problems for a (convex) QCP are

<!-- chunk {"id": "body-0010", "role": "body", "section": "QCPs and implicit functions", "weight": 1.0} -->

where $x \in \text{R}^{n}$ is the primal variable, $y \in \text{R}^{m}$ is the dual variable, and $s \in \text{R}^{m}$ is the primal slack variable. We assume that $\mathcal{K} \subseteq \text{R}^{m}$ is a nonempty, closed, convex cone with dual cone $\mathcal{K}^{\ast}$. The problem data are $P \in \text{S}_{+}^{n}$, $A \in \text{R}^{m \times n}$, $q \in \text{R}^{n}$, and $b \in \text{R}^{m}$. (The convex cone can also be problem data, but for our purposes we fix $\mathcal{K}$.) To simplify the subsequent discussion, we define the set

<!-- chunk {"id": "body-0011", "role": "body", "section": "QCPs and implicit functions", "weight": 1.0} -->

That is, $\theta$ is the concatenation of problem data (relaxed to allow $P \nsucceq 0$)---a change which embeds the problem data into a skew-symmetric matrix.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Optimality conditions", "weight": 1.0} -->

The optimality conditions for are

<!-- chunk {"id": "body-0013", "role": "body", "section": "Optimality conditions", "weight": 1.0} -->

Note that $s^{T}y$ is the duality gap, i.e., at any point that satisfies the first four equalities and inclusions, ${s^{T}y} = {\hat{p} - \hat{d}}$ where $\hat{p}$ is the primal objective at $(x,s)$ and $\hat{d}$ is the dual objective value at $(x,y)$. Also note that is an implicit system that defines the solution map to a QCP when it is single-valued.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Homogenous embedding", "weight": 1.0} -->

By applying ${s^{T}y} = {\hat{p} - \hat{d}}$, a solution that satisfies is equivalent to a solution of the following nonlinear systems of equations

<!-- chunk {"id": "body-0015", "role": "body", "section": "Homogenous embedding", "weight": 1.0} -->

However, because this system is not guaranteed to be feasible (e.g., when the problem is primal or dual infeasible), we instead consider the homogeneous embedding

<!-- chunk {"id": "body-0016", "role": "body", "section": "Homogenous embedding", "weight": 1.0} -->

where $\tau$ and $\kappa$ are new real-valued variables. Unlike, this embedding is guaranteed to be (asymptotically) feasible even when is primal or dual infeasible.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Homogenous embedding", "weight": 1.0} -->

Applying a change of variable with $N = {n + m + 1}$, the sets

<!-- chunk {"id": "body-0018", "role": "body", "section": "Solution map", "weight": 1.0} -->

For given problem data, the corresponding QCP may have no solution, a unique solution, or multiple solutions. For the remainder of this paper, we assume it has a unique solution. We define the solution map $S:{\Theta\rightarrow\text{R}^{n + {2m}}}$ of a family of parameterized optimization problems as the function mapping $\theta$ to vectors $(x,y,s)$ that satisfy. Similar to, we express this function as composition of functions. Unlike, we only have two functions in our composition: $S = {\phi \circ s}$, where

<!-- chunk {"id": "body-0019", "role": "body", "section": "Solution map", "weight": 1.0} -->

$s:{\Theta\rightarrow\text{R}^{N}}$ maps the problem data to a complementary solution of the homogeneous embedding and

<!-- chunk {"id": "body-0020", "role": "body", "section": "Solution map", "weight": 1.0} -->

$\phi:{\text{R}^{N}\rightarrow\text{R}^{n + {2m}}}$ maps a complementary solution to a solution of the primal-dual pair.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Solution map", "weight": 1.0} -->

At a point $\theta$ where $S$ is differentiable, the derivative of the solution map is

<!-- chunk {"id": "body-0022", "role": "body", "section": "Solution map", "weight": 1.0} -->

We pose the problem of finding a (complementary) solution to the homogeneous embedding as finding a root of a (differentiable) map, a function of both an input to the embedding and the primal-dual pair's problem data $\theta$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Solution map", "weight": 1.0} -->

We consider the differentiability of this map and collect its derivatives with respect to both the embedding input and problem data.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Solution map", "weight": 1.0} -->

Using the implicit function theorem, we find $Ds{(\theta)}$ in terms of these derivatives. While $Ds{(\theta)}$ will require the evaluation of $s$ at a point $\theta$ and we never find an expression for $s$ directly, in practice we can supply such a point, $s{(\theta)}$, by using a (convex) quadratic conic optimization numerical solver.

<!-- chunk {"id": "body-0025", "role": "body", "section": "The conic complementarity set", "weight": 1.0} -->

The conic complementarity set is defined as

<!-- chunk {"id": "body-0026", "role": "body", "section": "The conic complementarity set", "weight": 1.0} -->

Let $\Pi$ and $\Pi^{\circ}$ be the projections onto the cone $K$ and its polar cone $K^{\circ} = {- K^{\ast}}$, respectively. Note the functional equality (a form of the Moreau decomposition) $\Pi^{\circ} = {I - \Pi}$, where $I$ is the identity operator.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Minty's parameterization of the complementarity set", "weight": 1.0} -->

Let $M:{\mathbf{R}^{N}\rightarrow\mathcal{C}}$ be the Minty parameterization of $\mathcal{C}$, defined as

<!-- chunk {"id": "body-0028", "role": "body", "section": "Minty's parameterization of the complementarity set", "weight": 1.0} -->

are not equivalent to the homogeneous embedded conditions. While $z$ satisfying implies that ${u,v} = {M{(z)}}$ satisfy, there exists a non-complementary solution $(u,v)$ to such that $z = {M^{- 1}{(u,v)}}$ does not satisfy. However, is equivalent to the KKT conditions.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Residual map", "weight": 1.0} -->

The map $\mathcal{R}$ is positive homogeneous and differentiable almost everywhere.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Normalized residual map", "weight": 1.0} -->

By, if $z \in \mathbf{R}^{N}$ is a solution to the conic pair then ${\mathcal{N}{(z)}} = 0$. Conversely, if ${\mathcal{N}{(z)}} = 0$, then $z$ is a solution to.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Data dependence", "weight": 1.0} -->

Throughout this note we have fixed the data defining the primal-dual pair, and consequently have not made explicit the dependence of $\mathcal{R},\mathcal{N},Q$ on $\theta$. As we consider the derivative of these functions with respect to $\theta$, we will update our notation writing

<!-- chunk {"id": "body-0032", "role": "body", "section": "Normalized residual map with respect to the data", "weight": 1.0} -->

The normalized residual map is an affine function of the problem data, $\theta$. Therefore, it is differentiable with

<!-- chunk {"id": "body-0033", "role": "body", "section": "Normalized residual map with respect to the variables", "weight": 1.0} -->

The normalized residual map is differentiable at $z$ if $z_{N} \neq 0$ and $\Pi$ is differentiable at $z$. When $z$ is a solution of the primal-dual pair,

<!-- chunk {"id": "body-0034", "role": "body", "section": "Normalized residual map with respect to the variables", "weight": 1.0} -->

where the Jacobian of the nonlinear, homogeneous map $Q$ with respect to the embedding input is

<!-- chunk {"id": "body-0035", "role": "body", "section": "Implicit function theorem applied to $\\mathcal{N}$", "weight": 1.0} -->

If $z$ is a solution of the primal-dual pair and $\Pi$ is differentiable at $z$, then $\mathcal{N}$ is differentiable at $z$, ${N{(z,\theta)}} = 0$, and $z_{N} > 0$. Now suppose that $D_{z}\mathcal{N}{(z,\theta)}$ is invertible. The implicit function theorem guarantees that there exists a neighborhood $V \subseteq \Theta$ of $\theta$ on which the solution $z = {s{(\theta)}}$ of $\mathcal{N}{(z,\theta)}$ is unique. Furthermore, $s$ is differentiable on $V$, ${\mathcal{N}{({s{(\theta)}},\theta)}} = 0$ for all $\theta \in V$, and

<!-- chunk {"id": "body-0036", "role": "body", "section": "Solution construction", "weight": 1.0} -->

To construct a solution $(x,y,s)$ of the primal-dual pair from a complementary solution $z$ of the homogeneous embedding, we use the function $\phi$ given. With $\phi:{\mathbf{R}^{N}\rightarrow\mathbf{R}^{n + {2m}}}$ given by

<!-- chunk {"id": "body-0037", "role": "body", "section": "Computing the Jacobian-vector product", "weight": 1.0} -->

Applying the derivative $D\mathcal{S}{(\theta)}$ to a perturbation ${d\theta} = {({dP},{dA},{dq},{db})} \in \Theta$ corresponds to evaluating

<!-- chunk {"id": "body-0038", "role": "body", "section": "Computing the Jacobian-vector product", "weight": 1.0} -->

Given a solution $(x,y,s)$ to, we construct a root of the normalized residual map as $z = {s{(\theta)}} = {M^{- 1}{(u,v)}} = {u - v}$ where $u = {(x,y,1)}$ and $v = {(0,s,0)}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Computing the Jacobian-vector product", "weight": 1.0} -->

We now work from right to left. First, we compute $\Piz$ and form ${d_{\theta}\mathcal{N}} = {D_{\theta}\mathcal{N}{(z,\theta)}{\lbrack{d\theta}\rbrack}}$. Second, we compute

<!-- chunk {"id": "body-0040", "role": "body", "section": "Computing the Jacobian-vector product", "weight": 1.0} -->

Since it is impractical to form or factor $F$ as a dense matrix in some applications (e.g., when $F$ is large), we use LSMR to solve

<!-- chunk {"id": "body-0041", "role": "body", "section": "Computing the Jacobian-vector product", "weight": 1.0} -->

which only requires multiplication with $F$ and $F^{T}$. Finally, we compute the solution perturbations as

<!-- chunk {"id": "body-0042", "role": "body", "section": "Computing the vector-Jacobian product", "weight": 1.0} -->

The adjoint of the derivative applied to a perturbation $({dx},{dy},{ds})$ is

<!-- chunk {"id": "body-0043", "role": "body", "section": "Computing the vector-Jacobian product", "weight": 1.0} -->

letting $z = {s{(\theta)}}$ as in §3.1. Working right to left, first, we evaluate

<!-- chunk {"id": "body-0044", "role": "body", "section": "Computing the vector-Jacobian product", "weight": 1.0} -->

However, we do not form $dP$ and $dA$ exactly as formulated. Instead we only compute their nonzero (or, more precisely, non-explicit-zero) entries as dictated by the sparsity patterns of $P$ and $A$ respectively.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Hardware accelerated Python implementation", "weight": 1.0} -->

We have developed an open-source JAX library (also making significant use of the packages Equinox and Lineax ), diffqcp, which implements these algorithms and is available at Our implementation supports any QCP whose cone can be expressed as the Cartesian product of the zero cone, the positive orthant, second-order cones, and positive semidefinite cones. (Support for exponential cones, power cones, and their duals is in development.)

<!-- chunk {"id": "body-0046", "role": "body", "section": "Data movement", "weight": 1.0} -->

Host-to-device transfers have been a long-standing limitation of CVXPYlayers, a Python library for constructing differentiable convex optimization layers in PyTorch, JAX, and TensorFlow using CVXPY. Since CVXPYlayers only supports computing the derivative (and its adjoint) of the solution map of a conic program on the CPU, using this library to embed a differentiable convex optimization layer in a neural network requires tranferring any data on the device to the host during the forward or backward pass. Such transfers can be expensive, so having to perform them on both the forward and backward passes during every training iteration can make this embedding prohibitive. Being a JAX library, diffqcp can compute JVPs and VJPs on a GPU, allowing our software to be integrated into GPU workflows, such as neural network training, without these significant host-to-device data transfers.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Performance", "weight": 1.0} -->

diffqcp relies on JAX to enable its high performance. The JAX library uses Python as a "metaprogramming language" to build performant and just-in-time compiled XLA programs. Moreover we rely on the JAX transformation vmap, to simplify writing SIMD computations. diffqcp makes extensive use of this transformation to "batch" projections onto a family of cones with the same dimensionality. This batching is especially advantageous when computing JVPs and VJPs on a GPU, as it enables the execution of many independent computations in parallel, thereby maximizing processor occupancy and overall throughput.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Example", "weight": 1.0} -->

To test our implementation, we applied gradient descent to a loss function of the form

<!-- chunk {"id": "body-0049", "role": "body", "section": "Example", "weight": 1.0} -->

where each ${(x,r)},s,y$ are the optimal primal, slack, and dual solutions of

<!-- chunk {"id": "body-0050", "role": "body", "section": "Example", "weight": 1.0} -->

with $D,E,P$ are diagonal, and $q,f,b$ are vectors and where ${(x^{\star},r^{\star})},s^{\star},y^{\star}$ are the primal, slack, and dual solutions of

<!-- chunk {"id": "body-0051", "role": "body", "section": "Results", "weight": 1.0} -->

We take $m = 2000$ and $n = 1000$. CuClarabel and diffqcp on an Intel Xeon E5-2670 CPU and an NVIDIA TITAN Xp GPU took $44.20$ seconds per iteration. As a control, we canonicalized the objective with SOCs and ran the gradient descent with Clarabel and diffcp, which took $96.86$ seconds per iteration on the Intel Xeon E5-2670 CPU. The improved modeling capacity and GPU-acceleration enabled a $2.19 \times$ speedup.
