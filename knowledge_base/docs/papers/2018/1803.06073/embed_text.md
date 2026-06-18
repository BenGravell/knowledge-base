## Introduction

In this work, we study first-order methods for solving the (unconstrained) minimization problem

where $f:^{d}\rightarrow$. In the sequel, we focus on the case where $f$ is $L$-smooth and $\mu$-strongly convex, though our methodology can be adapted to a broader class of problems.

To solve ($\mathcal{P}$), we consider methods that iteratively update their estimate of the optimizer using only gradient evaluations. One possibility for proving convergence of such methods is by finding *Lyapunov functions*.

A Lyapunov function can be interpreted as defining an "energy" that decreases geometrically with each iteration of the method, with an energy of zero corresponding to reaching the optimal solution of ($\mathcal{P}$). The existence of such an energy function thus provides a straightforward certificate of linear convergence for the iterative method.

In this paper, we present an automated way of generating quadratic Lyapunov functions for certifying linear convergence of first-order iterative methods to solve ($\mathcal{P}$). The procedure relies on solving a small-sized semidefinite program (SDP) so it is computationally efficient. Moreover, the procedure is *tight*, meaning that if the SDP is infeasible, then no such quadratic Lyapunov function exists.

Our results unify recent SDP-based works for certifying convergence of first-order methods, namely: performance estimation problems and integral quadratic constraints from robust control, using smooth strongly convex interpolation. These connections are further discussed in Section 4.3.

### Organization

The paper is organized as follows. We describe the class of methods under consideration and basic properties of Lyapunov functions in Sections 2 and 3 respectively. Our main results are then presented in Section 4, which also features numerical examples and comparisons to other approaches. The corresponding proof is presented in Section 5. Finally, we explore extensions of our approach in Section 6, and conclude in Section 7.

### Preliminaries

A function $f:^{d}\rightarrow$ is called $L$-smooth if its gradient is Lipschitz continuous with parameter $L$, i.e.,

Furthermore, $f$ is called convex if

and $\mu$-strongly convex if ${f{(x)}} - {\frac{\mu}{2}{\| x\|}^{2}}$ is convex. The set of $L$-smooth and $\mu$-strongly convex functions is denoted $\mathcal{F}_{\mu,L}$, and we define $\kappa{: =}\frac{L}{\mu}$, the corresponding condition number.

When $f \in \mathcal{F}_{\mu,L}$ with $0 < \mu \leq L$, optimization problem ($\mathcal{P}$) has a unique minimizer denoted $x_{\star}{: =}{{{\arg\min}_{x}f}{(x)}}$. The function and gradient values at optimality are denoted $f_{\star}{: =}{f{(x_{\star})}}$ and $g_{\star}{: =}{{\nabla f}{(x_{\star})}} = \mathbf{0}_{d}$, respectively.

## First-Order Iterative Fixed-Step Methods

To solve the optimization problem ($\mathcal{P}$), we consider *first-order iterative fixed-step methods* of the form

for $k \geq 0$ where $\alpha$, $\beta_{j}$, $\gamma_{j}$ are the (fixed) step-sizes and $x_{j} \in^{d}$ for $j = {{- N},\ldots,0}$ are the initial conditions. We call the constant $N \geq 0$ the *degree* of the method.

Many first-order optimization methods are of the form ($\mathcal{M}$), including: the Gradient Method, Heavy Ball Method, Fast Gradient Method for smooth strongly convex minimization, Triple Momentum Method, and Robust Momentum Method.

For method ($\mathcal{M}$) to solve ($\mathcal{P}$), it must have a fixed-point at the optimizer $x_{\star}$. Hence, we require the step-sizes to satisfy

For simplicity, let us define the concatenated error vectors at iteration $k$ as ${\mathbf{x}_{k},\mathbf{g}_{k}} \in^{{({N + 1})}d}$ and $\mathbf{f}_{k} \in^{N + 1}$ with

$\mathbf{x}_{k}$ ${: =}\begin{bmatrix} (3a)
{({x_{k} - x_{\star}})}^{\mathsf{T}} & \ldots & {({x_{k - N} - x_{\star}})}^{\mathsf{T}}
\end{bmatrix}^{\mathsf{T}}$
$\mathbf{g}_{k}$ ${: =}\begin{bmatrix} (3b)
{({g_{k} - g_{\star}})}^{\mathsf{T}} & \ldots & {({g_{k - N} - g_{\star}})}^{\mathsf{T}}
\end{bmatrix}^{\mathsf{T}}$
$\mathbf{f}_{k}$ ${: =}\begin{bmatrix} (3c)
{({f_{k} - f_{\star}})} & \ldots & {({f_{k - N} - f_{\star}})}
\end{bmatrix}^{\mathsf{T}}$

