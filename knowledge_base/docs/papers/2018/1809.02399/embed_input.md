<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Sampling-based Optimal Kinodynamic Planning with Motion Primitives

Topics include Kinodynamic planning, Trajectory planning, Asymptotic optimality, Sampling-based, Rapidly-exploring random tree star, Motion primitives, Precomputed, Lookup table, Grid.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Integrates a grid of states and offline precomputed connecting motion primitives into RRT*. Moves the computational burden of trajectory generation to an offline phase, trading runtime efficiency for memory usage and some optimality degradation tied to grid resolution.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

This paper proposes a novel sampling-based motion planner, which integrates in Rapidly exploring Random Tree star (RRT*) a database of pre-computed motion primitives to alleviate its computational load and allow for motion planning in a dynamic or partially known environment. The database is built by considering a set of initial and final state pairs in some grid space, and determining for each pair an optimal trajectory that is compatible with the system dynamics and constraints, while minimizing a cost. Nodes are progressively added to the tree of feasible trajectories in the RRT* algorithm by extracting at random a sample in the gridded state space and selecting the best obstacle-free motion primitive in the database that joins it to an existing node. The tree is rewired if some nodes can be reached from the new sampled state through an obstacle-free motion primitive with lower cost. The computationally more intensive part of motion planning is thus moved to the preliminary offline phase of the database construction at the price of some performance degradation due to gridding. Grid resolution can be tuned so as to compromise between (sub)optimality and size of the database.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The planner is shown to be asymptotically optimal as the grid resolution goes to zero and the number of sampled states grows to infinity.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Motion planning is one of the fundamental problems in robotics, and consists of guiding the robot from an initial state to a final one along a collision-free path.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

For many robots, focusing only on kinematics could result in collision-free paths that are impossible to be executed by the actual system. In particular, for systems that are differentially constrained, such a decoupled approach makes it difficult to turn a collision-free path into a feasible trajectory. In order to tackle this problem, Donald et al proposed the idea of *kinodynamic planning*, which combines the search for a collision-free path with the underlying dynamics of the system, so that the resulting trajectory would be feasible.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

For most robotic applications, the solution to the planning problem should not only be feasible and collision-free, but also satisfy some properties such as, e.g., reaching the goal in minimum time, minimizing the energy consumption, and maximizing safety. These additional requirements have shifted the focus from simply designing collision-free and feasible trajectories to finding optimal ones.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

This paper deals with *optimal kinodynamic motion planning* for systems with complex dynamics and subject to constraints.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Literature review", "weight": 1.0} -->

A significant amount of work in the robotics community has then been dedicated to the problem of kinodynamic planning so as to determine a trajectory that fulfills the differential constraints arising from the dynamics of the robot. Solving this problem is complex, in general, since it requires a search in the state space of the robot, which often implies a higher-dimensional search space compared to a pure kinematic planning.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Literature review", "weight": 1.0} -->

Most of the motion planners can be classified under the two categories of *exact* and *sampling-based* methods, LaValle. The former looks for a solution in the continuous state space, while the latter samples this space redefining it as a graph where nodes are connected via edges representing local trajectories between sampled states.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Literature review", "weight": 1.0} -->

Exact methods are said to be *complete*, since they terminate in finite time with a solution, if one exists, and return the nonexistence otherwise. However, with the exact approaches even the simplest problem is PSPACE hard. Exact methods require that the obstacles are represented explicitly in the state space, dramatically increasing the problem complexity. However, they can provide practical solutions for problems that are characterized by a low dimensional state space, or for which a low dimensional obstacle representation can be adopted. Obstacles introduce non convex constraints in the admissible state space, and make the problem of computing an optimal trajectory hard. In particular, most of the algorithms, that are gradient based, can only find a solution in the same homotopy class of the initial guess. There has been a significant progress to address this issue and, in particular, the ideas of dividing the global optimal trajectory planning problem into simpler subproblems and of using numerical optimization to compute locally optimal trajectories have been explored, e.g.,.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Literature review", "weight": 1.0} -->

Sampling-based approaches emerged to handle systems with high dimensional state spaces, and they became the most popular approaches in the planning literature techniques, representing the practical way to tackle the problem. The basic idea is to sample states (nodes) in the continuous state space and connect these nodes with trajectories in the collision-free space, building a roadmap in the form of a graph or a tree of feasible trajectories. These algorithms avoid an explicit representation of obstacles by using a collision check module that allows to determine the feasibility of a tentative trajectory. They are not complete, but they satisfy the *probabilistic completeness* property, i.e., they return a solution with a probability converging to one as the number of samples grows to infinity, if such a solution exists.\Probabilistic Road Map (PRM), introduced by Kavraki et al, and Rapidly exploring Random Trees (RRT), introduced by LaValle and Kuffner Jr, were the first popular sampling-based planners. PRM first creates a graph in the free configuration space by randomly sampling nodes and connecting them to the already existing ones in the graph using a local planner.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Literature review", "weight": 1.0} -->

The graph can then be used to answer multiple queries, where in each query a start node and a goal node are added to the graph and a path connecting the two nodes is looked. RRT, on the other hand, incrementally builds a tree starting from a given node, returning a solution as soon as the tree reaches the goal region, hence providing a fast on-line implementation. In all the different formulations of sampling-based planners, a steering function is required to design a trajectory (edge in the tree terminology) connecting two nodes of the tree.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Literature review", "weight": 1.0} -->

Considering the quality of the solution, an important progress has been made with the introduction of RRT^⋆^ (Rapidly exploring Random Tree star) and PRM^⋆^ (Probabilistic Road Map star), which have been proven to be *asymptotically optimal*, i.e., the probability of finding an optimal solution, if there exists one, converges to 1 as the tree cardinality grows to infinity,. The main idea of these algorithms is to ensure that each node is connected to the graph optimally, possibly rewiring the graph by testing connections with pre-existing nodes that are in a suitably defined neighborhood. The same strategy applies to kinodynamic planning as well, with the additional difficulty that when optimality is required, implementing the steering function involves solving a *two point boundary value problem* (TPBVP), which is computationally challenging especially when dealing with complex dynamics, such as for non-holonomic robots, in presence of actuation constraints. In the context of kinodynamic planning RRT^⋆^ and PRM^⋆^ cannot be considered in the same way.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Literature review", "weight": 1.0} -->

