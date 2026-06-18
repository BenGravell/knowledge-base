AORRTC: Almost-Surely Asymptotically Optimal Planning with RRT-Connect

Topics include Motion planning, Sampling-based planning, Asymptotic optimality, Anytime planning, Bidirectional search, Rapidly-exploring random tree connect, Single-instruction multiple-data, High-dimensional planning.

Applies the AO-x meta-algorithm to RRT-Connect, inheriting its fast initial solution times while adding almost-sure asymptotic optimality. With SIMD acceleration, AORRTC solves difficult high-DoF problems (Panda, Fetch robots) in milliseconds where other almost-surely asymptotically optimal planners failed to find solutions even with seconds of planning time.

Finding high-quality solutions quickly is an important objective in motion planning. This is especially true for high-degree-of-freedom robots. Satisficing planners have traditionally found feasible solutions quickly but provide no guarantees on their optimality, while almost-surely asymptotically optimal (a.s.a.o.) planners have probabilistic guarantees on their convergence towards an optimal solution but are more computationally expensive. This paper uses the AO-x meta-algorithm to extend the satisficing RRT-Connect planner to optimal planning. The resulting Asymptotically Optimal RRT-Connect (AORRTC) finds initial solutions in similar times as RRT-Connect and uses any additional planning time to converge towards the optimal solution in an anytime manner. It is proven to be probabilistically complete and a.s.a.o. AORRTC was tested with the Panda (7 DoF) and Fetch (8 DoF) robotic arms on the MotionBenchMaker dataset. These experiments show that AORRTC finds initial solutions as fast as RRT-Connect and faster than the tested state-of-the-art a.s.a.o. algorithms while converging to better solutions faster....

## Introduction

Motion planning seeks to quickly find high-quality solutions to a given problem, especially when planning for high degree-of-freedom (DoF) robots or in real time. Motion planning algorithms search a discrete approximation of the robot's continuous *configuration space* (i.e., search space).

Motion planning algorithms approximate the search space in different ways. Graph-based planners, such as Dijkstra's algorithm and A\*, require *a priori* discretization of the search space. High-resolution approximations generally contain high quality solutions but are computationally expensive to search, while low-resolution approximations are cheaper to search but may only contain a low quality solution, or no solution at all....

Figure 4: Near-optimality results for 5 trials of all planners on the 7 DoF Panda for a single problem from the cage, (a), bookshelf small, (b), and table pick, (c), environments from the MotionBenchMaker dataset (Sec.˜IV). The top plots show the percentage of runs that found a solution within a suboptimality factor, ϵ, of the empirically determined optimum, $\hat{c^{\ast}}$, with Clopper-Pearson 99% confidence intervals. The bottom plots show the median time to find a solution within a suboptimality factor, ϵ, of the empirically determined optimum, $\hat{c^{\ast}}$, with nonparametric 99% confidence intervals.

OMPL and VAMP implementations of AORRTC were evaluated against OMPL implementations of RRT-Connect, RRT*, BIT*, and AIT* and VAMP implementations of RRT-Connect, RRT*, BIT*, and FCIT*. We also show results for a VAMP implementation of Anytime RRT-Connects (Sec.˜III-E) in Fig.˜3. The reported solution costs and times for AORRTC include the computational costs of randomized shortcutting and B-spline smoothing....

Bidirectional sampling-based planners, such as RRT-Connect, explore the search space by extending a tree from both the start and goal vertices and trying to connect these trees. RRT-Connect finds initial solutions significantly faster than other planning algorithms on most real-world manipulation problems but offers no guarantees on solution quality and often finds low quality solutions.

Anytime a.s.a.o. planners use additional planning time to improve their approximation of the search space and find better solutions....
