<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Augmented Graphs of Convex Sets and the Traveling Salesman Problem

Topics include Bellman equations, Trajectory optimization, Graphs, Optimization, Traveling salesman problem, Graphs of convex sets, Shortest path problem.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We present a trajectory optimization algorithm for the traveling salesman problem (TSP) in graphs of convex sets (GCS). Our framework uses an augmented graph of convex sets to encode the TSP specification and solve it exactly as a shortest path problem in GCS. We establish a precise relationship between the landmark Bellman-Held-Karp algorithm and the augmented graph of convex sets with a TSP specification. Additionally, we present a branch and bound heuristic that uses minimum 1-trees to obtain certifiably optimal or near optimal solutions and scales to problems far larger than the exact framework can handle. To assess and certify performance, we explore several alternative lower bounds.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Path and motion planning are foundational problems in robotics. Many such problems involve combinatorial optimization, where the optimal solution must be selected from a discrete set of candidates. A canonical example from combinatorial optimization that arises naturally in motion planning contexts is the Traveling Salesman Problem (TSP). The TSP has many practical applications, including vehicle routing, warehouse order picking, and drill hole sequencing. It is formulated as a complete graph on $n$ vertices, where edge weights represent costs between vertices such as distance, time, or monetary value. The solution to the TSP is known as a *tour*: a cycle in which every vertex has degree 2, meaning the *salesman* departs from a starting vertex, visits every other vertex exactly once, and returns to the start. The optimal tour achieves this with minimum total cost. Despite its simple statement, the TSP is well-known to be NP-hard, making general solutions challenging. The best known exact algorithm is the Bellman-Held-Karp (BHK) algorithm, which solves the TSP to optimality via dynamic programming in exponential rather than factorial time.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

The exponential complexity of BHK has motivated a rich literature of heuristics that trade small optimality losses for substantial gains in computational efficiency.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

We build on a framework called Graphs of Convex Sets (GCS), which has been used in path and motion planning problems, to formulate and solve the TSP in GCS (TSP-GCS). GCS associates convex programs with the graph; each vertex is associated with a continuous variable, convex constraint set, and convex objective function, and each edge is associated with a convex set and cost function that couples the vertex variables. When the continuous variables are fixed, the problem reduces to a traditional graph optimization problem over subgraphs, such as shortest paths or TSP tours. When the graph structure is fixed, the problem becomes a convex program that can be efficiently solved. GCS elegantly combines the discrete graph optimization and continuous variable optimization.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

We use an augmented GCS (AGCS), which was developed for motion planning problems with complex temporal logic, to encode the TSP specifications into a new augmented GCS (AGCS-TSPS) that exactly solves the TSP-GCS. However, the AGCS-TSPS scales exponentially with the number of target sets. An example workflow for a seven target set graph can be seen in Figure 1.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop heuristics and lower bounds to solve larger instances which would be intractable for exact methods. Our best heuristic uses bounded edge costs, the minimum cost between two convex sets, to approximate the problem as a traditional graph problem. This heuristic uses the Minimum 1-Tree (MOT) combined with branch and bound techniques to achieve optimal or near optimal solutions.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Our contributions", "weight": 1.0} -->

We establish a precise relationship between the AGCS-TSPS and the BHK algorithm, showing how it converts the TSP-GCS into a Shortest Path Problem in Graphs of Convex Sets (SPP-GCS). We discuss how the AGCS potentially provides better lower bounds and heuristics for the TSP-GCS.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Our contributions", "weight": 1.0} -->

We develop a heuristic for the TSP-GCS that uses minimum 1-trees (MOTs) and a branch and bound method to obtain certifiably optimal or near optimal solutions.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Our contributions", "weight": 1.0} -->

We create a mixed-integer convex formulation for the MOT in GCS (MOT-GCS).

<!-- chunk {"id": "body-0011", "role": "body", "section": "Our contributions", "weight": 1.0} -->

We develop four lower bounds for the TSP-GCS.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Our contributions", "weight": 1.0} -->

