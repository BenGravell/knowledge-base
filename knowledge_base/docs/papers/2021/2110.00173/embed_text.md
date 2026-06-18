## Introduction

For safe and reliable autonomous robot operation in a real-world environment, consideration of various uncertainties becomes necessary. These uncertainties may arise from an inaccurate motion model, actuation or sensor noise, partial sensing, and the presence of other agents moving in the same environment. In this paper, we study the safe motion planning problem of robot systems with nontrivial dynamics, motion uncertainty, and state-dependent measurement uncertainty, in an environment with non-convex obstacles.

Planning under uncertainties is referred to as belief space planning (BSP), where the state of the robot is characterized by a probability distribution function (pdf) over all possible states. This pdf is commonly referred to as the belief or information state. A BSP problem can be formulated as a partially observable Markov decision process (POMDP) problem. Solving POMDPs for continuous state, control, and observation spaces, is, however, intractable. Existing methods based on discretization are resolution-limited. Optimization over the entire discretized belief space to find a path is computationally expensive and does not scale well to large-scale problems. Online POMDP algorithms are often limited to short-horizon planning, have challenges in dealing with local minimums, and are not suitable for global planning in large environments.

Planning in infinite-dimensional distributional (e.g., belief) spaces can become more tractable by using sampling-based methods. For example, belief roadmap methods build a belief roadmap to reduce estimation uncertainty; the rapidly-exploring random belief trees (RRBT) algorithm has been proposed to grow a tree in the belief space. Owing to their advantages in avoiding local minima, dealing with nonconvex obstacles and high-dimensional state spaces, along with their anytime property, sampling-based methods have gained increased attention in the robotics community recently.

Robot safety under uncertainty can be also formulated as a chance-constrained optimization problem. In addition to minimizing the cost function, one also wants the robot not to collide with obstacles, with high probability. By approximating the chance constraints as deterministic constraints, references solve the problem using an optimization-based framework. However, those approaches lack scalability with respect to problem complexity, and the explicit representation of the obstacles is usually required.

In this paper, we focus on sampling-based approaches similar to. One challenge of sampling-based algorithms for planning under uncertainty is the lack of the optimal substructure property, which has been discussed in. The lack of optimal substructure property is further explained by the lack of total ordering on paths based on cost. Specifically, it is not enough to only minimize the usual cost function -- explicitly finding paths that reduce the uncertainty of the robot is also important (see Figure 1(a)).

The RRBT algorithm proposed in overcomes the lack of optimal substructure property by introducing a partial-ordering of belief nodes and by keeping all non-dominated nodes in the belief tree. Note that without this partial-ordering, the methods in may not be able to find a solution, even if one exists. Minimizing the cost and checking the chance constraints can only guarantee that the existing paths in the tree satisfy the chance constraints. Without searching for paths that explicitly reduce the state uncertainty, it will be difficult for future paths to satisfy the chance constraints.

In this paper, we propose the Batch Belief Tree (BBT) algorithm, which improves over the RRBT algorithm with the introduction of a batch sampling extension and by introducing a modified exploration and exploitation interplay. BBT uses the partial ordering of belief nodes as in and searches over the graph of nominal trajectories to find non-dominated belief nodes. Compared to, BBT is able to find sophisticated plans that visit and revisit the information-rich region to gain information. Compared to RRBT, instead of an exhaustive graph search (exploitation) after every exploration (adding a sample), BBT uses batch sampling for faster state-space exploration, and does not require an exhaustive graph search before adding another batch of samples. Thus, BBT is able to find the initial solution in a shorter time and has better cost-time performance compared to RRBT, as will be shown in Section VI.

## Related Works

In, the problem of finding the minimum estimation uncertainty path for a robot from a starting position to a goal is studied by building a roadmap. In, it was noted that the true a priori probability distribution of the state should be used for motion planning instead of assuming maximum likelihood observations. A linear-quadratic Gaussian (LQG) controller along with the RRT algorithm were used for motion planning in. To achieve asymptotic optimality, the authors in incrementally construct a graph and search over the graph to find all non-dominated belief nodes. Given the current graph, the Pareto frontier of belief nodes at each vertex is saved, where the Pareto frontier is defined by considering both the path cost and the node uncertainty.

