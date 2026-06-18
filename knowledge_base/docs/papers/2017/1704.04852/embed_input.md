Downwash-Aware Trajectory Planning for Large Quadrotor Teams

Topics include Robotics, Aerial robotics, Safety, Graphs, Planning.

We describe a method for formation-change trajectory planning for large quadrotor teams in obstacle-rich environments. Our method decomposes the planning problem into two stages: a discrete planner operating on a graph representation of the workspace, and a continuous refinement that converts the non-smooth graph plan into a set of C^k-continuous trajectories, locally optimizing an integral-squared-derivative cost. We account for the downwash effect, allowing safe flight in dense formations. We demonstrate the computational efficiency in simulation with up to 200 robots and the physical plausibility with an experiment with 32 nano-quadrotors. Our approach can compute safe and smooth trajectories for hundreds of quadrotors in dense environments with obstacles in a few minutes.

## INTRODUCTION

Trajectory planning is a fundamental problem in multi-robot systems. Given a set of robots with known initial locations and a set of goal locations, the task is to find a one-to-one goal assignment and a set of continuous functions that move each robot from its start position to its goal, while avoiding collisions and respecting dynamic limits. Trajectory planning is a core subproblem of various applications including search-and-rescue, inspection, and delivery. In this work we address the *unlabeled* case; in the *labeled* case the goal assignment is given.

A large body of work has addressed this problem with varied discrete and continuous formulations. However, no existing solution simultaneously satisfies the goals of completeness, physical plausibility, optimality in time or energy usage, and good computational performance. In this work, we present a method that attempts to balance these goals.

Our approach can compute safe and arbitrarily smooth trajectories for hundreds of quadrotors in dense environments with obstacles in a few minutes. The trajectory plan outputs have been tested and executed safely in numerous trials on a team of 32 quadrotors.

In future work, we plan to generalize our method to support arbitrary environments and start and goal locations that are not limited to an underlying grid, by exploring different discrete planning algorithms. We also plan to investigate performance improvements in both discrete and continuous stages.

where $E = {\operatorname{\mathbf{d}\mathbf{i}\mathbf{a}\mathbf{g}}{(r_{x},r_{y},r_{z})}}$ is the ellipsoid matrix. Robot-obstacle separating hyperplanes are computed similarly, except we use a different ellipsoid $E_{obs}$ for obstacles to model the fact that downwash is only important for robot-robot interactions, and we shift the hyperplanes such that they touch the obstacles.

We require that the discrete planner supplies a plan that satisfies the ellipsoid collision-avoidance constraint for all possible identical velocity profiles. We also require all robots to share the same sequence of waypoint times $t_{0}\ldotst_{K}$.

TABLE I: Runtime for different examples and safety distances, see Section VI-B. All times are given in seconds.

Our method uses a graph-based planner to compute a solution for a discretized version of the problem, and then refines this solution into smooth...
