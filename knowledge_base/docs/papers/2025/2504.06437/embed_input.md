DBaS-Log-MPPI: Efficient and Safe Trajectory Optimization via Barrier States

Topics include Model predictive path integral control, Trajectory optimization, Safety, Barrier states, Constraint satisfaction.

Integrates logarithmic barrier states (DBaS) into the dynamics, providing smooth cost shaping that discourages safety constraint violations.

Optimizing trajectory costs for nonlinear control systems remains a significant challenge. Model Predictive Control (MPC), particularly sampling-based approaches such as the Model Predictive Path Integral (MPPI) method, has recently demonstrated considerable success by leveraging parallel computing to efficiently evaluate numerous trajectories. However, MPPI often struggles to balance safe navigation in constrained environments with effective exploration in open spaces, leading to infeasibility in cluttered conditions. To address these limitations, we propose DBaS-Log-MPPI, a novel algorithm that integrates Discrete Barrier States (DBaS) to ensure safety while enabling adaptive exploration with enhanced feasibility. Our method is efficiently validated through three simulation missions and one real-world experiment, involving a 2D quadrotor and a ground vehicle navigating through cluttered obstacles. We demonstrate that our algorithm surpasses both Vanilla MPPI and Log-MPPI, achieving higher success rates, lower tracking errors, and a conservative average speed.

## INTRODUCTION

With the increasing focus on robotic control, designing safe and reliable control methods for autonomous robots operating in unknown environments---while maintaining real-time performance---remains a significant challenge \[\]. Successful navigation requires robots to accurately detect both static and dynamic obstacles, including convex and non-convex shapes, using appropriate sensors. Moreover, robots must dynamically re-plan their trajectories to avoid local optima, prevent collisions, and reach their target locations efficiently....

Model predictive control (MPC) \[\], a well-established control framework, offers robust navigation capabilities by handling obstacles under both hard and soft system constraints. MPC employs a receding horizon strategy to generate a sequence of control inputs over a predefined prediction window. Only the first input is executed, while the remaining inputs serve as warm starts for subsequent optimization steps. MPC methods can be broadly categorized into gradient-based and sampling-based approaches....

This paper presents a novel DBaS-Log-MPPI controller that adaptively explores the action space through effective sampling within barrier states embedded in dynamics ensuring safety guarantees. The integration of the barrier state enables the proposed algorithm with continuous collision risk assessment. Furthermore, the adaptive exploration mechanism enhances sampling diversity and coverage, particularly in proximity to obstacles....

Future work will focus on refining the controller by developing more comprehensive safety barrier formulations and extending its application to complex control scenarios, such as multi-agent planning. Additionally, we plan to implement the algorithm on advanced robotic platforms, including 3D quadrotors and quadruped robots, which present broader action spaces and challenges in sampling effective trajectories.

### IV-B Adaptive trajectory sampling

Figure 2: Proposed DBaS-Log-MPPI control scheme.

Additionally, the algorithm is implemented on the "Antelope" ground vehicle in a real-world scenario. The experiments demonstrate the algorithm's effectiveness in performing safe trajectory optimization in challenging navigation tasks.

Figure 1: Demonstration of trajectory sampling: ours (left) vs. vanilla MPPI (right).
