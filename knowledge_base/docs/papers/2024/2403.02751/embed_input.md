Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps

Topics include Robotics, Safety, Robustness, Pose estimation, Real-time systems, Online algorithms, Planning, Splat-Nav.

We present Splat-Nav, a real-time robot navigation pipeline for Gaussian Splatting (GSplat) scenes, a powerful new 3D scene representation. Splat-Nav consists of two components: 1) Splat-Plan, a safe planning module, and 2) Splat-Loc, a robust vision-based pose estimation module. Splat-Plan builds a safe-by-construction polytope corridor through the map based on mathematically rigorous collision constraints and then constructs a Bézier curve trajectory through this corridor. Splat-Loc provides real-time recursive state estimates given only an RGB feed from an on-board camera, leveraging the point-cloud representation inherent in GSplat scenes. Working together, these modules give robots the ability to recursively re-plan smooth and safe trajectories to goal locations. Goals can be specified with position coordinates, or with language commands by using a semantic GSplat. We demonstrate improved safety compared to point cloud-based methods in extensive simulation experiments. In a total of 126 hardware flights, we demonstrate equivalent safety and speed compared to motion capture and visual odometry, but without a manual frame alignment required by those methods.

## Introduction

Autonomous robotic operation requires robots to localize themselves within an envrionment, plan safe paths to reach a desired goal location, and have closed-loop trajectory-tracking. Traditionally, the fundamental problems of planning and localization have been performed in maps represented as occupancy grids, triangular meshes, point clouds, and Signed Distance Fields (SDFs), all of which provide well-defined geometry.

However, these explicit scene representations are generally constructed at limited resolutions (to enable real-time operation), leaving out potentially-important scene details that could be valuable in planning and localization problems.

In this paper, we introduce *Splat-Nav*, a pipeline for drone navigation in GSplat maps with a *monocular* camera. Splat-Nav comprises a lightweight pose estimation module, Splat-Loc, coupled with a planning module, Splat-Plan, to enable safe navigation from RGB-only (monocular) camera observations, as illustrated in Figure 1. Given an incoming RGB frame, Splat-Loc performs Perspective-n-Point (PnP)-based localization, leveraging the GSplat map to estimate the RGB and depth values rendered at candidate poses, which are then used to estimate the drone's pose.

In extensive simulations we compare Splat-Plan and Splat-Loc with baseline alternatives for planning and localization, respectively. We show Splat-Plan is always safe with respect to the full collision geometry, while four variants of a point-cloud based planner sometimes lead to collisions, or fail to find trajectories. Splat plan achieves similar or better solutions in terms of path length compared to point cloud-based planner in all cases, with similar computation time.

## Conclusion

We introduce an efficient navigation pipeline termed *Splat-Nav* for robots operating in GSplat environments. Splat-Nav consists of a guaranteed-safe planning module *Splat-Plan*, which allows for real-time planning ($>$ 2 Hz) by leveraging the ellipsoidal representation inherent in GSplats for efficient collision-checking and safe corridor generation, facilitating real-time online replanning. Splat-Plan demonstrates superior performance in terms of conservativeness, safety, success rate and comparable computation times compared to point-cloud and NeRF methods on the same scene.
