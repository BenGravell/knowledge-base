<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

iDb-RRT: Sampling-based Kinodynamic Motion Planning with Motion Primitives and Trajectory Optimization

Topics include Kinodynamic planning, Rapidly-exploring random tree, iDb-RRT, Motion primitives, Trajectory optimization, Discontinuity bounded.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Combines short motion primitives (allowing bounded discontinuities) with the RRT exploration strategy, iteratively repairing discontinuities via trajectory optimization. Finds solutions up to 10X faster than prior methods across a benchmark of 30 problems.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Rapidly-exploring Random Trees (RRT) and its variations have emerged as a robust and efficient tool for finding collision-free paths in robotic systems. However, adding dynamic constraints makes the motion planning problem significantly harder, as it requires solving two-value boundary problems (computationally expensive) or propagating random control inputs (uninformative). Alternatively, Iterative Discontinuity Bounded A* (iDb-A*), introduced in our previous study, combines search and optimization iteratively. The search step connects short trajectories (motion primitives) while allowing a bounded discontinuity between the motion primitives, which is later repaired in the trajectory optimization step. Building upon these foundations, in this paper, we present iDb-RRT, a sampling-based kinodynamic motion planning algorithm that combines motion primitives and trajectory optimization within the RRT framework. iDb-RRT is probabilistically complete and can be implemented in forward or bidirectional mode.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

Kinodynamic motion planning is a fundamental problem in robotics where the goal is to find collision-free trajectories in high-dimensional, continuous, and non-convex spaces, while also considering actuation limits and dynamics of the robot. Over the last two decades, a wide variety of sampling-, search-, and optimization-based methods have been proposed to address (kinodynamic) motion planning problems.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

A breakthrough was the introduction of Rapidly-exploring Random Trees (RRT), a sampling-based method that incrementally builds a tree of configurations by expanding nodes towards randomly sampled new configurations. RRT-like algorithms (e.g., ) are highly efficient for geometric planning, i.e., motion planning settings that involve only joint configurations of the system, since in the geometric setting, two configurations can be connected exactly by using linear interpolation.

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Although RRT-like algorithms can be adapted for kinodynamic motion planning (e.g., ), their efficiency significantly decreases, as they typically require solving multiple two-point boundary value problems or the propagation of random control inputs. Two-point boundary problems, as they arise for most robotic systems, often do not have an analytic solution, and solving them is computationally expensive, generally requiring the solution of a nonlinear trajectory optimization problem. Propagating random control inputs tends to be uninformative for many systems, as random controls can lead to poor exploration of the state space, particularly in highly nonlinear systems such as quadrotors where random inputs often lead to instability in the system. Further, it is not clear how to perform a bidirectional search, as in RRT-Connect, in the kinodynamic setting with the propagation of random inputs.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Alternative approaches for kinodynamic motion planning are optimization-based methods, which scale polynomially instead of exponentially but require an initial guess and may fail to converge; and search-based methods, which provide strong theoretical guarantees but require a pre-defined discretization of the state or control space. More recently, hybrid methods have been proposed to merge the strengths of the three previous approaches to kinodynamic motion planning. Iterative Discontinuity-Bounded A\* (iDb-A\*) introduces an approach based on A\*-search with *motion primitives*, i.e., short and locally optimal trajectories, that are connected not necessarily exactly, but allowing for a bounded discontinuity between primitives. These discontinuities between the motion primitives are later rectified using trajectory optimization (TO). By iteratively combining optimization and search with an increasing number of motion primitives and a reduced discontinuity bound, this method achieves asymptotically optimal motion planning and outperforms state-of-the-art methods across various robotic systems.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

A primary limitation of iDb-A\* is its inefficiency in finding an initial solution, particularly in large environments, where the time required to find the initial solution remains high.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we combine the strengths of the exploration of RRT with the concept of discontinuities between motion primitives and trajectory optimization. We present iDb-RRT (iterative Discontinuity-bounded RRT), a new kinodynamic motion planning algorithm that builds on the ideas of allowing discontinuities in an initial motion from iDb-A\*, and integrates the RRT exploration strategy with short motion primitives and trajectory optimization. iDb-RRT samples a random configuration, then expands the configuration that is closest using applicable motion primitives with bounded discontinuity. Once a solution is found, we employ trajectory optimization to correct the discontinuities between motion primitives. By incrementally increasing the number of primitives and reducing the allowed discontinuity, our algorithm achieves probabilistic completeness.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

