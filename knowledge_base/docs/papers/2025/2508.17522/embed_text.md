<!-- arxiv-full-text:v1 {"arxiv_id": "2508.17522", "source": "arxiv-html"} -->

## Introduction

A quadratic cone program (QCP) is an optimization problem which minimizes a convex quadratic function over the intersection of a subspace and a convex cone. Quadratic cone programming is the generalization of both quadratic programming and (linear) cone programming, which date to the 1950s and 1990s \[23, Chapter 4\], respectively. Specifically, a quadratic program (QP) is a QCP whose cone is restricted to the product of $\{0\}$, R, and ${\mbox{\bf R}}_{+}$, while a (linear) cone program is a QCP restricted to having a linear objective.

Quadratic programs, despite their limited modeling power, have been studied extensively as they arise ubiquitously across many disciplines---from classical engineering contexts to finance. Cone programming, on the other hand, has been studied for its generality---all convex optimization problems can be equivalently written as a cone program. Along with their rich theory, signficant development has gone into specialized solvers for both quadratic programs and cone programs. Moreover, domain specific languages, such as CVXPY and CVXR, have been designed to enable easy modeling with both classes of programs.

Perturbation and sensitivity analysis has also been thoroughly developed for QPs and cone programs. Clasically, this analysis centered on the Lagrange multipliers. In recent years, differentiable optimization---the derivative of the solution map between an optimization problem's parameters and its solution---has been developed. The gradients of the solution map of a quadratic program (with respect to the problem data) were derived in by exploiting the problem structure. Subsequently, proposed a technique for differentiating the solution map of a cone program using a more general approach based on the implicit function theorem. Differentiable optimization has found applications across energy systems, statistics, control, and in neural networks.

In recent years, specialized solvers for QCPs have been developed and have demonstrated significant speedups on problems previously solved via cone programs or quadratic programs. As a result, QCPs are emerging as a practical alternative to cone programs for many convex optimization problems. Further, there has been success at GPU-accelerating these QCP solvers. However, the theory of differentiating the solution map of QCPs has remained undeveloped.

### Our contribution

Closely following, we derive conditions for when the derivative, and its adjoint, of the primal-dual solution map to a QCP with respect to the QCP's parameters exists. We then present an extension to to evaluate Jacobian-vector and vector-Jacobian products with these derivatives via projection onto cones and sparse linear system solves. We then describe our GPU-accelerated Python implementation of this method in §3, which forms the derivative of the solution map as an abstract linear operator. Additionally, in §A we present a unified reference of cone projection operators and their derivatives. Notably, this reference and our implementation includes the power cone, which has previously been neglected in the differentiable optimization literature.

## Solution map and its derivative

Following, we consider the mapping from the numerical data defining the primal and dual problems of a QCP to its solutions. This solution map is in general set-valued, but in neighborhoods where it is single-valued it is an implicit function of the problem data. In the sequel, we present a system of equations that implicitly define the solution map of a QCP when it is single-valued. Applying the implicit function theorem to this system, we obtain regularity conditions on the problem data that guarantee when the solution map is single-valued and its derivative exists. Finally, we provide an expression for the derivative at points where these conditions are satisfied.

### QCPs and implicit functions

The primal and dual problems for a (convex) QCP are where $x\in{\mbox{\bf R}}^{n}$ is the primal variable, $y\in{\mbox{\bf R}}^{m}$ is the dual variable, and $s\in{\mbox{\bf R}}^{m}$ is the primal slack variable. We assume that $\mathcal{K}\subseteq{\mbox{\bf R}}^{m}$ is a nonempty, closed, convex cone with dual cone $\mathcal{K}^{*}$. The problem data are $P\in{\mbox{\bf S}}_{+}^{n}$, $A\in{\mbox{\bf R}}^{m\times n}$, $q\in{\mbox{\bf R}}^{n}$, and $b\in{\mbox{\bf R}}^{m}$. (The convex cone can also be problem data, but for our purposes we fix $\mathcal{K}$.) To simplify the subsequent discussion, we define the set That is, $\theta$ is the concatenation of problem data (relaxed to allow $P\not\succeq 0$)---a change from which embeds the problem data into a skew-symmetric matrix.

