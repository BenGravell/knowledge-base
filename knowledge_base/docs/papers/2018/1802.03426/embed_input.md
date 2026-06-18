UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction

Topics include Learning, UMAP.

UMAP (Uniform Manifold Approximation and Projection) is a novel manifold learning technique for dimension reduction. UMAP is constructed from a theoretical framework based in Riemannian geometry and algebraic topology. The result is a practical scalable algorithm that applies to real world data. The UMAP algorithm is competitive with t-SNE for visualization quality, and arguably preserves more of the global structure with superior run time performance. Furthermore, UMAP has no computational restrictions on embedding dimension, making it viable as a general purpose dimension reduction technique for machine learning.

## Introduction

Dimension reduction plays an important role in data science, being a fundamental technique in both visualisation and as pre-processing for machine learning. Dimension reduction techniques are being applied in a broadening range of fields and on ever increasing sizes of datasets. It is thus desirable to have an algorithm that is both scalable to massive data and able to cope with the diversity of data available. Dimension reduction algorithms tend to fall into two categories; those that seek to preserve the pairwise distance structure amongst all the data samples and those that favor the preservation of local distances over global distance.

In this paper we introduce a novel manifold learning technique for dimension reduction. We provide a sound mathematical theory grounding the technique and a practical scalable algorithm that applies to real world data. UMAP (Uniform Manifold Approximation and Projection) builds upon mathematical foundations related to the work of Belkin and Niyogi on Laplacian eigenmaps. We seek to address the issue of uniform data distributions on manifolds through a combination of Riemannian geometry and the work of David Spivak in category theoretic approaches to geometric realization of fuzzy simplicial sets.

This paper is laid out as follows. In Section 2 we describe the theory underlying the algorithm. Section 2 is necessary to understand both the theory underlying why UMAP works and the motivation for the choices that where made in developing the algorithm. A reader without a background (or interest) in topological data analysis, category theory or the theoretical underpinnings of UMAP should skip over this section and proceed directly to Section 3.

## Future Work

Having established both relevant mathematical theory and a concrete implementation, there still remains significant scope for future developments of UMAP.

A comprehensive empirical study which examines the impact of the various algorithmic components, choices, and hyper-parameters of the algorithm would be beneficial. While the structure and choices of the algorithm presented were derived from our foundational mathematical framework, examining the impacts that these choices have on practical results would be enlightening and a significant contribution to the literature.
