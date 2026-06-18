Global Convergence of Policy Gradient Methods for the Linear Quadratic Regulator

Topics include Convex optimization, Policy gradients, Reinforcement learning, Optimal control, System identification, Optimization, Planning, Control, Learning, Linear quadratic regulator, Gradient method.

Direct policy gradient methods for reinforcement learning and continuous control problems are a popular approach for a variety of reasons: 1) they are easy to implement without explicit knowledge of the underlying model 2) they are an "end-to-end" approach, directly optimizing the performance metric of interest 3) they inherently allow for richly parameterized policies. A notable drawback is that even in the most basic continuous control problem (that of linear quadratic regulators), these methods must solve a non-convex optimization problem, where little is understood about their efficiency from both computational and statistical perspectives. In contrast, system identification and model based planning in optimal control theory have a much more solid theoretical footing, where much is known with regards to their computational and statistical properties. This work bridges this gap showing that (model free) policy gradient methods globally converge to the optimal solution and are efficient (polynomially so in relevant problem dependent quantities) with regards to their sample and computational complexities.

## Introduction

Recent years have seen major advances in the control of uncertain dynamical systems using reinforcement learning and data-driven approaches; examples range from allowing robots to perform more sophisticated controls tasks such as robotic hand manipulation, to sequential decision making in game domains, e.g., AlphaGo and Atari game playing. Deep reinforcement learning (DeepRL) is becoming increasingly popular for tackling such challenging sequential decision making problems.

Many of these successes have relied on sampling based reinforcement learning algorithms such as policy gradient methods, including the DeepRL approaches. For these approaches, there is little theoretical understanding of their efficiency, either from a statistical or a computational perspective. In contrast, control theory (optimal and adaptive control) has a rich body of tools, with provable guarantees, for related sequential decision making problems, particularly those that involve continuous control.

This work builds bridges between these two lines of work, namely, between optimal control theory and sample based reinforcement learning methods, using ideas from mathematical optimization.

## The optimal control problem

In the standard optimal control problem, a dynamical system is described as
