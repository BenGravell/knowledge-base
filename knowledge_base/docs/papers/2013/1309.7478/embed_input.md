The Achievable Performance of Convex Demixing

Topics include Convex demixing, Conic geometry, Statistical dimension, Signal separation, Phase transitions, Noisy observations, Structured recovery.

Generalizes convex demixing analysis to superimposed, undersampled, and noisy observations, emphasizing the achievable limits of convex programs under generic incoherence. The central takeaway is geometric: each structure contributes an intrinsic degrees-of-freedom term, and convex demixing succeeds essentially when the measurement dimension exceeds the sum of those terms, giving a precise benchmark for what convex separation can and cannot recover.

Demixing is the problem of identifying multiple structured signals from a superimposed, undersampled, and noisy observation. This work analyzes a general framework, based on convex optimization, for solving demixing problems. When the constituent signals follow a generic incoherence model, this analysis leads to precise recovery guarantees. These results admit an attractive interpretation: each signal possesses an intrinsic degrees-of-freedom parameter, and demixing can succeed if and only if the dimension of the observation exceeds the total degrees of freedom present in the observation.

## Introduction

Demixing refers to the problem of extracting multiple informative signals from a single, possibly noisy and undersampled, observation. One rather general model for a mixed observation ${\mathbf{z}}_{0} \in {\mathbb{R}}^{\gtrdot}$ takes the form

where the constituents ${({\mathbf{x}}_{i}^{\natural})}_{i = 1}^{n}$ are the unknown informative signals that we wish to find; the matrices ${({\mathbf{U}}_{i})}_{i = 1}^{n}$ model the relative orientation of the constituent vectors; the operator ${\mathbf{A}} \in {\mathbb{R}}^{\gtrdot \times}$ compresses the observation from $d$ dimensions to $m \leq d$ dimensions; and ${\mathbf{w}} \in {\mathbb{R}}$ is unstructured noise. We assume that all elements appearing in (1.1) are known except for the constituents ${({\mathbf{x}}_{i}^{\natural})}_{i = 1}^{n}$ and the noise $\mathbf{w}$.

: Our numerical experience indicates that the incoherence model considered in this work is predictive for highly incoherent situations. However, these results appear overly optimistic in more coherent situations. The difference between these situations appears, for example, in an application to calcium imaging \[, Fig. 3\]. Extending our results to other incoherence models will clarify where the phase transition in Theorem A predicts empirical performance, and where it does not.

: For practical applications of this work, we require accurate statistical dimension calculations. A recipe for these computations put forward in \[\] has provable guarantees under some technical conditions (cf. \[, Sec. 4.4\] and \[, Prop. 1\]), but expressions for the statistical dimension of a number of important convex regularizers remains unknown. New statistical dimension computations immediately extend the reach of the methods used in this paper.

Early work on demixing methods used the $\ell_{1}$ norm to encourage sparsity. Taylor, Banks, & McCoy \[\] used (1.2) with $\left. f_{1} = f_{2} = \parallel \cdot \parallel{}_{\ell_{1}} \right.$ to demix a sparse signal from sparse noise, with applications to geophysics. About ten years later, Donoho & Stark \[\] explained how uncertainty principles can guarantee the success of demixing signals that are sparse in frequency from those that are sparse in time using the $\ell_{1}$ norm.
