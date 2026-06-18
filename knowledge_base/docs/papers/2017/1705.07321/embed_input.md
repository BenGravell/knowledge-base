Accelerated Hierarchical Density Clustering

Topics include Clustering, Accelerated HDBSCAN.

We present an accelerated algorithm for hierarchical density based clustering. Our new algorithm improves upon HDBSCAN*, which itself provided a significant qualitative improvement over the popular DBSCAN algorithm. The accelerated HDBSCAN* algorithm provides comparable performance to DBSCAN, while supporting variable density clusters, and eliminating the need for the difficult to tune distance scale parameter. This makes accelerated HDBSCAN* the default choice for density based clustering.

## Introduction

Clustering is the attempt to group data in a way that meets with human intuition. Unfortunately, our intuitive ideas of what makes a 'cluster' are poorly defined and highly context sensitive. This results in a plethora of clustering algorithms each of which matches a slightly different intuitive notion of what a natural grouping is.

The major contribution of this paper is section 3, which describes a new algorithm for computing HDBSCAN\* clustering results. This new algorithm, building on the work of March et al. and Curtin et al. offers significant improvements in average case asymptotic performance.

In section 4 we compare the performance of our new HDBSCAN\* algorithm against other clustering algorithms. In particular, we demonstrate the asymptotic performance improvement over the reference HDBSCAN\* algorithm, and show our new algorithm provides HDBSCAN\* with comparable asymptotic performance to DBSCAN, one of the fastest extant clustering algorithms.

## Future work

A number of avenues for significant future work exist. First there are several ways that our current Python implementation could be improved. The effects of approximate nearest neighbor search via spill trees, bounding adjustments, or RP-trees with local neighborhood exploration, both on core-distance computation, and within March's algorithm remains unexplored. Approximate nearest neighbor computations may offer significant performance improvements for a small trade-off in the accuracy of results. Secondly, since there is no cover tree implementation for scikit-learn, our Python implementation does not support cover trees.

A significant weakness of our accelerated HDBSCAN\* algorithm as described is that it is inherently serial. The inability to parallelise the algorithm is an obstacle for its use on large distributed data sets. We believe that partitioning the space via spill trees, and building MSTs on the partitioned data in parallel, then using the techniques of Karger, Klein and Tarjan to reconcile the overlapping trees may result in such a parallel algorithm. This is a topic of continued research.