We analyze both a forward and a bidirectional version of iDb-RRT. In the open-source benchmark Dynobench comprising 30 problems across 8 different systems, iDb-RRT significantly outperforms state-of-the-art methods in initial solution time, especially in complex scenarios requiring long-horizon planning or navigating through narrow passages.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

We consider a robot with a continuous state $\mathbf{x} \in \mathcal{X}$ (e.g., $\mathcal{X} \subseteq {\mathbb{R}}^{d_{x}}$) and a control vector $\mathbf{u} \in \mathcal{U} \subset {\mathbb{R}}^{d_{u}}$. The dynamics of the robot are deterministic, described by a differential equation,

<!-- chunk {"id": "body-0012", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

To employ gradient-based optimization, we assume that we can compute the Jacobian of $\mathbf{f}$ with respect to $\mathbf{x}$ and $\mathbf{u}$, typically available in systems studied in kinodynamic motion planning, such as mobile robots or rigid-body articulated systems. We use $\mathcal{X}_{\text{free}} \subseteq \mathcal{X}$ to denote the collision-free space, i.e., the subset of states that are not in collision with the obstacles in the environment.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

We discretize the dynamics with a zero-order hold, i.e., we assume the applied control is constant during a time step of duration $\Delta t$. The discretized dynamics can then be written as,

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

using a small $\Delta t$ to ensure the accuracy of the Euler approximation.

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

We use $K \in {\mathbb{N}}$ to denote the number of time steps (which is not fixed but subject to optimization), $\mathbf{X} = {\langle\mathbf{x}_{0},\mathbf{x}_{1},\ldots,\mathbf{x}_{K}\rangle}$ to denote the sequence of states sampled at times $0,{\Delta t},\ldots,{K\Delta t}$ and $\mathbf{U} = {\langle\mathbf{u}_{0},\mathbf{u}_{1},\ldots,\mathbf{u}_{K - 1}\rangle}$ to denote the sequence of controls applied to the system for the time frames ${\lbrack 0,{\Delta t})},{\lbrack{\Delta t},{2\Delta t})},\ldots,{\lbrack{{({K - 1})}\Delta t},{K\Delta

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

t})}$. The objective of navigating the robot from its start state $\mathbf{x}_{s}$ to a goal state $\mathbf{x}_{g}$ can then be framed as the search problem,

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

In this paper we focus on finding a valid trajectory quickly (i.e, very little compute time), as opposed to finding the optimal solution. Although there is no explicit minimization of a cost function in our algorithms, we can evaluate the cost of the trajectory a posteriori. We use the cost term ${J{(\mathbf{U},\mathbf{X})}} = {\sum_{k = 0}^{K - 1}{j{(\mathbf{u}_{k},\mathbf{x}_{k})}\Delta t}}$, with ${j{(\mathbf{u}_{k},\mathbf{x}_{k})}} = 1$ for minimal time (span) (alternatively, one might use ${j{(\mathbf{u}_{k},\mathbf{x}_{k})}} = {\|\mathbf{u}_{k}\|}^{2}$ for minimal control effort).

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem Definition", "weight": 1.0} -->

We assume the dynamics function $\text{step}{(\mathbf{x},\mathbf{u})}$, control space $\mathcal{U}$, state space $\mathcal{X}$, and cost function $j{(\mathbf{x},\mathbf{u})}$, are known before solving the problem, which allows us to precompute motion primitives.

<!-- chunk {"id": "body-0019", "role": "body", "section": "IV-A Background", "weight": 1.0} -->

Our approach relies on two concepts, that we now define.

<!-- chunk {"id": "body-0020", "role": "body", "section": "IV-B Overview", "weight": 1.0} -->

Our approach is summarized in Algorithm 1. We assume that a large set of motion primitives $\mathcal{M}_{L}$ has been precomputed and is available before planning.

<!-- chunk {"id": "body-0021", "role": "body", "section": "IV-B Overview", "weight": 1.0} -->

