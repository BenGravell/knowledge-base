<!-- arxiv-full-text:v1 {"arxiv_id": "2607.15508", "source": "arxiv-html"} -->

## Introduction

Motion planning is a core capability for intelligent autonomous systems, governing how dynamic agents move safely and efficiently through their environments. Beyond collision avoidance, effective motion planning requires a notion of trajectory *quality*, which is classically captured by a *single* cost metric, e.g., path length. In practice, however, objectives are rarely singular: an autonomous vehicle must balance passenger comfort against travel time, and a mobile manipulator must trade off workspace clearance against task completion speed. When *multiple* competing objectives are present, no single trajectory is universally optimal. Rather, the space of high-quality solutions becomes a rich, multidimensional landscape of trade-offs, where the goal shifts to identifying *Pareto-optimal* solutions, i.e., those that cannot be improved in one objective without sacrificing another. This introduces several computational challenges, especially under kinodynamic constraints. In this work, we address these challenges and develop a *foundational* framework for *multi-objective kinodynamic motion planning* that enables efficient exploration, approximation, and reasoning over this landscape.

(a) Solution paths in workspace.

(b) Solutions in objective space.

Fig. 1: Two-objective motion planning with obstacle clearance (c1) and path length (c2) objectives. (a) Workspace showing obstacles (light blue), goal region (green), theoretical Pareto-optimal trajectories (lines in purple-green color scale), and three planner solutions (thick lines). (b) The bi-objective space with color-coded solution costs and the true Pareto front.

Graph-based algorithms provide the earliest foundations for optimal path planning, with A^∗^ and its variants guaranteeing shortest paths over edge traversal costs. MOA^∗^ and NAMOA^∗^ generalize this optimality to multi-objective problems, returning the full set of Pareto-optimal paths. More recent work has dramatically improved efficiency with BOA^∗^ for bi-objective problems, EMOA^∗^ for arbitrarily many objectives, A^∗^pex for improved pruning of the Pareto front, and multi-objective search under linear temporal logic tasks. However, all of these methods require a finite graph representation, whereas real robotic platforms operate in continuous state spaces with complex dynamics.

For continuous systems, constraint-based trajectory optimization methods have been introduced, including CHOMP, TrajOpt, and STOMP. However, these methods are designed for a single cost function and do not natively support multiple objectives (beyond scalarization). Further, they typically struggle with non-convex problems, which are common in practice.

An alternative and more practical paradigm for planning in continuous domains is sampling-based algorithms, which have been extended to kinodynamic systems via tree structures in which nodes (states) are expanded by sampling a control and propagating it through the dynamics. Notably, the Stable Sparse-RRT (SST) planner established that asymptotic near-optimality can be achieved by maintaining a sparse set of locally optimal nodes within witness neighborhoods, and subsequent work further improved efficiency through dominance-informed pruning and sparse roadmaps. However, these planners remain limited to single-objective optimization.

To extend an existing single-cost planner to multiple objectives, the prevailing approach is to scalarize the costs into a single objective, then apply a standard cost-aware planner. Weighted-sum (WS) scalarization is the most common choice, but it is structurally limited to recovering solutions on the convex hull of the Pareto front, missing solutions in non-convex regions. Weighted-maximum (WM) scalarization addresses this limitation and can, in principle, reach any Pareto-optimal point. However, the mapping from weights to the resulting trade-off remains opaque, making it impractical to target a specific trade-off, especially in kinodynamic settings. Recent work proposes principled weight-sampling strategies for Pareto-front approximation via scalarization, but each weight vector still requires a separate planning run. To our knowledge, no scalarization approach guarantees asymptotic optimality or completeness for multi-objective planning in continuous domains.

In this work, we address the gap above by introducing a unified framework for multi-objective sampling-based kinodynamic motion planning that is applicable to general dynamical systems and arbitrary smooth cost functions. We specifically consider three common problems in multi-objective optimization: (i) lexicographic optimization, in which objectives are minimized according to a strict priority ordering, (ii) constrained optimization, in which a primary objective is minimized subject to bounds on the remaining costs, and (iii) Pareto front optimization, in which the goal is to approximate the full set of optimal trade-offs among competing objectives. We first show that cost-scalarization methods cannot solve these problems with correctness and completeness guarantees.

Our key insight is that to approach Pareto optimality, a *representative set* of locally Pareto-optimal nodes must be maintained in the motion tree. This enables the simultaneous tracking and refinement of non-dominated subtrajectories within a single search tree. We then build upon SST and, by incorporating this idea, propose three algorithms: lexSST, coSST, and poSST, each tailored to one of the aforementioned problems. We prove that these algorithms are probabilistically $\delta$-robustly complete and asymptotically near-optimal. We illustrate their power through eight case studies, comparing them against scalarization-based baselines.

In short, our contributions are sixfold: We prove that no scalar utility function can correctly represent lexicographic dominance over continuous cost spaces, establishing a fundamental limitation of scalarization-based approaches.

We introduce the notion of $\epsilon$-equivalence, which relaxes the strict equality required by lexicographic dominance to a user-defined tolerance, enabling objective refinement in continuous settings.

We propose lexSST, the first probabilistically $\delta$-robustly complete and asymptotically near-optimal motion planner for lexicographic minimization of continuous dynamic systems with bi-objective costs.

We propose coSST, the first probabilistically $\delta$-robustly complete and asymptotically near-optimal motion planner for constrained optimization of continuous dynamic systems, resolving the structural incompleteness of single-representative planners for this problem class.

We propose poSST, the first probabilistically $\delta$-robustly Pareto-complete and asymptotically near-Pareto-optimal motion planner for approximating the full Pareto front of kinodynamic systems with multiple objectives.

We validate these theoretical properties through extensive empirical evaluations, demonstrating the effectiveness and computational efficiency of our methods against scalarization-based baselines.

## Problem Formulation

We consider a robot with motion dynamics given: where $x\in\mathbb{X}\subseteq\mathbb{R}^{d}$ is the state, $u\in\mathbb{U}\subset\mathbb{R}^{m}$ is the control input, and $f:\mathbb{X}\times\mathbb{U}\to\mathbb{R}^{d}$ is the vector field. We assume that the dynamics satisfy standard smoothness and regularity conditions. Specifically, the second derivative of $x$ is uniformly bounded, i.e., $\|\ddot{x}\|\leq M$ for some constant $M\in\mathbb{R}_{\geq 0}$, and $f$ is Lipschitz continuous in both $x$ and $u$, i.e., for all $x,x^{\prime}\in\mathbb{X}$ and $u,u^{\prime}\in\mathbb{U}$, there exist $K_{x},K_{u}\geq 0$ such that The robot operates in a bounded workspace containing static obstacles and is subject to state constraints, such as velocity limits. We collectively represent these constraints as the obstacle set $\mathbb{X}_{O}\subset\mathbb{X}$ in the state space. The collision-free portion of the state space is then defined as $\mathbb{X}_{f}=\mathbb{X}\setminus\mathbb{X}_{O}$. In the classical kinodynamic motion planning problem, the aim is to find a robot trajectory from an initial state $x_{0}$ to a given goal region $\mathbb{X}_{G}\subseteq\mathbb{X}_{f}$ such that every state along the trajectory remains within $\mathbb{X}_{f}$.

### Definition 1 (Trajectory)

Given an initial state $x_{0}\in\mathbb{X}$ and control signal $U:[0,T]\rightarrow\mathbb{U}$, a robot trajectory $\pi:[0,T]\rightarrow\mathbb{X}$ is a continuous function such that $\pi(t)=x_{0}+\int_{0}^{T}f(\pi(\tau),U(\tau))d\tau$. A trajectory $\pi$ is *valid* if it remains entirely within the collision-free set, i.e., $\pi(t)\in\mathbb{X}_{f}$ for all $t\in[0,T].$ The set of all valid trajectories is denoted by $\Pi$.

### Definition 2 (Motion Plan)

A valid trajectory $\pi\in\Pi$ is called a *motion plan* if it begins at $x_{0}$ and reaches a given goal region $\mathbb{X}_{G}$, i.e., $\pi(t)\in\mathbb{X}_{G}$ for some $t\in[0,T]$. The set of all motion plans is denoted by $\Pi_{sol}$.

In this work, we consider settings in which the robot is subject to multiple motion-cost criteria. That is, each trajectory $\pi$ is evaluated using multiple cost functions, each capturing a different aspect of the trajectory's quality.

### Definition 3 (Cost Function)

A cost function $c:\Pi\rightarrow\mathbb{R}_{\geq 0}$ maps a trajectory $\pi$ to a non-negative scalar cost $c(\pi)\in\mathbb{R}_{\geq 0}$.

As , we assume each cost function is smooth, monotonic, and non-degenerate as formalized below.

### Assumption 1 (​​)

The cost function $c$ is *Lipschitz continuous*, i.e, there exists constant $K_{c}>0$ such that for all $\pi,\pi^{\prime}\in\Pi$ with the same start state, i.e., $\pi=\pi^{\prime}$. Furthermore, consider a trajectory $\pi\in\Pi$ with duration $T>0$, and for $t\in[0,T]$, define $\pi^{t}$ and $\pi_{t}$ as its *prefix* up to time $t$ and *suffix* from time $t$, respectively, so that their concatenation $\pi^{t}\cdot\pi_{t}=\pi$. Then, it holds that, for all $t\in[0,T]$: Given $N\in\mathbb{N}_{\geq 2}$ scalar cost functions ${c_{1},\ldots,c_{N}}$ that satisfy Assumption 1. ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), we aggregate them into a cost vector We are interested in high-quality motion plans that account for all pertinent cost metrics. This naturally motivates a multi-objective framework, in which we specifically focus on three problem classes: *lexicographic-optimal*, *constrained-optimal*, and *Pareto-optimal* planning.

### II-A Lexicographic-Optimal Motion Planning

Here, we assume that the ordering of a cost vector $C$ reflects the user-defined priorities among its components. Specifically, $c_{1}$ is prioritized over $c_{2}$, $c_{2}$ over $c_{3}$, and so . We formalize this prioritization using the notion of lexicographic dominance.

### Definition 4 (Lexicographic dominance)

Given valid trajectories $\pi,\pi^{\prime}\in\Pi$ with associated cost vectors $C(\pi),C(\pi^{\prime})\in\mathbb{R}^{N}_{\geq 0}$, then $\pi$ *lexicographically dominates* $\pi^{\prime}$, denoted $\pi\succ_{\text{lex}}\pi^{\prime}$, if there exists index $i\in\{1,\dots,N\}$ such that $c_{i}(\pi)<c_{i}(\pi^{\prime})$ and for all $j<i$, $c_{j}(\pi)=c_{j}(\pi^{\prime})$.

### Definition 5 (Lexicographic optimal plan)

A motion plan $\pi^{*}_{\text{lex}}\in\Pi_{\text{sol}}$ is *lexicographically optimal* if it is *not* lexicographically dominated by any other motion plan, i.e., $\nexists\pi^{\prime}\in\Pi_{\text{sol}}$ such that $\pi^{\prime}\succ_{\text{lex}}\pi$.

Intuitively, $\pi^{*}_{\text{lex}}$ is a motion plan that minimizes $c_{1}$ and, among those that do, minimizes $c_{2}$, and so . In Fig. 1(a), $\pi^{*}_{\text{lex}}$---which maximizes clearance ($c_{1}$), then path length ($c_{2}$)---is shown in light green, with its cost vector $C(\pi^{*}_{\text{lex}})$ marked as a red-outlined diamond in Fig. 1(b). Note that the blue trajectory (SST) minimizes $c_{1}$ but fails to refine $c_{2}$; as a result, it is lexicographically dominated by $\pi^{*}_{\text{lex}}$ (i.e., $\pi^{*}_{\text{lex}}\succ_{\text{lex}}\pi_{\text{{SST} }}$).

This motivates our first problem formulation.

### Problem 1 (Lexicographic-optimal motion planning)

