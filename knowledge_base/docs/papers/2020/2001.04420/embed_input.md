FASTER: Fast and Safe Trajectory Planner for Navigation in Unknown Environments

Planning high-speed trajectories for UAVs in unknown environments requires algorithmic techniques that enable fast reaction times to guarantee safety as more information about the environment becomes available. The standard approaches that ensure safety by enforcing a "stop" condition in the free-known space can severely limit the speed of the vehicle, especially in situations where much of the world is unknown. Moreover, the ad-hoc time and interval allocation scheme usually imposed on the trajectory also leads to conservative and slower trajectories. This work proposes FASTER (Fast and Safe Trajectory Planner) to ensure safety without sacrificing speed. FASTER obtains high-speed trajectories by enabling the local planner to optimize in both the free-known and unknown spaces. Safety is ensured by always having a safe back-up trajectory in the free-known space. The MIQP formulation proposed also allows the solver to choose the trajectory interval allocation. FASTER is tested extensively in simulation and in real hardware, showing flights in unknown cluttered environments with velocities up to 7.8m/s, and experiments at the maximum speed of a skid-steer ground robot (2m/s).

## Introduction

Despite its numerous applications, high-speed UAV navigation through unknown environments is still an open problem. The desired high speeds together with partial observability of the environment and limits on payload weight make this task especially challenging for aerial robots. Safe operation, in addition to flying fast, is also critical but difficult to guarantee since the vehicle must repeatedly generate collision-free, dynamically feasible trajectories in real-time with limited sensing. Similar to the model predictive control literature, safety is guaranteed by ensuring a feasible solution exists indefinitely.

Figure 1: Safety and Speed tradeoff. 𝒪 is the occupied-known space, and 𝒰 is the unknown space. A and E are, respectively, the start and goal locations of the local plan.

Our algorithm has also some limitations: In environments where the planning horizon is not very large (as in all the experiments shown in this article), $2 - 4$ polyhedra usually suffice, and our algorithm maintains computational tractability. However, for large known worlds (for example if a map of the environment already exists beforehand), a long planning horizon may require more than 4 polyhedra, which, as shown in Fig. 17, will increase the computation time....

Finally, another promising future work is the reduction of the computation times of the time allocation approaches. Experiments in Sec. IV-B use a generic nonconvex solver to optimize the time allocation, which may be inefficient in some situations. Exploitation of the structure of the time allocation problem and/or the use of hierarchical optimization could help to reduce the associated computation times. This could potentially avoid the use of binary variables needed for the interval allocation, or allow the optimization of *both* the interval and the time allocation in the trajectory planning problem.

### Assumption 1

Figure 7: Dynamic adaptation of the factor used to compute the heuristic of the time allocated per interval (d t): For iteration k, the range of factors used is taken around the factor that worked in the iteration k − 1. As f = 1 is the lower bound that makes the problem feasible, only factors f ≥ 1 are tried.

We evaluate the performance of the proposed algorithm in different simulated scenarios....
