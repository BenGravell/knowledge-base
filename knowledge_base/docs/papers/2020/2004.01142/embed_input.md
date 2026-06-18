Safe Feedback Motion Planning: A Contraction Theory and L1-Adaptive Control Based Approach

Topics include Motion planning, Robotics, Safety, Online algorithms, Planning, Control.

Autonomous robots that are capable of operating safely in the presence of imperfect model knowledge or external disturbances are vital in safety-critical applications. In this paper, we present a planner-agnostic framework to design and certify safe tubes around desired trajectories that the robot is always guaranteed to remain inside of. By leveraging recent results in contraction analysis and L_1-adaptive control we synthesize an architecture that induces safe tubes for nonlinear systems with state and time-varying uncertainties. We demonstrate with a few illustrative examples how contraction theory-based L_1-adaptive control can be used in conjunction with traditional motion planning algorithms to obtain provably safe trajectories.

## Introduction

Motion planning algorithms generate optimal open-loop trajectories for robots to follow; however, any uncertainty in the system can potentially drive the robot far away from the desired path. For instance, quadrotors experience blade-flapping and induced drag forces that are dependent on the velocity, ground effects that are dependent on the altitude, and external wind effects that are often unaccounted for by the motion planner,. Accurate modeling of these uncertainty effects on system dynamics can be very expensive and time-consuming....

Robust trajectory tracking controllers using classical Lyapunov stability theory have been designed for helicopters, hovercraft, marine vehicles, and several other autonomous robots, which exhibit nonlinear behavior. These approaches rely on backstepping techniques, sliding-mode control, passivity-based control, or other robust nonlinear control design tools \[6, Chapter 14\]. However, the classical methods do not provide a 'one size fits all' procedure for the constructive design of tracking controllers for a large class of nonlinear systems....

## Conclusion and Future Work

We present a control methodology to enable safe and guaranteed feedback motion planning. The presented work relies on differential geometric contraction theory and $\mathcal{L}_{1}$-adaptive control. The proposed controller enables the apriori computation of uniform and ultimate-bounds which act as safety-certificates. These safety certificates induce 'tubes' which can be taken into account by any planner of choice. In this way, the safety of the system/robot is always guaranteed in the presence of model and environmental uncertainties....

Figure 2: Architecture of CCM-based ℒ1-adaptive control

### Definition 3.2

Based on the definition of $\rho_{r}$ in Eq. 30 and the bounds on the Riemannian energy $\mathcal{E}{({x^{\star}{(t)}},{x{(t)}})}$ in Eq. 12, the inequality $\rho_{r}^{2} > {{\mathcal{E}{(x_{0}^{\star},x_{0})}}/\underset{¯}{\alpha}}$ holds. Furthermore, since $\zeta_{1}{(\omega)}$, $\zeta_{2}{(\omega)}$, and $\zeta_{3}{(\omega)}$, all converge to zero as $\omega$ increases, the bandwidth conditions in (32a)-(32b) can always be satisfied by choosing a large enough $\omega$.

Advances in computational resources and optimization toolboxes available to autonomous robots have led to active developments in the field of...