Consider a robot with dynamics described , obstacle set $\mathbb{X}_{O}\subset\mathbb{X}$, an initial state $x_{0}\in\mathbb{X}_{f}=\mathbb{X}\setminus\mathbb{X}_{O}$, and a goal region $\mathbb{X}_{G}\subseteq\mathbb{X}_{f}$. Given a prioritized vector of cost functions $C=(c_{1},\ldots,c_{N})$, each satisfying Assumption 1. ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), compute a lexicographic-optimal motion plan $\pi^{*}_{\text{lex}}\in\Pi_{\text{sol}}$.

### II-B Constrained-Optimal Motion Planning

In the second setting, we consider a constrained optimization problem. That is, we assume user-defined upper bounds on $N-1$ costs, and our goal is to minimize the last one.

### Problem 2 (Constrained-Optimal Motion Planning)

Consider the setting described in Problem 1. ‣ II-A Lexicographic-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"). Given $N$ cost functions $c_{1},\dots,c_{N}$, each satisfying Assumption 1. ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), and $N-1$ cost upper-bounds $\bar{c}_{1},\dots,\bar{c}_{N-1}\in\mathbb{R}^{N-1}_{\geq 0}$, compute an optimal motion plan $\pi^{*}_{\text{co}}=\arg\min_{\pi\in\Pi_{\text{sol}}}c_{N}(\pi)$ subject to $c_{i}(\pi^{*})\leq\bar{c}_{i}$ for all $i\in\{1,\ldots,N-1\}$.

In the bi-objective setting shown in Fig. 1, an upper bound $\bar{c}_{1}=94$ is imposed. The solution to Problem 2. ‣ II-B Constrained-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality") is then the trajectory whose cost lies at the intersection of the constraint boundary $\bar{c}_{1}=94$ (red) and the true Pareto front (black).

### II-C Pareto-Optimal Motion Planning

Lastly, we consider the setting in which no prioritization or constraints are imposed. Instead, the goal is to find a *set* of motion plans that simultaneously optimize all objectives. Since costs are often competing --- e.g., minimizing path length may reduce obstacle clearance --- no single trajectory can, in general, optimize every objective. The goal, then, is to characterize the trade-offs among objectives by identifying the set of Pareto-optimal solutions. We formalize this using the notion of dominance.

### Definition 6 (Trajectory dominance)

A valid trajectory $\pi\in\Pi$ is said to dominate another trajectory $\pi^{\prime}\in\Pi$, denoted $\pi\succ\pi^{\prime}$, iff, for every $i\in\{1,\ldots,N\}$, it holds that $c_{i}(\pi)<c_{i}(\pi^{\prime})$.

We extend the notion of dominance to cost vectors : $C(\pi)\succ C(\pi^{\prime})\iff\pi\succ\pi^{\prime}$.

### Definition 7 (Pareto optimal & Pareto front)

A motion plan $\pi^{*}\in\Pi_{\text{sol}}$ is called *Pareto optimal* if it is not dominated by any other motion plan, i.e., $\nexists\pi^{\prime}\in\Pi_{\text{sol}}$ s.t. $\pi^{\prime}\succ\pi^{*}$. The set of all Pareto optimal motion plans is denoted by $\Pi_{\text{sol}}^{*}\subseteq\Pi_{\text{sol}}$. The set of cost vectors corresponding to all Pareto-optimal solutions $\mathcal{C}^{*}$ is called the *Pareto front*, i.e., In Fig. 1(a), samples of Pareto-optimal trajectories are shown using a purple-green color scale. Their corresponding cost vectors, $C(\pi^{*})\in\mathcal{C}^{*}$, are shown as diamonds in Fig. 1(b).

A Pareto front captures all possible optimal trade-offs among the cost objectives. For a designer, it is valuable to understand the range of optimal choices and the motion plans that realize them. We formalize the problem as follows.

### Problem 3 (Pareto-Optimal Motion Planning)

Consider the setting in Problem 1. ‣ II-A Lexicographic-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"). Compute the Pareto front $\mathcal{C}^{*}$ and the corresponding set of Pareto-optimal motion plans $\Pi_{\text{sol}}^{*}$.

### Approach Overview

Problems 1. ‣ II-A Lexicographic-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")-3. ‣ II-C Pareto-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality") are multi-objective optimization problems subject to nonlinear kinodynamic constraints; hence, they are nonconvex and difficult to solve. Even in the single-objective setting, kinodynamic motion planning is challenging as it requires searching both the state space for feasible trajectories and the objective space for cost improvements. In particular, computing a truly optimal motion plan is intractable, since even small perturbations to a candidate trajectory can yield strict improvements.

State-of-the-art planners (e.g., ) mitigate this by introducing sparsity into the search, retaining only trajectories that differ sufficiently in cost or state, while relying on sampling and forward propagation to handle kinodynamic constraints. This relaxes the problem to finding near-optimal solutions with suboptimality bounded by a user-defined sparsity metric.

We extend these ideas to the multi-objective cases for Problems 1. ‣ II-A Lexicographic-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")-3. ‣ II-C Pareto-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), by guaranteeing that near-optimal solutions are found with respect to the Pareto-point(s) of interest. For Problem 3. ‣ II-C Pareto-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), we approximate the entire Pareto front with arbitrarily tight bounds, enabling accurate representation of any desired trade-off among objectives.

## Preliminaries

We begin by reviewing the Stable Sparse-RRT (SST) algorithm, which forms the foundation for our proposed algorithms. We then highlight the fundamental limitations of reducing multi-objective optimization to a single-objective problem through cost scalarization, as commonly adopted in the literature.

### III-A Stable Sparse RRT (SST)

SST is a sampling-based kinodynamic planner that achieves asymptotic near-optimality for a single objective (cost) by growing a sparse motion tree in the state space $\mathbb{X}$ with cost-informed selection and pruning. Like RRT-based planners, it iteratively selects a node, propagates it forward under randomized controls, and adds a new state if feasible. To guide the search, SST samples a random state in $\mathbb{X}$ and selects the best-cost node (state) within a radius of $\delta_{\text{BN}}>0$ for extension. In addition, SST employs witness nodes: each defining a neighborhood (hyper-ball) of radius $\delta_{s}>0$ centered at $x\in\mathbb{X}$ (denoted by $\mathcal{B}_{\delta_{s}}(x)=\{x^{\prime}\in\mathbb{X}\mid\|x^{\prime}-x\|\leq\delta_{s}\}$), and represented by the lowest-cost node within that ball. A new state becomes a representative if it improves upon the cost of an existing representative, or if it lies outside all existing neighborhoods and creates a new one. This process ensures sparsity while monotonically improving trajectories toward low-cost solutions.

Due to the sparsity of the search tree, SST can only probabilistically guarantee the generation of a motion plan that is $\delta$-similar to an optimal solution $\pi^{*}$.

### Definition 8 ($\delta$-Similar trajectories)

Two trajectories $\pi,\pi^{\prime}\in\Pi$ with time durations $T_{\pi}$ and $T_{\pi^{\prime}}$, respectively, are *$\delta$-similar* if, for a continuous, non-decreasing scaling function $\sigma:[0,T_{\pi}]\rightarrow[0,T_{\pi^{\prime}}]$, it is true that $\pi^{\prime}(\sigma(t))\in\mathcal{B}_{\delta}(\pi(t))$.

The *obstacle clearance* of a valid trajectory $\pi\in\Pi$ is the minimum distance from $\pi$ to the obstacle set $X_{O}$. The *dynamic clearance* of $\pi$ is the maximum distance $\delta_{d}$ that the start and end points of $\pi$ can be displaced such that a new, $\delta_{d}$-similar trajectory is feasible according to the dynamics in (see Definition 4 and Lemma 6 in for details). A trajectory is called $\delta$-robust if both its obstacle and dynamic clearances exceed $\delta$.

Consequently, SST ensures the approximation of $\delta$-robust solutions and is therefore probabilistically $\delta$-robustly complete and asymptotically $\delta$-robustly near-optimal, as defined below.

### Definition 9 (Probabilistic $\delta$-Robust Completeness)

Let $\Pi_{n}^{\textsc{alg}}$ denote the set of trajectories discovered by an algorithm alg at iteration $n$. Algorithm alg is probabilistically $\delta$-robustly complete if, for every motion planning problem where there exists at least one $\delta$-robust solution trajectory, the following holds for all independent runs:

### Definition 10 (Asymptotic $\delta$-robust Near-Optimality)

Consider a motion planning problem with a single cost and assume there exists at least one $\delta$-robust motion plan. Denote by $c_{\delta}^{*}$ the minimum achievable cost over all $\delta$-robust solution trajectories, and let $Y_{n}^{\textsc{alg}}$ denote a random variable representing the minimum cost among all trajectories returned by algorithm alg after iteration $n$. The algorithm alg is *asymptotically $\delta$-robustly near-optimal* if for all independent runs: where $h:\mathbb{R}_{\geq 0}\times\mathbb{R}_{\geq 0}\rightarrow\mathbb{R}_{\geq 0}$ is a function of the optimum cost $c_{\delta}^{*}$ and the $\delta$ clearance such that $h(c_{\delta}^{*},\delta)\geq c_{\delta}^{*}$.

The probabilistic completeness and near-optimality analyses of our algorithms build on these properties of SST, extending them to the multi-cost setting. In Section VII, we show that our approach maintains the ability to find $\delta$-similar trajectories to any $\delta$-robust solution of interest, which, most generally, includes all non-dominated (Pareto-optimal) solutions.

### III-B Scalarized Cost Function

A common approach to multi-objective optimization is to aggregate multiple costs into a single scalar objective, thereby enabling the use of standard cost-aware planners (e.g., SST). In this subsection, we briefly review two common scalarization methods, namely, *weighted sum* (WS) and *weighted maximum* (WM), and explain why they fail to address Problems 2. ‣ II-B Constrained-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality") and 3. ‣ II-C Pareto-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"). Further, in Section IV-A, we show that no scalarization method can recover the lexicographic minimum in continuous domains, making them unsuitable for Problem 1. ‣ II-A Lexicographic-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality").

### III-B1 Weighted-Sum (WS) Scalarization

The most common scalarization is the weighted sum, where the quality of a trajectory $\pi$ is described by a scalar cost where weights $w_{i}$ encode the relative importance of objectives.

Minimizing $c_{\text{ws}}$ produces a single Pareto-optimal trade-off, $\pi^{*}=\arg\min_{\pi\in\Pi_{\text{sol}}}c_{\text{ws}}(\pi)$. However, because this scalarization is a linear combination of objectives, it can only recover Pareto points lying on the convex hull of the Pareto front. Consequently, WS minimization cannot capture non-convex Pareto points and is thus incomplete for Problems 2. ‣ II-B Constrained-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality") and 3. ‣ II-C Pareto-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality").

### III-B2 Weighted-Maximum (WM) Scalarization

An alternative approach is the WM scalarization, which substitutes the summation of WS with a maximization operator, While WM avoids the convexity limitations of weighted sums, it still yields only a single Pareto point for each weight selection. For Problem 2. ‣ II-B Constrained-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), although suitable weights may exist to target a particular Pareto point (i.e., $\pi^{*}_{\text{co}}$), determining them a priori is generally not possible. For Problem 3. ‣ II-C Pareto-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), computing the full Pareto set would require repeatedly reinitializing a planner with different weights and then solving multiple independent planning problems. In contrast, our approach maintains and refines non-dominated trajectories within a single search tree, enabling simultaneous approximation of the entire Pareto set.

## Lexicographic-Optimal Motion Planning

In this section, we present our approach to Problem 1. ‣ II-A Lexicographic-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"). We first show that a lexicographic ordering relation cannot be captured by any cost scalarization, then introduce a method to approximate the lexicographic-optimal solution with bounded error in bi-objective settings. In Section VI, we extend this approach to address $N$-dimensional cost spaces.

### IV-A Limitations of Extending Lexicographic Ordering to Continuous Domains

