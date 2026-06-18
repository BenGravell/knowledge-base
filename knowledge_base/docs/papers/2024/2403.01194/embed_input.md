A Comparative Study of Rapidly-exploring Random Tree Algorithms Applied to Ship Trajectory Planning and Behavior Generation

Topics include Rapidly-exploring random tree, Comparison study, Ship trajectory planning, Scenario generation, Electronic navigational charts, R-trees, Constrained Delaunay triangulation.

Compares variations of RRT in an application domain for marine ship navigation. The dynamic model is basically the same as for car-like vehicles.

Rapidly Exploring Random Tree (RRT) algorithms, notably used for nonholonomic vehicle navigation in complex environments, are often not thoroughly evaluated for their specific challenges. This paper presents a first such comparison study of the variants Potential-Quick RRT* (PQ-RRT*), Informed RRT* (IRRT*), RRT*, and RRT, in maritime single-query nonholonomic motion planning. Additionally, the practicalities of using these algorithms in maritime environments are discussed and outlined. We also contend that these algorithms are beneficial not only for trajectory planning in Collision Avoidance Systems (CAS) but also for CAS verification when used as vessel behavior generators. Optimal RRT variants tend to produce more distance-optimal paths but require more computational time due to complex tree wiring and nearest neighbor searches. Our findings, supported by Welch`s t-test at a significance level of Alpha = 0.05, indicate that PQ-RRT* slightly outperform IRRT* and RRT* in achieving shorter trajectory length but at the expense of higher tuning complexity and longer run-times.

## Previous Work

Collision-free trajectory planning is a well-studied topic, and we refer the reader to review studies as in (Vagale et al. Huang et al., ) for extensive summaries on the various methods proposed previously, and to for an extensive review on RRT planning dated 2016. This brief review focuses on core versions of RRT having been proposed previously, in addition to ship scenario generation and falsification, respectively. The RRT algorithms are single-query, and thus they are tailored for planning trajectories or paths from a start position to a specified goal.

## Rapidly-exploring Random Trees

The first baseline RRT planner was introduced by LaValle et al., with the core concept of incrementally sampling configurations or nodes in the obstacle-free space, and wiring of the tree towards these configurations if the trajectory segments in between are collision-free. However, baseline RRT is only probabilistically complete in the sense that the probability of the planner finding a solution approaches $1$ as the number of iterations approaches infinity.

## Discussion

Gauging the results on planning, we see that the RRT-based planners are viable for use in problems of adequate size, i.e. less than ${1\ {km}} \times {1\ {km}}$ in map size. In these cases, the planners can find and optimize the best solution in adequate time. However, for larger maps, the planners struggle. This is attributed to the increased number of samples and iterations required in order to find and refine a solution. Although the planners find initial solutions fast, they have a hard time optimizing the solutions when considering larger map sizes and complex environments.

We note that IRRT\*, although providing linear algorithm convergence properties for obstacle-free environments, struggles with both planning cases and especially the larger one. This is due to the large volume occupied by obstacles in the configuration space, leading to a significant rejection rate in the informed heuristical sampling. Thus, for IRRT\* to be of practical usage, it requires an improvement. This can be an update and creation of a new CDT for the safe sea domain inside the informed sampling domain, each time a new solution is found.
