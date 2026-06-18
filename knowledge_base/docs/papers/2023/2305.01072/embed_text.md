## Introduction

Path planning is a problem at the core of almost any autonomous system. Driverless cars, drones, autonomous aircraft, robot manipulators, and legged robots are just a few examples of systems that rely on a path-planning algorithm to navigate in their environment. Path-planning problems can be challenging on many fronts. The environment can be dynamic, i.e., change over time, or uncertain because of noisy sensor measurements. Computation might be subject to strict real-time requirements. Interactions between multiple robots without central coordination can lead to game-theoretic problems. In this paper we consider problems where a single smooth path needs to be found through an environment that is fully known and static, but potentially very large and complicated to navigate through. For example, this is the case for a drone inspecting an industrial plant or a mobile robot transporting packages in a large warehouse.

Figure 1: Path planning for a quadrotor flying through a simulated village. Top. The village, composed of buildings, trees, and bushes. The free space is decomposed using more than ten thousand safe boxes. Bottom. A snapshot of the quadrotor flight. The smooth path connects two opposite corners of the village and is guaranteed to be collision free at all times. The online planning time is only a few seconds.

Like previous methods, we assume that the environment is described as a collection of safe sets, through which our system or robot can move freely without colliding with obstacles. Our problem is to find a smooth path that is contained in the union of the safe sets, and connects given initial and terminal points. We consider the case where the safe sets are axis-aligned boxes and large in number (thousands or tens of thousands). Note that the decomposition of complex environments into boxes can be approximate (conservative), and can be computed using simple variations of existing algorithms, as well as methods tailored to kinematic trees. Focusing on box-shaped safe sets allows us to substantially accelerate multiple parts of our algorithm.

Our path-planning method is composed of an offline and an online part. In the offline preprocessing, we construct a graph that stores the intersections of the safe boxes and solve a convex program to label the edges of this graph with approximate distances. These computations are done only once, since the environment is static, and they require from a fraction of a second to a few tens of seconds, depending on the problem size. In the online part we first use the graph constructed offline to design a polygonal curve of short length that connects the given initial and terminal points. Then we solve a sequence of convex optimal-control problems to transform the polygonal curve into a smooth path that minimizes a given objective function. The online runtimes of our algorithm are dominated by these control problems, which, however, are solvable in a time that increases only linearly with the number of boxes traversed by the path. This results in online planning times on the scale of a hundredth of a second for medium-size problems and of a second for very large problems. Consider that, for a problem like the quadrotor flight in Fig. 1, existing techniques take a few seconds to find a path through less than one hundred safe boxes. Within the same time, our planner designs a path through more than ten thousand boxes.

The proposed algorithm is *complete*: it always finds a smooth path connecting the initial and final positions if such a path exists, and it certifies infeasibility of the planning problem otherwise. In addition, by using Bézier curves for the path parameterization, our smooth trajectories are guaranteed to be safe at all times, and not only at a finite number of sample points. Our method is *heuristic*: although it designs paths that have typically low cost, it is not guaranteed to solve the planning problem optimally, or within a fixed percentage of the optimum. The techniques of this paper are implemented in a companion open-source package, fastpathplanning.

### I-A Related work

A wide variety of path-planning algorithms have been developed over the last fifty years. An excellent overview of the techniques available in the literature can be found in \[24, Part 2\]. Here we review the methods that are most closely related to ours.

The closest approach to the one presented here is GCS (graphs of convex sets) from. Similarly to our method, GCS designs smooth paths through collections of safe sets that are preprocessed to form a graph. Leveraging the optimization framework from, it formulates a tight convex relaxation of the planning problem and it recovers a collision-free trajectory using a cheap rounding strategy. Thanks to this workflow, GCS also provides tight optimality bounds for the trajectories it designs. On the other hand, by trying to solve the planning problem through a single convex program, GCS has a few limitations. First, at present, GCS does not efficiently handle costs or constraints on the path acceleration and higher derivatives, which are a central component of the problems analyzed in this paper. Secondly, GCS does not scale to the very large numbers of safe sets considered here. The proposed algorithm is different in spirit from GCS: it leverages fast graph search to heuristically solve the discrete part of the planning problem and, only at a later stage, it uses convex optimization to shape the continuous path. This division sacrifices the optimality guarantees but retains the algorithm completeness, and it allows us to quickly find paths of low cost for planning problems of very large scale.

A natural approach for designing smooth paths that avoid obstacles optimally is mixed-integer programming. Earlier mixed-integer formulations dealt with polyhedral obstacles, and used a binary variable for each facet of each obstacle to enforce the constraint that a trajectory point is not in collision. Conversely, the formulation from leverages the algorithm from to cover (all or part of) the collision-free space with convex regions, and ensures safety by forcing each trajectory segment to lie entirely in at least one convex region. This makes the mixed-integer program more efficient, since each trajectory segment requires only one binary variable per safe set. The path planning problem considered in is essentially the same as ours, but our algorithm can solve dramatically larger problems in a fraction of the time (see the comparison in §VII-D).

Two popular approaches for collision-free path planning are local nonconvex optimization and sampling-based algorithms. The former methods can handle kinematic and dynamic constraints, but suffer from local minima and can often fail in finding a feasible trajectory if the environment has many obstacles. Although multiple approaches have been proposed to mitigate this issue, sampling-based algorithms are typically more reliable when the environment is complex (in fact, they are *probabilistically complete*). However, sampling-based methods can struggle in high dimensions and are less suitable for the design of smooth paths. Similar to, the approach we propose here can be thought of as a generalization of sampling-based algorithms, where collision-free samples are substituted with collision-free sets. Instead of sampling the environment densely, we fill it with large safe boxes. This reduces the combinatorial complexity to the minimum and allows us to plan through the open space using efficient convex optimization.

Decompositions of the environment into safe sets (or cells) are also common in feedback motion planning. There, a feedback plan is constructed by composing a navigation function with a piecewise-smooth vector field: the former decides the discrete transitions between the cells and the latter causes all states in a cell to flow into the next cell \[24, §8.4\]. In a similar fashion, the method in leverages discrete abstractions to generate provably correct control policies for planar robots moving in polygonal environments. In robust motion planning, funnels, tubes, barrier functions, and positively invariant sets are frequently used to abstract away the continuous dynamics and reduce the planning problem to a discrete search. While similar in spirit to our algorithm, the methods presented in those papers consider problems of different nature from our. We do not aim to synthesize a feedback policy, nor do we reason about dynamics and disturbances explicitly. Our goal is to design safe smooth paths of low cost, and the challenge in our problem is the environment complexity (i.e., the number of safe boxes).

Lastly, in this paper we use Bézier curves to parameterize smooth paths. These curves enjoy several properties that make them particularly well suited for convex optimization, and have been widely used in path planning and optimal control over the last fifteen years.

### I-B Outline

This paper is organized as follows. In §II we state the path-planning problem and give a high-level overview of our algorithm. The algorithm can be broken down into three parts, one offline and two online. The offline preprocessing, which does not use either the endpoints of the path or the specific objective function, is described in §III. The first online phase, illustrated in §IV, finds a polygonal curve of short length that is contained in the safe boxes and connects the given path endpoints. The second online phase, described in §V, transforms the polygonal curve into a safe smooth path of low cost. In §VI we summarize the main properties of our path planner. In §VII we evaluate the performance of our algorithm through multiple numerical experiments. In conclusion, in §VIII, we describe some extensions of our method to more general planning problems.

## Path Planning

In this section we state the path-planning problem and we describe at a high-level the components of our algorithm.

