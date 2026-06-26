<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

acados: A Modular Open-source Framework for Fast Embedded Optimal Control

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents the acados software package, a collection of solvers for fast embedded optimization intended for fast embedded applications. Its interfaces to higher-level languages make it useful for quickly designing an optimization-based control algorithm by putting together different algorithmic components that can be readily connected and interchanged. Since the core of acados is written on top of a high-performance linear algebra library, we do not sacrifice computational performance. Thus, we aim to provide both flexibility and performance through modularity, without the need to rely on automatic code generation, which facilitates maintainability and extensibility. The main features of acados are: efficient optimal control algorithms targeting embedded devices implemented in C, linear algebra based on the high-performance BLASFEO library, user-friendly interfaces to Matlab and Python, and compatibility with the modeling language of CasADi. acados is free and open-source software released under the permissive BSD 2-Clause license.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Embedded optimization, according to the definition in [Ferreau2017], is solving optimization problems autonomously and with limited resources. The topic of this article is embedded optimal control, an important class of methods within embedded optimization. It focuses on calculating optimal decisions in order to control a dynamic system as the state changes. There exist many algorithms for embedded optimal control and quite a few were successfully applied to real-time and embedded applications such as robotic trajectory optimization[Schulman2014], autonomous driving[Liniger2015] and drones[Hehn2011]. For an overview on embedded optimization, we refer the reader to[Ferreau2017]. One of the most popular approaches in embedded optimal control nowadays is model predictive control (MPC) [Maciejowski2002,Rawlings2017,Gruene2017]. It is based on predicting the future behavior of a system and using this information to optimize for the action at the current time step. In linear MPC (also called linear-quadratic MPC (LQMPC)), the constraints, including the dynamic model, are affine and the objective is quadratic.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

With nonlinear MPC (NMPC), some or all of the constraints and objective are nonlinear functions In this paper, we focus on finite-dimensional problems, i.e., the objective is not a functional.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A related problem is that of moving horizon estimation(MHE) for estimating states and parameters online. We will present a unified notation of NMPC and MHE problems in Section[sec:preliminaries].

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Historically, MPC was primarily applied to systems with long timescales, most notably in chemical processing [Qin1996], due to the fact that during each time step, a computationally costly optimization problem has to be solved. More recent algorithmic developments[Diehl2002b,Li1989,Ohtsuka2004,Bemporad1999] and increasingly powerful embedded hardware render MPC real-time feasible for applications with shorter timescales such as autonomous driving, robotics, and avionics, as in some of the references cited above.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

A big role in bringing MPC to real-time applications is played by the implementation of efficient embedded optimal control methods, giving rise to software packages such as MPT[Herceg2013] for explicit MPC, qpOASES[Ferreau2014], an active-set solver for quadratic programming (QP), FORCES[Domahidi2012,Zanelli2017b], an interior-point solver for quadratically constrained quadratic programming (QCQP) and nonlinear programs with optimal control structure, and the ACADO Code Generation tool[Houska2011] for tailored sequential quadratic programming (SQP) based NMPC solvers. Other examples of nonlinear embedded optimization packages are VIATOC[Kalmari2015], GRAMPC[Englert2019] and FalcOpt[Torrisi2018], to which we compare acados in Section[sec:numerical\_results]. A non-exhaustive list of embedded optimization software packages can be found in Table[tab:software\_packages].

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

Ultimately, embedded software should run on a dedicated hardware platform.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we focus solely on central processing units (CPU) as the algorithms presented typically don't profit as much from the parallelization capabilities of massively parallel hardware platforms such as graphical processing units (GPU), tensor processing units (TPU) or field programmable gate arrays (FPGA). Please note that we don't pin ourselves down to a specific CPU architecture: acados has been shown to work with x86, x86\_64, ARMv7A, ARMv8A and PowerPC architectures.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Software packages for embedded optimization.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

| Software | Year | Latest Reference | Targets | License | As implemented by Pantelis Sopasakis.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

One challenge in developing software for embedded optimal control lies in the trade-off between flexibility, memory usage and speed. Many of the software packages mentioned in Table [tab:software\_packages] are based on automatic code generation. One reason for that is to have self-contained efficient linear algebra routines. Often however, the size of the problem and the choice of algorithms are then fixed for one specific optimal control instance, inducing a loss of flexibility. In some cases, a compiler or a human could generate faster or more memory-efficient code. For example, for linear algebra operations, the recently developed high-performance linear algebra package BLASFEO[Frison2018] outperforms code-generated triple-loop linear algebra routines and state of the art BLAS and LAPACK implementations for the moderate matrix size typical for embedded optimization applications. Since the linear algebra operations typically comprise most of the computational complexity of the algorithms considered, we can use standard compiler optimizations for the code surrounding the linear algebra routines without noticeably sacrificing performance (see Section[sec:numerical\_results]).

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

By basing \normalfont{\texttt{acados}}~on BLASFEO, we exchange self-containedness for performance and flexibility. We believe this is a better trade-off.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

Another challenge for embedded optimal control software is related to the process of software development. Often, to not sacrifice speed of execution and/or memory footprint, embedded optimal control software uses global data and suffers from tight coupling between algorithmic components. This might lead to a codebase that is difficult to understand, maintain and extend. We choose, as opposed to some other embedded optimal control software packages, to avoid these pitfalls by not unnecessarily sacrificing maintainability and readability of the codebase for a small gain in performance and/or a reduction of memory footprint. We try to achieve this goal by organizing the code in a modular fashion, with formal interfaces between the different algorithmic components, as described in Section This allows for a straightforward way of interchanging solvers, routines, and libraries needed for the embedded control algorithm.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

A final aspect of embedded optimal control software that affects flexibility, memory and runtime is the choice of modeling language and corresponding automatic differentiation tool. Several modeling languages exist, e.g., Mathematica, sympy or the MATLAB Symbolic Toolbox. Many of these languages make use of expression trees to represent mathematical functions, which potentially leads to a large code size, high memory usage and slow evaluation of higher-order derivatives for non-trivial models. On the contrary, the CasADi[Andersson2018] modeling language is based on expression graphs. This often leads to shorter instruction sequences and to smaller, typically faster code, which makes it more suitable for embedded applications. Also, it is free and open-source software. For these reasons, we favor CasADi for modeling nonlinear functions and differential-algebraic equations. Additionally, acados supports the use of hand-written or code-generated dynamic models as Csource files.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

- efficient optimal control algorithms implemented in C, - modular architecture enabling rapid prototyping of solution algorithms, - interfaces to Python and \textsc{Matlab{}}, - high-performance linear algebra based on BLASFEO[Frison2018], - compatible with CasADi expressions[Andersson2018], - deployable on a variety of embedded devices, - publicly available as permissively licensed free and open-source software.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Introduction", "weight": 1.5} -->

The remainder of the paper is organized as follows: in Section [sec:preliminaries], we review some important elements of nonlinear embedded optimization algorithms relevant to acados. We discuss recent advances in embedded optimization algorithms that motivate the development of acados in Section[sec:implementation]. The software package acados itself is introduced in Section[sec:acados]. Various numerical experiments including hardware-in-the-loop simulations as well as comparisons to other embedded optimization packages are presented in Section[sec:numerical\_results], and the paper is concluded in Section[sec:conclusion].

<!-- chunk {"id": "body-0018", "role": "body", "section": "Algorithmic ingredients for embedded nonlinear optimal control", "weight": 1.0} -->

In this section, we first introduce the problems that typically have to be solved for NMPC and MHE. We introduce a general formulation, that can facilitate both multiple-shooting discretized NMPC and MHE problems. Subsequently, we describe the algorithmic incredients of SQP-type methods as implemented in acadosfor the general problem.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Nonlinear Optimal Control", "weight": 1.0} -->

