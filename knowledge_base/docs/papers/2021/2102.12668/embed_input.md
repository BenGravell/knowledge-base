Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach

Topics include Convex optimization, Motion planning, Lyapunov methods, Stability analysis, Robustness, Neural networks, Online algorithms, Optimization, Planning, Control, Learning, Stability, LAG-ROS, Lyapunov functions, Euclidean distance, Robust control.

This paper presents Learning-based Autonomous Guidance with RObustness and Stability guarantees (LAG-ROS), which provides machine learning-based nonlinear motion planners with formal robustness and stability guarantees, by designing a differential Lyapunov function using contraction theory. LAG-ROS utilizes a neural network to model a robust tracking controller independently of a target trajectory, for which we show that the Euclidean distance between the target and controlled trajectories is exponentially bounded linearly in the learning error, even under the existence of bounded external disturbances. We also present a convex optimization approach that minimizes the steady-state bound of the tracking error to construct the robust control law for neural network training. In numerical simulations, it is demonstrated that the proposed method indeed possesses superior properties of robustness and nonlinear stability resulting from contraction theory, whilst retaining the computational efficiency of existing learning-based motion planners.

## Introduction

In the near future of robotic exploration, teams of robots are expected to perform complex decision-making tasks autonomously in extreme environments, where their motions are typically governed by nonlinear dynamics with external disturbances. For such operations to be successful, they need to compute optimal motion plans online while robustly guaranteeing convergence to the target trajectory, both with their limited onboard computational resources. Thus, this work aims to propose a learning-based robust motion planning and control algorithm that meets these challenging requirements.

### Related Work

## Conclusion

In this work, we propose a new learning-based motion planning framework, called LAG-ROS, with the formal robustness and stability guarantees of Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"). It extensively utilizes contraction theory to provide an explicit exponential bound on the distance between the target and controlled trajectories, even under the existence of the learning error and external disturbances....

where $c_{1} \geq 0$, $c_{2} \geq 0$, $P{(\overline{x},\overline{u},t)}$ is some performance-based cost function, $T > 0$ is a given time horizon, $\overline{\mathcal{X}}$ is robust admissible state space defined as ${\overline{\mathcal{X}}{(o_{g},t)}} = \left. \{{{v{(t)}} \in {\mathbb{R}}^{n}} \middle| {{{\forall{\xi{(t)}}} \in \left....

In addition, we modify the CV-STEM in to derive a robust control input $u^{\ast}$ which also greedily minimizes the deviation of $u^{\ast}$ from the target $u_{d}$, using the computed contraction metric $M$ to construct a differential Lyapunov function $V = {\deltay^{\top}M\deltay}$. Note that $u^{\ast}$ is to be modeled by a neural network which maps $(x,o_{\ell},t)$ to $u^{\ast}$ implicitly accounting for $(x_{d},u_{d})$ as described in Theorem 1 ‣ Learning-based Robust Motion Planning with Guaranteed Stability: A Contraction Theory Approach"), although $u^{\ast}$ takes $(x,x_{d},u_{d},t)$ as its inputs (see Sec. IV-B).

We use a neural network $u_{L}$ with $3$ layers and $100$ neurons. The network is trained using stochastic gradient descent with training data sampled by Theorems 2--4, and the loss function is defined as $\|{u_{L} - u^{\ast}}\|$ to satisfy the learning error bound $\epsilon_{\ell}$ of Theorem 1 ‣...
