Crocoddyl: An Efficient and Versatile Framework for Multi-Contact Optimal Control

Topics include Trajectory optimization, Differential dynamic programming, Multi-contact, Legged robots, Optimal control, Feasibility-driven differential dynamic programming, Open source.

Introduces Crocoddyl, an open-source multi-contact trajectory optimization library built on Feasibility-driven DDP (FDDP). FDDP accepts infeasible initial trajectories and keeps shooting gaps open during early iterations, achieving faster convergence and higher reliability than standard DDP for legged robot tasks.

We introduce Crocoddyl (Contact RObot COntrol by Differential DYnamic Library), an open-source framework tailored for efficient multi-contact optimal control. Crocoddyl efficiently computes the state trajectory and the control policy for a given predefined sequence of contacts. Its efficiency is due to the use of sparse analytical derivatives, exploitation of the problem structure, and data sharing. It employs differential geometry to properly describe the state of any geometrical system, e.g. floating-base systems. Additionally, we propose a novel optimal control algorithm called Feasibility-driven Differential Dynamic Programming (FDDP). Our method does not add extra decision variables which often increases the computation time per iteration due to factorization. FDDP shows a greater globalization strategy compared to classical Differential Dynamic Programming (DDP) algorithms. Concretely, we propose two modifications to the classical DDP algorithm. First, the backward pass accepts infeasible state-control trajectories. Second, the rollout keeps the gaps open during the early "exploratory" iterations (as expected in multiple-shooting methods with only equality constraints).

## Introduction

Multi-contact optimal control promises to generate whole-body motions and control policies that allow legged robots to robustly react to unexpected events in real-time. It has several advantages compared with state-of-the-art frameworks (e.g. ) in which a whole-body controller (e.g. ) compliantly tracks an optimized Centroidal dynamics trajectory (e.g. ) with optionally an optimized contact plan (e.g. ). For instance, they cannot properly handle the robot orientation, particularly during flight phases due to the nonholonomic effect on the dynamics, and to regulate the angular momentum to zero leads to tracking errors even in walking motions.

Recent work on optimal control has shown that nonlinear Model Predictive Control (MPC) is plausible for controlling legged robots in real-time. All these methods have in common that they solve the nonlinear Optimal Control (OC) problem by iteratively building and solving a Linear-Quadratic Regulator (LQR) problem (i.e. DDP with Gauss-Newton approximation ). These frameworks use numerical or automatic differentiation which is often inefficient compared to sparse and analytical derivatives. Furthermore, they do not explicitly handle the geometric structure of legged systems which include elements of ${\mathbb{S}}{\mathbb{E}}{}$.

## I-A Contribution

We propose a novel and efficient framework for multi-contact OC called Crocoddyl. Our framework efficiently solves this problem by employing sparse and analytical derivatives of the contact and impulse dynamics. The OC solver properly handles the geometry of rigid bodies using dedicated numerical routines for Lie groups and their derivatives. Indeed, we model the floating-base as a ${\mathbb{S}}{\mathbb{E}}{}$ element, needed for example for the generation of front-flip motions.

## Conclusion

We presented a novel and efficient framework for multi-contact optimal control. The gap contraction of FDDP is equivalent to direct multiple-shooting formulations with only equality constraints (i.e. the Newton method applied to the KKT conditions). However, and in contrast to classical multiple-shooting, FDDP does not add extra decision variables which often increases the computation time per iteration due to factorization; it has cubic complexity in matrix dimension. FDDP also improves the poor globalization strategy of classical DDP methods.