### Optimality conditions

The optimality conditions for are Note that $s^{T}y$ is the duality gap, i.e., at any point that satisfies the first four equalities and inclusions, $s^{T}y=\hat{p}-\hat{d}$ where $\hat{p}$ is the primal objective at $(x,s)$ and $\hat{d}$ is the dual objective value at $(x,y)$. Also note that is an implicit system that defines the solution map to a QCP when it is single-valued.

### Homogenous embedding

By applying $s^{T}y=\hat{p}-\hat{d}$, a solution that satisfies is equivalent to a solution of the following nonlinear systems of equations However, because this system is not guaranteed to be feasible (e.g., when the problem is primal or dual infeasible), we instead consider the homogeneous embedding (as defined in) | | | $\displaystyle\begin{bmatrix}0\\ | | \(4\) | | | | \kappa\end{bmatrix}=\begin{bmatrix}Px+A^{T}y+\tau q\\ | | | | | | -(1/\tau)x^{T}Px-q^{T}x-b^{T}y\end{bmatrix},$ | | | | | | $\displaystyle(x,s,y,\tau,\kappa)\in\mathbf{R}^{n}\times\mathcal{K}\times\mathcal{K}^{*}\times\mathbf{R}_{+}\times\mathbf{R}_{+},\quad\tau+\kappa>0,$ | | | where $\tau$ and $\kappa$ are new real-valued variables. Unlike, this embedding is guaranteed to be (asymptotically) feasible even when is primal or dual infeasible.

Applying a change of variable with $N=n+m+1$, the sets and the functions $Q_{1}:{\mbox{\bf R}}^{N}\to{\mbox{\bf R}}^{n}$, $Q_{2}:{\mbox{\bf R}}^{N}\to{\mbox{\bf R}}^{m}$, and $Q_{3}:{\mbox{\bf R}}^{N}\to{\mbox{\bf R}}$ defined as we simplify the sequel by writing as Here $Q:{\mbox{\bf R}}^{N}\to{\mbox{\bf R}}^{N}$ is defined as $Q(u)=(Q_{1}(u),Q_{2}(u),Q_{3}(u))$. Lastly, we define a solution to as a complementary solution if $u_{N}v_{N}=0$.

### Solution map

For given problem data, the corresponding QCP may have no solution, a unique solution, or multiple solutions. For the remainder of this paper, we assume it has a unique solution. We define the solution map $S:\Theta\to{\mbox{\bf R}}^{n+2m}$ of a family of parameterized optimization problems as the function mapping $\theta$ to vectors $(x,y,s)$ that satisfy. Similar to, we express this function as composition of functions. Unlike, we only have two functions in our composition: $S=\phi\circ s$, where $s:\Theta\to{\mbox{\bf R}}^{N}$ maps the problem data to a complementary solution of the homogeneous embedding and $\phi:{\mbox{\bf R}}^{N}\to{\mbox{\bf R}}^{n+2m}$ maps a complementary solution to a solution of the primal-dual pair.

At a point $\theta$ where $S$ is differentiable, the derivative of the solution map is by the chain rule. In the remainder of this section we develop an expression for $DS(\theta)$ by following the approach taken: We pose the problem of finding a (complementary) solution to the homogeneous embedding as finding a root of a (differentiable) map, a function of both an input to the embedding and the primal-dual pair's problem data $\theta$.

We consider the differentiability of this map and collect its derivatives with respect to both the embedding input and problem data.

Using the implicit function theorem, we find $Ds(\theta)$ in terms of these derivatives. While $Ds(\theta)$ will require the evaluation of $s$ at a point $\theta$ and we never find an expression for $s$ directly, in practice we can supply such a point, $s(\theta)$, by using a (convex) quadratic conic optimization numerical solver.

