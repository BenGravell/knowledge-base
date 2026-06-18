Approximation of the Joint Spectral Radius Using Sum of Squares

Topics include Joint spectral radius, Sum of squares, Lyapunov functions, Semidefinite programming, Switched systems, Approximation bounds.

Uses sum-of-squares polynomial Lyapunov functions to approximate the joint spectral radius of a set of matrices. The paper gives asymptotically tight approximation bounds and connects computational SDP relaxations to stability analysis for switched systems.

We provide an asymptotically tight, computationally efficient approximation of the joint spectral radius of a set of matrices using sum of squares (SOS) programming. The approach is based on a search for an SOS polynomial that proves simultaneous contractibility of a finite set of matrices. We provide a bound on the quality of the approximation that unifies several earlier results and is independent of the number of matrices. Additionally, we present a comparison between our approximation scheme and earlier techniques, including the use of common quadratic Lyapunov functions and a method based on matrix liftings. Theoretical results and numerical investigations show that our approach yields tighter approximations.

## Introduction

Stability of discrete linear inclusions has been a topic of major research over the past two decades. Such systems can be represented as a switched linear system of the form ${x{({k + 1})}} = {A_{\sigma{(k)}}x{(k)}}$, where $\sigma$ is a mapping from the integers to a given set of indices. The above model, and its many variations, has been studied extensively across multiple disciplines including control theory, theory of non-negative matrices and Markov chains, subdivision schemes and wavelet theory, dynamical systems, etc.

and represents the maximum growth rate that can be achieved by taking arbitrary products of the matrices $A_{i}$. As in the case of the classical spectral radius, the value of this expression is independent of the choice of norm . Daubechies and Lagarias conjectured that the joint spectral radius is equal to a related quantity, the generalized spectral radius, which is defined in a similar way except for the fact that the norm of the product is replaced by the spectral radius. Berger and Wang proved this conjecture to be true for finite sets of matrices.

Ando and Shih describe a constructive procedure for generating a set of $m$ matrices whose joint spectral radius is equal to $\frac{1}{\sqrt{m}}$, but for which no quadratic Lyapunov function exists. They prove that the interval $\lbrack 0,\frac{1}{\sqrt{m}})$ is effectively the "optimal" range for the joint spectral radius necessary to guarantee simultaneous contractibility under an ellipsoidal norm for a finite collection of $m$ matrices.

In this paper, we develop a sum of squares (SOS) based scheme for the approximation of the joint spectral radius. The method computes, using the techniques of semidefinite programming, a homogeneous polynomial that serves as a Lyapunov-like function for the corresponding switched linear system. We prove several results on the quality of approximation of the proposed scheme. In particular, it will follow from Theorems 10 and 4.3 that our SOS-based approximation $\rho_{{SOS},{2d}}$ satisfies