We develop a new metric called the bounded edge cost, the minimum cost between two convex sets. This metric is capable of converting a GCS problem into a traditional graph problem to obtain a base solution.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The objective is a weighted sum of the trajectory length and the time horizon with weights $\alpha$ and $\beta$, respectively. The first constraint is a temporal logic specification that requires each target set to be eventually visited, but does not specify a visit order. The second constraint requires the velocity to be in the convex set $\mathcal{Q}$ for all time. The last two constraints enforce the tour structure. The third requires that the initial and terminal positions, located in the initial target set, be equal. Without a visit order, any target set can be the initial target set. The fourth constraint requires the initial and terminal velocities to be equal for dynamic feasibility.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The optimization problem is infinite-dimensional, so candidate trajectories can be parameterized with piecewise Bézier curves defined by a finite set of control points. It is straightforward to include additional objective function terms and constraints that are convex in this parameterization. For example, penalties and constraints on higher-order derivatives promote additional smoothness on the trajectory $q$. Ensuring that the trajectory is differentiable a certain number of times facilitates the design of dynamically feasible trajectories for fully actuated and differentially flat systems.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-A TSP Specification via Signal Temporal Logic", "weight": 1.0} -->

We use Signal Temporal Logic (STL) to encode the TSP specification. STL is a variation of temporal logic that offers a general and powerful framework to specify complex spatiotemporal tasks and constraints. A STL formula can be composed from the following grammar

<!-- chunk {"id": "body-0016", "role": "body", "section": "II-A TSP Specification via Signal Temporal Logic", "weight": 1.0} -->

by starting from a set of atomic propositions $AP$ with $p \in {AP}$ and recursively applying boolean operators: $\neg$ (not), $\land$ (and), and $\vee$ (or), and temporal operators: $\mathcal{U}$ (until), and $\mathcal{R}$ (release). The until operator $\phi\mathcal{U}\psi$ is satisfied if $\phi$ remains true until $\psi$ becomes true. The release operator $\phi\mathcal{R}\psi$ is satisfied if $\psi$ remains true until and including when $\phi$ becomes true, and if $\phi$ never becomes true, then $\psi$ always remains true; in other words, $\phi$ releases $\psi$.

<!-- chunk {"id": "body-0017", "role": "body", "section": "II-A TSP Specification via Signal Temporal Logic", "weight": 1.0} -->

Additional temporal operators can be defined, such as eventually (${\mathcal{F}\varphi}:={\top{\mathcal{U}\varphi}}$) and always (${G\varphi}:={\neg{\mathcal{F}{\neg\varphi}}}$). STL operators and formulas can also be restricted to hold over specific and finite time intervals.

<!-- chunk {"id": "body-0018", "role": "body", "section": "II-A TSP Specification via Signal Temporal Logic", "weight": 1.0} -->

The traveling salesman specification can be expressed using the eventually operator.

<!-- chunk {"id": "body-0019", "role": "body", "section": "II-A TSP Specification via Signal Temporal Logic", "weight": 1.0} -->

which requires all target sets to be eventually visited but does not specify an ordering.

<!-- chunk {"id": "body-0020", "role": "body", "section": "II-B Graphs of Convex Sets", "weight": 1.0} -->

A general optimization problem on the GCS is

<!-- chunk {"id": "body-0021", "role": "body", "section": "II-B Graphs of Convex Sets", "weight": 1.0} -->

where the variables are the (discrete) subgraph $H$ with vertex set $\mathcal{W} \subseteq \mathcal{V}$ and edge set $\mathcal{F} \subseteq {\mathcal{W}^{2} \cap \mathcal{E}}$ within an admissible subset of graphs $\mathcal{H}$ and the (continuous) variables $x_{v}$ for each vertex $v \in \mathcal{W}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-B1 Shortest Path Problem in GCS", "weight": 1.0} -->

For a given start vertex $s \in \mathcal{V}$ and target vertex $t \in \mathcal{V}$, a path $p$ is a sequence of distinct vertices that connects $s$ to $t$ via an edge subset $\mathcal{F} \subset \mathcal{E}$. The general problem can be specialized to the Shortest Path Problem (SPP) by taking $\mathcal{H}$ as the set of all paths, $\mathcal{P}$, from $s$ to $t$ in the graph $\mathcal{G}$. The SPP-GCS is stated as

<!-- chunk {"id": "body-0023", "role": "body", "section": "II-B1 Shortest Path Problem in GCS", "weight": 1.0} -->

