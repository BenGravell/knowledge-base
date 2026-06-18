NanoMap: Fast, Uncertainty-Aware Proximity Queries with Lazy Search over Local 3D Data

Topics include Motion planning, Robotics, Aerial robotics, Safety, Robustness, Uncertainty, State estimation, Planning, NanoMap.

We would like robots to be able to safely navigate at high speed, efficiently use local 3D information, and robustly plan motions that consider pose uncertainty of measurements in a local map structure. This is hard to do with previously existing mapping approaches, like occupancy grids, that are focused on incrementally fusing 3D data into a common world frame. In particular, both their fragile sensitivity to state estimation errors and computational cost can be limiting. We develop an alternative framework, NanoMap, which alleviates the need for global map fusion and enables a motion planner to efficiently query pose-uncertainty-aware local 3D geometric information. The key idea of NanoMap is to store a history of noisy relative pose transforms and search over a corresponding set of depth sensor measurements for the minimum-uncertainty view of a queried point in space.

## INTRODUCTION

Robust, fast motion near obstacles is an open problem that is central in robotics, with applications spanning across manipulation, autonomous cars, and UAV navigation in unknown environments. Although many approaches exist for planning obstacle-free motions, mapping errors due to significant state estimation uncertainty can degrade their performance. Accordingly, a notable trend in the state of the art has been to develop memoryless approaches to obstacle avoidance that use only the current depth sensor measurement. These approaches are less prone to state estimation errors, but fail to capture all available information.

Towards this goal, a primary motivation of this work was to be able to use pose uncertainty to reason about a local history of depth information. NanoMap is an algorithm and data structure that enables uncertainty-aware proximity queries for planning. While traditional mapping approaches rely on fusing a history of depth information into a discretized world frame, we propose an alternative: perform no discretization, and no fusing. Instead, the process for querying local 3D data is a search over views.

This paper presents the design of NanoMap and our experiments in quantifying the benefits of its novel properties. We believe this work strongly demonstrates that more deeply integrating motion planning and perception can improve a system's robustness and computational efficiency.

## CONCLUSION

We have described, implemented, analyzed, and validated NanoMap. NanoMap provides novel features for using local 3D data with pose uncertainty. Specifically, it (a) models relative positional uncertainty into its response to local 3D data queries, (b) uses the minimum-uncertainty view to respond to these queries, and (c) can trivially incorporate updated pose information two to four orders of magnitude faster than the benchmarked alternatives.
