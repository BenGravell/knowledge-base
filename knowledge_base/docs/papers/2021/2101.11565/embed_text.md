## Introduction

Figure 1: Example of an SPP in GCS. The source set is on the left and the target set is on the right. The graph edges are arrows, and the shortest path is shown in dashed green. The dotted red lines connect the optimal positions of the vertices along the shortest path.

The Shortest-Path Problem (SPP) is one of the most important and ubiquitous problems in combinatorial optimization. In its single-source single-target version, this problem asks for a path of minimum length connecting two prescribed vertices of a graph, where the length of a path is defined as the sum of the lengths of its edges. Typically, the edge lengths are fixed scalars, given as problem data, and the assumptions made on their values have a dramatic impact on the problem complexity \[43, Chapters 6 to 8\]. In this paper we introduce the SPP in Graph of Convex Sets (GCS), a variant of the SPP in which the edge lengths are convex functions of continuous variables representing the position of the vertices (see Figure 1). More precisely, a GCS is a directed graph in which each vertex is paired with a convex set. The spatial position of a vertex is a continuous variable, constrained to lie in the corresponding convex set. The length of an edge is a given convex function of the position of the vertices that this edge connects. When looking for a path of minimum length in a GCS, we then have the extra degree of freedom of optimizing the position of the vertices visited by the path. According to the literature, this problem could also be classified as an SPP *with neighborhoods*; we call it SPP in GCS to highlight the crucial role that convexity plays in the developments of this paper.

Many problems of practical interest can be formulated as SPPs in GCS: for some of those the convex sets and the edge-length functions are naturally suggested by the application, for others the construction of the GCS requires more thinking. As an example of the former class of problems, scheduling the flight of a drone with limited batteries is immediately cast as an SPP in GCS like the one in Figure 1. The start region is on the left, the goal region is on the right, and the remaining regions can be used for recharging. Pairs of regions that are close enough for the drone to fly between are connected by an edge. The objective is to minimize the overall length of the flight. Optimal control of discrete-time hybrid dynamical systems is a main application that we target in this paper, and is an example of a problem whose formulation as an SPP in GCS is nontrivial. In this case we let the convex sets live in the joint state and control space of the dynamical system. Each discrete time step corresponds to an edge transition in the GCS, and the edge lengths quantify, e.g., the energy consumed to move between states (a length that is infinite if the motion is not compatible with the system dynamics). This is explained in detail in Section 8.

### Contributions

The following are the main contributions of this article.

### Problem statement (Section 2)

The SPP in GCS represents an unexplored class of problems at the interface of combinatorial and convex optimization. It lends itself to a simple problem statement and, at the same time, it is a versatile framework that includes as special cases many problems of practical relevance.

### Mixed-integer convex formulation (Section 5)

The SPP in GCS is easily seen to be NP-hard (Section 3). Our main contribution is the formulation of this problem as a strong and lightweight Mixed-Integer Convex Program (MICP). This program extends in a natural way the classical network-flow formulation of the SPP, and it allows us to efficiently find shortest paths in large graphs (hundreds of vertices) and high-dimensional spaces (tens of dimensions). In addition, the design principles of this MICP can be applied to improve existing mixed-integer formulations of other graph problems with neighborhoods, which are limited to small graphs and sets in two or three dimensions (see Appendix A).

### Set-based convex relaxation of bilinear constraints (Section 7)

The main building block of our MICP is a tight and compact convex relaxation for a class of bilinear constraints that emerge naturally in our problem. This relaxation is *set based*, in the sense that it does not rely on the explicit constraints that define the sets in our GCS, but it works directly with their abstract set representations. This makes our MICP usable even when these sets are black boxes accessible only through a separation oracle. This relaxation is similar in spirit to the Lovász-Schrijver one, and is based on perspective operators (a popular tool in mixed-integer optimization ).

### Control applications (Section 8)

Computation times are the main limitation to a widespread application of mixed-integer optimization in control of hybrid systems. Our shortest-path formulation of these problems is substantially different from the state of the art, as we do not use binary variables to encode the discrete mode in which the system is at each time step but, instead, we use them to select the transitions between modes. This different parameterization yields slightly larger but much stronger MICPs that, in our computational experiments, are orders of magnitude faster to solve.

### Related graph problems

In this subsection we overview a few variants of classical graph problems that are closely related to our problem formulation.

### Graph problems with neighborhoods

Graph problems where the vertices are allowed to move within corresponding sets are often called problems with neighborhoods. The SPP with neighborhoods has been analyzed in under stringent assumptions that ensure polynomial-time solvability: the sets are disjoint rectilinear polygons in the plane, and the edge lengths penalize the $\mathcal{L}_{1}$ distance between the vertices. The applications we target with this paper, however, do not verify any of these hypotheses. A special case of the SPP with neighborhoods is the touring-polygon problem, which asks for the shortest path between two points that visits a set of polygons in a given order. Our problem differs from this in that our sets are convex and the order in which we visit them is not predefined. Other problems akin to the touring polygon, but substantially different from the SPP in GCS, are the safari, the zookeeper, and the watchman route; see \[29, Part IV\] and the references therein.

The Traveling-Salesman Problem (TSP) and the Minimum-Spanning-Tree Problem (MSTP) are the two combinatorial problems that have been studied most extensively in their variants with neighborhoods. Exact algorithms for these generally rely on expensive mixed-integer nonconvex optimization, and do not scale beyond two or three dimensions. Although the techniques we propose in this paper are particularly well suited to the structure of the SPP, they can be used without modifications to formulate other graph problems with neighborhoods as very tractable MICPs (see Appendix A).

### Graph problems with clusters

Generalized Steiner problems (otherwise known as generalized network-design problems ) can be thought as the discrete counterpart of the graph problems with neighborhoods: the vertex set is partitioned into clusters and the problem constraints are expressed in terms of these clusters, rather than the original vertices. A clustered version of the SPP has been presented in: each vertex in the graph is assigned a nonnegative weight, and the total vertex weight incurred by the shortest path within each cluster must not exceed a given value. The problem we analyze in this paper can be approximated as an SPP with clusters in a natural way. In low-dimensional spaces, this approximation can be computationally efficient and sufficiently accurate for practical applications. However, this strategy is infeasible in high dimensions, where covering a volume of space with a cluster requires an exponential number of points.

### Euclidean shortest paths

Another related variant of the SPP is the Euclidean SPP, where we look for a continuous path that connects two points and avoids given polygonal obstacles. In two dimensions, this problem can be reduced to a discrete search and is solvable in polynomial time. In three dimensions or more the problem is NP-hard \[8, Theorem 2.3.2\], and common algorithms rely on a grid discretization of the space. More recently, a moment-based technique that handles semialgebraic obstacles has been proposed in.

## Problem statement

We start with a formal statement of the SPP in GCS. Let $G:={(\mathcal{V},\mathcal{E})}$ be a directed graph with vertex set $\mathcal{V}$ and edge set $\mathcal{E}$. For each vertex $v \in \mathcal{V}$, we have a nonempty compact convex set $\mathcal{X}_{v} \subset {\mathbb{R}}^{n}$ and a point ${\mathbf{x}}_{v}$ contained in it.^11^1The results presented in this paper are easily extended to the case in which the sets $\mathcal{X}_{v}$ do not have common dimension $n$. The length of an edge $e = {(u,v)} \in \mathcal{E}$ is determined by the location of the points ${\mathbf{x}}_{u}$ and ${\mathbf{x}}_{v}$ via the expression $\ell_{e}{({\mathbf{x}}_{u},{\mathbf{x}}_{v})}$. The *edge length* function $\ell_{e}$ takes values in ${\mathbb{R}}_{\geq 0} \cup {\{\infty\}}$ and is assumed to be proper, closed, and convex. Note that, despite its name, we do not assume $\ell_{e}$ to be a valid metric, and properties like symmetry or the triangle inequality are not required to hold. Given a source vertex $s$ and a target vertex $t \neq s$, an $s$-$t$ path $p$ is a sequence of distinct vertices $(v_{0},\ldots,v_{K})$ such that $v_{0} = s$, $v_{K} = t$, and ${(v_{k},v_{k + 1})} \in \mathcal{E}$ for all $k = {0,\ldots,{K - 1}}$. We denote with $\mathcal{E}_{p}:={\{{(v_{0},v_{1})},\ldots,{(v_{K - 1},v_{K})}\}}$ the set of edges traversed by this path, and with $\mathcal{P}$ the set of all $s$-$t$ paths in the graph $G$. The SPP in GCS is then stated as

The decision variables are the discrete path $p$ and the continuous values ${\mathbf{x}}_{v}$. The cost minimizes the total path length. Constraint is enforced only for the vertices visited by the path, since the positions of the other vertices are irrelevant.

The edge length used in Figure 1 is the Euclidean distance:

With this choice the polygonal line connecting the points ${\mathbf{x}}_{v}$ along a shortest path is as straight as possible, perfectly straight if ${(s,t)} \in \mathcal{E}$. Conversely, if the edge length is the Euclidean distance squared,

straight trajectories may be suboptimal if they require long steps ${\mathbf{x}}_{v} - {\mathbf{x}}_{u}$. Note also that by letting $\ell_{e}$ take infinite value outside a convex set $\mathcal{X}_{e}$ we are effectively enforcing the edge constraint ${({\mathbf{x}}_{u},{\mathbf{x}}_{v})} \in \mathcal{X}_{e}$. This will be used in Section 8 to formulate optimal-control problems as SPPs in GCS: there the edge constraints will couple the vertex positions according to the system dynamics.

## Complexity analysis

If we fix the vertex positions ${\mathbf{x}}_{v}$, problem simplifies to the classical SPP with scalar nonnegative edge lengths, which is easily solvable using, e.g., Linear Programming (LP). Similarly, if we fix the path $p$, problem simplifies to a convex program that can be efficiently solved for most convex sets $\mathcal{X}_{v}$ and edge lengths $\ell_{e}$. In this section we show that the simultaneous optimization of the vertex positions and the path makes the SPP in GCS an NP-hard problem.

Recall that an $s$-$t$ path $p:={(v_{0},\ldots,v_{K})}$ is said to be Hamiltonian if it visits every vertex in the graph (i.e., if $K = {{|\mathcal{V}|} - 1}$), and a graph is Hamiltonian if it contains such a path. The Hamiltonian-Path Problem (HPP) asks if a given graph is Hamiltonian. As an example, the graph in Figure 1 is not Hamiltonian.

### Theorem 3.1

The SPP in GCS is NP-hard.

### Proof 3.2

