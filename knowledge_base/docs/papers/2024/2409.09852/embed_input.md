<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

A Complete Algorithm for a Moving Target Traveling Salesman Problem with Obstacles

Topics include Traveling salesman problem, Moving targets, Obstacles, Complete algorithms, Motion planning, Combinatorial optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Presents a complete algorithm for a moving-target traveling-salesman variant with obstacle avoidance and target time windows. The paper connects geometric motion planning with combinatorial routing by proving finite-time termination and handling the coupling between visit order, timing, and collision-free travel.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The moving target traveling salesman problem with obstacles (MT-TSP-O) is a generalization of the traveling salesman problem (TSP) where, as its name suggests, the targets are moving. A solution to the MT-TSP-O is a trajectory that visits each moving target during a certain time window(s), and this trajectory avoids stationary obstacles. We assume each target moves at a constant velocity during each of its time windows. The agent has a speed limit, and this speed limit is no smaller than any target's speed. This paper presents the first complete algorithm for finding feasible solutions to the MT-TSP-O. Our algorithm builds a tree where the nodes are agent trajectories intercepting a unique sequence of targets within a unique sequence of time windows. We generate each of a parent node's children by extending the parent's trajectory to intercept one additional target, each child corresponding to a different choice of target and time window. This extension consists of planning a trajectory from the parent trajectory's final point in space-time to a moving target.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

To solve this point-to-moving-target subproblem, we define a novel generalization of a visibility graph called a moving target visibility graph (MTVG). Our overall algorithm is called MTVG-TSP. To validate MTVG-TSP, we test it on 570 instances with up to 30 targets. We implement a baseline method that samples trajectories of targets into points, based on prior work on special cases of the MT-TSP-O. MTVG-TSP finds feasible solutions in all cases where the baseline does, and when the sum of the targets' time window lengths enters a critical range, MTVG-TSP finds a feasible solution with up to 38 times less computation time.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Given a set of targets and the travel costs between every pair of targets, the traveling salesman problem (TSP) seeks an order of targets for an agent to visit that minimizes the agent's total travel cost. In the moving target traveling salesman problem (MT-TSP), the targets are moving through free space, and we seek not only an order of targets, but a trajectory for the agent intercepting each target. The agent's trajectory is subject to a speed limit and must intercept each target within a set of target-specific time intervals, called time windows. We consider the case where travel cost between targets is equal to the travel time: this cost is not fixed *a priori*, as in the TSP, and instead depends on the time at which the agent intercepts each target. Prior work on the MT-TSP assumes that the agent's speed limit is no smaller than the speed of any target, and we make the same assumption in our work. When there are moving targets as well as obstacles for the agent to avoid, we refer to the problem as the moving target traveling salesman problem with obstacles (MT-TSP-O), shown in Fig..

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Two properties we desire for an MT-TSP-O algorithm are completeness^11^1Completeness refers to an algorithm's guarantee on finding a feasible solution when a problem instance is feasible or reporting infeasible in finite time otherwise. and optimality. No algorithm for the MT-TSP-O in the literature has either of these properties. Guaranteeing completeness is complicated by the fact that even the problem of finding a feasible solution is NP-complete, since the MT-TSP-O generalizes the TSP with time windows (TSP-TW). In this paper, we present the first complete algorithm for the MT-TSP-O.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Simpler cases of the MT-TSP-O have been addressed in the literature, with completeness guarantees in some cases. For example, in the absence of obstacles, provides a complete and optimal solver for the MT-TSP assuming targets move at constant velocities. provides a complete and optimal method when targets have piecewise-constant velocities. Heuristics are presented in for variants of the MT-TSP, only guaranteeing completeness in the absence of time windows. In the presence of obstacles, there is one related work that considers the case where the agent is restricted to travel along a straight-line path when moving from one target to the next, providing an incomplete algorithm. A generic approach to solving these special cases of the MT-TSP-O is to sample the trajectories of targets into points, find agent trajectories between every pair of points, then select a sequence of points to visit by solving a generalized traveling salesman problem (GTSP). This approach is not complete, since it may only be possible for the agent to intercept some target at a time that is in between two of the sampled points in time representing the target's trajectory.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

