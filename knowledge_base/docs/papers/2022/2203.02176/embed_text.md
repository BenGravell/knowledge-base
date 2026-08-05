<!-- arxiv-full-text:v1 {"arxiv_id": "2203.02176", "source": "ar5iv"} -->

## Introduction

Motion planning is a fundamental challenge in robotics. In many real-world applications, obstacles change positions over time and goals are only valid at specific times. For applications such as multi-robot assembly, multiple motion scheduling subproblems need to be solved. Assuming that obstacle trajectories are given a priori, the subproblems can be modelled as *navigation through dynamic environments*. Mathematically, this is formulated as planning through a space-time state space.

Efficient and optimal planning through space-time raises three fundamental challenges. First, since goal arrival times are unknown upfront, it becomes difficult, yet crucial, to define and adjust the time range in a coordinated and meaningful way. The second challenge is the representation of kinodynamic constraints in the planning model. Whether a movement is possible depends on kinematic parameters, velocity, and acceleration. Lastly, robots should minimize arrival time. Arrival time is crucial for long-horizon planning problems, where optimization of intermediate arrival times is one of the central challenges. These challenges make planning through space-time a demanding problem. We are not aware of any sampling-based method which either operates in unbounded space-time or is asymptotically optimal with respect to shortest arrival time.

Figure 1: Four snapshots of ST-RRT* in ℝ1 + 1 (one space, plus one time dimension). The forward tree is blue, the backward trees are red, obstacles are black, and the goal regions are yellow. (a) Using the initial batch of samples, no solution was found. (b) The upper bound of the time space (dashed line) is expanded, more goal nodes are sampled and the trees are grown. (c) An initial solution is found (orange), and the upper bound is decreased accordingly. (d) Parts of the trees that can not contribute to the solution anymore are pruned (lower opacity), and the final solution after convergence.

To address those challenges, we develop Space-Time RRT\* (ST-RRT\*). The basic operating principle of ST-RRT\* is illustrated in Fig. 1: (a) We compute an initial estimate of a feasible goal time (blue dashed line), and grow both a forward tree from the start state (blue), and a set of reverse trees from the goal regions (red). If no solution is found given a certain number of samples, the upper time limit in which we generate samples is increased (b). If a solution (orange) is found (c), the parts of the trees that can not lead to an improved solution are pruned. This process continues to improve the solution path, and tighten the upper time bound until a termination condition is reached (d).

ST-RRT\* is a bidirectional motion planning algorithm that is probabilistically complete and asymptotically optimal with respect to shortest arrival time. ST-RRT\* is able to operate in unbounded time spaces and model velocity constraints. ST-RRT\* is inspired by RRT-Connect, with three changed components to attain the stated qualities in space-time. Our main contributions are: Progressive Goal Region Expansion: ST-RRT\* gradually increases the sampled time range to efficiently operate in unbounded time spaces. Simultaneously, we adjust the sampling densities over the time dimension to ensure a more uniform sampling distribution.

Conditional Sampling: We develop a novel sampling method that prevents the sampling of states which cannot be part of a solution path due to velocity constraints.

Simplified Rewiring: To obtain optimal solutions, states are rewired similar to RRT\*. In contrast to RRT\*, we perform a simplified rewiring step, where only nodes in the set of goal trees are rewired.

We demonstrate our algorithm on both abstract (planning for a disk in up to ${\mathbb{R}}^{8 + 1}$), and simulated robotic motion planning problems (both robotic arms and mobile robots).

## Related Work

In the following two sections, we review literature on planning in dynamic environments and time-optimal path planning. For an exhaustive discussion of path planning methods we refer to and for an overview on (asymptotically optimal) sampling based path planning methods.

### II-A Planning in Dynamic environments

Planning in dynamic environments can be roughly divided in two approaches. First, we have reactive methods, which work with the assumption that the trajectories of the moving obstacles are unknown, whereas the second category assumes full knowledge of the obstacles' trajectories.

