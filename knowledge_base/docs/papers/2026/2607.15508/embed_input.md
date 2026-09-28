<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this paper, we address the challenge of multi-objective motion planning for systems under kinodynamic constraints. We consider three problem classes: (i) lexicographic optimization, in which objectives are minimized according to a strict priority ordering, (ii) constrained optimization, in which a primary objective is minimized subject to bounds on the remaining costs, and (iii) Pareto front optimization, in which the goal is to approximate the full set of optimal trade-offs among competing objectives. We first show that established cost scalarization methods for multi-objective problems cannot be extended to continuous-domain systems with correctness guarantees. Then, we propose a unified algorithmic framework built upon the Stable Sparse-RRT (SST) algorithm, in which the single representative maintained at each witness neighborhood is replaced by a representative set of locally Pareto-optimal nodes. This structure gives rise to three distinct algorithms: lexSST for lexicographic minimization, coSST for constrained optimization, and poSST for Pareto-front approximation. We provide theoretical guarantees for the completeness and optimality of our algorithms and demonstrate their effectiveness through extensive empirical evaluations.

<!-- chunk {"id": "body-0003", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning is a core capability for intelligent autonomous systems, governing how dynamic agents move safely and efficiently through their environments. Beyond collision avoidance, effective motion planning requires a notion of trajectory *quality*, which is classically captured by a *single* cost metric, e.g., path length. In practice, however, objectives are rarely singular: an autonomous vehicle must balance passenger comfort against travel time, and a mobile manipulator must trade off workspace clearance against task completion speed. When *multiple* competing objectives are present, no single trajectory is universally optimal. Rather, the space of high-quality solutions becomes a rich, multidimensional landscape of trade-offs, where the goal shifts to identifying *Pareto-optimal* solutions, i.e., those that cannot be improved in one objective without sacrificing another. This introduces several computational challenges, especially under kinodynamic constraints. In this work, we address these challenges and develop a *foundational* framework for *multi-objective kinodynamic motion planning* that enables efficient exploration, approximation, and reasoning over this landscape.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Fig. 1: Two-objective motion planning with obstacle clearance (c1) and path length (c2) objectives. (a) Workspace showing obstacles (light blue), goal region (green), theoretical Pareto-optimal trajectories (lines in purple-green color scale), and three planner solutions (thick lines). (b) The bi-objective space with color-coded solution costs and the true Pareto front.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Graph-based algorithms provide the earliest foundations for optimal path planning, with A^∗^ and its variants guaranteeing shortest paths over edge traversal costs. MOA^∗^ and NAMOA^∗^ generalize this optimality to multi-objective problems, returning the full set of Pareto-optimal paths. More recent work has dramatically improved efficiency with BOA^∗^ for bi-objective problems, EMOA^∗^ for arbitrarily many objectives, A^∗^pex for improved pruning of the Pareto front, and multi-objective search under linear temporal logic tasks. However, all of these methods require a finite graph representation, whereas real robotic platforms operate in continuous state spaces with complex dynamics.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

For continuous systems, constraint-based trajectory optimization methods have been introduced, including CHOMP, TrajOpt, and STOMP. However, these methods are designed for a single cost function and do not natively support multiple objectives (beyond scalarization). Further, they typically struggle with non-convex problems, which are common in practice.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

An alternative and more practical paradigm for planning in continuous domains is sampling-based algorithms, which have been extended to kinodynamic systems via tree structures in which nodes (states) are expanded by sampling a control and propagating it through the dynamics. Notably, the Stable Sparse-RRT (SST) planner established that asymptotic near-optimality can be achieved by maintaining a sparse set of locally optimal nodes within witness neighborhoods, and subsequent work further improved efficiency through dominance-informed pruning and sparse roadmaps. However, these planners remain limited to single-objective optimization.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

To extend an existing single-cost planner to multiple objectives, the prevailing approach is to scalarize the costs into a single objective, then apply a standard cost-aware planner. Weighted-sum (WS) scalarization is the most common choice, but it is structurally limited to recovering solutions on the convex hull of the Pareto front, missing solutions in non-convex regions. Weighted-maximum (WM) scalarization addresses this limitation and can, in principle, reach any Pareto-optimal point. However, the mapping from weights to the resulting trade-off remains opaque, making it impractical to target a specific trade-off, especially in kinodynamic settings. Recent work proposes principled weight-sampling strategies for Pareto-front approximation via scalarization, but each weight vector still requires a separate planning run. To our knowledge, no scalarization approach guarantees asymptotic optimality or completeness for multi-objective planning in continuous domains.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this work, we address the gap above by introducing a unified framework for multi-objective sampling-based kinodynamic motion planning that is applicable to general dynamical systems and arbitrary smooth cost functions. We specifically consider three common problems in multi-objective optimization: (i) lexicographic optimization, in which objectives are minimized according to a strict priority ordering, (ii) constrained optimization, in which a primary objective is minimized subject to bounds on the remaining costs, and (iii) Pareto front optimization, in which the goal is to approximate the full set of optimal trade-offs among competing objectives. We first show that cost-scalarization methods cannot solve these problems with correctness and completeness guarantees.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our key insight is that to approach Pareto optimality, a *representative set* of locally Pareto-optimal nodes must be maintained in the motion tree. This enables the simultaneous tracking and refinement of non-dominated subtrajectories within a single search tree. We then build upon SST and, by incorporating this idea, propose three algorithms: lexSST, coSST, and poSST, each tailored to one of the aforementioned problems. We prove that these algorithms are probabilistically $\delta$-robustly complete and asymptotically near-optimal. We illustrate their power through eight case studies, comparing them against scalarization-based baselines.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Introduction", "weight": 1.5} -->

In short, our contributions are sixfold: We prove that no scalar utility function can correctly represent lexicographic dominance over continuous cost spaces, establishing a fundamental limitation of scalarization-based approaches.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Introduction", "weight": 1.5} -->

We introduce the notion of $\epsilon$-equivalence, which relaxes the strict equality required by lexicographic dominance to a user-defined tolerance, enabling objective refinement in continuous settings.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose lexSST, the first probabilistically $\delta$-robustly complete and asymptotically near-optimal motion planner for lexicographic minimization of continuous dynamic systems with bi-objective costs.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose coSST, the first probabilistically $\delta$-robustly complete and asymptotically near-optimal motion planner for constrained optimization of continuous dynamic systems, resolving the structural incompleteness of single-representative planners for this problem class.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Introduction", "weight": 1.5} -->

We propose poSST, the first probabilistically $\delta$-robustly Pareto-complete and asymptotically near-Pareto-optimal motion planner for approximating the full Pareto front of kinodynamic systems with multiple objectives.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Introduction", "weight": 1.5} -->

We validate these theoretical properties through extensive empirical evaluations, demonstrating the effectiveness and computational efficiency of our methods against scalarization-based baselines.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

We consider a robot with motion dynamics given: where $x\in\mathbb{X}\subseteq\mathbb{R}^{d}$ is the state, $u\in\mathbb{U}\subset\mathbb{R}^{m}$ is the control input, and $f:\mathbb{X}\times\mathbb{U}\to\mathbb{R}^{d}$ is the vector field. We assume that the dynamics satisfy standard smoothness and regularity conditions.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

Specifically, the second derivative of $x$ is uniformly bounded, i.e., $\|\ddot{x}\|\leq M$ for some constant $M\in\mathbb{R}_{\geq 0}$, and $f$ is Lipschitz continuous in both $x$ and $u$, i.e., for all $x,x^{\prime}\in\mathbb{X}$ and $u,u^{\prime}\in\mathbb{U}$, there exist $K_{x},K_{u}\geq 0$ such that The robot operates in a bounded workspace containing static obstacles and is subject to state constraints, such as velocity limits. We collectively represent these constraints as the obstacle set $\mathbb{X}_{O}\subset\mathbb{X}$ in the state space. The collision-free portion of the state space is then defined as $\mathbb{X}_{f}=\mathbb{X}\setminus\mathbb{X}_{O}$.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem Formulation", "weight": 1.0} -->

In the classical kinodynamic motion planning problem, the aim is to find a robot trajectory from an initial state $x_{0}$ to a given goal region $\mathbb{X}_{G}\subseteq\mathbb{X}_{f}$ such that every state along the trajectory remains within $\mathbb{X}_{f}$.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Assumption 1 (​​)", "weight": 1.0} -->

The cost function $c$ is *Lipschitz continuous*, i.e, there exists constant $K_{c}>0$ such that for all $\pi,\pi^{\prime}\in\Pi$ with the same start state, i.e., $\pi=\pi^{\prime}$. Furthermore, consider a trajectory $\pi\in\Pi$ with duration $T>0$, and for $t\in[0,T]$, define $\pi^{t}$ and $\pi_{t}$ as its *prefix* up to time $t$ and *suffix* from time $t$, respectively, so that their concatenation $\pi^{t}\cdot\pi_{t}=\pi$. Then, it holds that, for all $t\in[0,T]$: Given $N\in\mathbb{N}_{\geq 2}$ scalar cost functions ${c_{1},\ldots,c_{N}}$ that satisfy Assumption 1.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Assumption 1 (​​)", "weight": 1.0} -->

‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), we aggregate them into a cost vector We are interested in high-quality motion plans that account for all pertinent cost metrics. This naturally motivates a multi-objective framework, in which we specifically focus on three problem classes: *lexicographic-optimal*, *constrained-optimal*, and *Pareto-optimal* planning.