In high-frequency replanning is shown to be able to better react to uncertainty during plan execution. Monte Carlo simulation and importance sampling are used in to compute the collision probability. Moving obstacles are considered in. In, state dependence of the collision probability is considered and incorporated with chance-constraint RRT\*. In, a roadmap search method is proposed to deal with localization uncertainty; however, solutions for which the robot need to revisit a position to gain information are ruled out. Distributionally robust RRT is proposed in, where moment-based ambiguity sets of distributions are used to enforce chance constraints instead of assuming Gaussian distributions. Similarly, a moment-based approach considering non-Gaussian state distributions is studied in.

Other works that are not based on sampling-based methods formulate the chance-constrained motion planning problem as an optimization problem. In those methods, the explicit representation of the obstacles is usually required. The obstacles may be represented by convex constraints or polynomial constraints. The chance constraints are then approximated as deterministic constraints and the optimization problem is solved by convex or nonlinear programming. Differential dynamic programming has also been used to solve motion planning under uncertainty. These algorithms find a locally optimal trajectory in the neighborhood of a given reference trajectory. The algorithms iteratively linearize the system dynamics along the reference trajectory and solve an LQG problem to find the next reference trajectory.

## Problem formulation

We consider the problem of planning for a robot with nontrivial dynamics, model uncertainty, measurement uncertainty from sensor noise, and obstacle constraints. The motion model and sensing model are given by the following discrete-time equations,

where $k = {0,1,\ldots,{N - 1}}$ are the discrete time-steps, $x_{k} \in {\mathbb{R}}^{n_{x}}$ is the state, $u_{k} \in {\mathbb{R}}^{n_{u}}$ is the control input, and $y_{k} \in {\mathbb{R}}^{n_{y}}$ is the measurement at time step $k$. The steps of the noise processes $w_{k} \in {\mathbb{R}}^{n_{w}}$ and $v_{k} \in {\mathbb{R}}^{n_{y}}$ are i.i.d standard Gaussian random vectors, respectively. We assume that ${(w_{k})}_{k = 0}^{N - 1}$ and ${(v_{k})}_{k = 0}^{N - 1}$ are independent.

The state-space $\mathcal{X}$ is decomposed into free space $\mathcal{X}_{free}$ and obstacle space $\mathcal{X}_{obs}$. The motion planning problem is given by

where is the boundary condition for the motion planning problem. The goal is to steer the system from some initial distribution to a goal state. Since the robot state is uncertain, the mean of the final state ${\overline{x}}_{N}$ is constrained to be equal to the goal state ${\overline{x}}_{g}$. Condition is a chance constraint that enforces safety of the robot.

Similar to, the motion plan considered in this paper is formed by a nominal trajectory and a feedback controller that stabilizes the system around the nominal trajectory. Specifically, we will use a Connect function that returns a nominal trajectory and a stabilizing controller between two states ${\overline{x}}^{a}$ and ${\overline{x}}^{b}$,

${\overline{X}}^{a,b}$ and ${\overline{U}}^{a,b}$ are the sequence of states and controls from the nominal trajectory, and $K^{a,b}$ is a sequence of feedback control gains. The nominal trajectory can be obtained by solving a deterministic optimal control problem with boundary conditions ${\overline{x}}^{a}$ and ${\overline{x}}^{b}$, and system dynamics ${\overline{x}}_{k + 1} = {f{({\overline{x}}_{k},{\overline{u}}_{k},0)}}$. The stabilizing controller can be computed using, for example, finite-time LQR design.

A Kalman filter is used for online state estimation, which gives the state estimate^11^1Note non-standard notation. ${\hat{x}}_{k}$ of $({x_{k} - {\overline{x}}_{k}})$. Thus, the control at time $k$ is given by

