CVXPY: A Python-Embedded Modeling Language for Convex Optimization

Topics include Convex optimization, Optimization, CVXPY.

CVXPY is a domain-specific language for convex optimization embedded in Python. It allows the user to express convex optimization problems in a natural syntax that follows the math, rather than in the restrictive standard form required by solvers. CVXPY makes it easy to combine convex optimization with high-level features of Python such as parallelism and object-oriented design. CVXPY is available at under the GPL license, along with documentation and examples.

## Introduction

Convex optimization has many applications to fields as diverse as machine learning, control, finance, and signal and image processing. Using convex optimization in an application requires either developing a custom solver or converting the problem into a standard form. Both of these tasks require expertise, and are time-consuming and error prone. An alternative is to use a domain-specific language (DSL) for convex optimization, which allows the user to specify the problem in a natural way that follows the math; this specification is then automatically converted into the standard form required by generic solvers....

CVXPY is a new DSL for convex optimization. It is based on CVX, but introduces new features such as signed disciplined convex programming analysis and parameters. CVXPY is an ordinary Python library, which makes it easy to combine convex optimization with high-level features of Python such as parallelism and object-oriented design.

The vertex and edge objects are composed into a graph using the edges' `connect` method. To construct the single commodity flow problem, we sum the vertices and edges' local problems. (Addition of problems is overloaded in CVXPY to add the objectives together and concatenate the constraints.)

prob = sum([object.prob for object in vertices + edges])
prob.solve # Solve the single commodity flow problem.

Another improvement in CVXPY is the introduction of parameters. Parameters are constants whose symbolic properties (e.g., dimensions and sign) are fixed but whose numeric value can change. A problem involving parameters can be solved repeatedly for different values of the parameters without redoing computations that do not depend on the parameter values. Parameters are an old idea in DSLs for optimization, appearing in AMPL.

Solvers that handle conic form are known as cone solvers; each one can handle combinations of several types of cones. CVXPY interfaces with the open-source cone solvers CVXOPT, ECOS, and SCS, which are implemented in combinations of Python and C. These solvers have different characteristics, such as the types of cones they can handle and the type of algorithms employed....
