<!-- arxiv-full-text:v1 {"arxiv_id": "2510.21074", "source": "arxiv-html"} -->

## Introduction

A key application of motion planning algorithms in robotics is to find paths in environments with unknown or dynamic obstacles. Most planners use some combination of predictive or reactive approaches to find feasible or optimal paths quickly and efficiently. Predictive approaches attempt to predict the movement of obstacles in the environment and generate plans around these predictions. Reactive approaches make exact plans using the known information and quickly modify them when changes are detected.

Predictive planners leverage a priori knowledge of their likely environments to improve their planning efficiency and path quality. When this includes the trajectories of dynamic obstacles, the planner can find plans that guarantee it does not collide with obstacles. Planners may also inform their paths by avoiding sections of the environment that are likely to contain an obstacle or ensuring their paths are valid within assumed obstacle parameters.

Figure 1: A Franka Research 3 arm replanning around a dynamic obstacle by independently solving new planning problems each time the obstacle information changes. The VAMP implementation of AORRTC plans fast enough in a CAPT obstacle map that it is able to replan without stopping the arm.

Figure 2: A visualization of the paths travelled on 50 attempts of the incremental planning problem done by EIT*, RRT*, RRT-Connect and RRTX with a planning budget of 0.1s. The hue of each path is determined by the order it was run in the experiment. The length of a planner’s global solution is the overall length of the path travelled. EIT* found the smallest median global solution length and had a 100% success rate. RRT* followed similar paths to EIT* due to its ASAO properties, when it was successful, but only succeeded 6% of the time. RRT-Connect also maintained a 100% success rate but had a longer median path length than EIT*. RRTX had a 0% success rate due to the overhead of optimally rewiring its solution trees.

The quality of the paths found by predictive approaches depends heavily on the quality of the predictions. These can be poor in situations with limited preexisting data or highly complex dynamics. In such challenging environments, robots must pair their predictions with reactive planning.

Reactive approaches do not require assumptions about the position or motion of obstacles. These methods instead quickly generate intermediate plans when obstacle changes are detected. A successful reactive planner must efficiently generate high-quality intermediate paths while remaining consistent with the previously executed path.

Plan-reuse algorithms maintain consistency to previous plans by keeping the existing search and updating the parts affected by the change. This can allow them to provide formal guarantees on the optimality of their intermediate solutions (e.g., D\*, LPA\*, RRT^X^ ). They find better global paths than reactive approaches that focus solely on reaction times (e.g., bug algorithms ) but can be slower to react to changes in information.

Plan-reuse methods require the locations of obstacle changes in their search trees to efficiently maintain optimal intermediate paths. These locations may sometimes be available in the map representation but otherwise require manual evaluation to find. Changed edges can always be found by iterating through each edge in the search graph and confirming that it is still obstacle free. This increases the time it takes to update plans and may require a prohibitively large number of collision checks on large graphs.