<!-- chunk {"id": "body-0022", "role": "body", "section": "II-A Lexicographic-Optimal Motion Planning", "weight": 1.0} -->

Here, we assume that the ordering of a cost vector $C$ reflects the user-defined priorities among its components. Specifically, $c_{1}$ is prioritized over $c_{2}$, $c_{2}$ over $c_{3}$, and so. We formalize this prioritization using the notion of lexicographic dominance.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Problem 1 (Lexicographic-optimal motion planning)", "weight": 1.0} -->

Consider a robot with dynamics described, obstacle set $\mathbb{X}_{O}\subset\mathbb{X}$, an initial state $x_{0}\in\mathbb{X}_{f}=\mathbb{X}\setminus\mathbb{X}_{O}$, and a goal region $\mathbb{X}_{G}\subseteq\mathbb{X}_{f}$. Given a prioritized vector of cost functions $C=(c_{1},\ldots,c_{N})$, each satisfying Assumption 1. ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), compute a lexicographic-optimal motion plan $\pi^{*}_{\text{lex}}\in\Pi_{\text{sol}}$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "II-B Constrained-Optimal Motion Planning", "weight": 1.0} -->

In the second setting, we consider a constrained optimization problem. That is, we assume user-defined upper bounds on $N-1$ costs, and our goal is to minimize the last one.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Problem 2 (Constrained-Optimal Motion Planning)", "weight": 1.0} -->

Consider the setting described in Problem 1. ‣ II-A Lexicographic-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"). Given $N$ cost functions $c_{1},\dots,c_{N}$, each satisfying Assumption 1.

<!-- chunk {"id": "body-0026", "role": "body", "section": "Problem 2 (Constrained-Optimal Motion Planning)", "weight": 1.0} -->

In the bi-objective setting shown in Fig. 1, an upper bound $\bar{c}_{1}=94$ is imposed. The solution to Problem 2. ‣ II-B Constrained-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality") is then the trajectory whose cost lies at the intersection of the constraint boundary $\bar{c}_{1}=94$ (red) and the true Pareto front (black).

<!-- chunk {"id": "body-0027", "role": "body", "section": "II-C Pareto-Optimal Motion Planning", "weight": 1.0} -->

Lastly, we consider the setting in which no prioritization or constraints are imposed. Instead, the goal is to find a *set* of motion plans that simultaneously optimize all objectives. Since costs are often competing --- e.g., minimizing path length may reduce obstacle clearance --- no single trajectory can, in general, optimize every objective. The goal, then, is to characterize the trade-offs among objectives by identifying the set of Pareto-optimal solutions. We formalize this using the notion of dominance.

<!-- chunk {"id": "body-0028", "role": "body", "section": "Problem 3 (Pareto-Optimal Motion Planning)", "weight": 1.0} -->

Consider the setting in Problem 1. ‣ II-A Lexicographic-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"). Compute the Pareto front $\mathcal{C}^{*}$ and the corresponding set of Pareto-optimal motion plans $\Pi_{\text{sol}}^{*}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "Approach Overview", "weight": 1.0} -->

Problems 1. ‣ II-A Lexicographic-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")-3. ‣ II-C Pareto-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality") are multi-objective optimization problems subject to nonlinear kinodynamic constraints; hence, they are nonconvex and difficult to solve. Even in the single-objective setting, kinodynamic motion planning is challenging as it requires searching both the state space for feasible trajectories and the objective space for cost improvements. In particular, computing a truly optimal motion plan is intractable, since even small perturbations to a candidate trajectory can yield strict improvements.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Approach Overview", "weight": 1.0} -->

State-of-the-art planners (e.g., ) mitigate this by introducing sparsity into the search, retaining only trajectories that differ sufficiently in cost or state, while relying on sampling and forward propagation to handle kinodynamic constraints. This relaxes the problem to finding near-optimal solutions with suboptimality bounded by a user-defined sparsity metric.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Approach Overview", "weight": 1.0} -->

We extend these ideas to the multi-objective cases for Problems 1. ‣ II-A Lexicographic-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")-3. ‣ II-C Pareto-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), by guaranteeing that near-optimal solutions are found with respect to the Pareto-point(s) of interest. For Problem 3. ‣ II-C Pareto-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), we approximate the entire Pareto front with arbitrarily tight bounds, enabling accurate representation of any desired trade-off among objectives.

<!-- chunk {"id": "body-0032", "role": "body", "section": "III-A Stable Sparse RRT (SST)", "weight": 1.0} -->

SST is a sampling-based kinodynamic planner that achieves asymptotic near-optimality for a single objective (cost) by growing a sparse motion tree in the state space $\mathbb{X}$ with cost-informed selection and pruning. Like RRT-based planners, it iteratively selects a node, propagates it forward under randomized controls, and adds a new state if feasible. To guide the search, SST samples a random state in $\mathbb{X}$ and selects the best-cost node (state) within a radius of $\delta_{\text{BN}}>0$ for extension.

<!-- chunk {"id": "body-0033", "role": "body", "section": "III-A Stable Sparse RRT (SST)", "weight": 1.0} -->

In addition, SST employs witness nodes: each defining a neighborhood (hyper-ball) of radius $\delta_{s}>0$ centered at $x\in\mathbb{X}$ (denoted by $\mathcal{B}_{\delta_{s}}(x)=\{x^{\prime}\in\mathbb{X}\mid\|x^{\prime}-x\|\leq\delta_{s}\}$), and represented by the lowest-cost node within that ball. A new state becomes a representative if it improves upon the cost of an existing representative, or if it lies outside all existing neighborhoods and creates a new one. This process ensures sparsity while monotonically improving trajectories toward low-cost solutions.

<!-- chunk {"id": "body-0034", "role": "body", "section": "III-A Stable Sparse RRT (SST)", "weight": 1.0} -->

Due to the sparsity of the search tree, SST can only probabilistically guarantee the generation of a motion plan that is $\delta$-similar to an optimal solution $\pi^{*}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "III-B Scalarized Cost Function", "weight": 1.0} -->

A common approach to multi-objective optimization is to aggregate multiple costs into a single scalar objective, thereby enabling the use of standard cost-aware planners (e.g., SST). In this subsection, we briefly review two common scalarization methods, namely, *weighted sum* (WS) and *weighted maximum* (WM), and explain why they fail to address Problems 2. ‣ II-B Constrained-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality") and 3. ‣ II-C Pareto-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"). Further, in Section IV-A, we show that no scalarization method can recover the lexicographic minimum in continuous domains, making them unsuitable for Problem 1. ‣ II-A Lexicographic-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality").

<!-- chunk {"id": "body-0036", "role": "body", "section": "III-B1 Weighted-Sum (WS) Scalarization", "weight": 1.0} -->

The most common scalarization is the weighted sum, where the quality of a trajectory $\pi$ is described by a scalar cost where weights $w_{i}$ encode the relative importance of objectives.

<!-- chunk {"id": "body-0037", "role": "body", "section": "III-B1 Weighted-Sum (WS) Scalarization", "weight": 1.0} -->

Minimizing $c_{\text{ws}}$ produces a single Pareto-optimal trade-off, $\pi^{*}=\arg\min_{\pi\in\Pi_{\text{sol}}}c_{\text{ws}}(\pi)$. However, because this scalarization is a linear combination of objectives, it can only recover Pareto points lying on the convex hull of the Pareto front. Consequently, WS minimization cannot capture non-convex Pareto points and is thus incomplete for Problems 2. ‣ II-B Constrained-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality") and 3. ‣ II-C Pareto-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality").

