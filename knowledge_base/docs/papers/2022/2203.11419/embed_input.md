Embedded Code Generation with CVXPY

Topics include Convex optimization, Optimization, Control, CVXPYgen, Code generation, Domain-specific language.

We introduce CVXPYgen, a tool for generating custom C code, suitable for embedded applications, that solves a parametrized class of convex optimization problems. CVXPYgen is based on CVXPY, a Python-embedded domain-specific language that supports a natural syntax (that follows the mathematical description) for specifying convex optimization problems. Along with the C implementation of a custom solver, CVXPYgen creates a Python wrapper for prototyping and desktop (non-embedded) applications. We give two examples, position control of a quadcopter and back-testing a portfolio optimization model. CVXPYgen outperforms a state-of-the-art code generation tool in terms of problem size it can handle, binary code size, and solve times. CVXPYgen and the generated solvers are open-source.

## Introduction

Convex optimization is used in many domains, including signal and image processing, control, and finance, to mention just a few. A (parametrized) convex optimization problem can be written as

where $x \in \mathbf{R}^{n}$ is the optimization variable, $f_{0}$ is the objective function to be minimized, $f_{1},\ldots,f_{p}$ are the inequality constraint functions, and ${g_{1}\ldots},g_{r}$ are the equality constraint functions. We require that $f_{0},\ldots,f_{p}$ are convex functions, and $g_{1},\ldots,g_{r}$ are affine functions. The parameter $\theta \in \mathbf{R}^{d}$ specifies data that can change, but is constant and given when we solve an instance of the problem. We refer to the parametrized problem as a *problem family*; when we specify a fixed value of $\theta$, we refer to it as a *problem instance*.

The problem family can be specified using a domain-specific language (DSL) for convex optimization. Such systems allow the user to specify the functions $f_{i}$ and $g_{j}$ in a simple format that closely follows the mathematical description of the problem. Examples include YALMIP and CVX (in Matlab), CVXPY (in Python), Convex.jl and JuMP (in Julia), and CVXR (in R). We focus on CVXPY, which also supports the declaration of parameters, enabling it to specify problem families, not just problem instances.

## Conclusion

We have described CVXPYgen, a tool for generating custom C code that solves instances of a family of convex optimization problems specified within CVXPY. This gives a seemless path from prototyping an application using Python and CVXPY, to a final embedded implementation in C. In addition to CVXPYgen supporting a wider variety of problems (such as SOCPs) than the state-of-the-art code generator CVXGEN, numerical experiments show that it outperforms CVXGEN in terms of allowable problem size, compiled code size, and solve times.
