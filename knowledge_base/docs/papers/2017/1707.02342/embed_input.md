Information Theoretic Model Predictive Control: Theory and Applications to Autonomous Driving

Topics include Optimal control, Model predictive control, Predictive control, Autonomous driving, Sampling-based methods, Optimization, Control, Sampling, IT-MPC.

We present an information theoretic approach to stochastic optimal control problems that can be used to derive general sampling based optimization schemes. This new mathematical method is used to develop a sampling based model predictive control algorithm. We apply this information theoretic model predictive control (IT-MPC) scheme to the task of aggressive autonomous driving around a dirt test track, and compare its performance to a model predictive control version of the cross-entropy method.

## Introduction

Autonomous vehicles have the potential to revolutionize transportation by drastically reducing traffic injuries and fatalities, freeing commute time for more productive activities, and enabling more efficient infrastructure utilization. A key step in the design of an autonomous vehicle is the control methodology used to convert the vehicle state and world representation into physical actuation. Existing control methodologies have proven to be effective for many standard vehicle tasks such as lane keeping, turning, and parking.

The control problem for aggressive autonomous driving, and for autonomous driving generally, can naturally be phrased in the language of stochastic optimal control theory. In this framework, a cost function depending on the state and control input is specified, and the goal is to minimize the expected accumulated cost subject to the stochastic dynamical constraints of the vehicle. The advantage of stochastic optimal control over alternative methods is that it directly takes into account the noise characteristics and dynamics of the vehicle during optimization.

In this paper, we develop a new type of control framework based on an information theoretic interpretation of optimal control, and we demonstrate that it is able to overcome the tractability issues associated with the autonomous driving problem. This framework results in a theoretically-sound method for creating sampling based optimization methods, and by utilizing recent advances in computing with graphics processing units (GPUs), we can create a highly parallel sampling algorithm which can operate in a model predictive control (receding horizon) manner in a fast control loop (40 Hz).

In section III we derive a highly parallelizable control update law using an information theoretic interpretation of stochastic optimal control, and we show how it can be used to create a flexible model predictive control algorithm.

## Discussion

In this paper we have derived an information theoretic framework which provides the mathematical tools required to design sampling based optimization algorithms suited for controlling autonomous systems. We compared and contrasted the theoretical aspects of this new framework with traditional stochastic optimal control, and we demonstrated how the new framework can be used to derive a sampling based model predictive controller.