<!-- chunk {"id": "body-0038", "role": "body", "section": "III-B2 Weighted-Maximum (WM) Scalarization", "weight": 1.0} -->

An alternative approach is the WM scalarization, which substitutes the summation of WS with a maximization operator, While WM avoids the convexity limitations of weighted sums, it still yields only a single Pareto point for each weight selection. For Problem 2. ‣ II-B Constrained-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), although suitable weights may exist to target a particular Pareto point (i.e., $\pi^{*}_{\text{co}}$), determining them a priori is generally not possible. For Problem 3. ‣ II-C Pareto-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), computing the full Pareto set would require repeatedly reinitializing a planner with different weights and then solving multiple independent planning problems. In contrast, our approach maintains and refines non-dominated trajectories within a single search tree, enabling simultaneous approximation of the entire Pareto set.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Lexicographic-Optimal Motion Planning", "weight": 1.0} -->

In this section, we present our approach to Problem 1. ‣ II-A Lexicographic-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"). We first show that a lexicographic ordering relation cannot be captured by any cost scalarization, then introduce a method to approximate the lexicographic-optimal solution with bounded error in bi-objective settings. In Section VI, we extend this approach to address $N$-dimensional cost spaces.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-A Limitations of Extending Lexicographic Ordering to Continuous Domains", "weight": 1.0} -->

When costs are limited to *integers*, i.e., vector $C(\pi)\in\mathbb{N}^{N}$, lexicographic ordering can be neatly captured by a utility function that assigns a unique scalar value to each cost vector according to a fixed priority among dimensions. Specifically, for a set of cost vectors $\mathcal{C}=\{C_{1},C_{2},\dots,C_{N}\}$ with each $C_{i}\in\mathbb{N}^{N}$, a lexicographic dominance relation $\succ_{\text{lex}}$ can be encoded using a utility function $u:\mathbb{N}^{N}\to\mathbb{R}$ that respects the ordering, i.e., $C\succ_{\text{lex}}C^{\prime}\iff u(C)>u(C^{\prime})$.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-A Limitations of Extending Lexicographic Ordering to Continuous Domains", "weight": 1.0} -->

A simple construction can exploit the discreteness of the domain (i.e., $\mathbb{N}$) of each cost component by assigning strictly decreasing scaling coefficients, so that any unit improvement in a higher-priority dimension outweighs the maximum possible variation across all lower-priority dimensions. Thus, the first component determines the primary ordering, the second breaks ties, and so. For example, for a weight $M\geq\max_{\pi\in\Pi_{\text{sol}}}\|C(\pi)\|_{\infty}$, the utility function ensures lexicographic ordering. However, when costs are defined in *continuous domains*, i.e., $C(\pi)\in\mathbb{R}^{N}$, which is the case in this work, lexicographic ordering $\succ_{\text{lex}}$ can *not* be represented by any utility function $u:\mathbb{R}^{N}\to\mathbb{R}$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-B $\\epsilon$-Equivalence for Lexicographic Minimization in $\\mathbb{R}^{N}$", "weight": 1.0} -->

Before presenting our approach, we first argue that, given the nature of sampling-based methods, a strict notion of lexicographic dominance is unsuitable; instead, we introduce a notion of $\epsilon$-equivalence, formalized below.

<!-- chunk {"id": "body-0043", "role": "body", "section": "IV-B $\\epsilon$-Equivalence for Lexicographic Minimization in $\\mathbb{R}^{N}$", "weight": 1.0} -->

When sampling from a continuous control space and integrating the dynamics, the likelihood of obtaining two trajectories $\pi$ and $\pi^{\prime}$ that yield identical costs $c_{i}(\pi)=c_{i}(\pi^{\prime})$ is vanishingly small. Consequently, lexicographic dominance effectively reduces to a scalar comparison on the highest-priority cost $c_{1}$, precluding meaningful consideration of lower-priority costs.

<!-- chunk {"id": "body-0044", "role": "body", "section": "IV-B $\\epsilon$-Equivalence for Lexicographic Minimization in $\\mathbb{R}^{N}$", "weight": 1.0} -->

To overcome this, we introduce the notion of $\epsilon$-equivalence, wherein cost components that differ by less than an $\epsilon>0$ tolerance are treated as "equivalent". Specifically, let $\Pi^{\epsilon}_{0}\subseteq\Pi_{\text{sol}}$ be a set of non-dominated trajectories, and let the minimum primary cost in this set be denoted by $\hat{c}^{*}_{1}=\min_{\pi\in\Pi^{\epsilon}_{0}}c_{1}(\pi)$. We first construct a set of $\epsilon$-equivalent trajectories in $c_{1}$ as Then, we can approximate $\pi^{*}_{\text{lex}}$ by finding the minimum secondary cost within this set, i.e., $\pi^{\epsilon}_{\text{lex}}=\min_{\pi\in\Pi^{\epsilon}_{1}}c_{2}(\pi)$.

<!-- chunk {"id": "body-0045", "role": "body", "section": "IV-B $\\epsilon$-Equivalence for Lexicographic Minimization in $\\mathbb{R}^{N}$", "weight": 1.0} -->

We now examine the properties of using $\epsilon$-equivalence in bi-objective settings and its limitations for systems with $N>2$ objectives.

<!-- chunk {"id": "body-0046", "role": "body", "section": "IV-B1 Case of $N=2$", "weight": 1.0} -->

Fig. 2: Approximating πlex* using ϵ-equivalence when N = 2.

<!-- chunk {"id": "body-0047", "role": "body", "section": "IV-B1 Case of $N=2$", "weight": 1.0} -->

Consider a 2D Pareto front as illustrated in Fig. 2. Let point $A$ represent the cost of a solution trajectory $\pi_{A}$ whose first cost component $c_{1}(\pi_{A})$ achieves the global minimum $c_{1}^{*}$, but whose secondary cost $c_{2}(\pi_{A})$ is significantly suboptimal. Let point $L$ denote the cost of the lexicographic optimum $\pi_{L}=\pi^{*}_{\text{lex}}$.

<!-- chunk {"id": "body-0048", "role": "body", "section": "IV-B1 Case of $N=2$", "weight": 1.0} -->

Therefore, for a algorithm that can approximate a solution trajectory $\pi\in\Pi_{\text{sol}}$ with bounded (cost) error this approach yields a solution with error $\vec{e}_{\text{lex}}=\vec{e}_{\textsc{alg}}+(\epsilon_{1},0)$ from the true lexicographic optimal. Clearly, as $\epsilon_{1}\to 0$, $\vec{e}_{\text{lex}}\to\vec{e}_{\textsc{alg}}$ monotonically.

<!-- chunk {"id": "body-0049", "role": "body", "section": "IV-B2 Case of $N>2$", "weight": 1.0} -->

Now consider a 3D Pareto front, as shown in Fig. 3, where each point on the surface corresponds to a cost vector of a Pareto-optimal trajectory. Using the same procedure, we construct $\Pi^{\epsilon}_{1}$ by including all solutions with $c_{1}<c_{1}^{*}+\epsilon_{1}$, visualized as a half-space bounded by the orange plane in Fig. 3(a). Within this set, we compute $\hat{c}_{2}^{*}$, the best observed secondary cost (located at point $B$), and form $\Pi^{\epsilon}_{2}$ by retaining only those elements with $c_{2}<\hat{c}_{2}^{*}+\epsilon_{2}$, represented by the green plane.

<!-- chunk {"id": "body-0050", "role": "body", "section": "IV-B2 Case of $N>2$", "weight": 1.0} -->

Fig. 3: Example in which ϵ-equivalence fails to capture a bound on the true lexicographic optimum (point L). (a) Pareto front for three cost objectives. Half-space partitions representing filtering at Π1ϵ (orange) and Π2ϵ (green). (b) Projection onto the c1-c2 plane. (c) Projection onto the c2-c3 plane.

<!-- chunk {"id": "body-0051", "role": "body", "section": "IV-B2 Case of $N>2$", "weight": 1.0} -->

