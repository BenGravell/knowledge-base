FOCI: Trajectory Optimization on Gaussian Splats

Topics include Trajectory optimization, Gaussian splatting, 3D Gaussian splatting, 3D scene, Representation.

FOCI is a trajectory optimization method that operates directly on Gaussian Splat scene representations.

3D Gaussian Splatting (3DGS) has recently gained popularity as a faster alternative to Neural Radiance Fields (NeRFs) in 3D reconstruction and view synthesis methods. Leveraging the spatial information encoded in 3DGS, this work proposes FOCI (Field Overlap Collision Integral), an algorithm that is able to optimize trajectories directly on the Gaussians themselves. FOCI leverages a novel and interpretable collision formulation for 3DGS using the notion of the overlap integral between Gaussians. Contrary to other approaches, which represent the robot with conservative bounding boxes that underestimate the traversability of the environment, we propose to represent the environment and the robot as Gaussian Splats. This not only has desirable computational properties, but also allows for orientation-aware planning, allowing the robot to pass through very tight and narrow spaces. We extensively test our algorithm in both synthetic and real Gaussian Splats, showcasing that collision-free trajectories for the ANYmal legged robot that can be computed in a few seconds, even with hundreds of thousands of Gaussians making up the environment. The project page and code are available at

## INTRODUCTION

Trajectory planning is integral to autonomous mobile robotics to ensure guided and safe operation. However, in order to make an informed decision, these planning algorithms heavily depend on the underlying environment representations. Popular representations include occupancy grids, signed distance fields, 3D Meshes, and point clouds.

Recently, \\acpnerf \[\] have been proposed as a novel neural representation of the environment. They can be created from simple monocular images and they encode the environment as a fully connected neural network, mapping position in space and viewing direction to occupancy and color. However, they suffer from having slow inference speeds because new views have to be created using a computationally expensive ray-casting procedure. More recently, \\ac3dgs \[\] has been proposed as a promising alternative to \\acpnerf....

## Conclusion

In this work, we proposed a novel collision formulation for \\acl3dgs, that is computed in an efficient parallel manner, and integrated it into a trajectory optimization pipeline. We show that it can be effectively used for orientation-aware planning and verify it on the ANYmal quadruped robot. Because we exclusively operate in 3D Gaussian space, representing the environment and the robot as Gaussians, our method can be freely combined with new developments from the 3DGS community. Furthermore, we show that this method works on realistic data including scenes captured using the onboard sensor of the robot itself....

Whenever integrating a quantity like the collision measure along the spline is necessary, we approximate it as a discrete sum over the values discretized along the spline in $K$ equidistant steps. We represented the robot position and yaw orientation as a cubic B-spline. The kinematics of each Gaussian that makes up the robot is a function of the position and orientation of the base ${{\overline{\mathbf{μ}}}_{j}{(\mathbf{p},\psi)}} = {{\overline{\mathbf{μ}}}_{j}{(\mathbf{x})}}$.

Our methodology can be split into three parts: 1) trajectory representation to create an initial spline, 2) collision measure and 3) optimization loop.

Figure 2: Sample trajectories created on synthetic testing data showing a 3 Gaussian robot rotating to navigate the environments....