We develop a new algorithm for the MT-TSP-O that guarantees completeness. Our algorithm, called MTVG-TSP, leverages a novel generalization of a visibility graph, which we call a moving target visibility graph (MTVG), which enables us to plan a trajectory from a starting point in space-time to a moving target. Given a sequence of time windows of targets, we can find a minimum-time agent trajectory intercepting each target within its specified time window via a sequence of A\* searches, each on a MTVG. In particular, we can do so without sampling any target's trajectory, avoiding the limitations of prior work. By performing a higher level search for a sequence of time windows and computing an agent trajectory for each generated sequence, MTVG-TSP finds an MT-TSP-O solution if one exists. We extensively test our algorithm on problem instances with up to 30 targets, varying the length and number of time windows, and we compare our algorithm's computation time to a method based on prior work that samples trajectories of targets into points.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

We demonstrate that when the sum of the time window lengths for each target enters a critical range, the sampled-points method requires an excessive number of sample points to find a feasible solution, while our method finds solutions relatively quickly.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

Each target has a set of $N_{i}$ time windows $\{ w_{i,1},w_{i,2},\ldots,w_{i,N_{i}}\}$, where $w_{i,j} = {\lbrack t_{i,j}^{0},t_{i,j}^{f}\rbrack}$ is the $j^{th}$ time window of target $i$. Target $i$ moves at a constant velocity within each of its time windows, but its velocity may be different for each time window. Given a final time $T^{f}$, denote the trajectory for the agent as $\tau_{A}:{{\lbrack 0,T^{f}\rbrack}\rightarrow{\mathbb{R}}^{2}}$. $\tau_{A}$ must start and end at a given point called the depot denoted as $d$ with position $p_{d} \in {\mathbb{R}}^{2}$.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

The agent can move in any direction with a speed at most $v_{max}$.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

Let $\{ O_{1},O_{2},{\ldots O_{N_{O}}}\}$ denote the set of obstacles where $N_{O}$ denotes the number of obstacles. We define $\Psi{(t^{0},t^{f})}$ as the set of all the feasible agent trajectories defined on the time interval $\lbrack t^{0},t^{f}\rbrack$ such that for any time $t \in {\lbrack t^{0},t^{f}\rbrack}$, the agent satisfies the speed constraint and its position never enters the interior of any obstacle. We assume that within target $i$'s time windows, target $i$ does not move with speed greater than $v_{max}$ and does not enter the interior of any obstacle.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Setup", "weight": 1.0} -->

We say that a trajectory $\tau_{A}$ for the agent intercepts target $i \in {\lbrack N_{\tau}\rbrack}$ if there exists a time $t$ such that for some $j \in {\lbrack N_{i}\rbrack}$, $t \in w_{i,j}$ and ${\tau_{A}{(t)}} = {\tau_{i}{(t)}}$. We define the MT-TSP-O as the problem of finding a final time $T^{f}$ and an agent trajectory $\tau_{A} \in {\Psi{(0,T^{f})}}$ such that $\tau_{A}$ starts and ends at the depot, intercepts each target $i \in {\lbrack N_{\tau}\rbrack}$, and $T^{f}$ is minimized.

<!-- chunk {"id": "body-0014", "role": "body", "section": "MTVG-TSP Algorithm", "weight": 1.0} -->

The MTVG-TSP algorithm interleaves a higher-level search on a time window graph and a lower-level search on a moving target visibility graph (MTVG). The nodes in the time window graph, called window-nodes, each represent either the depot or a pairing of a target with one of its time windows. A feasible solution to the MT-TSP-O corresponds to a cycle in the time window graph containing the depot and exactly one window-node per target. Our algorithm finds such a cycle by building a trajectory tree, where each tree-node contains a sequence of window-nodes and an associated agent trajectory. A tree-node's children are each generated in two steps. First, we append a window-node to the end of the tree-node's window-node sequence. Then we extend the tree-node's agent trajectory to intercept the appended window-node's target. We perform this trajectory extension via the MTVG. In particular, we construct the MTVG by augmenting a standard visibility graph with the window-node whose target we aim to intercept.

<!-- chunk {"id": "body-0015", "role": "body", "section": "MTVG-TSP Algorithm", "weight": 1.0} -->

Extending a tree-node's trajectory consists of planning a path in the MTVG from the final point in the tree-node's trajectory to the added window-node. When we have a tree-node with a trajectory that intercepts all targets and returns to the depot, we have a solution to the MT-TSP-O.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Initial Visibility Computations", "weight": 1.0} -->

