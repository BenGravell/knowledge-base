Willems' Fundamental Lemma for State-Space Systems and Its Extension to Multiple Datasets

Topics include Willems' fundamental lemma, Data-driven control, Behavioral systems, State-space systems, Multiple datasets, Persistency of excitation, Missing data, Unstable systems.

Extends the fundamental lemma from one long trajectory to multiple shorter trajectories via collective persistency of excitation. This is important for practical data collection, missing samples, and unstable systems where one long persistently exciting run may be difficult or unsafe.

Willems et al.'s fundamental lemma asserts that all trajectories of a linear system can be obtained from a single given one, assuming that a persistency of excitation condition holds. This result has profound implications for system identification and data-driven control, and has seen a revival over the last few years. The purpose of this paper is to extend Willems' lemma to the situation where multiple (possibly short) system trajectories are given instead of a single long one. To this end, we introduce a notion of collective persistency of excitation. We will then show that all trajectories of a linear system can be obtained from a given finite number of trajectories, as long as these are collectively persistently exciting. We will demonstrate that this result enables the identification of linear systems from data sets with missing data samples. Additionally, we show that the result is of practical significance in data-driven control of unstable systems.

## Introduction

In the seminal work by Willems and coauthors, it was shown that a single, sufficiently exciting trajectory of a linear system can be used to parameterize *all* trajectories that the system can produce. This result has later been named the *fundamental lemma*, and plays an important role in the learning and control of dynamical systems on the basis of measured data.

An immediate consequence of the fundamental lemma is that a persistently exciting trajectory captures the entire behavior of the data-generating system, thus allowing successful identification of a system model using subspace methods. The lemma also enables data-driven simulation, which involves the computation of the system's response to a given reference input. In addition, Willems' lemma is instrumental in the design of controllers from data....

## Conclusions

Willems *et al.*'s fundamental lemma is a beautiful result that asserts that all trajectories of a linear system can be parameterized by a single, persistently exciting one. In this paper we have extended the fundamental lemma to the scenario where multiple trajectories are given instead of a single one. To this end, we have introduced a notion of collective persistency of excitation. Subsequently, we have shown that all trajectories of a linear system can be parameterized by a finite number of them, assuming these are collectively persistently exciting....

Consider system and assume that the pair $(A,B)$ is controllable. Let $(u_{\lbrack 0,{T_{i} - 1}\rbrack}^{i},x_{\lbrack 0,{T_{i} - 1}\rbrack}^{i},y_{\lbrack 0,{T_{i} - 1}\rbrack}^{i})$ be an input/state/output trajectory of for $i = {1,2,\ldots,q}$. Assume that the inputs $u_{\lbrack 0,{T_{i} - 1}\rbrack}^{i}$ are collectively persistently exciting of order $n + L$. Then the following statements hold:

Next, by the laws of system (1a) we have

## Examples of application

All of the above examples show the value of the fundamental lemma in modeling, simulation and control using a *single* measured system trajectory. Nonetheless, there are many scenarios in which *multiple* system trajectories are measured instead of a single one. For example, performing multiple short experiments becomes desirable when the data-generating system has unstable dynamics....
