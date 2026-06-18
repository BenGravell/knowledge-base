BP-MPC: Optimizing the Closed-Loop Performance of MPC Using Backpropagation

Topics include Model predictive control, Backpropagation, Policy optimization, Differentiable control, Model predictive control tuning, Closed-loop performance.

Optimizes MPC costs and constraints by backpropagating closed-loop performance through linearized dynamics and MPC policies. The paper contributes a convergence-backed tuning procedure for improving closed-loop behavior, including a feasibility-loss extension for cases where the MPC problem can fail.

Model predictive control (MPC) is pervasive in research and industry. However, designing the cost function and the constraints of the MPC to maximize closed-loop performance remains an open problem. To achieve optimal tuning, we propose a backpropagation scheme that solves a policy optimization problem with nonlinear system dynamics and MPC policies. We enforce the system dynamics using linearization and allow the MPC problem to contain elements that depend on the current system state and on past MPC solutions. Moreover, we propose a simple extension that can deal with losses of feasibility. Our approach, unlike other methods in the literature, enjoys convergence guarantees.

## Introduction

In recent years, optimization-based control algorithms have become increasingly popular in industry and academia, in part thanks to the ever-growing computational power of CPUs, and the availability of fast numerical implementations. Arguably, the biggest appeal of optimization-based control techniques is their ability to explicitly account for process constraints in their formulation, allowing for an optimal and safe selection of the control inputs.

A second limitation of all the approaches mentioned before, is that they all utilize objective functions that concern a single time-step. In most cases, the objective is exclusively open-loop and does not take into account the interaction between the controller and the system dynamics. In this paper, on the other hand, we consider the problem of optimizing the closed-loop trajectory directly by employing a backpropagation-based scheme.

The idea of using backpropagation to improve closed-loop performance of MPC first appeared in and. However, in these works, the authors focused on linear dynamics and simple MPC schemes with no state constraints, without providing formal convergence guarantees. In this paper, we greatly extend the backpropagation framework, primarily by considering nonlinear system dynamics, nonconvex closed-loop objectives, and by allowing the MPC scheme to contain elements that depend on the current state of the system and / or on the MPC solution computed in the previous time-step.

The contributions of this paper can be summarized as follows.

## Conclusion

In this paper, we proposed a backpropagation algorithm to optimally design an MPC scheme to maximize closed-loop performance. The cost and the constraints in the MPC can depend on the current state of the system, as well as on past solutions of previous MPC problems. This allows, for example, the utilization of the successive linearization strategy.

We employed conservative Jacobians to compute the sensitivity of the closed-loop trajectory with respect to variations of the design parameter. Leveraging a non-smooth version of the implicit function theorem, we derived sufficient conditions under which the gradient-based optimization procedure converges to a critical point of the problem.