When costs are limited to *integers*, i.e., vector $C(\pi)\in\mathbb{N}^{N}$, lexicographic ordering can be neatly captured by a utility function that assigns a unique scalar value to each cost vector according to a fixed priority among dimensions. Specifically, for a set of cost vectors $\mathcal{C}=\{C_{1},C_{2},\dots,C_{N}\}$ with each $C_{i}\in\mathbb{N}^{N}$, a lexicographic dominance relation $\succ_{\text{lex}}$ can be encoded using a utility function $u:\mathbb{N}^{N}\to\mathbb{R}$ that respects the ordering, i.e., $C\succ_{\text{lex}}C^{\prime}\iff u(C)>u(C^{\prime})$.

A simple construction can exploit the discreteness of the domain (i.e., $\mathbb{N}$) of each cost component by assigning strictly decreasing scaling coefficients, so that any unit improvement in a higher-priority dimension outweighs the maximum possible variation across all lower-priority dimensions. Thus, the first component determines the primary ordering, the second breaks ties, and so. For example, for a weight $M\geq\max_{\pi\in\Pi_{\text{sol}}}\|C(\pi)\|_{\infty}$, the utility function ensures lexicographic ordering. However, when costs are defined in *continuous domains*, i.e., $C(\pi)\in\mathbb{R}^{N}$, which is the case in this work, lexicographic ordering $\succ_{\text{lex}}$ can *not* be represented by any utility function $u:\mathbb{R}^{N}\to\mathbb{R}$. The following theorem formalizes this limitation:

### Theorem 1

There does *not* exist a utility function $u:\mathbb{R}^{N}\rightarrow\mathbb{R}$ that represents the lexicographic dominance $\succ_{\text{lex}}$, i.e., $\nexists u$ s.t., for every $C,C^{\prime}\in\mathbb{R}^{N}_{\geq 0}$, $C\succ_{\text{lex}}C^{\prime}\iff u(C)>u(C^{\prime})$.

The proof is provided in Appendix -A. Intuitively, it relies on the fact that a real-valued utility function has insufficient "bandwidth" to encode any more than one continuous cost component. To faithfully capture lexicographic ordering, the utility must dedicate every element of its range to resolving differences in the first cost (i.e., $c_{1}$); then, no values would be available to encode secondary considerations in $c_{2}$, and so .

### Corollary 1

There do not exist weights $w_{1},\ldots,w_{N}\in\mathbb{R}_{\geq 0}$ such that the minimization of the weighted-sum cost $c_{\text{ws}}$ in (2 Scalarization ‣ III-B Scalarized Cost Function ‣ III Preliminaries ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")) or the weighted-max cost $c_{\text{wm}}$ in (3 Scalarization ‣ III-B Scalarized Cost Function ‣ III Preliminaries ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")) guarantees the lexicographically optimal solution $\pi^{*}_{\text{lex}}$.

This result implies that Problem 1. ‣ II-A Lexicographic-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality") cannot be solved by any scalarization method (e.g., WS and WM). Additionally, algorithmic approaches that rely on scalar cost metrics (e.g., SST) or optimization methods that use smooth or continuous utility functions cannot properly model lexicographic objectives. Our proposed solution, detailed below, retains information about the entire cost vector and can therefore explicitly handle the desired preference structure.

### IV-B $\epsilon$-Equivalence for Lexicographic Minimization in $\mathbb{R}^{N}$

Before presenting our approach, we first argue that, given the nature of sampling-based methods, a strict notion of lexicographic dominance is unsuitable; instead, we introduce a notion of $\epsilon$-equivalence, formalized below.

When sampling from a continuous control space and integrating the dynamics , the likelihood of obtaining two trajectories $\pi$ and $\pi^{\prime}$ that yield identical costs $c_{i}(\pi)=c_{i}(\pi^{\prime})$ is vanishingly small. Consequently, lexicographic dominance effectively reduces to a scalar comparison on the highest-priority cost $c_{1}$, precluding meaningful consideration of lower-priority costs.

To overcome this, we introduce the notion of $\epsilon$-equivalence, wherein cost components that differ by less than an $\epsilon>0$ tolerance are treated as "equivalent". Specifically, let $\Pi^{\epsilon}_{0}\subseteq\Pi_{\text{sol}}$ be a set of non-dominated trajectories, and let the minimum primary cost in this set be denoted by $\hat{c}^{*}_{1}=\min_{\pi\in\Pi^{\epsilon}_{0}}c_{1}(\pi)$. We first construct a set of $\epsilon$-equivalent trajectories in $c_{1}$ as Then, we can approximate $\pi^{*}_{\text{lex}}$ by finding the minimum secondary cost within this set, i.e., $\pi^{\epsilon}_{\text{lex}}=\min_{\pi\in\Pi^{\epsilon}_{1}}c_{2}(\pi)$.

This procedure can be recursively applied for $N>2$ objectives such that $\Pi^{\epsilon}_{i}=\{\pi\in\Pi^{\epsilon}_{i-1}\mid c_{i}(\pi)\leq\hat{c}^{*}_{i}+\epsilon_{i}\}$, and the lexicographic $\epsilon$-optimal trajectory computed by We refer to $\Pi^{\epsilon}_{N-1}$ as the $\epsilon$-minimal set.

We now examine the properties of using $\epsilon$-equivalence in bi-objective settings and its limitations for systems with $N>2$ objectives.

### IV-B1 Case of $N=2$

Fig. 2: Approximating πlex* using ϵ-equivalence when N = 2.

Consider a 2D Pareto front as illustrated in Fig. 2. Let point $A$ represent the cost of a solution trajectory $\pi_{A}$ whose first cost component $c_{1}(\pi_{A})$ achieves the global minimum $c_{1}^{*}$, but whose secondary cost $c_{2}(\pi_{A})$ is significantly suboptimal. Let point $L$ denote the cost of the lexicographic optimum $\pi_{L}=\pi^{*}_{\text{lex}}$.

Assume a motion planner finds solutions $\hat{\pi}_{A}$ and $\hat{\pi}_{L}$ that approximate $\pi_{A}$ and $\pi_{L}$ arbitrarily closely. Then, $\hat{\pi}_{L}$ may not strictly dominate $\hat{\pi}_{A}$, but rather satisfy $c_{1}(\hat{\pi}_{L})\in[c_{1}^{*},c_{1}^{*}+\epsilon_{1}]$. Consequently, $\hat{\pi}_{L}$ is guaranteed to be included in the (first-stage) $\epsilon$-equivalent set $\Pi^{\epsilon}_{1}$, and minimizing $c_{2}$ over $\Pi^{\epsilon}_{1}$ will ensure a trajectory $\pi^{\epsilon}_{\text{lex}}$ that lies in the green region (Fig. 2).

Therefore, for a algorithm that can approximate a solution trajectory $\pi\in\Pi_{\text{sol}}$ with bounded (cost) error this approach yields a solution with error $\vec{e}_{\text{lex}}=\vec{e}_{\textsc{alg}}+(\epsilon_{1},0)$ from the true lexicographic optimal. Clearly, as $\epsilon_{1}\to 0$, $\vec{e}_{\text{lex}}\to\vec{e}_{\textsc{alg}}$ monotonically.

### IV-B2 Case of $N>2$

Now consider a 3D Pareto front, as shown in Fig. 3, where each point on the surface corresponds to a cost vector of a Pareto-optimal trajectory. Using the same procedure, we construct $\Pi^{\epsilon}_{1}$ by including all solutions with $c_{1}<c_{1}^{*}+\epsilon_{1}$, visualized as a half-space bounded by the orange plane in Fig. 3(a). Within this set, we compute $\hat{c}_{2}^{*}$, the best observed secondary cost (located at point $B$), and form $\Pi^{\epsilon}_{2}$ by retaining only those elements with $c_{2}<\hat{c}_{2}^{*}+\epsilon_{2}$, represented by the green plane.

Fig. 3: Example in which ϵ-equivalence fails to capture a bound on the true lexicographic optimum (point L). (a) Pareto front for three cost objectives. Half-space partitions representing filtering at Π1ϵ (orange) and Π2ϵ (green). (b) Projection onto the c1-c2 plane. (c) Projection onto the c2-c3 plane.

