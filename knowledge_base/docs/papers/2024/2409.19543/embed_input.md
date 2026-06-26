<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Multi-Query Shortest-Path Problem in Graphs of Convex Sets

Topics include Semidefinite programming, Motion planning, Robotics, Graphs, Online algorithms, Offline algorithms, Optimization, Planning, Shortest path problem.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The Shortest-Path Problem in Graph of Convex Sets (SPP in GCS) is a recently developed optimization framework that blends discrete and continuous decision making. Many relevant problems in robotics, such as collision-free motion planning, can be cast and solved as an SPP in GCS, yielding lower-cost solutions and faster runtimes than state-of-the-art algorithms. In this paper, we are motivated by motion planning of robot arms that must operate swiftly in static environments. We consider a multi-query extension of the SPP in GCS, where the goal is to efficiently precompute optimal paths between given sets of initial and target conditions. Our solution consists of two stages. Offline, we use semidefinite programming to compute a coarse lower bound on the problem's cost-to-go function. Then, online, this lower bound is used to incrementally generate feasible paths by solving short-horizon convex programs. For a robot arm with seven joints, our method designs higher quality trajectories up to two orders of magnitude faster than existing motion planners.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

A Graph of Convex Sets (GCS) is a graph where each vertex is paired with a convex set and an optimization variable inside this set, while each edge couples adjacent vertex variables through additional convex costs and constraints. In the Shortest-Path Problem (SPP) in GCS, we simultaneously seek a discrete path through this graph and optimize the continuous variables associated with the vertices along the path, while minimizing the cumulative edge costs.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Though the SPP in GCS is NP-hard \[26, Section 9.2\], effective solution methods have been proposed. This technique has shown remarkable success in various robotics applications, such as optimal control, planning through contact, and other robotics problems. In real-world hardware deployment, it has been especially effective in collision-free motion planning, addressing the challenges of non-convex obstacle avoidance constraints.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, solving the SPP in GCS can sometimes be too slow for real-time applications on high-dimensional robotic systems. Consider a 7-DoF KUKA iiwa robot arm repeatedly performing online motion planning in a static environment. When the environment is simple, the GCS is small, and the shortest path queries can be solved quickly, in under 50ms. However, when the environment is complex and the configuration space must be covered thoroughly, as in Fig. 1, the GCS becomes large, and the shortest path queries can take up to of 600ms. This is not practical for high-productivity applications, such as robot arms in warehouses, where the company's income is nearly proportional to the operational speed.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

In an effort to reduce solve times for online shortest path queries in GCS, we seek an efficient way of precomputing optimal paths between given sets of source and target conditions in the GCS. We formulate this problem as a generalization of the SPP in GCS that is akin to the all-pairs generalization of the classical SPP. Our solution contains two phases, illustrated in Fig. 2. Offline, we solve a semidefinite program that produces convex quadratic lower bounds to the cost-to-go function over the convex sets associated with GCS vertices. Pictured in Fig. 2(a) are the contour plots of these lower bounds at every vertex. Then, online, we use a greedy multi-step lookahead policy with the cost-to-go lower bounds to determine the next vertex to visit. Thus, as shown in Fig. 2(b), the path is obtained incrementally, one vertex at a time. Though the quadratic cost-to-go lower bounds can be coarse, using the lookahead policy is equivalent to producing piecewise-quadratic lower bounds, which can be very expressive. As a result, the obtained paths are nearly optimal in practice.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Convexity of the quadratic cost-to-go lower bounds allows us to evaluate the greedy policy by solving a set of small convex programs in parallel, which can be done quickly at runtime. Applied to the complex scenario shown in Fig. 1, our method requires just 6s of offline computation to produce the cost-to-go lower bounds. Subsequent online queries take 2-11ms, which is up to two orders of magnitude faster than solving the SPP in GCS from scratch.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

(a) Offline: synthesize cost-to-go over the GCS. Contour plots are shown.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

(b) Online: at each iteration, we evaluate all n-step paths from the current vertex (n = 1 shown) and greedily select the decision that minimizes the n-step lookahead cost-to-go. The first three iterations are shown, as the path is built incrementally.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Literature review", "weight": 1.0} -->

Graph search plays a central role in both modelling and solving a wide variety of planning problems in robotics. In this section we briefly connect our work to some notable examples in this literature.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Literature review", "weight": 1.0} -->

A common approach to motion planning is to construct a graph where nodes correspond to collision-free configurations and edges correspond to collision-free motions. The most popular approaches based on this idea are the Rapidly exploring Random Trees (RRT), Probabilistic Roadmap (PRM), and their many variants. The GCS approach to motion planning is similar to the PRM one, but collision-free configurations are replaced with large collision-free sets. GCS avoids two major drawbacks of planning with a PRM: the need to densely sample in high-dimensional spaces and post-process the motion plan to obtain a smooth trajectory. However, generating these collision-free sets can be computationally challenging and expensive. Furthermore, SPP in GCS queries can still be very expensive, motivating this current work.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Literature review", "weight": 1.0} -->