This problem seeks to simultaneously find a (discrete) path in the graph from the start vertex to the target vertex and the (continuous) values $x_{v}$ for each vertex that together minimize the total edge length across all edges in the path. Although this problem is computationally difficult in general, a novel and tight mixed-integer formulation was developed. This formulation uses a network flow formulation of the shortest path problem and exploits duality between perspective cones and valid inequality cones to convexify bilinear constraints that arise from the continuous vertex variables.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B2 Minimum Spanning Tree Problem in GCS", "weight": 1.0} -->

A spanning tree $\tau$ is a connected subgraph of $\mathcal{G}$ with no cycles that contains every vertex of $\mathcal{G}$. The general problem can be specialized to the Minimum Spanning Tree Problem (MSTP) by taking $\mathcal{H}$ as the set of all spanning trees, $\mathcal{T}$, of $\mathcal{G}$. The Minimum Spanning Tree Problem in Graphs of Convex Sets (MSTP-GCS) is stated as

<!-- chunk {"id": "body-0025", "role": "body", "section": "II-B2 Minimum Spanning Tree Problem in GCS", "weight": 1.0} -->

In the Minimum Spanning Arborescence Problem (MSAP), the directed version of the MSTP, was formulated using cutset constraints and the same convexification of the bilinear constraints. By replacing these cutset constraints with subtour constraints and making all edges undirected, a mixed-integer formulation can be constructed for the MSTP-GCS. Due to the exponential number of subtours, these subtour constraints are added as lazy constraints rather than all at once.

<!-- chunk {"id": "body-0026", "role": "body", "section": "II-B3 Traveling Salesman Problem in GCS", "weight": 1.0} -->

A tour $\sigma$ is a connected subgraph of $\mathcal{G}$ with only one cycle that contains every vertex of $\mathcal{G}$. The general problem can be specialized to the TSP by taking $\mathcal{H}$ as the set of all tours, $\mathcal{O}$, of $\mathcal{G}$. The TSP-GCS is stated as

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-B3 Traveling Salesman Problem in GCS", "weight": 1.0} -->

Unlike the SPP-GCS, the MSTP-GCS, and TSP-GCS are not tight. For this reason, we will take a similar approach as in and will reformulate the TSP into an SPP using AGCS. We will demonstrate that a shortest path in this AGCS exactly solves problem by solving it as.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Augmented GCS Construction for TSP", "weight": 1.0} -->

In this section, we describe how to construct an AGCS that encodes the TSP Specification (AGCS-TSPS) based on the labeled GCS $\mathcal{G}{(\mathcal{V},\mathcal{E})}$ from Section II-B. The AGCS-TSPS consists of copies of $\mathcal{G}{(\mathcal{V},\mathcal{E})}$ that encode the specific set of visited target sets.

<!-- chunk {"id": "body-0029", "role": "body", "section": "III-A Constructing the AGCS-TSPS", "weight": 1.0} -->

The AGCS-TSPS is built recursively from the labeled graph $\mathcal{G}{(\mathcal{V},\mathcal{E})}$ based on an initial target set $s \in \mathcal{V}$ whose corresponding convex set contains the initial condition. The augmented GCS consists of $n_{\mathcal{K}}$ layers, where each layer represents visited target subsets of a certain cardinality. Figure 2 shows an example where $n_{\mathcal{K}} = 5$, which will be a useful reference to supplement the AGCS-TSPS construction.

<!-- chunk {"id": "body-0030", "role": "body", "section": "III-A Constructing the AGCS-TSPS", "weight": 1.0} -->

The Base Layer. The base layer of the AGCS-TSPS corresponds to the starting target set. Since no visit order is specified, any target set is a valid starting set. This target set will be indexed as $i = 0$ and will correspond to the target set $\{\mathcal{K}_{0}\}$. Unlike the AGCS with precedence specifications, this subgraph does not need to be modified and will contain the exact same target and edge sets as $\mathcal{G}{(\mathcal{V},\mathcal{E})}$ only with each target set having a suffix denoting which set it belongs to. For example, target sets $\mathcal{K}_{0}$ and $\mathcal{K}_{1}$ will be $\mathcal{K}_{0}{\{ 0\}}$ and $\mathcal{K}_{1}{\{ 0\}}$, respectively. This is done to identify which target set belongs to which subgraph.

