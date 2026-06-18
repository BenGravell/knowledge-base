On Symplectic Optimization

Topics include Optimization, Learning, Machine learning.

Accelerated gradient methods have had significant impact in machine learning - in particular the theoretical side of machine learning - due to their ability to achieve oracle lower bounds. But their heuristic construction has hindered their full integration into the practical machine-learning algorithmic toolbox, and has limited their scope. In this paper we build on recent work which casts acceleration as a phenomenon best explained in continuous time, and we augment that picture by providing a systematic methodology for converting continuous-time dynamics into discrete-time algorithms while retaining oracle rates. Our framework is based on ideas from Hamiltonian dynamical systems and symplectic integration. These ideas have had major impact in many areas in applied mathematics, but have not yet been seen to have a relationship with optimization.

## Introduction

Optimization theory has played an increasingly central role in the development of machine learning in recent years. This has happened not only because optimization theory supplies algorithms and convergence rates for learning algorithms, but also because it supplies lower bounds, and hence fundamental understanding. A milestone in this regard was the discovery by Nemirovskii & Yudin of oracle lower bounds for gradient-based optimization, and the ensuing derivation by Nesterov of an "accelerated gradient descent" (AGD) algorithm whose rate is provably better than that of gradient descent, and which matches the oracle lower bound.

In the current paper we show how to apply symplectic integration to gradient-based optimization. Our approach is cast in a Hamiltonian framework, obtained from the Bregman-Lagrangian framework via a Legendre transformation. This Hamiltonian is time-varying, a fact that we address via a lifting procedure. We then show how to derive a symplectic integrator from the lifted Hamiltonian. The end result is a fully generative mathematical pipeline, from problem specification to discrete-time accelerated algorithm. Our algorithms are related to Nesterov's algorithms, but they are *not* exactly the same, and the differences are interesting.

## Discussion

Wibisono et al. introduced a dynamical system that converged to the minimum of a given objective function at the same rate as accelerated Nesterov methods. Moreover, by carefully discretizing the Lagrangian representation of these dynamics they were able to explicitly derive entire families of known accelerated Nesterov discretizations. Given the dynamical system itself, however, discretization is more systematically achieved by considering the Hamiltonian view of the system and appealing to symplectic integrators.

In particular, this systematic approach allows us to isolate the effects of the dynamics from other modifications, such as the gradient flow added to stabilize the original discretization of the Lagrangian representation of the dynamics. This separation then allows us to analyze the performance of the latent Bregman dynamics and that of any amendments independently.