The importance of the SPP has led to a breadth of literature on its solution, with Bellman's dynamic programming approach illustrating the central role of the cost-to-go function. Given the cost-to-go, a shortest path can be extracted using a simple greedy strategy: given a vertex $v$, the next vertex in the path is the one which minimizes the cost-to-go among all the neighbors of $v$. This is captured by the famous Bellman's equation.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Literature review", "weight": 1.0} -->

Multi-query SPP setting has also been thoroughly investigated. The All-Pairs Shortest Paths (APSP) is the problem of finding shortest paths between every pair of vertices in a discrete graph \[10, Ch. 23\]. One method for solving this problem, from which we draw particular inspiration, first computes the cost-to-go function between every pair of vertices in the graph (also known as a *distance oracle*). This cost-to-go is used to produce a successor along the shortest path between every pair of vertices, which is stored into the successor matrix. The optimal paths are retrieved by sequentially querying this matrix.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Literature review", "weight": 1.0} -->

Explicit solutions to the Bellman equation exist only in a handful of contexts. In the case of purely discrete graphs, a number of efficient methods exist, where the cost-to-go function can be encoded using a simple matrix. Another notable example from control is Explicit Model Predictive Control (MPC) where the cost-to-go is a piecewise quadratic. However, even in these settings, storing the cost-to-go can be prohibitively expensive for large graphs, particularly in the APSP setting. In the purely discrete setting, the description of the APSP cost-to-go function grows quadratically in the size of the graph, while in the MPC setting it grows exponentially.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Literature review", "weight": 1.0} -->

In most cases, solving the Bellman equation is known to be intractable. This has motivated a breadth of literature for computing approximations for the cost-to-go in various setting. Similarly, in this paper we seek a computationally tractable way to approximate the cost-to-go function to solve the APSP in GCS. The generalization in the particular context of GCS is not straightforward and constitutes one of the contributions of this work.

<!-- chunk {"id": "body-0016", "role": "body", "section": "All-Pairs Shortest Paths in a Graph of Convex Sets", "weight": 1.0} -->

We seek to efficiently precompute optimal solutions to the SPP in GCS between given sets of source and target conditions. Section 2.1 presents the classical APSP, which is the corresponding problem in an ordinary graph. In Section 2.2, we describe the single-query SPP in GCS. We then formulate the APSP in GCS in Section 2.3, and outline our approximate solution method in Section 2.4.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Graphs and paths", "weight": 1.0} -->

Let $G = {(\mathcal{V},\mathcal{E})}$ be a directed graph with vertex set $\mathcal{V}$ and edge set $\mathcal{E}$. Given a source vertex $s$ and target vertex $t$, an $s\text{-}t$ path is a sequence of distinct vertices $p = {({{s = {v_{0},v_{1},\ldots}},{v_{K} = t}})}$, where each consecutive pair of vertices is connected by an edge in $\mathcal{E}$ and no vertex is revisited.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Shortest Path Problem (SPP)", "weight": 1.0} -->

Let us associate with every edge $e \in \mathcal{E}$ a non-negative edge cost $c_{e} \in {\mathbb{R}}_{+}$. A shortest path $p$ between the vertices $s$ and $t$ minimizes the sum of the edge costs along the path: The optimal value of this program is called the cost-to-go between $s$ and $t$, and is denoted by $J_{s,t}^{\ast}$. The principle of optimality holds in this context, stating that every subpath of a shortest path is itself a shortest path. This forms the foundation for many efficient solution algorithms to this problem.

<!-- chunk {"id": "body-0019", "role": "body", "section": "All-Pairs Shortest Paths (APSP)", "weight": 1.0} -->

The APSP is the multi-query generalization of the SPP, where we seek a shortest path between all pairs of vertices in a graph. Efficient solutions to the APSP leverage the principle of optimality. Instead of computing the full path for each pair of vertices, it suffices to compute only the immediate successor along this path. The full path can thus be attained incrementally, one vertex at the time.

<!-- chunk {"id": "body-0020", "role": "body", "section": "All-Pairs Shortest Paths (APSP)", "weight": 1.0} -->

This solution to the APSP can be implicitly encoded via the cost-to-go function $J_{v,t}^{\ast}$ for every pair of vertices $v$ and $t$, computed via dynamic programming \[10, Ch. 23\]. The successor is then computed by greedily picking a vertex that minimizes the one-step lookahead with respect to the cost-to-go: The solution $\pi$ is a decision policy that, given the current and target vertices $v$ and $t$, selects the next vertex on the shortest $v\text{-}t$ path. We refer to $\pi$ as the successor policy.

<!-- chunk {"id": "body-0021", "role": "body", "section": "The Shortest Path Problem in a Graph of Convex Sets", "weight": 1.0} -->

