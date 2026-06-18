<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees

Topics include Semidefinite programming, Lyapunov methods, Optimization, Automated convergence proofs, Lyapunov functions.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a novel way of generating Lyapunov functions for proving linear convergence rates of first-order optimization methods. Our approach provably obtains the fastest linear convergence rate that can be verified by a quadratic Lyapunov function (with given states), and only relies on solving a small-sized semidefinite program. Our approach combines the advantages of performance estimation problems (PEP, due to Drori & Teboulle ) and integral quadratic constraints (IQC, due to Lessard et al. ), and relies on convex interpolation (due to Taylor et al. ).

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we study first-order methods for solving the (unconstrained) minimization problem

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

where $f:^{d}\rightarrow$. In the sequel, we focus on the case where $f$ is $L$-smooth and $\mu$-strongly convex, though our methodology can be adapted to a broader class of problems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

To solve ($\mathcal{P}$), we consider methods that iteratively update their estimate of the optimizer using only gradient evaluations. One possibility for proving convergence of such methods is by finding *Lyapunov functions*.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

A Lyapunov function can be interpreted as defining an "energy" that decreases geometrically with each iteration of the method, with an energy of zero corresponding to reaching the optimal solution of ($\mathcal{P}$). The existence of such an energy function thus provides a straightforward certificate of linear convergence for the iterative method.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we present an automated way of generating quadratic Lyapunov functions for certifying linear convergence of first-order iterative methods to solve ($\mathcal{P}$). The procedure relies on solving a small-sized semidefinite program (SDP) so it is computationally efficient. Moreover, the procedure is *tight*, meaning that if the SDP is infeasible, then no such quadratic Lyapunov function exists.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our results unify recent SDP-based works for certifying convergence of first-order methods, namely: performance estimation problems and integral quadratic constraints from robust control, using smooth strongly convex interpolation. These connections are further discussed in Section 4.3.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Organization", "weight": 1.0} -->

The paper is organized as follows. We describe the class of methods under consideration and basic properties of Lyapunov functions in Sections 2 and 3 respectively. Our main results are then presented in Section 4, which also features numerical examples and comparisons to other approaches. The corresponding proof is presented in Section 5. Finally, we explore extensions of our approach in Section 6, and conclude in Section 7.

<!-- chunk {"id": "body-0010", "role": "body", "section": "First-Order Iterative Fixed-Step Methods", "weight": 1.0} -->

To solve the optimization problem ($\mathcal{P}$), we consider *first-order iterative fixed-step methods* of the form

<!-- chunk {"id": "body-0011", "role": "body", "section": "First-Order Iterative Fixed-Step Methods", "weight": 1.0} -->

for $k \geq 0$ where $\alpha$, $\beta_{j}$, $\gamma_{j}$ are the (fixed) step-sizes and $x_{j} \in^{d}$ for $j = {{- N},\ldots,0}$ are the initial conditions. We call the constant $N \geq 0$ the *degree* of the method.

<!-- chunk {"id": "body-0012", "role": "body", "section": "First-Order Iterative Fixed-Step Methods", "weight": 1.0} -->

Many first-order optimization methods are of the form ($\mathcal{M}$), including: the Gradient Method, Heavy Ball Method, Fast Gradient Method for smooth strongly convex minimization, Triple Momentum Method, and Robust Momentum Method.

<!-- chunk {"id": "body-0013", "role": "body", "section": "First-Order Iterative Fixed-Step Methods", "weight": 1.0} -->

For method ($\mathcal{M}$) to solve ($\mathcal{P}$), it must have a fixed-point at the optimizer $x_{\star}$. Hence, we require the step-sizes to satisfy

<!-- chunk {"id": "body-0014", "role": "body", "section": "What is a Lyapunov Function?", "weight": 1.0} -->

Lyapunov functions are one of the fundamental tools in control theory that can be used to verify stability of a dynamical system.

<!-- chunk {"id": "body-0015", "role": "body", "section": "What is a Lyapunov Function?", "weight": 1.0} -->

Consider applying method ($\mathcal{M}$) to solve problem ($\mathcal{P}$). Our goal is to find the smallest possible $0 \leq \rho < 1$ such that $\{ x_{k}\}$ converges linearly to the optimizer $x_{\star}$ with rate $\rho$.

<!-- chunk {"id": "body-0016", "role": "body", "section": "What is a Lyapunov Function?", "weight": 1.0} -->