In fact, PRM^⋆^ is limited to symmetric costs and to those systems for which the cost associated to a TPBVP is conserved when the boundary pairs are swapped. Note that, nonholonomic systems do not belong to this class.\Considering instead RRT^⋆^, it must be noticed that for various dynamical systems, such as non-holonomic vehicles, the presence of kinodynamic constraints makes the constrained optimization problem that the steering function has to solve extremely complex.\To deal with this computational complexity, some effort has been made towards developing effective steering functions for different types of dynamical systems. Webb and van den Berg have obtained the closed-form analytical solution for a minimum time minimum energy optimization problem for systems with linear dynamics, and extended it to non-linear dynamics using first-order Taylor approximation. Other works have focused on approximating the solution for systems with linearizable dynamics, by locally linearizing the system and applying linear quadratic regulation (LQR).\Some recent attempts have been made towards optimality without formulating and solving a TPBVP, as well.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Literature review", "weight": 1.0} -->

For example, algorithms like Stable Sparse RRT^⋆^ (SST^⋆^) have proved asymptotic optimality given access only to a forward propagation model. The idea is to iteratively sample a set of controls and final times instead of explicitly solving the BVP. Similarly, a variant of RRT^⋆^ uses a shooting method without a steering function to improve the solution by pruning branches from the tree. If a sampled node has a lower cost compared to another one that is close by and that shares the same parent, the pre-existing node is pruned from the tree and its branches are connected to the newly sampled node, or they are pruned completely if they are not collision-free. This approach generates feasible but inherently suboptimal solutions. Other works on extending RRT^⋆^ to handle kinodynamic constraints include limiting the volume in the state space from which nodes are selected by tailoring it to the considered dynamical system in order to improve computational effectiveness.\Nevertheless, solving the TPBVP for an arbitrary nonlinear system remains challenging and typically calls for numerical solvers.

<!-- chunk {"id": "body-0017", "role": "body", "section": "Literature review", "weight": 1.0} -->

The algorithms that account for a nonlinear optimization tool, like for example ACADO toolkit, GPOPS-II, etc., commonly use *Sequential Quadratic Programming* (SQP) for solving the TPBVPs numerically, and embed it as a subroutine in the sampling based planning framework such as in RRT\* or in Batch-Informed-Trees star (BIT^⋆^).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Literature review", "weight": 1.0} -->

A different class of algorithms, aiming at optimality, is based on graph search and adopt a gridding approach. The main idea is to discretize the state space, building a grid, and compute a graph. The motion planning problem is then recast into finding the best sequence of motions by traversing this graph with an optimal search algorithm like A^⋆^. This graph is often represented by a state lattice, a set of states distributed in a regular pattern, where the connections between states are provided by feasible/optimal trajectories. Likhachev and Ferguson improved the idea of state lattice by using a multi-resolution lattice such that the portion of the graph that is close to either the initial or the goal state has a higher resolution than the other parts. These approaches have been successfully applied to several robotic systems and found to be effective for dynamic environments. However, these algorithms are *resolution optimal*, such that the optimality is guaranteed up to the grid resolution. Furthermore, their computational effectiveness is highly related to the resolution: the finer is the grid, the higher the branching factor, and thus the computational time and the required memory to execute a graph traversal algorithm.

<!-- chunk {"id": "body-0019", "role": "body", "section": "Contribution of the paper", "weight": 1.0} -->

The main contribution of this paper is proposing an algorithm, called ${\mathtt{R}\mathtt{R}\mathtt{T}}^{\star}\ {\mathtt{M}\mathtt{o}\mathtt{t}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{P}\mathtt{r}\mathtt{i}\mathtt{m}\mathtt{i}\mathtt{t}\mathtt{i}\mathtt{v}\mathtt{e}\mathtt{s}}$, which extends RRT^⋆^ by introducing a database of pre-computed motion primitives in order to avoid the online solution of a constrained TPBVP for the edge computation. The database is composed of a set of trajectories, each one connecting an initial state to a final one in a suitably defined grid.

<!-- chunk {"id": "body-0020", "role": "body", "section": "Contribution of the paper", "weight": 1.0} -->

By sampling in the gridded state space, the implementation of the steering function adopted for growing and rewiring the RRT^⋆^ tree reduces to the search of a motion primitive in a pre-computed Look Up Table (LUT).\The proposed approach is applicable to any dynamical system described by differential equations and subject to analytical constraints, for which edge design can be formulated as a TPBVP. Notably, when a model of the robot is not available, the database can be derived directly from experimental trajectories.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Contribution of the paper", "weight": 1.0} -->

The main difference of the proposed approach, with respect to existing algorithms that use a database of pre-computed trajectories, e.g., search based approaches as, is that it leverages on a dynamic tree whose size depends only on the number of samples, but not on the number of motion primitives that affects the accuracy in the approximation of the robot kinematic and dynamic characteristics. As a consequence, memory consumption to store the tree and computation time to determine a solution on a given tree can be bounded selecting an appropriate maximum number of samples, without introducing undesired constraints in the robot action space.\Search based approaches, instead, have to strongly limit the action space, keeping the number of motion primitives low, as the branching factor of the graph, i.e., the number of edges generated expanding each node, depends on the size of the database.

<!-- chunk {"id": "body-0022", "role": "body", "section": "Contribution of the paper", "weight": 1.0} -->

The effectiveness of ${\mathtt{R}\mathtt{R}\mathtt{T}}^{\star}\ {\mathtt{M}\mathtt{o}\mathtt{t}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{P}\mathtt{r}\mathtt{i}\mathtt{m}\mathtt{i}\mathtt{t}\mathtt{i}\mathtt{v}\mathtt{e}\mathtt{s}}$ has been validated in simulation, showing that the time required to build the tree is greatly reduced with the introduction of a LUT. This represents a promising result for online applications, especially in dynamic environments where the planner has to generate a new trajectory in response to changes in the obstacle-free state space.

<!-- chunk {"id": "body-0023", "role": "body", "section": "Contribution of the paper", "weight": 1.0} -->

An analysis of the probabilistic completeness and optimality properties of ${\mathtt{R}\mathtt{R}\mathtt{T}}^{\star}\ {\mathtt{M}\mathtt{o}\mathtt{t}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{P}\mathtt{r}\mathtt{i}\mathtt{m}\mathtt{i}\mathtt{t}\mathtt{i}\mathtt{v}\mathtt{e}\mathtt{s}}$ is also provided. This involves a two-step procedure where we assess how close the proposed sample-based solution gets to the optimal one in the gridded state space as the number of samples grows to infinity, and how it gets close to the optimal solution in the continuous state space as the gridding gets finer and finer.

<!-- chunk {"id": "body-0024", "role": "body", "section": "Paper structure", "weight": 1.0} -->