<!-- chunk {"id": "body-0031", "role": "body", "section": "III-A Constructing the AGCS-TSPS", "weight": 1.0} -->

Layer 2. The second layer of the AGCS-TSPS corresponds to the 3-element visited target sets, $S_{2} \subset {\mathcal{K} \cup {\{\mathcal{K}_{0}\}}}$, where ${|S_{2}|} = 3$. For each subgraph in this layer, a copy of $\mathcal{G}{(\mathcal{V},\mathcal{E})}$ is used, and each target set is given a suffix. A single directed edge is added from each subgraph in layer 1 to the new subgraph in layer 2. For example, subgraph $\{ 0,1,2\}$ has parent sets $\{ 0,1\}$ and $\{ 0,2\}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Constructing the AGCS-TSPS", "weight": 1.0} -->

Layer $\ell.$ In general, layer $\ell$ consists of subgraphs corresponding to all $({\ell + 1})$-element visited target sets, $S_{\ell} \subset {\mathcal{K} \cup {\{\mathcal{K}_{0}\}}}$ where ${|S_{\ell}|} = {\ell + 1}$. Like before, a copy of $\mathcal{G}{(\mathcal{V},\mathcal{E})}$ is used with a suffix applied to each target set. Each subgraph in this layer will have $\ell$ directed edges connected to subgraphs in layer $\ell - 1$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A Constructing the AGCS-TSPS", "weight": 1.0} -->

Layer $n_{\mathcal{K}} - 1$. The final layer will consist of only one subgraph which has visited every target set $S_{n_{\mathcal{K}} - 1} = \mathcal{K}$ where ${|S_{n_{\mathcal{K}} - 1}|} = n_{\mathcal{K}}$. Just like before, a directed edge will be added connecting every subgraph in the previous layer to the final subgraph. For example, if $n_{\mathcal{K}} = 5$, then an edge will be added between ${\mathcal{K}_{1}{\{ 0,2,3,4\}}}\rightarrow{\mathcal{K}_{1}{\{ 0,1,2,3,4\}}}$ connecting subgraphs ${\{ 0,2,3,4\}}\rightarrow{\{ 0,1,2,3,4\}}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A Constructing the AGCS-TSPS", "weight": 1.0} -->

By specifying $\mathcal{K}_{0}{\{ 0\}}$ as the initial target set and $\mathcal{K}_{0}{\{ 0,\ldots,{n_{\mathcal{K}} - 1}\}}$ as the terminal target set alongside the directed edges connecting the subgraphs, the AGCS-TSPS has reformulated the TSP-GCS as a SPP-GCS using STL. The network flow constraints in the SPP conveniently replace the degree constraint of each target set and the directed edges between and within subgraphs replace the subtour constraints. Additionally, to convert the shortest path into the optimal tour, we must add the constraint, $x_{s} = x_{t}$, without it, the initial and terminal target set locations would differ. This now allows methods from to compute a shortest path in the AGCS-TSPS. A summary of the algorithm can be found in Algorithm 1.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B Connecting AGCS-TSPS and the BHK Algorithm", "weight": 1.0} -->

One core element of the AGCS-TSPS and the BHK algorithm is the use of binary subsets. These binary subsets are sorted by size in both the AGCS-TSPS and the BHK algorithm and are methodically examined by set size in increasing order. In the AGCS-TSPS, this is done using directed edges between subgraphs, which prevent backtracking in a dynamic programming style. In the BHK algorithm, this is done with a cost matrix that uses dynamic programming directly to avoid recomputing unnecessary solutions. For example, if it has been determined by the BHK algorithm that the path $0\rightarrow 1\rightarrow 2\rightarrow 3$ is shorter than $0\rightarrow 2\rightarrow 1\rightarrow 3$, then the path $0\rightarrow 1\rightarrow 2\rightarrow 3\rightarrow 4$ must be shorter than $0\rightarrow 2\rightarrow 1\rightarrow 3\rightarrow 4$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-B Connecting AGCS-TSPS and the BHK Algorithm", "weight": 1.0} -->