Crucially, because $\hat{c}_{2}^{*}$ may be less than $c_{2}(\pi^{*}_{\text{lex}})$ (i.e., point $c_{2}(B)<c_{2}(L)$), the second filtering step may discard the true lexicographic optimal point altogether (Fig. 3b). Consequently, the final set used to minimize $c_{3}$ may not include $\pi^{*}_{\text{lex}}$, and the resulting solution $\pi^{\epsilon}_{\text{lex}}$ may have an arbitrarily poor $c_{3}$ cost (point D, Fig. 3c).

<!-- chunk {"id": "body-0052", "role": "body", "section": "IV-B2 Case of $N>2$", "weight": 1.0} -->

That is, $|c_{3}(\pi^{\epsilon}_{\text{lex}})-c_{3}(\pi^{*}_{\text{lex}})|\in0,\infty).$ The source of this failure lies in the compounded filtering: once $\pi^{*}_{\text{lex}}$ is excluded at any intermediate step $i$, it can no longer influence the minimization of subsequent cost components $c_{i+1},\dots,c_{N}$. Thus, while $\epsilon$-equivalence offers a practical heuristic, it fails to guarantee bounded approximation error for problems with more than two objectives.

<!-- chunk {"id": "body-0053", "role": "body", "section": "IV-B2 Case of $N>2$", "weight": 1.0} -->

Nevertheless, our approach for approximating the full Pareto set $\Pi_{\text{sol}}^{*}$ (detailed in Section [VI) can recover a near-optimal solution with respect to the true lexicographic optimal, since, by definition, it is a Pareto-optimal solution (i.e., $\pi^{*}_{\text{lex}}\in\Pi_{\text{sol}}^{*}$).

<!-- chunk {"id": "body-0054", "role": "body", "section": "IV-C lexSST", "weight": 1.0} -->

Having clarified these nuances of lexicographic optimization in continuous cost spaces, we now introduce our approach to Problem 1. ‣ II-A Lexicographic-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), lexicographic SST (lexSST). lexSST is an adaptation of SST, in that the algorithm iteratively grows a search tree $G=(V,E)$ and uses a set of witness nodes $S\subseteq V$ to define local neighborhoods $\mathcal{B}_{\delta_{s}}(s)$ about every $s\in S$ (refer to Section III-A ‣ III Preliminaries ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")). However, instead of each witness maintaining a single representative (lowest cost) node, lexSST maintains a representative set $R_{s}$ of viable candidates in $\mathcal{B}_{\delta_{s}}(s)$.

<!-- chunk {"id": "body-0055", "role": "body", "section": "IV-C lexSST", "weight": 1.0} -->

Our main contribution is the extension from a single representative in the single-cost case to a representative set in the multi-objective setting. All our proposed algorithms --- lexSST, coSST, and poSST --- leverage this structure to solve their respective problems and differ only in their definitions of $R_{s}$.

<!-- chunk {"id": "body-0056", "role": "body", "section": "IV-C lexSST", "weight": 1.0} -->

In each case, the representative set begins by considering non-dominated nodes at witness $s$. We define the local Pareto set of nodes within neighborhood $\mathcal{B}_{\delta_{s}}(s)$ as, For lexSST, we define the representative set as $R^{\text{lex}}_{s}:=L^{\epsilon}(V^{\text{PO}}_{\mathcal{B}_{s}})$, where $L^{\epsilon}(\cdot)$ returns the $\epsilon$-minimal set of nodes according to the procedure described in Section IV-B.

<!-- chunk {"id": "body-0057", "role": "body", "section": "IV-C lexSST", "weight": 1.0} -->

The algorithm begins by initializing the vertex $V$, edge $E$, witness $S$, and solution $\Pi^{\textsc{alg}}_{\text{sol}}$ sets. At each iteration, a node is selected for extension using the ParetoSelect routine (Algorithm 2), which uniformly samples a non-dominated node within a ball of radius $\delta_{\text{PS}}$ centered at a randomly selected state $x_{rand}$ returned by RandomSample.

<!-- chunk {"id": "body-0058", "role": "body", "section": "IV-C lexSST", "weight": 1.0} -->

1 $x_{rand}\leftarrow\textsc{RandomSample}(\mathbb{X})$; 2 $X_{near}\leftarrow\textsc{Near}(x_{rand},V,\delta_{\text{PS}})$; 3 $X_{pareto}\leftarrow\textsc{PruneDominated}(X_{near})$; 4 $x_{selected}\leftarrow\textsc{RandomSample}(X_{pareto})$; Input: xselected, 𝕌, Tprop 1 $t_{prop}\leftarrow\textsc{Sample}([0,T_{prop}]);\ u\leftarrow\textsc{Sample}(\mathbb{U})$; 2 return xnew ← xselected + ∫0tpropf(x(t), u)dt; Once a node is selected, it is extended using MonteCarloProp (Algorithm 3), which samples a random control and duration to propagate $x_{\text{selected}}$

<!-- chunk {"id": "body-0059", "role": "body", "section": "IV-C lexSST", "weight": 1.0} -->

according to, yielding a new candidate state $x_{\text{new}}$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "IV-C lexSST", "weight": 1.0} -->

The nearest witness $s_{\text{near}}$ is then identified via NearestWitness: if $s_{\text{near}}$ lies farther than $\delta_{s}$ from $x_{\text{new}}$, a new witness is created and associated with $x_{\text{new}}$; otherwise, $x_{\text{new}}$ is evaluated against the current representative set of $s_{\text{near}}$.

<!-- chunk {"id": "body-0061", "role": "body", "section": "IV-C lexSST", "weight": 1.0} -->

If $x_{\text{new}}$ is not pruned by either PruneLexSet or PruneDominated (Algorithms 4 and 5, respectively), then it is added to $R^{\text{lex}}_{s_{\text{near}}}$ and the motion tree. As well, the new node may result in the pruning of existing nodes. Nodes entering the goal region are added to the solution set $\Pi^{\textsc{alg}}_{\text{sol}}$ (Algorithm 6).

<!-- chunk {"id": "body-0062", "role": "body", "section": "IV-C lexSST", "weight": 1.0} -->

6 Remove x from R and V; 3 if not ∃ x′ ∈ R such that C(x′) ≻ C(x) then 6 if not ∃ x′ ∈ VℬsPO s.t.

<!-- chunk {"id": "body-0063", "role": "body", "section": "IV-C lexSST", "weight": 1.0} -->

This metric ensures that each set $R_{s}$ retains only nodes that are sufficiently different in cost, i.e., As the algorithm progresses, the state-space sparsity metric $\delta_{s}$ (inherited from SST) ensures a finite number of neighborhoods $\mathcal{B}_{\delta_{s}}(s)$ are reached, while $\vec{\varepsilon}$ ensures a finite number of representatives within each neighborhood. In Section VII, we show that $\vec{\varepsilon}$ directly affects the near-optimality of our proposed algorithms, and in Sec. VIII, we empirically demonstrate the trade-off between sparsity and solution quality by varying $\vec{\varepsilon}$.

<!-- chunk {"id": "body-0064", "role": "body", "section": "IV-C lexSST", "weight": 1.0} -->

The algorithm continues for a fixed time budget, incrementally growing the motion tree $G$ and maintaining a set of candidate solution trajectories $\Pi^{\textsc{alg}}_{\text{sol}}$. Upon termination, it returns the solution that minimizes the final cost component $\pi^{\epsilon}_{\text{lex}}=\arg\min_{\pi\in\Pi^{\textsc{alg}}_{\text{sol}}}c_{N}(\pi)$.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Constrained-Optimal Motion Planning", "weight": 1.0} -->

Here, we introduce our proposed algorithm, constrained-optimal SST (coSST), for solving Problem 2. ‣ II-B Constrained-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), with the goal of returning the trajectory that minimizes cost $c_{N}$ subject to $N-1$ constraints. Similar to lexSST, we define a representative set $R^{\text{co}}_{s}$ for each witness, but use a different pruning procedure to ensure efficient exploration while respecting the user-defined constraints $\bar{c}_{i}$.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Constrained-Optimal Motion Planning", "weight": 1.0} -->

Effectively, this replaces the shifting window of lexSST, retaining nodes with $c_{i}<\hat{c}_{i}^{*}+\epsilon_{i}$, with a static window keeping nodes with $c_{i}<\bar{c}_{i}+\bar{\epsilon}_{i}$. The buffer term $\bar{\epsilon}_{i}$ is introduced to ensure that a $\delta$-similar trajectory to the true solution $\pi^{*}_{\text{co}}$ is not pruned prematurely, as discussed in Section VII-C. Formally, we define the representative set as As with lexSST, $R^{\text{co}}_{s}$ only contains non-dominated nodes.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Constrained-Optimal Motion Planning", "weight": 1.0} -->

