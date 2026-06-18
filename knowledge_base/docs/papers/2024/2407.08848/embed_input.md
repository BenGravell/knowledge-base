<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

GCS*: Forward Heuristic Search on Implicit Graphs of Convex Sets

Topics include Motion planning, Probabilistic models, Graphs, Sampling-based methods, Planning, Sampling, Graphs of convex sets.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We consider large-scale, implicit-search-based solutions to Shortest Path Problems on Graphs of Convex Sets (GCS). We propose GCS*, a forward heuristic search algorithm that generalizes A* search to the GCS setting, where a continuous-valued decision is made at each graph vertex, and constraints across graph edges couple these decisions, influencing costs and feasibility. Such mixed discrete-continuous planning is needed in many domains, including motion planning around obstacles and planning through contact. This setting provides a unique challenge for best-first search algorithms: the cost and feasibility of a path depend on continuous-valued points chosen along the entire path. We show that by pruning paths that are cost-dominated over their entire terminal vertex, GCS* can search efficiently while still guaranteeing cost-optimality and completeness. To find satisficing solutions quickly, we also present a complete but suboptimal variation, pruning instead reachability-dominated paths. We implement these checks using polyhedral-containment or sampling-based methods. The former implementation is complete and cost-optimal, while the latter is probabilistically complete and asymptotically cost-optimal and performs effectively even with minimal samples in practice.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We demonstrate GCS* on planar pushing tasks where the combinatorial explosion of contact modes renders prior methods intractable and show it performs favorably compared to the state-of-the-art.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Many real-world planning problems involve making discrete and continuous decisions jointly. Collision-free motion planning selects whether to go left or right around an obstacle along with a continuous trajectory to do so. In Task and Motion Planning (TAMP), discrete task-level decisions about the type and sequence of actions are intimately coupled with continuous robot motions and object configurations. For example, where a robot grasps a hockey stick impacts its ability to hook an object; in the construction of a tower, the order in which materials are assembled, as well as their geometric relationships, affect stability.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A natural representation of such a problem structure is the Graph of Convex Sets (GCS). In a GCS, graph vertices represent these discrete choices, with edges denoting allowed transitions. A continuous decision within each vertex is encoded by a point constrained to lie within a convex set associated with the vertex. For example, the free configuration space around an obstacle may be (sometimes approximately) decomposed into a number of intersecting convex regions in which trajectory segments can be planned. The point associated with each vertex, which encodes the motion within the corresponding free-space region, could be, for example, a sequence of positions at a fixed number of knot points. In the case of a single knot point, the associated vertex's convex set is simply the corresponding convex free-space set. In the case of more knot points, the vertex's set would be the higher-dimensional set in which each knot point is contained within the free-space set. In this example, intersecting free-space regions lead to graph edges. A valid way to get around the obstacle involves a path -- a sequence of vertices -- through the graph, along with a trajectory -- a sequence of continuous-valued points assigned to vertices on the path.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Importantly, in such problems, there may be constraints coupling points across edges, presenting a fundamental difference from classical graph search problems. For example, for trajectory continuity, knot points across an edge must coincide.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

While Shortest-Path Problems (SPPs) in discrete graphs can be solved in polynomial time, SPPs in GCS are NP-hard. GCS can be solved with a Mixed-Integer Convex Program (MICP) formulation; Marcucci et al. give a notably scalable transcription of SPPs in GCS with a tight convex relaxation. However, these approaches become intractable as the graph grows. Many discrete-continuous problems exhibit a combinatorial explosion of discrete modes, e.g., in a manipulation task where contact dynamics between every pair of bodies are considered. In TAMP, the search space is typically so large that explicit enumeration of the search space is impractical.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

For such problems, we can instead define a graph implicitly via a source vertex and a successor operator that acts on a vertex and returns all outgoing edges. Implicit graph search algorithms use this representation to solve SPPs without loading the entire graph in memory. A\* is forward heuristic search algorithm which can solve the SPP on implicit discrete graphs. However, key differences between discrete graphs and GCS make search in GCS more challenging.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