### Other machinery

This subsection closely follows.

### The conic complementarity set

The conic complementarity set is defined as Let $\Pi$ and $\Pi^{\circ}$ be the projections onto the cone $K$ and its polar cone $K^{\circ}=-K^{*}$, respectively. Note the functional equality (a form of the Moreau decomposition) $\Pi^{\circ}=I-\Pi$, where $I$ is the identity operator.

### Minty's parameterization of the complementarity set

Let $M:\mathbf{R}^{N}\to\mathcal{C}$ be the Minty parameterization of $\mathcal{C}$, defined as with inverse $M^{-1}:\mathcal{C}\to\mathbf{R}^{N}$ given by are not equivalent to the homogeneous embedded conditions. While $z$ satisfying implies that $u,v=M(z)$ satisfy, there exists a non-complementary solution $(u,v)$ to such that $z=M^{-1}(u,v)$ does not satisfy. However, is equivalent to the KKT conditions.

### Residual map

The residual map $\mathcal{R}:\mathbf{R}^{N}\to\mathbf{R}^{N}$ is defined as The map $\mathcal{R}$ is positive homogeneous and differentiable almost everywhere.

### Normalized residual map

The normalized residual map $\mathcal{N}:\left\{z\in\mathbf{R}^{N}\,\middle|\,z_{N}\not=0\right\}\to\mathbf{R}^{N}$ is defined as By, if $z\in\mathbf{R}^{N}$ is a solution to the conic pair then $\mathcal{N}(z)=0$. Conversely, if $\mathcal{N}(z)=0$, then $z$ is a solution to.

### Data dependence

Throughout this note we have fixed the data defining the primal-dual pair, and consequently have not made explicit the dependence of $\mathcal{R},\mathcal{N},Q$ on $\theta$. As we consider the derivative of these functions with respect to $\theta$, we will update our notation writing

### Derivatives

### Normalized residual map with respect to the data

The normalized residual map is an affine function of the problem data, $\theta$. Therefore, it is differentiable with and $D_{\theta}Q(u,\theta)^{T}[w]=(\widetilde{P},\widetilde{A},\widetilde{b},\widetilde{q},\widetilde{b})$ where for $w\in{\mbox{\bf R}}^{N}$ and $\widetilde{\theta}\in\Theta$.

### Normalized residual map with respect to the variables

The normalized residual map is differentiable at $z$ if $z_{N}\neq 0$ and $\Pi$ is differentiable at $z$. When $z$ is a solution of the primal-dual pair, where the Jacobian of the nonlinear, homogeneous map $Q$ with respect to the embedding input is

### Implicit function theorem applied to $\mathcal{N}$

If $z$ is a solution of the primal-dual pair and $\Pi$ is differentiable at $z$, then $\mathcal{N}$ is differentiable at $z$, $N(z,\theta)=0$, and $z_{N}>0$. Now suppose that $D_{z}\mathcal{N}(z,\theta)$ is invertible. The implicit function theorem guarantees that there exists a neighborhood $V\subseteq\Theta$ of $\theta$ on which the solution $z=s(\theta)$ of $\mathcal{N}(z,\theta)$ is unique. Furthermore, $s$ is differentiable on $V$, $\mathcal{N}(s(\theta),\theta)=0$ for all $\theta\in V$, and

### Solution construction

To construct a solution $(x,y,s)$ of the primal-dual pair from a complementary solution $z$ of the homogeneous embedding, we use the function $\phi$ given. With $\phi:\mathbf{R}^{N}\to\mathbf{R}^{n+2m}$ given by If $\Pi_{\mathcal{K}^{*}}$ is differentiable at $z_{n+1:n+m}$, then $\phi$ is also differentiable and

## Implementation

### Computing the Jacobian-vector product