Reactive methods such as Execution-extended RRT, Closed-loop RRT, RRTX or Real-time RRT\* are methods specifically developed for rapid replanning. Rapid replanning is necessary when previously computed paths become invalid during execution. Risk-RRT incorporates predictions about the obstacles' movement, and computes partial motion paths to keep the probability of a collision under a given threshold. However, frequent replanning is still needed as only partial paths are returned. Various methods exist to enable efficient replanning, i.e. to reuse as much prior work as possible from previously planned paths, or to establish coarse connectivity of the space, and only replan for dynamic obstacles.

Contrary to reactive methods, the following methods assume full knowledge of obstacle trajectories, and thus do not rely on replanning. Time-Based RRT expands the configuration state space by the time dimension and plans unidirectionally to a set of known goal states. However, knowledge of the specific time for each goal configuration is assumed, and only unidirectional planning is supported. Safe Interval Path planning finds optimal paths with respect to shortest time by constructing a discrete search space with states defined by their configuration and a corresponding 'safe interval'. However, a graph needs to be constructed for the entire state space, and thus it suffers the inherent problems: it is only feasible for problems with few dimensions.

In this work, we assume full knowledge of all paths of the moving obstacles, but no a priori knowledge of the arrival time, as is the case in multi-robot assembly planning tasks. Thus, our method does not require replanning and is able to efficiently find feasible and time-optimal paths. Our method also enables to plan bidirectionally in unbounded time spaces, leading to a more efficient planner than other RRT-based planners in the space-time setting.

### II-B Time-optimal Trajectory planning

A common approach to find kinodynamically feasible paths is based on path-velocity decomposition: first find a geometrically feasible path, and then find a valid time-parametrization for this path. Extensions to this approach were presented e.g. , which relaxes the quasi-static requirement. However, this approach is inapplicable here, as obstacles are dynamic and the time optimization on a fixed path might render it infeasible.

Other approaches to planning include optimization approaches (e.g. STOMP, or sequential convex optimization ), or extending the configuration space with velocity coordinates. Optimization based approaches work well to incorporate complex constraints, but suffer from the well known non-convexity of the general planning problem. Furthermore, optimizing for arrival time is not straightforward. In general, these methods are not complete and therefore can not achieve global optimality.

Sampling based kinodynamic planning on the other hand, doubles the dimensionality of the state space we plan , and thus makes planning with high DoF-robots slow or even infeasible. Since time is not taken into account explicitly, planning with dynamic obstacles is not straightforward.

By extending the configuration space with a time component, and planning and optimizing in this space-time state space, we retain these guarantees. Through usage of bidirectional planning, conditional sampling, and simplified rewiring, we achieve a high efficiency.

## The Space-Time RRT\* Algorithm

We consider the motion planning problem in space-time with unbounded arrival time. Our objective is to minimize arrival time under given velocity constraints. By adding a time dimension to the configuration space we obtain the Space-Time state-space $\mathcal{X} = {\mathcal{Q} \times \mathcal{T}}$, where $\mathcal{Q}$ is the underlying configuration state space and $\mathcal{T}$ is the time state space. Note that $\mathcal{X}$ can be unbounded in time. Let $\mathcal{X}_{\text{free}} \in \mathcal{X}$ be the obstacle-free subset of states, $x_{\text{start}}$ the start state, and $\mathcal{X}_{\text{goal}} = {\mathcal{Q}_{\text{goal}} \times \mathcal{T}_{\text{goal}}}$ the goal region. In the following, we assume full knowledge of the obstacles' trajectories, and plan for holonomic robots with a given maximum velocity. We define $v_{\text{max}} \in {\mathbb{R}}^{|\mathcal{Q}|}$ as a vector containing the maximum velocity for each space component.

The goal is to compute a continuous path $p:{{\lbrack 0,1\rbrack}\rightarrow\mathcal{X}_{\text{free}}}$, such that ${p{}} = x_{\text{start}}$, ${p{}} \in \mathcal{X}_{\text{goal}}$, and the velocity constraints are satisfied. We are interested in finding not only feasible, but paths which minimize the arrival-time, ${c{(p)}} = t_{1}$ with $t_{1}$ being the time element of ${p{}} = {(q_{1},t_{1})}$.