Crucially, because $\hat{c}_{2}^{*}$ may be less than $c_{2}(\pi^{*}_{\text{lex}})$ (i.e., point $c_{2}(B)<c_{2}(L)$), the second filtering step may discard the true lexicographic optimal point altogether (Fig. 3b). Consequently, the final set used to minimize $c_{3}$ may not include $\pi^{*}_{\text{lex}}$, and the resulting solution $\pi^{\epsilon}_{\text{lex}}$ may have an arbitrarily poor $c_{3}$ cost (point D, Fig. 3c). That is, $|c_{3}(\pi^{\epsilon}_{\text{lex}})-c_{3}(\pi^{*}_{\text{lex}})|\in0,\infty).$ The source of this failure lies in the compounded filtering: once $\pi^{*}_{\text{lex}}$ is excluded at any intermediate step $i$, it can no longer influence the minimization of subsequent cost components $c_{i+1},\dots,c_{N}$. Thus, while $\epsilon$-equivalence offers a practical heuristic, it fails to guarantee bounded approximation error for problems with more than two objectives. Nevertheless, our approach for approximating the full Pareto set $\Pi_{\text{sol}}^{*}$ (detailed in Section [VI) can recover a near-optimal solution with respect to the true lexicographic optimal, since, by definition, it is a Pareto-optimal solution (i.e., $\pi^{*}_{\text{lex}}\in\Pi_{\text{sol}}^{*}$).

### IV-C lexSST

Having clarified these nuances of lexicographic optimization in continuous cost spaces, we now introduce our approach to Problem 1. ‣ II-A Lexicographic-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), lexicographic SST (lexSST). lexSST is an adaptation of SST, in that the algorithm iteratively grows a search tree $G=(V,E)$ and uses a set of witness nodes $S\subseteq V$ to define local neighborhoods $\mathcal{B}_{\delta_{s}}(s)$ about every $s\in S$ (refer to Section III-A ‣ III Preliminaries ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")). However, instead of each witness maintaining a single representative (lowest cost) node, lexSST maintains a representative set $R_{s}$ of viable candidates in $\mathcal{B}_{\delta_{s}}(s)$. Our main contribution is the extension from a single representative in the single-cost case to a representative set in the multi-objective setting. All our proposed algorithms --- lexSST, coSST, and poSST --- leverage this structure to solve their respective problems and differ only in their definitions of $R_{s}$.

In each case, the representative set begins by considering non-dominated nodes at witness $s$. We define the local Pareto set of nodes within neighborhood $\mathcal{B}_{\delta_{s}}(s)$ as, For lexSST, we define the representative set as $R^{\text{lex}}_{s}:=L^{\epsilon}(V^{\text{PO}}_{\mathcal{B}_{s}})$, where $L^{\epsilon}(\cdot)$ returns the $\epsilon$-minimal set of nodes according to the procedure described in Section IV-B.

1 $\Pi^{\textsc{alg}}_{\text{sol}}\leftarrow\emptyset$; 5 $x_{selected}\leftarrow\textsc{ParetoSelect}(\mathbb{X},V,\delta_{\text{PS}})$; 6 $x_{new}\leftarrow\textsc{MonteCarloProp}(x_{selected},\mathbb{U},T_{prop})$; 7 if $\textsc{CollisionFree}(\overline{x_{selected}\rightarrow x_{new}})$ then 8 $s\leftarrow\textsc{NearestWitness}(x_{new},S,\delta_{s})$; 10 $s.R\leftarrow\textsc{PruneLexSet}(s.R\cup\{x_{new}\})$; 11 $s.R\leftarrow\textsc{PruneDominated}(s.R)$; 13 $\textsc{AddNewNode}(x_{new},x_{selected},G,\Pi^{\textsc{alg}}_{\text{sol}})$ 15 snew ← xnew, snew.R = {xnew}; 17 $\textsc{AddNewNode}(x_{new},G,\Pi^{\textsc{alg}}_{\text{sol}})$ 18 $\pi^{\epsilon}_{\text{lex}}\leftarrow\arg\min_{\pi\in\Pi^{\textsc{alg}}_{\text{sol}}}c_{N}(\pi)$; We detail lexSST in Algorithm 1, where $\overline{x\rightarrow x^{\prime}}$ denotes the tree branch (trajectory) that connects node (state) $x$ to $x^{\prime}$. The algorithm begins by initializing the vertex $V$, edge $E$, witness $S$, and solution $\Pi^{\textsc{alg}}_{\text{sol}}$ sets. At each iteration, a node is selected for extension using the ParetoSelect routine (Algorithm 2), which uniformly samples a non-dominated node within a ball of radius $\delta_{\text{PS}}$ centered at a randomly selected state $x_{rand}$ returned by RandomSample.

1 $x_{rand}\leftarrow\textsc{RandomSample}(\mathbb{X})$; 2 $X_{near}\leftarrow\textsc{Near}(x_{rand},V,\delta_{\text{PS}})$; 3 $X_{pareto}\leftarrow\textsc{PruneDominated}(X_{near})$; 4 $x_{selected}\leftarrow\textsc{RandomSample}(X_{pareto})$; Input: xselected, 𝕌, Tprop 1 $t_{prop}\leftarrow\textsc{Sample}([0,T_{prop}]);\ u\leftarrow\textsc{Sample}(\mathbb{U})$; 2 return xnew ← xselected + ∫0tpropf(x(t), u)dt; Once a node is selected, it is extended using MonteCarloProp (Algorithm 3), which samples a random control and duration to propagate $x_{\text{selected}}$ according to, yielding a new candidate state $x_{\text{new}}$. The nearest witness $s_{\text{near}}$ is then identified via NearestWitness: if $s_{\text{near}}$ lies farther than $\delta_{s}$ from $x_{\text{new}}$, a new witness is created and associated with $x_{\text{new}}$; otherwise, $x_{\text{new}}$ is evaluated against the current representative set of $s_{\text{near}}$.

If $x_{\text{new}}$ is not pruned by either PruneLexSet or PruneDominated (Algorithms 4 and 5, respectively), then it is added to $R^{\text{lex}}_{s_{\text{near}}}$ and the motion tree. As well, the new node may result in the pruning of existing nodes. Nodes entering the goal region are added to the solution set $\Pi^{\textsc{alg}}_{\text{sol}}$ (Algorithm 6).

6 Remove x from R and V; 3 if not ∃ x′ ∈ R such that C(x′) ≻ C(x) then 6 if not ∃ x′ ∈ VℬsPO s.t. |ci(x′) − ci(x)| < εi ∀i then Input: xnew, xselected, G, $\Pi^{\textsc{alg}}_{\text{sol}}$ 4 $\Pi^{\textsc{alg}}_{\text{sol}}\leftarrow\textsc{PruneLexSet}(\Pi^{\textsc{alg}}_{\text{sol}}\cup\{x_{new}\})$; 5 $\Pi^{\textsc{alg}}_{\text{sol}}\leftarrow\textsc{PruneDominated}(\Pi^{\textsc{alg}}_{\text{sol}})$; Since the number of non-dominated nodes, and thus active representatives, can grow without bound, we introduce a cost-space sparsity metric $\vec{\varepsilon}$. This metric ensures that each set $R_{s}$ retains only nodes that are sufficiently different in cost, i.e., As the algorithm progresses, the state-space sparsity metric $\delta_{s}$ (inherited from SST) ensures a finite number of neighborhoods $\mathcal{B}_{\delta_{s}}(s)$ are reached, while $\vec{\varepsilon}$ ensures a finite number of representatives within each neighborhood. In Section VII, we show that $\vec{\varepsilon}$ directly affects the near-optimality of our proposed algorithms, and in Sec. VIII, we empirically demonstrate the trade-off between sparsity and solution quality by varying $\vec{\varepsilon}$.

The algorithm continues for a fixed time budget, incrementally growing the motion tree $G$ and maintaining a set of candidate solution trajectories $\Pi^{\textsc{alg}}_{\text{sol}}$. Upon termination, it returns the solution that minimizes the final cost component $\pi^{\epsilon}_{\text{lex}}=\arg\min_{\pi\in\Pi^{\textsc{alg}}_{\text{sol}}}c_{N}(\pi)$.

## Constrained-Optimal Motion Planning

Here, we introduce our proposed algorithm, constrained-optimal SST (coSST), for solving Problem 2. ‣ II-B Constrained-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), with the goal of returning the trajectory that minimizes cost $c_{N}$ subject to $N-1$ constraints. Similar to lexSST, we define a representative set $R^{\text{co}}_{s}$ for each witness, but use a different pruning procedure to ensure efficient exploration while respecting the user-defined constraints $\bar{c}_{i}$.

Effectively, this replaces the shifting window of lexSST, retaining nodes with $c_{i}<\hat{c}_{i}^{*}+\epsilon_{i}$, with a static window keeping nodes with $c_{i}<\bar{c}_{i}+\bar{\epsilon}_{i}$. The buffer term $\bar{\epsilon}_{i}$ is introduced to ensure that a $\delta$-similar trajectory to the true solution $\pi^{*}_{\text{co}}$ is not pruned prematurely, as discussed in Section VII-C. Formally, we define the representative set as As with lexSST, $R^{\text{co}}_{s}$ only contains non-dominated nodes.

Intuitively, each witness neighborhood maintains a slice of its local Pareto front, defined by the intersection of half-spaces $c_{i}\leq\bar{c}_{i}+\bar{\epsilon}_{i}$ for cost dimensions $i\in\{1,\dots,N-1\}$. As the algorithm progresses, nodes are selected from $R^{\text{co}}_{s}$ for extension, ensuring all viable subtrajectories are maintained. Since costs are monotonic, we can safely prune nodes that exceed this threshold and focus our search on more promising ones. Further, if an admissible cost-to-go heuristic $g:\mathbb{X}\times 2^{\mathbb{X}}\rightarrow\mathbb{R}_{\geq 0}$ is available, this pruning can be made more aggressive by retaining nodes that satisfy $c_{i}(x)\leq\bar{c}_{i}+\bar{\epsilon}_{i}-g(x,\mathbb{X}_{G})$.

The algorithm for coSST follows that of Algorithm 1, except that we replace PruneLexSet in Line 10 with PruneCoSet (Algorithm 7). Upon termination, coSST returns the solution that minimizes the unconstrained cost, i.e., $\pi_{\text{co}}=\arg\min_{\pi\in\Pi^{\textsc{alg}}_{\text{sol}}}c_{N}(\pi)$.

### V-A Limitations of SST for Constrained Optimization

The solution to Problem 2. ‣ II-B Constrained-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality") involves minimizing a single cost while satisfying the remaining $N-1$ constraints, yielding an optimal trajectory $\pi^{*}_{\text{co}}$. Unlike lexicographic optimization, no $\epsilon$-equivalence is required for tie-breaking, which might suggest that vanilla SST is sufficient. However, we show that because SST maintains only a single representative per witness, it cannot account for downstream constraint satisfaction and is therefore *incomplete* for Problem 2. ‣ II-B Constrained-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality").

Consider the flytrap example in Fig. 4, where the agent must navigate from the start (yellow star) to the goal (red region) via a narrow passage. The goal is to minimize path length while satisfying a constraint on the line integral over a cost function shown in greyscale, i.e., $c_{1}(\pi)=\int_{\pi}\mathcal{N}(y)dy$, where $\mathcal{N}(y)$ is a Gaussian function evaluated at state $y$, and $c_{2}(\pi)=\int_{\pi}dy$.

The narrow passage can accommodate only a few witnesses through which all candidate solutions must pass. Now, consider three subtrajectories $\pi_{a},\pi_{b},$ and $\pi_{c}$ that arrive at witness $s$. Naively applying SST to optimize for path length ($c_{2}$) while pruning $c_{1}\leq\bar{c}_{1}$ would select $x_{b}$ as the representative of $s$, even if it nearly exceeds $\bar{c}_{1}$. Then, nodes $x_{a}$ and $x_{c}$ are pruned since they do not improve upon $c_{2}$. However, the minimum cost-to-go from $x_{b}$ may exceed the cost threshold (i.e., $c_{1}(\pi_{B})>\bar{c}_{1}$), rendering SST incomplete for Problem 2. ‣ II-B Constrained-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"). Nearby witnesses would exhibit similar behavior, as the shortest path to any witness in the passage would pass through the high-cost region. In Section VIII-C, we demonstrate this limitation empirically.

Fig. 4: Flytrap example showing the limitation of SST in minimizing PathLength given a constraint on GaussianCost.

In contrast, conSST maintains all nodes that respect the cost constraints in each neighborhood. Therefore, $x_{a},x_{b},$ and $x_{c}$ are maintained in $R^{\text{co}}_{s}$, allowing the algorithm to select and extend each node with positive probability until a near-optimal motion plan is found (i.e., trajectory $\pi^{*}_{C}$). In Section VII, we prove that conSST is asymptotically near-optimal.

## Pareto-Optimal Motion Planning

Lastly, we present Pareto-optimal SST (poSST), a kinodynamic sampling-based motion planner that approximates the entire Pareto front of solution trajectories with arbitrarily tight error bounds, thereby solving Problem 3. ‣ II-C Pareto-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"). This algorithm closely mirrors the structure of lexSST and coSST but employs fewer pruning operations, thereby exploring a broader set of cost trade-offs.

Specifically, poSST retains Pareto-optimal candidates per neighborhood (every node when $\vec{\varepsilon}=0$, otherwise a sparse subset). This can be interpreted as initializing coSST with constraints $\bar{c}_{i}=\infty$ for all $i$, allowing the algorithm to explore the full extent of the Pareto front. Consequently, the representative set for poSST is simply $R^{\text{PO}}_{s}:=V^{\text{PO}}_{\mathcal{B}_{s}}$, as no additional filters are applied. Upon termination, poSST returns a set of trajectories $\Pi^{\textsc{alg}}_{\text{sol}}$ rather than a single solution.

Due to this broader search scope, poSST converges more slowly than lexSST and coSST, especially in high-dimensional cost spaces. However, it guarantees that all trade-offs among objectives are represented in the output, making it suitable for applications where post-hoc preference elicitation is necessary.

## Analysis

Here, we analyze the theoretical properties of our proposed algorithms, focusing on probabilistic completeness and near-optimality guarantees. For clarity, we first prove these properties for poSST, then show how the additional pruning procedures employed by lexSST and coSST preserve them within their respective problem classes. All the proofs are provided in the appendix.

We first extend the notions of probabilistic $\delta$-robust completeness (Def. 9. ‣ III-A Stable Sparse RRT (SST) ‣ III Preliminaries ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")) and asymptotic $\delta$-robust near-optimality (Def. 10. ‣ III-A Stable Sparse RRT (SST) ‣ III Preliminaries ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")) from to the multi-objective setting. When targeting a single solution, as in lexSST and coSST, Defs. 9. ‣ III-A Stable Sparse RRT (SST) ‣ III Preliminaries ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")-10. ‣ III-A Stable Sparse RRT (SST) ‣ III Preliminaries ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality") apply with slight alterations. For poSST, which must approximate the entire Pareto front, we introduce analogous definitions that generalize these requirements to hold simultaneously across all Pareto-optimal solutions.

### Definition 11 (Probabilistic $\delta$-Robust Pareto-Completeness)

