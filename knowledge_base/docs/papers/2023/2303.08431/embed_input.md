Policy Gradient Converges to the Globally Optimal Policy for Nearly Linear-Quadratic Regulators

Topics include Nonconvex optimization, Policy gradients, Reinforcement learning, Online algorithms, Optimization, Control, Learning, Nonlinear systems.

Nonlinear control systems with partial information to the decision maker are prevalent in a variety of applications. As a step toward studying such nonlinear systems, this work explores reinforcement learning methods for finding the optimal policy in the nearly linear-quadratic regulator systems. In particular, we consider a dynamic system that combines linear and nonlinear components, and is governed by a policy with the same structure. Assuming that the nonlinear component comprises kernels with small Lipschitz coefficients, we characterize the optimization landscape of the cost function. Although the cost function is nonconvex in general, we establish the local strong convexity and smoothness in the vicinity of the global optimizer. Additionally, we propose an initialization mechanism to leverage these properties. Building on the developments, we design a policy gradient algorithm that is guaranteed to converge to the globally optimal policy with a linear rate.

## Introduction

Reinforcement learning (RL) is one of the three classical machine learning paradigms, alongside supervised and unsupervised learning. RL is learning via trial and error, through interactions with an environment and possibly with other agents. In RL, an agent takes actions and receives reinforcement signals in terms of numerical rewards encoding the outcome of the chosen action. In order to maximize the accumulated reward over time, the agent learns to select actions based on past experiences (exploitation) and by making new choices (exploration)....

To establish a better foundation of RL, there has been a surge of theoretical works in recent years on the Linear Quadratic Regulator (LQR) problem. This problem is a special class of control problems with linear dynamics and quadratic cost functions. In the seminal work of \[\], the authors studied an LQR problem with deterministic dynamics over an infinite horizon. They proved that the simple policy gradient method converges to the globally optimal solution with a linear rate (despite nonconvexity of the objective)....

## Conclusions

We consider a nonlinear optimal control problem, characterize the local strong convexity of the cost function, and prove that the globally optimal solution is close to a carefully chosen initialization. Additionally, we design a zeroth-order policy gradient algorithm and establish a convergence result under the proposed policy initialization scheme for the nonlinear control problem. We hope these results would shed light on the efficiency of policy gradient methods for nonlinear optimal control problems when the underlying models are unknown to the decision maker....

In this section, we numerically evaluate the performance of our policy gradient method proposed in Section through extensive experiments. In particular, we focus on addressing the following questions:

By Lemma 6.1. ‣ 6.1 Proof of Proposition 4.6 ‣ 6 Proofs ‣ Policy gradient converges to the globally optimal policy for nearly linear-quadratic regulators"), for each $\nu \in {}$, $Y_{N}^{\top}Y_{N}$ is invertible with probability at least $1 - \nu$ for any $N \geq N_{0} ≔ \left( {{d_{1}\sqrt{n + p + d}} - \sqrt{\frac{1}{d_{2}}{\log\frac{2}{\nu}}}} \right)^{2}$. As a consequence, we have
