Downwash-Aware Trajectory Planning for Large Quadrotor Teams

Topics include Robotics, Aerial robotics, Safety, Graphs, Planning.

We describe a method for formation-change trajectory planning for large quadrotor teams in obstacle-rich environments. Our method decomposes the planning problem into two stages: a discrete planner operating on a graph representation of the workspace, and a continuous refinement that converts the non-smooth graph plan into a set of C^k-continuous trajectories, locally optimizing an integral-squared-derivative cost. We account for the downwash effect, allowing safe flight in dense formations. We demonstrate the computational efficiency in simulation with up to 200 robots and the physical plausibility with an experiment with 32 nano-quadrotors. Our approach can compute safe and smooth trajectories for hundreds of quadrotors in dense environments with obstacles in a few minutes.

## INTRODUCTION

Trajectory planning is a fundamental problem in multi-robot systems. Given a set of robots with known initial locations and a set of goal locations, the task is to find a one-to-one goal assignment and a set of continuous functions that move each robot from its start position to its goal, while avoiding collisions and respecting dynamic limits. Trajectory planning is a core subproblem of various applications including search-and-rescue, inspection, and delivery. In this work we address the *unlabeled* case; in the *labeled* case the goal assignment is given.

A large body of work has addressed this problem with varied discrete and continuous formulations. However, no existing solution simultaneously satisfies the goals of completeness, physical plausibility, optimality in time or energy usage, and good computational performance. In this work, we present a method that attempts to balance these goals.

Our method uses a graph-based planner to compute a solution for a discretized version of the problem, and then refines this solution into smooth trajectories in a separate, decoupled optimization stage. We directly take the downwash effect of quadrotors into account, preserving safety during dense formation flights. Furthermore, our method is complete with respect to the resolution of the discretization, and locally optimal with respect to an energy-minimizing integral-squared-derivative objective function. We also present an anytime iterative refinement scheme that improves the trajectories within a given computational budget.

## CONCLUSION

We presented a trajectory planning method for large quadrotor teams. Our approach is downwash-aware and thus creates plans where robots can safely fly in close proximity to each other. We plan trajectories using two independent stages, a discrete stage and a continuous stage. The presented discrete planner finds a goal assignment for each robot and a path such that the makespan is minimized while avoiding collisions and respecting downwash constraints. The continuous stage decouples each robot's trajectory planning, allowing easy parallelization and improving performance for large teams.