We show that the HPP is polynomial-time reducible to the SPP in GCS. The thesis will then follow since the HPP is NP-complete. We construct an SPP in GCS that shares the same graph $G$ as the given HPP. We let the source $\mathcal{X}_{s}:={\{ 0\}}$ and target $\mathcal{X}_{t}:={\{ 1\}}$ sets be singletons on the real line, while we define $\mathcal{X}_{v}:={\lbrack 0,1\rbrack}$ for all $v \neq {s,t}$. The length of each edge is the Euclidean distance squared. Given these choices, the optimal positioning of the vertices for a fixed path $p$ is given by $\mathbf{x}_{v_{k}} = {k/K}$ for $k = {0,\ldots,K}$. The length of this path is ${K{({1/K})}^{2}} = {1/K}$. We conclude that an optimal path is one for which $K$ is maximized, and is Hamiltonian if and only if $G$ is Hamiltonian. This reduction operates in polynomial time.

This simple reduction shows that, even if the convex sets $\mathcal{X}_{v}$ are one-dimensional intervals, the SPP in GCS can be a hard problem. Nonetheless, one might wonder if additional assumptions on the problem data could turn the SPP in GCS into a problem that is solvable in polynomial time.

What if the graph $G$ is acyclic? In case of an acyclic graph the HPP is solvable in linear time \[2, Section 4.4\], and our hardness proof is not valid.

What if the sets $\mathcal{X}_{v}$ are disjoint? In fact, some graph problems with neighborhoods can be solved more efficiently in case of disjoint neighborhoods.

What if the edge lengths $\ell_{e}$ are positively homogeneous? An edge length like the Euclidean distance could not be used in our reduction since it would not force the optimal path $p$ to visit as many vertices as possible.

It turns out that all these questions have a negative answer. This is summarized in the following theorem, whose proof is omitted since it is a long and relatively straightforward adaptation of the complexity analysis of the Euclidean SPP from.

### Theorem 3.3

Assume that the graph $G$ is acyclic, the sets $\mathcal{X}_{v}$ are disjoint, and the edge lengths $\ell_{e}$ are positively homogeneous. The SPP in GCS is NP-hard.

## Convex-analysis background

This section introduces two basic concepts in convex analysis: perspective operators (homogenization) and valid inequalities (duality). These are the main tools that we will use in the design and the analysis of our MICP. Our goal here is to set the notation and collect some important definitions and properties; for a comprehensive introduction to these topics see \[42, Parts II and III\] or \[25, Chapters III and IV\].

### Perspective operators

There is a natural construction that maps a set in $n$ dimensions to a cone in $n + 1$ dimensions. This is sometimes called *homogenization*, or the *cone over* the set. Here we call it *perspective*, for coherence with the name commonly used for the same operation applied to functions \[25, Section IV.2.2\].

### Definition 4.1

We define the *perspective* of a closed convex set $\mathcal{X} \subseteq {\mathbb{R}}^{n}$ as

where $cl$ denotes the closure of the set.

### Remark 4.2

The closure operation in Definition 4.1 is unnecessary for bounded sets $\mathcal{X}$. While, when the set $\mathcal{X}$ is unbounded, it ensures that the perspective $\overset{\sim}{\mathcal{X}}$ contains all its limit points with $\lambda = 0$ \[42, Theorem 8.2\].

Importantly, the perspective operation preserves convexity, and the set $\overset{\sim}{\mathcal{X}}$ is a closed convex cone. The next example shows that the perspective of a set represented in conic form can be computed very easily.

### Example 4.3

Let $\mathcal{X}:={\{\mathbf{x}:{{{\mathbf{A}\mathbf{x}} + \mathbf{b}} \in \mathcal{K}}\}}$, for some matrix $\mathbf{A}$, vector $\mathbf{b}$, and closed convex cone $\mathcal{K}$. We have $\overset{\sim}{\mathcal{X}} = {\{{(\mathbf{x},\lambda)}:{{\lambda \geq 0},{{{\mathbf{A}\mathbf{x}} + {\mathbf{b}\lambda}} \in \mathcal{K}}}\}}$.

This example has great practical relevance since, informally, it tells us that if a conic-optimization solver can handle the set $\mathcal{X}$ then it can also handle its perspective $\overset{\sim}{\mathcal{X}}$. For instance, we see that the perspective of a polyhedral, ellipsoidal, and spectrahedral set can be represented through a set of linear, second-order-cone, and semidefinite constraints, respectively. More in general, if the set $\mathcal{X}$ is bounded, the formal equivalence of optimizing over $\mathcal{X}$ and its perspective $\overset{\sim}{\mathcal{X}}$ can be established using the ellipsoid method \[21, Chapter 4\], since the separation problems for these two sets are easily seen to be equivalent.

The next definition uses the construction from \[42, Page 39\] to describe what the perspective operation does to a convex function.

### Definition 4.4

We define the *perspective* of a closed convex function $f:{{\mathbb{R}}^{n}\rightarrow{{\mathbb{R}} \cup {\{\infty\}}}}$ as the unique function $\overset{\sim}{f}$ whose epigraph is the perspective of the epigraph of $f$, i.e.,

where ${{epi}f}:={\{{(\mathbf{x},\sigma)}:{{f{(\mathbf{x})}} \leq \sigma}\}}$.^22^2More precisely the sets ${epi}\overset{\sim}{f}$ and $\overset{\sim}{{epi}⁡f}$ are isomorphic: ${{epi}\overset{\sim}{f}}:={\{{(\mathbf{x},\lambda,\sigma)}:{{(\mathbf{x},\sigma,\lambda)} \in \overset{\sim}{{epi}⁡f}}\}}$.

Since its epigraph is closed and convex, the perspective function $\overset{\sim}{f}$ is closed and jointly convex in $\mathbf{x}$ and $\lambda$.

### Remark 4.5

For $\lambda > 0$, noticing that ${\lambda{{epi}f}} = {\{{(\mathbf{x},\sigma)}:{{\lambda f{({\mathbf{x}/\lambda})}} \leq \sigma}\}}$, we have that the perspective function is ${\overset{\sim}{f}{(\mathbf{x},\lambda)}} = {\lambda f{({\mathbf{x}/\lambda})}}$. For $\lambda < 0$, we immediately see that ${\overset{\sim}{f}{(\mathbf{x},\lambda)}} = \infty$. The behavior for $\lambda = 0$ is more complicated \[42, Corollary 8.5.2\], but for the scope of this paper it suffices to note that if $f$ is proper then, by the closedness of $\overset{\sim}{f}$, we must have ${\overset{\sim}{f}{(\mathbf{0},0)}} = 0$.

Although Definition 4.4 might seem unsuitable for numerical optimization, the perspectives of most common functions $f$ can be minimized using standard solvers. In fact, given a conic representation of the epigraph of $f$, we can compute the epigraph of $\overset{\sim}{f}$ as in Example 4.3, and minimize $\overset{\sim}{f}$ using a slack variable.

The next two examples draw further useful parallels between the perspective operation applied to sets and to functions.

### Example 4.6

Let $\mathcal{X}$ be a nonempty closed convex set and $g$ be a finite convex function. Define ${f{(\mathbf{x})}}:={g{(\mathbf{x})}}$ if $\mathbf{x} \in \mathcal{X}$ and ${f{(\mathbf{x})}}:=\infty$ otherwise. We have ${\overset{\sim}{f}{(\mathbf{x},\lambda)}} = {\overset{\sim}{g}{(\mathbf{x},\lambda)}}$ if ${(\mathbf{x},\lambda)} \in \overset{\sim}{\mathcal{X}}$ and ${\overset{\sim}{f}{(\mathbf{x},\lambda)}} = \infty$ otherwise.

### Example 4.7

For a set $\mathcal{X}:={\{\mathbf{x}:{{f_{i}{(\mathbf{x})}} \leq {0{for}{all}i} \in \mathcal{I}}\}}$, where the functions $f_{i}$ are closed and convex, we have $\overset{\sim}{\mathcal{X}} = {\{{(\mathbf{x},\lambda)}:{{{\overset{\sim}{f}}_{i}{(\mathbf{x},\lambda)}} \leq {0{for}{all}i} \in \mathcal{I}}\}}$. Equivalently, using Remark 4.5, we have $\overset{\sim}{\mathcal{X}} = {{cl}{\{{{(\mathbf{x},\lambda)}:{{\lambda > 0},{{\lambda f_{i}{({\mathbf{x}/\lambda})}} \leq {0{for}{all}i} \in \mathcal{I}}}}\}}}$.

### Valid inequalities

A second cone that is naturally associated with a convex set is the cone of its valid inequalities. This will play an important role in the analysis of our MICP in Section 7. We report here a formal definition and a useful property.

### Definition 4.8

We define the *cone of valid inequalities* of a set $\mathcal{X} \subseteq {\mathbb{R}}^{n}$ as

The cone $\mathcal{X}^{\circ}$ is easily seen to be closed and convex, even when $\mathcal{X}$ is neither closed nor convex. Note also that the cone of valid inequalities is closely related to the *polar set*, but the latter lives in $n$ dimensions.

The next lemma relates the two operations defined in this section. Recall that the *dual cone* of a closed convex cone $\mathcal{K}$ is the set $\mathcal{K}^{*}:={\{{\mathbf{a}}:{{{\mathbf{a}}^{\top}{\mathbf{x}}} \geq {0{for}{all}{\mathbf{x}}} \in \mathcal{K}}\}}$.

### Lemma 4.9

Let $\mathcal{X}$ be a closed convex set. The closed convex cones $\overset{\sim}{\mathcal{X}}$ and $\mathcal{X}^{\circ}$ are dual to each other.

### Proof 4.10

The perspective cone $\overset{\sim}{\mathcal{X}}$ can be equivalently defined as the closure of the cone generated by $\mathcal{X} \times {\{ 1\}}$. By applying \[42, Corollary 11.7.2\] to the latter set, we obtain $\overset{\sim}{\mathcal{X}} = {\{{(\mathbf{x},\lambda)}:{{{\mathbf{a}^{\top}\mathbf{x}} + {b\lambda}} \geq {0{for}{all}{(\mathbf{a},b)}} \in \mathcal{X}^{\circ}}\}}$. This shows that $\overset{\sim}{\mathcal{X}} = {(\mathcal{X}^{\circ})}^{*}$. The other direction follows from the bipolar theorem \[42, Theorem 14.1\].

## Mixed-integer convex formulation