### II-A Problem statement

We consider the design of a smooth path in $\text{𝐑}^{d}$ from a given initial point $p^{init} \in \text{𝐑}^{d}$ to a given terminal point $p^{term} \in \text{𝐑}^{d}$. We represent the path as the function $p:{{\lbrack 0,T\rbrack}\rightarrow\text{𝐑}^{d}}$, where $T$ is the time taken to traverse the path. In addition to the initial and terminal point constraints,

we require that the path stay in a given set $\mathcal{S} \subset \text{𝐑}^{d}$ of safe points:

We assume that the safe set $\mathcal{S}$ is a union of $K$ axis-aligned boxes,

Here the inequalities are elementwise, and the box bounds satisfy $l_{k} \leq u_{k}$ for $k = {1,\ldots,K}$.

We considers paths with $D$ continuous derivatives, and we take our objective to be a weighted sum of the squared $L_{2}$ norm of these derivatives,

where $p^{(i)}$ denotes the $i$th derivative of $p$, and $\alpha_{i}$ are nonnegative weights.

The path-planning problem is

The optimization variable is the path $p$. The problem data are the objective weights $\alpha_{i}$, the final time $T$, the initial and terminal points $p^{init}$ and $p^{term}$, and the safe set $\mathcal{S}$ (specified by the box bounds $l_{k}$ and $u_{k}$). This statement includes only the essential components of a path-planning problem. For example, here we specify the initial and terminal positions, but do not constrain the initial and terminal derivatives. In §VIII we will discuss multiple of these simple extensions, and highlight the necessary modifications to our method.

The path-planning problem is infinite dimensional, but we will restrict candidate paths to piecewise Bézier curves, which are parameterized by a finite set of control points.

### II-B Safety map

Problem has convex quadratic objective, two linear equality constraints, and the safety constraint, which, in general, is not convex. The safety constraint is an infinite collection of disjunctive constraints, that force the point $p{(t)}$, for each $t \in {\lbrack 0,T\rbrack}$, to lie in at least one of the boxes $\mathcal{B}_{k}$. Ensuring safety of a path $p$ is then equivalent to finding a function $s:{{\lbrack 0,T\rbrack}\rightarrow{\{ 1,\ldots,K\}}}$ such that

The value ${s{(t)}} \in {\{ 1,\ldots,K\}}$ represents the choice of a safe box for the path at time $t$, and the overall function $s$ can be thought of as a *safety map* for our path.

Our safety maps will have a finite number of transitions, i.e., will be of the form

where $0 = t_{0} < t_{1} < \cdots < t_{N} = T$. We will refer to $s_{1},\ldots,s_{N}$ as the *box sequence* of the safety map $s$, and to ${T_{1} = {{t_{1} - t_{0}},\ldots}},{T_{N} = {t_{N} - t_{N - 1}}}$ as the *traversal times*.

In terms of the safety map, the path-planning problem is

where the variables are the path $p$ and the safety map $s$. We observe that if the box sequence $s_{1},\ldots,s_{N}$ is fixed, problem reduces to a nonconvex but continuous optimal-control problem, with the path $p$ and the traversal times $T_{1},\ldots,T_{N}$ as decision variables. If we also fix the traversal times, then the safety map is entirely specified, and problem becomes a convex optimal-control problem with quadratic objective and linear constraints.

### II-C Feasibility

We will say that a safety map is *feasible* if it satisfies

The first condition says that the first and last boxes in the box sequence cover the initial and terminal points, respectively. The second condition requires that every two consecutive boxes intersect; thus the box sequence can be traversed by a continuous path.

Importantly, the path-planning problem is feasible if and only if a feasible safety map exists. To see this, note that if a path $p$ and a safety map $s$ are feasible for, then the safety map must satisfy both conditions in. (In particular, the second condition follows from the continuity of $p$, which ensures that ${p{(t_{j})}} \in {\mathcal{B}_{s_{j}} \cap \mathcal{B}_{s_{j + 1}}}$ for all $j = {1,\ldots,{N - 1}}$.) For the other direction, suppose a safety map is feasible, and let $p_{j} \in {\mathcal{B}_{s_{j}} \cap \mathcal{B}_{s_{j + 1}}}$ for $j = {1,\ldots,{N - 1}}$. Then the polygonal curve with nodes $p^{init} = p_{0}$, ${p_{1},\ldots,p_{N - 1},p_{N}} = p^{term}$ is entirely contained in the safe set $\mathcal{S}$. Through the following steps, we construct a path $p$ that has $D$ continuous derivatives, and moves along the polygonal curve (and so is safe). We select any times $0 = t_{0} < t_{1} < \cdots < t_{N} = T$. We choose any smooth time parameterization of the polygonal curve that satisfies the interpolation conditions ${p{(t_{j})}} = p_{j}$ for $j = {0,\ldots,N}$, as well as the derivative constraints ${p^{(i)}{(t_{j})}} = 0$ for $i = {1,\ldots,D}$ and $j = {1,\ldots,{N - 1}}$. While the polygonal curve has kinks, the path $p$ is differentiable $D$ times since it comes to a full stop at each kink. By pairing this path with the feasible safety map, we have a feasible solution of problem.

### II-D Method outline

We give here a high-level description of the three phases in our path-planning algorithm, with the details illustrated in future sections.

### Offline preprocessing

The offline preprocessing uses only the safe set $\mathcal{S}$, i.e., the safe boxes $\mathcal{B}_{1},\ldots,\mathcal{B}_{K}$. In this phase we construct a *line graph* $G$ whose vertices correspond to points in the intersection of two boxes, and whose edges connect pairs of points that lie in the same box. When considered as a subset of $\text{𝐑}^{d}$, this graph lies entirely in the safe set, and it can be used to quickly design safe polygonal curves that connect given initial and terminal points. The points associated with the vertices are called *representative points*, and are optimized to minimize the total Euclidean length of the edges in the line graph. This serves as a heuristic to reduce the length of the polygonal curves.

1:procedure Offline Preprocessing

2: compute intersections of safe boxes $\mathcal{B}_{1},\ldots,\mathcal{B}_{K}$

3: construct line graph $G$

4: optimize representative points

### Polygonal phase

Here we find a polygonal curve $\mathcal{C}$ that connects $p^{init}$ to $p^{term}$, is entirely contained in the safe set $\mathcal{S}$, and has small length. The curve is initialized by solving a shortest-path problem in the line graph constructed offline. Then it is shortened through an iterative process, where we alternate between minimizing the curve length for a fixed box sequence, and updating the box sequence for a fixed polygonal curve.

1:procedure Polygonal Phase

2: connect $p^{init}$ to $p^{term}$ with safe polygonal curve $\mathcal{C}$

3: while not converged do

4: fix box sequence $s_{1},\ldots,s_{N}$ and shorten curve

5: fix curve and improve box sequence

### Smooth phase

In this phase we freeze the box sequence $s_{1},\ldots,s_{N}$ identified in the polygonal phase, and traversed by the curve $\mathcal{C}$. As observed above, this reduces problem to a continuous but nonconvex optimal-control problem. To solve this control problem, we first use a simple heuristic to estimate initial traversal times $T_{1},\ldots,T_{N}$. Then we alternate between two convex optimal-control problems. In the first, we fix the traversal times (thus we specify the whole safety map $s$) and optimize the shape of the path. In the second, we attempt to improve the traversal times by solving a local convex approximation of the nonconvex optimal-control problem.

1:procedure Smooth Phase

2: fix box sequence $s_{1},\ldots,s_{N}$

