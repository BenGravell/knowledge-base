Coherence-based Approximate Derivatives via Web of Affine Spaces Optimization

Computing derivatives is a crucial subroutine in computer science and related fields as it provides a local characterization of a function's steepest directions of ascent or descent. In this work, we recognize that derivatives are often not computed in isolation; conversely, it is quite common to compute a \textit{sequence} of derivatives, each one somewhat related to the last. Thus, we propose accelerating derivative computation by reusing information from previous, related calculations-a general strategy known as \textit{coherence}. We introduce the first instantiation of this strategy through a novel approach called the Web of Affine Spaces (WASP) Optimization. This approach provides an accurate approximation of a function's derivative object (i.e. gradient, Jacobian matrix, etc.) at the current input within a sequence. Each derivative within the sequence only requires a small number of forward passes through the function (typically two), regardless of the number of function inputs and outputs. We demonstrate the efficacy of our approach through several numerical experiments, comparing it with alternative derivative computation methods on benchmark functions....

## Introduction

Mathematical derivatives are fundamental to much of science. At a high level, derivatives offer a local characterization of a function's steepest ascent or descent directions. In practice, this property is frequently employed in numerical optimization, where derivatives guide the iterative process of navigating downhill through the landscape of a function \[\]. For example, derivative-based optimization is widely used in robotics for tasks such as inverse kinematics, trajectory optimization, physics simulation, control, learning, and constrained planning.

Since derivative computation often takes place within a tight, low-level loop in the application stack, the speed of this process is critical to maintaining sufficient performance. For example, consider a legged robot using a derivative-based model predictive control (MPC) algorithm to maintain balance. If the robot is nudged, it must compute derivatives very rapidly to guide the optimization process and allow the real-time reactive actuations of its legs to stay upright.

### IX-B Implications

Due to the ubiquity of derivative computation in robotics and beyond, we believe our work has the potential for broad impact and applicability. For example, it could prove to be valuable in areas such as model predictive control, physics simulation, trajectory optimization, inverse kinematics, and more. Our goal is to enable the community to leverage these derivatives to streamline computationally expensive subroutines, achieving performance gains with minimal code modifications....

A ground truth JVP, $\Delta\mathbf{f}_{i}$, is computed in the direction $\Delta\mathbf{x}_{i}$ at the given input $\mathbf{x}_{k}$ using Equation.

This constrained optimization best matches the intersection of the web of affine spaces, specified in the objective function, while also restricting the solution to lie on the affine solution space, specified in the constraint.

Web of Affine Spaces Optimization with random, non-orthonormal $\Delta\mathbf{X}$ matrix and NumPy \[\] backend (abbreviated as WASP-NO).

As we will discuss in §II, there are several standard techniques to calculate the derivatives of a function \[\]. These techniques generally involve repeatedly evaluating the function with slightly modified arguments, observing the resulting perturbations in the function's input or output space, and...