The SPP on a discrete graph has the optimal substructure property: All sub-paths of an optimal path between two vertices are themselves optimal paths between the first and last vertices they traverse. A\* (or any best-first search algorithm) leverages this property, pruning a sub-path when its cost-to-come is dominated by another sub-path terminating in the same vertex because it cannot be a sub-path of any optimal path. However, the SPP on a GCS lacks the optimal substructure property. Importantly, as exemplified in fig. 2 and by Morozov et al., a sub-path of an optimal path on a GCS is not necessarily an optimal path between that subpath's first and last vertices. Thus, when considering whether a partial path to the target could be a sub-path of an optimal path, it is insufficient to ask whether it is the cheapest way to reach its terminal vertex. As a result, a naive application of A\* to GCS could prune an important sub-path, preventing the optimal path from being returned.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We leverage the key insight that, while the optimal substructure property does not hold on the path level in GCS, it does hold on the trajectory level: Given an optimal path and corresponding trajectory, any sub-path is optimal to reach its own final point, as exemplified in fig. 2 (b). That is, while an optimal path may not contain an optimal subpath to reach each vertex it visits, its trajectory is optimal to reach each point it visits. In order to maintain this property, we place no restrictions on the number of times a path may revisit vertices. Formally, paths that may revisit vertices are generally referred to as "walks," but for readability we continue to use "path" even though this term traditionally excludes cycles.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

The trajectory-level optimal substructure property holds because the optimal way to reach a point is independent of the optimal way to continue on from it. However, this is only true if visiting a particular vertex on the way to that point does not exclude that vertex from being visited subsequently. It is well-known that shortest paths on discrete graphs never revisit vertices; however, this does not hold on a GCS because a different point may be visited each time.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

More severe than the loss of optimality is the loss of completeness. Because a GCS may have constraints coupling points across edges, a path may not be feasible even if edges connect the sequence of vertices. As a result, A\* on a GCS might prune a candidate path even though the cheaper alternate path is infeasible for reaching the target. An example is shown in fig. 3.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we address these challenges and generalize A\* to the GCS setting. We call our algorithm GCS\* (sec. 4), leveraging two key insights. First, to retain optimality, the algorithm must keep track of every path that reaches any point in a set more cheaply than alternate paths. Second, to retain completeness, the algorithm only needs to keep track of every path that reaches previously unreached points within a set. These insights give rise to domination checks we call ReachesCheaper and ReachesNew, respectively (sec. 4.2.2). Using ReachesCheaper with an admissible heuristic makes GCS\* optimal, while using ReachesNew prunes paths more aggressively, sacrificing optimality for speed, but retaining completeness^11^1Similar to A\*, GCS\* is complete if a solution exists or the user defines a limit on the length of paths that can be returned.. We present polyhedral-containment-based implementations of these checks and prove completeness and optimality of GCS\* (sec. 4.3).

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

However, we achieve significant speed improvements with only mildly suboptimal results with sampling-based implementations, under which GCS\* is probabilisitically complete and asymptotically cost optimal, i.e., complete and optimal in the limit of infinite samples. The theoretical properties of each variant of the algorithm are summarized in table 2.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

Finally, we formulate planar pushing as a GCS problem in sec. 5 and share GCS\* results for tasks with multiple moving objects and multi-step solutions in sec. 6. Such problems are notorious for combinatorially exploding discrete options. For example, the STACK task (fig. 1) leads to approximately $10^{9}$ sets and up to $10^{18}$ edges, making it wildly intractable for methods that require loading the graph into memory, but sampling-based GCS\* finds a solution in 21.9 seconds. Two key strengths of the best-first search framework extend to GCS\*. First, GCS\* is able to solve huge problems that are intractable for methods which require explicit construction of the graph. Second, search effort is proportional to query difficulty. In contrast, methods that solve the problem as a single optimization program require full effort regardless of query difficulty. Similar to A\*, GCS\* also guides the search using a priority function that sums the cost-to-come and heuristic cost-to-go.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

Exactly as in weighted A\*, inflation of the heuristic can be used to trade-off bounded sub-optimality with speed.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In this section we present the problem of interest as a mathematical program.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Directed graph with vertices 𝒱 and edges ℰ

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Convex set associated with vertex v

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Convex constraint set for edge e