The SPP in GCS between point ${\overline{x}}_{s} \in \mathcal{X}_{s}$ of vertex $s$ and ${\overline{x}}_{t} \in \mathcal{X}_{t}$ of vertex $t$ is defined as follows: Similar to the classical SPP, the SPP in GCS searches for an $s\text{-}t$ path $p = {(v_{0},v_{1},\ldots,v_{K})}$ though a graph, which is a sequence of distinct vertices. In addition to that, it also searches for a sequence of corresponding vertex variables $({{{\overline{x}}_{s} = {x_{v_{0}},x_{v_{1}},\ldots}},{x_{v_{K}} = {\overline{x}}_{t}}})$, referred to as a trajectory.

<!-- chunk {"id": "body-0022", "role": "body", "section": "The Shortest Path Problem in a Graph of Convex Sets", "weight": 1.0} -->

This trajectory satisfies the vertex and edge constraints (2c), (2d), (2e), while minimizing the edge costs (2a). The optimal solution to is thus a tuple (path and trajectory). We denote the optimal value of as $J_{s,t}^{\ast}{({\overline{x}}_{s},{\overline{x}}_{t})}$ and refer to it as the cost-to-go from point ${\overline{x}}_{s}$ of vertex $s$ to point ${\overline{x}}_{t}$ of vertex $t$.

<!-- chunk {"id": "body-0023", "role": "body", "section": "The Shortest Path Problem in a Graph of Convex Sets", "weight": 1.0} -->

Unlike the classical SPP, the SPP in GCS is NP-hard \[24, Section 9.2\], and thus unlikely to have a polynomial-time solution. However, it can be reformulated as a Mixed-Integer Convex Program (MICP) with a strong convex relaxation: using a rounding strategy, this relaxation often yields near-optimal solutions in practice.

<!-- chunk {"id": "body-0024", "role": "body", "section": "The Shortest Path Problem in a Graph of Convex Sets", "weight": 1.0} -->

For the classical SPP, the principle of optimality holds and the optimal policy is independent of past decisions, which simplifies the problem and enables many efficient solution algorithms. As demonstrated in the following example, these properties break down in the SPP in GCS.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Example 1", "weight": 1.0} -->

Consider the GCS in Fig. 3, which is embedded in ${\mathbb{R}}^{2}$. This GCS has four vertices $\mathcal{V} = {\{ s,v,w,t\}}$, where the convex sets $\mathcal{X}_{s},\mathcal{X}_{v},\mathcal{X}_{t}$ are points, and the convex set $\mathcal{X}_{w}$ is a segment. Every vertex is connected to every other vertex with an edge, and the edge lengths $l_{e}$ are the squared Euclidean distance (e.g., $l_{(v,w)} = {\|{x_{v} - x_{w}}\|}_{2}^{2}$).

<!-- chunk {"id": "body-0026", "role": "body", "section": "Example 1", "weight": 1.0} -->

Due to the constraint that vertices cannot be revisited, the optimal policy is a function of the set of previously visited vertices. This is demonstrated in Fig. 3(a), where we plot the optimal $s\text{-}t$ path in orange and the optimal $v\text{-}t$ path in blue. The optimal decision at vertex $v$ depends on previously visited vertices: if $w$ was visited before, the optimal decision is to go to $t$ (orange), otherwise the optimal decision is to go to $w$ (blue).

<!-- chunk {"id": "body-0027", "role": "body", "section": "Example 1", "weight": 1.0} -->

(a) The optimal policy at vertex v depends on previous decisions. If w has been visited already, the optimal decision is to go to t (orange), otherwise it is to go to w (blue).

<!-- chunk {"id": "body-0028", "role": "body", "section": "Example 1", "weight": 1.0} -->

(b) If we allow vertex revisits, the optimal policy is independent of past decisions. Shown are the optimal s-t (green) and v-t (blue) solutions to the relaxed problem.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Example 1", "weight": 1.0} -->

Observe also that the principle of optimality does not hold for this problem: the $v\text{-}t$ subpath of the optimal $s\text{-}t$ path (orange) is not the optimal $v\text{-}t$ path (blue). We cannot substitute the optimal $v\text{-}t$ path (blue) in place of the original $v\text{-}t$ subpath, since the resulting vertex sequence $(s,w,v,w,t)$ (Fig. 3(b), green) visits vertex $w$ twice, and is therefore not a path.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Example 1", "weight": 1.0} -->

The constraint that vertices cannot be revisited is a key challenge of the SPP in GCS. This is unlike the classical SPP with non-negative edge lengths, where this constraint does not increase problem complexity. It can be shown that if we allow vertex revisits, then the principle of optimality holds, and the optimal decision policy is independent of past decisions. This is illustrated in Fig. 3(b), where the optimal $s\text{-}t$ and $v\text{-}t$ solutions to the relaxed problem are shown in green and blue respectively.