This behavior is explicitly encoded in the AGCS-TSPS, the only difference being that the computation that determines if the path $0\rightarrow 1\rightarrow 2\rightarrow 3$ is shorter than the path $0\rightarrow 2\rightarrow 1\rightarrow 3$ in the BHK is a simple operation and a complex operation in the AGCS-TSPS. Both algorithms scale exponentially in the number of target sets due to the exponential number of binary subsets. The shows how the AGCS-TSPS generalizes the BHK algorithm in the GCS setting.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-C Properties of the AGCS-TSP", "weight": 1.0} -->

By construction, every path in the AGCS-TSPS from the initial target set to the terminal target set satisfies the traveling salesman specifications. Therefore, a shortest path in the AGCS-TSPS corresponds to an optimal solution of the original problem. The mixed-integer convex reformulation of the AGCS-TSPS based on thus exactly solves, up to a finite parameterization of the trajectory $q$ (e.g., using Bézier curves). It is guaranteed to find a path if one exists (in the absence of a bound on the horizon $T$).

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-C Properties of the AGCS-TSP", "weight": 1.0} -->

A convex relaxation of the exact mixed-integer formulation, obtained by simply dropping the binary constraints, along with an inexpensive rounding scheme, can be used to obtain approximate solutions to. It was observed in that in many practical motion planning problems (without specifications), this relaxation is often tight and provides certifiably near-optimal solutions. We will study the tightness of this relaxation for problems with TSP specifications in our numerical experiments.

<!-- chunk {"id": "body-0039", "role": "body", "section": "III-D Size of the AGCS-TSPS", "weight": 1.0} -->

The number of subgraphs in the AGCS-TSPS is directly correlated to the number of target sets. The number of subgraphs in the AGCS-TSPS is $2^{n_{\mathcal{K}}}$. This is the same as the upper bound obtained in for the AGCS with precedence specifications where all keys are reachable by every other key. A graph $\mathcal{G}{(\mathcal{V},\mathcal{E})}$ with $|\mathcal{V}|$ vertices (target sets) will have ${|\mathcal{E}|} = {{|\mathcal{V}|} \cdot {({{|\mathcal{V}|} - 1})}}$ edges, since each edge must be directed.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Lower Bounds for the TSP-GCS", "weight": 1.0} -->

The best known lower bound for the TSP is the weighted 1-tree derived by Held-Karp. It is well known that the MST is a lower bound for the TSP, since removing a single edge from the minimum tour will result in a spanning tree (not necessarily a MST). A 1-tree is a spanning tree created from all the vertices in a graph except one, and connecting this vertex to form exactly one cycle. This excluded vertex is called the root. A Minimum 1-Tree (MOT) is a MST on all vertices except the root, with the two cheapest edges from the root connecting to the MST. The MOT is a better lower bound for the TSP compared to the MST. The reason is if every vertex in the MOT has degree 2, then the MOT is an optimal tour for the TSP. In other words, the additional edge in the MOT makes it a better lower bound to the TSP than the MST. In other words, $\text{MST} \leq \text{MOT} \leq \text{TSP}$. We will now discuss four different approaches to lower bound the TSP-GCS.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-A Minimum 1-Tree in GCS", "weight": 1.0} -->

For a given root vertex $r \in \mathcal{V}$, a 1-tree $\alpha$ is a spanning tree $\tau$ with vertices $\mathcal{V} \smallsetminus {\{ r\}}$, with two edges connecting $r$ to the spanning tree $\tau$ creating exactly one cycle. The general problem can be specialized to the Minimum 1-Tree Problem (MOTP) by taking $\mathcal{H}$ as the set of all 1-trees, $\mathcal{A}$, of $\mathcal{G}$. The MOT in GCS (MOT-GCS) is stated as

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-A Minimum 1-Tree in GCS", "weight": 1.0} -->

The MOT can be efficiently solved when using MSTP algorithms. Such algorithms are not known for the MSTP-GCS. This is because, the MSTP-GCS, and by extension the MOT-GCS, are NP-hard. This is similar to how the SPP can be efficiently solved, but the SPP-GCS is NP-hard. The most computationally efficient lower bound is the MOT-GCS relaxation (MOT-GCS\*).

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-B Traveling Salesman Relaxation Lower Bound", "weight": 1.0} -->