<!-- chunk {"id": "body-0021", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Discrete path in the graph, defined as a sequence of vertices

<!-- chunk {"id": "body-0022", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The i-th vertex in the path v

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The point on trajectory x associated with vertex v

<!-- chunk {"id": "body-0024", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Cost of the edge between vertices u and v, evaluated on trajectory x

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Optimal cost of a solution via vertex v

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

$\overset{\sim}{f}(\mathbf{v})$
Total cost estimate via path v

<!-- chunk {"id": "body-0027", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

$\overset{\sim}{f}(\mathbf{v},x)$
Total cost estimate via path v and point x ∈ 𝒳vend

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

$\overset{\sim}{g}(\mathbf{v},x)$
Optimal cost-to-come from s to point x ∈ 𝒳vend via path v

<!-- chunk {"id": "body-0029", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Heuristic estimate of cost-to-go from point x to t

<!-- chunk {"id": "body-0030", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Optimal trajectory via path v subject to the heuristic $\overset{\sim}{h}$

<!-- chunk {"id": "body-0031", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

A GCS is a directed graph $G:={(\mathcal{V},\mathcal{E})}$ defined by a (potentially infinite) set of vertices $\mathcal{V}$ and edges $\mathcal{E} \subset \mathcal{V}^{2}$, where ${(u,v)} \in \mathcal{E}$ if the graph allows transitions from vertex $u$ to vertex $v$, i.e., $v$ is a *successor* of $u$. Each vertex $v \in \mathcal{V}$ is paired with a compact convex set $\mathcal{X}_{v}$. These sets may live in different spaces. We assume each vertex has a finite number of successors. The graph is implicitly defined via source vertex $s \in \mathcal{V}$ and operator Successors that, when applied to a vertex $u$, returns all successors $v_{i}$ of $u$. We define a path $\mathbf{v}$ in graph $G$ as a sequence of vertices, where the bold font indicates a sequence.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

A subscripted index operates on a sequence to select the element at that index: $\mathbf{v}_{i}$ gives the $i$-th vertex in the sequence and each $\mathbf{v}_{i + 1}$ is a successor of $\mathbf{v}_{i}$. Likewise, we define a trajectory $\mathbf{x}$ on path $\mathbf{v}$ as a sequence of points in the sets associated with $\mathbf{v}$, $\mathbf{x}_{i} \in \mathcal{X}_{\mathbf{v}_{i}}$. We also overload the indexing of $\mathbf{x}$ to go by vertex, such that $\mathbf{x}_{\mathbf{v}_{i}}:=\mathbf{x}_{i}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We denote the last vertex in the path $\mathbf{v}$ as $\mathbf{v}_{\text{end}}$, and the edges traversed by $\mathbf{v}$ as $\mathcal{E}_{\mathbf{v}}$. The cost of edge $e:={(u,v)}$ is determined by a proper, closed, convex, positive, bounded-away-from-zero function of its endpoints $c{(\mathbf{x}_{u},\mathbf{x}_{v})}$. The bounded-away-from-zero stipulation ensures finite optimal paths when cycles are permitted. Each edge can additionally have constraints ${(\mathbf{x}_{u},\mathbf{x}_{v})} \in \mathcal{X}_{e}$, where $\mathcal{X}_{e}$ is a closed convex set.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

For source vertex $s \in \mathcal{V}$ and target vertex $t \in \mathcal{V}$, the SPP in GCS is

<!-- chunk {"id": "body-0035", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

The objective (1a) is to minimize the total cost of traversing the path $\mathbf{v}$ in the graph. Constraint (1b) enforces that path $\mathbf{v}$ starts at source vertex $s$, and ends at target vertex $t$. Constraint (1c) enforces that each edge in the path $\mathbf{v}$ exists. Constraint (1d) enforces that each point on the trajectory $\mathbf{x}$ lies within the convex set corresponding to its vertex. Finally, constraint (1e) enforces that the continuous values of trajectory $\mathbf{x}$ satisfy all edge constraints along path $\mathbf{v}$.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

If the discrete path $\mathbf{v}$ is fixed, prog. becomes convex and easy to solve; we call this program ConvexRestriction. Given $\mathbf{v}$, solving ConvexRestriction determines its corresponding optimal cost and optimal trajectory $\mathbf{x}$.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Graph Search Formulation", "weight": 1.0} -->

A\* (alg. 1) searches over paths from the source, pruning some and expanding others based on estimated costs of extending to reach the target, until a path reaches the target and is returned. In particular, paths await expansion in a priority queue $Q$ ordered by total cost estimate $\overset{\sim}{f}$. Often, instead of specifying $\overset{\sim}{f}$ directly, a user equivalently provides $\overset{\sim}{h}$, a heuristic that estimates costs-to-go from vertices to the target, and $\overset{\sim}{f}$ is computed as the sum of heuristic $\overset{\sim}{h}$ and cost-to-come $\overset{\sim}{g}$. A path is pruned via a domination check if its cost-to-come $\overset{\sim}{g}$ is greater than that of the current cheapest path reaching the same vertex.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Graph Search Formulation", "weight": 1.0} -->

This current cheapest path for each vertex is stored in a map $S$, that maps each vertex to the current lowest-cost path. Equivalently, $\overset{\sim}{f}$ can be compared since paths reaching the same vertex share an $\overset{\sim}{h}$ value. We use the term "domination check" generically to refer to a function that determines whether a candidate path should be pruned or added to $Q$. We call a path expanded if it has been popped from $Q$. We call a vertex expanded if any path terminating at it has been expanded.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Graph Search Formulation", "weight": 1.0} -->

GCS\* (alg. 2) proceeds similarly. The key difference is the use of a different domination check $\text{NotDominated} \in$ $\{\text{ReachesCheaper},\text{ReachesNew}\}$ (defined in sec. 4.2.2). To facilitate these domination checks, GCS\* maintains a map $S$ which maps each vertex to a set of un-pruned paths reaching the vertex. This is in contrast to A\*, which stores a single path reaching each vertex. For any vertex $v \in \mathcal{V}$, we define $f^{\ast}{(v)}$ as the optimal cost of prog. with the additional constraint that vertex $v$ is on the path $\mathbf{v}$ (not necessarily as the terminal vertex $\mathbf{v}_{\text{end}}$), i.e., $v \in \mathbf{v}$, where path $\mathbf{v}$ is a decision variable in prog..

<!-- chunk {"id": "body-0040", "role": "body", "section": "Graph Search Formulation", "weight": 1.0} -->

Let $g^{\ast}{(x)}$ be the optimal cost-to-come from source $s$ to point $x$, and $h^{\ast}{(x)}$ be the optimal cost-to-go from point $x$ to target $t$, both infinite if infeasible.^22^2More precisely, every "function" $l{(x)}$ that takes a point $x$ as input in this paper is actually a family of functions $\{ l_{v}:{\mathcal{X}_{v}\rightarrow{{\mathbb{R}} \mid v} \in V}\}$ defined over each vertex, as these points may lie in different spaces.

<!-- chunk {"id": "body-0041", "role": "body", "section": "Graph Search Formulation", "weight": 1.0} -->

Note that $f^{\ast}{(x)}$, $g^{\ast}{(x)}$, and $h^{\ast}{(x)}$ are well defined even if point $x$ is contained in (intersecting) sets corresponding to multiple vertices.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Graph Search Formulation", "weight": 1.0} -->

In general, ${f^{\ast},g^{\ast}},$ and $h^{\ast}$ cannot be computed without solving prog.. Instead, we define computationally viable functions $\overset{\sim}{f},\overset{\sim}{g}$ and $\overset{\sim}{h}$. The A\* algorithm uses a heuristic function for estimating the cost-to-go from a vertex to the target. Extending this to GCS\*, we use a heuristic function $\overset{\sim}{h}{(x)}$ that estimates the cost-to-go from a point $x$ to the target $t$.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Graph Search Formulation", "weight": 1.0} -->

1:Input: s, t, $\overset{\sim}{f}$, $\overset{\sim}{g}$, Successors
3:Output: Path from s to t or Fail
$Q\leftarrow{\text{priority queue ordered by~}\overset{\sim}{f}(\mathbf{v})}$
8:v← Q.Pop \Ifvend = t \Returnv \EndIf\ForAllv′ ∈ Successorsvend
9:v′ = [v,v′] \Ifv′ ∉ S or ${\overset{\sim}{g}\left( \mathbf{v}^{\prime} \right)} &lt; {\overset{\sim}{g}\left( {S\left\lbrack v^{\prime} \right\rbrack} \right)}$
11:Q.Addv′ \EndIf\EndFor\EndWhile

<!-- chunk {"id": "body-0044", "role": "body", "section": "Graph Search Formulation", "weight": 1.0} -->

1:Input: s, t, $\overset{\sim}{f}$, NotDominated, Successors
2:Output: Path from s to t or Fail
4: S ← {s: {v}} ⊳ Map of sets of paths
$Q\leftarrow{\text{priority queue ordered by~}\overset{\sim}{f}(\mathbf{v})}$
7:v← Q.Pop \Ifvend = t \Returnv \EndIf\ForAllv′ ∈ Successorsvend
10:Q.Addv′ \EndIf\EndFor\EndWhile

<!-- chunk {"id": "body-0045", "role": "body", "section": "Graph Search Formulation", "weight": 1.0} -->

To evaluate the total cost estimate for a path additionally restricted to pass through a specific point $x \in \mathcal{X}_{\mathbf{v}_{\text{end}}}$, we overload ${\overset{\sim}{f}{(\mathbf{v},x)}}:={{\overset{\sim}{g}{(\mathbf{v},x)}} + {\overset{\sim}{h}{(x)}}}$. ConvexRestriction can be used to evaluate $\overset{\sim}{g}{(\mathbf{v},x)}$ and $\overset{\sim}{f}{(\mathbf{v},x)}$ (used to evaluate sample points in sec. 4.2.1).

<!-- chunk {"id": "body-0046", "role": "body", "section": "Graph Search Formulation", "weight": 1.0} -->

Additionally, if $\overset{\sim}{h}$ is convex^33^3More precisely, ${\overset{\sim}{h}}_{v}$ is convex for all $v \in \mathcal{V}$., ConvexRestriction can be used to evaluate $\mathbf{x}^{\ast}{(\mathbf{v})}$ (used to return the final optimal trajectory) and $\overset{\sim}{f}{(\mathbf{v})}$ (used to prioritize the queue $Q$ in alg. 2).

<!-- chunk {"id": "body-0047", "role": "body", "section": "Graph Search Formulation", "weight": 1.0} -->

We assume heuristic $\overset{\sim}{h}{(x)}$ is nonnegative, i.e., ${\overset{\sim}{h}{(x)}} \geq {0,{\forall x}}$. Furthermore, heuristic $\overset{\sim}{h}$ must be pointwise admissible (def. 1) in order for optimality guarantees (sec. 4.3) to hold.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Domination Checks", "weight": 1.0} -->

In of alg. 2, GCS\* uses one of two domination checks, ReachesCheaper or ReachesNew. In practice, exact checks are not tractable, so we compute approximate checks. An approximate NotDominated check is said to be *conservative* if it never returns False incorrectly, i.e., it never says a candidate path is dominated when it is not. Under a conservative domination check, GCS\* may track more candidate paths than necessary, but never overlooks an important path (which paths are "important" depends on the domination check being used and will be precisely stated in this section). Using exact or conservative ReachesCheaper checks, GCS\* is cost optimal. Satisficing solutions (solutions which are feasible but likely suboptimal) can be found more quickly using ReachesNew. Using exact or conservative ReachesNew checks, GCS\* is complete.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Domination Checks", "weight": 1.0} -->

If a candidate path $\mathbf{v}$ reaches some point $x \in \mathcal{X}_{\mathbf{v}_{\text{end}}}$ cheaper than any way found yet, as in sec. 4.2

<!-- chunk {"id": "body-0050", "role": "body", "section": "Domination Checks", "weight": 1.0} -->

If ${{ReachesCheaper\mathbf{v}},{S{\lbrack\mathbf{v}_{\text{end}}\rbrack}}} = \text{False}$, path $\mathbf{v}$ is said to be *dominated*, or, more specifically, *cost-dominated*. Intuitively, GCS\* returns an optimal path when it has pruned only cost-dominated paths (discussed in sec. 4.3, proven in appendix 0.A) because such paths cannot be subpaths of optimal paths.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Domination Checks", "weight": 1.0} -->

If a candidate path $\mathbf{v}$ reaches some point $x \in \mathcal{X}_{\mathbf{v}_{\text{end}}}$ that has not yet been reached, as in sec. 4.2

<!-- chunk {"id": "body-0052", "role": "body", "section": "Domination Checks", "weight": 1.0} -->

If ${{ReachesNew\mathbf{v}},{S{\lbrack\mathbf{v}_{\text{end}}\rbrack}}} = \text{False}$, $\mathbf{v}$ is said to be *dominated*, or, more specifically, *reachability-dominated*. Where ReachesCheaper compares costs-to-come at all points in the terminal set, ReachesNew compares feasibility of reaching these points. Note that ReachesNew implies ReachesCheaper since the cost of any feasible path is finite, but ReachesCheaper does not imply ReachesNew.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Sampling-based Approximation", "weight": 1.0} -->

The simplest and fastest approach to approximating ReachesCheaper and ReachesNew queries is to check whether sample points $x \in \mathcal{X}_{\mathbf{v}_{\text{end}}}$ meet the conditions on $x$ in eq. 1b and eq. 1c respectively, returning True if any sampled point does. These approximations are not conservative: the candidate path not being dominated at some sampled point $x$ is sufficient to conclude that the candidate path is not dominated, but not necessary. For example, in sec. 4.2 (d), sparse sampling may miss the green interval where the cost-to-come of the candidate path $\overset{\sim}{g}{(\mathbf{v},x)}$ is lower than the others, leading ReachesCheaper to return False, signaling that $\mathbf{v}$ is dominated, when in fact it is not. However, completeness and optimality are approached in the limit of infinite samples; in this sense we say GCS\* is probabilistically complete and asymptotically optimal. We discuss this further in sec.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Polyhedral-containment-based Approximation", "weight": 1.0} -->

We prove in appendix 0.A that conservative (necessary but not sufficient) approximations of ReachesNew and ReachesCheaper enable completeness and optimality guarantees. We formulate such checks via polyhedral containment queries. One source of conservatism is that, unfortunately, these queries can check only single domination: They compare candidate path $\mathbf{v}$ to individual alternate paths in $S{\lbrack\mathbf{v}_{\text{end}}\rbrack}$. These checks can detect reachability domination like in sec. 4.2 (a) and (c) and cost domination like in sec. 4.2 (a), in which $\mathbf{v}$ is dominated by a single other path $\mathbf{v}^{(i)}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Polyhedral-containment-based Approximation", "weight": 1.0} -->

These checks cannot detect reachability domination like in (d) or (e), or cost domination like in (e), in which the candidate path $\mathbf{v}$ is dominated by several alternate paths $\mathbf{v}^{(i)}$ collectively but not by any individual alternate path $\mathbf{v}^{(i)}$. Further conservatism occurs due to inability to compute exact containment queries tractably.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Polyhedral-containment-based Approximation", "weight": 1.0} -->

We first re-define ReachesCheaper and ReachesNew in terms of set containment, before relaxing these conditions to tractable containment queries.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Polyhedral-containment-based Approximation", "weight": 1.0} -->

The union over convex sets is not generally itself convex, and we know of no efficient way to compute these queries. Instead, we check single domination, comparing to individual other paths. In particular, we use

<!-- chunk {"id": "body-0058", "role": "body", "section": "Polyhedral-containment-based Approximation", "weight": 1.0} -->

as necessary conditions for ReachesCheaper (1ea) and ReachesNew (1eb) respectively: if the candidate path is not dominated by the collective of other paths, then it certainly is not dominated by any individual other path.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Polyhedral-containment-based Approximation", "weight": 1.0} -->

These single domination checks are still non-trivial because they involve comparing projections of convex sets, which are expensive to compute explicitly. In our examples, vertex sets are polytopic and costs are linear, which allows us to use Sadraddini and Tedrake's sufficient condition for containment of affine transformations of polyhedra, evaluated by solving a convex program. Using this condition to check (1fb) and (1fa), ${NotDominated\mathbf{v}},{S{\lbrack\mathbf{v}_{\text{end}}\rbrack}}$ is conservative: If candidate path $\mathbf{v}$ is not dominated, it certainly returns True, but if candidate path $\mathbf{v}$ is dominated, it may return True or False. In the case of more general convex vertex sets and costs, Jones and Morari's work on computing inner and outer polytopic approximations of convex sets can be used before evaluating these containment queries.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Properties of the Algorithm", "weight": 1.0} -->

We state properties of the algorithm in this section, and include proofs in appendix 0.A.

<!-- chunk {"id": "body-0061", "role": "body", "section": "Efficiency", "weight": 1.0} -->

In contrast to A\*, GCS\* is not optimally efficient. That is, given the heuristic information $\overset{\sim}{h}$, it can be shown that GCS\* expands subpaths that may not be expanded by some other hypothetical algorithm guaranteed to return the optimal solution. Conceptually, GCS\* loses this property that applies to A\* because when GCS\* expands a subpath $\mathbf{v}$, by considering paths through the children of $\mathbf{v}_{\text{end}}$, GCS\* now has access to potentially improved lower-bound on the true cost-to-go, $\overset{\sim}{h}{(x)}$, for $x$ in the reachable set of $\mathbf{v}$, $\mathcal{S}_{\mathbf{v}}$ (1db), but we do not choose to use this information to update $\overset{\sim}{h}{(x)}$.

<!-- chunk {"id": "body-0062", "role": "body", "section": "Efficiency", "weight": 1.0} -->

A\* with a consistent heuristic does not suffer from this inefficiency because it never expands a node twice, whereas GCS\* may expand many subpaths whose terminal sets contain points in $\mathcal{S}_{\mathbf{v}}$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "Properties when using sampling-based domination checks", "weight": 1.0} -->

While we have proven that GCS\* is cost-optimal and complete under conservative IsDominated checks, a sampling-based implementation is sometimes preferred, as discussed in sec. 4.2.2. In the limit of infinite samples, the sampling-based implementations of NotDominated are exact. Thus it follows from theorems 0.A.1 and 0.A.2 that sampling-based GCS\* is probabilistically complete and asymptotically cost-optimal. One might raise concern that the backward-reachable set from the target in some set $\mathcal{X}_{v}$ may never be sampled, leading some important feasible path to be pruned. However, because all $\mathcal{P}_{\mathbf{v}}$ (1da) are compact, the sets being checked for containment, $\mathcal{S}_{\mathbf{v}}$ (1db), are closed.

<!-- chunk {"id": "body-0064", "role": "body", "section": "Properties when using sampling-based domination checks", "weight": 1.0} -->

Therefore, $\mathcal{S}_{\mathbf{v}} \smallsetminus {\bigcup_{\mathbf{v}^{\prime} \in {S{\lbrack\mathbf{v}_{\text{end}}\rbrack}}}\mathcal{S}_{\mathbf{v}^{\prime}}}$ with respect to the topology of $\mathcal{S}_{\mathbf{v}}$ (the space being sampled) is open and thus either empty or positive-measure. If it has positive measure, it will eventually be sampled.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Application to Planar Pushing", "weight": 1.0} -->

Tasks involving making and breaking contact while constraining non-penetration notoriously lead to an explosion of discrete modes, especially as the number of bodies scales. Indeed, the naive formulation in sec. 5.1 sees this combinatorial growth. With more careful construction of contact modes, or by introducing hierarchy, one could greatly reduce search space for these problems. However, additional structure can make such methods less general. Our goal with these experiments is not to demonstrate state of the art performance on contact-rich manipulation tasks specifically, but instead to show that our method is able to approach such large problems.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Formulation", "weight": 1.0} -->

We implement a simplified planar pushing model with polyhedral robots and objects that can translate but not rotate, and static obstacles. Robot-object and object-object contact are frictionless, and motion quasi-static, where bodies' velocities are proportional to the net forces applied to them. We enforce non-penetration between all pairs of bodies, defining collision-free sets over robot and object positions. We also define sets over positions and contact forces defining the permissible physical contact behavior for each pair of bodies. Together, these two kinds of discrete modes define the sets of the graph $G$. Each point $\mathbf{x}_{v} \in \mathcal{X}_{v}$ in prog. is comprised of $n_{k}$ knot points, defining the planar positions for each robot and object, actuation forces for each robot, and a force magnitude for each pair of bodies in contact. The constraints defining these sets, which we explain throughout this section, are straightforward to compose. As such, the Successors operator can construct them on demand.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Formulation", "weight": 1.0} -->

In particular, the successors of some vertex are defined by changing the contact state or the non-penetration separating hyperplane (defined below) for a single pair of bodies.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Formulation", "weight": 1.0} -->

All constraints are linear, leading to polyhedral sets. However, extensions of this model to include rotations could involve semidefinite relaxations, leading to spectrahedral sets, in a formulation similar to that of Graesdal et al.. This work could also be extended to borrow other components of the GCS formulation of planar pushing from Graesdal et al., like frictional contact. We omit these features for simplicity. However, the assumption that bodies are polyhedral is harder to relax, as it allows for an exact polyhedral decomposition of collision-free space. Alternative settings that require only an approximate convex decomposition of the free configuration space can handle rotations and non-polyhedral bodies. However, these formulations are not conducive to making contact due to incomplete coverage. As these decompositions are generally composed offline and cannot produce new sets as quickly as our Successors operator can, this formulation would either require building the entire graph before running GCS\* or accepting slower evaluation of Successors.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Non-penetration", "weight": 1.0} -->

We constrain that each pair of bodies do not penetrate one another by imposing that one face of one of the two polyhedra is a separating hyperplane: all vertices of one body lie on one side, and all vertices of the other body lie on the other side.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Contact", "weight": 1.0} -->

Every pair of bodies may have any of the following kinds of contact: no contact, any face of one body in contact with any face of another, or any face of one body in contact with any vertex of another. Gathering these options over all pairs of bodies produces a contact set. Each pair of bodies in contact in each contact set is accompanied by a force magnitude variable, leading to variation in dimension between sets. This force acts normal to the face in contact. Position constraints are added to ensure the associated contact is physically feasible. Relative sliding of features in contact is allowed within a single contact set, as long as they remain in contact.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Quasi-static dynamics", "weight": 1.0} -->

For each object and robot, we enforce that between consecutive knot points, translation is proportional to the sum of forces on the body, including a robot's actuation force. Edge constraints enforce that robot and object positions remain the same across edges -- for an edge $(u,v)$ in eq. 1, the positions from the last knot point in $\mathbf{x}_{u}$ must equal the positions from the first knot point in $\mathbf{x}_{v}$. As a result of this constraint, a path containing the edge $(u,v)$ is only feasible if there is a shared position that is feasible in both convex sets associated with these vertices, $\mathcal{X}_{u}$ and $\mathcal{X}_{v}$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

Our sampling-based implementations can handle $L_{2}$ norm or $L_{2}$ norm squared edge costs easily. However, as discussed in sec. 4.2.2, our containment-based implementations need modification to accommodate non-linear costs.

<!-- chunk {"id": "body-0073", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

For sampling-based domination checks, we use only a single sample per check. As we will discuss, empirically, this is sufficient. In practice, due to edge constraints, the reachable set for a path $\mathbf{v}$, $\mathcal{S}_{\mathbf{v}} \subseteq \mathcal{X}_{\mathbf{v}_{\text{end}}}$, is often low-volume within the terminal set $\mathcal{X}_{\mathbf{v}_{\text{end}}}$. As such, we sample uniformly in $\mathcal{X}_{\mathbf{v}_{\text{end}}}$ and then project onto $\mathcal{S}_{\mathbf{v}}$.

<!-- chunk {"id": "body-0074", "role": "body", "section": "Implementation Details", "weight": 1.0} -->

For containment-based methods, we first perform a cheap single-sample NotDominated check, and only check containment if it returns False. Additionally, taking advantage of the unique structure of our planar pushing formulation, we only check the domination conditions on the last position knot point instead of all variables in the set. To reduce problem size for domination checks, we "solve away" equality constraints by parameterizing in their nullspace.

<!-- chunk {"id": "body-0075", "role": "body", "section": "Results", "weight": 1.0} -->

Table 2 presents results for three planar pushing tasks: AROUND, SQUEEZE, and STACK shown in figs. 5 and. AROUND is the simplest task: its graph has 194 vertices and 8,328 edges. SQUEEZE has a larger graph with 628 vertices and 56,806 edges. The dimensions of sets in AROUND and SQUEEZE range from 4 to 12. STACK (fig. 1) has 5 bodies, leading to a combinatorial explosion of approximately $1.3 \times 10^{9}$ sets and up to $8.5 \times 10^{17}$ edges. The dimensions of its sets range from 8 to 24. Due to the sizes of the graphs, the direct convex optimization approach cannot be used, thus we compare GCS\* against IxG and IxG\*, the state-of-the-art for incrementally solving SPP on GCS.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Results", "weight": 1.0} -->

For sampling-based domination checks, as we increase the number of samples per check, we approach completeness and optimality. Due to the curse of dimensionality, such coverage demands exponentially more samples as set dimensions increase. However, in our tasks, we found that very sparse sampling -- in particular, a single sample per domination check -- still resulted in good solution quality. This is an interesting result that enables an efficient and de facto nearly optimal implementation. We understand this to be a property particular to our problem structure, in which the condition that two paths reach the same final knot point within the same vertex is quite restrictive. For example, the sampling-based ReachesNew approximation asks whether any path in $S$ can achieve a trajectory ending at a particular sampled object position and robot position in some contact state that can be achieved by a candidate path, calling the candidate path dominated if so. In this event, it is likely that that path in $S$ can reach much of what the candidate path can, and the candidate path can be pruned with little consequence.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Results", "weight": 1.0} -->

Containment-based domination checks scale poorly with path length, or, more precisely, the dimension of the full trajectory through it. This is reflected in the solve times in the rows marked "Cont." in table 2.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Results", "weight": 1.0} -->

The number of paths expanded is impacted greatly by the strength of the heuristic in the context of the particular task. In general, the "shortcut" edge heuristic is strong for AROUND and STACK and weaker for SQUEEZE which requires squeezing through a narrow gap then maneuvering around the object to push it from a different direction multiple times. As expected, use of an inadmissible heuristic leads to cost increase. Typically, containment-based checks lead to more paths being expanded as compared to sampling-based checks (as seen in table 2) because of false negatives from sampling, as well as conservatism of the single domination criteria. However, containment-based checks could also lead to fewer paths being expanded because important paths are not wrongly pruned, as they might be when using sampling-based checks (not observed in table 2).

<!-- chunk {"id": "body-0079", "role": "body", "section": "Results", "weight": 1.0} -->

In comparison to our methods, the baselines require significant time to compute heuristic values for the entire graph before starting their query phase. While this approach can yield a stronger heuristic (as in the bottommost row, where IxG expands fewer paths than GCS\* for AROUND), for these tasks the solve times can be dominated by this pre-processing phase. When the graph is very large, this pre-processing can become intractable (as in STACK). Because IxG\* prunes paths based on a global upper bound found by IxG, in cases where IxG is unable to return a solution (as in SQUEEZE), or simply when an admissible heuristic is used (as in row 3), no paths will be pruned, resulting in intractably large search spaces. As GCS\* is complete, and our domination checks do not rely on a global upper bound, GCS\* does not experience these particular limitations.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We propose GCS\*, a forward heuristic search algorithm for solving large discrete-continuous planning problems formulated as GCS. We define two domination checks ReachesNew and ReachesCheaper, as well as containment and sampling-based implementations of those checks that allow GCS\* to be complete and optimal, or have probabilistic/asymptotic versions of those properties, respectively. GCS\* provides a principled way of addressing the challenges of applying graph search to the discrete-continuous setting. We demonstrate settings in which GCS\* performs favourably compared to the state-of-the-art. For application to real-world planar pushing tasks, further work would be required to handle rotations. Incorporating these insights into algorithms that leverage hierarchy, factorization or learned heuristics could solve more complex problems faster.
