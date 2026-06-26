<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints

Topics include Semidefinite programming, Stability analysis, Robustness, Optimization, Control, IQC.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This manuscript develops a new framework to analyze and design iterative optimization algorithms built on the notion of Integral Quadratic Constraints (IQC) from robust control theory. IQCs provide sufficient conditions for the stability of complicated interconnected systems, and these conditions can be checked by semidefinite programming. We discuss how to adapt IQC theory to study optimization algorithms, proving new inequalities about convex functions and providing a version of IQC theory adapted for use by optimization researchers. Using these inequalities, we derive numerical upper bounds on convergence rates for the gradient method, the heavy-ball method, Nesterov's accelerated method, and related variants by solving small, simple semidefinite programming problems. We also briefly show how these techniques can be used to search for optimization algorithms with desired performance characteristics, establishing a new methodology for algorithm design.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Convex optimization algorithms provide a powerful toolkit for robust, efficient, large-scale optimization algorithms. They provide not only effective tools for solving optimization problems, but are guaranteed to converge to accurate solutions in provided time budgets, are robust to errors and time delays, and are amendable to declarative modeling that decouples the algorithm design from the problem formulation. However, as we push up against the boundaries of the convex analysis framework, try to build more complicated models, and aim to deploy optimization systems in highly complex environments, the mathematical guarantees of convexity start to break. The standard proof techniques for analyzing convex optimization rely on deep insights by experts and are devised on an algorithm-by-algorithm basis. It is thus not clear how to extend the toolkit to more diverse scenarios where multiple objectives---such as robustness, accuracy, and speed---need to be delicately balanced.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper marks an attempt at providing a systematized approach to the design and analysis optimization algorithms using techniques from control theory. Our strategy is to adapt the notion of an *integral quadratic constraint* from robust control theory. These constraints link sequences of inputs and outputs of operators, and are ideally suited to proving algorithmic convergence. We will see that for convex functions, we can derive these constraints using only the standard first-order characterization of convex functions, and that these inequalities will be sufficient to reduce the analysis of first-order methods to the solution of a very small semidefinite program. Our IQC framework puts the analysis of algorithms in a unified proof framework, and enables new analyses of algorithms by minor perturbations of existing proofs. This new system aims to simplify and automate the analysis of optimization programs, and perhaps to open new directions for algorithm design.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our methods are inspired by the recent work of Drori and Teboulle. In their manuscript, the authors propose writing down the first-order convexity inequality for all steps of an algorithmic procedure. They then derive a semidefinite program that analytically verifies very tight bounds for the convergence rate for the Gradient method, and numerically precise bounds for convergence of Nesterov's method and other first-order methods. The main drawback of the Drori and Teboulle approach is that the size of the semidefinite program scales with the number of time steps desired. Thus, it becomes computationally laborious to analyze algorithms that require more than a few hundred iterations.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Integral quadratic constraints will allow us to circumvent this issue. A typical example of one of our semidefinite programs might have a $3 \times 3$ positive semidefinite decision variable, 3 scalar variables, a $5 \times 5$ semidefinite cone constraint, and 4 scalar constraints. Such a problem can be solved in less than 10 milliseconds on a laptop with standard solvers.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We are able to analyze a variety of methods in our framework. We show that our framework recovers the standard rates of convergence for the Gradient method applied to strongly convex functions. We show that we can numerically estimate the performance of Nesterov's method. Indeed, our analysis provides slightly sharper bounds than Nesterov's proof. We show how our system fails to certify the stability of the popular Heavy-ball method of Polyak for strongly convex functions whose condition ratio is larger than 18. Based on this analysis, we are able to construct a one-dimensional strongly convex function whose condition ratio is 25 and prove analytically that the Heavy-ball method fails to find the global minimum of this function. This suggests that our tools can also be used as a way to guide the construction of counterexamples.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We show that our methods extend immediately to the projected and proximal variants of all the first order methods we analyze. We also show how to extend our analysis to functions that are convex but not strongly convex, and provide bounds on convergence that are within a logarithmic factor of the best upper bounds. We also demonstrate that our methods can bound convergence rates when the gradient is perturbed by relative deterministic noise. We show how different parameter settings lead to very different degradations in performance bounds as the noise increases.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we turn to algorithm *design*. Since our semidefinite program takes as input the parameters of our iterative scheme, we can search over these parameters. For simple two-step methods, our algorithms are parameterized by 3 parameters, and we show how we can derive first-order methods that achieve nearly the same rate of convergence as Nesterov's accelerated method but are more robust to noise.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

The manuscript is organized as follows. We begin with a discussion of discrete-time dynamical system and how common optimization algorithms can be viewed as feedback interconnections between a known *linear* system with an uncertain *nonlinear* component. We then turn to show how quadratic Lyapunov functions can be used to certify rates of convergence for optimization problems and can be found by semidefinite programming. This immediately leads to the notion of an integral quadratic constraint. Another contribution of this work is a new form of IQC analysis geared specifically toward rate-of-convergence conclusions, and accessible to optimization researchers. We also discuss their history in robust control theory and how they can be derived. With these basic IQCs in hand, we then turn to analyzing the Gradient method and Nesterov method, their projected and proximal variants, and their robustness to noise. We discuss one possible brute-force technique for designing new algorithms, and how we can outperform existing methods. Finally, we conclude with many directions for future work.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Common matrices", "weight": 1.0} -->

The $d \times d$ identity matrix and zero matrix are denoted $I_{d}$ and $0_{d}$, respectively. Subscripts are omitted when they are to be inferred by context.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Norms and sequences", "weight": 1.0} -->

We define $\ell_{2e}^{n}$ to be the set of all one-sided sequences $x:{{\mathbb{N}}\rightarrow{\mathbb{R}}^{n}}$. We sometimes omit $n$ and simply write $\ell_{2e}$ when the superscript is clear from context. The notation $\parallel \cdot \parallel:{\mathbb{R}}^{n}\rightarrow{\mathbb{R}}$ denotes the standard 2-norm. The subset $\ell_{2} \subset \ell_{2e}$ consists of all square-summable sequences. In other words, $x \in \ell_{2}$ if and only if $\sum_{k = 0}^{\infty}{\| x_{k}\|}^{2}$ is convergent.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Convex functions", "weight": 1.0} -->

For a given $0 < m < L$, we define $S{(m,L)}$ to be the set of functions $f:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}}$ that are continuously differentiable, strongly convex with parameter $m$, and have Lipschitz gradients with parameter $L$. In other words, $f$ satisfies We call $\kappa{: =}{L/m}$ the *condition ratio* of $f \in {S{(m,L)}}$. We adopt this terminology to distinguish the condition ratio of a function from the related concept of *condition number* of a matrix. The connection is that if $f$ is twice differentiable, we have the bound: ${{cond}{({{\nabla^{2}f}{(x)}})}} \leq \kappa$ for all $x \in {\mathbb{R}}^{d}$, where ${cond}{(\cdot)}$ is the condition number.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Optimization algorithms as dynamical systems", "weight": 1.0} -->

A linear dynamical system is a set of recursive linear equations of the form At each timestep $k = {0,1,\ldots}$, $u_{k} \in {\mathbb{R}}^{d}$ is the *input*, $y_{k} \in {\mathbb{R}}^{d}$ is the *output*, and $\xi_{k} \in {\mathbb{R}}^{m}$ is the *state*. We can write the dynamical system (2.1) compactly by stacking the matrices into a block using the notation We can connect this linear system in *feedback* with a nonlinearity $\phi$ by defining the rule In this case, the output is transformed by the map $\phi:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$ and is then used as the input to the linear system.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Optimization algorithms as dynamical systems", "weight": 1.0} -->

In this paper, we will be interested in the case when the interconnected nonlinearity has the form ${\phi{(y)}} = {{\nabla f}{(y)}}$ where $f \in {S{(m,L)}}$. In particular, we will consider algorithms designed to solve the optimization problem as dynamical systems and see how this new viewpoint can give us insights into convergence analysis. Section 5.3 considers variants of (2.3) where the decision variable $x$ is constrained or $f$ is non-smooth.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Optimization algorithms as dynamical systems", "weight": 1.0} -->

