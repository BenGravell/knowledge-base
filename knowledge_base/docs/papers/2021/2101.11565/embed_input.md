Shortest Paths in Graphs of Convex Sets

Topics include Graphs of convex sets, Graph search, Convex, Convex set, Convex optimization, Mixed-integer programming, Motion planning, Optimal control, Trajectory optimization.

Each graph vertex is associated with a convex set and edge lengths are convex functions of the endpoints' positions. The key contribution is a strong mixed-integer convex program (MICP) formulation based on perspective operators that yields a tight relaxation, enabling globally optimal paths in large graphs and high-dimensional spaces. Forms the theoretical foundation for GCS-based motion planning.

Given a graph, the shortest-path problem requires finding a sequence of edges with minimum cumulative length that connects a source vertex to a target vertex. We consider a variant of this classical problem in which the position of each vertex in the graph is a continuous decision variable constrained in a convex set, and the length of an edge is a convex function of the position of its endpoints. Problems of this form arise naturally in many areas, from motion planning of autonomous vehicles to optimal control of hybrid systems. The price for such a wide applicability is the complexity of this problem, which is easily seen to be NP-hard. Our main contribution is a strong and lightweight mixed-integer convex formulation based on perspective operators, that makes it possible to efficiently find globally optimal paths in large graphs and in high-dimensional spaces.

## Introduction

The Shortest-Path Problem (SPP) is one of the most important and ubiquitous problems in combinatorial optimization. In its single-source single-target version, this problem asks for a path of minimum length connecting two prescribed vertices of a graph, where the length of a path is defined as the sum of the lengths of its edges. Typically, the edge lengths are fixed scalars, given as problem data, and the assumptions made on their values have a dramatic impact on the problem complexity \[43, Chapters 6 to 8\].

Many problems of practical interest can be formulated as SPPs in GCS: for some of those the convex sets and the edge-length functions are naturally suggested by the application, for others the construction of the GCS requires more thinking. As an example of the former class of problems, scheduling the flight of a drone with limited batteries is immediately cast as an SPP in GCS like the one in Figure 1. The start region is on the left, the goal region is on the right, and the remaining regions can be used for recharging. Pairs of regions that are close enough for the drone to fly between are connected by an edge.

## Contributions

The following are the main contributions of this article.

## Problem statement (Section 2)

The SPP in GCS represents an unexplored class of problems at the interface of combinatorial and convex optimization. It lends itself to a simple problem statement and, at the same time, it is a versatile framework that includes as special cases many problems of practical relevance.
