<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

ADMM-based Continuous Trajectory Optimization in Graphs of Convex Sets

Topics include Trajectory optimization, Robustness, Graphs, Optimization, Control, Alternating-direction method of multipliers.

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper presents a numerical solver for computing continuous trajectories in non-convex environments. Our approach relies on a customized implementation of the Alternating Direction Method of Multipliers (ADMM) built upon two key components: First, we parameterize trajectories as polynomials, allowing the primal update to be computed in closed form as a minimum-control-effort problem. Second, we introduce the concept of a spatio-temporal allocation graph based on a mixed-integer formulation and pose the slack update as a shortest-path search. The combination of these ingredients results in a solver with several distinct advantages over the state of the art. By jointly optimizing over both discrete spatial and continuous temporal domains, our method accesses a larger search space than existing decoupled approaches, enabling the discovery of superior trajectories. Additionally, the solver's structural robustness ensures reliable convergence from naive initializations, removing the bottleneck of complex warm starting in non-convex environments.

<!-- chunk {"id": "body-0003", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Simultaneous discrete and continuous search is fundamental to various scientific and engineering domains, including task and motion planning, hybrid system control, and constrained decision-making. In these settings, discrete choices---such as selecting topological routes or contact modes---are intrinsically coupled with continuous variables like system states and control inputs. Given this interdependence, algorithms capable of efficiently addressing this problem class could have a profound impact across a vast portfolio of autonomous applications.

<!-- chunk {"id": "body-0004", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

Historically, the joint search over discrete and continuous spaces was considered prohibitively difficult, leading to a traditional decoupling of planning (high-level logic) and control (low-level execution). This separation allows for specialized numerical techniques: sampling- or search-based methods for the discrete planning stage and gradient-based optimization for the continuous control stage. However, this "numerical convenience" comes at a significant cost. By partitioning the search space, the optimization becomes blind to the global landscape, often resulting in holistically suboptimal performance.

<!-- chunk {"id": "body-0005", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

To address these challenges, this paper introduces a novel numerical solver that leverages a customized Alternating Direction Method of Multipliers (ADMM) for continuous trajectory optimization over a union of convex sets. This allows us to decompose the joint optimization into primal, slack, and dual updates, each tailored to exploit the specific mathematical structure of the problem.

<!-- chunk {"id": "body-0006", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We introduce the concept of a spatio-temporal allocation graph based on a mixed-integer formulation of the non-convex safety constraints. The graph encodes all feasible convex realizations of the problem and provides the structure required for projection onto the non-convex feasible set, thereby enabling an ADMM-based solver.

<!-- chunk {"id": "body-0007", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

By formulating the primal update as a quadratic minimum-control-effort problem over polynomial segments, we derive a closed-form solution. This approach is factorization-free, significantly reducing the per-iteration computational overhead.

<!-- chunk {"id": "body-0008", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

We frame the slack update as a shortest-path problem over the weighted allocation graph. Since the graph is directed and acyclic, this search procedure reduces to a simple dynamic programming iteration which can be carried out very efficiently.

<!-- chunk {"id": "body-0009", "role": "body", "section": "INTRODUCTION", "weight": 1.5} -->

The remainder of this paper is structured as follows: Section III formally defines the problem, while Section IV introduces the necessary mathematical background. We detail our proposed method in Section V and evaluate its performance through various benchmarks in Section VI. Finally, Section VII provides concluding remarks and discusses directions for future work.

<!-- chunk {"id": "body-0010", "role": "body", "section": "II-A Nonlinear Programming", "weight": 1.0} -->

A general approach to collision-free trajectory optimization in non-convex environments is to formulate collision avoidance constraints through direct nonlinear constraints between the trajectory and the environment. These formulations result in nonlinear programs which can be solved using general nonlinear solvers based on Newton-type methods such as interior-point (e.g. IPOPT ) and sequential convex programming (SNOPT ). However, formulating smooth nonlinear constraints with respect to general environment representations is non-trivial. In robotic motion planning, Ratliff et al. first introduced Euclidean signed-distance fields (ESDF) to obtain gradient information w.r.t. obstacles. The SQP-based solver TrajOpt by Schulman et al. considers signed-distance (SD) functions to convex obstacles and propose a geometric linearization procedure based on separating hyperplanes. Following work by Zhang et al. reformulates the generally non-differentiable SD constraints into an exact smooth formulation by exploiting the strong duality for convex sets.

<!-- chunk {"id": "body-0011", "role": "body", "section": "II-A Nonlinear Programming", "weight": 1.0} -->

A key limitation of these methods is their susceptibility to infeasible local minima affecting their reliability and completeness.

<!-- chunk {"id": "body-0012", "role": "body", "section": "II-B Mixed-Integer Programming", "weight": 1.0} -->

Mixed-integer programming offers a systematic way to encode exact obstacle avoidance constraints in smooth trajectory optimization. By modeling the non-convex set of obstacle-free states as the union of finitely many convex regions, one can perform a mixed-integer convex optimization in which the integer variables correspond to the assignment of trajectory segments to convex regions. This formulation is desirable for several reasons. First, the arbitrary connection of sets admits exploration of many different possible paths in a non-convex environment. Second, the flexible assignment of different numbers of (fixed-duration) segments to individual sets ensures spatio-temporal flexibility while avoiding nonlinear optimization over time as proposed by FASTER. However, the combinatorial nature of the mixed-integer problem makes it NP-hard and any algorithm that finds the global solution suffers from non-polynomial worst-case runtime. This prevents the application of MIQP beyond small problem instances. The seminal work by Marcucci et al. presents an empirically-tight convex relaxations of this problem based on Semi-Definite Programming. However, their method is limited to continuity and bounds up to velocity.

<!-- chunk {"id": "body-0013", "role": "body", "section": "II-C Decoupled Methods", "weight": 1.0} -->

Another widely adopted approach is to decompose the problem into a series of simpler subproblems. In the first stage, these approaches usually leverage shortest-path heuristics to heuristically solve the discrete and non-convex part of the planning problem and, only at a later stage, use continuous optimization to shape the trajectory in the selected corridor. Many works on autonomous navigation employ graph-search methods (e.g. A\* or RRT\* ) to find shortest paths on occupancy grids and subsequently construct a safe corridor. If there already exists a decomposition of the environment, the problem may be posed as a shortest path problem in a Graph of Convex Sets (GCS). Von Wrangel and Tedrake employ this method with convex surrogate cost for safe corridor selection and initialization of the non-convex setting involving constraints and cost on higher-order derivatives. In the subsequent stage, a continuous spatio-temporal trajectory is optimized inside a sequence of convex sets (corridor). The nonlinear relationship with respect to time still renders this a nonlinear programming (NLP) problem.

<!-- chunk {"id": "body-0014", "role": "body", "section": "II-C Decoupled Methods", "weight": 1.0} -->

Tordesillas et al. avoid optimizing over time and ensure temporal flexibility using a MIQP formulation. The most efficient approach is to reformulate the NLP into an unconstrained problem by relaxing constraints into soft penalties. However, these methods rely on cumbersome tuning for different scenarios and cannot guarantee constraint satisfaction.

<!-- chunk {"id": "body-0015", "role": "body", "section": "II-C Decoupled Methods", "weight": 1.0} -->

In our work, we adopt the general mixed-integer formulation which allows for flexible path and time allocation. Building upon this formulation, we present a novel gradient-based method based on ADMM which is efficient in finding locally optimal solutions to this problem.

<!-- chunk {"id": "body-0016", "role": "body", "section": "PROBLEM STATEMENT", "weight": 1.0} -->

In this section we introduce the problem formulation and the underlying assumptions that we make in order to solve the problem.

<!-- chunk {"id": "body-0017", "role": "body", "section": "PROBLEM STATEMENT", "weight": 1.0} -->

where $q:{{\lbrack 0,T\rbrack}\rightarrow{\mathbb{R}}^{d}}$ represents a continuous, sufficiently differentiable trajectory. Constraint (1b) enforces collision avoidance by requiring the trajectory $q$ to remain within the obstacle-free space $\mathcal{S} \subset {\mathbb{R}}^{d}$, which is generally non-convex. Dynamic feasibility is imposed through constraint (1c), where $\mathcal{D}$ denotes the set of dynamically admissible trajectories. Finally, the constraints in 1d enforce the boundary conditions for the start and goal positions. Due to the continuous-time formulation and the presence of nonlinear and non-convex constraints, solving directly is computationally intractable. We therefore introduce structural assumptions that render the problem numerically well posed and amenable to efficient optimization.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Objective -- Minimum Control Effort", "weight": 1.0} -->

We consider smooth trajectories that minimize the control effort required for the robot to follow these trajectories. The objective is therefore a weighted sum of quadratic energy integrals that penalize the derivatives of the trajectory.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Dynamic Feasibility -- Continuous Trajectories", "weight": 1.0} -->

For differentiable flat or linear systems, any sufficiently differentiable trajectory of the flat output variables guarantees the dynamic feasibility implicitly, provided that its derivatives are sufficiently bounded to avoid input saturation.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Safety -- Union of Convex Sets", "weight": 1.0} -->

Without loss of generality, we represent the non-convex search space through a union of convex sets as

<!-- chunk {"id": "body-0021", "role": "body", "section": "Safety -- Union of Convex Sets", "weight": 1.0} -->

where $\mathcal{Q}_{k}$ refers to a convex set $k$. We only require $\mathcal{Q}_{k}$ to be simple in the sense that Euclidean projections onto $\mathcal{Q}_{k}$ can be performed efficiently (e.g., ball sets, box sets, or polyhedra in low-dimensional spaces).

<!-- chunk {"id": "body-0022", "role": "body", "section": "Safety -- Union of Convex Sets", "weight": 1.0} -->

In the following, we introduce a transcription of the continuous state variables $q{(t)}$ and address the safety constraint over a union of convex sets through a mixed-integer formulation.

<!-- chunk {"id": "body-0023", "role": "body", "section": "METHOD", "weight": 1.0} -->

The solver presented in this work relies on two main building blocks: (i) a piecewise-polynomial parameterization of the system dynamics and (ii) a graph-based representation of the feasible space through an allocation graph. This section introduces these components and formalizes the required definitions before presenting the solver in the next section.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-A Trajectories as Piecewise Polynomials", "weight": 1.0} -->

To solve problem numerically, the trajectory $q{(t)}$ must be parameterized using a finite number of decision variables. Due to their smoothness and differentiability properties, polynomials provide a natural choice for this parameterization. Moreover, the feasibility and safety constraints defined in and can be enforced through linear relationships in the polynomial coefficients.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-A Trajectories as Piecewise Polynomials", "weight": 1.0} -->

A single polynomial is generally insufficient to represent an entire trajectory. To increase flexibility, the trajectory is divided into consecutive segments, each parameterized by an individual polynomial. A general $M$-segment polynomial trajectory $p:{{\lbrack 0,T_{\text{tot}}\rbrack}\mapsto{\mathbb{R}}^{d}}$ with $T_{\text{tot}} = {\sum_{m = 1}^{M}T_{i}}$ is defined as

<!-- chunk {"id": "body-0026", "role": "body", "section": "Derivatives", "weight": 1.0} -->

for $t \in {\lbrack 0,T_{m}\rbrack}$, which itself represents a Bézier curve with $n$ control points ${}_{}^{} = {{n/T_{m}}\left( {c_{m}^{i + 1} - c_{m}^{i}} \right)}$ and basis $\beta_{n - 1}^{i}{(\tau)}$. Thus, recursive application of this formula determines the control points of the higher-order derivatives.

<!-- chunk {"id": "body-0027", "role": "body", "section": "Continuity and Boundary Constraints", "weight": 1.0} -->

for all $j \in {\{ 0,\ldots,n_{c}\}}$ and $m \in {\{ 0,\ldots,{M - 1}\}}$, which relates control points of consecutive segments through linear relationships.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Continuity and Boundary Constraints", "weight": 1.0} -->

The boundary constraints can be expressed in an equivalent way, replacing one side of the equation with the fixed boundary derivatives.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Safety Constraints", "weight": 1.0} -->

Bézier curves are widely used in constrained trajectory optimization due to their convex hull property, which guarantees that the curve lies entirely within the convex hull of its control points.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Safety Constraints", "weight": 1.0} -->

Given our safety constraint ${p_{m}{(t)}} \in {\bigcup_{k \in \mathcal{K}}\mathcal{Q}_{k}}$ defined over a union of convex sets, we will keep the assignment of segments to sets flexible which is discussed in the next section.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Time Allocation", "weight": 1.0} -->

For a given time-allocation $\mathbf{T} = {\lbrack T_{1},T_{2},\ldots,T_{m}\rbrack}$ both the continuity and boundary constraints depend linearly on the control points $c = {\lbrack c_{0},c_{1},\ldots,c_{M}\rbrack}^{\top}$ and can be written in the compact matrix form as ${{\mathbf{A}_{\text{cont}}c} = 0},{{\mathbf{A}_{\text{bound}}c} = q_{0}}$, respectively. The same is true for the inequality constraints on the derivatives ${\mathbf{A}_{\text{ineq}}c} \leq b$. The quadratic objective can be rewritten in block-diagonal structure $c^{\top}\mathbf{Q}c$, overall yielding a convex quadratic program (QP).

<!-- chunk {"id": "body-0032", "role": "body", "section": "IV-B Spatio-temporal Allocation Graph", "weight": 1.0} -->

In the previous section, we introduced the piecewise trajectory but did not address the non-convex union of convex set constraint. In the following, we provide more insights regarding the underlying topological structure of this constraint through an intersection graph. Secondly, we introduce a mixed-integer formulation for this constraint and use it to derive the concept of a spatio-temporal allocation graph. This graph structure is one of the main results, ensuring the success and efficiency of our solver.

<!-- chunk {"id": "body-0033", "role": "body", "section": "IV-B1 Intersection Graph $G_{\\text{I}}$", "weight": 1.0} -->

where each convex set $\mathcal{Q}_{k}$ is associated with a vertex $k$ and edges exist between intersecting sets. This is depicted in Fig. 2(a). The intersection graph encodes the adjacency structure of the sets ${\{\mathcal{Q}_{k}\}}_{k \in \mathcal{K}}$ and thus captures the connectivity of the free space $\mathcal{S}$. In particular, paths in $G_{\text{I}}$ correspond to sequences of overlapping convex regions that permit continuous transitions within $\mathcal{S}$.

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-B2 Mixed-integer Formulation", "weight": 1.0} -->

At this point, we will introduce a mixed-integer (MI) formulation of the safety constraints $\mathcal{S}$ to relate each segment $p_{m}$ of the trajectory to a safe set.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-B2 Mixed-integer Formulation", "weight": 1.0} -->

where the linear constraint (13b) ensures that segment $m$ is contained in at least one set $\mathcal{Q}_{k}$. The implication in (13a) is one-directional and $p_{m} \in \mathcal{Q}_{l}$ does not require $b_{ml} = 1$, allowing segment $p_{m}$ to be contained in multiple sets.\

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-B2 Mixed-integer Formulation", "weight": 1.0} -->

Given the allocation of segment $m$ to set $k$ and segment $m + 1$ to set $l$ expressed through $b_{m,k} = b_{{m + 1},l} = 1$, these constraints ensure that there is only one active flow variable $y_{m,{(k,l)}}$ connecting both sets. Despite continuity being already guaranteed through continuity constraints between individual segments, explicitly enforcing adjacency between sets reduces the number of possible binary combinations in the MIP and will be crucial for the result presented in the next section. We highlight that imposing these constraints does not restrict the feasible set of the original problem.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-B3 Allocation Graph $G_{\\text{A}}$", "weight": 1.0} -->

In the following, we show that the previously introduced mixed-integer formulation can be reformulated into a concise graph structure which we denote as allocation graph. We define each variable $b_{mk}$ to represent a vertex $(m,k)$ in this graph and each flow variable $y_{m,{(k,l)}}$ as an edge between two vertices $(m,k)$ and $({m + 1},l)$. A visual example is given in Fig. 2.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-B3 Allocation Graph $G_{\\text{A}}$", "weight": 1.0} -->

The constraint in 13b ensures only one set is selected for each segment $m$ which results in a layered structure of the graph. The mixed-integer flow conservation constraints (14a, 14b) enforce that exactly one incoming and one outgoing edge is selected at each layer, thereby ensuring connectivity across consecutive layers through a single path. The strict temporal ordering of the trajectory segments $0 = t_{0} < t_{1} < \cdots < t_{M} = T$ induces a natural orientation of the edges from layer $m$ to layer $m + 1$. Thus, the resulting allocation graph is a directed acyclic graph (DAG). We will exploit this structure for efficient graph search in our solver.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-B3 Allocation Graph $G_{\\text{A}}$", "weight": 1.0} -->

We remark that each path $\mathcal{P} \in G_{A}$ in the graph corresponds to a feasible solution. In particular, for a given path of binary variables ${\{ b_{mk}\}}_{m \in {\lbrack 0,\ldots,{M - 1}\rbrack}}$ the safe set becomes convex and problem reduces to a convex QP.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-C Problem Description", "weight": 1.0} -->

The problem only involves spatial parameters in the form of control points $c$. However, temporal flexibility of the trajectory is preserved through the spatio-temporal allocation graph in (15d). Analogously, the graph structure encodes alternative feasible routes and retains the non-convex solution space.

<!-- chunk {"id": "body-0041", "role": "body", "section": "THE ACTOR SOLVER", "weight": 1.0} -->

The optimization problem in involves a quadratic objective (15a) with affine equality (15b) and affine inequality constraints (15c) but, most importantly, a non-convex set constraint (15d) arising from the union of convex sets.

<!-- chunk {"id": "body-0042", "role": "body", "section": "THE ACTOR SOLVER", "weight": 1.0} -->

In our solver, we employ the Alternating Direction Method of Multipliers (ADMM) to address this problem in a systematic way. The key idea is to decompose the problem into subproblems that isolate the difficult set constraint from the smooth quadratic objective. This allows each update step to reduce to a problem class that is well understood and computationally efficient.

<!-- chunk {"id": "body-0043", "role": "body", "section": "THE ACTOR SOLVER", "weight": 1.0} -->

To enable this decomposition, we introduce auxiliary (slack) variables that decouple the quadratic objective from the set constraints. Specifically, we rewrite in an equivalent consensus form

<!-- chunk {"id": "body-0044", "role": "body", "section": "THE ACTOR SOLVER", "weight": 1.0} -->

where $(\lambda_{nc},\rho_{nc})$ and $(\lambda_{c},\rho_{c})$ correspond to the dual variables and penalty parameters of the equality constraints (16c) and (16b), respectively.

<!-- chunk {"id": "body-0045", "role": "body", "section": "THE ACTOR SOLVER", "weight": 1.0} -->

The Method of Multipliers performs primal-dual iterations on the Lagrangian by first minimizing w.r.t. the primal variables $c,z$ before performing a dual-ascent step.

<!-- chunk {"id": "body-0046", "role": "body", "section": "THE ACTOR SOLVER", "weight": 1.0} -->

These steps can be iterated until a desired convergence tolerance is achieved.

<!-- chunk {"id": "body-0047", "role": "body", "section": "THE ACTOR SOLVER", "weight": 1.0} -->

In the following, we detail each subproblem and provide its corresponding solution.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-1 Primal -- Equality-constrained QP", "weight": 1.0} -->

whose solution can be obtained by solving the linear system arising from the optimality conditions ${\mathbf{A}_{\text{eq}}c^{+}} = \mathbf{b}$, ${{\overset{\sim}{\mathbf{Q}}c^{+}} + \overset{\sim}{q} + {\mathbf{A}_{\text{eq}}^{\top}\lambda_{\text{eq}}^{+}}} = 0$. Since both $\overset{\sim}{\mathbf{Q}}$ and $\mathbf{A}_{\text{eq}}$ remain unchanged between iterations, the factorization can be performed offline and online evaluation of $c^{\ast}$ only involves sparse matrix multiplications.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-2 Slack -- Projection & Shortest Path Problem", "weight": 1.0} -->

The slack update (18b) resembles the general form of a Euclidean projection problem

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-2 Slack -- Projection & Shortest Path Problem", "weight": 1.0} -->

where $\overline{z}$ includes the primal solution $c^{+}$ and $\mathcal{X}$ represents the feasible set. Intuitively, this step involves a projection of the primal variables onto the feasible set as illustrated in Fig. 3b. Since terms for $z_{c}$ and $z_{nc}$ are fully separable, this step is split into individual problems for each set.

<!-- chunk {"id": "body-0051", "role": "body", "section": "Safety Set ($\\mathcal{S}$)", "weight": 1.0} -->

For the variables $z_{nc}$, the update involves a projection onto a non-convex set which may not be unique. In our setting, we have encoded all combinations of feasible segment-set projections in the spatio-temporal allocation graph $G_{A}$ that we introduced in (IV-B3). In accordance with 18b, we seek the minimizer of

<!-- chunk {"id": "body-0052", "role": "body", "section": "Safety Set ($\\mathcal{S}$)", "weight": 1.0} -->

with $\overline{z} = c$. We have omitted the subscript of $z_{nc}$ for clarity. The objective and constraints are fully separable for each segment $m$. Further, given a segment-set allocation $(m,k)$, it is also fully separable for each individual control point $z_{m}^{i}$.

<!-- chunk {"id": "body-0053", "role": "body", "section": "Safety Set ($\\mathcal{S}$)", "weight": 1.0} -->

which essentially becomes a shortest path problem involving the sum over all projection costs for each segment-set pair in a possible path $\mathcal{P} \in G_{A}$. In Fig. 3, we visualize the cost for both segment-set pairs in (b) and paths in (c), respectively.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Safety Set ($\\mathcal{S}$)", "weight": 1.0} -->

yielding a SPP on the weighted allocation graph $G_{A}$ with vertex cost $l_{mk}$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "Shortest Path Problem on DAG", "weight": 1.0} -->

As derived in IV-B3, the allocation graph $G_{A}$ is a directed acyclic graph (DAG) with layers induced through segments $m$. Thus, the shortest path problem can be solved through $m$ dynamic programming iterations in topological order.\
For each ${m = {1,\ldots,M}}:$

<!-- chunk {"id": "body-0056", "role": "body", "section": "Shortest Path Problem on DAG", "weight": 1.0} -->

where $V_{mk}$ is the value function and $\pi_{mk}$ the minimizing predecessor of each node. After the forward pass, the optimal path can be obtained by simple backtracking from the goal node by $k_{m - 1} = \pi_{m,k_{m}}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "Shortest Path Problem on DAG", "weight": 1.0} -->

Finally, the optimal projection $z_{nc}^{+}$ is obtained by selecting $z_{m}^{k}$ from (24 ‣ V-2 Slack – Projection & Shortest Path Problem ‣ V THE ACTOR SOLVER ‣ ADMM-based Continuous Trajectory Optimization in Graphs of Convex Sets")) based on the optimal path ${\{{(m,k)}\}}_{\mathcal{P}}$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-3 Dual - Gradient-ascent Step", "weight": 1.0} -->

After updating both primal variables $c$ and $z$ that minimize the AL, the dual update (18c) performs a gradient-ascent step on the Lagrange multipliers. This update gradually enforces consensus between variables $c$ and $z$. Intuitively, it acts as a price update that shifts the primal solution towards feasibility as depicted in Fig. 3d.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-A Overview", "weight": 1.0} -->

The method iterates between primal, slack, and dual updates until a prescribed convergence tolerance is achieved. A key practical advantage of this procedure is that each step is computationally lightweight. The primal update admits an efficient evaluation of the QP solution, while the slack update reduces to projection and graph search operations whose complexity scales linearly with the number of sets and trajectory segments, respectively. The method requires only a single set of hyperparameters, the penalty parameters $\rho_{nc}$ and $\rho_{c}$, which correspond to the step size of the dual ascent step.

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-B Convergence and Completeness", "weight": 1.0} -->

Unlike the convex case, there is no general guarantee that ADMM will converge to a globally optimal point for non-convex set constraints and it must be considered a local optimization method. However, our method encodes all feasible^11^1feasibility here only refers to the non-convex constraint $\mathcal{S}$ solutions of the MIQP in the allocation graph $G_{A}$ and searches for the locally optimal one in each iteration V-2. Recall that each path $\mathcal{P} \in G_{A}$ corresponds to a convex QP based on our MI formulation in IV-B2. Thus, if the path $\mathcal{P}$ is frozen at any time, we recover the convex setting, and primal and dual residuals are guaranteed to converge to 0 in the limit. In practice, we observe that this happens naturally after a few tens of iterations and does not have to be enforced explicitly. The primal variables $c$ and $z$ will converge to stationary points under this condition, even if the bounded set $\mathcal{B}$ renders some QPs in $G_{A}$ infeasible.

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-B Convergence and Completeness", "weight": 1.0} -->

Infeasible solutions are naturally avoided in our algorithm by selecting the locally optimal path $\mathcal{P}$ in each iteration, but general completeness of the algorithm can only be guaranteed for the unbounded case.

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-B Convergence and Completeness", "weight": 1.0} -->

For the special case, where derivatives of the boundary conditions (start and goal states) are zero, we can solve the unbounded problem and afterwards scale the total time to satisfy any bounds on the derivatives of the trajectory.

<!-- chunk {"id": "body-0063", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

We demonstrate the effectiveness of ACTOR on a variety of numerical examples. Section VI-A illustrates, through qualitative comparisons, the key advantages of ACTOR over existing state-of-the-art approaches. We then demonstrate the method on a navigation task in Section VI-B. Section VI-C examines scalability and computational complexity. Finally, we highlight the advantages of our method in a challenging study on minimum-snap trajectory generation under higher-order feasibility constraints.

<!-- chunk {"id": "body-0064", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

Optimization-based Collision Avoidance (OBCA), a direct NLP formulation that enforces collision avoidance through direct nonlinear obstacle constraints. The resulting problem is solved using IPOPT.

<!-- chunk {"id": "body-0065", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

Safe corridor optimization (SafeC), as employed in several prior works which optimizes a spatio-temporal trajectory within a prescribed sequence of convex sets. Following, we use SNOPT as the NLP solver.

<!-- chunk {"id": "body-0066", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

A\*, used as path search heuristic both to initialize OBCA and to construct safe corridors for SafeC.

<!-- chunk {"id": "body-0067", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

Graph of Convex Sets (GCS), used as a convex surrogate method for safe corridor selection.

<!-- chunk {"id": "body-0068", "role": "body", "section": "EXPERIMENTS", "weight": 1.0} -->

We use the same polynomial parameterization and objective for all methods and rely on optimized C/C++ implementations. Only our method is implemented in Python/NumPy.

<!-- chunk {"id": "body-0069", "role": "body", "section": "VI-A Non-convex Environments", "weight": 1.0} -->

Non-convex space constraints pose a fundamental challenge in trajectory optimization, as they induce infeasible local minima and multiple homotopy classes. To demonstrate the conceptual benefits of our method, we consider two minimal illustrative scenarios that are specifically designed to expose characteristic weaknesses of existing trajectory optimization approaches. The first scenario depicted in Fig. 4(a) consists of a U-shaped obstacle positioned between start and goal. Both methods are initialized with a straight-line that enters the cavity of the obstacle. Escaping this cavity requires a global deformation that temporarily increases cost and constraint violation. OBCA follows local descent directions and converges to an infeasible stationary point from which it cannot escape, failing to produce a feasible trajectory. In ACTOR, each gradient step is coupled with the allocation graph, which encodes global connectivity of the free space and systematically guides the iterates toward a feasible homotopy class. Importantly, this behavior extends beyond minimal examples: in the highly non-convex maze shown in Fig. 1, ACTOR reliably converges to feasible trajectories despite the presence of numerous competing homotopy classes.

<!-- chunk {"id": "body-0070", "role": "body", "section": "VI-A Non-convex Environments", "weight": 1.0} -->

To address this limitation, many existing methods generate a feasible initialization or pre-select a convex safe corridor prior to optimization. While often effective, this strategy can yield suboptimal solutions by restricting the admissible solution space. We exemplify this in the second example in Fig. 4(b), which features multiple routes through a separating wall. In this scenario, we consider trajectories subject to dynamic initial and final state constraints and determine the optimal solution by solving the corresponding MIQP to global optimality. Both OBCA and SafeC when initialized from the shortest-path based on A\* yield suboptimal trajectories involving sharp turns and aggressive maneuvers. GCS selects a corridor based on convex approximations for the smooth nonlinear constraints and objective of the problem which results in a better homotopy choice and a smoother trajectory. However, the lack of tightness of these surrogates still affects the optimality of the solution. Only ACTOR converges to the globally optimal trajectory by jointly taking spatial and dynamic constraints into account.

<!-- chunk {"id": "body-0071", "role": "body", "section": "VI-B Naive Space Decomposition", "weight": 1.0} -->

Having demonstrated the key qualitative properties of ACTOR in the previous section, we now examine how these properties translate to practical navigation tasks. We adopt a point-cloud representation of the obstacles to highlight a key practical benefit of the proposed union-of-convex-sets formulation: free space can be decomposed in a simple and naive manner. Unlike existing methods, whose performance depends critically on carefully constructed free-space decompositions around a prescribed initial path, ACTOR can operate effectively on such naive decompositions. As shown in Fig. 5, the proposed graph formulation enables a much larger admissible solution space, allowing ACTOR to recover a substantially smoother trajectory than a corridor-based approach (SafeC), whose solution remains restricted to the pre-selected safe corridor. This ability of our method to operate on naive decompositions eliminates the need to pose free-space decomposition as an additional optimization problem, substantially simplifying the planning pipeline.

<!-- chunk {"id": "body-0072", "role": "body", "section": "VI-C Scalability", "weight": 1.0} -->

While the previous subsection established the practical relevance of ACTOR, we now investigate its scalability as the size of the problem increases. For a controlled comparison with existing safe-corridor methods, we consider problems defined over a single prescribed corridor and examine the resulting scaling behavior as the number of sets and trajectory segments increases. Within this setting, we compare ACTOR against a commercial MIQP solver, solving the same MIQP formulation as ours to global optimality as, and the NLP-based spatio-temporal SafeC formulation of. As shown in Fig. 6, runtimes for both the MIQP and NLP solver grow combinatorially or exponentially due to the repeated solution of increasingly large QPs. In contrast, ACTOR is factorization-free and exhibits per-iteration complexity linear in the number of sets and trajectory segments, thereby scaling substantially better to large problem instances.

<!-- chunk {"id": "body-0073", "role": "body", "section": "VI-D Quadrotor Minimum-Snap Trajectory Planning", "weight": 1.0} -->

Finally, we showcase the full strength of ACTOR on a challenging quadrotor minimum-snap planning problem that combines non-convex spatial constraints with higher-order dynamic feasibility constraints on velocity and acceleration. As shown in Fig. 1, our method is able to find a smooth and feasible trajectory in such a highly constrained setting, where most paths in the allocation graph are rendered infeasible by the constraints on velocity and acceleration. In fact, we observe reliable convergence from a naive initial guess to a feasible optimum in these settings as depicted in Figure 7. The number of discrete vertex changes in the allocation path stabilizes after 100 iterations, from which we retain the convex setting and rapid convergence to a pre-specified error tolerance. This experiment consolidates the main advantages of the proposed method: ACTOR jointly optimizes over continuous spaces involving the higher-order dynamics and discrete spaces involving non-convex geometry, avoiding the restrictive decoupling inherent to existing pipeline-based approaches.

<!-- chunk {"id": "body-0074", "role": "body", "section": "CONCLUSION", "weight": 1.5} -->

In this work, we introduced ACTOR, a novel solver for continuous trajectory optimization in non-convex environments described by general unions of convex sets. Central to the method is a spatio-temporal graph which enables the joint treatment of smooth dynamics and discrete constraints within a single ADMM-based optimization scheme. The resulting solver is robust to naive initialization, factorization-free, and exhibits linear scaling with respect to problem size. Extensive experimental results demonstrate its effectiveness, underscoring the potential of this framework as a principled and scalable foundation for motion planning and trajectory optimization in increasingly complex environments.
