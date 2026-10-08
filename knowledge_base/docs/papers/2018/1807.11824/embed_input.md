<!-- embedding-input:v1 -->

<!-- chunk {"id": "metadata-0001", "role": "metadata", "section": "Metadata", "weight": 3.0} -->

t-SNE-CUDA: GPU-Accelerated t-SNE and Its Applications to Modern Data

Topics include Dimensionality reduction, Data visualization, Graphics processing unit acceleration, Neural network embeddings, Scalability.

<!-- chunk {"id": "summary-0002", "role": "summary", "section": "Summary", "weight": 2.0} -->

Accelerates t-SNE on GPUs to visualize large datasets and neural-network embeddings, demonstrating substantial speedups and ImageNet-scale activation visualization.

<!-- chunk {"id": "abstract-0003", "role": "abstract", "section": "Abstract", "weight": 2.0} -->

Modern datasets and models are notoriously difficult to explore and analyze due to their inherent high dimensionality and massive numbers of samples. Existing visualization methods which employ dimensionality reduction to two or three dimensions are often inefficient and/or ineffective for these datasets. This paper introduces t-SNE-CUDA, a GPU-accelerated implementation of t-distributed Symmetric Neighbor Embedding (t-SNE) for visualizing datasets and models. t-SNE-CUDA significantly outperforms current implementations with 50-700x speedups on the CIFAR-10 and MNIST datasets. These speedups enable, for the first time, visualization of the neural network activations on the entire ImageNet dataset - a feat that was previously computationally intractable. We also demonstrate visualization performance in the NLP domain by visualizing the GloVe embedding vectors. From these visualizations, we can draw interesting conclusions about using the L2 metric in these embedding spaces. t-SNE-CUDA is publicly available at