Standard first order methods such as the Gradient method, Heavy-ball method, and Nesterov's accelerated method, can all be cast in the form (2.2). In all cases, the nonlinearity is the mapping ${\phi{(y)}} = {{\nabla f}{(y)}}$. The state transition matrices $A$, $B$, $C$, $D$ differ for each algorithm. The Gradient method can be expressed as To verify this, substitute (2.4) into (2.2) and obtain Eliminating $y_{k}$ and $u_{k}$ and renaming $\xi$ to $x$ yields which is the familiar Gradient method with constant stepsize. Nesterov's accelerated method for strongly convex functions is given by the dynamical system Verifying that (2.5) is equivalent to Nesterov's method takes only slightly more effort than it did for the Gradient method.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Optimization algorithms as dynamical systems", "weight": 1.0} -->

Substituting (2.5) into (2.2) now yields Note that (2.6b) asserts that the partial state $\xi^{}$ is a delayed version of the state $\xi^{}$. Substituting (2.6b) into (2.6a) gives the simplified system Eliminating $u_{k}$ and renaming $\xi^{}$ to $x$ yields the common form of Nesterov's method Note that other variants of this algorithm exist for which the $\alpha$ and $\beta$ parameters are updated at each iteration. In this paper, we restrict our analysis to the constant-parameter version above. The Heavy-ball method is given by One can check by similar analysis that (2.7) is equivalent to the update rule

<!-- chunk {"id": "body-0018", "role": "body", "section": "Proving algorithm convergence", "weight": 1.0} -->

Convergence analysis of convex optimization algorithms typically follows a two step procedure. First one must show that the algorithm has a fixed point that solves the optimization problem in question. Then, one must verify that from a reasonable starting point, the algorithm converges to this optimal solution at a specified rate.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Proving algorithm convergence", "weight": 1.0} -->

In dynamical systems, such proofs are called stability analysis. By writing common first order methods as dynamical systems, we can unify their stability analysis. For a general problem with minimum occurring at $y_{\star}$, a necessary condition for optimality is that $u_{\star} = {{\nabla f}{(y_{\star})}} = 0$. Substituting into (2.1), the fixed point satisfies In particular, $A$ must have an eigenvalue of $1$. If the blocks of $A$ are diagonal as in the Gradient, Heavy-ball, or Nesterov methods shown above, then the eigenvalue of $1$ will have a geometric multiplicity of at least $d$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Proving algorithm convergence", "weight": 1.0} -->

Proving that all paths lead to the optimal solution requires more effort and constitutes the bulk of what is studied herein. Before we proceed for general convex $f$, it is instructive to study what happens for quadratic $f$.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Quadratic problems", "weight": 1.0} -->

What happens when we run a first order method on a quadratic problem? Assume throughout this section that $D = 0$. Substituting the equation for $y_{\star}$ and ${\nabla f}{(y)}$ back into (2.2), we obtain the system of equations: Now make use of the fixed-point equations $y_{\star} = {C\xi_{\star}}$ and $\xi_{\star} = {A\xi_{\star}}$ and we obtain $u_{k} = {QC{({\xi_{k} - \xi_{\star}})}}$. Eliminating $y_{k}$ and $u_{k}$ from the above equations, we obtain Let $T{: =}{A + {BQC}}$ denote the closed-loop state transition matrix. A necessary and sufficient condition for $\xi_{k}$ to converge to $\xi_{\star}$ is that the *spectral radius* of $T$ is strictly less than $1$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Quadratic problems", "weight": 1.0} -->

Recall that the spectral radius of a matrix $M$ is defined as the largest magnitude of the eigenvalues of $M$. We denote the spectral radius by $\rho{(M)}$. It is a fact that where $\parallel \cdot \parallel$ is the induced $2$-norm. Therefore, for any $\varepsilon > 0$, we have for all $k$ sufficiently large that ${\rho{(T)}^{k}} \leq {\| T^{k}\|} \leq {({{\rho{(T)}} + \varepsilon})}^{k}$. Hence, we can bound the convergence rate: So the spectral radius also determines the rate of convergence of the algorithm. With only bounds on the eigenvalues of $Q$, we can provide conditions under which the algorithms above converge for quadratic $f$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Proving convergence using integral quadratic constraints", "weight": 1.0} -->

When the function being minimized is quadratic as explored in Section 2.2, its gradient is affine and the interconnected dynamical system is a simple linear difference equation whose stability and convergence rate is analyzed solely in terms of eigenvalues of the closed-loop system. When the cost function is not quadratic, the gradient update is not an affine function and hence a different analysis technique is required.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Proving convergence using integral quadratic constraints", "weight": 1.0} -->

A popular technique in the control theory literature is to use *integral quadratic constraints* (IQCs) to capture features of the behavior of partially-known components. The term IQC was introduced in the seminal paper by Megretski and Rantzer. In that work, the authors analyzed continuous time dynamical systems and the constraints involved integrals of quadratic functions, hence the name IQC.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Proving convergence using integral quadratic constraints", "weight": 1.0} -->

In the development that follows, we repurpose the classical IQC theory for use in algorithm analysis. This requires using discrete time dynamical systems so our constraints will involve sums of quadratics rather than integrals. We also adapt the theory in a way that allows us to certify a specific convergence rate in addition to stability.

<!-- chunk {"id": "body-0026", "role": "body", "section": "An introduction to IQCs", "weight": 1.0} -->

IQCs provide a convenient framework for analyzing interconnected dynamical systems that contain components that are noisy, uncertain, or otherwise difficult to model. The idea is to replace this troublesome component by a quadratic constraint on its inputs and outputs that is known to be satisfied by all possible instances of the component. If we can certify that the newly constrained system performs as desired, then the original system must do so as well.

<!-- chunk {"id": "body-0027", "role": "body", "section": "An introduction to IQCs", "weight": 1.0} -->

Suppose $\phi:{\ell_{2e}\rightarrow\ell_{2e}}$ is the troublesome function we wish to analyze. The equation $u = {\phi{(y)}}$ can be represented using a block diagram, as in Figure 1.

<!-- chunk {"id": "body-0028", "role": "body", "section": "An introduction to IQCs", "weight": 1.0} -->

Although we do not know $\phi$ exactly, we assume that we have some knowledge of the constraints it imposes on the pair $(y,u)$. For example, suppose it is known that $\phi$ satisfies the following properties: $\phi$ is static and memoryless: ${\phi{(y_{0},y_{1},\ldots)}} = {({g{(y_{0})}},{g{(y_{1})}},\ldots)}$ for some $g:{{\mathbb{R}}^{d}\rightarrow{\mathbb{R}}^{d}}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Core idea behind IQC", "weight": 1.0} -->

Instead of analyzing a system that contains $\phi$, we analyze the system where $\phi$ is removed, but we enforce the constraints (3.1) on the signals $(y,u)$. Since (3.1) is true for all admissible choices of $\phi$, then any properties we can prove for the constrained system must hold for the original system as well.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Core idea behind IQC", "weight": 1.0} -->

Note that (3.1) is rather special in that the quadratic coupling of $(y,u)$ is pointwise; it only manifests itself as separate quadratic constraints on each $(y_{k},u_{k})$. It is possible to specify more general quadratic constraints that couple different $k$ values, and the key insight above still holds. To do this, introduce auxiliary sequences ${\zeta,z} \in \ell_{2e}$ together with a map $\Psi$ characterized by the matrices $(A_{\Psi},B_{\Psi}^{y},B_{\Psi}^{u},C_{\Psi},D_{\Psi}^{y},D_{\Psi}^{u})$ and the recursion where we will define the initial condition $\zeta_{\star}$ shortly. The equations (3.2) define an affine map $z = {\Psi{(y,u)}}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Core idea behind IQC", "weight": 1.0} -->

