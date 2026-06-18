Robust Principal Component Analysis?

Topics include Robust principal component analysis, Low-rank recovery, Sparse errors, Convex optimization, Principal component pursuit, Matrix decomposition.

Shows that a low-rank matrix corrupted by sparse errors can be exactly recovered by a convex program combining nuclear norm and L1 penalties. This principal-component-pursuit formulation became the standard convex model for robust PCA.

This paper is about a curious phenomenon. Suppose we have a data matrix, which is the superposition of a low-rank component and a sparse component. Can we recover each component individually? We prove that under some suitable assumptions, it is possible to recover both the low-rank and the sparse components exactly by solving a very convenient convex program called Principal Component Pursuit; among all feasible decompositions, simply minimize a weighted combination of the nuclear norm and of the L1 norm. This suggests the possibility of a principled approach to robust principal component analysis since our methodology and results assert that one can recover the principal components of a data matrix even though a positive fraction of its entries are arbitrarily corrupted. This extends to the situation where a fraction of the entries are missing as well.

## Motivation

Suppose we are given a large data matrix $M$, and know that it may be decomposed as

where $L_{0}$ has low-rank and $S_{0}$ is sparse; here, both components are of arbitrary magnitude. We do not know the low-dimensional column and row space of $L_{0}$, not even their dimension. Similarly, we do not know the locations of the nonzero entries of $S_{0}$, not even how many there are. Can we hope to recover the low-rank and sparse components both accurately (perhaps even exactly) and efficiently?

A provably correct and scalable solution to the above problem would presumably have an impact on today's data-intensive scientific discovery.^11^1Data-intensive computing is advocated by Jim Gray as the fourth paradigm for scientific discovery. The recent explosion of massive amounts of high-dimensional data in science, engineering, and society presents a challenge as well as an opportunity to many areas such as image, video, multimedia processing, web relevancy data analysis, search, biomedical imaging and bioinformatics.

## Discussion

This paper delivers some rather surprising news: one can disentangle the low-rank and sparse components exactly by convex programming, and this provably works under very broad conditions that are much broader than those provided by the best known results. Further, our analysis has revealed rather close relationships between matrix completion and matrix recovery (from sparse errors) and our results even generalize to the case when there are both incomplete and corrupted entries (i.e. Theorem 1.2).

Our study so far is limited to the low-rank component being exactly low-rank, and the sparse component being exactly sparse. It would be interesting to investigate when either or both these assumptions are relaxed. One way to think of this is via the new observation model $M = {L_{0} + S_{0} + N_{0}}$, where $N_{0}$ is a dense, small perturbation accounting for the fact that the low-rank component is only approximately low-rank and that small errors can be added to all the entries (in some sense, this model unifies the classical PCA and the robust PCA by combining both sparse gross errors and dense small noise).