With the introduction of the Connect function, the optimal motion planning problem - is reformulated as finding the sequence of intermediate states $({\overline{x}}^{0},{\overline{x}}^{1},\cdots,{\overline{x}}^{\ell})$. The final control is given by

The remaining problem is to find the optimal sequence of intermediate states and enforce the chance constraints.

## Covariance Propagation

We assume that the system given by and is locally well approximated by its linearization along the nominal trajectory. This is a common assumption as the system will stay close to the nominal trajectory using the feedback controller. Define

By linearizing along $({\overline{x}}_{k},{\overline{u}}_{k})$, the error dynamics is

We will consider this linear time-varying system hereafter. A Kalman filter is used for estimating ${\check{x}}_{k}$ and is given by

and $L_{k}$ is the Kalman gain.

The covariances of ${\check{x}}_{k}$, ${\hat{x}}_{k}$ and ${\overset{\sim}{x}}_{k} \triangleq {{\check{x}}_{k} - {\hat{x}}_{k}}$ are denoted as $P_{k} = {{\mathbb{E}}{\lbrack{{\check{x}}_{k}{\check{x}}_{k}^{\text{T}}}\rbrack}}$, ${\hat{P}}_{k} = {{\mathbb{E}}{\lbrack{{\hat{x}}_{k}{\hat{x}}_{k}^{\text{T}}}\rbrack}}$ and ${\overset{\sim}{P}}_{k} = {{\mathbb{E}}{\lbrack{{\overset{\sim}{x}}_{k}{\overset{\sim}{x}}_{k}^{\text{T}}}\rbrack}}$, respectively. Note that the covariance of $x_{k}$ is also given by $P_{k}$ and the estimation error covariance ${\overset{\sim}{P}}_{k}$ is computed from. From -, it can be verified that ${{\mathbb{E}}{\lbrack{\check{x}}_{k}\rbrack}} = {{\mathbb{E}}{\lbrack{\hat{x}}_{k}\rbrack}} = {{\mathbb{E}}{\lbrack{\hat{x}}_{k^{\text{-}}}\rbrack}}$. Since ${{\mathbb{E}}{\lbrack{\check{x}}_{0}\rbrack}} = 0$, by choosing ${{\mathbb{E}}{\lbrack{\hat{x}}_{0}\rbrack}} = 0$, we have ${{\mathbb{E}}{\lbrack{\hat{x}}_{k}\rbrack}} = 0$ for $k = {0,\cdots,N}$. Using and we also have that

Using the fact that ${{\mathbb{E}}{\lbrack{{\hat{x}}_{k}{\overset{\sim}{x}}_{k}^{\text{T}}}\rbrack}} = 0$, it can be verified that $P_{k} = {{\hat{P}}_{k} + {\overset{\sim}{P}}_{k}}$. Thus, given the feedback gains $K_{k}$ and the Kalman filter gain $L_{k}$, we can predict the covariances of the state estimation error and the state along the trajectory, which also provides the state distributions in the case of a Gaussian distribution.

## Batch Belief Tree Algorithm

The Batch Belief Tree algorithm performs two main operations: It first builds a graph of nominal trajectories to explore the state space of the robot, and then it searches over this graph to grow a belief tree in the belief space. For graph construction, batches of samples are added to the graph intermittently. The Rapidly-exploring Random Graph (RRG) algorithm is adopted to add a batch of samples and maintain a graph of nominal trajectories.

The operation of graph construction is referred to as exploration, as it will incrementally build a graph to cover the state space. Analogously, the operation of searching over the current graph is referred to as exploitation, as it exploits the current graph to search a tree in belief space. Previous work performed an exhaustive search whenever one sample is added to the graph, which results in poor performance in terms of exploration. Note that the operation of an exhaustive search is more complicated than adding a single sample to the RRG graph. The proposed Batch Belief Tree (BBT) algorithm adds a batch of samples at a time and it does not require a complete graph search before adding another batch of samples. As it will be shown in Section VI, the resulting advantage of BBT is that it finds a better path given the same amount of time compared to.