Next, we describe two initial data structures needed to construct the moving target visibility graph. The first is a standard visibility graph $G_{vis} = {(V_{vis},E_{vis})}$. Let $V_{O} \subseteq {\mathbb{R}}^{2}$ be the set of convex vertices of all the obstacles^33^3A convex obstacle vertex is is a vertex where the internal angle between the two incident edges is less than $\pi$ radians. Using only convex vertices in a visibility graph reduces graph size without discarding shortest paths through the graph.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Initial Visibility Computations", "weight": 1.0} -->

We draw an edge from $q \in V_{vis}$ to $q^{\prime} \in V_{vis}$ if $q^{\prime}$ is contained in the visibility polygon of $q$, denoted as $\text{vpoly}{(q)}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Initial Visibility Computations", "weight": 1.0} -->

The second data structure encodes visibility relationships between points in space and window-nodes. In particular, for each $q \in V_{vis}$, $s \in V_{tw}$, we compute a visible interval set $\text{vis}{(q,s)}$, containing every interval $I \subseteq {\lbrack{t^{0}{(s)}},{t^{f}{(s)}}\rbrack}$ such that for all $t \in I$, we have ${\tau_{\text{targ}{(s)}}{(t)}} \in {\text{vpoly}{(q)}}$. We illustrate $\text{vis}{(q,s)}$ in Fig. (a).

<!-- chunk {"id": "body-0019", "role": "body", "section": "Moving Target Visibility Graph", "weight": 1.0} -->

A recurring subproblem in our algorithm is to find a trajectory from a point $(p,T)$ in space-time that intercepts a particular window-node $s$ in minimum time. For each of these subproblems, we define a graph ${\overset{\sim}{G}}_{vis} = {({\overset{\sim}{V}}_{vis},{\overset{\sim}{E}}_{vis})}$ called a moving target visibility graph (MTVG). The set of nodes is ${\overset{\sim}{V}}_{vis} = {V_{vis} \cup {\{ p,s\}}}$, where nodes in $V_{vis} \cup {\{ p\}}$ are called position-nodes, and $s$ is the window-node we aim to intercept. The set of edges is ${\overset{\sim}{E}}_{vis} = {E_{vis} \cup E_{p} \cup E_{s}}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Moving Target Visibility Graph", "weight": 1.0} -->

We construct $E_{p}$ by drawing edges from $p$ to all $q \in V_{vis}$ such that $q \in {\text{vpoly}{(p)}}$; if we already have $p \in V_{vis}$, we can skip this step, since all possible edges from $p$ to $q \in V_{vis}$ already exist in $E_{vis}$. Constructing $E_{s}$ consists of two steps. First, we compute $\text{vis}{(p,s)}$; if $p \in V_{vis}$, we can skip this step, because we computed $\text{vis}{(p,s)}$ in Section 3.2. Second, we draw an edge to $s$ from any position-node $q$, including $p$, such that ${\text{vis}{(q,s)}} \neq \varnothing$, as shown in Fig. (b).

<!-- chunk {"id": "body-0021", "role": "body", "section": "Moving Target Visibility Graph", "weight": 1.0} -->

The cost of edge ${(u,v)} \in {\overset{\sim}{E}}_{vis}$ depends on $u$, $v$, and a time variable $t$ representing the time at which the agent departs from node $u$. We denote the cost of $(u,v)$ at time $t$ as ${\overset{\sim}{c}}_{vis}{(u,v,t)}$. For edges between position-nodes $u$ and $v$, the time variable is not used: the edge cost is simply equal to the agent's minimum travel time from $u$ to $v$: ${{\overset{\sim}{c}}_{vis}{(u,v,t)}} = {\frac{{\|{u - v}\|}_{2}}{v_{max}}{\forall t}}$.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Moving Target Visibility Graph", "weight": 1.0} -->

where $SFT$ stands for shortest feasible travel, as. \"Shortest\" refers to shortest time. The SFT from point $(q,t)$ to window-node $s$ on interval $I$ is the optimal cost of optimization Problem 3.3: {mini!} t_s ∈It_s - tSFT(q, t, s, I) = \\addConstraint∥τtarg(s)(ts) - q∥ts- t ≤v_max Problem 3.3 computes the minimum travel time of a straight-line trajectory starting from $(q,t)$ and intercepting $s$ within interval $I$, and can be solved in closed-form using methods. The SFT computation does not consider obstacle-avoidance, but in our case, it does not need to: any straight-line trajectory from $q$ to $s$ intercepting $s$ within some $I \in {\text{vis}{(q,s)}}$ is already obstacle-free.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Moving Target Visibility Graph", "weight": 1.0} -->

