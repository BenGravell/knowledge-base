A Data-Driven Approach to Synthesizing Dynamics-Aware Trajectories for Underactuated Robotic Systems

Topics include Optimal control, Trajectory optimization, Robotics, Aerial robotics, Online algorithms, Optimization, Planning, Control.

We consider joint trajectory generation and tracking control for under-actuated robotic systems. A common solution is to use a layered control architecture, where the top layer uses a simplified model of system dynamics for trajectory generation, and the low layer ensures approximate tracking of this trajectory via feedback control. While such layered control architectures are standard and work well in practice, selecting the simplified model used for trajectory generation typically relies on engineering intuition and experience. In this paper, we propose an alternative data-driven approach to dynamics-aware trajectory generation. We show that a suitable augmented Lagrangian reformulation of a global nonlinear optimal control problem results in a layered decomposition of the overall problem into trajectory planning and feedback control layers. Crucially, the resulting trajectory optimization is dynamics-aware, in that, it is modified with a tracking penalty regularizer encoding the dynamic feasibility of the generated trajectory....

## Introduction

Modularity is a guiding principle behind the design of numerous autonomous platforms. For example, the autonomy stack of a typical robot consists of separate modules for perception, planning, and control. In spite of the requirement of safely executing tasks in real time with limited on board computational resources, such modules usually operate at different frequencies and levels of abstraction. Roughly speaking, higher levels of abstraction allow for faster decision making. However, if the degree of abstraction varies among the different modules beyond a suitable threshold, the system as a whole can behave in unexpected, unsafe ways....

Although trajectory planning and control have been among the most extensively studied areas of robotics, numerous problems remain to be solved. In particular, graph-search-based path planning algorithms can find it challenging to account for complex nonlinear system dynamics. Similarly, real-time optimization-based methods for generating trajectories typically use a simplified or a reduced order dynamics model of the agent. In contrast, low-level feedback control policies often rely on more accurate, detailed dynamics of the system being controlled in order to track a reference trajectory planned by some of the aforementioned approaches....

## Conclusion

We showed that the familiar two layer architecture composed of a trajectory planning layer and a low-layer tracking controller can be derived via a suitable relaxation of a global optimization problem. The result of this relaxation is a regularized trajectory planning problem, wherein the original state objective function is augmented with a tracking penalty which captures the low layer closed-loop system's ability to track a given reference trajectory. We further observed that this penalty can be interpreted as the cost-to-go of an augmented system, and showed how it could be learned from data....

### Unicycle Control

We then relax this redundant equality constraint to a soft-constraint in the objective function, resulting in the augmented Lagrangian reformulation:

We train a multi-layer perceptron network with $3$ hidden layers of $\{ 1000,500,200\}$ neurons, respectively, with Exponential Linear Unit (ELU) activation functions. ---see Network Parameterization and Training for more details....