Let $\Pi^{\textsc{alg}}_{\text{sol}}$ denote the set of trajectories computed by algorithm alg at iteration $n$. Algorithm alg is probabilistically $\delta$-robustly Pareto-complete if, for every motion planning problem admitting a non-empty set of $\delta$-robust Pareto-optimal solutions $\Pi^{*}_{\delta,\text{sol}}$, the following holds for each independent run: Given an algorithm with this property and the Lipschitz continuity of the cost functions (Assumption 1. ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")), we can ensure that any Pareto-optimal trajectory in $\Pi^{*}_{\delta,\text{sol}}$ can be approximated, yielding the following notion of near-optimality.

### Definition 12 (Asymptotic $\delta$-Robust Near-Pareto-Optimality)

Consider a motion-planning problem that admits at least one $\delta$-robust motion plan. Let $\mathcal{C}^{*}_{\delta}=\{C(\pi^{*})\mid\pi^{*}\in\Pi^{*}_{\delta,\text{sol}}\}$ denote the set of cost vectors of all $\delta$-robust Pareto-optimal trajectories, and let $\mathcal{Y}_{n}^{\textsc{alg}}$ denote a random variable representing the set of cost vectors $\mathcal{C}=\{C(\pi)\mid\pi\in\Pi^{\textsc{alg}}_{\text{sol}}\}$ returned by algorithm alg after iteration $n$. Algorithm alg is *asymptotically $\delta$-robustly near-Pareto-optimal* if for each independent run: where $H:\mathbb{R}^{n}_{\geq 0}\times\mathbb{R}^{n}_{\geq 0}\times\mathbb{R}_{\geq 0}\rightarrow\mathbb{R}^{n}_{\geq 0}$ bounds the sub-optimality of alg as a function of an optimum cost $C^{*}$ and the user-defined sparsity parameters. Note that $H(C^{*},\vec{\varepsilon},\delta)\to C^{*}$ as $\delta\to 0$ and $\vec{\varepsilon}\to 0$.

### VII-A Analysis of poSST

Here, we show that the pruning and selection procedures of poSST preserve the ability to generate a $\delta$-similar trajectory to any $\delta$-robust, Pareto-optimal solution $\pi^{*}\in\Pi^{*}_{\delta,\text{sol}}$, from which completeness and near-optimality follow. We begin by recalling three results . First, we relate the user-defined parameters $\delta_{\text{PS}}$ and $\delta_{s}$ to the dynamic clearance $\delta$.

### Proposition 1 (​\[17, Prop. 13\])

The parameters $\delta_{\text{PS}}$ and $\delta_{s}$ must satisfy the following relationship with $\delta$ for a $\delta$-robust feasible motion planning problem to be solved: Next, we characterize $\delta$-similarity by defining a covering ball sequence, adapted, over each $\pi^{*}\in\Pi^{*}_{\delta,\text{sol}}$.

### Definition 13 (Covering Balls)

Given a trajectory $\pi^{*}$, a dynamic clearance $\delta>0$, and a cost increment $\Delta c_{1}\in\mathbb{R}_{>0}$, the covering ball sequence $\mathbb{B}(\pi^{*},\delta,\Delta c_{1})$ is a set of $M+1$ hyper-balls where each $x^{*}_{i}$ lies along $\pi^{*}$ and satisfies $\Delta c_{1}=c_{1}(\overline{x^{*}_{j}\rightarrow x^{*}_{j+1}})$ for all $j\in\{0,1,\dots,M-1\}$.

Without loss of generality, we partition a reference trajectory $\pi^{*}$ according to its primary cost $c_{1}$, resulting in $k=\frac{c_{1}(\pi^{*})}{\Delta c_{1}}$ segments. A trajectory is $\delta$-similar to $\pi^{*}$ if and only if it remains entirely within this sequence.

Lastly, because MonteCarloProp (Algorithm 3) samples controls with full support over $\mathbb{U}$, it can produce a control arbitrarily close to that of $\pi^{*}$, ensuring a positive probability of transitioning from one ball to the next \[17, Theorem 17\]. Since poSST is initialized at $x_{0}=\pi^{*}\in\mathcal{B}_{\delta}(x^{*}_{0})$ for all $\pi^{*}\in\Pi^{*}_{\delta,\text{sol}}$ (i.e., all solutions begin at $x_{0}$), a $\delta$-similar trajectory to any Pareto-optimal reference can therefore be generated, provided that nodes within its covering ball sequence have a positive probability of selection at each iteration. It thus remains to show that the subroutines ParetoSelect and PruneDominated preserve this selection property.

### VII-A1 Properties of ParetoSelect

We first analyze ParetoSelect (Algorithm 2), which biases node selection toward locally non-dominated solutions, thereby accelerating convergence relative to simple nearest-neighbor selection.

At each iteration, a random state $x_{\text{rand}}\sim\mathcal{U}(\mathbb{X})$ is sampled from a uniform distribution over $\mathbb{X}$. Then, all active nodes within a ball $\mathcal{B}_{\delta_{\text{PS}}}(x_{\text{rand}})$ are retrieved. The subset of these nodes that are not dominated by any other node in the set (with respect to all cost objectives) forms a local Pareto front. Finally, a random node $x_{\text{selected}}$ is chosen uniformly from this set for propagation.

### Lemma 1

Assume $x_{\text{rand}}\sim\mathcal{U}(\mathbb{X})$. If there exists a node $x\in\mathcal{B}_{\delta_{\text{PS}}}(x^{*}_{i})$ at some iteration $n$, where $x^{*}_{i}$ corresponds to a state along a $\delta$-robust reference trajectory $\pi^{*}$, then the probability that ParetoSelect chooses a node $x^{\prime}\in\mathcal{B}_{\delta}(x^{*}_{i})$ for propagation is lower bounded by a positive constant $\gamma>0$ for all iterations $n^{\prime}>n$.

The proof for Lemma 1 can be found in Appendix -B.

While ParetoSelect ensures that locally non-dominated nodes are considered for propagation with positive probability, this alone does not guarantee efficient exploration of the Pareto-optimal set. The local Pareto front may be arbitrarily dense, and uniform sampling from it may not promote diversity among the generated trajectories. We address this redundancy by actively managing the search tree using the pruning procedure discussed next.

### VII-A2 Properties of PruneDominated

The PruneDominated procedure (Algorithm 5) is used by poSST to retain only non-dominated candidate nodes at every witness neighborhood. Further, this procedure involves a sparsity parameter $\vec{\varepsilon}$ that ensures only one node is retained within a region of the objective space. Then, we bound the worst-case deviation from a reference trajectory $\pi^{*}$ that can result from applying PruneDominated.

### Lemma 2

Let $\delta_{c}=\delta_{\text{PS}}-2\delta_{s}$. If a state $x\in V$ is generated at iteration $n$ such that $x\in\mathcal{B}_{\delta_{c}}(x^{*}_{i})$, then for every iteration $n^{\prime}>n$, there exists a state $x^{\prime}\in V$ such that $x^{\prime}\in\mathcal{B}_{\delta-\delta_{\text{PS}}}(x^{*}_{i})$ and $C(x^{\prime})\succeq C(x)+\vec{\varepsilon}$.

### Lemma 3

Assuming uniform sampling of the state space in ParetoSelect, if there exists a node $x\in V$ such that $x\in\mathcal{B}_{\delta_{c}}(x^{*}_{i})$ at iteration $n$, then the probability that ParetoSelect chooses a node $x^{\prime}\in\mathcal{B}_{\delta}(x^{*}_{i})$ is lower bounded by a positive constant $\gamma_{\text{PS}}>0$ for all iterations $n^{\prime}>n$.

Proofs are included in Appendices -C and -D. From this result, the following is immediate.

### Theorem 2 (Completeness of poSST)

poSST is probabilistically $\delta$-robustly Pareto-complete.

### VII-A3 Near-optimality of poSST

We now derive a formal bound on the worst-case performance of poSST in approximating any Pareto-optimal trajectory. Building on the result that poSST can generate a $\delta$-similar trajectory to any reference trajectory $\pi^{*}\in\Pi^{*}_{\delta,\text{sol}}$, we analyze how this deviation in the state space translates into sub-optimality in the multi-objective cost space.

Let $\mathbf{K}_{c}=(K_{c,1},\dots,K_{c,N})\in\mathbb{R}^{N}_{\geq 0}$ denote the Lipschitz constants of the $N$ cost components. Intuitively, for any $\delta$-similar subtrajectories $\pi,\pi^{*}$, the cost deviation is bounded component-wise by $|c_{i}(\pi^{*})-c_{i}(\pi)|\leq\delta\cdot K_{c,i}$ for all $i$. We formalize this in the following theorem.

### Theorem 3 (Asymptotic near-optimality of poSST)

poSST is asymptotically $\delta$-robustly near-Pareto-optimal.

The proof, included in Appendix -F, also provides an upper bound on the near-optimality of poSST, reproduced below: where $\Delta c_{i}=\min_{j\in\{0,\dots,M-1\}}c_{i}(\overline{x^{*}_{j}\rightarrow x^{*}_{j+1}})$.

Figure 5 illustrates this upper bound in a 2D objective space. Finally, since the probability of generating a $\delta$-similar trajectory segment is strictly positive, poSST almost surely generates a $\delta$-similar motion plan to any point along the true Pareto front. Thus, in the worst case, it returns a solution within this upper bound as the approximate Pareto front, i.e., for every $\pi^{*}\in\Pi^{*}_{\delta,\text{sol}}$, $\exists\pi\in\Pi^{\textsc{alg}}_{\text{sol}}$ s.t. holds.

Fig. 5: Upper bound on approximation error of the Pareto-front returned by poSST as n → ∞. Worst-case, near-optimal solutions of lexSST (πlexϵ, green) and coSST (πco, yellow) shown relative to true minimums πlex* and πco*, respectively.

### VII-B Analysis of lexSST

We now analyze the impact of PruneLexSet on the poSST framework, arguing that its integration preserves the ability to generate a $\delta$-similar trajectory to the lexicographical minimum $\pi^{*}_{\text{lex}}\in\Pi^{*}_{\delta,\text{sol}}$ for bi-objective problems. Recall that rather than exploring the entire Pareto front, lexSST restricts the search to nodes within an $\epsilon$-tolerance of the current best-known primary cost, effectively considering a slice of width $\epsilon$ near the lexicographical optimum (shown in blue in Fig. 5).

We first show that PruneLexSet does not remove nodes along a $\delta$-similar trajectory to $\pi^{*}_{\text{lex}}$.

### Lemma 4

Let $\epsilon\geq\frac{\delta\cdot K_{c_{1}}+\varepsilon_{1}}{\Delta c_{1}}\cdot c_{1}(\pi^{*}_{\text{lex}})$, and let $R^{\text{lex}}_{s}$ be the representative set of a witness centered at $s\in\mathcal{B}_{\delta_{c}+\delta_{s}}(x^{*}_{\text{lex},j})$. If a state $x\in R^{\text{lex}}_{s}$ is generated at iteration $n$ such that $x\in\mathcal{B}_{\delta_{c}}(x^{*}_{\text{lex},j})$ and then for every iteration $n^{\prime}>n$, there exists a state $x^{\prime}\in R^{\text{lex}}_{s}$ such that $x^{\prime}\in\mathcal{B}_{\delta-\delta_{\text{PS}}}(x^{*}_{\text{lex},j})$ and $C(x^{\prime})\succeq C(x)$.

### Theorem 4 (Completeness of lexSST)

lexSST is probabilistically $\delta$-robustly complete for Problem 1. ‣ II-A Lexicographic-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality") with bi-objective requirements.

### Theorem 5 (Asymptotic near-optimality of lexSST)

lexSST is asymptotically $\delta$-robustly near-optimal for Problem 1. ‣ II-A Lexicographic-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality") with bi-objective requirements.

Proofs are included in Appendices -G, -H, and -I, respectively.

In practice, $c_{1}(\pi^{*}_{\text{lex}})$ is unknown a priori, so a sufficiently large, fixed $\epsilon$ cannot be set to satisfy the condition in Lemma 4. However, a surrogate $\tilde{\epsilon}$ can be computed dynamically from the current best solution: Since $c_{1}(\hat{\pi}^{*})\geq c_{1}(\pi^{*}_{\text{lex}})$, we maintain a conservative tolerance satisfying Lemma 4. As the algorithm progresses, $c_{1}(\hat{\pi}^{*})$ decreases monotonically, $\tilde{\epsilon}$ shrinks accordingly, and Since $\delta$, $\delta_{s}$, and $\vec{\varepsilon}$ are user-defined, the sub-optimality bound can be driven to zero, and by Eq. in the proof: An asymptotically optimal variant $\textsc{lexSST}^{*}$ can be obtained by applying a shrinking schedule to $\delta_{\text{PS}}$, $\delta_{s}$, and $\vec{\varepsilon}$, analogous to that of $\textsc{SST}^{*}$, thereby progressively densifying the search tree in both the state and objective spaces.

### VII-C Analysis of coSST

The analysis of coSST mirrors that of lexSST, with the key difference that PruneConSet enforces a fixed constraint window $\bar{c}_{i}+\bar{\epsilon}_{i}$ rather than the shifting $\epsilon$-window of PruneLexSet. We show this substitution preserves the ability to generate a $\delta$-similar trajectory to $\pi^{*}_{\text{co}}$, the motion plan minimizing $c_{N}$ subject to all $N-1$ constraints. For compactness, we write $i\neq N$ to mean $i\in\{1,\dots,N-1\}$.

### Lemma 5

Let $\bar{\epsilon}_{i}\geq\frac{\delta\cdot K_{c,i}+\varepsilon_{i}}{\Delta c_{i}}\cdot c_{i}(\pi^{*}_{\text{co}})$ for all $i\neq N$, and let $R^{\text{co}}_{s}$ be the representative set of a witness centered at $s\in\mathcal{B}_{\delta_{c}+\delta_{s}}(x^{*}_{\text{co},j})$. If a state $x\in R^{\text{co}}_{s}$ is generated at iteration $n$ such that $x\in\mathcal{B}_{\delta_{c}}(x^{*}_{\text{co},j})$ and then for every iteration $n^{\prime}>n$, there exists a state $x^{\prime}\in R^{\text{co}}_{s}$ such that $x^{\prime}\in\mathcal{B}_{\delta-\delta_{\text{PS}}}(x^{*}_{\text{co},j})$ and $C(x^{\prime})\succeq C(x)$.

### Theorem 6 (Completeness of coSST)

coSST is probabilistically $\delta$-robustly complete for Problem 2. ‣ II-B Constrained-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality").

### Theorem 7 (Asymptotic near-optimality of coSST)

coSST is asymptotically $\delta$-robustly near-optimal for Problem 2. ‣ II-B Constrained-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality").

Proofs are included in Appendices -J, -K, and -L, respectively.

Since $c_{i}(\pi^{*}_{\text{co}})$ is unknown a priori, $\bar{\epsilon}_{i}$ can be conservatively set using the user-defined bounds $\bar{c}_{i}$: which satisfies Lemma 5 since $c_{i}(\pi^{*}_{\text{co}})\leq\bar{c}_{i}$ by the problem statement. As with lexSST, the sub-optimality bound decreases monotonically as $\delta_{\text{PS}},\delta_{s}\to 0$ and $\vec{\varepsilon}\to 0$, and an asymptotically optimal variant, $\textsc{coSST}^{*}$, follows by applying a shrinking schedule analogous to that of $\textsc{SST}^{*}$.

## Evaluations

We present a series of case studies designed to validate the theoretical contributions of this work and demonstrate the practical advantages of our proposed algorithms. We first introduce the experimental setup, then present our evaluations of lexSST, coSST, and poSST in the subsequent subsections.

### VIII-A Overview

### Workspaces

Experiments are conducted across four workspaces shown in Fig. 6: a simple environment (WS-1), a two-homotopy-class environment (WS-2), a three-homotopy-class environment (WS-3), and a cluttered environment with many homotopic solution classes (WS-4).

### Dynamics Models

We consider two dynamic models: (i) a 2D double integrator (Integrator) with state $x=[p_{x},p_{y},v_{x},v_{y}]^{\top}$ comprising position and velocity, and control input $u=[a_{x},a_{y}]^{\top}$ representing acceleration, and (ii) a 4D bicycle model (Bicycle) with dynamics: where $(p_{x},p_{y})$ is the rear-axle position, $\theta$ is the heading angle, and $\lambda$ is the steering angle. The control input consists of the longitudinal velocity $u_{v}$ and the steering rate $u_{\dot{\lambda}}$.

### Objective functions

We consider three cost functions: where $\mathcal{\check{D}}(x,\mathbb{X})$ is the shortest distance from state $x$ to the set $\mathbb{X}_{O}$. Each experiment is given two of the above objectives, with the goal of minimizing the associated cost functions.

For example, a subset of Pareto-optimal trajectories for objectives PathLength and MaxMinClearance is shown in Figs. 6(a) and 6(b) for workspaces WS-1 and WS-2, respectively. Due to the simplicity of these environments and the interdependence of the objectives, the Pareto front can be computed analytically.

Fig. 6: Considered workspaces. Shades of gray in (c) and (d) correspond to the values of GaussianCost.

### Setup

Results are reported across 100 independent runs and compared against weighted-sum SST (ws-SST) as the primary baseline. Each case study is designed to isolate a specific aspect of the proposed approach, progressing from single-solution problems to full Pareto front approximation.

All algorithms were implemented in C++ as extensions to the SST implementation provided by the Open Motion Planning Library (OMPL). No parallelization was employed; all simulations were run sequentially on a machine equipped with an AMD Ryzen™ 5 8645HS processor (4.3 GHz base clock) and 16 GB of RAM. The implementation will be made publicly available upon the acceptance of the article.

### VIII-B Lexicographic Minimization

### Case Study 1 -- lexSST vs SST

(a) Solution trajs. in WS-1.

(b) Solutions in objective space.

(c) Time evolution of $c_{1}(\pi_{n}^{\textsc{alg}})$.

(d) Time evolution of $c_{2}(\pi_{n}^{\textsc{alg}})$.

Fig. 7: Case Study 1 (lexSST vs. SST). Lexicographic objectives: MaxMinClearance (1st) and PathLength (2nd).

(a) Solution trajectories in WS-2.

(b) Solutions in objective space.

(c) Time evolution of $c_{1}(\pi_{n}^{\textsc{alg}})$.

(d) Time evolution of $c_{2}(\pi_{n}^{\textsc{alg}})$.

Fig. 8: Case Study 2 (lexSST vs. ws-SST). Lexicographic objectives: MaxMinClearance (1st) and PathLength (2nd).

We begin by validating lexSST's ability to approximate the true lexicographic minimum, as established in Theorems 4. ‣ VII-B Analysis of lexSST ‣ VII Analysis ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality") and 5. ‣ VII-B Analysis of lexSST ‣ VII Analysis ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"). The experiment considers workspace WS-1 with the Integrator model, where the optimization objective is lexicographic: minimize MaxMinClearance first, then PathLength. A 10-second planning budget was given per instance. Note that the primary optimum $c_{1}(\pi^{*}_{\text{lex}})$ is achieved by infinitely many trajectories, since any path traversing the widest passage without approaching an obstacle attains the same optimal clearance.

The results are shown in Fig. 7. As seen in Fig. 7(a), SST (blue) reliably finds trajectories that maximize clearance but produces a wide spread of path lengths, since it lacks a mechanism to refine secondary objectives. In contrast, lexSST (orange) correctly prioritizes MaxMinClearance and simultaneously refines PathLength, yielding a tight cluster of solutions near the true lexicographic minimum (red dashed line). This behavior is further evident in the objective space (Fig. 7(b)), where SST solutions are broadly dispersed along the PathLength axis, while lexSST solutions concentrate around the lexicographic minimum (red diamond).

The time series in Figs. 7(c)--7(d) shows the convergence behavior of both planners. Both SST and lexSST converge to $c_{1}(\pi^{*}_{\text{lex}})$ at comparable rates, and lexSST's final solutions remain within the user-defined tolerance $\epsilon$, consistent with Eq.. However, while SST exhibits a large spread in PathLength, lexSST steadily converges toward $c_{2}(\pi^{*}_{\text{lex}})$, demonstrating its ability to refine the secondary objective while respecting the tolerance on the primary one.

### Case Study 2 -- Robustness of lexSST to Weight Selection

Case Study 1 shows that SST produces wide variance in $c_{2}$ when optimizing $c_{1}$ alone. A natural remedy is to add a small weight to $c_{2}$, giving preference to solutions that also improve upon PathLength. Here, we demonstrate the practical failure of this approach in a setting where weight selection is consequential. Workspace WS-2 contains two homotopy classes: an upper corridor with slightly greater clearance and a lower corridor with shorter path length. Using the same dynamics model and objectives as Case Study 1, we compare lexSST against ws-SST with two weight vectors: $\mathbf{w}^{1}=[1,0.01]$ (blue) and $\mathbf{w}^{2}=[1,0.05]$ (green), shown in Fig. 8. Here, a 30-second planning budget was used.

Despite both weight vectors appearing to heavily prioritize $c_{1}$, their behavior differs. In Fig. 8(a), $\mathbf{w}^{1}$ assigns insufficient weight to PathLength, resulting in solutions with high variance in $c_{2}$, similar to vanilla SST. Conversely, $\mathbf{w}^{2}$ overweights PathLength, biasing the planner toward the lower corridor at the expense of $c_{1}$-optimality. In contrast, lexSST consistently selects the upper corridor, forming a tighter bundle around $\pi^{*}_{\text{lex}}$. Fig. 8(b) shows these results in the objective space: ws-SST solutions exhibit either large $c_{2}$ variance ($\mathbf{w}^{1}$) or unbounded $c_{1}$ suboptimality ($\mathbf{w}^{2}$), while lexSST clusters about $\pi^{*}_{\text{lex}}$ within the user-defined tolerance $\epsilon$.

The time series in Figs. 8(c)--8(d) are consistent with Case Study 1: all planners converge in $c_{1}$ at comparable rates, but only lexSST steadily improves $c_{2}$ toward $c_{2}(\pi^{*}_{\text{lex}})$; whereas the variance under $\mathbf{w}^{1}$ persists throughout the planning horizon. This underscores a fundamental limitation of scalarization: no fixed weight vector reliably guarantees near-optimality of the lexicographic solution, whereas lexSST achieves this without any weight tuning.

### VIII-C Constrained Optimization

We now evaluate coSST on Problem 2. ‣ II-B Constrained-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), examining its ability to restrict the search tree to constraint-admissible regions and its completeness advantage over SST. In the following studies, we use the Integrator model and a 10-second time budget per planning instance.

