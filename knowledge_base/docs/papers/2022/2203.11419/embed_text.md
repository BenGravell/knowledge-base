## Introduction

Convex optimization is used in many domains, including signal and image processing, control, and finance, to mention just a few. A (parametrized) convex optimization problem can be written as where $x \in \mathbf{R}^{n}$ is the optimization variable, $f_{0}$ is the objective function to be minimized, $f_{1},\ldots,f_{p}$ are the inequality constraint functions, and ${g_{1}\ldots},g_{r}$ are the equality constraint functions. We require that $f_{0},\ldots,f_{p}$ are convex functions, and $g_{1},\ldots,g_{r}$ are affine functions. The parameter $\theta \in \mathbf{R}^{d}$ specifies data that can change, but is constant and given when we solve an instance of the problem. We refer to the parametrized problem as a *problem family*; when we specify a fixed value of $\theta$, we refer to it as a *problem instance*. We let $x^{\star}$ denote an optimal point for the problem, assuming it exists.

The problem family can be specified using a domain-specific language (DSL) for convex optimization. Such systems allow the user to specify the functions $f_{i}$ and $g_{j}$ in a simple format that closely follows the mathematical description of the problem. Examples include YALMIP and CVX (in Matlab), CVXPY (in Python), Convex.jl and JuMP (in Julia), and CVXR (in R). We focus on CVXPY, which also supports the declaration of parameters, enabling it to specify problem families, not just problem instances.

DSLs parse the problem description and translate (or canonicalize) it to an equivalent problem that is suitable for a solver that handles some generic class of problems, such as linear programs (LPs), quadratic programs (QPs), second-order cone programs (SOCPs), semidefinite programs (SDPs), and others such as exponential cone programs. We focus on solvers that are suitable for embedded applications, *i.e.*, are single-threaded, can be statically compiled, and do not make system calls: OSQP handles QPs, SCS and ECOS handle cone programs that include SOCPs. After the canonicalized problem is solved, a solution of the original problem is retrieved from a solution of the canonicalized problem.

It is useful to think of the whole process as a function that maps $\theta$, the parameter that specifies the problem instance, into $x^{\star}$, an optimal value of the variable. With a DSL, this process consists of three steps. First the original problem description is canonicalized to a problem in some standard (or canonical) form; then the canonicalized problem is solved using a solver; and finally, a solution of the original problem is retrieved from a solution of the canonicalized problem.

(a) Parser-solver calculating solution x⋆ for problem instance with parameter θ.

(b) Source code generation for problem family, followed by compilation to custom solver. The compiled solver computes a solution x⋆ to the problem instance with parameter θ.

Figure 1: Comparison of convex optimization problem parsing and solving approaches.

Most of these DSLs are organized as *parser-solvers*, which carry out the canonicalization each time the problem is solved (with different parameter values). This simple setting is illustrated in figure 1(a). We are interested in applications where we solve many instances of the problem, possibly in an embedded application with hard real-time constraints. For such applications, a *code generator* makes more sense. A code generator takes as input a description of a problem family, and generates specialized solver source code for that specific family. That source code is then compiled, and we have an efficient solver for the specific family.

This workflow is illustrated in figure 1(b). The compiled solver has a number of advantages over parser-solvers. First, the compiled solver can be deployed in embedded systems, fulfilling rules for safety-critical code. Second, by caching canonicalization and exploiting the problem structure, the compiled solver is faster.

A well known code generator is CVXGEN. It handles problems that can be transformed to QPs and includes a custom interior-point solver. CVXGEN is used in many applications, including autonomous driving, dynamic energy management, and real-time trading in finance. SpaceX uses CVXGEN to generate flight code for high-speed onboard convex optimization for precision landing of space rockets.

CVXGEN was designed for use in real-time control systems, where the problems solved are not too big, either in terms of the number of variables or number of parameters. CVXGEN unrolls for-loops in its generated source code files to increase the solving speed, but this can also result in large compiled code size. Due to the flat and explicit code generated, CVXGEN only handles problems with up to around a few thousand parameters. (More accurately, CVXGEN is limited to 4000 nonzero entries in the linear system of equations solved in each iteration.)

### I-A Contribution

In this paper, we introduce the code generation tool CVXPYgen, which produces custom C code to solve a parametrized family of convex optimization problems. The design decisions for CVXPYgen are somewhat different from those made for CVXGEN. First, CVXPYgen is built on top of the DSL CVXPY, whereas CVXGEN is entirely self-contained. This means that prototypes can be developed, prototyped, and simulated in Python using CVXPY. Second, CVXPYgen interfaces with multiple solvers, currently OSQP, SCS, and ECOS. This means that CVXPYgen supports problems more general than those that can be transformed to QPs. As far as we know, CVXPYgen is the first generic code generator for convex optimization that supports SOCPs. When using OSQP or SCS (both based on first-order methods), the generated solvers support warm-starting, which can bring more speed in some applications. Third, CVXPYgen does not aggressively unroll loops in the generated code, which allows it to support high-dimensional parameters. In addition, matrix parameters can have any user-defined sparsity pattern. CVXPYgen uses partial update canonicalization, in which only the parameters changed are processed when solving a new problem instance. Fourth, CVXPYgen and its generated solvers are fully open-source, whereas CVXGEN is proprietary.

