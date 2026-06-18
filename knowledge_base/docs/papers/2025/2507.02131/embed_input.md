Perturbed Gradient Descent Algorithms Are Small-Disturbance Input-to-State Stable

Topics include Gradient descent, Policy gradients, Lyapunov methods, Stability analysis, Robustness, Online algorithms, ISS, PL.

This article investigates the robustness of gradient descent algorithms under perturbations. The concept of small-disturbance input-to-state stability (ISS) for discrete-time nonlinear dynamical systems is introduced, along with its Lyapunov characterization. The conventional linear Polyak-Lojasiewicz (PL) condition is then extended to a nonlinear version, and it is shown that the gradient descent algorithm is small-disturbance ISS provided the objective function satisfies the generalized nonlinear PL condition. This small-disturbance ISS property guarantees that the gradient descent algorithm converges to a small neighborhood of the optimum under sufficiently small perturbations. As a direct application of the developed framework, we demonstrate that the LQR cost satisfies the generalized nonlinear PL condition, thereby establishing that the policy gradient algorithm for LQR is small-disturbance ISS. Additionally, other popular policy gradient algorithms, including natural policy gradient and Gauss-Newton method, are also proven to be small-disturbance ISS.

## Introduction

Gradient-based optimization algorithms are a cornerstone of machine learning's success, as they efficiently navigate high-dimensional variable spaces to identify suitable extrema for objective function optimization. For instance, gradient descent and adaptive moment estimation (Adam) \[\] are among the most widely used first-order gradient-based optimizers in deep learning. Consequently, the convergence analysis of gradient descent algorithms is crucial for understanding and improving their performance. While such analyses typically assume exact gradient information, in practice, gradient computations are often subject to perturbations....

A solution to better understanding optimization is to consider gradient-based algorithms as dynamical systems. This perspective enables the application of tools and concepts from control theory, such as Lyapunov stability, to analyze the behavior of optimization algorithms. However, Lyapunov stability primarily examines a system's behavior in the absence of external inputs, making it less suitable for analyzing the convergence and robustness of gradient-based methods subject to external perturbations....

## Conclusions

This article introduces the concept of small-disturbance ISS as a unified framework for analyzing the robustness of gradient descent algorithms. Small-disturbance ISS provided a systematic approach to quantify the transient behavior, convergence speed, and robustness of gradient descent algorithms under perturbations. By generalizing the classical linear PL condition to a nonlinear version, referred to as the $\mathcal{K}$-PL condition, we show that gradient descent algorithms are small-disturbance ISS, provided the objective function satisfies the $\mathcal{K}$-PL condition....

## Application to LQR Problem

This section applies the concept of small-disturbance ISS to analyze the gradient descent algorithm for solving the constrained nonlinear program:

Hence, the proof is completed by \[, Lemma 1.2.2\].

In this paper, we aim to establish a connection between the ISS of gradient descent algorithms and the *Polyak-Łojasiewicz (PL)* type condition. The PL condition has been shown to be a sufficient condition for the linear convergence rate of gradient descent, even without assuming the convexity of the objective function....
