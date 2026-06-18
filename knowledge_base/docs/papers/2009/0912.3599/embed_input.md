Robust Principal Component Analysis?

Topics include Robust principal component analysis, Low-rank recovery, Sparse errors, Convex optimization, Principal component pursuit, Matrix decomposition.

Shows that a low-rank matrix corrupted by sparse errors can be exactly recovered by a convex program combining nuclear norm and L1 penalties. This principal-component-pursuit formulation became the standard convex model for robust PCA.

This paper is about a curious phenomenon. Suppose we have a data matrix, which is the superposition of a low-rank component and a sparse component. Can we recover each component individually? We prove that under some suitable assumptions, it is possible to recover both the low-rank and the sparse components exactly by solving a very convenient convex program called Principal Component Pursuit; among all feasible decompositions, simply minimize a weighted combination of the nuclear norm and of the L1 norm. This suggests the possibility of a principled approach to robust principal component analysis since our methodology and results assert that one can recover the principal components of a data matrix even though a positive fraction of its entries are arbitrarily corrupted. This extends to the situation where a fraction of the entries are missing as well....

## Introduction

### Motivation

Suppose we are given a large data matrix $M$, and know that it may be decomposed as

where $\mathcal{A},\mathcal{B},\mathcal{C}$ are known linear maps. An ambitious goal might be to understand exactly under what conditions, one can effectively retrieve or decompose $L_{0}$ and $S_{0}$ from such noisy linear measurements via convex programming.

The remarkable ability of convex optimizations in recovering low-rank matrices and sparse signals in high-dimensional spaces suggest that they will be a powerful tool for processing massive data sets that arise in image/video processing, web data analysis, and bioinformatics. Such data are often of millions or even billions of dimensions so the computational and memory cost can be far beyond that of a typical PC. Thus, one important direction for future investigation is to develop algorithms that have even better scalability, and can be easily implemented on the emerging parallel and distributed computing infrastructures.

We now propose constructing a dual certificate

We begin with a useful definition and an elementary result we shall use a few times.

by Theorem 2.6. In particular, this gives that with high probability

where $L_{0}$ has low-rank and $S_{0}$ is sparse; here, both components are of arbitrary magnitude. We do not know the low-dimensional column and row space of $L_{0}$, not even their dimension. Similarly, we do not know the locations of the nonzero entries of $S_{0}$, not even how many there are. Can we hope to recover the low-rank and sparse components both accurately (perhaps even exactly) and efficiently?

A provably correct and scalable solution to the above problem would presumably have an impact on today's data-intensive scientific discovery.^11^1Data-intensive computing is advocated by Jim Gray as the fourth paradigm for scientific discovery. The recent explosion of massive amounts of high-dimensional data in science, engineering, and society presents a challenge as well as an opportunity to many areas such as image, video, multimedia processing, web relevancy data analysis, search, biomedical imaging and bioinformatics....

To alleviate the curse of dimensionality and scale,^22^2We refer to either the complexity of algorithms that increases drastically as dimension increases, or to their performance that decreases sharply when scale goes up....