Let us first regard the continuous-time nonlinear optimal control problem (OCP) of the form In this notation, $x: \mathbb{R} \rightarrow \mathbb{R}^{n_x}$ denotes the differential states, $z: \mathbb{R} \rightarrow \mathbb{R}^{n_z}$ are the algebraic variables and $u: \mathbb{R} \rightarrow \mathbb{R}^{n_u}$ denotes the control inputs. Furthermore, we use $\ell: \mathbb{R}^{n_x} \times \mathbb{R}^{n_z} \times \mathbb{R}^{n_u} \rightarrow \mathbb{R}$ for the Lagrange term or running cost, $M: \mathbb{R}^{n_x} \rightarrow \mathbb{R}$ for the Mayer term or terminal cost.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Nonlinear Optimal Control", "weight": 1.0} -->

The dynamics are modeled with a set of implicit differential-algebraic equations (DAE) with right-hand-side $f: \mathbb{R}^{n_x} \times \mathbb{R}^{n_x} \times \mathbb{R}^{n_z} \times \mathbb{R}^{n_u} \rightarrow \mathbb{R}^{n_x} \times \mathbb{R}^{n_z}$. In the remainder of the paper, we assume the implicit DAE to be of index 1, i.e. $\partial f / (\partial \dot{x}, \partial z)$ is invertible.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Nonlinear Optimal Control", "weight": 1.0} -->

The nonlinear path constraints are given by $g: \mathbb{R}^{n_x} \times \mathbb{R}^{n_z} \times \mathbb{R}^{n_u} \rightarrow \mathbb{R}^{n_g}$, and the initial value of the states is $\overline{x}_0 \in \mathbb{R}^{n_x}$. We consider the horizon length $T$to be fixed.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Multiple Shooting Discretization", "weight": 1.0} -->

In acados, we discretize nonlinear OCPs with a multiple shooting approach[Bock1984]. We introduce a time grid $[t_0, t_1, \ldots, t_N]$ with $t_k < t_{k+1}, k=0,\ldots,N-1$, discrete state variables $x_0, \ldots, x_N$, algebraic variables $z_0, \ldots, z_{N-1}$ and controls $u_0, \ldots, u_{N-1}$. For the control trajectory, we choose a piecewise constant control parametrization. On each time interval $ \left[t_k, t_{k+1} \right)$, we can then write the result of the numerical simulation routine as where the separate components will be denoted by $\phi_k^x(x_k, u_k)$ and $\phi_k^z(x_k, u_k)$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Multiple Shooting Discretization", "weight": 1.0} -->

The multiple shooting approach can often lead to better convergence behavior compared to single shooting, where the simulation and optimization is performed sequentially, as shown in The resulting nonlinear programming (NLP) formulation looks as follows: The optimal control formulation above is not the most general one that acados can handle: among others moving horizon estimation (MHE) problems, constraint relaxation via slack variables and equality constraints are supported as well. The next section presents a more general class of optimization problems which is handled by acados.

<!-- chunk {"id": "body-0024", "role": "body", "section": "General Nonlinear Optimal Control structured Optimization Problem", "weight": 1.0} -->

In order to facilitate many different OCP formulations occurring in practice, acados uses the following general formulation of nonlinear optimal control structured optimization problems: Here, the initial state constraint from [eq:NOCP\_initial\_state] is contained in the inequality constraint [eq:acados\_OCP\_ineq] for $ k = 0 $.

<!-- chunk {"id": "body-0025", "role": "body", "section": "General Nonlinear Optimal Control structured Optimization Problem", "weight": 1.0} -->

Note that this general formulation also includes slack variables $ s_k $ which could alternatively be formulated as control inputs $ u_k $. However, the slack variables $ s_k $ do not enter the system dynamics [eq:acados\_OCP\_eq] and can only enter the cost linearly and quadratically, i.e. via the functions $ \rho_k(\cdot) $ of the form \rho_k(s_k) = \sum_{i=1}^{n_{s_k}} \alpha_k^i s_k^i + \beta_k^i {s_k^i}^2, with $ \alpha_k^i\in\mathbb{R} $, $ \beta_k^i> 0 $. These properties motivate the separation between slack and control variables and allow for an efficient treatment in solution methods as implemented in acados. The slack variables can be used to formulate soft constraints or model piecewise quadratic possibly assymetric cost functions among others.

<!-- chunk {"id": "body-0026", "role": "body", "section": "General Nonlinear Optimal Control structured Optimization Problem", "weight": 1.0} -->

Soft constraints are often useful in practice, for example to deal with constraint violations due to model-plant mismatch or disturbances that would yield infeasibility of [eq:multiple\_shooting].

<!-- chunk {"id": "body-0027", "role": "body", "section": "General Nonlinear Optimal Control structured Optimization Problem", "weight": 1.0} -->

Moreover, acados is able to handle the most common types of cost and constraint functions in a tailored fashion. Regarding the cost functions $ l_k(\cdot) $, $ M(\cdot) $, acados is capable of exploiting the structure of the widely used linear and nonlinear least-squares functions, while also being able to handle general nonlinear functions.

<!-- chunk {"id": "body-0028", "role": "body", "section": "General Nonlinear Optimal Control structured Optimization Problem", "weight": 1.0} -->

Within the constraint functions $ g_k(\cdot) $, acados is able to exploit the most common constraint types, which are simply bounds on $ x_k $ and $ u_k $, linear constraints in $ x_k $ and $ u_k $, such that only truly nonlinear constraints have to be formulated and treated as such, and one could write $ g_k(\cdot) $ as g_k(x_k,z_k,u_k) = \begin{bmatrix} {J\ind{bx}}_{,k} x_k \\ {J\ind{bu}}_{,k} u_k \\ C_{\mathrm{x},k} x_k + C_{\mathrm{u},k} u_k\\ g\ind{nonl}(x_k,z_k,u_k) \end{bmatrix},%\begin{bmatrix} {J\ind{bx}}_k x \\ {J\ind{bu}}_k u \\

<!-- chunk {"id": "body-0029", "role": "body", "section": "General Nonlinear Optimal Control structured Optimization Problem", "weight": 1.0} -->

Additionally, it is common to have upper and lower bounds on a constraint component of $ g_k $, which allows for a more efficient treatment of these constraints within acados.

<!-- chunk {"id": "body-0030", "role": "body", "section": "General Nonlinear Optimal Control structured Optimization Problem", "weight": 1.0} -->

The above NLP[eq:acados\_OCP] could be solved by any general-purpose NLP solver, like IPOPT [Waechter2006]. The current scope of acados, however, encompasses efficient embedded optimal control methods for solving such structured NLPs, since these are better suited in a real-time and/or embedded setting[Diehl2009c]. Sequential Quadratic Programming (SQP) is an example of an embeddable optimization method and will be discussed in the following section.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Sequential Quadratic Programming and Real-Time Iterations", "weight": 1.0} -->

We briefly present the structure of an SQP algorithm as implemented in acados.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Sequential Quadratic Programming and Real-Time Iterations", "weight": 1.0} -->

- numerical integration of the continuous-time dynamics, - generation of first-order and possibly second-order sensitivities of objective and constraints, - a procedure for approximating the Hessian matrix, - an efficient QP solver (typically developed separately). globalization strategies such as line search or trust regions are considered out of scope for this paper, because globalization is not recommended in a real-time setting, since runtime bounds can not be established in general [Diehl2002b], and the initializations are typically close to the exact solution [Gros2006]. In practice, globalization is typically not necessary. Possibly extending acados with globalization strategies such as merit functions[Leineweber1999] and filter based line search methods [Waechter2006a]for use in a fully converged setting is subject of future work.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Sequential Quadratic Programming and Real-Time Iterations", "weight": 1.0} -->