where $\xi_{k}{: =}{(\mathbf{x}_{k},\mathbf{g}_{k},\mathbf{f}_{k})}$ is the *state* of the system at iteration $k$. The state at iteration $k$ includes past iterates, function values, and gradient values from iterations $k - N$ up to $k$. If we can find such a $\mathcal{V}$, then it can be used to show that the state converges linearly to the fixed-point from any initial condition (the rate of convergence depends on both $\rho$ and the structure of $\mathcal{V}$).

<!-- chunk {"id": "body-0017", "role": "body", "section": "What is a Lyapunov Function?", "weight": 1.0} -->

Lyapunov functions are typically found by searching over a parameterized family of functions (called Lyapunov function candidates). In the simple case where the state $\{\xi_{k}\}$ is generated by a linear dynamical system, one can search over quadratic Lyapunov function candidates by solving a semidefinite program, as illustrated in Example 1. ‣ 3 What is a Lyapunov Function? ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees") below.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Example 1 (Quadratic Lyapunov function)", "weight": 1.0} -->

Consider the linear dynamical system described by

<!-- chunk {"id": "body-0019", "role": "body", "section": "Example 1 (Quadratic Lyapunov function)", "weight": 1.0} -->

has solution $P_{\star}$. Then a Lyapunov function for the system is

<!-- chunk {"id": "body-0020", "role": "body", "section": "Example 1 (Quadratic Lyapunov function)", "weight": 1.0} -->

which can be used to show that $\xi_{k}\rightarrow\xi_{\star}$ linearly with rate $\rho$. Specifically, we have the bound

<!-- chunk {"id": "body-0021", "role": "body", "section": "Example 1 (Quadratic Lyapunov function)", "weight": 1.0} -->

To find the best bound, we can perform a bisection search on $\rho$ to find the smallest $\rho$ such that (4. ‣ 3 What is a Lyapunov Function? ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) is feasible.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Example 1 (Quadratic Lyapunov function)", "weight": 1.0} -->

Note that although $\mathcal{V}$ depends explicitly on the fixed point $\xi_{\star}$, we do not need to know $\xi_{\star}$ to solve the SDP (4. ‣ 3 What is a Lyapunov Function? ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")).

<!-- chunk {"id": "body-0023", "role": "body", "section": "Example 1 (Quadratic Lyapunov function)", "weight": 1.0} -->

The linear dynamical system of Example 1. ‣ 3 What is a Lyapunov Function? ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees") converges linearly if and only if a quadratic Lyapunov function exists, which happens if and only if the SDP (4. ‣ 3 What is a Lyapunov Function? ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) is feasible.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Main Results", "weight": 1.0} -->

Similar to Example 1. ‣ 3 What is a Lyapunov Function? ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees"), we now show how to use quadratic Lyapunov functions to prove linear convergence of a first-order iterative fixed-step method applied to the minimization of a smooth strongly convex function. Furthermore, we show that such Lyapunov function exists if and only if a small-sized semidefinite program is feasible (whose optimal solution produces the Lyapunov function).

<!-- chunk {"id": "body-0025", "role": "body", "section": "Quadratic Lyapunov Functions", "weight": 1.0} -->

We begin with sufficiency: if we can find a quadratic Lyapunov function, we can use it to prove linear convergence.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Remark 3", "weight": 1.0} -->

The Lyapunov function (5. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) is only defined for $k \geq N$ since the state $\xi_{k}$ is a function of the previous $N$ function and gradient values. This is why the bound (6. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) is expressed in terms of $\mathcal{V}{(\xi_{N})}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Remark 4", "weight": 1.0} -->

The states used in the Lyapunov function (5. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) can be modified to include other iterates (such as $y_{k}$) in the quadratic term as well as the function and gradient values evaluated at iterates other than $y_{k}$. We chose the form in (5. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) because it contains all necessary ingredients while also being straightforward to generalize to other cases.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Remark 4", "weight": 1.0} -->

In addition, note that the structure of (5. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) makes it *permutation-invariant* (i.e., it does not depend on the ordering of the coordinate set). This is largely motivated by the fact that there is no reason to favor any coordinate among ^d^.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Remark 4", "weight": 1.0} -->

Lemma 2. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees") shows that if we can find a quadratic Lyapunov function, then we can use this to prove linear convergence of method ($\mathcal{M}$) when $f \in \mathcal{F}_{\mu,L}$. In the following section, we construct an SDP whose feasibility is necessary and sufficient for the existence of such a Lyapunov function.

<!-- chunk {"id": "body-0030", "role": "body", "section": "SDP for Quadratic Lyapunov Functions", "weight": 1.0} -->

