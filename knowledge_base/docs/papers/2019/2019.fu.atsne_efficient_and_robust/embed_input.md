<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

AtSNE: Efficient and Robust Visualization on GPU through Hierarchical Optimization

Topics include Dimensionality reduction, Data visualization, Graphics processing unit acceleration, Manifold learning, Hierarchical optimization.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Uses anchor points and hierarchical optimization to preserve global structure while scaling GPU-based visualization to millions of high-dimensional samples.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Visualization of high-dimensional data is a fundamental yet challenging problem in data mining. These visualization techniques are commonly used to reveal the patterns in the high-dimensional data, such as clusters and the similarity among clusters. Recently, some successful visualization tools (e.g., BH-t-SNE and LargeVis) have been developed. However, there are two limitations with them: they cannot capture the global data structure well. Thus, their visualization results are sensitive to initialization, which may cause confusions to the data analysis. They cannot scale to large-scale datasets. They are not suitable to be implemented on the GPU platform because their complex algorithm logic, high memory cost, and random memory access mode will lead to low hardware utilization. To address the aforementioned problems, we propose a novel visualization approach named as Anchor-t-SNE (AtSNE), which provides efficient GPU-based visualization solution for large-scale and high-dimensional data. Specifically, we generate a number of anchor points from the original data and regard them as the skeleton of the layout, which holds the global structure information.

<!-- chunk {"id": "abstract-0004", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

We propose a hierarchical optimization approach to optimize the positions of the anchor points and ordinary data points in the layout simultaneously. Our approach presents much better and robust visual effects on 11 public datasets, and achieve 5 to 28 times speed-up on different datasets, compared with the current state-of-the-art methods. In particular, we deliver a high-quality 2-D layout for a 20 million and 96-dimension dataset within 5 hours, while the current methods fail to give results due to running out of the memory.
