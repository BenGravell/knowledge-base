<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Interleaving Optimization with Sampling-Based Motion Planning (IOS-MP): Combining Local Optimization with Global Exploration

Topics include Motion planning, Sampling-based planning, Trajectory optimization, Asymptotically optimal planning, Local optimization, Global exploration, Robot motion planning, Homotopy classes.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Proposes IOS-MP, a hybrid planning loop that alternates between sampling-based global exploration and local trajectory optimization. The key idea is to keep broad coverage of different homotopy classes while continually refining promising paths, addressing a weakness of purely asymptotically optimal planners and purely local optimizers.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Computing globally optimal motion plans for a robot is challenging in part because it requires analyzing a robot's configuration space simultaneously from both a macroscopic viewpoint (i.e., considering paths in multiple homotopic classes) and a microscopic viewpoint (i.e., locally optimizing path quality). We introduce Interleaved Optimization with Sampling-based Motion Planning (IOS-MP), a new method that effectively combines global exploration and local optimization to quickly compute high quality motion plans. Our approach combines two paradigms: asymptotically-optimal sampling-based motion planning, which is effective at global exploration but relatively slow at locally refining paths, and optimization-based motion planning, which locally optimizes paths quickly but lacks a global view of the configuration space. IOS-MP iteratively alternates between global exploration and local optimization, sharing information between the two, to improve motion planning efficiency. We evaluate IOS-MP as it scales with respect to dimensionality and complexity, as well as demonstrate its effectiveness on a 7-DOF manipulator for tasks specified using goal configurations and workspace goal regions.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robots are increasingly entering domains such as transportation, surgery, and home assistance where safe interaction with people is critical. This interaction motivates robots which are capable of planning high quality motions under short time horizons. Unfortunately, the landscape of feasible motion plans in a robot's configuration space can be extremely complex, consisting of many local minima, with paths spanning multiple homotopic classes. The complexity of this landscape means that an ideal motion planning algorithm must employ a macroscopic global view, considering paths in multiple homotopic classes, while also taking a microscopic local view, ensuring plans are as close to locally optimal as possible. Our work focusses on unifying these two perspectives by interleaving path refinement through local optimization, with global exploration through sampling-based motion planning. In this way, we compute high quality, locally optimized plans while continuing to explore the global landscape for as long as time allows.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Sampling-based motion planning methods typically take the macroscopic view, drawing samples from the robot's entire configuration space to build a graph that progressively covers more and more of the space. The global nature of these algorithms allows them to explore every relevant homotopic class eventually. Many of these methods will also converge upon the globally optimal solution as the number of samples approaches infinity. Unfortunately, the resulting paths may converge slowly, so in *finite* time, they frequently return paths that are far from locally optimal, especially in higher dimensional problems.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Optimization-based motion planning methods take a more microscopic approach. These methods quickly compute high quality paths by numerically optimizing an initial path, converging toward a local minimum. However, the resulting path quality of such methods is directly tied to the path initialization. Due to the inherently non-convex nature of motion planning with obstacles, for some initializations the resulting paths may be far from globally optimal, or the optimization may not find a solution at all. This limitation can be partially circumvented through techniques such as restarting the optimization with multiple different initial paths (e.g., ), but such approaches are heuristically driven and typically provide no global guarantees. Additionally, by treating each restart as independent, they potentially ignore useful pre-computed information (such as collision-free configurations) that could be valuable if shared across restarts.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Our new method, Interleaved Optimization with Sampling-based Motion Planning (IOS-MP), alternates between local optimization and global exploration, sharing information between the two, effectively combining the best of both of these paradigms (see Fig. 1: Combining Local Optimization with Global Exploration")). IOS-MP starts with global exploration by building a graph using an asymptotically optimal motion planner, such as $k$-nearest Probabilistic Roadmap (PRM\*) or Batch Informed Trees (BIT\*), until it finds a collision free path (Fig. 1: Combining Local Optimization with Global Exploration")(a) top). IOS-MP then uses constrained local optimization based on an augmented Lagrangian method to refine the path found by the sampling-based method (Fig. 1: Combining Local Optimization with Global Exploration")(a) bottom). The algorithm then iterates between resuming the sampling-based motion planner until a new better path is found and running constrained local optimization on this new path (see Fig. 1: Combining Local Optimization with Global Exploration")(b),(c)).

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

