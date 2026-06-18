Information Theoretic Model Predictive Control: Theory and Applications to Autonomous Driving

Topics include Optimal control, Model predictive control, Predictive control, Autonomous driving, Sampling-based methods, Optimization, Control, Sampling, IT-MPC.

We present an information theoretic approach to stochastic optimal control problems that can be used to derive general sampling based optimization schemes. This new mathematical method is used to develop a sampling based model predictive control algorithm. We apply this information theoretic model predictive control (IT-MPC) scheme to the task of aggressive autonomous driving around a dirt test track, and compare its performance to a model predictive control version of the cross-entropy method.

## Introduction

Autonomous vehicles have the potential to revolutionize transportation by drastically reducing traffic injuries and fatalities, freeing commute time for more productive activities, and enabling more efficient infrastructure utilization. A key step in the design of an autonomous vehicle is the control methodology used to convert the vehicle state and world representation into physical actuation. Existing control methodologies have proven to be effective for many standard vehicle tasks such as lane keeping, turning, and parking....

The control problem for aggressive autonomous driving, and for autonomous driving generally, can naturally be phrased in the language of stochastic optimal control theory. In this framework, a cost function depending on the state and control input is specified, and the goal is to minimize the expected accumulated cost subject to the stochastic dynamical constraints of the vehicle. The advantage of stochastic optimal control over alternative methods is that it directly takes into account the noise characteristics and dynamics of the vehicle during optimization....

Our experiments demonstrate that the costs and dynamics associated with the autonomous driving problem are well suited for a sampling based control scheme: the method naturally handles the non-linear dynamics and it is possible to use large impulse terms in the cost function to provide a strong incentive to avoid the track boundary, while still treating track boundary collisions as a soft constraint. This enables the vehicle to steer out of collision when it does contact the barrier....

The type of approach that we have demonstrated is a promising new direction for solving the challenging problems that arise in autonomous driving tasks. The key tools in this approach are the information theoretic concepts of free energy and the KL divergence, and intensive parallel computation for online optimization.

which can be approximated in discrete time as:

The challenge with this formulation is that changing the inverse temperature $\lambda$, also changes the relative control cost and vice versa. The inverse temperature determines how tightly peaked the optimal distribution is, as $\lambda\rightarrow 0$, the optimal distribution places all of its mass on a single trajectory, whereas as $\lambda\rightarrow\infty$ all points in the state space have equal...
