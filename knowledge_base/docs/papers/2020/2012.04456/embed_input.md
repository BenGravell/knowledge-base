Understanding How Dimension Reduction Tools Work: An Empirical Approach to Deciphering t-SNE, UMAP, TriMAP, and PaCMAP for Data Visualization

Topics include Datasets, Control, Dimension reduction, DR.

Dimension reduction (DR) techniques such as t-SNE, UMAP, and TriMAP have demonstrated impressive visualization performance on many real world datasets. One tension that has always faced these methods is the trade-off between preservation of global structure and preservation of local structure: these methods can either handle one or the other, but not both. In this work, our main goal is to understand what aspects of DR methods are important for preserving both local and global structure: it is difficult to design a better method without a true understanding of the choices we make in our algorithms and their empirical impact on the lower-dimensional embeddings they produce. Towards the goal of local structure preservation, we provide several useful design principles for DR loss functions based on our new understanding of the mechanisms behind successful DR methods. Towards the goal of global structure preservation, our analysis illuminates that the choice of which components to preserve is important. We leverage these insights to design a new algorithm for DR, called Pairwise Controlled Manifold Approximation Projection (PaCMAP), which preserves both local and global structure.

## Introduction

Dimension reduction (DR) tools for data visualization can act as either a blessing or a curse in understanding the geometric and neighborhood structures of datasets. Being able to visualize the data can provide an understanding of cluster structure or provide an intuition of distributional characteristics. On the other hand, it is well-known that DR results can be misleading, displaying cluster structures that are simply not present in the original data, or showing observations to be far from each other in the projected space when they are actually close in the original space.

Without an understanding of the algorithms' loss functions and what aspects of them have an impact on the embedding, it is difficult to substantially improve upon them. Similarly, without an understanding of other choices made within these algorithms, it becomes hard to navigate adjustments of their parameters. Hence, we ask: What aspects of the various loss functions for different algorithms are important? Is there a not-very-complicated loss function that allows us to handle both local and global structure in a unified way?

The loss function controls the attractive and repulsive forces between each pair of data points. In Section 4, we focus on deciphering general principles of a good loss function. We show how UMAP and other algorithms obey these principles, and show empirically why deviating from these principles ruins the DR performance. We also introduce a simple loss function obeying our principles. This new loss function is used in an algorithm called Pairwise Controlled Manifold Approximation Projection (PaCMAP) introduced in this work.

Throughout, we also discuss other aspects of DR algorithms. For example, in Section 6, we show that initialization and scaling can be important, in fact, we show that TriMap's ability to preserve global structure comes from an unexpected source, namely its initialization.

## Discussion and Conclusion

In this study, our goal was to empirically dissect what approaches to dimension reduction work and what do not, using a selection of datasets for which local- and global-structure preservation needs are different, and where the algorithms could be visually evaluated after projecting to two dimensions.
