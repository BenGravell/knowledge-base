Embedded Code Generation with CVXPY

Topics include Convex optimization, Optimization, Control, CVXPYgen, Code generation, Domain-specific language.

We introduce CVXPYgen, a tool for generating custom C code, suitable for embedded applications, that solves a parametrized class of convex optimization problems. CVXPYgen is based on CVXPY, a Python-embedded domain-specific language that supports a natural syntax (that follows the mathematical description) for specifying convex optimization problems. Along with the C implementation of a custom solver, CVXPYgen creates a Python wrapper for prototyping and desktop (non-embedded) applications. We give two examples, position control of a quadcopter and back-testing a portfolio optimization model. CVXPYgen outperforms a state-of-the-art code generation tool in terms of problem size it can handle, binary code size, and solve times. CVXPYgen and the generated solvers are open-source.

## Introduction

Convex optimization is used in many domains, including signal and image processing, control, and finance, to mention just a few. A (parametrized) convex optimization problem can be written as

where $x \in \mathbf{R}^{n}$ is the optimization variable, $f_{0}$ is the objective function to be minimized, $f_{1},\ldots,f_{p}$ are the inequality constraint functions, and ${g_{1}\ldots},g_{r}$ are the equality constraint functions. We require that $f_{0},\ldots,f_{p}$ are convex functions, and $g_{1},\ldots,g_{r}$ are affine functions. The parameter $\theta \in \mathbf{R}^{d}$ specifies data that can change, but is constant and given when we solve an instance of the problem. We refer to the parametrized problem as a *problem family*; when we specify a fixed value of $\theta$, we refer to it as a *problem instance*....

## Conclusion

We have described CVXPYgen, a tool for generating custom C code that solves instances of a family of convex optimization problems specified within CVXPY. This gives a seemless path from prototyping an application using Python and CVXPY, to a final embedded implementation in C. In addition to CVXPYgen supporting a wider variety of problems (such as SOCPs) than the state-of-the-art code generator CVXGEN, numerical experiments show that it outperforms CVXGEN in terms of allowable problem size, compiled code size, and solve times....

where $R$ is a sparse matrix. Typically $R$ is a selector matrix, with only one nonzero entry in each row, equal to one, in which case this step can be handled via simple pointers in C.

Several other code generators for optimization have been developed in addition to CVXGEN. FORCESPRO and FORCES NLP are proprietary code generators for multi-stage control problems. They handle problems that can be transformed to multi-stage quadratically constrained quadratic programs and nonlinear programs, respectively. The open-source code generators QCML and CVXPY-CODEGEN, which interface with ECOS, were developed before CVXPY included support for parameters. These early prototypes are no longer actively supported or maintained.

where $\overset{\sim}{x} \in \mathbf{R}^{\overset{\sim}{n}}$ is the canonical variable and all other symbols are canonical parameters, *i.e.*, $\overset{\sim}{\theta} = {(P,q,A,l,u)}$. (In this form, entries of $l$ can be $- \infty$, and entries of $u$ can be $+ \infty$.)