After constructing ${\overset{\sim}{G}}_{vis}$, we find a minimum-time trajectory from $(p,T)$ to $s$ via an A\* search from $p$ to $s$ on ${\overset{\sim}{G}}_{vis}$, shown in Alg.. Since edge costs in ${\overset{\sim}{G}}_{vis}$ encode travel time, the g-value $g{(v)}$ for a node $v$ is the shortest travel time out of all paths to $v$ that A\* has explored so far. $T + {g{(v)}}$ is then the earliest known arrival time to node $v$. In Line, we use this arrival time to compute edge costs from $v$ to its successors.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Moving Target Visibility Graph", "weight": 1.0} -->

The heuristic $h{(q)}$ for a position-node $q$ is the Euclidean distance from $q$ to the spatial line segment defined by $s$, divided by $v_{max}$, underestimating the travel time from $q$ to $s$. We set ${h{(s)}} = 0$. When A\* finds a path to $s$, the ConstructTrajectory function performs a standard backpointer traversal to obtain a path $Q = {(p,q^{1},\ldots,q^{N - 1},s)}$ through ${\overset{\sim}{G}}_{vis}$, moves the agent at max speed between each position-node in $Q$, and finally executes the straight-line trajectory associated with ${\overset{\sim}{c}}_{vis}{(q^{N - 1},s,{T + {g{(q^{N - 1})}}})}$.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Moving Target Visibility Graph", "weight": 1.0} -->

The result is a minimum-time trajectory from $(p,T)$ to $s$, if one exists. If such a trajectory does not exist, the condition ${g_{cand}{(v^{\prime})}} \leq {{t^{f}{(s)}} - T}$ on Line for adding $v^{\prime}$ to OPEN ensures the search terminates, described in Section.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Moving Target Visibility Graph", "weight": 1.0} -->

1 Function PointToMovingTargetSearch(p, T, s, Gvis, Λvis):
2 ${\overset{\sim}{G}}_{vis} = {({\overset{\sim}{V}}_{vis},{\overset{\sim}{E}}_{vis})} =$ ConstructMTVG (p, s, Gvis, Λvis);
5 Insert p into OPEN with f(p) = 0;
6 Set g(v) = ∞ for all $v \in {\overset{\sim}{V}}_{vis}$ with v ≠ p. Set g(p) = 0.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Moving Target Visibility Graph", "weight": 1.0} -->

7 while OPEN is not empty and ${f{(s)}} &gt; {{\min\limits_{v \in}f}{(v)}}$ do
8 Remove v with smallest f(v) from OPEN;
9 Insert v into CLOSED;
12 ${g_{cand}{(v^{\prime})}} = {{g{(v)}} + {{\overset{\sim}{c}}_{vis}{(v,v^{\prime},{T + {g{(v)}}})}}}$;
13 if gcand(v′) &lt; g(v′) and v′∉ CLOSED and gcand(v′) ≤ tf(s) − T then
15 Insert v′ into OPEN with f(v′) = g(v′) + h(v′);
24 return ConstructTrajectory(s), g(s) + T, FEASIBLE;
27 return NULL, ∞, INFEASIBLE;
Algorithm 1 A* search from initial point (p,T) to window-node s

<!-- chunk {"id": "body-0028", "role": "body", "section": "Time Window Graph", "weight": 1.0} -->

The MTVG defined in Section 3.3 enables finding a minimum-time trajectory intercepting a single window-node. We will need to chain these trajectory computations together to intercept a sequence of window-nodes, containing one window-node per target. To determine this sequence, we define a time window graph denoted as $G_{tw} = {(V_{tw},E_{tw})}$. The set of nodes in $G_{tw}$ is the set of all window nodes $V_{tw}$ from Section 3.1. We add an edge $(u,v)$ to $E_{tw}$ if there exists an agent trajectory that intercepts $u$ at time $t_{u}$ and $v$ at time $t_{v}$ with $t_{u} \leq t_{v}$, satisfying speed limit and obstacle avoidance constraints. In particular, we search for such a trajectory that departs at the latest feasible departure time from $u$ to $v$, denoted as $LFDT{(u,v)}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Time Window Graph", "weight": 1.0} -->