We now present the main contribution of this paper: the formulation of the SPP in GCS as a strong and lightweight MICP. This program is designed in two steps. First, in Section 5.2, we extend the network-flow formulation of the classical SPP (recalled in Section 5.1) to our setting. This yields an optimization problem with bilinear equality constraints. Second, in Section 5.3, we construct a convex relaxation tailored to these bilinear constraints and we formulate our MICP. The relaxation technique used in this section will be described at a higher level of generality and thoroughly analyzed in Section 7.

### Network-flow formulation of the SPP

The starting point for the design of our MICP is the network-flow formulation of the SPP with scalar nonnegative edge lengths (see, e.g., \[2, Section 4.1\]):

$\sum\limits_{e \in \mathcal{E}}{l_{e}y_{e}}$

${{{\sum\limits_{e \in \mathcal{E}_{s}^{out}}y_{e}} = 1},{{\sum\limits_{e \in \mathcal{E}_{t}^{in}}y_{e}} = 1}},$

${{{\sum\limits_{e \in \mathcal{E}_{v}^{in}}y_{e}} = {\sum\limits_{e \in \mathcal{E}_{v}^{out}}y_{e}}},{{\sum\limits_{e \in \mathcal{E}_{v}^{out}}y_{e}} \leq 1}},$

In this LP the decision variables $y_{e}$ parameterize a path $p$, with $y_{e} = 1$ if the edge $e$ is traversed by $p$ and $y_{e} = 0$ otherwise. The scalar $l_{e} \geq 0$ represents the length of the edge $e$. The sets $\mathcal{E}_{v}^{in}:={\{{{(u,v)} \in \mathcal{E}}\}}$ and $\mathcal{E}_{v}^{out}:={\{{{(v,u)} \in \mathcal{E}}\}}$ collect the edges incoming and outgoing vertex $v$. Without loss of generality, we assume ${|\mathcal{E}_{s}^{in}|} = {|\mathcal{E}_{t}^{out}|} = 0$, i.e., the source and the target have no incoming and outgoing edges, respectively. Interpreting the value of $y_{e}$ as the *flow* carried by the edge $e$, constraint (4b) asks that one unit of flow is injected in the source and ejected from the target. For all the other vertices, constraint (4c) enforces the *flow conservation* and a *degree constraint*. The latter enforces a limit of one to the total flow traversing the vertex.

### Remark 5.1

Note that we do not explicitly require the flows $y_{e}$ to be binary, but we only enforce their nonnegativity in (4d). This is because all the basic feasible solutions of the LP (5.1) can be shown to have binary value (see, e.g., \[2, Section 11.12\]), and the constraints $y_{e} \in {\{ 0,1\}}$ would not affect the optimal value of this program.

### Remark 5.2

Since we assumed the edge lengths $l_{e}$ to be nonnegative, the degree constraint in (4c) is actually redundant for the LP (5.1), as well as for problem (5.2) below. However, as we will see in Section 5.4, this constraint is not redundant for our final MICP. Therefore we include it in our formulation from the start.

### Biconvex formulation

As an intermediate step towards our MICP, we formulate the SPP in GCS as a *biconvex* optimization problem. Specifically, a nonlinear program whose nonconvexity comes only from products between the vertex locations and the flow variables parameterizing a path. Note that this is consistent with the observation from Section 3 that the SPP in GCS simplifies to a convex program if we fix either the vertex locations or the path through the graph.

A natural attempt to extend the LP (5.1) to the SPP in GCS is to proceed as done for other graph problems with neighborhoods: include the vertex locations ${\mathbf{x}}_{v}$ among our decision variables, enforce the constraint ${\mathbf{x}}_{v} \in \mathcal{X}_{v}$ for all $v \in \mathcal{V}$, and substitute the addends in the cost (4a) with $\ell_{e}{({\mathbf{x}}_{u},{\mathbf{x}}_{v})}y_{e}$. However, one immediate issue with this approach is that the latter product is undefined if ${\ell_{e}{({\mathbf{x}}_{u},{\mathbf{x}}_{v})}} = \infty$ and $y_{e} = 0$, while we would like the cost contribution of the edge $e$ to always be zero if $y_{e} = 0$. Perspective functions give us a convenient and rigorous way to "turn on and off" the length of an edge using the corresponding flow variable.

Let us introduce two auxiliary variables ${\mathbf{z}}_{e}:={y_{e}{\mathbf{x}}_{u}}$ and ${\mathbf{z}}_{e}^{\prime}:={y_{e}{\mathbf{x}}_{v}}$ per edge $e = {(u,v)}$, and consider the perspective function ${\overset{\sim}{\ell}}_{e}{({\mathbf{z}}_{e},{\mathbf{z}}_{e}^{\prime},y_{e})}$.^33^3 We are slightly abusing notation here: since in Definition 4.4 we defined the perspective of functions with a single argument, to be precise, we should write ${\overset{\sim}{\ell}}_{e}{({({\mathbf{z}}_{e},{\mathbf{z}}_{e}^{\prime})},y_{e})}$. When the flow $y_{e}$ is positive, this function coincides with the product above:

where the first equality comes from Remark 4.5. When the flow $y_{e}$ is zero, the function ${\overset{\sim}{\ell}}_{e}$ is well defined and correctly evaluates to zero, even when ${\ell_{e}{({\mathbf{x}}_{u},{\mathbf{x}}_{v})}} = \infty$. In fact, $y_{e} = 0$ implies ${\mathbf{z}}_{e} = {\mathbf{z}}_{e}^{\prime} = \mathbf{0}$, and ${{\overset{\sim}{\ell}}_{e}{(\mathbf{0},\mathbf{0},0)}} = 0$ as discussed in Remark 4.5.

Overall, we then have the following biconvex formulation of the SPP in GCS:

The decision variables are the flows $y_{e}$, the vertex positions ${\mathbf{x}}_{v}$, and the auxiliary variables ${\mathbf{z}}_{e}$ and ${\mathbf{z}}_{e}^{\prime}$. The role of the latter is to match the vertices ${\mathbf{x}}_{u}$ and ${\mathbf{x}}_{v}$ when $y_{e} = 1$, and collapse to zero when $y_{e} = 0$. This behavior is driven by the bilinear equality constraints (5.2), which are the only nonconvexity in our formulation and whose convexification is the focus of the next subsection. Before that, let us formally verify that, as mentioned in Remark 5.1 for the LP (5.1), forcing the flows $y_{e}$ to be binary does not affect the optimal value of the biconvex program (5.2).

### Proposition 5.3

For any local minimum $L \in {\mathbb{R}}_{\geq 0}$ of problem (5.2), there exists a feasible point of (5.2) with cost equal to $L$ and such that $y_{e} \in {\{ 0,1\}}$ for all $e \in \mathcal{E}$.

### Proof 5.4

Given a local minimizer of (5.2) with cost $L$, we fix the vertex positions $\mathbf{x}_{v}$. This reduces problem (5.2) to an LP of the form (5.1). The optimal value of this LP must be $L$, otherwise we would have found a descent direction and our solution of (5.2) would not be locally optimal. Furthermore, because of Remark 5.1, we can assume that the optimal flows of this LP are binary. Paired with the previously fixed variables $\mathbf{x}_{v}$, these binary flows yield a feasible solution of (5.2) with cost $L$.

### Convex relaxation of the bilinear constraints

The biconvex program (5.2) is our first formulation of the SPP in GCS that can be tackled numerically. However, the bilinear constraints (5.2) make this optimization problem challenging to solve, even just locally. In this subsection we show how to reformulate problem (5.2) as a lightweight and strong MICP, that can be reliably solved to global optimality using branch-and-bound algorithms.

The next lemma allows us to construct a tight envelope around the constraints of the biconvex program (5.2) through a small number of perspective cones. In its statement we let $\mathcal{E}_{v}:={\mathcal{E}_{v}^{in} \cup \mathcal{E}_{v}^{out}}$ denote the set of edges incident with vertex $v \in \mathcal{V}$. Recall also that a valid constraint for an optimization problem is a constraint that is verified by all the feasible points.

### Lemma 5.5

For some vertex $v \in \mathcal{V}$, assume that the linear inequality

is valid for problem (5.2). Partitioning the summation over $\mathcal{E}_{v}$ in incoming and outgoing edges, we have that the following convex constraint is also valid for (5.2):

### Proof 5.6

Constraint requires two conditions to hold. One is, which is assumed. The other is verified by multiplying both sides of $\mathbf{x}_{v} \in \mathcal{X}_{v}$ from (5.2) by the left-hand side of, and then using the bilinear constraints (5.2).

### Remark 5.7

If the valid constraint holds with equality, Lemma 5.5 simply amounts to multiplying this equality by $\mathbf{x}_{v}$, and it gives us a valid linear equality of the form ${{\sum_{e \in \mathcal{E}_{v}^{in}}{c_{e}\mathbf{z}_{e}^{\prime}}} + {\sum_{e \in \mathcal{E}_{v}^{out}}{c_{e}\mathbf{z}_{e}}} + {d\mathbf{x}_{v}}} = \mathbf{0}$.

### Remark 5.8

Generating new valid constraints by multiplying existing ones is a standard procedure at the core of many relaxation techniques. Lemma 5.5 will be analyzed at a higher level of generality in Section 7, where its similarities with existing methods will be clearly drawn.

Lemma 5.5 lifts any valid linear constraint on the flows incident with vertex $v$ into a convex constraint that envelops the feasible set of problem (5.2). Our MICP is obtained by applying this lemma to each flow constraint in the LP (5.1), and by replacing the constraints of the biconvex program (5.2) with the envelope resulting from this process. Let us first state our MICP and then prove its equivalence to the SPP in GCS (Theorem 5.9 below):

Constraint (5.3) is obtained as in Remark 5.7 from the flow conservation in (4c), and (5.3) is the result of applying Lemma 5.5 to the nonnegativity constraint (4d). Note that the application of the same technique to the equalities (5.3) and to the degree constraint in (4c) would give us

${{{\mathbf{x}}_{s} = {\sum\limits_{e \in \mathcal{E}_{s}^{out}}{\mathbf{z}}_{e}}},{{\mathbf{x}}_{t} = {\sum\limits_{e \in \mathcal{E}_{t}^{in}}{\mathbf{z}}_{e}^{\prime}}}},$

${{{\mathbf{x}}_{v} - {\sum\limits_{e \in \mathcal{E}_{v}^{out}}{\mathbf{z}}_{e}}} \in {\left( {1 - {\sum\limits_{e \in \mathcal{E}_{v}^{out}}y_{e}}} \right)\mathcal{X}_{v}}},$