<!-- chunk {"id": "body-0031", "role": "body", "section": "All-Pairs Shortest Paths in a Graph of Convex Sets", "weight": 1.0} -->

The APSP in GCS extends the classical APSP in a natural way. We are given a set of source vertices $\mathcal{S} \subset \mathcal{V}$ and a set of target vertices $\mathcal{T} \subset \mathcal{V}$. The goal is to solve the SPP in GCS between every pair of source and target points ${\overline{x}}_{s} \in \mathcal{X}_{s}$ and ${\overline{x}}_{t} \in \mathcal{X}_{t}$, and every pair of source and target vertices $s \in \mathcal{S}$ and $t \in \mathcal{T}$. Since the SPP in GCS is NP-hard, the APSP in GCS is at least NP-hard as well.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Method outline", "weight": 1.0} -->

Our approach generalizes the solution to the classical APSP outlined in Section 2.1. We proceed in two phases. Offline, we compute a coarse quadratic lower bound on the cost-to-go between relevant pairs of GCS vertices. Then online, we extend the greedy policy (1. ‣ 2.1 All-Pairs Shortest Paths ‣ 2 All-Pairs Shortest Paths in a Graph of Convex Sets ‣ Multi-Query Shortest-Path Problem in Graphs of Convex Sets")) to the GCS setting. At runtime, we rollout this policy to obtain the solution path incrementally, one vertex at a time.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Method outline", "weight": 1.0} -->

Unlike the classical APSP, a greedy policy with the cost-to-go $J_{s,t}^{\ast}$ is not an optimal policy for the APSP in GCS. This is because the optimal policy for paths in GCS depends on previously visited vertices, which is not captured by the cost-to-go $J_{s,t}^{\ast}{(x_{s},x_{t})}$. Thus, our approach is bound to yield approximate solutions, further limited by the coarseness of quadratic cost-to-go lower bounds.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Method outline", "weight": 1.0} -->

To incorporate the challenging "no-vertex-revisit constraint" into the cost-to-go function, we relax this constraint by introducing penalties for vertex revisits. These penalties are applied to the edge lengths, producing a biased cost-to-go lower bound that discourages revisits. When rolling out a greedy policy online, we also explicitly prohibit vertex revisits. To mitigate the coarseness of quadratic cost-to-go lower bounds and better approximate the optimal policy, we employ a multi-step lookahead generalization of the greedy policy (1. ‣ 2.1 All-Pairs Shortest Paths ‣ 2 All-Pairs Shortest Paths in a Graph of Convex Sets ‣ Multi-Query Shortest-Path Problem in Graphs of Convex Sets")), optimizing over $n$-step decision sequences at each iteration.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Offline phase: synthesis of cost-to-go lower bounds", "weight": 1.0} -->

In Section 3.1, we present the optimization problem that produces cost-to-go lower bounds for the APSP in GCS. This program is infinite-dimensional, so in Section 3.2 we present a tractable numerical approximation for it.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Offline phase: synthesis of cost-to-go lower bounds", "weight": 1.0} -->

For clarity of presentation, we make some simplifying assumptions. First, we assume that we have just one source vertex and one target vertex, i.e., $\mathcal{S} = {\{ s\}}$ and $\mathcal{T} = {\{ t\}}$. Second, we assume that the set $\mathcal{X}_{t}$ corresponding to the target vertex $t$ is a singleton: $\mathcal{X}_{t} = {\{ x_{t}\}}$. Since the target vertex $t$ and point $x_{t}$ are fixed, we also simplify the notation and refer to $J_{v,t}^{\ast}{(x_{v},x_{t})}$ as $J_{v}^{\ast}{(x_{v})}$. The extensions of our method when these assumptions do not hold are straightforward and discussed in Appendix 0.A.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Cost-to-go lower bounds via infinite-dimensional LP", "weight": 1.0} -->

The cost-to-go lower bounds are synthesized with the following optimization problem: We now give a detailed line-by-line explanation of this program, and prove the validity of the lower bounds it produces in Lemma 1 below.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Cost-to-go lower bounds via infinite-dimensional LP", "weight": 1.0} -->

In constraint (3b), we associate with every vertex $v \in \mathcal{V}$ a (possibly non-convex) function $J_{v}$ defined over the set $\mathcal{X}_{v}$. These functions serve as the lower bounds on the cost-to-go $J_{v}^{\ast}$, as will be shown later. We emphasize that we are searching over the space of functions $J_{v}$, not over the individual points $x_{v}$.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Cost-to-go lower bounds via infinite-dimensional LP", "weight": 1.0} -->

In the objective function (3a), $\phi_{s}$ is a probability distribution of anticipated source conditions over the set $\mathcal{X}_{s}$. Thus, the integral in (3a) maximizes the weighted average of $J_{s}$ over the source set $\mathcal{X}_{s}$, effectively "pushing up" on the cost-to-go lower bound at the source vertex.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Cost-to-go lower bounds via infinite-dimensional LP", "weight": 1.0} -->