Extending the idea, $LFDT{(u,v)}$ is the optimal cost of optimization Problem 3.4: {maxi!} t_u ∈\[t\^0(u), t\^f(u)\],τ_At_uLFDT(u, v) = \\addConstraintτ_A ∈Ψ(t_u, t\^f(v)) \\addConstraintτ_A(t_u) = τ_targ(u)(t_u) \\addConstraintτ_A(t\^f(v)) = τ_targ(v)(t\^f(v)).

<!-- chunk {"id": "body-0030", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Constraint (3.4) requires the agent to meet $v$ at its end time $t^{f}{(v)}$, raising the question of whether the agent could depart later from $u$ if we relaxed (3.4) and only required the agent to meet $v$ at some time $t_{v} \in {\lbrack{t^{0}{(v)}},{t^{f}{(v)}}\rbrack}$. Since we assumed $\tau_{\text{targ}{(v)}}$ neither exceeds the agent's maximum speed nor enters the interior of an obstacle during $\text{targ}{(v)}$'s time window, this relaxation would not let the agent depart later from $u$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 1", "weight": 1.0} -->

Problem 3.4 seeks a trajectory that starts by intercepting a window-node and terminates at a prescribed point. We transform Problem 3.4 via a time reversal to instead seek a trajectory that starts at a prescribed point and terminates by intercepting a window-node. We do so because the transformed problem can be solved using Alg.. The transformation defines a fictitious node $\underset{¯}{u} = {({- {\text{targ}{(u)}}},{- {t^{f}{(u)}}},{- {t^{0}{(u)}}})}$ associated with fictitious target ${\text{targ}{(\underset{¯}{u})}} = {- {\text{targ}{(u)}}}$.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Remark 1", "weight": 1.0} -->

The trajectory of $\text{targ}{(\underset{¯}{u})}$ is ${\tau_{- {\text{targ}{(u)}}}{(t)}} = {\tau_{\text{targ}{(u)}}{({- t})}}$. Consider a reversed time variable $\underset{¯}{t} = {- t}$. An agent trajectory that departs as late as possible from $u$, measured in conventional time $t$, arrives at $\underset{¯}{u}$ as early as possible, measured in reversed time $\underset{¯}{t}$.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Remark 1", "weight": 1.0} -->

We find $LFDT{(u,v)}$ by solving the transformed Problem: {mini!} t_u ∈\[t\^f(u), t\^0(u)\],τ_At_uLFDT(u, v) = - \\addConstraintτ_A ∈Ψ(-t\^f(v), t_u) \\addConstraintτ_A(t_u) = τ_targ(u)(t_u) \\addConstraintτ_A(-t\^f(v)) = τ_targ(v)(t\^f(v)). We solve Problem using Alg., and if we find a feasible solution, we draw an edge from $u$ to $v$ in $G_{tw}$ and store $LFDT{(u,v)}$ with that edge.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Trajectory Tree", "weight": 1.0} -->

Any feasible agent trajectory $\tau_{A}$ for the MT-TSP-O must intercept each target during one of its time windows before returning to the depot. This means that $\tau_{A}$ intercepts a sequence of window-nodes $(s^{1},s^{2},\ldots,s^{N_{\tau}})$ containing exactly one window-node per target, implying the existence of the cycle $S = {(s_{d},s^{1},s^{2},\ldots,s^{N_{\tau}},s_{d})}$ in $G_{tw}$. In this paper, we use the depth-first search (DFS) in Alg. to find a feasible trajectory and its corresponding cycle (if one exists). While we apply DFS in this work to quickly find feasible solutions, other search methods can be used as well, e.g. best-first search to find the global optimum.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Trajectory Tree", "weight": 1.0} -->

Alg. maintains a stack that stores tuples $(S,\tau_{A},T)$, where $S$ is a path (sequence of window-nodes) through $G_{tw}$, and $(\tau_{A},T)$ is a partial solution to the MT-TSP-O, in that $(\tau_{A},T)$ starts at the depot, avoids obstacles, satisfies the speed limit, and intercepts each window-node in $S$ in order. As the search proceeds, we construct a tree of these tuples, which we call a trajectory tree. We refer to tuples $(S,\tau_{A},T)$ as tree-nodes.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Trajectory Tree", "weight": 1.0} -->

If $s^{\prime} = s_{d}$, then $S$ contains one window-node per target.

<!-- chunk {"id": "body-0037", "role": "body", "section": "Trajectory Tree", "weight": 1.0} -->

3Function DFS(S, Gvis, Λvis):
5 while STACK is not empty do
9 ${\overline{\tau}}_{A}^{\prime}$, T′, status = PointToMovingTargetSearch (τA(T), T, s′, Gvis, Λvis);
11 if Lookahead (S′, T′) is INFEASIBLE then
15 τA′= ConcatenateTrajectories ($\tau_{A},{\overline{\tau}}_{A}^{\prime})$;
// Add successors to stack in order of decreasing final time
30 return NULL, ∞, INFEASIBLE;
Algorithm 2 Constructing a cycle through Gtw and a trajectory intercepting each node in the cycle. See Alg. 1 for the PointToMovingTargetSearch function. See Section 3.5 for details on the Lookahead function.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Trajectory Tree", "weight": 1.0} -->

For each successor window-node $s^{\prime}$, we generate a successor tree-node $(S^{\prime},\tau_{A}^{\prime},T^{\prime})$ by generating a trajectory ${\overline{\tau}}_{A}^{\prime}$ that begins at $({\tau_{A}{(T)}},T)$ and intercepts $s^{\prime}$. We plan ${\overline{\tau}}_{A}^{\prime}$ using Alg., obtaining final time $T^{\prime} = {T + {g{(s^{\prime})}}}$. Condition in the definition of a successor window-node ensures that we always find a trajectory in this step.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Trajectory Tree", "weight": 1.0} -->

Next, we generate a path $S^{\prime}$ through $G_{tw}$ (or a cycle through $G_{tw}$, if $s^{\prime} = s_{d}$) by appending $s^{\prime}$ to $S$ (Alg., Line ). Then we perform a check denoted as Lookahead in Line.

<!-- chunk {"id": "body-0040", "role": "body", "section": "Trajectory Tree", "weight": 1.0} -->

where $|S^{\prime}|$ is the length of $S^{\prime}$. If inequality holds for some $i \in \Gamma_{unvisited}$,

<!-- chunk {"id": "body-0041", "role": "body", "section": "Trajectory Tree", "weight": 1.0} -->

then the agent has arrived at $s^{\prime}$ too late to intercept target $i$ in the future, making it impossible to intercept the set of unvisited targets. Thus we do not add $S^{\prime}$ as a successor to $S$. This Lookahead check is analogous to Test 1. While it is not needed for completeness, it reduces computation time.

<!-- chunk {"id": "body-0042", "role": "body", "section": "Trajectory Tree", "weight": 1.0} -->

If the Lookahead check succeeds, we concatenate ${\overline{\tau}}_{A}^{\prime}$ with $\tau_{A}$ to obtain trajectory $\tau_{A}^{\prime}$, and thereby a partial solution $(\tau_{A}^{\prime},T^{\prime})$ corresponding to $S^{\prime}$ (Line. If $s^{\prime} = s_{d}$, then $(\tau_{A}^{\prime},T^{\prime})$ is a feasible solution to the MT-TSP-O and we return. Otherwise, we add $(S^{\prime},\tau_{A}^{\prime},T^{\prime})$ to the list of successors of $S$. After obtaining all successors, we push the successors onto the stack in order of decreasing final time (Lines -), so the next popped tree-node will be the successor of $(S,\tau_{A},T)$ with the earliest final time.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Theoretical Analysis", "weight": 1.0} -->

In this section, we state MTVG-TSP's completeness theorems and sketch the proofs, providing full proofs in Appendix C in the supplementary material.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experiments", "weight": 1.0} -->

We ran all experiments on an Intel i9-9820X 3.3GHz CPU with 128 GB RAM. As a baseline, we implemented a sampled-points based method detailed in Section 5.1, based on prior work that solve special cases of the MT-TSP-O. We test MTVG-TSP and the baseline on 570 problem instances, where an instance consists of a depot location, trajectories and time windows of targets, and an obstacle grid. An example instance is shown in Fig., and we show a solution to an example instance in the video in the supplementary material. For each method, we measured the computation time for the method to obtain its first feasible solution for each instance, setting an upper limit of 300 s.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Baseline", "weight": 1.0} -->

For our baseline, based, we sample the trajectory of each target within its time windows into points in space-time, such that if we concatenated all of a target's time windows, the points would be spaced uniformly in time. Next, we plan the shortest obstacle-free path in space between each pair of points using, then convert the path into a trajectory where the agent moves at max speed along the path, then waits with zero velocity at the final position until the final time. If the agent cannot reach the final position by the final time, travel between those two points is infeasible. After computing these trajectories, we pose a generalized traveling salesman problem (GTSP) to find a sequence of points to visit. We then formulate the GTSP as an integer linear program (ILP) as, but without subtour elimination constraints. Subtours are only possible if trajectories of two targets intersect exactly in space and time, and we ensure this does not occur. We solve the ILP using Gurobi, obtaining a sequence of points, then concatenate the trajectories between every consecutive pair of points in the sequence to obtain a MT-TSP-O solution.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Baseline", "weight": 1.0} -->

Since we are not guaranteed to get a feasible solution for a fixed number of sample points, we initialize the algorithm with 10 points per target. If the ILP is infeasible, we increase the number of points by 10 and attempt to solve the ILP again. We repeat this process until the ILP is feasible, then take the first feasible solution Gurobi produces. The computation time reported for an instance is the sum of computation times for all attempted numbers of sample points.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Generating Problem Instances", "weight": 1.0} -->

We generated two sets of instances, corresponding to Experiment 1 (Section 5.3) and Experiment 2 (Section 5.4). In Experiment 1, we varied the number of targets from 10 to 30 in increments of 10 and varied the sum of each target's time window lengths from 2 s to 50 s in increments of 4, keeping the number of time windows per target fixed to 2. In Experiment 2, we varied the number of targets as in Experiment 1 and the number of time windows per target from 1 to 6, keeping the sum of lengths fixed. We generated 10 instances for each choice of experiment parameters. When varying the sum of a target's time window lengths, we randomly generated the instances with the longest windows first, then randomly shortened the time windows to generate more instances. When varying the number of windows per target, we first generated instances with 1 window with length equal to 22 s, then randomly split this single window into multiple windows. We generated the instances prior to shortening and splitting time windows as follows to ensure all instances were feasible. First, we randomly sampled an occupancy grid with 20% of cells occupied.

<!-- chunk {"id": "body-0048", "role": "body", "section": "Generating Problem Instances", "weight": 1.0} -->

Then we initialized the agent at a random depot location $p_{d}$ in free space.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Generating Problem Instances", "weight": 1.0} -->

Sample an interception position $p^{i}$ in free space for target $i$.

<!-- chunk {"id": "body-0050", "role": "body", "section": "Generating Problem Instances", "weight": 1.0} -->

Plan a path in space from $p^{i - 1}$ to $p_{i}$ using.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Generating Problem Instances", "weight": 1.0} -->

Move the agent at a speed $\beta v_{max}$ along the path until the end of the path at $p^{i}$, obtaining an arrival time $t^{i} = {t^{i - 1} + {d^{i}/{({\beta v_{max}})}}}$, where $d^{i}$ is the distance traveled along the path. Here, we use $\beta = 0.99$ to make the instances challenging without making them borderline infeasible.

<!-- chunk {"id": "body-0052", "role": "body", "section": "Generating Problem Instances", "weight": 1.0} -->

Sample a piecewise linear trajectory for target $i$ such that the number of linear segments equals the specified number of time windows, the trajectory duration is greater than the specified sum of window lengths, and the trajectory arrives at position $p^{i}$ at time $t^{i}$. For each segment of the trajectory, we sample the velocity direction uniformly at random, then select the speed uniformly at random from the range $\lbrack\frac{v_{max}}{8},\frac{v_{max}}{4}\rbrack$. This range is, which studies the MT-TSP. After creating this trajectory, we randomly sample a subset of each segment's time interval to create the time windows.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Experiment 1: Varying Sum of Time Window Lengths", "weight": 1.0} -->

In this experiment, we varied the number of targets and the sum of each target's time window lengths. The results in Fig. show that as we increase the number of targets, we see wider and wider ranges for the sum of window lengths where MTVG-TSP outperforms the sampled-points method in median and maximum computation time. In these critical ranges, the sampled-points method's computation time is large because it needs a large number of points to find a feasible solution, as shown in Fig., leading to a large underlying integer program. In Appendix A in the supplementary material, we show that these peaks occur when there are large intervals in some target's time windows where no feasible MT-TSP-O solution intercepts the target. In these cases, it is difficult to sample a point in one of the usable intervals where some feasible solution does intercept the target, since the combined length of these usable intervals is small relative to the combined length of the time windows.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Experiment 1: Varying Sum of Time Window Lengths", "weight": 1.0} -->

MTVG-TSP's median computation time varies less significantly than the sampled-points method's, though MTVG-TSP's maximum computation time peaks in the same regions as the sampled-points method's. For example, in Fig. (b), consider the 20-target instance with the largest peak in MTVG-TSP's runtime, occuring when the sum of time window lengths equals 14 s. In this instance, we found that if we decreased the sum of lengths to 10 s, MTVG-TSP found a solution intercepting the same sequence of time windows as it did for the 14 s instance, but with 65% less computation time. The reason for this phenomenon is that in the 14 s instance, there are several paths through $G_{tw}$ that do not exist in the 10 s instance, adding branches to Alg. 's search tree. Profiling showed that in the 14 s instance, Alg. spent 60% of its time exploring these additional branches.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Experiment 1: Varying Sum of Time Window Lengths", "weight": 1.0} -->

The fact that it returned the same sequence of time windows as in the 10 s instance indicates that the additional paths through $G_{tw}$ are useless: they cannot be part of a cycle corresponding to a feasible MT-TSP-O solution, only adding to computation time. On the other hand, we found that increasing the sum of time window lengths from 14 s to 18 s caused MTVG-TSP to find a different time window sequence than in the 14 s instance, and twice as quickly. In this case, increasing time window lengths added useful paths to $G_{tw}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "Experiment 1: Varying Sum of Time Window Lengths", "weight": 1.0} -->

In Table, we compare the costs between the methods in instances where the sampled-points method found a solution^44^4MTVG-TSP found a solution in all instances.. The median percent difference in cost between the methods is small, indicating that both methods often provide similar solution quality. The range of percent differences is large, since we take the first feasible solution from each method as opposed to solving to optimality.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Experiment 2: Varying Number of Time Windows per Target", "weight": 1.0} -->

In this experiment, we varied the number of targets and number of time windows. Since the sampled-points method does not depend on the number of time windows, only the total set of times covered by the time windows (which we are not varying), we run the sampled-points method for the instances with one window, then show the same runtimes for instances with multiple time windows. As shown in Fig., when we decrease the number of time windows, MTVG-TSP outperforms the sampled-points method in median and max computation time. Both methods' computation times increase with the number of targets. To explain the trends in MTVG-TSP's computation time, we divide its computation time between its three major components: initial visibility computations (Section 3.2), time window graph construction (Section 3.4), and trajectory tree construction (Section 3.5). Fig. shows that computation time for all components increases with the number of targets and number of time windows per target. Increasing either of these quantities increases the total number of time windows, leading to more window-nodes in the time window graph.

<!-- chunk {"id": "body-0058", "role": "body", "section": "Experiment 2: Varying Number of Time Windows per Target", "weight": 1.0} -->

This requires adding more nodes into the initial visibility graph corresponding to endpoints of targets' trajectories within their time windows, and computing more visible interval sets. Both operations increase initial visibility computation time. More window-nodes also leads to more pairwise LFDT computations when constructing the time window graph. Finally, a larger time window graph leads to a wider and deeper trajectory tree, leading to a larger number of MTVG constructions and searches during trajectory tree construction.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Experiment 2: Varying Number of Time Windows per Target", "weight": 1.0} -->

We similarly break down the timing for the sampled-points method in this experiment in Appendix B, Fig., dividing time between GTSP graph construction (finding trajectories between all pairs of points) and GTSP solve time. GTSP solve time exceeds graph construction time when we have 20 or more targets.

<!-- chunk {"id": "body-0060", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we presented MTVG-TSP, a complete algorithm for the moving target traveling salesman problem with obstacles, leveraging a novel graph called a moving target visibility graph (MTVG). We showed that for a range of time window lengths, our algorithm takes less median and maximum time to find feasible solutions than prior methods. Future directions for this work are to incorporate kinodynamic constraints on the agent and involve multiple agents.
