## Introduction

Figure 1: Examples of kinodynamic motion planning problems. Start and goal configurations are shown in green and red, respectively, while gray boxes represent obstacles. We display some trajectories found by our algorithm, iDb-A*, in blue. (a) A unicycle with asymmetric angular speed bounds and a positive minimum velocity. (b) A car pulling a trailer. (c) Acrobatics with a planar multirotor with an underactuated pendulum. (d) A recovery flight with a quadrotor with a very limited thrust-to-weight ratio.

Kinodynamic motion planning for robots remains a challenging task, particularly when the objective is to compute time-optimal plans. Fig. 1 showcases four interesting problems: obstacle-free recovery motions from unstable configurations with low-power quadcopters (Fig. 1(d)), swing-up motions with acrobatic pole-copters among obstacles (Fig. 1(c)), maneuvering an Ackermann steering car with a trailer through a tight corridor (Fig. 1(b)), and a unicycle with asymmetric angular speed bounds and a positive minimum velocity (Fig. 1(a)). Together, these examples illuminate the key challenges in kinodynamic motion planning: *i)* the diversity of the intended robotic systems, *ii)* the nonlinearity of the dynamics, and *iii)* nonconvex configuration spaces with narrow passages among obstacles.

Current planning approaches are sampling-based, search-based, optimization-based, or hybrid. Each of these methods has its strengths and weaknesses. Sampling-based planners can find initial solutions quickly and have strong guarantees for asymptotic convergence to an optimal solution in theory. In practice, the initial solutions are far from optimal; the convergence rate is low, and the solutions typically require post-processing.

Search-based approaches can remedy some of those shortcomings by connecting precomputed trajectories, so-called *motion primitives*, using A\* or related graph search algorithms. Yet, the theoretical guarantees of A\* only hold to the selected discretization of the state space and the precomputed motions. Moreover, scaling this approach to higher dimensions or general systems requires careful, frequently hand-crafted design of the motion primitives, which requires domain-specific knowledge and is impractical for many dynamical systems.

Optimization-based planners scale polynomially rather than exponentially with the number of state dimensions, which makes them better suited for high-dimensional planning problems. However, these planners are, in general, only locally optimal and thus require a good initial guess both for the trajectory and the time horizon.

Thus, optimization approaches are typically combined with a sampling-based planner that generates an initial path with a simplified version of the dynamics, e.g., a geometric planner that avoids obstacles. This strategy is not guaranteed to produce valid motion plans and requires in-depth knowledge of the dynamical system to choose an informative, yet simple enough, dynamics model. For instance, a simple linear position model can be used to plan quadcopter motions around the hovering state but fails to plan trajectories that recover from upside-down configurations.

Our main contribution is Iterative Discontinuity Bounded A\* (iDb-A\*), a novel kinodynamic motion planner that combines a search algorithm, Discontinuity-Bounded A\* (Db-A\*), and trajectory optimization in an Iterative fashion. iDb-A\* combines key ideas and strengths of the previously introduced methods. We rely on a graph search with short trajectories that are connected with bounded discontinuity because it provides a theoretically grounded exploration-exploitation trade-off. We avoid predefined discretization and instead use a set of randomized motions similar to sampling-based planning.

Introducing discontinuity when connecting primitives makes the search tractable: we can reuse the primitives and have a finite number of states to expand. While the output trajectory of the search algorithm is not feasible, it can be used as an initial guess for trajectory optimization that locally repairs the discontinuous trajectory into a valid one. We execute search and optimization iteratively, where the value of the discontinuity bound decreases with each iteration, and the number of primitives increases. For large discontinuity bounds, the search is fast, but the optimizer might fail to find a valid solution. For small bounds, the search requires a longer runtime, but the optimizer has a better initial guess. Thus, the iterative combination results in an efficient anytime planner with probabilistic optimality guarantees.

Our algorithm is implemented in C++ and is publicly available. Our second contribution is an open-source benchmark that compares the three major kinodynamic motion planning techniques on the same problem instances. While we focus in our evaluation on time optimality, our approach supports other cost functions that are additive and non-negative (e.g., energy or squared acceleration).

Statement of Extension: This article is based on our previous conference paper, but it provides algorithmic improvements, a faster implementation, and a more extensive evaluation, which includes several problems that require obstacle avoidance and aggressive movements with flying robots.

*New Algorithmic Contributions:* A new strategy to optimize trajectories with free terminal time in the optimization step of iDb-A\*.

The generalization of iDb-A\* from translation-invariant systems to systems without invariance (e.g., the acrobot), or with additional linear velocity invariance (e.g., multirotors).

Additionally, we provide a refined theoretical analysis and an ablation study of different components, including various optimization strategies, heuristics, and motion primitives.

## Related Work

Search-based approaches rely on existing methods for discrete path planning, such as A\* and its variants. The common approach is to generate short trajectories (*motion primitives*) using a state lattice---a pre-specified discrete set of states. Each primitive starts and ends at a grid cell, and swept cells can be precomputed for efficient collision checking. Once motion primitives are computed, existing algorithms such as A\* or an anytime variant (e.g., Anytime Repairing A\* ) can be employed without modification, providing very strong theoretical guarantees on both optimality and completeness with respect to the chosen primitives. The major challenge is selecting and computing effective motion primitives, especially for high-dimensional systems.

Sampling-based approaches build a tree $\mathcal{T}$ rooted at the start state $\mathbf{x}_{s}$. During tree expansion, i) a random state $\mathbf{x}_{\text{rand}}$ in the state space is sampled, ii) an existing state $\mathbf{x}_{\text{expand}} \in \mathcal{T}$ is selected, and iii) a new state $\mathbf{x}_{\text{new}}$ is added with a motion that starts at $\mathbf{x}_{\text{expand}}$ and moves towards $\mathbf{x}_{\text{rand}}$. The motions are typically generated by propagating random control inputs, and the classic version of this approach, *kinodynamic RRT*, is probabilistically complete. Asymptotic optimality can be achieved when planning in state-cost space (*AO-RRT*) or by computing a sparse tree (*SST\**). These methods rely on a distance function and often require fast nearest neighbor data structures, such as k-d trees, for efficiency.

Sampling-based approaches are designed to explore the state space as rapidly as possible and typically do not explicitly use a heuristic function, unlike search-based methods. Instead, the exploration/exploitation trade-off is controlled by using goal-biasing. In these approaches, the goal constraint is typically reformulated using a goal region rather than a goal state.

Optimization-based approaches locally refine an initial trajectory using the gradients of the cost function, dynamics, and collision constraints, unlike the previous gradient-free methods. The trajectory optimization problem can be formulated as a finite-dimensional nonlinear program (NLP) using either direct collocation or shooting methods, and solved with general-purpose nonlinear solvers (e.g., ).

For instance, *TrajOpt* and *GuSTO* rely on direct transcription and sequential convex programming (SCP), while *KOMO* combines direct transcription with the Augmented Lagrangian algorithm.

Trajectories can also be computed with optimal control solvers based on Differential Dynamic Programming or the iterative Linear Quadratic Regulator (iLQR).

All optimization-based approaches require an initial guess as a starting trajectory, but this guess does not necessarily need to be feasible. For nonlinear dynamics and constraints, optimization approaches are incomplete and might fail or converge to a local optimum. In fact, they often converge to infeasible solutions unless the initial guess is close to a feasible solution. When successful, the solution quality is significantly higher (e.g., in terms of smoothness) compared to sampling-based or search-based approaches. Moreover, optimization-based approaches do not suffer directly from the curse of dimensionality, although higher dimensions might result in more local optima.

Hybrid approaches combine search, sampling, and optimization. For instance, one can combine search and optimization, search and sampling, or combine sampling and optimization. For some dynamical systems, using insights from control theory for motion planning can also be beneficial, but it requires domain knowledge. Motion planning can also benefit from using machine learning for computational efficiency.

Our algorithm, iDb-A\*, combines ideas and tools from the three main approaches to kinodynamic motion planning. The most closely related works are methods that reuse edges within a sampling-based planning framework and search-based methods with duplicate detection. Compared to these works, we include trajectory optimization and reuse locally optimal precomputed motion primitives interconnected with bounded discontinuity for better success and faster convergence.

Apart from the aforementioned approaches, a popular approach to kinodynamic motion planning problems is to first plan with simplified dynamic models and to use trajectory optimization or a local controller to follow the reference path while accounting for the true dynamics. The simplest model is a geometric model (holonomic, first-order integrator), which enables geometric motion planning , e.g., RRT, RRT\*, PRM, or PRM\*. Second-order systems can be approximated by a double integrator linear model.

The trajectories computed with simplified dynamics can then be used as initial guesses for trajectory optimization (that is, optimization-based approaches as previously discussed), model predictive control, or system-specific controllers for quadcopters, unicycle-like robots, or car-like robots. System-specific motion planners can exploit certain properties of the dynamics, such as differential flatness in quadcopters, which allows faster motion planning as shown for quadcopters and for some specific fixed-wing UAVs. However, differential flatness cannot account for actuation constraints directly---leading to either conservative or infeasible trajectories, especially for small UAVs with a low thrust-to-weight ratio.

Notably, planning with simplified dynamics does not guarantee the generation of valid motion plans and demands an in-depth understanding of the dynamical system. In our algorithm, iDb-A\*, connecting motion primitives with bounded discontinuity during the search step can be interpreted as an alternative form of simplified dynamics. However, iDb-A\* is complete and asymptotically optimal because it combines search and optimization in an iterative fashion, increasing the number of motion primitives and reducing the allowed discontinuity in each iteration.

## Problem Description

We consider a robot with a continuous state $\mathbf{x} \in \mathcal{X}$ (e.g., $\mathcal{X} \subseteq {\mathbb{R}}^{d_{x}}$) that is actuated by actions $\mathbf{u} \in \mathcal{U} \subset {\mathbb{R}}^{d_{u}}$. The dynamics of the robot are deterministic, described by a differential equation, To employ gradient-based optimization, we assume that we can compute the Jacobian of $\mathbf{f}$ with respect to $\mathbf{x}$ and $\mathbf{u}$, typically available in systems studied in kinodynamic motion planning, such as mobile robots or rigid-body articulated systems. We use $\mathcal{X}_{\text{free}} \subseteq \mathcal{X}$ to denote the collision-free space, i.e., the subset of states that are not in collision with the obstacles in the environment.

