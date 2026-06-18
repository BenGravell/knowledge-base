GCS*: Forward Heuristic Search on Implicit Graphs of Convex Sets

Topics include Motion planning, Probabilistic models, Graphs, Sampling-based methods, Planning, Sampling, Graphs of convex sets.

We consider large-scale, implicit-search-based solutions to Shortest Path Problems on Graphs of Convex Sets (GCS). We propose GCS*, a forward heuristic search algorithm that generalizes A* search to the GCS setting, where a continuous-valued decision is made at each graph vertex, and constraints across graph edges couple these decisions, influencing costs and feasibility. Such mixed discrete-continuous planning is needed in many domains, including motion planning around obstacles and planning through contact. This setting provides a unique challenge for best-first search algorithms: the cost and feasibility of a path depend on continuous-valued points chosen along the entire path. We show that by pruning paths that are cost-dominated over their entire terminal vertex, GCS* can search efficiently while still guaranteeing cost-optimality and completeness. To find satisficing solutions quickly, we also present a complete but suboptimal variation, pruning instead reachability-dominated paths. We implement these checks using polyhedral-containment or sampling-based methods....

## Introduction

Many real-world planning problems involve making discrete and continuous decisions jointly. Collision-free motion planning selects whether to go left or right around an obstacle along with a continuous trajectory to do so. In Task and Motion Planning (TAMP), discrete task-level decisions about the type and sequence of actions are intimately coupled with continuous robot motions and object configurations. For example, where a robot grasps a hockey stick impacts its ability to hook an object \[\]; in the construction of a tower, the order in which materials are assembled, as well as their geometric relationships, affect stability.

Figure 1: An ϵ-suboptimal solution found in 21.9s by GCS* using sampling-based ReachesCheaper domination checks on the STACK planar pushing task. STACK is formulated as a GCS problem with approximately 1.3 × 109 vertices and up to 8.5 × 1017 edges.

## Conclusion

We propose GCS\*, a forward heuristic search algorithm for solving large discrete-continuous planning problems formulated as GCS. We define two domination checks ReachesNew and ReachesCheaper, as well as containment and sampling-based implementations of those checks that allow GCS\* to be complete and optimal, or have probabilistic/asymptotic versions of those properties, respectively. GCS\* provides a principled way of addressing the challenges of applying graph search to the discrete-continuous setting. We demonstrate settings in which GCS\* performs favourably compared to the state-of-the-art....

If a candidate path $\mathbf{v}$ reaches some point $x \in \mathcal{X}_{\mathbf{v}_{\text{end}}}$ cheaper than any way found yet, as in sec. 4.2 (b), (c), and (d), we say it ReachesCheaper:

A GCS \[\] is a directed graph $G:={(\mathcal{V},\mathcal{E})}$ defined by a (potentially infinite) set of vertices $\mathcal{V}$ and edges $\mathcal{E} \subset \mathcal{V}^{2}$, where ${(u,v)} \in \mathcal{E}$ if the graph allows transitions from vertex $u$ to vertex $v$, i.e., $v$ is a *successor* of $u$. Each vertex $v \in \mathcal{V}$ is paired with a compact convex set $\mathcal{X}_{v}$. These sets may live in different spaces. We assume each vertex has a finite number of successors....

GCS\* returns a path from $s$ to $t$ in finite iterations if one exists.