The sampling-based motion planning phase of each iteration explores globally, discovering other homotopic classes in configuration space, as well as escaping local minima in the path cost landscape. The constrained local optimization phase in turn allows the method to provide a high quality local solution at the end of each iteration. For efficiency, information is shared by both of the phases at each iteration, with the sampling-based method seeding the local optimization with improving initial solutions, and the local optimization passing potentially valuable new vertices and edges to the sampling-based method.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

IOS-MP is an *anytime* motion planning algorithm, in that the algorithm can be stopped at any time (after iteration 1) and return a locally optimized path, and running the algorithm for more time will return locally optimized paths that asymptotically approach a globally optimal path. The framework we introduce is generalizable; while our implementation uses augmented Lagrangian optimization and PRM\* or BIT\*, other local optimization algorithms and other sampling-based planning algorithms can be substituted in as long as the formulations and constraints described in this paper can be applied. The contribution of this paper is in describing and evaluating a framework for constructing a motion planning algorithm which leverages both local path optimization and global exploration. This allows it to provide higher quality paths earlier than asymptotically optimal sampling-based motion planning algorithms alone can provide, while providing the guarantees---namely completeness and asymptotic optimality---which are not provided by most optimization-based motion planning algorithms.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper we optimize trajectories with respect to path length. We demonstrate IOS-MP's efficacy in simulated environments of varying dimensionality and complexity as well as for a 7 degree of freedom (DOF) manipulator performing tasks defined by both goal configurations and workspace goal regions.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

Let $C$ be the configuration space of the robot. Let $\mathbf{q} \in C$ represent a single robot configuration and $\mathbf{p} = {\{\mathbf{q}_{0},\mathbf{q}_{1},\ldots,\mathbf{q}_{n}\}}$ be a continuous path in configuration space represented in a piecewise manner by a sequence of configurations. In this paper, we minimize the path with respect to the length, where we define $\text{length}{(\mathbf{p})}$ to be the sum of Euclidean distances in configuration space along the path. We use the sum of Euclidean distances because it is a commonly used metric for path length and because it satisfies the triangle inequality property required by asymptotically optimal sampling-based motion planners (unlike other metrics such as sum of squared distances). While we use path length for our optimization objective, certain other cost functions that are continuous, differentiable, and do not violate the triangle inequality could be used instead.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

In the robot's workspace are obstacles that must be avoided. Each obstacle may be composed of a set of obstacle primitives, and let the set of primitives composing all obstacles be $O$. Let $C_{\text{free}} \subseteq C$ be the collision free subspace and $C_{\text{obs}} \subseteq C$ be the in-collision subspace of $C$ based on obstacle primitives $O$. In the context of this work, we are considering static environments, such that $C_{\text{obs}}$ is unchanging as a function of time. A path is collision-free if each edge ${{{(\mathbf{q}_{i},\mathbf{q}_{i + 1})},i} = 0},{\ldots,{{|\mathbf{p}|} - 1}}$, does not intersect an obstacle primitive $o \in O$.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

Formally, we define $\text{clearance}{(\mathbf{q}_{i},\mathbf{q}_{i + 1},o)}$ as the signed squared distance between the path *edge* $(\mathbf{q}_{i},\mathbf{q}_{i + 1})$ and obstacle primitive $o$ (where negative values correspond to obstacle penetration distance); a collision-free path is a path for which each edge has non-negative clearance. This requires that the obstacle and robot representations allow for the computation, either analytically or numerically, of the signed distance between the robot and the obstacle primitive. This property holds for robots and obstacles represented using collections of bounding spheres or bounding capsules (volumes defined by a sphere swept along a straight line segment) as well as point clouds and other representations, which are common representations used in the literature and useful in practice.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

The optimal motion planning problem then becomes finding a collision-free path from $\mathbf{q}_{\text{start}}$ to $\mathbf{q}_{\text{goal}} \in C_{\text{goal}}$ that minimizes cost, where $C_{\text{goal}}$ is the (possibly singleton) set of goal configurations. This optimal motion planning problem can be formulated as a nonlinear, constrained optimization problem: where $J$ is a set of generalized inequality constraints that are specific to the problem and robot (e.g., to represent joint angle limits for a manipulator), and where $\mathbf{p}^{\ast}$ is the optimal motion plan. Let $K$ be the set of inequality constraints implied by $O$ for obstacle avoidance. The set of all inequality constraints then becomes $I = {J{\bigcup K}}$. IOS-MP is an iterative algorithm for efficiently solving this problem such that the solution asymptotically approaches $\mathbf{p}^{\ast}$.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Method", "weight": 1.0} -->