We discretize the dynamics with a zero-order hold, i.e., we assume the applied action is constant during a time step of duration $\Deltat$. The discretized dynamics can then be written as, using a small $\Deltat$ to ensure the accuracy of the Euler approximation. We use $K \in {\mathbb{N}}$ to denote the number of time steps (which is not fixed but subject to optimization), $\mathbf{X} = {\langle\mathbf{x}_{0},\mathbf{x}_{1},\ldots,\mathbf{x}_{K}\rangle}$ to denote the sequence of states sampled at times $0,{\Deltat},\ldots,{K\Deltat}$ and $\mathbf{U} = {\langle\mathbf{u}_{0},\mathbf{u}_{1},\ldots,\mathbf{u}_{K - 1}\rangle}$ to denote the sequence of actions applied to the system for the time frames ${\lbrack 0,{\Deltat})},{\lbrack{\Deltat},{2\Deltat})},\ldots,{\lbrack{{({K - 1})}\Deltat},{K\Deltat})}$. The objective of navigating the robot from its start state $\mathbf{x}_{s}$ to a goal state $\mathbf{x}_{g}$ can then be framed as the optimization problem, with the cost term ${J{(\mathbf{U},\mathbf{X})}} = {\sum_{k = 0}^{K - 1}{j{(\mathbf{u}_{k},\mathbf{x}_{k})}\Deltat}}$, where ${j{(\mathbf{u}_{k},\mathbf{x}_{k})}} \geq 0$. In this paper, we will focus on time-optimal trajectories, i.e., ${j{(\mathbf{u}_{k},\mathbf{x}_{k})}} = 1$; ${J{(\mathbf{U},\mathbf{X},K)}} = {K\Deltat}$, but our framework can be applied to optimize any additive cost function, for example, minimum control effort ${j{(\mathbf{u}_{k},\mathbf{x}_{k})}} = {\|\mathbf{u}_{k}\|}^{2}$.

We assume the dynamics function $\text{step}{(\mathbf{x},\mathbf{u})}$, control space $\mathcal{U}$, state space $\mathcal{X}$, and cost function $j{(\mathbf{x},\mathbf{u})}$, are known before solving the problem, which allows us to precompute motion primitives.

### Example 1

Consider a unicycle robot with state $\mathbf{x} = {\lbrack x,y,\theta\rbrack} \in {{{\mathbb{R}}^{2} \times S}O{}}$, i.e., $x,y$ are the position and $\theta$ is the orientation. The actions are $\mathbf{u} = {\lbrack v,\omega\rbrack} \in \mathcal{U} \subset {\mathbb{R}}^{2}$, i.e., the speed and angular velocity can be controlled directly. The dynamics are $\overset{˙}{\mathbf{x}} = {\lbrack{v{\cos{(\theta)}}},{v{\sin{(\theta)}}},\omega\rbrack}$. The choice of $\mathcal{U}$ can make this low-dimensional problem challenging to solve. For example, Fig. 1(a) shows a plane-like case (positive minimum speed, i.e., $0.25 \leq v \leq 0.5$ $\ {m/s}$) with a malfunctioning rudder (asymmetric angular speed, i.e., ${- 0.25} \leq \omega \leq 0.5$ $\ {{rad}/s}$).

### Example 2

Consider a quadrotor $\mathbf{x} = {\lbrack\mathbf{p},\mathbf{v},\mathbf{q},\mathbf{w}\rbrack}$ in ${{\mathbb{R}}^{9} \times S}O{}$ where $\mathbf{p}$ represents the position, $\mathbf{v}$ is the velocity, $\mathbf{q}$ represents the orientation using a quaternion, and $\mathbf{w}$ is the angular velocity in the body frame. The control input is the force at each rotor, $\mathbf{u} \in {\mathbb{R}}^{4}$. The dynamics are, where $m$ is the mass, $\mathbf{I}$ represents the inertia matrix, $\mathbf{g}$ is the gravity vector, $\mathbf{R}{(\mathbf{q})}$ is the rotation matrix corresponding to the quaternion $\mathbf{q}$, and $\otimes$ denotes the quaternion product. The matrices ${\mathbf{B}_{0},\mathbf{B}_{1}} \in {\mathbb{R}}^{3 \times 4}$ are constant and depend on the quadcopter's geometry. The parameters of the Bitcraze Crazyflie 2.1 robot are used, which, with a very low thrust-to-weight ratio of 1.3 (i.e., $0 \leq u_{i} \leq {{1.3 \times g \times m}/4}$), pose significant challenges for kinodynamic motion planning.

Figure 2: Visual representation of iDb-A* in the problem Planar rotor – Recovery obstacles (i.e., a recovery maneuver with a planar multirotor). Start and goal configurations are shown in solid green (note that the multirotor starts upside down) and red, respectively. (a) In the search step of iDb-A*, called Db-A*, we expand states (in this case, the initial state) using motion primitives that are applicable with bounded discontinuity. (b) Intermediate search tree during the execution of Db-A*. For visualization, the 6D configuration space is projected into a 2D space. (c) Solution found by Db-A*. The transparent, border-only green and red shapes show the start and end of each motion primitive, respectively. They do not match exactly, which highlights the allowed discontinuities when stitching motion primitives (note that the discontinuities in the velocities are not shown in this 2D representation). (d) The output of Db-A* is used to warm-start nonlinear trajectory optimization. The resulting trajectory, shown in blue, fulfills the dynamics constraints and is locally optimal.

## iDb-A\* - Overview

Our iterative approach, which combines search and optimization, is detailed in Algorithm 1. We require a *large* set of *motion primitives* $\mathcal{M}_{L}$, which will be used incrementally and can be computed offline. Motion primitives are short trajectories that fulfill our dynamics (see Definition 1. ‣ V Discontinuity Bounded A* Search ‣ iDb-A*: Iterative Search and Optimization for Optimal Kinodynamic Motion Planning") and Section VII for a formal definition and details on primitive generation). In every iteration of iDb-A\*, the following steps are performed: We increase the number of available motion primitives for the search (by choosing new primitives from $\mathcal{M}_{L}$) and decrease the allowed discontinuity bound $\delta$ (Algorithms 1 and 1).

The discrete planner, Db-A\*, computes a trajectory using the current set of motion primitives. This trajectory may include a bounded violation of the dynamic constraints (Db-A\* in Algorithm 1, see Section V).

The result of Db-A\* is used to initialize an optimization-based motion planner that attempts to compute a feasible and locally optimal trajectory (Algorithm 1). See Optimization (Section VI).

Additional motion primitives are extracted from the output of the trajectory optimization (Extract Primitives in Algorithm 1). iDb-A\* executes a sequence of A\*-searches using a growing, randomized set of motion primitives, akin to Batch Informed Tree (BIT\*), a successful sampling-based planner for geometric motion planning. In each iteration, the computation time and the success of the search and optimization steps depend on the number of motion primitives $n_{i} = {|\mathcal{M}_{i}|}$ and the allowed discontinuity bound $\delta_{i}$. We can choose AddPrimitives (Algorithm 1) and DecreaseDelta (Algorithm 1) so that these parameters follow geometric sequences $n_{i + 1} = {n_{i}n_{r}}$ and $\delta_{i + 1} = {\delta_{i}\delta_{r}}$, with $n_{r} > 1$, $\delta_{r} < 1$ and initial values $n_{0}$, $\delta_{0}$. We find this strategy easier to tune than the alternative approach presented in our prior work, where we choose only the scheduling for the number of motion primitives and estimate the allowed discontinuity bound based on a desired approximate branching factor.

Motion primitives can also be extracted online in Algorithm 1. The ExtractPrimitives procedure utilizes the output of the optimization by dividing the trajectory into small sections. The resulting primitives can be particularly useful for the planning problem at hand as they are computed with full knowledge of the environment.

A visual representation of some key components of iDb-A\* is shown in Fig. 2 using the problem *Planar rotor -- Recovery obstacles*.

Input: xs, xg, step, 𝒳free, 𝒰, ℳL ⊳ Initial Set of motion primitives ⊳ Solution cost bound 4 Xd, Ud← Db-A*(xs, xg, 𝒳free, ℳi, δi, cmax) 5 if Xd, Ud successfully computed then 6 X, U← Optimization(Xd, Ud, xs, xg, step, 𝒳free, 𝒰) 7 if X, U successfully computed then ⊳ New solution found cmax ← min (cmax, J (X, U)) Algorithm 1 iDb-A* – Iterative Discontinuity Bounded A*

## Discontinuity Bounded A\* Search

Figure 3: (a, b, c) A graphical description of Db-A*. The gray edges represent motion primitives, and the states xs and xg are the start and the goal, respectively. (a) Given an initial state xs, we can only apply primitives that start with a discontinuity lower than α δ (gray circumference) and are collision-free. The applicable primitives are shown with solid black edges. (b) The search is ordered by a heuristic (e.g., the Euclidean heuristic, shown with a dotted line for the best node) and the cost-to-come. When expanding a node, we create new states only if they are not within (1 − α) δ of a previously discovered state (i.e., the dashed edge is not expanded). (c) The search is terminated when a node close to the goal is expanded. (d) The solution of Db-A* will be used to warm-start a trajectory optimization algorithm that repairs the discontinuities and locally optimizes the trajectory. The optimized trajectory is shown in blue.

Discontinuity Bounded A\* (Db-A\*) is a search algorithm that uses a set of motion primitives, which are connected while allowing for a maximum discontinuity.

A motion primitive is a sequence of states and controls that fulfill the dynamics of the system. Formally,

### Definition 1 (Motion Primitive)

A motion primitive $m = {(\mathbf{X},\mathbf{U},\mathbf{x}_{s},\mathbf{x}_{f},c)}$ is a sequence of states $\mathbf{X} = {(\mathbf{x}_{0},\ldots,\mathbf{x}_{N})}$, $\mathbf{x}_{k} \in \mathcal{X}$, and controls $\mathbf{U} = {(\mathbf{u}_{0},\ldots,\mathbf{u}_{N - 1})}$, $\mathbf{u}_{k} \in \mathcal{U}$ that fulfill the dynamics $\mathbf{x}_{k + 1} = {{step}{(\mathbf{x}_{k},\mathbf{u}_{k})}}$. It connects the start state $\mathbf{x}_{s} = \mathbf{x}_{0}$ and the final state $\mathbf{x}_{f} = \mathbf{x}_{N}$, with a corresponding cost $c \in {\mathbb{R}}^{+}$. The length of the motion primitive (i.e., the number of states and controls) is randomized.

In the following, we rely on a user-specified *metric* $d:{{\mathcal{X} \times \mathcal{X}}\rightarrow{\mathbb{R}}^{+}}$, which measures the distance between two states (e.g., a weighted Euclidean norm). We assume that $\langle\mathcal{X},d\rangle$ is a metric space in order to use efficient nearest-neighbor data structures, such as k-d trees.

### Definition 2

The pair of sequences $\mathbf{X} = {\langle\mathbf{x}_{0},\ldots,\mathbf{x}_{K}\rangle}$, $\mathbf{U} = {\langle\mathbf{u}_{0},\ldots,\mathbf{u}_{K - 1}\rangle}$ is a $\delta$-discontinuity bounded solution (with $\delta > 0$) to the kinodynamic motion planning problem 3 if and only if the following conditions hold: Intuitively, Definition 2 enforces that the sequences connect the start and goal states with a bounded error $\delta$ in the dynamics, which corresponds to "stitching" primitives together.

### V-A Algorithm

Our approach to computing such sequences is Discontinuity Bounded A\* (Db-A\*).

Db-A\*, like A\*, is an informed search that relies on a heuristic $h:{\mathcal{X}\rightarrow{\mathbb{R}}}$ to explore an implicitly defined directed graph efficiently. Nodes in the graph represent states, and an edge between two nodes indicates that there exists a motion that connects the states, allowing up to $\delta$-discontinuity.

The algorithm is shown in Algorithm 2, and Fig. 3 provides a graphical representation. Db-A\* keeps track of nodes to explore using a priority queue, which is sorted by the lowest ${f{(\mathbf{x})}} = {{g{(\mathbf{x})}} + {h{(\mathbf{x})}}}$ value, where $g{(\mathbf{x})}$ is the cost-to-come. The overall structure is the same as in A\*: The OPEN priority queue $\mathcal{O}$ is initialized with the start state (Algorithm 2). At each iteration, we remove the first element from $\mathcal{O}$ (Algorithm 2), and that node is expanded using the applicable collision-free motion primitives (Algorithms 2 to 2). A motion $m$ is applicable in state $\mathbf{x}$ if its start state $m.\mathbf{x}_{s}$ is within a distance of at most $\alpha\delta$ (Algorithm 2), resulting in a new state $m.\mathbf{x}_{f}$.

New states are added to $\mathcal{O}$ (Algorithm 2) only if they are not within ${({1 - \alpha})}\delta$ of previously discovered nodes. If the state is close to a previous node, the previous node is updated if the new cost-to-come is reduced (Algorithm 2). Therefore, unlike A\*, we consider two states to be equivalent if they are within ${({1 - \alpha})}\delta$ of each other.

For computing and updating the cost to come, we consider the cost of the motion primitive $m.c$ and the cost of the discontinuity bound using a lower bound function $l:{{\mathcal{X} \times \mathcal{X}}\rightarrow{\mathbb{R}}^{+}}$ of the true cost. Therefore, given a state $\mathbf{x}$ with cost to come $g{(\mathbf{x})}$, the cost of a new state ${\mathbf{x}' = {\mathbf{x} \oplus m} = m}.\mathbf{x}_{f}$ is $g{(\mathbf{x}')} = g{(\mathbf{x})} + l{(\mathbf{x},m.\mathbf{x}_{s})} + m.c$ (Algorithm 2).