For integer programs, a guaranteed lower bound, which is often used as a starting feasible solution, is the relaxation of the integer constraints. If the relaxation is tight, then the relaxation is a good approximation of the integer program. This, however, is not the case for the TSP as shown. It is assumed that this translates over to the TSP-GCS.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-C AGCS-TSPS Relaxation Lower Bound", "weight": 1.0} -->

As previously stated, the AGCS-TSPS has a tighter formulation compared to the TSP-GCS. If the integer constraints are relaxed on the AGCS-TSPS, this will produce a lower bound for the TSP-GCS.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-D Bounded Edge Costs", "weight": 1.0} -->

GCS problems are complicated due to the variable edge costs that are dependent on which vertices are selected. Many traditional graph algorithms use a cost matrix or equivalent structure to select edges in a systematic way based on the static cost of said edges. This cannot be done in the GCS case. One possible way to approximate this cost would be to take the Chebyshev center of each vertex and use these centers as fixed $x_{v}$ for problem. The problem with this approach is that the proposed solution from fixing $x_{v}$ in this way can be larger than the true optimal solution to. A better approach would be to use bounded edge costs, which lower bound the edge cost between any pair of vertices. This can be done by solving a simple convex program which minimizes the edge cost between each pair of vertices. This simple convex program is stated as

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-D Bounded Edge Costs", "weight": 1.0} -->

Since many problems in GCS will be minimizing a cost function, a lower bound on this optimal cost is preferred. These bounded edge costs can be used to construct a cost matrix or equivalent structure and be passed to traditional graph problems to create base solutions for any GCS problems. This base solution will contain a set of edges which will fix $H$. This would convert the problem into a convex program which will produce a realized cost of the selected bounded edges. This realized cost is lower bounded by the bounded edge cost. The realized cost does not lower bound the optimal solution. Figure 3 shows one example where the optimal bounded cost produces a realized cost that is larger than the optimal cost of the TSP-GCS. The key takeaway is that the optimal bounded cost will lower bound the optimal solution to, and that the realized cost of the optimal bounded cost does not. The best way to obtain a lower bound is to use bounded edge cost matrix in the MOTP since it can be efficiently solved.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Heuristic for the Traveling Salesman Problem in Graphs of Convex Sets", "weight": 1.0} -->

In practice, heuristics are used to obtain optimal or near optimal solutions for the TSP, given the problem is NP-hard. This would apply to the TSP-GCS since the problem is at least as hard as the TSP. The heuristic that will be discussed in this section uses bounded edge costs with MOTs to create a promising bounded cost tour which will then be realized.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Heuristic for the Traveling Salesman Problem in Graphs of Convex Sets", "weight": 1.0} -->

Weighted 1-Trees. As mentioned in Section IV-A, MOTs are both efficient to compute and provide better lower bound potential for the TSP. These can provide even better lower bounds for the TSP by using penalty terms, $\pi$, which can be used to penalize vertices with degrees larger than 2, and reward vertices with degree 1 to incentivize a MOT where all vertices have degree 2. This method is known as the Lagrangian relaxation, developed by Held-Karp, which moves difficult constraints into the objective function. Here the penalty terms are added to each edge cost $c_{ij}$ by converting each edge cost into a new cost, ${\overline{c}}_{ij} = {c_{ij} + \pi_{i} + \pi_{j}}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Heuristic for the Traveling Salesman Problem in Graphs of Convex Sets", "weight": 1.0} -->

By doing so, the degree constraints are added into the objective function. These penalties will increase the cost of any tour by exactly $2{\sum_{i = 0}^{n - 1}\pi_{i}}$ since every vertex in a tour will have degree 2. An ascent method is used to update the values of $\pi_{i}$ based on the degree of vertex $i$ using the following formula at every $k$-th iteration

<!-- chunk {"id": "body-0050", "role": "body", "section": "Heuristic for the Traveling Salesman Problem in Graphs of Convex Sets", "weight": 1.0} -->

Here $t$ is the step size used for the ascent method and $d_{k}$ is the vector of vertices degrees at the $k$-th iteration. With these penalty terms at every $k$-th iteration, a MOT is computed using $\pi_{k}$ and based on this MOT, $\pi_{k + 1}$ is updated and the process repeats. This method can be improved by using branch and bound methods.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Heuristic for the Traveling Salesman Problem in Graphs of Convex Sets", "weight": 1.0} -->

