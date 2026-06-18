<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

Accelerating t-SNE Using Tree-Based Algorithms

<!-- chunk {"id": "abstract-0002", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

The paper investigates the acceleration of t-SNE - an embedding technique that is commonly used for the visualization of high- dimensional data in scatter plots - using two tree-based algorithms. In particular, the paper develops variants of the Barnes-Hut algorithm and of the dual-tree algorithm that approximate the gradient used for learning t-SNE embeddings in O(NlogN). Our experiments show that the resulting algorithms substantially accelerate t-SNE, and that they make it possible to learn embeddings of data sets with millions of objects. Somewhat counterintuitively, the Barnes-Hut variant of t-SNE appears to outperform the dual-tree variant.
