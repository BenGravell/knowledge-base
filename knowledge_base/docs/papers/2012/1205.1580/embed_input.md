Sharp Recovery Bounds for Convex Demixing, with Applications

Topics include Convex demixing, Signal separation, Conic geometry, Sparse recovery, Low-rank recovery, Random orientations, Statistical dimension.

Analyzes a broad convex demixing template for separating structured components from a superposition, using random orientation and incoherence assumptions to turn geometry into sharp phase-transition bounds. Its lasting contribution is the degrees-of-freedom accounting rule: demixing succeeds when the observation dimension exceeds the combined complexity of the constituent structures, with examples covering sparse-basis separation, error correction, and low-rank-plus-sparse decomposition.

Demixing refers to the challenge of identifying two structured signals given only the sum of the two signals and prior information about their structures. Examples include the problem of separating a signal that is sparse with respect to one basis from a signal that is sparse with respect to a second basis, and the problem of decomposing an observed matrix into a low-rank matrix plus a sparse matrix. This paper describes and analyzes a framework, based on convex optimization, for solving these demixing problems, and many others. This work introduces a randomized signal model which ensures that the two structures are incoherent, i.e., generically oriented. For an observation from this model, this approach identifies a summary statistic that reflects the complexity of a particular signal. The difficulty of separating two structured, incoherent signals depends only on the total complexity of the two structures. Some applications include (i) demixing two signals that are sparse in mutually incoherent bases; (ii) decoding spread-spectrum transmissions in the presence of impulsive errors; and (iii) removing sparse corruptions from a low-rank matrix....

## Introduction

In modern data-intensive science, it is common to observe a superposition of multiple information-bearing signals. *Demixing* refers to the challenge of separating out the constituent signals from the observation. A fundamental computational question is to understand when a tractable algorithm can successfully complete the demixing. Problems of this sort arise in fields as diverse as acoustics, astronomy, communications geophysics, image processing machine learning, and statistics. Some well-known examples of convex methods for demixing include morphological component analysis, robust principal component analysis and inpainting.

This work presents a general framework for demixing based on convex optimization. We study the geometry of the optimization problem, and we develop conditions that describe precisely when our method succeeds. Let us illustrate the major aspects of our approach through a concrete example.

: The analysis in this work focuses on a specific random model. It would be interesting to incorporate more general probability measures into our framework. This may be a difficult problem; by the results of Section 5.2, this question is closely related to the observed universality phenomenon in basis pursuit.

*Bayati et al. provide a rigorous version the universality property for basis pursuit observed in. It remains unclear whether their methods adapt to demixing problems considered here.*

then program (4.1) succeeds with overwhelming probability in high dimensions.

The spherical intrinsic volumes of the nonnegative orthant ${\mathbb{R}}_{+}^{d}$ are given by the binomial sequence

### Direct approach

### A first application: Morphological component analysis

Starck et al. use demixing to model the problem of distinguishing stars from galaxies in an astronomical image. This task requires hypotheses on the two types of objects. First, we must assume that stars and galaxies exhibit different kinds of structure: stars appear as localized bright points, while galaxies are wispy or filamented. Second, we must insist that the image is not so full of stars, nor of galaxies, that they obscure one another. These two properties are modeled by the notions of *incoherence* and *sparsity*. With these hypotheses, we can solve the demixing problem using a method known as morphological component analysis (MCA).

### The MCA signal model
