Sensor Placement for Optimal Kalman Filtering: Fundamental Limits, Submodularity, and Algorithms

In this paper, we focus on sensor placement in linear dynamic estimation, where the objective is to place a small number of sensors in a system of interdependent states so to design an estimator with a desired estimation performance. In particular, we consider a linear time-variant system that is corrupted with process and measurement noise, and study how the selection of its sensors affects the estimation error of the corresponding Kalman filter over a finite observation interval. Our contributions are threefold: First, we prove that the minimum mean square error of the Kalman filter decreases only linearly as the number of sensors increases. That is, adding extra sensors so to reduce this estimation error is ineffective, a fundamental design limit. Similarly, we prove that the number of sensors grows linearly with the system's size for fixed minimum mean square error and number of output measurements over an observation interval; this is another fundamental limit, especially for systems where the system's size is large....

## Introduction

In this paper, we aim to monitor dynamic, interdependent phenomena, that is, phenomena with temporal and spatial correlations ---with the term "spatial" we refer to any kind of interdependencies between the phenomena. For example, the temperature at any point of an indoor environment depends across time ---temporal correlation--- on the temperatures of the adjacent points ---spatial correlation....

Specifically, we consider phenomena modelled as a linear time-variant system that is corrupted with process and measurement noise, and study how the selection of its sensors affect the minimum mean square error of the corresponding Kalman filter. To this end, we consider that each of the sensors measures a single state of the system. Thereby, this study is an important distinction in the sensor placement literature in linear systems, since the Kalman filter is the optimal linear estimator ---in the minimum mean square sense--- given a sensor set....

## Concluding Remarks

We considered a linear time-variant system and studied the properties of its Kalman estimator given an observation interval $\lbrack 0,k\rbrack$ and a sensor set $\mathcal{S}$. Our contributions were threefold. First, in Section III we presented several design and performance limits. For example, we proved that the cardinality of the selected sensors $\mathcal{S}$ grows linearly with the system's size for fixed minimum mean square estimation error and $k$....

A function $h:{2^{\lbrack n\rbrack}\mapsto{\mathbb{R}}}$ is *supermodular* if $({- h})$ is submodular.

Given an observation interval $\lbrack 0,k\rbrack$, identify a sensor set $\mathcal{S}$ that solves either the *minimal sensor placement problem:*

The following greedy algorithm has been proposed for its approximate solution, for which, the subsequent fact is true.

First, we identify fundamental limits in the design of the Kalman filter with respect to its sensors. In particular, given a fixed number of output measurements over an observation interval, we prove among others that the number of sensors grows linearly with the system's size for fixed minimum mean square error ---this is a design limit, especially for complex systems where the system's size is large....

These results are the first to characterize the effect of the sensor set on the minimum mean square error of the Kalman filter....