Assuming a reference point $(y_{\star},u_{\star})$ as before, we can define the associated reference $(\zeta_{\star},z_{\star})$ that is a fixed point of (3.2). In other words, We will require that ${\rho{(A_{\Psi})}} < 1$, which ensures that (3.3) has a unique solution $(\zeta_{\star},z_{\star})$ for any choice of $(y_{\star},u_{\star})$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Core idea behind IQC", "weight": 1.0} -->

We then consider the quadratic forms ${({z_{k} - z_{\star}})}^{\mathsf{T}}M{({z_{k} - z_{\star}})}$ for a given symmetric matrix $M$ (typically indefinite). Note that each such quadratic form is a function of $(y_{0},\ldots,y_{k},u_{0},\ldots,u_{k})$ that is determined by our choice of $(\Psi,M,y_{\star},u_{\star})$. In our previous example (3.1), $\Psi$ has no dynamics and the corresponding $\Psi$ and $M$ are In other words, if we use the definitions (3.4), then ${{({z_{k} - z_{\star}})}^{\mathsf{T}}M{({z_{k} - z_{\star}})}} \geq 0$ is the same as (3.1).

<!-- chunk {"id": "body-0033", "role": "body", "section": "Core idea behind IQC", "weight": 1.0} -->

In general, these sorts of quadratic constraints are called IQCs. We consider four different types of IQCs, which we now define.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Stability and performance results", "weight": 1.0} -->

In this section, we show how IQCs can be used to prove that iterative algorithms converge and to bound the rate of convergence. In both cases, the certification requires solving a tractable convex program. We note that the original work on IQCs only proved stability (boundedness). Some other works have addressed exponential stability, but the emphasis of these works is on proving the *existence* of an exponential decay rate, and so the rates constructed are very conservative. We require rates that are less conservative, and this is reflected in the inclusion of $\rho$ in the LMI of our main result, Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints").

<!-- chunk {"id": "body-0035", "role": "body", "section": "Stability and performance results", "weight": 1.0} -->

We will now combine the dynamical system framework of Section 2 and the IQC theory of Section 3.1. Suppose $G:{\ell_{2e}^{d}\rightarrow\ell_{2e}^{d}}$ is an affine map $u\mapsto y$ described by the recursion where $(A,B,C)$ are matrices of appropriate dimensions. The map is affine rather than linear because of the initial condition $\xi_{0}$. As in Section 2, $G$ is the iterative algorithm we wish to analyze, and using the general formalism of Section 3.1, $\phi$ is the nonlinear map ${(y_{0},y_{1},\ldots)}\mapsto{(u_{0},u_{1},\ldots)}$ that characterizes the feedback. Of course, this framework subsumes the special case of interest in which $u_{k} = {{\nabla f}{(y_{k})}}$ for each $k$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Stability and performance results", "weight": 1.0} -->

We assume that $\phi$ satisfies an IQC, and this IQC is characterized by a map $\Psi$ and matrix $M$. We can interpret $z = {\Psi{(y,u)}}$ as a filtered version of the signals $u$ and $y$. These equations can be represented using a block-diagram as in Figure 2(a).

<!-- chunk {"id": "body-0037", "role": "body", "section": "Stability and performance results", "weight": 1.0} -->

(a) The auxiliary system Ψ produces z, which is a filtered version of the signals y and u.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Stability and performance results", "weight": 1.0} -->

(b) The nonlinearity ϕ is replaced by a constraint on z, so we may remove ϕ entirely.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Stability and performance results", "weight": 1.0} -->

Consider the dynamics of $G$ and $\Psi$ from (3.5) and (3.2), respectively. Upon eliminating $y$, the recursions may be combined to obtain More succinctly, (3.6) can be written as The dynamical system (3.7) is represented in Figure 2(b) by the dashed box. Our main result is as follows.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Pointwise and hard IQCs", "weight": 1.0} -->

Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints") can easily be adapted to other types of IQCs.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Pointwise and hard IQCs", "weight": 1.0} -->

If the pointwise IQC defined by some $(\Psi,M,y_{\star},u_{\star})$ is satisfied, then so is the $\rho$-hard IQC defined by $(\Psi,M,\rho,y_{\star},u_{\star})$ for any $\rho$. Therefore, we may apply Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints") directly and ignore the $\rho$-hardness constraint. The smallest $\rho$ that makes (3.9 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")) feasible will correspond to the best exponential rate we can guarantee.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Pointwise and hard IQCs", "weight": 1.0} -->

Hard IQCs are a special case of $\rho$-hard IQCs with $\rho = 1$. Therefore, if the LMI (3.9 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")) is feasible, Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints") guarantees that ${\|{\xi_{k} - \xi_{\star}}\|} \leq {\sqrt{{cond}{(P)}}{\|{\xi_{0} - \xi_{\star}}\|}}$. In other words, the iterates are bounded (but not necessarily convergent).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Pointwise and hard IQCs", "weight": 1.0} -->

If a $\rho_{1}$-hard IQC is satisfied, then so is the $\rho$-hard IQC for any $\rho \geq \rho_{1}$. Also, if (3.9 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")) is feasible for some $\rho_{2}$, it will also be feasible for any $\rho \geq \rho_{2}$. Therefore, if we use a $\rho_{1}$-hard IQC and (3.9 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")) is feasible for $\rho_{2}$, then the smallest exponential rate we can guarantee is $\rho = {\max{(\rho_{1},\rho_{2})}}$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Multiple IQCs", "weight": 1.0} -->

Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints") can also be generalized to the case where $\phi$ satisfies multiple IQCs. Suppose $\phi$ satisfies the $\rho$-hard IQCs defined by $(\Psi_{i},M_{i},\rho,y_{\star}^{(i)},u_{\star}^{(i)})$ for $i = {1,\ldots,r}$. Simply redefine the matrices $(\hat{A},\hat{B},\hat{C},\hat{D})$ in a manner analogous to (3.7), but where the output is now $(z_{k}^{},\ldots,z_{k}^{(r)})$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Multiple IQCs", "weight": 1.0} -->

Instead of (3.9 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")), use where ${\lambda_{1},\ldots,\lambda_{r}} \geq 0$. Thus, when (3.11) is multiplied out as in (3.10), we now obtain and the rest of the proof proceeds as in Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints").

<!-- chunk {"id": "body-0046", "role": "body", "section": "Remark on Lyapunov functions", "weight": 1.0} -->

In the quadratic case treated in Section 2.2, a quadratic Lyapunov function is constructed from the solution $P$ in (2.12). In the case of IQCs, such a quadratic function cannot serve as a Lyapunov function because it does not strictly decrease over all trajectories. Nevertheless, Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints") shows how $\rho$-hard IQCs can be used to certify a convergence rate and no Lyapunov function is explicitly constructed. We can explain this difference more explicitly. If $V{(x)}$ is a Lyapunov function, then by definition it satisfies the properties; ${\lambda_{1}{\|{x - x_{\star}}\|}^{2}} \leq {V{(x)}} \leq {\lambda_{2}{\|{x - x_{\star}}\|}^{2}}$ for all $x$ and $k$.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Remark on Lyapunov functions", "weight": 1.0} -->

Property (ii) implies that which, combined with Property (i) implies that ${\|{x_{k} - x_{\star}}\|} \leq {\sqrt{\lambda_{2}/\lambda_{1}}\rho^{k}{\|{x_{0} - x_{\star}}\|}}$. In Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints"), we use ${V{(x)}} = {{({x - x_{\star}})}^{\mathsf{T}}P{({x - x_{\star}})}}$, which satisfies (i) but not (ii). So $V{(x)}$ is *not* a Lyapunov function in the technical sense. Nevertheless, we prove directly that (3.12) holds, and so the desired result still holds.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Remark on Lyapunov functions", "weight": 1.0} -->