The search terminates when we find a node that is within $\delta$ distance of the goal state (Algorithm 2).

For efficient search, we employ two k-d trees. The first tree indexes the start states of all provided motion primitives, which can be done once at the beginning. The second k-d tree contains the states of all explored nodes and grows dynamically. It is used to find nearby previously explored states. The discontinuity with a magnitude of up to $\delta$ may occur in two cases: first, when we select suitable motion primitives for expansion (Algorithm 2), and second, when we prune a potential new node in favor of already existing states (Algorithm 2). The tradeoff between the two can be adjusted by a user-specified parameter $\alpha \in {}$.

Input: xs, xg, 𝒳free, ℳ, δ, cmax 𝒪 ← {Node(x: xs, g: 0, h: h(xs), p: None, a: None)} ⊳ Initialize open list (priority queue) ⊳ Initialize list of closed nodes ⊳ Remove node with lowest f-value ⊳ Trace back solution ⊳ Find applicable motion primitives with discontinuity up to α δ ⊳ Motion is not collision-free ⊳ Tentative new state ⊳ Check if we have previously discovered states within (1 − α) δ ⊳ Update node. If it is in closed list, reinsert in open list. Algorithm 2 Db-A* – Discontinuity Bounded A*

### V-B Heuristic Functions

In kinodynamic motion planning, three heuristic functions $h{(\mathbf{x})}$ are particularly relevant:

### Euclidean Heuristic

The Euclidean heuristic is based on the Euclidean distance to the goal, considering state and control constraints such as maximum velocity or acceleration, while ignoring dynamics and obstacles. It is usually computed by a combination of weighted Euclidean or infinity norms and does not require any precomputation.

### Roadmap Heuristic

The Roadmap heuristic approximates the collision-free space using a geometric roadmap, thus taking collisions and control bounds into account but ignoring the dynamics. It requires a precomputation step to build the geometric roadmap, which can be reused between iterations of iDb-A\*, and it is usually more informative in problems where obstacles play a significant role. Given a finite set of state-cost pairs $S = \left. \{{(\mathbf{s}_{i},c_{i})} \middle| {{\mathbf{s}_{i} \in \mathcal{X}},{c_{i} \in {\mathbb{R}}}}\} \right.$, the heuristic function is given: where $l$ is a lower bound on the cost for reaching $\mathbf{s}_{i}$ from $\mathbf{x}$, and $R$ is a user-defined connection radius. To compute $S$, we construct a roadmap with randomly sampled configurations and annotate each vertex with the geometric cost-to-go (i.e., using the Euclidean heuristic for each collision-free edge). Each query requires a nearest-neighbor search (implemented using a k-d tree).

### Blind Heuristic

Lastly, we also evaluate the Blind heuristic, where ${h{(\mathbf{x})}} = {0,{\forall\mathbf{x}}}$. This heuristic is motivated by systems where the dynamics play a central role, such that feasible trajectories of the robot strongly differ from straight lines in the state space (e.g., the acrobot), making the Euclidean and Roadmap heuristics uninformative.

### Example 3

Consider the unicycle robot, with state and dynamics as in Example 1. Given a state $\mathbf{x} = {\lbrack x,y,\theta\rbrack}$, goal $\mathbf{g} = {\lbrack g_{x},g_{y},g_{\theta}\rbrack}$, and the control bounds ${|v|} \leq v_{\text{max}}$, ${|w|} \leq w_{\text{max}}$, the Euclidean heuristic is: where $D_{\theta}{(\cdot, \cdot)}$ is the distance metric in SO.

### V-C Equivalence Between Continuous States

A fundamental issue when applying search algorithms in continuous spaces is that the set of possible reachable states is infinite. The search algorithm will unnecessarily expand similar states, especially when the heuristic is not informative.

To mitigate this issue, in Db-A\* we have defined a notion of similarity or equivalence between states, often referred to as duplicate detection in related work. In Algorithm 2, a state is considered not novel if it is close to a previously discovered state, in which case the state is pruned. This makes Db-A\* incomplete and suboptimal for fixed values of $\delta$. As Db-A\* runs for decreasing $\delta$ inside iDb-A\*, the size of the equivalence class is iteratively reduced. In combination with subsequent optimization, we found our duplicate detection to be sufficient for both good practical performance and asymptotic optimality (Section VIII).

### V-D Invariance and Equivariance in the Motion Primitives

To decide which motion primitives are applicable in a state (Algorithm 2), we can exploit invariance and equivariance in the system dynamics, which allows us to reuse the same primitive in different states with smaller discontinuities.

A prominent example is the translation invariance of the dynamics of mobile robots. Intuitively, a valid motion primitive can be "translated" to match other starting states so that there is no discontinuity in the translation components of the state. This concept is formalized in Section VII, where we provide two examples: translation invariance for a car-like robot and translation and linear velocity invariance for flying robots.

From an implementation perspective, to account for invariances, all primitives are stored in a canonical form (e.g., with 0 translation component) inside a k-d tree. At runtime, we transform the query state into the canonical form to check which primitives are applicable, and the valid primitives are then transformed on-the-fly to expand the query state.

### V-E Efficient Collision Checks with Collision Shapes

Collision checking is one of the most expensive operations in motion planning. To check collisions between the environment and a motion primitive (Algorithm 2), we use either precomputed collision shapes of the motion primitive (if available) or check collisions at a small temporal resolution. Importantly, precomputed collision shapes can also be transformed online for any translation or rotation of the motion primitive. When available, collision shapes are considerably faster than checking individual configurations at a chosen resolution.

In practice, we observe that the running time of Db-A\* is dominated by both nearest neighbor searches to find neighboring states and applicable motion primitives, and by collision detection (see Fig. 7 in Section IX-E).

## Trajectory Optimization

For the Optimization subroutine (Algorithm 1 in Algorithm 1), we use gradient-based trajectory optimization. We assume that the derivatives of the dynamics, the distance function, and the collision constraints can be computed efficiently, e.g., using analytical expressions, a differentiable simulator, or finite differences. For collisions, we now require a signed distance function instead of a binary collision check.