### Case Study 3 -- Constraint-Guided Search

(a) coSST search tree with $\Pi_{n}^{\textsc{alg}}$ dominance pruning.

(b) Search tree with cost-to-go pruning for PathLength.

Fig. 9: Case Study 3 (Constraint-guided search via coSST). Constrained search of πco* for objectives MaxMinClearance and PathLength.

We apply a constraint $\bar{c}_{1}=91$ to MaxMinClearance in WS-1, requiring all trajectories to maintain a clearance of at least 9 units from obstacles. Fig. 9 shows the resulting search trees after a 10-second planning window, with nodes in yellow and witness neighborhoods in blue. The tree is visibly confined to the admissible region, returning multiple non-dominated solutions (in green), with the one that minimizes PathLength (in red).

(c) SST search tree.

(d) coSST search tree.

Fig. 10: Case Study 4 (incompleteness of SST for constrained optimization). SST fails to find feasible solutions in most runs, whereas coSST maintains completeness by retaining multiple constraint-admissible subtrajectories for each witness.

Two additional pruning mechanisms further focus the search. First, we utilize a solution-set dominance check to prune nodes that are strictly dominated by existing solutions in $\Pi_{n}^{\textsc{alg}}$. Since costs increase monotonically, there is no risk of prematurely pruning such nodes. As shown in Fig. 9(a), this prevents exploration of the upper-right and lower-right regions of the workspace, since shorter solutions already exist. Second, we leverage an admissible cost-to-go heuristic which inflates each candidate node's PathLength cost by the shortest remaining path to the goal. As shown in Fig. 9(b), this disqualifies a substantially larger region, since reaching the goal within the remaining PathLength budget becomes infeasible from those states.

### Case Study 4 -- Incompleteness of SST

We empirically confirm the incompleteness of SST for constrained optimization, as argued in Section V-A. The task is to minimize PathLength subject to a constraint on GaussianCost in the narrow-passage environment in Fig. 10, with sparsity parameters chosen to guarantee the existence of a $\delta$-robust solution. We conduct 100 independent runs per planner, each with a 30-second time budget, using the Integrator model.

