A Family of Iterative Gauss-Newton Shooting Methods for Nonlinear Optimal Control

Topics include Trajectory optimization, Multiple shooting, Gauss-Newton methods, Nonlinear optimal control, Iterative linear quadratic regulator, iLQR.

Presents a unified family of iterative Gauss-Newton multiple-shooting methods for nonlinear optimal control, covering single and multiple shooting variants within a common framework with analysis of convergence and computational tradeoffs.

This paper introduces a family of iterative algorithms for unconstrained nonlinear optimal control. We generalize the well-known iLQR algorithm to different multiple-shooting variants, combining advantages like straight-forward initialization and a closed-loop forward integration. All algorithms have similar computational complexity, i.e. linear complexity in the time horizon, and can be derived in the same computational framework. We compare the full-step variants of our algorithms and present several simulation examples, including a high-dimensional underactuated robot subject to contact switches. Simulation results show that our multiple-shooting algorithms can achieve faster convergence, better local contraction rates and much shorter runtimes than classical iLQR, which makes them a superior choice for nonlinear model predictive control applications.

## Introduction

### I-A Overview and Motivation

In this paper, we discuss a family of iterative Gauss-Newton shooting methods for numerically solving unconstrained optimal control problems, and illustrate the effectiveness of our algorithms with various robotics examples. We outline the connection between a number of 'direct' optimal control methods and Gauss-Newton methods from the class of Differential Dynamic Programming (DDP) algorithms. Additionally, we present a natural extension arising from this connection and introduce a family of hybrid Gauss-Newton Multiple Shooting methods.

The focus of this paper is on unconstrained optimal control problems without general (in)equality path constraints. It is obvious that the lifting approach naturally transfers to equality-constrained variants of iLQR, such as. The inclusion of general (in)equality path constraints is part of ongoing work. One option to include them in the existing framework is to replace the standard Riccati backward sweep with a dedicated solver for constrained LQ optimal control problems. In this way, general (in)equality path constraints can be included while keeping linear time-complexity.

While this work treats algorithms using a Gauss-Newton Hessian approximation, it similarly transfers to exact-Hessian approaches, resulting in a multiple-shooting DDP algorithm combining the advantages of simultaneous methods, quadratic convergence and closed-loop integration.

TABLE I: An overview of different GNMS-type methods.

for $n \in {0,\ldots,{N - 1}}$. For the final time-step $N$ we obtain the terminal conditions $\mathbf{S}_{N} = \mathbf{Q}_{N}$, $\mathbf{s}_{N} = \mathbf{q}_{N}$ and $s_{N} = q_{N}$, and the recursion is subsequently swept backwards. Note that Equation does not contribute to the control update and can therefore be omitted in practice.

are not the same. In this example, GNMS and GNMS show better contraction than iLQR. Asymptotic contraction rates are investigated in more detail in Section IV-C.

In direct approaches to optimal control, infinite-dimensional optimal control problems are transcribed into finite dimensional Nonlinear Programs (NLPs). Two prominent ways of transcription by 'shooting' are direct single shooting (SS) and direct multiple shooting (MS), which differ in the choice of decision variables....
