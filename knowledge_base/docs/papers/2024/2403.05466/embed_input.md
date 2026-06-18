Grasping Trajectory Optimization with Point Clouds

Topics include Trajectory optimization, Robotics, Online algorithms, Optimization, Planning, Point cloud.

We introduce a new trajectory optimization method for robotic grasping based on a point-cloud representation of robots and task spaces. In our method, robots are represented by 3D points on their link surfaces. The task space of a robot is represented by a point cloud that can be obtained from depth sensors. Using the point-cloud representation, goal reaching in grasping can be formulated as point matching, while collision avoidance can be efficiently achieved by querying the signed distance values of the robot points in the signed distance field of the scene points. Consequently, a constrained nonlinear optimization problem is formulated to solve the joint motion and grasp planning problem. The advantage of our method is that the point-cloud representation is general to be used with any robot in any environment. We demonstrate the effectiveness of our method by performing experiments on a tabletop scene and a shelf scene for grasping with a Fetch mobile manipulator and a Franka Panda arm. The project page is available at

## Introduction

In robot manipulation, planning a robot trajectory to grasp an object is a fundamental research problem. The problem is challenging since it requires motion planning to avoid obstacles in the task space and grasp planning to decide how to grasp a target object. Traditionally, the motion planning problem and the grasp planning problem are tackled separately. Motion planning approaches focus on finding a collision-free path to reach a given end-effector goal.

In this work, motivated by the goal-set-based trajectory optimization framework for joint motion and grasp planning, we introduce a new trajectory optimization method for robotic grasping. Compared to previous methods, our method has the following advantages. First, we introduce a point-cloud representation of robots and task spaces for goal reaching and obstacle avoidance. Point clouds of robots are generated using the 3D meshes of the robot links, whereas point clouds of the task space can be obtained from depth sensors such as RGB-D cameras.

## Conclusion and Discussion

We introduce a new trajectory optimization method for joint motion and grasp planning. The core component of our method is a point cloud-based representation for robots and task spaces. This representation is generalizable to different robots and different environments. We formulate goal reaching and collision avoidance in the trajectory optimization using the point-cloud representation. By solving a constrained nonlinear optimization problem using the Ipopt solver, our method can generate robot trajectories for grasping. Experiments are conducted in simulation and in the real world to demonstrate the effectiveness of our method.

One limitation of our method is that trajectory optimization is slow when relying on an external solver. Future work includes speeding up the optimization. One direction is to explore using GPUs for parallel computing. Another direction is to explore model predictive control with our point-cloud representation for robotic grasping. To further improve the grasp success rate, a grasp planner that considers force closure or grasp stability will be helpful.
