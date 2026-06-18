Robust Exploration in Linear Quadratic Reinforcement Learning

Topics include Convex optimization, Reinforcement learning, Robustness, Uncertainty, Optimization, Control, Learning.

This paper concerns the problem of learning control policies for an unknown linear dynamical system to minimize a quadratic cost function. We present a method, based on convex optimization, that accomplishes this task robustly: i.e., we minimize the worst-case cost, accounting for system uncertainty given the observed data. The method balances exploitation and exploration, exciting the system in such a way so as to reduce uncertainty in the model parameters to which the worst-case cost is most sensitive. Numerical simulations and application to a hardware-in-the-loop servo-mechanism demonstrate the approach, with appreciable performance and robustness gains over alternative methods observed in both.

## Introduction

Learning to make decisions in an uncertain and dynamic environment is a task of fundamental importance in a number of domains. Though it has been the subject of intense research activity since the formulation of the 'dual control problem' in the 1960s, the recent success of reinforcement learning (RL), particularly in games, has inspired a resurgence in interest in the topic. Problems of this nature require decisions to be made with respect to two objectives. First, there is a goal to be achieved, typically quantified as a reward function to be maximized.

It is important to recognize that the second objective (exploration) is important only in so far as it facilitates the first (maximizing reward); there is no intrinsic value in reducing uncertainty. As a consequence, exploration should be targeted or application specific; it should *not* excite the system arbitrarily, but rather in such a way that the information gathered is useful for achieving the goal. Furthermore, in many real-world applications, it is essential that exploration does not compromise the safe and reliable operation of the system.

This paper is concerned with control of uncertain linear dynamical systems, with the goal of maximizing (minimizing) rewards (costs) that are a quadratic function of states and actions; cf. §2 for a detailed problem formulation. We derive methods to synthesize control policies that balance the exploration/exploitation tradeoff by performing robust, targeted exploration: *robust* in the sense that we optimize for worst-case performance given uncertainty in our knowledge of the system, and *targeted* in the sense that the policy excites the system so as to reduce uncertainty in such a way that specifically minimizes the worst-case cost.

## Problem statement

In this section we describe in detail the problem addressed in this paper. Notation is as follows: $A^{\top}$ denotes the transpose of a matrix $A$. $x_{1:n}$ is shorthand for the sequence ${\{ x_{t}\}}_{t = 1}^{n}$. $\lambda_{\text{max}}{(A)}$ denotes the maximum eigenvalue of a matrix $A$. $\otimes$ denotes the Kronecker product. $\text{vec}(A)$ stacks the columns of $A$ to form a vector. ${\mathbb{S}}_{+}^{n}$ (${\mathbb{S}}_{+ +}^{n}$) denotes the cone(s) of $n \times n$ symmetric positive semidefinite (definite) matrices. w.p.