where $x_{k} \in^{d}$ are the iterates, $f_{k}{: =}{f{(y_{k})}} \in$ are the function values, and $g_{k}{: =}{{\nabla f}{(y_{k})}} \in^{d}$ are the gradient values. Note that we shifted $(\mathbf{x}_{k},\mathbf{g}_{k},\mathbf{f}_{k})$ so that the optimal solution corresponds to ${(\mathbf{x}_{\star},\mathbf{g}_{\star},\mathbf{f}_{\star})} = {(\mathbf{0},\mathbf{0},\mathbf{0})}$.

## What is a Lyapunov Function?

Lyapunov functions are one of the fundamental tools in control theory that can be used to verify stability of a dynamical system.

Consider applying method ($\mathcal{M}$) to solve problem ($\mathcal{P}$). Our goal is to find the smallest possible $0 \leq \rho < 1$ such that $\{ x_{k}\}$ converges linearly to the optimizer $x_{\star}$ with rate $\rho$. A Lyapunov function $\mathcal{V}$ is a continuous function $\mathcal{V}:^{n}\rightarrow$ that satisfies the following properties:

(nonnegative) ${\mathcal{V}{(\xi)}} \geq 0$ for all $\xi$,

(zero at fixed-point) ${\mathcal{V}{(\xi)}} = 0$ if and only if $\xi = \xi_{\star}$,

(radially unbounded) ${\mathcal{V}{(\xi)}}\rightarrow\infty$ as ${\|\xi\|}\rightarrow\infty$,

(decreasing) ${\mathcal{V}{(\xi_{k + 1})}} \leq {\rho^{2}\mathcal{V}{(\xi_{k})}}$ for $k \geq N$,

where $\xi_{k}{: =}{(\mathbf{x}_{k},\mathbf{g}_{k},\mathbf{f}_{k})}$ is the *state* of the system at iteration $k$. The state at iteration $k$ includes past iterates, function values, and gradient values from iterations $k - N$ up to $k$. If we can find such a $\mathcal{V}$, then it can be used to show that the state converges linearly to the fixed-point from any initial condition (the rate of convergence depends on both $\rho$ and the structure of $\mathcal{V}$).

Lyapunov functions are typically found by searching over a parameterized family of functions (called Lyapunov function candidates). In the simple case where the state $\{\xi_{k}\}$ is generated by a linear dynamical system, one can search over quadratic Lyapunov function candidates by solving a semidefinite program, as illustrated in Example 1. ‣ 3 What is a Lyapunov Function? ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees") below.

### Example 1 (Quadratic Lyapunov function)

Consider the linear dynamical system described by

with fixed-point $\xi_{\star} \in^{n}$ (i.e., $\xi_{\star} = {A\xi_{\star}}$). Suppose that

has solution $P_{\star}$. Then a Lyapunov function for the system is

which can be used to show that $\xi_{k}\rightarrow\xi_{\star}$ linearly with rate $\rho$. Specifically, we have the bound

To find the best bound, we can perform a bisection search on $\rho$ to find the smallest $\rho$ such that (4. ‣ 3 What is a Lyapunov Function? ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) is feasible.