Recent almost-surely asymptotically optimal (ASAO) planners are able to quickly converge towards optimal solutions to complex problems. This provides an alternative for fast, globally optimal replanning without the complexity and computational overhead of plan reuse. Fast ASAO planners (e.g., Effort Informed Trees; EIT\* \[22 and Effort Informed Trees (EIT*): asymmetric bidirectional sampling-based path planning")\], Asymptotically Optimal RRT-Connect; AORRTC ) can instead be run independently each time information changes to quickly find intermediate paths with optimality guarantees.

This challenges the historical assumption that fast incremental planning requires plan reuse. This paper demonstrates that independent runs of EIT\* outperform all other tested incremental planning algorithms on the simulated problems, including RRT^X^, a planner specifically designed for efficient plan reuse. EIT\* finds more and higher-quality solutions than all other planners across all tested planning budgets, successfully replanning as quickly as 50ms in simulated experiments. It also evaluates this approach on a real robotic platform using AORRTC for moving-obstacle avoidance on a Franka Research 3 arm (Figure 1).

The rest of this paper is organized as follows. Section II presents a discussion of current and classic approaches to incremental planning. Section III presents further background and the independent incremental planning approach. Section IV presents the experimental details and Section V presents a discussion of the results. Finally, Section VI provides a conclusion and discusses future work.

## Literature Review

Most replanning systems include a combination of predictive (Section II-A) and reactive (Section II-B) approaches.

### II-A Predictive Approaches

Predictive approaches leverage a priori information about their operational environments to inform their path plans but are susceptible to error in highly complex environments.

Space-Time RRT\* (ST-RRT\*) uses ASAO planning to find paths through moving obstacles with optimality guarantees when their trajectories are known. ST-RRT\* uses an ASAO planner in a space augmented with a time dimension to model obstacle movements. This approach yields optimal plans through the moving obstacles but assumes perfect knowledge of their trajectories.

Velocity obstacle approaches assume that obstacles move up to a predetermined velocity and plan a trajectory to the goal avoiding any region that may be occupied by an obstacle under this constraint. Velocity constraints ensure the feasibility of solution paths but conservative bounds may restrict the quality of the solutions found and can create unsolvable problems.

Finite-horizon Model Predictive Control (MPC) can also be used to avoid obstacles. These approaches simultaneously react to obstacle changes and predict future trajectories by solving a finite-horizon optimal control problem defined by obstacle predictions. This replans quickly but provides no optimality guarantees on the intermediate paths if the problem horizon is shorter than the path to the goal.

### II-B Reactive Approaches

Reactive approaches do not require assumptions about the dynamics of their environments but must be able to quickly replan to maintain feasibility through the environment.

Bug algorithms avoid expensive planning by following a deterministic policy. Basic bug algorithms drive a straight-line path to the goal when possible and follow the perimeter of any obstacles they encounter. Bug algorithms react quickly to new obstacles but provide no optimality guarantees and often execute highly suboptimal paths.

Following suboptimal intermediate paths may result in the robot unnecessarily changing the homotopy class of its path which can lead to a much longer global solution. Many existing approaches avoid this problem by providing guarantees of near-optimal intermediate paths.

Zelinsky presents an algorithm that replans from scratch with A\* once environment changes are detected. This approach guarantees resolution-optimal intermediate paths but suffers from slow intermediate path formulation.

D\* extends the A\* algorithm to replan when information changes. It improves the replanning speed by propagating local graph updates through the previous graph once changes are detected. This is proven to find the resolution optimal solution given the information available at the time of planning but assumes it is given all graph changes and does not account for the computational cost of detecting them.

Lifelong Planning A\* (LPA\*) also directly extends A\* to incremental planning. It further improves replanning speed by only propagating updates through edges that are affected by graph changes. LPA\* also assumes knowledge of which edges in the graph have changed and does not consider the computational cost of detecting changes.

Lifelong Generalized Lazy Search (L-GLS) extends LPA\* to take advantage of the efficiency of lazy search algorithms. This finds the resolution optimal solution faster than other graph-based incremental replanners by deferring expensive edge checks until necessary but does not avoid the computational costs of detecting changes.

Execution extended RRT (ERRT) extends the Rapidly-exploring Random Trees (RRT) algorithm to incremental planning. ERRT samples states from previous planning efforts to bias its search toward previous paths. This can reduce the replanning time if obstacle locations are similar between planning efforts but provides no guarantees about the quality of its intermediate solutions.

Dynamic RRT (DRRT) also extends RRTs to incremental planning. DRRT reuses feasible branches of previous planning efforts to speed up intermediate path planning but it must validate all of its previous edges once obstacle changes are detected and makes no guarantees about the quality of its intermediate solutions.

RRT^X^ extends RRT\* to apply ASAO sampling-based planning methods to incremental planning. RRT^X^ efficiently repairs its path as information changes and plans from the goal state to avoid unnecessary rerooting of the tree once the planner's location is updated. RRT^X^ does not consider the computational costs of detecting which edges in its solution tree are invalidated by obstacle changes.

Multiobjective Dynamic RRT\* (MOD-RRT\*) uses a modified RRT\* to find an initial path to the goal and then uses a rewiring method to quickly repair paths that collide with obstacles near the robot. This rewiring does not explicitly maintain path optimality and therefore provides no guarantees around intermediate path quality. MOD-RRT\* avoids expensive rewiring cascades by only rewiring locally and not propagating costs through the tree but this reduces the quality of its global solutions.

### II-C Independent Replanning

Any single-query planner can be used for incremental planning by solving a new independent planning problem each time new obstacles are detected. This does not require specific knowledge of obstacle changes and therefore avoids the computational overhead of many replanning methods. When these problems are solved optimally, the resulting global path will avoid unnecessary changes of direction (i.e., homotopy class switches) but each independent problem must be solved quickly enough to react to obstacle changes.

Recent ASAO planners, such as EIT\* \[22 and Effort Informed Trees (EIT*): asymmetric bidirectional sampling-based path planning")\] and AORRTC, quickly find high-quality solutions and their intermediate paths may be combined into high-quality global solutions without the extra computational cost of replanning.

## Methodology

Incremental planning is an extension of optimal planning with imperfect information about the environment.

### III-A Optimal Planning

The optimal planning problem is defined similarly to. Let $X\subseteq\mathbb{R}^{n}$ be the state space of the planning problem, $X_{\mathrm{obs}}\subset X$ be the set of states in collision with obstacles, and $X_{\mathrm{free}}$ = $\mathrm{closure}(X\setminus X_{\mathrm{obs}})$ be the resulting set of permissible states. Let $x_{\mathrm{start}}\in X_{\mathrm{free}}$ be the initial state and $X_{\mathrm{goal}}\subseteq X_{\mathrm{free}}$ be the set of desired final states. Let $\sigma:\to X$ be a sequence of states (i.e., a path) and $\Sigma$ be the set of all paths.

The optimal solution is the path, $\sigma^{*}\in\Sigma$, that minimizes a chosen cost function, $c:\Sigma\to\mathbb{R}_{\geq 0}$, while connecting the start, $x_{\mathrm{start}}$, to any goal, $x_{\mathrm{goal}}\in X_{\mathrm{goal}}$, through free space, where $\mathbb{R}_{\geq 0}$ denotes the set of all real numbers greater than or equal to zero.

### III-B Incremental Planning

Figure 3: A visualization of the intermediate paths found by EIT* with a sensor range of 0.1 and a planning budget of 0.1s. The gray area is unsensed and assumed to be free space by the planner. The dark green dot represents the starting point of the query, and the red dot represents the goal. The green path represents the path travelled so far. The number of circles gives a representation of the number of queries of the planner.

The incremental planning problem is an extension of the optimal planning problem where the locations of obstacles in the environment are not perfectly known and may change as the robot moves. Exact knowledge of obstacles is assumed to be limited to those detected in a specified distance of the robot, $r_{\text{s}}$, within a retrospective time horizon, $\tau$.

Let $B(r_{\text{s}},x)\subset X$ denote a sensing region (e.g., a ball) with maximum sensing range, $r_{\text{s}}\in\mathbb{R_{\mathrm{\geq 0}}}$, and a center point, $x\in X$. The robot has exact knowledge of obstacles that are within the sensor range of its current position, i.e., $X_{\mathrm{sensed}}(t)=X_{\mathrm{obs}}(t)\cap B(r_{\mathrm{s}},x)$, where $X_{\mathrm{obs}}(t)$ is the obstacles at time $t$. Let $X_{\mathrm{sensed},i}$ be the set of all obstacles sensed by the robot and considered for planning at the $i^{\text{th}}$ iteration, $X_{\mathrm{sensed},i}=\bigcup_{t=t_{i}}^{t_{j}}X_{\mathrm{sensed}}(t)$, where $t_{i}=t_{j}-\tau$ is the minimum time from which the planner still uses its previous obstacle measurements. The robot may also include a prior over obstacle motions in its set of obstacles.

The robot plans in the free space defined by the set of obstacles sensed within the retrospective time horizon, $X_{\mathrm{free},i}=X\setminus X_{\mathrm{sensed},i}$, and follows the resulting solution path, $\sigma_{i}$, until it reaches a state at which it determines it must replan , $x_{i+1}$. This process repeats until the robot reaches the goal, $X_{\mathrm{goal}}$.

Let $s_{i}\in$ denote the parameter at which the robot replans from when following its $i^{\text{th}}$ intermediate solution path, i.e., $x_{i+1}=\sigma_{i}(s_{i})$. Let $\sigma_{i,s_{i}}:[0,s_{i}]\to X$ denote the partial path travelled during the $i^{\text{th}}$ planning iteration. The global solution path is defined as $\pi=\sigma_{1,s_{1}}\oplus\sigma_{2,s_{2}}\oplus\cdots\oplus\sigma_{N,s_{N}}$, where $\oplus$ denotes path concatenation and $N\in\mathbb{Z_{\mathrm{\geq 0}}}$ is the number of planning cycles until the goal is reached. An incremental planner seeks to minimize the cost of its global solution, $c(\pi)$.

### III-C Independent Incremental Planning Approach

The independent incremental planning approach uses independent calls to ASAO planners to solve the incremental planning problem. The robot solves an independent optimal planning problem in the free space defined by the sensed obstacles at each planning iteration, $X_{\mathrm{free},i}=X\setminus X_{\mathrm{sensed},i}$, to find a path, $\sigma_{i}$. The robot follows the path until it arrives at a state at the edge of the sensed area or otherwise determines it needs to replan, $x_{i+1}$. The robot updates its obstacles using the sensor and then replans from the new position. The process of planning, following the solution path and sensing repeats until the robot reaches the goal.

Let $\sigma^{*}_{i}$ be the shortest path in the known free space from the current state, $x_{i}$, to the goal. Let $\sigma^{*}_{i,s_{i}}$ denote the subpath of $\sigma^{*}_{i}$ that ends at the next sensing boundary. Following the optimal path with respect to the given information at each iteration, $\sigma^{*}_{i,s_{i}}$, minimizes the worst-case total path cost over all possible environments, given the current information.

The quality of a global solution to the incremental planning problem depends on the quality of its intermediate paths. If the planner finds sufficiently optimal intermediate solutions then the executed path will avoid oscillating between different homotopy classes (i.e., be consistent) without explicitly considering path consistency and result in a near optimal global solution. If the planner does not provide optimality guarantees then it may yield suboptimal intermediate paths that are inefficient, backtrack, and/or unnecessarily switch homotopy classes and generally reduce the quality of the global solution.

Given: X, x0, xgoal, rs, planner 7 σi ← planner(xi, xgoal, Xfree, i); 12 $X_{\mathrm{sensed},i}=\bigcup_{t=t_{i}}^{t_{j}}X_{\mathrm{sensed}}(t)$; Algorithm 1 Independent Incremental Planning

## Experiments

(b) Random Rectangles Success Rates at 100ms (c) Random Rectangles Success Rates at 50ms (e) Wall Gap Success Rates at 100ms (f) Wall Gap Success Rates at 50ms (h) Double Enclosure Success Rates at 100ms (i) Double Enclosure Success Rates at 50ms Figure 4: The success rates of all planners across 100 runs on three of the simulated worlds. A visualization of the world as well as a solution found by EIT* is shown in (a), (d) and (g). Each of the planners was tested with a planning budget of 0.1s and 0.05s. The success rate at the nth query is defined by the percentage of planners that are able to find a solution to the nth intermediate problem within the planning budget. Success rates are carried forward, i.e., if a planner fails on a query it is also considered to fail on all subsequent queries. The independent ASAO approach with EIT* maintained the highest success rate across every world and every planning budget while finding the shortest global solution (Table I).

The independent incremental planning approach was tested on both probabilistically complete (RRT-Connect with and without smoothing) and ASAO planners (RRT\* and EIT\*) and was compared against a state-of-the-art planner designed for incremental replanning problems (RRT^X^). Since the planning time of RRT^X^ is slow when it has to optimally rewire dense solution trees, results are presented for both the full version of RRT^X^ and a version that stops after it finds an initial solution to provide best-case results for RRT^X^ with respect to initial solution time.

Each of the planners were tested on three types of simulated worlds using publicly available Open Motion Planning Library (OMPL) implementations with the partial RRT^X^ implementation publicly available in OMPL extended to handle replanning. EIT\* used a batch size of 100, radius factor of 1.001, repair factor of 1.2 and used the $k$-nearest implementation with pruning. RRT-based planners used a maximum edge length of 0.3 and single-tree RRT-based planners used a goal bias of 0.05. RRT^X^ was run without informed sampling and an epsilon of zero. RRT\* was run with a rewire factor of 1.001.

The incremental planning problem was simulated as an extension of the Planner Development Tools (PDT) \[4: reproducible experiments and statistical analysis for developing and testing motion planners")\]. The simulation requires three parameters to describe the environment: a planning budget, $t$, a maximum sensor range, $r_{\text{s}}$, and a global problem. The environment the planner interacts with for each intermediate problem is referred to as the *incremental* environment. The simulation assumes that all sensed obstacles are stationary, i.e., $\tau=\infty$.

The incremental environment starts out empty with the same start, $x_{0}$, and goal, $X_{\text{goal}}$, as the global environment. Only the obstacles within the sensor range from the start are added, and the planner attempts to find a path from the start to the goal that avoids these obstacles before the planning budget runs out. If the planner succeeds in finding a solution, the robot follows this path until it reaches a state at the end of the sensor radius, $x_{1}$. Once the robot has moved, a circle centered at its current position with a radius equal to $r_{\text{s}}$, i.e., $B(r_{\mathrm{s}},x_{1})$, is added to the sensed area. The next incremental problem is defined as a new optimal planning problem using $x_{1}$ as its starting point. The obstacles in this problem are the intersection of all obstacles in the global environment and the (now larger) sensed area. This process is repeated until the planner reaches the goal (Figure 3). This sequential planning problem under the free space assumption occurs when planning with limited sensing range and also for dynamic obstacles without any predictions.

The performance of RRT^X^ depends on the computational cost of detecting edges that are invalidated by newly discovered obstacles. This can be computationally inexpensive in map representations that provide this information directly or expensive when each existing edge must be checked each time new obstacle information is received. In order to provide best-case results for RRT^X^, the computational cost of detecting invalidated edges for RRT^X^ was ignored in the experiments.

### IV-A Simulated Experiments

The simulated worlds are two-dimensional path length minimization problems in a square environment, $X=^{2}$. A sensor range of 0.1 was used on each Random Rectangles world, 0.075 on the Wall Gap world and 0.05 on the Double Enclosure world.

### IV-A1 Random Rectangles

Each random world consists of 20 randomly placed rectangles with side lengths uniformly distributed between 0.1 and 0.2. The starting state is $(-0.1,-0.1)$, and the goal state is $(0.4,0.4)$. Each world is checked for validity (i.e., a feasible path exists) before it is used. Figure 4a illustrates a representative world for which individual results are presented. The random worlds evaluate the capability of each planner to quickly navigate around many obstacles to reach the goal.

### IV-A2 Wall Gap

The wall gap world (Figure 4d) has two rectangles as obstacles centered about the y-axis. There is a narrow rectangular gap between the two rectangles that the planner must navigate through. The wall gap tests the ability for planners to find and navigate through a narrow gap at the center of the world.

### IV-A3 Double Enclosure

The double enclosure is two rectangular enclosures, each with one open end, containing the start and goal (Figure 4g). The planner initially sees an unobstructed path from start to goal but will discover it is blocked after travelling towards it. The planner must then retrace back towards the start to leave the first enclosure and then circumnavigate the second enclosure to reach the goal. The double enclosure tests the planner's ability to adapt when initial plans are proven invalid by new information.

Three sets of experiments were run using the simulated worlds. Every planner was run 100 times on the Wall Gap problem, Double Enclosure problem and 40 different Random Rectangles problems with a planning budget of 0.1s to investigate the performance of each planner on a diverse set of problems. Every planner was run 100 more times on the Wall Gap problem, Double Enclosure problem and a representative Random Rectangles problem with a planning budget of 0.05s to investigate their performance on representative problems with a smaller budget. Each planner was also run 10 times with planning budgets of 0.01s, 0.05s and 0.1s on 100 different Random Rectangles problems for each planning budget to investigate the performance of each planner at different planning budgets (Figure 5).

Figure 5: The combined success rate of each planner on 100 different random worlds for planning budgets of 0.01s, 0.05s and 0.1s. EIT* had the highest total success rate at each planning budget and RRTX was not able to consistently solve the problems in the available time.

### IV-B Results

The per-query success rate, global solution time, global path length, and number of queries were measured for each simulated world. The combined success rate, median problem success and median rank of each planner's median global path length, global solution time, and number of queries were also collected across the 40 random worlds. The combined success rate across all runs over the 100 random worlds was collected for each planning budget. A summary of the results from a planning budget of 0.1 seconds is presented in Table I. Only the success rates are shown for the 50ms experiments (Figure 4) since EIT\* was the only planner that solved more than 50% of all trials on all of the worlds. A plot of the total success rate over 100 random worlds at each planning budget is shown in Figure 5.

### IV-B1 Success Rates

The success rate for each query is shown in Figure 4. The success rate at a given query is a measure of how often the planner is able to find a solution within the given planning budget at that query. The global success rate (i.e., the percentage of runs that the planner reached the goal) can be extracted from the success rate at the final query. EIT\* had the highest global success rate on all simulated worlds at all evaluated planning budgets. None of the evaluated planners had 100% success on all problems because some randomly generated worlds require solutions to pass through very narrow gaps to reach the goal. Increasing the planning budget further on these difficult problems would increase their success rate.

### IV-B2 Global Path Length

The median global path length is shown in Table I. The global path length measures how far each planner travelled from the start to the goal. The global path length is the length of the portions of the intermediate paths followed to travel between the start and goal. EIT\* had the shortest median global path length on all problems due to the high-quality intermediate paths it finds as a result of its ASAO properties.

### IV-B3 Global Solution Time & Queries

The median global solution time and median number of queries are shown in Table I. The global solution time is the total time spent finding a solution to the incremental planning problem. The number of queries is the number of intermediate queries a planner took to reach the goal.

Nonoptimal planners, such as RRT-Connect, do not spend the whole planning budget and instead return as soon as they find an initial solution. Optimal planners, such as RRT\* and RRT^X^, first find an initial solution and then spend the rest of the planning budget searching for shorter paths. Other optimal planners, such as EIT\*, have the capability to exit early if they detect that they have found the optimal solution. The number of queries is presented alongside the global solution time to give a fair comparison between planners.

EIT\* had the smallest median number of queries on all problems. RRT-Connect had a smaller median global solution time than EIT\* on the Wall Gap and Double Enclosure problems since it does not use the whole planning budget. EIT\* maintained the smallest median global planning budget on the selected Random Rectangles problem despite spending the whole planning budget optimizing its paths due to the small number of queries it needs to solve the problem.

Rand. Rect. (Example) Rand. Rect. (Agg.)

TABLE I: A summary of all planning results on the Random Rectangles, Wall Gap and Double Enclosure simulated worlds. Each result shows the percentage of successful runs, the median solution path length, the median solution time, and the median number of queries taken to reach the goal. Clopper-Pearson 95% confidence intervals are shown in brackets for single-environment success rates and nonparametric 95% confidence intervals for the median of all other metrics. The best result on each environment is shown in bold. Unsuccessful trials were considered to have infinite path length, solution time, and queries. The combined success rate, median success rate and the median rank of each planner’s median path length, median global solution time and median number of queries are shown for the 40 different Random Rectangles worlds.

### IV-C Real-World Planning

A VAMP implementation of AORRTC was used as the incremental planner to navigate a seven DoF Franka Research 3 robot arm around moving obstacles. A collision-affording point tree (CAPT) was used to efficiently map obstacles presented in different configurations and AORRTC planned a new solution around each of the different obstacles with no prior knowledge of their locations.

AORRTC successfully navigated past each obstacle configuration in real-time due to its ability to quickly find high-quality intermediate paths. The robotic arm experiment demonstrates the ability for fast ASAO planners to navigate successfully in high-dimensional environments with moving obstacles without modelling their motion.

## Discussion

The simulated experiments show that the incremental planning problem can be solved by independent planning and that when these planners find high-quality solutions quickly this independent incremental planning approach outperforms specifically designed incremental planners.

RRT-Connect was able to quickly find solutions to intermediate problems but had larger median global path lengths than the ASAO planners. The lack of solution quality guarantees meant that RRT-Connect did not find consistent paths, both with and without smoothing. This resulted in paths that unnecessarily left the sensed area or changed homotopy classes and resulted in more planning queries than necessary. The smoothed variation of RRT-Connect outperformed unsmoothed RRT-Connect on path length and number of queries but had a longer median path length and larger number of queries than EIT\* across all problems. Both variations of RRT-Connect had lower total success rates than EIT\* on all sets of random worlds because their inconsistent intermediate solutions cause them to solve an unnecessarily large number of planning queries to reach the goal.

RRT^X^ failed to find a complete global solution within the incremental planning budget on more than 90% of its trials across all simulated worlds. This is because RRT^X^ spends computational effort to update its entire search tree each time obstacles change, even if parts of it are not necessary to solve an individual query. RRT^X^ has to rewire potentially very large trees when there are significant obstacle changes that affect many edges in its solution tree, which is computationally expensive.

The computational cost of this tree update also increases with the planning budget. A large planning budget means that more nodes will be inserted during each query and therefore need to be rewired and collision checked when updating the tree in future queries. This is an inherent trade-off of anytime-resolution plan-reuse algorithms, since the tree becomes more dense with more time between queries. This has been addressed in multiquery settings by rewinding the sample density between queries \[6: efficient asymptotically optimal multiquery planning by actively reusing validation effort")\].

The computational cost of optimally rewiring dense solution trees is further demonstrated by the performance of RRT^X^ when it is limited to only finding an initial solution. This truncated version of RRT^X^ was able to find solutions to more intermediate queries than the full RRT^X^ on most simulated experiments but failed to find a complete global solution within the incremental planning budget on more than 90% of the trials.

RRT\* was able to find shorter median global path lengths than RRT-Connect and RRT^X^ but struggled to find initial solutions on small planning budgets. The ASAO properties of RRT\* ensure that when it is given sufficient planning time it converges towards the optimal solution. This consistency between intermediate solutions ensures that RRT\* only exits the sensed area when necessary but the required planning budget proved to be large. RRT\* failed more than half the time on the Double Enclosure problems and all sets of Random Rectangles due to its slow initial solution time.

EIT\* is able to find fast and near-optimal intermediate solutions since it is designed to quickly find an initial solution and then converge toward the optimal path. EIT\* found shorter median solution paths than all other tested planning algorithms at all planning budgets. EIT\* had the highest success rates on all sets of Random Rectangles problems at every planning budget and was the only planner to solve more than 50% of the problems on all experiments.

The real-world experiments demonstrate the applicability of the independent ASAO replanning strategy to other fast ASAO planning algorithms, dynamic obstacles, and real-world robotics problems. Suitably fast ASAO planners are able to replan each time obstacle changes are detected and achieve real-time dynamic planning, as demonstrated in the Franka arm experiment.

The simplicity of implementing the independent ASAO approach is also worth noting. Replanning from scratch simplifies many modeling assumptions in dynamic environments by not relying on a prior or attempting to reuse information between queries. An incremental planner that tries to reuse information from previous planning efforts would incur a performance overhead on long-horizon planning problems like the Franka arm experiment and would require careful tuning or sophisticated methods to control its solution-tree density. Many existing dynamic planners would require prior information about their obstacles like a maximum velocity or probabilities of different obstacle trajectories to navigate in the experiment. The only parameter tuning needed to run the independent ASAO replanning strategy is to use the largest budget that can be afforded and no problem-specific information or prior data is required, although it can be incorporated into the obstacle map if available.

## Conclusion and Future Work

Traditional reactive planning literature focuses on trying to reuse information from previous queries in order to speed up planning time. This is often done by attempting to repair old plans when new obstacle information becomes available in order to maintain their path validity, consistency, and/or optimality. For this to be computationally tractable, many current algorithms assume that there is an efficient method to identify the locations of obstacle changes and propagate this information throughout their existing plans.

This paper shows that independent calls to ASAO planners can instead outperform these planners on incremental planning problems. We demonstrate that a suitably fast ASAO planner, such as EIT\*, outperforms information-reuse algorithms, such as RRT^X^, even when access to obstacle changes is free. It also shows that EIT\* finds lower-cost solutions more quickly and with a higher success rate than independent runs of other ASAO algorithms, such as RRT\*, and fast probabilistically complete algorithms like RRT-Connect.

The results of this paper demonstrate the capability of ASAO planners to replan in simulation as quickly as 50ms and the applicability of this approach to a real-world robotic arm problem. This capability is exciting as it shows the ability to find near-optimal global solutions at close to the speed of control-level systems. In the future we would like to investigate using the independent ASAO approach on robots with obstacle predictions to find better solutions in environments with dynamic obstacles and on robots with kinodynamic or other constraints.