The objective of the optimization is to solve the original kinodynamic motion planning problem, using the output of Db-A\* as an initial guess, $\mathbf{X}_{d} = {\{\mathbf{x}_{0},\mathbf{x}_{1},\ldots,\mathbf{x}_{K}\}}$, $\mathbf{U}_{d} = {\{\mathbf{u}_{0},\mathbf{u}_{1},\ldots,\mathbf{u}_{K - 1}\}}$.

Even with the initial guess from Db-A\*, the optimization problem is challenging for gradient-based optimization, especially when starting with large discontinuities.

The problem is nonconvex even for systems with linear dynamics and constraints, and the infeasible initial guess and underactuation of the systems prevent the use of time-optimal path tracking approaches (e.g., ). In this section, we describe four different methods that we studied for the optimization step of iDb-A\*, based on different approaches in the optimization and control literature.

### Joint Optimization of Trajectory and Terminal Time (Free-dt)

This approach adds the duration of the time interval as an optimization variable for joint nonlinear optimization of time and trajectory: Here, $\Deltat$ is a variable, initialized to $\Deltat_{\text{ref}}$, the reference value used for time-discretization in the motion primitives for the given dynamical system. The number of time steps $K$ is fixed. After solving (8 ‣ VI Trajectory Optimization ‣ iDb-A*: Iterative Search and Optimization for Optimal Kinodynamic Motion Planning")), we would like to have the solution trajectory discretized with the original time step duration for consistency. Thus, we recompute the state and control trajectories using the reference time step $\Deltat_{\text{ref}}$. This requires i) interpolation of the solution of (8 ‣ VI Trajectory Optimization ‣ iDb-A*: Iterative Search and Optimization for Optimal Kinodynamic Motion Planning")) with $\Deltat_{\text{ref}}$, and ii) a second run of trajectory optimization, now with fixed ${\Deltat} = {\Deltat_{\text{ref}}}$ to repair the small errors arising from the Euler integration with different step sizes (note that the second optimization is very efficient because the interpolation of the solution of (8 ‣ VI Trajectory Optimization ‣ iDb-A*: Iterative Search and Optimization for Optimal Kinodynamic Motion Planning")) is already accurate).

### Hierarchical Time Search (Search-T)

A hierarchical approach that combines a linear search on the terminal time with trajectory optimization with a fixed terminal time. Given the time bounds $\{ T_{\text{min}},T_{\text{max}}\}$ and a time resolution $h$, we define a set of candidate times $\mathcal{T} = {\{ T_{\text{min}},{T_{\text{min}} + h},\ldots,T_{\text{max}}\}}$, and solve the hierarchical optimization problem: where $\text{Trajectory_Optimization}{(T_{i})}$ first rescales temporally the initial guess to have a time duration of $T_{i}$ (the time step size $\Deltat$ is kept constant, but the number of time steps of the trajectory varies) and then solves with a fixed number of time steps $K_{i}$ and fixed $\Deltat$. For time-optimal trajectories, we start the search at $T_{\text{min}}$, and stop at the first $T_{i}$ when $\text{Trajectory_Optimization}{(T_{i})}$ is feasible. Based on the duration $T_{0}$ of the initial guess, a reasonable choice of the parameters is, e.g., $T_{\text{min}} = {0.5T_{0}}$, $T_{\text{max}} = {2T_{0}}$, and $h = {{({T_{\text{max}} - T_{\text{min}}})}/10}$.

### VI-A Sliding Window Optimization

Instead of considering the full trajectory at once, the optimization step can try to repair the discontinuities locally. While this approach is more constrained to follow the initial guess, it is also potentially faster. Solving a sequence of smaller subproblems often reduces the computational cost and number of nonlinear iterations, which typically increase for longer trajectories.

The following two approaches are inspired by two optimal control formulations, namely Model Predictive Control (MPC) and Model Predictive Contouring Control (MPCC). In both approaches, we repair the initial guess trajectory in a sequence of steps, starting from the beginning of the initial guess. At each step, we (i) optimize the sequence of states and controls inside a small optimization window of length $W_{o}$ (e.g., 50 steps), (ii) fix the first $W_{s} \leq W_{o}$ states and controls (e.g., 10 steps), and (iii) move the optimization window by $W_{s}$, so that the new start state is the last fixed state. The time step duration $\Deltat$ is fixed, but the resulting final trajectory might have a different duration than the initial guess from Db-A\*.

### Subgoal Following (MPC)

The optimization problem in each step is: Here, $\mathbf{X}_{W},\mathbf{U}_{W}$ are the sequence of states and controls in the optimization window, $\mathbf{x}_{W}$ is the last state of the current window, and $\mathbf{g}$ is the subgoal state for this optimization window, chosen from the Db-A\* initial guess to encourage making progress in the path. The weight $k_{1} > 0$ combines the objective of minimizing the distance to the subgoal $d{(\mathbf{x}_{W},\mathbf{g})}$ with the original control cost function.

### Path Following (MPCC)

The optimization problem in each step is: The function ${\pi{(\cdot)}}:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{X}}$ is a smooth parameterization of the initial guess (e.g., a spline through the waypoints), and the scalar variable $\alpha$ indicates the progress on the path. The term $k_{1}\alpha$, with $k_{1} > 0$, tries to maximize the progress along the path. The term $k_{2}d{(\mathbf{x}_{W},{\pi{(\alpha)}})}^{2}$, with $k_{2} > 0$, minimizes the distance between the last state in the window and the progress on the path. Together, these two terms push the last state $\mathbf{x}_{W}$ to make progress along the path while following it closely (note that, compared to other MPCC formulations, we only apply the contouring cost to the last state in the window).

### VI-B Algorithm for Trajectory Optimization

All different approaches for trajectory optimization require solving nonlinear optimal control problems. In our previous work, we used a direct control method, namely k-order optimization, and the Augmented Lagrangian algorithm. In this revised version, we switch to an indirect control method, Differential Dynamic Programming (DDP), which ensures precise dynamics during shooting and therefore more reliable convergence to locally optimal solutions in systems with complex dynamics.

Differential Dynamic Programming is a second-order method for solving optimal control problems of the form: It iteratively computes a quadratic approximation of the cost-to-go using a backward pass and updates states and controls using a forward pass. For more details, we refer to,.

To deal with collisions, goal constraints, and state and control bounds, we use a squared penalty method---adding all constraints in the cost term with a squared penalty.

In particular, we use *feasibility-driven DDP*, which can be warm-started with an infeasible sequence of states and actions, providing a good balance between local convergence and globalization.

## Motion Primitives

In our framework, we define a motion primitive as a valid trajectory that fulfills the dynamics, control, and state constraints, disregarding collisions with the environment. A formal definition is provided in Definition 1. ‣ V Discontinuity Bounded A* Search ‣ iDb-A*: Iterative Search and Optimization for Optimal Kinodynamic Motion Planning") in Section V.

### VII-A Generation of Locally Optimal Motion Primitives

In the problem setting outlined in Section III, a key observation is that motion primitives can be precomputed because they are independent of the collision-free space and the start and goal configurations of a particular motion planning problem.

Our algorithms, iDb-A\* and Db-A\*, are agnostic about how the primitives have been generated. However, the theoretical properties of the algorithms depend on the properties of the set of primitives (Section VIII). In our implementation of iDb-A\*, we use locally optimal motion primitives computed with trajectory optimization.

To generate motion primitives, we solve two-point boundary value problems with random start and goal configurations in free space using nonlinear optimization. In contrast to the typical approach in sampling-based motion planning of sampling control sequences at random, our strategy results in a superior primitive distribution, especially for systems with unstable dynamics (e.g., flying robots). Our approach achieves better coverage of the state space and produces smoother and lower-cost motion primitives, which are key factors contributing to the success of the algorithm (see Section IX).

Specifically, we generate motion primitives offline using the following three steps: First, uniform random sampling of start and goal configurations in free space; second, solving 3 with trajectory optimization using the hierarchical time search approach and a trivial initial guess; and third, splitting the resulting motion into multiple pieces of random length.

We observe that our strategy generates a good distribution of motion primitives. However, it requires several hours of offline computation with a standard CPU. In the case of flying robots, most of the time is spent attempting to find trajectories where the goal is not reachable within the given time horizon or where trajectory optimization fails to converge. Our sampling approach might bias the primitives' distribution towards configurations that are easy to connect to other configurations. However, the results in Section IX confirm that the primitives are diverse and can solve a wide range of problems.

### VII-B Invariance and Equivariance in System Dynamics

Several robotic systems of interest exhibit symmetries and invariances in the dynamics that can be exploited to reduce the required number of motion primitives for planning.

Specifically, invariance/equivariance enables the adaptation of primitives on-the-fly to match some components of the state space exactly in our search algorithm, Db-A\*. This significantly reduces the number of primitives required to cover the state space, resulting in smaller discontinuities, reduced memory requirements, and faster nearest neighbor searches.

A prominent example is translation invariance, a property that holds for many mobile robots, such as differential-drives, cars, airplanes, and multirotors. In these systems, we can decompose the state into two components, $\mathbf{x} = {\lbrack\mathbf{x}^{t},\mathbf{x}^{r}\rbrack}$, where $\mathbf{x}^{t}$ represents translations and $\mathbf{x}^{r}$ contains rotations and possibly velocities. The dynamics ${f{(\mathbf{x},\mathbf{u})}} = {f{(\mathbf{x}^{r},\mathbf{u})}}$ only depend on the non-translation part of the state.

We are interested in invariances that preserve optimality. For instance, the translation of a primitive in translation invariant systems retains optimality for a running cost of type ${j{(\mathbf{x},\mathbf{u})}} = {r{(\mathbf{u})}}$, e.g., a minimum time trajectory ${r{(\mathbf{u})}} = 1$, or minimum control effort ${r{(\mathbf{u})}} = \left. \parallel\mathbf{u}\parallel \right.^{2}$.

### Example 4 (Translation Invariance in the Unicycle)

Consider the unicycle from Example 1. The dynamics ${f{(\mathbf{x},\mathbf{u})}} = {f{(\theta,\mathbf{u})}} = {\lbrack{v{\cos{(\theta)}}},{v{\sin{(\theta)}}},w\rbrack}$ depend only on the orientation $\theta$, but not on the position $\lbrack x,y\rbrack$. Using translation invariance, we can translate a motion primitive $m = {(\mathbf{X},\mathbf{U},\mathbf{x}_{s},\mathbf{x}_{f},c)}$ with $\mathbf{t} \in {\mathbb{R}}^{2}$, resulting in $m \oplus \mathbf{t} = m' = {(\mathbf{X}',\mathbf{U}' = \mathbf{U},\mathbf{x}_{s}',\mathbf{x}_{f}',c' = c)}$. The states in $\mathbf{X}'$, $\mathbf{x}_{s}'$, and $\mathbf{x}_{f}'$ are transformed as follows: The operator $\lbrack \bullet \rbrack$ indicates the $\bullet$-component of a state $\mathbf{x}$ or translation vector $\mathbf{t}$ (e.g., ${\mathbf{x}{\lbrack x\rbrack}} \in {\mathbb{R}}$ is the "x-component" of the state $\mathbf{x}$).