The paper is organized as follows. Section 2 introduces a formal description of the problem. In Section 3 the proposed ${\mathtt{R}\mathtt{R}\mathtt{T}}^{\star}\ {\mathtt{M}\mathtt{o}\mathtt{t}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{P}\mathtt{r}\mathtt{i}\mathtt{m}\mathtt{i}\mathtt{t}\mathtt{i}\mathtt{v}\mathtt{e}\mathtt{s}}$ algorithm is explained in detail.

<!-- chunk {"id": "body-0025", "role": "body", "section": "Paper structure", "weight": 1.0} -->

An analysis of its probabilistic completeness and optimality properties is presented in Section 4. A numerical validation of ${\mathtt{R}\mathtt{R}\mathtt{T}}^{\star}\ {\mathtt{M}\mathtt{o}\mathtt{t}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{P}\mathtt{r}\mathtt{i}\mathtt{m}\mathtt{i}\mathtt{t}\mathtt{i}\mathtt{v}\mathtt{e}\mathtt{s}}$ is provided in Section 5. Finally, some concluding remarks are drawn in Section 6.

<!-- chunk {"id": "body-0026", "role": "body", "section": "PROBLEM STATEMENT", "weight": 1.0} -->

In this work, dynamical systems with state vector $\mathbf{q} \in {\mathbb{R}}^{d}$ and control input $\mathbf{u} \in {\mathbb{R}}^{m}$, governed by where $f$ is continuously differentiable as a function of both arguments, are considered. The control input $\mathbf{u}{(t)}$ is subject to actuation constraints, and the admissible control space is denoted as $U \subset {\mathbb{R}}^{m}$. The state $\mathbf{q}{(t)}$ is constrained in the set $Q \subset {\mathbb{R}}^{d}$, and initialized with ${\mathbf{q}{}} = \mathbf{q}_{0} \in Q$. Both $U$ and $Q$ are assumed to be compact. An open subset $Q_{goal}$ of $Q$ represents the goal region that the state has to reach.

<!-- chunk {"id": "body-0027", "role": "body", "section": "PROBLEM STATEMENT", "weight": 1.0} -->

A *trajectory* of system is defined by the tuple $\mathbf{z} = \left( {\mathbf{q}{( \cdot )}},{\mathbf{u}{( \cdot )}},\tau \right)$, where $\tau$ is the duration of the trajectory, and ${\mathbf{q}{( \cdot )}}:{{\lbrack 0,\tau\rbrack}\rightarrow Q}$ and ${\mathbf{u}{( \cdot )}}:{{\lbrack 0,\tau\rbrack}\rightarrow U}$ define the state and control input evolution along the time interval $\lbrack 0,\tau\rbrack$, satisfying the differential equation for $t \in {\lbrack 0,\tau\rbrack}$, the initial condition ${\mathbf{q}{}} = \mathbf{q}_{0}$, and the final condition ${\mathbf{q}{(\tau)}} \in

<!-- chunk {"id": "body-0028", "role": "body", "section": "PROBLEM STATEMENT", "weight": 1.0} -->

Obstacles are represented via an open subset $Q_{obs}$ of $Q$. The free space is then defined as $Q_{free}:={Q \smallsetminus Q_{obs}}$, and the assumption $\mathbf{q}_{0} \in Q_{free}$ is enforced.\A trajectory $\mathbf{z} = \left({\mathbf{q}{(\cdot)}},{\mathbf{u}{(\cdot)}},\tau \right)$ of system is said to be *collision free*, if it avoids collisions with obstacles, i.e., ${\mathbf{q}{(t)}} \in Q_{free}$, $t \in {\lbrack 0,\tau\rbrack}$.\The set of collision free trajectories is denoted as $Z_{free}$.

<!-- chunk {"id": "body-0029", "role": "body", "section": "PROBLEM STATEMENT", "weight": 1.0} -->

An *optimal kinodynamic motion planning problem* can then be formalized as finding a feasible and collision free trajectory $\mathbf{z}^{\star} = \left({\mathbf{q}^{\star}{(\cdot)}},{\mathbf{u}^{\star}{(\cdot)}},\tau^{\star} \right) \in Z_{free}$ that is *optimal* according to a cost criterion ${J{(\mathbf{z})}}:{Z_{free}\rightarrow{\mathbb{R}}_{\geq 0}}$ that is expressed as where $g:{{Q \times U}\rightarrow{\mathbb{R}}_{\geq 0}}$ is an instantaneous cost function. We assume that trajectories joining two different states have a non-zero cost.

<!-- chunk {"id": "body-0030", "role": "body", "section": "PROBLEM STATEMENT", "weight": 1.0} -->

This is for instance the case in minimum time optimization where ${g{(\mathbf{q},\mathbf{u})}} = 1$ and the trajectory duration $\tau$ is one of the optimization variables of the problem.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Remark 1 (translation invariance property)", "weight": 1.0} -->

In the context of motion planning, system represents the robot equations of motion and, consequently, its state vector $\mathbf{q}$ includes the robot position with respect to a given absolute reference frame. In the following, a translation invariance property is supposed to hold. This means that, if obstacles are neglected and a pair of initial and final states and the associated optimal trajectory $\mathbf{z}^{\star} = \left( {\mathbf{q}^{\star}{( \cdot )}},{\mathbf{u}^{\star}{( \cdot )}},\tau^{\star} \right)$ are considered, by shifting the origin of the coordinate system and rewriting all relevant quantities -- including system dynamics, and initial and final states -- in the new coordinate system and applying input $\mathbf{u}^{\star}{( \cdot )}$, the optimal robot trajectory is obtained, which is $\mathbf{z}^{\star}$ rewritten in the new coordinates.

<!-- chunk {"id": "body-0032", "role": "body", "section": "RRT^⋆^ WITH MOTION PRIMITIVES", "weight": 1.0} -->

The approach here proposed is based on previous works on search-based, and sampling-based methods, and combines them in a novel way.\In particular, it relies on a uniform discretization of the state space, and on the computation of a finite set of motion primitives by solving a constrained optimization problem with boundary conditions on the grid points of a smaller (uniform) grid. The motion primitives are then embedded in the RRT^⋆^ algorithm, where they are used to connect the randomly generated nodes to the tree, thus eliminating the need of solving online challenging and time consuming TPBVPs.

<!-- chunk {"id": "body-0033", "role": "body", "section": "Database of Motion Primitives", "weight": 1.0} -->

The database of motion primitives is built by gridding the continuous state space in order to obtain a finite set of boundary conditions (initial and final states), and by solving offline a constrained boundary value optimization problem for each pair. The resulting set of optimal trajectories is then used repeatedly online, implementing a procedure that, when an edge connecting two nodes is requested by the planner, simply picks up from the database a suitable trajectory.