However these constraints would be redundant since the vertex positions ${\mathbf{x}}_{v}$ for $v \in \mathcal{V}$ do not appear in the rest of problem (5.3). Note also that the combination of (5.3) and (5.3) implies the constraints ${\mathbf{x}}_{v} \in \mathcal{X}_{v}$ for all $v \in \mathcal{V}$, which would also be redundant for our MICP. The convex relaxation of (5.3) is obtained simply by dropping the integrality constraint (5.3) (the nonnegativity of the flows $y_{e}$ is imposed by the cost and also by (5.3)). Observe that, unlike the biconvex program (5.2), the optimal value of the MICP can decrease if the flows are allowed to be fractional.

### Theorem 5.9

The MICP (5.3) has optimal value equal to the SPP in GCS. An optimal path $p$ for problem is recovered from the solution of (5.3) through the relation $\mathcal{E}_{p}:={\{{e \in \mathcal{E}}:{y_{e} = 1}\}}$. An optimal positioning of the vertices is reconstructed for the source and the target as in (9a), and for all the other vertices by letting $\mathbf{x}_{v}$ be any point such that (9b) holds.

In Section 7.3 we will see that this theorem follows from a simple geometric property of Lemma 5.5. Here we give a direct proof that explicitly illustrates the logic behind our formulation.

### Proof 5.10

The only flows that can satisfy the constraints in (5.3) are such that the set $\mathcal{E}_{p}$ defined above describes the vertex-disjoint union of an $s$-$t$ path and cycles. However, the presence of cycles can be excluded since the edge lengths $\ell_{e}$ are nonnegative, and traversing a cycle that is disjoint from the main path cannot decrease the cost. Therefore, at optimality, $\mathcal{E}_{p}$ identifies a path $p$. For all the edges $e \notin \mathcal{E}_{p}$, constraint (5.3) simplifies to $\mathbf{z}_{e} = \mathbf{z}_{e}^{\prime} = \mathbf{0}$, and the corresponding cost addends give ${{\overset{\sim}{\ell}}_{e}{(\mathbf{0},\mathbf{0},0)}} = 0$. For the vertices $v \notin p$, constraint (5.3) is trivially satisfied and (9b) reads $\mathbf{x}_{v} \in \mathcal{X}_{v}$. For an edge $e = {(u,v)}$ along the path $p$, constraint (5.3) becomes $\mathbf{z}_{e} \in \mathcal{X}_{u}$ and $\mathbf{z}_{e}^{\prime} \in \mathcal{X}_{v}$, and the cost addend is ${{\overset{\sim}{\ell}}_{e}{(\mathbf{z}_{e},\mathbf{z}_{e}^{\prime},1)}} = {\ell_{e}{(\mathbf{z}_{e},\mathbf{z}_{e}^{\prime})}}$. Denoting with $f = {(v,w)} \in \mathcal{E}_{p}$ the edge after $e$ in the path, the flow conservation (5.3) reads $\mathbf{z}_{e}^{\prime} = \mathbf{z}_{f}$. Finally, the conditions in (5.3) give us $\mathbf{x}_{u} = \mathbf{z}_{e}$ and $\mathbf{x}_{v} = \mathbf{z}_{e}^{\prime}$ for all edges $e = {(u,v)} \in \mathcal{E}_{p}$.

### Remark 5.11

If the sets $\mathcal{X}_{v}$ are singletons, the SPP in GCS simplifies to the SPP with nonnegative edge lengths. In this case our MICP reduces to the LP (5.1) and its convex relaxation is exact, as discussed in Remark 5.1.

### Remark 5.12

For the edge lengths $\ell_{e}$ and convex sets $\mathcal{X}_{v}$ that typically appear in practice, the MICP (5.3) can be solved to global optimality with standard solvers (see the discussion in Section 4.1). However, problem (5.3) can be tackled numerically even when the sets in our GCS are not defined by explicit constraints (e.g., convex inequalities). For example, each set $\mathcal{X}_{v}$ may be very complex and accessible only through an oracle that, given a point $\mathbf{x}_{v}$, either certifies that $\mathbf{x}_{v} \in \mathcal{X}_{v}$ or returns a separating hyperplane. In fact, such an oracle is easily adapted to checking membership to the perspective cones in (5.3), and this black-box access to the problem constraints is sufficient for efficient optimization algorithms like the ellipsoid method.

### Degree constraints

In Remark 5.2 we anticipated that, although redundant for the LP (5.1), the degree constraints (5.3) play an important role in our MICP. This is illustrated in the next example, which shows how the optimal flows from (5.3) can induce cycles if the degree constraints are not enforced.

### Example 5.13

Consider a graph with vertices $\mathcal{V}:={\{ s,1,2,t\}}$ and edges $\mathcal{E}:={\{{(s,1)},{},{},{(1,t)}\}}$. Define the sets $\mathcal{X}_{s}:={\{{- 1}\}}$, $\mathcal{X}_{1}:={\lbrack{- 1},1\rbrack}$, $\mathcal{X}_{2}:={\{ 0\}}$, and $\mathcal{X}_{t}:={\{ 1\}}$. Let the length of each edge be the Euclidean distance squared. The optimal value of this SPP in GCS is $2$ and the optimal path is $p = {(s,1,t)}$. However, if we do not enforce the degree constraints (5.3), our MICP has optimal value equal to $1$ and its optimal flows are $y_{e} = 1$ for all $e \in \mathcal{E}$, i.e., they induce the cycle $$.

In case of an acyclic graph $G$, the issues just described do not arise and the degree constraints are redundant for our MICP and its convex relaxation. Nonetheless, we still include them in our formulation since they are computationally light and their explicit presence can trigger the use of specialized generalized-upper-bound branching rules in the solver \[10, Section 9.2\].

## Alternative formulations

Multiple alternative MICP formulations of the SPP in GCS can be designed and finding the most effective one is a tradeoff between the size of the program and the tightness of its convex relaxation. The MICP (5.3) is very compact: it has only $O{({|\mathcal{E}|})}$ binary variables, $O{({n{|\mathcal{E}|}})}$ continuous variables, and $O{({n{({{|\mathcal{V}|} + {|\mathcal{E}|}})}})}$ constraints (assuming that the cones in (5.3) are described by $O{(n)}$ constraints). In addition, in the experiments in Section 9, we will see that the relaxation of our MICP is typically very tight (although a carefully designed instance in Section 9.4 shows that our relaxation can, in principle, be arbitrarily loose).

A simple alternative way to reformulate the biconvex problem (5.2) as an MICP is to enforce the integrality constraints $y_{e} \in {\{ 0,1\}}$ for all $e \in \mathcal{E}$, and relax each bilinear constraint (5.2) independently using a McCormick envelope. With our notation, this amounts to replacing (5.2) with

where, for each $v \in \mathcal{V}$, we let $\mathcal{B}_{v}$ be an axis-aligned box that contains $\mathcal{X}_{v}$. Especially if the convex sets $\mathcal{X}_{v}$ are defined by many constraints, this MICP is more compact than ours. However, as we will see in Section 9, this formulation has loose convex relaxation and its solution times are generally much larger than with our approach.

At the other end of the spectrum, a variety of stronger but potentially more expensive formulations could be devised. For example, we have found that subtour-elimination constraints like \[48, Section 2.2\] can tighten the relaxation of our MICP for some classes of problems. Alternatively, we could formulate our MICP by grouping the constraints in (5.2) vertex by vertex, and by computing the convex hull of each group (see Section 7.2 below). We could also use more expensive semidefinite relaxations of the bilinear constraints (5.2). In our computational experience, the MICP (5.3) represents the best compromise between a lightweight and a strong formulation, and its solution times are lower than any other formulation we have tested.

## Analysis of the mixed-integer formulation

In this section we describe and analyze at a more abstract level the method used in Section 5.3 to formulate the SPP in GSC as an MICP. We show that Lemma 5.5 can be used to design convex relaxations of a large class of bilinear constraints, and we connect this result to existing relaxation techniques for nonconvex optimization. Finally, we give a simpler geometric proof of the validity of our MICP (already shown in Theorem 5.9).

### Set-based relaxation of bilinear constraints

Our first step in this analysis is to show that Lemma 5.5 is, in fact, a general-purpose relaxation technique for nonconvex sets of the form

where $\mathcal{X} \subseteq {\mathbb{R}}^{n}$ and $\mathcal{Y} \subseteq {\mathbb{R}}^{m}$ are closed convex sets. In particular, here $\mathcal{X}$ takes the place of a generic set $\mathcal{X}_{v}$ in our GCS, while $\mathcal{Y}$ plays the role of the linear constraints on the flow variables incident with vertex $v$ (see Remark 7.3 below for more details).

A natural approach to construct a convex envelope around the set $\mathcal{S}$ is to multiply all the valid inequalities ${{{\mathbf{a}}^{\top}{\mathbf{x}}} + b} \geq 0$ for the set $\mathcal{X}$ by all the valid inequalities ${{{\mathbf{c}}^{\top}{\mathbf{y}}} + d} \geq 0$ for the set $\mathcal{Y}$, and then use the bilinear equality ${\mathbf{Z}} = {{\mathbf{x}}{\mathbf{y}}^{\top}}$ to linearize these products. This gives us an infinite family of valid linear inequalities for $\mathcal{S}$, which form our convex relaxation:

Note that the conditions ${\mathbf{x}} \in \mathcal{X}$ and ${\mathbf{y}} \in \mathcal{Y}$ are implied by the inequalities in that correspond to ${(\mathbf{0},1)} \in \mathcal{Y}^{\circ}$ and ${(\mathbf{0},1)} \in \mathcal{X}^{\circ}$, respectively.

The relaxation is not obviously implementable on a computer, since it involves an infinite number of constraints. However, if one of the two sets is a polytope (i.e., a bounded polyhedron) then the convex set $\mathcal{S}^{\prime}$ can be efficiently described by a finite number of perspective-cone constraints.

### Proposition 7.1

Let $\mathcal{Y}$ be a polytope with halfspace representation $\{\mathbf{y}:{{{\mathbf{c}_{i}^{\top}\mathbf{y}} + d_{i}} \geq {0{for}{all}i} \in \mathcal{I}}\}$. We have

### Proof 7.2

