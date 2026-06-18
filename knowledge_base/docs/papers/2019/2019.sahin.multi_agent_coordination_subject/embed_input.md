Multi-Agent Coordination Subject to Counting Constraints: A Hierarchical Approach

Topics include Multi-agent systems, Multi-agent pathfinding, Temporal logic, Hierarchical planning, Reachability analysis, Formal methods, Asynchronous coordination.

Proposes a two-level coordination method that first plans over counting-logic constraints and then solves lower-level reachability problems for the agents. The hierarchy makes the method scale better and gives infeasibility feedback from motion planning back to the symbolic planning layer.

This paper considers the problem of generating multi-agent trajectories to satisfy properties given in counting temporal logic. A hierarchical solution approach is proposed where a coarse plan that satisfies the logic constraints is computed first at the higher-level, followed by a lower-level task of solving a sequence of multi-agent reachability problems. Collision avoidance and potential asynchronous executions are also dealt with at the lower-level. When lower-level planning problems are found to be infeasible, these infeasibility certificates are incorporated into the higher-level problem to re-generate plans. The results are demonstrated with several examples that show how the proposed approach scales with respect to different parameters.
