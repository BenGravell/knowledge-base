Representing Robot Geometry as Distance Fields: Applications to Whole-Body Manipulation

Topics include Robot kinematics, Signed distance, Distance queries, Robot manipulation, Collision avoidance, Trajectory optimization, Robotics.

Represents articulated robot geometry with differentiable distance fields built from per-link signed-distance models and kinematic structure. This gives optimization-based manipulation and collision avoidance access to smooth robot-surface distance queries in task and joint spaces.

In this work, we propose a novel approach to represent robot geometry as distance fields (RDF) that extends the principle of signed distance fields (SDFs) to articulated kinematic chains. Our method employs a combination of Bernstein polynomials to encode the signed distance for each robot link with high accuracy and efficiency while ensuring the mathematical continuity and differentiability of SDFs. We further leverage the kinematics chain of the robot to produce the SDF representation in joint space, allowing robust distance queries in arbitrary joint configurations. The proposed RDF representation is differentiable and smooth in both task and joint spaces, enabling its direct integration to optimization problems. Additionally, the 0-level set of the robot corresponds to the robot surface, which can be seamlessly integrated into whole-body manipulation tasks. We conduct various experiments in both simulations and with 7-axis Franka Emika robots, comparing against baseline methods, and demonstrating its effectiveness in collision avoidance and whole-body manipulation tasks.

## Introduction

In robotics, the representation of a robot commonly relies on low-dimensional states, like joint configuration and end-effector poses. However, this low-dimensional representation lacks internal structure details and is insensitive to external factors, limiting the ability to interact with the environment and respond to real-world. To handle this problem, some geometric representations have been proposed, like primitives and meshes, with various applications. However, they either make simplified assumptions or require significant computational resources to obtain a detailed model.

We experimentally demonstrate the capabilities of our RDF in three aspects. First, we provide a quantitative comparison of the produced distance fields against other representative methods, showing the advantage of our approach. Then, we conduct collision avoidance experiments to show the real-time control performance. Finally, we present a novel formulation that leverages the RDF representation for manipulation tasks requiring contact, by generalizing the robot's Jacobian matrix from its end-effector to the 0-level set of SDF.

We propose a simple and flexible structure that leverages Bernstein polynomials to encode SDFs, showing high accuracy and efficiency while ensuring continuity and differentiability.

We demonstrate the effectiveness of our RDF representation in experiments and show how to integrate it into optimization problems for whole-body manipulation tasks without defining any points on the robot surface.

## Conclusion

In this paper, we proposed a novel approach to represent the geometry of a robot as distance fields. We leveraged the kinematic structure of the robot to generalize configuration-agnostic signed distance functions that remain valid for arbitrary robot configurations, which enables more effective learning and more accurate inference of distance fields. The SDF for each link of the robot is represented by a combination of piecewise multivariate polynomials, ensuring interpretability, compactness and smoothness while remaining competitive in terms of efficiency and accuracy.
