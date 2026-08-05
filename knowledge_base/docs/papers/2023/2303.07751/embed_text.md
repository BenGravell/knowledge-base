<!-- arxiv-full-text:v1 {"arxiv_id": "2303.07751", "source": "ar5iv"} -->

## Introduction

Mobile robots have the potential to automate logistic tasks ranging from indoor transportation tasks, as found in automated warehouses and hospitals, to outdoor transportation tasks, such as package delivery. One of the major challenges for mobile robots is to move safely among humans.

Dynamic collision avoidance constraints are usually imposed on the motion of the robot, making its free configuration space nonconvex. In fact, each obstacle in a 2-D environment leads to at least two possible driving behaviors for the robot: passing left or right.

Existing motion planners are either local or global. Local planners typically remain in the driving behavior that they are initialized . This may lead to poor performance (e.g. long travel times) if a higher performance driving behavior exists, but is not explored. Because of the limited scope, these planners are typically fast and can consider detailed dynamic models. Global planners explore and find the optimal driving behavior and motion plan, but can suffer from high computation times when the robot dynamical model is considered.

A common approach in the presence of static obstacles is to find a high-level path using a global planner. This path is passed to a local motion planner which improves the quality of the plan locally. The majority of existing works following this hierarchy do not consider dynamic obstacles in their global planner, they delegate dynamic collision avoidance to the local planner directly. Although this is computationally faster, it fails to address that when obstacles move, the set of driving behaviors becomes richer, since the planner needs to decide when and *how* to pass the obstacles. Fig. 1 illustrates these driving behaviors by looking at the planning problem in a 3-D state space consisting of 2-D position and bounded time. Each driving behavior travels through a distinct section of the state space and can therefore be identified by analyzing their topology in the collision-free space.

(a) Topview of a crossing scenario.

(b) Topologically distinct trajectories in the 3-D state space.

Figure 1: An illustration of how topologically distinct guidance trajectories explore driving behaviors for a scenario where two pedestrians cross at the same time.

In this work we explicitly consider the possible driving behaviors in a dynamic environment by planning topologically distinct guidance trajectories in the state space. We select the most suitable guidance trajectory based on a high-level cost. This trajectory is passed to a Model Predictive Contouring Controller (MPCC) that locally optimizes the motion of the robot while following the selected guidance trajectory, resulting in a fast and safe motion plan.

### Related Work

Local optimization can be leveraged to plan locally optimal trajectories. Model Predictive Control (MPC) is often used to optimize planning performance (e.g., speed and comfort) while satisfying constraints (e.g., collision avoidance, vehicle model, actuator limits) offering a flexible and safe framework that can include road following and dynamic collision avoidance in the deterministic and uncertain case. A limitation of MPC motion planners is that their solution is only guaranteed to be locally optimal, which can lead to unsafe or unexpected driving behavior when the local optimum corresponds to unsuitable (e.g., aggressive or slow) driving behavior.

Global planners such as Rapidly expanding Random Trees (RRT), RRT\* and Probabilistic RoadMaps (PRM) in principle resolve this issue, but are typically not fast enough to consider dynamic obstacles, especially when the robot's dynamic constraints are considered.

Topology-based planning methods identify driving behaviors through the environment by comparing trajectory topologies. When two trajectories can be smoothly transformed into each other without colliding with an obstacle, they are *homotopy* equivalent. In, methods using this measure are divided in three groups. The first group plans in a given homotopy class, for example, road rules are used in to motivate a desired homotopy class in highway driving.

The second group leverages structure in the environment to enumerate possible homotopy classes after which trajectories in a subset of the classes are computed. An example of this approach is where a 2-D workspace is decomposed with a trapezoidal decomposition. Similarly, , homotopy classes are derived from the road structure. The works, compute a homology^11^1Homology differs slightly from homotopy. See for definitions. invariant that for each obstacle identifies the rotations of a path around it. Graphs extended with this invariant can be used to plan a path in each homology class.

