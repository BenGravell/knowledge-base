The Achievable Performance of Convex Demixing

Topics include Convex demixing, Conic geometry, Statistical dimension, Signal separation, Phase transitions, Noisy observations, Structured recovery.

Generalizes convex demixing analysis to superimposed, undersampled, and noisy observations, emphasizing the achievable limits of convex programs under generic incoherence. The central takeaway is geometric: each structure contributes an intrinsic degrees-of-freedom term, and convex demixing succeeds essentially when the measurement dimension exceeds the sum of those terms, giving a precise benchmark for what convex separation can and cannot recover.

Demixing is the problem of identifying multiple structured signals from a superimposed, undersampled, and noisy observation. This work analyzes a general framework, based on convex optimization, for solving demixing problems. When the constituent signals follow a generic incoherence model, this analysis leads to precise recovery guarantees. These results admit an attractive interpretation: each signal possesses an intrinsic degrees-of-freedom parameter, and demixing can succeed if and only if the dimension of the observation exceeds the total degrees of freedom present in the observation.

## Introduction

Demixing refers to the problem of extracting multiple informative signals from a single, possibly noisy and undersampled, observation. One rather general model for a mixed observation ${\mathbf{z}}_{0} \in {\mathbb{R}}^{\gtrdot}$ takes the form

where the constituents ${({\mathbf{x}}_{i}^{\natural})}_{i = 1}^{n}$ are the unknown informative signals that we wish to find; the matrices ${({\mathbf{U}}_{i})}_{i = 1}^{n}$ model the relative orientation of the constituent vectors; the operator ${\mathbf{A}} \in {\mathbb{R}}^{\gtrdot \times}$ compresses the observation from $d$ dimensions to $m \leq d$ dimensions; and ${\mathbf{w}} \in {\mathbb{R}}$ is unstructured noise. We assume that all elements appearing in (1.1) are known except for the constituents ${({\mathbf{x}}_{i}^{\natural})}_{i = 1}^{n}$ and the noise $\mathbf{w}$.

Numerous applications of the model (1.1) appear in modern data-intensive science. In imaging, for example, the informative signals can model features like stars and galaxies, while an undersampling operator accounts for known occlusions or missing data. In graphical model selection, the data may consist of the sum of a sparse component that encodes causality structure and a confounding low-rank component that arises from unobserved latent variables. Similar mixed-signal models appear in robust statistics and image processing \[PGW^+^12, \]. In every case, the question of interest is

This work answers this question for a popular class of demixing procedures under a random model. The analysis reveals that each constituent possesses a degrees-of-freedom parameter, and that these demixing procedures can succeed with high probability if and only if the total number of measurements exceeds the total degrees of freedom.