<!-- chunk {"id": "body-0034", "role": "body", "section": "Database of Motion Primitives", "weight": 1.0} -->

Note that, thanks to the translation invariance property introduced in Remark 1. ‣ 2 PROBLEM STATEMENT ‣ Sampling-based optimal kinodynamic planning with motion primitives"), the size of the database can be kept small while covering a wide range of the space where the robot is moving. Indeed, one can, without loss of generality, set the initial position ${\overline{\mathbf{π}}}_{0}$ to ${\overline{\mathbf{π}}}_{0} = 0$ when building the database, and recover the optimal trajectory for an arbitrary initial position ${\mathbf{π}}_{0}$ by simply centring the coordinate system in ${\mathbf{π}}_{0}$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "Example 1", "weight": 1.0} -->

Consider, as an example, a planning problem for a unicycle robot characterised by a 3D search space $(x,y,\theta)$, including the position $(x,y)$ and the orientation $\theta$, and by a 2D actuation space $(v,\omega)$, constituted by the linear velocity $v$ and the angular velocity $\omega$.\Motion primitives are computed solving the following TPBVP for different initial and final poses.\Figure 1 shows a subset of these motion primitives, characterized by trajectories starting from ${\overline{x}}_{0} = {\overline{y}}_{0} = {\overline{\theta}}_{0} = 0$.\As can be seen in Figure 1, with the dynamical system and cost function considered in this example, motion primitives, corresponding to boundary conditions that are symmetric with respect to the $x$-axis, are symmetric. A further analysis reveals that the same property holds for the $y$-axis as well, and that symmetric primitives are characterized by the same cost.

<!-- chunk {"id": "body-0036", "role": "body", "section": "Remark 2", "weight": 1.0} -->

When for the considered dynamical system and cost criterion stronger invariance properties hold, like the axis symmetry in Example 1, the size of the database can be further reduced by storing only a few "reference trajectories", and generating all the others using the invariance transformation.\Figure 2 shows an example, referred to the TPBVP considered in Example 1, where the trajectories represented by the pairs $(\mathbf{q}_{0},\mathbf{q}_{f}^{1})$, $(\mathbf{q}_{0},\mathbf{q}_{f}^{2})$, $(\mathbf{q}_{0},\mathbf{q}_{f}^{3})$ are characterised by the same cost and can be easily mapped to a "reference trajectory" corresponding to the boundary value pair $\left(\mathbf{q}_{0},\mathbf{q}_{f} \right)$. In this case, the size of the database can be further reduced storing only the "reference trajectory".\

<!-- chunk {"id": "body-0037", "role": "body", "section": "Search Space design", "weight": 1.0} -->

In order to take advantage of the pre-computed database of motion primitives in sampling-based planning, the search space of the planner has to be defined appropriately so that every time the planner needs to connect two nodes, the corresponding optimal trajectory can be found in the database. To guarantee that this is indeed the case, the search space of the planner is uniformly gridded as the region where motion primitives are built. The translation invariance property^11^1This approach can be easily extended in case stronger invariance properties hold. can then be exploited, as any optimal trajectory which connects a pair of initial and final states (in the discretized search space) can be computed by first shifting the initial and final states so that the initial robot position corresponds to the zero position, then picking a suitable motion primitive in the database, and finally shifting the motion primitive so as to get back to the original reference coordinate system. Translation invariance, jointly with uniform gridding, allow a reduced number of motion primitives to cover the entire (discretized) search space. Note that, as the resolution of the database and the uniform grid size of the search space are coupled, we often use these two terms interchangeably.

<!-- chunk {"id": "body-0038", "role": "body", "section": "Search Space design", "weight": 1.0} -->

Determining optimal state space discretization depends on the specific application, and is out of the scope of this work. We shall assume here that the state space grid should include the initial state $\mathbf{q}_{0}$, at least a grid point in the goal region, and few points in the free space $Q_{free}$. Moreover, in order to find a solution that reaches the goal region, the algorithm should be able to search within all homotopy classes that are feasible given the robot footprint. In other words, one should be able to represent in the grid space all sets of trajectories in the continuous state space that can be obtained applying a smooth transformation and lead to the goal region. Missing a homotopy class could highly deteriorate performance in terms of achieved cost.\In Section 5 some numerical examples are provided, in which different grids are used for solving the same case study and results are compared.

<!-- chunk {"id": "body-0039", "role": "body", "section": "Search Space design", "weight": 1.0} -->

3 qrand ← SAMPLE (Qfree) 4 Qnear ← NEAR _ NODES (qrand) 5 qbest ← EXTEND (Qnear, qrand) 10 ET ← REWIRE (QT, ET, qrand, Qnear) 15 ET ← REWIRE (QT, ET, qrand, Qnear) Algorithm 1 RRT⋆ MotionPrimitives

<!-- chunk {"id": "body-0040", "role": "body", "section": "Motion Planning", "weight": 1.0} -->

This section introduces ${\mathtt{R}\mathtt{R}\mathtt{T}}^{\star}\ {\mathtt{M}\mathtt{o}\mathtt{t}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{P}\mathtt{r}\mathtt{i}\mathtt{m}\mathtt{i}\mathtt{t}\mathtt{i}\mathtt{v}\mathtt{e}\mathtt{s}}$ (Algorithm 1), the proposed variant of RRT^⋆^ integrating the database of motion primitives for the computation of a collision-free optimal trajectory (cf. Section 2).

<!-- chunk {"id": "body-0041", "role": "body", "section": "Motion Planning", "weight": 1.0} -->

Nodes are states and edges are optimal trajectories, each one connecting a pair of origin and destination nodes and solving the TPBVP.\The tree $T$ is expanded for a maximum number of iterations $N$, defined by the user, starting from $Q_{T} = {\{\mathbf{q}_{0}\}}$, where $\mathbf{q}_{0} \in Q_{free}$ is the initial state, and $E_{T} = \varnothing$, as described in Algorithm 1.\Every node $\mathbf{q} \in Q_{T}$ is connected to $\mathbf{q}_{0}$ via a single sequence of intermediate nodes $\mathbf{q}_{i} \in Q_{T}$, $i = {1,\ldots,{n - 1}}$, $n \leq N$, and associated edges $e_{i} = e_{\mathbf{q}_{i},\mathbf{q}_{i + 1}} \in

<!-- chunk {"id": "body-0042", "role": "body", "section": "Motion Planning", "weight": 1.0} -->

Algorithm 2 NEAR _ NODES Tree growing is based on four main steps -- random sampling, finding near nodes, extending the tree, and rewiring -- that are described in the following.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Random sampling", "weight": 1.0} -->