Given parameters $\alpha$, $\beta_{j}$, and $\gamma_{j}$ for a method ($\mathcal{M}$) of degree $N$ and a rate $\rho$ to be verified, we construct the semidefinite program as follows.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Step 1: Initialization", "weight": 1.0} -->

First, we initialize the row vectors ${{\overline{x}}_{k}^{(K)},{\overline{g}}_{k}^{(K)}} \in^{N + K + 2}$ and ${\overline{f}}_{k}^{(K)} \in^{K + 1}$, corresponding to the initial conditions, gradient values, and function values, respectively, as

<!-- chunk {"id": "body-0032", "role": "body", "section": "Step 1: Initialization", "weight": 1.0} -->

for $K \in {\{ N,{N + 1}\}}$ ($\mathbf{e}_{i}$ denotes the $i^{\text{th}}$ unit vector with appropriate dimension). These form a basis for all iterates, function values, and gradient values up to iteration $K$. Also, define the row vectors corresponding to the fixed-point as

<!-- chunk {"id": "body-0033", "role": "body", "section": "Step 2: Method", "weight": 1.0} -->

Next, we iterate the method for $k = {0,\ldots,K}$ using the row vectors we previously defined.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Step 4: Lyapunov function", "weight": 1.0} -->

We now construct the linear and quadratic terms in the Lyapunov function, denoted $v_{k}^{(K)} \in^{K + 1}$ and $V_{k}^{(K)} \in {\mathbb{S}}^{N + K + 2}$, respectively, as

<!-- chunk {"id": "body-0035", "role": "body", "section": "Step 4: Lyapunov function", "weight": 1.0} -->

Also, define the decrease in the linear and quadratic terms of the Lyapunov function as

<!-- chunk {"id": "body-0036", "role": "body", "section": "Step 4: Lyapunov function", "weight": 1.0} -->

where $\rho$ is the convergence rate to be verified.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Comparison to PEP and IQC", "weight": 1.0} -->

Our results are closely related to several other recent approaches utilizing semidefinite programs for studying convergence of first-order methods, which we discuss now.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Performance Estimation Problem (PEP)", "weight": 1.0} -->

The performance estimation approach was introduced by Drori & Teboulle as a systematic way to obtain worst-case performance guarantees of a given method. In the context of fixed-step first-order methods, performance estimation problems (PEP) can be formulated as semidefinite programs.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Performance Estimation Problem (PEP)", "weight": 1.0} -->

The key idea in PEP is to look for a tuple $(x_{- N},\ldots,x_{0},f)$ such that the given algorithm behaves in the worst possible way, according to a given performance measure. The dual of PEP corresponding to the performance measure ${{\mathcal{V}{(\xi_{N + 1})}}/\mathcal{V}}{(\xi_{N})}$ for some fixed $P$ and $p$ is exactly the same as solving $\min_{\rho}\rho^{2}$ subject to ($\rho$-SDP) being feasible.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Performance Estimation Problem (PEP)", "weight": 1.0} -->

The difference between PEP and our approach is that in PEP, the optimization is for a fixed performance measure carried out over multiple timesteps. This yields exact worst-case bounds, but at the cost of solving an SDP whose size is proportional to the number of timesteps (this allows, among others, dealing with time-varying methods and sublinear convergence rates). In our approach, for a fixed $\rho$, we optimize the performance measure itself. This yields a Lyapunov function with a guaranteed decrease at every iteration while maintaining tightness and solving a small SDP of fixed size. Both approaches ensure tightness via *(smooth) convex interpolation*, developed by Taylor et al..

<!-- chunk {"id": "body-0041", "role": "body", "section": "Integral Quadratic Constraints (IQCs)", "weight": 1.0} -->

Integral quadratic constraints are an analysis method for bounding the worst-case performance of dynamical systems in feedback with nonlinearities. This approach was recently adapted for use in analyzing first-order optimization algorithms. In the optimization context, the nonlinear component is the gradient of the objective function, while the dynamical system is the iterative method being analyzed.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Integral Quadratic Constraints (IQCs)", "weight": 1.0} -->

The key idea with IQCs is to replace the nonlinearity ($\nabla f$) by quadratic constraints that it must satisfy. This is precisely the idea behind *interpolation* (discussed in Section 5.1), which is a foundational concept in our methodology.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Integral Quadratic Constraints (IQCs)", "weight": 1.0} -->

