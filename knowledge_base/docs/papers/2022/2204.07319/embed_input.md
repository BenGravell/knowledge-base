A Review of Path Following Control Strategies for Autonomous Robotic Vehicles: Theory, Simulations, and Experiments

Topics include Robotics, Vehicles, Control, Frenet-serret, F-S, Parallel transport, P-T, Reference frame, MATLAB.

This article presents an in-depth review of the topic of path following for autonomous robotic vehicles, with a specific focus on vehicle motion in two dimensional space (2D). From a control system standpoint, path following can be formulated as the problem of stabilizing a path following error system that describes the dynamics of position and possibly orientation errors of a vehicle with respect to a path, with the errors defined in an appropriate reference frame. In spite of the large variety of path following methods described in the literature we show that, in principle, most of them can be categorized in two groups: stabilization of the path following error system expressed either in the vehicle's body frame or in a frame attached to a "reference point" moving along the path, such as a Frenet-Serret (F-S) frame or a Parallel Transport (P-T) frame. With this observation, we provide a unified formulation that is simple but general enough to cover many methods available in the literature. We then discuss the advantages and disadvantages of each method, comparing them from the design and implementation standpoint.

## Introduction

Path-following (PF) is one of the most fundamental tasks to be executed by autonomous vehicles. It consists of driving a vehicle to and maintaining it on a pre-defined path while tracking a path-dependent speed profile. Unlike trajectory tracking, the path is not parameterized by time but rather by any other useful parameter that in some cases may be the path length. Thus, there is more flexibility in making the vehicle first converge to the path smoothly then move along it while tracking a given speed assignment.

An in-depth review of standard path-following methods in two dimensional space (2D) explaining in detail the theoretical principles of the different methods.

A discussion of the advantages and disadvantages of each method, comparing them from the design and implementation standpoint.

A Matlab simulation toolbox and ROS/Gazebo simulation packages of path-following methods.