Intuitively, each witness neighborhood maintains a slice of its local Pareto front, defined by the intersection of half-spaces $c_{i}\leq\bar{c}_{i}+\bar{\epsilon}_{i}$ for cost dimensions $i\in\{1,\dots,N-1\}$. As the algorithm progresses, nodes are selected from $R^{\text{co}}_{s}$ for extension, ensuring all viable subtrajectories are maintained. Since costs are monotonic, we can safely prune nodes that exceed this threshold and focus our search on more promising ones.

<!-- chunk {"id": "body-0068", "role": "body", "section": "Constrained-Optimal Motion Planning", "weight": 1.0} -->

Further, if an admissible cost-to-go heuristic $g:\mathbb{X}\times 2^{\mathbb{X}}\rightarrow\mathbb{R}_{\geq 0}$ is available, this pruning can be made more aggressive by retaining nodes that satisfy $c_{i}(x)\leq\bar{c}_{i}+\bar{\epsilon}_{i}-g(x,\mathbb{X}_{G})$.

<!-- chunk {"id": "body-0069", "role": "body", "section": "Constrained-Optimal Motion Planning", "weight": 1.0} -->

The algorithm for coSST follows that of Algorithm 1, except that we replace PruneLexSet in Line 10 with PruneCoSet (Algorithm 7). Upon termination, coSST returns the solution that minimizes the unconstrained cost, i.e., $\pi_{\text{co}}=\arg\min_{\pi\in\Pi^{\textsc{alg}}_{\text{sol}}}c_{N}(\pi)$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "V-A Limitations of SST for Constrained Optimization", "weight": 1.0} -->

The solution to Problem 2. ‣ II-B Constrained-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality") involves minimizing a single cost while satisfying the remaining $N-1$ constraints, yielding an optimal trajectory $\pi^{*}_{\text{co}}$. Unlike lexicographic optimization, no $\epsilon$-equivalence is required for tie-breaking, which might suggest that vanilla SST is sufficient. However, we show that because SST maintains only a single representative per witness, it cannot account for downstream constraint satisfaction and is therefore *incomplete* for Problem 2. ‣ II-B Constrained-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality").

<!-- chunk {"id": "body-0071", "role": "body", "section": "V-A Limitations of SST for Constrained Optimization", "weight": 1.0} -->

Consider the flytrap example in Fig. 4, where the agent must navigate from the start (yellow star) to the goal (red region) via a narrow passage. The goal is to minimize path length while satisfying a constraint on the line integral over a cost function shown in greyscale, i.e., $c_{1}(\pi)=\int_{\pi}\mathcal{N}(y)dy$, where $\mathcal{N}(y)$ is a Gaussian function evaluated at state $y$, and $c_{2}(\pi)=\int_{\pi}dy$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "V-A Limitations of SST for Constrained Optimization", "weight": 1.0} -->

The narrow passage can accommodate only a few witnesses through which all candidate solutions must pass. Now, consider three subtrajectories $\pi_{a},\pi_{b},$ and $\pi_{c}$ that arrive at witness $s$. Naively applying SST to optimize for path length ($c_{2}$) while pruning $c_{1}\leq\bar{c}_{1}$ would select $x_{b}$ as the representative of $s$, even if it nearly exceeds $\bar{c}_{1}$. Then, nodes $x_{a}$ and $x_{c}$ are pruned since they do not improve upon $c_{2}$. However, the minimum cost-to-go from $x_{b}$ may exceed the cost threshold (i.e., $c_{1}(\pi_{B})>\bar{c}_{1}$), rendering SST incomplete for Problem 2.

<!-- chunk {"id": "body-0073", "role": "body", "section": "V-A Limitations of SST for Constrained Optimization", "weight": 1.0} -->

‣ II-B Constrained-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"). Nearby witnesses would exhibit similar behavior, as the shortest path to any witness in the passage would pass through the high-cost region. In Section VIII-C, we demonstrate this limitation empirically.

<!-- chunk {"id": "body-0074", "role": "body", "section": "V-A Limitations of SST for Constrained Optimization", "weight": 1.0} -->

Fig. 4: Flytrap example showing the limitation of SST in minimizing PathLength given a constraint on GaussianCost.

<!-- chunk {"id": "body-0075", "role": "body", "section": "V-A Limitations of SST for Constrained Optimization", "weight": 1.0} -->

In contrast, conSST maintains all nodes that respect the cost constraints in each neighborhood. Therefore, $x_{a},x_{b},$ and $x_{c}$ are maintained in $R^{\text{co}}_{s}$, allowing the algorithm to select and extend each node with positive probability until a near-optimal motion plan is found (i.e., trajectory $\pi^{*}_{C}$). In Section VII, we prove that conSST is asymptotically near-optimal.

<!-- chunk {"id": "body-0076", "role": "body", "section": "Pareto-Optimal Motion Planning", "weight": 1.0} -->

Lastly, we present Pareto-optimal SST (poSST), a kinodynamic sampling-based motion planner that approximates the entire Pareto front of solution trajectories with arbitrarily tight error bounds, thereby solving Problem 3. ‣ II-C Pareto-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"). This algorithm closely mirrors the structure of lexSST and coSST but employs fewer pruning operations, thereby exploring a broader set of cost trade-offs.

<!-- chunk {"id": "body-0077", "role": "body", "section": "Pareto-Optimal Motion Planning", "weight": 1.0} -->

Specifically, poSST retains Pareto-optimal candidates per neighborhood (every node when $\vec{\varepsilon}=0$, otherwise a sparse subset). This can be interpreted as initializing coSST with constraints $\bar{c}_{i}=\infty$ for all $i$, allowing the algorithm to explore the full extent of the Pareto front. Consequently, the representative set for poSST is simply $R^{\text{PO}}_{s}:=V^{\text{PO}}_{\mathcal{B}_{s}}$, as no additional filters are applied. Upon termination, poSST returns a set of trajectories $\Pi^{\textsc{alg}}_{\text{sol}}$ rather than a single solution.

<!-- chunk {"id": "body-0078", "role": "body", "section": "Pareto-Optimal Motion Planning", "weight": 1.0} -->

Due to this broader search scope, poSST converges more slowly than lexSST and coSST, especially in high-dimensional cost spaces. However, it guarantees that all trade-offs among objectives are represented in the output, making it suitable for applications where post-hoc preference elicitation is necessary.

<!-- chunk {"id": "body-0079", "role": "body", "section": "Analysis", "weight": 1.0} -->

Here, we analyze the theoretical properties of our proposed algorithms, focusing on probabilistic completeness and near-optimality guarantees. For clarity, we first prove these properties for poSST, then show how the additional pruning procedures employed by lexSST and coSST preserve them within their respective problem classes. All the proofs are provided in the appendix.

<!-- chunk {"id": "body-0080", "role": "body", "section": "Analysis", "weight": 1.0} -->

We first extend the notions of probabilistic $\delta$-robust completeness (Def. 9. ‣ III-A Stable Sparse RRT (SST) ‣ III Preliminaries ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")) and asymptotic $\delta$-robust near-optimality (Def. 10. ‣ III-A Stable Sparse RRT (SST) ‣ III Preliminaries ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")) from to the multi-objective setting. When targeting a single solution, as in lexSST and coSST, Defs. 9. ‣ III-A Stable Sparse RRT (SST) ‣ III Preliminaries ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")-10. ‣ III-A Stable Sparse RRT (SST) ‣ III Preliminaries ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality") apply with slight alterations.

<!-- chunk {"id": "body-0081", "role": "body", "section": "Analysis", "weight": 1.0} -->

For poSST, which must approximate the entire Pareto front, we introduce analogous definitions that generalize these requirements to hold simultaneously across all Pareto-optimal solutions.

<!-- chunk {"id": "body-0082", "role": "body", "section": "VII-A Analysis of poSST", "weight": 1.0} -->

Here, we show that the pruning and selection procedures of poSST preserve the ability to generate a $\delta$-similar trajectory to any $\delta$-robust, Pareto-optimal solution $\pi^{*}\in\Pi^{*}_{\delta,\text{sol}}$, from which completeness and near-optimality follow. We begin by recalling three results. First, we relate the user-defined parameters $\delta_{\text{PS}}$ and $\delta_{s}$ to the dynamic clearance $\delta$.

