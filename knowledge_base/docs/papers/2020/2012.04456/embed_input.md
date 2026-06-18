Understanding How Dimension Reduction Tools Work: An Empirical Approach to Deciphering t-SNE, UMAP, TriMAP, and PaCMAP for Data Visualization

Topics include Datasets, Control, Dimension reduction, DR.

Dimension reduction (DR) techniques such as t-SNE, UMAP, and TriMAP have demonstrated impressive visualization performance on many real world datasets. One tension that has always faced these methods is the trade-off between preservation of global structure and preservation of local structure: these methods can either handle one or the other, but not both. In this work, our main goal is to understand what aspects of DR methods are important for preserving both local and global structure: it is difficult to design a better method without a true understanding of the choices we make in our algorithms and their empirical impact on the lower-dimensional embeddings they produce. Towards the goal of local structure preservation, we provide several useful design principles for DR loss functions based on our new understanding of the mechanisms behind successful DR methods. Towards the goal of global structure preservation, our analysis illuminates that the choice of which components to preserve is important. We leverage these insights to design a new algorithm for DR, called Pairwise Controlled Manifold Approximation Projection (PaCMAP), which preserves both local and global structure....

## Introduction

Dimension reduction (DR) tools for data visualization can act as either a blessing or a curse in understanding the geometric and neighborhood structures of datasets. Being able to visualize the data can provide an understanding of cluster structure or provide an intuition of distributional characteristics. On the other hand, it is well-known that DR results can be misleading, displaying cluster structures that are simply not present in the original data, or showing observations to be far from each other in the projected space when they are actually close in the original space....

The goal of this work is to decipher these algorithms, and why they work or don't work. We study and compare several leading algorithms, in particular, t-SNE, UMAP, and TriMap. Each of these algorithms is subject to different limitations. For instance, t-SNE can be very sensitive to the perplexity parameter and creates spurious clusters; both t-SNE and UMAP perform beautifully in preserving local structure but struggle to preserve global structure....

The qualitative performance results we examine for PaCMAP led directly to high-quality quantitative results measured on 12 datasets.

There are many avenues for future work. First, one could consider the possibility of a continuum between local and global structure. While considering a simple dichotomy between local and global has been convenient, it is possible that the data contains multi-scale or hierarchical structure at many levels. We provide an analysis of a simple synthetic dataset with hierarchical structure in Appendix B, where all methods have difficulty displaying structure on all levels of the hierarchy (although PaCMAP slightly outperforms other methods)....

Figure 8: 2D line dataset (left), and a projection also onto 2D that respects local structure but not global structure (right). The right curve (created using UMAP) would achieve perfect (zero) 0-1 triplet loss, as long as all triplets contain a nearby unit.

Except in the bottom area of the rainbow figures (where $d_{ik}$ is small), the gradient of the loss should go mainly to the left. If $d_{ik}$ is not too small (assuming that the further point $k$ is sufficiently far from $i$), we no longer encourage it to be even larger, and focus on minimizing $d_{ij}$....
