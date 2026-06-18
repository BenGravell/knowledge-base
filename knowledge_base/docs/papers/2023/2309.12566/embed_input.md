Recent Advances in Path Integral Control for Trajectory Optimization: An Overview in Theoretical and Algorithmic Perspectives

Topics include Model predictive path integral control, Path integral control, Survey, Trajectory optimization, Stochastic optimal control, Variational inference.

Survey paper reviewing the theoretical foundations and algorithmic advances in path integral control methods for trajectory optimization, covering MPPI variants, variational inference approaches, and connections to stochastic optimal control theory.

This paper presents a tutorial overview of path integral (PI) approaches for stochastic optimal control and trajectory optimization. We concisely summarize the theoretical development of path integral control to compute a solution for stochastic optimal control and provide algorithmic descriptions of the cross-entropy (CE) method, an open-loop controller using the receding horizon scheme known as the model predictive path integral (MPPI), and a parameterized state feedback controller based on the path integral control theory. We discuss policy search methods based on path integral control, efficient and stable sampling strategies, extensions to multi-agent decision-making, and MPPI for the trajectory optimization on manifolds. For tutorial demonstrations, some PI-based controllers are implemented in Python, MATLAB and ROS2/Gazebo simulations for trajectory optimization. The simulation frameworks and source codes are publicly available at

## Introduction

Trajectory optimization for motion or path planning is a fundamental problem in autonomous systems. Several requirements must be simultaneously considered for autonomous robot motion, path planning, navigation, and control. Examples include the specifications of mission objectives, examining the certifiable dynamical feasibility of a robot, ensuring collision avoidance, and considering the internal physical and communication constraints of autonomous robots.

In particular, generating an energy-efficient and collision-free safe trajectory is of the utmost importance during the process of autonomous vehicle driving, autonomous racing drone, unmanned aerial vehicles, electric vertical take-off and landing (eVTOL) urban air mobility (UAM), missile guidance, space vehicle control, and satellite attitude trajectory optimization

From an algorithmic perspective, the complexity of motion planning is NP-complete. Various computational methods have been proposed for motion planning, including sampling-based methods, nonlinear programming (NLP), sequential convex programming (SCP), differential dynamic programming (DDP), hybrid methods, and differential-flatness-based optimal control.

Optimization methods can explicitly perform safe and efficient trajectory generation for path and motion planning. The two most popular optimal path and motion planning methods for autonomous robots are gradient- and sampling-based methods for trajectory optimization. The former frequently assumes that the objective and constraint functions in a given planning problem are differentiable and can rapidly provide a locally optimal smooth trajectory.

The remainder of this paper is organized as follows: Section II presents the overview of some path integral control methods. Section III reviews the theoretical background of path integral control and its variations. Section IV describes the algorithmic implementation of several optimal control methods that employ a path-integral control framework. In Section V, two MATLAB simulation case studies are presented to demonstrate the effectiveness of predictive path integral control.