3: estimate traversal times $T_{1},\ldots,T_{N}$

4: while not converged do

5: fix traversal times and optimize path $p$

6: attempt improvement of traversal times

## Offline Preprocessing

In this section we describe the offline part of our algorithm. The steps below are also illustrated through a simple example at the end of the section.

### III-A Line graph

We start by computing the line graph associated with the safe boxes. The vertices of this graph are pairs of safe boxes that intersect, and the edges connect pairs of intersections that share a box. Formally, the line graph is an undirected graph $G = {(\mathcal{V},\mathcal{E})}$ with vertices

The name line graph is motivated by the fact that $G$ can be equivalently defined as the line graph of the *intersection graph* of our collection of boxes.

The line graph allows us to efficiently construct polygonal curves that are guaranteed to be safe. Consider a path in the line graph. For each vertex in this path, choose a point in $\text{𝐑}^{d}$ in the corresponding box intersection. Then form the polygonal curve passing through these points. Each line segment in this curve is associated with an edge in the line graph, and therefore with a safe box. By construction, this safe box contains the line segment entirely. It follows that the whole polygonal curve is safe.

Since computing the intersection of two boxes is a trivial operation, we can construct the line graph $G$ very efficiently, even when the number $K$ of boxes is very large. Our implementation is based on the technique from \[60, §2\].

### III-B Representative points

Figure 2: Offline preprocessing of the safe boxes. Left. Safe boxes. Center left. Pairwise intersections of the safe boxes. Center right. Line graph, with vertices in the box intersections and edges connecting intersections that share a box. Right. Line graph with optimized representative points.

Our next step is to choose a representative point for each vertex of the line graph, i.e., for each pair of intersecting boxes. As a heuristic method to shorten the polygonal curves constructed as described above, we position these points close to their neighbors in the line graph. More formally, denoting with $x_{v} \in \text{𝐑}^{d}$ the representative point of vertex $v \in \mathcal{V}$, we minimize the sum of the Euclidean distances between all pairs of representative points that are connected by an edge:

Here the variables are the representative points $x_{v}$, $v \in \mathcal{V}$. Each of these points is constrained in the corresponding box intersection, which is itself an axis-aligned box. This is a convex optimization problem that can be represented as a second-order cone program (SOCP) and efficiently solved \[41, §4.4.2\],.

After optimizing the position of the representative points $x_{v}$ as in, each edge $\{ v,w\}$ of the line graph is assigned the weight ${\|{x_{v} - x_{w}}\|}_{2}$.

### III-C Example

We illustrate the offline preprocessing on a small problem that will serve as a running example throughout the paper. This problem has $K = 9$ safe boxes in $d = 2$ dimensions and is depicted in Fig. 2. The left figure shows the safe boxes, and the center left figure shows their intersections (with some overlapping when more than two boxes intersect). These intersections correspond to the ${|\mathcal{V}|} = 11$ vertices of the line graph. In the center right figure, we show the ${|\mathcal{E}|} = 20$ edges of the line graph as line segments connecting the centers of the box intersections. The right figure shows the optimized representative points, which minimize the total Euclidean distance over the edges of the line graph, i.e., a solution of. Note that some of the $20$ edges overlap in this figure. Observe also that the line graph, considered as a subset of $\text{𝐑}^{2}$, is entirely contained in the safe set, since each edge is in at least one safe box.

## Polygonal Phase

We now describe the first online phase of our algorithm, where we design a safe polygonal curve $\mathcal{C}$ of short length that connects $p^{init}$ to $p^{term}$. An illustration of the steps below can be found at the end of the section, where we continue our running example.

### IV-A Shortest-path problem

We use the line graph $G$ to initialize the polygonal curve $\mathcal{C}$. We augment the line graph with two new vertices with representative points $p^{init}$ and $p^{term}$. An edge is added between $p^{init}$ and all the intersections of safe boxes that contain $p^{init}$, i.e., all the vertices ${\{ k,l\}} \in \mathcal{V}$ such that $p^{init} \in \mathcal{B}_{k}$ or $p^{init} \in \mathcal{B}_{l}$. An analogous operation is done for $p^{term}$. As for the other edges in the line graph, these new edges are assigned a weight equal to the Euclidean distance between the representative points that they connect. We then find a shortest path from the initial point to the terminal point, and recover an initial polygonal curve $\mathcal{C}$ by connecting the representative points along this path. As noted above, this curve is safe because each of its segments is contained in a safe box.

This shortest-path step determines whether or not our path-planning problem is feasible. If there is no path in the augmented line graph between the vertices associated with $p^{init}$ and $p^{term}$, then the path-planning problem is infeasible. Conversely, if there is a path between these two vertices, then the path-planning problem is feasible since a feasible trajectory can be constructed as in §II-C.

The problem of identifying all the safe boxes that contain the initial and terminal points is known as *stabbing problem* and, given the precomputations done to construct the line graph, it takes negligible time. Using an optimized implementation of Dijkstra's algorithm (e.g., the one provided by scipy ), finding a shortest path is also very fast.

### IV-B Shortening of the polygonal curve

Thanks to the optimization of the representative points in, our initial polygonal curve $\mathcal{C}$ is typically short. However, the online knowledge of the initial and terminal points, which were unknown during the preprocessing, can allow us to shorten this curve further. This is done iteratively: we alternate between solving a convex program that minimizes the curve length for a fixed box sequence, and improving the box sequence for a fixed polygonal curve.

### Optimization of the polygonal curve

Denote with $\mathcal{C}$ the curve at the current iteration (initialized with the solution of the shortest-path problem). Let $N$ be the number of segments in $\mathcal{C}$ and ${y_{0},\ldots,y_{N}} \in \text{𝐑}^{d}$ be the curve nodes, with $y_{0} = p^{init}$ and $y_{N} = p^{term}$. For $j = {1,\ldots,N}$, let also $s_{j}$ be the index of the safe box that covers the line segment between $y_{j - 1}$ and $y_{j}$. We fix the box sequence $s_{1},\ldots,s_{N}$ traversed by the current curve, and we optimize the position of the nodes $y_{j}$ so that the length of the curve is minimized. This leads to the problem

with variables $y_{0},\ldots,y_{N}$. This is a small SOCP with banded constraints that can be solved very efficiently, in time that is only linear in the number $N$ of segments.

The optimal nodes from define our new curve $\mathcal{C}$. We will assume that these nodes are distinct, since if two nodes coincide we can always eliminate one.

### Improvement of the box sequence

After solving problem, the nodes $y_{0},\ldots,y_{N}$ minimize the curve length for the given box sequence $s_{1},\ldots,s_{N}$. However, as Fig. 3 illustrates, the insertion of a new box can potentially give us room to further shorten our polygonal curve. In our second step, we seek a new sequence of boxes that contains the current curve and is guaranteed to yield a length decrease. Since our safe sets are boxes, this step will be extremely quick.

Figure 3: Shortening of the polygonal curve 𝒞 through the insertion of a new box (ℬk in green) in the current box sequence.

For all $j = {1,\ldots,{N - 1}}$, we solve a stabbing problem to find all the boxes $\mathcal{B}_{k}$ that contain the curve node $y_{j}$. Then we consider inserting the index $k$ between $s_{j}$ and $s_{j + 1}$ in our box sequence. As shown in Fig. 3, this insertion leads to a new instance of problem where the variable $y_{j}$ is replaced by two variables:

Choosing $z_{1} = z_{2} = y_{j}$ gives us a feasible solution of this new instance of, and does not change the length of our curve $\mathcal{C}$. Therefore the insertion of $\mathcal{B}_{k}$ leads to a shorter curve if and only if this feasible solution is not optimal.

We fix $z_{1} = z_{2} = y_{j}$ and check if the optimality conditions of the new instance of can be satisfied. As explained in §A, this check reduces to finding a vector $\lambda \in \text{𝐑}^{d}$ that satisfies the following inequalities:

Here the vectors ${\lambda_{1},\lambda_{2}} \in \text{𝐑}^{d}$ are fixed and given by

The matrices $L_{1}$ and $U_{1}$ select the indices of the inactive inequalities in the box constraint $y_{j} \in {\mathcal{B}_{s_{j}} \cap \mathcal{B}_{k}}$ ($L_{1}$ for the lower bounds and $U_{1}$ for the upper bounds). Similarly, $L_{2}$ and $U_{2}$ select the inactive inequalities in $y_{j} \in {\mathcal{B}_{k} \cap \mathcal{B}_{s_{j + 1}}}$.

Checking if the inequalities in are satisfiable is very quick. In fact, since $L_{1}$, $L_{2}$, $U_{1}$, and $U_{2}$ are selection matrices, the corresponding inequalities in simply impose bounds on a subset of the entries of $\lambda$. We express these bounds as $c_{1} \leq \lambda \leq c_{2}$, for two suitable vectors $c_{1} \in {({\text{𝐑} \cup {\{{- \infty}\}}})}^{d}$ and $c_{2} \in {({\text{𝐑} \cup {\{\infty\}}})}^{d}$. Then the vector $\lambda$ of minimum Euclidean norm that lies within these bounds can be computed as

where the minimum and maximum are elementwise. We conclude that $\lambda^{\star}$ has norm greater than one if and only if the system of inequalities has no solution, which is equivalent to the insertion of the box $\mathcal{B}_{k}$ shortening our curve $\mathcal{C}$.

For each index $j = {1,\ldots,{N - 1}}$ such that the norm of $\lambda^{\star}$ is greater than one, we insert a new box in our sequence. If multiple boxes satisfy this condition for the same index $j$, we select one for which the norm of $\lambda^{\star}$ is largest (this heuristic is motivated in §A). After updating the box sequence, we optimize the curve $\mathcal{C}$ by solving the new instance of problem. This process is iterated until the condition above fails for every curve node $j$ and every box $k$.

### IV-C Example

Figure 4: Polygonal phase of the algorithm. Left. Line graph augmented with pinit and pterm, shown as black disks. Center left. Shortest path from pinit to pterm. Center right. The safe box sequence is fixed and the polygonal curve is shortened via convex optimization. Right. A new box (shown in green) is inserted in the sequence and the curve is shortened a second time. Since no further shortening is possible, the polygonal phase converges in one iteration.

Fig. 4 continues our running example, and illustrates the construction of the polygonal curve. The initial position $p^{init}$ and terminal position $p^{term}$ are shown as black disks in the bottom left and bottom right, respectively. The left figure shows the augmented line graph, where these two points are connected to their adjacent vertices. The initial point $p^{init}$ has two adjacent vertices, while the terminal point $p^{term}$ has only one. The center left figure shows the shortest path from the initial point to the terminal point. In the center right figure, we fix the boxes that the curve must traverse, and we minimize the curve length by solving the SOCP. In the right figure, a new box is inserted in the box sequence and the curve nodes are optimized again. In this example the polygonal phase converges in a single iteration.

## Smooth Phase

The smooth phase is the final phase of our algorithm. It starts from the polygonal curve $\mathcal{C}$ and constructs a smooth path $p$ that is feasible for our planning problem, and has small objective value. For the path parameterization we use a piecewise Bézier curve, i.e., a sequence of Bézier curves that connect smoothly. (Sometimes this is also called a composite Bézier curve.) We start this section by reviewing some basic properties of this family of curves. Next we describe the optimal-control problems that we solve to design our smooth path. Finally, we conclude our running example.

### V-A Bézier curves

A Bézier curve is constructed using Bernstein polynomials. The Bernstein polynomials of degree $M$ are defined over the interval ${\lbrack a,b\rbrack} \subset \text{𝐑}$, with $b > a$, as

For $t \in {\lbrack a,b\rbrack}$ the Bernstein polynomials are nonnegative and, by the binomial theorem, they sum up to one. Therefore, the scalars ${\beta_{0}{(t)}},\ldots,{\beta_{M}{(t)}}$ can be thought of as the coefficients of a convex combination. Using these coefficients to combine a given set of *control points* ${\gamma_{0},\ldots,\gamma_{M}} \in \text{𝐑}^{d}$, we obtain a Bézier curve:

The Bézier curve $\gamma:{{\lbrack a,b\rbrack}\rightarrow\text{𝐑}^{d}}$ is a polynomial function of degree $M$. An example of a Bézier curve is shown in Fig. 5, for $d = 2$ and $M = 4$. Below we list some important properties that we will use later in this section.

### Endpoints

A Bézier curve starts at its first control point and ends at its last control point, i.e.,

With this property, a piecewise Bézier curve (our path) can be made continuous simply by equating the last control point of each curve piece with the first control point of the next piece.

### Control polytope

Since each point on a Bézier curve is a convex combination of the control points, the entire curve is contained in the convex hull of the control points:

for all $t \in {\lbrack a,b\rbrack}$. This convex hull is called the *control polytope* of the Bézier curve $\gamma$. From this property it follows that if all control points lie in a convex set (in our case a box), then so does the Bézier curve.

### Derivatives

The derivative $\gamma^{}$ of a Bézier curve $\gamma$ is also a Bézier curve. It has degree $M - 1$ and its control points are given by the difference equation

Iterating this, we see that the derivative $\gamma^{(i)}$ of any order $i \geq 1$ is a Bézier curve of degree $M - i$. Moreover, the derivatives of a piecewise Bézier curve are also piecewise Bézier curves, and their continuity can be enforced using the endpoint property.

### Squared $L_{2}$ norm

The square of the $L_{2}$ norm of a Bézier curve $\gamma$ can be expressed as a function of the control points using the following expression \[63, §3.3\]:

where $Q$ is a convex quadratic function defined as

This formula allows us also to compute the squared $L_{2}$ norm of a piecewise Bézier curve and its derivatives.

Figure 5: Bézier curve with control points γ0, …, γM, M = 4. The curve starts at γ(a) = γ0, ends at γ(b) = γM, and is entirely contained in the convex hull of the control points, shown shaded.

### V-B Nonconvex optimal-control problem

In the smooth phase we limit our attention to paths that are piecewise Bézier curves and traverse the same box sequence $s_{1},\ldots,s_{N}$ as the curve $\mathcal{C}$. This reduces the path-planning problem to an optimal-control problem that is finite dimensional and has only continuous variables, but is nonconvex. This subsection illustrates this control problem, and the next subsection describes our approach to its solution.

### Variables

The variables in problem are the safety map $s$ and the path $p$. Here the box sequence is fixed, therefore a safety map is specified only through the traversal times $T_{1},\ldots,T_{N}$, which are the first variables in our control problem. For the path parameterization we use a piecewise Bézier curve with $N$ pieces (one per safe box that our path must traverse). Each piece, or subpath, is a Bézier curve

These Bézier curves have degree equal to $M$, and their control points,

are the second group of variables in our control problem.

For $i = {1,\ldots,D}$, the derivatives $p_{j}^{(i)}$ of the subpaths are Bézier curves of degree $M - i$. Our last set of variables are the control points these derivatives:

For simplicity of notation, we will sometimes denote the control points in as $p_{j,0}^{},\ldots,p_{j,M}^{}$, where the superscript represents the zeroth derivative.

### Constraints

We assemble the constraints of our control problem by leveraging the properties of the Bézier curves.

Using the endpoint property, the boundary conditions in problem are enforced simply as

Similarly, the continuity and differentiability of our path are enforced as

Property tells us that a Bézier curve lies within its control polytope. Therefore, to ensure that a subpath $p_{j}$ is entirely contained in the corresponding safe box $\mathcal{B}_{s_{j}}$, it is sufficient to constrain its control points:

Since each subpath $p_{j}$ is constrained in a safe box, the whole piecewise Bézier curve $p$ will be safe.

The control points of the subpath derivatives need to satisfy a difference equation analogous to:

Note that these equality constraints are nonlinear, since both the control points and the traversal times are variables in our optimization problem.

Lastly, the traversal times need to be positive,

and sum up to the final time,

### Objective function

We split the integrals in our objective function into the sum of $N$ terms (one per subpath):

We use to express each term as a function of the control points and the traversal times:

for $i = {1,\ldots,D}$ and $j = {1,\ldots,N}$. Note that the quadratic function $Q$ is convex, but its product with the traversal time $T_{j}$ makes our objective nonconvex.

### Optimization problem

Collecting all the components, we obtain the optimization problem

This program has the structure of an optimal-control problem where the difference equation acts as a dynamical system that links the variables over time. Together with the nonconvex objective terms, this nonlinear difference equation makes the problem nonconvex. However, similarly to its infinite-dimensional counterpart, this problem simplifies to a convex quadratic program (QP) \[41, §4.4\] if we fix the traversal times. In fact, this makes the difference equation linear and the objective function convex quadratic.

### Curve degree and feasibility

If the degree of the subpaths satisfies $M \geq {{2D} + 1}$, then problem is guaranteed to be feasible. In fact, similarly to the discussion in §II-C, this minimum degree ensures that each subpath can be a line segment, with the first $D$ derivatives equal to zero at the endpoints. The overall path $p$ can then take the shape of the safe polygonal curve $\mathcal{C}$, while satisfying the differentiability constraints. Note also that the degree $M$ must be at least $D + 1$, since the continuity and differentiability constraints fix the value of $D + 1$ control points per subpath. In the rest of this paper we will use curves of degree $M = {{2D} + 1}$, so that problem will always be feasible. Although, in practice, we have found that also values of $M$ closer to $D + 1$ almost always yield feasible problems.

### V-C Solution via convex alternations

We solve the nonconvex program by alternating between a *projection problem* and a *tangent problem*, both of which are convex optimal-control problems. As the other parts of our planning method, this step is heuristic: it is guaranteed to find a feasible solution of, but this solution needs not to be optimal.

### Initialization

We start by computing an initial estimate of the traversal times $T_{1},\ldots,T_{N}$ that satisfies the constraints and. To do so, we imagine travelling along the polygonal curve $\mathcal{C}$ at constant speed. The window of time $T_{j}$ that we allocate for the $j$th box is then equal to the distance between the nodes $y_{j}$ and $y_{j - 1}$, divided by the total length of the curve $\mathcal{C}$ and multiplied by the final time $T$.

Although this heuristic is very simple, we have found that it works well for most problems. More precise initial estimates of the traversal times are certainly possible but, in our experience, they are rarely worth their increased complexity.

### Projection problem

In this step we fix the current value of the traversal times (initialized as just described) and we solve the control problem. As observed above this is a convex QP, which has the effect of projecting the current iterate onto the nonconvex feasible set of. Thanks to their optimal-control structure and their banded constraints, these QPs are solvable in a time that grows only linearly with the number $N$ of boxes traversed by our path.

### Tangent problem

In this step we attempt to improve the estimate of the traversal times by solving a convex approximation of.

Let us introduce auxiliary variables that represent the products of the traversal times and the control points of the path derivatives:

for $i = {1,\ldots,D}$, $j = {1,\ldots,N}$, and $n = {0,\ldots,{M - i}}$. Using these variables, the nonlinear difference equation becomes linear,

and the nonconvex objective terms become quadratic over linear \[41, §3.2.6\],

(Recall that quadratic-over-linear functions, with the numerator convex and the denominator positive, are convex and representable through a second-order cone \[61, §2.3\].)

The only nonconvexity left in our problem is the nonlinear equality constraint, which we simply linearize around the current traversal times ${\overline{T}}_{j}$ and control points ${\overline{p}}_{j,n}^{(i)}$ (obtained by solving the projection problem):

Since this linearization might be inaccurate away from the nominal point, we also add a trust-region constraint

This sets a limit of $\kappa > 0$ to the maximum relative variation of the traversal times.

The resulting problem is an SOCP that approximates the nonconvex program locally, and tries to improve the current solution by taking a step in the tangent space of the nonlinear equation. Like the projection problem, it can be solved in a time that increases only linearly with $N$. From its solution we only retain the optimal traversal times $T_{1}^{\star},\ldots,T_{N}^{\star}$, and then we solve a new projection problem to obtain a new feasible path. If the optimal objective value decreases, compared to the previous projection problem, we accept the new times and update our path. Otherwise we keep the previous times and path.

### Trust region update

After each iteration, independently of its success, we decrease the value of the trust-region parameter $\kappa$. A simple way to do so would be to divide $\kappa$ by a parameter $\omega > 1$. However, using this rule, we might have that two consecutive iterations produce the same unsuccessful update of the traversal times. Specifically, if one iteration is unsuccessful and the transition times computed in the tangent problem are not at the boundary of the trust region, then these times might still be feasible (and thus optimal) after we shrink the trust region. To prevent this phenomenon, we use a slightly more sophisticated update:

Here $\kappa$ and $\kappa^{+}$ are the current and the updated trust-region parameters, respectively. The term in the parenthesis is the minimum value of $\kappa$ that, in hindsight, would have activated at least one of the trust-region constraints. If one of these constraints was already active, then this rule reduces to $\kappa^{+} = {\kappa/\omega}$. If none of the trust-region constraints was active, and the iteration was unsuccessful, then the trust region is shrunk enough to make the solution of the last tangent problem infeasible for the next.

### Termination

The tangent problem has optimal value smaller than or equal to its preceding projection problem. We terminate our algorithm when this gap, normalized by the cost of the projection problem, is smaller than a fixed tolerance $\varepsilon > 0$. In which case, we solve one last projection problem and we return the best path that we have found.

### Choice of the parameters

We have found that for most problems the value of $\kappa$ can be simply initialized to one. Large values of $\omega$ (e.g., $\omega = 5$) tend to work well when our initialization of the traversal times is accurate, while smaller values (e.g., $\omega = 2$) are more effective otherwise. In the numerical experiments discussed in this paper we use $\omega = 3$. For the termination tolerance a reasonable choice is $\varepsilon = 10^{- 2}$.

### V-D Example

Figure 6: Smooth phase of our algorithm. Left. The curve from the polygonal phase with the corresponding sequence of safe boxes. Center left. The polygonal curve is used to estimate initial traversal times and a first smooth path is optimized. For each box traversed by the path, the labels show the traversal time (normalized by the final time) at the top, and the cost of the trajectory piece at the bottom. The red shaded sets are the control polytopes of the Bézier curves. Center right. The traversal times are improved and the path is optimized a second time. Right. The path at the last (fourth) iteration, whose cost is within 0.01% of the global minimum.

