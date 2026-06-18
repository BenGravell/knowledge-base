Data-Enabled Predictive Control: In the Shallows of the DeePC

Topics include Model predictive control, Predictive control, Safety, Real-time systems, Online algorithms, Control, DeePC.

We consider the problem of optimal trajectory tracking for unknown systems. A novel data-enabled predictive control (DeePC) algorithm is presented that computes optimal and safe control policies using real-time feedback driving the unknown system along a desired trajectory while satisfying system constraints. Using a finite number of data samples from the unknown system, our proposed algorithm uses a behavioural systems theory approach to learn a non-parametric system model used to predict future trajectories. The DeePC algorithm is shown to be equivalent to the classical and widely adopted Model Predictive Control (MPC) algorithm in the case of deterministic linear time-invariant systems. In the case of nonlinear stochastic systems, we propose regularizations to the DeePC algorithm. Simulations are provided to illustrate performance and compare the algorithm with other methods.

## Introduction

As systems are becoming more complex and data is becoming more readily available, scientists and practitioners are beginning to bypass classical model-based techniques in favour of data-driven methods. Data-driven methods are suitable for applications where first-principle models are not conceivable (e.g., in human-in-the-loop applications), when models are too complex for control design (e.g., in fluid dynamics), and when thorough modelling and parameter identification is too costly (e.g., in robotics).

MPC based on Dynamic Matrix Control has been historically used as a data-driven control technique, in which zero-initial condition step responses are used to predict future trajectories. Although this technique has many limitations, it motivates the use of a non-parametric predictive control model. Other non-parametric predictive models have been proposed . These methods do not solve the problem of optimal trajectory tracking with constraints, but serve as building blocks for our approach.

Here we present a Data-enabled Predictive Control (DeePC) algorithm. Unlike classical MPC and the learning-based control techniques outlined above, the DeePC algorithm does not rely on a parametric system representation. Instead, similar to, we approach the problem from a behavioural systems theory perspective. Rather than attempting to learn a parametric system model, we aim at learning the system's "behaviour" (see Section IV for the precise definition).

## Conclusion

We presented a data-enabled algorithm that can be applied to unknown LTI systems and formally showed its equivalence to the classical MPC algorithm. The DeePC algorithm uses a finite data set to learn the behaviour of the unknown system and computes optimal controls using real-time feedback to drive the system along a desired trajectory while respecting system constraints. Furthermore, we simulated a regularized version of the algorithm on stochastic nonlinear quadcopter dynamics illustrating its capabilities beyond deterministic LTI systems. The performance was superior when compared to system ID followed by MPC.