Note that the algebraic variables have been eliminated from the OCP, but numerical approximations of these values are accessible from the numerical integration routine. The step $\Delta w^\mathrm{QP}$is computed by solving the following QP: Above, we used the shorthands $ \bar{\phi}^x_k, \, \bar{g}_k,\, k=0,\ldots, N-1$ and $\bar{g}_N$ to denote the function evaluations $\phi^x_k(x_k, u_k), \,g_k(x_k, z_k, u_k)$ and $g_N(x_N)$, respectively. We formulate the NLP in such a way that the slack variables appear directly as tailored optimization variables. We note that some, but not all QP solvers can deal with slack variables directly. For those that do not, slack variables are reformulated as extra input variables.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Sequential Quadratic Programming and Real-Time Iterations", "weight": 1.0} -->

In the remainder of this section, we discuss each of the ingredients of an efficient SQP solver, described above, separately. Generation of sensitivities using numerical integration will be treated in Section [sec:numerical\_simulation], Hessian approximation in Section[sec:convex\_hessians], structure-exploiting QP solvers in Section[sec:qp\_solvers] and real-time considerations in Section[sec:embedded\_sqp].

<!-- chunk {"id": "body-0035", "role": "body", "section": "Numerical simulation and sensitivities", "weight": 1.0} -->

An important part of the implementation of direct shooting methods for optimal control consists of reliably and efficiently computing numerical simulation and sensitivity results for the nonlinear system of differential-algebraic equations that represents a dynamic model for our particular system of interest.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Numerical simulation and sensitivities", "weight": 1.0} -->

Within the family of single-step integration methods one typically distinguishes between explicit and implicit schemes Well-known examples of explicit integration schemes include explicit Runge-Kutta(RK) formulas such as explicit Euler and the RK method of order$4$. Explicit integration schemes are easy to implement since they rely on a direct combination of explicit evaluations of the right-hand side of the system dynamics. Instead, implicit integration schemes result in a nonlinear system of equations that implicitly defines the numerical simulation result. Unlike explicit integration methods, the nonlinear system in implicit integration schemes generally needs to be solved numerically using an iterative procedure such as a Newton-type method. However, implicit formulas are very popular in practice because of their improved numerical stability properties and higher order of accuracy. Especially in case of stiff dynamical systems and implicit or differential-algebraic equations, an implicit integration scheme should often be used[Hairer1991].

<!-- chunk {"id": "body-0037", "role": "body", "section": "Numerical simulation and sensitivities", "weight": 1.0} -->

When using these numerical integration schemes within direct multiple shooting, one additionally needs a computationally efficient and reliable way of computing first (and possibly second) order derivatives of the simulation results with respect to the state and control input values: $$\dfrac{\partial \phi^x_k(x_k, u_k)}{\partial x_k}, \quad \dfrac{\partial \phi^x_k(x_k, u_k)}{\partial u_k}, \quad \sum_{i=1}^{n_x}\pi_{k,i} \dfrac{\partial^2 \phi^x_{k,i}(x_k, u_k)}{\partial^2 (x_k, u_k)},$$ where $\pi_k \in \mathbb{R}^{n_x}$ is called the seed vector, for which the Lagrange multipliers are used to compute the exact Hessian of the Lagrangian.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Numerical simulation and sensitivities", "weight": 1.0} -->

Sensitivity propagation for direct optimal control methods is typically based on a discretize-then-differentiate type of approach such as internal numerical differentiation(IND) in[Bock1983]. For the class of explicit integration methods, this concept leads to a forward or backward sensitivity propagation based on algorithmic differentiation(AD) techniques[Griewank2000]. In case of an implicit integration scheme, the IND approach either results in iterative differentiation techniques or a direct computation of sensitivities based on the implicit function theorem[Albersmeyer2010b]. In addition, forward-backward propagation schemes can be derived to compute the symmetric Hessian contributions[Quirynen2017a]. [Quirynen2017b,Quirynen2018] proposed an algorithmic approach to embed implicit integration schemes with sensitivity analysis in Newton-type optimization for direct optimal control without the need for any iterative procedure, based on the concepts of numerical condensing and expansion in a lifted Newton-type optimization method[Albersmeyer2010].

<!-- chunk {"id": "body-0039", "role": "body", "section": "Convex Hessian Approximation Methods", "weight": 1.0} -->

Gauss-Newton Hessian approximation. In the case of a (nonlinear) least-squares objective in[eq:acados\_OCP], e.g. when tracking a reference, we have with $r: \mathbb{R}^{n_x} \times \mathbb{R}^{n_u} \rightarrow \mathbb{R}^{n_{\mathrm{r}_k}}$, $r_N: \mathbb{R}^{n_x} \rightarrow \mathbb{R}^{n_{\mathrm{r}_N}}$. Notice that this kind of residual function is a common case in embedded optimization.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Convex Hessian Approximation Methods", "weight": 1.0} -->

The Gauss-Newton Hessian approximation amounts to linearizing "between the norm signs".

<!-- chunk {"id": "body-0041", "role": "body", "section": "Convex Hessian Approximation Methods", "weight": 1.0} -->

Since no second-order sensitivities are necessary, the Gauss-Newton Hessian approximation offers a competitive alternative to SQP with exact Hessians, although it converges linearly only. We remark that for a quadratic objective function in[eq:acados\_OCP], the same quadratic objective arises in[eq:OCP\_QP\_subproblem], and no additional computations are needed. For more details on Gauss-Newton methods in the context of NMPC, we refer the reader to[Gros2016].

<!-- chunk {"id": "body-0042", "role": "body", "section": "Convex Hessian Approximation Methods", "weight": 1.0} -->

Sequential Convex Quadratic Programming (SCQP).

<!-- chunk {"id": "body-0043", "role": "body", "section": "Convex Hessian Approximation Methods", "weight": 1.0} -->

A generalization to using SQP with a Gauss-Newton Hessian approximation is sequential convex quadratic programming In a sense, a Gauss-Newton SQP algorithm neglects any curvature present in the inequality constraints by linearizing them. In practice however, convex-over-nonlinear objectives and/or constraints arise often, which are of the form $\varphi(c(x, u))$ with a convex function $\varphi(\cdot)$ and a nonlinear function $c(\cdot)$. Examples include ellipsoidal terminal constraints to ensure stability of an NMPC scheme, the friction ellipse in automotive applications, or tunnel-following for robotic manipulators.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Convex Hessian Approximation Methods", "weight": 1.0} -->

In SCQP, we still linearize the inequalities, but bring the convex contributions from the inequality constraints, multiplied with a Lagrange multiplier, into the Hessian approximation. Doing so, the SCQP Hessian is guaranteed to be positive semi-definite. For problems that feature convex-over-nonlinear constraints, this Hessian contribution offers better convergence guarantees than a Gauss-Newton Hessian Structure-preserving convexification with minimal regularization.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Convex Hessian Approximation Methods", "weight": 1.0} -->

In the last two paragraphs, we devised two Hessian approximations which are convex However, when the exact Hessian of the Lagrangian is used, it might be indefinite. When this happens, the optimal direction $\Delta w_\mathrm{QP}$ cannot be guaranteed to be a descent direction. Furthermore, many QP solver codes expect a positive (semi-)definite Hessian, even if the second order sufficient conditions for optimality are met. The aim of regularization is to obtain an approximation $\widetilde{H} = \mathrm{blkdiag}(\widetilde{H}_0,\ldots,\widetilde{H}_N)$ with each $\widetilde{H}_k \succ 0$. We very briefly discuss three different methods here and compare their convergence in an SQP-type setting in Section[sec:numerical\_results]. $V_k D_k V_k^{-1}$ be the eigenvalue decomposition of $H_k$, for $k=0,\ldots,N$.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Convex Hessian Approximation Methods", "weight": 1.0} -->

