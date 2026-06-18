Baidu Apollo EM Motion Planner

Topics include Autonomous driving, Motion planning, Trajectory optimization, Quadratic programming, Frenet frame.

Describes the production motion-planning stack used in Baidu Apollo, combining lane-level strategy, Frenet-frame path and speed optimization, dynamic programming, and spline-based quadratic programming. It is valuable as a rare industrial account of a deployed autonomous-driving planner.

In this manuscript, we introduce a real-time motion planning system based on the Baidu Apollo (open source) autonomous driving platform. The developed system aims to address the industrial level-4 motion planning problem while considering safety, comfort and scalability. The system covers multilane and single-lane autonomous driving in a hierarchical manner: The top layer of the system is a multilane strategy that handles lane-change scenarios by comparing lane-level trajectories computed in parallel. Inside the lane-level trajectory generator, it iteratively solves path and speed optimization based on a Frenet frame. For path and speed optimization, a combination of dynamic programming and spline-based quadratic programming is proposed to construct a scalable and easy-to-tune framework to handle traffic rules, obstacle decisions and smoothness simultaneously. The planner is scalable to both highway and lower-speed city driving scenarios. We also demonstrate the algorithm through scenario illustrations and on-road test results.

## Introduction

Autonomous driving research began in the 1980s and has significantly grown over the past ten years. Autonomous driving aims to reduce road fatalities, increase traffic efficiency and provide convenient travel. However, autonomous driving is a challenging task that requires accurately sensing the environment, a deep understanding of vehicle intentions and safe driving under different scenarios. To address these difficulties, we constructed an Apollo open source autonomous driving platform. The flexible modularized architecture of the developed platform supports fully autonomous driving deployment

In the figure, the HD map module provides a high-definition map that can be accessed by every on-line module. Perception and localization modules provide the necessary dynamic environment information, which can be further used to predict future environment status in the prediction module. The motion planning module considers all information to generate a safe and smooth trajectory to feed into the vehicle control module.

Fig. 1 shows the architecture of the Apollo online modules.

## Conclusion

EM planner is a light-decision-based algorithm. Compared with other heavy-decision-based algorithms, the advantage of EM planner is its ability to perform under complicated scenarios with multiple obstacles. When heavy-decision-based methods attempt to predetermine how to act with each obstacle, the difficulties are significant: It is difficult to understand and predict how obstacles interact with each other and the master vehicle; thus, their following movement is hard to describe and therefore hard to be considered by any rules.

One critical issue in autonomous driving vehicles is the challenge of safety vs. passability. A strict rule increases the safety of the vehicle but lowers the passability, and vice versa. Take the lane-changing case as an example; one could easily pause the lane-changing process if there is a vehicle behind with simple rules. This could grant safety but considerably decreases the passability. EM planner described in this manuscript is also designed to solve the inconsistency of potential decisions and planning, while it also improves the passability of autonomous driving vehicles.