In (3c), we introduce a non-negative penalty $h_{w}$ for every vertex $w \in \mathcal{V}$. This penalty is meant to discourage revisits to vertex $w$, which is a way to relax the constraint that a path must not visit any vertex more than once.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Cost-to-go lower bounds via infinite-dimensional LP", "weight": 1.0} -->

To implement the penalty $h_{w}$, we increment the edge length $l_{e}$ for every edge $e \in \mathcal{E}$ that enters vertex $w$. This is formalized in (3d), which states that for every edge $e = {(v,w)}$ and a feasible transition ${(x_{v},x_{w})} \in \mathcal{X}_{e}$, the value $J_{v}{(x_{v})}$ is a lower bound on the sum of the penalty-incremented edge length ${l_{e}{(x_{v},x_{w})}} + h_{w}$ and the subsequent cost-to-go lower bound $J_{w}{(x_{w})}$. As written, the non-negative penalty $h_{w}$ increases the cost of the edges leading into vertex $w$, thereby discouraging visits to $w$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Cost-to-go lower bounds via infinite-dimensional LP", "weight": 1.0} -->

However, since our goal is to only discourage vertex revisits, we need to waive the penalty $h_{w}$ once. This is achieved by setting the cost-to-go lower bound $J_{t}{(x_{t})}$ to $- {\sum_{w \in \mathcal{V}}h_{w}}$ in constraint (3e). Upon reaching the target vertex, we subtract the sum of all vertex penalties from the cost-to-go lower bound, effectively waiving the penalties once per vertex. We now show that these constraints produce lower bounds on the cost-to-go function.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Example 1, continued", "weight": 1.0} -->

Consider the solution to program for the GCS instance in Fig. 3. Setting the revisit penalty $h_{w} = 0$ results in $J_{s} = 14$, which is the cost of the vertex sequence that visits $w$ twice (green in Fig. 3(b)). By jointly optimizing over the penalties and the cost-to-go lower bounds, program selects the penalty $h_{w} = 2$. Revisiting vertex $w$ is no longer advantageous, and the cost of the shortest $s\text{-}t$ path (orange in Fig. 3(a)) is achieved: $J_{s} = J_{s}^{\ast} = 16$.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Example 1, continued", "weight": 1.0} -->

We note that program naturally generalizes the cost-to-go synthesis LP for the classical SPP. When each convex set $\mathcal{X}_{v}$ is a singleton, the problem reduces to the classical SPP, where functions $J_{v}$ are defined at single points and represented by a single decision variable. Setting vertex penalties $h_{w} = 0$ recovers the standard cost-to-go synthesis LP for the classical SPP: | | $\max\limits_{{\{ J_{v}\}}_{v \in \mathcal{V}}}$ | $J_{s}$ | | \(6\) | Compared to the purely discrete setting of, optimization program is also an LP; however, it searches over the space of functions and is therefore infinite-dimensional. Next, we develop a tractable finite-dimensional approximation to that is conducive to numerical methods.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Numerical approximation via semidefinite programming", "weight": 1.0} -->

We now produce an approximate solution to the cost-to-go synthesis program. We restrict each function $J_{v}$ to be convex quadratic, which allows us to cast as a tractable Semidefinite Program (SDP). SDPs are mathematical programs where the objective function is linear and the constraints are either linear or linear matrix inequalities (LMIs). To help with the presentation, we first state without proof three well-known facts.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Defining cost-to-go lower bounds in (3b)", "weight": 1.0} -->

We restrict lower bounds $J_{v}$ per vertex $v \in \mathcal{V}$ to be convex quadratic functions. By Lemma 2 ‣ 3.2 Numerical approximation via semidefinite programming ‣ 3 Offline phase: synthesis of cost-to-go lower bounds ‣ Multi-Query Shortest-Path Problem in Graphs of Convex Sets"), searching for such functions is equivalent to searching for appropriate PSD matrices $Q_{v}$. The decision variables are thus the coefficients of the quadratic polynomials. As a result, we produce coarse quadratic lower bounds on the optimal $J_{v}^{\ast}$; this coarseness will be mitigated via the multi-step lookahead policies.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Defining cost-to-go lower bounds in (3b)", "weight": 1.0} -->

Constraint (3c) is already linear, and constraint (3e) is linear in the coefficients of the quadratic polynomial $J_{t}$ and the decision variables $h_{w}$. These constraints are thus already suitable for the SDP.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Enforcing the lower-bound constraint (3d)", "weight": 1.0} -->

To apply Corollary 1 to enforce this constraint, we impose additional restrictions. First, we restrict vertex and edge sets $\mathcal{X}_{v}$ and $\mathcal{X}_{e}$ to be intersections of ellipsoids and polyhedra. We also restrict edge lengths $l_{e}$ to be quadratic, ensuring that the expression in (3d) is quadratic. For non-quadratic $l_{e}$, such as the Euclidean distance, we use a quadratic approximation instead. Applying Corollary 1, we verify constraint (3d) with an LMI.