IOS-MP integrates ideas from both sampling-based and optimization-based motion planning. The method interleaves path optimization steps with graph expansion steps to achieve fast convergence.

<!-- chunk {"id": "body-0016", "role": "body", "section": "IV-A Overview", "weight": 1.0} -->

The top level algorithm for IOS-MP, Alg. 1: Combining Local Optimization with Global Exploration"), runs in an anytime manner, iterating as time allows and storing the best path found up to any time.

<!-- chunk {"id": "body-0017", "role": "body", "section": "IV-A Overview", "weight": 1.0} -->

Input: start configuration qstart, obstacle set O, time limit t Output: motion plan p* 4 while time elapsed ≤ t do 7 $\hat{\mathbf{p}}\leftarrow{\text{optimizationStep}{(\mathbf{p})}}$ 8 $c\leftarrow{\text{cost}{(\hat{\mathbf{p}})}}$ 9 $G\leftarrow{G{\bigcup\hat{\mathbf{p}}}}$ 10 $\mathbf{p}^{\ast}\leftarrow\hat{\mathbf{p}}$ In the first step of each iteration, IOS-MP executes a sampling-based motion planner to expand the graph $G$ until a new path is found that has cost lower than $c$. The sampling-based motion planner returns the new path $\mathbf{p}$ and updates $c$. In the second step of each iteration, IOS-MP executes a local optimization method to locally optimize $\mathbf{p}$.

<!-- chunk {"id": "body-0018", "role": "body", "section": "IV-A Overview", "weight": 1.0} -->

The method saves the optimized path $\hat{\mathbf{p}}$ as the best new motion plan found. It also adds the configurations and segments defining $\hat{\mathbf{p}}$ as new vertices in $G$. The algorithm then iterates, returning to global exploration with the sampling-based motion planner, but seeded with vertices and edges generated by both the prior random sampling and the local optimization.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-B Global Exploration using Sampling-based Motion Planning", "weight": 1.0} -->

The global exploration step uses a sampling-based motion planner to expand a graph until a new path---spanning from the start configuration to any goal configuration---is found that is of lower cost than any previously found path. The sampling-based motion planner maintains a graph $G = {(V,E)}$, where $V$ is a set of vertices which represent collision-free configurations of the robot and $E$ is a set of edges, where an edge represents a collision-free transition between two robot configurations.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-B Global Exploration using Sampling-based Motion Planning", "weight": 1.0} -->

To expand the graph $G$, our method is designed to use an asymptotically optimal sampling based motion planner such as $k$-nearest Probabilistic Roadmap (PRM\*). PRM\* samples random configurations in the robot's configuration space, locates their $k$ nearest neighbors (where $k$ changes as a function of the number of vertices in the graph), and attempts to connect the configurations to each of its neighbors (connection step). In each graph expansion step, PRM\* executes until a path better than the current best is found, at which point the optimization step begins. We require that the algorithm randomly samples and attempts to connect at least one vertex in between consecutive optimization steps, to ensure that the global exploration continues. We refer to IOS-MP with $k$-nearest PRM\* for its sampling-based planning step as IOS-MP (PRM\*).

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Global Exploration using Sampling-based Motion Planning", "weight": 1.0} -->

IOS-MP can alternatively be used with other asymptotically optimal motion planners, such as Batch Informed Trees (BIT\*). BIT\* operates by processing samples in batches. From a batch of samples it builds a tree using a graph search heuristic during tree construction until a solution is found or the tree can no longer be expanded. For the next batch, it limits its sampling to the subspace in which a solution of higher quality could be found. For IOS-MP with BIT\*, the usual BIT\* algorithm executes for a short amount of time without interruption ($\leq 0.2$ seconds) to take advantage of its batching properties. After the short execution, the best path found by BIT\* is evaluated against the previous best, and if it has improved, it is optimized. We refer to IOS-MP with BIT\* for its sampling-based planning step as IOS-MP (BIT\*). In Sec. V: Combining Local Optimization with Global Exploration"), we show results for both when PRM\* and when BIT\* are used within IOS-MP.

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-C Local Optimization using an Augmented Lagrangian Method", "weight": 1.0} -->