The third group evaluates the homotopy of a trajectory after it is found. In the homology invariant from is applied to extend a PRM graph around static obstacles and the resulting high-level trajectories are optimized by a local planner. An alternative to homotopy, Universal Visibility Deformation (UVD) (based on VD ), introduced in efficiently compares the topology of two trajectories. A UVD aware visibility-PRM (see ) is presented to plan mulitple distinct trajectories in real-time for drone flight. The same method is leveraged in and to achieve state-of-the-art results for drone flight in static environments.

Previous works in the second group plan among dynamic obstacles in the state space, all of which assume and leverage road structure. Works in the third group plan drone flight in unstructured 3-D environments, but do not consider dynamic obstacles.

### Contribution

In this work, we present a method in the third group, based on to plan trajectories through dynamic environments without relying on road structure. The contributions of this work are as follows: A planner that considers multiple topologically distinct high-level trajectories in dynamic environments, without assuming a structured environment. The most suitable trajectory is selected as initialization (guidance) for a local planner.

An algorithm to identify and propagate topology information of trajectories to successive iterations, making the planner behavior stable and consistent.

We validate the proposed planner on a mobile robot both in simulation and in real-world experiments. Our results indicate that the addition of the high-level planner results in faster trajectories, where this improvement increases as the driving scenarios become more crowded. In addition, we observe less collisions in crowded scenarios. Our planner is implemented in ROS/C++ and will be released open-source.

## Problem Formulation

We model the robot motion by the deterministic discrete-time nonlinear dynamics where ${\mathbf{x}}_{k} \in {\mathbb{R}}^{n_{x}}$ and ${\mathbf{u}}_{k} \in {\mathbb{R}}^{n_{u}}$ are the state and input at discrete time instance $k$, $n_{x}$ and $n_{u}$ are the state and input dimensions respectively and the state contains the 2-D position of the robot ${\mathbf{p}}_{k} = {(x_{k},y_{k})} \in {\mathbb{R}}^{2} \subseteq {\mathbb{R}}^{n_{x}}$. Obstacles move in the same space as the robot. The position of obstacle $j$ at time $k = 0$ is denoted ${\mathbf{o}}_{0}^{j} \in {\mathbb{R}}^{2}$ and we assume that for each obstacle predictions of its motion over the next $N$ time steps (i.e., ${\mathbf{o}}_{1}^{j},\ldots,{\mathbf{o}}_{N}^{j}$) are available to the robot at each time instance. We model the obstacles and robot area with a single disc each, with radius $r_{\text{obs}}$ and $r$, respectively. We further assume that the robot is given a high-level reference path to follow, e.g., a straight line to the goal. The robot tracks the reference path through the workspace (it can deviate from it) without colliding with the obstacles.

## Global Guidance

The proposed planner consists of two components, the first computes a global guidance trajectory to guide the second component, a local planner, to the global optimum in the dynamic environment. We design the guidance trajectory search to be light-weight and fast, giving an estimate in the vicinity of the global optimum. The local planner is initialized from the guidance trajectory and leverages more accurate robot models and constraints to locally obtain a safe high quality trajectory.

(a) Visibility-PRM graph, with spheres denoting guards (orange), start and goal (red) and connector nodes (colored).

(b) Geometric paths (colored lines) and cubic spline points (cubes) before (green) and after optimization (black).

(c) Guidance trajectories with the picked trajectory (dark blue) thickened.

Figure 2: Our high-level guidance method, viewed in the state space 𝒳. (a) A graph is constructed using visibility-PRM. (b) Geometric paths are found through graph-search and are sampled and smoothed. (c) Cubic splines are fitted through the resulting points. Based on a high-level cost, one guidance trajectory is selected, to be tracked by a local planner.

### III-A Dynamic Trajectory Planning

We explicitly consider multiple local optimal driving behaviors in the presence of dynamic obstacles by planning high-level collision-free paths in the state space. The state space, composed of the workspace and time, is described by $\mathcal{X} = {{\mathbb{R}}^{2} \times {\lbrack 0,T\rbrack}}$, with $\lbrack 0,T\rbrack$ a continuous domain. A trajectory is a continuous path through the state space, ${\mathbf{τ}}:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{X}}$. The area of the workspace occupied by the union of obstacles at time t is denoted by $\mathcal{O}_{t} \subset {\mathbb{R}}^{2}$ and the obstacle set in the state space is thus $\mathcal{O}:={\bigcup_{{\forall t} \in {\lbrack 0,T\rbrack}}{(\mathcal{O}_{t},t)}} \subset \mathcal{X}$. Obstacles puncture holes in the state space, which make the collision-free space nonconvex and results in the existence of multiple locally optimal trajectories.