To recover from we first use Lemma 4.9 to rewrite the membership to $\overset{\sim}{\mathcal{X}}$ as ${{\mathbf{a}^{\top}{({{\mathbf{Z}\mathbf{c}_{i}} + {d_{i}\mathbf{x}}})}} + {b{({{\mathbf{c}_{i}^{\top}\mathbf{y}} + d_{i}})}}} \geq 0$ for all ${(\mathbf{a},b)} \in \mathcal{X}^{\circ}$. Then we notice that listing only the valid inequalities $(\mathbf{c}_{i},d_{i})$ for $i \in \mathcal{I}$ is equivalent to listing all the valid inequalities ${(\mathbf{c},d)} \in \mathcal{Y}^{\circ}$. In fact, since $\mathcal{Y}$ is bounded, any vector ${(\mathbf{c},d)} \in \mathcal{Y}^{\circ}$ can be expressed as $\sum_{i \in \mathcal{I}}{\alpha_{i}{(\mathbf{c}_{i},d_{i})}}$ for some nonnegative coefficients $\alpha_{i}$. Using these coefficients, the inequality ${{\mathbf{a}^{\top}\mathbf{Z}\mathbf{c}} + {d\mathbf{a}^{\top}\mathbf{x}} + {b\mathbf{c}^{\top}\mathbf{y}} + {bd}} \geq 0$ is seen to be implied by the inequalities generated by $(\mathbf{c}_{i},d_{i})$ for $i \in \mathcal{I}$.

We then have two descriptions of the relaxation $\mathcal{S}^{\prime}$: the symmetric one that clearly exposes the logic behind the technique, and the asymmetric one that is computationally efficient, provided that one of the two sets is polytopic and has a small number of facets. The asymmetric relaxation generalizes Lemma 5.5, with ${{{\mathbf{c}}_{i}^{\top}{\mathbf{y}}} + d_{i}} \geq 0$ taking the place of the flow inequality. The asymmetric relaxation is also set based, in the sense that it does not rely on the explicit constraints defining $\mathcal{X}$, but it works directly with its abstract set representation. Besides making the analysis very concise, this has also the practical advantages discussed in Remark 5.12.

### Remark 7.3

The constraints of the biconvex program (5.2) can be restated in terms of the set $\mathcal{S}$ as follows. First, we collect in the vector $\mathbf{y}_{v}:={(y_{e})}_{e \in \mathcal{E}_{v}}$ the flows incident with vertex $v$. Second, we let $\mathcal{Y}_{v}$ be the polytope defined by the linear constraints acting on $\mathbf{y}_{v}$. Constraint (4b) and the flow nonnegativity (4d) make $\mathcal{Y}_{s}$ and $\mathcal{Y}_{t}$ unit simplices (recall that ${|\mathcal{E}_{s}^{in}|} = {|\mathcal{E}_{t}^{out}|} = 0$). For $v \neq {s,t}$, the polytope $\mathcal{Y}_{v}$ is defined by the flow nonnegativity (4d) together with the conservation and degree constraints in (4c). Third, we stack in the columns of the matrix $\mathbf{Z}_{v}$ the auxiliary variables $\mathbf{z}_{e}^{\prime}$ for $e \in \mathcal{E}_{v}^{in}$ and $\mathbf{z}_{e}$ for $e \in \mathcal{E}_{v}^{out}$, so that the bilinear constraints (5.2) take the form $\mathbf{Z}_{v} = {\mathbf{x}_{v}\mathbf{y}_{v}^{\top}}$. By defining the sets $\mathcal{S}_{v}$ as in, the constraints of problem (5.2) become ${(\mathbf{x}_{v},\mathbf{y}_{v},\mathbf{Z}_{v})} \in \mathcal{S}_{v}$ for all $v \in \mathcal{V}$. Our relaxation of the SPP in GCS is then obtained by replacing the constraint sets $\mathcal{S}_{v}$ with $\mathcal{S}_{v}^{\prime}$ defined as in.

### Tightness of the relaxation $\mathcal{S}^{\prime}$

Ideally, we would like our relaxation to be as tight as possible, and the set $\mathcal{S}^{\prime}$ to coincide with the convex hull of $\mathcal{S}$. This equality holds, for example, when $\mathcal{X}$ and $\mathcal{Y}$ are intervals on the real line, in which case $\mathcal{S}^{\prime}$ simplifies to the McCormick envelope. However, the inclusion ${{conv}\mathcal{S}} \subset \mathcal{S}^{\prime}$ can be strict in general. In fact, for polytopic sets $\mathcal{X}$ and $\mathcal{Y}$, our approach of multiplying valid inequalities simplifies to the first level of the Reformulation-Linearization Technique (RLT), which does not yield the convex hull of $\mathcal{S}$ if, e.g., $\mathcal{X}:=\mathcal{Y}:={\lbrack 0,1\rbrack}^{2}$.

The convex hull of $\mathcal{S}$ can be efficiently described when $\mathcal{Y}$ is a polytope with a small number of extreme points ${\{{\hat{\mathbf{y}}}_{j}\}}_{j \in \mathcal{J}}$. Specifically, by using disjunctive-programming techniques, it can be verified that

Note that this (lifted) description is convex and also set based. While our relaxation $\mathcal{S}^{\prime}$ has size proportional to the number $|\mathcal{I}|$ of facets of $\mathcal{Y}$, this description of the convex hull has size proportional to the number $|\mathcal{J}|$ of extreme points of $\mathcal{Y}$. For the SPP in GCS, the polytopes $\mathcal{Y}_{v}$ have $O{({{|\mathcal{E}_{v}^{in}|} + {|\mathcal{E}_{v}^{out}|}})}$ facets and only $O{({{|\mathcal{E}_{v}^{in}|}{|\mathcal{E}_{v}^{out}|}})}$ extreme points, and this difference can be relatively small if the graph is sparse. However, in our experience the MICPs obtained with our method provide a better tradeoff between strength and size, and are typically much faster to solve.

### Remark 7.4

That our relaxation $\mathcal{S}^{\prime}$ is not always the convex hull of $\mathcal{S}$ should be fully expected. In fact, for $\mathcal{X}:={\lbrack 0,1\rbrack}^{n}$ and $\mathcal{Y}:={\lbrack 0,1\rbrack}^{m}$, the bilinear program

is NP-hard, and equivalent to minimizing a linear function over $\mathcal{S}$. The equality $\mathcal{S}^{\prime} = {{conv}\mathcal{S}}$ would then allow us to solve an NP-hard problem in polynomial time.

### Geometric proof of Theorem 5.9

In the proof of Theorem 5.9 we have shown the correctness of the MICP (5.3) by analyzing all the feasible values that the variables in this program can take. We now present a simple property of the relaxation $\mathcal{S}^{\prime}$ that will lead to a geometric and more concise proof of Theorem 5.9. This result will also generalize a known property of RLT.

### Lemma 7.5

Let $\mathcal{Y}$ be a polytope and $\hat{\mathbf{y}}$ one of its extreme points. We have ${(\mathbf{x},\hat{\mathbf{y}},\mathbf{Z})} \in \mathcal{S}$ if and only if ${(\mathbf{x},\hat{\mathbf{y}},\mathbf{Z})} \in \mathcal{S}^{\prime}$.

### Proof 7.6

One direction follows from $\mathcal{S} \subseteq \mathcal{S}^{\prime}$. For the other direction we show that if ${(\mathbf{x},\hat{\mathbf{y}},\mathbf{Z})} \in \mathcal{S}^{\prime}$ then $\mathbf{Z} = {\mathbf{x}{\hat{\mathbf{y}}}^{\top}}$. Since $\hat{\mathbf{y}}$ is an extreme point of $\mathcal{Y}$, there are $m$ linearly independent inequalities that are active at $\hat{\mathbf{y}}$. Let $\mathbf{C} \in {\mathbb{R}}^{m \times m}$ and $\mathbf{d} \in {\mathbb{R}}^{m}$ collect the coefficients $(\mathbf{c}_{i},d_{i})$ of these inequalities, so that ${{\mathbf{C}\hat{\mathbf{y}}} + \mathbf{d}} = \mathbf{0}$. For the same inequalities, the constraints in give us ${{\mathbf{Z}\mathbf{c}_{i}} + {d_{i}\mathbf{x}}} = \mathbf{0}$ or, equivalently, ${{\mathbf{Z}\mathbf{C}^{\top}} + {\mathbf{x}\mathbf{d}^{\top}}} = \mathbf{0}$. We then have ${\mathbf{Z}\mathbf{C}^{\top}} = {\mathbf{x}{\hat{\mathbf{y}}}^{\top}\mathbf{C}^{\top}}$ and, since $\mathbf{C}$ is invertible, $\mathbf{Z} = {\mathbf{x}{\hat{\mathbf{y}}}^{\top}}$.

### Proof 7.7 (Alternative proof of Theorem 5.9)

As in the first proof of Theorem 5.9, note that the optimal solution of the MICP (5.3) is such that the edges traversed by a unit of flow identify a path $p$. Note also that, for all $v \in \mathcal{V}$, the flow vectors $\mathbf{y}_{v}$ corresponding to a path $p$ are extreme points of the polytopes $\mathcal{Y}_{v}$. Then the validity of the MICP (5.3) follows since our relaxation is exact in these points by Lemma 7.5.

### Remark 7.8

Consider the bilinear program with polytopic sets $\mathcal{X}$ and $\mathcal{Y}$, and the additional constraint $\mathbf{y} \in {\{ 0,1\}}^{m}$. Assuming $\mathcal{Y} \subseteq {\lbrack 0,1\rbrack}^{m}$, the first-level RLT is known to yield a valid mixed-integer linear formulation of this program \[1, Theorem 1\]. Lemma 7.5 extends this result to generic closed convex sets $\mathcal{X}$. In fact, $\mathcal{Y} \subseteq {\lbrack 0,1\rbrack}^{m}$ ensures that any vector $\mathbf{y} \in {\mathcal{Y} \cap {\{ 0,1\}}^{m}}$ is an extreme point of $\mathcal{Y}$, and the relaxation $\mathcal{S}^{\prime}$ is exact in correspondence of these points.

### Related relaxation techniques