Two simple ways of regularizing the Hessian blocks are \widetilde{H}_k &= \mathrm{project}(H_k,\epsilon):= V_k \, \big[\mathrm{maxdiag}(\epsilon, D_k) \big] \, V_k^{-1}, \\\widetilde{H}_k &= \mathrm{mirror}(H_k,\epsilon):= V_k \, \big[\mathrm{maxdiag}(\epsilon, \mathrm{abs}(D_k)) \big] \, V_k^{-1}, with $\epsilon$ small, $ \mathrm{abs}(\cdot)$ defined elementwise and $ \mathrm{maxdiag}(\cdot, \cdot) $ selecting the maximum values on the diagonal while not changing the off-diagonal elements.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Convex Hessian Approximation Methods", "weight": 1.0} -->

Another approach is to exploit the optimal control problem structure of[eq:OCP\_QP\_subproblem]. One approach of this kind is called convexification and has been proposed in[Verschueren2017]. The difference with more naive regularization methods as stated above, is that it first exploits as much convexity as possible through the optimal control structure, before regularizing the remaining negative directions. The complexity of the regularization method is linear in the horizon length, and under some conditions, the SQP iterates converge quadratically to a local solution. An efficient implementation of this new Hessian regularization method is included in acados. A numerical example is given in Section[sec:numerical\_results], which shows the superior convergence behavior of convexification with respect to the mirror and project regularization techniques.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Convex Hessian Approximation Methods", "weight": 1.0} -->

Further convex Hessian approximations Other Hessian approximations exist in the literature, such as BFGS and its limited-memory variant (see [Nocedal2006]). They might be added to acadosin the future.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Structure-exploiting embedded QP solvers", "weight": 1.0} -->

There exist different solution strategies for QP [eq:OCP\_QP\_subproblem], which we briefly describe in this section. We note that linear-quadratic optimal control problems can be efficiently solved with the same kind of QP solving strategies presented. As such, acados, conceived as a modular software package, can also be used to facilitate solving linear-quadratic QPs, arising in linear-quadratic MPC.In the following subsections, we give an overview on sparsity exploitation for optimal control structred QPs.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Structure-exploiting embedded QP solvers", "weight": 1.0} -->

Sparse approach. OCP[eq:OCP\_QP\_subproblem] can be solved directly by using a general-purpose sparse QP solver, e.g., CVXGEN[Mattingley2012], OOQP[Gertz2003], both primal-dual interior-point solvers, or OSQP[Stellato2020], a first-order method. First-order methods are mainly based on either the fast gradient method or the alternating direction method of multipliers (ADMM). The strict real-time requirements for solution methods make first-order methods a viable candidate. However, they might suffer from slow convergence rates. For an overview of first-order methods in the context of embedded optimal control, see[Ferreau2017,Kouzoupis2015].

<!-- chunk {"id": "body-0051", "role": "body", "section": "Structure-exploiting embedded QP solvers", "weight": 1.0} -->

Structured approach. OCP[eq:OCP\_QP\_subproblem] is solved by exploiting its multi-stage structure, but dense linear algebra is used. An example is the approach from[Steinbach1995,Rao1998] and in solvers like FORCES[Domahidi2012,Zanelli2017b], HPMPC[Frison2014] and HPIPM[Frison2020a], which are all interior-point solvers.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Structure-exploiting embedded QP solvers", "weight": 1.0} -->

Condensing approach. An alternative to the previous approaches is the so-called condensing approach[Bock1984]. By eliminating the state variables by means of the dynamic equality constraints in[eq:OCP\_QP\_subproblem], we obtain a smaller QP with only the control inputs and possibly the initial state as optimization variables. Any general-purpose dense QP solver can then be used to solve the smaller QP, e.g. an active-set solver like qpOASES[Ferreau2014] or an interior-point method like the dense variant in HPIPM. Since qpOASES is able to reuse information (i.e. warm-starting) from one problem to the next, it is particularly well-suited for (N)MPC. Condensing is shown to be of quadratic complexity in the horizon length[Frison2015a].

<!-- chunk {"id": "body-0053", "role": "body", "section": "Structure-exploiting embedded QP solvers", "weight": 1.0} -->

Partial condensing. A mix between the two previous approaches (i.e. structured, condensing) for solving[eq:OCP\_QP\_subproblem] can be obtained by not eliminating all state variables, but only per blocks of $N / N_2$ stages (we assume for simplicity that $N$ is an integer multiple of $N_2$), where $N_2$ is the `new' horizon length of the partially condensed problem. By this additional degree of freedom, partial condensing enables us to find a better trade-off between horizon length and number of optimization variables, for a given problem. For more details on partial condensing, the reader is referred to[Axehill2015].

<!-- chunk {"id": "body-0054", "role": "body", "section": "Structure-exploiting embedded QP solvers", "weight": 1.0} -->

Further condensing strategies. There are further condensing strategies in the literature, which might be added to \normalfont{\texttt{acados}}~in the future. A method called complementary condensing was proposed in [Kirches2012b], where the KKT system is solved in the space of the multipliers corresponding to the equality constraints. This approach favorable if the problem has more control inputs than states.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Structure-exploiting embedded QP solvers", "weight": 1.0} -->

The dual Newton strategy is an algorithm that is based on dual decomposition tailored to linear-quadratic OCPs in the form of [eq:OCP\_QP\_subproblem], with an open-source implementation in the software qpDUNES[Frasch2015].

<!-- chunk {"id": "body-0056", "role": "body", "section": "Structure-exploiting embedded QP solvers", "weight": 1.0} -->

A main advantage of the dual Newton strategy, as in most active set methods, is warm-starting. Contrary to qpOASES, qpDUNES can perform multiple active set changes per iteration. However, a premature termination of the algorithm does not return a meaningful solution as in the case ofqpOASES since it is not feasible nor optimal for a neighboring problem. As recently observed in[Kouzoupis2015b], the convergence ofqpDUNEScan benefit significantly from a partial condensing preprocessing step.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Real-time iterations", "weight": 1.0} -->

In a real-time control setting, we solve NLP [eq:acados\_OCP] in sequence and under stringent time conditions. Since the environment is anyway changing continuously, it is often sufficient to solve it approximately it is of no use to have a high-accuracy but past-the-deadline solution.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Real-time iterations", "weight": 1.0} -->

One such online method is the real-time iteration (RTI) scheme It solves an inequality-constrained QP in each iteration. The resulting generalized predictor is better suited for predictions across active set changes, than e.g. a tangential predictor obtained from an interior-point method. For a brief overview, we refer the reader to[Diehl2009c].

<!-- chunk {"id": "body-0059", "role": "body", "section": "Real-time iterations", "weight": 1.0} -->

In each RTI, one full iteration of an SQP-type scheme is performed, including generation of the sensitivities w.r.t.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Real-time iterations", "weight": 1.0} -->

We could introduce additional approximations by not updating all sensitivities in each RTI[Zanelli2019]. Such approximations exist on different levels: from only updating the initial state constraint with the current estimate of the state of the system, over updating the right-hand side of the (in)equality constraints, to the full RTI. By interleaving different approximations at different sample times, we obtain a multi-level iterations scheme, as introduced by[Bock2005].

<!-- chunk {"id": "body-0061", "role": "body", "section": "Algorithm implementations in acados", "weight": 1.0} -->

In this section, we focus on the algorithm implementations in Since acados builds on other software to handle basic linear algebra operations (BLASFEO[Frison2018]) and QPs (HPIPM[Frison2020a]), these will be presented first. Afterwards, a short description of integrators and SQP-type optimization solvers will be given.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Linear algebra: BLASFEO", "weight": 1.0} -->

At the heart of all embedded optimization routines lies either an implementation of a small set of linear algebra routines (e.g. matrix-matrix multiplication, Cholesky decomposition), or a call to a specialized linear algebra library (e.g.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Linear algebra: BLASFEO", "weight": 1.0} -->

BLAS and LAPACK). Generally BLAS implementations focus on performance for large dense matrices, as used in high-performance computing and data science. Considerably less investigated are BLAS and LAPACKimplementations for small dense matrices.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Linear algebra: BLASFEO", "weight": 1.0} -->

Often, the linear algebra code in embedded optimization packages, for example in the ACADO Code Generation tool or Forces Pro, is code-generated. For very small matrix sizes (e.g. $4 \times 4$), this technique outperforms optimized linear algebra libraries. Furthermore, code-generation has the advantage that the code can be kept `library-free'. However, for larger matrix sizes (e.g. in the range $10 \times 10$ to $100 \times 100$, typical in MPC applications), code-generated linear algebra routines underperform with respect to optimized libraries.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Linear algebra: BLASFEO", "weight": 1.0} -->