<!-- chunk {"id": "body-0083", "role": "body", "section": "VII-A1 Properties of ParetoSelect", "weight": 1.0} -->

We first analyze ParetoSelect (Algorithm 2), which biases node selection toward locally non-dominated solutions, thereby accelerating convergence relative to simple nearest-neighbor selection.

<!-- chunk {"id": "body-0084", "role": "body", "section": "VII-A1 Properties of ParetoSelect", "weight": 1.0} -->

At each iteration, a random state $x_{\text{rand}}\sim\mathcal{U}(\mathbb{X})$ is sampled from a uniform distribution over $\mathbb{X}$. Then, all active nodes within a ball $\mathcal{B}_{\delta_{\text{PS}}}(x_{\text{rand}})$ are retrieved. The subset of these nodes that are not dominated by any other node in the set (with respect to all cost objectives) forms a local Pareto front. Finally, a random node $x_{\text{selected}}$ is chosen uniformly from this set for propagation.

<!-- chunk {"id": "body-0085", "role": "body", "section": "VII-A2 Properties of PruneDominated", "weight": 1.0} -->

The PruneDominated procedure (Algorithm 5) is used by poSST to retain only non-dominated candidate nodes at every witness neighborhood. Further, this procedure involves a sparsity parameter $\vec{\varepsilon}$ that ensures only one node is retained within a region of the objective space. Then, we bound the worst-case deviation from a reference trajectory $\pi^{*}$ that can result from applying PruneDominated.

<!-- chunk {"id": "body-0086", "role": "body", "section": "VII-A3 Near-optimality of poSST", "weight": 1.0} -->

We now derive a formal bound on the worst-case performance of poSST in approximating any Pareto-optimal trajectory. Building on the result that poSST can generate a $\delta$-similar trajectory to any reference trajectory $\pi^{*}\in\Pi^{*}_{\delta,\text{sol}}$, we analyze how this deviation in the state space translates into sub-optimality in the multi-objective cost space.

<!-- chunk {"id": "body-0087", "role": "body", "section": "VII-A3 Near-optimality of poSST", "weight": 1.0} -->

Let $\mathbf{K}_{c}=(K_{c,1},\dots,K_{c,N})\in\mathbb{R}^{N}_{\geq 0}$ denote the Lipschitz constants of the $N$ cost components. Intuitively, for any $\delta$-similar subtrajectories $\pi,\pi^{*}$, the cost deviation is bounded component-wise by $|c_{i}(\pi^{*})-c_{i}(\pi)|\leq\delta\cdot K_{c,i}$ for all $i$. We formalize this in the following theorem.

<!-- chunk {"id": "body-0088", "role": "body", "section": "VII-B Analysis of lexSST", "weight": 1.0} -->

We now analyze the impact of PruneLexSet on the poSST framework, arguing that its integration preserves the ability to generate a $\delta$-similar trajectory to the lexicographical minimum $\pi^{*}_{\text{lex}}\in\Pi^{*}_{\delta,\text{sol}}$ for bi-objective problems. Recall that rather than exploring the entire Pareto front, lexSST restricts the search to nodes within an $\epsilon$-tolerance of the current best-known primary cost, effectively considering a slice of width $\epsilon$ near the lexicographical optimum (shown in blue in Fig. 5).

<!-- chunk {"id": "body-0089", "role": "body", "section": "VII-B Analysis of lexSST", "weight": 1.0} -->

We first show that PruneLexSet does not remove nodes along a $\delta$-similar trajectory to $\pi^{*}_{\text{lex}}$.

<!-- chunk {"id": "body-0090", "role": "body", "section": "VII-C Analysis of coSST", "weight": 1.0} -->

The analysis of coSST mirrors that of lexSST, with the key difference that PruneConSet enforces a fixed constraint window $\bar{c}_{i}+\bar{\epsilon}_{i}$ rather than the shifting $\epsilon$-window of PruneLexSet. We show this substitution preserves the ability to generate a $\delta$-similar trajectory to $\pi^{*}_{\text{co}}$, the motion plan minimizing $c_{N}$ subject to all $N-1$ constraints. For compactness, we write $i\neq N$ to mean $i\in\{1,\dots,N-1\}$.

<!-- chunk {"id": "body-0091", "role": "body", "section": "Evaluations", "weight": 1.0} -->

We present a series of case studies designed to validate the theoretical contributions of this work and demonstrate the practical advantages of our proposed algorithms. We first introduce the experimental setup, then present our evaluations of lexSST, coSST, and poSST in the subsequent subsections.

<!-- chunk {"id": "body-0092", "role": "body", "section": "Workspaces", "weight": 1.0} -->

Experiments are conducted across four workspaces shown in Fig. 6: a simple environment (WS-1), a two-homotopy-class environment (WS-2), a three-homotopy-class environment (WS-3), and a cluttered environment with many homotopic solution classes (WS-4).

<!-- chunk {"id": "body-0093", "role": "body", "section": "Dynamics Models", "weight": 1.0} -->

We consider two dynamic models: (i) a 2D double integrator (Integrator) with state $x=[p_{x},p_{y},v_{x},v_{y}]^{\top}$ comprising position and velocity, and control input $u=[a_{x},a_{y}]^{\top}$ representing acceleration, and (ii) a 4D bicycle model (Bicycle) with dynamics: where $(p_{x},p_{y})$ is the rear-axle position, $\theta$ is the heading angle, and $\lambda$ is the steering angle. The control input consists of the longitudinal velocity $u_{v}$ and the steering rate $u_{\dot{\lambda}}$.

<!-- chunk {"id": "body-0094", "role": "body", "section": "Objective functions", "weight": 1.0} -->

We consider three cost functions: where $\mathcal{\check{D}}(x,\mathbb{X})$ is the shortest distance from state $x$ to the set $\mathbb{X}_{O}$. Each experiment is given two of the above objectives, with the goal of minimizing the associated cost functions.

<!-- chunk {"id": "body-0095", "role": "body", "section": "Objective functions", "weight": 1.0} -->

For example, a subset of Pareto-optimal trajectories for objectives PathLength and MaxMinClearance is shown in Figs. 6(a) and 6(b) for workspaces WS-1 and WS-2, respectively. Due to the simplicity of these environments and the interdependence of the objectives, the Pareto front can be computed analytically.

<!-- chunk {"id": "body-0096", "role": "body", "section": "Objective functions", "weight": 1.0} -->

Fig. 6: Considered workspaces. Shades of gray in (c) and (d) correspond to the values of GaussianCost.

<!-- chunk {"id": "body-0097", "role": "body", "section": "Setup", "weight": 1.0} -->

Results are reported across 100 independent runs and compared against weighted-sum SST (ws-SST) as the primary baseline. Each case study is designed to isolate a specific aspect of the proposed approach, progressing from single-solution problems to full Pareto front approximation.

<!-- chunk {"id": "body-0098", "role": "body", "section": "Setup", "weight": 1.0} -->

All algorithms were implemented in C++ as extensions to the SST implementation provided by the Open Motion Planning Library (OMPL). No parallelization was employed; all simulations were run sequentially on a machine equipped with an AMD Ryzen™ 5 8645HS processor (4.3 GHz base clock) and 16 GB of RAM. The implementation will be made publicly available upon the acceptance of the article.

<!-- chunk {"id": "body-0099", "role": "body", "section": "Case Study 1 -- lexSST vs SST", "weight": 1.0} -->

Fig. 7: Case Study 1 (lexSST vs. SST). Lexicographic objectives: MaxMinClearance (1st) and PathLength (2nd).

<!-- chunk {"id": "body-0100", "role": "body", "section": "Case Study 1 -- lexSST vs SST", "weight": 1.0} -->

Fig. 8: Case Study 2 (lexSST vs. ws-SST). Lexicographic objectives: MaxMinClearance (1st) and PathLength (2nd).

<!-- chunk {"id": "body-0101", "role": "body", "section": "Case Study 1 -- lexSST vs SST", "weight": 1.0} -->

We begin by validating lexSST's ability to approximate the true lexicographic minimum, as established in Theorems 4. ‣ VII-B Analysis of lexSST ‣ VII Analysis ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality") and 5. ‣ VII-B Analysis of lexSST ‣ VII Analysis ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"). The experiment considers workspace WS-1 with the Integrator model, where the optimization objective is lexicographic: minimize MaxMinClearance first, then PathLength. A 10-second planning budget was given per instance. Note that the primary optimum $c_{1}(\pi^{*}_{\text{lex}})$ is achieved by infinitely many trajectories, since any path traversing the widest passage without approaching an obstacle attains the same optimal clearance.