A random state $\mathbf{q}_{rand}$ is sampled from the free state space $Q_{free}$ according to a uniform distribution by ${\mathtt{S}\mathtt{A}\mathtt{M}\mathtt{P}\mathtt{L}\mathtt{E}}\left( Q_{free} \right)$. Unlike the original RRT^⋆^ algorithm, however, the node is not sampled from the continuous state space, but from its discretization according to a uniform grid. For this reason, there is also a non zero probability that the same state $\mathbf{q}_{rand}$ is sampled again in the next iterations of the algorithm.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Near nodes (Algorithm 2)", "weight": 1.0} -->

In RRT^⋆^ a random state $\mathbf{q}_{rand}$ can be connected only to a node that is within the set of its near nodes.\For Euclidean cost metrics, the set of near nodes is defined as a $d$-dimensional ball centered at $\mathbf{q}_{rand}$ of radius where $n$ is the tree cardinality at the current iteration of the algorithm and $\gamma_{RRT^{\star}}$ is a suitable constant selected as $\mu{(Q_{free})}$ and $\zeta_{d}$ denoting the volume of the free configuration space and of the unit ball, respectively, in a $d$-dimensional Euclidean space.\For non-Euclidean cost metrics, the distance between two states is represented by the optimal cost of the trajectory that connects them, and near nodes are selected from a set of reachable states, $Q_{reach}$, defined as the set of states that can be reached from $\mathbf{q}_{rand}$ or that can reach $\mathbf{q}_{rand}$ with a cost that

<!-- chunk {"id": "body-0045", "role": "body", "section": "Near nodes (Algorithm 2)", "weight": 1.0} -->

(c) inverse transformation and edge design Figure 3: Steps involved in the coordinate transformation within the FindTrajectory procedure.

<!-- chunk {"id": "body-0046", "role": "body", "section": "Near nodes (Algorithm 2)", "weight": 1.0} -->

In ${\mathtt{R}\mathtt{R}\mathtt{T}}^{\star}\ {\mathtt{M}\mathtt{o}\mathtt{t}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{P}\mathtt{r}\mathtt{i}\mathtt{m}\mathtt{i}\mathtt{t}\mathtt{i}\mathtt{v}\mathtt{e}\mathtt{s}}$, however, the set $Q_{reach}$ has to be further constrained to ensure that there is a pre-computed trajectory in the database for each connection in the set of near nodes, that is thus redefined as follows where

<!-- chunk {"id": "body-0047", "role": "body", "section": "Near nodes (Algorithm 2)", "weight": 1.0} -->

${\mathtt{B}\mathtt{o}\mathtt{u}\mathtt{n}\mathtt{d}\mathtt{i}\mathtt{n}\mathtt{g}\mathtt{B}\mathtt{o}\mathtt{x}}{({\mathbf{π}}_{rand})}$ denotes the box of grid points in the state space $Q$ adopted for the database construction, with the origin of the reference coordinate system shifted from ${\overline{\pi}}_{0} = 0$ to $\pi_{rand}$, which is the robot position associated to state $\mathbf{q}_{rand}$ and obtained by using $\mathtt{G}\mathtt{e}\mathtt{t}\mathtt{P}\mathtt{o}\mathtt{s}\mathtt{i}\mathtt{t}\mathtt{i}\mathtt{o}\mathtt{n}$.\If $Q_{near}$ occurs to be an empty set, the algorithm continues

<!-- chunk {"id": "body-0048", "role": "body", "section": "Near nodes (Algorithm 2)", "weight": 1.0} -->

to the next iteration selecting a new $\mathbf{q}_{rand}$.

<!-- chunk {"id": "body-0049", "role": "body", "section": "Extend (Algorithm 3 ‣ 3.3 Motion Planning ‣ 3 RRT⋆ WITH MOTION PRIMITIVES ‣ Sampling-based optimal kinodynamic planning with motion primitives\"))", "weight": 1.0} -->

The tree is extended to include $\mathbf{q}_{rand}$ by selecting the node $\mathbf{q}_{best} \in Q_{T}$ such that the edge $e_{\mathbf{q}_{best},\mathbf{q}_{rand}}$ connects $\mathbf{q}_{rand}$ with a minimum cost collision free trajectory.\$\mathbf{q}_{best}$ is determined as follows where $Q_{feasible} \subseteq Q_{near}$ is the set of nodes $\mathbf{q}$ that belong to $Q_{near}$ and such that the trajectory connecting $\mathbf{q}$ to $\mathbf{q}_{rand}$ is collision free, i.e., where

<!-- chunk {"id": "body-0050", "role": "body", "section": "Extend (Algorithm 3 ‣ 3.3 Motion Planning ‣ 3 RRT⋆ WITH MOTION PRIMITIVES ‣ Sampling-based optimal kinodynamic planning with motion primitives\"))", "weight": 1.0} -->

Sampling-based optimal kinodynamic planning with motion primitives")), obtaining the normalized pair $\left(\overset{\sim}{\mathbf{q}},{\overset{\sim}{\mathbf{q}}}_{rand} \right)$, such that the resulting $\overset{\sim}{\mathbf{q}}$ has the position $\overset{\sim}{\mathbf{π}}$ corresponding to the null vector (Figure 3(b) ‣ 3.3 Motion Planning ‣ 3 RRT⋆ WITH MOTION PRIMITIVES ‣ Sampling-based optimal kinodynamic planning with motion primitives")); a query is executed on the database to look for the trajectory $\mathbf{z}_{i} \in \mathcal{Z}$ and the cost ${C{(e_{\overset{\sim}{\mathbf{q}},{\overset{\sim}{\mathbf{q}}}_{rand}})}} \in {\mathbb{R}}$; the inverse of the previous translation is

<!-- chunk {"id": "body-0051", "role": "body", "section": "Extend (Algorithm 3 ‣ 3.3 Motion Planning ‣ 3 RRT⋆ WITH MOTION PRIMITIVES ‣ Sampling-based optimal kinodynamic planning with motion primitives\"))", "weight": 1.0} -->