An RRT search algorithm that connects motion primitives with bounded discontinuity, called Db-RRT. The output is a discontinuity bounded solution, i.e., a collision-free trajectory with bounded violation of dynamic constraints (Definition 1 ‣ IV-A Background ‣ IV iDb-RRT ‣ iDb-RRT: Sampling-based Kinodynamic Motion Planning with Motion Primitives and Trajectory Optimization")).

<!-- chunk {"id": "body-0022", "role": "body", "section": "IV-B Overview", "weight": 1.0} -->

Gradient-based trajectory optimization, which attempts to repair the discontinuities between the motion primitives to produce a dynamically feasible trajectory.

<!-- chunk {"id": "body-0023", "role": "body", "section": "IV-B Overview", "weight": 1.0} -->

If the search fails to find a solution within a given timeout (TerminateCondition), we increase the number of available motion primitives. If gradient-based optimization fails, we reduce the allowed discontinuity. In practice, we typically require only one or two outer iterations (that is, a call to the search and optimization algorithms) to find a solution. We decrease the allowed discontinuity following a geometric sequence, $d_{i} = {d_{i - 1} \cdot d_{r}}$ with a fixed rate $d_{r} < 1$, and increase the number of primitives also following a geometric sequence $m_{i} = {m_{i - 1} \cdot m_{r}}$ with a fixed rate $m_{r} > 1$.

<!-- chunk {"id": "body-0024", "role": "body", "section": "IV-B Overview", "weight": 1.0} -->

Input: xs, xg, step, 𝒳free, 𝒰, ℳL
δ ← δ0 ⊳ Choose initial discontinuity bound
ℳ ← 𝙲𝚑𝚘𝚘𝚜𝚎𝙿𝚛𝚒𝚖𝚒𝚝𝚒𝚟𝚎𝚜(ℳL) ⊳ Choose initial subset of primitives from ℳL
1 while not found do
2 Xd, Ud← db-RRT(xs, xg, 𝒳free, ℳ, δ) if Xd, Ud successfully computed then
3 X, U← Optimization(Xd, Ud, xs, xg, step, 𝒳free, 𝒰) if X, U successfully computed then
Return(X, U) ⊳ New solution found
Algorithm 1 iDb-RRT – Iterative Discontinuity Bounded RRT

<!-- chunk {"id": "body-0025", "role": "body", "section": "IV-C Db-RRT: RRT with Motion Primitives", "weight": 1.0} -->

Db-RRT is an RRT algorithm that connects motion primitives with bounded discontinuity, following the general RRT algorithm to choose the next state to expand. This approach provides a Voronoi bias (i.e., nodes at the frontier of the search tree are more likely to get expanded), thus rapidly exploring the feasible state space. In Algorithm 2, we describe our Db-RRT algorithm and highlight our modifications from RRT. In Db-RRT, the expansion operation is performed using motion primitives with bounded discontinuity. Given the state $\mathbf{x}_{\text{near}}$, we assess which primitives are applicable (e.g., Algorithm 3 in Algorithm 3). We then differentiate between focused expansion (Algorithm 3), where we select the primitive that brings us closest to $\mathbf{x}_{\text{rand}}$ from a finite number of nearby candidates, and uninformed expansion (Algorithm 4), where we choose one collision-free primitive at random. With a small probability (the so-called goal bias), we expand towards the goal state instead of a random state.

<!-- chunk {"id": "body-0026", "role": "body", "section": "IV-C Db-RRT: RRT with Motion Primitives", "weight": 1.0} -->

We stop when we find a state that is within a distance lower than $\delta$ of the goal state. Further, the value of $\delta$ is also used to avoid creating nodes in the tree that are too close to previously discovered nodes.

<!-- chunk {"id": "body-0027", "role": "body", "section": "IV-C Db-RRT: RRT with Motion Primitives", "weight": 1.0} -->

Both expansion strategies are guaranteed to find a solution, if one exists, given sufficient compute time. The inherent trade-off is that Algorithm 3 requires more compute time, as it involves evaluating collisions for multiple motion primitives, but it provides a more focused and uniform expansion. In our implementation, we utilize Algorithm 3 for expansions towards the goal and Algorithm 4 for expansions towards random nodes, but any combination of these two approaches is valid. Focused and uninformed expansion are analogous to guided Monte-Carlo and Monte-Carlo propagation in classic RRT literature, but in Db-RRT we use motion primitives instead of randomly sampled controls.

<!-- chunk {"id": "body-0028", "role": "body", "section": "IV-C Db-RRT: RRT with Motion Primitives", "weight": 1.0} -->

2 if rand &lt; goalBias then
6 xnearest ← 𝙽𝚎𝚊𝚛𝚎𝚜𝚝(𝒯,xrand) xnew, m ← 𝙴𝚡𝚙𝚊𝚗𝚍𝙳𝚋(xnearest,xrand,𝒳free,ℳ,δ) if xnew ≠ NULL then
𝒯 ← 𝙰𝚍𝚍𝙽𝚘𝚍𝚎(𝒯,xnew) Xd, Ud ← 𝚃𝚛𝚊𝚌𝚎𝚋𝚊𝚌𝚔𝚃𝚛𝚊𝚓𝚎𝚌𝚝𝚘𝚛𝚢(𝒯,xnew) Return(Xd, Ud) ⊳ Discontinuity bounded solution
9 else if NearestDistance (𝒯, xnew) &gt; δ then
Algorithm 2 Db-RRT – Rapidly-Exploring Random Trees with Motion Primitives

<!-- chunk {"id": "body-0029", "role": "body", "section": "IV-D Db-RRT-Connect and other Db-RRT variants", "weight": 1.0} -->

The expansion step of Db-RRT can be integrated with many of the variations and enhancements of RRT that have been previously proposed,

<!-- chunk {"id": "body-0030", "role": "body", "section": "Backward and Bidirectional Search", "weight": 1.0} -->

Inspired by RRT-Connect, we present a bidirectional variant of Db-RRT, where we grow two trees, one from the start (using standard motion primitives) and one from the goal (using reversed motion primitives), and attempt to connect them. The expansion step in a backward search mirrors that of a forward search but requires reversing the order of states and controls in the motion primitives beforehand. The two trees are connected if two of their states are within the discontinuity bound.

<!-- chunk {"id": "body-0031", "role": "body", "section": "Asymptotically Optimal Algorithms", "weight": 1.0} -->

Db-RRT can also be applied to RRT variants that require connecting two states precisely, instead of only expanding the state towards random targets. The discontinuity bound $\delta$ can be leveraged to consider two states as equivalent---thereby enabling their exact connection in any rewiring step, such as in RRT\*. Such rewiring steps, which are essential for the asymptotic optimality of RRT\* and its variants, are already implemented in iDb-A\*.

<!-- chunk {"id": "body-0032", "role": "body", "section": "Asymptotically Optimal Algorithms", "weight": 1.0} -->

Return NULL, NULL
Algorithm 3 Expand-Db: Focused

<!-- chunk {"id": "body-0033", "role": "body", "section": "Asymptotically Optimal Algorithms", "weight": 1.0} -->

Return NULL, NULL
Algorithm 4 Expand-Db: Randomized

<!-- chunk {"id": "body-0034", "role": "body", "section": "IV-E Trajectory Optimization", "weight": 1.0} -->

The output of Db-RRT is a sequence of states and controls that connects the start and goal states with a bounded discontinuity, see Definition 1 ‣ IV-A Background ‣ IV iDb-RRT ‣ iDb-RRT: Sampling-based Kinodynamic Motion Planning with Motion Primitives and Trajectory Optimization"). In the optimization step of iDb-RRT, we employ nonlinear trajectory optimization to repair the discontinuity between the motion primitives and to obtain a feasible and locally optimal trajectory.

<!-- chunk {"id": "body-0035", "role": "body", "section": "IV-E Trajectory Optimization", "weight": 1.0} -->

For gradient-based trajectory optimization, we require the gradients of the dynamics and the cost function with respect to the states and controls. These can be easily obtained for most robotics systems using finite differences, analytic expressions, or a differentiable simulator. Instead of the binary collision check in Db-RRT, we now use a signed distance function.

<!-- chunk {"id": "body-0036", "role": "body", "section": "IV-E Trajectory Optimization", "weight": 1.0} -->

In the trajectory optimization step, the number of time steps $K$ is fixed by the output of Db-RRT. If desired, we can also optimize the duration of the trajectory by including the length of the time interval in the optimization problem or using other techniques, as explored. Because our goal is to find a valid trajectory quickly, we choose not to include the time interval as an optimization variable. This choice is supported by the fact that trajectories from RRT-like algorithms tend to be suboptimal, where the time duration of the initial guess is often sufficient to reach the goal.

<!-- chunk {"id": "body-0037", "role": "body", "section": "IV-E Trajectory Optimization", "weight": 1.0} -->

To solve the trajectory optimization problem, we use the Differential Dynamic Programming (DDP) algorithm, which is a second-order method for solving optimal control problems of the form Eq. (IV-E). Collision and goal constraints, and state and control bounds of the original kinodynamic motion planning problem are added to the cost (4a) with a squared penalty method and a max activation function for inequalities. Further, we include small regularization terms on the control effort and the acceleration of the system to improve convergence.

<!-- chunk {"id": "body-0038", "role": "body", "section": "IV-E Trajectory Optimization", "weight": 1.0} -->

In particular, we use the optimization algorithm *Feasibility-driven DDP*, which can be warm-started with an infeasible sequence of states and controls, providing a good balance between local convergence and globalization.

<!-- chunk {"id": "body-0039", "role": "body", "section": "IV-F Analysis", "weight": 1.0} -->

The RRT algorithm is probabilistically complete, that is, the probability of eventually finding a solution, if one exists, converges to one. The proof assumes that the planning problem is $\delta_{1}$-robust (informally: the solution should not require traversing a "gap" smaller than $\delta_{1}$) and that the dynamics are Lipschitz continuous. Formally, it uses an inductive argument over overlapping balls that cover the solution trajectory, demonstrating that the probability of finding an edge between neighboring balls is non-zero.

<!-- chunk {"id": "body-0040", "role": "body", "section": "IV-F Analysis", "weight": 1.0} -->

We first consider Db-RRT (Algorithm 2) with the precondition that we have a sufficiently large set of motion primitives $\mathcal{M}_{L}$ and a discontinuity bound $\delta < \delta_{1}$. Then, the additional if-condition in Algorithm 2 does not prevent finding a solution. Algorithm 2 changes the distribution for the expansion operation but continues to assign a positive probability density to all successors for large sets of randomly generated $\mathcal{M}_{L}$. Next, we consider iDb-RRT (Algorithm 1). If Db-RRT fails to find a solution because at least one precondition is violated (a large $\mathcal{M}_{L}$ and $\delta < \delta_{1}$), we adjust both parameters and repeat, yielding a non-zero probability of executing Db-RRT with parameters that fulfill our assumptions.

<!-- chunk {"id": "body-0041", "role": "body", "section": "IV-F Analysis", "weight": 1.0} -->

Finally, we assume that there exists a $\delta$ such that if Db-RRT generates a $\delta$-discontinuity bounded solution, the trajectory optimization algorithm will converge with a non-zero probability, which makes our algorithm, iDb-RRT, probabilistically complete.

<!-- chunk {"id": "body-0042", "role": "body", "section": "IV-F Analysis", "weight": 1.0} -->

In practice, we demonstrate that we can use a large discontinuity $\delta$ and a small number of primitives to efficiently find solutions to a wide range of problems.

<!-- chunk {"id": "body-0043", "role": "body", "section": "Experiments", "weight": 1.0} -->

We evaluate iDb-RRT on 30 problems that include 8 different dynamical systems in various environments. The first 16 problems are inspired by previous work on kinodynamic motion planning. Furthermore, we include 14 additional problems with the same dynamical systems but in larger, more complex environments with more obstacles, which require longer trajectories (last $14$ rows in Table I).

<!-- chunk {"id": "body-0044", "role": "body", "section": "Experiments", "weight": 1.0} -->

All benchmark problems are available in Dynobench. It provides a C++ implementation of the dynamical systems (dynamics with analytical Jacobians, state, and bound constraints), collision and signed distance function (based on the Flexible Collision Library, FCL), the environments (in human-friendly YAML files), and visualization tools.

<!-- chunk {"id": "body-0045", "role": "body", "section": "Experiments", "weight": 1.0} -->

Implementations of iDb-RRT and the other planners are available in Dynoplan, including the motion primitives and instructions to replicate the benchmark results. Visualizations of the problems and examples of solution trajectories computed by our algorithm are available on our website.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-A Dynamical Systems", "weight": 1.0} -->

We include a diverse range of dynamical systems and environments, featuring varying state dimensionality (from 3 to 14), the number of underactuated degrees of freedom, and controllability. All systems use explicit Euler integration, with ${\Delta t} = {0.1\ s}$ for all car-like robots and ${\Delta t} = {0.01\ s}$ for the flying robots and the Acrobot.

<!-- chunk {"id": "body-0047", "role": "body", "section": "V-A Dynamical Systems", "weight": 1.0} -->

The 8 systems are: Unicycle 1 ($1^{\text{𝑠𝑡}}$ order): 3-dimensional state space and 2-dimensional control space. Unicycle 2 ($2^{\text{𝑛𝑑}}$ order): 5-dimensional state space and 2-dimensional acceleration control. Car with trailer: 4-dimensional state space and a 2-dimensional control space, Acrobot: 4-dimensional state space and 1-dimensional control space. Quadrotor v0: 13-dimensional state space and a 4-dimensional control space (force for each of the four motors)^11^1We use the parameters of the Crazyflie 2.1, where the low thrust-to-weight ratio of $1.3$ is very challenging for kinodynamic motion planning.. Quadrotor v1: The state space is the same as in Quadrotor v0, but controls are now the total thrust and torques in the body frame. Planar rotor: 6-dimensional state space and 2-dimensional control space, also with $1.3$ thrust-to-weight ratio. Rotor pole: 2-dimensional control space and 8-dimensional state space.

<!-- chunk {"id": "body-0048", "role": "body", "section": "V-B Metrics", "weight": 1.0} -->

Each experiment is run $20$ times with different random seeds on a desktop computer^22^2Intel(R) Xeon(R) W-2145 CPU @ 3.70GHz, single-core.

<!-- chunk {"id": "body-0049", "role": "body", "section": "V-B Metrics", "weight": 1.0} -->

$t{\lbrack s\rbrack}$: Compute time to get the first solution (median).

<!-- chunk {"id": "body-0050", "role": "body", "section": "V-B Metrics", "weight": 1.0} -->

$c{\lbrack s\rbrack}$: Cost of the first solution. As a cost, we use the duration of the found trajectory, in seconds (median).

<!-- chunk {"id": "body-0051", "role": "body", "section": "V-B Metrics", "weight": 1.0} -->

If all the runs of an algorithm fail to find a solution before the timeout of $60\ s$, we use a dash ('-') in the table. If less than $50$% of the runs find a solution, we report the best value but add an asterisk ('\*') to indicate a low success rate.

<!-- chunk {"id": "body-0052", "role": "body", "section": "V-C Algorithms", "weight": 1.0} -->

iDb-RRT-F: using a forward Db-RRT (Algorithm 2).

<!-- chunk {"id": "body-0053", "role": "body", "section": "V-C Algorithms", "weight": 1.0} -->

iDb-RRT-C: using a bidirectional Db-RRT inspired by RRT-Connect.

<!-- chunk {"id": "body-0054", "role": "body", "section": "V-C Algorithms", "weight": 1.0} -->

We compare our algorithms against state-of-the-art methods that use optimization, search, and sampling, and have available open-source implementations.

<!-- chunk {"id": "body-0055", "role": "body", "section": "V-C Algorithms", "weight": 1.0} -->

$\bullet$ For a sampling-based approach, we use the kinodynamic version of RRT implemented in OMPL (Open Motion Planning Library), which uses the propagation of random control inputs to grow the search tree. Since sampling-based kinodynamic approaches cannot reach a goal state exactly, we use a goal region using the same value of $\delta$ used in iDb-A\* and iDb-RRT. We denote this algorithm as Kino-RRT.

<!-- chunk {"id": "body-0056", "role": "body", "section": "V-C Algorithms", "weight": 1.0} -->

$\bullet$ For optimization-based planning, we choose a standard combination of a geometric motion planner and a trajectory optimizer, which we denote as Geo-RRT-TO. Specifically, we use a geometric RRT (using the implementation in OMPL) to plan using only the position and orientation of the system, without considering velocity and dynamics. The trajectory optimizer (also based on Feasibility-driven DDP, see for details) is warm-started with the geometric guess. If trajectory optimization fails, we run RRT again from scratch and repeat.

<!-- chunk {"id": "body-0057", "role": "body", "section": "V-C Algorithms", "weight": 1.0} -->

$\bullet$ iDb-A\* is a hybrid method that integrates search with motion primitives and trajectory optimization, but uses incremental A\*-searches instead of RRT. Notably, iDb-A\* has been designed to combine asymptotic optimality with good anytime behavior, as it starts with a small number of motion primitives and incrementally increases the number of available motion primitives during each A\*-search. We terminate the algorithm once the first solution is found.

<!-- chunk {"id": "body-0058", "role": "body", "section": "V-C Algorithms", "weight": 1.0} -->

In all algorithms, all hyperparameters are chosen per dynamical system.

<!-- chunk {"id": "body-0059", "role": "body", "section": "V-D Results -- Comparison with Baselines", "weight": 1.0} -->

Car with trailer/Double bugtrap

<!-- chunk {"id": "body-0060", "role": "body", "section": "V-D Results -- Comparison with Baselines", "weight": 1.0} -->

Car with trailer/Narrow passage

<!-- chunk {"id": "body-0061", "role": "body", "section": "V-D Results -- Comparison with Baselines", "weight": 1.0} -->

Results are summarized in Table I. Due to space constraints, we report only the median of each metric. A graphical representation of these results using boxplots is available on our website. In general, we observe that iDb-A\* has lower variance than iDb-RRT, Kino-RRT, and Geo-RRT-TO. iDb-RRT-F and iDb-RRT-C solve all problems with a success rate of $100$% (except two problems each, where they achieve $80$-$90$% success rate), outperforming all baseline algorithms in terms of compute time to generate a solution (e.g., iDb-RRT-C is the fastest in $19$ problems, and iDb-RRT-F is the fastest in $6$ problems).

<!-- chunk {"id": "body-0062", "role": "body", "section": "V-D Results -- Comparison with Baselines", "weight": 1.0} -->

Kino-RRT: it finds a first solution in low-dimensional car-like systems in a competitive timeframe (but slower than iDb-RRT-F in $13$ out of $19$ cases) with a higher average cost. However, in agile systems (e.g., flying robots), propagation of random control inputs is very inefficient, and Kino-RRT fails to find a solution in $11$ problems out of $30$.

<!-- chunk {"id": "body-0063", "role": "body", "section": "V-D Results -- Comparison with Baselines", "weight": 1.0} -->

Geo-RRT-TO often requires multiple runs of RRT to provide a suitable initial guess for trajectory optimization, and sometimes fails completely as the initial guesses never contain information about the dynamics of the system (solving only $18$ out of $30$ problems with a success rate above $50$%). If the initial guess works for the optimizer, it can be very fast (Geo-RRT-TO is faster than iDb-RRT-F in $7$ problems).

<!-- chunk {"id": "body-0064", "role": "body", "section": "V-D Results -- Comparison with Baselines", "weight": 1.0} -->

iDb-A\*: is the strongest baseline, with success rate of $100$% in all problems except Planar rotor/Double bugtrap. However, iDb-A\* is always outperformed in the time to find the first solution by iDb-RRT-C. The difference between iDb-A\* and iDb-RRT-C increases in the new benchmark (last 14 problems), which require longer plans, with improvements up to $10$-$20$x. On the other hand, the first solution found with iDb-A\* has a better cost than any other algorithm in $23$ cases.

<!-- chunk {"id": "body-0065", "role": "body", "section": "Forward vs Bidirectional Search", "weight": 1.0} -->

Comparing our two variants, we observe that iDb-RRT-C is better in $21$ out of $30$ problems in terms of compute time. These results agree with previous experiments in the RRT literature, where RRT-Connect is generally faster than a forward search (in robotics problems, starting a search from the start and the goal is often beneficial because these configurations are often close to obstacles and narrow passages).

<!-- chunk {"id": "body-0066", "role": "body", "section": "Number of primitives and discontinuity bound", "weight": 1.0} -->

Connecting primitives with discontinuities allows our algorithms to plan using a reduced number of primitives. As a reference, for the system Unicycle 1 v0, we use an initial set of 200 primitives and an initial discontinuity bound of $0.3$. The discontinuity is computed with a weighted Euclidean norm (e.g., weight $1$ for position and $0.5$ for orientation); thus a $\delta$ of $0.3$ could represent up to $30\ {cm}$ of discontinuity in position or $0.6\ {rad}$ in orientation. Such discontinuities are large enough that the trajectory is not directly applicable to the real robot, but it can be efficiently repaired in the nonlinear trajectory optimization step of iDb-RRT. For the Quadcopter v0, we use $5000$ primitives and a discontinuity bound of $0.35$, and for the Rotor pole, we use $8000$ motions and a discontinuity bound of $0.45$.

<!-- chunk {"id": "body-0067", "role": "body", "section": "Number of primitives and discontinuity bound", "weight": 1.0} -->

The time spent to generate one motion primitive (offline) ranges from $10$ms for car-like robots to up to $5$s for flying robots (most of the time is spent attempting to solve two-point boundary value problems that do not have a solution).

<!-- chunk {"id": "body-0068", "role": "body", "section": "Analysis of compute time in iDb-RRT", "weight": 1.0} -->

In iDb-RRT, the time spent in trajectory optimization dominates the total compute time. For instance, the compute time required to optimize one trajectory in the new benchmark problems with flying robots is between $1$s and $3$s, while in car-like robots is between $50$ms and $200$ms. In addition, in the systems Quadrotor v0 and Quadrotor v1, trajectory optimization may fail at the first attempt, and finding a feasible solution requires multiple iterations of iDb-RRT. For car-like systems, we can compute trajectories of duration up to $50$s in less than $1$s. For flying robots, we require between $0.5$s and $4$s to generate trajectories of duration up to $14$s. A straightforward way to speed up the trajectory optimization step is to reduce the time discretization from $0.01$s to $0.05$s (with an expected $5$x speedup).

<!-- chunk {"id": "body-0069", "role": "body", "section": "RRT is easier to tune than incremental A\\*", "weight": 1.0} -->

The running time of A\* with motion primitives in a continuous space is highly sensitive to the number of motion primitives, i.e., the discretization level. With too few primitives, the problem becomes unsolvable; with too many, the state space to be expanded becomes unmanageably large. Conversely, our iDb-RRT algorithms lack an explicit notion of a branching factor. As confirmed by our results, the RRT approach naturally adapts to efficiently solving both simple and complex problems alike, obviating the need for choosing a branching factor while also providing faster exploration.

<!-- chunk {"id": "body-0070", "role": "body", "section": "Limitations and future work", "weight": 1.5} -->

The main limitation of iDb-RRT, similar to iDb-A⁢, lies in its scalability to higher-dimensional systems. As the dimensionality increases, the number of motion primitives required to cover the state space with a small discontinuity grows exponentially. This issue can be partially mitigated by planning with larger discontinuities. In our benchmark, we successfully scaled to 13-DOF for the Quadrotor and 8-DOF for Rotor pole, thanks to leveraging translation invariance and the second-order linear velocity invariance of the dynamics. To effectively scale to higher dimensions, we see great potential in using function approximation to learn a more informative distance metric and to combine motion primitives with deep generative models or learned policies.

<!-- chunk {"id": "body-0071", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We present iDb-RRT, a novel algorithm for kinodynamic motion planning that combines search and optimization within the framework of Rapidly-Exploring Random Trees (RRT). Our algorithm connects motion primitives with a bounded discontinuity as the expansion step of an RRT, which is later repaired using trajectory optimization. iDb-RRT is probabilistically complete and finds solutions faster than state-of-the-art kinodynamic motion planning across a diverse set of problems.

<!-- chunk {"id": "body-0072", "role": "body", "section": "Conclusion", "weight": 1.5} -->

Comparatively, iDb-RRT and iDb-A\* possess complementary strengths: the former finds solutions significantly faster, while the latter converges to optimal solutions with more compute time. Together, they demonstrate that combining motion primitives, bounded discontinuity, and trajectory optimization, is a promising approach for both sampling-based and search-based motion planning.