<!-- chunk {"id": "body-0049", "role": "body", "section": "The objective function (3a)", "weight": 1.0} -->

Since $J_{s}$ is a quadratic polynomial, the integral in (3a) is linear in the coefficients of $J_{s}$, which are the decision variables of the program. Therefore, the objective function (3a) is linear in the decision variables, as required for the SDP.

<!-- chunk {"id": "body-0050", "role": "body", "section": "The objective function (3a)", "weight": 1.0} -->

Empirically, we found quadratic lower bounds to be a good balance between computational complexity and expressive power. Note that higher-degree polynomial lower bounds $J_{v}$ can be synthesized via the Sums-of-Squares (SOS) hierarchy. However, in practice, the resulting programs tend to be prohibitively expensive. On the other hand, restricting $J_{v}$ to be affine yields a program that almost exactly matches the dual to the convex relaxation of the SPP in GCS, discussed in \[26, App. B\]. In other words, solving the SPP in GCS already gives a coarse affine cost-to-go lower bound that can be used to solve the APSP in GCS. In Section 5.3, we show that empirically, these affine lower bounds have significantly less expressive power than the quadratic lower bounds.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Online phase: greedy multi-step lookahead policy", "weight": 1.0} -->

We now generalize the greedy successor policy (1. ‣ 2.1 All-Pairs Shortest Paths ‣ 2 All-Pairs Shortest Paths in a Graph of Convex Sets ‣ Multi-Query Shortest-Path Problem in Graphs of Convex Sets")) from the classical APSP to the GCS setting. Suppose that at runtime, we are given a source vertex $v_{0} \in \mathcal{S}$ and a source point $x_{0} \in \mathcal{X}_{v_{0}}$. At iteration $k$ of the policy rollout, let $(v_{k},x_{k})$ be the current vertex and vertex variable, and let $p_{k} = {(v_{0},v_{1},\ldots,v_{k - 1})}$ be the path so far.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Online phase: greedy multi-step lookahead policy", "weight": 1.0} -->

The successor policy ${\pi{(v_{k},x_{k},p_{k})}} = {(v_{k + 1},x_{k + 1})}$, which we will define shortly, produces the next vertex $v_{k + 1}$ and the corresponding vertex variable $x_{k + 1}$. We then advance to the next iteration. The rollout terminates when we reach the target vertex $t$, where we must select the target point $x_{t}$. Upon termination, we extract the vertex path $p = {(v_{0},v_{1},\ldots,v_{t})}$ and re-optimize for the continuous vertex variables $(x_{0},x_{1},\ldots,x_{t})$, so as to produce a trajectory that is optimal within this path.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Online phase: greedy multi-step lookahead policy", "weight": 1.0} -->

At each iteration of the policy rollout, we solve a greedy lookahead optimization problem with the coarse quadratic lower bounds obtained in Section 3.2. For simplicity, here we present just the 1-step lookahead program: Note that we do not use the penalty-incremented edge cost ${l_{e}{(x_{k},x_{w})}} + h_{w}$ in (7a), since the penalty $h_{w}$ is waived the first time that $w$ is visited. Vertex revisits are then also explicitly prohibited in (7b).

<!-- chunk {"id": "body-0054", "role": "body", "section": "Online phase: greedy multi-step lookahead policy", "weight": 1.0} -->

In a multi-step lookahead formulation, we instead solve for an $n$-step optimal decision sequence, take just the first step, and repeat at next iteration. The multi-step lookahead is key for mitigating the coarseness of the quadratic lower bounds. This is because an $n$-step lookahead from vertex $v$ effectively produces a piecewise-quadratic lower bound on the cost-to-go $J_{v}^{\ast}$ over $\mathcal{X}_{v}$, which has significantly more expressive power. While these lower bounds can still be loose in theory, the multi-step lookahead enables effective decision-making in practice.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Online phase: greedy multi-step lookahead policy", "weight": 1.0} -->

Convexity of $J_{w}$ is crucial, as it allows us to solve the program efficiently at run-time. To find the minimizer to, we solve multiple convex programs in parallel, one for every $n$-step lookahead sequence.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Online phase: greedy multi-step lookahead policy", "weight": 1.0} -->

Finally, we note that the lookahead program is not guaranteed to be recursively feasible. If we end up in a vertex where has no solution, we backtrack to a previous vertex that has a different feasible outgoing edge, and retry from there. Generally, our planner is sound but not complete: it is not guaranteed to produce a solution, but every solution it produces is feasible.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Experimental evaluation", "weight": 1.0} -->

We evaluate our approach through multiple numerical experiments. Section 5.1 presents a simple two-dimensional problem that provides visual intuition to our method. In Section 5.2, we apply our approach to a complex high-dimensional scenario, the robot arm in Fig. 1. Finally, Section 5.3 shows that our approach scales well to large graphs. We also discuss how the coarseness of the cost-to-go lower bounds and the multi-step lookahead horizon impact the performance.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Experimental evaluation", "weight": 1.0} -->