That is, $V{(x)}$ serves the same purpose as a Lyapunov function.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IQCs for convex functions", "weight": 1.0} -->

We will derive three IQCs that are useful for describing gradients of strongly convex functions: the *sector* (pointwise) IQC, the *off-by-one* (hard) IQC, and *weighted off-by-one* ($\rho$-hard) IQC. In general, gradients of strongly convex functions satisfy an infinite family of IQCs, originally characterized by Zames and Falb for the single-input-single-output case. A generalization of the Zames-Falb IQCs to multidimensional functions is derived. Both the sector and off-by-one IQCs are special cases of Zames-Falb, while the weighted off-by-one IQC is a convex combination of the sector and off-by-one IQCs. While the Zames-Falb family is infinite, the three simple IQCs mentioned above are the only ones used in this paper. IQCs can be used to describe many other types of functions as well, and further examples are available. We begin with some fundamental inequalities that describe strongly convex function.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Remark 7", "weight": 1.0} -->

In Lemma 6. ‣ 3.3 IQCs for convex functions ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints"), we use a slight abuse of notation in representing the map $\Psi:{{\ell_{2e}^{d} \times \ell_{2e}^{d}}\rightarrow\ell_{2e}^{m}}$. In writing $\Psi$ as a matrix in ${\mathbb{R}}^{{{2d} \times 2}d}$, we mean that $\Psi$ is a static map that operates pointwise on $(y,u)$. In other words,

<!-- chunk {"id": "body-0051", "role": "body", "section": "Remark 11", "weight": 1.0} -->

In implementing the weighted off-by-one IQC, one can simply set $\overline{\rho} = \rho$. However, a less conservative approach is to keep $\overline{\rho}$ as an additional degree of freedom. In Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints"), the IQC constraint is included in (3.9 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")) in the final term and is multiplied by the constant $\lambda \geq 0$. When using the weighted off-by-one IQC, this amounts to: By defining $\lambda_{1} = {\lambda{({1 - {\overline{\rho}}^{2}})}}$ and $\lambda_{2} = {\lambda{\overline{\rho}}^{2}}$, an equivalent expression is

<!-- chunk {"id": "body-0052", "role": "body", "section": "Historical context of IQCs and Lyapunov theory", "weight": 1.0} -->

Constructing Lyapunov functions has a long history in control and dynamical systems, and the central focus of this paper is borrowing tools from this literature to see how we can generalize our analysis from quadratic functions to more general, nonlinear convex functions.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Historical context of IQCs and Lyapunov theory", "weight": 1.0} -->

One of the most fundamental problems in control theory is certifying the stability of nonlinear systems. In interconnected systems such as electric circuits or chemical plants, individual components are typically modeled using differential (or difference) equations. Interconnected systems often contain nonlinearities or components that are otherwise difficult to model. The earliest results on such systems date back to the work of Lur'e and Postnikov. The goal was to prove stability under a wide range of admissible uncertainties. This notion of robust stability was called *absolute stability*. Indeed, Lur'e studied precisely the model we are concerned: a known linear system interconnected in feedback to an uncertain nonlinear system.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Historical context of IQCs and Lyapunov theory", "weight": 1.0} -->

In the 1960's and 70's, several sufficient conditions for absolute stability were expressed as frequency-domain conditions. In other words, the main objects of interest are ratios of the Laplace transforms of the outputs to the inputs, also known as *transfer functions*. Examples include the Popov criterion, the small-gain theorem, the circle criterion, and passivity theory. Frequency-domain conditions were popular at the time because they could be verified graphically. The work of Willems unified many of the existing results by casting them in the time domain in a framework called *dissipativity theory*. This notion is on one hand a generalization of Lyapunov functions to include systems with exogenous inputs, and on the other hand a generalization of passivity theory and the small-gain theorem. These ideas form the core of modern nonlinear control theory, and are covered in many textbooks such as Khalil.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Historical context of IQCs and Lyapunov theory", "weight": 1.0} -->

With the advent of computers, graphical methods were no longer required. The connection between frequency-domain conditions and Linear Matrix Inequalities (LMIs) was made by Kalman and Yakubovich and culminated in the Kalman-Yakubovich-Popov (KYP) lemma, also known as the Positive-Real lemma. This paved the way for the use of modern computational tools such as semidefinite programming. Another important development is the concept of the *structured singular value*, also known as $\mu$-analysis. While previous theory had been used to describe *static* nonlinearities or uncertainties, $\mu$-analysis is a computationally tractable framework for describing a system containing multiple *dynamic* uncertainties. A survey of $\mu$-related techniques and results is given. For a comprehensive overview of the history and development of LMIs in control theory, we refer the reader to.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Historical context of IQCs and Lyapunov theory", "weight": 1.0} -->

Integral Quadratic Constraints (IQCs) were first introduced by Yakubovich, who considered the notion of imposing quadratic constraints on an infinite-horizon control problem, and combining multiple constraints via the S-procedure. The definitive work on IQCs is Megretski and Rantzer. In this seminal paper, the authors showed that dissipativity theory, as well as all the frequency-domain conditions, could be formulated as IQCs. Furthermore, the KYP lemma in conjunction with the S-procedure allows stability to be verified by solving an LMI.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Historical context of IQCs and Lyapunov theory", "weight": 1.0} -->

The seminal paper on IQCs develops the theory primarily in the frequency domain, but also alludes to time-domain versions of the results by introducing *hard* IQCs. This notion of hard IQCs is pursued, where the main IQC stability theorem is rederived entirely in the time domain. In the time domain, these constraints parallel the development of Nesterov, where we are able to construct inequalities linking multiple inputs and outputs of uncertain functions. This allows us to provide a wholly self-contained development of the theory. Moreover, we are able to enhance the techniques of, providing new IQCs and considerably sharper rates of convergence than those discussed in the earlier work. In this sense, our work provides useful methods for control theorists interested in estimating rates of stabilization of their control systems.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Case studies", "weight": 1.0} -->

We now use the results of Section 3 to rederive some existing results from the literature on iterative large-scale algorithms. The IQC approach gives a unified method to analyze many different algorithms. In addition to verifying existing results, we also present a negative result that was not previously known.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Computational approach", "weight": 1.0} -->

Given an iterative algorithm, our first step is to express it as a feedback interconnection of a discrete linear time-invariant dynamical system with a nonlinearity representing $\nabla f$. This procedure is explained in Section 2 and yields matrices $(A,B,C)$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Computational approach", "weight": 1.0} -->

The next step is to decide which IQCs will be used to characterize the nonlinearity. A simple but conservative choice is the sector IQC defined in Lemma 6. ‣ 3.3 IQCs for convex functions ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints"). A less conservative choice is the weighted off-by-one IQC of Lemma 10. ‣ 3.3 IQCs for convex functions ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints"). For the chosen $(\Psi,M)$, we find the smallest $\rho$ such that the semidefinite program (SDP) (3.9 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")) of Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints") is feasible. In the case of the sector IQC, the SDP has variables $(P,\lambda,\rho)$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Computational approach", "weight": 1.0} -->

For the weighted off-by-one IQC, the SDP has variables $(P,\lambda_{1},\lambda_{2},\rho)$ as explained in Remark 11. The resulting $\rho$ is an upper bound for the worst-case convergence rate of the algorithm. Specifically, To solve the SDP (3.9 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")) numerically, observe that it is a quasiconvex program. In particular, for every fixed $\rho$, (3.9 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")) is an LMI. The simplest way to solve (3.9 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")) is to use a bisection search on $\rho$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Computational approach", "weight": 1.0} -->

For a fixed $\rho$, the SDP (3.9 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")) or (3.11) become an LMI and can be efficiently solved using interior-point methods. Popular implementations include SDPT3, SeDuMi, and Mosek. This approach was used for all the simulations presented herein.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Computational approach", "weight": 1.0} -->