Figure 1: (a) Two paths reach the same point B. Red path detours to an information-rich region to reduce uncertainty. Both paths are preserved in the belief tree in RRBT. (b) If the blue path $\overline{BG}$ satisfies the chance constraint, the whole blue path $\overline{SBG}$ satisfies the chance constraint and has a lower cost than the red path $\overline{SABG}$. The operation of finding more paths reaching B with less uncertainty (but larger cost), such as the red one, becomes redundant.

The motivation of BBT is shown in Figure 1. Two paths reach point $B$ in Figure 1(a). The red path reaches $B$ with a large cost but with low uncertainty. The blue path reaches $B$ with a small cost but with high uncertainty. In this case, the blue path cannot dominate the red path, as it will incur a high probability of chance constraint violation for future segments of the path. Thus, both paths are preserved in the belief tree as discussed in. However, in Figure 1(b), if the blue path $\overline{BG}$ (starting from the blue ellipse) satisfies the chance constraint, the blue path $\overline{SBG}$ will be the solution of the problem since it satisfies the chance constraints and has a lower cost than $\overline{SABG}$. The operation of searching the current graph to find more paths reaching $B$ with less uncertainty (but a higher cost), such as the red path, becomes redundant. Here, we assume that the cost in is mainly the cost from the mean trajectory. That is, for path $\overline{BG}$, starting from the red ellipse and blue ellipse will incur a similar cost. Reducing the uncertainty at node $B$ is mainly for satisfying the chance constraint of the future trajectory. Such assumption can also be found, for example, in.

RRBT performs an exhaustive search to find all non-dominated nodes whenever a vertex is added to the graph. Specifically, it will spend a lot of effort finding nodes with low uncertainty but a high cost-to-come. Such nodes are only necessary if they are indeed part of the optimal path. If the blue path in Figure 1(b) is the solution, we do not need to search for other non-dominated nodes (red node). However, since we do not know if the future blue path $\overline{BG}$ will satisfy the chance constraint or not, the red node may still be needed. Thus, we propose to delay the search procedure and only search (exploitation) when is necessary and when prioritizing exploration becomes beneficial. The refined exploration versus exploitation in BBT can be interpreted as delayed graph exploitation (which will promote exploration) and will allow us to find the solution faster.

2n.P ← P0; $n.{\overset{\sim}{P}\leftarrow{\overset{\sim}{P}}_{0}}$; n.c ← 0; n.parent ← Null;
3 vinit.x ← xinit; vinit.N ← {n};
5 (G,Qnext) ← RRG-D (G, m, Qnext←⌀);
6 Qcurrent ← Qnext; Qnext ← ⌀;
11 nnew ← Propagate (eneighbor,n);
12 if (vneighbor,nnew) then
13 Qnext ← Qnext ∪ {nnew};
20 (G,Qnext) ← RRG-D (G,m,Qnext);
22 Qcurrent ← Qnext; Qnext ← ⌀;
Algorithm 1 Batch Belief Tree

5 vnearest ← Nearest (V,xrand);
6 enearest ← Connect(vnearest.x,xrand);
8 Qnext ← Qnext ∪ vnearest.N;
9 Vnear ← Near (V,xrand);
12 e ← Connect(xrand,vnearest.x);
16 foreach vnear ∈ Vnear do
17 e ← Connect(vnear.x,xrand);
20 Qnext ← Qnext ∪ vnear.N;
22 e ← Connect(xrand,vnear.x);