In space-time, the distance that can be covered in a given time is constrained by $v_{\text{max}}$ and it is not possible to move backwards in time. Thus, we define our distance function $d$ between two states, $x_{1} = {(q_{1},t_{1})}$ and $x_{2} = {(q_{2},t_{2})}$ as where $d_{\mathcal{Q}}$ is the intrinsic metric of the configuration space, $\lambda \in $ weights the importance of $d_{\mathcal{Q}}$ with respect to the time-distance (but does not influence optimality), and $v^{i}$ is the required speed in dimension $i$, such that $q_{2}$ can be reached from $q_{1}$ in time $t_{2} - t_{1}$. As $d$ is not symmetric, it is only a pseudometric.

### III-A Algorithm

1:𝒳, xstart, 𝒳goal, d, ptc, tmax, pgoal, P 6: if pgoal ≥ Rnd then 7: B ← SampleGoal (xstart, 𝒳goal, Tgoal, tmax, B) 8: xrand ← SampleConditionally (xstart, 𝒳, B, d) 9: if not Extend (Ta, xrand, d) = T r a p p e d then 12: RewireTree (Ta, Tgoal, xnew) 13: if Connect (Tb, xnew, d) = R e a c h e d then The algorithmic details of ST-RRT\* are shown in Algorithms 1--5. In addition to $\mathcal{X}$, $x_{\text{start}}$, $\mathcal{X}_{\text{goal}}$, and $d$ it requires a planner termination condition ptc, a time bound $t_{\text{max}} \in {(0,\infty\rbrack}$, a probability to sample a new goal $p_{\text{goal}} \in {(0,1\rbrack}$, and several bound parameters contained in $P$ (see Section III-A1). The basic framework is similar to RRT-Connect: In each iteration a new goal is sampled with probability $p_{\text{goal}}$ (Line 6 & 7). Then, a random state $x_{\text{rand}}$ is sampled (Line 8). If possible, the current tree $T_{a}$ is expanded by the new state $x_{\text{new}}$ (i.e. the extension between $x_{\text{near}}$ and $x_{\text{rand}}$) and a connection from $x_{\text{new}}$ to the other tree $T_{b}$ is attempted (Line 9 & 13). In case of a successful connection, the solution is updated (Line 14). Finally, $T_{a}$ and $T_{b}$ are swapped and the next iteration begins (Line 18). Our extensions to RRT-Connect are: Progressive Goal Region Expansion, which progressively enlarges the time component of the space (Line 5), and samples new goals for the goal tree (Line 7), Conditional Sampling (Line 8), which first samples a state from $\mathcal{Q}$, and then samples a corresponding valid time, with which $x_{\text{rand}}$ is constructed, and Simplified Rewiring, which improves the solution (Line 12) by optimizing for minimal arrival time.

We also prune the trees (Line 17) to remove parts which cannot improve the solution anymore.

### III-A1 Progressive Goal Region Expansion

Figure 2: Illustration of the search trees after the same computation time with naive and weighted sampling strategy with similar numbers of samples (for naive sampling, not all samples are visible, and the time bound was increased beyond the shown range).

If the time-space $\mathcal{T}$ is unbounded it is difficult to generate samples distributed throughout the whole space. However, when imposing an arbitrary time-bound, the problem might become infeasible. Therefore, we expand the sampled goal region progressively whenever a new batch of samples is added. To do that, we introduce several parameters contained in the bound struct $B$: $B.\text{timeRange}$ determines the time bound for goal sampling and $B.\text{batchSize}$ determines after how many generated samples the expansion takes place. When a batch is full, $B.\text{timeRange}$ is increased by $P.\text{rangeFactor}$ and $B.\text{batchSize}$ is increased accordingly.

With an increasing time-bound, the sample density is higher at the lower time values due to the previously generated samples. Figure 2 shows how naive sampling may lead to cases where it becomes increasingly unlikely to find any solution. Thus we use weighted sampling, where the old and newly expanded region are explicitly sampled with probability $B.\text{batchProbability}$ and ${1 - B}.\text{batchProbability}$, respectively, to ensure a uniform distribution over the total space.

Precisely, the Progressive Goal Region Expansion works as follows: The parameters $P.\text{rangeFactor}$, $P.\text{initialBatchSize}$, and $P.\text{sampleRatio}$ are user-specified. All variables of $B$ are initialized at the start (Algorithm 2) and updated during execution. While $B.\text{timeRange}$ is used when the current goal region is sampled, $B.\text{newTimeRange}$ is used to sample the newly expanded one. After the first expansion, $B.\text{newTimeRange}$ is always higher than $B.\text{timeRange}$ by a factor equal to $P.\text{rangeFactor}$ (Alg. 3, Line 3 & 4). The minimum amount of the new batch size is given by ${(P.\text{rangeFactor} - 1)} \cdot B.\text{totalSamples}$. That is, when all samples of the new batch are placed in the new region, the overall distribution would be uniform over the time-space. To ensure that the old region is also sampled, $B.\text{batchSize}$ is further increased by $P.{\text{sampleRatio} \in {}}$ (Line 5). The probability to sample the old batch $B.\text{batchProbability}$ is calculated in dependence of $P.\text{rangeFactor}$ and $P.\text{sampleRatio}$ (Line 6). Due to the exponential growth of the batch size, the choice of the configuration parameters is important for performance.

To sample a goal state, its space component $q$ is sampled first (Alg 4, Line 2). The lower and upper bounds for the time, $t_{\text{lb}}$ and $t_{\text{ub}}$, are calculated in dependence on whether the time is explicitly bounded (Line 5), the current region is sampled (Line 7), or the newly expanded one is sampled (Line 9). The sampling of nongoal-states is subject to the sampled goal states and therefore implicitly bounded by the time value of the sampled goal states (Section III-A2).

2:if tmax = ∞ and B.samplesInBatch = B.batchSize then 5: $B.{\text{batchSize}\leftarrow\frac{{(P.\text{rangeFactor} - 1)}B.\text{totalSamples}}{P.\text{sampleRatio}}}$ 6: $B.{\text{batchProbability}\leftarrow\frac{{1 - P}.\text{sampleRatio}}{P.\text{rangeFactor}}}$ 7: B.goals ← B.goals ∪ B.newGoals 1:xstart, 𝒳goal, Tgoal, tmax, B 3:tmin ← LowerBoundArrivalTime (qstart, q) 4:SampleOldBatch ← Rnd ≤ B.batchProbability 6: tlb ← tmin; tub ← tmax 7:else if SampleOldBatch then 8: tlb ← tmin; tub ← tmin ⋅ B.timeRange 10: tlb ← tmin ⋅ B.timeRange 11: tub ← tmin ⋅ B.newTimeRange 12:if tub > tlb then 13: t ← SampleUniform (tlb, tub)

### III-A2 Conditional Sampling

Figure 3: The start and goal cones contain all states that can be reached from the start or can reach the goal respectively. The intersection contains all states that can be part of a solution.

Any state that can be part of a solution path must have a finite distance $d$ to the start and at least one goal state. Due to velocity-constraints, only states in the intersection of the start and goal cones (see Fig. 3 for an illustration) meet this requirement. Thus, similar to Informed RRT\*, we only sample the region that can produce solutions. Ideally, one would sample directly from the union of intersections of start and goal velocity-cones.

However, as the explicit computation of the intersection is not possible for multiple goal states, we use Conditional Sampling: We first uniformly sample a configuration $q$ (Alg 5, Line 3). Using $q$, we then sample a feasible time from the range of possible times conditioned upon $q$. The range of possible times is dependent on $x_{\text{start}}$ and the previously sampled goal states. To sample more uniformly, we use two goal sets: $B.\text{goals}$ for the current goal states and $B.\text{newGoals}$ for the goal states in the newly expanded region. The time bounds $t_{\text{lb}}$, $t_{\text{ub}}$ are obtained by the minimal arrival time from the start configuration $q_{\text{start}}$ until $q$ (Line 4) and the maximum valid time given: The specific calculation of $t_{\text{lb}}$, $t_{\text{ub}}$ is dependent on whether the current (Line 5) or the new region is sampled (Line 8).

4: tmin ← tstart + LowerBoundArrivalTime (qstart, q) 5: if Random < B.batchProbability then 7: tub ← MaxValidTime(q, B.goals) ⊳ eq 9: tmin* ← MaxValidTime(q, B.goals) 10: tlb ← Max (tmin, tmin*) 11: tub ← MaxValidTime(q, B.newGoals) 12:until tlb < tub 13:t ← SampleUniform (tlb, tub)

### III-A3 Simplified Rewiring

To compute time-optimal solutions ST-RRT\* uses similar methods as RRT\* and preserves its property of asymptotic optimality. Equal to RRT\*, ST-RRT\* tries to rewire a set of states near to the newly added state, $x_{\text{new}}$, after tree expansion. Contrary to RRT\*, rewiring is only performed in the goal trees. This is due to the fact that rewiring nodes in the start tree can never lead to a better arrival time in the path. Rewiring states in the start tree can not change their arrival time, whereas in the goal trees a node can be rewired to a root node with a smaller time value. One more deviation is the check of which nodes should be rewired. For all nodes in the goal trees simply the time value of their respective root node has to be considered.

### III-B Proof Sketches

To prove probabilistic completeness in space-time, we distinguish between two cases. In case of bounded time, planning with a quasi-metric reverts to kinodynamic planning, where we refer to results from and for completeness proofs.

The second case is unbounded time: If a solution exists, there needs to be a feasible goal region at a finite time. Since we iteratively increase the upper bound, we will, eventually, have increased the goal region to include the feasible goal region. Due to the use of uniform sampling of the time range, there will be positive probability that the feasible goal region will be sampled. Since conditional sampling always gives a positive probability of sampling any open set, this makes ST-RRT\* retain probabilistic completeness.

Apart from probabilistic completeness, ST-RRT\* is also asymptotically optimal with respect to arrival time. Since ST-RRT\* is modelled after RRT-Connect, it can be made asymptotically optimal by tree rewiring. Inside the rewiring step, we connect newly added states to the nearest goal tree which minimizes arrival time. This ensures asymptotic optimality with respect to final arrival time.

## Evaluation

We compared ST-RRT\* to other planners on 4 different scenarios using the benchmarking capabilities of OMPL. All evaluations were performed over $100$ runs with different pseudorandom seeds of $30\text{s}$ each (if not stated otherwise). ST-RRT\* is compared to RRT-Connect^11^1The metric had to be changed to be symmetric for distance calculation, but remained as stated for motion validation (this change did not help in the other planners). and RRT\* in space-time using their OMPL implementations in default configuration. Since RRT\* and RRT-Connnect algorithms can not operate on unbounded time, three different time bounds are measured. The lowest time bound was determined according to the best solutions of ST-RRT\* and set to a higher value to ensure feasibility. Without knowing a solution this is generally not possible. For planning through Space-Time, most of the planners in OMPL do not work either due to only working with metric spaces, only working with euclidean spaces, not supporting asymmetric distance function (e.g. due to using undirected graph structures), or were never able to find solutions in the specified runtime.

### IV-A Scenarios

(a) Narrow passage in time (ℝ1 + 1).

(b) Rnd. moving obstacles (ℝ2 + 1). Obstacle start in black, end position in grey.

Figure 4: Illustrations of the scenarios: Starts are shown in blue, goals and goal regions in yellow, and obstacles in black. The dashed lines are the paths of the moving obstacles.

We evaluate the method on the following scenarios^22^2Videos of the scenarios, and the paths are in the supplementary material.: Narrow passage: A point has to move from start configuration $q_{0}$ to goal configuration $q_{F}$ in an environment where the configuration space is split into two parts by an obstacle up to a certain point in time except for three narrow periods of time (Fig. 4(a)).

Cluttered space: A (hyper-)sphere has to move from $q_{0}$ to $q_{F}$ in an environment with randomly moving obstacles (Fig. 4(b)).

Sequential mobile robot planning: A robot with a mobile base and a robot arm on top (${\mathbb{R}}^{8}$) has to move from $q_{0}$ to $q_{F}$ in an environment with randomly distributed obstacles, and other moving mobile robots that move on a fixed trajectory (Fig. 4(c)). This is a common subproblem in prioritized multi robot planning.

Sequential robot arm planning: A robotic arm (${\mathbb{R}}^{7}$) has to move from configuration $q_{0}$ to $q_{F}$ in an environment with previously planned panda robotic arms (Fig. 4(d)). Such a scenario may arise in e.g. simultaneous bin-picking with multiple robots.

We show the narrow passage problem in ${\mathbb{R}}^{1 + 1}$ and ${\mathbb{R}}^{8 + 1}$ and the cluttered env. in ${\mathbb{R}}^{2 + 1}$ and ${\mathbb{R}}^{8 + 1}$. For the robotic settings, we test the planners in the 6$^{\text{th}}$ and the 11$^{\text{th}}$ agent (i.e. the previous 5, and 10 agents, respectively, already have a trajectory).

(a) Narrow passage in time: ℝ1 + 1 (b) Narrow passage in time: ℝ8 + 1 (c) Rnd. moving obstacles: ℝ2 + 1 (d) Rnd. moving obstacles: ℝ8 + 1 (e) Mobile robots: 6th agent (f) Mobile robots: 11th agent: 100 s (g) Robot arms: 6th arm (h) Robot arms: 11th arm Figure 5: Success rates and cost plots for the experiments (Section IV-A) for ST-RRT*, RRT-Connect, and RRT* over 100 runs. RRT-Connect and RRT* were run with 3 different upper bounds, tub for the time (indicated in the figure), since they can not operate in unbounded time-spaces. The thick line is the median, and the shaded area in the cost plot shows the 95% nonparametric confidence interval. Cost for RRT-Connect is shown as the median with error bars for the 95% nonparametric confidence interval. Unsuccessful runs are treated as infinite cost. The upper time limits for RRT* and RRT-Connect are listed in the figures. Planners that are not shown were not able to find any solution in the given time.

### IV-B Experimental Results

We analyze the results of both the abstract experiments (Fig. 5(a) - Fig. 5(d)), and the simulated robot experiments (Fig. 5(e) - Fig. 5(h)). We compare the success rates and the cost-convergence plots of the different algorithms.

### IV-B1 Initial solution time

In almost all cases the median initial solution time of ST-RRT\* is lower than for both RRT-Connect and RRT\*, even with the tightest time-bound. This can be attributed to the conditional sampling, which helps avoid exploring areas that are clearly not reachable.

### IV-B2 Success Rate

A low time bound helps to more quickly find solutions for RRT-Connect and RRT\*; however, it can lead to the inability to find solutions at all. This is especially problematic for RRT-Connect which stops sampling goal states at some point, leading to RRT-Connect sometimes not reaching 100% success rate even though the time bound is specified such that a solution would be attainable.

### IV-B3 Cost

ST-RRT\* converges to the best found solution more quickly than RRT\*. Additionally, while the initial cost of the solution of ST-RRT\* is sometimes higher than RRT-Connect's solution, the final solution cost of ST-RRT\* is in all cases lower or equal than for the other methods.

Summarizing the results, a special treatment of the time-space is clearly necessary in a planner to achieve good performance in the motion planning process and ST-RRT\* outperforms the other planners on the tested problems.

## Conclusion

We proposed ST-RRT\*, a planning algorithm that is able to efficiently deal with unbounded time spaces and optimizes for arrival time in an environment with moving obstacles on known trajectories. We guarantee probabilistic completeness and asymptotic optimality by introducing progressive expansion of the goal space and generate new samples accordingly. Our algorithm efficiently deals with many goals and converges to the optimal path quickly by making use of conditional sampling and shrinking the goal spaces.

The current implementation of ST-RRT\* still has two limitations: the batch size and the expansion factor must be chosen in the beginning with a crude estimate of when the goal can be reached. In practice this is not a large limitation since real settings usually impose some upper limit on the acceptable maximum time to reach a goal state. Additionally, acceleration and more complex kinodynamic constraints (e.g. torque limits) are not taken into account. While this does not pose a problem in our applications, it would not be applicable to robots which have to be in quasi-static equilibrium.

We experimentally demonstrated that ST-RRT\* scales well to high dimensions on both abstract and simulated robotic experiments. Our algorithm outperforms state of the art algorithms on both initial solution time and convergence to the optimal solution. An initial version of ST-RRT\* was used in work on large-scale multi-robot coordination.