The difference between IQCs and our approach is that the interpolation conditions are necessary and sufficient to characterize $\nabla f$ when $f \in \mathcal{F}_{\mu,L}$. However, the sector IQC and weighted off-by-one IQC used by Lessard et al. are a strict subset of the interpolation conditions; they are only sufficient for describing $\nabla f$ when $f \in \mathcal{F}_{\mu,L}$. In particular, the IQC framework does not use any constraints on $\nabla f$ that explicitly involve function values. This amounts to solving ($\rho$-SDP) with additional constraints on $\lambda_{ij}$ and $\eta_{ij}$ such that all the function values cancel out in the SDP.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Numerical Comparisons", "weight": 1.0} -->

To illustrate our results, we consider the Gradient Method (GM), Heavy Ball Method (HBM), Fast Gradient Method (FGM), and Triple Momentum Method (TMM). Each of these methods can be parametrized as

<!-- chunk {"id": "body-0045", "role": "body", "section": "Numerical Comparisons", "weight": 1.0} -->

We use ($\rho$-SDP) to find corresponding Lyapunov functions. The corresponding convergence rates are provided in Figure 1; the results match those obtained using IQCs for GM, HBM, and FGM, and those for TMM provided. For more complicated cases, the performance estimation toolbox PESTO can be used to perform numerical validations.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Numerical Comparisons", "weight": 1.0} -->

For illustrative purposes, we present results obtained using a restricted class of Lyapunov functions. We fixed $\lambda_{ij} = 0$ in ($\rho$-SDP) and plotted the best achievable $\rho$ in Figure 2. We observe that this restricted class is not sufficient to recover the rates obtained in Figure 1.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Sampled Smooth Strongly Convex Functions", "weight": 1.0} -->

To prove Theorem 5. ‣ Step 5: Semidefinite program. ‣ 4.2 SDP for Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees"), we first need a result on smooth strongly convex functions that are sampled at discrete points. Indeed, inequalities and completely characterize functions that are smooth and strongly convex. However, these inequalities are defined on an infinite set of points, and it was shown in Section 2.2 of that using them to prove convergence may introduce conservatism. Therefore, in order to completely characterize points which are sampled from smooth strongly convex functions, we need the concept of *interpolation*.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Sampled Smooth Strongly Convex Functions", "weight": 1.0} -->

The following theorem is borrowed from and forms the basic building block for our analysis.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Positive Definite Quadratics From Sampling", "weight": 1.0} -->

Recall from Section 3 that the Lyapunov function must satisfy two conditions: (i) $\mathcal{V}$ must be positive definite (i.e, nonnegative, zero at the fixed-point, and radially unbounded), and (ii) ${\Delta\mathcal{V}}{: =}{\mathcal{V}_{k + 1} - {\rho^{2}\mathcal{V}_{k}}}$ must be negative semidefinite (i.e., $\mathcal{V}$ must satisfy the decrease condition). To prove both (i) and (ii), we use the following theorem, which provides necessary and sufficient conditions for a quadratic form to be positive (semi-)definite when the iterates are generated by method ($\mathcal{M}$) applied to $f \in \mathcal{F}_{\mu,L}$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 8", "weight": 1.0} -->

Theorem 7. ‣ 5.2 Positive Definite Quadratics From Sampling ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees") can be seen as a specialized application of the S-procedure where the points in $\xi$ are generated by method ($\mathcal{M}$), and the positive semidefinite quadratic terms come from the interpolation conditions in Theorem 6. ‣ 5.1 Sampled Smooth Strongly Convex Functions ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees"). While the S-procedure is known to be lossy in certain cases (i.e., the conditions are sufficient but not necessary for $\sigma$ to be positive (semi)definite), Theorem 7. ‣ 5.2 Positive Definite Quadratics From Sampling ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees") shows that it is in fact *lossless* under the large-scale assumption $d \geq {N + K + 2}$.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 8", "weight": 1.0} -->

We now apply Theorem 7. ‣ 5.2 Positive Definite Quadratics From Sampling ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees") to obtain necessary and sufficient conditions for both $\mathcal{V}$ to be positive definite and ${\Delta\mathcal{V}}{: =}{{\mathcal{V}{(\xi_{k + 1})}} - {\rho^{2}\mathcal{V}{(\xi_{k})}}}$ to be negative semidefinite. To that end, note that the basis vectors ${\overline{x}}_{k}^{(K)}$, ${\overline{g}}_{k}^{(K)}$, and ${\overline{f}}_{k}^{(K)}$ in are such that

<!-- chunk {"id": "body-0052", "role": "body", "section": "Remark 8", "weight": 1.0} -->

