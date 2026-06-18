Shortest Paths in Graphs of Convex Sets

Topics include Graphs of convex sets, Graph search, Convex, Convex set, Convex optimization, Mixed-integer programming, Motion planning, Optimal control, Trajectory optimization.

Each graph vertex is associated with a convex set and edge lengths are convex functions of the endpoints' positions. The key contribution is a strong mixed-integer convex program (MICP) formulation based on perspective operators that yields a tight relaxation, enabling globally optimal paths in large graphs and high-dimensional spaces. Forms the theoretical foundation for GCS-based motion planning.

Given a graph, the shortest-path problem requires finding a sequence of edges with minimum cumulative length that connects a source vertex to a target vertex. We consider a variant of this classical problem in which the position of each vertex in the graph is a continuous decision variable constrained in a convex set, and the length of an edge is a convex function of the position of its endpoints. Problems of this form arise naturally in many areas, from motion planning of autonomous vehicles to optimal control of hybrid systems. The price for such a wide applicability is the complexity of this problem, which is easily seen to be NP-hard. Our main contribution is a strong and lightweight mixed-integer convex formulation based on perspective operators, that makes it possible to efficiently find globally optimal paths in large graphs and in high-dimensional spaces.

## Introduction

Figure 1: Example of an SPP in GCS. The source set is on the left and the target set is on the right. The graph edges are arrows, and the shortest path is shown in dashed green. The dotted red lines connect the optimal positions of the vertices along the shortest path.

The Shortest-Path Problem (SPP) is one of the most important and ubiquitous problems in combinatorial optimization. In its single-source single-target version, this problem asks for a path of minimum length connecting two prescribed vertices of a graph, where the length of a path is defined as the sum of the lengths of its edges. Typically, the edge lengths are fixed scalars, given as problem data, and the assumptions made on their values have a dramatic impact on the problem complexity \[43, Chapters 6 to 8\]....

## Conclusions

In this paper we have introduced the SPP in GCS, a versatile generalization of the classical SPP. Our main contribution is a compact MICP formulation for the solution of this NP-hard problem. Numerical experiments show that the convex relaxation of our formulation is typically very tight, and it enables us to quickly solve large problems to global optimality. We have demonstrated the applicability of the proposed framework to control systems: many optimal control problems are interpretable as SPPs in GCS and, in our tests, the proposed formulation outperforms state-of-the-art techniques for their solution.

Constraint (5.3) is obtained as in Remark 5.7 from the flow conservation in (4c), and (5.3) is the result of applying Lemma 5.5 to the nonnegativity constraint (4d). Note that the application of the same technique to the equalities (5.3) and to the degree constraint in (4c) would give us

The cone $\mathcal{X}^{\circ}$ is easily seen to be closed and convex, even when $\mathcal{X}$ is neither closed nor convex. Note also that the cone of valid inequalities is closely related to the *polar set*, but the latter lives in $n$ dimensions.

Ideally, we would like our relaxation to be as tight as possible, and the set $\mathcal{S}^{\prime}$ to coincide with the convex hull of $\mathcal{S}$. This equality holds, for example, when $\mathcal{X}$ and $\mathcal{Y}$ are intervals on the real line, in which case $\mathcal{S}^{\prime}$ simplifies to the McCormick envelope....