BLASFEO[Frison2018] is a linear algebra package that targets computations for small matrices. It offers highly optimized linear algebra routines (e.g. dgemm, dsyrk, dpotrf), tailored for the matrix sizes typically encountered in embedded optimization. These routines exploit architecture-specific vector instructions for floating point operations (e.g. AVX), and focus on performance for matrices fitting in cache.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Linear algebra: BLASFEO", "weight": 1.0} -->

BLASFEO defines a packed matrix format (called panel major) which optimizes the cache usage, guaranteeing close to peak performance for matrices of sizes up to a couple hundreds. All high-performance BLASFEO routines use this panel major matrix format, and there is a rich set of auxiliary routines to operate on this matrix format, as well as to convert from/to column- or row-major formats. In this sense, BLASFEOprovides a complete linear algebra framework, which can be used to implement many fast optimization algorithms.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Linear algebra: BLASFEO", "weight": 1.0} -->

Except for trivially small matrices, BLASFEO enables a considerable speedup (up to $10\times$ for some matrix sizes) in the matrix computations, compared to code-generated linear algebra kernels. For all small matrix sizes up to, say, $300 \times 300$, BLASFEO offers a considerable speedup compared to state-of-the-art BLAS implementations, like OpenBLAS, too. The use of BLASFEO is one of the factors why acados performs better than ACADO on medium-scale problems, as we will see in Section[sec:numerical\_results].

<!-- chunk {"id": "body-0068", "role": "body", "section": "Quadratic programming: HPIPM", "weight": 1.0} -->

In the implementation of SQP-type algorithms, QP sub-problems need to be solved efficiently at each iteration. The QP sub-problem solution is typically one of the two most expensive steps in SQP schemes, the other being the simulation and sensitivity computations of dynamical systems.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Quadratic programming: HPIPM", "weight": 1.0} -->

HPIPM[Frison2020a] is a library defining three QP types (dense QP, OCP QP and tree-structured OCP QP, all handling soft constraints via tailored slack variables), and a rich set of routines to create, manage and solve the QPs. All QP solvers are Mehrotra's type primal-dual interior point methods, and they are implemented using the BLASFEOlinear algebra framework.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Quadratic programming: HPIPM", "weight": 1.0} -->

HPIPMprovides a set of efficiently implemented routines to convert between the different QP types, e.g. condensing routines convert an OCP QP into a dense QP, partial condensing routines convert an OCP QP into another OCP QP with shorter horizon length. Additional expansion routines recover the original QP solution from the (partially) condensed one. acados, the QP framework is based on HPIPM, in the sense that HPIPM provides both the dense QP and OCP QP definitions, as well as (partial) condensing algorithms to convert them and interior-point methods to solve them. Numerous other QP solvers are then interfaced to acados to alternatively solve the same types of QP problems. At the time of writing, additional interfaces exist toHPMPC, qpDUNES, qpOASES, and OSQP.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Algorithmic Differentiation", "weight": 1.0} -->

The main difference between software packages for linear quadratic MPC and nonlinear MPC is that NMPC packages need a modeling language for the nonlinear functions. We support CasADi, a graph-based source transformation algorithmic differentiation tool[Andersson2018]. In our workflow, a user would typically specify the dynamic continuous-time models and nonlinear constraint functions with CasADi in a high-level language such as \textsc{Matlab{}} or Python. In combination with CasADi's code generator we obtain fast, embeddable code, see Section [sec:high\_level\_interfaces].

<!-- chunk {"id": "body-0072", "role": "body", "section": "Numerical simulation", "weight": 1.0} -->

acados features different kinds of numerical simulation routines. There are implementations of explicit and implicit Runge-Kutta integrators available, both of which support the optional propagation of first-order forward and adjoint sensitivities, as well as second-order sensitivities. The explicit integrators can be used with explicit ODE models and supports different Butcher tableaus, including Euler's method and RK4. Moreover, the implicit integrators can be used with an index-1 differential-algebraic equation (DAE) or implicit ODE model and use the Gauss-Legendre Butcher tableaus. A novel implementation for lifted collocation integrators[Quirynen2017b] has been made part of acados, as well as a recently proposed structure-exploiting IRK algorithm, the so-called GNSF-IRK scheme[Frey2019], discussed next.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Numerical simulation", "weight": 1.0} -->

The concept of GNSF-IRK is to rigorously exploit the linear dependencies within the dynamic system. It extends the ideas of the linear input and linear output subsystems that have been implemented within the ACADO Code Generation tool[Quirynen2013a] and uses a more flexible structured dynamic system formulation that can also handle index-1 DAEs. A main challenge for structure-exploiting integrators is to appropriately reformulate the dynamic system of interest into the desired structured form. acados features an automatic transcription method for the GNSF structure[Frey2019], implemented as a \textsc{Matlab{}}function for CasADimodels.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Numerical simulation", "weight": 1.0} -->

A last important feature of acadosis that integrators can vary from stage to stage, with e.g. different state and control dimensions, different integration step length, or different integration schemes.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Numerical simulation", "weight": 1.0} -->

We note that all integrator modules, except for the ERK integrator, are based on hardware tailored linear algebra routines in BLASFEO to speed up the LU factorizations and the corresponding triangular system solutions, as discussed in[Frison2017].

<!-- chunk {"id": "body-0076", "role": "body", "section": "SQP-type methods", "weight": 1.0} -->

For nonlinear programming, acados offers different SQP-like methods. A full-step SQP method is available, with different algorithmic options. As Hessian approximations, we have Gauss-Newton Hessians, SCQP, and exact Hessians with regularization/convexification as discussed in Section[sec:embedded\_sqp], and we allow for user-defined Hessian approximations. For use in an online setting, e.g. in NMPC, a specialized RTI routine is available.

<!-- chunk {"id": "body-0077", "role": "body", "section": "SQP-type methods", "weight": 1.0} -->

Both the SCQP algorithm and the convexification method of Section [sec:convex\_hessians]are novel features, to the authors' knowledge, not present in any other NMPC software packages.

<!-- chunk {"id": "body-0078", "role": "body", "section": "The acados software package", "weight": 1.0} -->

acados implements some of the optimization methods mentioned in the previous sections. acados is meant to be user-friendly at a high level, and efficient at a low level. In order to balance these properties, we developed a core library written in C which exposes functionality to the Python and \textsc{Matlab{}}interfaces. In this section, we first discuss the functionality of this inner core module, we then describe internal and external interfaces that are crucial for usability.

<!-- chunk {"id": "body-0079", "role": "body", "section": "The acados core library", "weight": 1.0} -->

The embedded optimization algorithms discussed in Section [sec:preliminaries] are implemented in acados in a modular fashion. For example, there is a clear interface between an NLP solver and an integrator.

<!-- chunk {"id": "body-0080", "role": "body", "section": "The acados core library", "weight": 1.0} -->

The integrator expects a linearization point $w^{[i]}$and returns the end state of a simulated trajectory, and optionally first- and second-order sensitivities: confidence=None created_by=None text='\\begin{tikzpicture}\n\\begin{tikzcd}[every arrow/.append style={shift left}]\n\t\\mathrm{NLP~solver} \\arrow{r}{\\mathrm{lin.~point}} &\\mathrm{integrator} \\arrow{l}{\\mathrm{sim., sens.}}\n\\end{tikzcd}\n\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> Similar diagrams can be drawn for all other algorithmic components, including (partial) condensing, QP solvers, function evaluations etc. Each of these algorithmic components are modeled within acados as separate modules.