The basic idea of generating new valid constraints by multiplying existing ones is classical, and has many incarnations: from the simple McCormick envelope to semidefinite hierarchies for polynomial optimization, passing through RLT. Among this family of techniques, the Lovász-Schrijver hierarchy is the closest to ours, since it is set based and includes constraints of the form; see \[31, Theorem 1.6 and Conditions (iii) to (iii")\]. However, this hierarchy focuses on binary optimization and symmetric quadratic maps, and its naive application to the bilinear set $\mathcal{S}$ would produce multiple redundant variables and constraints. Our approach leverages the bilinear structure of the set $\mathcal{S}$, that emerges naturally in the SPP in GCS, to construct a relaxation $\mathcal{S}^{\prime}$ that is smaller and as tight as the first level of the Lovász-Schrijver hierarchy, without semidefinite constraints. (As discussed in Section 6, our practical experience is that higher levels of the hierarchy and semidefinite constraints lead to MICPs that, although stronger, are significantly slower to solve.)

If both the sets $\mathcal{X}$ and $\mathcal{Y}$ are polytopes, the convex hull of $\mathcal{S}$ in is also a polytope, and its extreme points are ${{ext}\mathcal{S}} = {\{{({\mathbf{x}},{\mathbf{y}},{{\mathbf{x}}{\mathbf{y}}^{\top}})}:{{{\mathbf{x}} \in {{ext}\mathcal{X}}},{{\mathbf{y}} \in {{ext}\mathcal{Y}}}}\}}$. In general, this yields an exponential-size description of ${conv}\mathcal{S}$. Nevertheless, if the sets $\mathcal{X}$ and $\mathcal{Y}$ have further special structure then specialized techniques can be applied to efficiently generate additional valid inequalities for ${conv}\mathcal{S}$; see, e.g., the techniques developed for network-interdiction problems, pooling problems, bipartite bilinear programs, and bipartite boolean quadratic programs.

The recent work shows how perspective functions can be used to allow the multiplication of nonlinear convex constraints in the RLT algorithm. However, the relaxation in that work is not set based, and requires an explicit analysis of all the possible products of basic cone inequalities.

## Control applications

A main application of the framework presented in this paper is optimal control of discrete-time dynamical systems. In this section we show how two simple control problems can be cast as SPPs in GCS. These examples illustrate some basic modeling techniques that can also be applied to control problems involving more complex discrete decision making.

### Minimum-time control

Consider the linear dynamical system ${\mathbf{s}}_{\tau + 1} = {{{\mathbf{A}}{\mathbf{s}}_{\tau}} + {{\mathbf{B}}{\mathbf{a}}_{\tau}}}$, where ${\mathbf{s}}_{\tau} \in {\mathbb{R}}^{q}$ and ${\mathbf{a}}_{\tau} \in {\mathbb{R}}^{r}$ are the system state and control action at time step $\tau$. Given an initial state ${\mathbf{s}}_{0}$, we look for a sequence of controls that drives the system state to the origin in the minimum number $T$ of time steps. At each time $\tau$, the state and control pair $({\mathbf{s}}_{\tau},{\mathbf{a}}_{\tau})$ is constrained in a compact convex set $\mathcal{D}$.

To formulate this problem as an SPP in GCS we proceed as in Figure 2a. The vertices $\mathcal{V}$ in our graph are ordered in a sequence. The source $s$ is the first vertex and the target $t$ is the last. The number of vertices is equal to $\overline{T} + 1$, where $\overline{T}$ is a given upper bound on the optimal time horizon $T$. Each vertex that is not the target has two outgoing edges: one that connects it to the next vertex in the sequence and one that goes to the target. For each $v \in \mathcal{V}$, the continuous variable ${\mathbf{x}}_{v}$ represents a state and control pair $({\mathbf{s}}_{v},{\mathbf{a}}_{v})$. These variables are constrained by the following sets: $\mathcal{X}_{s}:={\mathcal{D} \cap {({{\{{\mathbf{s}}_{0}\}} \times {\mathbb{R}}^{r}})}}$ for the source, $\mathcal{X}_{t}:={\{{(\mathbf{0},\mathbf{0})}\}}$ for the target (the value of ${\mathbf{a}}_{t}$ is actually irrelevant), and $\mathcal{X}_{v}:=\mathcal{D}$ for all the other vertices. To minimize the number of edges in the optimal path (i.e., the time steps to reach the origin), the length of each edge $(u,v)$ is $1$ if ${\mathbf{s}}_{v} = {{{\mathbf{A}}{\mathbf{s}}_{u}} + {{\mathbf{B}}{\mathbf{a}}_{u}}}$ and infinite otherwise. (See Example 4.6 for the perspective of such a function.)

The solution of the MICP (5.3) gives us a path $p:={(v_{0},\ldots,v_{K})}$. The optimal time horizon is $T:=K$, and the corresponding control sequence is ${\mathbf{a}}_{\tau}:={\mathbf{a}}_{v_{\tau}}$ for $\tau = {0,\ldots,{T - 1}}$. The state trajectory is retrieved similarly, and is such that ${\mathbf{s}}_{T}:={\mathbf{s}}_{t} = \mathbf{0}$.

(b) Control of a PWA system.

Figure 2: Graphs for the formulation of the optimal-control problems in Section 8 as SPPs in GCS.

### Control of hybrid systems

PieceWise-Affine (PWA) systems are a popular framework for modeling hybrid dynamics. Loosely speaking, almost any dynamical system whose nonlinearity is exclusively due to discrete logics can be written in PWA form. Among the many applications of PWA systems, we have automotive, power electronics, and robotics. Given a finite collection ${\{\mathcal{D}_{\nu}\}}_{\nu \in \mathcal{N}}$ of compact convex subsets of the state and control space, a PWA system has dynamics ${\mathbf{s}}_{\tau + 1} = {{{\mathbf{A}}_{\nu_{\tau}}{\mathbf{s}}_{\tau}} + {{\mathbf{B}}_{\nu_{\tau}}{\mathbf{a}}_{\tau}} + {\mathbf{c}}_{\nu_{\tau}}}$ if ${({\mathbf{s}}_{\tau},{\mathbf{a}}_{\tau})} \in \mathcal{D}_{\nu_{\tau}}$. The index $\nu_{\tau} \in \mathcal{N}$ represents the system discrete *mode* at time $\tau$, which is itself a decision variable. We consider the problem of driving a PWA system from a given initial state ${\mathbf{s}}_{0}$ to the origin, in a fixed number $T$ of time steps. The objective is to minimize the sum of the stage costs $\gamma{({\mathbf{s}}_{\tau},{\mathbf{a}}_{\tau})}$ for $\tau = {0,\ldots,{T - 1}}$. The function $\gamma$ is convex and finite.

We model this problem through the GCS in Figure 2b. The source $s$ is the leftmost vertex and the target $t$ is the rightmost. In between, we have $T$ layers with $|\mathcal{N}|$ vertices each. The source is connected via an edge to each vertex in the first layer, and all the vertices in the last layer are connected to the target. Each pair of consecutive layers is fully connected. Also in this case the continuous variables ${\mathbf{x}}_{v}$ represent state and control pairs $({\mathbf{s}}_{v},{\mathbf{a}}_{v})$. The source is paired with the set $\mathcal{X}_{s}:={\{{({\mathbf{s}}_{0},\mathbf{0})}\}}$, the target with $\mathcal{X}_{t}:={\{{(\mathbf{0},\mathbf{0})}\}}$, and the $\nu$th vertex $v$ of each layer with $\mathcal{X}_{v}:=\mathcal{D}_{\nu}$. To enforce the initial conditions, the edges $(s,v)$ outgoing from the source have zero length if ${\mathbf{s}}_{v} = {\mathbf{s}}_{s}$, and infinite length otherwise. (Note that here the values of both ${\mathbf{a}}_{s}$ and ${\mathbf{a}}_{t}$ are irrelevant.) The length of any other edge $(u,v)$, where $u$ is the $\nu$th vertex in its layer, is $\gamma{({\mathbf{s}}_{u},{\mathbf{a}}_{u})}$ if ${\mathbf{s}}_{v} = {{{\mathbf{A}}_{\nu}{\mathbf{s}}_{u}} + {{\mathbf{B}}_{\nu}{\mathbf{a}}_{u}} + {\mathbf{c}}_{\nu}}$ and infinite otherwise.

A shortest path $p:={(v_{0},\ldots,v_{K})}$ has now $T + 2$ vertices. The optimal control at time $\tau = {0,\ldots,{T - 1}}$ is ${\mathbf{a}}_{\tau}:={\mathbf{a}}_{v_{\tau + 1}}$. The state trajectory is defined similarly.

### Remark 8.1

Frequently in optimal control we need to enforce convex terminal constraints of the form $\mathbf{s}_{T} \in \mathcal{D}_{T}$, as well as convex terminal penalties $\gamma_{T}{(\mathbf{s}_{T})}$. These are easily incorporated in our construction through a suitable modification of the set $\mathcal{X}_{t}$ and the lengths of the edges incoming to the target vertex.

### Remark 8.2

The size of the GCS we just constructed is linear in the time horizon $T$ and quadratic in the number $|\mathcal{N}|$ of discrete modes. Conversely, common formulations for these problems have size linear in both $T$ and $|\mathcal{N}|$. We will see in Section 9.3 that the greater strength of our MICPs can be well worth this price.

## Numerical results

This section collects multiple numerical experiments. We start in Section 9.1 with a simple two-dimensional problem. Section 9.2 presents a statistical analysis of the performance of our MICP on large-scale instances of the SPP in GCS. In Section 9.3 we compare our approach with state-of-the-art mixed-integer formulations for control. Finally, in Section 9.4 we use a carefully designed problem to show how symmetries in the GCS can loosen the relaxation of our MICP.

The code necessary to reproduce these results is available at [https://github.com/TobiaMarcucci/shortest-paths-in-graphs-of-convex-sets](https://github.com/TobiaMarcucci/shortest-paths-in-graphs-of-convex-sets). All the experiments are run using the commercial solver MOSEK 10.0 with default options on a laptop computer with processor 2.4 GHz 8-Core Intel Core i9 and memory 64 GB 2667 MHz DDR4. A mature implementation of the techniques presented in this paper is also provided by the open-source software Drake.

### Two-dimensional example

We consider the two-dimensional problem in Figure 3a. We have a graph $G$ with ${|\mathcal{V}|} = 9$ vertices, ${|\mathcal{E}|} = 22$ edges, and multiple cycles. The source $\mathcal{X}_{s}:={\{{\mathbf{θ}}_{s}\}}$ and target $\mathcal{X}_{t}:={\{{\mathbf{θ}}_{t}\}}$ sets are single points, while the remaining regions are full dimensional. The geometry of the sets $\mathcal{X}_{v}$ and the edge set $\mathcal{E}$ can be deduced from Figure 3a. As edge lengths we consider the Euclidean distance and the Euclidean distance squared, whose corresponding shortest paths are shown in Figure 3a in orange and blue. As expected, the first path is almost straight, while the lengths of the segments in the second are better balanced.

In Figure 3b we compare the optimal values of the SPP in GCS, the relaxation of our MICP (5.3), and the relaxation of the McCormick formulation. Both relaxations are Second-Order-Cone Program (SOCPs), and for the McCormick one the bounding boxes $\mathcal{B}_{v}$ are chosen as small as the corresponding sets $\mathcal{X}_{v}$ allow. We run this comparison for different values of a parameter $\sigma > 0$ that controls the volume of the sets $\mathcal{X}_{v}$. The value $\sigma = 1$ corresponds to the GCS in Figure 3a. While for $\sigma \neq 1$ each set $\mathcal{X}_{v}$ is shrunk or enlarged via a uniform scaling, with scale factor $\sigma$, relative to a fixed Chebyshev center of the set.

(a) GCS with sets of nominal size, σ = 1. The optimal solutions for the edge lengths and are shown in orange and blue, respectively.

(b) Optimal values of the SPP in GCS and its convex relaxations as functions of the edge length and the size of the sets.

Figure 3: Two-dimensional SPP in GCS from Section 9.1. The tightness of the convex relaxation of our MICP (5.3) is analyzed for two edge lengths (the Euclidean distance and the Euclidean distance squared ) and different sizes of the sets 𝒳v (parameterized by the scalar σ). As a baseline, we also report the optimal value of the relaxation of the McCormick formulation.

When the edge length is the Euclidean distance, the top panel in Figure 3b shows that our relaxation is exact for all values of $\sigma$. This was expected for $\sigma$ close to zero, since by Remark 5.11 our relaxation is exact when the sets are singletons. Similarly, the problem is trivial for very large $\sigma$, when the regions are so big that, no matter the discrete path we take, we can always reach the target via a straight line. However, that our relaxation is exact for all the intermediate values of $\sigma$ is not an obvious result. The McCormick relaxation is also exact for small $\sigma$, but gives a trivial lower bound of zero when the sets are large.

With the Euclidean length squared, both relaxations are still guaranteed to be tight as $\sigma$ goes to zero. This is confirmed by the bottom panel of Figure 3b. When $\sigma$ is very large, we have seen in Section 3 that our problem is equivalent to the HPP, and the argument from Theorem 3.1 shows that its optimal value is ${{\|{{\mathbf{θ}}_{t} - {\mathbf{θ}}_{s}}\|}_{2}^{2}/K} = 11.6$, where $K = 7$ is the number of edges in the longest $s$-$t$ path in the graph in Figure 3a. A close inspection of the bottom of Figure 3b reveals that, for large $\sigma$, our relaxation yields the lower bound ${{\|{{\mathbf{θ}}_{t} - {\mathbf{θ}}_{s}}\|}_{2}^{2}/{({{|\mathcal{V}|} - 1})}} = 10.1$, which corresponds to the simple inequality $K \leq {{|\mathcal{V}|} - 1}$. (Using a duality argument, it can be verified that our relaxation always recovers this bound.) Conversely, the lower bound provided by the McCormick relaxation is again equal to zero.

### Large-scale random instances

We present a statistical analysis of the performance of our formulation. We generate a variety of random large-scale SPPs in GCS, and we analyze the relaxation tightness and the solution times of the MICP (5.3) as functions of various problem parameters. We stress that generating random graphs representative of the "typical" SPP in GCS we might encounter in practice is a difficult operation. Inevitably, the instances we describe below are not completely representative, and our algorithm might perform worse or better on other classes of random graphs. Our goal here is to show that our MICP is not limited to small-scale problems.

We construct an SPP in GCS as follows. We set $\mathcal{X}_{s}:={\{\mathbf{0}\}}$ and $\mathcal{X}_{t}:={\{\mathbf{1}\}}$. The rest of the sets $\mathcal{X}_{v}$ are axis-aligned cubes with volume $\Lambda$ and center drawn uniformly at random in ${\lbrack 0,1\rbrack}^{n}$. Given a number $|\mathcal{E}|$ of edges, we construct the edge set in two steps. First we generate multiple $s$-$t$ paths such that every vertex $v \neq {s,t}$ is traversed exactly by one path. These are determined via a random partition of the set $\mathcal{V} - {\{ s,t\}}$: the number of sets in the partition (number of paths) is drawn uniformly from the interval $\lbrack 1,{{|\mathcal{V}|} - 2}\rbrack$, and also the number of vertices in each set (length of each path) is a uniform random variable. Then we extend the edge set by drawing edges uniformly at random from the set $\{{{(u,v)} \in \mathcal{V}^{2}}:{{v \neq s},{{u \neq t},{u \neq v}}}\}$ until a desired cardinality $|\mathcal{E}|$ is reached. As edge lengths we consider the Euclidean distance and the Euclidean distance squared, which both make our formulation (5.3) a mixed-integer SOCP.

For each edge length, we first solve $100$ random instances with the following nominal parameters: volume $\Lambda = 0.01$, $n = 4$ dimensions, ${|\mathcal{V}|} = 50$ vertices, and ${|\mathcal{E}|} = 100$ edges. Then we solve four other batches of $100$ problems where, in each batch, a different subset of these parameters is increased by a factor of $5$. Specifically, these additional batches test our formulation in case of large sets $\mathcal{X}_{v}$ ($\Lambda$ from $0.01$ to $0.05$), high dimensions ($n$ from $4$ to $20$), dense graphs ($|\mathcal{E}|$ from $100$ to $500$), and large graphs ($|\mathcal{V}|$ and $|\mathcal{E}|$ from $50$ and $100$ to $250$ and $500$). To give an idea of what these problems look like, the projection onto two dimensions of a GCS generated using the nominal parameters is shown in Figure 4.

Figure 4: Projection onto two dimensions of a random instance of the SPP in GCS from Section 9.2. The problem parameters have nominal value.

Figure 5: Relaxation gap versus MICP solution time for the 500 random instances described in Section 9.2. Two edge lengths are analyzed: the Euclidean distance and the Euclidean distance squared. For each edge length, 100 nominal instances are generated with the nominal problem parameters, and four other batches of 100 instances each are obtained by increasing a different subset of the parameters. Our relaxation is almost always exact with the Euclidean length. While, with the Euclidean length squared, it is more sensitive to the dimension n of the space and the density of the graph G. (Note the different horizontal scales of the two plots.)

Figure 5 shows the relaxation gap (cost gap between the MICP and its relaxation, normalized by the MICP cost) versus the MICP solution time for all the instances described above. As observed in the previous example, the Euclidean edge length results in easier programs: our relaxation is tight in almost all the instances and the solution times are relatively low. The squared edge length leads to more challenging problems, even though the maximum relaxation gap and runtime are only $2.1\%$ and $0.66$s in the nominal case. When the volume of the cubes $\mathcal{X}_{v}$ is increased to $\Lambda = 0.05$ these values increase to $9.1\%$ and $1.12$s, and the performance of our MICP is minimally affected. Note that this is not in contrast with the previous example, where we analyzed the regime of extremely large sets $\mathcal{X}_{v}$. Note also that the volume of the sets does not affect the MICP size. The growth of the space dimension to $n = 20$ increases the size of our programs, and also loosens the relaxation. The largest relaxation gap is $28.9\%$, and our MICP takes $72$s to be solved in the worst case. Similarly, when the number $|\mathcal{E}|$ of edges is increased to $500$ the maximum relaxation gap and runtime become $32.9\%$ and $174$s. This is due to the combination of the quadratic edge length and the large number of cycles that we have in a graph with high density of edges ${|\mathcal{E}|}/{|\mathcal{V}|}$. To show this, in the last batch of problems we keep ${|\mathcal{E}|} = 500$ and we increase the number of vertices to ${|\mathcal{V}|} = 250$. This increases the MICP size further but makes the graph sparser, reducing the maximum relaxation gap and runtime to $5.3\%$ and $5.4$s.

Also for the problems in this analysis our formulation outperforms the McCormick one in. With the nominal parameters, the McCormick median (maximum) runtime is $12.9$ ($4.3$) times larger than ours for the Euclidean length, and $10.3$ ($2.7$) times larger for the Euclidean length squared. This performance difference grows larger for the other batches of problems, where the McCormick formulation reaches our time limit of one hour very often. The slowness of the McCormick approach is due to its loose relaxation: even with the nominal parameters, we have a median (maximum) relaxation gap of $29\%$ ($52\%$) for, and $34\%$ ($58\%$) for.

### Optimal control

We apply the method from Section 8.2 to solve the optimal-control problem shown in Figure 6a. We have a mechanical system with position ${\mathbf{q}} \in {\mathbb{R}}^{2}$, velocity ${\mathbf{v}} \in {\mathbb{R}}^{2}$, and force ${\mathbf{a}} \in {\mathbb{R}}^{2}$. The system has the dynamics of a double integrator: ${\mathbf{q}}_{\tau + 1} = {{\mathbf{q}}_{\tau} + {\mathbf{v}}_{\tau}}$ and ${\mathbf{v}}_{\tau + 1} = {{\mathbf{v}}_{\tau} + {\eta{\mathbf{a}}_{\tau}}}$, where $\eta$ is a scalar parameter that regulates the system controllability. The system state at time $\tau$ is ${\mathbf{s}}_{\tau}:={({\mathbf{q}}_{\tau},{\mathbf{v}}_{\tau})}$. The initial position is ${\mathbf{q}}_{0}:={(0.5,{- 3.5})}$ (green plus at the bottom left of Figure 6a), the initial velocity is ${\mathbf{v}}_{0}:=\mathbf{0}$. At each time step $\tau = {1,\ldots,{T - 1}}$, the position ${\mathbf{q}}_{\tau}$ must belong to one of the seven regions in Figure 6a, while the velocity and the controls are limited by the constraints ${\|{\mathbf{v}}_{\tau}\|}_{\infty} \leq 1$ and ${\|{\mathbf{a}}_{\tau}\|}_{\infty} \leq 1$. The goal is to reach the point ${\mathbf{q}}_{T}:={(6.5,3.5)}$ (green cross at the top right of Figure 6a) with zero velocity ${\mathbf{v}}_{T}$ in $T:=30$ time steps. The cost function is the sum of the stage costs ${\gamma{({\mathbf{s}}_{\tau},{\mathbf{a}}_{\tau})}}:={{{\|{\mathbf{v}}_{\tau}\|}_{2}^{2}/5} + {\|{\mathbf{a}}_{\tau}\|}_{2}^{2}}$.

We let the parameter $\eta$ vary between the seven regions. The five regions in the range ${- 5} \leq q_{2} \leq 5$ (light blue in Figure 6a) have $\eta = 1$. While in the other two regions (red in Figure 6a) we make the system more expensive to control by setting $\eta = 0.1$. Since the parameter $\eta$ varies with the state, the system dynamics is PWA and the control problem falls into the class considered in Section 8.2. The GCS beneath this problem (depicted in Figure 2b) has ${|\mathcal{V}|} = 212$ vertices and ${|\mathcal{E}|} = 1435$ edges, and the convex sets $\mathcal{X}_{v}$ live in ${\mathbb{R}}^{6}$. Also in this case problem (5.3) is a mixed-integer SOCP.

(a) Optimal solution of the control problem.

(b) Solution of the convex relaxation from. The relaxation gap is 93%, and the MICP is solved in 17min.

(c) Solution of our convex relaxation. The relaxation gap is 20%, and the MICP is solved in 7.1s.

Figure 6: Control problem from Section 9.3 of driving a dynamical system from start (green plus) to goal (green cross). The light-blue and red regions have high and low controllability, respectively. The optimal positions qτ are white circles, the optimal controls aτ are blue arrows. The triangles are the auxiliary variables qτν whose convex combination yields qτ. The opacity of the triangles equals the optimal value of the variables bτν that serve as weights in this convex combination.

Figure 6a shows the optimal trajectory $({\mathbf{q}}_{0},\ldots,{\mathbf{q}}_{T})$ (white circles) and the optimal controls $({\mathbf{a}}_{0},\ldots,{\mathbf{a}}_{T - 1})$ (blue arrows). Geometrically, the red regions would be shortcuts to the goal, but the low controllability in these areas makes it too expensive not to fall out of the feasible set. The optimal strategy is then to follow a winding trajectory and incur a cost of $9.37$.

As a baseline, we first solve the problem using the state-of-the-art perspective formulation from \[37, Section 6\] (see also \[34, Section 5.2.2\]). At each time step $\tau$, this expresses the system state ${\mathbf{s}}_{\tau}$ as a convex combination of one auxiliary variable ${\mathbf{s}}_{\tau}^{\nu}$ per region $\nu = {1,\ldots,7}$. The control ${\mathbf{a}}_{\tau}$ is decomposed similarly. When the coefficients $b_{\tau}^{\nu}$ of this combination are required to be binary, the solver is forced to make a hard selection of the region in which the system must be at each time step. When the coefficients $b_{\tau}^{\nu}$ can be fractional, the system evolves according to a convex combination of the dynamics in each region. Figure 6b illustrates the solution of the convex relaxation of this formulation (which, thanks to a perspective reformulation of the stage cost, is also an SOCP). It reports the position ${\mathbf{q}}_{\tau}$, the barely visible controls ${\mathbf{a}}_{\tau}$, and the auxiliary copies ${\mathbf{q}}_{\tau}^{\nu}$ of the position vector. The latter have triangular markers and opacity equal to the value of the indicator $b_{\tau}^{\nu}$. As it can be seen, this relaxation is insensitive to the arrangement of the regions, and its optimal trajectory heads straight to the goal. Also the indicator variables $b_{\tau}^{\nu}$ are uninformative, and take nonzero value in the regions with low controllability (visible triangles in the red regions). The optimal value of this relaxation is $0.67$, which is only $7\%$ of the MICP value ($93\%$ relaxation gap). The MICP solution time is ${1011\text{s}} \approx 17$min.

The convex relaxation of our formulation is much tighter: its optimal value is $7.46$, which is $80\%$ of the MICP value ($20\%$ relaxation gap). This has a dramatic effect on computation times that are now reduced to $7.1$s. To make a plot comparable to Figure 6b we leverage the structure of our GCS in Figure 2b. The equivalent of the indicator variable $b_{\tau}^{\nu}$ is the total flow traversing the $\nu$th vertex in the $\tau$th layer of the graph. Similarly, the position of the same vertex plays the role of the auxiliary variables $({\mathbf{s}}_{\tau}^{\nu},{\mathbf{a}}_{\tau}^{\nu})$, which can then be combined using the coefficients $b_{\tau}^{\nu}$ to get candidate values for the state ${\mathbf{s}}_{\tau}$ and the control ${\mathbf{a}}_{\tau}$. Figure 6c illustrates these values, and shows that the trajectory reconstructed from our relaxation resembles the MICP solution in Figure 6a much more closely. All the markers in the regions with low controllability are now invisible, indicating that our relaxation correctly identifies these as regions of high cost. The visible points ${\mathbf{q}}_{\tau}^{\nu}$ are clustered along the optimal trajectory of the MICP, suggesting that our relaxation contains detailed information about the optimal path to reach the goal.

### Symmetries in the GCS

(a) Optimal solution of the MICP, with the optimal vertex positions connected by orange lines.

(b) Optimal solution of the relaxation. For each edge e = (u,v), the orange line connects the surrogates ${\overline{\mathbf{z}}}_{e}$ and ${\overline{\mathbf{z}}}_{e}^{\prime}$ of the vertex positions xu and xv, and is labeled with the flow ye.

Figure 7: Instance of the SPP in GCS from Section 9.4 that shows how symmetries in the GCS can deteriorate the convex relaxation of our MICP. For the relaxation, the cost contribution of edge e is obtained by multiplying the flow ye by the distance between ${\overline{\mathbf{z}}}_{e}$ and ${\overline{\mathbf{z}}}_{e}^{\prime}$. Since only the mean of ${\overline{\mathbf{z}}}_{}^{\prime}$ and ${\overline{\mathbf{z}}}_{}^{\prime}$ is required to match ${\overline{\mathbf{z}}}_{(3,t)}$, the cost is minimized by moving these two points closer to ${\overline{\mathbf{z}}}_{}$ and ${\overline{\mathbf{z}}}_{}$, respectively.

We conclude by showing how symmetries in the GCS can deteriorate the convex relaxation of our MICP and, in principle, make it arbitrarily loose. We illustrate this through the following carefully designed problem.

We consider the SPP in GCS depicted in Figure 7a. We have an acyclic graph with ${|\mathcal{V}|} = 5$ vertices and ${|\mathcal{E}|} = 5$ edges. All the sets $\mathcal{X}_{v}$ are singletons $\{{\mathbf{θ}}_{v}\}$, except for $\mathcal{X}_{3}$ which is a full-dimensional rectangle. As an edge length, we use the Euclidean distance. Solving this problem, we obtain the optimal path $p = {(s,1,3,t)}$ with length $7.4$ (the symmetric solution $p = {(s,2,3,t)}$ would also be optimal). The corresponding vertex positions are connected by an orange line in Figure 7a.

Figure 7b illustrates the solution of the relaxation of the MICP (5.3). For each edge $e$, we connect the optimal points ${\overline{\mathbf{z}}}_{e}:={{\mathbf{z}}_{e}/y_{e}}$ and ${\overline{\mathbf{z}}}_{e}^{\prime}:={{\mathbf{z}}_{e}^{\prime}/y_{e}}$ with an orange line, labeled in blue with the corresponding flow $y_{e}$. Note that, for $y_{e} > 0$, we have ${{\overset{\sim}{\ell}}_{e}{({\mathbf{z}}_{e},{\mathbf{z}}_{e}^{\prime},y_{e})}} = {\ell_{e}{({\overline{\mathbf{z}}}_{e},{\overline{\mathbf{z}}}_{e}^{\prime})}y_{e}}$, and the vectors ${\overline{\mathbf{z}}}_{e}$ and ${\overline{\mathbf{z}}}_{e}^{\prime}$ are the actual points where the length of the edge $e$ is evaluated. Note also that, by (5.3), we have ${\overline{\mathbf{z}}}_{e} \in \mathcal{X}_{u}$ and ${\overline{\mathbf{z}}}_{e}^{\prime} \in \mathcal{X}_{v}$. The relaxation splits the unit of flow injected in the source into two: half unit is shipped to the target via the top path, the other half via the bottom path. The optimal value of this convex program is $7.0$.

The looseness of the relaxation can be explained as follows. If we denote with $\rho$ the flow traversing edge $$, the flow conservation gives $y_{} = {1 - \rho}$, while the flow through the edge $(3,t)$ is always one. Since the variables ${\overline{\mathbf{z}}}_{}$, ${\overline{\mathbf{z}}}_{}$, and ${\overline{\mathbf{z}}}_{(3,t)}^{\prime}$ are forced to match ${\mathbf{θ}}_{1}$, ${\mathbf{θ}}_{2}$, and ${\mathbf{θ}}_{t}$, respectively, the cost terms in (5.3) corresponding to the edges $$, $$, and $(3,t)$ read

The only constraint that links these variables is (5.3) for $v = 3$, which gives ${{\rho{\overline{\mathbf{z}}}_{}^{\prime}} + {{({1 - \rho})}{\overline{\mathbf{z}}}_{}^{\prime}}} = {\overline{\mathbf{z}}}_{(3,t)}$. When $\rho = {1/2}$, this constraint asks the mean of ${\overline{\mathbf{z}}}_{}^{\prime}$ and ${\overline{\mathbf{z}}}_{}^{\prime}$ to match ${\overline{\mathbf{z}}}_{(3,t)}$, as opposed to forcing either one of the first two points to match the third, as it would be for $\rho \in {\{ 0,1\}}$. Therefore, while keeping their mean equal to ${\overline{\mathbf{z}}}_{(3,t)}$, the points ${\overline{\mathbf{z}}}_{}^{\prime}$ and ${\overline{\mathbf{z}}}_{}^{\prime}$ can move vertically, and get closer to ${\mathbf{θ}}_{1}$ and ${\mathbf{θ}}_{2}$. This reduces the first two terms in, and keeps the third term unchanged.

Although this example leads to a relaxation gap of only $5\%$, a simple variation of it shows that our relaxation can be arbitrarily loose. In particular, if we let $\ell_{(s,1)}:=\ell_{(s,2)}:=0$ and we shift the centers of the sets $\mathcal{X}_{3}$ and $\mathcal{X}_{t}$ to the origin, then the cost of the MICP and its relaxation are reduced to $2$ and $0$, and the relaxation gap becomes $100\%$. Nevertheless, we emphasize that this is a contrived problem, and the instances we encounter in practice lead to these phenomena very rarely.

## Conclusions

In this paper we have introduced the SPP in GCS, a versatile generalization of the classical SPP. Our main contribution is a compact MICP formulation for the solution of this NP-hard problem. Numerical experiments show that the convex relaxation of our formulation is typically very tight, and it enables us to quickly solve large problems to global optimality. We have demonstrated the applicability of the proposed framework to control systems: many optimal control problems are interpretable as SPPs in GCS and, in our tests, the proposed formulation outperforms state-of-the-art techniques for their solution.
