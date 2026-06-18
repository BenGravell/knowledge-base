Stabilizing Dynamical Systems via Policy Gradient Methods

Topics include Policy gradients, Stabilization, Dynamical systems, Linear quadratic regulator, Model-free control, Reinforcement learning, Nonlinear systems.

Shows that direct policy search can be used to find stabilizing controllers without starting from an already-stabilizing policy. The method follows a continuation path through discounted LQR problems, increasing the discount factor until it recovers a stabilizing controller for linear systems and locally for smooth nonlinear systems.

Stabilizing an unknown control system is one of the most fundamental problems in control systems engineering. In this paper, we provide a simple, model-free algorithm for stabilizing fully observed dynamical systems. While model-free methods have become increasingly popular in practice due to their simplicity and flexibility, stabilization via direct policy search has received surprisingly little attention. Our algorithm proceeds by solving a series of discounted LQR problems, where the discount factor is gradually increased. We prove that this method efficiently recovers a stabilizing controller for linear systems, and for smooth, nonlinear systems within a neighborhood of their equilibria. Our approach overcomes a significant limitation of prior work, namely the need for a pre-given stabilizing control policy. We empirically evaluate the effectiveness of our approach on common control benchmarks.

## Introduction

Stabilizing an unknown control system is one of the most fundamental problems in control systems engineering. A wide variety of tasks - from maintaining a dynamical system around a desired equilibrium point, to tracking a reference signal (e.g a pilot's input to a plane) - can be recast in terms of stability. More generally, synthesizing an initial stabilizing controller is often a necessary first step towards solving more complex tasks, such as adaptive or robust control design.

In this work, we consider the problem of finding a stabilizing controller for an unknown dynamical system via direct policy search methods. We introduce a simple procedure based off policy gradients which provably stabilizes a dynamical system around an equilibrium point. Our algorithm only requires access to a simulator which can return rollouts of the system under different control policies, and can efficiently stabilize both linear and smooth, nonlinear systems.

## Discussion

This works illustrates how one can provably stabilize a broad class of dynamical systems via a simple model-free procedure based off policy gradients. In line with the simplicity and flexibility that have made model-free methods so popular in practice, our algorithm works under relatively weak assumptions and with little knowledge of the underlying dynamics. Furthermore, we solve an open problem from previous work and take a step towards placing model-free methods on more solid theoretical footing. We believe that our results raise a number of interesting questions and directions for future work.

In particular, our theoretical analysis states that discount annealing returns a controller whose stability properties are similar to those of the optimal LQR controller for the system's Jacobian linearization. We were therefore quite surprised when in experiments, the resulting controller had a significantly better radius of attraction than the exact optimal LQR and $\mathcal{H}_{\infty}$ controllers for the linearization of the dynamics.