applied in order to recover the trajectory connecting the actual pair of boundary values $\left(\mathbf{q},\mathbf{q}_{rand} \right)$, determining the edge $e_{\mathbf{q},\mathbf{q}_{rand}}$ (Figure 3(c) ‣ 3.3 Motion Planning ‣ 3 RRT⋆ WITH MOTION PRIMITIVES ‣ Sampling-based optimal kinodynamic planning with motion primitives")).

<!-- chunk {"id": "body-0052", "role": "body", "section": "Extend (Algorithm 3 ‣ 3.3 Motion Planning ‣ 3 RRT⋆ WITH MOTION PRIMITIVES ‣ Sampling-based optimal kinodynamic planning with motion primitives\"))", "weight": 1.0} -->

1 qbest ← ⌀, ebest ← ⌀, cbest ← ∞ 3 z, C (eq, qrand) ← FindTrajectory (q, qrand) 4 if C (eq, qrand) < cbest then 5 if CollisionFree (eq, qrand) then 2 z, C (eqrand, q) ← FindTrajectory (qrand, q) 4 if CollisionFree (eq, qrand) then

<!-- chunk {"id": "body-0053", "role": "body", "section": "Rewiring (Algorithm 4 ‣ 3.3 Motion Planning ‣ 3 RRT⋆ WITH MOTION PRIMITIVES ‣ Sampling-based optimal kinodynamic planning with motion primitives\"))", "weight": 1.0} -->

In order to ensure that all node pairs are connected by an optimal sequence of edges, every time a new node $\mathbf{q}_{rand}$ is added to the tree, a check is performed to verify if an already existing node can be reached from this newly added node with a smaller cost.\Therefore, ${\forall\mathbf{q}} \in Q_{near}$ if $e_{\mathbf{q}_{rand},\mathbf{q}}$ is collision free, and the following conditions hold the tree is rewired, i.e., where $e_{prev}$ is the previous edge connecting the node $\mathbf{q}$ to the tree.

<!-- chunk {"id": "body-0054", "role": "body", "section": "Termination and best sequence selection", "weight": 1.0} -->

After the maximum number of iterations is reached the procedure to build the tree terminates.\The best trajectory is selected as the node sequence reaching the goal region with the minimum cumulative cost $C$.\Note that, using a discretized search space limits the number of nodes that can be sampled, once all of them have been sampled the tree cardinality does not increase any more, but the algorithm can still continue updating the edges to ensure that each node is connected with the best possible parent node.

<!-- chunk {"id": "body-0055", "role": "body", "section": "COMPLETENESS AND OPTIMALITY ANALYSIS", "weight": 1.0} -->

In this section, probabilistic completeness of the proposed planning algorithm and optimality of the solution are discussed. Furthermore, some results to assess how close the solution obtained using a discretized state space and motion primitives is to the optimal trajectory computed considering a continuous state space are provided.

<!-- chunk {"id": "body-0056", "role": "body", "section": "COMPLETENESS AND OPTIMALITY ANALYSIS", "weight": 1.0} -->

Let $Q^{\Delta}$ define the set of grid points that represent the discretized state space^22^2In this section, a $\Delta$ superscript is used to denote all variables that are associated with the grid state space, so as to distinguish them from their continuous state space counterpart. and similarly $Q_{free}^{\Delta}:={Q^{\Delta} \cap Q_{free}}$ represents the free discrete state space. Assuming that the discretization step size is chosen properly, then, the collection of all grid points $\mathbf{q} \in Q_{free}^{\Delta}$ that can be reached from $\mathbf{q}_{0}$ by concatenating a sequence of motion primitives in $Q_{free}$ is a non empty set. We shall denote this set as $V_{free}^{\Delta}$ and its cardinality as $N^{\Delta}$.

<!-- chunk {"id": "body-0057", "role": "body", "section": "COMPLETENESS AND OPTIMALITY ANALYSIS", "weight": 1.0} -->

Note that the end points of the concatenated motion primitives are grid points in $Q_{free}^{\Delta}$ and hence they belong to $V_{free}^{\Delta}$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "COMPLETENESS AND OPTIMALITY ANALYSIS", "weight": 1.0} -->

Let $\mathcal{G}_{free}^{\Delta} = {(V_{free}^{\Delta},E_{free}^{\Delta})}$ be a graph where the set of nodes is given by $V_{free}^{\Delta}$ defined before and the set of edges $E_{free}^{\Delta}$ is the collection of all the (possibly translated) motion primitives iteratively built as follows: starting from $\mathbf{q}_{0}$ consider all the (translated) motion primitives that lie in $Q_{free}$ and connect $\mathbf{q}_{0}$ to all possible grid points in $Q_{free}^{\Delta}$, and, then, continue with the same strategy for all of the newly reached grid points iteratively until it is not possible to further expand the graph.

<!-- chunk {"id": "body-0059", "role": "body", "section": "COMPLETENESS AND OPTIMALITY ANALYSIS", "weight": 1.0} -->

Finally, $Q_{goal}^{\Delta}$ denotes the set of those grid points of $V_{free}^{\Delta}$ that belong to $Q_{goal}$. The motion planning problem using the grid representation admits a solution if $Q_{goal}^{\Delta}$ is not empty since this means that there exists a way of reaching a state in $Q_{goal}$ starting from $\mathbf{q}_{0}$ with the available motion primitives. In the following derivations we assume that $Q_{goal}^{\Delta} \neq \varnothing$.

<!-- chunk {"id": "body-0060", "role": "body", "section": "COMPLETENESS AND OPTIMALITY ANALYSIS", "weight": 1.0} -->

However, unlike RRT^⋆^, the nodes and edges added to the tree belong respectively to $V_{free}^{\Delta}$ and $E_{free}^{\Delta}$, so that the obtained tree $T$ is a sub-graph of $\mathcal{G}_{free}^{\Delta}$, i.e., $T \subset \mathcal{G}_{free}^{\Delta}$. The subscript $i$ is used to denote the generated tree and the cost of the lowest cost trajectory represented in that tree after $i$-th iterations, i.e., $T_{i}$ and $c_{i}$, respectively.

<!-- chunk {"id": "body-0061", "role": "body", "section": "COMPLETENESS AND OPTIMALITY ANALYSIS", "weight": 1.0} -->

Let $c^{\star \Delta}$ denote the cost of this optimal trajectory, i.e., ${C\mspace{7mu}{({\rightarrow\mathbf{q}_{k}^{\star}})}} = c^{\star \Delta}$, which is named *resolution optimal $\Delta$-cost*.

<!-- chunk {"id": "body-0062", "role": "body", "section": "COMPLETENESS AND OPTIMALITY ANALYSIS", "weight": 1.0} -->

However, this can still be an issue due to the combinatorial nature of the problem, in particular due to the branching caused by the dimensionality of the state space and the number of nodes contained in the graph.

<!-- chunk {"id": "body-0063", "role": "body", "section": "COMPLETENESS AND OPTIMALITY ANALYSIS", "weight": 1.0} -->

