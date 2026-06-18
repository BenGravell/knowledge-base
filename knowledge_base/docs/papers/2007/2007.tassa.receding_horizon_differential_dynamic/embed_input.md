Receding Horizon Differential Dynamic Programming

Topics include Differential dynamic programming, Receding horizon control, Optimal control, Nonlinear control, Model predictive control, Trajectory optimization.

Adapts differential dynamic programming to a receding-horizon control setting, using local second-order trajectory optimization repeatedly online. The work is an early precursor to the iLQG/DDP style controllers now common in robotics and model-based control.

The control of high-dimensional, continuous, non-linear systems is a key problem in reinforcement learning and control. Local, trajectory-based methods, using techniques such as Differential Dynamic Programming (DDP) are not directly subject to the curse of dimensionality, but generate only local controllers. In this paper, we introduce Receding Horizon DDP (RH-DDP), an extension to the classic DDP algorithm, which allows us to construct stable and robust controllers based on a library of local-control trajectories. We demonstrate the effectiveness of our approach on a series of high-dimensional control problems using a simulated multi-link swimming robot. These experiments show that our approach effectively circumvents dimensionality issues, and is capable of dealing effectively with problems with (at least) 34 state and 14 action dimensions.
