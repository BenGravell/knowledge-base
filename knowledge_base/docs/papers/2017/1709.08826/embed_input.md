Sensing-Constrained LQG Control

Linear-Quadratic-Gaussian (LQG) control is concerned with the design of an optimal controller and estimator for linear Gaussian systems with imperfect state information. Standard LQG assumes the set of sensor measurements, to be fed to the estimator, to be given. However, in many problems, arising in networked systems and robotics, one may not be able to use all the available sensors, due to power or payload constraints, or may be interested in using the smallest subset of sensors that guarantees the attainment of a desired control goal. In this paper, we introduce the sensing-constrained LQG control problem, in which one has to jointly design sensing, estimation, and control, under given constraints on the resources spent for sensing. We focus on the realistic case in which the sensing strategy has to be selected among a finite set of possible sensing modalities. While the computation of the optimal sensing strategy is intractable, we present the first scalable algorithm that computes a near-optimal sensing strategy with provable sub-optimality guarantees....

## Introduction

Traditional approaches to control of systems with partially observable state assume the choice of sensors used to observe the system is given. The choice of sensors usually results from a preliminary design phase in which an expert designer selects a suitable sensor suite that accommodates estimation requirements (e.g., observability, desired estimation error) and system constraints (e.g., size, cost). Modern control applications, from large networked systems to miniaturized robotics systems, pose serious limitations to the applicability of this traditional paradigm....

Motivated by these applications, in this paper we consider the problem of jointly designing control, estimation, and sensor selection for a system with partially observable state.

## Concluding Remarks

In this paper, we introduced the *sensing-constrained LQG control* Problem 1. ‣ Control policies ‣ II Sensing-Constrained LQG Control ‣ Sensing-Constrained LQG Control"), which is central in modern control applications that range from large-scale networked systems to miniaturized robotics networks. While the computation of the optimal sensing strategy is intractable, We provided the first scalable algorithm for Problem 1....

We prove that Algorithm 1 is the first scalable algorithm for the joint sensing and control design Problem 1. ‣ Control policies ‣ II Sensing-Constrained LQG Control ‣ Sensing-Constrained LQG Control"), and that it achieves a value for the LQG cost function in eq. (5. ‣ Control policies ‣ II Sensing-Constrained LQG Control ‣ Sensing-Constrained LQG Control")) that is finitely close to the optimal. We start by introducing the notion of supermodularity ratio (Section IV-A), which will enable to bound the sub-optimality gap of Algorithm 1 (Section IV-B).

The control gain matrices $K_{1},K_{2},\ldots,K_{T}$ are the same as the ones that make the controllers $(K_{1}x_{1}$, $K_{1}x_{2},\ldots,K_{T}x_{T})$ optimal for the perfect state-information version of Problem 1. ‣ Control policies ‣ II Sensing-Constrained LQG Control ‣ Sensing-Constrained LQG Control"), where the state $x_{t}$ is known to the controllers \[19, Chapter 4\].

Theorem 2. ‣ IV-B Performance Analysis for Algorithm 1 ‣ IV Performance Guarantees for Joint Sensing and Control Design ‣ Sensing-Constrained LQG Control") ensures that Algorithm 1 is the first scalable algorithm for the...