In some second-order systems, such as the quadrotor, the acceleration depends only on the orientation and the angular velocity but is invariant to both translation and linear velocity. Thus, we can modify primitives to match the starting position and velocity.

### Example 5 (Translation and Linear Velocity Invariance in the Quadrotor)

The second-order dynamics of the quadrotor from Example 2 depend only on the rotation and angular velocity $\mathbf{q},\mathbf{w}$ but not on the position $\mathbf{p}$ or linear velocity $\mathbf{v}$. We can transform a motion primitive $m = {(\mathbf{X},\mathbf{U},\mathbf{x}_{s},\mathbf{x}_{f},c)}$ with $\mathbf{t} = {\lbrack\mathbf{t}_{p},\mathbf{t}_{v}\rbrack}$, $\mathbf{t}_{p} \in {\mathbb{R}}^{3}$, $\mathbf{t}_{v} \in {\mathbb{R}}^{3}$, resulting in $m \oplus \mathbf{t} = m' = {(\mathbf{X}',\mathbf{U}' = \mathbf{U},\mathbf{x}_{s}',\mathbf{x}_{f}',c' = c)}$. The states in $\mathbf{X}'$, $\mathbf{x}_{s}'$, and $\mathbf{x}_{f}'$ are transformed as follows: While invariance and equivariance are advantageous properties, they require an individual study of each new dynamical system. For simplicity, in our work, we focus only on translation invariance and linear velocity invariance as two classical and ubiquitous properties. Additional properties, such as rotation invariance (for car-like robots), rotation symmetries (for 3D quadcopters), or angular rotational invariance (for planar multirotors), could be exploited to improve performance in particular systems.

## Theoretical Properties

In this section, we analyze the theoretical properties of iDb-A\* and argue that it is asymptotically optimal under very mild assumptions. Intuitively, given enough computational time, iDb-A\* (Algorithm 1) will compute the optimal solution, because in each iteration, we add more primitives and reduce the allowed discontinuity $\delta$, eventually producing an initial guess that is close to the optimal solution, which is then locally repaired and optimized with trajectory optimization.

### VIII-A Kinodynamic Motion Planning

### Assumption 1

The dynamics function 1 has a bounded Lipschitz constant for both states and controls. Moreover, there exists a $\delta$-robust trajectory that solves the kinodynamic motion planning problem.

*Note:* A $\delta$-robust trajectory has both obstacle clearance and dynamical clearance of $\delta$. These assumptions are standard in kinodynamic motion planning, and we refer to for a formal definition.

### Remark 1

In a system with Lipschitz dynamics, the discrete-time dynamics converge to the continuous-time dynamics as the time step discretization approaches zero. Thus, we limit our study to the time-discretized system 2 used in our framework.

### VIII-B Db-A\*

### Theorem 1

Sequences $\mathbf{X}$ and $\mathbf{U}$ returned by Db-A\* (Algorithm 2) are $\delta$-discontinuity bounded solutions to the given motion planning problem (Definition 2).

### Proof

When Db-A\* terminates, we trace back the solution by following the parent pointers and obtain a sequence of motion primitives $\lbrack m_{1},\ldots,m_{N}\rbrack$. This sequence defines the sequence of controls $\mathbf{U} = {\lbrack m_{1}.\mathbf{U},\ldots,m_{N}.\mathbf{U}\rbrack}$, and states $\mathbf{X} = {\lbrack m_{1}.\mathbf{X}_{\lbrack{:{- 1}}\rbrack},\ldots,m_{N}.\mathbf{X}\rbrack}$, i.e., we take all but the last state for each primitive except for the last one, which should also include the last state. During Db-A\*, we expand a node $n$ with a motion $m$ if the start state $m.\mathbf{x}_{s}$ is at most $\alpha\delta$ away from the current state $n.\mathbf{x}$. Any node $n$ is reached by a motion $\overset{\sim}{m}$ that ends at point $\overset{\sim}{m}.\mathbf{x}_{f}$, which is at most ${({1 - \alpha})}\delta$ from $n.\mathbf{x}$. Using the triangle inequality of the metric space, $d{(\overset{\sim}{m}.\mathbf{x}_{f},m.\mathbf{x}_{s})} \leq d{(\overset{\sim}{m}.\mathbf{x}_{f},n.\mathbf{x})} + d{(n.\mathbf{x},m.\mathbf{x}_{s})} \leq \delta$. Thus, 5a holds for all connections between motion primitives, and 5d holds for the state in the first motion. We already know that $\mathbf{x}_{k} \in \mathcal{X}$, $\mathbf{u}_{k} \in \mathcal{U}$ for all $k$ 5b. Motions are only used as edges if the entire motion is within $\mathcal{X}_{free}$, thus 5c holds. Finally, 5e holds by the termination conditions. ∎

### Definition 3

Given a start state $\mathbf{x}_{s}$ and a goal state $\mathbf{x}_{g}$, a set of motion primitives $\mathcal{M}$, and a discontinuity bound $\delta$, we define the implicit graph $G_{\delta,\mathcal{M}} = {(V,E)}$ ,

### Remark 2

For an arbitrary fixed value of $\delta > 0$, Db-A\* is incomplete and suboptimal when searching on the implicit graph $G_{\mathcal{M},\delta}$.

### Proof

Consider an example where a robot has to move through a narrow door to navigate to an adjacent room. Even if a $\delta$-discontinuity bounded solution using the available primitives exists (i.e., a path in the graph $G_{\delta,\mathcal{M}}$), Db-A\* may not find it because motions are expanded in a random order and only if no previous node is within distance ${({1 - \alpha})}\delta$. This could potentially prune a node that is required in the solution. Since Db-A\* is incomplete, it cannot guarantee that no better $\delta$-discontinuity bounded solution exists once it finds one. ∎

### Theorem 2

For a given set of motion primitives $\mathcal{M}$, there exists a $\delta > 0$ such that Db-A\* is complete and optimal when searching in the implicit graph $G_{\mathcal{M},\delta}$.

### Proof

If the choice of a given $\delta_{0}$ renders Db-A\* incomplete on the graph $G_{\mathcal{M},\delta_{0}}$, we can always reduce $\delta$, resulting in a different graph, where the nodes in the solution are either not pruned during the Db-A\* search, or the graph becomes unsolvable. Note that since decreasing $\delta$ may render the graph unsolvable, this property is valuable in an asymptotic setting, used to demonstrate asymptotic optimality when incrementally adding more motion primitives. ∎

### VIII-C Optimization

### Assumption 2

(Convergence of the Optimizer) Let $(\mathbf{X}_{d},\mathbf{U}_{d})$ be a $\delta$-discontinuity bounded solution (Definition 2) to the planning problem. Then, there exists a (small) $\delta > 0$ such that trajectory optimization converges to a locally optimal solution $(\mathbf{X}^{\ast},\mathbf{U}^{\ast})$ of the original kinodynamic motion planning problem 3.

*Discussion:* Nonlinear constrained optimization algorithms for trajectory optimization have convergence guarantees toward stationary points: these are either points that satisfy the first-order optimality conditions---thereby converging to a locally optimal feasible solution; or points that locally minimize the constraint violation.

In general, these methods typically require the dynamics, distance function, and collision constraints to have smoothness or bounded derivatives. The exact conditions for convergence can vary slightly among different trajectory optimization algorithms, such as Differential Dynamic Programming, Sequential Convex Optimization, the Augmented Lagrangian, and Interior Points.

Specifically, we assume that for a small $\delta$, the initial guess is close to a feasible solution, thereby ensuring that the optimizer converges to a feasible and locally optimal solution. We argue that this is a very reasonable assumption, especially when the optimal solution is a $\delta$-robust trajectory, as often assumed in the literature. The experimental success rate of our planner (Section IX) also supports this assumption.

### VIII-D Motion Primitives

Our optimization-based approach for generating motion primitives, as well as propagation of random control inputs from random starting points, creates a set of motion primitives that asymptotically covers the state space, which will be required to prove the asymptotic optimality of iDb-A\*.

### Definition 4