More sophisticated methods exist to solve (3.9 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")) as well. A quasiconvex program of the type (3.9 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")) is known as a *generalized eigenvalue optimization problem* (GEVP). The GEVP is well-studied and modified interior-point methods such as the *method of centers* and the *long-step method of analytic centers* can be used to solve it.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Lossless dimensionality reduction", "weight": 1.0} -->

The size of the SDP in (3.9 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")) is proportional to $d$, the size of the state $\xi_{k}$ in the optimization algorithm. This can be problematic in cases where $d$ is large because it can be computationally costly to solve large SDPs. In many cases of interest, however, the algorithms we wish to analyze have a block-diagonal structure. For example, Nesterov's accelerated method has the form (2.5), which is Each of the matrices $(A,B,C)$ is a block matrix with repeated diagonal blocks. Using Kronecker product notation (see Section 1.1, this means for example that and similarly for $B$ and $C$. Moreover, the IQCs we use to describe $\nabla f$ have the same sort of structure.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Lossless dimensionality reduction", "weight": 1.0} -->

That is, $(A_{\Psi},B_{\Psi}^{y},B_{\Psi}^{u},C_{\Psi},D_{\Psi}^{y},D_{\Psi}^{u})$ are block matrices with repeated diagonal blocks. Now consider the SDP (3.9 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")) from Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints").

<!-- chunk {"id": "body-0066", "role": "body", "section": "Lossless dimensionality reduction", "weight": 1.0} -->

Based on the discussion above, each of the matrices $(\hat{A},\hat{B},\hat{C},\hat{D},M)$ have the form e.g. $A_{0} \otimes I_{d}$. Rather than looking for a general $P \in {\mathbb{R}}^{{{nd} \times n}d}$ with $P \succ 0_{nd}$, if we restrict our search to $P = {P_{0} \otimes I_{d}}$ with $P_{0} \in {\mathbb{R}}^{n \times n}$ and $P_{0} \succ 0_{n}$, then the SDP reduces to The resulting SDP no longer depends on $d$ and is effectively the same as if we had solved the original problem with $d = 1$. As it turns out, there is no loss of generality in assuming a $P$ of this form.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Lossless dimensionality reduction", "weight": 1.0} -->

Multiplying the left-hand side of (4.2) by ${({I_{n} \otimes e_{1}})}^{\mathsf{T}}$ on the left and $({I_{n} \otimes e_{1}})$ on the right, we conclude that $P_{0}$ satisfies (4.3). Thus, $\hat{P} = {P_{0} \otimes I_{d}}$ is also a solution to (4.2). In other words, (4.2) is feasible if and only if (4.3) is feasible.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Known bounds for first-order optimization algorithms", "weight": 1.0} -->

The following proposition summarizes some of the known bounds for optimizing strongly convex functions.

<!-- chunk {"id": "body-0069", "role": "body", "section": "The Gradient method", "weight": 1.0} -->

The Gradient method with constant stepsize is among the simplest optimization schemes. The recursion is given by We will analyze this algorithm by applying Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints"). Since $f \in {S{(m,L)}}$, we may use the sector IQC of Lemma 6. ‣ 3.3 IQCs for convex functions ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints") and (3.9 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")) together with the dimensionality reduction of Section 4.2 yields the following SDP.

<!-- chunk {"id": "body-0070", "role": "body", "section": "The Gradient method", "weight": 1.0} -->

Note that $P$ is $1 \times 1$, so we may set $P = 1$ without loss of generality and we obtain the following LMI in $(\rho^{2},\lambda)$.

<!-- chunk {"id": "body-0071", "role": "body", "section": "The Gradient method", "weight": 1.0} -->

Using Schur complements, (4.6) is equivalent to By analyzing the lower bound on $\rho$ in (4.7), we can find the optimal choice of $\lambda$ as a function of the stepsize $\alpha$. Omitting the details, we eventually obtain the simple expression $\rho = {\max\left\{ {|{1 - {\alpham}}|},{|{1 - {\alphaL}}|} \right\}}$. This is precisely the bound found for the quadratic case, as derived in Appendix A. However, we have shown something much stronger here, since the only assumption we made about $f$ is that $\nabla f$ satisfies the sector IQC of Lemma 6. ‣ 3.3 IQCs for convex functions ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints").

<!-- chunk {"id": "body-0072", "role": "body", "section": "The Gradient method", "weight": 1.0} -->

In particular, the Gradient method rates in Proposition 1 hold not only for quadratics, but also for strongly convex functions, and even for functions that change or switch over time (either stochastically, adversarially, or otherwise), so long as each function satisfies the pointwise sector constraint. Note that (4.6) can be transformed using Schur complements: And now (4.8) is linear in $(\rho^{2},\lambda,\alpha)$. This formulation allows one to directly answer questions such as "what range of stepsizes can yield a given rate?".

<!-- chunk {"id": "body-0073", "role": "body", "section": "Nesterov's accelerated method", "weight": 1.0} -->

Nesterov's accelerated method with constant stepsize converges at a linear rate. There exists some $c > 0$ such that for any initial condition $\xi_{0}$, when applied to functions $f \in {S{(m,L)}}$. In this case, the parameters are the standard parameters from Proposition 12, which are $\alpha{: =}{1/L}$ and $\beta{: =}{{({\sqrt{L} - \sqrt{m}})}/{({\sqrt{L} + \sqrt{m}})}}$. Nesterov also showed that a *lower bound* on convergence rate for *any* algorithm of the form (2.2) and for any $f \in {S{(m,L)}}$ is given by Since $\rho$ and $\rho_{\text{opt}}$ behave similarly as ${L/m}\rightarrow\infty$, Nesterov's accelerated method is sometimes called "optimal" or "nearly optimal".

<!-- chunk {"id": "body-0074", "role": "body", "section": "Nesterov's accelerated method", "weight": 1.0} -->

We computed the rate bounds using Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints") using either the sector IQC of Lemma 6. ‣ 3.3 IQCs for convex functions ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints"), or a combination of the sector IQC and the weighted off-by-one IQC of Lemma 10. ‣ 3.3 IQCs for convex functions ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints"). It is important to note that unlike the Gradient method case, the LMI (3.9 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")) is no longer linear in $\rho^{2}$. Therefore, we found the minimal $\rho$ by performing a bisection search on $\rho$, see the first plot in Figure 3.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Nesterov's accelerated method", "weight": 1.0} -->

The rate obtained using the sector IQC alone is very poor. To understand why, recall from Lemma 6. ‣ 3.3 IQCs for convex functions ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints") that the sector IQC allows for $f_{k}$ to be different at each iteration. Unlike the Gradient method, Nesterov's accelerated method is not robust to having a changing $f_{k}$. However, convergence can nevertheless be guaranteed as long as $\rho < 1$, which corresponds approximately to ${L/m} < 11.7$.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Nesterov's accelerated method", "weight": 1.0} -->

The rate obtained using the weighted off-by-one IQC improves upon the rate proven in using the estimate sequence approach (see Proposition 12). Note that we do not have an analytical expression for the improved bound; it was found numerically by solving the LMI of Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints").

<!-- chunk {"id": "body-0077", "role": "body", "section": "Nesterov's accelerated method", "weight": 1.0} -->

As we can see from Figure 3, Nesterov's method applied to quadratics is within a factor of $2$ of the theoretical lower bound, and the bound we can prove for Nesterov's method applied to strongly convex functions is within a factor of $1.4$ of the bound for quadratics.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Nesterov's accelerated method", "weight": 1.0} -->

Finally, we must also ensure that $P$ is reasonably well-conditioned. In Figure 4, we see that ${cond}{(P)}$ appears to be proportional to $L/m$, which agrees with the scale factor found by Nesterov.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Nesterov's accelerated method", "weight": 1.0} -->

If we repeat the above experiments, but instead using the optimal tuning of Nesterov's method given in Proposition 1, the resulting plots are virtually identical. The only differences are that the curves are shifted down slightly because the optimal rate for quadratics is now $1 - \frac{2}{\sqrt{{3\kappa} + 1}}$ instead of $1 - \frac{1}{\sqrt{\kappa}}$. The sector-IQC curve goes unstable a little sooner as well, at around ${L/m} \approx 10$. Roughly speaking, if we use the optimal tuning we can guarantee slightly faster convergence but slightly less robustness.

