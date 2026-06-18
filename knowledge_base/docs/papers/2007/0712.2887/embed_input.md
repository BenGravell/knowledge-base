Approximation of the Joint Spectral Radius Using Sum of Squares

Topics include Joint spectral radius, Sum of squares, Lyapunov functions, Semidefinite programming, Switched systems, Approximation bounds.

Uses sum-of-squares polynomial Lyapunov functions to approximate the joint spectral radius of a set of matrices. The paper gives asymptotically tight approximation bounds and connects computational SDP relaxations to stability analysis for switched systems.

We provide an asymptotically tight, computationally efficient approximation of the joint spectral radius of a set of matrices using sum of squares (SOS) programming. The approach is based on a search for an SOS polynomial that proves simultaneous contractibility of a finite set of matrices. We provide a bound on the quality of the approximation that unifies several earlier results and is independent of the number of matrices. Additionally, we present a comparison between our approximation scheme and earlier techniques, including the use of common quadratic Lyapunov functions and a method based on matrix liftings. Theoretical results and numerical investigations show that our approach yields tighter approximations.

## Introduction

Stability of discrete linear inclusions has been a topic of major research over the past two decades. Such systems can be represented as a switched linear system of the form ${x{({k + 1})}} = {A_{\sigma{(k)}}x{(k)}}$, where $\sigma$ is a mapping from the integers to a given set of indices. The above model, and its many variations, has been studied extensively across multiple disciplines including control theory, theory of non-negative matrices and Markov chains, subdivision schemes and wavelet theory, dynamical systems, etc....

and represents the maximum growth rate that can be achieved by taking arbitrary products of the matrices $A_{i}$. As in the case of the classical spectral radius, the value of this expression is independent of the choice of norm in. Daubechies and Lagarias \[\] conjectured that the joint spectral radius is equal to a related quantity, the generalized spectral radius, which is defined in a similar way except for the fact that the norm of the product is replaced by the spectral radius. Berger and Wang \[\] proved this conjecture to be true for finite sets of matrices....

We introduced a novel scheme for the approximation of the joint spectral radius of a set of matrices using sum of squares programming. The method is based on the use of a multivariate polynomial to provide a norm-like quantity under which all matrices are contractive. We provided an asymptotically tight estimate for the quality of the bound, which is independent of the number of matrices. We also proposed an alternative bound, that depends on the number $m$ of matrices, based on a generalization of a Lyapunov iteration.

Our results can be alternatively interpreted in a simpler way as providing a trajectory-preserving lifting to a higher dimensional space, and proving contractiveness with respect to an ellipsoidal norm in that space. In this case, a weaker estimate can be obtained by computing the spectral radius of a fixed matrix. These results generalize earlier work of Ando and Shih \[\], Blondel, Nesterov and Theys \[\], and provide an improvement over the lifting procedure of Blondel and Nesterov \[\]. The good performance of our procedure was also verified using numerical examples.

## Symmetric algebra and induced matrices

### Quality of approximation

### Theorem 4.1
