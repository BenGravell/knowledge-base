Regret Lower Bounds for Learning Linear Quadratic Gaussian Systems

TWe establish regret lower bounds for adaptively controlling an unknown linear Gaussian system with quadratic costs. We combine ideas from experiment design, estimation theory and a perturbation bound of certain information matrices to derive regret lower bounds exhibiting scaling on the order of magnitude sqrt(T) in the time horizon T. Our bounds accurately capture the role of control-theoretic parameters and we are able to show that systems that are hard to control are also hard to learn to control; when instantiated to state feedback systems we recover the dimensional dependency of earlier work but with improved scaling with system-theoretic constants such as system costs and Gramians. Furthermore, we extend our results to a class of partially observed systems and demonstrate that systems with poor observability structure also are hard to learn to control.

## Introduction

Learning algorithms are set to play an increasing role in modern engineering solutions. Early successes include walking robots and playing repeated games such as Go and are likely to become increasingly important in modern safety-critical infrastructure such as smart grids and intelligent transportation. However, their emergence in safety-critical systems is not without problems. Indeed, one of the hallmarks of these early successes is abundant data from a relatively unchanging source, potentially even through simulation access.

Such an understanding must necessarily be based on two components: *i.* the study of fundamental performance limitations, which no algorithm can excede, and *ii.* the provision of algorithms which match these fundamental limitations. In this work, we focus on the first component and provide an information-theoretic framework for understanding the fundamental limits of adaptive controlling an a priori unknown linear Gaussian system subject to a quadratic cost function.

## Problem Formulation

We

We will also consider the extension to partially observed systems, in which the controller is constrained to rely on past and present observations of the form
