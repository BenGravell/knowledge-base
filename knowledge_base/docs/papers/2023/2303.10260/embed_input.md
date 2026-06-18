Online Linear Quadratic Tracking with Regret Guarantees

Online learning algorithms for dynamical systems provide finite time guarantees for control in the presence of sequentially revealed cost functions. We pose the classical linear quadratic tracking problem in the framework of online optimization where the time-varying reference state is unknown a priori and is revealed after the applied control input. We show the equivalence of this problem to the control of linear systems subject to adversarial disturbances and propose a novel online gradient descent based algorithm to achieve efficient tracking in finite time. We provide a dynamic regret upper bound scaling linearly with the path length of the reference trajectory and a numerical example to corroborate the theoretical guarantees.

## Introduction

Linear quadratic tracking (LQT) is the natural generalization of the optimal linear quadratic regulator (LQR) for the setting where the goal is not to drive the state to the origin but to a certain reference. The reference trajectory need not be necessarily time-invariant and in the classic formulation of the problem is known in advance. This is a reasonable assumption in many practical applications, such as aircraft tracking of a predetermined trajectory or precision control in industrial process engineering....

In this letter, we study the LQT problem with an unknown reference trajectory. We pose the problem in the framework of online convex optimization (OCO) subject to the dynamics constraint of the system. In particular, the tracking problem is recast into an equivalent regulation problem with a redefined state that evolves with linear dynamics subject to additive adversarial disturbances. In the spirit of online decision-making under computational and memory constraints, our goal is to develop a gradient-based algorithm that is fast and simple to implement and requires no large memory....

Since $A - {BK}$ is stable, there always exists an arbitrarily small $\alpha > 0$ such that the above is fulfilled.

## Proof of Theorem 3.3

### Theorem 3.3

where $v_{t}$ is updated in the opposite direction of the gradient of the most recent cost. Here $\alpha \in R_{+}$ is the step size and the recursion starts from some $v_{0} \in {\mathbb{R}}^{m}$. As the online objective is quadratic, the gradient is available in a closed form and the update can be represented as $v_{t} = {v_{t - 1} - {2\alpha{({{Ru_{t - 1}} + {B^{\top}Qe_{t}}})}}}$. For the case of a constant reference signal and an underactuated system, the algorithm can converge to a point that is not necessarily the optimal one with respect to infinite horizon cost minimization....

### Proof of Theorem 4.1

The LQT problem for sequentially revealed adversarial reference states is studied mostly with policy regret guarantees, with one of the first works \[\] suggesting a relatively computationally heavy algorithm. In a more recent line of work \[\] the authors introduce a memory-based, gradient descent algorithm and in \[\] tackle the constrained tracking problem....
