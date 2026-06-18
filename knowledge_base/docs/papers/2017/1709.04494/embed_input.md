A Rewriting System for Convex Optimization Problems

Topics include Convex optimization, Optimization, Optimization problem.

We describe a modular rewriting system for translating optimization problems written in a domain-specific language to forms compatible with low-level solver interfaces. Translation is facilitated by reductions, which accept a category of problems and transform instances of that category to equivalent instances of another category. Our system proceeds in two key phases: analysis, in which we attempt to find a suitable solver for a supplied problem, and canonicalization, in which we rewrite the problem in the selected solver's standard form. We implement the described system in version 1.0 of CVXPY, a domain-specific language for mathematical and especially convex optimization. By treating reductions as first-class objects, our method makes it easy to match problems to solvers well-suited for them and to support solvers with a wide variety of standard forms.

## Introduction

Mathematical optimization centers on the optimization problem. Every optimization problem has three attributes: a variable whose value is to be assigned, constraints that the variable must satisfy, and a real-valued objective function that measures the displeasure or cost incurred by any particular assignment to the variable. To solve an optimization problem is to find a numerical assignment to the variable that minimizes the objective function among all choices that satisfy the constraints.

Unfortunately, most optimization problems cannot be solved efficiently (Boyd \\BBA Vandenberghe, \\APACyear2004, §1.4). There are, however, classes of optimization problems that can be solved in polynomial time. An important such class contains convex optimization problems --- problems where the objective function is convex and where the constraints are described by a set of equality constraints with affine functions and inequality constraints with convex functions (Nesterov \\BBA Nemirovski, \\APACyear1994; Boyd \\BBA Vandenberghe, \\APACyear2004).

All problem rewriting is facilitated by Reduction objects, and every reduction implements three methods: accepts, apply, and retrieve. The accepts method takes as input a problem and returns a boolean indicating whether or not the reduction can be applied to the problem, the apply method takes as input a problem and returns a new equivalent problem, and the retrieve method takes a solution for the problem returned by an invocation of apply and retrieves from it a solution for its problem of provenance....

Creating expressions and constraints in CVXPY invokes behind-the-scenes a front end that parses them into expression trees; this functionality is not new (see Diamond \\BBA Boyd, \\APACyear2016\\APACexlab\\BCnt1). What is new is the method by which solvers are chosen for problems and the methods by which problems are canonicalized to their standard forms. In CVXPY 1.0, invoking the solve method of a problem triggers an analyzer, phase two of our rewriting system....

In this section, we present some simple but useful reductions.\

Every rewriting must yield an equivalent problem that is target-compatible.

Eliminating fixed variables. Any variable that is constrained to be a constant is called a fixed variable; replacing every occurrence of it with the value of the constant yields an equivalent...
