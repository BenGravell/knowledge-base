Splat-Nav: Safe Real-Time Robot Navigation in Gaussian Splatting Maps

Topics include Robotics, Safety, Robustness, Pose estimation, Real-time systems, Online algorithms, Planning, Splat-Nav.

We present Splat-Nav, a real-time robot navigation pipeline for Gaussian Splatting (GSplat) scenes, a powerful new 3D scene representation. Splat-Nav consists of two components: 1) Splat-Plan, a safe planning module, and 2) Splat-Loc, a robust vision-based pose estimation module. Splat-Plan builds a safe-by-construction polytope corridor through the map based on mathematically rigorous collision constraints and then constructs a Bézier curve trajectory through this corridor. Splat-Loc provides real-time recursive state estimates given only an RGB feed from an on-board camera, leveraging the point-cloud representation inherent in GSplat scenes. Working together, these modules give robots the ability to recursively re-plan smooth and safe trajectories to goal locations. Goals can be specified with position coordinates, or with language commands by using a semantic GSplat. We demonstrate improved safety compared to point cloud-based methods in extensive simulation experiments. In a total of 126 hardware flights, we demonstrate equivalent safety and speed compared to motion capture and visual odometry, but without a manual frame alignment required by those methods....

## Introduction

Autonomous robotic operation requires robots to localize themselves within an envrionment, plan safe paths to reach a desired goal location, and have closed-loop trajectory-tracking. Traditionally, the fundamental problems of planning and localization have been performed in maps represented as occupancy grids \[\], triangular meshes \[\], point clouds \[\], and Signed Distance Fields (SDFs) \[\], all of which provide well-defined geometry.

However, these explicit scene representations are generally constructed at limited resolutions (to enable real-time operation), leaving out potentially-important scene details that could be valuable in planning and localization problems.

The performance of Splat-Loc depends on the presence of informative features in the scene. We can address this in two ways: through planning and by incorporating additional sensor data. Future work will explore the design of planning algorithms that bias the path towards feature-rich regions, improving localization accuracy during path execution. Future work will also incorporate IMU data to improve the robustness of the pose estimator, particularly in featureless regions of the scene where the PnP-RANSAC procedure might fail.

Splat-Plan and Splat-Nav require loading the GSplat model onto the GPU, which takes up about 10 GB of GPU memory. Many drone platforms do not have the onboard compute resources to load the GSplat model, hindering onboard computation. Future work will seek to reduce the memory-usage demands of GSplat models, e.g., using sparse GSplat models.

To check all ellipsoids that are at least partially contained within the box, we check for the minimum signed distance between each hyperplane ${\min_{x \in \mathcal{E}_{j}}{a_{i}^{bb}x}} \leq b_{i}^{bb}$ with every ellipsoid $\mathcal{E}_{j}$ in the scene. Ellipsoids that have negative signed distance for every hyperplane in the box will be at least partially contained. To perform this check, the plane and ellipsoid undergo an affine transformation to produce a new plane and an origin-centered sphere. The signed distance of the new plane from the origin must be less than 1, namely

### Corollary 3

Non-invasive Pose Correction. While fusing Splat-Loc poses with existing pose estimates like VIO is beyond the scope of this work, we will address challenges that arises when using Splat-Plan to plan...