As shown in Figs. 10(a)--10(b), SST (blue) finds a valid motion plan in only a small fraction (0.11) of runs, whereas coSST succeeds across all runs. This failure is structural, not a consequence of limited planning time. Figs. 10(c)--10(d) show the search trees after a 300-second budget to ensure convergence. Because SST greedily optimizes for PathLength, its single representative at each witness accumulates a high GaussianCost, leaving no feasible extensions through the narrow passage. In contrast, coSST retains multiple constraint-admissible subtrajectories per witness, preserving the ability to extend through the passage. The cost of this completeness guarantee is a larger search tree, as shown in Fig. 10(e), since multiple nodes are maintained per witness.

### VIII-D Pareto Front Coverage

Having validated the single-solution algorithms, we now evaluate poSST on Problem 3. ‣ II-C Pareto-Optimal Motion Planning ‣ II Problem Formulation ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"). We first demonstrate poSST's Pareto-completeness and near-optimality, and then show its computational advantages relative to scalarization methods.

### Case Study 5 -- Convex Pareto Front

We again consider a Integrator model in WS-1 under the objectives MaxMinClearance and PathLength, but without imposing any priority among the objectives, aiming to recover the entire Pareto front. Fig. 11(a) shows an example run as poSST discovers a diverse set of non-dominated trajectories that span the full Pareto front. Fig. 11(b) shows how the approximate front computed by poSST progressively approaches the theoretical optimum over time, with lighter hues indicating later times.

Over 100 runs with a 60-second planning budget, poSST identified, on average, 50 non-dominated solutions per run, providing broad coverage of the objective space as shown in Fig. 11(c). To quantify approximation quality, we define a coverage metric according to the ratio of the region dominated by the approximate front to the area enclosed by the true Pareto front and the axis-aligned boundary (red dashed lines in Fig. 11(b)). As shown in Fig. 11(d), poSST dominated, on average, roughly 80% of the reference area over the 60-second planning horizon, demonstrating its near-Pareto-optimality.

(b) Evolution of Pareto front.

(c) Pareto fronts (all runs).

(d) Coverage metric of $\Pi_{n}^{\textsc{alg}}$.

Fig. 11: Case Study 5 (efficacy of poSST in approximating Πsol* with objectives MaxMinClearance and PathLength). (a) and (b) show a single representative run. (c) and (d) aggregate over 100 runs.

### Case Study 6 -- Non-Convex Pareto Fronts

A key motivation for this work is the structural inability of weighted-sum scalarization to recover non-convex Pareto fronts, as established in Section III. We evaluate poSST with objectives GaussianCost and PathLength across two environments: WS-3 with three homotopic solution classes and a cluttered workspace, WS-4. We compare poSST against ws-SST initialized with 101 different weight vectors, spanning a normalized sweep of unique ratios to promote diverse solutions: Each instance of ws-SST is given a planning budget of 30-seconds (3030 seconds total), while poSST is given a single 30-second planning instance. This comparison is intentionally demanding, as the baseline is allocated $101\times$ the computational budget of poSST.

Non-convex front recovery (Figs. 12(a), 12(c)): Workspace WS-3, using the Integrator model, isolates the structural limitation of WS scalarization (ws-SST) on a highly non-convex Pareto front, where many optimal trade-offs do not lie on the convex hull. Across the 101 weight selections, ws-SST collapses to two solution clusters: one that prioritizes PathLength by passing through the gap, and one that prioritizes GaussianCost by traveling over the wall. The intermediate trade-offs that balance both objectives are missed entirely. poSST, by contrast, discovers a diverse set of solutions spanning all three homotopic classes, empirically demonstrating the Pareto-completeness established in Theorem 2. ‣ VII-A2 Properties of PruneDominated ‣ VII-A Analysis of poSST ‣ VII Analysis ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality").

(a) WS-3 solution trajectories.

(b) WS-4 solution trajectories.

(c) WS-3 Pareto front.

(d) WS-4 Pareto front.

Fig. 12: Case Study 6 (poSST vs. ws-SST on non-convex Pareto fronts). In WS-3, ws-SST recovers only extreme solutions, while poSST discovers trade-offs across all homotopic classes. In WS-4, a single run of poSST achieves better coverage than 101 scalarized planning instances combined.

Computational efficiency (Figs. 12(b), 12(d)): In WS-4 using the Bicycle model, poSST recovers 124 unique Pareto-optimal solutions within a single 30-second planning instance, achieving better coverage than ws-SST across all 101 weight selections. As seen in Fig. 12(d), the cluster of solutions near the PathLength optimum reveals a key pitfall of WS scalarization: since PathLength operates over a larger range than MaxMinClearance, any weight ratio greater than about 0.5 collapses to the same solution, rendering most weight selections redundant. This imbalance is not known a priori, making it difficult to choose weights that yield a diverse spread. poSST avoids this issue entirely, as its element-wise cost comparisons require no unified (scalar) cost metric across objectives. Further, this case study highlights that maintaining a single, non-dominated search tree is substantially more efficient than repeatedly scalarizing and re-planning to recover a diverse set of trade-offs.

### Case Study 7 -- Effect of $\vec{\varepsilon}$ on Pareto Convergence

Finally, we examine the effect of the objective-space sparsity parameter $\vec{\varepsilon}$ introduced in this work, which governs the trade-off between near-optimality and tree size (sparsity). Using workspace WS-1 and the Integrator model, we sweep $\vec{\varepsilon}$ over a range of values and run 100 instances of poSST for each configuration over a 300-second planning horizon.

Fig. 13 presents results as box plots. As expected, larger $\vec{\varepsilon}$ values admit fewer nodes per witness neighborhood (Fig. 13(a)), reducing tree size but coarsening the approximation of the Pareto front (Fig. 13(c)). Conversely, smaller $\vec{\varepsilon}$ yields denser trees with tighter approximations at the cost of slower convergence rates (Fig. 13(d)). This experiment provides practical guidance for tuning $\vec{\varepsilon}$: in time-constrained settings, a moderate $\vec{\varepsilon}$ efficiently achieves broad Pareto coverage, whereas $\vec{\varepsilon}\to\mathbf{0}$ is appropriate when tight bounds are required.

(a) Size of search tree.

(b) Number of witness nodes.

(c) Size of solution set.

(d) Coverage metric of $\Pi_{n}^{\textsc{alg}}$.

Fig. 13: Case Study 7. Effect of ε⃗ on key metrics of poSST with objectives MaxMinClearance and PathLength.

## Conclusion

In this paper, we introduced a unified framework for multi-objective kinodynamic motion planning built on the Stable Sparse-RRT algorithm. Our key insight is the extension from a single representative per witness neighborhood to a *representative set*, enabling the simultaneous maintenance of locally Pareto-optimal subtrajectories within a single search tree. This structure underlies three algorithms: lexSST for lexicographic minimization, coSST for constrained optimization, and poSST for Pareto-front approximation.

For lexSST, we proved that no scalar utility function can represent lexicographic dominance over continuous cost spaces, and, for coSST, we showed that vanilla SST is structurally incomplete under cost constraints. Instead, our algorithms are probabilistically complete and asymptotically near-optimal for both problems. Finally, poSST approximates the entire Pareto front in a single planning instance with formal completeness and bounded sub-optimality guarantees, recovering diverse trade-offs at a fraction of the computation time of repeated scalarized re-planning.

Several directions for future work remain. The $\epsilon$-equivalence approach for lexicographic search does not extend beyond two objectives; hence, how to apply lexSST with three or more cost functions remains an open question. Also, since the cost of maintaining representative sets grows with the number of non-dominated nodes per witness, leveraging GPU-accelerated and vectorized sampling-based planning could bring these algorithms closer to real-time deployment. Adaptation of these algorithms and their formal analysis for multi-objective problems are left to future work.

### A Proof for Theorem 1

### Proof

We prove the result by contradiction in the $N=2$ case, and then argue that it extends to any $N>2$.

Assume that there exists a function $u:\mathbb{R}^{2}_{\geq 0}\rightarrow\mathbb{R}$ such that $C\succ_{\text{lex}}C^{\prime}$ iff $u(C)>u(C^{\prime})$. Fix any $c_{1}\in\mathbb{R}_{\geq 0}$, then by definition of lexicographic preference, we have: $(c_{1},0)\succ_{\text{lex}}(c_{1},1).$ So it must follow that: $u((c_{1},0))>u((c_{1},1)),$ and an interval between $c_{1}$-equivalent vectors can be defined: $I(c_{1}):=[u((c_{1},1)),u((c_{1},0))]\subset\mathbb{R}.$ We claim that for any two distinct $c_{1},c^{\prime}_{1}\in\mathbb{R}_{+}$, the intervals $I(c_{1})$ and $I(c_{1}^{\prime})$ are disjoint. W.L.O.G., assume $c_{1}<c_{1}^{\prime}$. Then: By the construction of each interval, we have: Hence, $I(c_{1})\cap I(c_{1}^{\prime})=\emptyset$. Now define the mapping: where $\mathbb{I}$ is the collection of disjoint intervals in $\mathbb{R}$. Since each $I(c_{1})$ is distinct and disjoint, $\phi$ is injective. Next, since the rationals $\mathbb{Q}$ are dense in $\mathbb{R}$, each interval $I(c_{1})$ contains at least one rational number. Thus, we can define: where $r_{c_{1}}$ is any rational number contained in $I(c_{1})$. Since each $r_{c_{1}}$ is drawn from a distinct and disjoint interval, they are unique. Thus, $\tau$ is injective and the composition $\tau\circ\phi:\mathbb{R}_{\geq 0}\rightarrow\mathbb{Q}$ is likewise injective, implying: $|\mathbb{R}_{\geq 0}|\leq|\mathbb{Q}|.$ This is a contradiction, since $\mathbb{R}_{\geq 0}$ is uncountable and $\mathbb{Q}$ is countable. Hence, the assumption is incorrect, and no such $u$ exists.

The contradiction above holds for vectors in $\mathbb{R}^{2}_{\geq 0}$, and generalizes naturally to $\mathbb{R}^{n}_{\geq 0}$ for $n>2$. Since lexicographic ordering compares objectives sequentially, the utility function will necessarily compare objectives $c_{i}$ and $c_{i+1}$, resulting in the same conclusion. ∎

### B Proof for Lemma 1

### Proof

Consider a node $x\in\mathcal{B}_{\delta_{\text{PS}}}(x^{*}_{i})$ added to the tree at iteration $n$. Suppose a sample $x_{\text{rand}}$ is drawn such that $x_{\text{rand}}\in\mathcal{B}_{\delta_{\text{PS}}}(x)\cap B_{\theta}(x^{*}_{i}),$ where $\theta=\delta-\delta_{\text{PS}}>0$ by Proposition 1. ‣ VII-A Analysis of poSST ‣ VII Analysis ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"). In this case, node $x$ lies within the region considered by ParetoSelect, and $\gamma_{x}>0$ unless $x$ is strictly dominated by another node $x^{\prime}$ (i.e., $C(x^{\prime})\succ C(x)$). In that case, $x^{\prime}$ is the better representative of $\pi^{*}$. This leads to a positive lower bound on the probability of selecting a node within $\mathcal{B}_{\delta}(x^{*}_{i})$ that can generate a $\delta$-similar trajectory to $\pi^{*}$: where $\mu(\cdot)$ denotes the Lebesgue measure and $|\cdot|$ denotes the cardinality of a set. ∎

### C Proof for Lemma 2

### Proof

Suppose a node $x$ is generated by poSST at iteration $n$ such that $x\in\mathcal{B}_{\delta_{c}}(x^{*}_{i})$. Then, $x$ is either used to establish a new witness set or is added to an existing witness located at most $\delta_{s}$ away. In the latter case, $x$ can lie at most a distance $\delta_{c}$ from $x^{*}_{i}$ while being associated with a witness at a distance $\delta_{c}+\delta_{s}$ from $x^{*}_{i}$, as shown by the blue ball in Figure 14.

Fig. 14: The witness and selection radii used in poSST.

The PruneDominated procedure ensures that a node $x\in\mathcal{B}_{\delta_{c}}(x_{i}^{*})$ is pruned only if there exists another node $x^{\prime}\in\mathcal{B}_{\delta_{c}+2\delta_{s}}(x_{i}^{*})$ such that $C(x^{\prime})\succeq C(x)+\vec{\varepsilon}$. The presence of such a node $x^{\prime}$ may lead to the pruning of any node it $\varepsilon$-dominates, as indicated by the gray region in Figure 14 (right).

