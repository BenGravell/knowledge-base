Augmented Lagrangian Methods as Layered Control Architectures

Topics include Nonconvex optimization, Optimal control, Online algorithms, Planning, Control, Alternating-direction method of multipliers, Augmented Lagrangian method, Lagrange multiplier.

For optimal control problems that involve planning and following a trajectory, two degree of freedom (2DOF) controllers are a ubiquitously used control architecture that decomposes the problem into a trajectory generation layer and a feedback control layer. However, despite the broad use and practical success of this layered control architecture, it remains a design choice that must be imposed a priori on the control policy. To address this gap, this paper seeks to initiate a principled study of the design of layered control architectures, with an initial focus on the 2DOF controller. We show that applying the Alternating Direction Method of Multipliers (ADMM) algorithm to solve a strategically rewritten optimal control problem results in solutions that are naturally layered, and composed of a trajectory generation layer and a feedback control layer. Furthermore, these layers are coupled via Lagrange multipliers that ensure dynamic feasibility of the planned trajectory....

## Introduction

Optimal control has proven to be a key approach to solving problems across a wide range of fields, including economics, robotics, and communication systems. However, despite their significance, solving optimal control problems can be challenging due to nonlinear dynamics, high-dimensional state and control spaces, uncertainty, noise, and constraints. For optimal control problems that involve planning and following a trajectory, a ubiquitous *layered control architecture* \[1, Ch. 15\] commonly referred to as a *two degree of freedom (2DOF) controller* has emerged as the standard solution approach....

We elaborate more on these different settings below, but highlight here that despite the ubiquity and practical success of the layered approach, this control structure does not emerge naturally from solving an optimal control problem, but rather must be imposed *a priori* on the control policy. To address this gap, we seek to initiate a principled study of the design of layered control architectures, with an initial focus on the 2DOF design pattern....

## Conclusion

We showed that by introducing a redundant reference variable to an optimal control problem and subsequently applying ADMM, optimal controllers with a layered structure are obtained. We instantiated this approach in the context of linear optimal control problems, and recovered a feedforward/feedback-based optimal controller. In the context of nonlinear optimal control, we empirically demonstrated the benefits of separating trajectory generation from feedback control in terms of both convergence (as compared to vanilla iLQR) and flexibility (by seamlessly incorporating both convex and nonconvex constraints)....

Feedforward term $K_{t}^{ff}\mu_{t}$: this term applies control actions to drive the system towards the desired reference trajectory, as encoded in the look-ahead state $\mu_{t} = {(r_{t}^{k + 1},\ldots,r_{N}^{k + 1},0,\ldots,0)}$.

where $\mathcal{R}^{N}:={\mathcal{R} \times \cdots \times \mathcal{R}}$ is the Cartesian product of the constraint set $\mathcal{R}$ over the time horizon $N$.

### Layered control architectures for nonlinear systems

*Contributions:* This paper seeks to initiate the study of layered control architectures (LCAs) through the lens of optimization algorithms. Our specific contributions are:
