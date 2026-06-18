Random Fourier Features for Kernel Ridge Regression: Approximation Bounds and Statistical Guarantees

Topics include Regression, Datasets, Sampling, Random fourier features, Kernel methods.

Random Fourier features is one of the most popular techniques for scaling up kernel methods, such as kernel ridge regression. However, despite impressive empirical results, the statistical properties of random Fourier features are still not well understood. In this paper we take steps toward filling this gap. Specifically, we approach random Fourier features from a spectral matrix approximation point of view, give tight bounds on the number of Fourier features required to achieve a spectral approximation, and show how spectral matrix approximation bounds imply statistical guarantees for kernel ridge regression. Qualitatively, our results are twofold: on the one hand, we show that random Fourier feature approximation can provably speed up kernel ridge regression under reasonable assumptions. At the same time, we show that the method is suboptimal, and sampling from a modified distribution in Fourier space, given by the leverage function of the kernel, yields provably better performance. We study this optimal sampling distribution for the Gaussian kernel, achieving a nearly complete characterization for the case of low-dimensional bounded datasets.

## Introduction

Kernel methods constitute a powerful paradigm for devising non-parametric modeling techniques for a wide range of problems in machine learning. One of the most elementary is Kernel Ridge Regression (KRR).

In the above, $\mathbf{K} \in {\mathbb{R}}^{n \times n}$ is the kernel matrix or Gram matrix defined by $\mathbf{K}_{ij} \equiv {k{(\mathbf{x}_{i},\mathbf{x}_{j})}}$ and $\mathbf{y} \equiv {\lbrack{y_{1}\cdotsy_{n}}\rbrack}^{\text{T}}$ is the vector of responses. The KRR estimator can be derived by minimizing a regularized square loss objective function over a hypothesis space defined by the reproducing kernel Hilbert space associated with $k{( \cdot, \cdot )}$; however, the details are not important for this paper.

While simple, KRR is a powerful technique that is well understood statistically and capable of achieving impressive empirical results. Nevertheless, the method has a key weakness: computing the KRR estimator can be prohibitively expensive for large datasets. Solving (1 [AKM+17].")) generally requires $\Theta{(n^{3})}$ time^22^2The running time can be improved using fast matrix products. However fast matrix products are typically not employed in practice due to large hidden constants. and $\Theta{(n^{2})}$ memory.

naturally have statistical and algorithmic implications. Indeed, in §3 [AKM+17].") we show that when (2 [AKM+17].")) holds we can bound the excess risk introduced by the random Fourier features estimator when compared to the KRR estimator. We also show that $\overset{\sim}{\mathbf{K}} + {\lambda\mathbf{I}_{n}}$ can be used as an effective preconditioner for the solution of (1 [AKM+17].")). This motivates the study of how large $s$ should be as a function of $\Delta$ for (2 [AKM+17].")) to hold.

In this paper we rigorously analyze the relation between the number of random Fourier features and the spectral approximation bound (2 [AKM+17].")).

We show that the upper bound can be improved dramatically by modifying the sampling distribution used in classical random Fourier features (§4 [AKM+17].")). Our sampling distribution is based on an appropriately defined leverage function of the kernel, closely related to so-called leverage scores frequently encountered in the analysis of sampling based methods for linear regression. Unfortunately, it is unclear how to efficiently sample using the leverage function.
