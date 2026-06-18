Control Barrier Functions: Theory and Applications

Topics include Robotics, Control barrier functions, Safety, Optimization, Control.

This paper provides an introduction and overview of recent work on control barrier functions and their use to verify and enforce safety properties in the context of (optimization based) safety-critical controllers. We survey the main technical results and discuss applications to several domains including robotic systems.

## Introduction

It is easy to agree that any engineered system should be designed to be *safe*. In fact, the term *safety-critical* system is many times used to distinguish those systems for which safety is a major design consideration. But what exactly is *safety*? How do we define it and how can we design systems to achieve it? The notion of safety was first introduced in 1977 in the context of program correctness by Leslie Lamport and formalized in, see also....

The objective of this paper is to refocus the discussion on safety by introducing control barrier functions that play a role equivalent to Lyapunov functions in the study of liveness properties. There are two main reasons driving a surge in research related to safety and control barrier functions: 1) the recent interest in autonomous systems has brought safety to the forefront of systems' design....

## Conclusions

This paper presented a summary of recent results in safety-critical control based upon a novel form of control barrier functions. The basis theoretic foundations of this formulation were reviewed, all with selected application domains. Due to the recent activity in this domain, and the pressing need for safety in the context of autonomous systems, the authors imagine control barrier functions to become an essential component of modern control system design.

Given the affine control system, assume $f{(x)}$ and $g{(x)}$ are polynomials. Let $\rho{(x)}$ be a polynomial performance function and let $\beta{(x)}$ be a polynomial nominal controller. A polynomial $h{(x)}$ is a CBF if there exists positive constants ${a > 0},{\epsilon > 0}$ and SOS polynomials $s_{1}{(x)}$, $s_{2}{(x)}$ such that

### Remark 5

Thus, an exponential CBF can be designed using classical pole placement strategies from linear feedback theory. The location of the poles is specified to be both real and negative as well as dependent on the higher time-derivatives of the barrier function at initial time.

### I-A Brief History of Barrier Functions

The study of safety in the context of dynamical systems dates back to the 1940's when Nagumo provided necessary and sufficient conditions for set invariance (see for a more detailed historical account, and for a modern proof)....
