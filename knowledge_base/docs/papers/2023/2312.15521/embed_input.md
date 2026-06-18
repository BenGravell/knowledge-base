BP-MPC: Optimizing the Closed-Loop Performance of MPC Using Backpropagation

Topics include Model predictive control, Backpropagation, Policy optimization, Differentiable control, Model predictive control tuning, Closed-loop performance.

Optimizes MPC costs and constraints by backpropagating closed-loop performance through linearized dynamics and MPC policies. The paper contributes a convergence-backed tuning procedure for improving closed-loop behavior, including a feasibility-loss extension for cases where the MPC problem can fail.

Model predictive control (MPC) is pervasive in research and industry. However, designing the cost function and the constraints of the MPC to maximize closed-loop performance remains an open problem. To achieve optimal tuning, we propose a backpropagation scheme that solves a policy optimization problem with nonlinear system dynamics and MPC policies. We enforce the system dynamics using linearization and allow the MPC problem to contain elements that depend on the current system state and on past MPC solutions. Moreover, we propose a simple extension that can deal with losses of feasibility. Our approach, unlike other methods in the literature, enjoys convergence guarantees.

## Introduction

In recent years, optimization-based control algorithms have become increasingly popular in industry and academia, in part thanks to the ever-growing computational power of CPUs, and the availability of fast numerical implementations. Arguably, the biggest appeal of optimization-based control techniques is their ability to explicitly account for process constraints in their formulation, allowing for an optimal and safe selection of the control inputs.

A well-known strategy, also commonly used in industry, is model predictive control (MPC). This technique enables feedback by repeatedly solving a numerical optimization problem at every time-step, each time taking into account the current (measured or estimated) state of the system.

We extended our framework to cases where the MPC problem becomes infeasible using nonsmooth penalty functions. We derived conditions under which the closed-loop is guaranteed to converge to a safe solution.

Current work focuses on deploying our optimization scheme on more realistic real-life examples. Future work will focus on extending our scheme to scenarios where the system dynamics are only partially known and / or affected by stochastic noise.

In our case, the closed loop dynamics can be expressed as a recursive equation

### Assumption 1

Following the strategy above, we can choose each $A_{k|t}$, $B_{k|t}$, and $c_{k|t}$ to be the linearization of $f$ and the approximation error evaluated along the state input-trajectory $(x_{t - 1},u_{t - 1})$:

Because of its effectiveness in practical applications, researchers have dedicated significant effort to the task of designing MPC controllers. For example, showed that the introduction of an appropriately selected terminal cost can ensure stability and feasibility of the closed-loop. More recently, proposed a design to ensures that the MPC behaves like a linear controller around a specified operating point, with the goal of inheriting the well-known stability and robustness properties of linear controllers. The objective function of an MPC can also be chosen to incentivise learning of an unknown model, as proposed in.

MPC design can be viewed as a policy optimization problem. Policy optimization is a well-known problem in reinforcement learning, where the goal is to obtain a control policy that minimizes some performance objective....