<!-- chunk {"id": "body-0081", "role": "body", "section": "The acados core library", "weight": 1.0} -->

Some modules can be used as standalone modules, or in combination with others. For instance, depending on the choice of algorithm, an NLP solver will make use of some or all of the other modules. In Table[tab:modules], we see an overview of all modules currently present in acados, together with the implemented algorithmic variants.

<!-- chunk {"id": "body-0082", "role": "body", "section": "The acados core library", "weight": 1.0} -->

Overview of the software modules present in acados.

<!-- chunk {"id": "body-0083", "role": "body", "section": "The acados core library", "weight": 1.0} -->

It is an important design choice that all modules are identical in their signature. That way, all modules look similar to the users of For developers, it should be straightforward to extend acados with another module. The signature is as follows (in Csyntax): int (void *config, <module> stands for the name of the module at hand, for example ocp\_qp for QP problems with optimal control structure or sim for integration problems, and <solver> is a placeholder for a function implementing the specific solver for problems corresponding to this module, e.g., ocp\_qp\_hpipm (interface to HPIPM solver) or sim\_erk (explicit Runge-Kutta method), etc. Each module returns an int which denotes a solver-specific error status zero means successful completion by convention. All input arguments are pointers.

<!-- chunk {"id": "body-0084", "role": "body", "section": "The acados core library", "weight": 1.0} -->

Each of the arguments comes with a set of helper functions, called...\_calculate\_size, computing the size (in bytes) of the struct pointed to, as well as a set of functions, called...\_assign, to initialize a block of memory.

<!-- chunk {"id": "body-0085", "role": "body", "section": "The acados core library", "weight": 1.0} -->

Some modules comprise other modules. For example, an SQP solver for optimal control problems might need an integrator, which is on its own a proper In this context, we call the integrator a submodule. Each of the arguments above, dims etc., have fields corresponding to submodules. As an example, the relation between an NLP solver and its submodules is depicted in Figure[fig:submodules]. We remark that the calculation of the memory size of a module with submodules is done recursively, i.e., calling the calculate\_size function on the top module returns the required memory size of the top module and all of its submodules, and submodules of submodules, etc. This allows users to allocate all the memory outside of acados, by design.

<!-- chunk {"id": "body-0086", "role": "body", "section": "The acados core library", "weight": 1.0} -->

module=[rectangle,draw=black!50,fill=gray!20,node distance=18pt] confidence=None created_by=None text='\\begin{tikzpicture}\n\t\\node[module] (dyn) [align=center] {dynamics \\\\ (continuous)};\n\t\\node[module] (int) [below=of dyn, align=center] {simulation \\\\ (ERK)};\n\t\\node[module] (ext1) [below=of int, align=center] {external \\\\ function};\n\t\\node[module] (cos) [right=of dyn, align=center] {cost \\\\ (nonlinear)};\n\t\\node[module] (ext2) [below=of cos, align=center] {external \\\\ function};\n\t\\node[module] (con) [right=of cos, align=center] {constraints \\\\

<!-- chunk {"id": "body-0087", "role": "body", "section": "The acados core library", "weight": 1.0} -->

(nonlinear)};\n\t\\node[module] (ext3) [below=of con,align=center] {external \\\\function};\n\t\\node[module] (qps) [right=of con, align=center] {OCP QP solver \\\\ (HPIPM)};\n\t\\node (mid) at ($(cos)!0.5!(con)$) {};\n\t\\node[module] (NLP) [above=of mid, align=center] {OCP NLP solver \\\\ (SQP)};\n\t\\draw -> (dyn) -- (NLP);\n\t\\draw -> (cos) -- (NLP);\n\t\\draw -> (con) -- (NLP);\n\t\\draw -> (qps) -- (NLP);\n\t\\draw -> (int) --

<!-- chunk {"id": "body-0088", "role": "body", "section": "The acados core library", "weight": 1.0} -->

(dyn);\n\t\\draw -> (ext1) -- (int);\n\t\\draw -> (ext2) -- (cos);\n\t\\draw -> (ext3) -- (con);\n\t\\end{tikzpicture}' language=<CodeLanguageLabel.TIKZ: 'Tikz'> Example of the relation between modules and submodules in acados for a specific case of a possible SQP algorithm.

<!-- chunk {"id": "body-0089", "role": "body", "section": "The acados core library", "weight": 1.0} -->

core library of acados contains mostly what has been described in this section: a collection of modules, each with corresponding data types and variants of solvers, as well as helper functions for memory management. Using the core library directly can be cumbersome and error-prone, as many details need to be taken into account: it is designed to be efficient and flexible. To cater to the specific needs of the end user, we offer different interfaces to the core of acados, which are described next.

<!-- chunk {"id": "body-0090", "role": "body", "section": "The C interface", "weight": 1.0} -->

C interface is responsible for encapsulating the low-level constructs of the acadoscore.

<!-- chunk {"id": "body-0091", "role": "body", "section": "The C interface", "weight": 1.0} -->

Choosing Solvers. When working with the core library, all functions are specific to one variant of a module: when solving a QP, say, qpOASES, the code will refer to structs like dense\_qp\_qpoases\_memory, dense\_qp\_qpoases\_opts, etc. We provide an abstraction layer to facilitate switching solvers easily. To this end, for each module we define a `plan'. A plan is a struct that contains a number of fields representing the choice of a particular combination of solvers. For example, the plan for an SQP-type method with Gauss-Newton Hessian approximation, for a problem discretized with an ERK integrator using HPIPM as an underlying QP solver, reads as ocp_nlp_solver_plan plan = { {PARTIAL_CONDENSING_HPIPM}, {ERK, ERK, ERK,...}, Here, the arrays should be of the correct length (omitted for brevity, with a slight abuse of notation).

<!-- chunk {"id": "body-0092", "role": "body", "section": "The C interface", "weight": 1.0} -->

As a general rule, solvers that make use of other modules should include them in their plan.

<!-- chunk {"id": "body-0093", "role": "body", "section": "The C interface", "weight": 1.0} -->

For each module, we manipulate a specific options structusing functions that take a textual representation of the option via a string. The string encodes both the module that the option belongs to, as well as the name of the option.

<!-- chunk {"id": "body-0094", "role": "body", "section": "The C interface", "weight": 1.0} -->

Memory management. Allocating memory `manually' as described above can quickly become cumbersome. For this reason, we make available a few routines that automate that process. To this end, in the C interface each module from the core library is mirrored by an additional function with signature _solve(_solver *solver, solver is a pointer to a C structure that encapsulates the data needed other than input and output. By doing so, we reduce the amount of boilerplate code.

<!-- chunk {"id": "body-0095", "role": "body", "section": "The C interface", "weight": 1.0} -->

C interface additionally offers helper routines, so-called `setters' and `getters', that wrap the handling of the low-level structs of the acadoscore.

<!-- chunk {"id": "body-0096", "role": "body", "section": "High-level interfaces", "weight": 1.0} -->

Often, software for NMPC is coded in scripting languages. Therefore, we offer interfaces to two popular languages for scientific computing: Python and \textsc{Matlab{}}, where the interface to \textsc{Matlab{}} is largely compatible with its free and open-source alternative Octave. As such, we created a small domain-specific language within each of these frameworks. We build on top of code from the C interface of acados.

<!-- chunk {"id": "body-0097", "role": "body", "section": "High-level interfaces", "weight": 1.0} -->

In order to formulate the OCP [eq:acados\_OCP] through the acados modules (cost, constraints and dynamics), the main challenge is to pass the generally nonlinear functions and their derivatives to these modules. The Python and \textsc{Matlab{}} interfaces of acados use CasADi as a modeling language, i.e. to formulate all generally nonlinear parts of the OCP. The acados high level interfaces are able to use CasADi's code generation and algorithmic differentiation to generate the C functions needed for each acados module. A major benefit of using CasADi as a modeling language is that the solution behavior of acados can be easily compared with the solutions coming from the numerous optimization tools interfaced with CasADi.