The topology of trajectories can be analyzed to identify a single trajectory for each local optimum. To distinguish trajectory topologies, we require a comparison function, We then seek to find the set of topologically distinct trajectories $\mathcal{T}^{\ast} = {\{{\mathbf{τ}}_{0},{\mathbf{τ}}_{1},\ldots,{\mathbf{τ}}_{N_{\tau}}\}}$ in the workspace, where In this work, we adopt the topology measure UVD. Two trajectories are in the same UVD class (topology equivalent) if points along the trajectories can be connected, without intersecting with obstacles.

### Definition 1

Two trajectories ${{\mathbf{τ}}_{1}{(s)}},{{\mathbf{τ}}_{2}{(s)}}$ parameterized by $s \in {\lbrack 0,1\rbrack}$ and satisfying ${{\mathbf{τ}}_{1}{}} = {{\mathbf{τ}}_{2}{}}$, ${{\mathbf{τ}}_{1}{}} = {{\mathbf{τ}}_{2}{}}$, belong to the same uniform visibility deformation class, if for all $s$, line $\overline{{\mathbf{τ}}_{1}{(s)}{\mathbf{τ}}_{2}{(s)}}$ is collision-free.

In practice, we check collisions for $s$ at discrete intervals along the trajectories.

### III-B Visibility-PRM

We build on Visibility-PRM to compute a sparse representation of the paths from start to goal, with distinct topologies. We introduce important adaptations to repurpose the approach in the state space domain, that includes time, to ensure that the algorithm gives consistent outputs over successive time steps. The modified Visibility-PRM algorithm is given in Algorithm 1 and is detailed below.

PRM initializes its graph with start (${\mathbf{x}}_{0}$) and goal (${\mathbf{x}}_{N}$) nodes. States for new nodes are drawn at random from a feasible state distribution ${\mathbf{x}}^{(i)} \sim {\mathbb{P}}_{\text{PRM}}$ (NewSample line $8$) and if possible, the new node is connected to the graph.

Visibility-PRM distinguishes between Guard and Connector nodes, as follows, to ensure that the graph is sparse. The start and goal nodes are initialized as guards (lines $1$, $2$). For each new sample, we find the guards that it can be connected to without colliding (VisibleGuards line $9$). If it connects to $0$ guards, it is added as *guard* (AddGuard line $11$). When a sample connects to exactly $2$ guards, it becomes a *connector* (InitializeConnector line $17$). For connectors we verify that the connection is dynamically feasible (ConnectionInvalid lines $13$, $15$). We then construct a piecewise linear path (Path) between a connector and the guards. Lines $22$-$29$ replace an existing connector when the newly sampled connector is in the same UVD class and the new path is shorter. New connectors with a distinct UVD class are added by AddConnector in line $32$.

A depth-first graph search augmented with a visited node list, similar to, computes paths on the graph from start to goal, giving the UVD distinct trajectories $\mathcal{T}^{\ast}$. We refer to these trajectories as the *geometric trajectories*. An example of the result is visualized in Fig. 2(a).

Input: 𝒪, x0, xN, Previous nodes 𝒢− 4while Below sample and time limit do 5 reintroduce ← Not all samples 𝒢− were reintroduced 13 if |ℒ| = 0 (No guards visible) then 15 else if |ℒ| = 2 (Exactly 2 guards visible) then 30 for Shared neighbour xj, 𝒩j of x, 𝒩 in ℒ do 35 if Length(τ) < Length(τj) then 36 Transfer the segment ID of 𝒩j to 𝒩 37 In 𝒢, replace connector 𝒩j with 𝒩 43 if reintroduce is False then 44 Initialize segment ID of 𝒩 with unused ID Algorithm 1 Proposed Visibility-PRM

### III-C Propagating Guidance Trajectories

