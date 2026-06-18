Control Barrier Functions: Theory and Applications

Topics include Robotics, Control barrier functions, Safety, Optimization, Control.

This paper provides an introduction and overview of recent work on control barrier functions and their use to verify and enforce safety properties in the context of (optimization based) safety-critical controllers. We survey the main technical results and discuss applications to several domains including robotic systems.

## Introduction

It is easy to agree that any engineered system should be designed to be *safe*. In fact, the term *safety-critical* system is many times used to distinguish those systems for which safety is a major design consideration. But what exactly is *safety*? How do we define it and how can we design systems to achieve it? The notion of safety was first introduced in 1977 in the context of program correctness by Leslie Lamport and formalized , see also.

The objective of this paper is to refocus the discussion on safety by introducing control barrier functions that play a role equivalent to Lyapunov functions in the study of liveness properties. There are two main reasons driving a surge in research related to safety and control barrier functions: 1) the recent interest in autonomous systems has brought safety to the forefront of systems' design.

## I-A Brief History of Barrier Functions

The study of safety in the context of dynamical systems dates back to the 1940's when Nagumo provided necessary and sufficient conditions for set invariance (see for a more detailed historical account, and for a modern proof).

These conditions have been independently re-discovered on multiple occasions; in particular, around the 1970s by Bony and Brezis (the proof in follows Brezis).