For the local optimization step, we use a nonlinear constrained optimization method called the augmented Lagrangian (AL) method to locally optimize the path. AL is similar to standard Lagrangian methods, in that it utilizes Lagrangian multipliers, but differs in that it adds additional quadratic constraint terms. AL is also similar to penalty-based optimization methods, but by introducing explicit Lagrange multiplier estimates at each step of the optimization, in practice it is able to reduce ill conditioning.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-C Local Optimization using an Augmented Lagrangian Method", "weight": 1.0} -->

We apply AL to the nonlinear constrained optimization problem in (1: Combining Local Optimization with Global Exploration")), where the initial value for $\mathbf{p}$ is the most recent path found by the sampling-based method. The AL method iteratively minimizes the augmented Lagrangian function, $\mathcal{L}_{A}$ defined in (2: Combining Local Optimization with Global Exploration")) and (3: Combining Local Optimization with Global Exploration")), based on each constraint $g_{i}$ in the set of constraints $I$, and an iterative approximation of the Lagrangian multipliers $\lambda$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-C Local Optimization using an Augmented Lagrangian Method", "weight": 1.0} -->

At the $k^{th}$ step of the AL algorithm, outlined in Alg. 2: Combining Local Optimization with Global Exploration"), $\mathcal{L}_{A}$ is minimized with respect to the trajectory $\mathbf{p}_{k}$. In our implementation we use gradient descent with line search for this minimization.

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-C Local Optimization using an Augmented Lagrangian Method", "weight": 1.0} -->

Output: optimized path p Algorithm 2 The Augmented Lagrangian method After the minimization, for each inequality constraint $i \in I$, its associated Lagrangian multiplier $\lambda_{i}$ is then updated using the following formula.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-C Local Optimization using an Augmented Lagrangian Method", "weight": 1.0} -->

Penalty multiplier $\mu$ is then updated by multiplying it by a parameter $\mu_{up}:{0 < \mu_{up} < 1}$. The algorithm then updates the augmented Lagrangian function and iteration continues until convergence of $\mathbf{p}$.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-C Local Optimization using an Augmented Lagrangian Method", "weight": 1.0} -->

For IOS-MP, $f{(\mathbf{p})}$ is path length, and the set of inequality constraints $I$ in (1: Combining Local Optimization with Global Exploration")) is the union of the problem-specific inequality constraints $J$ and the obstacle avoidance constraints. For obstacle avoidance, the set of inequality constraints $K$ consists of a constraint per obstacle primitive per pair of adjacent configurations in $\mathbf{p}$. For a path $\mathbf{p}$ consisting of $k$ configurations, there will be ${({k - 1})} \cdot {|O|}$ inequality constraints related to obstacle avoidance, as we require the edge between configurations to be collision free.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-C Local Optimization using an Augmented Lagrangian Method", "weight": 1.0} -->

In the case of motion planning from one configuration to another configuration, the AL method does not update these two configurations but rather updates only the configurations between the start and goal. In this way, the equality constraints $\mathbf{q}_{0} = \mathbf{q}_{\text{start}}$ and $\mathbf{q}_{|\mathbf{p}|} = \mathbf{q}_{\text{goal}}$ are trivially enforced. In the case of goal regions, an additional inequality constraint is added to guarantee that the goal configuration remains within the goal region. Also in practice, to guarantee timely exit, we enforce maximum iteration counts for both the internal minimization and the outside AL loop.

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-D Analysis", "weight": 1.0} -->

We show that IOS-MP (PRM\*), a variant of IOS-MP that uses $k$-nearest PRM\* for its sampling-based planning step, is asymptotically optimal. To ensure that paths computed asymptotically approach the globally optimal path, we must ensure that adding vertices to the graph based on the optimization step does not affect the asymptotic optimality properties of the sampling-based motion planner. We do this by making a distinction between vertices added by the sampling-based method and vertices added by the optimization. We only count vertices added by the sampling-based method toward the $k$-nearest neighbor count when adding edges. Because of this distinction, we can show that IOS-MP (PRM\*) produces a valid supergraph of what PRM\* would have produced, were the optimization steps of IOS-MP (PRM\*) not performed. The behavior, as time progresses, of IOS-MP (PRM\*) can be conceptualized as the behavior of PRM\* with *finite* time interruptions occurring periodically during which the optimization steps are performed.