Because the search for guidance trajectories is repeated at each time step, consistency between successive iterations must be guaranteed to prevent the robot from switching between different trajectories. We address this by marking nodes in the graph with a topology identifier, then reintroducing the nodes in the next iteration with their identifiers. This allows us to reidentify and favour the selected guidance trajectory from the previous iteration.

Each segment consisting of a connector and two guards is in a distinct UVD class by construction. We assign to each connector $i$ a *segment ID*, $\alpha_{i} \in {\mathbb{Z}}^{+}$, that uniquely identifies this segment (line $31$). When a connector is replaced, the ID is transferred (line $27$). This is illustrated in Fig. 3.

(a) Segments with new topology (b) Segments with existing topology Figure 3: Each segment is associated with a topological ID. (a) Two segments with new distinct topologies are given unique IDs. (b) A new connector creates a shorter segment within an existing topology, the ID is transferred.

Each geometric trajectory is composed of one or more segments. We associate each geometric trajectory $i$ with a *trajectory ID*, $\beta_{i} \in {\mathbb{Z}}^{+}$ and maintain a mapping between each trajectory and its segments, making it possible to reidentify each trajectory in successive iterations. For example if trajectory ${\mathbf{τ}}_{1}$ with ID $\beta_{i} = 1$ contains segments ${\alpha_{1} = 1},{\alpha_{2} = 4}$, we first save the mapping $1\rightarrow{\{ 1,4\}}$. In the next iteration, a trajectory consisting of segments $1,4$ is reassigned the ID $1$.

In line $6$ of Algorithm 1, ReintroduceSample reintroduces all nodes of the previous graph ($\mathcal{G}^{-}$) before sampling new states. Because a sampling time passes between these iterations, the time coordinate of each node $(x,y,t)$ in the previous graph needs to be updated to $(x,y,{t - h})$, where $h$ is the sampling time. When the time coordinate becomes zero, we resample a new node halfway along the trajectory.

Since the connectors possess a segment ID, the segment associations are carried over from the previous iteration (line $19$). After new paths are found, we reidentify previous trajectories from their segments. These steps result in consistent identification of UVD distinct trajectories and improve the overall planner performance, since trajectories and their topology are propagated to successive iterations.

### III-D Spline Optimization

The geometric trajectories do not satisfy the kinematic constraints of the robot (they are discontinuous) and therefore cannot be followed by a low-level controller. We smoothen these trajectories in two steps as visualized in Figs. 2(b) and 2(c). The first step samples the trajectories and optimizes the resulting points. The second step fits a smooth curve through the optimized points.

### Step 1

We first convert the state space paths to time parameterized trajectories, ${\mathbf{τ}}_{geometric}:{{\lbrack 0,T\rbrack}\rightarrow{\mathbb{R}}^{2}}$. Each trajectory is sampled with regular intervals $\Deltat$ to obtain a set of control points ${\mathbf{Q}} = {\lbrack{\mathbf{Q}}_{0},\ldots,{\mathbf{Q}}_{N}\rbrack}$, with ${\mathbf{Q}}_{i} \in {\mathbb{R}}^{2}$.

We optimize these control points to improve smoothness both in position and velocity. The optimization problem is designed to be quadratic and unconstrained to minimize computation times. We define the cost as where the geometric cost penalizes distance to the original control points $\overline{\mathbf{Q}}$ on the geometric trajectory, The smoothness cost functions as an elastic band that smoothens the trajectory.

The obstacle cost is designed to penalize the linear distance $d_{i}^{j}$ from control point $i$ to the obstacle $j$ by an exponential penalty. To keep the cost quadratic however, we use the second order Taylor expansion. Let ${\mathbf{A}}_{i,j} = {{\overline{\mathbf{Q}}}_{i} - {\mathbf{o}}_{k}^{j}}$, where time index $k$ matches the time associated with ${\mathbf{Q}}_{i}$. Then the cost is given by $J_{\text{obst}} = {{\sum_{i}{\sum_{j}{{\mathbf{Q}}_{i}^{T}{\mathbf{H}}_{i,j}{\mathbf{Q}}_{i}}}} + {{\mathbf{f}}_{i,j}^{T}{\mathbf{Q}}_{i}}}$, with The velocity cost penalizes an offset with respect to a tracking velocity $v_{\text{ref}}$. We compute this cost by constructing a trajectory that satisfies the velocity tracking cost everywhere, based on the geometric trajectory. We then penalize the distance to that trajectory. The velocity control points of the geometric path can be computed using Then the associated velocity optimized path is given by with ${\mathbf{Q}}_{0}^{v}$ equal to the current velocity of the robot. The velocity cost matches with $\overline{\mathbf{Q}}$ replaced by ${\mathbf{Q}}^{v}$.