<!-- chunk {"id": "body-0098", "role": "body", "section": "High-level interfaces", "weight": 1.0} -->

Once the OCP to be solved is described through the domain-specific language implemented by the high-level interfaces, a human readable self-con tained C project that makes use of templated code can be generated. The generated project contains all the C code necessary for function and derivative evaluations generated through CasADi and the C code necessary to set up the NLP solver using the acados C interface. Moreover, a \textsc{Matlab{}} S-Function and a build system for its compilation is generated. Note that this kind of code generation is inherently different from the one in ACADO, since the templated code uses only the functions exposed by the C interface of acados. In contrast to this, ACADO generated solvers are standalone C projects that are extremely problem specific and do not rely on a common library.

<!-- chunk {"id": "body-0099", "role": "body", "section": "High-level interfaces", "weight": 1.0} -->

With the workflow described above, it is possible to obtain a self-contained, high-per formance solver that can be easily deployed on embedded hardware starting from a description of the OCP in a high-level language.

<!-- chunk {"id": "body-0100", "role": "body", "section": "High-level interfaces", "weight": 1.0} -->

We remark that model equations and other nonlinear functions are called from acados in a completely language-agnostic way: acados is at no point aware of which modeling tool is being used. One benefit is that this facilitates self-written models (in C/C++), which are also completely compatible with acados. However, this is more involved, since in the case of CasADi functions, memory allocation and matrix format conversions are taken into account automatically by the CasADi functions wrapper in acados.

<!-- chunk {"id": "body-0101", "role": "body", "section": "Numerical Results", "weight": 1.0} -->

This section consists of a few numerical experiments with acadosand comparisons to other embedded optimization software packages. We discuss performance on the nonlinear chain-of-masses problem, we present one open-loop example with different Hessian approximations, and show one closed-loop engine control experiment on an embedded platform.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Case Study 1: Chain of Masses", "weight": 1.0} -->

As a benchmarking problem, we take the chain-of-masses problem as presented in [Wirsching2006]. The control objective is to stabilize a chain of masses with nonlinear interaction between them. For a full description of the system, we refer to the appendix. The system is useful as a benchmark in the sense that the problem is simple enough to understand intuitively, yet complicated enough to get non-trivial results from a range of different solvers. Also, by increasing the number of masses, one could compare behavior for different numbers of states easily, without changing much code.

<!-- chunk {"id": "body-0103", "role": "body", "section": "Closed-loop experiments", "weight": 1.0} -->

In closed-loop, an MPC controller repeatedly (approximately) solves OCP [eq:chain\_of\_masses\_ocp]. The first control $u_0$ is passed to the dynamic system under control and a new initial state $\overline{x}_0$ is obtained. Here, we simulate the system by using a more accurate integrator than the one in OCP[eq:chain\_of\_masses\_ocp], namely the Dormand-Prince method, as implemented in the \textsc{Matlab{}} routine ode45.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Closed-loop experiments", "weight": 1.0} -->

We introduce one disturbance into the closed-loop system, similar as in [Wirsching2006]: in the beginning of the simulation, we start from a horizontal configuration of the chain of masses. Around the midpoint of the simulation, we override the closed loop control with a constant $u_\mathrm{d} = ^\top$. After one second of simulation time, the controller takes over again.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Closed-loop experiments", "weight": 1.0} -->

We compare the following solvers with each other for this particular closed-loop setup: As a solver not targeting embedded devices specifically, we use it as a baseline to compare against. A projected gradient descent method tailored for NMPC. A gradient projection method for MPC that only allows linear inequality constraints. - ACADO Code Generation tool[Houska2011]. Generates SQP-based solvers. An embedded Augmented Lagrangian-based solver. Framework presented in the current paper.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Closed-loop experiments", "weight": 1.0} -->

The tuning parameters for the different solvers are listed in Table[tab:tuning\_parameters].

<!-- chunk {"id": "body-0107", "role": "body", "section": "Closed-loop experiments", "weight": 1.0} -->

Solver options for the different solvers in Case Study 1.

<!-- chunk {"id": "body-0108", "role": "body", "section": "Closed-loop experiments", "weight": 1.0} -->

| Solver | Solver options | In order to compare the quality of the closed-loop solutions, we use the notion of distance-from-reference (DR), which is an approximation of the integrated cost along closed-loop trajectories: $$\mathrm{DR}_{(\cdot), n} = \sum_{i=0}^{n} \begin{bmatrix}x_{(\cdot),i}-x_\mathrm{ref} \\ u_{(\cdot),i}-u_\mathrm{ref}\end{bmatrix}^\top \begin{bmatrix} Q & 0 \\ 0 & R \end{bmatrix} \begin{bmatrix}x_{(\cdot),i}-x_\mathrm{ref} \\ u_{(\cdot),i}-u_\mathrm{ref}\end{bmatrix}.$$ To compare the different solvers, we plot the relative cumulative sub-optimality (RCSO), relative to a fully converged solution, in this

<!-- chunk {"id": "body-0109", "role": "body", "section": "Closed-loop experiments", "weight": 1.0} -->

case, the IPOPT solution, which reads as $$\mathrm{RCSO}_{(\cdot),n} = \left|\frac{\mathrm{DR}_{(\cdot),n} - \mathrm{DR}_{\software{ipopt},n}}{\mathrm{DR}_{\software{ipopt},n}}\right|,$$ where $n = 0,\ldots, 300$ denotes the time step in our simulation.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Closed-loop experiments", "weight": 1.0} -->

We show a comparison in Table[tab:nlchainclosedloop]. The results for ACADO and acados are exactly the same, as they implement the same real-time algorithm, with both being very close to the reference solution from IPOPT. The solvers GRAMPC, VIATOC and FalcOPT, being based on first-order methods, are further away from the IPOPT solution. These findings are consistent with previously published work by other authors, see [Englert2019].

<!-- chunk {"id": "body-0111", "role": "body", "section": "Closed-loop experiments", "weight": 1.0} -->

Relative suboptimality at the end of the simulation of the hanging chain with $M=5$ and $N=40$. First-order methods VIATOC, GRAMPC and FalcOPT were tuned to perform similarly. The algorithms chosen in ACADO and acados are identical, hence the results are identical.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Closed-loop experiments", "weight": 1.0} -->

| Solver name | RCSO | We have a look at the computational performance along the closed-loop trajectories in Figure GRAMPC, ACADO, VIATOC and acados produce consistent timings throughout the entire experiment, even when the disturbance occurs. This is a beneficial property for embedded solvers, as they often have a fixed time deadline, being part of a larger control application. GRAMPC and acados produce solutions at almost the same speed, both approximately a factor 2 faster than ACADO which is in turn a factor 2-3 faster than VIATOC. Near the equilibrium, FalcOPT takes the shortest computation time, as it needs to perform only a few gradient steps per iteration. IPOPT is included as a baseline for comparison to non-embedded solvers. The timings are summarized in Table[tab:nlchaintimings].

<!-- chunk {"id": "body-0113", "role": "body", "section": "Closed-loop experiments", "weight": 1.0} -->

Computational time for each iteration of the closed loop simulation, averaged over 10 runs.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Closed-loop experiments", "weight": 1.0} -->