Applying the derivative $D\mathcal{S}(\theta)$ to a perturbation $d\theta=(dP,dA,dq,db)\in\Theta$ corresponds to evaluating Given a solution $(x,y,s)$ to, we construct a root of the normalized residual map as $z=s(\theta)=M^{-1}(u,v)=u-v$ where $u=(x,y,1)$ and $v=(0,s,0)$.

We now work from right to left. First, we compute $\Pi z$ and form $d_{\theta}\mathcal{N}=D_{\theta}\mathcal{N}(z,\theta)[d\theta]$. Second, we compute Since it is impractical to form or factor $F$ as a dense matrix in some applications (e.g., when $F$ is large), we use LSMR to solve which only requires multiplication with $F$ and $F^{T}$. Finally, we compute the solution perturbations as

### Computing the vector-Jacobian product

The adjoint of the derivative applied to a perturbation $(dx,dy,ds)$ is letting $z=s(\theta)$ as in §3.1. Working right to left, first, we evaluate Second, we evaluate $\Pi z$ and form $d_{\theta}\mathcal{N}=-F^{-T}dz$ using LSMR. Finally the problem data perturbation $d\theta=(dP,dA,dq,db)$ is given by However, we do not form $dP$ and $dA$ exactly as formulated. Instead we only compute their nonzero (or, more precisely, non-explicit-zero) entries as dictated by the sparsity patterns of $P$ and $A$ respectively.

### Hardware accelerated Python implementation

We have developed an open-source JAX library (also making significant use of the packages Equinox and Lineax ), diffqcp, which implements these algorithms and is available at Our implementation supports any QCP whose cone can be expressed as the Cartesian product of the zero cone, the positive orthant, second-order cones, and positive semidefinite cones. (Support for exponential cones, power cones, and their duals is in development.)

### Data movement

Host-to-device transfers have been a long-standing limitation of CVXPYlayers, a Python library for constructing differentiable convex optimization layers in PyTorch, JAX, and TensorFlow using CVXPY. Since CVXPYlayers only supports computing the derivative (and its adjoint) of the solution map of a conic program on the CPU, using this library to embed a differentiable convex optimization layer in a neural network requires tranferring any data on the device to the host during the forward or backward pass. Such transfers can be expensive, so having to perform them on both the forward and backward passes during every training iteration can make this embedding prohibitive. Being a JAX library, diffqcp can compute JVPs and VJPs on a GPU, allowing our software to be integrated into GPU workflows, such as neural network training, without these significant host-to-device data transfers.

### Performance

diffqcp relies on JAX to enable its high performance. The JAX library uses Python as a "metaprogramming language" to build performant and just-in-time compiled XLA programs. Moreover we rely on the JAX transformation vmap, to simplify writing SIMD computations. diffqcp makes extensive use of this transformation to "batch" projections onto a family of cones with the same dimensionality. This batching is especially advantageous when computing JVPs and VJPs on a GPU, as it enables the execution of many independent computations in parallel, thereby maximizing processor occupancy and overall throughput.

### Example

To test our implementation, we applied gradient descent to a loss function of the form where each $(x,r),s,y$ are the optimal primal, slack, and dual solutions of with $D,E,P$ are diagonal, and $q,f,b$ are vectors and where $(x^{\star},r^{\star}),s^{\star},y^{\star}$ are the primal, slack, and dual solutions of for a randomly selected $C^{\star},d^{\star}$.

### Results

We take $m=2000$ and $n=1000$. CuClarabel and diffqcp on an Intel Xeon E5-2670 CPU and an NVIDIA TITAN Xp GPU took $44.20$ seconds per iteration. As a control, we canonicalized the objective with SOCs and ran the gradient descent with Clarabel and diffcp, which took $96.86$ seconds per iteration on the Intel Xeon E5-2670 CPU. The improved modeling capacity and GPU-acceleration enabled a $2.19\times$ speedup.