The complete BBT algorithm is given by Algorithm 1 and Algorithm 2. The RRG-D algorithm given by Algorithm 2 follows the RRG algorithm developed in with the additional consideration of system dynamics. RRG-D uses the Connect function introduced in Section III to build a graph of nominal trajectories. The edge is added to the graph only if the nominal trajectory is obstacle-free, which is indicated by the ObstacleFree checking in Algorithm 2. RRG-D adds $m$ samples to the current graph whenever it is called by the BBT algorithm. The $m$ samples constitute one batch. One batch of samples is added to the graph without any graph exploitation in between, which is different from RRBT, which performs a search whenever a single sample is added. RRG-D also updates the belief queue $Q_{next}$, which is defined later.

The sampled states $x$ along with the edges $e$ connecting them generate a graph in the search space. Additional variables are needed to define a belief tree. A belief node $n$ is defined by a state covariance $n.P$, an estimation error covariance $n.\overset{\sim}{P}$, a cost $n.c$, and a parent node index $n.{parent}$. A vertex $v$ is defined by a state $v.x$, and a set of belief nodes $v.N$. Each belief node traces back a unique path from the initial belief node. Two queues $Q_{current}$ and $Q_{next}$ are defined to store two sets of belief nodes.

We use the partial ordering of belief nodes as in. Let $n_{a}$ and $n_{b}$ be two belief nodes of the same vertex $v$. We use $n_{a} < n_{b}$ to denote that belief node $n_{b}$ is dominated by $n_{a}$. $n_{a} < n_{b}$ is true if

In this case, $n_{a}$ is better than $n_{b}$ since it traces back a path that reaches $v$ with less cost and less uncertainty compared with $n_{b}$. Next, we summarize some primitive procedures used in the BBT algorithm.\
Pop: $\text{Pop}{(Q_{current})}$ selects a belief node from $Q_{current}$ and removes it from $Q_{current}$. Here we select the belief node with the minimum cost $n.c$.\
Propagate: The Propagate procedure implements three operations: covariance propagation, chance constraint evaluation, and cost calculation. $\text{Propagate}{(e,n)}$ performs the covariance propagation using and. It takes an edge $e$ and an initial belief node $n$ at the starting vertex of the edge as inputs. Chance constraints are evaluated using the state covariance $P_{k}$ along the edge. If there are no chance constraint violations, a new belief $n_{new}$ is returned, which is the final belief at the end vertex of the edge. Otherwise, the procedure returns no belief. The cost of $n_{new}$ is the sum of $n.c$ and the cost of edge $e$ by applying the controller associated with $e$.\
Append Belief: The function AppendBelief$(v,n_{new})$ decides if the new belief $n_{new}$ should be added to vertex $v$ or not. If $n_{new}$ is not dominated by any existing belief nodes in $v.N$, $n_{new}$ is added to $v.N$. Note that adding $n_{new}$ means extending the current belief tree such that $n_{new}$ becomes a leaf node of the current belief tree. Next, we also check if any existing belief node is dominated by $n_{new}$. If an existing belief is dominated, its descendant and the node itself are pruned.\
New Batch: The NewBatch condition calls the RRG-D algorithm to add a new batch of samples. The NewBatch condition is satisfied, for example, if the inner while loop Line 7-17 is executed with a maximum number of times or the queue $Q_{next}$ is empty (or close to empty).\
Terminate: The Terminate condition allows the algorithm to terminate without conducting an exhaustive graph search. This condition may be satisfied when the current solution is close to the optimal one or the maximum planning time is reached.\

The initial condition of the motion planning problem is given by the initial state $x_{0}$, state covariance $P_{0}$, and estimation error covariance ${\overset{\sim}{P}}_{0}$. Lines 1-3 of Algorithm 1 initialize the belief tree. In Line 4, the RRG-D is called to add $m$ samples and maintain a graph of nominal trajectories. After Line 4, $Q_{next}$ only contains one belief node which is the initial belief node.

