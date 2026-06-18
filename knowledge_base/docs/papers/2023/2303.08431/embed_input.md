Policy Gradient Converges to the Globally Optimal Policy for Nearly Linear-Quadratic Regulators

Topics include Nonconvex optimization, Policy gradients, Reinforcement learning, Online algorithms, Optimization, Control, Learning, Nonlinear systems.

Nonlinear control systems with partial information to the decision maker are prevalent in a variety of applications. As a step toward studying such nonlinear systems, this work explores reinforcement learning methods for finding the optimal policy in the nearly linear-quadratic regulator systems. In particular, we consider a dynamic system that combines linear and nonlinear components, and is governed by a policy with the same structure. Assuming that the nonlinear component comprises kernels with small Lipschitz coefficients, we characterize the optimization landscape of the cost function. Although the cost function is nonconvex in general, we establish the local strong convexity and smoothness in the vicinity of the global optimizer. Additionally, we propose an initialization mechanism to leverage these properties. Building on the developments, we design a policy gradient algorithm that is guaranteed to converge to the globally optimal policy with a linear rate.

## Introduction

Reinforcement learning (RL) is one of the three classical machine learning paradigms, alongside supervised and unsupervised learning. RL is learning via trial and error, through interactions with an environment and possibly with other agents. In RL, an agent takes actions and receives reinforcement signals in terms of numerical rewards encoding the outcome of the chosen action. In order to maximize the accumulated reward over time, the agent learns to select actions based on past experiences (exploitation) and by making new choices (exploration).

To establish a better foundation of RL, there has been a surge of theoretical works in recent years on the Linear Quadratic Regulator (LQR) problem. This problem is a special class of control problems with linear dynamics and quadratic cost functions. In the seminal work of, the authors studied an LQR problem with deterministic dynamics over an infinite horizon. They proved that the simple policy gradient method converges to the globally optimal solution with a linear rate (despite nonconvexity of the objective).

## Discussion

In Figure 1(a), we observe that the policy gradient algorithm converges under all three initialization regimes, with promising accuracy achieved within around 50 iterations. This indicates that the algorithm is relatively stable with small fluctuations and is consistent with the linear convergence rate demonstrated in the theoretical part. We also observe that the initial value obtained by the policy $K^{lin}$ is comparably close to its convergent value. Such a phenomenon implies that $K^{lin}$ is close to the optimal solution $K^{\ast}$ as expected.

In Figure 1(b), we observe that the policy gradient algorithm converges when $\ell \leq 4$ and the method does not converge for $\ell \geq 5$. Furthermore, Figure suggests the convergence of our policy gradient method under numerous model configurations regardless of the non-linear system dynamics. Therefore, we conclude that the algorithm is robust within a certain magnitude of the nonlinear term, and extends to cases beyond the theoretical requirements.