<!-- chunk {"id": "body-0080", "role": "body", "section": "The Heavy-ball method", "weight": 1.0} -->

The optimal Heavy-ball rate for quadratics in Proposition 1 matches Nesterov's lower bound (4.9) for strongly convex functions. Although the Heavy-ball method and Nesterov's accelerated method have similar recursions, Figures 3 and 5 tell very different stories. When we allow for a different $f_{k}$ at every iteration (sector IQC), we can guarantee stability when ${L/m} \approx 6$ or less. When we include the weighted off-by-one IQC as well, we can only guarantee stability when ${L/m} \approx 18$ or less. While it seems possible that using more IQCs could potentially improve this upper bound, it turns out that the poor quality of these bounds is due to something more serious: the Heavy-ball method optimized for quadratics does not converge for general $f \in {S{(m,L)}}$.

<!-- chunk {"id": "body-0081", "role": "body", "section": "The Heavy-ball method", "weight": 1.0} -->

To find an example of an $f{(x)}$ that leads to a non-convergent Heavy-ball method, Figure 5 indicates that we should search for ${L/m} > 18$. The following one-dimensional example does the job.

<!-- chunk {"id": "body-0082", "role": "body", "section": "The Heavy-ball method", "weight": 1.0} -->

It is easy to check that ${\nabla f}{(x)}$ is continuous and monotone, and so $f \in {S{(m,L)}}$ with $m = 1$ and $L = 25$. When using an initial condition in the interval $3.07 \leq x_{0} \leq 3.46$, the Heavy-ball method produces a limit cycle with oscillations that never damp out. The first 50 iterates for $x_{0} = 3.3$ are shown in Figure 6, and a plot of $f{(x)}$ with the limit cycle overlaid is shown in Figure 7.

<!-- chunk {"id": "body-0083", "role": "body", "section": "The Heavy-ball method", "weight": 1.0} -->

For a detailed proof that $f$ can indeed converge to a limit cycle, see Appendix B. We further investigate the stability of the Heavy-ball method in Section 5.

<!-- chunk {"id": "body-0084", "role": "body", "section": "Stability of the Heavy-ball method", "weight": 1.0} -->

We saw in Section 4.6 that the Heavy-ball method that uses $\alpha$ and $\beta$ optimized for quadratic functions is unstable for general strongly convex functions. A natural question to ask is whether the Heavy-ball method is stable over the class $S{(m,L)}$ for *some* choice of $\alpha$ and $\beta$. This experiment is easy to carry out in our framework, because choosing new values of $\alpha$ and $\beta$ simply amounts to changing parameters in the LMI. We chose $\alpha = \frac{1}{L}$, and for a sampling of points in $\beta \in {\lbrack 0,1\rbrack}$, we evaluated the corresponding Heavy-ball method using Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints") together with the weighted off-by-one IQC. See Figure 8.

<!-- chunk {"id": "body-0085", "role": "body", "section": "Stability of the Heavy-ball method", "weight": 1.0} -->

The first plot shows convergence rate. When $\beta = 0$, the Heavy-ball method becomes the Gradient method, which is always convergent. However, we can improve upon the gradient rate by optimizing over $\beta$. The best achievable rate is given by the black curve. The black curve lies strictly above the optimal Heavy-ball rate for quadratics, but below the optimal gradient rate.

<!-- chunk {"id": "body-0086", "role": "body", "section": "Stability of the Heavy-ball method", "weight": 1.0} -->

In the second plot, we show the iterations required to achieve convergence. Again, the black curve represents the optimal parameter choice. As $L/m$ gets large, the envelope veers away from the optimal Heavy-ball curve and becomes parallel to the optimal gradient curve. So when $L/m$ is large, even when $\beta$ is chosen optimally, the Heavy-ball method is comparable to the Gradient method in worst-case for general strongly convex functions.

<!-- chunk {"id": "body-0087", "role": "body", "section": "Multiplicative gradient noise", "weight": 1.0} -->

A common consideration is the inclusion of noise in the gradient computation. One possible model is *relative deterministic noise* where we assume the gradient error is proportional to the distance to optimality. Instead of directly observing ${\nabla f}{(y)}$, we see ${u_{k} = {{{\nabla f}{(y_{k})}} + r_{k}}},$ where for some small nonnegative $\delta$. The IQC framework can be used to analyze such situations to study the robustness of various algorithms to this type of noise.

<!-- chunk {"id": "body-0088", "role": "body", "section": "Multiplicative gradient noise", "weight": 1.0} -->

If $w_{k}$ is the true gradient, we actually measure $u_{k} = {\Delta_{k}w_{k}}$, where the gradient error is bounded above by a quantity proportional to the true gradient. In other words, we assume there is some $\delta > 0$ such that ${\|{u_{k} - w_{k}}\|} \leq {\delta{\| w_{k}\|}}$. Squaring both sides of the inequality and rearranging, we obtain the IQC Note that this is simply the sector IQC with $m = {1 - \delta}$ and $L = {1 + \delta}$. We make no assumptions on how the noise is generated; it may be the output of a stochastic process, or could even be chosen adversarially. The modified block-diagram is shown in Figure 9.

<!-- chunk {"id": "body-0089", "role": "body", "section": "Multiplicative gradient noise", "weight": 1.0} -->

By making a small modification, we can apply Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints"). We will look to show that the following inequality holds over all trajectories for some ${\lambda_{1},\lambda_{2}} \geq 0$. In order to formulate an LMI that implies a solution to (5.1), we use the signal $\begin{bmatrix} x_{k}^{\mathsf{T}} & u_{k}^{\mathsf{T}} & w_{k}^{\mathsf{T}} \end{bmatrix}$. Consequently, the matrices $(\hat{A},\hat{B},\hat{C},\hat{D})$ from (3.6)--(3.7) now become a map ${(w_{k},u_{k})}\mapsto z_{k}$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "Multiplicative gradient noise", "weight": 1.0} -->

This leads to an LMI of the form (3.11) which is now block-$3 \times 3$ instead of the $2 \times 2$ LMI of Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints"). The proof is identical to that of Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints").

<!-- chunk {"id": "body-0091", "role": "body", "section": "Gradient method", "weight": 1.0} -->

Our first experiment is to test the Gradient method. We used noise values of $\delta \in {\{ 0.01,0.02,0.05,0.1,0.2,0.5\}}$. See Figure 10.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Gradient method", "weight": 1.0} -->

In examining Figure 10, we observe that the Gradient method with stepsize $\frac{2}{L + m}$ is not very robust to multiplicative noise. Even with noise as low as 1% ($\delta = 0.01$), the Gradient method is no longer stable for ${L/m} > 100$. An explanation for this phenomenon is that in choosing the stepsize $\alpha$, we are trading off convergence rate with robustness. The choice $\frac{2}{L + m}$ yields the minimum worst-case rate, but is fragile to noise. If we pick a more conservative stepsize such as the popular choice $\alpha = \frac{1}{L}$, we obtain a very different picture. See Figure 11.

<!-- chunk {"id": "body-0093", "role": "body", "section": "Gradient method", "weight": 1.0} -->

Notice that with the updated stepsize of $\alpha = \frac{1}{L}$, the Gradient method is now robust to multiplicative noise. Robustness comes at the expense of a degradation in the best achievable convergence rate. This degradation manifests itself as a gap in Figure 11 between the black curves and the other ones.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Nesterov's accelerated method", "weight": 1.0} -->

We can carry out an experiment similar to the one we did with the Gradient method, but now with Nesterov's method. As before, we examine the trade-off between the magnitude of the multiplicative noise and the degradation of the optimal convergence rate. This time, we use $\delta \in {\{ 0.05,0.1,0.2,0.3,0.4,0.5\}}$. See Figure 12.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Nesterov's accelerated method", "weight": 1.0} -->

