UMAP: Uniform Manifold Approximation and Projection for Dimension Reduction

Topics include Learning, UMAP.

UMAP (Uniform Manifold Approximation and Projection) is a novel manifold learning technique for dimension reduction. UMAP is constructed from a theoretical framework based in Riemannian geometry and algebraic topology. The result is a practical scalable algorithm that applies to real world data. The UMAP algorithm is competitive with t-SNE for visualization quality, and arguably preserves more of the global structure with superior run time performance. Furthermore, UMAP has no computational restrictions on embedding dimension, making it viable as a general purpose dimension reduction technique for machine learning.

## Introduction

Dimension reduction plays an important role in data science, being a fundamental technique in both visualisation and as pre-processing for machine learning. Dimension reduction techniques are being applied in a broadening range of fields and on ever increasing sizes of datasets. It is thus desirable to have an algorithm that is both scalable to massive data and able to cope with the diversity of data available....

In this paper we introduce a novel manifold learning technique for dimension reduction. We provide a sound mathematical theory grounding the technique and a practical scalable algorithm that applies to real world data. UMAP (Uniform Manifold Approximation and Projection) builds upon mathematical foundations related to the work of Belkin and Niyogi on Laplacian eigenmaps. We seek to address the issue of uniform data distributions on manifolds through a combination of Riemannian geometry and the work of David Spivak in category theoretic approaches to geometric realization of fuzzy simplicial sets....

## Conclusions

We have developed a general purpose dimension reduction technique that is grounded in strong mathematical foundations. The algorithm implementing this technique is demonstrably faster than t-SNE and provides better scaling. This allows us to generate high quality embeddings of larger data sets than had previously been attainable. The use and effectiveness of UMAP in various scientific fields demonstrates the strength of the algorithm.

## Construct the relevant weighted graph
top-rep ← ⋃x ∈ Xfs-set [x] # We recommend the probabilistic t-conorm

We note that in this case we restricted attention to comparisons of the 1-skeleton of the fuzzy simplicial sets. One can extend this to $\ell$-skeleta by defining a cost function $C_{\ell}$ as

Figure 3: Variation of UMAP hyperparameters n and min-dist result in different embeddings. The data is the MNIST dataset, where each point is an 28x28 grayscale image of a hand-written digit.

Based upon preliminary releases of a software implementation, UMAP has already found widespread use in the fields of bioinformatics, materials science, and machine learning among others.

This paper is laid out as follows. In Section 2 we describe the theory underlying the algorithm. Section 2 is necessary to understand both the theory underlying why UMAP works and the motivation for the...
