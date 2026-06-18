Data-Enabled Predictive Control: In the Shallows of the DeePC

Topics include Model predictive control, Predictive control, Safety, Real-time systems, Online algorithms, Control, DeePC.

We consider the problem of optimal trajectory tracking for unknown systems. A novel data-enabled predictive control (DeePC) algorithm is presented that computes optimal and safe control policies using real-time feedback driving the unknown system along a desired trajectory while satisfying system constraints. Using a finite number of data samples from the unknown system, our proposed algorithm uses a behavioural systems theory approach to learn a non-parametric system model used to predict future trajectories. The DeePC algorithm is shown to be equivalent to the classical and widely adopted Model Predictive Control (MPC) algorithm in the case of deterministic linear time-invariant systems. In the case of nonlinear stochastic systems, we propose regularizations to the DeePC algorithm. Simulations are provided to illustrate performance and compare the algorithm with other methods.

## Introduction

As systems are becoming more complex and data is becoming more readily available, scientists and practitioners are beginning to bypass classical model-based techniques in favour of data-driven methods. Data-driven methods are suitable for applications where first-principle models are not conceivable (e.g., in human-in-the-loop applications), when models are too complex for control design (e.g., in fluid dynamics), and when thorough modelling and parameter identification is too costly (e.g., in robotics)....

A challenging problem in systems control is optimal trajectory tracking, where a control policy is computed based on output feedback that drives a dynamical system along a desired output trajectory while minimizing a stage cost and respecting safety constraints. A special case of the trajectory tracking problem is regulation, in which a control policy drives the system to an equilibrium point. One of the most celebrated and widely used control techniques for trajectory tracking is receding horizon Model Predictive Control (MPC), precisely because it allows one to include safety considerations during control design....

## Conclusion

We presented a data-enabled algorithm that can be applied to unknown LTI systems and formally showed its equivalence to the classical MPC algorithm. The DeePC algorithm uses a finite data set to learn the behaviour of the unknown system and computes optimal controls using real-time feedback to drive the system along a desired trajectory while respecting system constraints. Furthermore, we simulated a regularized version of the algorithm on stochastic nonlinear quadcopter dynamics illustrating its capabilities beyond deterministic LTI systems. The performance was superior when compared to system ID followed by MPC....

### V-A Data collection

$({\mathbb{Z}}_{\geq 0},{\mathbb{W}},\mathcal{B})$ is *complete* if $\mathcal{B}$ is closed in the topology of pointwise convergence.

where $x_{\text{ini}}$ is uniquely determined from $\text{col}{(u_{\text{ini}},y_{\text{ini}})}$. We now look at the feasible set of (III). By rewriting the constraints in (III) we obtain

In the context of unknown black-box systems, there is no approach which solves the optimal trajectory tracking problem subject to constraints and partial (output) observations....
