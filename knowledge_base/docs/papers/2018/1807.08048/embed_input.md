Baidu Apollo EM Motion Planner

Topics include Autonomous driving, Motion planning, Trajectory optimization, Quadratic programming, Frenet frame.

Describes the production motion-planning stack used in Baidu Apollo, combining lane-level strategy, Frenet-frame path and speed optimization, dynamic programming, and spline-based quadratic programming. It is valuable as a rare industrial account of a deployed autonomous-driving planner.

In this manuscript, we introduce a real-time motion planning system based on the Baidu Apollo (open source) autonomous driving platform. The developed system aims to address the industrial level-4 motion planning problem while considering safety, comfort and scalability. The system covers multilane and single-lane autonomous driving in a hierarchical manner: The top layer of the system is a multilane strategy that handles lane-change scenarios by comparing lane-level trajectories computed in parallel. Inside the lane-level trajectory generator, it iteratively solves path and speed optimization based on a Frenet frame. For path and speed optimization, a combination of dynamic programming and spline-based quadratic programming is proposed to construct a scalable and easy-to-tune framework to handle traffic rules, obstacle decisions and smoothness simultaneously. The planner is scalable to both highway and lower-speed city driving scenarios. We also demonstrate the algorithm through scenario illustrations and on-road test results....

## Introduction

Autonomous driving research began in the 1980s and has significantly grown over the past ten years. Autonomous driving aims to reduce road fatalities, increase traffic efficiency and provide convenient travel. However, autonomous driving is a challenging task that requires accurately sensing the environment, a deep understanding of vehicle intentions and safe driving under different scenarios. To address these difficulties, we constructed an Apollo open source autonomous driving platform. The flexible modularized architecture of the developed platform supports fully autonomous driving deployment

In the figure, the HD map module provides a high-definition map that can be accessed by every on-line module. Perception and localization modules provide the necessary dynamic environment information, which can be further used to predict future environment status in the prediction module. The motion planning module considers all information to generate a safe and smooth trajectory to feed into the vehicle control module.

As of May 16th, 2018, the effectivity of this system has been proven under 3,380 hours and approximately 68,000 kilometers (42,253 miles) of intense closed-loop testing in Baidu Apollo autonomous driving vehicles. The algorithm has been evaluated under different countries, traffic laws and conditions, including extremely crowded urban scenarios such as Beijing, China, and Sunnyvale, CA, USA. The algorithm has also been evaluated and tested in more than one-hundred-thousand hours and a million kilometers (0.621 million miles) simulation test.

The algorithm described in this manuscript is available at

where $g{(s)}$ is the DP path result. $f^{\prime}{(s)}$, $f^{\operatorname{\prime\prime}}{(s)}$ and $f^{\operatorname{\prime\prime\prime}}{(s)}$ are related to the heading, curvature and derivative of curvature. The objective function describes the balance between nudging obstacles and smoothness.

The M-step path optimizer optimizes the path profile in the Frenet frame. This is represented as finding an optimal function of lateral coordinate $l = {f{(s)}}$ w.r.t. station coordinate in nonconvex SL space (e.g., nudging from left and right might be two local optima). Thus, the path optimizer includes two steps: dynamic-programming-based path decision and spline-based path planning....