A set of primitives $\mathcal{M}$ covers the state space with discontinuity $\epsilon > 0$ if and only if, for all pairs of states ${\mathbf{x},\mathbf{x}'} \in \mathcal{X}$, there exists a $\epsilon$-discontinuity bounded trajectory from $\mathbf{x}$ to $\mathbf{x}'$ (Definition 2) using the primitives $m \in \mathcal{M}$.

### Definition 5

A method to generate motion primitives asymptotically covers the state if, for every $\overset{\sim}{\epsilon} > 0$, there exists a *finite* set of primitives $\overset{\sim}{\mathcal{M}}$, ${|\overset{\sim}{\mathcal{M}}|} < \infty$ such that Definition 4 holds. In other words, asymptotic coverage means that if ${|\mathcal{M}|}\rightarrow\infty$, then $\epsilon\rightarrow 0$ in Definition 4.

### Remark 3

Motion primitives generated with our randomized optimization-based approach, as well as rollouts of random control inputs from random starting points, asymptotically covers the state space.

### VIII-E iDb-A\*

So far, we have demonstrated that there exists a small discontinuity bound $\delta > 0$ such that Db-A\* finds an optimal discontinuity bounded trajectory (if one exists), and that trajectory optimization can be used to repair a $\delta$-discontinuity bounded solution into a locally optimal solution.

To prove asymptotic optimality for iDb-A\*, we use techniques from sampling-based motion planning to show that, as we increase the number of primitives, the solution of Db-A\* converges towards an optimal discontinuity bounded solution (and thus, after optimization, we converge towards the optimal solution). In Algorithm 1, we iteratively reduce $\delta$ to achieve good anytime behavior. For the proof, it is sufficient to assume that we are using a small fixed discontinuity $\overset{\sim}{\delta} > 0$ such that Theorem 2 and 2 hold.

### Theorem 3

If the set of motion primitives asymptotically optimally covers the state space with discontinuity $\overset{\sim}{\delta}$, and assuming convergence of the optimizer, iDb-A\* (Algorithm 1) is asymptotically optimal, i.e., where $c_{n}$ is the cost in iteration $n$ and $c^{\ast}$ is the optimal cost.

### Proof

We closely follow the proof strategy from previous work in sampling-based motion planning \[18, Th. 3\]. Let $S_{1},\ldots,S_{n}$ be random variables denoting the suboptimality $c_{n} - c^{\ast}$. In every iteration of Algorithm 1, we either reduce the cost if we find a new solution or we remain at the same cost, i.e., $c_{n + 1} \leq c_{n}$. We now aim to show that, with sufficient motion primitives, the solution of Db-A\* will be close to the true solution, and thus can be correctly optimized by trajectory optimization. Crucially, in each iteration of iDb-A\*, there is a positive probability that the new primitives will improve the solution, ${E{\lbrack\left. S_{n} \middle| S_{n - 1} \right.\rbrack}} \leq {{({1 - \omega})}S_{n - 1}}$, i.e., in expectation, the solution improves by at least a constant amount $\omega > 0$ every iteration. This nonzero probability only holds if the motion primitives asymptotically cover the entire state space with discontinuity $\overset{\sim}{\delta}$ (Definition 5). Then, we have Applying the Markov inequality, we have ${P{({S_{n} > \epsilon})}} \leq {{E{\lbrack S_{n}\rbrack}}/\epsilon} = {{{({1 - \omega})}^{n - 1}E{\lbrack S_{1}\rbrack}}/\epsilon}$, which approaches 0 as $n$ approaches infinity. ∎ It remains an open question what the theoretical convergence rate of our proposed algorithm is, a property that is known for some sampling-based planners. Empirically, we have shown that our initial solution is often much closer to the optimum compared to our baselines, and that the region of attraction for trajectory optimization is large enough to plan with a few primitives and large discontinuity bounds.

## Experimental Evaluation

Figure 4: Kinodynamic motion planning problems: Start and goal positions are represented in green and red, respectively. Obstacles are depicted in gray. Trajectories computed by iDb-A* are illustrated in blue. (a) Quadrotor v1 – Window, (b) Acrobot – Swing up obstacles v1, (c) Planar rotor – Hole, (d) Rotor pole – Small window, (e) Unicycle 1 v0 – Park.

We evaluate iDb-A\* on 43 problems that include 8 different dynamical systems in various environments. Most of the problems and systems are selected from previous work in kinodynamic motion planning. Additionally, we include several problems that require dynamic and agile maneuvers with multirotors.

The benchmark problems are available in DynoBench, our new benchmark library. It provides a C++ implementation of all the dynamical systems (including dynamics with analytical Jacobians, state, and bound constraints), collision and distance computation with the Flexible Collision Library (FCL), the environments (in human-friendly YAML files), and visualization tools in Python.

Our implementation of iDb-A\* and the other planners is available in our repository, along with the motion primitives and instructions to replicate the benchmark results. A visualization of each problem and the corresponding solution trajectories computed by our algorithm is available on our website.

### IX-A Dynamical Systems and Environments

We include a diverse range of dynamical systems and environments, featuring varying state dimensionality (from 3 to 14), number of underactuated degrees of freedom, and controllability.

Unicycle 1 ($1^{\text{st}}$ order) has a 3-dimensional state space ${\lbrack x,y,\theta\rbrack} \in \mathcal{X} \subset {{{\mathbb{R}}^{2} \times S}O{}}$ and a 2-dimensional velocity control ${\lbrack v,\omega\rbrack} \in \mathcal{U} \subset {\mathbb{R}}^{2}$. The three variants ($\text{v}0$, $\text{v}1$, $\text{v}2$) use different control bounds. See Figs. 1(a) and 4(e) ‣ Figure 4 ‣ IX Experimental Evaluation ‣ iDb-A*: Iterative Search and Optimization for Optimal Kinodynamic Motion Planning").

Unicycle 2 ($2^{\text{nd}}$ order) has a 5-dimensional state space ${\lbrack x,y,\theta,v,\omega\rbrack} \in \mathcal{X} \subset {{{\mathbb{R}}^{4} \times S}O{}}$ and a 2-dimensional acceleration control ${\lbrack\overset{˙}{v},\overset{˙}{\omega}\rbrack} \in \mathcal{U} \subset {\mathbb{R}}^{2}$. See Fig. 5.

Car with trailer has a 4-dimensional state space ${\lbrack x,y,\theta_{0},\theta_{1}\rbrack} \in \mathcal{X} \subset {{{\mathbb{R}}^{2} \times S}O{}^{2}}$ and a 2-dimensional control space ${\lbrack v,\phi\rbrack} \in \mathcal{U} \subset {\mathbb{R}}^{2}$ (steering angle and velocity). See Fig. 1(b).

Acrobot is a two-link planar manipulator actuated only at the middle joint. It requires long trajectories to swing up the two links. See Fig. 4(b).

Quadrotor v0 has a 13-dimensional state space (position, orientation, and first-order derivatives) and a 4-dimensional control space (force for each of the four motors). Dynamics are defined in Example 2, and we use the parameters of the Crazyflie 2.1. The low thrust-to-weight ratio of $1.3$ is very challenging for kinodynamic motion planning, and harsh initial conditions prevent the use of specialized methods. See Fig. 1(d).

Quadrotor v1. The state space is the same as in Quadrotor v0. Controls are the total thrust and torques in the body frame, which make sampling-based methods more efficient but approximate real rotor-force limits. We use the system parameters and model from the OMPL APP repository, but increase the control bounds to perform agile maneuvers. See Fig. 4(a).

Planar rotor. The input is the force in each rotor $\mathbf{u} = {\lbrack f_{1},f_{2}\rbrack} \in {\mathbb{R}}^{2}$ and the state space is 6-dimensional $\mathbf{x} = {\lbrack x,z,\theta,v_{x},v_{y},w\rbrack} \in {{{\mathbb{R}}^{5} \times S}O{}}$. The thrust-to-weight ratio is also limited to $1.3$. See Fig. 4(c).

Rotor pole (Planar multirotor with pole) is a planar multirotor with an additional underactuated pendulum. The control space is the same as in *Planar rotor* (but with larger control bounds) and the state space has two additional degrees of freedom $\lbrack q,\overset{˙}{q}\rbrack$ for the pendulum. See Fig. 4(d).

All systems use the explicit Euler integration, with ${\Deltat} = {0.1\ s}$ for all car-like robots, and ${\Deltat} = {0.01\ s}$ for the flying robots and the Acrobot, due to the fast rotational dynamics.

For most car-like robots, we consider three environments (Kink, Park, Bugtrap). For the Acrobot and multirotors, we use environments with and without obstacles to evaluate performance in settings that require both aggressive maneuvers (e.g., recovering from upside-down positions) and navigation around obstacles.

### IX-B Algorithms

Following our previous work, the goal of this benchmark is to compare methods for kinodynamic motion planning that use different methodologies: search, optimization, and sampling. We compare our algorithm against state-of-the-art methods that have available open-source implementations.

For a search-based approach, we rely on SBPL (Search-based Planning Library), a commonly used C++ library. We generate our own primitives and make minor adjustments to the heuristic to enable time-optimal anytime planning using the provided implementation of ARA\* in SBPL. SBPL requires the motion primitives to be connected without discontinuity and to span a lattice. We limit our evaluation to dynamic models that are readily available in SBPL, namely the Unicycle 1 v0.

For a sampling-based approach, we use SST\*, which is implemented in OMPL (Open Motion Planning Library). Since sampling-based kinodynamic approaches cannot reach a goal state exactly, we use a goal region instead and run subsequent trajectory optimization with fixed terminal time to generate an exact solution to the goal. The reported time does *not* include the time spent in trajectory optimization, thus providing a favorable lower bound.

For optimization-based planning, we choose a classic combination of a geometric motion planner and a trajectory optimizer, which we call RRT^∗^-TO in the following. The motion planner generates an obstacle-free initial guess, ignoring the dynamics of the system, i.e., *planning with a simplified model*, and the optimizer uses this trajectory as an initial guess. As a motion planner, we use geometric RRT\* (using the implementation in OMPL), which provides anytime behavior by incrementally improving the geometric trajectory. Importantly, the probability of finding a feasible solution with optimization might increase when using the multiple geometric initial guesses provided by RRT\*. The initial guess provided by the geometric planner is collision-free but is often not accurate for dynamic constraints. Therefore, for trajectory optimization with free terminal time, we use the strategy Search-T 9 ‣ VI Trajectory Optimization ‣ iDb-A*: Iterative Search and Optimization for Optimal Kinodynamic Motion Planning"), which is more robust and provides better success in this planner than Free-dt, later used in iDb-A^∗^.

For iDb-A\*, we implement Algorithm 1 and Algorithm 2 in C++. As a heuristic $h$, we use the Euclidean-based heuristic (e.g., distance divided by the upper bound of the speed, see Section V-B), because it is general, fast to compute, and does not require precomputation. For trajectory optimization, we use Free-dt (8 ‣ VI Trajectory Optimization ‣ iDb-A*: Iterative Search and Optimization for Optimal Kinodynamic Motion Planning")), which provides a good balance between local optimality and computational time when using a good initial guess, as usually provided by Db-A\*. We provide an ablation study of the choices of heuristic and trajectory optimization strategy in Section IX-E, where we analyze and compare different alternatives.

The rates that control the number of primitives and the discontinuity bound in each iteration of iDb-A^∗^ (Algorithm 1) are set to $n_{r} = 1.5$, $\delta_{r} = 0.9$ in all problems. However, when the search terminates without finding a solution, we keep the discontinuity bound (almost) constant with $\delta_{r} = 0.999$ and only increment the number of primitives with a rate of $n_{r} = 1.5$. The parameter $\alpha$ in Algorithm 2 is set to 0.5. The initial number of motion primitives, discontinuity bound, and hyperparameters of the trajectory optimization are chosen per dynamical system. For example, in all problem instances with Unicycle 1 v0, we start with 100 primitives and a discontinuity $\delta_{0} = 0.3$, and in all instances with Quadrotor v0, we start with 2000 primitives and $\delta_{0} = 0.7$. The distance function $d$ used to measure the distance between states in Db-A^∗^ is a weighted Euclidean norm, which uses different weights for the position, orientation, and velocity components of the state (e.g., in the Unicycle 2 we use weights 1, 0.5, and 0.25, respectively).

The offline generation of a valid primitive takes a few seconds, from $0.1\ s$ for the Unicycle 1 v0 to $6\ s$ for a Quadrotor v0 using a single core of a laptop computer with a CPU i7-1165G7@2.80GHz, where most of the time is spent attempting to solve random two-value boundary problems, which cannot be solved with short trajectories.

The benchmarking infrastructure is written in Python, and all tuning parameters for our algorithms and baselines can be found in our open-source repository.

For nearest-neighbors computation in iDb-A^∗^, SST^∗^, and RRT^∗^-TO, we use NIGH in single-core mode, which provides faster lookup and insertion times than the default Geometric Near-neighbor Access Tree (GNAT) implementation in OMPL. All trajectory optimization algorithms are implemented based on the DDP solver in Crocoddyl.

### IX-C Metrics

In the following, we report the metrics: Success Rate ($p$): The ratio of trials where a solution was found within the planning budget of $120\ s$.

Median time required to find a solution ($t^{\text{st}}$).

Median cost when 50% of the trials have found a solution ($J^{\text{st}}$).

Median cost of the final solution ($J^{\text{f}}$) found within the planning budget of $120\ s$.

### IX-D Benchmark

Figure 5: Example of the first trajectory computed by iDb-A∗, SST∗, and RRT∗-TO in Unicycle 2 – Bugtrap. The orange line in iDb-A∗ and RRT∗-TO shows the initial guess trajectory before optimization. The first solution of iDb-A∗ has the lowest cost (J). The average computational time to get the first solution is 1.2 s in iDb-A∗, 2.8 s in RRT∗-TO, and 0.9 s in SST∗.

We conducted our benchmark on a workstation with a CPU AMD EPYC 7502 32-Core Processor \@2.50 GHz. All planners use a single core. Our results are summarized in Table I, where we provide a selection of 16 problems (two for each dynamical system). For brevity, Table I does not include any standard deviations. The complete results (43 problems) are available on the project webpage. In general, we found that SBPL has almost no variance, SST^∗^ has very high variance, and RRT^∗^-TO and iDb-A^∗^ are somewhere in between the two extremes. The plots in Fig. 6 show the convergence behavior and the variance in three representative problems, which are discussed later.

We summarize the main results as follows: $\bullet$ SBPL has been excluded from the table because it is only readily applicable to the three problems that use *Unicycle 1 v0*. In this setting, it consistently finds a solution in competitive time: $2.1\ s$ in *Bugtrap*, $0.2\ s$ in *Kink*, and $0.1\ s$ in *Park*.

However, due to the limited number of lattice-based primitives, the initial and final costs are rather constant: $36.6$ in *Bugtrap*, $22.6$ in *Kink*, and $6.2$ in *Park* (and higher than the costs achieved by iDb-A^∗^ ).

Car with trailer Car with trailer TABLE I: Benchmark with selected problems. Bold indicates the best result.

Figure 6: Success and cost convergence plots for three representative systems. Cost is only plotted when 50% of the runs have found a solution. The shaded region indicates the 95% non-parametric confidence interval for the median. $\bullet$ SST^∗^ can find an initial solution quickly in problems with car-like dynamics; however, the quality of the initial solution is poor, especially in the larger, higher-dimensional systems. The convergence is slow---our $120\ s$ timeout was not sufficient for SST^∗^ to fully converge in most cases. Notably, in problems involving multirotors, it was unable to find solutions within the time limit for most problems (for instance, we observed a 0% success rate in the dynamics of *Quadrotor v0* and 10% with *Quadrotor v1*). Because SST^∗^ relies on propagating random control inputs, it is very inefficient for multirotor systems, where random inputs quickly bring the system into unstable configurations. However, in low-dimensional and stable dynamical systems like cars and unicycles, it finds the first solution faster but is clearly outperformed in terms of the cost of initial and final solutions by both iDb-A^∗^ and RRT^∗^-TO. $\bullet$ RRT^∗^-TO can find near-optimal initial solutions in some problems but fails if the geometric initial guess is not close to dynamically feasible motion, which occurs more often in environments with flying robots. Thus, the main drawback is that this approach is incomplete, with success rates below 70% on several problems and complete failures in others. The cost at convergence is often worse than that of iDb-A^∗^. In general, we conclude that RRT^∗^-TO is a good method when the simplified model is informative and when the primary challenge is obstacle avoidance. In these settings, it often matches the time to first solution of iDb-A^∗^. $\bullet$ iDb-A^∗^ finds the highest-quality first solution in 14 out of 16 selected problems (better in the $J^{\text{st}}$ column), converged to the lowest-cost solution in 12 out of 16 problems (column $J^{\text{f}}$), and achieved a 100% success rate in 15 out of 16 problems (column $p$) (and 41 out of 43 total problems). The time to generate the first solution (column $t^{\text{st}}$) is competitive with the other approaches in the problems solved by all methods, while it is the only method that consistently solves all problems with multirotor flying robots.

We can conclude that our method performs well across all systems and environments, from navigation among obstacles with car models to recovery flights with control-limited quadrotors. Note that the performance we report here is considerably better than our previous results. This improvement is due to an improved implementation of the search algorithm, a superior trajectory optimization algorithm and formulation, and a better strategy for choosing the number of primitives and the discontinuity bound.

Fig. 5 shows the different first solutions found by iDb-A^∗^, RRT^∗^-TO, and SST^∗^ in the Unicycle 2 -- Bugtrap problem. We also display the convergence and success plots for some instructive problems in Fig. 6: *Rotor pole -- Swing up obstacles*: This problem involves swinging the pole upwards while avoiding obstacles (Fig. 1(c)). Only iDb-A^∗^ consistently solves the problem within a competitive timeframe. On average, RRT^∗^-TO requires 10x more computational time to find a solution and does not achieve a 100% success rate. The disparate performance across runs of RRT^∗^-TO stems from the uninformative geometric guess, which often leads to failure in the subsequent optimization and thus requires multiple trials with different initial guesses. SST^∗^ does not find any solution within the computational budget.

*Quadrotor v1 -- Window*: In this problem, the quadrotor needs to find a path through a window; see Fig. 4(a). SST^∗^ achieves a low success rate because propagating random controls is often inefficient, with a low probability of generating useful trajectories. iDb-A^∗^ consistently solves the problem in at most two seconds and improves the solution with more compute time. RRT^∗^-TO fails to find a solution in some runs and the median cost is considerably higher.

*Unicycle 1 v0 -- Bugtrap*: The *Bugtrap* environment is shown in Fig. 5, but here we use the *Unicycle 1 v0* system instead of *Unicycle 2*. SST^∗^ finds the first solution the fastest, but convergence to the optimum is slow. iDb-A^∗^ is also quick and produces a high-quality solution already in the first iteration. RRT^∗^-TO finds solutions as well but often requires multiple optimization trials to obtain the first valid solution (similar to the previous problems, RRT^∗^-TO has a high variance in the time required to solve the problem). Regarding SBPL, the time to reach the first solution is competitive with the other methods, but due to the limited number of primitives, the solution does not improve.

### IX-E Ablation Studies of iDb-A\*

We analyze the main algorithmic components of iDb-A^∗^ to study the impact on the overall performance and to justify the most important design decisions, namely: Scheduling for increasing/decreasing the number of primitives and the discontinuity bound.

Euclidean heuristic in the search step.

Optimization with free terminal time using Free-dt.

Optimization-based motion primitives.

Invariance/equivariance of motion primitives.

We find a significant interaction between hyperparameters and design decisions, making it challenging to evaluate the impact of each component. For instance, the runtime of the search step with different heuristics is strongly dependent on the number of primitives. Therefore, instead of including more variations of iDb-A^∗^ in our benchmark, we choose to analyze and discuss each component individually, which we believe provides a clearer understanding. The experiments in the ablation study are conducted on a modern laptop computer with a CPU i7-1165G7@2.80GHz (single core), which has single-core performance similar to that of the workstation used.

### IX-E1 Time Spent in Each Component

We first evaluate how much computational time is spent in the search or optimization components, and how this varies when we decrease the discontinuity bound and increase the number of primitives.

Figure 7: Time spent in the search and optimization steps during the first iteration of iDb-A∗ in the Bugtrap environment, with three different dynamical systems and two different discontinuity bounds. The labels u1, u2, and r2 are short names for the systems Unicycle 1 v0, Unicycle 2, and Planar rotor. The number after the hyphen indicates the discontinuity bound; for example, u1-0.3 is Unicycle 1 v0 with δ = 0.3.

Fig. 7 shows an analysis of the computation time spent in the search and optimization during the first iteration of iDb-A^∗^ for three different systems (*Unicycle 1 v0*, *Unicycle 2*, and Planar rotor), using two different values of the discontinuity bound (with a consistent number of motion primitives), in the Bugtrap environment (e.g., Fig. 5).

The total time is predominantly occupied by the search component, where both collision checks and nearest-neighbor queries consume a significant fraction of the computational time. When comparing different values of discontinuity bounds (e.g., *u1-0.3* versus *u1-0.2*), we observe that the search is quicker with a larger discontinuity (and a consistently small number of primitives) because it results in a smaller branching factor and fewer states to expand. The computational time of the optimization component remains roughly constant, even when smaller discontinuity bounds provide a better initial guess.

Comparing across systems (e.g., *u1-0.3* versus *r2-0.5*), the time spent in the search increases with the dimensionality of the system's state space, in line with the theoretical exponential complexity. The optimization time also increases, but it remains a minor fraction of the total time.

This analysis offers valuable insights for selecting the initial discontinuity bound and the number of primitives in iDb-A^∗^. Ideally, the initial number of primitives and the discontinuity bounds should be chosen to be small (primitives) and large (discontinuity) so that 1) the search finds a discontinuous solution quickly, and 2) the optimizer finds a feasible solution. Thus, our recommendation is to "choose the largest discontinuity bound that the trajectory optimization can handle effectively".

