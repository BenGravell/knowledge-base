Accelerated Hierarchical Density Clustering

Topics include Clustering, Accelerated HDBSCAN.

We present an accelerated algorithm for hierarchical density based clustering. Our new algorithm improves upon HDBSCAN*, which itself provided a significant qualitative improvement over the popular DBSCAN algorithm. The accelerated HDBSCAN* algorithm provides comparable performance to DBSCAN, while supporting variable density clusters, and eliminating the need for the difficult to tune distance scale parameter. This makes accelerated HDBSCAN* the default choice for density based clustering. Library available at:

## Introduction

Clustering is the attempt to group data in a way that meets with human intuition. Unfortunately, our intuitive ideas of what makes a 'cluster' are poorly defined and highly context sensitive. This results in a plethora of clustering algorithms each of which matches a slightly different intuitive notion of what a natural grouping is.

Despite the uncertainty underlying the clustering process it continues to be used in a multitude of scientific domains. The fundamental problem of finding groupings is pervasive and results, however poor, are still important and informative. It is used in diverse fields such as molecular dynamics, airplane flight path analysis, crystallography, and social analytics, among many others.

## Conclusions

The HDBSCAN\* clustering algorithm lies at the confluence of several threads of research from diverse fields. As a density based algorithm with a small number of intuitive parameters and few assumptions about data distribution, it is ideally suited to exploratory data analysis. In this paper we have described an accelerated HDBSCAN\* algorithm that can provide comparable performance to the popular DBSCAN clustering algorithm. Since it has more intuitive parameters and can find variable density clusters, HDBSCAN\* is clearly superior to DBSCAN from a qualitative clustering perspective....

The computation of core-distances is a query for the $k^{\text{th}}$ nearest neighbor of each point in the input data set. The use of space tree algorithms for efficient nearest neighbor computations is well established. In particular kd-trees in euclidean space, and ball-trees or cover trees for generic metric spaces, provide fast asymptotic performance for nearest neighbor computation. Strict asymptotic run-time bounds for such algorithms are often complicated by properties of the data set....

subject to the constraint that, for all ${i,j} \in I$ with $i \neq j$, we have

With this is mind, the BaseCase (algorithm 3) needs to find points in different components that have a shorter distance separating them than the current value stored for the component under consideration. If such a pair is found we update $\mathcal{N}$, $\mathcal{P}$ and $\mathcal{D}$ accordingly.

While clustering has many uses to many people, our particular focus is on clustering for the purpose of exploratory data analysis....