<!-- chunk {"id": "body-0102", "role": "body", "section": "Case Study 1 -- lexSST vs SST", "weight": 1.0} -->

The results are shown in Fig. 7. As seen in Fig. 7(a), SST (blue) reliably finds trajectories that maximize clearance but produces a wide spread of path lengths, since it lacks a mechanism to refine secondary objectives. In contrast, lexSST (orange) correctly prioritizes MaxMinClearance and simultaneously refines PathLength, yielding a tight cluster of solutions near the true lexicographic minimum (red dashed line). This behavior is further evident in the objective space (Fig. 7(b)), where SST solutions are broadly dispersed along the PathLength axis, while lexSST solutions concentrate around the lexicographic minimum (red diamond).

<!-- chunk {"id": "body-0103", "role": "body", "section": "Case Study 1 -- lexSST vs SST", "weight": 1.0} -->

The time series in Figs. 7(c)--7(d) shows the convergence behavior of both planners. Both SST and lexSST converge to $c_{1}(\pi^{*}_{\text{lex}})$ at comparable rates, and lexSST's final solutions remain within the user-defined tolerance $\epsilon$, consistent with Eq.. However, while SST exhibits a large spread in PathLength, lexSST steadily converges toward $c_{2}(\pi^{*}_{\text{lex}})$, demonstrating its ability to refine the secondary objective while respecting the tolerance on the primary one.

<!-- chunk {"id": "body-0104", "role": "body", "section": "Case Study 2 -- Robustness of lexSST to Weight Selection", "weight": 1.0} -->

Case Study 1 shows that SST produces wide variance in $c_{2}$ when optimizing $c_{1}$ alone. A natural remedy is to add a small weight to $c_{2}$, giving preference to solutions that also improve upon PathLength. Here, we demonstrate the practical failure of this approach in a setting where weight selection is consequential. Workspace WS-2 contains two homotopy classes: an upper corridor with slightly greater clearance and a lower corridor with shorter path length. Using the same dynamics model and objectives as Case Study 1, we compare lexSST against ws-SST with two weight vectors: $\mathbf{w}^{1}=[1,0.01]$ (blue) and $\mathbf{w}^{2}=[1,0.05]$ (green), shown in Fig. 8. Here, a 30-second planning budget was used.

<!-- chunk {"id": "body-0105", "role": "body", "section": "Case Study 2 -- Robustness of lexSST to Weight Selection", "weight": 1.0} -->

Despite both weight vectors appearing to heavily prioritize $c_{1}$, their behavior differs. In Fig. 8(a), $\mathbf{w}^{1}$ assigns insufficient weight to PathLength, resulting in solutions with high variance in $c_{2}$, similar to vanilla SST. Conversely, $\mathbf{w}^{2}$ overweights PathLength, biasing the planner toward the lower corridor at the expense of $c_{1}$-optimality. In contrast, lexSST consistently selects the upper corridor, forming a tighter bundle around $\pi^{*}_{\text{lex}}$.

<!-- chunk {"id": "body-0106", "role": "body", "section": "Case Study 2 -- Robustness of lexSST to Weight Selection", "weight": 1.0} -->

Fig. 8(b) shows these results in the objective space: ws-SST solutions exhibit either large $c_{2}$ variance ($\mathbf{w}^{1}$) or unbounded $c_{1}$ suboptimality ($\mathbf{w}^{2}$), while lexSST clusters about $\pi^{*}_{\text{lex}}$ within the user-defined tolerance $\epsilon$.

<!-- chunk {"id": "body-0107", "role": "body", "section": "Case Study 2 -- Robustness of lexSST to Weight Selection", "weight": 1.0} -->

The time series in Figs. 8(c)--8(d) are consistent with Case Study 1: all planners converge in $c_{1}$ at comparable rates, but only lexSST steadily improves $c_{2}$ toward $c_{2}(\pi^{*}_{\text{lex}})$; whereas the variance under $\mathbf{w}^{1}$ persists throughout the planning horizon. This underscores a fundamental limitation of scalarization: no fixed weight vector reliably guarantees near-optimality of the lexicographic solution, whereas lexSST achieves this without any weight tuning.

<!-- chunk {"id": "body-0108", "role": "body", "section": "VIII-C Constrained Optimization", "weight": 1.0} -->

We now evaluate coSST on Problem 2. ‣ II-B Constrained-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), examining its ability to restrict the search tree to constraint-admissible regions and its completeness advantage over SST. In the following studies, we use the Integrator model and a 10-second time budget per planning instance.

<!-- chunk {"id": "body-0109", "role": "body", "section": "Case Study 3 -- Constraint-Guided Search", "weight": 1.0} -->

(a) coSST search tree with $\Pi_{n}^{\textsc{alg}}$ dominance pruning.

<!-- chunk {"id": "body-0110", "role": "body", "section": "Case Study 3 -- Constraint-Guided Search", "weight": 1.0} -->

(b) Search tree with cost-to-go pruning for PathLength.

<!-- chunk {"id": "body-0111", "role": "body", "section": "Case Study 3 -- Constraint-Guided Search", "weight": 1.0} -->

Fig. 9: Case Study 3 (Constraint-guided search via coSST). Constrained search of πco* for objectives MaxMinClearance and PathLength.

<!-- chunk {"id": "body-0112", "role": "body", "section": "Case Study 3 -- Constraint-Guided Search", "weight": 1.0} -->

We apply a constraint $\bar{c}_{1}=91$ to MaxMinClearance in WS-1, requiring all trajectories to maintain a clearance of at least 9 units from obstacles. Fig. 9 shows the resulting search trees after a 10-second planning window, with nodes in yellow and witness neighborhoods in blue. The tree is visibly confined to the admissible region, returning multiple non-dominated solutions (in green), with the one that minimizes PathLength (in red).

<!-- chunk {"id": "body-0113", "role": "body", "section": "Case Study 3 -- Constraint-Guided Search", "weight": 1.0} -->

Fig. 10: Case Study 4 (incompleteness of SST for constrained optimization). SST fails to find feasible solutions in most runs, whereas coSST maintains completeness by retaining multiple constraint-admissible subtrajectories for each witness.

<!-- chunk {"id": "body-0114", "role": "body", "section": "Case Study 3 -- Constraint-Guided Search", "weight": 1.0} -->

Two additional pruning mechanisms further focus the search. First, we utilize a solution-set dominance check to prune nodes that are strictly dominated by existing solutions in $\Pi_{n}^{\textsc{alg}}$. Since costs increase monotonically, there is no risk of prematurely pruning such nodes. As shown in Fig. 9(a), this prevents exploration of the upper-right and lower-right regions of the workspace, since shorter solutions already exist. Second, we leverage an admissible cost-to-go heuristic which inflates each candidate node's PathLength cost by the shortest remaining path to the goal. As shown in Fig. 9(b), this disqualifies a substantially larger region, since reaching the goal within the remaining PathLength budget becomes infeasible from those states.

<!-- chunk {"id": "body-0115", "role": "body", "section": "Case Study 4 -- Incompleteness of SST", "weight": 1.0} -->

We empirically confirm the incompleteness of SST for constrained optimization, as argued in Section V-A. The task is to minimize PathLength subject to a constraint on GaussianCost in the narrow-passage environment in Fig. 10, with sparsity parameters chosen to guarantee the existence of a $\delta$-robust solution. We conduct 100 independent runs per planner, each with a 30-second time budget, using the Integrator model.

<!-- chunk {"id": "body-0116", "role": "body", "section": "Case Study 4 -- Incompleteness of SST", "weight": 1.0} -->

As shown in Figs. 10(a)--10(b), SST (blue) finds a valid motion plan in only a small fraction (0.11) of runs, whereas coSST succeeds across all runs. This failure is structural, not a consequence of limited planning time. Figs. 10(c)--10(d) show the search trees after a 300-second budget to ensure convergence. Because SST greedily optimizes for PathLength, its single representative at each witness accumulates a high GaussianCost, leaving no feasible extensions through the narrow passage. In contrast, coSST retains multiple constraint-admissible subtrajectories per witness, preserving the ability to extend through the passage. The cost of this completeness guarantee is a larger search tree, as shown in Fig. 10(e), since multiple nodes are maintained per witness.

