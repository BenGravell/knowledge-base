CVXPY: A Python-Embedded Modeling Language for Convex Optimization

Topics include Convex optimization, Optimization, CVXPY.

CVXPY is a domain-specific language for convex optimization embedded in Python. It allows the user to express convex optimization problems in a natural syntax that follows the math, rather than in the restrictive standard form required by solvers. CVXPY makes it easy to combine convex optimization with high-level features of Python such as parallelism and object-oriented design. CVXPY is available at under the GPL license, along with documentation and examples.

## Introduction

Convex optimization has many applications to fields as diverse as machine learning, control, finance, and signal and image processing. Using convex optimization in an application requires either developing a custom solver or converting the problem into a standard form. Both of these tasks require expertise, and are time-consuming and error prone. An alternative is to use a domain-specific language (DSL) for convex optimization, which allows the user to specify the problem in a natural way that follows the math; this specification is then automatically converted into the standard form required by generic solvers.

CVXPY is a new DSL for convex optimization. It is based on CVX, but introduces new features such as signed disciplined convex programming analysis and parameters. CVXPY is an ordinary Python library, which makes it easy to combine convex optimization with high-level features of Python such as parallelism and object-oriented design.

CVXPY has been downloaded by thousands of users and used to teach multiple courses. Many tools have been built on top of CVXPY, such as an extension for stochastic optimization.

## CVXPY Syntax

CVXPY has a simple, readable syntax inspired by CVX. The following code constructs and solves a least squares problem where the variable's entries are constrained to be between 0 and 1. The problem data $A \in \text{R}^{m \times n}$ and $b \in \text{R}^{m}$ could be encoded as NumPy ndarrays or one of several other common matrix representations in Python.