We conclude our running example by illustrating the smooth phase of the path-planning algorithm. We seek a path that is $D = 3$ times continuously differentiable, and has total duration $T$ equal to one. We use Bézier curves of degree $M = {{2D} + 1} = 7$. We take objective weights $\alpha_{1} = \alpha_{2} = 0$ and $\alpha_{3} > 0$, i.e., our objective penalizes the squared $L_{2}$ norm of the third derivative (or jerk) of the path. To simplify the analysis, the weight $\alpha_{3}$ is chosen so that the global minimum of the problem is equal to one.

In the left of Fig. 6 we have the curve computed in the polygonal phase, with the corresponding sequence of safe boxes highlighted in cyan. In the center left of Fig. 6 we show the path obtained by solving the first projection problem, with the traversal times initialized using the constant-velocity heuristic. Each box traversed by the path is labeled with two numbers: the percentage on top is the ratio between the traversal time $T_{j}$ of that box and the final time $T$; the number at the bottom is the cost $J_{3,j}$ of the subpath $p_{j}$. The red shaded areas are the Bézier control polytopes within each box. We solve the tangent problem, we update the traversal times, and we solve the projection problem a second time. The resulting path is depicted in the center right of Fig. 6. After four iterations the smooth phase terminates, with the resulting path depicted in the right of Fig. 6.

The initial path (center left) has cost $12.04$. The path after the first iteration (center right) has cost $1.27$, which is $89\%$ smaller. The final path (right) has cost $1.0001$, and is essentially the global minimum of the problem. Although our simple heuristic to initialize the traversal times was not accurate, our algorithm converges in very few iterations.

## Algorithm Efficiency and Guarantees

We briefly summarize the main properties of our path-planning method.

### Completeness

Our algorithm is complete: it finds a safe smooth path connecting the initial and final positions if such a path exists, and it certifies infeasibility otherwise. Feasibility is decided almost immediately with the solutions of the shortest-path problem at the beginning of the polygonal phase. If this problem is infeasible, then the initial and terminal points cannot be connected by a continuous curve. Conversely, if the shortest-path problem is feasible, then our algorithm can always recover a smooth feasible path as described at the end of §V-B. Of course, if the safe boxes approximate a more complex space, then the completeness of our method is up to the conservatism of this approximation.

### Suboptimality

Our algorithm is heuristic, and not guaranteed to solve problem optimally (or within a fixed optimality tolerance). In practice, the main source of suboptimality is the choice of the box sequence, which is frozen after the polygonal phase, and does not take into account the actual objective of our path-planning problem. Solving the nonconvex problem is another source of suboptimality, and our alternating method in §V-C is designed to prioritize a low number of iterations over the cost of the final path. Two other (milder) approximations are the path parameterization using Bézier curves, and the sufficiency of the safety constraint.

Some heuristic steps in our path planner do not contribute to the algorithm completeness, but can play an important role in limiting the optimality losses just described. For example, we could take the centers of the box intersections as representative points, instead of optimizing them as in. However, the downstream shortest-path problem would typically select less efficient box sequences with this choice. Two other main heuristic components of our method are the iterative shortening of the polygonal curve in §IV-B and the initialization of the traversal times in §V-C.

### Runtimes

The offline and online runtimes of our method are dominated by the convex optimization problems. The SOCP is the preprocessing step that takes most time, but is efficiently solvable even for path-planning problems of very large scale. In addition, we note that this subproblem only needs to be solved to modest, or even low, accuracy. The SOCP in the polygonal phase takes negligible time, since it is very small and has banded constraints. Furthermore, this phase usually converges within four or five iterations. (More formally, the iterations of this phase can be bounded by the number $K$ of safe boxes; since each iteration adds at least one box to our sequence, and box repetitions are not optimal). The projection QPs and the tangent SOCPs in the smooth phase can be large problems, but they take a time that is only linear in the number of traversed boxes and can be solved to modest precision. Note also that the trust region shrinks geometrically during the iterations of the smooth phase. Therefore, after a handful of iterations (typically four to eight with the parameters given in §V-C) the projection and the tangent problems are essentially identical, and the smooth phase terminates.

## Numerical Experiments

In this section we analyze the performance of our method through multiple numerical experiments. Every experiment was run using the default values in our software implementation fastpathplanning, which we briefly describe below. The computations were carried out on a computer with 2.4 GHz 8-Core Intel Core i9 processor and 64 GB of RAM.

For code readability and fast prototyping, the current version of fastpathplanning uses CVXPY to construct the convex optimization problems and pass them to the solver. This introduces an overhead that for some problems can be even a few times larger than the actual solver times. Since by communicating directly with the solver this overhead can be made negligible, the time spent within CVXPY has been eliminated from the runtimes reported in this paper.

### VII-A Software package