CVXPYgen (and more generally, code generation) is useful for two families of practical applications. The first is solving convex optimization problems in real-time settings on embedded devices, as is done in control systems, real-time resource allocators, and other applications. The second is in solving a large number of instances of a problem family, possibly on general-purpose computers. One example is back-testing in finance, where a trading policy based on convex optimization is simulated on historical or simulated data over many periods. Typical back-tests involve solving thousands or more instances of a problem family. In these applications, there is no hard real-time constraint; the goal is simply to speed up solving by avoiding repeatedly canonicalizing the problem.

### I-B Prior work

Several other code generators for optimization have been developed in addition to CVXGEN. FORCESPRO and FORCES NLP are proprietary code generators for multi-stage control problems. They handle problems that can be transformed to multi-stage quadratically constrained quadratic programs and nonlinear programs, respectively. The open-source code generators QCML and CVXPY-CODEGEN, which interface with ECOS, were developed before CVXPY included support for parameters. These early prototypes are no longer actively supported or maintained.

### I-C Outline

The remainder of this paper is structured as follows. In §II we describe, at a high level, how CVXPYgen works, and in §III, we illustrate how it is used with a simple example. In §IV and §V we compare CVXPYgen to CVXGEN (for embedded use) and CVXPY (for general purpose use), respectively. We conclude the paper in §VI.

## CVXPYgen

CVXPYgen is based on the open-source Python-embedded DSL CVXPY. CVXPY handles many types of conic programs and certain types of nonconvex problems, whereas we focus on LPs, QPs, and SOCPs for code generation. CVXPY provides modeling instructions that follow the mathematical description for convex optimization problems. It ensures that the modeled problems are convex, using disciplined convex programming (DCP). DCP is the process of constructing convex functions by assembling given base functions in mathematical expressions using a simple set of rules. DCP ensures that the resulting problem is convex, and also, readily canonicalized to a standard form.

In DCP, parameters are treated as constants, optionally with specified sign, and there are no restrictions about how these constants appear in the expressions defining the problem family. The recently developed concept of disciplined parametrized programming (DPP) puts additional restrictions on how parameters can enter a problem description. If a problem family description is DPP-compliant, then canonicalization and retrieval can be represented as *affine* mappings. Thus DPP-compliant problems are reducible to ASA-form, which stands for *Affine-Solve-Affine*. This is the key property we exploit in CVXPYgen. More about the DCP and DPP rules can be found in the aforementioned papers, or at After CVXPY has reduced the DPP-compliant problem to ASA-form, CVXPYgen extracts a sparse matrix $C$ that canonicalizes the user-defined parameters $\theta$ to the parameters $\overset{\sim}{\theta}$ appearing in the standard form solver: CVXPYgen analyzes $C$ to determine the user-defined parameters (*i.e.*, components of $\theta$) that every standardized form parameter depends. This information is used when generating the custom solver, where only slices of the above mapping are computed if not all user-defined parameters are updated between solves. In addition, it is very useful to know the set of updated canonical parameters when using the OSQP solver or SCS, as detailed below.

In a similar way the retrieval of the solution $x^{\star}$ for the original problem from a solution ${\overset{\sim}{x}}^{\star}$ of the canonicalized problem is an affine mapping, where $R$ is a sparse matrix. Typically $R$ is a selector matrix, with only one nonzero entry in each row, equal to one, in which case this step can be handled via simple pointers in C.

CVXPYgen generates allocation-, library-, and division-free C code for the canonicalization and retrieval steps, which in essence are nothing more than sparse matrix-vector multiplication, with some logic that exploits pointers or partial updates. Sparse matrices are stored in compressed sparse column format and dense matrices are stored as vectors via column-major flattening.

Any solver can be used to solve the canonicalized problem, which provides the final link: where $\mathcal{S}$ denotes the mapping from the canonicalized parameters to a solution of the canonicalized problem. (We assume here that the problem instance is feasible, and that when there are multiple solutions, we simply pick one.) If available, CVXPYgen uses the canonical solver's code generation method to produce C code for canonical solving. As of now, only OSQP provides this functionality. Otherwise, the solver's C code is simply copied, possibly modified for use in embedded applications.

OSQP and SCS provide a set of C functions for updating their parameters. This way, when only canonical vector parameters are updated, the factorization of the linear system involved in the OSQP or SCS algorithms can be cached and re-used, which can lead to substantial speed up and division-free code. In the same way as only the parts of $\overset{\sim}{\theta}$ are re-canonicalized that depend on the updated parts of $\theta$, only the OSQP or SCS update functions associated with these parameters are called before the canonicalized problem is solved.

The code and the full documentation for CVXPYgen with its generated solvers are available at

