FOCI: Trajectory Optimization on Gaussian Splats

Topics include Trajectory optimization, Gaussian splatting, 3D Gaussian splatting, 3D scene, Representation.

FOCI is a trajectory optimization method that operates directly on Gaussian Splat scene representations.

3D Gaussian Splatting (3DGS) has recently gained popularity as a faster alternative to Neural Radiance Fields (NeRFs) in 3D reconstruction and view synthesis methods. Leveraging the spatial information encoded in 3DGS, this work proposes FOCI (Field Overlap Collision Integral), an algorithm that is able to optimize trajectories directly on the Gaussians themselves. FOCI leverages a novel and interpretable collision formulation for 3DGS using the notion of the overlap integral between Gaussians. Contrary to other approaches, which represent the robot with conservative bounding boxes that underestimate the traversability of the environment, we propose to represent the environment and the robot as Gaussian Splats. This not only has desirable computational properties, but also allows for orientation-aware planning, allowing the robot to pass through very tight and narrow spaces. We extensively test our algorithm in both synthetic and real Gaussian Splats, showcasing that collision-free trajectories for the ANYmal legged robot that can be computed in a few seconds, even with hundreds of thousands of Gaussians making up the environment. The project page and code are available at

## INTRODUCTION

Trajectory planning is integral to autonomous mobile robotics to ensure guided and safe operation. However, in order to make an informed decision, these planning algorithms heavily depend on the underlying environment representations. Popular representations include occupancy grids, signed distance fields, 3D Meshes, and point clouds.

Given the advantages that \\ac3dgs offers when compared with \\acpnerf, the natural question is how a robot can leverage this Gaussian representation for navigation. In this paper, we propose an algorithm that enables a robot to perform trajectory optimization directly on the 3D Gaussians. Although some steps have been taken in this direction, the huge number of Gaussians a scene can have, together with the specific formulation of an explicit collision measure, makes this problem especially hard.

To overcome these challenges, we propose FOCI, a trajectory optimization algorithm that leverages the overlap integral - the spatial integral over the multiplication of two functions - as a proxy measure for the collision between two Gaussians. By representing both the robot and the environment with 3D Gaussians, evaluating the full-body collision between them reduces to a sum of normal distribution evaluations. Furthermore, the resulting expression is fully differentiable, yielding expressive gradients in the optimization step.

## Limitations

Three current shortcomings of the algorithm include a) occasional obstacle collision, b) distance agnostic optimization, c) sensitivity to \\ac3dgs quality.

a\) Both the jerk as well as the obstacle cost are additive terms in the cost function. Since obstacle avoidance is not formulated as a hard constraint, it can be traded off with the jerk cost, yielding a low jerk but colliding trajectories. Figure shows a trajectory resulting from such a trade off. Related work, such as trajectory planning on NeRFs by Adamkiewicz et al., has also encoded obstacle avoidance as a cost function component.
