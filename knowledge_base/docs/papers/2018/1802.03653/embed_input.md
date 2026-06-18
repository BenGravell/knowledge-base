On Symplectic Optimization

Topics include Optimization, Learning, Machine learning.

Accelerated gradient methods have had significant impact in machine learning - in particular the theoretical side of machine learning - due to their ability to achieve oracle lower bounds. But their heuristic construction has hindered their full integration into the practical machine-learning algorithmic toolbox, and has limited their scope. In this paper we build on recent work which casts acceleration as a phenomenon best explained in continuous time, and we augment that picture by providing a systematic methodology for converting continuous-time dynamics into discrete-time algorithms while retaining oracle rates. Our framework is based on ideas from Hamiltonian dynamical systems and symplectic integration. These ideas have had major impact in many areas in applied mathematics, but have not yet been seen to have a relationship with optimization.

## Introduction

Optimization theory has played an increasingly central role in the development of machine learning in recent years. This has happened not only because optimization theory supplies algorithms and convergence rates for learning algorithms, but also because it supplies lower bounds, and hence fundamental understanding. A milestone in this regard was the discovery by Nemirovskii & Yudin of oracle lower bounds for gradient-based optimization, and the ensuing derivation by Nesterov of an "accelerated gradient descent" (AGD) algorithm whose rate is provably better than that of gradient descent, and which matches the oracle lower bound.

A flurry of mathematical and algorithmic results have followed in the wake of these seminal discoveries from the 1980's, but even after three decades there remains a lack of understanding of the general acceleration phenomenon. In particular, a theoretical framework that can *generate* accelerated methods has not yet emerged. Recent progress in this regard has been achieved by considering continuous-time analogs of acceleration methods. Notably, Wibisono et al....

Unfortunately, the introduction of Hamiltonian symplectic integrators also complicates the formal analysis of Hamiltonian optimization itself. For example, the accuracy of leapfrog integrators comes from cancellations in their symmetric updates, but any individual update can have large error. Hence we cannot expect to be able to bound convergence term-by-term. Indeed the stability of symplectic integrators is a global property---the discretized dynamics oscillate around the true dynamics and discrete updates will in general deviate away from the exact dynamics before finally returning....

Ultimately, however, the direct window into Bregman dynamics provided by their Hamiltonian representation and corresponding symplectic integration enables not only a better understanding of existing accelerated Nesterov methods but also a principled way of developing new implementations and generalizations.

Symplectic integrators are naturally constructed by splitting the Hamiltonian into component Hamiltonians whose dynamics can be solved exactly, or at least sufficiently close to exactly numerically, and then composing those dynamics together symmetrically. For example, consider the splitting

we can invert this relationship to give
