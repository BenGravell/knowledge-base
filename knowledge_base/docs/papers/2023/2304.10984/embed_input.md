<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

IBBT: Informed Batch Belief Trees for Motion Planning under Uncertainty

Topics include Motion planning under uncertainty, Belief-space planning, Batch planning, Sampling-based planning, POMDPs, State estimation, Risk-aware planning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces Informed Batch Belief Trees for planning in belief space, using batch expansion and informed sampling to search efficiently under state uncertainty. The contribution sits between sampling-based motion planning and POMDP-style planning, with emphasis on reducing wasted exploration in high-dimensional belief spaces.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

In this work, we propose the Informed Batch Belief Trees (IBBT) algorithm for motion planning under motion and sensing uncertainties. The original stochastic motion planning problem is divided into a deterministic motion planning problem and a graph search problem. We solve the deterministic planning problem using sampling-based methods such as PRM or RRG to construct a graph of nominal trajectories. Then, an informed cost-to-go heuristic for the original problem is computed based on the nominal trajectory graph. Finally, we grow a belief tree by searching over the graph using the proposed heuristic. IBBT interleaves between batch state sampling, nominal trajectory graph construction, heuristic computing, and search over the graph to find belief space motion plans. IBBT is an anytime, incremental algorithm. With an increasing number of batches of samples added to the graph, the algorithm finds motion plans that converge to the optimal one. IBBT is efficient by reusing results between sequential iterations. The belief tree searching is an ordered search guided by an informed heuristic. We test IBBT in different planning environments. Our numerical investigation confirms that IBBT finds non-trivial motion plans and is faster compared with previous similar methods.

<!-- chunk {"id": "body-0004", "role": "body", "section": "Introduction", "weight": 1.5} -->

For safe and reliable autonomous robot operation in a real-world environment, consideration of various uncertainties becomes necessary. These uncertainties may arise from an inaccurate motion model, actuation or sensor noise, partial sensing, and the presence of other agents moving in the same environment. In this paper, we study the safe motion planning problem for robot systems with nontrivial dynamics, motion uncertainty, and state-dependent measurement uncertainty in an environment with non-convex obstacles.

<!-- chunk {"id": "body-0005", "role": "body", "section": "Introduction", "weight": 1.5} -->

Planning under uncertainty is referred to as belief space planning (BSP), where the state of the robot is characterized by a probability distribution function (pdf) over all possible states. This pdf is commonly referred to as the belief or information state. A BSP problem can be formulated as a partially observable Markov decision process (POMDP) problem. Solving POMDPs for continuous state, control, and observation spaces, is, however, intractable. Existing methods based on discretization are resolution-limited. Optimization over the entire discretized belief space to find a path is computationally expensive and does not scale well to large-scale problems. Online POMDP algorithms are often limited to short-horizon planning, have challenges when dealing with local minima, and are not suitable for global planning in large environments

<!-- chunk {"id": "body-0006", "role": "body", "section": "Introduction", "weight": 1.5} -->

Planning in infinite-dimensional distributional (e.g., belief) spaces can become more tractable by using sampling-based methods. For example, belief roadmap methods build a belief roadmap to reduce estimation uncertainty; the rapidly-exploring random belief trees (RRBT) algorithm has been proposed to grow a tree in the belief space. Owing to their advantages in avoiding local minima, dealing with nonconvex obstacles and high-dimensional state spaces, along with their anytime property, sampling-based methods have gained increased attention in the robotics community.

<!-- chunk {"id": "body-0007", "role": "body", "section": "Introduction", "weight": 1.5} -->

Robot safety under uncertainty can be also formulated as a chance-constrained optimization problem. In addition to minimizing the cost function, one also wants the robot not to collide with obstacles, with high probability. By approximating the chance constraints as deterministic constraints, references solve the problem using an optimization-based framework. However, those approaches lack scalability with respect to problem complexity, and the explicit representation of the obstacles is usually required.