All of the experiments are run on a desktop computer with a 4.5Ghz 16-core AMD Ryzen 9 processor and 64GB 4800MHz DDR5 memory. We use Mosek 10.2.1 to solve all the convex programs in this section.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Two-dimensional example", "weight": 1.0} -->

We first consider a two-dimensional GCS problem in Fig. 2. We have a graph $G$ with ${|\mathcal{V}|} = 9$ vertices, ${|\mathcal{E}|} = 25$ edges, including multiple cycles. The geometry of the convex sets $\mathcal{X}_{v}$ can be deduced from Fig. 2(a); no edge constraints $\mathcal{X}_{e}$ are used. The edge costs ${l_{e}{(x_{v},x_{w})}} = {\|{x_{v} - x_{w}}\|}_{2}^{2}$ are the squared Euclidean distance. The source vertex $s$ is a box, and the target vertex $t$ is a singleton.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Two-dimensional example", "weight": 1.0} -->

We compute the convex quadratic lower bounds on the cost-to-go function at every vertex and visualize their contour plots in Fig. 2(a). In Fig. 2(b), we depict the first three iterations of the 1-step lookahead rollout of the successor policy. At each iteration, we expand the neighbours of the current vertex and greedily select the next vertex $w$ and the vertex point $x_{w}$ that minimize the objective (7a). The rollout proceeds until the target vertex $t$ is reached.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Two-dimensional example", "weight": 1.0} -->

We evaluate the quality of the cost-to-go lower bounds and the resulting solutions in Fig. 4. The optimal shortest path cost-to-go function $J_{s}^{\ast}$ (green) is piecewise-quadratic. Naturally, the convex quadratic lower bound $J_{s}$ (purple) is a poor lower bound to $J_{s}^{\ast}$. The quality of the lower bound is greatly improved via multi-step lookaheads (solid lines, orange for 1-step, blue for 2-step). A horizon-$n$ lookahead produces a piecewise-quadratic lower bound to $J_{s}^{\ast}$, with up to as many quadratic pieces as there are different $n$-step paths from the source vertex $s$. Though neither 1-step nor 2-step lookahead lower bounds are tight, they are sufficient for near-optimal decision making. The costs of the rollouts of the successor policy are plotted as dashed lines; 2-step lookahead rollouts (blue) attain optimal solutions nearly always.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Collision-free motion planning for a robot arm", "weight": 1.0} -->

We now demonstrate that our approach scales well to high-dimensional hardware systems. We study multi-query collision-free motion planning for the KUKA iiwa robotic arm (Fig. 1), tasked with moving virtual items between shelves and bins. Our methodology requires minimal additional offline computation, while delivering significant online speed up with negligible solution quality reduction.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Collision-free motion planning for a robot arm", "weight": 1.0} -->

We first produce an approximate polytopic decomposition of the 7-dimensional collision-free configuration space of the arm. This is done via the IRIS-NP algorithm, and we use IRIS clique seeding to obtain polytopes inside the shelves and bins. We assign a GCS vertex $v$ per polytope in this decomposition. The convex set $\mathcal{X}_{v}$ is the set of linear segments contained within the region, with the segment represented by its endpoints. Two GCS vertices are connected by an edge if the corresponding regions overlap. The resulting graph contains 23 vertices and 68 edges. For each edge $e = {(v,w)}$, we constrain the linear segments at $v$ and $w$ to form a continuous path. The path length is the sum of the Euclidean distances of the linear segments. We define 12 source vertices (6 shelves, 2 vertices per shelf) and 3 target vertices (inside the left, front, and right bins). To generate the quadratic lower bounds on the cost-to-go function, we use the generalization of discussed in Appendix 0.A.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Collision-free motion planning for a robot arm", "weight": 1.0} -->

We evaluate our algorithm in a multi-query scenario: at runtime, the arm is given a random next position to go to, alternating between shelves and bins. We rollout a 1-step lookahead policy to generate paths from shelves to bins, and reverse them to obtain paths from bins to shelves. We evaluate our approach on a total of 120 queries. We compare our algorithm against solving the SPP in GCS from scratch, as well as against the shortcut PRM (sPRM) algorithm, which is its natural sampling based multi-query competitor. We use a high-performance implementation of sPRM based, producing a large roadmap with 10,000 vertices. Our solutions are visualized in Fig. 1; performance comparison is provided in Fig. 5. Similar to how the quality of the PRM solutions depends on the density of the PRM, the quality of solutions obtained with GCS depends on the quality of the polytopic decomposition of the collision-free configuration space. We thus make no claims about the optimality of the solutions in this section.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Collision-free motion planning for a robot arm", "weight": 1.0} -->