As with our first Gradient method test, Nesterov's method is not robust to multiplicative noise. For moderate $L/m$, the degradation is minor, but eventually leads to instability when we reach a certain threshold. The idea that accelerated methods are sensitive to noise and can lead to an accumulation of error was noted in the recent work, using a different notion of gradient perturbation.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Nesterov's accelerated method", "weight": 1.0} -->

Robustness of Nesterov's method can be improved by modifiying the $\alpha$ and $\beta$ parameters. Choosing a smaller $\alpha$ pushes back the instability threshold, while choosing a smaller $\beta$ simultaneously pushes back the instability threshold and degrades the rate. In the limit $\beta\rightarrow 0$, Nesterov's method becomes the Gradient method, so we recover the plots of Figure 11.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Proximal point methods", "weight": 1.0} -->

Suppose we are interested in solving a problem of the form where $f \in {S{(m,L)}}$, and $P$ is an extended-real-valued convex function on ${\mathbb{R}}^{n}$. An example of such a problem is constrained optimization, where we require that $x \in C$. In this case, we simply let $P$ be the indicator function of $C$. We will now show how the IQC framework can be used to analyze algorithms involving a *proximal* operator. Define the proximal operator of $P$ as As an illustrative example, we will show how to analyze the proximal version of Nesterov's algorithm. Iterations take the form: Note that when $\Pi_{\nu} = I$, we recover the standard Nesterov algorithm. When $\beta = 0$, we recover the proximal gradient method.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Proximal point methods", "weight": 1.0} -->

In order to analyze this algorithm, we must characterize $\Pi_{\nu}$ using IQCs. To this end, let $T{: =}{\partial P}$ be the subdifferential of $P$. Then, $\Pi_{\nu}{(x)}$ is the unique point such that ${x - {\Pi_{\nu}{(x)}}} \in {\nuT{({\Pi_{\nu}{(x)}})}}$. Or, written another way, Since $T$ is a subdifferential, it satisfies the *incremental passivity* condition. Namely, Therefore, $T$ satisfies the sector IQC with $m = 0$ and $L = \infty$. In fact, via minor modifications of Lemma 8. ‣ 3.3 IQCs for convex functions ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints") and Lemma 9.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Proximal point methods", "weight": 1.0} -->

‣ 3.3 IQCs for convex functions ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints") using the definition of a subdifferential rather than (3.13c. ‣ 3.3 IQCs for convex functions ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")), $T$ satisfies the off-by-one and weighted off-by-one IQCs as well. Now transform (5.2) by introducing the auxiliary signals $u_{k}{: =}{{\nabla f}{(y_{k})}}$, $w_{k}{: =}{\Pi_{\nu}{({y_{k} - {\alphau_{k}}})}}$, $v_{k}{: =}{\nuT{(w_{k})}}$.

<!-- chunk {"id": "body-0100", "role": "body", "section": "Proximal point methods", "weight": 1.0} -->

The definitions of $w_{k}$ and $v_{k}$ together with (5.3) immediately imply that $w_{k} = {y_{k} - {\alphau_{k}} - v_{k}}$. Therefore, we can rewrite (5.2) as These equations may be succinctly represented as a block diagram, as in Figure 13.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Proximal point methods", "weight": 1.0} -->

Analyzing this interconnection is done by accounting for the IQCs for both unknown blocks. If $(\Psi_{1},M_{1})$ is the IQC for $\nabla f$ with output $z_{k}^{1}$ and $(\Psi_{2},M_{2})$ is the IQC for $\nuT$ with output $z_{k}^{2}$, then we seek to show that for all trajectories satisfy where $x_{k}$ now includes the states $\xi_{k}$ as well as the internal states of $\Psi_{1}$ and $\Psi_{2}$.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Proximal point methods", "weight": 1.0} -->

As in the proof of Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints"), for each fixed $\rho$, we can write (5.4) as an LMI in the variables $P \succ 0$, $\lambda_{1} \geq 0$, $\lambda_{2} \geq 0$.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Proximal point methods", "weight": 1.0} -->

Applying this approach to the proximal version of Nesterov's accelerated method, we recover the exact same plots as in Figure 3. This is to be expected because it is known that the proximal gradient and accelerated methods achieves the same worst-case convergence rates as their unconstrained counterparts. We conjecture that any algorithm $G$ of the form (2.2) which converges with rate $\rho$ has a proximal variant that converges at precisely the same rate.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Weakly convex functions", "weight": 1.0} -->

With minor modifications to our analysis, we can immediately extend our results to the case where the function to be optimized is convex, but not strongly convex. Specifically, we will assume throughout this subsection that $f \in {S{(0,L)}}$. The following development is due to Elad Hazan.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Weakly convex functions", "weight": 1.0} -->

Suppose we want to minimize $f$ over a compact, convex domain $\mathcal{D}$ for which we can readily compute the Euclidean projection. Let $R$ denote the diameter of the set $\mathcal{D}$. Define the function ${f_{\varepsilon}{(x)}}{: =}{{f{(x)}} + {\frac{\varepsilon}{2R^{2}}{\| x\|}^{2}}}$. Note that $f_{\varepsilon}$ is differentiable and strongly convex; it satisfies $f_{\varepsilon} \in {S{(\frac{\varepsilon}{R^{2}},{L + \frac{\varepsilon}{R^{2}}})}}$. Therefore, we may apply our analysis to $f_{\varepsilon}$.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Weakly convex functions", "weight": 1.0} -->

Suppose we execute on $f_{\varepsilon}$ an algorithm with interleaved projections as in Section 5.3. Let $x_{\star}$ be any minimizer of $f$ on $\mathcal{D}$ and $x_{\star}^{(\varepsilon)}$ be the minimizer of $f_{\varepsilon}$. Let $\rho$ denote the rate of convergence achieved when the condition ratio is set as $\kappa = {({1 + {{LR^{2}}/\varepsilon}})}$ and let $P_{\varepsilon} \succ 0$ be the associated solution to the LMI. Let $\sigma{: =}{{cond}{(P_{\varepsilon})}}$. After $k$ steps, Now apply (3.13a. ‣ 3.3 IQCs for convex functions ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints")) from Proposition 5.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Weakly convex functions", "weight": 1.0} -->

‣ 3.3 IQCs for convex functions ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints") using ${(f,x,y)} = {(f_{\varepsilon},x_{\star}^{(\varepsilon)},x_{k})}$ and obtain Where the last inequality follows from the definition of set diameter. Therefore, if then ${{f{(x_{k})}} - {f{(x_{\star})}}} \leq \varepsilon$. Substituting the rates found algebraically for the quadratic case (Section 2.2) or our numerical results for the strongly convex case (Sections 4.4--4.5), the convergence rate $\rho$ satisfies Finally, note that $\sigma = {{cond}{(P_{\varepsilon})}}$ also depends on $\varepsilon$.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Weakly convex functions", "weight": 1.0} -->

We can control the growth of $\sigma$ directly by including a constraint of the form $I \preceq P \preceq {\sigmaI}$ when solving the SDP of Theorem 4 ‣ 3.2 Stability and performance results ‣ 3 Proving convergence using integral quadratic constraints ‣ Analysis and Design of Optimization Algorithms via Integral Quadratic Constraints"). Alternatively, we can observe (see Figure 4) that $\sigma \propto \kappa = {({1 + {{LR^{2}}/\varepsilon}})}$. Therefore, we conclude that This analysis matches the standard bounds up to the logarithmic terms.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Algorithm design", "weight": 1.0} -->

In this section, we show one way in which the IQC analysis framework can be used for algorithm design. We saw in Section 5.2 that the Gradient method can be very robust to noise (Figure 11), or not robust at all (Figure 10), depending on whether we use a stepsize of $\alpha = {1/L}$ or $\alpha = {2/{({L + m})}}$, respectively.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Algorithm design", "weight": 1.0} -->