<!-- chunk {"id": "body-0008", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we focus on sampling-based approaches similar to. One challenge of sampling-based algorithms for planning under uncertainty is the lack of the optimal substructure property, which has been discussed. The lack of optimal substructure property is further explained by the lack of total ordering on paths based on cost. Specifically, it is not enough to only minimize the usual cost function -- explicitly finding paths that reduce the uncertainty of the robot is also important (see Figure 1(a)). The RRBT algorithm proposed in overcomes the lack of optimal substructure property by introducing a partial-ordering of belief nodes and by keeping all non-dominated nodes in the belief tree. Note that without this partial-ordering, the methods in may not be able to find a solution, even if one exists. Minimizing the cost and checking the chance constraints can only guarantee that the existing paths in the tree satisfy the chance constraints. Without searching for paths that explicitly reduce state uncertainty, it will be difficult for future paths to satisfy the chance constraints.

<!-- chunk {"id": "body-0009", "role": "body", "section": "Introduction", "weight": 1.5} -->

In this paper, we propose the Informed Batch Belief Tree (IBBT) algorithm, which improves over the RRBT algorithm with the introduction of batch sampling and ordered graph search guided by an informed heuristic. Firstly, IBBT uses the partial ordering of belief nodes as. Compared to, IBBT is able to find sophisticated plans that visit and revisit the information-rich region to gain information. Secondly, RRBT uses unordered search like RRT\* while IBBT uses batch sampling and ordered search. RRBT adds one sample each time to the graph randomly. As shown in and, ordered searches such as FMT\* and BIT\* perform better than RRT\*. Thirdly, RRBT only uses the cost-to-come cost to guide the belief tree search while IBBT introduces a cost-to-go heuristic and uses the total path cost heuristic for informed belief tree search. After adding a sample, RRBT performs an exhaustive graph search. Thus all non-dominated belief nodes are added to the belief tree. With batch sampling and informed graph search, IBBT avoids adding unnecessary belief nodes.

<!-- chunk {"id": "body-0010", "role": "body", "section": "Introduction", "weight": 1.5} -->

Thus, IBBT is able to find the initial solution in a shorter time and has better cost-time performance compared to RRBT.

<!-- chunk {"id": "body-0011", "role": "body", "section": "Related Works", "weight": 1.0} -->

In, the problem of finding the minimum estimation uncertainty path for a robot from a starting position to a goal is studied by building a roadmap. In, it was noted that the true a priori probability distribution of the state should be used for motion planning instead of assuming maximum likelihood observations. A linear-quadratic Gaussian (LQG) controller along with the RRT algorithm were used for motion planning. To achieve asymptotic optimality, the authors in incrementally construct a graph and search over the graph to find all non-dominated belief nodes. Given the current graph, the Pareto frontier of belief nodes at each vertex is saved, where the Pareto frontier is defined by considering both the path cost and the node uncertainty.

<!-- chunk {"id": "body-0012", "role": "body", "section": "Related Works", "weight": 1.0} -->

In high-frequency replanning is shown to be able to better react to uncertainty during plan execution. Monte Carlo simulation and importance sampling are used in to compute the collision probability. Moving obstacles are considered. In, state dependence of the collision probability is considered and incorporated with chance-constraint RRT\*. In, a roadmap search method is proposed to deal with localization uncertainty; however, solutions for which the robot needs to revisit a position to gain information are ruled out. Distributionally robust RRT is proposed, where moment-based ambiguity sets of distributions are used to enforce chance constraints instead of assuming Gaussian distributions. Similarly, a moment-based approach that considers non-Gaussian state distributions is studied. In, the Wasserstein distance is used as a metric for Gaussian belief space planning. The algorithm is compared with RRBT. However, from the simulation results, RRBT usually finds better (lower cost) plans and thus has a better convergence performance.

<!-- chunk {"id": "body-0013", "role": "body", "section": "Related Works", "weight": 1.0} -->

Other works that are not based on sampling-based methods formulate the chance-constrained motion planning problem as an optimization problem. In those methods, the explicit representation of the obstacles is usually required. The obstacles may be represented by convex constraints or polynomial constraints. The chance constraints are then approximated as deterministic constraints and the optimization problem is solved by convex or nonlinear programming. Differential dynamic programming has also been used to solve motion planning under uncertainty. These algorithms find a locally optimal trajectory in the neighborhood of a given reference trajectory. The algorithms iteratively linearize the system dynamics along the reference trajectory and solve an LQG problem to find the next reference trajectory.

<!-- chunk {"id": "body-0014", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

We consider the problem of planning for a robot with nontrivial dynamics, model uncertainty, measurement uncertainty from sensor noise, and obstacle constraints. The state-space $\mathcal{X}$ is decomposed into free space $\mathcal{X}_{free}$ and obstacle space $\mathcal{X}_{obs}$. The motion planning problem is given by

<!-- chunk {"id": "body-0015", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Expression is the boundary condition for the motion planning problem. The goal is to steer the system from some initial distribution to a goal state. Since the robot state is uncertain, the mean of the final state ${\overline{x}}_{N}$ is constrained to be equal to the goal state ${\overline{x}}_{g}$. Condition is a chance constraint that enforces safety of the robot.

<!-- chunk {"id": "body-0016", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

Similar to, the motion plan considered in this paper is formed by a nominal trajectory and a feedback controller that stabilizes the system around the nominal trajectory. Specifically, we will use a Connect function that returns a nominal trajectory and a stabilizing controller between two states ${\overline{x}}^{a}$ and ${\overline{x}}^{b}$,

<!-- chunk {"id": "body-0017", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

${\overline{X}}^{a,b}$ and ${\overline{U}}^{a,b}$ are the sequence of states and controls of the nominal trajectory, and $K^{a,b}$ is a sequence of the corresponding feedback control gains. The nominal trajectory can be obtained by solving a deterministic optimal control problem with boundary conditions ${\overline{x}}^{a}$ and ${\overline{x}}^{b}$, and system dynamics ${\overline{x}}_{k + 1} = {f{({\overline{x}}_{k},{\overline{u}}_{k},0)}}$. The stabilizing controller can be computed using, for example, finite-time LQR design.

<!-- chunk {"id": "body-0018", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

A Kalman filter is used for online state estimation, which gives the state estimate^11^1Note non-standard notation. ${\hat{x}}_{k}$ of $({x_{k} - {\overline{x}}_{k}})$. Thus, the control at time $k$ is given by

<!-- chunk {"id": "body-0019", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

With the introduction of the Connect function, the optimal motion planning problem - is reformulated as finding the sequence of intermediate states $({\overline{x}}^{0},{\overline{x}}^{1},\cdots,{\overline{x}}^{\ell})$. The final control is given by

<!-- chunk {"id": "body-0020", "role": "body", "section": "Problem formulation", "weight": 1.0} -->

The remaining problem is to find the optimal sequence of intermediate states and enforce the chance constraints.

<!-- chunk {"id": "body-0021", "role": "body", "section": "Covariance Propagation", "weight": 1.0} -->

We assume that the system given by and is locally well approximated by its linearization along the nominal trajectory. This is a common assumption as the system will stay close to the nominal trajectory using the feedback controller. Define

<!-- chunk {"id": "body-0022", "role": "body", "section": "Covariance Propagation", "weight": 1.0} -->

We will consider this linear time-varying system hereafter. A Kalman filter is used for estimating ${\check{x}}_{k}$ and is given by

<!-- chunk {"id": "body-0023", "role": "body", "section": "Covariance Propagation", "weight": 1.0} -->

Using the fact that ${{\mathbb{E}}{\lbrack{{\hat{x}}_{k}{\overset{\sim}{x}}_{k}^{\text{T}}}\rbrack}} = 0$, it can be verified that $P_{k} = {{\hat{P}}_{k} + {\overset{\sim}{P}}_{k}}$. Thus, given the feedback gains $K_{k}$ and the Kalman filter gain $L_{k}$, we can predict the covariances of the state estimation error and the state along the trajectory, which also provides the state distributions in the case of a Gaussian distribution.

<!-- chunk {"id": "body-0024", "role": "body", "section": "V-A Motivation", "weight": 1.0} -->

The motivation of IBBT is shown in Figure 1. Two paths reach point $B$ in Figure 1(a). The red path reaches $B$ with a large cost but with low uncertainty. The blue path reaches $B$ with a small cost but with high uncertainty. In this case, the blue path cannot dominate the red path, as it will incur a high probability of chance constraint violation for future segments of the path. Thus, in RRBT, both paths are preserved in the belief tree. More specifically, RRBT will find all non-dominated belief nodes by exhaustively searching the graph.

<!-- chunk {"id": "body-0025", "role": "body", "section": "V-A Motivation", "weight": 1.0} -->

However, IBBT avoids exhaustive graph search and hence avoids adding unnecessary belief nodes. In Figure 1(b), if the blue path $\overline{BG}$ (starting anywhere inside the blue ellipse) satisfies the chance constraint, the blue path $\overline{SBG}$ will be the solution of the problem since it satisfies the chance constraints and has a lower cost than $\overline{SABG}$. The operation of searching the current graph to find more paths reaching $B$ with less uncertainty (but a higher cost), including the red one, becomes redundant.

<!-- chunk {"id": "body-0026", "role": "body", "section": "V-A Motivation", "weight": 1.0} -->

Here, we assume that the cost of the nominal trajectory, $\sum_{k = 0}^{N - 1}{J{({\overline{x}}_{k},{\overline{u}}_{k})}}$, makes most of the cost. That is, for the path $\overline{BG}$, starting from the red ellipse and the blue ellipse will incur a similar cost. Reducing the uncertainty at node $B$ is mainly for satisfying the chance constraint of the future trajectory. Such an assumption can also be found, for example,.

<!-- chunk {"id": "body-0027", "role": "body", "section": "V-A Motivation", "weight": 1.0} -->

RRBT performs an exhaustive search to find all non-dominated nodes whenever a vertex is added to the graph. Specifically, RRBT will spend a lot of effort finding nodes with low uncertainty but a high cost-to-come. Such nodes are only necessary if they are indeed part of the optimal path. If the blue path in Figure 1(b) is the solution, we do not need to search for other non-dominated nodes (red ellipse). However, since we do not know if the future blue path $\overline{BG}$ will satisfy the chance constraint or not, the red node may still be needed. Thus, IBBT explores the graph and adds belief nodes to the belief tree only when is necessary. This is done by batch sampling and using an informed heuristic.

<!-- chunk {"id": "body-0028", "role": "body", "section": "V-B Nominal Trajectory Graph", "weight": 1.0} -->

The stochastic motion planning problem - is divided into a simpler deterministic planning problem and a belief tree search problem. The deterministic planning problem is given by

<!-- chunk {"id": "body-0029", "role": "body", "section": "V-B Nominal Trajectory Graph", "weight": 1.0} -->

The deterministic planning problem can be solved using sampling-based methods. The Rapidly-exploring Random Graph (RRG) algorithm is adopted to add a batch of samples and maintain a graph of nominal trajectories. Similarly, the PRM algorithm may be used in place of RRG.

<!-- chunk {"id": "body-0030", "role": "body", "section": "V-B Nominal Trajectory Graph", "weight": 1.0} -->

The RRG-D algorithm given by Algorithm 1 follows the RRG algorithm developed in with the additional consideration of system dynamics. RRG-D uses the Connect function introduced in Section III to build a graph of nominal trajectories. The edge is added to the graph only if the nominal trajectory is obstacle-free, which is indicated by the ObstacleFree checking in Algorithm 1. RRG-D draws $m$ samples whenever it is called by the IBBT algorithm. The $m$ samples constitute one batch. The sampled states $\overline{x}$ along with the edges $e$ connecting them generate a graph in the search space. For belief space planning, each vertex $v$ has both state information $v.\overline{x}$ and belief information $v.N$. We use $v{(\overline{x})}$ to refer to the vertex $v$ whose state is $v.\overline{x}$. RRG-D returns the updated new graph and the newly added vertex set $V_{new}$.

<!-- chunk {"id": "body-0031", "role": "body", "section": "V-C IBBT", "weight": 1.0} -->

The Informed Batch Belief Tree algorithm repeatedly performs two main operations: It first builds a graph of nominal trajectories to explore the state space of the robot, and then it searches over this graph to grow a belief tree in the belief space. The IBBT algorithm is given by Algorithm 2 and Algorithm 3.

<!-- chunk {"id": "body-0032", "role": "body", "section": "V-C IBBT", "weight": 1.0} -->

1 n.P ← P0; $n.{\overset{\sim}{P}\leftarrow{\overset{\sim}{P}}_{0}}$; n.c ← 0; n.h ← Inf; n.parent ← null;
3 $v_{s}.{\overline{x}\leftarrow{\overline{x}}_{s}}$; $v_{g}.{\overline{x}\leftarrow{\overline{x}}_{g}}$;
10 foreach vnew ∈ Vnew do
11 foreach vneighbor of vnew do
Algorithm 2 Informed Batch Belief Tree

<!-- chunk {"id": "body-0033", "role": "body", "section": "V-C IBBT", "weight": 1.0} -->

4 if ${v{(n)}}.{\overline{x} = {\overline{x}}_{g}}$ then
8 nnew ← Propagate (eneighbor,n);
9 succ, G ← AppendBelief (G,vneighbor,nnew);
Algorithm 3 Graph Search

<!-- chunk {"id": "body-0034", "role": "body", "section": "V-C IBBT", "weight": 1.0} -->

Additional variables are needed to define a belief tree. A belief node $n$ is defined by a state covariance $n.P$, an estimation error covariance $n.\overset{\sim}{P}$, a cost-to-come $n.c$, a heuristic cost-to-go $n.h$, and a parent node index $n.{parent}$. A vertex $v$ is defined by a state $v.\overline{x}$, a set of belief nodes $v.N$, and a vertex cost $v.h$.

<!-- chunk {"id": "body-0035", "role": "body", "section": "V-C IBBT", "weight": 1.0} -->

The graph search given by Algorithm 3 repeats two primitive procedures to grow a belief tree: Belief node selection which selects the best node in the belief queue for expansion; Belief propagation which propagates the selected belief node to its neighbor vertices to generate new belief nodes. The metric to rank the belief nodes in the belief queue is vital for efficient graph search.

<!-- chunk {"id": "body-0036", "role": "body", "section": "V-C IBBT", "weight": 1.0} -->

Based on the nominal trajectory graph, we can compute the cost-to-go for all vertices. A nominal trajectory graph is shown in Figure 2(a). Every edge in the graph is computed by solving a deterministic optimal control problem with edge cost given. We compute the cost-to-go $v_{i}.h$ using value iteration for every vertex in the graph. $v_{i}.h$ is the true cost-to-go for the nominal trajectory graph and is an informed, admissible cost-to-go heuristic for the belief tree search problem.

<!-- chunk {"id": "body-0037", "role": "body", "section": "V-C IBBT", "weight": 1.0} -->

For example, a quadratic cost is very common in robotics applications where we want to minimize control effort and state uncertainty (covariance). Moreover, additional chance constraint checking is performed in the belief tree search. Therefore, $\sum_{k = 0}^{N - 1}{J{({\overline{x}}_{k},{\overline{u}}_{k})}}$ is an underestimate of the actual cost.

<!-- chunk {"id": "body-0038", "role": "body", "section": "V-C IBBT", "weight": 1.0} -->

The nodes in the belief node queue are ranked based on the total heuristic cost $n.{f = n}.{c + n}.h$. All belief nodes at the same vertex have the same heuristic cost-to-go and $n.{h = v}.h$. In Figure 2(b), two belief nodes $n_{1}$, $n_{2}$ are shown at vertex $v_{i}$. Their total heuristic costs are $n_{1}.{f = n_{1}}.{c + v_{i}}.h$ and $n_{2}.{f = n_{2}}.{c + v_{i}}.h$, respectively.

<!-- chunk {"id": "body-0039", "role": "body", "section": "V-C IBBT", "weight": 1.0} -->

The partial ordering of belief nodes is defined as follows. Let $n_{a}$ and $n_{b}$ be two belief nodes of the same vertex $v$. We use $n_{a} < n_{b}$ to denote that belief node $n_{b}$ is dominated by $n_{a}$. $n_{a} < n_{b}$ is true if

<!-- chunk {"id": "body-0040", "role": "body", "section": "V-C IBBT", "weight": 1.0} -->

In this case, $n_{a}$ is better than $n_{b}$ since it traces back a path that reaches $v$ with less cost and less uncertainty compared with $n_{b}$. Next, we summarize some primitive procedures used in the IBBT algorithm.\
Pop: $\text{Pop}{(Q)}$ selects the best belief node in term of the lowest cost $n.f$ from belief queue $Q$ and removes it from $Q$.\
Propagate: The Propagate procedure implements three operations: covariance propagation, chance constraint evaluation, and cost calculation. $\text{Propagate}{(e,n)}$ performs the covariance propagation using (13a)-. It takes an edge $e$ and a belief node $n$ at the starting vertex of the edge as inputs. Chance constraints are evaluated using the state covariance $P_{k}$ along the edge. If there are no chance constraint violations, a new belief $n_{new}$ is returned, which is the final belief at the end vertex of the edge. Otherwise, the procedure returns no belief.

<!-- chunk {"id": "body-0041", "role": "body", "section": "V-C IBBT", "weight": 1.0} -->

The cost-to-come of $n_{new}$ is the sum of $n.c$ and the cost of edge $e$ by applying the controller associated with $e$.\
Append Belief: The function AppendBelief$(G,v,n_{new})$ decides if the new belief $n_{new}$ should be added to vertex $v$ or not. If $n_{new}$ is not dominated by any existing belief nodes in $v.N$, $n_{new}$ is added to $v.N$. Note that adding $n_{new}$ means extending the current belief tree such that $n_{new}$ becomes a leaf node of the current belief tree. Next, we also check if any existing belief node in $v.N$ is dominated by $n_{new}$. If an existing belief is dominated, its descendant and the node itself are pruned.\
Prune Node Queue: The function Prune$(Q,{Cost})$ removes nodes in $Q$ whose total heuristic cost is greater than $Cost$.

<!-- chunk {"id": "body-0042", "role": "body", "section": "V-C IBBT", "weight": 1.0} -->

$Cost$ is the cost of the current solution found.\
Value Iteration: The function ValueIteration$(G)$ computes the cost-to-go for all vertices in $G$ use value iteration. The value iteration is done using the nominal trajectory graph. For vertices whose cost-to-go values are computed in the last iteration (before calling this function), their values are reused for initialization for faster convergence.\

<!-- chunk {"id": "body-0043", "role": "body", "section": "V-C IBBT", "weight": 1.0} -->

In Algorithm 2, Line 1-5 initializes the graph and the belief tree. The initial condition of the motion planning problem is given by the starting state ${\overline{x}}_{s}$, state covariance $P_{0}$, and estimation error covariance ${\overset{\sim}{P}}_{0}$. The goal state is ${\overline{x}}_{g}$. In Line 6, the queue $Q$ is initialized with the initial node $n$ and the cost of the current solution is set as infinity. In Line 8, the RRG-D is called to add $m$ samples and maintain a graph of nominal trajectories, $V_{new}$ is the set of newly added vertices after calling RRG-D. Based the on the nominal trajectory graph, cost-to-go for all vertices in $G$ is computed using value iteration (Line 9). Line 10-12 update the belief node queue after batch sampling.

<!-- chunk {"id": "body-0044", "role": "body", "section": "V-C IBBT", "weight": 1.0} -->

For every vertex that has an outgoing edge towards $v_{new}$, all the belief nodes at that vertex are added to the queue.

<!-- chunk {"id": "body-0045", "role": "body", "section": "V-C IBBT", "weight": 1.0} -->

In Algorithm 3, the belief $n$ is propagated outwards to all the neighbor vertices of $v{(n)}$ to grow the belief tree in Line 7-11. $v{(n)}$ refers to the vertex associated with $n$. $v_{neighbor}$ is a neighbor of $v{(n)}$ when there is an edge $e_{neighbor}$ from $v{(n)}$ to $v_{neighbor}$ in the graph. The new belief $n_{new}$ is added to the $v_{neighbor}.N$ and $Q$ if the belief tree extension is successful. Then, $n$ is marked as the parent node of $n_{new}$. Note that each belief node traces back a unique path from the initial belief node. For every belief node in the belief tree, we already found a feasible path (satisfies chance constraint) to this node. Algorithm 3 terminates when the belief node at ${\overline{x}}_{g}$ is selected for expansion (Line 4-6, Algorithm 3) or $Q$ is empty.

<!-- chunk {"id": "body-0046", "role": "body", "section": "V-C IBBT", "weight": 1.0} -->

In the first case, the best solution is found. In the second case, no solution exists given the current graph.

<!-- chunk {"id": "body-0047", "role": "body", "section": "Experimental Results", "weight": 1.0} -->

In this section, we test the IBBT algorithm for different motion planning problems and compared the results with the RRBT algorithm.

<!-- chunk {"id": "body-0048", "role": "body", "section": "VI-A Double Integrator", "weight": 1.0} -->

The first planning environment is shown in Figure 3. The gray areas are obstacles and the blue region is the information-rich region, that is, the measurement noise is small when the robot is in this region. We use the 2D double integrator dynamics with motion and sensing uncertainties as an example. The system model is linear and is given by

<!-- chunk {"id": "body-0049", "role": "body", "section": "VI-A Double Integrator", "weight": 1.0} -->

where the system state includes position and velocity, the control input is the acceleration. The system matrices are given by

<!-- chunk {"id": "body-0050", "role": "body", "section": "VI-A Double Integrator", "weight": 1.0} -->

To compute the nominal trajectories, the analytical solution is available. An LQG controller is used to compute the feedback gain $K$ in the Connect function. The collision probability in the chance constraint is approximated using Monte Carlo simulations. We sample from the state distribution and count the number of samples that collide with the obstacles. The ratio of collided samples to the total samples is the approximate collision probability.

<!-- chunk {"id": "body-0051", "role": "body", "section": "VI-A Double Integrator", "weight": 1.0} -->

We compared the performance of RRBT and IBBT to find the first solution. The belief tree from RRBT is shown in Figure 3(a), and the belief tree from IBBT is shown in Figure 3(b). Both algorithms use the same set of states and find the same solution, which is given in Figure 4. The robot first goes down to the information-rich region to reduce its uncertainty, while directly moving toward to goal will violate the chance constraint.

<!-- chunk {"id": "body-0052", "role": "body", "section": "VI-A Double Integrator", "weight": 1.0} -->

Fewer belief nodes are searched and added to the tree using IBBT compared with RRBT, even though they return the same solution. IBBT uses batch sampling and computes the informed cost-to-go heuristic to guide the belief tree search, while RRBT only uses the cost-to-come. RRBT tries to find all non-dominated belief nodes whenever a vertex is added to the graph. Thus, it will find belief nodes that have low uncertainty but high cost-to-come (shown as small ellipses in Figure 3(a)). However, if such a node is not part of the solution path, this computation is not necessary. The comparison of the results is shown in Figure 5. The solving time for IBBT and RRBT is around 0.05 sec and 0.14 sec respectively.

<!-- chunk {"id": "body-0053", "role": "body", "section": "VI-A Double Integrator", "weight": 1.0} -->

The second planning environment is shown in Figure 6. The problem setting is similar to the first environment except that more obstacles and information-rich regions are added. The first solution and the improved solution are shown in Figure 6(a) and Figure 6(b), respectively. The green lines are the mean trajectories. The gray lines around the green lines are the Monte-Carlo simulation results. The comparison with the RRBT algorithm is given in Figure 7. After finding the initial solution, both algorithms are able to improve their solution when more samples are added to the graph but IBBT is able to find a better solution in a much shorter time.

<!-- chunk {"id": "body-0054", "role": "body", "section": "VI-B Dubins Vehicle", "weight": 1.0} -->

Finally, we tested our algorithm using the Dubins vehicle model. The deterministic discrete-time model is given by

<!-- chunk {"id": "body-0055", "role": "body", "section": "VI-B Dubins Vehicle", "weight": 1.0} -->

The nominal trajectory for the Dubins vehicle is chosen as the minimum length path connecting two configurations of the vehicle. The analytical solution for the nominal trajectory is available.

<!-- chunk {"id": "body-0056", "role": "body", "section": "VI-B Dubins Vehicle", "weight": 1.0} -->

After linearization, the error dynamics around the nominal path is given, where the system matrices are

<!-- chunk {"id": "body-0057", "role": "body", "section": "VI-B Dubins Vehicle", "weight": 1.0} -->

$G_{k} = {\sqrt{\Deltat}{diag}{(0.02,0.02,0.02)}}$, $D_{k} = {0.1I_{3}}$ when the robot is in a information-rich region, otherwise $D_{k} = {2I_{3}}$. An LQG controller is used to compute the feedback gain $K$, the weighting matrices of the LQG cost are $Q = {2I_{3}}$ and $R = 1$.

<!-- chunk {"id": "body-0058", "role": "body", "section": "VI-B Dubins Vehicle", "weight": 1.0} -->

The first solution and the improved solution are shown in Figure 8(a) and Figure 8(b), respectively. The green line is the mean trajectory. The gray lines around the green lines are the Monte-Carlo simulations. The comparison with the RRBT algorithm is given in Figure 9. After finding the initial solution, both algorithms are able to improve their current solution when more samples are added to the graph. Again, IBBT has better cost vs. time performance.

<!-- chunk {"id": "body-0059", "role": "body", "section": "Conclusion", "weight": 1.5} -->

We developed an online, anytime, incremental algorithm, IBBT, for motion planning under uncertainties. The algorithm considers a robot that is partially observable, has motion uncertainty, and operates in a continuous domain. The algorithm interleaves between batch sampling, building a graph of nominal trajectories in the state space, and searches over the graph to grow a belief tree. The heuristic cost-to-go is computed using the nominal trajectory graph along with value iteration. This cost-to-go along with the cost-to-come provides an informed heuristic to guide the belief tree search. The algorithm finds motion plans that converge to the optimal one as more batches of samples are added to the graph. We have tested the IBBT algorithm in different planning environments. The proposed algorithm finds non-trivial motion plans and provides better solutions using a smaller amount of time compared with previous methods.