<!-- chunk {"id": "body-0117", "role": "body", "section": "VIII-D Pareto Front Coverage", "weight": 1.0} -->

Having validated the single-solution algorithms, we now evaluate poSST on Problem 3. ‣ II-C Pareto-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"). We first demonstrate poSST's Pareto-completeness and near-optimality, and then show its computational advantages relative to scalarization methods.

<!-- chunk {"id": "body-0118", "role": "body", "section": "Case Study 5 -- Convex Pareto Front", "weight": 1.0} -->

We again consider a Integrator model in WS-1 under the objectives MaxMinClearance and PathLength, but without imposing any priority among the objectives, aiming to recover the entire Pareto front. Fig. 11(a) shows an example run as poSST discovers a diverse set of non-dominated trajectories that span the full Pareto front. Fig. 11(b) shows how the approximate front computed by poSST progressively approaches the theoretical optimum over time, with lighter hues indicating later times.

<!-- chunk {"id": "body-0119", "role": "body", "section": "Case Study 5 -- Convex Pareto Front", "weight": 1.0} -->

Over 100 runs with a 60-second planning budget, poSST identified, on average, 50 non-dominated solutions per run, providing broad coverage of the objective space as shown in Fig. 11(c). To quantify approximation quality, we define a coverage metric according to the ratio of the region dominated by the approximate front to the area enclosed by the true Pareto front and the axis-aligned boundary (red dashed lines in Fig. 11(b)). As shown in Fig. 11(d), poSST dominated, on average, roughly 80% of the reference area over the 60-second planning horizon, demonstrating its near-Pareto-optimality.

<!-- chunk {"id": "body-0120", "role": "body", "section": "Case Study 5 -- Convex Pareto Front", "weight": 1.0} -->

Fig. 11: Case Study 5 (efficacy of poSST in approximating Πsol* with objectives MaxMinClearance and PathLength). (a) and (b) show a single representative run. (c) and (d) aggregate over 100 runs.

<!-- chunk {"id": "body-0121", "role": "body", "section": "Case Study 6 -- Non-Convex Pareto Fronts", "weight": 1.0} -->

A key motivation for this work is the structural inability of weighted-sum scalarization to recover non-convex Pareto fronts, as established in Section III. We evaluate poSST with objectives GaussianCost and PathLength across two environments: WS-3 with three homotopic solution classes and a cluttered workspace, WS-4. We compare poSST against ws-SST initialized with 101 different weight vectors, spanning a normalized sweep of unique ratios to promote diverse solutions: Each instance of ws-SST is given a planning budget of 30-seconds (3030 seconds total), while poSST is given a single 30-second planning instance. This comparison is intentionally demanding, as the baseline is allocated $101\times$ the computational budget of poSST.

<!-- chunk {"id": "body-0122", "role": "body", "section": "Case Study 6 -- Non-Convex Pareto Fronts", "weight": 1.0} -->

Non-convex front recovery (Figs. 12(a), 12(c)): Workspace WS-3, using the Integrator model, isolates the structural limitation of WS scalarization (ws-SST) on a highly non-convex Pareto front, where many optimal trade-offs do not lie on the convex hull. Across the 101 weight selections, ws-SST collapses to two solution clusters: one that prioritizes PathLength by passing through the gap, and one that prioritizes GaussianCost by traveling over the wall. The intermediate trade-offs that balance both objectives are missed entirely. poSST, by contrast, discovers a diverse set of solutions spanning all three homotopic classes, empirically demonstrating the Pareto-completeness established in Theorem 2. ‣ VII-A2 Properties of PruneDominated ‣ VII-A Analysis of poSST ‣ VII Analysis ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality").

<!-- chunk {"id": "body-0123", "role": "body", "section": "Case Study 6 -- Non-Convex Pareto Fronts", "weight": 1.0} -->

Fig. 12: Case Study 6 (poSST vs. ws-SST on non-convex Pareto fronts). In WS-3, ws-SST recovers only extreme solutions, while poSST discovers trade-offs across all homotopic classes. In WS-4, a single run of poSST achieves better coverage than 101 scalarized planning instances combined.

<!-- chunk {"id": "body-0124", "role": "body", "section": "Case Study 6 -- Non-Convex Pareto Fronts", "weight": 1.0} -->

Computational efficiency (Figs. 12(b), 12(d)): In WS-4 using the Bicycle model, poSST recovers 124 unique Pareto-optimal solutions within a single 30-second planning instance, achieving better coverage than ws-SST across all 101 weight selections. As seen in Fig. 12(d), the cluster of solutions near the PathLength optimum reveals a key pitfall of WS scalarization: since PathLength operates over a larger range than MaxMinClearance, any weight ratio greater than about 0.5 collapses to the same solution, rendering most weight selections redundant. This imbalance is not known a priori, making it difficult to choose weights that yield a diverse spread. poSST avoids this issue entirely, as its element-wise cost comparisons require no unified (scalar) cost metric across objectives. Further, this case study highlights that maintaining a single, non-dominated search tree is substantially more efficient than repeatedly scalarizing and re-planning to recover a diverse set of trade-offs.

<!-- chunk {"id": "body-0125", "role": "body", "section": "Case Study 7 -- Effect of $\\vec{\\varepsilon}$ on Pareto Convergence", "weight": 1.0} -->

Finally, we examine the effect of the objective-space sparsity parameter $\vec{\varepsilon}$ introduced in this work, which governs the trade-off between near-optimality and tree size (sparsity). Using workspace WS-1 and the Integrator model, we sweep $\vec{\varepsilon}$ over a range of values and run 100 instances of poSST for each configuration over a 300-second planning horizon.

<!-- chunk {"id": "body-0126", "role": "body", "section": "Case Study 7 -- Effect of $\\vec{\\varepsilon}$ on Pareto Convergence", "weight": 1.0} -->

Fig. 13 presents results as box plots. As expected, larger $\vec{\varepsilon}$ values admit fewer nodes per witness neighborhood (Fig. 13(a)), reducing tree size but coarsening the approximation of the Pareto front (Fig. 13(c)). Conversely, smaller $\vec{\varepsilon}$ yields denser trees with tighter approximations at the cost of slower convergence rates (Fig. 13(d)). This experiment provides practical guidance for tuning $\vec{\varepsilon}$: in time-constrained settings, a moderate $\vec{\varepsilon}$ efficiently achieves broad Pareto coverage, whereas $\vec{\varepsilon}\to\mathbf{0}$ is appropriate when tight bounds are required.

<!-- chunk {"id": "body-0127", "role": "body", "section": "Case Study 7 -- Effect of $\\vec{\\varepsilon}$ on Pareto Convergence", "weight": 1.0} -->

Fig. 13: Case Study 7. Effect of ε⃗ on key metrics of poSST with objectives MaxMinClearance and PathLength.

<!-- chunk {"id": "body-0128", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we introduced a unified framework for multi-objective kinodynamic motion planning built on the Stable Sparse-RRT algorithm. Our key insight is the extension from a single representative per witness neighborhood to a *representative set*, enabling the simultaneous maintenance of locally Pareto-optimal subtrajectories within a single search tree. This structure underlies three algorithms: lexSST for lexicographic minimization, coSST for constrained optimization, and poSST for Pareto-front approximation.

<!-- chunk {"id": "body-0129", "role": "body", "section": "Conclusion", "weight": 1.5} -->

For lexSST, we proved that no scalar utility function can represent lexicographic dominance over continuous cost spaces, and, for coSST, we showed that vanilla SST is structurally incomplete under cost constraints. Instead, our algorithms are probabilistically complete and asymptotically near-optimal for both problems. Finally, poSST approximates the entire Pareto front in a single planning instance with formal completeness and bounded sub-optimality guarantees, recovering diverse trade-offs at a fraction of the computation time of repeated scalarized re-planning.

<!-- chunk {"id": "body-0130", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Several directions for future work remain. The $\epsilon$-equivalence approach for lexicographic search does not extend beyond two objectives; hence, how to apply lexSST with three or more cost functions remains an open question. Also, since the cost of maintaining representative sets grows with the number of non-dominated nodes per witness, leveraging GPU-accelerated and vectorized sampling-based planning could bring these algorithms closer to real-time deployment. Adaptation of these algorithms and their formal analysis for multi-objective problems are left to future work.