Note that although $\mathcal{V}$ depends explicitly on the fixed point $\xi_{\star}$, we do not need to know $\xi_{\star}$ to solve the SDP (4. ‣ 3 What is a Lyapunov Function? ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")).

The linear dynamical system of Example 1. ‣ 3 What is a Lyapunov Function? ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees") converges linearly if and only if a quadratic Lyapunov function exists, which happens if and only if the SDP (4. ‣ 3 What is a Lyapunov Function? ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) is feasible.

## Main Results

Similar to Example 1. ‣ 3 What is a Lyapunov Function? ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees"), we now show how to use quadratic Lyapunov functions to prove linear convergence of a first-order iterative fixed-step method applied to the minimization of a smooth strongly convex function. Furthermore, we show that such Lyapunov function exists if and only if a small-sized semidefinite program is feasible (whose optimal solution produces the Lyapunov function).

### Quadratic Lyapunov Functions

We begin with sufficiency: if we can find a quadratic Lyapunov function, we can use it to prove linear convergence.

### Lemma 2 (Quadratic Lyapunov function)

Consider applying the first-order iterative fixed-step method ($\mathcal{M}$) of degree $N$ to a smooth strongly convex function $f \in \mathcal{F}_{\mu,L}{(^{d})}$ with $0 < \mu \leq L$. Define the state $\xi_{k}{: =}{(\mathbf{x}_{k},\mathbf{g}_{k},\mathbf{f}_{k})}$ as in. Consider the quadratic function

with parameters $P \in {\mathbb{S}}^{2{({N + 1})}}$ and $p \in^{N + 1}$, and where $\otimes$ denotes the Kronecker product. Suppose $\mathcal{V}$ is a Lyapunov function for the system with rate $\rho$. Then, the following bound is satisfied:

Proof. Suppose $\mathcal{V}$ is a Lyapunov function for method ($\mathcal{M}$) with $f \in \mathcal{F}_{\mu,L}$. Then $0 \geq {{\mathcal{V}{(\xi_{i + 1})}} - {\rho^{2}\mathcal{V}{(\xi_{i})}}}$ for $i \geq N$. Multiplying this inequality by $\rho^{2{({k - i - 1})}}$ and summing over $i = {N,\ldots,{k - 1}}$ gives a telescoping sum that yields (6. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")).

As a consequence to Lemma 2. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees"), we have the relations:

$\|{x_{k} - x_{\star}}\|$ $= {\mathcal{O}{(\rho^{k})}}$ (7a)
$\|{{\nabla f}{(y_{k})}}\|$ $= {\mathcal{O}{(\rho^{k})}}$ (7b)
${f{(y_{k})}} - f_{\star}$ $= {\mathcal{O}{(\rho^{2k})}}$ (7c)

where $x_{\star} \in^{d}$ is the optimizer of ($\mathcal{P}$) and $f_{\star}{: =}{f{(x_{\star})}}$.

### Remark 3

The Lyapunov function (5. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) is only defined for $k \geq N$ since the state $\xi_{k}$ is a function of the previous $N$ function and gradient values. This is why the bound (6. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) is expressed in terms of $\mathcal{V}{(\xi_{N})}$.

### Remark 4

The states used in the Lyapunov function (5. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) can be modified to include other iterates (such as $y_{k}$) in the quadratic term as well as the function and gradient values evaluated at iterates other than $y_{k}$. We chose the form in (5. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) because it contains all necessary ingredients while also being straightforward to generalize to other cases.

In addition, note that the structure of (5. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) makes it *permutation-invariant* (i.e., it does not depend on the ordering of the coordinate set). This is largely motivated by the fact that there is no reason to favor any coordinate among ^d^.

Lemma 2. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees") shows that if we can find a quadratic Lyapunov function, then we can use this to prove linear convergence of method ($\mathcal{M}$) when $f \in \mathcal{F}_{\mu,L}$. In the following section, we construct an SDP whose feasibility is necessary and sufficient for the existence of such a Lyapunov function.

### SDP for Quadratic Lyapunov Functions

Given parameters $\alpha$, $\beta_{j}$, and $\gamma_{j}$ for a method ($\mathcal{M}$) of degree $N$ and a rate $\rho$ to be verified, we construct the semidefinite program as follows.

### Step 1: Initialization

First, we initialize the row vectors ${{\overline{x}}_{k}^{(K)},{\overline{g}}_{k}^{(K)}} \in^{N + K + 2}$ and ${\overline{f}}_{k}^{(K)} \in^{K + 1}$, corresponding to the initial conditions, gradient values, and function values, respectively, as

${\overline{x}}_{k}^{(K)}{: =}\mathbf{e}_{k + N + 1}^{\mathsf{T}}$ ${\text{for~}k} \in {\{{- N},\ldots,0\}}$ (8a)
${\overline{g}}_{k}^{(K)}{: =}\mathbf{e}_{k + N + 2}^{\mathsf{T}}$ ${\text{for~}k} \in {\{ 0,\ldots,K\}}$ (8b)
${\overline{f}}_{k}^{(K)}{: =}\mathbf{e}_{k + 1}^{\mathsf{T}}$ ${\text{for~}k} \in {\{ 0,\ldots,K\}}$ (8c)

for $K \in {\{ N,{N + 1}\}}$ ($\mathbf{e}_{i}$ denotes the $i^{\text{th}}$ unit vector with appropriate dimension). These form a basis for all iterates, function values, and gradient values up to iteration $K$. Also, define the row vectors corresponding to the fixed-point as

We also introduce the following SDP variables:

where $\mathcal{I}_{K}{: =}{\{ 0,1,\ldots,K, \star \}}$ is an index set.

### Step 2: Method

Next, we iterate the method for $k = {0,\ldots,K}$ using the row vectors we previously defined.

${\overline{y}}_{k}^{(K)}$ $= {\sum\limits_{j = 0}^{N}{\gamma_{j}{\overline{x}}_{k - j}^{(K)}}}$ (9a)
${\overline{x}}_{k + 1}^{(K)}$ ${= {{\sum\limits_{j = 0}^{N}{\beta_{j}{\overline{x}}_{k - j}^{(K)}}} - {\alpha{\overline{g}}_{k}^{(K)}}}}.$ (9b)

### Step 3: Interpolation conditions^11^1The terms $M_{i\hspace{0pt}j}^{(K)}$ and $m_{i\hspace{0pt}j}^{(K)}$ are related to *interpolation* by smooth strongly convex functions as discussed in Section 5.1

Using the computed vectors, define $m_{ij}^{(K)} \in^{K + 1}$ and $M_{ij}^{(K)} \in {\mathbb{S}}^{N + K + 2}$ as

$m_{ij}^{(K)}$ ${: =}{{({L - \mu})}\left( {{\overline{f}}_{i}^{(K)} - {\overline{f}}_{j}^{(K)}} \right)^{\mathsf{T}}}$ (10a)
$M_{ij}^{(K)}$ ${: =}{\frac{1}{2}\begin{bmatrix} (10b)
\end{bmatrix}^{\mathsf{T}}M\begin{bmatrix}

for ${i,j} \in \mathcal{I}_{K}$ where

### Step 4: Lyapunov function

We now construct the linear and quadratic terms in the Lyapunov function, denoted $v_{k}^{(K)} \in^{K + 1}$ and $V_{k}^{(K)} \in {\mathbb{S}}^{N + K + 2}$, respectively, as

$v_{k}^{(K)}$ ${: =}{p^{\mathsf{T}}{\overline{\mathbf{f}}}_{k}^{(K)}}$ (12a)
\end{bmatrix}^{\mathsf{T}}P\begin{bmatrix}

where the matrices ${{\overline{\mathbf{x}}}_{k}^{(K)},{\overline{\mathbf{g}}}_{k}^{(K)}} \in^{{({N + 1})} \times {({N + K + 2})}}$ and ${\overline{\mathbf{f}}}_{k}^{(K)} \in^{{({N + 1})} \times {({K + 1})}}$ are defined as

Also, define the decrease in the linear and quadratic terms of the Lyapunov function as

where $\rho$ is the convergence rate to be verified.

### Step 5: Semidefinite program

Finally, we compute the quadratic Lyapunov function (if one exists) for a given rate $\rho$ by solving the following semidefinite program:

SDP for quadratic Lyapunov function ($\rho$-SDP) $\operatorname{feasible}\limits_{\substack{P \in {\mathbb{S}}^{2{({N + 1})}} \\ p \in^{N + 1} \\ \{\lambda_{ij}\} \\ \{\eta_{ij}\}}}$ $0 \prec {V_{N}^{(N)} - {\sum\limits_{{i,j} \in \mathcal{I}_{N}}{\lambda_{ij}M_{ij}^{(N)}}}}$ $0 < {v_{N}^{(N)} - {\sum\limits_{{i,j} \in \mathcal{I}_{N}}{\lambda_{ij}m_{ij}^{(N)}}}}$ $0 \succeq {{\DeltaV_{N}^{({N + 1})}} + {\sum\limits_{{i,j} \in \mathcal{I}_{N + 1}}{\eta_{ij}M_{ij}^{({N + 1})}}}}$ $0 \geq {{\Deltav_{N}^{({N + 1})}} + {\sum\limits_{{i,j} \in \mathcal{I}_{N + 1}}{\eta_{ij}m_{ij}^{({N + 1})}}}}$ ${0 \leq {\lambda_{ij}\quad{\text{for~}i}}},{j \in \mathcal{I}_{N}}$ ${0 \leq {\eta_{ij}\quad{\text{for~}i}}},{j \in \mathcal{I}_{N + 1}}$

### Theorem 5 (Main Result)

Consider applying the first-order iterative fixed-step method ($\mathcal{M}$) of degree $N$ to a smooth strongly convex function $f \in \mathcal{F}_{\mu,L}{(^{d})}$ with $0 < \mu \leq L$. Let the step-sizes $\alpha$, $\beta_{j}$, and $\gamma_{j}$ be such that $\alpha \neq 0$, $\gamma_{0} \neq 0$, and

Then there exists a quadratic Lyapunov function of the form (5. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) with rate $\rho$ that is valid for all $d \in {\mathbb{N}}$ if and only if ($\rho$-SDP) is feasible.

From Theorem 5. ‣ Step 5: Semidefinite program. ‣ 4.2 SDP for Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees"), we can perform bisection on $\rho$ to find the minimum $\rho$ such that ($\rho$-SDP) is feasible to produce the *fastest* linear convergence rate that is able to be verified using a quadratic Lyapunov function with states $(\mathbf{x},\mathbf{g},\mathbf{f})$.

### Comparison to PEP and IQC

Our results are closely related to several other recent approaches utilizing semidefinite programs for studying convergence of first-order methods, which we discuss now.

### Performance Estimation Problem (PEP)

The performance estimation approach was introduced by Drori & Teboulle as a systematic way to obtain worst-case performance guarantees of a given method. In the context of fixed-step first-order methods, performance estimation problems (PEP) can be formulated as semidefinite programs.

The key idea in PEP is to look for a tuple $(x_{- N},\ldots,x_{0},f)$ such that the given algorithm behaves in the worst possible way, according to a given performance measure. The dual of PEP corresponding to the performance measure ${{\mathcal{V}{(\xi_{N + 1})}}/\mathcal{V}}{(\xi_{N})}$ for some fixed $P$ and $p$ is exactly the same as solving $\min_{\rho}\rho^{2}$ subject to ($\rho$-SDP) being feasible.

The difference between PEP and our approach is that in PEP, the optimization is for a fixed performance measure carried out over multiple timesteps. This yields exact worst-case bounds, but at the cost of solving an SDP whose size is proportional to the number of timesteps (this allows, among others, dealing with time-varying methods and sublinear convergence rates). In our approach, for a fixed $\rho$, we optimize the performance measure itself. This yields a Lyapunov function with a guaranteed decrease at every iteration while maintaining tightness and solving a small SDP of fixed size. Both approaches ensure tightness via *(smooth) convex interpolation*, developed by Taylor et al..

### Integral Quadratic Constraints (IQCs)

Integral quadratic constraints are an analysis method for bounding the worst-case performance of dynamical systems in feedback with nonlinearities. This approach was recently adapted for use in analyzing first-order optimization algorithms. In the optimization context, the nonlinear component is the gradient of the objective function, while the dynamical system is the iterative method being analyzed.

The key idea with IQCs is to replace the nonlinearity ($\nabla f$) by quadratic constraints that it must satisfy. This is precisely the idea behind *interpolation* (discussed in Section 5.1), which is a foundational concept in our methodology.

The difference between IQCs and our approach is that the interpolation conditions are necessary and sufficient to characterize $\nabla f$ when $f \in \mathcal{F}_{\mu,L}$. However, the sector IQC and weighted off-by-one IQC used by Lessard et al. are a strict subset of the interpolation conditions; they are only sufficient for describing $\nabla f$ when $f \in \mathcal{F}_{\mu,L}$. In particular, the IQC framework does not use any constraints on $\nabla f$ that explicitly involve function values. This amounts to solving ($\rho$-SDP) with additional constraints on $\lambda_{ij}$ and $\eta_{ij}$ such that all the function values cancel out in the SDP.

### Numerical Comparisons

To illustrate our results, we consider the Gradient Method (GM), Heavy Ball Method (HBM), Fast Gradient Method (FGM), and Triple Momentum Method (TMM). Each of these methods can be parametrized as

for $k \geq 0$ where ${x_{- 1},x_{0}} \in^{d}$ are the initial conditions, and the parameters for each method are:

We use ($\rho$-SDP) to find corresponding Lyapunov functions. The corresponding convergence rates are provided in Figure 1; the results match those obtained using IQCs for GM, HBM, and FGM, and those for TMM provided in. For more complicated cases, the performance estimation toolbox PESTO can be used to perform numerical validations.

For illustrative purposes, we present results obtained using a restricted class of Lyapunov functions. We fixed $\lambda_{ij} = 0$ in ($\rho$-SDP) and plotted the best achievable $\rho$ in Figure 2. We observe that this restricted class is not sufficient to recover the rates obtained in Figure 1.

Figure 1: Worst-case linear convergence rates from (ρ-SDP).

Figure 2: Order of magnitude of the worst-case number of iterations, which is 𝒪 (−1/log ρ), to solve problem (𝒫). The bounds are obtained by searching for Lyapunov functions of the form in two cases: (i) (P,p) found using (ρ-SDP) (solid), and (ii) restricting P ≻ 0 and p &gt; 0 (dashed).

## Proof of Theorem 5. ‣ Step 5: Semidefinite program. ‣ 4.2 SDP for Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")

### Sampled Smooth Strongly Convex Functions

To prove Theorem 5. ‣ Step 5: Semidefinite program. ‣ 4.2 SDP for Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees"), we first need a result on smooth strongly convex functions that are sampled at discrete points. Indeed, inequalities and completely characterize functions that are smooth and strongly convex. However, these inequalities are defined on an infinite set of points, and it was shown in Section 2.2 of that using them to prove convergence may introduce conservatism. Therefore, in order to completely characterize points which are sampled from smooth strongly convex functions, we need the concept of *interpolation*.

The following theorem is borrowed from and forms the basic building block for our analysis.

### Theorem 6 ($\mathcal{F}_{\mu,L}$-interpolation)

Let $\mathcal{I}$ be an index set, and consider the set of triples $S = {\{{(y_{i},g_{i},f_{i})}\}}_{i \in \mathcal{I}}$ where ${y_{i},g_{i}} \in^{d}$ and $f_{i} \in$ for all $i \in \mathcal{I}$. There exists a function^22^2In other words, we say that the set $S$ is *$\mathcal{F}_{\mu,L}$-interpolable*. $f \in \mathcal{F}_{\mu,L}$ such that ${f{(y_{i})}} = f_{i}$ and ${{\nabla f}{(y_{i})}} = g_{i}$ for all $i \in \mathcal{I}$ if and only if $\phi_{ij} \geq 0$ for all ${i,j} \in \mathcal{I}$ where

with $M \in {\mathbb{S}}^{4}$ defined in (11 and 𝑚_{𝑖⁢𝑗}^(𝐾) are related to interpolation by smooth strongly convex functions as discussed in Section 5.1. ‣ 4.2 SDP for Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")).

### Positive Definite Quadratics From Sampling

Recall from Section 3 that the Lyapunov function must satisfy two conditions: (i) $\mathcal{V}$ must be positive definite (i.e, nonnegative, zero at the fixed-point, and radially unbounded), and (ii) ${\Delta\mathcal{V}}{: =}{\mathcal{V}_{k + 1} - {\rho^{2}\mathcal{V}_{k}}}$ must be negative semidefinite (i.e., $\mathcal{V}$ must satisfy the decrease condition). To prove both (i) and (ii), we use the following theorem, which provides necessary and sufficient conditions for a quadratic form to be positive (semi-)definite when the iterates are generated by method ($\mathcal{M}$) applied to $f \in \mathcal{F}_{\mu,L}$.

### Theorem 7 (Sampled positive definite quadratics)

Consider applying the first-order iterative fixed-step method ($\mathcal{M}$) of degree $N$ to a smooth strongly convex function $f \in \mathcal{F}_{\mu,L}{(^{d})}$ for $K$ iterations. Suppose the step-sizes $\alpha$, $\beta_{j}$, and $\gamma_{j}$ are such that $\alpha \neq 0$, $\gamma_{0} \neq 0$, and

Define the vectors $\mathbf{x} \in^{{({N + 1})}d}$, $\mathbf{g} \in^{{({K + 1})}d}$, and $\mathbf{f} \in^{K + 1}$ as

$\mathbf{x}$ ${: =}\begin{bmatrix} (16a)
{({x_{- N} - x_{\star}})}^{\mathsf{T}} & \ldots & {({x_{0} - x_{\star}})}^{\mathsf{T}}
\end{bmatrix}^{\mathsf{T}}$
$\mathbf{g}$ ${: =}\begin{bmatrix} (16b)
{({g_{0} - g_{\star}})}^{\mathsf{T}} & \ldots & {({g_{K} - g_{\star}})}^{\mathsf{T}}
\end{bmatrix}^{\mathsf{T}}$
$\mathbf{f}$ ${: =}\begin{bmatrix} (16c)
{f_{0} - f_{\star}} & \ldots & {f_{K} - f_{\star}}
\end{bmatrix}^{\mathsf{T}}$

and denote the triple $\xi{: =}{(\mathbf{x},\mathbf{g},\mathbf{f})}$. Define $m_{ij}^{(K)} \in^{K + 1}$ and $M_{ij}^{(K)} \in {\mathbb{S}}^{N + K + 2}$ such that

for ${i,j} \in \mathcal{I}_{K}{: =}{\{ 0,\ldots,K, \star \}}$ where $\phi_{ij}$ is defined in (15. ‣ 5.1 Sampled Smooth Strongly Convex Functions ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")). Consider the quadratic function

where $Q \in {\mathbb{S}}^{N + K + 2}$ and $q \in^{N + 1}$. Suppose the dimension $d$ satisfies^33^3This requirement is only used for necessity. $d \geq {N + K + 2}$.

Then $\sigma$ is positive semidefinite (i.e., nonnegative) if and only if there exists $\tau_{ij} \geq 0$ for ${i,j} \in \mathcal{I}_{K}$ such that

$0$ $\preceq {Q - {\sum\limits_{{i,j} \in \mathcal{I}_{K}}{\tau_{ij}M_{ij}^{(K)}}}}$
$0$ ${\leq {q - {\sum\limits_{{i,j} \in \mathcal{I}_{K}}{\tau_{ij}m_{ij}^{(K)}}}}}.$

Furthermore, $\sigma$ is positive definite if and only if there exists $\tau_{ij} \geq 0$ for ${i,j} \in \mathcal{I}_{K}$ such that

$0$ $\prec {Q - {\sum\limits_{{i,j} \in \mathcal{I}_{K}}{\tau_{ij}M_{ij}^{(K)}}}}$ (19a)
$0$ ${< {q - {\sum\limits_{{i,j} \in \mathcal{I}_{K}}{\tau_{ij}m_{ij}^{(K)}}}}}.$ (19b)

Proof. We prove the second statement that $\sigma$ is positive definite if and only if there exists $\tau_{ij} \geq 0$ for ${i,j} \in \mathcal{I}_{K}$ such that (19. ‣ 5.2 Positive Definite Quadratics From Sampling ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) holds; the proof of the first statement is similar.

Here we prove that the conditions are sufficient for $\sigma$ to be positive definite; necessity is more involved and can be found in the supplementary material.

(Sufficiency). Suppose there exists $\tau_{ij} \geq 0$ for ${i,j} \in \mathcal{I}_{K}$ such that (19. ‣ 5.2 Positive Definite Quadratics From Sampling ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) holds. Clearly, we have ${\sigma{}} = 0$. Now assume that $\xi \neq 0$. Sum the following two inequalities: (i) take the Kronecker product of (19a. ‣ 5.2 Positive Definite Quadratics From Sampling ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) with $I_{d}$ and multiply the result on the left and right by $\begin{bmatrix}
\mathbf{x}^{\mathsf{T}} & \mathbf{g}^{\mathsf{T}}
\end{bmatrix}$ and its transpose, respectively, and (ii) multiply the tranpose of (19b. ‣ 5.2 Positive Definite Quadratics From Sampling ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) on the right by $\mathbf{f}$. Doing so gives the inequality

which is strict due to the strict inequalities in (19. ‣ 5.2 Positive Definite Quadratics From Sampling ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) and since $\xi \neq 0$. Since $f \in \mathcal{F}_{\mu,L}$, we have $\phi_{ij} \geq 0$ from Thm. 6. ‣ 5.1 Sampled Smooth Strongly Convex Functions ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees"), so

Then ${\sigma{(\xi)}} \geq 0$, and ${\sigma{(\xi)}} = 0$ if and only if $\xi = 0$. Finally, note that the strict inequalities in (19. ‣ 5.2 Positive Definite Quadratics From Sampling ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) imply that the right side of grows arbitrarily large as ${\|\xi\|}\rightarrow\infty$, so $\sigma$ is radially unbounded. Thus, $\sigma$ is positive definite.

### Remark 8

Theorem 7. ‣ 5.2 Positive Definite Quadratics From Sampling ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees") can be seen as a specialized application of the S-procedure where the points in $\xi$ are generated by method ($\mathcal{M}$), and the positive semidefinite quadratic terms come from the interpolation conditions in Theorem 6. ‣ 5.1 Sampled Smooth Strongly Convex Functions ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees"). While the S-procedure is known to be lossy in certain cases (i.e., the conditions are sufficient but not necessary for $\sigma$ to be positive (semi)definite), Theorem 7. ‣ 5.2 Positive Definite Quadratics From Sampling ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees") shows that it is in fact *lossless* under the large-scale assumption $d \geq {N + K + 2}$.

We now apply Theorem 7. ‣ 5.2 Positive Definite Quadratics From Sampling ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees") to obtain necessary and sufficient conditions for both $\mathcal{V}$ to be positive definite and ${\Delta\mathcal{V}}{: =}{{\mathcal{V}{(\xi_{k + 1})}} - {\rho^{2}\mathcal{V}{(\xi_{k})}}}$ to be negative semidefinite. To that end, note that the basis vectors ${\overline{x}}_{k}^{(K)}$, ${\overline{g}}_{k}^{(K)}$, and ${\overline{f}}_{k}^{(K)}$ in are such that

where $\mathbf{x}$, $\mathbf{g}$, and $\mathbf{f}$ are defined in (16. ‣ 5.2 Positive Definite Quadratics From Sampling ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) and we used the iterations in. We can then sum the following: (i) take the Kronecker product of $M_{ij}^{(K)}$ in (10 and 𝑚_{𝑖⁢𝑗}^(𝐾) are related to interpolation by smooth strongly convex functions as discussed in Section 5.1. ‣ 4.2 SDP for Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) with $I_{d}$ and multiply the result on the left and right by $\begin{bmatrix}
\mathbf{x}^{\mathsf{T}} & \mathbf{g}^{\mathsf{T}}
\end{bmatrix}$ and its transpose, respectively, and (ii) multiply the transpose of $m_{ij}^{(K)}$ on the right by $\mathbf{f}$. Adding these two quantities gives (17. ‣ 5.2 Positive Definite Quadratics From Sampling ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")). Similarly, the Lyapunov function in (5. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) is given by

and the decrease in the Lyapunov function is given by

using the definitions in and. This leads to the following results.

### Corollary 9 ($\mathcal{V}$ positive definite)

$\mathcal{V}$ in (5. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) is positive definite for all values of $d \in {\mathbb{N}}$ if and only if there exists $\lambda_{ij} \geq 0$ for ${i,j} \in \mathcal{I}_{N}$ such that

where $M_{ij}^{(N)}$ and $m_{ij}^{(N)}$ defined in (10 and 𝑚_{𝑖⁢𝑗}^(𝐾) are related to interpolation by smooth strongly convex functions as discussed in Section 5.1. ‣ 4.2 SDP for Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")).

Proof. The result follows from applying Theorem 7. ‣ 5.2 Positive Definite Quadratics From Sampling ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees") with $K = N$ to show that the quadratic function $\mathcal{V}$ in is positive definite.

### Corollary 10 ($\Delta\hspace{0pt}\mathcal{V}$ negative semidefinite)

Consider $\mathcal{V}$ in (5. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) and define ${\Delta\mathcal{V}}{: =}{{\mathcal{V}{(\xi_{k + 1})}} - {\rho^{2}\mathcal{V}{(\xi_{k})}}}$. Then $\Delta\mathcal{V}$ is negative semidefinite for all values of $d \in {\mathbb{N}}$ if and only if there exists $\eta_{ij} \geq 0$ for ${i,j} \in \mathcal{I}_{N + 1}$ such that

where $\DeltaV_{N}^{({N + 1})}$ and $\Deltav_{N}^{({N + 1})}$ are defined in.

Proof. The result follows from applying Theorem 7. ‣ 5.2 Positive Definite Quadratics From Sampling ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees") with $K = {N + 1}$ to show that the quadratic function $\Delta\mathcal{V}$ in is negative semidefinite.

Theorem 5. ‣ Step 5: Semidefinite program. ‣ 4.2 SDP for Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees") then follows from combining the results in Corollaries 9. ‣ 5.2 Positive Definite Quadratics From Sampling ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees") and 10. ‣ 5.2 Positive Definite Quadratics From Sampling ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees"). In particular, the inequalities in each corollary correspond to the constraints in the semidefinite program ($\rho$-SDP). If the problem is feasible, then $\mathcal{V}$ is positive definite and $\Delta\mathcal{V}$ is negative semidefinite at iteration $N$. Since this holds for any initial condition, we can apply the result for each $k \geq N$ to show that $\mathcal{V}$ is a valid Lyapunov function. On the other hand, if the problem is infeasible, then there exists no quadratic function of the form (5. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) such that $\mathcal{V}$ is positive definite and $\Delta\mathcal{V}$ is negative semidefinite, so no valid quadratic Lyapunov function with state $\xi_{k}$ exists for the given rate $\rho$. This completes the proof of Thm. 5. ‣ Step 5: Semidefinite program. ‣ 4.2 SDP for Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees").

## Extensions

Our main result in Theorem 5. ‣ Step 5: Semidefinite program. ‣ 4.2 SDP for Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees") applies to methods of the form ($\mathcal{M}$) with fixed step-sizes applied to smooth strongly convex functions. Our framework, however, can be extended to many other scenarios, with or without tightness.

We now proceed with some examples of how our procedure of searching for Lyapunov functions can serve as a basis for the analysis of many *exotic* algorithms. We provide two such examples: (i) the analysis of variants of GM and HBM involving subspace searches, and (ii) the analysis of a fast gradient scheme with scheduled restarts.

### Exact Line Searches

In this section, we search for quadratic Lyapunov functions when it is possible to perform an exact line search. We illustrate the procedure on steepest descent

and on a variant of HBM:

The detailed analyses can be found in the supplementary material, whereas the results are presented on Figure 3.

Figure 3: Convergence rates of GM and HBM with subspace searches. Note that the Gradient Method with exact line search matches the worst-case rate $\frac{\kappa - 1}{\kappa + 1}$ from. For comparison, the rates of the Gradient Method with step-size 1/L and the Triple Momentum Method are also shown.

### Scheduled Restarts

In this section, we apply the methodology to estimate the convergence rate of FGM with scheduled restarts; motivations for this kind of techniques can be found in e.g.,. We present numerical guarantees obtained when using a version of FGM tailored for smooth convex minimization, which is restarted every $N$ iterations. This setting goes slightly beyond the fixed-step model presented in ($\mathcal{M}$), as the step-size rules depend on the iteration counter.

Define $\beta_{0}{: =}1$ and $\beta_{i + 1}{: =}\frac{1 + \sqrt{{4\beta_{i}^{2}} + 1}}{2}$; we use the following iterative procedure

which does $N$ steps of the standard fast gradient method before restarting. We study the convergence of this scheme using quadratic Lyapunov functions with states $({y_{k}^{N} - y_{\star}},{{\nabla f}{(y_{k}^{N})}},{{f{(y_{k}^{N})}} - {f{(y_{\star})}}})$. The derivations of the SDP for verifying $\mathcal{V}_{k + 1} \leq {\rho^{2N}\mathcal{V}_{k}}$ (where $\rho^{N}$ is the convergence rate of the inner loop) is similar to that of ($\rho$-SDP) (details in supplementary material). Numerical results are provided in Figure 4.

Figure 4: Worst-case number of gradient evaluations to convergence 𝒪 (−1/log ρ) for different restart schedules N (purple) along with the optimal restart schedule N⋆ = arg minNρ (N) (dashed blue). For comparison, we also plot the upper bound ${\rho{(N_{\star})}} \leq {\exp\left( \frac{- 1}{e\sqrt{8\kappa}} \right)}$ (dashed black) from. Results are not shown for small κ due to numerical limitations of the SDP solvers.

## Conclusion

In this work, we studied first-order iterative fixed-step methods applied to smooth strongly convex functions. We presented a semidefinite formulation whose feasibility is both necessary and sufficient for the existence of a quadratic Lyapunov function. For smooth strongly convex minimization, restriction to quadratic Lyapunov functions is natural, as nonlinearities are exactly characterized by quadratic interpolation constraints. Using other tools such as sum-of-squares Lyapunov functions (see e.g., Parrilo ) could be beneficial for more general algorithm and problem classes.

This methodology unifies two previous approaches to worst-case analyses: performance estimation due to Drori & Teboulle and integral quadratic constraints due to Lessard et al.. Moreover, this approach admits a large number of potential extensions, both in terms of classes of optimization problems and types of algorithms that can be analyzed (see e.g., extensions for performance estimation ). In particular, Lyapunov functions can be used to study sublinear convergence rates (see e.g., Hu & Lessard ), switched systems (e.g., for adaptive methods), noisy methods (see e.g., Cyrus et al. ), or continuous-time settings such as in.

### Code

The code used to implement ($\rho$-SDP) and generate the figures in this paper is available at [https://github.com/QCGroup/quad-lyap-first-order](https://github.com/QCGroup/quad-lyap-first-order).