where $\mathbf{x}$, $\mathbf{g}$, and $\mathbf{f}$ are defined in (16. ‣ 5.2 Positive Definite Quadratics From Sampling ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) and we used the iterations. We can then sum the following: (i) take the Kronecker product of $M_{ij}^{(K)}$ in (10 and 𝑚_{𝑖⁢𝑗}^(𝐾) are related to interpolation by smooth strongly convex functions as discussed in Section 5.1.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Remark 8", "weight": 1.0} -->

‣ 4.2 SDP for Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) with $I_{d}$ and multiply the result on the left and right by $\begin{bmatrix}
\mathbf{x}^{\mathsf{T}} & \mathbf{g}^{\mathsf{T}}
\end{bmatrix}$ and its transpose, respectively, and (ii) multiply the transpose of $m_{ij}^{(K)}$ on the right by $\mathbf{f}$. Adding these two quantities gives (17. ‣ 5.2 Positive Definite Quadratics From Sampling ‣ 5 Proof of Theorem 5 ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")). Similarly, the Lyapunov function in (5. ‣ 4.1 Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees")) is given by

<!-- chunk {"id": "body-0054", "role": "body", "section": "Remark 8", "weight": 1.0} -->

and the decrease in the Lyapunov function is given by

<!-- chunk {"id": "body-0055", "role": "body", "section": "Remark 8", "weight": 1.0} -->

using the definitions in and. This leads to the following results.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Extensions", "weight": 1.0} -->

Our main result in Theorem 5. ‣ Step 5: Semidefinite program. ‣ 4.2 SDP for Quadratic Lyapunov Functions ‣ 4 Main Results ‣ Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees") applies to methods of the form ($\mathcal{M}$) with fixed step-sizes applied to smooth strongly convex functions. Our framework, however, can be extended to many other scenarios, with or without tightness.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Extensions", "weight": 1.0} -->

We now proceed with some examples of how our procedure of searching for Lyapunov functions can serve as a basis for the analysis of many *exotic* algorithms. We provide two such examples: (i) the analysis of variants of GM and HBM involving subspace searches, and (ii) the analysis of a fast gradient scheme with scheduled restarts.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Exact Line Searches", "weight": 1.0} -->

In this section, we search for quadratic Lyapunov functions when it is possible to perform an exact line search. We illustrate the procedure on steepest descent

<!-- chunk {"id": "body-0059", "role": "body", "section": "Exact Line Searches", "weight": 1.0} -->

The detailed analyses can be found in the supplementary material, whereas the results are presented on Figure 3.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Scheduled Restarts", "weight": 1.0} -->

In this section, we apply the methodology to estimate the convergence rate of FGM with scheduled restarts; motivations for this kind of techniques can be found in e.g.,. We present numerical guarantees obtained when using a version of FGM tailored for smooth convex minimization, which is restarted every $N$ iterations. This setting goes slightly beyond the fixed-step model presented in ($\mathcal{M}$), as the step-size rules depend on the iteration counter.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Scheduled Restarts", "weight": 1.0} -->

which does $N$ steps of the standard fast gradient method before restarting. We study the convergence of this scheme using quadratic Lyapunov functions with states $({y_{k}^{N} - y_{\star}},{{\nabla f}{(y_{k}^{N})}},{{f{(y_{k}^{N})}} - {f{(y_{\star})}}})$. The derivations of the SDP for verifying $\mathcal{V}_{k + 1} \leq {\rho^{2N}\mathcal{V}_{k}}$ (where $\rho^{N}$ is the convergence rate of the inner loop) is similar to that of ($\rho$-SDP) (details in supplementary material). Numerical results are provided in Figure 4.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this work, we studied first-order iterative fixed-step methods applied to smooth strongly convex functions. We presented a semidefinite formulation whose feasibility is both necessary and sufficient for the existence of a quadratic Lyapunov function. For smooth strongly convex minimization, restriction to quadratic Lyapunov functions is natural, as nonlinearities are exactly characterized by quadratic interpolation constraints. Using other tools such as sum-of-squares Lyapunov functions (see e.g., Parrilo ) could be beneficial for more general algorithm and problem classes.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Conclusion", "weight": 1.5} -->

This methodology unifies two previous approaches to worst-case analyses: performance estimation due to Drori & Teboulle and integral quadratic constraints due to Lessard et al.. Moreover, this approach admits a large number of potential extensions, both in terms of classes of optimization problems and types of algorithms that can be analyzed (see e.g., extensions for performance estimation ). In particular, Lyapunov functions can be used to study sublinear convergence rates (see e.g., Hu & Lessard ), switched systems (e.g., for adaptive methods), noisy methods (see e.g., Cyrus et al. ), or continuous-time settings such as.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Code", "weight": 1.0} -->

The code used to implement ($\rho$-SDP) and generate the figures in