### Step 2

Since the optimization problem is quadratic and unconstrained, we obtain the solution in closed-form. We fit cubic splines separately through the optimized $x$ and $y$ position of the control points to obtain a continuous trajectory, consisting of segments ${{\mathbf{τ}}^{i}{(t)}} = \begin{bmatrix} \end{bmatrix}^{T}$, with $\tau_{x}^{i}$ (and $\tau_{y}^{i}$) given by which is twice continuously differentiable and passes through the control points. We impose a boundary condition on the initial velocity of the trajectories to ensure that it respects the robot's current velocity. For more details on fitting the cubic splines, we refer to. The cubic splines together form a smooth trajectory ${\mathbf{τ}}:{{\lbrack 0,T\rbrack}\rightarrow{\mathbb{R}}^{2}}$ from the current robot position to the goal (see Fig. 2(c)). Guidance trajectory $\mathbf{τ}$ is not guaranteed to be collision-free, but is smooth enough to be used by a local planner that enforces collision avoidance.

### III-E Spline Selection

From the candidate splines generated in each control iteration, we need to select the guidance trajectory that best represents the performance indicators for the robot's motion. We consider the following criteria: Minimize path length - preferring short paths.

Minimize difference to preferred velocity - penalizing too fast or slow driving.

Minimize acceleration - preferring smooth trajectories.

Consistency - ensuring that when another trajectory improves over the selected trajectory of the previous control iteration, it should significantly outperform it.

We compute the costs for each trajectory by taking samples of positions ${\mathbf{p}}_{i}$, velocities ${\mathbf{v}}_{i}$ and accelerations ${\mathbf{a}}_{i}$ at constant time intervals along the trajectory, resulting in the objective | | $J_{\text{select}} =$ | $\sum\limits_{i \in \mathcal{I}}{w_{L}{\|{{\mathbf{p}}_{i} - {{\mathbf{p}}_{i - 1}{\|{+ w_{V}}\|}{\|{\mathbf{v}}_{i}\|}} - \overline{v}}\|}}$ | | \(9\) | where $\mathcal{I}$ is the number of samples, $w$ denotes weights, $\overline{v}$ is the reference velocity, $\alpha \approx 1$ to discount accelerations later in the trajectory and $C$ denotes a constant penalty if this trajectory was not selected in the previous iteration. We select the lowest cost trajectory (thickened in Fig. 2(c)).

## Local Planning

The local planner needs to plan a kinematically feasible motion that is collision-free, since this is not guaranteed by the guidance trajectory. We introduce the guidance trajectory to the local planner in two ways. First, the solver is initialized with the guidance trajectory. This in itself may not be sufficient to converge to the desired optimum. We therefore also follow the guidance trajectory by using an MPCC as local planner. This planner is designed to follow the path traced by the guidance trajectory while tracking its velocity.

The objective of the MPCC is given by where $J_{c,k}$ and $J_{l,k}$ denote the lag and contouring costs as, the velocity reference tracking is enforced via $J_{v,k} = {\|{v_{k} - {\overline{v}}_{k}}\|}$, where ${\overline{v}}_{k}$ is the velocity on the guidance trajectory at time step $k$, and the costs $J_{a,k}$ and $J_{\omega,k}$ penalize actuation.

To avoid obstacles one would typically use nonconvex constraints ${\|{{\mathbf{p}}_{k} - {\mathbf{o}}_{k}}\|} \geq {r + r_{\text{obs}}}$. However, in practice these may result in switching between local optima, without giving a consistent solution. We employ the linearized version of these constraints, the linear constraint orthogonal to the vector between the robot and obstacle, ${{\mathbf{A}}^{T}{\mathbf{p}}_{k}} \leq b$, where These constraints result in consistent and smooth motion^22^2In principle we could run a local planner for each guidance trajectory in parallel and choose the best one. This is left for future work..