The algorithm presented in this paper is implemented in the open-source Python software package fastpathplanning, which is available at [https://github.com/cvxgrp/fastpathplanning](https://github.com/cvxgrp/fastpathplanning). For the graph computations (e.g., the construction of the line graph) we use NetworkX 3.2. For the solution of the shortest-path problem in the line graph we use scipy 1.11.3. The convex optimization problems are specified using CVXPY 1.4.1, and solved with the Clarabel 0.6.0 solver.

The following is a basic example of the usage of fastpathplanning.

[⬇](data:text/plain;base64,aW1wb3J0IGZhc3RwYXRocGxhbm5pbmcgYXMgZnBwCgojIG9mZmxpbmUgcHJlcHJvY2Vzc2luZwpMID0gLi4uICMgbG93ZXIgYm91bmRzIG9mIHRoZSBzYWZlIGJveGVzClUgPSAuLi4gIyB1cHBlciBib3VuZHMgb2YgdGhlIHNhZmUgYm94ZXMKUyA9IGZwcC5TYWZlU2V0KEwsIFUpCgojIG9ubGluZSBwYXRoIHBsYW5uaW5nCnBfaW5pdCA9IC4uLiAjIGluaXRpYWwgcG9pbnQKcF90ZXJtID0gLi4uICMgdGVybWluYWwgcG9pbnQKVCA9IDEgIyBmaW5hbCB0aW1lCmFscGhhID0gWzEsIDEsIDVdICMgY29zdCB3ZWlnaHRzCnAgPSBmcHAucGxhbihTLCBwX2luaXQsIHBfdGVybSwgVCwgYWxwaGEpCgojIGV2YWx1YXRlIHNvbHV0aW9uCnQgPSAwLjUgIyBzYW1wbGUgdGltZQpwX3QgPSBwKHQp){download=""}

1import fastpathplanning as fpp

4L = \... # lower bounds of the safe boxes

5U = \... # upper bounds of the safe boxes

8# online path planning

9p_init = \... # initial point

10p_term = \... # terminal point

12alpha = # cost weights

13p = fpp.plan(S, p_init, p_term, T, alpha)

The matrices L and U contain the lower bound $l_{k}$ and the upper bound $u_{k}$ of each safe box $\mathcal{B}_{k}$, $k = {1,\ldots,K}$. These have dimension $K \times d$, and are not explicitly defined in the code above. In line 6 they are used to instantiate the safe set $\mathcal{S}$ (as the object S). This line is where the offline preprocessing is done, i.e., we construct the line graph and optimize the representative points. In line 13 the function plan finds a smooth path p, given the safe set, initial and terminal points, final time, and objective coefficients. The number $D$ of continuous derivatives that our path will have is equal to the length of the list alpha. By default, the degree of the Bézier curves is set to $M = {{2D} + 1}$. The path object p can be called like a function by passing a time $t \in {\lbrack 0,T\rbrack}$ as in line 17. (It also contains other attributes such as the list of Bézier control points and the safe boxes $s_{1},\ldots,s_{N}$ that the path traverses.)

### VII-B Scaling study

In our first example we consider path-planning problems in $d = 2$ dimensions, and analyze the performance of our algorithm as a function of the number $K$ of safe boxes.

We generate an instance of problem as follows. We construct a square grid with $P^{2}$ points with integer coordinates ${\{ 1,\ldots,P\}}^{2}$. We let each point in this grid be the center of a safe box $\mathcal{B}_{k}$. Each box elongates either horizontally or vertically, with equal probability. The short and long sides of a box are drawn uniformly at random from the intervals $\lbrack 0,0.5\rbrack$ and $\lbrack 0,2\rbrack$, respectively.

We use this procedure to generate six feasible path-planning problems with grids of side $P = {5,10,20,40,80,160}$. The number of boxes in these problems is then

The final time is taken to be $T = P$ and the cost weights are $\alpha_{1} = 0$ and $\alpha_{2} = \alpha_{3} = 1$. The path is continuously differentiable $D = 3$ times, and the Bézier curves have degree $M = {{2D} + 1} = 7$. The initial position is the center of the bottom-left box, $p^{init} = {}$, and the terminal position is the center of the top-right box, $p^{init} = {(P,P)}$. The largest of these instances (with $K = {25,600}$ safe boxes) is depicted in Fig. 7.

Figure 7: Largest problem instance in the scaling study, with K = 25, 600 safe boxes and final path shown.

The computation times are shown in Fig. 8, broken down into offline preprocessing, polygonal phase, and smooth phase. The smaller instances are solved in a few hundredths or tenths of seconds. For the largest instance in Fig. 7 the offline processing time is $25$ seconds, while the online polygonal and smooth phases take $0.12$ and $3.4$ seconds, respectively. Accounting for some fixed overhead, we see that the preprocessing times grow almost linearly with the number of boxes $K$ (unit slope in the log-log plot), while the online runtimes grow even more slowly. Tab. I shows the number of vertices $|\mathcal{V}|$ and edges $|\mathcal{E}|$ in the line graph $G$ and the number of boxes $N$ traversed by the final path, for all the problems in this analysis.

We report that for both the polygonal and the smooth phase the number of iterations is essentially unaffected by the size of the problem. In the polygonal phase the number of iterations ranges between 1 and 4, in the smooth phase between 5 and 6.

Figure 8: Computation times for the scaling study, broken down into offline preprocessing, polygonal phase, and smooth phase.

TABLE I: Size of the instances in the scaling study

### VII-C Large example

In our second example we plan a path for a quadrotor in an environment with many obstacles. The configuration space of a quadrotor is six dimensional: three coordinates specify the position of the center of mass, and three coordinates specify the orientation. However, given any path for the center of mass that is differentiable four times, a dynamically feasible trajectory for the quadrotor's orientation, together with the necessary control thrusts, can always be reconstructed. This convenient property is called *differential flatness*, and it allows us to plan the flight of a quadrotor by solving a path-planning problem in only $d = 3$ dimensions.

The quadrotor environment is shown at the top of Fig. 1, and it resembles a village with multiple buildings and dense vegetation. This village is constructed over a square grid with ${P^{2} = 50^{2} = 2},500$ points, which divide the ground into ${({P - 1})}^{2}$ square cells of unit side. The cell indexed by ${(i,j)} \in {\{ 1,\ldots,{P - 1}\}}^{2}$ has bottom-left coordinate ${(i,j)} \in \text{𝐑}^{2}$ and top-right coordinate ${({i + 1},{j + 1})} \in \text{𝐑}^{2}$. Each cell contains one of the following obstacles: a building, a bush, or a tree. There are a total of $9^{2} = 81$ buildings. The cells that each building occupies are identified through a random walk of length $5$ that starts in the cell with index ${(i,j)} \in {\{ 5,10,\ldots,40,45\}}^{2}$. Therefore each building can cover up to six cells, and neighboring buildings can potentially be connected. The buildings are constructed so that the quadrotor, whose collision geometry is overestimated with a sphere of radius $0.1$, cannot collide with them while flying in another cell. The height of each building is equal to $5.0$. In the cells that are not occupied by a building we have either a bush or a tree, with equal probability. Bushes and trees are positioned in the center of their cells. A bush has square base of side chosen uniformly at random between $0.2$ and $0.7$, and its height is twice the side of its base. The foliage of a tree is represented as a cube of side $0.8$. The center of the foliage has height that is drawn uniformly at random between $1.0$ and $4.5$. The trunk of a tree has square section with side $0.2$.

To construct the safe set $\mathcal{S}$ we decompose the free space in each cell independently using axis-aligned boxes. The buildings occupy their cells entirely, so for these cells we do not use any safe box. The free space around a bush is decomposed using five safe boxes: four around the bush and one on top. Similarly, for a tree we have four safe boxes around the trunk and one safe box on top of the foliage. These boxes are appropriately shrunk to take into account the collision geometry of the quadrotor. The total number of safe boxes needed to decompose the environment in Fig. 1 using this method is $K = {10,150}$. The resulting line graph has ${|\mathcal{V}|} = {70,907}$ vertices and ${|\mathcal{E}|} = {1,022,782}$ edges.

As shown in, a natural objective function when planning the path of a quadrotor is the squared $L_{2}$ norm of the fourth derivative (or snap). Thus we set our cost weights to $\alpha_{1} = \alpha_{2} = \alpha_{3} = 0$ and $\alpha_{4} = 1$. We design a path that is continuously differentiable $D = 4$ times, and we use Bézier curves of degree $M = {{2D} + 1} = 9$. The final time is taken to be $T = P = 50$. The quadrotor takes off at the bottom left of the environment $p^{init} = {}$, and lands in the top right $p^{init} = {(P,P,0)}$. Using the results from, it can be seen that for the quadrotor to start and stop horizontally, with zero translational and angular velocity, the following boundary conditions are necessary:

The small modifications necessary for our algorithm to handle these constraints are described in §VIII.

The offline preprocessing of the safe boxes takes $101$ seconds, with the representative points in computed using the commercial solver MOSEK 10.0. The polygonal phase takes $0.22$ seconds, and it converges in $5$ iterations. The smooth phase takes $7.5$ seconds and $8$ iterations. The number of boxes in the final path is $135$. The bottom of Fig. 1 shows the quadrotor flying along the path generated by our algorithm. A video of the quadrotor flight can be found at [https://youtu.be/t9UWIi9NyxM](https://youtu.be/t9UWIi9NyxM).

In this example, as well as in any other problem where we only penalize the path snap, our initial guess of the traversal times is quite inaccurate, and the initial trajectory has very high cost. However, the first iteration of the smooth phase is already sufficient to reduce the cost by $84.3\%$, and the final trajectory has a cost that is $99.3\%$ smaller than the initial one.

### VII-D Comparison with mixed-integer optimization

A very natural approach to solving problem is mixed-integer (global) optimization. We conclude our experiments with a comparison of our method with these techniques. As a benchmark we use our simple running example illustrated in §III--V, since the mixed-integer approach is impractical for larger problems.

To solve problem using mixed-integer optimization, we parameterize a path as a piecewise Bézier curve with $N$ subpaths of equal duration $T_{j} = {T/N}$, $j = {1,\ldots,N}$. We write a mixed-integer program that is identical to problem, except for the traversal times $T_{j}$ that here have fixed value, and the safety condition that is substituted with a disjunctive constraint. This disjunctive constraint requires that each subpath $p_{j}$ be contained in at least one safe box $\mathcal{B}_{k}$, and is encoded using the binary variables $\sigma_{j,k} \in {\{ 0,1\}}$, $j = {1,\ldots,N}$ and $k = {1,\ldots,K}$. Since our safe sets are axis-aligned boxes, this constraint takes the following simple form:

for $j = {1,\ldots,N}$ and $n = {0,\ldots,M}$. The binary variables are also subject to the "one-hot" constraint

for $j = {1,\ldots,N}$. The resulting problem is a mixed-integer quadratic program (MIQP).

We solve a sequence of MIQPs for an increasing number of subpaths in our piecewise Bézier curve: $N = {9,\ldots,18}$. The minimum value $N = K = 9$ is chosen since the optimal path might have to visit each safe box. Setting the degree of the Bézier curves to $M = {{2D} + 1} = 7$, we then have that the mixed-integer approach features the same completeness guarantee as our method, i.e., the MIQP is feasible if and only if the original planning problem is feasible. Larger values of $N$ yield a more flexible path parameterization and can decrease the MIQP optimal value. However, they also increase the MIQP solution times, which in the worst case are proportional to the number $K^{N}$ of possible assignments of the binary variables. Note that, since $N \geq K$, this worst-case runtime is super-exponential in the number $K$ of boxes.

The path designed by our method for the running example is illustrated in the right of Fig. 6, has cost $1.0001$, and is essentially the global minimum of the problem (which has unit cost). The offline preprocessing (Fig. 2), the polygonal phase (Fig. 4), and the smooth phase (Fig. 6) of our algorithm take $1.0$, $1.7$, and $14.5$ milliseconds, respectively. The sum of these three times ($17.2$ milliseconds) and the cost of our path are reported in Fig. 9 with a yellow star.

Figure 9: Comparison of our algorithm with mixed-integer optimization. The yellow star represents our method. The three curves mark the performance of different commercial solvers (CPLEX, Gurobi, and MOSEK) as the number N of subpaths used in the path parameterization increases.

For the solution of the MIQPs we consider three state-of-the-art commercial solvers: CPLEX 22.1.1, Gurobi 10.0, and MOSEK 10.0. Fig. 9 reports the solution times and the path costs for these solvers, as functions of the number $N$ of subpaths. For $N = 9$ the MIQP has an optimal value of $1.27$, which is higher than our method since the duration of each subpath is fixed in the MIQP, and the solver cannot finely optimize the traversal times. The fastest solver is CPLEX which takes $124$ milliseconds, and is six times slower than our approach. The number of subpaths that leads to the MIQP of lowest optimal value is $N = 15$. This optimal value is $1.01$, which is closer to but still larger than the cost of the path found with our method. CPLEX is the fastest solver also in this case, and takes $439$ milliseconds ($26$ times slower than our algorithm).

As expected, the mixed-integer approach becomes quickly impractical as the problem size grows. For instance, by solving via MIQP the smallest problem in the scaling study in §VII-B (with $N = K$ and $M = {{2D} + 1}$), we get a path that is approximately three times cheaper than ours. However, our planner takes only $43$ milliseconds (including the offline preprocessing), while CPLEX takes $584$ seconds to solve the MIQP, and $25$ seconds of branch and bound before finding a feasible path with cost lower than ours. The other solvers are even slower.

## Extensions

We conclude by briefly mentioning how the techniques presented in this paper can be extended to more general path-planning problems.

### Initial and final derivatives

Our method handles boundary values on the path derivatives very easily. We only need to specify them in problem using the control points $p_{1,0}^{(i)}$ and $p_{N,{M - i}}^{(i)}$, with $i \in {\{ 1,\ldots,D\}}$, as done for the endpoint constraints in.

An additional modification to our algorithm that is useful in presence of boundary conditions on the derivatives concerns the estimate of the traversal times in §V-C. Instead of initializing the traversal times by traveling the whole polygonal curve $\mathcal{C}$ at constant speed, we travel at constant speed only the central part of $\mathcal{C}$, and in the first and last segments we set to a constant the smallest derivative that gives us enough variables to satisfy the boundary conditions and the differentiability constraints. For example, in the quadrotor problem in §VII-C, we need constant seventh derivative in the initial and final segments of $\mathcal{C}$ to find a time parameterization whose first three derivatives vanish at the endpoints, and that is continuously differentiable four times.

Finally, we note that with boundary conditions on the derivatives the degree of the first and last Bézier curves might need to be increased to preserve the completeness of our algorithm. For example, if the initial position is close to a boundary of the safe set, and the initial velocity points outwards, we may need many control points to design a sharp turn that does not leave the safe set.

### Convex safe sets

The assumption that the safe sets are axis-aligned boxes is very convenient in the offline part of our algorithm, since the pairwise intersections between a collection of boxes can be found very efficiently. We also leveraged this assumption in the polygonal phase, specifically in the multiple stabbing problems and in the improvement of the box sequence in §IV-B. In case of more generic convex safe sets these computations are more demanding and can significantly slow down our algorithm. For example, checking if two convex sets intersect requires solving a convex optimization problem, e.g., a linear program when the sets are polyhedra. However, if each convex safe set is equipped with an axis-aligned bounding box, part of the efficiency of our approach can be recovered.

### Unspecified final time

In some applications specifying a fixed final time $T$ is not straightforward, and it is preferable to let the planning algorithm select this value automatically. In these cases, we also add a penalty on $T$ (e.g., a linear cost $\alpha_{0}T$ with fixed weight $\alpha_{0} > 0$) that prevents our original objective $J$ from making the final time arbitrarily large. Our approach can be extended to these problems very naturally. In the initialization of the traversal times in §V-C, we now require an initial guess also for the total duration of the path. This guess is then improved by solving the tangent problem in §V-C, where the final time $T$ is now a variable in the linear constraint, and the cost function includes the time penalty (e.g., $\alpha_{0}T$).

### Derivative constraints

Convex constraints on the path derivatives are also easily incorporated in our framework. In fact, the path derivatives are piecewise Bézier curves, and, similarly to the safety constraints in, they can be forced to lie in a convex set at all times by constraining their control points. If the final time $T$ is fixed, the addition of these constraints breaks the completeness of our algorithm. Specifically, the feasibility argument in §II-C does not hold anymore, and the optimization of our piecewise Bézier path in might be infeasible even if the original path-planning problem is feasible. However, if we let $T$ be an optimization variable as described above, then the algorithm completeness is recovered. This because any derivative constraint (that contains the origin in its interior) can be satisfied by travelling along a curve sufficiently slowly.

### Multiple waypoints

In some path-planning problems we need to design a single smooth path that interpolates or passes through a given sequence of intermediate waypoints in order. To extend our approach to these problems, the steps in the polygonal phase are repeated to connect each pair of consecutive waypoints, yielding a single polygonal curve that satisfies all the interpolation constraints. Similarly, in the smooth phase, we concatenate multiple problems of the form into a single program, where each piecewise Bézier curve has fixed endpoints and is constrained to connect smoothly with its neighbors. The time at which the overall path visits each waypoint is then automatically selected by the smooth phase. Finally, periodic trajectories that visit all the waypoints can be generated by asking our path to satisfy ${p^{(i)}{}} = {p^{(i)}{(T)}}$, $i = {0,\ldots,D}$. These conditions translate immediately to linear constraints on the control points of the initial and final Bézier subpaths.