### IX-E2 Analysis of Trajectory Optimization with Free Terminal Time

We evaluate the four trajectory optimization approaches discussed in Sec. VI: *(i)* joint trajectory and time optimization (Free-dt), *(ii)* hierarchical time search (Search-T), *(iii)* model predictive control (MPC), and *(iv)* model predictive contouring control (MPCC).

We analyze the computational speed, the success, and the cost value in a set of initial guesses of different discontinuities for some representative problems with different dynamical systems. A summary of the results is shown in Fig. 8 (more extensive results are available on the project webpage).

Figure 8: Analysis of four different strategies for trajectory optimization with free terminal time with six different initial guesses (two per problem). The label r2-bug is short for Planar rotor – Bugtrap, the label q-rec is short for Quadrotor v0 – Recovery, and the label u2-bug is short for Unicycle 2 – Bugtrap. The number after the hyphen indicates the discontinuity bound of each initial guess. A bar reaching the top of the plot indicates the algorithm’s failure to find a solution.

First, we note that the results highlight a strong variation across the dynamical systems, scenarios, and initial guesses. We can draw the following general conclusions: *Robustness*: Free-dt and Search-T are more robust and are able to successfully optimize more initial guesses than MPC and MPCC. On the contrary, MPC and MPCC are harder to tune and sometimes fail, especially for larger values of the discontinuity bound. The sliding window approaches repair the trajectory locally, step by step, and often cannot reach the final goal if doing so requires jointly improving the initial guess trajectory (where we need to propagate information about the goal across the entire trajectory).