A natural question to ask is whether such a trade-off between performance and robustness exists with Nesterov's method as well. As can be seen in Figure 12, Nesterov's method is only somewhat robust to noise. In the sequel, we will synthesize variants of Nesterov's method that explore the performance-robustness trade-off space.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Algorithm design", "weight": 1.0} -->

Consider an algorithm of the form (2.2). Based on the discussion in Section 2.1, we know $A$ must have an eigenvalue of $1$. Moreover, given any invertible $T$, the algorithms $(A,B,C,D)$ and $({TAT^{- 1}},{TB},{CT^{- 1}},D)$ are *equivalent realizations* in the sense that if one is stable with rate $\rho$, the other is stable with rate $\rho$ as well. Indeed, if the first algorithm has state $\xi_{k}$, the second algorithm has state $T\xi_{k}$. We limit our search to the case $A \in {\mathbb{R}}^{2 \times 2}$ and $D = 0$. Three parameters are required to characterize all possible algorithms in this family (modulo equivalences due to a choice of $T$).

<!-- chunk {"id": "body-0112", "role": "body", "section": "Algorithm design", "weight": 1.0} -->

One possible parameterization is given by In light of the discussion in Section 2, we see that the Gradient, Heavy-ball, and Nesterov methods are all special cases of (6.1). In particular, We may also rewrite (6.1) in more familiar recursion form as Our approach is straightforward: for each choice of condition ratio $L/m$ and noise strength $\delta$, we generate a large grid of tuples $(\alpha,\beta_{1},\beta_{2})$ and use the approach of Section 5.2 to evaluate each algorithm. We then choose the algorithm with the lowest $\rho$. In other words, given bounds on the condition ratio and noise strength, we choose the algorithm for which we can certify the best possible convergence rate over all admissible choices of $f$ and gradient noise. The performance of each optimized algorithm is plotted in Figure 14.

<!-- chunk {"id": "body-0113", "role": "body", "section": "Algorithm design", "weight": 1.0} -->

By design, this new family of algorithms must have a performance superior to the Gradient method, Nesterov's method, and the Heavy-ball method for any choice of tuning parameters. In the limit $\delta\rightarrow 0$, we appear to recover the performance of Nesterov's method when it is applied to *quadratics*. That is, we have used numerical search to find an algorithm whose worst case performance guarantee is slightly better than what is guaranteed by Nesterov's method.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Algorithm design", "weight": 1.0} -->

In the second plot of Figure 14, the algorithms robust to higher noise levels have greater slopes. When the noise level is low ($\delta = 0.01$), we approach a slope of 0.5, the same as Nesterov. When the noise level is high ($\delta = 0.5$), the slope is roughly 0.75. Note that the Gradient method, which was robust for *all* noise levels, has a slope of 1. Therefore, the new algorithms we found explore the trade-off between noise robustness and performance, and may be useful in instances where Nesterov's method would be too fragile and the Gradient method would be too slow.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Future work", "weight": 1.5} -->

We are only beginning to get a sense of what IQCs can tell us about optimization schemes, and there are many more control theory tools and techniques left to adapt to the context of optimization and machine learning. We conclude this paper with several interesting directions for future work.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Analytic proofs", "weight": 1.0} -->

One of the drawbacks of our numerical proofs is that we are always pushing up against numerical error and conditioning error. Analytic proofs would alleviate this issue and could provide more interpretable results about how parameters of algorithms should vary to meet performance and robustness demands. To provide such analytic proofs, one would have to solve small LMIs in closed form. This amounts to solving small semidefinite programming problems, and this may be doable using analytic tools from algebraic geometry.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Lower Bounds", "weight": 1.0} -->

Our IQC conditions are merely sufficient for verifying the convergence of an optimization problem. However, as pointed out by Megretski and Rantzer, the derived conditions are necessary in a restricted sense. If we fail to find a solution to our LMI, then there is necessarily a sequence of point that satisfy all of the IQC constraints and that do not converge to an equilibrium. It is thus possible that this tool can be used to construct a convex function to serve as a counterexample for convergence. This intuition was what guided our construction of a counterexample for the convergence of the Heavy-ball method. It may be possible that this construction can be generalized to systematically produce counterexamples.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Time-varying algorithms", "weight": 1.0} -->

In many practical scenarios, we know neither the Lipschitz constant $L$ nor the strong convexity parameter $m$. Under such conditions, some sort of estimation scheme is used to choose the appropriate step size. This could be a simple backoff scheme to ensure a sufficient decrease, or a more intricate search method to find the appropriate parameters. From our control vantage point, it may be possible to use techniques from adaptive control to certify when such line search methods are stable. In particular, these could be used to differentiate between the different sorts of schemes used to choose the parameters of the nonlinear conjugate gradient method. Useful connections are made between robustness analysis of adaptive controllers and Lyapunov theory.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Time-varying algorithms", "weight": 1.0} -->

A related area of study is that of linear parameter varying (LPV) systems. This extension of linear systems analysis considers parameterized variations in the dynamical system matrices $(A,B,C,D)$. Algorithms with variable stepsize are examples of LPV systems. Some recent work discussing IQCs applied to LPV systems appeared. Another possible direction would be to use optimal control techniques directly to choose algorithm parameters, possibly solving a small SDP at every iteration to choose new assignments.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Algorithm synthesis", "weight": 1.0} -->

Perhaps even more ambitiously than using our framework for parameter selection, our initial results show that we can use IQCs as a way of designing new algorithms. We restricted our attention to algorithms with one-step of memory, as then we only had to search over 3 parameters. However, new techniques would be necessary to explore more complicated algorithms. Local search heuristics could be used here to probe the feasible region of the associated LMIs, but convex methods and convex relaxations may also be applicable and should be investigated for these searches.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Noise analysis", "weight": 1.0} -->

Our robustness analysis only allows us to consider certain forms of deterministic noise. Expanding our techniques to study stochastic noise would expand the applicability of our techniques and could provide new insight into popular stochastic optimization algorithms such as stochastic coordinate descent and stochastic gradient descent. Many of the most common techniques for proving convergence of stochastic methods rely on Lyapunov-type arguments, and we may be able to generalize this approach to account for the variety of different methods. In order to expand our techniques to this space, we would need to introduce IQCs that were valid *in expectation*. Stability methods from stochastic control may be applicable to such investigations.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Beyond convexity", "weight": 1.0} -->

Since our analysis decouples the derivation of constraints on function classes from the algorithm analysis, it is possible that it can be generalized to nonconvex optimization. If we can characterize the function class by reasonable quadratic constraints, our framework immediately applies, and may lead to entirely new analyses for nonconvex function classes. For example, IQCs for saturating nonlinearities are readily available in the controls literature. From a complementary perspective, if we know that our function is not merely convex, but has additional structure, this can be incorporated as additional IQCs. With extra constraints, it is possible that we can derive faster rates or more robustness for smaller function classes.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Non-quadratic Lyapunov functions", "weight": 1.0} -->

There has been substantial work in the past decade on efficient algorithms to search over *non-quadratic* Lyapunov functions. These techniques use sum-of-squares hierarchies to certify that non-quadratic polynomials are nonnegative, and still reduce to solving small semidefinite programming problems. This more general class of Lyapunov functions could be better matched to certain classes of functions than quadratics, and we could perhaps analyze more complicated algorithms and interconnections.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Large-scale composite system analysis", "weight": 1.0} -->

Perhaps the most ambitious goal of this program is to move beyond convex models and attempt to analyze complicated optimization systems used in science and industry. Powerful modeling languages like AMPL or GAMS allow for local analysis of large, complex systems, and certifying that the decisions about these systems are valid and safe would have impact in a variety of fields including process technology, web-scale analytics, and power management. Since our methods nicely abstract beyond two interconnected systems, it is our hope that they can be extended to analyze the variety of optimization algorithms deployed to handle large, high throughput data processing.
