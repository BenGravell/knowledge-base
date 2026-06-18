<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Density-Based Clustering Based on Hierarchical Density Estimates

Topics include HDBSCAN, Density-based clustering, Hierarchical clustering, Cluster stability, DBSCAN, Outlier detection, Unsupervised learning.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Introduces the HDBSCAN clustering idea: build a density-based hierarchy, then extract a flat clustering by selecting the most stable clusters rather than fixing a single density threshold. The contribution is both theoretical and practical, because the stability objective gives a principled way to summarize the hierarchy and often outperforms DBSCAN and OPTICS-style methods on datasets with variable cluster density.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a theoretically and practically improved density-based, hierarchical clustering method, providing a clustering hierarchy from which a simplified tree of significant clusters can be constructed. For obtaining a “flat” partition consisting of only the most significant clusters (possibly corresponding to different density thresholds), we propose a novel cluster stability measure, formalize the problem of maximizing the overall stability of selected clusters, and formulate an algorithm that computes an optimal solution to this problem. We demonstrate that our approach outperforms the current, state-of-the-art, density-based clustering methods on a wide variety of real world data.