TABLE I: Experimental settings. Weights are denoted “(w)”.

## results

We validate our approach in simulation and real-world experiments, comparing in both cases against a local planner without guidance. Our planner is implemented in ROS/C++ and will be released open-source. A video of the simulations and experiments is available .

### V-A Notes on Implementation

Experimental settings are given in Table I. The high-level planner is fast enough to plan over a longer horizon than the local planner while remaining real-time (i.e., $N_{\text{PRM}} > N_{\text{MPCC}}$). In crowded scenarios, this leads to smoother trajectories as the robot can adapt its high-level maneuvre earlier. We select the goal for PRM as the point along the reference path reached when the robot drives at the preferred velocity. It is projected to the nearest collision-free position if necessary. When the goal cannot be reached, we reduce the horizon. PRM nodes are sampled (i.e., ${\mathbb{P}}_{\text{PRM}}$) in a forward directed arc considering velocity and acceleration limits.

Figure 4: Snapshots of the simulations, viewed in the state-space. Pedestrians (black discs) are visualized with their predicted area (colored disc) inflated by the robot area. Visualization of the graph and guidance trajectories are identical to Fig. 2. The robot’s local motion plan is denoted by blue discs, indicating the predicted area occupied by the robot.

Computation Time High-Level Planning [ms] TABLE II: Statistical results for the task duration, number of collisions and computation times when comparing MPCC with and without guidance over 200 simulations each in 4 different scenarios. Results are denoted as “avg (std)” over experiments except for collisions. We denote with “High-Level Planning” the time spent to compute the guidance trajectory.

Figure 5: A comparison of trajectories with and without guidance in a randomized environment with 8 pedestrians.

### V-B Simulated Guidance Ablation Study

Our simulations consider four environments with pedestrians. The first environment (*head-on*) consists of a straight road with two pedestrians moving towards the robot. The other environments contain $4,8$ and $16$ pedestrians with random start positions and velocities near the reference path. The random scenarios are identical for all planners (i.e., we use the same random seed). In all simulations, pedestrians move with constant velocity. We reset the simulation when the robot reaches the end of the road in the x-direction and repeat each experiment $200$ times.

Statistical results are given in Table II and snapshots are shown in Fig. 4. The guidance allows the robot to consistently navigate around the pedestrians in the head-on scenario. Without guidance, indecisiveness of the planner leads to infeasibility and collisions in most simulations. In the randomized environments, the guidance reduces the task duration by $2,3$ and $5\%$, with a larger improvement in more crowded environments. Trajectories for the $8$ pedestrian case, visualized in Fig. 5, show that guidance allows the planner to choose faster driving behaviors. Guidance MPCC collides slightly more often than the baseline. When obstacles block the path, the high-level planner may not find a guidance trajectory. We then use the last computed guidance trajectory, which can lead to collisions. Future work may resolve this problem by considering multiple goals.

Figure 6: Trajectories recorded in the real-world experiments for the robot (dark blue) and pedestrians (green). Start positions are denoted in black.

### V-C Real-World Experiments

We deploy the proposed planner experimentally on a mobile robot (Clearpath Jackal) navigating among pedestrians. The robot is equipped with an Intel i5 CPU@2.6GHz. Localization of the robot and pedestrians is obtained from a marker based tracking system and pedestrian predictions assume constant velocity, where the velocity is obtained from Kalman filtered position data.

Trajectories for $2$ scenarios and the setup are visualized in Fig. 6. In the first scenario, the guidance allows the robot to pass behind the last pedestrian. In the second scenario, the robot moves left to evade both pedestrians efficiently.

## Conclusion

This work presented a novel planner for autonomous navigation in dynamic environments. The planner finds distinct high-level trajectories to guide a local optimization-based planner to a global optimal plan. Guidance trajectories are computed and tracked over successive control iterations.

We showed that the resulting planner leads to shorter average task duration times than the local planner in isolation, with larger improvement in crowded environments. Real-world experiments further validated the proposed approach.

Further research could explore applications of the guidance trajectory search to predict human motion or to endow the local planner with socially compliant motion.
