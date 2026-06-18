FDSPC: Fast and Direct Smooth Path Planning via Continuous Curvature Integration

Topics include Path planning, Smooth paths, Curvature continuity, Heuristic.

Proposes FDSPC, a global path planner that directly produces G2 smooth paths via continuous curvature integration. It essentially uses a goal-directed heuristic for selecting (otherwise unspecified) yaw angles at sampled positions, rather than attempting to connect (x, y, yaw) boundary poses directly.

In recent decades, global path planning of robot has seen significant advancements. Both heuristic search-based methods and probability sampling-based methods have shown capabilities to find feasible solutions in complex scenarios. However, mainstream global path planning algorithms often produce paths with bends, requiring additional smoothing post-processing. In this work, we propose a fast and direct path planning method based on continuous curvature integration. This method ensures path feasibility while directly generating global smooth paths with constant velocity, thus eliminating the need for post-path-smoothing. Furthermore, we compare the proposed method with existing approaches in terms of solution time, path length, memory usage, and smoothness under multiple scenarios. The proposed method is vastly superior to the average performance of state-of-the-art (SOTA) methods, especially in terms of the self-defined S_2 smoothness (mean angle of steering). These results demonstrate the effectiveness and superiority of our approach in several representative environments.

## Introduction

Robot motion planning has undergone significant development in recent years, and played crucial roles in various fields, such as autonomous vehicles, robot arms and unmanned aerial vehicles. However, existing commonly used path planning methods, such as search-based algorithms A\*, Dijkstra, sampling-based algorithms Rapidly-exploring Random Trees (RRT), RRT\*, extended-RRT, RRT-Connect and swarm intelligence-based algorithms Ant Colony Optimization (ACO), all yield non-continuous, zigzag global paths.

In this letter, a fast and direct motion planning method based on continuous curvature integration (FDSPC) is proposed for mobile robot trajectory tracking on a given map, as shown in Fig.. The algorithm iteratively explores collision-free path segments satisfying $G^{2}$ smoothness (curvature continuity). If trapped in a local solution, it automatically backtracks to the previous optimal state to ensure feasibility. FDSPC demonstrates superior performances by comparing various indicators, including solution time, smoothness, in multiple scenarios. The contributions of this letter are as follows,

A fast motion planning method based on continuous curvature integration is proposed, which can generate global paths that satisfies $G^{2}$ smoothness, avoiding the re-collision checking and smoothing.

A variant of the direct positioning binary tree combined with an ordered dictionary is introduced to facilitate heuristic search of the path rapidly and ensuring both the feasibility and efficiency of the algorithm.

## CONCLUSION

In this letter, we introduced a novel motion planning algorithm FDSPC, based on continuous curvature integration. It explores feasible paths by continuous changes in curvature angles, offering high solution speed, efficient memory usage, shorter path lengths, and exceptional path smoothness. In five typical scenarios, FDSPC demonstrated superior performance, and successfully implemented in obstacle-crossing trajectories on our self-designed wheel-legged robot in a $2.5$-D terrain environment. However, FDSPC has some drawbacks: it's sensitive to parameter settings, may fail to find a path if parameters are unreasonable.

In the future, we will improve the FDSPC, reduce adjustable parameters and enhance its completeness, and aim to explore its potential as an effective initial value for mobile robot trajectory optimization.
