A Family of Iterative Gauss-Newton Shooting Methods for Nonlinear Optimal Control

Topics include Trajectory optimization, Multiple shooting, Gauss-Newton methods, Nonlinear optimal control, Iterative linear quadratic regulator, iLQR.

Presents a unified family of iterative Gauss-Newton multiple-shooting methods for nonlinear optimal control, covering single and multiple shooting variants within a common framework with analysis of convergence and computational tradeoffs.

This paper introduces a family of iterative algorithms for unconstrained nonlinear optimal control. We generalize the well-known iLQR algorithm to different multiple-shooting variants, combining advantages like straight-forward initialization and a closed-loop forward integration. All algorithms have similar computational complexity, i.e. linear complexity in the time horizon, and can be derived in the same computational framework. We compare the full-step variants of our algorithms and present several simulation examples, including a high-dimensional underactuated robot subject to contact switches. Simulation results show that our multiple-shooting algorithms can achieve faster convergence, better local contraction rates and much shorter runtimes than classical iLQR, which makes them a superior choice for nonlinear model predictive control applications.

## I-A Overview and Motivation

In this paper, we discuss a family of iterative Gauss-Newton shooting methods for numerically solving unconstrained optimal control problems, and illustrate the effectiveness of our algorithms with various robotics examples. We outline the connection between a number of 'direct' optimal control methods and Gauss-Newton methods from the class of Differential Dynamic Programming (DDP) algorithms. Additionally, we present a natural extension arising from this connection and introduce a family of hybrid Gauss-Newton Multiple Shooting methods.

## Conclusion and Outlook

In this paper, we have shown how the well-known iLQR algorithm can be lifted and transformed into Gauss-Newton Multiple Shooting, GNMS. We have generalized the concept to form a family of Gauss-Newton shooting algorithms, which can be distinguished into sequential and simultaneous algorithms and closed and open-loop algorithms. Some algorithms partially overwrite decision variables by means of a numeric forward integration. All presented variants have approximately the same computational cost and feature linear time-complexity.

We have compared the performance of the algorithms in different simulation experiments, which indicate that the lifted algorithms can outperform classical iLQR. While not included in this paper for reasons of compactness, similar results were obtained for other rigid-body dynamic systems including a 6 DoF fixed-base arm model. A more fundamental investigation for formalizing the conditions that result in improved convergence rates for GNMS($M$) and iLQR-GNMS($M$) is subject to ongoing work.

The focus of this paper is on unconstrained optimal control problems without general (in)equality path constraints. It is obvious that the lifting approach naturally transfers to equality-constrained variants of iLQR, such as. The inclusion of general (in)equality path constraints is part of ongoing work. One option to include them in the existing framework is to replace the standard Riccati backward sweep with a dedicated solver for constrained LQ optimal control problems. In this way, general (in)equality path constraints can be included while keeping linear time-complexity.
