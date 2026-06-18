Safe Feedback Motion Planning: A Contraction Theory and L1-Adaptive Control Based Approach

Topics include Motion planning, Robotics, Safety, Online algorithms, Planning, Control.

Autonomous robots that are capable of operating safely in the presence of imperfect model knowledge or external disturbances are vital in safety-critical applications. In this paper, we present a planner-agnostic framework to design and certify safe tubes around desired trajectories that the robot is always guaranteed to remain inside of. By leveraging recent results in contraction analysis and L_1-adaptive control we synthesize an architecture that induces safe tubes for nonlinear systems with state and time-varying uncertainties. We demonstrate with a few illustrative examples how contraction theory-based L_1-adaptive control can be used in conjunction with traditional motion planning algorithms to obtain provably safe trajectories.

## Introduction

Motion planning algorithms generate optimal open-loop trajectories for robots to follow; however, any uncertainty in the system can potentially drive the robot far away from the desired path. For instance, quadrotors experience blade-flapping and induced drag forces that are dependent on the velocity, ground effects that are dependent on the altitude, and external wind effects that are often unaccounted for by the motion planner,. Accurate modeling of these uncertainty effects on system dynamics can be very expensive and time-consuming.

In this paper, we present an approach for safe feedback motion planning for control-affine nonlinear systems that relies on contraction theory-based solution for exponential stabilizability around trajectories and $\mathcal{L}_{1}$-adaptive control for handling uncertainties and providing guarantees for transient performance and robustness. In $\mathcal{L}_{1}$ control architecture, estimation is decoupled from control, thereby allowing for arbitrarily fast adaptation subject only to hardware limitations,.

## Discussion

A few critical comments are in order for the performance analysis. The main result in Theorem 5.1 provides uniform ultimate bounds. Let us first discuss the implication of the uniform bound $\rho$ in Eq. 37. As per the definition in Eq. 30, $\rho = {\rho_{r} + \rho_{a}}$. It is evident from the definition that $\rho$ is lower bounded by the initial condition difference $\left. \parallel{x_{0}^{\star} - x_{0}}\parallel \right.$ and the positive scalars $\underset{¯}{\alpha}$ and $\overline{\alpha}$ which are associated with the CCM $M{(x)}$ of the nominal dynamics.

Theorem 5.1 also provides the (uniform) ultimate bound via $\delta{(\omega,T)}$ defined in Eq. 39. As already mentioned, $\rho_{a} \propto {1/\sqrt{\Gamma}}$. Furthermore, from the definition of $\zeta_{1}{(\omega)}$ in Eq. 31a, it is evident that by choosing a large enough $\omega$, there will always exist a known $0 < T < \infty$ such that ${\delta{(\omega,t)}} \leq \overline{\rho}$, for all $t \geq T$, for any chosen $\overline{\delta} > 0$. Therefore, we can always arbitrarily shrink the tube $\mathcal{O}{(\overline{\delta})}$ by choosing appropriate bandwidth $\omega$ and rate of adaptation $\Gamma$.