Branch and Bound. Once the ascent method has run for a set amount of iterations, the resulting 1-tree is passed to a branch and bound method. The purpose of the branch and bound is to find vertices with degrees larger than 2, examine the edges associated with these vertices and select one edge to begin the branching process. The edge selected is the one with the highest bounded cost, as this will be the most influential edge. This selected edge will branch in two directions. In the first direction the edge is forced to be in the 1-tree and the other one it is forbidden to be in the 1-tree. Kruskal's MSTP algorithm, which builds a MST using disconnected components, implements both criteria naturally. To reuse some information, the $\pi$ from the last iteration of the ascent method is passed on to each branch. A limit can be imposed on how many branching operations can be made, and the maximum number of forced/forbidden edges in a branch to help with computations.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Heuristic for the Traveling Salesman Problem in Graphs of Convex Sets", "weight": 1.0} -->

Upper Bound. To be able to bound each branch, a cheap upper bound is needed to prune any branches that are not promising. The upper bound is initialized as a greedy tour using bounded edge costs that starts from a random vertex. This greedy tour is then used as an initial tour for the 2-Opt heuristic to improve the initial tour, if at all. The 2-Opt heuristic takes a tour such as $$, which means $0\rightarrow 1\rightarrow 2\rightarrow 3\rightarrow 4\rightarrow 0$, performs two edge swaps which reverses a part of the tour and compares the cost of the old edges versus the new edges. For example, the tour $$ can be improved by the 2-Opt heuristic to produce $$ which would swap edges ${}\text{~and~}{}$ with ${}\text{~and~}{}$. Using bounded edge costs the 2-Opt heuristics is just as efficient in GCS as it is in the traditional graph setting.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Heuristic for the Traveling Salesman Problem in Graphs of Convex Sets", "weight": 1.0} -->

A better, but more computationally demanding option is to check each swap with using the candidate tour for $\sigma$.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Heuristic for the Traveling Salesman Problem in Graphs of Convex Sets", "weight": 1.0} -->

At each branch, if a tour is found and it is better than the current upper bound, it replaces the upper bound. Branches are explored based on the cost of the MOT from the ascent method. Once the branch and bound heuristic has explored all branches, or the maximum number of branches, the resulting tour can be realized by solving using the fixed $\sigma$ to obtain a realized cost of the best bounded tour. A summary of this algorithm can be found in Algorithm 2.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Heuristic for the Traveling Salesman Problem in Graphs of Convex Sets", "weight": 1.0} -->

0: Bounded Cost Matrix C, Optional: max iterations MAX 0: Best TSP Tour σ 1: Compute upper bound tour $\overline{\sigma}$ using C and $\sigma\leftarrow\overline{\sigma}$ 2: Initialize min_heap with lower bound $\underset{¯}{\sigma}\leftarrow{- \infty}$ forbidden set SX:= ⌀, forced set SY:= ⌀, π = 0 4: while min_heap is not empty and i&lt; MAX do 6: ${\underset{¯}{\sigma},S_{X},S_{Y},\pi}\leftarrow$ min_heap.pop