<!-- chunk {"id": "body-0030", "role": "body", "section": "Assumption 1", "weight": 1.0} -->

The optimization step is guaranteed to exit in finite time.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Assumption 2", "weight": 1.0} -->

The order and configurations randomly sampled by the graph construction algorithm are unchanged from what they would be were there no optimization steps occurring.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-A Dimensionality and Complexity Scaling", "weight": 1.0} -->

To evaluate how the method scales with respect to both configuration space dimensionality and environmental complexity, we evaluate IOS-MP for a point robot in a unit box of dimension $d$. We varied $d$ from 2 to 8 and varied the number of obstacle primitives from as few as 25 to as many as 100. In each environment of dimension $d$ we randomly placed obstacles in the form of hyperspheres of dimension $d$, i.e., circles for 2D, spheres for 3D, and hyperspheres for 4D and 8D. The radii of each obstacle was a random number sampled from a uniform distribution in the range \[0.05,0.2\]. We defined the start and goal configurations for the point robot as points at the centers of opposite faces of the box. In the optimization formulation for (1: Combining Local Optimization with Global Exploration")), we used inequality constraints for clearance from the hypersphere obstacles. An example environment for 2D is shown in Fig. 1: Combining Local Optimization with Global Exploration").

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-A Dimensionality and Complexity Scaling", "weight": 1.0} -->

We show the relative performance of IOS-MP (PRM\*), IOS-MP (BIT\*), PRM\*, BIT\*, and Optimization (based on a local augmented Lagrangian method) for scenarios of different dimensionality and environment complexity in Fig. 2: Combining Local Optimization with Global Exploration"). In each plot, we ran the IOS-MP variants and the sampling-based methods in an anytime manner for 25 seconds, considering the best solution found over time and averaging over runs in 15 environments. For Optimization, we initialized the algorithm with a straight line path in configuration space from start to goal and a fixed number of trajectory points and ran the algorithm until convergence for each of the 15 environments. Optimization does not always succeed in finding a solution (it was successful in $86\%$ of the point robot scenarios represented here); because of this, we computed averages only across runs for which a collision-free solution was found and plot a $\ast$ for this average.

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-A Dimensionality and Complexity Scaling", "weight": 1.0} -->

To display meaningful averages across the 15 environments for each graph, we defined the "best solution" for a particular environment as the shortest path found by any method at any time for that environment, and then averaged over ratios with respect to the best solution in each environment.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-A Dimensionality and Complexity Scaling", "weight": 1.0} -->

In Fig. 2: Combining Local Optimization with Global Exploration"), both IOS-MP (BIT\*) and IOS-MP (PRM\*) outperform their sampling only counterparts in every case, and outperform optimization-based motion planning in most cases, with IOS-MP (BIT\*) being the best all around method. The results show that the sampling-based methods PRM\* and BIT\* perform relatively well in the lower dimensionality cases, especially where the environment is complex (i.e. many obstacle primitives), while local optimization performs increasingly well as the dimensionality increases. By interleaving sampling-based methods and local optimization, IOS-MP gains the speed of both of these methods on these different types of problems. When looking at the trend from left to right of Fig. 2: Combining Local Optimization with Global Exploration"), dimensionality increases, and the percent of configuration space that is free also rises because the number and average radius of the obstacles is held constant.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-A Dimensionality and Complexity Scaling", "weight": 1.0} -->

Because local optimization is relatively more efficient at reducing the length of a path in higher dimensional configuration spaces that are more sparse, IOS-MP is particularly effective for these higher dimensional problems compared to the motion planners that only use sampling-based methods.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-B 7-DOF Manipulation Tasks", "weight": 1.0} -->

We demonstrate IOS-MP's efficacy in various 7-DOF manipulation tasks with the arm of a Fetch robot.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-B1 Motion Planning to a Goal Configuration", "weight": 1.0} -->

In the first scenario (Fig. 3: Combining Local Optimization with Global Exploration")), the Fetch robot must plan a motion from its start configuration, where its arm is beneath a ladder to grasp a tool, to a goal configuration, where its arm is above the ladder, as if handing off the tool to a person above. The ladder and robot links were represented by 8 capsule primitives. In the optimization formulation for (1: Combining Local Optimization with Global Exploration")), we used inequality constraints for obstacles avoidance, to represent joint limits, and to guarantee the robot does not self-collide.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-B1 Motion Planning to a Goal Configuration", "weight": 1.0} -->