Computation times for the closed-loop experiments on a chain of masses (cf.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Closed-loop experiments", "weight": 1.0} -->

| comp. time per iteration $(\mathrm{ms})$ | median | minimum | maximum | Of course, any solver can trade off sub-optimality for computation time. To get the full picture, we plot both measures against each other in Figure [fig:nlchainparetofront]: we look at relative cumulative sub-optimality over the entire length of the experiment, versus worst-case computation times. By this comparison, we see that acados and GRAMPC are on the Pareto-optimal front: although acados is a factor 1000 less suboptimal than GRAMPC, the computational cost is higher. By the median computation times, acados is faster (see Table[tab:nlchaintimings]).

<!-- chunk {"id": "body-0116", "role": "body", "section": "Closed-loop experiments", "weight": 1.0} -->

Trade-off between sub-optimality (Tabletab:nlchainclosedloop) and computation time (Figurefig:nlchaintimings). We see that acados and GRAMPC lie on the Pareto-optimal front.

<!-- chunk {"id": "body-0117", "role": "body", "section": "Case study 2: Hessian regularization", "weight": 1.0} -->

[sec:embedded\_sqp], we briefly mentioned the impact of Hessian regularization on SQP methods. In this case study, we compare the convergence of exact-Hessian based SQP with three different Hessian regularizations, on a simple control problem, namely a cart-pole swingup, which is described in the appendix. Note that in this case study, as opposed to the others, we do not perform closed-loop experiments but solve one optimal control problem up until convergence.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Exact-Hessian based SQP", "weight": 1.0} -->

[eq:OCP\_pendulum] with SQP, where we use the exact Hessian of the Lagrangian. In the notation of[eq:OCP\_QP\_subproblem]: \end{bmatrix} + \sum_{i=0}^{n_x} \pi_{k,i} \nabla^2_{(x,u)} \phi^x_i(x_k, u_k), \quad k=0,\ldots,N-1 \\where $\pi_{k,i}$are the Lagrange multipliers associated with the dynamic equality constraints.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Exact-Hessian based SQP", "weight": 1.0} -->

In some cases, the non-convexity of the dynamic equations gives rise to an indefinite Hessian matrix. $\mathrm{project}(\cdot)$ and $\mathrm{mirror}(\cdot)$ regularizations, as well as the convexification method previously mentioned in Section[sec:convex\_hessians]. All are implemented as modules in the acadosframework.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Exact-Hessian based SQP", "weight": 1.0} -->

We compare the convergence of the SQP iterates obtained using the three different regularization methods. For each SQP variant, we start the SQP iterations from an initialization point with zeros for all states except a linearly decreasing initialization for the angle, from The result can be seen in Figure[fig:regularization\_convergence]. The structure-exploiting convexification converges almost twice as fast as the projection regularization, and is in turn much faster than the mirroring regularization. Intuitively, this makes sense, as mirroring is `blocking' directions associated with large negative eigenvalues, by introducing large positive eigenvalues in those directions. This prevents the solver from taking larger steps This is also the approach followed by the algorithms obtained with the ACADO Code Generation tool.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Exact-Hessian based SQP", "weight": 1.0} -->

In turn, the structure-exploiting regularization is faster than merely projecting the eigenvalues on the positive definite cone, because it is redistributing convexity among all stages, and thus needs less regularization overall.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Exact-Hessian based SQP", "weight": 1.0} -->

Convergence comparison of exact-Hessian based SQP with three different regularization strategies.

<!-- chunk {"id": "body-0123", "role": "body", "section": "Exact-Hessian based SQP", "weight": 1.0} -->

Exact-Hessian based SQP: computation times | regularization | convexification | project | mirror | It must be said that the convexification method is quite a bit more involved than the other two regularization schemes. However, by using the optimized linear algebra routines of BLASFEO, we implemented the convexification method such that it is only slightly more expensive per iteration than the basic regularization methods, see Table[tab:regularization\_timings], but much less computationally expensive overall. Thus, the Hessian convexification method allows us to perform exact-Hessian based NMPC online, with better performance than state-of-the-art methods.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Case study 3: Hardware-in-the-loop experiments for an engine control application", "weight": 1.0} -->

As a last case study, we discuss the performance of acados on an embedded platform, namely the dSPACE MicroAutoboxII[dspace2006]. It is an industrial computing platform that is used in the car industry. It features a 900 MHz PowerPC processor (IBM PPC 750GL) with 16MB of main memory. The control application that we focus on is engine control, with the engine model as presented in[Albin2017], which we will briefly reproduce in the appendix.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Case study 3: Hardware-in-the-loop experiments for an engine control application", "weight": 1.0} -->

The control objective is to track a boost pressure signal, where the boost pressure is given by $y_p(x):= \Pi_{c,\mathrm{lp}} \cdot \Pi_{c,\mathrm{hp}}$ (see appendix). To this end, we solve an OCP arising from a multiple shooting formulation with the Gauss-Legendre method of order 6 with sampling time $0.05 \, \mathrm{s}$ and $N=20$ shooting intervals. The DAE simulation functions are denoted by $\phi$. The OCP then reads as $\Pi_{c,\mathrm{lp}}, \Pi_{t,\mathrm{hp}}$are included to prevent damage to the compressor. The exact values of the weight matrices and the reference vectors can be found in the appendix.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Case study 3: Hardware-in-the-loop experiments for an engine control application", "weight": 1.0} -->

Closed-loop simulation of the engine control task with steps in the reference boost pressure. Simulations are carried out on the dSPACE MicroAutoboxII platform at a clock speed of $900\,\mathrm{MHz}$.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Case study 3: Hardware-in-the-loop experiments for an engine control application", "weight": 1.0} -->

We repeatedly solve OCP [eq:engine\_control] approximately by performing real time iterations. As an underlying QP solver, we useHPIPM. When ran in closed loop on the dSPACE MicroAutoboxII, the results can be seen in Figure[fig:enginetracking]. Control bounds and state bounds become active at some point in the simulation, for the high-pressure stage. The reference is tracked closely and without oscillations, which have been observed when linear-quadratic MPC is used[Albin2017]. As for the computation times, it is interesting to note that there are spikes everywhere where a jump occurs or a constraint becomes (in)active. The computation times close to the solution (i.e. at the beginning of the simulation) drop to almost zero. Overall, the maximum computation time remains under $10\,\mathrm{ms}$, which is 5x faster than the sampling time of the system ($50\,\mathrm{ms}$).

<!-- chunk {"id": "body-0128", "role": "body", "section": "Case study 3: Hardware-in-the-loop experiments for an engine control application", "weight": 1.0} -->

We remark that the computation times obtained with the dSPACE MicroAutoboxII, for this HIL experiment, are about three times slower than a desktop computer with a 2.5GHz Intel Core i7-4870HQ processor.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Conclusion and outlook", "weight": 1.5} -->

In this article, we presented acados, a new software package for embedded optimization. It is free and open-source software that facilitates rapid testing and deployment of (N)MPC algorithms on embedded hardware platforms. For ease of use, we offer interfaces with higher-level languages such as Matlab and Python.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Conclusion and outlook", "weight": 1.5} -->

Among many features that state-of-the-art NMPC algorithms require, a couple of new features that are not present in any other software package is the convexification procedure of Section [sec:convex\_hessians], allowing the use of exact-Hessian based SQP methods in real-time, and the SCQP Hessian approximation. Additionally, the structure exploiting GNSF-IRK integrator has the potential to speed up the simulation and sensitivity propagation tasks within an NMPC scheme. Furthermore, acados features partial condensing, different state and control dimensions per multiple shooting stage, the use of BLASFEO as a linear algebra backend and facilities for using CasADias a modeling language.

<!-- chunk {"id": "body-0131", "role": "body", "section": "Conclusion and outlook", "weight": 1.5} -->

The software is shown to be embeddable, by numerical experiments on the dSPACE MicroAutoboxII industrial computer, resulting in computation times in the millisecond range for a non-trivial NMPC problem. Furthermore, it is shown to be fast, by comparison to other embedded optimization packages. acados is an ongoing endeavor. Future work includes extending interoperability with Simulinkfor easier deployment on embedded systems, and adding features for nonlinear interior-point methods, as well as other SQP-based methods like multi-level iterations.