The BBT algorithm explicitly uses two lists, $Q_{current}$ and $Q_{next}$, to store belief nodes that will be propagated later. In Lines 7-12, all belief nodes in $Q_{current}$ are propagated once, and $Q_{current}$ will be empty. All the newly added belief nodes are added to $Q_{next}$, which will be propagated in the next iteration. $v{(n)}$ refers to the vertex associated with $n$. In Lines 9-12, the belief $n$ is propagated outwards to all the neighbor vertices of $v{(n)}$ to grow the belief tree. The new belief $n_{new}$ is added to the $v_{neighbor}.N$ if the connection is successful. The batch sampling in Lines 15-16, along with $Q_{current}$ and $Q_{next}$ allow adding another batch of samples without an exhaustive graph search, which results in delayed graph exploitation and promoting exploration.

### V-A Convergence Analysis

In this section, we briefly discuss the asymptotic optimality of the BBT algorithm, which states that the solution returned by BBT converges to the optimal solution as the number of the samples goes to infinite.

Note that the RRBT algorithm is shown to be asymptotically optimal. Here, we argue the asymptotic optimality of the BBT by drawing to its connection with the RRBT algorithm.

### Proposition 1

Given the same sequence of samples of the RRBT algorithm with any fixed length, the RRG graphs constructed by BBT and RRBT are the same. Provided that the terminate condition in Line 13 of Algorithm 1 is not satisfied, the BBT algorithm finds all the non-dominated belief nodes over the RRG graph and the belief trees built by BBT and RRBT are the same.

### Proof

The proof of Proposition 1 is straightforward. After running the BBT algorithm, both $Q_{current}$ and $Q_{next}$ will be empty. The AppendBelief function ensures that every non-dominated belief is added to the belief tree, and only the dominated beliefs are pruned. Thus, the RRG graph is exhaustively searched and all the non-dominated belief nodes are in the belief tree. Therefore, the asymptotic optimality of the RRBT algorithm implies the asymptotic optimality of the BBT algorithm. ∎

## Experimental Results

In this section, we test the BBT algorithm for different motion planning problems and compared the results with the RRBT algorithm.

Figure 2: (a) Belief tree from the RRBT algorithm. (b) Belief tree from the BBT algorithm. Both algorithms stop when they find the first solution. The extra ellipses in the right figure indicate that RRBT adds more nodes to the belief tree by exhaustive search. BBT delays such exploitation and thus is able to find the solution faster.

Figure 3: First solution found by both algorithms.

Figure 4: Comparison between the BBT and the RRBT algorithms. BBT is faster to find the first solution.

### VI-A Double Integrator

The first planning environment is shown in Figure 2. The gray areas are obstacle and the blue region is the information-rich region, that is, the measurement noise is small when the robot is in this region. We use the 2D double integrator dynamics with motion and sensing uncertainties as an example. The system model is linear and is given by

where the system state includes position and velocity, the control input is the acceleration. The system matrices are given by

$G_{k} = {\sqrt{\Deltat}{diag}{(0.03,0.03,0.02,0.02)}}$, and $D_{k} = {0.01I_{4}}$ when the robot is in a information-rich region, otherwise $D_{k} = I_{4}$.

To compute the nominal trajectory, we consider a quadratic cost of the control input where the cost matrix is $R = I_{2}$. We use the analytical solution for this mean steering problem. An LQG controller is used to compute the feedback gain $K$ in the Connect function. The collision probability in the chance constraint is approximated using Monte-Carlo simulations. We sample from the state distribution and count the number of samples that collide with the obstacles. The ratio of collided samples to the total samples is the approximate collision probability. All simulations were done on a laptop computer with a 1.6 GHz Intel i5-8255u processor and 8 GB RAM using MATLAB.

We compared the performance of RRBT and BBT to find the first solution. The belief tree from RRBT is shown in Figure 2(a), and the belief tree from BBT is shown in Figure 2(b). Both algorithms find the same solution, which is given in Figure 3. The robot first goes down to the information-rich region to reduce its uncertainty, then revisits the starting position and go up towards the goal. Directly moving toward to goal will violate the chance constraint. Other methods that do not utilize partial-ordering of the belief nodes cannot find this solution.