In this section the quality of the solution obtained by ${\mathtt{R}\mathtt{R}\mathtt{T}}^{\star}\ {\mathtt{M}\mathtt{o}\mathtt{t}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{P}\mathtt{r}\mathtt{i}\mathtt{m}\mathtt{i}\mathtt{t}\mathtt{i}\mathtt{v}\mathtt{e}\mathtt{s}}$ is analyzed by addressing the following questions: resolution optimality: if there exists a resolution optimal $\Delta$-trajectory $S^{\star}$ in $\mathcal{G}_{free}^{\Delta}$, then, is it possible to obtain such a trajectory? asymptotic optimality: how close is the resolution optimal $\Delta$-cost to the cost of the optimal trajectory, as the grid resolution increases and the grid converges to the continuous state space?

<!-- chunk {"id": "body-0064", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The following properties hold for the dynamical system in the system is small-time locally attainable (STLA)^33^3A system is STLA from a state $\mathbf{q} \in Q$ if ${\forall T} > 0$ the reachable set of states from $q$ in time $0 < t \leq T$, $\mathcal{R}{(\mathbf{q}, \leq T)}$ contains a d-dimensional subset of $\mathcal{N}$, where $\mathcal{N}$ denotes the set of neighborhood states in terms of Euclidean distance,.; function $f{(\cdot)}$, representing the system dynamics, is Lipschitz continuous with Lipschitz constant $\mathcal{K}_{f}$; function $C{(\cdot)}$, assigning a cost to an edge, satisfies the following Lipschitz-like continuity condition with Lipschitz constant $\mathcal{K}_{c}$: for each pair of edges

<!-- chunk {"id": "body-0065", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

Derivations in the rest of this section apply straightforwardly to state spaces that are Euclidean, and can be generalized to state spaces that are manifolds if the following assumption holds.

<!-- chunk {"id": "body-0066", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The state space manifold of system with $d$ state variables is a subspace of the $d$-dimensional Euclidean space, ${\mathbb{R}}^{d}$, therefore can be locally treated as ${\mathbb{R}}^{d}$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

With a slight abuse of the previously introduced notation, in the rest of this section we use the term "trajectory" for the state space component of the tuple $\mathbf{z}$ defined in Section 2. In order to compare the trajectory returned by ${\mathtt{R}\mathtt{R}\mathtt{T}}^{\star}\ {\mathtt{M}\mathtt{o}\mathtt{t}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{P}\mathtt{r}\mathtt{i}\mathtt{m}\mathtt{i}\mathtt{t}\mathtt{i}\mathtt{v}\mathtt{e}\mathtt{s}}$ and the optimal trajectory in the continuous state space, firstly, trajectories whose points are all away from obstacles by a certain distance are considered. For this reason, the definition of obstacle clearance of a trajectory, i.e., the minimum distance between obstacles and points belonging to the trajectory, has to be introduced.

<!-- chunk {"id": "body-0068", "role": "body", "section": "NUMERICAL EXAMPLE", "weight": 1.0} -->

In this section a numerical example is presented to show the effectiveness of the proposed algorithm.\A 4D state-space $(x,y,\theta,v)$ representing a unicycle like robot moving on a planar surface is considered. The robot is described by the following equations where $(x,y)$ is the position of the robot and $\theta$ the orientation with respect to a global reference frame, $v$ and $w$ are the linear and angular velocity, respectively. The control input is represented by $\mathbf{u} = {\lbrack w,a\rbrack}^{T}$, where $w$ and $a$ are angular velocity and linear acceleration, respectively.

<!-- chunk {"id": "body-0069", "role": "body", "section": "NUMERICAL EXAMPLE", "weight": 1.0} -->

The motion primitives in the database are computed for each pair of initial and final state, $\mathbf{q}_{0} = {\lbrack x_{0},y_{0},\theta_{0},v_{0}\rbrack}$ and $\mathbf{q}_{f} = {\lbrack x_{f},y_{f},\theta_{f},v_{f}\rbrack}$, solving the TPBVP in for the differential equations given in and the cost function that minimizes the total time of the trajectory $\tau$, penalizing the total actuation effort with a weight $R = {0.5I_{2}}$.

<!-- chunk {"id": "body-0070", "role": "body", "section": "NUMERICAL EXAMPLE", "weight": 1.0} -->

The control variables $a$ and $w$ are bounded as $a \in {{\lbrack{- 3},3\rbrack}\text{m/s}^{2}}$, $w \in {{\lbrack{- 5},5\rbrack}\text{rad/s}}$.\TPBVPs are solved using MATLAB toolbox GPOPS, a nonlinear optimization tool based on the Gauss pseudo-spectral collocation method.

<!-- chunk {"id": "body-0071", "role": "body", "section": "NUMERICAL EXAMPLE", "weight": 1.0} -->

Three databases based on different grids have been considered. For all of them the initial state is characterised by the same position ${(x_{0},y_{0})} = {}$.\The first database is based on a coarse resolution uniform square grid (Figure 8(a)), where ${(x_{f},y_{f})} \in {{{\lbrack{- 2},2\rbrack} \times {\lbrack{- 2},2\rbrack}} \smallsetminus {\{{}\}}}$ and each square cell has a size of one meter. The initial orientation $\theta_{0}$ is selected among three values ${\{ 0,{\pi/4},{\pi/2}\}}\text{rad}$, the final orientation $\theta_{f}$ can take 8 equally spaced values in the range ${\lbrack 0,{2\pi})}\text{rad}$.

<!-- chunk {"id": "body-0072", "role": "body", "section": "NUMERICAL EXAMPLE", "weight": 1.0} -->

For the initial and final velocities, $v_{0}$ and $v_{f}$, a minimum and a maximum velocity of $1\text{m/s}$ and $4\text{m/s}$ is considered.\The second database is based on a fine resolution uniform square grid (Figure 8(b)), where ${(x_{f},y_{f})} \in {{{\lbrack{- 2},2\rbrack} \times {\lbrack{- 2},2\rbrack}} \smallsetminus {\{{}\}}}$ and each square cell has a size of half a meter. The initial and final orientations can take 24 equally spaced values in the range ${\lbrack 0,{2\pi})}\text{rad}$.

<!-- chunk {"id": "body-0073", "role": "body", "section": "NUMERICAL EXAMPLE", "weight": 1.0} -->

The initial and final velocities are selected among 5 equally spaced values in the range ${\lbrack 0,4\rbrack}\text{m/s}$.\Finally, the third database is based on a uniform diamond grid (Figure 8(c)), characterised by the same initial and final states as the previous one, plus some additional final states at ${(x_{f},y_{f})} \in {{\lbrack{- 1.75},1.75\rbrack} \times {\lbrack{- 1.75},1.75\rbrack}}$ with a discretization step of half a meter in each direction. These additional states are characterized by the same orientation and velocity of the rest of the database.

<!-- chunk {"id": "body-0074", "role": "body", "section": "NUMERICAL EXAMPLE", "weight": 1.0} -->

Simulations are performed on an IntelCore i7@2.40 GHz personal computer with 8Gb RAM and the algorithm has been implemented in MATLAB.\An indoor map is considered (Figures 10-12), setting the robot initial pose at $\left(1,0,{\pi/2} \right)$ with zero velocity. The goal area is defined as a square of half a meter side and centred at $$. The robot should stop at the end of the trajectory.

<!-- chunk {"id": "body-0075", "role": "body", "section": "NUMERICAL EXAMPLE", "weight": 1.0} -->

Figures 10-12 show the trees and the optimal trajectories obtained for different number of iterations and for the three different gridding strategies. Correspondingly, Figure 9 shows the velocity and the actuation profiles for the optimal trajectories computed with 3000 and 50000 iterations, and reported in Figures 10(c), 11(c) and 12(c), clearly demonstrating that the velocity constraint and the actuation bounds are satisfied. Note that the velocity profile that corresponds to the coarse resolution square gridding exhibits a jerky acceleration behaviour, due to the fact that the velocity at each node is constrained to be exactly one of the values in the database. This demonstrates that the velocity discretization step has to be accurately selected if a smoother velocity profile is required.

<!-- chunk {"id": "body-0076", "role": "body", "section": "NUMERICAL EXAMPLE", "weight": 1.0} -->

The same planning problem has been solved for 10 independent simulation runs. Figure 13 shows the average cost evolutions related to the coarse resolution, fine resolution and diamond gridding, as the number of iterations increases. As expected, the cost reduces increasing the number of iterations, and converges to the *resolution optimal $\Delta$-cost*: once this minimum is achieved the solution will not further improve.\As can be easily seen, motion primitives computed using a denser grid provide lower cost plans. Moreover, the resolution optimal $\Delta$-cost achieved using the fine resolution square and diamond grids are similar, demonstrating that the choice of the discretization step is strictly related to the specific problem. Finally, it is worth mentioning that as the resolution of the grid increases, the cardinality of $Q_{free}^{\Delta}$ increases as well, slowing down the convergence to the resolution optimal $\Delta$-cost.

<!-- chunk {"id": "body-0077", "role": "body", "section": "NUMERICAL EXAMPLE", "weight": 1.0} -->

In order to assess the impact of the grid resolution on the size of the search space, in Table 1 we report the number of nodes corresponding to the grids of the three adopted databases (see Figure 8), together with the corresponding minimum and maximum branching factors, i.e., the number of neighbors that each node is connected to. The computed number of nodes is an upper bound on the cardinality of $\mathcal{G}_{free}^{\Delta}$. Yet, from the figures in Table 1, it should be clear the combinatorial nature of the problem, which makes it hard building the whole graph of motion primitives and applying a graph search. As a matter of fact, the most commonly used lattice-based approaches use graph search algorithms that resort to some heuristic (see for example dynamic A^⋆^ (D^⋆^) and anytime repairing A^⋆^ (ARA^⋆^) by Stentz and Likhachev et al respectively).

<!-- chunk {"id": "body-0078", "role": "body", "section": "NUMERICAL EXAMPLE", "weight": 1.0} -->

It is also worth mentioning that the resulting computation time is promising, even for online replanning in the case of dynamic and partially known environments. Code optimisation and a C/C++ implementation can be considered for a further speed up.

<!-- chunk {"id": "body-0079", "role": "body", "section": "NUMERICAL EXAMPLE", "weight": 1.0} -->

To better emphasize the advantage of using a precomputed database, we report in Figure 16 the histogram of the computation time for solving a single TPBVP of the considered example using the GPOPS commercial numerical solver. As can be seen from this figure, it typically takes around 400 ms to get a solution for a single TPBVP while a trajectory can be extracted from the database in a time of the order of 0.01 ms (values ranged between 0.008 ms and 0.015 ms over 100 trials). Note that at each iteration of the standard ${\mathtt{R}\mathtt{R}\mathtt{T}}^{\star}$ algorithm, a set of TPBVPs that corresponds to the set of tentative trajectories connecting $\mathbf{q}_{rand}$ to a set of nearby nodes has to be solved.

<!-- chunk {"id": "body-0080", "role": "body", "section": "NUMERICAL EXAMPLE", "weight": 1.0} -->

When the TPBVP is not easy to be solved (like in the considered example), the applicability of ${\mathtt{R}\mathtt{R}\mathtt{T}}^{\star}$ to dynamic and partially known environments is hampered.

<!-- chunk {"id": "body-0081", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

In this paper, a variant of RRT^⋆^, named ${{\mathtt{R}\mathtt{R}\mathtt{T}}^{\star}\ {\mathtt{M}\mathtt{o}\mathtt{t}\mathtt{i}\mathtt{o}\mathtt{n}}} -$ $\mathtt{P}\mathtt{r}\mathtt{i}\mathtt{m}\mathtt{i}\mathtt{t}\mathtt{i}\mathtt{v}\mathtt{e}\mathtt{s}$, that allows to introduce motion primitives in the RRT^⋆^ planning framework is presented. In particular, a set of pre-computed trajectories, named motion primitives, is used to substitute the computationally challenging step of solving for a steering action.

<!-- chunk {"id": "body-0082", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

Then, in order to ensure that for any queried steering action a pre-computed trajectory exists, a grid representation of the state space has been introduced.\This newly conceived algorithm is supported by an accurate theoretical analysis, demonstrating the optimality and probabilistic completeness.\The performance of ${\mathtt{R}\mathtt{R}\mathtt{T}}^{\star}\ {\mathtt{M}\mathtt{o}\mathtt{t}\mathtt{i}\mathtt{o}\mathtt{n}\mathtt{P}\mathtt{r}\mathtt{i}\mathtt{m}\mathtt{i}\mathtt{t}\mathtt{i}\mathtt{v}\mathtt{e}\mathtt{s}}$ has been verified in simulation, showing promising results in terms of quality of the planned trajectory and computation time, that is particularly important for an online usage in the case of dynamic environments that require repeated replanning. The results show also that as the grid size gets smaller, asymptotic optimality is achieved.

<!-- chunk {"id": "body-0083", "role": "body", "section": "CONCLUSIONS", "weight": 1.0} -->

Having a fine resolution, however, increases the size of the database and the number of iterations required to converge to the resolution optimal trajectory. Nevertheless, one advantage of adopting a sampling based approach is the possibility of computing a feasible though sub-optimal solution first, and then, in case more time is available, improve it. One should indeed choose the best compromise between computing time and performance, according to the application at hand.