Fig. 3c: Combining Local Optimization with Global Exploration") shows the results of applying PRM\*, BIT\*, IOS-MP (PRM\*), and IOS-MP (BIT\*) to this motion planning problem. The methods were run for 120 seconds, recording the path length based on Euclidean distance in configuration space of the best path found up to that time. Additionally, we evaluated augmented Lagrangian local optimization, initialized with a 20-point straight line path in configuration space, but this method did not converge to a valid collision-free solution.

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-B1 Motion Planning to a Goal Configuration", "weight": 1.0} -->

In this scenario, both IOS-MP (PRM\*) and IOS-MP (BIT\*) drastically outperform their sampling-only counterparts. In just a couple of iterations, the loop of sampling-based methods and local optimization produces better plans than other methods produce in 120 seconds. The high dimensionality of the problem means that the optimization step of IOS-MP can provide a large benefit in a short time. Fig. 3: Combining Local Optimization with Global Exploration") illustrates (a) a path found during the graph expansion step of IOS-MP (PRM\*), and (b) the path after the optimization step of the same iteration of IOS-MP. The optimization step of IOS-MP significantly reduces extraneous motion, and iterating with both a sampling-based step and optimization step allows for fast improvement toward a globally optimal solution.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-B2 Motion Planning to a Workspace Goal Region", "weight": 1.0} -->

In the second scenario, the Fetch robot is placed in a more cluttered scene (see Fig.4: Combining Local Optimization with Global Exploration")) and must plan a path starting from a start configuration, in which it is reaching up as if to grab a tool from a person on the ladder, and moving such that its end-effector enters a goal *region* in the workspace under the ladder. We randomly perturb the location of the workspace goal region under the ladder and average the results of 80 runs. The ladder, robot, and other obstacle geometries are being represented in this scene using 16 capsule obstacle primitives. In this scenario, the goal is not a specific configuration, but a potentially infinite number of configurations, all configurations in which the end effector is within a workspace region. In fact, in configuration space the goal region may be both non-convex and disconnected. To solve this motion planning problem, the robot must consider many possible paths across multiple homotopic classes that may pass between different rungs or around the side of the ladder.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-B2 Motion Planning to a Workspace Goal Region", "weight": 1.0} -->

During execution, IOS-MP (PRM\*) incrementally discovers and explores the goal region as the PRM\* graph is constructed. As configurations which lay within the goal region are sampled, they are added to the set of goal configurations to which the planner is attempting to connect to from the start configuration. In the optimization formulation for this scenario, we add an additional inequality constraint, the end effector's proximity to the workspace goal region, which requires the end effector to remain within the workspace goal region during optimization, however the goal configuration is allowed to vary during the optimization as long as the constraint is respected at convergence. Due to goal region restrictions in the OMPL 1.2.1 BIT\* implementation, we only evaluate IOS-MP (PRM\*) and PRM\* for this scenario. To evaluate the efficacy of sharing information from the optimizer with the roadmap we show results for which the optimized paths from IOS-MP are added back into the roadmap and results for which they are not. To average multiple runs we show results beginning at the instant the first path was found.

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-B2 Motion Planning to a Workspace Goal Region", "weight": 1.0} -->

Fig. 4: Combining Local Optimization with Global Exploration")(a-b) depicts paths which exist in two separate homotopic classes, demonstrating the effectiveness of the global nature of the sampling-based planning while still benefiting from the optimization of the paths found. Fig. 4: Combining Local Optimization with Global Exploration")(c) also shows that IOS-MP (PRM\*) performs very well compared to the sampling-based planner alone, and demonstrates the substantial benefit of adding the optimized path back into the roadmap.

<!-- chunk {"id": "body-0044", "role": "body", "section": "Conclusion", "weight": 1.5} -->

In this paper, we present a method designed to achieve the best of both local optimization and global sampling-based motion planning. Through interleaving local optimization with global exploration, and sharing valuable information between the two, our method works in an anytime fashion, providing locally optimized solutions as of the most recent optimization step, while still providing global asymptotic optimality. We demonstrate that our method, integrated with both PRM\* and BIT\*, performs well compared to local optimization or sampling-based methods alone in experiments of varying environmental complexity and dimensionality. In the future, we plan to investigate integrating IOS-MP with other optimization methods, such as sequential quadratic programming, using cost functions other than path length, and using different obstacle primitives.