Consequently, for any reference trajectory $\pi^{*}\in\Pi^{*}_{\delta,\text{sol}}$, there always exists a node $x^{\prime}\in V$ that deviates from $x$ by at most $\varepsilon_{i}$ in some (but not all) cost components and remains within a distance of $\delta-\delta_{\text{PS}}$ from $x_{i}^{*}$ for all iterations $n^{\prime}>n$. ∎

### D Proof for Lemma 3

### Proof

Refer to Fig. 14 for visualization. The ParetoSelect procedure considers all non-dominated nodes in the neighborhood $\mathcal{B}_{\delta_{\text{PS}}}(x_{\text{rand}})$. For the algorithm to consider only nodes within $\mathcal{B}_{\delta}(x^{*}_{i})$, the sampled state $x_{\text{rand}}$ must lie in $\mathcal{B}_{\delta-\delta_{\text{PS}}}(x^{*}_{i})$. In the worst case, a node $x\in\mathcal{B}_{\delta_{c}}(x^{*}_{i})$ is replaced by a node $x^{\prime}\in\mathcal{B}_{\delta-\delta_{\text{PS}}}(x^{*}_{i})$, lying on the outer edge of that ball. For $x^{\prime}$ to be considered, the sample $x_{\text{rand}}$ must fall within the intersection of $\mathcal{B}_{\delta-\delta_{\text{PS}}}(x^{*}_{i})$ and $\mathcal{B}_{\delta_{\text{PS}}}(x^{\prime})$. Once $x^{\prime}$ is considered, then it will have a non-zero probability of selection unless it is strictly dominated by another node $x^{\prime\prime}\in\mathcal{B}_{\delta_{\text{PS}}}(x^{\prime})$, which, in the worst case, lies on the outer edge of $\mathcal{B}_{\delta}(x_{i}^{*})$. Therefore, the probability of selecting such a node is lower-bounded : $\gamma_{\text{PS}}=\frac{\mu\left(\mathcal{B}_{\delta-\delta_{\text{PS}}}(x^{*}_{i})\cap\mathcal{B}_{\delta_{\text{PS}}}(x^{\prime})\right)}{|\mathcal{B}_{\delta_{\text{PS}}}(x^{\prime})|\cdot\mu(\mathbb{X})}>0.$ ∎

### E Proof for Theorem 2. ‣ VII-A2 Properties of PruneDominated ‣ VII-A Analysis of poSST ‣ VII Analysis ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")

### Proof

Given that the initial state satisfies $x_{0}=\pi^{*}\in\mathcal{B}_{\delta_{c}}(\pi^{*})$ for all $\pi^{*}\in\Pi^{*}$, and that $V$ is initialized as $\{x_{0}\}$, we can inductively establish the continued progress of poSST in generating a $\delta$-similar trajectory to any reference trajectory $\pi^{*}$. At each iteration, the following two conditions are guaranteed: with probability $\rho_{\delta\rightarrow\delta_{c}}>0$, the propagation procedure MonteCarloProp successfully transitions from $\mathcal{B}_{\delta}(x^{*}_{i})$ to the next ball $\mathcal{B}_{\delta_{c}}(x^{*}_{i+1})$ along the reference trajectory by \[17, Theorem 17\]; and with probability $\gamma_{\text{PS}}>0$, a node within $\mathcal{B}_{\delta}(x^{*}_{i})$ is selected for extension by Lemma 3. Together, these properties guarantee that at every iteration, poSST maintains a non-zero probability of generating a node within each ball $\mathcal{B}_{\delta_{c}}(x^{*}_{i})$ and selecting a node in $\mathcal{B}_{\delta}(x^{*}_{i})$ for all $i=0,1,\dots,M-1$, thereby ensuring probabilistic visitation of every ball in a covering sequence about any reference path. ∎

### F Proof for Theorem 3. ‣ VII-A3 Near-optimality of poSST ‣ VII-A Analysis of poSST ‣ VII Analysis ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")

### Proof

Consider a $\delta$-similar trajectory segment $\overline{x_{j}\rightarrow x_{j+1}}$ generated by poSST, where $x_{j}\in\mathcal{B}_{\delta}(x_{j}^{*})$ and $x_{j+1}\in\mathcal{B}_{\delta}(x_{j+1}^{*})$ for some optimal trajectory $\pi^{*}$. Then, due to the Lipschitz continuity of the cost functions, each cost component $c_{i}$ satisfies: $c_{i}(\overline{x_{j}\rightarrow x_{j+1}})\leq c_{i}(\overline{x_{j}^{*}\rightarrow x_{j+1}^{*}})+\delta\cdot K_{c,i}.$ Furthermore, from Lemma 2, we know that if a node $x_{j}\in\mathcal{B}_{\delta-\delta_{\text{PS}}}(x_{j}^{*})$ exists at iteration $n$, then there exists at least one node $x_{j}^{\prime}\in V$ that is either $\varepsilon$-dominant or equal to $x_{j}$ in the same ball $\mathcal{B}_{\delta-\delta_{\text{PS}}}(x_{j}^{*})$. Lemma 1 ensures that $x_{j}^{\prime}$ will be selected with probability at least $\gamma_{\text{PS}}>0$, or else a dominant node $x_{j}^{\prime\prime}\in\mathcal{B}_{\delta}(x_{j}^{*})$ will be selected. Therefore, we have for all future iterations of the algorithm.

Now, consider the first segment $\overline{x_{0}\rightarrow x_{1}}$ of a trajectory generated by poSST that approximates a Pareto-optimal trajectory $\pi^{*}$. Then, the cost of a representative segment at an iteration $n^{\prime}>n$ can be bounded as: We can extend the bound to a $k$-segment trajectory from $x_{0}$: Let $\Delta c_{i}$ denote the minimum cost incurred in objective $i$ among all segments of $\pi^{*}$ in $\mathbb{B}(\pi^{*},\delta,\Delta c_{1})$. Then, the maximum number of segments $k$ is bounded by $k\leq\frac{c_{i}(\pi^{*})}{\Delta c_{i}}$ for each $i$, yielding the final sub-optimality bound:

### G Proof for Lemma 4

### Proof

By Theorems 2. ‣ VII-A2 Properties of PruneDominated ‣ VII-A Analysis of poSST ‣ VII Analysis ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality") and 3. ‣ VII-A3 Near-optimality of poSST ‣ VII-A Analysis of poSST ‣ VII Analysis ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), the ParetoSelect and PruneDominated procedures do not hinder the generation of a $\delta$-similar trajectory to any Pareto-optimal solution. Since $\pi^{*}_{\text{lex}}$ is Pareto-optimal by definition, a node $x_{j}\in\mathcal{B}_{\delta}(x^{*}_{\text{lex},j})$ that lies within the covering ball sequence of $\pi^{*}_{\text{lex}}$ will have a primary cost that satisfies after the $j$-th segment: $c_{1}(x_{j})\leq c_{1}(x^{*}_{\text{lex},j})+j\cdot(\delta\cdot K_{c,1}+\varepsilon_{1}).$ PruneLexSet removes all nodes exceeding $\bar{c}_{1}^{*}+\epsilon$, where $\bar{c}_{1}^{*}=\min_{x\in R^{\text{lex}}_{s}}c_{1}(x)$. Since $\epsilon\geq k(\delta\cdot K_{c,1}+\varepsilon_{1})$, $\bar{c}_{1}^{*}\geq c_{1}(x^{*}_{\text{lex},j})$, and $k\geq j$, we get: and $x_{j}$ remains in $R^{\text{lex}}_{s}$. ∎

### H Proof for Theorem 4. ‣ VII-B Analysis of lexSST ‣ VII Analysis ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")

### Proof

The search tree is initialized with $x_{0}\in\mathcal{B}_{\delta_{c}}(\pi^{*}_{\text{lex}})$. At every iteration: Lemma 1 guarantees a positive probability of selecting a node in $\mathcal{B}_{\delta}(x^{*}_{\text{lex},j})$; Lemma 4 ensures PruneLexSet retains at least one such node; and \[17, Theorem 17\] guarantees a positive probability of transitioning to $\mathcal{B}_{\delta_{c}}(x^{*}_{\text{lex},j+1})$. Together, these ensure lexSST makes progress toward a $\delta$-similar trajectory to $\pi^{*}_{\text{lex}}$ at every iteration. ∎

### I Proof for Theorem 5. ‣ VII-B Analysis of lexSST ‣ VII Analysis ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")

### Proof

The proof follows that of Theorem 3. ‣ VII-A3 Near-optimality of poSST ‣ VII-A Analysis of poSST ‣ VII Analysis ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), restricted to $\pi^{*}_{\text{lex}}$. Since lexSST is guaranteed to find a $\delta$-similar trajectory $\hat{\pi}_{\text{lex}}$ to $\pi^{*}_{\text{lex}}$, the bound in gives: By Lemma 4, the solution set $\Pi^{\textsc{alg}}_{\text{sol}}$ always contains a trajectory $\hat{\pi}_{\text{lex}}^{\prime}$ with $C(\hat{\pi}_{\text{lex}}^{\prime})\succeq C(\hat{\pi}_{\text{lex}})$. The returned solution $\pi^{\epsilon}_{\text{lex}}$ incurs an additional $\epsilon$-penalty on the primary cost bound due to the $\epsilon$-window, yielding:

### J Proof for Lemma 5

### Proof

The proof follows that of Lemma 4, replacing the $\epsilon$-window on the primary cost with per-constraint buffers $\bar{\epsilon}_{i}$. Since $\pi^{*}_{\text{co}}$ minimizes $c_{N}$ and is thus Pareto-optimal, a node $x_{j}$ within the covering ball sequence of $\pi^{*}_{\text{co}}$ satisfies: PruneConSet removes nodes exceeding $\bar{c}_{i}+\bar{\epsilon}_{i}$. Since $\bar{\epsilon}_{i}\geq k(\delta\cdot K_{c,i}+\varepsilon_{i})$, $\bar{c}_{i}\geq c_{i}(x^{*}_{\text{co},j})$, and $k\geq i$, we get $c_{i}(x_{j})\leq\bar{c}_{i}+\bar{\epsilon}_{i}$ and $x_{j}$ is retained in $R^{\text{co}}_{s}$. ∎

### K Proof for Theorem 6. ‣ VII-C Analysis of coSST ‣ VII Analysis ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")

### Proof

Follows the outline of Theorem 4. ‣ VII-B Analysis of lexSST ‣ VII Analysis ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), with Lemma 5 replacing Lemma 4 to guarantee that PruneCoSet retains at least one node in $\mathcal{B}_{\delta}(x^{*}_{\text{co},j})$ at every iteration. ∎

### L Proof for Theorem 7. ‣ VII-C Analysis of coSST ‣ VII Analysis ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality")

### Proof

Follows directly from Theorem 3. ‣ VII-A3 Near-optimality of poSST ‣ VII-A Analysis of poSST ‣ VII Analysis ‣ Multi-Objective Kinodynamic Motion Planning with Asymptotic Pareto Optimality"), restricted to $\pi^{*}_{\text{co}}$, which ensure a motion plan $\pi_{\text{co}}$ will be generated that satisfies: By Lemma 5, the solution set $\Pi^{\textsc{alg}}_{\text{sol}}$ will contain a trajectory $\hat{\pi}_{\text{con}}^{\prime}$ with $C(\hat{\pi}_{\text{con}}^{\prime})\succeq C(\hat{\pi}_{\text{con}})$ for iterations $n^{\prime}>n$. Then, the returned solution $\pi_{\text{co}}=\arg\min_{\pi\in\Pi^{\textsc{alg}}_{\text{sol}}}c_{N}(\pi)$ satisfies: where $\mathbf{1}_{\{\cdot\}}$ is an indicator function applied to the buffer $\bar{\epsilon}_{i}$ which accounts for the fixed constraint window, analogous to the $\epsilon$-penalty in Eq.. ∎