<!-- chunk {"id": "body-0056", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

In this section, we run some numeric examples on a set of randomly generated instances. These randomly generated instances consist of $n_{\mathcal{K}}$ randomly generated polytope target sets placed uniformly on a $n_{\mathcal{K}} \times n_{\mathcal{K}}$ grid. Specific tractable sizes were solved to optimality to serve as benchmark examples. To simplify the analysis, the Euclidean distance was used as the edge cost function. For all comparisons with the benchmark examples, the percent error was calculated for the lower bound $\underset{¯}{\delta}$ and heuristic $\overline{\delta}$ with a tolerance of $0.0001$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Numerical Experiments", "weight": 1.0} -->

All experiments were performed on a laptop with an Intel Core Ultra 7 258V and 32 GB of ram. Experiments were performed using CVXPY, GCSOPT, and Gurobi.

<!-- chunk {"id": "body-0058", "role": "body", "section": "VI-A Numeric Experiments using the AGCS-TSPS", "weight": 1.0} -->

As stated in Section III-D, the scalability of the AGCS-TSPS is limited, even when using the relaxation. For this reason only select instances were used to compare the AGCS-TSPS to the TSP-GCS. Table I shows the cost and time comparison between the TSP-GCS and AGCS-TSPS, and their relaxations. The AGCS-TSPS relaxation uses a cheap rounding scheme.

<!-- chunk {"id": "body-0059", "role": "body", "section": "VI-B Numeric Experiments for Lower Bounds", "weight": 1.0} -->

To compare the proposed lower bounds mentioned in Section IV, benchmark tests were created for sizes $n_{\mathcal{K}} = {5,10,15}$ to get different types of sample sizes. For each size 1000 different instances were created to build up a set of benchmark tests to compare lower bounds. The lower bounds used are the TSP-GCS relaxation (TSP-GCS\*), MOT-GCS relaxation (MOT-GCS\*), and the Weighted 1-Tree with Bounded edge costs (WOT-B). It was shown in the previous section that the AGCS-TSPS is intractable even for small sizes. For this reason it was not considered for this set of numeric experiments. Table II, shows the comparison of the percent error $\underset{¯}{\delta}$ between the lower bounds of interest.

<!-- chunk {"id": "body-0060", "role": "body", "section": "VI-C Numerical Experiments with Branch and Bound Heuristic", "weight": 1.0} -->

We evaluated the performance of the heuristic described in Algorithm 2 against the same set of benchmark tests used in the lower bound calculation. The ascent method is capped at 1000 iterations with a step size of 2 that decreases by 5% each iteration. Table III shows the percent error of the heuristic $\overline{\delta}$ between the benchmark tests and the branch and bound heuristic. Table IV shows the time comparison between the two algorithms to further test the performance of the heuristic.

<!-- chunk {"id": "body-0061", "role": "body", "section": "VI-C Numerical Experiments with Branch and Bound Heuristic", "weight": 1.0} -->

Discussion. From Table I, we can observe that the AGCS-TSPS can optimally solve the TSP-GCS, but is limited in scale due to its exponential nature. The number of edges in the AGCS-TSPS even in the smallest case, where $n_{\mathcal{K}} = 5$, has 352 edges compared to the 20 present in the TSP-GCS, almost 18 times more edges (and thus binary variables). This shows that although the AGCS-TSPS has a tighter formulation than the TSP-GCS itself, its complexity makes it hard to take advantage of this fact. From the results in Table II the most reliable lower bound is the TSP-GCS\*. Based on the results in Table III, this heuristic is capable of finding the optimal solution in $62.0 - {95.2\%}$ of cases, and when it does not the solution is only off by $0.0265 - {0.2531\%}$. This heuristic is not perfect, as seen here the largest $\overline{\delta}$ was $8.8633\%$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "VI-C Numerical Experiments with Branch and Bound Heuristic", "weight": 1.0} -->

This sacrifice in optimality can be made up for by the speed of this heuristic, which from Table IV is about two orders of magnitude faster while producing near optimal solutions.

<!-- chunk {"id": "body-0063", "role": "body", "section": "VI-C Numerical Experiments with Branch and Bound Heuristic", "weight": 1.0} -->

Future Work. From Table II and Figure 4 it can be seen that better lower bounds and heuristics are needed for the TSP-GCS for larger $n_{\mathcal{K}}$. One potential use of the AGCS-TSPS would be to translate TSP heuristics and apply them to the AGCS-TSPS to prune subgraphs. Figure 5 shows how a 2-Opt heuristic could work in the AGCS-TSP by converting the tour $$ into $$ which swaps edges $$ and $$ for $$ and $$. This would replace subgraph $\{ 0,2,4\}$ with $\{ 0,1,4\}$ in the AGCS-TSPS. Superimposing these two paths can form a sub-AGCS of the AGCS-TSPS that could be solved more efficiently. Also note that if a path in the AGCS-TSPS has been selected there is no need to include the other target sets or edges, reducing the edge and vertex count in the AGCS-TSPS significantly.

<!-- chunk {"id": "body-0064", "role": "body", "section": "VI-C Numerical Experiments with Branch and Bound Heuristic", "weight": 1.0} -->

Future work will explore applying heuristics, such as the 2-Opt, to the AGCS-TSPS to create more efficient algorithms that can exploit the tightness of the SPP-GCS formulation. We will also investigate the role that obstacles play in reducing the overall size of the AGCS-TSPS due to the partition of the free space limiting the options between different target sets.