Offline, generating cost-to-go lower bounds takes only 6 seconds, which is just 6% of the time that it takes to generate the polytopic decomposition necessary to use GCS. Then online, our policy rollouts are very fast, with a median solve time of 5ms and a maximum of 11ms (we report the parallelized solver time). Our method is on average 40 time faster than the SPP in GCS, producing paths that are only 7% longer on average. Compared to sPRM, our method is on average 110 times faster and produces paths that are 5% shorter on average. We achieve consistent performance in both solve time and path length, unlike sPRM, which shows high variance in both. Overall, compared to these state-of-the-art baselines, the APSP in GCS reduces the online solve times significantly, with minimal compromise in solution quality.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Scalability and ablation on lower bounds and lookahead horizon", "weight": 1.0} -->

In this section, we demonstrate the scalability of our approach and analyze how the coarseness of the cost-to-go lower bounds and the lookahead horizon impact solution quality. First, we show that multi-step lookaheads with quadratic $J_{v}$ yield near-optimal solutions in large graphs. Second, we demonstrate that quadratic lower bounds significantly outperform the affine ones, which are available from the dual of the convex relaxation of the SPP in GCS \[26, App. B\].

<!-- chunk {"id": "body-0067", "role": "body", "section": "Scalability and ablation on lower bounds and lookahead horizon", "weight": 1.0} -->

We consider a randomly generated environment depicted in Fig. 6. We assign a GCS vertex $v$ for each teal box. Each convex set $\mathcal{X}_{v}$ is the set of control points of a cubic Bézier curve within the box (see ). The GCS vertices are connected by a pair of edges if the corresponding teal boxes overlap. The resulting graph has 190 vertices and 540 edges. For each edge, we constrain the vertex Bézier curves to be differentiable at the transition point. The path cost is the sum of squared Euclidean distances between the consecutive control points of the Bézier curves. The source vertex $s$ is at the top, and the target vertex $t$ is at the bottom.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Scalability and ablation on lower bounds and lookahead horizon", "weight": 1.0} -->

We synthesize the quadratic and affine lower bounds over the GCS, which takes 6s and 2s respectively. We then uniformly sample 120 pairs of source and target conditions, and rollout the greedy policy using different lower bounds and lookahead horizons. Optimal solutions are obtained by solving the MICP formulation of the SPP in GCS. Numerical results are reported in Table 1.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Scalability and ablation on lower bounds and lookahead horizon", "weight": 1.0} -->

Table 1 shows that our approach scales well to large problem instances, yielding better solve times than the SPP in GCS. A 2-3 step lookahead policy with a quadratic cost-to-go lower bound produces near-optimal solutions (8-9% median suboptimality) in under 10ms. The SPP in GCS produces slightly better solutions (7% median suboptimality), but due to the size of the graph, the solve-time increases to over 1000ms. For large graph instances, incremental search through the graph via the APSP in GCS achieves competitive solution quality while reducing solve times by up to two-three orders of magnitude.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Scalability and ablation on lower bounds and lookahead horizon", "weight": 1.0} -->

Finally, Table 1 shows that quadratic lower bounds with short-horizon lookaheads offer a good balance between expressive power and solve times. A 3-step lookahead policy with affine lower bounds has a median suboptimality of 80.2%, compared to 8.8% with quadratic lower bounds. Achieving similar solution quality with affine lower bounds requires a lookahead horizon of 8-9 steps, but the resulting rollouts take significantly more time. Fig. 6 shows that 3-step lookahead rollouts with affine lower bounds fail to capture the diversity of optimal solutions. Additionally, low-horizon lookahead policies with affine lower bounds often fail to produce solutions within a reasonable number of iterations, as demonstrated by the failure rate statistics. Overall, we observe that the lookahead policies with quadratic lower bounds perform much better than those with affine ones.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Conclusion and future work", "weight": 1.5} -->

In this work, we generalized the classical All-Pairs Shortest-Paths problem to the Graphs of Convex Sets, and developed practical approximate numerical methods for solving this problem. We demonstrated that a coarse lower bound on the cost-to-go with a greedy multi-step lookahead policy produce near-optimal paths, while significantly reducing solve times. Our methodology effectively scales to high-dimensional set scenarios and large graph instances, enabling practical robotics applications in multi-query settings. We plan to provide an efficient implementation of our approach within the Drake library.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Conclusion and future work", "weight": 1.5} -->

For hardware applications in non-static environments, we are interested in ways to tackle changes to the robot's configuration space, like those arising in object manipulation, as well as addition and removal of obstacles. Assuming the changes are minor, the online search via the multi-step lookahead policy provides natural local adaptation. Changes to the environment can be incorporated into the online policy rollout program via non-convex constraints, similar to.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Conclusion and future work", "weight": 1.5} -->

Finally, we are interested in exploring alternative incremental search policies beyond the multi-step lookahead policy. We expect randomized rollouts inspired by MCTS and A\*-based approaches like to be effective.
