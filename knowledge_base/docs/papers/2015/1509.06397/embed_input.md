SnapVX: A Network-Based Convex Optimization Solver

SnapVX is a high-performance Python solver for convex optimization problems defined on networks. For these problems, it provides a fast and scalable solution with guaranteed global convergence. SnapVX combines the capabilities of two open source software packages: Snap.py and CVXPY. Snap.py is a large scale graph processing library, and CVXPY provides a general modeling framework for small-scale subproblems. SnapVX offers a customizable yet easy-to-use interface with out-of-the-box functionality. Based on the Alternating Direction Method of Multipliers (ADMM), it is able to efficiently store, analyze, and solve large optimization problems from a variety of different applications. Documentation, examples, and more can be found on the SnapVX website at

## Introduction

Convex optimization is a widely used approach of modeling and solving problems in many different fields, as it offers well-established methods for finding globally optimal solutions. Numerous general-purpose optimization software packages exist, but they typically rely on algorithms that are difficult to scale, so many modern machine learning problems cannot be solved by these common, yet general, approaches. Instead, solving large scale examples often requires developing problem-specific solution methods, which can be very fast but require significant optimization expertise to build.

In this paper, we build on the observation that many large convex optimization examples follow a common form in that they can often be split up into a series of subproblems using a network (graph) structure. Nodes are subproblems, representing anything from timestamps in a time-series data set to users in a social network. The edges then define the coupling, or relationships between the different nodes, and the combination of nodes and edges yields the original convex optimization problem.

Here, we present SnapVX, a solver that is both scalable and general on optimization problems defined over networks. It combines the graph capabilities of Snap.py with the general modeling framework from CVXPY. We show how SnapVX works, present syntax and supported features, scale it to large problems, and describe how it can be used to solve convex optimization problems from a variety of different fields.

## SnapVX General Form

Consider