Fewer belief nodes are searched and added to the tree in Figure 2(b) compared with Figure 2(a), even though they return the same solution. This is due to the refined exploration and exploitation interplay of the BBT algorithm. RRBT tries to find all non-dominated belief nodes whenever a vertex is added to the graph. Thus, it will find belief nodes that have low uncertainty but high cost-to-come (shown as small ellipses in Figure 2(a)). However, if such a node is not part of the solution path, this computation is not necessary. BBT delays such exploitation and prioritizes exploration. Note that BBT will eventually find all the non-dominated belief nodes and return the same belief tree as RRBT when the belief queues are empty. The comparison of the results is shown in Figure 4. BBT is faster than RRBT to find the solution. Note that belief nodes being pruned are not shown in Figure 2.

Figure 5: (a) Belief tree built by the BBT algorithm when finding the first solution; (b) The first solution returned by BBT; (c) An improved solution as more vertices are added to the graph.

Figure 6: Comparison between the BBT algorithm and the RRBT algorithm. BBT has better cost-time performance and finds the first solution with less time.

The second planning environment is shown in Figure 5. The problem setting is similar to the first environment except that more obstacles and information-rich regions are added. The belief tree built by the BBT algorithm, when the first solution is found, is shown in Figure 5(a). The first solution and the improved solution are shown in Figure 5(b) and (c), respectively. The green lines are the mean trajectories. The gray lines around the green lines are the Monte-Carlo simulation results. The comparison with the RRBT algorithm is given in Figure 6. The same sequence of samples is used in both algorithms. After finding the initial solution, both algorithms are able to improve their current solution when more samples are added to the graph but BBT is able to find the same paths as the RRBT algorithm at a much shorter time.

### VI-B Dubins Vehicle

Finally, we tested our algorithm using the Dubins vehicle model. The deterministic discrete-time model is given by

The nominal trajectory for the Dubins vehicle is chosen as the minimum length path connecting two configurations of the vehicle. The analytical solution for the nominal trajectory is available in.

After linearization, the error dynamics around the nominal path is given by, where the system matrices are

$G_{k} = {\sqrt{\Deltat}{diag}{(0.02,0.02,0.02)}}$, $D_{k} = {0.1I_{3}}$ when the robot is in a information-rich region, otherwise $D_{k} = {2I_{3}}$. An LQG controller is used to compute the feedback gain $K$, the weighting matrices of the LQG cost are $Q = {2I_{3}}$ and $R = 1$.

The belief tree built by the BBT algorithm is shown in Figure 7(a). The planned trajectory is shown in Figure 7(b). The green line is the mean trajectory. The gray lines around the green lines are the Monte-Carlo simulation results. The comparison with the RRBT algorithm is given in Figure 8. After finding the initial solution, both algorithms are able to improve their current solution when more samples are added to the graph. BBT is able to find the same paths as the RRBT algorithm at a much shorter time.

Figure 7: Planning results of the Dubins vehicle. (a) Belief tree built by the BBT algorithm. (b) Planned trajectory.

Figure 8: Comparison between the BBT algorithm and the RRBT algorithm. BBT has better cost-time performance and finds the first solution with less time.

## Conclusion

In this paper, we propose the Batch Belief Tree (BBT) algorithm for motion planning under uncertainties. The algorithm considers a robot that is partially observable, has motion uncertainty, and operates in a continuous domain. By searching over the graph, the algorithm finds sophisticated plans that will visit (and revisit) information-rich regions to reduce uncertainty. With intermittent batch sampling and delayed graph exploitation, BBT has good performance in terms of exploring the state space. BBT finds all non-dominated belief nodes within the graph and is asymptotic optimal. We have tested the BBT algorithm in different planning environments. Compare to with previous methods, BBT finds non-trivial solutions that have lower costs at the same amount of time.

Extensions of the BBT algorithm include, for example, adding informed state-space sampling. Also, heuristics could be used for ordering the belief nodes in $Q_{current}$, which will expand the promising beliefs first, thus helping with the convergence of the algorithm.
