RAPTOR: Robust and Perception-aware Trajectory Replanning for Quadrotor Fast Flight

Recent advances in trajectory replanning have enabled quadrotor to navigate autonomously in unknown environments. However, high-speed navigation still remains a significant challenge. Given very limited time, existing methods have no strong guarantee on the feasibility or quality of the solutions. Moreover, most methods do not consider environment perception, which is the key bottleneck to fast flight. In this paper, we present RAPTOR, a robust and perception-aware replanning framework to support fast and safe flight. A path-guided optimization (PGO) approach that incorporates multiple topological paths is devised, to ensure finding feasible and high-quality trajectories in very limited time. We also introduce a perception-aware planning strategy to actively observe and avoid unknown obstacles. A risk-aware trajectory refinement ensures that unknown obstacles which may endanger the quadrotor can be observed earlier and avoid in time. The motion of yaw angle is planned to actively explore the surrounding space that is relevant for safe navigation. The proposed methods are tested extensively. We will release our implementation as an open-source package for the community.

## Introduction

In recent years, progresses on different aspects of unmanned aerial vehicles (UAVs), especially quadrotor autonomy have been achieved and promote autonomous navigation. Nonetheless, high-speed flight in unknown and highly cluttered environments still remains one of the biggest challenges toward full autonomy. To achieve fast flight, trajectory replanning is of vital importance to cope with previously unknown obstacles, guaranteeing smooth and safe navigation.

Figure 1: An example of planning without perception awareness. The quadrotor flies near the wall, where it has poor visibility to the space behind the corner. In consequence, an obstacle is not revealed until the quadrotor gets very close.

## Conclusions

In this paper, we propose a robust and perception-aware replanning method for high-speed quadrotor autonomous navigation. The path-guided optimization and topological path searching are devised to escape from local minima and explore the solution space more thoroughly, through which higher robustness and optimality guarantee are obtained. The robust planner is further enhanced by the perception-aware strategy, which takes special caution about regions that may be dangerous to the quadrotor. The yaw angle of the quadrotor is also planned to actively explore the environments, especially areas that are relevant to the future flight....

which means that if at $\mathbf{p}_{c}$ the quadrotor sees an obstacle, it can decelerate to a stop before colliding with the obstacle right behind $\mathbf{p}_{f}$. $R_{q}$ compensates the quadrotor size and disturbance. If it is not true, extra constraints are added to meet this criteria.

Alg.1 is used to construct a UVD roadmap $\mathcal{G}$ capturing an abundant set of paths from different UVD classes. Unlike standard PRM containing many redundant loops, our method generates a more compact roadmap where each UVD class contains just one or a few paths (displayed in Fig.8(a)-8(c)).

Figure 16: A comparison of the trajectories in scene 1 replanned with (a) optimistic assumption and (b) risk-aware refinement. Trajectories already executed and not executed yet are showed in opaque red and transparent red respectively. (a) Along the trajectory visibility toward the unknown region behind the observed obstacle is poor....