*Computation speed*: When MPC and MPCC manage to find a solution, they are the fastest methods. Comparing Free-dt and Search-T, Free-dt is between 1.5 and 5 times faster than Search-T.

*Cost convergence*: The joint approaches Free-dt and Search-T converge to a better cost than the sliding window approaches because they consider the full trajectory at once, but the difference is small.

It is worth noting that compute times for the same problem with different discontinuity bounds are not directly comparable since the initial guesses contain a varying number of steps. Furthermore, these results heavily depend on the underlying optimization algorithm (differential dynamic programming), which effectively addresses the temporal dimension of the trajectory optimization problem (with linear complexity on the number of time steps).

In iDb-A^∗^, the search component consumes more computational time than the optimization process, as illustrated in Fig. 7. In trajectory optimization, we prioritize achieving reliable results and converging to low-cost solutions over computational efficiency. Consequently, Free-dt has been selected as the default optimization algorithm for iDb-A^∗^, striking an optimal balance between convergence, robustness, and computational speed.

### IX-E3 Analysis of Heuristic Functions

Figure 9: Analysis of the heuristic function in Db-A* across six different problems: Unicycle 1 v0 – Bugtrap (u1-bug), Unicycle 2 – Bugtrap (u2-bug), Planar rotor – Bugtrap (r2-bug), Quadrotor v0 – Obstacle (q-obs), Quadrotor v0 – Recovery obstacles (q-recobs), and Rotor pole – Window (r2pole-win). The number of expansions is measured in thousands of units; for example, a value of 100 on the graph represents 100,000 expansions. A bar reaching the top of the plot indicates the algorithm’s failure to find a solution.

We analyze three different heuristic functions to inform the search in Db-A^∗^: the Euclidean heuristic (Euclidean), the roadmap heuristic (Roadmap), and the blind heuristic (Blind) (see Section V).

We report the number of expanded nodes and the computational time for a single search of Db-A^∗^ on six different problems involving obstacles in Fig. 9 (with more extensive results on our webpage). We first note that the comparison is highly dependent on the number of motion primitives and the discontinuity bound. For a large discontinuity bound and a small number of primitives, the search's branching factor is small, and the heuristic is relatively irrelevant; even uninformed exploration can find the goal with few expansions. With an increased number of primitives, the potential states to expand grow, necessitating a good heuristic function.

To better illustrate the differences between heuristics, we evaluate Db-A^∗^ with smaller discontinuity values (and correspondingly higher numbers of primitives) than those used in the first iteration of iDb-A^∗^ in the main benchmark, resulting in many more expansions and computational time.

The Roadmap heuristic does not include precomputation time, which requires building a coarse roadmap and computing the optimal cost-to-go for all nodes. This process takes approximately $50\ {ms}$ for the unicycles, $70\ {ms}$ for the Planar rotor (with roadmaps of 1,000 configurations), and $400\ {ms}$ for the Quadrotor v0 (with a roadmap of 3,000 configurations).

We observe that the Roadmap heuristic is the most informative (as it considers obstacles) and reduces the number of expanded nodes in all selected problems. However, in some cases, the Euclidean heuristic is competitive in terms of compute time (and even faster for some problems), as it is quicker to evaluate because the Roadmap requires a k-d tree search with every evaluation. The Blind heuristic fails to solve some problems within the time limit of $30\ s$. Based on these results, in our algorithm, we select the Euclidean heuristic because it requires no precomputation or additional hyperparameters, and it is informative and rapid for all dynamical systems.

### IX-E4 Motion Primitives - Optimization vs. Sampling

We also evaluated the performance of iDb-A^∗^ using motion primitives with random controls (i.e., short trajectories generated by sampling controls uniformly at random within bounds), as opposed to our optimization-based motion primitives.

For car-like robots, the success, convergence, and computation time of iDb-A^∗^ are similar with both strategies. The cost of the discontinuity-bounded trajectories produced in the search step using primitives with random controls is often higher, but the optimization step successfully improves these trajectories, achieving a similar cost in the final feasible trajectory. Conversely, motion primitives with random controls often fail to solve problems with flying robots, where such primitives frequently result in unstable final intermediate configurations and erratic trajectories (as exemplified by the performance of SST^∗^ with flying robots in the benchmark).

### IX-E5 Motion Primitives -- Invariance and Equivariance

All systems, except for the Acrobot, exhibit a form of invariance or equivariance. Using invariance, the same primitive can be transformed on-the-fly (e.g., translated) to be applicable in different states with smaller discontinuity values (Section V-D). For car-like robots, we leverage only translation invariance (Example 4. ‣ VII-B Invariance and Equivariance in System Dynamics ‣ VII Motion Primitives ‣ iDb-A*: Iterative Search and Optimization for Optimal Kinodynamic Motion Planning")). For flying robots, we utilize translation and linear velocity invariance in the second-order dynamics (Example 5. ‣ VII-B Invariance and Equivariance in System Dynamics ‣ VII Motion Primitives ‣ iDb-A*: Iterative Search and Optimization for Optimal Kinodynamic Motion Planning")). Since the number of motion primitives required to attain a given coverage resolution grows exponentially with each dimension, exploiting invariance is crucial for planning with a reduced number of primitives. For instance, we use only 2,000 primitives for the Quadrotor v0 in the first iteration of iDb-A^∗^ by utilizing translation and velocity invariance. With only translation invariance, over 50,000 primitives would be required to achieve comparable levels of discontinuity.

### IX-F Limitations and Future Work

From a practical standpoint, the main limitation of iDb-A^∗^ is that it necessitates a preliminary offline step to generate motion primitives. Moreover, adding a new dynamical system requires solid theoretical and practical knowledge of two different paradigms in motion planning: search and trajectory optimization, and the interplay between them to choose some important hyperparameters. In this sense, the method is more complex than sample-based motion planners.

The number of required motion primitives grows exponentially with the state dimension. To mitigate this issue, a possible solution is to use a more informative distance metric (instead of the weighted Euclidean metric) when deciding which primitive to apply, which correlates better with the underlying dynamics and the subsequent trajectory optimization. Additionally, more informed sampling strategies for start and goal configurations when generating motion primitives could reduce the number of primitives needed.

To improve the computation time required to find the first solution in some problems (e.g., $1.5\ s$ in Quadrotor v0 - Recovery obstacles or $12.3\ s$ in Planar rotor - Bugtrap) and scale to larger environments with more obstacles, we see great potential in combining our discontinuity-based approach with an RRT-like planner, instead of an incremental A\* search. We are also interested in exploring hybrid approaches between our method and the control propagation used .

## Conclusion

We present iDb-A\*, a new kinodynamic motion planner that combines a novel graph-search method with trajectory optimization iteratively. For the graph search, we introduce Db-A\*, a generalization of A\* that reuses motion primitives to compute trajectories with bounded discontinuity, which are later used as a warm start for trajectory optimization. iDb-A\* amalgamates the ideas and advantages of sampling-based, search-based, and optimization-based kinodynamic motion planners: it converges asymptotically to the optimal solution, rapidly finds a near-optimal solution, and does not require any additional post-processing.

We evaluate iDb-A\* on a diverse set of challenging, time-optimal kinodynamic motion planning problems, from obstacle avoidance with car-like robots to highly dynamic maneuvers with quadcopters. iDb-A\* consistently outperforms other algorithms on these benchmarks and solves problems that were beyond the capabilities of previous motion planners.

The main limitation is that the number of motion primitives required grows exponentially with the state dimension, which poses a challenge to systems with higher dimensionality.

Finally, we believe that our combination of search, sampling, and optimization lays the foundation for novel kinodynamic planners for robotic manipulation and contact planning.
