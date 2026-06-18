A Rewriting System for Convex Optimization Problems

Topics include Convex optimization, Optimization, Optimization problem.

We describe a modular rewriting system for translating optimization problems written in a domain-specific language to forms compatible with low-level solver interfaces. Translation is facilitated by reductions, which accept a category of problems and transform instances of that category to equivalent instances of another category. Our system proceeds in two key phases: analysis, in which we attempt to find a suitable solver for a supplied problem, and canonicalization, in which we rewrite the problem in the selected solver's standard form. We implement the described system in version 1.0 of CVXPY, a domain-specific language for mathematical and especially convex optimization. By treating reductions as first-class objects, our method makes it easy to match problems to solvers well-suited for them and to support solvers with a wide variety of standard forms.

## Introduction

Mathematical optimization centers on the optimization problem. Every optimization problem has three attributes: a variable whose value is to be assigned, constraints that the variable must satisfy, and a real-valued objective function that measures the displeasure or cost incurred by any particular assignment to the variable. To solve an optimization problem is to find a numerical assignment to the variable that minimizes the objective function among all choices that satisfy the constraints.

Unfortunately, most optimization problems cannot be solved efficiently (Boyd \\BBA Vandenberghe, \\APACyear2004, §1.4). There are, however, classes of optimization problems that can be solved in polynomial time. An important such class contains convex optimization problems --- problems where the objective function is convex and where the constraints are described by a set of equality constraints with affine functions and inequality constraints with convex functions (Nesterov \\BBA Nemirovski, \\APACyear1994; Boyd \\BBA Vandenberghe, \\APACyear2004).

Modern convex optimization has its origin in linear programming, which traces back to the late 1940s, after the Second World War (Dantzig, \\APACyear1963, §2). Since then, convex optimization has been extended to include a much wider variety of problems, and has found application in machine learning (Hastie \\BOthers., \\APACyear2009), control (Boyd \\BOthers., \\APACyear1994), and computer science (Bertsekas, \\APACyear1991; Goemans \\BBA Williamson, \\APACyear1995; Parrilo, \\APACyear2003), to name just a few of the fields touched by it.

## Domain-specific languages

A domain-specific language (DSL) is a language that is designed for a particular application domain (Mernik \\BOthers., \\APACyear2005); familiar examples include MATLAB and SQL. DSLs for convex optimization are languages designed for specifying convex optimization problems in natural, human-readable forms, and they obtain solutions to problems on their users' behalf by invoking numerical solvers; popular ones include Yalmip (Löfberg, \\APACyear2004), CVX (Grant \\BBA Boyd, \\APACyear2014), Convex.jl (Udell \\BOthers., \\APACyear2014), and CVXPY (Diamond \\BBA Boyd, \\APACyear2016\\APACexlab\\BCnt1).