## Simple example

We consider the nonnegative least squares problem where $x \in \mathbf{R}^{n}$ is the variable and $G \in \mathbf{R}^{m \times n}$, $h \in \mathbf{R}^{m}$ are parameters, so $\theta = {(G,h)}$. We will canonicalize this to the standard form accepted by OSQP, where $\overset{\sim}{x} \in \mathbf{R}^{\overset{\sim}{n}}$ is the canonical variable and all other symbols are canonical parameters, *i.e.*, $\overset{\sim}{\theta} = {(P,q,A,l,u)}$. (In this form, entries of $l$ can be $- \infty$, and entries of $u$ can be $+ \infty$.)

The naïve canonicalization of to takes $\overset{\sim}{x} = x$ and In this canonicalization, $\overset{\sim}{\theta}$ is not an affine function of $\theta$, since some entries of $\overset{\sim}{\theta}$ are products of entries of $\theta$.

The canonicalization that uses DPP first expresses problem as with variable $\overset{\sim}{x} = {({\overset{\sim}{x}}_{1},{\overset{\sim}{x}}_{2})}$, where ${\overset{\sim}{x}}_{1} = x$ and ${\overset{\sim}{x}}_{2} \in \mathbf{R}^{m}$. We can express this as with parameters where the second part of $u$ has $\infty$ in every entry, *i.e.*, there is no upper bound on the second part of $A\overset{\sim}{x}$. In this canonicalization, $\overset{\sim}{\theta}$ is indeed an affine function of $\theta$. The retrieval map has the simple (linear) form $x^{\star} = {{\lbrack{I0}\rbrack}{\overset{\sim}{x}}^{\star}}$.

2from cvxpygen import cpg 8p=cp.Problem(cp.Minimize(cp.sum_squares(G@x-h)), 11cpg.generate_code(p) Figure 2: Code generation for example. We assume that the dimensions m and n have been previously defined.

We generate code for this problem as shown in figure 2. The problem is modeled with CVXPY in lines 5--9. The actual code generation is done in line 11. The variable and parameters are named in lines 5--7 via their name attributes. These names are used for C variable and function naming.

## Comparison to CVXGEN

We compare CVXPYgen to CVXGEN for a model predictive control (MPC) problem family, described in Appendix A. In particular, we compare solve times of the C interface and executable sizes. The MPC problems are parametrized by their horizon length $H \in \left\{ 6,12,18,30,60 \right\}$; the number of variables is around $10H$. Figure 3 shows the resulting solve times averaged over 100 simulation steps. CVXGEN is not able to generate code for $H > 18$. Together with the automatically chosen OSQP solver, CVXPYgen outperforms CVXGEN for all problem sizes.

Figure 3: Comparison of solve times (top) and binary sizes (bottom) with CVXGEN (magenta) and CVXPYgen (blue) used for code generation.

The bottom of figure 3 presents the example executable sizes for CVXGEN and CVXPYgen, respectively. For all values of $H$, the executables corresponding to CVXPYgen are considerably smaller.

The execution times cited above are on a MacBook Pro 2.3GHz Intel i5. We have also used these generated solvers to control the position of a custom-built 14-by-14 cm quadcopter. The generated code was compiled in a robot operating system (ROS) node, and run on the drone's Intel Atom x5-Z8350 processor, at 30 Hz. We provide a video of the quadcopter following a circle trajectory at

## Comparison to CVXPY

Here we compare CVXPYgen to CVXPY, for a (financial) portfolio optimization problem family, described in Appendix B. This family of problems is parametrized by the number of assets in the portfolio $N \in {\{ 10,20,40,60,100\}}$. The number of variables in these problems is around $2N$. Figure 4 gives the results for 500 solves, a two year back-test using historical data. We see that the average solver speed is about 6 times faster with CVXPYgen, for $N = 10$, with the ratio dropping to 2.5 for $N = 100$. The execution times are measured on the same MacBook described in the previous section.

Figure 4: Comparison of solve times with CVXPY (magenta) and the CVXPY interface of CVXPYgen (blue).

An interesting metric is the break-even point, which is the number of instances that need to be solved before CVXPYgen is faster than CVXPY, when we include the code generation and compilation time. This number is around 5000, and not too dependent on $N$. A typical back-test might involve daily trading, with around 250 trading days in each year, over 4 years, with hundreds of different hyper-parameter values, which gives on the order of 100,000 solves, well above this break-even point.

## Conclusion

We have described CVXPYgen, a tool for generating custom C code that solves instances of a family of convex optimization problems specified within CVXPY. This gives a seemless path from prototyping an application using Python and CVXPY, to a final embedded implementation in C. In addition to CVXPYgen supporting a wider variety of problems (such as SOCPs) than the state-of-the-art code generator CVXGEN, numerical experiments show that it outperforms CVXGEN in terms of allowable problem size, compiled code size, and solve times. For applications running on general purpose machines, we obtain a significant speedup over CVXPY when many problem instances are to be solved.
